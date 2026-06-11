# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade-pre2", "2026-1", "data.json")
ADIR = os.path.join(BASE, "data", "grade-pre2", "2026-1")

OFFICIAL = {
    1: 2, 2: 1, 3: 1, 4: 4, 5: 4, 6: 3, 7: 2, 8: 3, 9: 4, 10: 1,
    11: 2, 12: 4, 13: 1, 14: 1, 15: 2,
    16: 1, 17: 3, 18: 2, 19: 1, 20: 3,
    21: 4, 22: 1, 23: 3, 24: 4, 25: 3, 26: 3, 27: 4, 28: 2, 29: 3,
}

LISTENING = {
    "part1": {
        1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1, 7: 3, 8: 3, 9: 3, 10: 1,
    },
    "part2": {
        11: 3, 12: 3, 13: 4, 14: 1, 15: 4, 16: 2, 17: 1, 18: 2, 19: 1, 20: 4,
    },
    "part3": {
        21: 3, 22: 3, 23: 2, 24: 2, 25: 2, 26: 1, 27: 2, 28: 2, 29: 3, 30: 4,
    },
}

MONOTONY_PHRASES = {
    "と矛盾": 8,
    "意味が通らない": 6,
    "不自然": 10,
    "正反対": 6,
    "記述はない": 4,
}

d = json.load(open(DATA_PATH, encoding="utf-8"))
issues = []
warns = []


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((sec["name"], sec.get("type"), q, None))
        for p in sec.get("passages", []):
            corpus = " ".join(p.get("paragraphs", []))
            for q in p.get("questions", []):
                out.append((sec["name"], sec.get("type"), q, corpus))
    return out


def has_english_evidence(text):
    """choiceAnalysis に英文根拠（括弧内引用 or 英単語列）があるか"""
    if re.search(r"[（(][^）)]*[A-Za-z]{4,}[^）)]*[）)]", text):
        return True
    if re.search(r"[A-Za-z]{3,}(?:\s+[A-Za-z]{2,}){1,}", text):
        return True
    return False


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q, _ in all_qs}

# ---- 1. 正答 ----
for n, ans in OFFICIAL.items():
    if n not in seen:
        issues.append(f"[正答] Q{n}: 問題欠落")
for _, _, q, _ in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        issues.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL.get(n)}")

# ---- 2. リスニング ----
for part, expected in LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for k, v in expected.items():
        key = str(k)
        gv = got.get(key, got.get(k))
        if gv != v:
            issues.append(f"[リスニング] {part} Q{k}: {gv} != {v}")

# ---- 3. choiceAnalysis マーク位置 ----
for sec_name, _, q, _ in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    checks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")]
    if checks != [q["answer"]]:
        issues.append(f"[解説] Q{n}: ✅位置={checks} answer={q['answer']}")
    correct_marks = [i + 1 for i, t in enumerate(ca) if "正解" in t and "誤答" not in t]
    if len(correct_marks) != 1 or correct_marks[0] != q["answer"]:
        issues.append(f"[解説] Q{n}: 「正解」表記={correct_marks} answer={q['answer']}")

# ---- 4. sentencePairs ----
for sec in d["sections"]:
    for p in sec.get("passages", []):
        full = " ".join(p.get("paragraphs", []))
        for i, pair in enumerate(p.get("sentencePairs", [])):
            if pair[0] not in full:
                issues.append(
                    f"[構造] {sec['name']}{p.get('label','')}: sentencePair[{i}] 本文不一致: {pair[0][:50]}..."
                )
        if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
            issues.append(f"[構造] {p.get('title')}: paragraphs/translations数不一致")

# ---- 5. sourceEvidence（大問3・4 = Q21〜29）----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    if n < 21:
        continue
    ev = q.get("sourceEvidence")
    if not ev:
        issues.append(f"[根拠] Q{n}: sourceEvidence未設定")
        continue
    if not isinstance(ev, list) or len(ev) < 1:
        issues.append(f"[根拠] Q{n}: sourceEvidenceが空")
        continue
    if corpus:
        for phrase in ev:
            if phrase not in corpus:
                issues.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:60]}...")

# ---- 6. 解説の英文エビデンス ----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    context = corpus or q.get("text", q.get("question", ""))
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            issues.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")
    # 正解解説は本文/会話からの引用を必須（大問3以降は特に厳格）
    ans_idx = q["answer"] - 1
    correct_ca = q.get("choiceAnalysis", [])[ans_idx] if q.get("choiceAnalysis") else ""
    if n >= 21 and not has_english_evidence(correct_ca):
        issues.append(f"[根拠] Q{n}: 正解解説に本文引用なし")

# ---- 7. 単調さチェック ----
phrase_counts = Counter()
for _, _, q, _ in all_qs:
    for ca in q.get("choiceAnalysis", []):
        for phrase in MONOTONY_PHRASES:
            if phrase in ca:
                phrase_counts[phrase] += 1
for phrase, limit in MONOTONY_PHRASES.items():
    cnt = phrase_counts[phrase]
    if cnt > limit:
        warns.append(f"[単調] 「{phrase}」が{cnt}回（推奨上限{limit}）— 言い回しの多様化を検討")

# 同一文末パターン（❌のみ）
endings = Counter()
for _, _, q, _ in all_qs:
    for ca in q.get("choiceAnalysis", []):
        if ca.startswith("❌"):
            m = re.search(r"[。\.]([^。\.]+)$", ca)
            if m:
                endings[m.group(1)] += 1
for end, cnt in endings.items():
    if cnt >= 3:
        warns.append(f"[単調] 誤答文末「{end}」が{cnt}回繰り返し")

# ---- 8. 語彙・音声 ----
vocab = d.get("vocabulary", [])
if len(vocab) != 40:
    issues.append(f"[語彙] count={len(vocab)} != 40")
for i, v in enumerate(vocab):
    rel = v.get("wordAudio", "")
    expected = f"audio/vocab/w_{i+1:03d}_"
    if not rel.startswith(expected):
        issues.append(f"[音声] vocab {v['word']}: wordAudio {rel}")
    fp = os.path.join(ADIR, rel.replace("/", os.sep))
    if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
        issues.append(f"[音声] vocab {v['word']}: {rel} 欠落")

# ---- 9. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "

for fp in d.get("lessonPlan", {}).get("focusPoints", []):
    fid = fp.get("id", "?")
    pp = fp.get("practicePassage", {})
    af = pp.get("audioFile")
    if af:
        fpth = os.path.join(ADIR, af.replace("/", os.sep))
        if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fid}: {af} 欠落")
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
