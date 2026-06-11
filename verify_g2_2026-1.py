# -*- coding: utf-8 -*-
"""2026-1 2級（本会場）OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

OFFICIAL = {
    1: 4, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 3, 10: 1,
    11: 4, 12: 4, 13: 2, 14: 1, 15: 1, 16: 1, 17: 2,
    18: 1, 19: 1, 20: 3, 21: 2, 22: 1, 23: 4,
    24: 3, 25: 1, 26: 4, 27: 3, 28: 1, 29: 3, 30: 1, 31: 4,
}

LISTENING = {
    "part1": {
        1: 3, 2: 4, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 1, 10: 4,
        11: 4, 12: 1, 13: 4, 14: 3, 15: 2,
    },
    "part2": {
        16: 1, 17: 2, 18: 1, 19: 1, 20: 1, 21: 3, 22: 2, 23: 1, 24: 4, 25: 2,
        26: 2, 27: 4, 28: 1, 29: 2, 30: 2,
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
