# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級 data.json
大問4（長文読解）Q26〜35 — 解説・和訳付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)

section4 = {
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "passages": [
        {
            "label": "A",
            "title": "Field Trip",
            "format": "notice",
            "paragraphs": [
                "Field Trip",
                "Third-grade students will go to the Rainbow Zoo on a school trip by bus.",
                "Date: Friday, June 20\nMeeting Time: 8:00 a.m.",
                "The bus ride to the Rainbow Zoo will take about two hours.\nWe will go to the Rainbow Museum instead if it rains.\nWe will come back to the school at 3:30 p.m.",
            ],
            "translations": [
                "遠足",
                "3年生はバスで学校遠足にレインボー動物園へ行きます。",
                "日付：6月20日（金）\n集合時間：午前8時",
                "動物園までのバスは約2時間かかります。\n雨の場合はレインボー博物館に行きます。\n午後3時30分に学校に戻ります。",
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "If it rains, the students will go to",
                    "choices": [
                        "the Rainbow Zoo.",
                        "another school.",
                        "the Rainbow Museum.",
                        "the theater.",
                    ],
                    "answer": 3,
                    "grammar": "「雨の場合はレインボー博物館に行く」→ the Rainbow Museum。",
                    "grammarSimple": "「あめのときはレインボーはくぶつかん」って書いてあるよ！",
                    "choiceAnalysis": [
                        "動物園＝晴れの日の行き先。",
                        "別の学校＝書いてない。",
                        "○ レインボー博物館。if it rains とセット。",
                        "劇場＝書いてない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「どうぶつえん」ははれのときだよ。",
                        "「べつのがっこう」はちがうよ。",
                        "○「はくぶつかん」がぴったり！",
                        "「げきじょう」はちがうよ。",
                    ],
                    "questionTranslation": "雨が降ったら、生徒たちはどこに行く？",
                    "choiceTranslations": [
                        "レインボー動物園。",
                        "別の学校。",
                        "レインボー博物館。",
                        "劇場。",
                    ],
                    "questionAudio": "audio/q26.mp3",
                },
                {
                    "number": 27,
                    "question": "What time will the students come back to the school?",
                    "choices": [
                        "At 8:00 a.m.",
                        "At 2:00 p.m.",
                        "At 3:00 p.m.",
                        "At 3:30 p.m.",
                    ],
                    "answer": 4,
                    "grammar": "「午後3時30分に学校に戻る」→ At 3:30 p.m.",
                    "grammarSimple": "「ごご3じ30ぷんにがっこうにもどる」って書いてあるよ！",
                    "choiceAnalysis": [
                        "8時＝集合時間。帰校時間ではない。",
                        "2時＝書いてない。",
                        "3時＝30分ではない。",
                        "○ 3時30分＝come back to the school の時刻。",
                    ],
                    "choiceAnalysisSimple": [
                        "「8じ」はしゅうごうの時間だよ。",
                        "「2じ」はちがうよ。",
                        "「3じ」は30ぷんじゃないよ。",
                        "○「3じ30ぷん」がぴったり！",
                    ],
                    "questionTranslation": "生徒たちは何時に学校に戻る？",
                    "choiceTranslations": [
                        "午前8時。",
                        "午後2時。",
                        "午後3時。",
                        "午後3時30分。",
                    ],
                    "questionAudio": "audio/q27.mp3",
                },
            ],
        },
        {
            "label": "B",
            "title": "About next week",
            "paragraphs": [
                "From: Ted Miller\nTo: Leo Smith\nDate: October 10\nSubject: About next week",
                "Hi Leo,\nYou were not at basketball practice yesterday, right? Are you OK? We will have a meeting in room 203 next Monday, and we can meet our new coach at the meeting! Can you come to the meeting? Also, you can get your new uniform after practice next Friday!\nYour teammate,\nTed",
                "From: Leo Smith\nTo: Ted Miller\nDate: October 10\nSubject: Thank you!",
                "Hi Ted,\nI did not have a fever, but I had a headache yesterday afternoon. So, I could not go to practice. However, I am feeling better now. I will go to the meeting, and I am excited to meet our new coach! By the way, my friend David is interested in joining our team. Can I go to practice with him next Wednesday?\nBye,\nLeo",
            ],
            "translations": [
                "差出人：テッド・ミラー\n宛先：レオ・スミス\n日付：10月10日\n件名：来週について",
                "やあレオ\nきのうバスケの練習に来なかったね。大丈夫？来週の月曜、203教室でミーティングがあるよ。ミーティングで新しいコーチに会える！来れる？あと、来週の金曜の練習のあとに新しいユニフォームがもらえるよ！\nチームメイトのテッドより",
                "差出人：レオ・スミス\n宛先：テッド・ミラー\n日付：10月10日\n件名：ありがとう！",
                "やあテッド\n熱はなかったけど、きのうの午後は頭痛だった。だから練習に行けなかった。でも今はよくなった。ミーティングには行くし、新しいコーチに会えるのが楽しみ！ところで、友達のデイビッドがチームに入りたがってる。来週の水曜に彼と一緒に練習に行っていい？\nレオより",
            ],
            "questions": [
                {
                    "number": 28,
                    "question": "What can Ted and Leo do at the meeting?",
                    "choices": [
                        "Get their new shoes.",
                        "Meet their new teammate.",
                        "Get their new uniform.",
                        "Meet their new coach.",
                    ],
                    "answer": 4,
                    "grammar": "「ミーティングで新しいコーチに会える」→ Meet their new coach。",
                    "grammarSimple": "「ミーティングであたらしいコーチにあえる」ってテッドが書いてるよ！",
                    "choiceAnalysis": [
                        "新しい靴＝書いてない。",
                        "新しいチームメイト＝デイビッドの話は別のメール。",
                        "ユニフォーム＝金曜の練習のあと（ミーティングではない）。",
                        "○ 新しいコーチに会う。at the meeting と一致。",
                    ],
                    "choiceAnalysisSimple": [
                        "「くつ」はちがうよ。",
                        "「チームメイト」はミーティングの話じゃないよ。",
                        "「ユニフォーム」はきんようのれんしゅうのあとだよ。",
                        "○「コーチにあう」がぴったり！",
                    ],
                    "questionTranslation": "テッドとレオは、ミーティングで何ができる？",
                    "choiceTranslations": [
                        "新しい靴をもらえる。",
                        "新しいチームメイトに会える。",
                        "新しいユニフォームをもらえる。",
                        "新しいコーチに会える。",
                    ],
                    "questionAudio": "audio/q28.mp3",
                },
                {
                    "number": 29,
                    "question": "Yesterday afternoon, Leo",
                    "choices": [
                        "had a headache.",
                        "had a fever.",
                        "met his team's captain.",
                        "played basketball with Ted.",
                    ],
                    "answer": 1,
                    "grammar": "「熱はなかったが、午後は頭痛だった」→ had a headache。",
                    "grammarSimple": "「ねつはなかったけど、ごごはずつうだった」ってレオが書いてるよ！",
                    "choiceAnalysis": [
                        "○ 頭痛があった。I had a headache yesterday afternoon.",
                        "熱＝did not have a fever で否定されている。",
                        "キャプテンに会った＝書いてない。",
                        "テッドとバスケ＝練習に行けなかった。",
                    ],
                    "choiceAnalysisSimple": [
                        "○「ずつうだった」がぴったり！",
                        "「ねつ」はなかったって書いてあるよ。",
                        "「キャプテン」はちがうよ。",
                        "「バスケした」はちがうよ。れんしゅうにいけなかった。",
                    ],
                    "questionTranslation": "昨日の午後、レオはどうだった？",
                    "choiceTranslations": [
                        "頭痛があった。",
                        "熱があった。",
                        "チームのキャプテンに会った。",
                        "テッドとバスケットボールをした。",
                    ],
                    "questionAudio": "audio/q29.mp3",
                },
                {
                    "number": 30,
                    "question": "When does Leo want to go to practice with David?",
                    "choices": [
                        "Next Monday.",
                        "Next Wednesday.",
                        "Next Friday.",
                        "Next Saturday.",
                    ],
                    "answer": 2,
                    "grammar": "「来週の水曜にデイビッドと練習に行っていい？」→ Next Wednesday。",
                    "grammarSimple": "「らいしゅうのすいようにデイビッドといっしょにれんしゅう」って聞いてるよ！",
                    "choiceAnalysis": [
                        "月曜＝ミーティングの日。",
                        "○ 水曜＝go to practice with him next Wednesday.",
                        "金曜＝ユニフォームをもらう日。",
                        "土曜＝書いてない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「げつよう」はミーティングの日だよ。",
                        "○「すいよう」がぴったり！",
                        "「きんよう」はユニフォームの日だよ。",
                        "「どよう」はちがうよ。",
                    ],
                    "questionTranslation": "レオはいつ、デイビッドと一緒に練習に行きたい？",
                    "choiceTranslations": [
                        "来週の月曜日。",
                        "来週の水曜日。",
                        "来週の金曜日。",
                        "来週の土曜日。",
                    ],
                    "questionAudio": "audio/q30.mp3",
                },
            ],
        },
        {
            "label": "C",
            "title": "Kate's Story",
            "paragraphs": [
                "Kate is sixteen years old and loves her grandmother. Her grandmother always made fun stories for Kate. Kate enjoyed visiting her grandmother's house with her parents and listening to her grandmother's stories. Then, she also began to write her own stories.",
                "Kate's grandmother got sick a year ago, so she is in the hospital now. One day, Kate's father said, \"Let's go to see your grandma next Sunday!\" Kate said, \"Sure! Should I buy some flowers or cookies as a present?\" Kate's father said, \"No. You're good at writing stories! You should write a story for her.\" Kate said, \"Good idea! I'll try it.\"",
                "When Kate and her father visited the hospital, they saw three novels, four history books, and two magazines around her grandmother's bed. Kate gave her grandmother a notebook. Kate's grandmother looked in the notebook and said, \"You wrote a story! This is a wonderful present!\" Kate was so happy.",
            ],
            "translations": [
                "ケイトは16歳で、おばあちゃんが大好き。おばあちゃんはいつもケイトのために楽しい物語を作ってくれた。ケイトは両親と一緒におばあちゃんの家を訪れ、おばあちゃんの話を聞くのが好きだった。それから、自分でも物語を書き始めた。",
                "ケイトのおばあちゃんは1年前に病気になり、今は病院にいる。ある日、お父さんが「来週の日曜におばあちゃんに会いに行こう！」と言った。ケイトは「いいね！花やクッキーをプレゼントに買おうか？」お父さんは「いや、物語を書くのが上手だろう。おばあちゃんのために物語を書きなさい」と言った。ケイトは「いい考え！やってみる」と言った。",
                "ケイトとお父さんが病院を訪れると、おばあちゃんのベッドのまわりに小説が3冊、歴史の本が4冊、雑誌が2冊あった。ケイトはおばあちゃんにノートを渡した。おばあちゃんはノートを見て「物語を書いたのね！素敵なプレゼントだわ！」と言った。ケイトはとてもうれしかった。",
            ],
            "questions": [
                {
                    "number": 31,
                    "question": "What did Kate's grandmother always do for Kate?",
                    "choices": [
                        "She visited Kate's house.",
                        "She made fun stories.",
                        "She listened to Kate's stories.",
                        "She bought many books.",
                    ],
                    "answer": 2,
                    "grammar": "「いつも楽しい物語を作ってくれた」→ made fun stories。",
                    "grammarSimple": "「いつもたのしいものがたりをつくってくれた」って書いてあるよ！",
                    "choiceAnalysis": [
                        "ケイトの家を訪れた＝ケイトがおばあちゃんの家を訪れていた。",
                        "○ 楽しい物語を作った。always made fun stories for Kate.",
                        "ケイトの話を聞いた＝逆の関係。",
                        "本をたくさん買った＝書いてない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「ケイトのいえ」はちがうよ。ケイトがおばあちゃんのいえに行ったんだ。",
                        "○「たのしいものがたり」がぴったり！",
                        "「ケイトのはなしをきいた」はちがうよ。",
                        "「ほんをかった」はちがうよ。",
                    ],
                    "questionTranslation": "ケイトのおばあちゃんは、いつもケイトのために何をした？",
                    "choiceTranslations": [
                        "ケイトの家を訪れた。",
                        "楽しい物語を作った。",
                        "ケイトの物語を聞いた。",
                        "たくさんの本を買った。",
                    ],
                    "questionAudio": "audio/q31.mp3",
                },
                {
                    "number": 32,
                    "question": "Where is Kate's grandmother now?",
                    "choices": [
                        "In Kate's house.",
                        "In the hospital.",
                        "At her friend's house.",
                        "At her own house.",
                    ],
                    "answer": 2,
                    "grammar": "「今は病院にいる」→ In the hospital。",
                    "grammarSimple": "「いまはびょういんにいる」って書いてあるよ！",
                    "choiceAnalysis": [
                        "ケイトの家＝今は病院。",
                        "○ 病院にいる。she is in the hospital now.",
                        "友達の家＝書いてない。",
                        "自分の家＝1年前までは家にいたが、今は病院。",
                    ],
                    "choiceAnalysisSimple": [
                        "「ケイトのいえ」はちがうよ。",
                        "○「びょういん」がぴったり！",
                        "「ともだちのいえ」はちがうよ。",
                        "「じぶんのいえ」はいまはちがうよ。",
                    ],
                    "questionTranslation": "ケイトのおばあちゃんは今、どこにいる？",
                    "choiceTranslations": [
                        "ケイトの家。",
                        "病院。",
                        "友達の家。",
                        "自分の家。",
                    ],
                    "questionAudio": "audio/q32.mp3",
                },
                {
                    "number": 33,
                    "question": "What did Kate's father say to Kate about the present for her grandmother?",
                    "choices": [
                        "Kate should write a story.",
                        "Kate should make some cookies.",
                        "Kate should bring some flowers.",
                        "Kate should buy some fun books.",
                    ],
                    "answer": 1,
                    "grammar": "「物語を書きなさい」→ Kate should write a story。",
                    "grammarSimple": "「ものがたりをかきなさい」っておとうさんが言ったよ！",
                    "choiceAnalysis": [
                        "○ 物語を書くべき。You should write a story for her.",
                        "クッキーを作る＝ケイトの提案を父が断った。",
                        "花を持っていく＝ケイトの提案を父が断った。",
                        "楽しい本を買う＝書いてない。",
                    ],
                    "choiceAnalysisSimple": [
                        "○「ものがたりをかく」がぴったり！",
                        "「クッキー」はケイトの案で、おとうさんはNOだよ。",
                        "「はな」もケイトの案で、おとうさんはNOだよ。",
                        "「ほんをかう」はちがうよ。",
                    ],
                    "questionTranslation": "おばあちゃんへのプレゼントについて、ケイトのお父さんは何と言った？",
                    "choiceTranslations": [
                        "ケイトは物語を書くべきだ。",
                        "ケイトはクッキーを作るべきだ。",
                        "ケイトは花を持っていくべきだ。",
                        "ケイトは楽しい本を買うべきだ。",
                    ],
                    "questionAudio": "audio/q33.mp3",
                },
                {
                    "number": 34,
                    "question": "How many history books did Kate see around her grandmother's bed?",
                    "choices": ["One.", "Two.", "Three.", "Four."],
                    "answer": 4,
                    "grammar": "「歴史の本が4冊」→ four history books → Four.",
                    "grammarSimple": "「れきしのほんが4さつ」って書いてあるよ！",
                    "choiceAnalysis": [
                        "1冊＝小説が3冊。歴史の本は4冊。",
                        "2冊＝雑誌の数。",
                        "3冊＝小説の数。",
                        "○ 4冊＝four history books。",
                    ],
                    "choiceAnalysisSimple": [
                        "「1さつ」はしょうせつだよ。",
                        "「2さつ」はざっしだよ。",
                        "「3さつ」はしょうせつだよ。",
                        "○「4さつ」がぴったり！れきしのほん！",
                    ],
                    "questionTranslation": "ケイトは、おばあちゃんのベッドのまわりに歴史の本を何冊見た？",
                    "choiceTranslations": ["1冊。", "2冊。", "3冊。", "4冊。"],
                    "questionAudio": "audio/q34.mp3",
                },
                {
                    "number": 35,
                    "question": "What did Kate give her grandmother?",
                    "choices": [
                        "Some history books.",
                        "A picture.",
                        "Some magazines.",
                        "A notebook.",
                    ],
                    "answer": 4,
                    "grammar": "「おばあちゃんにノートを渡した」→ A notebook。",
                    "grammarSimple": "「おばあちゃんにノートをわたした」って書いてあるよ！",
                    "choiceAnalysis": [
                        "歴史の本＝ベッドのまわりにあっただけ。プレゼントではない。",
                        "絵＝書いてない。",
                        "雑誌＝ベッドのまわりにあっただけ。",
                        "○ ノート。Kate gave her grandmother a notebook.",
                    ],
                    "choiceAnalysisSimple": [
                        "「れきしのほん」はプレゼントじゃないよ。",
                        "「え」はちがうよ。",
                        "「ざっし」はプレゼントじゃないよ。",
                        "○「ノート」がぴったり！",
                    ],
                    "questionTranslation": "ケイトはおばあちゃんに何をあげた？",
                    "choiceTranslations": [
                        "歴史の本。",
                        "絵。",
                        "雑誌。",
                        "ノート。",
                    ],
                    "questionAudio": "audio/q35.mp3",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data.get("sections", [])
new_sections = []
replaced = False
for sec in sections:
    if sec.get("name") == "大問4":
        new_sections.append(section4)
        replaced = True
    else:
        new_sections.append(sec)
if not replaced:
    new_sections.append(section4)

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section4 ({sum(len(p['questions']) for p in section4['passages'])} questions) to {DATA_PATH}")
