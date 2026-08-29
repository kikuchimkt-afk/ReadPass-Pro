# -*- coding: utf-8 -*-
"""2026-1-sat 2級の原本・正答・解説・対訳・語彙・教材・音声監査。"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data" / "grade2" / "2026-1-sat"
DATA = BASE / "data.json"
SOURCE_ROOT = Path(r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）")
SOURCE_PROBLEM = SOURCE_ROOT / "2級.pdf"
SOURCE_ANSWER = SOURCE_ROOT / "解答" / "2級_解答.pdf"
SOURCE_AUDIO = SOURCE_ROOT / "2026-1_音源" / "2級"

SOURCE_HASHES = {
    SOURCE_PROBLEM: "5DA294C30399816177842451B145FB9A3FF37D6433779632090F840D108176E9",
    SOURCE_ANSWER: "181BA8E0D0283680CA8A0160E92E9A22D3BF1E6E993F27E5EC20C944FD2F925B",
}

OFFICIAL_READING = {
    1: 3, 2: 2, 3: 3, 4: 3, 5: 1, 6: 3, 7: 3, 8: 1, 9: 4, 10: 3,
    11: 3, 12: 3, 13: 4, 14: 2, 15: 3, 16: 1, 17: 1,
    18: 4, 19: 2, 20: 3, 21: 1, 22: 4, 23: 3,
    24: 4, 25: 1, 26: 3, 27: 1, 28: 3, 29: 4, 30: 2, 31: 1,
}

OFFICIAL_LISTENING = {
    "part1": {str(i): answer for i, answer in enumerate(
        [4, 4, 1, 1, 4, 4, 4, 3, 3, 2, 4, 1, 1, 1, 4], start=1)},
    "part2": {str(i): answer for i, answer in enumerate(
        [1, 2, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 4, 2, 1], start=16)},
}

# Section名・instruction・英文・選択肢・正答・長文原文だけを固定した値。
IMMUTABLE_SOURCE_SHA256 = "208ef43555f0339d270505a76d76b1ddd92d3b53ab5991189fa44479f71b6240"

EXPECTED_PASSAGES = {
    "Child-Friendly City": (3, 15),
    "Dead Trees": (3, 19),
    "Inquiry about the factory": (4, 14),
    "The Lost City": (4, 20),
}

EXPECTED_VOCAB_WORDS = [
    "incident", "argument", "outcome", "quantity", "sacrifice", "stir",
    "resemble", "favor", "cable", "appreciation", "preference", "scold",
    "detect", "estimate", "decline", "neglect", "patiently", "current",
    "up until now", "needless to say", "lose one's temper",
    "keep one's fingers crossed", "confident of", "keep to", "effect on",
    "effort", "surround", "trial", "permanently", "indicate", "observation",
    "urban", "improvement", "reflect", "community", "ban", "habitat",
    "creature", "absorb", "substance", "moisture", "eventually", "bark",
    "element", "maintain", "cycle", "manufacturing", "impress", "research",
    "permit", "consideration", "conveniently", "restore", "ancient", "collapse",
    "gradually", "investigation", "sculpture", "underwater", "explore", "ruins",
]

KEY_VOCAB = {
    "favor": ("好む、支持する", "動詞"),
    "up until now": ("今まで、これまでずっと", "熟語"),
    "needless to say": ("言うまでもなく", "熟語"),
    "lose one's temper": ("かっとなる、怒りを抑えられなくなる", "熟語"),
    "keep one's fingers crossed": ("幸運を祈る、うまくいくよう願う", "熟語"),
    "confident of": ("〜に自信がある", "熟語"),
    "keep to": ("〜に従う、〜から離れない", "句動詞"),
    "effect on": ("〜への影響", "熟語"),
    "observation": ("観察、意見", "名詞"),
    "habitat": ("生息地", "名詞"),
    "moisture": ("湿気、水分", "名詞"),
    "manufacturing": ("製造、製造業", "名詞"),
    "permit": ("許可する", "動詞"),
    "conveniently": ("便利に、都合よく", "副詞"),
    "gradually": ("徐々に、だんだんと", "副詞"),
    "underwater": ("水中の、海中の", "形容詞"),
    "ruins": ("遺跡、廃墟", "名詞"),
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def source_payload(data: dict) -> list[dict]:
    payload = []
    for section in data["sections"]:
        item = {
            "name": section["name"],
            "nameEn": section["nameEn"],
            "type": section["type"],
            "instruction": section["instruction"],
        }
        if "questions" in section:
            item["questions"] = [
                {
                    "number": question["number"],
                    "text": question["text"],
                    "choices": question["choices"],
                    "answer": question["answer"],
                }
                for question in section["questions"]
            ]
        if "passages" in section:
            item["passages"] = [
                {
                    "label": passage.get("label"),
                    "title": passage["title"],
                    "format": passage.get("format"),
                    "meta": passage.get("meta"),
                    "paragraphs": passage["paragraphs"],
                    "questions": [
                        {
                            "number": question["number"],
                            "question": question.get("question"),
                            "choices": question["choices"],
                            "answer": question["answer"],
                        }
                        for question in passage["questions"]
                    ],
                }
                for passage in section["passages"]
            ]
        payload.append(item)
    return payload


def collect_questions(data: dict) -> list[tuple[dict, str | None, str | None]]:
    out = []
    for section in data.get("sections", []):
        out.extend((question, None, None) for question in section.get("questions", []))
        for passage in section.get("passages", []):
            corpus = " ".join(passage.get("paragraphs", []))
            translation = " ".join(passage.get("translations", []))
            out.extend((question, corpus, translation) for question in passage.get("questions", []))
    return out


data = json.loads(DATA.read_text(encoding="utf-8"))
errors: list[str] = []
notes: list[str] = []

for source_path, expected_hash in SOURCE_HASHES.items():
    if source_path.is_file():
        actual_hash = sha256_file(source_path)
        if actual_hash != expected_hash:
            errors.append(f"[原本] {source_path.name}: SHA256={actual_hash} expected={expected_hash}")
        else:
            notes.append(f"[原本] {source_path.name}: SHA256一致")
    else:
        notes.append(f"[原本] ローカル原本なし（スキップ）: {source_path}")

for key in ("grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan", "listening"):
    if key not in data:
        errors.append(f"[構造] missing {key}")
if (data.get("grade"), data.get("year"), data.get("session")) != ("2級", "2026", "1-sat"):
    errors.append("[構造] grade/year/session mismatch")

expected_sections = [
    ("大問1", "vocabulary", 17, 0),
    ("大問2", "passage-fill", 0, 2),
    ("大問3", "reading-comprehension", 0, 2),
]
if len(data.get("sections", [])) != len(expected_sections):
    errors.append(f"[構造] sections={len(data.get('sections', []))} != 3")
else:
    for section, (name, kind, questions, passages) in zip(data["sections"], expected_sections):
        if (section.get("name"), section.get("type")) != (name, kind):
            errors.append(f"[構造] {name}: name/type mismatch")
        if len(section.get("questions", [])) != questions:
            errors.append(f"[構造] {name}: direct question count")
        if len(section.get("passages", [])) != passages:
            errors.append(f"[構造] {name}: passage count")
        if not section.get("instruction"):
            errors.append(f"[構造] {name}: instruction missing")

payload_bytes = json.dumps(
    source_payload(data), ensure_ascii=False, separators=(",", ":")
).encode("utf-8")
payload_hash = hashlib.sha256(payload_bytes).hexdigest()
if payload_hash != IMMUTABLE_SOURCE_SHA256:
    errors.append(
        f"[原文不変] source payload SHA256={payload_hash} expected={IMMUTABLE_SOURCE_SHA256}"
    )

all_questions = collect_questions(data)
numbers = [question["number"] for question, _, _ in all_questions]
if numbers != list(range(1, 32)):
    errors.append(f"[設問] numbers={numbers}")

analysis_lengths = []
for question, corpus, passage_translation in all_questions:
    number = question["number"]
    if question.get("answer") != OFFICIAL_READING[number]:
        errors.append(f"[正答] Q{number}: {question.get('answer')} != {OFFICIAL_READING[number]}")
    if len(question.get("choices", [])) != 4 or len(question.get("choiceTranslations", [])) != 4:
        errors.append(f"[選択肢] Q{number}: choices/choiceTranslations != 4")
    if not question.get("grammar", "").startswith("💡"):
        errors.append(f"[文法] Q{number}: missing or unmarked grammar")
    analyses = question.get("choiceAnalysis", [])
    if len(analyses) != 4:
        errors.append(f"[解説] Q{number}: choiceAnalysis={len(analyses)} != 4")
        continue
    analysis_lengths.extend(map(len, analyses))
    for choice, analysis in enumerate(analyses, 1):
        if analysis.startswith(("✅", "❌", "○")):
            errors.append(f"[marker] Q{number} choice{choice}: leading marker forbidden")
        has_correct = "→正解。💡" in analysis
        if has_correct != (choice == question["answer"]):
            errors.append(f"[marker] Q{number} choice{choice}: correct marker mismatch")

    if number <= 17:
        if not question.get("text") or not question.get("translation"):
            errors.append(f"[対訳] Q{number}: text/translation missing")
        if f"( {number} )" not in question.get("text", ""):
            errors.append(f"[空所] Q{number}: English blank missing")
        if f"( {number} )" not in question.get("translation", ""):
            errors.append(f"[空所] Q{number}: Japanese blank missing")
    elif number <= 23:
        if f"( {number} )" not in (corpus or ""):
            errors.append(f"[空所] Q{number}: passage English blank missing")
        if f"( {number} )" not in (passage_translation or ""):
            errors.append(f"[空所] Q{number}: passage Japanese blank missing")
    else:
        if not question.get("question") or not question.get("questionTranslation"):
            errors.append(f"[設問対訳] Q{number}: missing")

    if number >= 18:
        evidence = question.get("sourceEvidence", [])
        if not evidence:
            errors.append(f"[根拠] Q{number}: sourceEvidence missing")
        for phrase in evidence:
            if not corpus or phrase not in corpus:
                errors.append(f"[根拠] Q{number}: not in source: {phrase!r}")

if analysis_lengths:
    average = sum(analysis_lengths) / len(analysis_lengths)
    if average > 65:
        errors.append(f"[簡潔性] choiceAnalysis average={average:.1f} > 65")
    if max(analysis_lengths) > 120:
        errors.append(f"[簡潔性] choiceAnalysis max={max(analysis_lengths)} > 120")

passages = [passage for section in data["sections"] for passage in section.get("passages", [])]
if {passage["title"] for passage in passages} != set(EXPECTED_PASSAGES):
    errors.append("[長文] passage titles mismatch")
no_main_verb_english = {
    "Dear James White,",
    "Sincerely,\nJessica Jenkins\nRiverstone High School",
}
for passage in passages:
    title = passage["title"]
    expected_paragraphs, expected_pairs = EXPECTED_PASSAGES[title]
    if len(passage.get("paragraphs", [])) != expected_paragraphs:
        errors.append(f"[長文] {title}: paragraph count")
    if len(passage.get("translations", [])) != expected_paragraphs:
        errors.append(f"[長文] {title}: translation count")
    pairs = passage.get("sentencePairs", [])
    if len(pairs) != expected_pairs:
        errors.append(f"[長文] {title}: sentencePairs={len(pairs)} != {expected_pairs}")
    for index, pair in enumerate(pairs, 1):
        if (
            not isinstance(pair, list)
            or len(pair) != 4
            or not all(isinstance(field, str) for field in pair)
            or not all(pair[:3])
        ):
            errors.append(f"[長文] {title}: invalid pair {index}")
            continue
        slash_english = []
        slash_chunks = pair[2].split("||")
        if len(slash_chunks) < 2:
            errors.append(f"[長文] {title}: pair {index} slash needs multiple units")
        for chunk_index, chunk in enumerate(slash_chunks, 1):
            if chunk.count("|") != 1:
                errors.append(
                    f"[長文] {title}: pair {index} slash chunk {chunk_index} invalid"
                )
                continue
            english_unit, japanese_unit = chunk.split("|", 1)
            if not english_unit.strip() or not japanese_unit.strip():
                errors.append(
                    f"[長文] {title}: pair {index} slash chunk {chunk_index} empty"
                )
            slash_english.append(english_unit)
        if compact(" ".join(slash_english)) != compact(pair[0]):
            errors.append(f"[長文] {title}: pair {index} slash English mismatch")
        if pair[0] in no_main_verb_english:
            if pair[3] != "":
                errors.append(
                    f"[長文] {title}: pair {index} non-sentence main verb must be empty"
                )
        elif not pair[3] or not re.search(
            r"(?<![A-Za-z0-9])" + re.escape(pair[3]) + r"(?![A-Za-z0-9])",
            pair[0],
        ):
            errors.append(
                f"[長文] {title}: pair {index} main verb/phrase token mismatch"
            )
    pair_en = compact(" ".join(pair[0] for pair in pairs if len(pair) >= 2))
    source_en = compact(" ".join(passage.get("paragraphs", [])))
    if pair_en != source_en:
        errors.append(f"[長文] {title}: English sentencePairs not full/ordered")
    pair_ja = compact(" ".join(pair[1] for pair in pairs if len(pair) >= 2))
    source_ja = compact(" ".join(passage.get("translations", [])))
    if pair_ja != source_ja:
        errors.append(f"[長文] {title}: Japanese sentencePairs not full/ordered")

email = next((passage for passage in passages if passage["title"] == "Inquiry about the factory"), {})
if not email.get("paragraphs", [""])[0].startswith("Dear James White,\n"):
    errors.append("[メール] greeting missing")
if email.get("paragraphs", [""])[-1] != "Sincerely,\nJessica Jenkins\nRiverstone High School":
    errors.append("[メール] closing/signature missing")

vocabulary = data.get("vocabulary", [])
if [item.get("word") for item in vocabulary] != EXPECTED_VOCAB_WORDS:
    errors.append("[語彙] headword order/set mismatch")
for item in vocabulary:
    word = item.get("word", "?")
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "wordAudio"):
        if not item.get(key):
            errors.append(f"[語彙] {word}: missing {key}")
    if item.get("level") != "2級":
        errors.append(f"[語彙] {word}: level mismatch")
    distractors = item.get("distractors", [])
    if len(distractors) != 3 or len(set(distractors)) != 3:
        errors.append(f"[語彙] {word}: distractors must be three unique items")
    if item.get("meaning") in distractors:
        errors.append(f"[語彙] {word}: correct meaning in distractors")
    audio_ref = item.get("wordAudio", "")
    audio_path = BASE / Path(audio_ref.replace("/", os.sep))
    if not audio_ref.endswith(".mp3") or not audio_path.is_file() or audio_path.stat().st_size < 500:
        errors.append(f"[語彙音声] {word}: invalid {audio_ref}")
for word, expected in KEY_VOCAB.items():
    item = next((entry for entry in vocabulary if entry.get("word") == word), {})
    if (item.get("meaning"), item.get("pos")) != expected:
        errors.append(f"[語彙] {word}: meaning/pos mismatch")

focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if [point.get("id") for point in focus_points] != ["fp1", "fp2", "fp3", "fp4", "fp5"]:
    errors.append("[Focus] ids must be fp1..fp5")
global_corpus = " ".join(" ".join(passage["paragraphs"]) for passage in passages)
filled_corpus = global_corpus
for number in range(18, 24):
    question = next(question for question, _, _ in all_questions if question["number"] == number)
    filled_corpus = filled_corpus.replace(
        f"( {number} )", question["choices"][question["answer"] - 1]
    )
for point in focus_points:
    point_id = point.get("id", "?")
    for key in (
        "id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
        "highlightColor", "highlightLabel",
    ):
        if not point.get(key):
            errors.append(f"[Focus] {point_id}: missing {key}")
    if len(point.get("examples", [])) != 3:
        errors.append(f"[Focus] {point_id}: examples != 3")
    questions = point.get("practiceQuestions", [])
    if len(questions) != 4 or any(not qa.get("q") or not qa.get("a") for qa in questions):
        errors.append(f"[Focus] {point_id}: practiceQuestions invalid")
    practice = point.get("practicePassage", {})
    english = practice.get("en", "")
    if not english.startswith("[出典:") or not practice.get("ja"):
        errors.append(f"[Focus] {point_id}: source label/translation missing")
    for line in english.splitlines():
        if not line or line.startswith("[出典:"):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            if sentence and sentence not in filled_corpus:
                errors.append(f"[Focus] {point_id}: practice English not in source: {sentence[:60]!r}")
    for pattern in point.get("highlightPatterns", []):
        if pattern not in global_corpus:
            errors.append(f"[Focus] {point_id}: highlight not in source: {pattern!r}")
    audio_ref = practice.get("audioFile", "")
    audio_path = BASE / Path(audio_ref.replace("/", os.sep))
    if not audio_ref.endswith(".mp3") or not audio_path.is_file() or audio_path.stat().st_size < 500:
        errors.append(f"[Focus音声] {point_id}: invalid {audio_ref}")

if data.get("listening") != OFFICIAL_LISTENING:
    errors.append("[リスニング] data key differs from official answer PDF")
if SOURCE_AUDIO.is_dir():
    tracks = sorted(SOURCE_AUDIO.glob("*.mp3"))
    track_numbers = []
    for track in tracks:
        match = re.match(r"(\d+)\s", track.name)
        if match:
            track_numbers.append(int(match.group(1)))
        if track.stat().st_size < 100_000:
            errors.append(f"[リスニング音源] too small: {track.name}")
    if track_numbers != list(range(1, 36)):
        errors.append(f"[リスニング音源] tracks={track_numbers} expected=1..35")
    else:
        notes.append("[リスニング音源] 1〜35の35ファイルを確認")
else:
    notes.append(f"[リスニング音源] ローカル音源なし（スキップ）: {SOURCE_AUDIO}")

average = sum(analysis_lengths) / len(analysis_lengths) if analysis_lengths else 0.0
print(
    f"questions={len(all_questions)} vocab={len(vocabulary)} passages={len(passages)} "
    f"focus={len(focus_points)} analysis_avg={average:.1f} errors={len(errors)}"
)
for note in notes:
    print("  [INFO]", note)
for error in errors:
    print("  [ERROR]", error)
if errors:
    raise SystemExit(1)
print("AUDIT OK: 2026-1-sat 2級")
