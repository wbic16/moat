#!/usr/bin/env python3
"""MOAT calibration audit — Legs A+B. Recomputes every number from
~/workspace/thirst-quest/predictions.jsonl (primary record).
Conventions:
- NI(pred, basis)  = (pred_new + 0.5*pred_revised) / (cb_basis + pred_new)
- NI(actual, basis)= (actual_new + 0.5*actual_revised) / (cb_basis + actual_new)
  basis 'sealed' uses concepts_before at seal time; 'absorption' uses the
  count at taking-in. Headline basis: sealed (the skim is what is tested).
- Band rule (charter, research.phext 1.1.4): axis -> hold or fall ~5;
  NI>0.50 -> hold/fall; NI 0.20-0.50 no axis -> +~5; NI<0.20 no axis -> +~10.
- Null Oracle convention: point = clip(prev actual OP + step, 0, 100);
  range = [point-10, point+10] clipped to [0,100] (the streak-era habit).
"""
import json, re, statistics as st

RAW = open('predictions.jsonl').read()
dec = json.JSONDecoder(); recs = []; i = 0
while i < len(RAW):
    while i < len(RAW) and RAW[i] in ' \t\r\n': i += 1
    if i >= len(RAW): break
    o, j = dec.raw_decode(RAW, i); recs.append(o); i = j

def rng(v):
    if v is None: return None
    if isinstance(v, list): return (int(v[0]), int(v[1]))
    m = re.match(r'\s*(\d+)\s*-\s*(\d+)\s*$', str(v))
    return (int(m.group(1)), int(m.group(2))) if m else None

def links_total(r, side, other=None):
    if side == 'pred':
        for src in (r, r.get('impact') or {}, other or {}):
            if src.get('pred_links_total') is not None: return int(src['pred_links_total'])
            if src.get('pred_new_links') is not None: return int(src['pred_new_links'])
            if src.get('pred_links_in') is not None: return int(src['pred_links_in']) + int(src.get('pred_links_cross') or 0)
    else:
        for src in (r, other or {}):
            if src.get('actual_links_total') is not None: return int(src['actual_links_total'])
            if src.get('actual_new_links') is not None: return int(src['actual_new_links'])
            if src.get('actual_links_in') is not None: return int(src['actual_links_in']) + int(src.get('actual_links_cross') or 0)
    return None

def op_pred_of(pr, sc):
    for src in (pr, pr.get('impact') or {}, sc):
        v = src.get('pred_oracle_after_pct', src.get('pred_oracle'))
        if v is not None: return int(v)
    return None
def op_range_pred_of(pr, sc):
    for src in (pr, pr.get('impact') or {}, sc):
        v = src.get('pred_oracle_range')
        if v is not None: return rng(v)
    return None

def links_split(s):
    if not s: return None
    m = re.search(r'(\d+)\s*internal.*?(\d+)\s*cross', str(s))
    return (int(m.group(1)), int(m.group(2))) if m else None

PAPERS = ['008','009','010','011','012','013','014','015','016','017','018','019']
ARXIV = {'008':'2611.09694','009':'2611.08625','010':'2611.08794','011':'2611.07088',
         '012':'2611.11959','013':'2611.14463','014':'2510.01346','015':'2611.14039',
         '016':'1903.06830','017':None,'018':'2611.17082','019':'2611.14543'}
CRON = {'008','012','013','018'}   # arXiv-listing picks; all others Will-posted
CLUSTER = {'008':'E','009':'N','010':'O','011':'P','012':'O','013':'O','014':'Q',
           '015':'R','016':'T','017':'W','018':'O','019':'Y'}  # P011 = cluster P (its axis note)

pred_list = [r for r in recs if 'pred_new' in r and 'actual_new' not in r]
score_list = [r for r in recs if 'actual_new' in r]
assert len(pred_list) == 12 and len(score_list) == 12, (len(pred_list), len(score_list))
preds = dict(zip(PAPERS, pred_list)); scores = dict(zip(PAPERS, score_list))
# consistency: where a record names its arXiv id, it must match the slot
for p in PAPERS:
    for r in (preds[p], scores[p]):
        for cand in (r.get('arxiv_id'), r.get('for'), str(r.get('paper') or '')):
            if ARXIV[p] and cand == ARXIV[p]: break
        else:
            if p != '017':
                print('WARN pairing check:', p, str(r.get('title') or r.get('paper'))[:60])

rows = []
prev_op = 35  # ledger: OP after Paper 007 ~35 (range 25-45)
for p in PAPERS:
    pr, sc = preds[p], scores[p]
    cb_s = sc.get('concepts_before_sealed', pr.get('concepts_before'))
    cb_a = sc.get('concepts_before_absorption', cb_s)
    pn = pr['pred_new']; prr = pr['pred_revised']; pa = bool(pr['pred_axis'])
    an = sc['actual_new']; ar = sc['actual_revised']; aa = bool(sc.get('actual_axis', sc.get('axis_opened')))
    ni_p_s = (pn + 0.5*prr) / (cb_s + pn)
    ni_a_s = (an + 0.5*ar) / (cb_s + an)
    ni_p_a = (pn + 0.5*prr) / (cb_a + pn)
    ni_a_a = (an + 0.5*ar) / (cb_a + an)
    op_pred = op_pred_of(pr, sc)
    op_act = sc.get('actual_oracle_after_pct', sc.get('actual_oracle'))
    if op_act is not None: op_act = int(op_act)
    rg_pred = op_range_pred_of(pr, sc)
    rg_act = rng(sc.get('actual_oracle_range'))
    lt_p = links_total(pr,'pred', sc); lt_a = links_total(sc,'act')
    row = dict(paper=p, cron=(p in CRON), cb_sealed=cb_s, cb_abs=cb_a,
        pred_new=pn, act_new=an, new_err=an-pn,
        pred_rev=prr, act_rev=ar, rev_counthit=(prr==ar),
        pred_axis=pa, act_axis=aa, axis_hit=(pa==aa),
        ni_pred_sealed=ni_p_s, ni_act_sealed=ni_a_s, ni_err_sealed=abs(ni_p_s-ni_a_s),
        ni_pred_abs=ni_p_a, ni_act_abs=ni_a_a, ni_err_abs=abs(ni_p_a-ni_a_a),
        ni_recorded_err=(sc.get('ni_abs_error') or sc.get('ni_error') or sc.get('ni_error_sealed_basis')),
        op_before=prev_op, op_pred=op_pred, op_act=op_act,
        op_range_pred=rg_pred, op_range_act=rg_act,
        point_exact=(op_pred==op_act), range_exact=(rg_pred==rg_act),
        links_pred=lt_p, links_act=lt_a,
        links_pred_split=(pr.get('pred_links_internal'), pr.get('pred_links_cross_cluster')) if pr.get('pred_links_internal') is not None else links_split(pr.get('pred_links_split')),
        links_act_split=(sc.get('actual_links_in'), sc.get('actual_links_cross')) if sc.get('actual_links_in') is not None else links_split(sc.get('actual_links_split')),
        cluster=CLUSTER[p] or sc.get('cluster'),
        recorded_pred_ni=(pr.get('pred_ni') or pr.get('pred_NI')),
        recorded_act_ni=(sc.get('actual_ni') or sc.get('ni_actual') or sc.get('ni_actual_sealed_basis')),
    )
    rows.append(row)
    prev_op = op_act

def band(ni, axis):
    if axis: return 'axis'
    if ni > 0.50: return 'gt50'
    if ni >= 0.20: return 'mid'
    return 'low'
def step(ni, axis, axis_step=-5):
    b = band(ni, axis)
    return {'low':10, 'mid':5, 'axis':axis_step, 'gt50':0}[b]

# ---- band sensitivity (suspicion 1) ----
for r in rows:
    err = r['ni_err_sealed']
    same_band = band(r['ni_pred_sealed'], r['pred_axis']) == band(r['ni_act_sealed'], r['act_axis'])
    # adverse move: actual NI pushed away from predicted NI toward the 0.20 edge
    def survives(k):
        moved = r['ni_pred_sealed'] + (r['ni_act_sealed']-r['ni_pred_sealed'])*k if err>0 else r['ni_act_sealed']
        if r['ni_act_sealed'] < r['ni_pred_sealed']:  # adverse = downward only matters at 0.50 edge; low band floor is 0
            moved = r['ni_pred_sealed'] - err*k
        return band(moved, r['act_axis']) == band(r['ni_pred_sealed'], r['pred_axis'])
    r['same_band'] = same_band
    r['band_headroom'] = (0.20 - r['ni_act_sealed']) if band(r['ni_act_sealed'], r['act_axis'])=='low' else None
    r['headroom_x'] = (r['band_headroom']/err) if (r['band_headroom'] is not None and err>0) else (float('inf') if r['band_headroom'] else None)
    r['survives_2x'] = survives(2); r['survives_5x'] = survives(5)

# ---- null models ----
def null_oracle(op_before, ni, axis):
    pt = max(0, min(100, op_before + step(ni, axis)))
    return pt, (max(0, pt-10), min(100, pt+10))
past = []
for r in rows:
    # N1: flat NI 0.05, no axis; implied new solves 0.05 = n/(cb+n), revised 0
    n1_new = 0.05*r['cb_sealed']/0.95
    n1_pt, n1_rg = null_oracle(r['op_before'], 0.05, False)
    r['n1'] = dict(ni_err=abs(0.05-r['ni_act_sealed']), new_err=abs(n1_new-r['act_new']),
                   axis_hit=(False==r['act_axis']), point=n1_pt, range=n1_rg,
                   point_exact=(n1_pt==r['op_act']), full_exact=(n1_pt==r['op_act'] and n1_rg==r['op_range_act']))
    # N2: expanding mean of past actuals (sealed basis)
    if past:
        m_ni = st.mean(x['ni_act_sealed'] for x in past)
        m_new = st.mean(x['act_new'] for x in past)
        axes = [x['act_axis'] for x in past]
        m_ax = (sum(axes) > len(axes)/2)
        n2_pt, n2_rg = null_oracle(r['op_before'], m_ni, m_ax)
        r['n2'] = dict(ni=m_ni, ni_err=abs(m_ni-r['ni_act_sealed']), new_err=abs(m_new-r['act_new']),
                       axis_hit=(m_ax==r['act_axis']), point=n2_pt, range=n2_rg,
                       point_exact=(n2_pt==r['op_act']), full_exact=(n2_pt==r['op_act'] and n2_rg==r['op_range_act']))
    else: r['n2'] = None
    # N3: same-cluster past mean, else N2 fallback
    same = [x for x in past if x['cluster'] and r['cluster'] and x['cluster']==r['cluster']]
    if same:
        m_ni = st.mean(x['ni_act_sealed'] for x in same); m_new = st.mean(x['act_new'] for x in same)
        m_ax = (sum(x['act_axis'] for x in same) > len(same)/2)
        src = 'cluster '+r['cluster']
    elif past:
        m_ni = st.mean(x['ni_act_sealed'] for x in past); m_new = st.mean(x['act_new'] for x in past)
        m_ax = (sum(x['act_axis'] for x in past) > len(past)/2); src = 'fallback-global'
    else:
        m_ni = None; src = 'undefined'
    if m_ni is not None:
        n3_pt, n3_rg = null_oracle(r['op_before'], m_ni, m_ax)
        r['n3'] = dict(ni=m_ni, ni_err=abs(m_ni-r['ni_act_sealed']), new_err=abs(m_new-r['act_new']),
                       axis_hit=(m_ax==r['act_axis']), point=n3_pt, range=n3_rg, src=src,
                       point_exact=(n3_pt==r['op_act']), full_exact=(n3_pt==r['op_act'] and n3_rg==r['op_range_act']))
    else: r['n3'] = None
    past.append(r)

# ---- self-grading sensitivity: documented fold alternatives ----
# k = concepts the AFTER record itself names as split out / folded differently.
FOLD = {'008':1,'011':1,'012':1,'015':4,'017':6,'018':1,'019':2}
for r in rows:
    k = FOLD.get(r['paper'], 0)
    an2 = r['act_new'] - k
    ni2 = (an2 + 0.5*r['act_rev']) / (r['cb_sealed'] + an2)
    r['fold_k'] = k; r['alt_new'] = an2; r['alt_new_err'] = abs(an2 - r['pred_new'])
    r['alt_ni_err'] = abs(r['ni_pred_sealed'] - ni2)

def agg(rs, key):
    return st.mean(r[key] for r in rs)
out = dict(rows=rows)
def summary(rs, label):
    d = dict(label=label, n=len(rs),
        skim_ni_err=agg(rs,'ni_err_sealed'), skim_ni_err_abs=agg(rs,'ni_err_abs'),
        skim_new_mae=st.mean(abs(r['new_err']) for r in rs),
        skim_axis=sum(r['axis_hit'] for r in rs),
        skim_point_exact=sum(r['point_exact'] for r in rs),
        skim_full_exact=sum(r['point_exact'] and r['range_exact'] for r in rs),
        n1_ni_err=agg(rs,'n1') if False else st.mean(r['n1']['ni_err'] for r in rs),
        n1_new_mae=st.mean(r['n1']['new_err'] for r in rs),
        n1_axis=sum(r['n1']['axis_hit'] for r in rs),
        n1_point_exact=sum(r['n1']['point_exact'] for r in rs),
        n1_full_exact=sum(r['n1']['full_exact'] for r in rs))
    n2 = [r for r in rs if r['n2']]
    if n2:
        d.update(n2_n=len(n2), n2_ni_err=st.mean(r['n2']['ni_err'] for r in n2),
                 n2_new_mae=st.mean(r['n2']['new_err'] for r in n2),
                 n2_axis=sum(r['n2']['axis_hit'] for r in n2),
                 n2_point_exact=sum(r['n2']['point_exact'] for r in n2),
                 n2_full_exact=sum(r['n2']['full_exact'] for r in n2))
    n3 = [r for r in rs if r['n3']]
    if n3:
        d.update(n3_n=len(n3), n3_ni_err=st.mean(r['n3']['ni_err'] for r in n3),
                 n3_new_mae=st.mean(r['n3']['new_err'] for r in n3),
                 n3_axis=sum(r['n3']['axis_hit'] for r in n3),
                 n3_point_exact=sum(r['n3']['point_exact'] for r in n3),
                 n3_full_exact=sum(r['n3']['full_exact'] for r in n3))
    return d
out['all'] = summary(rows, 'all 12')
out['cron'] = summary([r for r in rows if r['cron']], 'cron picks')
out['will'] = summary([r for r in rows if not r['cron']], 'Will-posted')
out['streak'] = summary([r for r in rows if r['paper'] in ('013','014','015','016','017','018','019')], 'streak P013-019')
out['fold_alt'] = dict(
    skim_new_mae_as_filed=st.mean(abs(r['new_err']) for r in rows),
    skim_new_mae_fold_alt=st.mean(r['alt_new_err'] for r in rows),
    skim_ni_err_as_filed=agg(rows,'ni_err_sealed'),
    skim_ni_err_fold_alt=st.mean(r['alt_ni_err'] for r in rows))
# revision record
out['revisions'] = dict(
    foretold_positive=sum(1 for r in rows if r['pred_rev'] > 0),
    foretold_positive_landed=sum(1 for r in rows if r['pred_rev'] > 0 and r['act_rev'] > 0),
    phantoms=[r['paper'] for r in rows if r['pred_rev'] > 0 and r['act_rev'] == 0],
    foretold_zero=sum(1 for r in rows if r['pred_rev'] == 0),
    foretold_zero_landed=sum(1 for r in rows if r['pred_rev'] == 0 and r['act_rev'] == 0),
    count_hits=sum(r['rev_counthit'] for r in rows))
# head-to-head on the common subset where every predictor is defined (P009-P019)
common = [r for r in rows if r['n2'] and r['n3']]
out['common'] = dict(n=len(common),
    skim_ni_err=st.mean(r['ni_err_sealed'] for r in common),
    n1_ni_err=st.mean(r['n1']['ni_err'] for r in common),
    n2_ni_err=st.mean(r['n2']['ni_err'] for r in common),
    n3_ni_err=st.mean(r['n3']['ni_err'] for r in common),
    skim_new_mae=st.mean(abs(r['new_err']) for r in common),
    n1_new_mae=st.mean(r['n1']['new_err'] for r in common),
    n2_new_mae=st.mean(r['n2']['new_err'] for r in common),
    n3_new_mae=st.mean(r['n3']['new_err'] for r in common),
    skim_axis=sum(r['axis_hit'] for r in common), n1_axis=sum(r['n1']['axis_hit'] for r in common),
    n2_axis=sum(r['n2']['axis_hit'] for r in common), n3_axis=sum(r['n3']['axis_hit'] for r in common),
    skim_full=sum(r['point_exact'] and r['range_exact'] for r in common),
    n1_full=sum(r['n1']['full_exact'] for r in common),
    n2_full=sum(r['n2']['full_exact'] for r in common),
    n3_full=sum(r['n3']['full_exact'] for r in common),
    links_mae_skim=st.mean(abs(r['links_act']-r['links_pred']) for r in common if r['links_pred'] is not None and r['links_act'] is not None))
# rolling-10 mean |NI error| after each paper (sealed basis)
for idx, r in enumerate(rows):
    w = rows[max(0, idx-9):idx+1]
    r['rolling10'] = st.mean(x['ni_err_sealed'] for x in w)
json.dump(out, open('eval-work/evaluation-data.json','w'), indent=1, default=str)

for r in rows:
    print(f"P{r['paper']} {'cron' if r['cron'] else 'will'} cb{r['cb_sealed']}/{r['cb_abs']} "
          f"new {r['pred_new']}->{r['act_new']} rev {r['pred_rev']}->{r['act_rev']} "
          f"axis {int(r['pred_axis'])}->{int(r['act_axis'])} "
          f"NI {r['ni_pred_sealed']:.4f}->{r['ni_act_sealed']:.4f} err {r['ni_err_sealed']:.4f} (rec {r['ni_recorded_err']}) "
          f"OP {r['op_pred']}->{r['op_act']} ptEx {r['point_exact']} rgEx {r['range_exact']} "
          f"links {r['links_pred']}->{r['links_act']} roll10 {r['rolling10']:.4f} "
          f"headx {r['headroom_x'] if r['headroom_x'] is None else round(r['headroom_x'],1)} 2x {r['survives_2x']} 5x {r['survives_5x']}")
print()
for k in ('all','cron','will','streak'):
    print(k, json.dumps(out[k], indent=1))
print('fold_alt', out['fold_alt'])
