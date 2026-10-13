"""Audit ReadPass Grade Pre-2 2024-1 Saturday sub-venue data and assets."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data" / "grade-pre2" / "2024-1-sat"
DATA_PATH = BASE / "data.json"
GENERATOR_PATH = ROOT / "gen_pre2_2024-1-sat.py"
PDF_PATH = (
    ROOT
    / "output"
    / "pdf"
    / "ReadPass_EIKEN_GradePre2_2024-1-sat_Practice_Exam_Large_Type_v1.pdf"
)
SOURCE_ROOT = Path(r"D:\Files\英検過去問\土曜準会場\2024-1（土曜）")
SOURCE_HASHES = {
    SOURCE_ROOT / "2024_1_英検準2級問題.pdf": (
        "3197E03E36FA3022F225F51C07AB8D90AE84F7E91F8460997997F2FA53D5F0BA"
    ),
    SOURCE_ROOT / "準2級_解答.pdf": (
        "500D0C07D53A546034C4DA32BCA7D744420B61C8D27CCE8CE215D8D192E8B581"
    ),
}
OFFICIAL_ANSWERS = [
    4, 1, 1, 1, 1, 3, 1, 1, 1, 3,
    1, 2, 3, 4, 1, 4, 3, 4, 3, 2,
    1, 4, 1, 2, 2, 1, 4, 2, 3,
]
EXPECTED_PASSAGES = {
    "Maria's Baking Adventure": (2, 15, 2),
    "A question": (3, 16, 3),
    "Antoni Gaudí": (4, 22, 4),
}
EXPECTED_SOURCE_PAYLOAD_SHA256 = "6a6d1fff5121b2a6d5f0f60e7f6f5d59833d629b888c56429ffa1efb0ccc7c07"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def collect_questions(data: dict) -> list[dict]:
    questions: list[dict] = []
    for section in data.get("sections", []):
        questions.extend(section.get("questions", []))
        for passage in section.get("passages", []):
            questions.extend(passage.get("questions", []))
    return questions


def source_payload(data: dict) -> list[dict]:
    payload: list[dict] = []
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


errors: list[str] = []
notes: list[str] = []

data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

# Source identity.
for source_path, expected_hash in SOURCE_HASHES.items():
    if not source_path.is_file():
        notes.append(f"原本なし（SHA監査をスキップ）: {source_path}")
        continue
    actual_hash = sha256_file(source_path)
    if actual_hash != expected_hash:
        errors.append(f"原本SHA不一致: {source_path.name}: {actual_hash}")
    else:
        notes.append(f"原本SHA一致: {source_path.name}")

# Reproducible JSON generation.
spec = importlib.util.spec_from_file_location("pre2_2024_1_sat_generator", GENERATOR_PATH)
if spec is None or spec.loader is None:
    errors.append("generatorを読み込めない")
else:
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.build_data() != data:
        errors.append("data.jsonがgeneratorのbuild_data()と一致しない")

# Metadata and section schema.
if (
    data.get("grade"),
    data.get("year"),
    data.get("session"),
    data.get("title"),
) != (
    "準2級",
    "2024",
    "1",
    "2024年度 第1回（土曜準会場） 英語資格検定準2級 リーディング",
):
    errors.append("grade/year/session/titleが期待値と一致しない")

expected_sections = [
    ("大問1", "vocabulary", 15, 0),
    ("大問2", "vocabulary", 5, 0),
    ("大問3", "passage-fill", 0, 1),
    ("大問4", "reading-comprehension", 0, 2),
]
if len(data.get("sections", [])) != 4:
    errors.append(f"sections={len(data.get('sections', []))} != 4")
else:
    for section, (name, section_type, question_count, passage_count) in zip(
        data["sections"], expected_sections
    ):
        if (section.get("name"), section.get("type")) != (name, section_type):
            errors.append(f"{name}: name/type不一致")
        if len(section.get("questions", [])) != question_count:
            errors.append(f"{name}: questions件数不一致")
        if len(section.get("passages", [])) != passage_count:
            errors.append(f"{name}: passages件数不一致")
        if not section.get("instruction"):
            errors.append(f"{name}: instruction欠落")

# Immutable English source payload and official answers.
payload_bytes = json.dumps(
    source_payload(data), ensure_ascii=False, separators=(",", ":")
).encode("utf-8")
payload_hash = hashlib.sha256(payload_bytes).hexdigest()
if payload_hash != EXPECTED_SOURCE_PAYLOAD_SHA256:
    errors.append(
        f"原文payload SHA不一致: {payload_hash} != {EXPECTED_SOURCE_PAYLOAD_SHA256}"
    )

questions = collect_questions(data)
if [question.get("number") for question in questions] != list(range(1, 30)):
    errors.append("設問番号が1〜29の連番ではない")
if [question.get("answer") for question in questions] != OFFICIAL_ANSWERS:
    errors.append("Q1〜29の正答が公式解答と一致しない")

for question in questions:
    number = question["number"]
    if not all(
        len(question.get(key, [])) == 4
        for key in ("choices", "choiceTranslations", "choiceAnalysis")
    ):
        errors.append(f"Q{number}: choices/訳/解説が4件ではない")
    if not question.get("grammar"):
        errors.append(f"Q{number}: grammar欠落")
    if number <= 20 and (not question.get("text") or not question.get("translation")):
        errors.append(f"Q{number}: 問題文または訳欠落")
    if number >= 23 and (
        not question.get("question") or not question.get("questionTranslation")
    ):
        errors.append(f"Q{number}: questionまたはquestionTranslation欠落")
    for index, analysis in enumerate(question.get("choiceAnalysis", []), start=1):
        if number <= 15:
            expected_marker = "✅" if index == question["answer"] else "❌"
            if not analysis.startswith(expected_marker):
                errors.append(f"Q{number} choice{index}: 正誤marker不一致")
        else:
            if analysis.startswith(("✅", "❌", "○")):
                errors.append(f"Q{number} choice{index}: 先頭markerは同年度形式外")
            if ("→正解。💡" in analysis) != (index == question["answer"]):
                errors.append(f"Q{number} choice{index}: 正解marker不一致")
            if index == question["answer"] and not analysis.split("→正解。💡", 1)[-1].strip():
                errors.append(f"Q{number}: 正解の根拠（💡の後）が空")
        if any("とはない" in analysis for analysis in question.get("choiceAnalysis", [])):
            errors.append(f"Q{number}: 「とはない」は「とは書かれていない」にする")

# Passages, email metadata, translations, and sentence pairs.
passages = [
    passage
    for section in data["sections"]
    for passage in section.get("passages", [])
]
if {passage.get("title") for passage in passages} != set(EXPECTED_PASSAGES):
    errors.append("長文タイトルが期待値と一致しない")
for passage in passages:
    title = passage["title"]
    expected_paragraphs, expected_pairs, expected_questions = EXPECTED_PASSAGES[title]
    if len(passage.get("paragraphs", [])) != expected_paragraphs:
        errors.append(f"{title}: paragraphs件数不一致")
    if len(passage.get("translations", [])) != expected_paragraphs:
        errors.append(f"{title}: translations件数不一致")
    if len(passage.get("sentencePairs", [])) != expected_pairs:
        errors.append(f"{title}: sentencePairs件数不一致")
    if len(passage.get("questions", [])) != expected_questions:
        errors.append(f"{title}: questions件数不一致")
    english_corpus = " ".join(passage.get("paragraphs", []))
    for pair_index, pair in enumerate(passage.get("sentencePairs", []), start=1):
        if not isinstance(pair, list) or len(pair) != 2 or not all(pair):
            errors.append(f"{title}: sentencePairs[{pair_index}]が不正")
        elif pair[0] not in english_corpus:
            errors.append(f"{title}: sentencePairs[{pair_index}]が原文にない")

email = next((passage for passage in passages if passage["title"] == "A question"), {})
if email.get("format") != "email" or email.get("meta") != {
    "from": "Steve Potter <steve.musiclover@mailme.com>",
    "to": "Jenny King <jennyk1234@zmail.com>",
    "date": "June 1",
    "subject": "A question",
}:
    errors.append("メールformat/metaが原本と一致しない")

# Vocabulary, Focus Points, and exact audio coverage.
vocabulary = data.get("vocabulary", [])
if len(vocabulary) != 40 or len({item.get("word") for item in vocabulary}) != 40:
    errors.append("語彙が40件一意ではない")
audio_refs = set()
for item in vocabulary:
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "wordAudio"):
        if not item.get(key):
            errors.append(f"語彙 {item.get('word', '?')}: {key}欠落")
    if len(item.get("distractors", [])) != 3:
        errors.append(f"語彙 {item.get('word', '?')}: distractorsが3件ではない")
    if item.get("exampleAudio"):
        errors.append(f"語彙 {item.get('word', '?')}: 同年度外のexampleAudioあり")
    audio_refs.add(item.get("wordAudio", ""))

focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if [focus.get("id") for focus in focus_points] != ["fp1", "fp2", "fp3", "fp4", "fp5"]:
    errors.append("Focus Pointがfp1〜fp5ではない")
# 2024年度の準2級と同じ5色（凡例で区別できること）と、fp5のパラフレーズ固定。
if [focus.get("highlightColor") for focus in focus_points] != [
    "#4f8cff", "#f472b6", "#34d399", "#fbbf24", "#f59e0b",
]:
    errors.append("highlightColorが2024年度形式の5色ではない")
if focus_points and (
    focus_points[-1].get("title") != "今回の重要なパラフレーズ"
    or focus_points[-1].get("highlightLabel") != "パラフレーズ"
):
    errors.append("fp5が「今回の重要なパラフレーズ」ではない")
for focus in focus_points:
    for key in (
        "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "highlightPatterns", "highlightColor",
        "highlightLabel", "practiceQuestions",
    ):
        if not focus.get(key):
            errors.append(f"{focus.get('id', '?')}: {key}欠落")
    passage = focus.get("practicePassage", {})
    if not passage.get("en") or not passage.get("ja") or not passage.get("audioFile"):
        errors.append(f"{focus.get('id', '?')}: practicePassage不完全")
    audio_refs.add(passage.get("audioFile", ""))
    if len(focus.get("practiceQuestions", [])) != 4:
        errors.append(f"{focus.get('id', '?')}: practiceQuestionsが4件ではない")

audio_files = {
    path.relative_to(BASE).as_posix() for path in (BASE / "audio").rglob("*.mp3")
}
if len(audio_refs) != 45 or len(audio_files) != 45 or audio_refs != audio_files:
    errors.append(
        f"音声参照/実体不一致: refs={len(audio_refs)} files={len(audio_files)}"
    )
for audio_ref in audio_refs:
    audio_path = BASE / audio_ref
    if not audio_path.is_file() or audio_path.stat().st_size < 500:
        errors.append(f"音声欠落または小さすぎる: {audio_ref}")
    elif audio_path.read_bytes()[:1] not in (b"I", b"\xff"):
        errors.append(f"MP3 signature不正: {audio_ref}")

# Catalog, fixed PDF map, cache busting, and PDF geometry.
top_text = (ROOT / "top.js").read_text(encoding="utf-8")
print_text = (ROOT / "print.js").read_text(encoding="utf-8")
for filename, text in (("top.js", top_text), ("print.js", print_text)):
    start = text.index("id: 'grade-pre2'")
    end = text.index("id: 'grade3'", start)
    block = text[start:end]
    if block.count("{ id: '2024-1-sat'") != 1:
        errors.append(f"{filename}: grade-pre2 catalog登録が1件ではない")
    if block.index("{ id: '2024-1'") > block.index("{ id: '2024-1-sat'"):
        errors.append(f"{filename}: 2024-1-satの並び順不正")

fixed_key = "'grade-pre2/2024-1-sat':"
if print_text.count(fixed_key) != 1 or "pages: 10" not in print_text[
    print_text.index(fixed_key): print_text.index(fixed_key) + 600
]:
    errors.append("print.js: 固定PDF登録不正")
# print.html must load a print.js built on or after the day this exam was added.
cache = re.search(r"print\.js\?v=(\d{8})-", (ROOT / "print.html").read_text(encoding="utf-8"))
if not cache or cache.group(1) < "20261013":
    errors.append("print.html: print.jsのcache versionが2024-1-sat追加前のまま")

if not PDF_PATH.is_file():
    errors.append("固定PDF欠落")
else:
    reader = PdfReader(str(PDF_PATH))
    if len(reader.pages) != 10:
        errors.append(f"固定PDF pages={len(reader.pages)} != 10")
    for page_number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.28) > 1 or abs(height - 841.89) > 1:
            errors.append(f"固定PDF page {page_number}: A4ではない ({width}, {height})")

print(
    f"questions={len(questions)} passages={len(passages)} vocab={len(vocabulary)} "
    f"focus={len(focus_points)} audio={len(audio_files)} errors={len(errors)}"
)
for note in notes:
    print(f"  [INFO] {note}")
for error in errors:
    print(f"  [ERROR] {error}")
if errors:
    raise SystemExit(1)
print("AUDIT OK: 2024-1-sat 準2級")
