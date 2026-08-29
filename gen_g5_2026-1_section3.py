# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検5級 data.json
大問3（並べ替え）Q21〜25 — 解説付き
文の型ごとに解説の切り口を変えて単調さを避ける。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1-sat", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "sentence-order",
    "instruction": "次の(21)から(25)までの日本文の意味を表すように①から④までを並べかえて( )の中に入れなさい。そして、1番目と3番目にくるものの最も適切な組合せを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。※ただし、( )の中では、文のはじめにくる語も小文字になっています。",
    "questions": [
        {
            "number": 21,
            "text": "私の姉は毎日お皿を洗います。",
            "choices": ["③ ─ ②", "④ ─ ③", "① ─ ④", "② ─ ③"],
            "answer": 4,
            "words": ["the dishes", "my", "washes", "sister"],
            "correctOrder": [2, 4, 3, 1],
            "framePrefix": "",
            "frameSuffix": "every day.",
            "answerSlots": [1, 3],
            "grammar": "【主語＋三人称単数】完成文は「My sister washes the dishes every day.」。主語 my sister のあとに動詞 washes（三人称単数）。1番目 my、3番目 washes。",
            "grammarSimple": "できあがりは「My sister washes the dishes every day.」。おねえちゃんがおさらをあらう、だよ。1ばんめ my、3ばんめ washes！",
            "choiceAnalysis": [
                "「③─②」＝washes と my。文頭が washes になり「洗う 私の…」となり、主語が後ろに回って不自然。",
                "「④─③」＝sister と washes。my が抜けて「姉は洗う…」だけでは「私の姉」の意味にならない。",
                "「①─④」＝the dishes と sister。文頭が「お皿」になり、主語・動詞の語順が成立しない。",
                "○「②─③」＝my と washes。my sister washes the dishes every day. で「私の姉は毎日お皿を洗う」。",
            ],
            "choiceAnalysisSimple": [
                "「washes」からはじまるとへんな文になるよ。",
                "「my」がないと「わたしの」にならないよ。",
                "「おさら」からはじまると文にならないよ。",
                "○「my」と「washes」でぴったり！My sister washes...！",
            ],
            "questionAudio": "audio/q21.mp3",
            "translation": "私の姉は毎日お皿を洗います。",
        },
        {
            "number": 22,
            "text": "ビルと私は冬にスキーに行きます。",
            "choices": ["② ─ ③", "④ ─ ③", "① ─ ④", "③ ─ ②"],
            "answer": 4,
            "words": ["skiing", "go", "and", "I"],
            "correctOrder": [3, 4, 2, 1],
            "framePrefix": "Bill",
            "frameSuffix": "in winter.",
            "answerSlots": [1, 3],
            "grammar": "【and でつなぐ主語】Bill のあとに and I で「ビルと私」。動詞は go、go skiing＝「スキーに行く」がセット。1番目 and、3番目 go。",
            "grammarSimple": "できあがりは「Bill and I go skiing in winter.」。ビルとわたしがふゆにスキーにいく、だよ。1ばんめ and、3ばんめ go！",
            "choiceAnalysis": [
                "「②─③」＝go と and。Bill go and ... となり、主語 and I が続かない。",
                "「④─③」＝I と and。Bill I and ... となり、and でつなぐ形にならない。",
                "「①─④」＝skiing と I。Bill skiing ... から始まり、go skiing の動詞 go が抜ける。",
                "○「③─②」＝and と go。Bill and I go skiing in winter. で自然な文。",
            ],
            "choiceAnalysisSimple": [
                "「go」が1ばんめだと「Bill go...」になってへんよ。",
                "「I」がつぎに来ると「Bill I...」になってへんよ。",
                "「skiing」からはじまると go がたりないよ。",
                "○「and」と「go」でぴったり！Bill and I go skiing！",
            ],
            "questionAudio": "audio/q22.mp3",
            "translation": "ビルと私は冬にスキーに行きます。",
        },
        {
            "number": 23,
            "text": "学校にかさを持って行きなさい。",
            "choices": ["④ ─ ③", "② ─ ④", "① ─ ③", "② ─ ①"],
            "answer": 3,
            "words": ["take", "school", "to", "your umbrella"],
            "correctOrder": [1, 4, 3, 2],
            "framePrefix": "",
            "frameSuffix": ".",
            "answerSlots": [1, 3],
            "grammar": "【命令文】文頭は動詞 take。「take ～ to ～」＝「～を～に持っていきなさい」。1番目 take、3番目 to。",
            "grammarSimple": "できあがりは「Take your umbrella to school.」。がっこうにかさをもっていきなさい、だよ。1ばんめ take、3ばんめ to！",
            "choiceAnalysis": [
                "「④─③」＝your umbrella と to。文頭が名詞になり、命令文の動詞 take が先頭に来ない。",
                "「②─④」＝school と your umbrella。school your umbrella ... となり、命令の形にならない。",
                "○「①─③」＝take と to。Take your umbrella to school. で「学校にかさを持っていきなさい」。",
                "「②─①」＝school と take。school take ... となり、to school の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "「かさ」からはじまるとめいれいぶんじゃないよ。",
                "「school」からはじまると文にならないよ。",
                "○「take」と「to」でぴったり！Take ... to school.！",
                "「school take」はへんなじゅんばんだよ。",
            ],
            "questionAudio": "audio/q23.mp3",
            "translation": "学校にかさを持って行きなさい。",
        },
        {
            "number": 24,
            "text": "マイクのサッカーチームには3人のコーチがいます。",
            "choices": ["① ─ ②", "④ ─ ②", "② ─ ③", "③ ─ ④"],
            "answer": 3,
            "words": ["coaches", "soccer team", "three", "has"],
            "correctOrder": [2, 4, 3, 1],
            "framePrefix": "Mike's",
            "frameSuffix": ".",
            "answerSlots": [1, 3],
            "grammar": "【三単現 has】Mike's soccer team が主語。has three coaches＝「3人のコーチがいる」。1番目 soccer team、3番目 three。",
            "grammarSimple": "できあがりは「Mike's soccer team has three coaches.」。マイクのチームにコーチが3にんいる、だよ。1ばんめ soccer team、3ばんめ three！",
            "choiceAnalysis": [
                "「①─②」＝coaches と soccer team。Mike's coaches soccer team ... となり、主語と動詞の形が合わない。",
                "「④─②」＝has と soccer team。Mike's has soccer team ... となり、主語が抜ける。",
                "○「②─③」＝soccer team と three。Mike's soccer team has three coaches. で文が完成。",
                "「③─④」＝three と has。Mike's three has coaches ... となり、語順が逆になる。",
            ],
            "choiceAnalysisSimple": [
                "「coaches」からはじまると文にならないよ。",
                "「has」がすぐ来ると「Mike's has...」でへんよ。",
                "○「soccer team」と「three」でぴったり！has three coaches！",
                "「three has」はじゅんばんがちがうよ。",
            ],
            "questionAudio": "audio/q24.mp3",
            "translation": "マイクのサッカーチームには3人のコーチがいます。",
        },
        {
            "number": 25,
            "text": "今日は学校がありません。",
            "choices": ["④ ─ ②", "① ─ ②", "② ─ ①", "③ ─ ④"],
            "answer": 4,
            "words": ["don't", "school", "we", "have"],
            "correctOrder": [3, 1, 4, 2],
            "framePrefix": "",
            "frameSuffix": "today.",
            "answerSlots": [1, 3],
            "grammar": "【否定文 don't have】主語 we のあとに don't have school＝「学校がない」。have school＝「授業がある」の否定。1番目 we、3番目 have。",
            "grammarSimple": "できあがりは「We don't have school today.」。きょうはがっこうがない、だよ。1ばんめ we、3ばんめ have！",
            "choiceAnalysis": [
                "「④─②」＝have と school。have ?? school ?? となり、主語 we と否定 don't が抜ける。",
                "「①─②」＝don't と school。don't ?? school ?? となり、主語 we が先頭に来ない。",
                "「②─①」＝school と don't。school don't ... となり、We don't have の形にならない。",
                "○「③─④」＝we と have。We don't have school today. で「今日は学校がない」。",
            ],
            "choiceAnalysisSimple": [
                "「have」からはじまるとだれが？がわからないよ。",
                "「don't」からはじまると「だれが？」がたりないよ。",
                "「school don't」はへんな文だよ。",
                "○「we」と「have」でぴったり！We don't have school today.！",
            ],
            "questionAudio": "audio/q25.mp3",
            "translation": "今日は学校がありません。",
        },
    ],
}

# 2026-08 content audit: generate the fully checked slot explanations from the
# immutable question fields.  The former hand-written draft did not reproduce
# the reviewed data.json and could silently restore less precise explanations.
_CIRCLED_TO_NUMBER = {"①": 1, "②": 2, "③": 3, "④": 4}
_NUMBER_TO_CIRCLED = {value: key for key, value in _CIRCLED_TO_NUMBER.items()}
_ORDER_REASON = {
    21: "my sister（私の姉）を主語にし、三人称単数の動詞 washes、目的語 the dishes の順に並べます。",
    22: "Bill のあとを and I と続けて主語を作り、go skiing（スキーに行く）を続けます。",
    23: "命令文なので動詞 take で始め、take ～ to ～（～を～へ持って行く）の順に並べます。",
    24: "Mike's のあとに soccer team を置いて主語を作り、三人称単数の動詞 has、three coaches の順に並べます。",
    25: "主語 we のあとに don't have を置き、have school（授業がある）を否定する形にします。",
}
_COMPLETED = {
    21: "My sister washes the dishes every day.",
    22: "Bill and I go skiing in winter.",
    23: "Take your umbrella to school.",
    24: "Mike's soccer team has three coaches.",
    25: "We don't have school today.",
}


def _apply_audited_slot_explanations(question):
    number = question["number"]
    completed = _COMPLETED[number]
    order = question["correctOrder"]
    words = question["words"]
    first_number, third_number = order[0], order[2]
    first_circle = _NUMBER_TO_CIRCLED[first_number]
    third_circle = _NUMBER_TO_CIRCLED[third_number]
    first_word = words[first_number - 1]
    third_word = words[third_number - 1]
    order_labels = "".join(_NUMBER_TO_CIRCLED[item] for item in order)
    ordered_words = " → ".join(words[item - 1] for item in order)

    question["grammar"] = (
        f"日本語は「{question['text']}」。正しい英語は「{completed}」です。"
        f"{_ORDER_REASON[number]}①〜④を正しい順にすると{order_labels}（{ordered_words}）です。"
        f"空所は1番目と3番目なので、1番目＝{first_circle}「{first_word}」、"
        f"3番目＝{third_circle}「{third_word}」。よって答えは{first_circle} ─ {third_circle}です。"
    )
    question["grammarSimple"] = (
        f"いみは「{question['text']}」。ただしい えいごは「{completed}」だよ。"
        f"1ばんめは{first_circle}「{first_word}」、3ばんめは{third_circle}「{third_word}」。"
        f"だから こたえは{first_circle} ─ {third_circle}！"
    )

    detailed = []
    simple = []
    for choice_index, label in enumerate(question["choices"], start=1):
        left_circle, right_circle = label.split(" ─ ")
        left_number = _CIRCLED_TO_NUMBER[left_circle]
        right_number = _CIRCLED_TO_NUMBER[right_circle]
        left_word = words[left_number - 1]
        right_word = words[right_number - 1]
        if choice_index == question["answer"]:
            detailed.append(
                f"○ {label}：1番目＝{left_circle}「{left_word}」、3番目＝{right_circle}「{right_word}」。"
                f"完成文「{completed}」の語順と一致します。"
            )
            simple.append(
                f"○ {label}：1ばんめ{left_circle}「{left_word}」、3ばんめ{right_circle}「{right_word}」でピッタリ！"
            )
        else:
            detailed.append(
                f"{label}：1番目が{left_circle}「{left_word}」、3番目が{right_circle}「{right_word}」になり、"
                f"正しい語順「{completed}」になりません。正しくは1番目＝{first_circle}「{first_word}」、"
                f"3番目＝{third_circle}「{third_word}」です。"
            )
            simple.append(
                f"{label}：1ばんめ{left_circle}「{left_word}」と3ばんめ{right_circle}「{right_word}」だと "
                f"ならびがちがうよ。ただしくは{first_circle}「{first_word}」と{third_circle}「{third_word}」だね。"
            )
    question["choiceAnalysis"] = detailed
    question["choiceAnalysisSimple"] = simple


for question in section3["questions"]:
    _apply_audited_slot_explanations(question)

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data.get("sections", [])
new_sections = []
replaced = False
for sec in sections:
    if sec.get("name") == "大問3":
        new_sections.append(section3)
        replaced = True
    else:
        new_sections.append(sec)
if not replaced:
    out = []
    for sec in sections:
        out.append(sec)
        if sec.get("name") == "大問2":
            out.append(section3)
    new_sections = out

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section3 ({len(section3['questions'])} questions) to {DATA_PATH}")
