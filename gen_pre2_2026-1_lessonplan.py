# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json
Step E: lessonPlan（focusPoints × 5）
本文中に実在する構文のみを使用。practicePassage は試験本文の抜粋＋[出典: タイトル]。
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat", "data.json",
)

fp1 = {
    "id": "fp1",
    "title": "物語の時間経過と結末の表現",
    "subtitle": "Time Sequence & Story Conclusion",
    "explanation": "In the end（結局）で物語の結末を示し、A few years later（数年後）で時間の経過を表し、surprised to hear that（～と聞いて驚いた）で感情を述べる物語文パターン。nowhere to be found（どこにも見つからない）で行方不明を表します。",
    "sourceQuote": "In the end, he had to accept that Leo had gone / A few years later / surprised to hear that",
    "sourceLocation": "大問3「A Lost Dog」",
    "examples": [
        {
            "en": "Max looked for him for hours, but the dog was nowhere to be found.",
            "ja": "マックスは何時間も探したが、犬の姿はどこにもなかった。",
            "note": "nowhere to be found＝「どこにも見つからない」。否定＋不定詞の定型。",
        },
        {
            "en": "In the end, he had to accept that Leo had gone.",
            "ja": "結局、彼はレオがいなくなったことを受け入れなければならなかった。",
            "note": "In the end＝「結局」。had to accept＝「受け入れなければならなかった」。",
        },
        {
            "en": "A few years later, Max was in college and living in another city.",
            "ja": "数年後、マックスは大学に通い、別の都市に住んでいた。",
            "note": "A few years later＝時間の経過。物語の場面転換に使われる。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: A Lost Dog]\n"
            "Max was a high school student who had a dog named Leo. One day, while they were taking their usual walk in the mountains, Leo suddenly ran off. Max looked for him for hours, but the dog was nowhere to be found. Max did everything that he could. He made posters, gave them to neighbors, and called dog shelters. Still, Leo was missing. In the end, he had to accept that Leo had gone.\n"
            "A few years later, Max was in college and living in another city. One afternoon, he got a call from his mother. She told him that a dog very similar to Leo had appeared and was sitting in front of their house. Max was surprised to hear that. He hurried back to his home in his hometown."
        ),
        "ja": (
            "マックスはレオという犬を飼っている高校生だった。ある日、山を散歩しているとレオが走り去った。何時間も探したが、犬はどこにも見つからなかった。マックスはできる限りのことをした。ポスターを作り、近所に配り、保護施設に電話した。それでもレオは行方不明だった。結局、レオがいなくなったことを受け入れなければならなかった。\n"
            "数年後、マックスは大学に通い別の都市に住んでいた。ある午後、母親から電話があった。レオに似た犬が家の前に座っていると言われた。マックスは驚いた。故郷の実家に急いで戻った。"
        ),
    },
    "practiceQuestions": [
        {
            "q": "物語の時間的順序を整理してください。",
            "a": "犬が走り去る→何時間も探す→ポスター等の努力→結局あきらめる→数年後→母からの電話→故郷へ急ぐ。",
        },
        {
            "q": "'In the end' はどのような場面で使われていますか？",
            "a": "長い捜索の末、レオを見つけられず「いなくなった」と受け入れる結末の場面。",
        },
        {
            "q": "'nowhere to be found' の意味は？",
            "a": "「どこにも見つからない」。Maxが何時間も探したが犬の姿がなかった状況。",
        },
        {
            "q": "'surprised to hear that' の that は何を指しますか？",
            "a": "母親が言った「レオに似た犬が家の前に座っている」という知らせ。",
        },
    ],
    "highlightPatterns": [
        "nowhere to be found",
        "In the end, he had to accept",
        "A few years later",
        "surprised to hear that",
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "時間・結末",
}

fp2 = {
    "id": "fp2",
    "title": "仕事内容・待遇の説明表現",
    "subtitle": "Job Description & Benefits",
    "explanation": "like ～ing（～のような）で仕事例を示し、is not part of the job（仕事に含まれない）で範囲を限定し、be allowed to（～することが許可されている）で待遇を説明する案内文パターン。受動態 will be done で仕事の実施方法を述べます。",
    "sourceQuote": "like serving customers / is not part of the job / you are allowed to ski or snowboard / even on the days you don't work",
    "sourceLocation": "大問4A メール第2〜3段落",
    "examples": [
        {
            "en": "The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment.",
            "ja": "仕事にはギフトショップでの接客やレンタル依頼への対応など、さまざまな役割が含まれる。",
            "note": "like + ～ing＝「～のような」例示。includes＝「含む」。",
        },
        {
            "en": "Working in the cafeteria or hotel is not part of the job.",
            "ja": "カフェテリアやホテルでの仕事は、この仕事に含まれない。",
            "note": "not part of the job＝「仕事の範囲外」。動名詞主語。",
        },
        {
            "en": "Also, you are allowed to ski or snowboard there for free.",
            "ja": "また、スキーやスノーボードを無料で楽しむことが許可されている。",
            "note": "be allowed to ～＝「～することが許可されている」。for free＝無料で。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: A job at a ski resort]\n"
            "The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment. It also includes clearing snow from the streets. Working in the cafeteria or hotel is not part of the job. You will be working five days a week for about one month. Some work will be done in the evenings instead of during the day.\n"
            "First, three free meals are served every day, even on the days you don't work. Also, you are allowed to ski or snowboard there for free. And you will have a free room just for yourself. However, it is not in the same hotel where the customers stay."
        ),
        "ja": (
            "仕事にはギフトショップでの接客やレンタル器材の依頼対応など、さまざまな役割が含まれる。道路の除雪も含まれる。カフェテリアやホテルでの仕事は含まれない。週5日、約1ヶ月働く。一部の仕事は夕方に行われる。\n"
            "毎日3食無料で、働かない日でも同様。スキーやスノーボードを無料で楽しめる。自分だけの無料の部屋がある。ただし、お客と同じホテルではない。"
        ),
    },
    "practiceQuestions": [
        {
            "q": "この仕事に含まれないものを2つ挙げてください。",
            "a": "カフェテリアでの仕事、ホテルでの仕事（Working in the cafeteria or hotel is not part of the job）。",
        },
        {
            "q": "'even on the days you don't work' は何を意味しますか？",
            "a": "働かない日でも（3食無料が）適用される。休日の待遇。",
        },
        {
            "q": "'Some work will be done in the evenings' の受動態の意味は？",
            "a": "一部の仕事は夕方に行われる。will be done＝未来の受動態。",
        },
        {
            "q": "'However, it is not in the same hotel' の it は何を指しますか？",
            "a": "前文の a free room just for yourself（スタッフ用の無料の部屋）。",
        },
    ],
    "highlightPatterns": [
        "like serving customers",
        "is not part of the job",
        "will be done in the evenings",
        "you are allowed to ski or snowboard",
        "even on the days you don't work",
    ],
    "highlightColor": "#f472b6",
    "highlightLabel": "仕事・待遇",
}

fp3 = {
    "id": "fp3",
    "title": "While節と言い換えの表現",
    "subtitle": "While Contrast & In Other Words",
    "explanation": "While A, others B（Aする人もいれば、Bする人もいる）で対比を示し、One reason for this is that（その理由の一つは～である）で理由を説明し、In other words（つまり）で言い換える論説文パターン。",
    "sourceQuote": "While some of them go to a doctor / One reason for this is that / In other words, they believe",
    "sourceLocation": "大問4B 第1〜2段落",
    "examples": [
        {
            "en": "While some of them go to a doctor for help, others rely on social media and try to improve their mental health with information they find on it.",
            "ja": "医者の助けを求める人もいれば、ソーシャルメディアに頼って情報で精神的健康を改善しようとする人もいる。",
            "note": "While some..., others...＝「～する人もいれば、他の人は…」対比。",
        },
        {
            "en": "One reason for this is that they may be able to find useful information for free.",
            "ja": "その理由の一つは、有用な情報を無料で見つけられる可能性があることだ。",
            "note": "One reason for this is that＝理由の説明。for free＝無料で。",
        },
        {
            "en": "In other words, they believe they can feel connected to others and get support from them on social media.",
            "ja": "つまり、ソーシャルメディアで他者とつながり、支援を得られると信じている。",
            "note": "In other words＝「つまり」前文の言い換え・要約。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Social Media for Mental Health]\n"
            "While some of them go to a doctor for help, others rely on social media and try to improve their mental health with information they find on it. One reason for this is that they may be able to find useful information for free.\n"
            "A study of over 1,000 young people showed their positive experiences on social media. For example, more than half of them said that they could feel safe when they were having a hard time, thanks to social media. Also, many of them said that they felt accepted. In other words, they believe they can feel connected to others and get support from them on social media."
        ),
        "ja": (
            "医者に頼る人もいれば、ソーシャルメディアの情報で精神的健康を改善しようとする人もいる。その理由の一つは、有用な情報を無料で見つけられることだ。\n"
            "1,000人以上の研究がポジティブな経験を示した。半数以上が辛いときに安心感を得られると答え、多くの人が受け入れられたと感じた。つまり、ソーシャルメディアでつながりと支援を得られると信じている。"
        ),
    },
    "practiceQuestions": [
        {
            "q": "'While some..., others...' の対比の内容は？",
            "a": "some＝医者に行く人。others＝ソーシャルメディアに頼る人。",
        },
        {
            "q": "'One reason for this' の this は何を指しますか？",
            "a": "前文の「ソーシャルメディアに頼って精神的健康を改善しようとすること」。",
        },
        {
            "q": "'In other words' の直後は何の言い換えですか？",
            "a": "feel safe / feel accepted の具体的内容を「つながりと支援を得られる」と要約している。",
        },
        {
            "q": "'more than half of them' は設問でどう言い換えられますか？",
            "a": "many young people / helps many young people feel better など、多数を示す表現に対応。",
        },
    ],
    "highlightPatterns": [
        "While some of them go to a doctor",
        "One reason for this is that",
        "more than half of them said",
        "In other words, they believe",
    ],
    "highlightColor": "#34d399",
    "highlightLabel": "対比・言い換え",
}

fp4 = {
    "id": "fp4",
    "title": "専門家の見解と情報の信頼性",
    "subtitle": "Expert Opinion & Information Reliability",
    "explanation": "not necessarily（必ずしも～ではない）で慎重な判断を示し、should not be trusted（信頼すべきではない）で注意を促し、the expert suggests（専門家は示唆する）と should check that（～であることを確認すべき）で対策を述べる論説文パターン。",
    "sourceQuote": "is not necessarily good / should not be trusted / the expert suggests / should check that the information comes from experts",
    "sourceLocation": "大問4B 第3〜4段落",
    "examples": [
        {
            "en": "However, one expert says that trying to solve mental health problems through social media is not necessarily good.",
            "ja": "しかし、ある専門家は、ソーシャルメディアで精神的健康の問題を解決しようとすることは必ずしも良いことではないと言う。",
            "note": "not necessarily＝「必ずしも～ではない」。慎重な否定。",
        },
        {
            "en": "This is because some information should not be trusted or is not professional.",
            "ja": "一部の情報は信頼すべきではない、または専門的ではないからである。",
            "note": "should not be trusted＝「信頼すべきではない」受動態。",
        },
        {
            "en": "they should check that the information comes from experts in the field.",
            "ja": "その情報がその分野の専門家によるものか確認すべきだ。",
            "note": "check that ～＝「～であることを確認する」。experts in the field＝分野の専門家。",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: Social Media for Mental Health]\n"
            "However, one expert says that trying to solve mental health problems through social media is not necessarily good. This is because some information should not be trusted or is not professional. For example, a study was performed to check how much information on social media about a particular mental illness could be trusted. The results showed some of the information was actually wrong. If people use such information to treat their mental illness, it could have a negative impact on them.\n"
            "To avoid these situations, the expert suggests there is something people can do. For example, if people want to use the Internet to get information about mental health, they should check that the information comes from experts in the field. That way, social media can truly help mental health, and people can find help from social media."
        ),
        "ja": (
            "しかし専門家は、ソーシャルメディアで問題を解決しようとすることは必ずしも良くないと言う。情報が信頼できない、または専門的でないからだ。研究の結果、一部の情報は誤りだった。その情報で治療すると悪影響がある。\n"
            "これを避けるため、専門家はできることがあると示唆する。精神的健康の情報を得る際は、分野の専門家によるものか確認すべきだ。そうすればソーシャルメディアは本当に助けになる。"
        ),
    },
    "practiceQuestions": [
        {
            "q": "'not necessarily good' はどのような意味ですか？",
            "a": "「必ずしも良いとは限らない」。断定を避えた専門家の慎重な表現。",
        },
        {
            "q": "誤った情報を使うとどうなりますか？",
            "a": "it could have a negative impact on them（悪影響を及ぼす可能性がある）。",
        },
        {
            "q": "専門家が勧める対策は？",
            "a": "情報が experts in the field（その分野の専門家）によるものか確認すること。",
        },
        {
            "q": "'That way' は何を指しますか？",
            "a": "専門家による情報か確認するという前の行動。その結果としてSNSが助けになる。",
        },
    ],
    "highlightPatterns": [
        "is not necessarily good",
        "should not be trusted",
        "some of the information was actually wrong",
        "the expert suggests",
        "comes from experts in the field",
    ],
    "highlightColor": "#fbbf24",
    "highlightLabel": "専門家・信頼性",
}

fp5 = {
    "id": "fp5",
    "title": "今回の重要なパラフレーズ",
    "subtitle": "Key Paraphrases in This Exam",
    "explanation": "英語資格検定では、本文の表現が設問や選択肢で別の言い方に言い換え（パラフレーズ）されます。",
    "sourceQuote": (
        "①send a message by November 5＝contact the ski resort by November 5（11月5日までに連絡）\n"
        "②handling requests to rent equipment＝helping people who rent items（レンタル対応）\n"
        "③even on the days you don't work＝on any day（いつでも3食無料）\n"
        "④find useful information for free＝free, useful advice（無料で有用な助言）\n"
        "⑤feel safe / feel accepted / feel connected＝feel better during tough times（辛い時期の支え）\n"
        "⑥should not be trusted＝not always good to trust（信頼すべきでない）\n"
        "⑦comes from experts in the field＝use information from experts（専門家の情報を使う）"
    ),
    "sourceLocation": "大問4A, 大問4B",
    "examples": [
        {
            "en": "send a message → contact",
            "ja": "メッセージを送る＝連絡する",
            "note": "Q23のパラフレーズ",
        },
        {
            "en": "handling requests to rent equipment → helping people who rent items",
            "ja": "レンタル依頼への対応＝借りる人の手伝い",
            "note": "Q24のパラフレーズ",
        },
        {
            "en": "should not be trusted → not always good to trust",
            "ja": "信頼すべきでない＝信じるのは必ずしも良くない",
            "note": "Q28のパラフレーズ",
        },
    ],
    "practicePassage": {
        "en": (
            "[出典: A job at a ski resort]\n"
            "You need to send a message to the ski resort by November 5. Then, you will have an online interview on November 10.\n"
            "[出典: Social Media for Mental Health]\n"
            "One reason for this is that they may be able to find useful information for free. However, one expert says that trying to solve mental health problems through social media is not necessarily good. This is because some information should not be trusted or is not professional. For example, if people want to use the Internet to get information about mental health, they should check that the information comes from experts in the field."
        ),
        "ja": (
            "11月5日までにスキーリゾートにメッセージを送る必要がある。その後、11月10日にオンライン面接がある。\n"
            "有用な情報を無料で見つけられることが理由の一つ。しかし専門家は、ソーシャルメディアで解決しようとすることは必ずしも良くないと言う。情報が信頼できないからだ。分野の専門家によるものか確認すべきだ。"
        ),
    },
    "practiceQuestions": [
        {
            "q": "「send a message to the ski resort by November 5」のパラフレーズは？",
            "a": "contact the ski resort by November 5（11月5日までにリゾートに連絡する）。",
        },
        {
            "q": "「find useful information for free」のパラフレーズは？",
            "a": "find free, useful advice to improve their mental health（無料で有用な助言を見つける）。",
        },
        {
            "q": "「should not be trusted」と対応する選択肢の表現は？",
            "a": "It is not always a good idea to trust any information on social media.",
        },
        {
            "q": "「comes from experts in the field」のパラフレーズは？",
            "a": "use information from experts in the field of mental health.",
        },
    ],
    "highlightPatterns": [
        "send a message to the ski resort by November 5",
        "find useful information for free",
        "should not be trusted",
        "comes from experts in the field",
    ],
    "highlightColor": "#f59e0b",
    "highlightLabel": "パラフレーズ",
}

lesson_plan = {
    "focusPoints": [fp1, fp2, fp3, fp4, fp5],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

if len(data.get("sections", [])) < 4:
    raise SystemExit("sections 0-3 not found")

data["lessonPlan"] = lesson_plan

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote lessonPlan ({len(lesson_plan['focusPoints'])} focusPoints) to {DATA_PATH}")
for fp in lesson_plan["focusPoints"]:
    print(f"  {fp['id']}: {fp['title']} ({len(fp['highlightPatterns'])} patterns)")
