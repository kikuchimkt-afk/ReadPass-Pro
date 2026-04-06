"""Verify data.json for Pre-Grade 2 2022-1"""
import json
def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []
    for k in ["grade","year","session","title","vocabulary","sections","lessonPlan"]:
        if k not in d: errors.append(f"Missing: {k}")
    vocab = d.get("vocabulary",[])
    if len(vocab) < 40: errors.append(f"vocab={len(vocab)}<40")
    sections = d.get("sections",[])
    if len(sections) != 4: errors.append(f"sections={len(sections)} != 4")
    total_q = 0
    for s in sections:
        total_q += len(s.get("questions",[]))
        for p in s.get("passages",[]): total_q += len(p.get("questions",[]))
    if total_q != 37: errors.append(f"questions={total_q} != 37")
    fps = d.get("lessonPlan",{}).get("focusPoints",[])
    if len(fps) != 5: errors.append(f"fps={len(fps)} != 5")
    for i,fp in enumerate(fps):
        pp = fp.get("practicePassage",{})
        if pp and not pp.get("en","").startswith("[出典:"): errors.append(f"FP{i+1}: no [出典:]")
    # Build full text for HL check
    all_text = []
    for s in sections:
        for q in s.get("questions",[]): all_text.append(q.get("text",""))
        for p in s.get("passages",[]):
            for para in p.get("paragraphs",[]): all_text.append(para)
    full = "\n".join(all_text)
    for fp in fps:
        for pat in fp.get("highlightPatterns",[]):
            if pat not in full: errors.append(f"HL {fp['id']}: '{pat[:50]}...' NOT FOUND")
    # Answer key
    ak = {1:1,2:3,3:3,4:3,5:3,6:1,7:4,8:1,9:4,10:3,11:4,12:3,13:1,14:1,15:4,16:2,17:4,18:1,19:2,20:2,
          21:1,22:3,23:4,24:1,25:3,26:1,27:2,28:4,29:3,30:2,31:1,32:1,33:2,34:1,35:4,36:2,37:4}
    for s in sections:
        for q in s.get("questions",[]):
            n=q["number"]
            if n in ak and q["answer"]!=ak[n]: errors.append(f"Q{n}: {q['answer']}!={ak[n]}")
        for p in s.get("passages",[]):
            for q in p.get("questions",[]):
                n=q["number"]
                if n in ak and q["answer"]!=ak[n]: errors.append(f"Q{n}: {q['answer']}!={ak[n]}")
    # sentencePairs
    for s in sections:
        if s["type"] in ["passage-fill","reading-comprehension"]:
            for p in s.get("passages",[]):
                if not p.get("sentencePairs"): errors.append(f"'{p.get('title','')}': no sentencePairs")
    print(f"INFO: vocab={len(vocab)}, questions={total_q}, fps={len(fps)}")
    if errors:
        print(f"\n⚠ FAILED ({len(errors)}):")
        for e in errors: print(f"  - {e}")
    else:
        print("\n✅ ALL CHECKS PASSED")
verify(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-1\data.json")
