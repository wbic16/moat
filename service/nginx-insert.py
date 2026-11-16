#!/usr/bin/env python3
"""Insert the tluf-submit API proxy blocks into an nginx site config.

Used by install-submit.sh on the live, certbot-managed config (which
must not be overwritten: certbot owns its TLS blocks). Idempotent: if
the marker comment is already present, the file is left unchanged.

Target block selection: the server block that serves tluf.org over
HTTPS (contains `server_name ... tluf.org` and a `listen ... 443`
directive); if no such block exists, the first server block naming
tluf.org. The location blocks are inserted just before that block's
closing brace, found by brace matching.

Usage: nginx-insert.py <config-path>
Exit codes: 0 inserted or already present; 2 no suitable server block;
3 unbalanced braces.
"""
import re
import sys

MARKER = "# tluf-submit-api"

BLOCK = """
    # tluf-submit-api: paper submission service (loopback 127.0.0.1:8643)
    location = /api/submit {
        proxy_pass http://127.0.0.1:8643;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size 64k;
    }
    location = /api/health {
        proxy_pass http://127.0.0.1:8643;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        access_log off;
    }
"""


def server_blocks(text):
    """Yield (start, end) spans of each top-level `server { ... }` block."""
    spans = []
    for m in re.finditer(r"(?m)^\s*server\s*\{", text):
        depth = 0
        i = m.end() - 1  # at the opening brace
        start = i
        while i < len(text):
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    spans.append((m.start(), i))
                    break
            i += 1
        else:
            raise ValueError("unbalanced braces")
    return spans


def main():
    path = sys.argv[1]
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if MARKER in text:
        print("already present — no change")
        return 0
    try:
        spans = server_blocks(text)
    except ValueError:
        print("unbalanced braces in config", file=sys.stderr)
        return 3
    target = None
    fallback = None
    for start, end in spans:
        body = text[start:end + 1]
        if "tluf.org" not in body:
            continue
        if not re.search(r"server_name[^;]*\btluf\.org\b", body):
            continue
        if fallback is None:
            fallback = (start, end)
        if re.search(r"listen[^;]*\b443\b", body):
            target = (start, end)
            break
    chosen = target or fallback
    if chosen is None:
        print("no server block for tluf.org found", file=sys.stderr)
        return 2
    _, end = chosen
    new_text = text[:end] + BLOCK + text[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    print("inserted tluf-submit-api blocks into the tluf.org server block")
    return 0


if __name__ == "__main__":
    sys.exit(main())
