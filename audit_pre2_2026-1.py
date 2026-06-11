# -*- coding: utf-8 -*-
"""2026-1-sat 準2級 総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat",
)
DATA = os.path.join(BASE, "data.json")

OFFICIAL = {
    1: 2, 2: 2, 3: 3, 4: 4, 5: 3, 6: 4, 7: 3, 8: 4, 9: 2, 10: 4,
    11: 4, 12: 2, 13: 3, 14: 1, 15: 2,
    16: 1, 17: 1, 18: 4, 19: 1, 20: 2,
    21: 4, 22: 1, 23: 3, 24: 4, 25: 1, 26: 4, 27: 4, 28: 3, 29: 2,
}

MONOTONY_PHRASES = {
    "と矛盾": 9,
    "意味が通らない": 6,
    "不自然": 10,
    "正反対": 6,
    "記述はない": 6,
}

d = json.load(open(DATA, encoding="utf-8"))
errors = []
warns = []


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((q, None))
        for p in sec.get("passages", []):
            corpus = " ".join(p.get("paragraphs", []))
            for q in p.get("questions", []):
                out.append((q, corpus))
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
seen = {q["number"] for q, _ in all_qs}

for n, ans in OFFICIAL.items():
    if n not in seen:
        errors.append(f"[正答] Q{n}: 問題欠落")
for q, _ in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL.get(n)}")

for q, _ in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        errors.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    checks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")]
    if checks != [q["answer"]]:
        errors.append(f"[解説] Q{n}: ✅位置={checks} answer={q['answer']}")

for sec in d["sections"]:
    for p in sec.get("passages", []):
        full = " ".join(p["paragraphs"])
        for i, pair in enumerate(p.get("sentencePairs", [])):
            if pair[0] not in full:
                errors.append(f"sentencePair[{i}] 本文不一致: {pair[0][:50]}...")

for q, corpus in all_qs:
    n = q["number"]
    if n < 21:
        continue
    ev = q.get("sourceEvidence")
    if not ev:
        errors.append(f"[根拠] Q{n}: sourceEvidence未設定")
        continue
    if corpus:
        for phrase in ev:
            if phrase not in corpus:
                errors.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:60]}...")

for q, _ in all_qs:
    n = q["number"]
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            errors.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")

phrase_counts = Counter()
for q, _ in all_qs:
    for ca in q.get("choiceAnalysis", []):
        for phrase in MONOTONY_PHRASES:
            if phrase in ca:
                phrase_counts[phrase] += 1
for phrase, limit in MONOTONY_PHRASES.items():
    if phrase_counts[phrase] > limit:
        warns.append(f"[単調] 「{phrase}」が{phrase_counts[phrase]}回（推奨上限{limit}）")

vocab = d.get("vocabulary", [])
if len(vocab) != 40:
    errors.append(f"[語彙] count={len(vocab)} != 40")

corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "

for fp in d.get("lessonPlan", {}).get("focusPoints", []):
    pp = fp.get("practicePassage", {})
    af = pp.get("audioFile", "")
    if af:
        fpath = os.path.join(BASE, af.replace("/", os.sep))
        if not os.path.isfile(fpath) or os.path.getsize(fpath) < 500:
            errors.append(f"{fp['id']}: missing audio {af}")

print(f"errors={len(errors)} warnings={len(warns)}")
for e in errors:
    print("  [ERROR]", e)
for w in warns:
    print("  [WARN] ", w)
if errors:
    sys.exit(1)
print("AUDIT OK")
