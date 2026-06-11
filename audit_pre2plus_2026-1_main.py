# -*- coding: utf-8 -*-
"""2026-1 準2級プラス（本会場）総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

OFFICIAL = {
    1: 4, 2: 1, 3: 3, 4: 4, 5: 4, 6: 4, 7: 3, 8: 4, 9: 1, 10: 4,
    11: 1, 12: 3, 13: 1, 14: 3, 15: 4, 16: 3, 17: 3,
    18: 2, 19: 4, 20: 3, 21: 1, 22: 2, 23: 4,
    24: 3, 25: 2, 26: 3, 27: 1, 28: 4, 29: 3, 30: 4, 31: 2,
}

LISTENING = {
    "part1": {
        1: 3, 2: 3, 3: 3, 4: 1, 5: 2, 6: 2, 7: 2, 8: 4, 9: 3, 10: 1,
        11: 4, 12: 2, 13: 1, 14: 1, 15: 1,
    },
    "part2": {
        16: 4, 17: 3, 18: 2, 19: 2, 20: 4, 21: 4, 22: 3, 23: 4, 24: 2, 25: 1,
        26: 3, 27: 3, 28: 1, 29: 1, 30: 3,
    },
}

MONOTONY_PHRASES = {
    "と矛盾": 12,
    "意味が通らない": 6,
    "不自然": 14,
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
            out.append((sec["name"], q, None))
        for p in sec.get("passages", []):
            corpus = " ".join(p.get("paragraphs", []))
            for q in p.get("questions", []):
                out.append((sec["name"], q, corpus))
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
seen = {q["number"] for _, q, _ in all_qs}

for key in ("grade", "year", "session", "title", "sections", "vocabulary", "lessonPlan"):
    if key not in d:
        errors.append(f"top-level: missing {key}")

for n, ans in OFFICIAL.items():
    if n not in seen:
        errors.append(f"[正答] Q{n}: 問題欠落")
for _, q, _ in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL.get(n)}")

for part, expected in LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for k, v in expected.items():
        key = str(k)
        gv = got.get(key, got.get(k))
        if gv != v:
            errors.append(f"[リスニング] {part} Q{k}: {gv} != {v}")

for _, q, _ in all_qs:
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
                errors.append(f"{sec['name']}{p.get('label', '')}: sentencePair[{i}] 本文不一致")
        if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
            errors.append(f"[構造] {p.get('title')}: paragraphs/translations不一致")

for sec in d["sections"]:
    if sec["type"] == "passage-fill":
        for p in sec["passages"]:
            text = " ".join(p["paragraphs"])
            blanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", text))
            qnums = sorted(q["number"] for q in p["questions"])
            if blanks != qnums:
                errors.append(f"{sec['name']}{p['label']}: blanks {blanks} != questions {qnums}")

for _, q, corpus in all_qs:
    n = q["number"]
    if n < 18:
        continue
    ev = q.get("sourceEvidence")
    if not ev:
        errors.append(f"[根拠] Q{n}: sourceEvidence未設定")
        continue
    if corpus:
        for phrase in ev:
            if phrase not in corpus:
                errors.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:60]}...")

for _, q, _ in all_qs:
    n = q["number"]
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            errors.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")

phrase_counts = Counter()
for _, q, _ in all_qs:
    for ca in q.get("choiceAnalysis", []):
        for phrase in MONOTONY_PHRASES:
            if phrase in ca:
                phrase_counts[phrase] += 1
for phrase, limit in MONOTONY_PHRASES.items():
    if phrase_counts[phrase] > limit:
        warns.append(f"[単調] 「{phrase}」が{phrase_counts[phrase]}回（推奨上限{limit}）")

vocab = d.get("vocabulary", [])
if len(vocab) != 55:
    errors.append(f"[語彙] count={len(vocab)} != 55")
for i, v in enumerate(vocab):
    rel = v.get("wordAudio", "")
    fp = os.path.join(BASE, rel.replace("/", os.sep))
    if rel and (not os.path.isfile(fp) or os.path.getsize(fp) < 500):
        errors.append(f"[音声] vocab {v['word']}: {rel} 欠落")

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
    for pat in fp.get("highlightPatterns", []):
        if pat not in corpus_all and pat not in pp.get("en", ""):
            errors.append(f"[FP] {fp['id']}: highlight不在: {pat[:50]}")

print(f"errors={len(errors)} warnings={len(warns)}")
for e in errors:
    print("  [ERROR]", e)
for w in warns:
    print("  [WARN] ", w)
if errors:
    sys.exit(1)
print("AUDIT OK")
