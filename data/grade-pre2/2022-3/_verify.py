"""Verify data.json structure for Pre-Grade 2 2022-3"""
import json

def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []

    # 1. Top-level keys
    for k in ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]:
        if k not in d:
            errors.append(f"Missing top-level key: {k}")
    vocab = d.get("vocabulary", [])
    if len(vocab) < 40:
        errors.append(f"vocabulary count = {len(vocab)}, must be 40+")

    # 2. sections check
    sections = d.get("sections", [])
    if len(sections) != 4:
        errors.append(f"sections count = {len(sections)}, expected 4")
    expected_types = ["vocabulary", "vocabulary", "passage-fill", "reading-comprehension"]
    for i, s in enumerate(sections):
        if i < len(expected_types) and s.get("type") != expected_types[i]:
            errors.append(f"Section {i}: type='{s.get('type')}', expected '{expected_types[i]}'")

    # 3. Question count (old format = 37)
    total_q = 0
    for s in sections:
        total_q += len(s.get("questions", []))
        for p in s.get("passages", []):
            total_q += len(p.get("questions", []))
    if total_q not in (29, 37):
        errors.append(f"Total questions = {total_q}, expected 29 (new) or 37 (old)")

    # 4. Part 1 & Part 2 check
    if len(sections) >= 2:
        q1 = len(sections[0].get("questions", []))
        q2 = len(sections[1].get("questions", []))
        if q1 not in (15, 20):
            errors.append(f"大問1: {q1} questions, expected 15 (new) or 20 (old)")
        if q2 != 5:
            errors.append(f"大問2: {q2} questions, expected 5")

    # 5. focusPoints check
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5:
        errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        if "id" not in fp:
            errors.append(f"FP{i+1}: missing 'id'")
        for key in ["explanation", "examples", "practicePassage", "practiceQuestions", "highlightPatterns", "highlightColor", "highlightLabel"]:
            if key not in fp:
                errors.append(f"FP{i+1} '{fp.get('title','')}': missing '{key}'")
        if "practicePassage" in fp:
            pp = fp["practicePassage"]
            if not pp.get("en") or not pp.get("ja"):
                errors.append(f"FP{i+1}: practicePassage missing 'en' or 'ja'")
            if not pp.get("audioFile"):
                errors.append(f"FP{i+1}: practicePassage missing 'audioFile'")
            en = pp.get("en", "")
            if not en.startswith("[出典:"):
                errors.append(f"FP{i+1}: practicePassage.en must start with '[出典: ...]'")
        pq = fp.get("practiceQuestions", [])
        if len(pq) < 3:
            errors.append(f"FP{i+1}: only {len(pq)} practiceQuestions (need 3-4)")
        hp = fp.get("highlightPatterns", [])
        if len(hp) < 3:
            errors.append(f"FP{i+1}: only {len(hp)} highlight patterns (need 4+)")

    # 6. highlightPatterns match check
    all_text = []
    for s in sections:
        for q in s.get("questions", []):
            all_text.append(q.get("text", ""))
            for c in q.get("choices", []):
                all_text.append(c)
        for p in s.get("passages", []):
            for para in p.get("paragraphs", []):
                all_text.append(para)
            for q in p.get("questions", []):
                all_text.append(q.get("question", ""))
                for c in q.get("choices", []):
                    all_text.append(c)
    full_text = "\n".join(all_text)
    for fp in fps:
        for pat in fp.get("highlightPatterns", []):
            if pat not in full_text:
                errors.append(f"HL MISMATCH {fp['id']}: '{pat}' NOT FOUND in exam text")

    # 7. sentencePairs check
    for s in sections:
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND: '{pair[0][:60]}...'")

    # 8. answer range & analysis check
    for s in sections:
        qs = list(s.get("questions", []))
        for p in s.get("passages", []):
            qs += list(p.get("questions", []))
        for q in qs:
            a = q.get("answer")
            if a is not None and (a < 1 or a > 4):
                errors.append(f"Q{q.get('number')}: answer={a} out of range 1-4")
            if not q.get("choiceAnalysis"):
                errors.append(f"Q{q.get('number')}: missing choiceAnalysis")
            if not q.get("grammar"):
                errors.append(f"Q{q.get('number')}: missing grammar")

    # 9. Answer key verification
    answer_key = {
        1:3, 2:1, 3:3, 4:1, 5:3, 6:3, 7:4, 8:2, 9:2, 10:1,
        11:2, 12:2, 13:3, 14:4, 15:2, 16:3, 17:3, 18:2, 19:2, 20:2,
        21:4, 22:1, 23:3, 24:2, 25:1,
        26:2, 27:1, 28:3, 29:1, 30:2,
        31:2, 32:3, 33:4, 34:3, 35:1, 36:3, 37:4
    }
    for s in sections:
        for q in s.get("questions", []):
            n = q["number"]
            if n in answer_key and q["answer"] != answer_key[n]:
                errors.append(f"Q{n}: answer={q['answer']}, expected {answer_key[n]}")
        for p in s.get("passages", []):
            for q in p.get("questions", []):
                n = q["number"]
                if n in answer_key and q["answer"] != answer_key[n]:
                    errors.append(f"Q{n}: answer={q['answer']}, expected {answer_key[n]}")

    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, focusPoints={len(fps)}")

    if errors:
        print(f"\n⚠ VERIFICATION FAILED ({len(errors)} errors):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\n✅ ALL CHECKS PASSED")

verify(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-3\data.json")
