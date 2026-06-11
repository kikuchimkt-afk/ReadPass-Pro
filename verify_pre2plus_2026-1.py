# -*- coding: utf-8 -*-
"""2026-1 準2級プラス（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

OFFICIAL = {
    1: 4, 2: 1, 3: 3, 4: 4, 5: 4, 6: 4, 7: 3, 8: 4, 9: 1, 10: 4,
    11: 1, 12: 3, 13: 1, 14: 3, 15: 4, 16: 3, 17: 3,
    18: 2, 19: 4, 20: 3, 21: 1, 22: 2, 23: 4,
    24: 3, 25: 2, 26: 3, 27: 1, 28: 4, 29: 3, 30: 4, 31: 2,
}

LISTENING = {
    "part1": {
        1: 3, 2: 3, 3: 3, 4: 1, 5: 2, 6: 2, 7: 2, 8: 4, 9: 3, 10: 1,
        11: 4, 12: 2, 13: 1, 14: 1, 15: 1,
    },
    "part2": {
        16: 4, 17: 3, 18: 2, 19: 2, 20: 4, 21: 4, 22: 3, 23: 4, 24: 2, 25: 1,
        26: 3, 27: 3, 28: 1, 29: 1, 30: 3,
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

if len(all_qs) != 31:
    errors.append(f"question count {len(all_qs)} != 31")

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
print("OK: 31 questions, all answers match official key")
