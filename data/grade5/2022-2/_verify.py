import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r'c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2022-2\data.json', 'r', encoding='utf-8'))
errors = []
answers = {1:3,2:4,3:3,4:2,5:1,6:4,7:1,8:4,9:1,10:1,11:2,12:4,13:1,14:2,15:2,16:2,17:2,18:3,19:4,20:2,21:2,22:2,23:1,24:4,25:4}
if len(d['sections']) != 3:
    errors.append(f"Expected 3 sections, got {len(d['sections'])}")
for s in d['sections']:
    for q in s.get('questions', []):
        n = q['number']
        if n in answers and q['answer'] != answers[n]:
            errors.append(f"Q{n}: expected {answers[n]}, got {q['answer']}")
        for key in ['grammar','grammarSimple','choiceAnalysis','choiceAnalysisSimple']:
            if key not in q:
                errors.append(f"Q{n}: missing {key}")
for s in d['sections']:
    if s['type'] == 'sentence-order':
        for q in s['questions']:
            if q.get('answerSlots') != [1, 3]:
                errors.append(f"Q{q['number']}: answerSlots should be [1,3]")
            if len(q.get('words', [])) != 4:
                errors.append(f"Q{q['number']}: words should have 4 items")
for v in d.get('vocabulary', []):
    for dist in v.get('distractors', []):
        if all(ord(ch) < 128 for ch in dist.replace(' ','')):
            errors.append(f"ENGLISH distractor: {v['word']} -> {dist}")
if errors:
    print("FAILED:")
    for e in errors:
        print(f"  - {e}")
else:
    print("ALL CHECKS PASSED")
    print(f"Sections: {len(d['sections'])}")
    total_q = sum(len(s.get('questions',[])) for s in d['sections'])
    print(f"Total questions: {total_q}")
    print(f"Vocabulary: {len(d.get('vocabulary',[]))}")
    print(f"Focus Points: {len(d.get('lessonPlan',{}).get('focusPoints',[]))}")
