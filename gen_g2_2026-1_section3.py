# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検2級 data.json
Step C: 大問3（reading-comprehension型）Q24〜31
  3A Your service / 3B The Humboldt Brothers
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1", "data.json",
)

p3a_paras = [
    "Dear Mary Carter,\nMy name is Matthew Watts, and I am a teacher at Polar Village Elementary School. We are looking for an outdoor facility where we can hold an athletic event this fall. One of my coworkers recommended your facility and suggested I contact you. She used one of the grounds for an event at the school where she had previously worked. Also, your facility is appealing because it is easy to access from several train stations.",
    "Although the exact date has not been set, our athletic event will take place on a weekday in September or October. We hope to use the large ground from 8 a.m. to 3 p.m. Currently, we expect about 150 people to attend the event, including some parents and teachers. According to the website, this is about the number of people your facility can hold.",
    "Could you please let me know which date might be suitable for our event? It would be great if you could provide a few possible dates. We can meet to discuss the details of the event as needed. Our school is close to your main office, and we have enough teachers and staff. Therefore, we can easily adjust our schedules to make sure at least one person can visit for the meeting before 5 p.m. on the day you choose.",
    "Sincerely,\nMatthew Watts\nPolar Village Elementary School",
]

p3a_trans = [
    "メアリー・カーター様\nマシュー・ワッツと申します。ポーラー・ビレッジ小学校の教師です。今年の秋に運動会を開催できる屋外施設を探しています。同僚の一人が貴施設を勧め、ご連絡するよう勧めてくれました。彼女は以前勤めていた学校のイベントで、貴施設のグラウンドの一つを使用したことがあります。また、いくつかの駅からアクセスしやすいため、貴施設は魅力的です。",
    "正確な日程はまだ決まっていませんが、運動会は9月か10月の平日に行われます。午前8時から午後3時まで大きなグラウンドを使いたいと考えています。現在、保護者や教師を含め約150人が参加する見込みです。ウェブサイトによると、これは貴施設が収容できる人数とほぼ同じです。",
    "どの日程が私たちのイベントに適しているか教えていただけますか。可能な日程をいくつかご提示いただけるとありがたいです。必要に応じて、イベントの詳細について打ち合わせができます。本校は貴社の本社に近く、教師や職員も十分にいます。したがって、スケジュールを調整して、ご指定の日の午後5時前に少なくとも1人が打ち合わせのために訪問できるようにできます。",
    "敬具\nマシュー・ワッツ\nポーラー・ビレッジ小学校",
]

p3a_pairs = [
    [
        "One of my coworkers recommended your facility and suggested I contact you.",
        "同僚の一人が貴施設を勧め、ご連絡するよう勧めてくれました。",
    ],
    [
        "your facility is appealing because it is easy to access from several train stations.",
        "いくつかの駅からアクセスしやすいため、貴施設は魅力的です。",
    ],
    [
        "we expect about 150 people to attend the event, including some parents and teachers.",
        "保護者や教師を含め約150人が参加する見込みです。",
    ],
    [
        "this is about the number of people your facility can hold.",
        "これは貴施設が収容できる人数とほぼ同じです。",
    ],
    [
        "Our school is close to your main office, and we have enough teachers and staff.",
        "本校は貴社の本社に近く、教師や職員も十分にいます。",
    ],
    [
        "we can easily adjust our schedules to make sure at least one person can visit for the meeting before 5 p.m.",
        "スケジュールを調整して、午後5時前に少なくとも1人が打ち合わせのために訪問できるようにできます。",
    ],
]

p3b_paras = [
    "Alexander and Wilhelm von Humboldt were born in the late eighteenth century in what is now Germany into a wealthy family. When Alexander was just a child, their father passed away. Even before his death, their parents wanted to ensure that their sons received a good education. Following his death, the brothers were raised mainly by their mother, who held strict and serious religious beliefs. She took charge of their education, hiring famous educators and experts in various fields to tutor them. The brothers' education covered many academic subjects, such as mathematics, languages, history, and economics.",
    "The younger of the two, Alexander, had been deeply interested in adventure since early childhood. The money he received after his mother's death made his dream of traveling to South America come true. He spent several years there studying plants, animals, and the natural features of the land. Alexander wrote books about what he had learned there after the trip. One of his most famous books is Kosmos, in which he tried to explain how everything in the natural world worked and how things were connected to each other.",
    "On the other hand, Wilhelm's passion was education and language. He served as the education director of the Ministry of the Interior in Prussia and helped found a university. The proposal he wrote for the university has influenced the German university system ever since. He is also known for his studies of language. He considered language to be something whose structure and character reflected the culture and individuality of its speakers. According to him, language was not just a collection of words but a means that allowed people to perceive the world.",
    "It is clear that the environment in which the Humboldt brothers grew up gave them opportunities to achieve something with a lasting impact. They enjoyed a life that not everyone could have, growing up around great leaders, scientists, and writers. Their wealthy background gave them early access to quality education and rich intellectual opportunities. These experiences helped shape ideas that continue to influence society today. While not many people in the world may know their names, many people have indirectly received benefits from their work.",
]

p3b_trans = [
    "アレクサンダーとヴィルヘルム・フォン・フンボルトは、18世紀後半に現在のドイツにある地域で裕福な家庭に生まれました。アレクサンダーがまだ子どものころ、父は亡くなりました。父の死以前から、両親は息子たちに良い教育を受けさせたいと考えていました。父の死後、兄弟は主に母によって育てられました。母は厳格で真剣な宗教的信念を持っていました。母は教育を担当し、さまざまな分野の有名な教育者や専門家を雇って家庭教師として教えさせました。兄弟の教育は、数学、語学、歴史、経済学など多くの学問分野をカバーしました。",
    "二人のうち弟のアレクサンダーは、幼い頃から冒険に深い関心を持っていました。母の死後に受け取ったお金が、南アメリカへの旅という夢を実現させました。彼はそこで数年を過ごし、植物、動物、土地の自然の特徴を研究しました。アレクサンダーは旅の後、そこで学んだことを本にまとめました。最も有名な本の一つが『コスモス』で、自然界のすべてがどのように機能し、物事が互いにどう結びついているかを説明しようとしました。",
    "一方、ヴィルヘルムの情熱は教育と言語でした。彼はプロイセン内務省の教育局長を務め、大学の設立にも協力しました。大学のために書いた提案書は、それ以来ドイツの大学制度に影響を与え続けています。彼は言語研究でも知られています。言語の構造と性格は、その話者の文化と個性を反映すると考えました。彼にとって言語は単なる語の集まりではなく、人々が世界を認識する手段でした。",
    "フンボルト兄弟が育った環境が、永続的な影響を与える何かを成し遂げる機会を彼らに与えたことは明らかです。彼らは偉大な指導者、科学者、作家たちに囲まれて育ち、誰もが持てるわけではない人生を享受しました。裕福な背景は質の高い教育と豊かな知的機会への早期のアクセスを与えました。これらの経験は、今日も社会に影響を与え続ける思想の形成を助けました。世界中で彼らの名前を知る人は多くないかもしれませんが、多くの人が彼らの仕事から間接的に恩恵を受けています。",
]

p3b_pairs = [
    [
        "She took charge of their education, hiring famous educators and experts in various fields to tutor them.",
        "母は教育を担当し、さまざまな分野の有名な教育者や専門家を雇って家庭教師として教えさせました。",
    ],
    [
        "The money he received after his mother's death made his dream of traveling to South America come true.",
        "母の死後に受け取ったお金が、南アメリカへの旅という夢を実現させました。",
    ],
    [
        "The proposal he wrote for the university has influenced the German university system ever since.",
        "大学のために書いた提案書は、それ以来ドイツの大学制度に影響を与え続けています。",
    ],
    [
        "language was not just a collection of words but a means that allowed people to perceive the world.",
        "言語は単なる語の集まりではなく、人々が世界を認識する手段でした。",
    ],
    [
        "Their wealthy background gave them early access to quality education and rich intellectual opportunities.",
        "裕福な背景は質の高い教育と豊かな知的機会への早期のアクセスを与えました。",
    ],
    [
        "many people have indirectly received benefits from their work.",
        "多くの人が彼らの仕事から間接的に恩恵を受けています。",
    ],
]

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文 [A], [B] の内容に関して, (24) から (31) までの質問に対して最も適切なもの, または文を完成させるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び, その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Your service",
            "format": "email",
            "meta": {
                "from": "Matthew Watts <mwatts@polarvillageelementary.edu>",
                "to": "Mary Carter <mcarter@trackfitrentals.com>",
                "date": "May 27",
                "subject": "Your service",
            },
            "paragraphs": p3a_paras,
            "translations": p3a_trans,
            "sentencePairs": p3a_pairs,
            "questions": [
                {
                    "number": 24,
                    "question": "What is one reason Matthew Watts is interested in the facility?",
                    "questionTranslation": "マシュー・ワッツがその施設に関心を持つ理由の一つは何か？",
                    "choices": [
                        "The ground is perfect for camping.",
                        "The staff working there is helpful.",
                        "It is located near public transportation.",
                        "It is popular among schoolchildren.",
                    ],
                    "choiceTranslations": [
                        "グラウンドがキャンプに最適である。",
                        "そこで働くスタッフが親切である。",
                        "公共交通機関の近くにある。",
                        "学童の間で人気がある。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ キャンプに最適→athletic event（運動会）の話。キャンプの記述はない",
                        "❌ スタッフが親切→スタッフの対応についての記述はない",
                        "✅ 公共交通の近く→正解。💡 easy to access from several train stations（いくつかの駅からアクセスしやすい）の言い換え",
                        "❌ 学童に人気→人気の記述はなく、同僚の勧めとアクセスの良さが理由",
                    ],
                    "sourceEvidence": [
                        "your facility is appealing because it is easy to access from several train stations",
                    ],
                    "grammar": "💡 be appealing because ～＝～なので魅力的だ。public transportation＝train stations の言い換えに注意。",
                },
                {
                    "number": 25,
                    "question": "Regarding the event that is being planned,",
                    "questionTranslation": "計画されているイベントについて、正しいのはどれか？",
                    "choices": [
                        "the number of people will likely be appropriate for the space.",
                        "it will happen only on weekends this September or October.",
                        "only the students from the school will attend this year.",
                        "it will last all day until the end of the year.",
                    ],
                    "choiceTranslations": [
                        "参加人数はおそらく施設の収容に適している。",
                        "今年の9月か10月の週末のみに行われる。",
                        "今年は学校の生徒だけが参加する。",
                        "年末まで一日中続く。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 人数が施設に適している→正解。💡 about 150 people to attend ＋ about the number of people your facility can hold",
                        "❌ 週末のみ→on a weekday in September or October（平日）と矛盾",
                        "❌ 生徒だけ→including some parents and teachers（保護者・教師も含む）と矛盾",
                        "❌ 年末まで一日中→8 a.m. to 3 p.m.（午前8時〜午後3時）の1日イベント",
                    ],
                    "sourceEvidence": [
                        "we expect about 150 people to attend the event, including some parents and teachers",
                        "this is about the number of people your facility can hold",
                    ],
                    "grammar": "💡 about 150 people ＋ can hold about that number＝人数と収容力がほぼ一致。appropriate for the space の根拠。",
                },
                {
                    "number": 26,
                    "question": "Why does Matthew mention the location of the school and the number of staff to Mary Carter?",
                    "questionTranslation": "マシューはなぜ学校の場所と職員の人数に言及しているか？",
                    "choices": [
                        "To suggest changing the time of the event to the morning.",
                        "To ask if the facility staff can help prepare for the event.",
                        "To explain that the school needs more teachers than it has.",
                        "To show that visiting her in the office is not too difficult.",
                    ],
                    "choiceTranslations": [
                        "イベントの時間を午前に変更することを提案するため。",
                        "施設スタッフが準備を手伝えるか尋ねるため。",
                        "学校が教師をもっと必要としていることを説明するため。",
                        "オフィスへの訪問がそれほど難しくないことを示すため。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 午前に変更→8 a.m. to 3 p.m. はすでに提示済み。変更の提案ではない",
                        "❌ スタッフに準備を依頼→施設側の準備支援の話はない",
                        "❌ 教師が足りない→we have enough teachers and staff（十分にいる）と矛盾",
                        "✅ 訪問が難しくないことを示す→正解。💡 school is close to your main office ＋ adjust schedules to visit for the meeting",
                    ],
                    "sourceEvidence": [
                        "Our school is close to your main office, and we have enough teachers and staff",
                        "we can easily adjust our schedules to make sure at least one person can visit for the meeting",
                    ],
                    "grammar": "💡 Therefore で結論。close to the office ＋ enough staff ＋ adjust schedules → 訪問の容易さを説明。",
                },
            ],
        },
        {
            "label": "B",
            "title": "The Humboldt Brothers",
            "paragraphs": p3b_paras,
            "translations": p3b_trans,
            "sentencePairs": p3b_pairs,
            "questions": [
                {
                    "number": 27,
                    "question": "To provide a great education for the Humboldt brothers, their mother",
                    "questionTranslation": "フンボルト兄弟に素晴らしい教育を提供するために、母親は何をしたか？",
                    "choices": [
                        "took them to Berlin to learn languages through their travels.",
                        "chose to send them to a famous school for wealthy families.",
                        "arranged private lessons with academic experts for them.",
                        "had their own parents decide what the brothers should study.",
                    ],
                    "choiceTranslations": [
                        "ベルリンに連れて行き、旅を通じて語学を学ばせた。",
                        "裕福な家庭向けの有名な学校に通わせることを選んだ。",
                        "学問の専門家による個人教授を手配した。",
                        "自分の両親に兄弟が学ぶべきことを決めさせた。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ ベルリンへの旅行→Berlin の記述はない",
                        "❌ 有名な学校に通わせた→学校ではなく hiring ... to tutor them（家庭教師を雇った）",
                        "✅ 専門家による個人教授→正解。💡 hiring famous educators and experts in various fields to tutor them",
                        "❌ 祖父母に決めさせた→母が took charge of their education（教育を担当）",
                    ],
                    "sourceEvidence": [
                        "She took charge of their education, hiring famous educators and experts in various fields to tutor them",
                    ],
                    "grammar": "💡 hire ～ to tutor＝～を雇って教える。private lessons＝tutor them の言い換え。",
                },
                {
                    "number": 28,
                    "question": "What made it possible for Alexander von Humboldt to travel to South America?",
                    "questionTranslation": "アレクサンダー・フォン・フンボルトが南アメリカへ旅できるようになったのは何のおかげか？",
                    "choices": [
                        "The money left to him after his mother passed away.",
                        "The sales of the book he wrote about the natural world.",
                        "An invitation from his brother to travel to new places.",
                        "Support given by a group of scientists in South America.",
                    ],
                    "choiceTranslations": [
                        "母の死後に彼に残されたお金。",
                        "自然界について書いた本の売上。",
                        "弟からの新しい場所への旅の誘い。",
                        "南アメリカの科学者グループからの支援。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 母の死後の遺産→正解。💡 The money he received after his mother's death made his dream ... come true",
                        "❌ 本の売上→本は旅の後に書いた（after the trip）ので因果が逆",
                        "❌ 弟からの誘い→兄アレクサンダーの旅。Wilhelm からの誘いの記述なし",
                        "❌ 南米の科学者の支援→本文にない",
                    ],
                    "sourceEvidence": [
                        "The money he received after his mother's death made his dream of traveling to South America come true",
                    ],
                    "grammar": "💡 make one's dream come true＝夢を実現させる。after his mother's death が資金の出所。",
                },
                {
                    "number": 29,
                    "question": "What did Wilhelm von Humboldt believe about language?",
                    "questionTranslation": "ヴィルヘルム・フォン・フンボルトは言語について何を信じていたか？",
                    "choices": [
                        "It developed in similar ways across different cultures and societies.",
                        "It reflected both the German cultural background and educational systems.",
                        "It was a tool that helped individuals see and understand the world around them.",
                        "It was closely related to education and played a role in creating university systems.",
                    ],
                    "choiceTranslations": [
                        "異なる文化・社会で似たように発展した。",
                        "ドイツの文化的背景と教育制度の両方を反映した。",
                        "個人が周囲の世界を見て理解するのを助ける道具だった。",
                        "教育と密接に関連し、大学制度の創設に役割を果たした。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 似たように発展→individuality of its speakers（話者の個性）を強調しており、均質な発展の話ではない",
                        "❌ ドイツ文化と教育制度→German の記述はない。speakers の文化一般の話",
                        "✅ 世界を認識する道具→正解。💡 a means that allowed people to perceive the world（世界を認識する手段）",
                        "❌ 大学制度の創設→Wilhelm は大学設立に関わったが、これは言語についての信念ではない",
                    ],
                    "sourceEvidence": [
                        "language was not just a collection of words but a means that allowed people to perceive the world",
                    ],
                    "grammar": "💡 perceive the world＝世界を認識する。see and understand the world around them がパラフレーズ。",
                },
                {
                    "number": 30,
                    "question": "What is one reason the Humboldt brothers could focus on their achievements?",
                    "questionTranslation": "フンボルト兄弟が自分たちの業績に集中できた理由の一つは何か？",
                    "choices": [
                        "Their childhood provided them with access to knowledge and learning.",
                        "Their jobs were flexible enough to allow them a lot of free time for research.",
                        "They had a lot of volunteer workers who were willing to work for them.",
                        "They worked with teams of several great assistants on each project.",
                    ],
                    "choiceTranslations": [
                        "幼少期に知識と学習へのアクセスが与えられた。",
                        "仕事が柔軟で研究の自由時間が多かった。",
                        "喜んで働いてくれるボランティアがたくさんいた。",
                        "各プロジェクトで優れた助手のチームと働いた。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 幼少期の知識・学習へのアクセス→正解。💡 wealthy background gave them early access to quality education and rich intellectual opportunities",
                        "❌ 仕事が柔軟→flexible jobs の記述はない",
                        "❌ ボランティア→volunteer の記述はない",
                        "❌ 助手のチーム→teams of assistants の記述はない",
                    ],
                    "sourceEvidence": [
                        "Their wealthy background gave them early access to quality education and rich intellectual opportunities",
                        "growing up around great leaders, scientists, and writers",
                    ],
                    "grammar": "💡 early access to quality education＝幼少期からの知識・学習へのアクセス。achievements に集中できる環境の説明。",
                },
                {
                    "number": 31,
                    "question": "Which of the following statements is true?",
                    "questionTranslation": "次のうち正しいものはどれか？",
                    "choices": [
                        "Alexander finished writing a book about the functions of nature before he went on a journey.",
                        "The Humboldt brothers desired to become rich and chose their own study subjects accordingly.",
                        "The Humboldts' father wanted to teach them piano himself and took steps to make it happen.",
                        "Wilhelm wrote a proposal that has had a great impact on the German university system.",
                    ],
                    "choiceTranslations": [
                        "アレクサンダーは旅に出る前に自然界の働きについての本を書き終えた。",
                        "兄弟は裕福になりたく、それに合わせて学ぶ科目を選んだ。",
                        "父は自分でピアノを教えたく、そのための措置を取った。",
                        "ヴィルヘルムが書いた提案書はドイツの大学制度に大きな影響を与えた。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 旅の前に本を書いた→Alexander wrote books ... after the trip（旅の後）と矛盾",
                        "❌ 裕福になりたかった→すでに wealthy family（裕福な家庭）に生まれている",
                        "❌ 父がピアノを教えた→piano の記述はなく、父は Alexander が幼い頃に亡くなっている",
                        "✅ ヴィルヘルムの提案書が大学制度に影響→正解。💡 The proposal he wrote for the university has influenced the German university system ever since",
                    ],
                    "sourceEvidence": [
                        "The proposal he wrote for the university has influenced the German university system ever since",
                    ],
                    "grammar": "💡 ever since＝それ以来ずっと。Which is true? 問題は本文と明確に矛盾する選択肢を除外する。",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

s1 = next((s for s in data.get("sections", []) if s.get("name") == "大問1"), None)
s2 = next((s for s in data.get("sections", []) if s.get("name") == "大問2"), None)
data["sections"] = [x for x in (s1, s2, section3) if x]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 大問3リッチ解説を保存: {DATA_PATH}")
print(f"   パッセージ: {len(section3['passages'])} / 問題: 8")
