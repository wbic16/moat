#!/usr/bin/env python3
"""Protocol scorer — Paper 021 (protocol sample 2 of 12, stratum cron 1 of 5).

Scores the sealed BEFORE record for Paper 021 (arXiv:2611.16759) against
the filed actuals, under evaluation-preregistration.md (ratified
2026-11-14) sections 2-4. All arithmetic is done here; no score anywhere
is hand-computed.

Filed actuals (headline filing, Chapter 32 of research.phext):
  10 new concepts (1.2.260-1.2.269, cluster Z founded), 0 revised,
  axis actual 0 (judged in writing at filing, before this script ran),
  links 15 internal / 4 cross (internal = among the ten new concepts;
  the founding cluster holds no held concepts to link to).
Sensitivity filing (the one rule-permitted fold recorded in the AFTER
record): fold the test at the pre-interpolant (1.2.268) into test-free
PDL (1.2.261): 9 new concepts, links 14 internal / 4 cross.
A second recorded alternative runs the other way (a split, not a
fold): semilinearity split out of execution lengths (1.2.264) gives
11 new concepts; it is reported in the note, not as the sensitivity
headline, because the protocol's sensitivity line is defined on the
filing's permitted folds.

Nulls (protocol section 4), scored on this same paper by this same
script, over the thirteen previously scored papers (008-020):
  N1: flat NI 0.05, axis probability 0.05; concept count implied.
  N2: expanding mean of past actuals — for sample paper 2 this is the
      mean over Papers 008-020 actuals (the retrospective record plus
      sample paper 1), the protocol's seeds being that mean's value
      at the sample's opening (NI 0.064, count 9.8 declared).
  N3: same-cluster past mean. Paper 021 founds cluster Z; no scored
      past paper sits in cluster Z, so N3 falls back to the global
      expanding mean, per protocol.
The Oracle enters NO score (protocol section 2). The band step on the
actuals is computed at the end for the ledger entry only, labelled.
"""
import json

HERE = "/home/hatch/workspace/thirst-quest"

RAW = open(f"{HERE}/predictions.jsonl").read()
dec = json.JSONDecoder(); recs = []; i = 0
while i < len(RAW):
    while i < len(RAW) and RAW[i] in " \t\r\n":
        i += 1
    if i >= len(RAW):
        break
    o, j = dec.raw_decode(RAW, i); recs.append(o); i = j

before = next(r for r in recs if str(r.get("paper")) == "021"
              and r.get("phase") == "BEFORE")
pred_list = [r for r in recs if "pred_new" in r and "actual_new" not in r
             and str(r.get("paper")) != "021"]
scores = [r for r in recs if "actual_new" in r]
assert len(scores) == 13 and len(pred_list) == 13, (len(scores), len(pred_list))
PAIRED = list(zip(pred_list, scores))

CLUSTER = {"008": "E", "009": "N", "010": "O", "011": "P", "012": "O",
           "013": "O", "014": "Q", "015": "R", "016": "T", "017": "W",
           "018": "O", "019": "Y", "020": "S"}
THIS_CLUSTER = "Z"

def ni(new, revised, cb):
    return (new + 0.5 * revised) / (cb + new)

cb = before["concepts_before"]                       # 259
sealed_ni = before["pred_ni"]                         # 0.0263
sealed_ni_iv = before["pred_ni_interval_80"]          # [0.015, 0.037]
sealed_new = before["pred_new"]                       # 7
sealed_new_iv = before["pred_new_interval_80"]        # [4, 10]
sealed_rev = before["pred_revised"]                   # 0
sealed_axis_p = before["pred_axis_prob"]              # 0.15
sealed_lin = before["pred_links_internal"]            # 8
sealed_lx = before["pred_links_cross_cluster"]        # 4

ACT = dict(new=10, revised=0, axis=0, links_in=15, links_cross=4,
           questions_opened=2, questions_closed=0)
ALT = dict(new=9, revised=0, axis=0, links_in=14, links_cross=4)
SPLIT_NEW = 11

def score(filing):
    a_ni = ni(filing["new"], filing["revised"], cb)
    return dict(
        actual_ni=round(a_ni, 4),
        ni_abs_error=round(abs(a_ni - sealed_ni), 4),
        ni_interval_covered=sealed_ni_iv[0] <= a_ni <= sealed_ni_iv[1],
        new_signed_error=filing["new"] - sealed_new,
        new_abs_error=abs(filing["new"] - sealed_new),
        new_interval_covered=sealed_new_iv[0] <= filing["new"] <= sealed_new_iv[1],
        revised_hit=filing["revised"] == sealed_rev,
        axis_brier=round((sealed_axis_p - filing["axis"]) ** 2, 4),
        links_in_error=filing["links_in"] - sealed_lin,
        links_cross_error=filing["links_cross"] - sealed_lx,
    )

headline = score(ACT)
sensitivity = score(ALT)
split_ni = ni(SPLIT_NEW, 0, cb)
split_line = dict(actual_ni=round(split_ni, 4),
                  ni_abs_error=round(abs(split_ni - sealed_ni), 4),
                  ni_interval_covered=sealed_ni_iv[0] <= split_ni <= sealed_ni_iv[1],
                  new_signed_error=SPLIT_NEW - sealed_new,
                  new_abs_error=abs(SPLIT_NEW - sealed_new),
                  new_interval_covered=sealed_new_iv[0] <= SPLIT_NEW <= sealed_new_iv[1])

a_ni = ni(ACT["new"], ACT["revised"], cb)

def cb_of(pr, sc):
    return sc.get("concepts_before_sealed", pr.get("concepts_before"))

past_ni = [ni(sc["actual_new"], sc["actual_revised"], cb_of(pr, sc))
           for pr, sc in PAIRED]
past_new = [sc["actual_new"] for _, sc in PAIRED]
past_axis = [1 if sc.get("actual_axis", sc.get("axis_opened")) else 0
             for _, sc in PAIRED]
exp_ni = sum(past_ni) / len(past_ni)
exp_new = sum(past_new) / len(past_new)
exp_axis_p = sum(past_axis) / len(past_axis)
same = [k for k, (_, sc) in enumerate(PAIRED)
        if CLUSTER.get(str(sc.get("paper"))) == THIS_CLUSTER]

n1_new = 0.05 * cb / 0.95
nulls = dict(
    N1=dict(ni=0.05, ni_abs_error=round(abs(0.05 - a_ni), 4),
            new=round(n1_new, 2), new_abs_error=round(abs(n1_new - ACT["new"]), 4),
            axis_p=0.05, axis_brier=round((0.05 - ACT["axis"]) ** 2, 4)),
    N2=dict(ni=round(exp_ni, 4), ni_abs_error=round(abs(exp_ni - a_ni), 4),
            new=round(exp_new, 2), new_abs_error=round(abs(exp_new - ACT["new"]), 4),
            axis_p=round(exp_axis_p, 4),
            axis_brier=round((exp_axis_p - ACT["axis"]) ** 2, 4),
            basis="expanding mean of past actuals (Papers 008-020) "
                  "computed from the log; the protocol's declared seeds "
                  "(NI 0.064, count 9.8) are this mean's value over "
                  "Papers 008-019 at the sample's opening"),
    N3=dict(ni=round(exp_ni, 4) if not same else None,
            new=round(exp_new, 2) if not same else None,
            src=("same-cluster (Z) past mean" if same else
                 "fallback-global: no scored past paper sits in "
                 "cluster Z (founded by this paper), so the global "
                 "expanding mean stands"),
            basis="expanding mean of past actuals computed from the log"),
)
if not same:
    nulls["N3"].update(
        ni_abs_error=round(abs(exp_ni - a_ni), 4),
        new_abs_error=round(abs(exp_new - ACT["new"]), 4),
        axis_p=round(exp_axis_p, 4),
        axis_brier=round((exp_axis_p - ACT["axis"]) ** 2, 4))

seed_check = dict(
    expanding_mean_ni_p008_p020=round(exp_ni, 4),
    expanding_mean_count_p008_p020=round(exp_new, 4),
    past_axis_openings=f"{sum(past_axis)} of {len(past_axis)}",
)

past_errs = []
for pr, sc in PAIRED:
    c = cb_of(pr, sc)
    p_ni = ni(pr["pred_new"], pr["pred_revised"], c)
    past_errs.append(abs(p_ni - ni(sc["actual_new"], sc["actual_revised"], c)))
window = (past_errs + [headline["ni_abs_error"]])[-10:]
rolling10 = round(sum(window) / len(window), 4)

def band_step(ni_v, axis):
    if axis:
        return -5
    if ni_v > 0.50:
        return 0
    if ni_v >= 0.20:
        return 5
    return 10

step = band_step(a_ni, ACT["axis"])
ledger = dict(prior=100, band_step_on_actuals=step,
              after=max(0, min(100, 100 + step)), range=[90, 100],
              note="LEDGER BOOKKEEPING ONLY under the ratified protocol: "
                   "the band rule applied to the filed actuals; the Oracle "
                   "enters no score and no criterion.")

out = dict(paper="021", sample="2 of 12", stratum="cron (1 of 5)",
           cluster_filed="Z founded", concepts_before=cb,
           sealed=dict(ni=sealed_ni, ni_interval_80=sealed_ni_iv,
                       new=sealed_new, new_interval_80=sealed_new_iv,
                       revised=sealed_rev, axis_prob=sealed_axis_p,
                       links_internal=sealed_lin, links_cross=sealed_lx),
           headline=headline, sensitivity_fold=sensitivity,
           sensitivity_split_note=split_line,
           nulls=nulls, seed_check=seed_check,
           rolling10_abs_ni_error_after_p021=rolling10,
           ledger_bookkeeping=ledger)
json.dump(out, open(f"{HERE}/score_p021_output.json", "w"), indent=1)
print(json.dumps(out, indent=1))
