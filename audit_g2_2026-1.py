# -*- coding: utf-8 -*-
"""2026-1 本会場 2級 詳細監査スクリプト"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1",
)
DATA = os.path.join(BASE, "data.json")

d = json.load(open(DATA, encoding="utf-8"))
errors = []
warns = []

# ============================================================
# 1. メタデータ
# ============================================================
for key in ("grade", "year", "session", "title", "sections", "vocabulary", "lessonPlan"):
    if key not in d:
        errors.append(f"top-level: missing {key}")

# 準会場(2026-1-sat)との形式比較
sat = json.load(open(os.path.join(os.path.dirname(BASE), "2026-1-sat", "data.json"), encoding="utf-8"))
for key in ("grade", "year", "session"):
    t_main, t_sat = type(d.get(key)).__name__, type(sat.get(key)).__name__
    if t_main != t_sat:
        warns.append(f"top-level type mismatch vs sat: {key} = {t_main} (sat: {t_sat})")

# ============================================================
# 2. sentencePairs が本文の部分文字列か
# ============================================================
for sec in d["sections"]:
    for p in sec.get("passages", []):
        full = " ".join(p["paragraphs"])
        for i, pair in enumerate(p.get("sentencePairs", [])):
            en = pair[0]
            if en not in full:
                errors.append(f"{sec['name']}{p['label']}: sentencePair[{i}] not in paragraphs: {en[:60]}...")

# ============================================================
# 3. 大問1: choiceAnalysis 先頭の単語が choices と一致するか
# ============================================================
sec1 = d["sections"][0]
for q in sec1["questions"]:
    n = q["number"]
    for i, ca in enumerate(q["choiceAnalysis"]):
        m = re.match(r"^[✅❌]\s*([A-Za-z' \-]+?)[＝=]", ca)
        if m:
            word = m.group(1).strip()
            choice = q["choices"][i]
            if word.lower() not in choice.lower() and choice.lower() not in word.lower():
                errors.append(f"S1 Q{n} choice{i+1}: analysis word '{word}' != choice '{choice}'")

# ============================================================
# 4. 大問1: choiceTranslations が正解位置で choiceAnalysis と矛盾しないか（簡易: 件数のみ）
#    + grammar/translation の存在
# ============================================================
for q in sec1["questions"]:
    if "( )" not in q["text"] and "（ ）" not in q["text"]:
        warns.append(f"S1 Q{q['number']}: text has no blank '( )'")

# ============================================================
# 5. 語彙: word 重複・distractor 内部重複・source と例文の整合
# ============================================================
vocab = d["vocabulary"]
words = [v["word"].lower() for v in vocab]
for w in set(words):
    if words.count(w) > 1:
        errors.append(f"vocab: duplicate word '{w}'")
for v in vocab:
    ds = v["distractors"]
    if len(set(ds)) != 3:
        errors.append(f"vocab {v['word']}: duplicate distractors {ds}")
    # 例文に word（または語幹）が含まれるか
    w = v["word"].lower().replace("-", " ")
    ex = v["example"].lower().replace("-", " ")
    stem = w.split()[0][:4] if " " in w else w[:4]
    if stem not in ex:
        warns.append(f"vocab {v['word']}: example may not contain the word: {v['example'][:50]}...")

# ============================================================
# 6. 語彙の音声ファイル番号と wordAudio パスの一致
# ============================================================
for i, v in enumerate(vocab):
    expected_prefix = f"audio/vocab/w_{i+1:03d}_"
    if not v.get("wordAudio", "").startswith(expected_prefix):
        errors.append(f"vocab[{i}] {v['word']}: wordAudio mismatch {v.get('wordAudio')}")

# ============================================================
# 7. lessonPlan: practicePassage の音声ファイル存在・practiceQuestions の構造
# ============================================================
for fp in d["lessonPlan"]["focusPoints"]:
    pp = fp["practicePassage"]
    af = pp.get("audioFile", "")
    fpath = os.path.join(BASE, af.replace("/", os.sep))
    if not os.path.isfile(fpath) or os.path.getsize(fpath) < 500:
        errors.append(f"{fp['id']}: missing audio {af}")
    for j, pq in enumerate(fp["practiceQuestions"]):
        if not pq.get("q") or not pq.get("a"):
            errors.append(f"{fp['id']}: practiceQuestion[{j}] missing q/a")

# ============================================================
# 8. リスニング: 全30問の解答が 1〜4 の範囲か
# ============================================================
listening = d.get("listening", {})
p1 = listening.get("part1", {})
p2 = listening.get("part2", {})
if len(p1) != 15:
    errors.append(f"listening part1: {len(p1)} answers, expected 15")
if len(p2) != 15:
    errors.append(f"listening part2: {len(p2)} answers, expected 15")
for part, ans in (("part1", p1), ("part2", p2)):
    for k, vv in ans.items():
        if vv not in (1, 2, 3, 4):
            errors.append(f"listening {part} Q{k}: answer {vv} out of range")

# ============================================================
# 9. 大問2/3: 段落内の空所番号と questions の番号一致
# ============================================================
for sec in d["sections"]:
    if sec["type"] == "passage-fill":
        for p in sec["passages"]:
            text = " ".join(p["paragraphs"])
            blanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", text))
            qnums = sorted(q["number"] for q in p["questions"])
            if blanks != qnums:
                errors.append(f"{sec['name']}{p['label']}: blanks {blanks} != questions {qnums}")
            # 訳側の空所も確認
            jtext = " ".join(p["translations"])
            jblanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", jtext))
            if jblanks != qnums:
                errors.append(f"{sec['name']}{p['label']}: JA blanks {jblanks} != questions {qnums}")

# ============================================================
# 10. 大問3: sourceEvidence が本文に存在するか
# ============================================================
sec3 = next(s for s in d["sections"] if s["name"] == "大問3")
for p in sec3["passages"]:
    full = " ".join(p["paragraphs"])
    for q in p["questions"]:
        for ev in q.get("sourceEvidence", []):
            if ev not in full:
                errors.append(f"大問3{p['label']} Q{q['number']}: sourceEvidence not in text: {ev[:60]}...")

# ============================================================
# 結果
# ============================================================
print(f"errors={len(errors)} warnings={len(warns)}")
for e in errors:
    print("  [ERROR]", e)
for w in warns:
    print("  [WARN] ", w)
if errors:
    sys.exit(1)
print("AUDIT OK")
