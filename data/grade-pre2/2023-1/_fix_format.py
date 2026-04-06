"""Fix 2023-1 data structure to match 2023-2 format:
1. choiceAnalysis: dict → list
2. vocab: add missing 'source' field
3. FP: add missing 'sourceQuote'/'sourceLocation' if needed
"""
import json

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

fixes = 0

# 1. Fix choiceAnalysis from dict to list
for s in d["sections"]:
    qs = list(s.get("questions", []))
    for p in s.get("passages", []):
        qs += list(p.get("questions", []))
    for q in qs:
        ca = q.get("choiceAnalysis")
        if isinstance(ca, dict):
            # Convert {"1":"...", "2":"...", "3":"...", "4":"..."} → ["...", "...", "...", "..."]
            q["choiceAnalysis"] = [ca.get(str(i+1), "") for i in range(len(q["choices"]))]
            fixes += 1
        # Add choiceTranslations if missing (大問1/2 don't have them)
        if "choiceTranslations" not in q:
            q["choiceTranslations"] = ["" for _ in q["choices"]]
            
        # Add questionTranslation if missing
        if "questionTranslation" not in q:
            q["questionTranslation"] = ""

# 2. Fix vocabulary - add source field
for v in d.get("vocabulary", []):
    if "source" not in v:
        v["source"] = "大問1-4"

# 3. Verify FP structure matches
ref_fp_keys = ['examples', 'explanation', 'highlightColor', 'highlightLabel',
               'highlightPatterns', 'id', 'practicePassage', 'practiceQuestions',
               'sourceLocation', 'sourceQuote', 'subtitle', 'title']
for fp in d["lessonPlan"]["focusPoints"]:
    for k in ref_fp_keys:
        if k not in fp:
            print(f"  FP {fp['id']}: missing key '{k}'")

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"✅ Fixed {fixes} choiceAnalysis entries (dict → list)")
print(f"✅ Vocab: {len(d['vocabulary'])} words with 'source' field")
