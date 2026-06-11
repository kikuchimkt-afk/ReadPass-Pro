# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検4級 data.json
lessonPlan（focusPoints × 4）— 大問1〜4の要点をテーマ別にリッチ化
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade4", "2026-1-sat", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "単語は「セット」で覚える",
    "subtitle": "Collocations: Verb + Preposition",
    "explanation": (
        "大問1では、単語ひとつより「決まった組み合わせ」が鍵です。"
        "wash your hands（手を洗う）、stay at my friend's place（友達の家に泊まる）、"
        "sick in bed（寝込んでいる）、be kind to your brother（弟に親切に）、"
        "fifteen meters long（15メートルの長さ）は、空所の前後とセットで意味が決まります。"
        "また don't have to（〜する必要はない）、stop playing（〜するのをやめる）、must clean（掃除しなきゃ）、"
        "knew（過去形の知っていた）も、時制・文型と一緒に押さえると得点源になります。"
    ),
    "explanationSimple": (
        "たんごはセットでおぼえよう！wash your hands は「てをあらう」、"
        "stay at は「〜にとまる」、sick in bed は「ねこんでびょうき」。"
        "don't have to は「〜しなくていい」、stop playing は「やめる」、must clean は「そうじしなきゃ」だよ。"
    ),
    "sourceQuote": "Do you wash your hands / we'll stay at my friend's place / She's still sick in bed / Be kind to your brother",
    "sourceLocation": "大問1 (2)(8)(11)(12)",
    "examples": [
        {
            "en": "Do you wash your hands before you eat? Yes, I do. It's important.",
            "ja": "食べる前に手を洗う？うん、するよ。大事だからね。",
            "note": "wash your hands＝「手を洗う」。eat の前の習慣として自然。",
            "noteSimple": "wash your hands は「てをあらう」だよ。",
        },
        {
            "en": "Yes, we'll stay at my friend's place.",
            "ja": "うん、友達の家に泊まるよ。",
            "note": "stay at ～'s place＝「〜の家に泊まる」。at が場所を示す。",
            "noteSimple": "stay at は「〜にとまる」。place は「いえ」の意味だよ。",
        },
        {
            "en": "She's still sick in bed, but she's better.",
            "ja": "まだ寝込んでいるけど、よくなってきた。",
            "note": "sick in bed＝「寝込んでいる・床で休んでいる」。in bed がセット。",
            "noteSimple": "sick in bed は「ねこんでびょうき」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問1]\n"
            "The pool is fifteen meters long. It is also very deep.\n\n"
            "Do you wash your hands before you eat?\n\n"
            "Kyoko always wakes up early in the morning.\n\n"
            "Yes, we'll stay at my friend's place.\n\n"
            "She's still sick in bed, but she's better.\n\n"
            "Be kind to your brother.\n\n"
            "Stop playing the video game and go to bed.\n\n"
            "Yes, but you must clean your bedroom first."
        ),
        "ja": (
            "プールは15メートルの長さ。とても深い。\n\n"
            "食べる前に手を洗う？\n\n"
            "キョーコはいつも朝早く起きる。\n\n"
            "友達の家に泊まるよ。\n\n"
            "まだ寝込んでいるけど、よくなってきた。\n\n"
            "お兄ちゃんに親切にしなさい。\n\n"
            "ゲームをやめて寝なさい。\n\n"
            "でも、先に部屋を掃除しなさい。"
        ),
        "source": "大問1 (3)(2)(9)(8)(11)(12)(14)(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "meters long",
        "wash your hands",
        "wakes up early",
        "stay at",
        "sick in bed",
        "kind to",
        "Stop playing",
        "must clean",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "セット表現",
    "practiceQuestions": [
        {
            "q": "Q8で stay at が正解になるのは、直後の my friend's place からどう読み取れる？",
            "a": "「友達の家に泊まる」＝stay at ～'s place の定型句。stay to/on/as では「泊まる」の意味にならない。",
        },
        {
            "q": "Q14の stop の後ろはなぜ playing（～ing）？",
            "a": "stop ～ing＝「〜するのをやめる」。Stop play / Stop played は文法的に誤り。",
        },
        {
            "q": "Q13で knew が正解なのは、文中のどの語がヒント？",
            "a": "yesterday があるので過去形 knew。「昨日知っていた」＝過去の事実。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "wash your hands ってどういう意味？", "a": "「てをあらう」だよ。"},
        {"q": "stay at my friend's place って？", "a": "「ともだちのいえにとまる」だよ。"},
        {"q": "stop playing って？", "a": "「あそぶのをやめる」だよ。stop のあとは ing！"},
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話は「次のセリフ」で選ぶ",
    "subtitle": "Dialogue Flow & Set Phrases",
    "explanation": (
        "大問2は、空所の直後（ときどき直前）のセリフが最大のヒントです。"
        "She's talking with Aunt Jill. → She's on the phone.（電話中だから伝えられない）"
        "Yes. I'll get my bag. → Do you want to come?（一緒に行く誘いへの返事）"
        "What does it look like? → It's red and white.（見た目の説明）"
        "I looked in every room, but ... → I can't find it.（財布が見つからない）"
        "Wait a minute. や She's on the phone. のような「決まり文句」もセットで覚えましょう。"
    ),
    "explanationSimple": (
        "かいわはつぎのセリフをよんでね！"
        "「ジルおばさんと話してる」→「でんわちゅう」。"
        "「かばんをもってくる」→「いっしょに行く？」。"
        "「どんなかんじ？」→「あかとしろ」。"
    ),
    "sourceQuote": "She's on the phone / Do you want to come / What does it look like / I can't find it",
    "sourceLocation": "大問2 (16)〜(20)",
    "examples": [
        {
            "en": "Father: Please tell Mom.\nSon: She's on the phone. She's talking with Aunt Jill.",
            "ja": "父：お母さんに伝えて。\n息子：電話中だよ。ジルおばさんと話している。",
            "note": "on the phone と talking with が理由のセット。",
            "noteSimple": "「でんわちゅう」だから今は伝えられないよ。",
        },
        {
            "en": "Father: I'm going to the video shop. Do you want to come?\nDaughter: Yes. I'll get my bag.",
            "ja": "父：ビデオ屋に行くんだ。一緒に来る？\n娘：うん。カバンを取ってくる。",
            "note": "Do you want to come? → Yes が自然な返事。",
            "noteSimple": "「いっしょに行く？」→「うん！」だよ。",
        },
        {
            "en": "Girl 2: What does it look like?\nGirl 1: It's red and white.",
            "ja": "女の子2：どんな見た目？\n女の子1：赤と白だよ。",
            "note": "look like への答えは色や形の説明。",
            "noteSimple": "「どんなかんじ？」→「あかとしろ」！",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問2]\n"
            "Father: Eric, it's dinnertime. Please tell Mom.\n"
            "Son: She's on the phone. She's talking with Aunt Jill.\n\n"
            "Father: I'm going to the video shop. Do you want to come?\n"
            "Daughter: Yes. I'll get my bag.\n\n"
            "Daughter: Can you take me to the supermarket today, Dad?\n"
            "Father: Sorry, Lisa. I'm going to work now.\n\n"
            "Girl 1: I'm looking for my umbrella.\n"
            "Girl 2: What does it look like?\n"
            "Girl 1: It's red and white.\n\n"
            "Father: I'm looking for my wallet. I looked in every room, but I can't find it.\n"
            "Daughter: I'll help you."
        ),
        "ja": (
            "父：夕食の時間だよ。お母さんに伝えて。\n"
            "息子：電話中だよ。ジルおばさんと話している。\n\n"
            "父：ビデオ屋に行くんだ。一緒に来る？\n"
            "娘：うん。カバンを取ってくる。\n\n"
            "娘：スーパーに連れて行って。\n"
            "父：ごめん。今から仕事に行くところなんだ。\n\n"
            "女の子1：傘を探しているの。\n"
            "女の子2：どんな見た目？\n"
            "女の子1：赤と白だよ。\n\n"
            "父：財布を探している。全部屋探したけど見つからない。\n"
            "娘：手伝うね。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "She's on the phone",
        "Do you want to come",
        "I'm going to work",
        "What does it look like",
        "red and white",
        "I can't find it",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "会話のつながり",
    "practiceQuestions": [
        {
            "q": "Q16で I'll go to the store が合わない理由は？",
            "a": "父は「お母さんに伝えて」と依頼。次のセリフは母が電話中だという理由（She's on the phone）が必要。",
        },
        {
            "q": "Q18で It's too small が合わない理由は？",
            "a": "娘はスーパーに連れて行ってほしい。父は断る理由として「仕事に行く」と言う流れ。サイズの話ではない。",
        },
        {
            "q": "Q20で it wasn't mine が合わない理由は？",
            "a": "父は自分の財布を探している。見つからない＝I can't find it が自然。所有の否定ではない。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "She's on the phone って？", "a": "「でんわちゅう」だよ。"},
        {"q": "What does it look like? って？", "a": "「どんなかんじ？」と見た目をきくよ。"},
        {"q": "会話問題のコツは？", "a": "つぎのセリフをよんで、なぜそう言うか考えること！"},
    ],
}

fp3 = {
    "id": "fp3",
    "title": "並べ替え——5つの「型」を知る",
    "subtitle": "Sentence Order Patterns",
    "explanation": (
        "大問3は、日本文の意味から英文の「型」を思い出す問題です。"
        "① don't have to ～（〜する必要はない）"
        "② How about ～ for dinner?（〜はどう？）"
        "③ not ... at all（まったく〜ない）"
        "④ not so easy（それほど簡単ではない）"
        "⑤ why did you ...?（なぜ〜した？）"
        "並べ終えたら、2番目と4番目の語が選択肢と一致するか確認するのが最終チェックです。"
    ),
    "explanationSimple": (
        "ならべかえは「かた」をおぼえよう！"
        "don't have to＝しなくていい、How about＝どう？、"
        "not ... at all＝ぜんぜん〜ない、not so easy＝それほどかんたんじゃない、"
        "why did you＝なぜ〜した？だよ。"
    ),
    "sourceQuote": "I don't have to wear my uniform / How about spaghetti for dinner / was not interesting at all / was not so easy / why did you choose",
    "sourceLocation": "大問3 (21)〜(25)",
    "examples": [
        {
            "en": "I don't have to wear my uniform today.",
            "ja": "今日は制服を着る必要はない。",
            "note": "don't have to ＋ wear。have to の否定。",
            "noteSimple": "don't have to は「〜しなくていい」だよ。",
        },
        {
            "en": "How about spaghetti for dinner?",
            "ja": "夕食にスパゲッティはどう？",
            "note": "How about ～? で提案。for dinner が後ろに来る。",
            "noteSimple": "How about は「〜はどう？」だよ。",
        },
        {
            "en": "That TV program was not interesting at all.",
            "ja": "あのテレビ番組はまったく面白くなかった。",
            "note": "not ... at all＝「まったく〜ない」。",
            "noteSimple": "not ... at all は「ぜんぜん〜ない」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: 大問3]\n"
            "I don't have to wear my uniform today.\n\n"
            "How about spaghetti for dinner?\n\n"
            "That TV program was not interesting at all.\n\n"
            "The math test was not so easy for me.\n\n"
            "Paul, why did you choose this school?"
        ),
        "ja": (
            "今日は制服を着る必要はない。\n\n"
            "夕食にスパゲッティはどう？\n\n"
            "あのテレビ番組はまったく面白くなかった。\n\n"
            "数学のテストは私にはそれほど簡単ではなかった。\n\n"
            "ポール、なぜこの学校を選んだの？"
        ),
        "source": "大問3 (21)〜(25)",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "don't have to",
        "How about",
        "not interesting at all",
        "not so easy",
        "why did you",
    ],
    "highlightColor": "#a78bfa",
    "highlightLabel": "並べ替えの型",
    "practiceQuestions": [
        {
            "q": "Q21で ①−③ が正解になる完成文は？2・4番目の語は？",
            "a": "I don't have to wear my uniform today. 2番目 have（①）、4番目 wear（③）。",
        },
        {
            "q": "Q23で not interesting at all の at all は何を強調する？",
            "a": "「まったく〜ない」という意味を強める。not interesting alone より強い否定。",
        },
        {
            "q": "Q25の語順で、文頭の Paul, のあとに来るのはなぜ why ？",
            "a": "Paul, why did you choose ...? と呼びかけ＋疑問文。why が文の疑問の核。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "don't have to って？", "a": "「〜しなくていい」だよ。"},
        {"q": "How about spaghetti for dinner? って？", "a": "「ゆうしょくにスパゲッティはどう？」だよ。"},
        {"q": "並べ替えのさいごのチェックは？", "a": "2ばんめと4ばんめが選択肢とあうかな？"},
    ],
}

fp4 = {
    "id": "fp4",
    "title": "読解——お知らせ・メール・物語の読み分け",
    "subtitle": "Notice, E-mail & Story Reading",
    "explanation": (
        "大問4は3タイプの読み方があります。"
        "【お知らせ】if it rains → 代替の行き先、時刻は集合と帰校を混同しない（Q26-27）。"
        "【メール】月曜＝meeting、水曜＝Davidと練習、金曜＝uniform。同じ曜日の情報を取り違えない（Q28-30）。"
        "【物語】登場人物の行動を時系列で整理。made fun stories（昔）→ write a story（プレゼント）→ notebook（実際に渡したもの）（Q31-35）。"
        "数字（four history books）と「ベッドの周りにあったもの」と「プレゼント」を区別するのがQ34-35のコツです。"
    ),
    "explanationSimple": (
        "よみものは3タイプ！"
        "お知らせ＝あめのときどこ？なんじにもどる？"
        "メール＝げつよう・すいよう・きんようのよていをまちがえない！"
        "ものがたり＝だれがなにをしたか、すうじとプレゼントにちゅうい！"
    ),
    "sourceQuote": "We will go to the Rainbow Museum instead if it rains / meet our new coach at the meeting / You should write a story for her / four history books / gave her grandmother a notebook",
    "sourceLocation": "大問4A・4B・4C",
    "examples": [
        {
            "en": "We will go to the Rainbow Museum instead if it rains.",
            "ja": "雨の場合はレインボー博物館に行きます。",
            "note": "if it rains＝条件。instead＝代わりに。Q26の根拠。",
            "noteSimple": "「あめのときははくぶつかん」だよ。",
        },
        {
            "en": "We can meet our new coach at the meeting!",
            "ja": "ミーティングで新しいコーチに会える！",
            "note": "uniform は金曜の練習後。meeting でできることは coach に会うこと。",
            "noteSimple": "「ミーティングでコーチにあえる」！ユニフォームはきんようだよ。",
        },
        {
            "en": "You should write a story for her. Kate gave her grandmother a notebook.",
            "ja": "物語を書きなさい。ケイトはおばあちゃんにノートを渡した。",
            "note": "父の提案＝write a story。実際に渡した＝notebook。history books は周りにあっただけ。",
            "noteSimple": "「ものがたりをかく」→「ノートをわたした」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Field Trip]\n"
            "Third-grade students will go to the Rainbow Zoo on a school trip by bus.\n"
            "We will go to the Rainbow Museum instead if it rains.\n"
            "We will come back to the school at 3:30 p.m.\n\n"
            "[出典: About next week — Ted & Leo]\n"
            "We will have a meeting in room 203 next Monday, and we can meet our new coach at the meeting!\n"
            "I had a headache yesterday afternoon. So, I could not go to practice.\n"
            "Can I go to practice with him next Wednesday?\n\n"
            "[出典: Kate's Story]\n"
            "Her grandmother always made fun stories for Kate.\n"
            "You should write a story for her.\n"
            "They saw three novels, four history books, and two magazines around her grandmother's bed.\n"
            "Kate gave her grandmother a notebook."
        ),
        "ja": (
            "【遠足】3年生はレインボー動物園へ。雨なら博物館。午後3時30分に帰校。\n\n"
            "【メール】月曜ミーティングでコーチに会える。昨日午後は頭痛で練習休み。水曜にデイビッドと練習したい。\n\n"
            "【物語】おばあちゃんは物語を作ってくれた。父は物語を書けと言った。ベッドの周りに本があった。ノートをプレゼントした。"
        ),
        "source": "大問4A「Field Trip」/ 4B「About next week」/ 4C「Kate's Story」",
        "audioFile": "audio/practice_pp4.mp3",
    },
    "highlightPatterns": [
        "if it rains",
        "Rainbow Museum",
        "3:30 p.m.",
        "meet our new coach",
        "next Wednesday",
        "write a story",
        "four history books",
        "gave her grandmother a notebook",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "読解キーワード",
    "practiceQuestions": [
        {
            "q": "Q28で Get their new uniform が不正解な理由は？",
            "a": "ユニフォームは after practice next Friday（金曜の練習後）。meeting でできるのは meet our new coach。",
        },
        {
            "q": "Q34とQ35を区別するコツは？",
            "a": "Q34はベッド周りに「あった」本の数（four history books）。Q35はケイトが「渡した」もの（notebook）。",
        },
        {
            "q": "Q33で cookies / flowers が不正解な理由は？",
            "a": "それらはケイトの提案。父は No と言い、write a story for her を勧めている。",
        },
    ],
    "practiceQuestionsSimple": [
        {"q": "あめのときどこに行く？", "a": "レインボー博物館だよ。"},
        {"q": "ミーティングでなにができる？", "a": "あたらしいコーチにあえるよ。"},
        {"q": "ケイトはおばあちゃんに何をあげた？", "a": "ノートだよ。れきしのほんはあげてないよ。"},
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

new_fps = [fp1, fp2, fp3, fp4]
old_fps = {fp.get("id"): fp for fp in data.get("lessonPlan", {}).get("focusPoints", [])}
for fp in new_fps:
    old = old_fps.get(fp["id"], {})
    if old.get("sourceQuoteAudio"):
        fp["sourceQuoteAudio"] = old["sourceQuoteAudio"]
    pp = fp.get("practicePassage", {})
    if old.get("practicePassage", {}).get("audioFile"):
        pp["audioFile"] = old["practicePassage"]["audioFile"]
    for i, ex in enumerate(fp.get("examples", [])):
        oex = old.get("examples", [])
        if i < len(oex) and oex[i].get("audio"):
            ex["audio"] = oex[i]["audio"]

data["lessonPlan"] = {
    "title": "英検4級 2026年度 第1回（土曜準会場）",
    "focusPoints": new_fps,
}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(data['lessonPlan']['focusPoints'])} focusPoints) to {DATA_PATH}")
