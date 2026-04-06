"""Check existing FP topics to avoid duplication"""
import json, os

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2"
for exam in sorted(os.listdir(base)):
    path = os.path.join(base, exam, "data.json")
    if os.path.exists(path):
        d = json.load(open(path, "r", encoding="utf-8"))
        fps = d.get("lessonPlan", {}).get("focusPoints", [])
        print(f"\n{exam}:")
        for fp in fps:
            print(f"  {fp.get('id','?')}: {fp.get('title','?')}")
