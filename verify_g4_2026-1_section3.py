# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade4 section3 (sentence-order) structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)

EXPECTED = {21: 1, 22: 1, 23: 3, 24: 4, 25: 2}

REQUIRED_KEYS = (
    "text", "choices", "words", "correctOrder", "framePrefix", "frameSuffix",
    "answerSlots", "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "questionAudio",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問3"), None)
if not sec:
    errors.append("missing 大問3")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

if sec.get("type") != "sentence-order":
    errors.append(f"type is {sec.get('type')}, expected sentence-order")

qs = sec["questions"]
if len(qs) != 5:
    errors.append(f"question count {len(qs)} != 5")

for q in qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in REQUIRED_KEYS:
        if key not in q:
            errors.append(f"Q{n}: missing {key}")
    if len(q.get("words", [])) != 5:
        errors.append(f"Q{n}: words count != 5")
    if len(q.get("correctOrder", [])) != 5:
        errors.append(f"Q{n}: correctOrder count != 5")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices count != 4")
    if len(q.get("choiceAnalysis", [])) != 4:
        errors.append(f"Q{n}: choiceAnalysis count != 4")
    # 正解スロットと選択肢の整合
    slots = q.get("answerSlots", [])
    order = q.get("correctOrder", [])
    words = q.get("words", [])
    if len(slots) == 2 and len(order) == 5:
        w2 = words[order[slots[0] - 1] - 1]
        w4 = words[order[slots[1] - 1] - 1]
        circled = lambda i: chr(0x2460 + i - 1)
        expected_label = f"{circled(order[slots[0] - 1])}−{circled(order[slots[1] - 1])}"
        actual = q["choices"][q["answer"] - 1]
        if actual != expected_label:
            errors.append(
                f"Q{n}: answer choice {actual} != slot pair {expected_label} ({w2}, {w4})"
            )
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if i + 1 == q["answer"]:
            if not ca.startswith("○"):
                errors.append(f"Q{n}: correct choice {i + 1} missing ○")
        elif ca.startswith("○"):
            errors.append(f"Q{n}: wrong choice {i + 1} has ○")

print(f"questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 rich data verified")
