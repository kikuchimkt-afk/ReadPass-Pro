# -*- coding: utf-8 -*-
"""2026年第1回準2級（土曜準会場）PDF → PNG変換"""
import fitz
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）"
PDF_PATH = os.path.join(BASE, "準2級.pdf")
ANSWER_PDF = os.path.join(BASE, "解答", "準2級_解答.pdf")
OUTPUT_DIR = os.path.join(BASE, "pre2_pages")
ANSWER_DIR = os.path.join(BASE, "pre2_answer_pages")
DPI = 300
MAT = fitz.Matrix(DPI / 72, DPI / 72)


def extract(pdf_path, out_dir, prefix):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    print(f"{pdf_path} — {doc.page_count} pages")
    for i in range(doc.page_count):
        pix = doc[i].get_pixmap(matrix=MAT)
        out_path = os.path.join(out_dir, f"{prefix}_{i+1:02d}.png")
        pix.save(out_path)
        print(f"  {prefix}_{i+1:02d}.png  {pix.width}x{pix.height}")
    doc.close()
    print(f"Saved to: {out_dir}\n")


extract(PDF_PATH, OUTPUT_DIR, "page")
extract(ANSWER_PDF, ANSWER_DIR, "answer")
