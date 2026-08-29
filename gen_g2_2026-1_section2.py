# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級 data.json
Step B: 大問2（passage-fill型）Q18〜23
  2A Efforts at a Village / 2B The Science of Fear
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文 A, B を読み、その文意にそって (18) から (23) までの ( ) に入れるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Efforts at a Village",
            "paragraphs": [
                "El Pital is a rural village in Honduras. Like many places in this country, it faced ( 18 ). Literacy rates were low in the community, and few students had access to books. To solve this problem, an artist and young people worked together to invent a special character named Bibliobandido. They did this to help children enjoy learning to read and write. This character wore a mask and went around the village. Children were told that he would get hungry unless they fed him their stories. Motivated by this, children began writing stories.",
                "Efforts were made to make children believe that Bibliobandido was real. Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life. During one visit, Bibliobandido appeared in the village on a horse, and children were asked to create new stories within an hour so that he would not starve. This activity turned a writing task into an exciting community event. This was possible because ( 19 ) to make the event successful. Their efforts brought people of different ages together.",
                "The story of Bibliobandido spread to other places and led to some interesting developments. In North America, the idea was changed to fit different places and cultures. For example, in New York, a female character called La Dama Violeta was created as a subway superhero. She protected passengers from having the newspapers and books they were reading stolen by Bibliobandido. ( 20 ), this character added a creative twist to public reading while traveling and reminded people of the joy of reading.",
            ],
            "translations": [
                "エル・ピタルはホンジュラスの農村です。この国の多くの地域と同様、そこは( 18 )に直面していました。地域社会では識字率が低く、本を利用できる生徒はほとんどいませんでした。この問題を解決するため、ある芸術家と若者たちが協力して、ビブリオバンディード（Bibliobandido）という特別なキャラクターを考案しました。子どもたちが読み書きを楽しめるようにするためです。このキャラクターは仮面をかぶり、村を回りました。子どもたちは、自分たちの物語を彼に「食べさせ」なければ、彼がお腹を空かせると言われました。これに促され、子どもたちは物語を書き始めました。",
                "子どもたちにビブリオバンディードが本当にいると信じさせるための取り組みが行われました。衣装が作られ、うわさが広められ、劇的な場面が演じられて、彼を本当に生きているかのように見せました。ある訪問の際、ビブリオバンディードは馬に乗って村に現れました。そして子どもたちは、彼を飢えさせないよう、1時間以内に新しい物語を作るよう求められました。この活動は作文という課題を刺激的な地域イベントに変えました。この活動が可能だったのは、イベントを成功させるために( 19 )からです。彼らの努力はさまざまな年齢の人々を結びつけました。",
                "ビブリオバンディードの物語は他の地域に広がり、興味深い展開をもたらしました。北米では、このアイデアがさまざまな場所や文化に合うように変えられました。例えばニューヨークでは、ラ・ダマ・ビオレタ（La Dama Violeta）という女性キャラクターが地下鉄のスーパーヒーローとして生み出されました。彼女は、乗客が読んでいる新聞や本をビブリオバンディードに盗まれないよう守りました。( 20 )、このキャラクターは、移動中に公共の場で本を読むことに創造的な工夫を加え、読書の喜びを人々に思い出させました。",
            ],
            "sentencePairs": [
                [
                    "El Pital is a rural village in Honduras.",
                    "エル・ピタルはホンジュラスの農村です。",
                    "El Pital|エル・ピタルは||is a rural village in Honduras.|ホンジュラスにある農村です。",
                    "is",
                ],
                [
                    "Like many places in this country, it faced ( 18 ).",
                    "この国の多くの地域と同様、そこは( 18 )に直面していました。",
                    "Like many places in this country,|この国の多くの地域と同様、||it faced|そこは直面していました||( 18 ).|( 18 )に。",
                    "faced",
                ],
                [
                    "Literacy rates were low in the community, and few students had access to books.",
                    "地域社会では識字率が低く、本を利用できる生徒はほとんどいませんでした。",
                    "Literacy rates were low|識字率は低く||in the community,|地域社会では、||and few students had access to books.|そして本を利用できる生徒はほとんどいませんでした。",
                    "were",
                ],
                [
                    "To solve this problem, an artist and young people worked together to invent a special character named Bibliobandido.",
                    "この問題を解決するため、ある芸術家と若者たちが協力して、ビブリオバンディードという特別なキャラクターを考案しました。",
                    "To solve this problem,|この問題を解決するため、||an artist and young people|ある芸術家と若者たちが||worked together|協力しました||to invent a special character named Bibliobandido.|ビブリオバンディードという特別なキャラクターを考案するために。",
                    "worked",
                ],
                [
                    "They did this to help children enjoy learning to read and write.",
                    "子どもたちが読み書きを楽しめるようにするためです。",
                    "They did this|彼らがそうしたのは||to help children enjoy|子どもたちが楽しめるようにするためです||learning to read and write.|読み書きを学ぶことを。",
                    "did",
                ],
                [
                    "This character wore a mask and went around the village.",
                    "このキャラクターは仮面をかぶり、村を回りました。",
                    "This character|このキャラクターは||wore a mask|仮面をかぶり||and went around the village.|村を回りました。",
                    "wore",
                ],
                [
                    "Children were told that he would get hungry unless they fed him their stories.",
                    "子どもたちは、自分たちの物語を彼に「食べさせ」なければ、彼がお腹を空かせると言われました。",
                    "Children were told|子どもたちは言われました||that he would get hungry|彼がお腹を空かせると||unless they fed him their stories.|自分たちの物語を彼に食べさせなければ。",
                    "were told",
                ],
                [
                    "Motivated by this, children began writing stories.",
                    "これに促され、子どもたちは物語を書き始めました。",
                    "Motivated by this,|これに促され、||children began writing stories.|子どもたちは物語を書き始めました。",
                    "began",
                ],
                [
                    "Efforts were made to make children believe that Bibliobandido was real.",
                    "子どもたちにビブリオバンディードが本当にいると信じさせるための取り組みが行われました。",
                    "Efforts were made|取り組みが行われました||to make children believe|子どもたちに信じさせるための||that Bibliobandido was real.|ビブリオバンディードが本当にいると。",
                    "were made",
                ],
                [
                    "Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life.",
                    "衣装が作られ、うわさが広められ、劇的な場面が演じられて、彼を本当に生きているかのように見せました。",
                    "Costumes were created,|衣装が作られ、||rumors were spread,|うわさが広められ、||and dramatic scenes were performed|劇的な場面が演じられました||to bring him to life.|彼を本当に生きているかのように見せるために。",
                    "were created",
                ],
                [
                    "During one visit, Bibliobandido appeared in the village on a horse, and children were asked to create new stories within an hour so that he would not starve.",
                    "ある訪問の際、ビブリオバンディードは馬に乗って村に現れました。そして子どもたちは、彼を飢えさせないよう、1時間以内に新しい物語を作るよう求められました。",
                    "During one visit,|ある訪問の際、||Bibliobandido appeared|ビブリオバンディードは現れました||in the village on a horse,|馬に乗って村に、||and children were asked|そして子どもたちは求められました||to create new stories within an hour|1時間以内に新しい物語を作るよう||so that he would not starve.|彼が飢えないように。",
                    "appeared",
                ],
                [
                    "This activity turned a writing task into an exciting community event.",
                    "この活動は作文という課題を刺激的な地域イベントに変えました。",
                    "This activity|この活動は||turned a writing task|作文という課題を変えました||into an exciting community event.|刺激的な地域イベントに。",
                    "turned",
                ],
                [
                    "This was possible because ( 19 ) to make the event successful.",
                    "この活動が可能だったのは、イベントを成功させるために( 19 )からです。",
                    "This was possible|この活動が可能だったのは||because ( 19 ) to make the event successful.|イベントを成功させるために( 19 )からです。",
                    "was",
                ],
                [
                    "Their efforts brought people of different ages together.",
                    "彼らの努力はさまざまな年齢の人々を結びつけました。",
                    "Their efforts|彼らの努力は||brought people of different ages together.|さまざまな年齢の人々を結びつけました。",
                    "brought",
                ],
                [
                    "The story of Bibliobandido spread to other places and led to some interesting developments.",
                    "ビブリオバンディードの物語は他の地域に広がり、興味深い展開をもたらしました。",
                    "The story of Bibliobandido|ビブリオバンディードの物語は||spread to other places|他の地域に広がり||and led to some interesting developments.|興味深い展開をもたらしました。",
                    "spread",
                ],
                [
                    "In North America, the idea was changed to fit different places and cultures.",
                    "北米では、このアイデアがさまざまな場所や文化に合うように変えられました。",
                    "In North America,|北米では、||the idea was changed|このアイデアが変えられました||to fit different places and cultures.|さまざまな場所や文化に合うように。",
                    "was changed",
                ],
                [
                    "For example, in New York, a female character called La Dama Violeta was created as a subway superhero.",
                    "例えばニューヨークでは、ラ・ダマ・ビオレタという女性キャラクターが地下鉄のスーパーヒーローとして生み出されました。",
                    "For example, in New York,|例えばニューヨークでは、||a female character|女性キャラクターが||called La Dama Violeta|ラ・ダマ・ビオレタという名の||was created|生み出されました||as a subway superhero.|地下鉄のスーパーヒーローとして。",
                    "was created",
                ],
                [
                    "She protected passengers from having the newspapers and books they were reading stolen by Bibliobandido.",
                    "彼女は、乗客が読んでいる新聞や本をビブリオバンディードに盗まれないよう守りました。",
                    "She protected passengers|彼女は乗客を守りました||from having the newspapers and books they were reading|乗客が読んでいる新聞や本を||stolen by Bibliobandido.|ビブリオバンディードに盗まれることから。",
                    "protected",
                ],
                [
                    "( 20 ), this character added a creative twist to public reading while traveling and reminded people of the joy of reading.",
                    "( 20 )、このキャラクターは、移動中に公共の場で本を読むことに創造的な工夫を加え、読書の喜びを人々に思い出させました。",
                    "( 20 ),|( 20 )、||this character|このキャラクターは||added a creative twist|創造的な工夫を加え||to public reading while traveling|移動中に公共の場で本を読むことに||and reminded people|そして人々に思い出させました||of the joy of reading.|読書の喜びを。",
                    "added",
                ],
            ],
            "questions": [
                {
                    "number": 18,
                    "choices": [
                        "a lack of educational resources",
                        "a decline in the number of children",
                        "the loss of safe school routes",
                        "poor cooperation among villagers",
                    ],
                    "choiceTranslations": [
                        "教育資源の不足",
                        "子ども数の減少",
                        "安全な通学路の喪失",
                        "村人同士の協力不足",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ a lack of educational resources＝教育資源の不足。Literacy rates were low（識字率が低い）＋few students had access to books（本にアクセスできない）が直接の根拠→正解",
                        "❌ a decline in the number of children＝子ども数の減少。空所直後は low literacy と limited access to books を具体例としており、子どもの人口減少は述べていない",
                        "❌ the loss of safe school routes＝安全な通学路の喪失。空所後に説明されるのは識字率と本の不足で、通学路についての記述はない",
                        "❌ poor cooperation among villagers＝村人の協力不足。問題として示されるのは教育資源の不足であり、後には an artist and young people worked together（協力した）とある",
                    ],
                    "sourceEvidence": [
                        "Literacy rates were low in the community, and few students had access to books.",
                    ],
                    "grammar": "💡 face ～＝～に直面する。空所の直後2文が「何に直面したか」の具体説明。low literacy / few books → educational resources の不足。",
                },
                {
                    "number": 19,
                    "choices": [
                        "many people worked behind the scenes",
                        "some children watched quietly from home",
                        "almost no children waited to meet him",
                        "several students talked about the costumes",
                    ],
                    "choiceTranslations": [
                        "多くの人が舞台裏で働いた",
                        "一部の子どもが家で静かに見ていた",
                        "ほとんどの子どもが会うのを待たなかった",
                        "数人の生徒が衣装について話した",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ many people worked behind the scenes＝多くの人が舞台裏で働いた。Costumes were created, rumors were spread, and dramatic scenes were performed（衣装・うわさ・演出）がイベント成功の理由→正解",
                        "❌ some children watched quietly from home＝家で静かに見ていた。This activity turned a writing task into an exciting community event（地域イベント）と、家で見るだけの描写は合わない",
                        "❌ almost no children waited to meet him＝ほとんどの子どもが会うのを待たなかった。本文には待ったかどうかの記述がなく、イベントを可能にした理由にもならない",
                        "❌ several students talked about the costumes＝数人の生徒が衣装について話した。本文は Costumes were created（衣装が作られた）など複数の準備作業を述べており、衣装について話したとは書かれていない",
                    ],
                    "sourceEvidence": [
                        "Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life.",
                        "This activity turned a writing task into an exciting community event.",
                    ],
                    "grammar": "💡 behind the scenes＝舞台裏で・陰で。This was possible because ～（～があったから可能だった）の空所は、直前の演出描写を受ける。",
                },
                {
                    "number": 20,
                    "choices": [
                        "To begin with",
                        "Unfortunately",
                        "In this way",
                        "On the other hand",
                    ],
                    "choiceTranslations": [
                        "まず第一に",
                        "残念ながら",
                        "このようにして",
                        "一方で",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ To begin with＝まず第一に。For example, in New York（例えばニューヨークでは）の具体例の結果を述べる位置で、話の導入語としては不適切",
                        "❌ Unfortunately＝残念ながら。直後は added a creative twist to public reading（創造的な工夫）という前向きな内容",
                        "✅ In this way＝このようにして。La Dama Violeta was created as a subway superhero（地下鉄のスーパーヒーロー）という工夫の結果をまとめる接続→正解",
                        "❌ On the other hand＝一方で。the idea was changed to fit different places（各地でアイデアが変化）の具体例の効果を述べており、単純な対比ではない",
                    ],
                    "sourceEvidence": [
                        "She protected passengers from having the newspapers and books they were reading stolen by Bibliobandido.",
                        "this character added a creative twist to public reading while traveling and reminded people of the joy of reading.",
                    ],
                    "grammar": "💡 in this way＝このようにして（方法・結果のまとめ）。For example の具体例のあと、それがもたらした効果を接続するパターン。",
                },
            ],
        },
        {
            "label": "B",
            "title": "The Science of Fear",
            "paragraphs": [
                "Fear is a natural emotion that helps protect people from danger. When people see dangerous animals or hear a sudden loud noise, fear quickly makes the brain react and send a message to the body. This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles. These changes ( 21 ). This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately. Fear has been helping humans survive for millions of years.",
                "Sometimes, people feel fear even when they are not facing real danger. For example, some people feel afraid when they watch a scary scene in a movie, although they are in a safe place. The brain uses memories and past experiences to predict possible danger and generate fear, causing the body to react strongly and become more alert. Some people ( 22 ). They like scary things and seek excitement. This also explains why many people enjoy activities such as riding roller coasters.",
                "However, fear is not always enjoyable. Some people feel fear too often or too intensely. In such cases, the brain treats normal events as dangerous, which can lead to problems. ( 23 ), this intense fear can make everyday activities feel overwhelming and difficult. Recent studies have identified specific brain mechanisms that allow people to control learned fears, offering hope for more effective treatments. Currently, scientists are studying how fear is generated in the brain and seeking solutions for those who suffer from it.",
            ],
            "translations": [
                "恐怖は、人々を危険から守るのに役立つ自然な感情です。危険な動物を見たり、突然大きな音を聞いたりすると、恐怖によって脳はすぐに反応し、体へメッセージを送ります。この反応は、心拍数の上昇、呼吸の加速、筋肉の緊張などの変化を引き起こします。これらの変化は( 21 )。これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。恐怖は何百万年もの間、人類の生存を助けてきました。",
                "時には、人々は実際の危険に直面していなくても恐怖を感じます。例えば、安全な場所にいるにもかかわらず、映画の怖い場面を見て恐怖を感じる人もいます。脳は記憶や過去の経験を使って起こり得る危険を予測し、恐怖を生み出すことで、体を強く反応させて警戒を高めます。ある人々は( 22 )。彼らは怖いものが好きで、興奮を求めます。これは、多くの人がジェットコースターに乗るといった活動を楽しむ理由も説明しています。",
                "しかし、恐怖はいつも楽しいものとは限りません。恐怖をあまりに頻繁に、またはあまりに強く感じる人もいます。そのような場合、脳は普通の出来事を危険なものとして扱い、それが問題につながることがあります。( 23 )、この強い恐怖によって、日常の活動が手に負えないほど難しく感じられることがあります。最近の研究では、学習によって身についた恐怖を人が制御できるようにする特定の脳の仕組みが明らかになり、より効果的な治療法への期待が生まれています。現在、科学者たちは脳内で恐怖がどのように生み出されるかを研究し、恐怖に苦しむ人々のための解決策を探しています。",
            ],
            "sentencePairs": [
                [
                    "Fear is a natural emotion that helps protect people from danger.",
                    "恐怖は、人々を危険から守るのに役立つ自然な感情です。",
                    "Fear|恐怖は||is a natural emotion|自然な感情です||that helps protect people|人々を守るのに役立つ||from danger.|危険から。",
                    "is",
                ],
                [
                    "When people see dangerous animals or hear a sudden loud noise, fear quickly makes the brain react and send a message to the body.",
                    "危険な動物を見たり、突然大きな音を聞いたりすると、恐怖によって脳はすぐに反応し、体へメッセージを送ります。",
                    "When people see dangerous animals|人々が危険な動物を見たり||or hear a sudden loud noise,|突然大きな音を聞いたりすると、||fear quickly makes the brain react|恐怖によって脳はすぐに反応し||and send a message to the body.|体へメッセージを送ります。",
                    "makes",
                ],
                [
                    "This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles.",
                    "この反応は、心拍数の上昇、呼吸の加速、筋肉の緊張などの変化を引き起こします。",
                    "This reaction|この反応は||causes changes|変化を引き起こします||such as a faster heart rate,|例えば心拍数の上昇、||quicker breathing,|呼吸の加速、||and tense muscles.|筋肉の緊張などです。",
                    "causes",
                ],
                [
                    "These changes ( 21 ).",
                    "これらの変化は( 21 )。",
                    "These changes|これらの変化は||( 21 ).|( 21 )。",
                    "( 21 )",
                ],
                [
                    "This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately.",
                    "これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。",
                    "This is called the \"fight-or-flight\" response to fear or stress,|これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、||which gets the body ready|体を準備させます||to act immediately.|すぐに行動できるように。",
                    "is called",
                ],
                [
                    "Fear has been helping humans survive for millions of years.",
                    "恐怖は何百万年もの間、人類の生存を助けてきました。",
                    "Fear|恐怖は||has been helping humans survive|人類が生存するのを助けてきました||for millions of years.|何百万年もの間。",
                    "has been helping",
                ],
                [
                    "Sometimes, people feel fear even when they are not facing real danger.",
                    "時には、人々は実際の危険に直面していなくても恐怖を感じます。",
                    "Sometimes,|時には、||people feel fear|人々は恐怖を感じます||even when they are not facing real danger.|実際の危険に直面していないときでさえ。",
                    "feel",
                ],
                [
                    "For example, some people feel afraid when they watch a scary scene in a movie, although they are in a safe place.",
                    "例えば、安全な場所にいるにもかかわらず、映画の怖い場面を見て恐怖を感じる人もいます。",
                    "For example,|例えば、||some people feel afraid|恐怖を感じる人もいます||when they watch a scary scene in a movie,|映画の怖い場面を見ると||although they are in a safe place.|安全な場所にいるにもかかわらず。",
                    "feel",
                ],
                [
                    "The brain uses memories and past experiences to predict possible danger and generate fear, causing the body to react strongly and become more alert.",
                    "脳は記憶や過去の経験を使って起こり得る危険を予測し、恐怖を生み出すことで、体を強く反応させて警戒を高めます。",
                    "The brain uses memories and past experiences|脳は記憶や過去の経験を使います||to predict possible danger|起こり得る危険を予測し||and generate fear,|恐怖を生み出し、||causing the body to react strongly|その結果、体を強く反応させ||and become more alert.|より警戒状態にします。",
                    "uses",
                ],
                [
                    "Some people ( 22 ).",
                    "ある人々は( 22 )。",
                    "Some people|ある人々は||( 22 ).|( 22 )。",
                    "( 22 )",
                ],
                [
                    "They like scary things and seek excitement.",
                    "彼らは怖いものが好きで、興奮を求めます。",
                    "They|彼らは||like scary things|怖いものが好きで||and seek excitement.|興奮を求めます。",
                    "like",
                ],
                [
                    "This also explains why many people enjoy activities such as riding roller coasters.",
                    "これは、多くの人がジェットコースターに乗るといった活動を楽しむ理由も説明しています。",
                    "This also explains|これはまた説明しています||why many people enjoy activities such as riding roller coasters.|多くの人がジェットコースターに乗るといった活動を楽しむ理由を。",
                    "explains",
                ],
                [
                    "However, fear is not always enjoyable.",
                    "しかし、恐怖はいつも楽しいものとは限りません。",
                    "However,|しかし、||fear|恐怖は||is not always enjoyable.|いつも楽しいものとは限りません。",
                    "is",
                ],
                [
                    "Some people feel fear too often or too intensely.",
                    "恐怖をあまりに頻繁に、またはあまりに強く感じる人もいます。",
                    "Some people|人によっては||feel fear|恐怖を感じます||too often|あまりに頻繁に||or too intensely.|またはあまりに強く。",
                    "feel",
                ],
                [
                    "In such cases, the brain treats normal events as dangerous, which can lead to problems.",
                    "そのような場合、脳は普通の出来事を危険なものとして扱い、それが問題につながることがあります。",
                    "In such cases,|そのような場合、||the brain treats normal events|脳は普通の出来事を扱います||as dangerous,|危険なものとして、||which can lead to problems.|そしてそれが問題につながることがあります。",
                    "treats",
                ],
                [
                    "( 23 ), this intense fear can make everyday activities feel overwhelming and difficult.",
                    "( 23 )、この強い恐怖によって、日常の活動が手に負えないほど難しく感じられることがあります。",
                    "( 23 ),|( 23 )、||this intense fear|この強い恐怖は||can make everyday activities feel overwhelming and difficult.|日常の活動を手に負えず困難だと感じさせることがあります。",
                    "can make",
                ],
                [
                    "Recent studies have identified specific brain mechanisms that allow people to control learned fears, offering hope for more effective treatments.",
                    "最近の研究では、学習によって身についた恐怖を人が制御できるようにする特定の脳の仕組みが明らかになり、より効果的な治療法への期待が生まれています。",
                    "Recent studies|最近の研究は||have identified specific brain mechanisms|特定の脳の仕組みを明らかにしました||that allow people to control learned fears,|学習による恐怖を人が制御できるようにする||offering hope for more effective treatments.|より効果的な治療法への期待をもたらしています。",
                    "have identified",
                ],
                [
                    "Currently, scientists are studying how fear is generated in the brain and seeking solutions for those who suffer from it.",
                    "現在、科学者たちは脳内で恐怖がどのように生み出されるかを研究し、恐怖に苦しむ人々のための解決策を探しています。",
                    "Currently,|現在、||scientists are studying|科学者たちは研究しています||how fear is generated in the brain|脳内で恐怖がどのように生み出されるかを||and seeking solutions for those who suffer from it.|そして恐怖に苦しむ人々のための解決策を探しています。",
                    "are studying",
                ],
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "make people feel sleepy and calm",
                        "prepare people for escape or defense",
                        "stop people from moving their bodies",
                        "help people pretend they are not scared",
                    ],
                    "choiceTranslations": [
                        "人を眠く穏やかにさせる",
                        "人が逃走または防御できる態勢を整える",
                        "人の体の動きを止める",
                        "怖がらないふりをさせる",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ make people feel sleepy and calm＝眠く穏やかにさせる。a faster heart rate, quicker breathing, and tense muscles（心拍上昇・筋肉緊張）という覚醒反応と正反対",
                        "✅ prepare people for escape or defense＝逃走または防御の態勢を整える。fight-or-flight response（闘争・逃走反応）＋gets the body ready to act immediately（すぐ行動できるようにする）と一致→正解",
                        "❌ stop people from moving their bodies＝体の動きを止める。gets the body ready to act immediately（すぐ行動できるようにする）と記述が食い違う",
                        "❌ help people pretend they are not scared＝怖がらないふりをさせる。直後は体をすぐ行動できる状態にする反応の説明であり、恐怖を隠す行動については述べていない",
                    ],
                    "sourceEvidence": [
                        "This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately.",
                    ],
                    "grammar": "💡 fight-or-flight＝闘争か逃走。空所の直後がこの反応の定義文。prepare for escape or defense がその言い換え。",
                },
                {
                    "number": 22,
                    "choices": [
                        "are even fascinated by this feeling",
                        "are often afraid of opening their eyes",
                        "forget fear soon after it happens",
                        "love surprising their friends and family",
                    ],
                    "choiceTranslations": [
                        "この感情にさえ夢中になっている",
                        "目を開けるのを怖がることが多い",
                        "恐怖をすぐに忘れる",
                        "友人や家族を驚かせるのが好き",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ are even fascinated by this feeling＝この感情に夢中。直後の They like scary things and seek excitement（怖いものが好きで興奮を求める）が言い換え→正解",
                        "❌ are often afraid of opening their eyes＝目を開けるのを怖がる。本文は怖いものを好んで興奮を求める人を説明しており、目を開けることへの恐怖は述べていない",
                        "❌ forget fear soon after it happens＝すぐに恐怖を忘れる。直後は They like scary things and seek excitement とその感情への関心を説明しており、恐怖を忘れる話ではない",
                        "❌ love surprising their friends and family＝友人を驚かせる。riding roller coasters（ジェットコースター）など自己の興奮の話で、他人を驚かせる内容は出てこない",
                    ],
                    "sourceEvidence": [
                        "They like scary things and seek excitement.",
                        "This also explains why many people enjoy activities such as riding roller coasters.",
                    ],
                    "grammar": "💡 be fascinated by ～＝～に夢中になる。Some people ( ) の空所は直後の They like scary things で説明される。",
                },
                {
                    "number": 23,
                    "choices": [
                        "On the other hand",
                        "Fortunately",
                        "Without this",
                        "In particular",
                    ],
                    "choiceTranslations": [
                        "一方で",
                        "幸いにも",
                        "これがなければ",
                        "特に",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ On the other hand＝一方で。Some people feel fear too often or too intensely（恐怖を感じすぎる人）の具体化であり、前段との単純な対比ではない",
                        "❌ Fortunately＝幸いにも。直後の this intense fear can make everyday activities feel overwhelming and difficult（日常生活が困難に）という否定的内容",
                        "❌ Without this＝これがなければ。直前の『普通の出来事を危険と扱うこと』がなければ強い恐怖が日常生活を困難にする、という因果になり、文意がつながらない",
                        "✅ In particular＝特に。too often or too intensely（頻繁・過度に恐怖）のケースを強調し、日常生活への影響を述べる→正解",
                    ],
                    "sourceEvidence": [
                        "Some people feel fear too often or too intensely.",
                        "this intense fear can make everyday activities feel overwhelming and difficult.",
                    ],
                    "grammar": "💡 in particular＝特に（特定の場合を際立たせる）。too often or too intensely のあと、具体的な影響を強調する接続。",
                },
            ],
        },
    ],
}

# 2025年度の2級データと同じ表示規約にそろえる。
for passage in section2["passages"]:
    for question in passage["questions"]:
        normalized = []
        for index, analysis in enumerate(question["choiceAnalysis"], 1):
            analysis = analysis.removeprefix("✅ ").removeprefix("❌ ")
            if index == question["answer"]:
                analysis = analysis.replace("→正解。💡", "→正解").replace(
                    "→正解", "→正解。💡"
                )
            normalized.append(analysis)
        question["choiceAnalysis"] = normalized

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

others = [s for s in data.get("sections", []) if s.get("name") != "大問2"]
# 大問1を先頭に、大問2を差し替え、大問3以降を保持
s1 = next((s for s in data.get("sections", []) if s.get("name") == "大問1"), None)
rest = [s for s in others if s.get("name") != "大問1"]
data["sections"] = ([s1] if s1 else []) + [section2] + rest

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 大問2リッチ解説を保存: {DATA_PATH}")
print(f"   パッセージ: {len(section2['passages'])} / 問題: 6")
