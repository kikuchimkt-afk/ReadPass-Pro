import fitz, sys, os
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"D:\Files\英検過去問\準2級\準2級2023-2\2023-2-1ji-p2kyu.pdf"
output_dir = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\extracted"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
print(f"\nTotal pages: {len(doc)}")
print(f"Output: {output_dir}")
