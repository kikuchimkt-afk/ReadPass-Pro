# -*- coding: utf-8 -*-
"""Build the audited ReadPass data set for EIKEN Grade 2, 2022-2 main venue."""

import json
import os
import re
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent
OUT_DIR = REPO / "data" / "grade2" / "2022-2"
OUT_PATH = OUT_DIR / "data.json"

ANSWERS = dict(enumerate([
    1, 1, 3, 3, 1, 2, 3, 4, 2, 3,
    2, 3, 3, 4, 1, 1, 2, 1, 2, 2,
    2, 3, 1, 2, 3, 4,
    2, 1, 2, 4, 4, 1, 1, 2, 2, 1, 1, 4,
], 1))

LISTENING = {
    "part1": {str(i): answer for i, answer in enumerate(
        [3, 4, 4, 1, 2, 4, 3, 4, 1, 3, 1, 1, 3, 1, 3], 1)},
    "part2": {str(i): answer for i, answer in enumerate(
        [4, 1, 4, 2, 3, 1, 1, 1, 2, 2, 2, 4, 2, 2, 2], 16)},
}


def make_question(number, text, translation, choices, choice_ja, reasons, grammar,
                  *, question=None, question_translation=None, source_evidence=None):
    answer = ANSWERS[number]
    analyses = []
    for index, (choice, meaning, reason) in enumerate(zip(choices, choice_ja, reasons), 1):
        marker = "→正解。💡" if index == answer else "→"
        analyses.append(f"{choice}（{meaning}）{marker}{reason}")
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
        item.pop("text", None)
        item.pop("translation", None)
        item["question"] = question
        item["questionTranslation"] = question_translation
    if source_evidence:
        item["sourceEvidence"] = source_evidence
    return item


def pair(en, ja, verb=""):
    return [en, ja, f"{en}|{ja}", verb]


def build_passage(label, title, paragraph_sentences, pair_rows, questions, **extra):
    paragraphs = []
    translations = []
    offset = 0
    for count in paragraph_sentences:
        selected = pair_rows[offset:offset + count]
        paragraphs.append(" ".join(item[0] for item in selected))
        translations.append("".join(item[1] for item in selected))
        offset += count
    assert offset == len(pair_rows)
    item = {
        "label": label,
        "title": title,
        "paragraphs": paragraphs,
        "translations": translations,
        "sentencePairs": [pair(*row) for row in pair_rows],
        "questions": questions,
    }
    item.update(extra)
    return item


section1_questions = [
    make_question(
        1,
        "Considering that Keiko has only been studying English for six months, she gave a ( ) good English presentation at yesterday’s contest. She got second prize.",
        "ケイコが英語を勉強し始めてまだ6か月だということを考えると、昨日のコンテストで（　）上手な英語の発表をした。彼女は2位になった。",
        ["remarkably", "nervously", "suddenly", "carefully"],
        ["著しく・驚くほど", "緊張して", "突然に", "注意深く"],
        ["学習期間が短いのに2位という高評価なので、驚くほど上手だったという意味が合う。", "発表時の態度ではなく good の程度を表す文脈である。", "上手さが突然だったという意味にはならない。", "注意深い発表というより、good を強める程度副詞が必要である。"],
        "Considering that ... は「…を考えると」。remarkably は形容詞 good を修飾する程度の副詞。",
    ),
    make_question(
        2,
        "A: How was your vacation, Dale?\nB: It was ( )! We had seven days of pure fun and relaxation.",
        "A：休暇はどうだった、デイル。\nB：（　）だったよ。7日間ずっと心から楽しみ、くつろげた。",
        ["marvelous", "industrial", "humble", "compact"],
        ["すばらしい", "産業の", "謙虚な", "小型の・ぎっしりした"],
        ["pure fun and relaxation から、休暇がすばらしかったと分かる。", "休暇を産業のと評価するのは不自然である。", "休暇そのものを謙虚だとは言わない。", "休暇の満足度を表す語ではない。"],
        "How was ...? への答えとして It was + 形容詞を用いる。marvelous は強い肯定評価。",
    ),
    make_question(
        3,
        "People around the world are afraid that the ( ) between the two countries will cause a war.",
        "世界中の人々は、両国間の（　）が戦争を引き起こすのではないかと心配している。",
        ["patient", "phrase", "conflict", "courage"],
        ["患者・忍耐強い", "句・表現", "対立・紛争", "勇気"],
        ["国と国の間の出来事を patient とは呼ばない。", "句が戦争を引き起こすという意味にはならない。", "between the two countries と cause a war が、国家間の対立を示す。", "勇気が戦争を起こすという文脈ではない。"],
        "be afraid that S V は「SがVすることを心配する」。conflict between A and B で「AとBの間の対立」。",
    ),
    make_question(
        4,
        "The baseball player Shuta Omura had to have ( ) on his right knee in 2019, but he made a full recovery and was ready to play again in 2020.",
        "野球選手の大村修太は2019年に右ひざの（　）を受けなければならなかったが、完全に回復し、2020年には再びプレーできる状態になった。",
        ["recognition", "innocence", "surgery", "inquiry"],
        ["認識・評価", "無実", "手術", "調査・問い合わせ"],
        ["ひざに recognition を受けるとは言わない。", "ひざの無実という意味は成立しない。", "have surgery on one's knee で「ひざの手術を受ける」。回復した流れとも一致する。", "ひざについての問い合わせを受けた話ではない。"],
        "have surgery on + 身体部位で「…の手術を受ける」。make a full recovery は「完全に回復する」。",
    ),
    make_question(
        5,
        "The restaurant lost its good ( ) after several cases of food poisoning, and eventually it had to close.",
        "そのレストランは食中毒が数件起きた後、良い（　）を失い、最終的に閉店しなければならなかった。",
        ["reputation", "anticipation", "observation", "examination"],
        ["評判", "予想・期待", "観察", "試験・検査"],
        ["food poisoning の発生で店の評判を失ったという因果が自然である。", "期待を失うより、社会的評価を失った文脈である。", "観察を失うとは言わない。", "検査を失うという意味にはならない。"],
        "lose one's reputation で「評判を失う」。after + 名詞句が時を表す。",
    ),
    make_question(
        6,
        "Sunlight is important for people to stay healthy. However, it is not good to ( ) skin to too much sunlight.",
        "日光は健康を保つために大切だ。しかし、肌を過度の日光に（　）のはよくない。",
        ["protest", "expose", "conduct", "represent"],
        ["抗議する", "さらす", "実施する・導く", "表す・代表する"],
        ["protest skin という語の結び付きはない。", "expose A to B で「AをBにさらす」。too much sunlight が根拠。", "肌を日光へ実施するとは言わない。", "肌を日光に代表させる意味ではない。"],
        "expose A to B は重要語法。it は形式主語で、to expose ... が真の主語。",
    ),
    make_question(
        7,
        "After Kai broke his arm, it took about three months to ( ) completely. Now he can play tennis again without any problems.",
        "カイが腕を折ってから、完全に（　）まで約3か月かかった。今では問題なく再びテニスができる。",
        ["fulfill", "cheat", "heal", "retire"],
        ["果たす", "だます", "治る", "引退する"],
        ["腕が目的を果たすという意味ではない。", "けがからの回復とは関係がない。", "骨折した腕が完全に治るまでの期間を述べている。", "腕が引退するという意味にはならない。"],
        "It takes 時間 to do は「…するのに時間がかかる」。heal は自動詞で「傷が治る」。",
    ),
    make_question(
        8,
        "These days, many companies are offering their employees a lot of ( ). For example, staff members can sometimes work from home or choose what time to start and finish.",
        "最近、多くの会社が従業員に多くの（　）を提供している。例えば、在宅勤務をしたり、始業・終業時刻を選んだりできる場合がある。",
        ["majority", "similarity", "quantity", "flexibility"],
        ["大多数", "類似性", "量", "柔軟性"],
        ["在宅勤務や時刻選択は多数派の話ではない。", "働き方が似ているという説明ではない。", "仕事量を多く与える意味では文脈に合わない。", "場所や時間を選べることは働き方の柔軟性を示す。"],
        "offer 人 物 は第4文型で「人に物を提供する」。For example 以下が flexibility の具体例。",
    ),
    make_question(
        9,
        "Kevin got stuck in a snowstorm while driving home. The weather was so bad that he had to ( ) his car and walk the rest of the way.",
        "ケビンは車で帰宅中、吹雪で動けなくなった。天候があまりに悪かったので、車を（　）して残りの道を歩かなければならなかった。",
        ["maintain", "abandon", "prevent", "supply"],
        ["維持する", "放棄する・置き去りにする", "防ぐ", "供給する"],
        ["車を整備した後に歩いたという話ではない。", "吹雪で車を置いて歩いたという流れに合う。", "車を防ぐという目的語関係は不自然である。", "車を供給する文脈ではない。"],
        "so + 形容詞 + that S V は「とても…なのでSはVする」。abandon one's car は「車を置き去りにする」。",
    ),
    make_question(
        10,
        "Laura was unhappy about being ( ) from the badminton tournament so early, but now she supports her friends during their matches.",
        "ローラはバドミントン大会からこんなに早く（　）されたことを残念に思ったが、今は友人の試合を応援している。",
        ["committed", "defended", "eliminated", "imported"],
        ["委ねられた", "守られた", "敗退させられた", "輸入された"],
        ["大会に委ねられたという意味ではない。", "大会から守られたという話ではない。", "be eliminated from a tournament で「大会から敗退する」。", "人が大会から輸入されることはない。"],
        "being + 過去分詞は動名詞の受動態。be eliminated from ... は「…から敗退させられる」。",
    ),
    make_question(
        11,
        "Sarah has been told to ( ) running until her foot is better. Otherwise, she might make her injury worse.",
        "サラは足がよくなるまでランニングを（　）よう言われている。そうしなければけがを悪化させるかもしれない。",
        ["read through", "refrain from", "reflect on", "refer to"],
        ["通読する", "控える", "振り返る", "参照する"],
        ["running を通読することはできない。", "refrain from doing で「…するのを控える」。けがの悪化防止と合う。", "走ることを振り返るという助言ではない。", "running を参照するという意味ではない。"],
        "tell 人 to do の受動態 has been told to do。refrain from の後は動名詞。",
    ),
    make_question(
        12,
        "A: How did you like the movie?\nB: ( ), I enjoyed it. Even though some of the actors weren’t the best, the story was great and the music was beautiful.",
        "A：映画はどうだった。\nB：（　）、楽しめたよ。俳優の中には最高とは言えない人もいたが、物語は素晴らしく音楽も美しかった。",
        ["On the move", "In respect", "As a whole", "By then"],
        ["移動中で", "その点で", "全体として", "その時までに"],
        ["移動しながら映画を見たという話ではない。", "in respect 単独ではこの総合評価を表さない。", "一部に不満はあるが全体として楽しんだ、という対比に合う。", "過去の基準時までという時間表現は不要である。"],
        "Even though は譲歩「…だけれども」。as a whole は文全体を評価する副詞句。",
    ),
    make_question(
        13,
        "A: What’s wrong, Emily?\nB: Jim made a ( ) of me in front of my friends. He said my shoes were ugly.",
        "A：どうしたの、エミリー。\nB：ジムが友達の前で私を（　）にしたの。私の靴がひどいと言った。",
        ["difference", "point", "fool", "start"],
        ["違い", "要点", "笑いもの・ばか", "始まり"],
        ["make a difference of 人 とは言わない。", "make a point of は後ろに動名詞を取る別の表現。", "make a fool of 人 で「人を笑いものにする」。靴をけなした状況と合う。", "make a start of 人 という表現はない。"],
        "make a fool of + 人 は熟語。in front of ... は「…の前で」。",
    ),
    make_question(
        14,
        "Jason has asked his mother several times to stop ( ) his personal life. He is upset that she wants to try to control him even though he is an adult.",
        "ジェイソンは母親に、自分の私生活へ（　）のをやめるよう何度も頼んだ。成人なのに母親が自分を支配しようとすることに腹を立てている。",
        ["counting on", "insisting on", "comparing with", "interfering with"],
        ["頼ること", "言い張ること", "比較すること", "干渉すること"],
        ["母親が彼の私生活を頼るという意味ではない。", "insist on の目的語は行為・主張で、personal life への関与を表さない。", "比較対象が示されていない。", "interfere with ... で「…に干渉する」。control him が根拠。"],
        "stop doing は「…するのをやめる」。interfere with + 名詞で「…に干渉する」。",
    ),
    make_question(
        15,
        "A: It’s a shame that we had to ( ) the barbecue.\nB: Yes, but we can’t hold a barbecue outside in the rain. We can hold it next week instead if the weather is better.",
        "A：バーベキューを（　）しなければならなかったのは残念だ。\nB：そうだね。でも雨の中、外ではできないよ。天気がよければ代わりに来週できる。",
        ["call off", "pick on", "fall for", "bring out"],
        ["中止する", "いじめる", "だまされる", "持ち出す・発表する"],
        ["雨のため予定を中止し、来週へ延期する流れに合う。", "バーベキューをいじめるとは言わない。", "バーベキューにだまされる意味ではない。", "屋外へ持ち出す話ではなく、開催をやめた話である。"],
        "have to do は必要・義務。call off an event は「行事を中止する」。",
    ),
    make_question(
        16,
        "The thief must have gotten into the building ( ) of a ladder. The only way to get in was through a second-floor window.",
        "泥棒ははしご（　）建物へ入ったに違いない。入れる唯一の方法は2階の窓からだった。",
        ["by means", "in charge", "at times", "for all"],
        ["…を使って", "…を担当して", "時々", "…にもかかわらず"],
        ["by means of a ladder で「はしごを使って」。", "in charge of は「…を担当して」で手段にならない。", "at times of a ladder という表現はない。", "for all は譲歩を表し、道具を示さない。"],
        "must have + 過去分詞は過去についての強い推量。by means of は手段を表す。",
    ),
    make_question(
        17,
        "Barney tried to teach his cat to follow some simple commands, but his efforts were ( ). Every time he told it to lie down, it just walked away.",
        "バーニーは猫に簡単な命令へ従うよう教えようとしたが、努力は（　）だった。横になるよう言うたび、猫はただ歩き去った。",
        ["of late", "in vain", "for sure", "by chance"],
        ["最近", "無駄に", "確かに", "偶然に"],
        ["時間を表す of late は努力の結果にならない。", "猫が命令に従わなかったので、努力は無駄だった。", "efforts were for sure という表現は不自然である。", "努力が偶然だったという意味ではない。"],
        "try to do は試み。in vain は「無駄に・効果なく」。Every time S V は「SがVするたび」。",
    ),
    make_question(
        18,
        "( ) lived in Tokyo for three years, Cassandra knew exactly how to get to Tokyo Skytree from her apartment.",
        "東京に3年間住んでいたので、カサンドラは自宅から東京スカイツリーまでの行き方を正確に知っていた。",
        ["Having", "Had", "Have", "To have"],
        ["…したので（完了分詞構文）", "持っていた", "持つ", "持つために"],
        ["Having lived は主節より前の経験を示す完了分詞構文で、道を知る理由になる。", "Had lived なら接続詞と主語が必要である。", "Have lived は主語のない定動詞になり文を作れない。", "To have lived は目的を表せず、後続の knew につながらない。"],
        "Having + 過去分詞は完了形の分詞構文。主節の主語 Cassandra が lived の意味上の主語。",
    ),
    make_question(
        19,
        "Somebody had broken one of the windows in Michelle’s classroom. Michelle had not done it, but some of the other students looked at her ( ) she had.",
        "誰かがミシェルの教室の窓を1枚割っていた。ミシェルはしていなかったが、ほかの生徒の何人かは、まるで彼女がした（　）彼女を見た。",
        ["as to", "as if", "if only", "if not"],
        ["…について", "まるで…であるかのように", "…でさえあれば", "…でないとしても"],
        ["as to は話題を示し、had の節を導かない。", "as if she had で「まるで彼女がしたかのように」。事実に反する見方を表す。", "if only は願望を表し、looked at her につながらない。", "if not は「そうでなければ」で、比較の意味にならない。"],
        "as if + 過去完了は過去の事実に反する様子を表す。had の後には broken it が省略されている。",
    ),
    make_question(
        20,
        "A: How long does it take to drive to your parents’ house?\nB: There’s no ( ) with traffic during the holidays. It could take thirty minutes, or it could take two hours.",
        "A：ご両親の家まで車でどのくらいかかる。\nB：休暇中の交通は（　）できないよ。30分のこともあれば、2時間かかることもある。",
        ["tell", "telling", "tells", "told"],
        ["分かること", "予測すること", "分かる（三単現）", "言われた"],
        ["There’s no の後には動詞原形を直接置けない。", "There is no telling で「予測できない・分からない」という定型表現。", "三単現動詞は no の後に置けない。", "過去分詞では定型表現にならない。"],
        "There is no doing は「…することはできない」。could は状況により起こり得る幅を示す。",
    ),
]


questions_2a = [
    make_question(
        21, None, None,
        ["completely disappears", "ends up elsewhere", "is given to charities", "could be used again"],
        ["完全に消える", "別の場所へ行き着く", "慈善団体へ渡される", "再利用できる"],
        ["直後に海へ流入する量が示されるため、消えるのではない。", "埋立地以外へ行き着き、具体的には海へ入ることを後続文が説明している。", "慈善団体への寄付については述べられていない。", "再利用可能性ではなく、海へ流出する問題を述べている。"],
        "end up + 副詞で「最終的に…に行き着く」。However が埋立てと別の行き先を対比する。",
        source_evidence=["more than 14 million tons of plastic waste goes into the ocean each year"],
    ),
    make_question(
        22, None, None,
        ["live in large family groups", "have to make long journeys", "see these as food", "leave the ocean"],
        ["大きな家族集団で暮らす", "長い旅をしなければならない", "これらを食べ物だと思う", "海を離れる"],
        ["家族集団の大きさは問題として述べられていない。", "移動距離ではなく、小さなプラスチック片を食べる問題である。", "魚や海鳥が小片を餌と見て食べてしまうことが後続文で示される。", "海を離れるのではなく、海中のプラスチックを食べる。"],
        "see A as B は「AをBと見なす」。these は smaller pieces of plastic を指す。",
        source_evidence=["have accidentally eaten tiny pieces of plastic floating in the ocean"],
    ),
    make_question(
        23, None, None,
        ["In spite of this", "Therefore", "Likewise", "In particular"],
        ["それにもかかわらず", "それゆえ", "同様に", "特に"],
        ["団体の努力があるにもかかわらず、廃棄量が増えるという逆接に合う。", "努力の結果としてごみが増えたわけではない。", "同種の出来事を並べる文脈ではない。", "具体例を一つ強調する文ではない。"],
        "in spite of + 名詞は譲歩。「this」は法整備要求や啓発活動をまとめて受ける。",
        source_evidence=["people continue to throw away plastic, and the amount of plastic in the ocean continues to increase"],
    ),
]

rows_2a = [
    ("Plastic is used in a wide variety of goods.", "プラスチックは多種多様な製品に使われている。", "is used"),
    ("In fact, it is estimated that about 400 million tons of plastic is produced around the world each year.", "実際、毎年世界で約4億トンのプラスチックが生産されると推定されている。", "is estimated / is produced"),
    ("Much of it is designed to be used only once and then thrown away.", "その多くは一度だけ使われ、その後捨てられるように作られている。", "is designed"),
    ("Most of this waste is buried in the ground in landfill sites.", "この廃棄物の大部分は埋立地の地中に埋められる。", "is buried"),
    ("However, a large amount ( 21 ).", "しかし、大量のものは（21）。", ""),
    ("According to the International Union for Conservation of Nature, more than 14 million tons of plastic waste goes into the ocean each year.", "国際自然保護連合によると、毎年1,400万トンを超えるプラスチックごみが海へ流れ込む。", "goes"),
    ("Plastic is strong and takes a long time to break down.", "プラスチックは丈夫で、分解するまで長い時間がかかる。", "is / takes"),
    ("For this reason, the world’s oceans are quickly filling up with it.", "このため、世界の海は急速にプラスチックで埋まりつつある。", "are filling up"),
    ("Plastic waste causes two major problems for wildlife living in and by the ocean.", "プラスチックごみは、海中や海辺に生きる野生生物に二つの大きな問題を引き起こす。", "causes"),
    ("First, animals sometimes get trapped by larger pieces of plastic and die because they are unable to swim freely.", "第一に、動物は大きなプラスチック片に絡まり、自由に泳げず死ぬことがある。", "get trapped / die"),
    ("The other problem, however, is caused by smaller pieces of plastic.", "しかし、もう一つの問題は、より小さなプラスチック片によって起こる。", "is caused"),
    ("Animals often ( 22 ).", "動物はしばしば（22）。", ""),
    ("A recent study found that about two-thirds of fish species and 90 percent of all seabirds have accidentally eaten tiny pieces of plastic floating in the ocean.", "最近の研究では、魚類の約3分の2の種と全海鳥の90パーセントが、海に漂う小さなプラスチック片を誤って食べていることが分かった。", "found / have eaten"),
    ("In response, many environmental protection organizations are making efforts to get governments to do something about the plastic in the ocean.", "これを受け、多くの環境保護団体が、海洋プラスチックについて政府に対策を取らせようと努力している。", "are making"),
    ("For instance, the Center for Biological Diversity has asked the U.S. government to make laws to control plastic pollution.", "例えば、生物多様性センターは米国政府にプラスチック汚染を規制する法律を作るよう求めている。", "has asked"),
    ("Such groups are also trying to educate the public about the problem.", "そのような団体は、この問題について一般の人々を啓発しようともしている。", "are trying"),
    ("( 23 ), people continue to throw away plastic, and the amount of plastic in the ocean continues to increase.", "（23）、人々はプラスチックを捨て続け、海中の量も増え続けている。", "continue / continues"),
]

passage_2a = build_passage("A", "Trouble at Sea", [8, 5, 4], rows_2a, questions_2a)


questions_2b = [
    make_question(
        24, None, None,
        ["not very important", "not created by him", "difficult to like", "based on his friends"],
        ["あまり重要ではなかった", "彼が作ったものではなかった", "好きになりにくかった", "友人をモデルにしていた"],
        ["Cats の登場人物は重要でないとは述べられていない。", "ほかの作品と同様、以前からある物語・詩から取られ、ウェバー自身の創作ではなかった。", "人気の理由を登場人物の好みにくさで説明していない。", "友人ではなく、T. S. Eliot の詩の猫が元である。"],
        "be created by ... は受動態。Like many of ... が前に述べた taken from stories との共通点を示す。",
        source_evidence=["The characters in these were taken from well-known stories", "one of Webber’s favorite books was Old Possum’s Book of Practical Cats"],
    ),
    make_question(
        25, None, None,
        ["the history of cats as pets", "how to take care of cats", "the personalities of some cats", "how cats’ bodies work"],
        ["ペットとしての猫の歴史", "猫の世話の仕方", "何匹かの猫の性格", "猫の体の仕組み"],
        ["猫の歴史を年代順に述べる詩ではない。", "飼育方法の説明ではない。", "注目を浴びたがる猫や夜に働く猫など、性格の異なる猫を描く詩である。", "体の機能を科学的に説明していない。"],
        "describe は「描写する」。For example 以下の具体例から personalities を判断する。",
        source_evidence=["one of the characters likes to be the focus of everyone’s attention", "Another seems to be lazy during the daytime"],
    ),
    make_question(
        26, None, None,
        ["In any case", "Unfortunately", "By mistake", "Similarly"],
        ["いずれにせよ", "残念ながら", "誤って", "同様に"],
        ["話題をまとめ直すのではなく、ロンドンとニューヨークを比較している。", "18年間の上演は否定的な出来事ではない。", "偶然上演されたのではない。", "ロンドンで長期上演されたのと同様、ニューヨークでも18年間続いた。"],
        "Similarly は二つの似た事実をつなぐ文副詞。after 以下はBroadwayでの初演時点を示す。",
        source_evidence=["it was still being performed there 21 years later", "it ran for 18 years there"],
    ),
]

rows_2b = [
    ("Andrew Lloyd Webber is famous for writing musicals, and many of the songs he has written have become famous.", "アンドルー・ロイド・ウェバーはミュージカル作曲で有名で、彼が書いた多くの歌も有名になっている。", "is / have become"),
    ("Over the last 50 years, Webber has created a number of popular musicals, including The Phantom of the Opera and Joseph and the Amazing Technicolor Dreamcoat.", "過去50年間、ウェバーは『オペラ座の怪人』や『ヨセフ・アンド・ザ・アメージング・テクニカラー・ドリームコート』など多くの人気ミュージカルを作った。", "has created"),
    ("The characters in these were taken from well-known stories that had been around for many years.", "これらの登場人物は、長年親しまれてきた有名な物語から取られていた。", "were taken"),
    ("One of Webber’s most successful musicals is Cats.", "ウェバーの最も成功したミュージカルの一つが『キャッツ』である。", "is"),
    ("This features the song “Memory,” the most popular one he has ever written.", "この作品には、彼が書いた中で最も人気の高い歌「メモリー」が登場する。", "features"),
    ("Like many of Webber’s other musicals, though, the characters in Cats were ( 24 ).", "しかし、ウェバーのほかの多くの作品と同様、『キャッツ』の登場人物は（24）。", "were"),
    ("As a child, one of Webber’s favorite books was Old Possum’s Book of Practical Cats by T. S. Eliot.", "子どものころ、ウェバーのお気に入りの本の一冊はT・S・エリオットの『キャッツ－ポッサムおじさんの猫とつき合う法』だった。", "was"),
    ("This is a collection of poems that describe ( 25 ).", "これは（25）を描いた詩集である。", "is / describe"),
    ("For example, one of the characters likes to be the focus of everyone’s attention.", "例えば、ある登場人物は皆の注目の的になるのが好きだ。", "likes"),
    ("Another seems to be lazy during the daytime, but at night, she secretly works hard to stop mice and insects from causing trouble.", "別の猫は昼は怠けているように見えるが、夜にはネズミや虫が問題を起こさないようひそかに懸命に働く。", "seems / works"),
    ("Webber used the words of these poems for the songs in his musical, and he created a world in which these cats live together.", "ウェバーはこれらの詩の言葉をミュージカルの歌に使い、猫たちが共に暮らす世界を作った。", "used / created"),
    ("Webber began work on Cats in 1977, and it had its first performance in London in 1981.", "ウェバーは1977年に『キャッツ』の制作を始め、1981年にロンドンで初演された。", "began / had"),
    ("It was so popular that it was still being performed there 21 years later.", "非常に人気があり、21年後もそこで上演され続けていた。", "was / was being performed"),
    ("( 26 ), after its first performance on Broadway in New York City in 1982, it ran for 18 years there.", "（26）、1982年にニューヨークのブロードウェイで初演された後、そこでも18年間上演された。", "ran"),
    ("Cats has become popular around the world.", "『キャッツ』は世界中で人気を得ている。", "has become"),
    ("In fact, the show has been translated into 15 languages, performed in over 30 countries, and seen by more than 73 million people.", "実際、15言語に翻訳され、30か国以上で上演され、7,300万人を超える人が観ている。", "has been translated / performed / seen"),
]

passage_2b = build_passage("B", "Performing Cats", [6, 5, 5], rows_2b, questions_2b)


questions_3a = [
    make_question(
        27, None, None,
        ["It was sent to him without an instruction manual.", "It has received some positive online reviews.", "He got it from his local Television Depot store.", "He chose it because it was in a recent sale."],
        ["説明書なしで送られた。", "好意的なオンライン評価をいくつか受けている。", "地元の店舗で買った。", "最近のセール品だったので選んだ。"],
        ["説明書を読み設定したので、説明書は付いていた。", "購入前に複数の高評価レビューを読んだと述べている。", "実店舗ではなく online store で購入した。", "セールを理由に選んだとは書かれていない。"],
        "現在完了 has received は、過去から現在までに受けた評価を表す。",
        question="What is one thing that Michael Green says about the TV that he bought?",
        question_translation="マイケル・グリーンが購入したテレビについて述べていることは何ですか。",
        source_evidence=["After reading several excellent reviews of the ZX950 LCD TV on the Internet"],
    ),
    make_question(
        28, None, None,
        ["The sound level cannot be changed with the remote control.", "The remote control uses up its batteries in just a few hours.", "The buttons on the TV do not seem to be working.", "The TV sometimes turns itself off unexpectedly."],
        ["リモコンで音量を変えられない。", "リモコンの電池が数時間で切れる。", "テレビ本体のボタンが動かないようだ。", "テレビが突然消えることがある。"],
        ["remote control では音量を調節できないと明記されている。", "電池を交換しても直らなかっただけで、電池消耗が速いとは書かれていない。", "本体のボタンでは音量を変えられる。", "電源が勝手に切れる問題ではない。"],
        "be unable to do / cannot be changed は不可能を表す。with は道具。",
        question="What problem does Michael Green say the TV has?",
        question_translation="テレビにどのような問題があるとマイケルは述べていますか。",
        source_evidence=["I was unable to adjust the volume of the TV with the remote control"],
    ),
    make_question(
        29, None, None,
        ["send someone to help him put the TV back into its box.", "solve the problem in time for him to watch a sports event.", "tell him about tournaments sponsored by Television Depot.", "give him instructions to allow him to fix the problem himself."],
        ["箱へ戻すのを手伝う人を送る。", "スポーツ大会を見るのに間に合うよう問題を解決する。", "店が協賛する大会を知らせる。", "自分で修理できる説明を与える。"],
        ["大きなテレビを箱へ戻したくないと述べている。", "next weekend のサッカー大会を見るため、数日以内の解決を望んでいる。", "大会は店の協賛イベントではない。", "交換リモコンまたは返品について尋ねており、自力修理の説明を求めてはいない。"],
        "in time for ... は「…に間に合って」。hope + S will ... に相当する内容を問う。",
        question="Michael Green hopes the customer service representative will",
        question_translation="マイケル・グリーンはカスタマーサービス担当者に何をしてほしいと望んでいますか。",
        source_evidence=["solve this problem in the next few days", "watch the European soccer tournament that begins next weekend"],
    ),
]

email_body_rows = [
    ("After reading several excellent reviews of the ZX950 LCD TV on the Internet, I purchased one from your Television Depot online store.", "インターネットでZX950液晶テレビの高評価レビューをいくつか読んだ後、Television Depotのオンラインストアで1台購入しました。", "purchased"),
    ("When the item arrived, it appeared to be in perfect condition, and I was able to set it up successfully by following the TV’s instruction manual.", "商品が届いたときは完全な状態に見え、テレビの説明書に従って問題なく設置できました。", "arrived / appeared / was able"),
    ("However, once I started using it, I noticed that there was a problem.", "しかし使い始めると、問題があることに気付きました。", "started / noticed"),
    ("I was unable to adjust the volume of the TV with the remote control.", "リモコンでテレビの音量を調節できませんでした。", "was unable"),
    ("I tried replacing the batteries in the remote control, but this did not fix the problem.", "リモコンの電池を交換してみましたが、問題は直りませんでした。", "tried / did not fix"),
    ("I looked through the instruction manual, but I could not find a solution.", "説明書を調べましたが、解決策を見つけられませんでした。", "looked / could not find"),
    ("Although I can adjust the volume with the buttons on the TV, I’m sure that you can understand how inconvenient it is to do it this way.", "テレビ本体のボタンでは音量を変えられますが、この方法がどれほど不便かお分かりいただけると思います。", "can adjust / am sure"),
    ("Would it be possible to obtain a replacement remote control, or do I need to return the TV, too?", "交換用リモコンを入手できますか。それともテレビも返品する必要がありますか。", "would be / do need"),
    ("It would be good if I don’t need to send it back because it will be difficult to put such a large TV back into its box.", "これほど大きなテレビを箱へ戻すのは難しいので、返品しなくてよければ助かります。", "would be / will be"),
    ("I hope you are able to solve this problem in the next few days.", "今後数日以内に問題を解決していただけることを願っています。", "hope / are able"),
    ("I would very much like to use my new TV to watch the European soccer tournament that begins next weekend.", "来週末に始まるヨーロッパのサッカー大会を新しいテレビでぜひ見たいです。", "would like"),
    ("I look forward to receiving your reply.", "ご返信をお待ちしております。", "look forward"),
]

passage_3a = {
    "label": "A",
    "title": "ZX950 LCD TV",
    "format": "email",
    "meta": {
        "from": "Michael Green <mikeyg4000@friendlymail.com>",
        "to": "Television Depot Customer Service <service@televisiondepot.com>",
        "date": "October 9",
        "subject": "ZX950 LCD TV",
    },
    "paragraphs": [
        "Dear Customer Service Representative,",
        " ".join(item[0] for item in email_body_rows[:3]),
        " ".join(item[0] for item in email_body_rows[3:7]),
        " ".join(item[0] for item in email_body_rows[7:]),
        "Regards,\nMichael Green",
    ],
    "translations": [
        "カスタマーサービスご担当者様",
        "".join(item[1] for item in email_body_rows[:3]),
        "".join(item[1] for item in email_body_rows[3:7]),
        "".join(item[1] for item in email_body_rows[7:]),
        "敬具\nマイケル・グリーン",
    ],
    "sentencePairs": [pair(*item) for item in email_body_rows],
    "questions": questions_3a,
}


questions_3b = [
    make_question(
        30, None, None,
        ["Its thin threads are over 20 times stronger than those of silk.", "It stopped Bangladesh from becoming a major exporter of clothes.", "Modern techniques have allowed factories to produce it cheaply.", "Many people say it is the best kind that there has ever been."],
        ["細糸は絹の20倍以上強い。", "バングラデシュが衣料輸出大国になるのを妨げた。", "現代技術で安く生産できる。", "史上最高の布だと多くの人が言う。"],
        ["価格が絹の20倍超であり、糸の強度ではない。", "現代の衣料輸出とは別に、過去の高級布を説明している。", "現代には生産が途絶えており、安価な大量生産品ではない。", "Many regard this cloth as the finest ever made と一致する。"],
        "regard A as B は「AをBと見なす」。the finest ever made は最上級＋過去分詞。",
        question="What is true of the cloth known as Dhaka muslin?",
        question_translation="ダッカ・モスリンとして知られる布について正しいことは何ですか。",
        source_evidence=["Many regard this cloth as the finest ever made"],
    ),
    make_question(
        31, None, None,
        ["Various colors were introduced to appeal to European customers.", "The price of Dhaka muslin in Europe increased dramatically.", "Makers began to use British techniques to make better cloth.", "Production of high-quality Dhaka muslin stopped completely."],
        ["欧州向けに多彩な色を導入した。", "欧州で価格が急上昇した。", "英国技術でよりよい布を作り始めた。", "高品質ダッカ・モスリンの生産が完全に止まった。"],
        ["色についての要求は述べられていない。", "要求は低価格化であり、値上がりではない。", "英国技術を採用したのではなく、低品質化か廃業を選んだ。", "作り手全員が低品質品へ移るかやめたため、高品質品の生産は途絶えた。"],
        "as a result of ... は「…の結果」。either A or B が全製作者の二つの選択を示す。",
        question="What happened as a result of the demands made by British traders?",
        question_translation="英国商人の要求の結果、何が起きましたか。",
        source_evidence=["all the makers decided to either produce lower-quality types of cloth or quit"],
    ),
    make_question(
        32, None, None,
        ["to find plants like the ones that were used to make Dhaka muslin.", "to check whether samples of Dhaka muslin were genuine or fake.", "to explain the evolution of Dhaka muslin at an exhibition.", "to create artificial Dhaka muslin in a laboratory in London."],
        ["原料植物に似た植物を見つけるため。", "布見本が本物か偽物か調べるため。", "展示会で布の進化を説明するため。", "ロンドンの研究室で人工布を作るため。"],
        ["乾燥葉のDNAから、原料植物とほぼ同じ種を見つけた。", "布そのものの鑑定には使っていない。", "展示会後の再現研究で使ったので、進化説明のためではない。", "人工布を研究室で合成したのではなく、近縁植物を探した。"],
        "using ... は手段を表す分詞句。the ones は phuti karpas plants を指す。",
        question="Saiful Islam used the DNA from some phuti karpas leaves",
        question_translation="サイフル・イスラムはphuti karpasの葉のDNAを何のために使いましたか。",
        source_evidence=["using the DNA from some dried leaves of phuti karpas from a museum, he was able to find a species that was almost the same"],
    ),
    make_question(
        33, None, None,
        ["It wants to make the country famous for producing high-quality cloth.", "It believes that his project will create new jobs for Bangladeshis.", "Because he will quit unless he gets additional financial support.", "Because he may discover a way to produce cheap clothes more easily."],
        ["高品質布の生産国として有名にしたい。", "新しい雇用が生まれると考えている。", "追加資金がなければ彼がやめるから。", "安い服を容易に作る方法を発見しそうだから。"],
        ["the finest cloth の生産国として知られたいという政府の目的に一致する。", "雇用創出は本文にない。", "イスラムが辞める条件は述べられていない。", "安価な服ではなく最高品質の布の復活を目指している。"],
        "want O to be known as ... は「Oが…として知られることを望む」。",
        question="Why is the government of Bangladesh supporting Islam’s efforts?",
        question_translation="なぜバングラデシュ政府はイスラムの取り組みを支援していますか。",
        source_evidence=["it wants the country to be known as the producer of the finest cloth in the world"],
    ),
]

rows_3b = [
    ("The Asian country of Bangladesh is one of the largest exporters of clothes in the world.", "アジアの国バングラデシュは、世界最大級の衣料輸出国の一つである。", "is"),
    ("Low wages and modern techniques have allowed clothing factories in Bangladesh to produce cheap clothes.", "低賃金と現代技術により、バングラデシュの衣料工場は安い服を生産できるようになった。", "have allowed"),
    ("However, until the 19th century, the country produced a luxury cloth called Dhaka muslin.", "しかし19世紀まで、この国はダッカ・モスリンという高級布を生産していた。", "produced"),
    ("Many regard this cloth as the finest ever made, and it cost over 20 times more than the best silk.", "多くの人はこの布を史上最高と見なし、最高級の絹の20倍を超える値段だった。", "regard / cost"),
    ("It was produced from cotton from a plant called phuti karpas.", "それはphuti karpasという植物の綿から作られた。", "was produced"),
    ("This kind of cotton can be made into very thin threads, which can be used to make incredibly soft and light cloth.", "この綿は非常に細い糸にでき、その糸で驚くほど柔らかく軽い布を作れる。", "can be made / can be used"),
    ("Dhaka muslin was difficult to make, but wealthy people were happy to pay the high prices demanded by the makers.", "ダッカ・モスリンは作るのが難しかったが、裕福な人々は作り手が求める高値を喜んで払った。", "was / were"),
    ("The fame of this cloth spread to Europe, and the wife of Emperor Napoleon of France loved to wear dresses made from Dhaka muslin.", "この布の名声は欧州へ広がり、フランス皇帝ナポレオンの妻はダッカ・モスリンのドレスを好んだ。", "spread / loved"),
    ("When the area that includes Bangladesh became part of the British Empire, though, British traders put pressure on the makers of Dhaka muslin to produce more cloth at lower prices.", "しかしバングラデシュを含む地域が大英帝国の一部になると、英国商人は作り手に、より安く多く作るよう圧力をかけた。", "became / put"),
    ("Eventually, all the makers decided to either produce lower-quality types of cloth or quit.", "最終的に作り手は全員、低品質の布を作るか廃業するかを選んだ。", "decided"),
    ("In 2013, Saiful Islam, a Bangladeshi man living in London, was asked to organize an exhibition about Dhaka muslin.", "2013年、ロンドン在住のバングラデシュ人サイフル・イスラムはダッカ・モスリン展の企画を依頼された。", "was asked"),
    ("Islam was amazed by the high quality of this material.", "イスラムはこの素材の高品質に驚いた。", "was amazed"),
    ("He wondered if it would be possible to produce Dhaka muslin again.", "彼はダッカ・モスリンを再び作れるだろうかと考えた。", "wondered"),
    ("Sadly, he could not find any phuti karpas plants in Bangladesh.", "残念ながら、バングラデシュではphuti karpasを見つけられなかった。", "could not find"),
    ("However, using the DNA from some dried leaves of phuti karpas from a museum, he was able to find a species that was almost the same.", "しかし博物館の乾燥葉のDNAを使い、ほぼ同じ種を見つけられた。", "was able"),
    ("Islam harvested cotton from plants of this species, but the threads he made were too thin and broke easily.", "イスラムはこの種から綿を採ったが、作った糸は細すぎて簡単に切れた。", "harvested / were / broke"),
    ("He had to mix the cotton with some from other plants.", "彼はその綿をほかの植物の綿と混ぜなければならなかった。", "had to mix"),
    ("The threads made from this mixture, though, were still much thinner than normal.", "それでも混合綿の糸は普通よりはるかに細かった。", "were"),
    ("After a lot of hard work, Islam and his team produced some cloth that was almost as good as Dhaka muslin.", "多大な努力の末、イスラムらはダッカ・モスリンにほぼ匹敵する布を作った。", "produced"),
    ("He wants to keep improving the production technique.", "彼は生産技術を改良し続けたいと考えている。", "wants"),
    ("The government of Bangladesh is supporting him because it wants the country to be known as the producer of the finest cloth in the world.", "バングラデシュ政府は、世界最高の布の生産国として国を知らしめたいので彼を支援している。", "is supporting / wants"),
]

passage_3b = build_passage("B", "The Empress’s Favorite Clothes", [6, 4, 5, 6], rows_3b, questions_3b)


questions_3c = [
    make_question(
        34, None, None,
        ["They used to protect the border between Mexico and the United States.", "They lived in small communities and kept farms in a dry area.", "They ate wild plants and animals instead of growing their own food.", "They were forced to leave their homes and live in the Sonoran Desert."],
        ["米墨国境を守っていた。", "乾燥地の小共同体で農業をして暮らした。", "作物を育てず野生動植物だけを食べた。", "故郷を離れ砂漠に住むよう強制された。"],
        ["国境付近に住んだが、国境警備についてはない。", "villages に住み、乾燥した砂漠で作物を育てたとある。", "作物も育て、野生の食べ物も利用した。", "政府が強制したのは生活様式の変更で、砂漠への移住ではない。"],
        "used to do は過去の習慣。keep farms は選択肢で grow crops を言い換えている。",
        question="What is true about the Tohono O’odham people of North America?",
        question_translation="北米のトホノ・オーダムの人々について正しいことは何ですか。",
        source_evidence=["lived in villages and grew crops such as beans, corn, and melons"],
    ),
    make_question(
        35, None, None,
        ["The sunshine in the area means that some plants can actually grow better there.", "The Sonoran Desert gets enough rain twice a year to allow the plants to grow.", "There are few human beings or wild animals living in the region that eat them.", "There is one kind of soil in the desert that almost any plant can grow in."],
        ["日光で一部の植物がよく育つ。", "年2回、植物が育つだけの雨が降る。", "植物を食べる人や動物が少ない。", "ほぼ全植物が育つ一種類の土がある。"],
        ["日光の量は二つの理由に含まれていない。", "冬と夏に一度ずつ降る雨が一部の植物の生存に十分だとある。", "捕食者の少なさでは説明されていない。", "一種類ではなく、さまざまな種類の土が多様性を支える。"],
        "enough + 名詞 + to do は「…するのに十分な名詞」。allow A to do は「Aが…するのを可能にする」。",
        question="What is one reason that over 2,000 different types of plants can survive in the Sonoran Desert?",
        question_translation="ソノラ砂漠で2,000種を超える植物が生きられる理由の一つは何ですか。",
        source_evidence=["it rains a couple of times each year—once in the winter and once in the summer", "This rain is enough for some kinds of plants to survive"],
    ),
    make_question(
        36, None, None,
        ["produces fruit that the local people have enjoyed for a long time.", "was discovered by the Tohono O’odham people about 200 years ago.", "has roots that grow 15 meters below the ground to reach water.", "is best to eat with a special sauce made from traditional wine."],
        ["地元の人が長年親しむ実をつける。", "約200年前に発見された。", "地下15メートルまで根を伸ばす。", "伝統的なワインのソースで食べるのが最適だ。"],
        ["saguaro fruit は長年お気に入りの食べ物だった。", "200年はサボテンの寿命で、発見時期ではない。", "15メートルは高さで、根の深さではない。", "実からソースやワインを作れるのであり、ワイン製ソースで食べるとはない。"],
        "have enjoyed は現在完了で、長期間続く好みを表す。that は fruit を修飾する。",
        question="The saguaro cactus",
        question_translation="サワロサボテンは",
        source_evidence=["This fruit—the saguaro fruit—has long been a favorite food of the Tohono O’odham people"],
    ),
    make_question(
        37, None, None,
        ["The U.S. government wanted them to behave more like other U.S. citizens.", "The U.S. government offered them opportunities to travel overseas to study.", "They wanted their children to study English so that they could enter good schools.", "They lost their independence after a war that took place in the early 20th century."],
        ["米政府がほかの米国民のようにさせたかった。", "米政府が海外留学の機会を与えた。", "よい学校へ入るため英語を学ばせたかった。", "20世紀初頭の戦争後に独立を失った。"],
        ["政府は学校で英語を学ばせ、固有文化を忘れさせ、生活様式を変えようとした。", "海外留学についてはない。", "子どもや家族の希望ではなく、政府が強制した。", "戦争で独立を失ったとは述べられていない。"],
        "force A to do / make A do は使役。forget their own culture が同化政策を示す。",
        question="Why did many Tohono O’odham people stop following their traditions?",
        question_translation="なぜ多くのトホノ・オーダムの人々は伝統に従わなくなったのですか。",
        source_evidence=["the U.S. government forced them to change their lifestyle", "make them learn English and forget their own culture"],
    ),
    make_question(
        38, None, None,
        ["The method of collecting saguaro fruit is endangering the plants that it grows on.", "The name of the Tohono O’odham tribe comes from its people’s favorite food.", "The soil in the Sonoran Desert is different in the winter and in the summer.", "The Tohono O’odham people have a tradition of collecting fruit in family groups."],
        ["採集法が植物を危険にさらす。", "部族名は好物に由来する。", "土壌は冬と夏で異なる。", "家族単位で実を採集する伝統がある。"],
        ["実を落として集めるが、サボテンを危険にするとはない。", "部族名は「砂漠の人々」を意味し、食べ物由来ではない。", "土の種類は多いが、季節で変わるとはない。", "families work together to knock it down and collect it と一致する。"],
        "have a tradition of doing は「…する伝統がある」。family groups は families work together の言い換え。",
        question="Which of the following statements is true?",
        question_translation="次の記述のうち正しいものはどれですか。",
        source_evidence=["families work together to knock it down from the cactuses and collect it"],
    ),
]

rows_3c = [
    ("The Tohono O’odham people are Native Americans who come from the Sonoran Desert.", "トホノ・オーダムの人々はソノラ砂漠出身の先住民である。", "are / come"),
    ("In fact, the name of this tribe means “desert people” in their own language.", "実際、この部族名は彼らの言語で「砂漠の人々」を意味する。", "means"),
    ("The Sonoran Desert lies around the border between the United States and Mexico.", "ソノラ砂漠は米国とメキシコの国境周辺にある。", "lies"),
    ("Traditionally, the Tohono O’odham people lived in villages and grew crops such as beans, corn, and melons.", "伝統的に、彼らは村に住み、豆・トウモロコシ・メロンなどを育てた。", "lived / grew"),
    ("They also ate some of the wild plants and animals that are found in the desert.", "砂漠にいる野生の植物や動物も食べた。", "ate"),
    ("Although the Sonoran Desert is hot and dry, it has over 2,000 different species of plants.", "ソノラ砂漠は暑く乾燥しているが、2,000種を超える植物がある。", "is / has"),
    ("Hundreds of these plants are safe for people to eat.", "そのうち数百種は人が安全に食べられる。", "are"),
    ("There are two reasons why the Sonoran Desert has so many species of plants.", "ソノラ砂漠に多くの植物種がある理由は二つある。", "are / has"),
    ("One is that it contains a variety of types of soil, and these support the growth of many kinds of plants.", "一つは多様な種類の土があり、それが多くの植物の成長を支えることだ。", "is / contains / support"),
    ("The other is that, although the desert is mostly dry, it rains a couple of times each year—once in the winter and once in the summer.", "もう一つは、ほぼ乾燥しているものの、毎年冬と夏に一度ずつ雨が降ることだ。", "is / rains"),
    ("This rain is enough for some kinds of plants to survive.", "この雨は一部の植物が生き残るのに十分である。", "is"),
    ("One desert plant, the saguaro cactus, is especially important to the people of the Tohono O’odham tribe.", "砂漠植物の一つ、サワロサボテンはトホノ・オーダムの人々に特に重要だ。", "is"),
    ("Saguaro cactuses can live for over 200 years and grow more than 15 meters tall.", "サワロサボテンは200年以上生き、高さ15メートル超に育つ。", "can live / grow"),
    ("Once a year, around June, they produce red fruit.", "年に一度、6月ごろ赤い実をつける。", "produce"),
    ("This fruit—the saguaro fruit—has long been a favorite food of the Tohono O’odham people.", "この実、つまりサワロの実は長年彼らのお気に入りの食べ物である。", "has been"),
    ("When the fruit is ready to eat, families work together to knock it down from the cactuses and collect it.", "実が熟すと家族で協力し、サボテンから落として集める。", "is / work"),
    ("The fruit is sweet and delicious when it is fresh, and it can also be turned into sauce or wine so that it can be stored for long periods.", "新鮮な実は甘くおいしく、長期保存できるようソースやワインにも加工できる。", "is / can be turned"),
    ("The people of the Tohono O’odham tribe were very independent, and for a long time, they fought to keep their traditional way of life.", "彼らは非常に自立しており、長い間、伝統的生活を守るため戦った。", "were / fought"),
    ("However, in the early 20th century, the U.S. government forced them to change their lifestyle.", "しかし20世紀初頭、米国政府は生活様式を変えるよう強制した。", "forced"),
    ("It sent Tohono O’odham children to schools to make them learn English and forget their own culture.", "政府は子どもたちを学校へ送り、英語を学ばせ、自文化を忘れさせた。", "sent / make"),
    ("Many stopped following their traditional way of life.", "多くの人が伝統的生活に従わなくなった。", "stopped"),
    ("Recently, though, some Tohono O’odham people have begun bringing back their tribe’s endangered traditions, including collecting and eating saguaro fruit.", "しかし近年、一部の人々は、サワロの実を採集して食べることを含む、失われかけた伝統を復活させ始めている。", "have begun"),
]

passage_3c = build_passage("C", "Desert Delight", [5, 6, 6, 5], rows_3c, questions_3c)


vocab_rows = [
    ("remarkably", "著しく、驚くほど", "副詞", "Part 1 Q1", "Keiko gave a remarkably good presentation.", "ケイコは驚くほど上手な発表をした。"),
    ("marvelous", "すばらしい", "形容詞", "Part 1 Q2", "We had a marvelous vacation.", "私たちはすばらしい休暇を過ごした。"),
    ("conflict", "対立、紛争", "名詞", "Part 1 Q3", "The conflict between the countries may cause a war.", "両国間の対立が戦争を引き起こすかもしれない。"),
    ("surgery", "手術", "名詞", "Part 1 Q4", "He had surgery on his right knee.", "彼は右ひざの手術を受けた。"),
    ("reputation", "評判、名声", "名詞", "Part 1 Q5", "The restaurant lost its good reputation.", "その店はよい評判を失った。"),
    ("expose", "さらす", "動詞", "Part 1 Q6", "Do not expose your skin to too much sunlight.", "肌を過度の日光にさらしてはいけない。"),
    ("heal", "治る、治す", "動詞", "Part 1 Q7", "His broken arm took three months to heal.", "彼の骨折は治るのに3か月かかった。"),
    ("flexibility", "柔軟性", "名詞", "Part 1 Q8", "Working from home gives employees flexibility.", "在宅勤務は従業員に柔軟性を与える。"),
    ("abandon", "放棄する、置き去りにする", "動詞", "Part 1 Q9", "He had to abandon his car in the snowstorm.", "彼は吹雪の中で車を置き去りにしなければならなかった。"),
    ("eliminate", "敗退させる、除外する", "動詞", "Part 1 Q10", "Laura was eliminated from the tournament.", "ローラは大会で敗退した。"),
    ("refrain from", "…を控える", "熟語", "Part 1 Q11", "Sarah must refrain from running.", "サラは走るのを控えなければならない。"),
    ("as a whole", "全体として", "熟語", "Part 1 Q12", "As a whole, I enjoyed the movie.", "全体として、その映画を楽しんだ。"),
    ("make a fool of", "…を笑いものにする", "熟語", "Part 1 Q13", "Jim made a fool of Emily.", "ジムはエミリーを笑いものにした。"),
    ("interfere with", "…に干渉する、妨げる", "熟語", "Part 1 Q14", "Do not interfere with his personal life.", "彼の私生活に干渉してはいけない。"),
    ("call off", "中止する", "熟語", "Part 1 Q15", "They called off the barbecue because of rain.", "彼らは雨のためバーベキューを中止した。"),
    ("by means of", "…を使って、…によって", "熟語", "Part 1 Q16", "The thief entered by means of a ladder.", "泥棒ははしごを使って入った。"),
    ("in vain", "無駄に、効果なく", "熟語", "Part 1 Q17", "His efforts to train the cat were in vain.", "猫を訓練する努力は無駄だった。"),
    ("having done", "…したので、…した後で", "文法表現", "Part 1 Q18", "Having lived in Tokyo, she knew the city well.", "東京に住んだことがあったので、彼女は街をよく知っていた。"),
    ("as if", "まるで…であるかのように", "接続詞", "Part 1 Q19", "They looked at her as if she had done it.", "彼らはまるで彼女がしたかのように見た。"),
    ("There is no telling", "予測できない、分からない", "文法表現", "Part 1 Q20", "There is no telling how long the trip will take.", "旅にどれだけかかるか分からない。"),
    ("a wide variety of", "多種多様な", "熟語", "Part 2A", "Plastic is used in a wide variety of goods.", "プラスチックは多種多様な製品に使われる。"),
    ("be estimated", "推定される", "熟語", "Part 2A", "It is estimated that 400 million tons of plastic is produced each year.", "毎年4億トンのプラスチックが生産されると推定される。"),
    ("landfill site", "埋立地", "名詞", "Part 2A", "Most waste is buried in landfill sites.", "大部分のごみは埋立地に埋められる。"),
    ("end up", "結局…になる、行き着く", "熟語", "Part 2A", "A large amount ends up in the ocean.", "大量のごみが結局海へ流れ込む。"),
    ("break down", "分解する、壊れる", "熟語", "Part 2A", "Plastic takes a long time to break down.", "プラスチックは分解に長い時間がかかる。"),
    ("get trapped", "閉じ込められる、絡まる", "熟語", "Part 2A", "Animals get trapped by plastic.", "動物がプラスチックに絡まる。"),
    ("be unable to", "…することができない", "熟語", "Part 2A", "The animals are unable to swim freely.", "動物は自由に泳げない。"),
    ("two-thirds", "3分の2", "数詞", "Part 2A", "About two-thirds of fish species were studied.", "魚類の約3分の2の種が調査された。"),
    ("in response", "これを受けて、それに応じて", "熟語", "Part 2A", "In response, organizations asked for new laws.", "これを受け、団体は新法を求めた。"),
    ("make efforts", "努力する", "熟語", "Part 2A", "Groups are making efforts to reduce pollution.", "団体は汚染を減らそうと努力している。"),
    ("for instance", "例えば", "熟語", "Part 2A", "For instance, the center asked for laws.", "例えば、そのセンターは法律を求めた。"),
    ("educate the public", "一般の人々を啓発する", "熟語", "Part 2A", "The groups educate the public about plastic.", "団体はプラスチックについて市民を啓発する。"),
    ("in spite of", "…にもかかわらず", "熟語", "Part 2A", "In spite of these efforts, the waste increased.", "こうした努力にもかかわらず、ごみは増えた。"),
    ("pollution", "汚染", "名詞", "Part 2A", "New laws could control plastic pollution.", "新法でプラスチック汚染を規制できる。"),
    ("wildlife", "野生生物", "名詞", "Part 2A", "Plastic causes problems for wildlife.", "プラスチックは野生生物に問題を起こす。"),
    ("musical", "ミュージカル", "名詞", "Part 2B", "Cats is a successful musical.", "『キャッツ』は成功したミュージカルだ。"),
    ("be famous for", "…で有名である", "熟語", "Part 2B", "Webber is famous for writing musicals.", "ウェバーはミュージカル作曲で有名だ。"),
    ("a number of", "多くの、いくつかの", "熟語", "Part 2B", "He created a number of popular musicals.", "彼は多くの人気ミュージカルを作った。"),
    ("well-known", "よく知られた、有名な", "形容詞", "Part 2B", "The characters came from well-known stories.", "登場人物は有名な物語から取られた。"),
    ("feature", "特色として含む、登場させる", "動詞", "Part 2B", "Cats features the song Memory.", "『キャッツ』には「メモリー」が登場する。"),
    ("collection", "収集物、作品集", "名詞", "Part 2B", "The book is a collection of poems.", "その本は詩集である。"),
    ("attention", "注目、注意", "名詞", "Part 2B", "The cat likes to be the focus of attention.", "その猫は注目の的になるのが好きだ。"),
    ("secretly", "ひそかに", "副詞", "Part 2B", "The cat secretly works at night.", "その猫は夜ひそかに働く。"),
    ("translate into", "…に翻訳する", "熟語", "Part 2B", "The show has been translated into 15 languages.", "その作品は15言語に翻訳された。"),
    ("performance", "上演、公演、演技", "名詞", "Part 2B", "Its first performance was in London.", "初演はロンドンだった。"),
    ("review", "批評、レビュー", "名詞", "Part 3A", "Michael read several excellent reviews.", "マイケルはいくつかの高評価レビューを読んだ。"),
    ("set up", "設置する、準備する", "熟語", "Part 3A", "He set up the TV successfully.", "彼はテレビを問題なく設置した。"),
    ("adjust", "調節する", "動詞", "Part 3A", "He could not adjust the volume.", "彼は音量を調節できなかった。"),
    ("remote control", "リモコン", "名詞", "Part 3A", "The remote control did not change the volume.", "リモコンでは音量が変わらなかった。"),
    ("replace", "交換する、取り替える", "動詞", "Part 3A", "He replaced the batteries.", "彼は電池を交換した。"),
    ("inconvenient", "不便な", "形容詞", "Part 3A", "Using the TV buttons was inconvenient.", "テレビ本体のボタンを使うのは不便だった。"),
    ("obtain", "入手する", "動詞", "Part 3A", "He wanted to obtain a replacement remote.", "彼は交換用リモコンを入手したかった。"),
    ("exporter", "輸出業者、輸出国", "名詞", "Part 3B", "Bangladesh is a major exporter of clothes.", "バングラデシュは主要な衣料輸出国だ。"),
    ("luxury", "高級な、ぜいたく品", "名詞・形容詞", "Part 3B", "Dhaka muslin was a luxury cloth.", "ダッカ・モスリンは高級布だった。"),
    ("regard A as B", "AをBと見なす", "熟語", "Part 3B", "Many regard the cloth as the finest ever made.", "多くの人はその布を史上最高と見なす。"),
    ("demand", "要求する、要求", "動詞・名詞", "Part 3B", "The makers demanded high prices.", "作り手は高値を求めた。"),
    ("put pressure on", "…に圧力をかける", "熟語", "Part 3B", "British traders put pressure on the makers.", "英国商人は作り手に圧力をかけた。"),
    ("exhibition", "展覧会、展示", "名詞", "Part 3B", "Islam organized an exhibition about Dhaka muslin.", "イスラムはダッカ・モスリン展を企画した。"),
    ("species", "（生物の）種", "名詞", "Part 3B", "He found a similar plant species.", "彼は似た植物種を見つけた。"),
    ("production technique", "生産技術", "名詞", "Part 3B", "He wants to improve the production technique.", "彼は生産技術を改良したい。"),
    ("Native American", "アメリカ先住民", "名詞", "Part 3C", "The Tohono O’odham are Native Americans.", "トホノ・オーダムはアメリカ先住民だ。"),
    ("tribe", "部族", "名詞", "Part 3C", "The tribe’s name means desert people.", "その部族名は「砂漠の人々」を意味する。"),
    ("soil", "土、土壌", "名詞", "Part 3C", "The desert contains several types of soil.", "その砂漠には複数種類の土がある。"),
    ("saguaro cactus", "サワロサボテン", "名詞", "Part 3C", "The saguaro cactus produces red fruit.", "サワロサボテンは赤い実をつける。"),
    ("endangered", "危機にさらされた、絶滅の恐れがある", "形容詞", "Part 3C", "They are bringing back endangered traditions.", "彼らは失われかけた伝統を復活させている。"),
]

DISTRACTOR_POOL = [
    "増加させる", "静かな", "許可", "不足している", "伝統的な",
    "偶然に", "保護", "柔らかい", "費用", "急いで", "拒否する", "似ている",
]


def make_distractors(index, meaning):
    values = []
    cursor = index % len(DISTRACTOR_POOL)
    while len(values) < 3:
        candidate = DISTRACTOR_POOL[cursor % len(DISTRACTOR_POOL)]
        cursor += 1
        if candidate != meaning and candidate not in values:
            values.append(candidate)
    return values


vocabulary = []
for index, (word, meaning, pos, source, example, example_ja) in enumerate(vocab_rows, 1):
    slug = re.sub(r"[^a-zA-Z0-9_]", "_", word.lower()).strip("_")
    vocabulary.append({
        "word": word,
        "meaning": meaning,
        "pos": pos,
        "level": "2級",
        "source": source,
        "example": example,
        "exampleJa": example_ja,
        "distractors": make_distractors(index, meaning),
        "wordAudio": f"audio/vocab/w_{index:03d}_{slug}.mp3",
    })


focus_points = [
    {
        "id": "fp1",
        "title": "It is estimated that ...（…と推定される）",
        "subtitle": "Reporting Passive",
        "explanation": "It is estimated that S V は、推定の情報源を前面に出さず客観的に数値を示す受動表現である。本文では生産量を示し、続く海洋流出量との規模比較につながる。",
        "sourceQuote": "it is estimated that about 400 million tons of plastic is produced",
        "sourceLocation": "Part 2A",
        "examples": [
            {"en": "It is estimated that 400 million tons of plastic is produced each year.", "ja": "毎年4億トンのプラスチックが生産されると推定されている。", "note": "It は形式主語。"},
            {"en": "It is believed that the problem will get worse.", "ja": "問題は悪化すると考えられている。", "note": "believe にも同じ型を使える。"},
            {"en": "About 14 million tons is said to enter the ocean.", "ja": "約1,400万トンが海へ入ると言われている。", "note": "S is said to do への書き換え。"},
        ],
        "practicePassage": {
            "en": "[Source: Trouble at Sea]\nPlastic is used in a wide variety of goods. In fact, it is estimated that about 400 million tons of plastic is produced around the world each year. More than 14 million tons of plastic waste goes into the ocean each year.",
            "ja": "プラスチックは多種多様な製品に使われている。実際、毎年世界で約4億トンが生産されると推定され、そのうち1,400万トン超のごみが海へ入る。",
            "audioFile": "audio/practice_pp1.mp3",
        },
        "practiceQuestions": [
            {"q": "It is estimated that の It は何ですか。", "a": "that節を受ける形式主語です。"},
            {"q": "推定されている年間生産量はいくらですか。", "a": "約4億トンです。"},
            {"q": "is produced は何態ですか。", "a": "受動態です。"},
            {"q": "about は数値の前でどう訳しますか。", "a": "「約」と訳します。"},
        ],
        "highlightPatterns": ["it is estimated that", "is produced around the world"],
        "highlightColor": "#2563EB",
        "highlightLabel": "reporting passive",
    },
    {
        "id": "fp2",
        "title": "get trapped / be unable to（被害と結果）",
        "subtitle": "Change-of-state Passive",
        "explanation": "get + 過去分詞は状態変化を強調する。get trapped（絡まって動けなくなる）に、be unable to swim（泳げない）が続き、原因から結果を一続きで読める。",
        "sourceQuote": "animals sometimes get trapped by larger pieces of plastic",
        "sourceLocation": "Part 2A",
        "examples": [
            {"en": "Animals get trapped by larger pieces of plastic.", "ja": "動物は大きなプラスチック片に絡まる。", "note": "get が状態変化を示す。"},
            {"en": "They are unable to swim freely.", "ja": "動物は自由に泳げない。", "note": "be unable to = cannot。"},
            {"en": "Plastic takes a long time to break down.", "ja": "プラスチックは分解に長い時間がかかる。", "note": "take time to do。"},
        ],
        "practicePassage": {
            "en": "[Source: Trouble at Sea]\nFirst, animals sometimes get trapped by larger pieces of plastic and die because they are unable to swim freely. Plastic is strong and takes a long time to break down.",
            "ja": "第一に、動物は大きなプラスチック片に絡まり、自由に泳げないため死ぬことがある。プラスチックは丈夫で分解に長い時間がかかる。",
            "audioFile": "audio/practice_pp2.mp3",
        },
        "practiceQuestions": [
            {"q": "動物は何によって get trapped しますか。", "a": "larger pieces of plastic です。"},
            {"q": "be unable to swim を一語で書き換えると何ですか。", "a": "cannot swim です。"},
            {"q": "because 以下は何を示しますか。", "a": "動物が死ぬ理由を示します。"},
            {"q": "break down は本文でどんな意味ですか。", "a": "「分解する」です。"},
        ],
        "highlightPatterns": ["get trapped", "are unable to swim", "takes a long time to break down"],
        "highlightColor": "#DC2626",
        "highlightLabel": "cause and result",
    },
    {
        "id": "fp3",
        "title": "has been translated, performed, and seen",
        "subtitle": "Present Perfect Passive in Parallel",
        "explanation": "現在完了受動態 has been + 過去分詞が、翻訳・上演・鑑賞という三つの実績を並列で示す。二つ目以降では has been が省略され、同じ文法構造を共有する。",
        "sourceQuote": "has been translated into 15 languages, performed in over 30 countries, and seen by more than 73 million people",
        "sourceLocation": "Part 2B",
        "examples": [
            {"en": "The show has been translated into 15 languages.", "ja": "その作品は15言語に翻訳されている。", "note": "現在完了の受動態。"},
            {"en": "It has been performed in over 30 countries.", "ja": "30か国以上で上演されている。", "note": "場所は in で示す。"},
            {"en": "It has been seen by more than 73 million people.", "ja": "7,300万人を超える人が観ている。", "note": "行為者は by で示す。"},
        ],
        "practicePassage": {
            "en": "[Source: Performing Cats]\nCats has become popular around the world. In fact, the show has been translated into 15 languages, performed in over 30 countries, and seen by more than 73 million people.",
            "ja": "『キャッツ』は世界中で人気を得ている。実際、15言語に翻訳され、30か国以上で上演され、7,300万人超が観ている。",
            "audioFile": "audio/practice_pp3.mp3",
        },
        "practiceQuestions": [
            {"q": "has been translated は何態・何時制ですか。", "a": "現在完了の受動態です。"},
            {"q": "performed の前に省略されている語は何ですか。", "a": "has been です。"},
            {"q": "何言語に翻訳されましたか。", "a": "15言語です。"},
            {"q": "seen by の by は何を示しますか。", "a": "作品を見た行為者を示します。"},
        ],
        "highlightPatterns": ["has been translated", "performed in over 30 countries", "seen by more than 73 million people"],
        "highlightColor": "#7C3AED",
        "highlightLabel": "perfect passive",
    },
    {
        "id": "fp4",
        "title": "Would it be possible to ...（丁寧な依頼）",
        "subtitle": "Polite Email Requests",
        "explanation": "Would it be possible to do? は可能かどうかを遠回しに尋ねる丁寧な依頼。would like to、look forward to doing と合わせ、苦情メールでも落ち着いた依頼表現を作る。",
        "sourceQuote": "Would it be possible to obtain a replacement remote control",
        "sourceLocation": "Part 3A",
        "examples": [
            {"en": "Would it be possible to obtain a replacement?", "ja": "交換品を入手することは可能でしょうか。", "note": "丁寧に可能性を尋ねる。"},
            {"en": "I would very much like to use my new TV.", "ja": "新しいテレビをぜひ使いたいです。", "note": "want より丁寧。"},
            {"en": "I look forward to receiving your reply.", "ja": "ご返信をお待ちしております。", "note": "to は前置詞なので動名詞。"},
        ],
        "practicePassage": {
            "en": "[Source: ZX950 LCD TV]\nWould it be possible to obtain a replacement remote control, or do I need to return the TV, too? I hope you are able to solve this problem in the next few days. I look forward to receiving your reply.",
            "ja": "交換用リモコンを入手できますか。それともテレビも返品する必要がありますか。数日以内の解決を願っています。ご返信をお待ちしております。",
            "audioFile": "audio/practice_pp4.mp3",
        },
        "practiceQuestions": [
            {"q": "依頼している品物は何ですか。", "a": "a replacement remote control です。"},
            {"q": "Would it be possible to の後は何形ですか。", "a": "動詞の原形です。"},
            {"q": "look forward to の後で receiving になる理由は何ですか。", "a": "to が前置詞だからです。"},
            {"q": "問題解決を望む期限はいつですか。", "a": "in the next few days です。"},
        ],
        "highlightPatterns": ["Would it be possible to", "would very much like to", "look forward to receiving"],
        "highlightColor": "#059669",
        "highlightLabel": "polite request",
    },
    {
        "id": "fp5",
        "title": "force A to do / make A do（強制の使役）",
        "subtitle": "Causative Structures",
        "explanation": "force A to do はto不定詞、make A do は原形不定詞を取る。本文では政府が生活様式を変えさせ、子どもに英語を学ばせ文化を忘れさせた二段階の強制を表す。",
        "sourceQuote": "forced them to change their lifestyle",
        "sourceLocation": "Part 3C",
        "examples": [
            {"en": "The government forced them to change their lifestyle.", "ja": "政府は彼らに生活様式を変えるよう強制した。", "note": "force A to do。"},
            {"en": "It made the children learn English.", "ja": "政府は子どもたちに英語を学ばせた。", "note": "make A do。"},
            {"en": "Some people have begun bringing back their traditions.", "ja": "一部の人々は伝統を復活させ始めている。", "note": "begin doing と現在完了。"},
        ],
        "practicePassage": {
            "en": "[Source: Desert Delight]\nThe U.S. government forced them to change their lifestyle. It sent Tohono O’odham children to schools to make them learn English and forget their own culture. Recently, some people have begun bringing back their tribe’s endangered traditions.",
            "ja": "米国政府は彼らに生活様式を変えるよう強制し、子どもを学校へ送って英語を学ばせ、自文化を忘れさせた。近年、一部の人々は失われかけた伝統を復活させ始めている。",
            "audioFile": "audio/practice_pp5.mp3",
        },
        "practiceQuestions": [
            {"q": "force の後で change の前に必要な語は何ですか。", "a": "to です。"},
            {"q": "make them learn で learn が原形なのはなぜですか。", "a": "使役動詞 make は目的語の後に原形不定詞を取るからです。"},
            {"q": "forget の目的語は何ですか。", "a": "their own culture です。"},
            {"q": "have begun bringing back は何を表しますか。", "a": "近年始まり、現在につながる伝統復活の動きを表します。"},
        ],
        "highlightPatterns": ["forced them to change", "make them learn", "have begun bringing back"],
        "highlightColor": "#EA580C",
        "highlightLabel": "force / make",
    },
]


sections = [
    {
        "name": "大問1",
        "nameEn": "Part 1",
        "type": "vocabulary",
        "instruction": "次の(1)から(20)までの（　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "questions": section1_questions,
    },
    {
        "name": "大問2",
        "nameEn": "Part 2",
        "type": "passage-fill",
        "instruction": "次の英文A、Bを読み、その文意にそって(21)から(26)までの（　）に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "passages": [passage_2a, passage_2b],
    },
    {
        "name": "大問3",
        "nameEn": "Part 3",
        "type": "reading-comprehension",
        "instruction": "次の英文A、B、Cの内容に関して、(27)から(38)までの質問に対して最も適切なもの、または文を完成させるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
        "passages": [passage_3a, passage_3b, passage_3c],
    },
]

all_questions = []
all_passages = []
for section in sections:
    all_questions.extend(section.get("questions", []))
    all_passages.extend(section.get("passages", []))
    for passage in section.get("passages", []):
        all_questions.extend(passage.get("questions", []))

assert [item["number"] for item in all_questions] == list(range(1, 39))
assert {item["number"]: item["answer"] for item in all_questions} == ANSWERS
assert [len(passage["questions"]) for passage in all_passages] == [3, 3, 3, 4, 5]
assert all(len(item["choiceAnalysis"]) == 4 for item in all_questions)
assert all(item["choiceAnalysis"][item["answer"] - 1].count("→正解。💡") == 1 for item in all_questions)
assert len(vocabulary) == len({item["word"] for item in vocabulary}) == 65
assert len(focus_points) == 5
assert all(len(point["examples"]) == 3 and len(point["practiceQuestions"]) == 4 for point in focus_points)
for passage in all_passages:
    assert len(passage["paragraphs"]) == len(passage["translations"])
    corpus = " ".join(passage["paragraphs"])
    assert all(item[0] in corpus for item in passage["sentencePairs"])
    pair_source = (
        passage["paragraphs"][1:-1]
        if passage["title"] == "ZX950 LCD TV"
        else passage["paragraphs"]
    )
    normalized_source = re.sub(r"\s+", " ", " ".join(pair_source)).strip()
    normalized_pairs = re.sub(
        r"\s+",
        " ",
        " ".join(item[0] for item in passage["sentencePairs"]),
    ).strip()
    assert normalized_source == normalized_pairs
    for question in passage["questions"]:
        assert question.get("sourceEvidence")
        assert all(evidence in corpus for evidence in question["sourceEvidence"])
pair_anchors = {
    "Trouble at Sea": ("world’s oceans",),
    "Performing Cats": ("“Memory,”", "Webber’s", "Old Possum’s", "everyone’s"),
    "ZX950 LCD TV": ("TV’s instruction manual", "I’m sure", "I don’t need"),
    "The Empress’s Favorite Clothes": ("phuti karpas",),
    "Desert Delight": (
        "Tohono O’odham",
        "“desert people”",
        "each year—once",
        "This fruit—the saguaro fruit—",
        "tribe’s endangered traditions",
    ),
}
for passage in all_passages:
    paragraph_blob = " ".join(passage["paragraphs"])
    pair_blob = " ".join(item[0] for item in passage["sentencePairs"])
    assert all(anchor in paragraph_blob for anchor in pair_anchors[passage["title"]])
    assert all(anchor in pair_blob for anchor in pair_anchors[passage["title"]])
assert passage_3a["paragraphs"][0] == "Dear Customer Service Representative,"
assert passage_3a["paragraphs"][-1] == "Regards,\nMichael Green"

data = {
    "grade": "2級",
    "year": "2022",
    "session": "2",
    "title": "2022年度 第2回 英語資格検定2級 リーディング",
    "exam": "2022-2",
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
    f"passages={len(all_passages)} vocabulary={len(vocabulary)} focusPoints={len(focus_points)}"
)
