# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade4 section2 structure and answers."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)
DATA_DIR = os.path.dirname(DATA_PATH)


def has_blank(text):
    return bool(re.search(r"[（(][\s　]*[）)]", text or ""))


def audio_ok(rel):
    path = os.path.join(DATA_DIR, (rel or "").replace("/", os.sep))
    return bool(rel) and os.path.isfile(path) and os.path.getsize(path) >= 500

EXPECTED = {16: 2, 17: 2, 18: 1, 19: 4, 20: 3}

REQUIRED_KEYS = (
    "text", "translation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "questionAudio",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問2"), None)
if not sec:
    errors.append("missing 大問2")
    print(f"errors={len(errors)}")
    for e in errors:
        print(" ", e)
    sys.exit(1)

qs = sec["questions"]
if len(qs) != 5:
    errors.append(f"question count {len(qs)} != 5")

for q in qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in REQUIRED_KEYS:
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q["choices"]) != 4:
        errors.append(f"Q{n}: choices count {len(q['choices'])}")
    if len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"Q{n}: choiceTranslations count {len(q.get('choiceTranslations', []))}")
    if has_blank(q.get("text")) and not has_blank(q.get("translation")):
        errors.append(f"Q{n}: blank missing from translation")
    if not audio_ok(q.get("questionAudio")):
        errors.append(f"Q{n}: missing audio {q.get('questionAudio')}")
    if len(q["choiceAnalysis"]) != 4:
        errors.append(f"Q{n}: choiceAnalysis count {len(q['choiceAnalysis'])}")
    if len(q["choiceAnalysisSimple"]) != 4:
        errors.append(f"Q{n}: choiceAnalysisSimple count {len(q['choiceAnalysisSimple'])}")
    for field in ("choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        marked = [i + 1 for i, ca in enumerate(values) if ca.lstrip().startswith("○")]
        if marked != [q["answer"]]:
            errors.append(f"Q{n}: {field} marker positions {marked}")
        if any(ca.lstrip().startswith(("✅", "❌")) for ca in values):
            errors.append(f"Q{n}: {field} has old emoji marker")

print(f"questions={len(qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section2 rich data verified")
