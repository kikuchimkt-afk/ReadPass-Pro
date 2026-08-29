# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 Focus Practiceの出典・構造・音声を検証。"""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

base = Path(__file__).resolve().parent / "data" / "grade-pre2" / "2026-1-sat"
data = json.loads((base / "data.json").read_text(encoding="utf-8"))
errors = []
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])

if [fp.get("id") for fp in focus_points] != ["fp1", "fp2", "fp3", "fp4", "fp5"]:
    errors.append("focus ids must be fp1..fp5")

fp1 = next((fp for fp in focus_points if fp.get("id") == "fp1"), {})
if "一区切り" not in fp1.get("explanation", ""):
    errors.append("fp1: In the end must be explained as the search's interim conclusion")
if "物語の結末" in fp1.get("explanation", ""):
    errors.append("fp1: stale whole-story conclusion wording remains")

passages = [p for sec in data["sections"] for p in sec.get("passages", [])]
filled_corpus = " ".join(" ".join(p["paragraphs"]) for p in passages)
filled_corpus = filled_corpus.replace("Max ( 21 ).", "Max did everything that he could.")
filled_corpus = filled_corpus.replace("Max was ( 22 ).", "Max was surprised to hear that.")

required = (
    "id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
    "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
    "highlightColor", "highlightLabel",
)
for fp in focus_points:
    fid = fp.get("id", "?")
    for key in required:
        if not fp.get(key):
            errors.append(f"{fid}: missing {key}")
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    if not en.startswith("[出典:") or not pp.get("ja"):
        errors.append(f"{fid}: source tag/Japanese missing")
    for line in en.splitlines():
        if not line or line.startswith("[出典:"):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            if sentence and sentence not in filled_corpus:
                errors.append(f"{fid}: practice English not in source: {sentence[:50]!r}")
    for pattern in fp.get("highlightPatterns", []):
        if pattern not in en:
            errors.append(f"{fid}: missing highlight pattern {pattern!r}")
    if len(fp.get("examples", [])) < 3:
        errors.append(f"{fid}: examples < 3")
    questions = fp.get("practiceQuestions", [])
    if len(questions) < 4:
        errors.append(f"{fid}: practiceQuestions < 4")
    for qa in questions:
        if not qa.get("q") or not qa.get("a"):
            errors.append(f"{fid}: empty practice question/answer")
        if "避え" in qa.get("a", ""):
            errors.append(f"{fid}: typo 避え")
    audio_ref = pp.get("audioFile", "")
    audio_path = base / Path(audio_ref.replace("/", os.sep))
    if not audio_ref.endswith(".mp3") or not audio_path.is_file() or audio_path.stat().st_size < 500:
        errors.append(f"{fid}: invalid audio {audio_ref}")

print(f"lessonPlan focusPoints={len(focus_points)} errors={len(errors)}")
for error in errors:
    print(" ", error)
sys.exit(1 if errors else 0)
