import json, os

base = r"G:\マイドライブ\ReadPass Pro\data\grade2"
for exam in sorted(os.listdir(base)):
    path = os.path.join(base, exam, "data.json")
    if os.path.exists(path):
        d = json.load(open(path, "r", encoding="utf-8"))
        fps = d.get("lessonPlan", {}).get("focusPoints", [])
        print(f"\n{exam}:")
        for fp in fps:
            print(f"  {fp.get('id','?')}: {fp.get('title','?')}")
