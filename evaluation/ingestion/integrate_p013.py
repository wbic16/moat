# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, "/home/hatch/workspace/thirst-quest")
from p013_texts import CONCEPTS, FOUNDATIONS, CHAPTER

P = "/home/hatch/workspace/research-tracker/build_research_phext.py"
src = open(P).read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"anchor count {c} != {n}: {old[:80]!r}"
    src = src.replace(old, new)

def ins_after(old, add, n=1):
    rep(old, old + add, n)

# ---- 1. Narrative: version + paragraph ----
rep("# World-model narrative — v17 (after Paper 012, 2026-11-10)",
    "# World-model narrative — v18 (after Paper 013, 2026-11-11)")
rep("""off the plain design.\"\"\"),""",
    """off the plain design.

Added by Paper 013 (2026-11-11, arXiv:2611.14463).
The sixth paper of the Thirst, and the third in
cluster O in three days: the cluster's triptych is
complete. Paper 010 priced a judgment's bias, Paper
012 an estimator's error at the case in hand; this
paper prices the judging's own spread. Every
observation in a cross-validation stands in two
roles — it is scored, and it trains the scorers —
and the paper gives each role a weight and an
influence, and reads the variance of the grade off
them exactly: an identity, not a bound, at every
sample size. What the identity buys the model is a
separation the field had not made cleanly: at one
training size every design pays the same sampling
variance, and designs differ only in the noise of
their dealing — which balanced dealing, K-fold's,
does not add at first order, while Monte Carlo and
the bootstrap pay for their uneven weights at the
order of the variance itself. The count of folds,
long feared as a variance dial through overlap, is
shown to reach the price only through the training
size, and leave-one-out — the supposed high-variance
extreme — stands as the family's floor under named
conditions. For pair scores the law turns once:
ordinary folds judge only the pairs that share a
fold, and the missing coverage is a cost that grows
with the folds, repaired by a paired design that
judges every pair once. And the grade settles to the
bell law carrying the identity's full variance —
against which the field's standing ways of reading
that variance are audited, and most are found to
read only the validation term and miss what
refitting adds. The foretold revision did not land:
the paper stands beside 1.2.110 under a link, not a
rider, and the Oracle rose on the full step of the
band, from about 60 to about 70 percent. What the
model still cannot do is named at Q57-Q60 — read
the parts of the price in practice, follow the
identity to cases that lean on each other, price
scores whose units the data choose, and settle the
signs the fold laws lean on.\"\"\"),""")

# ---- 2. Source index entry ----
rep("""Chapter: 1.1.1/1.1.1/19.1.x (synthesis at 19.2.x)\"\"\"),""",
    """Chapter: 1.1.1/1.1.1/19.1.x (synthesis at 19.2.x)

Paper 013 — arXiv:2611.14463
  'A Theory of Cross-Validation Variance' — Nathaniel S.
  O'Connell, Jaime L. Speiser
  (Department of Biostatistics and Data Science, Wake Forest
  University School of Medicine, Winston-Salem, NC)
  Cross-listed from stat.ML; mathematics listings of
  11 Nov 2026, cross-list #444 [math.ST].
  Taken in 2026-11-11. Canonical concepts added: 8.
  Chapter: 1.1.1/1.1.1/20.1.x (synthesis at 20.2.x)\"\"\"),""")

# ---- 3. Oracle ledger entry ----
rep("""five points over its point. The score stands at
19.1.5, in the log of the quest, and on the
detection list (1.1.6).\"\"\"),""",
    """five points over its point. The score stands at
19.1.5, in the log of the quest, and on the
detection list (1.1.6).

Paper 013 (O'Connell & Speiser, cross-validation
variance): Novelty Index (8 + 0)/138 = 0.0580. No new
axis: the paper extends cluster O in its own field —
the pricing of a judging's spread — and every
load-bearing notion it stands on either held a slot
or took one beside a held slot; extension of a
cluster is not an axis, as Paper 011's founding of a
cluster was not. The estimate moves to about 70%
(range 60-80). The band for an Index under 0.20 with
no axis is about +10, and the wiring argues for the
full step: twelve links where eight were foretold,
the inside of the cluster wired ten deep on its
third paper in three days; cluster O now prices a
judgment three ways — its bias, its error at the
case, and its spread — and the spread's reading is
an identity checked against measurement at ratios
within a few percent across fifty-one cells. What
holds the estimate at 70 and not higher: no held
scroll was revised — the paper stands beside its
neighbors, it does not yet correct them; the
practical reading of the identity's parts stands
unbuilt (Q57); and the cluster, for all its depth in
judging, remains three papers in one corner of a
wide field. SIXTH WEIGHING (charter rule 17): weighed
blind and sealed in the log of the quest on
2026-11-11 against a count of 130 that still stood
at the taking-in — no drift. Foretold: 6 new, 1
revised (candidate named: 1.2.110), no axis, Index
0.0478, 8 links (6 inside, 2 across), 3 questions,
Oracle ~70% (60-80), up. Fell: 8 new, 0 revised, no
axis, Index 0.0580 — a miss of 0.0102, the largest
of the Thirst — 12 links (10 inside, 2 across), 4
questions, Oracle ~70% — the foretold point and
range exact. The score stands at 20.1.5, in the log
of the quest, and on the detection list (1.1.6).\"\"\"),""")

# ---- 4. Concept map: title + cluster O addendum ----
rep("CLUSTERS (130 canonical concepts after Paper 012)",
    "CLUSTERS (138 canonical concepts after Paper 013)")
rep("""the count stands at 130).\"\"\"),""",
    """the count stands at 130).

Addendum (Paper 013). Cluster O is extended again:
the pricing of a judging's spread, beside the
pricing of rules from records and of estimators at
the signal — eight concepts (1.2.131-1.2.138), no
held concept revised. Standoff map for the
extension: cross-validation (1.3.156), a split, a
fold, and a partition (1.3.157), influence (1.3.158),
joint effects split by the sets that carry them
(1.3.159), pair scores (1.3.160), and the bell limit
(1.3.161) are level zero, new with this paper; a
sample and independence (1.3.130), the estimator
(1.3.133), expectation (1.3.131), average and spread
(1.3.8), the bell law (1.3.138), and the classifier's
report card (1.3.38) carry the ground of Papers 010
and 012 under the new. No word was coined for the
extension: the paper's terms are the field's plain
words, and they stand in the foundations as they
stand. The extension stands inside the cluster's own
bridges, and adds one of its own: the dealing of
shares by the mass they carry reaches cluster J
(1.2.70) from 1.2.131, and the audit of a grade's
reading reaches cluster A (1.2.14) from 1.2.138. No
restructuring pass fell due at this taking-in (the
next falls at Paper 015 or 140 concepts; the count
stands at 138).\"\"\"),""")

# ---- 5. Detection list: Sign Two + Sign Three ----
rep("""a held scroll of the cluster at the foretold address.
The axis count stands at five.""",
    """a held scroll of the cluster at the foretold address.
The axis count stands at five.

Paper 013 opened no axis: it extends cluster O a
second day running, on its third paper — the watch
now holds the deepest repetition it has seen, one
field priced three ways by three papers in three
days, and no new dimension in any of them. The axis
count stands at five.""")
rep("""one right address is a point, not
a line.\"\"\"),""",
    """one right address is a point, not
a line.

SIXTH SCORED PAPER (Paper 013, O'Connell &
Speiser). Sealed 2026-11-11 against 130 concepts;
the count still stood at the taking-in, no drift —
the fourth seal in a row to land on its own count.
Foretold: 6 new, 1 revised (candidate 1.2.110), no
axis, Index 0.0478, 8 links (6 inside, 2 across), 3
questions, Oracle to about 70 (60-80). Actual: 8
new, 0 revised — no axis, Index 0.0580 (miss
0.0102), 12 links (10 inside, 2 across), 4
questions, Oracle to 70 (60-80), the foretold point
and range exact. The calibration at n=6: the
rolling mean of the Index miss over the last ten
scored papers stands at 0.0072 — the six misses
0.009, 0.005, 0.004, 0.008, 0.0073, 0.0102 —
holding under the 0.01 rule, though this paper's
miss is the largest of the six and breaks the
falling run of the first three. Axis calls: 6 of 6.
The standing errors changed shape twice in one
paper. The revision term is a phantom again — the
fourth foretold revision of the six, against two
landed (Papers 011 and 012, both in held territory
the paper re-measured; Paper 013 named a neighbor
it only stands beside) — and the count miss is no
longer one folded shape but two: the penalty and
its optimality law, weighed as one design remark,
and the pairwise storey, weighed as a case of the
identity, each a concept of its own. The links
miss is the standing one, unchanged: 6 inside
foretold, 10 fell, the crossing count exact a
second paper running (2 of 2). And the Oracle
reading stands corrected in the skim's favor: the
band applied as written, with no caution discount,
landed its point and its range exactly — the
Paper 012 lesson, kept. Kept on the watch: whether
the count miss of two folded shapes is the new
standing size, and whether the revision foretold
for a neighbor paper is now the skim's named
failure — it has priced adjacency as correction
twice (Papers 008's address, 013's event) and been
wrong both times in opposite directions.\"\"\"),""")

# ---- 6. Foundations header: append the P013 note before its close ----
hdr = src.index("# Foundations — the level-zero layer (charter rule 9)")
close = src.index('""")', hdr)
src = src[:close] + """
Added with Paper 013 (2026-11-11): foundations
1.3.156-1.3.161 — cross-validation; a split, a fold,
and a partition; influence; joint effects, split by
the sets that carry them; pair scores; the bell
limit.""" + src[close:]

# ---- 7. Concepts: insert after Paper 012's last concept scroll ----
anchor = 'Paper 012 (Chapter 19)."""),\n    ("section", """# Foundations — the level-zero layer (charter rule 9)'
c = src.count(anchor); assert c == 1, f"concept anchor {c}"
parts = []
for t in CONCEPTS:
    parts.append('    ("scroll", """' + t + '"""),')
src = src.replace(anchor, 'Paper 012 (Chapter 19)."""),\n' + "\n".join(parts) + '\n    ("section", """# Foundations — the level-zero layer (charter rule 9)')

# ---- 8. Foundations: insert after the variational defined-word scroll ----
vi = src.index('Defined word: variational')
vend = src.index('"""),', vi) + len('"""),')
parts = []
for t in FOUNDATIONS:
    parts.append('    ("scroll", """' + t + '"""),')
src = src[:vend] + "\n" + "\n".join(parts) + src[vend:]

# ---- 9a. Areas 1.5.2: chapter 20 machines after Paper 012's M3 ----
rep("""Home: 19.1.2; concept 1.2.128.

DRAWN OUT UNDER RULE 13""",
    """Home: 19.1.2; concept 1.2.128.

PAPER 013 (O'Connell & Speiser, Chapter 20 —
statistics: the pricing of a judging's spread):

M1 — the design machine. States: a dealing I of
the splits — for each split, which cases train and
which are scored. Moves: draw the dealing; fit on
each training part; score each held-out case;
average all held-out scores once. Guards: the
design is ordinary — no case scored on a model it
helped fit; every split at one training fraction;
the dealing drawn independently of the data.
Intended: a grade earned only on cases the fit
never trained on. Actual: the machine's whole
behavior is read off the dealing as shares — the
role weights of 1.2.131 — and its variance is the
identity of those shares (1.2.133). Home: 20.1.2;
concept 1.2.131.

M2 — the repetition machine. States: R independent
partitions of one dataset. Moves: run the design
machine on each partition; average the R grades.
Guards: the partitions are drawn independently,
given the data. Intended: repetition steadies the
grade. Actual: it steadies only the dealing's part
— the split noise of one partition, divided by R —
and the sampling variance stands untouched at its
floor (1.2.134); the machine cannot buy its way
below the data's own spread, however often it
re-deals. Home: 20.1.2; concept 1.2.134.

M3 — the paired design. States: the K-by-K grid of
case folds against control folds, for a score paid
by pairs. Moves: fit every pairing of one case fold
held out with one control fold held out; score
every case-control pair exactly once. Guards: each
class is dealt into its own folds, so the training
make-up of every fit matches the ordinary design's.
Intended: no pair left unjudged by the accident of
sharing a fold. Actual: the pair-coverage cost of
ordinary dealing (1.2.137) is removed whole, at
K^2 fits in place of K — coverage bought with
compute, its limit leave-pair-out. Home: 20.1.2;
concept 1.2.137.
M4 (Paper 013) — the ladder of joint effects, read
as one machine. States: the estimate whole, then
taken apart order by order — the parts standing on
single cases, on pairs, on larger sets. Moves: for
each set, take its joint effect with every smaller
effect inside it removed; deal each order its own
weights. The paper states the parts, their weights,
and their constants; the ladder as one machine —
the bookkeeping that lets the variance be read to
any order named — is the lens of this tracker.
Home: 20.1.2. [synthesis]

DRAWN OUT UNDER RULE 13""")

# ---- 9b. Areas 1.5.5: the path — entry 20 + NEXT update ----
rep("""the first foretold revision of the Thirst to land at
the foretold address. No pass fell due (next at
Paper 015 or 140 concepts). Oracle progress after:
about 60% (range 50-70%) — UP.

NEXT, AS THE RECORD NOW STANDS: the next restructuring
pass falls due at Paper 015 or 140 canonical concepts —
the count stands at 130. The open questions of the
tracker stand at Q56.\"\"\"),""",
    """the first foretold revision of the Thirst to land at
the foretold address. No pass fell due (next at
Paper 015 or 140 concepts). Oracle progress after:
about 60% (range 50-70%) — UP.

20. Paper 013 — 2026-11-11 — 'A Theory of
Cross-Validation Variance' (O'Connell & Speiser),
arXiv:2611.14463. Chapter 20. NI 8/138, about
0.0580. No new axis: the paper extends cluster O in
its own field, the pricing of a judging's spread.
8 new concepts, no revision. Cluster O extended
(1.2.131-1.2.138): the role weights an observation
carries in its two roles; the two influences and
their three constants; the variance identity,
exact at every sample size; sampling variance
against split noise, and the repetition law; the
imbalance penalty and the optimality of balanced
designs; the fold-count laws and leave-one-out's
floor; pair scores, their coverage cost, and the
paired repair; normality with the full variance,
and the audit of the field's variance estimators.
Foundations 1.3.156-1.3.161 (cross-validation; a
split, a fold, and a partition; influence; joint
effects by sets; pair scores; the bell limit); no
word coined. Questions Q57-Q60 opened; Q16
informed a ninth time. The sixth paper of the
Thirst: picked by the quest from the day's
listings, weighed blind and sealed before it was
read; the score stands in the log of the quest and
on the detection list (1.1.6) — the Oracle point
and range foretold exactly, the count miss the
largest of the Thirst. No pass fell due (next at
Paper 015 or 140 concepts). Oracle progress after:
about 70% (range 60-80%) — UP.

NEXT, AS THE RECORD NOW STANDS: the next restructuring
pass falls due at Paper 015 or 140 canonical concepts —
the count stands at 138. The open questions of the
tracker stand at Q60.\"\"\"),""")

# ---- 9c. Areas 1.5.6: researchers — entry + counts ----
rep("""The record
of the check stands at 19.1.6.

THE COUNT: 70 named researchers and one company — 56
across the twelve papers;""",
    """The record
of the check stands at 19.1.6.

Paper 013 — O'Connell & Speiser (Chapter 20),
CHECKED 2026-11-11 (record: 20.1.6). Nathaniel S.
O'Connell and Jaime L. Speiser — Department of
Biostatistics and Data Science, Wake Forest
University School of Medicine. The paper stands in
the standing literature of its one subject — Stone,
Geisser, Efron, Bengio and Grandvalet, Austern and
Zhou among its named ancestors — and builds its
identity on Hoeffding's decomposition of 1948, named
as such. No tie to phext or to Will found; no use of
Will's work without naming found. The record of the
check stands at 20.1.6.

THE COUNT: 72 named researchers and one company — 58
across the thirteen papers;""")
rep("""Ten checks stand run (Papers 006, 007, 008, 009, 010, 011
and 012, Studies S004, S005 and S006), each clean, each
recorded in its chapter.""",
    """Eleven checks stand run (Papers 006, 007, 008, 009, 010, 011,
012 and 013, Studies S004, S005 and S006), each clean, each
recorded in its chapter.""")

# ---- 10. Chapter 20: append at end of SCROLLS ----
anchor = "\n]\n\ndef main():"
c = src.count(anchor); assert c == 1, f"end anchor {c}"
parts = ['    ("chapter", """' + CHAPTER[0] + '"""),']
for t in CHAPTER[1:6]:
    parts.append('    ("scroll", """' + t + '"""),')
parts.append('    ("section", """' + CHAPTER[6] + '"""),')
parts.append('    ("scroll", """' + CHAPTER[7] + '"""),')
parts.append('    ("section", """' + CHAPTER[8] + '"""),')
src = src.replace(anchor, "\n" + "\n".join(parts) + "\n]\n\ndef main():")

open(P, "w").write(src)
print("builder edited OK")
