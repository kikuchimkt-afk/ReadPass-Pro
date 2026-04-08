"""Final verification - outputs to file"""
import json, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
d = json.load(open(path, 'r', encoding='utf-8'))
errors = []
lines = []

official = {
    1:3,2:4,3:3,4:2,5:1,6:4,7:1,8:4,9:1,10:1,11:2,12:2,13:4,14:1,15:2,
    16:2,17:2,18:3,19:4,20:2,
    21:2,22:2,23:1,24:4,25:4
}
for s in d['sections']:
    for q in s['questions']:
        n = q['number']
        if n in official and q['answer'] != official[n]:
            errors.append(f"Q{n}: data={q['answer']} vs official={official[n]}")

if len(d['sections']) != 3:
    errors.append(f"Expected 3 sections, got {len(d['sections'])}")

for v in d.get('vocabulary', []):
    for dist in v.get('distractors', []):
        if all(ord(ch) < 128 for ch in dist.replace(' ', '')):
            errors.append(f"ENGLISH distractor: {v['word']} -> {dist}")

for s in d['sections']:
    if s['type'] == 'sentence-order':
        for q in s['questions']:
            if q.get('answerSlots') != [1, 3]:
                errors.append(f"Q{q['number']}: answerSlots={q.get('answerSlots')}")
            if len(q.get('words', [])) != 4:
                errors.append(f"Q{q['number']}: words count={len(q.get('words', []))}")

fps = d.get('lessonPlan', {}).get('focusPoints', [])
for fp in fps:
    pp = fp.get('practicePassage', {})
    if not pp.get('en'):
        errors.append(f"{fp['id']}: MISSING practicePassage.en")
    if not pp.get('ja'):
        errors.append(f"{fp['id']}: MISSING practicePassage.ja")
    if not pp.get('audioFile'):
        errors.append(f"{fp['id']}: MISSING practicePassage.audioFile")
    hps = fp.get('highlightPatterns', [])
    if pp.get('en') and hps:
        for hp in hps:
            if not re.search(hp, pp['en'], re.IGNORECASE):
                errors.append(f"{fp['id']}: highlightPattern NOT in passage: '{hp}'")

audio_dir = os.path.join(os.path.dirname(path), 'audio')
if os.path.exists(audio_dir):
    audio_files = os.listdir(audio_dir)
    pp_a = len([f for f in audio_files if f.startswith('practice_pp')])
    q_a = len([f for f in audio_files if f.startswith('q') and f.endswith('.mp3')])
    fp_a = len([f for f in audio_files if f.startswith('fp')])
    vocab_dir = os.path.join(audio_dir, 'vocab')
    v_a = len(os.listdir(vocab_dir)) if os.path.exists(vocab_dir) else 0
    lines.append(f"Audio: {len(audio_files)} + {v_a} vocab")
    lines.append(f"  PP:{pp_a}/4 Q:{q_a}/25 FP:{fp_a}/12 V:{v_a}/20")
else:
    errors.append("Audio directory NOT FOUND")

for s in d.get('sections', []):
    answers = ' '.join(f"({q['number']}){q['answer']}" for q in s['questions'])
    lines.append(f"{s['name']}: {answers}")

if errors:
    lines.append(f"FAILED ({len(errors)} errors):")
    for e in errors:
        lines.append(f"  - {e}")
else:
    lines.append("ALL CHECKS PASSED")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_result.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print("Done -> _result.txt")
