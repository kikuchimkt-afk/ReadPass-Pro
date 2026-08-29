# -*- coding: utf-8 -*-
"""Verify 2026-1 grade2 (本会場) lessonPlan structure."""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)
DATA_BASE = os.path.dirname(DATA_PATH)

with open(DATA_PATH, encoding="utf-8") as f:
    d = json.load(f)

errors = []
lp = d.get("lessonPlan", {})
fps = lp.get("focusPoints", [])


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()


sentence_pairs = [
    pair
    for section in d.get("sections", [])
    for passage in section.get("passages", [])
    for pair in passage.get("sentencePairs", [])
]
if len(sentence_pairs) != 73:
    errors.append(f"sentencePairs total={len(sentence_pairs)}, expected 73")
for index, pair in enumerate(sentence_pairs, 1):
    if (
        not isinstance(pair, list)
        or len(pair) != 4
        or not all(isinstance(item, str) and item.strip() for item in pair)
    ):
        errors.append(f"sentencePair[{index}] is not 4 nonempty strings")
        continue
    segments = pair[2].split("||")
    if len(segments) < 2 or any(
        segment.count("|") != 1
        or not all(part.strip() for part in segment.split("|", 1))
        for segment in segments
    ):
        errors.append(f"sentencePair[{index}] has invalid slash units")
        continue
    slash_english = " ".join(segment.split("|", 1)[0] for segment in segments)
    if norm(slash_english) != norm(pair[0]):
        errors.append(f"sentencePair[{index}] slash English mismatch")
    if not re.search(
        rf"(?<!\w){re.escape(pair[3])}(?!\w)", pair[0], re.IGNORECASE
    ):
        errors.append(f"sentencePair[{index}] main verb not found")

if len(fps) != 5:
    errors.append(f"focusPoints count = {len(fps)}, expected 5")

all_text = ""
for sec in d.get("sections", []):
    for q in sec.get("questions", []):
        all_text += q.get("text", "") + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p.get("paragraphs", [])) + " "

for i, fp in enumerate(fps):
    exp_id = f"fp{i + 1}"
    if fp.get("id") != exp_id:
        errors.append(f"{exp_id}: id mismatch ({fp.get('id')})")
    for key in (
        "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions",
        "highlightPatterns", "highlightColor", "highlightLabel",
    ):
        if key not in fp or not fp[key]:
            errors.append(f"{exp_id}: missing or empty '{key}'")
    if len(fp.get("examples", [])) < 3:
        errors.append(f"{exp_id}: need >=3 examples")
    pp = fp.get("practicePassage", {})
    if not pp.get("en") or not pp.get("ja"):
        errors.append(f"{exp_id}: practicePassage missing en/ja")
    if "[出典:" not in pp.get("en", ""):
        errors.append(f"{exp_id}: practicePassage missing [出典: ...]")
    audio = pp.get("audioFile", "")
    audio_path = os.path.join(DATA_BASE, audio.replace("/", os.sep))
    if not audio or not os.path.isfile(audio_path) or os.path.getsize(audio_path) < 500:
        errors.append(f"{exp_id}: missing/invalid practice audio {audio}")
    if len(fp.get("practiceQuestions", [])) < 4:
        errors.append(f"{exp_id}: need >=4 practiceQuestions")
    if len(fp.get("highlightPatterns", [])) < 3:
        errors.append(f"{exp_id}: need >=3 highlightPatterns")
    for pat in fp.get("highlightPatterns", []):
        if pat not in all_text:
            errors.append(f"{exp_id}: pattern not in exam text: {pat[:50]}...")

if len(fps) == 5:
    fp1, fp2, fp3, fp4, fp5 = fps
    if "are even fascinated by this feeling が正解" not in fp1["practiceQuestions"][1]["q"]:
        errors.append("fp1: Q22 practice question asks for the wrong answer phrase")
    if not fp1.get("sourceLocation", "").endswith("第1〜3段落"):
        errors.append("fp1: sourceLocation does not cover all referenced paragraphs")
    if "They like scary things and seek excitement" not in fp1["practiceQuestions"][1]["a"]:
        errors.append("fp1: Q22 practice answer lacks the direct evidence sentence")
    if "彼を本当に生きているかのように見せました" not in fp2["examples"][2]["ja"]:
        errors.append("fp2: to bring him to life is missing from example translation")
    if not fp2.get("sourceLocation", "").endswith("第1〜3段落"):
        errors.append("fp2: sourceLocation does not cover Q20 paragraph")
    if "彼を飢えさせないよう" not in fp2["practicePassage"]["ja"]:
        errors.append("fp2: so that he would not starve is missing from translation")
    fp3_answer = fp3["practiceQuestions"][0]["a"]
    if "staff is helpful" not in fp3_answer or "スタッフの親切さは根拠にできない" not in fp3_answer:
        errors.append("fp3: Q24 explanation lacks the precise absent-evidence rationale")
    if "唯一" in fp3_answer:
        errors.append("fp3: Q24 explanation incorrectly calls access the only appeal")
    if "Q30" not in fp4.get("explanation", ""):
        errors.append("fp4: wealthy-background question reference regression")

serialized = json.dumps(lp, ensure_ascii=False)
for stale in (
    "They like scary things and seek excitement が正解になる",
    "唯一の「魅力の理由」",
    "弟の誘い",
    "弟からの新しい場所",
    "恐怖はすぐに脳を反応させ",
    "few access to books",
    "Motivated by this（これに動機づけられて）",
):
    if stale in serialized:
        errors.append(f"lessonPlan stale explanation remains: {stale}")

print(f"lessonPlan focusPoints={len(fps)} errors={len(errors)}")
for e in errors:
    print(" ", e)
if errors:
    sys.exit(1)
print("OK: lessonPlan (5 focusPoints) verified")
