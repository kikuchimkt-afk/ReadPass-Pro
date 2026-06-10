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
                "❌ tight＝きつい。tight shoes（きつい靴）やtight schedule（厳しい日程）に使う語で、メニューの良さは表せない",
                "✅ appealing＝魅力的な。第2文のmany dishes from around the world＋not very expensiveがプラス評価の手がかり→正解",
                "❌ boring＝退屈な。マイナス評価の語。世界各国の料理が豊富という第2文のプラスの内容と正反対",
                "❌ faint＝かすかな。faint sound（かすかな音）やfaint light（弱い光）に使う語で、メニューには使えない",
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
                "❌ entrance＝入口。建物の入口を指す名詞で、人が「気をつける」対象にならない",
                "✅ appearance＝外見・身だしなみ。第2文のclean clothes（きれいな服）＋brushes his hair（髪を梳く）がすべて見た目の手入れ→正解",
                "❌ difference＝違い。his difference（彼の違い）では何と何の違いか不明で意味が通らない",
                "❌ intelligence＝知性。知性に気をつけるなら勉強などの描写になるはず。服や髪の手がかりと結びつかない",
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
                "❌ complaint＝苦情。make a complaint（苦情を言う）の形で使う語。新事業計画を「話し合う」目的と合わない",
                "❌ record＝記録。keep a record（記録をつける）やbreak a record（記録を破る）で使う語。with the managers（人と一緒に開く）ものではない",
                "✅ conference＝会議。have a ( ) with 人＋to talk about ～（～を話し合うために）の形が決め手→正解",
                "❌ treatment＝治療。receive treatment（治療を受ける）で使う医療の語。社長と管理職の場面に無関係",
            ],
            "grammar": "💡 have a conference with ～＝～と会議を開く。to talk about ～（目的のto不定詞）が空所のヒント。",
        },
        {
            "number": 4,
            "text": "The movie's ( 4 ) had a meeting with all of the actors. She explained some important things about their characters.",
            "translation": "映画の( 4 )が俳優全員と会議をしました。彼女は彼らの役柄について重要なことを説明しました。",
            "choices": ["patient", "nephew", "firefighter", "director"],
            "choiceTranslations": ["患者", "甥", "消防士", "監督"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ patient＝患者。病院の場面で使う語。The movie's patient（映画の患者）では意味が通らない",
                "❌ nephew＝甥。家族関係の語。俳優全員を集めて役柄を説明する立場ではない",
                "❌ firefighter＝消防士。職業名だが、映画制作で俳優に演技指導する役割ではない",
                "✅ director＝監督。俳優全員と会議し役柄（their characters）を説明できるのは監督→正解。💡 The movie's ( )＝映画の関係者を選ぶ",
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
                "❌ deserts＝砂漠。場所の名詞。部屋の箱で飼える（has some beetles in a plastic box）ものではない",
                "❌ planets＝惑星。天体の語。crawling around（這い回る）やeating the food（餌を食べる）の描写と結びつかない",
                "✅ insects＝昆虫。beetles（カブトムシ・甲虫）はinsectsの具体例。evenは「（好きが高じて）飼ってさえいる」の流れ→正解",
                "❌ ghosts＝幽霊。実体がないので餌を与える（the food he gives them）ことができず矛盾",
            ],
            "grammar": "💡 insect＝昆虫。抽象（insects）→具体例（beetles）の流れは語彙問題の頻出パターン。crawl around＝這い回る。",
        },
        {
            "number": 6,
            "text": "In the United States, more people are getting heart disease, so the government has started to ( 6 ) healthier lifestyles. They recommend that people exercise every day.",
            "translation": "アメリカでは心臓病になる人が増えているため、政府はより健康的な生活習慣を( 6 )し始めました。毎日運動するよう勧めています。",
            "choices": ["mark", "involve", "lift", "promote"],
            "choiceTranslations": ["印をつける", "関与させる", "持ち上げる", "促進する"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ mark＝印をつける。mark the date（日付に印をつける）など物理的な印に使う語。政策の動詞にならない",
                "❌ involve＝含む・関与させる。The job involves ～（仕事には～が含まれる）のように使い、「広める」意味はない",
                "❌ lift＝持ち上げる。lift a box（箱を持ち上げる）など物理的動作の語。lifestylesを目的語にできない",
                "✅ promote＝促進する・推進する。心臓病増加（原因）→so＋政府が健康的生活を推進（結果）の因果関係が決め手→正解",
            ],
            "grammar": "💡 promote＝促進する（pro-「前へ」＋mote「動かす」）。so＝だから（前半が理由、後半が政府の対策）。",
        },
        {
            "number": 7,
            "text": "A : Are you okay, Heather?\nB : Actually, I feel ( 7 ) tired. I think I should go to bed now.",
            "translation": "A：大丈夫、ヘザー？\nB：実は( 7 )疲れているの。もう寝たほうがいいと思う。",
            "choices": ["regularly", "hardly", "awfully", "gently"],
            "choiceTranslations": ["定期的に", "ほとんど～ない", "とても（強調）", "優しく"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ regularly＝定期的に。exercise regularly（定期的に運動する）のように習慣を表す語。今この瞬間の疲れの程度は表せない",
                "❌ hardly＝ほとんど～ない。hardly tiredなら「ほぼ疲れていない」となり、直後のI should go to bed now（もう寝るべき）と矛盾",
                "✅ awfully＝ものすごく（awful「ひどい」の副詞形だが、ここでは程度の強調）。寝るべきと言うほどの疲れ→正解",
                "❌ gently＝優しく・そっと。speak gently（優しく話す）のように動作の様子を表す語で、tiredの程度は表せない",
            ],
            "grammar": "💡 awfully＝とても・ものすごく（形容詞を強調する副詞）。Are you okay?への返答＝体調不良の流れを読む。",
        },
        {
            "number": 8,
            "text": "Martha had to read a book for her class. She ( 8 ) if it would be interesting, but she really enjoyed it.",
            "translation": "マーサは授業のために本を読まなければなりませんでした。面白いかどうか( 8 )のですが、とても楽しめました。",
            "choices": ["reminded", "replied", "prepared", "wondered"],
            "choiceTranslations": ["思い出した", "返事した", "準備した", "～かどうか思った"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ reminded＝思い出させた。remind 人 of ～（人に～を思い出させる）の形で使い、目的語（人）が必要。if節は続かない",
                "❌ replied＝返事した。reply to ～（～に返事する）の形で使う。読書前の気持ちを表す場面に合わない",
                "❌ prepared＝準備した。prepare for ～（～に備える）の形が基本。「面白いかどうか準備した」では意味が通らない",
                "✅ wondered＝～だろうかと思った。wonder if ～が定型。butで「（不安だったが）実際は楽しめた」と逆接につながる→正解",
            ],
            "grammar": "💡 wonder if ～＝～かどうかなと思う（疑問・不安）。butの前後で気持ちが変わる対比構造に注目。",
        },
        {
            "number": 9,
            "text": "Many people ( 9 ) other people by the way they look. However, it is more important to think about what they are like inside.",
            "translation": "多くの人は見た目で他人を( 9 )。しかし、内面がどうかを考えるほうが大切です。",
            "choices": ["announce", "judge", "practice", "complete"],
            "choiceTranslations": ["発表する", "判断する", "練習する", "完成させる"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ announce＝発表する・公表する。announce the results（結果を発表する）のように情報を公にする語。人を目的語に取れない",
                "✅ judge＝判断する。judge A by B（BでAを判断する）が定型。第2文のinside（内面）がby the way they look（外見）と対比→正解",
                "❌ practice＝練習する。practice the piano（ピアノを練習する）のように技能に使う語。other peopleを練習するは意味不成立",
                "❌ complete＝完成させる。complete the homework（宿題を終わらせる）のように使う語。人を完成させるは意味不成立",
            ],
            "grammar": "💡 judge A by B＝BによってAを判断する。However以降の「外見より内面」という対比が最大のヒント。",
        },
        {
            "number": 10,
            "text": "A : Excuse me. Is this chair ( 10 )?\nB : Yes, it is. My friend is sitting there. He just went to the restroom, but he will be back soon.",
            "translation": "A：すみません。この椅子は( 10 )ですか？\nB：はい。友達が座っています。トイレに行っただけで、すぐ戻ってきます。",
            "choices": ["spread", "expected", "considered", "occupied"],
            "choiceTranslations": ["広がった", "期待された", "考慮された", "使われている"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ spread＝広げられた。spread the map（地図を広げる）やspread butter（バターを塗る）に使う語。椅子の使用状況は表せない",
                "❌ expected＝予期された。be expected to ～（～すると期待される）の形が基本。席が空いているかの質問にならない",
                "❌ considered＝考慮された。be considered (to be) ～（～とみなされる）のように補語が必要。単独では意味が通らない",
                "✅ occupied＝使用中の。BのMy friend is sitting there（友達が座っている）が決め手。トイレや座席の「使用中」の定番表現→正解",
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
                "❌ for the time being＝当分の間・差し当たり。「当分の間買いたい」では一時的な状態の語と一回の購入が合わない",
                "❌ at the same time＝同時に。2つの出来事が同時に起こるときの表現。比較対象がここにはない",
                "❌ once upon a time＝昔々あるところに。おとぎ話の書き出し専用の表現。未来の希望には使えない",
                "✅ in the near future＝近い将来に。butの後のI need to save more money first（まず貯金が必要）→「今すぐではないが近いうち」の流れ→正解",
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
                "❌ a piece of＝一切れの。a piece of cake（ケーキ一切れ）など不可算名詞に使う。dateには使えない",
                "✅ a sort of＝一種の・ある意味。博物館＋夕食を「ある意味デートね」と言う照れた表現。単数形dateと正しくつながる→正解",
                "❌ a lot of＝たくさんの。後ろには複数形（a lot of dates）か不可算名詞が必要。単数形dateには使えない",
                "❌ a couple of＝2〜3の。a couple of days（2、3日）のように複数形が必要。単数形dateには使えない",
            ],
            "grammar": "💡 a sort of ～＝一種の～（＝a kind of）。後ろの名詞が単数形か複数形かが解答の決め手になる文法問題でもある。",
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
                "❌ used to＝（be used to ～で）～に慣れている。「最大の供給業者に慣れている」では会社紹介にならない。used to do（かつて～した）と混同しやすいが、その場合be動詞は不要",
                "❌ paid for＝～の代金を支払われた。we are paid for（代金を受け取る）では「最大の供給業者」が目的語として意味をなさない",
                "✅ known as＝～として知られている。be known as＋肩書き・名称が定型。会社の紹介として自然→正解",
                "❌ divided into＝～に分割された。be divided into groups（グループに分けられる）のように使う。会社の評判の説明にならない",
            ],
            "grammar": "💡 be known as ～＝～として知られている（asの後は肩書き・名称）。be known for ～（～で有名）との区別も頻出。",
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
                "✅ find fault with＝～のあら探しをする。BのIt's very well written（よく書けている）＝あら探しされる心配はない、と自然に呼応→正解",
                "❌ put up with＝～を我慢する。put up with the noise（騒音を我慢する）のように不快なものに使う。doesn'tと合わせると「我慢しないでほしい」となり意味が逆",
                "❌ look forward to＝～を楽しみにする。プラスの意味なので、I hope my boss doesn't ～（してほしくない）と組み合わせると不自然",
                "❌ take part in＝～に参加する。take part in the event（行事に参加する）のように活動に使う。レポートは参加対象ではない",
            ],
            "grammar": "💡 find fault with ～＝～のあら探しをする（fault＝欠点）。Bの返答が空所の意味を特定する根拠になる。",
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
                "❌ make sure＝確かめる。make sure (that) ～やmake sure to do（必ず～する）の形で使い、to＋名詞（to drinks）は続かない",
                "✅ help yourself＝ご自由にどうぞ。help yourself to＋食べ物・飲み物が定型。直後のJust take whatever you want（好きなものを取って）と完全に一致→正解",
                "❌ take care＝気をつける・お大事に。Take care!（じゃあね・お大事に）のように別れ際に使う表現。toの前に置けない",
                "❌ get acquainted＝知り合いになる。get acquainted with＋人の形で使う。飲み物（drinks）と知り合うことはできない",
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
