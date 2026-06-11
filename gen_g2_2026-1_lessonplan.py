# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級 data.json
Step D: lessonPlan（focusPoints × 5）
本文中に実在する構文のみを使用。practicePassage は試験本文の抜粋＋[出典: タイトル]。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "fight-or-flight と恐怖の身体反応",
    "subtitle": "Fear Response: fight-or-flight & Body Changes",
    "explanation": (
        "大問2B「The Science of Fear」では、恐怖が脳と体に与える変化を科学的に説明しています。"
        "a faster heart rate, quicker breathing, and tense muscles という3つの変化のあとに空所(21)があり、"
        "直後の This is called the \"fight-or-flight\" response ... gets the body ready to act immediately が正解 prepare people for escape or defense の定義文です。"
        "第2段落では映画やジェットコースターなど「安全なのに怖がる」「怖いものを楽しむ」人々の話へ展開し、"
        "第3段落の Some people feel fear too often or too intensely で問題のある恐怖へ話題を絞ります。"
        "空所問題では「直後の定義文」「They like scary things などの言い換え」が最大の手がかりになります。"
    ),
    "sourceQuote": "a faster heart rate, quicker breathing, and tense muscles / fight-or-flight response / gets the body ready to act immediately / They like scary things and seek excitement",
    "sourceLocation": "大問2B「The Science of Fear」第1〜2段落",
    "examples": [
        {
            "en": "This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles.",
            "ja": "この反応は、心拍数の上昇、呼吸の速さ、筋肉の緊張などの変化を引き起こします。",
            "note": "such as A, B, and C＝「A・B・Cなど」。恐怖反応の具体的変化を列挙。Q21空所の直前。",
        },
        {
            "en": "This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately.",
            "ja": "これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。",
            "note": "be called ～＝「～と呼ばれる」。which gets the body ready ...＝非制限用法で補足説明。Q21の決め手。",
        },
        {
            "en": "Some people are even fascinated by this feeling. They like scary things and seek excitement.",
            "ja": "ある人々はこの感情にさえ夢中になっています。彼らは怖いものが好きで、興奮を求めます。",
            "note": "be fascinated by ～＝「～に夢中」。They like ... and seek ... が Q22 正解の言い換え。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: The Science of Fear]\n"
            "Fear is a natural emotion that helps protect people from danger. When people see dangerous animals or hear a sudden loud noise, fear quickly makes the brain react and send a message to the body. This reaction causes changes such as a faster heart rate, quicker breathing, and tense muscles. These changes prepare people for escape or defense. This is called the \"fight-or-flight\" response to fear or stress, which gets the body ready to act immediately. Fear has been helping humans survive for millions of years.\n"
            "Sometimes, people feel fear even when they are not facing real danger. For example, some people feel afraid when they watch a scary scene in a movie, although they are in a safe place. The brain uses memories and past experiences to predict possible danger and generate fear, causing the body to react strongly and become more alert. Some people are even fascinated by this feeling. They like scary things and seek excitement. This also explains why many people enjoy activities such as riding roller coasters."
        ),
        "ja": (
            "恐怖は、人々を危険から守るのに役立つ自然な感情です。危険な動物を見たり、突然大きな音を聞いたりすると、恐怖はすぐに脳に反応させ、体にメッセージを送ります。この反応は、心拍数の上昇、呼吸の速さ、筋肉の緊張などの変化を引き起こします。これらの変化は人を逃げるか防御する準備をさせます。これは恐怖やストレスに対する「闘争・逃走反応」と呼ばれ、体をすぐに行動できる状態にします。恐怖は何百万年もの間、人類の生存を助けてきました。\n"
            "時には、人々は本当の危険に直面していなくても恐怖を感じます。例えば、安全な場所にいるにもかかわらず、映画の怖い場面を見て怖がる人もいます。脳は記憶や過去の経験を使って危険を予測し恐怖を生み、体を強く反応させ、より警戒状態にします。ある人々はこの感情にさえ夢中になっています。彼らは怖いものが好きで、興奮を求めます。これは多くの人がジェットコースターに乗るなどの活動を楽しむ理由も説明します。"
        ),
        "audioFile": "audio/practice_pp1.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q21の空所に prepare people for escape or defense が入る理由を、直後の fight-or-flight の説明から述べてください。",
            "a": "gets the body ready to act immediately（すぐ行動できるようにする）＝逃げるか防御する準備。make people feel sleepy / stop people from moving などは定義文と正反対。",
        },
        {
            "q": "Q22で They like scary things and seek excitement が正解になる根拠文を本文から抜き出し、are fascinated by this feeling との関係を説明してください。",
            "a": "Some people ( ) の直後が They like scary things and seek excitement。空所 are even fascinated by this feeling はその言い換え・具体化。",
        },
        {
            "q": "「although they are in a safe place」の although は何と何を対比していますか？",
            "a": "feel afraid when they watch a scary scene in a movie（怖い場面で怖がる）と in a safe place（安全な場所にいる）の対比。「実際の危険はないのに怖がる」状況を示す。",
        },
        {
            "q": "Q23で In particular が選ばれる理由を、too often or too intensely との関係で説明してください。",
            "a": "前文で頻繁・過度の恐怖を述べたあと、特に日常生活への影響（overwhelming and difficult）を強調する接続。On the other hand は別グループとの対比、Fortunately は否定的内容と合わない。",
        },
    ],
    "highlightPatterns": [
        "a faster heart rate, quicker breathing, and tense muscles",
        "fight-or-flight",
        "gets the body ready to act immediately",
        "They like scary things and seek excitement",
        "Some people feel fear too often or too intensely",
        "riding roller coasters",
        "Recent studies have identified specific brain mechanisms",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "恐怖反応",
}

fp2 = {
    "id": "fp2",
    "title": "Motivated by / Efforts were made（動機づけと舞台裏の努力）",
    "subtitle": "Motivation & Behind-the-Scenes Efforts in Community Events",
    "explanation": (
        "大問2A「Efforts at a Village」は、識字率の低さという問題→Bibliobandido という仕掛け→子どもの作文を促す→地域イベント化、という流れです。"
        "Motivated by this（これに動機づけられて）は直前の fed him their stories（物語を食べさせる）という仕掛けを受けます。"
        "Efforts were made to make children believe ... のあと、Costumes were created, rumors were spread, and dramatic scenes were performed と舞台裏の準備が列挙され、"
        "Q19の many people worked behind the scenes（多くの人が舞台裏で働いた）の根拠になります。"
        "Q18は Literacy rates were low と few students had access to books から a lack of educational resources を導く典型パターンです。"
    ),
    "sourceQuote": "Motivated by this, children began writing stories / Efforts were made to make children believe / Costumes were created, rumors were spread / Their efforts brought people of different ages together",
    "sourceLocation": "大問2A「Efforts at a Village」第1〜2段落",
    "examples": [
        {
            "en": "Literacy rates were low in the community, and few students had access to books.",
            "ja": "地域社会では識字率が低く、本にアクセスできる生徒はほとんどいませんでした。",
            "note": "Q18の根拠。low literacy ＋ few access to books → lack of educational resources の言い換え。",
        },
        {
            "en": "Children were told that he would get hungry unless they fed him their stories. Motivated by this, children began writing stories.",
            "ja": "子どもたちには物語を「食べさせて」やらないと彼はお腹が空くと言われました。これに動機づけられ、子どもたちは物語を書き始めました。",
            "note": "unless ～＝「～しないと」。Motivated by this の this は直前の仕掛け全体を指す。",
        },
        {
            "en": "Efforts were made to make children believe that Bibliobandido was real. Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life.",
            "ja": "子どもたちにビブリオバンディードが本当にいると信じさせる努力がなされました。衣装が作られ、うわさが広められ、劇的な場面が演じられました。",
            "note": "Efforts were made to V＝「Vする努力がなされた」。受動態で主体をぼかす表現。Q19の裏付け。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Efforts at a Village]\n"
            "El Pital is a rural village in Honduras. Like many places in this country, it faced a lack of educational resources. Literacy rates were low in the community, and few students had access to books. To solve this problem, an artist and young people worked together to invent a special character named Bibliobandido. They did this to help children enjoy learning to read and write. Children were told that he would get hungry unless they fed him their stories. Motivated by this, children began writing stories.\n"
            "Efforts were made to make children believe that Bibliobandido was real. Costumes were created, rumors were spread, and dramatic scenes were performed to bring him to life. During one visit, Bibliobandido appeared in the village on a horse, and children were asked to create new stories within an hour so that he would not starve. This activity turned a writing task into an exciting community event. This was possible because many people worked behind the scenes to make the event successful. Their efforts brought people of different ages together."
        ),
        "ja": (
            "エル・ピタルはホンジュラスの農村の村です。この国の多くの地域と同様、そこは教育資源の不足に直面していました。地域社会では識字率が低く、本にアクセスできる生徒はほとんどいませんでした。この問題を解決するため、ある芸術家と若者たちが協力して、ビブリオバンディードという特別なキャラクターを考案しました。子どもたちが読み書きを楽しめるようにするためです。子どもたちには物語を「食べさせて」やらないと彼はお腹が空くと言われました。これに動機づけられ、子どもたちは物語を書き始めました。\n"
            "子どもたちにビブリオバンディードが本当にいると信じさせる努力がなされました。衣装が作られ、うわさが広められ、劇的な場面が演じられて、彼を生きた存在のようにしました。ある訪問の際、ビブリオバンディードは馬に乗って村に現れ、子どもたちは1時間以内に新しい物語を作るよう求められました。この活動は作文という課題を刺激的な地域イベントに変えました。多くの人が舞台裏で働いたからこそ、イベントは成功しました。彼らの努力はさまざまな年齢の人々を一堂に集めました。"
        ),
        "audioFile": "audio/practice_pp2.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q18で a lack of educational resources を選ぶ手順を、空所の前後2文から説明してください。",
            "a": "it faced (18) の直後が Literacy rates were low ＋ few students had access to books。「識字率の低さ」「本へのアクセス不足」→教育資源の不足。",
        },
        {
            "q": "Q19で Costumes were created, rumors were spread ... と many people worked behind the scenes はどう結びつきますか？",
            "a": "衣装作り・うわさ・演出は「舞台裏での準備作業」。This was possible because の空所に「多くの人が陰で協力した」が入る。",
        },
        {
            "q": "「turned a writing task into an exciting community event」の into は何を表しますか？",
            "a": "turn A into B＝「AをBに変える」。退屈な作文課題→刺激的な地域イベントへの変化。Bibliobandido 仕掛けの効果。",
        },
        {
            "q": "Q20で In this way が選ばれる理由を、ニューヨーク版の具体例と直後の文から説明してください。",
            "a": "La Dama Violeta という工夫（地下鉄のスーパーヒーロー）によって、public reading に creative twist を加えた「方法・結果」を In this way でまとめる。",
        },
    ],
    "highlightPatterns": [
        "Literacy rates were low in the community",
        "few students had access to books",
        "Motivated by this, children began writing stories",
        "Efforts were made to make children believe that Bibliobandido was real",
        "Costumes were created, rumors were spread, and dramatic scenes were performed",
        "turned a writing task into an exciting community event",
        "Their efforts brought people of different ages together",
        "reminded people of the joy of reading",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "動機・努力",
}

fp3 = {
    "id": "fp3",
    "title": "施設問い合わせメールの丁寧表現（Could you please / It would be great if / Therefore）",
    "subtitle": "Polite Facility Inquiry Email",
    "explanation": (
        "大問3A「Your service」は、施設への関心の理由→イベント概要→日程・人数→打ち合わせ依頼、という実用的な問い合わせメールです。"
        "Could you please let me know ... と It would be great if you could provide ... は依頼の定型表現で、"
        "Q26の Therefore, we can easily adjust our schedules は「学校が近い・職員がいる」から「訪問が容易」と結論づける論理です。"
        "Q24は easy to access from several train stations → located near public transportation、"
        "Q25は about 150 people ... about the number your facility can hold → appropriate for the space のパラフレーズが鍵です。"
    ),
    "sourceQuote": "easy to access from several train stations / Could you please let me know which date might be suitable / It would be great if you could provide / Therefore, we can easily adjust our schedules",
    "sourceLocation": "大問3A「Your service」",
    "examples": [
        {
            "en": "Also, your facility is appealing because it is easy to access from several train stations.",
            "ja": "また、いくつかの駅からアクセスしやすいため、貴施設は魅力的です。",
            "note": "be appealing because ～＝「～なので魅力的」。Q24の直接根拠。public transportation への言い換えに注意。",
        },
        {
            "en": "According to the website, this is about the number of people your facility can hold.",
            "ja": "ウェブサイトによると、これは貴施設が収容できる人数とほぼ同じです。",
            "note": "about the number ... can hold＝「収容できる人数とほぼ同じ」。Q25の決め手。",
        },
        {
            "en": "Could you please let me know which date might be suitable for our event? It would be great if you could provide a few possible dates.",
            "ja": "どの日程が私たちのイベントに適しているか教えていただけますか。可能な日程をいくつかご提示いただけるとありがたいです。",
            "note": "Could you please ...? / It would be great if you could ...＝丁寧な依頼の二段構え。would・could で婉曲に。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Your service]\n"
            "Dear Mary Carter,\nMy name is Matthew Watts, and I am a teacher at Polar Village Elementary School. We are looking for an outdoor facility where we can hold an athletic event this fall. One of my coworkers recommended your facility and suggested I contact you. Also, your facility is appealing because it is easy to access from several train stations.\n"
            "Although the exact date has not been set, our athletic event will take place on a weekday in September or October. We hope to use the large ground from 8 a.m. to 3 p.m. Currently, we expect about 150 people to attend the event, including some parents and teachers. According to the website, this is about the number of people your facility can hold.\n"
            "Could you please let me know which date might be suitable for our event? It would be great if you could provide a few possible dates. Our school is close to your main office, and we have enough teachers and staff. Therefore, we can easily adjust our schedules to make sure at least one person can visit for the meeting before 5 p.m. on the day you choose."
        ),
        "ja": (
            "メアリー・カーター様\nマシュー・ワッツと申します。ポーラー・ビレッジ小学校の教師です。今年の秋に運動会を開催できる屋外施設を探しています。同僚が貴施設を勧め、ご連絡するよう勧めてくれました。また、いくつかの駅からアクセスしやすいため、貴施設は魅力的です。\n"
            "正確な日程はまだ決まっていませんが、運動会は9月か10月の平日に行われます。午前8時から午後3時まで大きなグラウンドを使いたいと考えています。現在、保護者や教師を含め約150人が参加する見込みです。ウェブサイトによると、これは貴施設が収容できる人数とほぼ同じです。\n"
            "どの日程が私たちのイベントに適しているか教えていただけますか。可能な日程をいくつかご提示いただけるとありがたいです。本校は貴社の本社に近く、教師や職員も十分にいます。したがって、スケジュールを調整して、ご指定の日の午後5時前に少なくとも1人が打ち合わせのために訪問できるようにできます。"
        ),
        "audioFile": "audio/practice_pp3.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q24で「スタッフが親切」が誤答になる理由を説明してください。",
            "a": "本文に staff is helpful の記述はない。appealing because it is easy to access from several train stations が唯一の「魅力の理由」として明示されている。",
        },
        {
            "q": "Q25で「週末のみ」が誤答になる根拠となる英文を抜き出してください。",
            "a": "our athletic event will take place on a weekday in September or October。weekday（平日）と only on weekends は矛盾。",
        },
        {
            "q": "Q26の Therefore の直前2文と、正解「訪問が難しくない」の関係を説明してください。",
            "a": "Our school is close to your main office（学校が本社に近い）＋ we have enough teachers and staff（職員が十分）→ Therefore adjust schedules to visit（訪問できる）という論理の結論。",
        },
        {
            "q": "「It would be great if you could provide」と Could you please の違い・共通点は？",
            "a": "どちらも丁寧な依頼。could/would で直接性を弱める。前者は「～していただけるとありがたい」という気持ちを添える表現。",
        },
    ],
    "highlightPatterns": [
        "easy to access from several train stations",
        "about the number of people your facility can hold",
        "Could you please let me know which date might be suitable for our event",
        "It would be great if you could provide a few possible dates",
        "Our school is close to your main office",
        "Therefore, we can easily adjust our schedules",
        "on a weekday in September or October",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "問い合わせメール",
}

fp4 = {
    "id": "fp4",
    "title": "兄弟の対比と人物描写（On the other hand / According to him / wealthy background）",
    "subtitle": "Contrasting Figures: Alexander vs. Wilhelm Humboldt",
    "explanation": (
        "大問3B「The Humboldt Brothers」は、裕福な家庭・質の高い教育という共通の土台のうえで、"
        "Alexander（冒険・自然研究）と Wilhelm（教育・言語）という2人の異なる道を描きます。"
        "On the other hand は段落の転換で Wilhelm の話題へ移る合図。"
        "According to him は Wilhelm の言語観を導入し、Q29の perceive the world → see and understand the world へのパラフレーズの根拠になります。"
        "Their wealthy background gave them early access to ... は Q30・Q31 を読むうえでの背景理解に直結します。"
    ),
    "sourceQuote": "On the other hand, Wilhelm's passion was education and language / According to him, language was ... a means that allowed people to perceive the world / Their wealthy background gave them early access to quality education",
    "sourceLocation": "大問3B「The Humboldt Brothers」第2〜4段落",
    "examples": [
        {
            "en": "She took charge of their education, hiring famous educators and experts in various fields to tutor them.",
            "ja": "母は教育を担当し、さまざまな分野の有名な教育者や専門家を雇って家庭教師として教えさせました。",
            "note": "take charge of ～＝「～を担当する」。Q27 arranged private lessons の直接根拠。",
        },
        {
            "en": "The money he received after his mother's death made his dream of traveling to South America come true.",
            "ja": "母の死後に受け取ったお金が、南アメリカへの旅という夢を実現させました。",
            "note": "make one's dream come true＝「夢を実現させる」。Q28の決め手。本の売上・弟の誘いは本文にない。",
        },
        {
            "en": "According to him, language was not just a collection of words but a means that allowed people to perceive the world.",
            "ja": "彼にとって言語は単なる語の集まりではなく、人々が世界を認識する手段でした。",
            "note": "not just A but B＝「AだけでなくB」。perceive the world＝Q29の see and understand the world の言い換え元。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: The Humboldt Brothers]\n"
            "The younger of the two, Alexander, had been deeply interested in adventure since early childhood. The money he received after his mother's death made his dream of traveling to South America come true. He spent several years there studying plants, animals, and the natural features of the land. One of his most famous books is Kosmos, in which he tried to explain how everything in the natural world worked and how things were connected to each other.\n"
            "On the other hand, Wilhelm's passion was education and language. He served as the education director of the Ministry of the Interior in Prussia and helped found a university. The proposal he wrote for the university has influenced the German university system ever since. He considered language to be something whose structure and character reflected the culture and individuality of its speakers. According to him, language was not just a collection of words but a means that allowed people to perceive the world.\n"
            "Their wealthy background gave them early access to quality education and rich intellectual opportunities. These experiences helped shape ideas that continue to influence society today. While not many people in the world may know their names, many people have indirectly received benefits from their work."
        ),
        "ja": (
            "二人のうち弟のアレクサンダーは、幼い頃から冒険に深い関心を持っていました。母の死後に受け取ったお金が、南アメリカへの旅という夢を実現させました。彼はそこで数年を過ごし、植物、動物、土地の自然の特徴を研究しました。最も有名な本の一つが『コスモス』で、自然界のすべてがどのように機能し、物事が互いにどう結びついているかを説明しようとしました。\n"
            "一方、ヴィルヘルムの情熱は教育と言語でした。彼はプロイセン内務省の教育局長を務め、大学の設立にも協力しました。大学のために書いた提案書は、それ以来ドイツの大学制度に影響を与え続けています。言語の構造と性格は話者の文化と個性を反映すると考えました。彼にとって言語は単なる語の集まりではなく、人々が世界を認識する手段でした。\n"
            "裕福な背景は質の高い教育と豊かな知的機会への早期のアクセスを与えました。これらの経験は、今日も社会に影響を与え続ける思想の形成を助けました。世界中で彼らの名前を知る人は多くないかもしれませんが、多くの人が彼らの仕事から間接的に恩恵を受けています。"
        ),
        "audioFile": "audio/practice_pp4.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q27で「有名な学校に通わせた」が誤答になる理由を説明してください。",
            "a": "本文は hiring ... experts to tutor them（家庭教師を雇った）。send them to a famous school の記述はない。",
        },
        {
            "q": "On the other hand は段落の論理でどのような転換を示しますか？",
            "a": "Alexander の冒険・自然研究の話から、Wilhelm の教育・言語への情熱へ話題を切り替える。2人の「対照的な関心」を示す。",
        },
        {
            "q": "Q31で Wilhelm の提案書に関する記述だけが正しい理由を、他の選択肢との矛盾から説明してください。",
            "a": "①本は旅の後（after the trip）②すでに wealthy family③父は幼少期に死去・piano の記述なし④proposal has influenced the German university system ever since は本文と一致。",
        },
        {
            "q": "whose structure and character reflected the culture and individuality の whose は何を指しますか？",
            "a": "language（言語）。関係代名詞 whose で「言語の構造と性格が文化と個性を反映した」と説明。Wilhelm の言語観の核心。",
        },
    ],
    "highlightPatterns": [
        "hiring famous educators and experts in various fields to tutor them",
        "made his dream of traveling to South America come true",
        "On the other hand, Wilhelm's passion was education and language",
        "The proposal he wrote for the university has influenced the German university system ever since",
        "allowed people to perceive the world",
        "Their wealthy background gave them early access to quality education and rich intellectual opportunities",
        "indirectly received benefits from their work",
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "人物・対比",
}

fp5 = {
    "id": "fp5",
    "title": "今回の重要パラフレーズ（本文→設問・選択肢の言い換え）",
    "subtitle": "Key Paraphrases in This Exam",
    "explanation": (
        "英検2級読解では、正解選択肢が本文の表現をそのまま使わないことがほとんどです。"
        "本試験では、easy to access from several train stations → located near public transportation（Q24）、"
        "about the number of people your facility can hold → appropriate for the space（Q25）、"
        "adjust our schedules to visit → visiting her in the office is not too difficult（Q26）、"
        "hiring ... experts to tutor them → arranged private lessons with academic experts（Q27）、"
        "perceive the world → see and understand the world around them（Q29）など、"
        "名詞句・動詞レベルの言い換えに気づけるかが正答の鍵です。"
        "大問1でも barely won（かろうじて勝利）や have a tendency to（～する傾向）など、"
        "文脈から意味を補完する読み方が求められます。"
    ),
    "sourceQuote": "easy to access → near public transportation / can hold → appropriate for the space / tutor them → private lessons / perceive the world → see and understand the world / proposal ... influenced → great impact on the university system",
    "sourceLocation": "大問1・大問3A Q24〜26・大問3B Q27〜31",
    "examples": [
        {
            "en": "本文: 'it is easy to access from several train stations'\n→ 選択肢: 'It is located near public transportation.'",
            "ja": "「いくつかの駅からアクセスしやすい」→「公共交通機関の近くにある」",
            "note": "access from train stations ⇔ near public transportation。Q24のパラフレーズ。",
        },
        {
            "en": "本文: 'hiring famous educators and experts in various fields to tutor them'\n→ 選択肢: 'arranged private lessons with academic experts for them.'",
            "ja": "「専門家を雇って教えさせた」→「学問の専門家による個人教授を手配した」",
            "note": "hire ... to tutor ⇔ arrange private lessons with experts。Q27のパラフレーズ。",
        },
        {
            "en": "本文: 'a means that allowed people to perceive the world'\n→ 選択肢: 'a tool that helped individuals see and understand the world around them.'",
            "ja": "「世界を認識する手段」→「周囲の世界を見て理解するのを助ける道具」",
            "note": "means/tool、perceive/see and understand、the world/the world around them。Q29のパラフレーズ。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Your service / The Humboldt Brothers]\n"
            "Also, your facility is appealing because it is easy to access from several train stations. Currently, we expect about 150 people to attend the event, including some parents and teachers. According to the website, this is about the number of people your facility can hold. Our school is close to your main office, and we have enough teachers and staff. Therefore, we can easily adjust our schedules to make sure at least one person can visit for the meeting before 5 p.m. on the day you choose.\n"
            "She took charge of their education, hiring famous educators and experts in various fields to tutor them. The proposal he wrote for the university has influenced the German university system ever since. According to him, language was not just a collection of words but a means that allowed people to perceive the world."
        ),
        "ja": (
            "また、いくつかの駅からアクセスしやすいため、貴施設は魅力的です。現在、保護者や教師を含め約150人が参加する見込みです。ウェブサイトによると、これは貴施設が収容できる人数とほぼ同じです。本校は貴社の本社に近く、教師や職員も十分にいます。したがって、スケジュールを調整して、ご指定の日の午後5時前に少なくとも1人が打ち合わせのために訪問できるようにできます。\n"
            "母は教育を担当し、さまざまな分野の有名な教育者や専門家を雇って家庭教師として教えさせました。大学のために書いた提案書は、それ以来ドイツの大学制度に影響を与え続けています。彼にとって言語は単なる語の集まりではなく、人々が世界を認識する手段でした。"
        ),
        "audioFile": "audio/practice_pp5.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q25で「生徒だけが参加」が誤答になる理由を、including some parents and teachers と照合して説明してください。",
            "a": "本文は保護者・教師も含む（including parents and teachers）。only the students と矛盾。人数は収容力と一致（appropriate for the space）が正解。",
        },
        {
            "q": "Q28で「本の売上」が誤答になる理由を、時系列から説明してください。",
            "a": "Alexander wrote books after the trip（旅の後に本を書いた）。旅の資金は The money he received after his mother's death（母の死後の遺産）。",
        },
        {
            "q": "Q9の barely won は本文のどの手がかりとセットで読むべきですか？",
            "a": "evenly matched（互角）と in the last seconds of the game（終了間際のゴール）。「僅差の勝利」を表す副詞 barely の典型文脈。",
        },
        {
            "q": "パラフレーズ問題で正解を見つける3つのチェックポイントを、この試験の例で説明してください。",
            "a": "①同じ主題か（交通アクセス・人数・訪問の容易さ）。②動詞の方向が同じか（perceive＝理解する、influence＝影響）。③時制・因果が矛盾しないか（本は旅の後、遺産は旅の前）。",
        },
    ],
    "highlightPatterns": [
        "easy to access from several train stations",
        "about the number of people your facility can hold",
        "hiring famous educators and experts in various fields to tutor them",
        "allowed people to perceive the world",
        "The proposal he wrote for the university has influenced the German university system ever since",
        "evenly matched",
        "in the last seconds of the game",
    ],
    "highlightColor": "#f59e0b",
    "highlightLabel": "パラフレーズ",
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

data["lessonPlan"] = {"focusPoints": [fp1, fp2, fp3, fp4, fp5]}

all_text = ""
for sec in data.get("sections", []):
    for q in sec.get("questions", []):
        all_text += q.get("text", "") + " "
    for p in sec.get("passages", []):
        all_text += " ".join(p.get("paragraphs", [])) + " "

missing = []
for fp in data["lessonPlan"]["focusPoints"]:
    for pat in fp["highlightPatterns"]:
        if pat not in all_text:
            missing.append(f"{fp['id']}: {pat}")

if missing:
    print("本文に見つからないパターン:")
    for m in missing:
        print(" -", m)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ lessonPlan 保存完了: {DATA_PATH}")
for fp in data["lessonPlan"]["focusPoints"]:
    print(f"  {fp['id']}: {fp['title']} | patterns: {len(fp['highlightPatterns'])} | pq: {len(fp['practiceQuestions'])}")
