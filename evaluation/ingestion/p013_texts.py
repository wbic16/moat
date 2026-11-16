# -*- coding: utf-8 -*-
"""Paper 013 integration texts (tracker voice). Imported by integrate_p013.py."""

CONCEPTS = [
"""# Role weights — the two shares of one observation

Cross-validation (1.3.156) judges a fitted model on
cases it did not train on, by turns: the data are
split, again and again, into a part that trains and a
part that validates (1.3.157), and the held-out scores
are averaged into one estimate. In that judging, one
observation plays two roles. When it is held out, its
own score is one of the scores the estimate averages.
When it trains, it helps fit the models that score
the others. Paper 013 gives each role a weight, and
the whole theory of the paper is read off the two
weights.

The validation weight of an observation is its share
of all the validation evaluations the procedure makes
— the number of splits that hold it out, over the
total number of held-out scores. The training weight
is its share of all the training use: over the splits
that train on it, the split's own share of the
estimate times its share of that split's training
set. Each set of weights sums to one over the data,
so each is a dealing of the whole estimate, or the
whole training, among the observations.

The designs of the field deal the weights differently.
Under K-fold, every observation is validated once per
partition and trains in the other K-1 folds, and both
weights stand at 1/n for every observation: the design
is BALANCED. Under Monte Carlo splitting the count of
validations is a draw, so the weights lean on the draw
— and the two weights are tied: an observation
validated more often trains less often, in exact
proportion. Under the bootstrap the two weights are
separate draws, neither fixing the other. A design
that deals uneven weights pays for the unevenness in
variance (1.2.135); a balanced design pays nothing.

Two held ideas stand near. The estimate itself is a
judge of a fitted model, as off-policy evaluation
(1.2.110) is a judge of a rule: both price a thing
they did not run as it will run. And a weight that
deals a whole among parts, by the share each part
carries, is the move of the budget that follows the
mass (1.2.70) — there the mass is attention, here it
is the two roles of judging. What the weights feed
stands at 1.2.132. As taken in by: Paper 013
(Chapter 20).""",
"""# The two influences — what one observation moves, in each role

A weight says how much of the estimate an observation
carries; an influence says how much it moves. Paper
013 separates the two roles of 1.2.131 into two
influences, each a function of the one observation,
with the rest of the data averaged out.

The VALIDATION influence of an observation is its
held-out score with the training data averaged away:
what its score is expected to be, given only itself.
Its spread over the data is the constant sigma_V^2.
The TRAINING influence is the other direction: fix a
value z, and ask how much the expected performance of
the fitted model moves when one of its training
observations stands at z, scaled by the training size
so the number stays of size one as the data grow. Its
spread is sigma_T^2. The two influences of the same
observation can lean together or against each other;
their covariance is the third constant, gamma_0, and
it can stand negative.

Added, the two influences make the COMBINED influence
of the observation — the single function whose spread
is the first-order price of the whole judging:
V = sigma_V^2 + sigma_T^2 + 2 gamma_0. The three
constants are constants of the model, the metric, and
the population — not of the design. The design enters
only through the weights of 1.2.131, and the variance
identity of 1.2.133 is the meeting of the two.

One special case governs much of the field's older
practice. When a learner is judged by the very loss
it was fit to make small, and smoothly, the training
influence dies at the limit: the fitted model stands
at a smallest point of that loss, where a step in any
direction moves the expected loss by nothing at first
order. Then sigma_T^2 and gamma_0 vanish, and only
the validation term remains — a fixed-model variance
formula is right at first order for such a pairing,
and wrong for a mismatched one, as when a model fit
by likelihood is reported by the Brier score.

The training influence is kin to a held concept of
this cluster: the own-observation effect (1.2.113),
where a walk's reading of a case is bent by the case
having trained the walk. Both price the same fact —
a case inside the fit moves the reading — one for a
walk in high dimensions, one for any fit at all. As
taken in by: Paper 013 (Chapter 20).""",
"""# The variance identity — the price of a judging, exactly

The central result of Paper 013 is an identity, not a
bound: at every sample size, for every design that
trains on the same count of cases in every split, the
variance of the cross-validated estimate is a finite
series whose terms are known in shape. The first
term is a quadratic form in the role weights of
1.2.131, with the three constants of 1.2.132: sigma_V^2
times the sum of the squared validation weights, plus
sigma_T^2 times the sum of the squared training
weights, plus twice gamma_0 times the sum of the
products. All the design contributes, at this order,
is three numbers — the role moments, the averaged
sums of those squares and products over the dealing
of the splits.

Above the first order, the series continues by the
size of the sets of observations that move the
estimate together. The joint effects are split by the
sets that carry them (1.3.159): pairs of observations
first — one validated while the other trains, in both
directions, and two training together — each order
with its own constants, the pair constants tau^2,
kappa, sigma_chi^2 and xi among them, and its own
weights of that order. Every term of the series is
nonnegative, so every stopping point of the series is
a lower bound on the variance: the identity can be
read partway and never overstates what it has read.

The simplest case shows the shape whole. When the
fitted model is the mean of its training set, judged
by squared error, each held-out score is a square in
the observations, the joint effects stop at pairs,
and the identity ends at order two, with all four
pair constants standing at 4 sigma^4 in size — the
two kinds of pair interaction equal in size, and xi
against them in sign, an opposition the fold-count
laws of 1.2.136 turn on.

Two guards stand on the identity. It is proved under
one standing condition on the data, the design, and
the model — cases drawn independently, splits drawn
independently of the data, a fit that treats its
training cases alike — and a second condition that
bounds how much of the variance the joint effects
carry, which the first-order reading needs and the
full identity does not. The bootstrap, whose training
sets have no fixed size, stands outside the identity
as stated and is brought under its first order by a
condition of its own, on how the fit answers to a
case counted twice.

The identity is this cluster's second floor. The
floor the classical theory sets for any judge
(1.2.116) bounds what a judge's answer can be worth;
the identity prices what a judge's answer costs to
trust, and its lowest term — the sampling variance of
1.2.134 — no design at the same training size can go
below. As taken in by: Paper 013 (Chapter 20).""",
"""# Sampling variance and split noise — the two parts of the price

The identity of 1.2.133 fixes the splits and varies
the data. Paper 013 then turns the conditioning
around, and the variance of the estimate splits into
two parts with different owners.

The SAMPLING variance is the variance the estimate
would keep if the splitting were repeated without
end: the variance, over datasets, of the estimate
averaged over all dealings of the splits. It depends
on the design only through the count of training
cases. Every design at a given training size has the
same sampling variance, and it is a floor: no
repetition of the splitting brings the variance
below it, because repetition averages the dealing,
not the data.

The SPLIT NOISE is the rest: the variance the dealing
of the splits adds at a fixed dataset, averaged over
datasets. It is the only part of the price where
designs at one training size differ at all. At first
order it is exactly the imbalance penalty of 1.2.135.
For K-fold it has a closed law of its own: repeat the
partition R times, independently, and the variance is
the sampling variance plus the split noise of one
partition divided by R — exactly, under the standing
condition alone. Repetition buys down only the noise
of the dealing; the sampling floor stands untouched.

Two older results of the field fall out of the split.
Burman's finding, that the number of repetitions of
K-fold enters the variance only at the second order,
is the law above read at the orders where K-fold's
split noise lives. And the corrected variance of
Nadeau and Bengio for Monte Carlo splitting is exact
at first order only under one named balance of the
constants — twice p times gamma_0 equal to (q - p)
times sigma_T^2, the condition for two split estimates
to stand correlated by exactly q — which the
matched-loss case of 1.2.132 meets in the limit, and
a mismatched metric need not meet at all, the error
then standing in either direction.

The split is the paper's answer to a confusion the
field carried for decades: the spread of repeated
cross-validation on one dataset feels like the
uncertainty of the estimate, and it is not — it is
the smaller, removable part, measured again at
1.2.138. As taken in by: Paper 013 (Chapter 20).""",
"""# The imbalance penalty — uneven weights are variance

At a fixed training size, designs differ only in
split noise (1.2.134), and at first order the split
noise has one source: the dealing of the role weights
of 1.2.131 unevenly. Write each weight as 1/n plus a
departure. The departures sum to zero, the cross
terms fall away, and what remains is a quadratic form
in the departures with the covariance of the two
influences of 1.2.132 as its matrix. That remainder
is the IMBALANCE PENALTY, Q_D. It is nonnegative for
every design, and it is zero exactly when the design
is balanced.

Read design by design, the penalty is explicit.
K-fold, with any number of repetitions, pays nothing:
its weights do not depart. Monte Carlo splitting pays
(1/nS) times (p/q sigma_V^2 + q/p sigma_T^2 - 2
gamma_0), and the bootstrap pays (1/nS) times (p/q
sigma_V^2 + sigma_T^2 - 2 gamma_0): both deal
validation counts by draw, and their penalties fall
only as the count of splits grows — at a fixed count
of splits the penalty stands at the same order as the
variance itself, not below it.

The penalty is the first order of a general law
(Theorem 4 of the paper). A design can be balanced
order by order: its weights of order k — the weights
on the joint effects of k observations — either vary
with the dealing or they do not. A design balanced
through order k has no split noise through order k,
and its variance is the sampling variance through
that order; every other design at the same training
size stands above that floor by its penalty and its
higher split noises. Under the dominance condition, a
design is variance-optimal at its training size, up
to the order named, exactly when its penalty and
split noises fall below that order.

Balance at the second order has a name and a price.
PAIR BALANCE asks that every pair of observations
share a fold equally often across the repetitions;
random partitions do not give it, and built ones make
the second-order split noise exactly zero — the paper
checks this on a built design, where the pair-balanced
split noise of the sample mean stands at zero to
machine precision while an unbalanced dealing of the
same count stands measurably above the floor (20.1.3).
But exact pair balance costs at least K(n-1)/(K-1)
fits — more than leave-one-out costs — and the paper's
verdict is plain: when the sampling variance does not
rise with the training size, pair balance is generally
not worth its compute. As taken in by: Paper 013
(Chapter 20).""",
"""# Fold counts — the count of folds is not the price

The field's standing worry about K-fold is that more
folds mean more overlap between training sets, and
more overlap must mean more variance. The identity of
1.2.133 shows the worry misreads where overlap acts.
Overlap makes held-out scores covary, through
sigma_T^2 and gamma_0 — but for K-fold those
covariances total (sigma_T^2 + 2 gamma_0)/n at first
order for EVERY K, because every observation's
training weight stands at 1/n whatever the fold count.
The count of folds reaches the first-order variance
only through the training size it sets.

So, when the combined influence of 1.2.132 settles to
one limit as the training size grows, the first-order
variance of K-fold is V_infinity / n for every K and
every count of repetitions: K-INVARIANCE. The law has
a named failure. If a fit leans on the full sample
size and not only on its training set — a ridge
penalty set at c times n, dealt to a training set of
size pn, bites at c/p per case — the limit itself
moves with K, and invariance falls with it. Tuning
inside the training set, by an inner cross-validation
of that set alone, does not break it.

Leave-one-out is the family's limit and, under named
conditions, its floor. It deals no splits at all, so
its split noise is zero at every order, and its
variance is the sampling variance at training size
n-1. When the sampling variance does not rise as the
training size grows, no repeated K-fold stands below
it, up to the second order; and when in addition the
pair covariance xi is not positive, the variance does
not rise with K, so at a fixed budget of fits one run
with as many folds as the budget allows beats the
same budget spent repeating fewer folds. Repetition,
read through 1.2.134, converges to K-fold's own
sampling variance — never to leave-one-out's.

The second order is where fold counts do their real
work: the split noise of one partition falls as
G(K)/n^2, with G(K) built from the pair constants —
the first and third of its terms nonnegative and
falling in K, the middle term carrying the sign of
xi, the opposition the sample-mean case of 1.2.133
shows standing negative. For pairwise metrics the
whole law turns, and stands at 1.2.137. As taken in
by: Paper 013 (Chapter 20).""",
"""# Pairwise metrics — when the unit of judging is a pair

Some scores are not paid case by case but pair by
pair: the area under the curve (1.3.160) reads a case
and a control together and pays for their order. The
identity of 1.2.133 extends to such metrics — the
pairwise case is Theorem 3 of the paper — with three
changes: the judging conditions on the labels, which
fix which pairs count; each observation is weighed
through the pairs it stands in, within its own class;
and a third kind of joint effect appears, the pair
interaction, the part of a pair's score that stands
on both its members together. The constants split by
class, and the training constant gains a LABEL PART:
a training case shifts the class mix of the training
set, and with it the expected score. At first order a
pairwise metric then behaves as a case metric with
its own constants, and the training terms that
fixed-model formulas miss — DeLong's variance among
them — stand at (sigma_T^2 + 2 gamma_A)/n.

The design law of 1.2.136 breaks here, in one named
place. Ordinary K-fold judges only the pairs that
share a validation fold: one K-th of all case-control
pairs. Each partition averages the pair interaction
over a different K-th, and the split noise this adds
— the PAIR-COVERAGE COST — grows in K, at
lambda_4 (K-1) / n^2 with lambda_4 the pair
interaction's spread divided by the product of the
class shares, so it grows again as the outcome grows
rare. More folds raise the training size and lower
the coverage at once, and an in-between fold count
can stand best: the one place in the paper where the
fold-count law of the case metrics does not carry.

The repair is a design, not a correction. PAIRED
K-fold splits each class into K folds and fits all
K^2 pairings of a case fold with a control fold, so
every case-control pair is judged exactly once: the
sampling variance stands as it stood, and the
coverage cost is removed whole. It is never worse
than ordinary class-stratified K-fold at the same
count of repetitions, and its limit, as the folds
shrink to single cases and single controls, is
LEAVE-PAIR-OUT — the pairwise leave-one-out, which
judges every pair once and carries no split noise at
all. Judging by pairs must balance the pairs, not
only the cases: the dealing of 1.2.131 has a second
storey. As taken in by: Paper 013 (Chapter 20).""",
"""# Normality and the audit of variance estimators — what an interval must carry

The identity prices the variance; the paper's last
theorem says what shape the estimate's own spread
takes. Under one standing condition, and a set of
difference conditions — no one observation moves the
estimate by a share of its own spread that fails to
vanish, and one observation's effect leans on the
others weakly, or strongly on only a few — the
estimate, scaled by the root of n, settles to the bell
law (1.3.161) centered at the target, with the FULL
variance the identity gives at the realized splits,
higher orders included. The proof runs by a normal
approximation for functions of independent inputs
(Chatterjee's), not by a sum of terms, so it stands
even where the joint effects carry a first-order
share of the variance and the older stability route
fails — a case the paper builds and checks by hand
(20.1.3). For a balanced design the limiting variance
is V_infinity; for Monte Carlo and the bootstrap it
stands higher by the imbalance penalty of the realized
splits, which stays in the limit and must stay in the
interval.

With a consistent reading of that variance, Wald
intervals and tests stand valid. What such a reading
must carry is the audit the paper then runs over the
field's standing estimators. The standard estimate —
the spread of the held-out scores, divided by n —
reads the validation term alone and misses
C_ell = (sigma_T^2 + 2 gamma_0)/n, the covariance
held-out scores take on through the training cases
their models share; the intervals built on it
undercover, as Bates and his co-workers measured.
DeLong's variance, and the influence-curve variance
that holds each fold's fit fixed, miss the same
training terms for the area under the curve (1.2.137).
The spread of repeated cross-validation on one
dataset reads the split noise of 1.2.134, which under
the dominance condition is smaller than the order of
the variance itself — as a standard error it
vanishes against the thing it claims to measure.
One standing method reads the first-order sampling
variance whole, training terms included: a weighted
bootstrap of the whole procedure, with the split
noise fitted out of each replicate (Cai and
co-workers) — at the price of thousands of fits, and
blind to the higher orders the theorem keeps. And
under the audit stands a proved limit: from the
held-out scores of one run, no unbiased estimate of
the K-fold variance exists at all (Bengio and
Grandvalet). A third road is named, not built: draw
fresh datasets from an estimated population and run
the procedure again on each, splits and all — it
reproduces every part of the price, to the measure
the estimated population is true.

The audit reaches back to the start of this cluster.
A judge is priced three ways in cluster O now: for
its bias against the rule it never ran (1.2.110), for
the sharpness of its price at the case in hand
(1.2.125), and here for the spread of its own reading
— and the measurement agenda of cluster A (1.2.14)
gains a worked case of its standing warning, that a
grade without its variance is half a grade. As taken
in by: Paper 013 (Chapter 20).""",
]

FOUNDATIONS = [
"""# Foundation: cross-validation — judging a fit on cases it did not train on

A model is fit on some cases and used on others. To
say how well it will do on cases not yet seen, hold
some of the cases in hand back from the fitting, fit
on the rest, and score the fit on the held-back
cases: those scores were earned on cases the fit
never trained on, so they speak of new cases, not of
memory. Do this by turns — split the data into a
training part and a validation part again and again,
each time fitting on the first and scoring on the
second — and average the held-out scores. The average
is the cross-validation estimate of the model's
performance, and the whole way of judging is
cross-validation.

Builds on: a sample, and independence (1.3.130);
estimator and consistency (1.3.133).""",
"""# Foundation: a split, a fold, and a partition — the dealing of the turns

One turn of cross-validation (1.3.156) is a SPLIT of
the data into two parts: a training set, which the
model is fit on, and a validation set, the rest,
which it is scored on. The share of the data in the
training set is the training fraction. A way of
making the splits, with its training fraction and
its count of splits, is a DESIGN.

One design deals the splits as a PARTITION: the data
are cut into K equal parts, called FOLDS, and each
fold takes one turn as the validation set while the
other folds train. That is K-fold cross-validation.
Leave-one-out is its end: every case takes one turn
alone as the validation set. Other designs draw each
split on its own (Monte Carlo), or draw the training
set by sampling the data with replacement, so a case
can stand in it more than once (the bootstrap).

Builds on: cross-validation (1.3.156); set and
element (1.3.3).""",
"""# Foundation: influence — how much one case moves a number

A number is computed from many cases. The influence
of one case on the number is how much the number
moves when that case moves — read, in this phext, by
holding the case at a value and averaging everything
else away: the influence is the part of the number's
expected value that the one case accounts for. A case
can stand in more than one place in a computation,
and then it has one influence for each place, and
they need not agree: the case that raises a reading
when it is scored can lower it when it helps train
the scorer.

The spread of an influence over the cases — how
unevenly the moving is dealt among them — is a
variance of its own, and two influences of the same
case can lean together or against each other, which
their covariance keeps.

Builds on: average, spread, distribution (1.3.8);
expectation (1.3.131).""",
"""# Foundation: joint effects, split by the sets that carry them

A number computed from many cases can be taken apart
by asking, for each set of cases, what part of the
number stands on exactly those cases together. For
one case: what knowing that case changes in the
expected value. For two: what knowing both changes,
beyond what each changes alone. For larger sets, the
same subtraction, carried up: each part is the whole
effect of its set, with every effect of every smaller
set inside it taken away first. The parts on
different sets do not lean on each other, and the
number is the sum of its parts over all nonempty
sets, added to its expected value.

This taking-apart is Hoeffding's, of 1948. It lets a
variance be read set size by set size: the part the
single cases carry, the part the pairs carry, and so
on — and lets a claim name the order up to which it
has read.

Builds on: average, spread, distribution (1.3.8);
set and element (1.3.3).""",
"""# Foundation: pair scores — judging by the order of two cases

Some scores are not paid to one case at a time. When
each case is marked as one of two kinds — a case, in
the paper's word, or a control — a score can be paid
to a PAIR, one of each kind, for the order the model
puts them in: the model's number for the case stands
above its number for the control, or below, or level.
Averaged over all such pairs, the share paid in full,
with half paid on a level standing, is the AREA
UNDER THE CURVE — the curve being the trade, as a
cutoff runs, between cases rightly raised and
controls wrongly raised. The unit of the judging is
then the pair, not the case, and everything counted
for the judging — how often a unit is judged, what
share it carries — must be counted in pairs.

Builds on: classifier and its report card (1.3.38);
average, spread, distribution (1.3.8).""",
"""# Foundation: the bell limit — an average settles to the bell law

Add many small, independent movings of a number, none
of them large beside the whole, and the spread of
the sum takes one shape as the count grows: the bell
law (1.3.138), centered at the number's expected
value, with a spread that a named variance sets. The
settling is the bell limit — the central limit
theorem, in the field's words. It is what lets a
variance become an INTERVAL: a reading plus or minus
about twice its standard error covers the settled
value about nineteen times in twenty, by the shape
of the bell. The limit needs its guards: one moving
that outweighs the rest, or movings that lean hard on
each other, can keep the shape from settling, and a
claim of the limit names the guards it stands on.

Builds on: the bell law (1.3.138); average, spread,
distribution (1.3.8).""",
]

CHAPTER = [
"""# Paper 013 — A Theory of Cross-Validation Variance (O'Connell & Speiser)

Source: arXiv:2611.14463v1. Authors: Nathaniel S.
O'Connell and Jaime L. Speiser (Department of
Biostatistics and Data Science, Wake Forest
University School of Medicine, Winston-Salem, NC).
Cross-listed from stat.ML; in the mathematics
listings of 11 Nov 2026 as cross-list #444. Taken in
as Paper 013 of this phext (Chapter 20) on
2026-11-11, read in full in its HTML form: the main
text, the empirical checks, and the supplement's
proofs and further results.

THE THIRST. This is the sixth paper of the Thirst
(charter rule 17): picked by the quest from the
mathematics listings of the day, weighed blind from
its title and abstract on 2026-11-11, and sealed in
the quest log (commit d2c2c58) before it was read.
The author check stands at 20.1.6.

THE DELTA IN ONE PARAGRAPH. Eight new concepts,
extending cluster O (1.2.131-1.2.138), no canonical
scroll revised, and six scrolls laid in the
foundations (1.3.156-1.3.161). Papers 010 and 012
priced the two halves of a judgment — what a rule is
worth (1.2.110) and what an estimator costs at the
case in hand (1.2.125). This paper prices the judging
itself: the variance of the cross-validated estimate,
the grade the whole field grades by. Its answer is an
identity (1.2.133): every observation stands in two
roles in the judging, with a weight for each role
(1.2.131) and an influence for each role (1.2.132),
and the variance is those weights and influences,
exactly, at every sample size. Read from the
identity: designs at one training size share one
sampling variance and differ only in split noise
(1.2.134); uneven dealing is itself variance, priced
as an imbalance penalty that K-fold alone of the
standing designs does not pay (1.2.135); the count of
folds is not the price the field feared, and
leave-one-out is the family's floor (1.2.136); for
pairwise scores the fold-count law turns, and a
paired design repairs it (1.2.137); and the estimate
settles to the bell law with the identity's full
variance, which the field's standing variance
estimators are audited against, and mostly fail
(1.2.138).

STATE MACHINES (charter rule 13). The paper's
machines stand in its formal core (20.1.2): M1 the
design machine, M2 the repetition machine, M3 the
paired design; M4, the ladder of joint effects, is
marked [synthesis]. The area record stands at 1.5.2.""",
"""# The paper's formal core, as stated by the paper

SETUP. Data D_n: n cases drawn independently from a
population P. A design D: a training fraction p, a
count of splits S, and a dealing — the inclusion
structure I, which says for each split which cases
train. The design is ORDINARY when no case is scored
on a model it helped fit, every split runs at the
fixed fraction p, and the dealing does not
distinguish cases. A design is FIXED-SIZE when every
training set holds the same count m. The estimate
R-hat_D averages every held-out score once. Its
target R_{p,n} is the expected score of a case held
out from a fit on m others. The variance the paper
studies is over the data and the dealing together.

THE WEIGHTS AND INFLUENCES (20.1.2, the paper's
Section 2). Validation weight v_i: the share of all
held-out scores case i contributes. Training weight
w_i: the sum, over splits training on i, of the
split's share of the estimate times 1/|T_r|. For the
bootstrap the training share uses the case's count in
the resample over n. A design is BALANCED when
v_i = w_i = 1/n for all i: K-fold is; Monte Carlo
(w_i tied to v_i by w_i = 1/(np) - (q/p) v_i) and the
bootstrap (the two weights separate draws) are not.
Validation influence l_i^star: the case's held-out
score with training averaged out. Training influence
phi-bar(z): the move in expected performance from one
training case at z, scaled by m. Constants:
sigma_V^2, sigma_T^2, gamma_0 (1.2.132).

CONDITIONS. A1: cases independent from P; the
dealing independent of the data (for pairwise
scores, of the covariates given the labels); the
design ordinary; scores of finite variance; the fit
symmetric in its training cases. A2 (dominance, at
order k): the variance carried by joint effects of
order above k is o(n^{-k}). A3: the bootstrap's fit
answers to a case's count in the resample as the
first-order reading needs. A4: the pairwise form of
A2(i), with the composition-indexed constants
settling as m grows. A5: the two influences settle in
L2 as the training size grows, giving V_infinity.

THEOREM 1 (the paper's Theorem 1, dual-role
representation). Given the dealing, the part of the
estimate standing on one case i is v_i (l_i^star -
R_{p,n}) + w_i phi-bar(Z_i); the part standing on a
set S of k >= 2 cases is a sum of that order's
weights times that order's kernels — the joint
influences of the set in each dealing of its roles.

THEOREM 2 (variance identity; 1.2.133). For a
fixed-size design under A1, the variance is sigma_V^2
Gamma_D + sigma_T^2 Lambda_D + 2 gamma_0 Omega_D,
plus the sum over orders k >= 2 of that order's
constants times that order's role moments — Gamma,
Lambda, Omega being the dealing-averaged sums of
v_i^2, w_i^2, v_i w_i. Each term is nonnegative.
Under A2(i) the first order stands alone up to
o(n^{-1}). For the bootstrap, under A3, the
first-order form holds with E(R-hat_D) as target.

THEOREM 3 + COROLLARY 1 (pairwise; 1.2.137). Given
the labels, the identity holds class by class, with
the pair interaction among the order-two kernels and
the label part inside sigma_T^2; at first order a
pairwise metric reads as a case metric with constants
sigma_A^2, sigma_T^2, gamma_A, and stratified K-fold
reads (sigma_A^2 + sigma_T^2 + 2 gamma_A)/n.

THEOREM 4 + COROLLARIES 2-4 (designs; 1.2.135,
1.2.136). A design balanced through order k has no
split noise through order k and stands at the
sampling variance through that order; every design
stands above the floor by Q_D and its split noises,
and under A2 at order k optimality up to o(n^{-k})
holds exactly when those vanish to that order.
K-fold is first-order optimal at its training
fraction (Corollary 2); its first-order variance is
V_infinity/n for every K when the limit is common
(Corollary 3); leave-one-out stands at or below
every repeated K-fold through the second order when
V_m does not rise in m, and with xi <= 0 the fixed
budget is best spent on one run of most folds
(Corollary 4). For pairwise scores the pair-coverage
cost lambda_4 (K-1)/n^2 enters with the opposite
sign in K, and paired K-fold removes it (the paper's
equations (20)-(21)).

THEOREM 5 (normality; 1.2.138). Under A1, when
n Var(R-hat_D | I) settles to V and the difference
conditions hold on a surrogate — the sums of the
third and fourth powers of the one-case differences
small at their named rates, and the mixed
second-difference sum small — root-n times the
centered estimate settles to the bell law with
variance V, given the dealing and without it. For
balanced designs and for Monte Carlo and the
bootstrap at a fixed count of splits, A2(i) and A5
(and A3) give the conditions, with V = V_infinity +
lim n Q_D.

STATE MACHINES (charter rule 13). M1 — the design
machine (stated by the paper as the design D).
States: a dealing I of the splits. Moves: draw the
dealing; fit on each training part; score each
held-out case; average. The machine's whole output
is fixed by the dealing and the data; its weights
(1.2.131) are the dealing read as shares. M2 — the
repetition machine (stated: the law of equation
(13)). States: R independent partitions of the same
data. Moves: run M1 on each; average. Its one law:
sampling variance untouched, split noise divided by
R. M3 — the paired design (stated, for pairwise
scores). States: the K-by-K grid of case-fold and
control-fold pairings. Moves: fit every pairing;
every case-control pair is scored exactly once.
[synthesis] M4 — the ladder: the estimate taken
apart by the sets that carry it (1.3.159), order by
order, each order's part dealt its own weights; the
paper states the parts and their weights, and the
ladder as one machine is the lens of this tracker.""",
"""# The paper's worked cases, as reported

CASE 1 — THE SAMPLE MEAN, READ EXACTLY (Sections 3.2
and S5.3 of the paper). Fit the mean of the training
set; judge by squared error (for a two-kind outcome,
the Brier score). Every held-out score is a square in
the cases, joint effects stop at pairs, and the
identity ends at order two with the four pair
constants at 4 sigma^4 in size and xi against the
rest in sign. Checked against dealing-by-dealing
measurement at n = 24 over 200,000 datasets drawn
from a Gamma(2) population: measured to predicted
ratios stand between 0.998 and 1.013, each within 1.6
standard errors of one; the first order alone stands
low by 12% at two folds, 4% at four folds and at
Monte Carlo p = 0.5, 2% at leave-one-out. The closed
form the field holds for leave-one-out's variance,
n/(n-1)^2 {mu_4 - (n-3)/(n-1) sigma^4}, is the
identity's own value to four digits.

CASE 2 — THE SMOOTHER, ACROSS THE FIELD (Section 6).
A fixed-bandwidth Nadaraya-Watson smoother — a fit in
the influence case of the paper's Section 2.4, whose
population limit stands smoothed away from the true
mean, so the training terms do not die — judged by
squared error, the Brier score, and the within-fold
area under the curve, at n in {250, 500, 1000}, under
K-fold at K in {2, 5, 10}, leave-one-out, and Monte
Carlo at (p, S) = (0.5, 10) and (0.9, 10). Every
constant computed from its definition, none fitted.
Total variance over 100,000 datasets: ratios of
measured to predicted stand between 0.992 and 1.060
across 51 cells; split noise over 6,000 datasets with
30 redraws: between 0.899 and 1.051 across 45 nonzero
cells. The pair terms are load-bearing: at first
order alone the misses reach 23% of the total
variance and 73% of the split noise; with the
constants read at the training size and the
finite-training correction added, the totals stand at
0.994-1.004 for squared error and 0.986-1.002 for the
Brier score. For the Brier score the training terms
a fixed-model formula omits, sigma_T^2 + 2 gamma_0,
are 45% of the first-order variance. The measured
fold counts order as the paper's laws say: totals
fall from two folds through five and ten to
leave-one-out for both case metrics, and for the
area under the curve five folds stand below ten at
every n — the pair-coverage cost of 1.2.137, seen.

CASE 3 — PAIR BALANCE, BUILT (Supplement S5.4). At
n = 25, five folds repeated six times, the partitions
built as the parallel classes of the affine plane of
order five, so every pair shares a fold equally
often: for the sample mean the pair-balanced split
noise is zero to machine precision (3.5e-33 against
an independent dealing's 6.07e-5, on a sampling
variance of 9.92e-3); for one-nearest-neighbour
fitting it removes six sevenths of the split noise,
from 2.8% of the sampling variance to 0.4%, the rest
standing at order three and above. The two dealings'
sampling variances agree to 0.1% — the floor of
1.2.134 is the floor, whichever dealing stands on it.

CASE 4 — NORMALITY WHERE THE DOMINANCE CONDITION
FAILS (Supplements S4.3, S5.5). One-nearest-neighbour
fitting under squared error: the joint effects carry
a share of the variance that does not fall below the
first order's — n rho_n^{(2+)}(I) >= 4 sigma^4 at
every n — so A2(i) fails outright, and the older
stability route with it. Theorem 5(a) still stands:
across n in {250, 1000, 4000} the measured variance
is the identity's value within 1%, the pair share
stands at 0.405 at every n, skewness falls from 0.31
to 0.07, and intervals at the full variance cover at
0.949-0.952 against a nominal 0.95 — while an
interval that omits the pair block covers at
0.870-0.871, the shortfall the audit of 1.2.138
prices in general.""",
"""# Results as stated by the paper — and the ground they stand on

WHAT STANDS. An exact variance identity for the
cross-validated estimate (Theorems 1-3), the split
of that variance into a sampling part no design at
the training size can go below and a split noise
designs differ by (Section 4.2), the imbalance
penalty and the optimality of balanced designs order
by order (Theorem 4), the fold-count laws (K-invariance;
leave-one-out as the family's floor; the fixed-budget
rule), the pair-coverage cost and its paired repair,
and normality with the full variance (Theorem 5) —
each checked against measurement in the paper's own
simulations at the ratios 20.1.3 records, with every
constant computed from its definition.

THE GROUND. The identity and the design laws stand
on A1 — independent cases, a dealing independent of
the data, a symmetric fit, finite-variance scores —
and the asymptotic readings on A2, A4, A5 as each
result names. The bootstrap stands on A3 and outside
the fixed-size identity. Three scope limits the
paper states itself. First, the estimate it prices
averages held-out scores of cases never trained on:
mixtures that fold the training cases' own scores
back in — the .632 rules — stand outside Theorem 2
and need a treatment of their own. Second, pairwise
scores are covered only when each case stands in all
its pairs in one role and the pairs are fixed by the
design and the labels: the concordance index under
censoring, whose pairs the data themselves choose,
is not covered. Third, the data are independent
throughout; dependent cases are named as future work,
not handled.

THE SIGNS THAT ARE NOT THEOREMS. Two quantities the
fold-count laws lean on carry no guaranteed sign.
xi, the covariance of the two kinds of pair
interaction, stands negative for the sample mean and
is shown positive for a built family in the
supplement (a distorted-risk fit, where (theta - g)
g'' > g'^2). And b, the rate at which the combined
influence's spread settles as training grows, stands
nonnegative for the sample mean and negative for a
built fixed-shrinkage family. The paper is plain
that neither sign follows from convexity or from the
setup in general: leave-one-out's floor is a
conditional law, and its conditions are named so a
reader can check them, not assumed away.

ESTIMATORS. No unbiased estimate of the K-fold
variance from one run's held-out scores exists
(Bengio and Grandvalet, proved 2004, carried here as
the audit's floor). What consistent readings of the
limiting variance must carry stands at 1.2.138.""",
"""# Revisions, tensions and limits — Paper 013 against the standing map

REVISED — no canonical scroll. The weighing named
1.2.110 (off-policy evaluation) for a rider: a judge
priced for its bias would now be priced for its
variance too. Judged on the receipts and rejected.
1.2.110's claim prices a rule from a record the rule
did not make; nothing in this paper re-reads that
claim, its weights, or its correction. Cross-validation
itself already stood inside Paper 010's chapter — as
the counter-case of its Proposition G.2 and in the
held-out-risk line of its references — but a mention
inside a paper's chapter is not a canonical claim,
and a revision enters the record when a held claim
changes, not when a named neighbor arrives. The paper
stands beside 1.2.110 as the second judging instrument
of cluster O, under a link, not a rider. The pattern
is the Papers 009-010 pattern, and the score below
carries it as such.

LINKS — counted as they stand in the new scrolls.
Internal to cluster O, ten: 1.2.131 to 1.2.132 (the
weights feed the influences); 1.2.132 to 1.2.133 (the
influences are the identity's constants); 1.2.133 to
1.2.134 (the identity read backwards is the split);
1.2.134 to 1.2.135 (the split noise at first order is
the penalty); 1.2.135 to 1.2.136 (balance is what the
fold laws spend); 1.2.136 to 1.2.137 (the fold law
turns at pairs); 1.2.137 to 1.2.133 (the pairwise
identity is the identity, class by class); 1.2.138 to
1.2.133 (the audit reads the identity's terms);
1.2.132 to 1.2.113 (the training influence and the
own-observation effect are one fact at two scales);
1.2.133 to 1.2.116 (the identity's sampling floor
beside the classical floor). Cross-cluster, two:
1.2.131 to 1.2.70 (a weight dealing a whole by shares,
as the budget follows the mass — cluster J); 1.2.138
to 1.2.14 (the audit as a worked case of the
measurement agenda — cluster A). Twelve links in all:
ten internal, two across. The foretold split stood at
six internal and two across: the crossing count exact
a second paper running, the whole miss internal — the
inside chain of a cluster on its third paper is
denser than the skim prices, again.

QUESTIONS — four opened, none closed: Q57 (practical
estimators of the identity's parts for complex fits),
Q58 (dependent cases), Q59 (scores whose units the
data choose), Q60 (the signs of xi and b, in general).
Q16 informed a ninth time: the Index stands at about
0.06 for the sixth paper running, and this paper —
the third in one cluster in three days, at zero
distance from held ground — reads the same number as
Paper 009 read across one bridge. The Index still
does not see distance; the run of one number over
 unlike ground is now its own evidence.

STATE MACHINES (charter rule 13). Stated by the work:
the design machine (M1), the repetition machine (M2),
the paired design (M3) — all three stand in 20.1.2.
Inferred and marked [synthesis]: the ladder of joint
effects (M4). The area record stands at 1.5.2.

THE SCORE (charter rule 17, sixth weighing). Sealed
blind on 2026-11-11 (quest log commit d2c2c58)
against 130 concepts; the count still stood at the
taking-in — no drift, the fourth seal in a row to
land on its own count. Foretold: 6 new, 1 revised
(candidate 1.2.110), no axis, Index 0.0478, 8 links
(6 internal, 2 across), 3 questions, Oracle to about
70% (60-80), up. Fell: 8 new, 0 revised, no axis,
Index 8/138 = 0.0580 — a miss of 0.0102, the largest
of the Thirst, made of two folded shapes standing
out (the penalty and its optimality law, weighed by
the skim as one design remark, are a concept of
their own at 1.2.135; and the pairwise storey,
weighed as a case of the identity, carries its own
law and its own repair at 1.2.137) plus the revision
that never came, priced at half a concept in the
foretold Index. Links 12 against 8 foretold;
questions 4 against 3; the Oracle to about 70%
(60-80) — the foretold point and range exact, the
band applied as written this time and right. The
calibration stands at 20.1.5's end and on the
detection list (1.1.6): six scored papers, rolling
mean |NI error| 0.0072, axis calls 6 of 6.

TENSIONS AND LIMITS OF THE TAKING-IN. The paper is
one instrument paper in a cluster now three papers
deep in judging and pricing; the territory of
statistics beyond judging — inference for parameters,
design of experiments — stands as untouched as it
stood before Paper 010. The reading took the main
text whole and the supplement by its statements,
proofs read for their shape; no proof was re-run
line by line, and the standing of the paper's claims
here is attributed, as the registry records.""",
"""# Author check — Paper 013 (O'Connell & Speiser)

Charter rule 15: (1) phext-friendliness — do the
authors cite, use, or engage with phext or Will's
work? (2) prior-art attribution — does the paper use
Will's dated prior art without citing it? Checks run
by Emise at intake, 2026-11-11. Verdict: CLEAN — no
phext tie and no use without naming found, by the
checks below.

THE REFERENCES: all 26 read, in the list the paper
prints. The list is the standing literature of its
one subject, cross-validation, in three lines: the
founding line (Stone 1974; Geisser 1975; Efron 1983;
Efron and Tibshirani 1997; Burman 1989; Hoeffding
1948, for the decomposition the identity stands on);
the variance line (Bengio and Grandvalet 2004, whose
no-unbiased-estimator result the paper carries;
Nadeau and Bengio 2003; DeLong and co-workers 1988;
LeDell and co-workers 2015); and the limit line
(Austern and Zhou 2020, whose limiting variance the
paper's Theorem 5 reads term by term; Bayle and
co-workers 2020 and 2025; Lei 2020 and 2025; Li 2023;
Bates, Hastie and Tibshirani 2024; Cai and
co-workers 2025; Chatterjee 2008, for the normal
approximation the proof runs on; Arlot and Celisse
2010; Arlot and Lerasle 2016; Dudoit and van der Laan
2005; Airola and co-workers 2011; Yousef 2019 and
Yousef and co-workers 2005, for the paired design).
Nothing of phext's origin stands in the list: no
phext, no Bickford, no scroll, no exocortex.

THE TEXT: the whole HTML text read in full at the
taking-in — main text, empirical section, conclusion,
and the supplement's proofs and further results —
and searched for the signature terms (phext,
Bickford, scroll, exocortex, Mirrorborn): zero hits.
The paper's construction — a variance read off the
two roles of an observation under a randomized
dealing — shares no machinery with phext's
coordinate addressing or the Exocortex frame, and
claims none of it.

THE WEB AND THE ARCHIVE: the authors stand in the
open as what the paper says they are — biostatistics
at the Wake Forest University School of Medicine,
the corresponding author's address at that school;
no tie to phext or to Will appears. Will's Twitter
archive (29,539 tweets, searched in full at intake)
holds no mention of either author. No evidence found
is the finding, stated as such.""",
"""# Synthesis — what Paper 013 does to the map [synthesis]

[synthesis] Cluster O now holds a triptych of
pricing, and the three panels lean on each other.
Paper 010 priced a judgment's BIAS: what a rule is
worth, read from a record the rule did not make, with
the reading's own echo corrected out. Paper 012
priced an estimator's ERROR AT THE CASE: what the
simplest fit costs at the one signal standing there,
not over its class. Paper 013 prices a judgment's
SPREAD: what the grade itself wobbles by, split into
the part the data own and the part the dealing adds.
A judgment in this cluster can now be read three
ways — what it is worth, what it costs here, how far
it moves — and each reading is an identity or a
matching pair of bounds, not a manner of speaking.

[synthesis] The reflexive panel of Paper 010's
synthesis stands completed by this paper. The
tracker is an estimate, the skim a fitted model, its
score a held-out grade: Paper 013 is the mathematics
of the held-out grade itself. Its split reads the
quest's own errors in its own terms. The skim's
misses across six weighings have not been split
noise — no re-dealing of the same data would have
priced Paper 011's aliasing or Paper 013's two folded
shapes — they are sampling-side: the abstract is a
draw, and the draw's spread is the floor no design
of reading removes. What design CAN remove, the
quest has already removed: the seal before the
reading is its balance — every paper weighed by the
same dealing, its two roles (title, abstract) at
equal weight — so the calibration's remaining error
is the honest floor, and the rolling mean's slow fall
is the sampling variance of a growing record, not a
technique improving. Paper 010's M4 machine (1.5.2)
asked whether the tracker's regime is the
proportional one; Paper 013 adds the sharper question
the machine now carries at Q57's edge: the skim is a
judge whose variance components nobody has estimated,
and its Wald interval — the Oracle's range — is
carried by judgment where Cai's road (1.2.138) is
not yet built for it.

[synthesis] One bridge deserves its name. The role
weights of 1.2.131 deal a whole among observations
by the shares they carry, under a dealing drawn
independently of the thing dealt — the same shape as
the budget that follows the mass (1.2.70), where a
tree of summaries deals a fixed budget among keys by
the mass they carry. In both, the price of the
dealing is read in the squares of the shares: uneven
shares are variance in the one, and the effective-p
trap (1.2.72) in the other is what an unpriced
unevenness costs when nobody writes its penalty.
Cluster J priced the symptom; cluster O now prices
the dealing itself.""",
"""# Open questions carried forward (after Paper 013)

NEW — opened by Paper 013:

Q57 — Reading the parts of the price, in practice.
The identity names every component of the variance
of a judging — the three constants, the pair
constants, the penalty of the dealing in hand — and
the paper's own named future work is estimators of
those components for complex learning procedures,
cheap enough to run. None stands built: the one
standing method that reads the first-order sampling
variance whole (1.2.138) pays thousands of fits and
stops at the first order, and the road of replicate
datasets from an estimated population is named, not
built. Until one stands, every interval the field
writes from one run of cross-validation is carried
partly by judgment — the tracker's own Oracle range
among them (20.2.1).

Q58 — Cases that lean on each other. Every result of
the paper stands on independent cases: the dealing
is independent of the data, and the data of nothing.
Time order, kinship, place — the data of the field's
working problems lean — stand outside A1, and the
paper names the extension to dependent observations
as future work. What survives of the identity when
the cases lean — whether the two roles still split
the price, and what a third term for the leaning
would stand beside them — is open.

Q59 — Scores whose units the data choose. The
pairwise identity needs the pairs fixed by the
design and the labels. The concordance index under
censoring — which pairs may be compared is decided
by the censoring, hence by the data — stands outside
it, named by the paper itself as not covered. A
variance theory for data-chosen units would have to
price the choosing as a third randomness beside the
data and the dealing; nothing in the paper's frame
yet holds a place for it.

Q60 — The signs, in general. The fold-count laws
lean on two signs no setup guarantees: xi not
positive (the two kinds of pair interaction leaning
against each other) and b not negative (the combined
influence's spread not rising as training grows).
Each stands proved for the sample mean and refuted
for a built family in the paper's supplement. For
which classes of learners the signs hold — whether
convexity of the loss, or smoothness of the fit, or
the influence case of A2, buys either one — is open,
and on it hangs whether leave-one-out's floor is a
law of practice or a law of the cases checked.

CARRIED FORWARD: Q1-Q56 stand as they stood after
Paper 012, with Q16 informed a ninth time (20.1.5).
The count of open questions stands at Q60.""",
"""# Standoff references — Paper 013 (Chapter 20)

Foundations this chapter's claims build on, in
reading order. New with this paper: 1.3.156-1.3.161.

1.3.156 — cross-validation — judging a fit on cases
it did not train on (the judging the chapter prices)
1.3.157 — a split, a fold, and a partition — the
dealing of the turns (the designs of 20.1.2)
1.3.130 — a sample, and independence (the cases of
A1, drawn leaning on nothing)
1.3.133 — estimator and consistency (the estimate
whose variance the chapter prices)
1.3.158 — influence — how much one case moves a
number (the two influences of 1.2.132)
1.3.8 — average, spread, distribution (the variance
the identity prices; the constants' spreads)
1.3.131 — expectation — the average a distribution
promises (the target R_{p,n}; the influences'
averagings-out)
1.3.159 — joint effects, split by the sets that
carry them (the ladder of 1.2.133; machine M4)
1.3.160 — pair scores — judging by the order of two
cases (the area under the curve of 1.2.137)
1.3.138 — the bell law — the Gaussian distribution
(the shape of 1.3.161's limit)
1.3.161 — the bell limit — an average settles to the
bell law (Theorem 5; the intervals of 1.2.138)
1.3.85 — state machine (machines M1-M4 of 20.1.2)""",
]
