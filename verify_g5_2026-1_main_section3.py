# -*- coding: utf-8 -*-
"""Verify 2026-1 grade5（本会場）section3."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "grade5", "2026-1")

EXPECTED = {21: 3, 22: 3, 23: 1, 24: 1, 25: 1}
KEYS = ("grammar", "grammarSimple", "choiceAnalysis", "choiceAnalysisSimple",
        "words", "correctOrder", "answerSlots", "questionAudio")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
sec = next(s for s in d["sections"] if s["name"] == "大問3")

for q in sec["questions"]:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != {EXPECTED[n]}")
    for key in KEYS:
        if not q.get(key):
            errors.append(f"Q{n}: missing {key}")
    order = q.get("correctOrder", [])
    words = q.get("words", [])
    slots = q.get("answerSlots", [])
    if len(order) == 4 and len(words) == 4 and len(slots) == 2:
        circled = lambda i: chr(0x2460 + i - 1)
        expected_label = f"{circled(order[slots[0] - 1])} ─ {circled(order[slots[1] - 1])}"
        actual = q["choices"][q["answer"] - 1]
        if actual != expected_label:
            errors.append(f"Q{n}: {actual} != {expected_label}")

print(f"errors={len(errors)}")
for e in errors:
    print(" ", e)
sys.exit(1 if errors else 0)
