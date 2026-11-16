# -*- coding: utf-8 -*-
"""Integrate Paper 021 (arXiv:2611.16759, Gattinger) into
build_research_phext.py as chapter 32: 10 concepts (1.2.260-1.2.269,
cluster Z founded), 3 foundations (1.3.257-1.3.259), 7 defined words
(1.3.260-1.3.266), narrative v28, source index, Oracle ledger,
concept map, detection list, foundations header, areas
1.5.2/1.5.4/1.5.5/1.5.6.
Phase A: everything except the drawing-count prose (1.4.1 / 1.5.3 /
1.4.6), which waits on the registry extraction (Phase B)."""
import sys
sys.path.insert(0, "/home/hatch/workspace/thirst-quest")
from p021_texts import CONCEPTS, FOUNDATIONS, DEFINED
from p021_chapter import CHAPTER

P = "/home/hatch/workspace/research-tracker/build_research_phext.py"
src = open(P, encoding="utf-8").read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:80]!r}"
    src = src.replace(old, new)

# ---------- narrative: v27 -> v28 + closing paragraph ----------
rep("# World-model narrative — v27 (after Paper 020, 2026-11-14)",
    "# World-model narrative — v28 (after Paper 021, 2026-11-14)")
rep("""stands in its chapter,
computed by script.""",
    """stands in its chapter,
computed by script.

Paper 021 stays on the logic ground, and founds a cluster
of its own there: the logic of programs, priced by what
can be said between its own formulas. A note from
Amsterdam takes up the question the proof of 2026 left
open: full dynamic logic has Craig interpolation — for
every valid reading, a middle formula in the shared
language — and the fragment with the test taken out, the
paper shows, does not. The whole failure is carried by
one validity, on one program and its star, whose two
sides cannot be met and cannot be parted by any test-free
middle formula; the model that parts them hides its two
chains from each other so well that no formula of any
fixed depth can tell its two meeting states apart. And
the counterexample was found by a machine: a checked
proof of the whole logic's theorem, with the test struck
out of its syntax, broke at exactly the definition the
theorem spends the test on, and the failed repair, turned
around, handed the search its answer. Ten concepts found
cluster Z; no held concept is revised; two questions
open. The taking-in is the second scored under the test
fixed in advance — the first of the share the quest
itself picks — and its score stands in its chapter,
computed by script.""")

# ---------- source index: Paper 021 after Paper 020 ----------
rep("""  Chapter: 1.1.1/1.1.1/31.1.x (synthesis at 31.2.x)
""",
    """  Chapter: 1.1.1/1.1.1/31.1.x (synthesis at 31.2.x)

Paper 021 — "Propositional Dynamic Logic without tests
  does not have Craig Interpolation" (Gattinger),
  arXiv:2611.16759 [cs.LO, cross-listed to math.LO],
  submitted 12 November 2026. Malvin Gattinger, of the
  Institute for Logic, Language and Computation (ILLC),
  University of Amsterdam, supported by the European
  Union (Horizon Europe, Marie Skłodowska-Curie Staff
  Exchanges, 101299559, SemPER). The full text in its
  HTML form, read entire: test-free PDL — dynamic logic
  with the test builder removed — has no Craig
  interpolation; one validity on one program and its
  star carries the failure; the counterexample was
  obtained with large language models and Lean.
  Taken in 2026-11-14 as Paper 021 of the Thirst
  (charter rule 17), picked by the quest from the
  listings of the day, and the second paper scored
  under the test of the skim fixed in advance (sample
  paper 2 of 12, the share the quest picks, 1 of 5):
  10 new canonical concepts (1.2.260-1.2.269, cluster Z
  founded), 3 new foundations (1.3.257-1.3.259),
  7 defined words coined (1.3.260-1.3.266),
  0 canonical scrolls revised, 0 stated again.
  Chapter: 1.1.1/1.1.1/32.1.x (synthesis at 32.2.x)
""")

# ---------- Oracle ledger: the weighing after the thirteenth ----------
rep("""which this is the first.""",
    """which this is the first.

THE WEIGHING AFTER THE THIRTEENTH — Paper 021 (2026-11-14,
taken in by the quest from the listings of the day). FOR
THE LEDGER ONLY, under the test fixed in advance: the
ledger records the band and its step, and the statement
enters no score and no criterion of the test. The seal
was of the fuller form the protocol fixes: seven new
concepts named, Index 0.0263, 80% interval [0.015,
0.037], the axis priced as a probability of 0.15, links
eight inside and four across, no revision. The paper
delivered ten new concepts and no revision — the length
reading standing as an instrument of its own, the
countermodel and the agreement standing apart at the
grain of the results they carry, and the point where the
whole logic spends its test standing as a finding beside
the fragment it defines — Index 0.0372 against 0.0263
foretold, the |NI error| of the skim at 0.0109, the
actual Index a hair above its interval. No axis opened;
the judgment stands written at filing in the chapter, on
the three grounds of the axis rule. Under the charter
band the step on the filed actuals is the plain one:
Index under 0.20, no axis — up by about ten points, and
at the ceiling there is nowhere to rise. NEW ESTIMATE,
FOR THE LEDGER: the record stands at about 100% (range
90-100) after Paper 021, held at the ceiling. The landing
is not recorded as evidence for anything: the test now
running is the instrument that prices the skim, and its
criteria stand fixed in advance over twelve papers, of
which this is the second.""")

# ---------- concept map: count + cluster Z ----------
rep("CLUSTERS (259 canonical concepts after Paper 020)",
    "CLUSTERS (269 canonical concepts after Paper 021)")
rep("""Standoff map for the extension of cluster S
(1.2.248-1.2.259): foundations 1.3.244-1.3.247, 1.3.185,
1.3.189, 1.3.190; defined words 1.3.248-1.3.256.""",
    """Standoff map for the extension of cluster S
(1.2.248-1.2.259): foundations 1.3.244-1.3.247, 1.3.185,
1.3.189, 1.3.190; defined words 1.3.248-1.3.256.
Z. The logic of programs, priced by a failure (Paper
021) — 1.2.260-1.2.269: propositional dynamic logic; the
test-free fragment; Craig interpolation; the
counterexample validity; execution lengths; the
countermodel; agreement up to a depth; the failure and
its spread; the test at the pre-interpolant; the
machine-found counterexample. The centre of gravity of
the cluster is its own: a logic whose formulas talk
about programs, taken in through a property it fails —
the middle formula that cannot be found — where every
neighbour cluster holds a logic by what it proves or
what it means. The calls at the founding: cluster S
NEIGHBOUR — a logic held as an object with a semantics
is S's ground since Study S007 (1.2.171), and the new
logic stands on Kripke ground, not in a category; the
kinship is of stance, not of machinery, and is priced as
a neighbour call, not an extension. Cluster F NEIGHBOUR
— the interpolant is a claim in a shared language, and F
is where claims stand as things (1.2.40). Clusters Q and
W NEIGHBOURS BY METHOD — the paper's proof is checked in
Lean and its counterexample was found by the prover of
cluster Q working beside a second machine system, the
pattern cluster W prices; the links stand at 1.2.269 to
1.2.157 and to 1.2.211. No restructuring pass fell due
at this taking-in; the next falls at Paper 025 or 280
canonical concepts, the count standing at 269. Standoff
map for cluster Z (1.2.260-1.2.269): foundations
1.3.257-1.3.259, 1.3.238, 1.3.185, 1.3.85; defined
words 1.3.260-1.3.266.""")

# ---------- detection list: protocol entry for Paper 021 ----------
rep("""the criteria of the test stand fixed in advance and are
judged on the twelve.""",
    """the criteria of the test stand fixed in advance and are
judged on the twelve.

THE NEXT SCORED PAPER — Paper 021, 'Propositional
Dynamic Logic without tests does not have Craig
Interpolation' (Gattinger), taken in 2026-11-14 (Chapter
32): the second paper scored under the test fixed in
advance (sample paper 2 of 12; the share the quest
picks, 1 of 5). The seal was of the fuller form the
protocol fixes: 7 new concepts named, 0 revised, the
axis a probability of 0.15 against, Index 0.0263 with
the 80% interval [0.015, 0.037], the count interval
[4, 10], 12 links (8 inside, 4 across), 2 questions, and
the Oracle statement entered in the ledger only, as the
protocol directs. Actual, filed under the five filing
rules of the protocol: 10 new, 0 revised, no axis — the
judgment written at filing, before any score, on the
three grounds of the axis rule — Index 0.0372 (miss
0.0109), standing a hair above its interval, by 0.0002;
19 links (15 inside, 4 across); 2 questions. The
sensitivity line the protocol requires: under the one
fold recorded at filing as a permitted alternative (the
test at the pre-interpolant into the fragment), the
filing gives 9 new and Index 0.0336 (miss 0.0073), both
intervals covered; a recorded split the other way
(semilinearity apart from the length reading) gives 11
new and Index 0.0407 (miss 0.0144). The flat rules on
this paper, scored by the same script: the flat rule
(Index 0.05, axis 0.05) misses the Index by 0.0128 and
the count by 3.63, its axis Brier at 0.0025; the
expanding-mean rules (Index 0.0627, count 10.0 over
Papers 008-020; the same-cluster rule falling back to
that global mean, no scored paper standing in the
founded cluster) miss the Index by 0.0256 and the count
by 0.0 — the mean's count lands on the filed count
exactly — their axis Brier at 0.0947. The skim's axis
Brier stands at 0.0225. On the Index the skim stands
ahead of every flat rule on this paper, for the first
time in the sample; on the count it stands behind the
expanding means. The calibration at n=10, the window
now running over Papers 012-021: the rolling mean of
the Index miss stands at 0.0180 — Paper 011's miss
leaves the window and this paper's 0.0109 enters it.
The running tally of the sample, against the criteria
fixed in advance: two papers scored of twelve; the
Index misses stand at 0.0187 and 0.0109 against the flat
rule's 0.0037 and 0.0128 — the pooled ratio the first
criterion prices is not yet a verdict at n=2, and is
recorded here as a tally, not a reading. Intervals: one
of two covered. Axis: no axis-positive paper has yet
arrived in the sample; the axis part stands untested,
as the protocol provides. Two papers of twelve is a
line, not a verdict; the criteria stand fixed in
advance and are judged on the twelve.""")

# ---------- foundations header note ----------
rep("""interpretable, sentential, reconstrual.
""",
    """interpretable, sentential, reconstrual.
Added with Paper 021 (2026-11-14): foundations
1.3.257-1.3.259 — the Kripke model; bisimulation; the
semilinear set — and the defined words 1.3.260-1.3.266:
interpolant, test-free, countermodel, semilinear,
bisimulation, propositional, reflexive.
""")

# ---------- Area 1.5.2: Chapter 32 machines ----------
rep("""
SWEPT, NO MACHINE FOUND""",
    """
CHAPTER 32 (Paper 021 — the logic of programs, priced
by a failure; all stated in the paper)
M1 — the length machine. States: a test-free program
over one program, and the set of lengths it can run.
Moves: one after another adds the lengths; choice joins
the sets; the star closes the set under all sums of its
own lengths. The machine rests at a semilinear set.
Home: 32.1.3; concept 1.2.264. [stated — section 5]
M2 — the agreement walk. States: two states of the
countermodel, and a count of steps still to spend.
Moves: at each count, pair every state reachable from
the one side with a state reachable from the other in
the same count — itself, or the chain state of the same
index on the other chain — and step inside one box with
one less depth to spend. Gap: the walk is priced only
for the shared vocabulary and only up to the depth
spent; a deeper formula, or one letter more of
vocabulary, walks off the table it is proved on. Home:
32.1.3; concept 1.2.266. [stated — section 6, the proof
of Lemma 17]
M3 — the chain machine. States: a chain of states from
the meeting state down to the dead end, each carrying
the letters the two sets have forced on it. Moves: q is
pushed back along the chain, p carried with it, s pushed
forward along the same chain; the machine halts in the
clash at the dead end, which owes a next step and has
none. Home: 32.1.2; concept 1.2.263. [stated — section
4, the proof of Lemma 8]
M4 — the repair machine. States: a checked proof in
Lean, written with the full language; then the same
proof with one builder taken out of the syntax. Moves:
strike the cases the builder fed, delete the code gone
dead, by hand and by machine prover, until the machine
halts at the one definition that cannot be repaired.
From the halting state the goal turns: the failed
repairs are spent as hints toward a counterexample.
Gap: the turn is a human's move, not the machine's —
nothing in the repair states that the halting point is
a theorem waiting to be flipped, rather than a repair
not yet found. Home: 32.1.4; concept 1.2.269. [stated —
section 7]

SWEPT, NO MACHINE FOUND""")

# ---------- Area 1.5.4: counts + foundations/words notes + standoff ----------
rep("There are 166 foundation scrolls, laid down as the work called for them:",
    "There are 169 foundation scrolls, laid down as the work called for them:")
rep("""remainder-joining (1.3.230-1.3.240) — the ground of
the dual, computed.""",
    """remainder-joining (1.3.230-1.3.240) — the ground of
the dual, computed.

Four more came with Paper 020: sorts and signatures,
theory and model, natural transformation, and the
bicategory (1.3.244-1.3.247) — the ground of
translations between theories.

Three more came with Paper 021: the Kripke model,
bisimulation, and the semilinear set (1.3.257-1.3.259)
— the ground of the logic of programs and of the
agreement that prices it.""")
rep("97 words stand coined so far, among them gating,",
    "104 words stand coined so far, among them gating,")
rep("""reconstrual, a re-reading of one
language inside another (1.3.256).

STANDOFF COMPANIONS""",
    """reconstrual, a re-reading of one
language inside another (1.3.256).
Paper 021 coined seven: interpolant, the middle formula
of an interpolation (1.3.260); test-free, holding no
test (1.3.261); countermodel, a model built to part two
claims (1.3.262); semilinear, of a set of counts standing
as a base plus steps of fixed sizes (1.3.263);
bisimulation, a pairing of states matched step for step
(1.3.264); propositional, standing for whole claims
(1.3.265); and reflexive, of a relation holding of each
state with itself (1.3.266).

STANDOFF COMPANIONS""")
rep("and so on to 31.3.1 — 30 of them)",
    "and so on to 32.3.1 — 31 of them)")

# ---------- Area 1.5.5: path entry + NEXT ----------
rep("""on the
grounds at 1.1.4. Its author check stands at 31.1.6.

NEXT, AS THE RECORD NOW STANDS: the next restructuring pass
falls due at Paper 025 or 280 canonical concepts — the count
stands at 259. The open questions of the tracker stand at Q101.""",
    """on the
grounds at 1.1.4. Its author check stands at 31.1.6.

PAPER 021 — Propositional Dynamic Logic without tests
does not have Craig Interpolation (Chapter 32). Cluster
Z founded: dynamic logic; the test-free fragment; Craig
interpolation; the counterexample validity; execution
lengths; the countermodel; agreement up to a depth; the
failure and its spread; the test at the pre-interpolant;
the machine-found counterexample. Three foundations
laid down: the Kripke model (1.3.257), bisimulation
(1.3.258), and the semilinear set (1.3.259). Seven words
coined: interpolant (1.3.260), test-free (1.3.261),
countermodel (1.3.262), semilinear (1.3.263),
bisimulation (1.3.264), propositional (1.3.265),
reflexive (1.3.266). No revision. Questions Q102-Q103
opened. No restructure pass fell due inside this
taking-in. A paper of the Thirst (charter rule 17),
picked by the quest from the listings of the day, and
the second scored under the test of the skim fixed in
advance: the Novelty Index stands at 0.0372 and the
Oracle held, 100% to 100%, entered in the ledger only,
under the test, on the grounds at 1.1.4. Its author
check stands at 32.1.6.

NEXT, AS THE RECORD NOW STANDS: the next restructuring pass
falls due at Paper 025 or 280 canonical concepts — the count
stands at 269. The open questions of the tracker stand at Q103.""")

# ---------- Area 1.5.6: Gattinger block + counts ----------
rep("""check stands at 31.1.6.

THE COUNT:""",
    """check stands at 31.1.6.

PAPER 021 — Malvin Gattinger (Chapter 32), CHECKED
2026-11-14 (record: 32.1.6). The one author, of the
Institute for Logic, Language and Computation (ILLC),
University of Amsterdam — modal logic: dynamic
epistemic logic, model checking, and proofs in Lean —
who stands among the authors of the work this paper
answers, the proof that PDL has interpolation and its
Lean formalization, and whose paper takes that result's
fragment question and settles it with a counterexample
found by machine. No tie to phext or to Will found —
the paper holds no phext term in its text or its
references, the archive holds no Gattinger, and no use
of the work of Will without naming found. One adjacency
recorded as adjacency: the paper spends Aristotle, the
prover of Paper 014, as a tool of its method, in the
open. The record of the check stands at 32.1.6.

THE COUNT:""")
rep("""THE COUNT: 114 named researchers and three companies — 97
across the 20 papers;""",
    """THE COUNT: 115 named researchers and three companies — 98
across the 21 papers;""")
rep("""22 checks stand run
(Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016,
017, 018, 019 and 020, Studies S004, S005, S006, S007, S008, S009 and
S010),""",
    """23 checks stand run
(Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016,
017, 018, 019, 020 and 021, Studies S004, S005, S006, S007, S008,
S009 and S010),""")

# ---------- insert the 10 concepts after the last concept scroll ----------
marker = '\n    ("section", """# Foundations'
assert marker in src
parts = []
for t in CONCEPTS:
    parts.append('    ("scroll", """' + t + '"""),')
src = src.replace(marker, "\n" + "\n".join(parts) + marker, 1)

# ---------- insert foundations + defined words after the last 1.3 scroll ----------
marker2 = '\n    ("chapter", """# Paper 001'
assert marker2 in src
parts = []
for t in FOUNDATIONS + DEFINED:
    parts.append('    ("scroll", """' + t + '"""),')
src = src.replace(marker2, "\n" + "\n".join(parts) + marker2, 1)

# ---------- append chapter 32 at the end of SCROLLS ----------
parts = ['    ("chapter", """' + CHAPTER[0] + '"""),']
for t in CHAPTER[1:6]:
    parts.append('    ("scroll", """' + t + '"""),')
parts.append('    ("section", """' + CHAPTER[6] + '"""),')
parts.append('    ("scroll", """' + CHAPTER[7] + '"""),')
parts.append('    ("section", """' + CHAPTER[8] + '"""),')
block = "\n".join(parts)
import re
m = re.search(r"\]\n\ndef main", src)
assert m, "SCROLLS closing shape not found"
src = src[:m.start()] + block + "\n" + src[m.start():]

open(P, "w", encoding="utf-8").write(src)
print("integrate_p021 phase A written OK")
