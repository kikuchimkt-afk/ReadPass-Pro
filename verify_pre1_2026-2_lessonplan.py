# -*- coding: utf-8 -*-
"""Verify the five lesson focus points for Grade Pre-1 2026-2.

audioFile is optional until data/pre-grade1/2026-2/_gen_tts.py has been run;
pass --require-audio to also require every practice MP3 to exist.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "pre-grade1"
DATA_PATH = DATA_DIR / "2026-2" / "data.json"
EXPECTED_COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#f59e0b"]
EXPECTED_SOURCES = [
    "The Y2K Bug",
    "Searching for a Sixth Taste",
    "Employment Requirements for Welfare",
    "Saint Helena",
    "Saint Helena",
]
FP_KEYS = {
    "id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation", "examples",
    "practicePassage", "practiceQuestions", "highlightPatterns", "highlightColor", "highlightLabel",
}
BLANK_RE = re.compile(r"\(\s*\d+\s*\)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-audio", action="store_true", help="also require every practice MP3")
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
    if list(data.get("lessonPlan", {})) != ["focusPoints"]:
        errors.append("lessonPlan must contain only focusPoints")
    if len(focus_points) != 5:
        errors.append(f"focusPoints={len(focus_points)} != 5")

    corpus = " ".join(
        paragraph
        for section in data.get("sections", [])
        for passage in section.get("passages", [])
        for paragraph in passage.get("paragraphs", [])
    )

    audio_count = 0
    for index, focus_point in enumerate(focus_points, 1):
        prefix = f"fp{index}"
        if set(focus_point) != FP_KEYS:
            errors.append(f"{prefix}: keys={sorted(focus_point)}")
            continue
        if focus_point["id"] != prefix:
            errors.append(f"{prefix}: id={focus_point['id']!r}")
        for field in ("title", "subtitle", "explanation", "sourceQuote", "sourceLocation", "highlightLabel"):
            if not isinstance(focus_point[field], str) or not focus_point[field].strip():
                errors.append(f"{prefix}: empty {field}")
        if index < 5 and focus_point["sourceQuote"] not in corpus:
            errors.append(f"{prefix}: sourceQuote is not an exact exam-text substring")
        if focus_point["highlightColor"] != EXPECTED_COLORS[index - 1]:
            errors.append(f"{prefix}: highlightColor={focus_point['highlightColor']!r}")

        examples = focus_point["examples"]
        if len(examples) != 3 or any(set(e) != {"en", "ja", "note"} or not all(str(e[k]).strip() for k in e) for e in examples):
            errors.append(f"{prefix}: needs three complete examples (en/ja/note)")

        passage = focus_point["practicePassage"]
        if set(passage) not in ({"en", "ja"}, {"en", "ja", "audioFile"}):
            errors.append(f"{prefix}: practicePassage keys={sorted(passage)}")
        if not passage.get("en", "").startswith(f"[出典: {EXPECTED_SOURCES[index - 1]}]\n"):
            errors.append(f"{prefix}: practice passage source label differs")
        if len(passage.get("en", "")) < 250 or len(passage.get("ja", "")) < 120:
            errors.append(f"{prefix}: practice passage is too short")
        if BLANK_RE.search(passage.get("en", "")) or BLANK_RE.search(passage.get("ja", "")):
            errors.append(f"{prefix}: practice passage still contains an answer blank")
        expected_audio = f"audio/practice_pp{index}.mp3"
        if "audioFile" in passage:
            audio_count += 1
            if passage["audioFile"] != expected_audio:
                errors.append(f"{prefix}: audioFile={passage['audioFile']!r}")
            elif not (DATA_PATH.parent / expected_audio).is_file():
                errors.append(f"{prefix}: referenced audio file is missing")
        elif args.require_audio:
            errors.append(f"{prefix}: audioFile is missing (run _gen_tts.py)")

        questions = focus_point["practiceQuestions"]
        if len(questions) != 4 or any(set(q) != {"q", "a"} or not q["q"].strip() or not q["a"].strip() for q in questions):
            errors.append(f"{prefix}: needs four complete practiceQuestions")

        patterns = focus_point["highlightPatterns"]
        if not patterns:
            errors.append(f"{prefix}: no highlightPatterns")
        for pattern in patterns:
            if pattern not in corpus:
                errors.append(f"{prefix}: highlight not found in exam text: {pattern!r}")
            if pattern not in passage.get("en", ""):
                errors.append(f"{prefix}: highlight not found in its practice passage: {pattern!r}")

    if len(focus_points) == 5 and focus_points[4].get("title") != "今回の重要なパラフレーズ":
        errors.append("fp5: title must be 今回の重要なパラフレーズ")
    if audio_count not in (0, 5):
        errors.append(f"audioFile is set on {audio_count}/5 focus points; rerun _gen_tts.py")

    # Grammar topics must not repeat an earlier Pre-1 session.
    titles = {fp.get("title") for fp in focus_points[:4]}
    for other in sorted(DATA_DIR.iterdir()):
        other_path = other / "data.json"
        if other.name == "2026-2" or not other_path.is_file():
            continue
        other_data = json.loads(other_path.read_text(encoding="utf-8"))
        other_titles = {fp.get("title") for fp in other_data.get("lessonPlan", {}).get("focusPoints", [])[:4]}
        for duplicate in titles & other_titles:
            errors.append(f"focus point title duplicates {other.name}: {duplicate!r}")

    if errors:
        print(f"ERRORS={len(errors)}")
        for error in errors:
            print(f"  {error}")
        raise SystemExit(1)
    print(f"OK: 5 focus points, 15 examples, 20 practice questions (practice audio {audio_count}/5)")


if __name__ == "__main__":
    main()
