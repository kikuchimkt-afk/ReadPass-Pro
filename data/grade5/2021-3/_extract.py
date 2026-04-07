import pdfplumber, os
pdf_path = r"D:\Files\英検過去問\5級\5級2021-3\2021-3-1ji-5kyu.pdf"
out = os.path.join(r"g:\マイドライブ\ReadPass Pro\data\grade5\2021-3", "extracted")
os.makedirs(out, exist_ok=True)
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        txt = page.extract_text() or ""
        with open(os.path.join(out, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(txt)
    print(f"Extracted {len(pdf.pages)} pages")
