# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級 data.json
Step C: 大問3（passage-fill型）Q21〜22「The Advice」— リッチ解説
一次ソース: 2026-1(本会場）/準2級.pdf / 準2級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2", "2026-1", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "passage-fill",
    "instruction": "次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "",
            "title": "The Advice",
            "paragraphs": [
                "Haruto is a high school student in Tokyo. Although he enjoyed studying English, he was always afraid to speak the language. He worried that he might be embarrassed if his English was wrong. One day, he talked with his older sister, who spoke English very well. She told him that there was ( 21 ). She even explained that it was a necessary step to improve his skills. Thanks to her, Haruto's attitude toward speaking English changed.",
                "One day, his teacher, Ms. Sato, gave a speech activity in her English class. Haruto still felt worried, but he decided to do his best. When his turn came, he stood up and spoke clearly, despite feeling nervous. He knew that ( 22 ). When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good. She also explained how he could make it even better. From that day, he began to enjoy speaking English.",
            ],
            "translations": [
                "ハルトは東京の高校生です。英語を勉強するのは楽しんでいましたが、話すことはいつも怖かったのです。英語が間違っていたら恥ずかしい思いをするかもしれないと心配していました。ある日、英語がとても上手な姉と話しました。姉は彼に、( 21 )と言いました。さらに、それはスキルを上げるために必要な段階だと説明しました。姉のおかげで、ハルトの英語を話すことへの態度は変わりました。",
                "ある日、佐藤先生は英語の授業でスピーチの活動を行いました。ハルトはまだ不安でしたが、ベストを尽くすことにしました。自分の番が来ると、緊張しながらも立ち上がり、はっきりと話しました。彼は( 22 )ことを知っていました。しかしスピーチ全体を終えると、佐藤先生は微笑んで、とてもよいスピーチだったと言いました。さらに、どうすればもっとよくできるかも説明してくれました。その日から、彼は英語を話すことを楽しみ始めました。",
            ],
            "sentencePairs": [
                [
                    "Although he enjoyed studying English, he was always afraid to speak the language.",
                    "英語を勉強するのは楽しんでいましたが、話すことはいつも怖かったのです。",
                ],
                [
                    "He worried that he might be embarrassed if his English was wrong.",
                    "英語が間違っていたら恥ずかしい思いをするかもしれないと心配していました。",
                ],
                [
                    "She even explained that it was a necessary step to improve his skills.",
                    "さらに、それはスキルを上げるために必要な段階だと説明しました。",
                ],
                [
                    "Thanks to her, Haruto's attitude toward speaking English changed.",
                    "姉のおかげで、ハルトの英語を話すことへの態度は変わりました。",
                ],
                [
                    "Haruto still felt worried, but he decided to do his best.",
                    "ハルトはまだ不安でしたが、ベストを尽くすことにしました。",
                ],
                [
                    "When his turn came, he stood up and spoke clearly, despite feeling nervous.",
                    "自分の番が来ると、緊張しながらも立ち上がり、はっきりと話しました。",
                ],
                [
                    "When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good.",
                    "しかしスピーチ全体を終えると、佐藤先生は微笑んで、とてもよいスピーチだったと言いました。",
                ],
                [
                    "She also explained how he could make it even better.",
                    "さらに、どうすればもっとよくできるかも説明してくれました。",
                ],
                [
                    "From that day, he began to enjoy speaking English.",
                    "その日から、彼は英語を話すことを楽しみ始めました。",
                ],
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": [
                        "no need to speak English",
                        "only one way for language learning",
                        "something more important than trying hard",
                        "nothing wrong with making mistakes",
                    ],
                    "choiceTranslations": [
                        "英語を話す必要はない",
                        "語学学習には一つの方法しかない",
                        "一生懸命やることより大切なことがある",
                        "間違えても何も悪いことはない",
                    ],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ no need to speak English＝英語を話す必要はない。He was always afraid to speak the language（話すのが怖い）という悩みに対し、話さなくてよいと言っても前に進まない",
                        "❌ only one way for language learning＝語学学習には一つの方法しかない。He worried that he might be embarrassed if his English was wrong（間違えて恥ずかしい）という個人の不安が論点で、学習法の数の話ではない",
                        "❌ something more important than trying hard＝一生懸命やることより大切なことがある。it was a necessary step to improve his skills（上達のための必要な段階）とあり、努力そのものを否定する内容ではない",
                        "✅ nothing wrong with making mistakes＝間違えても何も悪いことはない。embarrassed if his English was wrong（間違えて恥ずかしい）への助言として自然。a necessary step to improve his skills（上達のための必要な段階）とも一致→正解",
                    ],
                    "sourceEvidence": [
                        "He worried that he might be embarrassed if his English was wrong.",
                        "She even explained that it was a necessary step to improve his skills.",
                    ],
                    "grammar": "💡 there is nothing wrong with ～ing＝～しても何も悪いことはない。be embarrassed if ～ was wrong（間違っていたら恥ずかしい）と対になる姉のアドバイスを読む。",
                },
                {
                    "number": 22,
                    "choices": [
                        "his speech was not perfect",
                        "his classmate made the same mistake",
                        "he could not continue his speech",
                        "he had forgotten his speech",
                    ],
                    "choiceTranslations": [
                        "自分のスピーチは完璧ではなかった",
                        "クラスメートが同じ間違いをした",
                        "スピーチを続けられなかった",
                        "スピーチの内容を忘れていた",
                    ],
                    "answer": 1,
                    "choiceAnalysis": [
                        "✅ his speech was not perfect＝自分のスピーチは完璧ではなかった。He knew that ～の後、his speech was very good（とてもよかった）＋how he could make it even better（もっとよくする方法）が「良いが完璧ではない」と読める→正解",
                        "❌ his classmate made the same mistake＝クラスメートが同じ間違いをした。When his turn came, he stood up and spoke clearly（自分の番で立ってはっきり話した）とあり、論点はハルト自身のスピーチ",
                        "❌ he could not continue his speech＝スピーチを続けられなかった。When he finished the whole speech（スピーチ全体を終えた）と記述が食い違う",
                        "❌ he had forgotten his speech＝スピーチの内容を忘れていた。spoke clearly, despite feeling nervous（緊張しながらもはっきり話した）なら、内容を忘れていたとは読めない",
                    ],
                    "sourceEvidence": [
                        "When he finished the whole speech, however, Ms. Sato smiled and said his speech was very good.",
                        "She also explained how he could make it even better.",
                    ],
                    "grammar": "💡 make it even better＝（それを）さらに良くする。very good だが even better がある＝まだ改善の余地がある＝完璧ではなかった、という読み取りが決め手。",
                },
            ],
        }
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

section1 = next(s for s in data["sections"] if s["name"] == "大問1")
section2 = next(s for s in data["sections"] if s["name"] == "大問2")
others = [s for s in data["sections"] if s["name"] not in ("大問1", "大問2", "大問3")]
data["sections"] = [section1, section2, section3] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section3 ({len(section3['passages'][0]['questions'])} questions) to {DATA_PATH}")
