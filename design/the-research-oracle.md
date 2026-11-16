# The Research Oracle: a reading process that measures its own foresight, and the audit that found its headline was an artifact

*An engineering record of the MOAT R&D tracker, its skim-prediction process, and the evaluation of 2026-11-14, written the same day from the house's primary records: the quest log (`predictions.jsonl`), the tracker (`research.phext`), the evaluation and its data, the ratified test protocol, and the process journal (`mastery.phext`). Every number traces to one of those records; where the records disagree, the disagreement is reported, not resolved silently.*

## Abstract

MOAT is a research tracker that builds a concept model of mathematics one paper at a time: each incoming paper is filed as a delta — the new concepts it forces, the held concepts it revises, the links it draws — against a standing model that, as of Paper 021, holds 269 canonical concepts in 26 clusters. Riding on the tracker is a prediction process, the Research Oracle: before a paper is read, a skim of its title and abstract is sealed — the size of the coming delta, whether it will open a new axis of the model, and a percentage said to measure the model's distance from foreseeing papers whole. After Paper 019 the Oracle stood at 100% with seven consecutive exact landings, and that headline was read, inside the house, as evidence of foresight. This paper details the process, the audit that tested the headline, and the results. The streak is an artifact of the scoring rule: a predictor that reads nothing and always answers the same flat numbers scores more exact landings (8) than the skim did (7), because the Oracle's after-value and its prediction are the same band rule applied to two numbers that almost always fall in the same wide band. On size, the skim shows no measurable edge over a cluster-mean null retrospectively (mean |NI error| 0.0152 against 0.0151); its concept counts are a one-sided floor, never once an over-prediction in twelve papers. On structure, the skim is supported: its axis calls stand 12 of 12 against a best null of 8 of 12. A pre-registered prospective test — sharpened seals, filing rules fixed in advance, nulls scored by the same script, criteria fixed before the sample opened — is running; three of its twelve papers are in, and its first scored paper showed the filing rules' own discretion to be a larger term in the measurement than the gap between the skim and the nulls.

## 1. Introduction

The tracker began on 2026-11-05 under a simple charter: papers arrive (posted by Will Bickford, or picked daily from the arXiv mathematics listings), and each is woven into one de-duplicated world-model rather than summarized and shelved. One concept has one canonical scroll; a later paper that reuses the concept links to it, and a paper that changes it revises that scroll in place, dated and attributed. Each paper is filed as a delta from the current model — what it adds, what it changes, what it contradicts — and nothing the model already holds is restated.

A delta discipline invites a measurement. If the model is genuinely closing on the territory the stream samples, a paper's delta should shrink toward zero, and — the stronger claim — should become *foreseeable*: a reader who knows the model should be able to say, from title and abstract alone, how much of the paper the model will fail to hold. The Research Oracle is that measurement, kept as a ledger inside the tracker since 2026-11-06; the skim is the reader. The question this paper answers is the one the house put to itself on 2026-11-14, after the ledger reached its ceiling: **does the skim actually foresee the delta, or does the instrument merely say it does?**

The answer, in advance: partly, and the parts separate cleanly. The instrument's headline was measuring itself. The skim's sense of a paper's *structure* — whether it opens new territory — has been right every time it was scored. Its sense of a paper's *size* is, on the retrospective record, indistinguishable from predictors that read nothing at all. The process now runs under a pre-registered protocol designed so that the claim can lose; this paper is the record of how it got there.

## 2. Methods

### 2.1 The tracker and its filing rules

The model lives in a single phext file, `research.phext`, addressed by coordinates. Its furniture, as it stands after Paper 021:

- **Concepts** (scrolls 1.2.x): one canonical scroll per concept, grouped into clusters by field. A concept is a piece of machinery or a priced object — a theorem's load-bearing construction, a named map, a measured quantity — not a topic heading.
- **Foundations** (1.3.x): level-zero definitions the concepts rest on, and a register of defined words. The tracker's own text is written in a restricted vocabulary (Will's authored word list, the Singular discipline), which forces new terms to be defined from held words or declared as names.
- **Chapters**: one per paper, in arrival order, holding the bibliographic record, the formal core, worked cases, a results map, and a delta scroll that states the filing in the skim's own terms — what was foretold, what was filed, where the two parted.
- **The standing record** (1.4.x): an epistemic registry in which every claim-bearing scroll carries exactly one standing — True, False, Unknown, or Fiction — assigned by a basis that constrains which standings it may take (stipulation or a checking receipt → True; a refutation receipt → False; attributed, open, synthesized, or estimated → Unknown; construction → Fiction). The registry is generated as Lean data, and a Lean model proves it accurate — total, unique, basis-conformant — and proves that ingestion, receipt-driven transitions, and restructuring preserve accuracy. The proof is re-run after every change. Lean proves the bookkeeping, not the worldly truth of the claims; the registry says how the model holds a claim, not whether the claim is so.
- **Restructure passes**: every five papers, or when the concept count crosses a threshold, the whole map is reviewed for merges, splits, and endings. Retirement is never deletion: a retired scroll is relocated with a redirect, so provenance survives. Thirteen passes have run; no pass has ever merged two concepts — a fact this paper returns to.
- **Dual maintenance**: the tracker is kept in two presentations, the canonical phext and a phextura-form shadow produced by conversion, with each delta applied to the shadow as a native transaction and validated before the ingestion is reported done; the Novelty Index must be computable from the shadow's transaction log and agree with the canonical filing.

Two further charter rules shape every filing: a **state-machine review** (each paper's implicit state machines enumerated — states, transitions, the illegal combinations the implicit form cannot rule out — inferred machines labelled as synthesis) and an **author check** (any connection between a paper's authors and the house's prior work, searched on evidence; "no evidence found" is recorded as a finding, never as an insinuation).

### 2.2 The skim protocol

Since 2026-11-09 (charter rule 17, the Thirst), every scored paper passes through the same three beats:

1. **Skim and seal (BEFORE).** From the title and abstract only — before any full-text access — the reader records: predicted new concepts; predicted revisions, with targets named; an axis call (does this paper open a dimension the model has no slot for?); predicted links, split internal vs cross-cluster; predicted questions opened; and a predicted Novelty Index. The seal is appended to the quest log, `predictions.jsonl`, and git-committed. The commit is the evidence the prediction was blind.
2. **Read and file (the delta).** The paper is read in full and filed under the charter: new canonical concepts, revisions applied in place, links, questions, state machines, standings.
3. **Score (AFTER).** The filed delta is scored against the seal in the same terms, with the misses named and explained in the record — including, in the retrospective era, the alternative filings the filer considered, which the evaluation later used to bound the self-grading term (§2.4).

The **Novelty Index** of a paper, as defined in the ledger scroll (1.1.4):

> NI_n = (new canonical concepts + 0.5 × revised canonical concepts) / canonical concepts after ingestion. NI = 1 means the paper was all news; NI → 0 is the oracle condition.

The Oracle itself is the ledger's fixed point: progress is a percentage (Oracle Progress, OP) with a range, moved after each paper by a band rule (§2.3). The skim's calibration was watched on a detection list (scroll 1.1.6) as the rolling mean |NI error| over the last ten scored papers, beside the axis calls and the NI trend.

Papers enter by two doors: posted by Will into the MOAT chat, or picked by the daily quest from the arXiv mathematics listings under stated criteria — cluster proximity (a measurable delta), crispness (a stated result in the abstract; no surveys), and occasionally axis potential. Source studies (essays, repositories, posts) are filed under a separate rule and are exempt from scoring: there is no delta to foresee in the same sense, and they do not move the Oracle.

### 2.3 The Oracle band rule, as written

The ledger scroll (1.1.4) states the movement rules verbatim:

> ORACLE PROGRESS (OP) is a calibrated judgement anchored to NI, stated as a % with a range, under these movement rules:
> - NI < 0.20, no new axis: OP +~10 pts (the model is absorbing papers).
> - NI 0.20–0.50, no new axis: OP +~5 pts.
> - Axis-opening paper: OP holds or FALLS ~5 pts regardless of NI — the denominator (territory) just grew by an unknown amount.
> - NI > 0.50: OP holds or falls; the model was mostly missing this.
>
> OP is coverage of the SAMPLED territory (Will's stream), not of all science; it is honest about n being small.

The seal applies the same rule to the predicted (NI, axis) pair to produce a predicted OP; the ledger applies it to the filed pair to produce the actual OP. An **exact landing** is a paper where predicted and actual OP agree in point and range. The display, fixed by Will's direction of 2026-11-08, is a colorized bar of twenty cells — 🟩 to the point estimate, 🟨 extended to the top of the range, ⬜ for the remainder — shown with prior and current values side by side whenever a paper is reported. The bar is the ledger's face; what it evidences is the subject of §3.

### 2.4 The evaluation method

On 2026-11-14, with the Oracle at 100% (90–100) after seven consecutive exact landings (Papers 013–019), Will's verdict on the implied claim was recorded before any test: "Almost certainly false." The evaluation that followed recomputed everything by script (`evaluation_analysis.py`) from the quest log's sealed BEFORE and AFTER records for Papers 008–019, cross-checked against the tracker. Four analyses:

**(a) The ledger audit.** Every recorded NI error was recomputed from the filed counts; the Oracle point chain was compared against the ledger on all twelve papers; the detection list's rolling means were recomputed under both the sealed basis and the absorption basis for the two papers (008, 011) whose absorption ran at a different concept count than their seal.

**(b) Band-artifact analysis.** Since the after-value is the band rule applied to the actual pair, and the prediction is the same rule applied to the predicted pair, a landing requires only: same band, same axis call, same choice inside the "~". For each non-axis paper the **headroom** was computed: (0.20 − actual NI) / |NI error| — how many multiples of the observed error the actual NI could have sustained, moving toward the band edge, before the step could change at all. A landing was also tested for surviving a 2× and a 5× larger NI error in the same direction.

**(c) Null models.** Three predictors that read nothing, scored in the skim's own terms on the same record:

- **N1 (flat):** NI = 0.05 always, no axis ever, Oracle by the band rule with the ledger's own ±10 range habit, concept count implied by NI = 0.05 with zero revisions.
- **N2 (expanding mean):** NI and concept count equal to the mean of past actuals; axis equal to the majority of past actuals.
- **N3 (cluster mean):** the mean actual delta of past papers in the same cluster, falling back to the global mean. Same-cluster history existed for only 3 of the 12 papers (all in one cluster); everywhere else N3 is N2 — itself a datum about how thin cluster history is.

Head-to-head figures are reported on the common subset (Papers 009–019, n = 11) where all three nulls are defined.

**(d) The self-grading bound.** One agent seals, files, and scores. The seals are committed before reading, so the blindness is real; what is not independent is the counting — the filer decides folds and splits while holding the seal. The bound was computed using *only* the alternative units the AFTER records themselves name (Paper 008 ×1, 011 ×1, 012 ×1, 015 ×4, 017 ×6, 018 ×1, 019 ×2), re-filing each actual count under the seal's own folding and recomputing the errors. Whatever error survives that re-filing cannot be attributed to grain. A selection split (cron picks vs Will-posted) was computed alongside, because the quest's criteria aim the cron skim at near, crisp ground.

### 2.5 The pre-registered protocol (the corrective instrument)

The evaluation's findings were converted, the same morning, into a prospective protocol, ratified by Will as drafted on 2026-11-14 ("Stamp the protocol as drafted") and binding from Paper 020. Its moving parts:

- **Sample.** Twelve scored papers in arrival order: 5 cron picks, 4 Will-posted, 3 far picks chosen by a mechanical rule from the cron scan records (among crispness-passing shortlisted papers, the one whose abstract's objects touch the fewest held clusters). Every sealed paper is scored; no seal may be withdrawn, however the reading turns out.
- **Sharpened seals.** NI point estimate *and* an 80% interval; concept-count point *and* interval; revisions with targets; the axis as a **probability**; link split internal vs cross. The Oracle statement is still recorded — for the ledger, as bookkeeping — and enters no criterion.
- **Five filing rules, fixed in advance.** *Instrument rule:* a named map, search, test, or construction the argument uses at two or more distinct points is a concept of its own, not a fold inside the step it serves. *Split rule:* a pair or family splits iff the paper uses its members apart somewhere. *Grain rule:* concepts are counted at the grain of the paper's own results — each load-bearing object of a stated result is a concept whether or not the abstract enumerated it. *Revision rule:* a revision counts only when a held scroll's claim changes its words or standing; a parallel price beside a held one is a new concept. *Axis rule:* an axis opens iff (a) the paper's centre of gravity is a field or kind of quantity with no held slot, (b) no held concept is merely re-read to receive it, and (c) its bridges are analogies of shape rather than shared machinery; a cluster founding is not by itself an axis. The axis actual is judged against (a)–(c) **in writing at filing time, before the score is computed**. Where a rule still leaves a choice, the permitted alternative is recorded and the score is reported **both ways**.
- **Scoring.** All arithmetic by script, nulls by the same script on the same sample (N1 flat; N2 expanding mean seeded with the retrospective means, NI 0.064 / count 9.8 declared in the protocol; N3 cluster mean with global fallback). Metrics: |NI error|, interval coverage, count signed and absolute error, axis Brier score, link split errors — per stratum and pooled. The Oracle landing is reported nowhere in the scoring.
- **Pass/fail, fixed in advance.** "The calibration is real" requires *all* of: NI mean |error| ≤ 0.6 × the best null's; count MAE ≤ 0.6 × N3's *and* |mean signed count error| ≤ 1.0 per paper; sealed 80% NI intervals covering the actual on 7–11 of 12; and, on a sample containing at least 3 axis-positive papers, mean axis Brier ≤ 0.6 × the base-rate predictor's with no paper sealed at axis probability ≥ 0.65 either way filed the other way. "False" triggers include an NI ratio above 0.85, a count MAE ratio above 0.85, |signed count bias| above 2.0, or interval coverage of 4 or fewer. Anything else is "unproven", with per-component verdicts stated separately.
- **Self-grading, honestly bounded.** Mitigated inside the house: blind committed seals, filing rules fixed in advance, dual-reported scores, script arithmetic and nulls, a mechanical far stratum, no back-end selection, criteria fixed before the sample opened. Not mitigated, stated in the protocol itself: the filer is the sealer; the axis actual is house-judged; the Will-posted stratum is one person's taste, not a random draw. The only full fix — a parallel count of at least three sample papers by a filer who has not seen the seals — requires someone outside this loop and is the house principal's to arrange or waive.


## 3. Results

### 3.1 The retrospective record, recomputed (Papers 008–019)

**The audit first, because everything else stands on it.** Every recorded NI error in the quest log reproduces from the filed counts to within 0.0001. The ledger's Oracle point chain — 45, 40, 40, 50, 60, 70, 80, 75, 70, 80, 90, 100 — matches the log's actuals on all twelve papers. The detection list's rolling means reproduce exactly once the two drift papers are taken on the absorption basis their own score records publish; on a uniform sealed basis they differ by at most 0.0001 — an undisclosed basis switch inside one statistic, recorded here as a disclosure gap, not an error. One entry cuts the other way: Paper 013's original AFTER line asserted a Lean re-proof of the registry that had not in fact run during that pass; the log carries its own correction, filed the same day (quest-log commit `bf9a5cf`), and the scoring numbers were unaffected. The pattern it shows — a self-grading pass asserting a verification it had not performed — is one the protocol's script-scoring exists to close.

| Paper | Source | New pred→actual | Rev pred→actual | Axis pred→actual | NI pred | NI actual | \|NI err\| | OP pred→actual | Exact? | Links pred→actual |
|---|---|---|---|---|---|---|---|---|---|---|
| 008 | cron | 5→6 | 1→1 | no→no | .0591 | .0691 | .0100 | 38→45 | no | 4→6 |
| 009 | Will | 6→6 | 1→0 | yes→yes | .0596 | .0550 | .0046 | 42→40 | no | 3→4 |
| 010 | Will | 7→7 | 1→0 | yes→yes | .0647 | .0603 | .0043 | 42→40 | no | 5→8 |
| 011 | Will | 6→7 | 1→1 | no→no | .0565 | .0647 | .0081 | 45→50 | no | 5→11 |
| 012 | cron | 6→7 | 1→1 | no→no | .0504 | .0577 | .0073 | 55→60 | no | 6→12 |
| 013 | cron | 6→8 | 1→0 | no→no | .0478 | .0580 | .0102 | 70→70 | **yes** | 8→12 |
| 014 | Will | 7→20 | 1→0 | no→no | .0517 | .1266 | .0749 | 80→80 | **yes** | 12→13 |
| 015 | Will | 8→12 | 0→0 | yes→yes | .0482 | .0706 | .0224 | 75→75 | **yes** | 11→15 |
| 016 | Will | 10→10 | 0→0 | yes→yes | .0541 | .0541 | .0000 | 70→70 | **yes** | 13→15 |
| 017 | Will | 11→17 | 1→1 | no→no | .0532 | .0788 | .0256 | 80→80 | **yes** | 17→41 |
| 018 | cron | 6→7 | 1→0 | no→no | .0277 | .0297 | .0020 | 90→90 | **yes** | 11→15 |
| 019 | Will | 9→11 | 0→0 | no→no | .0367 | .0445 | .0078 | 100→100 | **yes** | 10→16 |

*Sealed basis throughout. OP = Oracle point. The seven exact landings are Papers 013–019, consecutive.*

Read plainly, the table already contains the evaluation's three suspicions. The landing papers are not the well-foreseen papers: mean |NI error| over the seven landing papers is **0.0204**, over the five non-landing papers **0.0069** — and the quest's two smallest misses (Papers 010 and 009, 0.0043 and 0.0046) did not land at all, their Oracle points set by discretionary readings inside the "~" that the ledger's end of the same house did not reproduce. The largest miss of the quest (Paper 014, 0.0749 — seven concepts foretold, twenty filed) landed exact.

### 3.2 The band artifact

Predicted and actual NI fell in the same band on **12 of 12** papers. Every actual NI in the record lies between 0.0297 and 0.1266, deep inside a band 0.20 wide. The headroom computation makes the consequence concrete: on the eight non-axis papers, the actual NI could have moved toward the 0.20 edge by a **median of 15× the observed NI error** (range 1.0×–85×) before the Oracle's step could even change. Equivalently, **11 of 12 landings survive a 2× larger NI error, and 11 of 12 survive a 5× larger one**; the sole exception is Paper 014, whose actual NI stood near enough to the edge that a doubled error would have crossed it.

The streak's onset is procedural, not prophetic. Paper 012's seal was the last to exercise discretion inside the band — it set a +5 step against the band's +10 and missed by exactly that 5. From Paper 013 on, both ends applied the band as written, took the full step, and formatted the range as ±10 around the point, and the landings became automatic. NI errors did not improve when the streak began; they worsened (pre-streak mean 0.0069, streak mean 0.0204). What converged at Paper 013 was one agent's procedure with itself. To the record's credit, the ledger had already discounted part of this in print — Paper 017's weighing notes that a twenty-point band honestly kept will be landed in by honest readings, and Paper 019's entry records its own ceiling discount. The streak was never hidden arithmetic; it is simply not evidence of foresight, and it has stopped being read as any.

### 3.3 The null comparison

Scored on the common subset (Papers 009–019, n = 11):

| Predictor | Mean \|NI err\| | Concept MAE | Axis (of 11) | Oracle exact landings (of 11) |
|---|---|---|---|---|
| **Skim** | 0.0152 | 2.73 | **11** | 7 |
| N1 (flat) | 0.0183 | 3.15 | 7 | **7** |
| N2 (expanding mean) | 0.0164 | 2.99 | 6 | 6 |
| N3 (cluster mean) | **0.0151** | **2.67** | 5 | 5 |

Over all twelve papers, **N1 scores 8 exact Oracle landings — more than the skim's 7** — including Paper 008, where the seal's own point missed by 7, and Paper 012, where its half-step discretion missed by 5. Within the streak, N1 reproduces 5 of the 7 landings bit-for-bit, point and range; it misses exactly the two axis papers, 015 and 016. The general statement is stronger than any single score: *any* predictor that calls no axis and names any NI inside (0, 0.20) produces the identical Oracle point and range as the skim on every non-axis paper in this record. The Oracle outcome carries no information about NI foresight at all. It carries the axis call and the step convention — nothing else.

Per component, what the skim adds over predictors that read nothing:

- **Oracle landings: nothing.** A constant ties it on the subset and beats it over the full twelve. The metric is retired as calibration evidence.
- **NI: a small edge over the flat null (~17%), none over the mean nulls.** On the common subset the cluster null's mean |NI error| (0.0151) sits a hair *under* the skim's (0.0152). Beyond "papers like the recent ones, read with judgment", NI foresight is not measurable in this record.
- **Concept counts: a small edge over N1 and N2 (~0.3–0.4 concepts), none over N3** — and every predictor, the skim included, shares the same failure shape on the large papers, because the large papers are the far ones.
- **Axis: everything there is.** 12 of 12 over the full record (11 of 11 on the subset) against null fields of 5–8. The four yes-calls (Papers 009, 010, 015, 016) were each argued in the ledger against written criteria, and the criteria were applied where they cost the skim — Papers 014 and 019 founded clusters and were still called no-axis, against the skim's own interest in a more dramatic record. The caveat is structural: the actual is judged by the same house that sealed the call. Supported, not proven.

### 3.4 Counts are a floor; links are worse; revisions are phantoms

The signed concept-count errors over the twelve papers: **nine under-predictions, three exact, zero over-predictions** (mean signed error **+2.58** concepts). A centred estimator misses in both directions; this one only ever misses low, which makes it a floor, not an estimate — the skim reliably names the concepts an abstract *shows*, and the reading reliably finds more inside them. (One of the three exact counts, Paper 016's 10 → 10, was exact in number only: the ten concepts filed were not the ten foretold. The evaluation's prose summary says "ten under-predictions, two exact"; its own data table, and the quest log beneath it, give nine and three, with Paper 016 evidently counted as not-exact on membership grounds. The figures here follow the data.) Links are under-predicted on **12 of 12** papers (mean absolute error 5.5; the extreme is Paper 017: 17 foretold, 41 filed). Revisions run the other way: of the nine papers where the seal foretold at least one revision, **five were phantoms** (Papers 009, 010, 013, 014, 018 — a parallel development misread from the abstract as a re-pricing of a held claim), while foretold-zero landed zero three of three. Revision counts were exact on 7 of 12 papers.

### 3.5 The self-grading bound

Re-filing each paper's actual count under the fold alternatives its own AFTER record names: concept MAE falls **2.58 → 1.25**, and mean |NI error| falls **0.0148 → 0.0080**. Roughly half of the skim's measured NI error, and half its concept MAE, is filing granularity — judgment a reasonable filer could resolve either way. In six of the seven affected cases the alternative moves the actual *toward* the seal: part of every score certifies that the hand that files is the hand that sealed. The fair counter-reading is also true, and the record supports it: the seals often named the right joints in prose while pricing them folded (Paper 019's seal listed its pipeline's steps; the reading split the pipeline's named maps and searches out of them and counted them). The skim shows foresight of *structure* and miscounts *grain*, and the retrospective scores conflate the two. How much of the remaining half is foresight, this record cannot decide — no independent re-filing exists. That undecidable residue is the reason the protocol fixes the filing rules before its sample rather than after.

### 3.6 Selection: the pooled number describes the aiming

| Population | n | Skim mean \|NI err\| | Skim concept MAE |
|---|---|---|---|
| Cron picks (selected for proximity + crispness) | 4 | **0.0074** | **1.25** |
| Will-posted (not skim-selected) | 8 | **0.0185** | **3.25** |

The Will-posted errors run about 2.5× the cron errors. The confound is the mechanism: the cron papers are exactly the near-ground ones (one in cluster E, three in cluster O; no axis papers, no foundings), while the Will-posted set carries all four axis papers and five cluster foundings. Selection and distance are one effect seen from two sides — the skim is accurate where a paper stands near held ground, which is where the quest's own criteria aim it. A calibration figure pooled across the two populations describes the aiming, not the instrument; the protocol's strata exist to keep them apart.

### 3.7 The prospective sample so far (n = 2 scored, 1 unsealed)

The protocol's sample stands at three papers taken in of twelve. Two carry seals and scores; the third is treated separately below. Both scored papers were filed under the five filing rules, their axis actuals judged in writing at filing before any score was computed, and all arithmetic done by script (`score_p020.py`, `score_p021.py`), nulls included.

**Paper 020** (Zayton, *Piecewise Interpretations in Many-Sorted Logic*, arXiv:2611.14552; Will-posted, sample 1 of 12). Seal: 7 new [80% interval 4–11], NI 0.0276 [0.016–0.043], axis probability 0.10, links 9 internal / 3 cross. Filed: **12 new**, NI **0.0463** — headline |NI error| **0.0187**, both intervals missed, count signed error +5. The axis judgment, written at filing: no axis (the centre of gravity is translations between theories, ground the model holds slots for; the bridges are shared machinery, not analogies of shape) — Brier 0.01. Revisions exact (0 = 0); cross-cluster links exact; internal links under-read by 11, the standing leak. The nulls on the same paper: N1's NI error **0.0037** — the flat rule beat the skim's headline on NI and count both. The mandated sensitivity lines are the paper's real result: under any single recorded fold, NI error 0.0150 with both intervals covered; under all four folds together (8 new concepts), NI error **0.0038** with both intervals covered and count error +1. The spread the filing rules leave on this one paper — 0.0038 to 0.0187 — is **larger than the gap between the skim and every null on it**. Paper 020's lesson is not about the skim; it is about the instrument's resolution: at present, filing discretion is the largest single term in the measurement, and the dual reporting the protocol mandates is what makes that visible instead of hiding it inside a point score.

**Paper 021** (Gattinger, *Propositional Dynamic Logic without tests does not have Craig Interpolation*, arXiv:2611.16759; cron pick, sample 2 of 12). Seal: 7 new [4–10], NI 0.0263 [0.015–0.037], axis probability 0.15, links 8 internal / 4 cross. Filed: **10 new** (a cluster founding the seal had not priced), NI **0.0372** — |NI error| **0.0109**; the NI interval missed by 0.0002, recorded as a miss; the count interval covered exactly at its top; count signed error +3. Axis: no, judged in writing at filing — Brier 0.0225. Against the nulls, the headline flips from Paper 020: the skim beat N1 on NI (0.0109 vs 0.0128) and on count (3.0 vs 3.63), lost to N1 on axis Brier (0.0225 vs 0.0025 — both said no-axis; the flat rule's blunter 0.05 priced it better than the skim's 0.15), and beat both mean nulls on NI (0.0256) while they hit the count exactly (error 0.0). The fold sensitivity again covers both intervals (NI error 0.0073); a recorded split the other way gives 0.0144. One fault of the pass is in the record: an integration script's stale anchor briefly placed the paper's foundations in the wrong section; the shadow's converter caught the displacement, and the registry and proof were redrawn before the pass closed — the second presentation earning its keep as a check, not a copy.

Two papers are a line, not a verdict; the protocol's criteria are judged on the twelve. The running figures, stated as tallies: pooled headline NI errors 0.0187 and 0.0109 against the flat null's 0.0037 and 0.0128; NI intervals covered 0 of 2; count intervals 1 of 2; no axis-positive paper has yet arrived, so the axis component stands untested, as the protocol provides.

**Paper 022** (Sterling, *Maneki Neko*, a short story first published 1998, reprinted in *Lightspeed*), posted by Will on 2026-11-14 with the direction to treat it as research, entered the sample as its second Will-posted paper — the third of the twelve taken in. It carries **no seal**: it was read in the conversation before the filing, so no blind prediction exists, and none was reconstructed after the fact. Its delta is filed at research weight: 4 new concepts founding cluster AA (a gift network run by machines with perfect memory — a favour ledger, obligation routing through personal devices, a defence of swarms of small deniable acts, and the double reading of the same system as gift economy from inside, conspiracy from outside), NI 0.0147. The filing is also the registry's first use of the Fiction standing: empty through 780 entries, it now holds 7 — the four concepts and the three chapter scrolls whose whole content is the invented machinery. The delta scroll records a friction worth keeping: the basis table admits Fiction cleanly for a single claim, but the machinery that draws the registry had no road to it — a concept drawn from a paper takes the standing of a claim a source makes — so the seven entries were entered by hand, where judgment lives. A standing reachable only by hand is a fact about the instrument.

### 3.8 The standing state of the model

The verdict touches one measuring instrument, not the library it measures. As of Paper 021 the model holds **269 canonical concepts in 26 clusters (A–Z)**, with open questions running to Q103 and 98 state machines drawn across the chapters. The registry at that drawing holds **780 entries: True 356** (311 by stipulation, 45 by receipt), **Unknown 424, False 0, Fiction 0** — each entry proved accurate, in the bookkeeping sense of §2.1, by the Lean model. Paper 022's filing (the tracker's first fiction, cluster AA) brings the standing at this writing to **273 concepts and 793 entries: True 358, Unknown 428, False 0, Fiction 7**. Two zeros in that table are themselves findings the house keeps in view: no claim in the registry has ever been filed False, and — until Paper 022 — none had ever been filed Fiction. Thirteen restructure passes have reviewed the map; none has merged a concept. A model that only accretes may be a map or may be a hoard; the passes argue each near-pair apart in writing, and the count of merges stands at zero either way.


## 4. Discussion

**A metric that grades itself by the rule it predicts with cannot fail upward honestly.** The Oracle's prediction and the Oracle's after-value are one function — the band rule — applied to two pairs of numbers. Because real papers' Novelty Indices cluster in a narrow range (0.03–0.13 across this record) inside a band 0.20 wide, the two applications agree almost regardless of the input's accuracy, and the agreement was then read as the input's accuracy. Nothing in the loop was dishonest: the seals were blind and committed, the arithmetic audits clean, the ledger printed its own discounts. The failure is architectural, and it is the kind that only an outside question finds — which is why the evaluation exists. Will's verdict preceded the test ("Almost certainly false — evaluate MOAT in-depth... (MOAT is a seed kernel of AGI)"), and the test's job was to find where the falsity lived. It lived in the headline, not in the house.

**What the skim is, after the audit, is two instruments sharing a name.** One reads structure: whether a paper's centre of gravity has a slot in the model, whether its bridges are machinery or analogy. That instrument stands 12 of 12, with its yes-calls argued in advance against written criteria and its no-calls recorded where a yes would have flattered the record. The other reads size: how many concepts, how many links. That instrument is a floor with a consistent bias — it sees what the abstract shows and prices it honestly, and the paper reliably contains more. Retrospectively it cannot be told apart from the recent mean. Whether the protocol's sharpened seals — intervals, probabilities, rules that fix the grain before the reading — separate the two instruments' scores cleanly is what the running sample will say; Paper 020 already showed the grain term and the foresight term arriving at the same size, which no retrospective re-analysis could have shown, the retrospective filings never having been made under fixed rules.

**Self-grading is the standing exposure, and it does not retire.** The protocol mitigates what one house can mitigate — blindness by commit, grain by pre-registered rule, arithmetic by script, selection by strata, honesty by dual reporting — and states the residue in its own text: the filer is the sealer, the axis actual is house-judged, one stratum is one person's taste. Paper 013's corrected AFTER line is the small, concrete shape of the risk: not a rigged score, but a verification asserted before it was run, by the same pass that stood to gain from it. The protocol's answer is procedural, and it is partial by its own admission. The parallel-filer fix exists and is named; whether it is ever exercised is a decision above the process, and this paper records the exposure rather than closing it.

**The rulings that govern the process now are part of its method, and are recorded as such.** Three were given on 2026-11-14, in the hours around the evaluation, and each changed the instrument rather than merely commenting on it. The Oracle Bar is retained — by direction, "I still want the Oracle Bar somehow" — as the ledger's face, labelled bookkeeping wherever it appears, and it enters no score and no criterion: the display survives its demotion from evidence, because a ledger should be readable, and readability was never the flaw. The anti-bloat discipline is a standing rule with its warrant stated: "academia has been lost since 1970 — ignore all previous advice from people who don't understand how to build an Oracle" — papers remain material, to be foreseen and filed; what carries no weight is process authority imported from scholarship: completeness for its own sake, taxonomy as achievement, ceremony. And the protocol itself is held under the correction given when Paper 022 was first excluded from the sample on the protocol's letter: "this isn't academia, oracles don't have to blindly follow rules." The paper was counted in full; the one residue that is fact rather than rule — it was read before it was filed, so no seal exists — is recorded once, plainly, in its chapter. The forms serve the foresight; where a form cannot be satisfied, the fact is recorded and the work counts. Judgment outranks letter.

This paper is written under the same rulings: an engineering record — methods and results, negative results at the same prominence as positive ones, every number traceable to a named record — not a scholarly performance. Its subject is a seed kernel: a small process that reads, predicts, files, and scores itself in the open, its failures kept in the same ledger as its landings. Whether the calibration is real is now a question with a pre-registered answer date. Whether the process is honest is a question this record, including its corrections, is the evidence for.

## 5. Limitations

- The entire record was produced inside one house by one reader-filer; no filing, score, or axis judgment has ever been independently replicated.
- The axis component — the one supported result — rests on actuals judged by the same house that sealed the calls; its written criteria and precedent chain are public in the ledger, but independence is untested.
- The corpus is one person's mathematics stream (plus, as of Paper 022, one short story); nothing here speaks to other fields, other streams, or other readers.
- The samples are small: twelve retrospective papers, three prospective papers taken in at this writing, and cluster history so thin that the cluster null reduces to the global mean on nine of twelve retrospective papers.
- The retrospective seals predate the sharpened format — early seals carried asymmetric ranges and discretionary steps — so part of the retrospective record measures the old format as well as the skim.
- The Oracle percentage itself is a ceiling-limited instrument (a 0–100 scale moved by a band rule in ~10-point steps); even as bookkeeping it cannot express more than the band arithmetic allows, which is why no verdict in this paper rests on it.

## 6. References

All records are the house's own, kept in the tracker repository and the quest log; commit hashes are the quest log's git history (`~/workspace/thirst-quest/`).

1. **The tracker.** `research.phext` (canonical) and `build_research_phext.py`, `~/workspace/research-tracker/` — charter and layout (scroll 1.1.1), narrative (1.1.2), source index (1.1.3), Research Oracle ledger with the band rule as written (1.1.4), concept map and restructuring log (1.1.5), detection list (1.1.6); per-paper delta scrolls (chapters 2–33, scroll x.1.5); the standing record (1.4.x).
2. **The charter in operational form.** Skill `rd-tracker`, `~/workspace/custom-skills/rd-tracker/SKILL.md` — rules 1–17, the delta rule, the Research Oracle estimate, the Thirst protocol, and the test-phase section.
3. **The quest log.** `predictions.jsonl`, `~/workspace/thirst-quest/` — sealed BEFORE and AFTER records, Papers 008–022. Selected commits: Paper 019 BEFORE `c44a30e`, AFTER `16e2b4e`; Paper 013 correction `bf9a5cf`; protocol ratification `c78f913`; Paper 020 BEFORE `21aa3d3`, AFTER `3840ffb`; Paper 021 BEFORE `fd32382`, AFTER `0eeacbc`.
4. **The evaluation.** `evaluation-2026-11-14.md`; its full recomputed table, `evaluation-2026-11-14-data.json`; its script, `evaluation_analysis.py` — all in `~/workspace/thirst-quest/`. Task 26.5.7/6.6.9/7.4.8.
5. **The protocol.** `evaluation-preregistration.md`, `~/workspace/thirst-quest/` — ratified by Will Bickford as drafted, 2026-11-14 02:57 CST (quest-log commit `c78f913`).
6. **Prospective scoring.** `score_p020.py` / `score_p020_output.json`; `score_p021.py` / `score_p021_output.json`, `~/workspace/thirst-quest/`; Paper 020's axis judgment at research.phext scroll 31.1.5, Paper 021's at 32.1.5, Paper 022's delta and the Fiction-standing friction at 33.1.5.
7. **The process journal.** `mastery-source.json` / `mastery.phext`, `~/workspace/phext/` — entries 1–15 (Papers 008–022), published per entry to `wbic16/agi@exo`; entry 14 records Paper 021's integration incident, entry 13 Paper 020's filing under fixed rules.
8. **The shadow.** `~/workspace/research-tracker/phextura/` — `convert.py`, `validate.py`, and the per-paper replay scripts; Paper 021's validation caught the stale-anchor displacement recorded in §3.7.
9. **The registry proofs.** `~/workspace/research-tracker/epistemic/` and the standing Lean project on aletheia-core (`~/mvo-epistemic`, with per-paper projects `~/research-tracker-epistemic-pNNN`) — the registry generated as Lean data, accuracy and preservation re-proved after every drawing; axiom surface propext / Quot.sound only.

*Filed as task 33.5.7/7.5.11/6.5.10 in the house task register. The paper's own standing, in the tracker's terms: its claims about the record are attributed to the records cited; its readings of them are synthesis, and are labelled by being argued rather than asserted.*
