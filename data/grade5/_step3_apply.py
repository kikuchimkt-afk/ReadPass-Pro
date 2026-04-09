"""
Step 3: 記入済みテンプレートの翻訳を各 data.json にマージする
使い方: python _step3_apply.py
入力: _translations_template.json（翻訳記入済み）
出力: 各 data.json に translation / choiceTranslations フィールドが追加される
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5"
TEMPLATE_PATH = os.path.join(BASE, "_translations_template.json")

if not os.path.exists(TEMPLATE_PATH):
    print(f"❌ Template not found: {TEMPLATE_PATH}")
    sys.exit(1)

template = json.load(open(TEMPLATE_PATH, "r", encoding="utf-8"))
errors = []
applied_count = 0

for exam, questions in template.items():
    data_path = os.path.join(BASE, exam, "data.json")
    if not os.path.exists(data_path):
        errors.append(f"{exam}: data.json not found")
        continue
    
    d = json.load(open(data_path, "r", encoding="utf-8"))
    
    for tq in questions:
        sec_idx = tq["sectionIndex"]
        q_num = tq["number"]
        translation = tq.get("translation", "")
        choice_translations = tq.get("choiceTranslations", [])
        
        # Validate
        if not translation:
            errors.append(f"{exam} Q{q_num}: translation is empty")
            continue
        if not choice_translations or all(ct == "" for ct in choice_translations):
            errors.append(f"{exam} Q{q_num}: choiceTranslations is empty")
            continue
        
        # Find and update the question in data.json
        section = d["sections"][sec_idx]
        target_q = None
        for q in section.get("questions", []):
            if q["number"] == q_num:
                target_q = q
                break
        
        if not target_q:
            errors.append(f"{exam} Q{q_num}: question not found in sections[{sec_idx}]")
            continue
        
        target_q["translation"] = translation
        target_q["choiceTranslations"] = choice_translations
        applied_count += 1
    
    # Save updated data.json
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
    print(f"✅ {exam}: saved")

print(f"\nApplied: {applied_count}")
if errors:
    print(f"\n⚠ Errors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ All translations applied successfully!")
