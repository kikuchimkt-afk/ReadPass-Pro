# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級プラス data.json
Step D: lessonPlan（focusPoints × 5）
本文中に実在する構文のみを使用。practicePassage は試験本文の抜粋＋[出典: タイトル]。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "手順の連鎖と目的の表現（not only ... but also / Eventually / By doing so）",
    "subtitle": "Sequential Actions & Purpose: not only ... but also / Eventually / By doing so",
    "explanation": (
        "大問2A「A Christmas Tradition」では、ファンの行動が「試合を見る→ぬいぐるみを投げる→回収される→届けられる」という時間の連鎖で進みます。"
        "not only A but also B（AだけでなくBも）は「2つの行動・目的」を並べる定番構文で、空所問題Q18の前後関係を読む鍵になります。"
        "Eventually（最終的に）は手順の最後の段階を示し、By doing so（そうすることで）は直前の行動がもたらす結果を結びつけます。"
        "Q19の with a specific purpose in mind も同じく「なぜそうしたか」の目的を補う表現です。"
    ),
    "sourceQuote": "not only to watch a match but also to throw soft toys / these toys are delivered to children who are in need / By doing so, many children both inside and outside the country can receive presents",
    "sourceLocation": "大問2A「A Christmas Tradition」第1・3段落",
    "examples": [
        {
            "en": "On a certain day, they come to the stadium not only to watch a match but also to throw soft toys onto the field.",
            "ja": "ある日、彼らは試合を見るだけでなく、フィールドにぬいぐるみを投げ込みます。",
            "note": "not only to V but also to V＝「～するだけでなく、～もする」。to 不定詞の並列。2つの目的を対等に並べる。",
        },
        {
            "en": "Tens of thousands of such toys are thrown, and then they are immediately collected by volunteers.",
            "ja": "何万ものぬいぐるみが投げられ、すぐにボランティアが回収します。",
            "note": "and then＝「そして次に」。手順の時間順序を示す。immediately collected＝受動態で「すぐに回収される」。",
        },
        {
            "en": "By doing so, many children both inside and outside the country can receive presents during the Christmas season.",
            "ja": "そうすることで、国内外の多くの子どもがクリスマスの季節にプレゼントを受け取れます。",
            "note": "By doing so＝「そうすることで」。so は直前の行動（海外へ送る等）を指す。both A and B＝「AもBも」。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: A Christmas Tradition]\n"
            "Every December, fans of a Spanish professional soccer team take part in a special event. On a certain day, they come to the stadium not only to watch a match but also to throw soft toys onto the field. Tens of thousands of such toys are thrown, and then they are immediately collected by volunteers. Eventually, these toys are delivered to children who are in need.\n"
            "This tradition began in 2018 with a specific purpose in mind. At that time, the soccer club and its fans wanted to do a kind act for local children who were less fortunate than others. Today, it has grown into a larger tradition that spreads kindness across nations. The toys are not only given to children in the local city. Some of the toys are sent to charity organizations in other parts of Spain and even to children overseas. By doing so, many children both inside and outside the country can receive presents during the Christmas season."
        ),
        "ja": (
            "毎年12月、スペインのプロサッカーチームのファンは特別なイベントに参加します。ある日、彼らは試合を見るだけでなく、フィールドにぬいぐるみを投げ込みます。何万ものぬいぐるみが投げられ、すぐにボランティアが回収します。最終的に、これらのぬいぐるみは困っている子どもたちに届けられます。\n"
            "この伝統は2018年、特定の目的を持って始まりました。当時、サッカークラブとファンは、他の子どもより恵まれない地域の子どもたちのために親切な行いをしたいと考えていました。今日、それは国々にわたって親切を広める、より大きな伝統へと成長しました。ぬいぐるみは地元の都市の子どもだけでなく、スペインの他の地域の慈善団体や海外の子どもにも送られます。そうすることで、国内外の多くの子どもがクリスマスの季節にプレゼントを受け取れます。"
        ),
        "audioFile": "audio/practice_pp1.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q18の空所に Eventually が入る理由を、前後の動詞の流れから説明してください。",
            "a": "throw（投げる）→ collect（回収する）→ deliver（届ける）という手順の「最後の段階」を示す接続詞が必要。In contrast や On the other hand は対比、Despite the fact は譲歩で、いずれも手順の連続には合わない。",
        },
        {
            "q": "「not only to watch a match but also to throw soft toys」の not only ... but also は何を並べていますか？",
            "a": "2つの目的（to 不定詞の並列）。「試合を見ること」と「ぬいぐるみを投げること」。ファンがスタジアムに来る2つの理由を対等に示している。",
        },
        {
            "q": "Q19の with a specific purpose in mind と直後の wanted to do a kind act はどう呼応していますか？",
            "a": "空所＝「特定の目的を持って」、直後＝「恵まれない子どもへの親切な行いをしたい」がその目的の具体的内容。purpose in mind → kind act の因果関係を読む。",
        },
        {
            "q": "「By doing so」の so は何を指しますか？本文のどの行動と結びつきますか？",
            "a": "直前の Some of the toys are sent ... even to children overseas（海外の子どもにも送る）という行動を指す。その結果として多くの子どもがプレゼントを受け取れる、という因果の結びつけ。",
        },
    ],
    "highlightPatterns": [
        "not only to watch a match but also to throw soft toys",
        "they are immediately collected by volunteers",
        "these toys are delivered to children who are in need",
        "This tradition began in 2018",
        "wanted to do a kind act for local children",
        "not only given to children in the local city",
        "even to children overseas",
        "By doing so, many children both inside and outside the country",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "手順・目的",
}

fp2 = {
    "id": "fp2",
    "title": "理由の列挙と対策の論理（One reason is / Another reason is / Therefore）",
    "subtitle": "Enumerating Reasons & Drawing Conclusions",
    "explanation": (
        "大問2B「Traveling for Dental Care」は、現象の説明→理由の列挙→注意喚起→対策、という論説文の典型構成です。"
        "One reason is ... / Another reason is ... で複数の原因を整理し、Q22の空所は直後の調査結果（予約できなかった）から「予約の難しさ」と特定します。"
        "According to experts, however で話題を転換し、Therefore, it is important to ... / By doing so, ... で「だから～すべき→そうすれば～できる」という対策の論理を完成させます。"
        "この流れはQ23の正解 collect information about the risks の根拠にも直結します。"
    ),
    "sourceQuote": "One reason is the high cost of treatment / Another reason is / Therefore, it is important to / By doing so, people can clearly understand the possible problems",
    "sourceLocation": "大問2B「Traveling for Dental Care」第2・3段落",
    "examples": [
        {
            "en": "One reason is the high cost of treatment. Some types of dental care in Australia cost more than twice as much as in Thailand.",
            "ja": "理由の一つは治療費の高さです。オーストラリアの一部の歯科治療は、タイの2倍以上の費用がかかります。",
            "note": "One reason is 名詞句＝「理由の一つは～」。直後の具体例（2倍以上）が空所の意味を裏付ける典型パターン。",
        },
        {
            "en": "In a 2024 survey of more than 2,000 people in the United Kingdom, around 20 percent reported that they had tried to book a clinic visit in the past year but could not see a dentist.",
            "ja": "2024年の英国2,000人以上を対象とした調査で、約20％が過去1年にクリニックの予約を試みたが歯科医に診てもらえなかったと報告した。",
            "note": "reported that S + V＝「～と報告した」。but could not see＝「しかし診てもらえなかった」。Q22の根拠文。",
        },
        {
            "en": "Therefore, it is important to collect information about the risks. By doing so, people can clearly understand the possible problems and make safe choices about getting dental care abroad.",
            "ja": "したがって、リスクについての情報を集めることが重要です。そうすることで、起こりうる問題を明確に理解し、海外での歯科治療について安全な選択ができます。",
            "note": "Therefore＝「したがって」結論。it is important to V＝形式主語 it。By doing so は直前の to 不定詞の内容を so で受ける。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Traveling for Dental Care]\n"
            "There are several reasons for this trend. One reason is the high cost of treatment. Some types of dental care in Australia cost more than twice as much as in Thailand. Another reason is the difficulty of making appointments in some countries. In a 2024 survey of more than 2,000 people in the United Kingdom, around 20 percent reported that they had tried to book a clinic visit in the past year but could not see a dentist. These factors lead people to receive dental care in other countries.\n"
            "According to experts, however, people should be careful about the dangers of dental tourism, because there is a possibility of receiving unnecessary treatment or getting treatment using low-quality materials. Also, they may not receive enough legal support if something goes wrong. Therefore, it is important to collect information about the risks. By doing so, people can clearly understand the possible problems and make safe choices about getting dental care abroad."
        ),
        "ja": (
            "この傾向にはいくつかの理由があります。理由の一つは治療費の高さです。オーストラリアの一部の歯科治療は、タイの2倍以上の費用がかかります。もう一つの理由は、一部の国における予約の難しさです。2024年の英国2,000人以上を対象とした調査で、約20％が過去1年にクリニックの予約を試みたが歯科医に診てもらえなかったと報告しました。これらの要因が、人々を他国で歯科治療を受ける方向へ導いています。\n"
            "しかし専門家によると、人々は歯科ツーリズムの危険に注意すべきです。不要な治療を受ける可能性や、品質の低い材料で治療を受ける可能性があるからです。また、何か問題が起きた場合、十分な法的支援を受けられないかもしれません。したがって、リスクについての情報を集めることが重要です。そうすることで、起こりうる問題を明確に理解し、海外での歯科治療について安全な選択ができます。"
        ),
        "audioFile": "audio/practice_pp2.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q22の空所「the difficulty of making appointments」を、直後の調査結果からどう導きますか？",
            "a": "tried to book a clinic visit ... but could not see a dentist（予約を試みたが歯科医に診てもらえなかった）＝予約・診察の機会を得ることの難しさ。difficulty of making appointments の言い換え根拠。",
        },
        {
            "q": "「According to experts, however」は段落の論理でどのような転換を示しますか？",
            "a": "前文までの「海外治療の理由（費用・予約）」から、「しかし危険もある」という注意喚起への転換。however が逆接の合図。",
        },
        {
            "q": "「Therefore, it is important to ( )」の空所を By doing so 以降から先読みする手順を説明してください。",
            "a": "By doing so, people can clearly understand the possible problems → 空所は「問題を理解するために何をすべきか」。正解は collect information about the risks（リスク情報の収集）。",
        },
        {
            "q": "「more than twice as much as in Thailand」の as は何と比較していますか？構文も説明してください。",
            "a": "オーストラリアの治療費とタイの治療費を比較。twice as much as ～＝「～の2倍」。比較対象は as の後ろの in Thailand（タイでの費用）。",
        },
    ],
    "highlightPatterns": [
        "One reason is the high cost of treatment",
        "more than twice as much as in Thailand",
        "Another reason is",
        "tried to book a clinic visit",
        "but could not see a dentist",
        "According to experts, however",
        "Therefore, it is important to",
        "By doing so, people can clearly understand the possible problems",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "理由・対策",
}

fp3 = {
    "id": "fp3",
    "title": "サービス案内メールの表現（look after / cannot ... so / speak with / respond by）",
    "subtitle": "Service Reply Email: Conditions, Limitations & Requests",
    "explanation": (
        "大問3Aの返信メールは、依頼内容の確認→サービス内容の説明→制限事項の告知→料金と条件→返信期限、という実用的なメール構成です。"
        "look after your dog while on a family trip は Q24 の核心で、「旅行中に犬の世話を頼む」と「犬を連れて行く」は全く異なる意味です。"
        "cannot prepare ... so I ask ... to bring は Q25 の正解根拠で、However が注意を引く接続詞として機能します。"
        "Since you are under eighteen, please speak with your parents は Q26 の正解で、18歳未満という条件が保護者への相談を求める理由になります。"
    ),
    "sourceQuote": "looking for someone to look after your dog / I cannot prepare dog food, so I ask dog owners to bring their food / please speak with your parents about my services, including the fee",
    "sourceLocation": "大問3A「Dog Sitting Email」",
    "examples": [
        {
            "en": "I understand you are looking for someone to look after your dog while on a family trip during the school holidays.",
            "ja": "学校の休み中の家族旅行の間、犬の世話をしてくれる人を探しているとのこと、承知しました。",
            "note": "look after ～＝「～の世話をする」。while on a trip＝「旅行中に」。Q24の根拠文。take the dog on the trip とは別の意味。",
        },
        {
            "en": "However, I cannot prepare dog food, so I ask dog owners to bring their food.",
            "ja": "ただし、私は犬用のフードを調理できないため、飼い主の方にフードを持参していただいています。",
            "note": "However＝「ただし」制限の導入。cannot ... so I ask ... to＝「～できないので、～するようお願いする」。Q25の決め手。",
        },
        {
            "en": "Since you are under eighteen, please speak with your parents about my services, including the fee.",
            "ja": "18歳未満の方ですので、料金を含めた私のサービスについて保護者の方と話し合ってください。",
            "note": "Since ～＝「～なので」理由。including the fee＝「料金を含めて」。Q26の正解根拠。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Dog Sitting Email]\n"
            "My name is Emma Lawrence. Thank you for your email. I understand you are looking for someone to look after your dog while on a family trip during the school holidays. I am happy to tell you I am available on the dates you mentioned. I used to work as an animal doctor and have five years of experience as a dog sitter. I am confident that your dog will feel safe and comfortable with me.\n"
            "My services usually include feeding dogs the food you provide, giving them water, and offering snacks if necessary. I take dogs for walks twice a day, for about an hour, and spend time playing with them. I also provide a comfortable place to sleep. However, I cannot prepare dog food, so I ask dog owners to bring their food. Please let me know if there is anything I should know about your dog, such as any health problems.\n"
            "The daily fee is $50. I will be looking after your dog for three days, so the total will be $150. Payment is required before the service. Since you are under eighteen, please speak with your parents about my services, including the fee. Please respond by June 22 if you wish to use my services. I look forward to hearing from you."
        ),
        "ja": (
            "エマ・ローレンスです。メールありがとうございます。学校の休み中の家族旅行の間、犬の世話をしてくれる人を探しているとのこと、承知しました。ご指定の日程で対応可能です。以前は動物の医者として働いており、ドッグシッターとして5年の経験があります。あなたの犬は私と一緒に安全で快適に過ごせると確信しています。\n"
            "私のサービスには、通常、飼い主が用意するフードを与えること、水を与えること、必要ならおやつを与えることが含まれます。1日2回、約1時間散歩に連れて行き、遊ぶ時間も設けます。快適な寝る場所も提供します。ただし、私は犬用のフードを調理できないため、飼い主の方にフードを持参していただいています。健康上の問題など、犬について知っておくべきことがあれば教えてください。\n"
            "1日の料金は50ドルです。3日間お世話するので、合計150ドルになります。サービス前の支払いが必要です。18歳未満の方ですので、料金を含めた私のサービスについて保護者の方と話し合ってください。サービスを利用したい場合は6月22日までにご返信ください。お返事をお待ちしています。"
        ),
        "audioFile": "audio/practice_pp3.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q24で「犬を旅行に連れて行けるか」が誤答になる理由を、look after と take on a trip の違いで説明してください。",
            "a": "look after＝「世話をする」（犬は家に残る）。take on a trip＝「連れて行く」。while on a family trip は飼い主が旅行中という状況設定であり、犬を連れて行く話ではない。",
        },
        {
            "q": "Q25の選択肢4「健康問題があると受け入れない」が誤答になる根拠は？",
            "a": "Please let me know ... such as any health problems は「健康問題があれば知らせてほしい」という情報収集の依頼。cannot welcome（受け入れない）という拒否表現は本文にない。",
        },
        {
            "q": "Q26で「6月22日までに支払う」が誤答になる理由を、本文の2つの期限表現と照合して説明してください。",
            "a": "Payment is required before the service（サービス前の支払い）と Please respond by June 22（6月22日までに返信）は別の要求。June 22は返信期限であり、支払い期限ではない。",
        },
        {
            "q": "「the food you provide」と「I cannot prepare dog food」の関係を整理してください。",
            "a": "エマは飼い主が用意したフードを与える（feeding dogs the food you provide）が、自分でフードを調理・用意することはできない（cannot prepare）。制限とサービス内容の対比。",
        },
    ],
    "highlightPatterns": [
        "looking for someone to look after your dog",
        "while on a family trip during the school holidays",
        "feeding dogs the food you provide",
        "However, I cannot prepare dog food",
        "Please let me know if there is anything I should know",
        "Payment is required before the service",
        "please speak with your parents about my services, including the fee",
        "Please respond by June 22 if you wish to use my services",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "サービスメール",
}

fp4 = {
    "id": "fp4",
    "title": "因果・対比・言い換えの論説表現（However / lead to / In other words / be responsible for）",
    "subtitle": "Cause-Effect & Rephrasing in Expository Writing",
    "explanation": (
        "大問3B「Avocado Production」は、健康上の利点→市場の拡大余地→生産の問題→FAIRTRADEによる解決、という4段落の論説構成です。"
        "which are better than ... found in meat は Q27 のパラフレーズの核心で、healthy fats の比較関係を読み取ります。"
        "there is still room for ... to grow / In other words は Q28 の根拠で、「成長の余地がある」→「市場は成長し続けうる」という言い換えの連鎖です。"
        "lead to reduced prices → earn less money は Q29 の因果連鎖、be responsible for a large part of the global avocado market は Q31 の「主要な消費国」への言い換えの手がかりです。"
    ),
    "sourceQuote": "which are better than other kinds of fats found in meat / there is still room for the avocado market to grow / In other words / which can lead to reduced prices / they are responsible for a large part of the global avocado market",
    "sourceLocation": "大問3B「Avocado Production」第1・2・3段落",
    "examples": [
        {
            "en": "For example, they contain high amounts of healthy fats, which are better than other kinds of fats found in meat.",
            "ja": "例えば、アボカドには健康的な脂肪が多く含まれており、肉に含まれる他の種類の脂肪よりも優れています。",
            "note": "which are better than ～＝関係代名詞の非制限用法で補足説明。Q27「肉より健康的な脂肪」の直接根拠。",
        },
        {
            "en": "However, there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller. In other words, the avocado market in Europe could continue to grow.",
            "ja": "しかし、市場が小さいイタリアや東欧諸国では、アボカド市場が成長する余地がまだあります。言い換えれば、ヨーロッパのアボカド市場は今後も成長し続ける可能性があります。",
            "note": "there is room for ～ to grow＝「～が成長する余地がある」。In other words＝前文の言い換え・要約。Q28の決め手。",
        },
        {
            "en": "the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados. This means that avocado farmers may earn less money and find it harder to continue their business.",
            "ja": "アボカドの大量生産は供給過多を引き起こすことがあり、アボカドの価格下落につながることがあります。つまり、アボカド農家は収入が減り、事業を続けるのが難しくなる可能性があります。",
            "note": "lead to ～＝「～につながる」。This means that ～＝「つまり～ということだ」。Q29の因果の3段階（供給過多→価格下落→収入減）。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Avocado Production]\n"
            "Avocados have been a popular food in many countries around the world. Their health value is especially attractive to people whose diets are based on plants. For example, they contain high amounts of healthy fats, which are better than other kinds of fats found in meat. According to researchers, they can also help reduce the risk of heart disease.\n"
            "Especially in many European countries and the United States, the number of people eating avocados has increased. Because these countries import a lot of avocados, they are responsible for a large part of the global avocado market. In Europe, countries like France and the United Kingdom have already experienced high demand. However, there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller. In other words, the avocado market in Europe could continue to grow.\n"
            "However, there are several problems with avocado production due to its increasing demand. For example, because the production requires a lot of water, increased demand puts pressure on water resources. Also, the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados. This means that avocado farmers may earn less money and find it harder to continue their business."
        ),
        "ja": (
            "アボカドは世界中の多くの国で人気のある食品です。その健康価値は、特に植物中心の食生活を送る人々にとって魅力的です。例えば、アボカドには健康的な脂肪が多く含まれており、肉に含まれる他の種類の脂肪よりも優れています。研究者によると、心臓病のリスクを減らすのにも役立つとされています。\n"
            "特に多くのヨーロッパ諸国とアメリカでは、アボカドを食べる人の数が増えています。これらの国は大量にアボカドを輸入しているため、世界のアボカド市場の大きな部分を占めています。ヨーロッパでは、フランスやイギリスのような国はすでに高い需要を経験しています。しかし、市場が小さいイタリアや東欧諸国では、アボカド市場が成長する余地がまだあります。言い換えれば、ヨーロッパのアボカド市場は今後も成長し続ける可能性があります。\n"
            "しかし、需要の増加により、アボカド生産にはいくつかの問題があります。例えば、生産には多くの水が必要なため、需要の増加は水資源に圧力をかけます。また、アボカドの大量生産は供給過多を引き起こすことがあり、アボカドの価格下落につながることがあります。つまり、アボカド農家は収入が減り、事業を続けるのが難しくなる可能性があります。"
        ),
        "audioFile": "audio/practice_pp4.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q27で「心臓病リスクが高まる」が誤答になる理由を、本文の動詞から説明してください。",
            "a": "本文は reduce the risk of heart disease（リスクを減らす）。increase the risk（リスクを高める）と正反対。healthy fats が better than fats in meat という比較も正解の裏付け。",
        },
        {
            "q": "Q28で「将来フランスに広がる」が誤答になる理由は？",
            "a": "France ... have already experienced high demand（すでに高い需要がある）。will probably spread to France in the future（将来広がる）と矛盾。成長余地があるのは Italy and Eastern European countries。",
        },
        {
            "q": "「In other words」の直前と直後はどのような言い換え関係ですか？",
            "a": "直前＝イタリア・東欧に成長の余地がある（there is still room to grow）→ 直後＝ヨーロッパ市場全体が成長し続けうる（could continue to grow）。部分の事実から全体の見通しへ要約している。",
        },
        {
            "q": "Q31で「アメリカは主要な消費国」を導く本文の表現を2つ挙げてください。",
            "a": "①the number of people eating avocados has increased（食べる人の数が増加）②they are responsible for a large part of the global avocado market（世界市場の大きな部分を占める）。",
        },
    ],
    "highlightPatterns": [
        "which are better than other kinds of fats found in meat",
        "reduce the risk of heart disease",
        "the number of people eating avocados has increased",
        "they are responsible for a large part of the global avocado market",
        "there is still room for the avocado market to grow",
        "In other words, the avocado market in Europe could continue to grow",
        "which can lead to reduced prices for avocados",
        "avocado farmers may earn less money",
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "因果・言い換え",
}

fp5 = {
    "id": "fp5",
    "title": "今回の重要パラフレーズ（本文→設問・選択肢の言い換え）",
    "subtitle": "Key Paraphrases: Text vs. Question Wording",
    "explanation": (
        "準2級プラス読解では、正解の選択肢が本文の表現をそのまま使わないことがほとんどです。"
        "本試験では、look after your dog → request her service to care for his dog（Q24）、"
        "cannot prepare dog food → cannot provide food on her own（Q25）、"
        "still room to grow in Italy and Eastern European countries → will be key to expanding the market（Q28）、"
        "earn fair pay and spend on environmental protection → earn fair pay and spend it on environmental protection（Q30）など、"
        "動詞・名詞句レベルの言い換えに気づけるかが正答の鍵です。"
        "誤答はしばしば本文の単語を使いながら意味をねじ曲げる（health problems で拒否、June 22 で支払い期限など）ため、"
        "「同じ語が出ていても意味が一致するか」を必ず確認する読み方が重要です。"
    ),
    "sourceQuote": "look after your dog → care for his dog / cannot prepare dog food → cannot provide food on her own / still room to grow → key to expanding / receive a fair amount of money → earn fair pay",
    "sourceLocation": "大問3A Q24〜26・大問3B Q27〜31",
    "examples": [
        {
            "en": "本文: 'you are looking for someone to look after your dog'\n→ 設問: 'To request her service to care for his dog.'",
            "ja": "「犬の世話をしてくれる人を探している」→「犬の世話を依頼する」",
            "note": "look after ～ ⇔ care for ～。someone to look after ⇔ request her service。Q24のパラフレーズ。",
        },
        {
            "en": "本文: 'I cannot prepare dog food, so I ask dog owners to bring their food'\n→ 選択肢: 'she cannot provide food for his dog on her own.'",
            "ja": "「フードを調理できないので持参を依頼」→「自分ではフードを提供できない」",
            "note": "cannot prepare ⇔ cannot provide ... on her own。bring their food が provide の否定の裏付け。Q25。",
        },
        {
            "en": "本文: 'there is still room for the avocado market to grow in Italy and Eastern European countries'\n→ 選択肢: 'Italy and Eastern European countries will be key to expanding the avocado market in Europe.'",
            "ja": "「イタリア・東欧に成長の余地がある」→「イタリア・東欧が市場拡大の鍵になる」",
            "note": "room to grow ⇔ key to expanding。still room（まだ余地）⇔ will be key（鍵となる）。Q28。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Avocado Production / Dog Sitting Email]\n"
            "To help solve these problems, consumers can choose to buy avocados with the FAIRTRADE Mark. The mark means the avocados are produced in an eco-friendly way and that the farmers receive a fair amount of money. Also, these farmers receive extra money that can be used for their businesses or community projects to protect the environment.\n"
            "I understand you are looking for someone to look after your dog while on a family trip during the school holidays. However, I cannot prepare dog food, so I ask dog owners to bring their food. Since you are under eighteen, please speak with your parents about my services, including the fee."
        ),
        "ja": (
            "これらの問題を解決するために、消費者はFAIRTRADEマークの付いたアボカドを選ぶことができます。このマークは、アボカドが環境に配慮した方法で生産され、農家が公正な金額を受け取ることを意味します。また、これらの農家は、事業や環境保護のための地域プロジェクトに使える追加の資金を受け取ります。\n"
            "学校の休み中の家族旅行の間、犬の世話をしてくれる人を探しているとのこと、承知しました。ただし、私は犬用のフードを調理できないため、飼い主の方にフードを持参していただいています。18歳未満の方ですので、料金を含めた私のサービスについて保護者の方と話し合ってください。"
        ),
        "audioFile": "audio/practice_pp5.mp3",
    },
    "practiceQuestions": [
        {
            "q": "Q30で receive a fair amount of money が earn fair pay にどう言い換えられていますか？",
            "a": "receive（受け取る）⇔ earn（得る）。a fair amount of money ⇔ fair pay。どちらも農家への公正な報酬を表す。extra money ... to protect the environment ⇔ spend it on environmental protection。",
        },
        {
            "q": "本文に health problems という語があるのに Q25 の選択肢4が誤答になるのはなぜですか？",
            "a": "本文は Please let me know ... health problems（知らせてほしい＝情報収集）。選択肢4は cannot welcome if it has health problems（受け入れない＝拒否）。同じ語でも動詞・文脈が異なれば意味は正反対になりうる。",
        },
        {
            "q": "Q29で supply を limit する（供給を制限）が誤答になる理由を、本文の too much supply と照合して説明してください。",
            "a": "本文は too much supply（供給過多）が問題。limit supply to maintain a high price（高値維持のため供給制限）は正反対の状況。パラフレーズではなく意味の矛盾で排除できる。",
        },
        {
            "q": "パラフレーズ問題で誤答を見抜く3つのチェックポイントを、この試験の例を挙げて説明してください。",
            "a": "①同じ語でも動詞が違う（let me know vs cannot welcome）。②同じ数字でも用途が違う（$50/日 vs 合計$150、June 22＝返信 vs 支払い）。③同じ国名でも時制が違う（France already vs spread to France in the future）。",
        },
    ],
    "highlightPatterns": [
        "looking for someone to look after your dog",
        "cannot prepare dog food",
        "receive a fair amount of money",
        "community projects to protect the environment",
        "there is still room for the avocado market to grow",
        "which can lead to reduced prices for avocados",
        "responsible for a large part of the global avocado market",
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
for fp in data["lessonPlan"]["focusPoints"]:
    print(f"  {fp['id']}: {fp['title']} | patterns: {len(fp['highlightPatterns'])} | pq: {len(fp['practiceQuestions'])}")
