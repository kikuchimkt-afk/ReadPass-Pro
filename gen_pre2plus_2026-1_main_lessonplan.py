# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス data.json
Step D: lessonPlan（focusPoints × 5）
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "言語に依存しない案内（Therefore / However / In this way）",
    "subtitle": "Language-Independent Signs: Cause, Contrast & Result",
    "explanation": (
        "大問2A「Guide Signs Without Words」では、ピクトグラムが言葉ではなく画像で情報を伝えることで、"
        "言語差による問題を避けられる、という因果関係が Therefore で結ばれます。"
        "However 以降は初期デザインの問題点（too complex / too detailed）への転換で、Q19の空所 issue with the early designs を読み取ります。"
        "1964年東京大会での簡素化の成功のあと In this way で新基準が設定された、という結果の結びつけが Q20 の核心です。"
    ),
    "sourceQuote": "do not depend on language / use images instead of words / too complex in style and too detailed / In this way, a new standard for pictograms was set",
    "sourceLocation": "大問2A「Guide Signs Without Words」",
    "examples": [
        {
            "en": "They do not depend on language. This is because they use images instead of words to share information.",
            "ja": "言語に依存しません。これは、情報を共有するために言葉の代わりに画像を使うからです。",
            "note": "do not depend on ～＝～に依存しない。instead of ～＝～の代わりに。Q18の根拠となる因果。",
        },
        {
            "en": "However, there was one issue with the early designs. They were often too complex in style and too detailed.",
            "ja": "しかし、初期のデザインには一つ問題がありました。スタイルが複雑すぎ、詳細すぎることが多かったのです。",
            "note": "However＝「しかし」対比・転換。there was one ～＝一つ～があった。Q19の決め手。",
        },
        {
            "en": "Their success demonstrated how effective simple visual communication could be. In this way, a new standard for pictograms was set.",
            "ja": "その成功は、シンプルな視覚的コミュニケーションがいかに効果的かを示しました。このようにして、ピクトグラムの新しい基準が設定されました。",
            "note": "In this way＝「このようにして」。success → new standard の因果。Q20の正解接続詞。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Guide Signs Without Words]\n"
            "Pictograms are a type of guide sign. They do not depend on language. This is because they use images instead of words to share information. Therefore, problems caused by language differences can be avoided. This makes pictograms useful for people around the world because they can easily and quickly understand what the images mean.\n"
            "However, there was one issue with the early designs. They were often too complex in style and too detailed, which made them difficult to understand quickly. A major change in pictograms was introduced at the 1964 Tokyo Olympic Games. Their success demonstrated how effective simple visual communication could be. In this way, a new standard for pictograms was set."
        ),
        "ja": (
            "ピクトグラムは案内標識の一種です。言語に依存しません。これは、情報を共有するために言葉の代わりに画像を使うからです。したがって、言語の違いによって引き起こされる問題は避けられます。世界中の人々が画像の意味を簡単かつ素早く理解できるため、ピクトグラムは有用です。\n"
            "しかし、初期のデザインには一つ問題がありました。スタイルが複雑すぎ、詳細すぎることが多く、素早く理解するのが難しかったのです。1964年の東京オリンピックでピクトグラムに大きな変化が導入されました。その成功は、シンプルな視覚的コミュニケーションがいかに効果的かを示しました。このようにして、ピクトグラムの新しい基準が設定されました。"
        ),
        "audioFile": "audio/practice_pp1.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q18で problems caused by language differences が正解になる理由を、直前の2文から説明してください。",
            "a": "do not depend on language（言語に依存しない）＋use images instead of words（言葉の代わりに画像）→ 言語差が問題の原因であることを避けられる、という Therefore 前後の因果。",
        },
        {
            "q": "Q19の However は段落内でどのような役割を果たしていますか？",
            "a": "第1段落までの「ピクトグラムの利点」から、「初期デザインの問題点」への転換。However の直後に there was one issue と問題が明示される。",
        },
        {
            "q": "「In this way」の way は何を指しますか？",
            "a": "直前の simpler pictograms の成功（シンプルな視覚的コミュニケーションが効果的だったこと）を指す。その方法・結果として新基準が設定された。",
        },
    ],
    "highlightPatterns": [
        "They do not depend on language",
        "use images instead of words to share information",
        "Therefore, problems",
        "too complex in style and too detailed",
        "Their success demonstrated how effective simple visual communication could be",
        "a new standard for pictograms was set",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "因果・転換",
}

fp2 = {
    "id": "fp2",
    "title": "注意力とスマホの影響（As a result / when people are / This means）",
    "subtitle": "Attention Span & Mobile Phone Effects",
    "explanation": (
        "大問2B「Attention Span」は、調査結果→原因（スマホ）→結果（脳の変化）→悪影響の拡大→対策、という論説構成です。"
        "Q21は As a result で、短い動画が注意力を要しないことと脳が少量の情報に慣れることの因果を結びます。"
        "Q22は when people are not using their phones のときでも集中できない、という一見逆説的な文を、For example 以降の reading books で読み解きます。"
        "Q23は This means で空所の内容を言い換え、personal attention rhythms と when they can and cannot focus during the day が一致します。"
    ),
    "sourceQuote": "As a result, the human brain becomes used to / when people are not using their phones / This means people should know when they can and cannot focus",
    "sourceLocation": "大問2B「Attention Span」",
    "examples": [
        {
            "en": "These platforms hardly require a long attention span. As a result, the human brain becomes used to receiving only small amounts of information.",
            "ja": "これらのプラットフォームは長い注意力をほとんど必要としません。その結果、人間の脳は少量の情報しか受け取らないことに慣れてしまいます。",
            "note": "As a result＝その結果。hardly require a long attention span → brain becomes used to small amounts。Q21の因果。",
        },
        {
            "en": "Problems can even occur when people are not using their phones. For example, people who often use their mobile phones are less likely to stay focused on reading books.",
            "ja": "人々が携帯電話を使っていないときでさえ、問題が起こることがあります。例えば、携帯電話をよく使う人は、本を読むことに集中しにくくなっています。",
            "note": "when people are not using their phones＝スマホを使っていない別の活動中。Q22の「逆説的」読みの鍵。",
        },
        {
            "en": "In addition, understanding personal attention rhythms is considered helpful. This means people should know when they can and cannot focus during the day.",
            "ja": "さらに、個人の注意力のリズムを理解することが役立つと考えられます。これは、人々が一日のうちいつ集中でき、いつできないかを知るべきだという意味です。",
            "note": "This means ～＝これは～という意味だ。空所の言い換え確認。Q23の決め手。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Attention Span]\n"
            "One key reason for this is mobile phones. Today, many people use social media platforms that show short videos and messages. These platforms hardly require a long attention span. As a result, the human brain becomes used to receiving only small amounts of information.\n"
            "Problems can even occur when people are not using their phones. For example, people who often use their mobile phones are less likely to stay focused on reading books or remembering information.\n"
            "In addition, understanding personal attention rhythms is considered helpful. This means people should know when they can and cannot focus during the day."
        ),
        "ja": (
            "主な理由の一つは携帯電話です。今日、多くの人が短い動画やメッセージを見せるソーシャルメディアのプラットフォームを使っています。これらのプラットフォームは長い注意力をほとんど必要としません。その結果、人間の脳は少量の情報しか受け取らないことに慣れてしまいます。\n"
            "人々が携帯電話を使っていないときでさえ、問題が起こることがあります。例えば、携帯電話をよく使う人は、本を読んだり情報を覚えたりすることに集中しにくくなっています。\n"
            "さらに、個人の注意力のリズムを理解することが役立つと考えられます。これは、人々が一日のうちいつ集中でき、いつできないかを知るべきだという意味です。"
        ),
        "audioFile": "audio/practice_pp2.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q22で「スマホをよく使う人」という例が、空所 not using their phones とどう結びつきますか？",
            "a": "スマホ依存により、スマホを使っていないとき（読書など）でも集中力が続かない、という悪影響の広がり。often use phones なのに problems when NOT using phones という対比を読む。",
        },
        {
            "q": "Q23の This means 以降から空所を先読みする手順を説明してください。",
            "a": "This means people should know when they can and cannot focus during the day → 空所は「いつ集中できるかを知る」ことに関する名詞句。正解は personal attention rhythms。",
        },
    ],
    "highlightPatterns": [
        "One key reason for this is mobile phones",
        "hardly require a long attention span",
        "the human brain becomes used to receiving only small amounts of information",
        "Problems can even occur when people are",
        "less likely to stay focused on reading books",
        "when they can and cannot focus during the day",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "注意力",
}

fp3 = {
    "id": "fp3",
    "title": "アパート案内メール（live alone / private outdoor space / before August 10）",
    "subtitle": "Apartment Rental Email: Conditions & Deadlines",
    "explanation": (
        "大問3Aのメールは、ニックの希望条件の確認→物件の紹介→内見の案内→契約手続きの期限、という実用的な構成です。"
        "live alone と quiet apartment、private outdoor space が Q24 の核心で、shared outdoor space や roommates は誤答の典型です。"
        "separate from the bedroom と plenty of light が Q25 の根拠。"
        "after your visit ... signing the agreement ... before August 10 の順序が Q26 の鍵です。"
    ),
    "sourceQuote": "looking for a quiet apartment to live alone / private outdoor space / the living room is separate from the bedroom / finishing this process at our office before August 10",
    "sourceLocation": "大問3A「Apartment viewing information」",
    "examples": [
        {
            "en": "Your email mentioned that you were looking for a quiet apartment to live alone because you would start college in September.",
            "ja": "9月に大学を始めるので一人暮らしの静かなアパートを探しているとのこと、承知しました。",
            "note": "live alone＝一人暮らし。quiet apartment＝静かなアパート。Q24の条件の一部。",
        },
        {
            "en": "Although the kitchen is not very important, you said having some private outdoor space was necessary.",
            "ja": "キッチンはあまり重要ではないものの、プライベートな屋外スペースが必要だとおっしゃっていました。",
            "note": "private outdoor space＝個人用の屋外スペース。shared（共有）との対比が誤答排除の鍵。",
        },
        {
            "en": "We recommend finishing this process at our office before August 10.",
            "ja": "8月10日までに当社オフィスでこの手続きを終えることをお勧めします。",
            "note": "before August 10＝8月10日までに。viewing on August 10（その日に内見）とは異なる。Q26。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Apartment viewing information]\n"
            "Your email mentioned that you were looking for a quiet apartment to live alone because you would start college in September. We understand that you prefer a safe neighborhood with good access to public transportation. Although the kitchen is not very important, you said having some private outdoor space was necessary.\n"
            "It is in a quiet neighborhood, and the living room is separate from the bedroom. The balcony is a bit small, but it gets plenty of light. The rent includes the Internet, but not water or electricity.\n"
            "If you decide to rent it after your visit, you will need to follow the next steps, including signing the agreement. We recommend finishing this process at our office before August 10."
        ),
        "ja": (
            "9月に大学を始めるので一人暮らしの静かなアパートを探しているとのこと、承知しました。安全な地区で公共交通機関へのアクセスが良いことを希望されていることも理解しています。キッチンはあまり重要ではないものの、プライベートな屋外スペースが必要だとおっしゃっていました。\n"
            "静かな地区にあり、リビングルームと寝室は別です。バルコニーは少し小さいですが、十分な光が入ります。家賃にはインターネットが含まれますが、水道と電気は含まれません。\n"
            "見学後に借りることを決めた場合は、契約書への署名を含む次のステップに従う必要があります。8月10日までに当社オフィスでこの手続きを終えることをお勧めします。"
        ),
        "audioFile": "audio/practice_pp3.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q24で shared outdoor space が誤答になる理由は？",
            "a": "本文は private outdoor space（個人用の屋外スペース）。shared（他の人と共有）とは意味が正反対。",
        },
        {
            "q": "Q26で August 10 が「内見の日」ではなく「手続きの期限」である根拠は？",
            "a": "arranging a viewing as soon as possible（できるだけ早く内見）と finishing this process ... before August 10（手続きを8月10日までに）は別の要求。after your visit → signing the agreement の流れを読む。",
        },
    ],
    "highlightPatterns": [
        "looking for a quiet apartment to live alone",
        "good access to public transportation",
        "private outdoor space was necessary",
        "the living room is separate from the bedroom",
        "gets plenty of light",
        "but not water or electricity",
        "after your visit",
        "signing the agreement",
        "before August 10",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "賃貸メール",
}

fp4 = {
    "id": "fp4",
    "title": "15分都市と環境（be based on / use cars less / be turned into）",
    "subtitle": "Fifteen-Minute City: Planning & Environment",
    "explanation": (
        "大問3B「A Fifteen-Minute City」は、概念の説明→環境問題への対応→具体施策→世界への広がり、という4段落構成です。"
        "be based on the idea that important places ... close to people's homes が Q27 の根拠。"
        "lower carbon dioxide / encouraging people to use cars less が Q28 の環境目的。"
        "An old hospital was turned into a school が Q29 の具体例。"
        "spreading to other cities / trying similar plans が Q30 の影響。"
    ),
    "sourceQuote": "based on the idea that important places / encouraging people to use cars less / An old hospital was turned into a school / are now trying similar plans",
    "sourceLocation": "大問3B「A Fifteen-Minute City」",
    "examples": [
        {
            "en": "This concept is based on the idea that important places for daily life should be located close to people's homes.",
            "ja": "この概念は、日常生活に重要な場所が人々の家の近くにあるべきだという考えに基づいています。",
            "note": "be based on the idea that ～＝～という考えに基づく。Q27の核心。",
        },
        {
            "en": "One way to do this is by encouraging people to use cars less.",
            "ja": "その方法の一つは、人々に車の使用を減らすよう促すことです。",
            "note": "encourage people to use cars less＝車の使用を減らすよう促す。Q28の環境対策。",
        },
        {
            "en": "An old hospital was turned into a school with a library and a sports ground that local people can use.",
            "ja": "古い病院は、図書館と運動場を備えた学校に改装され、地元の人々が利用できます。",
            "note": "be turned into ～＝～に改装される。Q29の former medical institution → school の言い換え。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: A Fifteen-Minute City]\n"
            "This concept is based on the idea that important places for daily life, such as schools, hospitals, offices, and parks, should be located close to people's homes. This means that the city should have a system that allows people to walk or ride a bicycle to these places easily.\n"
            "Paris is working to lower the amount of carbon dioxide released to reduce the level of harmful air pollution. One way to do this is by encouraging people to use cars less.\n"
            "bicycle lanes were introduced on a large scale. Also, the city uses unique approaches to utilize empty spaces. An old hospital was turned into a school with a library and a sports ground that local people can use. Cities such as Busan and Cleveland are now trying similar plans."
        ),
        "ja": (
            "この概念は、学校、病院、オフィス、公園など日常生活に重要な場所が人々の家の近くにあるべきだという考えに基づいています。つまり、人々がこれらの場所に歩いたり自転車で行ったりしやすい仕組みが都市にあるべきだということです。\n"
            "パリは有害な大気汚染のレベルを下げるために二酸化炭素の排出量を減らそうとしています。その方法の一つは、人々に車の使用を減らすよう促すことです。\n"
            "自転車専用道路が大規模に導入されました。また、都市は空きスペースを活用する独自のアプローチを使っています。古い病院は、図書館と運動場を備えた学校に改装され、地元の人々が利用できます。釜山やクリーブランドなどの都市が、同様の計画に取り組んでいます。"
        ),
        "audioFile": "audio/practice_pp4.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q29で former medical institution が old hospital の言い換えであることを、選択肢からどう見抜きますか？",
            "a": "medical institution（医療施設）＝hospital（病院）。became a school with some services for local people ＝ turned into a school ... local people can use と一致。",
        },
        {
            "q": "Q30で Utrecht が successfully achieved と誤答になる理由は？",
            "a": "本文は aiming to become a ten-minute city（10分都市を目指している）であり、すでに達成（successfully achieved）したとは書いていない。",
        },
    ],
    "highlightPatterns": [
        "based on the idea that important places",
        "located close to people's homes",
        "encouraging people to use cars less",
        "bicycle lanes were introduced on a large scale",
        "utilize empty spaces",
        "An old hospital was turned into a school",
        "are now trying similar plans",
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "都市計画",
}

fp5 = {
    "id": "fp5",
    "title": "今回の重要パラフレーズ（本文→設問の言い換え）",
    "subtitle": "Key Paraphrases: Text vs. Question Wording",
    "explanation": (
        "本会場では、正解選択肢が本文の表現をそのまま使わないことがほとんどです。"
        "private outdoor space → outdoor space that is shared with others（Q24誤答）のように、"
        "同じ語でも private / shared で意味が変わるケースに注意が必要です。"
        "plenty of light → gets good sunlight（Q25）、"
        "close to people's homes → easy access to important services（Q27）、"
        "encouraging people to use cars less → drive less to solve environmental problems（Q28）など、"
        "名詞句・動詞レベルの言い換えを追う読み方が正答の鍵です。"
    ),
    "sourceQuote": "private outdoor space / gets plenty of light / close to people's homes / use cars less / turned into a school",
    "sourceLocation": "大問3A Q24〜26・大問3B Q27〜31",
    "examples": [
        {
            "en": "本文: 'having some private outdoor space was necessary'\n→ 誤答: 'includes some outdoor space that is shared with others.'",
            "ja": "「個人用の屋外スペース」vs「共有の屋外スペース」",
            "note": "private ⇔ shared。同じ outdoor space でも形容詞で意味が正反対。Q24の誤答パターン。",
        },
        {
            "en": "本文: 'important places ... should be located close to people's homes'\n→ 設問: 'give people easy access to important services.'",
            "ja": "「家の近くに重要な場所」→「重要なサービスへの簡単なアクセス」",
            "note": "close to homes ⇔ easy access to services。Q27のパラフレーズ。",
        },
        {
            "en": "本文: 'encouraging people to use cars less'\n→ 設問: 'encourage people to drive less to solve environmental problems.'",
            "ja": "「車の使用を減らす」→「環境問題解決のために運転を減らす」",
            "note": "use cars less ⇔ drive less。carbon dioxide / air pollution が environmental problems の根拠。Q28。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Apartment viewing information / A Fifteen-Minute City]\n"
            "Although the kitchen is not very important, you said having some private outdoor space was necessary. The balcony is a bit small, but it gets plenty of light.\n"
            "This concept is based on the idea that important places for daily life should be located close to people's homes. One way to do this is by encouraging people to use cars less. bicycle lanes were introduced on a large scale. Also, the city uses unique approaches to utilize empty spaces."
        ),
        "ja": (
            "キッチンはあまり重要ではないものの、プライベートな屋外スペースが必要だとおっしゃっていました。バルコニーは少し小さいですが、十分な光が入ります。\n"
            "この概念は、日常生活に重要な場所が人々の家の近くにあるべきだという考えに基づいています。その方法の一つは、人々に車の使用を減らすよう促すことです。自転車専用道路が大規模に導入されました。また、都市は空きスペースを活用する独自のアプローチを使っています。"
        ),
        "audioFile": "audio/practice_pp5.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q25で plenty of light が good sunlight にどう言い換えられていますか？",
            "a": "plenty of light（十分な光）⇔ good sunlight（良い日光）。どちらもバルコニーの日当たりの良さを表す。",
        },
        {
            "q": "Q31で bicycle lanes と utilize empty spaces がどうまとめられていますか？",
            "a": "本文第3段落の2つの具体策を、Adding bicycle lanes and using empty spaces can help make the fifteen-minute city a reality と総合的に言い換えている。",
        },
    ],
    "highlightPatterns": [
        "private outdoor space",
        "gets plenty of light",
        "based on the idea that important places",
        "encouraging people to use cars less",
        "bicycle lanes were introduced",
        "utilize empty spaces",
        "An old hospital was turned into a school",
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

print(f"Wrote lessonPlan (5 focusPoints) to {DATA_PATH}")
