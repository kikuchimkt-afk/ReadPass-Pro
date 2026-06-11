# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

OFFICIAL = {
    1: 2, 2: 1, 3: 1, 4: 4, 5: 4, 6: 3, 7: 2, 8: 3, 9: 4, 10: 1,
    11: 2, 12: 4, 13: 1, 14: 1, 15: 2,
    16: 1, 17: 3, 18: 2, 19: 1, 20: 3,
    21: 4, 22: 1, 23: 3, 24: 4, 25: 3, 26: 3, 27: 4, 28: 2, 29: 3,
}

LISTENING = {
    "part1": {
        1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1, 7: 3, 8: 3, 9: 3, 10: 1,
    },
    "part2": {
        11: 3, 12: 3, 13: 4, 14: 1, 15: 4, 16: 2, 17: 1, 18: 2, 19: 1, 20: 4,
    },
    "part3": {
        21: 3, 22: 3, 23: 2, 24: 2, 25: 2, 26: 1, 27: 2, 28: 2, 29: 3, 30: 4,
    },
}

d = json.load(open(DATA, encoding="utf-8"))
errors = []

all_qs = []
for sec in d["sections"]:
    if sec.get("questions"):
        all_qs.extend(sec["questions"])
    for pa in sec.get("passages", []):
        all_qs.extend(pa.get("questions", []))

if len(all_qs) != 29:
    errors.append(f"question count {len(all_qs)} != 29")

for q in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={OFFICIAL.get(n)}")
    choices = q.get("choices", [])
    if len(choices) != 4:
        errors.append(f"Q{n}: choices != 4")

for key in ("title", "grade", "exam", "year", "session", "sections"):
    if key not in d:
        errors.append(f"missing {key}")

if d.get("exam") != "2026-1":
    errors.append(f"exam={d.get('exam')}")

if len(d.get("sections", [])) != 4:
    errors.append(f"sections count {len(d.get('sections', []))} != 4")

if "listening" not in d:
    errors.append("missing listening")
else:
    for part, expected in LISTENING.items():
        actual = d["listening"].get(part, {})
        for num, ans in expected.items():
            if actual.get(num) != ans and actual.get(str(num)) != ans:
                errors.append(f"listening {part} Q{num}: {actual.get(num)} != {ans}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: 29 questions, all answers match official key")
