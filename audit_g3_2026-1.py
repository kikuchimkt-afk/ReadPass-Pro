# -*- coding: utf-8 -*-
"""2026-1-sat 3級 総合監査 — 公式解答・原本・解説・音声・FP"""
import ast
import hashlib
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

EXPECTED_METADATA = {
    "grade": "grade3",
    "year": 2026,
    "session": "2026-1-sat",
    "title": "英検3級 2026年度 第1回（土曜準会場）",
    "exam": "2026-1-sat",
}

EXPECTED_SECTION_META = [
    {
        "name": "大問1",
        "nameEn": "Part 1",
        "type": "vocabulary",
        "instruction": "次の(1)から(15)までの( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    },
    {
        "name": "大問2",
        "nameEn": "Part 2",
        "type": "vocabulary",
        "instruction": "次の(16)から(20)までの会話について、( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    },
    {
        "name": "大問3",
        "nameEn": "Part 3",
        "type": "reading-comprehension",
        "instruction": "次のA，B，Cの内容に関して，質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    },
]

EXPECTED_WRITING = {
    "section4": {
        "type": "email-reply",
        "title": "ライティング（Eメール）",
        "prompt": {
            "from": "James",
            "body": (
                "Hi,\n"
                "Thank you for your e-mail.\n"
                "Your mother says that you often write letters to your grandparents.\n"
                "I have some questions. How many times a year do you write letters to them? "
                "And what do you write about in your letters?\n"
                "Your friend,\n"
                "James"
            ),
        },
        "sampleAnswer": (
            "I write letters to my grandparents four times a year. "
            "I write about my school life. "
            "I hope they enjoy reading my letters."
        ),
    },
    "section5": {
        "type": "composition",
        "title": "ライティング（英作文）",
        "question": "Do you like to invite friends to your home?",
        "sampleAnswer": (
            "Yes, I do. I have two reasons. First, I like to play video games with my friends at home. "
            "Second, it is fun for me to do our homework together in my room."
        ),
    },
}

SOURCE_PAYLOAD_SHA256 = "6489520fb8490e5cec0c3aa843590aa5569ddc4269b27ee5c823342f8169d13e"
EXPECTED_PAIR_COUNTS = {"A": 12, "B": 34, "C": 18}
EXPECTED_VOCAB_WORDS = [
    "kite", "pass", "boring", "tired", "exercise",
    "market", "college", "take care of", "himself", "wait for",
    "feel", "look around", "painted", "taught", "to practice",
    "help", "ice-skating", "wear", "stomachache", "say hello to",
    "ingredients", "vegetables", "website",
    "performance", "practiced", "nervous", "comedy",
    "indoors", "championships", "athlete",
]

VOCAB_EXAMPLE_FORMS = {
    # 見出し語は原形、出典文は過去形。出典文を改変せず活用形を許容する。
    "look around": ("look around", "looks around", "looked around", "looking around"),
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


def canonical_sha256(value):
    blob = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def question_payload(items, field):
    return [
        {
            "number": q["number"],
            field: q[field],
            "choices": q["choices"],
            "answer": OFFICIAL_READING[q["number"]],
        }
        for q in items
    ]


def passage_payload(passage):
    out = {
        key: passage[key]
        for key in ("label", "title", "format", "paragraphs")
        if key in passage
    }
    if "emails" in passage:
        out["emails"] = [
            {"meta": email["meta"], "body": email["body"]}
            for email in passage["emails"]
        ]
    out["questions"] = question_payload(passage["questions"], "question")
    return out


def extract_source_payload():
    src_path = os.path.join(BASE, "gen_g3_2026-1.py")
    tree = ast.parse(open(src_path, encoding="utf-8").read())
    wanted = {
        "section1_questions",
        "section2_questions",
        "passage_3a",
        "passage_3b",
        "passage_3c",
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
    payload = {
        "sectionMeta": EXPECTED_SECTION_META,
        "section1": question_payload(values["section1_questions"], "text"),
        "section2": question_payload(values["section2_questions"], "text"),
        "passages": [
            passage_payload(values[name])
            for name in ("passage_3a", "passage_3b", "passage_3c")
        ],
        "writing": EXPECTED_WRITING,
    }
    return payload, values


def extract_data_source_payload(data, source_values):
    data_sections = {section["name"]: section for section in data["sections"]}
    data_passages = {
        passage["label"]: passage
        for passage in data_sections["大問3"]["passages"]
    }

    def selected_passage(source_passage):
        current = data_passages[source_passage["label"]]
        out = {
            key: current[key]
            for key in ("label", "title", "format", "paragraphs")
            if key in source_passage
        }
        if "emails" in source_passage:
            out["emails"] = [
                {"meta": email["meta"], "body": email["body"]}
                for email in current["emails"]
            ]
        out["questions"] = [
            {
                "number": q["number"],
                "question": q["question"],
                "choices": q["choices"],
                "answer": q["answer"],
            }
            for q in current["questions"]
        ]
        return out

    return {
        "sectionMeta": [
            {
                key: section[key]
                for key in ("name", "nameEn", "type", "instruction")
            }
            for section in data["sections"]
        ],
        "section1": [
            {
                "number": q["number"],
                "text": q["text"],
                "choices": q["choices"],
                "answer": q["answer"],
            }
            for q in data_sections["大問1"]["questions"]
        ],
        "section2": [
            {
                "number": q["number"],
                "text": q["text"],
                "choices": q["choices"],
                "answer": q["answer"],
            }
            for q in data_sections["大問2"]["questions"]
        ],
        "passages": [
            selected_passage(source_values[name])
            for name in ("passage_3a", "passage_3b", "passage_3c")
        ],
        "writing": data["writing"],
    }


all_qs = collect_questions(d)
seen = {q["number"] for _, q in all_qs}
if len(all_qs) != 30 or seen != set(range(1, 31)):
    issues.append(f"[構造] reading questions={len(all_qs)} numbers={sorted(seen)}")

# ---- 0. メタデータ ----
for key, expected in EXPECTED_METADATA.items():
    if d.get(key) != expected:
        issues.append(f"[メタ] {key}={d.get(key)!r} != {expected!r}")

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
        if norm(q.get("text", "")).count("( )") != 1:
            issues.append(f"[空所] Q{n}: 英文の空所数が1ではない")
        if norm(q.get("translation", "")).count("( )") != 1:
            issues.append(f"[空所] Q{n}: 和訳が正答を埋めている、または空所数が不正")
        for field in ("choiceTranslations", "choiceAnalysis", "choiceAnalysisSimple"):
            values = q.get(field, [])
            if len(values) != 4:
                issues.append(f"[解説] Q{n}: {field}数={len(values)}")
                continue
            if field.startswith("choiceAnalysis"):
                marks = [
                    i + 1 for i, text in enumerate(values) if text.startswith("○")
                ]
                if marks != [q["answer"]]:
                    issues.append(
                        f"[解説] Q{n}: {field}の○位置={marks} answer={q['answer']}"
                    )
                if any(text.startswith(("×", "✅", "❌")) for text in values):
                    issues.append(f"[解説] Q{n}: {field}に規約外マーカー")

# ---- 4. 大問3 リッチフィールド ----
for p in d["sections"][2]["passages"]:
    if len(p.get("paragraphs", [])) != len(p.get("translations", [])):
        issues.append(f"[構造] 3{p['label']}: paragraphs/translations不一致")
    if p.get("emails"):
        corpus = " ".join(email.get("body", "") for email in p["emails"])
    else:
        corpus = " ".join(p.get("paragraphs", []))

    pairs = p.get("sentencePairs", [])
    expected_pair_count = EXPECTED_PAIR_COUNTS[p["label"]]
    if len(pairs) != expected_pair_count:
        issues.append(
            f"[対訳] 3{p['label']}: sentencePairs={len(pairs)} != {expected_pair_count}"
        )
    pair_english = []
    for i, pair in enumerate(pairs, 1):
        if (
            not isinstance(pair, list)
            or len(pair) != 2
            or not all(isinstance(text, str) and text.strip() for text in pair)
        ):
            issues.append(f"[対訳] 3{p['label']} pair{i}: [英文, 和訳] ではない")
            continue
        pair_english.append(pair[0])
    if norm(" ".join(pair_english)) != norm(corpus):
        issues.append(f"[対訳] 3{p['label']}: sentencePairsが原文全文を覆っていない")

    for q in p.get("questions", []):
        n = q["number"]
        for key in ("questionTranslation", "grammar", "grammarSimple",
                    "choiceAnalysis", "choiceAnalysisSimple", "choiceTranslations"):
            if not q.get(key):
                issues.append(f"[解説] Q{n}: missing {key}")
        ev = q.get("sourceEvidence", "")
        if ev and ev not in corpus:
            issues.append(f"[根拠] Q{n}: sourceEvidenceが本文にない: {ev[:60]}")
        if not q.get("sourceEvidence"):
            issues.append(f"[根拠] Q{n}: sourceEvidence未設定")
        for field in (
            "choices", "choiceTranslations", "choiceAnalysis", "choiceAnalysisSimple"
        ):
            values = q.get(field, [])
            if len(values) != 4:
                issues.append(f"[解説] Q{n}: {field}数={len(values)}")
                continue
            if field.startswith("choiceAnalysis"):
                marks = [
                    i + 1 for i, text in enumerate(values) if text.startswith("○")
                ]
                if marks != [q["answer"]]:
                    issues.append(
                        f"[解説] Q{n}: {field}の○位置={marks} answer={q['answer']}"
                    )
                if any(text.startswith(("×", "✅", "❌")) for text in values):
                    issues.append(f"[解説] Q{n}: {field}に規約外マーカー")

# ---- 5. 原本 gen_g3_2026-1.py との完全一致 ----
source_payload, source_values = extract_source_payload()
source_hash = canonical_sha256(source_payload)
if source_hash != SOURCE_PAYLOAD_SHA256:
    issues.append(
        f"[原本] generatorの原文スナップショット不一致: {source_hash}"
    )
data_source_payload = extract_data_source_payload(d, source_values)
if data_source_payload != source_payload:
    issues.append("[原本] 英文・選択肢・正答・本文・メール・ライティングが原本と不一致")

# ---- 6. vocabulary ----
vocab = d.get("vocabulary", [])
if len(vocab) != 30:
    issues.append(f"[語彙] count={len(vocab)} != 30")
if [item.get("word") for item in vocab] != EXPECTED_VOCAB_WORDS:
    issues.append("[語彙] 語順または必須語が不一致")
meanings = []
for i, v in enumerate(vocab, 1):
    for key in (
        "word", "meaning", "pos", "level", "source",
        "example", "distractors", "wordAudio",
    ):
        if not v.get(key):
            issues.append(f"[語彙] #{i}: missing {key}")
    m = v.get("meaning", "")
    if m in meanings:
        issues.append(f"[語彙] 意味重複: {m}")
    meanings.append(m)
    if v.get("level") != "3級":
        issues.append(f"[語彙] {v.get('word')}: level={v.get('level')}")
    distractors = v.get("distractors", [])
    if len(distractors) != 3 or len(set(distractors)) != 3:
        issues.append(f"[語彙] {v.get('word')}: distractors不正")
    if m in v.get("distractors", []):
        issues.append(f"[語彙] {v['word']}: distractorsに正解意味")
    word = v.get("word", "").lower()
    example = v.get("example", "").lower()
    forms = VOCAB_EXAMPLE_FORMS.get(word, (word,))
    if not any(form in example for form in forms):
        issues.append(f"[語彙] {v.get('word')}: exampleに見出し語がない")
    rel = v.get("wordAudio", "")
    if not rel:
        issues.append(f"[音声] vocab {v.get('word')}: wordAudio欠落")
    else:
        fp = os.path.join(ADIR, rel.replace("/", os.sep))
        if not os.path.isfile(fp) or os.path.getsize(fp) < 500:
            issues.append(f"[音声] vocab {v['word']}: {rel}")

source_counts = {}
for item in vocab:
    source_counts[item.get("source")] = source_counts.get(item.get("source"), 0) + 1
if source_counts != {"大問1": 15, "大問2": 5, "大問3A": 3, "大問3B": 4, "大問3C": 3}:
    issues.append(f"[語彙] source内訳不正: {source_counts}")

known_vocab = {item.get("word"): item for item in vocab}
for word, meaning in {
    "college": "大学",
    "himself": "彼自身（by himself で「彼一人で」）",
    "wait for": "待つ（for＋時間で期間）",
    "wear": "身につける（帽子をかぶる）",
}.items():
    if known_vocab.get(word, {}).get("meaning") != meaning:
        issues.append(f"[語彙] {word}: meaning監査値と不一致")

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
if [fp.get("id") for fp in fps] != ["fp1", "fp2", "fp3", "fp4"]:
    issues.append("[FP] idまたは順序が不正")

for fp in fps:
    fid = fp.get("id", "?")
    for key in (
        "title", "subtitle", "explanation", "explanationSimple",
        "sourceQuote", "sourceLocation", "highlightPatterns",
        "examples", "practicePassage",
        "practiceQuestions", "practiceQuestionsSimple",
        "sourceQuoteAudio",
    ):
        if not fp.get(key):
            issues.append(f"[FP] {fid}: missing {key}")
    if not 80 <= len(fp.get("explanation", "")) <= 220:
        issues.append(
            f"[FP] {fid}: explanation長={len(fp.get('explanation', ''))}"
        )
    if not 35 <= len(fp.get("explanationSimple", "")) <= 160:
        issues.append(
            f"[FP] {fid}: explanationSimple長={len(fp.get('explanationSimple', ''))}"
        )

    pp = fp.get("practicePassage", {})
    pp_text = pp.get("en", "")
    search = corpus_all + " " + pp_text
    for pat in fp.get("highlightPatterns", []):
        if pat not in search:
            issues.append(f"[FP] {fid}: highlight不在: {pat[:50]}")
    for key in ("en", "ja", "source", "audioFile"):
        if not pp.get(key):
            issues.append(f"[FP] {fid}: practicePassage missing {key}")
    af = pp.get("audioFile")
    if af:
        fpth = os.path.join(ADIR, af.replace("/", os.sep))
        if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fid}: {af}")
    examples = fp.get("examples", [])
    if len(examples) != 3:
        issues.append(f"[FP] {fid}: examples={len(examples)} != 3")
    for j, ex in enumerate(examples):
        for key in ("en", "ja", "note", "noteSimple", "audio"):
            if not ex.get(key):
                issues.append(f"[FP] {fid} ex{j+1}: missing {key}")
        au = ex.get("audio")
        if au:
            fpth = os.path.join(ADIR, au.replace("/", os.sep))
            if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
                issues.append(f"[音声] {fid} ex{j+1}: {au}")
    for field in ("practiceQuestions", "practiceQuestionsSimple"):
        questions = fp.get(field, [])
        if len(questions) != 3:
            issues.append(f"[FP] {fid}: {field}={len(questions)} != 3")
        for j, question in enumerate(questions, 1):
            if not question.get("q") or not question.get("a"):
                issues.append(f"[FP] {fid}: {field}[{j}] q/a欠落")
    source_audio = fp.get("sourceQuoteAudio")
    if source_audio:
        fpth = os.path.join(ADIR, source_audio.replace("/", os.sep))
        if not os.path.isfile(fpth) or os.path.getsize(fpth) < 500:
            issues.append(f"[音声] {fid}: {source_audio}")

data_blob = json.dumps(d, ensure_ascii=False)
for stale in (
    "wait for ～＝「～を待つ」",
    "お母さんと弟も来ます",
    "しつだんした話",
    "ねむれって",
    "おくのなか",
    "いちばんだけのスポーツ",
    "思い出してもらおうと思って",
):
    if stale in data_blob:
        issues.append(f"[表現] 古い誤説明・不自然表現が残存: {stale}")

analysis_texts = [
    text
    for _, question in all_qs
    for text in question.get("choiceAnalysis", [])
]
if analysis_texts:
    average_length = sum(map(len, analysis_texts)) / len(analysis_texts)
    if average_length > 50:
        issues.append(f"[解説] choiceAnalysis平均長={average_length:.1f} > 50")
    if max(map(len, analysis_texts)) > 100:
        issues.append(f"[解説] choiceAnalysis最大長={max(map(len, analysis_texts))} > 100")

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
if list(d.keys()) != list(EXPECTED_KEYS):
    issues.append(f"[構造] トップレベルキーまたは順序が不正: {list(d.keys())}")

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
