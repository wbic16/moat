#!/usr/bin/env python3
"""Protocol scorer — Paper 020 (protocol sample 1 of 12, stratum Will-posted).

Scores the sealed BEFORE record for Paper 020 (arXiv:2611.14552) against the
filed actuals, under evaluation-preregistration.md (ratified 2026-11-14)
sections 2-4. All arithmetic is done here; no score anywhere is hand-computed.

Filed actuals (headline filing, Chapter 31 of research.phext):
  12 new concepts (1.2.248-1.2.259, cluster S extended), 0 revised,
  axis actual 0 (judged in writing at filing, before this script ran),
  links 20 internal / 3 cross (internal = among the twelve new concepts
  and to held concepts of cluster S, the cluster they extend).
Sensitivity filing (the four rule-permitted folds recorded in the AFTER
record, all taken at once): 8 new concepts, links 16 internal / 3 cross.
Each single fold on its own gives 11 new concepts.

Nulls (protocol section 4), scored on this same paper by this same script:
  N1: flat NI 0.05, axis probability 0.05; its concept count is the count
      implied by NI 0.05 at concepts_before (evaluation_analysis.py
      convention: n = 0.05*cb/0.95, revised 0).
  N2: the protocol's declared seeds — NI 0.064, count 9.8 (first sample
      paper, so N2 is the seeds). Axis probability: the expanding mean of
      past actual axis values, the evaluation script's N2 convention
      carried to probabilities; computed from the log below.
  N3: same-cluster past mean. Paper 020 files in cluster S; no scored
      retrospective paper sits in cluster S, so N3 falls back to the
      global expanding mean (computed from the log), per protocol.
The Oracle enters NO score (protocol section 2). The band step on the
actuals is computed at the end for the ledger entry only, labelled as such.
"""
import json

HERE = "/home/hatch/workspace/thirst-quest"

# ---------- load the quest log ----------
RAW = open(f"{HERE}/predictions.jsonl").read()
dec = json.JSONDecoder(); recs = []; i = 0
while i < len(RAW):
    while i < len(RAW) and RAW[i] in " \t\r\n":
        i += 1
    if i >= len(RAW):
        break
    o, j = dec.raw_decode(RAW, i); recs.append(o); i = j

before = next(r for r in recs if str(r.get("paper")) == "020"
              and r.get("phase") == "BEFORE")
pred_list = [r for r in recs if "pred_new" in r and "actual_new" not in r
             and str(r.get("paper")) != "020"]
scores = [r for r in recs if "actual_new" in r]
assert len(scores) == 12 and len(pred_list) == 12, (len(scores), len(pred_list))
PAIRED = list(zip(pred_list, scores))  # arrival order, as evaluation_analysis.py

def cb_of(pr, sc):
    return sc.get("concepts_before_sealed", pr.get("concepts_before"))

CLUSTER = {"008": "E", "009": "N", "010": "O", "011": "P", "012": "O",
           "013": "O", "014": "Q", "015": "R", "016": "T", "017": "W",
           "018": "O", "019": "Y"}
THIS_CLUSTER = "S"

def ni(new, revised, cb):
    return (new + 0.5 * revised) / (cb + new)

# ---------- the seal ----------
cb = before["concepts_before"]                       # 247
sealed_ni = before["pred_ni"]                         # 0.0276
sealed_ni_iv = before["pred_ni_interval_80"]          # [0.016, 0.043]
sealed_new = before["pred_new"]                       # 7
sealed_new_iv = before["pred_new_interval_80"]        # [4, 11]
sealed_rev = before["pred_revised"]                   # 0
sealed_axis_p = before["pred_axis_prob"]              # 0.10
sealed_lin = before["pred_links_internal"]            # 9
sealed_lx = before["pred_links_cross_cluster"]        # 3

# ---------- the filing ----------
ACT = dict(new=12, revised=0, axis=0, links_in=20, links_cross=3,
           questions_opened=2, questions_closed=0)
ALT = dict(new=8, revised=0, axis=0, links_in=16, links_cross=3)
SINGLE_FOLD_NEW = 11

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
single_fold_ni = ni(SINGLE_FOLD_NEW, 0, cb)
single_fold = dict(actual_ni=round(single_fold_ni, 4),
                   ni_abs_error=round(abs(single_fold_ni - sealed_ni), 4),
                   ni_interval_covered=sealed_ni_iv[0] <= single_fold_ni <= sealed_ni_iv[1],
                   new_signed_error=SINGLE_FOLD_NEW - sealed_new,
                   new_abs_error=abs(SINGLE_FOLD_NEW - sealed_new),
                   new_interval_covered=sealed_new_iv[0] <= SINGLE_FOLD_NEW <= sealed_new_iv[1])

# ---------- nulls on this paper ----------
a_ni = ni(ACT["new"], ACT["revised"], cb)
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
    N2=dict(ni=0.064, ni_abs_error=round(abs(0.064 - a_ni), 4),
            new=9.8, new_abs_error=round(abs(9.8 - ACT["new"]), 4),
            axis_p=round(exp_axis_p, 4),
            axis_brier=round((exp_axis_p - ACT["axis"]) ** 2, 4),
            basis="protocol seeds (NI 0.064, count 9.8); axis p = expanding "
                  "mean of past actual axis values from the log"),
    N3=dict(ni=round(exp_ni, 4) if not same else None,
            new=round(exp_new, 2) if not same else None,
            src=("same-cluster (S) past mean" if same else
                 "fallback-global: no scored retrospective paper sits in "
                 "cluster S, so the global expanding mean stands"),
            basis="expanding mean of past actuals computed from the log"),
)
if not same:
    nulls["N3"].update(
        ni_abs_error=round(abs(exp_ni - a_ni), 4),
        new_abs_error=round(abs(exp_new - ACT["new"]), 4),
        axis_p=round(exp_axis_p, 4),
        axis_brier=round((exp_axis_p - ACT["axis"]) ** 2, 4))

seed_check = dict(
    recomputed_expanding_mean_ni_p008_p019=round(exp_ni, 4),
    protocol_declared_ni_seed=0.064,
    recomputed_expanding_mean_count=round(exp_new, 4),
    protocol_declared_count_seed=9.8,
    past_axis_openings=f"{sum(past_axis)} of {len(past_axis)}",
)

# ---------- rolling-10 |NI error| including Paper 020 ----------
past_errs = []
for pr, sc in PAIRED:
    c = cb_of(pr, sc)
    p_ni = ni(pr["pred_new"], pr["pred_revised"], c)
    past_errs.append(abs(p_ni - ni(sc["actual_new"], sc["actual_revised"], c)))
window = (past_errs + [headline["ni_abs_error"]])[-10:]
rolling10 = round(sum(window) / len(window), 4)

# ---------- ledger bookkeeping only (NOT a score) ----------
def band_step(ni_v, axis):
    if axis:
        return -5
    if ni_v > 0.50:
        return 0
    if ni_v >= 0.20:
        return 5
    return 10

prior_oracle = before["pred_oracle_after_pct"]  # seal recorded hold at 100
step = band_step(a_ni, ACT["axis"])
ledger_after = max(0, min(100, 100 + step))
ledger = dict(prior=100, band_step_on_actuals=step,
              after=ledger_after, range=[90, 100],
              note="LEDGER BOOKKEEPING ONLY under the ratified protocol: "
                   "the band rule applied to the filed actuals; the Oracle "
                   "enters no score and no criterion.")

out = dict(paper="020", sample="1 of 12", stratum="Will-posted (1 of 4)",
           cluster_filed="S extended", concepts_before=cb,
           sealed=dict(ni=sealed_ni, ni_interval_80=sealed_ni_iv,
                       new=sealed_new, new_interval_80=sealed_new_iv,
                       revised=sealed_rev, axis_prob=sealed_axis_p,
                       links_internal=sealed_lin, links_cross=sealed_lx),
           headline=headline, sensitivity_all_folds=sensitivity,
           sensitivity_single_fold=single_fold,
           nulls=nulls, seed_check=seed_check,
           rolling10_abs_ni_error_after_p020=rolling10,
           ledger_bookkeeping=ledger)
json.dump(out, open(f"{HERE}/score_p020_output.json", "w"), indent=1)
print(json.dumps(out, indent=1))
