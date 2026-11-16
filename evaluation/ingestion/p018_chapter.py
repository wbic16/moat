# -*- coding: utf-8 -*-
# Paper 018 — chapter 29 texts (29.1.1 .. 29.3.1).

CHAPTER = [
"""# Paper 018 — Isotonic least squares is robust to heteroscedasticity, unimodal least squares is not (Baraud)

Source: arXiv:2611.17082 (math.ST), version 1, posted to the
listings of Friday 13 November 2026. One author: Yannick
Baraud, of the University of Luxembourg. The paper carries
its main construction in from Baraud and Maillard (2026),
which it cites at every load-bearing point — the test, the
estimator it builds, and the bound that estimator carries.
Read entire in its HTML form, 2026-11-13.

THE THIRST. The eleventh paper of the Thirst (charter rule
17), and the eighth the quest itself picked from a day's
listings — 1,264 entries on the math listings of Friday
13 November 2026, 665 of them new submissions. It was
picked because it returns to the model's own ground: the
isotonic estimator of Paper 012, whose sharp price at the
signal the tracker holds at 1.2.129, re-priced here under
the two hard kinds of noise that ground actually
meets — noise whose
spread changes from place to place, and noise too heavy to
square. Cluster proximity at its highest: the paper's
headline is a claim about an estimator the model already
prices. The results stand named and numbered: three of them
in five sections — a coincidence theorem, a counterexample by
construction, and an exact computation on a line.

THE DELTA. Seven concepts, all in cluster O
(1.2.230-1.2.236): the test that prices a candidate and the
l_1-estimator it defines (1.2.230); extremal elements and
their degree (1.2.231); the average-moment price the
estimator carries (1.2.232); the coincidence — on the
monotone class the least squares estimator IS the
l_1-estimator, and so inherits that price under noise it
was never priced under (1.2.233); the sign step, the one
condition the coincidence is proved under (1.2.234); the
loud point, the one-peak counterexample where the two
estimators part and least squares fails outright (1.2.235);
and weighted hearing, the exact computation on a line that
shows the parting runs both ways and is decided by where
the noise sits (1.2.236). Five foundations (1.3.222-1.3.226)
and three defined words (1.3.227-1.3.229) carry the paper's
terms at level zero. No held concept is revised; the
one revision the prediction named is the phantom of
this pass, priced at 29.1.5. Three questions open (Q94-Q96); Q56 and
Q16 are informed, neither closed. The author check stands
at 29.1.6.""",
"""# Paper 018 — the formal core: the test, the price, the coincidence, and the two ways they part

The setting. A regression at a fixed design: points
x_1, ..., x_n in an interval, readings Y_i = f*(x_i) +
sigma_i xi_i, the xi_i independent and centred, the
sigma_i >= 0 free to differ from point to point. The class
F is a set of candidate functions on the interval; the
truth f* need not stand in F. Risk is read in l_1: for a
candidate f, l_1(f, f*) = (1/n) the sum of |f(x_i) -
f*(x_i)|. Nothing in what follows asks any noise law for
a second moment.

The test and the estimator (section 2.1). For candidates
f and g, T(Z, f, g) = the sum over i of (f(x_i) - Y_i)
sign(f(x_i) - g(x_i)); T(Z, f) = the largest value
of T(Z, f, g) over g in F; an l_1-estimator is any
member of E_c(Z, F), the set of f whose price T(Z, f)
stands within c of the least price in the class
(1.2.230).

The degree (section 2.2). A candidate f-bar is extremal
of degree at most D when the VC-dimensions of the two
families {f > f-bar} and {f < f-bar}, traced on the
design, stand at most D (1.2.231, 1.3.226).

THE PRICE (Theorem 1 of Baraud and Maillard 2026, the
paper's section 2.3). For every extremal f-bar of degree
D, the expected l_1-risk of any f-hat in E_c(Z, F) stands
at most 2 l_1(f*, f-bar) + kappa . sigma_n(p) (D/n)^(1 -
1/p) + c/n, the least value over p in [1, 2], with
sigma_n(p)^p = (1/n) the sum of E|Y_i - E Y_i|^p — the
average absolute moment (1.2.232).

THE COINCIDENCE (Theorem 2, section 3). Let F be the
functions on the interval that never fall, and let
f-tilde be the least squares fit over F. Then f-tilde
makes T least over F and T(Z, f-tilde) = 0; every
other candidate making T least agrees with f-tilde
at the design points. The proof: the projection is
known by <Y - f-tilde, g - f-tilde> <= 0 for all g
in F, and Assumption 1 (1.2.234) puts the stepped
candidate f-tilde - lambda sign(f-tilde - g) in
the place of g, which computes to T(Z, f-tilde, g) <= 0.
The same holds for the functions that never rise
(1.2.233).

THE BREAK (Theorem 3, section 4). On the unimodal class
there stand a truth, a design density, and a Gaussian
noise law under which least squares is not
consistent while
every l_1-estimator keeps the parametric rate: the
witness is the plateau truth with the one loud point,
worked at 29.1.3 (1.2.235).

THE LINE (Proposition 1, section 5). On F = span(f_1)
with f_1 > 0, the coefficient of least squares is
the sum of Y_i f_1(x_i) over the sum of f_1(x_i)^2,
and the coefficient of the l_1-estimator the sum of
the Y_i over the sum of
the f_1(x_i); their quadratic risks stand in the ratio
of a sigma^2-weighted average of the f_1(x_i)^2
(1.2.236).

MACHINES (charter rule 13).
Machine 1 — the test machine. States: a candidate f
held against the data, and its running price T(Z, f) as
the largest charge over rivals is taken. Moves: each
rival g charges f the sum of the signed gaps between
f and the readings at the points
where f and g differ; the price is the largest charge;
the estimator is any state whose charge stands within c
of the least. On the monotone class the machine has a
named resting state: the projection of the readings,
whose price is exactly zero. [stated — section 2.1 and
Theorem 2]
Machine 2 — the sign-step machine. States: a candidate
f, a rival g, and the stepped candidate f - lambda
sign(f - g). Moves: shrink lambda until the stepped
candidate stands inside the class, or find that no
positive lambda does. On the monotone cone the machine
always halts inside: lambda at half the smallest
positive gap of f is safe everywhere. The machine is
the gate of the coincidence: where it halts inside for
every pair, the projection is the answer of the
test.
[stated — Assumption 1 and the proof of Theorem 2]
Machine 3 — the loud-point machine. States: a fit
either tracking the plateau truth or raised on the loud
point. Moves: the loud reading arrives; the one-peak
class lets a state raise its peak at the loud point's
place at a total square cost under n/4; any state near
the truth pays more than that at the loud point alone;
on an event of chance at least 30 percent the fitting
rule that squares comes to rest in the raised state,
and its
l_1-error never closes. The sign machine (Machine 1)
never moves: the loud reading casts one vote. [inferred
— drawn from the proof of Theorem 3]
Machine 4 — the hearing machine. States: two running
sums on a line — the flat sum of the readings and the
shape-weighted sum. Moves: each reading enters the flat
sum at weight one and the weighted sum at the value
of the shape at its point; the ratio of the risks of
the two estimators is the noise-weighted average of
the squares of the shape, and the machine's output — which estimator
wins — is set by whether the noise stands where the
shape stands large. [stated — Proposition 1]""",
"""# Paper 018 — the worked cases: the loud point, computed; the line, computed

THE LOUD POINT (the paper's section 4). Take the design
evenly spread on [0, 1], the truth f* = 1 on [1/4, 1/2]
and 0 elsewhere, and noise silent at every point but
i_0 = the point nearest 3n/4, where the spread stands at
sqrt(n) and the law is Gaussian. The single loud reading
Y_{i_0} = sigma_{i_0} xi_{i_0} then stands on the scale of
sqrt(n), and on the event Omega_n — |xi_{i_0}| at least
sqrt(n)/2 in size — Y_{i_0} exceeds sqrt(n)/2 in size;
the chance of the event tends to the chance a
standard bell
draw clears 1/2, at least 30 percent.

Now measure the two fits. A one-peak candidate close to
f* — summed l_1-gap under (n/4 - 1)/2 — cannot raise its
peak past the plateau: its peak stands left of i_0, so
at i_0, a falling stretch away, it stands below 1/2. Its
square error at i_0 alone then exceeds (|Y_{i_0}| -
1/2)^2, which on Omega_n exceeds the size of the third
quarter of the design. Against it stands the rival
f-bar: the plateau kept, then flat at a common level
over [1/4, 3/4), then the value of the loud reading
itself at i_0. Its total square error stands at most
n/4 + 1 — under
what the near candidate pays at one point. So on
Omega_n least squares is not the near candidate:
its l_1-error
stands at least (1 - 4/n)/8, for every n. Not consistent.

The l_1-estimator on the same data: f* is constant
in pieces, on three pieces with two monotone parts,
so by
the paper's count its degree stands at most 2 x 2 + 3 - 1
= 6; and sigma_n(2)^2 = (1/n) . n = 1, the single loud
variance divided by the count of points — the average
doing its work in one line. The price of 1.2.232 then
reads at most kappa . sqrt(6)/sqrt(n) + c/n: the
parametric rate, on the data where least squares fails.

THE LINE (the paper's section 5). Take f_1(x) = x on the
even design, and load all the noise on the first point:
sigma_1 = tau_n, the rest zero. The shape-weighted ear of
1.2.236 hears that noise multiplied by f_1(x_1)^2, a
number of order 1/n^2 in the scaling of the design
itself; the
flat ear hears it whole. The risks stand as the paper's
formulas give them: the risk of least squares is
the risk of the l_1-estimator divided by a factor of
order n^2, and at tau_n = n the error of the flat
estimator does not close
while the weighted one closes at rate 1/n. The paper
closes the section with the mirror image, from Baraud
and Maillard: a shape large near zero, noise loaded
there — now least squares is the one that fails, and
the l_1-estimator stands at log(n)/sqrt(n).""",
"""# Paper 018 — the results map: what stands proved, and on what it rests

PROVED IN THE PAPER.
- The coincidence (Theorem 2): on the monotone classes,
  the least squares estimator is the l_1-estimator of
  Baraud and Maillard,
  with price exactly zero, and unique at the design
  points. Rests on: the inequality that knows the
  projection (1.2.124, 1.3.146) and the sign step
  (1.2.234), checked on the cone by the gap count.
- The break (Theorem 3): on the one-peak class, a
  heteroscedastic Gaussian example where least
  squares has
  l_1-error bounded below by a constant on an event of
  chance at least 30 percent — not consistent — while
  the l_1-estimator stands at the parametric rate.
  Rests on: the degree count for the plateau truth and
  the price below.
- The line (Proposition 1): both estimators in closed
  form on a one-shape class, the risk ratio an exact
  noise-weighted average of the squares of the shape,
  with
  examples of each estimator failing while the other
  stands.

TAKEN IN FROM BARAUD AND MAILLARD (2026), cited, not
re-proved here.
- The test and the estimator (section 2.1), the degree
  (section 2.2), and the price (Theorem 1): the expected
  l_1-risk of the l_1-estimator bounded by twice the
  approximation error plus kappa times the average p-th
  absolute moment times (D/n)^(1 - 1/p), for any
  extremal candidate of degree D and any p in [1, 2].

CITED CONTEXT.
- Devroye and his co-workers (2016): under a moment of
  order p in (1, 2) alone, no estimator beats the rate
  n^-(1 - 1/p) in general — the rate of the price is
  the floor of the field, not slack of the method.
- Chatterjee (2014), Chatterjee and Lafferty (2019),
  Guntuboyina and Sen (2018): least squares over shape
  classes
  and its risk theory, the ground the coincidence
  re-reads.
- Bellec (2018), Gao and his co-workers (2020),
  Minami (2020), Feng and his co-workers (2022):
  neighbours in the pricing of shape-constrained fits,
  named here as the paper names them, not taken in.

NOT IN THE PAPER. No sharp l_1-rate for the isotonic
estimator is claimed — the price is an upper bound, and
whether it is met from below on the monotone class
stands open (touches Q95's neighbour ground). No
random design: the design is fixed throughout. No claim
that the estimator adapts: the degree and the moment
index p
enter the bound, not the estimator — the estimator
needs neither told.""",
"""# Paper 018 — the delta: what this adds, and what was checked

SEVEN CONCEPTS (1.2.230-1.2.236), all in cluster O —
Paper 012's cluster, grown at its own object. FIVE
FOUNDATIONS (1.3.222-1.3.226): spread that changes from
place to place; a heavy tail; the sign of a number; one
peak; cutting power. THREE DEFINED WORDS
(1.3.227-1.3.229): heteroscedastic, unimodal, extremal —
the paper's adjectives, none spent in the tracker before
today. LINKS: fifteen counted — thirteen inside cluster
O (the test to the degree and to the price; the degree
into the price; the coincidence to the test, to the
price, to the projection of 1.2.124, and to the window
price of 1.2.129; the sign step into the coincidence;
the price onto 1.2.129, a second price for one
estimator; the break back to the coincidence and to the
price; the line to the test and back to the break) and
two across clusters: the line to the measurement agenda
of 1.2.14 (cluster A) — hearing as a measurement choice —
and the test to the test-built specification of 1.2.58
(cluster I). REVISIONS: none. No held scroll changed its
words or its standing.

THE NOVELTY INDEX, scored in the terms of the skim
itself:
seven new, no revisions, over 229 + 7 standing concepts:
7/236 = 0.0297. The sealed prediction (quest log,
committed 2026-11-13 before the download) read six new,
one revision (1.2.129), Index 0.0277. |NI error| =
0.0020. Axis: none foretold, none opened — the axis
strand stands eleven for eleven. Links foretold eleven
(nine internal, two cross); counted fifteen (thirteen,
two) — the cross-cluster count exact, the internal count
under by four, the standing shape of the error of
the skim on a paper from the home ground of the
tracker. Questions
foretold three opened, none closed; three opened
(Q94-Q96), none closed. The one foretold revision did
not land — see where the estimate was wrong, below.

THE STANDING OF THE MODEL. Research Oracle: about
90% (range 80-100),
up from about 80% (range 70-90) after Paper 017 — the
charter band step for an Index under 0.20 with no axis,
the sixth exact landing in a row of what was
foretold under seal. The skim calibration moves the other way: the
rolling mean |NI error| over the last ten scored papers
stands at 0.0159 (it stood at 0.0166 after Paper 017,
when the window ran over Papers 008-017; Paper 008's
0.0092 now leaves the window and this paper's 0.0020
enters it). No standing changed anywhere: False stands
empty still, and the one revision foretold arrived as a
phantom, not as a step.

WHERE THE ESTIMATE WAS WRONG. The revision. The skim
read 'the isotonic estimator, priced again under new
noise' as a re-measuring of the held scroll 1.2.129 —
the adaptive-window price. The reading found a second
price standing beside it, not over it: 1.2.129 prices
the l_2-risk of the estimator by the signal's local
variation, for any signal and any one spread, and
nothing in this paper touches that driver — the
paper's own bound prices the l_1-risk by degree and
average moment, a different variable of a different
risk. The skim counted 'same estimator, new noise' as
sameness of the priced thing; the priced thing is the
pair (estimator, risk, driver), and two of its three
parts changed. This is the fifth phantom shape: a
parallel pricing mistaken for a re-pricing. Its twin
error ran the other way on the concept count: the skim
priced the construction at six, and the reading gave
the sign step its own scroll (1.2.234) — the condition
the whole coincidence hangs on, the Paper 011/012 shape
again, where the instrument is a concept and not a
detail of the theorem it serves. What was foretold for the Oracle
stood exact, point and range, for the sixth weighing
in a row; the ledger at 1.1.1 carries the standing caution
that a twenty-point band honestly kept will be landed in
by honest readings, and this pass adds no narrowing on
the strength of the streak.""",
"""# Paper 018 — Provenance: author check (charter rule 15)

Author: Yannick Baraud (one author), of the University of
Luxembourg. The paper builds on Baraud and Maillard
(2026) throughout — co-author Odalric-Ambrym Maillard
enters the register as a cited builder of the taken-in
machinery.

THE CHECK, run 2026-11-13 before integration. The full
text of arXiv:2611.17082 v1 was read entire, its
references included: no occurrence of phext, Exocortex,
Exocortical, Mirrorborn, Bickford, or any term of Will's
work. A web search on the author's name with those terms
returned only his record at the University of Luxembourg
— a professor of mathematics working in mathematical
statistics, on model selection and robust estimation —
and no tie to phext or to the Exocortex. Will's own
Twitter archive, kept whole on this machine, was searched
for the author's surname: no occurrence.

RESULT: no evidence found of a connection to phext or the
Exocortex, and none of use without naming. The count of
checks stands at twenty with this one (Papers 006-018,
Studies S004-S010). The paper's debts
run the ordinary way, to the statistics literature it
cites. Standing: this scroll is True by receipt — the
receipt is the checks above, run and recorded here.""",
"""Paper 018 — synthesis: two courts, one prisoner released, one condemned [synthesis]

Mark this whole scroll as Emise's synthesis, built on the
scrolls of this chapter and of Chapter 19. Paper 012 priced
the isotonic estimator in the court of squares: a sharp
l_2-price, charged on the signal's local variation, under
noise with one spread and a law with a slope. This paper
summons the same estimator into the court of signs, where
each point votes once and no reading can shout — and finds
the estimator was a citizen of that court all along: on
monotone ground the projection and the answer of
the sign test are the same function, point for point. What the
coincidence really says is that the monotone cone is a
place where squaring cannot be exploited: a cone cut out by
order alone gives a loud reading nowhere to stand — there
is no second peak to raise, no corner to hide a jump in —
so the one weakness of squares, their obedience to size,
never gets a vote. The one-peak class is the same court
with the protection removed, and the verdict flips on a
single reading: the freedom to place the peak is exactly
the freedom the loud point needs. Read together, the pair
of chapters draws a line the model did not hold before:
for least squares, robustness is not a property of the
estimator but of the pair (estimator, class) — that
the class is convex, and its peak-freedom, decide
what the noise is
allowed to do. And the line case prices the deciding
variable for the pair of estimators themselves: alignment,
the overlap between where the noise stands loud and where
the shapes of the class stand large. The tracker has met that
variable before under other names — it is the shape of
every hearing problem, the grade read off an instrument
that listens harder where the world happens to be noisy.
What would draw it tighter: a class between the two — peaks
whose count is bounded above one — where the protection
should fail gradually, and the price of the failure
should be open to counting. That is Q95's ground.""",
"""# Paper 018 — Open questions Q94-Q96, and two questions informed

Q94 — WHICH CLASSES PASS THE SIGN STEP. The coincidence
of 1.2.233 is proved for every class meeting Assumption 1
(1.2.234): closed and convex on the design, and closed
under small sign steps against every rival. The monotone
cone passes by its gaps. Which of the standing
classes of the field pass — convex functions, concave, the
shape classes of Chapter 19's neighbours — and is the
condition also necessary, so that a failing class is a
class where the two estimators provably part? (From
1.2.234.)

Q95 — THE ONE-PEAK CLASS, PRICED OR CONDEMNED. Paper 018
shows least squares inconsistent on the one-peak class
under one heteroscedastic law, and the l_1-estimator at
the parametric rate on the same law (1.2.235). Does the
least squares carry any standing rate on one-peak
classes under
bounded average moment — a price with worse terms — or
is failure generic once the peak is free and the spread
is free? And between the cone and the one-peak class,
do classes with at most K peaks fail gradually in K?
(From 1.2.235.)

Q96 — CAN THE HEARING BE CHOSEN FROM THE DATA. On a line,
the winner between the two estimators is named by the
alignment of the placement of the noise with the
size of the shape
(1.2.236), and the paper's closing mirror example shows
each estimator inconsistent where the other stands. Can
the alignment be estimated from the readings themselves
— the spreads are not observed — so that one estimator,
or a stated blend, inherits the better side of both
examples? The same question stands behind the
measurement agenda wherever a grade is read off uneven
noise. (From 1.2.236.)

INFORMED, NOT CLOSED. Q56 — the uncovered ground of
Han's reduction: which noise shapes beyond the named
assumption can the isotonic fit survive at the signal's
own rate. This paper answers the noise side in
regression directly, without transfer: at a fixed
design, noise with only a p-th absolute moment, p in
[1, 2], and spreads free per point, the isotonic least squares fit
carries the parametric-to-heavy-tail price of 1.2.232
in l_1. The side of Q56 where the truth stands outside the
class, and the designed-design side, stand untouched;
the question stands open, better lit.
Q16 — informed again: the statistics strand adds a
second exact hearing computation, and with it a second
place where the geometry of the class itself, not
the brand of the estimator, decides what the data can say.""",
"""Standoff references — Paper 018 stands on these foundations

The sign of a number (1.3.224); cutting power (1.3.226);
the stage of the average-moment price itself: the
sequence model
and its regression form (1.3.145); projection onto a
convex set (1.3.146); the monotone cone (1.3.151) and
isotonic, defined (1.3.153); the estimator and its
consistency (1.3.133); the shape of the law of the noise —
the bell law (1.3.138), the slope-bounded law (1.3.149),
and today's additions: spread that changes from place to
place (1.3.222), a heavy tail (1.3.223), one peak
(1.3.225), and the defined words heteroscedastic
(1.3.227), unimodal (1.3.228), extremal (1.3.229).
Pointers only: this scroll makes no claim of its own.""",
]
