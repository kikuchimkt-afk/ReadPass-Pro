"""Verify data.json structure for Pre-Grade 2 2022-2"""
import json

def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []
    for k in ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]:
        if k not in d: errors.append(f"Missing top-level key: {k}")
    vocab = d.get("vocabulary", [])
    if len(vocab) < 40: errors.append(f"vocabulary count = {len(vocab)}, must be 40+")
    sections = d.get("sections", [])
    if len(sections) != 4: errors.append(f"sections count = {len(sections)}, expected 4")
    total_q = 0
    for s in sections:
        total_q += len(s.get("questions", []))
        for p in s.get("passages", []): total_q += len(p.get("questions", []))
    if total_q not in (29, 37): errors.append(f"Total questions = {total_q}, expected 29 or 37")
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5: errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        for key in ["id","explanation","examples","practicePassage","practiceQuestions","highlightPatterns","highlightColor","highlightLabel"]:
            if key not in fp: errors.append(f"FP{i+1}: missing '{key}'")
        pp = fp.get("practicePassage", {})
        if pp and not pp.get("en","").startswith("[出典:"): errors.append(f"FP{i+1}: practicePassage must start with '[出典:]'")
    # Highlight match check
    all_text = []
    for s in sections:
        for q in s.get("questions", []): all_text.append(q.get("text", ""))
        for p in s.get("passages", []):
            for para in p.get("paragraphs", []): all_text.append(para)
    full_text = "\n".join(all_text)
    for fp in fps:
        for pat in fp.get("highlightPatterns", []):
            if pat not in full_text: errors.append(f"HL MISMATCH {fp['id']}: '{pat}' NOT FOUND")
    # Answer key 2022-2
    answer_key = {1:1,2:2,3:2,4:2,5:1,6:3,7:4,8:1,9:3,10:2,11:1,12:2,13:2,14:1,15:3,16:2,17:2,18:4,19:2,20:1,
                  21:2,22:4,23:4,24:1,25:2,26:4,27:1,28:2,29:4,30:3,31:2,32:4,33:4,34:3,35:3,36:1,37:2}
    for s in sections:
        for q in s.get("questions", []):
            n = q["number"]
            if n in answer_key and q["answer"] != answer_key[n]: errors.append(f"Q{n}: answer={q['answer']}, expected {answer_key[n]}")
        for p in s.get("passages", []):
            for q in p.get("questions", []):
                n = q["number"]
                if n in answer_key and q["answer"] != answer_key[n]: errors.append(f"Q{n}: answer={q['answer']}, expected {answer_key[n]}")
    # sentencePairs check
    for s in sections:
        if s["type"] in ["passage-fill","reading-comprehension"]:
            for p in s.get("passages", []):
                if not p.get("sentencePairs"): errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, focusPoints={len(fps)}")
    if errors:
        print(f"\n⚠ VERIFICATION FAILED ({len(errors)} errors):")
        for e in errors: print(f"  - {e}")
    else:
        print("\n✅ ALL CHECKS PASSED")

verify(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2\data.json")
