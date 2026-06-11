# -*- coding: utf-8 -*-
"""2026-1 4級（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)

OFFICIAL = {
    1: 2, 2: 3, 3: 1, 4: 1, 5: 3, 6: 2, 7: 1, 8: 2, 9: 2, 10: 1,
    11: 1, 12: 1, 13: 4, 14: 2, 15: 3,
    16: 4, 17: 2, 18: 4, 19: 3, 20: 3,
    21: 2, 22: 1, 23: 2, 24: 3, 25: 3,
    26: 1, 27: 2, 28: 3, 29: 3, 30: 1,
    31: 3, 32: 3, 33: 4, 34: 1, 35: 3,
}

LISTENING = {
    "part1": {1: 1, 2: 3, 3: 2, 4: 1, 5: 1, 6: 1, 7: 3, 8: 1, 9: 3, 10: 2},
    "part2": {11: 1, 12: 2, 13: 3, 14: 4, 15: 4, 16: 3, 17: 4, 18: 3, 19: 4, 20: 1},
    "part3": {21: 2, 22: 3, 23: 3, 24: 4, 25: 2, 26: 4, 27: 1, 28: 3, 29: 1, 30: 4},
}

d = json.load(open(DATA, encoding="utf-8"))
errors = []

all_qs = []
for sec in d["sections"]:
    all_qs.extend(sec.get("questions", []))
    for pa in sec.get("passages", []):
        all_qs.extend(pa.get("questions", []))

if len(all_qs) != 35:
    errors.append(f"question count {len(all_qs)} != 35")

for q in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={OFFICIAL.get(n)}")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices != 4")

for key in ("title", "grade", "exam", "year", "session", "sections"):
    if key not in d:
        errors.append(f"missing {key}")

if d.get("exam") != "2026-1":
    errors.append(f"exam={d.get('exam')} != 2026-1")

for part, expected in LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for k, v in expected.items():
        gv = got.get(str(k), got.get(k))
        if gv != v:
            errors.append(f"listening {part} Q{k}: {gv} != {v}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 35 questions, all answers match official key")
