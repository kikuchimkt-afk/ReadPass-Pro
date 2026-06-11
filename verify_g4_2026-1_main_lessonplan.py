# -*- coding: utf-8 -*-
"""Verify 2026-1 grade4（本会場）lessonPlan structure and audio."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])

if len(fps) != 4:
    errors.append(f"focusPoints count {len(fps)} != 4")

for i, fp in enumerate(fps):
    fid = fp.get("id", f"fp{i + 1}")
    for key in ("title", "subtitle", "explanation", "explanationSimple",
                "sourceQuote", "sourceLocation"):
        if not fp.get(key):
            errors.append(f"{fid}: missing {key}")
    examples = fp.get("examples", [])
    if len(examples) < 3:
        errors.append(f"{fid}: examples < 3")
    for j, ex in enumerate(examples):
        for key in ("en", "ja", "note", "noteSimple", "audio"):
            if not ex.get(key):
                errors.append(f"{fid} ex{j + 1}: missing {key}")
            elif key == "audio":
                path = os.path.join(BASE, ex[key].replace("/", os.sep))
                if not os.path.isfile(path) or os.path.getsize(path) < 500:
                    errors.append(f"{fid} ex{j + 1}: missing audio file")
    pp = fp.get("practicePassage", {})
    for key in ("en", "ja", "source", "audioFile"):
        if not pp.get(key):
            errors.append(f"{fid}: practicePassage missing {key}")
        elif key == "audioFile":
            path = os.path.join(BASE, pp[key].replace("/", os.sep))
            if not os.path.isfile(path) or os.path.getsize(path) < 500:
                errors.append(f"{fid}: missing practice audio")
    if not fp.get("highlightPatterns"):
        errors.append(f"{fid}: missing highlightPatterns")
    if len(fp.get("practiceQuestions", [])) < 2:
        errors.append(f"{fid}: practiceQuestions < 2")
    if len(fp.get("practiceQuestionsSimple", [])) < 2:
        errors.append(f"{fid}: practiceQuestionsSimple < 2")
    if fp.get("sourceQuoteAudio"):
        path = os.path.join(BASE, fp["sourceQuoteAudio"].replace("/", os.sep))
        if not os.path.isfile(path) or os.path.getsize(path) < 500:
            errors.append(f"{fid}: missing sourceQuoteAudio")

print(f"focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan 4 FPs with audio")
