#!/usr/bin/env python3
"""Splice a fresh RegistryData.lean entry list into a project's
Mvo/RegistryData.lean (the file the Lean build actually reads).
Usage: splice_registry.py <project_dir> <fresh_registry_data.lean>
Verifies the entry count inside the def after splicing."""
import sys

proj, fresh = sys.argv[1], sys.argv[2]

def entry_lines(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("def currentRegistry"))
    end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == "]")
    return lines[start + 1:end]

new_entries = entry_lines(fresh)
print(f"fresh list: {len(new_entries)} entry lines")

target = proj.rstrip("/") + "/Mvo/RegistryData.lean"
lines = open(target, encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(lines) if "def currentRegistry" in l)
end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == "]")
old_n = end - start - 1
lines[start + 1:end] = new_entries
open(target, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"spliced {target}: {old_n} -> {len(new_entries)} entry lines")

# verify by re-reading
lines2 = open(target, encoding="utf-8").read().splitlines()
s2 = next(i for i, l in enumerate(lines2) if "def currentRegistry" in l)
e2 = next(i for i in range(s2 + 1, len(lines2)) if lines2[i].strip() == "]")
ids = [l for l in lines2[s2 + 1:e2] if "id :=" in l]
print(f"verify: {len(ids)} entries inside currentRegistry; first id line: {ids[0].strip()}; last: {ids[-1].strip()}")
