# -*- coding: utf-8 -*-
"""Verify 2026-1-sat pre2plus section2 structure and answers."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

EXPECTED = {18: 2, 19: 1, 20: 4, 21: 3, 22: 2, 23: 1}

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
assert len(d["sections"]) >= 2, f"expected >=2 sections, got {len(d['sections'])}"
sec = d["sections"][1]
assert sec["type"] == "passage-fill", f"expected passage-fill, got {sec['type']}"
assert len(sec["passages"]) == 2, f"expected 2 passages, got {len(sec['passages'])}"

for pa in sec["passages"]:
  for key in ("label", "title", "paragraphs", "translations"):
    if key not in pa or not pa[key]:
      errors.append(f"passage {pa.get('label')}: missing {key}")
  if len(pa["paragraphs"]) != len(pa["translations"]):
    errors.append(f"passage {pa.get('label')}: paragraphs/translations length mismatch")

all_qs = [q for pa in sec["passages"] for q in pa["questions"]]
for q in all_qs:
    n = q["number"]
    if q["answer"] != EXPECTED[n]:
        errors.append(f"Q{n}: answer {q['answer']} != expected {EXPECTED[n]}")
    for key in ("choices", "choiceTranslations", "choiceAnalysis", "sourceEvidence"):
        if key not in q or (key != "sourceEvidence" and len(q[key]) != 4):
            errors.append(f"Q{n}: bad {key}")
    if not q.get("sourceEvidence"):
        errors.append(f"Q{n}: missing sourceEvidence")
    if "grammar" not in q or not q["grammar"]:
        errors.append(f"Q{n}: missing grammar")

print(f"section2 passages=2 questions={len(all_qs)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
