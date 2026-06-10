# -*- coding: utf-8 -*-
"""2026-1-sat data.json 構造検証スクリプト（ワークフロー Step 5a 準拠）"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")


def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []

    # 1. トップレベルキー
    for k in ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]:
        if k not in d:
            errors.append(f"Missing top-level key: {k}")
    vocab = d.get("vocabulary", [])
    if len(vocab) < 50:
        errors.append(f"vocabulary count = {len(vocab)}, must be 50+")

    # 2. sections
    types = {s["type"] for s in d.get("sections", [])}
    for t in ["vocabulary", "passage-fill", "reading-comprehension"]:
        if t not in types:
            errors.append(f"Missing section type: {t}")

    # 3. focusPoints
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5:
        errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        if fp.get("id") != f"fp{i+1}":
            errors.append(f"FP{i+1}: id mismatch ({fp.get('id')})")
        for key in ["explanation", "examples", "practicePassage", "practiceQuestions",
                    "highlightPatterns", "highlightColor", "highlightLabel"]:
            if key not in fp:
                errors.append(f"FP{i+1} '{fp.get('title','')}': missing '{key}'")
        pp = fp.get("practicePassage", {})
        if not pp.get("en") or not pp.get("ja"):
            errors.append(f"FP{i+1}: practicePassage missing 'en' or 'ja'")
        pq = fp.get("practiceQuestions", [])
        if len(pq) < 3:
            errors.append(f"FP{i+1}: only {len(pq)} practiceQuestions (need 3-4)")
        hp = fp.get("highlightPatterns", [])
        if len(hp) < 3:
            errors.append(f"FP{i+1}: only {len(hp)} highlight patterns")

    # 4. sentencePairs 完全一致
    for s in d.get("sections", []):
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND: '{pair[0][:50]}...'")

    # 5. answer 範囲（1-indexed）と問題数
    counts = {}
    for s in d.get("sections", []):
        qs = list(s.get("questions", []))
        for p in s.get("passages", []):
            qs += p.get("questions", [])
        counts[s["name"]] = len(qs)
        for q in qs:
            a = q.get("answer")
            if a is None or not (1 <= a <= 4):
                errors.append(f"Q{q.get('number')}: answer={a} out of range 1-4")
            if len(q.get("choices", [])) != 4:
                errors.append(f"Q{q.get('number')}: choices != 4")
            ca = q.get("choiceAnalysis", [])
            if len(ca) != 4:
                errors.append(f"Q{q.get('number')}: choiceAnalysis != 4")

    expected = {"大問1": 17, "大問2": 6, "大問3": 8}
    for name, n in expected.items():
        if counts.get(name) != n:
            errors.append(f"{name}: {counts.get(name)}問 (expected {n})")

    # 6. 正答表との照合
    key = {1:3,2:2,3:3,4:3,5:1,6:3,7:3,8:1,9:4,10:3,11:3,12:3,13:4,14:2,15:3,16:1,17:1,
           18:4,19:2,20:3,21:1,22:4,23:3,24:4,25:1,26:3,27:1,28:3,29:4,30:2,31:1}
    for s in d.get("sections", []):
        qs = list(s.get("questions", []))
        for p in s.get("passages", []):
            qs += p.get("questions", [])
        for q in qs:
            if key.get(q["number"]) != q["answer"]:
                errors.append(f"Q{q['number']}: answer={q['answer']}, 正答表={key.get(q['number'])}")

    if errors:
        print("⚠ VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("✅ ALL CHECKS PASSED")
    print(f"  vocabulary: {len(vocab)}語 / sections: {len(d['sections'])} / focusPoints: {len(fps)}")
    print(f"  問題数: {counts}")


import os
verify(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "grade2", "2026-1-sat", "data.json"))
