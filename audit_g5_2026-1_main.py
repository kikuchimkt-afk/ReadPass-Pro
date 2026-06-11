# -*- coding: utf-8 -*-
"""2026-1 5級（本会場）総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

OFFICIAL = {
    1: 3, 2: 4, 3: 4, 4: 2, 5: 4, 6: 4, 7: 2, 8: 2, 9: 4, 10: 1,
    11: 1, 12: 4, 13: 1, 14: 4, 15: 1,
    16: 1, 17: 2, 18: 1, 19: 1, 20: 1,
    21: 3, 22: 3, 23: 1, 24: 1, 25: 1,
}

LISTENING = {
    "part1": {1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
    "part2": {11: 2, 12: 1, 13: 1, 14: 2, 15: 2},
    "part3": {
        16: 3, 17: 2, 18: 3, 19: 3, 20: 2,
        21: 3, 22: 1, 23: 2, 24: 1, 25: 3,
    },
}

MONOTONY_PHRASES = {
    "と矛盾": 6,
    "意味が通らない": 8,
    "不自然": 12,
    "記述はない": 4,
    "書かれていない": 4,
    "合わない": 18,
}

d = json.load(open(DATA, encoding="utf-8"))
issues = []
warns = []


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((sec["name"], sec.get("type"), q))
    return out


def has_english_evidence(text):
    if re.search(r"[（(][^）)]*[A-Za-z]{3,}[^）)]*[）)]", text):
        return True
    if re.search(r"[A-Za-z]{3,}(?:\s+[A-Za-z]{2,})+", text):
        return True
    if re.search(r"^[✅❌]\s*[A-Za-z「]", text):
        return True
    return False


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q in all_qs}

# ---- 1. メタデータ ----
for key in ("grade", "year", "session", "title", "exam", "sections", "vocabulary", "lessonPlan"):
    if key not in d:
        issues.append(f"top-level: missing {key}")

# ---- 2. 正答 ----
for n, ans in OFFICIAL.items():
    if n not in seen:
        issues.append(f"[正答] Q{n}: 問題欠落")
for _, _, q in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        issues.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL.get(n)}")

# ---- 3. リスニング ----
for part, expected in LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for k, v in expected.items():
        gv = got.get(str(k), got.get(k))
        if gv != v:
            issues.append(f"[リスニング] {part} Q{k}: {gv} != {v}")

# ---- 4. choiceAnalysis マーク ----
for _, _, q in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    checks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")]
    if checks != [q["answer"]]:
        issues.append(f"[解説] Q{n}: ✅位置={checks} answer={q['answer']}")
    wrong_marks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("❌")]
    if len(wrong_marks) != 3:
        issues.append(f"[解説] Q{n}: ❌数={len(wrong_marks)} (expected 3)")

# ---- 5. 大問1・2 リッチフィールド ----
for sec_name in ("大問1", "大問2"):
    sec = next(s for s in d["sections"] if s["name"] == sec_name)
    for q in sec["questions"]:
        n = q["number"]
        for key in ("grammar", "grammarSimple", "translation", "choiceTranslations",
                    "choiceAnalysis", "choiceAnalysisSimple", "questionAudio"):
            if not q.get(key):
                issues.append(f"[構造] Q{n}: missing {key}")

# ---- 6. 大問3 並べ替え構造 ----
sec3 = next(s for s in d["sections"] if s["name"] == "大問3")
for q in sec3["questions"]:
    n = q["number"]
    for key in ("grammar", "grammarSimple", "choiceAnalysis", "choiceAnalysisSimple",
                "words", "correctOrder", "answerSlots", "questionAudio"):
        if not q.get(key):
            issues.append(f"[構造] Q{n}: missing {key}")
    order = q.get("correctOrder", [])
    words = q.get("words", [])
    slots = q.get("answerSlots", [])
    if len(order) == 4 and len(words) == 4 and len(slots) == 2:
        circled = lambda i: chr(0x2460 + i - 1)
        expected_label = f"{circled(order[slots[0] - 1])} ─ {circled(order[slots[1] - 1])}"
        actual = q["choices"][q["answer"] - 1]
        if actual != expected_label:
            issues.append(f"[並べ替え] Q{n}: {actual} != {expected_label}")

# ---- 7. 解説の英文エビデンス ----
for _, _, q in all_qs:
    n = q["number"]
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            issues.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")

# ---- 8. 単調さ ----
phrase_counts = Counter()
for _, _, q in all_qs:
    for ca in q.get("choiceAnalysis", []):
        for phrase in MONOTONY_PHRASES:
            if phrase in ca:
                phrase_counts[phrase] += 1
for phrase, limit in MONOTONY_PHRASES.items():
    cnt = phrase_counts[phrase]
    if cnt > limit:
        warns.append(f"[単調] 「{phrase}」が{cnt}回（推奨上限{limit}）")

# ---- 9. 語彙・音声 ----
vocab = d.get("vocabulary", [])
if len(vocab) != 20:
    issues.append(f"[語彙] count={len(vocab)} != 20")
for i, v in enumerate(vocab):
    rel = v.get("wordAudio", "")
    expected = f"audio/vocab/w_{i+1:03d}_"
    if not rel.startswith(expected):
        issues.append(f"[音声] vocab {v['word']}: wordAudio {rel}")
    fp = os.path.join(BASE, rel.replace("/", os.sep))
    if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
        issues.append(f"[音声] vocab {v['word']}: {rel} 欠落")
    ex = v.get("exampleAudio")
    if ex:
        efp = os.path.join(BASE, ex.replace("/", os.sep))
        if not os.path.isfile(efp) or os.path.getsize(efp) < 500:
            issues.append(f"[音声] vocab {v['word']}: exampleAudio 欠落")

for _, _, q in all_qs:
    qa = q.get("questionAudio")
    if qa:
        fp = os.path.join(BASE, qa.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            issues.append(f"[音声] Q{q['number']}: {qa} 欠落")

# ---- 10. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
        if q.get("words"):
            corpus_all += " ".join(q["words"]) + " "

for fp in d.get("lessonPlan", {}).get("focusPoints", []):
    fid = fp.get("id", "?")
    pp = fp.get("practicePassage", {})
    af = pp.get("audioFile")
    if af:
        fpth = os.path.join(BASE, af.replace("/", os.sep))
        if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fid}: {af} 欠落")
    for ex in fp.get("examples", []):
        ea = ex.get("audio")
        if ea:
            fpth = os.path.join(BASE, ea.replace("/", os.sep))
            if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
                issues.append(f"[音声] {fid} example: {ea} 欠落")
    sq = fp.get("sourceQuoteAudio")
    if sq:
        fpth = os.path.join(BASE, sq.replace("/", os.sep))
        if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fid}: sourceQuoteAudio 欠落")
    for pat in fp.get("highlightPatterns", []):
        if pat not in corpus_all and pat not in pp.get("en", ""):
            warns.append(f"[FP] {fid}: highlight不在: {pat[:50]}")

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
sys.exit(1 if issues else 0)
