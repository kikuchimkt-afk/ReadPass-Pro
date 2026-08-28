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
        out.append(f"○ {cleaned}" if i + 1 == answer else cleaned)
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
            "grammar": "日本語は「なぜあなたは今朝、そんなに早く起きたのですか」。正しい語順は「Why did you get up so early this morning?」です。Why did＋主語＋動詞の原形で、過去の理由をたずねます。①〜⑤を並べると④⑤①③②（why → did → you → get → up）。空所内の2番目は⑤「did」、4番目は③「get」なので、答えは⑤−③です。",
            "grammarSimple": "ただしい文は「Why did you get up so early this morning?」。Why did you は「なぜあなたは〜したの？」。2ばんめは⑤ did、4ばんめは③ get。だから⑤−③だよ！",
            "choiceAnalysis": [
                "①−②：2番目が①「you」、4番目が②「up」になり、正しい位置と異なります。正しくは2番目が⑤「did」、4番目が③「get」です。",
                "○ 2番目＝⑤「did」、4番目＝③「get」。「Why did you get up so early this morning?」と正しく並びます。",
                "③−⑤：2番目が③「get」、4番目が⑤「did」になり、正しい位置と異なります。正しくは⑤「did」と③「get」です。",
                "④−①：2番目が④「why」、4番目が①「you」になり、正しい位置と異なります。正しくは⑤「did」と③「get」です。",
            ],
            "choiceAnalysisSimple": [
                "①「you」と②「up」では、2ばんめと4ばんめのばしょがちがうよ。",
                "○ 2ばんめ⑤「did」、4ばんめ③「get」でぴったり！",
                "③「get」と⑤「did」では、ばしょがぎゃくだよ。",
                "④「why」と①「you」では、2ばんめと4ばんめのばしょがちがうよ。",
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
            "grammar": "日本語は「今日の午後、あなたに電話してもいいですか」。正しい語順は「May I call you this afternoon?」です。May I＋動詞の原形で、ていねいに許可を求めます。①〜⑤を並べると②④⑤③①（may → I → call → you → this）。空所内の2番目は④「I」、4番目は③「you」なので、答えは④−③です。",
            "grammarSimple": "ただしい文は「May I call you this afternoon?」。May I call you は「でんわしてもいい？」。2ばんめは④ I、4ばんめは③ you。だから④−③だよ！",
            "choiceAnalysis": [
                "○ 2番目＝④「I」、4番目＝③「you」。「May I call you this afternoon?」と正しく並びます。",
                "①−③：2番目が①「this」、4番目が③「you」になり、正しい位置と異なります。正しくは④「I」と③「you」です。",
                "⑤−①：2番目が⑤「call」、4番目が①「this」になり、正しい位置と異なります。正しくは④「I」と③「you」です。",
                "③−①：2番目が③「you」、4番目が①「this」になり、正しい位置と異なります。正しくは④「I」と③「you」です。",
            ],
            "choiceAnalysisSimple": [
                "○ 2ばんめ④「I」、4ばんめ③「you」でぴったり！",
                "①「this」と③「you」では、2ばんめのばしょがちがうよ。",
                "⑤「call」と①「this」では、2ばんめと4ばんめのばしょがちがうよ。",
                "③「you」と①「this」では、2ばんめと4ばんめのばしょがちがうよ。",
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
            "grammar": "日本語は「ネパールではたくさんの高い山を見ることができます」。正しい語順は「You can see lots of high mountains in Nepal.」です。can＋動詞の原形で「〜できる」、lots of＋名詞で「たくさんの〜」。①〜⑤を並べると②③①⑤④（you → can → see → lots of → high mountains）。空所内の2番目は③「can」、4番目は⑤「lots of」なので、答えは③−⑤です。",
            "grammarSimple": "ただしい文は「You can see lots of high mountains in Nepal.」。can see は「みることができる」、lots of は「たくさんの」。2ばんめは③ can、4ばんめは⑤ lots of だよ！",
            "choiceAnalysis": [
                "④−②：2番目が④「high mountains」、4番目が②「you」になり、正しい位置と異なります。正しくは③「can」と⑤「lots of」です。",
                "○ 2番目＝③「can」、4番目＝⑤「lots of」。「You can see lots of high mountains in Nepal.」と正しく並びます。",
                "④−③：2番目が④「high mountains」、4番目が③「can」になり、正しい位置と異なります。正しくは③「can」と⑤「lots of」です。",
                "⑤−③：2番目が⑤「lots of」、4番目が③「can」になり、正しい位置と異なります。正しくは③「can」と⑤「lots of」です。",
            ],
            "choiceAnalysisSimple": [
                "④「high mountains」と②「you」では、ばしょがちがうよ。",
                "○ 2ばんめ③「can」、4ばんめ⑤「lots of」でぴったり！",
                "④「high mountains」と③「can」では、ばしょがちがうよ。",
                "⑤「lots of」と③「can」では、ばしょがちがうよ。",
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
            "grammar": "日本語は「私は毎朝7時に家を出て学校へ向かいます」。正しい語順は「I leave home for school at seven o'clock every morning.」です。leave home for school で「学校へ向かうために家を出る」。①〜⑤を並べると③⑤④②①（leave → home → for → school → at）。空所内の2番目は⑤「home」、4番目は②「school」なので、答えは⑤−②です。",
            "grammarSimple": "ただしい文は「I leave home for school at seven o'clock every morning.」。leave home for school は「いえをでて、がっこうへむかう」。2ばんめは⑤ home、4ばんめは② school だよ！",
            "choiceAnalysis": [
                "⑤−③：2番目が⑤「home」、4番目が③「leave」になり、正しい位置と異なります。正しくは⑤「home」と②「school」です。",
                "③−④：2番目が③「leave」、4番目が④「for」になり、正しい位置と異なります。正しくは⑤「home」と②「school」です。",
                "○ 2番目＝⑤「home」、4番目＝②「school」。「I leave home for school at seven o'clock every morning.」と正しく並びます。",
                "③−⑤：2番目が③「leave」、4番目が⑤「home」になり、正しい位置と異なります。正しくは⑤「home」と②「school」です。",
            ],
            "choiceAnalysisSimple": [
                "⑤「home」と③「leave」では、4ばんめのばしょがちがうよ。",
                "③「leave」と④「for」では、ばしょがちがうよ。",
                "○ 2ばんめ⑤「home」、4ばんめ②「school」でぴったり！",
                "③「leave」と⑤「home」では、ばしょがちがうよ。",
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
            "grammar": "日本語は「これらのコーヒーカップを洗ってくれますか」。正しい語順は「Could you wash these coffee cups, please?」です。Could you＋動詞の原形で、ていねいに依頼します。①〜⑤を並べると④②①⑤③（could → you → wash → these → coffee cups）。空所内の2番目は②「you」、4番目は⑤「these」なので、答えは②−⑤です。",
            "grammarSimple": "ただしい文は「Could you wash these coffee cups, please?」。Could you wash は「あらってくれますか」。2ばんめは② you、4ばんめは⑤ these。だから②−⑤だよ！",
            "choiceAnalysis": [
                "④−⑤：2番目が④「could」、4番目が⑤「these」になり、正しい位置と異なります。正しくは②「you」と⑤「these」です。",
                "③−①：2番目が③「coffee cups」、4番目が①「wash」になり、正しい位置と異なります。正しくは②「you」と⑤「these」です。",
                "○ 2番目＝②「you」、4番目＝⑤「these」。「Could you wash these coffee cups, please?」と正しく並びます。",
                "①−②：2番目が①「wash」、4番目が②「you」になり、正しい位置と異なります。正しくは②「you」と⑤「these」です。",
            ],
            "choiceAnalysisSimple": [
                "④「could」と⑤「these」では、2ばんめのばしょがちがうよ。",
                "③「coffee cups」と①「wash」では、ばしょがちがうよ。",
                "○ 2ばんめ②「you」、4ばんめ⑤「these」でぴったり！",
                "①「wash」と②「you」では、ばしょがちがうよ。",
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
