# -*- coding: utf-8 -*-
"""Cross-session audit for all three EIKEN Grade 2 exams from 2022."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:  # Report the dependency as an audit error in main().
    PdfReader = None


sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent
SESSIONS = ("2022-1", "2022-2", "2022-3")
REGRESSION_SESSIONS = ("2023-1", "2023-2", "2023-3")
EXPECTED_PRINT_CACHE_VERSION = "20260902-grade2-2022-all-v1"
FIXED_PDF_CACHE_VERSIONS = {
    "2022-1": "20260901-eiken-grade2-2022-1-v1",
    "2022-2": "20260902-eiken-grade2-2022-2-v1",
    "2022-3": "20260902-eiken-grade2-2022-3-v1",
    "2023-1": "20260828-eiken-grade2-2023-v1",
    "2023-2": "20260828-eiken-grade2-2023-v1",
    "2023-3": "20260828-eiken-grade2-2023-v1",
}
EXPECTED_TOP_KEYS = [
    "grade",
    "year",
    "session",
    "title",
    "exam",
    "sections",
    "listening",
    "vocabulary",
    "lessonPlan",
]
EXPECTED_SECTION_META = [
    ("大問1", "Part 1", "vocabulary"),
    ("大問2", "Part 2", "passage-fill"),
    ("大問3", "Part 3", "reading-comprehension"),
]
EXPECTED_QUESTION_SIGNATURE = [20, 3, 3, 3, 4, 5]
A4_WIDTH = 595.276
A4_HEIGHT = 841.89
A4_TOLERANCE = 0.5


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_command(args: list[str], *, cwd: Path = REPO) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONUTF8"] = "1"
    return subprocess.run(
        args,
        cwd=cwd,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def command_failure(label: str, result: subprocess.CompletedProcess[str]) -> str:
    details = (result.stdout + "\n" + result.stderr).strip()
    return f"[{label}] exit={result.returncode}" + (f"\n{details}" if details else "")


def extract_grade_exam_ids(text: str, label: str, errors: list[str]) -> list[str]:
    grade_position = text.find("id: 'grade2'")
    if grade_position < 0:
        errors.append(f"[{label}] Grade 2 block is missing")
        return []
    exams_position = text.find("exams:", grade_position)
    open_bracket = text.find("[", exams_position)
    close_bracket = text.find("]", open_bracket)
    if exams_position < 0 or open_bracket < 0 or close_bracket < 0:
        errors.append(f"[{label}] Grade 2 exams array could not be parsed")
        return []
    body = text[open_bracket + 1 : close_bracket]
    ids = re.findall(r"\bid:\s*'([^']+)'", body)

    for index, session in enumerate(SESSIONS, 1):
        expected_entry = (
            rf"\{{\s*id:\s*'{re.escape(session)}'\s*,\s*"
            rf"label:\s*'2022年度 第{index}回'"
        )
        if len(re.findall(expected_entry, body)) != 1:
            errors.append(f"[{label}] {session} is not present exactly once in the Grade 2 block")

    positions = [ids.index(session) if ids.count(session) == 1 else -1 for session in SESSIONS]
    if any(position < 0 for position in positions):
        return ids
    if positions != list(range(positions[0], positions[0] + len(SESSIONS))):
        errors.append(f"[{label}] 2022 sessions are not consecutive and ordered: {positions}")
    return ids


def check_ui_registration(errors: list[str], passes: list[str]) -> None:
    error_count_before = len(errors)
    top_path = REPO / "top.js"
    print_path = REPO / "print.js"
    print_html_path = REPO / "print.html"
    try:
        top_text = top_path.read_text(encoding="utf-8")
        print_text = print_path.read_text(encoding="utf-8")
        print_html = print_html_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"[registration] failed to read UI files: {exc}")
        return

    top_ids = extract_grade_exam_ids(top_text, "top.js", errors)
    catalog_text = print_text.split("const BASE_URL", 1)[0]
    print_ids = extract_grade_exam_ids(catalog_text, "print.js catalog", errors)
    if top_ids and print_ids:
        if top_ids != print_ids:
            errors.append(
                "[catalogs] Grade 2 exam IDs differ between top.js and print.js: "
                f"top={top_ids} print={print_ids}"
            )

    expected_transition = list(SESSIONS + REGRESSION_SESSIONS)
    for label, ids in (("top.js", top_ids), ("print.js catalog", print_ids)):
        if not ids:
            continue
        for session in REGRESSION_SESSIONS:
            if ids.count(session) != 1:
                errors.append(f"[{label}] existing {session} count={ids.count(session)} != 1")
        if any(ids.count(session) != 1 for session in expected_transition):
            continue
        transition_start = ids.index(SESSIONS[0])
        actual_transition = ids[transition_start : transition_start + len(expected_transition)]
        if actual_transition != expected_transition:
            errors.append(
                f"[{label}] 2022 sessions must be immediately before the ordered 2023 sessions: "
                f"got {actual_transition}"
            )

    for session in SESSIONS + REGRESSION_SESSIONS:
        key = f"'grade2/{session}': {{"
        if print_text.count(key) != 1:
            errors.append(f"[print.js fixed map] {session} key count={print_text.count(key)}")
            continue
        start = print_text.index(key)
        end = print_text.find("\n        },", start)
        if end < 0:
            errors.append(f"[print.js fixed map] {session} block terminator is missing")
            continue
        block = print_text[start:end]
        year, session_number = session.split("-", 1)
        filename = f"ReadPass_EIKEN_Grade2_{session}_Practice_Exam_Large_Type_v1.pdf"
        cache_version = FIXED_PDF_CACHE_VERSIONS[session]
        expected_properties = {
            "label": f"label: '英検2級 {year}年度 第{session_number}回',",
            "path": f"path: 'output/pdf/{filename}?v={cache_version}',",
            "downloadName": f"downloadName: '{filename}',",
            "pages": "pages: 13",
        }
        block_lines = [line.strip() for line in block.splitlines()]
        for property_name, expected_line in expected_properties.items():
            actual_lines = [
                line for line in block_lines if line.startswith(f"{property_name}:")
            ]
            if actual_lines != [expected_line]:
                errors.append(
                    f"[print.js fixed map] {session} {property_name}={actual_lines!r} "
                    f"!= {[expected_line]!r}"
                )

    cache_versions = re.findall(
        r'<script\s+src="print\.js\?v=([^"]+)"\s*></script>',
        print_html,
    )
    if cache_versions != [EXPECTED_PRINT_CACHE_VERSION]:
        errors.append(
            "[print.html] cache version "
            f"{cache_versions!r} != {[EXPECTED_PRINT_CACHE_VERSION]!r}"
        )
    if len(errors) == error_count_before:
        passes.append("UI catalogs, fixed PDF map, and print cache version")


def collect_questions(data: dict) -> list[dict]:
    questions: list[dict] = []
    for section in data.get("sections", []):
        questions.extend(section.get("questions", []))
        for passage in section.get("passages", []):
            questions.extend(passage.get("questions", []))
    return questions


def check_session_data(session: str, errors: list[str], passes: list[str]) -> None:
    session_number = int(session.rsplit("-", 1)[1])
    base = REPO / "data" / "grade2" / session
    data_path = base / "data.json"
    if not data_path.is_file():
        errors.append(f"[{session} data] missing {data_path}")
        return
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"[{session} data] could not be loaded: {exc}")
        return

    if list(data) != EXPECTED_TOP_KEYS:
        errors.append(f"[{session} data] top-level keys/order={list(data)}")
    expected_metadata = {
        "grade": "2級",
        "year": "2022",
        "session": str(session_number),
        "title": f"2022年度 第{session_number}回 英語資格検定2級 リーディング",
        "exam": session,
    }
    for field, expected in expected_metadata.items():
        if data.get(field) != expected:
            errors.append(f"[{session} metadata] {field}={data.get(field)!r} != {expected!r}")

    sections = data.get("sections", [])
    section_meta = [
        (section.get("name"), section.get("nameEn"), section.get("type"))
        for section in sections
    ]
    if section_meta != EXPECTED_SECTION_META:
        errors.append(f"[{session} sections] metadata/order={section_meta}")

    signature: list[int] = []
    if len(sections) == 3:
        signature.append(len(sections[0].get("questions", [])))
        signature.extend(
            len(passage.get("questions", []))
            for section in sections[1:]
            for passage in section.get("passages", [])
        )
    if signature != EXPECTED_QUESTION_SIGNATURE:
        errors.append(f"[{session} questions] signature={signature}")

    questions = collect_questions(data)
    numbers = [question.get("number") for question in questions]
    if len(questions) != 38 or numbers != list(range(1, 39)):
        errors.append(f"[{session} questions] count/order={len(questions)} / {numbers}")

    passage_count = sum(len(section.get("passages", [])) for section in sections)
    if passage_count != 5:
        errors.append(f"[{session} passages] count={passage_count} != 5")

    vocabulary = data.get("vocabulary", [])
    vocabulary_words = [item.get("word") for item in vocabulary]
    if len(vocabulary) != 65 or len(set(vocabulary_words)) != 65 or None in vocabulary_words:
        errors.append(f"[{session} vocabulary] expected 65 unique words; got {len(vocabulary)}")

    focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
    if len(focus_points) != 5:
        errors.append(f"[{session} focus] count={len(focus_points)} != 5")

    referenced_audio: set[str] = set()
    for item in vocabulary:
        relative = item.get("wordAudio")
        if isinstance(relative, str) and relative:
            referenced_audio.add(relative.replace("\\", "/"))
        else:
            errors.append(f"[{session} audio] vocabulary wordAudio missing for {item.get('word')!r}")
    for point in focus_points:
        relative = point.get("practicePassage", {}).get("audioFile")
        if isinstance(relative, str) and relative:
            referenced_audio.add(relative.replace("\\", "/"))
        else:
            errors.append(f"[{session} audio] practice audio missing for {point.get('id')!r}")
    if len(referenced_audio) != 70:
        errors.append(f"[{session} audio] referenced unique paths={len(referenced_audio)} != 70")

    actual_audio = {
        path.relative_to(base).as_posix()
        for path in (base / "audio").rglob("*.mp3")
    } if (base / "audio").is_dir() else set()
    if actual_audio != referenced_audio:
        missing = sorted(referenced_audio - actual_audio)
        extra = sorted(actual_audio - referenced_audio)
        errors.append(f"[{session} audio] path mismatch missing={missing} extra={extra}")

    manifest_path = base / "audio" / "tts_manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"[{session} audio] manifest could not be loaded: {exc}")
        manifest = {}
    if not isinstance(manifest, dict) or set(manifest) != referenced_audio:
        manifest_keys = set(manifest) if isinstance(manifest, dict) else set()
        errors.append(
            f"[{session} audio] manifest key count={len(manifest_keys)} "
            f"does not match referenced count={len(referenced_audio)}"
        )

    if not any(error.startswith(f"[{session} ") for error in errors):
        passes.append(f"{session} metadata/data: 38 questions, 5 passages, 65 vocab, 5 focus, 70 audio")


def check_fixed_pdf(session: str, errors: list[str], passes: list[str]) -> None:
    if PdfReader is None:
        errors.append("[PDF] pypdf is not installed")
        return
    pdf_path = (
        REPO
        / "output"
        / "pdf"
        / f"ReadPass_EIKEN_Grade2_{session}_Practice_Exam_Large_Type_v1.pdf"
    )
    if not pdf_path.is_file():
        errors.append(f"[{session} PDF] missing {pdf_path}")
        return
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        errors.append(f"[{session} PDF] could not be opened: {exc}")
        return
    if len(reader.pages) != 13:
        errors.append(f"[{session} PDF] pages={len(reader.pages)} != 13")
    for page_number, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - A4_WIDTH) > A4_TOLERANCE or abs(height - A4_HEIGHT) > A4_TOLERANCE:
            errors.append(
                f"[{session} PDF] page {page_number} not A4: {width:.3f} x {height:.3f}"
            )
    if not any(error.startswith(f"[{session} PDF]") for error in errors):
        passes.append(f"{session} fixed PDF: 13 A4 pages, sha256={sha256(pdf_path)}")


def check_generator_reproducibility(session: str, errors: list[str], passes: list[str]) -> None:
    generator = REPO / f"gen_g2_{session}.py"
    current_data = REPO / "data" / "grade2" / session / "data.json"
    if not generator.is_file():
        errors.append(f"[{session} generator] missing {generator}")
        return
    if not current_data.is_file():
        errors.append(f"[{session} generator] current data is missing")
        return

    source_before = sha256(current_data)
    generated_hashes: list[str] = []
    with tempfile.TemporaryDirectory(prefix=f"readpass-g2-{session}-generator-") as temporary:
        temporary_root = Path(temporary)
        temporary_generator = temporary_root / generator.name
        shutil.copy2(generator, temporary_generator)
        generated_data = temporary_root / "data" / "grade2" / session / "data.json"
        for run_number in (1, 2):
            result = run_command([sys.executable, temporary_generator.name], cwd=temporary_root)
            if result.returncode != 0:
                errors.append(command_failure(f"{session} generator run {run_number}", result))
                return
            if not generated_data.is_file():
                errors.append(f"[{session} generator run {run_number}] data.json was not created")
                return
            generated_hashes.append(sha256(generated_data))

    source_after = sha256(current_data)
    if source_after != source_before:
        errors.append(f"[{session} generator] shared data.json changed during isolated audit")
    if generated_hashes != [source_before, source_before]:
        errors.append(
            f"[{session} generator] SHA mismatch current={source_before} generated={generated_hashes}"
        )
    else:
        passes.append(f"{session} generator: two isolated runs match data.json sha256={source_before}")


def check_dedicated_audits(errors: list[str], passes: list[str]) -> None:
    candidates = [sys.executable]
    path_python = shutil.which("python")
    if path_python and Path(path_python).resolve() != Path(sys.executable).resolve():
        candidates.append(path_python)
    audit_python = None
    for candidate in candidates:
        dependency_check = run_command(
            [candidate, "-c", "import pypdf, soundfile"],
        )
        if dependency_check.returncode == 0:
            audit_python = candidate
            break
    if audit_python is None:
        errors.append(
            "[dedicated audits] no Python interpreter with pypdf and soundfile was found"
        )
        return

    for session in SESSIONS:
        audit_path = REPO / f"audit_g2_{session}.py"
        if not audit_path.is_file():
            errors.append(f"[{session} dedicated audit] missing {audit_path}")
            continue
        result = run_command([audit_python, audit_path.name])
        if result.returncode != 0:
            errors.append(command_failure(f"{session} dedicated audit", result))
        else:
            summary = next(
                (line.strip() for line in result.stdout.splitlines() if line.strip().startswith("PASS")),
                "passed",
            )
            passes.append(f"{session} dedicated audit: {summary}")


def check_javascript(errors: list[str], passes: list[str]) -> None:
    for filename in ("top.js", "print.js", "app.js"):
        result = run_command(["node", "--check", filename])
        if result.returncode != 0:
            errors.append(command_failure(f"node --check {filename}", result))
        else:
            passes.append(f"node --check {filename}")


def check_python_compile(errors: list[str], passes: list[str]) -> None:
    error_count_before = len(errors)
    paths = [
        Path(__file__).resolve(),
        REPO / "scripts" / "build_fixed_exam_pdf.py",
    ]
    for session in SESSIONS:
        paths.extend(
            [
                REPO / f"gen_g2_{session}.py",
                REPO / f"audit_g2_{session}.py",
                REPO / "data" / "grade2" / session / "_gen_tts.py",
            ]
        )
    for path in paths:
        if not path.is_file():
            errors.append(f"[Python compile] missing {path}")
            continue
        try:
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
        except (OSError, SyntaxError) as exc:
            errors.append(f"[Python compile] {path}: {exc}")
    if len(errors) == error_count_before:
        passes.append(f"Python compile: {len(paths)} files")


def check_git_diff(errors: list[str], passes: list[str]) -> None:
    result = run_command(["git", "diff", "--check"])
    if result.returncode != 0:
        errors.append(command_failure("git diff --check", result))
    else:
        passes.append("git diff --check")


def main() -> int:
    errors: list[str] = []
    passes: list[str] = []

    check_javascript(errors, passes)
    check_python_compile(errors, passes)
    check_git_diff(errors, passes)
    check_ui_registration(errors, passes)
    for session in SESSIONS:
        check_session_data(session, errors, passes)
        check_fixed_pdf(session, errors, passes)
        check_generator_reproducibility(session, errors, passes)
    check_dedicated_audits(errors, passes)

    print("ReadPass Grade 2 2022 cross-session audit")
    for message in passes:
        print(f"  PASS: {message}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "PASS: all three sessions are registered and reproducible "
        "(38 questions / 5 passages / 65 vocab / 5 focus / 70 audio / 13 A4 pages each)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
