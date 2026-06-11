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
                "仕事にはリゾートでのさまざまな役割が含まれます。ギフトショップでの接客やレンタル器材の依頼への対応などです。道路の除雪も含まれます。カフェテリアやホテルでの仕事は含まれません。週5日、約1ヶ月働きます。日中ではなく夕方に行う仕事もあります。残りの時間は自由に過ごせます。",
                "リゾートでもらえるものについてお伝えします。まず、毎日3食無料です。働かない日でも同様です。また、スキーやスノーボードを無料で楽しめます。自分だけの無料の部屋もあります。ただし、お客が泊まるのと同じホテルではありません。質問があれば面接で聞けます。ありがとう、ブレイク・ジョーンズ",
            ],
            "sentencePairs": [
                [
                    "You need to send a message to the ski resort by November 5.",
                    "11月5日までにスキーリゾートにメッセージを送る必要があります。",
                ],
                [
                    "Then, you will have an online interview on November 10.",
                    "その後、11月10日にオンライン面接があります。",
                ],
                [
                    "The job includes many different roles at the resort, like serving customers in the gift shop and handling requests to rent equipment.",
                    "仕事にはギフトショップでの接客やレンタル器材の依頼への対応など、リゾートでのさまざまな役割が含まれます。",
                ],
                [
                    "Working in the cafeteria or hotel is not part of the job.",
                    "カフェテリアやホテルでの仕事は含まれません。",
                ],
                [
                    "Some work will be done in the evenings instead of during the day.",
                    "日中ではなく夕方に行う仕事もあります。",
                ],
                [
                    "First, three free meals are served every day, even on the days you don't work.",
                    "毎日3食無料です。働かない日でも同様です。",
                ],
                [
                    "Also, you are allowed to ski or snowboard there for free.",
                    "スキーやスノーボードを無料で楽しめます。",
                ],
                [
                    "And you will have a free room just for yourself.",
                    "自分だけの無料の部屋もあります。",
                ],
                [
                    "However, it is not in the same hotel where the customers stay.",
                    "お客が泊まるのと同じホテルではありません。",
                ],
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
                        "❌ make a phone call to the ski resort＝電話する。You need to send a message to the ski resort（メッセージを送る）と異なる",
                        "❌ tell Blake Jones by November 10＝ブレイクに11月10日まで。online interview on November 10（面接の日）であり、連絡期限は11月5日",
                        "✅ contact the ski resort by November 5＝11月5日までに連絡。You need to send a message to the ski resort by November 5 と一致→正解",
                        "❌ have experience working at a ski resort＝勤務経験。本文に experience の要件の記載は出てこない",
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
                        "❌ cleaning rooms at the hotel＝ホテルの部屋掃除。Working in the cafeteria or hotel is not part of the job（ホテルでの仕事は含まれない）と矛盾",
                        "❌ working at night five days a week＝週5日夜勤。Some work will be done in the evenings（一部が夕方）であり、週5日すべての夜勤ではない",
                        "❌ serving customers in the cafeteria＝カフェテリアの接客。Working in the cafeteria or hotel is not part of the job と明記",
                        "✅ helping people who rent items＝レンタル品の手伝い。handling requests to rent equipment（レンタル依頼に対応）と一致→正解",
                    ],
                    "sourceEvidence": [
                        "handling requests to rent equipment",
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
                        "いつでも3食無料で食べられる。",
                        "スキーは無料だがスノーボードはできない。",
                        "友人と相部屋で寝られる。",
                        "お客と同じホテルに泊まれる。",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ have three meals for free on any day＝いつでも3食無料。three free meals are served every day, even on the days you don't work と一致→正解",
                        "❌ ski there without paying but cannot snowboard＝スノーボード不可。you are allowed to ski or snowboard there for free（両方無料）",
                        "❌ sleep in a room shared with his friend＝友人と相部屋。a free room just for yourself（自分だけの部屋）",
                        "❌ stay in the same hotel as the customers＝お客と同じホテル。it is not in the same hotel where the customers stay と矛盾",
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
                "今日、人々はソーシャルメディアの悪影響についてよく話します。しかし、ソーシャルメディアは精神的健康に良い影響を与えることができます。実際、精神的健康の問題を抱える多くの人にとって役立つようです。医者の助けを求める人もいれば、ソーシャルメディアに頼り、そこで見つけた情報で精神的健康を改善しようとする人もいます。その理由の一つは、有用な情報を無料で見つけられる可能性があることです。",
                "1,000人以上の若者を対象とした研究が、ソーシャルメディアでのポジティブな経験を示しました。研究の間、彼らはソーシャルメディアについての良い点をいくつか共有しました。例えば、半数以上が、辛いときにソーシャルメディアのおかげで安心感を得られると答えました。また多くの人が受け入れられたと感じたと言いました。つまり、ソーシャルメディアで他者とつながり、支援を得られると信じているのです。",
                "しかし、ある専門家は、ソーシャルメディアで精神的健康の問題を解決しようとすることは必ずしも良いことではないと言います。一部の情報は信頼すべきではない、または専門的ではないからです。例えば、特定の精神疾患についてソーシャルメディア上の情報がどれだけ信頼できるかを調べる研究が行われました。結果、一部の情報は実際に誤りであることがわかりました。そのような情報で治療すると、悪影響を及ぼす可能性があります。",
                "このように、ソーシャルメディアがネガティブに働く場合もあります。これを避けるため、専門家は人々にできることがあると示唆しています。例えば、精神的健康についてインターネットで情報を得たい場合、その情報がその分野の専門家によるものか確認すべきだと。そうすれば、ソーシャルメディアは本当に精神的健康の助けになり、人々はソーシャルメディアから助けを見つけられるのです。",
            ],
            "sentencePairs": [
                [
                    "However, social media can positively influence mental health.",
                    "ソーシャルメディアは精神的健康に良い影響を与えることができます。",
                ],
                [
                    "One reason for this is that they may be able to find useful information for free.",
                    "有用な情報を無料で見つけられる可能性があることです。",
                ],
                [
                    "For example, more than half of them said that they could feel safe when they were having a hard time, thanks to social media.",
                    "半数以上が、辛いときにソーシャルメディアのおかげで安心感を得られると答えました。",
                ],
                [
                    "In other words, they believe they can feel connected to others and get support from them on social media.",
                    "ソーシャルメディアで他者とつながり、支援を得られると信じているのです。",
                ],
                [
                    "However, one expert says that trying to solve mental health problems through social media is not necessarily good.",
                    "ソーシャルメディアで精神的健康の問題を解決しようとすることは必ずしも良いことではないと言います。",
                ],
                [
                    "The results showed some of the information was actually wrong.",
                    "一部の情報は実際に誤りであることがわかりました。",
                ],
                [
                    "For example, if people want to use the Internet to get information about mental health, they should check that the information comes from experts in the field.",
                    "精神的健康についてインターネットで情報を得たい場合、その情報がその分野の専門家によるものか確認すべきです。",
                ],
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
                        "ヘルスケアの有用な情報を得られる唯一の場所だから。",
                        "見たい医者を選ぶ最も簡単な方法だから。",
                        "親のアドバイスに従い、それを活用するから。",
                        "精神的健康を改善する無料で有用な助言を見つけられるから。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ the only place to get helpful information＝唯一の場所。While some of them go to a doctor for help（医者の助けもある）とあり、唯一ではない",
                        "❌ the easiest way to choose the doctors＝医者を選ぶ方法。rely on social media and try to improve their mental health with information（SNS上の情報）が論点",
                        "❌ they follow their parents' advice＝親のアドバイス。本文に parents の言及は出てこない",
                        "✅ they find free, useful advice to improve their mental health＝無料で有用な助言。find useful information for free（無料で有用な情報）と一致→正解",
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
                        "半数以上がソーシャルメディアに安心感を与えないと考えている。",
                        "半数以上がメンタルサポートのためにソーシャルメディアを使わない。",
                        "ソーシャルメディアはすべての若者を常につながった気にさせる。",
                        "ソーシャルメディアは多くの若者が辛い時期を乗り越える助けになる。",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ do not think social media gives a sense of safety＝安心感を与えない。more than half said they could feel safe when they were having a hard time（半数以上が安心感）と正反対",
                        "❌ do not use social media to find mental support＝使わない。their positive experiences on social media（ポジティブな経験）と矛盾",
                        "❌ makes every young person feel connected all the time＝すべての若者が常に。many of them said that they felt accepted（多くの人が）と、every/all the time は極端",
                        "✅ helps many young people feel better during tough times＝辛い時期の助け。feel safe when having a hard time, feel accepted, feel connected と総合→正解",
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
                        "❌ not much wrong information has been found＝誤情報は少ない。some of the information was actually wrong（実際に誤り）と矛盾",
                        "❌ most information can be trusted because it comes from doctors＝医者によるので信頼できる。some information should not be trusted or is not professional（信頼すべきでない）と矛盾",
                        "✅ it is not always a good idea to trust any information on social media＝すべて信じるのは良くない。not necessarily good, should not be trusted と一致→正解",
                        "❌ information will be fully replaced with doctors' advice＝医者のアドバイスに完全置換。本文にそのような予測の記述はない",
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
                        "ソーシャルメディアの情報と医者の意見を同等に頼るべきだ。",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ stop using social media＝SNSをやめる。check that the information comes from experts（情報源を確認）する提案であり、使用停止ではない",
                        "✅ use information from experts in the field of mental health＝専門家による情報を使う。check that the information comes from experts in the field と一致→正解",
                        "❌ ask experts which information to rely on＝専門家にどれを信じるか尋ねる。情報源を自分で確認すべきという提案",
                        "❌ rely on information and doctors' opinions equally＝同等に頼る。本文にそのようなバランスの指示は出てこない",
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

for pa in section4["passages"]:
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
