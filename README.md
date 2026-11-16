# MOAT — the Research Oracle process and the Assay service

MOAT is the internal name for the epistemic process: ingest a research claim,
split it into individual claims, and file each one as **True, False, Unknown,
or Fiction** (TLUF), with a receipt an independent checker can re-run. The
hosted service built on the process is **Assay** — the assayer tests the ore,
never owns it, never refuses the test. Its front door is
[tluf.org](https://tluf.org).

This repo is the code and design home for the assayist and the backend
(consolidated 2026-11-16). The Assay build stages in
`design/BUILD-PLAN.md` dispatch under task 37.8.8/10.8.13/7.7.13 in the house
task register; from this consolidation forward, this repo is their home.

## Layout

- `design/` — the Assay design corpus: REQUIREMENTS.md (117 requirements),
  BUILD-PLAN.md (10 stages), ADDRESSING.md (the `px2:` addressing profile —
  design of record for address minting), BRANDING.md, and the process paper
  the-research-oracle.md.
- `service/` — the tluf.org submissions service kit: `tluf-submit.py`
  (receiver; Python canonicalizer built in), `canon.js` (client canonicalizer,
  embedded verbatim into submit.html by `build-submit-page.py`),
  `install-submit.sh` + `nginx-insert.py` (the root install step),
  `verify-tluf.sh`, `start-tluf-submit.sh`, `tluf-submit.service`,
  `tluf.org.conf`.
- `evaluation/` — the MOAT evaluation machinery: the ratified 12-paper
  protocol preregistration, the 2026-11-14 evaluation, scoring scripts, and
  the protocol's data record (`data/`: predictions, fringe seals, scores,
  scans). `ingestion/` holds the per-paper integration scripts those runs used.
- `epistemic/` — the Minimum Viable Oracle Lean project: the registry
  extractor and the Lean proofs that the claim registry is total, unique,
  receipt-backed, and only moves by legal transitions.
- `tracker/` — the research-tracker builder (`build_research_phext.py`) and
  the Singular audit (`audit_singular.py`). The tracker corpus itself
  (research.phext and its sources) is data and stays in the phext register
  system; only the builder code lives here. See MANIFEST.md for the call.
- `DEPLOY.md` — the deployment map for tluf.org and this repo's service.
- `MANIFEST.md` — what came from where, what was deliberately left out, and why.

## Sibling repos

- [site-tluf-org](https://github.com/wbic16/site-tluf-org) — the tluf.org
  site source of record (index.html, submit.html).
- [moat](https://github.com/wbic16/moat) — this repo: the assayist + backend.
- [site-quickfork-net](https://github.com/wbic16/site-quickfork-net) — the
  quickfork.net portfolio site; its TLUF entry links https://tluf.org and
  this repo.

## Deployment status (2026-11-16)

tluf.org is live on awsbox. The submissions service runs on awsbox loopback
(127.0.0.1:8643, systemd user unit `tluf-submit.service`) and the submit page
is live; the awsbox copies are byte-identical to `service/` here (hashes in
DEPLOY.md). Exactly one root step remains Will's-hands — see DEPLOY.md.
Until it runs, the public `/api/health` returns 404 through nginx.
