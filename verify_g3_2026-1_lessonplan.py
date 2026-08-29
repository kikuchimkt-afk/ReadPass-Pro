# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade3 lessonPlan structure and audio."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])

if len(fps) != 4:
    errors.append(f"focusPoints count {len(fps)} != 4")
if [fp.get("id") for fp in fps] != ["fp1", "fp2", "fp3", "fp4"]:
    errors.append("focusPoint IDs/order mismatch")

for i, fp in enumerate(fps):
    fid = fp.get("id", f"fp{i + 1}")
    for key in ("title", "subtitle", "explanation", "explanationSimple",
                "sourceQuote", "sourceLocation", "sourceQuoteAudio"):
        if not fp.get(key):
            errors.append(f"{fid}: missing {key}")
    if not 80 <= len(fp.get("explanation", "")) <= 220:
        errors.append(f"{fid}: explanation length {len(fp.get('explanation', ''))}")
    if not 35 <= len(fp.get("explanationSimple", "")) <= 160:
        errors.append(
            f"{fid}: explanationSimple length {len(fp.get('explanationSimple', ''))}"
        )
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
    if len(fp.get("practiceQuestions", [])) != 3:
        errors.append(f"{fid}: practiceQuestions != 3")
    if len(fp.get("practiceQuestionsSimple", [])) != 3:
        errors.append(f"{fid}: practiceQuestionsSimple != 3")
    for field in ("practiceQuestions", "practiceQuestionsSimple"):
        for j, question in enumerate(fp.get(field, []), 1):
            if not question.get("q") or not question.get("a"):
                errors.append(f"{fid}: {field}[{j}] missing q/a")
    if fp.get("sourceQuoteAudio"):
        path = os.path.join(BASE, fp["sourceQuoteAudio"].replace("/", os.sep))
        if not os.path.isfile(path) or os.path.getsize(path) < 500:
            errors.append(f"{fid}: missing sourceQuoteAudio")

lesson_blob = json.dumps(lp, ensure_ascii=False)
for stale in (
    "wait for ～＝「～を待つ」",
    "お母さんと弟も来ます",
    "しつだんした話",
    "ねむれって",
):
    if stale in lesson_blob:
        errors.append(f"stale explanation remains: {stale}")

print(f"focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan 4 FPs with audio")
