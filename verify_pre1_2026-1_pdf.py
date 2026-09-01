# -*- coding: utf-8 -*-
"""Verify the deterministic fixed PDF and its print-page registration."""

import hashlib
import os
import sys

from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
RELATIVE_PDF = "output/pdf/ReadPass_EIKEN_GradePre1_2026-1_Practice_Exam_Large_Type_v1.pdf"
PDF_PATH = os.path.join(BASE, *RELATIVE_PDF.split("/"))
EXPECTED_SHA256 = "5b5163acc699aa9cf9d9b6cca76ca6087c96f6d55726f25355181e5887c3832a"
EXPECTED_PRINT_PATH = (
    "output/pdf/ReadPass_EIKEN_GradePre1_2026-1_Practice_Exam_Large_Type_v1.pdf"
    "?v=20260901-eiken-pre1-2026-1-v1"
)

errors = []
if not os.path.isfile(PDF_PATH):
    raise SystemExit(f"fixed PDF is missing: {PDF_PATH}")

with open(PDF_PATH, "rb") as handle:
    digest = hashlib.sha256(handle.read()).hexdigest()
if digest != EXPECTED_SHA256:
    errors.append(f"sha256={digest} != {EXPECTED_SHA256}")

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
    "2026年度 第1回",
    "Birth Order",
    "Digital Nations",
    "Uruk",
    "Animal Uplift",
    "Q31",
    "正解一覧",
):
    if required not in text:
        errors.append(f"required PDF text is missing: {required!r}")

with open(os.path.join(BASE, "print.js"), encoding="utf-8") as handle:
    print_js = handle.read()
if print_js.count("'pre-grade1/2026-1': {") != 1:
    errors.append("print.js fixed-map entry missing or duplicated")
if EXPECTED_PRINT_PATH not in print_js:
    errors.append("print.js fixed PDF path/version mismatch")
if "{ id: '2026-1', label: '2026年度 第1回' }" not in print_js:
    errors.append("print.js Pre-1 catalog entry missing")

with open(os.path.join(BASE, "print.html"), encoding="utf-8") as handle:
    print_html = handle.read()
if 'print.js?v=20260901-pre1-2026-1-v1' not in print_html:
    errors.append("print.html cache-busting version mismatch")

if errors:
    print(f"ERRORS={len(errors)}")
    for error in errors:
        print(f"  {error}")
    raise SystemExit(1)

print(
    "OK: fixed PDF registered and verified "
    f"(11 A4 pages, {os.path.getsize(PDF_PATH)} bytes, sha256={digest})"
)
