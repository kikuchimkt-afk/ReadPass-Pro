# -*- coding: utf-8 -*-
"""
2026年度 第1回（準会場）英検2級 data.json 生成スクリプト
Step A: sections（大問1・大問2・大問3）
既存の data.json（vocabulary 済み）を読み込み、sections を追加して保存する。
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = r"G:\マイドライブ\ReadPass Pro\data\grade2\2026-1-sat\data.json"

# ============================================================
# Section 0: 大問1（vocabulary 型）Q1〜Q17
# ============================================================

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A : Were there any problems on the flight? B : No, there were no ( 1 ). It was a very smooth journey.",
            "translation": "A：フライトで何か問題はありましたか？ B：いいえ、何の( 1 )もありませんでした。とても快適な旅でした。",
            "choices": ["arguments", "impressions", "incidents", "outcomes"],
            "answer": 3,
            "choiceAnalysis": [
                "arguments=口論→「問題がなかった」の言い換えとして不適切",
                "impressions=印象→文脈に合わない",
                "incidents=出来事・事件→正解。💡 no incidents（何事もなく）= a very smooth journey と一致",
                "outcomes=結果→文脈に合わない"
            ]
        },
        {
            "number": 2,
            "text": "A : How many apples do you want, Sarah? B : Just a small ( 2 ). I only need enough for an apple pie.",
            "translation": "A：リンゴはいくつ欲しい、サラ？ B：少しの( 2 )だけでいいわ。アップルパイに足りる分だけ必要なの。",
            "choices": ["destination", "quantity", "sacrifice", "achievement"],
            "answer": 2,
            "choiceAnalysis": [
                "destination=目的地→リンゴの数の話に合わない",
                "quantity=量→正解。💡 a small quantity（少量）= enough for an apple pie と一致",
                "sacrifice=犠牲→文脈に合わない",
                "achievement=業績→文脈に合わない"
            ]
        },
        {
            "number": 3,
            "text": "The chef told the new cook to ( 3 ) the soup carefully so that it would not stick to the bottom of the pot.",
            "translation": "シェフは新人の料理人に、鍋の底にくっつかないようにスープを注意深く( 3 )ように言った。",
            "choices": ["spill", "resemble", "stir", "amuse"],
            "answer": 3,
            "choiceAnalysis": [
                "spill=こぼす→鍋にくっつかないようにする行為ではない",
                "resemble=似ている→文脈に合わない",
                "stir=かき混ぜる→正解。💡 焦げ付き（stick to the bottom）防止にはかき混ぜる",
                "amuse=楽しませる→文脈に合わない"
            ]
        },
        {
            "number": 4,
            "text": "A : Excuse me. I'm looking for a high-quality tennis racket. B : I recommend this one. It's ( 4 ) by many professional tennis players, and many serious amateurs use it, too.",
            "translation": "A：すみません。高品質のテニスラケットを探しています。 B：こちらがおすすめです。多くのプロテニス選手に( 4 )されていて、本格的なアマチュアの多くも使っています。",
            "choices": ["threatened", "increased", "favored", "rescued"],
            "answer": 3,
            "choiceAnalysis": [
                "threatened=脅かされる→文脈に合わない",
                "increased=増やされる→文脈に合わない",
                "favored=好まれる→正解。💡 プロに好まれ、アマチュアも使う＝人気のラケット",
                "rescued=救助される→文脈に合わない"
            ]
        },
        {
            "number": 5,
            "text": "Many of the ( 5 ) that provided electricity to houses in the area were destroyed in the storm. The electricity company took three days to repair them all.",
            "translation": "その地域の家に電気を供給していた( 5 )の多くが嵐で破壊された。電力会社がすべてを修理するのに3日かかった。",
            "choices": ["cables", "leaps", "journals", "surveys"],
            "answer": 1,
            "choiceAnalysis": [
                "cables=ケーブル→正解。💡 電気を供給し（provided electricity）、嵐で壊れて修理されるもの＝電線",
                "leaps=跳躍→文脈に合わない",
                "journals=雑誌・日誌→文脈に合わない",
                "surveys=調査→文脈に合わない"
            ]
        },
        {
            "number": 6,
            "text": "The students in Mrs. Johnson's class gave her a present to show their ( 6 ) for her teaching them this year.",
            "translation": "ジョンソン先生のクラスの生徒たちは、今年教えてくれたことへの( 6 )を示すために先生にプレゼントを贈った。",
            "choices": ["preference", "victory", "appreciation", "disappointment"],
            "answer": 3,
            "choiceAnalysis": [
                "preference=好み→プレゼントを贈る理由として不適切",
                "victory=勝利→文脈に合わない",
                "appreciation=感謝→正解。💡 show their appreciation for ～＝～への感謝を示す",
                "disappointment=失望→プレゼントを贈る文脈と逆"
            ]
        },
        {
            "number": 7,
            "text": "When the teacher saw the broken window, she ( 7 ) the children in a loud voice for playing with a ball in the classroom.",
            "translation": "先生は割れた窓を見ると、教室でボール遊びをしたことについて大声で子どもたちを( 7 )。",
            "choices": ["detected", "infected", "scolded", "grabbed"],
            "answer": 3,
            "choiceAnalysis": [
                "detected=発見した→大声で行う行為ではない",
                "infected=感染させた→文脈に合わない",
                "scolded=叱った→正解。💡 scold A for B＝AをBのことで叱る。割れた窓＋大声の文脈と一致",
                "grabbed=つかんだ→文脈に合わない"
            ]
        },
        {
            "number": 8,
            "text": "A : How long do you think it will take us to get to the coast? B : Well, if there aren't any major problems on the roads, I ( 8 ) that it will take us about three hours.",
            "translation": "A：海岸まで行くのにどのくらいかかると思う？ B：そうだね、道路に大きな問題がなければ、3時間ほどかかると( 8 )するよ。",
            "choices": ["estimate", "decline", "stimulate", "neglect"],
            "answer": 1,
            "choiceAnalysis": [
                "estimate=見積もる→正解。💡 estimate that ...＝（時間などを）～と見積もる・推定する",
                "decline=断る・減少する→文脈に合わない",
                "stimulate=刺激する→文脈に合わない",
                "neglect=怠る→文脈に合わない"
            ]
        },
        {
            "number": 9,
            "text": "When it was announced that the train was going to be late, many of the passengers were upset. However, Michael sat ( 9 ) and read his book because he was not in a hurry.",
            "translation": "電車が遅れるとアナウンスされたとき、多くの乗客は動揺した。しかしマイケルは急いでいなかったので、( 9 )座って本を読んでいた。",
            "choices": ["legally", "roughly", "barely", "patiently"],
            "answer": 4,
            "choiceAnalysis": [
                "legally=合法的に→文脈に合わない",
                "roughly=おおよそ・乱暴に→文脈に合わない",
                "barely=かろうじて→文脈に合わない",
                "patiently=辛抱強く→正解。💡 not in a hurry（急いでいない）→落ち着いて辛抱強く待つ"
            ]
        },
        {
            "number": 10,
            "text": "The ( 10 ) price of gold has reached a record high. It is much more expensive this year than last year.",
            "translation": "金の( 10 )価格は記録的な高値に達した。昨年よりも今年のほうがはるかに高い。",
            "choices": ["negative", "absent", "current", "sudden"],
            "answer": 3,
            "choiceAnalysis": [
                "negative=否定的な→文脈に合わない",
                "absent=不在の→文脈に合わない",
                "current=現在の→正解。💡 current price（現在の価格）＝this year の価格の話と一致",
                "sudden=突然の→文脈に合わない"
            ]
        },
        {
            "number": 11,
            "text": "Ingrid has been working in a small company for two years. ( 11 ), she has been the only one in sales, but next week, another person will join her.",
            "translation": "イングリッドは2年間小さな会社で働いている。( 11 )、営業部門は彼女一人だけだったが、来週もう一人が加わる予定だ。",
            "choices": ["On the way", "In the end", "Up until now", "For the sake"],
            "answer": 3,
            "choiceAnalysis": [
                "On the way=途中で→文脈に合わない",
                "In the end=結局→文脈に合わない",
                "Up until now=今まで→正解。💡 現在完了（has been）＋ but next week（来週からは変わる）と対応",
                "For the sake=～のために→単独では使えない形"
            ]
        },
        {
            "number": 12,
            "text": "All the members of the drama club wanted to play a main character in the school's play. ( 12 ), not all of them could get one.",
            "translation": "演劇部のメンバー全員が学校の劇で主役を演じたがっていた。( 12 )、全員が主役になれるわけではなかった。",
            "choices": ["On the contrary", "Just in case", "Needless to say", "In other words"],
            "answer": 3,
            "choiceAnalysis": [
                "On the contrary=それどころか→前文の否定ではない",
                "Just in case=念のため→文脈に合わない",
                "Needless to say=言うまでもなく→正解。💡 全員が主役にはなれないのは当然の帰結",
                "In other words=言い換えれば→言い換えではない"
            ]
        },
        {
            "number": 13,
            "text": "Patrick's parents told him that he should not ( 13 ) with his little sister. They said he should be more patient and try to stay calm.",
            "translation": "パトリックの両親は、妹に対して( 13 )べきではないと彼に言った。もっと我慢強く、冷静でいるよう努めるべきだと言ったのだ。",
            "choices": ["make his way", "hold his breath", "take his place", "lose his temper"],
            "answer": 4,
            "choiceAnalysis": [
                "make his way=進む→文脈に合わない",
                "hold his breath=息を止める→文脈に合わない",
                "take his place=彼の代わりをする→文脈に合わない",
                "lose his temper=かんしゃくを起こす→正解。💡 be more patient / stay calm（我慢強く・冷静に）と対比"
            ]
        },
        {
            "number": 14,
            "text": "Sarah submitted her college applications last week. She is ( 14 ) that she gets accepted into her dream school.",
            "translation": "サラは先週、大学の出願書類を提出した。彼女は夢の学校に合格できるよう( 14 )いる。",
            "choices": ["coming into her hand", "keeping her fingers crossed", "taking her breath away", "making up her mind"],
            "answer": 2,
            "choiceAnalysis": [
                "coming into her hand=手に入る→文脈に合わない",
                "keeping her fingers crossed=幸運を祈っている→正解。💡 合格（gets accepted）を願う気持ちと一致",
                "taking her breath away=息をのむほど驚かせる→文脈に合わない",
                "making up her mind=決心する→出願はもう済んでいる"
            ]
        },
        {
            "number": 15,
            "text": "Mr. Smith is always ( 15 ) his decisions. He never doubts himself, even when other people disagree with him.",
            "translation": "スミス氏は常に自分の決断に( 15 )。他の人が反対しても、決して自分を疑わない。",
            "choices": ["sorry for", "similar to", "confident of", "tired of"],
            "answer": 3,
            "choiceAnalysis": [
                "sorry for=～をすまなく思う→「自分を疑わない」と矛盾",
                "similar to=～に似ている→文脈に合わない",
                "confident of=～に自信がある→正解。💡 never doubts himself（決して自分を疑わない）の言い換え",
                "tired of=～にうんざりしている→文脈に合わない"
            ]
        },
        {
            "number": 16,
            "text": "When traveling in the mountains, it is important to ( 16 ) the paths that are marked. Going off the paths can be dangerous because of the steep hills and trees.",
            "translation": "山を旅行するときは、印のついた道を( 16 )ことが大切だ。道を外れると、急な斜面や木々のせいで危険なことがある。",
            "choices": ["keep to", "hand over", "pull off", "lie down"],
            "answer": 1,
            "choiceAnalysis": [
                "keep to=～から離れない・～を守る→正解。💡 Going off the paths（道を外れること）の危険と対比",
                "hand over=手渡す→文脈に合わない",
                "pull off=成し遂げる・脱ぐ→文脈に合わない",
                "lie down=横になる→文脈に合わない"
            ]
        },
        {
            "number": 17,
            "text": "A : Did going to college have any ( 17 ) your life? B : Definitely. I met a lot of people who helped me develop important skills, and I also gained a lot of confidence in myself.",
            "translation": "A：大学に行ったことはあなたの人生に何か( 17 )ありましたか？ B：もちろん。重要なスキルを伸ばす手助けをしてくれる多くの人に出会ったし、自分への自信も大きくつきました。",
            "choices": ["effect on", "comparison to", "responsibility for", "reaction to"],
            "answer": 1,
            "choiceAnalysis": [
                "effect on=～への影響→正解。💡 have an effect on ～＝～に影響を与える。Bの返答（スキル・自信）＝人生への影響",
                "comparison to=～との比較→文脈に合わない",
                "responsibility for=～への責任→文脈に合わない",
                "reaction to=～への反応→文脈に合わない"
            ]
        }
    ]
}

# ============================================================
# Section 1: 大問2（passage-fill 型）Q18〜Q23
# ============================================================

# --- 2A: Child-Friendly City ---
p2a_paras = [
    "The city of Pontevedra, in Spain, has been praised for its efforts to make the city a better place for families. In the 1990s, Pontevedra was like many other mid-size cities in Spain, surrounded by traffic and pollution. Children had to be driven everywhere because it was too dangerous for them to walk. This inspired the city's mayor, Miguel Anxo Fernández Lores, to take a surprising step. ( 18 ) trying to find ways to deal with the traffic, such as building more parking areas, he decided to get rid of the cars and close the city center to traffic.",
    "At first, some people argued against the changes. Lores, however, wanted people to ( 19 ) for themselves. After a short trial, citizens began to see the positive results. The streets became safer and less polluted, and people started to enjoy walking and cycling in the city. Shops reported more customers because people walking around the city center were more likely to stop and shop.",
    "Since then, the changes have been made permanent. Observations by researchers indicate that these improvements are not just about traffic. They reflect a broader effort to make urban spaces more friendly to children. Pontevedra has shown other cities what can be achieved when leaders are willing to ban cars from city centers and ( 20 ) to live and play in."
]

p2a_trans = [
    "スペインのポンテベドラ市は、市を家族にとってより良い場所にする取り組みで称賛されてきた。1990年代、ポンテベドラはスペインの他の多くの中規模都市と同様、交通と汚染に囲まれていた。子どもたちは歩くには危険すぎたため、どこへ行くにも車で送ってもらわなければならなかった。これがきっかけとなり、市長のミゲル・アンショ・フェルナンデス・ロレスは驚くべき一歩を踏み出した。駐車場を増やすなど交通に対処する方法を探す( 18 )、彼は車をなくし、市の中心部を交通に対して閉鎖することを決めたのだ。",
    "当初、その変化に反対する人もいた。しかしロレスは、人々に自分自身で( 19 )してほしいと考えていた。短い試行期間の後、市民は良い結果を目にし始めた。通りはより安全で汚染も減り、人々は市内を歩いたり自転車に乗ったりすることを楽しみ始めた。市の中心部を歩き回る人々は立ち止まって買い物をする可能性が高かったため、店は客が増えたと報告した。",
    "それ以来、その変化は恒久的なものとなった。研究者による観察は、これらの改善が交通だけの問題ではないことを示している。それらは、都市空間を子どもにとってより親しみやすいものにするための、より広範な取り組みを反映している。ポンテベドラは、指導者が市の中心部から車を締め出し、子どもたちが住み遊ぶための( 20 )意志があるときに何が達成できるかを、他の都市に示したのである。"
]

p2a_pairs = [
    ["The city of Pontevedra, in Spain, has been praised for its efforts to make the city a better place for families.",
     "スペインのポンテベドラ市は、市を家族にとってより良い場所にする取り組みで称賛されてきた。"],
    ["In the 1990s, Pontevedra was like many other mid-size cities in Spain, surrounded by traffic and pollution.",
     "1990年代、ポンテベドラはスペインの他の多くの中規模都市と同様、交通と汚染に囲まれていた。"],
    ["Children had to be driven everywhere because it was too dangerous for them to walk.",
     "子どもたちは歩くには危険すぎたため、どこへ行くにも車で送ってもらわなければならなかった。"],
    ["This inspired the city's mayor, Miguel Anxo Fernández Lores, to take a surprising step.",
     "これがきっかけとなり、市長のミゲル・アンショ・フェルナンデス・ロレスは驚くべき一歩を踏み出した。"],
    ["( 18 ) trying to find ways to deal with the traffic, such as building more parking areas, he decided to get rid of the cars and close the city center to traffic.",
     "駐車場を増やすなど交通に対処する方法を探す( 18 )、彼は車をなくし、市の中心部を交通に対して閉鎖することを決めたのだ。"],
    ["At first, some people argued against the changes.",
     "当初、その変化に反対する人もいた。"],
    ["Lores, however, wanted people to ( 19 ) for themselves.",
     "しかしロレスは、人々に自分自身で( 19 )してほしいと考えていた。"],
    ["After a short trial, citizens began to see the positive results.",
     "短い試行期間の後、市民は良い結果を目にし始めた。"],
    ["The streets became safer and less polluted, and people started to enjoy walking and cycling in the city.",
     "通りはより安全で汚染も減り、人々は市内を歩いたり自転車に乗ったりすることを楽しみ始めた。"],
    ["Shops reported more customers because people walking around the city center were more likely to stop and shop.",
     "市の中心部を歩き回る人々は立ち止まって買い物をする可能性が高かったため、店は客が増えたと報告した。"],
    ["Since then, the changes have been made permanent.",
     "それ以来、その変化は恒久的なものとなった。"],
    ["Observations by researchers indicate that these improvements are not just about traffic.",
     "研究者による観察は、これらの改善が交通だけの問題ではないことを示している。"],
    ["They reflect a broader effort to make urban spaces more friendly to children.",
     "それらは、都市空間を子どもにとってより親しみやすいものにするための、より広範な取り組みを反映している。"],
    ["Pontevedra has shown other cities what can be achieved when leaders are willing to ban cars from city centers and ( 20 ) to live and play in.",
     "ポンテベドラは、指導者が市の中心部から車を締め出し、子どもたちが住み遊ぶための( 20 )意志があるときに何が達成できるかを、他の都市に示したのである。"]
]

# --- 2B: Dead Trees ---
p2b_paras = [
    "Dead trees are often full of life. In the woods, for example, they support many different animals and insects in various ways. When a tree is no longer alive or standing, it becomes a habitat, or a place to live, for many living things. First, mushrooms help break down the tree. This allows insects to ( 21 ). In turn, new insects and other creatures begin to grow. Some small animals hide under bark that has fallen off the tree. Some birds build their houses in holes in the wood.",
    "Dead trees not only provide homes for animals but also help keep forests healthy. While still alive, trees absorb carbon and help lower the amount of CO₂ in the air. ( 22 ), they serve as natural carbon storage after they die. When the wood breaks down, carbon and other elements eventually return to the ground, helping young plants grow. These substances are important for maintaining rich forest soil. In this way, dead trees are an important part of the natural forest cycle.",
    "While it is true that dead trees are helpful to the environment, they can also create problems in some situations. For instance, it might be necessary to remove them from places such as parks, campgrounds, and roadsides for safety reasons. This is especially important ( 23 ). In these conditions, dead trees lack moisture and can catch fire easily, causing serious damage. Removing dead trees where necessary can help prevent more serious issues in the future."
]

p2b_trans = [
    "枯れ木はしばしば生命に満ちあふれている。例えば森の中では、枯れ木はさまざまな方法で多くの異なる動物や昆虫を支えている。木が生きていなかったり立っていなかったりすると、それは多くの生き物にとっての生息地、つまり住む場所になる。まず、キノコが木の分解を助ける。これにより昆虫は( 21 )ことができる。やがて、新しい昆虫やその他の生き物が育ち始める。木から剥がれ落ちた樹皮の下に隠れる小動物もいる。木の穴に巣を作る鳥もいる。",
    "枯れ木は動物に住みかを提供するだけでなく、森林を健康に保つのにも役立つ。生きている間、木は炭素を吸収し、空気中のCO₂の量を減らすのに役立つ。( 22 )、枯れた後は天然の炭素貯蔵庫としての役割を果たす。木材が分解されると、炭素やその他の元素は最終的に地面に戻り、若い植物の成長を助ける。これらの物質は豊かな森林土壌を維持するために重要である。このように、枯れ木は自然の森林サイクルの重要な一部なのである。",
    "枯れ木が環境に役立つことは事実だが、状況によっては問題を引き起こすこともある。例えば、安全上の理由から、公園、キャンプ場、道路沿いなどの場所から枯れ木を取り除く必要があるかもしれない。これは( 23 )特に重要である。こうした状況では、枯れ木は水分を欠き、簡単に火がついて深刻な被害をもたらすことがある。必要な場所で枯れ木を取り除くことは、将来のより深刻な問題を防ぐのに役立つ。"
]

p2b_pairs = [
    ["Dead trees are often full of life.",
     "枯れ木はしばしば生命に満ちあふれている。"],
    ["In the woods, for example, they support many different animals and insects in various ways.",
     "例えば森の中では、枯れ木はさまざまな方法で多くの異なる動物や昆虫を支えている。"],
    ["When a tree is no longer alive or standing, it becomes a habitat, or a place to live, for many living things.",
     "木が生きていなかったり立っていなかったりすると、それは多くの生き物にとっての生息地、つまり住む場所になる。"],
    ["First, mushrooms help break down the tree.",
     "まず、キノコが木の分解を助ける。"],
    ["This allows insects to ( 21 ).",
     "これにより昆虫は( 21 )ことができる。"],
    ["In turn, new insects and other creatures begin to grow.",
     "やがて、新しい昆虫やその他の生き物が育ち始める。"],
    ["Some small animals hide under bark that has fallen off the tree.",
     "木から剥がれ落ちた樹皮の下に隠れる小動物もいる。"],
    ["Some birds build their houses in holes in the wood.",
     "木の穴に巣を作る鳥もいる。"],
    ["Dead trees not only provide homes for animals but also help keep forests healthy.",
     "枯れ木は動物に住みかを提供するだけでなく、森林を健康に保つのにも役立つ。"],
    ["While still alive, trees absorb carbon and help lower the amount of CO₂ in the air.",
     "生きている間、木は炭素を吸収し、空気中のCO₂の量を減らすのに役立つ。"],
    ["( 22 ), they serve as natural carbon storage after they die.",
     "( 22 )、枯れた後は天然の炭素貯蔵庫としての役割を果たす。"],
    ["When the wood breaks down, carbon and other elements eventually return to the ground, helping young plants grow.",
     "木材が分解されると、炭素やその他の元素は最終的に地面に戻り、若い植物の成長を助ける。"],
    ["These substances are important for maintaining rich forest soil.",
     "これらの物質は豊かな森林土壌を維持するために重要である。"],
    ["In this way, dead trees are an important part of the natural forest cycle.",
     "このように、枯れ木は自然の森林サイクルの重要な一部なのである。"],
    ["While it is true that dead trees are helpful to the environment, they can also create problems in some situations.",
     "枯れ木が環境に役立つことは事実だが、状況によっては問題を引き起こすこともある。"],
    ["For instance, it might be necessary to remove them from places such as parks, campgrounds, and roadsides for safety reasons.",
     "例えば、安全上の理由から、公園、キャンプ場、道路沿いなどの場所から枯れ木を取り除く必要があるかもしれない。"],
    ["This is especially important ( 23 ).",
     "これは( 23 )特に重要である。"],
    ["In these conditions, dead trees lack moisture and can catch fire easily, causing serious damage.",
     "こうした状況では、枯れ木は水分を欠き、簡単に火がついて深刻な被害をもたらすことがある。"],
    ["Removing dead trees where necessary can help prevent more serious issues in the future.",
     "必要な場所で枯れ木を取り除くことは、将来のより深刻な問題を防ぐのに役立つ。"]
]

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(18)から(23)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Child-Friendly City",
            "paragraphs": p2a_paras,
            "translations": p2a_trans,
            "sentencePairs": p2a_pairs,
            "questions": [
                {
                    "number": 18,
                    "choices": ["Because of", "In addition to", "Regardless of", "Instead of"],
                    "answer": 4,
                    "choiceAnalysis": [
                        "Because of=～のために→因果関係ではない",
                        "In addition to=～に加えて→駐車場建設などは実際には行っていないので不適",
                        "Regardless of=～に関係なく→文脈に合わない",
                        "Instead of=～の代わりに→正解。💡 交通対策（駐車場建設など）を探す代わりに、車自体をなくすという対比"
                    ]
                },
                {
                    "number": 19,
                    "choices": [
                        "record the changes and write reports",
                        "experience the changes and give feedback",
                        "study the changes and publish findings",
                        "ignore the changes and continue driving"
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "変化を記録し報告書を書く→市民の行動として本文にない",
                        "変化を体験し意見を伝える→正解。💡 直後の After a short trial, citizens began to see the positive results（試行後に市民が良さを実感）と一致",
                        "変化を研究し結果を発表する→研究者の行動であり市民ではない",
                        "変化を無視して運転を続ける→改革の趣旨と正反対"
                    ]
                },
                {
                    "number": 20,
                    "choices": [
                        "leave areas that are only for adults to relax in",
                        "build large parking areas for families to use",
                        "create a fun place for them",
                        "provide more cars for them"
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "大人だけがくつろぐ場所を残す→「子どもに優しい都市」の趣旨と逆",
                        "家族向けの大きな駐車場を建設する→車を排除する方針と矛盾",
                        "彼らのための楽しい場所をつくる→正解。💡 make urban spaces more friendly to children の言い換え。them＝children",
                        "彼らにもっと車を提供する→方針と正反対"
                    ]
                }
            ]
        },
        {
            "label": "B",
            "title": "Dead Trees",
            "paragraphs": p2b_paras,
            "translations": p2b_trans,
            "sentencePairs": p2b_pairs,
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "go inside the tree and lay eggs",
                        "fly around the area and build nests",
                        "leave the tree and search for food",
                        "climb the tree and eat its leaves"
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "木の中に入り卵を産む→正解。💡 直後の In turn, new insects and other creatures begin to grow（新しい昆虫が育ち始める）につながる",
                        "周囲を飛び回り巣を作る→巣作りは後述の鳥の行動",
                        "木を離れて食べ物を探す→枯れ木が住みかになるという流れと逆",
                        "木に登って葉を食べる→枯れ木に葉はない"
                    ]
                },
                {
                    "number": 22,
                    "choices": ["On the other hand", "For example", "In contrast", "Additionally"],
                    "answer": 4,
                    "choiceAnalysis": [
                        "On the other hand=他方で→対比ではなく追加の内容",
                        "For example=例えば→具体例ではない",
                        "In contrast=対照的に→対比ではない",
                        "Additionally=さらに→正解。💡 生きている間の働き（CO₂削減）に加えて、死後も炭素貯蔵庫として役立つという追加情報"
                    ]
                },
                {
                    "number": 23,
                    "choices": [
                        "in forests that are near large rivers",
                        "in areas that have heavy rainfall",
                        "in dry climates or during dry seasons",
                        "in places where the soil is very rich"
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "大きな川の近くの森→湿っており火災の危険が低い",
                        "降水量の多い地域→同じく火災の危険が低い",
                        "乾燥した気候や乾季→正解。💡 直後の dead trees lack moisture and can catch fire easily（水分を欠き燃えやすい）と一致",
                        "土壌が非常に豊かな場所→火災の危険とは無関係"
                    ]
                }
            ]
        }
    ]
}

# ============================================================
# Section 2: 大問3（reading-comprehension 型）Q24〜Q31
# ============================================================

# --- 3A: Email（工場見学の問い合わせ） ---
p3a_paras = [
    "My name is Jessica Jenkins, and I teach at Riverstone High School. Our students have been learning about manufacturing in social studies class, and one of my students has shown a strong interest in how everyday products, such as plastic bottles, are made. He found your factory's information online and was impressed by the work you did. After doing some research on his own, he would like to visit your factory to learn more.",
    "I am writing to ask whether it would be possible for the student to join one of the factory tours held on Fridays by himself. His last class of the day ends at 2:00 p.m. on Fridays, which is earlier than on other days. As the school is within walking distance of your factory, if he leaves right after the class, he should be able to arrive by 2:30 p.m.",
    "Please let me know if there is an available date and time for a tour on a Friday in the next two months. Could you also tell us what he should bring or prepare in advance? He would like to take a few photos for his class report, so please let us know whether photography is permitted during the tour. Thank you very much for your time and consideration. I look forward to hearing from you."
]

p3a_trans = [
    "私はジェシカ・ジェンキンスと申しまして、リバーストーン高校で教えています。本校の生徒たちは社会科の授業で製造業について学んでおり、生徒の一人がペットボトルなどの日用品がどのように作られるかに強い興味を示しています。彼はオンラインで貴工場の情報を見つけ、皆さまの仕事に感銘を受けました。自分なりに調べた後、さらに学ぶために貴工場を見学したいと考えています。",
    "その生徒が一人で、金曜日に開催されている工場見学ツアーに参加することが可能かどうかをお尋ねしたく、ご連絡しております。金曜日は彼のその日の最後の授業が午後2時に終わり、他の曜日より早く終わります。学校は貴工場から徒歩圏内にありますので、授業後すぐに出発すれば、午後2時30分までには到着できるはずです。",
    "今後2か月以内の金曜日で、ツアーに参加できる日時があれば教えてください。また、事前に持参または準備すべきものがあれば教えていただけますでしょうか。彼は授業のレポート用に写真を数枚撮りたいと考えていますので、ツアー中の写真撮影が許可されているかどうかもお知らせください。お時間とご配慮をいただき誠にありがとうございます。お返事をお待ちしております。"
]

p3a_pairs = [
    ["My name is Jessica Jenkins, and I teach at Riverstone High School.",
     "私はジェシカ・ジェンキンスと申しまして、リバーストーン高校で教えています。"],
    ["Our students have been learning about manufacturing in social studies class, and one of my students has shown a strong interest in how everyday products, such as plastic bottles, are made.",
     "本校の生徒たちは社会科の授業で製造業について学んでおり、生徒の一人がペットボトルなどの日用品がどのように作られるかに強い興味を示しています。"],
    ["He found your factory's information online and was impressed by the work you did.",
     "彼はオンラインで貴工場の情報を見つけ、皆さまの仕事に感銘を受けました。"],
    ["After doing some research on his own, he would like to visit your factory to learn more.",
     "自分なりに調べた後、さらに学ぶために貴工場を見学したいと考えています。"],
    ["I am writing to ask whether it would be possible for the student to join one of the factory tours held on Fridays by himself.",
     "その生徒が一人で、金曜日に開催されている工場見学ツアーに参加することが可能かどうかをお尋ねしたく、ご連絡しております。"],
    ["His last class of the day ends at 2:00 p.m. on Fridays, which is earlier than on other days.",
     "金曜日は彼のその日の最後の授業が午後2時に終わり、他の曜日より早く終わります。"],
    ["As the school is within walking distance of your factory, if he leaves right after the class, he should be able to arrive by 2:30 p.m.",
     "学校は貴工場から徒歩圏内にありますので、授業後すぐに出発すれば、午後2時30分までには到着できるはずです。"],
    ["Please let me know if there is an available date and time for a tour on a Friday in the next two months.",
     "今後2か月以内の金曜日で、ツアーに参加できる日時があれば教えてください。"],
    ["Could you also tell us what he should bring or prepare in advance?",
     "また、事前に持参または準備すべきものがあれば教えていただけますでしょうか。"],
    ["He would like to take a few photos for his class report, so please let us know whether photography is permitted during the tour.",
     "彼は授業のレポート用に写真を数枚撮りたいと考えていますので、ツアー中の写真撮影が許可されているかどうかもお知らせください。"],
    ["Thank you very much for your time and consideration.",
     "お時間とご配慮をいただき誠にありがとうございます。"],
    ["I look forward to hearing from you.",
     "お返事をお待ちしております。"]
]

# --- 3B: The Lost City ---
p3b_paras = [
    "About two thousand years ago, the city of Baia was like the Las Vegas of the Roman Empire. As it was conveniently located just about thirty kilometers from Naples on the west coast of Italy, wealthy people in Rome visited the city and enjoyed parties, hot springs, and the warm climate. Famous poets, speakers, and experts on nature also had their houses near the bay or public baths to restore their energy. Baia has been known as a hot spring resort since ancient times, and its name remains in history. Even Emperor Hadrian spent his last years in Baia.",
    "Baia had a volcano and hot springs, which attracted visitors and made the city popular and successful. However, this volcano caused the city's collapse eventually. As is common in areas with volcanoes, the surface of the land rose and sank over many centuries. This caused more and more parts of the land to sink underground gradually. Over the past two thousand years, many parts of Baia have sunk, and about half of the city's structures are now underwater.",
    "It was not until the 1940s that this underwater part of the city began attracting attention. An Italian military pilot discovered mysterious structures under the water in the bay while flying low. Walls and roads in the water were seen clearly in the picture he took. However, investigation in the water only began after scuba devices were advanced enough. Later investigations revealed a room filled with large sculptures, and since the early 2000s, the part of the city that sank into the sea has been managed as a protected marine area.",
    "Currently, tourists can experience this underwater part of the city in various ways. Divers can explore the ancient Roman city in the water with guides. When the ocean is calm, visitors can see the structures in the water through the glass bottom of boats. In addition to the underwater sites, some ruins on land, such as dome-shaped public baths, can be visited on foot. Visiting Baia offers a rare chance to experience both ancient Roman history and the beauty of the sea in one place."
]

p3b_trans = [
    "約2000年前、バイアの町はローマ帝国のラスベガスのような存在だった。イタリア西海岸のナポリからわずか約30キロという便利な場所にあったため、ローマの裕福な人々がこの町を訪れ、パーティーや温泉、温暖な気候を楽しんだ。有名な詩人、弁論家、自然の専門家たちも、英気を養うために湾や公衆浴場の近くに家を持っていた。バイアは古代から温泉リゾートとして知られ、その名は歴史に残っている。皇帝ハドリアヌスでさえ、晩年をバイアで過ごしたほどである。",
    "バイアには火山と温泉があり、それが訪問者を引きつけ、町を人気のある繁栄した場所にした。しかし、この火山が最終的には町の崩壊を引き起こした。火山のある地域ではよくあることだが、土地の表面は何世紀にもわたって隆起と沈降を繰り返した。これにより、土地のますます多くの部分が徐々に地中に沈んでいった。過去2000年の間にバイアの多くの部分が沈み、現在では町の建造物の約半分が水中にある。",
    "この町の水中部分が注目を集め始めたのは、1940年代になってからのことだった。イタリア軍のパイロットが低空飛行中に、湾の水中に謎の構造物を発見したのだ。彼が撮影した写真には、水中の壁や道路がはっきりと写っていた。しかし、水中での調査は、スキューバ装備が十分に進歩してから初めて始まった。その後の調査で大きな彫刻で満たされた部屋が発見され、2000年代初頭以降、海に沈んだ町の部分は保護海域として管理されている。",
    "現在、観光客はこの町の水中部分をさまざまな方法で体験できる。ダイバーはガイドと一緒に水中の古代ローマ都市を探検できる。海が穏やかなときは、訪問者は船のガラス底を通して水中の構造物を見ることができる。水中の遺跡に加えて、ドーム型の公衆浴場など、陸上に残るいくつかの遺跡も徒歩で訪れることができる。バイアを訪れることは、古代ローマの歴史と海の美しさの両方を一つの場所で体験できる貴重な機会を提供してくれる。"
]

p3b_pairs = [
    ["About two thousand years ago, the city of Baia was like the Las Vegas of the Roman Empire.",
     "約2000年前、バイアの町はローマ帝国のラスベガスのような存在だった。"],
    ["As it was conveniently located just about thirty kilometers from Naples on the west coast of Italy, wealthy people in Rome visited the city and enjoyed parties, hot springs, and the warm climate.",
     "イタリア西海岸のナポリからわずか約30キロという便利な場所にあったため、ローマの裕福な人々がこの町を訪れ、パーティーや温泉、温暖な気候を楽しんだ。"],
    ["Famous poets, speakers, and experts on nature also had their houses near the bay or public baths to restore their energy.",
     "有名な詩人、弁論家、自然の専門家たちも、英気を養うために湾や公衆浴場の近くに家を持っていた。"],
    ["Baia has been known as a hot spring resort since ancient times, and its name remains in history.",
     "バイアは古代から温泉リゾートとして知られ、その名は歴史に残っている。"],
    ["Even Emperor Hadrian spent his last years in Baia.",
     "皇帝ハドリアヌスでさえ、晩年をバイアで過ごしたほどである。"],
    ["Baia had a volcano and hot springs, which attracted visitors and made the city popular and successful.",
     "バイアには火山と温泉があり、それが訪問者を引きつけ、町を人気のある繁栄した場所にした。"],
    ["However, this volcano caused the city's collapse eventually.",
     "しかし、この火山が最終的には町の崩壊を引き起こした。"],
    ["As is common in areas with volcanoes, the surface of the land rose and sank over many centuries.",
     "火山のある地域ではよくあることだが、土地の表面は何世紀にもわたって隆起と沈降を繰り返した。"],
    ["This caused more and more parts of the land to sink underground gradually.",
     "これにより、土地のますます多くの部分が徐々に地中に沈んでいった。"],
    ["Over the past two thousand years, many parts of Baia have sunk, and about half of the city's structures are now underwater.",
     "過去2000年の間にバイアの多くの部分が沈み、現在では町の建造物の約半分が水中にある。"],
    ["It was not until the 1940s that this underwater part of the city began attracting attention.",
     "この町の水中部分が注目を集め始めたのは、1940年代になってからのことだった。"],
    ["An Italian military pilot discovered mysterious structures under the water in the bay while flying low.",
     "イタリア軍のパイロットが低空飛行中に、湾の水中に謎の構造物を発見したのだ。"],
    ["Walls and roads in the water were seen clearly in the picture he took.",
     "彼が撮影した写真には、水中の壁や道路がはっきりと写っていた。"],
    ["However, investigation in the water only began after scuba devices were advanced enough.",
     "しかし、水中での調査は、スキューバ装備が十分に進歩してから初めて始まった。"],
    ["Later investigations revealed a room filled with large sculptures, and since the early 2000s, the part of the city that sank into the sea has been managed as a protected marine area.",
     "その後の調査で大きな彫刻で満たされた部屋が発見され、2000年代初頭以降、海に沈んだ町の部分は保護海域として管理されている。"],
    ["Currently, tourists can experience this underwater part of the city in various ways.",
     "現在、観光客はこの町の水中部分をさまざまな方法で体験できる。"],
    ["Divers can explore the ancient Roman city in the water with guides.",
     "ダイバーはガイドと一緒に水中の古代ローマ都市を探検できる。"],
    ["When the ocean is calm, visitors can see the structures in the water through the glass bottom of boats.",
     "海が穏やかなときは、訪問者は船のガラス底を通して水中の構造物を見ることができる。"],
    ["In addition to the underwater sites, some ruins on land, such as dome-shaped public baths, can be visited on foot.",
     "水中の遺跡に加えて、ドーム型の公衆浴場など、陸上に残るいくつかの遺跡も徒歩で訪れることができる。"],
    ["Visiting Baia offers a rare chance to experience both ancient Roman history and the beauty of the sea in one place.",
     "バイアを訪れることは、古代ローマの歴史と海の美しさの両方を一つの場所で体験できる貴重な機会を提供してくれる。"]
]

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Inquiry about the factory",
            "format": "email",
            "meta": {
                "from": "Jessica Jenkins <jjenkins@riverstonehigh.edu>",
                "to": "James White <jwhite@clearplastindustries.com>",
                "date": "April 10",
                "subject": "Inquiry about the factory"
            },
            "paragraphs": p3a_paras,
            "translations": p3a_trans,
            "sentencePairs": p3a_pairs,
            "questions": [
                {
                    "number": 24,
                    "question": "Why is Jessica Jenkins contacting James White?",
                    "choices": [
                        "To learn more about the history of the factory.",
                        "To request free plastic bottles for a school project.",
                        "To ask about the work experience for students at his factory.",
                        "To explain why her student hopes to go to his factory."
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "工場の歴史について学ぶため→本文にない",
                        "学校のプロジェクト用に無料のペットボトルを依頼するため→本文にない",
                        "工場での生徒向け職業体験について尋ねるため→職業体験ではなく見学ツアーの話",
                        "生徒が工場に行きたい理由を説明するため→正解。💡 第1段落で生徒の強い興味と見学希望の経緯を説明している"
                    ]
                },
                {
                    "number": 25,
                    "question": "Jessica asks whether her student can take a factory tour on Friday because",
                    "choices": [
                        "classes finish later on other days of the week.",
                        "she can take him to the factory after her class.",
                        "his transportation options are better on that day.",
                        "the factory runs exclusive tours every Friday."
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "他の曜日は授業がもっと遅く終わるから→正解。💡 ends at 2:00 p.m. on Fridays, which is earlier than on other days の言い換え",
                        "彼女が授業後に工場へ連れて行けるから→生徒は一人で（by himself）行く",
                        "その日は交通手段の選択肢が良いから→学校から徒歩で行ける話で、曜日による交通の違いはない",
                        "工場が毎週金曜に限定ツアーを実施しているから→exclusive（限定）とは書かれていない"
                    ]
                },
                {
                    "number": 26,
                    "question": "What does Jessica want James to do?",
                    "choices": [
                        "Provide details on special clothing needed for the visit in advance.",
                        "Inform her if the student should submit a written form before visiting.",
                        "Let her know when a Friday tour is possible and what to bring.",
                        "Suggest bringing a school camera for the student on the tour."
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "訪問に必要な特別な服装の詳細を事前に提供する→服装の話は本文にない",
                        "訪問前に書面の提出が必要かどうか知らせる→本文にない",
                        "金曜のツアーが可能な日時と持ち物を知らせる→正解。💡 an available date and time for a tour on a Friday ＋ what he should bring or prepare の言い換え",
                        "ツアーに学校のカメラを持参するよう提案する→撮影の可否を尋ねているだけ"
                    ]
                }
            ]
        },
        {
            "label": "B",
            "title": "The Lost City",
            "paragraphs": p3b_paras,
            "translations": p3b_trans,
            "sentencePairs": p3b_pairs,
            "questions": [
                {
                    "number": 27,
                    "question": "Why did many wealthy Romans visit Baia?",
                    "choices": [
                        "To relax in the warm climate, take part in parties, and recharge their energy.",
                        "To attend the meetings on nature that were held regularly near the bay.",
                        "To talk with experts and scholars who visited Baia to share ideas.",
                        "To study poetry from world-famous poets and join poetry contests."
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "温暖な気候でくつろぎ、パーティーに参加し、英気を養うため→正解。💡 enjoyed parties, hot springs, and the warm climate ＋ restore their energy の言い換え",
                        "湾の近くで定期的に開かれる自然に関する会合に出席するため→本文にない",
                        "アイデアを共有しにバイアを訪れた専門家や学者と話すため→本文にない",
                        "世界的に有名な詩人から詩を学び、詩のコンテストに参加するため→本文にない"
                    ]
                },
                {
                    "number": 28,
                    "question": "The gradual movement of the ground in Baia",
                    "choices": [
                        "allowed new volcanoes to form in the surrounding area.",
                        "made it impossible to successfully farm in the area.",
                        "led parts of the city to slowly sink beneath the water.",
                        "created more hot springs that attracted new tourists."
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "周辺地域に新しい火山が形成されることを可能にした→本文にない",
                        "その地域での農業を不可能にした→本文にない",
                        "町の一部が徐々に水面下に沈む結果となった→正解。💡 caused more and more parts of the land to sink underground gradually の言い換え",
                        "新たな観光客を引きつける温泉をさらに作り出した→本文にない"
                    ]
                },
                {
                    "number": 29,
                    "question": "A part of the city of Baia, which had disappeared underwater, was discovered",
                    "choices": [
                        "by a group of history experts who noticed large sculptures near the bay.",
                        "by some children who were painting pictures of the protected marine area.",
                        "through exploration by scuba divers who were searching for ancient ships.",
                        "through a photo taken by a pilot who was flying over the bay."
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "湾の近くで大きな彫刻に気づいた歴史専門家の一団によって→彫刻は後の調査で発見されたもの",
                        "保護海域の絵を描いていた子どもたちによって→本文にない",
                        "古代の船を探していたスキューバダイバーの探索によって→水中調査はスキューバ装備の進歩後に始まった",
                        "湾の上空を飛んでいたパイロットが撮った写真によって→正解。💡 An Italian military pilot discovered ... while flying low ＋ the picture he took"
                    ]
                },
                {
                    "number": 30,
                    "question": "One way tourists can see the ancient city of Baia is by",
                    "choices": [
                        "diving freely in the area without a guide to search for the ruins.",
                        "looking at it from the sea through special glass on a tour boat.",
                        "visiting the newly built history museum in Rome on a guided tour.",
                        "joining a tour that shows both the city ruins and the structure museum."
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "ガイドなしでその地域を自由に潜って遺跡を探す→ダイバーはガイド付き（with guides）",
                        "ツアーボートの特殊なガラス越しに海から眺める→正解。💡 see the structures in the water through the glass bottom of boats の言い換え",
                        "ローマに新設された歴史博物館をガイド付きで訪問する→本文にない",
                        "町の遺跡と構造物博物館の両方を見せるツアーに参加する→本文にない"
                    ]
                },
                {
                    "number": 31,
                    "question": "Which of the following statements is true?",
                    "choices": [
                        "The area where Baia sank gained protection after it was discovered.",
                        "Baia was so crowded that Emperor Hadrian was unable to stay there.",
                        "The cool waters of lakes and rivers attracted Romans to Baia in summer.",
                        "Many parts of Baia have been slowly sinking since the 1940s."
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "バイアが沈んだ地域は発見後に保護されるようになった→正解。💡 1940年代の発見の後、since the early 2000s ... managed as a protected marine area",
                        "バイアは混雑しすぎてハドリアヌス帝は滞在できなかった→晩年を過ごした（spent his last years）ので逆",
                        "湖や川の冷たい水が夏のローマ人をバイアに引きつけた→魅力は温泉と温暖な気候",
                        "バイアの多くの部分は1940年代以降に沈み始めた→過去2000年にわたって沈んできた"
                    ]
                }
            ]
        }
    ]
}

# ============================================================
# 保存
# ============================================================

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

data["sections"] = [section1, section2, section3]

# sentencePairs 整合性チェック
errors = []
for sec in data["sections"]:
    for p in sec.get("passages", []):
        text = " ".join(p["paragraphs"])
        for pair in p["sentencePairs"]:
            if pair[0] not in text:
                errors.append(f"NOT FOUND in '{p['title']}': {pair[0][:60]}")

if errors:
    print("⚠ sentencePairs エラー:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ sections 保存完了: {DATA_PATH}")
print(f"  vocabulary: {len(data['vocabulary'])}語")
for s in data["sections"]:
    nq = len(s.get("questions", [])) + sum(len(p["questions"]) for p in s.get("passages", []))
    print(f"  {s['name']} ({s['type']}): {nq}問")
