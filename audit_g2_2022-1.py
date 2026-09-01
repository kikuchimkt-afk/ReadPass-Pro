# -*- coding: utf-8 -*-
"""Comprehensive local audit for ReadPass Grade 2 2022-1 (main venue)."""

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import soundfile as sf
from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent
BASE = REPO / "data" / "grade2" / "2022-1"
DATA_PATH = BASE / "data.json"
SOURCE_DIR = Path(r"D:\Files\英検過去問\2級\2級2022-1")
PDF_PATH = REPO / "output" / "pdf" / "ReadPass_EIKEN_Grade2_2022-1_Practice_Exam_Large_Type_v1.pdf"

SOURCE_HASHES = {
    "2022-1-1ji-2kyu.pdf": "d0daaac600e05e0bfe1b00739250c3135ff43dd5e02f593575b2e2d8865a84e1",
    "2022-1-1ji-2kyu-script.pdf": "74b70e3da2f2a76c5857f9c5f291340d3d1deef36d4a7aa193b69b8ef51284c1",
    "2kyu-sun.pdf": "bf2e776e593135cdbcd9413b4ac87ec339957dffe840d313013008e48590fc6a",
    "2Q-part1.mp3": "91c00f85e3acbe1374271698f0e7125481dcc876ac6f066ce9f2cb21ad5a641f",
    "2Q-part2.mp3": "44944bb0cf486e0ba3eb7dd800691c5c541f2bf1f6f18024a68331630a0d2007",
}

OFFICIAL = dict(enumerate([
    1, 4, 4, 3, 4, 4, 3, 4, 1, 4,
    1, 1, 1, 2, 2, 3, 2, 2, 3, 1,
    1, 3, 1, 3, 2, 4,
    4, 1, 2, 1, 4, 4, 3, 2, 2, 4, 4, 4,
], 1))
LISTENING = {
    "part1": dict(enumerate([1, 3, 4, 3, 3, 2, 4, 2, 1, 4, 2, 2, 2, 3, 4], 1)),
    "part2": dict(enumerate([3, 1, 4, 2, 3, 4, 2, 2, 3, 1, 3, 2, 3, 2, 3], 16)),
}
PAIR_COUNTS = {
    "An Answer in a Teacup": 16,
    "More than Just a Pretty Bird": 19,
    "Your order": 15,
    "Tweed": 18,
    "Clues from the Distant Past": 19,
}
EXPECTED_TOP_KEYS = [
    "grade", "year", "session", "title", "exam", "sections", "listening",
    "vocabulary", "lessonPlan",
]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm(value):
    return re.sub(r"\s+", " ", value or "").strip()


data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
errors = []

# 1. Original source identity
for filename, expected in SOURCE_HASHES.items():
    path = SOURCE_DIR / filename
    if not path.is_file():
        errors.append(f"[source] missing: {path}")
    elif sha256(path) != expected:
        errors.append(f"[source] SHA-256 mismatch: {filename}")

# 2. Metadata and section structure
if list(data) != EXPECTED_TOP_KEYS:
    errors.append(f"[metadata] top-level keys/order: {list(data)}")
expected_metadata = {
    "grade": "2級",
    "year": "2022",
    "session": "1",
    "title": "2022年度 第1回 英語資格検定2級 リーディング",
    "exam": "2022-1",
}
for key, expected in expected_metadata.items():
    if data.get(key) != expected:
        errors.append(f"[metadata] {key}: {data.get(key)!r} != {expected!r}")
sections = data.get("sections", [])
section_meta = [(s.get("name"), s.get("nameEn"), s.get("type")) for s in sections]
if section_meta != [
    ("大問1", "Part 1", "vocabulary"),
    ("大問2", "Part 2", "passage-fill"),
    ("大問3", "Part 3", "reading-comprehension"),
]:
    errors.append(f"[structure] section metadata: {section_meta}")
if len(sections) == 3:
    signature = [
        len(sections[0].get("questions", [])),
        *[len(p.get("questions", [])) for p in sections[1].get("passages", [])],
        *[len(p.get("questions", [])) for p in sections[2].get("passages", [])],
    ]
    if signature != [20, 3, 3, 3, 4, 5]:
        errors.append(f"[structure] question signature: {signature}")

# 3. Every reading question and explanation
questions = []
for section in sections:
    questions.extend((q, None) for q in section.get("questions", []))
    for passage in section.get("passages", []):
        corpus = " ".join(passage.get("paragraphs", []))
        questions.extend((q, corpus) for q in passage.get("questions", []))
if [q["number"] for q, _ in questions] != list(range(1, 39)):
    errors.append("[questions] numbers are not exactly Q1-Q38")
for question, corpus in questions:
    number = question["number"]
    if question.get("answer") != OFFICIAL[number]:
        errors.append(f"[answer] Q{number}: {question.get('answer')} != {OFFICIAL[number]}")
    for field in ("choices", "choiceTranslations", "choiceAnalysis"):
        if len(question.get(field, [])) != 4:
            errors.append(f"[question] Q{number}: {field} count != 4")
    if not question.get("grammar"):
        errors.append(f"[question] Q{number}: grammar missing")
    analyses = question.get("choiceAnalysis", [])
    if len(analyses) == 4:
        correct = analyses[question["answer"] - 1]
        if correct.count("→正解。💡") != 1:
            errors.append(f"[analysis] Q{number}: correct marker count != 1")
        if any("→正解" in text for i, text in enumerate(analyses, 1) if i != question["answer"]):
            errors.append(f"[analysis] Q{number}: wrong option marked correct")
        if any(text.lstrip().startswith(("✅", "❌", "○", "×")) for text in analyses):
            errors.append(f"[analysis] Q{number}: legacy leading symbol")
    if number <= 20:
        if not question.get("text") or not question.get("translation"):
            errors.append(f"[question] Q{number}: text/translation missing")
    elif number >= 27:
        if not question.get("question") or not question.get("questionTranslation"):
            errors.append(f"[question] Q{number}: question translation missing")
    if corpus is not None:
        evidence = question.get("sourceEvidence", [])
        if not evidence:
            errors.append(f"[evidence] Q{number}: sourceEvidence missing")
        for pattern in evidence:
            if norm(pattern).lower() not in norm(corpus).lower():
                errors.append(f"[evidence] Q{number}: not found in passage: {pattern!r}")

# 4. Listening answer table
for part, expected in LISTENING.items():
    actual = {int(key): value for key, value in data.get("listening", {}).get(part, {}).items()}
    if actual != expected:
        errors.append(f"[listening] {part} does not match official answers")

# 5. Passage translations and sentence popups
for section in sections[1:]:
    for passage in section.get("passages", []):
        title = passage.get("title")
        paragraphs = passage.get("paragraphs", [])
        translations = passage.get("translations", [])
        pairs = passage.get("sentencePairs", [])
        corpus = " ".join(paragraphs)
        if len(translations) != len(paragraphs) or any(not norm(text) for text in translations):
            errors.append(f"[translation] {title}: paragraph translation mismatch")
        if len(pairs) != PAIR_COUNTS.get(title):
            errors.append(f"[sentencePairs] {title}: {len(pairs)} != {PAIR_COUNTS.get(title)}")
        seen_english = set()
        for pair in pairs:
            if len(pair) != 4 or not all(norm(value) for value in pair[:3]):
                errors.append(f"[sentencePairs] {title}: malformed pair")
                continue
            if pair[0] not in corpus:
                errors.append(f"[sentencePairs] {title}: English sentence not found: {pair[0]!r}")
            if pair[0] in seen_english:
                errors.append(f"[sentencePairs] {title}: duplicate sentence")
            seen_english.add(pair[0])

email_passage = next(
    (passage for passage in sections[2].get("passages", []) if passage.get("title") == "Your order"),
    None,
)
if email_passage is None:
    errors.append("[email] Your order passage missing")
else:
    expected_signature = "Sincerely,\nNoel Lander\nCustomer Support\nCoffee Shop Supplies"
    expected_signature_ja = "敬具\nノエル・ランダー\nカスタマーサポート\nコーヒーショップ用品社"
    email_paragraphs = email_passage.get("paragraphs") or [None]
    email_translations = email_passage.get("translations") or [None]
    if email_paragraphs[0] != "Dear Mr. Stein,":
        errors.append("[email] greeting missing")
    if email_paragraphs[-1] != expected_signature:
        errors.append("[email] signature missing")
    if email_translations[0] != "スタイン様":
        errors.append("[email] greeting translation missing")
    if email_translations[-1] != expected_signature_ja:
        errors.append("[email] signature translation missing")

# 6. Vocabulary, focus points, generated audio, and manifest integrity
vocabulary = data.get("vocabulary", [])
if len(vocabulary) != 65 or len({item.get("word") for item in vocabulary}) != 65:
    errors.append(f"[vocabulary] expected 65 unique words; got {len(vocabulary)}")
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"[focus] expected 5; got {len(focus_points)}")
expected_audio = set()
for item in vocabulary:
    for field in ("word", "meaning", "pos", "level", "source", "example", "exampleJa", "wordAudio"):
        if not norm(item.get(field, "")):
            errors.append(f"[vocabulary] {item.get('word')}: {field} missing")
    if len(item.get("distractors", [])) != 3 or item.get("meaning") in item.get("distractors", []):
        errors.append(f"[vocabulary] {item.get('word')}: invalid distractors")
    expected_audio.add(item.get("wordAudio"))
for index, point in enumerate(focus_points, 1):
    for field in ("id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation", "highlightLabel"):
        if not norm(point.get(field, "")):
            errors.append(f"[focus] fp{index}: {field} missing")
    if len(point.get("examples", [])) != 3:
        errors.append(f"[focus] fp{index}: examples count != 3")
    if len(point.get("practiceQuestions", [])) != 4:
        errors.append(f"[focus] fp{index}: practiceQuestions count != 4")
    practice = point.get("practicePassage", {})
    if not norm(practice.get("en")) or not norm(practice.get("ja")):
        errors.append(f"[focus] fp{index}: practice passage missing")
    expected_audio.add(practice.get("audioFile"))
manifest_path = BASE / "audio" / "tts_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {}
if set(manifest) != expected_audio or len(expected_audio) != 70:
    errors.append(f"[audio] manifest/path set mismatch: manifest={len(manifest)} expected={len(expected_audio)}")
for relative in sorted(expected_audio):
    path = BASE / relative
    entry = manifest.get(relative, {})
    if not path.is_file() or path.stat().st_size < 500:
        errors.append(f"[audio] missing/small: {relative}")
        continue
    if entry.get("audioSha256") != sha256(path):
        errors.append(f"[audio] SHA-256 mismatch: {relative}")
    try:
        with sf.SoundFile(path) as audio:
            if audio.frames <= 0 or audio.samplerate <= 0 or audio.channels <= 0:
                errors.append(f"[audio] invalid stream metadata: {relative}")
    except Exception as exc:
        errors.append(f"[audio] decode failed: {relative}: {exc}")

# 7. UI and print registration
top_js = (REPO / "top.js").read_text(encoding="utf-8")
print_js = (REPO / "print.js").read_text(encoding="utf-8")
print_html = (REPO / "print.html").read_text(encoding="utf-8")
grade2_start = top_js.find("id: 'grade2'")
grade2_end = top_js.find("id: 'grade-pre2plus'", grade2_start)
grade2_block = top_js[grade2_start:grade2_end] if grade2_start >= 0 and grade2_end > grade2_start else ""
if "{ id: '2022-1', label: '2022年度 第1回', sub: '一次試験リーディング' }" not in grade2_block:
    errors.append("[registration] top.js Grade 2 catalog entry missing")
for required in (
    "'grade2/2022-1'",
    "ReadPass_EIKEN_Grade2_2022-1_Practice_Exam_Large_Type_v1.pdf",
    "20260901-eiken-grade2-2022-1-v1",
):
    if required not in print_js:
        errors.append(f"[registration] print.js missing: {required}")
if "print.js?v=20260902-grade2-2022-all-v1" not in print_html:
    errors.append("[registration] print.html cache identifier missing")

# 8. Fixed PDF: exact size/content and deterministic regeneration
if not PDF_PATH.is_file():
    errors.append(f"[pdf] missing: {PDF_PATH}")
else:
    reader = PdfReader(str(PDF_PATH))
    if len(reader.pages) != 13:
        errors.append(f"[pdf] pages={len(reader.pages)} != 13")
    for index, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.276) > 0.02 or abs(height - 841.89) > 0.02:
            errors.append(f"[pdf] page {index}: not A4 ({width} x {height})")
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    for anchor in (
        "An Answer in a Teacup",
        "More than Just a Pretty Bird",
        "Dear Mr. Stein",
        "Coffee Shop Supplies",
        "Tweed",
        "Clues from the Distant Past",
        "Q38",
        "大問3は正解番号のみ",
    ):
        if anchor not in pdf_text:
            errors.append(f"[pdf] text anchor missing: {anchor}")
    with tempfile.TemporaryDirectory(prefix="readpass-g2-2022-1-") as temporary:
        regenerated = Path(temporary) / PDF_PATH.name
        command = [
            sys.executable,
            str(REPO / "scripts" / "build_fixed_exam_pdf.py"),
            "--grade", "grade2",
            "--exam", "2022-1",
            "--output", str(regenerated),
        ]
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            errors.append(f"[pdf] deterministic rebuild failed: {result.stderr.strip()}")
        elif sha256(regenerated) != sha256(PDF_PATH):
            errors.append("[pdf] deterministic SHA-256 mismatch")

if errors:
    print(f"FAIL: {len(errors)} issue(s)")
    for error in errors:
        print(f" - {error}")
    raise SystemExit(1)

print("PASS: Grade 2 2022-1 comprehensive audit")
print(f"  questions: {len(questions)} (official answers matched)")
print(f"  passages: {sum(len(s.get('passages', [])) for s in sections)} / sentencePairs: {sum(PAIR_COUNTS.values())}")
print(f"  vocabulary: {len(vocabulary)} / focusPoints: {len(focus_points)}")
print(f"  generated audio: {len(expected_audio)} (manifest SHA + full decode)")
print(f"  fixed PDF: 13 A4 pages / SHA-256 {sha256(PDF_PATH)}")
