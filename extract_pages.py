"""
2026年第1回2級（準会場）PDF → PNG変換スクリプト
各ページを300dpiのPNG画像として出力する
"""
import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\2級.pdf"
output_dir = r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\pages"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {doc.page_count}")

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

# 解答PDFも同様に処理
answer_pdf = r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\解答\2級_解答.pdf"
answer_dir = r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\answer_pages"
os.makedirs(answer_dir, exist_ok=True)

doc2 = fitz.open(answer_pdf)
print(f"\nAnswer PDF - Total pages: {doc2.page_count}")

for i in range(doc2.page_count):
    page = doc2[i]
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(answer_dir, f"answer_{i+1:02d}.png")
    pix.save(out_path)
    print(f"Answer Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc2.close()
print(f"\nAnswer pages saved to: {answer_dir}")
