# -*- coding: utf-8 -*-
"""Generate 2026-1 Grade Pre-1 Part 3 (Q25-Q31).

This step intentionally requires an existing data.json so that Part 1 and Part 2
created by earlier steps are preserved.  It replaces the first existing Part 3,
or appends Part 3 when it is not present.
"""

import json
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")


DATA_PATH = (
    Path(__file__).resolve().parent
    / "data"
    / "pre-grade1"
    / "2026-1"
    / "data.json"
)


URUK_GROUPS = [
    [
        [
            "The ancient settlement of Uruk was located in a fertile delta between the Tigris and Euphrates rivers in the region of Sumer, in what is now southern Iraq.",
            "古代の集落ウルクは、現在のイラク南部にあたるシュメール地方の、チグリス川とユーフラテス川にはさまれた肥沃な三角州に位置していた。",
            "The ancient settlement of Uruk|古代の集落ウルクは||was located in a fertile delta|肥沃な三角州に位置していた||between the Tigris and Euphrates rivers|チグリス川とユーフラテス川の間の||in the region of Sumer,|シュメール地方にある||in what is now southern Iraq.|現在のイラク南部にあたる。",
            "was located",
        ],
        [
            "Uruk began life as a village.",
            "ウルクは村として歴史を始めた。",
            "Uruk began life|ウルクは歴史を始めた||as a village.|村として。",
            "began",
        ],
        [
            "However, toward the end of the fourth millennium BC, it had developed to such an extent that some historians consider it the world’s first city.",
            "しかし紀元前4千年紀の終わりごろには、ウルクは大きく発展し、一部の歴史家が世界最初の都市とみなすほどになっていた。",
            "However,|しかし、||toward the end of the fourth millennium BC,|紀元前4千年紀の終わりごろには、||it had developed to such an extent|それほどまでに発展していた||that some historians consider it|一部の歴史家がそれをみなすほどに||the world’s first city.|世界最初の都市と。",
            "had developed",
        ],
        [
            "Behind this remarkable growth were several factors, including technological advancements that increased agricultural efficiency, such as the construction of irrigation canals to funnel water to fields and orchards.",
            "この著しい成長の背景には、農業効率を高めた技術の進歩など、いくつかの要因があった。その一例が、畑や果樹園へ水を導くための灌漑用水路の建設である。",
            "Behind this remarkable growth|この著しい成長の背景には||were several factors,|いくつかの要因があった||including technological advancements|技術の進歩を含む||that increased agricultural efficiency,|農業効率を高めた||such as the construction of irrigation canals|たとえば灌漑用水路の建設のような||to funnel water to fields and orchards.|畑や果樹園へ水を導くための。",
            "were",
        ],
        [
            "These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded.",
            "こうした進歩によって、ウルクは増え続ける人口を支えられただけでなく、余剰生産物を生み出し、それを交易に回すこともできた。",
            "These advances|こうした進歩によって||not only allowed Uruk to support a growing population|ウルクは増え続ける人口を支えられただけでなく||but also to create a surplus,|余剰生産物を生み出すこともでき||which could then be traded.|それを交易に回すこともできた。",
            "allowed",
        ],
        [
            "Expansion continued, and by the third millennium BC, Uruk was thriving as a Sumerian cultural and religious center, a military power, and the hub of a trade network.",
            "拡大は続き、紀元前3千年紀までには、ウルクはシュメールの文化・宗教の中心地、軍事大国、そして交易網の要として繁栄していた。",
            "Expansion continued,|拡大は続き、||and by the third millennium BC,|紀元前3千年紀までには、||Uruk was thriving|ウルクは繁栄していた||as a Sumerian cultural and religious center,|シュメールの文化・宗教の中心地として||a military power,|軍事大国として||and the hub of a trade network.|そして交易網の要として。",
            "was thriving",
        ],
    ],
    [
        [
            "As Uruk grew, it helped shape the political and cultural landscape of the Sumer region, influencing other cities that developed around the same period.",
            "ウルクは成長するにつれて、シュメール地方の政治的・文化的な姿を形作り、同じ時期に発展したほかの都市にも影響を与えた。",
            "As Uruk grew,|ウルクは成長するにつれて、||it helped shape|形作る一助となった||the political and cultural landscape|政治的・文化的な姿を||of the Sumer region,|シュメール地方の||influencing other cities|ほかの都市にも影響を与えながら||that developed around the same period.|同じ時期に発展した。",
            "helped shape",
        ],
        [
            "Various other developments helped Uruk evolve into the sophisticated city it became, including its early use of cuneiform script.",
            "そのほかにもさまざまな発展が、ウルクが洗練された都市へ進化する助けとなった。その中には、くさび形文字を早くから使用したことも含まれていた。",
            "Various other developments|そのほかにもさまざまな発展が||helped Uruk evolve|ウルクが進化する助けとなった||into the sophisticated city it became,|実際にそうなった洗練された都市へ||including its early use|早くから使用したことを含めて||of cuneiform script.|くさび形文字を。",
            "helped",
        ],
        [
            "The script was mainly written on clay tablets, many of which survive to this day.",
            "その文字は主に粘土板に書かれ、その多くが今日まで残っている。",
            "The script was mainly written|その文字は主に書かれた||on clay tablets,|粘土板に||many of which survive|その多くが残っている||to this day.|今日まで。",
            "was mainly written",
        ],
        [
            "In its early form, it was relatively simple, with pictures representing goods, but it allowed for rudimentary recordkeeping.",
            "初期の形は比較的単純で、品物を表す絵から成っていたが、基本的な記録管理を可能にした。",
            "In its early form,|初期の形では、||it was relatively simple,|それは比較的単純で||with pictures representing goods,|品物を表す絵から成っていたが||but it allowed for|しかし可能にした||rudimentary recordkeeping.|基本的な記録管理を。",
            "was",
        ],
        [
            "The writing system gradually became more sophisticated and was used for accounting and general administrative matters, which helped facilitate the governance of the increasingly complex city.",
            "この文字体系は次第に複雑になり、会計や一般行政に使われるようになった。それによって、ますます複雑化する都市の統治が円滑になった。",
            "The writing system gradually became more sophisticated|この文字体系は次第に複雑になり||and was used|使われるようになった||for accounting and general administrative matters,|会計や一般行政に||which helped facilitate the governance|それによって統治が円滑になった||of the increasingly complex city.|ますます複雑化する都市の。",
            "became",
        ],
        [
            "Over time, the script was used in the Sumer region to keep records in fields such as economics, politics, and religion.",
            "やがて、その文字はシュメール地方で、経済・政治・宗教などの分野の記録を残すために使われた。",
            "Over time,|やがて、||the script was used|その文字は使われた||in the Sumer region|シュメール地方で||to keep records|記録を残すために||in fields such as economics, politics, and religion.|経済・政治・宗教などの分野の。",
            "was used",
        ],
    ],
    [
        [
            "However, Uruk’s dominant position was not to last forever.",
            "しかし、ウルクの支配的な地位が永遠に続くことはなかった。",
            "However,|しかし、||Uruk’s dominant position|ウルクの支配的な地位は||was not to last forever.|永遠に続くものではなかった。",
            "was not to last",
        ],
        [
            "Uruk had competed with neighboring Sumerian cities for hundreds of years, leaving them all vulnerable to forces from other regions.",
            "ウルクは近隣のシュメール諸都市と何百年も競い合っており、そのためそれらすべての都市が他地域の勢力に対して脆弱になっていた。",
            "Uruk had competed|ウルクは競い合っていた||with neighboring Sumerian cities|近隣のシュメール諸都市と||for hundreds of years,|何百年もの間||leaving them all vulnerable|そのすべてを脆弱な状態にして||to forces from other regions.|他地域の勢力に対して。",
            "had competed",
        ],
        [
            "In the latter half of the third millennium BC, the Akkadians conquered much of Sumer.",
            "紀元前3千年紀後半、アッカド人がシュメールの大部分を征服した。",
            "In the latter half|後半に||of the third millennium BC,|紀元前3千年紀の||the Akkadians conquered|アッカド人が征服した||much of Sumer.|シュメールの大部分を。",
            "conquered",
        ],
        [
            "Despite this conquest, Uruk’s religious districts were respected and protected, and after Akkadian rule came to an end, a renaissance of Sumerian culture occurred.",
            "この征服にもかかわらず、ウルクの宗教地区は尊重され、保護された。そしてアッカド人の支配が終わると、シュメール文化の復興が起こった。",
            "Despite this conquest,|この征服にもかかわらず、||Uruk’s religious districts|ウルクの宗教地区は||were respected and protected,|尊重され、保護された||and after Akkadian rule came to an end,|そしてアッカド人の支配が終わると||a renaissance of Sumerian culture occurred.|シュメール文化の復興が起こった。",
            "were respected",
        ],
        [
            "Although later conflicts and invasions meant that Uruk would not return to its earlier heights, it remained an important city for many centuries to come.",
            "その後の争いや侵略によってウルクがかつての隆盛を取り戻すことはなかったが、その後も何世紀にもわたって重要な都市であり続けた。",
            "Although later conflicts and invasions meant|その後の争いや侵略によって||that Uruk would not return|ウルクが戻ることはなかったが||to its earlier heights,|かつての隆盛へ||it remained an important city|重要な都市であり続けた||for many centuries to come.|その後も何世紀にもわたって。",
            "remained",
        ],
        [
            "Archaeological excavations have revealed an immense city wall, sculptures, artworks, large stone buildings decorated with mosaics, and numerous pyramid-like structures called ziggurats that were topped with temples—all of which point to the historical significance of Uruk.",
            "考古学的発掘によって、巨大な市壁、彫刻、美術品、モザイクで装飾された大きな石造建築、さらに神殿を頂くジッグラトと呼ばれる多数のピラミッド状建造物が明らかになっており、そのすべてがウルクの歴史的重要性を示している。",
            "Archaeological excavations have revealed|考古学的発掘によって明らかになっている||an immense city wall, sculptures, artworks,|巨大な市壁、彫刻、美術品、||large stone buildings decorated with mosaics,|モザイクで装飾された大きな石造建築、||and numerous pyramid-like structures called ziggurats|そしてジッグラトと呼ばれる多数のピラミッド状建造物が||that were topped with temples—all of which point to|神殿を頂き、そのすべてが示している||the historical significance of Uruk.|ウルクの歴史的重要性を。",
            "have revealed",
        ],
    ],
]


ANIMAL_UPLIFT_GROUPS = [
    [
        [
            "While the concept of artificially increasing animal intelligence through technology once seemed like science fiction, recent advances suggest it may be achievable.",
            "技術によって動物の知能を人為的に高めるという発想は、かつてはSFのように思われたが、最近の進歩はそれが実現可能かもしれないことを示している。",
            "While the concept|その発想は||of artificially increasing animal intelligence|動物の知能を人為的に高めるという||through technology|技術によって||once seemed like science fiction,|かつてはSFのように思われたが||recent advances suggest|最近の進歩は示している||it may be achievable.|それが実現可能かもしれないことを。",
            "suggest",
        ],
        [
            "One promising approach for doing so is genetic manipulation.",
            "そのための有望な方法の一つが遺伝子操作である。",
            "One promising approach|有望な方法の一つは||for doing so|そうするための||is genetic manipulation.|遺伝子操作である。",
            "is genetic manipulation",
        ],
        [
            "For instance, in 2014, researchers discovered that a human gene called FOXP2 was related to acquiring language skills in humans.",
            "たとえば2014年、研究者たちはFOXP2と呼ばれるヒトの遺伝子が、人間の言語能力の獲得に関係していることを発見した。",
            "For instance, in 2014,|たとえば2014年、||researchers discovered|研究者たちは発見した||that a human gene called FOXP2|FOXP2と呼ばれるヒトの遺伝子が||was related to acquiring language skills|言語能力の獲得に関係していることを||in humans.|人間における。",
            "discovered",
        ],
        [
            "When mice were genetically altered to produce it, they were able to learn a route through a maze much more rapidly than their unmodified counterparts, indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence.",
            "マウスがFOXP2を発現するよう遺伝的に改変されると、改変されていないマウスよりはるかに速く迷路の経路を覚えられた。このことは、その遺伝子が、知能に欠かせない要素である記憶力を大幅に高めたことを示している。",
            "When mice were genetically altered|マウスが遺伝的に改変されると||to produce it,|FOXP2を発現するように||they were able to learn a route|経路を覚えることができた||through a maze|迷路を通る||much more rapidly than their unmodified counterparts,|改変されていないマウスよりはるかに速く||indicating that the gene had significantly enhanced their memory,|その遺伝子が記憶力を大幅に高めたことを示しており||which is an essential component of intelligence.|それは知能に欠かせない要素である。",
            "were able",
        ],
        [
            "This research is preliminary, however, and intelligence depends on a multitude of genes, so significant technical and ethical hurdles must be overcome before such advancements can be responsibly applied.",
            "しかし、この研究はまだ予備段階であり、知能は多数の遺伝子に左右される。そのため、このような進歩を責任ある形で応用できるようになるまでには、技術上・倫理上の大きな障壁を克服しなければならない。",
            "This research is preliminary, however,|しかし、この研究はまだ予備段階であり||and intelligence depends|知能は左右される||on a multitude of genes,|多数の遺伝子に||so significant technical and ethical hurdles|そのため技術上・倫理上の大きな障壁を||must be overcome|克服しなければならない||before such advancements can be responsibly applied.|このような進歩を責任ある形で応用できるまでに。",
            "must be overcome",
        ],
    ],
    [
        [
            "An aspect of animal uplift that needs to be considered is the possibility of unintended outcomes.",
            "動物の知能向上について考慮すべき一面は、意図しない結果が生じる可能性である。",
            "An aspect of animal uplift|動物の知能向上の一面で||that needs to be considered|考慮すべきなのは||is the possibility|可能性である||of unintended outcomes.|意図しない結果が生じる。",
            "needs to be considered",
        ],
        [
            "One experiment compared fish with larger brains that were bred together to fish with smaller brains that were bred together.",
            "ある実験では、脳の大きな魚どうしを交配した群と、脳の小さな魚どうしを交配した群を比較した。",
            "One experiment compared|ある実験では比較した||fish with larger brains|脳の大きな魚を||that were bred together|互いに交配された||to fish with smaller brains|脳の小さな魚と||that were bred together.|互いに交配された。",
            "compared",
        ],
        [
            "The young of the larger-brained fish tended to have even bigger brains, and the babies’ performance on cognitive tests was superior to that of fish with smaller brains.",
            "脳の大きな魚の子はさらに大きな脳を持つ傾向があり、それらの稚魚の認知テストの成績は、脳の小さな魚の稚魚より優れていた。",
            "The young of the larger-brained fish|脳の大きな魚の子は||tended to have even bigger brains,|さらに大きな脳を持つ傾向があり||and the babies’ performance|そしてそれらの稚魚の成績は||on cognitive tests|認知テストでの||was superior to that|それより優れていた||of fish with smaller brains.|脳の小さな魚の稚魚より。",
            "tended",
        ],
        [
            "However, the researchers also observed that these fish produced young that had smaller digestive systems, and this in turn seems to have led them to produce fewer offspring.",
            "しかし研究者たちは、これらの魚が消化器官の小さい子を産むことも観察し、それが今度は子の数を減らしたとみられる。",
            "However, the researchers also observed|しかし研究者たちはさらに観察した||that these fish produced young|これらの魚が子を産むことを||that had smaller digestive systems,|より小さな消化器官を持つ||and this in turn seems to have led them|そしてそのことが今度は、それらの魚が||to produce fewer offspring.|より少ない子しか産まないことにつながったようだ。",
            "observed",
        ],
        [
            "This is likely due to the fact that larger brains require substantially more energy.",
            "これは、脳が大きいほどかなり多くのエネルギーを必要とするためだと考えられる。",
            "This is likely due to the fact|これはおそらく〜という事実による||that larger brains require|大きな脳ほど必要とする||substantially more energy.|はるかに多くのエネルギーを。",
            "is likely due",
        ],
        [
            "As this experiment indicates, trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations.",
            "この実験が示すように、知能を高めようとするとほかの身体的特徴が損なわれ、個体だけでなく集団全体にまで及ぶ結果を招く可能性がある。",
            "As this experiment indicates,|この実験が示すように、||trying to boost intelligence|知能を高めようとすると||may disrupt other physical attributes,|ほかの身体的特徴が損なわれる可能性があり||leading to consequences|結果を招いて||that extend beyond the individual animals|個々の動物を越えて及ぶ||to entire populations.|集団全体にまで。",
            "may disrupt",
        ],
    ],
    [
        [
            "Furthermore, opponents of animal uplift point out that the process would likely involve surgical procedures on healthy animals.",
            "さらに、動物の知能向上に反対する人々は、その過程では健康な動物に外科的処置を施す可能性が高いと指摘する。",
            "Furthermore, opponents of animal uplift|さらに、動物の知能向上に反対する人々は||point out|指摘する||that the process would likely involve|その過程では伴う可能性が高いと||surgical procedures|外科的処置を||on healthy animals.|健康な動物への。",
            "point out",
        ],
        [
            "There would almost certainly be psychological consequences as well, and an uplifted animal’s existence might well be completely transformed.",
            "心理面の影響もほぼ確実に生じ、知能を高められた動物の生き方は一変しかねない。",
            "There would almost certainly be|ほぼ確実に生じるだろう||psychological consequences as well,|心理面の影響も||and an uplifted animal’s existence|そして知能を高められた動物の生き方は||might well be completely transformed.|一変しかねない。",
            "would almost certainly be",
        ],
        [
            "A mouse, whose life would normally be a simple matter of survival, could instead be thrust into a confusing, possibly terrifying awareness of how brief its lifespan is and how little control it has over its environment.",
            "通常ならただ生き延びるだけの単純な一生を送るマウスが、代わりに、自分の寿命がいかに短く、環境をほとんど制御できないかという、混乱を招き恐怖さえ伴う認識へと突然追いやられるかもしれない。",
            "A mouse,|一匹のマウスが||whose life would normally be|その一生は通常なら||a simple matter of survival,|ただ生き延びるだけの単純なものなのに||could instead be thrust|代わりに突然追いやられるかもしれない||into a confusing, possibly terrifying awareness|混乱を招き恐怖さえ伴う認識へ||of how brief its lifespan is|自分の寿命がいかに短いか||and how little control it has|そしてほとんど制御できないかという||over its environment.|自分の環境を。",
            "could instead be thrust",
        ],
        [
            "There is also the issue of whether making such radical alterations to an animal’s biology could ever be considered ethical, since it would be impossible for the creature to give consent beforehand, especially since the procedures would probably not be reversible.",
            "また、動物の生物学的特徴をこのように根本から変えることが倫理的といえるのかという問題もある。動物が事前に同意することは不可能であり、処置が元に戻せない可能性が高いだけになおさらである。",
            "There is also the issue|また問題もある||of whether making such radical alterations|このように根本的な変更を加えることが||to an animal’s biology|動物の生物学的特徴に||could ever be considered ethical,|倫理的とみなされうるのかという||since it would be impossible|不可能だからである||for the creature to give consent beforehand,|動物が事前に同意することは||especially since the procedures|とりわけその処置は||would probably not be reversible.|元に戻せない可能性が高いので。",
            "could ever be considered",
        ],
    ],
    [
        [
            "George Dvorsky, chairperson of the Institute for Ethics and Emerging Technologies, however, argues that withholding animal uplift is itself unethical.",
            "しかし、倫理・新興技術研究所の代表ジョージ・ドヴォルスキーは、動物の知能向上を行わないこと自体が非倫理的だと主張する。",
            "George Dvorsky,|ジョージ・ドヴォルスキーは||chairperson of the Institute for Ethics and Emerging Technologies,|倫理・新興技術研究所の代表である||however, argues|しかし主張する||that withholding animal uplift|動物の知能向上を行わないことは||is itself unethical.|それ自体が非倫理的だと。",
            "argues",
        ],
        [
            "Animals have long been sacrificed as test subjects during the creation of new surgical procedures or the development of medicines that have increased human life expectancy, and if humans artificially increase our own intelligence, animals will likely be sacrificed for that as well.",
            "動物は、人間の寿命を延ばしてきた新しい外科処置や医薬品の開発において、長年実験対象として犠牲にされてきた。そして人間が自らの知能を人為的に高めるなら、そのためにも動物が犠牲にされる可能性が高い。",
            "Animals have long been sacrificed|動物は長年犠牲にされてきた||as test subjects|実験対象として||during the creation of new surgical procedures|新しい外科処置の創出や||or the development of medicines|医薬品の開発において||that have increased human life expectancy,|人間の寿命を延ばしてきた||and if humans artificially increase our own intelligence,|そして人間が自らの知能を人為的に高めるなら||animals will likely be sacrificed|動物が犠牲にされる可能性が高い||for that as well.|そのためにも。",
            "have long been sacrificed",
        ],
        [
            "According to Dvorsky, in light of increased awareness of animal rights and given the tremendous role that animals have played in improving human existence, withholding advances that could improve their intelligence would be just as unethical as withholding them from a group of humans who lack sufficient wealth to afford them.",
            "ドヴォルスキーによれば、動物の権利への意識が高まり、動物が人間の生活向上に果たしてきた大きな役割を考えれば、動物の知能を高めうる進歩を与えないことは、それを購入できるだけの財力がない人間の集団に同じ進歩を与えないことと同様に非倫理的である。",
            "According to Dvorsky,|ドヴォルスキーによれば、||in light of increased awareness of animal rights|動物の権利への意識の高まりを踏まえ||and given the tremendous role|そして大きな役割を考えれば||that animals have played|動物が果たしてきた||in improving human existence,|人間の生活向上に||withholding advances|進歩を与えないことは||that could improve their intelligence|動物の知能を高めうる||would be just as unethical|同様に非倫理的である||as withholding them from a group of humans|それを人間の集団に与えないことと||who lack sufficient wealth to afford them.|購入できるだけの財力がない。",
            "would be",
        ],
        [
            "While the ability to uplift animals would have undeniable benefits, it is also true that we face an ethical dilemma when altering another species.",
            "動物の知能を高める能力には否定できない利点がある一方、別の種を改変するとき私たちが倫理的ジレンマに直面することも事実である。",
            "While the ability to uplift animals|動物の知能を高める能力には||would have undeniable benefits,|否定できない利点がある一方||it is also true|それもまた事実である||that we face an ethical dilemma|私たちが倫理的ジレンマに直面することが||when altering another species.|別の種を改変するときに。",
            "is",
        ],
        [
            "Clearly, there are difficult decisions about animal uplift that need to be made.",
            "明らかに、動物の知能向上については難しい判断を下さなければならない。",
            "Clearly,|明らかに、||there are difficult decisions|難しい判断がある||about animal uplift|動物の知能向上について||that need to be made.|下されなければならない。",
            "need to be made",
        ],
    ],
]


def _paragraphs(groups):
    return [" ".join(pair[0] for pair in group) for group in groups]


def _translations(groups):
    return ["".join(pair[1] for pair in group) for group in groups]


def _pairs(groups):
    return [pair for group in groups for pair in group]


SECTION3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，質問に対して最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Uruk",
            "paragraphs": _paragraphs(URUK_GROUPS),
            "translations": _translations(URUK_GROUPS),
            "sentencePairs": _pairs(URUK_GROUPS),
            "questions": [
                {
                    "number": 25,
                    "question": "What does the author of the passage say about Uruk’s development?",
                    "questionTranslation": "本文の筆者は、ウルクの発展について何と述べているか。",
                    "choices": [
                        "Rapid progress would have been possible even without the technological advances that increased agricultural efficiency.",
                        "One important characteristic was its ability to produce more food than it needed, which allowed for more rapid change to occur.",
                        "The construction of canals for agricultural use could not keep up with the needs of a growing population.",
                        "It lost out on the most profitable trade deals because it reserved too much of its crop harvests for its own population.",
                    ],
                    "choiceTranslations": [
                        "農業効率を高めた技術の進歩がなくても、急速な発展は可能だっただろう。",
                        "必要量を超える食料を生産できたことが重要な特徴であり、それによってさらに急速な変化が可能になった。",
                        "農業用水路の建設は、増加する人口の必要量に追いつかなかった。",
                        "収穫物の多くを住民向けに確保したため、最も利益の大きい交易の機会を逃した。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 技術の進歩は著しい成長を支えた要因として挙げられており、それがなくても急速に発展できたとは述べていない。",
                        "✅ 余剰生産物を生み出して交易できたことが発展を支えたという内容で、produce more food than it needed は create a surplus の言い換え→正解。💡",
                        "❌ 灌漑用水路は農業効率を高め、増加する人口を支えたとある。人口の必要量に追いつかなかったという記述はない。",
                        "❌ 余剰生産物は交易できたとあり、収穫物を住民用に確保しすぎて交易で損をしたとは述べていない。",
                    ],
                    "sourceEvidence": [
                        "These advances not only allowed Uruk to support a growing population but also to create a surplus, which could then be traded."
                    ],
                },
                {
                    "number": 26,
                    "question": "What is one thing we learn about the cuneiform script?",
                    "questionTranslation": "くさび形文字について分かることの一つは何か。",
                    "choices": [
                        "The benefits its use provided were not enough to enable Uruk to stay ahead of rival cities.",
                        "Although it had uses that aided development in Uruk, it was less suited to complex bureaucratic tasks.",
                        "It was first developed for religious purposes but was later adopted for use in commerce and government.",
                        "It provided Uruk with a means to help manage the administration of its increasingly complex society.",
                    ],
                    "choiceTranslations": [
                        "その使用による恩恵だけでは、ウルクが競合都市より優位であり続けるには不十分だった。",
                        "ウルクの発展に役立つ用途はあったが、複雑な行政業務にはあまり適していなかった。",
                        "最初は宗教目的で作られたが、後に商業や統治に使われるようになった。",
                        "ますます複雑になる社会の行政管理を助ける手段をウルクにもたらした。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ くさび形文字は複雑な都市の統治を円滑にしたとあるが、競合都市より優位であり続けるには不十分だったとは述べていない。",
                        "❌ 会計や一般行政に使われ、複雑化する都市の統治に役立ったため、複雑な行政業務に不向きだったという説明とは逆である。",
                        "❌ 初期には品物を表す絵を使って記録管理を行ったとある。宗教目的で最初に作られたとは述べていない。",
                        "✅ 会計や一般行政に使われ、ますます複雑化する都市の統治を円滑にしたという本文の内容に一致する→正解。💡",
                    ],
                    "sourceEvidence": [
                        "The writing system gradually became more sophisticated and was used for accounting and general administrative matters, which helped facilitate the governance of the increasingly complex city."
                    ],
                },
                {
                    "number": 27,
                    "question": "Which of the following statements is true, based on the final paragraph?",
                    "questionTranslation": "最終段落に基づくと、次の記述のうち正しいものはどれか。",
                    "choices": [
                        "Even though the Sumer region was attacked and defeated by outside forces, the religious heritage of Uruk was not destroyed.",
                        "Uruk borrowed some of its religious architecture and artistic techniques from neighboring cities in Sumer.",
                        "The Akkadians had to destroy much of the wall and stone buildings in order to defeat Uruk.",
                        "Uruk’s decline can be attributed to the fact that neighboring Sumerian cities created alliances with the Akkadians.",
                    ],
                    "choiceTranslations": [
                        "シュメール地方は外部勢力に攻撃され敗れたものの、ウルクの宗教的遺産は破壊されなかった。",
                        "ウルクは宗教建築や芸術技法の一部を、近隣のシュメール諸都市から取り入れた。",
                        "アッカド人はウルクを倒すため、市壁や石造建築の多くを破壊しなければならなかった。",
                        "ウルクの衰退は、近隣のシュメール諸都市がアッカド人と同盟を結んだことに起因する。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ アッカド人に征服された後も、ウルクの宗教地区は尊重され保護されたとあり、宗教的遺産が破壊されなかったという内容に一致する→正解。💡",
                        "❌ 宗教建築や芸術技法を近隣都市から取り入れたという記述はない。",
                        "❌ 市壁や石造建築は後の発掘で明らかになったものとして挙げられており、アッカド人が破壊したとは述べていない。",
                        "❌ 近隣都市との長年の競争で外部勢力に対して脆弱になったとあるが、近隣都市がアッカド人と同盟を結んだとは述べていない。",
                    ],
                    "sourceEvidence": [
                        "Despite this conquest, Uruk’s religious districts were respected and protected"
                    ],
                },
            ],
        },
        {
            "label": "B",
            "title": "Animal Uplift",
            "paragraphs": _paragraphs(ANIMAL_UPLIFT_GROUPS),
            "translations": _translations(ANIMAL_UPLIFT_GROUPS),
            "sentencePairs": _pairs(ANIMAL_UPLIFT_GROUPS),
            "questions": [
                {
                    "number": 28,
                    "question": "What is one thing that we learn about the research into the FOXP2 gene?",
                    "questionTranslation": "FOXP2遺伝子の研究について分かることの一つは何か。",
                    "choices": [
                        "Since it only had a minor effect on the mice’s memory, it cannot really be said to have improved their overall intelligence.",
                        "Although it affected one element of the mice’s intelligence, it is just an early step in what will most likely be a complicated process.",
                        "It demonstrated that the way that mice communicated with each other was more sophisticated than had previously been believed.",
                        "It indicates that mice may actually have a form of intelligence that researchers were not aware of in the past.",
                    ],
                    "choiceTranslations": [
                        "マウスの記憶にはわずかな影響しかなかったため、全体的な知能を向上させたとは実際にはいえない。",
                        "マウスの知能の一要素に影響を与えたものの、今後おそらく複雑になる過程のまだ初期段階にすぎない。",
                        "マウスどうしの意思疎通の方法が、従来考えられていたより高度だったことを示した。",
                        "研究者が以前は認識していなかった種類の知能を、マウスが実際に持つ可能性を示している。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ FOXP2遺伝子は記憶力を significantly enhanced（大幅に高めた）とあり、影響がわずかだったという説明と矛盾する。",
                        "✅ 記憶は知能に欠かせない一要素だが、研究は予備段階で、知能には多数の遺伝子が関わる複雑な過程だという本文の要点に一致する→正解。💡",
                        "❌ 実験で調べたのは迷路の経路学習と記憶であり、マウスどうしの意思疎通ではない。",
                        "❌ 未知の種類の知能を発見したのではなく、遺伝子操作によって記憶力が高まったことを示した研究である。",
                    ],
                    "sourceEvidence": [
                        "indicating that the gene had significantly enhanced their memory, which is an essential component of intelligence",
                        "This research is preliminary, however, and intelligence depends on a multitude of genes",
                    ],
                },
                {
                    "number": 29,
                    "question": "What does the fish experiment indicate about attempts at animal uplift?",
                    "questionTranslation": "魚の実験は、動物の知能向上の試みについて何を示しているか。",
                    "choices": [
                        "There are limits to how intelligent animals can become, and no amount of breeding will ever be able to overcome them.",
                        "It is possible that an attempt to increase animal intelligence will actually have the opposite of its intended effect.",
                        "Attempts to increase an animal’s intelligence could interfere with other important aspects of the animal’s biology.",
                        "While it is possible to slightly increase animal intelligence, it is not likely that it will be inherited by an animal’s offspring.",
                    ],
                    "choiceTranslations": [
                        "動物がどこまで賢くなれるかには限界があり、どれほど交配してもそれを克服することはできない。",
                        "動物の知能を高めようとする試みが、実際には意図したものと反対の効果をもたらす可能性がある。",
                        "動物の知能を高める試みは、その動物の生物学的なほかの重要な側面を妨げる可能性がある。",
                        "動物の知能をわずかに高めることは可能だが、その特徴が子に受け継がれる可能性は低い。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 知能向上に絶対的な限界があり、交配では克服できないとは述べていない。",
                        "❌ 大きな脳を持つ魚の子は認知テストで優れていたため、知能への効果が意図と反対だったのではない。問題は別の身体的特徴への影響である。",
                        "✅ 脳を大きくすると、消化器官が小さくなり子の数も減ったことから、知能向上がほかの生物学的特徴を損なう可能性を示している→正解。💡",
                        "❌ 脳の大きな魚の子はさらに大きな脳を持つ傾向があったため、子に受け継がれにくいという説明とは逆である。",
                    ],
                    "sourceEvidence": [
                        "trying to boost intelligence may disrupt other physical attributes, leading to consequences that extend beyond the individual animals to entire populations"
                    ],
                },
                {
                    "number": 30,
                    "question": "One argument against animal uplift that is presented in the third paragraph is that",
                    "questionTranslation": "第3段落で示されている、動物の知能向上に反対する主張の一つは何か。",
                    "choices": [
                        "it should not be carried out because it is impossible for animals to agree to what is going to happen to them.",
                        "it could bring about significant changes in animal behavior that could, in turn, have negative effects on the environment.",
                        "there are likely to be more risks in performing operations on animals’ brains due to our lack of knowledge about how they function.",
                        "there is a significant risk that the effects of the procedure could reduce the survival instincts of animals that receive it.",
                    ],
                    "choiceTranslations": [
                        "動物は自分に何が行われるのかに同意できないため、実施すべきではない。",
                        "動物の行動を大きく変え、それが環境に悪影響を与える可能性がある。",
                        "動物の脳の働きについての知識が不足しているため、脳の手術にはより多くの危険が伴う可能性が高い。",
                        "処置の影響によって、それを受けた動物の生存本能が低下する重大な危険がある。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 動物は処置に事前同意できず、しかも元に戻せない可能性が高いため、根本的な改変を倫理的とみなせるかが問題になるという主張に一致する→正解。💡",
                        "❌ 動物の存在や心理が変わる可能性は述べられているが、行動の変化が環境に悪影響を与えるとは述べていない。",
                        "❌ 健康な動物への外科的処置には触れているが、脳機能への知識不足によって手術の危険が増すとは述べていない。",
                        "❌ マウスが生存だけでなく寿命や環境を意識する可能性は述べられているが、生存本能が低下するとは述べていない。",
                    ],
                    "sourceEvidence": [
                        "it would be impossible for the creature to give consent beforehand, especially since the procedures would probably not be reversible"
                    ],
                },
                {
                    "number": 31,
                    "question": "What does George Dvorsky believe about animal uplift?",
                    "questionTranslation": "ジョージ・ドヴォルスキーは動物の知能向上について何と考えているか。",
                    "choices": [
                        "Humans need to develop better types of surgical procedures so that we do not harm animals when trying to uplift them.",
                        "It is likely that the same medical advances that are used to uplift animals will also help them to live longer, healthier lives.",
                        "Humans should develop the technology necessary for uplifting animals before we consider whether it is right to do so or not.",
                        "If humans use animals in the process of increasing our own intelligence, that would increase our obligation to uplift them.",
                    ],
                    "choiceTranslations": [
                        "動物の知能を高める際に傷つけないよう、人間はより優れた種類の外科処置を開発する必要がある。",
                        "動物の知能向上に使われるのと同じ医療上の進歩が、動物をより長く健康に生きさせることにも役立つ可能性が高い。",
                        "それが正しいかどうかを考える前に、人間は動物の知能向上に必要な技術を開発すべきである。",
                        "人間が自らの知能を高める過程で動物を利用するなら、動物の知能も高める責務が強まる。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ ドヴォルスキーは動物の知能向上を差し控えることが非倫理的だと論じており、より安全な外科処置を開発すべきだとは述べていない。",
                        "❌ 人間の寿命を延ばす医薬品開発で動物が使われたとはあるが、知能向上技術が動物の寿命や健康も改善するとは述べていない。",
                        "❌ 技術を先に開発してから倫理を考えるべきだという主張ではなく、動物に進歩を与えないこと自体が非倫理的だと論じている。",
                        "✅ 人間が自らの知能向上のためにも動物を犠牲にするなら、人間社会に貢献してきた動物に知能向上の恩恵を与えないのは非倫理的だという主張に一致する→正解。💡",
                    ],
                    "sourceEvidence": [
                        "if humans artificially increase our own intelligence, animals will likely be sacrificed for that as well",
                        "withholding advances that could improve their intelligence would be just as unethical as withholding them from a group of humans who lack sufficient wealth to afford them",
                    ],
                },
            ],
        },
    ],
}


def main():
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            "data.json が見つかりません。大問1・2を生成した後に実行してください: "
            f"{DATA_PATH}"
        )

    with DATA_PATH.open(encoding="utf-8") as source:
        data = json.load(source)

    sections = data.get("sections")
    if not isinstance(sections, list):
        raise ValueError("data.json の sections が配列ではありません。")

    updated = []
    replaced = False
    for section in sections:
        if isinstance(section, dict) and section.get("name") == "大問3":
            if not replaced:
                updated.append(SECTION3)
                replaced = True
            continue
        updated.append(section)
    if not replaced:
        updated.append(SECTION3)

    data["sections"] = updated
    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as destination:
        json.dump(data, destination, ensure_ascii=False, indent=4)
        destination.write("\n")

    print(f"大問3を保存しました: {DATA_PATH}")
    print("passages=2 questions=7 sentencePairs=38")


if __name__ == "__main__":
    main()
