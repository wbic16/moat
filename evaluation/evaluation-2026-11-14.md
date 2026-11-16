# MOAT evaluated — an in-depth audit of the calibration claim

**Date:** 2026-11-14 · **Task:** 26.5.7/6.6.9/7.4.8 · **Direction:** Will Bickford, whose
verdict on the claim, stated before this test: **"Almost certainly false."**

**The claim under test.** After Paper 019 the Research Oracle stands at 100% (90–100)
with seven consecutive exact landings (P013–P019) and axis calls at 12/12. The implied
claim: *the skim (title + abstract) genuinely foresees a paper's delta, and the Oracle
measures the model's distance from foreseeing it perfectly.*

**Method.** Every number below was recomputed by script from the primary record —
`predictions.jsonl` (sealed BEFORE lines and AFTER score lines for Papers 008–019) —
and cross-checked against the tracker (charter band rule at 1.1.4, Oracle ledger,
detection list at 1.1.6). Script: `evaluation_analysis.py` in this folder; its full
output table is `evaluation-2026-11-14-data.json`. Conventions: NI is recomputed as
(new + 0.5 × revised) / (concepts-before + new) on the **sealed basis** (the
denominator the skim saw); the two drift papers (P008, P011) are also computed on the
absorption basis their own records declare. Nothing was taken from a summary.

---

## Verdict, by part of the claim

| Part of the claim | Verdict |
|---|---|
| The exact Oracle landings evidence foresight | **False — an artifact.** Will's verdict sustained. |
| The skim foresees the delta's size (Index, concept counts) | **Unproven, and weak where measurable.** Edge over the best null ≈ zero on the common subset; counts are a one-sided floor, not an estimate. |
| The skim foresees structure (axis calls) | **Supported within this record** — 12/12 with four yes-calls; no null comes close. Carries the self-judging caveat. |
| The Oracle measures distance from perfect foresight | **False as constructed.** It measures band + axis-call + step-choice; it is nearly insensitive to the size of the miss. |

What this verdict does **not** touch: the tracker corpus itself — 247 concepts, the
registry, the Lean proofs. Those never depended on the skim. What failed is one
measuring instrument's headline, not the library it was measuring.

---

## Leg A — the record, recomputed

All twelve scored papers (sealed basis; OP = Oracle point):

| Paper | Source | New pred→actual | Rev pred→actual | Axis pred→actual | NI pred | NI actual | \|NI err\| | OP pred→actual | Exact? | Links pred→actual |
|---|---|---|---|---|---|---|---|---|---|---|
| 008 | cron | 5→6 | 1→1 | no→no | .0591 | .0691 | .0100 | 38→45 | no | 4→6 |
| 009 | Will | 6→6 | 1→0 | **yes→yes** | .0596 | .0550 | .0046 | 42→40 | no | 3→4 |
| 010 | Will | 7→7 | 1→0 | **yes→yes** | .0647 | .0603 | .0043 | 42→40 | no | 5→8 |
| 011 | Will | 6→7 | 1→1 | no→no | .0565 | .0647 | .0081 | 45→50 | no | 5→11 |
| 012 | cron | 6→7 | 1→1 | no→no | .0504 | .0577 | .0073 | 55→60 | no | 6→12 |
| 013 | cron | 6→8 | 1→0 | no→no | .0478 | .0580 | .0102 | 70→70 | **yes** | 8→12 |
| 014 | Will | 7→20 | 1→0 | no→no | .0517 | .1266 | .0749 | 80→80 | **yes** | 12→13 |
| 015 | Will | 8→12 | 0→0 | **yes→yes** | .0482 | .0706 | .0224 | 75→75 | **yes** | 11→15 |
| 016 | Will | 10→10 | 0→0 | **yes→yes** | .0541 | .0541 | .0000 | 70→70 | **yes** | 13→15 |
| 017 | Will | 11→17 | 1→1 | no→no | .0532 | .0788 | .0256 | 80→80 | **yes** | 17→41 |
| 018 | cron | 6→7 | 1→0 | no→no | .0277 | .0297 | .0020 | 90→90 | **yes** | 11→15 |
| 019 | Will | 9→11 | 0→0 | no→no | .0367 | .0445 | .0078 | 100→100 | **yes** | 10→16 |

**Arithmetic audit.** Every recorded NI error in the AFTER lines reproduces from the
filed counts to ≤0.0001. The Oracle ledger's OP chain (45, 40, 40, 50, 60, 70, 80,
75, 70, 80, 90, 100) matches the log's actuals on all twelve. The detection list's
rolling means (0.0166 at P017's window, 0.0159 at P018, 0.0162 at P019) reproduce
exactly once the two drift papers are taken on the absorption basis their own score
records publish; on a uniform sealed basis they read 0.0167 / 0.0159 / 0.0163 — a
difference of ≤0.0001, i.e. an undisclosed basis switch inside one statistic, not an
error. One further entry for the record: P013's original AFTER line asserted a Lean
re-proof that had not in fact run; the log carries its own correction, filed the same
day. The scoring numbers were unaffected; the pattern it shows — the self-grading
pass asserting a verification it had not performed — is noted because Leg C's
protocol is designed to close exactly that hole.

**Findings inside the table itself:**

- **The concept count is a floor, not an estimate.** Signed count errors: ten
  under-predictions, two exact, **zero over-predictions** in twelve papers (mean
  signed error +2.58 concepts). A centered estimator misses both ways; this one
  only ever misses low. Links are worse: under-predicted on **12 of 12** (MAE 5.5;
  P017: 17 foretold, 41 filed).
- **Revisions:** of 9 papers where the seal foretold a revision, 5 were phantoms
  (P009, P010, P013, P014, P018). Foretold-zero landed zero 3 of 3. Count-hits 7/12.
- **The landing papers are the worst-foreseen papers.** Mean |NI error| of the seven
  landing papers (P013–P019): **0.0204**. Of the five non-landing papers (P008–P012):
  **0.0069**. The headline metric and the foresight metric run in opposite
  directions across this record — because, as Leg B shows, they are measuring
  different things.

### Suspicion 1 — band-rule determinism: **confirmed, with arithmetic**

The Oracle's after-value is OP-before + a step chosen from the charter band rule:
NI < 0.20 with no axis → +~10; NI 0.20–0.50 → +~5; axis → hold or fall ~5. The seal
applies the same rule to the predicted NI; the ledger applies it to the actual NI.
An exact landing therefore requires only: same band, same axis call, same choice
inside the "~".

- Predicted and actual NI fell in the same band on **12 of 12** papers. Every actual
  NI in the record sits between 0.0297 and 0.1266 — deep inside a band 0.20 wide.
- **Headroom:** on the eight non-axis papers, the actual NI could have moved toward
  the 0.20 edge by a median of **15× the observed NI error** (range 1.0×–85×) before
  the step could even change. Equivalently: **11 of 12 landings survive a 2× larger
  NI error; 11 of 12 survive a 5× larger one.** The sole exception is P014 — the
  paper with the worst miss of the quest (0.0749); its actual NI (0.1266) stood
  0.0734 from the edge, so a 2× error in the same direction would have crossed it.
- The largest NI miss of the streak (P017, 0.0256 — a 48% relative miss) and the
  largest of the quest (P014, 0.0749) both landed exact. The smallest misses of the
  quest (P010 0.0043, P009 0.0046) did not land at all — their points were set by
  discretionary readings of the "~" (a half-step here, a hold there) that the other
  end of the same house did not reproduce.
- The streak's onset is procedural, not prophetic. P012's seal was the last to
  exercise discretion inside the band (it set +5 against the +10 band and missed by
  exactly that 5). From P013 on, both ends "applied the band as written," chose the
  full step, and formatted the range as ±10 around the point (the ledger's own
  actual ranges are ±10 on every paper; the early seals' asymmetric ranges are the
  only reason early papers could miss on range at all). NI errors did not improve
  when the streak began — they worsened (pre-streak mean 0.0069, streak mean
  0.0204). What converged at P013 was one agent's procedure with itself.
- To the record's credit: the ledger had already priced part of this ("a
  twenty-point band honestly kept will be landed in by honest readings," P017
  weighing; the P019 ceiling discount). This evaluation confirms the house's own
  suspicion and puts numbers on it. The landing streak was never hidden arithmetic;
  it is simply not evidence of foresight, and must stop being read as any.

### Suspicion 2 — self-grading: **confirmed as a bound, ~half the measured error**

The same agent seals, files (deciding folds and splits), and scores. The seals are
git-committed before any full-text access — the blindness is real. What is not
independent is the counting. Sensitivity test, using **only** the alternative
filings the AFTER records themselves name (the units each score says were split out
or folded: P008 ×1, P011 ×1, P012 ×1, P015 ×4, P017 ×6, P018 ×1, P019 ×2):

- Recompute with those units folded as the seal had folded them: concept MAE falls
  **2.58 → 1.25**; mean |NI error| falls **0.0148 → 0.0080**.
- So roughly **half of the skim's measured NI error, and half its concept MAE, is
  filing granularity** — judgment a reasonable filer could resolve either way. In 6
  of the 7 cases the alternative moves the actual *toward* the seal: the filer files
  holding the seal, with its named fold risks in view, and part of every score
  certifies that the two hands are one hand.
- The fair counter-reading, stated because it is also true: the seals often named
  the right joints in prose while pricing them folded (P019's seal listed the
  pipeline's steps; the reading split its maps and searches out of them). The skim
  shows foresight of *structure* and miscounts *grain*; the present scores conflate
  the two. What this record cannot decide — no re-filing by an independent hand
  exists — is how much of the remaining half is foresight either. Leg C pre-registers
  filing rules for the known fold shapes precisely so grain stops being a free
  variable.

### Suspicion 3 — selection: **confirmed, with its confound named**

| Population | n | Skim mean \|NI err\| | Skim concept MAE |
|---|---|---|---|
| Cron picks (skim-selected for proximity + crispness) | 4 | **0.0074** | **1.25** |
| Will-posted (not skim-selected) | 8 | **0.0185** | **3.25** |

The Will-posted sample's errors run ~2.5× the cron sample's. The confound is the
mechanism, not an excuse for it: the cron papers are exactly the near-ground ones
(cluster E once, cluster O three times — no axis papers, no foundings), while the
Will-posted set carries all four axis papers and five cluster foundings. Selection
and distance are one effect seen from two sides: the skim is accurate where a paper
is near held ground, which is where the quest's own criteria aim it. A calibration
figure pooled across the two populations describes the aiming, not the instrument.

---

## Leg B — null models on the same record

Nulls scored in the same terms as the skim. **N1 (band null):** always no axis,
NI = 0.05 flat, Oracle by the band rule, range ±10 (the ledger's own habit), concept
count implied by NI = 0.05 with zero revisions. **N2 (mean null):** NI and concept
count = expanding mean of past actuals; axis = majority of past actuals. **N3
(cluster null):** mean actual delta of past papers in the same cluster, falling back
to the global mean (same-cluster history exists for only 3 of 12 papers — all in
cluster O; everywhere else N3 *is* N2, which is itself a finding about how thin
cluster history is). Head-to-head on the common subset where all are defined
(P009–P019, n = 11):

| Predictor | Mean \|NI err\| | Concept MAE | Axis (of 11) | Oracle exact landings (of 11) |
|---|---|---|---|---|
| **Skim** | 0.0152 | 2.73 | **11** | 7 |
| N1 band null | 0.0183 | 3.15 | 7 | **7** |
| N2 mean null | 0.0164 | 2.99 | 6 | 6 |
| N3 cluster null | **0.0151** | **2.67** | 5 | 5 |

Over all 12 papers, N1 scores **8 exact Oracle landings — more than the skim's 7** —
including P008 (where the seal's own point missed by 7) and P012 (where the seal's
half-step discretion missed by 5). Within the streak, N1 reproduces **5 of the 7**
exact landings bit-for-bit (point and range); it misses exactly the two axis papers,
P015 and P016. More generally: *any* predictor that calls no axis and names any NI
inside (0, 0.20) produces the identical Oracle point and range as the skim on every
non-axis paper in this record. The Oracle outcome carries no information about NI
foresight at all; it carries the axis call and the step convention.

**What the skim adds, per metric:**

- **Oracle landings: nothing.** A constant ties or beats it. This metric should be
  retired as calibration evidence.
- **NI: a small edge over the flat null (~17%), none over the cluster/mean nulls.**
  On the common subset the cluster null's mean |NI error| (0.0151) is a hair *under*
  the skim's (0.0152). The skim's NI foresight, beyond "papers like the recent ones,"
  is not measurable in this record.
- **Concept counts: a small edge over N1/N2 (~0.3–0.4 concepts), none over N3** —
  and all predictors share the skim's under-count shape on the large papers, because
  the large papers are the far ones.
- **Axis: everything.** 12/12 (11/11 on the subset) against fields of 5–8. The four
  yes-calls were each argued in the ledger against written criteria (a field with no
  slot; bridges of shape vs of substance; a cluster founding is not an axis — the
  P011 precedent, applied consistently, including against the skim's own interest at
  P014 and P019). This is the one component where the record shows a skill no flat
  rule has. Its caveat is structural, not numerical: the "actual" is judged by the
  same house that sealed the call. The criteria and the precedent chain are written
  and were applied where they cost the streak nothing and where they could have
  flattered it — but independence is untested, and at n = 12 with 4 positives, the
  honest statement is *supported, not proven*.

---

## What survives, and what the house should stop saying

**Survives:** a blind-sealed, git-committed prediction practice whose arithmetic is
clean; a structure call (axis) that has been right twelve times running under
written criteria; NI foresight at roughly the level of "the recent mean, read with
judgment" — real but modest, best near held ground; and a ledger that had already
discounted its own streak in print before this evaluation was ordered.

**Stops here:** "exact landing" as evidence of calibration, in any summary, in any
chat. The streak is a property of a 0.20-wide band, a shared rule, and a shared
±10 habit. The Oracle at 100% (90–100) is a ceiling artifact of that same band
arithmetic — as the P019 ledger entry itself states — and not a measurement that
the model approaches foreseeing papers whole: the same paper that "landed" at 100%
carried an NI of 0.0445, eleven concepts the skim priced as nine, and sixteen links
it priced as ten.

**Next:** the prospective test is drafted at `evaluation-preregistration.md`
(Leg C) — sharpened seals, nulls scored alongside by construction, pre-registered
filing rules, and pass/fail criteria fixed before the next paper is scored under
it. It waits on Will's stamp. The detection list at 1.1.6 carries this evaluation's
headline as a finding, appended 2026-11-14.
