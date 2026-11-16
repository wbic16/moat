#!/usr/bin/env python3
"""tluf-submit — the receiving service for tluf.org paper submissions.

Minimal by design (Assay REQUIREMENTS.md: submission is open; assessment
and merge are gated house acts this service does not perform). It only
receives: POST /api/submit validates a locator, derives its canonical
px2 address per ~/workspace/oracle-service/ADDRESSING.md (the server's
derivation is authoritative), and appends the submission as one file in
~/tluf-submissions/ (mailbox pattern). GET /api/health answers liveness.

Python 3 standard library only. Listens on loopback; nginx proxies the
public /api/submit and /api/health paths to it (see install-submit.sh).

Usage:
    tluf-submit.py                 run the server (127.0.0.1:8643)
    tluf-submit.py --canon LOCATOR print the canonical address or error
"""

import json
import os
import re
import sys
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import quote, unquote, urlsplit

# --------------------------------------------------------------------------
# Canonicalization — ADDRESSING.md §4-§6. The spec governs; this is a
# transcription. The submit page's JavaScript is a second transcription
# of the same section; both are tested against §7's worked examples.
# --------------------------------------------------------------------------

TRACKING_KEYS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_cid", "mc_eid",
}
UNRESERVED = set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~")

MODERN_ID = r"\d{4}\.\d{4,5}"
OLDSTYLE_ID = r"[a-z][a-z-]*(\.[A-Z]{2})?/\d{7}"


def _strip_sentence_punct(s):
    """ADDRESSING.md §4.1 step 4: one clinging '.' or ',' is stripped."""
    if s and s[-1] in ".,":
        return s[:-1]
    return s


def _drop_version(id_text):
    """§4.3: a repository version suffix is not an edition pin."""
    return re.sub(r"v\d+$", "", id_text)


def _canon_arxiv(id_text):
    s = _drop_version(_strip_sentence_punct(id_text.strip()))
    if s.lower().endswith(".pdf"):
        s = s[:-4]
    if re.fullmatch(MODERN_ID, s) or re.fullmatch(OLDSTYLE_ID, s):
        return "px2:arxiv:" + s
    return None


def _canon_doi(id_text):
    s = id_text.strip()
    if "doi.org/" in s:  # a resolver URL pasted after a doi: prefix
        s = s.split("doi.org/", 1)[1]
    s = _strip_sentence_punct(unquote(s)).lower()
    if re.fullmatch(r"10\.\d{4,9}/\S+", s):
        return "px2:doi:" + s
    return None


def _canon_repo(kind, id_text):
    s = _drop_version(_strip_sentence_punct(id_text.strip()))
    if re.fullmatch(MODERN_ID, s):
        return "px2:%s:%s" % (kind, s)
    return None


def _normalize_pct(s):
    """§6.2 step 2: decode unreserved, uppercase the rest."""
    def rep(m):
        ch = chr(int(m.group(1), 16))
        if ch in UNRESERVED:
            return ch
        return "%" + m.group(1).upper()
    return re.sub(r"%([0-9A-Fa-f]{2})", rep, s)


def _remove_dot_segments(path):
    """§6.2 step 3 (RFC 3986 §5.2.4, simplified to segment handling)."""
    out = []
    for seg in path.split("/"):
        if seg == ".":
            continue
        if seg == "..":
            if out:
                out.pop()
            continue
        out.append(seg)
    res = "/".join(out)
    if path.startswith("/") and not res.startswith("/"):
        res = "/" + res
    return res


def _canon_url(raw):
    """§6.2: canonicalize a web URL into a px2:url: address."""
    if "://" not in raw:
        raw = "https://" + raw
    parts = urlsplit(raw)
    scheme = parts.scheme.lower()
    if scheme not in ("http", "https"):
        return None
    host = (parts.hostname or "").lower()
    if not host:
        return None
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        return None
    netloc = host
    if port and not ((scheme == "http" and port == 80)
                     or (scheme == "https" and port == 443)):
        netloc = "%s:%d" % (host, port)
    path = _remove_dot_segments(_normalize_pct(parts.path))
    if path == "/":
        path = ""
    elif path.endswith("/") and len(path) > 1:
        path = path[:-1]
    pairs = []
    if parts.query:
        for pair in parts.query.split("&"):
            if not pair:
                continue
            if "=" in pair:
                k, v = pair.split("=", 1)
            else:
                k, v = pair, ""
            kd = unquote(k)
            if kd.lower() in TRACKING_KEYS:
                continue
            pairs.append((kd, unquote(v)))
        pairs.sort(key=lambda kv: (kv[0], kv[1]))
    query = "&".join(
        quote(k, safe="") + "=" + quote(v, safe="") if v != ""
        else quote(k, safe="") for k, v in pairs)
    url = "%s://%s%s" % (scheme, netloc, path)
    if query:
        url += "?" + query
    if "@e:" in url:  # §6.2 step 7 / gap G-1
        url = url.replace("@e:", "%40e:")
    return "px2:url:" + url


def _by_kind(kind, rest):
    if kind == "arxiv":
        return _canon_arxiv(rest)
    if kind == "doi":
        return _canon_doi(rest)
    if kind in ("hexagon", "vixra"):
        return _canon_repo(kind, rest)
    return None


def _canon_url_dispatch(s):
    """Route a URL-shaped locator: repository hosts first, else url:."""
    raw = s if "://" in s else "https://" + s
    parts = urlsplit(raw)
    host = (parts.hostname or "").lower()
    bare = host[4:] if host.startswith("www.") else host
    path = parts.path
    if bare == "arxiv.org":
        m = re.search(r"/(?:abs|pdf)/(.+)$", path)
        if m:
            addr = _canon_arxiv(unquote(m.group(1)))
            return (addr, None) if addr else (None, "MALFORMED")
        return None, "MALFORMED"
    if bare in ("doi.org", "dx.doi.org"):
        addr = _canon_doi(unquote(path.lstrip("/")))
        return (addr, None) if addr else (None, "MALFORMED")
    if bare == "vixra.org":
        m = re.search(r"/abs/(.+)$", path)
        if m:
            addr = _canon_repo("vixra", unquote(m.group(1)))
            return (addr, None) if addr else (None, "MALFORMED")
        return None, "MALFORMED"
    if bare == "hexagonmath.org":
        seg = path.rstrip("/").rsplit("/", 1)[-1]
        addr = _canon_repo("hexagon", unquote(seg))
        return (addr, None) if addr else (None, "MALFORMED")
    addr = _canon_url(s)
    return (addr, None) if addr else (None, "MALFORMED")


def _canon_px2(s):
    """A pasted px2: address is parsed per §2 and re-emitted canonically."""
    body = s[4:]
    head, hashmark, tail = body.partition("#")
    if head.startswith("sum:"):
        m = re.fullmatch(r"sum:xxh3-128:([0-9A-Fa-f]{32})", head)
        if not m:
            return None, "MALFORMED"
        out = "px2:sum:xxh3-128:" + m.group(1).lower()
    else:
        pin = ""
        if "@e:" in head:
            head, _, pinval = head.rpartition("@e:")
            if not re.fullmatch(r"[0-9A-Fa-f]{16,}", pinval):
                return None, "MALFORMED"
            pin = "@e:" + pinval.lower()
        token, colon, rest = head.partition(":")
        token = token.lower()
        if not colon:
            return None, "MALFORMED"
        if token == "corpus":
            if not re.fullmatch(r"[a-z][a-z0-9-]*", rest):
                return None, "MALFORMED"
            out = "px2:corpus:" + rest
        elif token == "tluf":
            if not re.fullmatch(r"[0-9a-f]{16}", rest.lower()):
                return None, "MALFORMED"
            out = "px2:tluf:" + rest.lower()
        elif token in ("arxiv", "doi", "hexagon", "vixra"):
            addr = _by_kind(token, rest)
            if not addr:
                return None, "MALFORMED"
            out = addr
        elif token == "url":
            addr = _canon_url(rest)
            if not addr:
                return None, "MALFORMED"
            out = addr
        else:
            return None, "MALFORMED"
        out += pin
    if hashmark:
        if not re.fullmatch(r"[a-z][a-z0-9-]*:[a-z][a-z0-9-]*", tail):
            return None, "MALFORMED"
        out += "#" + tail
    return out, None


def canonicalize(locator):
    """Return (address, error): exactly one of the two is None.

    Error vocabulary: MALFORMED, AMBIGUOUS-SOURCE (ADDRESSING.md §4.2).
    """
    if locator is None:
        return None, "MALFORMED"
    s = locator.strip()
    if not s:
        return None, "MALFORMED"
    if s.lower().startswith("px2:"):
        return _canon_px2(s)
    m = re.match(r"(?i)(arxiv|doi|hexagon|vixra)\s*:\s*(.+)$", s, re.S)
    if m:
        addr = _by_kind(m.group(1).lower(), m.group(2).strip())
        return (addr, None) if addr else (None, "MALFORMED")
    if re.match(r"10\.\d{4,9}/", s):  # bare DOI: unique grammar (§4.2)
        addr = _canon_doi(s)
        return (addr, None) if addr else (None, "MALFORMED")
    if re.fullmatch(OLDSTYLE_ID + r"(v\d+)?", s):  # bare old-style arXiv
        addr = _canon_arxiv(s)
        return (addr, None) if addr else (None, "MALFORMED")
    if re.fullmatch(MODERN_ID + r"(v\d+)?", s):
        return None, "AMBIGUOUS-SOURCE"  # §4.2: the profile does not guess
    if "://" in s or re.match(r"(?i)[a-z0-9-]+(\.[a-z0-9-]+)+(/|$)", s):
        return _canon_url_dispatch(s)
    return None, "MALFORMED"


# --------------------------------------------------------------------------
# The receiving service.
# --------------------------------------------------------------------------

QUEUE_DIR = os.path.expanduser("~/tluf-submissions")
HOST = "127.0.0.1"
PORT = 8643
MAX_BODY = 65536
CAPS = {"locator": 2048, "title": 512, "name": 256, "contact": 256,
        "notes": 8192}
ERROR_TEXT = {
    "MALFORMED": "that locator is not a form the addressing scheme "
                 "recognizes — paste a repository URL, a prefixed ID "
                 "(arxiv:… / doi:… / hexagon:… / vixra:…), or a web URL",
    "AMBIGUOUS-SOURCE": "that bare ID fits more than one repository — "
                        "paste the repository URL, or prefix the ID "
                        "(arxiv:… / hexagon:… / vixra:…)",
}
_lock = threading.Lock()


def _next_sequence():
    top = 0
    for name in os.listdir(QUEUE_DIR):
        m = re.match(r"(\d{6})\.txt$", name)
        if m:
            top = max(top, int(m.group(1)))
    return top + 1


def _header(value):
    """One header, one line: newlines never survive into the file."""
    return re.sub(r"[\r\n]+", " ", value or "").strip()


def store_submission(fields, address):
    os.makedirs(QUEUE_DIR, exist_ok=True)
    with _lock:
        seq = _next_sequence()
        path = os.path.join(QUEUE_DIR, "%06d.txt" % seq)
        lines = [
            "from: " + (_header(fields.get("name")) or "anonymous"),
            "date: " + datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"),
            "address: " + address,
            "locator: " + _header(fields.get("locator")),
            "title: " + _header(fields.get("title")),
            "contact: " + _header(fields.get("contact")),
            "",
            fields.get("notes") or "",
        ]
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        os.rename(tmp, path)
    return seq


class Handler(BaseHTTPRequestHandler):
    server_version = "tluf-submit/1.0"

    def _json(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/health":
            self._json(200, {"ok": True, "service": "tluf-submit"})
        else:
            self._json(404, {"ok": False, "error": "not found"})

    def do_POST(self):
        if self.path != "/api/submit":
            self._json(404, {"ok": False, "error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0:
            self._json(400, {"ok": False, "error": "empty body"})
            return
        if length > MAX_BODY:
            self._json(413, {"ok": False,
                             "error": "submission too large"})
            return
        raw = self.rfile.read(length)
        ctype = (self.headers.get("Content-Type") or "").lower()
        fields = {}
        try:
            if "json" in ctype:
                parsed = json.loads(raw.decode("utf-8"))
                if not isinstance(parsed, dict):
                    raise ValueError("not an object")
                fields = parsed
            else:
                from urllib.parse import parse_qs
                parsed = parse_qs(raw.decode("utf-8"))
                fields = {k: v[0] for k, v in parsed.items()}
        except Exception:
            self._json(400, {"ok": False, "error": "unreadable body"})
            return
        for key, cap in CAPS.items():
            value = fields.get(key)
            if value is None:
                continue
            if not isinstance(value, str):
                self._json(400, {"ok": False,
                                 "error": "field %s must be text" % key})
                return
            if len(value) > cap:
                self._json(400, {"ok": False,
                                 "error": "field %s exceeds %d characters"
                                          % (key, cap)})
                return
        locator = (fields.get("locator") or "").strip()
        if not locator:
            self._json(400, {"ok": False, "error": "locator is required"})
            return
        address, error = canonicalize(locator)
        if error:
            self._json(400, {"ok": False, "error": error,
                             "message": ERROR_TEXT[error]})
            return
        fields["locator"] = locator
        seq = store_submission(fields, address)
        self._json(201, {"ok": True, "address": address, "sequence": seq})

    def log_message(self, fmt, *args):
        sys.stderr.write("tluf-submit: %s\n" % (fmt % args))


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--canon":
        address, error = canonicalize(sys.argv[2])
        print(address if address else "ERROR " + error)
        return
    os.makedirs(QUEUE_DIR, exist_ok=True)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    sys.stderr.write(
        "tluf-submit listening on %s:%d, queue %s\n" % (HOST, PORT,
                                                        QUEUE_DIR))
    server.serve_forever()


if __name__ == "__main__":
    main()
