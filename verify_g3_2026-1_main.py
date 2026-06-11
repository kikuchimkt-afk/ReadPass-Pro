# -*- coding: utf-8 -*-
"""2026-1 3級（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

OFFICIAL = {
    1: 3, 2: 3, 3: 1, 4: 2, 5: 2, 6: 1, 7: 4, 8: 4, 9: 2, 10: 2,
    11: 1, 12: 4, 13: 3, 14: 3, 15: 1,
    16: 2, 17: 3, 18: 4, 19: 2, 20: 4,
    21: 1, 22: 4,
    23: 1, 24: 2, 25: 3,
    26: 1, 27: 2, 28: 4, 29: 3, 30: 2,
}

d = json.load(open(DATA, encoding="utf-8"))
errors = []

all_qs = []
for sec in d["sections"]:
    all_qs.extend(sec.get("questions", []))
    for pa in sec.get("passages", []):
        all_qs.extend(pa.get("questions", []))

if len(all_qs) != 30:
    errors.append(f"question count {len(all_qs)} != 30")

for q in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={OFFICIAL.get(n)}")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices != 4")

if d.get("exam") != "2026-1":
    errors.append(f"exam={d.get('exam')} != 2026-1")

for key in ("title", "grade", "exam", "sections", "writing", "listening"):
    if key not in d:
        errors.append(f"missing {key}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 30 questions, all answers match official key")
