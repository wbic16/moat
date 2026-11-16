# Assay — Build Plan

*Written 2026-11-14, the day the job was scheduled. Job: jobs.phext Job 1, "Build Assay — the hosted assessment service" (26.7.8/8.6.10/6.6.8). Scheduling handle: tasks.phext 37.8.8/10.8.13/7.7.13. Specification of record: `~/workspace/oracle-service/REQUIREMENTS.md` — 117 numbered requirements, six standing commitments (§0), acceptance tests §10. Where this plan and the requirements differ, the requirements govern.*

*Front-door move, 2026-11-14 (later the same day): Will obtained **tluf.org** — TLUF, truth, lies, unknown, fiction, the frame the service serves; his designation: "tluf.org: the asaayist for the future" — and moved the service's front door there: "move assay.phext.io here." Every front-door statement in this plan now reads **tluf.org**; assay.phext.io is superseded. The requirements record the designation and the move in their top matter.*

## Repository finding (site map checked 2026-11-14)

The site map (`~/workspace/site-map`, 172 public wbic16 repos) contains **no repo that fits this service** — no assay, moat, oracle, commons, or assessment-service repo exists. The nearest neighbours are components, not homes: `phext-lattice` (the hosted phext service behind edit.phext.io — storage/serving machinery Assay draws on), `sq` / `sq-cloud` (SQ hosting), `libphext-rs` (the format library). None holds accounts, submissions, a commons, or billing. **The plan therefore proposes creating `wbic16/assay`** when Stage 0 begins. No repo is created in this scheduling pass.

## How the stages work

- Stages run in order. A stage is done when its acceptance shape holds against the running service or its records — not when its code is written.
- Each stage lists the requirement groups it lands. Cross-cutting groups (T operations/trust, NG non-goals) are not a stage of their own until the end: every stage builds inside them, and Stage 8 proves them.
- **Open decisions:** each stage names the ODs it touches. A stage that reaches an unresolved OD builds the **strictest reading stated in the requirements** and flags the spot in the job's notes, so Will's later ruling changes a marked place, not a hidden assumption.
- The reading is the product: MOAT itself (research.phext + the rd-tracker discipline) is the reference implementation of an assessment throughout. Stages automate the service around the reading; they do not pretend the reading is software until the house's process says so.

## Stage 0 — Ground: repo, hosting, tenancy skeleton

- **Lands:** T (isolation, audit log, signed/versioned records) in skeleton; the §0 commitments as build rules.
- **Done when:** `wbic16/assay` exists (proposed above; creation is Stage 0's first act, under Will's word or the job's dispatch); the service skeleton runs on a ranch node behind tluf.org; one researcher's material is provably invisible to another's session (tenant isolation by construction, not by filter); every state change writes the append-only audit stub (T-4).
- **ODs touched:** OD-3 (audit retention) — strictest reading: stubs kept, content hashes of deleted private papers retained only as the requirements' default states, flagged.

## Stage 1 — Submission spine

- **Lands:** S-1…S-11; the intake half of F (content hash, duplicate linking under S-6, intake check records under S-11/F-3 — findings machinery completes in Stage 5).
- **Done when:** a preprint arrives in every S-1 form (PDF, LaTeX, text/Markdown, arXiv id, viXra id, native phext); its record carries only S-2's closed metadata (no affiliation field exists to fill); its state walks received → queued → in assessment → assessed → returned, queryable by the submitter at every step, with the honest live turnaround of S-10 shown from receipt; withdrawal before *assessed* deletes under O-5 semantics; an unreadable submission returns to *received* with the failure named (S-9).
- **Acceptance shape:** §10 test (1) begins here — the same paper submitted as pseudonym and as affiliated name is indistinguishable in handling.
- **ODs touched:** OD-6 (pseudonymous submission is permitted by S-3 regardless; only score accrual waits on the ruling).

## Stage 2 — The assessment

- **Lands:** A-1…A-13, including the False standard (A-2), shape extraction (A-3/A-4), nuance failures named at the line (A-5), dispute → re-examination as a new edition (A-11).
- **Done when:** a submitted paper is heated and spaghettified — every load-bearing claim carrying exactly one standing on a stated basis; a False is issuable only with exhibited grounds of one of A-2's three kinds; the shape is extracted (or "no shape found" stated plainly); the service's own gate standings are displayed on the submission surface (T-9, per commitment 0.6 — the instrument's ~62% binning reliability on day one, said out loud).
- **Acceptance shape:** §10 test (2) — a False's grounds survive the author's dispute unchanged, or change only by a visible new edition.
- **ODs touched:** OD-5 (depth/turnaround) — strictest reading: one depth, one honest queue, no paid priority, until Will rules.

## Stage 3 — The produced phext and ownership

- **Lands:** P-1…P-9; O-1…O-8.
- **Done when:** the assessment is delivered as a self-contained phext — claims with standings and grounds, the shape, the nuance list, questions opened, the novelty line, revision history, provenance (submission id, date, assessor version) — readable whole with the open tooling alone (libphext/SQ), addressable by coordinate and edition checksum; the researcher exports it natively at any time, deletes the service's copy, and no ownership act (export, read own, delete, withdraw) is ever billed, at any volume (O, API-6's principle applied service-wide from this stage).
- **Acceptance shape:** §10 test (3) — export, open with open tools alone, delete the account copy, the export still reads whole.
- **ODs touched:** OD-3 again (deletion leaves exactly the T-4 stub).

## Stage 4 — The commons and the merge gate

- **Lands:** C-1…C-9; M-1…M-9 (authenticate-and-attest, per author, bound to the edition checksum; no merge on a partial set).
- **Done when:** papers are private by default and nothing joins by bundle or inheritance; a merge is a distinct, affirmative, per-paper, per-edition act requiring every author of record authenticated and attesting; attestations are preserved as the commons' consent evidence; a revised edition needs fresh attestation; joining publishes the assessment, never the preprint unless separately deposited; a pseudonym key counts as an identity, so the gate cannot become a pedigree test.
- **Acceptance shape:** §10 test (4), second half — a joined paper is linkable from another's assessment.
- **ODs touched:** OD-1 (withdrawal semantics) — strictest reading until ruled: tombstone relocation (Option A, the tracker discipline); OD-2 (contested author lists) — strictest reading: the wide reading of author of record; OD-8 (unresponsive co-author) — strictest reading: (a) merge blocked; OD-9 (deceased/incapacitated author) — strictest reading: (a) unmergeable; OD-10 (attest-then-dispute) — strictest reading: (b) validity review first, then withdrawal. Each built spot is flagged in the job's notes.

## Stage 5 — Forgery checks, full machinery

- **Lands:** F-1…F-8 (identity forgery, document forgery, edition tampering), completing the intake hooks laid in Stage 1.
- **Done when:** checks run at submission *and* again at merge, invariant across submitter classes; every check ends in exactly one of two recorded outcomes — a finding with grounds exhibited at the False standard (both hashes, overlapping passages named, identity-control failure demonstrated), or "no evidence found"; a finding holds the merge only — not the assessment, not the researcher's other papers — and opens the A-11 dispute path, in which a withdrawn finding is withdrawn in the record.
- **Acceptance shape:** §10 test (8) — a materially overlapping paper under fresh names produces a finding with passages exhibited, or a recorded "no evidence found", and no third, quieter outcome.
- **ODs touched:** OD-11 (how public a confirmed forgery is) — strictest reading, and the requirements' stated default: private flag, house-eyes only.

## Stage 6 — Discovery

- **Lands:** D-1…D-8; NG-7 (not a directory of persons).
- **Done when:** matches are computed from merged material only — a shared domain, or a shared paper (co-authorship, or one of the four stated commons relations: re-pricing, collision, shape link, question closed); every match is shown with its reason; findability is the researcher's own setting, closable retroactively without withdrawing papers; contact runs through the service with no private channels exposed; findability obliges no reply.
- **Acceptance shape:** §10 test (6) — a researcher whose only paper stays private can neither find nor be found; after joining, they find exactly the matches the paper's domains and relations create, each with its reason.
- **ODs touched:** Note N-1 (name lookup) — not a decision yet; D-5's prohibition on naked people-search stands as built.

## Stage 7 — Researcher scores

- **Lands:** R-1…R-8.
- **Done when:** each author's novelty is a four-component vector (True / False / Unknown / Fiction), accrued only through assessed papers, priced against the state of the corpus at assessment time — so a known result re-submitted in fresh wording accrues nothing on any component (§10 test (5)); the vector is portable inside the owned phext, is never collapsed to a single number in any interface, and per-paper increments from merged papers are public with the paper while the whole stays the researcher's.
- **ODs touched:** OD-4 (publishing the whole vector as one signed statement) — strictest reading: not offered until ruled; OD-6 (accrual to a pseudonym) — strictest reading: accrual requires the identity ruling; pseudonymous papers are still assessed in full.

## Stage 8 — API, billing, and the house review queue

- **Lands:** API-1…API-12; the rest of T (published queue state, behavioural rate handling).
- **Done when:** the API offers the core acts (submit, poll state, fetch the produced phext itself, manage papers, request merge) as a channel and never a bypass — an API key is not an attestation, and API merges need the full §5A set; billing runs as posture: a generous free allowance sized for real fringe work, simple pre-published metering beyond it, ownership acts never billed (API-6); all API-arriving work enters the house review queue (assessment quality + forgery signals) before any API merge finalizes, with submitter-visible states (queued → under review → cleared / held with a stated reason), published depth and typical wait, no silent drops, and backlogs announced on the submission surfaces rather than absorbed as quiet slowdowns.
- **Acceptance shape:** §10 test (7) — an API merge sits visibly in the queue until the house clears or holds it, and the same merge attempted outside the queue finds no path.
- **ODs touched:** OD-12 (concrete pricing numbers) — no figures are invented; the allowance is set at Stage 8's dispatch from running costs, under Will's ruling; OD-5 again if paid queue position is ever proposed (it is not built).

## Stage 9 — The acceptance run

- **Lands:** the full §10 suite, run end to end as an inspector would; the remaining T requirements proven against records.
- **Done when:** all eight §10 tests pass against the live service at tluf.org; every OD still unresolved is listed in the job's scroll with the strictest reading that was built in its place; Job 1's standing in jobs.phext moves to *done* — by the record, not by announcement.

## Stage map, at a glance

| Stage | Lands | §10 tests |
|---|---|---|
| 0 Ground | repo, hosting, tenancy, audit skeleton | — |
| 1 Submission spine | S, intake F hooks | (1) begins |
| 2 Assessment | A | (2) |
| 3 Produced phext + ownership | P, O | (3) |
| 4 Commons + merge gate | C, M | (4) |
| 5 Forgery checks | F | (8) |
| 6 Discovery | D | (6) |
| 7 Researcher scores | R | (5) |
| 8 API + billing + review queue | API, rest of T | (7) |
| 9 Acceptance run | all of §10, T proven | (1)–(8) |

*End of plan.*

---

## Addressing note (2026-11-15)

**`~/workspace/oracle-service/ADDRESSING.md` is the addressing design of record for every stage that mints or records an address** — in the first instance Stage 1 (intake addressing of every arrival form), Stage 3 (the produced phext cites works by px2 address), and Stage 4 (commons links resolve by address). It is a profile of phextura's Layer 2 scheme, written 2026-11-15 under task 42.9.6/12.6.15/5.8.10, which also landed its first down payment: the public submission form at tluf.org and its receiving service. The addendum in REQUIREMENTS.md (2026-11-15) records the same designation from the specification side.
