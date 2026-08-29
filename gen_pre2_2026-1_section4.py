# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級 data.json
Step D: 大問4（reading-comprehension型）Q23〜29
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1-sat", "data.json",
)

section4 = {
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "instruction": "次の英文Ａ，Ｂの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "A job at a ski resort",
            "format": "email",
            "meta": {
                "from": "Blake Jones <blake.jones.0710@round-message.com>",
                "to": "Jacob Kennedy <j.k.1018@eletter-cloud.com>",
                "date": "October 30",
                "subject": "A job at a ski resort",
            },
            "paragraphs": [
                "Dear Jacob, How are you doing? This winter, I'm going to work a part-time job at a ski resort. I'll stay there while I work as a staff member for a short time. I thought you might be interested in this opportunity. If so, please check the information below. You need to send a message to the ski resort by November 5. Then, you will have an online interview on November 10.",
                "The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment. It also includes clearing snow from the streets. Working in the cafeteria or hotel is not part of the job. You will be working five days a week for about one month. Some work will be done in the evenings instead of during the day. The rest of the week will be spent freely.",
                "I should tell you about what you will receive at the ski resort. First, three free meals are served every day, even on the days you don't work. Also, you are allowed to ski or snowboard there for free. And you will have a free room just for yourself. However, it is not in the same hotel where the customers stay. If you have any questions, you can ask during the interview. Thank you, Blake Jones",
            ],
            "translations": [
                "ジェイコブへ、お元気ですか？この冬、私はスキーリゾートでアルバイトをします。短期間スタッフとして働く間、そこに滞在します。この機会に興味があるかもしれないと思いました。そうなら、下の情報を確認してください。11月5日までにスキーリゾートにメッセージを送る必要があります。その後、11月10日にオンライン面接があります。",
                "仕事にはリゾートでのさまざまな役割が含まれます。ギフトショップでの接客や、器材を借りたいという依頼への対応などです。道路の除雪も含まれます。カフェテリアやホテルでの仕事は含まれません。約1か月、週5日働きます。日中ではなく夕方に行う仕事もあります。週の残りは自由に過ごせます。",
                "スキーリゾートで受けられるものについてもお伝えします。まず、働かない日も含め、毎日3食の無料の食事が出ます。また、そこでスキーやスノーボードを無料で楽しめます。さらに、自分だけの無料の部屋があります。ただし、お客が泊まるホテルと同じホテルではありません。質問があれば面接で尋ねられます。ありがとう、ブレイク・ジョーンズ",
            ],
            "sentencePairs": [
                ["Dear Jacob,", "ジェイコブへ、"],
                ["How are you doing?", "お元気ですか？"],
                ["This winter, I'm going to work a part-time job at a ski resort.", "この冬、私はスキーリゾートでアルバイトをします。"],
                ["I'll stay there while I work as a staff member for a short time.", "短期間スタッフとして働く間、そこに滞在します。"],
                ["I thought you might be interested in this opportunity.", "この機会に興味があるかもしれないと思いました。"],
                ["If so, please check the information below.", "そうなら、下の情報を確認してください。"],
                ["You need to send a message to the ski resort by November 5.", "11月5日までにスキーリゾートにメッセージを送る必要があります。"],
                ["Then, you will have an online interview on November 10.", "その後、11月10日にオンライン面接があります。"],
                ["The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment.", "仕事にはリゾートでのさまざまな役割が含まれます。ギフトショップでの接客や、器材を借りたいという依頼への対応などです。"],
                ["It also includes clearing snow from the streets.", "道路の除雪も含まれます。"],
                ["Working in the cafeteria or hotel is not part of the job.", "カフェテリアやホテルでの仕事は含まれません。"],
                ["You will be working five days a week for about one month.", "約1か月、週5日働きます。"],
                ["Some work will be done in the evenings instead of during the day.", "日中ではなく夕方に行う仕事もあります。"],
                ["The rest of the week will be spent freely.", "週の残りは自由に過ごせます。"],
                ["I should tell you about what you will receive at the ski resort.", "スキーリゾートで受けられるものについてもお伝えします。"],
                ["First, three free meals are served every day, even on the days you don't work.", "まず、働かない日も含め、毎日3食の無料の食事が出ます。"],
                ["Also, you are allowed to ski or snowboard there for free.", "また、そこでスキーやスノーボードを無料で楽しめます。"],
                ["And you will have a free room just for yourself.", "さらに、自分だけの無料の部屋があります。"],
                ["However, it is not in the same hotel where the customers stay.", "ただし、お客が泊まるホテルと同じホテルではありません。"],
                ["If you have any questions, you can ask during the interview.", "質問があれば面接で尋ねられます。"],
                ["Thank you, Blake Jones", "ありがとう、ブレイク・ジョーンズ"],
            ],
            "questions": [
                {
                    "number": 23,
                    "question": "If Jacob Kennedy wants to take the job at the ski resort,",
                    "questionTranslation": "ジェイコブ・ケネディがスキーリゾートの仕事に就きたい場合、",
                    "choices": [
                        "he needs to make a phone call to the ski resort.",
                        "he has to tell Blake Jones by November 10.",
                        "he should contact the ski resort by November 5.",
                        "he must have experience working at a ski resort.",
                    ],
                    "choiceTranslations": [
                        "スキーリゾートに電話する必要がある。",
                        "11月10日までにブレイク・ジョーンズに伝えなければならない。",
                        "11月5日までにスキーリゾートに連絡すべきだ。",
                        "スキーリゾートでの勤務経験がなければならない。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "電話する。本文はsend a messageとしている",
                        "11月10日までにBlakeへ伝える。11月10日は面接日である",
                        "11月5日までにリゾートへ連絡する。send a messageの言い換え→正解。💡",
                        "勤務経験が必要。本文にその条件はない",
                    ],
                    "sourceEvidence": [
                        "You need to send a message to the ski resort by November 5.",
                        "Then, you will have an online interview on November 10.",
                    ],
                    "grammar": "💡 send a message to ～＝～にメッセージを送る。by November 5＝11月5日までに。",
                },
                {
                    "number": 24,
                    "question": "What is true about the job at the ski resort?",
                    "questionTranslation": "スキーリゾートの仕事について正しいのはどれか？",
                    "choices": [
                        "It includes cleaning rooms at the hotel.",
                        "It includes working at night five days a week.",
                        "It includes serving customers in the cafeteria.",
                        "It includes helping people who rent items.",
                    ],
                    "choiceTranslations": [
                        "ホテルの部屋の掃除が含まれる。",
                        "週5日、夜勤が含まれる。",
                        "カフェテリアでの接客が含まれる。",
                        "レンタル品を借りる人の手伝いが含まれる。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "ホテルの部屋を掃除する。hotelの仕事は含まれない",
                        "週5日すべて夜勤。一部がeveningsという記述を広げすぎ",
                        "カフェテリアで接客する。cafeteriaの仕事は含まれない",
                        "レンタルする人を手伝う。handling requests to rent equipmentの言い換え→正解。💡",
                    ],
                    "sourceEvidence": [
                        "The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment.",
                        "Working in the cafeteria or hotel is not part of the job.",
                    ],
                    "grammar": "💡 handle requests to rent equipment＝レンタル依頼に対応する。not part of the job＝仕事に含まれない。",
                },
                {
                    "number": 25,
                    "question": "If Jacob works at the ski resort, he can",
                    "questionTranslation": "ジェイコブがスキーリゾートで働く場合、彼にできることは？",
                    "choices": [
                        "have three meals for free on any day.",
                        "ski there without paying but cannot snowboard.",
                        "sleep in a room shared with his friend.",
                        "stay in the same hotel as the customers.",
                    ],
                    "choiceTranslations": [
                        "どの日でも3食無料で食べられる。",
                        "スキーは無料だがスノーボードはできない。",
                        "友人と相部屋で寝られる。",
                        "お客と同じホテルに泊まれる。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "どの日でも3食無料。働かない日も毎日提供される→正解。💡",
                        "スノーボードは不可。本文ではski or snowboardの両方が無料",
                        "友人と相部屋。just for yourselfと反対",
                        "お客と同じホテル。not in the same hotelと反対",
                    ],
                    "sourceEvidence": [
                        "three free meals are served every day, even on the days you don't work.",
                        "you are allowed to ski or snowboard there for free.",
                    ],
                    "grammar": "💡 be allowed to ～＝～することが許可されている。even on the days you don't work＝働かない日でも。",
                },
            ],
        },
        {
            "label": "B",
            "title": "Social Media for Mental Health",
            "paragraphs": [
                "Today, people often talk about the negative effects of social media. However, social media can positively influence mental health. In fact, it seems to be helpful for many people with mental health problems. While some of them go to a doctor for help, others rely on social media and try to improve their mental health with information they find on it. One reason for this is that they may be able to find useful information for free.",
                "A study of over 1,000 young people showed their positive experiences on social media. During the study, they shared several good things about social media. For example, more than half of them said that they could feel safe when they were having a hard time, thanks to social media. Also, many of them said that they felt accepted. In other words, they believe they can feel connected to others and get support from them on social media.",
                "However, one expert says that trying to solve mental health problems through social media is not necessarily good. This is because some information should not be trusted or is not professional. For example, a study was performed to check how much information on social media about a particular mental illness could be trusted. The results showed some of the information was actually wrong. If people use such information to treat their mental illness, it could have a negative impact on them.",
                "In this way, there are times when social media can work in a negative way. To avoid these situations, the expert suggests there is something people can do. For example, if people want to use the Internet to get information about mental health, they should check that the information comes from experts in the field. That way, social media can truly help mental health, and people can find help from social media.",
            ],
            "translations": [
                "今日、人々はソーシャルメディアの悪影響についてよく話します。しかし、ソーシャルメディアは心の健康に良い影響を与えることもできます。実際、心の健康に問題を抱える多くの人に役立つようです。医者に助けを求める人もいれば、ソーシャルメディアに頼り、そこで見つけた情報で心の健康を改善しようとする人もいます。その理由の一つは、役立つ情報を無料で見つけられる可能性があることです。",
                "1,000人を超える若者を対象とした研究は、彼らがソーシャルメディアで得た良い経験を示しました。研究中、若者たちはソーシャルメディアの良い点をいくつか挙げました。例えば、半数を超える人が、つらい時にソーシャルメディアのおかげで安心できたと答えました。また、多くの人が受け入れられていると感じたと答えました。言い換えると、ソーシャルメディア上で他者とのつながりを感じ、支援を得られると考えているのです。",
                "しかし、ある専門家は、ソーシャルメディアを通じて心の健康の問題を解決しようとすることが必ずしも良いとは限らないと言います。情報の中には、信頼すべきでないものや、専門的でないものがあるからです。例えば、特定の精神疾患に関するソーシャルメディア上の情報がどの程度信頼できるかを調べる研究が行われました。その結果、一部の情報は実際には間違っていました。そのような情報を使って精神疾患を治療すると、本人に悪影響を及ぼす可能性があります。",
                "このように、ソーシャルメディアが悪い方向に働く場合もあります。こうした状況を避けるために、人々にできることがあると専門家は述べています。例えば、心の健康についてインターネットで情報を得るなら、その情報がその分野の専門家から出たものか確認すべきです。そうすれば、ソーシャルメディアは本当に心の健康に役立ち、人々はそこから助けを得られます。",
            ],
            "sentencePairs": [
                ["Today, people often talk about the negative effects of social media.", "今日、人々はソーシャルメディアの悪影響についてよく話します。"],
                ["However, social media can positively influence mental health.", "しかし、ソーシャルメディアは心の健康に良い影響を与えることもできます。"],
                ["In fact, it seems to be helpful for many people with mental health problems.", "実際、心の健康に問題を抱える多くの人に役立つようです。"],
                ["While some of them go to a doctor for help, others rely on social media and try to improve their mental health with information they find on it.", "医者に助けを求める人もいれば、ソーシャルメディアに頼り、そこで見つけた情報で心の健康を改善しようとする人もいます。"],
                ["One reason for this is that they may be able to find useful information for free.", "その理由の一つは、役立つ情報を無料で見つけられる可能性があることです。"],
                ["A study of over 1,000 young people showed their positive experiences on social media.", "1,000人を超える若者を対象とした研究は、彼らがソーシャルメディアで得た良い経験を示しました。"],
                ["During the study, they shared several good things about social media.", "研究中、若者たちはソーシャルメディアの良い点をいくつか挙げました。"],
                ["For example, more than half of them said that they could feel safe when they were having a hard time, thanks to social media.", "例えば、半数を超える人が、つらい時にソーシャルメディアのおかげで安心できたと答えました。"],
                ["Also, many of them said that they felt accepted.", "また、多くの人が受け入れられていると感じたと答えました。"],
                ["In other words, they believe they can feel connected to others and get support from them on social media.", "言い換えると、ソーシャルメディア上で他者とのつながりを感じ、支援を得られると考えているのです。"],
                ["However, one expert says that trying to solve mental health problems through social media is not necessarily good.", "しかし、ある専門家は、ソーシャルメディアを通じて心の健康の問題を解決しようとすることが必ずしも良いとは限らないと言います。"],
                ["This is because some information should not be trusted or is not professional.", "情報の中には、信頼すべきでないものや、専門的でないものがあるからです。"],
                ["For example, a study was performed to check how much information on social media about a particular mental illness could be trusted.", "例えば、特定の精神疾患に関するソーシャルメディア上の情報がどの程度信頼できるかを調べる研究が行われました。"],
                ["The results showed some of the information was actually wrong.", "その結果、一部の情報は実際には間違っていました。"],
                ["If people use such information to treat their mental illness, it could have a negative impact on them.", "そのような情報を使って精神疾患を治療すると、本人に悪影響を及ぼす可能性があります。"],
                ["In this way, there are times when social media can work in a negative way.", "このように、ソーシャルメディアが悪い方向に働く場合もあります。"],
                ["To avoid these situations, the expert suggests there is something people can do.", "こうした状況を避けるために、人々にできることがあると専門家は述べています。"],
                ["For example, if people want to use the Internet to get information about mental health, they should check that the information comes from experts in the field.", "例えば、心の健康についてインターネットで情報を得るなら、その情報がその分野の専門家から出たものか確認すべきです。"],
                ["That way, social media can truly help mental health, and people can find help from social media.", "そうすれば、ソーシャルメディアは本当に心の健康に役立ち、人々はそこから助けを得られます。"],
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "Some people with mental health problems use social media because",
                    "questionTranslation": "精神的健康の問題を抱える人がソーシャルメディアを使う理由は？",
                    "choices": [
                        "it is the only place to get helpful information about health care.",
                        "it is the easiest way for them to choose the doctors they want to see.",
                        "they follow their parents' advice and take advantage of it.",
                        "they find free, useful advice to improve their mental health.",
                    ],
                    "choiceTranslations": [
                        "医療について役立つ情報を得られる唯一の場所だから。",
                        "診てもらいたい医者を選ぶ最も簡単な方法だから。",
                        "親のアドバイスに従い、それを活用するから。",
                        "精神的健康を改善する無料で有用な助言を見つけられるから。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "唯一の情報源。医者に助けを求める人もいるためonlyは誤り",
                        "医者を選ぶ方法。本文はSNS上の情報利用について述べる",
                        "親の助言に従う。parentsは本文に出てこない",
                        "無料で役立つ助言を得る。find useful information for freeの言い換え→正解。💡",
                    ],
                    "sourceEvidence": [
                        "they may be able to find useful information for free.",
                        "others rely on social media and try to improve their mental health with information they find on it.",
                    ],
                    "grammar": "💡 rely on ～＝～に頼る。improve one's mental health＝精神的健康を改善する。",
                },
                {
                    "number": 27,
                    "question": "What did the study of over 1,000 people show?",
                    "questionTranslation": "1,000人以上を対象とした研究が示したことは？",
                    "choices": [
                        "More than half of them do not think social media gives a sense of safety.",
                        "More than half of them do not use social media to find mental support.",
                        "Social media makes every young person feel connected all the time.",
                        "Social media helps many young people feel better during tough times.",
                    ],
                    "choiceTranslations": [
                        "半数以上が、ソーシャルメディアは安心感を与えないと考えている。",
                        "半数以上がメンタルサポートのためにソーシャルメディアを使わない。",
                        "ソーシャルメディアはすべての若者に、常に人とつながっていると感じさせる。",
                        "ソーシャルメディアは多くの若者がつらい時に気持ちが楽になる助けとなる。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "安心感を与えない。半数超がfeel safeと答えた記述と反対",
                        "支援を求めるために使わない。肯定的な経験の報告と合わない",
                        "全員が常につながる。manyをevery/all the timeへ広げすぎ",
                        "つらい時に多くの若者を助ける。feel safeやget supportを要約→正解。💡",
                    ],
                    "sourceEvidence": [
                        "more than half of them said that they could feel safe when they were having a hard time, thanks to social media.",
                        "they believe they can feel connected to others and get support from them on social media.",
                    ],
                    "grammar": "💡 more than half of ～＝～の半数以上。feel connected to ～＝～とつながっていると感じる。",
                },
                {
                    "number": 28,
                    "question": "What does one expert say about information about mental health problems on social media?",
                    "questionTranslation": "専門家はソーシャルメディア上の精神的健康に関する情報について何と言っているか？",
                    "choices": [
                        "There is not much wrong information that has been found so far.",
                        "Most information can be trusted because it comes from doctors.",
                        "It is not always a good idea to trust any information on social media.",
                        "Information on social media will be fully replaced with doctors' advice.",
                    ],
                    "choiceTranslations": [
                        "これまでに見つかった誤った情報はあまり多くない。",
                        "ほとんどの情報は医者によるものなので信頼できる。",
                        "ソーシャルメディアの情報をすべて信じるのは必ずしも良くない。",
                        "ソーシャルメディアの情報は医者のアドバイスに完全に置き換わる。",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "誤情報は少ない。量の少なさは示されていない",
                        "大半は医者の情報。専門的でない情報もあると述べる",
                        "どんな情報でも信じるのはよくない。not necessarily goodと一致→正解。💡",
                        "医者の助言に完全に置換される。その予測は本文にない",
                    ],
                    "sourceEvidence": [
                        "trying to solve mental health problems through social media is not necessarily good.",
                        "some information should not be trusted or is not professional.",
                    ],
                    "grammar": "💡 not necessarily＝必ずしも～ではない。should not be trusted＝信頼すべきではない。",
                },
                {
                    "number": 29,
                    "question": "What does the expert suggest about using the Internet for mental health?",
                    "questionTranslation": "専門家は精神的健康のためにインターネットを使うことについて何を勧めているか？",
                    "choices": [
                        "People should develop the habit of relying on doctors and stop using social media.",
                        "People should use information from experts in the field of mental health.",
                        "People should ask experts which information on social media to rely on.",
                        "People should rely on information on social media and doctors' opinions equally.",
                    ],
                    "choiceTranslations": [
                        "医者に頼る習慣を身につけ、ソーシャルメディアの使用をやめるべきだ。",
                        "精神的健康の分野の専門家による情報を使うべきだ。",
                        "ソーシャルメディアのどの情報を信じるか専門家に尋ねるべきだ。",
                        "ソーシャルメディアの情報と医者の意見に同じように頼るべきだ。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "SNSをやめる。提案は使用停止ではなく情報源の確認",
                        "専門家による情報を使う。comes from expertsの言い換え→正解。💡",
                        "どの情報を信じるか専門家に尋ねる。自分で情報源を確認する話",
                        "SNS情報と医師の意見を同等に扱う。その割合は示されていない",
                    ],
                    "sourceEvidence": [
                        "they should check that the information comes from experts in the field.",
                    ],
                    "grammar": "💡 experts in the field＝その分野の専門家。check that ～＝～であることを確認する。",
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

if len(data.get("sections", [])) < 3:
    raise SystemExit("sections 0-2 not found — run section1/2/3 scripts first")

data["sections"] = [
    data["sections"][0],
    data["sections"][1],
    data["sections"][2],
    section4,
]

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(p["questions"]) for p in section4["passages"])
print(f"Wrote section4 ({q_count} questions) to {DATA_PATH}")
