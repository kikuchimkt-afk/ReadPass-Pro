# -*- coding: utf-8 -*-
"""Build the audited ReadPass data set for EIKEN Grade 2, 2022-1 main venue."""

import json
import os
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent
OUT_DIR = REPO / "data" / "grade2" / "2022-1"
OUT_PATH = OUT_DIR / "data.json"

ANSWERS = {
    1: 1, 2: 4, 3: 4, 4: 3, 5: 4, 6: 4, 7: 3, 8: 4, 9: 1, 10: 4,
    11: 1, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 2, 18: 2, 19: 3, 20: 1,
    21: 1, 22: 3, 23: 1, 24: 3, 25: 2, 26: 4,
    27: 4, 28: 1, 29: 2, 30: 1, 31: 4, 32: 4, 33: 3, 34: 2, 35: 2,
    36: 4, 37: 4, 38: 4,
}

LISTENING = {
    "part1": {str(i + 1): value for i, value in enumerate(
        [1, 3, 4, 3, 3, 2, 4, 2, 1, 4, 2, 2, 2, 3, 4]
    )},
    "part2": {str(i + 16): value for i, value in enumerate(
        [3, 1, 4, 2, 3, 4, 2, 2, 3, 1, 3, 2, 3, 2, 3]
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
        item.pop("text", None)
        item.pop("translation", None)
        item["question"] = question
        item["questionTranslation"] = question_translation
    if source_evidence:
        item["sourceEvidence"] = source_evidence
    return item


section1_questions = [
    make_question(
        1,
        "Last week, Shelly went to see a horror movie. It was about a strange ( ) that was half shark and half man.",
        "先週、シェリーはホラー映画を見に行った。それは半分サメで半分人間という奇妙な（　）についての映画だった。",
        ["creature", "mineral", "package", "instrument"],
        ["生き物", "鉱物", "小包", "器具"], 1,
        ["half shark and half man は生き物の説明なので creature が合う。", "無生物の鉱物では説明と合わない。", "小包は half shark and half man にはなれない。", "器具では映画の怪物を表せない。"],
        "関係代名詞 that が creature を説明している。be about ... は「…についての内容である」。",
    ),
    make_question(
        2,
        "After high school, Ted joined the ( ) so that he could serve his country. He felt proud when he put on his army uniform for the first time.",
        "高校卒業後、テッドは国に仕えるため（　）に入った。初めて軍服を着たとき、彼は誇らしく感じた。",
        ["affair", "emergency", "container", "military"],
        ["事柄・事件", "緊急事態", "容器", "軍隊"], 4,
        ["join the affair という結び付きはない。", "緊急事態そのものに加入することはできない。", "容器に入隊するという意味にはならない。", "army uniform と serve his country が根拠。join the military で「軍隊に入る」。"],
        "so that S could ... は目的を表し「Sが…できるように」。join the military は定型表現。",
    ),
    make_question(
        3,
        "Reika's dream is to work for a famous French restaurant in Tokyo. She is trying to ( ) this by going to a cooking school.",
        "レイカの夢は東京の有名なフランス料理店で働くことだ。彼女は料理学校に通うことで、これを（　）しようとしている。",
        ["decrease", "unite", "overwhelm", "accomplish"],
        ["減らす", "結び付ける", "圧倒する", "達成する"], 4,
        ["夢を「減らす」では意味が合わない。", "夢を結合するという文脈ではない。", "夢を圧倒するという目的ではない。", "this は dream を指す。accomplish a dream で「夢を達成する」。"],
        "try to do は「…しようとする」。by doing は手段を表し「…することによって」。",
    ),
    make_question(
        4,
        "Arthur was going to sell his café. However, he ( ) his decision because he started to get more customers after a new college opened nearby.",
        "アーサーはカフェを売るつもりだった。しかし近くに新しい大学が開校して客が増え始めたため、その決定を（　）した。",
        ["abused", "secured", "reversed", "stimulated"],
        ["悪用した", "確保した", "覆した", "刺激した"], 3,
        ["decision を悪用したとは言わない。", "決定を確保するでは、売却を取りやめた流れにならない。", "客が増えたため売る決定を覆した、という因果が自然。", "decision を刺激するという語の組合せは不自然。"],
        "be going to do は予定。reverse one's decision は「決定を覆す・撤回する」。",
    ),
    make_question(
        5,
        "Frank did not have ( ) time to write his report, so he asked his boss if he could have a few more days to finish it.",
        "フランクには報告書を書く（　）時間がなかったので、仕上げるためにあと数日もらえるか上司に頼んだ。",
        ["possible", "delicate", "financial", "sufficient"],
        ["可能な", "繊細な", "財政上の", "十分な"], 4,
        ["possible time では「足りない時間」を表せない。", "時間を delicate と形容する文脈ではない。", "financial time という結び付きはない。", "a few more days を求めたことから、時間が十分でなかったと分かる。"],
        "sufficient + 名詞で「十分な…」。ask if S could ... は間接疑問を用いた依頼。",
    ),
    make_question(
        6,
        "There was a fire at a restaurant in Brigston City yesterday. No one was hurt, but the building was ( ) damaged. The owners will have to build a new one.",
        "昨日ブリグストン市のレストランで火事があった。けが人はいなかったが、建物は（　）損傷した。所有者は新しく建て直さなければならない。",
        ["mentally", "intelligently", "annually", "severely"],
        ["精神的に", "知的に", "毎年", "ひどく"], 4,
        ["建物の物理的損傷を mentally では修飾できない。", "「知的に損傷した」は意味をなさない。", "損傷の程度ではなく頻度を表す語なので合わない。", "build a new one が必要なほど、建物がひどく損傷した。"],
        "was damaged は受動態。severely は damaged の程度を強める副詞。",
    ),
    make_question(
        7,
        "Beth was invited to a wedding party last week. She did not want to go by herself, so she asked her friend Jeremy to ( ) her.",
        "ベスは先週、結婚パーティーに招待された。一人で行きたくなかったので、友人のジェレミーに（　）してくれるよう頼んだ。",
        ["restrict", "distribute", "accompany", "promote"],
        ["制限する", "配る", "同行する", "促進する"], 3,
        ["一人で行きたくない問題の解決にならない。", "人を distribute するとは言わない。", "accompany + 人で「人に同行する」。go by herself と対になる。", "昇進させる・促進する意味では文脈に合わない。"],
        "ask 人 to do は「人に…するよう頼む」。accompany は他動詞なので with は不要。",
    ),
    make_question(
        8,
        "The SOL-5 rocket will leave Earth tomorrow. The astronauts' ( ) is to repair a weather satellite.",
        "SOL-5ロケットは明日地球を離れる。宇宙飛行士たちの（　）は気象衛星を修理することだ。",
        ["foundation", "impression", "definition", "mission"],
        ["基礎・財団", "印象", "定義", "任務"], 4,
        ["修理する目的を foundation とは呼ばない。", "印象では is to repair の内容とつながらない。", "語の定義を述べる文ではない。", "宇宙飛行士が果たすべき任務の内容を不定詞で説明している。"],
        "S's mission is to do で「Sの任務は…することだ」。不定詞が補語。",
    ),
    make_question(
        9,
        "In chemistry class, the students added a small amount of acid to water. Then, they used this ( ) to carry out an experiment.",
        "化学の授業で、生徒たちは少量の酸を水に加えた。そして、この（　）を使って実験を行った。",
        ["mixture", "climate", "entry", "moment"],
        ["混合物", "気候", "入場・項目", "瞬間"], 1,
        ["acid と water を混ぜてできたものなので mixture。", "気候は実験に使う物質ではない。", "entry は混ぜた液体を指せない。", "moment は時間を表し、this の指す物質にならない。"],
        "this は直前の acid と water を混ぜたものを受ける指示語。carry out an experiment は「実験を行う」。",
    ),
    make_question(
        10,
        "It was raining very hard in the morning, so the government had to wait to ( ) the rocket into space.",
        "朝は雨が非常に激しかったので、政府はロケットを宇宙へ（　）するのを待たなければならなかった。",
        ["elect", "impact", "sweep", "launch"],
        ["選出する", "影響を与える", "掃く", "打ち上げる"], 4,
        ["ロケットを elect するとは言わない。", "impact は launch の動作を表せない。", "宇宙へ掃く、では意味が通らない。", "launch a rocket で「ロケットを打ち上げる」。悪天候で延期する流れにも合う。"],
        "wait to do は「…するのを待つ」。have to は必要・義務を表す。",
    ),
    make_question(
        11,
        "During history class, Aiden noticed that Risa did not have her notebook. He ( ) some paper from his notebook and gave it to her so that she could take notes.",
        "歴史の授業中、エイデンはリサがノートを持っていないことに気付いた。彼は自分のノートから紙を何枚か（　）、彼女がメモを取れるよう渡した。",
        ["tore off", "relied on", "answered back", "broke out"],
        ["ちぎり取った", "頼った", "口答えした", "突然起こった"], 1,
        ["紙をノートからちぎり取って渡す、という動作が自然。", "paper に頼るという意味ではない。", "answer back は人に口答えすることで、紙を目的語に取れない。", "break out は火事などが起こる自動詞句で、paper を目的語に取れない。"],
        "tear A off B で「AをBからちぎり取る」。so that S could ... は目的。",
    ),
    make_question(
        12,
        "Derek ( ) winning his company's golf tournament. However, he played a bad shot on the last hole, and he ended up finishing second.",
        "デレクは会社のゴルフ大会で優勝（　）。しかし最終ホールで悪いショットを打ち、結局2位になった。",
        ["came close to", "made fun of", "took pride in", "found fault with"],
        ["もう少しで…するところだった", "…をからかった", "…を誇りに思った", "…のあら探しをした"], 1,
        ["最後に失敗して2位なので「優勝しかけた」が合う。to の後は動名詞。", "優勝をからかったという意味ではない。", "実際には優勝していないので「優勝を誇りに思った」は合わない。", "優勝の欠点を探したという文脈ではない。"],
        "come close to doing は「もう少しで…する」。end up doing は「結局…することになる」。",
    ),
    make_question(
        13,
        "Mr. Griffith warned his students that they would get extra homework if they kept talking in class. He ( ) with his threat because they would not be quiet.",
        "グリフィス先生は、授業中に話し続けるなら宿題を追加すると生徒に警告した。生徒が静かにしなかったので、先生はその警告を（　）。",
        ["followed through", "went over", "got through", "turned over"],
        ["最後まで実行した", "見直した", "切り抜けた・通じた", "ひっくり返した"], 1,
        ["follow through with a threat で「警告したことを実行する」。", "go over は復習・点検で、警告の実行ではない。", "get through with a threat という結び付きは不自然。", "turn over は物を裏返すなどの意味で、threat と合わない。"],
        "warn 人 that ... は「人に…と警告する」。keep doing は「…し続ける」。",
    ),
    make_question(
        14,
        "A: Guess who I just ( ). Do you remember Gina from college?\nB: Oh, yes. I met her the other day, too. It seems she works in the same building as us.",
        "A：今ちょうど誰に（　）したと思う？ 大学時代のジーナを覚えている？\nB：ああ。私も先日会ったよ。同じ建物で働いているみたいだね。",
        ["hoped for", "ran into", "looked over", "complied with"],
        ["…を望んだ", "…に偶然会った", "…に目を通した", "…に従った"], 2,
        ["人を望むという流れではない。", "met her the other day, too が言い換え。run into 人で「人に偶然会う」。", "人を点検・ざっと見るという話ではない。", "人に従うという意味では会った話につながらない。"],
        "Guess who ... は「誰が…したと思う？」。run into は偶然の出会いを表す句動詞。",
    ),
    make_question(
        15,
        "Since changing jobs, Neil has been much more ( ) his work-life balance. He is enjoying his new position, but he is also glad that he can spend more time with his family and friends.",
        "転職して以来、ニールは仕事と生活のバランスにずっと（　）なった。新しい職を楽しみつつ、家族や友人との時間が増えたことも喜んでいる。",
        ["separate from", "content with", "based on", "equal to"],
        ["…から離れた", "…に満足して", "…に基づいて", "…と等しい"], 2,
        ["work-life balance から離れている、では後文と合わない。", "仕事も私生活も好調で glad とあるため「満足して」が合う。", "人が balance に基づくという補語にはならない。", "人と balance が等しいという意味にはならない。"],
        "since doing は「…して以来」。have been は現在完了で現在まで続く状態を表す。",
    ),
    make_question(
        16,
        "A: Mom, is it OK if I invite a couple of friends to the barbecue on Saturday?\nB: ( ). There should be more than enough for everyone to eat and drink.",
        "A：お母さん、土曜日のバーベキューに友達を2、3人呼んでもいい？\nB：（　）。みんなが食べたり飲んだりする分は十分以上にあるはずよ。",
        ["In any case", "At any rate", "By all means", "On the whole"],
        ["いずれにせよ", "とにかく", "ぜひどうぞ", "全体として"], 3,
        ["許可への直接の肯定返答にはならない。", "話題をまとめる表現で、快い許可を表さない。", "相手の依頼・許可に快く応じる表現。十分な食事があるという後文とも合う。", "全体的な評価を述べる場面ではない。"],
        "Is it OK if ...? は許可を求める表現。By all means. は「もちろん、ぜひ」。",
    ),
    make_question(
        17,
        "Alison hates it when her baby brother goes into her room. He always ( ) with her things, and she has to clean up afterward.",
        "アリソンは幼い弟が自分の部屋に入るのが嫌いだ。弟はいつも彼女の物で（　）をし、その後彼女が片付けなければならない。",
        ["makes an effort", "makes a mess", "takes a chance", "takes a rest"],
        ["努力する", "散らかす", "思い切ってやる", "休憩する"], 2,
        ["努力した結果、片付けが必要になる流れではない。", "clean up afterward が根拠。make a mess with ... で「…を散らかす」。", "危険を承知で試す話ではない。", "休憩したため部屋を片付けるという因果はない。"],
        "hate it when S V は「SがVするのが嫌だ」。have to do は必要を表す。",
    ),
    make_question(
        18,
        "After getting the first prize in the presentation competition, Kevin said in his speech that ( ) for his wife's help, he never would have won.",
        "プレゼンテーション大会で1位になった後、ケビンはスピーチで、妻の助けが（　）なら決して優勝できなかっただろうと述べた。",
        ["with", "but", "along", "over"],
        ["…があれば", "…がなければ", "…に沿って", "…を越えて"], 2,
        ["with では「妻の助けがあったため」となるが、後ろの仮定法と定型が合わない。", "but for ... は「…がなければ」。would have won と組み、過去の反実仮想を表す。", "along for という形では条件を表せない。", "over for では意味を作れない。"],
        "but for + 名詞は if it had not been for ... と同じ。would have + 過去分詞は仮定法過去完了の帰結。",
    ),
    make_question(
        19,
        "Sean has an important meeting early tomorrow morning, so he ( ) better not stay up late tonight.",
        "ショーンは明朝早く重要な会議があるので、今夜は夜更かししない（　）よい。",
        ["may", "would", "had", "should"],
        ["…かもしれない", "…だろう", "…したほうがよい", "…すべきだ"], 3,
        ["may better という助動詞の並びにはならない。", "would better では定型表現にならない。", "had better not do で「…しないほうがよい」。", "should better と助動詞を重ねることはできない。"],
        "had better (not) do は強めの助言。「…した（しない）ほうがよい」。",
    ),
    make_question(
        20,
        "A: Nicky, you're graduating from high school next year. It's time you ( ) thinking about which university you want to go to.\nB: You're right, Dad, but I still don't know what I want to be in the future.",
        "A：ニッキー、来年高校を卒業するね。どの大学へ行きたいか考え始める時だよ。\nB：その通りだけど、将来何になりたいかまだ分からないんだ。",
        ["started", "will start", "starting", "to start"],
        ["始めた", "始めるだろう", "始めている", "始めること"], 1,
        ["It's time S + 過去形 の形で、現在すべきことを表す。", "It's time の後の節では will ではなく過去形を用いる。", "主語 you の後に分詞だけは置けない。", "節内には定形動詞が必要で、to 不定詞は置けない。"],
        "It's time + S + 過去形は「Sがそろそろ…する時だ」。started thinking で start doing。",
    ),
]


def sp(en, ja, verb=""):
    """Sentence-popup entry: English, Japanese, slash guide, main verb."""
    return [en, ja, f"{en}|{ja}", verb]


passage_2a_paragraphs = [
    "As in many other countries, people in India are concerned about the problem of plastic waste. After all, the country produces 5.6 billion kilograms of it every year. The system for managing plastic waste needs improvement because a lot of plastic ends up as trash on land and in waterways such as the Ganges River. In response, the Indian government planned to introduce a ban on plastic items that could only be used once. ( 21 ), though, the government was forced to change its plans because of the condition of the economy and worries about an increase in unemployment.",
    "Nevertheless, there is one kind of situation where the use of plastic has come to an end. All 7,000 railway stations in India have replaced plastic teacups with brown clay teacups called kulhads. Long before plastic cups were used in India, people enjoyed drinking tea in these traditional cups. The minister for railways in India ordered railway stations to ( 22 ) kulhads. By doing so, he hopes the country will take an important step toward ending plastic waste.",
    "There are several reasons why kulhads are better than plastic teacups. First, after they have been thrown away, they soon break down into substances that do not harm the environment. Second, the clay that kulhads are made from actually improves the flavor of the tea. Finally, using kulhads ( 23 ). Plastic cups are made with machines, but kulhads are made by hand. The Indian government estimates that hundreds of thousands of people will get extra work because of this change.",
]

passage_2a_translations = [
    "多くの国と同様、インドの人々もプラスチックごみの問題を心配している。何しろ、この国では毎年56億キログラムものプラスチックごみが出る。多くが陸地やガンジス川などの水路にごみとして行き着くため、その管理制度には改善が必要だ。これを受け、インド政府は使い捨てプラスチック製品の禁止を導入する予定だった。しかし（21）、経済状況と失業増加への懸念から、計画変更を余儀なくされた。",
    "それでも、プラスチック使用が終わった場面が一つある。インドの全7,000駅がプラスチックのティーカップを、クルハドと呼ばれる茶色い素焼きのカップに替えた。プラスチックカップが使われるずっと以前から、人々はこの伝統的な器で茶を楽しんでいた。鉄道大臣は各駅に、クルハドで（22）よう命じた。そうすることで、プラスチックごみをなくす重要な一歩になることを期待している。",
    "クルハドがプラスチックカップより優れる理由はいくつかある。第一に、捨てられた後すぐに分解され、環境に害を与えない物質になる。第二に、その粘土は茶の風味を実際に良くする。最後に、クルハドを使うことは（23）。プラスチックカップは機械製だが、クルハドは手作りである。政府は、この変更によって何十万人もの人が追加の仕事を得ると見積もっている。",
]

passage_2a_pairs = [
    sp("As in many other countries, people in India are concerned about the problem of plastic waste.", "多くの国と同様、インドの人々もプラスチックごみの問題を心配している。", "are concerned"),
    sp("After all, the country produces 5.6 billion kilograms of it every year.", "何しろ、この国では毎年56億キログラムものそれが生産される。", "produces"),
    sp("The system for managing plastic waste needs improvement because a lot of plastic ends up as trash on land and in waterways such as the Ganges River.", "多くのプラスチックが陸地やガンジス川などの水路にごみとして行き着くため、その管理制度には改善が必要だ。", "needs"),
    sp("In response, the Indian government planned to introduce a ban on plastic items that could only be used once.", "これを受け、インド政府は使い捨てプラスチック製品の禁止を導入する予定だった。", "planned"),
    sp("( 21 ), though, the government was forced to change its plans because of the condition of the economy and worries about an increase in unemployment.", "しかし（21）、政府は経済状況と失業増加への懸念から計画変更を余儀なくされた。", "was forced"),
    sp("Nevertheless, there is one kind of situation where the use of plastic has come to an end.", "それでも、プラスチック使用が終わった場面が一つある。", "is"),
    sp("All 7,000 railway stations in India have replaced plastic teacups with brown clay teacups called kulhads.", "インドの全7,000駅がプラスチックのティーカップを、クルハドと呼ばれる茶色い素焼きのカップに替えた。", "have replaced"),
    sp("Long before plastic cups were used in India, people enjoyed drinking tea in these traditional cups.", "プラスチックカップがインドで使われるずっと以前から、人々はこの伝統的な器で茶を楽しんでいた。", "enjoyed"),
    sp("The minister for railways in India ordered railway stations to ( 22 ) kulhads.", "インドの鉄道大臣は各駅に、クルハドで（22）よう命じた。", "ordered"),
    sp("By doing so, he hopes the country will take an important step toward ending plastic waste.", "そうすることで、国がプラスチックごみをなくす重要な一歩を踏み出すことを期待している。", "hopes"),
    sp("There are several reasons why kulhads are better than plastic teacups.", "クルハドがプラスチックカップより優れる理由はいくつかある。", "are"),
    sp("First, after they have been thrown away, they soon break down into substances that do not harm the environment.", "第一に、捨てられた後すぐに分解され、環境に害を与えない物質になる。", "break down"),
    sp("Second, the clay that kulhads are made from actually improves the flavor of the tea.", "第二に、クルハドの材料である粘土は茶の風味を実際に良くする。", "improves"),
    sp("Finally, using kulhads ( 23 ).", "最後に、クルハドを使うことは（23）。", ""),
    sp("Plastic cups are made with machines, but kulhads are made by hand.", "プラスチックカップは機械製だが、クルハドは手作りである。", "are made"),
    sp("The Indian government estimates that hundreds of thousands of people will get extra work because of this change.", "インド政府は、この変更によって何十万人もの人が追加の仕事を得ると見積もっている。", "estimates"),
]

passage_2a = {
    "label": "A",
    "title": "An Answer in a Teacup",
    "paragraphs": passage_2a_paragraphs,
    "translations": passage_2a_translations,
    "sentencePairs": passage_2a_pairs,
    "questions": [
        make_question(21, None, None,
            ["In the end", "Moreover", "For one thing", "Overall"],
            ["結局", "さらに", "一つには", "全体として"], 1,
            ["計画したが最終的に変更を余儀なくされた、という時間的な結末を表す。", "情報の単純な追加ではなく、計画の結果を述べている。", "複数の理由の一例を挙げる位置ではない。", "全体の要約を置く位置ではなく、出来事の推移を述べる。"],
            "In the end は経過の最後の結果を示す。though と組み「しかし結局」の流れになる。",
            source_evidence=["the government was forced to change its plans"]),
        make_question(22, None, None,
            ["provide trash cans for", "use less plastic in", "only sell tea in", "charge more for"],
            ["…用のごみ箱を備える", "…で使うプラスチックを減らす", "…だけで茶を売る", "…により高い料金を取る"], 3,
            ["駅のごみ箱の話は本文にない。", "クルハドの中でプラスチックを使うという意味になり、置換の説明と合わない。", "plastic teacups を kulhads に替えたため、茶はクルハドだけで売るという内容。", "価格を上げたという記述はない。"],
            "order + 人・組織 + to do は「…に～するよう命じる」。",
            source_evidence=["have replaced plastic teacups with brown clay teacups called kulhads"]),
        make_question(23, None, None,
            ["will create jobs", "costs less money", "is better for people's health", "is just the beginning"],
            ["雇用を生み出す", "費用が少なくて済む", "人々の健康により良い", "ほんの始まりにすぎない"], 1,
            ["手作りなので何十万人もの追加の仕事が生まれる、という後続文につながる。", "価格や費用を比較する説明はない。", "健康効果ではなく環境・風味・雇用が理由。", "この変更が始まりにすぎないという説明はない。"],
            "動名詞句 using kulhads が主語。will create が述語となる。",
            source_evidence=["hundreds of thousands of people will get extra work"]),
    ],
}


passage_2b_paragraphs = [
    "Parrots are smart and sometimes very colorful birds. They are popular as pets and can often be seen in zoos. Unfortunately, about one-third of parrot species in the wild are in danger of dying out. Examples include hyacinth macaws and Lear's macaws. Each year, some of these birds are caught and sold illegally as pets. ( 24 ), many are dying because the forests where they live are being cleared to create farmland and to get wood. This has reduced the size of the areas in which they can build nests and collect food.",
    "A study published in the journal Diversity revealed that hyacinth macaws and Lear's macaws play an important role in the forests. Researchers studying these parrots in Brazil and Bolivia found that they spread the seeds of 18 kinds of trees. They observed the birds taking fruits and nuts from trees and carrying them over long distances. The birds do this so that they can eat the fruits and nuts later. However, they ( 25 ). When this happens in areas cleared by humans, the seeds inside the fruits and nuts grow into trees, helping the forests to recover.",
    "Today, conservation groups are working hard to protect hyacinth macaws and Lear's macaws. One difficulty is that these parrots ( 26 ). An important reason for this is that their eggs are often eaten by other birds. To prevent this, macaw eggs are sometimes removed from their nests by scientists and replaced with chicken eggs. The scientists keep the eggs safe. After the macaw chicks come out of their eggs, they are returned to their parents.",
]

passage_2b_translations = [
    "オウムは賢く、ときに非常に色鮮やかな鳥である。ペットとして人気があり、動物園でもよく見られる。しかし野生のオウム種の約3分の1が絶滅の危機にあり、スミレコンゴウインコやヒメコンゴウインコも含まれる。毎年、一部は捕らえられてペットとして違法に売られる。（24）、生息する森林が農地開発や木材採取のため伐採され、多くが死んでいる。巣作りや採餌のできる地域は縮小した。",
    "学術誌Diversityの研究は、この2種が森林で重要な役割を果たすと明らかにした。ブラジルとボリビアの研究者は、18種類の木の種を広げることを発見した。鳥は果実や木の実を取り、後で食べるため遠くまで運ぶ。しかし（25）。人間が切り開いた場所でこれが起こると、中の種が木に育ち、森林の回復を助ける。",
    "現在、保護団体は2種を守るため懸命に活動している。難点の一つは、これらのオウムが（26）ことだ。卵が他の鳥に食べられることが大きな理由である。防止のため科学者が卵を巣から取り出し、ニワトリの卵と交換することがある。科学者は卵を安全に保ち、ひながかえると親のもとへ戻す。",
]

passage_2b_pairs = [
    sp("Parrots are smart and sometimes very colorful birds.", "オウムは賢く、ときに非常に色鮮やかな鳥である。", "are"),
    sp("They are popular as pets and can often be seen in zoos.", "ペットとして人気があり、動物園でもよく見られる。", "are / can be seen"),
    sp("Unfortunately, about one-third of parrot species in the wild are in danger of dying out.", "残念ながら、野生のオウム種の約3分の1が絶滅の危機にある。", "are"),
    sp("Examples include hyacinth macaws and Lear's macaws.", "例としてスミレコンゴウインコやヒメコンゴウインコが挙げられる。", "include"),
    sp("Each year, some of these birds are caught and sold illegally as pets.", "毎年、これらの鳥の一部は捕らえられ、ペットとして違法に売られる。", "are caught and sold"),
    sp("( 24 ), many are dying because the forests where they live are being cleared to create farmland and to get wood.", "（24）、生息する森林が農地開発や木材採取のため伐採され、多くが死んでいる。", "are dying"),
    sp("This has reduced the size of the areas in which they can build nests and collect food.", "このため、巣作りや餌集めのできる地域が縮小した。", "has reduced"),
    sp("A study published in the journal Diversity revealed that hyacinth macaws and Lear's macaws play an important role in the forests.", "学術誌Diversityに掲載された研究は、2種のコンゴウインコが森林で重要な役割を果たすと明らかにした。", "revealed"),
    sp("Researchers studying these parrots in Brazil and Bolivia found that they spread the seeds of 18 kinds of trees.", "ブラジルとボリビアで研究する人々は、鳥が18種類の木の種を広げることを発見した。", "found"),
    sp("They observed the birds taking fruits and nuts from trees and carrying them over long distances.", "研究者は、鳥が果実や木の実を取り、遠くまで運ぶのを観察した。", "observed"),
    sp("The birds do this so that they can eat the fruits and nuts later.", "鳥は後で果実や木の実を食べられるよう、こうしている。", "do"),
    sp("However, they ( 25 ).", "しかし、鳥は（25）。", ""),
    sp("When this happens in areas cleared by humans, the seeds inside the fruits and nuts grow into trees, helping the forests to recover.", "人間が切り開いた場所でこれが起こると、中の種が木に育ち、森林の回復を助ける。", "grow"),
    sp("Today, conservation groups are working hard to protect hyacinth macaws and Lear's macaws.", "現在、保護団体は2種のコンゴウインコを守るため懸命に活動している。", "are working"),
    sp("One difficulty is that these parrots ( 26 ).", "難点の一つは、これらのオウムが（26）ことだ。", "is"),
    sp("An important reason for this is that their eggs are often eaten by other birds.", "大きな理由は、卵が他の鳥にしばしば食べられることだ。", "is / are eaten"),
    sp("To prevent this, macaw eggs are sometimes removed from their nests by scientists and replaced with chicken eggs.", "これを防ぐため、科学者が卵を巣から取り出し、ニワトリの卵と交換することがある。", "are removed and replaced"),
    sp("The scientists keep the eggs safe.", "科学者は卵を安全に保つ。", "keep"),
    sp("After the macaw chicks come out of their eggs, they are returned to their parents.", "ひなが卵からかえると、親のもとへ戻される。", "are returned"),
]

passage_2b = {
    "label": "B",
    "title": "More than Just a Pretty Bird",
    "paragraphs": passage_2b_paragraphs,
    "translations": passage_2b_translations,
    "sentencePairs": passage_2b_pairs,
    "questions": [
        make_question(24, None, None,
            ["On the contrary", "Under this", "What is worse", "Like before"],
            ["それどころか", "この下で", "さらに悪いことに", "以前のように"], 3,
            ["前文を否定して逆を述べる関係ではない。", "Under this だけでは接続表現にならない。", "違法取引に加え森林破壊というさらに悪い状況を追加している。", "過去との同様性を述べていない。"],
            "What is worse は文全体をつなぐ挿入句で「さらに悪いことに」。",
            source_evidence=["many are dying because the forests where they live are being cleared"]),
        make_question(25, None, None,
            ["often go back for more", "sometimes drop them", "also eat leaves and flowers", "bring them to their nests"],
            ["しばしばもっと取りに戻る", "ときどきそれらを落とす", "葉や花も食べる", "巣へ持ち帰る"], 2,
            ["戻ることでは、種が開けた場所に残る説明にならない。", "運ぶ途中で果実や木の実を落とし、その種が木に育つという流れ。", "葉や花を食べることは種の拡散につながらない。", "巣に持ち帰るなら、本文の cleared areas で種が育つ説明にならない。"],
            "observe A doing と同様、本文では行動とその結果を追う。them は fruits and nuts。",
            source_evidence=["the seeds inside the fruits and nuts grow into trees"]),
        make_question(26, None, None,
            ["do not build nests", "are not easy to catch", "have poor hearing", "lose many babies"],
            ["巣を作らない", "捕まえにくい", "聴力が弱い", "多くのひなを失う"], 4,
            ["巣があるからこそ卵を取り出して交換できる。", "保護のため捕獲が難しいという説明ではない。", "聴力についての記述はない。", "卵が他の鳥に食べられるため、多くのひなが育たないことが難点。"],
            "One difficulty is that ... で、that節が difficulty の具体的内容を示す。",
            source_evidence=["their eggs are often eaten by other birds"]),
    ],
}


passage_3a_paragraphs = [
    "Dear Mr. Stein,",
    "Thank you for placing an order by telephone with Jenna Marks of our sales department this morning. The order was for 500 medium-sized black paper cups with your café's name and logo printed on them. According to Jenna's notes on the order, you need these cups to be delivered to you by Saturday.",
    "I am sorry to say that we do not have any medium-sized black coffee cups at this time. What is more, the machine that makes our coffee cups is currently not working. The part that is broken was sent for repair the other day, but it will not be returned to our factory until Friday. Because of this, I am writing to you to suggest some alternatives.",
    "If you really need black cups, then we have them in small and large sizes. However, I guess that size is more important than color for you. We have medium-sized coffee cups in white, and we could print your logo on these instead. We also have medium-sized cups in brown. We are really sorry about this problem. Please let us know which of these options is best, and we'll send you an additional 50 cups for free. Our delivery company says we will need to send the order by Wednesday so that it arrives by Saturday. Please let me know your decision as soon as you can.",
    "Sincerely,\nNoel Lander\nCustomer Support\nCoffee Shop Supplies",
]

passage_3a_translations = [
    "スタイン様",
    "今朝、当社営業部のジェナ・マークスに電話でご注文いただき、ありがとうございます。注文は、お店の名前とロゴを印刷した中サイズの黒い紙コップ500個でした。ジェナの注文メモによれば、土曜日までの配達をご希望です。",
    "申し訳ありませんが、現在、中サイズの黒いコーヒーカップは在庫がありません。さらに、製造機械も現在故障中です。壊れた部品は先日修理に出しましたが、工場に戻るのは金曜日です。そのため、代替案をご提案します。",
    "黒が必要なら、小サイズと大サイズはあります。ただ、色よりサイズの方が重要だと思います。中サイズなら白があり、代わりにそれへロゴを印刷できます。茶色の中サイズもあります。ご迷惑をおかけして申し訳ありません。どの案がよいかお知らせいただければ、50個を無料で追加します。土曜日着にするには水曜日までに発送する必要があるため、できるだけ早くご決定ください。",
    "敬具\nノエル・ランダー\nカスタマーサポート\nコーヒーショップ用品社",
]

passage_3a_pairs = [
    sp("Thank you for placing an order by telephone with Jenna Marks of our sales department this morning.", "今朝、当社営業部のジェナ・マークスに電話でご注文いただき、ありがとうございます。", "Thank"),
    sp("The order was for 500 medium-sized black paper cups with your café's name and logo printed on them.", "注文は、お店の名前とロゴを印刷した中サイズの黒い紙コップ500個だった。", "was"),
    sp("According to Jenna's notes on the order, you need these cups to be delivered to you by Saturday.", "ジェナの注文メモによれば、土曜日までにこれらのカップを配達してもらう必要がある。", "need"),
    sp("I am sorry to say that we do not have any medium-sized black coffee cups at this time.", "申し訳ないが、現在、中サイズの黒いコーヒーカップは一つも在庫がない。", "am / do have"),
    sp("What is more, the machine that makes our coffee cups is currently not working.", "さらに、当社のコーヒーカップを作る機械は現在動いていない。", "is working"),
    sp("The part that is broken was sent for repair the other day, but it will not be returned to our factory until Friday.", "壊れた部品は先日修理に出されたが、金曜日まで工場に戻らない。", "was sent / will be returned"),
    sp("Because of this, I am writing to you to suggest some alternatives.", "このため、いくつかの代替案を提案するために書いている。", "am writing"),
    sp("If you really need black cups, then we have them in small and large sizes.", "黒いカップがどうしても必要なら、小サイズと大サイズがある。", "have"),
    sp("However, I guess that size is more important than color for you.", "しかし、あなたには色よりサイズの方が重要だと思う。", "guess"),
    sp("We have medium-sized coffee cups in white, and we could print your logo on these instead.", "中サイズなら白があり、代わりにそれへロゴを印刷できる。", "have / could print"),
    sp("We also have medium-sized cups in brown.", "茶色の中サイズもある。", "have"),
    sp("We are really sorry about this problem.", "この問題について本当に申し訳なく思っている。", "are"),
    sp("Please let us know which of these options is best, and we'll send you an additional 50 cups for free.", "どの案が最善か知らせていただければ、50個を無料で追加する。", "let / will send"),
    sp("Our delivery company says we will need to send the order by Wednesday so that it arrives by Saturday.", "配送会社によると、土曜日着にするには水曜日までに発送する必要がある。", "says"),
    sp("Please let me know your decision as soon as you can.", "できるだけ早く決定を知らせてほしい。", "let"),
]

passage_3a = {
    "label": "A",
    "title": "Your order",
    "format": "email",
    "meta": {
        "from": "Noel Lander <noel@coffeeshopsupplies.com>",
        "to": "Gary Stein <thedaydreamcoffeeshop@goodmail.com>",
        "date": "June 5",
        "subject": "Your order",
    },
    "paragraphs": passage_3a_paragraphs,
    "translations": passage_3a_translations,
    "sentencePairs": passage_3a_pairs,
    "questions": [
        make_question(27, None, None,
            ["wrote down the wrong name on Mr. Stein's order.", "gave a customer the wrong delivery date.", "contacted the sales department by telephone.", "took an order for cups for Mr. Stein's café."],
            ["スタイン氏の注文に誤った名前を書いた。", "客に誤った配達日を伝えた。", "電話で営業部へ連絡した。", "スタイン氏のカフェ用カップの注文を受けた。"], 4,
            ["名前を誤記したとは書かれていない。", "Saturday という希望日をメモしており、誤った日付を伝えた記述はない。", "電話をかけたのは注文者側で、ジェナは営業部で注文を受けた。", "placing an order ... with Jenna と order was for 500 ... cups が根拠。"],
            "take an order は「注文を受ける」。place an order with 人 は「人に注文する」。",
            question="This morning, Jenna Marks",
            question_translation="今朝、ジェナ・マークスは",
            source_evidence=["placing an order by telephone with Jenna Marks", "The order was for 500 medium-sized black paper cups"]),
        make_question(28, None, None,
            ["His company does not have the cups that Mr. Stein wants.", "His company's machine cannot print Mr. Stein's logo.", "The cups cannot be delivered to Mr. Stein until Friday.", "The cups were lost by the delivery company the other day."],
            ["会社にはスタイン氏が望むカップがない。", "会社の機械ではスタイン氏のロゴを印刷できない。", "カップは金曜日までスタイン氏へ配達できない。", "先日、配送会社がカップを紛失した。"], 1,
            ["medium-sized black coffee cups が在庫にない、と明記されている。", "故障中なのはカップを作る機械で、ロゴ印刷機とは書かれていない。", "金曜日に戻るのは修理中の部品で、カップの配達ではない。", "紛失ではなく、部品を修理に出した。"],
            "the cups that Mr. Stein wants は関係代名詞 that が cups を修飾する。",
            question="According to Noel Lander, what is the problem with the order?",
            question_translation="ノエル・ランダーによると、注文にはどのような問題がありますか。",
            source_evidence=["we do not have any medium-sized black coffee cups at this time"]),
        make_question(29, None, None,
            ["Ordering more than 50 cups next time.", "Using cups that are white or brown.", "Offering his customers free coffee.", "Buying his cups from another company."],
            ["次回は50個より多く注文すること。", "白または茶色のカップを使うこと。", "客へ無料のコーヒーを出すこと。", "別会社からカップを買うこと。"], 2,
            ["無料で追加するのが50個であり、次回注文数の提案ではない。", "中サイズの白と茶色を代替案として具体的に示している。", "無料なのは追加のカップで、コーヒーではない。", "自社にある別の色・サイズを提案しており、他社購入は勧めていない。"],
            "suggest A to 人／suggest that ... で提案。本文の instead が代替案の目印。",
            question="What does Noel Lander suggest to Mr. Stein?",
            question_translation="ノエル・ランダーはスタイン氏に何を提案していますか。",
            source_evidence=["We have medium-sized coffee cups in white", "We also have medium-sized cups in brown"]),
    ],
}


passage_3b_paragraphs = [
    "Tweed is the name given to a type of thick cloth that was first developed by farmers in Scotland and Ireland. Long pieces of wool are dyed different colors and then put together to make a cloth with a pattern. The weather in Scotland and Ireland is often cold and wet, so this warm, waterproof material was very popular with the farmers as they worked in the fields.",
    "Tweed did not become well known outside farming communities until the 19th century. At that time, wealthy English people were buying large areas of land in Scotland. These were known as estates, and they were used by their owners for hunting and fishing. Hunters became interested in tweed because it is mainly brown, green, or gray, so wild animals find it difficult to see people wearing clothes made of the material. The wealthy English owners began having patterns of tweed made for their estates. After Queen Victoria's husband, Prince Albert, had a unique pattern made for the people on a royal estate in Scotland, the cloth became famous throughout the United Kingdom.",
    "Clothes made from tweed became standard items for wealthy people to wear in the countryside. Men would wear blue or black suits when doing business in towns and cities, and tweed suits when they went to relax on their estates. Ordinary people began to imitate them by wearing tweed for outdoor hobbies such as playing golf or cycling. The fashion for wearing tweed also spread to the United States and the rest of Europe, and tweed became even more popular in the 20th century when various famous fashion designers used it for their clothes.",
    "Tweed remained fashionable for many years, though by the start of the 21st century, its popularity had dropped. However, tweed is now starting to become popular once more. One reason for this is that it does little harm to the environment. In addition to being made from natural wool, it is strong enough to last for a very long time, so people do not often need to buy new clothes. Indeed, some wealthy people in the United Kingdom still wear their grandparents' tweed suits.",
]

passage_3b_translations = [
    "ツイードとは、スコットランドとアイルランドの農民が最初に開発した厚手の布の一種に付けられた名称である。長い羊毛をさまざまな色に染め、組み合わせて模様のある布にする。両地域は寒く雨が多いため、この暖かく防水性のある素材は、畑で働く農民にとても人気だった。",
    "ツイードが農村の外で知られるようになったのは19世紀になってからだった。当時、裕福なイングランド人がスコットランドの広大な土地を買い、狩猟や釣りに使っていた。ツイードは主に茶・緑・灰色で野生動物から見つかりにくいため、猟師が注目した。裕福な所有者は自分の領地用の模様を作らせ始めた。ヴィクトリア女王の夫アルバート公が王室領地の人々用に独自模様を作らせると、英国中で有名になった。",
    "ツイード服は裕福な人が田舎で着る定番となった。男性は都市で仕事をするときは青や黒のスーツを、領地でくつろぐときはツイードを着た。一般の人もゴルフやサイクリングなど屋外の趣味で着て、彼らをまねた。この流行は米国や欧州各地にも広がり、20世紀には有名デザイナーが採用してさらに人気になった。",
    "ツイードは長年流行したが、21世紀初めには人気が落ちていた。しかし現在また人気が戻り始めている。理由の一つは環境への害が少ないことだ。天然羊毛製であるうえ非常に長持ちするため、頻繁に服を買い替えなくてよい。英国では祖父母のツイードスーツを今も着る裕福な人もいる。",
]

passage_3b_pairs = [
    sp("Tweed is the name given to a type of thick cloth that was first developed by farmers in Scotland and Ireland.", "ツイードとは、スコットランドとアイルランドの農民が最初に開発した厚手の布の一種に付けられた名称である。", "is"),
    sp("Long pieces of wool are dyed different colors and then put together to make a cloth with a pattern.", "長い羊毛をさまざまな色に染め、その後組み合わせて模様のある布にする。", "are dyed and put"),
    sp("The weather in Scotland and Ireland is often cold and wet, so this warm, waterproof material was very popular with the farmers as they worked in the fields.", "両地域は寒く雨が多いため、この暖かく防水性のある素材は畑で働く農民にとても人気だった。", "is / was"),
    sp("Tweed did not become well known outside farming communities until the 19th century.", "ツイードが農村の外で知られるようになったのは19世紀になってからだった。", "did become"),
    sp("At that time, wealthy English people were buying large areas of land in Scotland.", "当時、裕福なイングランド人はスコットランドの広大な土地を買っていた。", "were buying"),
    sp("These were known as estates, and they were used by their owners for hunting and fishing.", "それらは領地として知られ、所有者が狩猟や釣りに使っていた。", "were known / were used"),
    sp("Hunters became interested in tweed because it is mainly brown, green, or gray, so wild animals find it difficult to see people wearing clothes made of the material.", "ツイードは主に茶・緑・灰色で、野生動物から着用者が見えにくいため、猟師が関心を持った。", "became / find"),
    sp("The wealthy English owners began having patterns of tweed made for their estates.", "裕福なイングランド人所有者は、自分の領地用にツイードの模様を作らせ始めた。", "began"),
    sp("After Queen Victoria's husband, Prince Albert, had a unique pattern made for the people on a royal estate in Scotland, the cloth became famous throughout the United Kingdom.", "ヴィクトリア女王の夫アルバート公がスコットランドの王室領地の人々用に独自模様を作らせると、その布は英国中で有名になった。", "became"),
    sp("Clothes made from tweed became standard items for wealthy people to wear in the countryside.", "ツイード製の服は裕福な人が田舎で着る定番品になった。", "became"),
    sp("Men would wear blue or black suits when doing business in towns and cities, and tweed suits when they went to relax on their estates.", "男性は都市で仕事をするときは青や黒のスーツを、領地でくつろぐときはツイードスーツを着た。", "would wear"),
    sp("Ordinary people began to imitate them by wearing tweed for outdoor hobbies such as playing golf or cycling.", "一般の人もゴルフやサイクリングなど屋外の趣味でツイードを着て、彼らをまね始めた。", "began"),
    sp("The fashion for wearing tweed also spread to the United States and the rest of Europe, and tweed became even more popular in the 20th century when various famous fashion designers used it for their clothes.", "ツイードを着る流行は米国や欧州各地にも広がり、20世紀には有名デザイナーが服に使ってさらに人気になった。", "spread / became"),
    sp("Tweed remained fashionable for many years, though by the start of the 21st century, its popularity had dropped.", "ツイードは長年流行したが、21世紀初めには人気が落ちていた。", "remained / had dropped"),
    sp("However, tweed is now starting to become popular once more.", "しかし現在、ツイードは再び人気になり始めている。", "is starting"),
    sp("One reason for this is that it does little harm to the environment.", "その理由の一つは、環境への害が少ないことだ。", "is / does"),
    sp("In addition to being made from natural wool, it is strong enough to last for a very long time, so people do not often need to buy new clothes.", "天然羊毛製であるうえ非常に長持ちするため、人々は頻繁に新しい服を買う必要がない。", "is / do need"),
    sp("Indeed, some wealthy people in the United Kingdom still wear their grandparents' tweed suits.", "実際、英国では祖父母のツイードスーツを今も着る裕福な人もいる。", "wear"),
]

passage_3b = {
    "label": "B",
    "title": "Tweed",
    "paragraphs": passage_3b_paragraphs,
    "translations": passage_3b_translations,
    "sentencePairs": passage_3b_pairs,
    "questions": [
        make_question(30, None, None,
            ["it helped keep them warm and dry while they were outside.", "it helped them to make some money in their free time.", "it allowed them to use any extra wool they produced.", "it allowed them to teach their culture to younger people."],
            ["屋外で暖かく乾いた状態を保つのに役立った。", "自由時間にお金を稼ぐ助けになった。", "余った羊毛を使えるようにした。", "若い人へ文化を教えられるようにした。"], 1,
            ["cold and wet に対し warm, waterproof とあるため、暖かく濡れにくかった。", "農民がツイード販売で収入を得たという記述はない。", "余った羊毛の利用が人気の理由とは書かれていない。", "文化継承についての説明はない。"],
            "help keep O C で「OをCの状態に保つのを助ける」。while は同時性。",
            question="Tweed was popular with farmers in Scotland and Ireland because",
            question_translation="ツイードがスコットランドとアイルランドの農民に人気だったのはなぜですか。",
            source_evidence=["this warm, waterproof material was very popular with the farmers"]),
        make_question(31, None, None,
            ["He often went hunting on land owned by farmers in Scotland.", "He bought an estate in Scotland where there was a tweed factory.", "He was seen wearing it while traveling in Scotland.", "He ordered a special tweed pattern for an estate in Scotland."],
            ["スコットランドで農民所有地へよく狩りに行った。", "ツイード工場のある領地を買った。", "旅行中に着ている姿を見られた。", "スコットランドの領地用に特別な模様を注文した。"], 4,
            ["狩りへ行ったことが有名にした、とは書かれていない。", "領地購入や工場の記述はない。", "本人が着ていたことではなく、模様を作らせたことが契機。", "had a unique pattern made の言い換え。これで英国中に有名になった。"],
            "have + 目的語 + 過去分詞で「目的語を…してもらう・させる」。",
            question="How did Prince Albert help to make tweed well-known?",
            question_translation="アルバート公はどのようにツイードが有名になるのを助けましたか。",
            source_evidence=["Prince Albert, had a unique pattern made for the people on a royal estate"]),
        make_question(32, None, None,
            ["doing business in towns and cities.", "visiting the United States and Europe.", "trying to show that they were farmers.", "enjoying leisure activities outside."],
            ["都市で仕事をしているとき。", "米国や欧州を訪れているとき。", "農民だと示そうとするとき。", "屋外の余暇活動を楽しむとき。"], 4,
            ["都市で仕事をするとき青・黒のスーツを着たのは裕福な男性。", "流行が米国や欧州へ広がったのであり、旅行時の服装ではない。", "一般の人は裕福な人をまねたのであって、農民を装ったのではない。", "outdoor hobbies such as playing golf or cycling の言い換え。"],
            "by doing は手段。such as は具体例を挙げる。",
            question="Ordinary people wore tweed when they were",
            question_translation="一般の人々がツイードを着たのはどのようなときですか。",
            source_evidence=["wearing tweed for outdoor hobbies such as playing golf or cycling"]),
        make_question(33, None, None,
            ["It does not release harmful smoke when it is burned.", "It does not become dirty easily and needs little washing.", "It is tough enough for people to wear it for many years.", "It is made by hand in small factories run by families."],
            ["燃やしても有害な煙を出さない。", "汚れにくく、ほとんど洗濯を必要としない。", "丈夫で何年も着られる。", "家族経営の小工場で手作りされる。"], 3,
            ["燃焼時の煙について本文にない。", "汚れや洗濯回数について本文にない。", "strong enough to last for a very long time の言い換え。買い替えを減らせる。", "製造場所や手作りについて本文にない。"],
            "形容詞 + enough to do で「…するのに十分～」。In addition to doing は「…に加えて」。",
            question="What is one reason that tweed does little harm to the environment?",
            question_translation="ツイードが環境へほとんど害を与えない理由の一つは何ですか。",
            source_evidence=["it is strong enough to last for a very long time"]),
    ],
}


passage_3c_paragraphs = [
    "Humans who lived before the development of farming left many stone objects behind. These objects are usually parts of tools or weapons, and they show us how these people obtained their food. However, less is known about other parts of their culture. The other source of information we have from this period is paintings on the walls inside caves. These are mostly hunting scenes, so while they show that early humans lived in groups, they do not show that early humans participated in other social activities, such as religious ceremonies.",
    "The lack of evidence led many historians to believe that religions did not develop until humans started to build farms and live in villages. A recent discovery, though, suggests that religious beliefs may have existed before this time. The Shigir Idol is a tall wooden statue that has faces and symbols carved into it. Experts say that it is very likely that these symbols express religious beliefs about the gods they worshipped.",
    "The Shigir Idol was actually found in Russia in 1890. For a long time, people did not know how old it was, but analysis of the wood in the last few years has revealed that it was made around 12,500 years ago—long before humans in the area began farming. The statue was made in several pieces so that it could be taken down and set up again in a different place as the humans who owned it moved around. Unfortunately, some pieces were lost during the early 20th century and only drawings of them remain.",
    "At some point in history, the Shigir Idol fell into a kind of mud that kept it safe for thousands of years. The conditions in which it was found are very rare. Indeed, no other wooden statues of a similar age have been discovered. Judging from the quality of the Shigir Idol, early humans were skilled at making things from wood. However, few wooden items have survived. Despite this, the Shigir Idol has shown historians that early humans had more advanced cultures than people once thought and that they probably also had religions.",
]

passage_3c_translations = [
    "農耕の発達以前に暮らした人々は多くの石器を残した。これらは道具や武器の一部で、食料をどう得ていたかを示す。しかし文化の他の面はあまり分かっていない。もう一つの情報源は洞窟壁画である。大半は狩猟場面で、集団生活は示すものの、宗教儀式など他の社会活動への参加は示していない。",
    "証拠不足から、多くの歴史家は、人間が農地を作り村に住み始めるまで宗教は発達しなかったと考えた。しかし近年の発見は、それ以前にも宗教的信仰が存在した可能性を示す。シギルの偶像は、顔や記号が彫られた背の高い木像である。専門家は記号が崇拝した神々への宗教的信仰を表す可能性が高いと言う。",
    "シギルの偶像は1890年にロシアで発見された。長い間年代不明だったが、近年の木材分析で約12,500年前、地域で農耕が始まるはるか以前の作と判明した。所有者が移動する際に別の場所で分解・再設置できるよう複数の部品で作られた。残念ながら20世紀初頭に一部が失われ、図だけが残る。",
    "歴史上のある時点で、偶像は特殊な泥に落ち、何千年も保存された。発見時の条件は非常にまれで、同年代の木像はほかに見つかっていない。品質から、初期人類は木工に熟練していたと判断できる。しかし現存する木製品は少ない。それでもこの偶像は、初期人類の文化が従来考えられた以上に進み、おそらく宗教もあったことを歴史家に示した。",
]

passage_3c_pairs = [
    sp("Humans who lived before the development of farming left many stone objects behind.", "農耕の発達以前に暮らした人々は、多くの石器を残した。", "left"),
    sp("These objects are usually parts of tools or weapons, and they show us how these people obtained their food.", "これらは通常、道具や武器の一部で、人々が食料をどう得ていたかを示す。", "are / show"),
    sp("However, less is known about other parts of their culture.", "しかし、文化の他の面についてはあまり分かっていない。", "is known"),
    sp("The other source of information we have from this period is paintings on the walls inside caves.", "この時代についてのもう一つの情報源は、洞窟内の壁画である。", "is"),
    sp("These are mostly hunting scenes, so while they show that early humans lived in groups, they do not show that early humans participated in other social activities, such as religious ceremonies.", "大半は狩猟場面で、初期人類の集団生活は示すが、宗教儀式など他の社会活動への参加は示さない。", "are / show"),
    sp("The lack of evidence led many historians to believe that religions did not develop until humans started to build farms and live in villages.", "証拠不足は、多くの歴史家に、人間が農地を作り村に住み始めるまで宗教は発達しなかったと考えさせた。", "led"),
    sp("A recent discovery, though, suggests that religious beliefs may have existed before this time.", "しかし近年の発見は、それ以前にも宗教的信仰が存在した可能性を示す。", "suggests"),
    sp("The Shigir Idol is a tall wooden statue that has faces and symbols carved into it.", "シギルの偶像は、顔や記号が彫られた背の高い木像である。", "is"),
    sp("Experts say that it is very likely that these symbols express religious beliefs about the gods they worshipped.", "専門家は、これらの記号が人々の崇拝した神々への宗教的信仰を表す可能性が非常に高いと言う。", "say"),
    sp("The Shigir Idol was actually found in Russia in 1890.", "シギルの偶像は実際には1890年にロシアで発見された。", "was found"),
    sp("For a long time, people did not know how old it was, but analysis of the wood in the last few years has revealed that it was made around 12,500 years ago—long before humans in the area began farming.", "長い間年代不明だったが、近年の木材分析で約12,500年前、地域で農耕が始まるはるか以前の作と判明した。", "did know / has revealed"),
    sp("The statue was made in several pieces so that it could be taken down and set up again in a different place as the humans who owned it moved around.", "所有者が移動する際に別の場所で分解・再設置できるよう、像は複数の部品で作られた。", "was made"),
    sp("Unfortunately, some pieces were lost during the early 20th century and only drawings of them remain.", "残念ながら20世紀初頭に一部が失われ、図だけが残る。", "were lost / remain"),
    sp("At some point in history, the Shigir Idol fell into a kind of mud that kept it safe for thousands of years.", "歴史上のある時点で、シギルの偶像は何千年も安全に保つ泥の一種へ落ちた。", "fell"),
    sp("The conditions in which it was found are very rare.", "それが発見された条件は非常にまれである。", "are"),
    sp("Indeed, no other wooden statues of a similar age have been discovered.", "実際、同じくらい古い木像はほかに発見されていない。", "have been discovered"),
    sp("Judging from the quality of the Shigir Idol, early humans were skilled at making things from wood.", "シギルの偶像の品質から判断すると、初期人類は木でものを作ることに熟練していた。", "were"),
    sp("However, few wooden items have survived.", "しかし、現存する木製品は少ない。", "have survived"),
    sp("Despite this, the Shigir Idol has shown historians that early humans had more advanced cultures than people once thought and that they probably also had religions.", "それでも、偶像は初期人類の文化が従来考えられた以上に進み、おそらく宗教もあったことを歴史家に示した。", "has shown"),
]

passage_3c = {
    "label": "C",
    "title": "Clues from the Distant Past",
    "paragraphs": passage_3c_paragraphs,
    "translations": passage_3c_translations,
    "sentencePairs": passage_3c_pairs,
    "questions": [
        make_question(34, None, None,
            ["Whether or not they lived in caves.", "How they were able to get things to eat.", "Where their groups originally came from.", "Which kinds of animals they used to hunt."],
            ["洞窟に住んでいたかどうか。", "食べ物をどう得られたか。", "集団が元々どこから来たか。", "どの種類の動物を狩ったか。"], 2,
            ["洞窟について分かるのは壁画で、石器から居住場所は判断していない。", "show us how these people obtained their food の言い換え。", "集団の起源についての記述はない。", "食料の入手法は分かるが、動物種まで分かるとは書かれていない。"],
            "how S V は間接疑問で「SがどのようにVするか」。",
            question="What can be learned from the stone objects left behind by early humans?",
            question_translation="初期人類が残した石器から何が分かりますか。",
            source_evidence=["they show us how these people obtained their food"]),
        make_question(35, None, None,
            ["has the faces of famous historical leaders carved into it.", "may show that early humans believed in the existence of gods.", "is a symbol of the importance of farming to early humans.", "was probably at the center of one of the first human villages."],
            ["有名な歴史的人物の顔が彫られている。", "初期人類が神々の存在を信じていたことを示す可能性がある。", "初期人類にとって農耕が重要だったことの象徴である。", "最初期の村の一つの中心にあった可能性が高い。"], 2,
            ["faces はあるが、有名な歴史的人物の顔とは書かれていない。", "symbols express religious beliefs about the gods の言い換え。", "農耕開始より前の像で、農耕の重要性を示すものではない。", "村の中心にあったという記述はない。"],
            "may have existed は過去の可能性。believe in ... は「…の存在を信じる」。",
            question="The Shigir Idol is a wooden statue that",
            question_translation="シギルの偶像はどのような木像ですか。",
            source_evidence=["these symbols express religious beliefs about the gods they worshipped"]),
        make_question(36, None, None,
            ["The humans who owned it made drawings that show how to set it up.", "Some of the pieces that make up the statue have never been found.", "The statue can be put together in a number of different ways.", "It was made by people who had not yet begun growing their own food."],
            ["所有者が組み立て方を示す図を描いた。", "像を構成する一部の部品が一度も発見されていない。", "像はいくつもの異なる方法で組み立てられる。", "まだ自分たちの食料を栽培し始めていない人々が作った。"], 4,
            ["図は失われた部品を記録したもので、所有者作とも組立説明とも書かれていない。", "一部は20世紀初頭に失われたので、最初から未発見ではない。", "分解・再設置できたが、異なる組み方があるとは書かれていない。", "約12,500年前で、この地域の人々が農耕を始めるはるか以前だった。"],
            "long before S V は「SがVするずっと前」。had not yet begun は「まだ始めていなかった」。",
            question="What is one thing that has been recently discovered about the Shigir Idol?",
            question_translation="シギルの偶像について近年判明したことの一つは何ですか。",
            source_evidence=["it was made around 12,500 years ago—long before humans in the area began farming"]),
        make_question(37, None, None,
            ["Because the kind of mud in the area where it was found makes digging difficult.", "Because early humans often destroyed the religious statues made by other groups.", "Because few early people had the skills to make something like the Shigir Idol.", "Because wood survives for thousands of years only in very special conditions."],
            ["発見場所の泥が掘削を難しくするから。", "初期人類が他集団の宗教像をよく破壊したから。", "同様のものを作る技能を持つ初期人類が少なかったから。", "木が数千年残るのは非常に特殊な条件だけだから。"], 4,
            ["泥は像を保存したが、掘削を難しくしたとは書かれていない。", "他集団による破壊の説明はない。", "初期人類は木工に熟練していたとあり、技能不足が理由ではない。", "保存条件が非常にまれで、同年代の木像が他にないことが根拠。"],
            "Judging from ... は「…から判断すると」。現在完了 have been discovered は現在までの発見状況。",
            question="Why is the discovery of the Shigir Idol likely to be a unique event?",
            question_translation="シギルの偶像の発見が珍しい出来事だと考えられるのはなぜですか。",
            source_evidence=["The conditions in which it was found are very rare", "no other wooden statues of a similar age have been discovered"]),
        make_question(38, None, None,
            ["The Shigir Idol shows there was cultural exchange between groups of early humans.", "Paintings in caves show early humans participating in religious ceremonies.", "Historians have believed for a long time that humans have always had religions.", "The age of the Shigir Idol was a mystery for many years after it was discovered."],
            ["偶像は初期人類集団間の文化交流を示す。", "洞窟壁画は初期人類が宗教儀式に参加したことを示す。", "歴史家は人類に常に宗教があったと長年信じてきた。", "偶像の年代は発見後長年にわたり謎だった。"], 4,
            ["集団間の文化交流について本文にない。", "壁画は宗教儀式などへの参加を示さない、と本文は明確に否定する。", "歴史家は農耕・定住後に宗教が発達したと考えていた。", "1890年発見後、長い間年代不明で、近年の分析で判明した。"],
            "For a long time と in the last few years の対比が時間関係を示す。",
            question="Which of the following statements is true?",
            question_translation="次の記述のうち正しいものはどれですか。",
            source_evidence=["For a long time, people did not know how old it was"]),
    ],
}


vocab_rows = [
    ("creature", "生き物、動物", "名詞", "Part 1 Q1", "The strange creature lived deep in the ocean.", "その奇妙な生き物は海の深くに住んでいた。"),
    ("military", "軍隊", "名詞", "Part 1 Q2", "He joined the military after high school.", "彼は高校卒業後に軍隊へ入った。"),
    ("accomplish", "達成する、成し遂げる", "動詞", "Part 1 Q3", "She worked hard to accomplish her goal.", "彼女は目標達成のため懸命に努力した。"),
    ("reverse", "覆す、逆にする", "動詞", "Part 1 Q4", "The owner reversed his decision to close the shop.", "店主は閉店するという決定を覆した。"),
    ("sufficient", "十分な", "形容詞", "Part 1 Q5", "We have sufficient time to finish the report.", "私たちには報告書を終える十分な時間がある。"),
    ("severely", "ひどく、深刻に", "副詞", "Part 1 Q6", "The building was severely damaged by the fire.", "建物は火事でひどく損傷した。"),
    ("accompany", "同行する、付き添う", "動詞", "Part 1 Q7", "Her friend accompanied her to the party.", "友人がパーティーへ彼女に同行した。"),
    ("mission", "任務、使命", "名詞", "Part 1 Q8", "Their mission is to repair the satellite.", "彼らの任務は衛星を修理することだ。"),
    ("mixture", "混合物", "名詞", "Part 1 Q9", "The students used the mixture in an experiment.", "生徒たちは実験でその混合物を使った。"),
    ("launch", "打ち上げる、開始する", "動詞", "Part 1 Q10", "Bad weather delayed the plan to launch the rocket.", "悪天候でロケット打ち上げ計画が遅れた。"),
    ("tear off", "ちぎり取る", "句動詞", "Part 1 Q11", "He tore off a sheet of paper from his notebook.", "彼はノートから紙を一枚ちぎり取った。"),
    ("come close to", "もう少しで…する、…に近づく", "熟語", "Part 1 Q12", "Derek came close to winning the tournament.", "デレクはもう少しで大会に優勝するところだった。"),
    ("follow through", "最後まで実行する", "句動詞", "Part 1 Q13", "The teacher followed through with his warning.", "先生は警告したことを最後まで実行した。"),
    ("run into", "偶然出会う", "句動詞", "Part 1 Q14", "I ran into an old friend near the station.", "駅の近くで旧友に偶然会った。"),
    ("content with", "…に満足して", "熟語", "Part 1 Q15", "Neil is content with his work-life balance.", "ニールは仕事と生活のバランスに満足している。"),
    ("by all means", "ぜひ、もちろん", "熟語", "Part 1 Q16", "By all means, invite your friends to the barbecue.", "ぜひ友達をバーベキューに招いてください。"),
    ("make a mess", "散らかす", "熟語", "Part 1 Q17", "The child made a mess with the toys.", "その子はおもちゃを散らかした。"),
    ("but for", "…がなければ", "熟語", "Part 1 Q18", "But for her help, I would not have won.", "彼女の助けがなければ、私は勝てなかっただろう。"),
    ("had better", "…したほうがよい", "助動詞句", "Part 1 Q19", "You had better not stay up late tonight.", "今夜は夜更かししないほうがよい。"),
    ("It's time", "そろそろ…する時だ", "構文", "Part 1 Q20", "It's time you started planning for college.", "そろそろ大学の計画を始める時だ。"),
    ("be concerned about", "…を心配している", "熟語", "Part 2A", "Many people are concerned about plastic waste.", "多くの人がプラスチックごみを心配している。"),
    ("plastic waste", "プラスチックごみ", "名詞句", "Part 2A", "The city is trying to reduce plastic waste.", "その市はプラスチックごみを減らそうとしている。"),
    ("end up as", "結局…になる", "熟語", "Part 2A", "Much of the plastic ends up as trash in rivers.", "多くのプラスチックが結局川のごみになる。"),
    ("in response", "それに応じて", "熟語", "Part 2A", "In response, the government proposed a ban.", "それに応じて政府は禁令を提案した。"),
    ("be forced to", "…せざるを得ない", "熟語", "Part 2A", "The government was forced to change its plan.", "政府は計画を変更せざるを得なかった。"),
    ("unemployment", "失業、失業状態", "名詞", "Part 2A", "Leaders worried about an increase in unemployment.", "指導者たちは失業増加を心配した。"),
    ("nevertheless", "それにもかかわらず", "副詞", "Part 2A", "The task was difficult; nevertheless, they continued.", "課題は難しかったが、それでも彼らは続けた。"),
    ("come to an end", "終わる", "熟語", "Part 2A", "The use of plastic cups came to an end.", "プラスチックカップの使用は終わった。"),
    ("replace A with B", "AをBに替える", "熟語", "Part 2A", "The stations replaced plastic cups with clay cups.", "駅はプラスチックカップを素焼きのカップに替えた。"),
    ("kulhad", "クルハド（インドの素焼きカップ）", "名詞", "Part 2A", "Tea was served in a traditional kulhad.", "茶は伝統的なクルハドで出された。"),
    ("break down", "分解される、壊れる", "句動詞", "Part 2A", "Clay cups soon break down in the soil.", "素焼きのカップは土の中ですぐ分解される。"),
    ("substance", "物質", "名詞", "Part 2A", "The cup becomes a harmless substance.", "そのカップは害のない物質になる。"),
    ("by hand", "手作業で", "熟語", "Part 2A", "The clay cups are made by hand.", "その素焼きカップは手作りされる。"),
    ("estimate", "見積もる、推定する", "動詞", "Part 2A", "The government estimates that many jobs will be created.", "政府は多くの雇用が生まれると見積もっている。"),
    ("create jobs", "雇用を生み出す", "熟語", "Part 2A", "The new industry could create jobs in rural areas.", "新産業は地方に雇用を生み出せる。"),
    ("species", "（生物の）種", "名詞", "Part 2B", "One-third of parrot species are in danger.", "オウム種の3分の1が危機にある。"),
    ("be in danger of", "…の危険にさらされている", "熟語", "Part 2B", "Some birds are in danger of dying out.", "一部の鳥は絶滅の危険にさらされている。"),
    ("die out", "絶滅する、消滅する", "句動詞", "Part 2B", "Several wild species may die out.", "いくつかの野生種は絶滅するかもしれない。"),
    ("illegally", "違法に", "副詞", "Part 2B", "Some parrots are sold illegally as pets.", "一部のオウムはペットとして違法に売られる。"),
    ("clear", "（土地を）切り開く", "動詞", "Part 2B", "Forests are cleared to create farmland.", "農地を作るため森林が切り開かれる。"),
    ("farmland", "農地", "名詞", "Part 2B", "The forest was turned into farmland.", "その森林は農地に変えられた。"),
    ("reveal", "明らかにする", "動詞", "Part 2B", "The study revealed the birds' important role.", "研究は鳥の重要な役割を明らかにした。"),
    ("play a role", "役割を果たす", "熟語", "Part 2B", "Parrots play a role in helping forests recover.", "オウムは森林回復を助ける役割を果たす。"),
    ("spread seeds", "種を広げる", "熟語", "Part 2B", "The birds spread seeds over long distances.", "鳥は長い距離にわたって種を広げる。"),
    ("observe A doing", "Aが…するのを観察する", "構文", "Part 2B", "Researchers observed the birds carrying fruit.", "研究者は鳥が果実を運ぶのを観察した。"),
    ("conservation", "保護、自然保護", "名詞", "Part 2B", "Conservation groups protect rare parrots.", "保護団体は希少なオウムを守る。"),
    ("prevent", "防ぐ", "動詞", "Part 2B", "Scientists acted to prevent the loss of eggs.", "科学者は卵の損失を防ぐため行動した。"),
    ("remove A from B", "AをBから取り除く", "熟語", "Part 2B", "Scientists remove the eggs from the nests.", "科学者は巣から卵を取り出す。"),
    ("alternative", "代替案、代わりのもの", "名詞", "Part 3A", "The company suggested several alternatives.", "会社はいくつかの代替案を示した。"),
    ("additional", "追加の", "形容詞", "Part 3A", "The company offered 50 additional cups.", "会社はカップを50個追加で提供した。"),
    ("waterproof", "防水の", "形容詞", "Part 3B", "Tweed was a warm, waterproof material.", "ツイードは暖かく防水性のある素材だった。"),
    ("estate", "（広大な）領地、地所", "名詞", "Part 3B", "The family owned an estate in Scotland.", "その家族はスコットランドに領地を所有していた。"),
    ("imitate", "まねる", "動詞", "Part 3B", "Ordinary people began to imitate the wealthy.", "一般の人々は裕福な人をまね始めた。"),
    ("leisure", "余暇", "名詞", "Part 3B", "They wore tweed for outdoor leisure activities.", "彼らは屋外の余暇活動でツイードを着た。"),
    ("fashionable", "流行の、おしゃれな", "形容詞", "Part 3B", "Tweed remained fashionable for many years.", "ツイードは長年流行し続けた。"),
    ("do harm to", "…に害を与える", "熟語", "Part 3B", "The material does little harm to the environment.", "その素材は環境にほとんど害を与えない。"),
    ("in addition to", "…に加えて", "熟語", "Part 3B", "In addition to being natural, tweed is durable.", "天然素材であることに加え、ツイードは丈夫だ。"),
    ("religious ceremony", "宗教儀式", "名詞句", "Part 3C", "The paintings did not show a religious ceremony.", "壁画は宗教儀式を示していなかった。"),
    ("belief", "信仰、信念", "名詞", "Part 3C", "The symbols may express a religious belief.", "その記号は宗教的信仰を表す可能性がある。"),
    ("carve", "彫る", "動詞", "Part 3C", "Faces and symbols were carved into the statue.", "顔や記号が像に彫られていた。"),
    ("analysis", "分析", "名詞", "Part 3C", "Analysis of the wood revealed the statue's age.", "木材の分析で像の年代が判明した。"),
    ("set up", "組み立てる、設置する", "句動詞", "Part 3C", "The statue could be taken down and set up again.", "その像は分解して再設置できた。"),
    ("survive", "生き残る、現存する", "動詞", "Part 3C", "Few wooden items have survived.", "現存する木製品は少ない。"),
    ("be skilled at", "…に熟練している", "熟語", "Part 3C", "Early humans were skilled at working with wood.", "初期人類は木工に熟練していた。"),
    ("despite", "…にもかかわらず", "前置詞", "Part 3C", "Despite the missing pieces, the statue gave historians new clues.", "部品が欠けていても、その像は歴史家に新たな手掛かりを与えた。"),
]


def slugify(word):
    return "_".join(filter(None, "".join(
        ch.lower() if ch.isalnum() else " " for ch in word
    ).split()))


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
        "word": word,
        "meaning": meaning,
        "pos": pos,
        "level": "2級",
        "source": source,
        "example": example,
        "exampleJa": example_ja,
        "distractors": distractors,
        "wordAudio": f"audio/vocab/w_{index + 1:03d}_{slugify(word)}.mp3",
    })


focus_points = [
    {
        "id": "fp1",
        "title": "be forced to do（…せざるを得ない）",
        "subtitle": "Passive Voice + Infinitive",
        "explanation": "be forced to do は force A to do（Aに…させる）の受動態で、「…することを強いられる」「…せざるを得ない」を表す。本人の意思ではなく外部事情による変更を読み取る目印になる。",
        "sourceQuote": "the government was forced to change its plans",
        "sourceLocation": "Part 2A",
        "examples": [
            {"en": "The government was forced to change its plans.", "ja": "政府は計画変更を余儀なくされた。", "note": "経済状況と失業への懸念が外部要因。"},
            {"en": "The match was forced to stop because of heavy rain.", "ja": "大雨のため試合は中止せざるを得なかった。", "note": "受動態で避けられない事情を表す。"},
            {"en": "She was forced to choose another route.", "ja": "彼女は別の経路を選ばざるを得なかった。", "note": "be forced to + 動詞原形。"},
        ],
        "practicePassage": {
            "en": "[Source: An Answer in a Teacup]\nIn response, the Indian government planned to introduce a ban on plastic items that could only be used once. In the end, though, the government was forced to change its plans because of the condition of the economy and worries about an increase in unemployment.",
            "ja": "これを受け、インド政府は使い捨てプラスチック製品の禁止を導入する予定だった。しかし結局、経済状況と失業増加への懸念から計画変更を余儀なくされた。",
            "audioFile": "audio/practice_pp1.mp3",
        },
        "practiceQuestions": [
            {"q": "be forced to change の主語は誰ですか。", "a": "the government（インド政府）です。"},
            {"q": "政府が計画変更を余儀なくされた理由を2点答えてください。", "a": "経済状況と、失業増加への懸念です。"},
            {"q": "force A to do を受動態にするとどうなりますか。", "a": "A is forced to do となります。"},
            {"q": "could only be used once は何を修飾しますか。", "a": "plastic items を修飾し、「一度しか使えないプラスチック製品」という意味です。"},
        ],
        "highlightPatterns": ["was forced to change", "could only be used once"],
        "highlightColor": "#FF6B6B",
        "highlightLabel": "be forced to",
    },
    {
        "id": "fp2",
        "title": "replace A with B（AをBに替える）",
        "subtitle": "Replacement and Materials",
        "explanation": "replace A with B は「AをBに置き換える」。受動態では A is replaced with B となる。本文の be made from / be made with / be made by と合わせ、材料・手段・行為者を区別する。",
        "sourceQuote": "have replaced plastic teacups with brown clay teacups",
        "sourceLocation": "Part 2A",
        "examples": [
            {"en": "The stations replaced plastic teacups with clay teacups.", "ja": "駅はプラスチックのティーカップを素焼きのカップに替えた。", "note": "A=plastic teacups、B=clay teacups。"},
            {"en": "Macaw eggs are replaced with chicken eggs.", "ja": "コンゴウインコの卵はニワトリの卵と交換される。", "note": "受動態の replace A with B。"},
            {"en": "Kulhads are made by hand from clay.", "ja": "クルハドは粘土から手作りされる。", "note": "by は手段・行為、from は原料。"},
        ],
        "practicePassage": {
            "en": "[Source: An Answer in a Teacup]\nAll 7,000 railway stations in India have replaced plastic teacups with brown clay teacups called kulhads. Plastic cups are made with machines, but kulhads are made by hand.",
            "ja": "インドの全7,000駅がプラスチックのティーカップをクルハドと呼ばれる茶色い素焼きのカップに替えた。プラスチックカップは機械製だが、クルハドは手作りである。",
            "audioFile": "audio/practice_pp2.mp3",
        },
        "practiceQuestions": [
            {"q": "replace A with B のAとBを本文から答えてください。", "a": "Aは plastic teacups、Bは brown clay teacups called kulhads です。"},
            {"q": "are made with machines の with は何を示しますか。", "a": "製造に使う手段・道具（機械）です。"},
            {"q": "are made by hand の by hand はどう訳しますか。", "a": "「手作業で、手作りで」です。"},
            {"q": "現在完了 have replaced が示すことは何ですか。", "a": "置換が完了し、その結果が現在にも続いていることです。"},
        ],
        "highlightPatterns": ["replaced plastic teacups with brown clay teacups", "are made by hand"],
        "highlightColor": "#4F8CFF",
        "highlightLabel": "replace A with B",
    },
    {
        "id": "fp3",
        "title": "so that S can ...（目的）と分詞の結果",
        "subtitle": "Purpose and Result",
        "explanation": "so that S can ... は「Sが…できるように」と目的を表す。一方、文末の helping ... は前文全体の結果を補足し「その結果…を助けて」と読む。目的と結果を区別すると長文の因果関係を追いやすい。",
        "sourceQuote": "so that they can eat the fruits and nuts later",
        "sourceLocation": "Part 2B",
        "examples": [
            {"en": "The birds carry the fruits so that they can eat them later.", "ja": "鳥は後で食べられるよう果実を運ぶ。", "note": "so that 以下は行動の目的。"},
            {"en": "The seeds grow into trees, helping the forests to recover.", "ja": "種は木に育ち、その結果、森林の回復を助ける。", "note": "helping は結果を添える現在分詞。"},
            {"en": "Scientists protect the eggs so that the chicks can survive.", "ja": "ひなが生き残れるよう、科学者は卵を守る。", "note": "can は目的節内の可能。"},
        ],
        "practicePassage": {
            "en": "[Source: More than Just a Pretty Bird]\nThe birds do this so that they can eat the fruits and nuts later. However, they sometimes drop them. When this happens in areas cleared by humans, the seeds inside the fruits and nuts grow into trees, helping the forests to recover.",
            "ja": "鳥は後で果実や木の実を食べられるよう、こうしている。しかし、ときどきそれらを落とす。人間が切り開いた場所でこれが起こると、中の種が木に育ち、その結果、森林の回復を助ける。",
            "audioFile": "audio/practice_pp3.mp3",
        },
        "practiceQuestions": [
            {"q": "so that they can eat ... は何の目的ですか。", "a": "鳥が果実や木の実を遠くまで運ぶ目的です。"},
            {"q": "them は何を指しますか。", "a": "the fruits and nuts を指します。"},
            {"q": "helping the forests to recover の意味上の主語は何ですか。", "a": "直前の出来事、つまり種が木に育つことです。"},
            {"q": "areas cleared by humans の cleared は何を修飾しますか。", "a": "areas を後ろから修飾し、「人間によって切り開かれた地域」です。"},
        ],
        "highlightPatterns": ["so that they can eat", "helping the forests to recover"],
        "highlightColor": "#22C55E",
        "highlightLabel": "purpose / result",
    },
    {
        "id": "fp4",
        "title": "not ... until と have O done",
        "subtitle": "Time Limit and Causative Form",
        "explanation": "not ... until は「…するまで～しない」から「…して初めて～する」と読む。have O done は「Oを…してもらう・させる」で、本文では特別なツイード模様を作らせた行為を表す。",
        "sourceQuote": "did not become well known ... until the 19th century",
        "sourceLocation": "Part 3B",
        "examples": [
            {"en": "Tweed did not become well known until the 19th century.", "ja": "ツイードが広く知られたのは19世紀になってからだった。", "note": "19世紀まで知られなかった。"},
            {"en": "Prince Albert had a unique pattern made.", "ja": "アルバート公は独自の模様を作らせた。", "note": "have + O + 過去分詞。"},
            {"en": "The part will not be returned until Friday.", "ja": "その部品は金曜日まで戻らない。", "note": "Part 3Aにも同じ not ... until。"},
        ],
        "practicePassage": {
            "en": "[Source: Tweed]\nTweed did not become well known outside farming communities until the 19th century. After Prince Albert had a unique pattern made for the people on a royal estate in Scotland, the cloth became famous throughout the United Kingdom.",
            "ja": "ツイードが農村の外で広く知られたのは19世紀になってからだった。アルバート公がスコットランドの王室領地の人々用に独自模様を作らせると、その布は英国中で有名になった。",
            "audioFile": "audio/practice_pp4.mp3",
        },
        "practiceQuestions": [
            {"q": "not ... until の時点を本文から答えてください。", "a": "the 19th century（19世紀）です。"},
            {"q": "had a unique pattern made は誰が模様を作りましたか。", "a": "実際の製作者は明示されず、アルバート公が誰かに作らせたことを示します。"},
            {"q": "the cloth became famous のきっかけは何ですか。", "a": "アルバート公が王室領地用の独自模様を作らせたことです。"},
            {"q": "outside farming communities はどう訳しますか。", "a": "「農村共同体の外で」です。"},
        ],
        "highlightPatterns": ["did not become well known outside farming communities until", "had a unique pattern made"],
        "highlightColor": "#F59E0B",
        "highlightLabel": "not until / have O done",
    },
    {
        "id": "fp5",
        "title": "現在完了で「近年の発見」を追う",
        "subtitle": "Present Perfect and Evidence",
        "explanation": "has revealed / have been discovered / have survived は、過去の発見や保存結果が現在の知識につながることを示す。for a long time、in the last few years、no other などの時間・範囲表現と合わせて読む。",
        "sourceQuote": "analysis of the wood in the last few years has revealed",
        "sourceLocation": "Part 3C",
        "examples": [
            {"en": "Analysis of the wood has revealed the statue's age.", "ja": "木材分析で像の年代が明らかになった。", "note": "発見結果が現在の知識になっている。"},
            {"en": "No other wooden statues have been discovered.", "ja": "ほかに木像は発見されていない。", "note": "受動態の現在完了。"},
            {"en": "Few wooden items have survived.", "ja": "現存する木製品は少ない。", "note": "過去から現在まで残る。"},
        ],
        "practicePassage": {
            "en": "[Source: Clues from the Distant Past]\nFor a long time, people did not know how old the Shigir Idol was, but analysis of the wood in the last few years has revealed that it was made around 12,500 years ago. Indeed, no other wooden statues of a similar age have been discovered.",
            "ja": "長い間シギルの偶像の年代は不明だったが、近年の木材分析で約12,500年前の作と判明した。実際、同年代の木像はほかに発見されていない。",
            "audioFile": "audio/practice_pp5.mp3",
        },
        "practiceQuestions": [
            {"q": "has revealed の主語は何ですか。", "a": "analysis of the wood in the last few years です。"},
            {"q": "何が近年明らかになりましたか。", "a": "像が約12,500年前、地域の農耕開始よりはるか前に作られたことです。"},
            {"q": "have been discovered は何態ですか。", "a": "現在完了の受動態です。"},
            {"q": "for a long time と in the last few years の対比から何が分かりますか。", "a": "長年不明だった年代が、近年の分析でようやく明らかになったことです。"},
        ],
        "highlightPatterns": ["has revealed that it was made", "have been discovered", "have survived"],
        "highlightColor": "#A855F7",
        "highlightLabel": "present perfect",
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
for section in sections:
    all_questions.extend(section.get("questions", []))
    for passage in section.get("passages", []):
        all_questions.extend(passage.get("questions", []))

assert [item["number"] for item in all_questions] == list(range(1, 39))
assert {item["number"]: item["answer"] for item in all_questions} == ANSWERS
assert [len(passage["questions"]) for passage in [passage_2a, passage_2b, passage_3a, passage_3b, passage_3c]] == [3, 3, 3, 4, 5]
assert all(len(item["choiceAnalysis"]) == 4 for item in all_questions)
assert all(item["choiceAnalysis"][item["answer"] - 1].count("→正解。💡") == 1 for item in all_questions)

data = {
    "grade": "2級",
    "year": "2022",
    "session": "1",
    "title": "2022年度 第1回 英語資格検定2級 リーディング",
    "exam": "2022-1",
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
