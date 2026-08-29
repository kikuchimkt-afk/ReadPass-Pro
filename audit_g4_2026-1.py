# -*- coding: utf-8 -*-
"""2026-1-sat 4級 総合監査 — 原本固定・公式正答・解説・長文・音声・語彙・FP。"""
import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(REPO, "data", "grade4", "2026-1-sat")
DATA_PATH = os.path.join(DATA_DIR, "data.json")
SOURCE_GEN = os.path.join(REPO, "gen_g4_2026-1.py")

# gen_g4_2026-1.py 内の原本転記フィールドだけを安定化して得た SHA-256。
SOURCE_PAYLOAD_SHA256 = "61bfa859ecd5deb8fb1222b0d267d0c2962c7a1e53c3051a003bc4efb595b055"
SOURCE_PDFS = {
    r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\4級.pdf":
        "FCCA6D56D22EF933CF1FA32A70511B395E6BD7C7C4D8F70C28C1508AE22FC755",
    r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）\解答\4級_解答.pdf":
        "56ACA1A87BB52A0989E07E94C3C1F7AC9711B5E61DE6252B0320D553983A57DB",
}

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

EXPECTED_METADATA = {
    "grade": "grade4",
    "year": 2026,
    "session": "2026-1-sat",
    "exam": "2026-1-sat",
    "title": "英検4級 2026年度 第1回（土曜準会場）",
}
EXPECTED_SECTIONS = (
    ("大問1", "vocabulary", 15),
    ("大問2", "vocabulary", 5),
    ("大問3", "sentence-order", 5),
    ("大問4", "reading-comprehension", 10),
)
EXPECTED_PAIR_COUNTS = {"A": 7, "B": 17, "C": 13}
EXPECTED_VOCAB_SOURCES = {
    "大問1": 15, "大問2": 5, "大問3": 5,
    "大問4A": 1, "大問4B": 2, "大問4C": 2,
}


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def audio_ok(rel):
    if not rel:
        return False
    path = os.path.join(DATA_DIR, rel.replace("/", os.sep))
    return os.path.isfile(path) and os.path.getsize(path) >= 500


def has_blank(text):
    return bool(re.search(r"[（(][\s　]*[）)]", text or ""))


def compact(text):
    return re.sub(r"\s+", "", text or "")


def source_values():
    tree = ast.parse(open(SOURCE_GEN, encoding="utf-8").read())
    wanted = {
        "section1_questions", "section2_questions", "section3_questions",
        "passage_4a", "passage_4b", "passage_4c",
    }
    values = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            values[target.id] = ast.literal_eval(node.value)
    missing = wanted - values.keys()
    if missing:
        raise ValueError(f"source generator missing: {sorted(missing)}")
    return values


def source_payload(values):
    payload = []
    for key in ("section1_questions", "section2_questions"):
        payload.append([
            {"number": q["number"], "text": q["text"], "choices": q["choices"]}
            for q in values[key]
        ])
    payload.append([
        {
            "number": q["number"], "text": q["text"], "choices": q["choices"],
            "words": q["words"], "correctOrder": q["correctOrder"],
            "framePrefix": q["framePrefix"], "frameSuffix": q["frameSuffix"],
            "answerSlots": q["answerSlots"],
        }
        for q in values["section3_questions"]
    ])
    for key in ("passage_4a", "passage_4b", "passage_4c"):
        passage = values[key]
        payload.append({
            "label": passage["label"], "title": passage["title"],
            "format": passage.get("format"), "paragraphs": passage["paragraphs"],
            "questions": [
                {"number": q["number"], "question": q["question"], "choices": q["choices"]}
                for q in passage["questions"]
            ],
        })
    return payload


def section_questions(section):
    out = list(section.get("questions", []))
    for passage in section.get("passages", []):
        out.extend(passage.get("questions", []))
    return out


d = json.load(open(DATA_PATH, encoding="utf-8"))
issues = []
infos = []

# ---- 1. 原本PDFと原文固定スナップショット ----
for path, expected_hash in SOURCE_PDFS.items():
    if os.path.isfile(path):
        actual = file_sha256(path)
        if actual != expected_hash:
            issues.append(f"[原本PDF] SHA-256不一致: {path} {actual} != {expected_hash}")
        else:
            infos.append(f"[原本PDF] SHA-256一致: {os.path.basename(path)}")

try:
    src_values = source_values()
    raw = json.dumps(source_payload(src_values), ensure_ascii=False, separators=(",", ":"))
    actual_source_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    if actual_source_hash != SOURCE_PAYLOAD_SHA256:
        issues.append(
            f"[原文固定] source payload SHA-256={actual_source_hash} "
            f"!= {SOURCE_PAYLOAD_SHA256}"
        )
except Exception as exc:
    src_values = {}
    issues.append(f"[原文固定] source generator解析失敗: {exc}")

# ---- 2. メタデータ・セクション・正答 ----
for key, expected in EXPECTED_METADATA.items():
    if d.get(key) != expected:
        issues.append(f"[メタデータ] {key}={d.get(key)!r} != {expected!r}")

sections = d.get("sections", [])
if len(sections) != 4:
    issues.append(f"[構造] sections={len(sections)} != 4")

all_qs = []
for index, (name, sec_type, expected_count) in enumerate(EXPECTED_SECTIONS):
    if index >= len(sections):
        continue
    sec = sections[index]
    if sec.get("name") != name or sec.get("type") != sec_type:
        issues.append(
            f"[構造] sections[{index}]={sec.get('name')}/{sec.get('type')} "
            f"!= {name}/{sec_type}"
        )
    qs = section_questions(sec)
    if len(qs) != expected_count:
        issues.append(f"[構造] {name}: questions={len(qs)} != {expected_count}")
    all_qs.extend(qs)

q_by_num = {q.get("number"): q for q in all_qs}
if sorted(q_by_num) != list(range(1, 36)):
    issues.append(f"[構造] question numbers={sorted(q_by_num)}")
for number, expected in OFFICIAL_READING.items():
    q = q_by_num.get(number)
    if not q:
        issues.append(f"[正答] Q{number}: 問題欠落")
    elif q.get("answer") != expected:
        issues.append(f"[正答] Q{number}: {q.get('answer')} != {expected}")

for part, expected in OFFICIAL_LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    for number, answer in expected.items():
        actual = got.get(str(number), got.get(number))
        if actual != answer:
            issues.append(f"[リスニング] {part} Q{number}: {actual} != {answer}")

# ---- 3. 原文転記フィールドを一字単位で照合 ----
if src_values:
    for key in ("section1_questions", "section2_questions"):
        for source_q in src_values[key]:
            q = q_by_num.get(source_q["number"], {})
            for field in ("text", "choices"):
                if q.get(field) != source_q[field]:
                    issues.append(f"[原本] Q{source_q['number']}: {field}不一致")
    for source_q in src_values["section3_questions"]:
        q = q_by_num.get(source_q["number"], {})
        for field in (
            "text", "choices", "words", "correctOrder", "framePrefix",
            "frameSuffix", "answerSlots",
        ):
            if q.get(field) != source_q[field]:
                issues.append(f"[原本] Q{source_q['number']}: {field}不一致")

    source_passages = {
        p["label"]: p
        for p in (src_values["passage_4a"], src_values["passage_4b"], src_values["passage_4c"])
    }
    data_passages = {
        p.get("label"): p for p in sections[3].get("passages", [])
    } if len(sections) > 3 else {}
    for label, source_passage in source_passages.items():
        passage = data_passages.get(label)
        if not passage:
            issues.append(f"[原本] passage {label}: 欠落")
            continue
        for field in ("label", "title", "paragraphs"):
            if passage.get(field) != source_passage[field]:
                issues.append(f"[原本] passage {label}: {field}不一致")
        if passage.get("format") != source_passage.get("format"):
            issues.append(f"[原本] passage {label}: format不一致")
        source_questions = {q["number"]: q for q in source_passage["questions"]}
        for q in passage.get("questions", []):
            source_q = source_questions.get(q.get("number"), {})
            for field in ("question", "choices"):
                if q.get(field) != source_q.get(field):
                    issues.append(f"[原本] Q{q.get('number')}: {field}不一致")

# ---- 4. リッチ解説・マーカー・空所・音声 ----
common_keys = (
    "choices", "choiceAnalysis", "choiceAnalysisSimple", "grammar",
    "grammarSimple", "questionAudio",
)
for number, q in sorted(q_by_num.items()):
    for key in common_keys:
        if not q.get(key):
            issues.append(f"[解説] Q{number}: missing {key}")
    if number <= 20:
        for key in ("text", "translation", "choiceTranslations"):
            if not q.get(key):
                issues.append(f"[解説] Q{number}: missing {key}")
        if has_blank(q.get("text")) and not has_blank(q.get("translation")):
            issues.append(f"[和訳] Q{number}: 英文の空所が和訳に残っていません")
    if number >= 26:
        for key in ("question", "questionTranslation", "choiceTranslations", "sourceEvidence"):
            if not q.get(key):
                issues.append(f"[読解] Q{number}: missing {key}")

    for field in ("choices", "choiceTranslations", "choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        if values and len(values) != 4:
            issues.append(f"[解説] Q{number}: {field}={len(values)} != 4")

    for field in ("choiceAnalysis", "choiceAnalysisSimple"):
        values = q.get(field, [])
        marked = [i + 1 for i, text in enumerate(values) if text.lstrip().startswith("○")]
        if values and marked != [q.get("answer")]:
            issues.append(f"[マーカー] Q{number} {field}: ○位置={marked}")
        if any(text.lstrip().startswith(("✅", "❌")) for text in values):
            issues.append(f"[マーカー] Q{number} {field}: 旧✅/❌が残っています")

    if not audio_ok(q.get("questionAudio")):
        issues.append(f"[音声] Q{number}: {q.get('questionAudio')}")

# ---- 5. 並べ替え ----
if len(sections) > 2:
    for q in sections[2].get("questions", []):
        number = q["number"]
        order = q.get("correctOrder", [])
        slots = q.get("answerSlots", [])
        if sorted(order) != [1, 2, 3, 4, 5] or slots != [2, 4]:
            issues.append(f"[並べ替え] Q{number}: order/slots不正")
            continue
        circled = lambda value: chr(0x2460 + value - 1)
        expected_label = f"{circled(order[1])}−{circled(order[3])}"
        actual_label = q["choices"][q["answer"] - 1]
        if actual_label != expected_label:
            issues.append(f"[並べ替え] Q{number}: {actual_label} != {expected_label}")
        for index, explanation in enumerate(q.get("choiceAnalysis", []), 1):
            if "2番目" not in explanation or "4番目" not in explanation:
                issues.append(f"[並べ替え] Q{number} 選択肢{index}: 位置説明不足")

# ---- 6. 長文和訳・sentencePairs完全被覆・本文根拠 ----
if len(sections) > 3:
    passages = sections[3].get("passages", [])
    if len(passages) != 3:
        issues.append(f"[長文] passages={len(passages)} != 3")
    for passage in passages:
        label = passage.get("label")
        paragraphs = passage.get("paragraphs", [])
        translations = passage.get("translations", [])
        pairs = passage.get("sentencePairs", [])
        if len(paragraphs) != len(translations):
            issues.append(f"[長文] {label}: paragraphs/translations不一致")
        expected_count = EXPECTED_PAIR_COUNTS.get(label)
        if len(pairs) != expected_count:
            issues.append(f"[長文] {label}: sentencePairs={len(pairs)} != {expected_count}")
        valid_pairs = []
        for index, pair in enumerate(pairs):
            if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(x, str) and x for x in pair):
                issues.append(f"[長文] {label}: sentencePairs[{index}]不正")
            else:
                valid_pairs.append(pair)
        if len({pair[0] for pair in valid_pairs}) != len(valid_pairs):
            issues.append(f"[長文] {label}: sentencePairs英文重複")
        if compact("".join(pair[0] for pair in valid_pairs)) != compact("".join(paragraphs)):
            issues.append(f"[長文] {label}: sentencePairs英文が本文を完全被覆していません")
        if compact("".join(pair[1] for pair in valid_pairs)) != compact("".join(translations)):
            issues.append(f"[長文] {label}: sentencePairs和訳が段落和訳を完全被覆していません")
        corpus = " ".join(paragraphs)
        for q in passage.get("questions", []):
            evidence = q.get("sourceEvidence", "")
            if evidence and evidence not in corpus:
                issues.append(f"[根拠] Q{q['number']}: 本文にない: {evidence}")
            correct = q.get("choiceAnalysis", [])[q["answer"] - 1]
            if evidence and not any(token in correct for token in re.findall(r"[A-Za-z][A-Za-z0-9'.:-]*", evidence)):
                issues.append(f"[根拠] Q{q['number']}: 正解解説に英文根拠がありません")

# ---- 7. 語彙 ----
vocabulary = d.get("vocabulary", [])
if len(vocabulary) != 30:
    issues.append(f"[語彙] count={len(vocabulary)} != 30")
source_counts = Counter()
seen_meanings = set()
for index, item in enumerate(vocabulary, 1):
    for key in (
        "word", "meaning", "pos", "level", "source", "example",
        "distractors", "wordAudio", "exampleAudio",
    ):
        if not item.get(key):
            issues.append(f"[語彙] #{index}: missing {key}")
    if item.get("level") != "4級":
        issues.append(f"[語彙] {item.get('word')}: level={item.get('level')}")
    if len(item.get("distractors", [])) != 3:
        issues.append(f"[語彙] {item.get('word')}: distractors != 3")
    if item.get("meaning") in item.get("distractors", []):
        issues.append(f"[語彙] {item.get('word')}: 正解意味がdistractorsにあります")
    if item.get("meaning") in seen_meanings:
        issues.append(f"[語彙] 意味重複: {item.get('meaning')}")
    seen_meanings.add(item.get("meaning"))
    source_counts[item.get("source")] += 1
    for field in ("wordAudio", "exampleAudio"):
        if not audio_ok(item.get(field)):
            issues.append(f"[音声] vocab {item.get('word')} {field}: {item.get(field)}")
if dict(source_counts) != EXPECTED_VOCAB_SOURCES:
    issues.append(f"[語彙] source counts={dict(source_counts)} != {EXPECTED_VOCAB_SOURCES}")

# ---- 8. Focus Practice ----
fps = d.get("lessonPlan", {}).get("focusPoints", [])
if len(fps) != 4:
    issues.append(f"[FP] count={len(fps)} != 4")
for index, fp in enumerate(fps, 1):
    expected_id = f"fp{index}"
    if fp.get("id") != expected_id:
        issues.append(f"[FP] #{index}: id={fp.get('id')} != {expected_id}")
    for key in (
        "title", "subtitle", "explanation", "explanationSimple", "sourceQuote",
        "sourceLocation", "examples", "practicePassage", "highlightPatterns",
        "highlightColor", "highlightLabel", "practiceQuestions",
        "practiceQuestionsSimple", "sourceQuoteAudio",
    ):
        if not fp.get(key):
            issues.append(f"[FP] {expected_id}: missing {key}")
    if len(fp.get("explanation", "")) < 100:
        issues.append(f"[FP] {expected_id}: explanationが短すぎます")
    if len(fp.get("examples", [])) != 3:
        issues.append(f"[FP] {expected_id}: examples={len(fp.get('examples', []))} != 3")
    for example_index, example in enumerate(fp.get("examples", []), 1):
        for key in ("en", "ja", "note", "noteSimple", "audio"):
            if not example.get(key):
                issues.append(f"[FP] {expected_id} example{example_index}: missing {key}")
        if not audio_ok(example.get("audio")):
            issues.append(f"[音声] {expected_id} example{example_index}: {example.get('audio')}")
    passage = fp.get("practicePassage", {})
    for key in ("en", "ja", "source", "audioFile"):
        if not passage.get(key):
            issues.append(f"[FP] {expected_id}: practicePassage missing {key}")
    if "[出典:" not in passage.get("en", ""):
        issues.append(f"[FP] {expected_id}: practicePassageに出典表示なし")
    if not audio_ok(passage.get("audioFile")):
        issues.append(f"[音声] {expected_id} practice: {passage.get('audioFile')}")
    if not audio_ok(fp.get("sourceQuoteAudio")):
        issues.append(f"[音声] {expected_id} sourceQuote: {fp.get('sourceQuoteAudio')}")
    if len(fp.get("practiceQuestions", [])) != 3 or len(fp.get("practiceQuestionsSimple", [])) != 3:
        issues.append(f"[FP] {expected_id}: practiceQuestionsは各3問必要です")

all_japanese = json.dumps(d, ensure_ascii=False)
for stale in (
    "全部屋", "お兄ちゃんに親切", "おとうとにやさしく",
    "床で休んでいる", "「1さつ」はしょうせつだよ",
):
    if stale in all_japanese:
        issues.append(f"[表現] 古い表現が残っています: {stale}")
fp4_text = fps[3].get("practicePassage", {}).get("en", "") if len(fps) >= 4 else ""
full_history_sentence = (
    "When Kate and her father visited the hospital, they saw three novels, "
    "four history books, and two magazines around her grandmother's bed."
)
if full_history_sentence not in fp4_text or "\nThey saw three novels" in fp4_text:
    issues.append("[FP] fp4: Kate's Storyの原文引用が不完全です")

print(f"=== 監査結果: issues={len(issues)} ===")
for info in infos:
    print("  [OK]", info)
for issue in issues:
    print("  [NG]", issue)
if not issues:
    print("  問題なし")
sys.exit(1 if issues else 0)
