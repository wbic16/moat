# -*- coding: utf-8 -*-
# Paper 018 (arXiv:2611.17082, Baraud) — tracker texts.
# Concepts 1.2.230-1.2.236; foundations 1.3.222-1.3.226;
# defined words 1.3.227-1.3.229; chapter 29 (29.1.1-29.3.1).

CONCEPTS = [
"""# The test that prices a candidate — the l_1-estimator

An estimator built from tests taken two at a time. For two
candidates f and g in a class F, the paper's test
statistic reads the data Z through their difference:

T(Z, f, g) = the sum over the design points of
(f(x_i) - Y_i) times sign(f(x_i) - g(x_i)).

Each point casts one vote, and the vote is a sign,
never a size: a point where f stands above g charges
f the whole gap between f and the reading, with its
sign; a point where they
agree charges nothing. The price of a candidate is
the worst vote against it, T(Z, f) = the largest
T(Z, f, g) over all rivals g, and an l_1-estimator
is any candidate whose price stands within a small
constant c of the least price in the class — the set
E_c(Z, F) of the paper. When that set holds one
element it is called the l_1-estimator. The
construction is that of Baraud and Maillard (2026);
this paper takes it in and reads the least squares
estimator against it. What the test never does is
square a gap: the loud point of 1.2.235 can
shout in this court only once, with a sign. The
price of the estimator stands bounded at 1.2.232,
by way of
the degree of 1.2.231. Its kin in the model: the
specification built from tests in cluster I, where a
class is likewise known by the tests it can be put
to (1.2.58). Source: Paper 018, section 2.1,
building on Baraud and Maillard (2026). NEW in
Paper 018.""",
"""# Extremal elements and their degree

The candidates the price of 1.2.232 can reach are
the extremal (1.3.229) ones, and each carries a
degree. A candidate f-bar in F is extremal of degree
at most D when the two families of sets it cuts out
on the design points — the sets where rivals stand
above it, {f > f-bar}, and where they stand below
it, {f < f-bar} — are each poor in the sense of
cutting power (1.3.226): their VC-dimension stands
at most D. Every candidate is extremal with degree
at most n, the count of points; the useful ones
stand far below it. A member of a linear space of
dimension d is extremal of degree at most d + 1. A member of the monotone class constant on at most
d pieces is extremal of degree at most d + 1. A
candidate linear on at most d pieces, convex or
concave, stands at most 5 + 2d. The degree is the complexity the price
charges for: not the size of the class, but the
how rich the cuts are that one candidate lets the
class make around it. Source: Paper 018, section 2.2,
building on Baraud and Maillard (2026). NEW in
Paper 018.""",
"""# The average-moment price

The bound the l_1-estimator (1.2.230) carries,
proved by Baraud and Maillard (2026) and taken in
here as the paper's Theorem 1. For every extremal
(1.3.229) candidate f-bar of degree D in the class,
the expected l_1-risk of any estimator in E_c(Z, F)
stands at most

2 l_1(f*, f-bar) + kappa . sigma_n(p) (D/n)^(1 - 1/p)
+ c/n,

with the least value taken over p in [1, 2], kappa a
plain constant, and sigma_n(p) the AVERAGE over the
design points of the p-th absolute centred moment,
(1/n) the sum of E|Y_i - E Y_i|^p. Three things in
the bound do the work of the paper. First, no
square need stand: the errors need only a moment of
order p, as low as p = 1 — heavy tails (1.3.223)
are priced, not assumed away. Second, the noise
enters by its average, not by its worst point: a
single loud point moves the price by its share of
the average, where a price set by the maximum would
be set by that point alone — the bound is steady
under unequal spread (1.3.222) by its shape. Third,
the rate the bound gives is the rate of the field
itself: at
p = 2 with bounded degree, the parametric rate
1/sqrt(n); at p in (1, 2), the rate n^-(1 - 1/p),
which Devroye and his co-workers (2016) showed
no estimator beats in general, under a moment of
order p alone. Beside the price of the isotonic
estimator at 1.2.129 — local variation, read through
windows, under noise of one spread — this is a
second price for the same estimator, charged on
degree and average moment; the coincidence of
1.2.233 says the two prices price one object.
Source: Paper 018, section 2.3 (Theorem 1 of
Baraud and Maillard, 2026). NEW in Paper 018.""",
"""# The coincidence — on the monotone class the two estimators are one

The paper's main result (its Theorem 2). Let F be
the class of functions on an interval that never
fall, and let the least squares estimator over F
stand in — the projection of the seen list onto the
monotone cone (1.2.124, 1.3.151). Then that
estimator makes the test price of 1.2.230 least over
F, and its price is exactly zero: T(Z, f-tilde) = 0.
Any other candidate making the price least agrees
with it at every design point. So
on this class the two estimators are one estimator:
the fit built from squares is the fit the sign
tests choose, and the bound of 1.2.232 holds for the
least squares estimator itself, with c = 0. The
same holds on the class of functions that never
rise. What the coincidence
buys is the whole of Paper 012's isotonic ground
re-priced: the estimator whose sharp l_2-price is
the window sum of 1.2.129 now carries an l_1-price
under noise whose square need not average to
anything standing, and which need not share one
spread — because on monotone
ground it was the l_1-estimator all along. The
engine of the proof is the sign step of 1.2.234.
The coincidence is a property of the class, not of
the estimators: on the one-peak class it fails, at
1.2.235, and on a line it fails, at 1.2.236.
Source: Paper 018, section 3 (Theorem 2). NEW in
Paper 018.""",
"""# The sign step — the condition that makes the projection the answer

The one assumption the coincidence of 1.2.233 is
proved under, stated by the paper as its
Assumption 1 and worth a scroll of its own: a class
F meets it when, first, the set of its candidates'
vectors on the design points is closed and convex,
and second, for every two candidates f and g in F
some lambda > 0 has f - lambda . sign(f - g) still
in F — from any candidate, a small step in the
direction the signs name, against any rival, stays
inside the class. Under the assumption the proof is
three lines: the projection is known by
<Y - f-tilde, g - f-tilde> <= 0 for all g; putting
the stepped candidate in the place of g gives
T(Z, f-tilde, g) <= 0 for all g, which is the
coincidence. The work stands in checking the
assumption on the monotone cone. Where f rises
strictly, a step can break the rise only across a
gap, and lambda at half the smallest positive gap
keeps every step safe; where f stands flat, the
signs of two rising candidates can only help the
rise, and every lambda is safe. So the monotone
class meets the condition by the shape of its gaps.
The paper states the theorem for every class that
meets the condition; which of the other classes of
the field meet it stands open (Q94). Source:
Paper 018, section 3 (Assumption 1 and the proof
of Theorem 2). NEW in Paper 018.""",
"""# The loud point — the one-peak break

Where the coincidence dies. On the class of
unimodal (1.3.228) functions on [0, 1] — one peak,
its place free — the paper builds one example
(its Theorem 3). The truth is a plateau: f* = 1 on
[1/4, 1/2], 0 elsewhere. The noise is Gaussian and
silent at every design point but one: at
i_0 = the point nearest 3n/4 the spread stands at
sqrt(n), so that single reading Y_{i_0} swings on
the scale of sqrt(n). On an event whose chance
tends to the chance a standard bell draw clears
1/2 — at least 30 percent — that reading stands
huge. Now any one-peak candidate that stays near
f* in l_1 must keep its peak left of i_0, and so
must stand below 1/2 at i_0; its square error at
that one point then exceeds the whole square error
of a rival that jumps to the loud reading at i_0
and makes the stretch between the plateau and i_0
flat at a common level — a rival whose total stands
at most n/4 + 1. So least squares cannot be the
near one: its l_1-error stands at least (1 - 4/n)/8
on the event. Least squares is not consistent here. The
l_1-estimator stands untouched by the same reading:
f* is extremal in the class of degree at most 6 —
three constant pieces, two monotone parts — and
sigma_n(2) = 1, so the price of 1.2.232 gives its
expected l_1-risk at most kappa . sqrt(6)/sqrt(n)
+ c/n: the parametric rate. The mechanism is the
pair of the coincidence read backwards. Squaring
lets one point's error outweigh a quarter of the
design; a class whose peak may sit anywhere lets
the fit spend itself chasing that point. On the
monotone cone the chase is impossible — no second
peak can be raised — and the coincidence of
1.2.233 is the protection. Off the cone, the
protection is that the class is convex, and the
one-peak class is not (1.3.225). Source:
Paper 018, section 4 (Theorem 3). NEW in
Paper 018.""",
"""# Weighted hearing — on a line, the placement of the noise picks the winner

The answering case, on the smallest class of all:
F the line through one positive shape f_1, the
truth a* f_1 (the paper's section 5, its
Proposition 1). Here both estimators stand in
closed form. The least squares estimator is the
noise heard through the shape: a-tilde = the sum of
Y_i f_1(x_i) over the sum of f_1(x_i)^2, so each
point's noise is weighted by the size of the shape
at that point. The
l_1-estimator is the noise heard flat: because
f_1 is positive, every sign in its test (1.2.230)
collapses to the sign of the coefficient difference,
and a-hat = the plain sum of the Y_i over the sum
of the f_1(x_i) — every point weighted alike. The
two quadratic risks stand in exact ratio: the
risk of the l_1-estimator over the risk of the
least squares estimator is a weighted average of
the values f_1(x_i)^2, weighted by the
noise spreads sigma_i^2 — an average that stands
between the smallest and the largest of those
squares. So neither estimator dominates, and the
winner is named by an alignment: where the noise
sits against where the shape is large. With
f_1(x) = x and all the noise loaded on the first
point, the risk of least squares beats the other
by a factor of order n^2: at spread tau_n = n
there, the l_1-estimator is not consistent while
least squares converges at rate 1/n — the loud point of 1.2.235
read in the mirror, the shape standing near zero
exactly where the noise stands loud, so the
weighted ear barely hears it and the flat ear hears
nothing else. The reverse placement is the example of Baraud and
Maillard, cited by the paper: a shape large where
the noise is loaded makes least squares the
inconsistent one and leaves the l_1-estimator at
log(n)/sqrt(n). Hearing is a measurement choice —
the model's measurement agenda (1.2.14) meets the
same fork whenever a grade is read off data whose
noise is not spread evenly. Source: Paper 018,
section 5 (Proposition 1). NEW in Paper 018.""",
]

FOUNDATIONS = [
"""# Foundation: spread that changes from place to place

In the stage of 1.3.145 each reading carries noise,
and the noise at a place has a spread — how far its
readings scatter around the truth there. Noise of ONE SPREAD
carries that spread at every place.
HETEROSCEDASTIC (1.3.227) noise lets the spread
change from place to place: the i-th reading is
sigma_i times a centred draw, and the sigma_i need
not agree. The change can be the signal's own doing:
a yes-or-no reading whose chance is the signal has
spread set by the signal itself, and a count reading
likewise — so a model can be heteroscedastic by its
shape, before any failure of care. What a price for
an estimator may use, when the spreads differ, is
the whole question of Paper 018 (Chapter 29): a
price set by the largest spread is set by the worst
place; a price set by the average spread (1.2.232)
lets one loud place move it only by the share of
that place.
Builds on: the sequence model (1.3.145); average,
spread, distribution (1.3.8).""",
"""# Foundation: a heavy tail

A law of noise has a HEAVY TAIL when its far values
die away slowly: readings many spreads from the
centre stay common enough that high averages of the
size of the noise fail to settle. The measure the tracker
uses is the absolute moment of order p — the expected
value of |noise|^p. A law may carry the moment of
order 1 and of order 3/2 and no moment of order 2:
its readings have a centre and a typical size, but
no standing spread, and any method that begins by
squaring the noise begins by asking a question the
law cannot answer. The bell law (1.3.138) stands at
the other end: all its moments stand. Between them
the papers of cluster O draw their lines — Paper 012
under a slope bound on the law (1.3.149), Paper 018
under a moment of order p in [1, 2] alone (1.2.232).
Builds on: average, spread, distribution (1.3.8);
expectation (1.3.131).""",
"""# Foundation: the sign of a number

The SIGN of a number x, written sign(x), is 1 when
x > 0, 0 when x = 0, and -1 when x < 0. A sign keeps
one bit of a number — which side of zero it stands
on — and throws the size away. A sum weighted by
signs therefore asks a question of sides only: at
each place, is this candidate above that one, and
by which side does the reading vote? Such a sum
cannot be shouted down by one huge reading, because
a huge reading and a small one cast the same vote;
that is the whole strength, and the whole blindness,
of the test built on signs at 1.2.230.
Builds on: vector and distance (1.3.7).""",
"""# Foundation: one peak — the unimodal shape

A function on an interval is UNIMODAL (1.3.228)
when it rises, then falls: there is a place, the
peak, with the function never falling up to it and
never rising after it. The place of the peak is
part of the shape — a one-peak function is not told where
its peak stands. Two facts carry the weight of
Paper 018. First, the class of one-peak functions
is NOT convex (1.3.30): the average of two one-peak
functions with peaks at different places can carry
two peaks, and so stands outside the class — the
class is a union of monotone cones (1.3.151), one
for each peak place, glued along the monotone
functions, and gluing is where its good behaviour
ends. Second, the freedom of the peak is a freedom
to chase: a fit that may raise a peak anywhere may
raise one on a single loud reading (1.2.235).
Builds on: the monotone cone (1.3.151); mixing and
the convex hull (1.3.30).""",
"""# Foundation: cutting power — how rich the sets a class cuts are

Given a class of functions and one candidate in it,
look at the sets the other candidates cut out on
the design points by standing above the candidate,
and by standing below it. The CUTTING POWER of such
a family of sets — its VC-dimension, in the term
of the field — is the largest count of design points the
family can split in every possible way: for a
family of cutting power D, some D points can be
divided into the set and its outside in all
2^D patterns by members of the family, and no
D + 1 points can. Poor families — the cuts a line
makes, the cuts a few-piece step function makes —
have small cutting power however many points stand
in the design; rich families grow with the design
itself. Cutting power is the standing measure
of the field for how much a class can bend around one
candidate, and it is the currency the degree of
1.2.231 is paid in.
Builds on: set and element (1.3.3); a sample, and
independence (1.3.130).""",
]

DEFINED = [
"""Defined word: heteroscedastic — of noise in a
regression or a sequence model, whose spread
changes from place to place: each reading carries
its own sigma_i, and the sigma_i need not agree.
The plain account stands at 1.3.222. First spent
at Paper 018 (Chapter 29), for the noise the
isotonic least squares estimator is shown to
survive.""",
"""Defined word: unimodal — of a function on an
interval, rising then falling: never falling up to
one place and never rising after it, the place of
the peak free. The plain account stands at 1.3.225.
First spent at Paper 018 (Chapter 29), for the
class on which least squares and the l_1-estimator
part.""",
"""Defined word: extremal — of a candidate in a
class, whose cut sets are poor enough to be priced:
the families of sets where rivals stand above it
and below it carry cutting power (1.3.226) at most
some stated degree. The degree itself stands at
1.2.231. First spent at Paper 018 (Chapter 29),
for the candidates the average-moment price can
reach.""",
]
