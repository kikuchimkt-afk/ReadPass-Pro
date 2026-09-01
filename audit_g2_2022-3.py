# -*- coding: utf-8 -*-
"""Comprehensive local audit for ReadPass Grade 2 2022-3 (main venue)."""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import soundfile as sf
from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent
BASE = REPO / "data" / "grade2" / "2022-3"
DATA_PATH = BASE / "data.json"
GENERATOR_PATH = REPO / "gen_g2_2022-3.py"
SOURCE_DIR = Path(r"D:\Files\英検過去問\2級\2級2022-3")
PDF_PATH = REPO / "output" / "pdf" / "ReadPass_EIKEN_Grade2_2022-3_Practice_Exam_Large_Type_v1.pdf"

SOURCE_HASHES = {
    "2022-3-1ji-2kyu.pdf": "193cba78d43c203cf79b7abcef83f744e584cff588097bec24687c602f2436ab",
    "2022-3-1ji-2kyu-script.pdf": "85b5d73784dccea126b5e189486f5f1c4384fa64d53e79dd4dd5846a1cc61821",
    "2kyu-sun.pdf": "4762ca8ea025bf4f82bb394132fbce0cab84bb80b80607a80b26f76991d54932",
    "2Q-part1.mp3": "3491fc014dfe434c5d000580e408d1de105e59e0f819bd3eb8191e120b395a24",
    "2Q-part2.mp3": "e045da86e10f8c1a97bd9bbc9edb565ca11ae1572aa057b89aeba2c8306b6b1b",
}
SOURCE_PDF_PAGES = {
    "2022-3-1ji-2kyu.pdf": 24,
    "2022-3-1ji-2kyu-script.pdf": 11,
    "2kyu-sun.pdf": 1,
}
SOURCE_AUDIO = {
    "2Q-part1.mp3": (44100, 2, 33114639),
    "2Q-part2.mp3": (44100, 2, 36083632),
}
OFFICIAL = dict(enumerate([
    3, 1, 3, 1, 1, 4, 4, 3, 2, 2,
    1, 2, 3, 1, 1, 4, 3, 1, 3, 3,
    3, 4, 2, 3, 1, 3,
    1, 1, 3, 4, 1, 2, 4, 1, 3, 1, 3, 2,
], 1))
LISTENING = {
    "part1": dict(enumerate([2, 4, 2, 2, 3, 1, 2, 1, 2, 1, 4, 3, 2, 3, 4], 1)),
    "part2": dict(enumerate([4, 1, 2, 3, 4, 1, 4, 1, 2, 1, 3, 1, 4, 2, 2], 16)),
}
PAIR_COUNTS = {
    "Johnny Appleseed": 19,
    "Sea Shanties": 20,
    "Thank you for signing up": 15,
    "The King’s Little Path": 17,
    "The Evolution of Laughter": 17,
}
EXPECTED_TOP_KEYS = [
    "grade", "year", "session", "title", "exam", "sections", "listening",
    "vocabulary", "lessonPlan",
]
VOICE = "en-US-JennyNeural"
RATE = "-15%"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm(value):
    return re.sub(r"\s+", " ", value or "").strip()


def input_signature(text):
    payload = json.dumps(
        {"rate": RATE, "text": text, "voice": VOICE},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
errors = []

# 1. Original source identity, page counts, and complete source-audio decode.
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
        if reader.is_encrypted:
            reader.decrypt("")
        if len(reader.pages) != expected_pages:
            errors.append(f"[source-pdf] {filename}: pages={len(reader.pages)} != {expected_pages}")
        for index, page in enumerate(reader.pages, 1):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if abs(width - 595.276) > 0.5 or abs(height - 841.89) > 0.5:
                errors.append(f"[source-pdf] {filename} page {index}: not A4 ({width} x {height})")
    except Exception as exc:
        errors.append(f"[source-pdf] {filename}: cannot inspect: {exc}")
for filename, expected_metadata in SOURCE_AUDIO.items():
    path = SOURCE_DIR / filename
    if not path.is_file():
        continue
    try:
        decoded_frames = 0
        with sf.SoundFile(path) as audio:
            actual_metadata = (audio.samplerate, audio.channels, audio.frames)
            if actual_metadata != expected_metadata:
                errors.append(f"[source-audio] {filename}: {actual_metadata} != {expected_metadata}")
            while True:
                block = audio.read(262144, dtype="float32", always_2d=True)
                if len(block) == 0:
                    break
                decoded_frames += len(block)
        # libsndfile reports the MP3 header frame count including encoder delay/padding,
        # while its full sequential decode can omit up to one second of padding.
        if decoded_frames <= 0 or decoded_frames < expected_metadata[2] - expected_metadata[0]:
            errors.append(
                f"[source-audio] {filename}: decoded frame count is unexpectedly short "
                f"({decoded_frames} vs header {expected_metadata[2]})"
            )
    except Exception as exc:
        errors.append(f"[source-audio] {filename}: full decode failed: {exc}")

# 2. Deterministic generator-to-data synchronization.
if not GENERATOR_PATH.is_file():
    errors.append(f"[generator] missing: {GENERATOR_PATH}")
else:
    with tempfile.TemporaryDirectory(prefix="readpass-g2-2022-3-data-") as temporary:
        temporary_root = Path(temporary)
        temporary_generator = temporary_root / GENERATOR_PATH.name
        shutil.copy2(GENERATOR_PATH, temporary_generator)
        result = subprocess.run(
            [sys.executable, str(temporary_generator)],
            cwd=temporary_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        generated = temporary_root / "data" / "grade2" / "2022-3" / "data.json"
        if result.returncode != 0:
            errors.append(f"[generator] failed in temporary directory: {result.stderr.strip()}")
        elif not generated.is_file() or generated.read_bytes() != DATA_PATH.read_bytes():
            errors.append("[generator] generated data.json does not exactly match the registered file")

# 3. Metadata and section structure.
if list(data) != EXPECTED_TOP_KEYS:
    errors.append(f"[metadata] top-level keys/order: {list(data)}")
expected_metadata = {
    "grade": "2級",
    "year": "2022",
    "session": "3",
    "title": "2022年度 第3回 英語資格検定2級 リーディング",
    "exam": "2022-3",
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

# 4. Every question, translation, explanation, and evidence.
questions = []
for section in sections:
    questions.extend((question, None) for question in section.get("questions", []))
    for passage in section.get("passages", []):
        corpus = " ".join(passage.get("paragraphs", []))
        questions.extend((question, corpus) for question in passage.get("questions", []))
if [question.get("number") for question, _ in questions] != list(range(1, 39)):
    errors.append("[questions] numbers are not exactly Q1-Q38")
for question, corpus in questions:
    number = question.get("number")
    if number not in OFFICIAL:
        errors.append(f"[question] unexpected number: {number!r}")
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
        correct = analyses[question["answer"] - 1]
        if correct.count("→正解。💡") != 1:
            errors.append(f"[analysis] Q{number}: correct marker count != 1")
        if any("→正解" in text for index, text in enumerate(analyses, 1) if index != question["answer"]):
            errors.append(f"[analysis] Q{number}: wrong option marked correct")
        if any(text.lstrip().startswith(("✅", "❌", "○", "×")) for text in analyses):
            errors.append(f"[analysis] Q{number}: legacy leading symbol")
    if number <= 20:
        if not norm(question.get("text")) or not norm(question.get("translation")):
            errors.append(f"[question] Q{number}: text/translation missing")
    elif number >= 27:
        if not norm(question.get("question")) or not norm(question.get("questionTranslation")):
            errors.append(f"[question] Q{number}: question translation missing")
    if corpus is not None:
        evidence = question.get("sourceEvidence", [])
        if not evidence:
            errors.append(f"[evidence] Q{number}: sourceEvidence missing")
        for pattern in evidence:
            if norm(pattern).lower() not in norm(corpus).lower():
                errors.append(f"[evidence] Q{number}: not found in passage: {pattern!r}")

# 5. Official listening answer table.
for part, expected in LISTENING.items():
    actual = {int(key): value for key, value in data.get("listening", {}).get(part, {}).items()}
    if actual != expected:
        errors.append(f"[listening] {part} does not match official answers")

# 6. Passage translations, sentence popups, and typography anchors.
passages = []
for section in sections[1:]:
    passages.extend(section.get("passages", []))
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
    for pair in pairs:
        if len(pair) != 4 or not all(norm(value) for value in pair[:3]):
            errors.append(f"[sentencePairs] {title}: malformed pair")
            continue
        if pair[0] not in corpus:
            errors.append(f"[sentencePairs] {title}: English sentence not found: {pair[0]!r}")
        if pair[0] in seen_english:
            errors.append(f"[sentencePairs] {title}: duplicate sentence")
        if pair[2] != f"{pair[0]}|{pair[1]}":
            errors.append(f"[sentencePairs] {title}: slash guide mismatch: {pair[0]!r}")
        seen_english.add(pair[0])

passage_by_title = {passage.get("title"): passage for passage in passages}
typography_anchors = {
    "Johnny Appleseed": ["Appleseed’s dream", "Chapman’s life"],
    "Sea Shanties": ["“sea shanties,”", "“Capstan shanties”", "ships’ engines"],
    "Thank you for signing up": ["people’s costumes", "convention center’s cafeteria"],
    "The King’s Little Path": ["walkway’s amazing views", "“the king’s little path.”"],
    "The Evolution of Laughter": ["a chimpanzee’s way"],
}
for title, anchors in typography_anchors.items():
    passage = passage_by_title.get(title)
    if not passage:
        errors.append(f"[typography] passage missing: {title}")
        continue
    corpus = " ".join(passage.get("paragraphs", []))
    pair_corpus = " ".join(pair[0] for pair in passage.get("sentencePairs", []) if pair)
    for anchor in anchors:
        if anchor not in corpus:
            errors.append(f"[typography] {title}: paragraph anchor missing: {anchor!r}")
        if anchor not in pair_corpus:
            errors.append(f"[typography] {title}: sentencePair anchor missing: {anchor!r}")
serialized = json.dumps(data, ensure_ascii=False)
for anchor in (
    "The King’s Little Path", "The Evolution of Laughter",
    "chimpanzees’ laughter", "humans’ laughter", "humans’ brains",
    "science-fiction", "great-grandfathers", "fast-flowing", "one-meter-wide",
    "eight-kilometer", "laughter-like", "King Alfonso XIII", "2.2 million euros",
    "300,000 tickets",
):
    if anchor not in serialized:
        errors.append(f"[typography] global anchor missing: {anchor!r}")

# 7. Email fields, greeting, closing, and signature.
email_passage = passage_by_title.get("Thank you for signing up")
if email_passage is None:
    errors.append("[email] Thank you for signing up passage missing")
else:
    expected_meta = {
        "from": "Gravelton Comic Show <info@graveltoncomicshow.com>",
        "to": "Alice Sullivan <alisulli321@friendlymail.com>",
        "date": "January 22",
        "subject": "Thank you for signing up",
    }
    if email_passage.get("format") != "email":
        errors.append("[email] format=email missing")
    if email_passage.get("meta") != expected_meta:
        errors.append(f"[email] metadata mismatch: {email_passage.get('meta')}")
    email_paragraphs = email_passage.get("paragraphs") or [None]
    email_translations = email_passage.get("translations") or [None]
    checks = [
        (email_paragraphs[0], "Dear Alice,", "greeting"),
        (email_paragraphs[-2], "We look forward to seeing you at the show!", "closing"),
        (email_paragraphs[-1], "Gravelton Comic Show Staff", "signature"),
        (email_translations[0], "アリス様", "greeting translation"),
        (email_translations[-1], "グラベルトン・コミックショー運営スタッフ", "signature translation"),
    ]
    for actual, expected, label in checks:
        if actual != expected:
            errors.append(f"[email] {label} missing or changed")

# 8. Vocabulary, Focus Points, generated audio, and manifest integrity.
vocabulary = data.get("vocabulary", [])
if len(vocabulary) != 65 or len({item.get("word") for item in vocabulary}) != 65:
    errors.append(f"[vocabulary] expected 65 unique words; got {len(vocabulary)}")
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"[focus] expected 5; got {len(focus_points)}")
expected_audio_inputs = {}
for item in vocabulary:
    for field in ("word", "meaning", "pos", "level", "source", "example", "exampleJa", "wordAudio"):
        if not norm(item.get(field, "")):
            errors.append(f"[vocabulary] {item.get('word')}: {field} missing")
    if len(item.get("distractors", [])) != 3 or item.get("meaning") in item.get("distractors", []):
        errors.append(f"[vocabulary] {item.get('word')}: invalid distractors")
    expected_audio_inputs[item.get("wordAudio")] = item.get("word", "")
for index, point in enumerate(focus_points, 1):
    for field in ("id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation", "highlightLabel"):
        if not norm(point.get(field, "")):
            errors.append(f"[focus] fp{index}: {field} missing")
    if len(point.get("examples", [])) != 3:
        errors.append(f"[focus] fp{index}: examples count != 3")
    elif any(not all(norm(example.get(key, "")) for key in ("en", "ja", "note")) for example in point["examples"]):
        errors.append(f"[focus] fp{index}: malformed example")
    if len(point.get("practiceQuestions", [])) != 4:
        errors.append(f"[focus] fp{index}: practiceQuestions count != 4")
    practice = point.get("practicePassage", {})
    english = norm(practice.get("en"))
    if not english or not norm(practice.get("ja")):
        errors.append(f"[focus] fp{index}: practice passage missing")
    if not practice.get("en", "").startswith("[Source:"):
        errors.append(f"[focus] fp{index}: practice source header missing")
    spoken = re.sub(r"\[Source:.*?\]\s*", "", practice.get("en", ""), count=1).strip()
    expected_audio_inputs[practice.get("audioFile")] = spoken
manifest_path = BASE / "audio" / "tts_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {}
if set(manifest) != set(expected_audio_inputs) or len(expected_audio_inputs) != 70:
    errors.append(f"[audio] manifest/path set mismatch: manifest={len(manifest)} expected={len(expected_audio_inputs)}")
for relative, spoken_text in sorted(expected_audio_inputs.items()):
    if not relative:
        errors.append("[audio] empty audio path")
        continue
    path = BASE / relative
    entry = manifest.get(relative, {})
    if not path.is_file() or path.stat().st_size < 500:
        errors.append(f"[audio] missing/small: {relative}")
        continue
    if entry.get("audioSha256") != sha256(path):
        errors.append(f"[audio] SHA-256 mismatch: {relative}")
    if entry.get("inputSha256") != input_signature(spoken_text):
        errors.append(f"[audio] input SHA-256 mismatch: {relative}")
    try:
        decoded_frames = 0
        with sf.SoundFile(path) as audio:
            while True:
                block = audio.read(262144, dtype="float32", always_2d=True)
                if len(block) == 0:
                    break
                decoded_frames += len(block)
            if decoded_frames <= 0 or audio.samplerate <= 0 or audio.channels <= 0:
                errors.append(f"[audio] invalid stream metadata: {relative}")
    except Exception as exc:
        errors.append(f"[audio] full decode failed: {relative}: {exc}")

# 9. Grade 2-limited UI and print registration.
top_js = (REPO / "top.js").read_text(encoding="utf-8")
print_js = (REPO / "print.js").read_text(encoding="utf-8")
print_html = (REPO / "print.html").read_text(encoding="utf-8")
top_grade2_start = top_js.find("id: 'grade2'")
top_grade2_end = top_js.find("id: 'grade-pre2plus'", top_grade2_start)
top_grade2_block = top_js[top_grade2_start:top_grade2_end] if top_grade2_start >= 0 and top_grade2_end > top_grade2_start else ""
top_entry = "{ id: '2022-3', label: '2022年度 第3回', sub: '一次試験リーディング' }"
if top_grade2_block.count(top_entry) != 1:
    errors.append("[registration] top.js Grade 2 catalog entry missing or duplicated")
print_grade2_start = print_js.find("id: 'grade2',")
print_grade2_end = print_js.find("id: 'grade-pre2plus',", print_grade2_start)
print_grade2_block = print_js[print_grade2_start:print_grade2_end] if print_grade2_start >= 0 and print_grade2_end > print_grade2_start else ""
if print_grade2_block.count("{ id: '2022-3', label: '2022年度 第3回' }") != 1:
    errors.append("[registration] print.js Grade 2 catalog entry missing or duplicated")
fixed_start = print_js.find("'grade2/2022-1':")
fixed_end = print_js.find("'grade2/2023-1':", fixed_start)
fixed_grade2_2022_block = print_js[fixed_start:fixed_end] if fixed_start >= 0 and fixed_end > fixed_start else ""
for required in (
    "'grade2/2022-3':",
    "ReadPass_EIKEN_Grade2_2022-3_Practice_Exam_Large_Type_v1.pdf",
    "20260902-eiken-grade2-2022-3-v1",
    "pages: 13",
):
    if required not in fixed_grade2_2022_block:
        errors.append(f"[registration] print.js Grade 2 2022 fixed-PDF block missing: {required}")
if "print.js?v=20260902-grade2-2022-all-v1" not in print_html:
    errors.append("[registration] print.html cache identifier missing")

# 10. Fixed PDF: 13 A4 pages, required text, and deterministic regeneration.
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
        "Johnny Appleseed", "Sea Shanties", "Dear Alice",
        "Gravelton Comic Show Staff", "The King’s Little Path",
        "The Evolution of Laughter", "Q38", "大問3は正解番号のみ",
    ):
        if anchor not in pdf_text:
            errors.append(f"[pdf] text anchor missing: {anchor}")
    with tempfile.TemporaryDirectory(prefix="readpass-g2-2022-3-pdf-") as temporary:
        regenerated = Path(temporary) / PDF_PATH.name
        command = [
            sys.executable,
            str(REPO / "scripts" / "build_fixed_exam_pdf.py"),
            "--grade", "grade2",
            "--exam", "2022-3",
            "--output", str(regenerated),
        ]
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            errors.append(f"[pdf] deterministic rebuild failed: {result.stderr.strip()}")
        elif not regenerated.is_file() or sha256(regenerated) != sha256(PDF_PATH):
            errors.append("[pdf] deterministic SHA-256 mismatch")

if errors:
    print(f"FAIL: {len(errors)} issue(s)")
    for error in errors:
        print(f" - {error}")
    raise SystemExit(1)

print("PASS: Grade 2 2022-3 comprehensive audit")
print(f"  questions: {len(questions)} (official answers matched)")
print(f"  passages: {len(passages)} / sentencePairs: {sum(PAIR_COUNTS.values())}")
print(f"  vocabulary: {len(vocabulary)} / focusPoints: {len(focus_points)}")
print(f"  generated audio: {len(expected_audio_inputs)} (input SHA + audio SHA + full decode)")
print(f"  fixed PDF: 13 A4 pages / SHA-256 {sha256(PDF_PATH)}")
