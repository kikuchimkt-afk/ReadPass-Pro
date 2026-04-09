"""Verify data.json structure for grade5 2022-3"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2022-3\data.json", "r", encoding="utf-8"))
errors = []

# Check sections
if len(d['sections']) != 3:
    errors.append(f"Sections: {len(d['sections'])} (expected 3)")

# Check vocab distractors are Japanese
for v in d.get('vocabulary', []):
    for dist in v.get('distractors', []):
        if all(ord(ch) < 128 for ch in dist.replace(' ', '')):
            errors.append(f"EN distractor: {v['word']} -> {dist}")

# Check sentence-order
for s in d['sections']:
    if s['type'] == 'sentence-order':
        for q in s['questions']:
            if q.get('answerSlots') != [1, 3]:
                errors.append(f"Q{q['number']}: answerSlots={q.get('answerSlots')}")
            if len(q.get('words', [])) != 4:
                errors.append(f"Q{q['number']}: words has {len(q.get('words', []))} items (expected 4)")

# Check lesson plan
lp = d.get('lessonPlan', {})
fps = lp.get('focusPoints', [])
print(f"FP count: {len(fps)}")
for fp in fps:
    pp = fp.get('practicePassage', {})
    has_para = bool(pp.get('paragraphs'))
    has_en = bool(pp.get('en'))
    has_audio = bool(pp.get('audioFile'))
    print(f"  {fp['id']}: pp_para={has_para}, pp_en={has_en}, pp_audio={has_audio}, ex={len(fp.get('examples', []))}, pq={len(fp.get('practiceQuestions', []))}")

# Check vocab
print(f"Vocab count: {len(d.get('vocabulary', []))}")
for v in d.get('vocabulary', []):
    if 'wordAudio' not in v:
        errors.append(f"Missing wordAudio: {v['word']}")

# Check question audio refs
for s in d['sections']:
    for q in s['questions']:
        if 'questionAudio' not in q:
            errors.append(f"Q{q['number']}: missing questionAudio")

# Check Q8 answer
q8 = d['sections'][0]['questions'][7]
print(f"\nQ8 answer: {q8['answer']}, text: {q8['text']}")
print(f"Q8 choices: {q8['choices']}")

if errors:
    print("\n⚠ ERRORS:")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n✅ All structure checks OK")
