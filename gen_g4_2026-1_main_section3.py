# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
大問3（並べ替え）Q21〜25 — 解説付き
一次ソース: 2026-1(本会場）/4級.pdf / 4級解答.pdf
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def mark_ca(items, answer):
    out = []
    for i, text in enumerate(items):
        cleaned = re.sub(r"^[○✅❌]\s*", "", text)
        prefix = "✅" if i + 1 == answer else "❌"
        out.append(f"{prefix} {cleaned}")
    return out

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "sentence-order",
    "instruction": "次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて( )の中に入れなさい。",
    "questions": [
        {
            "number": 21,
            "text": "なぜあなたは今朝、そんなに早く起きたのですか。",
            "choices": ["①−②", "⑤−③", "③−⑤", "④−①"],
            "answer": 2,
            "words": ["you", "up", "get", "why", "did"],
            "correctOrder": [4, 5, 1, 3, 2],
            "framePrefix": "",
            "frameSuffix": "so early this morning?",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「Why did you get up so early this morning?」になります。why did you ...?＝「なぜあなたは〜したの？」。空所は2語目 did（⑤）と4語目 get（③）。",
            "grammarSimple": "正しい文は「Why did you get up so early this morning?」。なぜけさそんなにはやくおきたの？2ばんめ did、4ばんめ get！",
            "choiceAnalysis": [
                "「①−②」だと you up ... となり、Why did you get up の形にならない。",
                "○「⑤−③」＝did と get。Why did you get up so early this morning? が自然な疑問文。",
                "「③−⑤」だと get did ... となり、語順が合わない。",
                "「④−①」だと why you ... となり、did が抜けて文が成立しない。",
            ],
            "choiceAnalysisSimple": [
                "「①−②」は Why did you get up にならないよ。",
                "○「⑤−③」が正解！Why did you get up? だよ！",
                "「③−⑤」はじゅんばんがちがうよ。",
                "「④−①」は did がたりないよ。",
            ],
            "questionAudio": "audio/q21.mp3",
        },
        {
            "number": 22,
            "text": "今日の午後、あなたに電話してもいいですか。",
            "choices": ["④−③", "①−③", "⑤−①", "③−①"],
            "answer": 1,
            "words": ["this", "may", "you", "I", "call"],
            "correctOrder": [2, 4, 5, 3, 1],
            "framePrefix": "",
            "frameSuffix": "afternoon?",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「May I call you this afternoon?」になります。May I ...?＝「〜してもいいですか？」。空所は2語目 I（④）と4語目 you（③）。",
            "grammarSimple": "正しい文は「May I call you this afternoon?」。きょうのごご、でんわしてもいい？2ばんめ I、4ばんめ you！",
            "choiceAnalysis": [
                "○「④−③」＝I と you。May I call you this afternoon? が丁寧な許可を求める形。",
                "「①−③」だと this you ... となり、May I call の形にならない。",
                "「⑤−①」だと call this ... から始まり、語順が合わない。",
                "「③−①」だと you this ... となり、May I call you の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "○「④−③」が正解！May I call you? だよ！",
                "「①−③」は May I call の形にならないよ。",
                "「⑤−①」はじゅんばんがちがうよ。",
                "「③−①」は May I call you にならないよ。",
            ],
            "questionAudio": "audio/q22.mp3",
        },
        {
            "number": 23,
            "text": "ネパールではたくさんの高い山を見ることができます。",
            "choices": ["④−②", "③−⑤", "④−③", "⑤−③"],
            "answer": 2,
            "words": ["see", "you", "can", "high mountains", "lots of"],
            "correctOrder": [2, 3, 1, 5, 4],
            "framePrefix": "",
            "frameSuffix": "in Nepal.",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「You can see lots of high mountains in Nepal.」になります。can see＝「見ることができる」。空所は2語目 can（③）と4語目 lots of（⑤）。",
            "grammarSimple": "正しい文は「You can see lots of high mountains in Nepal.」。ネパールではたくさんのたかいやまがみえる。2ばんめ can、4ばんめ lots of！",
            "choiceAnalysis": [
                "「④−②」だと high mountains you ... となり、You can see の形にならない。",
                "○「③−⑤」＝can と lots of。You can see lots of high mountains で文が完成。",
                "「④−③」だと high mountains can ... となり、語順が合わない。",
                "「⑤−③」だと lots of can ... となり、can see の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "「④−②」は You can see にならないよ。",
                "○「③−⑤」が正解！You can see lots of ... だよ！",
                "「④−③」はじゅんばんがちがうよ。",
                "「⑤−③」は can see にならないよ。",
            ],
            "questionAudio": "audio/q23.mp3",
        },
        {
            "number": 24,
            "text": "私は毎朝７時に家を出て学校へ向かいます。",
            "choices": ["⑤−③", "③−④", "⑤−②", "③−⑤"],
            "answer": 3,
            "words": ["at", "school", "leave", "for", "home"],
            "correctOrder": [3, 5, 4, 2, 1],
            "framePrefix": "I",
            "frameSuffix": "seven o'clock every morning.",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「I leave home for school at seven o'clock every morning.」になります。leave home for school＝「家を出て学校へ向かう」。空所は2語目 home（⑤）と4語目 school（②）。",
            "grammarSimple": "正しい文は「I leave home for school at seven o'clock every morning.」。まいあさ7じにいえをでてがっこうへ。2ばんめ home、4ばんめ school！",
            "choiceAnalysis": [
                "「⑤−③」だと home leave ... となり、leave home for school の形にならない。",
                "「③−④」だと leave for ... のあと school が来ず、語順がずれる。",
                "○「⑤−②」＝home と school。I leave home for school at ... で文が完成。",
                "「③−⑤」だと leave home の順が逆になり、文として成立しない。",
            ],
            "choiceAnalysisSimple": [
                "「⑤−③」は leave home にならないよ。",
                "「③−④」はじゅんばんがちがうよ。",
                "○「⑤−②」が正解！leave home for school だよ！",
                "「③−⑤」はじゅんばんがちがうよ。",
            ],
            "questionAudio": "audio/q24.mp3",
        },
        {
            "number": 25,
            "text": "これらのコーヒーカップを洗ってくれますか。",
            "choices": ["④−⑤", "③−①", "②−⑤", "①−②"],
            "answer": 3,
            "words": ["wash", "you", "coffee cups", "could", "these"],
            "correctOrder": [4, 2, 1, 5, 3],
            "framePrefix": "",
            "frameSuffix": ", please?",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「Could you wash these coffee cups, please?」になります。Could you ...?＝「〜してくれますか？」。空所は2語目 you（②）と4語目 these（⑤）。",
            "grammarSimple": "正しい文は「Could you wash these coffee cups, please?」。このコーヒーカップをあらってくれる？2ばんめ you、4ばんめ these！",
            "choiceAnalysis": [
                "「④−⑤」だと could these ... となり、Could you wash の形にならない。",
                "「③−①」だと coffee cups wash ... から始まり、語順が合わない。",
                "○「②−⑤」＝you と these。Could you wash these coffee cups, please? が自然な依頼。",
                "「①−②」だと wash you ... となり、Could you wash の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "「④−⑤」は Could you wash にならないよ。",
                "「③−①」はじゅんばんがちがうよ。",
                "○「②−⑤」が正解！Could you wash these ...? だよ！",
                "「①−②」は Could you wash にならないよ。",
            ],
            "questionAudio": "audio/q25.mp3",
        },
    ],
}

for q in section3["questions"]:
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

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
