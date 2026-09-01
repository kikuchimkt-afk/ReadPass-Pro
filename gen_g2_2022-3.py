# -*- coding: utf-8 -*-
"""Build the audited ReadPass data set for EIKEN Grade 2, 2022-3 main venue."""

import json
import os
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent
OUT_DIR = REPO / "data" / "grade2" / "2022-3"
OUT_PATH = OUT_DIR / "data.json"

ANSWERS = dict(enumerate([
    3, 1, 3, 1, 1, 4, 4, 3, 2, 2,
    1, 2, 3, 1, 1, 4, 3, 1, 3, 3,
    3, 4, 2, 3, 1, 3,
    1, 1, 3, 4, 1, 2, 4, 1, 3, 1, 3, 2,
], 1))

LISTENING = {
    "part1": {str(i + 1): value for i, value in enumerate(
        [2, 4, 2, 2, 3, 1, 2, 1, 2, 1, 4, 3, 2, 3, 4]
    )},
    "part2": {str(i + 16): value for i, value in enumerate(
        [4, 1, 2, 3, 4, 1, 4, 1, 2, 1, 3, 1, 4, 2, 2]
    )},
}


def make_question(number, text, translation, choices, choice_ja, answer, reasons,
                  grammar, *, question=None, question_translation=None,
                  source_evidence=None):
    analyses = []
    for index, (choice, meaning, reason) in enumerate(zip(choices, choice_ja, reasons), 1):
        stem = f"{choice}（{meaning}）"
        if index == answer:
            analyses.append(f"{stem}→正解。💡{reason}")
        else:
            analyses.append(f"{stem}→{reason}")
    item = {
        "number": number,
        "text": text,
        "translation": translation,
        "choices": choices,
        "choiceTranslations": choice_ja,
        "answer": answer,
        "choiceAnalysis": analyses,
        "grammar": grammar,
    }
    if text is None:
        item.pop("text")
        item.pop("translation")
    if question is not None:
        item["question"] = question
        item["questionTranslation"] = question_translation
    if source_evidence:
        item["sourceEvidence"] = source_evidence
    return item


section1_questions = [
    make_question(
        1,
        "Jun taught his daughter an easy ( ) of making ice cream at home with milk, cream, sugar, and maple syrup.",
        "ジュンは娘に、牛乳、クリーム、砂糖、メープルシロップを使って家でアイスクリームを作る簡単な（　）を教えた。",
        ["cure", "register", "method", "slice"],
        ["治療法", "登録簿", "方法", "一切れ"], 3,
        ["病気を治す話ではない。", "登録簿は作り方を表さない。", "a method of doing で「…する方法」。", "一切れを教える、とはならない。"],
        "a method of doing は「…する方法」。of の後は動名詞 making が続く。",
    ),
    make_question(
        2,
        "Companies these days are making cameras that are ( ) small. Some are even smaller than a shirt button.",
        "近ごろ企業は（　）小さいカメラを作っている。中にはシャツのボタンより小さいものさえある。",
        ["incredibly", "partially", "eagerly", "consequently"],
        ["信じられないほど", "部分的に", "熱心に", "その結果"], 1,
        ["ボタンより小さいという驚くほどの程度を表す。", "「部分的に小さい」では程度の説明にならない。", "人の意欲を表す副詞で small を修飾できない。", "結果を導く接続副詞で small の程度を表さない。"],
        "incredibly は形容詞 small を強める程度の副詞。Some は前文の cameras を受ける。",
    ),
    make_question(
        3,
        "There are very few houses in the north part of Silver City. It is an ( ) area filled with factories and warehouses.",
        "シルバーシティ北部には住宅がほとんどない。そこは工場や倉庫でいっぱいの（　）地域である。",
        ["emergency", "instant", "industrial", "environmental"],
        ["緊急の", "即時の", "工業の", "環境の"], 3,
        ["工場や倉庫の特徴を表さない。", "時間的な「即時の」は地域の種類にならない。", "factories and warehouses が工業地域の根拠。", "環境地域という意味では住宅が少ない理由にならない。"],
        "filled with ... は「…で満たされた」。過去分詞句が area を後ろから修飾する。",
    ),
    make_question(
        4,
        "A: Do you think it’s going to rain tomorrow, Tetsuya?\nB: I ( ) it. The rainy season is over, and it’s been sunny all week.",
        "A：明日は雨が降ると思う、テツヤ？\nB：そうは（　）ね。梅雨は終わったし、一週間ずっと晴れているから。",
        ["doubt", "blame", "pardon", "affect"],
        ["疑う", "責める", "許す", "影響する"], 1,
        ["晴天が続いているため、雨になる可能性を疑っている。", "it は責任を負う人ではない。", "許しを与える文脈ではない。", "affect は他動詞だが「それに影響する」では返答にならない。"],
        "I doubt it. は相手の予想に対して「そうは思わない」。現在完了 it’s been は現在までの継続。",
    ),
    make_question(
        5,
        "A: Why has the office been so quiet recently?\nB: Since Amy and Ben had an argument, there has been a lot of ( ) between them.",
        "A：最近、なぜ職場がこんなに静かなの？\nB：エイミーとベンが口論して以来、二人の間には強い（　）があるんだ。",
        ["tension", "survival", "privacy", "justice"],
        ["緊張", "生存", "私生活・プライバシー", "正義"], 1,
        ["口論後に静かになった二人の気まずい緊張を表す。", "二人の生存についての話ではない。", "between them の気まずい関係を privacy とは言わない。", "正義の多少を表す文脈ではない。"],
        "Since S V は「SがVして以来」。there has been は現在完了で続く状態を表す。",
    ),
    make_question(
        6,
        "Julie’s teacher asked her to ( ) the new textbooks to all of the students. She had to place one on each desk in the classroom.",
        "ジュリーは先生から、新しい教科書を生徒全員に（　）よう頼まれた。教室の各机に一冊ずつ置かなければならなかった。",
        ["respond", "negotiate", "collapse", "distribute"],
        ["返答する", "交渉する", "崩壊する", "配る"], 4,
        ["respond は自動詞で textbooks を目的語に取らない。", "教科書について交渉する話ではない。", "教科書を崩壊させる、とはならない。", "各机に一冊置くので、生徒全員に配る。"],
        "ask 人 to do は「人に…するよう頼む」。distribute A to B は「AをBに配る」。",
    ),
    make_question(
        7,
        "A: Did your teacher ( ) your idea for your science project?\nB: No. He says that I’m not allowed to do anything that involves dangerous chemicals. I’ll have to think of something else.",
        "A：先生は理科研究の案を（　）してくれた？\nB：いいえ。危険な薬品を使うことは許されないと言われたよ。別の案を考えないと。",
        ["confine", "compare", "abandon", "approve"],
        ["制限する", "比較する", "断念する", "承認する"], 4,
        ["案を閉じ込める、ではない。", "比較対象が示されていない。", "先生が案を断念するという質問ではない。", "No と別案を考えるという返答から、承認しなかったと分かる。"],
        "be allowed to do は「…することを許される」。anything that ... は関係代名詞節が anything を修飾する。",
    ),
    make_question(
        8,
        "A: Is that the document you were looking for earlier?\nB: Yes, it is. It was ( ) under a pile of papers on my desk. I really need to be more organized.",
        "A：それがさっき探していた書類？\nB：そう。机の紙の山の下に（　）いたんだ。もっと整理しないとね。",
        ["dyed", "peeled", "buried", "honored"],
        ["染められた", "皮をむかれた", "埋もれた", "称えられた"], 3,
        ["書類を染めた話ではない。", "書類の皮をむく、とはならない。", "a pile of papers の下に埋もれていた。", "書類を称える文脈ではない。"],
        "the document (that) you were looking for は目的格の関係代名詞が省略されている。was buried は受動態。",
    ),
    make_question(
        9,
        "Many science-fiction authors have written about the ( ) of traveling at the speed of light. With future developments in technology, this idea could become a reality.",
        "多くのSF作家が光速で移動するという（　）について書いてきた。将来の技術発展で、この考えは現実になるかもしれない。",
        ["edition", "notion", "contact", "instinct"],
        ["版", "考え・概念", "接触", "本能"], 2,
        ["本の版についての話ではない。", "this idea が notion の言い換えになっている。", "光速との接触という意味ではない。", "技術的な考えを本能とは呼ばない。"],
        "the notion of doing は「…するという考え」。現在完了 have written は過去から現在までの経験・蓄積。",
    ),
    make_question(
        10,
        "When Hayley did some research into her ( ), she discovered that one of her great-grandfathers used to work in a famous theater in London.",
        "ヘイリーが自分の（　）を調べると、曽祖父の一人がかつてロンドンの有名な劇場で働いていたことが分かった。",
        ["angels", "ancestors", "employees", "enemies"],
        ["天使", "祖先", "従業員", "敵"], 2,
        ["曽祖父は天使ではなく家系の人物。", "great-grandfathers は祖先に当たる。", "自分の従業員を調べて曽祖父を知る流れではない。", "曽祖父を敵として調べたとは書かれていない。"],
        "do research into ... は「…を調査する」。used to do は「かつて…した」。",
    ),
    make_question(
        11,
        "The big storm caused a lot of damage to many of the homes in the city. The cost to repair all the damage ( ) over $70 million.",
        "大きな嵐が市内の多くの家に大きな被害を与えた。すべてを修理する費用は7,000万ドルを超える額に（　）。",
        ["amounted to", "aimed at", "calmed down", "checked with"],
        ["合計…になった", "…を狙った", "落ち着いた", "…に確認した"], 1,
        ["cost が金額に達したことを表す amount to が合う。", "費用が金額を狙う、とはならない。", "嵐なら落ち着くが、費用を主語にはしない。", "費用が人に確認する、とはならない。"],
        "amount to + 金額で「合計…になる」。to repair ... は cost を説明する不定詞。",
    ),
    make_question(
        12,
        "A: Tina, have you ( ) what you’re going to wear for Helen’s wedding?\nB: Yes. I’ve got quite a few nice dresses, but I’m going to wear the pink one that I bought at the New Year’s sale.",
        "A：ティナ、ヘレンの結婚式に何を着るか（　）？\nB：うん。素敵なドレスがかなりあるけれど、新年セールで買ったピンクのを着るつもり。",
        ["called up", "picked out", "occurred to", "disposed of"],
        ["電話した", "選び出した", "ふと思い付いた", "処分した"], 2,
        ["what 以下を電話する、とはならない。", "pink one を着ると決めたので、服を選び出した。", "occur to は「考えが人に浮かぶ」で、人を主語にこの形では使わない。", "何を着るかを処分する、とはならない。"],
        "pick out + 疑問詞節で「何を…するか選ぶ」。the one that ... の that 節が one を修飾する。",
    ),
    make_question(
        13,
        "The current president of Baxter’s Boxes is Mike Baxter. His business was ( ) his father, Peter, who retired 15 years ago.",
        "バクスターズ・ボクシズの現在の社長はマイク・バクスターだ。彼の事業は15年前に引退した父ピーターから（　）ものだ。",
        ["balanced on", "opposed to", "inherited from", "prohibited by"],
        ["…の上で均衡を取った", "…に反対した", "…から受け継いだ", "…に禁止された"], 3,
        ["事業が父の上で均衡する、とはならない。", "事業が父に反対する意味ではない。", "父から事業を受け継いだ、という継承関係。", "父が事業を禁止したとは書かれていない。"],
        "inherit A from B は「AをBから受け継ぐ」。was inherited は受動態。who は Peter を説明する。",
    ),
    make_question(
        14,
        "Neil tries to keep his work ( ) his private life. He does not like to mix them, so he never takes work home or talks about his family with his colleagues.",
        "ニールは仕事を私生活から（　）保とうとしている。両者を混ぜたくないので、仕事を家に持ち帰らず、同僚に家族の話もしない。",
        ["separate from", "familiar with", "anxious for", "equal to"],
        ["…から分けて", "…に詳しい", "…を切望して", "…と等しい"], 1,
        ["does not like to mix them が「分けておく」の根拠。", "仕事が私生活に詳しい、とはならない。", "仕事が私生活を切望する意味ではない。", "仕事と私生活を同一量にする話ではない。"],
        "keep A separate from B は「AをBから分けておく」。them は work と private life を指す。",
    ),
    make_question(
        15,
        "In the heavy rain, the ship’s crew members were ( ) of the weather. They had to wait for the storm to pass before they could start the engines safely.",
        "激しい雨の中、船員たちは天候の（　）だった。安全にエンジンを始動できるまで、嵐が過ぎるのを待たなければならなかった。",
        ["at the mercy", "on the point", "in the hope", "off the record"],
        ["なすがままに", "まさに…しようとして", "…を望んで", "非公式に"], 1,
        ["嵐が過ぎるまで行動できず、天候に左右されている。", "on the point of doing の形ではなく、意味も合わない。", "in the hope of doing の形ではなく、単なる希望の話ではない。", "非公式発言を表す表現で天候と結ばない。"],
        "at the mercy of ... は「…のなすがままに」。before S could ... は「Sが…できる前に」。",
    ),
    make_question(
        16,
        "The British TV drama Coronation Street first went ( ) in 1960. It has remained popular ever since, and in 2020, its 10,000th episode was broadcast.",
        "英国のテレビドラマ『Coronation Street』は1960年に初めて（　）になった。それ以来人気が続き、2020年には第1万話が放送された。",
        ["in a bit", "for a change", "at the rate", "on the air"],
        ["少ししたら", "気分を変えて", "その割合で", "放送されて"], 4,
        ["開始時刻を表す句ではない。", "いつもと違うことをする意味で放送開始を表さない。", "速度・割合を表す句で went と結ばない。", "go on the air で「放送が始まる」。broadcast が言い換え。"],
        "go on the air は「放送を開始する」。has remained ... ever since は過去から現在までの継続。",
    ),
    make_question(
        17,
        "A: Excuse me. I’m looking for an electric heater for my kitchen.\nB: I recommend this one, ma’am. It’s small, but it ( ) plenty of heat. It should warm your kitchen in just a few minutes.",
        "A：すみません。台所用の電気ヒーターを探しています。\nB：こちらがおすすめです。小さいですが、熱をたっぷり（　）。数分で台所が暖まるはずです。",
        ["drops out", "runs out", "gives off", "keeps off"],
        ["脱落する", "なくなる", "放出する", "近づけない"], 3,
        ["ヒーターが脱落する話ではない。", "run out は自動詞句なので plenty of heat を直接目的語に取れない。run out of heat なら「熱源が尽きる」。", "give off heat で「熱を放出する」。", "keep off heat は熱を遠ざける意味になり、用途と反対。"],
        "give off + 熱・光・においで「…を放出する」。should はここでは高い見込みを表す。",
    ),
    make_question(
        18,
        "A: I can’t help ( ) these peanuts. They’re so delicious!\nB: I know. Once you start, it’s very, very difficult to stop.",
        "A：このピーナツを（　）ずにはいられない。とてもおいしい！\nB：分かるよ。一度始めると、やめるのは本当に難しいね。",
        ["eating", "to eat", "eat", "eaten"],
        ["食べること", "食べるために", "食べる", "食べられた"], 1,
        ["cannot help doing で「…せずにはいられない」。", "cannot help の後に to不定詞は置かない。", "動詞原形では定型構文にならない。", "過去分詞は目的語 these peanuts を取れない。"],
        "cannot help doing は「…せずにはいられない」。Once S V は「いったんSがVすると」。",
    ),
    make_question(
        19,
        "A: What do you think of these cups in the shape of animals?\nB: They’re so cute! I need to get a present for my sister’s birthday, and one of those cups would be the ( ) thing.",
        "A：動物の形をしたこのカップ、どう思う？\nB：とてもかわいい！ 姉か妹の誕生日プレゼントが必要だから、そのうち一つがまさに（　）ものだね。",
        ["ever", "much", "very", "so"],
        ["これまで", "多く", "まさにその", "とても"], 3,
        ["the ever thing という形にはならない。", "the much thing では名詞を修飾できない。", "the very thing で「まさにそのもの」。", "the so thing という語順にはならない。"],
        "the very + 名詞は「まさにその…」。in the shape of ... は「…の形をした」。",
    ),
    make_question(
        20,
        "The members of the band Rockhammer were looking forward to playing with their new guitarist. However, she did not arrive ( ) the concert was over.",
        "バンド、ロックハンマーのメンバーは新しいギタリストとの演奏を楽しみにしていた。しかし彼女はコンサートが終わる（　）到着しなかった。",
        ["unless", "whether", "until", "yet"],
        ["…でない限り", "…かどうか", "…まで", "まだ"], 3,
        ["条件を表すと「コンサートが終わらない限り」となり不自然。", "選択・不確実性を導く位置ではない。", "not ... until で「…するまで～しない／…して初めて～した」。", "yet は接続詞としてこの節を導けない。"],
        "not ... until S V は「SがVするまで…しない」、文脈では「終演して初めて到着した」。",
    ),
]


def sp(en, ja, verb=""):
    """Sentence-popup entry: English, Japanese, slash guide, main verb."""
    return [en, ja, f"{en}|{ja}", verb]


passage_2a_paragraphs = [
    "The tale of Johnny Appleseed is an American legend. According to the story, Appleseed’s dream was to grow enough apples for everybody to have plenty to eat. He traveled all across the United States, planting apple trees on the way. Much of this story is fiction. However, Johnny Appleseed ( 21 ). This was a man called John Chapman, who was born in the northeastern state of Massachusetts in 1774.",
    "At the time, many people in the eastern United States were moving west to find cheap land. Chapman saw this as a ( 22 ). He got free bags of apple seeds from producers of cider, an alcoholic drink made from apples. As he traveled around, he bought land and planted apple trees in places that would likely become towns. Later, he would return to these places to check his apple trees and sell them. Sometimes, he also sold his land to people who wanted to settle there.",
    "Chapman became popular with the people that he visited on his travels. He would bring them news from far away and tell them stories from his interesting life. Also, it seems that he was a kind person. If someone paid for his apple trees with clothes, he would then give these clothes to people who needed them more than he did. He was happy to wear a jacket made from an old cloth bag, and he rarely wore shoes, even in winter. The story of Johnny Appleseed is mainly a legend. ( 23 ), though, it contains a few seeds of truth taken from Chapman’s life.",
]
passage_2a_translations = [
    "ジョニー・アップルシードの物語はアメリカの伝説である。物語によれば、皆が十分に食べられるほど多くのリンゴを育てることが彼の夢だった。彼は米国中を旅し、道々リンゴの木を植えた。物語の多くは創作である。しかし、ジョニー・アップルシードは（21）。それが、1774年に北東部マサチューセッツ州で生まれたジョン・チャップマンという男性だった。",
    "当時、米国東部の多くの人が安い土地を求めて西へ移動していた。チャップマンはこれを（22）と考えた。彼はシードル（リンゴから作る酒）の生産者から、リンゴの種が入った袋を無料でもらった。各地を旅しながら土地を買い、町になりそうな場所にリンゴの木を植えた。後に戻って木を確認して売り、ときには定住希望者に土地も売った。",
    "チャップマンは旅先の人々に人気があった。遠方の知らせや自分の興味深い人生の話を伝えた。また親切な人だったようだ。木の代金を服で払う人がいると、自分より必要な人へその服を与えた。古い布袋で作った上着を喜んで着て、冬でさえ靴をめったに履かなかった。ジョニー・アップルシードの物語は主に伝説である。しかし（23）、チャップマンの人生から取られた真実の種も少し含まれる。",
]
passage_2a_pairs = [
    sp("The tale of Johnny Appleseed is an American legend.", "ジョニー・アップルシードの物語はアメリカの伝説である。", "is"),
    sp("According to the story, Appleseed’s dream was to grow enough apples for everybody to have plenty to eat.", "物語によれば、皆が十分に食べられるほど多くのリンゴを育てることが彼の夢だった。", "was"),
    sp("He traveled all across the United States, planting apple trees on the way.", "彼は米国中を旅し、道々リンゴの木を植えた。", "traveled"),
    sp("Much of this story is fiction.", "この物語の多くは創作である。", "is"),
    sp("However, Johnny Appleseed ( 21 ).", "しかし、ジョニー・アップルシードは（21）。", ""),
    sp("This was a man called John Chapman, who was born in the northeastern state of Massachusetts in 1774.", "それが、1774年に北東部マサチューセッツ州で生まれたジョン・チャップマンという男性だった。", "was"),
    sp("At the time, many people in the eastern United States were moving west to find cheap land.", "当時、米国東部の多くの人が安い土地を求めて西へ移動していた。", "were moving"),
    sp("Chapman saw this as a ( 22 ).", "チャップマンはこれを（22）と考えた。", "saw"),
    sp("He got free bags of apple seeds from producers of cider, an alcoholic drink made from apples.", "彼はシードル（リンゴから作る酒）の生産者から、リンゴの種が入った袋を無料でもらった。", "got"),
    sp("As he traveled around, he bought land and planted apple trees in places that would likely become towns.", "各地を旅しながら土地を買い、町になりそうな場所にリンゴの木を植えた。", "bought / planted"),
    sp("Later, he would return to these places to check his apple trees and sell them.", "後に彼はその場所へ戻り、木を確認して売った。", "would return"),
    sp("Sometimes, he also sold his land to people who wanted to settle there.", "ときには、そこへ定住したい人々に土地も売った。", "sold"),
    sp("Chapman became popular with the people that he visited on his travels.", "チャップマンは旅先で訪ねた人々に人気があった。", "became"),
    sp("He would bring them news from far away and tell them stories from his interesting life.", "遠方の知らせや自分の興味深い人生の話を人々に伝えた。", "would bring / tell"),
    sp("Also, it seems that he was a kind person.", "また、彼は親切な人だったようだ。", "seems"),
    sp("If someone paid for his apple trees with clothes, he would then give these clothes to people who needed them more than he did.", "木の代金を服で払う人がいると、自分より必要な人へその服を与えた。", "would give"),
    sp("He was happy to wear a jacket made from an old cloth bag, and he rarely wore shoes, even in winter.", "彼は古い布袋で作った上着を喜んで着て、冬でさえ靴をめったに履かなかった。", "was / wore"),
    sp("The story of Johnny Appleseed is mainly a legend.", "ジョニー・アップルシードの物語は主に伝説である。", "is"),
    sp("( 23 ), though, it contains a few seeds of truth taken from Chapman’s life.", "しかし（23）、チャップマンの人生から取られた真実の種も少し含まれる。", "contains"),
]
passage_2a = {
    "label": "A", "title": "Johnny Appleseed",
    "paragraphs": passage_2a_paragraphs, "translations": passage_2a_translations,
    "sentencePairs": passage_2a_pairs,
    "questions": [
        make_question(21, None, None,
            ["has appeared in several movies", "has been given a new image", "was based on a real person", "was created by an apple farm"],
            ["いくつかの映画に登場した", "新しいイメージを与えられた", "実在の人物に基づいていた", "リンゴ農園によって作られた"], 3,
            ["映画への登場は述べられていない。", "イメージを変えた話ではない。", "直後に実在の John Chapman が紹介される。", "物語を農園が作ったとは書かれていない。"],
            "be based on ... は「…に基づく」。受動態 was based が伝説と実在人物の関係を示す。",
            source_evidence=["This was a man called John Chapman"]),
        make_question(22, None, None,
            ["reason to celebrate", "normal reaction", "serious mistake", "chance to make money"],
            ["祝う理由", "普通の反応", "重大な間違い", "金を稼ぐ機会"], 4,
            ["祝賀の話ではない。", "西への移動に反応しただけではなく事業を行った。", "土地購入を誤りと見る記述はない。", "町になりそうな土地で木や土地を売ったので商機だった。"],
            "see A as B は「AをBと見る」。chance to do は「…する機会」。",
            source_evidence=["he bought land and planted apple trees in places that would likely become towns", "he also sold his land"]),
        make_question(23, None, None,
            ["In response", "At least", "On average", "With luck"],
            ["それに応じて", "少なくとも", "平均して", "運がよければ"], 2,
            ["何かへの応答を示す位置ではない。", "主に伝説だが、少なくとも一部は真実という譲歩に合う。", "数量の平均を述べていない。", "幸運なら真実になる、という条件ではない。"],
            "At least は最低限認められる点を示す。though と組み譲歩の流れを作る。",
            source_evidence=["it contains a few seeds of truth taken from Chapman’s life"]),
    ],
}


passage_2b_paragraphs = [
    "Life on large sailing ships was hard. Sailors could be away from their homes and families for months or even years. The food they had to eat was often dried and in bad condition. The work that the sailors had to do on a ship was usually boring and physically tiring. ( 24 ), the sea itself was a very dangerous place, especially during storms, and accidents were common. It is not surprising that sailors started to make and sing their own songs to stay cheerful.",
    "These songs, called “sea shanties,” come in two varieties. “Capstan shanties” were used for work that needed a regular pace without stopping, such as raising the ship’s anchor. “Pulling shanties” were used when the sailors pulled ropes to raise the sails. They sang these shanties as they worked together for a few seconds, stopped to take a breath, and then started again. During these shanties, one of the sailors, known as the “shantyman,” would sing out a line. The other sailors would all sing the next line together. This helped them to ( 25 ).",
    "After the invention of steamships, sailors no longer had to work together in teams. The ships’ engines did all the hard work. Even so, sea shanties have remained popular. One reason is that their words are often based on funny stories. There are groups all over the world who get together to sing these amusing songs. Some people even write new ones. Like the sea shanties of the past, new ones also ( 26 ).",
]
passage_2b_translations = [
    "大型帆船での生活は厳しかった。船員は数か月、時には何年も家や家族を離れた。食料は乾燥させたもので、状態も悪いことが多く、仕事はたいてい退屈で肉体的に疲れるものだった。（24）、海自体も、特に嵐のときは非常に危険で事故が多かった。船員が陽気でいるため自分たちの歌を作って歌い始めたのも不思議ではない。",
    "「シー・シャンティ」と呼ばれる歌には二種類ある。「キャプスタン・シャンティ」は、いかりを上げるなど一定の速さで止まらず行う仕事に使われた。「プリング・シャンティ」は帆を上げるため綱を引くときに使われた。数秒間一緒に働きながら歌い、息をついて再開した。シャンティマンが一節を歌い、他の船員が次の一節を一緒に歌った。これが（25）のに役立った。",
    "蒸気船の発明後、船員はチームで働く必要がなくなり、エンジンが重労働を担った。それでもシー・シャンティは現在まで人気を保っている。歌詞が面白い話に基づくことが理由の一つである。世界中に集まって歌う団体があり、新曲を書く人もいる。昔の歌と同様、新しい歌も（26）。",
]
passage_2b_pairs = [
    sp("Life on large sailing ships was hard.", "大型帆船での生活は厳しかった。", "was"),
    sp("Sailors could be away from their homes and families for months or even years.", "船員は数か月、時には何年も家や家族を離れることがあった。", "could be"),
    sp("The food they had to eat was often dried and in bad condition.", "食べなければならない食料は乾燥させたもので、状態も悪いことが多かった。", "was"),
    sp("The work that the sailors had to do on a ship was usually boring and physically tiring.", "船上の仕事はたいてい退屈で肉体的に疲れるものだった。", "was"),
    sp("( 24 ), the sea itself was a very dangerous place, especially during storms, and accidents were common.", "（24）、海自体も、特に嵐のときは非常に危険で事故が多かった。", "was / were"),
    sp("It is not surprising that sailors started to make and sing their own songs to stay cheerful.", "船員が陽気でいるため自分たちの歌を作って歌い始めたのも不思議ではない。", "is"),
    sp("These songs, called “sea shanties,” come in two varieties.", "「シー・シャンティ」と呼ばれる歌には二種類ある。", "come"),
    sp("“Capstan shanties” were used for work that needed a regular pace without stopping, such as raising the ship’s anchor.", "「キャプスタン・シャンティ」は、いかりを上げるなど一定の速さで止まらず行う仕事に使われた。", "were used"),
    sp("“Pulling shanties” were used when the sailors pulled ropes to raise the sails.", "「プリング・シャンティ」は帆を上げるため綱を引くときに使われた。", "were used"),
    sp("They sang these shanties as they worked together for a few seconds, stopped to take a breath, and then started again.", "数秒間一緒に働きながら歌い、息をついてから再開した。", "sang / stopped / started"),
    sp("During these shanties, one of the sailors, known as the “shantyman,” would sing out a line.", "歌の間、シャンティマンと呼ばれる船員の一人が一節を歌った。", "would sing"),
    sp("The other sailors would all sing the next line together.", "他の船員は皆で次の一節を歌った。", "would sing"),
    sp("This helped them to ( 25 ).", "これは彼らが（25）のに役立った。", "helped"),
    sp("After the invention of steamships, sailors no longer had to work together in teams.", "蒸気船の発明後、船員はチームで働く必要がなくなった。", "had to work"),
    sp("The ships’ engines did all the hard work.", "船のエンジンがすべての重労働を担った。", "did"),
    sp("Even so, sea shanties have remained popular.", "それでもシー・シャンティは人気を保っている。", "have remained"),
    sp("One reason is that their words are often based on funny stories.", "理由の一つは、歌詞が面白い話に基づくことだ。", "is / are based"),
    sp("There are groups all over the world who get together to sing these amusing songs.", "世界中に、集まってこの楽しい歌を歌う団体がある。", "are"),
    sp("Some people even write new ones.", "新しい歌を書く人さえいる。", "write"),
    sp("Like the sea shanties of the past, new ones also ( 26 ).", "昔のシー・シャンティと同様、新しい歌も（26）。", ""),
]
passage_2b = {
    "label": "B", "title": "Sea Shanties",
    "paragraphs": passage_2b_paragraphs, "translations": passage_2b_translations,
    "sentencePairs": passage_2b_pairs,
    "questions": [
        make_question(24, None, None,
            ["After a while", "In exchange", "To make matters worse", "For this reason"],
            ["しばらくして", "引き換えに", "さらに悪いことに", "この理由で"], 3,
            ["時間の経過を述べるのではない。", "交換の相手や内容がない。", "食事・仕事の厳しさに海の危険を加える。", "海の危険が前文の結果という因果ではない。"],
            "To make matters worse は「さらに悪いことに」。前の悪条件へ別の悪条件を追加する。",
            source_evidence=["the sea itself was a very dangerous place", "accidents were common"]),
        make_question(25, None, None,
            ["keep a steady rhythm", "learn how to build ships", "get to know one another", "scare sharks away"],
            ["一定のリズムを保つ", "船の造り方を学ぶ", "互いを知る", "サメを追い払う"], 1,
            ["交互に同じテンポで歌うことで共同作業のリズムを保てる。", "造船技術を教える歌ではない。", "交流より作業の歩調を合わせる目的。", "サメについての記述はない。"],
            "help 人 to do は「人が…するのを助ける」。steady は「一定した」。",
            source_evidence=["needed a regular pace without stopping", "The other sailors would all sing the next line together"]),
        make_question(26, None, None,
            ["have both men’s and women’s parts", "teach people how to sail", "usually contain a lot of humor", "rarely last more than a minute"],
            ["男性と女性両方のパートがある", "航海方法を教える", "たいてい多くのユーモアを含む", "一分を超えることはめったにない"], 3,
            ["男女の歌唱パートについて本文にない。", "航海の教則歌だとは書かれていない。", "古い歌も新しい歌も面白い話を歌詞にする流れ。", "歌の長さについての記述はない。"],
            "Like A, B also ... は「Aと同様、Bも…」。ones は sea shanties を受ける代名詞。",
            source_evidence=["their words are often based on funny stories", "Some people even write new ones"]),
    ],
}


passage_3a_paragraphs = [
    "Dear Alice,",
    "Thank you for signing up online for the eighth annual Gravelton Comic Show. This year’s show will be held at the convention center in Gravelton on Saturday, February 18, and it will be our biggest ever. There will be thousands of comic books on sale, including rare items and comic books by local creators, as well as T-shirts, posters, and other goods from your favorite comic books. You’ll also have the chance to meet and talk to some of the artists and writers who created them.",
    "As usual, we’ll be holding costume contests for visitors. One contest is for kids aged 12 or under, and the other is for everybody else. If you want to participate, please sign up at the reception desk by noon. Please note that your costume must have been made by you. People wearing costumes bought from a store will not be allowed to enter the contest. Be creative, and you might win a fantastic prize.",
    "We ask all visitors to respect one another. Please do not touch other people’s costumes or take photos of them without getting permission first. Also, please remember that eating and drinking are not allowed in the main hall of the convention center. In addition to the convention center’s cafeteria, there will also be food trucks selling snacks and drinks in the square outside the center.",
    "We look forward to seeing you at the show!",
    "Gravelton Comic Show Staff",
]
passage_3a_translations = [
    "アリス様",
    "第8回グラベルトン・コミックショーにオンラインでお申し込みいただき、ありがとうございます。今年は2月18日土曜日にグラベルトンのコンベンションセンターで開催され、過去最大となります。珍しい品や地元作家の作品を含む何千冊ものコミックに加え、お気に入りのコミックにちなんだTシャツ、ポスター、その他のグッズが販売されます。作品を作った画家や作家と会って話す機会もあります。",
    "例年どおり来場者向け仮装コンテストを行います。一つは12歳以下、もう一つはそれ以外の全員が対象です。参加する場合は正午までに受付で申し込んでください。衣装は自作でなければなりません。店で買った衣装では参加できません。創意工夫を凝らせば、すばらしい賞品を得られるかもしれません。",
    "来場者全員に、互いを尊重するようお願いします。許可を得ずに他人の衣装へ触れたり写真を撮ったりしないでください。また、会場の大ホールでは飲食できません。館内食堂に加え、外の広場には軽食や飲み物を売るフードトラックも出ます。",
    "会場でお会いできることを楽しみにしています！",
    "グラベルトン・コミックショー運営スタッフ",
]
passage_3a_pairs = [
    sp("Thank you for signing up online for the eighth annual Gravelton Comic Show.", "第8回グラベルトン・コミックショーにオンラインでお申し込みいただき、ありがとうございます。", "Thank"),
    sp("This year’s show will be held at the convention center in Gravelton on Saturday, February 18, and it will be our biggest ever.", "今年は2月18日土曜日にグラベルトンのコンベンションセンターで開催され、過去最大となる。", "will be held / will be"),
    sp("There will be thousands of comic books on sale, including rare items and comic books by local creators, as well as T-shirts, posters, and other goods from your favorite comic books.", "珍しい品や地元作家の作品を含む何千冊ものコミックに加え、お気に入りのコミックにちなんだTシャツ、ポスター、その他のグッズも販売される。", "will be"),
    sp("You’ll also have the chance to meet and talk to some of the artists and writers who created them.", "作品を作った画家や作家と会って話す機会もある。", "will have"),
    sp("As usual, we’ll be holding costume contests for visitors.", "例年どおり来場者向け仮装コンテストを行う。", "will be holding"),
    sp("One contest is for kids aged 12 or under, and the other is for everybody else.", "一つは12歳以下、もう一つはそれ以外の全員が対象である。", "is"),
    sp("If you want to participate, please sign up at the reception desk by noon.", "参加する場合は正午までに受付で申し込んでほしい。", "want / sign up"),
    sp("Please note that your costume must have been made by you.", "衣装は自作でなければならないことに注意してほしい。", "must have been made"),
    sp("People wearing costumes bought from a store will not be allowed to enter the contest.", "店で買った衣装を着た人はコンテストに参加できない。", "will be allowed"),
    sp("Be creative, and you might win a fantastic prize.", "創意工夫を凝らせば、すばらしい賞品を得られるかもしれない。", "Be / might win"),
    sp("We ask all visitors to respect one another.", "来場者全員に互いを尊重するようお願いする。", "ask"),
    sp("Please do not touch other people’s costumes or take photos of them without getting permission first.", "許可を得ずに他人の衣装へ触れたり写真を撮ったりしないでほしい。", "touch / take"),
    sp("Also, please remember that eating and drinking are not allowed in the main hall of the convention center.", "また、会場の大ホールでは飲食できないことを覚えておいてほしい。", "remember / are allowed"),
    sp("In addition to the convention center’s cafeteria, there will also be food trucks selling snacks and drinks in the square outside the center.", "館内食堂に加え、外の広場には軽食や飲み物を売るフードトラックも出る。", "will be"),
    sp("We look forward to seeing you at the show!", "会場でお会いできることを楽しみにしている。", "look forward"),
]
passage_3a = {
    "label": "A", "title": "Thank you for signing up", "format": "email",
    "meta": {
        "from": "Gravelton Comic Show <info@graveltoncomicshow.com>",
        "to": "Alice Sullivan <alisulli321@friendlymail.com>",
        "date": "January 22", "subject": "Thank you for signing up",
    },
    "paragraphs": passage_3a_paragraphs, "translations": passage_3a_translations,
    "sentencePairs": passage_3a_pairs,
    "questions": [
        make_question(27, None, None,
            ["purchase comic books made by people from the Gravelton area.", "watch movies based on her favorite comic books.", "take lessons in how to create her own comic books.", "display her paintings of famous comic book characters."],
            ["グラベルトン地域の人が作ったコミックを購入する。", "お気に入りのコミックを原作とする映画を見る。", "自分のコミックの作り方を習う。", "有名キャラクターの絵を展示する。"], 1,
            ["local creators のコミックが販売されると明記されている。", "映画上映についての案内はない。", "制作講座についての案内はない。", "来場者の絵を展示する案内はない。"],
            "be able to do は「…できる」。comic books by local creators の by は作者を表す。",
            question="At the Gravelton Comic Show, Alice will be able to",
            question_translation="グラベルトン・コミックショーで、アリスができることは",
            source_evidence=["comic books by local creators"]),
        make_question(28, None, None,
            ["Make their costumes themselves.", "Sign up before coming to the show.", "Pay an entry fee at the reception desk.", "Explain why they chose their costumes."],
            ["衣装を自分で作る。", "来場前に申し込む。", "受付で参加料を払う。", "衣装を選んだ理由を説明する。"], 1,
            ["costume must have been made by you が条件。", "申込期限は当日正午で、来場前とは書かれていない。", "参加料についての記述はない。", "選択理由の説明は求められていない。"],
            "must have been made は must + 完了形の受動態。「すでに自分で作られたものでなければならない」。",
            question="What is one thing that participants in the costume contest need to do?",
            question_translation="仮装コンテストの参加者がしなければならないことの一つは何ですか。",
            source_evidence=["your costume must have been made by you"]),
        make_question(29, None, None,
            ["eat in the main hall of the convention center.", "use the parking lot in the square outside the center.", "take a picture of another visitor’s costume.", "bring their own snacks and drinks to the show."],
            ["会場の大ホールで食べる。", "会場外の広場にある駐車場を使う。", "別の来場者の衣装を撮影する。", "軽食や飲み物を持参する。"], 3,
            ["大ホールでの飲食は禁止されており、許可を求める話ではない。", "駐車場についての記述はない。", "他人の衣装を撮影する前に permission が必要。", "飲食物の持参許可についての記述はない。"],
            "without doing は「…せずに」。ask to be allowed to do は「…する許可を求める」。",
            question="Visitors to the Gravelton Comic Show must ask to be allowed to",
            question_translation="グラベルトン・コミックショーの来場者が許可を求めなければならないのは",
            source_evidence=["take photos of them without getting permission first"]),
    ],
}


passage_3b_paragraphs = [
    "For thousands of years, the Guadalhorce river has flowed through the mountains of southern Spain. Over time, it has created an impressive narrow valley with high rock walls that are 300 meters above the river in some places. At the beginning of the 20th century, engineers decided that the fast-flowing river was a good place for a dam that could be used to generate electricity. A one-meter-wide concrete walkway was built high up on the walls of the valley for people to reach the dam from a nearby town.",
    "To begin with, the walkway was only used by workers at the power plant and local people who wanted to get to the other side of the mountains. Soon, news of the walkway’s amazing views spread, and it became popular with hikers. The engineers decided to improve the walkway to make it more attractive to tourists, and in 1921, it was officially opened by King Alfonso XIII of Spain. After the ceremony, the king walked the eight-kilometer route, and it became known as El Caminito del Rey, meaning “the king’s little path.”",
    "Despite its popularity, the walkway was not well looked after. Holes appeared in places where the concrete had been damaged. Originally, there was a metal fence on one side of the walkway to stop people from falling, but this broke and fell to the bottom of the valley. El Caminito del Rey became famous as the most dangerous hiking path in the world, and people from many countries came for the excitement of walking along it. However, after four deaths in two years, the government decided to close the walkway in 2001.",
    "Interest in El Caminito del Rey remained, and 2.2 million euros were spent on rebuilding the walkway with wood and steel. The new walkway was opened in 2015, and although it is safer than the old one, some people still find it frightening. Despite this, the dramatic scenery attracts many visitors. To keep El Caminito del Rey in good condition for as long as possible, hikers must now buy tickets to use it, and only 300,000 tickets are available each year.",
]
passage_3b_translations = [
    "グアダルオルセ川は何千年もの間、スペイン南部の山々を流れてきた。長い時間をかけ、場所によって川面から300メートルに達する高い岩壁を持つ印象的な狭い谷を作った。20世紀初め、技師たちは流れの速い川が発電用ダムに適した場所だと考えた。近隣の町からダムへ行けるよう、谷の壁面高くに幅1メートルのコンクリート歩道が造られた。",
    "当初、歩道を使うのは発電所の作業員と山の反対側へ行く地元住民だけだった。やがて眺望の評判が広まり、ハイカーに人気となった。技師たちは、観光客にとってより魅力的にするため歩道を改良することを決め、1921年にスペイン国王アルフォンソ13世が正式に開通させた。式典後に国王が8キロの道を歩いたため、「王の小道」を意味するエル・カミニート・デル・レイと呼ばれるようになった。",
    "人気にもかかわらず歩道は十分に管理されず、コンクリートが傷んだ場所には穴が開いた。転落防止用の金属柵も壊れて谷底へ落ちた。世界一危険なハイキング道として有名になり、刺激を求めて各国から人が来た。しかし2年間に4人が死亡した後、政府は2001年に閉鎖を決めた。",
    "関心は残り、木と鋼での再建に220万ユーロが使われた。2015年に開通した新歩道は以前より安全だが、今も怖いと感じる人がいる。それでも壮大な景観が多くの来訪者を引き付ける。長く良好な状態を保つため、利用にはチケットが必要で、年間30万枚だけが販売される。",
]
passage_3b_pairs = [
    sp("For thousands of years, the Guadalhorce river has flowed through the mountains of southern Spain.", "グアダルオルセ川は何千年もの間、スペイン南部の山々を流れてきた。", "has flowed"),
    sp("Over time, it has created an impressive narrow valley with high rock walls that are 300 meters above the river in some places.", "長い時間をかけ、場所によって川面から300メートルに達する高い岩壁を持つ狭い谷を作った。", "has created"),
    sp("At the beginning of the 20th century, engineers decided that the fast-flowing river was a good place for a dam that could be used to generate electricity.", "20世紀初め、技師たちは流れの速い川が発電用ダムに適した場所だと考えた。", "decided"),
    sp("A one-meter-wide concrete walkway was built high up on the walls of the valley for people to reach the dam from a nearby town.", "近隣の町からダムへ行けるよう、谷の壁面高くに幅1メートルのコンクリート歩道が造られた。", "was built"),
    sp("To begin with, the walkway was only used by workers at the power plant and local people who wanted to get to the other side of the mountains.", "当初、歩道を使うのは発電所の作業員と山の反対側へ行く地元住民だけだった。", "was used"),
    sp("Soon, news of the walkway’s amazing views spread, and it became popular with hikers.", "やがて眺望の評判が広まり、ハイカーに人気となった。", "spread / became"),
    sp("The engineers decided to improve the walkway to make it more attractive to tourists, and in 1921, it was officially opened by King Alfonso XIII of Spain.", "技師たちは、観光客にとってより魅力的にするため歩道を改良することを決め、1921年にスペイン国王アルフォンソ13世が正式に開通させた。", "decided / was opened"),
    sp("After the ceremony, the king walked the eight-kilometer route, and it became known as El Caminito del Rey, meaning “the king’s little path.”", "式典後に国王が8キロの道を歩き、「王の小道」を意味するエル・カミニート・デル・レイと呼ばれるようになった。", "walked / became"),
    sp("Despite its popularity, the walkway was not well looked after.", "人気にもかかわらず、歩道は十分に管理されなかった。", "was looked after"),
    sp("Holes appeared in places where the concrete had been damaged.", "コンクリートが傷んだ場所には穴が開いた。", "appeared"),
    sp("Originally, there was a metal fence on one side of the walkway to stop people from falling, but this broke and fell to the bottom of the valley.", "当初は転落防止用の金属柵が片側にあったが、壊れて谷底へ落ちた。", "was / broke / fell"),
    sp("El Caminito del Rey became famous as the most dangerous hiking path in the world, and people from many countries came for the excitement of walking along it.", "世界一危険なハイキング道として有名になり、刺激を求めて各国から人が来た。", "became / came"),
    sp("However, after four deaths in two years, the government decided to close the walkway in 2001.", "しかし2年間に4人が死亡した後、政府は2001年に閉鎖を決めた。", "decided"),
    sp("Interest in El Caminito del Rey remained, and 2.2 million euros were spent on rebuilding the walkway with wood and steel.", "関心は残り、木と鋼での再建に220万ユーロが使われた。", "remained / were spent"),
    sp("The new walkway was opened in 2015, and although it is safer than the old one, some people still find it frightening.", "2015年に開通した新歩道は以前より安全だが、今も怖いと感じる人がいる。", "was opened / find"),
    sp("Despite this, the dramatic scenery attracts many visitors.", "それでも壮大な景観が多くの来訪者を引き付ける。", "attracts"),
    sp("To keep El Caminito del Rey in good condition for as long as possible, hikers must now buy tickets to use it, and only 300,000 tickets are available each year.", "長く良好な状態を保つため、利用にはチケットが必要で、年間30万枚だけが販売される。", "must buy / are available"),
]
passage_3b = {
    "label": "B", "title": "The King’s Little Path",
    "paragraphs": passage_3b_paragraphs, "translations": passage_3b_translations,
    "sentencePairs": passage_3b_pairs,
    "questions": [
        make_question(30, None, None,
            ["the river was too dangerous for boats to travel on.", "a lower walkway had been destroyed by a sudden flood.", "there were rocks in the valley that made it difficult to walk.", "people needed it to get to a newly constructed dam."],
            ["川は船が進むには危険すぎた。", "低い歩道が突然の洪水で壊されていた。", "谷の岩で歩くのが難しかった。", "新設ダムへ行くため必要だった。"], 4,
            ["船での移動についての記述はない。", "以前の低い歩道や洪水についての記述はない。", "谷底を歩く困難が建設理由ではない。", "nearby town から dam へ到達するため造られた。"],
            "for 人 to do は「人が…するために」。too ... to do は選択肢1で「…すぎてできない」。",
            question="A walkway was built high up on the walls of the Guadalhorce river valley because",
            question_translation="グアダルオルセ川の谷の壁面高くに歩道が造られたのは、",
            source_evidence=["for people to reach the dam from a nearby town"]),
        make_question(31, None, None,
            ["Because the king of Spain walked along it after he opened it.", "Because of the uniforms worn by the engineers who built it.", "Because of the amazing views that could be seen from it.", "Because local people wanted it to be attractive to tourists."],
            ["スペイン国王が正式に開通させた後、その道を歩いたから。", "建設した技師の制服に由来するから。", "歩道から見える眺望に由来するから。", "地元住民が観光客向けにしたかったから。"], 1,
            ["国王が式典後に道を歩き、「王の小道」と呼ばれた。", "技師の制服についての記述はない。", "景色は人気の理由だが名称の由来ではない。", "観光客向けの改良を決めたのは技師で、名称理由でもない。"],
            "become known as ... は「…として知られるようになる」。meaning ... は名称の意味を補足する分詞。",
            question="Why was the walkway called El Caminito del Rey?",
            question_translation="歩道がエル・カミニート・デル・レイと呼ばれたのはなぜですか。",
            source_evidence=["it was officially opened by King Alfonso XIII of Spain", "the king walked the eight-kilometer route", "meaning “the king’s little path.”"]),
        make_question(32, None, None,
            ["following the discovery of holes in the concrete.", "following accidents in which people died.", "after a metal fence fell onto it.", "after the cost of looking after it increased."],
            ["コンクリートの穴が見つかった後。", "死亡事故が起きた後。", "金属柵が歩道上に落ちた後。", "維持費が増えた後。"], 2,
            ["穴だけで閉鎖を決めたとは書かれていない。", "2年間に4人が死亡した後、政府が閉鎖を決めた。", "柵は歩道上でなく谷底へ落ちた。", "維持費増加についての記述はない。"],
            "following は前置詞で「…に続いて、…の後」。in which は accidents を説明する関係表現。",
            question="A decision was made to close the walkway",
            question_translation="歩道を閉鎖する決定がなされたのは、",
            source_evidence=["after four deaths in two years, the government decided to close the walkway"]),
        make_question(33, None, None,
            ["People have to wear special hiking boots when they use it.", "A roof has been added to prevent damage caused by rain.", "The surface of the walkway is made from a new material.", "The number of people who can hike on it has been limited."],
            ["利用時に特別な登山靴を履く。", "雨害防止の屋根が追加された。", "歩道面が新素材で作られている。", "歩ける人数が制限された。"], 4,
            ["特別な靴の規則はない。", "屋根についての記述はない。", "木と鋼で再建したが、表面の新素材を保護策とはしていない。", "年間チケットを30万枚に限定して利用者数を制限している。"],
            "the number of + 複数名詞は単数扱い。has been limited は現在完了の受動態。",
            question="What is one way in which the new walkway is being protected?",
            question_translation="新しい歩道を保護する方法の一つは何ですか。",
            source_evidence=["only 300,000 tickets are available each year"]),
    ],
}


passage_3c_paragraphs = [
    "Laughter is not only a way to express our feeling that something is funny, but it is also something that is good for our health. In the short term, it can help to relax muscles and improve blood flow, and in the long term, it can make our bodies better at fighting diseases. Researchers have been investigating how laughter evolved in humans by looking for similar behavior in other animals. A study carried out at the University of California, Los Angeles, has revealed evidence of laughter-like behavior in over 60 species.",
    "It has long been known that chimpanzees laugh, although the sound is a little different from human laughter. When most humans laugh, they only make a noise when they breathe out, but when chimpanzees laugh, they make a noise both when they breathe out and when they breathe in. Chimpanzees are closely related to humans, so it is not really surprising that they, gorillas, and orangutans laugh. However, as these animals do not have the complicated languages needed to tell jokes, the researchers were interested to find out what makes them laugh.",
    "The researchers found that chimpanzees made these laughing noises when they were playing roughly with each other. They believe that laughter is a chimpanzee’s way of letting others know that it is not really trying to harm them. Playing allows chimpanzees and other animals to develop fighting and hunting skills as well as to build stronger relationships with the other members of their groups.",
    "By listening for the noises made by other animals during play behavior, the researchers were able to identify “laughter” in a wide range of animals. Dogs, for example, breathe loudly when they play, and dolphins make special clicking noises. In the case of rats, the laughter-like sounds they make when they are touched gently are too high for humans to hear. However, the sounds can be detected with special equipment. The researchers have concluded that laughter began to evolve as a signal to others that they can relax and have fun. Of course, humans laugh for a variety of reasons, so researchers still have much to learn about how this behavior evolved.",
]
passage_3c_translations = [
    "笑いは面白いという気持ちを表す方法だけでなく、健康にもよい。短期的には筋肉をほぐし血流を改善し、長期的には病気と闘う力を高める。研究者は、ほかの動物に見られる同様の行動を探すことで、人間の笑いがどのように進化したかを調べている。カリフォルニア大学ロサンゼルス校の研究は、60を超える種で笑いに似た行動の証拠を示した。",
    "チンパンジーが笑うことは以前から知られているが、人間とは少し音が違う。ほとんどの人間は息を吐くときだけ音を出すが、チンパンジーは吐くときにも吸うときにも音を出す。チンパンジーは人間に近縁であり、チンパンジーやゴリラ、オランウータンが笑うことは、それほど意外ではない。ただし冗談を言う複雑な言語を持たないため、研究者は何が笑わせるのかに関心を持った。",
    "研究者は、チンパンジーが互いに荒っぽく遊ぶとき笑い声を出すと分かった。笑いは、本気で傷つけようとしていないと相手に知らせる方法だと考えている。遊びによって闘争や狩りの技能を伸ばし、群れの仲間との関係も強められる。",
    "遊び中の動物の音を聞くことで、研究者は広範な動物の「笑い」を特定できた。犬は遊ぶとき大きく息をし、イルカは特別なクリック音を出す。ネズミがやさしく触れられたとき出す笑いに似た音は、人には高すぎて聞こえないが、特殊装置で検出できる。研究者は、笑いは相手に安心して楽しめると伝える合図として進化し始めたと結論づけた。人間が笑う理由は多様なので、その進化にはまだ学ぶことが多い。",
]
passage_3c_pairs = [
    sp("Laughter is not only a way to express our feeling that something is funny, but it is also something that is good for our health.", "笑いは面白いという気持ちを表す方法だけでなく、健康にもよい。", "is"),
    sp("In the short term, it can help to relax muscles and improve blood flow, and in the long term, it can make our bodies better at fighting diseases.", "短期的には筋肉をほぐし血流を改善し、長期的には病気と闘う力を高める。", "can help / can make"),
    sp("Researchers have been investigating how laughter evolved in humans by looking for similar behavior in other animals.", "研究者は、ほかの動物に見られる同様の行動を探すことで、人間の笑いがどのように進化したかを調べている。", "have been investigating"),
    sp("A study carried out at the University of California, Los Angeles, has revealed evidence of laughter-like behavior in over 60 species.", "カリフォルニア大学ロサンゼルス校の研究は、60を超える種で笑いに似た行動の証拠を示した。", "has revealed"),
    sp("It has long been known that chimpanzees laugh, although the sound is a little different from human laughter.", "チンパンジーが笑うことは以前から知られているが、人間とは少し音が違う。", "has been known / is"),
    sp("When most humans laugh, they only make a noise when they breathe out, but when chimpanzees laugh, they make a noise both when they breathe out and when they breathe in.", "ほとんどの人間は息を吐くときだけ音を出すが、チンパンジーは吐くときにも吸うときにも音を出す。", "make"),
    sp("Chimpanzees are closely related to humans, so it is not really surprising that they, gorillas, and orangutans laugh.", "チンパンジーは人間に近縁であり、チンパンジーやゴリラ、オランウータンが笑うことは、それほど意外ではない。", "are"),
    sp("However, as these animals do not have the complicated languages needed to tell jokes, the researchers were interested to find out what makes them laugh.", "ただし冗談を言う複雑な言語を持たないため、研究者は何が笑わせるのかに関心を持った。", "were interested"),
    sp("The researchers found that chimpanzees made these laughing noises when they were playing roughly with each other.", "研究者は、チンパンジーが互いに荒っぽく遊ぶとき笑い声を出すと分かった。", "found"),
    sp("They believe that laughter is a chimpanzee’s way of letting others know that it is not really trying to harm them.", "笑いは、本気で傷つけようとしていないと相手に知らせる方法だと考えている。", "believe"),
    sp("Playing allows chimpanzees and other animals to develop fighting and hunting skills as well as to build stronger relationships with the other members of their groups.", "遊びによって闘争や狩りの技能を伸ばし、群れの仲間との関係も強められる。", "allows"),
    sp("By listening for the noises made by other animals during play behavior, the researchers were able to identify “laughter” in a wide range of animals.", "遊び中の動物の音を聞くことで、研究者は広範な動物の「笑い」を特定できた。", "were able"),
    sp("Dogs, for example, breathe loudly when they play, and dolphins make special clicking noises.", "例えば犬は遊ぶとき大きく息をし、イルカは特別なクリック音を出す。", "breathe / make"),
    sp("In the case of rats, the laughter-like sounds they make when they are touched gently are too high for humans to hear.", "ネズミがやさしく触れられたとき出す笑いに似た音は、人には高すぎて聞こえない。", "are"),
    sp("However, the sounds can be detected with special equipment.", "しかし、その音は特殊装置で検出できる。", "can be detected"),
    sp("The researchers have concluded that laughter began to evolve as a signal to others that they can relax and have fun.", "研究者は、笑いは相手に安心して楽しめると伝える合図として進化し始めたと結論づけた。", "have concluded"),
    sp("Of course, humans laugh for a variety of reasons, so researchers still have much to learn about how this behavior evolved.", "人間が笑う理由は多様なので、その進化にはまだ学ぶことが多い。", "laugh / have"),
]
passage_3c = {
    "label": "C", "title": "The Evolution of Laughter",
    "paragraphs": passage_3c_paragraphs, "translations": passage_3c_translations,
    "sentencePairs": passage_3c_pairs,
    "questions": [
        make_question(34, None, None,
            ["By searching for behavior that seems like laughter in other species.", "By analyzing the kinds of things that people think are funny.", "By studying the reactions of human babies from the time they are born.", "By investigating the muscles that are used when a person laughs."],
            ["他種の笑いに似た行動を探して。", "人が面白いと思う物事を分析して。", "出生時から赤ん坊の反応を研究して。", "笑うとき使う筋肉を調べて。"], 1,
            ["other animals の similar behavior を探して進化を調べている。", "ユーモアの内容を分析する研究ではない。", "乳児の追跡研究についての記述はない。", "健康効果として筋肉は出るが、進化研究の方法ではない。"],
            "by doing は手段を表し「…することによって」。how laughter evolved は間接疑問。",
            question="How are researchers trying to find out about the development of laughter in humans?",
            question_translation="研究者は人間の笑いの発達をどのように調べていますか。",
            source_evidence=["by looking for similar behavior in other animals"]),
        make_question(35, None, None,
            ["Chimpanzees make the same noises as humans do when they are surprised.", "Chimpanzees produce sounds by breathing through their noses.", "Chimpanzees do not only make sounds when they breathe out.", "Chimpanzees do not breathe as slowly as humans do when they laugh."],
            ["驚いた人間と同じ音を出す。", "鼻で呼吸して音を出す。", "息を吐くときだけ音を出すのではない。", "人間ほどゆっくり呼吸しない。"], 3,
            ["驚いたときの音は比較されていない。", "鼻呼吸についての記述はない。", "吐くときと吸うときの両方で音を出す。", "呼吸速度についての比較はない。"],
            "both A and B は「AとBの両方」。not only はここでは選択肢内で「…だけではない」。",
            question="How is chimpanzees’ laughter different from most humans’ laughter?",
            question_translation="チンパンジーの笑いは、ほとんどの人間の笑いとどう違いますか。",
            source_evidence=["they make a noise both when they breathe out and when they breathe in"]),
        make_question(36, None, None,
            ["indicate that their behavior is not serious.", "welcome new members to their groups.", "warm their muscles up before they go hunting.", "avoid fighting by scaring other chimpanzees away."],
            ["行動が本気でないと示す。", "群れの新しい仲間を歓迎する。", "狩りの前に筋肉を温める。", "他のチンパンジーを怖がらせ争いを避ける。"], 1,
            ["本気で傷つけるつもりがないと知らせる合図。", "新しい仲間の歓迎についての記述はない。", "遊びで技能は伸ばすが、筋肉を温める目的ではない。", "怖がらせるのではなく、安心させる。"],
            "let 人 know that ... は「人に…と知らせる」。try to harm は「傷つけようとする」。",
            question="Researchers think that chimpanzees use laughter to",
            question_translation="研究者はチンパンジーが笑いを何のために使うと考えていますか。",
            source_evidence=["letting others know that it is not really trying to harm them"]),
        make_question(37, None, None,
            ["measure the signals in humans’ brains when they laugh.", "recognize the different noises made by dolphins.", "observe the laughter-like noises of a kind of animal.", "identify the exact reason that a human is laughing."],
            ["人が笑うときの脳信号を測る。", "イルカの異なる音を識別する。", "ある動物の笑いに似た音を観察する。", "人が笑う正確な理由を特定する。"], 3,
            ["人間の脳信号についての研究ではない。", "イルカのクリック音は装置が必要とは書かれていない。", "人には高すぎるネズミの音を装置で検出する。", "人間の笑う理由を装置で特定する話ではない。"],
            "too + 形容詞 + for 人 to do は「人には…すぎて～できない」。can be detected は受動態。",
            question="Special equipment needs to be used in order to",
            question_translation="特殊な装置を使う必要があるのは、",
            source_evidence=["the laughter-like sounds they make when they are touched gently are too high for humans to hear", "the sounds can be detected with special equipment"]),
        make_question(38, None, None,
            ["The goal of play in animals is to make other members of their groups laugh.", "Experts still have things to learn about how human laughter developed.", "One of the benefits of laughter is that it helps people develop strong muscles.", "Researchers have found evidence that chimpanzees actually tell each other jokes."],
            ["動物の遊びの目的は群れの仲間を笑わせることだ。", "専門家には人間の笑いの発達についてまだ学ぶことがある。", "笑いには強い筋肉を育てる利点がある。", "チンパンジーが冗談を言い合う証拠が見つかった。"], 2,
            ["遊びは技能や関係を育て、笑わせること自体が目的とは書かれていない。", "研究者には人間の笑いの進化についてまだ学ぶことが多い。", "笑いは筋肉をほぐすが、強い筋肉を発達させるとは書かれていない。", "複雑な言語がなく冗談を言わないことが前提。"],
            "still have much to learn は「まだ学ぶべきことが多い」。how ... evolved は learn about の目的語となる間接疑問。",
            question="Which of the following statements is true?",
            question_translation="次の記述のうち正しいものはどれですか。",
            source_evidence=["researchers still have much to learn about how this behavior evolved"]),
    ],
}


vocab_rows = [
    ("method", "方法", "名詞", "Part 1 Q1", "This is an easy method of making ice cream.", "これはアイスクリームを作る簡単な方法だ。"),
    ("incredibly", "信じられないほど", "副詞", "Part 1 Q2", "The new camera is incredibly small.", "新しいカメラは信じられないほど小さい。"),
    ("industrial", "工業の、産業の", "形容詞", "Part 1 Q3", "The northern district is an industrial area.", "北部地区は工業地域だ。"),
    ("doubt", "疑う、そうではないと思う", "動詞", "Part 1 Q4", "I doubt that it will rain tomorrow.", "明日雨が降るとは思わない。"),
    ("tension", "緊張、気まずさ", "名詞", "Part 1 Q5", "There was tension between the two coworkers.", "二人の同僚の間に緊張があった。"),
    ("distribute", "配る、配布する", "動詞", "Part 1 Q6", "Please distribute the books to the students.", "生徒に本を配ってください。"),
    ("approve", "承認する、認める", "動詞", "Part 1 Q7", "The teacher did not approve the project.", "先生はその研究を承認しなかった。"),
    ("buried", "埋もれた、埋められた", "形容詞・過去分詞", "Part 1 Q8", "The document was buried under some papers.", "書類は紙の下に埋もれていた。"),
    ("notion", "考え、概念", "名詞", "Part 1 Q9", "The notion once seemed impossible.", "その考えはかつて不可能に思えた。"),
    ("ancestors", "祖先", "名詞", "Part 1 Q10", "She researched the lives of her ancestors.", "彼女は祖先の人生を調べた。"),
    ("amount to", "合計…になる", "句動詞", "Part 1 Q11", "The repairs amounted to over $70 million.", "修理費は7,000万ドルを超えた。"),
    ("pick out", "選び出す", "句動詞", "Part 1 Q12", "Tina picked out a pink dress.", "ティナはピンクのドレスを選んだ。"),
    ("inherit from", "…から受け継ぐ", "熟語", "Part 1 Q13", "Mike inherited the business from his father.", "マイクは父から事業を受け継いだ。"),
    ("separate from", "…から分けて", "熟語", "Part 1 Q14", "He keeps work separate from his private life.", "彼は仕事を私生活から分けている。"),
    ("at the mercy of", "…のなすがままに", "熟語", "Part 1 Q15", "The crew was at the mercy of the weather.", "船員は天候のなすがままだった。"),
    ("on the air", "放送されて", "熟語", "Part 1 Q16", "The program first went on the air in 1960.", "番組は1960年に初放送された。"),
    ("give off", "放出する", "句動詞", "Part 1 Q17", "The heater gives off plenty of heat.", "そのヒーターは十分な熱を出す。"),
    ("cannot help doing", "…せずにはいられない", "構文", "Part 1 Q18", "I cannot help eating these peanuts.", "このピーナツを食べずにはいられない。"),
    ("the very", "まさにその", "熟語", "Part 1 Q19", "That cup is the very thing I need.", "そのカップはまさに必要なものだ。"),
    ("not ... until", "…して初めて～する", "構文", "Part 1 Q20", "She did not arrive until the concert was over.", "彼女は終演して初めて到着した。"),
    ("legend", "伝説", "名詞", "Part 2A", "Johnny Appleseed is an American legend.", "ジョニー・アップルシードはアメリカの伝説だ。"),
    ("fiction", "創作、フィクション", "名詞", "Part 2A", "Much of the story is fiction.", "物語の多くは創作だ。"),
    ("be based on", "…に基づく", "熟語", "Part 2A", "The legend was based on a real person.", "伝説は実在の人物に基づいていた。"),
    ("northeastern", "北東部の", "形容詞", "Part 2A", "He was born in a northeastern state.", "彼は北東部の州で生まれた。"),
    ("move west", "西へ移動する", "熟語", "Part 2A", "Many families moved west to find land.", "多くの家族が土地を求めて西へ移動した。"),
    ("cider", "シードル、リンゴ酒", "名詞", "Part 2A", "Cider is an alcoholic drink made from apples.", "シードルはリンゴから作る酒だ。"),
    ("likely", "ありそうな、おそらく", "形容詞・副詞", "Part 2A", "The place would likely become a town.", "その場所は町になりそうだった。"),
    ("settle", "定住する", "動詞", "Part 2A", "Some people wanted to settle there.", "そこへ定住したい人もいた。"),
    ("rarely", "めったに…ない", "副詞", "Part 2A", "Chapman rarely wore shoes.", "チャップマンはめったに靴を履かなかった。"),
    ("at least", "少なくとも", "熟語", "Part 2A", "At least part of the tale is true.", "少なくとも物語の一部は真実だ。"),
    ("sailing ship", "帆船", "名詞句", "Part 2B", "Life on a sailing ship was hard.", "帆船での生活は厳しかった。"),
    ("physically", "肉体的に", "副詞", "Part 2B", "The work was physically tiring.", "その仕事は肉体的に疲れるものだった。"),
    ("to make matters worse", "さらに悪いことに", "熟語", "Part 2B", "To make matters worse, storms were common.", "さらに悪いことに、嵐が多かった。"),
    ("anchor", "いかり", "名詞", "Part 2B", "The sailors raised the ship’s anchor.", "船員はいかりを上げた。"),
    ("steady rhythm", "一定のリズム", "名詞句", "Part 2B", "The song helped them keep a steady rhythm.", "歌は一定のリズムを保つ助けになった。"),
    ("shantyman", "シャンティマン、音頭を取る船員", "名詞", "Part 2B", "The shantyman sang out the first line.", "シャンティマンが最初の一節を歌った。"),
    ("steamship", "蒸気船", "名詞", "Part 2B", "Steamships changed sailors’ work.", "蒸気船は船員の仕事を変えた。"),
    ("humor", "ユーモア、おかしみ", "名詞", "Part 2B", "Many shanties contain humor.", "多くのシャンティにはユーモアがある。"),
    ("annual", "年に一度の、毎年の", "形容詞", "Part 3A", "This is the eighth annual comic show.", "これは第8回の年次コミックショーだ。"),
    ("convention center", "コンベンションセンター", "名詞句", "Part 3A", "The show will be held at the convention center.", "ショーはコンベンションセンターで開かれる。"),
    ("rare", "珍しい、希少な", "形容詞", "Part 3A", "Rare comic books will be on sale.", "珍しいコミックが販売される。"),
    ("local creator", "地元の制作者", "名詞句", "Part 3A", "Visitors can buy books by local creators.", "来場者は地元作家の本を買える。"),
    ("participate", "参加する", "動詞", "Part 3A", "She wants to participate in the contest.", "彼女はコンテストに参加したい。"),
    ("reception desk", "受付", "名詞句", "Part 3A", "Please sign up at the reception desk.", "受付で申し込んでください。"),
    ("permission", "許可", "名詞", "Part 3A", "Get permission before taking a photo.", "写真を撮る前に許可を得なさい。"),
    ("cafeteria", "食堂、カフェテリア", "名詞", "Part 3A", "Visitors can eat in the cafeteria.", "来場者は食堂で食事できる。"),
    ("square", "広場", "名詞", "Part 3A", "Food trucks will be in the square.", "フードトラックは広場に出る。"),
    ("generate electricity", "発電する", "熟語", "Part 3B", "The dam was used to generate electricity.", "ダムは発電に使われた。"),
    ("walkway", "歩道", "名詞", "Part 3B", "A walkway was built above the river.", "川の上に歩道が造られた。"),
    ("power plant", "発電所", "名詞句", "Part 3B", "Workers used the path to reach the power plant.", "作業員は発電所へ行くため道を使った。"),
    ("attractive", "魅力的な", "形容詞", "Part 3B", "The path became attractive to tourists.", "その道は観光客に魅力的になった。"),
    ("officially", "正式に", "副詞", "Part 3B", "The walkway was officially opened in 1921.", "歩道は1921年に正式に開通した。"),
    ("route", "道筋、経路", "名詞", "Part 3B", "The king walked the eight-kilometer route.", "国王は8キロの経路を歩いた。"),
    ("concrete", "コンクリート", "名詞", "Part 3B", "Holes appeared in the concrete.", "コンクリートに穴が開いた。"),
    ("fence", "柵", "名詞", "Part 3B", "The metal fence fell into the valley.", "金属柵は谷へ落ちた。"),
    ("dramatic scenery", "壮大な景観", "名詞句", "Part 3B", "The dramatic scenery attracts visitors.", "壮大な景観が来訪者を引き付ける。"),
    ("evolve", "進化する", "動詞", "Part 3C", "Researchers study how laughter evolved.", "研究者は笑いがどう進化したかを研究する。"),
    ("blood flow", "血流", "名詞句", "Part 3C", "Laughter can improve blood flow.", "笑いは血流を改善し得る。"),
    ("species", "（生物の）種", "名詞", "Part 3C", "The behavior was found in over 60 species.", "その行動は60を超える種で見つかった。"),
    ("breathe out", "息を吐く", "句動詞", "Part 3C", "Humans make a noise when they breathe out.", "人間は息を吐くとき音を出す。"),
    ("closely related to", "…に近縁で", "熟語", "Part 3C", "Chimpanzees are closely related to humans.", "チンパンジーは人間に近縁だ。"),
    ("roughly", "荒っぽく", "副詞", "Part 3C", "The chimpanzees played roughly together.", "チンパンジーは一緒に荒っぽく遊んだ。"),
    ("identify", "特定する、見分ける", "動詞", "Part 3C", "Researchers identified laughter in many animals.", "研究者は多くの動物の笑いを特定した。"),
    ("detect", "検出する", "動詞", "Part 3C", "Special equipment can detect the sound.", "特殊装置でその音を検出できる。"),
    ("a variety of", "さまざまな", "熟語", "Part 3C", "Humans laugh for a variety of reasons.", "人間はさまざまな理由で笑う。"),
]


def slugify(word):
    return "_".join(filter(None, "".join(
        ch.lower() if ch.isalnum() else " " for ch in word
    ).split()))


assert len(vocab_rows) == 65
assert len({row[0] for row in vocab_rows}) == 65
vocabulary = []
meanings = [row[1] for row in vocab_rows]
for index, (word, meaning, pos, source, example, example_ja) in enumerate(vocab_rows):
    distractors = []
    for offset in (7, 19, 31):
        candidate = meanings[(index + offset) % len(meanings)]
        if candidate != meaning and candidate not in distractors:
            distractors.append(candidate)
    while len(distractors) < 3:
        candidate = meanings[(index + len(distractors) + 1) % len(meanings)]
        if candidate != meaning and candidate not in distractors:
            distractors.append(candidate)
    vocabulary.append({
        "word": word, "meaning": meaning, "pos": pos, "level": "2級",
        "source": source, "example": example, "exampleJa": example_ja,
        "distractors": distractors,
        "wordAudio": f"audio/vocab/w_{index + 1:03d}_{slugify(word)}.mp3",
    })


focus_points = [
    {
        "id": "fp1", "title": "cannot help doing（…せずにはいられない）",
        "subtitle": "Gerund after a Fixed Expression",
        "explanation": "cannot help doing は、意志で抑えようとしても「…せずにはいられない」という意味を表す。help の後はこの構文では to不定詞や動詞原形ではなく動名詞を置く。",
        "sourceQuote": "I can’t help eating these peanuts.", "sourceLocation": "Part 1 Q18",
        "examples": [
            {"en": "I can’t help eating these peanuts.", "ja": "このピーナツを食べずにはいられない。", "note": "help の後は eating。"},
            {"en": "She could not help laughing at the story.", "ja": "彼女はその話を聞いて笑わずにはいられなかった。", "note": "過去なら could not help doing。"},
            {"en": "We cannot help worrying about the storm.", "ja": "私たちは嵐を心配せずにはいられない。", "note": "感情や反応にも使える。"},
        ],
        "practicePassage": {
            "en": "[Source: Part 1 Q18]\nThe peanuts are so delicious that I can’t help eating them. Once I start, it is very difficult to stop.",
            "ja": "ピーナツがとてもおいしいので、食べずにはいられない。いったん食べ始めると、やめるのがとても難しい。",
            "audioFile": "audio/practice_pp1.mp3",
        },
        "practiceQuestions": [
            {"q": "cannot help の後に置く形は何ですか。", "a": "動名詞（doing）です。"},
            {"q": "can’t help eating を自然な日本語にしてください。", "a": "「食べずにはいられない」です。"},
            {"q": "Once I start の意味は何ですか。", "a": "「いったん始めると」です。"},
            {"q": "本文でやめにくい理由は何ですか。", "a": "ピーナツがとてもおいしいからです。"},
        ],
        "highlightPatterns": ["can’t help eating", "Once I start"],
        "highlightColor": "#FF6B6B", "highlightLabel": "cannot help doing",
    },
    {
        "id": "fp2", "title": "be based on（…に基づく）",
        "subtitle": "Passive Voice and Source",
        "explanation": "be based on ... は「…に基づいている」。伝説や物語の土台となる事実・人物を示す。本文では創作の多い伝説と実在の John Chapman を結び付ける重要表現である。",
        "sourceQuote": "Johnny Appleseed was based on a real person", "sourceLocation": "Part 2A",
        "examples": [
            {"en": "Johnny Appleseed was based on a real person.", "ja": "ジョニー・アップルシードは実在の人物に基づいていた。", "note": "real person が根拠。"},
            {"en": "The movie is based on a true story.", "ja": "その映画は実話に基づいている。", "note": "作品の元情報を示す。"},
            {"en": "Their decision was based on the evidence.", "ja": "彼らの決定は証拠に基づいていた。", "note": "判断の根拠にも使う。"},
        ],
        "practicePassage": {
            "en": "[Source: Johnny Appleseed]\nMuch of the story is fiction. However, Johnny Appleseed was based on a real person. This was a man called John Chapman.",
            "ja": "物語の多くは創作である。しかし、ジョニー・アップルシードは実在の人物に基づいていた。それがジョン・チャップマンという男性だった。",
            "audioFile": "audio/practice_pp2.mp3",
        },
        "practiceQuestions": [
            {"q": "be based on の意味は何ですか。", "a": "「…に基づく」です。"},
            {"q": "伝説の土台になった人物は誰ですか。", "a": "John Chapman です。"},
            {"q": "Much of the story is fiction は何を認めていますか。", "a": "物語の多くが創作であることです。"},
            {"q": "This was a man ... の This は何を指しますか。", "a": "a real person を指します。"},
        ],
        "highlightPatterns": ["was based on a real person", "Much of the story is fiction"],
        "highlightColor": "#4F8CFF", "highlightLabel": "be based on",
    },
    {
        "id": "fp3", "title": "To make matters worse（さらに悪いことに）",
        "subtitle": "Adding a Worse Condition",
        "explanation": "To make matters worse は、すでに悪い状況に別の悪条件を追加するつなぎ表現。前後の内容を比べ、単なる原因・時間経過ではなく「悪化の追加」だと判断する。",
        "sourceQuote": "To make matters worse, the sea itself was a very dangerous place", "sourceLocation": "Part 2B",
        "examples": [
            {"en": "To make matters worse, accidents were common.", "ja": "さらに悪いことに、事故が多かった。", "note": "悪条件を追加する。"},
            {"en": "The food was poor, and to make matters worse, the work was tiring.", "ja": "食事が悪く、さらに悪いことに仕事もきつかった。", "note": "and と共に追加できる。"},
            {"en": "It began to storm, and to make matters worse, the engine stopped.", "ja": "嵐になり、さらに悪いことにエンジンも止まった。", "note": "問題が重なる流れ。"},
        ],
        "practicePassage": {
            "en": "[Source: Sea Shanties]\nThe sailors’ work was boring and physically tiring. To make matters worse, the sea itself was very dangerous, especially during storms, and accidents were common.",
            "ja": "船員の仕事は退屈で肉体的に疲れるものだった。さらに悪いことに、海自体も特に嵐のときは危険で、事故が多かった。",
            "audioFile": "audio/practice_pp3.mp3",
        },
        "practiceQuestions": [
            {"q": "To make matters worse はどんな関係を表しますか。", "a": "悪い状況へ、さらに悪い状況を追加します。"},
            {"q": "最初の悪条件は何ですか。", "a": "仕事が退屈で肉体的に疲れることです。"},
            {"q": "追加された悪条件は何ですか。", "a": "海が危険で事故が多いことです。"},
            {"q": "especially during storms は何を限定しますか。", "a": "海が危険になる時、とりわけ嵐の間を示します。"},
        ],
        "highlightPatterns": ["To make matters worse", "physically tiring", "accidents were common"],
        "highlightColor": "#22C55E", "highlightLabel": "worse condition",
    },
    {
        "id": "fp4", "title": "must have been made（完了形の受動態）",
        "subtitle": "Completed Requirement",
        "explanation": "must have been made は must + have been + 過去分詞。ここでは過去の推量ではなく、応募時点までに衣装が本人によって作られている必要があるという参加条件を表す。",
        "sourceQuote": "your costume must have been made by you", "sourceLocation": "Part 3A",
        "examples": [
            {"en": "Your costume must have been made by you.", "ja": "衣装は自分で作ったものでなければならない。", "note": "by you が作者を示す。"},
            {"en": "The form must have been signed before noon.", "ja": "用紙は正午までに署名済みでなければならない。", "note": "期限までの完了条件。"},
            {"en": "Tickets must have been purchased online.", "ja": "チケットはオンラインで購入済みでなければならない。", "note": "受動態なので対象が主語。"},
        ],
        "practicePassage": {
            "en": "[Source: Thank you for signing up]\nIf you want to participate, sign up at the reception desk by noon. Your costume must have been made by you. People wearing costumes bought from a store will not be allowed to enter.",
            "ja": "参加する場合は正午までに受付で申し込む。衣装は自作でなければならない。店で買った衣装を着た人は参加できない。",
            "audioFile": "audio/practice_pp4.mp3",
        },
        "practiceQuestions": [
            {"q": "衣装を作った人は誰でなければなりませんか。", "a": "参加者本人です。"},
            {"q": "have been made は何態ですか。", "a": "完了形の受動態です。"},
            {"q": "申込期限はいつですか。", "a": "正午までです。"},
            {"q": "店で買った衣装の人は参加できますか。", "a": "参加できません。"},
        ],
        "highlightPatterns": ["must have been made by you", "will not be allowed to enter"],
        "highlightColor": "#F59E0B", "highlightLabel": "perfect passive",
    },
    {
        "id": "fp5", "title": "by doing と too ... to do",
        "subtitle": "Method and Impossibility",
        "explanation": "by doing は「…することによって」と手段を表す。too + 形容詞 + for 人 to do は「人には…すぎて～できない」。研究方法と、人間の耳では聞けない理由をそれぞれ正確に示す。",
        "sourceQuote": "By listening for the noises made by other animals", "sourceLocation": "Part 3C",
        "examples": [
            {"en": "Researchers learned by listening to animals.", "ja": "研究者は動物の音を聞くことで学んだ。", "note": "by doing は手段。"},
            {"en": "The sound is too high for humans to hear.", "ja": "その音は人間には高すぎて聞こえない。", "note": "too ... to は不可能を含む。"},
            {"en": "The sounds can be detected by using special equipment.", "ja": "その音は特殊装置を使うことで検出できる。", "note": "by using も手段。"},
        ],
        "practicePassage": {
            "en": "[Source: The Evolution of Laughter]\nBy listening for the noises made by animals during play, researchers identified “laughter.” The sounds made by rats are too high for humans to hear, but they can be detected with special equipment.",
            "ja": "遊び中の動物の音を聞くことで、研究者は「笑い」を特定した。ネズミの音は人には高すぎて聞こえないが、特殊装置で検出できる。",
            "audioFile": "audio/practice_pp5.mp3",
        },
        "practiceQuestions": [
            {"q": "By listening ... は何を表しますか。", "a": "研究者が笑いを特定した手段です。"},
            {"q": "too high for humans to hear の意味は何ですか。", "a": "人間には高すぎて聞こえない、です。"},
            {"q": "ネズミの音は何で検出できますか。", "a": "特殊な装置です。"},
            {"q": "made by animals の made は何を修飾しますか。", "a": "the noises を後ろから修飾します。"},
        ],
        "highlightPatterns": ["By listening for", "too high for humans to hear", "can be detected"],
        "highlightColor": "#A855F7", "highlightLabel": "method / too-to",
    },
]


sections = [
    {
        "name": "大問1", "nameEn": "Part 1", "type": "vocabulary",
        "instruction": "次の(1)から(20)までの（　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "questions": section1_questions,
    },
    {
        "name": "大問2", "nameEn": "Part 2", "type": "passage-fill",
        "instruction": "次の英文A、Bを読み、その文意にそって(21)から(26)までの（　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "passages": [passage_2a, passage_2b],
    },
    {
        "name": "大問3", "nameEn": "Part 3", "type": "reading-comprehension",
        "instruction": "次の英文A、B、Cの内容に関して、(27)から(38)までの質問に対して最も適切なもの、または文を完成させるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "passages": [passage_3a, passage_3b, passage_3c],
    },
]

all_questions = []
for section in sections:
    all_questions.extend(section.get("questions", []))
    for passage in section.get("passages", []):
        all_questions.extend(passage.get("questions", []))

assert [item["number"] for item in all_questions] == list(range(1, 39))
assert {item["number"]: item["answer"] for item in all_questions} == ANSWERS
assert [len(passage["questions"]) for passage in [passage_2a, passage_2b, passage_3a, passage_3b, passage_3c]] == [3, 3, 3, 4, 5]
assert [len(passage["sentencePairs"]) for passage in [passage_2a, passage_2b, passage_3a, passage_3b, passage_3c]] == [19, 20, 15, 17, 17]
assert all(len(item["choiceAnalysis"]) == 4 for item in all_questions)
assert all(item["choiceAnalysis"][item["answer"] - 1].count("→正解。💡") == 1 for item in all_questions)

data = {
    "grade": "2級",
    "year": "2022",
    "session": "3",
    "title": "2022年度 第3回 英語資格検定2級 リーディング",
    "exam": "2022-3",
    "sections": sections,
    "listening": LISTENING,
    "vocabulary": vocabulary,
    "lessonPlan": {"focusPoints": focus_points},
}

OUT_DIR.mkdir(parents=True, exist_ok=True)
temporary = OUT_PATH.with_suffix(".json.tmp")
with temporary.open("w", encoding="utf-8", newline="\n") as stream:
    json.dump(data, stream, ensure_ascii=False, indent=4)
    stream.write("\n")
os.replace(temporary, OUT_PATH)
print(
    f"Wrote {OUT_PATH} | questions={len(all_questions)} "
    f"vocabulary={len(vocabulary)} focusPoints={len(focus_points)}"
)
