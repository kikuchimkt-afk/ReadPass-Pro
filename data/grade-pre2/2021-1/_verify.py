import json
data = json.load(open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-1\data.json","r",encoding="utf-8"))
answers = {1:1,2:4,3:3,4:1,5:2,6:4,7:1,8:1,9:1,10:3,
           11:4,12:2,13:2,14:2,15:4,16:4,17:2,18:4,19:3,20:3,
           21:2,22:1,23:1,24:2,25:1,
           26:4,27:3,28:2,29:2,30:4,
           31:3,32:3,33:4,34:4,35:4,36:3,37:3}
all_q = []
for sec in data["sections"]:
    if sec.get("questions"): all_q.extend(sec["questions"])
    if sec.get("passages"):
        for p in sec["passages"]:
            if p.get("questions"): all_q.extend(p["questions"])
errors = []
for q in all_q:
    n = q["number"]
    if q.get("answer") != answers.get(n):
        errors.append(f"  Q{n}: expected={answers.get(n)}, got={q.get('answer')}")
print(f"Total: {len(all_q)} questions")
if errors:
    print("ERRORS:"); [print(e) for e in errors]
else:
    print("ALL CORRECT ✅")
print(f"Vocab: {len(data.get('vocabulary',[]))} | FPs: {len(data.get('lessonPlan',{}).get('focusPoints',[]))}")
for i,s in enumerate(data["sections"]):
    qc = len(s.get("questions",[])) + sum(len(p.get("questions",[])) for p in s.get("passages",[]))
    print(f"  sec[{i}] {s['name']} ({s['type']}): {qc}q")
