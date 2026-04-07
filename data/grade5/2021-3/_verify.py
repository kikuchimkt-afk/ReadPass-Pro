import json, os
base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base,"data.json"),"r",encoding="utf-8"))
# From user's answer key image
answers = {1:1,2:2,3:4,4:3,5:4,6:2,7:2,8:3,9:2,10:4,11:3,12:1,13:1,14:4,15:3,
           16:2,17:1,18:4,19:3,20:2,
           21:4,22:2,23:1,24:1,25:3}
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

for v in data.get("vocabulary",[]):
    for d in v.get("distractors",[]):
        if all(ord(c) < 128 for c in d.replace(" ","")):
            print(f"  ⚠ ENGLISH distractor: {v['word']} -> {d}")

for s in data["sections"]:
    if s["type"] == "sentence-order":
        for q in s["questions"]:
            if q.get("answerSlots") != [1,3]:
                print(f"  ⚠ Q{q['number']}: answerSlots={q.get('answerSlots')}")
print(f"Vocab: {len(data.get('vocabulary',[]))} | FPs: {len(data.get('lessonPlan',{}).get('focusPoints',[]))}")
