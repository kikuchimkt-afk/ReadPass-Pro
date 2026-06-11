# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級 data.json
lessonPlan（focusPoints × 4）— 大問1〜3の要点をテーマ別にリッチ化
一次ソース: 2026-1(本会場）/3級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "句動詞・コロケーションで空所を決める",
    "subtitle": "Phrasal Verbs, Collocations & Grammar Forms",
    "explanation": (
        "大問1では単語単体ではなく、前後の語とのセットで意味が決まります。"
        "give me a hand（手伝って）、get off the bus（バスを降りる）、throw away（捨てる）は定型句です。"
        "small enough to（〜するのに十分）、finished cleaning（掃除を終えた）、told him to go（行くよう言った）、"
        "good at cooking（料理が得意）のように、enough・finish＋動名詞・tell＋to不定詞・good at＋動名詞も頻出パターンです。"
    ),
    "explanationSimple": (
        "たんごはセットでおぼえるよ。"
        "give me a hand は「てつだって」、get off は「おりる」、throw away は「すてる」。"
        "enough、finish＋ing、tell＋to go、good at cooking もセットだよ。"
    ),
    "sourceQuote": "give me a hand / gets off the bus / throw away / small enough to / finished cleaning / told him to go / good at cooking",
    "sourceLocation": "大問1 (11)(10)(9)(8)(13)(14)(15)",
    "examples": [
        {
            "en": "Dad, can you give me a hand with my new TV? I need to bring it upstairs.",
            "ja": "お父さん、新しいテレビを手伝ってくれる？上の階に運ぶ必要があるんだ。",
            "note": "give me a hand＝「手伝って」。hand単体では「手のひら」だが、ここはイディオム。",
            "noteSimple": "give me a hand は「てつだって」。ぜったいセットでおぼえよう。",
        },
        {
            "en": "Jack gets off the bus before his stop. He likes to walk for 30 minutes.",
            "ja": "ジャックは自分の停留所の前でバスを降りる。30分歩くのが好きなんだ。",
            "note": "get off＝降りる。get on/up/in は「乗る」方向で意味が逆。",
            "noteSimple": "get off は「おりる」。のるときは get on だよ。",
        },
        {
            "en": "Jack finished cleaning his room. Ken's mother told him to go to bed earlier.",
            "ja": "ジャックは部屋の掃除を終えた。ケンの母親はもっと早く寝るように言った。",
            "note": "finish＋動名詞、tell＋人＋to不定詞。原形・過去形は続けられない。",
            "noteSimple": "finish のあとは ing、tell のあとは to + どうし だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "I like to relax at home. I often watch a movie.\n\n"
            "Why did you throw away your green sweater? It was really old.\n\n"
            "Jack gets off the bus before his stop. He likes to walk for 30 minutes.\n\n"
            "Dad, can you give me a hand with my new TV?\n\n"
            "I want a computer that is small enough to put in my backpack.\n\n"
            "Jack finished cleaning his room and then went to his friend's house.\n\n"
            "His mother told him to go to bed earlier.\n\n"
            "Ellen is good at cooking. Her friends enjoy eating her delicious food."
        ),
        "ja": (
            "家でのんびりするのが好き。よく映画を見る。\n\n"
            "なぜ緑のセーターを捨てたの？とても古かったから。\n\n"
            "ジャックは停留所の前でバスを降りる。30分歩くのが好き。\n\n"
            "お父さん、テレビを手伝ってくれる？\n\n"
            "リュックに入るのに十分小さいパソコンが欲しい。\n\n"
            "ジャックは部屋の掃除を終えてから友達の家へ行った。\n\n"
            "母親はもっと早く寝るように言った。\n\n"
            "エレンは料理が得意。友達はおいしい料理を食べるのを楽しんでいる。"
        ),
        "source": "大問1 (1)(9)(10)(11)(8)(13)(14)(15)",
        "audioFile": "audio/practice_pp1.mp3",
    },
    "highlightPatterns": [
        "relax at home",
        "throw away",
        "gets off the bus",
        "give me a hand",
        "small enough to",
        "finished cleaning",
        "told him to go",
        "good at cooking",
    ],
    "practiceQuestions": [
        {
            "q": "Q10で off が正解になる理由を、get とセットで説明してください。",
            "a": "get off the bus＝「バスを降りる」。walk for 30 minutes とつながる。get on/up は「乗る」で文脈と逆。",
        },
        {
            "q": "Q13で cleaning が必要な理由は？",
            "a": "finished の直後は動名詞。finished clean/cleaned/cleans は文法的に誤り。",
        },
        {
            "q": "Q15で cooking が正解で to cook が誤りになる理由は？",
            "a": "good at ～ing が定番。be good at to cook は文法的に成立しない。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "give me a hand ってどういう意味？",
            "a": "「てつだって」。てつだいをお願いするときのセットだよ。",
        },
        {
            "q": "get off ってどういう意味？",
            "a": "「おりる」。バスや電車をおりるときに使うよ。",
        },
        {
            "q": "good at cooking のポイントは？",
            "a": "good at のあとは ing！「りょうりがとくい」だよ。",
        },
    ],
}

fp2 = {
    "id": "fp2",
    "title": "会話の「前後のつながり」で選ぶ",
    "subtitle": "Dialogue Flow: Question → Answer",
    "explanation": (
        "大問2は会話の流れを読む問題です。空所の直前・直後の発言が最大のヒントになります。"
        "パリ旅行の話→ Have you ever been there? と Yes, it's beautiful. がセット。"
        "テニスの提案→ That sounds great. と I was thinking the same thing。"
        "夕食の呼び出し→ I'll be there in a minute。"
        "朝食を食べない→ What's the matter? と I'm just not hungry。"
        "ジャケットの取り違え→ I'm very sorry. と謝罪の流れです。"
    ),
    "explanationSimple": (
        "かいわはまえとうしろをよんでね。"
        "パリ→「行ったことある？」。テニス→「いいね」。"
        "ごはん→「すぐいく」。あさごはん→「どうしたの？」。"
        "じゃけっと→「ごめんなさい」。"
    ),
    "sourceQuote": "Have you ever been there? / That sounds great. / I'll be there in a minute. / What's the matter?",
    "sourceLocation": "大問2 (16)〜(20)",
    "examples": [
        {
            "en": "Boy: I'm planning to go to Paris this summer. Have you ever been there?\nGirl: Yes, it's a very beautiful place.",
            "ja": "男の子：この夏パリに行く予定なんだ。そこへ行ったことある？\n女の子：うん、とても美しい場所だよ。",
            "note": "旅行先の話→経験を聞く Have you ever been there?",
            "noteSimple": "「パリに行く」→「そこに行ったことある？」の流れだよ。",
        },
        {
            "en": "Man: Why don't we play tennis together on Saturday?\nWoman: That sounds great. I was thinking the same thing.",
            "ja": "男：土曜にテニスをしない？\n女：いいですね。私も同じことを考えていたわ。",
            "note": "提案への賛成＋同じ考えだった、という返答。",
            "noteSimple": "「テニスしない？」→「いいね！わたしもそう思ってた！」",
        },
        {
            "en": "Wife: You're not eating your breakfast. What's the matter?\nHusband: I'm just not hungry.",
            "ja": "妻：朝食を食べていないわね。どうしたの？\n夫：ただお腹が空いていないだけなんだ。",
            "note": "What's the matter? → 理由・状態の説明というパターン。",
            "noteSimple": "「どうしたの？」→「おなかがすいてないだけ」だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Boy: I'm planning to go to Paris this summer. Have you ever been there?\n"
            "Girl: Yes, it's a very beautiful place.\n\n"
            "Man: Why don't we play tennis together on Saturday?\n"
            "Woman: That sounds great. I was thinking the same thing.\n\n"
            "Mother: Samantha, dinner is ready. Come downstairs.\n"
            "Daughter: OK, Mom. I'll be there in a minute.\n\n"
            "Wife: You're not eating your breakfast. What's the matter?\n"
            "Husband: I'm just not hungry.\n\n"
            "Man 1: Excuse me. I think you're wearing my jacket.\n"
            "Man 2: Oh, I'm very sorry. It looks like mine."
        ),
        "ja": (
            "男の子：この夏パリに行く予定。行ったことある？\n"
            "女の子：うん、とても美しい場所だよ。\n\n"
            "男：土曜にテニスをしない？\n"
            "女：いいですね。私も同じことを考えていた。\n\n"
            "母：夕食の用意ができたわ。下に来て。\n"
            "娘：わかった。すぐ行くよ。\n\n"
            "妻：朝食を食べていないわね。どうしたの？\n"
            "夫：ただお腹が空いていないだけ。\n\n"
            "男1：すみません、僕のジャケットを着ていると思います。\n"
            "男2：ああ、本当にすみません。僕のと似ていますね。"
        ),
        "source": "大問2 (16)〜(20)",
        "audioFile": "audio/practice_pp2.mp3",
    },
    "highlightPatterns": [
        "Have you ever been there",
        "That sounds great",
        "I'll be there in a minute",
        "What's the matter",
        "I'm very sorry",
    ],
    "practiceQuestions": [
        {
            "q": "Q16で Would you like some? が不適切な理由は？",
            "a": "パリ旅行の話題に対する質問として不自然。相手の経験を聞く Have you ever been there? が次の Yes, it's beautiful. とつながる。",
        },
        {
            "q": "Q18で I'm too busy が合わない理由は？",
            "a": "母は Come downstairs（今すぐ降りてきて）と言っている。忙しすぎるは呼び出しに応じない。I'll be there in a minute が自然。",
        },
        {
            "q": "Q20で it's my pleasure が誤りになる理由は？",
            "a": "相手のジャケットを間違えて着ている場面。謝罪の I'm very sorry が適切。どういたしましては謝罪ではない。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "Have you ever been there ってどういう意味？",
            "a": "「そこに行ったことある？」。たびのはなしで使うよ。",
        },
        {
            "q": "What's the matter ってどういう意味？",
            "a": "「どうしたの？」。げんいんやきぶんをきくときだよ。",
        },
        {
            "q": "会話問題のコツは？",
            "a": "つぎのセリフをよんで、自然なやりとりかな？と考えること！",
        },
    ],
}

fp3 = {
    "id": "fp3",
    "title": "お知らせとメール——「誰が・どこで・何をしたか」を整理する",
    "subtitle": "Notice & Email: Track Who, Where, What",
    "explanation": (
        "大問3Aの掲示では、持参物（apron and a notebook）と講師の実績（won cooking contests）を区別して読みます。"
        "大問3Bの3通のメールでは、誰が・いつ・どこで・何をしたかをメモしながら読むと Q23〜25 が解けます。"
        "Judy がデパートで買ったのは scarf and coat、おばあちゃんが財布を買ったのは shopping mall next to the museum、"
        "料理中に Judy がしていたのは listen to Linda's stories、と主語と動作を混同しないことが重要です。"
    ),
    "explanationSimple": (
        "お知らせはもっていくものと、せんせいのじっせきをわけるよ。"
        "メールはだれが・どこで・なにをしたか、をメモしながらよむといいよ。"
    ),
    "sourceQuote": "Remember to bring an apron and a notebook / won some international cooking contests / bought a coat for myself / shopping mall next to the museum",
    "sourceLocation": "大問3A / 大問3B",
    "examples": [
        {
            "en": "Remember to bring an apron and a notebook.",
            "ja": "エプロンとノートを持参してください。",
            "note": "参加者の持参物。Q21は notebook が正答の根拠。",
            "noteSimple": "エプロンとノートをもっていくよ。",
        },
        {
            "en": "I saw a nice scarf and bought it for you! I also bought a coat for myself.",
            "ja": "いいマフラーを見つけて買ったよ！自分にもコートを買った。",
            "note": "Judy がデパートでしたこと。Q23の根拠。",
            "noteSimple": "ジュディはマフラーとコートをかったよ。",
        },
        {
            "en": "I found it at a shopping mall next to the museum. Linda often told me stories when you were cooking in the kitchen.",
            "ja": "博物館の隣のショッピングモールで見つけた。おばあちゃんが料理しているとき、リンダがよく物語を話してくれた。",
            "note": "財布の購入場所（Q24）と、料理中の行動（Q25）を別々に覚える。",
            "noteSimple": "さいふは博物館のとなりのモール。リンダの物語をきいていたよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Next March, Evansfield Cultural Center will hold cooking classes.\n"
            "Remember to bring an apron and a notebook.\n"
            "Mr. Chen has won some international cooking contests.\n\n"
            "Yesterday, I visited a department store near the station. They were having a winter sale!\n"
            "I saw a nice scarf and bought it for you! I also bought a coat for myself.\n"
            "I found the wallet at a shopping mall next to the museum.\n"
            "Linda often told me stories when you were cooking in the kitchen.\n"
            "I will visit you alone by bus."
        ),
        "ja": (
            "来月3月、文化センターで料理教室を開催します。\n"
            "エプロンとノートを持参してください。\n"
            "チェン先生は国際的な料理コンテストで優勝したことがあります。\n\n"
            "昨日、駅近くのデパートに行った。冬のセールだった！\n"
            "マフラーを買った！自分にもコートを買った。\n"
            "財布は博物館の隣のショッピングモールで見つけた。\n"
            "おばあちゃんが料理しているとき、リンダが物語を話してくれた。\n"
            "バスで一人で訪ねる予定だ。"
        ),
        "source": "大問3A「Mr. Chen's Cooking Classes」/ 大問3B「Winter sale」",
        "audioFile": "audio/practice_pp3.mp3",
    },
    "highlightPatterns": [
        "bring an apron and a notebook",
        "won some international cooking contests",
        "bought a coat for myself",
        "shopping mall next to the museum",
        "told me stories",
        "visit you alone by bus",
    ],
    "practiceQuestions": [
        {
            "q": "Q21で apron だけではなく notebook が答えになる理由は？",
            "a": "選択肢は Bring a notebook。本文は apron and a notebook の両方だが、選択肢に合うのは notebook。",
        },
        {
            "q": "Q24で department store が誤りになる理由は？",
            "a": "デパートは Judy がマフラーを買った場所。財布はおばあちゃんが shopping mall next to the museum で買った。",
        },
        {
            "q": "Q25で helped her grandmother が誤りになる理由は？",
            "a": "本文は Linda often told me stories（物語を聞いた）。台所で手伝ったとは書かれていない。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "教室に何をもっていく？",
            "a": "エプロンとノート！",
        },
        {
            "q": "ジュディはデパートで何をかった？",
            "a": "マフラーとコートだよ。",
        },
        {
            "q": "おばあちゃんが料理しているとき、ジュディは何をしてた？",
            "a": "リンダの物語をきいていたよ。",
        },
    ],
}

fp4 = {
    "id": "fp4",
    "title": "長文読解——人物の生涯と因果で答えを選ぶ",
    "subtitle": "Biography Reading: Cause, Effect & Main Idea",
    "explanation": (
        "大問3C「Never Too Late」は、グランマ・モーゼス（Anna）の生涯が時系列で述べられます。"
        "子どものころ＝drawing pictures on paper、高齢になって手が痛い＝try painting instead、"
        "絵の特徴＝with many colors、生涯の成果＝more than 1,500 works of art、"
        "全体のテーマ＝anyone can try something new at any time と整理すると Q26〜30 が速く解けます。"
        "問題文の主語に注意：hands hurt は Anna、popular artist は彼女全体の評価です。"
    ),
    "explanationSimple": (
        "長文はじかんじゅんにおぼえるよ。"
        "こどものころ＝紙にえをかく、てがいたい＝えをかきはじめる、"
        "え＝たくさんの色、しょうがい＝1500いじょうのさくひん、"
        "まとめ＝いつでも新しいことにちょうせんできる、だよ。"
    ),
    "sourceQuote": "drawing pictures on paper / because her hands hurt / with many colors / more than 1,500 works of art / anyone can try something new",
    "sourceLocation": "大問3C「Never Too Late」",
    "examples": [
        {
            "en": "She often enjoyed drawing pictures on paper her father bought for her.",
            "ja": "父が買ってくれた紙に絵を描くのをよく楽しんだ。",
            "note": "子どものころの好きなこと。Q26の根拠。",
            "noteSimple": "ちいさいときは紙にえをかくのがすきだったよ。",
        },
        {
            "en": "It was hard for her to do some things on the farm because her hands hurt. So, she decided to try painting instead.",
            "ja": "手が痛くて農場の作業が難しくなった。そこで絵を描くことに挑戦することにした。",
            "note": "絵を描き始めた理由＝手の問題。Q27の根拠。",
            "noteSimple": "てがいたくて、えをかくことにしたんだよ。",
        },
        {
            "en": "She created more than 1,500 works of art in her life. Anna and her paintings show that anyone can try something new at any time in their life.",
            "ja": "生涯で1,500点以上の作品を残した。アンナと彼女の絵は、いつでも誰でも新しいことに挑戦できることを示している。",
            "note": "Q29（作品数）と Q30（テーマ）の根拠。",
            "noteSimple": "1500いじょうのさくひんをつくった。いつでもあたらしいことにちょうせんできる、というお話だよ。",
        },
    ],
    "practicePassage": {
        "en": (
            "Anna Mary Robertson Moses, also known as Grandma Moses, was an American artist.\n"
            "She often enjoyed drawing pictures on paper her father bought for her.\n\n"
            "When she got older, it was hard for her to do some things on the farm because her hands hurt. "
            "So, she decided to try painting instead. She was already over seventy-five years old then.\n\n"
            "Her works painted in a simple way with many colors made people feel warm and happy.\n\n"
            "She created more than 1,500 works of art in her life, and her paintings became popular across the country.\n"
            "Anna and her paintings show that anyone can try something new at any time in their life."
        ),
        "ja": (
            "グランマ・モーゼスとして知られるアメリカの画家、アンナ・メアリー・ロバートソン・モーゼス。\n"
            "父が買ってくれた紙に絵を描くのをよく楽しんだ。\n\n"
            "年を取ると手が痛くて農場の作業が難しくなった。そこで絵を描くことにした。当時すでに75歳を超えていた。\n\n"
            "多くの色でシンプルに描かれた作品は、人々を温かく幸せな気持ちにした。\n\n"
            "生涯で1,500点以上の作品を残し、絵は全国で人気になった。\n"
            "いつでも誰でも新しいことに挑戦できることを示している。"
        ),
        "source": "大問3C「Never Too Late」",
        "audioFile": "audio/practice_pp4.mp3",
    },
    "highlightPatterns": [
        "drawing pictures on paper",
        "because her hands hurt",
        "try painting instead",
        "with many colors",
        "more than 1,500 works of art",
        "try something new",
    ],
    "practiceQuestions": [
        {
            "q": "Q27で She did not enjoy living on her farm が誤りになる理由は？",
            "a": "彼女は loved の農場で長く暮らしていた。絵を描き始めた理由は hands hurt（手が痛い）であり、農場が嫌になったわけではない。",
        },
        {
            "q": "Q28で made people free が誤りになる理由は？",
            "a": "本文は with many colors（多くの色）と warm and happy（温かく幸せ）について述べている。自由にしたとは書かれていない。",
        },
        {
            "q": "Q30で How to live on a farm が誤りになる理由は？",
            "a": "農場生活は背景の一部。全体はアメリカの人気画家の生涯と「いつでも新しいことに挑戦できる」というメッセージ。",
        },
    ],
    "practiceQuestionsSimple": [
        {
            "q": "アンナはなぜえをかきはじめた？",
            "a": "てがいたくて、のうさぎがむずかしかったからだよ。",
        },
        {
            "q": "アンナのえの特徴は？",
            "a": "たくさんの色をつかって、かんたんなしかたでかかれていたよ。",
        },
        {
            "q": "この話のメッセージは？",
            "a": "いつでもだれでも、あたらしいことにちょうせんできる、ということだよ。",
        },
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
