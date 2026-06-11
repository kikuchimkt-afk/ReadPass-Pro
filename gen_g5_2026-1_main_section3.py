# -*- coding: utf-8 -*-
"""2026年度 第1回（本会場）英検5級 data.json 大問3 Q21〜25"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)


def mark_ca(items, answer):
    out = []
    for i, text in enumerate(items):
        cleaned = re.sub(r"^[○✅❌]\s*", "", text)
        prefix = "✅" if i + 1 == answer else "❌"
        out.append(f"{prefix} {cleaned}")
    return out


section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "sentence-order",
    "instruction": "次の(21)から(25)までの日本文の意味を表すように①から④までを並べかえて( )の中に入れなさい。そして、1番目と3番目にくるものの最も適切な組合せを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。※ただし、( )の中では、文のはじめにくる語も小文字になっています。",
    "questions": [
        {
            "number": 21,
            "text": "あなたの英語のテストはいつですか。",
            "choices": ["④ ─ ②", "③ ─ ①", "② ─ ④", "① ─ ④"],
            "answer": 3,
            "words": ["is", "when", "English", "your"],
            "correctOrder": [2, 1, 4, 3],
            "framePrefix": "",
            "frameSuffix": "test?",
            "answerSlots": [1, 3],
            "grammar": "並べかえると「When is your English test?」になります。1番目 when（②）、3番目 your（④）。",
            "grammarSimple": "正しい文は「When is your English test?」。1ばんめ when、3ばんめ your！",
            "choiceAnalysis": [
                "「④─②」だと your when ... となり、When is your English の形にならない。",
                "「③─①」だと English is ... から始まり、疑問文の語順が合わない。",
                "「②─④」＝when と your。When is your English test? が自然な疑問文。",
                "「①─④」だと is your ... から始まり、When が抜けて文が成立しない。",
            ],
            "choiceAnalysisSimple": [
                "「④─②」は When is your にならないよ。",
                "「③─①」はじゅんばんがちがうよ。",
                "○「②─④」が正解！When is your English test? だよ！",
                "「①─④」は When がたりないよ。",
            ],
            "questionAudio": "audio/q21.mp3",
        },
        {
            "number": 22,
            "text": "ロンドンは何時ですか。",
            "choices": ["③ ─ ①", "④ ─ ②", "③ ─ ④", "② ─ ①"],
            "answer": 3,
            "words": ["in", "is", "time", "it"],
            "correctOrder": [3, 2, 4, 1],
            "framePrefix": "What",
            "frameSuffix": "London?",
            "answerSlots": [1, 3],
            "grammar": "並べかえると「What time is it in London?」になります。1番目 time（③）、3番目 it（④）。",
            "grammarSimple": "正しい文は「What time is it in London?」。1ばんめ time、3ばんめ it！",
            "choiceAnalysis": [
                "「③─①」だと time in ... となり、What time is it の形にならない。",
                "「④─②」だと it is ... から始まり、What time の語順が合わない。",
                "「③─④」＝time と it。What time is it in London? が正しい。",
                "「②─①」だと is in ... となり、What time is it の形にならない。",
            ],
            "choiceAnalysisSimple": [
                "「③─①」は What time is it にならないよ。",
                "「④─②」はじゅんばんがちがうよ。",
                "○「③─④」が正解！What time is it in London? だよ！",
                "「②─①」は合わないよ。",
            ],
            "questionAudio": "audio/q22.mp3",
        },
        {
            "number": 23,
            "text": "私たちの担任は遠藤先生です。",
            "choices": ["① ─ ③", "④ ─ ②", "③ ─ ④", "① ─ ②"],
            "answer": 1,
            "words": ["our", "is", "teacher", "homeroom"],
            "correctOrder": [1, 4, 3, 2],
            "framePrefix": "",
            "frameSuffix": "Mr. Endo.",
            "answerSlots": [1, 3],
            "grammar": "並べかえると「Our homeroom teacher is Mr. Endo.」になります。1番目 our（①）、3番目 teacher（③）。",
            "grammarSimple": "正しい文は「Our homeroom teacher is Mr. Endo.」。1ばんめ our、3ばんめ teacher！",
            "choiceAnalysis": [
                "「①─③」＝our と teacher。Our homeroom teacher is Mr. Endo. が自然。",
                "「④─②」だと homeroom is ... から始まり、Our homeroom teacher の形にならない。",
                "「③─④」だと teacher homeroom ... となり、語順が合わない。",
                "「①─②」だと our is ... となり、homeroom teacher がつながらない。",
            ],
            "choiceAnalysisSimple": [
                "○「①─③」が正解！Our homeroom teacher is Mr. Endo. だよ！",
                "「④─②」は合わないよ。",
                "「③─④」はじゅんばんがちがうよ。",
                "「①─②」は homeroom teacher にならないよ。",
            ],
            "questionAudio": "audio/q23.mp3",
        },
        {
            "number": 24,
            "text": "一樹は夕食にピザが欲しいです。",
            "choices": ["④ ─ ②", "② ─ ①", "③ ─ ④", "① ─ ③"],
            "answer": 1,
            "words": ["wants", "some pizza", "for", "Kazuki"],
            "correctOrder": [4, 1, 2, 3],
            "framePrefix": "",
            "frameSuffix": "dinner.",
            "answerSlots": [1, 3],
            "grammar": "並べかえると「Kazuki wants some pizza for dinner.」になります。1番目 Kazuki（④）、3番目 some pizza（②）。",
            "grammarSimple": "正しい文は「Kazuki wants some pizza for dinner.」。1ばんめ Kazuki、3ばんめ some pizza！",
            "choiceAnalysis": [
                "「④─②」＝Kazuki と some pizza。Kazuki wants some pizza for dinner. が自然。",
                "「②─①」だと some pizza wants ... となり、主語と動詞の語順が合わない。",
                "「③─④」だと for Kazuki ... から始まり、文の形にならない。",
                "「①─③」だと wants for ... となり、主語が抜ける。",
            ],
            "choiceAnalysisSimple": [
                "○「④─②」が正解！Kazuki wants some pizza for dinner. だよ！",
                "「②─①」はじゅんばんがちがうよ。",
                "「③─④」は文にならないよ。",
                "「①─③」は主語がたりないよ。",
            ],
            "questionAudio": "audio/q24.mp3",
        },
        {
            "number": 25,
            "text": "あなたは昼食に何を作っていますか。",
            "choices": ["③ ─ ④", "① ─ ②", "② ─ ③", "④ ─ ①"],
            "answer": 1,
            "words": ["are", "making", "what", "you"],
            "correctOrder": [3, 1, 4, 2],
            "framePrefix": "",
            "frameSuffix": "for lunch?",
            "answerSlots": [1, 3],
            "grammar": "並べかえると「What are you making for lunch?」になります。1番目 what（③）、3番目 you（④）。",
            "grammarSimple": "正しい文は「What are you making for lunch?」。1ばんめ what、3ばんめ you！",
            "choiceAnalysis": [
                "「③─④」＝what と you。What are you making for lunch? が自然な疑問文。",
                "「①─②」だと are making ... から始まり、What 疑問文の形にならない。",
                "「②─③」だと making what ... となり、語順が合わない。",
                "「④─①」だと you are ... から始まり、What 疑問文にならない。",
            ],
            "choiceAnalysisSimple": [
                "○「③─④」が正解！What are you making for lunch? だよ！",
                "「①─②」は What 文にならないよ。",
                "「②─③」はじゅんばんがちがうよ。",
                "「④─①」は What 文にならないよ。",
            ],
            "questionAudio": "audio/q25.mp3",
        },
    ],
}

for q in section3["questions"]:
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = []
replaced = False
for sec in data.get("sections", []):
    if sec.get("name") == "大問3":
        sections.append(section3)
        replaced = True
    else:
        sections.append(sec)
if not replaced:
    sections.append(section3)

data["sections"] = sections
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section3 ({len(section3['questions'])} questions) to {DATA_PATH}")
