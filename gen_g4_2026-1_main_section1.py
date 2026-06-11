# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
大問1（vocabulary型）Q1〜15 — 解説・和訳付き
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

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A: I want to make some pancakes for breakfast, but we don't have any (　).\nB: I'll go to the store and get some.",
            "choices": ["flowers", "eggs", "books", "sports"],
            "answer": 2,
            "grammar": "don't have any eggs＝「卵がない」。パンケーキを作る材料として eggs が自然。",
            "grammarSimple": "eggs は「たまご」。パンケーキをつくるのにたまごがないよ！",
            "choiceAnalysis": [
                "flowers＝花。パンケーキの材料として不自然。",
                "○ eggs＝卵。make pancakes と don't have any eggs がつながる。",
                "books＝本。食べ物の材料ではない。",
                "sports＝スポーツ。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "flowers は「はな」。たべものじゃないよ。",
                "○ eggs がぴったり！「たまご」がない！",
                "books は「ほん」。合わないよ。",
                "sports は「スポーツ」。合わないよ。",
            ],
            "questionAudio": "audio/q1.mp3",
            "translation": "A: 朝食にパンケーキを作りたいんだけど、（　）が全然ないんだ。\nB: 店に行って買ってくるよ。",
            "choiceTranslations": ["花", "卵", "本", "スポーツ"],
        },
        {
            "number": 2,
            "text": "A: I want to call my mother, but I don't have a phone.\nB: You can (　) my phone.",
            "choices": ["climb", "leave", "use", "send"],
            "answer": 3,
            "grammar": "You can use my phone.＝「私の電話を使っていいよ」。電話がない人への助け。",
            "grammarSimple": "use は「つかう」。でんわがないから、わたしのでんわをつかっていいよ！",
            "choiceAnalysis": [
                "climb my phone→「電話を登る」では意味が通らない。",
                "leave my phone→「電話を去る」では不自然。",
                "○ use＝使う。use my phone が自然。",
                "send my phone→「電話を送る」では文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "climb は「のぼる」。でんわには合わないよ。",
                "leave は「去る」。合わないよ。",
                "○ use がぴったり！「つかう」！",
                "send は「おくる」。合わないよ。",
            ],
            "questionAudio": "audio/q2.mp3",
            "translation": "A: お母さんに電話したいんだけど、電話を持ってないんだ。\nB: 私の電話を（　）っていいよ。",
            "choiceTranslations": ["登る", "去る", "使う", "送る"],
        },
        {
            "number": 3,
            "text": "A: Mom, I want to make some cookies.\nB: All right, but please (　) this carrot first.",
            "choices": ["cut", "arrive", "hit", "run"],
            "answer": 1,
            "grammar": "cut this carrot＝「このニンジンを切る」。クッキー作りの前準備。",
            "grammarSimple": "cut は「きる」。クッキーをつくるまえに、にんじんをきってね！",
            "choiceAnalysis": [
                "○ cut＝切る。クッキー作りの前に野菜を切る場面。",
                "arrive this carrot→「ニンジンが着く」では意味が通らない。",
                "hit this carrot→「ニンジンを打つ」では不自然。",
                "run this carrot→「ニンジンを走る」では不自然。",
            ],
            "choiceAnalysisSimple": [
                "○ cut がぴったり！「きる」！",
                "arrive は「つく」。にんじんには合わないよ。",
                "hit は「うつ」。合わないよ。",
                "run は「はしる」。合わないよ。",
            ],
            "questionAudio": "audio/q3.mp3",
            "translation": "A: ママ、クッキーを作りたい！\nB: いいわよ。でも、先にこのニンジンを（　）てね。",
            "choiceTranslations": ["切る", "着く", "打つ", "走る"],
        },
        {
            "number": 4,
            "text": "A: Is it warm in your (　) now?\nB: Yes, it's spring.",
            "choices": ["country", "ticket", "animal", "road"],
            "answer": 1,
            "grammar": "in your country＝「あなたの国では」。春が暖かい＝国の気候の話。",
            "grammarSimple": "country は「くに」。あなたのくにはいまあたたかい？はるだよ！",
            "choiceAnalysis": [
                "○ country＝国。warm in your country と it's spring がつながる。",
                "ticket＝切符。暖かさの場所として不自然。",
                "animal＝動物。in your animal では意味が通らない。",
                "road＝道路。気候の話には合わない。",
            ],
            "choiceAnalysisSimple": [
                "○ country がぴったり！「くに」！",
                "ticket は「きっぷ」。合わないよ。",
                "animal は「どうぶつ」。合わないよ。",
                "road は「みち」。合わないよ。",
            ],
            "questionAudio": "audio/q4.mp3",
            "translation": "A: 今、あなたの（　）は暖かい？\nB: うん、春だよ。",
            "choiceTranslations": ["国", "切符", "動物", "道路"],
        },
        {
            "number": 5,
            "text": "Taro enjoyed the chorus (　) on TV yesterday. He wants to join a chorus at school.",
            "choices": ["wall", "hobby", "contest", "trip"],
            "answer": 3,
            "grammar": "chorus contest＝「合唱コンテスト」。テレビで見て、学校の合唱に入りたい流れ。",
            "grammarSimple": "contest は「コンテスト」。テレビで合唱コンテストをみて、がっこうの合唱に入りたいんだ！",
            "choiceAnalysis": [
                "chorus wall→「合唱の壁」では意味が通らない。",
                "chorus hobby→「合唱の趣味」ではテレビ番組名として不自然。",
                "○ contest＝コンテスト。chorus contest on TV が自然。",
                "chorus trip→「合唱の旅行」では文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "wall は「かべ」。合わないよ。",
                "hobby は「しゅみ」。テレビの番組には合わないよ。",
                "○ contest がぴったり！「コンテスト」！",
                "trip は「りょこう」。合わないよ。",
            ],
            "questionAudio": "audio/q5.mp3",
            "translation": "タロウは昨日テレビで合唱（　）を楽しんだ。学校の合唱に入りたいと思っている。",
            "choiceTranslations": ["壁", "趣味", "コンテスト", "旅行"],
        },
        {
            "number": 6,
            "text": "A: Can I study in the library today?\nB: Yes, it's (　) now.",
            "choices": ["cold", "open", "late", "favorite"],
            "answer": 2,
            "grammar": "it's open now＝「今開いている」。図書館で勉強できるかの答え。",
            "grammarSimple": "open は「あいている」。いまとしょかんはあいてるよ！",
            "choiceAnalysis": [
                "it's cold now→「寒い」は開館の可否の答えにならない。",
                "○ open＝開いている。Can I study in the library? への自然な返答。",
                "it's late now→「遅い」だけでは勉強できるかの答えとして弱い。",
                "it's favorite now→favorite は名詞・形容詞だがこの文脈では不自然。",
            ],
            "choiceAnalysisSimple": [
                "cold は「さむい」。あいてるかの答えじゃないよ。",
                "○ open がぴったり！「あいている」！",
                "late は「おそい」。合わないよ。",
                "favorite は「すきな」。合わないよ。",
            ],
            "questionAudio": "audio/q6.mp3",
            "translation": "A: 今日、図書館で勉強してもいい？\nB: うん、今（　）よ。",
            "choiceTranslations": ["寒い", "開いている", "遅い", "お気に入りの"],
        },
        {
            "number": 7,
            "text": "Sally went to eat Chinese food in a big (　) last weekend.",
            "choices": ["city", "word", "body", "point"],
            "answer": 1,
            "grammar": "in a big city＝「大きな街で」。中華料理を食べに行った場所。",
            "grammarSimple": "city は「まち」。おおきなまちでちゅうかりょうりをたべに行ったよ！",
            "choiceAnalysis": [
                "○ city＝都市・街。eat Chinese food in a big city が自然。",
                "word＝単語。in a big word では意味が通らない。",
                "body＝体。食べに行く場所として不自然。",
                "point＝点。in a big point では不自然。",
            ],
            "choiceAnalysisSimple": [
                "○ city がぴったり！「おおきなまち」！",
                "word は「ことば」。合わないよ。",
                "body は「からだ」。合わないよ。",
                "point は「てん」。合わないよ。",
            ],
            "questionAudio": "audio/q7.mp3",
            "translation": "サリーは先週末、大きな（　）で中華料理を食べに行った。",
            "choiceTranslations": ["都市・街", "単語", "体", "点"],
        },
        {
            "number": 8,
            "text": "A: What do you want to do tomorrow afternoon?\nB: I have an (　). Let's go to the aquarium.",
            "choices": ["end", "idea", "arm", "eraser"],
            "answer": 2,
            "grammar": "I have an idea.＝「いい考えがある」。水族館に行こうという提案。",
            "grammarSimple": "idea は「アイデア」。すいぞくかんに行こう、というアイデアだよ！",
            "choiceAnalysis": [
                "have an end→「終わりを持っている」では提案にならない。",
                "○ idea＝アイデア。Let's go to the aquarium. とつながる。",
                "have an arm→「腕を持っている」では文脈に合わない。",
                "have an eraser→「消しゴムを持っている」では提案にならない。",
            ],
            "choiceAnalysisSimple": [
                "end は「おわり」。提案にならないよ。",
                "○ idea がぴったり！「アイデア」！",
                "arm は「うで」。合わないよ。",
                "eraser は「けしゴム」。合わないよ。",
            ],
            "questionAudio": "audio/q8.mp3",
            "translation": "A: 明日の午後、何をしたい？\nB: （　）があるんだ。水族館に行こう。",
            "choiceTranslations": ["終わり", "アイデア", "腕", "消しゴム"],
        },
        {
            "number": 9,
            "text": "A: These are my new glasses. What do you (　) of them?\nB: They're really nice, Grandma.",
            "choices": ["watch", "think", "tell", "finish"],
            "answer": 2,
            "grammar": "What do you think of ～?＝「〜についてどう思う？」。新しいメガネへの感想を聞く。",
            "grammarSimple": "think of は「〜についてどう思う」。あたらしいめがね、どう思う？",
            "choiceAnalysis": [
                "watch of them→What do you watch of them? では使わない。",
                "○ think＝think of ～ で「〜についてどう思う」。They're really nice. と呼応。",
                "tell of them→What do you tell of them? では不自然。",
                "finish of them→使わない。",
            ],
            "choiceAnalysisSimple": [
                "watch は「みる」。think of じゃないよ。",
                "○ think がぴったり！think of で「どう思う」！",
                "tell は「いう」。合わないよ。",
                "finish は「おえる」。合わないよ。",
            ],
            "questionAudio": "audio/q9.mp3",
            "translation": "A: これ、私の新しいメガネよ。どう思う？\nB: とてもいいわね、おばあちゃん。",
            "choiceTranslations": ["見る", "思う", "言う", "終える"],
        },
        {
            "number": 10,
            "text": "A: Mom, I'm going to play in the soccer game tomorrow.\nB: Good (　) you. You practiced a lot.",
            "choices": ["for", "with", "in", "after"],
            "answer": 1,
            "grammar": "Good for you.＝「よかったね・がんばってね」。練習をたくさんした子への励まし。",
            "grammarSimple": "Good for you. は「がんばってね」。たくさんれんしゅうしたんだね！",
            "choiceAnalysis": [
                "○ for＝Good for you. の定型表現。",
                "Good with you→使わない。",
                "Good in you→使わない。",
                "Good after you→使わない。",
            ],
            "choiceAnalysisSimple": [
                "○ for がぴったり！Good for you. で「がんばって」！",
                "with は合わないよ。",
                "in は合わないよ。",
                "after は合わないよ。",
            ],
            "questionAudio": "audio/q10.mp3",
            "translation": "A: ママ、明日サッカーの試合に出るんだ。\nB: （　）。たくさん練習したのね。",
            "choiceTranslations": ["〜にとって（Good for you）", "〜と一緒に", "〜の中で", "〜の後に"],
        },
        {
            "number": 11,
            "text": "A: Did you (　) about Dan?\nB: Yes. He's going to move back to England.",
            "choices": ["hear", "wait", "run", "want"],
            "answer": 1,
            "grammar": "Did you hear about Dan?＝「ダンのこと聞いた？」。イギリスに戻る話題。",
            "grammarSimple": "hear about は「〜のことをきいた？」。ダンがイギリスにもどるってきいた？",
            "choiceAnalysis": [
                "○ hear＝聞く。hear about Dan が自然。move back to England が続く。",
                "wait about Dan→「ダンについて待った？」では不自然。",
                "run about Dan→使わない。",
                "want about Dan→使わない。",
            ],
            "choiceAnalysisSimple": [
                "○ hear がぴったり！「きいた？」！",
                "wait は「まつ」。合わないよ。",
                "run は「はしる」。合わないよ。",
                "want は「ほしい」。合わないよ。",
            ],
            "questionAudio": "audio/q11.mp3",
            "translation": "A: ダンのこと（　）？\nB: うん。イギリスに戻ることになるんだ。",
            "choiceTranslations": ["聞く", "待つ", "走る", "望む"],
        },
        {
            "number": 12,
            "text": "A: Here are four cookies, Bob. Please (　) them with your sister.\nB: OK. I'll give her two of them.",
            "choices": ["share", "answer", "cry", "run"],
            "answer": 1,
            "grammar": "share them with your sister＝「妹と分け合って」。4つあるクッキーを分ける場面。",
            "grammarSimple": "share は「わけあう」。いもうととクッキーをわけあってね！",
            "choiceAnalysis": [
                "○ share＝分け合う。give her two of them とつながる。",
                "answer them→「クッキーに答える」では意味が通らない。",
                "cry them→使わない。",
                "run them→使わない。",
            ],
            "choiceAnalysisSimple": [
                "○ share がぴったり！「わけあう」！",
                "answer は「こたえる」。合わないよ。",
                "cry は「なく」。合わないよ。",
                "run は「はしる」。合わないよ。",
            ],
            "questionAudio": "audio/q12.mp3",
            "translation": "A: ボブ、クッキーが4つあるよ。妹と（　）てね。\nB: わかった。2つあげるよ。",
            "choiceTranslations": ["分け合う", "答える", "泣く", "走る"],
        },
        {
            "number": 13,
            "text": "A: Today, apples are (　) than bananas.\nB: OK. Let's get some apples.",
            "choices": ["cheap", "cheapest", "the cheapest", "cheaper"],
            "answer": 4,
            "grammar": "cheaper than ～＝「〜より安い」。比較級＋than の形。",
            "grammarSimple": "cheaper than は「〜よりやすい」。りんごのほうがバナナよりやすいよ！",
            "choiceAnalysis": [
                "cheap than→比較の than には比較級 cheaper が必要。",
                "cheapest than→最上級と than は一緒に使わない。",
                "the cheapest than→文法的に誤り。",
                "○ cheaper＝比較級。apples are cheaper than bananas. が正しい。",
            ],
            "choiceAnalysisSimple": [
                "cheap は「やすい」だけ。than には cheaper だよ。",
                "cheapest は「いちばんやすい」。than と一緒に使わないよ。",
                "the cheapest も than とは合わないよ。",
                "○ cheaper がぴったり！「よりやすい」！",
            ],
            "questionAudio": "audio/q13.mp3",
            "translation": "A: 今日、リンゴはバナナより（　）よ。\nB: わかった。リンゴを買おう。",
            "choiceTranslations": ["安い", "最も安い", "一番安い", "より安い"],
        },
        {
            "number": 14,
            "text": "The students (　) 50 meters in the school pool yesterday.",
            "choices": ["swim", "swam", "swimming", "to swim"],
            "answer": 2,
            "grammar": "yesterday があるので過去形 swam。「50メートル泳いだ」。",
            "grammarSimple": "swam は swim の過去形。きのう、がっこうのプールで50メートルおよいだよ！",
            "choiceAnalysis": [
                "swim＝現在形。yesterday と時制が合わない。",
                "○ swam＝過去形。yesterday と一致。",
                "swimming＝進行形・動名詞。述語として主に使えない。",
                "to swim＝不定詞。文の述語として不自然。",
            ],
            "choiceAnalysisSimple": [
                "swim は「いま」。きのうには合わないよ。",
                "○ swam がぴったり！「およいだ」！",
                "swimming はそのままでは合わないよ。",
                "to swim はそのままでは合わないよ。",
            ],
            "questionAudio": "audio/q14.mp3",
            "translation": "生徒たちは昨日、学校のプールで50メートル（　）。",
            "choiceTranslations": ["泳ぐ（現在）", "泳いだ（過去）", "泳いでいる", "泳ぐために"],
        },
        {
            "number": 15,
            "text": "A: You (　) read this book before the test next Monday.\nB: OK, Mr. Peterson.",
            "choices": ["have", "be", "must", "were"],
            "answer": 3,
            "grammar": "must read＝「読まなければならない」。テスト前の宿題としての指示。",
            "grammarSimple": "must read は「よまなきゃ」。らいしゅうのテストまえにこの本をよんでね！",
            "choiceAnalysis": [
                "have read→「読んだことがある」では先生の指示にならない。",
                "be read→文法的に不自然。",
                "○ must＝〜しなければならない。must read this book が自然。",
                "were read→過去形・受動態になり文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "have は「よんだことがある」。しじには合わないよ。",
                "be はそのままでは合わないよ。",
                "○ must がぴったり！「よまなきゃ」！",
                "were は「だった」。合わないよ。",
            ],
            "questionAudio": "audio/q15.mp3",
            "translation": "A: 来週月曜のテストの前に、この本を（　）読みなさい。\nB: はい、ピーターソン先生。",
            "choiceTranslations": ["〜したことがある", "〜である", "〜しなければならない", "〜だった"],
        },
    ],
}

for q in section1["questions"]:
    q["choiceAnalysis"] = mark_ca(q["choiceAnalysis"], q["answer"])

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
