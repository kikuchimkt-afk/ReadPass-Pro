# -*- coding: utf-8 -*-
"""
2026年度 第1回（土曜準会場）英検準2級プラス data.json
Step A: 大問1（vocabulary型）Q1〜17
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade-pre2plus", "2026-1-sat", "data.json",
)

section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "The teacher told the students to ( 1 ) their essays before they handed them in. They had made many mistakes.",
            "translation": "先生は生徒たちに、提出する前にエッセイを( 1 )するよう言いました。たくさんの間違いをしていたのです。",
            "choices": ["separate", "revise", "decrease", "greet"],
            "choiceTranslations": ["分ける", "修正する・見直す", "減らす", "挨拶する"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ separate＝分ける。separate A from B（AをBから分ける）の形で使う。間違いを直す文脈には合わない",
                "✅ revise＝修正する・見直す。第2文のThey had made many mistakes（たくさんの間違い）が決め手。提出前に直す→正解",
                "❌ decrease＝減らす。decrease the number（数を減らす）のように使う。エッセイを「減らす」では意味が通らない",
                "❌ greet＝挨拶する。greet someone（人に挨拶する）の形で使う。essaysを目的語にできない",
            ],
            "grammar": "💡 revise＝修正する（re-「再び」＋vise「見る」）。hand in＝提出する。空所の直後の文が理由のヒントになる典型パターン。",
        },
        {
            "number": 2,
            "text": "When the teacher told the students that they had done a good job on their homework, she made sure to ( 2 ) the students who had worked especially hard.",
            "translation": "先生が宿題をよくできたと生徒に伝えたとき、特に頑張った生徒を( 2 )するようにしました。",
            "choices": ["struggle", "acknowledge", "squeeze", "publish"],
            "choiceTranslations": ["苦労する", "認める・評価する", "絞る", "出版する"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ struggle＝苦労する。struggle to do（～するのに苦労する）は自動詞的。生徒を目的語に「苦労させる」では文脈に合わない",
                "✅ acknowledge＝認める・評価する。done a good job（よくできた）＋worked especially hard（特に頑張った）の流れで「ねぎらい・認める」→正解",
                "❌ squeeze＝絞る・押しつぶす。squeeze a lemon（レモンを絞る）など物理的な動作。頑張った生徒への対応として不自然",
                "❌ publish＝出版する。publish a book（本を出版する）の形。宿題をよくした生徒を「出版する」では意味不成立",
            ],
            "grammar": "💡 acknowledge＝認める・ねぎらう。make sure to do＝必ず～するようにする。especially hard＝特に懸命に。",
        },
        {
            "number": 3,
            "text": "The charity concert raised a lot of money to ( 3 ) the people affected by the earthquake. The concert organizers used the money to buy food and other supplies.",
            "translation": "慈善コンサートは地震の被害者を( 3 )するために多くのお金を集めました。主催者はそのお金で食料などを買いました。",
            "choices": ["lie", "reward", "honor", "aid"],
            "choiceTranslations": ["横たわる・嘘をつく", "報酬を与える", "称える", "援助する"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ lie＝横たわる・嘘をつく。lie the people（人を横たわらせる）では被害者支援の文脈にならない",
                "❌ reward＝報酬を与える。reward someone for ～（～の功績に報いる）の形。被災者への緊急支援には「報酬」ではなく「援助」のニュアンス",
                "❌ honor＝称える・敬意を表する。affected by the earthquake（地震の被害を受けた）人々を「称える」では食料・物資の支援と結びつかない",
                "✅ aid＝援助する。raised money to aid ～（～を援助するために資金を集める）＋buy food and suppliesが一致→正解",
            ],
            "grammar": "💡 aid＝援助する（名詞でも「援助」）。affected by ～＝～の影響を受けた。charity concert＝慈善コンサート。",
        },
        {
            "number": 4,
            "text": "There is no ( 4 ) between the computers in the office. They all have the same software and hardware.",
            "translation": "オフィスのコンピューターには( 4 )がありません。すべて同じソフトウェアとハードウェアです。",
            "choices": ["ratio", "challenge", "bargain", "distinction"],
            "choiceTranslations": ["比率", "挑戦", "お買い得", "違い・区別"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ ratio＝比率。the ratio of A to B（AとBの比率）の形。コンピューター同士に「比率がない」では第2文のsame（同じ）と結びつかない",
                "❌ challenge＝挑戦。no challenge between computers（コンピューター間に挑戦がない）は不自然な言い回し",
                "❌ bargain＝お買い得品。no bargain between（～の間にお買い得がない）はコロケーションとして成立しない",
                "✅ distinction＝違い・区別。no distinction between A and B（AとBの違いがない）＋the same software and hardware→正解",
            ],
            "grammar": "💡 distinction＝違い・区別（distinct「異なる」＋-ion）。no distinction between ～＝～の間に違いがない。",
        },
        {
            "number": 5,
            "text": "A : Who is your favorite ( 5 ), Maya?\nB : I really like the books by Kellan Storme. He wrote many interesting stories.",
            "translation": "A：あなたの好きな( 5 )は誰、マヤ？\nB：ケラン・ストームの本が本当に好きなの。たくさんの面白い物語を書いたのよ。",
            "choices": ["officer", "actor", "author", "engineer"],
            "choiceTranslations": ["役人", "俳優", "作家・著者", "技師"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ officer＝役人・士官。the books by ～（～の本）やwrote stories（物語を書いた）の手がかりと結びつかない",
                "❌ actor＝俳優。俳優は通常「演じる」ので、He wrote many stories（彼が物語を書いた）と矛盾",
                "✅ author＝作家・著者。favorite author＋the books by Kellan Storme＋He wrote many interesting storiesが一貫→正解",
                "❌ engineer＝技師・エンジニア。物語を書く職業の描写と無関係",
            ],
            "grammar": "💡 author＝著者（auth「書く」＋-or「人」）。write stories / books by ～が「作家」を特定する手がかり。",
        },
        {
            "number": 6,
            "text": "A : I finished writing my report, but I don't have any pictures to go with it.\nB : You can ( 6 ) some pictures from the Internet. Just make sure to write where you found them.",
            "translation": "A：レポートは書き終えたんだけど、一緒に載せる写真がないの。\nB：インターネットから写真を( 6 )できるわよ。どこで見つけたか書くのを忘れずに。",
            "choices": ["insert", "melt", "wander", "fold"],
            "choiceTranslations": ["挿入する", "溶かす", "さまよう", "折る"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ insert＝挿入する・入れる。レポートに写真を「入れる」＝insert pictures into a report。出典を書くという注意とも自然に呼応→正解",
                "❌ melt＝溶かす。melt butter（バターを溶かす）など。写真を「溶かす」では意味不成立",
                "❌ wander＝さまよう。wander around（歩き回る）は自動詞。写真を目的語に取れない",
                "❌ fold＝折る。fold paper（紙を折る）。デジタルの写真をレポートに「折る」では文脈に合わない",
            ],
            "grammar": "💡 insert A into B＝AをBに挿入する。go with it＝（レポートに）一緒に載せる。make sure to ～＝必ず～する。",
        },
        {
            "number": 7,
            "text": "The ( 7 ) of students in the class thought that the history test was too difficult. Only a few students thought that it was easy.",
            "translation": "クラスの生徒の( 7 )が歴史のテストは難しすぎると思いました。簡単だと思った生徒はほんの少数だけでした。",
            "choices": ["manner", "majority", "relation", "potential"],
            "choiceTranslations": ["方法・態度", "大多数", "関係", "可能性"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ manner＝方法・態度。the manner of students（生徒の態度）では「大多数」の意味にならない",
                "✅ majority＝大多数。the majority of ～（～の大多数）が定型。Only a few（ほんの少数）との対比が決め手→正解",
                "❌ relation＝関係。the relation of students（生徒の関係）では「多くの生徒が」とは言えない",
                "❌ potential＝可能性。the potential of students（生徒の可能性）ではテストの難易度の意見を表せない",
            ],
            "grammar": "💡 the majority of ～＝～の大多数。a few（少数）との対比が頻出。minority＝少数派。",
        },
        {
            "number": 8,
            "text": "A : You look really tired. Are you OK?\nB : Well, I couldn't sleep well because I had a horrible ( 8 ) about getting lost in a dark forest.",
            "translation": "A：すごく疲れて見えるけど、大丈夫？\nB：うーん、暗い森で迷うというひどい( 8 )を見たせいでよく眠れなかったの。",
            "choices": ["citizen", "nightmare", "display", "location"],
            "choiceTranslations": ["市民", "悪夢", "展示", "場所"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ citizen＝市民。had a horrible citizen（ひどい市民を持っていた）では意味が通らない",
                "✅ nightmare＝悪夢。had a horrible nightmare about ～（～についての悪夢を見た）＋couldn't sleep wellが一致→正解",
                "❌ display＝展示・ディスプレイ。had a display about getting lost では「展示を見た」になり、眠れない理由として不自然",
                "❌ location＝場所。had a location about ～ は文法的に不自然。場所を「持つ」では眠れない原因にならない",
            ],
            "grammar": "💡 nightmare＝悪夢。have a nightmare about ～＝～についての悪夢を見る。because節が空所の意味を裏付ける。",
        },
        {
            "number": 9,
            "text": "A : Congratulations on your promotion! You must feel proud.\nB : Thank you, but I'm just doing my job. I try to stay ( 9 ) and focused on my work.",
            "translation": "A：昇進おめでとう！誇りに思うでしょうね。\nB：ありがとう。でもただ仕事をしているだけよ。謙虚で仕事に集中するよう心がけているの。",
            "choices": ["empty", "sore", "cruel", "humble"],
            "choiceTranslations": ["空の", "痛い", "残酷な", "謙虚な"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ empty＝空の。stay empty（空のままでいる）は人の性格・態度を表さない",
                "❌ sore＝痛い。stay sore（痛いまま）＝体の状態。promotion（昇進）への返答の文脈に合わない",
                "❌ cruel＝残酷な。昇進を祝われたあとに「残酷でいる」は意味が通らない",
                "✅ humble＝謙虚な。I'm just doing my job（ただ仕事をしているだけ）＝誇りを見せない姿勢。stay humble and focused→正解",
            ],
            "grammar": "💡 humble＝謙虚な。promotion（昇進）への返答で「誇りではなく謙虚さ」を示す対比がポイント。stay focused on ～＝～に集中する。",
        },
        {
            "number": 10,
            "text": "A : What are the ingredients in the pumpkin pie you made?\nB : Pumpkin, of course, and spices that are ( 10 ) used in pumpkin pie, like cinnamon and nutmeg.",
            "translation": "A：作ったかぼちゃパイの材料は何？\nB：かぼちゃはもちろん、シナモンやナツメグのようにかぼちゃパイに( 10 )使われるスパイスも入れてるの。",
            "choices": ["kindly", "legally", "commonly", "professionally"],
            "choiceTranslations": ["親切に", "合法的に", "一般的に", "専門的に"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ kindly＝親切に。spices are kindly used（スパイスが親切に使われる）は不自然。副詞の意味が合わない",
                "❌ legally＝合法的に。料理の材料が「合法的に」使われるという文脈ではない",
                "✅ commonly＝一般的に・よく。commonly used in pumpkin pie（かぼちゃパイによく使われる）＝定番のスパイスという説明→正解",
                "❌ professionally＝専門的に・プロとして。家庭のパイの材料説明に「専門的に使われる」は不自然",
            ],
            "grammar": "💡 commonly＝一般的に（common「普通の」＋-ly）。be commonly used in ～＝～によく使われる。ingredients＝材料。",
        },
        {
            "number": 11,
            "text": "A : I think I'll go to the mall tomorrow.\nB : If you ( 11 ) the bookstore, could you get me a copy of this month's fashion magazine?",
            "translation": "A：明日モールに行こうかな。\nB：もし本屋に( 11 )なら、今月のファッション雑誌を買ってきてくれない？",
            "choices": ["give up", "figure out", "fall over", "drop by"],
            "choiceTranslations": ["あきらめる", "理解する・解決する", "転ぶ", "立ち寄る"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ give up＝あきらめる。give up the bookstore（本屋をあきらめる）では「立ち寄る」の意味にならない",
                "❌ figure out＝理解する・解決する。figure out the bookstore（本屋を理解する）では雑誌を買う依頼と結びつかない",
                "❌ fall over＝転ぶ。fall over the bookstore（本屋で転ぶ）では買い物の依頼の前提にならない",
                "✅ drop by＝立ち寄る。If you drop by the bookstore（本屋に寄るなら）＋get me a copy（買ってきて）の流れ→正解",
            ],
            "grammar": "💡 drop by ～＝～に立ち寄る（短時間訪問）。go to the mall（モールに行く）→bookstore（本屋）という流れに注目。",
        },
        {
            "number": 12,
            "text": "A : Could you check the stationery cupboard? We might ( 12 ) some supplies.\nB : You're right. We need to order more pens and folders.",
            "translation": "A：文房具入れを確認してくれる？備品が( 12 )かもしれないわ。\nB：その通りね。ペンやフォルダーをもっと注文しないと。",
            "choices": ["be sure of", "be short of", "be free of", "be kind of"],
            "choiceTranslations": ["〜を確信している", "〜が不足している", "〜がない", "〜の種類である"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ be sure of＝～を確信している。be sure of some supplies（備品を確信している）では不足の意味にならない",
                "✅ be short of＝～が不足している。We need to order more pens and folders（もっと注文が必要）が決め手→正解",
                "❌ be free of＝～がない（自由である）。be free of supplies（備品がない＝備品のない状態）と「注文が必要」は別の状況",
                "❌ be kind of＝～の種類である・ちょっと～。be kind of some supplies では文法的にも意味的にも不成立",
            ],
            "grammar": "💡 be short of ～＝～が不足している。Bのneed to order more（もっと注文する必要がある）が空所の意味を裏付ける。",
        },
        {
            "number": 13,
            "text": "A : I think we should take the squirrel back to its nest.\nB : No, ( 13 ). Its mother will come back for it.",
            "translation": "A：リスを巣に戻すべきだと思う。\nB：いいえ、( 13 )。お母さんが迎えに来るわよ。",
            "choices": ["move it on", "leave it alone", "throw it away", "take it over"],
            "choiceTranslations": ["追い払う", "そのままにしておく", "捨てる", "引き継ぐ"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ move it on＝追い払う・先に進ませる。母親が戻ってくると言うBの意見と矛盾。触らないほうがよい",
                "✅ leave it alone＝そのままにしておく・触らないでおく。Its mother will come back for it（母親が迎えに来る）と自然に呼応→正解",
                "❌ throw it away＝捨てる。母親が迎えに来ると言いながら「捨てる」は矛盾",
                "❌ take it over＝引き継ぐ・乗っ取る。リスの世話を「引き継ぐ」では巣に戻す・そのまま、という文脈に合わない",
            ],
            "grammar": "💡 leave ～ alone＝～をそのままにしておく・干渉しない。will come back for it＝迎えに来る（for＝目的）。",
        },
        {
            "number": 14,
            "text": "A : Thank you for coming to the airport to ( 14 ) my cousin.\nB : No problem. It's nice to have a chance to say goodbye in person.",
            "translation": "A：空港まで来て、いとこを( 14 )てくれてありがとう。\nB：どういたしまして。直接さよならを言える機会があってよかったわ。",
            "choices": ["show off", "hand out", "bring in", "see off"],
            "choiceTranslations": ["見せびらかす", "配る", "連れてくる", "見送る"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ show off＝見せびらかす。show off my cousin（いとこを見せびらかす）では空港でのお別れの場面に合わない",
                "❌ hand out＝配る。hand out my cousin（いとこを配る）では意味不成立",
                "❌ bring in＝連れてくる・導入する。空港でいとこを「連れてくる」は出発の見送りと逆の動き",
                "✅ see off＝見送る。at the airport（空港で）＋say goodbye in person（直接さよなら）が決め手→正解",
            ],
            "grammar": "💡 see ～ off＝～を見送る。空港・駅でのお別れの定番表現。say goodbye in person＝直接さよならを言う。",
        },
        {
            "number": 15,
            "text": "Harvey's family moved to a new town last month. ( 15 ), he made some new friends at school, and he started to enjoy living there.",
            "translation": "ハーヴェイの家族は先月、新しい町に引っ越しました。( 15 )、学校で新しい友達ができ、そこでの生活を楽しむようになりました。",
            "choices": ["For free", "In demand", "On average", "Before long"],
            "choiceTranslations": ["無料で", "需要が高い", "平均して", "まもなく"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ For free＝無料で。友達ができた・生活を楽しんだという出来事の時間関係を表せない",
                "❌ In demand＝需要が高い。人や物が「需要がある」という意味で、友達ができた流れとは無関係",
                "❌ On average＝平均して。統計的な表現で、個人のハーヴェイの体験の時系列を表さない",
                "✅ Before long＝まもなく。moved last month（先月引っ越し）→（まもなく）友達ができて楽しむようになった、という時間の流れ→正解",
            ],
            "grammar": "💡 Before long＝まもなく（＝soon）。引っ越し直後から順調に馴染んでいく流れを表す副詞句。",
        },
        {
            "number": 16,
            "text": "When Sarah was young, she lived next to a bakery. Now, the smell of fresh bread always ( 16 ) her childhood.",
            "translation": "サラは幼い頃、パン屋の隣に住んでいました。今でも焼きたてパンの香りがいつも彼女の幼少時代を( 16 )。",
            "choices": ["learns her from", "hears her from", "reminds her of", "talks her into"],
            "choiceTranslations": ["〜から学ぶ", "〜から聞く", "〜を思い出させる", "〜を説得する"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ learns her from＝彼女が～から学ぶ。learn A from B の形だが、香りが「幼少時代から学ぶ」では意味が通らない",
                "❌ hears her from＝彼女が～から聞く。hear from ～（～から便りがある）の形。香りと幼少時代の結びつきにならない",
                "✅ reminds her of＝彼女に～を思い出させる。remind A of B（AにBを思い出させる）が定型。パン屋の隣＋香り→幼少時代→正解",
                "❌ talks her into＝彼女を～するよう説得する。talk A into doing（Aを説得して～させる）。香りが「説得する」では不自然",
            ],
            "grammar": "💡 remind A of B＝AにBを思い出させる。感覚（smell）が記憶（childhood）を呼び起こす構文が頻出。",
        },
        {
            "number": 17,
            "text": "The weather forecast said it was going to rain all day, but it ( 17 ) to be sunny. In fact, it was the hottest day of the year.",
            "translation": "天気予報では一日中雨になると言っていたのに、結局晴れ( 17 )。実際、今年一番暑い日でした。",
            "choices": ["ran out", "put out", "turned out", "gave out"],
            "choiceTranslations": ["使い果たした", "消した・出した", "結局〜だった", "配った・切れた"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ ran out＝使い果たした・尽きた。it ran out to be sunny（晴れに使い果たした）では文法的に不自然",
                "❌ put out＝消す・出す。put out a fire（火を消す）。天気が「晴れに消した」では意味不成立",
                "✅ turned out＝結局～だった。予報（雨）と実際（晴れ・最高気温）のギャップを表す turn out to be ～→正解",
                "❌ gave out＝配る・（力が）尽きる。gave out to be sunny では「結局晴れだった」という意味にならない",
            ],
            "grammar": "💡 turn out to be ～＝結局～だとわかる。予想と異なる結果を表すときの定番表現。In fact＝実際には。",
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

# 大問1のみ差し替え、他のセクション（大問2・3）は保持する
others = [s for s in data.get("sections", []) if s.get("name") != "大問1"]
data["sections"] = [section1] + others

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Wrote section1 ({len(section1['questions'])} questions) to {DATA_PATH}")
