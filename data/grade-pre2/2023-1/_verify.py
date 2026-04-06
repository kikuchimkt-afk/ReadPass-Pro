import json, os
path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1\data.json"
d = json.load(open(path, "r", encoding="utf-8"))
e = []
ans = {1:1,2:4,3:2,4:4,5:3,6:4,7:4,8:1,9:1,10:2,11:1,12:4,13:2,14:1,15:2,16:3,17:4,18:4,19:1,20:3,21:4,22:1,23:2,24:3,25:2,26:4,27:2,28:1,29:3,30:3,31:1,32:4,33:3,34:2,35:4,36:1,37:4}
tq = 0
for s in d["sections"]:
    qs = list(s.get("questions", []))
    for p in s.get("passages", []):
        qs += list(p.get("questions", []))
    tq += len(qs)
    for q in qs:
        n = q["number"]
        if n in ans and q.get("answer") != ans[n]:
            e.append(f"Q{n}: got {q.get('answer')}, expected {ans[n]}")
types = [s["type"] for s in d["sections"]]
exp = ["vocabulary","vocabulary","passage-fill","reading-comprehension"]
if types != exp: e.append(f"types: {types}")
if tq != 37: e.append(f"total_q={tq}")
v = len(d.get("vocabulary", []))
if v < 40: e.append(f"vocab={v}")
fp = len(d.get("lessonPlan", {}).get("focusPoints", []))
if fp != 5: e.append(f"fp={fp}")
base = os.path.dirname(path)
for i, f in enumerate(d["lessonPlan"]["focusPoints"]):
    af = f.get("practicePassage", {}).get("audioFile", "")
    if af and not os.path.exists(os.path.join(base, af)):
        e.append(f"FP{i+1}: audio missing {af}")
    if not af: e.append(f"FP{i+1}: no audioFile")
ma = sum(1 for x in d.get("vocabulary", []) if "wordAudio" not in x)
if ma: e.append(f"{ma} vocab missing wordAudio")
# Check passages have paragraphs/translations/sentencePairs
for s in d["sections"]:
    for p in s.get("passages", []):
        if not p.get("paragraphs"): e.append(f"{s['name']} {p.get('label','')}: no paragraphs")
        if not p.get("translations"): e.append(f"{s['name']} {p.get('label','')}: no translations")
        if not p.get("sentencePairs"): e.append(f"{s['name']} {p.get('label','')}: no sentencePairs")
print(f"questions={tq} vocab={v} fp={fp}")
if e:
    print(f"FAILED ({len(e)}):")
    for x in e: print(f"  - {x}")
else:
    print("ALL CHECKS PASSED")
