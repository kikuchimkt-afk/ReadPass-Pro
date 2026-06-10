# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = os.path.join("data", "grade-pre2", "2026-1-sat", "data.json")
d = json.load(open(path, encoding="utf-8"))
errs = []

lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])
if len(fps) != 5:
    errs.append(f"expected 5 FPs, got {len(fps)}")

required_fp_keys = [
    "id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
    "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
    "highlightColor", "highlightLabel",
]
required_pp_keys = ["en", "ja"]

for fp in fps:
    fid = fp.get("id", "?")
    for k in required_fp_keys:
        if k not in fp:
            errs.append(f"{fid} missing {k}")
    pp = fp.get("practicePassage", {})
    for k in required_pp_keys:
        if k not in pp:
            errs.append(f"{fid} practicePassage missing {k}")
    if not pp.get("en", "").startswith("[出典:"):
        errs.append(f"{fid} practicePassage missing [出典: tag")
    en = pp.get("en", "")
    for pat in fp.get("highlightPatterns", []):
        if pat not in en.replace("[出典: A Lost Dog]", "").replace("[出典: A job at a ski resort]", "").replace("[出典: Social Media for Mental Health]", ""):
            # patterns must appear in passage body (after stripping source tags)
            body = en
            for tag in ["[出典: A Lost Dog]\n", "[出典: A job at a ski resort]\n", "[出典: Social Media for Mental Health]\n"]:
                body = body.replace(tag, "")
            if pat not in body:
                errs.append(f"{fid} pattern not in passage: {pat[:40]}")

titles = [fp["title"] for fp in fps]
if len(titles) != len(set(titles)):
    errs.append("duplicate FP titles")

print(f"lessonPlan FPs={len(fps)} errors={len(errs)}")
for e in errs:
    print(e)
sys.exit(1 if errs else 0)
