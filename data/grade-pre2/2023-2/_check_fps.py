"""Fix Q31 undefined issue - check question field"""
import json

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

# Check all questions in section 3 (大問4)
sec4 = d["sections"][3]
for p in sec4.get("passages", []):
    for q in p.get("questions", []):
        qtext = q.get("question", "MISSING")
        qt = q.get("questionTranslation", "MISSING")
        print(f"Q{q['number']}: question='{qtext[:60]}' qt='{qt[:60]}'")
