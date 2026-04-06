"""Fix highlight pattern for fp3"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-3"
data = json.load(open(os.path.join(base, "data.json"), "r", encoding="utf-8"))
all_text = []
for s in data["sections"]:
    for q in s.get("questions",[]): all_text.append(q.get("text",""))
    for p in s.get("passages",[]):
        for para in p.get("paragraphs",[]): all_text.append(para)
full = "\n".join(all_text)

fp3 = data["lessonPlan"]["focusPoints"][2]
new_patterns = []
for pat in fp3["highlightPatterns"]:
    if pat in full:
        new_patterns.append(pat)
    else:
        print(f"  Removing: {pat}")
# Replace with matching pattern from passages
replacements = [
    "The ducks spend all day walking around the plants and eating the pests",
    "they do not want any chemicals to get in their wine"
]
for r in replacements:
    if r in full and r not in new_patterns:
        new_patterns.append(r)
fp3["highlightPatterns"] = new_patterns

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# Verify
for fp in data["lessonPlan"]["focusPoints"]:
    for pat in fp["highlightPatterns"]:
        if pat not in full: print(f"  STILL MISSING {fp['id']}: {pat[:50]}")
print(f"✅ Fixed. fp3 now has {len(fp3['highlightPatterns'])} patterns")
