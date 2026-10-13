# -*- coding: utf-8 -*-
"""Verify the fixed practice PDF for Grade Pre-1 2026-2 and its print-page registration.

The PDF is checked by content rather than by hash so that it can be rebuilt
with scripts/build_fixed_exam_pdf.py on Windows (with the original fonts).
"""

import os
import re
import sys

from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
RELATIVE_PDF = "output/pdf/ReadPass_EIKEN_GradePre1_2026-2_Practice_Exam_Large_Type_v1.pdf"
PDF_PATH = os.path.join(BASE, *RELATIVE_PDF.split("/"))
EXPECTED_PRINT_PATH = f"{RELATIVE_PDF}?v=20261013-eiken-pre1-2026-2-v1"
OFFICIAL_ANSWERS = [
    1, 4, 4, 3, 3, 4, 2, 1, 1, 4, 4, 1, 4, 2, 1, 1, 4, 1,
    2, 1, 4, 3, 2, 4,
    3, 1, 4, 4, 2, 1, 2,
]

errors = []
if not os.path.isfile(PDF_PATH):
    raise SystemExit(f"fixed PDF is missing: {PDF_PATH}")

reader = PdfReader(PDF_PATH)
if len(reader.pages) != 11:
    errors.append(f"pages={len(reader.pages)} != 11")
for index, page in enumerate(reader.pages, 1):
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    if abs(width - 595.276) > 0.5 or abs(height - 841.89) > 0.5:
        errors.append(f"page {index}: not A4 ({width} x {height})")

text = "\n".join(page.extract_text() or "" for page in reader.pages)
for required in (
    "英検準1級",
    "2026年度 第2回",
    "The Y2K Bug",
    "Searching for a Sixth Taste",
    "Employment Requirements for Welfare",
    "Saint Helena",
    "Q31",
    "正解一覧",
):
    if required not in text:
        errors.append(f"required PDF text is missing: {required!r}")

answer_page = reader.pages[-1].extract_text() or ""
for number, answer in enumerate(OFFICIAL_ANSWERS, 1):
    if not re.search(rf"Q{number:02d}\s*{answer}\b", answer_page):
        errors.append(f"answer list: Q{number:02d} should be {answer}")

with open(os.path.join(BASE, "print.js"), encoding="utf-8") as handle:
    print_js = handle.read()
if print_js.count("'pre-grade1/2026-2': {") != 1:
    errors.append("print.js fixed-map entry missing or duplicated")
if EXPECTED_PRINT_PATH not in print_js:
    errors.append("print.js fixed PDF path/version mismatch")
if "{ id: '2026-2', label: '2026年度 第2回' }" not in print_js:
    errors.append("print.js Pre-1 catalog entry missing")

with open(os.path.join(BASE, "print.html"), encoding="utf-8") as handle:
    print_html = handle.read()
# Later releases bump the version again; it only must not predate this exam.
cache = re.search(r"print\.js\?v=(\d{8})-", print_html)
if not cache or cache.group(1) < "20261013":
    errors.append("print.html cache-busting version mismatch")

if errors:
    print(f"ERRORS={len(errors)}")
    for error in errors:
        print(f"  {error}")
    raise SystemExit(1)

print(f"OK: fixed PDF registered and verified (11 A4 pages, {os.path.getsize(PDF_PATH)} bytes)")
