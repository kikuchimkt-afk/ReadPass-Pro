# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級 data.json
Step A: 大問1（vocabulary型）Q1〜17 — リッチ解説
一次ソース: 2026-1(本会場）/2級.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(17)までの（　　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "In many countries, the ( ) wears a white dress at a wedding. However, in some countries, she may wear a red dress.",
            "translation": "多くの国では、( )は結婚式で白いドレスを着ます。しかし、国によっては赤いドレスを着ることもあります。",
            "choices": ["lawyer", "warrior", "surgeon", "bride"],
            "choiceTranslations": ["弁護士", "戦士", "外科医", "花嫁"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ lawyer＝弁護士。wears a white dress at a wedding（結婚式で白いドレスを着る）の主語として、代名詞 she が指す花嫁の役割と合わない",
                "❌ warrior＝戦士。at a wedding（結婚式で）white dress を着る she の描写として、戦士の職業は文脈に合わない",
                "❌ surgeon＝外科医。However, in some countries, she may wear a red dress（国によっては赤いドレス）という花嫁の衣装の話で、外科医は当てはまらない",
                "✅ bride＝花嫁。wears a white dress at a wedding（結婚式で白いドレスを着る）が花嫁の典型的な描写。代名詞 she とも一致→正解",
            ],
            "grammar": "💡 bride＝花嫁。at a wedding（結婚式で）＋white dress（白いドレス）が「花嫁」を特定する決定的な手がかり。",
        },
        {
            "number": 2,
            "text": "The teacher asked her students to find Argentina on a ( ). She wanted them to learn about countries that are far away from Japan.",
            "translation": "先生は生徒たちに、( )の上でアルゼンチンを見つけるよう求めました。日本から遠い国について学ばせたかったのです。",
            "choices": ["branch", "globe", "scale", "trail"],
            "choiceTranslations": ["枝・支店", "地球儀", "はかり・規模", "小道・跡"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ branch＝枝・支店。find Argentina on a branch（枝の上で国を探す）では地理の学習道具にならない",
                "✅ globe＝地球儀。find ～ on a globe（地球儀の上で～を見つける）は教室でよく使われる表現。遠い国の位置を学ぶ文脈と一致→正解",
                "❌ scale＝はかり・規模。find Argentina on a scale では countries that are far away from Japan（遠い国の位置を学ぶ）という目的に合わない",
                "❌ trail＝小道・跡。find Argentina on a trail では learn about countries（国について学ぶ）教室の地理学習と結びつかない",
            ],
            "grammar": "💡 globe＝地球儀。find ～ on a map / globe は「地図・地球儀で～の位置を探す」定番表現。countries far away from Japan が学習目的のヒント。",
        },
        {
            "number": 3,
            "text": "Yuki only started studying Korean two years ago, but she can already read the newspaper without any ( ). Everyone is surprised by how quickly she has learned the language.",
            "translation": "ゆきさんは韓国語の勉強を始めてまだ2年ですが、すでに何の( )もなく新聞が読めます。どれほど早く言語を習得したか、皆が驚いています。",
            "choices": ["glory", "balance", "difficulty", "priority"],
            "choiceTranslations": ["栄光", "バランス", "困難", "優先事項"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ glory＝栄光。without any glory（栄光なく）では「新聞が読める」という能力の話と結びつかない",
                "❌ balance＝バランス。without any balance は「均衡がない」という意味になり、言語学習の文脈に合わない",
                "✅ difficulty＝困難。without any difficulty（何の困難もなく）＝すんなり読める。only two years ago なのに早く習得した驚きと呼応→正解",
                "❌ priority＝優先事項。without any priority では「優先順位がない」となり、読解の容易さを表せない",
            ],
            "grammar": "💡 without any difficulty＝何の困難もなく（＝容易に）。how quickly she has learned が「困難なくできた」ことの驚きを補強。",
        },
        {
            "number": 4,
            "text": "A: Are you all right? You have a ( ) to be quiet when you're worried.\nB: Do I? I never realized I was like that. I'm fine. I just don't have much to say today.",
            "translation": "A：大丈夫？ 心配なとき、静かになる( )があるのよ。\nB：そうなの？ 自分がそうだとは気づかなかったわ。大丈夫よ。今日はあまり話すことがないだけ。",
            "choices": ["tendency", "discrimination", "shelter", "content"],
            "choiceTranslations": ["傾向", "差別", "避難所", "内容・満足"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ tendency＝傾向。have a tendency to do（～する傾向がある）が定型。心配なとき静かになる＝性格の傾向の話→正解",
                "❌ discrimination＝差別。have a discrimination to be quiet ではコロケーションが成立しない",
                "❌ shelter＝避難所。have a shelter to be quiet では「静かになる避難所」という意味にならない",
                "❌ content＝内容・満足。have a content to be quiet では文法的・意味的に不自然",
            ],
            "grammar": "💡 have a tendency to do＝～する傾向がある。Bの I never realized I was like that（自分がそうだと気づかなかった）が「傾向・癖」の話であることを裏付け。",
        },
        {
            "number": 5,
            "text": "Teachers at Billings Academy try to ( ) leadership qualities in their students. They teach the students how to communicate, make decisions, and take responsibility.",
            "translation": "ビリングス・アカデミーの教師たちは、生徒の中にリーダーシップの資質を( )しようとしています。コミュニケーションの取り方、意思決定、責任の取り方を教えています。",
            "choices": ["hate", "foster", "divide", "pronounce"],
            "choiceTranslations": ["憎む", "育む・促進する", "分ける", "発音する"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ hate＝憎む。try to hate leadership qualities（リーダーシップを憎む）では communicate, make decisions, and take responsibility（指導内容）と正反対",
                "✅ foster＝育む・促進する。foster leadership qualities（リーダーシップの資質を育む）＋communicate / make decisions / take responsibility の指導内容と一致→正解",
                "❌ divide＝分ける。divide qualities（資質を分ける）では教育の目的と合わない",
                "❌ pronounce＝発音する。pronounce qualities では「資質を発音する」となり意味不成立",
            ],
            "grammar": "💡 foster＝育む・促進する（名詞 foster care＝里子育てとも同語源）。leadership qualities in their students＝生徒の中に資質を育てる。",
        },
        {
            "number": 6,
            "text": "On a ( ) Saturday night, Mr. and Mrs. Nelson order pizza and watch TV together. But sometimes, they go out to a restaurant.",
            "translation": "ネルソン夫妻は、( )の土曜の夜にはピザを注文して一緒にテレビを見ます。でも時々、レストランに出かけます。",
            "choices": ["gradual", "chemical", "typical", "false"],
            "choiceTranslations": ["徐々の", "化学の", "典型的な・いつもの", "偽の"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ gradual＝徐々の。a gradual Saturday night では「徐々の土曜の夜」となり、名詞 Saturday night を修飾する形容詞として不自然",
                "❌ chemical＝化学の。a chemical Saturday night では意味が通らない",
                "✅ typical＝典型的な・いつもの。On a typical Saturday night（いつもの土曜の夜には）＋But sometimes（でも時々は）という「普段と例外」の対比→正解",
                "❌ false＝偽の。a false Saturday night では「偽の土曜の夜」となり文脈に合わない",
            ],
            "grammar": "💡 typical＝典型的な・いつもの。But sometimes（しかし時々は）とセットで読むと「普段の行動パターン」を表す typical が決め手。",
        },
        {
            "number": 7,
            "text": "When the movie ended, many people in the theater began to ( ). The story was very sad.",
            "translation": "映画が終わると、劇場の多くの人が( )し始めました。物語はとても悲しかったのです。",
            "choices": ["occur", "swell", "tap", "weep"],
            "choiceTranslations": ["起こる", "膨らむ・腫れる", "軽くたたく", "泣く"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ occur＝起こる。many people in the theater began to occur では人が「起こる」となり、The story was very sad（悲しい物語）への反応として不適切",
                "❌ swell＝膨らむ・腫れる。began to swell（腫れ始めた）では悲しい映画の反応として不適切",
                "❌ tap＝軽くたたく。began to tap では悲しい物語への感情的反応にならない",
                "✅ weep＝泣く。began to weep（泣き始めた）＋The story was very sad（とても悲しい物語）が直接的に結びつく→正解",
            ],
            "grammar": "💡 weep＝泣く（cry より文語的・文学的）。sad story → weep / cry の因果関係は英検頻出パターン。",
        },
        {
            "number": 8,
            "text": "The biology professor showed his students some videos of living cells. He wanted to ( ) how cells work.",
            "translation": "生物学の教授は生徒たちに生きた細胞の映像を見せました。細胞がどのように働くかを( )したかったのです。",
            "choices": ["occupy", "polish", "illustrate", "congratulate"],
            "choiceTranslations": ["占める", "磨く", "説明する・図解する", "祝う"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ occupy＝占める。illustrate how cells work（細胞の働きを占める）では意味不成立",
                "❌ polish＝磨く。polish how cells work では「働き方を磨く」となり、映像を見せる目的と合わない",
                "✅ illustrate＝説明する・図解する。show videos（映像を見せる）→ illustrate how ～ work（～の働きを説明する）が自然な流れ→正解",
                "❌ congratulate＝祝う。congratulate how cells work では文法的に目的語を取れない",
            ],
            "grammar": "💡 illustrate＝（例や図で）説明する。show videos / illustrate how ～ work は「視覚資料で仕組みを示す」定番の組み合わせ。",
        },
        {
            "number": 9,
            "text": "The Green Wolves and the Blue Stars were very evenly matched in the championship game. The Green Wolves ( ) won when they scored a goal in the last seconds of the game.",
            "translation": "グリーン・ウルブズとブルー・スターズは選手権試合で互角でした。グリーン・ウルブズは試合終了間際のゴールで( )勝利しました。",
            "choices": ["secretly", "gently", "barely", "repeatedly"],
            "choiceTranslations": ["こっそり", "優しく・穏やかに", "かろうじて", "繰り返し"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ secretly＝こっそり。secretly won（こっそり勝った）ではスポーツの試合結果の表現として不自然",
                "❌ gently＝優しく・穏やかに。gently won では「穏やかに勝利した」となり、激しい試合の描写と合わない",
                "✅ barely＝かろうじて。evenly matched（互角）＋in the last seconds（終了間際）→ ギリギリの勝利＝barely won→正解",
                "❌ repeatedly＝繰り返し。repeatedly won では「繰り返し勝った」となり、1試合の結果の話と矛盾",
            ],
            "grammar": "💡 barely＝かろうじて・あわや。evenly matched（互角）や in the last seconds（終了間際）と並ぶと「僅差の勝利」を表す。",
        },
        {
            "number": 10,
            "text": "When the teacher said there would be a test next week, the students ( ). They had hoped that they would have more time to study.",
            "translation": "先生が来週テストがあると言うと、生徒たちは( )しました。もっと勉強する時間があることを望んでいたのに。",
            "choices": ["frowned", "slipped", "guessed", "crawled"],
            "choiceTranslations": ["眉をひそめた", "滑った", "推測した", "這った"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ frowned＝眉をひそめた。テスト発表への不満・失望の表情。had hoped more time（もっと時間があると望んでいた）と感情が一致→正解",
                "❌ slipped＝滑った。there would be a test next week（来週テスト）の知らせを聞いて slipped では、had hoped more time to study（勉強時間を望んでいた）感情と合わない",
                "❌ guessed＝推測した。テストの発表を聞いて「推測した」では had hoped との因果が弱い",
                "❌ crawled＝這った。the students crawled when the teacher said there would be a test では、失望の反応として had hoped（望んでいた）と結びつかない",
            ],
            "grammar": "💡 frown＝眉をひそめる（不満・困惑の表情）。had hoped ...（～だと望んでいたのに）が frown の理由を説明する典型構造。",
        },
        {
            "number": 11,
            "text": "( ), people should drink eight glasses of water a day to stay healthy. However, some people may need more or less than this.",
            "translation": "( )、健康を保つために1日8杯の水を飲むべきです。ただし、これより多く必要な人や少なくてよい人もいます。",
            "choices": [
                "For a fresh start",
                "On a specific occasion",
                "In case of emergency",
                "As a general rule",
            ],
            "choiceTranslations": [
                "新たな始まりに",
                "特定の場面で",
                "緊急の場合に",
                "一般に・概して",
            ],
            "answer": 4,
            "choiceAnalysis": [
                "❌ For a fresh start＝新たな始まりに。健康アドバイス全体の導入として不自然。「新たな始まりに水を8杯」では意味が通らない",
                "❌ On a specific occasion＝特定の場面で。後文の However, some people may need more or less（個人差がある）と矛盾。特定の場面限定の助言ではない",
                "❌ In case of emergency＝緊急の場合に。日常的な水分摂取の一般論には当てはまらない",
                "✅ As a general rule＝一般に・概して。一般的な目安を示し、However で個人差を補足する構造→正解",
            ],
            "grammar": "💡 as a general rule＝一般の規則として・概して。However, some people may need more or less（ただし個人差がある）と対で覚える。",
        },
        {
            "number": 12,
            "text": "Ben moved out of his parents' house and into an apartment last week. Now, he has to do everything ( ), like cooking and cleaning.",
            "translation": "ベンは先週、実家を出てアパートに引っ越しました。今は料理や掃除など、すべてを( )しなければなりません。",
            "choices": ["on the air", "at a distance", "to his surprise", "on his own"],
            "choiceTranslations": ["放送中で", "離れて", "驚いたことに", "一人で・自力で"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ on the air＝放送中で。do everything on the air（放送中にすべてをする）では生活の自立と無関係",
                "❌ at a distance＝離れて。do everything at a distance では「離れた場所でする」となり、自立の意味にならない",
                "❌ to his surprise＝驚いたことに。文法的に do everything to his surprise では「驚きながらすべてをする」となり不自然",
                "✅ on his own＝一人で・自力で。実家を出てアパート暮らし→ cooking and cleaning を自分でする＝on his own→正解",
            ],
            "grammar": "💡 on one's own＝一人で・自力で。moved out of parents' house（実家を出た）が「自立」の文脈を作り、on his own の意味を限定する。",
        },
        {
            "number": 13,
            "text": "In the meeting, the president said that he could not ( ) the plan to expand the office because it would be too expensive.",
            "translation": "会議で社長は、オフィス拡張の計画は費用がかかりすぎるため、( )できないと述べました。",
            "choices": ["take away from", "go along with", "bring out in", "watch out for"],
            "choiceTranslations": [
                "〜から奪う・損なう",
                "〜に賛成する・従う",
                "〜を引き出す",
                "〜に注意する",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ take away from＝〜から奪う・価値を損なう。could not take away from the plan では「計画から奪えない」となり、社長の判断として不自然",
                "✅ go along with＝〜に賛成する・従う。could not go along with the plan（計画に賛成できない）＋too expensive（高すぎる）が理由として自然→正解",
                "❌ bring out in＝慣用句として成立しない。bring out（引き出す）と in の組み合わせはこの文脈で使えない",
                "❌ watch out for＝〜に注意する。could not watch out for the plan では「計画に注意できない」となり、賛否の判断と合わない",
            ],
            "grammar": "💡 go along with ～＝～に賛成する・～に従う。could not go along with ... because ...（～なので賛成できない）は会議・交渉の場面で頻出。",
        },
        {
            "number": 14,
            "text": "After ( ) tests, the doctors discovered that Masahiro had a rare illness. They immediately started treating him.",
            "translation": "( )の検査の後、医師たちはマサヒロが珍しい病気であることを発見しました。すぐに治療を始めました。",
            "choices": ["a series of", "the edge of", "a member of", "the back of"],
            "choiceTranslations": [
                "一連の",
                "〜の端",
                "〜の一員",
                "〜の裏側",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ a series of＝一連の。After a series of tests（一連の検査の後）→ discovered a rare illness（珍しい病気を発見）という診断の流れ→正解",
                "❌ the edge of＝〜の端。After the edge of tests では「検査の端の後」となり意味不成立",
                "❌ a member of＝〜の一員。After a member of tests では文法的に tests を修飾できない",
                "❌ the back of＝〜の裏側。After the back of tests では「検査の裏の後」となり不自然",
            ],
            "grammar": "💡 a series of ～＝一連の～。複数回の検査を経て診断に至る流れを表す。immediately started treating が緊急性を補強。",
        },
        {
            "number": 15,
            "text": "A: Our presentation next week will include a lot of data. It will take a lot of work to prepare.\nB: ( ), we are going to be very busy! Let's get started right away.",
            "translation": "A：来週のプレゼンにはたくさんのデータが含まれます。準備にはかなりの作業が必要です。\nB：( )、とても忙しくなりそうですね！ すぐに始めましょう。",
            "choices": [
                "In other words",
                "In the beginning",
                "Back and forth",
                "On the contrary",
            ],
            "choiceTranslations": [
                "言い換えれば",
                "最初に",
                "行ったり来たり",
                "それどころか",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ In other words＝言い換えれば。Aの a lot of work to prepare を B が we are going to be very busy と言い換えている→正解",
                "❌ In the beginning＝最初に。会話の「最初に忙しくなる」ではなく、Aの内容を受けた言い換えが必要",
                "❌ Back and forth＝行ったり来たり。文頭の接続詞・副詞句としてこの会話に合わない",
                "❌ On the contrary＝それどころか。AとBは同じ方向の内容（忙しい）なので逆接にはならない",
            ],
            "grammar": "💡 in other words＝言い換えれば。直前の内容を別の表現で言い直すときの接続。Let's get started right away が忙しさを受けた行動。",
        },
        {
            "number": 16,
            "text": "The two paintings looked ( ) each other at first, but when John looked more closely, he saw that they were very similar in one way.",
            "translation": "2つの絵は最初は互いに( )ように見えましたが、ジョンがもっとよく見ると、ある点ではとても似ていることに気づきました。",
            "choices": ["distinct from", "composed of", "absent from", "threatening to"],
            "choiceTranslations": [
                "〜と明確に異なる",
                "〜で構成された",
                "〜から欠席している",
                "〜を脅かす",
            ],
            "answer": 1,
            "choiceAnalysis": [
                "✅ distinct from＝〜と明確に異なる。looked distinct from each other at first（最初は互いに異なって見えた）＋but ... very similar（しかし似ていた）の対比→正解",
                "❌ composed of＝〜で構成されている。looked composed of each other では「互いで構成されて見えた」となり不自然",
                "❌ absent from＝〜から欠席している。絵が「欠席している」ようには見えない",
                "❌ threatening to＝〜を脅かす。looked threatening to each other では「互いを脅かすようだった」となり、似ていることの発見と無関係",
            ],
            "grammar": "💡 distinct from ～＝～と明確に異なる。but 以下の similar（似ている）と対比させて読む。at first ... but when ... more closely の逆転構造。",
        },
        {
            "number": 17,
            "text": "The company had to ( ) some of its workers because it was losing money. It was a very difficult decision to make.",
            "translation": "会社は赤字が続いていたため、従業員の一部を( )せざるを得ませんでした。とても難しい決断でした。",
            "choices": ["flip over", "lay off", "bring about", "catch up"],
            "choiceTranslations": [
                "ひっくり返す",
                "解雇する",
                "引き起こす",
                "追いつく",
            ],
            "answer": 2,
            "choiceAnalysis": [
                "❌ flip over＝ひっくり返す。flip over workers（従業員をひっくり返す）では経営判断の文脈に合わない",
                "✅ lay off＝解雇する。lay off workers（従業員を解雇する）＋losing money（赤字）＋difficult decision（難しい決断）が一貫→正解",
                "❌ bring about＝引き起こす。bring about workers では「従業員を引き起こす」となり意味不成立",
                "❌ catch up＝追いつく。catch up workers では「従業員に追いつく」となり、人員削減の文脈と無関係",
            ],
            "grammar": "💡 lay off＝解雇する（一時解雇・恒久解雇の両方あり得る）。because it was losing money が lay off の直接的な理由。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 大問1リッチ解説を保存: {DATA_PATH}")
print(f"   問題数: {len(section1['questions'])}")
