import json
data = json.load(open(r"g:\マイドライブ\ReadPass Pro\data\grade5\2021-2\data.json","r",encoding="utf-8"))
answers = {1:4,2:3,3:1,4:3,5:2,6:2,7:3,8:3,9:2,10:2,11:4,12:2,13:1,14:1,15:4,
           16:3,17:1,18:4,19:2,20:1,
           21:3,22:3,23:2,24:1,25:4}
errors = []
all_q = []
for sec in data["sections"]:
    all_q.extend(sec.get("questions",[]))
for q in all_q:
    n = q["number"]
    if q.get("answer") != answers.get(n):
        errors.append(f"  Q{n}: expected={answers.get(n)}, got={q.get('answer')}")
print(f"Total: {len(all_q)} questions")
if errors:
    print("ERRORS:"); [print(e) for e in errors]
else:
    print("ALL CORRECT ✅")

# Check vocabulary distractors are all Japanese
for v in data.get("vocabulary",[]):
    for d in v.get("distractors",[]):
        if all(ord(c) < 128 for c in d.replace(" ","")):
            print(f"  ⚠ ENGLISH distractor: {v['word']} -> {d}")

# Check sentence-order answerSlots
for s in data["sections"]:
    if s["type"] == "sentence-order":
        for q in s["questions"]:
            if q.get("answerSlots") != [1,3]:
                print(f"  ⚠ Q{q['number']}: answerSlots={q.get('answerSlots')}")
            if len(q.get("words",[])) != 4:
                print(f"  ⚠ Q{q['number']}: words count={len(q.get('words',[]))}")

print(f"Vocab: {len(data.get('vocabulary',[]))} | FPs: {len(data.get('lessonPlan',{}).get('focusPoints',[]))}")
print(f"Sections: {len(data['sections'])} (expected 3)")
