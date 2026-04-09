"""
Step 4: 全 grade5 の翻訳フィールドを最終検証する
使い方: python _step4_verify.py
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5"
EXAMS = ["2021-1", "2021-2", "2021-3", "2022-1", "2022-2", "2022-3"]

total_ok = 0
total_err = 0
errors = []

for exam in EXAMS:
    path = os.path.join(BASE, exam, "data.json")
    if not os.path.exists(path):
        errors.append(f"{exam}: data.json not found")
        continue
    
    d = json.load(open(path, "r", encoding="utf-8"))
    exam_ok = 0
    exam_err = 0
    
    for si, sec in enumerate(d.get("sections", [])):
        sec_type = sec.get("type", "")
        sec_name = sec.get("name", "")
        
        for q in sec.get("questions", []):
            qn = q["number"]
            
            if sec_type == "vocabulary":
                # 大問1・大問2: translation と choiceTranslations が必須
                t = q.get("translation", "")
                ct = q.get("choiceTranslations", [])
                
                if not t:
                    errors.append(f"{exam} {sec_name} Q{qn}: translation MISSING")
                    exam_err += 1
                elif t == "undefined" or t.strip() == "":
                    errors.append(f"{exam} {sec_name} Q{qn}: translation EMPTY/UNDEFINED")
                    exam_err += 1
                else:
                    exam_ok += 1
                
                if not ct or len(ct) != len(q.get("choices", [])):
                    errors.append(f"{exam} {sec_name} Q{qn}: choiceTranslations MISSING or wrong length")
                    exam_err += 1
                elif any(c == "" or c is None for c in ct):
                    errors.append(f"{exam} {sec_name} Q{qn}: choiceTranslations has empty entries")
                    exam_err += 1
            
            elif sec_type == "sentence-order":
                # 大問3: translation不要（元が日本語）
                pass
    
    status = "✅" if exam_err == 0 else "⚠"
    print(f"{status} {exam}: {exam_ok} OK, {exam_err} errors")
    total_ok += exam_ok
    total_err += exam_err

print(f"\n{'='*40}")
print(f"Total: {total_ok} OK, {total_err} errors")

if errors:
    print(f"\n⚠ Errors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n✅ ALL TRANSLATIONS VERIFIED SUCCESSFULLY!")
