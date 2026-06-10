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
            "translation": "駅の近くの新しいレストランにはとても( 1 )メニューがあります。世界中の料理がたくさんあり、それほど高くもありません。",
            "choices": ["tight", "appealing", "boring", "faint"],
            "choiceTranslations": ["きつい", "魅力的な", "退屈な", "かすかな"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ tight＝きつい・ぴったりの。メニューの魅力を表さない",
                "✅ appealing＝魅力的な。世界各国の料理が安くて魅力的→正解",
                "❌ boring＝退屈な。たくさんの料理がある描写と矛盾",
                "❌ faint＝かすかな。メニューの形容に不適切",
            ],
            "grammar": "💡 appealing＝魅力的な。appeal to ～＝～の心を引く。menu＝メニュー（可算名詞）。",
        },
        {
            "number": 2,
            "text": "Blake is very careful about his ( 2 ). He always puts on clean clothes and brushes his hair before he goes out.",
            "translation": "ブレイクは自分の( 2 )にとても気をつけています。出かける前にはいつもきれいな服を着て髪を梳きます。",
            "choices": ["entrance", "appearance", "difference", "intelligence"],
            "choiceTranslations": ["入口", "外見", "違い", "知性"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ entrance＝入口。身だしなみの文脈に合わない",
                "✅ appearance＝外見・身だしなみ。服や髪の手入れ→正解",
                "❌ difference＝違い。身だしなみの文脈に合わない",
                "❌ intelligence＝知性。服や髪の描写と無関係",
            ],
            "grammar": "💡 appearance＝外見・身だしなみ。be careful about ～＝～に気をつける。",
        },
        {
            "number": 3,
            "text": "The company president is going to have a ( 3 ) with the managers next week to talk about the new business plan.",
            "translation": "会社の社長は来週、新しい事業計画について話し合うためにマネージャーたちと( 3 )を開く予定です。",
            "choices": ["complaint", "record", "conference", "treatment"],
            "choiceTranslations": ["苦情", "記録", "会議", "治療"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ complaint＝苦情。計画を話し合う場ではない",
                "❌ record＝記録。have a recordは不自然",
                "✅ conference＝会議。社長とマネージャーが計画を話し合う→正解",
                "❌ treatment＝治療。ビジネスの文脈に合わない",
            ],
            "grammar": "💡 have a conference＝会議を開く。talk about ～＝～について話し合う。",
        },
        {
            "number": 4,
            "text": "The movie's ( 4 ) had a meeting with all of the actors. She explained some important things about their characters.",
            "translation": "映画の( 4 )が俳優全員と会議をしました。彼女は彼らの役柄について重要なことを説明しました。",
            "choices": ["patient", "nephew", "firefighter", "director"],
            "choiceTranslations": ["患者", "甥", "消防士", "監督"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ patient＝患者。映画制作の文脈に合わない",
                "❌ nephew＝甥。俳優への説明役として不自然",
                "❌ firefighter＝消防士。映画の文脈に合わない",
                "✅ director＝監督。俳優にキャラクターを説明→正解。💡 Sheが監督を指す",
            ],
            "grammar": "💡 director＝監督。character＝（劇中の）登場人物・キャラクター。",
        },
        {
            "number": 5,
            "text": "Brandon really likes ( 5 ). He even has some beetles in a plastic box in his room. He likes to watch them crawling around and eating the food he gives them.",
            "translation": "ブランドンは( 5 )が本当に好きです。なんと部屋のプラスチックの箱にカブトムシまで飼っています。這い回って自分があげた餌を食べるのを見るのが好きです。",
            "choices": ["deserts", "planets", "insects", "ghosts"],
            "choiceTranslations": ["砂漠", "惑星", "昆虫", "幽霊"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ deserts＝砂漠。beetles（甲虫）の説明と矛盾",
                "❌ planets＝惑星。虫を飼う文脈に合わない",
                "✅ insects＝昆虫。beetles（甲虫類）を含む→正解",
                "❌ ghosts＝幽霊。実際に餌を与えている描写と矛盾",
            ],
            "grammar": "💡 insect＝昆虫。beetle＝甲虫。crawl around＝這い回る。",
        },
        {
            "number": 6,
            "text": "In the United States, more people are getting heart disease, so the government has started to ( 6 ) healthier lifestyles. They recommend that people exercise every day.",
            "translation": "アメリカでは心臓病になる人が増えているため、政府はより健康的な生活習慣を( 6 )し始めました。毎日運動するよう勧めています。",
            "choices": ["mark", "involve", "lift", "promote"],
            "choiceTranslations": ["印をつける", "関与させる", "持ち上げる", "促進する"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ mark＝印をつける。生活習慣を促進する文脈に合わない",
                "❌ involve＝関与させる。生活習慣の推進には不自然",
                "❌ lift＝持ち上げる。文脈に合わない",
                "✅ promote＝促進する。運動を勧める政策→正解",
            ],
            "grammar": "💡 promote＝促進する。recommend that ～＝～するよう勧める。",
        },
        {
            "number": 7,
            "text": "A : Are you okay, Heather?\nB : Actually, I feel ( 7 ) tired. I think I should go to bed now.",
            "translation": "A：大丈夫、ヘザー？\nB：実は( 7 )疲れているの。もう寝たほうがいいと思う。",
            "choices": ["regularly", "hardly", "awfully", "gently"],
            "choiceTranslations": ["定期的に", "ほとんど～ない", "とても（強調）", "優しく"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ regularly＝定期的に。feel regularly tiredは不自然",
                "❌ hardly＝ほとんど～ない。寝るほど疲れていると矛盾",
                "✅ awfully＝とても（強調）。寝るべきほど疲れている→正解",
                "❌ gently＝優しく。feel gently tiredは不自然",
            ],
            "grammar": "💡 awfully＝とても（副詞の強調）。actually＝実は。should go to bed＝寝るべき。",
        },
        {
            "number": 8,
            "text": "Martha had to read a book for her class. She ( 8 ) if it would be interesting, but she really enjoyed it.",
            "translation": "マーサは授業のために本を読まなければなりませんでした。面白いかどうか( 8 )のですが、とても楽しめました。",
            "choices": ["reminded", "replied", "prepared", "wondered"],
            "choiceTranslations": ["思い出した", "返事した", "準備した", "～かどうか思った"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ reminded＝思い出した。if節との結びつきが不自然",
                "❌ replied＝返事した。本が面白いかは返事の対象ではない",
                "❌ prepared＝準備した。if it would be interestingと結びつかない",
                "✅ wondered＝～かどうか思った。面白いか不安だったが楽しめた→正解",
            ],
            "grammar": "💡 wonder if ～＝～かどうか思う・疑う。but＝しかし（予想と異なる結果）。",
        },
        {
            "number": 9,
            "text": "Many people ( 9 ) other people by the way they look. However, it is more important to think about what they are like inside.",
            "translation": "多くの人は見た目で他人を( 9 )。しかし、内面がどうかを考えるほうが大切です。",
            "choices": ["announce", "judge", "practice", "complete"],
            "choiceTranslations": ["発表する", "判断する", "練習する", "完成させる"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ announce＝発表する。見た目で発表するは不自然",
                "✅ judge＝判断する。見た目で人を判断する→正解。💡 insideと対比",
                "❌ practice＝練習する。人を練習するは不自然",
                "❌ complete＝完成させる。文脈に合わない",
            ],
            "grammar": "💡 judge A by B＝BによってAを判断する。what they are like inside＝内面がどうか。",
        },
        {
            "number": 10,
            "text": "A : Excuse me. Is this chair ( 10 )?\nB : Yes, it is. My friend is sitting there. He just went to the restroom, but he will be back soon.",
            "translation": "A：すみません。この椅子は( 10 )ですか？\nB：はい。友達が座っています。トイレに行っただけで、すぐ戻ってきます。",
            "choices": ["spread", "expected", "considered", "occupied"],
            "choiceTranslations": ["広がった", "期待された", "考慮された", "使われている"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ spread＝広がった。椅子の状態として不自然",
                "❌ expected＝期待された。席の空き状況の問いに合わない",
                "❌ considered＝考慮された。Is this chair considered?は不自然",
                "✅ occupied＝使われている・占有された。友達が座っている→正解",
            ],
            "grammar": "💡 be occupied＝（席などが）使われている・空いていない。restroom＝トイレ（米）。",
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
                "❌ for the time being＝当分の間。買う時期の希望を表さない",
                "❌ at the same time＝同時に。車を買う時期の表現として不自然",
                "❌ once upon a time＝昔々。物語の冒頭の表現で不適切",
                "✅ in the near future＝近い将来に。貯金してから買いたい→正解",
            ],
            "grammar": "💡 in the near future＝近い将来に。hope to ～＝～することを望む。save money＝貯金する。",
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
                "❌ a piece of＝一片の。a piece of dateは不自然",
                "✅ a sort of＝一種の。博物館＋夕食という一種のデート→正解",
                "❌ a lot of＝たくさんの。a lot of dateは文法的に不自然",
                "❌ a couple of＝二、三の。デート1回の文脈に合わない",
            ],
            "grammar": "💡 a sort of ～＝一種の～、ある意味～。date＝デート（可算名詞）。",
        },
        {
            "number": 13,
            "text": "A : What does your company do, Bill?\nB : Well, we are ( 13 ) the biggest supplier of office equipment in the area, but we also sell computers.",
            "translation": "A：あなたの会社は何をしているの、ビル？\nB：この地域で最大のオフィス用品の供給業者( 13 )、でもコンピューターも売っているの。",
            "choices": ["used to", "paid for", "known as", "divided into"],
            "choiceTranslations": [
                "かつて～だった",
                "～の代金を払った",
                "～として知られている",
                "～に分けられた",
            ],
            "answer": 3,
            "choiceAnalysis": [
                "❌ used to＝かつて～だった。現在の会社の説明に不適切",
                "❌ paid for＝～の代金を払った。会社の紹介文に合わない",
                "✅ known as＝～として知られている。地域最大の供給業者→正解",
                "❌ divided into＝～に分けられた。会社の業務説明に合わない",
            ],
            "grammar": "💡 be known as ～＝～として知られている。supplier of ～＝～の供給業者。",
        },
        {
            "number": 14,
            "text": "A : I hope my boss doesn't ( 14 ) my report.\nB : I'm sure he won't. It's very well written.",
            "translation": "A：上司が私のレポートの( 14 )をしないといいんだけど。\nB：きっとしないわ。とてもよく書けているもの。",
            "choices": [
                "find fault with",
                "put up with",
                "look forward to",
                "take part in",
            ],
            "choiceTranslations": [
                "～のあら探しをする",
                "～を我慢する",
                "～を楽しみにする",
                "～に参加する",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ find fault with＝～のあら探しをする・文句を言う。よく書けているので心配ない→正解",
                "❌ put up with＝～を我慢する。上司が部下のレポートを我慢するは不自然",
                "❌ look forward to＝～を楽しみにする。否定的なhopeと矛盾",
                "❌ take part in＝～に参加する。レポートへの参加は不自然",
            ],
            "grammar": "💡 find fault with ～＝～のあら探しをする。I hope ～ doesn't＝～しないことを願う。",
        },
        {
            "number": 15,
            "text": "A : Please ( 15 ) to drinks over there. There are sodas, tea, and water. Just take whatever you want.\nB : Thanks. I'll have a soda.",
            "translation": "A：あちらの飲み物を( 15 )。ソーダ、お茶、水があります。好きなものを取ってください。\nB：ありがとう。ソーダにするわ。",
            "choices": [
                "make sure",
                "help yourself",
                "take care",
                "get acquainted",
            ],
            "choiceTranslations": [
                "確かめる",
                "ご自由にどうぞ",
                "気をつける",
                "知り合う",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ make sure＝確かめる。make sure to drinksは文法的に不自然",
                "✅ help yourself＝ご自由にどうぞ。好きな飲み物を取って→正解",
                "❌ take care＝気をつける。飲み物を勧める場面に合わない",
                "❌ get acquainted＝知り合う。飲み物の案内に合わない",
            ],
            "grammar": "💡 help yourself to ～＝～をご自由にどうぞ。take whatever you want＝好きなものを取る。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["sections"] = [section1]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
