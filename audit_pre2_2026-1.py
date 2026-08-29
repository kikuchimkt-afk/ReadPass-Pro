# -*- coding: utf-8 -*-
"""2026-1-sat 準2級の原本・正答・解説・対訳・語彙・教材・音声監査。"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "data" / "grade-pre2" / "2026-1-sat"
DATA = BASE / "data.json"
SOURCE_ROOT = Path(r"D:\Files\英検過去問\土曜準会場\2026-1（土曜）")
SOURCE_PROBLEM = SOURCE_ROOT / "準2級.pdf"
SOURCE_ANSWER = SOURCE_ROOT / "解答" / "準2級_解答.pdf"
SOURCE_AUDIO = SOURCE_ROOT / "2026-1_音源" / "準2級"

SOURCE_HASHES = {
    SOURCE_PROBLEM: "F583F14662C2001E066B4509ADB4B7B0D5F4B91553C8B5CE3C777FA57170B61C",
    SOURCE_ANSWER: "8252125A2F6FE26AC3BC7CD4765948C3DC56F615E6D5D9F0A32C0068298EF158",
}

OFFICIAL_READING = {
    1: 2, 2: 2, 3: 3, 4: 4, 5: 3, 6: 4, 7: 3, 8: 4, 9: 2, 10: 4,
    11: 4, 12: 2, 13: 3, 14: 1, 15: 2,
    16: 1, 17: 1, 18: 4, 19: 1, 20: 2,
    21: 4, 22: 1, 23: 3, 24: 4, 25: 1, 26: 4, 27: 4, 28: 3, 29: 2,
}

# 公式解答PDF掲載のリスニング正答。ReadPassのdata.jsonはリーディング専用なので、
# 外部音源の存在と、この固定キー自体の件数・選択肢範囲を監査する。
OFFICIAL_LISTENING = {
    "part1": [2, 1, 2, 3, 3, 2, 2, 3, 2, 2],
    "part2": [2, 1, 3, 4, 1, 3, 1, 3, 3, 2],
    "part3": [4, 2, 1, 1, 1, 2, 4, 1, 4, 2],
}

# Section名・instruction・英文・選択肢・正答・長文原文だけを抽出した固定値。
# 翻訳や解説を改善しても、一次ソース由来の英語が変われば必ず失敗する。
IMMUTABLE_SOURCE_SHA256 = "271decf37f25359165402338d941b442256985c6d9770d9888db4f2f23bb29e9"

EXPECTED_PASSAGES = {
    "A Lost Dog": (2, 14),
    "A job at a ski resort": (3, 21),
    "Social Media for Mental Health": (4, 19),
}

EXPECTED_VOCAB = {
    "appealing": ("魅力的な", "形容詞"),
    "appearance": ("外見・身だしなみ", "名詞"),
    "conference": ("会議", "名詞"),
    "director": ("映画監督", "名詞"),
    "insects": ("昆虫", "名詞"),
    "promote": ("促進する・推進する", "動詞"),
    "awfully": ("とても（強調）", "副詞"),
    "wondered": ("～かどうかと思った", "動詞"),
    "judge": ("判断する", "動詞"),
    "occupied": ("使用中の・占有された", "形容詞"),
    "in the near future": ("近い将来に", "副詞句"),
    "a sort of": ("一種の", "句"),
    "known as": ("～として知られている", "熟語"),
    "find fault with": ("～のあら探しをする・けちをつける", "句動詞"),
    "help yourself": ("（食べ物などを）自由に取る", "句"),
    "boring": ("退屈な", "形容詞"),
    "intelligence": ("知性", "名詞"),
    "go straight there": ("そこへ直行する", "表現"),
    "sticker": ("ステッカー・シール", "名詞"),
    "mountain jacket": ("登山用ジャケット", "名詞句"),
    "arrival area": ("到着エリア・到着ロビー", "名詞句"),
    "pick up": ("（物を）受け取る・（人を）迎えに行く", "句動詞"),
    "poster": ("ポスター", "名詞"),
    "nowhere": ("どこにも～ない", "副詞"),
    "accept": ("受け入れる", "動詞"),
    "similar": ("似ている", "形容詞"),
    "hurry": ("急ぐ", "動詞"),
    "missing": ("行方不明の", "形容詞"),
    "opportunity": ("機会", "名詞"),
    "interview": ("面接", "名詞"),
    "equipment": ("装備・器材", "名詞"),
    "cafeteria": ("食堂", "名詞"),
    "freely": ("自由に", "副詞"),
    "mental health": ("精神的健康", "名詞句"),
    "social media": ("ソーシャルメディア", "名詞"),
    "influence": ("影響を与える", "動詞"),
    "accepted": ("受け入れられた", "形容詞"),
    "connected": ("つながった", "形容詞"),
    "expert": ("専門家", "名詞"),
    "professional": ("専門的な", "形容詞"),
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def source_payload(data: dict) -> list[dict]:
    payload = []
    for sec in data["sections"]:
        item = {
            "name": sec["name"],
            "nameEn": sec["nameEn"],
            "type": sec["type"],
            "instruction": sec["instruction"],
        }
        if "questions" in sec:
            item["questions"] = [
                {
                    "number": q["number"],
                    "text": q["text"],
                    "choices": q["choices"],
                    "answer": q["answer"],
                }
                for q in sec["questions"]
            ]
        if "passages" in sec:
            item["passages"] = [
                {
                    "label": p.get("label"),
                    "title": p["title"],
                    "format": p.get("format"),
                    "meta": p.get("meta"),
                    "paragraphs": p["paragraphs"],
                    "questions": [
                        {
                            "number": q["number"],
                            "question": q.get("question"),
                            "choices": q["choices"],
                            "answer": q["answer"],
                        }
                        for q in p["questions"]
                    ],
                }
                for p in sec["passages"]
            ]
        payload.append(item)
    return payload


def collect_questions(data: dict) -> list[tuple[dict, str | None]]:
    out = []
    for sec in data.get("sections", []):
        out.extend((q, None) for q in sec.get("questions", []))
        for passage in sec.get("passages", []):
            corpus = " ".join(passage.get("paragraphs", []))
            out.extend((q, corpus) for q in passage.get("questions", []))
    return out


data = json.loads(DATA.read_text(encoding="utf-8"))
errors: list[str] = []
notes: list[str] = []

# 一次ソースの同一性（ローカル原本がある場合は厳密照合）。
for source_path, expected_hash in SOURCE_HASHES.items():
    if source_path.is_file():
        actual_hash = sha256_file(source_path)
        if actual_hash != expected_hash:
            errors.append(f"[原本] {source_path.name}: SHA256={actual_hash} expected={expected_hash}")
        else:
            notes.append(f"[原本] {source_path.name}: SHA256一致")
    else:
        notes.append(f"[原本] ローカル原本なし（スキップ）: {source_path}")

# メタデータ・構造。
for key in ("grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"):
    if key not in data:
        errors.append(f"[構造] missing {key}")
if data.get("grade") != "準2級" or data.get("year") != "2026" or data.get("session") != "1":
    errors.append("[構造] grade/year/session mismatch")

expected_sections = [
    ("大問1", "vocabulary", 15),
    ("大問2", "vocabulary", 5),
    ("大問3", "passage-fill", 0),
    ("大問4", "reading-comprehension", 0),
]
if len(data.get("sections", [])) != 4:
    errors.append(f"[構造] sections={len(data.get('sections', []))} != 4")
else:
    for sec, (name, stype, qcount) in zip(data["sections"], expected_sections):
        if (sec.get("name"), sec.get("type")) != (name, stype):
            errors.append(f"[構造] {name}: name/type mismatch")
        if len(sec.get("questions", [])) != qcount:
            errors.append(f"[構造] {name}: questions={len(sec.get('questions', []))} != {qcount}")
        if not sec.get("instruction"):
            errors.append(f"[構造] {name}: instruction missing")

payload_bytes = json.dumps(
    source_payload(data), ensure_ascii=False, separators=(",", ":")
).encode("utf-8")
payload_hash = hashlib.sha256(payload_bytes).hexdigest()
if payload_hash != IMMUTABLE_SOURCE_SHA256:
    errors.append(
        f"[原文不変] source payload SHA256={payload_hash} expected={IMMUTABLE_SOURCE_SHA256}"
    )

# 全29問、公式正答、翻訳・解説、marker規則。
all_questions = collect_questions(data)
numbers = [q["number"] for q, _ in all_questions]
if numbers != list(range(1, 30)):
    errors.append(f"[設問] numbers={numbers}")

analysis_lengths = []
for q, corpus in all_questions:
    n = q["number"]
    if q.get("answer") != OFFICIAL_READING[n]:
        errors.append(f"[正答] Q{n}: {q.get('answer')} != {OFFICIAL_READING[n]}")
    if len(q.get("choices", [])) != 4 or len(q.get("choiceTranslations", [])) != 4:
        errors.append(f"[選択肢] Q{n}: choices/choiceTranslations != 4")
    if not 1 <= q.get("answer", 0) <= 4:
        errors.append(f"[正答] Q{n}: out of range")
    ca = q.get("choiceAnalysis", [])
    if len(ca) != 4:
        errors.append(f"[解説] Q{n}: choiceAnalysis={len(ca)} != 4")
        continue
    analysis_lengths.extend(map(len, ca))
    if n <= 15:
        for i, text in enumerate(ca, 1):
            expected_marker = "✅" if i == q["answer"] else "❌"
            if not text.startswith(expected_marker):
                errors.append(f"[marker] Q{n} choice{i}: expected {expected_marker}")
    else:
        for i, text in enumerate(ca, 1):
            if text.startswith(("✅", "❌", "○")):
                errors.append(f"[marker] Q{n} choice{i}: leading marker forbidden")
            has_correct = "→正解。💡" in text
            if has_correct != (i == q["answer"]):
                errors.append(f"[marker] Q{n} choice{i}: correct marker mismatch")
    if not q.get("grammar"):
        errors.append(f"[文法] Q{n}: missing")
    if n <= 20:
        if not q.get("text") or not q.get("translation"):
            errors.append(f"[対訳] Q{n}: text/translation missing")
        if f"( {n} )" not in q.get("text", ""):
            errors.append(f"[空所] Q{n}: English blank missing")
        if f"( {n} )" not in q.get("translation", ""):
            errors.append(f"[空所] Q{n}: Japanese blank missing")
        answer_ja = q.get("choiceTranslations", [""] * 4)[q["answer"] - 1]
        answer_ja = re.sub(r"[～（）()・\s]", "", answer_ja)
        translation_ja = re.sub(r"[～（）()・\s]", "", q.get("translation", ""))
        if len(answer_ja) >= 3 and answer_ja in translation_ja:
            errors.append(f"[答え漏洩] Q{n}: correct Japanese choice appears in translation")
    else:
        evidence = q.get("sourceEvidence", [])
        if not evidence:
            errors.append(f"[根拠] Q{n}: sourceEvidence missing")
        for phrase in evidence:
            if not corpus or phrase not in corpus:
                errors.append(f"[根拠] Q{n}: not in source: {phrase!r}")

if analysis_lengths:
    avg_length = sum(analysis_lengths) / len(analysis_lengths)
    if avg_length > 60:
        errors.append(f"[簡潔性] choiceAnalysis average={avg_length:.1f} > 60")
    if max(analysis_lengths) > 100:
        errors.append(f"[簡潔性] choiceAnalysis max={max(analysis_lengths)} > 100")

# 長文対訳は英日ともparagraphs/translationsを漏れなく一度ずつ覆う。
passages = [p for sec in data["sections"] for p in sec.get("passages", [])]
if {p["title"] for p in passages} != set(EXPECTED_PASSAGES):
    errors.append("[長文] passage titles mismatch")
for passage in passages:
    title = passage["title"]
    expected_paragraphs, expected_pairs = EXPECTED_PASSAGES[title]
    if len(passage.get("paragraphs", [])) != expected_paragraphs:
        errors.append(f"[長文] {title}: paragraph count")
    if len(passage.get("translations", [])) != expected_paragraphs:
        errors.append(f"[長文] {title}: translation count")
    pairs = passage.get("sentencePairs", [])
    if len(pairs) != expected_pairs:
        errors.append(f"[長文] {title}: sentencePairs={len(pairs)} != {expected_pairs}")
    for i, pair in enumerate(pairs, 1):
        if not isinstance(pair, list) or len(pair) != 2 or not all(pair):
            errors.append(f"[長文] {title}: invalid pair {i}")
    pair_en = compact(" ".join(pair[0] for pair in pairs if len(pair) == 2))
    source_en = compact(" ".join(passage.get("paragraphs", [])))
    if pair_en != source_en:
        errors.append(f"[長文] {title}: English sentencePairs are not full/ordered coverage")
    pair_ja = compact(" ".join(pair[1] for pair in pairs if len(pair) == 2))
    source_ja = compact(" ".join(passage.get("translations", [])))
    if pair_ja != source_ja:
        errors.append(f"[長文] {title}: Japanese sentencePairs are not full/ordered coverage")

# 語彙40件と全160フィールド、80音声参照。
vocab = data.get("vocabulary", [])
if len(vocab) != 40:
    errors.append(f"[語彙] count={len(vocab)} != 40")
by_word = {v.get("word"): v for v in vocab}
if set(by_word) != set(EXPECTED_VOCAB):
    errors.append("[語彙] headword set mismatch")
if len(by_word) != len(vocab):
    errors.append("[語彙] duplicate headword")
for word, (meaning, pos) in EXPECTED_VOCAB.items():
    item = by_word.get(word, {})
    if (item.get("meaning"), item.get("pos")) != (meaning, pos):
        errors.append(f"[語彙] {word}: meaning/pos mismatch")
    for key in ("word", "meaning", "pos", "level", "example", "distractors", "wordAudio", "exampleAudio"):
        if not item.get(key):
            errors.append(f"[語彙] {word}: missing {key}")
    if len(item.get("distractors", [])) != 3 or len(set(item.get("distractors", []))) != 3:
        errors.append(f"[語彙] {word}: distractors must be 3 unique items")
    if item.get("meaning") in item.get("distractors", []):
        errors.append(f"[語彙] {word}: correct meaning leaks into distractors")
    for audio_key in ("wordAudio", "exampleAudio"):
        ref = item.get(audio_key, "")
        audio_path = BASE / Path(ref.replace("/", os.sep))
        if not ref.endswith(".mp3") or not audio_path.is_file() or audio_path.stat().st_size < 500:
            errors.append(f"[語彙音声] {word}: invalid {audio_key}={ref}")

# Focus Practiceの出典、構造、本文整合、音声。
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
if [fp.get("id") for fp in focus_points] != ["fp1", "fp2", "fp3", "fp4", "fp5"]:
    errors.append("[Focus] ids must be fp1..fp5")

filled_corpus = " ".join(" ".join(p["paragraphs"]) for p in passages)
filled_corpus = filled_corpus.replace("Max ( 21 ).", "Max did everything that he could.")
filled_corpus = filled_corpus.replace("Max was ( 22 ).", "Max was surprised to hear that.")
for fp in focus_points:
    fid = fp.get("id", "?")
    for key in (
        "id", "title", "subtitle", "explanation", "sourceQuote", "sourceLocation",
        "examples", "practicePassage", "practiceQuestions", "highlightPatterns",
        "highlightColor", "highlightLabel",
    ):
        if not fp.get(key):
            errors.append(f"[Focus] {fid}: missing {key}")
    pp = fp.get("practicePassage", {})
    en = pp.get("en", "")
    if not en.startswith("[出典:") or not pp.get("ja"):
        errors.append(f"[Focus] {fid}: practicePassage source/translation missing")
    for line in en.splitlines():
        if not line or line.startswith("[出典:"):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            if sentence and sentence not in filled_corpus:
                errors.append(
                    f"[Focus] {fid}: practice English not in source: {sentence[:60]!r}"
                )
    for pattern in fp.get("highlightPatterns", []):
        if pattern not in en:
            errors.append(f"[Focus] {fid}: highlight missing from passage: {pattern!r}")
    questions = fp.get("practiceQuestions", [])
    if len(questions) < 4:
        errors.append(f"[Focus] {fid}: practiceQuestions < 4")
    for qa in questions:
        if not qa.get("q") or not qa.get("a"):
            errors.append(f"[Focus] {fid}: empty practice question/answer")
        if "避え" in qa.get("a", ""):
            errors.append(f"[Focus] {fid}: typo 避え")
    audio_ref = pp.get("audioFile", "")
    audio_path = BASE / Path(audio_ref.replace("/", os.sep))
    if not audio_ref.endswith(".mp3") or not audio_path.is_file() or audio_path.stat().st_size < 500:
        errors.append(f"[Focus音声] {fid}: invalid {audio_ref}")

# リスニング公式キーと原本音源参照。
if sum(len(x) for x in OFFICIAL_LISTENING.values()) != 30:
    errors.append("[リスニング] official key count != 30")
if any(ans not in (1, 2, 3, 4) for part in OFFICIAL_LISTENING.values() for ans in part):
    errors.append("[リスニング] official key contains invalid answer")
if SOURCE_AUDIO.is_dir():
    tracks = sorted(SOURCE_AUDIO.glob("*.mp3"))
    track_numbers = []
    for track in tracks:
        match = re.match(r"(\d+)\s", track.name)
        if match:
            track_numbers.append(int(match.group(1)))
        if track.stat().st_size < 100_000:
            errors.append(f"[リスニング音源] too small: {track.name}")
    if track_numbers != list(range(37, 73)):
        errors.append(f"[リスニング音源] tracks={track_numbers} expected=37..72")
    else:
        notes.append("[リスニング音源] 37〜72の36ファイルを確認")
else:
    notes.append(f"[リスニング音源] ローカル音源なし（スキップ）: {SOURCE_AUDIO}")

avg_analysis = sum(analysis_lengths) / len(analysis_lengths) if analysis_lengths else 0.0
print(
    f"questions={len(all_questions)} vocab={len(vocab)} passages={len(passages)} "
    f"focus={len(focus_points)} analysis_avg={avg_analysis:.1f} errors={len(errors)}"
)
for note in notes:
    print("  [INFO]", note)
for error in errors:
    print("  [ERROR]", error)
if errors:
    sys.exit(1)
print("AUDIT OK: 2026-1-sat 準2級")
