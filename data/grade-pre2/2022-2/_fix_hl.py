"""Fix highlight patterns that don't match exam text"""
import json, os

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2"
data = json.load(open(os.path.join(base, "data.json"), "r", encoding="utf-8"))

# Build full text
all_text = []
for s in data["sections"]:
    for q in s.get("questions", []):
        all_text.append(q.get("text", ""))
    for p in s.get("passages", []):
        for para in p.get("paragraphs", []):
            all_text.append(para)
full_text = "\n".join(all_text)

# Fix fp2: remove Q14 pattern (has ( 14 ) in text), replace with passage-based pattern
fp2 = data["lessonPlan"]["focusPoints"][1]
new_patterns = []
for pat in fp2["highlightPatterns"]:
    if pat in full_text:
        new_patterns.append(pat)
    else:
        print(f"  FP2 removing: {pat}")
# Add replacement from passages
replacements_fp2 = [
    "After watching it last Saturday, my mom took me to a bookstore",
    "While I was at the bookstore, I saw a poster for an action movie festival",
    "While studying, he worked part-time at a drugstore",
    "After he graduated from college in Canada, he went to study in New York City",
    "When my parents were young, a milkman brought milk to their homes every day",
    "After watching it last Saturday, my mom took me to a bookstore"
]
for r in replacements_fp2:
    if r in full_text and r not in new_patterns:
        new_patterns.append(r)
fp2["highlightPatterns"] = list(dict.fromkeys(new_patterns))  # dedupe preserving order

# Fix fp3: "Barcelona..." and "second-largest" are in Q20 text with ( 20 )
fp3 = data["lessonPlan"]["focusPoints"][2]
new_patterns = []
for pat in fp3["highlightPatterns"]:
    if pat in full_text:
        new_patterns.append(pat)
    else:
        print(f"  FP3 removing: {pat}")
# The Q20 text has ( 20 ) so "Barcelona is the second-largest city" won't match
# Replace with passage-based comparisons
replacements_fp3 = [
    "People are having a bigger and bigger effect on wild animals",
    "there are not as many places for animals like elephants",
    "As cities get bigger and more farms are needed",
    "he had created a lighter, spicier drink"
]
for r in replacements_fp3:
    if r in full_text and r not in new_patterns:
        new_patterns.append(r)
fp3["highlightPatterns"] = list(dict.fromkeys(new_patterns))

# Fix fp5: Q18 and Q2 patterns won't match because of ( 18 ) and ( 2 )
fp5 = data["lessonPlan"]["focusPoints"][4]
new_patterns = []
for pat in fp5["highlightPatterns"]:
    if pat in full_text:
        new_patterns.append(pat)
    else:
        print(f"  FP5 removing: {pat}")
# Add passage-based replacements for pronouns
replacements_fp5 = [
    "Some of them are old action movies from the 1980s and 1990s",
    "Should I get one for you, too",
    "People could use them to buy McLaughlin's drinks"
]
for r in replacements_fp5:
    if r in full_text and r not in new_patterns:
        new_patterns.append(r)
fp5["highlightPatterns"] = list(dict.fromkeys(new_patterns))

# Save
with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Verify all patterns now match
errors = 0
for fp in data["lessonPlan"]["focusPoints"]:
    for pat in fp["highlightPatterns"]:
        if pat not in full_text:
            print(f"  STILL MISSING {fp['id']}: {pat}")
            errors += 1
print(f"\n{'✅ All patterns fixed' if errors == 0 else f'⚠ {errors} still missing'}")
print(f"Pattern counts: {[len(fp['highlightPatterns']) for fp in data['lessonPlan']['focusPoints']]}")
