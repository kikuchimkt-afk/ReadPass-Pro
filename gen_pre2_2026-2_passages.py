# -*- coding: utf-8 -*-
"""Image-verified original passages; complete bilingual reading units.

Each row: natural translation, main finite verb, English|Japanese chunks.
The rows generate paragraphs, translations and four-field sentencePairs.
"""


def passage(label, title, blocks, **extra):
    paragraphs, translations, pairs = [], [], []
    for block in blocks:
        english, japanese = [], []
        for ja, verb, slash in block:
            en = " ".join(unit.split("|",1)[0] for unit in slash.split("||"))
            pairs.append([en, ja, slash, verb])
            english.append(en)
            japanese.append(ja)
        paragraphs.append(" ".join(english))
        translations.append("".join(japanese))
    return dict(label=label, title=title, paragraphs=paragraphs,
                translations=translations, sentencePairs=pairs, questions=[], **extra)


DREAM = passage("", "A Dream", [
    [
        ("ジョイスは、踊ることが大好きな20代の若い女性だった。", "was", "Joyce was a young woman|ジョイスは若い女性だった||in her twenties|20代の||who loved to dance.|踊ることが大好きな"),
        ("彼女はプロのダンサーになるために何年も一生懸命練習を続けてきたが、その夢はまだかなっていなかった。", "had been training", "She had been training hard for years|彼女は何年も一生懸命練習を続けてきた||to become a professional dancer,|プロのダンサーになるために||but her dream had not come true yet.|しかし、彼女の夢はまだかなっていなかった"),
        ("ある日、彼女はダンスを通じて知り合った友人からメッセージを受け取った。", "received", "One day, she received a message|ある日、彼女はメッセージを受け取った||from a friend|友人から||she had met through dancing.|ダンスを通じて知り合った"),
        ("彼がダンサーとしての仕事を得たと知ったとき、彼女は最初はうれしく思った。", "felt", "When she learned|彼女が知ったとき||that he had gotten a job as a dancer,|彼がダンサーとしての仕事を得たと||she felt happy at first.|彼女は最初はうれしく思った"),
        ("その後すぐに、( 21 )。", "", "Soon after,|その後すぐに||( 21 ).|（21）"),
        ("彼女は以前ほど自信が持てなくなり、自分には彼のような十分な才能がないと思った。", "became", "She became less confident|彼女は以前ほど自信が持てなくなった||and thought|そして思った||she did not have enough talent|自分には十分な才能がないと||like him.|彼のような"),
    ], [
        ("父親は、ジョイスが自分の状況をうれしく思えずにいることに気づいたので、彼女と話をすることにした。", "noticed", "Her father noticed|彼女の父親は気づいた||that Joyce was not feeling happy|ジョイスがうれしく思えずにいることに||about her situation,|自分の状況について||so he decided to talk with her.|それで彼は彼女と話をすることにした"),
        ("彼は、たとえ物事が望んだとおりにならなかったとしても、彼女の努力は決して無駄ではないと伝えた。", "told", "He told her|彼は彼女に伝えた||that her efforts were never wasted,|彼女の努力は決して無駄ではないと||even if things didn't turn out|たとえ物事がそうならなかったとしても||as she hoped.|彼女が望んだとおりに"),
        ("その瞬間、彼女は、ダンスに注いできた時間と努力のすべてを後悔する必要はないのだと気づいた。", "realized", "At that moment, she realized|その瞬間、彼女は気づいた||she did not have to regret|後悔する必要はないと||all the time and effort|すべての時間と努力を||she had put into dancing.|ダンスに注いできた"),
        ("ジョイスは ( 22 )。", "", "Joyce|ジョイスは||( 22 ).|（22）"),
        ("彼女は、自分がどれほど踊ることが好きだったかを思い出した。", "remembered", "She remembered|彼女は思い出した||how much she loved dancing.|自分がどれほど踊ることが好きだったかを"),
        ("父親のおかげで、彼女はもう一度挑戦する気持ちになれた。", "was", "Thanks to him,|彼（父親）のおかげで||she was ready to try again.|彼女はもう一度挑戦する準備ができていた"),
    ],
])

EMAIL = passage("A", "A film event", [
    [
        ("こんにちは、アラン。", "", "Hi Alan,|こんにちは、アラン"),
        ("ミーガン・ホワイトです。", "is", "This is Megan White.|ミーガン・ホワイトです"),
        ("先月お話しした映画イベントについて、改めてお知らせするためにこのメールを書いています。", "am writing", "I am writing to remind you|あなたに改めてお知らせするために書いています||about the film event|映画イベントについて||I told you about last month.|先月あなたに話した"),
        ("この特別なイベントでは、私たちの大学の映画クラブが、各メンバーが今学期に制作した短編映画を上映します。", "will show", "At this special event,|この特別なイベントでは||our college film club will show the short films|私たちの大学の映画クラブが短編映画を上映します||each member has made this semester.|各メンバーが今学期に制作した"),
        ("私の映画がいつ上映されるかはわかりませんが、イベント自体は今週金曜日の午後5時に、シティ・ハウス劇場で始まります。", "am", "I am not sure|私はよくわかりません||when my film will be shown,|私の映画がいつ上映されるか||but the event itself will start|しかし、イベント自体は始まります||at 5 p.m. this Friday|今週金曜日の午後5時に||at City House Theater.|シティ・ハウス劇場で"),
    ], [
        ("私が制作した映画は、短いドキュメンタリーです。", "is", "The film I made|私が制作した映画は||is a short documentary.|短いドキュメンタリーです"),
        ("地域社会の日常生活の美しい場面と、その周りの自然を映しています。", "shows", "It shows the beautiful scenes of daily life|それは日常生活の美しい場面を映しています||in a local community|地域社会での||and the nature around it.|そしてその周りの自然を"),
        ("市場で働いたり、市内の公園で過ごしたりするなど、人々がふだんのことをしている様子を撮影しました。", "filmed", "I filmed people|私は人々を撮影しました||doing everyday things,|ふだんのことをしている||like working at a market|例えば市場で働いたり||or spending time in a city park.|市内の公園で時間を過ごしたりといった"),
        ("田舎の木々や川、野生生物の場面も入れました。", "included", "I also included scenes|私は場面も入れました||of trees, rivers, and wildlife|木々や川、野生生物の||in the countryside.|田舎の"),
        ("映画の中に言葉はありませんでしたが、映像と音を通してメッセージを伝えようとしました。", "were", "There were no words in the film,|映画の中に言葉はありませんでした||but I tried to tell a message|しかし、私はメッセージを伝えようとしました||through the images and sounds.|映像と音を通して"),
    ], [
        ("これは有料のイベントですが、来たいのであれば、あなたに無料のチケットを差し上げることができます。", "is", "This is a paid event,|これは有料のイベントです||but I can give you a free ticket|しかし、私はあなたに無料のチケットを差し上げられます||if you want to come.|もしあなたが来たいなら"),
        ("また、関心のある友人がいれば、さらに2席を無料で確保しておくことができます。", "can save", "Also, if you have friends|また、もしあなたに友人がいれば||who are interested,|関心のある||I can save two more seats for free.|私はさらに2席を無料で確保できます"),
        ("その場合は、水曜日までにその人たちの名前を私に送ってください。", "send", "In that case,|その場合は||please send me their names|私に彼らの名前を送ってください||by Wednesday.|水曜日までに"),
        ("劇場はとても大きいので、予約がなくても参加することはできます。", "is", "The theater is huge,|劇場はとても大きいです||so you can still attend|だから、それでも参加できます||even without a reservation.|予約がなくても"),
        ("ただしその場合は、入口でチケット代を払う必要があります。", "will need", "But in that case,|ただしその場合は||you will need to pay for your ticket|チケット代を払う必要があります||at the door.|入口で"),
    ], [
        ("よろしくお願いします。", "", "Thank you,|よろしくお願いします"),
        ("ミーガン・ホワイト", "", "Megan White|ミーガン・ホワイト"),
    ],
], format="email", meta={"from":"Megan White <megan.white-0211@w.g-college.net>",
                        "to":"Alan Jones <alan.jones-0427@w.g-college.net>",
                        "date":"December 9", "subject":"A film event"})
# Preserve the greeting/signature line breaks, without changing sentence coverage.
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Hi Alan, ", "Hi Alan,\n", 1)
EMAIL["paragraphs"][-1] = "Thank you,\nMegan White"
EMAIL["translations"][0] = EMAIL["translations"][0].replace("こんにちは、アラン。", "こんにちは、アラン。\n", 1)
EMAIL["translations"][-1] = "よろしくお願いします。\nミーガン・ホワイト"

MEAT = passage("B", "Days Without Meat", [
    [
        ("ミートレス・マンデー（肉なしの月曜日）は、週に1日、肉を食べないようにする運動である。", "is", "Meatless Monday is a movement|ミートレス・マンデー（肉なしの月曜日）は運動である||to avoid eating meat|肉を食べないようにする||one day a week.|週に1日"),
        ("それは2000年代初めに最初に提案され、それ以来、その考えは多くの企業や、シェフなどの有名人から支持を得てきた。", "was first proposed", "It was first proposed|それは最初に提案された||in the early 2000s,|2000年代初めに||and since then,|そしてそれ以来||the idea has gained support|その考えは支持を得てきた||from many businesses and famous people,|多くの企業や有名人から||such as chefs.|シェフなどの"),
        ("今日、ミートレス・マンデーは40を超える国々に広がっており、多くの人々の食習慣に影響を与え続けている。", "has spread", "Today, Meatless Monday has spread|今日、ミートレス・マンデーは広がっている||to over forty countries,|40を超える国々に||and it continues to influence|そしてそれは影響を与え続けている||the eating habits of many people.|多くの人々の食習慣に"),
        ("アメリカやイギリスなどの国々の一部の学校は、それを給食の献立に取り入れている。", "have introduced", "Some schools|一部の学校は||in countries like the United States and the United Kingdom|アメリカやイギリスのような国々の||have introduced it|それを取り入れている||into their school lunch menus.|給食の献立に"),
    ], [
        ("この運動が始まったのには、いくつかの理由があった。", "were", "There were several reasons|いくつかの理由があった||why the movement started.|その運動が始まった"),
        ("主な理由の一つは、人々がより健康になるのを助けることだった。", "was", "One of the main reasons|主な理由の一つは||was to help people get healthier.|人々がより健康になるのを助けることだった"),
        ("この考えを思いついたあるアメリカ人は、アメリカの人々が本来とるべき量より約15パーセント多く脂肪をとっており、それが深刻な健康問題につながる可能性があることを知った。", "learned", "An American who came up with the idea|その考えを思いついたあるアメリカ人は||learned|知った||that people in the United States took in about 15 percent more fat|アメリカの人々が約15パーセント多く脂肪をとっていると||than they should,|とるべき量よりも||which could lead to serious health problems.|そしてそれは深刻な健康問題につながる可能性があった"),
        ("彼は、週にたった1日肉を避けるだけで、とりすぎている余分な脂肪を減らせると考えた。", "believed", "He believed|彼は考えた||that avoiding meat just one day a week|週にたった1日肉を避けることが||could reduce the extra fat taken in.|とりすぎた余分な脂肪を減らせると"),
        ("この考えが、ミートレス・マンデーの始まりだった。", "was", "This idea was the beginning|この考えが始まりだった||of Meatless Monday.|ミートレス・マンデーの"),
    ], [
        ("同じ頃、自分たちの食べ物の選び方が環境にどう影響するかについて考え始める人が増えた。", "started", "Around the same time,|同じ頃||more people started to think|より多くの人々が考え始めた||about how their food choices affect the environment.|自分たちの食べ物の選択が環境にどう影響するかについて"),
        ("彼らは、肉製品を作ることで多くの温室効果ガスが生み出されていることを知った。", "learned", "They learned|彼らは知った||that a lot of greenhouse gases were created|多くの温室効果ガスが生み出されていることを||by making meat products.|肉製品を作ることによって"),
        ("また、農場で牛や豚などの動物を育てるには、大量の水が必要だということにも気づいた。", "realized", "They also realized|彼らはまた気づいた||that a large amount of water was necessary|大量の水が必要だということに||for raising animals like cows and pigs|牛や豚のような動物を育てるために||on farms.|農場で"),
        ("しだいに、ますます多くの人々がこれらの問題を理解し、ミートレス・マンデーを環境を助ける簡単な方法と見るようになった。", "understood", "Gradually, more and more people understood these problems|しだいに、ますます多くの人々がこれらの問題を理解した||and started to see Meatless Monday|そしてミートレス・マンデーを見るようになった||as a simple way to help the environment.|環境を助ける簡単な方法として"),
    ], [
        ("しかし、誰もがミートレス・マンデーの考えに賛成しているわけではない。", "agrees", "However, not everyone agrees|しかし、誰もが賛成しているわけではない||with the idea of Meatless Monday.|ミートレス・マンデーの考えに"),
        ("例えば、特定の日に子どもたちが給食で肉を食べることを許されないことに、不満を言う人もいる。", "complain", "For example, some people complain|例えば、不満を言う人もいる||that children are not allowed to eat meat|子どもたちが肉を食べることを許されないと||in their school lunches|給食で||on certain days.|特定の日に"),
        ("そうした人々は、子どもとその親が、何を食べるかを自由に選べるべきだと考えている。", "believe", "They believe|彼らは考えている||children and their parents should be free|子どもとその親は自由であるべきだと||to choose what they eat.|何を食べるかを選ぶことについて"),
        ("また、ある研究は、生徒に肉の選択肢がないときには、より多くの食品廃棄物が出る可能性があることを示した。", "showed", "Also, a study showed|また、ある研究は示した||that more food waste could be produced|より多くの食品廃棄物が出る可能性があることを||when students had no meat choices.|生徒に肉の選択肢がないときに"),
        ("今後、ミートレス・マンデーがより広く受け入れられるようにするために、こうした意見を考慮する必要があるかもしれない。", "may need", "In the future,|今後||these opinions may need to be considered|これらの意見は考慮される必要があるかもしれない||in order to make Meatless Monday|ミートレス・マンデーを～にするために||more widely accepted.|より広く受け入れられるもの"),
    ],
])


def question(n, stem, ja, choices, translations, answer, reasons, grammar, evidence):
    return dict(number=n, question=stem, questionTranslation=ja, choices=choices,
                choiceTranslations=translations, answer=answer,
                choiceAnalysis=[f"{t}→{r}" for t,r in zip(translations,reasons)],
                grammar=grammar, sourceEvidence=evidence)


DREAM["questions"] = [
    question(21, "( 21 )", "空所 ( 21 ) に入る内容を選びなさい。",
             ["she wrote back to praise him", "she stopped making excuses", "her smile disappeared completely", "her dream felt closer than ever"],
             ["彼をほめるために返信した", "言い訳をするのをやめた", "彼女の笑顔がすっかり消えた", "夢がこれまで以上に近く感じられた"], 3,
             ["Soon after の後は気持ちが沈む流れで、彼をほめる返信をしたとは書かれていない。", "言い訳をしていたことは本文になく、直後の自信をなくした流れともつながらない。", "正解。💡at first（最初は）と直後の became less confident が、気持ちの変化を示す。", "直後で自分には才能が足りないと考えており、夢が近づいたという気持ちとは逆。"],
             "💡at first は「最初は」で、その後に気持ちが変わることを予告する表現。Soon after（その後すぐに）に続く空所には、次の文の became less confident（以前ほど自信が持てなくなった）につながる、気持ちが沈んだことを表す内容が入る。",
             [DREAM["sentencePairs"][3][0], DREAM["sentencePairs"][5][0]]),
    question(22, "( 22 )", "空所 ( 22 ) に入る内容を選びなさい。",
             ["felt saved by his words", "got a job as a dancer", "regretted her decision", "thought it was time to quit"],
             ["彼の言葉に救われた気がした", "ダンサーとしての仕事を得た", "自分の決断を後悔した", "やめる時が来たと思った"], 1,
             ["正解。💡父親の言葉で努力を後悔しなくてよいと気づき、Thanks to him（彼のおかげで）と続く。", "ダンサーの仕事を得たのは友人で、ジョイスはこれから再挑戦するところ。", "did not have to regret とあり、後悔しなくてよいと気づいた。", "was ready to try again とあり、やめるのではなく、もう一度挑戦しようとしている。"],
             "💡feel saved by ～ は「～に救われたと感じる」。his words は、父親の「努力は決して無駄ではない」という言葉を指す。did not have to ～ は realized に合わせて過去形になっており、「～する必要はない（と気づいた）」の意味。最後の文の Thanks to him（彼のおかげで）が、父親の言葉で前向きになれたことを裏づける。",
             [DREAM["sentencePairs"][7][0], DREAM["sentencePairs"][8][0], DREAM["sentencePairs"][11][0]]),
]

EMAIL["questions"] = [
    question(23, "Megan White contacts Alan Jones to", "ミーガン・ホワイトがアラン・ジョーンズに連絡しているのは、何のためですか。",
             ["remind him that her film will start at 5 p.m.", "explain to him the club she belongs to.", "share the information about an event.", "tell him how to join her club."],
             ["自分の映画が午後5時に始まることを思い出させるため。", "自分が所属するクラブについて彼に説明するため。", "あるイベントについての情報を伝えるため。", "自分のクラブへの入り方を彼に伝えるため。"], 3,
             ["午後5時に始まるのはイベント全体で、自分の映画の上映時間はわからない。", "映画クラブには触れているが、クラブについて説明することが目的ではない。", "正解。💡remind you about the film event が連絡の目的を示す。", "クラブへの入り方については何も書かれていない。"],
             "💡I am writing to ～ は「～するために書いています」で、メールの目的を示す定番の表現。remind A about B は「AにBについて改めて知らせる」。選択肢1は本文の 5 p.m. を使っているが、その時刻に始まるのは the event itself（イベント自体）であり、her film ではない点に注意する。",
             [EMAIL["sentencePairs"][2][0], EMAIL["sentencePairs"][4][0]]),
    question(24, "What is true about the film that Megan made?", "ミーガンが制作した映画について正しいことは何ですか。",
             ["It expresses the theme without using spoken words.", "It describes the long lives of some local people.", "It shows some wild animals found in the city park.", "It focuses on people working on a documentary film."],
             ["話し言葉を使わずにテーマを表現している。", "地元の何人かの人々の長い人生を描いている。", "市内の公園で見られる野生動物を映している。", "ドキュメンタリー映画の制作に取り組む人々に焦点を当てている。"], 1,
             ["正解。💡no words in the film と、映像と音でメッセージを伝えたことが一致する。", "描いているのは日常生活の場面で、地元の人々の長い人生については書かれていない。", "野生生物は countryside（田舎）の場面で、公園では人々を撮影している。", "撮影したのは市場で働く人などの日常で、映画を作る人々ではない。"],
             "💡without using spoken words は「話し言葉を使わずに」で、本文の There were no words in the film の言い換え。the theme（テーマ）は本文の a message にあたる。選択肢3は本文の wildlife と city park を組み合わせているが、本文では別々の場面なので注意する。",
             [EMAIL["sentencePairs"][9][0]]),
    question(25, "Megan tells Alan that he", "ミーガンはアランに、どのようなことを伝えていますか。",
             ["does not need to pay because it is a free event.", "cannot attend the event without a reservation.", "should inform her if he wants free seats for friends.", "may invite as many friends as possible for free tickets."],
             ["無料のイベントなので、お金を払う必要はない。", "予約がなければイベントに参加できない。", "友人のために無料の席が欲しければ、彼女に知らせるべきだ。", "できるだけ多くの友人を無料のチケットで招待してよい。"], 3,
             ["This is a paid event とあり、イベント自体は有料。", "劇場が大きいので予約がなくても参加でき、その場合は入口でチケット代を払う。", "正解。💡友人の無料席には please send me their names とある。", "無料で確保できるのは two more seats（さらに2席）まで。"],
             "💡In that case（その場合は）は、直前の if 節「関心のある友人がいる場合」を受ける。please send me their names（名前を送ってください）が、選択肢の inform her（彼女に知らせる）に言い換えられている。two more seats は「さらに2席」で、人数に上限があることを示す。",
             [EMAIL["sentencePairs"][11][0], EMAIL["sentencePairs"][12][0]]),
]

MEAT["questions"] = [
    question(26, "What is true about Meatless Monday?", "ミートレス・マンデーについて正しいことは何ですか。",
             ["It helps increase the number of people eating only vegetables.", "It helps change the way people eat in many countries.", "It refers to a holiday to appreciate food in forty countries.", "It refers to meals eaten at American schools every day."],
             ["野菜だけを食べる人の数を増やすのに役立っている。", "多くの国で、人々の食べ方を変えるのに役立っている。", "40か国で食べ物に感謝する祝日のことを指す。", "アメリカの学校で毎日食べられる食事のことを指す。"], 2,
             ["週に1日肉を避ける運動で、野菜だけを食べる人を増やすとは書かれていない。", "正解。💡40を超える国に広がり、influence the eating habits とある。", "祝日ではなく、週に1日肉を食べないようにする運動。", "一部の学校が給食に取り入れているだけで、毎日の食事を指すのではない。"],
             "💡change the way people eat（人々の食べ方を変える）は、本文の influence the eating habits（食習慣に影響を与える）の言い換え。continue to ～ は「～し続ける」。over forty countries は「40を超える国々」で、ちょうど40か国という意味ではない。",
             [MEAT["sentencePairs"][2][0]]),
    question(27, "An American man thought of the idea of Meatless Monday because", "あるアメリカ人男性がミートレス・マンデーの考えを思いついたのは、なぜですか。",
             ["he wanted to prove that avoiding meat would cause health problems.", "he found that 15 percent of Americans did not eat enough vegetables.", "he discovered that people in America had too much fat in their diet.", "he believed people could get enough fat by eating meat once a week."],
             ["肉を避けると健康問題が起きることを証明したかったから。", "アメリカ人の15パーセントが十分な野菜を食べていないとわかったから。", "アメリカの人々の食事に脂肪が多すぎるとわかったから。", "週に1回肉を食べれば十分な脂肪をとれると考えたから。"], 3,
             ["健康問題につながるのは脂肪のとりすぎで、肉を避けることではない。", "15 percent は脂肪のとりすぎの割合で、野菜を食べない人の割合ではない。", "正解。💡15 percent more fat than they should と一致する。", "週に1日肉を避けて、余分な脂肪を減らせると考えた。"],
             "💡more fat than they should は「とるべき量より多くの脂肪」で、should の後に take in が省略されている。took in は「（体に）取り入れた」。選択肢では had too much fat in their diet（食事に脂肪が多すぎた）と言い換えている。コンマの後の which（, which）は直前の内容を受けて「そしてそれは～」と説明を加える。",
             [MEAT["sentencePairs"][6][0], MEAT["sentencePairs"][7][0]]),
    question(28, "Why did more people start supporting Meatless Monday?", "より多くの人々がミートレス・マンデーを支持し始めたのは、なぜですか。",
             ["They thought eating meat could reduce water pollution.", "They learned that meat production created little greenhouse gas.", "They believed it was one of the easiest ways to protect animals.", "They realized it could help solve some environmental problems."],
             ["肉を食べることで水質汚染を減らせると考えたから。", "肉の生産では温室効果ガスがほとんど出ないと知ったから。", "それが動物を守る最も簡単な方法の一つだと考えたから。", "それがいくつかの環境問題の解決に役立ちうると気づいたから。"], 4,
             ["家畜に大量の水が必要とはあるが、水質汚染については書かれていない。", "a lot of greenhouse gases が出るとあり、逆の内容。", "a simple way は環境を助ける方法で、動物を守る方法ではない。", "正解。💡a simple way to help the environment とある。"],
             "💡see A as B は「AをBとみなす」。these problems は、直前の温室効果ガスの発生と大量の水の使用を指す。little は数えられない名詞について「ほとんど～ない」という否定の意味になり、本文の a lot of と反対になる。",
             [MEAT["sentencePairs"][10][0], MEAT["sentencePairs"][11][0], MEAT["sentencePairs"][12][0]]),
    question(29, "Why are some people against Meatless Monday at schools?", "学校でのミートレス・マンデーに反対する人がいるのは、なぜですか。",
             ["They think children need to eat meat every day to grow up healthy.", "They think children should be allowed to decide their own food.", "They think students will end up eating unhealthy food instead.", "They think students may waste more food if meat is the only choice."],
             ["子どもが健康に育つには、毎日肉を食べる必要があると考えているから。", "子どもは自分の食べるものを決めることを認められるべきだと考えているから。", "生徒が代わりに健康に悪い食べ物を食べることになると考えているから。", "肉しか選択肢がないと、生徒がより多くの食べ物を無駄にするかもしれないと考えているから。"], 2,
             ["毎日肉が必要だという意見は書かれていない。", "正解。💡free to choose what they eat とある。", "代わりに健康に悪い食べ物を食べることになるという記述はない。", "no meat choices のときの話で、条件が逆。"],
             "💡be free to ～ は「自由に～できる」で、選択肢の be allowed to decide（決めることを許される）に言い換えられている。what they eat は「彼らが食べるもの」。選択肢4は条件が逆で、本文は had no meat choices（肉の選択肢がない）ときの話である。",
             [MEAT["sentencePairs"][14][0], MEAT["sentencePairs"][15][0]]),
]

PASSAGES = [DREAM, EMAIL, MEAT]
