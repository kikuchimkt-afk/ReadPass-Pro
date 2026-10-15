"""Vocabulary and lesson plan of EIKEN Grade Pre-2 2024-3 Saturday sub-venue.

Loaded by gen_pre2_2024-3-sat.py, which passes its helper functions as ``h``.
Vocabulary examples are original sentences (not copied from the exam); lesson
examples, source quotes and practice passages quote the exam with the official
answers filled in.
"""

from __future__ import annotations


VOCABULARY = [
    # Part 1 answers
    ("bake", "焼く", "動詞", "We baked a cake for Dad's birthday.", ["燃やす", "曲げる", "破裂する"]),
    ("correct", "正しい", "形容詞", "Please check that all your answers are correct.", ["ひどい", "優しい", "きつい"]),
    ("easily", "簡単に・楽に", "副詞", "I could easily read the large letters on the sign.", ["急速に", "神経質に", "落ち着いて"]),
    ("deny", "否定する", "動詞", "The boy denied breaking the window.", ["尊敬する", "比較する", "励ます"]),
    ("freeze", "凍る", "動詞", "Water freezes at zero degrees Celsius.", ["沈む", "ほめる", "治す"]),
    ("beat", "打ち負かす", "動詞", "Our team beat the champions 3 to 1.", ["航海する", "切る", "測る"]),
    ("railroad", "鉄道", "名詞", "The railroad connects the two towns.", ["空港", "重さ", "給料"]),
    ("comfort", "慰める", "動詞", "Lisa comforted her little brother when he started crying.", ["発表する", "開発する", "探検する"]),
    ("complicate", "複雑にする", "動詞", "Too many rules can complicate a simple game.", ["修理する", "想像する", "刺激を与える"]),
    ("government", "政府", "名詞", "The government plans to build more schools.", ["科学技術", "健康", "職業"]),
    ("in the long run", "長い目で見れば", "句", "Studying a little every day will help you in the long run.", ["偏見を持たずに", "土壇場で", "大笑いするために"]),
    ("get rid of", "～を処分する・取り除く", "句動詞", "I got rid of some old toys that I no longer used.", ["～を使い果たす", "～にいたずらをする", "～を減らす"]),
    ("do the laundry", "洗濯をする", "句", "I usually do the laundry on Sunday mornings.", ["席に着く", "息を止める", "バランスを崩す"]),
    ("clear up", "（天気が）晴れる", "句動詞", "The sky cleared up after the storm.", ["あきらめる", "いっぱいになる", "現れる"]),
    ("day by day", "日ごとに", "句", "My English is getting better day by day.", ["共通して", "ひそかに", "せいぜい"]),
    # Part 2
    ("perform", "演じる・発表する", "動詞", "The band will perform at the town festival.", ["見学する", "片付ける", "予約する"]),
    ("extra", "追加の・余分の", "形容詞", "Bring an extra pencil to the test.", ["濡れた", "古い", "壊れた"]),
    ("fridge", "冷蔵庫", "名詞", "Put the milk back in the fridge.", ["車庫", "食器棚", "電子レンジ"]),
    ("shrine", "神社", "名詞", "We visited a shrine in Kyoto on New Year's Day.", ["寺", "城", "博物館"]),
    ("reservation", "予約", "名詞", "I made a reservation at the restaurant for six o'clock.", ["注文", "料金", "案内"]),
    # Part 3
    ("shy", "恥ずかしがりの", "形容詞", "My little sister is shy with new people.", ["勇敢な", "退屈な", "正直な"]),
    ("regret", "後悔する", "動詞", "I regret not studying harder for the test.", ["期待する", "報告する", "許す"]),
    ("take action", "行動を起こす", "句", "We need to take action to keep the beach clean.", ["休憩する", "決心を変える", "結果を待つ"]),
    ("successful", "成功した・うまくいった", "形容詞", "The school festival was very successful.", ["恥ずかしい", "危険な", "不完全な"]),
    # Part 4A
    ("photography", "写真撮影", "名詞", "My uncle's hobby is photography.", ["絵画", "料理", "陶芸"]),
    ("discount", "割引", "名詞", "Students can get a discount at this museum.", ["追加料金", "払い戻し", "税金"]),
    ("fee", "料金", "名詞", "The entrance fee for the zoo is 500 yen.", ["給料", "日程", "割引券"]),
    ("rent", "（お金を払って）借りる", "動詞", "We rented bikes and rode around the lake.", ["修理する", "返品する", "注文する"]),
    ("additional", "追加の", "形容詞", "The hotel charges an additional fee for breakfast.", ["基本の", "無料の", "前回の"]),
    ("apply", "申し込む", "動詞", "She applied for a summer job at the library.", ["引退する", "延期する", "返信する"]),
    ("regarding", "～に関して", "前置詞", "I have a question regarding the homework.", ["～の代わりに", "～にもかかわらず", "～の前に"]),
    ("feel free to", "遠慮なく～する", "句", "Feel free to call me if you need help.", ["～するのをためらう", "～する義務がある", "～するのに慣れている"]),
    # Part 4B
    ("impact", "影響", "名詞", "Smartphones have a big impact on our lives.", ["利益", "釣り合い", "世紀"]),
    ("attractive", "魅力的な", "形容詞", "The low price made the plan attractive to many families.", ["否定的な", "伝統的な", "疲れた"]),
    ("physical", "身体の", "形容詞", "Swimming is a good form of physical exercise.", ["精神の", "経済的な", "社会の"]),
    ("balance", "バランス・釣り合い", "名詞", "It is important to keep a good balance between study and rest.", ["予定", "影響", "利益"]),
    ("satisfied", "満足した", "形容詞", "The customers were satisfied with the service.", ["失望した", "退屈した", "混乱した"]),
    ("profit", "利益", "名詞", "The shop made a large profit last year.", ["損失", "給料", "料金"]),
    ("schedule", "予定・スケジュール", "名詞", "My schedule is full this week.", ["割引", "環境", "技術"]),
    ("approach", "取り組み方・方法", "名詞", "Our teacher has a new approach to teaching English.", ["到着", "要求", "結果"]),
]


def build_vocabulary(h) -> list[dict]:
    return [h.vocab(index, *entry) for index, entry in enumerate(VOCABULARY, start=1)]


def build_lesson_plan(h) -> dict:
    fp = h.focus_point
    points = [
        fp(
            "fp1",
            "so ～ that構文・形式主語のit・部分否定",
            "so ... that, Formal Subject it & Partial Negation",
            "so＋形容詞＋that ...は『とても～なので…』と、原因と結果を一つの文で表します。It is＋形容詞＋for 人＋to do ...のitは形式主語で、本当の主語は後ろのto不定詞です。not alwaysは『いつも～とは限らない』という部分否定で、『まったく～ない』という意味ではありません。",
            "so shy that it was hard for her to do what she wanted / does not always / It is important for her to try it",
            "大問3「Taking Action」第1・2段落",
            [
                {"en": "When she was little, she was so shy that it was hard for her to do what she wanted.", "ja": "小さいころ、ゾーイはとても恥ずかしがり屋だったので、やりたいことをするのが難しいときがありました。", "note": "so＋形容詞＋that ...＝とても～なので…。it was hard for her to doのitは形式主語で、to do what she wantedを指す。"},
                {"en": "This does not always bring her successful results.", "ja": "それがいつもよい結果をもたらすとは限りません。", "note": "not always＝いつも～とは限らない（部分否定）。よい結果になることもある、という含みがある。"},
                {"en": "It is important for her to try it if she is interested in it.", "ja": "興味があるなら、やってみることが彼女にとって大切なのです。", "note": "It is＋形容詞＋for 人＋to do＝人が～することは…だ。for herは不定詞の意味上の主語。"},
            ],
            "[出典: Taking Action 第1・2段落]\nWhen she was little, she was so shy that it was hard for her to do what she wanted. For example, she wanted to learn to dance, but she could not join a dance club because she was afraid to dance in front of the other children. Now, when she finds something that she wants to try, she remembers her father's words and takes action. This does not always bring her successful results. But she feels that is OK. It is important for her to try it if she is interested in it. That way, she will never regret her actions.",
            "小さいころ、ゾーイはとても恥ずかしがり屋だったので、やりたいことをするのが難しいときがありました。たとえば、ダンスを習いたかったのですが、ほかの子どもたちの前で踊るのが怖くて、ダンスクラブに入ることができませんでした。今では、やってみたいことを見つけると、父親の言葉を思い出して行動を起こします。それがいつもよい結果をもたらすとは限りません。でも、ゾーイはそれでよいと思っています。興味があるなら、やってみることが彼女にとって大切なのです。そうすれば、自分の行動を後悔することは決してないでしょう。",
            ["so shy that", "it was hard for her to do what she wanted", "does not always", "It is important for her to try it"],
            "構文・部分否定",
            [
                {"q": "so shy that ...の文で、原因と結果はそれぞれ何ですか？", "a": "原因はゾーイがとても恥ずかしがり屋だったこと、結果はやりたいことをするのが難しかったことです。"},
                {"q": "it was hard for her to do what she wantedのitは何を指しますか？", "a": "後ろのto do what she wanted（やりたいことをすること）を指す形式主語です。"},
                {"q": "This does not always bring her successful results.を『いつもよい結果をもたらさない』と訳してよいですか？", "a": "いいえ。not alwaysは部分否定なので、『いつもよい結果をもたらすとは限らない』と訳します。"},
                {"q": "It is important for her to try itで、『やってみる』のは誰ですか？", "a": "for herのher、つまりゾーイです。for＋人は不定詞の意味上の主語を表します。"},
            ],
        ),
        fp(
            "fp2",
            "目的を表す不定詞・ask if・関係代名詞that",
            "Infinitives of Purpose, ask if & Relative Clauses",
            "このメールでは、I am writing you to ～（～するためにメールを書いています）のto不定詞が、メールを書いた目的を示しています。ask if ...のifは『～かどうか』という意味で、askの目的語になる名詞節を作ります。that you may find helpfulは、直前のsome basic information about the workshopを説明する関係代名詞節です。",
            "you asked if there was a discount for a large group / I am writing you to answer your question / that you may find helpful / To apply, please contact me",
            "大問4A メール第1・2段落",
            [
                {"en": "In your e-mail, you asked if there was a discount for a large group.", "ja": "メールでは、大人数のグループ向けの割引があるかどうかをお尋ねでした。", "note": "ask if ...＝～かどうか尋ねる。askedに合わせてwasと過去形になっている（時制の一致）。"},
                {"en": "So, I am writing you to answer your question and also to provide some basic information about the workshop, such as fees and dates, that you may find helpful.", "ja": "そこで、ご質問にお答えするとともに、料金や日程など、お役に立ちそうなワークショップの基本的な情報をお伝えするためにメールを書いています。", "note": "to answer／to provideは『～するために』（目的）。that you may find helpfulはinformationを説明する関係代名詞節（find O C＝OがCだと思う）。"},
                {"en": "To apply, please contact me at least two days before the workshop.", "ja": "お申し込みの際は、ワークショップの少なくとも2日前までにご連絡ください。", "note": "文頭のTo apply＝申し込むためには（目的）。at least＝少なくとも。"},
            ],
            "[出典: Photography workshop 第1段落]\nThis is Sarah from SJ Studio. Thank you for your e-mail. I am glad to know that you are interested in my two-hour photography workshop. In your e-mail, you asked if there was a discount for a large group. So, I am writing you to answer your question and also to provide some basic information about the workshop, such as fees and dates, that you may find helpful.",
            "SJスタジオのサラです。メールをありがとうございます。私の2時間の写真ワークショップに興味を持っていただけたとのこと、うれしく思います。メールでは、大人数のグループ向けの割引があるかどうかをお尋ねでした。そこで、ご質問にお答えするとともに、料金や日程など、お役に立ちそうなワークショップの基本的な情報をお伝えするためにメールを書いています。",
            ["you asked if there was a discount for a large group", "I am writing you to answer your question", "that you may find helpful", "To apply, please contact me"],
            "目的・if節",
            [
                {"q": "you asked if there was a discountのifはどんな意味ですか？", "a": "『～かどうか』です。条件の『もし～なら』ではなく、askedの目的語になる名詞節を作っています。"},
                {"q": "askedの後でisではなくwasが使われているのはなぜですか？", "a": "主節の動詞askedが過去形なので、時制の一致でwasになっています。日本語では『割引があるかどうか』と訳せます。"},
                {"q": "to answer your questionとto provide ...は何を表していますか？", "a": "サラがこのメールを書いている目的（～するために）を表しています。"},
                {"q": "that you may find helpfulは何を説明していますか？", "a": "some basic information about the workshopを説明する関係代名詞節です。such as fees and datesは、その情報の具体例です。"},
            ],
        ),
        fp(
            "fp3",
            "断りと代案を伝える表現",
            "Declining Politely & Offering an Alternative",
            "Regarding ～（～については）で話題を示し、I am not able to ～で相手の希望に応えられないことを先に伝えています。そのあと、However, if ...で条件付きの代案を示し、I will be happy to ～（喜んで～します）で申し出ています。provide 人 with 物は『人に物を提供する』という意味で、代案のよさを説明しています。",
            "I am not able to offer discounts or coupons / However, if you are a group of five or more people / I will be happy to / This will provide you with a great environment",
            "大問4A メール第3段落",
            [
                {"en": "Regarding group discounts, I am not able to offer discounts or coupons for large groups.", "ja": "団体割引については、大人数のグループに割引やクーポンを提供することはできません。", "note": "Regarding ～＝～については。be not able to do＝～できない。相手の質問への答え（断り）を先に伝えている。"},
                {"en": "However, if you are a group of five or more people, I will be happy to organize a private workshop.", "ja": "しかし、5人以上のグループでしたら、喜んで貸し切りのワークショップを企画します。", "note": "Howeverで断りから代案へ転じる。if＋条件, I will ～＝もし～なら…します（条件付きの申し出）。be happy to do＝喜んで～する。"},
                {"en": "This will provide you with a great environment to practice and improve your photography skills just with your friends.", "ja": "お友達だけで写真の技術を練習し、上達させるのにとてもよい環境になるでしょう。", "note": "provide 人 with 物＝人に物を提供する。to practice and improveはenvironmentを説明する不定詞（～するための環境）。"},
            ],
            "[出典: Photography workshop 第3段落]\nRegarding group discounts, I am not able to offer discounts or coupons for large groups. However, if you are a group of five or more people, I will be happy to organize a private workshop. This will provide you with a great environment to practice and improve your photography skills just with your friends. Please feel free to ask if you have any questions!",
            "団体割引については、大人数のグループに割引やクーポンを提供することはできません。しかし、5人以上のグループでしたら、喜んで貸し切りのワークショップを企画します。お友達だけで写真の技術を練習し、上達させるのにとてもよい環境になるでしょう。ご質問があれば、遠慮なくお尋ねください。",
            ["I am not able to offer discounts or coupons", "However, if you are a group of five or more people", "I will be happy to", "This will provide you with a great environment"],
            "断り・代案",
            [
                {"q": "サラはジョージの質問（団体割引）にどう答えていますか？", "a": "I am not able to offer discounts or coupons for large groupsと、大人数のグループに割引やクーポンは提供できないと答えています。"},
                {"q": "However, if ...の文は、どのような代案を示していますか？", "a": "5人以上のグループなら、貸し切りのワークショップを企画するという代案です。"},
                {"q": "This will provide you with a great environmentのThisは何を指しますか？", "a": "前の文の、5人以上のグループのために貸し切りのワークショップを開くことを指します。"},
                {"q": "Please feel free to ask if you have any questions!のifは『～かどうか』の意味ですか？", "a": "いいえ。ここでは『もし～なら』という条件の意味です。第1段落のyou asked if ...（～かどうか尋ねた）と区別しましょう。"},
            ],
        ),
        fp(
            "fp4",
            "原因と結果をつなぐ表現",
            "Cause & Effect Expressions",
            "説明文では、原因と結果の関係をつかむことが大切です。A lead to Bは『AがBにつながる』、thanks to ～は『～のおかげで』、allow 人 to doは『人が～することを可能にする・認める』、That is why ～は『そういうわけで～』という意味です。Thisやthis changeが前の文のどの内容を指しているかも確かめましょう。",
            "This led to the forty-hour workweek / Thanks to this change / allowed workers at that time to have a better balance / That is why companies allow workers",
            "大問4B「Working Styles」第1・2・4段落",
            [
                {"en": "This led to the forty-hour workweek in the country, and it spread to other countries.", "ja": "このことがアメリカでの週40時間労働制につながり、それはほかの国々にも広がりました。", "note": "A lead to B＝AがBにつながる。Thisは前の文の、長時間労働が悪い影響を与えたことを指す。"},
                {"en": "Thanks to this change, people were able to improve their physical and mental health.", "ja": "この変化のおかげで、人々は心と体の健康を改善することができました。", "note": "thanks to ～＝～のおかげで。this changeは週40時間労働制への変化を指す。"},
                {"en": "That is why companies allow workers to work different schedules to fit their personal lives.", "ja": "そのため、会社は労働者が個人の生活に合わせて、さまざまな勤務スケジュールで働くことを認めています。", "note": "That is why ～＝そういうわけで～。前の文（週4日勤務はすべての人に完璧ではない）が理由、why以下が結果。allow 人 to do＝人が～することを認める。"},
            ],
            "[出典: Working Styles 第1・2段落]\nMany people around the world follow a working style based on forty hours a week. It was born in the United States about a century ago. In the early twentieth century, many people used to work ten to twelve hours a day. However, the long hours of work had a negative impact on both workers and how much work they could do. This led to the forty-hour workweek in the country, and it spread to other countries. When it started, it seemed attractive to many workers. Thanks to this change, people were able to improve their physical and mental health. In addition, it gave them more time to spend with their families. They could also use their private time to improve other skills. For these reasons, the new working style allowed workers at that time to have a better balance between work and personal life.",
            "世界中の多くの人が、週40時間を基本とする働き方をしています。この働き方は、約100年前にアメリカで生まれました。20世紀の初めには、多くの人が1日に10時間から12時間働いていました。しかし、長時間の労働は、労働者自身と、彼らがこなせる仕事の量の両方に悪い影響を与えました。このことがアメリカでの週40時間労働制につながり、それはほかの国々にも広がりました。この働き方が始まったとき、多くの労働者にとって魅力的に思えました。この変化のおかげで、人々は心と体の健康を改善することができました。さらに、家族と過ごす時間も増えました。自分の自由な時間を使って、ほかの技能を高めることもできました。こうした理由から、新しい働き方によって、当時の労働者は仕事と私生活のバランスをよりよく取れるようになりました。",
            ["This led to the forty-hour workweek", "Thanks to this change", "allowed workers at that time to have a better balance", "That is why companies allow workers"],
            "因果関係",
            [
                {"q": "This led to the forty-hour workweekのThisは何を指しますか？", "a": "前の文の、長時間の労働が労働者と仕事の量の両方に悪い影響を与えたことを指します。"},
                {"q": "led toの前と後では、どちらが原因ですか？", "a": "前（長時間労働の悪い影響）が原因で、後ろ（週40時間労働制）が結果です。"},
                {"q": "Thanks to this changeのthis changeは何を指しますか？", "a": "1日に10～12時間働く働き方から、週40時間労働制に変わったことを指します。"},
                {"q": "the new working style allowed workers at that time to have a better balance ...はどのような意味ですか？", "a": "『新しい働き方によって、当時の労働者は仕事と私生活のバランスをよりよく取れるようになった』という意味です。allow 人 to doは『人が～することを可能にする』です。"},
            ],
        ),
        fp(
            "fp5",
            "今回の重要なパラフレーズ",
            "Key Paraphrases in This Exam",
            "大問4の正解の選択肢は、本文と同じ内容を別の語句で言い換えていることがよくあります。たとえばQ24のThe workshop is organized every month.は、I hold the workshop once a monthの言い換えで、once a monthがevery monthに、hold（開く）がbe organized（開催される）に変わっています。反対に、本文の語句を使っていても、料金・日数・時間などの条件が本文と違う選択肢は不正解です。根拠の文と意味が同じかどうかを確かめて選びましょう。",
            "①you asked if there was a discount for a large group → Information about a group discount.（大人数の割引があるか尋ねた→団体割引についての情報）\n②I hold the workshop once a month → The workshop is organized every month.（月に1回開いている→毎月開かれる）\n③I will be happy to organize a private workshop → a private lesson.（貸し切りのワークショップを企画する→貸し切りのレッスン）\n④people were able to improve their physical and mental health → became mentally and physically healthier.（心と体の健康を改善できた→心身ともにより健康になった）\n⑤some companies using this style have reported positive results or even increased profits → Some companies have made more profits.（利益が増えたと報告した→より多くの利益を上げた）\n⑥a lot of companies will have their own approaches to meeting the needs of workers → have their own working styles based on workers' needs.（労働者のニーズに応える独自の方法→労働者のニーズに基づいた独自の働き方）",
            "大問4A・4B（Q23〜Q25・Q27〜Q29）",
            [
                {"en": "Thanks to this change, people were able to improve their physical and mental health.", "ja": "この変化のおかげで、人々は心と体の健康を改善することができました。", "note": "Q27：improve their physical and mental health → became mentally and physically healthier。名詞health → 形容詞の比較級healthier、physical and mental → mentally and physically。"},
                {"en": "In fact, some companies using this style have reported positive results or even increased profits.", "ja": "実際、この働き方を取り入れた会社の中には、よい結果が出た、あるいは利益が増えたと報告しているところもあります。", "note": "Q28：increased profits → have made more profits。increase（増やす）→ make more（より多く生み出す）。"},
                {"en": "So, we may see that a lot of companies will have their own approaches to meeting the needs of workers in the future.", "ja": "ですから将来は、多くの会社が、労働者のニーズに応えるための独自の方法を持つようになるかもしれません。", "note": "Q29：their own approaches to meeting the needs of workers → their own working styles based on workers' needs。approaches → working styles、meeting the needs of workers → based on workers' needs。"},
            ],
            "[出典: Working Styles 第3・4段落]\nIn modern times, however, some people want even more personal time. This is how another working style, the four-day workweek, was born recently. In this working style, people focus on increasing how much they can do in short working hours while working four days a week. These workers believe that they can be more satisfied with their companies. In fact, some companies using this style have reported positive results or even increased profits. However, the four-day workweek is not perfect for all workers. That is why companies allow workers to work different schedules to fit their personal lives. For example, some people work half days twice a week, while others work shorter hours five days a week. So, we may see that a lot of companies will have their own approaches to meeting the needs of workers in the future.",
            "しかし現代では、さらに多くの個人の時間を求める人もいます。こうして最近、週4日勤務というもう一つの働き方が生まれました。この働き方では、週に4日働きながら、短い労働時間でこなせる仕事の量を増やすことに力を注ぎます。こうした働き方をする人たちは、自分の会社にもっと満足できると考えています。実際、この働き方を取り入れた会社の中には、よい結果が出た、あるいは利益が増えたと報告しているところもあります。しかし、週4日勤務がすべての労働者にとって完璧なわけではありません。そのため、会社は労働者が個人の生活に合わせて、さまざまな勤務スケジュールで働くことを認めています。たとえば、週に2日半日だけ働く人もいれば、週に5日、短い時間働く人もいます。ですから将来は、多くの会社が、労働者のニーズに応えるための独自の方法を持つようになるかもしれません。",
            ["I hold the workshop once a month", "organize a private workshop", "improve their physical and mental health", "reported positive results or even increased profits", "their own approaches to meeting the needs of workers"],
            "パラフレーズ",
            [
                {"q": "Q28の正解Some companies have made more profits.は、第3段落のどの表現の言い換えですか？", "a": "some companies using this style have reported positive results or even increased profitsです。increased profits（増えた利益）がhave made more profits（より多くの利益を上げた）に言い換えられています。"},
                {"q": "Q28の『More workers started working longer hours each day.』は正しいですか？", "a": "誤りです。週4日勤務では短い労働時間でこなせる仕事の量を増やすことに力を注ぐとあり、毎日長く働くようになったとは書かれていません。"},
                {"q": "Q29の正解have their own working styles based on workers' needs.は、第4段落のどの表現の言い換えですか？", "a": "will have their own approaches to meeting the needs of workersです。approaches（方法）がworking styles（働き方）に、meeting the needs of workersがbased on workers' needsに言い換えられています。"},
                {"q": "Q29の『decided to go back to the traditional forty-hour workweek.』は正しいですか？", "a": "誤りです。本文は、会社が個人の生活に合わせたさまざまな勤務スケジュールを認めていると述べており、従来の週40時間制に戻したとは書かれていません。"},
            ],
        ),
    ]
    return {"focusPoints": points}
