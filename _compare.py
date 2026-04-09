"""Check reference 2021-1 question structure for translation and PQ format"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

# Check 2021-1 reference
ref = json.load(open(r'data\grade5\2021-1\data.json', 'r', encoding='utf-8'))

# Question fields
q1 = ref['sections'][0]['questions'][0]
print("=== Q1 keys ===")
print(sorted(q1.keys()))
print(f"\ntranslation: {q1.get('translation', 'NOT FOUND')}")

# PQ format  
fp1 = ref['lessonPlan']['focusPoints'][0]
pq = fp1.get('practiceQuestions', [])
pqs = fp1.get('practiceQuestionsSimple', [])
print(f"\n=== PQ format ===")
for p in pq[:2]:
    print(json.dumps(p, ensure_ascii=False))
print(f"\n=== PQS format ===")
for p in pqs[:2]:
    print(json.dumps(p, ensure_ascii=False))

# Check 2022-2 current
cur = json.load(open(r'data\grade5\2022-2\data.json', 'r', encoding='utf-8'))
cq1 = cur['sections'][0]['questions'][0]
print(f"\n=== 2022-2 Q1 keys ===")
print(sorted(cq1.keys()))
print(f"translation: {cq1.get('translation', 'NOT FOUND')}")
