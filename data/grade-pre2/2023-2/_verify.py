"""準2級 2023-2 構造検証スクリプト"""
import json

def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []

    # 1. トップレベルキーチェック
    for k in ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]:
        if k not in d:
            errors.append(f"Missing top-level key: {k}")
    vocab = d.get("vocabulary", [])
    if len(vocab) < 40:
        errors.append(f"vocabulary count = {len(vocab)}, must be 40+")

    # 2. sections チェック（準2級旧形式は4つ）
    sections = d.get("sections", [])
    if len(sections) != 4:
        errors.append(f"sections count = {len(sections)}, expected 4")
    
    # 旧形式: vocab, vocab, passage-fill, reading-comprehension
    expected_types = ["vocabulary", "vocabulary", "passage-fill", "reading-comprehension"]
    for i, s in enumerate(sections):
        if i < len(expected_types) and s.get("type") != expected_types[i]:
            errors.append(f"Section {i}: type='{s.get('type')}', expected '{expected_types[i]}'")

    # 3. 問題数チェック（旧形式37問）
    total_q = 0
    for s in sections:
        total_q += len(s.get("questions", []))
        for p in s.get("passages", []):
            total_q += len(p.get("questions", []))
    if total_q != 37:
        errors.append(f"Total questions = {total_q}, expected 37")

    # 4. 大問1・大問2チェック
    if len(sections) >= 2:
        q1 = len(sections[0].get("questions", []))
        q2 = len(sections[1].get("questions", []))
        if q1 != 20:
            errors.append(f"大問1: {q1} questions, expected 20")
        if q2 != 5:
            errors.append(f"大問2: {q2} questions, expected 5")

    # 5. パッセージチェック
    for s in sections:
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                if not p.get("paragraphs"):
                    errors.append(f"{s['name']} {p.get('label','')}: NO paragraphs")
                if not p.get("translations"):
                    errors.append(f"{s['name']} {p.get('label','')}: NO translations")
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"{s['name']} {p.get('label','')}: NO sentencePairs")
                # Verify sentencePairs match paragraphs
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND: '{pair[0][:60]}...'")
    
    # 6. 大問4A email format
    if len(sections) >= 4:
        p4a = sections[3].get("passages", [{}])[0]
        if p4a.get("format") != "email":
            errors.append("大問4A: missing format='email'")
        if not p4a.get("meta"):
            errors.append("大問4A: missing meta")

    # 7. focusPoints チェック
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
            en = pp.get("en", "")
            if not en.startswith("[出典:"):
                errors.append(f"FP{i+1}: practicePassage.en must start with '[出典:]'")
        pq = fp.get("practiceQuestions", [])
        if len(pq) < 3:
            errors.append(f"FP{i+1}: only {len(pq)} practiceQuestions (need 3-4)")
        hp = fp.get("highlightPatterns", [])
        if len(hp) < 3:
            errors.append(f"FP{i+1}: only {len(hp)} highlight patterns (need 3+)")

    # 8. highlightPatterns 整合性チェック
    all_text = []
    for s in sections:
        for q in s.get("questions", []):
            all_text.append(q.get("text", ""))
        for p in s.get("passages", []):
            for para in p.get("paragraphs", []):
                all_text.append(para)
    full_text = "\n".join(all_text)
    for fp in fps:
        for pat in fp.get("highlightPatterns", []):
            if pat not in full_text:
                errors.append(f"HL MISMATCH {fp['id']}: '{pat}' NOT FOUND in exam text")

    # 9. answer 範囲チェック (1-indexed: 1-4)
    answers = {
        1:3,2:4,3:1,4:2,5:2,6:2,7:1,8:1,9:4,10:2,
        11:1,12:4,13:4,14:2,15:2,16:1,17:2,18:2,19:2,20:3,
        21:2,22:2,23:1,24:1,25:2,
        26:4,27:1,28:2,29:1,30:3,
        31:2,32:2,33:1,34:4,35:2,36:3,37:1
    }
    for s in sections:
        qs = list(s.get("questions", []))
        for p in s.get("passages", []):
            qs += list(p.get("questions", []))
        for q in qs:
            qn = q.get("number")
            a = q.get("answer")
            if qn in answers and a != answers[qn]:
                errors.append(f"Q{qn}: answer={a}, expected={answers[qn]}")
            if not q.get("choiceAnalysis"):
                errors.append(f"Q{qn}: missing choiceAnalysis")
            if not q.get("grammar"):
                errors.append(f"Q{qn}: missing grammar")

    # 10. wordAudio チェック
    missing_audio = sum(1 for v in vocab if "wordAudio" not in v)
    if missing_audio:
        errors.append(f"{missing_audio} vocabulary items missing wordAudio")

    # 11. audioFile チェック
    import os
    base_dir = os.path.dirname(path)
    for fp in fps:
        pp = fp.get("practicePassage", {})
        af = pp.get("audioFile", "")
        if af:
            full_path = os.path.join(base_dir, af)
            if not os.path.exists(full_path):
                errors.append(f"FP {fp['id']}: audioFile not found: {af}")
        else:
            errors.append(f"FP {fp['id']}: no audioFile in practicePassage")

    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, focusPoints={len(fps)}")

    if errors:
        print(f"\n⚠ VERIFICATION FAILED ({len(errors)} errors):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\n✅ ALL CHECKS PASSED")
    return errors

verify(r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2\data.json")
