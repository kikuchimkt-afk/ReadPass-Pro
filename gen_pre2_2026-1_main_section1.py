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
            "choiceTranslations": ["神経質に", "非常に・絶対に", "めったに", "別々に"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ nervously＝神経質に。feel nervously（神経質に感じる）のように感情の様子を表す語で、delicious（おいしい）という形容詞を強調する副詞としては使えない",
                "✅ absolutely＝非常に・絶対に。this meal is absolutely delicious（この料理は本当においしい）が自然。the best pasta that I've ever eaten（今までで最高）という最高級の表現とも呼応→正解",
                "❌ rarely＝めったに。頻度を表す副詞（rarely eat out＝めったに外食しない）で、おいしさの程度を表す文脈に合わない",
                "❌ separately＝別々に。eat separately（別々に食べる）のように動作の仕方を表す語。deliciousを修飾できない",
            ],
            "grammar": "💡 absolutely＝非常に（形容詞・副詞を強調する副詞）。It's the best ～ that I've ever ～（今までで最高の～）とセットで出ることが多い褒め言葉のパターン。",
        },
        {
            "number": 2,
            "text": "Dennis was recently ( ) to his company's New York office. He likes his new apartment and is slowly finding out about the city.",
            "translation": "デニスは最近、会社のニューヨーク支店に( )された。新しいアパートが気に入り、ゆっくりと街について知り始めている。",
            "choices": ["transferred", "reduced", "proposed", "apologized"],
            "choiceTranslations": ["異動させられた", "減らされた", "提案された", "謝罪した"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ transferred＝異動させられた。be transferred to ～（～に異動される）が人事の定型。New York office（支店）＋new apartment（新しい住まい）の流れが一致→正解",
                "❌ reduced＝減らされた。be reduced to ～（～に減らされる）やreduce costs（コストを削減する）に使う語。人を支店に「減らす」では意味が通らない",
                "❌ proposed＝提案された。be transferred to his company's New York office（支店への異動）の文脈で、propose a plan（計画を提案する）の用法は当てはまらない",
                "❌ apologized＝謝罪した。apologize to 人 for ～（～について謝る）の形で使う。to his company's office とは結びつかない",
            ],
            "grammar": "💡 be transferred to ～＝～に異動される。recently（最近）＋新しいアパート・街を知る、という転勤後の生活描写が transferred を選ぶ手がかり。",
        },
        {
            "number": 3,
            "text": "Today, Mr. Carter taught his students about the ( ) of smoking. The students learned about the health problems it can cause.",
            "translation": "今日、カーター先生は生徒たちに喫煙の( )について教えた。生徒たちはそれが引き起こす健康上の問題について学んだ。",
            "choices": ["dangers", "palaces", "markets", "galleries"],
            "choiceTranslations": ["危険", "宮殿", "市場", "美術館"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ dangers＝危険（dangerの複数形）。the dangers of smoking（喫煙の危険）＋health problems it can cause（引き起こす健康問題）が完全に一致→正解",
                "❌ palaces＝宮殿。the dangers of smoking（喫煙の危険）という健康の授業で、the palaces of smoking では意味が成立しない",
                "❌ markets＝市場。health problems it can cause（引き起こす健康問題）という文脈で、the markets of smoking は授業のテーマとして合わない",
                "❌ galleries＝美術館・画廊。the galleries of smoking では意味が成立しない。健康問題の授業とは結びつかない",
            ],
            "grammar": "💡 the dangers of ～＝～の危険（ofの後に原因・対象が来る）。第2文のhealth problems（健康問題）が空所の意味を補強する典型パターン。",
        },
        {
            "number": 4,
            "text": "A: Why did you choose that hotel for our vacation?\nB: It had good reviews, and the price seemed ( ) compared to other options.",
            "translation": "A：なぜ休暇にそのホテルを選んだの？\nB：評判がよくて、他の選択肢と比べて値段も( )に思えたから。",
            "choices": ["wooden", "boring", "cute", "reasonable"],
            "choiceTranslations": ["木製の", "退屈な", "かわいい", "妥当な・手頃な"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ wooden＝木製の。a wooden table（木製のテーブル）のように材料を表す形容詞。the price seemed wooden（値段が木製に思えた）では意味不成立",
                "❌ boring＝退屈な。ホテル選びの理由としてgood reviews（良い評判）と並べると、値段が「退屈」では選ぶ動機にならない",
                "❌ cute＝かわいい。値段（price）をcuteで修飾するのは不自然。評判がよく手頃な価格、という流れとは合わない",
                "✅ reasonable＝妥当な・手頃な。good reviews（評判が良い）＋the price seemed reasonable compared to other options（他と比べて手頃）がホテル選びの理由として自然→正解",
            ],
            "grammar": "💡 reasonable＝手頃な・妥当な（reason「理由」＋-able「～できる」→「納得できる」）。compared to other options（他の選択肢と比べて）が価格の妥当さを示す。",
        },
        {
            "number": 5,
            "text": "At the start of the lesson, Mr. Harris made an ( ). He told the class that a student teacher would be teaching his lessons for the next few weeks.",
            "translation": "授業の始めに、ハリス先生は( )をした。今後数週間、学生の先生が自分の授業を担当することをクラスに伝えた。",
            "choices": ["award", "aisle", "attempt", "announcement"],
            "choiceTranslations": ["賞", "通路", "試み", "発表・告知"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ award＝賞。win an award（賞を受賞する）やgive an award（賞を授与する）に使う語。授業冒頭でクラスに伝える内容とは性質が違う",
                "❌ aisle＝通路。walk down the aisle（通路を歩く）のように物理的な通路を指す名詞。make an aisle では意味が通らない",
                "❌ attempt＝試み。make an attempt to do（～しようと試みる）の形で使う。クラスへのお知らせの名詞としては不自然",
                "✅ announcement＝発表・告知。make an announcement（お知らせをする）＋He told the class that ～（クラスに～と伝えた）が呼応→正解",
            ],
            "grammar": "💡 make an announcement＝お知らせをする・発表する。At the start of the lesson（授業の始めに）＋told the class that ～ が「告知」の場面を示す。",
        },
        {
            "number": 6,
            "text": "The mayor has asked several local artists to create ( ) that will be put in the city's parks. The artists have been told that they can use either metal or stone.",
            "translation": "市長は地元の芸術家数人に、市の公園に置かれる( )を制作するよう頼んだ。芸術家たちは金属か石のどちらかを使ってよいと言われている。",
            "choices": ["policies", "blankets", "statues", "insects"],
            "choiceTranslations": ["方針", "毛布", "彫像", "昆虫"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ policies＝方針。government policies（政府の方針）のように抽象的な計画に使う語。artistsが金属や石で「制作する」対象ではない",
                "❌ blankets＝毛布。公園に置く（put in the city's parks）ものとしては不自然。金属や石で作る対象とも合わない",
                "✅ statues＝彫像。artists create statues（芸術家が彫像を作る）＋use either metal or stone（金属か石を使う）＋put in parks（公園に置く）がすべて一致→正解",
                "❌ insects＝昆虫。use either metal or stone（金属か石を使う）・put in the city's parks（公園に置く）の依頼文脈では、statues（彫像）のほうが自然",
            ],
            "grammar": "💡 statue＝彫像。create（制作する）＋metal or stone（材料）＋put in parks（設置場所）の3つの手がかりがそろう典型問題。",
        },
        {
            "number": 7,
            "text": "When Adam buys expensive items, he always keeps the ( ) in a safe place. That way, he can return an item if it has a problem.",
            "translation": "アダムは高価な物を買うとき、いつも( )を安全な場所に保管している。そうすれば、問題があれば商品を返品できる。",
            "choices": ["battery", "receipt", "website", "frame"],
            "choiceTranslations": ["電池", "領収書", "ウェブサイト", "額縁"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ battery＝電池。change the battery（電池を交換する）に使う語。return an item if it has a problem（問題があれば返品する）の根拠にはならない",
                "✅ receipt＝領収書。keep the receipt（領収書を保管する）＋return an item（商品を返品する）が店での返品・交換の定番の流れ→正解",
                "❌ website＝ウェブサイト。keep the website in a safe place（ウェブサイトを安全な場所に保管する）では物理的に意味が通らない",
                "❌ frame＝額縁。a picture frame（額縁）に使う語。高価な物全般の購入記録としては receipt が適切",
            ],
            "grammar": "💡 receipt＝領収書。That way（そうすれば）以降のreturn an item（返品する）が、なぜ領収書を保管するのかを説明する決め手。",
        },
        {
            "number": 8,
            "text": "People can ( ) their friends to support them during difficult times and help them find solutions.",
            "translation": "人は困難な時期に支えてもらい、解決策を見つける手助けをしてもらうために、友人を( )ことができる。",
            "choices": ["paste", "blame", "trust", "scratch"],
            "choiceTranslations": ["貼り付ける", "責める", "信頼する", "かく"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ paste＝貼り付ける。paste a photo on the wall（写真を壁に貼る）のように物理的に貼る語。trust 人 to do（人を信頼して～してもらう）の構文にならない",
                "❌ blame＝責める。blame 人 for ～（～のことで人を責める）の形で使う。support them（支えてもらう）・help them find solutions（助けてもらう）という前向きな文脈と正反対",
                "✅ trust＝信頼する。trust their friends to support them（友人を信頼して支えてもらう）＋help them find solutions（解決策を見つける手助け）が自然→正解",
                "❌ scratch＝かく。scratch one's head（頭をかく）のように使う語。友人を目的語に取る動詞として意味が通らない",
            ],
            "grammar": "💡 trust 人 to do＝人を信頼して～してもらう（to不定詞で期待する行動を示す）。during difficult times（困難な時期に）が信頼の文脈を作る。",
        },
        {
            "number": 9,
            "text": "A: How many points did you ( ) in the math test?\nB: Only 50 out of 100. I did really badly.",
            "translation": "A：数学のテストで何点( )した？\nB：100点満点中50点だけ。本当にひどかったよ。",
            "choices": ["enter", "engage", "claim", "score"],
            "choiceTranslations": ["入る", "従事する", "主張する", "得点を取る"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ enter＝入る。enter the room（部屋に入る）のように場所に入る語。How many points did you enter では「何点入った」となり意味不成立",
                "❌ engage＝従事する。engage in ～（～に従事する）の形で使う。points（得点）を目的語に取れない",
                "❌ claim＝主張する。claim that ～（～だと主張する）の形が基本。テストの点数を「主張する」では文脈に合わない",
                "✅ score＝得点を取る。How many points did you score?（何点取った？）が定型。BのOnly 50 out of 100（100点中50点）が呼応→正解",
            ],
            "grammar": "💡 score＝得点を取る（名詞のscore「得点」と同形の動詞）。How many points ～?への答えがout of 100（100点満点中）の形になることが多い。",
        },
        {
            "number": 10,
            "text": "After running ten kilometers, Evan's legs started to ( ). He sat down to rest and did some leg stretching exercises.",
            "translation": "10キロ走った後、エヴァンの足が( )し始めた。彼は座って休み、足のストレッチ運動をいくつかした。",
            "choices": ["ache", "soothe", "push", "gather"],
            "choiceTranslations": ["痛む", "和らげる", "押す", "集める"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ ache＝痛む。legs started to ache（足が痛み始めた）が自然。10キロ走った後＋sat down to rest（座って休んだ）＋stretching exercises（ストレッチ）が一致→正解",
                "❌ soothe＝和らげる。soothe pain（痛みを和らげる）のように他動詞で使う語。legs started to soothe では「足が和らげ始めた」となり主語と合わない",
                "❌ push＝押す。push the door（ドアを押す）のように物理的に押す語。長距離走の後の足の状態を表せない",
                "❌ gather＝集める。gather information（情報を集める）のように使う語。足が「集め始めた」では意味が通らない",
            ],
            "grammar": "💡 ache＝痛む（名詞ache「痛み」と同形の動詞）。After running ～（走った後）→rest（休む）→stretching（ストレッチ）の因果の流れに注目。",
        },
        {
            "number": 11,
            "text": "Almost all the pets in the shelter found homes, ( ) one dog that was still waiting for a family.",
            "translation": "保護施設のペットはほとんどすべて家を見つけたが、( )まだ家族を待っている1匹の犬がいた。",
            "choices": ["next to", "except for", "across from", "up to"],
            "choiceTranslations": ["〜の隣に", "〜を除いて", "〜の向かいに", "〜まで"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ next to＝〜の隣に。Almost all the pets found homes（ほとんどのペットが家を見つけた）の後に「1匹を除く」例外を示す語としては except for が必要",
                "✅ except for＝〜を除いて。Almost all（ほとんどすべて）＋except for one dog（1匹を除いて）が「例外」を示す定型。still waiting for a family（まだ家族を待っている）と一致→正解",
                "❌ across from＝〜の向かいに。位置関係を表す前置詞句。found homes（家を見つけた）の後に例外を示す用法としては except for が必要",
                "❌ up to＝〜まで。Almost all the pets found homes（ほとんどのペットが家を見つけた）のあとに still waiting for a family（まだ家族を待っている）という例外を示す語としては up to ではない",
            ],
            "grammar": "💡 except for ～＝～を除いて（Almost all / most とセットで「大部分＋例外」を表す）。still waiting（まだ待っている）が「残り1匹」の手がかり。",
        },
        {
            "number": 12,
            "text": "A: ( )! There's a bee near your face!\nB: Oh, I didn't see it. Thanks for letting me know.",
            "translation": "A：( )！顔の近くにハチがいるよ！\nB：ああ、気づかなかった。教えてくれてありがとう。",
            "choices": ["Get on", "Take off", "Give up", "Look out"],
            "choiceTranslations": ["乗る", "脱ぐ・離陸する", "あきらめる", "気をつけて"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ Get on＝乗る。get on the bus（バスに乗る）のように乗り物に使う。危険を知らせる叫びとしては不自然",
                "❌ Take off＝脱ぐ・（飛行機が）離陸する。take off your coat（コートを脱ぐ）に使う語。ハチの危険を伝える場面に合わない",
                "❌ Give up＝あきらめる。give up trying（試すのをあきらめる）のように使う。感嘆符で叫ぶ警告の表現ではない",
                "✅ Look out＝気をつけて。Look out!（気をつけて！）が危険を知らせる定型。There's a bee near your face（顔の近くにハチ）と完全に一致→正解",
            ],
            "grammar": "💡 Look out!＝気をつけて！（危険・注意を促す感嘆表現）。Thanks for letting me know（教えてくれてありがとう）が、相手の警告だったことを示す。",
        },
        {
            "number": 13,
            "text": "A: Dad, can I have a new smartphone for my birthday this year?\nB: No, that's ( ), Megan. Your birthday is next month, and you just got a new one last month.",
            "translation": "A：お父さん、今年の誕生日に新しいスマホをもらえない？\nB：ダメよ、メーガン。それは( )。誕生日は来月だし、先月新しいのをもらったばかりでしょ。",
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
                "あなたの知ることではない",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ out of the question＝ありえない・話にならない。No, that's out of the question（それは無理だ）が断りの定型。just got a new one last month（先月もらったばかり）が理由→正解",
                "❌ up in the air＝未決定の。The plan is still up in the air（計画はまだ未定だ）のように「決まっていない」状態に使う。断りの表現としては不自然",
                "❌ in a good temper＝機嫌がいい。be in a good temper（機嫌がいい）の対義はin a bad temper。要求を断る文脈とは無関係",
                "❌ none of your business＝あなたの知ることではない。can I have a new smartphone for my birthday（誕生日にスマホをもらえる？）への返答として、父娘の会話では使わない",
            ],
            "grammar": "💡 out of the question＝ありえない・話にならない（question「疑問・問題」＝検討の余地がない）。just got ～ last month（先月～したばかり）が断る根拠。",
        },
        {
            "number": 14,
            "text": "A: Have you decided which club to join, Chris?\nB: No. I can't ( ). They all seem so interesting.",
            "translation": "A：どのクラブに入るか決めた、クリス？\nB：ううん。( )できないんだ。どれもとてもおもしろそうなんだ。",
            "choices": [
                "make up my mind",
                "get off my back",
                "go on a voyage",
                "put out the light",
            ],
            "choiceTranslations": [
                "決心する・決める",
                "うるさくするのをやめてほしい",
                "航海に出る",
                "明かりを消す",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ make up my mind＝決心する・決める。Have you decided ～?（決めた？）へのNo. I can't make up my mind（決められない）が呼応。They all seem so interesting（どれもおもしろそう）が理由→正解",
                "❌ get off my back＝しつこいのをやめてほしい。get off my back!（うるさい！）のように相手にしつこさをやめろと言う表現。クラブ選びの文脈に合わない",
                "❌ go on a voyage＝航海に出る。Have you decided which club to join?（どのクラブに入るか決めた？）への I can't go on a voyage では、決められないという答えにならない",
                "❌ put out the light＝明かりを消す。I can't put out the light では「明かりを消せない」となり、which club to join（どのクラブに入るか）と無関係",
            ],
            "grammar": "💡 make up one's mind＝決心する（mind＝心・意思）。decide ～?とcan't make up my mindが問答のペアとして頻出。",
        },
        {
            "number": 15,
            "text": "Before buying a new smartphone, you should ( ) several different ones. That way, you can find one that is right for you.",
            "translation": "新しいスマホを買う前に、いくつかの異なる機種を( )べきだ。そうすれば、自分に合ったものを見つけられる。",
            "choices": [
                "make a start on",
                "take a look at",
                "do a favor for",
                "have a word with",
            ],
            "choiceTranslations": [
                "〜に取りかかる",
                "見てみる",
                "〜のために親切にする",
                "〜と話をする",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ make a start on＝〜に取りかかる。make a start on the project（プロジェクトに取りかかる）のように作業の開始に使う。several different ones（いくつかの機種）を「取りかかる」対象としては不自然",
                "✅ take a look at＝見てみる。Before buying（買う前に）＋take a look at several different ones（いくつか見てみる）＋find one that is right for you（合うものを見つける）の流れが自然→正解",
                "❌ do a favor for＝〜のために親切にする。do a favor for someone（誰かの親切をする）の形で使う。スマホを目的語にできない",
                "❌ have a word with＝〜と話をする。have a word with the teacher（先生と話をする）のように人を目的語に取る。機種を比較する文脈とは合わない",
            ],
            "grammar": "💡 take a look at ～＝～を見てみる（look at「見る」を強調した表現）。Before buying ～（買う前に）→find one that is right for you（合うものを見つける）の順序に注目。",
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
