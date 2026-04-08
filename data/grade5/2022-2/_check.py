"""Verify grade5 2022-2 data.json structure and completeness"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

path = os.path.join(os.path.dirname(__file__), 'data.json')
d = json.load(open(path, 'r', encoding='utf-8'))

print(f"=== {d.get('title', '?')} ===")
print(f"Grade: {d.get('grade', '?')}")
print(f"Exam: {d.get('exam', '?')}")

# Sections
print(f"\n--- Sections ({len(d.get('sections', []))}) ---")
for i, s in enumerate(d.get('sections', [])):
    qs = s.get('questions', [])
    print(f"  Section {i}: {s.get('name','?')} ({s.get('type','?')}) - {len(qs)} questions")
    # Check fields
    for q in qs:
        missing = []
        for key in ['grammar', 'grammarSimple', 'choiceAnalysis', 'choiceAnalysisSimple']:
            if key not in q:
                missing.append(key)
        if missing:
            print(f"    Q{q.get('number','?')}: MISSING {missing}")
    # sentence-order checks
    if s.get('type') == 'sentence-order':
        for q in qs:
            slots = q.get('answerSlots')
            words = q.get('words', [])
            if slots != [1, 3]:
                print(f"    Q{q.get('number','?')}: answerSlots={slots} (should be [1,3])")
            if len(words) != 4:
                print(f"    Q{q.get('number','?')}: words count={len(words)} (should be 4)")

# Vocabulary
vocab = d.get('vocabulary', [])
print(f"\n--- Vocabulary ({len(vocab)}) ---")
eng_dist = []
for v in vocab:
    for dist in v.get('distractors', []):
        if all(ord(ch) < 128 for ch in dist.replace(' ', '')):
            eng_dist.append(f"  {v['word']}: English distractor '{dist}'")
    if 'wordAudio' not in v:
        print(f"  {v.get('word','?')}: MISSING wordAudio")
if eng_dist:
    print("  ⚠ ENGLISH DISTRACTORS FOUND:")
    for e in eng_dist:
        print(e)
else:
    print("  ✅ All distractors are Japanese")

# Lesson Plan
fps = d.get('lessonPlan', {}).get('focusPoints', [])
print(f"\n--- Focus Points ({len(fps)}) ---")
for fp in fps:
    print(f"  {fp.get('id','?')}: {fp.get('title','?')}")
    pp = fp.get('practicePassage', {})
    if not pp.get('en'):
        print(f"    ⚠ MISSING practicePassage.en")
    if not pp.get('ja'):
        print(f"    ⚠ MISSING practicePassage.ja")
    if not pp.get('audioFile'):
        print(f"    ⚠ MISSING practicePassage.audioFile")
    pqs = fp.get('practiceQuestions', [])
    if not pqs:
        print(f"    ⚠ MISSING practiceQuestions")
    hps = fp.get('highlightPatterns', [])
    if not hps:
        print(f"    ⚠ MISSING highlightPatterns")
    # Check highlightPatterns in passage
    if pp.get('en') and hps:
        passage_lower = pp['en'].lower()
        for hp in hps:
            if hp.lower() not in passage_lower:
                print(f"    ⚠ highlightPattern NOT in passage: '{hp}'")

# Audio files
audio_dir = os.path.join(os.path.dirname(__file__), 'audio')
if os.path.exists(audio_dir):
    audio_files = os.listdir(audio_dir)
    print(f"\n--- Audio Files ({len(audio_files)}) ---")
    # Check practice passage audio
    for fp in fps:
        af = fp.get('practicePassage', {}).get('audioFile', '')
        if af:
            full = os.path.join(os.path.dirname(__file__), af)
            exists = os.path.exists(full)
            print(f"  {af}: {'✅' if exists else '❌ MISSING'}")
    # Check question audio
    total_qs = sum(len(s.get('questions', [])) for s in d.get('sections', []))
    q_audio = [f for f in audio_files if f.startswith('q') and f.endswith('.mp3')]
    print(f"  Question audio: {len(q_audio)}/{total_qs}")
    # Check word audio
    w_audio = [f for f in audio_files if f.startswith('word_')]
    print(f"  Word audio: {len(w_audio)}/{len(vocab)}")
    # Check FP audio
    sq_audio = [f for f in audio_files if f.startswith('sq_')]
    ex_audio = [f for f in audio_files if f.startswith('ex_')]
    print(f"  FP sourceQuote audio: {len(sq_audio)}/{len(fps)}")
    print(f"  FP examples audio: {len(ex_audio)}")
else:
    print(f"\n--- Audio Directory: ❌ NOT FOUND ---")

# Answer key summary
print(f"\n--- Answer Key ---")
for s in d.get('sections', []):
    answers = [f"({q.get('number','')}){q.get('answer','')}" for q in s.get('questions', [])]
    print(f"  {s.get('name','?')}: {' '.join(answers)}")

print("\n=== Verification Complete ===")
