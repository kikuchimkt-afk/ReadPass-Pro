# -*- coding: utf-8 -*-
"""2026-1-sat 5級 OCRデータ検証（公式解答照合）"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat", "data.json",
)

OFFICIAL = {
    1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 1, 10: 1,
    11: 3, 12: 1, 13: 3, 14: 3, 15: 3,
    16: 1, 17: 3, 18: 1, 19: 3, 20: 3,
    21: 4, 22: 4, 23: 3, 24: 3, 25: 4,
}

LISTENING = {
    "part1": {1: 2, 2: 3, 3: 1, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
    "part2": {11: 2, 12: 1, 13: 3, 14: 3, 15: 1},
    "part3": {
        16: 2, 17: 1, 18: 1, 19: 2, 20: 3,
        21: 1, 22: 1, 23: 2, 24: 2, 25: 1,
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

sec3 = next(s for s in d["sections"] if s.get("name") == "大問3")
for q in sec3["questions"]:
    n = q["number"]
    slots = q.get("answerSlots", [])
    order = q.get("correctOrder", [])
    if len(slots) == 2 and len(order) == 4:
        w1 = order[slots[0] - 1]
        w3 = order[slots[1] - 1]
        circled = lambda i: chr(0x2460 + i - 1)
        expected = f"{circled(w1)} ─ {circled(w3)}"
        actual = q["choices"][q["answer"] - 1]
        if actual != expected:
            errors.append(f"Q{n}: choice {actual} != expected {expected}")

for key in ("title", "grade", "exam", "year", "session", "sections"):
    if key not in d:
        errors.append(f"missing {key}")

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
print("OK: 25 questions, all answers match official key")
