# -*- coding: utf-8 -*-
"""Comprehensive audit for ReadPass Grade Pre-1 2026-1."""

import json
import hashlib
import os
import re
import sys


sys.stdout.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(REPO, "data", "pre-grade1", "2026-1")
DATA_PATH = os.path.join(BASE, "data.json")
TOP_PATH = os.path.join(REPO, "top.js")
TTS_MANIFEST_PATH = os.path.join(BASE, "audio", "tts_manifest.json")
TTS_VOICE = "en-US-JennyNeural"
TTS_RATE = "-15%"
EXPECTED_SOURCE_SHA256 = "B1100C7AC94A5496BEB66CC3C7E7AFEAF11EC46E1351279CD805E56A6208D6C6"
OFFICIAL = [
    2, 3, 4, 2, 2, 4, 3, 3, 1, 4, 1, 4, 1, 3, 3, 1, 1, 4,
    2, 3, 1, 4, 1, 3, 2, 4, 1, 2, 3, 1, 4,
]
EXPECTED_KEYS = [
    "grade",
    "year",
    "session",
    "title",
    "vocabulary",
    "sections",
    "lessonPlan",
]
EXPECTED_SECTION_META = [
    ("大問1", "Part 1", "vocabulary"),
    ("大問2", "Part 2", "passage-fill"),
    ("大問3", "Part 3", "reading-comprehension"),
]


def normalized(text):
    return re.sub(r"\s+", " ", text or "").strip()


def tts_signature(text):
    payload = json.dumps(
        {"rate": TTS_RATE, "text": text, "voice": TTS_VOICE},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def mp3_stats(path):
    """Return (frame count, approximate duration) for valid MPEG Layer III frames."""
    with open(path, "rb") as handle:
        payload = handle.read()
    offset = 0
    if payload.startswith(b"ID3") and len(payload) >= 10:
        tag_size = sum((payload[6 + index] & 0x7F) << (21 - 7 * index) for index in range(4))
        offset = 10 + tag_size
    bitrate_mpeg1 = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0]
    bitrate_mpeg2 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]
    sample_rates = {
        3: [44100, 48000, 32000],
        2: [22050, 24000, 16000],
        0: [11025, 12000, 8000],
    }
    frames = 0
    duration = 0.0
    while offset + 4 <= len(payload):
        header = int.from_bytes(payload[offset : offset + 4], "big")
        if (header >> 21) & 0x7FF != 0x7FF:
            offset += 1
            continue
        version = (header >> 19) & 0x3
        layer = (header >> 17) & 0x3
        bitrate_index = (header >> 12) & 0xF
        sample_rate_index = (header >> 10) & 0x3
        padding = (header >> 9) & 0x1
        if version == 1 or layer != 1 or bitrate_index in (0, 15) or sample_rate_index == 3:
            offset += 1
            continue
        bitrate = (bitrate_mpeg1 if version == 3 else bitrate_mpeg2)[bitrate_index]
        sample_rate = sample_rates[version][sample_rate_index]
        coefficient = 144000 if version == 3 else 72000
        samples_per_frame = 1152 if version == 3 else 576
        frame_length = int(coefficient * bitrate / sample_rate + padding)
        if frame_length <= 4 or offset + frame_length > len(payload):
            offset += 1
            continue
        frames += 1
        duration += samples_per_frame / sample_rate
        offset += frame_length
    return frames, duration


def collect_questions(data):
    questions = []
    for section in data.get("sections", []):
        for question in section.get("questions", []):
            questions.append((section, None, question))
        for passage in section.get("passages", []):
            for question in passage.get("questions", []):
                questions.append((section, passage, question))
    return questions


def source_payload(data):
    sections = data.get("sections", [])
    if len(sections) != 3:
        return {}
    return {
        "section1": [
            {"number": question.get("number"), "text": question.get("text"), "choices": question.get("choices")}
            for question in sections[0].get("questions", [])
        ],
        "section2": [
            {
                "title": passage.get("title"),
                "paragraphs": passage.get("paragraphs"),
                "questions": [
                    {"number": question.get("number"), "choices": question.get("choices")}
                    for question in passage.get("questions", [])
                ],
            }
            for passage in sections[1].get("passages", [])
        ],
        "section3": [
            {
                "title": passage.get("title"),
                "paragraphs": passage.get("paragraphs"),
                "questions": [
                    {
                        "number": question.get("number"),
                        "question": question.get("question"),
                        "choices": question.get("choices"),
                    }
                    for question in passage.get("questions", [])
                ],
            }
            for passage in sections[2].get("passages", [])
        ],
    }


with open(DATA_PATH, encoding="utf-8") as handle:
    data = json.load(handle)

errors = []
warnings = []

canonical_source = json.dumps(
    source_payload(data),
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
actual_source_sha256 = hashlib.sha256(canonical_source).hexdigest().upper()
if actual_source_sha256 != EXPECTED_SOURCE_SHA256:
    errors.append(
        f"official source payload hash={actual_source_sha256} expected={EXPECTED_SOURCE_SHA256}"
    )

if list(data) != EXPECTED_KEYS:
    errors.append(f"top-level keys/order={list(data)}")
for key, expected in {
    "grade": "準1級",
    "year": "2026",
    "session": "1",
    "title": "2026年度 第1回 英語資格検定準1級 リーディング",
}.items():
    if data.get(key) != expected:
        errors.append(f"metadata {key}={data.get(key)!r} != {expected!r}")
if "listening" in data:
    errors.append("ReadPass Pre-1 2025 format has no top-level listening object")

section_meta = [
    (section.get("name"), section.get("nameEn"), section.get("type"))
    for section in data.get("sections", [])
]
if section_meta != EXPECTED_SECTION_META:
    errors.append(f"section metadata/order={section_meta}")

all_questions = collect_questions(data)
numbers = [question.get("number") for _, _, question in all_questions]
if numbers != list(range(1, 32)):
    errors.append(f"question order={numbers}")
for section, passage, question in all_questions:
    number = question.get("number")
    if not isinstance(number, int) or not 1 <= number <= 31:
        errors.append(f"invalid question number={number!r}")
        continue
    if question.get("answer") != OFFICIAL[number - 1]:
        errors.append(
            f"Q{number}: answer={question.get('answer')} official={OFFICIAL[number - 1]}"
        )
    for field in ("choices", "choiceAnalysis"):
        if len(question.get(field, [])) != 4:
            errors.append(f"Q{number}: {field} count={len(question.get(field, []))}")
    analyses = question.get("choiceAnalysis", [])
    if len(analyses) == 4:
        answer_index = question["answer"] - 1
        for index, analysis in enumerate(analyses):
            expected_marker = "✅" if index == answer_index else "❌"
            if not isinstance(analysis, str) or not analysis.startswith(expected_marker):
                errors.append(f"Q{number}: analysis {index + 1} must start {expected_marker}")
        if "→ 正解。💡" not in analyses[answer_index] and "→正解。💡" not in analyses[answer_index]:
            errors.append(f"Q{number}: correct analysis has no 2025-format answer marker")

    if section.get("type") == "vocabulary":
        for field in ("text", "translation", "grammar"):
            if not isinstance(question.get(field), str) or not question[field].strip():
                errors.append(f"Q{number}: empty {field}")
        blank_pattern = rf"\(\s*{number}\s*\)"
        if len(re.findall(blank_pattern, question.get("text", ""))) != 1:
            errors.append(f"Q{number}: English numbered blank count is not one")
        if len(re.findall(blank_pattern, question.get("translation", ""))) != 1:
            errors.append(f"Q{number}: Japanese numbered blank count is not one")
    else:
        if len(question.get("choiceTranslations", [])) != 4:
            errors.append(f"Q{number}: choiceTranslations count")
        evidence = question.get("sourceEvidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"Q{number}: sourceEvidence missing")
        elif passage:
            corpus = " ".join(passage.get("paragraphs", []))
            for phrase in evidence:
                if phrase not in corpus:
                    errors.append(f"Q{number}: evidence is not an exact source substring: {phrase!r}")
        if section.get("type") == "reading-comprehension":
            for field in ("question", "questionTranslation"):
                if not isinstance(question.get(field), str) or not question[field].strip():
                    errors.append(f"Q{number}: empty {field}")

pair_count = 0
blank_pair_count = 0
for section in data.get("sections", []):
    for passage in section.get("passages", []):
        title = passage.get("title", "(untitled)")
        paragraphs = passage.get("paragraphs", [])
        translations = passage.get("translations", [])
        pairs = passage.get("sentencePairs", [])
        if len(paragraphs) != len(translations) or not all(translations):
            errors.append(f"{title}: paragraph/translation count or emptiness")
        if not pairs:
            errors.append(f"{title}: sentencePairs missing")
            continue
        pair_english = []
        corpus = " ".join(paragraphs)
        for index, pair in enumerate(pairs, 1):
            pair_count += 1
            if not isinstance(pair, list) or len(pair) not in (2, 4):
                errors.append(f"{title} pair{index}: expected 2 or 4 elements")
                continue
            if not all(isinstance(value, str) and value.strip() for value in pair):
                errors.append(f"{title} pair{index}: empty/non-string element")
                continue
            english = pair[0]
            pair_english.append(english)
            if english not in corpus:
                errors.append(f"{title} pair{index}: English is not in passage")
            blank = bool(re.search(r"\(\s*\d+\s*\)", english))
            if blank:
                blank_pair_count += 1
            if blank != (len(pair) == 2):
                errors.append(f"{title} pair{index}: only blank sentences may use 2 elements")
            if len(pair) == 4:
                slash_segments = pair[2].split("||")
                if not slash_segments or any(segment.count("|") != 1 for segment in slash_segments):
                    errors.append(f"{title} pair{index}: invalid slash format")
                else:
                    slash_english = " ".join(segment.split("|", 1)[0] for segment in slash_segments)
                    if normalized(slash_english) != normalized(english):
                        errors.append(f"{title} pair{index}: slash English differs from source")
                main_verb_matches = list(re.finditer(re.escape(pair[3]), english, re.IGNORECASE))
                if len(main_verb_matches) != 1:
                    errors.append(f"{title} pair{index}: main verb is ambiguous")
                if not re.search(rf"(?<!\w){re.escape(pair[3])}(?!\w)", english, re.IGNORECASE):
                    errors.append(f"{title} pair{index}: main verb has no word-boundary match")
        if normalized(" ".join(pair_english)) != normalized(corpus):
            errors.append(f"{title}: sentencePairs do not cover the complete passage")

if blank_pair_count != 6:
    errors.append(f"blank sentencePairs={blank_pair_count} != 6")

vocabulary = data.get("vocabulary", [])
if len(vocabulary) != 80:
    errors.append(f"vocabulary={len(vocabulary)} != 80")
words = [item.get("word") for item in vocabulary]
if len(set(words)) != 80:
    errors.append("vocabulary words are not unique")
referenced_audio = []
expected_tts_inputs = {}
for index, item in enumerate(vocabulary, 1):
    if set(item) != {
        "word", "meaning", "pos", "level", "example", "distractors", "wordAudio", "exampleJa"
    }:
        errors.append(f"vocab {index}: invalid keys")
    for field in ("word", "meaning", "pos", "example", "wordAudio", "exampleJa"):
        if not isinstance(item.get(field), str) or not item[field].strip():
            errors.append(f"vocab {index}: empty {field}")
    if item.get("level") != "準1級":
        errors.append(f"vocab {index}: level={item.get('level')!r}")
    distractors = item.get("distractors", [])
    if len(distractors) != 3 or len(set(distractors)) != 3 or item.get("meaning") in distractors:
        errors.append(f"vocab {index}: invalid distractors")
    expected_prefix = f"audio/vocab/w_{index:03d}_"
    if not item.get("wordAudio", "").startswith(expected_prefix):
        errors.append(f"vocab {index}: non-deterministic audio path")
    referenced_audio.append(item.get("wordAudio", ""))
    expected_tts_inputs[item.get("wordAudio", "")] = tts_signature(item.get("word", ""))

focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"focusPoints={len(focus_points)} != 5")
for index, focus_point in enumerate(focus_points, 1):
    if len(focus_point.get("examples", [])) != 3:
        errors.append(f"fp{index}: examples != 3")
    if len(focus_point.get("practiceQuestions", [])) != 4:
        errors.append(f"fp{index}: practiceQuestions != 4")
    audio = focus_point.get("practicePassage", {}).get("audioFile", "")
    if audio != f"audio/practice_pp{index}.mp3":
        errors.append(f"fp{index}: audio path={audio!r}")
    referenced_audio.append(audio)
    practice_english = re.sub(
        r"\[出典:.*?\]\s*",
        "",
        focus_point.get("practicePassage", {}).get("en", ""),
        count=1,
    ).strip()
    expected_tts_inputs[audio] = tts_signature(practice_english)

if len(referenced_audio) != 85 or len(set(referenced_audio)) != 85:
    errors.append("audio references are not exactly 85 unique paths")
for relative_path in referenced_audio:
    path = os.path.join(BASE, *relative_path.split("/"))
    if not os.path.isfile(path) or os.path.getsize(path) < 500:
        errors.append(f"missing/small audio: {relative_path}")
        continue
    frames, duration = mp3_stats(path)
    if frames < 2 or duration < 0.05:
        errors.append(f"invalid/undecodable MP3 frames: {relative_path}")

expected_tts_manifest = {}
for relative_path, input_sha256 in expected_tts_inputs.items():
    path = os.path.join(BASE, *relative_path.split("/"))
    if os.path.isfile(path):
        with open(path, "rb") as handle:
            audio_sha256 = hashlib.sha256(handle.read()).hexdigest()
    else:
        audio_sha256 = None
    expected_tts_manifest[relative_path] = {
        "audioSha256": audio_sha256,
        "inputSha256": input_sha256,
    }

try:
    with open(TTS_MANIFEST_PATH, encoding="utf-8") as handle:
        actual_tts_manifest = json.load(handle)
except (FileNotFoundError, json.JSONDecodeError):
    actual_tts_manifest = None
if actual_tts_manifest != expected_tts_manifest:
    errors.append("TTS manifest does not exactly match text, voice, rate, and audio paths")

actual_audio = []
audio_root = os.path.join(BASE, "audio")
if os.path.isdir(audio_root):
    for root, _, filenames in os.walk(audio_root):
        for filename in filenames:
            if filename.lower().endswith(".mp3"):
                actual_audio.append(os.path.relpath(os.path.join(root, filename), BASE).replace("\\", "/"))
if set(actual_audio) != set(referenced_audio):
    errors.append(
        f"audio tree/reference mismatch actual={len(actual_audio)} referenced={len(referenced_audio)}"
    )

with open(TOP_PATH, encoding="utf-8") as handle:
    top_js = handle.read()
pre1_start = top_js.find("id: 'pre-grade1'")
grade2_start = top_js.find("id: 'grade2'", pre1_start)
pre1_catalog = top_js[pre1_start:grade2_start]
catalog_entry = "{ id: '2026-1', label: '2026年度 第1回', sub: '一次試験リーディング' }"
if pre1_catalog.count(catalog_entry) != 1:
    errors.append("top.js Pre-1 2026-1 catalog entry is missing or duplicated")

if errors:
    print(f"ERRORS={len(errors)} WARNINGS={len(warnings)}")
    for error in errors:
        print(f"  ERROR: {error}")
    for warning in warnings:
        print(f"  WARN: {warning}")
    raise SystemExit(1)

print(
    "OK: Pre-1 2026-1 comprehensive audit "
    f"(31 questions, 80 vocabulary, 5 focus points, {pair_count} sentence pairs, 85 audio)"
)
