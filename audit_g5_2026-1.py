# -*- coding: utf-8 -*-
"""2026-1-sat 5級 総合監査 — 公式解答・原本・解説・音声・語彙・FP"""
import ast
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "grade5", "2026-1-sat", "data.json")
ADIR = os.path.join(BASE, "data", "grade5", "2026-1-sat")

OFFICIAL_READING = {
    1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 1, 10: 1,
    11: 3, 12: 1, 13: 3, 14: 3, 15: 3,
    16: 1, 17: 3, 18: 1, 19: 3, 20: 3,
    21: 4, 22: 4, 23: 3, 24: 3, 25: 4,
}

OFFICIAL_LISTENING = {
    "part1": {1: 2, 2: 3, 3: 1, 4: 1, 5: 2, 6: 3, 7: 2, 8: 1, 9: 3, 10: 3},
    "part2": {11: 2, 12: 1, 13: 3, 14: 3, 15: 1},
    "part3": {
        16: 2, 17: 1, 18: 1, 19: 2, 20: 3,
        21: 1, 22: 1, 23: 2, 24: 2, 25: 1,
    },
}

d = json.load(open(DATA_PATH, encoding="utf-8"))
issues = []
warns = []


def norm(s):
    s = re.sub(r"[（(]\s*[　\s]*\s*[)）]", "( )", s or "")
    return re.sub(r"\s+", " ", s).strip()


def norm_choice(s):
    return re.sub(r"\s+", "", s.replace("─", "−").replace("–", "−").replace("-", "−"))


def collect_questions(data):
    out = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            out.append((sec["name"], sec.get("type"), q))
    return out


def audio_ok(rel):
    if not rel:
        return False
    fp = os.path.join(ADIR, rel.replace("/", os.sep))
    return os.path.isfile(fp) and os.path.getsize(fp) >= 500


def build_sentence(q):
    words = q.get("words", [])
    order = q.get("correctOrder", [])
    if not words or len(words) != len(order):
        return ""
    ordered = [words[i - 1] for i in order]
    prefix = (q.get("framePrefix") or "").strip()
    suffix = (q.get("frameSuffix") or "").strip()
    parts = []
    if prefix:
        parts.append(prefix)
    parts.extend(ordered)
    sentence = " ".join(parts)
    if suffix:
        if suffix.startswith((".", "?", "!")):
            sentence += suffix
        else:
            sentence += " " + suffix
    sentence = sentence.strip()
    if sentence and not prefix:
        sentence = sentence[0].upper() + sentence[1:]
    return sentence


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
        ct = q.get("choiceTranslations", [])
        if len(ct) != 4:
            issues.append(f"[解説] Q{n}: choiceTranslations数={len(ct)}")
        if not audio_ok(q.get("questionAudio")):
            issues.append(f"[音声] Q{n}: {q.get('questionAudio')}")

# ---- 4. 大問3 並べ替え ----
sec3 = next(s for s in d["sections"] if s["name"] == "大問3")
if sec3.get("type") != "sentence-order":
    issues.append(f"[構造] 大問3 type={sec3.get('type')}")
EXPECTED_SENTENCES = {
    21: "My sister washes the dishes every day.",
    22: "Bill and I go skiing in winter.",
    23: "Take your umbrella to school.",
    24: "Mike's soccer team has three coaches.",
    25: "We don't have school today.",
}
for q in sec3["questions"]:
    n = q["number"]
    for key in ("grammar", "grammarSimple", "choiceAnalysis", "choiceAnalysisSimple",
                "words", "correctOrder", "answerSlots", "questionAudio"):
        if key not in q:
            issues.append(f"[解説] Q{n}: missing {key}")
    if q.get("answerSlots") != [1, 3]:
        issues.append(f"[並べ替え] Q{n}: answerSlots={q.get('answerSlots')}")
    if len(q.get("words", [])) != 4:
        issues.append(f"[並べ替え] Q{n}: words数={len(q.get('words', []))}")
    marks = [i + 1 for i, t in enumerate(q.get("choiceAnalysis", [])) if t.startswith("○")]
    if marks and marks != [q["answer"]]:
        issues.append(f"[解説] Q{n}: ○位置={marks} answer={q['answer']}")
    slots = q.get("answerSlots", [])
    order = q.get("correctOrder", [])
    if len(slots) == 2 and len(order) == 4:
        circled = lambda i: chr(0x2460 + i - 1)
        expected_label = f"{circled(order[slots[0] - 1])}−{circled(order[slots[1] - 1])}"
        actual = norm_choice(q["choices"][q["answer"] - 1])
        if actual != expected_label:
            issues.append(f"[並べ替え] Q{n}: {q['choices'][q['answer'] - 1]} != {expected_label}")
    built = build_sentence(q)
    exp_sent = EXPECTED_SENTENCES.get(n, "")
    if built != exp_sent:
        issues.append(f"[並べ替え] Q{n}: 完成文「{built}」!= 期待「{exp_sent}」")
    if not audio_ok(q.get("questionAudio")):
        issues.append(f"[音声] Q{n}: {q.get('questionAudio')}")

# ---- 5. 原本 gen_g5_2026-1.py との一致 ----
src = open(os.path.join(BASE, "gen_g5_2026-1.py"), encoding="utf-8").read()
tree = ast.parse(src)
s1 = s2 = s3 = None
for node in tree.body:
    if isinstance(node, ast.Assign):
        tid = getattr(node.targets[0], "id", "")
        if tid == "section1_questions":
            s1 = ast.literal_eval(node.value)
        elif tid == "section2_questions":
            s2 = ast.literal_eval(node.value)
        elif tid == "section3_questions":
            s3 = ast.literal_eval(node.value)

orig_map = {}
for q in s1:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for q in s2:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])
for q in s3:
    orig_map[q["number"]] = ("text", q["text"], q["choices"])

for _, _, q in all_qs:
    n = q["number"]
    if n not in orig_map:
        continue
    kind, text, choices = orig_map[n]
    new_text = q.get(kind, q.get("text", ""))
    if norm(new_text) != norm(text):
        issues.append(f"[原本] Q{n}: 問題文不一致")
    if q["choices"] != choices:
        issues.append(f"[原本] Q{n}: 選択肢不一致")

# ---- 6. vocabulary ----
vocab = d.get("vocabulary", [])
if len(vocab) != 20:
    issues.append(f"[語彙] count={len(vocab)} != 20")
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

# ---- 7. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
        if q.get("words"):
            corpus_all += " ".join(q["words"]) + " "

fps = d.get("lessonPlan", {}).get("focusPoints", [])
if len(fps) != 3:
    issues.append(f"[FP] count={len(fps)} != 3")

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
    af = pp.get("audioFile")
    if af and not audio_ok(af):
        issues.append(f"[音声] {fid}: {af}")
    for j, ex in enumerate(fp.get("examples", [])):
        au = ex.get("audio")
        if au and not audio_ok(au):
            issues.append(f"[音声] {fid} ex{j+1}: {au}")
    sq = fp.get("sourceQuoteAudio")
    if sq and not audio_ok(sq):
        issues.append(f"[音声] {fid} sourceQuote: {sq}")

# ---- 8. トップレベル ----
EXPECTED_KEYS = ("grade", "year", "session", "title", "exam", "sections", "listening", "vocabulary", "lessonPlan")
for bad in ("id", "name", "passages"):
    if bad in d:
        issues.append(f"[構造] トップレベルに不要キー: {bad}")
for key in EXPECTED_KEYS:
    if key not in d:
        issues.append(f"[構造] missing top-level {key}")

if d.get("grade") != "grade5":
    issues.append(f"[構造] grade={d.get('grade')}")
if d.get("exam") != "2026-1-sat":
    issues.append(f"[構造] exam={d.get('exam')}")

# ---- 9. 問題数・連番 ----
if len(all_qs) != 25:
    issues.append(f"[構造] 問題数={len(all_qs)} != 25")
nums = sorted(q["number"] for _, _, q in all_qs)
if nums != list(range(1, 26)):
    issues.append(f"[構造] 問番号連番不正: {nums}")

# ---- 10. 音声ファイル総数 ----
audio_dir = os.path.join(ADIR, "audio")
mp3_count = 0
tiny = []
for root, _, files in os.walk(audio_dir):
    for f in files:
        if f.endswith(".mp3"):
            mp3_count += 1
            fp = os.path.join(root, f)
            if os.path.getsize(fp) < 500:
                tiny.append(fp)
if mp3_count != 80:
    warns.append(f"[音声] mp3総数={mp3_count} (期待80)")
for fp in tiny:
    issues.append(f"[音声] サイズ不足: {fp}")

print(f"=== 監査結果: issues={len(issues)} warns={len(warns)} ===")
for e in issues:
    print("  [NG]", e)
for w in warns:
    print("  [警告]", w)
if not issues and not warns:
    print("  問題なし")
sys.exit(1 if issues else 0)
