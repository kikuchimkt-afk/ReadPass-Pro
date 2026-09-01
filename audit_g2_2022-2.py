# -*- coding: utf-8 -*-
"""Comprehensive local audit for ReadPass Grade 2 2022-2 (main venue)."""

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
BASE = REPO / "data" / "grade2" / "2022-2"
DATA_PATH = BASE / "data.json"
SOURCE_DIR = Path(r"D:\Files\英検過去問\2級\2級2022-2")
PDF_PATH = REPO / "output" / "pdf" / "ReadPass_EIKEN_Grade2_2022-2_Practice_Exam_Large_Type_v1.pdf"

SOURCE_HASHES = {
    "2022-2-1ji-2kyu.pdf": "6eccbeaae61d75c8b601ab721e42fbf3f28c3785964ecc5a275f99d1a539ee28",
    "2022-2-1ji-2kyu-script.pdf": "de74de37f37e45c0a637097261e3856c44709f8b9fcac2f8ddf55328a360ab82",
    "2kyu-sun.pdf": "b0a3786781cec7a7972e6c8042c9a7b5aed9f023e7011270d0b864672ca53bcc",
    "2Q-part1.mp3": "0ec397a91236f118d2153465e8ddcd409ad2286f7f3c45679b02d955273e6198",
    "2Q-part2.mp3": "7666445c1c0095d0dd137ccb4588890480f1212a06b46e2b06e740e2a6f724fd",
}
SOURCE_PDF_PAGES = {
    "2022-2-1ji-2kyu.pdf": 24,
    "2022-2-1ji-2kyu-script.pdf": 9,
    "2kyu-sun.pdf": 1,
}
SOURCE_AUDIO_DECODED_FRAMES = {
    "2Q-part1.mp3": 33175296,
    "2Q-part2.mp3": 35377920,
}

OFFICIAL = dict(enumerate([
    1, 1, 3, 3, 1, 2, 3, 4, 2, 3,
    2, 3, 3, 4, 1, 1, 2, 1, 2, 2,
    2, 3, 1, 2, 3, 4,
    2, 1, 2, 4, 4, 1, 1, 2, 2, 1, 1, 4,
], 1))
LISTENING = {
    "part1": dict(enumerate([3, 4, 4, 1, 2, 4, 3, 4, 1, 3, 1, 1, 3, 1, 3], 1)),
    "part2": dict(enumerate([4, 1, 4, 2, 3, 1, 1, 1, 2, 2, 2, 4, 2, 2, 2], 16)),
}
PAIR_COUNTS = {
    "Trouble at Sea": 17,
    "Performing Cats": 16,
    "ZX950 LCD TV": 12,
    "The Empress’s Favorite Clothes": 21,
    "Desert Delight": 22,
}
SPECIAL_ANCHORS = {
    "Trouble at Sea": ("world’s oceans",),
    "Performing Cats": (
        "“Memory,”",
        "Webber’s",
        "Old Possum’s",
        "everyone’s attention",
    ),
    "ZX950 LCD TV": (
        "TV’s instruction manual",
        "I’m sure",
        "I don’t need",
    ),
    "The Empress’s Favorite Clothes": (
        "phuti karpas",
    ),
    "Desert Delight": (
        "Tohono O’odham",
        "“desert people”",
        "each year—once in the winter",
        "This fruit—the saguaro fruit—",
        "tribe’s endangered traditions",
    ),
}
QUESTION_ANCHORS = {
    1: ("yesterday’s contest",),
    12: ("weren’t the best",),
    13: ("What’s wrong",),
    15: ("It’s a shame", "can’t hold"),
    19: ("Michelle’s classroom",),
    20: ("parents’ house", "There’s no"),
    25: ("cats’ bodies",),
    33: ("Islam’s efforts",),
    34: ("Tohono O’odham",),
    36: ("Tohono O’odham",),
    37: ("Tohono O’odham",),
    38: ("Tohono O’odham", "people’s favorite food"),
}
FORBIDDEN_STRAIGHT_FORMS = (
    "yesterday's",
    "weren't",
    "What's",
    "It's a shame",
    "can't hold",
    "Michelle's",
    "parents'",
    "There's no",
    "world's oceans",
    "Webber's",
    "Old Possum's",
    "everyone's attention",
    "cats' bodies",
    "TV's instruction manual",
    "I'm sure",
    "I don't need",
    "The Empress's Favorite Clothes",
    "Islam's efforts",
    "Tohono O'odham",
    "tribe's endangered traditions",
    "people's favorite food",
)
EXPECTED_TOP_KEYS = [
    "grade", "year", "session", "title", "exam", "sections", "listening",
    "vocabulary", "lessonPlan",
]
VOICE = "en-US-JennyNeural"
RATE = "-15%"
# This checksum locks the audited source-facing transcription: question wording,
# all four choices, passage titles/meta, and every English paragraph.
SOURCE_TEXT_SHA256 = "aeb3db6eb0afb9d236a2bf2519763a8d4389f2951a7edb9a16e90fc880258f49"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm(value):
    return re.sub(r"\s+", " ", value or "").strip()


def is_a4(page, tolerance=0.5):
    return (
        abs(float(page.mediabox.width) - 595.276) <= tolerance
        and abs(float(page.mediabox.height) - 841.89) <= tolerance
    )


def tts_signature(text):
    payload = json.dumps(
        {"rate": RATE, "text": text, "voice": VOICE},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def decode_audio_fully(path):
    with sf.SoundFile(path) as audio:
        if audio.frames <= 0 or audio.samplerate <= 0 or audio.channels <= 0:
            raise ValueError("invalid stream metadata")
        decoded_frames = 0
        while True:
            block = audio.read(65536, dtype="float32", always_2d=True)
            if len(block) == 0:
                break
            decoded_frames += len(block)
        if decoded_frames <= 0:
            raise ValueError("decoder returned no samples")
        return decoded_frames


if not DATA_PATH.is_file():
    print(f"FAIL: data missing: {DATA_PATH}")
    raise SystemExit(1)

data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
errors = []

# 1. Original source identity, page geometry, and source-audio decodability
for filename, expected in SOURCE_HASHES.items():
    path = SOURCE_DIR / filename
    if not path.is_file():
        errors.append(f"[source] missing: {path}")
    elif sha256(path) != expected:
        errors.append(f"[source] SHA-256 mismatch: {filename}")
for filename, expected_pages in SOURCE_PDF_PAGES.items():
    path = SOURCE_DIR / filename
    if not path.is_file():
        continue
    try:
        reader = PdfReader(str(path))
        if len(reader.pages) != expected_pages:
            errors.append(f"[source] {filename}: pages={len(reader.pages)} != {expected_pages}")
        for index, page in enumerate(reader.pages, 1):
            if not is_a4(page):
                errors.append(f"[source] {filename} page {index}: not A4")
    except Exception as exc:
        errors.append(f"[source] {filename}: PDF read failed: {exc}")
for filename in ("2Q-part1.mp3", "2Q-part2.mp3"):
    path = SOURCE_DIR / filename
    if not path.is_file():
        continue
    try:
        decoded_frames = decode_audio_fully(path)
        if decoded_frames != SOURCE_AUDIO_DECODED_FRAMES[filename]:
            errors.append(
                f"[source] source-audio frames {filename}: "
                f"{decoded_frames} != {SOURCE_AUDIO_DECODED_FRAMES[filename]}"
            )
    except Exception as exc:
        errors.append(f"[source] source-audio decode failed: {filename}: {exc}")

# 2. Metadata and section structure
if list(data) != EXPECTED_TOP_KEYS:
    errors.append(f"[metadata] top-level keys/order: {list(data)}")
expected_metadata = {
    "grade": "2級",
    "year": "2022",
    "session": "2",
    "title": "2022年度 第2回 英語資格検定2級 リーディング",
    "exam": "2022-2",
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
else:
    errors.append(f"[structure] expected 3 sections; got {len(sections)}")

# 3. Every written question, option, explanation, and source-evidence anchor
questions = []
passages = []
for section in sections:
    questions.extend((q, None) for q in section.get("questions", []))
    for passage in section.get("passages", []):
        passages.append(passage)
        corpus = " ".join(passage.get("paragraphs", []))
        questions.extend((q, corpus) for q in passage.get("questions", []))
questions.sort(key=lambda item: item[0].get("number", 0))
if [q.get("number") for q, _ in questions] != list(range(1, 39)):
    errors.append("[questions] numbers are not exactly Q1-Q38")
for question, corpus in questions:
    number = question.get("number")
    if number not in OFFICIAL:
        errors.append(f"[questions] unexpected number: {number!r}")
        continue
    if question.get("answer") != OFFICIAL[number]:
        errors.append(f"[answer] Q{number}: {question.get('answer')} != {OFFICIAL[number]}")
    for field in ("choices", "choiceTranslations", "choiceAnalysis"):
        if len(question.get(field, [])) != 4:
            errors.append(f"[question] Q{number}: {field} count != 4")
    if not norm(question.get("grammar")):
        errors.append(f"[question] Q{number}: grammar missing")
    analyses = question.get("choiceAnalysis", [])
    if len(analyses) == 4:
        correct_markers = [
            index for index, text in enumerate(analyses, 1)
            if text.count("→正解。💡") == 1
        ]
        if correct_markers != [question["answer"]]:
            errors.append(
                f"[analysis] Q{number}: correct-marker positions {correct_markers} "
                f"!= [{question['answer']}]"
            )
        if any(
            "→正解" in text
            for index, text in enumerate(analyses, 1)
            if index != question["answer"]
        ):
            errors.append(f"[analysis] Q{number}: wrong option marked correct")
        if any(text.count("→正解。💡") > 1 for text in analyses):
            errors.append(f"[analysis] Q{number}: duplicate exact marker")
        if any(text.lstrip().startswith(("✅", "❌", "○", "×")) for text in analyses):
            errors.append(f"[analysis] Q{number}: legacy leading symbol")
    if number <= 20:
        if not norm(question.get("text")) or not norm(question.get("translation")):
            errors.append(f"[question] Q{number}: text/translation missing")
        source_wording = question.get("text", "")
    elif number >= 27:
        if not norm(question.get("question")) or not norm(question.get("questionTranslation")):
            errors.append(f"[question] Q{number}: question translation missing")
        source_wording = question.get("question", "") + " " + " ".join(question.get("choices", []))
    else:
        source_wording = " ".join(question.get("choices", []))
    for anchor in QUESTION_ANCHORS.get(number, ()):
        if anchor not in source_wording:
            errors.append(f"[typography] Q{number}: missing exact anchor {anchor!r}")
    if corpus is not None:
        evidence = question.get("sourceEvidence", [])
        if not evidence:
            errors.append(f"[evidence] Q{number}: sourceEvidence missing")
        for pattern in evidence:
            if norm(pattern).lower() not in norm(corpus).lower():
                errors.append(f"[evidence] Q{number}: not found in passage: {pattern!r}")

# 4. Lock the source-facing transcription and special typography
source_payload = {
    "questions": [
        {
            "number": question.get("number"),
            "text": question.get("text"),
            "question": question.get("question"),
            "choices": question.get("choices"),
        }
        for question, _ in questions
    ],
    "passages": [
        {
            "title": passage.get("title"),
            "format": passage.get("format"),
            "meta": passage.get("meta"),
            "paragraphs": passage.get("paragraphs"),
        }
        for passage in passages
    ],
}
source_text_sha256 = hashlib.sha256(
    json.dumps(
        source_payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
).hexdigest()
if SOURCE_TEXT_SHA256 and source_text_sha256 != SOURCE_TEXT_SHA256:
    errors.append(
        f"[transcription] source-facing SHA-256 {source_text_sha256} "
        f"!= {SOURCE_TEXT_SHA256}"
    )
source_blob = json.dumps(source_payload, ensure_ascii=False)
for forbidden in FORBIDDEN_STRAIGHT_FORMS:
    if forbidden in source_blob:
        errors.append(f"[typography] straight form remains: {forbidden!r}")

# 5. Official listening answer table
for part, expected in LISTENING.items():
    actual = {
        int(key): value
        for key, value in data.get("listening", {}).get(part, {}).items()
    }
    if actual != expected:
        errors.append(f"[listening] {part} does not match official answers")

# 6. Passage translations, complete sentence-pair coverage, and email framing
titles = [passage.get("title") for passage in passages]
if titles != list(PAIR_COUNTS):
    errors.append(f"[passages] titles/order mismatch: {titles}")
for passage in passages:
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
    for pair_item in pairs:
        if len(pair_item) != 4 or not all(norm(value) for value in pair_item[:3]):
            errors.append(f"[sentencePairs] {title}: malformed pair")
            continue
        if pair_item[0] not in corpus:
            errors.append(f"[sentencePairs] {title}: English sentence not found: {pair_item[0]!r}")
        if pair_item[0] in seen_english:
            errors.append(f"[sentencePairs] {title}: duplicate sentence")
        seen_english.add(pair_item[0])
    pair_source_paragraphs = (
        paragraphs[1:-1] if title == "ZX950 LCD TV" else paragraphs
    )
    if norm(" ".join(pair_source_paragraphs)) != norm(" ".join(item[0] for item in pairs)):
        errors.append(f"[sentencePairs] {title}: not a complete ordered transcription")
    pair_blob = " ".join(item[0] for item in pairs)
    for anchor in SPECIAL_ANCHORS.get(title, ()):
        if anchor not in corpus:
            errors.append(f"[typography] {title}: paragraph anchor missing {anchor!r}")
        if anchor not in pair_blob:
            errors.append(f"[typography] {title}: sentencePairs anchor missing {anchor!r}")

email_passage = next(
    (passage for passage in passages if passage.get("title") == "ZX950 LCD TV"),
    None,
)
if email_passage is None:
    errors.append("[email] ZX950 LCD TV passage missing")
else:
    expected_meta = {
        "from": "Michael Green <mikeyg4000@friendlymail.com>",
        "to": "Television Depot Customer Service <service@televisiondepot.com>",
        "date": "October 9",
        "subject": "ZX950 LCD TV",
    }
    if email_passage.get("format") != "email":
        errors.append("[email] format=email missing")
    if email_passage.get("meta") != expected_meta:
        errors.append(f"[email] metadata mismatch: {email_passage.get('meta')!r}")
    email_paragraphs = email_passage.get("paragraphs") or [None]
    email_translations = email_passage.get("translations") or [None]
    if email_paragraphs[0] != "Dear Customer Service Representative,":
        errors.append("[email] greeting missing")
    if email_paragraphs[-1] != "Regards,\nMichael Green":
        errors.append("[email] signature missing")
    if email_translations[0] != "カスタマーサービスご担当者様":
        errors.append("[email] greeting translation missing")
    if email_translations[-1] != "敬具\nマイケル・グリーン":
        errors.append("[email] signature translation missing")

# 7. Vocabulary, Focus, generated audio, and manifest integrity
vocabulary = data.get("vocabulary", [])
if len(vocabulary) != 65 or len({item.get("word") for item in vocabulary}) != 65:
    errors.append(f"[vocabulary] expected 65 unique words; got {len(vocabulary)}")
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"[focus] expected 5; got {len(focus_points)}")
all_passage_corpus = " ".join(
    " ".join(passage.get("paragraphs", [])) for passage in passages
)
expected_audio_inputs = {}
for item in vocabulary:
    word = item.get("word", "")
    for field in ("word", "meaning", "pos", "level", "source", "example", "exampleJa", "wordAudio"):
        if not norm(item.get(field, "")):
            errors.append(f"[vocabulary] {word!r}: {field} missing")
    distractors = item.get("distractors", [])
    if (
        len(distractors) != 3
        or len(set(distractors)) != 3
        or item.get("meaning") in distractors
        or any(not norm(value) for value in distractors)
    ):
        errors.append(f"[vocabulary] {word!r}: invalid distractors")
    relative = item.get("wordAudio")
    if isinstance(relative, str) and relative:
        expected_audio_inputs[relative] = word
for index, point in enumerate(focus_points, 1):
    for field in (
        "id", "title", "subtitle", "explanation", "sourceQuote",
        "sourceLocation", "highlightLabel",
    ):
        if not norm(point.get(field, "")):
            errors.append(f"[focus] fp{index}: {field} missing")
    if point.get("id") != f"fp{index}":
        errors.append(f"[focus] fp{index}: id/order mismatch")
    examples = point.get("examples", [])
    if len(examples) != 3:
        errors.append(f"[focus] fp{index}: examples count != 3")
    for example in examples:
        if any(not norm(example.get(field, "")) for field in ("en", "ja", "note")):
            errors.append(f"[focus] fp{index}: incomplete example")
    practice_questions = point.get("practiceQuestions", [])
    if len(practice_questions) != 4:
        errors.append(f"[focus] fp{index}: practiceQuestions count != 4")
    for practice_question in practice_questions:
        if any(not norm(practice_question.get(field, "")) for field in ("q", "a")):
            errors.append(f"[focus] fp{index}: incomplete practice question")
    if norm(point.get("sourceQuote")) not in norm(all_passage_corpus):
        errors.append(f"[focus] fp{index}: sourceQuote not found in source passage")
    practice = point.get("practicePassage", {})
    english = practice.get("en", "")
    if not norm(english) or not norm(practice.get("ja")):
        errors.append(f"[focus] fp{index}: practice passage missing")
    relative = practice.get("audioFile")
    if isinstance(relative, str) and relative:
        spoken = re.sub(r"\[Source:.*?\]\s*", "", english, count=1).strip()
        expected_audio_inputs[relative] = spoken

expected_audio = set(expected_audio_inputs)
if len(expected_audio) != 70:
    errors.append(f"[audio] expected 70 unique paths; got {len(expected_audio)}")
manifest_path = BASE / "audio" / "tts_manifest.json"
try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        manifest = {}
        errors.append("[audio] manifest is not an object")
except (FileNotFoundError, json.JSONDecodeError) as exc:
    manifest = {}
    errors.append(f"[audio] manifest missing/invalid: {exc}")
if set(manifest) != expected_audio:
    errors.append(
        f"[audio] manifest/path set mismatch: manifest={len(manifest)} "
        f"expected={len(expected_audio)}"
    )
for relative in sorted(expected_audio):
    path = BASE / relative
    entry = manifest.get(relative, {})
    if not path.is_file() or path.stat().st_size < 500:
        errors.append(f"[audio] missing/small: {relative}")
        continue
    if entry.get("audioSha256") != sha256(path):
        errors.append(f"[audio] SHA-256 mismatch: {relative}")
    expected_input = tts_signature(expected_audio_inputs[relative])
    if entry.get("inputSha256") != expected_input:
        errors.append(f"[audio] input SHA-256 mismatch: {relative}")
    try:
        decode_audio_fully(path)
    except Exception as exc:
        errors.append(f"[audio] decode failed: {relative}: {exc}")

# 8. Grade-2-only catalog registration and fixed-PDF mapping
top_js = (REPO / "top.js").read_text(encoding="utf-8")
print_js = (REPO / "print.js").read_text(encoding="utf-8")
print_html = (REPO / "print.html").read_text(encoding="utf-8")
grade2_start = top_js.find("id: 'grade2'")
grade2_end = top_js.find("id: 'grade-pre2plus'", grade2_start)
if grade2_start < 0 or grade2_end <= grade2_start:
    errors.append("[registration] Grade 2 catalog block boundaries missing")
    grade2_block = ""
else:
    grade2_block = top_js[grade2_start:grade2_end]
grade2_entry = "{ id: '2022-2', label: '2022年度 第2回', sub: '一次試験リーディング' }"
if grade2_block.count(grade2_entry) != 1:
    errors.append(
        f"[registration] top.js Grade 2 block entry count="
        f"{grade2_block.count(grade2_entry)} != 1"
    )
mapping_pattern = re.compile(
    r"'grade2/2022-2'\s*:\s*\{(?P<body>.*?)\n\s*\},",
    re.DOTALL,
)
mapping_matches = list(mapping_pattern.finditer(print_js))
if len(mapping_matches) != 1:
    errors.append(f"[registration] print.js mapping count={len(mapping_matches)} != 1")
else:
    mapping_body = mapping_matches[0].group("body")
    for required in (
        "label: '英検2級 2022年度 第2回'",
        "ReadPass_EIKEN_Grade2_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260902-eiken-grade2-2022-2-v1",
        "downloadName: 'ReadPass_EIKEN_Grade2_2022-2_Practice_Exam_Large_Type_v1.pdf'",
        "pages: 13",
    ):
        if required not in mapping_body:
            errors.append(f"[registration] print.js Grade 2 mapping missing: {required}")
if "print.js?v=20260902-grade2-2022-all-v1" not in print_html:
    errors.append("[registration] print.html cache identifier missing")

# 9. Fixed PDF: 13 A4 pages, required content, and deterministic rebuild
if not PDF_PATH.is_file():
    errors.append(f"[pdf] missing: {PDF_PATH}")
else:
    try:
        reader = PdfReader(str(PDF_PATH))
        if len(reader.pages) != 13:
            errors.append(f"[pdf] pages={len(reader.pages)} != 13")
        for index, page in enumerate(reader.pages, 1):
            if not is_a4(page, tolerance=0.02):
                errors.append(f"[pdf] page {index}: not A4")
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        for anchor in (
            "Trouble at Sea",
            "Performing Cats",
            "ZX950 LCD TV",
            "Dear Customer Service Representative",
            "Regards,",
            "Michael Green",
            "The Empress’s Favorite Clothes",
            "Desert Delight",
            "Q38",
            "大問3は正解番号のみ",
        ):
            if anchor not in pdf_text:
                errors.append(f"[pdf] text anchor missing: {anchor}")
    except Exception as exc:
        errors.append(f"[pdf] read failed: {exc}")
    with tempfile.TemporaryDirectory(prefix="readpass-g2-2022-2-") as temporary:
        regenerated = Path(temporary) / PDF_PATH.name
        command = [
            sys.executable,
            str(REPO / "scripts" / "build_fixed_exam_pdf.py"),
            "--grade", "grade2",
            "--exam", "2022-2",
            "--output", str(regenerated),
        ]
        result = subprocess.run(
            command,
            cwd=REPO,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            errors.append(f"[pdf] deterministic rebuild failed: {detail}")
        elif sha256(regenerated) != sha256(PDF_PATH):
            errors.append("[pdf] deterministic SHA-256 mismatch")

if errors:
    print(f"FAIL: {len(errors)} issue(s)")
    for error in errors:
        print(f" - {error}")
    print(f"  source-facing transcription SHA-256: {source_text_sha256}")
    raise SystemExit(1)

print("PASS: Grade 2 2022-2 comprehensive audit")
print(f"  questions: {len(questions)} (official answers matched)")
print(f"  passages: {len(passages)} / sentencePairs: {sum(PAIR_COUNTS.values())}")
print(f"  source-facing transcription SHA-256: {source_text_sha256}")
print(f"  vocabulary: {len(vocabulary)} / focusPoints: {len(focus_points)}")
print(f"  generated audio: {len(expected_audio)} (manifest input/audio SHA + full decode)")
print(f"  fixed PDF: 13 A4 pages / SHA-256 {sha256(PDF_PATH)}")
