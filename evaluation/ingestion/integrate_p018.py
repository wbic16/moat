# -*- coding: utf-8 -*-
"""Integrate Paper 018 (arXiv:2611.17082, Baraud) into
build_research_phext.py as chapter 29: 7 concepts (1.2.230-1.2.236),
5 foundations (1.3.222-1.3.226), 3 defined words (1.3.227-1.3.229),
narrative v25, source index, Oracle ledger, concept map, detection
list repair + update, foundations header, areas 1.5.2/1.5.4/1.5.5/1.5.6.
Phase A: everything except the drawing-count prose (1.4.1 / 1.5.3 /
1.4.6), which waits on the registry extraction (Phase B)."""
import sys
sys.path.insert(0, "/home/hatch/workspace/thirst-quest")
from p018_texts import CONCEPTS, FOUNDATIONS, DEFINED
from p018_chapter import CHAPTER

P = "/home/hatch/workspace/research-tracker/build_research_phext.py"
src = open(P, encoding="utf-8").read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:80]!r}"
    src = src.replace(old, new)

# ---------- narrative: v24 -> v25 + closing paragraph ----------
rep("# World-model narrative — v24 (after Paper 017, 2026-11-13)",
    "# World-model narrative — v25 (after Paper 018, 2026-11-13)")
rep("""and a bet in tokens standing open between them.""",
    """and a bet in tokens standing open between them.

Paper 018 returns to the isotonic estimator of Paper 012
and asks what its price becomes when the noise is allowed
to change its spread from point to point, and to grow
tails too heavy to square. The answer comes as a
coincidence: on the monotone class the least squares fit
is the sign-test estimator of Baraud and Maillard, and so
carries that estimator's price — twice the approximation
error, plus the average absolute moment times a power of
the degree over the count of points — under noise the old
pricing never admitted. The same paper takes the
protection away: on the one-peak class a single loud
point breaks least squares outright, while the sign-test
estimator stands at the parametric rate; and on a line an
exact computation shows the winner between the two is
decided by where the noise sits against where the shape
stands large. Seven concepts join cluster O; no held
concept is revised; three questions open.""")

# ---------- source index: Paper 018 after Study S010 ----------
rep("""  Chapter: 1.1.1/1.1.1/28.1.x (synthesis at 28.2.x)
""",
    """  Chapter: 1.1.1/1.1.1/28.1.x (synthesis at 28.2.x)

Paper 018 — "Isotonic least squares is robust to
  heteroscedasticity, unimodal least squares is not"
  (Baraud), arXiv:2611.17082 [math.ST], posted to the
  listings of Friday 13 November 2026. Yannick Baraud,
  of the University of Luxembourg. The full text in its
  HTML form, read entire: the least squares estimator
  over the monotone class is the l_1-estimator of
  Baraud and Maillard, and so is priced under noise of
  uneven spread and heavy tails; on the one-peak class
  the two estimators part, and least squares fails.
  Taken in 2026-11-13 as Paper 018 of the Thirst
  (charter rule 17), picked by the quest from the
  listings of the day: 7 new canonical concepts
  (1.2.230-1.2.236), 5 new foundations (1.3.222-1.3.226),
  3 defined words coined (1.3.227-1.3.229),
  0 canonical scrolls revised, 0 stated again.
  Chapter: 1.1.1/1.1.1/29.1.x (synthesis at 29.2.x)
""")

# ---------- Oracle ledger: eleventh weighing ----------
rep("""grain the skim cannot price in advance at all.""",
    """grain the skim cannot price in advance at all.

THE ELEVENTH WEIGHING — Paper 018 (2026-11-13, taken in
by the quest from the listings of the day). The skim
foretold 6 new concepts and one revision, Index 0.0277,
no axis. The paper delivered 7 new concepts and no
revision — the foretold revision a phantom, a second
price standing beside the window price of 1.2.129 rather
than over it — Index 0.0297 against 0.0277 foretold, the
|NI error| of the skim at 0.0020. No axis opened; the
strand of axis calls stands eleven for eleven. Under
the charter band the step is the plain one: Index under
0.20, no axis — up by about ten points. NEW ESTIMATE:
the record stands at about 90% (range 80-100) after
Paper 018.""")

# ---------- concept map: count + Cluster O addendum ----------
rep("CLUSTERS (229 canonical concepts after Study S010)",
    "CLUSTERS (236 canonical concepts after Paper 018)")
rep("""Addendum (Paper 014). A new cluster is founded:""",
    """Addendum (Paper 018). Cluster O is extended a third
time: the pricing of how an estimator stands up to hard
noise — seven concepts (1.2.230-1.2.236), no held
concept revised. The test that prices a candidate, and
the l_1-estimator it defines; extremal elements and
their degree; the average-moment price; the coincidence
on the monotone class; the sign step; the loud point;
weighted hearing on a line. Standoff map for the
extension: spread that changes from place to place
(1.3.222), a heavy tail (1.3.223), the sign of a number
(1.3.224), one peak (1.3.225), and cutting power
(1.3.226) are level zero, new with this paper; the
sequence model (1.3.145), projection onto a convex set
(1.3.146), the monotone cone (1.3.151), the estimator
and consistency (1.3.133), the bell law (1.3.138), and
the slope-bounded law (1.3.149) carry the ground under
the new. Three words were coined for the extension:
heteroscedastic (1.3.227), unimodal (1.3.228), and
extremal (1.3.229). The extension stands on ground the
cluster already holds — the estimator of Paper 012 —
and draws two bridges out: to the measurement agenda
of cluster A, where hearing is a measurement choice,
and to the test-built specification of cluster I.

Addendum (Paper 014). A new cluster is founded:""")

# ---------- detection list: Sign Two repair (016/017) + 018; Sign Three TENTH + ELEVENTH ----------
rep("""though analogies, were four in number and named at the
seal. The axis count stands at six.""",
    """though analogies, were four in number and named at the
seal. The axis count stands at six.

Paper 016 opened the seventh axis: geometrical gravity —
a field the model held nothing of, arriving as one paper
with three readings of one theory. Its bridges to held
work are the shared stage of mechanics and the affine
frame, not shared machinery, so the landing is nearer the
distant shape; the count of axes stands at seven.

Paper 017 opened no axis: it founded a cluster (W, the
verified artifact) in ground the proving vein and the
studies had dug — a founding is not by itself an axis,
and no new kind of quantity entered the book. The axis
count stands at seven.

Paper 018 opened no axis: a quest paper from the listings
of the day, in home ground of the tracker — an estimator
the model already priced, priced again for the noise it
actually meets. The axis count stands at seven.""")
rep("""abstract shows the concepts, not the debts) or two.""",
    """abstract shows the concepts, not the debts) or two.

TENTH SCORED PAPER — Paper 017, 'AlphaProof Code'
(Google DeepMind document 36), taken in 2026-11-13
(Chapter 27). The skim read the title and the opening
abstract of the document alone. Foretold: 11 new, 1
revised, no axis, Index 0.0532, 17 links, 3 questions,
Oracle to about 80 (70-90), up. Actual: 17 new, 1
revised — the revision at the very address foretold,
1.2.48, the rider of the second pole — no axis, Index
0.0788 (miss 0.0256), 41 links (36 inside, 5 across), 4
questions, Oracle to 80 (70-90) — the foretold point
and range exact a fifth paper running. The calibration
at n=10: the rolling mean of the Index miss stands at
0.0166 — the ten misses 0.0092, 0.0046, 0.0043, 0.0077,
0.0073, 0.0102, 0.0749, 0.0224, 0.0000, 0.0256. Axis
calls: 10 of 10. The miss is the count call again, in a
new shape: the skim priced a document of practice by
the papers it had met, and a framework whose concepts
stand inside a proved system carries more concepts
than its abstract lists — the testing of a
specification, the amendment protocol, the
concretization bound, the collision clause, priced
reductions, the joint judging of a key used twice each
stood alone where the skim had folded them into
neighbours. The revision term landed whole for the
first time since Paper 012: one priced, one fallen, at
the foretold address.

ELEVENTH SCORED PAPER — Paper 018, 'Isotonic least
squares is robust to heteroscedasticity, unimodal
least squares is not' (Baraud), taken in 2026-11-13
(Chapter 29). The skim read the title and the abstract
alone. Foretold: 6 new, 1 revised, no axis, Index
0.0277, 11 links (9 inside, 2 across), 3 questions,
Oracle to about 90 (80-100), up. Actual: 7 new, 0
revised, no axis, Index 0.0297 (miss 0.0020), 15 links
(13 inside, 2 across), 3 questions, Oracle to 90
(80-100) — the foretold point and range exact a sixth
paper running. The calibration at n=10, the window now
running over Papers 009-018: the rolling mean of the
Index miss stands at 0.0159 — Paper 008's 0.0092 leaves
the window and this paper's 0.0020 enters it. Axis
calls: 11 of 11. The revision term is where the miss
lives this time, and its shape is the fifth phantom: a
parallel pricing read as a re-pricing — the paper
prices the l_1-risk of the isotonic estimator by degree
and average moment, beside the held l_2-price by local
variation (1.2.129), and the skim had counted 'same
estimator, new noise' as a re-measuring of the held
scroll. The count call ran one the other way: the sign
step, the one condition the coincidence hangs on, stood
as a concept of its own (1.2.234) where the skim had
priced it inside the theorem it serves. The links miss
kept its standing shape — inside under-read (9 foretold,
13 fallen), across exact (2 and 2): the bridges out of
the cluster priced to the count, the weave inside it
under-priced again.""")

# ---------- foundations header note ----------
rep("""1.3.167-1.3.172: autoformalization,
counterexample, derangement, subgraph,
contamination, divisor.""",
    """1.3.167-1.3.172: autoformalization,
counterexample, derangement, subgraph,
contamination, divisor.
Added with Paper 018 (2026-11-13): foundations
1.3.222-1.3.226 — spread that changes from place to
place; a heavy tail; the sign of a number; one peak;
cutting power — and the defined words 1.3.227-1.3.229:
heteroscedastic, unimodal, extremal.""")

# ---------- Area 1.5.2: Chapter 29 machines ----------
rep("""
SWEPT, NO MACHINE FOUND""",
    """
CHAPTER 29 (Paper 018 — the isotonic estimator under
noise of uneven spread; all stated in the paper but
Machine 3, which is drawn from its proof)
M1 — the test machine. States: a candidate held against
the data, and its running price — the largest charge any
rival lays on it through the sign test. Moves: each
rival charges the sum of the signed gaps at the points
where the two differ; the estimator is any state whose
charge stands within a small constant of the least. On
the monotone class the machine rests at the projection
of the readings, whose price is exactly zero. Home:
29.1.2; concepts 1.2.230, 1.2.233. [stated — section 2.1
and Theorem 2 of the paper]
M2 — the sign-step machine. States: a candidate, a
rival, and the stepped candidate found by moving
against the signs of their difference. Moves: shrink
the step until the stepped candidate stands inside the
class, or find that no positive step does; on the
monotone cone, half the smallest positive gap is always
safe. Where the machine halts inside for every pair,
the projection is the answer of the test. Home: 29.1.2;
concept 1.2.234. [stated — Assumption 1 and the proof of
Theorem 2]
M3 — the loud-point machine. States: a fit tracking the
plateau truth, or raised on the one loud reading. Moves:
the loud reading arrives; the peak may be raised on it
at a total square cost under a quarter of the design;
any fit near the truth pays more than that at the loud
point alone; on an event of chance at least 30 percent
the rule that squares comes to rest raised, and its
l_1-error never closes, while the sign machine never
moves. Home: 29.1.2; concept 1.2.235. [inferred — drawn
from the proof of Theorem 3]
M4 — the hearing machine. States: two running sums on a
line — the flat sum of the readings, and the sum
weighted by the shape. Moves: each reading enters the
flat sum at weight one and the weighted sum at the
value of the shape at its point; which estimator wins
is set by whether the noise stands where the shape
stands large. Home: 29.1.2; concept 1.2.236.
[stated — Proposition 1]

SWEPT, NO MACHINE FOUND""")

# ---------- Area 1.5.4: reference counts + new kits ----------
rep("There are 146 foundation scrolls, laid down as the work called for them:",
    "There are 151 foundation scrolls, laid down as the work called for them:")
rep("""One more came with Study S010: undefined behaviour (1.3.219) —
the ground of the agreed meaning.""",
    """One more came with Study S010: undefined behaviour (1.3.219) —
the ground of the agreed meaning.

Five more came with Paper 018: spread that changes from
place to place, a heavy tail, the sign of a number, one
peak, and cutting power (1.3.222-1.3.226) — the ground
of the pricing of an estimator under uneven noise.""")
rep("82 words stand coined so far, among them gating,",
    "85 words stand coined so far, among them gating,")
rep("""Study S010 coined two: elaboration, the carrying of a program
into a simpler core language under a semantics (1.3.220); and
autoverification, the verifying of software by agents under
shared semantic models and engineered specifications
(1.3.221).""",
    """Study S010 coined two: elaboration, the carrying of a program
into a simpler core language under a semantics (1.3.220); and
autoverification, the verifying of software by agents under
shared semantic models and engineered specifications
(1.3.221).

Paper 018 coined three: heteroscedastic, of noise whose
spread changes from place to place (1.3.227); unimodal,
rising then falling with one peak (1.3.228); and
extremal, of a candidate whose cut sets are poor enough
to be priced (1.3.229).""")
rep("and so on to 28.3.1 — 27 of them)",
    "and so on to 29.3.1 — 28 of them)")

# ---------- Area 1.5.5: path entry + NEXT ----------
rep("""author check stands at 28.1.3.

NEXT, AS THE RECORD NOW STANDS: the next restructuring pass
falls due at Paper 020 or 240 canonical concepts — the count
stands at 229. The open questions of the tracker stand at Q93.""",
    """author check stands at 28.1.3.

PAPER 018 — Isotonic least squares is robust to
heteroscedasticity (Chapter 29). Cluster O extended a
third time, at its own object: the test that prices a
candidate; extremal elements and their degree; the
average-moment price; the coincidence on the monotone
class; the sign step; the loud point; weighted hearing.
Five foundations laid down: spread that changes from
place to place (1.3.222), a heavy tail (1.3.223), the
sign of a number (1.3.224), one peak (1.3.225), and
cutting power (1.3.226). Three words coined:
heteroscedastic (1.3.227), unimodal (1.3.228), extremal
(1.3.229). No revision. Questions Q94-Q96 opened. No
restructure pass fell due inside this taking-in. A
paper of the Thirst (charter rule 17), picked by the
quest from the listings of the day: the Novelty Index
stands at 0.0297 and the Oracle moved, 80% to 90%, on
the grounds at 1.1.4. Its author check stands at 29.1.6.

NEXT, AS THE RECORD NOW STANDS: the next restructuring pass
falls due at Paper 020 or 240 canonical concepts — the count
stands at 236. The open questions of the tracker stand at Q96.""")

# ---------- Area 1.5.6: Baraud block + counts ----------
rep("""check stands at 28.1.3.

THE COUNT:""",
    """check stands at 28.1.3.

PAPER 018 — Yannick Baraud (Chapter 29), CHECKED
2026-11-13 (record: 29.1.6). The one author, of the
University of Luxembourg — mathematical statistics:
model selection, robust estimation — whose paper takes
the l_1-estimator of his joint work with Odalric-Ambrym
Maillard and proves the least squares estimator over the
monotone class is that estimator, priced under noise of
uneven spread and heavy tails. Maillard is not an entry:
he stands behind the taken-in machinery as its co-author
of 2026, cited at every load-bearing point of the paper,
and the check ran on the paper and its one author. No
tie to phext or to Will found — the paper holds no phext
term in its text or its references, the
archive holds no Baraud, and no use of the work of Will
without naming found. The record of the check stands at
29.1.6.

THE COUNT:""")
rep("""THE COUNT: 111 named researchers and three companies — 94
across the 17 papers;""",
    """THE COUNT: 112 named researchers and three companies — 95
across the 18 papers;""")
rep("""S002 and the long tail of Study S005. 19 checks stand run
(Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016
and 017, Studies S004, S005, S006, S007, S008, S009 and S010),""",
    """S002 and the long tail of Study S005. 20 checks stand run
(Papers 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016,
017 and 018, Studies S004, S005, S006, S007, S008, S009 and
S010),""")

# ---------- insert the 7 concepts after the last concept scroll ----------
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

# ---------- append chapter 29 at the end of SCROLLS ----------
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
print("integrate_p018 phase A written OK")
