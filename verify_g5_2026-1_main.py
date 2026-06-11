# -*- coding: utf-8 -*-
"""2026-1 5級（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)

OFFICIAL = {
    1: 3, 2: 4, 3: 4, 4: 2, 5: 4, 6: 4, 7: 2, 8: 2, 9: 4, 10: 1,
    11: 1, 12: 4, 13: 1, 14: 4, 15: 1,
    16: 1, 17: 2, 18: 1, 19: 1, 20: 1,
    21: 3, 22: 3, 23: 1, 24: 1, 25: 1,
}

LISTENING = {
    "part1": {1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
    "part2": {11: 2, 12: 1, 13: 1, 14: 2, 15: 2},
    "part3": {
        16: 3, 17: 2, 18: 3, 19: 3, 20: 2,
        21: 3, 22: 1, 23: 2, 24: 1, 25: 3,
    },
}

d = json.load(open(DATA, encoding="utf-8"))
errors = []

all_qs = []
for sec in d["sections"]:
    all_qs.extend(sec.get("questions", []))

if len(all_qs) != 25:
    errors.append(f"question count {len(all_qs)} != 25")

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
print("OK: 25 questions, answers, listening")
