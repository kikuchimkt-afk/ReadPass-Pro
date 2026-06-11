# -*- coding: utf-8 -*-
"""2026年第1回 準2級（本会場）PDF → PNG変換"""
import os
import sys

import fitz

sys.stdout.reconfigure(encoding="utf-8")

base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_dir = os.path.join(base_dir, "2026-1(本会場）")

exam_pdf = os.path.join(pdf_dir, "準2級.pdf")
answer_pdf = os.path.join(pdf_dir, "準2級解答.pdf")

output_dir = os.path.join(base_dir, "pages_pre2_2026-1")
answer_dir = os.path.join(base_dir, "answer_pages_pre2_2026-1")
os.makedirs(output_dir, exist_ok=True)
os.makedirs(answer_dir, exist_ok=True)

mat = fitz.Matrix(300 / 72, 300 / 72)

doc = fitz.open(exam_pdf)
print(f"問題PDF ({os.path.basename(exam_pdf)}) - Total pages: {doc.page_count}")
for i in range(doc.page_count):
    pix = doc[i].get_pixmap(matrix=mat)
    out_path = os.path.join(output_dir, f"page_{i + 1:02d}.png")
    pix.save(out_path)
    print(f"Page {i + 1}: {pix.width}x{pix.height}")
doc.close()

doc2 = fitz.open(answer_pdf)
print(f"\n解答PDF ({os.path.basename(answer_pdf)}) - Total pages: {doc2.page_count}")
for i in range(doc2.page_count):
    pix = doc2[i].get_pixmap(matrix=mat)
    out_path = os.path.join(answer_dir, f"answer_{i + 1:02d}.png")
    pix.save(out_path)
    print(f"Answer Page {i + 1}: {pix.width}x{pix.height}")
doc2.close()

print(f"\nSaved: {output_dir}")
print(f"Saved: {answer_dir}")
