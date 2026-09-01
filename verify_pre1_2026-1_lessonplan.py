# -*- coding: utf-8 -*-
"""Verify the five 2025-format lesson focus points for Pre-1 2026-1."""

import json
import os
import sys


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "pre-grade1", "2026-1", "data.json")
EXPECTED_COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#f59e0b"]
EXPECTED_AUDIO = [f"audio/practice_pp{i}.mp3" for i in range(1, 6)]
REQUIRED_PRACTICE_EVIDENCE = [
    [
        ["as expected", "which did not fit the stereotype"],
        ["the differences for every birth position were extremely slight"],
        ["did lead to"],
        ["genetics", "living environment"],
    ],
    [
        ["these measures may be useless in the long term", "turning to technology instead"],
        ["Sea barriers have been built", "raised land"],
        ["Along with preserving geographical features"],
        ["defined territory", "permanent population", "virtual form"],
    ],
    [
        ["began life as a village", "create a surplus", "could then be traded"],
        ["which could then be traded"],
        ["including technological advancements", "such as the construction"],
        ["cuneiform script", "accounting and general administrative matters", "helped facilitate the governance"],
    ],
    [
        ["performance on cognitive tests was superior", "smaller digestive systems", "fewer offspring"],
        ["this in turn seems", "fewer offspring"],
        ["beyond the individual animals to entire populations"],
        ["FOXP2", "This research is preliminary, however", "a multitude of genes"],
    ],
    [
        ["withholding animal uplift is itself unethical", "sacrificed as test subjects"],
        ["in light of increased awareness of animal rights", "given the tremendous role"],
        ["just as unethical as withholding them from a group of humans", "lack sufficient wealth"],
        ["if humans artificially increase our own intelligence", "animals will likely be sacrificed", "withholding advances"],
    ],
]
FP_KEYS = {
    "id",
    "title",
    "subtitle",
    "explanation",
    "sourceQuote",
    "sourceLocation",
    "examples",
    "practicePassage",
    "practiceQuestions",
    "highlightPatterns",
    "highlightColor",
    "highlightLabel",
}

with open(DATA_PATH, encoding="utf-8") as handle:
    data = json.load(handle)

errors = []
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"focusPoints={len(focus_points)} != 5")

corpus = " ".join(
    paragraph
    for section in data.get("sections", [])
    for passage in section.get("passages", [])
    for paragraph in passage.get("paragraphs", [])
)

for index, focus_point in enumerate(focus_points, 1):
    prefix = f"fp{index}"
    if set(focus_point) != FP_KEYS:
        errors.append(f"{prefix}: keys={sorted(focus_point)}")
    if focus_point.get("id") != prefix:
        errors.append(f"{prefix}: id={focus_point.get('id')!r}")
    for field in (
        "title",
        "subtitle",
        "explanation",
        "sourceQuote",
        "sourceLocation",
        "highlightLabel",
    ):
        if not isinstance(focus_point.get(field), str) or not focus_point[field].strip():
            errors.append(f"{prefix}: empty {field}")
    if index < 5 and focus_point.get("sourceQuote") not in corpus:
        errors.append(f"{prefix}: sourceQuote is not an exact exam-text substring")
    if focus_point.get("highlightColor") != EXPECTED_COLORS[index - 1]:
        errors.append(f"{prefix}: highlightColor={focus_point.get('highlightColor')!r}")

    examples = focus_point.get("examples", [])
    if len(examples) != 3:
        errors.append(f"{prefix}: examples={len(examples)} != 3")
    for example_index, example in enumerate(examples, 1):
        if set(example) != {"en", "ja", "note"}:
            errors.append(f"{prefix} example{example_index}: invalid keys")
        if any(not isinstance(example.get(key), str) or not example[key].strip() for key in ("en", "ja", "note")):
            errors.append(f"{prefix} example{example_index}: empty field")

    passage = focus_point.get("practicePassage", {})
    if set(passage) != {"en", "ja", "audioFile"}:
        errors.append(f"{prefix}: practicePassage keys={sorted(passage)}")
    if not passage.get("en", "").startswith("[出典: "):
        errors.append(f"{prefix}: practice passage has no source label")
    if len(passage.get("en", "")) < 250 or len(passage.get("ja", "")) < 120:
        errors.append(f"{prefix}: practice passage is too short")
    if passage.get("audioFile") != EXPECTED_AUDIO[index - 1]:
        errors.append(f"{prefix}: audioFile={passage.get('audioFile')!r}")
    for question_index, evidence_group in enumerate(REQUIRED_PRACTICE_EVIDENCE[index - 1], 1):
        for evidence in evidence_group:
            if evidence not in passage.get("en", ""):
                errors.append(
                    f"{prefix} question{question_index}: required practice evidence is missing: {evidence!r}"
                )

    questions = focus_point.get("practiceQuestions", [])
    if len(questions) != 4:
        errors.append(f"{prefix}: practiceQuestions={len(questions)} != 4")
    for question_index, question in enumerate(questions, 1):
        if set(question) != {"q", "a"}:
            errors.append(f"{prefix} question{question_index}: invalid keys")
        if any(not isinstance(question.get(key), str) or not question[key].strip() for key in ("q", "a")):
            errors.append(f"{prefix} question{question_index}: empty q/a")

    patterns = focus_point.get("highlightPatterns", [])
    if len(patterns) < 1:
        errors.append(f"{prefix}: no highlightPatterns")
    for pattern in patterns:
        if pattern not in corpus:
            errors.append(f"{prefix}: highlight not found in exam text: {pattern!r}")
        if pattern not in passage.get("en", ""):
            errors.append(f"{prefix}: highlight not found in its practice passage: {pattern!r}")

if len(focus_points) == 5 and focus_points[4].get("title") != "今回の重要なパラフレーズ":
    errors.append("fp5: title must match the 2025 format")
if len(focus_points) == 5:
    fp2_answer = focus_points[1].get("practiceQuestions", [{}, {}, {}, {}])[3].get("a", "")
    if "明確に定められた領土と定住人口" not in fp2_answer:
        errors.append("fp2: statehood terminology must use 明確に定められた領土と定住人口")
    fp5_quote = focus_points[4].get("sourceQuote", "")
    if "increase our obligation to uplift them" not in fp5_quote or "share the advance" in fp5_quote:
        errors.append("fp5: Q31 paraphrase does not preserve the obligation logic")
    if "produce more food than it needed" not in fp5_quote or "immediately needed" in fp5_quote:
        errors.append("fp5: Q25 paraphrase must exactly preserve the official choice")
    fp5_questions = focus_points[4].get("practiceQuestions", [{}, {}, {}, {}])
    fp5_answers = " ".join(question.get("a", "") for question in fp5_questions)
    for concept in ("動物の権利", "人間の集団", "利用・犠牲"):
        if concept not in fp5_answers:
            errors.append(f"fp5: self-contained ethics practice is missing {concept!r}")

if errors:
    print(f"ERRORS={len(errors)}")
    for error in errors:
        print(f"  {error}")
    raise SystemExit(1)

print("OK: 5 focus points, 15 examples, 20 practice questions")
