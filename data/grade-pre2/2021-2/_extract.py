import pdfplumber, os
pdf_path = r"D:\Files\英検過去問\準2級\準2級2021-2\2021-2-1ji-p2kyu.pdf"
out = os.path.join(os.path.dirname(__file__), "extracted")
os.makedirs(out, exist_ok=True)
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        txt = page.extract_text() or ""
        with open(os.path.join(out, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(txt)
    print(f"Extracted {len(pdf.pages)} pages")
