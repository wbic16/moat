# Assay / TLUF — Branding Pack (working draft)

*DRAFT — prepared 2026-11-14 for Will Bickford's review. Not inscribed in artifacts.phext, not published, not in force. Nothing in this file is public copy until Will stamps it. Spec of record: `REQUIREMENTS.md` in this directory — where this draft and the requirements differ, the requirements govern.*

*Purpose: public surface copy for the hosted assessment service, written for two audiences that punish vagueness in different ways — LessWrong (calibration, explicit uncertainty, published misses, null models, pre-registration, no hype) and arXiv readers (descriptive titles, standard terminology, abstracts that state problem, method, evaluation, and limits, stable categories, versioning, machine-readable records). One naming system, two registers. The service's facts do not change between registers; only the emphasis does.*

---

## 1. The name lockup and first-mention expansions

**Lockup (both audiences):**

> **Assay** — claim-level assessment of preprints, at **tluf.org**
> **TLUF**: truth, lies, unknown, fiction — the four standings every assessed claim receives.

Order matters: the service name first (Assay is what a researcher uses), the frame second (TLUF is what the service serves). Never "TLUF by Assay," never "the Assay platform," never any form of "Oracle" as a product name — Oracle is a software company and an internal process name, and it promises prophecy the service does not sell.

**First mentions — arXiv register:**

- **Assay** — "Assay, a hosted service that decomposes a submitted preprint into its individual claims and assigns each claim one of four standings (true, false, unknown, fiction) on a stated basis."
- **TLUF** — "TLUF (truth, lies, unknown, fiction), the four-standing scheme the assessment applies." *(The Lies/False seam in this expansion was ruled on by Will, 2026-11-14 — see §7: the bin stays False, and lies are its malicious subset, tracked by failure kind.)*
- **phext** — "phext, a plain-text format that stores text at nine-dimensional coordinates, used here as the assessment record's storage format; the record is the researcher's property and is exportable in full."

**First mentions — LessWrong register:**

- **Assay** — "Assay is a preprint assessment service built around a refusal: it never returns accept or reject. It returns a claim-by-claim reading instead."
- **TLUF** — "TLUF — truth, lies, unknown, fiction — is the binning scheme: every claim extracted from a paper is placed in exactly one bin, on a stated basis, and the basis is part of the record."
- **phext** — "The assessment is delivered as a phext (a coordinate-addressed plain-text document). You own it; joining the public commons is your choice, per paper, and merging requires every author of record to authenticate and attest to the exact edition being merged."

After first mention: Assay, TLUF, and phext are used bare, lowercase for phext (it is a format, not a brand), capitals for Assay and TLUF.

---

## 2. The descriptive subtitle (one sentence, two registers)

**arXiv register** (for paper titles' subtitles, the service's about page, and repository descriptions):

> Assay is a hosted service that decomposes submitted preprints into individual claims, assigns each claim one of four standings — true, false, unknown, or fiction — on a stated basis, and returns the resulting record to the researcher, who owns it.

**LessWrong register** (for the introductory post and community-facing pages):

> Assay reads a preprint the way a careful referee would if referees published their working: claim by claim, each claim binned as true, false, unknown, or fiction with its grounds stated — including the claims where the honest bin is "unknown," and including our own published record of where this binning process has been wrong.

Both sentences say the same thing. The arXiv sentence leads with the procedure; the LessWrong sentence leads with the epistemic posture and ends on the published error record, because that is the claim that audience will check first.

---

## 3. Taglines

**The house line** (Will's, verbatim, internal and ceremonial use — not proposed as public copy unless Will says so):

> tluf.org: the assayist for the future

**Public variants proposed** (shortest first; all are candidates for Will to cut, none are adopted):

1. "Every claim, binned. Every basis, stated."
2. "Assessment without verdicts."
3. "We test what you bring in. You keep the ore."
4. "The shape survives, even when the nuance fails."
5. "Preprint assessment that publishes its own error rate."

Notes: variant 3 carries the assayer ethic from the requirements (the assayer never owns the ore) and is the only variant that mentions ownership — if one line must serve both audiences, it is the strongest candidate. Variant 5 is LessWrong-register only; arXiv surfaces should carry the descriptive subtitle instead of a tagline. No variant uses "revolutionary," "AI-powered," "oracle," "AGI," or a superlative.

---

## 4. Abstract skeleton (for service and process write-ups)

Every public write-up of the service or its process — paper, post, or long README — follows this shape. Bracketed text is instruction, not copy.

> **[Problem]** [One to three sentences. Preprint assessment today returns a single verdict (accept/reject, or a review score) over a whole paper, which discards correct structure when individual claims fail and gives authors no claim-level account of what was found wanting. State the cost plainly; name who bears it — independent and fringe researchers first, because venue and pedigree act as unstated filters on the verdict route.]
>
> **[Method]** [The decomposition procedure: claims extracted per claim; each claim assigned exactly one of four standings — true, false, unknown, fiction — by a basis code that constrains which standings it may take; the paper's shape (the correct structure, independent of whether its detailed claims hold) extracted as a first-class result; each failure given its breaking line. The produced record is a phext owned by the researcher; commons membership is per paper; merge requires authentication and attestation from every author of record, bound to the edition checksum.]
>
> **[Evaluation]** [Numbers, with the comparison class named. Any foresight or reliability claim is reported against stated null models (at minimum: a flat-rate predictor, an expanding-mean predictor, and a same-cluster mean predictor), under criteria fixed before the test sample was scored, with misses reported at the same prominence as hits. Current standing, stated as of writing: the binning-reliability measure stands at ~62% (range 55–70) across four gates — true gate met, unknown gate met, fiction gate half-met, false gate unmet. If a number in this section cannot be recomputed from published records, it does not appear.]
>
> **[Limits]** [What the instrument cannot currently do, in the same type size as the results: the false bin has not yet been exercised on grounded filings in the tracker's diet; fiction standings are entered by hand, not yet by the machinery; the assessor and the forecaster are the same house, and that exposure is mitigated by committed-in-advance predictions and script-scored results, not eliminated. Venue and pedigree are never inputs to a binning; if a future version changes that, it is a different service and must say so.]

A write-up that cannot fill the Evaluation section does not get written yet. A write-up whose Limits section is shorter than its Evaluation section gets sent back.

---

## 5. Lexicon — house term → public term

| House term | Public term | Reason |
|---|---|---|
| spaghettification | claim decomposition | The house word is vivid and unexplained; "decomposition" is the standard term both audiences already use for the same act. |
| the Oracle (as product) | Assay; the assessment record | "Oracle" is another company's name and promises prophecy; the service returns a record, not a pronouncement. |
| MOAT | the assessment process (internal name on first mention only) | An unexplained acronym reads as pedigree signalling; the process is described, not branded. |
| crackpot | fringe / independent researcher | The house's market is the fringe; the public word must not insult the customer or prejudge the binning. |
| bins (as a verb, unexplained) | assigns one of four standings | "Standing" is the requirements' own word and carries the basis with it; "bin" alone sounds like disposal. |
| shape (bare) | the paper's structure — what it got right about the problem's form | "Shape" is house shorthand; in public it is expanded on first use, every time, because the whole service turns on it. |
| novelty score | novelty vector (four components, never a single number) | A "score" invites collapse to one figure; the requirements forbid the collapse, so the copy must too. |
| receipts | evidence | House rule, and the plainer word. |
| skim | pre-registered advance estimate | The skim's value is that it is committed before reading; the public name states the property that makes it evidence. |
| the commons | the commons | Kept as-is: already plain, already accurate, and the ownership terms beside it do the explaining. |
| phext (bare) | phext, a coordinate-addressed plain-text format | The format is unfamiliar to both audiences; it earns one appositive at first mention and none after. |
| researcher standing | researcher record | "Standing" is used for claims; reusing it for people invites a league-table reading the vector is designed to prevent. |

---

## 6. Claims we do not make

- **No AGI claims.** Nothing about the service is described as AGI, a step to AGI, or evidence about AGI timelines. The process is a reading discipline with a scoring record; that is the whole claim.
- **No unqualified accuracy.** No percentage appears without its gates, its range, and its date. The current public form is: "binning reliability ~62% (55–70), four gates: true met, unknown met, fiction half-met, false unmet" — and when a gate's standing changes, the sentence changes the same day.
- **No verdict language.** The service does not "accept," "reject," "certify," or "validate" papers. It assesses claims and returns a record. (A certificate in the assayer's sense — a statement of what the material contains — is the strongest word allowed, and only in that sense.)
- **No foresight claims beyond the scored record.** The house's own evaluation found its earlier headline calibration figure was an artifact of its scoring bands and published that finding; public copy cites the corrected record and the ongoing pre-registered test, never the retired headline.
- **No pedigree claims, in either direction.** Neither "from the lab that brought you" nor "outsiders academia ignored." The service's handling is identical for affiliated and unaffiliated authors, and the copy says exactly that and nothing warmer.
- **No single-number researcher rankings.** Novelty is a four-component vector; copy never sums it, averages it, or ranks researchers by it.
- **No ownership ambiguity.** Copy never implies the service holds rights in submitted or produced material. The researcher owns the produced phext; commons membership is per paper, chosen, and attested.
- **No silence about the false gate.** Until grounded false filings exist and survive re-examination, every public description of the four standings notes that one of the four is untested. The gap is printed, not footnoted.

---

## 7. Lies or False? — ruled by Will, 2026-11-14

**The tension, stated plainly.** TLUF expands to *truth, lies, unknown, fiction* — your words, and the Directive's third line. But the operational bins in the tracker and the requirements are **True / False / Unknown / Fiction**: a claim is filed False on stated grounds (a counterexample, an internal break, a collision with a named held True), with no finding about its author's intent. "Lies" and "False" are not the same claim. A lie is a falsehood told knowingly; most false claims in preprints are errors, not lies. The acronym says one thing; the machinery does another. This draft does not resolve it — both public expansions above are written so either ruling can be dropped in — but it cannot stay unresolved in public copy, because the first careful reader (and both target audiences are careful readers) will find the seam.

**Option A — public expansion keeps "lies"; bins stay True/False/Unknown/Fiction, with the seam explained.**
- Keeps TLUF pronounceable and your expansion intact; the domain, the Directive line, and the acronym agree.
- Cost: every public surface carries a standing explanation that the second bin is "false" in operation and "lies" only in the acronym's poetry — an explanation that reads, to a LessWrong reader, like a motte-and-bailey in miniature: the strong word in the name, the weak word in the fine print.
- Risk: submitters hear "lies" as an accusation the service then has to walk back per paper.

**Option B — the second bin is renamed "Lies" in operation too, with an intent standard.**
- The name and the machinery agree exactly; no fine print.
- Cost: the bin becomes nearly unusable. Filing a claim as a *lie* requires evidence of the author's knowledge and intent, which an assessment of a text almost never has. The false gate is already unmet with the weaker standard; under an intent standard it would be unmeetable, and wrong-but-honest work — the fringe's most common kind — would have no accurate bin except Unknown, which would corrupt the Unknown bin's meaning.
- Risk: a "lie" filing about a named researcher is a claim about a person, with the same exposure the requirements already flag for public forgery marks (OD-11).

**Option C — TLUF's expansion is restated publicly as "truth, falsehood, unknown, fiction" (or the acronym is presented unexpanded, as a name).**
- The machinery, the name, and the copy all say the same thing; "falsehood" keeps the four-beat rhythm without the intent claim.
- Cost: it edits your expansion and breaks the literal match with Directive line 3 ("Truth, Lies, Uncertainty, and Fiction") — and note the Directive also says *Uncertainty* where the bin says *Unknown*, so the acronym has always been a compression of the line, not a transcription of the bins. That precedent cuts both ways and is yours to weigh.

**DECIDED — Will, 2026-11-14 21:52 CST: "we'll track both malicious and naive failures."**

The ruling closes the seam not by renaming either word but by tracking a **failure kind** on every False filing:

- A claim binned False on stated grounds also carries a recorded kind: **malicious** — the claim fails and intent to deceive is part of the record — or **naive** — an honest failure (a wrong shape, a broken step, an over-claimed nuance).
- The bin stays **False** on its grounds either way. The kind is tracked alongside the filing — it is never a fifth bin, and never a gate on binning: no False waits on an intent finding.
- **Malicious is recorded only where the stated grounds carry intent**; in every other case the kind is naive.
- So the acronym keeps **"lies"** and the bin keeps **"False"**, and the two words are reconciled by subset, not by synonym: **lies are the malicious subset of False**, named as such when the grounds carry intent.

What happens to the three options above, which stand as the record of how this was decided: Option A's standing explanation is no longer needed — there is no fine print, because the kind field says in the record itself what "lies" means operationally. Option B's intent standard is not adopted as a binning gate (the False gate stays meetable on grounds alone), but its warning — that a lie is a claim about a person — is honoured by the rule that malicious is recorded only on stated grounds carrying intent. Option C's restatement is not needed: the standings are enumerated True / False / Unknown / Fiction, TLUF's expansion stays Will's words, and the compression the acronym always was is now a compression with a key.

The same ruling is recorded where the machinery lives: the failure-kind amendment after A-2 in `REQUIREMENTS.md`, and the filing rule in the rd-tracker skill. This section is decided; the rest of this draft still awaits Will's review.

---

*End of draft. Prepared for Will's review; on his stamp, the adopted copy moves into the service's surfaces and this file's status line changes. The Lies/False question (§7) was ruled by Will on 2026-11-14 and is recorded as decided there; the tagline choice (§3) is the decision that still rides with him.*
