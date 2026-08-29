# -*- coding: utf-8 -*-
"""2026-1 準2級（本会場）総合監査 — 正答・解説エビデンス・単調さ・音声"""
import json
import hashlib
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

# 原本PDF（SHA-256: 70293E...FFCC0）から転記した、問題英文・選択肢・正答・
# 本文・メールメタ情報・設問の正規化スナップショット。
# 解説を直す際に出題内容そのものを誤って変えないための不変条件。
SOURCE_PAYLOAD_SHA256 = "d630c1da0f93894a0e800d722f7fe7660e05b8ae90aa5ad129a92d8999fd68fc"

EXPECTED_VOCAB_SOURCES = {
    "大問1": 15,
    "大問2": 10,
    "大問3": 5,
    "大問4A": 5,
    "大問4B": 5,
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


def has_blank(text):
    return bool(re.search(r"[_＿]{2,}|[（(][\s　]*[）)]", text or ""))


def has_numbered_blank(text, number):
    return bool(re.search(rf"[（(][\s　]*{number}[\s　]*[）)]", text or ""))


def source_payload(data):
    """原本に由来する不変フィールドだけを正規化する。"""
    payload = []
    for sec in data.get("sections", []):
        item = {
            key: sec.get(key)
            for key in ("name", "nameEn", "type", "instruction")
        }
        if sec.get("questions"):
            item["questions"] = [
                {
                    key: q.get(key)
                    for key in ("number", "text", "choices", "answer")
                }
                for q in sec["questions"]
            ]
        if sec.get("passages"):
            item["passages"] = []
            for passage in sec["passages"]:
                p_item = {
                    key: passage.get(key)
                    for key in ("label", "title", "format", "meta", "paragraphs")
                    if key in passage
                }
                p_item["questions"] = [
                    {
                        key: q.get(key)
                        for key in ("number", "question", "choices", "answer")
                        if key in q
                    }
                    for q in passage.get("questions", [])
                ]
                item["passages"].append(p_item)
        payload.append(item)
    return payload


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q, _ in all_qs}

# ---- 1. メタデータ・原本不変フィールド ----
for key in (
    "grade", "year", "session", "title", "exam", "sections", "listening",
    "vocabulary", "lessonPlan",
):
    if key not in d:
        issues.append(f"[構造] top-level: missing {key}")

payload_json = json.dumps(
    source_payload(d), ensure_ascii=False, sort_keys=True, separators=(",", ":")
).encode("utf-8")
payload_hash = hashlib.sha256(payload_json).hexdigest()
if payload_hash != SOURCE_PAYLOAD_SHA256:
    issues.append(
        f"[原本] 問題英文・選択肢・正答・本文が原本スナップショットと不一致: {payload_hash}"
    )

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
        key = str(k)
        gv = got.get(key, got.get(k))
        if gv != v:
            issues.append(f"[リスニング] {part} Q{k}: {gv} != {v}")

# ---- 4. choiceAnalysis・和訳の空所 ----
for sec_name, _, q, _ in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    if len(q.get("choiceTranslations", [])) != 4:
        issues.append(f"[解説] Q{n}: choiceTranslations数={len(q.get('choiceTranslations', []))}")
    if not q.get("grammar"):
        issues.append(f"[解説] Q{n}: grammar未設定")
    checks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")]
    crosses = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("❌")]
    if n <= 15:
        if checks != [q["answer"]]:
            issues.append(f"[解説] Q{n}: ✅位置={checks} answer={q['answer']}")
        expected_crosses = [i for i in range(1, 5) if i != q["answer"]]
        if crosses != expected_crosses:
            issues.append(f"[解説] Q{n}: ❌位置={crosses} expected={expected_crosses}")
    elif checks or crosses:
        issues.append(f"[解説] Q{n}: 大問2以降に✅/❌が残っている")
    correct_marks = [i + 1 for i, t in enumerate(ca) if "正解" in t and "誤答" not in t]
    if len(correct_marks) != 1 or correct_marks[0] != q["answer"]:
        issues.append(f"[解説] Q{n}: 「正解」表記={correct_marks} answer={q['answer']}")
    if n >= 16:
        correct_text = ca[q["answer"] - 1]
        if "💡" not in correct_text:
            issues.append(f"[解説] Q{n}: 正答解説に💡がない")
    if n <= 20 and has_blank(q.get("text")) and not has_blank(q.get("translation")):
        issues.append(f"[和訳] Q{n}: 英文の空所が和訳に残っていない")

# ---- 5. sentencePairs・本文和訳 ----
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
        for key in ("title", "paragraphs", "translations", "sentencePairs", "questions"):
            if not p.get(key) and key != "title":
                issues.append(f"[構造] {p.get('title')}: {key}未設定")
        if sec.get("type") == "passage-fill":
            english = " ".join(p.get("paragraphs", []))
            japanese = " ".join(p.get("translations", []))
            for q in p.get("questions", []):
                n = q["number"]
                if has_numbered_blank(english, n) and not has_numbered_blank(japanese, n):
                    issues.append(f"[和訳] Q{n}: 長文和訳に番号付き空所が残っていない")

# ---- 6. sourceEvidence（大問3・4 = Q21〜29）----
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

# ---- 7. 解説の英文エビデンス ----
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

# ---- 8. 単調さチェック ----
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

# ---- 9. 語彙・音声 ----
vocab = d.get("vocabulary", [])
if len(vocab) != 40:
    issues.append(f"[語彙] count={len(vocab)} != 40")
source_counts = Counter()
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "source", "example", "distractors"):
        if not v.get(key):
            issues.append(f"[語彙] vocab[{i}]: {key}未設定")
    if len(v.get("distractors", [])) != 3:
        issues.append(f"[語彙] {v.get('word')}: distractors数={len(v.get('distractors', []))}")
    source_counts[v.get("source")] += 1
    rel = v.get("wordAudio", "")
    expected = f"audio/vocab/w_{i+1:03d}_"
    if not rel.startswith(expected):
        issues.append(f"[音声] vocab {v['word']}: wordAudio {rel}")
    fp = os.path.join(ADIR, rel.replace("/", os.sep))
    if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
        issues.append(f"[音声] vocab {v['word']}: {rel} 欠落")
    example_rel = v.get("exampleAudio", "")
    expected_example = f"audio/vocab/ex_{i+1:03d}_"
    if not example_rel.startswith(expected_example):
        issues.append(f"[音声] vocab {v.get('word')}: exampleAudio {example_rel}")
    example_fp = os.path.join(ADIR, example_rel.replace("/", os.sep))
    if not os.path.isfile(example_fp) or os.path.getsize(example_fp) < 500:
        issues.append(f"[音声] vocab {v.get('word')}: {example_rel} 欠落")

for source, expected_count in EXPECTED_VOCAB_SOURCES.items():
    if source_counts[source] != expected_count:
        issues.append(f"[語彙] {source}: count={source_counts[source]} != {expected_count}")

# ---- 10. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "

focus_points = d.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    issues.append(f"[FP] focusPoints数={len(focus_points)} != 5")

for index, fp in enumerate(focus_points, 1):
    fid = fp.get("id", "?")
    if fid != f"fp{index}":
        issues.append(f"[FP] index={index}: id={fid}")
    for key in (
        "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
        "highlightColor", "highlightLabel",
    ):
        if not fp.get(key):
            issues.append(f"[FP] {fid}: {key}未設定")
    if len(fp.get("examples", [])) < 3:
        issues.append(f"[FP] {fid}: examples数={len(fp.get('examples', []))}")
    for ex_index, example in enumerate(fp.get("examples", []), 1):
        if not all(example.get(key) for key in ("en", "ja", "note")):
            issues.append(f"[FP] {fid}: example[{ex_index}]不完全")
    if len(fp.get("practiceQuestions", [])) < 4:
        issues.append(f"[FP] {fid}: practiceQuestions数={len(fp.get('practiceQuestions', []))}")
    for q_index, practice_q in enumerate(fp.get("practiceQuestions", []), 1):
        if not practice_q.get("q") or not practice_q.get("a"):
            issues.append(f"[FP] {fid}: practiceQuestion[{q_index}]不完全")
    pp = fp.get("practicePassage", {})
    if not pp.get("en") or not pp.get("ja") or "[出典:" not in pp.get("en", ""):
        issues.append(f"[FP] {fid}: practicePassage不完全")
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
