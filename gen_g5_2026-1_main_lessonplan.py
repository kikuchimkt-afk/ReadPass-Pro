# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検5級 data.json
lessonPlan（focusPoints × 3）— 大問1〜3の要点をテーマ別にリッチ化
一次ソース: 2026-1(本会場）/5級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade5", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "空所の前後を読んで「セット」で選ぶ",
    "subtitle": "Context Clues & Set Phrases",
    "explanation": (
        "大問1では、空所の直前・直後の英語が最大のヒントです。"
        "read a newspaper（新聞を読む）、people are waiting（人々が待っている）、"
        "tennis racket（テニスラケット）、drink your coffee（コーヒーを飲む）、"
        "goes to the mountain（山に行く）、how tall is ～?（どれくらい高い？）、"
        "You can leave now.（もう帰っていい）、Oh, I see.（なるほど）、"
        "at home（家で）、go hiking（ハイキングに行く）、after school（放課後）、"
        "wake up（起きる）、his class（彼の授業）、use mine（私のものを使う）、"
        "is studying（勉強している）は、それぞれ前後の語とセットで覚えると速いです。"
    ),
    "explanationSimple": (
        "まえうしろのことばをよんでね！"
        "read a newspaper＝「しんぶんをよむ」、at home＝「いえで」、"
        "go hiking＝「ハイキングに行く」、wake up＝「おきる」、"
        "use mine＝「わたしのものをつかう」、is studying＝「べんきょうしている」だよ！"
    ),
    "sourceQuote": (
        "read a newspaper / people are waiting / tennis racket / drink your coffee / "
        "goes to the mountain / how tall / You can leave / Oh, I see / at home / "
        "go hiking / after school / wake up / his class / use mine / is studying"
    ),
    "sourceLocation": "大問1 (1)〜(15)",
    "examples": [
        {
            "en": "A: What do you do in your free time, John?\nB: I read a newspaper every day.",
            "ja": "A: ジョン、暇なときは何をするの？\nB: 毎日新聞を読むんだ。",
            "note": "read a newspaper＝新聞を読む。free time の過ごし方として自然。Q1。",
            "noteSimple": "read a newspaper は「しんぶんをよむ」だよ。",
        },
        {
            "en": "A: Mike, how tall is that building?\nB: It's 200 meters.",
            "ja": "A: マイク、その建物はどれくらい高い？\nB: 200メートルだよ。",
            "note": "how tall is ～? ↔ 200 meters。高さを聞く定型表現。Q6。",
            "noteSimple": "how tall は「どれくらいたかい？」。メートルでこたえるよ。",
        },
        {
            "en": "A: Nancy, I can't find my eraser. Can I use yours?\nB: Yes. You can use mine.",
            "ja": "A: ナンシー、消しゴムが見つからない。あなたのを使ってもいい？\nB: うん。私のを使っていいわよ。",
            "note": "use mine＝所有代名詞 mine。「私の（消しゴム）を使う」。Q14。",
            "noteSimple": "use mine は「わたしのものをつかう」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "A: What do you do in your free time, John?\n"
            "B: I read a newspaper every day.\n\n"
            "Many people are waiting for the new pink train.\n\n"
            "A: Where is your tennis racket, Hiroki?\n"
            "B: It's in my bag, Mom.\n\n"
            "A: Mike, please drink your coffee before you go to school.\n\n"
            "Taro likes skiing. He goes to the mountain near his house every winter.\n\n"
            "A: Mike, how tall is that building?\n"
            "B: It's 200 meters.\n\n"
            "A: Can I go home now?\n"
            "B: Yes, John. You can leave now.\n\n"
            "A: Sorry, I can't go to the movie with you today.\n"
            "B: Oh, I see.\n\n"
            "A: Do you often eat fruit at home?\n\n"
            "A: Dad, can we go hiking tomorrow?\n"
            "B: Sure.\n\n"
            "Taro goes to the swimming pool after school.\n\n"
            "I wake up at seven every morning.\n\n"
            "Mr. Ford teaches English. We like his class very much.\n\n"
            "A: Can I use yours?\n"
            "B: Yes. You can use mine.\n\n"
            "A: Is Kent in the library?\n"
            "B: Yes, he is studying there."
        ),
        "ja": (
            "暇なときは新聞を読む。\n\n"
            "多くの人がピンクの電車を待っている。\n\n"
            "テニスラケットはかばんの中。\n\n"
            "学校に行く前にコーヒーを飲んで。\n\n"
            "冬は近くの山にスキーに行く。\n\n"
            "建物はどれくらい高い？→200メートル。\n\n"
            "もう帰っていいよ。\n\n"
            "映画に行けない→なるほど。\n\n"
            "家で果物を食べる？\n\n"
            "明日ハイキングに行こう。\n\n"
            "放課後プールに行く。\n\n"
            "毎朝7時に起きる。\n\n"
            "フォード先生の授業が好き。\n\n"
            "私の消しゴムを使っていい。\n\n"
            "ケントは図書館で勉強している。"
        ),
        "source": "大問1 (1)〜(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "read a newspaper",
        "people are waiting",
        "tennis racket",
        "drink your coffee",
        "goes to the mountain",
        "how tall",
        "You can leave",
        "Oh, I see",
        "at home",
        "go hiking",
        "after school",
        "wake up",
        "his class",
        "use mine",
        "is studying",
    ],
    "practiceQuestions": [
        {
            "q": "Q8で Oh, I play. が合わない理由は？",
            "a": "相手が映画に行けないと言った場面では Oh, I see.（なるほど）が自然。play はこの文脈では使わない。",
        },
        {
            "q": "Q14で use me が不正解な理由は？",
            "a": "use のあとは「消しゴム」という名詞が必要。mine（私のもの）が所有代名詞として正しい。me は「私を」となり不自然。",
        },
        {
            "q": "Q15で are studying が合わない理由は？",
            "a": "主語は he（三人称単数）。現在進行形は is studying。are / am は主語と一致しない。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "Oh, I see. って？", "a": "「なるほど」だよ。"},
        {"q": "at home って？", "a": "「いえで」だよ。"},
        {"q": "大問1のコツは？", "a": "まえうしろをよんで、セットのことばをさがすこと！"},
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話は「次のセリフ」で選ぶ",
    "subtitle": "Dialogue Flow & Set Phrases",
    "explanation": (
        "大問2は、空所の直後（ときどき直前）のセリフが最大のヒントです。"
        "Is Ken in your class? → Yes, he is.（クラスにいるかへの肯定）"
        "I enjoy basketball. → I do, too.（好き、への同意）"
        "work at a hospital → She's a nurse.（病院の仕事＝看護師）"
        "Let's go to that hamburger shop. → Good idea.（提案への同意）"
        "Are you from Australia? → Yes, I am.（出身への肯定）"
        "場面の型を知ると、選択肢を1つずつ試す手間が減ります。"
    ),
    "explanationSimple": (
        "かいわはつぎのセリフをよんでね！"
        "「クラスにいる？」→「うん、いるよ」、"
        "「バスケ好き」→「わたしも！」、"
        "「びょういんではたらう？」→「かんごしだよ」、"
        "「ハンバーガー店に行こう」→「いいね！」、"
        "「オーストラリア出身？」→「うん！」だよ。"
    ),
    "sourceQuote": (
        "Yes, he is / I do, too / She's a nurse / Good idea / Yes, I am"
    ),
    "sourceLocation": "大問2 (16)〜(20)",
    "examples": [
        {
            "en": "Girl 1: Is Ken in your class this year?\nGirl 2: Yes, he is. I like him a lot.",
            "ja": "女の子1：ケンは今年、あなたのクラスにいる？\n女の子2：うん、いるよ。彼のことがとても好きなの。",
            "note": "Is Ken in your class? → Yes, he is. の肯定のセット。Q16。",
            "noteSimple": "「いる？」→「うん、いるよ」だよ。",
        },
        {
            "en": "Boy: I enjoy basketball.\nGirl: I do, too. I often play it on Sundays.",
            "ja": "男の子：バスケットボールが好きなんだ。\n女の子：私もだよ。日曜日によくやるの。",
            "note": "I enjoy ～ → I do, too. で好きという意見に同意。Q17。",
            "noteSimple": "「すき」→「わたしも！」は I do, too. だよ。",
        },
        {
            "en": "Man: Let's go to that hamburger shop.\nWoman: Good idea. I'm hungry.",
            "ja": "男：あのハンバーガー店に行こう。\n女：いい考えだね。お腹が空いたわ。",
            "note": "Let's ～ → Good idea. で提案に同意。I'm hungry. とつながる。Q19。",
            "noteSimple": "「行こう」→「いいね！」は Good idea. だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Girl 1: Is Ken in your class this year?\n"
            "Girl 2: Yes, he is. I like him a lot.\n\n"
            "Boy: I enjoy basketball.\n"
            "Girl: I do, too. I often play it on Sundays.\n\n"
            "Teacher: Does your sister work at a hospital, Sally?\n"
            "Girl: Yes. She's a nurse.\n\n"
            "Man: Let's go to that hamburger shop.\n"
            "Woman: Good idea. I'm hungry.\n\n"
            "Man: Are you from Australia?\n"
            "Woman: Yes, I am."
        ),
        "ja": (
            "ケンはクラスにいる？→うん、いるよ。好きなの。\n\n"
            "バスケが好き→私も！日曜によくやる。\n\n"
            "お姉さんは病院で働く？→うん、看護師だよ。\n\n"
            "ハンバーガー店に行こう→いいね！お腹すいた。\n\n"
            "オーストラリア出身？→はい、そうです。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "Yes, he is",
        "I do, too",
        "She's a nurse",
        "Good idea",
        "Yes, I am",
    ],
    "practiceQuestions": [
        {
            "q": "Q16で No, I don't. が合わない理由は？",
            "a": "次のセリフは I like him a lot.（彼が好き）。否定の No, I don't. とは矛盾する。",
        },
        {
            "q": "Q18で I like volleyball. が合わない理由は？",
            "a": "先生は姉の仕事を聞いている。She's a nurse. が職業の説明。バレーボールの好みは答えにならない。",
        },
        {
            "q": "Q20で Yes, it is. が合わない理由は？",
            "a": "Are you from ～? は人への質問。答えは Yes, I am.（私は〜出身です）。it は物に使う。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "I do, too. って？", "a": "「わたしも（そう）だよ」だよ。"},
        {"q": "Good idea. って？", "a": "「いいね！」だよ。"},
        {"q": "会話問題のコツは？", "a": "つぎのセリフをよんで、なぜそう言うか考えること！"},
    ],
}

fp3 = {
    "id": "fp3",
    "title": "並べ替え——4語の「型」を知る",
    "subtitle": "Sentence Order Patterns (1st & 3rd)",
    "explanation": (
        "大問3は、日本文の意味から英文の型を思い出し、①〜④を並べる問題です。"
        "5級は4語・空所は1番目と3番目を選ぶ形式。"
        "① When is your English test?（いつ英語のテスト？）"
        "② What time is it in London?（ロンドンは何時？）"
        "③ Our homeroom teacher is Mr. Endo.（担任は遠藤先生）"
        "④ Kazuki wants some pizza for dinner.（一樹は夕食にピザが欲しい）"
        "⑤ What are you making for lunch?（昼食に何を作っている？）"
        "並べ終えたら、1番目と3番目の語が選択肢と一致するか最終確認します。"
    ),
    "explanationSimple": (
        "ならべかえは「かた」をおぼえよう！"
        "When is your＝いつ〜？、What time is it＝なんじ？、"
        "Our homeroom teacher＝したんいんせんせい、"
        "Kazuki wants some pizza＝ピザがほしい、"
        "What are you making＝なにをつくってる？だよ。"
    ),
    "sourceQuote": (
        "When is your English test / What time is it in London / "
        "Our homeroom teacher is Mr. Endo / Kazuki wants some pizza for dinner / "
        "What are you making for lunch"
    ),
    "sourceLocation": "大問3 (21)〜(25)",
    "examples": [
        {
            "en": "When is your English test?",
            "ja": "あなたの英語のテストはいつですか。",
            "note": "When is your ...? が疑問文の型。1番目 when、3番目 your。Q21。",
            "noteSimple": "When is your は「いつ〜？」だよ。",
        },
        {
            "en": "What time is it in London?",
            "ja": "ロンドンは何時ですか。",
            "note": "What time is it in ～? が時刻を聞く型。1番目 time、3番目 it。Q22。",
            "noteSimple": "What time is it は「なんじ？」だよ。",
        },
        {
            "en": "What are you making for lunch?",
            "ja": "あなたは昼食に何を作っていますか。",
            "note": "What are you making ...? が現在進行形の疑問文。1番目 what、3番目 you。Q25。",
            "noteSimple": "What are you making は「なにをつくってる？」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "When is your English test?\n\n"
            "What time is it in London?\n\n"
            "Our homeroom teacher is Mr. Endo.\n\n"
            "Kazuki wants some pizza for dinner.\n\n"
            "What are you making for lunch?"
        ),
        "ja": (
            "あなたの英語のテストはいつ？\n\n"
            "ロンドンは何時？\n\n"
            "私たちの担任は遠藤先生です。\n\n"
            "一樹は夕食にピザが欲しいです。\n\n"
            "あなたは昼食に何を作っていますか。"
        ),
        "source": "大問3 (21)〜(25)",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "When is your English test",
        "What time is it in London",
        "Our homeroom teacher",
        "Kazuki wants some pizza",
        "What are you making for lunch",
    ],
    "practiceQuestions": [
        {
            "q": "Q21で ②─④ が正解になる完成文は？1・3番目の語は？",
            "a": "When is your English test? 1番目 when（②）、3番目 your（④）。",
        },
        {
            "q": "Q23で ①─③ が正解になる理由は？",
            "a": "Our homeroom teacher is Mr. Endo. で 1番目 our（①）、3番目 teacher（③）。",
        },
        {
            "q": "Q24とQ25の違いは？",
            "a": "Q24は Kazuki wants some pizza（平叙文・三単現 wants）。Q25は What are you making?（疑問文・進行形）。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "When is your って？", "a": "「いつ〜？」だよ。"},
        {"q": "Our homeroom teacher って？", "a": "「わたしたちのしたんいんせんせい」だよ。"},
        {"q": "並べ替えのさいごのチェックは？", "a": "1ばんめと3ばんめが選択肢とあうかな？"},
    ],
}

for fp in (fp1, fp2, fp3):
    fp_id = fp["id"]
    for ei, ex in enumerate(fp["examples"]):
        ex["audio"] = f"audio/{fp_id}_ex{ei + 1}.mp3"
    fp["sourceQuoteAudio"] = f"audio/{fp_id}_source.mp3"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {
    "title": "英検5級 2026年度 第1回",
    "focusPoints": [fp1, fp2, fp3],
}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(data['lessonPlan']['focusPoints'])} focusPoints) to {DATA_PATH}")
