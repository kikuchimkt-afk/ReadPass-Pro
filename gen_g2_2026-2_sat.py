# -*- coding: utf-8 -*-
"""Reproducible source for Grade 2, 2026-2 Saturday supplementary venue.

Transcribed against the supplied scanned booklet, pp. 3-11; answers against
the separate official answer sheet. Run from any directory. Audio references
are deterministic and are populated by this generator, not by a post-edit.
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade2/2026-2-sat/data.json"


def module(suffix):
    spec = importlib.util.spec_from_file_location(suffix, ROOT / f"gen_g2_2026-2_sat_{suffix}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# text, natural translation (blank retained), choices, choice translations,
# 1-indexed answer, four contextual analyses, grammar/evidence note
PART1 = [
    ("A : I heard that your father became a dentist because he was afraid of going to the dentist.\nB : Yes, that's true. The ( 1 ) is that he is now a dentist himself.",
     "A：お父さんは歯医者に行くのが怖かったから歯医者になったと聞いたよ。\nB：うん、本当だよ。( 1 ) なことに、今では本人が歯医者なんだ。",
     ["irony", "impression", "adventure", "option"], ["皮肉・意外な巡り合わせ", "印象", "冒険", "選択肢"], 1,
     ["irony＝皮肉→正解。💡怖がっていた人が歯医者本人になった、という意外な逆転。", "impression＝印象。人に与える印象の話ではない。", "adventure＝冒険。冒険的な体験ではなく、立場の逆転を述べている。", "option＝選択肢。職業の候補を列挙する文脈ではない。"],
     "💡The irony is that S＋V は「皮肉なことに～だ」。afraid of の後ろは動名詞 going。himself は「本人・自身」を強調する。"),
    ("A : So, Fiona, what exactly are you studying at university?\nB : I'm studying ( 2 ) because I have always wanted to design beautiful and functional buildings one day.",
     "A：それで、フィオナ、大学では具体的に何を勉強しているの？\nB：いつか美しく機能的な建物を設計したいとずっと思ってきたので、( 2 ) を勉強しているの。",
     ["architecture", "furniture", "infection", "horizon"], ["建築学", "家具", "感染", "地平線"], 1,
     ["architecture＝建築学→正解。💡建物を設計するという将来の希望に合う専攻。", "furniture＝家具。建物そのものを設計する専攻とは異なる。", "infection＝感染。医療の語で、建物の設計には結びつかない。", "horizon＝地平線。大学で学ぶ専攻を表さない。"],
     "💡have always wanted は過去から現在まで続く希望。to design は wanted の目的語となる不定詞。functional は「機能的な」。"),
    ("Before making a decision about his career, Akira decided to ( 3 ) his university's career guidance counselor. He wanted to get some professional advice.",
     "将来の仕事について決める前に、アキラは大学の進路相談員に ( 3 ) することにした。専門的な助言をもらいたかったのだ。",
     ["prohibit", "consult", "bother", "imitate"], ["禁止する", "相談する", "困らせる", "まねる"], 2,
     ["prohibit＝禁止する。相談員を禁止するという意味は成立しない。", "consult＝相談する→正解。💡専門家の助言を得たい、という次の文が根拠。", "bother＝困らせる。助言を求める目的に合わない。", "imitate＝まねる。相談員の行動をまねる話ではない。"],
     "💡consult＋人 は前置詞なしで「人に相談する」。Before は前置詞なので making。decide to V は「～することに決める」。"),
    ("In art class, Ms. Jones gave each of the students a ball of ( 4 ). She told them that they should use it to make a plate, a bowl, a cup, or a vase.",
     "美術の授業で、ジョーンズ先生は生徒一人ひとりに丸めた ( 4 ) を渡した。それを使って皿、ボウル、カップ、または花瓶を作るように言った。",
     ["loss", "clay", "opinion", "manner"], ["損失", "粘土", "意見", "方法・態度"], 2,
     ["loss＝損失。丸めたり器を作ったりできる材料ではない。", "clay＝粘土→正解。💡丸めた材料から皿や花瓶を作る、美術の授業。", "opinion＝意見。器を作る材料にはならない。", "manner＝方法・態度。ball of に続く物質ではない。"],
     "💡give＋人＋物 の第4文型。each of the students は「生徒の一人ひとり」。use it to make の to は目的「作るために」。"),
    ("The soccer team realized that they needed to ( 5 ) their defense after the match in which they allowed seven goals. Now, they are training to improve their skills.",
     "サッカーチームは7点を許した試合の後、守備を ( 5 ) する必要があると気づいた。今は技術を向上させるために練習している。",
     ["recover", "strengthen", "interrupt", "gather"], ["回復する", "強化する", "中断する", "集める"], 2,
     ["recover＝回復する。失った物や健康を取り戻す語で、守備力の強化には不適切。", "strengthen＝強化する→正解。💡7失点を受け、守備を改善するために練習している。", "interrupt＝中断する。守備を止めると改善につながらない。", "gather＝集める。defense は集める対象ではない。"],
     "💡the match in which ... は「その試合で～した」。in which＝in the match。to improve は練習の目的を示す。"),
    ("Patricia thought she had explained the game's rules ( 6 ), but when her friends started playing, some of them did not know what to do. Patricia had to explain the rules again.",
     "パトリシアはゲームのルールを ( 6 ) 説明したつもりだったが、友達が遊び始めると、何をすればよいかわからない人がいた。ルールをもう一度説明しなければならなかった。",
     ["thoroughly", "refreshingly", "formerly", "purely"], ["十分に・徹底的に", "さわやかに", "以前は", "純粋に・単に"], 1,
     ["thoroughly＝十分に→正解。💡十分説明したつもりなのに理解されていなかった、という対比。", "refreshingly＝さわやかに。ルール説明の十分さを表さない。", "formerly＝以前は。時期ではなく説明の程度が焦点。", "purely＝純粋に・単に。理解できるほど十分だったという意味にならない。"],
     "💡had explained は thought より前の説明を示す過去完了。what to do は「何をすべきか」。had to は過去の必要を表す。"),
    ("The school had ( 7 ) how much money it would need for the trip to the science museum. Each student would have to pay five dollars.",
     "学校は科学博物館への遠足にどれほどの費用が必要か ( 7 ) していた。生徒一人につき5ドルを払う必要があるということだった。",
     ["calculated", "encountered", "influenced", "represented"], ["計算した", "遭遇した", "影響を与えた", "代表した・表した"], 1,
     ["calculated＝計算した→正解。💡必要な費用を計算し、1人5ドルと算出している。", "encountered＝遭遇した。必要金額を算出する意味はない。", "influenced＝影響を与えた。費用を計算する行為とは異なる。", "represented＝代表した。必要金額を求める文脈に合わない。"],
     "💡how much money it would need は疑問詞＋主語＋動詞の間接疑問。had calculated は過去完了、would は過去から見た未来。"),
    ("When the deliveryman arrived, Hannah was ( 8 ) because she had just gotten out of the shower. She quickly put on some clothes and went to answer the door.",
     "配達員が来たとき、ハンナはシャワーから出たばかりだったので ( 8 ) だった。急いで服を着て、玄関に応対に行った。",
     ["naked", "obvious", "intensive", "proper"], ["裸の", "明らかな", "集中的な", "適切な"], 1,
     ["naked＝裸の→正解。💡シャワー直後で、次の文では急いで服を着ている。", "obvious＝明らかな。服を着ていない状態を表さない。", "intensive＝集中的な。人の服装の状態を表さない。", "proper＝適切な。シャワー直後に急いで着替える理由にならない。"],
     "💡had just gotten out は到着より直前の出来事。put on は「服を着る」という動作。answer the door は「玄関に応対する」。"),
    ("A : Are there any ( 9 ) to the rule that all visitors must show their ID?\nB : Yes, children under ten don't need to show their ID.",
     "A：訪問者全員が身分証を見せなければならないという規則に ( 9 ) はありますか。\nB：はい、10歳未満の子供は見せる必要がありません。",
     ["punishments", "exceptions", "concentrations", "requirements"], ["罰", "例外", "集中", "要件・必要条件"], 2,
     ["punishments＝罰。規則が適用されない人について尋ねている。", "exceptions＝例外→正解。💡全員という規則に対し、10歳未満は不要という例外。", "concentrations＝集中。規則の適用範囲の話に合わない。", "requirements＝要件。追加条件ではなく、規則の例外を尋ねている。"],
     "💡an exception to a rule は「規則の例外」。the rule that ... の that 節は規則の内容を説明する。under ten は10歳を含まない。"),
    ("The cake that Aaron's sister made tasted terrible, but Aaron ( 10 ) that he liked it because he did not want to make her feel bad.",
     "アーロンの姉（または妹）が作ったケーキはひどい味だったが、彼女を嫌な気持ちにさせたくなかったので、気に入った ( 10 ) をした。",
     ["discovered", "pretended", "estimated", "wondered"], ["発見した", "ふりをした", "見積もった", "疑問に思った"], 2,
     ["discovered＝発見した。実際はひどい味で、気に入ったことを発見したのではない。", "pretended＝ふりをした→正解。💡本心ではなく、相手を傷つけないために気に入ったふりをした。", "estimated＝見積もった。味の感想は数量の見積もりではない。", "wondered＝疑問に思った。that he liked it とつないで演技を表せない。"],
     "💡pretend that S＋V は「～のふりをする」。make＋人＋動詞の原形で make her feel bad。「姉／妹」の別は本文では不明。"),
    ("A : Have you given up on your diet?\nB : No, I'm going to ( 11 ) it this time. I want to be healthier.",
     "A：ダイエットはもう諦めたの？\nB：いいえ、今回はそれを ( 11 ) つもりよ。もっと健康になりたいの。",
     ["look at", "walk away", "stick to", "run across"], ["見る", "立ち去る", "続ける・守る", "偶然出会う"], 3,
     ["look at＝見る。ダイエットを続けるという返答にはならない。", "walk away＝立ち去る。諦めていないという返答と逆の意味。", "stick to＝続ける→正解。💡諦めずに健康のための計画を守ると答えている。", "run across＝偶然出会う。ダイエットは偶然出会う対象ではない。"],
     "💡give up on は「～を諦める」、stick to は「～をやり通す」。to は前置詞で、it はダイエットを指す。"),
    ("A : Oh, I wrote the wrong date on this letter. What should I do?\nB : Just ( 12 ) the date and write the correct one above it.",
     "A：あ、この手紙に間違った日付を書いてしまった。どうすればいい？\nB：その日付を ( 12 ) して、その上に正しい日付を書けばいいよ。",
     ["pull away", "cross out", "knock down", "turn off"], ["離れる・引き離す", "線を引いて消す", "倒す", "電源を切る"], 2,
     ["pull away＝離れる。書いた日付を訂正する動作にならない。", "cross out＝線を引いて消す→正解。💡誤った日付を取り消して上に正しい日付を書く。", "knock down＝倒す。文字の訂正には使わない。", "turn off＝電源を切る。日付には電源がない。"],
     "💡cross out＋文字 は「文字を線で消す」。the correct one の one は date の代用語。above it の it も誤った日付を指す。"),
    ("The construction of the new library is ( 13 ). The builders hope to finish it by the end of next year.",
     "新しい図書館の建設は ( 13 ) だ。建設業者は来年末までに完成させたいと考えている。",
     ["in case", "in progress", "at peace", "at random"], ["万一に備えて", "進行中で", "平穏で", "無作為に"], 2,
     ["in case＝万一に備えて。建設の現在の進み具合を表さない。", "in progress＝進行中で→正解。💡まだ完成しておらず、来年末までの完成を目指している。", "at peace＝平穏で。建設が進んでいる状態とは異なる。", "at random＝無作為に。作業の進捗を表す語ではない。"],
     "💡be in progress は「進行中だ」。hope to finish の to は不定詞。by the end of ... は「～の終わりまでに」という期限。"),
    ("A : Dad, please let me have one! All my friends have smartphones, and I really need one for school.\nB : No, Sarah. I'm not going to ( 14 ) just because your friends have them.",
     "A：お父さん、お願い、私にも買って！友達はみんなスマートフォンを持っているし、学校で本当に必要なの。\nB：だめだよ、サラ。友達が持っているというだけで ( 14 ) つもりはない。",
     ["take off", "give in", "bring up", "come up"], ["離陸する・脱ぐ", "折れる・譲歩する", "話題に出す・育てる", "持ち上がる・近づく"], 2,
     ["take off＝離陸する・脱ぐ。要求を認める意味にはならない。", "give in＝折れる→正解。💡娘に押し切られて要求を認めるつもりはない、という父の返答。", "bring up＝話題に出す。ここでは話題に出す対象の目的語もない。", "come up＝持ち上がる。人が要求に屈する意味ではない。"],
     "💡let＋人＋動詞の原形で let me have。not ... just because ... は「～という理由だけで…するわけではない」。"),
    ("A : How did the meeting go?\nB : Not well. We decided to ( 15 ) the discussions because we couldn't agree on a price.",
     "A：会議はどうだった？\nB：うまくいかなかった。価格に合意できなかったので、話し合いを ( 15 ) することにした。",
     ["fall for", "take up", "break off", "let down"], ["だまされる・好きになる", "始める・取り上げる", "打ち切る", "失望させる"], 3,
     ["fall for＝だまされる。話し合いそのものにだまされるとは言わない。", "take up＝取り上げる。会議が不調で協議をやめる文脈と逆。", "break off＝打ち切る→正解。💡価格の折り合いがつかず、協議を中断した。", "let down＝失望させる。目的語 discussions は失望する人ではない。"],
     "💡break off＋交渉など は「打ち切る」。agree on＋事柄 は「事柄について合意する」。How did ... go? は結果を尋ねる定型。"),
    ("A : ( 16 ) how much I try to go to sleep early, I always end up staying awake until midnight.\nB : Maybe you should try putting your smartphone in another room at night.",
     "A：( 16 ) どれほど早く寝ようと努力しても、結局いつも真夜中まで起きているの。\nB：夜はスマートフォンを別の部屋に置いてみるといいかもしれないね。",
     ["No better", "No matter", "Depending on", "Based on"], ["より良くはない", "～にかかわらず", "～次第で", "～に基づいて"], 2,
     ["No better＝より良くはない。how much に続けて譲歩節を作れない。", "No matter＝～にかかわらず→正解。💡No matter how much で「どんなに～しても」。", "Depending on＝～次第で。努力の程度によらず同じ結果、という内容に合わない。", "Based on＝～に基づいて。努力しても寝られないという譲歩にならない。"],
     "💡No matter how much S＋V は程度に左右されない結果を示す。end up V-ing は「結局～する」。try putting は「試しに置いてみる」。"),
    ("Some students prefer studying alone, while others like working in groups. ( 17 ), group work helps students learn from each other more effectively.",
     "一人で勉強する方を好む生徒もいれば、グループで取り組むことを好む生徒もいる。( 17 )、グループ活動は生徒がお互いからより効果的に学ぶ助けになる。",
     ["In contrast", "In detail", "In short", "In general"], ["対照的に", "詳しく", "要するに", "一般に"], 4,
     ["In contrast＝対照的に。前の好みの違いと対照的な事実を挙げているのではない。", "In detail＝詳しく。具体的な詳細を説明する文ではない。", "In short＝要するに。前文の好みを要約した内容ではない。", "In general＝一般に→正解。💡個人の好みは異なるが、グループ学習の一般的な利点を述べる。"],
     "💡Some ... while others ... は「～する人もいれば、…する人もいる」。help＋人＋動詞の原形で helps students learn。"),
]


def build():
    passages = module("passages")
    materials = module("materials")
    questions = []
    for number, row in enumerate(PART1, 1):
        text, translation, choices, ctrans, answer, analysis, grammar = row
        questions.append(dict(number=number, text=text, translation=translation,
                              choices=choices, choiceTranslations=ctrans, answer=answer,
                              choiceAnalysis=analysis, grammar=grammar))
    sections = [
        dict(name="大問1", nameEn="Part 1", type="vocabulary",
             instruction="次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", questions=questions),
        dict(name="大問2", nameEn="Part 2", type="passage-fill",
             instruction="次の英文A，Bを読み，その文意にそって(18)から(23)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=passages.PASSAGES[:2]),
        dict(name="大問3", nameEn="Part 3", type="reading-comprehension",
             instruction="次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=passages.PASSAGES[2:]),
    ]
    return dict(grade="2級", year="2026", session="2-sat",
                title="2026年度 第2回（土曜準会場）英検2級 リーディング",
                vocabulary=materials.vocabulary(), sections=sections,
                lessonPlan=materials.lessonplan(passages.PASSAGES),
                listening={"part1": dict(zip(map(str, range(1, 16)), [4,4,1,3,2,3,2,1,2,3,1,1,2,2,2])),
                           "part2": dict(zip(map(str, range(16, 31)), [1,1,3,1,1,4,2,4,3,1,1,1,2,1,1]))})


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(OUT)
