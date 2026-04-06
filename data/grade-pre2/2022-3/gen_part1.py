"""Generate data.json for Pre-Grade 2 2022-3 (Part 1: sections 0-1, vocabulary)"""
import json, os

data = {
    "grade": "準2級",
    "year": "2022",
    "session": "3",
    "title": "2022年度 第3回 英検準2級 リーディング",
    "vocabulary": [],
    "sections": [],
    "lessonPlan": {}
}

# =====================================================
# Section 0: 大問1（vocabulary型・20問）
# =====================================================
section1 = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(20)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "The lifeguard at the hotel pool told the swimmers not to ( 1 ) there because the pool was not deep enough.",
            "translation": "ホテルのプールのライフガードは、プールが十分深くないので、そこで( 1 )しないように泳いでいる人たちに言った。",
            "choices": ["flow", "melt", "dive", "announce"],
            "choiceTranslations": ["流れる", "溶ける", "飛び込む", "発表する"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ flow＝流れる。水の動きであり泳ぐ人への指示としては不適切",
                "❌ melt＝溶ける。プールの文脈に合わない",
                "✅ dive＝飛び込む。浅いプールでは危険なので禁止→正解",
                "❌ announce＝発表する。プールでの行動とは無関係"
            ],
            "grammar": "💡 dive＝飛び込む。名詞形 diving は水泳競技の「飛び込み」。deep enough＝十分に深い（enough は形容詞の後ろに置く）"
        },
        {
            "number": 2,
            "text": "Greg is going to play in a tennis tournament next weekend. He has only been playing for three months, so he is very ( 2 ) to win.",
            "translation": "グレッグは来週末テニスのトーナメントに出場する予定だ。テニスを始めてまだ3ヶ月なので、勝つ見込みは非常に( 2 )。",
            "choices": ["unlikely", "traditional", "similar", "honest"],
            "choiceTranslations": ["ありそうにない", "伝統的な", "似ている", "正直な"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ unlikely＝ありそうにない。3ヶ月の経験では勝つ可能性が低い→正解",
                "❌ traditional＝伝統的な。勝つことの文脈に合わない",
                "❌ similar＝似ている。文脈に合わない",
                "❌ honest＝正直な。人の性格を表し、勝つこととは無関係"
            ],
            "grammar": "💡 be unlikely to ～＝～する可能性が低い。反意語は likely（ありそうな）。tournament＝トーナメント、勝ち抜き戦"
        },
        {
            "number": 3,
            "text": "Jenny's dream is to become a famous writer. She wants to be like her favorite ( 3 ), who has written over 10 best-selling novels.",
            "translation": "ジェニーの夢は有名な作家になることだ。彼女は10冊以上のベストセラー小説を書いたお気に入りの( 3 )のようになりたいと思っている。",
            "choices": ["astronaut", "accountant", "author", "athlete"],
            "choiceTranslations": ["宇宙飛行士", "会計士", "著者", "運動選手"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ astronaut＝宇宙飛行士。小説を書く人ではない",
                "❌ accountant＝会計士。作家とは別の職業",
                "✅ author＝著者。ベストセラー小説を書いた人→正解",
                "❌ athlete＝運動選手。小説とは無関係"
            ],
            "grammar": "💡 author＝著者、作家。writer と同義。best-selling＝ベストセラーの（最もよく売れている）"
        },
        {
            "number": 4,
            "text": "When the dog took Linda's hat, Linda had to ( 4 ) it around the park to get it back.",
            "translation": "犬がリンダの帽子を取ったとき、リンダは帽子を取り返すために公園中をそれを( 4 )しなければならなかった。",
            "choices": ["chase", "greet", "hire", "share"],
            "choiceTranslations": ["追いかける", "挨拶する", "雇う", "共有する"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ chase＝追いかける。帽子を取った犬を追う→正解",
                "❌ greet＝挨拶する。帽子を取り返す文脈に合わない",
                "❌ hire＝雇う。犬を雇うのは不自然",
                "❌ share＝共有する。帽子を取り返す状況に合わない"
            ],
            "grammar": "💡 chase＝追いかける。chase after ～でも同義。had to ～＝～しなければならなかった"
        },
        {
            "number": 5,
            "text": "It is easy to get around in big cities, such as Osaka and Fukuoka, because they have ( 5 ) of trains and buses.",
            "translation": "大阪や福岡のような大都市は、電車やバスの( 5 )があるので、移動が簡単だ。",
            "choices": ["struggles", "recordings", "networks", "purposes"],
            "choiceTranslations": ["苦闘", "録音", "ネットワーク", "目的"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ struggles＝苦闘。交通手段の説明に合わない",
                "❌ recordings＝録音。電車やバスとは無関係",
                "✅ networks＝ネットワーク。交通網の意味で移動の利便性を説明→正解",
                "❌ purposes＝目的。電車やバスの文脈に合わない"
            ],
            "grammar": "💡 network＝ネットワーク、網。交通ネットワーク（transportation network）。get around＝移動する、あちこち行く"
        },
        {
            "number": 6,
            "text": "The teacher ( 6 ) the class into small groups so they could discuss ideas for their projects.",
            "translation": "先生はプロジェクトのアイデアを話し合えるように、クラスを小さなグループに( 6 )。",
            "choices": ["accepted", "warmed", "divided", "injured"],
            "choiceTranslations": ["受け入れた", "温めた", "分けた", "怪我させた"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ accepted＝受け入れた。クラスをグループにする意味にならない",
                "❌ warmed＝温めた。文脈に合わない",
                "✅ divided＝分けた。クラスを小グループに分ける→正解",
                "❌ injured＝怪我させた。教室の状況に合わない"
            ],
            "grammar": "💡 divide A into B＝AをBに分ける。so (that) they could ～＝～できるように（目的）"
        },
        {
            "number": 7,
            "text": "Sayaka and her father have very different opinions on ( 7 ) such as taxes and the environment.",
            "translation": "サヤカと父親は、税金や環境などの( 7 )について非常に異なる意見を持っている。",
            "choices": ["degrees", "partners", "responses", "issues"],
            "choiceTranslations": ["学位／程度", "パートナー", "反応", "問題"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ degrees＝学位、程度。税金や環境の文脈に合わない",
                "❌ partners＝パートナー。意見を持つ対象としては不適切",
                "❌ responses＝反応。意見の対象としては不自然",
                "✅ issues＝問題、課題。税金や環境は社会的な問題→正解"
            ],
            "grammar": "💡 issue＝問題、課題。problem より公的・社会的な問題に使う。opinions on ～＝～についての意見"
        },
        {
            "number": 8,
            "text": "Austin was sad after his girlfriend left him. However, he quickly forgot about her, and now he is in good ( 8 ) again.",
            "translation": "オースティンは彼女に振られて悲しかった。しかし、すぐに忘れて、今はまた良い( 8 )だ。",
            "choices": ["contests", "spirits", "arguments", "decisions"],
            "choiceTranslations": ["コンテスト", "気分", "議論", "決断"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ contests＝コンテスト。気分の表現としては使わない",
                "✅ spirits＝気分。be in good spirits＝機嫌がいい→正解",
                "❌ arguments＝議論。文脈に合わない",
                "❌ decisions＝決断。気分を表す表現ではない"
            ],
            "grammar": "💡 be in good spirits＝機嫌がいい、気分がいい。spirit は「精神、気分」。複数形 spirits で使う慣用表現"
        },
        {
            "number": 9,
            "text": "A : Is it difficult to grow these flowers?\nB : Not at all. You ( 9 ) plant the seeds in the ground and make sure they get plenty of water.",
            "translation": "A：この花を育てるのは難しいですか？\nB：全然。種を地面に( 9 )植えて、たっぷり水をやるだけです。",
            "choices": ["loudly", "simply", "shortly", "finally"],
            "choiceTranslations": ["大声で", "単に", "まもなく", "ついに"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ loudly＝大声で。花を植える動作には不適切",
                "✅ simply＝単に、ただ～するだけ。簡単さを強調→正解",
                "❌ shortly＝まもなく。植え方の説明には合わない",
                "❌ finally＝ついに。手順の簡単さを説明する文脈に合わない"
            ],
            "grammar": "💡 simply＝単に、ただ～するだけ。Not at all.＝全然（否定の強調）。make sure (that) ～＝～を確かにする"
        },
        {
            "number": 10,
            "text": "Carl was very sorry for breaking his neighbor's window with his baseball. He went to his neighbor's house to ( 10 ). He also promised to be more careful.",
            "translation": "カールは野球のボールで隣の家の窓を割ってしまいとても申し訳なく思った。彼は隣の家に( 10 )しに行った。さらに気をつけると約束した。",
            "choices": ["apologize", "export", "limit", "nod"],
            "choiceTranslations": ["謝罪する", "輸出する", "制限する", "うなずく"],
            "answer": 1,
            "choiceAnalysis": [
                "✅ apologize＝謝罪する。窓を割ったことを謝りに行く→正解",
                "❌ export＝輸出する。日常の文脈に全く合わない",
                "❌ limit＝制限する。謝罪の場面に合わない",
                "❌ nod＝うなずく。わざわざ行く目的としては不十分"
            ],
            "grammar": "💡 apologize＝謝罪する。apologize for ～＝～について謝る。名詞形は apology。be sorry for ～＝～を申し訳なく思う"
        },
        {
            "number": 11,
            "text": "A : Ashley, which dress should I buy?\nB : I don't know. They ( 11 ) to me. They have the same buttons and they're both blue.",
            "translation": "A：アシュリー、どのドレスを買うべきかな？\nB：わからない。私にはそれらは( 11 )。同じボタンがついていて、どちらも青いし。",
            "choices": ["look ahead", "look alike", "catch on", "catch up"],
            "choiceTranslations": ["前を見る", "似ている", "流行する", "追いつく"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ look ahead＝前を見る、先を見据える。ドレスの比較に合わない",
                "✅ look alike＝似て見える。同じボタンで同じ色なので似ている→正解",
                "❌ catch on＝流行する、理解する。文脈に合わない",
                "❌ catch up＝追いつく。ドレスの比較に合わない"
            ],
            "grammar": "💡 look alike＝似て見える。alike は「似ている」を意味する副詞・形容詞。They look alike. は They look similar. と同義"
        },
        {
            "number": 12,
            "text": "Michael had to ( 12 ) the campfire before he went to sleep in the tent. He went to the river to get some water and threw it on the fire.",
            "translation": "マイケルはテントで寝る前にキャンプファイヤーを( 12 )しなければならなかった。彼は川に水を汲みに行き、火にかけた。",
            "choices": ["come out", "put out", "fill up", "back up"],
            "choiceTranslations": ["出てくる", "消す", "満たす", "後退する"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ come out＝出てくる。火を消す意味にならない",
                "✅ put out＝消す。水をかけて火を消す→正解",
                "❌ fill up＝満たす。火に対して使う表現ではない",
                "❌ back up＝後退する、バックアップする。文脈に合わない"
            ],
            "grammar": "💡 put out＝（火を）消す。extinguish と同義。campfire＝キャンプファイヤー。throw A on B＝AをBにかける"
        },
        {
            "number": 13,
            "text": "There are various ways to help people ( 13 ). For example, you can give money, clothes, or food to people who do not have enough.",
            "translation": "( 13 )の人々を助けるにはさまざまな方法がある。例えば、十分に持っていない人々にお金、衣服、食料を寄付できる。",
            "choices": ["on end", "by heart", "in need", "of use"],
            "choiceTranslations": ["続けて", "暗記して", "困っている", "役に立つ"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ on end＝続けて、立てて。人を助ける文脈に合わない",
                "❌ by heart＝暗記して。人を助ける文脈に合わない",
                "✅ in need＝困っている、必要としている。十分に持っていない人＝困っている人→正解",
                "❌ of use＝役に立つ。人を修飾する表現としては不自然"
            ],
            "grammar": "💡 in need＝困っている。people in need＝困っている人々。those in need とも言う。various＝さまざまな"
        },
        {
            "number": 14,
            "text": "Tony got a job as a train driver after he finished high school. He ( 14 ) the railway company for almost 50 years. He left when he became 65 years old.",
            "translation": "トニーは高校を卒業した後、電車の運転士の仕事に就いた。彼はほぼ50年間その鉄道会社で( 14 )。65歳になった時に退職した。",
            "choices": ["came over", "took after", "brought up", "worked for"],
            "choiceTranslations": ["やって来た", "似ている", "育てた", "～のために働いた"],
            "answer": 4,
            "choiceAnalysis": [
                "❌ came over＝やって来た。会社で50年の文脈に合わない",
                "❌ took after＝（外見・性格が）～に似ている。会社との関係には使わない",
                "❌ brought up＝育てた。会社を育てるでは文脈に合わない",
                "✅ worked for＝～のために働いた。50年間鉄道会社に勤めた→正解"
            ],
            "grammar": "💡 work for ～＝～に勤める、～のために働く。railway company＝鉄道会社。almost＝ほぼ、ほとんど"
        },
        {
            "number": 15,
            "text": "A : How long have you been ( 15 )?\nB : I started two months ago. So far, I've lost about 5 kilograms.",
            "translation": "A：どのくらい( 15 )してるの？\nB：2ヶ月前に始めたよ。今のところ、約5キロ痩せたよ。",
            "choices": ["for a change", "on a diet", "in place", "with time"],
            "choiceTranslations": ["気分転換に", "ダイエット中", "定位置に", "時間とともに"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ for a change＝気分転換に。期間を問う文脈に合わない",
                "✅ on a diet＝ダイエット中。5キロ痩せたので→正解",
                "❌ in place＝定位置に。体重減少と無関係",
                "❌ with time＝時間とともに。期間を尋ねる会話に合わない"
            ],
            "grammar": "💡 be on a diet＝ダイエット中である。go on a diet＝ダイエットを始める。So far＝今のところ"
        },
        {
            "number": 16,
            "text": "Some types of birds are ( 16 ) travel long distances. For example, arctic terns make journeys of around 90,000 kilometers each year.",
            "translation": "ある種の鳥は長距離を移動することで( 16 )。例えば、キョクアジサシは毎年約9万キロの旅をする。",
            "choices": ["jealous of", "belonged to", "known to", "true of"],
            "choiceTranslations": ["～を妬んで", "～に属した", "～することで知られている", "～に当てはまる"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ jealous of＝～を妬んで。鳥の説明に合わない",
                "❌ belonged to＝～に属した。travel と文法的に繋がらない",
                "✅ known to＝～することで知られている。長距離移動で有名な鳥→正解",
                "❌ true of＝～に当てはまる。文法的に不自然"
            ],
            "grammar": "💡 be known to ～＝～することで知られている。arctic terns＝キョクアジサシ。make a journey＝旅をする"
        },
        {
            "number": 17,
            "text": "Kelly loves the sea, but she has always lived far away from it. Her dream is to move to a house ( 17 ) the ocean after she retires.",
            "translation": "ケリーは海が好きだが、ずっと海から離れた場所に住んでいる。彼女の夢は退職後に海の( 17 )家に引っ越すことだ。",
            "choices": ["certain of", "fit for", "close to", "poor at"],
            "choiceTranslations": ["～を確信して", "～に適した", "～に近い", "～が苦手で"],
            "answer": 3,
            "choiceAnalysis": [
                "❌ certain of＝～を確信して。家の位置を説明する表現ではない",
                "❌ fit for＝～に適した。海の近くという意味にならない",
                "✅ close to＝～に近い。海の近くの家に住みたい→正解",
                "❌ poor at＝～が苦手で。場所の説明に合わない"
            ],
            "grammar": "💡 close to ～＝～に近い。反意語は far from ～（～から遠い）。retire＝退職する"
        },
        {
            "number": 18,
            "text": "( 18 ) three months, a big market is held in Coopersville. The last one was held in December, so the next one will be held in March.",
            "translation": "( 18 ) 3ヶ月ごとに、クーパーズビルでは大きな市場が開かれる。前回は12月に開かれたので、次回は3月に開かれる。",
            "choices": ["All", "Every", "With", "Some"],
            "choiceTranslations": ["全て", "～ごとに", "～と一緒に", "いくつかの"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ All＝全て。All three months では3ヶ月ごとにの意味にならない",
                "✅ Every＝～ごとに。Every three months＝3ヶ月ごとに→正解",
                "❌ With＝～と一緒に。期間の頻度表現にならない",
                "❌ Some＝いくつかの。定期開催の意味にならない"
            ],
            "grammar": "💡 every＝～ごとに。every three months＝3ヶ月ごとに。every other day＝1日おきに。is held＝開催される（受動態）"
        },
        {
            "number": 19,
            "text": "Billy often listens to a radio channel called Sonic FM because he wants to hear the ( 19 ) music. Sonic FM usually only plays songs from the past two or three months.",
            "translation": "ビリーは( 19 )音楽を聴きたいので、よくソニックFMというラジオチャンネルを聴いている。ソニックFMは通常、過去2〜3ヶ月の曲しか流さない。",
            "choices": ["highest", "latest", "fastest", "earliest"],
            "choiceTranslations": ["最も高い", "最新の", "最も速い", "最も早い"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ highest＝最も高い。音楽を修飾する文脈に合わない",
                "✅ latest＝最新の。過去2-3ヶ月の曲＝最新曲→正解",
                "❌ fastest＝最も速い。曲の新しさとは無関係",
                "❌ earliest＝最も早い。最新曲を聴きたい文脈と矛盾"
            ],
            "grammar": "💡 latest＝最新の。the latest news＝最新ニュース。late の最上級。channel＝チャンネル、局"
        },
        {
            "number": 20,
            "text": "Kenny gets angry when his parents tell him to go to bed or to eat his vegetables. He hates ( 20 ) like a little child.",
            "translation": "ケニーは両親に寝なさいとか野菜を食べなさいと言われると怒る。彼は小さな子供のように( 20 )のが嫌いだ。",
            "choices": ["treated", "being treated", "treating", "to be treating"],
            "choiceTranslations": ["扱われた", "扱われること", "扱うこと", "扱っていること"],
            "answer": 2,
            "choiceAnalysis": [
                "❌ treated＝扱われた（過去分詞）。hateの目的語としては文法的に不完全",
                "✅ being treated＝扱われること。受動態の動名詞。子供扱いされるのが嫌い→正解",
                "❌ treating＝扱うこと。ケニーが扱う側ではなく扱われる側",
                "❌ to be treating＝扱っていること。進行形の不定詞で不自然"
            ],
            "grammar": "💡 hate + being + 過去分詞＝～されるのを嫌う。動名詞の受動態。like a little child＝小さな子供のように"
        }
    ]
}

# =====================================================
# Section 1: 大問2（vocabulary型・5問・会話文空所補充）
# =====================================================
section2 = {
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(21)から(25)までの会話文の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 21,
            "text": "A : Good evening, sir. Are you ready to order yet?\nB : Do you still serve seafood pasta?\nA : We used to, but we ( 21 ) recently.\nB : That's a shame. I really liked that dish.",
            "translation": "A：こんばんは、お客様。ご注文はお決まりですか？\nB：シーフードパスタはまだありますか？\nA：以前はありましたが、最近( 21 )。\nB：それは残念です。あの料理が本当に好きだったんです。",
            "choices": ["started opening later", "got some new staff", "bought some new chairs", "changed our menu"],
            "choiceTranslations": ["営業時間を遅くした", "新しいスタッフを採用した", "新しい椅子を買った", "メニューを変えた"],
            "answer": 4,
            "choiceAnalysis": [
                "営業時間を遅くした→料理の提供と無関係",
                "新しいスタッフを採用した→メニューの変更理由にならない",
                "新しい椅子を買った→料理の有無と無関係",
                "メニューを変えた→正解。💡 シーフードパスタがなくなった理由"
            ],
            "grammar": "💡 used to ～＝以前は～した（過去の習慣）。serve＝（料理を）出す、提供する。That's a shame.＝それは残念だ"
        },
        {
            "number": 22,
            "text": "A : Dad, can you help me with my science homework?\nB : Sure, Claire. What do you need to do?\nA : I have to ( 22 ). Then, I have to color it and write the names of the different parts on it.\nB : That sounds like fun. Let's go and choose one from the garden.",
            "translation": "A：パパ、理科の宿題を手伝ってくれる？\nB：もちろん、クレア。何をしなければならないの？\nA：( 22 )しなければならないの。それから色を塗って、いろいろな部分の名前を書かなきゃいけないの。\nB：楽しそうだね。庭に行って一つ選ぼう。",
            "choices": ["draw a picture of a plant", "answer questions in my textbook", "get some information about space", "measure the size of my head"],
            "choiceTranslations": ["植物の絵を描く", "教科書の質問に答える", "宇宙の情報を集める", "頭のサイズを測る"],
            "answer": 1,
            "choiceAnalysis": [
                "植物の絵を描く→正解。💡 色を塗り部分名を書く＝植物の絵。庭で選ぶのも一致",
                "教科書の質問に答える→色を塗る作業と矛盾",
                "宇宙の情報を集める→庭に行って選ぶと矛盾",
                "頭のサイズを測る→色を塗り部分名を書く作業と矛盾"
            ],
            "grammar": "💡 have to ～＝～しなければならない。color＝色を塗る（動詞）。That sounds like fun.＝楽しそうだね"
        },
        {
            "number": 23,
            "text": "A : What kind of clothes are you looking for, sir?\nB : I heard about your sale. Can ( 23 ) if I bring you my old one?\nA : Yes. However, today is the last chance to get that discount.\nB : Right. I'll be back soon!",
            "translation": "A：どのような服をお探しですか、お客様？\nB：セールのことを聞いたんですが。古いのを持ってきたら( 23 )か？\nA：はい。ただし、その割引を受けられるのは今日が最後です。\nB：わかりました。すぐ戻ります！",
            "choices": ["you give me 25 percent off a new car", "you print a new receipt for me", "I buy a new suit for half price", "I get a new TV for less money"],
            "choiceTranslations": ["新しい車を25%オフにしてもらえる", "新しい領収書を印刷してもらえる", "新しいスーツを半額で買える", "新しいテレビを安く買える"],
            "answer": 3,
            "choiceAnalysis": [
                "新しい車を25%オフ→服屋で車の話は不自然",
                "新しい領収書を印刷→セールの割引内容ではない",
                "新しいスーツを半額で買える→正解。💡 服屋で古いものを持参して割引",
                "新しいテレビを安く買える→服屋でテレビは不適切"
            ],
            "grammar": "💡 half price＝半額。discount＝割引。I'll be back soon.＝すぐ戻ります。bring＝持ってくる"
        },
        {
            "number": 24,
            "text": "A : Mom, can my friend Jan come and stay at our house this weekend?\nB : Hmm. I'm not sure. Won't you both have ( 24 )?\nA : Our teacher said that after the tests this week, we wouldn't have to study this weekend.\nB : I see. How about your room? Have you cleaned it?\nA : Not yet, but I promise that I'll do it on Thursday evening.\nB : OK, then. I'd better speak to Jan's mother first to make sure that it's OK for Jan to stay with us.",
            "translation": "A：ママ、友達のジャンが今週末うちに泊まりに来てもいい？\nB：うーん。どうかな。二人とも( 24 )があるんじゃない？\nA：先生が今週テストが終わったら週末は勉強しなくていいって言ってたよ。\nB：なるほど。部屋はどうなの？掃除した？\nA：まだだけど、木曜の夜にやるって約束するよ。\nB：じゃあいいわ。ジャンのお母さんにまず話して、泊まっても大丈夫か確認しないとね。",
            "choices": ["meetings to go to", "homework to do", "club activities", "doctor's appointments"],
            "choiceTranslations": ["行かなきゃいけない会議", "やらなきゃいけない宿題", "部活動", "医者の予約"],
            "answer": 2,
            "choiceAnalysis": [
                "行かなきゃいけない会議→学生の週末の文脈に合わない",
                "やらなきゃいけない宿題→正解。💡 テスト後なので勉強不要という回答が根拠",
                "部活動→テスト後に勉強不要とは関係ない",
                "医者の予約→学校のテストの文脈に合わない"
            ],
            "grammar": "💡 Won't you ～?＝～しないの？（確認・懸念）。I'd better ～＝～した方がいい。make sure (that) ～＝～を確認する"
        },
        {
            "number": 25,
            "text": "A : Thanks, Mom. I'll ask Jan to send me ( 25 ).\nB : Actually, I think I already have it. Let me check my address book.",
            "translation": "A：ありがとう、ママ。ジャンに( 25 )を送ってもらうよう頼むね。\nB：実は、もう持っていると思うわ。住所録を確認させて。",
            "choices": ["her mom's phone number", "her grandma's cookie recipe", "a book for our tests", "a photo of her family"],
            "choiceTranslations": ["お母さんの電話番号", "おばあちゃんのクッキーのレシピ", "テスト用の本", "家族の写真"],
            "answer": 1,
            "choiceAnalysis": [
                "お母さんの電話番号→正解。💡 ジャンのお母さんに連絡するので電話番号が必要。住所録で確認できるのも一致",
                "おばあちゃんのクッキーのレシピ→お泊まりの許可に関する話と無関係",
                "テスト用の本→テストは終わった文脈",
                "家族の写真→お母さんに連絡する文脈に合わない"
            ],
            "grammar": "💡 ask someone to ～＝～するよう頼む。address book＝住所録（電話番号帳）。Actually＝実は、実のところ"
        }
    ]
}

data["sections"] = [section1, section2]

# Save intermediate file
output_dir = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-3"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "_part1.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"Part 1 saved: {len(section1['questions'])} + {len(section2['questions'])} = {len(section1['questions']) + len(section2['questions'])} questions")
