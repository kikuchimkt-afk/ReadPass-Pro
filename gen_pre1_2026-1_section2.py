# -*- coding: utf-8 -*-
"""Generate Part 2 for the 2026-1 EIKEN Grade Pre-1 reading data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "pre-grade1" / "2026-1" / "data.json"


SECTION2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(19)から(24)までの(　)に入れるのに最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Birth Order",
            "paragraphs": [
                "The idea that the order in which children are born can have a lasting and dramatic effect on their personalities was developed by the Austrian psychologist Alfred Adler more than a century ago. ( 19 ), Adler believed that firstborns tended to be responsible yet anxious, that middle children were more diplomatic, and that youngest siblings were more rebellious. Today, the theory is featured in many parenting books.",
                "Extensive research has been conducted on birth order. One notable study, for example, examined thousands of teenagers and found that it did lead to some measurable differences. Eldest siblings, for instance, differed from others in terms of things like responsibility and anxiety. However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype. In addition to such contradictions, the differences for every birth position were extremely slight. According to the researchers, associations between birth order and a person’s character ( 20 ).",
                "As children grow, there are obvious differences in everything from maturity to rebelliousness. Parents often observe that younger children have less self-control and disobey them more than older children. However, it is also true that this ( 21 ). It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development their children are going through. Personality, experts tell us, is determined more by things like genetics and one’s living environment than it is by the order in which children were born.",
            ],
            "translations": [
                "子どもが生まれた順番が、その性格に長期的かつ大きな影響を与えうるという考えは、1世紀以上前にオーストリアの心理学者アルフレッド・アドラーによって提唱された。( 19 )、アドラーは、第一子は責任感が強い一方で不安を感じやすく、中間子は人の間をうまく取り持ち、末っ子はより反抗的な傾向があると考えた。今日、この理論は多くの育児書で取り上げられている。",
                "出生順位については幅広い研究が行われてきた。例えば、ある注目すべき研究では数千人の10代の若者を調べ、出生順位が測定可能な違いをいくつか生むことが分かった。例えば最年長のきょうだいは、責任感や不安といった点で、ほかのきょうだいと異なっていた。しかし、第一子は予想どおり責任感が強いことが分かった一方、不安はむしろ少ない傾向にあり、これは固定観念と一致しなかった。このような矛盾に加え、どの出生順位についても違いはごくわずかだった。研究者らによると、出生順位と人の性格との関連は( 20 )。",
                "子どもが成長するにつれて、成熟度から反抗性に至るまでのあらゆる面に明らかな違いが見られる。親はしばしば、年下の子どもは年上の子どもより自制心が弱く、親に従わないと感じる。しかし、これが( 21 )こともまた事実である。したがって、多くの人が出生順位による性格への影響だと受け止めているものは、実際には子どもが通過している一時的な発達段階にすぎないようだ。専門家によれば、性格を決めるのは、子どもの生まれた順番よりも、遺伝や生活環境などの要因である。",
            ],
            "sentencePairs": [
                [
                    "The idea that the order in which children are born can have a lasting and dramatic effect on their personalities was developed by the Austrian psychologist Alfred Adler more than a century ago.",
                    "子どもが生まれた順番が、その性格に長期的かつ大きな影響を与えうるという考えは、1世紀以上前にオーストリアの心理学者アルフレッド・アドラーによって提唱された。",
                    "The idea|その考えは||that the order in which children are born|子どもが生まれる順番が||can have a lasting and dramatic effect on their personalities|その性格に長期的かつ大きな影響を与えうるという||was developed by the Austrian psychologist Alfred Adler|オーストリアの心理学者アルフレッド・アドラーによって提唱された||more than a century ago.|1世紀以上前に。",
                    "was developed",
                ],
                [
                    "( 19 ), Adler believed that firstborns tended to be responsible yet anxious, that middle children were more diplomatic, and that youngest siblings were more rebellious.",
                    "( 19 )、アドラーは、第一子は責任感が強い一方で不安を感じやすく、中間子は人の間をうまく取り持ち、末っ子はより反抗的な傾向があると考えた。",
                ],
                [
                    "Today, the theory is featured in many parenting books.",
                    "今日、この理論は多くの育児書で取り上げられている。",
                    "Today,|今日では、||the theory is featured|この理論は取り上げられている||in many parenting books.|多くの育児書で。",
                    "is featured",
                ],
                [
                    "Extensive research has been conducted on birth order.",
                    "出生順位については幅広い研究が行われてきた。",
                    "Extensive research has been conducted|幅広い研究が行われてきた||on birth order.|出生順位について。",
                    "has been conducted",
                ],
                [
                    "One notable study, for example, examined thousands of teenagers and found that it did lead to some measurable differences.",
                    "例えば、ある注目すべき研究では数千人の10代の若者を調べ、出生順位が測定可能な違いをいくつか生むことが分かった。",
                    "One notable study, for example,|例えば、ある注目すべき研究では、||examined thousands of teenagers|数千人の10代の若者を調べ||and found|そして明らかにした||that it did lead to some measurable differences.|出生順位が測定可能な違いをいくつか生むことを。",
                    "examined",
                ],
                [
                    "Eldest siblings, for instance, differed from others in terms of things like responsibility and anxiety.",
                    "例えば最年長のきょうだいは、責任感や不安といった点で、ほかのきょうだいと異なっていた。",
                    "Eldest siblings, for instance,|例えば最年長のきょうだいは、||differed from others|ほかのきょうだいと異なっていた||in terms of things like responsibility and anxiety.|責任感や不安といった点で。",
                    "differed",
                ],
                [
                    "However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype.",
                    "しかし、第一子は予想どおり責任感が強いことが分かった一方、不安はむしろ少ない傾向にあり、これは固定観念と一致しなかった。",
                    "However,|しかし、||while firstborns were, as expected, found to be more responsible,|第一子は予想どおり責任感が強いことが分かった一方、||they tended to be less anxious,|不安はむしろ少ない傾向にあり、||which did not fit the stereotype.|これは固定観念と一致しなかった。",
                    "tended",
                ],
                [
                    "In addition to such contradictions, the differences for every birth position were extremely slight.",
                    "このような矛盾に加え、どの出生順位についても違いはごくわずかだった。",
                    "In addition to such contradictions,|このような矛盾に加えて、||the differences for every birth position|どの出生順位についても違いは||were extremely slight.|ごくわずかだった。",
                    "were",
                ],
                [
                    "According to the researchers, associations between birth order and a person’s character ( 20 ).",
                    "研究者らによると、出生順位と人の性格との関連は( 20 )。",
                ],
                [
                    "As children grow, there are obvious differences in everything from maturity to rebelliousness.",
                    "子どもが成長するにつれて、成熟度から反抗性に至るまでのあらゆる面に明らかな違いが見られる。",
                    "As children grow,|子どもが成長するにつれて、||there are obvious differences|明らかな違いが見られる||in everything from maturity to rebelliousness.|成熟度から反抗性に至るまでのあらゆる面に。",
                    "are",
                ],
                [
                    "Parents often observe that younger children have less self-control and disobey them more than older children.",
                    "親はしばしば、年下の子どもは年上の子どもより自制心が弱く、親に従わないと感じる。",
                    "Parents often observe|親はしばしば感じる||that younger children have less self-control|年下の子どもは自制心が弱く||and disobey them more than older children.|年上の子どもより親に従わないと。",
                    "observe",
                ],
                [
                    "However, it is also true that this ( 21 ).",
                    "しかし、これが( 21 )こともまた事実である。",
                ],
                [
                    "It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development their children are going through.",
                    "したがって、多くの人が出生順位による性格への影響だと受け止めているものは、実際には子どもが通過している一時的な発達段階にすぎないようだ。",
                    "It therefore seems|したがって、〜のようだ||that what many people take to be birth order affecting personality|多くの人が出生順位による性格への影響だと受け止めているものは||is really just the temporary stages of development|実際には一時的な発達段階にすぎない||their children are going through.|子どもが通過している。",
                    "seems",
                ],
                [
                    "Personality, experts tell us, is determined more by things like genetics and one’s living environment than it is by the order in which children were born.",
                    "専門家によれば、性格を決めるのは、子どもの生まれた順番よりも、遺伝や生活環境などの要因である。",
                    "Personality, experts tell us,|専門家によれば、性格は||is determined more by things like genetics and one’s living environment|遺伝や生活環境などによってより強く決まり||than it is by the order in which children were born.|子どもが生まれた順番によって決まるのではない。",
                    "is determined",
                ],
            ],
            "questions": [
                {
                    "number": 19,
                    "choices": ["Consequently", "Specifically", "Nonetheless", "Otherwise"],
                    "answer": 2,
                    "choiceTranslations": ["その結果", "具体的に言うと", "それにもかかわらず", "そうでなければ"],
                    "choiceAnalysis": [
                        "❌ Consequently＝その結果。前文は理論が提唱された経緯であり、後続文との間に原因と結果の関係はない。",
                        "✅ Specifically＝具体的に言うと。理論の内容を、第一子・中間子・末っ子の特徴に分けて具体化している→正解。💡 抽象的な説明のあとに具体例や詳細が続く流れを見抜く。",
                        "❌ Nonetheless＝それにもかかわらず。前後に予想外の対立や逆接の関係はない。",
                        "❌ Otherwise＝そうでなければ。条件に対する別の結果を示す文脈ではない。",
                    ],
                    "sourceEvidence": [
                        "Adler believed that firstborns tended to be responsible yet anxious, that middle children were more diplomatic, and that youngest siblings were more rebellious."
                    ],
                },
                {
                    "number": 20,
                    "choices": [
                        "have less effect on youngest siblings",
                        "become stronger as children age",
                        "are mostly meaningless",
                        "should be more widely accepted",
                    ],
                    "answer": 3,
                    "choiceTranslations": [
                        "末っ子にはより小さな影響しか与えない",
                        "子どもの年齢が上がるにつれて強くなる",
                        "ほとんど意味がない",
                        "もっと広く受け入れられるべきだ",
                    ],
                    "choiceAnalysis": [
                        "❌ have less effect on youngest siblings＝末っ子にはより小さな影響しか与えない。本文はすべての出生順位で差がごくわずかだと述べており、末っ子だけを比較していない。",
                        "❌ become stronger as children age＝子どもの年齢が上がるにつれて強くなる。次段落では年齢による違いは一時的な発達段階だと説明され、強まるとは述べていない。",
                        "✅ are mostly meaningless＝ほとんど意味がない。予想と矛盾する結果があり、どの出生順位でも差が極めて小さいという研究者の評価に合う→正解。💡 空所直前の contradictions と extremely slight が結論の根拠。",
                        "❌ should be more widely accepted＝もっと広く受け入れられるべきだ。研究結果は出生順位説を積極的に支持するのではなく、その関連の弱さを示している。",
                    ],
                    "sourceEvidence": [
                        "However, while firstborns were, as expected, found to be more responsible, they tended to be less anxious, which did not fit the stereotype.",
                        "the differences for every birth position were extremely slight.",
                    ],
                },
                {
                    "number": 21,
                    "choices": [
                        "tends to fade with time",
                        "is related mainly to intelligence",
                        "affects their success as adults",
                        "is due to parenting styles",
                    ],
                    "answer": 1,
                    "choiceTranslations": [
                        "時間とともに薄れる傾向がある",
                        "主として知能に関係している",
                        "成人後の成功に影響する",
                        "子育ての仕方が原因である",
                    ],
                    "choiceAnalysis": [
                        "✅ tends to fade with time＝時間とともに薄れる傾向がある。直後で、子どもの行動差は成長過程の一時的な段階にすぎないと説明されている→正解。💡 this が直前の年下の子どもの自制心や反抗的な行動を受けることを確認する。",
                        "❌ is related mainly to intelligence＝主として知能に関係している。本文は成熟度・自制心・反抗性を扱い、知能との関係は述べていない。",
                        "❌ affects their success as adults＝成人後の成功に影響する。成人後の成功についての記述はなく、むしろ差は一時的だと説明される。",
                        "❌ is due to parenting styles＝子育ての仕方が原因である。本文が性格の主な要因として挙げるのは遺伝と生活環境で、子育ての仕方に限定していない。",
                    ],
                    "sourceEvidence": [
                        "It therefore seems that what many people take to be birth order affecting personality is really just the temporary stages of development their children are going through."
                    ],
                },
            ],
        },
        {
            "label": "B",
            "title": "Digital Nations",
            "paragraphs": [
                "The small Polynesian island nation of Tuvalu is in danger of disappearing forever. Scientists have predicted that, decades from now, living in Tuvalu will become impossible due to rising sea levels caused by climate change. When that happens, the only option for Tuvaluans will be to move elsewhere. ( 22 ), the preparations for doing this are already in place. Tuvalu has negotiated an agreement with Australia that allows a certain number of its people to emigrate there every year.",
                "Tuvalu’s government is doing what it can to save its nation. Sea barriers have been built, and work is underway to create an area of raised land that will provide a habitable area for residents. However, the government knows these measures may be useless in the long term. So, it ( 23 ). A few years ago, it set up the Future Now Project. Part of this project involves creating a virtual reconstruction of the nation. Along with preserving geographical features, the project aims to create a digital record of Tuvalu’s people and customs.",
                "Some critics claim the resources required for the project could be better used to tackle climate change. In response, Tuvalu’s government points out that the project ( 24 ). The current international treaty states that sovereign nations must have a “defined territory” and a “permanent population.” Tuvalu’s government hopes to pioneer a new form of statehood that allows it to continue to exist by meeting these criteria in a virtual form. This could also help to ensure the survival of other island nations facing similar threats from the sea.",
            ],
            "translations": [
                "ポリネシアの小さな島国ツバルは、永遠に消滅してしまう危機にある。科学者たちは、気候変動による海面上昇のため、数十年後にはツバルで暮らすことが不可能になると予測している。そうなったとき、ツバルの人々に残された唯一の選択肢は、ほかの場所へ移ることになる。( 22 )、そのための準備はすでに整っている。ツバルはオーストラリアと協定を結び、毎年一定数の国民が同国へ移住できるようにしている。",
                "ツバル政府は国を救うためにできることを行っている。防潮壁が建設され、住民が暮らせる場所となるかさ上げ地を造成する工事も進められている。しかし政府は、こうした対策が長期的には役に立たないかもしれないことを分かっている。そこで政府は( 23 )。数年前、政府は「フューチャー・ナウ・プロジェクト」を立ち上げた。このプロジェクトの一部には、国を仮想空間に再現する取り組みが含まれる。地理的特徴を保存するだけでなく、ツバルの人々と慣習をデジタル記録として残すことも目指している。",
                "批判する人の中には、プロジェクトに必要な資源を気候変動への対策に使うほうがよいと主張する人もいる。これに対し、ツバル政府は、このプロジェクトが( 24 )と指摘する。現行の国際条約では、主権国家は「明確に定められた領土」と「定住人口」を持たなければならないとされている。ツバル政府は、これらの要件を仮想的な形で満たすことにより国が存続できる、新たな国家のあり方を切り開きたいと考えている。これは、海から同様の脅威を受けているほかの島国の存続を確かなものにするうえでも役立つ可能性がある。",
            ],
            "sentencePairs": [
                [
                    "The small Polynesian island nation of Tuvalu is in danger of disappearing forever.",
                    "ポリネシアの小さな島国ツバルは、永遠に消滅してしまう危機にある。",
                    "The small Polynesian island nation of Tuvalu|ポリネシアの小さな島国ツバルは||is in danger of disappearing forever.|永遠に消滅してしまう危機にある。",
                    "is in danger",
                ],
                [
                    "Scientists have predicted that, decades from now, living in Tuvalu will become impossible due to rising sea levels caused by climate change.",
                    "科学者たちは、気候変動による海面上昇のため、数十年後にはツバルで暮らすことが不可能になると予測している。",
                    "Scientists have predicted|科学者たちは予測している||that, decades from now,|数十年後には||living in Tuvalu will become impossible|ツバルで暮らすことが不可能になると||due to rising sea levels|海面上昇のために||caused by climate change.|気候変動によって引き起こされる。",
                    "have predicted",
                ],
                [
                    "When that happens, the only option for Tuvaluans will be to move elsewhere.",
                    "そうなったとき、ツバルの人々に残された唯一の選択肢は、ほかの場所へ移ることになる。",
                    "When that happens,|そうなったとき、||the only option for Tuvaluans|ツバルの人々に残された唯一の選択肢は||will be to move elsewhere.|ほかの場所へ移ることになる。",
                    "will be",
                ],
                [
                    "( 22 ), the preparations for doing this are already in place.",
                    "( 22 )、そのための準備はすでに整っている。",
                ],
                [
                    "Tuvalu has negotiated an agreement with Australia that allows a certain number of its people to emigrate there every year.",
                    "ツバルはオーストラリアと協定を結び、毎年一定数の国民が同国へ移住できるようにしている。",
                    "Tuvalu has negotiated an agreement with Australia|ツバルはオーストラリアと協定を結んだ||that allows a certain number of its people|その協定により一定数の国民が||to emigrate there every year.|毎年同国へ移住できる。",
                    "has negotiated",
                ],
                [
                    "Tuvalu’s government is doing what it can to save its nation.",
                    "ツバル政府は国を救うためにできることを行っている。",
                    "Tuvalu’s government is doing|ツバル政府は行っている||what it can|できることを||to save its nation.|国を救うために。",
                    "is doing",
                ],
                [
                    "Sea barriers have been built, and work is underway to create an area of raised land that will provide a habitable area for residents.",
                    "防潮壁が建設され、住民が暮らせる場所となるかさ上げ地を造成する工事も進められている。",
                    "Sea barriers have been built,|防潮壁が建設され、||and work is underway|工事も進められている||to create an area of raised land|かさ上げ地を造成するための||that will provide a habitable area for residents.|それは住民が暮らせる場所となる。",
                    "have been built",
                ],
                [
                    "However, the government knows these measures may be useless in the long term.",
                    "しかし政府は、こうした対策が長期的には役に立たないかもしれないことを分かっている。",
                    "However,|しかし、||the government knows|政府は分かっている||these measures may be useless|こうした対策が役に立たないかもしれないことを||in the long term.|長期的には。",
                    "knows",
                ],
                [
                    "So, it ( 23 ).",
                    "そこで政府は( 23 )。",
                ],
                [
                    "A few years ago, it set up the Future Now Project.",
                    "数年前、政府は「フューチャー・ナウ・プロジェクト」を立ち上げた。",
                    "A few years ago,|数年前、||it set up|政府は立ち上げた||the Future Now Project.|「フューチャー・ナウ・プロジェクト」を。",
                    "set up",
                ],
                [
                    "Part of this project involves creating a virtual reconstruction of the nation.",
                    "このプロジェクトの一部には、国を仮想空間に再現する取り組みが含まれる。",
                    "Part of this project involves|このプロジェクトの一部には||creating a virtual reconstruction of the nation.|国を仮想復元する取り組みが含まれる。",
                    "involves",
                ],
                [
                    "Along with preserving geographical features, the project aims to create a digital record of Tuvalu’s people and customs.",
                    "地理的特徴を保存するだけでなく、ツバルの人々と慣習をデジタル記録として残すことも目指している。",
                    "Along with preserving geographical features,|地理的特徴を保存するだけでなく、||the project aims to create|プロジェクトは作ることを目指す||a digital record of Tuvalu’s people and customs.|ツバルの人々と慣習のデジタル記録を。",
                    "aims",
                ],
                [
                    "Some critics claim the resources required for the project could be better used to tackle climate change.",
                    "批判する人の中には、プロジェクトに必要な資源を気候変動への対策に使うほうがよいと主張する人もいる。",
                    "Some critics claim|批判する人の中には主張する人もいる||the resources required for the project|プロジェクトに必要な資源を||could be better used|使うほうがよいと||to tackle climate change.|気候変動に取り組むために。",
                    "claim",
                ],
                [
                    "In response, Tuvalu’s government points out that the project ( 24 ).",
                    "これに対し、ツバル政府は、このプロジェクトが( 24 )と指摘する。",
                ],
                [
                    "The current international treaty states that sovereign nations must have a “defined territory” and a “permanent population.”",
                    "現行の国際条約では、主権国家は「明確に定められた領土」と「定住人口」を持たなければならないとされている。",
                    "The current international treaty states|現行の国際条約では定められている||that sovereign nations must have|主権国家は持たなければならないと||a “defined territory”|「明確に定められた領土」と||and a “permanent population.”|「定住人口」を。",
                    "states",
                ],
                [
                    "Tuvalu’s government hopes to pioneer a new form of statehood that allows it to continue to exist by meeting these criteria in a virtual form.",
                    "ツバル政府は、これらの要件を仮想的な形で満たすことにより国が存続できる、新たな国家のあり方を切り開きたいと考えている。",
                    "Tuvalu’s government hopes|ツバル政府は望んでいる||to pioneer a new form of statehood|新たな国家のあり方を切り開くことを||that allows it to continue to exist|それによって国が存続できる||by meeting these criteria|これらの要件を満たすことにより||in a virtual form.|仮想的な形で。",
                    "hopes",
                ],
                [
                    "This could also help to ensure the survival of other island nations facing similar threats from the sea.",
                    "これは、海から同様の脅威を受けているほかの島国の存続を確かなものにするうえでも役立つ可能性がある。",
                    "This could also help|これは〜にも役立つ可能性がある||to ensure the survival|存続を確かなものにするうえで||of other island nations|ほかの島国の||facing similar threats from the sea.|海から同様の脅威を受けている。",
                    "could also help",
                ],
            ],
            "questions": [
                {
                    "number": 22,
                    "choices": ["On the contrary", "Despite this", "Similarly", "In fact"],
                    "answer": 4,
                    "choiceTranslations": ["それどころか", "これにもかかわらず", "同様に", "実際"],
                    "choiceAnalysis": [
                        "❌ On the contrary＝それどころか。前文の移住の必要性を否定するのではなく、移住の準備が進んでいることを補強している。",
                        "❌ Despite this＝これにもかかわらず。準備は移住の必要性に反する事柄ではなく、その必要性を見越した対応である。",
                        "❌ Similarly＝同様に。比較対象となる別の国や同種の事例は直前に示されていない。",
                        "✅ In fact＝実際。将来は移住しかないという説明を受け、その準備がすでに進んでいるという、さらに具体的で強い事実を示す→正解。💡 一般的な説明を具体的事実で補強する流れを捉える。",
                    ],
                    "sourceEvidence": [
                        "the preparations for doing this are already in place.",
                        "Tuvalu has negotiated an agreement with Australia that allows a certain number of its people to emigrate there every year.",
                    ],
                },
                {
                    "number": 23,
                    "choices": [
                        "is turning to technology instead",
                        "is planning to construct stronger defenses",
                        "has stopped all current projects",
                        "has requested help from other nations",
                    ],
                    "answer": 1,
                    "choiceTranslations": [
                        "代わりに技術を活用しようとしている",
                        "より強固な防御策を計画している",
                        "現在のすべての事業を中止した",
                        "ほかの国々に支援を要請した",
                    ],
                    "choiceAnalysis": [
                        "✅ is turning to technology instead＝代わりに技術を活用しようとしている。物理的な防潮・造成策には長期的な限界があるため、直後で国を仮想空間に再現する計画へ移っている→正解。💡 instead は、直前の対策とは別の手段への転換を示す。",
                        "❌ is planning to construct stronger defenses＝より強固な防御設備を建設する計画を立てている。直後に説明されるのは防潮壁の強化ではなく、仮想的な国家の再現である。",
                        "❌ has stopped all current projects＝現在のすべての事業を中止した。政府はフューチャー・ナウ・プロジェクトを立ち上げており、中止とは反対である。",
                        "❌ has requested help from other nations＝ほかの国々に支援を要請した。オーストラリアとの移住協定は述べられるが、ここで説明される対応は他国への支援要請ではない。",
                    ],
                    "sourceEvidence": [
                        "A few years ago, it set up the Future Now Project.",
                        "Part of this project involves creating a virtual reconstruction of the nation.",
                    ],
                },
                {
                    "number": 24,
                    "choices": [
                        "is no longer necessary",
                        "should not take long to complete",
                        "will not only benefit Tuvalu",
                        "has no clear purpose",
                    ],
                    "answer": 3,
                    "choiceTranslations": [
                        "もはや必要ではない",
                        "完了まで長くはかからないはずだ",
                        "ツバルだけに利益をもたらすのではない",
                        "明確な目的がない",
                    ],
                    "choiceAnalysis": [
                        "❌ is no longer necessary＝もはや必要ではない。政府は国家存続のために計画を進めており、不要だとは述べていない。",
                        "❌ should not take long to complete＝完了まで長くはかからないはずだ。完成時期や所要時間についての情報は本文にない。",
                        "✅ will not only benefit Tuvalu＝ツバルだけに利益をもたらすのではない。新たな国家のあり方は、同じ海面上昇の脅威に直面するほかの島国の存続にも役立ちうる→正解。💡 空所後の This がプロジェクトと新しい国家の仕組みを受け、他国への波及効果を示す。",
                        "❌ has no clear purpose＝明確な目的がない。領土と住民の要件を仮想的に満たして国家を存続させるという目的が明示されている。",
                    ],
                    "sourceEvidence": [
                        "This could also help to ensure the survival of other island nations facing similar threats from the sea."
                    ],
                },
            ],
        },
    ],
}


def main() -> None:
    if not DATA_PATH.is_file():
        raise SystemExit(
            f"Base data is missing: {DATA_PATH}. Run gen_pre1_2026-1.py before this generator."
        )

    with DATA_PATH.open(encoding="utf-8") as source:
        data = json.load(source)

    sections = data.get("sections")
    if not isinstance(sections, list):
        raise SystemExit("Base data must contain a sections array.")

    part1_indexes = [i for i, section in enumerate(sections) if section.get("name") == "大問1"]
    if len(part1_indexes) != 1:
        raise SystemExit(f"Expected exactly one 大問1 section, found {len(part1_indexes)}.")

    retained = [section for section in sections if section.get("name") != "大問2"]
    part1_index = next(i for i, section in enumerate(retained) if section.get("name") == "大問1")
    retained.insert(part1_index + 1, SECTION2)

    part2_index = next(i for i, section in enumerate(retained) if section.get("name") == "大問2")
    part3_indexes = [i for i, section in enumerate(retained) if section.get("name") == "大問3"]
    if part3_indexes and part2_index >= min(part3_indexes):
        raise SystemExit("Internal error: 大問2 must be placed before 大問3.")

    data["sections"] = retained
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as target:
        json.dump(data, target, ensure_ascii=False, indent=2)
        target.write("\n")

    print(f"Wrote {DATA_PATH}")
    print("大問2: 2 passages / 6 questions (Q19-Q24)")


if __name__ == "__main__":
    main()
