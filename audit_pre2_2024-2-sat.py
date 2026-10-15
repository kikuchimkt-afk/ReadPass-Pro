"""Audit ReadPass Grade Pre-2 2024-2 Saturday sub-venue data and assets.

Paper: 2024年度 第2回 準2級, 土曜日準会場, 2024年10月5日（土）実施.

The booklet PDF is a scan whose text layer is noisy OCR ("fbr", "wann",
"infbnnation", glued and split words). Every English field (Part 1-2 stems and
choices, the Part 3 story, the e-mail headers and body, the Part 4B passage, the
reading stems and choices) was therefore transcribed from the page images rendered
at 220-500 dpi, and the text layer is used only as a cross-check. Two independent
readings of booklet pages 3-9 (PDF index 2-8) are compared with the transcription:

* Tesseract OCR (eng) of the pages rendered at 300 dpi, word by word in both
  directions after folding the usual scanner confusions (l/1/I/i/|, o/0, y/v,
  accents), and sentence by sentence (contiguous word order) for every English
  sentence;
* the booklet's own OCR text layer, word by word in both directions with the same
  folding (its word order is too broken for a sentence comparison).

The words and sentences the readers garble are listed in UNREAD, NOISE,
OCR_SENTENCE_MISREADS, LAYER_UNREAD and LAYER_NOISE; each was checked against the
page image, and the lists must match exactly, so a new transcription error cannot
hide behind them. The official answer sheet (a born-digital PDF) is parsed
independently with pypdf and PyMuPDF. After those checks the English source
payload is frozen by EXPECTED_SOURCE_PAYLOAD_SHA256.

Use --skip-sources only on hosts without the local original PDFs (or without
Tesseract), and --require-audio once data/grade-pre2/2024-2-sat/_gen_tts.py has
been run.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data" / "grade-pre2" / "2024-2-sat"
DATA_PATH = BASE / "data.json"
GENERATOR_PATH = ROOT / "gen_pre2_2024-2-sat.py"
GENERATOR_GLOB = "gen_pre2_2024-2-sat*.py"
PDF_NAME = "ReadPass_EIKEN_GradePre2_2024-2-sat_Practice_Exam_Large_Type_v1.pdf"
GUIDE_NAME = "ReadPass_EIKEN_GradePre2_2024-2-sat_Grammar_Guide_v1.pdf"
PRACTICE_PAGES = 10
SOURCE_ROOT = Path(r"D:\Files\英検過去問\土曜準会場\2024-2（土曜）")
BOOKLET = SOURCE_ROOT / "準2級問題.pdf"
ANSWER_SHEET = SOURCE_ROOT / "解答" / "準２級.pdf"  # full-width ２ in the file name
SOURCE_HASHES = {
    BOOKLET: "4A4B9FD5D5A8FF15AFD909A476B069C7F2B9E4702A04AE6345A18E79CE36AB54",
    ANSWER_SHEET: "AE2F631C364B05D3A2638D1C41B3D30F6A2B6A936E34135101831E7BB0230EE7",
}
OFFICIAL_ANSWERS = [
    4, 3, 1, 1, 1, 2, 4, 2, 2, 2,
    3, 1, 3, 3, 4, 3, 4, 1, 2, 4,
    3, 1, 4, 3, 2, 1, 4, 3, 1,
]
EXPECTED_PASSAGES = {
    "First Camping Trip": (2, 13, 2),
    "Helpful employee": (3, 15, 3),
    "Magazines in the Digital Age": (4, 22, 4),
}
EMAIL_META = {
    "from": "Joyce Dixon <joyce_dixon@goodmail.com>",
    "to": "Customer Service <cusserv@tennmart.com>",
    "date": "October 5",
    "subject": "Helpful employee",
}
# Greeting and sign-off lines of the e-mail are kept in the paragraphs (as in
# 2024-1-sat) but are not sentences, so they have no sentencePairs row.
EMAIL_FRAME = ["Dear Customer Service,", "Best regards, Joyce Dixon"]
# Frozen after the page-image transcription and the OCR / text-layer cross-check.
EXPECTED_SOURCE_PAYLOAD_SHA256 = "08f26fecd3c1e8dfe61dfe167f4facb69a7b3f54a4aa9b6c98127d08f9f00817"

# --- OCR cross-check -------------------------------------------------------
TESSERACT_CANDIDATES = [
    Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
    Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
]
OCR_PAGES = range(2, 9)  # PDF index; printed page = index + 1
OCR_DPI = 300
FOLD = str.maketrans({"1": "l", "|": "l", "!": "l", "i": "l", "0": "o", "v": "y", "$": "s"})
# Transcribed words (folded) that the Tesseract OCR does not read: none, every
# transcribed word is read somewhere on its page.
UNREAD: set[tuple[int, str]] = set()
# Tesseract words (folded, 3+ letters) with no transcribed counterpart: the
# "Grade Pre-2" running head and the Japanese instruction lines of Parts 1-4,
# which the eng model turns into letter noise (checked on each page image).
NOISE = {(page, "grade") for page in OCR_PAGES} | {(page, "pre") for page in (3, 4, 5, 6, 7)} | {
    (2, "eoe"), (2, "mcansokcrebde"), (2, "oru"), (2, "torsemarmomemlcy"),
    (4, "chru"), (4, "guncoel"), (4, "lcashendelthrh"), (4, "lcy"),
    (4, "robmlomsmnyermalysehlc"), (4, "toblemabmomem"),
    (5, "adhps"), (5, "boblcooe"), (5, "cmu"), (5, "lta"), (5, "premlcy"), (5, "rormega"),
    (5, "tonmeblct"), (5, "torsemshmo"), (5, "weahso"),
    (6, "bloarlcmult"), (6, "cobol"), (6, "dru"), (6, "ersamomemlcy"),
    (6, "hellnmerkmacaydlcrdbdlede"), (6, "hhdled"), (6, "rna"), (6, "tors"),
}
# Sentences whose words Tesseract does not read in one run, checked on the image:
# p.4 (11) the grey side bar is read as "|" before "instead"; p.5 (17) "I'd like to
# ( 17 )" is read as "'dliketo( J7 )"; p.7 the e-mail's "I'm writing" loses its "I"
# and the box edge after "Your employee" is read as "|".
OCR_SENTENCE_MISREADS = {
    (3, "Why do you ride a bike instead of taking the train?"),
    (4, "I'd like to ( )."),
    (6, "Dear Customer Service, I'm writing to you about one of your employees at the downtown store."),
    (6, "Your employee Mark Brown was a big help."),
}
# Transcribed words (folded) that the booklet's own OCR text layer garbles or
# drops; each confirmed on the rendered page and read correctly by Tesseract.
# The layer reads "for" as "fbr" (and "fo"/"fu" inside words: comfbrtable, fbod,
# fbrecast, fbllow, fbrget, perfbrmance, befbre, fbund, infbrmation), "fi"/"ff" as
# "fl"/"h"/"廿" (fiom, oflce, oflen, aflald, fifiend, suhered, oher, 廿ee, oH),
# "rn"/"m" as "nn"/"m" (wann, wanner, momlng, infbnnation, remmed for returned),
# "tu" as "m" (acmally, Samrday), "find"/"five" as "6nd"/"nve", "full" as "filll",
# "softball" glued as "ssofiballgame", "taxes" as "taxcs", "successful" as
# "successfill", "different" as "diferent", "NME" as "MIm"/"Am", the italic titles
# "First Camping Trip"/"Magazines in the Digital Age" as Japanese glyph noise, the
# e-mail addresses as "qoodmail"/"tennmait", "does" inside the glued Q25 stem, and
# the "!" of "forget!"/"performance!" (folded to "l") as a separate mark.
LAYER_UNREAD = {
    (2, "comfortable"), (2, "flnd"), (2, "flye"), (2, "food"), (2, "for"), (2, "forecast"),
    (2, "from"), (2, "returned"), (2, "softball"), (2, "taxes"), (2, "warm"),
    (3, "for"), (3, "from"), (3, "mornlng"), (3, "off"), (3, "offlce"), (3, "often"),
    (4, "actually"), (4, "afrald"), (4, "follow"), (4, "for"), (4, "forgetl"), (4, "free"),
    (4, "frlends"), (4, "full"), (4, "performancel"), (4, "saturday"),
    (5, "before"), (5, "flrst"), (5, "food"), (5, "for"), (5, "frlend"), (5, "warmer"),
    (6, "does"), (6, "frlend"), (6, "goodmall"), (6, "tennmart"),
    (7, "dlgltal"), (7, "for"), (7, "found"), (7, "from"), (7, "lnformatlon"), (7, "nme"),
    (7, "offer"), (7, "successful"), (7, "suffered"),
    (8, "before"), (8, "dlfferent"), (8, "for"), (8, "free"), (8, "lnformatlon"),
}
# Text-layer words (folded, 3+ letters) with no transcribed counterpart: the
# garbled readings above, the running head ("Grade", "Pre", "G rade"), stems
# glued into one run (Q16 line 1, Q17 choice 3, Q23, Q25), "B:Wow" as "BfWow",
# "after" as "afier", "sky" as "sIq", "Joyce" as "iovce", the side-bar texture
# read as "KII"/"lllllllll", "from" in "far from" as "廿OIn", and "&h晴FmE" noise.
LAYER_NOISE = {(page, "grade") for page in OCR_PAGES if page != 5} | {(page, "pre") for page in (3, 4, 6, 7)} | {
    (2, "afler"), (2, "comfbrtable"), (2, "fbod"), (2, "fbr"), (2, "fbrecast"), (2, "flom"),
    (2, "remmed"), (2, "ssoflballgame"), (2, "taxcs"), (2, "wann"),
    (3, "fbr"), (3, "momlng"), (3, "oflce"), (3, "oflen"), (3, "oln"),
    (4, "acmally"), (4, "aflald"), (4, "bfwow"), (4, "fbllow"), (4, "fbr"), (4, "fbrgetl"),
    (4, "flflends"), (4, "fllll"), (4, "kll"), (4, "mplaylngtheylollnlnaconcertonsamrday"),
    (4, "payfbrmytrlp"), (4, "perfbrmance"), (4, "samrday"),
    (5, "befbre"), (5, "fbod"), (5, "fbr"), (5, "flflend"), (5, "fme"), (5, "rade"), (5, "slq"),
    (5, "wanner"),
    (6, "fbr"), (6, "loyce"), (6, "qoodmall"), (6, "tennmalt"),
    (6, "whatdocsjoyccwantthestorctodofbrherandhcrfamlly"), (6, "whylsjoycedlxonwrltlngthlsc"),
    (7, "fbr"), (7, "fbund"), (7, "flom"), (7, "lllllllll"), (7, "lnfbnnatlon"), (7, "lnfbrmatlon"),
    (7, "lntemet"), (7, "mlm"), (7, "oher"), (7, "successflll"), (7, "suhered"),
    (8, "befbre"), (8, "dlferent"), (8, "fbr"), (8, "lnfbnnatlon"),
}
ENGLISH_FIELD_COUNT = 158

# Vocabulary entries whose form in the exam differs from the headword.
VOCAB_SOURCE_FORMS = {"make one's bed": "makes his bed", "run out": "runs out", "find out": "found out"}
FOCUS_IDS = ["fp1", "fp2", "fp3", "fp4", "fp5"]
FOCUS_COLORS = ["#4f8cff", "#f472b6", "#34d399", "#fbbf24", "#f59e0b"]
AUDIO_COUNT = 45
MIN_AUDIO_BYTES = 6000


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def compact(value: str) -> str:
    return re.sub(r"\s+", "", value)


def fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", unicodedata.normalize("NFKC", text))
    return "".join(c for c in text if not unicodedata.combining(c)).lower().translate(FOLD)


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", fold(text))


def strip_blank_numbers(text: str) -> str:
    """'( 16 )' -> '( )': Part 1 prints empty blanks, the OCR reads '( 17 _ )'."""
    return re.sub(r"\(\s*\d+[^)]*\)", "( )", text)


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


def payload_digest(data: dict) -> str:
    payload_bytes = json.dumps(
        source_payload(data), ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload_bytes).hexdigest()


def english_fields(sections: list[dict]) -> list[tuple[int, str]]:
    """(booklet PDF page index, text) for every English field."""
    fields: list[tuple[int, str]] = []
    for question in sections[0]["questions"] + sections[1]["questions"]:
        number = question["number"]
        page = 2 if number <= 10 else 3 if number <= 15 else 4
        fields.append((page, strip_blank_numbers(question["text"])))
        fields.extend((page, choice) for choice in question["choices"])
    story = sections[2]["passages"][0]
    fields.append((5, story["title"]))
    fields.extend((5, strip_blank_numbers(paragraph)) for paragraph in story["paragraphs"])
    for question in story["questions"]:
        fields.extend((5, choice) for choice in question["choices"])
    email, article = sections[3]["passages"]
    fields.extend((6, f"{key.capitalize()}: {value}") for key, value in email["meta"].items())
    fields.extend((6, paragraph) for paragraph in email["paragraphs"])
    for question in email["questions"]:
        fields.append((6, question["question"]))
        fields.extend((6, choice) for choice in question["choices"])
    fields.append((7, article["title"]))
    fields.extend((7, paragraph) for paragraph in article["paragraphs"])
    for question in article["questions"]:
        fields.append((8, question["question"]))
        fields.extend((8, choice) for choice in question["choices"])
    return fields


def tesseract_path() -> Path | None:
    found = shutil.which("tesseract")
    if found:
        return Path(found)
    return next((path for path in TESSERACT_CANDIDATES if path.is_file()), None)


def ocr_booklet(exe: Path) -> dict[int, str]:
    import fitz

    document = fitz.open(BOOKLET)
    env = dict(os.environ, OMP_THREAD_LIMIT="1")
    with tempfile.TemporaryDirectory(prefix="pre2-2024-2-sat-ocr-") as temp:
        images = {}
        for index in OCR_PAGES:
            image = Path(temp) / f"p{index:02d}.png"
            document[index].get_pixmap(dpi=OCR_DPI, colorspace=fitz.csGRAY).save(image)
            images[index] = image

        def read(index: int) -> tuple[int, str]:
            result = subprocess.run(
                [str(exe), str(images[index]), "stdout", "-l", "eng", "--psm", "3"],
                capture_output=True, text=True, encoding="utf-8", env=env, check=True,
            )
            return index, result.stdout

        with ThreadPoolExecutor(max_workers=4) as pool:
            return dict(pool.map(read, OCR_PAGES))


def text_layer() -> dict[int, str]:
    import fitz

    document = fitz.open(BOOKLET)
    return {index: document[index].get_text() for index in OCR_PAGES}


def word_differences(
    layer: dict[int, str], fields: list[tuple[int, str]], strip: bool = True
) -> tuple[set[tuple[int, str]], set[tuple[int, str]]]:
    """(transcribed words the reading lacks, reading words not transcribed).

    The text layer prints "(" and ")" of a blank on separate lines around the
    choice numbers, so stripping blank numbers there would eat whole questions:
    strip=False keeps it as it is.
    """
    if strip:
        layer = {index: strip_blank_numbers(text) for index, text in layer.items()}
    layer_words = {index: set(words(text)) for index, text in layer.items()}
    layer_compact = {index: "".join(words(text)) for index, text in layer.items()}
    unread = {
        (page, word)
        for page, text in fields
        for word in words(text)
        if word not in layer_words[page] and word not in layer_compact[page]  # glued words count as read
    }
    mine = {
        index: "".join(word for page, text in fields if page == index for word in words(text))
        for index in layer
    }
    extra = {
        (index, word)
        for index, text in layer.items()
        for word in words(text)
        if len(word) >= 3 and word.isalpha() and word not in mine[index]
    }
    return unread, extra


def sentence_units(text: str) -> list[str]:
    return [part for part in re.split(r"(?<=[.?!])\s+|\n", text) if part.strip()]


def sentence_misreads(layer: dict[int, str], fields: list[tuple[int, str]]) -> set[tuple[int, str]]:
    layer_compact = {index: "".join(words(strip_blank_numbers(text))) for index, text in layer.items()}
    return {
        (page, unit)
        for page, text in fields
        for unit in sentence_units(text)
        if "".join(words(unit)) not in layer_compact[page]
    }


def filled(text: str, question: dict) -> str:
    return re.sub(
        rf"\(\s*{question['number']}\s*\)", question["choices"][question["answer"] - 1], text
    )


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-sources", action="store_true")
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--show-source-hash", action="store_true")
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if args.show_source_hash:
        print(payload_digest(data))
        return
    errors: list[str] = []
    notes: list[str] = []

    def check(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)

    sections = data["sections"]
    questions = collect_questions(data)
    passages = [passage for section in sections for passage in section.get("passages", [])]

    # Source identity, official key, OCR and text-layer cross-check.
    if args.skip_sources:
        notes.append("--skip-sources: 原本PDF・OCR照合をスキップ")
    else:
        import fitz

        for source_path, expected_hash in SOURCE_HASHES.items():
            if not source_path.is_file():
                errors.append(f"原本なし: {source_path}（原本のない環境では --skip-sources）")
                continue
            actual_hash = sha256_file(source_path)
            check(actual_hash == expected_hash, f"原本SHA不一致: {source_path.name}: {actual_hash}")
        if ANSWER_SHEET.is_file():
            expected_key = dict(enumerate(OFFICIAL_ANSWERS, start=1))
            for reader_name, text in (
                ("pypdf", PdfReader(ANSWER_SHEET).pages[0].extract_text()),
                ("PyMuPDF", fitz.open(ANSWER_SHEET)[0].get_text()),
            ):
                check("2024年度 第2回" in text and "10月5日（土）実施" in text, f"解答PDF ({reader_name}): 回・実施日が不一致")
                check("準2級" in text, f"解答PDF ({reader_name}): 級の表示がない")
                key = {int(n): int(a) for n, a in re.findall(r"\((\d+)\)\s+([1-4])", text)}
                check(key == expected_key, f"解答PDF ({reader_name}): 公式解答とOFFICIAL_ANSWERSが不一致")
        if BOOKLET.is_file():
            fields = english_fields(sections)
            check(len(fields) == ENGLISH_FIELD_COUNT, f"英語フィールド数 {len(fields)} != {ENGLISH_FIELD_COUNT}")
            layer_unread, layer_extra = word_differences(text_layer(), fields, strip=False)
            check(layer_unread == LAYER_UNREAD, f"転記語がテキスト層にない: new {sorted(layer_unread - LAYER_UNREAD)[:6]}, stale {sorted(LAYER_UNREAD - layer_unread)[:6]}")
            check(layer_extra == LAYER_NOISE, f"テキスト層の語が転記にない: new {sorted(layer_extra - LAYER_NOISE)[:6]}, stale {sorted(LAYER_NOISE - layer_extra)[:6]}")
            notes.append(f"テキスト層照合: {len(fields)}フィールド / 誤読リスト {len(LAYER_UNREAD)}語")
            exe = tesseract_path()
            if exe is None:
                errors.append("Tesseract OCRが見つからない（OCR照合には必須。原本のない環境では --skip-sources）")
            else:
                layer = ocr_booklet(exe)
                unread, extra = word_differences(layer, fields)
                check(unread == UNREAD, f"転記語がOCRにない: new {sorted(unread - UNREAD)[:6]}, stale {sorted(UNREAD - unread)[:6]}")
                check(extra == NOISE, f"OCRの語が転記にない: new {sorted(extra - NOISE)[:6]}, stale {sorted(NOISE - extra)[:6]}")
                broken = sentence_misreads(layer, fields)
                check(
                    broken == OCR_SENTENCE_MISREADS,
                    f"語順がOCRと一致しない文: new {sorted(broken - OCR_SENTENCE_MISREADS)[:4]}, stale {sorted(OCR_SENTENCE_MISREADS - broken)[:4]}",
                )
                notes.append(f"OCR照合: {len(fields)}フィールド / 誤読リスト {len(UNREAD)}語・{len(OCR_SENTENCE_MISREADS)}文 ({exe.name})")

    # Reproducible JSON generation (in-process and byte-identical in isolation).
    spec = importlib.util.spec_from_file_location("pre2_2024_2_sat_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        errors.append("generatorを読み込めない")
    else:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        check(module.build_data() == data, "data.jsonがgeneratorのbuild_data()と一致しない")
        check(module.OFFICIAL_ANSWERS == OFFICIAL_ANSWERS, "generatorのOFFICIAL_ANSWERSが監査と一致しない")
    with tempfile.TemporaryDirectory(prefix="pre2-2024-2-sat-gen-") as temp:
        folder = Path(temp)
        for script in ROOT.glob(GENERATOR_GLOB):
            shutil.copy2(script, folder / script.name)
        process = subprocess.run(
            [sys.executable, "-I", str(folder / GENERATOR_PATH.name)],
            capture_output=True, text=True, encoding="utf-8",
        )
        output = folder / "data" / "grade-pre2" / "2024-2-sat" / "data.json"
        check(process.returncode == 0, f"isolated generator execution: {process.stderr[-300:]}")
        check(
            process.returncode == 0 and output.read_bytes() == DATA_PATH.read_bytes(),
            "generatorの単独実行結果がdata.jsonとバイト一致しない",
        )

    # Metadata and section schema.
    check(
        (data.get("grade"), data.get("year"), data.get("session"), data.get("title"))
        == ("準2級", "2024", "2", "2024年度 第2回（土曜準会場） 英語資格検定準2級 リーディング"),
        "grade/year/session/titleが期待値と一致しない",
    )
    expected_sections = [
        ("大問1", "vocabulary", 15, 0),
        ("大問2", "vocabulary", 5, 0),
        ("大問3", "passage-fill", 0, 1),
        ("大問4", "reading-comprehension", 0, 2),
    ]
    if len(sections) != 4:
        errors.append(f"sections={len(sections)} != 4")
    else:
        for section, (name, section_type, question_count, passage_count) in zip(sections, expected_sections):
            check((section.get("name"), section.get("type")) == (name, section_type), f"{name}: name/type不一致")
            check(len(section.get("questions", [])) == question_count, f"{name}: questions件数不一致")
            check(len(section.get("passages", [])) == passage_count, f"{name}: passages件数不一致")
            check(bool(section.get("instruction")), f"{name}: instruction欠落")

    # Frozen English source payload and official answers.
    digest = payload_digest(data)
    check(
        digest == EXPECTED_SOURCE_PAYLOAD_SHA256,
        f"原文payload SHA不一致: {digest} != {EXPECTED_SOURCE_PAYLOAD_SHA256}",
    )
    check([q.get("number") for q in questions] == list(range(1, 30)), "設問番号が1〜29の連番ではない")
    check([q.get("answer") for q in questions] == OFFICIAL_ANSWERS, "Q1〜29の正答が公式解答と一致しない")

    for q in questions:
        number = q["number"]
        check(
            all(len(q.get(key, [])) == 4 and all(q.get(key, [])) for key in ("choices", "choiceTranslations", "choiceAnalysis")),
            f"Q{number}: choices/訳/解説が4件ではない",
        )
        check(len(set(q.get("choices", []))) == 4, f"Q{number}: 選択肢が重複")
        check(q.get("grammar", "").startswith("💡 ") and len(q.get("grammar", "")) >= 25, f"Q{number}: grammar欠落または短すぎる")
        if number <= 20:
            check(bool(q.get("text")) and bool(q.get("translation")), f"Q{number}: 問題文または訳欠落")
            check(f"( {number} )" in q.get("text", "") and f"（{number}）" in q.get("translation", ""), f"Q{number}: 空所番号が原文/訳にない")
            check(q.get("text", "").count("\n") == q.get("translation", "").count("\n"), f"Q{number}: 会話の行数が原文と訳で違う")
        if number >= 23:
            check(bool(q.get("question")) and bool(q.get("questionTranslation")), f"Q{number}: questionまたはquestionTranslation欠落")
        analyses = q.get("choiceAnalysis", [])
        for index, analysis in enumerate(analyses, start=1):
            if number <= 15:
                marker = "✅" if index == q["answer"] else "❌"
                check(analysis.startswith(marker), f"Q{number} choice{index}: 正誤marker不一致")
                check(q["choices"][index - 1] in analysis, f"Q{number} choice{index}: 解説が選択肢に触れていない")
            else:
                check(not analysis.startswith(("✅", "❌", "○")), f"Q{number} choice{index}: 先頭markerは同年度形式外")
                check(("→正解。💡" in analysis) == (index == q["answer"]), f"Q{number} choice{index}: 正解marker不一致")
                if index == q["answer"]:
                    check(bool(analysis.split("→正解。💡", 1)[-1].strip()), f"Q{number}: 正解の根拠（💡の後）が空")
            check(len(analysis) >= 15, f"Q{number} choice{index}: 解説が短すぎる")
            check("。。" not in analysis, f"Q{number} choice{index}: 句点の重複")
        check(not any("とはない" in analysis for analysis in analyses), f"Q{number}: 「とはない」は「とは書かれていない」にする")
    check(questions[18]["text"] == questions[19]["text"], "Q19/Q20の会話文が共有されていない")

    # Passages, e-mail metadata, translations, and sentence pairs.
    check({p.get("title") for p in passages} == set(EXPECTED_PASSAGES), "長文タイトルが期待値と一致しない")
    for passage in passages:
        title = passage.get("title")
        if title not in EXPECTED_PASSAGES:
            continue
        expected_paragraphs, expected_pairs, expected_questions = EXPECTED_PASSAGES[title]
        check(len(passage.get("paragraphs", [])) == expected_paragraphs, f"{title}: paragraphs件数不一致")
        check(len(passage.get("translations", [])) == expected_paragraphs and all(passage.get("translations", [])), f"{title}: translations件数不一致")
        check(len(passage.get("sentencePairs", [])) == expected_pairs, f"{title}: sentencePairs件数不一致")
        check(len(passage.get("questions", [])) == expected_questions, f"{title}: questions件数不一致")
        corpus = " ".join(passage.get("paragraphs", []))
        for pair_index, pair in enumerate(passage.get("sentencePairs", []), start=1):
            if not isinstance(pair, list) or len(pair) != 2 or not all(pair):
                errors.append(f"{title}: sentencePairs[{pair_index}]が不正")
            elif pair[0] not in corpus:
                errors.append(f"{title}: sentencePairs[{pair_index}]が原文にない")
            else:
                for q in passage["questions"]:
                    check((f"( {q['number']} )" in pair[0]) == (f"（{q['number']}）" in pair[1]), f"{title}: sentencePairs[{pair_index}]の空所が訳と対応しない")
        uncovered = compact(corpus)
        for frame in EMAIL_FRAME if passage.get("format") == "email" else []:
            check(compact(frame) in uncovered, f"{title}: メールの挨拶/結び「{frame}」がない")
            uncovered = uncovered.replace(compact(frame), "", 1)
        check(uncovered == compact(" ".join(pair[0] for pair in passage.get("sentencePairs", []))), f"{title}: sentencePairsが本文を順に過不足なく覆っていない")
    story = sections[2]["passages"][0]
    check("( 21 )" in story["paragraphs"][0] and "( 22 )" in story["paragraphs"][1], "大問3: 空所(21)(22)の位置")
    email = next((p for p in passages if p.get("title") == "Helpful employee"), {})
    check(email.get("format") == "email" and email.get("meta") == EMAIL_META, "メールformat/metaが原本と一致しない")

    # English corpus with the official answers filled in.
    part12 = [filled(q["text"], q) for q in questions if q["number"] <= 20]
    part3_filled = [filled(filled(p, story["questions"][0]), story["questions"][1]) for p in story["paragraphs"]]
    passage_units = [pair[0] for p in passages for pair in p["sentencePairs"]]
    filled_units = [filled(filled(unit, story["questions"][0]), story["questions"][1]) for unit in passage_units]
    corpus = " ".join(
        part12 + part3_filled + [p for passage in passages[1:] for p in passage["paragraphs"]]
        + [p["title"] for p in passages]
        + [q.get("question") or "" for q in questions]
        + [c for q in questions for c in q["choices"]]
    )

    # Vocabulary.
    vocabulary = data.get("vocabulary", [])
    check(len(vocabulary) == 40 and len({item.get("word") for item in vocabulary}) == 40, "語彙が40件一意ではない")
    audio_refs = set()
    for item in vocabulary:
        word = item.get("word", "?")
        for key in ("word", "meaning", "pos", "level", "example", "distractors", "wordAudio"):
            check(bool(item.get(key)), f"語彙 {word}: {key}欠落")
        distractors = item.get("distractors", [])
        check(len(distractors) == 3 and len(set(distractors)) == 3 and item.get("meaning") not in distractors, f"語彙 {word}: distractorsが不正")
        check(item.get("level") == "準2級", f"語彙 {word}: level")
        check(not item.get("exampleAudio"), f"語彙 {word}: 同年度外のexampleAudioあり")
        check(VOCAB_SOURCE_FORMS.get(word, word).lower() in corpus.lower(), f"語彙 {word}: 本試験に出てこない")
        check(compact(item.get("example", "")).lower() not in compact(corpus).lower(), f"語彙 {word}: 例文が本試験の文のコピー")
        audio_refs.add(item.get("wordAudio", ""))

    # Focus points.
    focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
    check([f.get("id") for f in focus_points] == FOCUS_IDS, "Focus Pointがfp1〜fp5ではない")
    # 2024年度の準2級と同じ5色（凡例で区別できること）と、fp5のパラフレーズ固定。
    check([f.get("highlightColor") for f in focus_points] == FOCUS_COLORS, "highlightColorが2024年度形式の5色ではない")
    check(
        bool(focus_points) and focus_points[-1].get("title") == "今回の重要なパラフレーズ" and focus_points[-1].get("highlightLabel") == "パラフレーズ",
        "fp5が「今回の重要なパラフレーズ」ではない",
    )
    reading_sentences = [pair[0] for p in passages for pair in p["sentencePairs"]]
    spans: list[tuple[str, int, int, str]] = []
    all_units = part12 + filled_units
    correct_choices = [q["choices"][q["answer"] - 1].rstrip(".") for q in questions if q["number"] >= 23]
    for focus in focus_points:
        fid = focus.get("id", "?")
        for key in (
            "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
            "examples", "practicePassage", "highlightPatterns", "highlightColor",
            "highlightLabel", "practiceQuestions",
        ):
            check(bool(focus.get(key)), f"{fid}: {key}欠落")
        passage = focus.get("practicePassage", {})
        check(bool(passage.get("en")) and bool(passage.get("ja")) and passage.get("audioFile") == f"audio/practice_pp{fid[2:]}.mp3", f"{fid}: practicePassage不完全")
        audio_refs.add(passage.get("audioFile", ""))
        check(len(focus.get("practiceQuestions", [])) == 4 and all(x.get("q") and x.get("a") for x in focus.get("practiceQuestions", [])), f"{fid}: practiceQuestionsが4件ではない")
        examples = focus.get("examples", [])
        check(len(examples) == 3 and all(e.get("en") and e.get("ja") and e.get("note") for e in examples), f"{fid}: examplesが3件でない")
        for example in examples:
            check(compact(example.get("en", "")) in compact(corpus), f"{fid}: 例文が本文にない: {example.get('en', '')[:40]}")
        remaining = compact(re.sub(r"\[出典:.*?\]\n?", "", passage.get("en", "")))
        check(passage.get("en", "").startswith("[出典: "), f"{fid}: practicePassageの出典行")
        for unit in sorted(all_units, key=len, reverse=True):
            remaining = remaining.replace(compact(unit), "")
        check(not remaining, f"{fid}: practicePassageが原文の文そのものでできていない: {remaining[:40]}")
        for pattern in focus.get("highlightPatterns", []):
            # The app marks each pattern inside a single sentence span of Parts 3-4.
            check(any(pattern.lower() in sentence.lower() for sentence in reading_sentences), f"{fid}: highlightPattern「{pattern}」が大問3・4の一文に収まらない")
            text = " ".join(reading_sentences).lower()
            spans += [(fid, m.start(), m.end(), pattern) for m in re.finditer(re.escape(pattern.lower()), text)]
        if fid != "fp5":
            for part in focus.get("sourceQuote", "").split(" / "):
                check(compact(part) in compact(corpus), f"{fid}: sourceQuote「{part}」が本文にない")
        else:
            lines = focus.get("sourceQuote", "").splitlines()
            check(len(lines) >= 5, "fp5: パラフレーズの例が5件未満")
            for line in lines:
                match = re.match(r"^[①-⑩](.+?) → (.+?)（", line)
                check(bool(match), f"fp5: sourceQuoteの行形式: {line[:30]}")
                if match:
                    check(compact(match.group(1)) in compact(corpus), f"fp5: 本文側「{match.group(1)[:30]}」が本文にない")
                    check(match.group(2).rstrip(".") in correct_choices, f"fp5: 言い換え側「{match.group(2)[:30]}」が正解の選択肢ではない")
    for a in spans:
        for b in spans:
            if a[0] < b[0] and a[1] < b[2] and b[1] < a[2]:
                errors.append(f"highlightが重なる: {a[0]}「{a[3]}」/ {b[0]}「{b[3]}」")

    # Audio coverage.
    audio_files = {path.relative_to(BASE).as_posix() for path in (BASE / "audio").rglob("*.mp3")} if (BASE / "audio").is_dir() else set()
    check(len(audio_refs) == AUDIO_COUNT, f"音声参照 {len(audio_refs)} != {AUDIO_COUNT}")
    if args.require_audio or audio_files:
        check(audio_refs == audio_files, f"音声参照/実体不一致: refs={len(audio_refs)} files={len(audio_files)}（_gen_tts.pyを実行）")
        for audio_ref in sorted(audio_refs):
            audio_path = BASE / audio_ref
            if not audio_path.is_file() or audio_path.stat().st_size < MIN_AUDIO_BYTES:
                errors.append(f"音声欠落または短すぎる（{MIN_AUDIO_BYTES}バイト未満）: {audio_ref}")
            elif audio_path.read_bytes()[:1] not in (b"I", b"\xff"):
                errors.append(f"MP3 signature不正: {audio_ref}")
    else:
        notes.append("音声未生成（_gen_tts.py実行後に --require-audio）")

    # Catalog order and fixed PDF registration.
    top_text = (ROOT / "top.js").read_text(encoding="utf-8")
    print_text = (ROOT / "print.js").read_text(encoding="utf-8")
    for filename, text in (("top.js", top_text), ("print.js", print_text)):
        start = text.index("id: 'grade-pre2'")
        block = text[start:text.index("id: 'grade3'", start)]
        check(block.count("{ id: '2024-2-sat'") == 1, f"{filename}: grade-pre2 catalog登録が1件ではない")
        if block.count("{ id: '2024-2-sat'") == 1:
            check(
                block.index("{ id: '2024-2',") < block.index("{ id: '2024-2-sat'") < block.index("{ id: '2024-3',"),
                f"{filename}: 2024-2-satの並び順不正",
            )
    fixed_key = "'grade-pre2/2024-2-sat': {"
    if fixed_key in print_text:
        entry = print_text[print_text.index(fixed_key):][:600]
        entry = entry[:entry.index("}") + 1]
        check(print_text.count(fixed_key) == 1, "print.js: 固定PDF登録が重複")
        check(PDF_NAME in entry and f"pages: {PRACTICE_PAGES}" in entry, "print.js: 固定PDF登録不正")
    else:
        notes.append(f"print.js FIXED_EXAM_PDFS に 'grade-pre2/2024-2-sat'（{PRACTICE_PAGES}ページ）が未登録")
    guides_path = ROOT / "output" / "pdf" / "grammar_guides.json"
    guides = json.loads(guides_path.read_text(encoding="utf-8")) if guides_path.is_file() else {}
    if "grade-pre2/2024-2-sat" in guides:
        check(guides["grade-pre2/2024-2-sat"].get("downloadName") == GUIDE_NAME, "grammar_guides.json: downloadName不正")
    else:
        notes.append("output/pdf/grammar_guides.json に grade-pre2/2024-2-sat が未登録")

    # Fixed practice PDF and grammar guide PDF.
    pdf = ROOT / "output" / "pdf" / PDF_NAME
    check(pdf.is_file(), f"固定PDF欠落（scripts/build_fixed_exam_pdf.py --grade grade-pre2 --exam 2024-2-sat --output output/pdf/{PDF_NAME}）")
    if pdf.is_file():
        reader = PdfReader(pdf)
        check(len(reader.pages) == PRACTICE_PAGES, f"固定PDF pages={len(reader.pages)} != {PRACTICE_PAGES}")
        for page_number, page in enumerate(reader.pages, start=1):
            width, height = float(page.mediabox.width), float(page.mediabox.height)
            check(abs(width - 595.28) <= 1 and abs(height - 841.89) <= 1, f"固定PDF page {page_number}: A4ではない ({width}, {height})")
        printed = compact(" ".join(page.extract_text() for page in reader.pages))
        check("2024年度第2回（土曜準会場）" in printed, "固定PDF: 回の表示")
        for q in questions:
            stem = q.get("text") if q["number"] <= 20 else q.get("question")
            if stem:
                check(compact(stem) in printed, f"固定PDF: Q{q['number']}の問題文")
            for choice in q["choices"]:
                check(compact(choice) in printed, f"固定PDF: Q{q['number']}の選択肢「{choice}」")
        for passage in passages:
            body = passage["paragraphs"] if passage.get("format") != "email" else [pair[0] for pair in passage["sentencePairs"]]
            check(all(compact(part) in printed for part in body), f"固定PDF: {passage['title']}の本文")
        key_text = reader.pages[-1].extract_text()
        printed_key = {int(n): int(a) for n, a in re.findall(r"Q(\d\d)\s+([1-4])\s", key_text)}
        check(printed_key == dict(enumerate(OFFICIAL_ANSWERS, start=1)), "固定PDF: 正解一覧が公式解答と一致しない")
    guide = ROOT / "output" / "pdf" / GUIDE_NAME
    check(guide.is_file() and len(PdfReader(guide).pages) == len(focus_points), "文法解説PDF（1ページ1ポイント）が欠落またはページ数不一致")

    print(
        f"questions={len(questions)} passages={len(passages)} "
        f"sentencePairs={sum(len(p['sentencePairs']) for p in passages)} vocab={len(vocabulary)} "
        f"focus={len(focus_points)} audio={len(audio_files)}/{AUDIO_COUNT} pdf_pages={PRACTICE_PAGES} errors={len(errors)}"
    )
    for note in notes:
        print(f"  [INFO] {note}")
    for error in errors:
        print(f"  [ERROR] {error}")
    if errors:
        raise SystemExit(1)
    print("AUDIT OK: 2024-2-sat 準2級")


if __name__ == "__main__":
    main()
