# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス data.json
Step B: 大問2（passage-fill型）Q18〜23
  2A Guide Signs Without Words / 2B Attention Span
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文 A, B を読み、その文意にそって (18) から (23) までの ( ) に入れるのに最も適切なものを 1, 2, 3, 4 の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Guide Signs Without Words",
            "paragraphs": [
                "Pictograms are a type of guide sign. They do not depend on language. This is because they use images instead of words to share information. Therefore, problems ( 18 ) can be avoided. This makes pictograms useful for people around the world because they can easily and quickly understand what the images mean. Today, pictograms can be found in many fields of daily life, such as transportation, tourism, and weather. One of the most common situations where they appear is at the Olympic Games.",
                "Pictograms were first used as signs for many sports and some events in the Olympic Games many years ago. For example, the Games in Paris in 1924 and London in 1948 used pictograms on tickets and programs. However, there was one ( 19 ). They were often too complex in style and too detailed, which made them difficult to understand quickly. This fact clearly showed the need for simpler and more effective visual communication at international events.",
                "A major change in pictograms was introduced at the 1964 Tokyo Olympic Games. Unlike earlier versions, the design team at the time tried to create much simpler pictograms while still showing the meaning without words. These new pictograms were used to guide visitors, athletes, and staff members throughout the event. Their success demonstrated how effective simple visual communication could be. ( 20 ), a new standard for pictograms was set. Since then, pictograms have continued to play an important role in supporting the Olympic Games.",
            ],
            "translations": [
                "ピクトグラムは案内標識の一種です。言語に依存しません。これは、情報を共有するために言葉の代わりに画像を使うからです。したがって、( 18 )による問題は避けられます。世界中の人々が画像の意味を簡単かつ素早く理解できるため、ピクトグラムは有用です。今日、ピクトグラムは交通、観光、天気など日常生活の多くの分野で見られます。最も一般的な場面の一つはオリンピックです。",
                "ピクトグラムは何年も前から、多くのスポーツやオリンピックのイベントの標識として使われてきました。例えば、1924年のパリ大会と1948年のロンドン大会では、チケットやプログラムにピクトグラムが使われました。しかし、( 19 )が一つありました。スタイルが複雑すぎ、詳細すぎることが多く、素早く理解するのが難しいものでした。この事実は、国際的なイベントにおいてよりシンプルで効果的な視覚的コミュニケーションの必要性を明確に示しました。",
                "ピクトグラムの大きな変化は1964年の東京オリンピックで導入されました。以前の版とは異なり、当時のデザインチームは、言葉なしで意味を示しながら、はるかにシンプルなピクトグラムを作ろうとしました。これらの新しいピクトグラムは、来場者、選手、スタッフをイベント全体で案内するために使われました。その成功は、シンプルな視覚的コミュニケーションがいかに効果的かを示しました。( 20 )、ピクトグラムの新しい基準が設定されました。それ以来、ピクトグラムはオリンピックを支える重要な役割を果たし続けています。",
            ],
            "sentencePairs": [
                [
                    "They do not depend on language.",
                    "言語に依存しません。",
                ],
                [
                    "This is because they use images instead of words to share information.",
                    "これは、情報を共有するために言葉の代わりに画像を使うからです。",
                ],
                [
                    "They were often too complex in style and too detailed, which made them difficult to understand quickly.",
                    "スタイルが複雑すぎ、詳細すぎることが多く、素早く理解するのが難しいものでした。",
                ],
                [
                    "Their success demonstrated how effective simple visual communication could be.",
                    "その成功は、シンプルな視覚的コミュニケーションがいかに効果的かを示しました。",
                ],
                [
                    "These new pictograms were used to guide visitors, athletes, and staff members throughout the event.",
                    "これらの新しいピクトグラムは、来場者、選手、スタッフをイベント全体で案内するために使われました。",
                ],
            ],
            "questions": [
                {
                    "number": 18,
                    "choices": [
                        "influenced through social media",
                        "caused by language differences",
                        "shown in large pictures",
                        "related to written construction",
                    ],
                    "choiceTranslations": [
                        "ソーシャルメディアの影響を受けた",
                        "言語の違いによって引き起こされた",
                        "大きな絵で示された",
                        "書かれた構成に関連した",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ ソーシャルメディアの影響→本文に social media の記述はなく、ピクトグラムが言語に依存しない話と無関係",
                        "✅ 言語の違いによる問題→正解。💡 do not depend on language（言語に依存しない）＋use images instead of words が決め手",
                        "❌ 大きな絵で示された→shown in large pictures では「問題を避ける」という因果関係が説明できない",
                        "❌ 書かれた構成に関連→written construction は本文にない。images instead of words とは別の話",
                    ],
                    "grammar": "💡 problems caused by ～＝～によって引き起こされる問題。Therefore の前後で「言葉ではなく画像→言語差の問題を回避」と読む。",
                },
                {
                    "number": 19,
                    "choices": [
                        "celebration of the Olympic spirit",
                        "example of modern art",
                        "reason for using colors",
                        "issue with the early designs",
                    ],
                    "choiceTranslations": [
                        "オリンピック精神の祝賀",
                        "現代美術の例",
                        "色を使う理由",
                        "初期のデザインの問題点",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ オリンピック精神の祝賀→However 以降は問題点の指摘。celebration（祝賀）では too complex / too detailed と結びつかない",
                        "❌ 現代美術の例→example of modern art では「理解しにくい」という問題の説明にならない",
                        "❌ 色を使う理由→本文に colors の記述はない",
                        "✅ 初期デザインの問題点→正解。💡 too complex in style and too detailed, which made them difficult to understand quickly",
                    ],
                    "grammar": "💡 there was one issue with ～＝～に一つ問題があった。However が「転換」の合図。直後の too complex / too detailed が空所の内容を特定する。",
                },
                {
                    "number": 20,
                    "choices": [
                        "To begin with",
                        "Most of all",
                        "In this way",
                        "Especially",
                    ],
                    "choiceTranslations": [
                        "まず第一に",
                        "何よりも",
                        "このようにして",
                        "特に",
                    ],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ まず第一に→To begin with は列挙の最初。ここは成功の結果として基準が設定された段階",
                        "❌ 何よりも→Most of all は強調だが、前後の因果（成功→基準設定）を結ばない",
                        "✅ このようにして→正解。💡 success demonstrated how effective ... could be → ( ) a new standard was set の「方法・結果」の結び",
                        "❌ 特に→Especially は例示・強調。新基準の設定という結果の説明には合わない",
                    ],
                    "grammar": "💡 In this way＝「このようにして」。直前の simpler pictograms の成功が、新しい基準設定につながったことを示す。",
                },
            ],
        },
        {
            "label": "B",
            "title": "Attention Span",
            "paragraphs": [
                "According to a study conducted by an IT company, humans have shorter attention spans than they did in the past. In fact, the study suggests people cannot focus as long as a goldfish. One key reason for this is mobile phones. Today, many people use social media platforms that show short videos and messages. These platforms hardly require a long attention span. ( 21 ), the human brain becomes used to receiving only small amounts of information. People find it hard to stop using these platforms. This makes the problem even worse.",
                "The impact of shorter attention spans on young students seems very large. Another study showed that about 30 percent of teenagers reported difficulty focusing in class because they often checked their mobile phones. The negative effects of mobile-phone use are also seen in other parts of people's lives. Problems can even occur when people are ( 22 ). For example, people who often use their mobile phones are less likely to stay focused on reading books or remembering information, and giving up is getting easier for them.",
                "Some experts suggest a few solutions to help people maintain a longer attention span. A simple approach is to take regular breaks. It is said to be important to avoid a state where people get mentally too tired and lose control of their attention. In addition, understanding ( 23 ) is considered helpful. This means people should know when they can and cannot focus during the day. That will help people plan their day and perform their tasks successfully.",
            ],
            "translations": [
                "IT企業が実施した調査によると、人間の注意力の持続時間は過去より短くなっています。実際、その調査は人々が金魚ほど長く集中できないと示唆しています。主な理由の一つは携帯電話です。今日、多くの人が短い動画やメッセージを見せるソーシャルメディアのプラットフォームを使っています。これらのプラットフォームは長い注意力をほとんど必要としません。( 21 )、人間の脳は少量の情報しか受け取らないことに慣れてしまいます。人々はこれらのプラットフォームの使用をやめるのが難しくなります。これが問題をさらに悪化させます。",
                "若い学生への短い注意力の影響は非常に大きいようです。別の調査では、十代の約30％が授業中に集中するのが難しいと報告し、よく携帯電話を確認していたと述べました。携帯電話使用の悪影響は人々の生活の他の場面でも見られます。人々が( 22 )ときでさえ、問題が起こることがあります。例えば、携帯電話をよく使う人は、本を読んだり情報を覚えたりすることに集中しにくく、諦めることがより容易になっています。",
                "専門家は、より長い注意力を維持するためのいくつかの解決策を提案しています。簡単な方法は定期的に休憩を取ることです。精神的に疲れすぎて注意力のコントロールを失う状態を避けることが重要だと言われています。さらに、( 23 )を理解することが役立つと考えられています。これは、人々が一日のうちいつ集中でき、いつできないかを知るべきだという意味です。それは一日を計画し、任務をうまく遂行するのに役立ちます。",
            ],
            "sentencePairs": [
                [
                    "One key reason for this is mobile phones.",
                    "主な理由の一つは携帯電話です。",
                ],
                [
                    "These platforms hardly require a long attention span.",
                    "これらのプラットフォームは長い注意力をほとんど必要としません。",
                ],
                [
                    "about 30 percent of teenagers reported difficulty focusing in class because they often checked their mobile phones.",
                    "十代の約30％が授業中に集中するのが難しいと報告し、よく携帯電話を確認していたと述べました。",
                ],
                [
                    "This means people should know when they can and cannot focus during the day.",
                    "これは、人々が一日のうちいつ集中でき、いつできないかを知るべきだという意味です。",
                ],
                [
                    "A simple approach is to take regular breaks.",
                    "簡単な方法は定期的に休憩を取ることです。",
                ],
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "As a result",
                        "Even so",
                        "On the other hand",
                        "Fortunately",
                    ],
                    "choiceTranslations": [
                        "その結果",
                        "それでも",
                        "一方で",
                        "幸いにも",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ その結果→正解。💡 hardly require a long attention span → brain becomes used to receiving only small amounts of information という因果",
                        "❌ それでも→Even so は譲歩。短い動画が注意力を要しないことと脳の変化は矛盾関係ではない",
                        "❌ 一方で→On the other hand は対比。前後は原因と結果の流れ",
                        "❌ 幸いにも→Fortunately は好意的な転換。脳が少量の情報に慣れるのは問題の側面であり「幸い」ではない",
                    ],
                    "grammar": "💡 As a result＝その結果。SNSが短い注意力しか要しない → 脳が少量の情報に慣れる、という因果連鎖を読む。",
                },
                {
                    "number": 22,
                    "choices": [
                        "not studying at home",
                        "not using their phones",
                        "sleeping well at night",
                        "trying to find their phones",
                    ],
                    "choiceTranslations": [
                        "家で勉強していないとき",
                        "携帯電話を使っていないとき",
                        "夜よく眠っているとき",
                        "携帯電話を探しているとき",
                    ],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 家で勉強していない→not studying at home では直後の reading books / remembering information との関係が弱い",
                        "✅ 携帯電話を使っていないとき→正解。💡 スマホを使わない別の活動（読書・記憶）のときでも集中できない、という悪影響の広がり",
                        "❌ 夜よく眠っている→sleeping well at night では reading books の例と結びつかない",
                        "❌ 携帯電話を探している→trying to find their phones は本文の論点（注意力の低下）と無関係",
                    ],
                    "grammar": "💡 For example 以降が空所の具体例。often use mobile phones なのに not using phones のとき問題が起きる＝スマホ依存が他の活動の集中力も奪う、と読む。",
                },
                {
                    "number": 23,
                    "choices": [
                        "their sleeping patterns",
                        "their preferred study location",
                        "personal eating habits",
                        "personal attention rhythms",
                    ],
                    "choiceTranslations": [
                        "睡眠パターン",
                        "好みの勉強場所",
                        "個人の食習慣",
                        "個人の注意力のリズム",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ 睡眠パターン→sleeping patterns は本文に出てこない。when they can and cannot focus とは別の話",
                        "❌ 好みの勉強場所→preferred study location は集中の「時間帯」ではなく「場所」の話",
                        "❌ 食習慣→personal eating habits は注意力の維持と無関係",
                        "✅ 個人の注意力のリズム→正解。💡 know when they can and cannot focus during the day（いつ集中できるか）と完全一致",
                    ],
                    "grammar": "💡 This means ～ で空所の内容を言い換え。plan their day and perform their tasks successfully が「リズムを知る」利点を示す。",
                },
            ],
        },
    ],
}

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

sections = data.get("sections", [])
others_before = [s for s in sections if s.get("name") == "大問1"]
others_after = [s for s in sections if s.get("name") not in ("大問1", "大問2")]
data["sections"] = others_before + [section2] + others_after

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section2 (6 questions, 2 passages) to {DATA_PATH}")
