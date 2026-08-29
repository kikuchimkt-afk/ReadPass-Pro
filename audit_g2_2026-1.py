# -*- coding: utf-8 -*-
"""2026-1 本会場 2級 総合監査 — 原本・正答・全文対訳・解説・音声"""
import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1",
)
DATA = os.path.join(BASE, "data.json")
REPO = os.path.dirname(os.path.abspath(__file__))

OFFICIAL = {
    1: 4, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 3, 10: 1,
    11: 4, 12: 4, 13: 2, 14: 1, 15: 1, 16: 1, 17: 2,
    18: 1, 19: 1, 20: 3, 21: 2, 22: 1, 23: 4,
    24: 3, 25: 1, 26: 4, 27: 3, 28: 1, 29: 3, 30: 1, 31: 4,
}

LISTENING = {
    "part1": {
        1: 3, 2: 4, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 1, 10: 4,
        11: 4, 12: 1, 13: 4, 14: 3, 15: 2,
    },
    "part2": {
        16: 1, 17: 2, 18: 1, 19: 1, 20: 1, 21: 3, 22: 2, 23: 1, 24: 4, 25: 2,
        26: 2, 27: 4, 28: 1, 29: 2, 30: 2,
    },
}

EXPECTED_METADATA = {
    "grade": "2級",
    "year": "2026",
    "session": "1",
    "title": "2026年度 第1回 英語資格検定2級 リーディング",
    "exam": "2026-1",
}

EXPECTED_SECTION_META = [
    ("大問1", "Part 1", "vocabulary"),
    ("大問2", "Part 2", "passage-fill"),
    ("大問3", "Part 3", "reading-comprehension"),
]

# gen_g2_2026-1_reading.py に固定した、公式問題の英文・選択肢・正答のスナップショット。
SOURCE_PAYLOAD_SHA256 = "80271176ec2df6c974354ac3573292e93a8f90afdd05bc2ecca100006325c7b7"
EXPECTED_PAIR_COUNTS = {
    "Efforts at a Village": 19,
    "The Science of Fear": 18,
    "Your service": 14,
    "The Humboldt Brothers": 22,
}
EXPECTED_VOCAB_WORDS = [
    "bride", "lawyer", "surgeon", "globe", "branch", "difficulty", "glory",
    "tendency", "discrimination", "foster", "typical", "gradual", "weep",
    "occur", "illustrate", "occupy", "barely", "frown", "as a general rule",
    "on his own", "go along with", "a series of", "in other words",
    "distinct from", "lay off", "rural", "literacy", "motivate", "costume",
    "rumor", "dramatic", "community", "spread", "superhero", "creative",
    "starve", "emotion", "dangerous", "breathing", "muscle", "fight-or-flight",
    "fascinated", "intensely", "overwhelming", "mechanism", "treatment",
    "facility", "athletic", "coworker", "access", "suitable", "wealthy",
    "adventure", "tutor", "proposal", "perceive", "individuality",
    "intellectual", "impact", "indirectly", "economics",
]
CRITICAL_VOCAB = {
    "access": ("（場所などに）行く、利用する", "動詞"),
    "tutor": ("個別に教える、家庭教師として教える", "動詞"),
}

MONOTONY_PHRASES = {
    "と矛盾": 10,
    "意味が通らない": 6,
    "不自然": 12,
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
            out.append((sec["name"], sec.get("type"), q, None))
        for p in sec.get("passages", []):
            corpus = " ".join(p.get("paragraphs", []))
            for q in p.get("questions", []):
                out.append((sec["name"], sec.get("type"), q, corpus))
    return out


def has_english_evidence(text):
    if re.search(r"[（(][^）)]*[A-Za-z]{3,}[^）)]*[）)]", text):
        return True
    if re.search(r"[A-Za-z]{3,}(?:\s+[A-Za-z]{2,})+", text):
        return True
    return False


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()


def canonical_sha256(value):
    blob = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def select_source_shape(source, current):
    """Return current data projected to the immutable source object's shape."""
    if isinstance(source, dict):
        return {key: select_source_shape(value, current[key]) for key, value in source.items()}
    if isinstance(source, list):
        if not isinstance(current, list) or len(source) != len(current):
            return current
        return [
            select_source_shape(source_item, current_item)
            for source_item, current_item in zip(source, current)
        ]
    return current


def extract_source_payload():
    source_path = os.path.join(REPO, "gen_g2_2026-1_reading.py")
    tree = ast.parse(open(source_path, encoding="utf-8").read())
    wanted = {
        "section1_questions", "passage_2a", "passage_2b", "passage_3a", "passage_3b",
    }
    values = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id in wanted
        ):
            values[node.targets[0].id] = ast.literal_eval(node.value)
    missing = wanted - set(values)
    if missing:
        raise AssertionError(f"source assignments missing: {sorted(missing)}")
    return values


def extract_data_source_payload(data, source):
    sections = {section["name"]: section for section in data["sections"]}
    passages = {
        (section["name"], passage["label"]): passage
        for section in data["sections"]
        for passage in section.get("passages", [])
    }
    mapping = {
        "section1_questions": sections["大問1"]["questions"],
        "passage_2a": passages[("大問2", "A")],
        "passage_2b": passages[("大問2", "B")],
        "passage_3a": passages[("大問3", "A")],
        "passage_3b": passages[("大問3", "B")],
    }
    return {
        key: select_source_shape(source[key], mapping[key])
        for key in source
    }


all_qs = collect_questions(d)
seen = {q["number"] for _, _, q, _ in all_qs}

# ---- 1. メタデータ ----
for key, expected in EXPECTED_METADATA.items():
    if d.get(key) != expected:
        errors.append(f"[メタ] {key}={d.get(key)!r} != {expected!r}")
expected_keys = [
    "grade", "year", "session", "title", "exam", "sections", "listening",
    "vocabulary", "lessonPlan",
]
if list(d) != expected_keys:
    errors.append(f"[メタ] top-level keys/order={list(d)}")
if len(d.get("sections", [])) != 3:
    errors.append(f"[構造] sections={len(d.get('sections', []))} != 3")
else:
    section_meta = [
        (s.get("name"), s.get("nameEn"), s.get("type")) for s in d["sections"]
    ]
    if section_meta != EXPECTED_SECTION_META:
        errors.append(f"[構造] section metadata={section_meta}")
if len(all_qs) != 31 or seen != set(range(1, 32)):
    errors.append(f"[構造] reading questions={len(all_qs)} numbers={sorted(seen)}")

# ---- 2. 正答 ----
for n, ans in OFFICIAL.items():
    if n not in seen:
        errors.append(f"[正答] Q{n}: 問題欠落")
for _, _, q, _ in all_qs:
    n = q["number"]
    if OFFICIAL.get(n) != q.get("answer"):
        errors.append(f"[正答] Q{n}: answer={q.get('answer')} 公式={OFFICIAL.get(n)}")
    for field in ("choices", "choiceTranslations", "choiceAnalysis"):
        if len(q.get(field, [])) != 4:
            errors.append(f"[構造] Q{n}: {field}数={len(q.get(field, []))}")
    if not q.get("grammar"):
        errors.append(f"[解説] Q{n}: grammar欠落")
    if n <= 17:
        for field in ("text", "translation"):
            if norm(q.get(field, "")).count("( )") != 1:
                errors.append(f"[空所] Q{n}: {field}の空所数が1ではない")
    elif n >= 24:
        for field in ("question", "questionTranslation"):
            if not q.get(field):
                errors.append(f"[解説] Q{n}: {field}欠落")

# ---- 3. リスニング ----
for part, expected in LISTENING.items():
    got = d.get("listening", {}).get(part, {})
    normalized = {int(key): value for key, value in got.items()}
    if normalized != expected:
        errors.append(f"[リスニング] {part}: 設問番号・正答マップが公式一覧と完全一致しない")
    for k, v in expected.items():
        key = str(k)
        gv = got.get(key, got.get(k))
        if gv != v:
            errors.append(f"[リスニング] {part} Q{k}: {gv} != {v}")

# ---- 4. choiceAnalysis 表示規約（2025年度2級と統一） ----
for _, _, q, _ in all_qs:
    n = q["number"]
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        errors.append(f"[解説] Q{n}: choiceAnalysis数={len(ca)}")
        continue
    if any(text.lstrip().startswith(("✅", "❌", "○", "×")) for text in ca):
        errors.append(f"[解説] Q{n}: 先頭マーカーが残っている")
    correct = ca[q["answer"] - 1]
    if correct.count("→正解。💡") != 1:
        errors.append(f"[解説] Q{n}: 正答解説に「→正解。💡」が1個ではない")
    for index, text in enumerate(ca, 1):
        if index != q["answer"] and "→正解" in text:
            errors.append(f"[解説] Q{n}: 誤答{index}に正解表示がある")

# ---- 5. sentencePairs ----
total_sentence_pairs = 0
for sec in d["sections"]:
    for p in sec.get("passages", []):
        full = " ".join(p["paragraphs"])
        pairs = p.get("sentencePairs", [])
        total_sentence_pairs += len(pairs)
        expected_count = EXPECTED_PAIR_COUNTS.get(p.get("title"))
        if len(pairs) != expected_count:
            errors.append(
                f"[対訳] {p.get('title')}: sentencePairs={len(pairs)} != {expected_count}"
            )
        pair_english = []
        for i, pair in enumerate(pairs):
            if (
                not isinstance(pair, list)
                or len(pair) != 4
                or not all(isinstance(text, str) and text.strip() for text in pair)
            ):
                errors.append(
                    f"[対訳] {p.get('title')} pair{i + 1}: "
                    "[英文, 和訳, スラッシュ読み, 主動詞] ではない"
                )
                continue
            pair_english.append(pair[0])
            if pair[0] not in full:
                errors.append(
                    f"{sec['name']}{p.get('label', '')}: sentencePair[{i}] not in paragraphs: {pair[0][:60]}..."
                )
            slash_segments = pair[2].split("||")
            if len(slash_segments) < 2:
                errors.append(f"[対訳] {p.get('title')} pair{i + 1}: 意味単位が2個未満")
                continue
            if any(
                segment.count("|") != 1
                or not all(part.strip() for part in segment.split("|", 1))
                for segment in slash_segments
            ):
                errors.append(f"[対訳] {p.get('title')} pair{i + 1}: slash形式不正")
                continue
            slash_english = " ".join(
                segment.split("|", 1)[0] for segment in slash_segments
            )
            if norm(slash_english) != norm(pair[0]):
                errors.append(
                    f"[対訳] {p.get('title')} pair{i + 1}: slash英文が原文と不一致"
                )
            if not re.search(
                rf"(?<!\w){re.escape(pair[3])}(?!\w)", pair[0], re.IGNORECASE
            ):
                errors.append(
                    f"[対訳] {p.get('title')} pair{i + 1}: 主動詞が英文内にない"
                )
        if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
            errors.append(f"[構造] {p.get('title')}: paragraphs/translations不一致")
        if p.get("format") == "email":
            # 2025年度データと同様、あいさつ・署名を除く本文全14文を対訳化する。
            expected_corpus = (
                p["paragraphs"][0].split("\n", 1)[1]
                + " " + p["paragraphs"][1]
                + " " + p["paragraphs"][2]
            )
        else:
            expected_corpus = full
        if norm(" ".join(pair_english)) != norm(expected_corpus):
            errors.append(f"[対訳] {p.get('title')}: sentencePairsが本文全文を覆っていない")
if total_sentence_pairs != 73:
    errors.append(f"[対訳] sentencePairs総数={total_sentence_pairs} != 73")

# ---- 6. 大問2: 空所番号 ----
for sec in d["sections"]:
    if sec["type"] == "passage-fill":
        for p in sec["passages"]:
            text = " ".join(p["paragraphs"])
            blanks = sorted(int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", text))
            translated = " ".join(p.get("translations", []))
            translated_blanks = sorted(
                int(x) for x in re.findall(r"\(\s*(\d+)\s*\)", translated)
            )
            qnums = sorted(q["number"] for q in p["questions"])
            if blanks != qnums:
                errors.append(f"{sec['name']}{p['label']}: blanks {blanks} != questions {qnums}")
            if translated_blanks != qnums:
                errors.append(
                    f"{sec['name']}{p['label']}: 和訳blanks {translated_blanks} != questions {qnums}"
                )

# ---- 7. sourceEvidence（大問2・3 = Q18〜31）----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    if n < 18:
        continue
    ev = q.get("sourceEvidence")
    if not ev:
        errors.append(f"[根拠] Q{n}: sourceEvidence未設定")
        continue
    if not isinstance(ev, list) or not ev:
        errors.append(f"[根拠] Q{n}: sourceEvidenceが空")
        continue
    if corpus:
        for phrase in ev:
            if phrase not in corpus:
                errors.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {phrase[:60]}...")

# ---- 8. 解説の英文エビデンス ----
for sec_name, sec_type, q, corpus in all_qs:
    n = q["number"]
    for i, ca in enumerate(q.get("choiceAnalysis", [])):
        if not has_english_evidence(ca):
            errors.append(f"[根拠] Q{n} 選択肢{i+1}: choiceAnalysisに英文根拠なし")

# ---- 9. 単調さ ----
phrase_counts = Counter()
for _, _, q, _ in all_qs:
    for ca in q.get("choiceAnalysis", []):
        for phrase in MONOTONY_PHRASES:
            if phrase in ca:
                phrase_counts[phrase] += 1
for phrase, limit in MONOTONY_PHRASES.items():
    if phrase_counts[phrase] > limit:
        warns.append(f"[単調] 「{phrase}」が{phrase_counts[phrase]}回（推奨上限{limit}）")

# ---- 10. 公式問題スナップショット ----
source_payload = extract_source_payload()
source_hash = canonical_sha256(source_payload)
if source_hash != SOURCE_PAYLOAD_SHA256:
    errors.append(f"[原本] generatorの問題スナップショット不一致: {source_hash}")
if extract_data_source_payload(d, source_payload) != source_payload:
    errors.append("[原本] 英文・選択肢・正答・本文・メール情報が原本と不一致")

# ---- 11. 語彙 ----
vocab = d["vocabulary"]
words = [v["word"].lower() for v in vocab]
if len(vocab) != 61:
    errors.append(f"[語彙] count={len(vocab)} != 61")
if [v.get("word") for v in vocab] != EXPECTED_VOCAB_WORDS:
    errors.append("[語彙] 見出し語または順序が監査済み一覧と不一致")
for w in set(words):
    if words.count(w) > 1:
        errors.append(f"vocab: duplicate word '{w}'")
for i, v in enumerate(vocab):
    for key in ("word", "meaning", "pos", "level", "source", "example", "distractors"):
        if not v.get(key):
            errors.append(f"[語彙] vocab[{i}] {v.get('word')}: {key}欠落")
    if len(v.get("distractors", [])) != 3:
        errors.append(f"[語彙] {v.get('word')}: distractors数 != 3")
    expected_prefix = f"audio/vocab/w_{i+1:03d}_"
    if not v.get("wordAudio", "").startswith(expected_prefix):
        errors.append(f"vocab[{i}] {v['word']}: wordAudio mismatch")
    fp = os.path.join(BASE, v.get("wordAudio", "").replace("/", os.sep))
    if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
        errors.append(f"[音声] vocab {v['word']}: {v.get('wordAudio')} 欠落")
for word, (meaning, pos) in CRITICAL_VOCAB.items():
    item = next((entry for entry in vocab if entry.get("word") == word), None)
    if not item or (item.get("meaning"), item.get("pos")) != (meaning, pos):
        errors.append(f"[語彙] {word}: meaning/posが監査値と不一致")

# ---- 12. lessonPlan ----
corpus_all = ""
for sec in d["sections"]:
    for q in sec.get("questions", []):
        corpus_all += q.get("text", "") + " "
    for p in sec.get("passages", []):
        corpus_all += " ".join(p.get("paragraphs", [])) + " "

focus_points = d.get("lessonPlan", {}).get("focusPoints", [])
if len(focus_points) != 5:
    errors.append(f"[FP] focusPoints={len(focus_points)} != 5")
for index, fp in enumerate(focus_points, 1):
    if fp.get("id") != f"fp{index}":
        errors.append(f"[FP] index={index}: id={fp.get('id')}")
    for key in (
        "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
        "highlightColor", "highlightLabel",
    ):
        if not fp.get(key):
            errors.append(f"[FP] {fp.get('id')}: {key}欠落")
    pp = fp["practicePassage"]
    if "[出典:" not in pp.get("en", ""):
        errors.append(f"[FP] {fp.get('id')}: practicePassageの出典欠落")
    af = pp.get("audioFile", "")
    fpath = os.path.join(BASE, af.replace("/", os.sep))
    if not os.path.isfile(fpath) or os.path.getsize(fpath) < 500:
        errors.append(f"{fp['id']}: missing audio {af}")
    for pat in fp.get("highlightPatterns", []):
        if pat not in corpus_all and pat not in pp.get("en", ""):
            errors.append(f"[FP] {fp['id']}: highlight不在: {pat[:50]}")

if len(focus_points) == 5:
    fp1, fp2, fp3, fp4, _ = focus_points
    if "are even fascinated by this feeling が正解" not in fp1["practiceQuestions"][1]["q"]:
        errors.append("[FP] fp1: Q22の正答表現が逆転している")
    if "彼を本当に生きているかのように見せました" not in fp2["examples"][2]["ja"]:
        errors.append("[FP] fp2: to bring him to life の訳が欠落")
    if "彼を飢えさせないよう" not in fp2["practicePassage"]["ja"]:
        errors.append("[FP] fp2: so that he would not starve の訳が欠落")
    fp3_answer = fp3["practiceQuestions"][0]["a"]
    if "唯一" in fp3_answer or "スタッフの親切さは根拠にできない" not in fp3_answer:
        errors.append("[FP] fp3: Q24の根拠説明が不正確")
    if "Q30" not in fp4.get("explanation", ""):
        errors.append("[FP] fp4: wealthy background の参照設問がQ30ではない")

# 今回確認した誤説明・不自然な旧訳の再混入を防ぐ。
data_blob = json.dumps(d, ensure_ascii=False)
for stale in (
    "illustrate how cells work（細胞の働きを占める）",
    "恐怖はすぐに脳に反応させ",
    "恐怖はすぐに脳を反応させ",
    "農村の村",
    "移動中の公共の読書",
    "弟からの新しい場所への旅の誘い",
    "兄からの新しい場所への旅の誘い",
    "裕福な背景は質の高い教育",
    "( )の検査の後",
    "従業員の一部を( )せざる",
    "barely＝かろうじて・あわや",
    "They like scary things and seek excitement が正解になる",
    "唯一の「魅力の理由」",
    "bring out in＝慣用句として成立しない",
    "do everything to his surprise では「驚きながらすべてをする」",
    "few access to books",
    "Motivated by this（これに動機づけられて）",
    "名詞 foster care",
    "On the contrary＝それどころか",
):
    if stale in data_blob:
        errors.append(f"[表現] 古い誤説明・不自然表現が残存: {stale}")

print(f"errors={len(errors)} warnings={len(warns)}")
for e in errors:
    print("  [ERROR]", e)
for w in warns:
    print("  [WARN] ", w)
if errors:
    sys.exit(1)
print("AUDIT OK")
