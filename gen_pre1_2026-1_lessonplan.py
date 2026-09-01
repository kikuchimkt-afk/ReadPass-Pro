# -*- coding: utf-8 -*-
"""Add five 2025-format focus points to Grade Pre-1 2026-1."""

import json
import os
import sys


sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "pre-grade1", "2026-1", "data.json")

if not os.path.exists(DATA_PATH):
    raise SystemExit("data.json is missing; run gen_pre1_2026-1.py first")

with open(DATA_PATH, encoding="utf-8") as handle:
    data = json.load(handle)

focus_points = [
    {
        "id": "fp1",
        "title": "as expected...However, while...（予想と調査結果のずれ）",
        "subtitle": "Contrasting a Stereotype with Research Findings",
        "explanation": (
            "大問2A「Birth Order」は、出生順位について広く知られたイメージを紹介したあと、"
            "実証研究で得られた結果を対比しています。as expected は予想と一致した点を示しますが、"
            "However と while が直後の反対方向の結果を導きます。設問では、個々の違いがあっても"
            "every birth position で差が extremely slight だったことを読み取り、研究者の結論を選びます。"
        ),
        "sourceQuote": "However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype.",
        "sourceLocation": "Part 2A「Birth Order」第2段落",
        "examples": [
            {
                "en": "While firstborns were, as expected, found to be more responsible, they tended to be less anxious.",
                "ja": "第一子は予想どおり責任感が強いと分かった一方、不安はむしろ少ない傾向がありました。",
                "note": "while が同じ調査内の対照を示し、前半だけで判断してはいけないことを知らせます。",
            },
            {
                "en": "The differences for every birth position were extremely slight.",
                "ja": "どの出生順位についても、その違いはきわめてわずかでした。",
                "note": "extremely slight が Q20 の are mostly meaningless を支える中心表現です。",
            },
            {
                "en": "It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development.",
                "ja": "したがって、多くの人が出生順位による性格への影響だと考えるものは、実際には一時的な発達段階にすぎないようです。",
                "note": "what A take to be B＝「AがBだと考えるもの」。therefore 以下が本文全体の結論です。",
            },
        ],
        "practicePassage": {
            "en": (
                "[出典: Birth Order]\n"
                "Extensive research has been conducted on birth order. One notable study, for example, examined thousands of teenagers and found that it did lead to some measurable differences. Eldest siblings, for instance, differed from others in terms of things like responsibility and anxiety. However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype. In addition to such contradictions, the differences for every birth position were extremely slight. According to the researchers, associations between birth order and a person's character are mostly meaningless. As children grow, there are obvious differences in everything from maturity to rebelliousness. Parents often observe that younger children have less self-control and disobey them more than older children. However, it is also true that this tends to fade with time. It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development their children are going through. Personality, experts tell us, is determined more by things like genetics and one's living environment than it is by the order in which children were born."
            ),
            "ja": (
                "出生順位については広範な研究が行われてきました。たとえば、ある注目すべき研究では数千人の10代の若者を調べ、出生順位によって測定可能な違いがいくつか確かに生じることが分かりました。たとえば第一子は、責任感や不安などの点でほかのきょうだいと異なっていました。しかし、第一子は予想どおり責任感が強いと分かった一方、不安はむしろ少ない傾向があり、これは固定観念に合いませんでした。こうした矛盾に加え、どの出生順位についても差はきわめてわずかでした。研究者によれば、出生順位と人の性格との関連はほとんど意味がありません。子どもが成長するにつれて、成熟度から反抗性まで、さまざまな面に明らかな違いが見られます。親はしばしば、年下の子どもは年上の子どもより自制心が弱く、親に従わないと感じます。しかし、その違いは時間とともに薄れる傾向があります。したがって、多くの人が出生順位による性格への影響だと考えるものは、実際には子どもが通過している一時的な発達段階にすぎないようです。専門家によれば、性格を決めるのは出生順位よりも、遺伝や生活環境などの要因です。"
            ),
            "audioFile": "audio/practice_pp1.mp3",
        },
        "practiceQuestions": [
            {
                "q": "as expected と which did not fit the stereotype は、それぞれ何を指しますか？",
                "a": "責任感が強い点は予想どおりですが、不安が少ない点は『第一子は不安が強い』という固定観念に反します。",
            },
            {
                "q": "Q20で are mostly meaningless を選ぶ直接の根拠は何ですか？",
                "a": "the differences for every birth position were extremely slight（どの出生順位でも差はきわめて小さかった）です。",
            },
            {
                "q": "did lead to の did にはどのような働きがありますか？",
                "a": "lead to を強調し、『確かにいくつかの違いは生じた』と認めたうえで、その違いの小ささへ話を進めます。",
            },
            {
                "q": "本文が最終的に出生順位より重視している要因を2つ答えてください。",
                "a": "遺伝（genetics）と生活環境（one's living environment）です。",
            },
        ],
        "highlightPatterns": [
            "while firstborns were, as expected, found to be more responsible",
            "the differences for every birth position were extremely slight",
        ],
        "highlightColor": "#FF6B6B",
        "highlightLabel": "予想と研究結果",
    },
    {
        "id": "fp2",
        "title": "When that happens...So, it is turning to technology instead（将来予測から代替策へ）",
        "subtitle": "From a Future Threat to a Technological Alternative",
        "explanation": (
            "大問2B「Digital Nations」は、海面上昇による国土喪失の予測から、移住、土地のかさ上げ、"
            "デジタル国家という複数の対応策へ展開します。When that happens は将来の条件を受け、"
            "So と instead は物理的対策だけでは長期的に不十分かもしれないため別の手段へ移る合図です。"
            "最終段落では Tuvalu だけでなく同様の島国にも利益が及ぶため、not only benefit Tuvalu が成立します。"
        ),
        "sourceQuote": "However, the government knows these measures may be useless in the long term. So, it ( 23 ).",
        "sourceLocation": "Part 2B「Digital Nations」第2〜3段落",
        "examples": [
            {
                "en": "When that happens, the only option for Tuvaluans will be to move elsewhere.",
                "ja": "そうなったとき、ツバルの人々に残る唯一の選択肢は別の場所へ移ることになります。",
                "note": "When that happens の that は、ツバルで暮らせなくなるという直前の予測を指します。",
            },
            {
                "en": "However, the government knows these measures may be useless in the long term.",
                "ja": "しかし政府は、こうした対策が長期的には役に立たない可能性を理解しています。",
                "note": "these measures は防潮壁と高くした土地。However が次の代替策を必要とする理由です。",
            },
            {
                "en": "This could also help to ensure the survival of other island nations facing similar threats from the sea.",
                "ja": "これは、海から同様の脅威に直面するほかの島国の存続を確かなものにする助けにもなり得ます。",
                "note": "also と other island nations が Q24 の will not only benefit Tuvalu の根拠です。",
            },
        ],
        "practicePassage": {
            "en": (
                "[出典: Digital Nations]\n"
                "Sea barriers have been built, and work is underway to create an area of raised land that will provide a habitable area for residents. However, the government knows these measures may be useless in the long term. So, it is turning to technology instead. A few years ago, it set up the Future Now Project. Part of this project involves creating a virtual reconstruction of the nation. Along with preserving geographical features, the project aims to create a digital record of Tuvalu's people and customs. Some critics claim the resources required for the project could be better used to tackle climate change. In response, Tuvalu's government points out that the project will not only benefit Tuvalu. The current international treaty states that sovereign nations must have a \"defined territory\" and a \"permanent population.\" Tuvalu's government hopes to pioneer a new form of statehood that allows it to continue to exist by meeting these criteria in a virtual form. This could also help to ensure the survival of other island nations facing similar threats from the sea."
            ),
            "ja": (
                "防潮壁が建設され、住民が暮らせる区域となる、かさ上げされた土地を造る工事も進行中です。しかし政府は、こうした対策が長期的には役に立たない可能性を理解しています。そこで政府は代わりに技術へ目を向けています。数年前、政府はFuture Now Projectを立ち上げました。この計画の一部には、国を仮想復元する取り組みが含まれます。地理的特徴を保存するだけでなく、この計画はツバルの人々と慣習をデジタル記録として残すことを目指しています。批判する人の中には、必要な資源を気候変動対策に使うほうがよいと主張する人もいます。これに対し政府は、この計画はツバルだけに利益をもたらすのではないと指摘します。現行の国際条約では、主権国家は「明確に定められた領土」と「定住人口」を持たなければなりません。ツバル政府は、これらの条件を仮想的な形で満たして国として存続できる、新たな国家のあり方を切り開こうとしています。これは、同様の海からの脅威に直面するほかの島国の存続にも役立つ可能性があります。"
            ),
            "audioFile": "audio/practice_pp2.mp3",
        },
        "practiceQuestions": [
            {
                "q": "Q23で is turning to technology instead が入る論理を説明してください。",
                "a": "防潮壁や土地のかさ上げは長期的には無駄かもしれず、その直後に国の仮想復元計画が説明されるためです。",
            },
            {
                "q": "these measures が指す2つの対策は何ですか？",
                "a": "防潮壁の建設と、住民が暮らせるよう土地をかさ上げする工事です。",
            },
            {
                "q": "Along with preserving geographical features の along with は何を表しますか？",
                "a": "『地理的特徴を保存することに加えて』という追加を表し、人々と慣習の記録も目的だと示します。",
            },
            {
                "q": "Tuvalu が virtual statehood を目指す理由を一文でまとめてください。",
                "a": "国土を失っても、明確に定められた領土と定住人口という国家の条件を仮想的な形で満たし、国として存続するためです。",
            },
        ],
        "highlightPatterns": [
            "these measures may be useless in the long term",
            "creating a virtual reconstruction of the nation",
        ],
        "highlightColor": "#4ECDC4",
        "highlightLabel": "物理的対策と代替策",
    },
    {
        "id": "fp3",
        "title": "not only allowed...but also...（発展を生んだ因果関係）",
        "subtitle": "Cause and Effect in the Growth of Uruk",
        "explanation": (
            "大問3A「Uruk」では、灌漑技術の進歩が農業効率を高め、人口を支え、余剰生産物を生み、"
            "交易につながったという因果の鎖を追います。not only A but also B は二つの効果を並列し、"
            "which could then be traded が余剰生産物の次の役割を説明します。第2段落では楔形文字の"
            "発達が会計・行政を助け、複雑化する都市の統治を可能にした点が Q26 の根拠です。"
        ),
        "sourceQuote": "These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded.",
        "sourceLocation": "Part 3A「Uruk」第1〜2段落",
        "examples": [
            {
                "en": "These advances not only allowed Uruk to support a growing population but also to create a surplus.",
                "ja": "こうした進歩により、ウルクは増加する人口を支えられただけでなく、余剰生産物も生み出せました。",
                "note": "allow A to V と not only A but also B が、技術進歩の二つの効果を整理します。",
            },
            {
                "en": "The writing system gradually became more sophisticated and was used for accounting and general administrative matters.",
                "ja": "その文字体系は徐々に高度化し、会計や一般的な行政事務に使われるようになりました。",
                "note": "became more sophisticated と was used for が、文字の発達と用途を順に示します。",
            },
            {
                "en": "This helped facilitate the governance of the increasingly complex city.",
                "ja": "これは、ますます複雑化する都市の統治を円滑にする助けとなりました。",
                "note": "This は直前の会計・行政利用を指し、Q26 の helped manage administration に言い換えられます。",
            },
        ],
        "practicePassage": {
            "en": (
                "[出典: Uruk]\n"
                "The ancient settlement of Uruk was located in a fertile delta between the Tigris and Euphrates rivers in the region of Sumer, in what is now southern Iraq. Uruk began life as a village. However, toward the end of the fourth millennium BC, it had developed to such an extent that some historians consider it the world's first city. Behind this remarkable growth were several factors, including technological advancements that increased agricultural efficiency, such as the construction of irrigation canals to funnel water to fields and orchards. These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded. Expansion continued, and by the third millennium BC, Uruk was thriving as a Sumerian cultural and religious center, a military power, and the hub of a trade network. As Uruk grew, it helped shape the political and cultural landscape of the Sumer region, influencing other cities that developed around the same period. Various other developments helped Uruk evolve into the sophisticated city it became, including its early use of cuneiform script. The script was mainly written on clay tablets, many of which survive to this day. In its early form, it was relatively simple, with pictures representing goods, but it allowed for rudimentary recordkeeping. The writing system gradually became more sophisticated and was used for accounting and general administrative matters, which helped facilitate the governance of the increasingly complex city. Over time, the script was used in the Sumer region to keep records in fields such as economics, politics, and religion."
            ),
            "ja": (
                "古代の集落ウルクは、現在のイラク南部にあたるシュメール地方の、チグリス川とユーフラテス川にはさまれた肥沃な三角州に位置していました。ウルクは村として歴史を始めました。しかし紀元前4千年紀の終わりごろには、一部の歴史家が世界最初の都市とみなすほど発展していました。この著しい成長の背景には、農業効率を高める技術の進歩など、いくつもの要因がありました。たとえば、畑や果樹園へ水を引く灌漑用水路の建設です。こうした進歩により、ウルクは増加する人口を支えられただけでなく、交易できる余剰生産物も生み出せました。拡大は続き、紀元前3千年紀までにウルクは、シュメールの文化・宗教の中心、軍事大国、交易網の中枢として繁栄していました。ウルクは成長するにつれてシュメール地方の政治的・文化的な姿を形作り、同時期に発展したほかの都市にも影響を与えました。ウルクを洗練された都市へ発展させた要素には、くさび形文字の早期利用もありました。この文字は主に粘土板に記され、その多くが今日まで残っています。初期の形は品物を表す絵から成る比較的単純なものでしたが、基本的な記録管理を可能にしました。やがて文字体系は複雑になり、会計や一般行政に用いられ、ますます複雑化する都市の統治を円滑にしました。その後、シュメール地方では経済・政治・宗教などの記録にも使われました。"
            ),
            "audioFile": "audio/practice_pp3.mp3",
        },
        "practiceQuestions": [
            {
                "q": "Q25で ability to produce surplus food が rapid transformation につながる理由は何ですか？",
                "a": "余剰生産物を交易でき、人口増加も支えられたため、村から都市への急速な発展を後押ししたからです。",
            },
            {
                "q": "which could then be traded の which は何を指しますか？",
                "a": "a surplus（余剰生産物）を指します。",
            },
            {
                "q": "including と such as の役割の違いを説明してください。",
                "a": "including は成長要因の一つとして技術進歩を加え、such as はその具体例として灌漑用水路を示します。",
            },
            {
                "q": "楔形文字が都市統治を助けた流れを要約してください。",
                "a": "簡単な物品記録から始まり、会計・行政に使える高度な文字体系へ発達し、複雑な都市の管理を支えました。",
            },
        ],
        "highlightPatterns": [
            "not only allowed Uruk to support a growing population but also to create a surplus",
            "helped facilitate the governance of the increasingly complex city",
        ],
        "highlightColor": "#45B7D1",
        "highlightLabel": "技術・余剰・統治",
    },
    {
        "id": "fp4",
        "title": "one promising approach...However...（可能性と副作用の評価）",
        "subtitle": "Balancing Scientific Promise and Unintended Outcomes",
        "explanation": (
            "大問3B「Animal Uplift」は、動物の知能を高める技術の可能性を示したあと、研究の限界、"
            "身体的な副作用、心理的・倫理的問題を段階的に検討します。one promising approach は期待を示しますが、"
            "This research is preliminary, however が結論を限定します。魚の実験では大きな脳と高い認知能力だけでなく、"
            "消化器官の縮小と繁殖数の減少まで追うことで、unintended outcomes の具体例を示しています。"
        ),
        "sourceQuote": "As this experiment indicates, trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations.",
        "sourceLocation": "Part 3B「Animal Uplift」第1〜2段落",
        "examples": [
            {
                "en": "This research is preliminary, however, and intelligence depends on a multitude of genes.",
                "ja": "しかし、この研究は予備的な段階であり、知能は多数の遺伝子に左右されます。",
                "note": "however が有望な実験結果を認めつつ、一般化できない限界へ転換します。",
            },
            {
                "en": "The young of the larger-brained fish tended to have even bigger brains, and the babies' performance on cognitive tests was superior.",
                "ja": "脳の大きな魚から生まれた稚魚はさらに大きな脳を持つ傾向があり、その稚魚は認知テストでより優れた成績を示しました。",
                "note": "tended to は傾向として慎重に述べる一方、was superior はテスト結果の比較を明確に述べます。",
            },
            {
                "en": "Trying to boost intelligence may disrupt other physical attributes.",
                "ja": "知能を高めようとすると、ほかの身体的特徴を損なう可能性があります。",
                "note": "may disrupt が断定を避けながら、Q29 の interferes with other aspects of biology を支えます。",
            },
        ],
        "practicePassage": {
            "en": (
                "[出典: Animal Uplift]\n"
                "While the concept of artificially increasing animal intelligence through technology once seemed like science fiction, recent advances suggest it may be achievable. One promising approach for doing so is genetic manipulation. For instance, in 2014, researchers discovered that a human gene called FOXP2 was related to acquiring language skills in humans. When mice were genetically altered to produce it, they were able to learn a route through a maze much more rapidly than their unmodified counterparts, indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence. This research is preliminary, however, and intelligence depends on a multitude of genes, so significant technical and ethical hurdles must be overcome before such advancements can be responsibly applied. One experiment compared fish with larger brains that were bred together to fish with smaller brains that were bred together. The young of the larger-brained fish tended to have even bigger brains, and the babies' performance on cognitive tests was superior to that of fish with smaller brains. However, the researchers also observed that these fish produced young that had smaller digestive systems, and this in turn seems to have led them to produce fewer offspring. This is likely due to the fact that larger brains require substantially more energy. As this experiment indicates, trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations."
            ),
            "ja": (
                "技術によって動物の知能を人為的に高めるという発想は、かつてはSFのように思われましたが、最近の進歩は実現可能かもしれないことを示しています。そのための有望な方法の一つが遺伝子操作です。2014年、研究者たちはFOXP2と呼ばれるヒトの遺伝子が言語能力の獲得に関係していることを発見しました。マウスがFOXP2を発現するよう遺伝的に改変されると、改変されていないマウスよりはるかに速く迷路の経路を覚えられました。これは、知能に欠かせない要素である記憶力が大幅に高まったことを示します。ただし、この研究は予備段階であり、知能は多数の遺伝子に左右されるため、責任ある応用には技術上・倫理上の大きな障壁があります。ある実験では、脳の大きな魚どうしを交配したものと、脳の小さな魚どうしを交配したものを比較しました。脳の大きな魚から生まれた稚魚はさらに大きな脳を持つ傾向があり、それらの稚魚の認知テストの成績は、脳の小さな魚の稚魚より優れていました。しかし研究者は、これらの魚から生まれた子は消化器官が小さく、それが今度は子の数が少なくなることにつながったようだとも観察しました。これは、より大きな脳がかなり多くのエネルギーを必要とするためだと考えられます。この実験が示すように、知能を高めようとするとほかの身体的特徴を損ない、個々の動物を越えて集団全体に及ぶ結果を招く可能性があります。"
            ),
            "audioFile": "audio/practice_pp4.mp3",
        },
        "practiceQuestions": [
            {
                "q": "魚の実験で確認された利点と不利益を一つずつ答えてください。",
                "a": "利点は認知テストの成績向上、不利益は消化器官の縮小と、それに関連する子の数の減少です。",
            },
            {
                "q": "this in turn は何を受け、何につながりましたか？",
                "a": "消化器官が小さいことを受け、それが今度は産む子の数の減少につながったと述べています。",
            },
            {
                "q": "beyond the individual animals to entire populations の意味を説明してください。",
                "a": "影響が一匹の動物だけで終わらず、繁殖を通じて集団全体に広がり得るという意味です。",
            },
            {
                "q": "Q28で FOXP2 の実験を preliminary step と表す理由は何ですか？",
                "a": "記憶という知能の一要素には効果が見られましたが、知能は多数の遺伝子に依存し、研究も予備段階だからです。",
            },
        ],
        "highlightPatterns": [
            "This research is preliminary, however",
            "trying to boost intelligence may disrupt other physical attributes",
        ],
        "highlightColor": "#96CEB4",
        "highlightLabel": "期待と副作用",
    },
    {
        "id": "fp5",
        "title": "今回の重要なパラフレーズ",
        "subtitle": "Key Paraphrases in This Exam",
        "explanation": (
            "準1級の内容一致問題では、本文と選択肢が同じ語を繰り返すとは限りません。"
            "本文中の因果関係、程度、対象を保ったまま別の表現に置き換えられているかを確認します。"
            "特に may や tended to のような限定表現を、断定的な選択肢へ読み替えないことが重要です。"
        ),
        "sourceQuote": (
            "①create a surplus = produce more food than it needed\n"
            "②facilitate the governance = help manage administration\n"
            "③disrupt other physical attributes = interfere with other aspects of biology\n"
            "④impossible for the creature to give consent = animals cannot agree beforehand\n"
            "⑤use animals in increasing our own intelligence = increase our obligation to uplift them"
        ),
        "sourceLocation": "Part 3 全体",
        "examples": [
            {
                "en": "create a surplus → produce more food than it needed",
                "ja": "余剰を生み出す → 必要量を超える食料を生産する",
                "note": "surplus の定義を具体的な動作へ言い換えています。",
            },
            {
                "en": "facilitate the governance of the city → help manage the city's administration",
                "ja": "都市の統治を円滑にする → 都市の行政管理を助ける",
                "note": "facilitate＝help、governance＝administration の対応です。",
            },
            {
                "en": "withholding animal uplift is itself unethical → humans have an obligation to make the benefits available to animals",
                "ja": "動物の知能向上を差し控えること自体が非倫理的である → 人間にはその利益を動物も利用できるようにする義務がある",
                "note": "否定形の倫理判断を obligation という肯定形の義務へ変換しています。",
            },
        ],
        "practicePassage": {
            "en": (
                "[出典: Animal Uplift]\n"
                "George Dvorsky, chairperson of the Institute for Ethics and Emerging Technologies, however, argues that withholding animal uplift is itself unethical. Animals have long been sacrificed as test subjects during the creation of new surgical procedures or the development of medicines that have increased human life expectancy, and if humans artificially increase our own intelligence, animals will likely be sacrificed for that as well. According to Dvorsky, in light of increased awareness of animal rights and given the tremendous role that animals have played in improving human existence, withholding advances that could improve their intelligence would be just as unethical as withholding them from a group of humans who lack sufficient wealth to afford them."
            ),
            "ja": (
                "しかし、倫理・新興技術研究所の代表ジョージ・ドヴォルスキーは、動物の知能向上を差し控えること自体が非倫理的だと主張します。人間の寿命を延ばしてきた新しい手術法や医薬品の開発では、長い間、動物が実験対象として犠牲にされてきました。そして、人間が自分たちの知能を人工的に高めるなら、そのためにも動物が犠牲になる可能性が高いでしょう。ドヴォルスキーによれば、動物の権利に対する意識が高まり、動物が人間の暮らしの向上に果たしてきた大きな役割を考えれば、動物の知能を高め得る技術的進歩を利用させないことは、それを購入できるだけの富を持たない人間の集団に利用させないのと同じくらい非倫理的です。"
            ),
            "audioFile": "audio/practice_pp5.mp3",
        },
        "practiceQuestions": [
            {
                "q": "Dvorsky が withholding animal uplift is itself unethical と主張する理由は何ですか？",
                "a": "人間の医療や寿命向上のために動物が長く犠牲になってきた以上、動物の知能を高め得る進歩を動物に与えないことも非倫理的だと考えるからです。",
            },
            {
                "q": "in light of ... と given ... は、どの2つの根拠を示していますか？",
                "a": "動物の権利への意識が高まっていることと、動物が人間の生活向上に大きな役割を果たしてきたことです。",
            },
            {
                "q": "would be just as unethical as ... では、どの2つを同程度に非倫理的だと比べていますか？",
                "a": "知能向上の進歩を動物に与えないことと、費用を負担できない人間の集団に同じ進歩を与えないことです。",
            },
            {
                "q": "Q31で withholding ... is unethical から obligation を導く手順を説明してください。",
                "a": "人間が自らの知能を高める過程でも動物を利用・犠牲にするなら、人間には知能向上の恩恵を動物も利用できるようにする責務がいっそう強まる、と捉えます。",
            },
        ],
        "highlightPatterns": [
            "withholding animal uplift is itself unethical",
            "would be just as unethical as withholding them from a group of humans",
            "the tremendous role that animals have played in improving human existence",
        ],
        "highlightColor": "#f59e0b",
        "highlightLabel": "パラフレーズ",
    },
]

data["lessonPlan"] = {"focusPoints": focus_points}

with open(DATA_PATH, "w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=4)
    handle.write("\n")

print(f"Updated {DATA_PATH}")
print(f"  focus points: {len(focus_points)}")
