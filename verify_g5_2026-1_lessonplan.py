# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade5 lessonPlan structure."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade5", "2026-1-sat", "data.json")
ADIR = os.path.join(BASE, "data", "grade5", "2026-1-sat")


def audio_ok(rel):
    if not rel:
        return False
    fp = os.path.join(ADIR, rel.replace("/", os.sep))
    return os.path.isfile(fp) and os.path.getsize(fp) >= 500


with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])

if not lp.get("title"):
    errors.append("missing lessonPlan.title")
if len(fps) != 3:
    errors.append(f"focusPoints count {len(fps)} != 3")

corpus = ""
for sec in d.get("sections", []):
    for q in sec.get("questions", []):
        corpus += q.get("text", "") + " "
        if q.get("words"):
            corpus += " ".join(q["words"]) + " "

required_fp = (
    "id", "title", "subtitle", "explanation", "explanationSimple",
    "sourceQuote", "sourceLocation", "examples", "practicePassage",
    "highlightPatterns", "highlightColor", "highlightLabel",
    "practiceQuestions", "practiceQuestionsSimple",
)

for fp in fps:
    fid = fp.get("id", "?")
    for key in required_fp:
        if key not in fp or not fp[key]:
            errors.append(f"{fid}: missing {key}")
    if len(fp.get("examples", [])) < 3:
        errors.append(f"{fid}: examples < 3")
    pp = fp.get("practicePassage", {})
    if not pp.get("en") or not pp.get("ja"):
        errors.append(f"{fid}: practicePassage en/ja missing")
    if "[出典:" not in pp.get("en", ""):
        errors.append(f"{fid}: practicePassage missing [出典: ...]")
    if len(fp.get("practiceQuestions", [])) < 2:
        errors.append(f"{fid}: practiceQuestions < 2")
    af = pp.get("audioFile")
    if af and not audio_ok(af):
        errors.append(f"{fid}: missing audio {af}")
    sq = fp.get("sourceQuoteAudio")
    if sq and not audio_ok(sq):
        errors.append(f"{fid}: missing sourceQuoteAudio {sq}")
    for j, ex in enumerate(fp.get("examples", [])):
        au = ex.get("audio")
        if au and not audio_ok(au):
            errors.append(f"{fid} ex{j+1}: missing audio {au}")
    search = corpus + " " + pp.get("en", "")
    for pat in fp.get("highlightPatterns", []):
        if pat not in search:
            errors.append(f"{fid}: highlight不在: {pat[:50]}")

print(f"focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan 3 focusPoints verified")
