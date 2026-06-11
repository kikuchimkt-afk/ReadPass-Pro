# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検4級 data.json
lessonPlan（focusPoints × 4）— 大問1〜4の要点をテーマ別にリッチ化
一次ソース: 2026-1(本会場）/4級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "単語は「セット」で覚える",
    "subtitle": "Collocations, Comparatives & Grammar Forms",
    "explanation": (
        "大問1では、単語ひとつより「決まった組み合わせ」が鍵です。"
        "don't have any eggs（卵がない）、What do you think of ～?（〜についてどう思う？）、"
        "Good for you.（よかったね）、cheaper than（〜より安い）、must read（読まなければならない）"
        "は、空所の前後とセットで意味が決まります。"
        "chorus contest（合唱コンテスト）、it's open now（今開いている）、"
        "swam yesterday（昨日泳いだ）のように、名詞のセット・時制も押さえましょう。"
    ),
    "explanationSimple": (
        "たんごはセットでおぼえよう！think of は「〜についてどう思う」、"
        "Good for you は「がんばってね」、cheaper than は「〜よりやすい」、"
        "must read は「よまなきゃ」だよ。"
    ),
    "sourceQuote": "don't have any eggs / What do you think of / Good for you / cheaper than bananas / must read this book",
    "sourceLocation": "大問1 (1)(9)(10)(13)(15)",
    "examples": [
        {
            "en": "I want to make some pancakes, but we don't have any eggs.",
            "ja": "パンケーキを作りたいんだけど、卵がないんだ。",
            "note": "don't have any eggs＝「卵がない」。make pancakes とセット。",
            "noteSimple": "don't have any eggs は「たまごがない」だよ。",
        },
        {
            "en": "What do you think of them? They're really nice, Grandma.",
            "ja": "どう思う？とてもいいわね、おばあちゃん。",
            "note": "think of ～?＝「〜についてどう思う？」。新しいメガネへの感想。",
            "noteSimple": "think of は「〜についてどう思う」だよ。",
        },
        {
            "en": "Good for you. You practiced a lot. Today, apples are cheaper than bananas.",
            "ja": "よかったね。たくさん練習したのね。今日、リンゴはバナナより安いよ。",
            "note": "Good for you.＝励まし。cheaper than＝比較級＋than。",
            "noteSimple": "Good for you は「がんばって」、cheaper than は「〜よりやすい」！",
        },
    ],
    "practicePassage": {
        "en": (
            "I want to make some pancakes, but we don't have any eggs.\n\n"
            "You can use my phone.\n\n"
            "Taro enjoyed the chorus contest on TV yesterday.\n\n"
            "Yes, it's open now.\n\n"
            "What do you think of them? They're really nice.\n\n"
            "Good for you. You practiced a lot.\n\n"
            "Today, apples are cheaper than bananas.\n\n"
            "The students swam 50 meters in the school pool yesterday.\n\n"
            "You must read this book before the test next Monday."
        ),
        "ja": (
            "パンケーキを作りたいが卵がない。\n\n"
            "私の電話を使っていいよ。\n\n"
            "合唱コンテストを楽しんだ。\n\n"
            "今開いているよ。\n\n"
            "どう思う？とてもいいね。\n\n"
            "よかったね。たくさん練習したのね。\n\n"
            "リンゴはバナナより安い。\n\n"
            "昨日50メートル泳いだ。\n\n"
            "テスト前にこの本を読みなさい。"
        ),
        "source": "大問1 (1)(2)(5)(6)(9)(10)(13)(14)(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "don't have any eggs",
        "use my phone",
        "chorus contest",
        "it's open now",
        "think of them",
        "Good for you",
        "cheaper than",
        "must read",
    ],
    "practiceQuestions": [
        {
            "q": "Q13で cheapest が不正解な理由は？",
            "a": "than の前は比較級 cheaper。cheapest / the cheapest は最上級で than と一緒に使わない。",
        },
        {
            "q": "Q10で Good with you が合わない理由は？",
            "a": "Good for you. が定型の励ましの表現。with / in / after では使わない。",
        },
        {
            "q": "Q14で swam が正解なのは、文中のどの語がヒント？",
            "a": "yesterday があるので過去形 swam。「昨日泳いだ」＝過去の事実。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "think of ってどういう意味？", "a": "「〜についてどう思う」だよ。"},
        {"q": "cheaper than って？", "a": "「〜よりやすい」だよ。"},
        {"q": "must read って？", "a": "「よまなきゃ」だよ。"},
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話は「次のセリフ」で選ぶ",
    "subtitle": "Dialogue Flow & Set Phrases",
    "explanation": (
        "大問2は、空所の直後（ときどき直前）のセリフが最大のヒントです。"
        "Of course you can. Here you are. → Can I borrow yours?（借りていい？）"
        "Let's climb the one over there. → It's too tall.（高すぎる）"
        "Two dollars. → How much are they?（いくら？）"
        "Thanks. → It's on the kitchen table.（キッチンのテーブルの上）"
        "I'm just a little tired. → Are you OK?（大丈夫？）"
    ),
    "explanationSimple": (
        "かいわはつぎのセリフをよんでね！"
        "「はいどうぞ」→「かりていい？」。"
        "「あっちの木にのぼろう」→「たかすぎる」。"
        "「2ドル」→「いくら？」。"
    ),
    "sourceQuote": "Can I borrow yours / It's too tall / How much are they / on the kitchen table / Are you OK",
    "sourceLocation": "大問2 (16)〜(20)",
    "examples": [
        {
            "en": "Girl: I forgot my red pen. Can I borrow yours?\nBoy: Of course you can. Here you are.",
            "ja": "女の子：赤いペンを忘れた。借りていい？\n男の子：もちろん。はいどうぞ。",
            "note": "borrow yours と Here you are がセット。",
            "noteSimple": "「かりていい？」→「はいどうぞ」だよ。",
        },
        {
            "en": "Girl 1: I want to climb this tree.\nGirl 2: It's too tall. Let's climb the one over there.",
            "ja": "女の子1：この木に登りたい。\n女の子2：高すぎるよ。あっちの木に登ろう。",
            "note": "too tall が別の木を提案する理由。",
            "noteSimple": "「たかすぎる」からあっちの木だよ。",
        },
        {
            "en": "Man: How much are they?\nClerk: Two dollars.",
            "ja": "男：いくらですか？\n店員：2ドルです。",
            "note": "How much are they? と値段の答えがセット。",
            "noteSimple": "「いくら？」→「2ドル」！",
        },
    ],
    "practicePassage": {
        "en": (
            "Girl: I forgot my red pen. Can I borrow yours?\n"
            "Boy: Of course you can. Here you are.\n\n"
            "Girl 1: I want to climb this tree.\n"
            "Girl 2: It's too tall. Let's climb the one over there.\n\n"
            "Man: Excuse me. I want to buy these socks. How much are they?\n"
            "Clerk: Two dollars.\n\n"
            "Daughter: Dad, I can't find my social studies textbook.\n"
            "Father: It's on the kitchen table.\n"
            "Daughter: Thanks.\n\n"
            "Girl 1: Jenny, you don't look well today. Are you OK?\n"
            "Girl 2: I'm fine. I'm just a little tired."
        ),
        "ja": (
            "赤いペンを忘れた。借りていい？→もちろん、はいどうぞ。\n\n"
            "この木に登りたい。→高すぎる。あっちの木にしよう。\n\n"
            "靴下を買いたい。いくら？→2ドル。\n\n"
            "教科書が見つからない。→キッチンのテーブルの上。ありがとう。\n\n"
            "元気そうに見えない。大丈夫？→ちょっと疲れただけ。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "Can I borrow yours",
        "It's too tall",
        "How much are they",
        "on the kitchen table",
        "Are you OK",
    ],
    "practiceQuestions": [
        {
            "q": "Q16で Will you go home soon? が合わない理由は？",
            "a": "次のセリフは Of course you can. Here you are.（貸してあげる）。家に帰る話ではない。",
        },
        {
            "q": "Q18で How many do you have? が合わない理由は？",
            "a": "店員の答えは Two dollars.（値段）。個数を聞く質問ではない。",
        },
        {
            "q": "Q20で Can I go home? が合わない理由は？",
            "a": "Jenny は I'm fine. I'm just a little tired. と答える。相手の体調を心配する Are you OK? が自然。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "Can I borrow yours って？", "a": "「あなたのをかりていい？」だよ。"},
        {"q": "How much are they? って？", "a": "「いくら？」だよ。"},
        {"q": "会話問題のコツは？", "a": "つぎのセリフをよんで、なぜそう言うか考えること！"},
    ],
}

fp3 = {
    "id": "fp3",
    "title": "並べ替え——5つの「型」を知る",
    "subtitle": "Sentence Order Patterns",
    "explanation": (
        "大問3は、日本文の意味から英文の「型」を思い出す問題です。"
        "① Why did you ...?（なぜ〜した？）"
        "② May I call you ...?（〜してもいい？）"
        "③ You can see lots of ...（〜を見ることができる）"
        "④ leave home for school（家を出て学校へ）"
        "⑤ Could you wash these ...?（〜してくれますか？）"
        "並べ終えたら、2番目と4番目の語が選択肢と一致するか確認するのが最終チェックです。"
    ),
    "explanationSimple": (
        "ならべかえは「かた」をおぼえよう！"
        "Why did you＝なぜ〜した？、May I call you＝でんわしていい？、"
        "You can see＝みえる、leave home for school＝いえをでてがっこうへ、"
        "Could you wash＝あらってくれる？だよ。"
    ),
    "sourceQuote": "Why did you get up / May I call you / You can see lots of high mountains / leave home for school / Could you wash these coffee cups",
    "sourceLocation": "大問3 (21)〜(25)",
    "examples": [
        {
            "en": "Why did you get up so early this morning?",
            "ja": "なぜ今朝、そんなに早く起きたの？",
            "note": "Why did you ...? が疑問文の型。",
            "noteSimple": "Why did you は「なぜ〜した？」だよ。",
        },
        {
            "en": "May I call you this afternoon?",
            "ja": "今日の午後、電話してもいい？",
            "note": "May I ...? で許可を求める丁寧な表現。",
            "noteSimple": "May I call you は「でんわしていい？」だよ。",
        },
        {
            "en": "Could you wash these coffee cups, please?",
            "ja": "これらのコーヒーカップを洗ってくれますか？",
            "note": "Could you ...? で依頼。these coffee cups が目的語。",
            "noteSimple": "Could you wash は「あらってくれる？」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Why did you get up so early this morning?\n\n"
            "May I call you this afternoon?\n\n"
            "You can see lots of high mountains in Nepal.\n\n"
            "I leave home for school at seven o'clock every morning.\n\n"
            "Could you wash these coffee cups, please?"
        ),
        "ja": (
            "なぜ今朝そんなに早く起きたの？\n\n"
            "今日の午後、電話していい？\n\n"
            "ネパールではたくさんの高い山が見える。\n\n"
            "毎朝7時に家を出て学校へ向かう。\n\n"
            "これらのコーヒーカップを洗ってくれますか？"
        ),
        "source": "大問3 (21)〜(25)",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "Why did you get up",
        "May I call you",
        "You can see lots of",
        "leave home for school",
        "Could you wash these",
    ],
    "practiceQuestions": [
        {
            "q": "Q21で ⑤−③ が正解になる完成文は？2・4番目の語は？",
            "a": "Why did you get up so early this morning? 2番目 did（⑤）、4番目 get（③）。",
        },
        {
            "q": "Q24で leave home for school の home と school は何番目？",
            "a": "2番目 home（⑤）、4番目 school（②）。I leave home for school at ... の語順。",
        },
        {
            "q": "Q25の Could you と you の違いは？",
            "a": "Could you wash ...? の you は「あなたに」依頼する相手。2番目の you（②）と4番目の these（⑤）を区別する。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "Why did you get up って？", "a": "「なぜおきたの？」だよ。"},
        {"q": "leave home for school って？", "a": "「いえをでてがっこうへ」だよ。"},
        {"q": "並べ替えのさいごのチェックは？", "a": "2ばんめと4ばんめが選択肢とあうかな？"},
    ],
}

fp4 = {
    "id": "fp4",
    "title": "読解——お知らせ・メール・物語の読み分け",
    "subtitle": "Notice, E-mail & Story Reading",
    "explanation": (
        "大問4は3タイプの読み方があります。"
        "【お知らせ】gym＝speech、music room＝three songs。場所と出来事を混同しない（Q26-27）。"
        "【メール】next month＝訪問の時期、three babies＝子猫の数、yesterday＝友達が訪問（Q28-30）。"
        "【物語】sister wanted to go＝行った理由、forty years old＝黒板の年数（建物80年と区別）、"
        "dark brown＝机の色、textbooks most＝いちばん好きだったもの、now favorite is history（Q31-35）。"
    ),
    "explanationSimple": (
        "よみものは3タイプ！"
        "お知らせ＝たいいくかんはスピーチ、おんがくしつは3きょく！"
        "メール＝らいげつ・3ひき・ともだちがきのうきた！"
        "ものがたり＝いもうとが行きたがった、こくばん40ねん、きょうかしょがいちばんすき！"
    ),
    "sourceQuote": "give a speech in the gym / play three songs / visit your home next month / She has three babies / his sister wanted to go / textbooks most / now his favorite is history",
    "sourceLocation": "大問4A・4B・4C",
    "examples": [
        {
            "en": "He will first give a speech in the gym and then play three songs in the music room.",
            "ja": "まず体育館でスピーチをし、その後音楽室で3曲演奏する。",
            "note": "gym＝speech、music room＝songs。場所ごとに内容が違う。",
            "noteSimple": "たいいくかんはスピーチ、おんがくしつはえんそうだよ。",
        },
        {
            "en": "Can I visit your home next month? She has three babies, and they are very cute.",
            "ja": "来月訪問していい？子猫が3匹いてとてもかわいい。",
            "note": "next month＝訪問時期。three babies＝子猫の数。",
            "noteSimple": "「らいげつ」に行く、「3ひき」いるよ。",
        },
        {
            "en": "His sister wanted to go to a history museum. He liked looking at the textbooks most. Now his favorite is history.",
            "ja": "妹が博物館に行きたがった。教科書を見るのがいちばん好きだった。今は歴史が好き。",
            "note": "行った理由・教室で好きだったもの・今の好きな科目を区別。",
            "noteSimple": "いもうとが行きたがった、きょうかしょがすき、いまはれきし！",
        },
    ],
    "practicePassage": {
        "en": (
            "He will first give a speech in the gym and then play three songs in the music room.\n\n"
            "Can I visit your home next month? She has three babies, and they are very cute.\n"
            "Yesterday, one of my friends visited me and saw them, too!\n\n"
            "Recently, his sister wanted to go to a history museum. So, his family went to the museum last Saturday.\n"
            "The blackboard was forty years old. They were dark brown.\n"
            "He liked looking at the textbooks most because they were so old.\n"
            "Now his favorite is history."
        ),
        "ja": (
            "【お知らせ】体育館でスピーチ、音楽室で3曲演奏。\n\n"
            "【メール】来月訪問していい？子猫3匹。昨日友達が訪問。\n\n"
            "【物語】妹が博物館に行きたがった。黒板40年。机は濃い茶色。教科書がいちばん好き。今は歴史が好き。"
        ),
        "source": "大問4A「Musician Will Visit Our School」/ 4B「How are your cats?」/ 4C「A Visit to a History Museum」",
        "audioFile": "audio/practice_pp4.mp3",
    },
    "highlightPatterns": [
        "give a speech in the gym",
        "play three songs",
        "next month",
        "three babies",
        "friends visited me",
        "sister wanted to go",
        "forty years old",
        "dark brown",
        "textbooks most",
        "favorite is history",
    ],
    "practiceQuestions": [
        {
            "q": "Q26で play songs in the gym が不正解な理由は？",
            "a": "演奏は the music room。体育館では give a speech（スピーチ）が行われる。",
        },
        {
            "q": "Q30で Jimmy が不正解な理由は？",
            "a": "Jimmy は来月訪問する予定。昨日訪問したのは one of my friends（おばあちゃんの友達）。",
        },
        {
            "q": "Q32とQ33で eighty years old と forty years old を区別するコツは？",
            "a": "eighty years old＝建物（museum building）。forty years old＝黒板（blackboard）。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "体育館では何が行われる？", "a": "スピーチだよ。えんそうはおんがくしつ！"},
        {"q": "リリーには子猫が何匹？", "a": "3ひきだよ。"},
        {"q": "ジョージがいちばん好きだったのは？", "a": "きょうかしょだよ。いまのすきなかもくはれきし！"},
    ],
}

for fp in (fp1, fp2, fp3, fp4):
    fp_id = fp["id"]
    for ei, ex in enumerate(fp["examples"]):
        ex["audio"] = f"audio/{fp_id}_ex{ei + 1}.mp3"
    fp["sourceQuoteAudio"] = f"audio/{fp_id}_source.mp3"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {"focusPoints": [fp1, fp2, fp3, fp4]}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(data['lessonPlan']['focusPoints'])} focusPoints) to {DATA_PATH}")
