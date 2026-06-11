# -*- coding: utf-8 -*-
"""2026-1-sat 準2級プラス 監査スクリプト
原本(gen_pre2plus_2026-1.py 由来の正答・本文)と data.json を突き合わせる。
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data", "grade-pre2plus", "2026-1-sat", "data.json")

d = json.load(open(DATA, encoding="utf-8"))
issues = []
warns = []

# ---- 1. 公式解答（answer_01.png より）----
OFFICIAL = {
    1: 2, 2: 2, 3: 4, 4: 4, 5: 3, 6: 1, 7: 2, 8: 2, 9: 4, 10: 3,
    11: 4, 12: 2, 13: 2, 14: 4, 15: 4, 16: 3, 17: 3,
    18: 2, 19: 1, 20: 4, 21: 3, 22: 2, 23: 1,
    24: 4, 25: 3, 26: 1, 27: 2, 28: 4, 29: 4, 30: 4, 31: 2,
}

all_qs = []
for sec in d.get("sections", []):
    for q in sec.get("questions", []):
        all_qs.append((sec["name"], q))
    for p in sec.get("passages", []):
        for q in p.get("questions", []):
            all_qs.append((sec["name"], q))

seen = set()
for name, q in all_qs:
    n = q["number"]
    seen.add(n)
    if OFFICIAL.get(n) != q["answer"]:
        issues.append(f"[正答] Q{n}: answer={q['answer']} 公式={OFFICIAL.get(n)}")

missing_q = set(OFFICIAL) - seen
if missing_q:
    issues.append(f"[欠落] 問題が存在しない: {sorted(missing_q)}")

# ---- 2. choiceAnalysis の「正解」位置が answer と一致するか ----
for name, q in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    correct_marks = [i + 1 for i, t in enumerate(ca) if "正解" in t and "誤答" not in t]
    if q["answer"] not in correct_marks:
        issues.append(f"[解説] Q{n}: 正解マークが選択肢{correct_marks}にあるが answer={q['answer']}")
    if len(correct_marks) != 1:
        issues.append(f"[解説] Q{n}: 「正解」表記が{len(correct_marks)}箇所 {correct_marks}")
    # ✅マークの位置チェック（使用している場合）
    checks = [i + 1 for i, t in enumerate(ca) if t.lstrip().startswith("✅")]
    if checks and checks != [q["answer"]]:
        issues.append(f"[解説] Q{n}: ✅位置={checks} answer={q['answer']}")

# ---- 3. choices と choiceTranslations の整合 ----
for name, q in all_qs:
    n = q["number"]
    if len(q.get("choices", [])) != 4:
        issues.append(f"[選択肢] Q{n}: choices数")
    if len(q.get("choiceTranslations", [])) != 4:
        issues.append(f"[選択肢] Q{n}: choiceTranslations数")

# ---- 4. 原本（gen_pre2plus_2026-1.py の data 定義）と sections の本文・選択肢一致 ----
import ast

src = open(os.path.join(BASE, "gen_pre2plus_2026-1.py"), encoding="utf-8").read()
tree = ast.parse(src)
orig = None
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "data":
        orig = ast.literal_eval(node.value)
        break
if orig is None:
    issues.append("[原本] gen_pre2plus_2026-1.py から data 定義を抽出できない")
    orig = {"passages": []}
old = {p["id"]: p for p in orig.get("passages", [])}

def norm(s):
    s = re.sub(r"\(\s*\d*\s*\)", "( )", s)  # 空所表記を統一
    return re.sub(r"\s+", " ", s).strip()

# 大問1: 旧 id="1"
if "1" in old:
    old_qs = {int(q["number"]): q for q in old["1"]["questions"]}
    sec1 = d["sections"][0]
    for q in sec1["questions"]:
        n = q["number"]
        oq = old_qs.get(n)
        if not oq:
            issues.append(f"[原本] Q{n}: 旧データに存在しない")
            continue
        if norm(q["text"]) != norm(oq["text"]):
            issues.append(f"[原本] Q{n}: 問題文が原本と不一致")
        if q["choices"] != oq["options"]:
            issues.append(f"[原本] Q{n}: 選択肢が原本と不一致 {q['choices']} vs {oq['options']}")
        if q["answer"] != int(oq["answer"]):
            issues.append(f"[原本] Q{n}: answerが原本と不一致")

# 大問2: 旧 2A/2B の本文と選択肢
for old_id, pa_idx in (("2A", 0), ("2B", 1)):
    if old_id not in old:
        continue
    op = old[old_id]
    np_ = d["sections"][1]["passages"][pa_idx]
    if norm(op["content"]["body"]) != norm(" ".join(np_["paragraphs"])):
        issues.append(f"[原本] 大問2{op['id'][-1]}: 本文が原本と不一致")
    if op["content"]["title"] != np_["title"]:
        warns.append(f"[原本] 大問2: title {op['content']['title']} vs {np_['title']}")
    old_qs = {int(q["number"]): q for q in op["questions"]}
    for q in np_["questions"]:
        oq = old_qs.get(q["number"])
        if oq and q["choices"] != oq["options"]:
            issues.append(f"[原本] Q{q['number']}: 選択肢が原本と不一致")

# 大問3: 旧 3A/3B
for old_id, pa_idx in (("3A", 0), ("3B", 1)):
    if old_id not in old:
        continue
    op = old[old_id]
    np_ = d["sections"][2]["passages"][pa_idx]
    old_qs = {int(q["number"]): q for q in op["questions"]}
    for q in np_["questions"]:
        oq = old_qs.get(q["number"])
        if not oq:
            issues.append(f"[原本] Q{q['number']}: 旧データに存在しない")
            continue
        if q["choices"] != oq["options"]:
            issues.append(f"[原本] Q{q['number']}: 選択肢が原本と不一致")
        if norm(q["question"]) != norm(oq["text"]):
            issues.append(f"[原本] Q{q['number']}: 設問文が原本と不一致\n    new: {q['question']}\n    old: {oq['text']}")
    # 本文一致（3Aはメールヘッダ除去して比較）
    body = op["content"]["body"]
    if old_id == "3A":
        body = re.sub(r"^From:.*?\nDear Cooper,\n", "", body, flags=re.S)
        new_text = " ".join(np_["paragraphs"][1:-1])  # Dear Cooper, と署名を除く
        if norm(body.replace("\nThank you,\nEmma Lawrence", "")) != norm(new_text):
            issues.append("[原本] 大問3A: 本文が原本と不一致")
    else:
        if norm(body) != norm(" ".join(np_["paragraphs"])):
            issues.append("[原本] 大問3B: 本文が原本と不一致")

# ---- 5. paragraphs / translations / sentencePairs ----
for sec in d["sections"][1:]:
    for p in sec.get("passages", []):
        if len(p["paragraphs"]) != len(p["translations"]):
            issues.append(f"[構造] {p['title']}: paragraphs/translations数の不一致")
        text = " ".join(p["paragraphs"])
        for pair in p.get("sentencePairs", []):
            if pair[0] not in text:
                issues.append(f"[構造] {p['title']}: sentencePair本文不一致: {pair[0][:50]}")

# ---- 6. vocabulary 音声ファイルの実在 ----
adir = os.path.join(BASE, "data", "grade-pre2plus", "2026-1-sat")
for v in d.get("vocabulary", []):
    for key in ("wordAudio", "exampleAudio"):
        rel = v.get(key)
        if not rel:
            warns.append(f"[音声] {v['word']}: {key} 未設定")
            continue
        fp = os.path.join(adir, rel.replace("/", os.sep))
        if not os.path.exists(fp) or os.path.getsize(fp) < 500:
            issues.append(f"[音声] {v['word']}: {rel} が存在しないか壊れている")

# ---- 7. lessonPlan 音声と highlightPatterns ----
all_text = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        all_text += q.get("text", "") + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p.get("paragraphs", [])) + " "

for fp_ in d.get("lessonPlan", {}).get("focusPoints", []):
    pp = fp_.get("practicePassage", {})
    af = pp.get("audioFile")
    if af:
        fpth = os.path.join(adir, af.replace("/", os.sep))
        if not os.path.exists(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fp_['id']}: {af} が存在しない")
    for pat in fp_.get("highlightPatterns", []):
        if pat not in all_text:
            issues.append(f"[FP] {fp_['id']}: パターン本文不一致: {pat[:50]}")

# ---- 8. 解説品質（英文エビデンス・sourceEvidence・単調さ）----
import re
from collections import Counter

MONOTONY = {"と矛盾": 10, "意味が通らない": 6, "不自然": 12, "正反対": 6, "記述はない": 6}
phrase_counts = Counter()


def has_english_evidence(text):
    if re.search(r"[（(][^）)]*[A-Za-z]{3,}[^）)]*[）)]", text):
        return True
    if re.search(r"[A-Za-z]{3,}(?:\s+[A-Za-z]{2,})+", text):
        return True
    if re.search(r"^[✅❌]\s*[A-Za-z]", text):
        return True
    return False


for name, q in all_qs:
    n = q["number"]
    if n >= 18 and not q.get("sourceEvidence"):
        issues.append(f"[根拠] Q{n}: sourceEvidence未設定")
    corpus = ""
    for sec in d["sections"]:
        for p in sec.get("passages", []):
            if q in p.get("questions", []):
                corpus = " ".join(p["paragraphs"])
    if n >= 18:
        for phrase in q.get("sourceEvidence", []):
            if corpus and phrase not in corpus:
                issues.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:50]}")
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            issues.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")
        for ph in MONOTONY:
            if ph in ca:
                phrase_counts[ph] += 1

for ph, limit in MONOTONY.items():
    if phrase_counts[ph] > limit:
        warns.append(f"[単調] 「{ph}」が{phrase_counts[ph]}回（推奨上限{limit}）")

# ---- 9. トップレベル構造 ----
print("=== トップレベルキー ===")
print(" ", list(d.keys()))
print()

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
