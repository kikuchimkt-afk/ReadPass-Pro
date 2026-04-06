"""Verify data.json structure"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

errors = []
total = 0

# Check sections
for s in d["sections"]:
    qs = s.get("questions", [])
    ps = s.get("passages", [])
    count = len(qs)
    for p in ps:
        count += len(p["questions"])
    total += count
    print(f"  {s['name']}: {count} questions")
    
    # Check vocabulary/conversation questions
    for q in qs:
        for f in ["text","translation","choices","choiceTranslations","answer","choiceAnalysis","grammar"]:
            if f not in q:
                errors.append(f"Q{q['number']}: missing {f}")
        if "choices" in q and len(q["choices"]) != 4:
            errors.append(f"Q{q['number']}: has {len(q['choices'])} choices (expected 4)")
        if "choiceTranslations" in q and len(q["choiceTranslations"]) != 4:
            errors.append(f"Q{q['number']}: has {len(q['choiceTranslations'])} choiceTranslations")
        if "choiceAnalysis" in q and len(q["choiceAnalysis"]) != 4:
            errors.append(f"Q{q['number']}: has {len(q['choiceAnalysis'])} choiceAnalysis")
    
    # Check passage questions
    for p in ps:
        if "passage" not in p:
            errors.append(f"Passage {p.get('label','?')}: missing passage")
        if "passageTranslation" not in p:
            errors.append(f"Passage {p.get('label','?')}: missing passageTranslation")
        for q in p["questions"]:
            for f in ["text","translation","choices","choiceTranslations","answer","choiceAnalysis","grammar"]:
                if f not in q:
                    errors.append(f"P{p.get('label','?')}Q{q['number']}: missing {f}")

print(f"\nTotal questions: {total}")
print(f"Vocabulary: {len(d['vocabulary'])} words")

# Check FPs
fps = d.get("lessonPlan", {}).get("focusPoints", [])
print(f"Focus Points: {len(fps)}")
for fp in fps:
    for f in ["practicePassage","practiceQuestions","highlightPatterns","highlightColor","highlightLabel","explanation","sourceQuote","sourceLocation","examples"]:
        if f not in fp:
            errors.append(f"FP {fp['id']}: missing {f}")

if errors:
    print(f"\n❌ {len(errors)} errors found:")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n✅ All checks passed!")

# Check question numbering
nums = []
for s in d["sections"]:
    for q in s.get("questions", []):
        nums.append(q["number"])
    for p in s.get("passages", []):
        for q in p["questions"]:
            nums.append(q["number"])
expected = list(range(1, 38))
if sorted(nums) == expected:
    print("✅ Question numbering: 1-37 correct")
else:
    missing = set(expected) - set(nums)
    extra = set(nums) - set(expected)
    if missing:
        print(f"❌ Missing question numbers: {sorted(missing)}")
    if extra:
        print(f"❌ Extra question numbers: {sorted(extra)}")
