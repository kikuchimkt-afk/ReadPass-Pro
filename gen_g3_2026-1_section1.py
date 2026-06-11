# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検3級 data.json
大問1（vocabulary型）Q1〜15 — 解説・和訳付き
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1-sat", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A: What are you going to do next Sunday?\nB: I'm going to the park to fly my (　).",
            "choices": ["field", "kite", "lock", "university"],
            "answer": 2,
            "grammar": "fly my kite＝「たこを揚げる」。公園でたこを揚げに行く場面。",
            "grammarSimple": "fly my kite は「たこをあげる」。公園でたこあげに行くよ。",
            "choiceAnalysis": [
                "field＝野原・畑。fly my field では意味が通らない。",
                "○ kite＝たこ。fly a kite が定番表現。",
                "lock＝鍵。たこを揚げる文脈に合わない。",
                "university＝大学。公園で大学を「揚げる」では不自然。",
            ],
            "choiceAnalysisSimple": [
                "field は「野原」。たこあげには合わないよ。",
                "○ kite がぴったり！たこをあげに行く！",
                "lock は「かぎ」。合わないよ。",
                "university は「だいがく」。合わないよ。",
            ],
            "translation": "A: 来週の日曜日は何をする予定？\nB: 公園に行って、たこを揚げるつもりだよ。",
            "choiceTranslations": ["野原・畑", "たこ", "鍵", "大学"],
        },
        {
            "number": 2,
            "text": "A: Can you (　) me the ball, please?\nB: Here you are.",
            "choices": ["imagine", "remember", "waste", "pass"],
            "answer": 4,
            "grammar": "pass me the ball＝「ボールを私に渡して」。Here you are.＝「はい、どうぞ」。",
            "grammarSimple": "pass me the ball は「ボールをわたして」。Here you are は「はい、どうぞ」。",
            "choiceAnalysis": [
                "imagine＝想像する。ボールを「想像する」では文脈に合わない。",
                "remember＝覚えている。ボールを渡す場面ではない。",
                "waste＝無駄にする。pass の方が自然。",
                "○ pass＝渡す。Can you pass me ～? がよく使われる。",
            ],
            "choiceAnalysisSimple": [
                "imagine は「そうぞうする」。合わないよ。",
                "remember は「おぼえている」。合わないよ。",
                "waste は「むだにする」。合わないよ。",
                "○ pass がぴったり！ボールをわたして！",
            ],
            "translation": "A: ボールを渡してもらえますか？\nB: はい、どうぞ。",
            "choiceTranslations": ["想像する", "覚えている", "無駄にする", "渡す"],
        },
        {
            "number": 3,
            "text": "The movie was very (　). Lucy fell asleep in the theater.",
            "choices": ["boring", "clever", "colorful", "absent"],
            "answer": 1,
            "grammar": "boring＝「退屈な」。fell asleep（眠ってしまった）が決め手。",
            "grammarSimple": "boring は「たいくつな」。映画がつまらなくてねむっちゃった！",
            "choiceAnalysis": [
                "○ boring＝退屈な。眠るほどつまらない映画。",
                "clever＝賢い。映画の性質として不自然。",
                "colorful＝カラフルな。眠る理由にならない。",
                "absent＝欠席の・いない。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "○ boring がぴったり！つまらなくてねむった！",
                "clever は「かしこい」。映画には合わないよ。",
                "colorful は「カラフル」。ねむる理由にならないよ。",
                "absent は「いない」。合わないよ。",
            ],
            "translation": "その映画はとても退屈だった。ルーシーは映画館で眠ってしまった。",
            "choiceTranslations": ["退屈な", "賢い", "カラフルな", "欠席の"],
        },
        {
            "number": 4,
            "text": "Yoko is (　) today. She studied English for five hours yesterday.",
            "choices": ["sad", "bright", "alive", "tired"],
            "answer": 4,
            "grammar": "tired＝「疲れた」。5時間勉強した→今日は疲れている。",
            "grammarSimple": "tired は「つかれた」。きのう5時間べんきょうしたから、きょうはつかれてるよ。",
            "choiceAnalysis": [
                "sad＝悲しい。勉強時間とは直接つながりにくい。",
                "bright＝明るい・輝いている。疲れの文脈に合わない。",
                "alive＝生きている。文脈に合わない。",
                "○ tired＝疲れた。studied for five hours が理由。",
            ],
            "choiceAnalysisSimple": [
                "sad は「かなしい」。つながりが弱いよ。",
                "bright は「あかるい」。つかれとは合わないよ。",
                "alive は「いきている」。合わないよ。",
                "○ tired がぴったり！5時間べんきょうしてつかれた！",
            ],
            "translation": "ヨーコは今日疲れている。彼女は昨日5時間英語を勉強した。",
            "choiceTranslations": ["悲しい", "明るい", "生きている", "疲れた"],
        },
        {
            "number": 5,
            "text": "A: Do you want to be a good swimmer?\nB: Sure. My coach says I need to (　) for three hours every day.",
            "choices": ["exercise", "invite", "wrap", "follow"],
            "answer": 1,
            "grammar": "exercise＝「運動する」。泳ぐためには毎日3時間の練習が必要。",
            "grammarSimple": "exercise は「うんどうする」。およぐためにはまいにち3時間うんどうがひつようだよ。",
            "choiceAnalysis": [
                "○ exercise＝運動する。good swimmer になるための練習。",
                "invite＝招待する。3時間「招待する」では意味が通らない。",
                "wrap＝包む。文脈に合わない。",
                "follow＝ついていく。for three hours every day とは結びつかない。",
            ],
            "choiceAnalysisSimple": [
                "○ exercise がぴったり！まいにち3時間うんどう！",
                "invite は「しょうたいする」。合わないよ。",
                "wrap は「つつむ」。合わないよ。",
                "follow は「ついていく」。合わないよ。",
            ],
            "translation": "A: 上手な泳ぎ手になりたい？\nB: もちろん。コーチは毎日3時間運動する必要があると言っている。",
            "choiceTranslations": ["運動する", "招待する", "包む", "ついていく"],
        },
        {
            "number": 6,
            "text": "Jim saw some people who were buying fresh fish and meat at the (　).",
            "choices": ["promise", "cousin", "novel", "market"],
            "answer": 4,
            "grammar": "market＝「市場」。fresh fish and meat（新鮮な魚と肉）を買う場所。",
            "grammarSimple": "market は「いちば」。さかなやおにくをかうばしょだよ。",
            "choiceAnalysis": [
                "promise＝約束。買い物の場所ではない。",
                "cousin＝いとこ。人を買う場所ではない。",
                "novel＝小説。文脈に合わない。",
                "○ market＝市場。魚や肉を買う定番の場所。",
            ],
            "choiceAnalysisSimple": [
                "promise は「やくそく」。合わないよ。",
                "cousin は「いとこ」。合わないよ。",
                "novel は「しょうせつ」。合わないよ。",
                "○ market がぴったり！いちばでかいもの！",
            ],
            "translation": "ジムは、市場で新鮮な魚や肉を買っている人々を見かけた。",
            "choiceTranslations": ["約束", "いとこ", "小説", "市場"],
        },
        {
            "number": 7,
            "text": "Meg is a student at a large (　). She is studying to be a nurse.",
            "choices": ["mall", "moon", "college", "example"],
            "answer": 3,
            "grammar": "college＝「大学・専門学校」。看護師になるために勉強している学生。",
            "grammarSimple": "college は「だいがく・せんもんがっこう」。かんごしになるためにべんきょうしてるよ。",
            "choiceAnalysis": [
                "mall＝ショッピングモール。看護師の勉強の場としては不自然。",
                "moon＝月。文脈に合わない。",
                "○ college＝大学・専門学校。student at a college が自然。",
                "example＝例。student at an example では意味が通らない。",
            ],
            "choiceAnalysisSimple": [
                "mall は「モール」。がっこうじゃないよ。",
                "moon は「つき」。合わないよ。",
                "○ college がぴったり！がっこうのせいとだよ！",
                "example は「れい」。合わないよ。",
            ],
            "translation": "メグは大きな専門学校の学生だ。彼女は看護師になるために勉強している。",
            "choiceTranslations": ["ショッピングモール", "月", "大学・専門学校", "例"],
        },
        {
            "number": 8,
            "text": "I always (　) care of my little sister when my mother is out. She likes to listen to my stories.",
            "choices": ["make", "give", "pick", "take"],
            "answer": 4,
            "grammar": "take care of＝「〜の世話をする」。弟妹のお世話をする定番表現。",
            "grammarSimple": "take care of は「せわをする」。おかあさんがいないとき、いもうとのせわをするよ。",
            "choiceAnalysis": [
                "make care of→make care of は使わない。",
                "give care of→give care of は使わない。",
                "pick care of→pick care of は使わない。",
                "○ take＝take care of の形。妹の世話をする。",
            ],
            "choiceAnalysisSimple": [
                "make は合わないよ。take care of だよ。",
                "give は合わないよ。",
                "pick は合わないよ。",
                "○ take がぴったり！take care of で「せわをする」！",
            ],
            "translation": "母が外出しているとき、私はいつも妹の世話をしている。彼女は私の話を聞くのが好きだ。",
            "choiceTranslations": ["作る", "与える", "選ぶ", "世話をする（take）"],
        },
        {
            "number": 9,
            "text": "A: Did Roger need help with the math homework?\nB: No, he did it all by (　).",
            "choices": ["him", "he", "his", "himself"],
            "answer": 4,
            "grammar": "by himself＝「彼一人で」。助けは要らなかった。",
            "grammarSimple": "by himself は「ひとりで」。ロジャーはひとりでやったよ。",
            "choiceAnalysis": [
                "him＝彼を。by him では「一人で」の意味にならない。",
                "he＝彼は。by he は文法的に誤り。",
                "his＝彼の。by his では意味が通らない。",
                "○ himself＝by himself＝一人で。",
            ],
            "choiceAnalysisSimple": [
                "him は合わないよ。",
                "he は文法がちがうよ。",
                "his は合わないよ。",
                "○ himself がぴったり！ひとりでやった！",
            ],
            "translation": "A: ロジャーは数学の宿題で助けが必要だった？\nB: いいえ、彼は全部一人でやったよ。",
            "choiceTranslations": ["彼を", "彼は", "彼の", "彼自身（一人で）"],
        },
        {
            "number": 10,
            "text": "A: Oh no! The train has just left. We'll have to wait (　) 30 minutes until the next one comes.\nB: That's OK. Let's get a drink at the store.",
            "choices": ["into", "from", "at", "for"],
            "answer": 4,
            "grammar": "wait for＝「〜を待つ」。wait for 30 minutes＝30分待つ。",
            "grammarSimple": "wait for は「〜をまつ」。つぎの電車まで30ぷんまつつもりだよ。",
            "choiceAnalysis": [
                "into＝〜の中へ。wait into 30 minutes は不自然。",
                "from＝〜から。wait from では「待つ」の意味にならない。",
                "at＝〜で。wait at 30 minutes は不自然。",
                "○ for＝wait for ～＝〜を待つ。",
            ],
            "choiceAnalysisSimple": [
                "into は合わないよ。",
                "from は合わないよ。",
                "at は合わないよ。",
                "○ for がぴったり！wait for で「まつ」！",
            ],
            "translation": "A: ああ、電車が出て行っちゃった！次の電車が来るまで30分待たなきゃ。\nB: 大丈夫。お店で飲み物を買おう。",
            "choiceTranslations": ["〜の中へ", "〜から", "〜で", "〜を待つ（for）"],
        },
        {
            "number": 11,
            "text": "I couldn't sleep on the flight from New York, but I (　) much better this morning. I slept really well last night.",
            "choices": ["cover", "brush", "feel", "share"],
            "answer": 3,
            "grammar": "feel much better＝「ずっと気分が良い」。昨夜よく眠れたから。",
            "grammarSimple": "feel much better は「きぶんがずっといい」。きのうよくねたから、けさはげんきだよ。",
            "choiceAnalysis": [
                "cover＝覆う。feel better の方が自然。",
                "brush＝磨く・ブラシをかける。文脈に合わない。",
                "○ feel＝感じる。feel much better が定番。",
                "share＝分け合う。気分が良いとは言えない。",
            ],
            "choiceAnalysisSimple": [
                "cover は「おおう」。合わないよ。",
                "brush は「みがく」。合わないよ。",
                "○ feel がぴったり！きぶんがいい！",
                "share は「わけあう」。合わないよ。",
            ],
            "translation": "ニューヨークからの便では眠れなかったが、今朝はずっと気分が良い。昨夜はとてもよく眠れた。",
            "choiceTranslations": ["覆う", "磨く", "感じる", "分け合う"],
        },
        {
            "number": 12,
            "text": "Jerry and Betty wanted to buy a new house. They looked (　) downtown, but everything was too small. They found a nice home outside of town.",
            "choices": ["off", "out", "beside", "around"],
            "answer": 4,
            "grammar": "look around＝「あちこちを見て回る」。街の中を探し回った。",
            "grammarSimple": "look around は「あちこちみてまわる」。まちのなかをさがしまわったよ。",
            "choiceAnalysis": [
                "look off→look off は「見る」の意味で使わない。",
                "look out＝気をつける・外を見る。家探しの文脈とずれる。",
                "beside＝〜のそばに。look beside downtown は不自然。",
                "○ around＝look around＝あちこち見て回る。",
            ],
            "choiceAnalysisSimple": [
                "off は合わないよ。",
                "look out は「きをつける」。ちがうよ。",
                "beside は「となり」。合わないよ。",
                "○ around がぴったり！あちこちさがした！",
            ],
            "translation": "ジェリーとベティは新しい家を買いたかった。彼らはダウンタウンをあちこち見て回ったが、どれも小さすぎた。町の外にいい家を見つけた。",
            "choiceTranslations": ["離れる（look off）", "外を見る・気をつける", "〜のそばに", "あちこち（look around）"],
        },
        {
            "number": 13,
            "text": "Some of the art in this airport was (　) by a famous artist.",
            "choices": ["painting", "paints", "painted", "paint"],
            "answer": 3,
            "grammar": "was painted by＝「〜によって描かれた」。受動態の過去分詞。",
            "grammarSimple": "was painted by は「〜によってえがかれた」。ゆうめいながかがかいたアートだよ。",
            "choiceAnalysis": [
                "painting＝現在分詞・名詞。was painting では「描いていた途中」になる。",
                "paints＝三単現・複数形。was paints は文法的に誤り。",
                "○ painted＝過去分詞。was painted by ～ が受動態。",
                "paint＝原形。was paint は文法的に誤り。",
            ],
            "choiceAnalysisSimple": [
                "painting は「かいているところ」。ちがうよ。",
                "paints は文法がちがうよ。",
                "○ painted がぴったり！えがかれた！",
                "paint は文法がちがうよ。",
            ],
            "translation": "この空港にある芸術作品のいくつかは、有名な芸術家によって描かれたものだ。",
            "choiceTranslations": ["描いている（分詞）", "描く（三単現）", "描かれた（過去分詞）", "描く（原形）"],
        },
        {
            "number": 14,
            "text": "Dr. Kobayashi (　) at a university for many years. All the students enjoyed her classes.",
            "choices": ["teaching", "to teach", "taught", "teach"],
            "answer": 3,
            "grammar": "taught＝「教えた」（teachの過去形）。for many years なので過去形。",
            "grammarSimple": "taught は「おしえた」。ながいあいだだいがくでおしえていたよ。",
            "choiceAnalysis": [
                "teaching＝was teaching なら「教えていた」だが、空所だけでは不自然。",
                "to teach＝不定詞。文の述語として主に使えない。",
                "○ taught＝過去形。長年教えていた。",
                "teach＝現在形。for many years とは時制が合わない。",
            ],
            "choiceAnalysisSimple": [
                "teaching はそのままでは合わないよ。",
                "to teach は文の動詞にならないよ。",
                "○ taught がぴったり！ながいあいだおしえた！",
                "teach は「いま」になっちゃうよ。",
            ],
            "translation": "小林先生は長年大学で教えていた。生徒たちはみんな彼女の授業を楽しんでいた。",
            "choiceTranslations": ["教えている（分詞）", "教えるために（不定詞）", "教えた（過去形）", "教える（原形）"],
        },
        {
            "number": 15,
            "text": "A: Are you going out, Paul?\nB: Yes. I'm going to the park (　) basketball.",
            "choices": ["practiced", "to practice", "practice", "practices"],
            "answer": 2,
            "grammar": "to practice basketball＝「バスケットボールの練習をするために」。目的を表す不定詞。",
            "grammarSimple": "to practice は「れんしゅうするために」。こうえんでバスケのれんしゅうに行くよ。",
            "choiceAnalysis": [
                "practiced＝過去形。going to the park practiced では文法的に誤り。",
                "○ to practice＝目的の不定詞。公園に行く目的＝練習。",
                "practice＝原形。going to practice の形なら別だが、ここでは park の後。",
                "practices＝三単現。文法的に合わない。",
            ],
            "choiceAnalysisSimple": [
                "practiced は「れんしゅうした」。合わないよ。",
                "○ to practice がぴったり！れんしゅうするために！",
                "practice はそのままでは合わないよ。",
                "practices は文法がちがうよ。",
            ],
            "translation": "A: ポール、外出するの？\nB: うん。公園にバスケットボールの練習をしに行くところ。",
            "choiceTranslations": ["練習した（過去形）", "練習するために（不定詞）", "練習する（原形）", "練習する（三単現）"],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
