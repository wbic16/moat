# -*- coding: utf-8 -*-
"""Paper 021 (arXiv:2611.16759, Gattinger) — canonical texts:
10 concepts (1.2.260-1.2.269, cluster Z founded),
3 foundations (1.3.257-1.3.259), defined words (1.3.260-)."""

CONCEPTS = [
"""# Propositional dynamic logic — a logic whose formulas talk about programs

Propositional dynamic logic (PDL), from Fischer and Ladner
(1979), is a modal logic that reasons about the running of
programs. Its language is built in two halves that define
each other. The formulas say what holds at a state: the
false, a letter, the not and the and of formulas, and, for
any program, the box form that says the words after the
program hold at every state the program can reach. The
programs are built from the single-step programs, the test
of a formula — the step that stays in place where the
formula holds and fails where it does not — choice between
two programs, one program after another, and the star: a
program run any number of times, zero times counted. The
diamond form, that some run of the program reaches a state
where the words after it hold, is defined from the box and
the not. Read on a Kripke model (1.3.257): each single-step
program is a relation between states, a test is the
relation that holds a state fixed where its formula is
true, choice is the joining of two relations, one after
another is the chaining of two relations, and the star is
the reflexive transitive closure of a relation — the steps
of the program, closed under standing still and under
chaining. A formula is valid when it holds at every state
of every model. The logic can say things like: if we keep
running the step while a letter holds, then whenever the
loop ends, another letter holds. What the logic is priced
by, in this paper, is a property of the logic as a whole —
interpolation (1.2.262) — and the price turns on one of its
program builders, the test (1.2.261, 1.2.268).
Source: Paper 021, sections 1 and 3. NEW in Paper 021.""",

"""# Test-free PDL — the fragment with the test taken out

The test-free fragment of PDL (1.2.260) is what stands
when the test builder is removed from the programs: no
step of any program may ask whether a formula holds. A
formula or a program is called test-free when it holds no
test at all. The fragment is not a toy: it was already
known to be weaker than the whole logic in what it can
say — Berman and Paterson (1981) showed the whole logic
says more, and their witness is a formula that runs a
while loop: keep running the step while a letter holds,
then run it once more under a test of the letter. The
paper of this chapter prices the fragment on a second
axis: not what it can say, but what can be said between
two of its own formulas. Full PDL has Craig interpolation
(1.2.262); whether the test-free fragment has it stood
open, and the direction of the one known bridge made the
question sharp — interpolation for the fragment would
have given interpolation for the whole (Kracht, 1999), so
the whole logic having it settled nothing about the
fragment. The answer of this paper is no (1.2.267), and
the no is carried by one validity (1.2.263). The fragment
is used apart from the whole logic at every step of the
paper — its programs are read by their lengths (1.2.264),
its formulas by their depth (1.2.266) — and it is filed
apart under the split rule for that reason.
Source: Paper 021, sections 1, 2 and 3. NEW in Paper 021.""",

"""# Craig interpolation — a property of a logic, priced by a shared language

A logic has Craig interpolation when every valid reading
from one formula to another can be passed through a
middle formula that speaks only in the shared language.
In the paper's own terms: for formulas such that the
first reading to the second is valid, an interpolant is a
formula whose stock of letters and single-step programs —
its vocabulary — stands inside the shared part of the
vocabulary of the two, and such that the reading from the first to
the middle and from the middle to the second are both
valid. The property is a property of the logic, not of
any one reading: a logic has it when an interpolant
stands ready for every valid reading. It can fail in two
ways — the middle formula may need words one side does
not share, or, as here, the only middle formulas may need
builders the fragment does not have (1.2.268). The
property is old and widely priced: temporal logics with a
next step do not have it (Maksimova, 1991); some fragments
of the linear-time temporal logic do (Gheerbrant and ten
Cate, 2009); the common-knowledge logics lose it by way
of losing the Beth property (Studer, 2009). Full PDL
(1.2.260) gained it only in 2026, by a proof built on
tableau (Borzechowski and five others); this paper takes
it away from the test-free fragment (1.2.261) with one
counterexample (1.2.263). It shares its word with the
interpolation the tracker already holds as a foundation
(1.3.238) — the recovery of a whole form from its values
at points — and the two are kept apart: that one builds a
form from points, this one asks what may stand between
two formulas.
Source: Paper 021, sections 1, 2 and 3. NEW in Paper 021.""",

"""# The counterexample validity — two sets of formulas that cannot be met, and with nothing between them

The load-bearing object of the paper: two finite sets of
test-free formulas, built on the letters p, q, s and the
one single-step program a, whose shared vocabulary is
exactly {a, p}. The first set says: s holds; and at every
state the star of a can reach, if p and s hold together,
then a has a next step and s holds after every a-step.
The second set says: at every reached state, q reads to
p; at every reached state, a next step to a q-state makes
the state itself a q-state; and some run of the star
reaches a state where q holds and a has no next step.
The two sets cannot be met at one state: from the reached
end state, q is pushed back along the chain to the start,
p comes with it, and s is then pushed forward along the
same chain until the end state must both have a next step
and have none. So the reading from the first set to the
denial of the second is valid — and the proof system of
the full logic even hands back an interpolant for it, a
long formula that keeps p under the star of a test of p
followed by a. That interpolant spends a test. The claim
of the paper is that every interpolant for this validity
must: no test-free formula in the shared vocabulary {a, p}
can stand between the two sets (1.2.266, 1.2.267). One
validity, on one program and its star, carries the whole
failure of a fragment (1.2.267) — and it was found by a
machine before it was proved by a hand (1.2.269).
Source: Paper 021, section 4. NEW in Paper 021.""",

"""# Execution lengths — a program read by the lengths it can run

In the single-program fragment — test-free programs over
the one program a — a program can be read by the set of
lengths it can run: the set of counts n such that running
the program can be done in exactly n steps of a. The set
is built as the program is built: the program a has the
set {1}; one program after another adds the lengths of
the two; choice joins the two sets; the star takes all
sums of lengths the program inside it can run, the empty
sum counted. This set of lengths is the Parikh image of
the program read as a word over a one-letter alphabet,
and by Parikh's theorem it is always a semilinear set
(1.3.259) — a finite joining of sets of the form of a base
plus steps of fixed sizes. In the Lean work under the
paper this is proved head-on, by induction on the
program, from the facts the library holds about semilinear
sets; the theorem about languages is not spent. The
reading back is almost exact: the sets that arise are
exactly the non-empty semilinear sets with one bar — a
set that holds zero must hold every multiple of some
period, since zero can only enter through a star. The two
gaps (the empty set, and {0} alone, can never arise, for
every test-free program can run at least one step) close
if a skip program — the step that stands still, the test
of the true in the whole logic, a builder of its own in
the fragment — is added. The length reading is the
instrument the main proof runs on: by it, a box formula
over a single-program test-free program says exactly that
its words hold at every state reachable in a number of
a-steps that stands in the length set (the paper's two
lemmas of section 5), and the agreement proof of 1.2.266
is walked in counts of steps.
Source: Paper 021, section 5. NEW in Paper 021.""",

"""# The countermodel — one model that holds the two sets at two states

The model the no-interpolant proof stands on, built for
the pair of sets of 1.2.263. Its letters are p, q, s and
its one program is a. Its states are two hubs, m and u,
and two endless chains running down to dead ends, the
v-chain and the w-chain. The program a runs: from m to m
and to u; from u to m, to u, and down into every w-state;
from each chain state of index above zero, one step down
its own chain and one step to u. The letters stand: p at
m and at every state of both chains; q at the v-chain
alone; s at the two hubs alone. In this one model the two
sets of the counterexample part company: m meets the
first set — it is the only state the star can reach from
m where p and s stand together, and it has a next step
whose every landing holds s — while every v-state meets
the second set: q reads to p everywhere, a step to a
q-state only starts at q-states, and the chain down to
the dead end v0 is the run the last formula asks for. A
model that satisfies each side of a validity somewhere is
no news; the work of this one is in what its two chains
hide from the shared vocabulary (1.2.266): from inside
either chain, the other chain cannot be told apart, and
the hub m looks, to any test-free formula of bounded
depth, exactly like a v-state far enough down its chain.
Source: Paper 021, section 6. NEW in Paper 021.""",

"""# Agreement up to a depth — two states no shallow formula can part

The engine of the no-interpolant proof. The modal depth
of a test-free formula counts its box forms, and nothing
else: letters and the false stand at depth zero, the not
and the and keep the depth of their parts, and a box adds
one. The count is shallow by design — it does not care
about the build of the programs inside the boxes. Two
states agree on a stock of letters and programs up to a
depth when every test-free formula in that stock, of
depth at most the count, holds at the one exactly when it
holds at the other. The paper's key lemma: in the
countermodel (1.2.265), the hub m and the chain state v_j
agree on the shared stock {a, p} up to depth j — for every
j. The proof walks in counts of steps: by the length
reading (1.2.264), a box formula at m and at v_j ranges
over the states reachable in the same counts of a-steps,
and row by row of the table of reach those states can be
paired — each with itself, or a v-state with the w-state
of the same index, which agree on all {a, p}-formulas by a
bisimulation (1.3.258) between the two chains — so that
paired states agree on the words inside the box, whose
depth is one less. This is what an interpolant would have
to break and cannot: a test-free interpolant of depth j
in the shared vocabulary would have to hold at m, where
the first set of 1.2.263 is met, and fail at v_j, where
the second is met — and the two states agree on it.
Source: Paper 021, sections 3 and 6. NEW in Paper 021.""",

"""# The failure, and its spread — no interpolation without tests

The paper's theorem: test-free PDL does not have Craig
interpolation (Theorem 19 of the paper), proved by the
one validity of 1.2.263 and the agreement of 1.2.266. The
failure spreads wider than the fragment it is stated for,
and the paper names the spread itself. The counterexample
spends only one single-step program and its star — no
choice, no composition — so any fragment of PDL that
holds at least one single-step program and its star, but
no tests, fails interpolation in the same way: it does
not matter whether choice and composition stand in the
language or not. Said in the older language, the basic
modal logic with the two forms [a] and [a*] — modal logic
K with the reflexive transitive closure added — does not
have interpolation; the paper's abstract notes this was
shown before, by Studer (2009), by the road of common
knowledge. The overlap is real and the difference is
named by the paper itself: the common-knowledge operator
cannot count steps, and a logic of programs can — the
program that runs a twice, starred, counts parity. So the
new proof is not the old result read again: it prices the
star itself, in a logic whose programs can count, and it
draws the line of the failure at the test, the one
builder the fragment lacks (1.2.268).
Source: Paper 021, section 6. NEW in Paper 021.""",

"""# The test at the pre-interpolant — where the whole logic spends its question mark

The one place the proof of interpolation for the whole
logic spends the builder the fragment lacks. The tableau
proof for PDL (Borzechowski and five others, 2026) builds
interpolants (1.2.262) in two stages: first a
pre-interpolant, then the solving of a fixed-point
equation that turns pre-interpolants into interpolants —
and the solving can only be carried out inside the logic
when the pre-interpolants stand in a fixed normal form.
The definition of the pre-interpolant (Definition 9.18 of
that work) writes an or — not-this or that — as a
box over a test: the step that tests the first words and
then asks the second. That is the whole use, and it is
load-bearing: when the author of this paper removed the
test from the syntax of the Lean formalization of that
proof, the code could be repaired almost everywhere —
cases struck out, dead code deleted — and the one place
it could not be repaired was this definition. The failure
of interpolation for the fragment (1.2.267) is, at the
level of the proof, exactly this: the normal form the
fixed-point step needs is bought with a test, and no
other builder in the fragment pays for it. Filed apart
from the fragment itself (1.2.261) under the grain rule:
it is the load-bearing object of the paper's account of
why, and the point its method story turns on (1.2.269).
Source: Paper 021, section 7. NEW in Paper 021.""",

"""# The machine-found counterexample — a failed repair, turned around

How the counterexample of 1.2.263 was found, in September
2026, with Lean and two systems of the kind the tracker
calls large language models. The work began inside the
Lean formalization of the proof that PDL has
interpolation: the author took the test out of the syntax
and repaired the code that broke, part by hand and part
with Aristotle — the prover of Paper 014 (1.2.157). The
repair halted at the pre-interpolant (1.2.268). Both
Aristotle and a second system, Claude Fable, were then
asked for other grammars of pre-interpolants; that led
nowhere. The turn: the second system was asked to spend
the failed proof ideas on the opposite goal — to find a
counterexample instead. It did so within a few minutes,
with a Lean formalization of the result. The example in
the paper is the author's own simplification of the first
one found — fewer letters, a model with less in it — with the
main idea the same. Every word of the paper's text is the
human author's; the build of the proof and the statements of
its lemmas stand strongly shaped by the Lean proof the
machine wrote, and its two figures were drawn from code
the machine wrote for them. All prompts and the summaries
of the machine answers are published, at a public archive
the paper names, and the Lean formalization stands at the
author's page. The method is filed as a concept because
the paper states it as part of its result: a theorem
about a logic, found by removing a builder from a checked
proof until the proof broke at exactly the builder the
theorem is about.
Source: Paper 021, section 7. NEW in Paper 021.""",
]

FOUNDATIONS = [
"""# Foundation: Kripke model — states, steps, and what holds where

A Kripke model gives a logic of states and steps its
ground. It holds: a set of states; for each single-step
program, a relation between states — the pairs where one
step of that program runs from the first state to the
second; and a reading that says, for each letter, at
which states the letter holds. A state together with its
model is a pointed model. What a formula says is then
read off the ground: a letter holds at a state when the
reading puts it there; a box form over a program holds at
a state when its words hold at every state the program's
relation reaches from it. Every richer program reads off
the same ground — a test holds a state in place, a choice
joins two relations, one program after another chains
them, and a star closes a relation under standing still
and under chaining. Builds on: set, relation, and the
everyday words state and step, which stand as they are.
""",

"""# Foundation: bisimulation — states matched step for step

A bisimulation between two states of a model (1.3.257),
for a stock of letters and programs, is a pairing of
states that never lets the two sides part. The pairing
must hold the two states themselves; paired states must
agree on every letter of the stock; and every step of a
program of the stock from one side must be matched by a
step of the same program from the other side to a state
paired with the landing — and the same back again. Two
states paired by such a matching agree on every formula
of the stock: no formula can price them apart, since each
of its steps can be shadowed on the other side. A
bisimulation is the strong form of agreement; the weaker,
bounded form — agreement up to a count of steps of depth —
is priced at 1.2.266. Builds on: the Kripke model
(1.3.257) and the everyday words pair and match.
""",

"""# Foundation: semilinear set — a base, and steps of fixed sizes

A semilinear set is a set of counts of the kind that
arises when a process may repeat its steps: a finite
joining of sets, each of the form of a base count plus
any number of steps of each of a few fixed sizes — the
base, and then the first size as many times as one likes,
the second size as many times as one likes, and so on.
The set of even counts is one: base zero, one step of
size two. The set of all counts from some point on is
one: a base, and a step of size one. By Parikh's theorem,
the count of each letter in the words of a language of
the context-free kind always lands in such a set; in the
single-letter case the set of lengths of a program
(1.2.264) is of this kind. Builds on: count, sum, and the
everyday words base and step.
""",
]

DEFINED = [
"""Defined word: interpolant (also: interpolants) — the
middle formula of Craig interpolation (1.2.262): a
formula in the shared vocabulary of two formulas, such
that the first reads to it and it reads to the second,
both readings valid. First spent at Paper 021
(Chapter 32).
""",

"""Defined word: test-free (also: the test-free fragment) —
of a formula or a program of dynamic logic (1.2.260):
holding no test at all; and, of the logic itself, the
fragment that stands when the test builder is taken out
(1.2.261). First spent at Paper 021 (Chapter 32).
""",

"""Defined word: countermodel (also: countermodels) — a
model built to part two claims: a ground (1.3.257) where
the one claim is met at one state and the other at
another, so that a reading said to hold between them, or
a middle term said to stand between them, is shown not
to stand. The countermodel of this tracker at 1.2.265 is
the one of Paper 021. First spent at Paper 021
(Chapter 32).
""",

"""Defined word: semilinear (also: semilinearity) — of a
set of counts: standing as a finite joining of sets of a
base plus steps of fixed sizes (1.3.259). First spent at
Paper 021 (Chapter 32).
""",

"""Defined word: bisimulation (also: bisimulations) — a
pairing of states of a model, matched step for step in
both directions, whose paired states agree on the letters
cared about (1.3.258). First spent at Paper 021
(Chapter 32).
""",

"""Defined word: propositional (also: propositionally) — of
a logic or a letter: standing for whole claims that hold
or fail at a state, as the letters of dynamic logic
(1.2.260) do, against the names of things. First spent at
Paper 021 (Chapter 32).
""",

"""Defined word: reflexive (also: reflexivity) — of a
relation between states: holding of each state with
itself, so that standing still counts as a run of length
zero; a relation closed under standing still and under
chaining is its reflexive transitive closure, the reading
of the star in dynamic logic (1.2.260). First spent at
Paper 021 (Chapter 32).
""",
]
