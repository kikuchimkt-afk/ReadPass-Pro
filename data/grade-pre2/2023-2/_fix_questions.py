"""Fix missing 'question' field for 大問4 questions"""
import json

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))

sec4 = d["sections"][3]

# 大問4A questions
questions_4a = {
    31: "What is one thing that Grandpa says to Peter?",
    32: "Grandpa asks Peter",
    33: "What did Peter start doing recently?"
}

# 大問4B questions
questions_4b = {
    34: "What is one thing that we learn about Richard Hollingshead's mother?",
    35: "One reason that drive-in movie theaters became popular was",
    36: "Some movies were not shown in drive-in movie theaters because",
    37: "Why did many drive-in movie theater owners sell their theaters?"
}

for p in sec4["passages"]:
    qs_map = questions_4a if p["label"] == "A" else questions_4b
    for q in p["questions"]:
        if q["number"] in qs_map:
            q["question"] = qs_map[q["number"]]
            print(f"  Q{q['number']}: set question = '{qs_map[q['number']]}'")

# Also fix 大問3 - check if questions have question field (passage-fill doesn't need it,
# but let's verify the data is consistent)
sec3 = d["sections"][2]
for p in sec3.get("passages", []):
    for q in p.get("questions", []):
        has_q = "question" in q
        print(f"  大問3 Q{q['number']}: has question = {has_q}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print("✅ Fixed missing question fields")
