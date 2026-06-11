# -*- coding: utf-8 -*-
"""2026年第1回 準2級プラス（本会場）PDF → PNG変換

注意: 本会場フォルダではファイル名が入れ替わっている。
  - 試験問題24頁 → 準2級プラス解答.pdf
  - 解答1頁     → 準2級プラス.pdf
"""
import os
import sys

import fitz

sys.stdout.reconfigure(encoding="utf-8")

base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_dir = os.path.join(base_dir, "2026-1(本会場）")

# 試験問題（24頁）
exam_pdf = os.path.join(pdf_dir, "準2級プラス解答.pdf")
output_dir = os.path.join(base_dir, "pages_pre2plus_2026-1")
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(exam_pdf)
print(f"問題PDF ({os.path.basename(exam_pdf)}) - Total pages: {doc.page_count}")
for i in range(doc.page_count):
    page = doc[i]
    mat = fitz.Matrix(300 / 72, 300 / 72)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(output_dir, f"page_{i + 1:02d}.png")
    pix.save(out_path)
    print(f"Page {i + 1}: {pix.width}x{pix.height}")
doc.close()

# 解答（1頁）
answer_pdf = os.path.join(pdf_dir, "準2級プラス.pdf")
answer_dir = os.path.join(base_dir, "answer_pages_pre2plus_2026-1")
os.makedirs(answer_dir, exist_ok=True)

doc2 = fitz.open(answer_pdf)
print(f"\n解答PDF ({os.path.basename(answer_pdf)}) - Total pages: {doc2.page_count}")
for i in range(doc2.page_count):
    page = doc2[i]
    mat = fitz.Matrix(300 / 72, 300 / 72)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(answer_dir, f"answer_{i + 1:02d}.png")
    pix.save(out_path)
    print(f"Answer Page {i + 1}: {pix.width}x{pix.height}")
doc2.close()

print(f"\nSaved: {output_dir}")
print(f"Saved: {answer_dir}")
