# -*- coding: utf-8 -*-
"""2026-1-sat 3級 OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

OFFICIAL = {
    1: 2, 2: 4, 3: 1, 4: 4, 5: 1, 6: 4, 7: 3, 8: 4, 9: 4, 10: 4,
    11: 3, 12: 4, 13: 3, 14: 3, 15: 2,
    16: 3, 17: 3, 18: 3, 19: 1, 20: 2,
    21: 3, 22: 1, 23: 1, 24: 4, 25: 3,
    26: 3, 27: 1, 28: 2, 29: 3, 30: 4,
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

for key in ("title", "grade", "exam", "sections"):
    if key not in d:
        errors.append(f"missing {key}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 30 questions, all answers match official key")
