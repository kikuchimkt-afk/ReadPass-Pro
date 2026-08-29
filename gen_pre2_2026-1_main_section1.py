# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
Step A: 大問1（vocabulary型）Q1〜15 — リッチ解説
一次ソース: 2026-1(本会場）/準2級.pdf / 準2級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A: Michael, this meal is ( ) delicious! It's the best pasta that I've ever eaten.\nB: Really? I'm glad you like it.",
            "translation": "A：マイケル、この料理は( )おいしい！今まで食べた中で最高のパスタだよ。\nB：本当？気に入ってくれてうれしいわ。",
            "choices": ["nervously", "absolutely", "rarely", "separately"],
            "choiceTranslations": ["緊張して・不安そうに", "本当に・まったく", "めったに〜ない", "別々に"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ nervously＝緊張して・不安そうに。act nervously（緊張して行動する）のように動作の様子を表し、deliciousの程度は表さない",
                "✅ absolutely＝本当に・まったく。absolutely delicious（本当においしい）が自然→正解",
                "❌ rarely＝めったに〜ない。rarely eat out（めったに外食しない）のように頻度を表す",
                "❌ separately＝別々に。eat separately（別々に食べる）のように動作の仕方を表す",
            ],
            "grammar": "💡 absolutely delicious＝本当においしい。absolutelyはここではdeliciousを強く修飾する。",
        },
        {
            "number": 2,
            "text": "Dennis was recently ( ) to his company's New York office. He likes his new apartment and is slowly finding out about the city.",
            "translation": "デニスは最近、会社のニューヨークオフィスへ( )。新しいアパートが気に入り、少しずつ街のことも分かってきている。",
            "choices": ["transferred", "reduced", "proposed", "apologized"],
            "choiceTranslations": ["異動になった・転勤した", "減らされた", "提案された", "謝った"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ transferred＝異動になった。be transferred to an office（オフィスへ異動になる）が文脈に合う→正解",
                "❌ reduced＝減らされた。reduce costs（費用を減らす）のように数量を小さくする語で、オフィスへの異動は表さない",
                "❌ proposed＝提案された。propose new plans（新しい計画を提案する）の用法で、人の異動には合わない",
                "❌ apologized＝謝った。apologize to someone（人に謝る）と使い、オフィスへの移動は表さない",
            ],
            "grammar": "💡 be transferred to ～＝～へ異動になる。new apartment（新しい住まい）が転勤後の生活を示す。",
        },
        {
            "number": 3,
            "text": "Today, Mr. Carter taught his students about the ( ) of smoking. The students learned about the health problems it can cause.",
            "translation": "今日、カーター先生は生徒たちに喫煙の( )について教えた。生徒たちはそれが引き起こす健康上の問題について学んだ。",
            "choices": ["dangers", "palaces", "markets", "galleries"],
            "choiceTranslations": ["危険", "宮殿", "市場", "美術館・画廊"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ dangers＝危険。the dangers of smoking（喫煙の危険）がhealth problemsと呼応する→正解",
                "❌ palaces＝宮殿。palaces of smokingでは健康問題の授業内容にならない",
                "❌ markets＝市場。markets of smokingではhealth problemsにつながらない",
                "❌ galleries＝美術館・画廊。art galleries（美術館）は喫煙による健康問題と無関係",
            ],
            "grammar": "💡 the dangers of ～＝～の危険。health problems（健康問題）が意味を決める手がかり。",
        },
        {
            "number": 4,
            "text": "A: Why did you choose that hotel for our vacation?\nB: It had good reviews, and the price seemed ( ) compared to other options.",
            "translation": "A：なぜ休暇にそのホテルを選んだの？\nB：評判がよくて、他の選択肢と比べて値段も( )に思えたから。",
            "choices": ["wooden", "boring", "cute", "reasonable"],
            "choiceTranslations": ["木製の", "退屈な", "かわいい", "妥当な・手頃な"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ wooden＝木製の。a wooden table（木製のテーブル）のように材料を表し、priceには使わない",
                "❌ boring＝退屈な。a boring hotelとは言えるが、the price seemed boringは不自然",
                "❌ cute＝かわいい。a cute roomとは言えるが、the price seemed cuteは価格評価にならない",
                "✅ reasonable＝妥当な・手頃な。a reasonable price（手頃な価格）がcompared to other optionsと合う→正解",
            ],
            "grammar": "💡 a reasonable price＝手頃な価格。compared to ～（～と比べて）が判断の基準を示す。",
        },
        {
            "number": 5,
            "text": "At the start of the lesson, Mr. Harris made an ( ). He told the class that a student teacher would be teaching his lessons for the next few weeks.",
            "translation": "授業の初めに、ハリス先生は( )をした。そして、今後数週間は教育実習生が自分の授業を担当するとクラスに伝えた。",
            "choices": ["award", "aisle", "attempt", "announcement"],
            "choiceTranslations": ["賞", "通路", "試み", "発表・告知"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ award＝賞。win an award（賞を受賞する）と使い、クラスへの知らせではない",
                "❌ aisle＝通路。walk down the aisle（通路を歩く）のように場所を表す",
                "❌ attempt＝試み。make an attempt（試みる）は文法上可能だが、He told the class that ～の内容と合わない",
                "✅ announcement＝発表・告知。make an announcement（発表する）がHe told the class that ～と呼応する→正解",
            ],
            "grammar": "💡 make an announcement＝発表する・知らせる。told the class that ～が発表内容を示す。",
        },
        {
            "number": 6,
            "text": "The mayor has asked several local artists to create ( ) that will be put in the city's parks. The artists have been told that they can use either metal or stone.",
            "translation": "市長は地元の芸術家数人に、市の公園に置かれる( )を制作するよう頼んだ。芸術家たちは金属か石のどちらかを使ってよいと言われている。",
            "choices": ["policies", "blankets", "statues", "insects"],
            "choiceTranslations": ["方針", "毛布", "彫像", "昆虫"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ policies＝方針。create policies（方針を作る）は可能だが、metal or stoneという材料とは合わない",
                "❌ blankets＝毛布。metal blankets（金属製の毛布）は制作物として不自然",
                "✅ statues＝彫像。metal or stone statues（金属や石の彫像）を公園に置く流れが自然→正解",
                "❌ insects＝昆虫。create insects（昆虫を作る）はartistsへの依頼内容として合わない",
            ],
            "grammar": "💡 statue＝彫像。metal or stone（材料）とput in parks（設置場所）が手がかり。",
        },
        {
            "number": 7,
            "text": "When Adam buys expensive items, he always keeps the ( ) in a safe place. That way, he can return an item if it has a problem.",
            "translation": "アダムは高価な物を買うとき、いつも( )を安全な場所に保管している。そうすれば、問題があれば商品を返品できる。",
            "choices": ["battery", "receipt", "website", "frame"],
            "choiceTranslations": ["電池", "レシート・領収書", "ウェブサイト", "額縁"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ battery＝電池。change the battery（電池を交換する）では返品の購入証明にならない",
                "✅ receipt＝レシート・領収書。keep the receipt（レシートを保管する）とreturn an itemがつながる→正解",
                "❌ website＝ウェブサイト。keep a website in a safe placeでは物理的な保管物にならない",
                "❌ frame＝額縁。a picture frame（額縁）は商品の購入記録ではない",
            ],
            "grammar": "💡 keep the receipt＝レシートを保管する。return an item（商品を返品する）が目的を示す。",
        },
        {
            "number": 8,
            "text": "People can ( ) their friends to support them during difficult times and help them find solutions.",
            "translation": "人は、困難なときに支えて解決策を見つけるのを助けてくれる友人を( )ことができる。",
            "choices": ["paste", "blame", "trust", "scratch"],
            "choiceTranslations": ["貼り付ける", "責める", "信頼する", "ひっかく"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ paste＝貼り付ける。paste the photo（写真を貼る）のように物を貼る語",
                "❌ blame＝責める。blame friends for ～（～のことで友人を責める）はsupport themという文脈と合わない",
                "✅ trust＝信頼する。trust their friends to support them（友人が支えてくれると信頼する）が自然→正解",
                "❌ scratch＝ひっかく。scratch someone's arm（人の腕をひっかく）では支えを期待する意味にならない",
            ],
            "grammar": "💡 trust A to do＝Aが～してくれると信頼する。to supportとhelpは友人に期待する行動。",
        },
        {
            "number": 9,
            "text": "A: How many points did you ( ) in the math test?\nB: Only 50 out of 100. I did really badly.",
            "translation": "A：数学のテストでは何点を( )？\nB：100点満点中50点だけ。本当にひどかったよ。",
            "choices": ["enter", "engage", "claim", "score"],
            "choiceTranslations": ["入る・入力する", "従事する", "主張する・請求する", "得点する・点を取る"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ enter＝入る・入力する。enter pointsなら点数の入力を表し、試験で取った点を尋ねる文脈ではない",
                "❌ engage＝従事する。engage in an activity（活動に従事する）と使い、pointsを直接目的語にしない",
                "❌ claim＝主張する・請求する。claim pointsならポイントの請求・獲得を表し、試験の得点には使わない",
                "✅ score＝得点する。score 50 points（50点を取る）がOnly 50 out of 100と呼応する→正解",
            ],
            "grammar": "💡 score points＝点を取る。scoreは「得点」という名詞のほか「得点する」という動詞にもなる。",
        },
        {
            "number": 10,
            "text": "After running ten kilometers, Evan's legs started to ( ). He sat down to rest and did some leg stretching exercises.",
            "translation": "10キロ走った後、エヴァンの脚は( )ようになった。彼は座って休み、脚のストレッチをした。",
            "choices": ["ache", "soothe", "push", "gather"],
            "choiceTranslations": ["痛む", "和らげる", "押す", "集める"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ ache＝痛む。legs started to ache（脚が痛み始めた）が走った後の状態に合う→正解",
                "❌ soothe＝和らげる。soothe sore legs（痛む脚を和らげる）のように目的語を取る",
                "❌ push＝押す。push the door（ドアを押す）のような動作で、脚の状態は表さない",
                "❌ gather＝集める。gather information（情報を集める）のような動作で、脚の状態は表さない",
            ],
            "grammar": "💡 ache＝痛む。start to ache＝痛み始める。restとstretchingが脚の痛みを示す。",
        },
        {
            "number": 11,
            "text": "Almost all the pets in the shelter found homes, ( ) one dog that was still waiting for a family.",
            "translation": "保護施設のペットは、まだ家族を待っている1匹の犬( )、ほとんどすべて引き取り先が見つかった。",
            "choices": ["next to", "except for", "across from", "up to"],
            "choiceTranslations": ["〜の隣に", "〜を除いて", "〜の向かいに", "〜まで"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ next to＝〜の隣に。next to one dogは位置関係を表し、1匹だけ残った例外を示せない",
                "✅ except for＝〜を除いて。except for one dog（1匹を除いて）がAlmost allと対応する→正解",
                "❌ across from＝〜の向かいに。across from one dogは位置関係で、例外の意味にならない",
                "❌ up to＝〜まで。up to one dogではstill waitingという例外を表せない",
            ],
            "grammar": "💡 except for ～＝～を除いて。Almost all（ほとんどすべて）に例外を加える表現。",
        },
        {
            "number": 12,
            "text": "A: ( )! There's a bee near your face!\nB: Oh, I didn't see it. Thanks for letting me know.",
            "translation": "A：( )！顔の近くにハチがいるよ！\nB：ああ、気づかなかった。教えてくれてありがとう。",
            "choices": ["Get on", "Take off", "Give up", "Look out"],
            "choiceTranslations": ["乗る", "脱ぐ・離陸する", "あきらめる", "気をつけて"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ Get on＝乗る。get on a bus（バスに乗る）はハチへの警告にならない",
                "❌ Take off＝脱ぐ・離陸する。take off a coat（コートを脱ぐ）は危険を知らせる表現ではない",
                "❌ Give up＝あきらめる。give up trying（試すのをやめる）は警告にならない",
                "✅ Look out＝気をつけて。Look out for bees（ハチに気をつけて）のように危険を知らせる→正解",
            ],
            "grammar": "💡 Look out!＝気をつけて！ 危険を知らせる定型表現。",
        },
        {
            "number": 13,
            "text": "A: Dad, can I have a new smartphone for my birthday this year?\nB: No, that's ( ), Megan. Your birthday is next month, and you just got a new one last month.",
            "translation": "A：お父さん、今年の誕生日に新しいスマホをもらえない？\nB：いや、それは( )よ、メーガン。誕生日は来月だし、先月新しいものを手に入れたばかりじゃないか。",
            "choices": [
                "out of the question",
                "up in the air",
                "in a good temper",
                "none of your business",
            ],
            "choiceTranslations": [
                "ありえない・不可能",
                "未決定の",
                "機嫌がいい",
                "あなたには関係ない・余計なお世話だ",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ out of the question＝ありえない・話にならない。that's out of the question（それは無理だ）が強い断りになる→正解",
                "❌ up in the air＝未決定の。the plan is up in the air（計画は未定だ）のように決まっていない状態を表す",
                "❌ in a good temper＝機嫌がいい。be in a good temper（機嫌がいい）は要求への返答にならない",
                "❌ none of your business＝あなたには関係ない。none of your businessでは許可を求める質問や後続の理由につながらない",
            ],
            "grammar": "💡 out of the question＝ありえない・話にならない。検討の余地がないという強い断り。",
        },
        {
            "number": 14,
            "text": "A: Have you decided which club to join, Chris?\nB: No. I can't ( ). They all seem so interesting.",
            "translation": "A：どのクラブに入るか決めた、クリス？\nB：いや、まだ( )ことができないんだ。どれもとてもおもしろそうなんだ。",
            "choices": [
                "make up my mind",
                "get off my back",
                "go on a voyage",
                "put out the light",
            ],
            "choiceTranslations": [
                "決心する・決める",
                "私を放っておく・私にしつこくするのをやめる",
                "航海に出る",
                "明かりを消す",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ make up my mind＝決心する・決める。can't make up my mind（決められない）がdecidedと呼応する→正解",
                "❌ get off my back＝私を放っておく。Get off my back!（しつこく干渉しないで！）はクラブ選びの答えにならない",
                "❌ go on a voyage＝航海に出る。go on a voyageはwhich club to joinと無関係",
                "❌ put out the light＝明かりを消す。put out the lightはクラブを決める意味ではない",
            ],
            "grammar": "💡 make up one's mind＝決心する・決める。decideとほぼ同じ意味で使える。",
        },
        {
            "number": 15,
            "text": "Before buying a new smartphone, you should ( ) several different ones. That way, you can find one that is right for you.",
            "translation": "新しいスマホを買う前に、いくつかの機種を( )べきだ。そうすれば、自分に合ったものを見つけられる。",
            "choices": [
                "make a start on",
                "take a look at",
                "do a favor for",
                "have a word with",
            ],
            "choiceTranslations": [
                "〜に取りかかる",
                "見てみる",
                "〜の頼みを聞く・〜に親切なことをする",
                "〜と話をする",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ make a start on＝〜に取りかかる。make a start on a project（計画に着手する）と使い、機種を見る意味ではない",
                "✅ take a look at＝見てみる。take a look at several phones（いくつかの機種を見る）が購入前の行動として自然→正解",
                "❌ do a favor for＝〜の頼みを聞く。do a favor for someone（人のために親切なことをする）はスマホを目的語にしない",
                "❌ have a word with＝〜と話をする。have a word with someone（人と話す）は機種を比較する意味ではない",
            ],
            "grammar": "💡 take a look at ～＝～を見てみる。look at ～とほぼ同じ意味の慣用表現。",
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
