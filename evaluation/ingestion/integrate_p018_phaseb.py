# -*- coding: utf-8 -*-
"""Paper 018, Phase B: drawing-count prose that waits on the registry
extraction (683 entries: True 313 = 271 stipulation + 42 verified;
Unknown 370 = 321 attributed + 29 synthesis + 18 open + 2 estimate;
False 0, Fiction 0). Scrolls: 1.4.1 (framing counts, incl. the Study
S010 paragraph its pass left out), 1.5.3 (statement counts), 1.4.6
(drawing event)."""
P = "/home/hatch/workspace/research-tracker/build_research_phext.py"
src = open(P, encoding="utf-8").read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:80]!r}"
    src = src.replace(old, new)

# ---------- 1.5.3: drawing paragraph before HOW TO WALK IT ----------
rep("""count of the drawing events stands at 1.4.6.

HOW TO WALK IT.""",
    """count of the drawing events stands at 1.4.6.

DRAWING OF PAPER 018 (Paper 018 taken in, 2026-11-13). The
phext stands at 683 scrolls; the living registry stands exact
at 683: True 313 (271 by stipulation, 42 by evidence), Unknown
370 (321 by attribution, 29 by synthesis, 18 open, 2 by
estimate), False 0, Fiction 0. The drawing added 24 statements
to the book: seven concepts, five foundations, three defined
words, and the nine scrolls of a chapter. No held statement
was carried in a new form. No restructure pass fell due
inside the taking-in. This drawing brings author check
number 20 (Chapter 29), also True by receipt.
False still stands empty after 18 papers and ten studies. The
count of the drawing events stands at 1.4.6.

HOW TO WALK IT.""")

# ---------- 1.4.6: the drawing event of Paper 018 ----------
rep("""instance theorem holds.
""",
    """instance theorem holds.
""", n=src.count("instance theorem holds.\n"))
# append after the LAST occurrence (Study S010's paragraph)
idx = src.rfind("instance theorem holds.\n")
end = idx + len("instance theorem holds.\n")
addition = """
The drawing of Paper 018 (2026-11-13): 24 scrolls entered —
seven concepts (1.2.230-1.2.236, cluster O extended a third
time), five foundations (1.3.222-1.3.226), three defined
words (1.3.227-1.3.229), and the nine scrolls of Chapter 29.
No held scroll was carried in a new form. No restructure
pass fell due inside the taking-in. One entry entered among
the verified: author check number twenty (29.1.6), True by
receipt. False stands empty still. The registry was drawn
from the built phext as it then stood; its sha256 stands in
the registry file kept with the tracker, and the Lean model
was re-checked over the new registry the same day — the
drawing entered into the model in full, its entry count
first checked against the count of the registry itself —
and its instance theorem holds.
"""
src = src[:end] + addition + src[end:]

# ---------- 1.4.1: S010 paragraph (left out by its pass) + P018 paragraph ----------
anchor = "The drawing of Paper 017 adds two plain foundations"
i = src.find(anchor)
assert i > 0
j = src.find('"""),', i)
assert j > i
insert = """
The drawing of Study S010 adds one plain foundation —
undefined behaviour (1.3.219) — and coins two words, each
with its scroll: elaboration (1.3.220) and
autoverification (1.3.221); its author stands as a company
in the declared list kept with the tracker. The counts of
this drawing: the phext stands at 659 scrolls and the
living registry exact at 659 — True 303 (262 by
definition, 41 by receipt), Unknown 356 (309 by the
say-so of a source, 28 reasoned links, 17 open questions,
2 weighed estimates), False 0, Fiction 0. Two held scrolls
were carried in a new form: 1.2.48 and 1.2.208, by
receipt, their standings unchanged. In the living
registry the fifteen scrolls of this drawing stand
entered like any other scroll: pages of the record
itself, set down under the rules of the tracker. The
counts of the first drawing are kept above as they were
made; the counts of this drawing stand with them.

The drawing of Paper 018 adds five plain foundations —
spread that changes from place to place (1.3.222), a
heavy tail (1.3.223), the sign of a number (1.3.224), one
peak (1.3.225), and cutting power (1.3.226) — and coins
three words, each with its scroll: heteroscedastic
(1.3.227), unimodal (1.3.228), and extremal (1.3.229); its
name (Baraud; Maillard stands behind the taken-in
machinery as a cited co-author, not an entry) stands as
an address in the declared list kept with the tracker.
The counts of this drawing: the phext stands at 683
scrolls and the living registry exact at 683 — True 313
(271 by definition, 42 by receipt), Unknown 370 (321 by
the say-so of a source, 29 reasoned links, 18 open
questions, 2 weighed estimates), False 0, Fiction 0. No
held scroll was carried in a new form. In the living
registry the twenty-four scrolls of this drawing stand
entered like any other scroll: pages of the record
itself, set down under the rules of the tracker. The
counts of the first drawing are kept above as they were
made; the counts of this drawing stand with them.
"""
src = src[:j] + insert + src[j:]

open(P, "w", encoding="utf-8").write(src)
print("phase B written OK")
