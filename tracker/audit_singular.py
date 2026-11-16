import subprocess, sys
out = subprocess.run(["python3", "/home/hatch/workspace/custom-skills/singular/scripts/check_singular.py", "research.phext"], capture_output=True, text=True).stdout
flagged = {}
for line in out.splitlines():
    line = line.strip()
    if not line or line.startswith("flagged"): continue
    parts = line.split()
    word = parts[0]
    n = 1
    if len(parts) > 1 and parts[1].startswith("x"): n = int(parts[1][1:])
    flagged[word] = n
allowed = set(open("singular-names.txt").read().split()) | set(open("singular-coined.txt").read().split())
resid = {w: n for w, n in flagged.items() if w not in allowed}
print(f"total flagged tokens {sum(flagged.values())}, distinct {len(flagged)}; residual distinct {len(resid)}")
for w, n in sorted(resid.items(), key=lambda kv: -kv[1]):
    print(f"  {w} x{n}")
