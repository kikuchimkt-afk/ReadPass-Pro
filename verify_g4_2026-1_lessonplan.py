# -*- coding: utf-8 -*-
"""Verify 2026-1-sat grade4 lessonPlan structure."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade4", "2026-1-sat", "data.json")
ADIR = os.path.join(BASE, "data", "grade4", "2026-1-sat")


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
if len(fps) != 4:
    errors.append(f"focusPoints count {len(fps)} != 4")

corpus = ""
for sec in d.get("sections", []):
    for q in sec.get("questions", []):
        corpus += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus += " ".join(p.get("paragraphs", [])) + " "

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
    if len(fp.get("examples", [])) != 3:
        errors.append(f"{fid}: examples != 3")
    if len(fp.get("explanation", "")) < 100:
        errors.append(f"{fid}: explanation too short")
    pp = fp.get("practicePassage", {})
    if not pp.get("en") or not pp.get("ja"):
        errors.append(f"{fid}: practicePassage en/ja missing")
    if "[出典:" not in pp.get("en", ""):
        errors.append(f"{fid}: practicePassage missing [出典: ...]")
    if len(fp.get("practiceQuestions", [])) != 3:
        errors.append(f"{fid}: practiceQuestions != 3")
    if len(fp.get("practiceQuestionsSimple", [])) != 3:
        errors.append(f"{fid}: practiceQuestionsSimple != 3")
    af = pp.get("audioFile")
    if not audio_ok(af):
        errors.append(f"{fid}: missing audio {af}")
    sq = fp.get("sourceQuoteAudio")
    if not audio_ok(sq):
        errors.append(f"{fid}: missing sourceQuoteAudio {sq}")
    for j, ex in enumerate(fp.get("examples", [])):
        au = ex.get("audio")
        if not audio_ok(au):
            errors.append(f"{fid} ex{j+1}: missing audio {au}")
    search = corpus + " " + pp.get("en", "")
    for pat in fp.get("highlightPatterns", []):
        if pat not in search:
            errors.append(f"{fid}: highlight不在: {pat[:50]}")

serialized = json.dumps(d, ensure_ascii=False)
for stale in ("全部屋", "お兄ちゃんに親切", "おとうとにやさしく", "床で休んでいる"):
    if stale in serialized:
        errors.append(f"stale expression remains: {stale}")

full_history_sentence = (
    "When Kate and her father visited the hospital, they saw three novels, "
    "four history books, and two magazines around her grandmother's bed."
)
if len(fps) >= 4:
    fp4_en = fps[3].get("practicePassage", {}).get("en", "")
    if full_history_sentence not in fp4_en or "\nThey saw three novels" in fp4_en:
        errors.append("fp4: incomplete Kate's Story source quote")

print(f"focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan 4 focusPoints verified")
