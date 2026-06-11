# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検準2級プラス data.json
Step A: 大問1（vocabulary型）Q1〜17 — リッチ解説
一次ソース: 2026-1(本会場）/準2級プラス解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(17)までの(　)に入れるのに最も適切なものを1, 2, 3, 4の中から一つ選び、その番号を解答用紙の所定欄にマークしなさい。",
    "questions": [
        {
            "number": 1,
            "text": "A: Excuse me. I wanted to buy a pair of tennis shoes, but I couldn't find any on the shelf.\nB: Let me check our ( ). One moment, please.",
            "translation": "A：すみません。テニスシューズを買いたかったのですが、棚に見当たりませんでした。\nB：当店の( )を確認しますね。少々お待ちください。",
            "choices": ["permission", "audience", "horizon", "inventory"],
            "choiceTranslations": ["許可", "観客", "地平線", "在庫"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ permission＝許可。check our permission（許可を確認する）では、棚に商品がないという客の相談に応えられない",
                "❌ audience＝観客。check our audience（観客を確認する）は店員の対応として不自然。商品探しの場面と無関係",
                "❌ horizon＝地平線。check our horizon では「地平線を確認する」となり、店舗の文脈に全く合わない",
                "✅ inventory＝在庫。棚にない商品を探す場面で、店員が在庫を確認する check our inventory が自然→正解",
            ],
            "grammar": "💡 inventory＝在庫。check inventory＝在庫を確認する。on the shelf（棚に）にない→倉庫・在庫を調べる、という流れが決め手。",
        },
        {
            "number": 2,
            "text": "Many people in Japan do not follow any ( ), but they often take part in traditional festivals that come from the beliefs of ancient Japanese people.",
            "translation": "日本では特定の( )を持たない人も多いが、古代日本人の信仰に由来する伝統的な祭りにはよく参加する。",
            "choices": ["religion", "condition", "enthusiasm", "progress"],
            "choiceTranslations": ["宗教", "状態", "熱意", "進歩"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ religion＝宗教。do not follow any religion（特定の宗教を信仰しない）と、beliefs of ancient Japanese people（古代の信仰）から来る祭り参加が対比として自然→正解",
                "❌ condition＝状態。follow any condition（状態に従う）では「信仰・宗教」の話にならない",
                "❌ enthusiasm＝熱意。follow enthusiasm ではコロケーションが不自然。祭りの起源である beliefs とは結びつかない",
                "❌ progress＝進歩。follow any progress では「進歩に従う」となり、宗教・信仰の文脈に合わない",
            ],
            "grammar": "💡 follow a religion＝（特定の）宗教を信仰する。but 以降の traditional festivals / beliefs が「宗教」との対比を示すヒント。",
        },
        {
            "number": 3,
            "text": "Scientists are worried about the ( ) of gases from cars. They think that these gases are bad for the environment.",
            "translation": "科学者たちは自動車からのガスの( )を心配している。これらのガスは環境に悪いと考えている。",
            "choices": ["principal", "shortage", "emission", "custom"],
            "choiceTranslations": ["校長・主要な", "不足", "排出", "習慣・関税"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ principal＝校長・主要なもの。the principal of gases では「ガスの校長」となり意味不成立",
                "❌ shortage＝不足。the shortage of gases from cars（車からのガスの不足）では、環境問題の文脈と逆のニュアンス",
                "✅ emission＝排出。the emission of gases from cars（自動車からのガスの排出）＋bad for the environment が一致→正解",
                "❌ custom＝習慣・関税。the custom of gases では「ガスの習慣」となり、環境汚染の話に結びつかない",
            ],
            "grammar": "💡 emission＝排出（emit「放出する」＋-ion）。gases from cars（車からのガス）＋bad for the environment が排出問題を示す。",
        },
        {
            "number": 4,
            "text": "A: Did you buy batteries for the camera?\nB: Yes, and I also bought some extra ones to ( ) that we don't run out.",
            "translation": "A：カメラ用の電池は買った？\nB：うん、それに切れないよう( )するために予備も買ったよ。",
            "choices": ["express", "stare", "greet", "ensure"],
            "choiceTranslations": ["表現する", "じっと見る", "挨拶する", "確実にする"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ express＝表現する。express that we don't run out では「切れないことを表現する」となり、予備購入の目的と合わない",
                "❌ stare＝じっと見る。stare that ～ という構文は成立しない",
                "❌ greet＝挨拶する。greet that we don't run out では文法的に不自然",
                "✅ ensure＝確実にする。ensure that ～（～であることを確実にする）が定型。extra ones（予備）＋don't run out（切れない）→正解",
            ],
            "grammar": "💡 ensure that ～＝～であることを確実にする。run out＝使い果たす・なくなる。予備を買う理由を表す典型パターン。",
        },
        {
            "number": 5,
            "text": "A: What are you going to do this weekend, Karen?\nB: I'm going to ( ) some friends at my house. We're going to have a party.",
            "translation": "A：今週末何をするの、カレン？\nB：家で友達を( )するつもりよ。パーティーをするの。",
            "choices": ["repair", "wander", "explain", "entertain"],
            "choiceTranslations": ["修理する", "さまよう", "説明する", "もてなす"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ repair＝修理する。repair some friends（友達を修理する）では意味が通らない",
                "❌ wander＝さまよう。wander some friends では文法的に不自然。パーティーの文脈と合わない",
                "❌ explain＝説明する。explain some friends（友達を説明する）では at my house / have a party と結びつかない",
                "✅ entertain＝もてなす。entertain friends at my house（家で友達をもてなす）＋have a party が自然→正解",
            ],
            "grammar": "💡 entertain＝もてなす・楽しませる。entertain guests at home は「家で客をもてなす」の定番表現。",
        },
        {
            "number": 6,
            "text": "A: What did you do in your camping class today, Bill?\nB: We learned about the ( ) skills needed for camping, like building a shelter and starting a fire.",
            "translation": "A：今日のキャンプの授業で何をしたの、ビル？\nB：キャンプに必要な( )のスキルについて学んだよ。避難所を作ったり火を起こしたりするような。",
            "choices": ["guarantee", "wealth", "affection", "survival"],
            "choiceTranslations": ["保証", "富", "愛情", "サバイバル・生存"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ guarantee＝保証。survival skills ではなく guarantee skills では「保証のスキル」となり、シェルター・火起こしと結びつかない",
                "❌ wealth＝富。wealth skills では「富のスキル」となり、野外での生活技術の文脈に合わない",
                "❌ affection＝愛情。affection skills では意味が通らない。building a shelter とは無関係",
                "✅ survival＝サバイバル・生存。survival skills（サバイバルスキル）＋building a shelter / starting a fire が一致→正解",
            ],
            "grammar": "💡 survival skills＝サバイバルスキル・生存に必要な技術。building a shelter（避難所を作る）・starting a fire（火を起こす）が手がかり。",
        },
        {
            "number": 7,
            "text": "A: I'm going to go to Canada next month. I hope I don't have any problems with the money.\nB: You should ( ) some Japanese yen to Canadian dollars before you go.",
            "translation": "A：来月カナダに行くの。お金で困らないといいんだけど。\nB：行く前に日本円をカナダドルに( )したほうがいいよ。",
            "choices": ["protect", "imagine", "convert", "detect"],
            "choiceTranslations": ["保護する", "想像する", "両替する・変換する", "検出する"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ protect＝保護する。protect yen to dollars では「円をドルに保護する」となり、通貨の話として不自然",
                "❌ imagine＝想像する。imagine yen to dollars では両替の意味にならない",
                "✅ convert＝両替する・変換する。convert A to B（AをBに換える）が通貨交換の定型。problems with the money が手がかり→正解",
                "❌ detect＝検出する。detect yen to dollars では「円をドルに検出する」となり意味不成立",
            ],
            "grammar": "💡 convert A to B＝AをBに変換する・両替する。Japanese yen to Canadian dollars が具体的な換金の場面を示す。",
        },
        {
            "number": 8,
            "text": "Tom is very good at drawing people's faces. He can ( ) their emotions so well that it is easy to see how each person was feeling when Tom drew them.",
            "translation": "トムは人の顔を描くのがとても上手だ。感情をうまく( )するので、トムが描いたときその人がどんな気持ちだったかすぐわかる。",
            "choices": ["exclude", "shoot", "cure", "portray"],
            "choiceTranslations": ["除外する", "撃つ・撮影する", "治す", "描く・表現する"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ exclude＝除外する。exclude their emotions（感情を除外する）では、感情が「見える」という文脈と矛盾",
                "❌ shoot＝撃つ・撮影する。shoot their emotions では「感情を撃つ」となり、絵画の文脈に合わない",
                "❌ cure＝治す。cure their emotions では「感情を治す」となり、drawing faces とは無関係",
                "✅ portray＝描く・表現する。portray emotions（感情を表現する）＋drawing people's faces / how each person was feeling→正解",
            ],
            "grammar": "💡 portray＝（絵・言葉で）描写する・表現する。so ～ that …（とても～なので…）が感情表現のうまさを強調。",
        },
        {
            "number": 9,
            "text": "A: Look at the man. He fell off his bicycle.\nB: He was going too fast. You have to go at a ( ) pace, Mike.",
            "translation": "A：あの男性を見て。自転車から落ちたわ。\nB：速すぎたんだよ。もっと( )ペースで行かないと、マイク。",
            "choices": ["steadier", "braver", "freer", "politer"],
            "choiceTranslations": ["より安定した", "より勇敢な", "より自由な", "より丁寧な"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ steadier＝より安定した。going too fast（速すぎた）への忠告として、a steadier pace（より安定したペース）が自然→正解",
                "❌ braver＝より勇敢な。a braver pace では「勇敢なペース」となり、転倒の原因である speed への対策にならない",
                "❌ freer＝より自由な。a freer pace では「自由なペース」となり、安全運転の助言として不適切",
                "❌ politer＝より丁寧な。a politer pace では「丁寧なペース」となり、速度・安定性の話と結びつかない",
            ],
            "grammar": "💡 pace＝ペース・速度。too fast への対比として steadier（より安定した）が選ばれる。fall off his bicycle が速度の問題を示す。",
        },
        {
            "number": 10,
            "text": "The weather in Russia is ( ) cold in winter. In Moscow, the average temperature in January is around -10 degrees Celsius.",
            "translation": "ロシアの冬の天気は( )寒い。モスクワでは1月の平均気温が摂氏マイナス10度前後だ。",
            "choices": ["publicly", "briefly", "shortly", "extremely"],
            "choiceTranslations": ["公に", "短く", "まもなく", "極めて"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ publicly＝公に。publicly cold では「公に寒い」となり、気温の程度を表せない",
                "❌ briefly＝短く。briefly cold では「短く寒い」となり、冬の気候の描写として不自然",
                "❌ shortly＝まもなく。shortly cold では「まもなく寒くなる」という意味になり、平均気温 -10℃ の説明と合わない",
                "✅ extremely＝極めて。extremely cold（極めて寒い）＋average temperature around -10℃ が一致→正解",
            ],
            "grammar": "💡 extremely＝極めて（程度を強調する副詞）。具体的な気温 -10 degrees Celsius が「極めて寒い」の根拠。",
        },
        {
            "number": 11,
            "text": "A: My computer is really old. I hope it doesn't ( ) before I finish my report.\nB: I hope so, too. It would be a disaster.",
            "translation": "A：私のコンピューターは本当に古いの。レポートを終える前に( )しないといいんだけど。\nB：私もそう願うわ。大変なことになるわね。",
            "choices": ["break down", "dress up", "look around", "shake off"],
            "choiceTranslations": ["故障する", "着飾る", "見回る", "振り払う"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ break down＝故障する。古い computer が before I finish my report の前に故障する、という心配が自然。It would be a disaster とも呼応→正解",
                "❌ dress up＝着飾る。computer doesn't dress up では意味が通らない",
                "❌ look around＝見回る。computer doesn't look around では機械の動作として不自然",
                "❌ shake off＝振り払う。computer doesn't shake off では故障の心配を表せない",
            ],
            "grammar": "💡 break down＝（機械が）故障する。really old な computer ＋ finish my report まで動いてほしい、という文脈が決め手。",
        },
        {
            "number": 12,
            "text": "Before writing his novel, Michael had to ( ) a lot of research. He spent many hours reading books and searching on the Internet.",
            "translation": "小説を書く前に、マイケルはたくさんの調査を( )しなければならなかった。何時間も本を読んだりインターネットで調べたりした。",
            "choices": ["decide on", "come up", "go through", "consent to"],
            "choiceTranslations": ["決める", "生じる・出てくる", "調べる・経験する", "同意する"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ decide on＝決める。decide on a lot of research では「調査を決める」となり、reading books / searching の行動と合わない",
                "❌ come up＝生じる・出てくる。had to come up a lot of research では文法的に不自然",
                "✅ go through＝調べる・経験する。go through research（調査を行う・くまなく調べる）＋reading books and searching on the Internet→正解",
                "❌ consent to＝同意する。consent to research では「調査に同意する」となり、実際に調べる行為の描写と合わない",
            ],
            "grammar": "💡 go through ～＝～をくまなく調べる・経験する。第2文の reading books / searching on the Internet が go through research の具体的内容。",
        },
        {
            "number": 13,
            "text": "The new president has made some changes to the way the company is run. ( ), the changes seem to be working well.",
            "translation": "新社長は会社の運営方法にいくつか変更を加えた。( )のところ、その変更はうまく機能しているようだ。",
            "choices": ["So far", "For free", "As well", "In vain"],
            "choiceTranslations": ["これまでのところ", "無料で", "同様に・また", "無駄に"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ So far＝これまでのところ。変更を加えた直後の現時点での評価として、the changes seem to be working well と自然に結びつく→正解",
                "❌ For free＝無料で。For free, the changes seem… では「無料で変更がうまくいっている」となり不自然",
                "❌ As well＝同様に・また。文頭の As well では「変更がうまくいっている」という評価の導入として弱い",
                "❌ In vain＝無駄に。In vain, the changes seem to be working well では意味が矛盾する",
            ],
            "grammar": "💡 So far＝これまでのところ（現時点までの評価）。変更の効果を述べるとき、まだ結果が確定していないニュアンスを出せる。",
        },
        {
            "number": 14,
            "text": "A: What will you do if your boss says no when you ask for time off?\nB: I'll go to the beach ( ) he says no. I need a break!",
            "translation": "A：休みを頼んだら上司がダメと言ったらどうするの？\nB：彼がダメと言う( )ビーチに行くわ。休みが必要なの！",
            "choices": ["as though", "only if", "even if", "only when"],
            "choiceTranslations": ["まるで〜のように", "〜の場合のみ", "たとえ〜でも", "〜の時だけ"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ as though＝まるで〜のように。go to the beach as though he says no では「ダメと言うように見えてビーチに行く」となり不自然",
                "❌ only if＝〜の場合のみ。only if he says no だと「ダメと言われた場合だけ行く」となり、I need a break!（休みが必要）と矛盾",
                "✅ even if＝たとえ〜でも。上司の許可がなくても行く、という強い意思。I need a break! と一致→正解",
                "❌ only when＝〜の時だけ。only when he says no では「ダメと言った時だけ行く」となり、文脈と合わない",
            ],
            "grammar": "💡 even if＝たとえ〜でも（譲歩）。上司が no と言っても行く、という決意を表す。I need a break! が even if 選びの根拠。",
        },
        {
            "number": 15,
            "text": "The city of Ironton is not very big, but it is easy to get to ( ) a new highway that connects it to the larger city of Winsterville.",
            "translation": "アイアントン市はあまり大きくないが、ウィンスタービルという大きな都市と結ぶ新しい高速道路( )行きやすい。",
            "choices": ["for fear of", "for the sake of", "in case of", "by way of"],
            "choiceTranslations": ["〜を恐れて", "〜のために", "〜の場合に", "〜経由で"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ for fear of＝〜を恐れて。get to for fear of a highway では「高速道路を恐れて行く」となり、easy to get to と矛盾",
                "❌ for the sake of＝〜のために。for the sake of a highway では「高速道路のために行く」となり、到達の容易さを表せない",
                "❌ in case of＝〜の場合に。in case of a highway では「高速道路の場合に行きやすい」となり不自然",
                "✅ by way of＝〜経由で。get to ～ by way of a highway（高速道路経由で～に行ける）が交通の定番表現→正解",
            ],
            "grammar": "💡 by way of ～＝～経由で。connects it to the larger city が「高速道路を使って行きやすい」理由を示す。",
        },
        {
            "number": 16,
            "text": "A: I'm sorry. I'm not very good at this game.\nB: It's OK. Just sit ( ) me, and I'll show you how to play.",
            "translation": "A：ごめんなさい。このゲームはあまり得意じゃないんです。\nB：大丈夫だよ。私の( )に座って。やり方を教えるから。",
            "choices": ["aware of", "apart of", "next to", "short of"],
            "choiceTranslations": ["〜を意識して", "〜の一部として", "〜の隣に", "〜が不足して"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ aware of＝〜を意識して。sit aware of me では「私を意識して座る」となり、教える場面として不自然",
                "❌ apart of＝〜の一部として（試験文面の表記）。sit apart of me では「私の一部として座る」となり、物理的な位置を表せない",
                "✅ next to＝〜の隣に。sit next to me（私の隣に座って）＋I'll show you how to play が自然→正解",
                "❌ short of＝〜が不足して。sit short of me ではコロケーションが成立しない",
            ],
            "grammar": "💡 sit next to ～＝～の隣に座る。教えるときに隣に座る、という場面設定が next to を選ぶ手がかり。",
        },
        {
            "number": 17,
            "text": "A: I'm going to the supermarket. Do you need anything?\nB: No, thanks. But ( ) to borrow my car if you want to.",
            "translation": "A：スーパーに行くんだけど、何か要る？\nB：いいえ、結構です。でも、よかったら車を借りて( )。",
            "choices": ["try hard", "devote yourself", "feel free", "take turns"],
            "choiceTranslations": ["一生懸命やる", "専念する", "遠慮なく", "交代する"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ try hard＝一生懸命やる。try hard to borrow my car では「借りるのに一生懸命になる」となり、相手への申し出として不自然",
                "❌ devote yourself＝専念する。devote yourself to borrow では文法的に不自然",
                "✅ feel free＝遠慮なく。feel free to do（遠慮なく～していい）が申し出の定型。borrow my car if you want to と一致→正解",
                "❌ take turns＝交代する。take turns to borrow my car では「交代で借りる」となり、1台の車を貸す場面と合わない",
            ],
            "grammar": "💡 feel free to do＝遠慮なく～していい。相手に許可・申し出をする丁寧な表現。if you want to が補足的な条件。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
