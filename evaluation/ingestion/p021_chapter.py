# -*- coding: utf-8 -*-
"""Paper 021 — Chapter 32 scrolls, in builder order:
[0] 32.1.1 lead, [1] 32.1.2 formal core (the logic and the
property), [2] 32.1.3 formal core (lengths, the countermodel,
agreement), [3] 32.1.4 results map, [4] 32.1.5 delta,
[5] 32.1.6 author check, [6] 32.2.1 synthesis (section),
[7] 32.2.2 open questions, [8] 32.3.1 standoff (section)."""

CHAPTER = [
"""# Paper 021 — Propositional Dynamic Logic without tests does not have Craig Interpolation (Gattinger)

Source: arXiv:2611.16759 (cs.LO, cross-listed to
math.LO), version 1, submitted 12 November 2026. One
author: Malvin Gattinger, of the Institute for Logic,
Language and Computation (ILLC), University of
Amsterdam, supported by the European Union (Horizon
Europe, Marie Skłodowska-Curie Staff Exchanges, grant
agreement 101299559, SemPER). The paper states its own
making in its section 7: the result was obtained using
Lean and two large language models, and all text in the
paper was written by its human author. Read entire in
its HTML form, 2026-11-14.

THE THIRST. A paper of the Thirst (charter rule 17),
picked by the quest from the listings of the day — the
listings for Friday 13 November 2026, the current
listings on Saturday 14 November — as a cross-list of
the mathematics listings. It is the second scored paper
of the test of the skim fixed in advance and stamped by
Will (the protocol the quest keeps, 2026-11-14): sample
paper 2 of 12, of the share the quest itself picks (the
first of its five). It was weighed blind under seal
beforehand, in the fuller form the protocol fixes: seven
new concepts named, Index 0.0263 with an 80% interval
[0.015, 0.037], the count interval [4, 10], the axis
priced as a probability, 0.15, links eight inside and
four across, questions two, no revision. The reading
gave ten concepts in a cluster of their own; the score,
computed by script under the protocol, stands at 32.1.5.

THE DELTA. Ten concepts, founding cluster Z (1.2.260-
1.2.269): propositional dynamic logic (1.2.260); test-
free PDL (1.2.261); Craig interpolation (1.2.262); the
counterexample validity (1.2.263); execution lengths
(1.2.264); the countermodel (1.2.265); agreement up to a
depth (1.2.266); the failure and its spread (1.2.267);
the test at the pre-interpolant (1.2.268); and the
machine-found counterexample (1.2.269). Three
foundations (1.3.257-1.3.259): the Kripke model;
bisimulation; the semilinear set. Seven defined words
(1.3.260-1.3.266): interpolant, test-free, countermodel,
semilinear, bisimulation, propositional, reflexive. No
held concept revised; no held scroll stated again.
FOUR state machines drawn, all stated in the paper
(32.1.2, 32.1.3, 32.1.4; the area at 1.5.2). Two
questions opened, Q102-Q103 (32.2.2). The author check
stands at 32.1.6.
""",

"""# Paper 021 — the formal core: the logic, the property, and the pair with nothing between them

THE LOGIC (section 3 of the paper; concepts 1.2.260,
1.2.261). Formulas and programs define each other. A
formula is the false, a letter, a not, an and, or a box:
a program followed by a formula, saying the formula
holds at every state the program reaches. A program is a
single-step program, the test of a formula, a choice of
two programs, one program after another, or the star of
a program — run any number of times. A formula or
program is test-free when it holds no test. The
vocabulary of a formula or program is the set of its
letters and single-step programs. Meaning stands on a
Kripke model (1.3.257): states, one relation per
single-step program, a reading of the letters. A test is
the relation that holds a state fixed where the tested
formula holds; choice joins two relations; one after
another chains them; the star is the reflexive (1.3.266)
transitive closure. A formula is valid when it holds at
every state of every model.

THE PROPERTY (concept 1.2.262). An interpolant for a
valid reading from one formula to another is a formula
in the shared vocabulary, such that both halves of the
reading are valid through it. The modal depth of a
test-free formula counts only its boxes; two states
agree on a vocabulary up to a depth when no test-free
formula of that vocabulary and at most that depth parts
them (concept 1.2.266).

THE PAIR (section 4; concept 1.2.263). Two sets of
formulas over the letters p, q, s and the one program a,
with shared vocabulary {a, p}. The first: s; and under
the star, p and s together read to a next step existing
and s after every step. The second: under the star, q
reads to p; under the star, a step to a q-state makes a
state a q-state; and the star reaches a state where q
holds and no step leaves. The paper's Lemma 8: the two
sets cannot be met — from a state meeting both, the
reached dead end sends q back along its chain, p comes
with q, s runs forward along the same chain, and the
dead end must both have a next step and have none. So
the reading from the first set to the denial of the
second is valid. The same section names the shape of
the whole proof to come: build one model where the
first set is met at one state and the second at another
(1.2.265); take a test-free interpolant of some depth j;
show the two states agree on every test-free {a, p}-
formula of depth at most j (1.2.266); then the
interpolant must both hold and fail, and there is none.

STATE MACHINE OF THIS SCROLL. M3 — the chain machine.
States: a chain of states from the meeting state down
to the dead end, each carrying the letters the two sets
have forced on it. Moves: q is pushed back along the
chain from the dead end, p is carried with it, and then
s is pushed forward along the same chain from the start;
the machine halts in the clash at the dead end, which
owes a next step and has none. Home: this scroll;
concept 1.2.263. [stated — section 4, the proof of
Lemma 8]
""",

"""# Paper 021 — the formal core: lengths, the countermodel, and agreement

LENGTHS (section 5 of the paper; concept 1.2.264). For
a test-free program over the one program a, its set of
execution lengths: {1} for a itself; sums for one after
another; the joining for choice; all sums of its own
lengths, the empty sum counted, for the star. That set
is the Parikh image of the program over a one-letter
alphabet, and it is semilinear (1.3.259) — in the Lean
work proved by induction on the program, from the
facts the library holds about semilinear sets, and not by
spending the theorem about languages. The sets that
arise are exactly the non-empty semilinear sets that,
when they hold zero, hold every multiple of some period;
the empty set and {0} never arise, and both gaps close
if a skip step — standing still, the test of the true in
the whole logic — is added as a builder of its own. Two
lemmas then read the semantics through the lengths: a
program reaches from one state to another exactly when
some count in its length set does; and a box formula
holds at a state exactly when its words hold at every
state reachable in a count from its program's set.

THE COUNTERMODEL (section 6; concept 1.2.265). One
model, on the letters p, q, s and the program a: the
hubs m and u, and the two chains of v-states and
w-states, each chain running down to a dead end. The
hub m meets the first set of the pair; every v-state
meets the second (Lemma 15 of the paper, checked formula
by formula). The two chains agree on every {a, p}-
formula: the pairing that matches each w-state with the
v-state of the same index, and every state with itself,
is a bisimulation (1.3.258) for that vocabulary
(Lemma 16).

AGREEMENT (concept 1.2.266). The key lemma (Lemma 17):
for every j, the hub m and the chain state v_j agree on
all test-free {a, p}-formulas of modal depth at most j.
The proof pairs, count by count of steps, the states
reachable from the two sides: the same states, or a
v-state with the w-state of the same index, or a state
with itself — paired states agreeing on the words inside
one fewer box. From it, the end (Lemma 18 and Theorem
19): a test-free interpolant of depth j for the pair
would have to hold at m and fail at v_j, and the two
agree on it — so there is none, and test-free PDL does
not have Craig interpolation (1.2.267).

STATE MACHINES OF THIS SCROLL. M1 — the length machine.
States: a test-free program over one program, and the
set of lengths it can run. Moves: one after another adds
the lengths; choice joins the sets; the star closes the
set under all sums of its own lengths. The machine rests
at a semilinear set. Home: this scroll; concept
1.2.264. [stated — section 5]
M2 — the agreement walk. States: two states of the
countermodel, and a count of steps still to spend.
Moves: at each count, pair every state reachable from
the one side with a state reachable from the other side
in the same count — itself, or the chain state of the
same index on the other chain — and step inside one box,
with one less depth to spend. The walk never parts the
two states on any formula the depth can still pay for.
Home: this scroll; concept 1.2.266. [stated — section 6,
the proof of Lemma 17]
""",

"""# Paper 021 — the results map: what stands proved, and on what it rests

THE THEOREM. Test-free PDL does not have Craig
interpolation (1.2.267). It rests on: the pair of sets
and their joint clash (Lemma 8, section 4); the length
reading of single-program programs (section 5); the
countermodel and its two lemmas (Lemmas 15-17,
section 6); and the closing step that turns agreement
into the absence of an interpolant (Lemma 18). No
tableau and no proof system is spent in the paper's own
proof: the argument is semantic throughout, and the
proof system of the earlier work is named only where it
hands back the with-test interpolant for the same
validity — a long formula under the star of a test of p.

THE SPREAD. The counterexample spends one program and
its star, so the failure holds for every fragment with
at least one program and the star and no tests, with or
without choice and composition; and, in the older
language, for the basic modal logic with [a] and [a*] —
modal logic K with the reflexive transitive closure.
That corollary was shown by Studer (2009), by the road
of common knowledge and the Beth property; the paper
names both the overlap and the difference — common
knowledge cannot count steps, and programs here can,
down to parity.

THE GROUND IT STANDS ON. Full PDL has interpolation
(Borzechowski and five others, 2026 — the author among
them), by a tableau proof whose pre-interpolant spends
the test at exactly one definition (1.2.268). The
test-free fragment was already known weaker in what it
can say (Berman and Paterson, 1981). The bridge of
Kracht (1999) — interpolation for the fragment would
give it for the whole — is why the result for the whole logic
left the question of the fragment open, and the paper is
careful to state the direction. Around it: temporal
logics with a next step lose the property (Maksimova,
1991); some fragments of the linear-time temporal logic
keep it (Gheerbrant and ten Cate, 2009).

THE METHOD (section 7; concept 1.2.269). The result was
obtained in September 2026 with Lean and two large
language models. The prompts and the summaries of the
answers stand at a public archive the paper names (a
Zenodo record), and the Lean formalization at the
author's own page. The text of the paper is the human
author's; the build of the proof and the statements of
its lemmas stand strongly shaped by the machine's Lean
proof, and the two figures were drawn from machine-
written code. Caveats, in the paper's own terms: the
example printed is a simplification of the first one
found — fewer letters, a model with less in it — with the main
idea the same; and the second road to the exact reading
of the length sets, by adding the skip step, is stated
and not formalized.

STATE MACHINE OF THIS SCROLL. M4 — the repair machine.
States: a checked proof of a theorem, written with the
full language in Lean; then the same proof with one
builder taken out of the syntax. Moves: strike the cases
the builder fed, delete the code gone dead, by hand and
by machine prover, until the machine halts at the one
definition that cannot be repaired — the pre-interpolant
(1.2.268). From the halting state the goal itself turns:
the failed repairs are spent as hints toward a
counterexample, and its sibling among the machine systems finds
one, checked, within minutes. Home: this scroll;
concept 1.2.269. [stated — section 7]
""",

"""# Paper 021 — the delta: what this adds, and what was checked

TEN CONCEPTS (1.2.260-1.2.269), founding cluster Z — the
logic of programs, priced by what can be said between
its own formulas. THREE FOUNDATIONS (1.3.257-1.3.259):
the Kripke model; bisimulation; the semilinear set.
SEVEN DEFINED WORDS (1.3.260-1.3.266): interpolant,
test-free, countermodel, semilinear, bisimulation,
propositional, reflexive. LINKS: counted at 19 —
fifteen inside, among the ten new concepts (dynamic
logic to its fragment; interpolation to the logic it is
first priced on; the counterexample validity to the
fragment it is built in and to the property it breaks;
the length reading to the fragment and to the agreement
proof that walks in its counts; the countermodel to the
validity it was built for; agreement to the countermodel
and to the length reading; the spread of the failure to
the validity and to the fragment; the test at the
pre-interpolant to interpolation, whose middle terms it
builds, and to the fragment that lacks it; the
machine-found counterexample to the validity it found
and to the pre-interpolant where its search turned) and
four across clusters: the machine-found counterexample
to solved-means-kernel-complete (1.2.157) — its Lean
formalization is judged by the same kernel standard the
proving cluster holds; the machine-found counterexample
to the gatekeeper (1.2.211) — a machine's work admitted
by a check, in the cluster where a claim of a prover is
priced by comparison; dynamic logic to a logic read in a
category (1.2.171) — a logic held as an object with a
semantics, in the own ground of cluster S; and interpolation
to propositions as types (1.2.40) — the interpolant is a
formula, a claim in the shared language, and cluster F
is where claims stand as things. Inside is counted as:
among the ten new concepts — the founding cluster holds
no held concept to link to. REVISIONS: none. No held
scroll changed its words or its standing. TWIN-CHECK:
interpolation (1.2.262) against interpolation (1.3.238),
one word and two things — the recovery of a form from
its points against the middle formula between two
formulas — kept apart in the concept itself, and linked
there, not merged.

THE FILING, UNDER THE PROTOCOL. This paper is sample
paper 2 of 12 of the test fixed in advance (the share
the quest picks, 1 of 5), and its delta was filed under
the five filing rules of that test. The rules at work:
the split rule parts test-free PDL (1.2.261) from dynamic
logic (1.2.260) — the paper spends the fragment apart
from the whole at every point (its programs read by
lengths, its formulas by depth, its theorem about the
fragment alone); the instrument rule parts execution
lengths (1.2.264) — a named map the argument spends at
three distinct points (the reading of a program's reach,
the reading of a box formula, and the walk of the
agreement proof); the grain rule parts the countermodel
(1.2.265), agreement up to a depth (1.2.266), and the
test at the pre-interpolant (1.2.268) from their
neighbours — each is the load-bearing object of a result
or of the paper's account of why the result holds. One
fold a filing hand could argue stands recorded as the
permitted alternative, and the score is reported both
ways below: the test at the pre-interpolant (1.2.268)
folded into test-free PDL (1.2.261) — the builder whose
absence defines the fragment, read as a note on the
fragment rather than a finding of its own. Taken, the
fold gives nine concepts. A second alternative runs the
other way and is recorded, not folded: semilinearity
split out of execution lengths (1.2.264) gives eleven
concepts — the split was not taken, because the paper
spends the length set and its semilinearity as one
instrument, in one definition and one fact.

THE AXIS JUDGMENT, made in writing at filing, before any
score was computed. The axis rule asks three things.
(a) The centre of gravity of the paper is a property of
a fragment of a logic of programs: whether a middle
formula can always be found in a shared language. The
model holds logics as objects with semantics (cluster
S), claims and the kernels that check them (cluster F),
and the proving of theorems by machine (clusters Q and
W); a property of a logic, priced by a counterexample, is
a kind of quantity those clusters already trade in — the
tracker has priced logics by what they can say since
Study S007. Modal logic is new ground, and a cluster
founding is not by itself an axis (the Paper 011
precedent). (b) No held concept is re-read to receive
the paper: the ten new concepts are built from held
kinds — formula, program, model (1.3.257 is laid down
new because the ground itself was not yet a foundation,
which is the level-zero duty, not a re-reading), proof —
and every held scroll keeps its words and its standing
(revisions none). (c) The bridges to held ground are
shared machinery — Kripke semantics, the standard ground
of the modal family, and kernel-checked proof in Lean —
not analogies of shape; the one bridge priced as shape
in the seal, toward cluster S, is recorded as a neighbour
call in the map and carries no load in the filing.
JUDGMENT: no axis opens. The sealed probability stood at
0.15; the rest it priced — that a logic of programs,
priced by a property failure, be judged a new kind of
quantity — is answered by (a): the quantity is a property
of a logic, and properties of logics are held ground.

THE SCORE, computed by script (score_p021.py, kept with
the quest; no number here is computed by hand). The
Novelty Index, in the terms of the skim itself: ten new,
no revisions, over 259 + 10 standing concepts: 10/269 =
0.0372. The sealed prediction read seven new, Index
0.0263, 80% interval [0.015, 0.037]. |NI error| = 0.0109,
and the actual Index stands a hair above its interval —
0.0372 against a top of 0.037: not covered. The count:
signed error +3, absolute 3, the sealed interval [4, 10]
covered at its top. Revisions exact (0 foretold under
the revision rule, 0 taken). The axis: judged no in
writing at filing, on the three grounds above; the filed
actual agrees; Brier score of the sealed 0.15 against the
actual 0: 0.0225. Links: fifteen inside against eight
sealed (error +7 — the founding weave under-read again,
on new ground as on home ground), four across against
four sealed, exact. Questions exact: two foretold, two
opened (Q102-Q103), both of the foretold shapes. THE
SENSITIVITY LINE the protocol requires: under the
recorded fold (the test at the pre-interpolant into the
fragment), the filing gives nine new, Index 0.0336, |NI
error| 0.0073, and both intervals covered; under the
recorded split (semilinearity apart), eleven new, Index
0.0407, |NI error| 0.0144, neither interval covered. THE
FLAT RULES on the same paper, scored by the same script:
the flat rule (Index 0.05, axis 0.05) misses the Index by
0.0128 and the count by 3.63, and its axis Brier stands
at 0.0025; the expanding-mean rules — the mean of past
actuals over Papers 008-020, Index 0.0627 and count 10.0,
the second of them falling back to that same global mean
since no scored paper stands in the founded cluster —
miss the Index by 0.0256 and the count by 0.0 exactly,
and their axis Brier stands at 0.0947. On this paper the
skim stands ahead of every flat rule on the Index, level
with none on the count — the count of the expanding mean,
10.0, lands on the filed count exactly — and between the
flat rule and the expanding means on the axis. The
rolling mean of the Index miss over the last ten scored
papers stands at 0.0180 (the window now running over
Papers 012-021). THE LEDGER, entered in the ledger
only, under the test: the band step on the filed actuals
(Index under 0.20, no axis) is +10 at the ceiling, so the
ledger holds at 100 (90-100); the statement enters no
score and no criterion. The standing record: no held scroll moved;
the new drawing stands counted at 1.4.1. State machines:
four drawn in this chapter (M1-M4, all stated, none
inferred); the drawn total of the tracker stands at 98
(78 stated, 20 inferred).
""",

"""# Paper 021 — Provenance: author check (charter rule 15)

Twenty-third check of the register, run 2026-11-14 by
Emise. The one author: Malvin Gattinger, of the
Institute for Logic, Language and Computation (ILLC),
University of Amsterdam — a worker in modal logic whose
doctoral work (2018) was on model checking for dynamic
epistemic logic, and who stands among the authors of the
very work this paper answers: the proof that PDL has
Craig interpolation (Borzechowski and five others, 2026,
the paper's reference [4]) and of its Lean formalization
(reference [7]).

CHECKS RUN. (1) The paper read entire in its HTML form,
and its reference list read in full (14 entries):
no phext, no Bickford, no Exocortex, no Mirrorborn, and
no phext scroll or coordinate in the text or the list;
the word scroll never stands in the paper at all.
(2) The web searched for the author with phext: no tie
found — the pages the search returns are his institute
and publication pages, which show a modal-logic line
(dynamic epistemic logic, model checking, Lean) and,
among his works, a verified proof of Craig interpolation
for basic modal logic in Lean: his own road to this
paper, held in the open. (3) Will's archive of his own
posts searched for the author's name: no Gattinger
found.

VERDICT: no evidence found — stated as a finding, on the
checks above. No tie to phext in the sense of the
rule: the paper neither cites nor uses phext or the work
of Will. No prior art of Will's stands in the paper
without naming: its machinery is the tableau proof and
Lean formalization of its own authors' line. One
adjacency is recorded as adjacency, not a tie: the
paper spends, as a tool of its method, Aristotle — the
prover taken in at Paper 014 (cluster Q) — and names it
in its references and its section 7; and its author is a
co-author of the result this paper bounds. Both stand in
the open, in the paper itself.
""",

"""Paper 021 — synthesis: the builder that is the whole difference [synthesis]

Two papers in two days have now priced a logic by a
property, and they price opposite ends of one scale.
Paper 020 asked when two theories count as the same, and
found sameness an equivalence with a structure of its
own. This paper asks what can stand between two formulas
of one logic, and finds a place where nothing can: the
shared language is too poor, not in words, but in one
builder. The test is the smallest builder in PDL — a step
that goes nowhere and only asks a question — and the
whole difference between a logic that has interpolation and
its fragment that does not is that step. The tracker has
met this shape before, on the side of making: in cluster
I a specification is priced by what each of its pieces
removes, and a piece no test can see is a finding. Here
the shape stands on the side of saying: a builder no
formula can do without is priced by the property that
falls when it is taken out. [synthesis]

The second shape is the method, and it belongs to the
proving continent. The tracker holds machines that prove
(cluster Q), machines whose proofs pass a gate (cluster W),
and now a machine that found the counterexample a human
then simplified and proved in prose — found, what is
more, by breaking a checked proof at exactly the builder
the theorem is about, and turning the break into the
search. The prompts and the summaries of the machine's
answers are published with the paper, as part of its
record. Whether that trail is evidence or only
provenance — whether the standing of a machine-found
thing rests on the kernel's check alone, or also on the
road that found it — is now a question of the tracker
itself, and it stands open at Q103. [synthesis]
""",

"""# Paper 021 — Open questions Q102-Q103

Q102 — WHAT THE TEST BUYS, IN FULL. The paper prices one
place where the test is spent: the writing, at the pre-interpolant,
of an or as a box over a test, in the normal form
the fixed-point step needs (1.2.268). Is that the only
place? Which other properties of PDL stand or fall with
the test — and is there a fragment, weaker than the
whole and stronger than the test-free, where
interpolation returns, bought with less than the full
test? The paper's spread (1.2.267) draws the line for
every fragment under the test-free one; the ground
between the fragment and the whole stands unpriced.

Q103 — THE STANDING OF A MACHINE-FOUND FINDING. The
counterexample of this paper was found by a large
language model, with its Lean formalization, in minutes;
the human author simplified it and wrote the paper. The
prompts and the summaries of the machine's answers are
published. For the proving clusters of the tracker itself: does
the standing of such a finding rest on the kernel check
alone — the proof in Lean, judged as 1.2.157 judges —
with the trail as provenance only? Or does the trail
itself carry weight: that the search was a turned-around
repair, that the failed proofs are on record, that the
first example found was more tangled than the one
printed? The question belongs to the tracker itself, opened by
this paper and not answered by it.
""",

"""Standoff references — Paper 021 stands on these foundations

New with this paper: the Kripke model (1.3.257),
bisimulation (1.3.258), and the semilinear set
(1.3.259); and the defined words interpolant (1.3.260),
test-free (1.3.261), countermodel (1.3.262), semilinear
(1.3.263), bisimulation (1.3.264), propositional
(1.3.265), reflexive (1.3.266).
Held ground it also stands on: interpolation (1.3.238),
the foundation of cluster Y that shares its word, kept apart from
the property of logics at 1.2.262; the category
(1.3.185), the ground of the neighbour cluster S; and
the state machine (1.3.85), the sense in which the four
machines of this chapter are machines.
""",
]
