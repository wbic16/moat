// canon.js — the tluf.org paper-address canonicalizer (client transcription).
// Spec: ~/workspace/oracle-service/ADDRESSING.md §4–§6. The spec governs;
// this file and the receiving service (tluf-submit.py) are two
// transcriptions of the same section and are tested against the same
// worked examples (ADDRESSING.md §7). canonicalize(locator) returns
// {address: "..."} or {error: "MALFORMED" | "AMBIGUOUS-SOURCE"}.
"use strict";

var TRACKING_KEYS = {
  utm_source: 1, utm_medium: 1, utm_campaign: 1, utm_term: 1,
  utm_content: 1, fbclid: 1, gclid: 1, mc_cid: 1, mc_eid: 1
};
var UNRESERVED = {};
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
  .split("").forEach(function (c) { UNRESERVED[c] = 1; });
var MODERN_ID = /^\d{4}\.\d{4,5}$/;
var OLDSTYLE_ID = /^[a-z][a-z-]*(\.[A-Z]{2})?\/\d{7}$/;

function stripSentencePunct(s) {
  if (s && (s.charAt(s.length - 1) === "." || s.charAt(s.length - 1) === ",")) {
    return s.slice(0, -1);
  }
  return s;
}

function dropVersion(s) {
  return s.replace(/v\d+$/, "");
}

function canonArxiv(idText) {
  var s = dropVersion(stripSentencePunct(idText.trim()));
  if (s.toLowerCase().slice(-4) === ".pdf") { s = s.slice(0, -4); }
  if (MODERN_ID.test(s) || OLDSTYLE_ID.test(s)) { return "px2:arxiv:" + s; }
  return null;
}

function pctDecode(s) {
  try { return decodeURIComponent(s); } catch (e) { return s; }
}

function canonDoi(idText) {
  var s = idText.trim();
  var idx = s.indexOf("doi.org/");
  if (idx >= 0) { s = s.slice(idx + "doi.org/".length); }
  s = stripSentencePunct(pctDecode(s)).toLowerCase();
  if (/^10\.\d{4,9}\/\S+$/.test(s)) { return "px2:doi:" + s; }
  return null;
}

function canonRepo(kind, idText) {
  var s = dropVersion(stripSentencePunct(idText.trim()));
  if (MODERN_ID.test(s)) { return "px2:" + kind + ":" + s; }
  return null;
}

function normalizePct(s) {
  return s.replace(/%([0-9A-Fa-f]{2})/g, function (m, hex) {
    var ch = String.fromCharCode(parseInt(hex, 16));
    if (UNRESERVED[ch]) { return ch; }
    return "%" + hex.toUpperCase();
  });
}

function removeDotSegments(path) {
  var out = [];
  var segs = path.split("/");
  for (var i = 0; i < segs.length; i++) {
    var seg = segs[i];
    if (seg === ".") { continue; }
    if (seg === "..") { if (out.length) { out.pop(); } continue; }
    out.push(seg);
  }
  var res = out.join("/");
  if (path.charAt(0) === "/" && res.charAt(0) !== "/") { res = "/" + res; }
  return res;
}

function strictQuote(s) {
  return encodeURIComponent(s).replace(/[!'()*]/g, function (c) {
    return "%" + c.charCodeAt(0).toString(16).toUpperCase();
  });
}

// Split a URL by hand (scheme://netloc/path?query#fragment) so the
// normalization is the spec's, not the URL class's.
function splitUrl(raw) {
  var rest = raw, scheme = "";
  var m = rest.match(/^([A-Za-z][A-Za-z0-9+.-]*):\/\//);
  if (m) { scheme = m[1].toLowerCase(); rest = rest.slice(m[0].length); }
  var frag = "";
  var hi = rest.indexOf("#");
  if (hi >= 0) { frag = rest.slice(hi + 1); rest = rest.slice(0, hi); }
  var query = "";
  var qi = rest.indexOf("?");
  if (qi >= 0) { query = rest.slice(qi + 1); rest = rest.slice(0, qi); }
  var netloc = rest, path = "";
  var si = rest.indexOf("/");
  if (si >= 0) { netloc = rest.slice(0, si); path = rest.slice(si); }
  var userinfo = "";
  var ai = netloc.lastIndexOf("@");
  if (ai >= 0) { userinfo = netloc.slice(0, ai); netloc = netloc.slice(ai + 1); }
  var host = netloc, port = "";
  var ci = netloc.lastIndexOf(":");
  if (ci >= 0 && /^\d+$/.test(netloc.slice(ci + 1))) {
    host = netloc.slice(0, ci); port = netloc.slice(ci + 1);
  }
  return { scheme: scheme, host: host.toLowerCase(), port: port,
           path: path, query: query };
}

function canonUrl(raw) {
  if (raw.indexOf("://") < 0) { raw = "https://" + raw; }
  var p = splitUrl(raw);
  if (p.scheme !== "http" && p.scheme !== "https") { return null; }
  var host = p.host;
  if (!host) { return null; }
  if (host.slice(0, 4) === "www.") { host = host.slice(4); }
  var netloc = host;
  var port = p.port ? parseInt(p.port, 10) : null;
  if (port !== null && !((p.scheme === "http" && port === 80) ||
                         (p.scheme === "https" && port === 443))) {
    netloc = host + ":" + port;
  }
  var path = removeDotSegments(normalizePct(p.path));
  if (path === "/") { path = ""; }
  else if (path.length > 1 && path.charAt(path.length - 1) === "/") {
    path = path.slice(0, -1);
  }
  var pairs = [];
  if (p.query) {
    var parts = p.query.split("&");
    for (var i = 0; i < parts.length; i++) {
      if (!parts[i]) { continue; }
      var eq = parts[i].indexOf("=");
      var k = eq >= 0 ? parts[i].slice(0, eq) : parts[i];
      var v = eq >= 0 ? parts[i].slice(eq + 1) : "";
      var kd = pctDecode(k);
      if (TRACKING_KEYS[kd.toLowerCase()]) { continue; }
      pairs.push([kd, pctDecode(v)]);
    }
    pairs.sort(function (a, b) {
      if (a[0] !== b[0]) { return a[0] < b[0] ? -1 : 1; }
      if (a[1] !== b[1]) { return a[1] < b[1] ? -1 : 1; }
      return 0;
    });
  }
  var query = pairs.map(function (kv) {
    return kv[1] !== "" ? strictQuote(kv[0]) + "=" + strictQuote(kv[1])
                        : strictQuote(kv[0]);
  }).join("&");
  var url = p.scheme + "://" + netloc + path;
  if (query) { url += "?" + query; }
  if (url.indexOf("@e:") >= 0) { url = url.split("@e:").join("%40e:"); }
  return "px2:url:" + url;
}

function byKind(kind, rest) {
  if (kind === "arxiv") { return canonArxiv(rest); }
  if (kind === "doi") { return canonDoi(rest); }
  if (kind === "hexagon" || kind === "vixra") { return canonRepo(kind, rest); }
  return null;
}

function canonUrlDispatch(s) {
  var raw = s.indexOf("://") >= 0 ? s : "https://" + s;
  var p = splitUrl(raw);
  var bare = p.host.slice(0, 4) === "www." ? p.host.slice(4) : p.host;
  var path = p.path, m, addr;
  if (bare === "arxiv.org") {
    m = path.match(/\/(?:abs|pdf)\/(.+)$/);
    if (m) {
      addr = canonArxiv(pctDecode(m[1]));
      return addr ? { address: addr } : { error: "MALFORMED" };
    }
    return { error: "MALFORMED" };
  }
  if (bare === "doi.org" || bare === "dx.doi.org") {
    addr = canonDoi(pctDecode(path.replace(/^\//, "")));
    return addr ? { address: addr } : { error: "MALFORMED" };
  }
  if (bare === "vixra.org") {
    m = path.match(/\/abs\/(.+)$/);
    if (m) {
      addr = canonRepo("vixra", pctDecode(m[1]));
      return addr ? { address: addr } : { error: "MALFORMED" };
    }
    return { error: "MALFORMED" };
  }
  if (bare === "hexagonmath.org") {
    var seg = path.replace(/\/+$/, "").split("/").pop();
    addr = canonRepo("hexagon", pctDecode(seg));
    return addr ? { address: addr } : { error: "MALFORMED" };
  }
  addr = canonUrl(s);
  return addr ? { address: addr } : { error: "MALFORMED" };
}

function canonPx2(s) {
  var body = s.slice(4);
  var hi = body.indexOf("#");
  var head = hi >= 0 ? body.slice(0, hi) : body;
  var tail = hi >= 0 ? body.slice(hi + 1) : null;
  var out;
  if (head.slice(0, 4) === "sum:") {
    var m = head.match(/^sum:xxh3-128:([0-9A-Fa-f]{32})$/);
    if (!m) { return { error: "MALFORMED" }; }
    out = "px2:sum:xxh3-128:" + m[1].toLowerCase();
  } else {
    var pin = "";
    var ei = head.lastIndexOf("@e:");
    if (ei >= 0) {
      var pinval = head.slice(ei + 3);
      if (!/^[0-9A-Fa-f]{16,}$/.test(pinval)) { return { error: "MALFORMED" }; }
      pin = "@e:" + pinval.toLowerCase();
      head = head.slice(0, ei);
    }
    var ci = head.indexOf(":");
    if (ci < 0) { return { error: "MALFORMED" }; }
    var token = head.slice(0, ci).toLowerCase();
    var rest = head.slice(ci + 1);
    if (token === "corpus") {
      if (!/^[a-z][a-z0-9-]*$/.test(rest)) { return { error: "MALFORMED" }; }
      out = "px2:corpus:" + rest;
    } else if (token === "tluf") {
      if (!/^[0-9a-f]{16}$/.test(rest.toLowerCase())) {
        return { error: "MALFORMED" };
      }
      out = "px2:tluf:" + rest.toLowerCase();
    } else if (token === "arxiv" || token === "doi" ||
               token === "hexagon" || token === "vixra") {
      var addr = byKind(token, rest);
      if (!addr) { return { error: "MALFORMED" }; }
      out = addr;
    } else if (token === "url") {
      var uaddr = canonUrl(rest);
      if (!uaddr) { return { error: "MALFORMED" }; }
      out = uaddr;
    } else {
      return { error: "MALFORMED" };
    }
    out += pin;
  }
  if (tail !== null) {
    if (!/^[a-z][a-z0-9-]*:[a-z][a-z0-9-]*$/.test(tail)) {
      return { error: "MALFORMED" };
    }
    out += "#" + tail;
  }
  return { address: out };
}

function canonicalize(locator) {
  if (locator === null || locator === undefined) {
    return { error: "MALFORMED" };
  }
  var s = String(locator).trim();
  if (!s) { return { error: "MALFORMED" }; }
  if (s.toLowerCase().slice(0, 4) === "px2:") { return canonPx2(s); }
  var m = s.match(/^(arxiv|doi|hexagon|vixra)\s*:\s*([\s\S]+)$/i);
  if (m) {
    var addr = byKind(m[1].toLowerCase(), m[2].trim());
    return addr ? { address: addr } : { error: "MALFORMED" };
  }
  if (/^10\.\d{4,9}\//.test(s)) {
    var d = canonDoi(s);
    return d ? { address: d } : { error: "MALFORMED" };
  }
  if (/^[a-z][a-z-]*(\.[A-Z]{2})?\/\d{7}(v\d+)?$/.test(s)) {
    var a = canonArxiv(s);
    return a ? { address: a } : { error: "MALFORMED" };
  }
  if (/^\d{4}\.\d{4,5}(v\d+)?$/.test(s)) {
    return { error: "AMBIGUOUS-SOURCE" };
  }
  if (s.indexOf("://") >= 0 || /^[a-z0-9-]+(\.[a-z0-9-]+)+(\/|$)/i.test(s)) {
    return canonUrlDispatch(s);
  }
  return { error: "MALFORMED" };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { canonicalize: canonicalize };
}
