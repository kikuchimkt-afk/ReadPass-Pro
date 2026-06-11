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
                "エル・ピタルはホンジュラスの農村の村です。この国の多くの地域と同様、そこは( 18 )に直面していました。地域社会では識字率が低く、本にアクセスできる生徒はほとんどいませんでした。この問題を解決するため、ある芸術家と若者たちが協力して、ビブリオバンディード（Bibliobandido）という特別なキャラクターを考案しました。子どもたちが読み書きを楽しめるようにするためです。このキャラクターは仮面をかぶり、村を回りました。子どもたちには、自分たちの物語を「食べさせて」やらないと彼はお腹が空くと言われました。これに動機づけられ、子どもたちは物語を書き始めました。",
                "子どもたちにビブリオバンディードが本当にいると信じさせる努力がなされました。衣装が作られ、うわさが広められ、劇的な場面が演じられて、彼を生きた存在のようにしました。ある訪問の際、ビブリオバンディードは馬に乗って村に現れ、子どもたちは1時間以内に新しい物語を作るよう求められ、彼が飢え死にしないようにしました。この活動は作文という課題を刺激的な地域イベントに変えました。これは( 19 )ことができたからです。彼らの努力はさまざまな年齢の人々を一堂に集めました。",
                "ビブリオバンディードの物語は他の地域に広がり、興味深い展開をもたらしました。北米では、アイデアはさまざまな場所や文化に合わせて変更されました。例えばニューヨークでは、ラ・ダマ・ビオレタ（La Dama Violeta）という女性キャラクターが地下鉄のスーパーヒーローとして作られました。彼女は乗客が読んでいる新聞や本をビブリオバンディードに盗まれるのから守りました。( 20 )、このキャラクターは移動中の公共の読書に創造的なひねりを加え、読書の喜びを人々に思い出させました。",
            ],
            "sentencePairs": [
                [
                    "Literacy rates were low in the community, and few students had access to books.",
                    "地域社会では識字率が低く、本にアクセスできる生徒はほとんどいませんでした。",
                ],
                [
                    "To solve this problem, an artist and young people worked together to invent a special character named Bibliobandido.",
                    "この問題を解決するため、ある芸術家と若者たちが協力して、ビブリオバンディードという特別なキャラクターを考案しました。",
                ],
                [
                    "Children were told that he would get hungry unless they fed him their stories.",
                    "子どもたちには、自分たちの物語を「食べさせて」やらないと彼はお腹が空くと言われました。",
                ],
                [
                    "Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life.",
                    "衣装が作られ、うわさが広められ、劇的な場面が演じられて、彼を生きた存在のようにしました。",
                ],
                [
                    "This activity turned a writing task into an exciting community event.",
                    "この活動は作文という課題を刺激的な地域イベントに変えました。",
                ],
                [
                    "Their efforts brought people of different ages together.",
                    "彼らの努力はさまざまな年齢の人々を一堂に集めました。",
                ],
                [
                    "in New York, a female character called La Dama Violeta was created as a subway superhero.",
                    "ニューヨークでは、ラ・ダマ・ビオレタという女性キャラクターが地下鉄のスーパーヒーローとして作られました。",
                ],
                [
                    "this character added a creative twist to public reading while traveling and reminded people of the joy of reading.",
                    "このキャラクターは移動中の公共の読書に創造的なひねりを加え、読書の喜びを人々に思い出させました。",
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
                        "❌ a decline in the number of children＝子ども数の減少。children began writing stories（子どもが物語を書き始めた）とあり、子ども数減少とは読めない",
                        "❌ the loss of safe school routes＝安全な通学路の喪失。El Pital is a rural village（農村の村）の識字・読書の問題が論点で、通学路の話は出てこない",
                        "❌ poor cooperation among villagers＝村人の協力不足。an artist and young people worked together（芸術家と若者が協力）と記述が食い違う",
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
                        "❌ almost no children waited to meet him＝会うのを待たなかった。Motivated by this, children began writing stories（子どもが物語を書き始めた）と記述が逆",
                        "❌ several students talked about the costumes＝衣装について話した。Costumes were created（衣装を作った）などの裏方作業がポイントで、「話した」だけではない",
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
                "恐怖は、人々を危険から守るのに役立つ自然な感情です。危険な動物を見たり、突然大きな音を聞いたりすると、恐怖はすぐに脳に反応させ、体にメッセージを送ります。この反応は、心拍数の上昇、呼吸の速さ、筋肉の緊張などの変化を引き起こします。これらの変化は( 21 )。これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。恐怖は何百万年もの間、人類の生存を助けてきました。",
                "時には、人々は本当の危険に直面していなくても恐怖を感じます。例えば、安全な場所にいるにもかかわらず、映画の怖い場面を見て怖がる人もいます。脳は記憶や過去の経験を使って危険を予測し恐怖を生み、体を強く反応させ、より警戒状態にします。ある人々は( 22 )。彼らは怖いものが好きで、興奮を求めます。これは多くの人がジェットコースターに乗るなどの活動を楽しむ理由も説明します。",
                "しかし、恐怖は常に楽しいわけではありません。恐怖を感じすぎたり、強く感じすぎたりする人もいます。そのような場合、脳は普通の出来事を危険だと扱い、問題につながることがあります。( 23 )、この強い恐怖は日常生活を圧倒的で困難に感じさせることがあります。最近の研究では、学習した恐怖をコントロールできる特定の脳の仕組みが特定され、より効果的な治療への希望が示されています。現在、科学者たちは脳で恐怖がどのように生じるかを研究し、それに苦しむ人々のための解決策を探しています。",
            ],
            "sentencePairs": [
                [
                    "This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles.",
                    "この反応は、心拍数の上昇、呼吸の速さ、筋肉の緊張などの変化を引き起こします。",
                ],
                [
                    "This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately.",
                    "これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。",
                ],
                [
                    "The brain uses memories and past experiences to predict possible danger and generate fear, causing the body to react strongly and become more alert.",
                    "脳は記憶や過去の経験を使って危険を予測し恐怖を生み、体を強く反応させ、より警戒状態にします。",
                ],
                [
                    "They like scary things and seek excitement.",
                    "彼らは怖いものが好きで、興奮を求めます。",
                ],
                [
                    "Some people feel fear too often or too intensely.",
                    "恐怖を感じすぎたり、強く感じすぎたりする人もいます。",
                ],
                [
                    "the brain treats normal events as dangerous, which can lead to problems.",
                    "脳は普通の出来事を危険だと扱い、問題につながることがあります。",
                ],
                [
                    "Recent studies have identified specific brain mechanisms that allow people to control learned fears, offering hope for more effective treatments.",
                    "最近の研究では、学習した恐怖をコントロールできる特定の脳の仕組みが特定され、より効果的な治療への希望が示されています。",
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
                        "人を逃げるか防御する準備をさせる",
                        "人の体の動きを止める",
                        "怖がらないふりをさせる",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ make people feel sleepy and calm＝眠く穏やかにさせる。a faster heart rate, quicker breathing, and tense muscles（心拍上昇・筋肉緊張）という覚醒反応と正反対",
                        "✅ prepare people for escape or defense＝逃げるか防御の準備。fight-or-flight response（闘争・逃走反応）＋gets the body ready to act immediately（すぐ行動できるようにする）と一致→正解",
                        "❌ stop people from moving their bodies＝体の動きを止める。gets the body ready to act immediately（すぐ行動できるようにする）と記述が食い違う",
                        "❌ help people pretend they are not scared＝怖がらないふりをさせる。Fear is a natural emotion that helps protect people from danger（危険から守る感情）という本質と逆",
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
                        "❌ are often afraid of opening their eyes＝目を開けるのを怖がる。watch a scary scene in a movie（映画の怖い場面を見る）とあり、「目を開けない」話ではない",
                        "❌ forget fear soon after it happens＝すぐに恐怖を忘れる。seek excitement（興奮を求める）・enjoy activities such as riding roller coasters（ジェットコースターを楽しむ）と逆",
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
                        "❌ Without this＝これがなければ。the brain treats normal events as dangerous（普通の出来事を危険と扱う）のあとに先行詞のない Without this は不自然",
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
