import json, os
base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base,"data.json"),"r",encoding="utf-8"))
answers = {1:2,2:3,3:4,4:3,5:3,6:4,7:2,8:4,9:2,10:1,11:3,12:2,13:3,14:1,15:3,
           16:1,17:3,18:1,19:4,20:3,
           21:1,22:4,23:2,24:1,25:3}
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
print(f"Vocab: {len(data.get('vocabulary',[]))} | FPs: {len(data.get('lessonPlan',{}).get('focusPoints',[]))}")
