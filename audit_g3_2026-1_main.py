# -*- coding: utf-8 -*-
"""2026-1 3級（本会場）総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

OFFICIAL = {
    1: 3, 2: 3, 3: 1, 4: 2, 5: 2, 6: 1, 7: 4, 8: 4, 9: 2, 10: 2,
    11: 1, 12: 4, 13: 3, 14: 3, 15: 1,
    16: 2, 17: 3, 18: 4, 19: 2, 20: 4,
    21: 1, 22: 4, 23: 1, 24: 2, 25: 3,
    26: 1, 27: 2, 28: 4, 29: 3, 30: 2,
}

LISTENING = {
    "part1": {1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2, 7: 3, 8: 1, 9: 3, 10: 2},
    "part2": {11: 2, 12: 3, 13: 3, 14: 3, 15: 1, 16: 4, 17: 3, 18: 3, 19: 1, 20: 1},
    "part3": {21: 1, 22: 4, 23: 1, 24: 1, 25: 4, 26: 1, 27: 3, 28: 2, 29: 2, 30: 4},
}

MONOTONY_PHRASES = {
    "と矛盾": 8,
    "意味が通らない": 8,
    "不自然": 12,
    "記述はない": 8,
    "書かれていない": 25,
}

d = json.load(open(DATA, encoding="utf-8"))
issues = []
warns = []


def passage_corpus(p):
    corpus = " ".join(p.get("paragraphs", []))
    for em in p.get("emails", []):
        corpus += " " + em.get("body", "")
    return corpus


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((sec["name"], sec.get("type"), q, None))
        for p in sec.get("passages", []):
            corpus = passage_corpus(p)
            for q in p.get("questions", []):
                out.append((sec["name"], sec.get("type"), q, corpus))
    return out


def has_english_evidence(text):
    if re.search(r"[（(][^）)]*[A-Za-z]{3,}[^）)]*[）)]", text):
        return True
    if re.search(r"[A-Za-z]{3,}(?:\s+[A-Za-z]{2,})+", text):
        return True
    if re.search(r"^[✅❌]\s*[A-Za-z]", text):
        return True
    return False


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q, _ in all_qs}

# ---- 1. メタデータ ----
for key in ("grade", "year", "session", "title", "exam", "sections", "vocabulary", "lessonPlan"):
    if key not in d:
        issues.append(f"top-level: missing {key}")

# ---- 2. 正答 ----
for n, ans in OFFICIAL.items():
    if n not in seen:
        issues.append(f"[正答] Q{n}: 問題欠落")
for _, _, q, _ in all_qs:
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
for _, _, q, _ in all_qs:
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

# ---- 5. 構造 ----
for sec in d["sections"]:
    for p in sec.get("passages", []):
        if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
            issues.append(f"[構造] {p.get('title')}: paragraphs/translations不一致")
        if p.get("format") == "multi-email":
            for em in p.get("emails", []):
                if not em.get("translation"):
                    issues.append(f"[構造] passage {p.get('label')}: email translation欠落")

# ---- 6. sourceEvidence（大問3 = Q21〜30）----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    if n < 21:
        continue
    ev = q.get("sourceEvidence")
    if not ev:
        issues.append(f"[根拠] Q{n}: sourceEvidence未設定")
        continue
    ev_list = ev if isinstance(ev, list) else [ev]
    if not ev_list:
        issues.append(f"[根拠] Q{n}: sourceEvidenceが空")
        continue
    if corpus:
        for phrase in ev_list:
            if phrase not in corpus:
                issues.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:60]}...")

# ---- 7. 解説の英文エビデンス ----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            issues.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")
    ans_idx = q["answer"] - 1
    correct_ca = q.get("choiceAnalysis", [])[ans_idx] if q.get("choiceAnalysis") else ""
    if n >= 21 and not has_english_evidence(correct_ca):
        issues.append(f"[根拠] Q{n}: 正解解説に本文引用なし")

# ---- 8. 単調さ ----
phrase_counts = Counter()
for _, _, q, _ in all_qs:
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
if len(vocab) != 30:
    issues.append(f"[語彙] count={len(vocab)} != 30")
for i, v in enumerate(vocab):
    rel = v.get("wordAudio", "")
    expected = f"audio/vocab/w_{i+1:03d}_"
    if not rel.startswith(expected):
        issues.append(f"[音声] vocab {v['word']}: wordAudio {rel}")
    fp = os.path.join(BASE, rel.replace("/", os.sep))
    if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
        issues.append(f"[音声] vocab {v['word']}: {rel} 欠落")

# ---- 10. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += passage_corpus(p) + " "

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
    for pat in fp.get("highlightPatterns", []):
        if pat not in corpus_all and pat not in pp.get("en", ""):
            issues.append(f"[FP] {fid}: highlight不在: {pat[:50]}")

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
sys.exit(1 if issues else 0)
