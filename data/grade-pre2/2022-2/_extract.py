"""Extract text from Pre-Grade 2 2022-2 PDF"""
import fitz, sys, os
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\makoto\OneDrive\英検過去問など\準2級\準2級2022-2\2022-2-1ji-p2kyu.pdf"
output_dir = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2\extracted"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
page_count = len(doc)
for i in range(page_count):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
print(f"\nDone. {page_count} pages extracted to {output_dir}")
