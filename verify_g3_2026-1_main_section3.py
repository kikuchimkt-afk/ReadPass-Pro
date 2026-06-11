# -*- coding: utf-8 -*-
"""Verify 2026-1 grade3（本会場）section3 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

EXPECTED = {
    21: 1, 22: 4, 23: 1, 24: 2, 25: 3,
    26: 1, 27: 2, 28: 4, 29: 3, 30: 2,
}

Q_KEYS = (
    "question", "questionTranslation", "choices", "choiceTranslations",
    "choiceAnalysis", "choiceAnalysisSimple", "grammar", "grammarSimple",
    "sourceEvidence",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
sec = next((s for s in d["sections"] if s.get("name") == "大問3"), None)
if not sec:
    errors.append("missing 大問3")
    print(f"errors={len(errors)}")
    sys.exit(1)

passages = sec.get("passages", [])
if len(passages) != 3:
    errors.append(f"passage count {len(passages)} != 3")

all_qs = []
for pa in passages:
    if pa.get("label") not in ("A", "B", "C"):
        errors.append(f"bad label {pa.get('label')}")
    if "translations" not in pa or not pa["translations"]:
        errors.append(f"passage {pa.get('label')}: missing translations")
    if len(pa.get("paragraphs", [])) != len(pa.get("translations", [])):
        errors.append(
            f"passage {pa.get('label')}: paragraphs/translations length mismatch"
        )
    if pa.get("format") == "multi-email":
        for em in pa.get("emails", []):
            if "translation" not in em or not em["translation"]:
                errors.append("passage B email missing translation")
    corpus = " ".join(pa.get("paragraphs", []))
    for em in pa.get("emails", []):
        corpus += " " + em.get("body", "")
    for q in pa.get("questions", []):
        n = q["number"]
        ev = q.get("sourceEvidence", [])
        ev_list = ev if isinstance(ev, list) else [ev]
        for phrase in ev_list:
            if phrase and phrase not in corpus:
                errors.append(f"Q{n}: sourceEvidence not in passage text: {phrase[:40]}")
        if not isinstance(ev, list):
            errors.append(f"Q{n}: sourceEvidence should be a list")
    all_qs.extend(pa.get("questions", []))

if len(all_qs) != 10:
    errors.append(f"question count {len(all_qs)} != 10")

for q in all_qs:
    n = q["number"]
    if EXPECTED.get(n) != q.get("answer"):
        errors.append(f"Q{n}: answer={q.get('answer')} official={EXPECTED.get(n)}")
    for key in Q_KEYS:
        if key not in q or not q[key]:
            errors.append(f"Q{n}: missing {key}")
    if len(q.get("choices", [])) != 4:
        errors.append(f"Q{n}: choices != 4")
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if i + 1 == q["answer"]:
            if not ca.startswith("✅"):
                errors.append(f"Q{n}: correct choice {i + 1} missing ✅")
        elif ca.startswith("✅"):
            errors.append(f"Q{n}: wrong choice {i + 1} has ✅")
    for i, ca in enumerate(q.get("choiceAnalysisSimple", [])):
        if i + 1 == q["answer"]:
            if not ca.startswith("○"):
                errors.append(f"Q{n}: correct simple choice {i + 1} missing ○")

print(f"passages={len(passages)} questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: section3 Q21-30 with rich explanations")
