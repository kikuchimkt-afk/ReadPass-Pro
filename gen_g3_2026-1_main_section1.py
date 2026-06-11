# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級 data.json
大問1（vocabulary型）Q1〜15 — 解説・和訳付き
一次ソース: 2026-1(本会場）/3級.pdf / 3級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの( )に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号のマーク欄をぬりつぶしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A: What do you like to do on weekends, Bob?\nB: I like to (　) at home. I often watch a movie.",
            "choices": ["move", "plan", "relax", "grow"],
            "answer": 3,
            "grammar": "relax＝「のんびりする・くつろぐ」。at home で映画を見る週末の過ごし方。",
            "grammarSimple": "relax は「のんびりする」。おうちでえいがをみてのんびりするよ。",
            "choiceAnalysis": [
                "move＝動く。I like to move at home では「家で動く」となり、映画を見る文脈とずれる。",
                "plan＝計画する。週末のくつろぎ方として不自然。",
                "○ relax＝のんびりする。I like to relax at home が自然。",
                "grow＝育てる・成長する。家でくつろぐ場面に合わない。",
            ],
            "choiceAnalysisSimple": [
                "move は「うごく」。のんびりとはちがうよ。",
                "plan は「けいかくする」。合わないよ。",
                "○ relax がぴったり！おうちでのんびり！",
                "grow は「そだつ」。合わないよ。",
            ],
            "translation": "A: ボブ、週末は何をするのが好き？\nB: 家でのんびりするのが好きだよ。よく映画を見るんだ。",
            "choiceTranslations": ["動く", "計画する", "のんびりする", "育てる・成長する"],
        },
        {
            "number": 2,
            "text": "A: Your shoes are so (　), John.\nB: I know. I have to clean them.",
            "choices": ["clever", "common", "dirty", "foolish"],
            "answer": 3,
            "grammar": "dirty＝「汚い」。I have to clean them（靴を洗わなければ）が決め手。",
            "grammarSimple": "dirty は「よごい」。くつがよごいからあらわなきゃだよ。",
            "choiceAnalysis": [
                "clever＝賢い。靴の状態を表す形容詞として不自然。",
                "common＝一般的な。洗う理由にならない。",
                "○ dirty＝汚い。clean them と対になる。",
                "foolish＝ばかな。靴の見た目とは関係しない。",
            ],
            "choiceAnalysisSimple": [
                "clever は「かしこい」。くつには合わないよ。",
                "common は「ふつうの」。あらう理由にならないよ。",
                "○ dirty がぴったり！よごいからあらう！",
                "foolish は「ばかな」。合わないよ。",
            ],
            "translation": "A: ジョン、君の靴はとても汚いね。\nB: わかってるよ。洗わなきゃ。",
            "choiceTranslations": ["賢い", "一般的な", "汚い", "ばかな"],
        },
        {
            "number": 3,
            "text": "A: What happened to your leg, Bob?\nB: I had an (　). I fell down the stairs this morning.",
            "choices": ["accident", "advice", "adult", "addition"],
            "answer": 1,
            "grammar": "have an accident＝「事故に遭う」。階段から落ちた場面。",
            "grammarSimple": "have an accident は「じこにあう」。けさかいだんからおちちゃったよ。",
            "choiceAnalysis": [
                "○ accident＝事故。fell down the stairs とつながる。",
                "advice＝助言。have an advice では意味が通らない。",
                "adult＝大人。足の怪我の説明にならない。",
                "addition＝追加。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "○ accident がぴったり！じこにあった！",
                "advice は「アドバイス」。合わないよ。",
                "adult は「おとな」。合わないよ。",
                "addition は「ついか」。合わないよ。",
            ],
            "translation": "A: ボブ、足に何があったの？\nB: 事故に遭ったんだ。今朝、階段から落ちたよ。",
            "choiceTranslations": ["事故", "助言", "大人", "追加"],
        },
        {
            "number": 4,
            "text": "A: What is that building?\nB: It's the library. It's a (　) of our city.",
            "choices": ["sand", "symbol", "condition", "bottle"],
            "answer": 2,
            "grammar": "a symbol of our city＝「私たちの街の象徴」。図書館の役割。",
            "grammarSimple": "symbol は「しょうちょう」。としょかんはまちのしょうちょうだよ。",
            "choiceAnalysis": [
                "sand＝砂。a sand of our city では意味が通らない。",
                "○ symbol＝象徴。図書館が街を表す定番表現。",
                "condition＝状態・条件。建物の説明として不自然。",
                "bottle＝瓶。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "sand は「すな」。合わないよ。",
                "○ symbol がぴったり！まちのしょうちょう！",
                "condition は「じょうたい」。合わないよ。",
                "bottle は「びん」。合わないよ。",
            ],
            "translation": "A: あの建物は何？\nB: 図書館だよ。私たちの街の象徴なんだ。",
            "choiceTranslations": ["砂", "象徴", "状態・条件", "瓶"],
        },
        {
            "number": 5,
            "text": "Mr. Jones went to a nice restaurant with his family. He (　) some cake for dessert.",
            "choices": ["arrived", "ordered", "taught", "believed"],
            "answer": 2,
            "grammar": "ordered some cake＝「ケーキを注文した」。レストランでのデザート。",
            "grammarSimple": "ordered は「ちゅうもんした」。レストランでケーキをちゅうもんしたよ。",
            "choiceAnalysis": [
                "arrived＝到着した。ケーキを「到着した」では意味が通らない。",
                "○ ordered＝注文した。for dessert と自然につながる。",
                "taught＝教えた。レストランの文脈に合わない。",
                "believed＝信じた。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "arrived は「とうちゃくした」。合わないよ。",
                "○ ordered がぴったり！ケーキをちゅうもん！",
                "taught は「おしえた」。合わないよ。",
                "believed は「しんじた」。合わないよ。",
            ],
            "translation": "ジョーンズさんは家族と素敵なレストランに行った。デザートにケーキを注文した。",
            "choiceTranslations": ["到着した", "注文した", "教えた", "信じた"],
        },
        {
            "number": 6,
            "text": "The tomato soup that Mike made didn't (　) good. It was too salty.",
            "choices": ["taste", "carry", "find", "serve"],
            "answer": 1,
            "grammar": "didn't taste good＝「味が良くなかった」。too salty（塩辛すぎる）が理由。",
            "grammarSimple": "taste good は「あじがいい」。しおからすぎておいしくなかったよ。",
            "choiceAnalysis": [
                "○ taste＝味がする。taste good が定番表現。",
                "carry＝運ぶ。スープが「運ぶ」では文脈に合わない。",
                "find＝見つける。味の良し悪しとは言えない。",
                "serve＝出す・提供する。味についての述語として不自然。",
            ],
            "choiceAnalysisSimple": [
                "○ taste がぴったり！あじがよくなかった！",
                "carry は「はこぶ」。合わないよ。",
                "find は「みつける」。合わないよ。",
                "serve は「だす」。あじの話じゃないよ。",
            ],
            "translation": "マイクが作ったトマトスープは味が良くなかった。塩辛すぎたんだ。",
            "choiceTranslations": ["味がする", "運ぶ", "見つける", "出す・提供する"],
        },
        {
            "number": 7,
            "text": "A: It is a nice day today. Open the (　), John.\nB: OK, Mom.",
            "choices": ["sentence", "stadium", "florist", "curtain"],
            "answer": 4,
            "grammar": "Open the curtain＝「カーテンを開けて」。晴れた日に光を入れる場面。",
            "grammarSimple": "curtain は「カーテン」。いいおてんきだからカーテンをあけて！",
            "choiceAnalysis": [
                "sentence＝文。Open the sentence では意味が通らない。",
                "stadium＝スタジアム。家の中の指示として不自然。",
                "florist＝花屋。開ける対象として不自然。",
                "○ curtain＝カーテン。nice day なのでカーテンを開ける。",
            ],
            "choiceAnalysisSimple": [
                "sentence は「ぶん」。合わないよ。",
                "stadium は「スタジアム」。合わないよ。",
                "florist は「はなや」。合わないよ。",
                "○ curtain がぴったり！カーテンをあけて！",
            ],
            "translation": "A: 今日はいい天気ね。カーテンを開けて、ジョン。\nB: わかった、ママ。",
            "choiceTranslations": ["文", "スタジアム", "花屋", "カーテン"],
        },
        {
            "number": 8,
            "text": "I want a computer that is small (　) to put in my backpack.",
            "choices": ["again", "more", "never", "enough"],
            "answer": 4,
            "grammar": "small enough to＝「〜するのに十分小さい」。リュックに入るサイズ。",
            "grammarSimple": "enough は「じゅうぶんに」。リュックに入るくらいちいさくてほしいよ。",
            "choiceAnalysis": [
                "again＝再び。small again to では意味が通らない。",
                "more＝もっと。small more to は不自然。",
                "never＝決して〜ない。文脈に合わない。",
                "○ enough＝十分に。small enough to put in が定番。",
            ],
            "choiceAnalysisSimple": [
                "again は「もういちど」。合わないよ。",
                "more は「もっと」。合わないよ。",
                "never は「ぜったいに〜ない」。合わないよ。",
                "○ enough がぴったり！じゅうぶんちいさい！",
            ],
            "translation": "リュックに入るのに十分小さいパソコンが欲しい。",
            "choiceTranslations": ["再び", "もっと", "決して〜ない", "十分に"],
        },
        {
            "number": 9,
            "text": "A: Why did you (　) away your green sweater?\nB: It was really old.",
            "choices": ["fall", "throw", "hope", "shop"],
            "answer": 2,
            "grammar": "throw away＝「捨てる」。really old（とても古い）が理由。",
            "grammarSimple": "throw away は「すてる」。ふるくなったからセーターをすてたよ。",
            "choiceAnalysis": [
                "fall away＝崩れ落ちる。セーターを意図的に処分する場面とずれる。",
                "○ throw＝throw away の形。古い服を捨てる。",
                "hope away→hope away は使わない。",
                "shop away→shop away は使わない。",
            ],
            "choiceAnalysisSimple": [
                "fall は「おちる」。すてるとはちがうよ。",
                "○ throw がぴったり！throw away で「すてる」！",
                "hope は合わないよ。",
                "shop は合わないよ。",
            ],
            "translation": "A: なぜ緑のセーターを捨てたの？\nB: とても古かったから。",
            "choiceTranslations": ["落ちる", "捨てる（throw）", "望む", "買い物をする"],
        },
        {
            "number": 10,
            "text": "On his way home from work, Jack gets (　) the bus before his stop. He likes to walk for 30 minutes after sitting all day.",
            "choices": ["again", "off", "up", "in"],
            "answer": 2,
            "grammar": "get off the bus＝「バスを降りる」。stop の前で降りて歩く。",
            "grammarSimple": "get off は「おりる」。ていしばすよりまえでおりてあるくよ。",
            "choiceAnalysis": [
                "get again→get again the bus は不自然。",
                "○ off＝get off＝降りる。walk for 30 minutes とつながる。",
                "get up the bus→乗る意味には get on を使う。",
                "get in the bus→乗車の表現で、降りる文脈と逆。",
            ],
            "choiceAnalysisSimple": [
                "again は合わないよ。",
                "○ off がぴったり！get off でバスをおりる！",
                "up は「のる」方向だよ。",
                "in も「のる」方向だよ。",
            ],
            "translation": "仕事の帰り道、ジャックは自分の停留所の前でバスを降りる。一日中座っていた後、30分歩くのが好きなんだ。",
            "choiceTranslations": ["再び", "降りる（off）", "起きる・乗る", "中に入る・乗る"],
        },
        {
            "number": 11,
            "text": "A: Dad, can you give me a (　) with my new TV? I need to bring it upstairs.\nB: Just a minute.",
            "choices": ["hand", "face", "leg", "foot"],
            "answer": 1,
            "grammar": "give me a hand＝「手伝って」。重いテレビを上の階に運ぶ場面。",
            "grammarSimple": "give me a hand は「てつだって」。あたらしいTVをうえのかいにもっていきたいよ。",
            "choiceAnalysis": [
                "○ hand＝give me a hand＝手伝って。定番のイディオム。",
                "face＝顔。give me a face では意味が通らない。",
                "leg＝脚。手伝いの慣用句ではない。",
                "foot＝足。文脈に合わない。",
            ],
            "choiceAnalysisSimple": [
                "○ hand がぴったり！give me a hand で「てつだって」！",
                "face は「かお」。合わないよ。",
                "leg は「あし」。合わないよ。",
                "foot は「あし」。合わないよ。",
            ],
            "translation": "A: お父さん、新しいテレビを手伝ってくれる？上の階に運ぶ必要があるんだ。\nB: ちょっと待って。",
            "choiceTranslations": ["手（手伝い）", "顔", "脚", "足"],
        },
        {
            "number": 12,
            "text": "Ethan lives far (　) school, so he has to take the bus.",
            "choices": ["along", "below", "under", "from"],
            "answer": 4,
            "grammar": "far from school＝「学校から遠くに」。バスに乗る理由。",
            "grammarSimple": "far from は「〜からとおく」。がっこうがとおいからバスにのるよ。",
            "choiceAnalysis": [
                "far along school→along は「沿って」。距離の表現にならない。",
                "far below school→below は「下に」。距離とは言えない。",
                "far under school→under は「下に」。文脈に合わない。",
                "○ from＝far from ～＝〜から遠くに。",
            ],
            "choiceAnalysisSimple": [
                "along は「にそって」。合わないよ。",
                "below は「したに」。合わないよ。",
                "under は「したに」。合わないよ。",
                "○ from がぴったり！far from で「とおく」！",
            ],
            "translation": "イーサンは学校から遠くに住んでいるので、バスに乗らなければならない。",
            "choiceTranslations": ["沿って", "より下に", "〜の下に", "〜から"],
        },
        {
            "number": 13,
            "text": "Jack finished (　) his room and then went to his friend's house.",
            "choices": ["clean", "cleaned", "cleaning", "cleans"],
            "answer": 3,
            "grammar": "finished cleaning＝「掃除を終えた」。finish＋動名詞の形。",
            "grammarSimple": "finished cleaning は「そうじをおえた」。finish のあとは ing だよ。",
            "choiceAnalysis": [
                "finished clean→finish の後に原形は取れない。",
                "finished cleaned→過去形は続けられない。",
                "○ cleaning＝動名詞。finished cleaning his room が正しい。",
                "finished cleans→三単現は文法的に誤り。",
            ],
            "choiceAnalysisSimple": [
                "clean はそのままではダメだよ。",
                "cleaned もダメだよ。",
                "○ cleaning がぴったり！finish のあとは ing！",
                "cleans もダメだよ。",
            ],
            "translation": "ジャックは部屋の掃除を終えてから、友達の家に行った。",
            "choiceTranslations": ["掃除する（原形）", "掃除した（過去形）", "掃除すること（動名詞）", "掃除する（三単現）"],
        },
        {
            "number": 14,
            "text": "Ken watched TV until twelve o'clock last night. His mother told him (　) to bed earlier.",
            "choices": ["going", "went", "to go", "goes"],
            "answer": 3,
            "grammar": "told him to go to bed＝「もっと早く寝なさいと言った」。tell＋人＋to不定詞。",
            "grammarSimple": "told him to go は「ねなさいといった」。tell のあとは to + 動詞だよ。",
            "choiceAnalysis": [
                "told him going→tell の後に動名詞だけでは「寝なさい」にならない。",
                "told him went→過去形は続けられない。",
                "○ to go＝tell 人 to do の形。早く寝るよう指示。",
                "told him goes→三単現は文法的に誤り。",
            ],
            "choiceAnalysisSimple": [
                "going はそのままではダメだよ。",
                "went もダメだよ。",
                "○ to go がぴったり！もっとはやくねなさい！",
                "goes もダメだよ。",
            ],
            "translation": "ケンは昨夜12時までテレビを見ていた。母親はもっと早く寝るように言った。",
            "choiceTranslations": ["行っている（動名詞）", "行った（過去形）", "行くために（不定詞）", "行く（三単現）"],
        },
        {
            "number": 15,
            "text": "Ellen is good at (　). Her friends enjoy going to her house and eating her delicious food.",
            "choices": ["cooking", "to cook", "cooked", "cooks"],
            "answer": 1,
            "grammar": "good at cooking＝「料理が得意」。at の後は名詞・動名詞。",
            "grammarSimple": "good at cooking は「りょうりがとくい」。おいしいごはんをつくるよ。",
            "choiceAnalysis": [
                "○ cooking＝動名詞。be good at ～ing が定番。",
                "to cook＝不定詞。good at to cook は文法的に誤り。",
                "cooked＝過去形・過去分詞。good at cooked は不自然。",
                "cooks＝三単現。good at cooks は文法的に誤り。",
            ],
            "choiceAnalysisSimple": [
                "○ cooking がぴったり！good at のあとは ing！",
                "to cook は文法がちがうよ。",
                "cooked も合わないよ。",
                "cooks も合わないよ。",
            ],
            "translation": "エレンは料理が得意だ。友達は彼女の家に行って、おいしい料理を食べるのを楽しんでいる。",
            "choiceTranslations": ["料理（動名詞）", "料理するために（不定詞）", "料理した（過去形）", "料理する（三単現）"],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

def mark_choice_analysis(q):
    marked = []
    for i, t in enumerate(q.get("choiceAnalysis", [])):
        t = t.strip()
        if t.startswith("○"):
            t = t[1:].strip()
        if t.startswith(("✅", "❌")):
            marked.append(t)
        else:
            marked.append(("✅ " if i + 1 == q["answer"] else "❌ ") + t)
    q["choiceAnalysis"] = marked


for q in section1["questions"]:
    mark_choice_analysis(q)

others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
