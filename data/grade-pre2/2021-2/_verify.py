"""Verify 2021-2 data.json against official answer key"""
import json
data = json.load(open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2021-2\data.json","r",encoding="utf-8"))
answers = {1:2,2:4,3:4,4:2,5:3,6:2,7:3,8:1,9:3,10:4,
           11:1,12:2,13:1,14:4,15:1,16:3,17:1,18:4,19:2,20:1,
           21:2,22:2,23:3,24:3,25:2,
           26:2,27:1,28:4,29:4,30:4,
           31:1,32:3,33:2,34:3,35:2,36:1,37:3}
errors = []
all_q = []
for sec in data["sections"]:
    if sec.get("questions"):
        all_q.extend(sec["questions"])
    if sec.get("passages"):
        for p in sec["passages"]:
            if p.get("questions"):
                all_q.extend(p["questions"])
for q in all_q:
    n = q["number"]
    expected = answers.get(n)
    actual = q.get("answer")
    if actual != expected:
        errors.append(f"  Q{n}: expected={expected}, got={actual}")
print(f"Total questions: {len(all_q)}")
print(f"Expected: {len(answers)}")
if errors:
    print("ERRORS:")
    for e in errors: print(e)
else:
    print("ALL CORRECT ✅")
print(f"Vocabulary: {len(data.get('vocabulary',[]))} words")
print(f"FocusPoints: {len(data.get('lessonPlan',{}).get('focusPoints',[]))}")
# Check sections
for i,s in enumerate(data["sections"]):
    qc = len(s.get("questions",[]))
    pc = sum(len(p.get("questions",[])) for p in s.get("passages",[]))
    print(f"  sec[{i}] {s['name']} ({s['type']}): {qc+pc} questions")
