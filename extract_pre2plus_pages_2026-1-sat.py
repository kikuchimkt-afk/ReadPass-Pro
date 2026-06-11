"""
2026年第1回 準2級プラス（土曜準会場）PDF → PNG変換スクリプト
各ページを300dpiのPNG画像として出力する
"""
import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"C:\Users\user\Documents\GitHub\ReadPass-Pro"

# 問題PDF
pdf_path = os.path.join(base_dir, "2026-1-sat_準2級プラス.pdf")
output_dir = os.path.join(base_dir, "pages_pre2plus_2026-1-sat")
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"問題PDF - Total pages: {doc.page_count}")

for i in range(doc.page_count):
    page = doc[i]
    # 300 DPI for high-quality OCR
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
    pix.save(out_path)
    print(f"Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc.close()
print(f"\nAll pages saved to: {output_dir}")

# 解答PDF
answer_pdf = os.path.join(base_dir, "2026-1-sat_準2級プラス_解答.pdf")
answer_dir = os.path.join(base_dir, "answer_pages_pre2plus_2026-1-sat")
os.makedirs(answer_dir, exist_ok=True)

doc2 = fitz.open(answer_pdf)
print(f"\n解答PDF - Total pages: {doc2.page_count}")

for i in range(doc2.page_count):
    page = doc2[i]
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(answer_dir, f"answer_{i+1:02d}.png")
    pix.save(out_path)
    print(f"Answer Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc2.close()
print(f"\nAnswer pages saved to: {answer_dir}")
