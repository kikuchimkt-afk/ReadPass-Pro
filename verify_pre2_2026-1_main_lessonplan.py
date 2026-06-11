# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）lessonPlan 検証"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])

if len(fps) != 5:
    errors.append(f"focusPoints count = {len(fps)}, expected 5")

all_text = ""
for sec in d.get("sections", []):
    for q in sec.get("questions", []):
        all_text += q.get("text", "") + " "
        all_text += " ".join(q.get("choices", [])) + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p.get("paragraphs", [])) + " "
        for qq in p.get("questions", []):
            all_text += " ".join(qq.get("choices", [])) + " "
            if qq.get("question"):
                all_text += qq.get("question", "") + " "

for i, fp in enumerate(fps):
    exp_id = f"fp{i + 1}"
    if fp.get("id") != exp_id:
        errors.append(f"{exp_id}: id mismatch ({fp.get('id')})")
    for key in (
        "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions",
        "highlightPatterns", "highlightColor", "highlightLabel",
    ):
        if key not in fp or not fp[key]:
            errors.append(f"{exp_id}: missing or empty '{key}'")
    if len(fp.get("examples", [])) < 3:
        errors.append(f"{exp_id}: need >=3 examples")
    pp = fp.get("practicePassage", {})
    if not pp.get("en") or not pp.get("ja"):
        errors.append(f"{exp_id}: practicePassage missing en/ja")
    if "[出典:" not in pp.get("en", ""):
        errors.append(f"{exp_id}: practicePassage missing [出典: ...]")
    if len(fp.get("practiceQuestions", [])) < 4:
        errors.append(f"{exp_id}: need >=4 practiceQuestions")
    if len(fp.get("highlightPatterns", [])) < 3:
        errors.append(f"{exp_id}: need >=3 highlightPatterns")
    for pat in fp.get("highlightPatterns", []):
        if pat not in all_text:
            errors.append(f"{exp_id}: pattern not in exam text: {pat[:50]}...")

print(f"lessonPlan focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan verified")
