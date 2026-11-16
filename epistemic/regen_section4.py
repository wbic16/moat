#!/usr/bin/env python3
"""Regenerate the Section 4 list scrolls (1.4.2 True, 1.4.3 False,
1.4.4 Unknown, 1.4.5 Fiction) in build_research_phext.py from
epistemic/registry.json: every entry except Section 4's own six
pages, grouped by status, in registry (parse) order, formatted
'- coord — claim [basis]'. The preamble of each list scroll is
kept; only the entry lines are replaced. Prose scrolls 1.4.1 and
1.4.6 are NOT touched (their counts/events are written per pass).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILDER = os.path.join(HERE, "..", "build_research_phext.py")
SECTION4 = {f"1.1.1/1.1.1/1.4.{i}" for i in range(1, 7)}
HEADING = {"True": "# Registry: True", "False": "# Registry: False",
           "Unknown": "# Registry: Unknown", "Fiction": "# Registry: Fiction"}

reg = json.load(open(os.path.join(HERE, "registry.json")))
entries = [e for e in reg["entries"] if e["coordinate"] not in SECTION4]
src = open(BUILDER).read()

for status, heading in HEADING.items():
    lines = [f"- {e['coordinate']} — {e['claim']} [{e['basis']}]"
             for e in entries if e["status"] == status]
    start = src.index(f'"""{heading}')
    end = src.index('""")', start)
    block = src[start:end]
    # split preamble (up to first entry line) from entries
    m = re.search(r"\n- 1\.1\.1/", block)
    if m:
        preamble, _ = block[:m.start()], block[m.start():]
        newblock = preamble + "\n" + "\n".join(lines) + "\n"
    else:
        if lines:
            newblock = block.rstrip() + "\n\n" + "\n".join(lines) + "\n"
        else:
            newblock = block  # prose-only scroll, no entries yet
    src = src[:start] + newblock + src[end:]
    print(f"{heading}: {len(lines)} entries")

open(BUILDER, "w").write(src)
print("section 4 lists regenerated from registry.json")
