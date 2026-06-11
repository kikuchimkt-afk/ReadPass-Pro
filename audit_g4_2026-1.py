# -*- coding: utf-8 -*-
"""2026-1-sat 4級 総合監査 — 公式解答・原本・解説・音声・語彙・FP"""
import ast
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade4", "2026-1-sat", "data.json")
ADIR = os.path.join(BASE, "data", "grade4", "2026-1-sat")

OFFICIAL_READING = {
    1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 3, 10: 3,
    11: 3, 12: 1, 13: 2, 14: 4, 15: 1,
    16: 2, 17: 2, 18: 1, 19: 4, 20: 3,
    21: 1, 22: 1, 23: 3, 24: 4, 25: 2,
    26: 3, 27: 4, 28: 4, 29: 1, 30: 2,
    31: 2, 32: 2, 33: 1, 34: 4, 35: 4,
}

OFFICIAL_LISTENING = {
    "part1": {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 1, 10: 2},
    "part2": {11: 4, 12: 3, 13: 4, 14: 2, 15: 4, 16: 3, 17: 3, 18: 4, 19: 1, 20: 2},
    "part3": {21: 1, 22: 3, 23: 1, 24: 1, 25: 1, 26: 3, 27: 3, 28: 3, 29: 2, 30: 3},
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
            out.append((sec["name"], sec.get("type"), q))
        for p in sec.get("passages", []):
            for q in p.get("questions", []):
                out.append((sec["name"], sec.get("type"), q))
    return out


def audio_ok(rel):
    if not rel:
        return False
    fp = os.path.join(ADIR, rel.replace("/", os.sep))
    return os.path.isfile(fp) and os.path.getsize(fp) >= 500


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q in all_qs}

# ---- 1. 正答 ----
for n, ans in OFFICIAL_READING.items():
    if n not in seen:
        issues.append(f"[正答] Q{n}: 問題欠落")
for _, _, q in all_qs:
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
                    "choiceAnalysis", "choiceAnalysisSimple", "questionAudio"):
            if not q.get(key):
                issues.append(f"[解説] Q{n}: missing {key}")
        ca = q.get("choiceAnalysis", [])
        if len(ca) != 4:
            issues.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        else:
            marks = [i + 1 for i, t in enumerate(ca) if t.startswith("○")]
            if marks != [q["answer"]]:
                issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")
        if not audio_ok(q.get("questionAudio")):
            issues.append(f"[音声] Q{n}: {q.get('questionAudio')}")

# ---- 4. 大問3 並べ替え ----
sec3 = next(s for s in d["sections"] if s["name"] == "大問3")
if sec3.get("type") != "sentence-order":
    issues.append(f"[構造] 大問3 type={sec3.get('type')}")
for q in sec3["questions"]:
    n = q["number"]
    for key in ("grammar", "grammarSimple", "choiceAnalysis", "choiceAnalysisSimple",
                "words", "correctOrder", "answerSlots", "questionAudio"):
        if not q.get(key):
            issues.append(f"[解説] Q{n}: missing {key}")
    marks = [i + 1 for i, t in enumerate(q.get("choiceAnalysis", [])) if t.startswith("○")]
    if marks and marks != [q["answer"]]:
        issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")
    slots = q.get("answerSlots", [])
    order = q.get("correctOrder", [])
    words = q.get("words", [])
    if len(slots) == 2 and len(order) == 5:
        circled = lambda i: chr(0x2460 + i - 1)
        expected_label = f"{circled(order[slots[0] - 1])}−{circled(order[slots[1] - 1])}"
        actual = q["choices"][q["answer"] - 1]
        if actual != expected_label:
            issues.append(f"[並べ替え] Q{n}: {actual} != {expected_label}")
    if not audio_ok(q.get("questionAudio")):
        issues.append(f"[音声] Q{n}: {q.get('questionAudio')}")

# ---- 5. 大問4 読解 ----
sec4 = next(s for s in d["sections"] if s["name"] == "大問4")
for pa in sec4.get("passages", []):
    if len(pa.get("paragraphs", [])) != len(pa.get("translations", [])):
        issues.append(f"[構造] 4{pa['label']}: paragraphs/translations不一致")
    corpus = " ".join(pa.get("paragraphs", []))
    for q in pa.get("questions", []):
        n = q["number"]
        for key in ("question", "questionTranslation", "grammar", "grammarSimple",
                    "choiceAnalysis", "choiceAnalysisSimple", "choiceTranslations",
                    "questionAudio"):
            if not q.get(key):
                issues.append(f"[解説] Q{n}: missing {key}")
        marks = [i + 1 for i, t in enumerate(q.get("choiceAnalysis", [])) if t.startswith("○")]
        if marks and marks != [q["answer"]]:
            issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")
        if not audio_ok(q.get("questionAudio")):
            issues.append(f"[音声] Q{n}: {q.get('questionAudio')}")

# ---- 6. 原本 gen_g4_2026-1.py との一致 ----
src = open(os.path.join(BASE, "gen_g4_2026-1.py"), encoding="utf-8").read()
tree = ast.parse(src)
s1 = s2 = s3 = None
p4a = p4b = p4c = None
for node in tree.body:
    if isinstance(node, ast.Assign):
        tid = getattr(node.targets[0], "id", "")
        if tid == "section1_questions":
            s1 = ast.literal_eval(node.value)
        elif tid == "section2_questions":
            s2 = ast.literal_eval(node.value)
        elif tid == "section3_questions":
            s3 = ast.literal_eval(node.value)
        elif tid == "passage_4a":
            p4a = ast.literal_eval(node.value)
        elif tid == "passage_4b":
            p4b = ast.literal_eval(node.value)
        elif tid == "passage_4c":
            p4c = ast.literal_eval(node.value)

orig_map = {}
for q in s1:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for q in s2:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for q in s3:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for pa in (p4a, p4b, p4c):
    for q in pa["questions"]:
        orig_map[q["number"]] = ("question", q["question"], q["choices"])

for _, _, q in all_qs:
    n = q["number"]
    if n not in orig_map:
        continue
    kind, text, choices = orig_map[n]
    new_text = q.get(kind, q.get("text", q.get("question", "")))
    if norm(new_text) != norm(text):
        issues.append(f"[原本] Q{n}: 問題文不一致")
    if q["choices"] != choices:
        issues.append(f"[原本] Q{n}: 選択肢不一致")

# ---- 7. vocabulary ----
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
    for rel in (v.get("wordAudio"), v.get("exampleAudio")):
        if rel and not audio_ok(rel):
            issues.append(f"[音声] vocab {v['word']}: {rel}")

# ---- 8. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "

fps = d.get("lessonPlan", {}).get("focusPoints", [])
if len(fps) != 4:
    issues.append(f"[FP] count={len(fps)} != 4")

for fp in fps:
    fid = fp.get("id", "?")
    if not fp.get("highlightColor") or not fp.get("highlightLabel"):
        warns.append(f"[FP] {fid}: highlightColor/Label未設定")
    if not fp.get("explanationSimple"):
        issues.append(f"[FP] {fid}: explanationSimple欠落")
    pp = fp.get("practicePassage", {})
    pp_text = pp.get("en", "")
    if "[出典:" not in pp_text:
        issues.append(f"[FP] {fid}: practicePassageに[出典:]なし")
    search = corpus_all + " " + pp_text
    for pat in fp.get("highlightPatterns", []):
        if pat not in search:
            issues.append(f"[FP] {fid}: highlight不在: {pat[:50]}")
    for af_key in ("audioFile",):
        af = pp.get(af_key)
        if af and not audio_ok(af):
            issues.append(f"[音声] {fid}: {af}")
    for j, ex in enumerate(fp.get("examples", [])):
        au = ex.get("audio")
        if au and not audio_ok(au):
            issues.append(f"[音声] {fid} ex{j+1}: {au}")
    sq = fp.get("sourceQuoteAudio")
    if sq and not audio_ok(sq):
        issues.append(f"[音声] {fid} sourceQuote: {sq}")

# ---- 9. トップレベル ----
EXPECTED_KEYS = ("grade", "year", "session", "title", "exam", "sections", "listening", "vocabulary", "lessonPlan")
for bad in ("id", "name", "passages"):
    if bad in d:
        issues.append(f"[構造] トップレベルに不要キー: {bad}")
for key in EXPECTED_KEYS:
    if key not in d:
        issues.append(f"[構造] missing top-level {key}")

# ---- 10. 選択肢和訳の数 ----
for _, _, q in all_qs:
    n = q["number"]
    ct = q.get("choiceTranslations", [])
    if ct and len(ct) != 4:
        issues.append(f"[選択肢] Q{n}: choiceTranslations数={len(ct)}")

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
sys.exit(1 if issues else 0)
