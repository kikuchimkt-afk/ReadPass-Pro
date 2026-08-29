# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json
Step A: 大問1（vocabulary型）Q1〜15
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "The new restaurant near the train station has a very ( 1 ) menu. It has many dishes from around the world, and they are not very expensive.",
            "translation": "駅の近くの新しいレストランのメニューはとても( 1 )ものです。世界各地の料理が多く、値段もあまり高くありません。",
            "choices": ["tight", "appealing", "boring", "faint"],
            "choiceTranslations": ["きつい", "魅力的な", "退屈な", "かすかな"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ tight＝きつい。menuの魅力を表す形容詞ではない",
                "✅ appealing＝魅力的な。料理が豊富で高くないという説明に合う→正解",
                "❌ boring＝退屈な。料理が豊富というプラスの説明と合わない",
                "❌ faint＝かすかな。音や光の弱さを表す語で、menuには不適切",
            ],
            "grammar": "💡 appealing＝魅力的な。appeal to ～＝～の心を引く。空所の直後の文が空所のヒントになる典型パターン。",
        },
        {
            "number": 2,
            "text": "Blake is very careful about his ( 2 ). He always puts on clean clothes and brushes his hair before he goes out.",
            "translation": "ブレイクは自分の( 2 )にとても気をつけています。出かける前にはいつもきれいな服を着て髪を梳きます。",
            "choices": ["entrance", "appearance", "difference", "intelligence"],
            "choiceTranslations": ["入口", "外見", "違い", "知性"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ entrance＝入口。服装や髪の手入れとは結びつかない",
                "✅ appearance＝外見・身だしなみ。clean clothesとbrushes his hairが根拠→正解",
                "❌ difference＝違い。careful about his differenceでは意味が定まらない",
                "❌ intelligence＝知性。服や髪についての説明と合わない",
            ],
            "grammar": "💡 appearance＝外見・身だしなみ（動詞appear＝現れる の名詞形）。be careful about ～＝～に気をつける。",
        },
        {
            "number": 3,
            "text": "The company president is going to have a ( 3 ) with the managers next week to talk about the new business plan.",
            "translation": "会社の社長は来週、新しい事業計画について話し合うためにマネージャーたちと( 3 )を開く予定です。",
            "choices": ["complaint", "record", "conference", "treatment"],
            "choiceTranslations": ["苦情", "記録", "会議", "治療"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ complaint＝苦情。事業計画を話し合う集まりを表さない",
                "❌ record＝記録。have a record with the managersは不自然",
                "✅ conference＝会議。managersと事業計画を話し合う目的に合う→正解",
                "❌ treatment＝治療。会社の事業計画の場面とは無関係",
            ],
            "grammar": "💡 have a conference with ～＝～と会議を開く。to talk about ～（目的のto不定詞）が空所のヒント。",
        },
        {
            "number": 4,
            "text": "The movie's ( 4 ) had a meeting with all of the actors. She explained some important things about their characters.",
            "translation": "映画の( 4 )が俳優全員と会議をしました。彼女は彼らの役柄について重要なことを説明しました。",
            "choices": ["patient", "nephew", "firefighter", "director"],
            "choiceTranslations": ["患者", "甥", "消防士", "映画監督"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ patient＝患者。映画で俳優に役柄を説明する立場ではない",
                "❌ nephew＝甥。家族関係を表し、映画制作の役職ではない",
                "❌ firefighter＝消防士。俳優に役柄を説明する仕事ではない",
                "✅ director＝映画監督。俳優にtheir charactersを説明する立場→正解",
            ],
            "grammar": "💡 director＝監督（direct＝指揮する＋-or「人」）。character＝（劇中の）役柄・登場人物。",
        },
        {
            "number": 5,
            "text": "Brandon really likes ( 5 ). He even has some beetles in a plastic box in his room. He likes to watch them crawling around and eating the food he gives them.",
            "translation": "ブランドンは( 5 )が本当に好きです。なんと部屋のプラスチックの箱にカブトムシまで飼っています。這い回って自分があげた餌を食べるのを見るのが好きです。",
            "choices": ["deserts", "planets", "insects", "ghosts"],
            "choiceTranslations": ["砂漠", "惑星", "昆虫", "幽霊"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ deserts＝砂漠。箱の中で飼う対象ではない",
                "❌ planets＝惑星。beetlesやcrawling aroundと結びつかない",
                "✅ insects＝昆虫。beetlesが昆虫の具体例になっている→正解",
                "❌ ghosts＝幽霊。餌を食べるbeetlesの説明と合わない",
            ],
            "grammar": "💡 insect＝昆虫。抽象（insects）→具体例（beetles）の流れは語彙問題の頻出パターン。crawl around＝這い回る。",
        },
        {
            "number": 6,
            "text": "In the United States, more people are getting heart disease, so the government has started to ( 6 ) healthier lifestyles. They recommend that people exercise every day.",
            "translation": "アメリカでは心臓病になる人が増えているため、政府はより健康的な生活習慣を( 6 )ようになりました。毎日運動するよう勧めています。",
            "choices": ["mark", "involve", "lift", "promote"],
            "choiceTranslations": ["印をつける", "含む・関与させる", "持ち上げる", "促進する・推進する"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ mark＝印をつける。健康的な生活習慣を広める意味はない",
                "❌ involve＝含む・関与させる。lifestylesを推進する文脈に合わない",
                "❌ lift＝持ち上げる。lifestylesを目的語にする用法ではない",
                "✅ promote＝促進する・推進する。政府が運動を勧める対策に合う→正解",
            ],
            "grammar": "💡 promote＝促進する・推進する。so＝だから（前半が理由、後半が政府の対策）。",
        },
        {
            "number": 7,
            "text": "A : Are you okay, Heather?\nB : Actually, I feel ( 7 ) tired. I think I should go to bed now.",
            "translation": "A：大丈夫、ヘザー？\nB：実は( 7 )疲れているの。もう寝たほうがいいと思う。",
            "choices": ["regularly", "hardly", "awfully", "gently"],
            "choiceTranslations": ["定期的に", "ほとんど～ない", "とても（強調）", "優しく"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ regularly＝定期的に。今の疲れの程度を表さない",
                "❌ hardly＝ほとんど～ない。go to bed nowという判断と反対になる",
                "✅ awfully＝とても。tiredを強め、今すぐ寝たい状況に合う→正解",
                "❌ gently＝優しく。動作の様子を表し、tiredを強めない",
            ],
            "grammar": "💡 awfully＝とても・ものすごく（形容詞を強調する副詞）。Are you okay?への返答＝体調不良の流れを読む。",
        },
        {
            "number": 8,
            "text": "Martha had to read a book for her class. She ( 8 ) if it would be interesting, but she really enjoyed it.",
            "translation": "マーサは授業のために本を読まなければなりませんでした。その本は面白いだろうかと( 8 )が、実際にはとても楽しめました。",
            "choices": ["reminded", "replied", "prepared", "wondered"],
            "choiceTranslations": ["思い出させた", "返事をした", "準備をした", "思った"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ reminded＝思い出させた。remindの後には人などの目的語が必要",
                "❌ replied＝返事した。reply if it would be interestingとは言わない",
                "❌ prepared＝準備した。if節を続けて疑問を表す動詞ではない",
                "✅ wondered＝～かどうかと思った。wonder ifの定型でbutの対比にも合う→正解",
            ],
            "grammar": "💡 wonder if ～＝～だろうかと思う（疑問・不安）。butの前後で気持ちが変わる対比構造に注目。",
        },
        {
            "number": 9,
            "text": "Many people ( 9 ) other people by the way they look. However, it is more important to think about what they are like inside.",
            "translation": "多くの人は見た目で他人を( 9 )。しかし、内面がどうかを考えるほうが大切です。",
            "choices": ["announce", "judge", "practice", "complete"],
            "choiceTranslations": ["発表する", "判断する", "練習する", "完成させる"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ announce＝発表する。人を見た目で発表するとは言わない",
                "✅ judge＝判断する。judge A by Bと外見・内面の対比が決め手→正解",
                "❌ practice＝練習する。other peopleを目的語にする意味ではない",
                "❌ complete＝完成させる。人の外見を評価する意味はない",
            ],
            "grammar": "💡 judge A by B＝BによってAを判断する。However以降の「外見より内面」という対比が最大のヒント。",
        },
        {
            "number": 10,
            "text": "A : Excuse me. Is this chair ( 10 )?\nB : Yes, it is. My friend is sitting there. He just went to the restroom, but he will be back soon.",
            "translation": "A：すみません。この椅子は( 10 )状態ですか？\nB：はい。友達が座っています。トイレに行っただけで、すぐ戻ってきます。",
            "choices": ["spread", "expected", "considered", "occupied"],
            "choiceTranslations": ["広げられた", "期待された", "考慮された", "使用中の"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ spread＝広げられた。椅子の使用状況を表さない",
                "❌ expected＝期待された。空席かどうかを尋ねる表現にならない",
                "❌ considered＝考慮された。単独で椅子の状態を表せない",
                "✅ occupied＝使用中の。My friend is sitting thereが直接の根拠→正解",
            ],
            "grammar": "💡 be occupied＝（席・トイレなどが）使用中である（⇔vacant＝空いている）。restroom＝トイレ（米）。",
        },
        {
            "number": 11,
            "text": "A : Are you going to buy a car, Patrick?\nB : Yes, I am. I hope to buy one ( 11 ), but I need to save more money first.",
            "translation": "A：車を買うの、パトリック？\nB：うん。( 11 )買いたいんだけど、まずもっと貯金しないと。",
            "choices": [
                "for the time being",
                "at the same time",
                "once upon a time",
                "in the near future",
            ],
            "choiceTranslations": [
                "当分の間",
                "同時に",
                "昔々",
                "近い将来に",
            ],
            "answer": 4,
            "choiceAnalysis": [
                "❌ for the time being＝当分の間。一回の購入時期を表す語ではない",
                "❌ at the same time＝同時に。同時に起こる別の出来事がない",
                "❌ once upon a time＝昔々。未来の希望とは時制が合わない",
                "✅ in the near future＝近い将来に。まず貯金が必要という後半に合う→正解",
            ],
            "grammar": "💡 in the near future＝近い将来に。timeを含む熟語の使い分けが問われる定番問題。first＝まず（順序）。",
        },
        {
            "number": 12,
            "text": "A : What do you want to do today, Honey?\nB : Well, I was thinking we could go to a museum and then have dinner. It'll be ( 12 ) date.",
            "translation": "A：今日は何をしたい、ハニー？\nB：博物館に行ってから夕食を食べようと思ってたの。( 12 )デートになるわね。",
            "choices": ["a piece of", "a sort of", "a lot of", "a couple of"],
            "choiceTranslations": [
                "一片の・少しの",
                "一種の",
                "たくさんの",
                "二、三の",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ a piece of＝一片の。単数形dateをこの意味では修飾しない",
                "✅ a sort of＝一種の。博物館と夕食を「ある意味デート」と表せる→正解",
                "❌ a lot of＝たくさんの。後ろの単数形dateと数が合わない",
                "❌ a couple of＝2、3の。後ろには複数形が必要",
            ],
            "grammar": "💡 a sort of ～＝一種の～（＝a kind of）。後ろの名詞が単数形か複数形かが解答の決め手になる文法問題でもある。",
        },
        {
            "number": 13,
            "text": "A : What does your company do, Bill?\nB : Well, we are ( 13 ) the biggest supplier of office equipment in the area, but we also sell computers.",
            "translation": "A：あなたの会社は何をしているの、ビル？\nB：この地域で最大のオフィス用品の供給業者( 13 )、でもコンピューターも売っているの。",
            "choices": ["used to", "paid for", "known as", "divided into"],
            "choiceTranslations": [
                "かつて～した",
                "～の代金を支払った",
                "～として知られている",
                "～に分けられた",
            ],
            "answer": 3,
            "choiceAnalysis": [
                "❌ used to＝かつて～した。直前にareがあるためused to doの形にならない",
                "❌ paid for＝～の代金を支払った。会社の呼び名を説明する表現ではない",
                "✅ known as＝～として知られている。be known as＋名称の定型→正解",
                "❌ divided into＝～に分けられた。供給業者としての評判を表さない",
            ],
            "grammar": "💡 be known as ～＝～として知られている（asの後は肩書き・名称）。be known for ～（～で有名）との区別も頻出。",
        },
        {
            "number": 14,
            "text": "A : I hope my boss doesn't ( 14 ) my report.\nB : I'm sure he won't. It's very well written.",
            "translation": "A：上司が私のレポートについて( 14 )ことがなければいいんだけど。\nB：きっとしないよ。とてもよく書けているもの。",
            "choices": [
                "find fault with",
                "put up with",
                "look forward to",
                "take part in",
            ],
            "choiceTranslations": [
                "あら探しをする・けちをつける",
                "我慢する",
                "楽しみにする",
                "参加する",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ find fault with＝～のあら探しをする。well writtenという返答に合う→正解",
                "❌ put up with＝～を我慢する。reportを我慢するという文脈ではない",
                "❌ look forward to＝～を楽しみにする。してほしくないという希望と合わない",
                "❌ take part in＝～に参加する。reportは参加する活動ではない",
            ],
            "grammar": "💡 find fault with ～＝～のあら探しをする（fault＝欠点）。Bの返答が空所の意味を特定する根拠になる。",
        },
        {
            "number": 15,
            "text": "A : Please ( 15 ) to drinks over there. There are sodas, tea, and water. Just take whatever you want.\nB : Thanks. I'll have a soda.",
            "translation": "A：あちらの飲み物を( 15 )。ソーダ、お茶、水があります。好きなものを取ってください。\nB：ありがとう。ソーダにするよ。",
            "choices": [
                "make sure",
                "help yourself",
                "take care",
                "get acquainted",
            ],
            "choiceTranslations": [
                "確かめる",
                "自由に取ってください",
                "気をつける",
                "知り合う",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ make sure＝確かめる。make sure to drinksとは言わない",
                "✅ help yourself＝自由に取る。help yourself to＋飲食物の定型→正解",
                "❌ take care＝気をつける。to drinksを続ける形ではない",
                "❌ get acquainted＝知り合う。飲み物を自由に取る場面に合わない",
            ],
            "grammar": "💡 help yourself to ～＝～をご自由にどうぞ（おもてなしの定番表現）。直後のtoと正しくつながるかが決め手。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["sections"] = [section1]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
