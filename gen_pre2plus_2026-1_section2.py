# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級プラス data.json
Step B: 大問2（passage-fill型）Q18〜23
  2A A Christmas Tradition / 2B Traveling for Dental Care
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(18)から(23)までの（　）に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "A Christmas Tradition",
            "paragraphs": [
                "Every December, fans of a Spanish professional soccer team take part in a special event. On a certain day, they come to the stadium not only to watch a match but also to throw soft toys onto the field. Tens of thousands of such toys are thrown, and then they are immediately collected by volunteers. ( 18 ), these toys are delivered to children who are in need. This event is held every year, and it is a way for soccer fans to help bring joy to many children at this special time of the year.",
                "This tradition began in 2018 ( 19 ). At that time, the soccer club and its fans wanted to do a kind act for local children who were less fortunate than others. Since then, the event has grown and turned into an occasion that even fans of other teams look forward to every year. Many people have been touched by the kind gesture of the club and its fans in organizing such an event, and call it a wonderful tradition.",
                "Today, it has grown into a larger tradition that ( 20 ). The toys are not only given to children in the local city. Some of the toys are sent to charity organizations in other parts of Spain and even to children overseas. By doing so, many children both inside and outside the country can receive presents during the Christmas season. Thanks to this event, more children can feel happy and celebrate this special time of the year.",
            ],
            "translations": [
                "毎年12月、スペインのプロサッカーチームのファンは特別なイベントに参加します。ある日、彼らは試合を見るだけでなく、フィールドにぬいぐるみを投げ込みます。何万ものぬいぐるみが投げられ、すぐにボランティアが回収します。( 18 )、これらのぬいぐるみは困っている子どもたちに届けられます。このイベントは毎年開催され、サッカーファンがこの特別な時期に多くの子どもに喜びをもたらす方法です。",
                "この伝統は2018年に始まりました( 19 )。当時、サッカークラブとファンは、他の子どもより恵まれない地域の子どもたちのために親切な行いをしたいと考えていました。それ以来、イベントは成長し、他チームのファンさえも毎年楽しみにする行事になりました。多くの人がクラブとファンの親切な行いに感動し、素晴らしい伝統だと呼んでいます。",
                "今日、それはより大きな伝統へと成長し、( 20 )。ぬいぐるみは地元の都市の子どもだけでなく、スペインの他の地域の慈善団体や海外の子どもにも送られます。そうすることで、国内外の多くの子どもがクリスマスの季節にプレゼントを受け取れます。このイベントのおかげで、より多くの子どもが幸せを感じ、この特別な時期を祝えます。",
            ],
            "sentencePairs": [
                [
                    "On a certain day, they come to the stadium not only to watch a match but also to throw soft toys onto the field.",
                    "ある日、彼らは試合を見るだけでなく、フィールドにぬいぐるみを投げ込みます。",
                ],
                [
                    "Tens of thousands of such toys are thrown, and then they are immediately collected by volunteers.",
                    "何万ものぬいぐるみが投げられ、すぐにボランティアが回収します。",
                ],
                [
                    "these toys are delivered to children who are in need.",
                    "これらのぬいぐるみは困っている子どもたちに届けられます。",
                ],
                [
                    "At that time, the soccer club and its fans wanted to do a kind act for local children who were less fortunate than others.",
                    "当時、サッカークラブとファンは、他の子どもより恵まれない地域の子どもたちのために親切な行いをしたいと考えていました。",
                ],
                [
                    "Some of the toys are sent to charity organizations in other parts of Spain and even to children overseas.",
                    "ぬいぐるみはスペインの他の地域の慈善団体や海外の子どもにも送られます。",
                ],
                [
                    "many children both inside and outside the country can receive presents during the Christmas season.",
                    "国内外の多くの子どもがクリスマスの季節にプレゼントを受け取れます。",
                ],
            ],
            "questions": [
                {
                    "number": 18,
                    "choices": [
                        "In contrast",
                        "Eventually",
                        "On the other hand",
                        "Despite the fact",
                    ],
                    "choiceTranslations": [
                        "対照的に",
                        "最終的に・やがて",
                        "一方で",
                        "その事実にもかかわらず",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ In contrast＝対照的に。they are immediately collected by volunteers（回収）→ these toys are delivered（届ける）という手順の続きで、対比関係ではない",
                        "✅ Eventually＝最終的に・やがて。collected by volunteers（回収）のあと delivered to children who are in need（届ける）という時間の流れ→正解",
                        "❌ On the other hand＝一方で。throw → collect → deliver の手順の連続であり、対比の接続詞ではない",
                        "❌ Despite the fact＝その事実にもかかわらず。回収と配送は矛盾する内容ではなく、手順の続き",
                    ],
                    "sourceEvidence": [
                        "they are immediately collected by volunteers.",
                        "these toys are delivered to children who are in need.",
                    ],
                    "grammar": "💡 Eventually＝最終的に・やがて。手順の最後の段階を示すときに使う。throw → collect → deliver の流れを読む。",
                },
                {
                    "number": 19,
                    "choices": [
                        "with a specific purpose in mind",
                        "as part of a marketing campaign",
                        "to compete with other clubs' events",
                        "to celebrate the team's victory",
                    ],
                    "choiceTranslations": [
                        "特定の目的を持って",
                        "マーケティングキャンペーンの一環として",
                        "他クラブのイベントと競うために",
                        "チームの勝利を祝うために",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ with a specific purpose in mind＝特定の目的を持って。wanted to do a kind act for local children who were less fortunate（恵まれない子どもへの親切）が目的の具体的内容→正解",
                        "❌ as part of a marketing campaign＝マーケティングキャンペーン。a kind act for local children（地域の子どもへの親切）の文脈で、宣伝・販売促進の記述は出てこない",
                        "❌ to compete with other clubs' events＝他クラブと競う。even fans of other teams look forward to every year（他チームファンも楽しみにする）と矛盾する動機",
                        "❌ to celebrate the team's victory＝勝利を祝う。children who are in need（困っている子ども）への支援が主題で、victory の言及はない",
                    ],
                    "sourceEvidence": [
                        "the soccer club and its fans wanted to do a kind act for local children who were less fortunate than others.",
                    ],
                    "grammar": "💡 with a specific purpose in mind＝特定の目的を持って。This tradition began in 2018 ( ) の空所は「なぜ始まったか」の理由・目的を補う。",
                },
                {
                    "number": 20,
                    "choices": [
                        "focuses on entertaining the fans",
                        "replaces Christmas gifts with tickets",
                        "encourages the fans to bring food instead",
                        "spreads kindness across nations",
                    ],
                    "choiceTranslations": [
                        "ファンを楽しませることに焦点を当てる",
                        "クリスマスプレゼントをチケットに置き換える",
                        "ファンに食べ物を持参するよう促す",
                        "国々にわたって親切を広める",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ focuses on entertaining the fans＝ファンを楽しませる。children who are in need（困っている子ども）への支援が主題で、entertaining the fans ではない",
                        "❌ replaces Christmas gifts with tickets＝プレゼントをチケットに置き換える。sent to charity organizations ... and even to children overseas（海外にも送る）と矛盾",
                        "❌ encourages the fans to bring food instead＝食べ物の持参を促す。throw soft toys onto the field（ぬいぐるみ）の話で、food ではない",
                        "✅ spreads kindness across nations＝国々にわたって親切を広める。other parts of Spain and even to children overseas（海外の子どもへ）が決め手→正解",
                    ],
                    "sourceEvidence": [
                        "Some of the toys are sent to charity organizations in other parts of Spain and even to children overseas.",
                    ],
                    "grammar": "💡 spread kindness across nations＝国々にわたって親切を広める。a larger tradition that ～ の関係代名詞節が空所の形。",
                },
            ],
        },
        {
            "label": "B",
            "title": "Traveling for Dental Care",
            "paragraphs": [
                "These days, people travel abroad not only for fun or sightseeing but also for other purposes. One growing purpose is to receive dental care. This means that people visit other countries to get their teeth treated. This practice is known as dental tourism. In recent years, this trend has become common in many parts of the world. ( 21 ), data shows that people from countries such as Australia and the United Kingdom are traveling long distances for dental health.",
                "There are several reasons for this trend. One reason is the high cost of treatment. Some types of dental care in Australia cost more than twice as much as in Thailand. Another reason is ( 22 ) in some countries. In a 2024 survey of more than 2,000 people in the United Kingdom, around 20 percent reported that they had tried to book a clinic visit in the past year but could not see a dentist. These factors lead people to receive dental care in other countries.",
                "According to experts, however, people should be careful about the dangers of dental tourism, because there is a possibility of receiving unnecessary treatment or getting treatment using low-quality materials. Also, they may not receive enough legal support if something goes wrong. Therefore, it is important to ( 23 ). By doing so, people can clearly understand the possible problems and make safe choices about getting dental care abroad. The trend of dental tourism also highlights the importance of providing easy access to dental care in all countries.",
            ],
            "translations": [
                "最近、人々は楽しみや観光だけでなく、他の目的でも海外旅行をします。増えている目的の一つは歯科治療を受けることです。つまり、人々は歯の治療を受けるために他国を訪れます。この慣行は歯科ツーリズムとして知られています。近年、この傾向は世界の多くの地域で一般的になっています。( 21 )、オーストラリアやイギリスなどの国の人々が歯の健康のために遠くまで旅行しているというデータがあります。",
                "この傾向にはいくつかの理由があります。一つは治療費の高さです。オーストラリアのある歯科治療はタイの2倍以上の費用がかかります。もう一つの理由は、一部の国での( 22 )です。2024年のイギリスでの2,000人以上を対象とした調査で、約20％が過去1年にクリニックの予約を試みたが歯医者に診てもらえなかったと報告しました。これらの要因が、人々を他国で歯科治療を受ける方向へ導いています。",
                "しかし専門家によると、歯科ツーリズムの危険性には注意すべきだと言います。不必要な治療を受ける可能性や、低品質の材料で治療される可能性があるからです。また、何か問題が起きた場合、十分な法的支援を受けられないこともあります。したがって、( 23 )ことが重要です。そうすることで、人々は起こりうる問題を明確に理解し、海外での歯科治療について安全な選択ができます。歯科ツーリズムの傾向は、すべての国で歯科医療へのアクセスを容易にすることの重要性も浮き彫りにしています。",
            ],
            "sentencePairs": [
                [
                    "This practice is known as dental tourism.",
                    "この慣行は歯科ツーリズムとして知られています。",
                ],
                [
                    "Some types of dental care in Australia cost more than twice as much as in Thailand.",
                    "オーストラリアのある歯科治療はタイの2倍以上の費用がかかります。",
                ],
                [
                    "around 20 percent reported that they had tried to book a clinic visit in the past year but could not see a dentist.",
                    "約20％が過去1年にクリニックの予約を試みたが歯医者に診てもらえなかったと報告しました。",
                ],
                [
                    "there is a possibility of receiving unnecessary treatment or getting treatment using low-quality materials.",
                    "不必要な治療を受ける可能性や、低品質の材料で治療される可能性があるからです。",
                ],
                [
                    "By doing so, people can clearly understand the possible problems and make safe choices about getting dental care abroad.",
                    "そうすることで、人々は起こりうる問題を明確に理解し、海外での歯科治療について安全な選択ができます。",
                ],
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "By contrast",
                        "As a result",
                        "For example",
                        "In the end",
                    ],
                    "choiceTranslations": [
                        "対照的に",
                        "その結果",
                        "例えば",
                        "結局",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ By contrast＝対照的に。this trend has become common in many parts of the world（一般的）のあと、具体国のデータを挙げる段階で対比ではない",
                        "❌ As a result＝その結果。people from countries such as Australia and the United Kingdom（具体国）は「結果」ではなく例示",
                        "✅ For example＝例えば。this trend has become common（一般的）→ Australia and the United Kingdom（具体国）という一般→具体の流れ→正解",
                        "❌ In the end＝結局。data shows that people from countries such as Australia... は傾向の具体例を挙げている段階",
                    ],
                    "sourceEvidence": [
                        "this trend has become common in many parts of the world.",
                        "people from countries such as Australia and the United Kingdom are traveling long distances for dental health.",
                    ],
                    "grammar": "💡 For example＝例えば。一般論の直後に具体例を挙げる定番パターン。such as Australia and the United Kingdom が例示の目印。",
                },
                {
                    "number": 22,
                    "choices": [
                        "the long travel times between cities",
                        "the difficulty of making appointments",
                        "the lack of professional skills among dentists",
                        "the poor quality of the machines used",
                    ],
                    "choiceTranslations": [
                        "都市間の長い移動時間",
                        "予約を取ることの難しさ",
                        "歯科医の専門技術の不足",
                        "使用される機械の品質の低さ",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ the long travel times between cities＝都市間の移動時間。receive dental care in other countries（他国で治療）の話で、国内の都市間移動とは無関係",
                        "✅ the difficulty of making appointments＝予約の難しさ。tried to book a clinic visit but could not see a dentist（予約したが診てもらえなかった）と完全一致→正解",
                        "❌ the lack of professional skills among dentists＝歯科医の技術不足。tried to book a clinic visit but could not see a dentist（予約・診察の機会）の問題で、skill の話ではない",
                        "❌ the poor quality of the machines used＝機械の品質の低さ。low-quality materials（治療材料）は第3段落の話で、ここは予約の問題",
                    ],
                    "sourceEvidence": [
                        "they had tried to book a clinic visit in the past year but could not see a dentist.",
                    ],
                    "grammar": "💡 Another reason is ( ) in some countries. の空所は名詞句。直後のsurveyの内容が空所の意味を特定する根拠になる。",
                },
                {
                    "number": 23,
                    "choices": [
                        "collect information about the risks",
                        "choose a clinic with good reviews",
                        "avoid traveling for major dental work",
                        "let the dentists make all the decisions",
                    ],
                    "choiceTranslations": [
                        "リスクについての情報を集める",
                        "評判の良いクリニックを選ぶ",
                        "大きな歯科治療のために旅行を避ける",
                        "歯科医にすべての決定を任せる",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ collect information about the risks＝リスク情報を集める。By doing so, people can clearly understand the possible problems（起こりうる問題を理解する）と呼応→正解",
                        "❌ choose a clinic with good reviews＝評判の良いクリニック。understand the possible problems and make safe choices（安全な選択）の文脈で、reviews（口コミ）の記述はない",
                        "❌ avoid traveling for major dental work＝大きな治療の旅行を避ける。make safe choices about getting dental care abroad（安全な選択）を促すが、旅行禁止の話ではない",
                        "❌ let the dentists make all the decisions＝歯科医にすべて任せる。people should be careful about the dangers（危険性に注意）と矛盾。自分で情報を得るべき",
                    ],
                    "sourceEvidence": [
                        "people can clearly understand the possible problems and make safe choices about getting dental care abroad.",
                    ],
                    "grammar": "💡 Therefore, it is important to ( ). By doing so, ... の空所は「そうすることで」の内容を先読みする。understand the possible problems が決め手。",
                },
            ],
        },
    ],
}

# choiceAnalysis に ✅/❌ マークを付与（大問1・3とスタイル統一）
for pa in section2["passages"]:
    for q in pa["questions"]:
        marked = []
        for i, t in enumerate(q["choiceAnalysis"]):
            if t.startswith(("✅", "❌")):
                marked.append(t)
            else:
                marked.append(("✅ " if i + 1 == q["answer"] else "❌ ") + t)
        q["choiceAnalysis"] = marked

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

# 大問2のみ差し替え、他のセクション（大問1・3）は保持する
sections = data.get("sections", [])
others_before = [s for s in sections if s.get("name") == "大問1"]
others_after = [s for s in sections if s.get("name") not in ("大問1", "大問2")]
data["sections"] = others_before + [section2] + others_after

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 (6 questions, 2 passages) to {DATA_PATH}")
