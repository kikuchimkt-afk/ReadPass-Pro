# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス data.json
Step C: 大問3（reading-comprehension型）Q24〜31
  3A Apartment viewing information / 3B A Fifteen-Minute City
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

p3a_paras = [
    "Dear Nick,\nMy name is Lucy Henderson, and I work for CMW Apartments. Thank you for contacting us. Your email mentioned that you were looking for a quiet apartment to live alone because you would start college in September. We understand that you prefer a safe neighborhood with good access to public transportation. Although the kitchen is not very important, you said having some private outdoor space was necessary.",
    "We found an apartment that we thought would suit you well. It is in a quiet neighborhood, and the living room is separate from the bedroom. There are some shops and restaurants nearby. A bus stop is just two minutes away. The rent is $850 per month, and it includes the Internet, but not water or electricity. The apartment will be available by late August. The balcony is a bit small, but it gets plenty of light.",
    "If this apartment sounds good, please let us know when you are free to come and see it. As the apartment might be rented soon by someone else, we recommend arranging a viewing as soon as possible. If you decide to rent it after your visit, you will need to follow the next steps, including signing the agreement. We recommend finishing this process at our office before August 10.\nThank you,\nLucy Henderson",
]

p3a_trans = [
    "ニックへ\n私はCMWアパートメントのルーシー・ヘンダーソンです。お問い合わせありがとうございます。9月に大学を始めるので一人暮らしの静かなアパートを探しているとのこと、承知しました。安全な地区で公共交通機関へのアクセスが良いことを希望されていることも理解しています。キッチンはあまり重要ではないものの、プライベートな屋外スペースが必要だとおっしゃっていました。",
    "あなたに合いそうなアパートを見つけました。静かな地区にあり、リビングルームと寝室は別です。近くに店やレストランがあります。バス停までわずか2分です。家賃は月850ドルで、インターネットは含まれますが、水道と電気は含まれません。アパートは8月下旬までに利用可能になります。バルコニーは少し小さいですが、十分な光が入ります。",
    "このアパートがよさそうでしたら、内見に来られる日程をお知らせください。他の人に借りられてしまう可能性があるため、できるだけ早く内見の手配をお勧めします。見学後に借りることを決めた場合は、契約書への署名を含む次のステップに従う必要があります。8月10日までに当社オフィスでこの手続きを終えることをお勧めします。\nありがとうございます。\nルーシー・ヘンダーソン",
]

p3a_pairs = [
    [
        "Your email mentioned that you were looking for a quiet apartment to live alone because you would start college in September.",
        "9月に大学を始めるので一人暮らしの静かなアパートを探しているとのこと、承知しました。",
    ],
    [
        "We understand that you prefer a safe neighborhood with good access to public transportation.",
        "安全な地区で公共交通機関へのアクセスが良いことを希望されていることも理解しています。",
    ],
    [
        "Although the kitchen is not very important, you said having some private outdoor space was necessary.",
        "キッチンはあまり重要ではないものの、プライベートな屋外スペースが必要だとおっしゃっていました。",
    ],
    [
        "The balcony is a bit small, but it gets plenty of light.",
        "バルコニーは少し小さいですが、十分な光が入ります。",
    ],
    [
        "We recommend finishing this process at our office before August 10.",
        "8月10日までに当社オフィスでこの手続きを終えることをお勧めします。",
    ],
]

p3b_paras = [
    "In recent years, a new city planning project has begun in Paris, France. It is called the \"fifteen-minute city.\" This concept is based on the idea that important places for daily life, such as schools, hospitals, offices, and parks, should be located close to people's homes. This means that the city should have a system that allows people to walk or ride a bicycle to these places easily. Since the project began, the city has seen huge changes.",
    "There is a strong reason why this idea was proposed. Today, Paris is working to lower the amount of carbon dioxide released to reduce the level of harmful air pollution. One way to do this is by encouraging people to use cars less. Through the fifteen-minute city concept, citizens can expect to get around the city more easily. The project helps provide improved access to services necessary for daily life. Therefore, it can lead to a better quality of life for people.",
    "As part of the fifteen-minute city project, bicycle lanes were introduced on a large scale. Also, the city uses unique approaches to utilize empty spaces. For example, a building once used by the government is now a space offering a market, a hotel, restaurants, and even a rooftop garden. Parking areas that were not often used were replaced with houses. An old hospital was turned into a school with a library and a sports ground that local people can use after school and on school holidays.",
    "The fifteen-minute city project in Paris is getting attention around the world and is spreading to other cities. Cities such as Busan in South Korea and Cleveland in the United States are now trying similar plans. In fact, the city of Utrecht in the Netherlands is aiming to become a \"ten-minute city.\" The efforts of these cities may prove that it is possible to achieve important changes on a city scale to help solve the global problem of climate change today.",
]

p3b_trans = [
    "近年、フランス・パリで新しい都市計画プロジェクトが始まりました。「15分都市」と呼ばれています。この概念は、学校、病院、オフィス、公園など日常生活に重要な場所が人々の家の近くにあるべきだという考えに基づいています。つまり、人々がこれらの場所に歩いたり自転車で行ったりしやすい仕組みが都市にあるべきだということです。プロジェクトが始まって以来、都市は大きな変化を見ています。",
    "この考えが提案されたには強い理由があります。今日、パリは有害な大気汚染のレベルを下げるために二酸化炭素の排出量を減らそうとしています。その方法の一つは、人々に車の使用を減らすよう促すことです。15分都市の概念を通じて、市民は都市内をより簡単に移動できると期待できます。このプロジェクトは日常生活に必要なサービスへのアクセス改善に役立ちます。したがって、人々の生活の質の向上につながる可能性があります。",
    "15分都市プロジェクトの一環として、自転車専用道路が大規模に導入されました。また、都市は空きスペースを活用する独自のアプローチを使っています。例えば、かつて政府が使っていた建物は、市場、ホテル、レストラン、さらには屋上庭園を備えた空間になっています。あまり使われていなかった駐車場は住宅に置き換えられました。古い病院は、図書館と運動場を備えた学校に改装され、地元の人々が放課後や学校の休日に利用できます。",
    "パリの15分都市プロジェクトは世界中で注目を集め、他の都市にも広がっています。韓国の釜山やアメリカのクリーブランドなどの都市が、同様の計画に取り組んでいます。実際、オランダのユトレヒトは「10分都市」を目指しています。これらの都市の取り組みは、都市規模で重要な変化を達成し、今日の気候変動という世界的問題の解決に役立つことが可能であることを証明するかもしれません。",
]

p3b_pairs = [
    [
        "This concept is based on the idea that important places for daily life, such as schools, hospitals, offices, and parks, should be located close to people's homes.",
        "この概念は、学校、病院、オフィス、公園など日常生活に重要な場所が人々の家の近くにあるべきだという考えに基づいています。",
    ],
    [
        "One way to do this is by encouraging people to use cars less.",
        "その方法の一つは、人々に車の使用を減らすよう促すことです。",
    ],
    [
        "An old hospital was turned into a school with a library and a sports ground that local people can use after school and on school holidays.",
        "古い病院は、図書館と運動場を備えた学校に改装され、地元の人々が放課後や学校の休日に利用できます。",
    ],
    [
        "Cities such as Busan in South Korea and Cleveland in the United States are now trying similar plans.",
        "韓国の釜山やアメリカのクリーブランドなどの都市が、同様の計画に取り組んでいます。",
    ],
    [
        "bicycle lanes were introduced on a large scale.",
        "自転車専用道路が大規模に導入されました。",
    ],
    [
        "Parking areas that were not often used were replaced with houses.",
        "あまり使われていなかった駐車場は住宅に置き換えられました。",
    ],
]

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文 A, B の内容に関して, (24) から (31) までの質問に対して最も適切なもの, または文を完成させるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び, その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Apartment viewing information",
            "format": "email",
            "meta": {
                "from": "Lucy Henderson <service@cmw-apartments.com>",
                "to": "Nick King <n.king-0328@zero-borders.com>",
                "date": "July 29",
                "subject": "Apartment viewing information",
            },
            "paragraphs": p3a_paras,
            "translations": p3a_trans,
            "sentencePairs": p3a_pairs,
            "questions": [
                {
                    "number": 24,
                    "question": "Nick King is looking for an apartment that",
                    "questionTranslation": "ニック・キングが探しているアパートは（　）ものである。",
                    "choices": [
                        "offers a big indoor area to live in with some roommates.",
                        "includes some outdoor space that is shared with others.",
                        "sits in a quiet area with easy access to local transport options.",
                        "has a kitchen that is big enough for a single person to cook.",
                    ],
                    "choiceTranslations": [
                        "ルームメイトと一緒に住むための広い屋内スペースを提供する",
                        "他の人と共有する屋外スペースを含む",
                        "静かな地区にあり、地域の交通手段にアクセスしやすい",
                        "一人で料理するのに十分な大きさのキッチンがある",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ ルームメイトと広い屋内→live alone（一人暮らし）と矛盾。roommates の記述はない",
                        "❌ 共有の屋外スペース→private outdoor space（プライベートな屋外スペース）と正反対",
                        "✅ 静かな地区＋交通アクセス→正解。💡 quiet apartment＋good access to public transportation",
                        "❌ 大きなキッチン→Although the kitchen is not very important（キッチンは重要でない）と矛盾",
                    ],
                    "sourceEvidence": [
                        "looking for a quiet apartment to live alone",
                        "prefer a safe neighborhood with good access to public transportation",
                    ],
                    "grammar": "💡 live alone＝一人暮らし。private outdoor space＝個人用の屋外スペース。設問はニックの希望条件をまとめて問う。",
                },
                {
                    "number": 25,
                    "question": "What is true about the apartment that Lucy Henderson offers?",
                    "questionTranslation": "ルーシー・ヘンダーソンが提案するアパートについて正しいのはどれか？",
                    "choices": [
                        "It has a living room that is also used as a bedroom.",
                        "It comes with a balcony that gets good sunlight.",
                        "It includes the water and electricity fees in the rent.",
                        "It is ready for Nick to move anytime in August.",
                    ],
                    "choiceTranslations": [
                        "リビングルームが寝室としても使われている",
                        "日当たりの良いバルコニーが付いている",
                        "家賃に水道と電気代が含まれている",
                        "8月中いつでも入居できる",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ リビングが寝室兼用→the living room is separate from the bedroom（別々）と矛盾",
                        "✅ 日当たりの良いバルコニー→正解。💡 The balcony ... gets plenty of light",
                        "❌ 水道・電気込み→includes the Internet, but not water or electricity と矛盾",
                        "❌ 8月中いつでも→available by late August（8月下旬までに）であり anytime ではない",
                    ],
                    "sourceEvidence": [
                        "the living room is separate from the bedroom",
                        "The balcony is a bit small, but it gets plenty of light",
                        "includes the Internet, but not water or electricity",
                    ],
                    "grammar": "💡 separate from＝～と別の。plenty of light＝十分な日光。but not water or electricity で含まれない費用を確認する。",
                },
                {
                    "number": 26,
                    "question": "What does Nick need to do to rent the apartment?",
                    "questionTranslation": "アパートを借りるためにニックが必要なことは何か？",
                    "choices": [
                        "Attend a viewing on August 10 as a first step.",
                        "Visit Lucy's office before a viewing.",
                        "Sign the agreement by August 10 after a viewing.",
                        "Make an appointment for a viewing after August 10.",
                    ],
                    "choiceTranslations": [
                        "第一歩として8月10日に内見に参加する",
                        "内見の前にルーシーのオフィスを訪れる",
                        "内見の後、8月10日までに契約書に署名する",
                        "8月10日以降に内見の予約をする",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 8月10日に内見→August 10は内見日ではなく手続き完了の期限",
                        "❌ 内見前にオフィス訪問→visit before a viewing の記述はない",
                        "✅ 内見後に8月10日までに署名→正解。💡 after your visit ... signing the agreement ... before August 10",
                        "❌ 8月10日以降に予約→as soon as possible（できるだけ早く）と矛盾",
                    ],
                    "sourceEvidence": [
                        "If you decide to rent it after your visit, you will need to follow the next steps, including signing the agreement",
                        "We recommend finishing this process at our office before August 10",
                    ],
                    "grammar": "💡 after your visit＝見学の後。before August 10＝8月10日までに。内見→契約署名→期限、の順序を追う。",
                },
            ],
        },
        {
            "label": "B",
            "title": "A Fifteen-Minute City",
            "paragraphs": p3b_paras,
            "translations": p3b_trans,
            "sentencePairs": p3b_pairs,
            "questions": [
                {
                    "number": 27,
                    "question": "What idea is the concept of \"the fifteen-minute city\" based on?",
                    "questionTranslation": "「15分都市」の概念はどのような考えに基づいているか？",
                    "choices": [
                        "The city should be designed to give people easy access to important services.",
                        "Local people should travel more to see different parts of the city.",
                        "Better parking is needed to get to schools and offices easily.",
                        "More people should live at least fifteen minutes away from the city.",
                    ],
                    "choiceTranslations": [
                        "人々が重要なサービスに簡単にアクセスできるよう都市を設計すべき",
                        "地元の人々は都市のさまざまな場所を見るためにより多く移動すべき",
                        "学校やオフィスに簡単に行くためにより良い駐車場が必要",
                        "より多くの人が都市から少なくとも15分離れた場所に住むべき",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ 重要なサービスへのアクセス→正解。💡 important places ... should be located close to people's homes / walk or ride a bicycle to these places easily",
                        "❌ より多く移動→家の近くに重要な場所を置く話であり、travel more とは逆",
                        "❌ 駐車場の改善→use cars less（車を減らす）と矛盾。parking の改善は主題ではない",
                        "❌ 15分離れて住む→close to people's homes（家の近く）と正反対",
                    ],
                    "sourceEvidence": [
                        "important places for daily life, such as schools, hospitals, offices, and parks, should be located close to people's homes",
                        "allows people to walk or ride a bicycle to these places easily",
                    ],
                    "grammar": "💡 be based on the idea that ～＝～という考えに基づく。close to people's homes が設計思想の核心。",
                },
                {
                    "number": 28,
                    "question": "Why did Paris start the project of the fifteen-minute city?",
                    "questionTranslation": "パリが15分都市プロジェクトを始めた理由は何か？",
                    "choices": [
                        "To create more space for nature to improve air quality in the city.",
                        "To grow the economy by attracting more cars entering the city.",
                        "To bring in businesses related to everyday life to make the city better.",
                        "To encourage people to drive less to solve environmental problems.",
                    ],
                    "choiceTranslations": [
                        "都市の大気質を改善するために自然のためのスペースを増やすため",
                        "都市に入る車を増やして経済を成長させるため",
                        "日常生活に関連するビジネスを呼び込んで都市を良くするため",
                        "環境問題を解決するために人々の運転を減らすよう促すため",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 自然のスペース→lower carbon dioxide / air pollution の話はあるが、more space for nature の記述はない",
                        "❌ 車を増やす→encouraging people to use cars less と正反対",
                        "❌ ビジネスを呼び込む→bring in businesses の記述はない",
                        "✅ 運転を減らして環境問題を解決→正解。💡 lower carbon dioxide ... harmful air pollution / encouraging people to use cars less",
                    ],
                    "sourceEvidence": [
                        "Paris is working to lower the amount of carbon dioxide released to reduce the level of harmful air pollution",
                        "One way to do this is by encouraging people to use cars less",
                    ],
                    "grammar": "💡 lower the amount of carbon dioxide＝二酸化炭素排出量を減らす。One way to do this is by ～ing＝その方法の一つは～することだ。",
                },
                {
                    "number": 29,
                    "question": "As part of creating the fifteen-minute city of Paris,",
                    "questionTranslation": "パリの15分都市づくりの一環として、（　）。",
                    "choices": [
                        "a rooftop garden was created to encourage farming in the city.",
                        "some of the old local services were replaced with government services.",
                        "a former medical institution became a school with some services for local people.",
                        "some parking areas were open to the local people during the holidays.",
                    ],
                    "choiceTranslations": [
                        "都市での農業を促進するために屋上庭園が作られた",
                        "古い地域サービスの一部が政府サービスに置き換えられた",
                        "かつての医療施設が、地元住民向けのサービスを備えた学校になった",
                        "一部の駐車場が休日に地元住民に開放された",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 農業促進の屋上庭園→rooftop garden はあるが encourage farming（農業促進）の記述はない",
                        "❌ 政府サービスに置換→government building が market/hotel 等に変わった話。local services → government ではない",
                        "✅ 医療施設が学校に→正解。💡 An old hospital was turned into a school with a library and a sports ground that local people can use",
                        "❌ 休日に駐車場開放→Parking areas ... were replaced with houses（住宅に置換）であり open during holidays ではない",
                    ],
                    "sourceEvidence": [
                        "An old hospital was turned into a school with a library and a sports ground that local people can use after school and on school holidays",
                    ],
                    "grammar": "💡 be turned into ～＝～に改装される。As part of creating ... の空所は第3段落の具体例を探す。",
                },
                {
                    "number": 30,
                    "question": "What impact has Paris's fifteen-minute city project had?",
                    "questionTranslation": "パリの15分都市プロジェクトはどのような影響を与えたか？",
                    "choices": [
                        "Cleveland has already developed itself in the same way as Paris.",
                        "Utrecht followed Paris and successfully achieved the fifteen-minute city project.",
                        "Busan has found it hard to start a similar project.",
                        "Some cities in other countries are trying similar plans.",
                    ],
                    "choiceTranslations": [
                        "クリーブランドはすでにパリと同じように発展した",
                        "ユトレヒトはパリに続き15分都市を成功させた",
                        "釜山は同様のプロジェクトを始めるのが難しいとわかった",
                        "他国のいくつかの都市が同様の計画に取り組んでいる",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ クリーブランドはすでに同様に→are now trying similar plans（試みている）であり already developed ではない",
                        "❌ ユトレヒトは成功→aiming to become a ten-minute city（目指している）であり successfully achieved ではない",
                        "❌ 釜山は困難→found it hard の記述はなく、trying similar plans と矛盾",
                        "✅ 他国の都市が同様の計画→正解。💡 spreading to other cities / Busan and Cleveland ... trying similar plans",
                    ],
                    "sourceEvidence": [
                        "is spreading to other cities",
                        "Cities such as Busan in South Korea and Cleveland in the United States are now trying similar plans",
                    ],
                    "grammar": "💡 spread to other cities＝他の都市に広がる。are now trying similar plans＝同様の計画に取り組んでいる（進行中）。",
                },
                {
                    "number": 31,
                    "question": "What do we learn from the passage?",
                    "questionTranslation": "本文からわかることはどれか？",
                    "choices": [
                        "The Paris example shows how personal efforts can solve environmental problems.",
                        "Adding bicycle lanes and using empty spaces can help make the fifteen-minute city a reality.",
                        "The project will take a while to attract interest around the world.",
                        "The project caused a drop in the number of houses in Paris.",
                    ],
                    "choiceTranslations": [
                        "パリの例は個人の努力が環境問題を解決できることを示す",
                        "自転車専用道路の追加と空きスペースの活用が15分都市の実現に役立つ",
                        "プロジェクトが世界中の関心を集めるには時間がかかる",
                        "プロジェクトはパリの住宅数の減少を引き起こした",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 個人の努力→city scale（都市規模）の変化の話。personal efforts とは異なる",
                        "✅ 自転車レーンと空きスペース活用→正解。💡 bicycle lanes were introduced / utilize empty spaces が第3段落の具体策",
                        "❌ 関心を集めるのに時間→getting attention around the world（すでに注目）と矛盾",
                        "❌ 住宅数の減少→Parking areas were replaced with houses（住宅が増える方向）と矛盾",
                    ],
                    "sourceEvidence": [
                        "bicycle lanes were introduced on a large scale",
                        "the city uses unique approaches to utilize empty spaces",
                    ],
                    "grammar": "💡 What do we learn from the passage?＝本文全体の要点を問う総合問題。第3段落の具体例（bicycle lanes, empty spaces）が手がかり。",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

sections = data.get("sections", [])
s1 = sections[0] if sections and sections[0].get("name") == "大問1" else None
s2 = sections[1] if len(sections) >= 2 and sections[1].get("name") == "大問2" else None
if s1 and s2:
    data["sections"] = [s1, s2, section3]
elif s1:
    data["sections"] = [s1, section3]
else:
    data["sections"] = [section3]

errors = []
for pa in section3["passages"]:
    text = " ".join(pa["paragraphs"])
    for pair in pa["sentencePairs"]:
        if pair[0] not in text:
            errors.append(f"NOT FOUND in '{pa['title']}': {pair[0][:60]}")

if errors:
    print("sentencePairs エラー:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(pa["questions"]) for pa in section3["passages"])
print(f"Wrote section3 ({q_count} questions, 2 passages) to {DATA_PATH}")
