"""
Step 1: 翻訳が必要な問題を全て抽出し、テンプレートJSONを生成する
使い方: python _step1_extract.py
出力: _translations_template.json
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5"
EXAMS = ["2021-1", "2021-2", "2021-3", "2022-1", "2022-2", "2022-3"]

result = {}

for exam in EXAMS:
    path = os.path.join(BASE, exam, "data.json")
    if not os.path.exists(path):
        print(f"SKIP: {path} not found")
        continue
    
    d = json.load(open(path, "r", encoding="utf-8"))
    questions = []
    
    for si, sec in enumerate(d.get("sections", [])):
        # 大問1・大問2 (vocabulary) のみ。大問3 (sentence-order) は日本語なのでスキップ
        if sec.get("type") != "vocabulary":
            continue
        
        for q in sec.get("questions", []):
            questions.append({
                "sectionIndex": si,
                "sectionName": sec.get("name", ""),
                "number": q["number"],
                "text": q["text"],
                "choices": q["choices"],
                "translation": "",           # ← Geminiがここを埋める
                "choiceTranslations": ["", "", "", ""]  # ← Geminiがここを埋める
            })
    
    result[exam] = questions
    print(f"{exam}: {len(questions)} questions extracted")

output_path = os.path.join(BASE, "_translations_template.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n✅ Template saved to: {output_path}")
print(f"Total questions to translate: {sum(len(v) for v in result.values())}")
