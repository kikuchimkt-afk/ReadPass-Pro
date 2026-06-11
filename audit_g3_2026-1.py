# -*- coding: utf-8 -*-
"""2026-1-sat 3級 総合監査 — 公式解答・原本・解説・音声・FP"""
import ast
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade3", "2026-1-sat", "data.json")
ADIR = os.path.join(BASE, "data", "grade3", "2026-1-sat")

OFFICIAL_READING = {
    1: 2, 2: 4, 3: 1, 4: 4, 5: 1, 6: 4, 7: 3, 8: 4, 9: 4, 10: 4,
    11: 3, 12: 4, 13: 3, 14: 3, 15: 2,
    16: 3, 17: 3, 18: 3, 19: 1, 20: 2,
    21: 3, 22: 1, 23: 1, 24: 4, 25: 3,
    26: 3, 27: 1, 28: 2, 29: 3, 30: 4,
}

OFFICIAL_LISTENING = {
    "part1": {1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 6: 1, 7: 2, 8: 3, 9: 3, 10: 3},
    "part2": {11: 1, 12: 4, 13: 1, 14: 4, 15: 4, 16: 2, 17: 3, 18: 3, 19: 1, 20: 3},
    "part3": {21: 2, 22: 1, 23: 4, 24: 1, 25: 4, 26: 1, 27: 2, 28: 1, 29: 2, 30: 2},
}

d = json.load(open(DATA_PATH, encoding="utf-8"))
issues = []
warns = []


def norm(s):
    s = re.sub(r"[（(]\s*[　\s]*\s*[)）]", "( )", s or "")
    return re.sub(r"\s+", " ", s).strip()


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((sec["name"], q))
        for p in sec.get("passages", []):
            for q in p.get("questions", []):
                out.append((sec["name"], q))
    return out


all_qs = collect_questions(d)
seen = {q["number"] for _, q in all_qs}

# ---- 1. 正答 ----
for n, ans in OFFICIAL_READING.items():
    if n not in seen:
        issues.append(f"[正答] Q{n}: 問題欠落")
for _, q in all_qs:
    n = q["number"]
    if OFFICIAL_READING.get(n) != q.get("answer"):
        issues.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL_READING.get(n)}")

# ---- 2. リスニング正答 ----
for part, expected in OFFICIAL_LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for k, v in expected.items():
        key = str(k)
        if got.get(key) != v and got.get(k) != v:
            issues.append(f"[リスニング] {part} Q{k}: {got.get(key, got.get(k))} != {v}")

# ---- 3. 大問1・2 リッチフィールド ----
for sec_name in ("大問1", "大問2"):
    sec = next(s for s in d["sections"] if s["name"] == sec_name)
    for q in sec["questions"]:
        n = q["number"]
        for key in ("grammar", "grammarSimple", "translation", "choiceTranslations",
                    "choiceAnalysis", "choiceAnalysisSimple"):
            if not q.get(key):
                issues.append(f"[解説] Q{n}: missing {key}")
        ca = q.get("choiceAnalysis", [])
        if len(ca) != 4:
            issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        else:
            marks = [i + 1 for i, t in enumerate(ca) if t.startswith("○")]
            if marks != [q["answer"]]:
                issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")

# ---- 4. 大問3 リッチフィールド ----
for p in d["sections"][2]["passages"]:
    if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
        issues.append(f"[構造] 3{p['label']}: paragraphs/translations不一致")
    corpus = " ".join(p.get("paragraphs", []))
    for em in p.get("emails", []):
        corpus += " " + em.get("body", "")
    for q in p.get("questions", []):
        n = q["number"]
        for key in ("questionTranslation", "grammar", "grammarSimple",
                    "choiceAnalysis", "choiceAnalysisSimple", "choiceTranslations"):
            if not q.get(key):
                issues.append(f"[解説] Q{n}: missing {key}")
        ev = q.get("sourceEvidence", "")
        if ev and ev not in corpus:
            issues.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {ev[:60]}")
        marks = [i + 1 for i, t in enumerate(q.get("choiceAnalysis", [])) if t.startswith("○")]
        if marks and marks != [q["answer"]]:
            issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")
        smarks = [i + 1 for i, t in enumerate(q.get("choiceAnalysisSimple", [])) if t.startswith("○")]
        if smarks and smarks != [q["answer"]]:
            issues.append(f"[解説] Q{n}: ○(簡易)位置={smarks} answer={q['answer']}")
        if not q.get("sourceEvidence"):
            warns.append(f"[根拠] Q{n}: sourceEvidence未設定")

# ---- 5. 原本 gen_g3_2026-1.py との一致 ----
src = open(os.path.join(BASE, "gen_g3_2026-1.py"), encoding="utf-8").read()
tree = ast.parse(src)
orig_sections = None
for node in tree.body:
    if isinstance(node, ast.Assign) and node.targets[0].id == "section1_questions":
        s1 = ast.literal_eval(node.value)
    if isinstance(node, ast.Assign) and node.targets[0].id == "section2_questions":
        s2 = ast.literal_eval(node.value)
    if isinstance(node, ast.Assign) and node.targets[0].id == "passage_3a":
        p3a = ast.literal_eval(node.value)
    if isinstance(node, ast.Assign) and node.targets[0].id == "passage_3b":
        p3b = ast.literal_eval(node.value)
    if isinstance(node, ast.Assign) and node.targets[0].id == "passage_3c":
        p3c = ast.literal_eval(node.value)

orig_map = {}
for q in s1:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for q in s2:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for pa in (p3a, p3b, p3c):
    for q in pa["questions"]:
        orig_map[q["number"]] = ("question", q["question"], q["choices"])

for _, q in all_qs:
    n = q["number"]
    if n not in orig_map:
        continue
    kind, text, choices = orig_map[n]
    new_text = q.get(kind, q.get("text", q.get("question", "")))
    if norm(new_text) != norm(text):
        issues.append(f"[原本] Q{n}: 問題文不一致")
    if q["choices"] != choices:
        issues.append(f"[原本] Q{n}: 選択肢不一致")

# ---- 6. vocabulary ----
vocab = d.get("vocabulary", [])
if len(vocab) != 30:
    issues.append(f"[語彙] count={len(vocab)} != 30")
meanings = []
for i, v in enumerate(vocab):
    m = v.get("meaning", "")
    if m in meanings:
        issues.append(f"[語彙] 意味重複: {m}")
    meanings.append(m)
    if m in v.get("distractors", []):
        issues.append(f"[語彙] {v['word']}: distractorsに正解意味")
    rel = v.get("wordAudio", "")
    if rel:
        fp = os.path.join(ADIR, rel.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            issues.append(f"[音声] vocab {v['word']}: {rel}")

# ---- 7. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "
        for em in p.get("emails", []):
            corpus_all += em.get("body", "") + " "

fps = d.get("lessonPlan", {}).get("focusPoints", [])
if len(fps) != 4:
    issues.append(f"[FP] count={len(fps)} != 4")

for fp in fps:
    fid = fp.get("id", "?")
    pp = fp.get("practicePassage", {})
    pp_text = pp.get("en", "")
    search = corpus_all + " " + pp_text
    for pat in fp.get("highlightPatterns", []):
        if pat not in search:
            issues.append(f"[FP] {fid}: highlight不在: {pat[:50]}")
    af = pp.get("audioFile")
    if af:
        fpth = os.path.join(ADIR, af.replace("/", os.sep))
        if not os.path.isfile(fpth):
            issues.append(f"[音声] {fid}: {af}")
    for j, ex in enumerate(fp.get("examples", [])):
        au = ex.get("audio")
        if au:
            fpth = os.path.join(ADIR, au.replace("/", os.sep))
            if not os.path.isfile(fpth):
                issues.append(f"[音声] {fid} ex{j+1}: {au}")

# ---- 8. トップレベル・キー順 ----
EXPECTED_KEYS = (
    "grade", "year", "session", "title", "exam",
    "sections", "writing", "listening", "vocabulary", "lessonPlan",
)
for bad in ("id", "name", "passages"):
    if bad in d:
        issues.append(f"[構造] トップレベルに不要キー: {bad}")
for key in EXPECTED_KEYS:
    if key not in d:
        issues.append(f"[構造] missing top-level {key}")
if list(d.keys())[: len(EXPECTED_KEYS)] != list(EXPECTED_KEYS):
    warns.append(f"[構造] キー順が標準と異なる: {list(d.keys())}")

# ---- 9. メール和訳 ----
p3b = d["sections"][2]["passages"][1]
for em in p3b.get("emails", []):
    if not em.get("translation"):
        issues.append("[構造] 3B email: translation欠落")

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
sys.exit(1 if issues else 0)
