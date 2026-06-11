# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級 data.json
大問3（並べ替え）Q21〜25 — 解説付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "sentence-order",
    "instruction": "次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて( )の中に入れなさい。",
    "questions": [
        {
            "number": 21,
            "text": "今日は制服を着る必要はありません。",
            "choices": ["①−③", "④−②", "⑤−①", "③−⑤"],
            "answer": 1,
            "words": ["have", "my", "wear", "don't", "to"],
            "correctOrder": [4, 1, 5, 3, 2],
            "framePrefix": "I",
            "frameSuffix": "uniform today.",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「I don't have to wear my uniform today.」になります。don't have to＝「〜する必要はない」。空所は2語目 have（①）と4語目 wear（③）。",
            "grammarSimple": "正しい文は「I don't have to wear my uniform today.」。きょうはせいふくをきるひつようはない、だよ。2ばんめ have、4ばんめ wear！",
            "choiceAnalysis": [
                "○「①−③」＝have と wear。don't have to wear my uniform で文が完成。",
                "「④−②」だと don't my ... の順になり、文が正しく組めない。",
                "「⑤−①」だと to have ... となり、have to wear の形にならない。",
                "「③−⑤」だと wear to ... となり、語順が合わない。",
            ],
            "choiceAnalysisSimple": [
                "○「①−③」が正解！have と wear でぴったり！",
                "「④−②」はじゅんばんがちがうよ。",
                "「⑤−①」は have to wear にならないよ。",
                "「③−⑤」はじゅんばんがちがうよ。",
            ],
            "questionAudio": "audio/q21.mp3",
        },
        {
            "number": 22,
            "text": "夕食にスパゲッティはどうですか。",
            "choices": ["⑤−③", "⑤−①", "②−④", "③−④"],
            "answer": 1,
            "words": ["dinner", "how", "for", "spaghetti", "about"],
            "correctOrder": [2, 5, 4, 3, 1],
            "framePrefix": "",
            "frameSuffix": "?",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「How about spaghetti for dinner?」になります。How about ～?＝「〜はどう？」。空所は2語目 about（⑤）と4語目 for（③）。",
            "grammarSimple": "正しい文は「How about spaghetti for dinner?」。ゆうしょくにスパゲッティはどう？2ばんめ about、4ばんめ for！",
            "choiceAnalysis": [
                "○「⑤−③」＝about と for。How about spaghetti for dinner? が自然な提案の形。",
                "「⑤−①」だと about dinner が続き、spaghetti for が後ろに回って不自然。",
                "「②−④」だと how spaghetti ... となり、How about の形にならない。",
                "「③−④」だと for spaghetti ... から始まり、文として成立しない。",
            ],
            "choiceAnalysisSimple": [
                "○「⑤−③」が正解！How about ... for dinner? だよ！",
                "「⑤−①」はじゅんばんがちがうよ。",
                "「②−④」は How about の形にならないよ。",
                "「③−④」は文にならないよ。",
            ],
            "questionAudio": "audio/q22.mp3",
        },
        {
            "number": 23,
            "text": "そのテレビ番組はまったく面白くありませんでした。",
            "choices": ["③−④", "①−⑤", "⑤−④", "②−①"],
            "answer": 3,
            "words": ["at", "not", "that TV program", "interesting", "was"],
            "correctOrder": [3, 5, 2, 4, 1],
            "framePrefix": "",
            "frameSuffix": "all.",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「That TV program was not interesting at all.」になります。not interesting at all＝「まったく面白くない」。空所は2語目 was（⑤）と4語目 interesting（④）。",
            "grammarSimple": "正しい文は「That TV program was not interesting at all.」。ぜんぜんおもしろくなかった、だよ。2ばんめ was、4ばんめ interesting！",
            "choiceAnalysis": [
                "「③−④」だと that TV program interesting ... となり、was が抜けて文が成立しない。",
                "「①−⑤」だと at was ... から始まり、語順が合わない。",
                "○「⑤−④」＝was と interesting。was not interesting at all で完成。",
                "「②−①」だと not at ... となり、not interesting の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "「③−④」は was がたりないよ。",
                "「①−⑤」はじゅんばんがちがうよ。",
                "○「⑤−④」が正解！was not interesting だよ！",
                "「②−①」は not interesting にならないよ。",
            ],
            "questionAudio": "audio/q23.mp3",
        },
        {
            "number": 24,
            "text": "数学のテストは私にはそれほど簡単ではありませんでした。",
            "choices": ["⑤−④", "①−③", "③−④", "①−②"],
            "answer": 4,
            "words": ["not", "easy", "for", "was", "so"],
            "correctOrder": [4, 1, 5, 2, 3],
            "framePrefix": "The math test",
            "frameSuffix": "me.",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「The math test was not so easy for me.」になります。not so easy＝「それほど簡単ではない」。空所は2語目 not（①）と4語目 easy（②）。",
            "grammarSimple": "正しい文は「The math test was not so easy for me.」。すうがくのテストはわたしにはそれほどかんたんじゃなかった。2ばんめ not、4ばんめ easy！",
            "choiceAnalysis": [
                "「⑤−④」だと so was ... となり、was not so easy の形にならない。",
                "「①−③」だと not for ... となり、not so easy が続かない。",
                "「③−④」だと for was ... となり、語順が合わない。",
                "○「①−②」＝not と easy。was not so easy for me で文が完成。",
            ],
            "choiceAnalysisSimple": [
                "「⑤−④」は was not so easy にならないよ。",
                "「①−③」は not so easy がつながらないよ。",
                "「③−④」はじゅんばんがちがうよ。",
                "○「①−②」が正解！not so easy だよ！",
            ],
            "questionAudio": "audio/q24.mp3",
        },
        {
            "number": 25,
            "text": "ポール，あなたはなぜこの学校を選んだのですか。",
            "choices": ["④−③", "②−④", "①−③", "④−①"],
            "answer": 2,
            "words": ["you", "did", "this", "choose", "why"],
            "correctOrder": [5, 2, 1, 4, 3],
            "framePrefix": "Paul,",
            "frameSuffix": "school?",
            "answerSlots": [2, 4],
            "grammar": "並べかえると「Paul, why did you choose this school?」になります。why did you ...?＝「なぜあなたは〜したの？」。空所は2語目 did（②）と4語目 choose（④）。",
            "grammarSimple": "正しい文は「Paul, why did you choose this school?」。なぜこのがっこうをえらんだの？2ばんめ did、4ばんめ choose！",
            "choiceAnalysis": [
                "「④−③」だと choose this ... が先に来て、why did の疑問文の形にならない。",
                "○「②−④」＝did と choose。why did you choose this school? が自然な疑問文。",
                "「①−③」だと you this ... となり、did you choose の形にならない。",
                "「④−①」だと choose you ... となり、語順が合わない。",
            ],
            "choiceAnalysisSimple": [
                "「④−③」はぎもんぶんにならないよ。",
                "○「②−④」が正解！why did you choose? だよ！",
                "「①−③」は did you choose にならないよ。",
                "「④−①」はじゅんばんがちがうよ。",
            ],
            "questionAudio": "audio/q25.mp3",
        },
    ],
}

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
