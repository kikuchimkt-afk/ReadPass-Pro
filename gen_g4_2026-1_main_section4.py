# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
大問4（長文読解）Q26〜35 — 解説・和訳付き
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

section4 = {
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "passages": [
        {
            "label": "A",
            "title": "Musician Will Visit Our School",
            "format": "notice",
            "paragraphs": [
                "Musician Will Visit Our School",
                "The famous piano player Mr. Stevens will visit the school on Friday afternoon for one hour.",
                "He will first give a speech in the gym and then play three songs in the music room. After this performance, students can eat snacks in the cafeteria.",
                "Date: February 12\nTime: 4:00 p.m. to 5:00 p.m.",
            ],
            "translations": [
                "ミュージシャンが学校を訪問します",
                "有名なピアニストのスティーブンス先生が、金曜の午後1時間、学校を訪問します。",
                "まず体育館でスピーチを行い、その後音楽室で3曲演奏します。この公演のあと、生徒はカフェテリアでおやつを食べられます。",
                "日付：2月12日\n時間：午後4時〜5時",
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "What will happen in the gym?",
                    "choices": [
                        "A piano player will give a speech.",
                        "Students will receive free snacks.",
                        "A piano player will play songs.",
                        "Students will dance.",
                    ],
                    "answer": 1,
                    "grammar": "give a speech in the gym＝「体育館でスピーチをする」。音楽室で演奏するのはその後。",
                    "grammarSimple": "「たいいくかんでスピーチをする」って書いてあるよ！おんがくしつでえんそうするのはそのあとだよ。",
                    "choiceAnalysis": [
                        "○ give a speech in the gym＝体育館でスピーチ。He will first give a speech in the gym と一致。",
                        "eat snacks in the cafeteria＝おやつはカフェテリアでの出来事。",
                        "play songs＝演奏は the music room（音楽室）。",
                        "dance＝書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "○「スピーチ」がぴったり！たいいくかんでするよ！",
                        "「おやつ」はカフェテリアだよ。",
                        "「えんそう」はおんがくしつだよ。",
                        "「ダンス」はちがうよ。",
                    ],
                    "questionTranslation": "体育館では何が行われる？",
                    "choiceTranslations": [
                        "ピアニストがスピーチをする。",
                        "生徒が無料のおやつをもらう。",
                        "ピアニストが曲を演奏する。",
                        "生徒がダンスをする。",
                    ],
                    "sourceEvidence": ["He will first give a speech in the gym"],
                    "questionAudio": "audio/q26.mp3",
                },
                {
                    "number": 27,
                    "question": "How many songs will Mr. Stevens play?",
                    "choices": [
                        "Two songs.",
                        "Three songs.",
                        "Four songs.",
                        "Five songs.",
                    ],
                    "answer": 2,
                    "grammar": "play three songs＝「3曲演奏する」。",
                    "grammarSimple": "「3きょくえんそうする」って書いてあるよ！",
                    "choiceAnalysis": [
                        "Two songs＝本文は three songs。",
                        "○ Three songs.＝play three songs in the music room と一致。",
                        "Four songs＝書かれていない。",
                        "Five songs＝書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「2きょく」はちがうよ。",
                        "○「3きょく」がぴったり！",
                        "「4きょく」はちがうよ。",
                        "「5きょく」はちがうよ。",
                    ],
                    "questionTranslation": "スティーブンス先生は何曲演奏する？",
                    "choiceTranslations": [
                        "2曲。",
                        "3曲。",
                        "4曲。",
                        "5曲。",
                    ],
                    "sourceEvidence": ["play three songs in the music room"],
                    "questionAudio": "audio/q27.mp3",
                },
            ],
        },
        {
            "label": "B",
            "title": "How are your cats?",
            "paragraphs": [
                "From: Jimmy Cook\nTo: Cathy Cook\nDate: July 7\nSubject: How are your cats?",
                "Dear Grandma,\nLast summer was so much fun! I enjoyed spending two weeks at your home. How is your cat, Lily? She had some babies, right? Dad told me about it. How many babies does she have? I really want to see them! Can I visit your home next month? I can stay for four days then!\nWrite soon,\nJimmy",
                "From: Cathy Cook\nTo: Jimmy Cook\nDate: July 7\nSubject: They are fine!",
                "Dear Jimmy,\nOf course, come and see my cat Lily and her babies next month! She has three babies, and they are very cute. Yesterday, one of my friends visited me and saw them, too! I'll send you a picture of the babies by email tomorrow!\nLove,\nGrandma",
            ],
            "translations": [
                "差出人：ジミー・クック\n宛先：キャシー・クック\n日付：7月7日\n件名：猫は元気？",
                "おばあちゃんへ\n去年の夏はとても楽しかった！2週間おばあちゃんの家にいたのが好きだった。猫のリリーは元気？子猫が生まれたんでしょ？お父さんが教えてくれた。子猫は何匹？ぜひ会いたい！来月おばあちゃんの家に行っていい？4日間滞在できるよ！\n早く返事してね、\nジミーより",
                "差出人：キャシー・クック\n宛先：ジミー・クック\n日付：7月7日\n件名：元気だよ！",
                "ジミーへ\nもちろん、来月リリーと子猫に会いに来て！子猫は3匹でとてもかわいいの。昨日、友達がうちに来て子猫にも会ったの！明日メールで子猫の写真を送るね！\n愛を込めて、\nおばあちゃんより",
            ],
            "questions": [
                {
                    "number": 28,
                    "question": "When can Jimmy visit his grandmother's home?",
                    "choices": [
                        "Tomorrow.",
                        "Next week.",
                        "Next month.",
                        "Next summer.",
                    ],
                    "answer": 3,
                    "grammar": "Can I visit your home next month?＝「来月訪問していい？」。おばあちゃんも come next month と返信。",
                    "grammarSimple": "「らいげついっていい？」ってジミーが聞いて、おばあちゃんも「らいげつ来て」って言ってるよ！",
                    "choiceAnalysis": [
                        "Tomorrow＝写真を明日送る話。訪問の時期ではない。",
                        "Next week＝書かれていない。",
                        "○ Next month.＝Can I visit your home next month? と一致。",
                        "Next summer＝last summer（去年の夏）の話。",
                    ],
                    "choiceAnalysisSimple": [
                        "「あした」はしゃしんの話だよ。",
                        "「らいしゅう」はちがうよ。",
                        "○「らいげつ」がぴったり！",
                        "「らいねんのなつ」はちがうよ。",
                    ],
                    "questionTranslation": "ジミーはいつおばあちゃんの家を訪ねられる？",
                    "choiceTranslations": [
                        "明日。",
                        "来週。",
                        "来月。",
                        "来年の夏。",
                    ],
                    "sourceEvidence": ["Can I visit your home next month?"],
                    "questionAudio": "audio/q28.mp3",
                },
                {
                    "number": 29,
                    "question": "How many babies does Lily have?",
                    "choices": ["One.", "Two.", "Three.", "Four."],
                    "answer": 3,
                    "grammar": "She has three babies＝「子猫が3匹いる」。",
                    "grammarSimple": "「3ひきいる」っておばあちゃんが書いてるよ！",
                    "choiceAnalysis": [
                        "One＝本文は three babies。",
                        "Two＝書かれていない。",
                        "○ Three.＝She has three babies, and they are very cute. と一致。",
                        "Four＝書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「1ひき」はちがうよ。",
                        "「2ひき」はちがうよ。",
                        "○「3ひき」がぴったり！",
                        "「4ひき」はちがうよ。",
                    ],
                    "questionTranslation": "リリーには子猫が何匹いる？",
                    "choiceTranslations": ["1匹。", "2匹。", "3匹。", "4匹。"],
                    "sourceEvidence": ["She has three babies, and they are very cute."],
                    "questionAudio": "audio/q29.mp3",
                },
                {
                    "number": 30,
                    "question": "Who visited Jimmy's grandmother yesterday?",
                    "choices": [
                        "Her friend.",
                        "Her daughter.",
                        "Jimmy.",
                        "Jimmy's father.",
                    ],
                    "answer": 1,
                    "grammar": "one of my friends visited me＝「友達の一人が訪ねてきた」。",
                    "grammarSimple": "「ともだちのひとりがきのうきた」って書いてあるよ！",
                    "choiceAnalysis": [
                        "○ Her friend.＝one of my friends visited me yesterday と一致。",
                        "Her daughter＝書かれていない。",
                        "Jimmy＝ジミーはまだ訪問していない（来月の予定）。",
                        "Jimmy's father＝Dad told me about it の話で、昨日訪問した人ではない。",
                    ],
                    "choiceAnalysisSimple": [
                        "○「ともだち」がぴったり！きのうきたよ！",
                        "「むすめ」はちがうよ。",
                        "「ジミー」はまだ行ってないよ。",
                        "「おとうさん」はちがうよ。",
                    ],
                    "questionTranslation": "昨日、ジミーのおばあちゃんのところを誰が訪ねた？",
                    "choiceTranslations": [
                        "彼女の友達。",
                        "彼女の娘。",
                        "ジミー。",
                        "ジミーの父親。",
                    ],
                    "sourceEvidence": ["Yesterday, one of my friends visited me and saw them, too!"],
                    "questionAudio": "audio/q30.mp3",
                },
            ],
        },
        {
            "label": "C",
            "title": "A Visit to a History Museum",
            "paragraphs": [
                "George is thirteen years old. Recently, his sister wanted to go to a history museum. So, his family went to the museum last Saturday. The museum was in an old building. It was eighty years old. In the museum, he saw many interesting things. The best part was an old classroom.",
                "George walked into the classroom and saw an old blackboard. The blackboard was forty years old. He was surprised because the blackboard was green. He also saw desks and chairs. They were dark brown. Then, George saw some old history textbooks. He saw a lot of interesting things in the classroom. He liked looking at the textbooks most because they were so old.",
                "The history museum was very fun. George's favorite subjects in school were English and math before, but now his favorite is history. George wants to go to more museums with his sister.",
            ],
            "translations": [
                "ジョージは13歳。最近、妹が歴史博物館に行きたがった。そこで家族は先週の土曜日、博物館に行った。博物館は古い建物にあった。建物は80年の歴史がある。博物館ではたくさんの面白いものを見た。いちばんよかったのは古い教室だった。",
                "ジョージは教室に入り、古い黒板を見た。黒板は40年ものだった。黒板が緑色だったので驚いた。机と椅子も見た。それらは濃い茶色だった。それから、古い歴史の教科書も見た。教室には面白いものがたくさんあった。教科書がとても古かったので、いちばん見るのが好きだった。",
                "歴史博物館はとても楽しかった。以前は英語と数学が好きな科目だったが、今は歴史がいちばん好きだ。ジョージは妹と、もっと博物館に行きたいと思っている。",
            ],
            "questions": [
                {
                    "number": 31,
                    "question": "Why did George's family go to the museum last Saturday?",
                    "choices": [
                        "George's father had four tickets.",
                        "George's mother works there.",
                        "George's sister wanted to go.",
                        "George likes history.",
                    ],
                    "answer": 3,
                    "grammar": "his sister wanted to go to a history museum＝「妹が博物館に行きたがった」が理由。",
                    "grammarSimple": "「いもうとがびょうぶつかんに行きたがった」から行ったんだよ！",
                    "choiceAnalysis": [
                        "four tickets＝書かれていない。",
                        "mother works there＝書かれていない。",
                        "○ George's sister wanted to go.＝his sister wanted to go to a history museum と一致。",
                        "George likes history＝今は好きだが、行った理由は妹の希望。",
                    ],
                    "choiceAnalysisSimple": [
                        "「チケット」はちがうよ。",
                        "「おかあさんがはたらく」はちがうよ。",
                        "○「いもうとが行きたかった」がぴったり！",
                        "「ジョージがすき」はいまの話だよ。",
                    ],
                    "questionTranslation": "ジョージの家族は、なぜ先週の土曜日に博物館に行った？",
                    "choiceTranslations": [
                        "父がチケットを4枚持っていたから。",
                        "母がそこで働いているから。",
                        "妹が行きたがったから。",
                        "ジョージが歴史が好きだから。",
                    ],
                    "sourceEvidence": ["his sister wanted to go to a history museum"],
                    "questionAudio": "audio/q31.mp3",
                },
                {
                    "number": 32,
                    "question": "How old was the blackboard?",
                    "choices": [
                        "Thirteen years old.",
                        "Twenty years old.",
                        "Forty years old.",
                        "Eighty years old.",
                    ],
                    "answer": 3,
                    "grammar": "The blackboard was forty years old.＝黒板は40年もの。",
                    "grammarSimple": "「こくばんは40ねんもの」って書いてあるよ！80ねんはたてものの話だよ。",
                    "choiceAnalysis": [
                        "Thirteen＝George is thirteen（ジョージの年齢）。",
                        "Twenty＝書かれていない。",
                        "○ Forty years old.＝The blackboard was forty years old. と一致。",
                        "Eighty years old＝建物の年数（It was eighty years old）。",
                    ],
                    "choiceAnalysisSimple": [
                        "「13さい」はジョージのねんれいだよ。",
                        "「20ねん」はちがうよ。",
                        "○「40ねん」がぴったり！こくばんだよ！",
                        "「80ねん」はたてものの話だよ。",
                    ],
                    "questionTranslation": "黒板は何年ものだった？",
                    "choiceTranslations": [
                        "13年。",
                        "20年。",
                        "40年。",
                        "80年。",
                    ],
                    "sourceEvidence": ["The blackboard was forty years old."],
                    "questionAudio": "audio/q32.mp3",
                },
                {
                    "number": 33,
                    "question": "What color were the desks?",
                    "choices": ["Black.", "Green.", "Light brown.", "Dark brown."],
                    "answer": 4,
                    "grammar": "They were dark brown.＝机と椅子は濃い茶色。green は黒板の色。",
                    "grammarSimple": "「くろいちゃいろ」って書いてあるよ！みどりはこくばんのいろだよ。",
                    "choiceAnalysis": [
                        "Black＝本文は dark brown。",
                        "Green＝黒板（blackboard）の色。",
                        "Light brown＝dark brown と異なる。",
                        "○ Dark brown.＝They were dark brown.（desks and chairs）と一致。",
                    ],
                    "choiceAnalysisSimple": [
                        "「くろ」はちがうよ。",
                        "「みどり」はこくばんだよ。",
                        "「うすいちゃ」はちがうよ。",
                        "○「こいちゃいろ」がぴったり！",
                    ],
                    "questionTranslation": "机は何色だった？",
                    "choiceTranslations": ["黒。", "緑。", "薄茶色。", "濃い茶色。"],
                    "sourceEvidence": ["They were dark brown."],
                    "questionAudio": "audio/q33.mp3",
                },
                {
                    "number": 34,
                    "question": "What did George like most in the classroom?",
                    "choices": [
                        "The textbooks.",
                        "The desks.",
                        "The map.",
                        "The blackboard.",
                    ],
                    "answer": 1,
                    "grammar": "He liked looking at the textbooks most＝「いちばん教科書を見るのが好きだった」。",
                    "grammarSimple": "「きょうかしょをみるのがいちばんすき」って書いてあるよ！",
                    "choiceAnalysis": [
                        "○ The textbooks.＝liked looking at the textbooks most と一致。",
                        "The desks＝机は見たが、いちばん好きだったのは教科書。",
                        "The map＝書かれていない。",
                        "The blackboard＝黒板は驚いたが、most は textbooks。",
                    ],
                    "choiceAnalysisSimple": [
                        "○「きょうかしょ」がぴったり！いちばんすき！",
                        "「つくえ」はいちばんじゃないよ。",
                        "「ちず」はちがうよ。",
                        "「こくばん」はいちばんじゃないよ。",
                    ],
                    "questionTranslation": "教室でジョージがいちばん好きだったものは？",
                    "choiceTranslations": [
                        "教科書。",
                        "机。",
                        "地図。",
                        "黒板。",
                    ],
                    "sourceEvidence": ["He liked looking at the textbooks most because they were so old."],
                    "questionAudio": "audio/q34.mp3",
                },
                {
                    "number": 35,
                    "question": "Now, George's favorite subject is",
                    "choices": ["math.", "English.", "history.", "music."],
                    "answer": 3,
                    "grammar": "now his favorite is history＝「今は歴史がいちばん好き」。",
                    "grammarSimple": "「いまはれきしがいちばんすき」って書いてあるよ！",
                    "choiceAnalysis": [
                        "math＝before の favorite（以前は好きだった）。",
                        "English＝before の favorite。",
                        "○ history.＝now his favorite is history と一致。",
                        "music＝書かれていない。",
                    ],
                    "choiceAnalysisSimple": [
                        "「すうがく」はむかしのすきなかもくだよ。",
                        "「えいご」もむかしのすきなかもくだよ。",
                        "○「れきし」がぴったり！いまのいちばんすき！",
                        "「おんがく」はちがうよ。",
                    ],
                    "questionTranslation": "今、ジョージのいちばん好きな科目は？",
                    "choiceTranslations": ["数学。", "英語。", "歴史。", "音楽。"],
                    "sourceEvidence": ["now his favorite is history"],
                    "questionAudio": "audio/q35.mp3",
                },
            ],
        },
    ],
}

for pa in section4["passages"]:
    for q in pa["questions"]:
        q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

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
