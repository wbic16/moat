# Prospective test of the skim — PRE-REGISTRATION

> **RATIFIED by Will Bickford, 2026-11-14 02:57 CST, in the MOAT chat**
> ("Stamp the protocol as drafted") — enacted **as drafted, with no
> amendments**. This protocol rests on the evaluation report
> `evaluation-2026-11-14.md` and governs the test phase from Paper 020 onward.

**Status: ENACTED.** This document governs the pre-registered test sample
(§1) from Paper 020 onward. Drafted 2026-11-14 as Leg C of the MOAT
evaluation (task 26.5.7/6.6.9/7.4.8), from the findings of
`evaluation-2026-11-14.md`.

**Purpose.** The retrospective record (Papers 008–019) cannot settle whether the
skim's calibration is real: its headline metric (exact Oracle landings) is an
artifact of the band rule, its NI and count accuracy is statistically
indistinguishable from flat null predictors, its sample was selected for
foreseeability, and its scores are self-graded. This protocol fixes, **before the
next paper is scored under it**, a sample, a seal format, filing rules, and
pass/fail criteria under which the claim can actually lose.

The claim under test, restated so it can fail: *from title and abstract alone, the
skim predicts a paper's filed delta (Index, concept count, axis) materially better
than predictors that read nothing.*

---

## 1. The sample

**Twelve scored papers**, in arrival order, in three strata:

- **5 cron picks** — chosen by the quest's existing criteria (cluster proximity,
  crispness), exactly as now. These measure the skim on the ground it aims at.
- **4 Will-posted papers** — whatever Will posts into MOAT during the window, in
  arrival order. No substitution, no skipping.
- **3 far picks** — chosen by mechanical rule from the cron scans during the
  window: among shortlisted papers passing the charter's crispness bar (a stated
  theorem/result in the abstract; no surveys), the far pick is the one whose
  abstract's stated objects touch the **fewest held clusters**, counted from the
  scan record before any seal is written. Ties break by scan order. This stratum
  exists because the retrospective record shows accuracy collapsing with distance;
  a test without a far stratum tests the aiming, not the instrument.

**No back-end selection:** every sealed paper is scored, including a paper that
proves uncrisp, unreadable, or dull on the full read. A seal may not be withdrawn.

The window closes at 12 scored papers or at Will's call, whichever comes first.

## 2. The sharpened seal

Each seal is git-committed before any full-text access, as now, and carries:

- **NI point estimate and an 80% interval** [low, high] for the actual NI.
- **Concept count point estimate and an 80% interval.**
- **Revision count** (with targets named, as now).
- **Axis as a probability** (0–1), not a bit — e.g. "axis: 0.15". The reasoning
  stays in prose beside it.
- **Link split:** internal and cross-cluster counts, separately.
- **The Oracle statement** continues for the ledger's sake (the charter requires
  it), but it is **not evidence** under this protocol and enters no criterion.

## 3. Filing rules, fixed in advance

The retrospective sensitivity test showed ~half the measured error is filing
granularity. These rules remove the known free variables before the sample starts:

- **Instrument rule** (the P019 lesson): a named map, search, test, or construction
  that the paper's argument uses at two or more distinct points is a concept of its
  own, not a fold inside the step it serves.
- **Split rule** (the P015 lesson): a pair or family is split into separate
  concepts if and only if the paper uses its members apart somewhere; always
  together and never apart = one concept.
- **Grain rule** (the P014 lesson): concepts are counted at the grain of the
  paper's own results — each load-bearing object of a stated result is a concept,
  whether or not the abstract enumerated it.
- **Revision rule** (the P018 phantom): a revision is counted only when a held
  scroll's claim changes its words or its standing. A parallel new price standing
  beside a held one is a new concept, never a revision.
- **Axis rule** (the standing criteria, restated from ledger practice): an axis
  opens iff (a) the paper's centre of gravity is a field or kind of quantity for
  which the model holds no slot, (b) no held concept is merely re-read to receive
  it, and (c) its bridges to held ground are analogies of shape rather than shared
  machinery. A cluster founding is not by itself an axis (the Paper 011
  precedent). The axis *actual* is judged against (a)–(c) in writing at filing
  time, before the score is computed.

Where a rule still leaves a choice on a given paper, the filer records the
permitted alternative in the AFTER line and the score is reported **both ways**
(the headline uses the first filing; the sensitivity line is not optional).

## 4. Scoring

All arithmetic by script from the filed record (the evaluation script, extended);
no hand-computed scores. Nulls are computed by the same script on the same sample:

- **N1** — flat NI 0.05, no axis (axis probability 0.05), concept count implied.
- **N2** — expanding mean of past actuals (within the prospective sample, seeded
  with the retrospective record's means, declared here: NI seed 0.064, count seed
  9.8 — the means of Papers 008–019 actuals, sealed basis).
- **N3** — same-cluster past mean, global-mean fallback, as in the evaluation.

Metrics per paper and pooled: |NI error|, interval coverage, concept-count signed
and absolute error, axis Brier score, link split errors. Reported per stratum and
pooled. The Oracle landing is reported nowhere in the scoring.

## 5. Pass/fail criteria — fixed now

The verdict **"the calibration is real"** requires **all** of:

1. **NI:** skim mean |NI error| ≤ **0.6 ×** the best null's mean |NI error| on the
   same sample. (Retrospective ratio vs the best null: ≈ 1.0. This criterion is
   the distance between the claim and the record as it stands.)
2. **Counts:** skim concept MAE ≤ **0.6 ×** N3's MAE on the same sample, **and**
   |mean signed count error| ≤ **1.0** concept per paper. (Retrospective signed
   mean: +2.58 — a floor, not an estimate. A real calibration is centered.)
3. **Intervals:** the sealed 80% NI intervals cover the actual NI on **7 to 11**
   of the 12 papers. (Under-coverage = overconfidence; full coverage at this width
   = intervals too wide to mean anything. Both fail.)
4. **Axis:** the sample contains ≥ 3 papers whose filed actual is axis-positive;
   the skim's mean axis Brier score ≤ **0.6 ×** the base-rate predictor's; and no
   paper sealed at axis probability ≥ 0.65 either way is filed the other way.
   If fewer than 3 axis-positive papers arrive, the axis component's verdict is
   **untested**, and the overall verdict cannot be "real" — it is "unproven".

The verdict is **"false"** if any of: NI ratio > 0.85; count MAE ratio > 0.85;
|signed count bias| > 2.0; interval coverage ≤ 4 of 12; or any axis criterion in
(4) fails on a sample that contains ≥ 3 axis-positive papers.

Anything else is **"unproven"**, with the per-component verdicts stated
separately (NI / counts / intervals / axis). A split verdict is a legitimate
outcome; the retrospective record already suggests it is the likely one.

## 6. Self-grading — what is and is not mitigated

**Mitigated inside this house:** blind seals, git-committed before full-text
access (already the practice); filing rules fixed in advance (§3); dual-reported
scores wherever a rule leaves a choice; all arithmetic and all nulls by script;
the far stratum chosen by mechanical rule, not by taste; no back-end selection
(§1); criteria fixed in this document before the sample opens.

**Not mitigated, stated plainly:** the filer is the sealer. The axis actual is
judged by the house that sealed the axis call. The Will-posted stratum is Will's
taste, not a random draw. No arrangement inside one house closes these; the only
full fix is a parallel count of at least 3 sample papers by a filer who has not
seen the seals, which requires a person or agent outside this loop and is
therefore **Will's to arrange or waive** — the protocol records the exposure
either way and does not pretend the waiver is a fix.

## 7. Generalizing — sketch only, gated

Will's direction: if the calibration proves real, "we're moving on to other
research areas while generalizing." Operationally, what would generalize is the
**protocol** — blind sharpened seals, pre-registered filing rules, script-scored
nulls, fixed criteria — carried to a second corpus whose map is young (a fresh
tracker over a non-math listing stream, or the phextura research stream), with
cluster distance and the filing rules re-derived on that corpus before its sample
opens. The skim's skill, if real, is the second thing carried; the discipline is
the first. This section is a sketch: the phase opens only on a "real" verdict
**and** Will's word, and its own pre-registration would be written then, not
inherited silently from this one.

---

*Drafted 2026-11-14. Ratified by Will Bickford as drafted on 2026-11-14
02:57 CST (MOAT chat). From Paper 020 onward, sample papers are sealed and
scored under this protocol.*
