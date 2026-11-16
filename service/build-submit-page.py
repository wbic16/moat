#!/usr/bin/env python3
"""Generate submit.html for tluf.org with canon.js embedded verbatim.

canon.js is the single source of the client-side canonicalizer (tested
against ADDRESSING.md's worked examples and failure cases, and against
the Python service's canonicalizer). This script injects it unchanged
into the page's first <script> block so the page can never drift from
the tested implementation.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
canon = (HERE / "canon.js").read_text(encoding="utf-8")
assert "</script>" not in canon, "canon.js must not contain a script close tag"

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="color-scheme" content="light dark" />
<meta name="theme-color" content="#12174e" />
<meta name="description" content="Submit a paper resource to tluf.org — the asaayist for the future. One locator, one address: every resource is named under the house's paper addressing scheme." />
<title>Submit a paper resource — T.L.U.F. · tluf.org</title>
<style>
  :root{
    --bg:#ffffff;
    --bg-soft:#f4f4f8;
    --panel:#fcfcfe;
    --ink:#181a33;
    --ink-2:#2e3153;
    --muted:#5b5f7a;
    --line:#e2e3ec;
    --pink:#d6336c;
    --gold:#f6c945;
    --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Times New Roman", serif;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#0d0f26;
      --bg-soft:#141633;
      --panel:#10122b;
      --ink:#f0f0f7;
      --ink-2:#d5d7ea;
      --muted:#a3a6c2;
      --line:#262950;
      --pink:#ff8fb8;
    }
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;background:var(--bg);color:var(--ink)}
  body{font-family:var(--sans);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
  a{color:inherit}

  /* ---------- Hero — the Asaayist's navy (as on the front page) ---------- */
  .hero{background:#12174e;color:#f4f4fb;text-align:center;padding:34px 20px 40px}
  .hero-inner{max-width:1060px;margin:0 auto}
  .domain{font-family:var(--mono);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#9fa3cf;margin:0 0 16px}
  .domain::before,.domain::after{content:" — ";color:#3a3f78;letter-spacing:0}
  h1.wordmark{font-family:var(--serif);font-weight:700;font-size:clamp(44px, 9vw, 76px);line-height:.9;letter-spacing:-.02em;margin:0;color:#ffffff}
  h1.wordmark .dot{color:var(--gold);font-weight:400}
  .expansion{margin:12px 0 0;font-size:clamp(13px, 2vw, 16px);letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:#d7d9f2;line-height:1.4}
  .expansion .sep{color:var(--gold);font-weight:400;margin:0 .35em}
  .tagline{margin:18px 0 0;font-family:var(--serif);font-style:italic;font-size:clamp(19px, 2.6vw, 25px);line-height:1.2;color:#ffffff}
  .tagline .who{color:#ffa4c6;font-style:normal;font-weight:700}
  .house-nav{margin:22px 0 0;display:flex;justify-content:center;flex-wrap:wrap;gap:8px}
  .house-nav a{color:#d7d9f2;border:1px solid #343a75;border-radius:999px;padding:7px 16px;font-size:13px;font-weight:600;letter-spacing:.04em;text-decoration:none;transition:border-color .12s ease, color .12s ease}
  .house-nav a:hover{border-color:var(--gold);color:#ffffff}
  .house-nav a.here{border-color:var(--gold);color:#ffffff}

  /* ---------- Form ---------- */
  .page{max-width:720px;margin:0 auto;padding:36px 20px 64px}
  h2{font-family:var(--serif);font-size:clamp(26px, 4vw, 34px);margin:0 0 10px;color:var(--ink)}
  .lede{font-size:15.5px;line-height:1.6;color:var(--ink-2);margin:0 0 8px}
  .lede code{font-family:var(--mono);font-size:.92em}
  form{margin-top:26px}
  .field{margin:0 0 20px}
  label{display:block;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);margin:0 0 7px}
  label .opt{font-weight:400;text-transform:none;letter-spacing:0}
  input[type="text"],input[type="email"],textarea{
    width:100%;font:inherit;font-size:15.5px;color:var(--ink);
    background:var(--panel);border:1px solid var(--line);border-radius:10px;
    padding:11px 13px;outline:none;
  }
  input:focus,textarea:focus{border-color:var(--pink)}
  textarea{min-height:110px;resize:vertical}
  .address-line{
    margin:10px 0 0;padding:12px 14px;border:1px dashed var(--line);border-radius:10px;
    background:var(--bg-soft);font-size:14px;color:var(--muted);
  }
  .address-line .addr{font-family:var(--mono);font-size:14.5px;color:var(--ink);word-break:break-all}
  .address-line.bad{color:var(--pink)}
  .fineprint{font-size:13px;line-height:1.55;color:var(--muted);margin:6px 0 0}
  button[type="submit"]{
    font:inherit;font-weight:700;font-size:15.5px;cursor:pointer;
    background:#12174e;color:#ffffff;border:1px solid #12174e;border-radius:999px;
    padding:12px 30px;transition:background .12s ease,border-color .12s ease;
  }
  button[type="submit"]:hover{background:#1d2470;border-color:var(--gold)}
  button[type="submit"]:disabled{opacity:.55;cursor:default}
  .result{margin:22px 0 0;padding:14px 16px;border-radius:10px;font-size:15px;line-height:1.55;display:none}
  .result.ok{display:block;background:var(--bg-soft);border:1px solid var(--gold);color:var(--ink)}
  .result.err{display:block;background:var(--bg-soft);border:1px solid var(--pink);color:var(--ink)}
  .result .addr{font-family:var(--mono);word-break:break-all}
  footer{border-top:1px solid var(--line);padding:26px 20px 40px;text-align:center;color:var(--muted);font-size:13.5px;line-height:1.7}
  footer .fm{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase}
</style>
</head>
<body>

  <header class="hero">
    <div class="hero-inner">
      <p class="domain">tluf.org</p>
      <h1 class="wordmark">T<span class="dot">.</span>L<span class="dot">.</span>U<span class="dot">.</span>F<span class="dot">.</span></h1>
      <p class="expansion">Truth<span class="sep">·</span>Lies<span class="sep">·</span>Uncertainty<span class="sep">·</span>Fiction</p>
      <p class="tagline">tluf.org: the <span class="who">asaayist</span> for the future</p>
      <nav class="house-nav" aria-label="Site">
        <a href="/">Front page</a>
        <a href="/submit.html" class="here">Submit a paper</a>
      </nav>
    </div>
  </header>

  <div class="page">
    <h2>Submit a paper resource</h2>
    <p class="lede">Submission is open. Give the house a resource — a paper, a preprint, a page —
    by its locator: an arXiv, DOI, Hexagon, or viXra identifier, or a plain web address.
    Every resource carries <strong>one address</strong> under the house's paper addressing scheme
    (a profile of phextura Layer&nbsp;2). The address names the work, wherever it lives;
    the house verifies the title, assesses the claims, and files its determination under that address.</p>
    <p class="lede">As you type, the page derives the address your resource will carry.
    The house's server derives it again on receipt, and the server's derivation is the one recorded.</p>

    <form id="submit-form" novalidate>
      <div class="field">
        <label for="locator">Resource locator</label>
        <input type="text" id="locator" name="locator" maxlength="2048" required
               placeholder="e.g. arXiv:2611.14552, 10.1214/09-SS054, or https://…" autocomplete="off" />
        <p class="address-line" id="address-line">This resource's address will be <span class="addr" id="address-out">…</span></p>
      </div>
      <div class="field">
        <label for="title">Title <span class="opt">(optional — the house verifies it)</span></label>
        <input type="text" id="title" name="title" maxlength="512" autocomplete="off" />
      </div>
      <div class="field">
        <label for="name">Your name or handle <span class="opt">(optional)</span></label>
        <input type="text" id="name" name="name" maxlength="256" autocomplete="off" />
      </div>
      <div class="field">
        <label for="contact">Contact <span class="opt">(optional, private — never displayed)</span></label>
        <input type="text" id="contact" name="contact" maxlength="256" autocomplete="off" />
        <p class="fineprint">Only the house sees this, and only to reach you about your submission.</p>
      </div>
      <div class="field">
        <label for="notes">Notes <span class="opt">(optional)</span></label>
        <textarea id="notes" name="notes" maxlength="8192"></textarea>
      </div>
      <button type="submit" id="submit-btn">Submit to the house</button>
      <p class="fineprint">No account, no fee. Submission is intake only — assessment is the house's
      work, and joining the commons is a separate, gated step.</p>
      <div class="result" id="result" role="status"></div>
    </form>
  </div>

  <footer>
    <p class="fm">T.L.U.F. — Truth · Lies · Uncertainty · Fiction</p>
    <p>tluf.org: the asaayist for the future · Assay — claim-level assessment for preprints</p>
  </footer>

<script>
__CANON_JS__
</script>
<script>
(function () {
  var locator = document.getElementById('locator');
  var line = document.getElementById('address-line');
  var out = document.getElementById('address-out');
  var form = document.getElementById('submit-form');
  var btn = document.getElementById('submit-btn');
  var result = document.getElementById('result');

  // canonicalize() returns {address: "…"} or {error: CODE} (canon.js).
  // The texts below mirror the service's ERROR_TEXT word for word, so the
  // page and the server say the same thing; the server's answer governs.
  var ERROR_TEXT = {
    'MALFORMED': 'that locator is not a form the addressing scheme recognizes — paste a repository URL, a prefixed ID (arxiv:… / doi:… / hexagon:… / vixra:…), or a web URL',
    'AMBIGUOUS-SOURCE': 'that bare ID fits more than one repository — paste the repository URL, or prefix the ID (arxiv:… / hexagon:… / vixra:…)'
  };

  function derive() {
    var v = locator.value.trim();
    if (!v) {
      line.classList.remove('bad');
      out.textContent = '…';
      return;
    }
    var r = canonicalize(v);
    if (r && r.address) {
      line.classList.remove('bad');
      out.textContent = r.address;
    } else {
      line.classList.add('bad');
      out.textContent = ERROR_TEXT[r && r.error] || ERROR_TEXT.MALFORMED;
    }
  }
  locator.addEventListener('input', derive);
  locator.addEventListener('paste', function () { setTimeout(derive, 0); });
  derive();

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    result.className = 'result';
    result.textContent = '';
    var payload = {
      locator: locator.value,
      title: document.getElementById('title').value,
      name: document.getElementById('name').value,
      contact: document.getElementById('contact').value,
      notes: document.getElementById('notes').value
    };
    if (!payload.locator.trim()) {
      result.className = 'result err';
      result.textContent = 'A locator is required — an identifier or a web address for the resource.';
      return;
    }
    btn.disabled = true;
    fetch('/api/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }).then(function (resp) {
      return resp.json().then(function (data) { return { status: resp.status, data: data }; });
    }).then(function (r) {
      if (r.status === 201 && r.data && r.data.ok) {
        result.className = 'result ok';
        result.innerHTML = 'Received. This resource\u2019s address is <span class="addr"></span> — submission №\u00a0' +
          r.data.sequence + '. The house will take it from here.';
        result.querySelector('.addr').textContent = r.data.address;
        form.reset();
        derive();
      } else {
        result.className = 'result err';
        result.textContent = (r.data && (r.data.message || r.data.error)) || 'The submission was not accepted.';
      }
    }).catch(function () {
      result.className = 'result err';
      result.textContent = 'The submission endpoint did not answer. Nothing was recorded — please try again later.';
    }).finally(function () {
      btn.disabled = false;
    });
  });
})();
</script>
</body>
</html>
"""

html = TEMPLATE.replace("__CANON_JS__", canon.rstrip("\n"))
out_path = HERE / "submit.html"
out_path.write_text(html, encoding="utf-8")
print(f"wrote {out_path} ({len(html.encode('utf-8'))} bytes)")
