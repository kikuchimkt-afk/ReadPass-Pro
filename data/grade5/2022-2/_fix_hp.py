"""Fix fp1 highlightPatterns"""
import json, os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
d = json.load(open(path, 'r', encoding='utf-8'))
fp1 = d['lessonPlan']['focusPoints'][0]
old = fp1['highlightPatterns']
fp1['highlightPatterns'] = ['I like', 'My favorite']
with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
print(f"Fixed: {old} -> {fp1['highlightPatterns']}")
