"""Fix remaining issues: HL pattern + audioFile"""
import json, os

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json"
d = json.load(open(path, "r", encoding="utf-8"))
fps = d["lessonPlan"]["focusPoints"]

# 1. Fix FP1 highlight pattern: remove non-passage pattern, add valid one
fp1 = fps[0]
fp1["highlightPatterns"] = [
    "people who use social media",
    "a message to tell them that one of their friends has a birthday or wedding anniversary soon",
    "movies that were older or less popular",
    "the children could run around and shout without bothering other people",
    "children could enjoy themselves while they waited for the movies to start"
]

# 2. Add audioFile to all FPs
for i, fp in enumerate(fps):
    fp["practicePassage"]["audioFile"] = f"audio/practice_pp{i+1}.mp3"

# 3. Verify audio files exist
base = os.path.dirname(path)
for i, fp in enumerate(fps):
    af = fp["practicePassage"]["audioFile"]
    full = os.path.join(base, af)
    exists = os.path.exists(full)
    print(f"  FP{i+1}: {af} → {'✓' if exists else '✗ NOT FOUND'}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print("✅ Fixed HL patterns and audioFile paths")
