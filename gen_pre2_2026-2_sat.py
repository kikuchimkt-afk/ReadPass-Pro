# -*- coding: utf-8 -*-
"""Image-verified source, Grade Pre-2 2026-2 Saturday (booklet pp. 3-9).

Run to reproduce data.json, including deterministic audio references.
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade-pre2/2026-2-sat/data.json"


def module(suffix):
    spec = importlib.util.spec_from_file_location(suffix, ROOT / f"gen_pre2_2026-2_sat_{suffix}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# Original stem, blank-preserving translation, choices/translations, answer,
# contextual reasons, grammar. Part 1 follows the Pre-2 check/cross convention.
PART1 = [
    ("A : Do you want to go to the movie theater with me, Miranda?\nB : I can't. I have to study for a test. ( 1 ), there aren't any good movies at the theater now.",
     "A：ミランダ、私と映画館に行きませんか。\nB：行けません。テストの勉強をしなければなりません。( 1 )、今は映画館でよい映画を上映していません。",
     ["However", "Fairly", "Besides", "Instead"], ["しかし", "かなり", "そのうえ", "その代わりに"], 3,
     ["❌ However＝しかし。勉強が必要という理由に、別の理由を加える流れで、逆接ではない。", "❌ Fairly＝かなり。形容詞などを修飾する副詞で、ここでは文をつなげない。", "✅ Besides＝そのうえ。勉強に加え、よい映画がないという理由も挙げている→正解。", "❌ Instead＝その代わりに。映画へ行く代わりの行動を述べてはいない。"],
     "💡Besides は理由を追加する接続副詞。However は逆接、Instead は代替を示す。直前の I have to study と後ろの there aren't any good movies が同じ結論を支えている。"),
    ("Silver City has a nice ( 2 ) pool. Because it is not inside, it is only open from May until August.",
     "シルバーシティにはすてきな ( 2 ) のプールがあります。屋内にないので、5月から8月までしか営業していません。",
     ["frequent", "lonely", "outdoor", "daily"], ["頻繁な", "孤独な", "屋外の", "毎日の"], 3,
     ["❌ frequent＝頻繁な。プールが屋内にないという場所の説明に合わない。", "❌ lonely＝孤独な。人の気持ちを表し、プールの設置場所ではない。", "✅ outdoor＝屋外の。not inside が、屋内ではなく屋外にあることを示す→正解。", "❌ daily＝毎日の。営業期間が夏に限られる理由を説明できない。"],
     "💡outdoor pool は「屋外プール」。反対は indoor pool。Because S＋V で理由を述べ、from May until August は営業期間の始まりと終わりを示す。"),
    ("Today is Mike and Jane's five-year ( 3 ). They are going to a fancy restaurant to celebrate the special day.",
     "今日はマイクとジェーンの5年目の ( 3 ) です。その特別な日を祝うため、高級なレストランへ行く予定です。",
     ["anniversary", "symphony", "mystery", "trend"], ["記念日", "交響曲", "謎", "流行"], 1,
     ["✅ anniversary＝記念日。5年目の特別な日を祝うという内容に合う→正解。", "❌ symphony＝交響曲。5年目を迎えて祝う日を表さない。", "❌ mystery＝謎。special day を祝う説明につながらない。", "❌ trend＝流行。2人が迎える特別な日の名称ではない。"],
     "💡five-year anniversary は「5年目の記念日」。名詞を修飾する five-year の year は単数形。to celebrate はレストランへ行く目的を表す不定詞。"),
    ("A : How was your rugby match yesterday, Kevin?\nB : Not so good. One of our players got an ( 4 ) during the game, so we had to stop playing for a while.",
     "A：ケビン、昨日のラグビーの試合はどうでしたか。\nB：あまりよくありませんでした。選手の1人が試合中に ( 4 ) をしたので、しばらくプレーを中断しなければなりませんでした。",
     ["item", "iron", "image", "injury"], ["品目", "鉄", "画像・印象", "けが"], 4,
     ["❌ item＝品目。試合を中断する原因になる身体の問題ではない。", "❌ iron＝鉄。選手が鉄を得たからプレーを止めた、とは読めない。", "❌ image＝画像・印象。試合中に負うけがを表さない。", "✅ injury＝けが。選手がけがをして、しばらく試合を中断した→正解。"],
     "💡get an injury は「けがをする」。stop V-ing は「～するのをやめる」で、stop to V（～するために立ち止まる）とは異なる。for a while は「しばらくの間」。"),
    ("A : Be careful with that cup of coffee, dear. It's really hot.\nB : I know. I can see the ( 5 ) coming from it.",
     "A：そのコーヒーには気をつけてね。とても熱いですよ。\nB：分かっています。そこから ( 5 ) が出ているのが見えます。",
     ["panic", "shelf", "steam", "courage"], ["恐慌・パニック", "棚", "蒸気", "勇気"], 3,
     ["❌ panic＝恐慌・パニック。熱いコーヒーから出る物質ではない。", "❌ shelf＝棚。カップから出てくるものではない。", "✅ steam＝蒸気。熱いコーヒーから立ち上る湯気が見える→正解。", "❌ courage＝勇気。熱い飲み物から出る、目に見えるものではない。"],
     "💡steam は不可算名詞で、ここでは「湯気」。see＋目的語＋V-ing で、動作中の様子が見えることを表す。coming from it の it はコーヒーを指す。"),
    ("At first, it was difficult for Haruka to find a job she liked. Now, she ( 6 ) a small clothing store and she enjoys her work.",
     "最初は、ハルカが気に入る仕事を見つけるのは難しいことでした。今では小さな衣料品店を ( 6 ) していて、仕事を楽しんでいます。",
     ["manages", "offends", "preserves", "discovers"], ["経営する", "気分を害する", "保存する", "発見する"], 1,
     ["✅ manages＝経営する。衣料品店を運営する仕事を楽しんでいる→正解。", "❌ offends＝気分を害する。店に対して行う仕事を表さない。", "❌ preserves＝保存する。店の運営を職業として述べる流れに合わない。", "❌ discovers＝発見する。店を見つける行動は、今の仕事の説明にならない。"],
     "💡manage a store は「店を経営する」。a job she liked は関係代名詞の目的格が省略され、she liked が job を説明する。At first と Now の時間的な対比も手がかり。"),
    ("The sign on the supermarket door says that the store will ( 7 ) open throughout the New Year's holiday.",
     "スーパーのドアの掲示には、年末年始の休暇の間ずっと店は開いたまま ( 7 ) と書かれています。",
     ["pass", "mean", "spend", "remain"], ["通過する", "意味する", "費やす", "～のままである"], 4,
     ["❌ pass＝通過する。open という状態を維持する意味にならない。", "❌ mean＝意味する。店が営業を続けることを表せない。", "❌ spend＝費やす。通常は時間やお金を目的語に取り、open を補語にしない。", "✅ remain＝～のままである。remain open で休暇中も営業を続ける→正解。"],
     "💡remain＋形容詞で「～の状態のままである」。open はここでは動詞ではなく形容詞。throughout は「～の間ずっと」で、営業を続ける期間を示す。"),
    ("It is hard for Anna to ( 8 ) living in a place where there is no snow. She loves snow, and she could never live far away from it.",
     "アンナにとって、雪のない場所で暮らすことを ( 8 ) するのは難しいことです。雪が大好きなので、雪から遠く離れた場所にはとても住めません。",
     ["announce", "receive", "hear", "imagine"], ["発表する", "受け取る", "聞く", "想像する"], 4,
     ["❌ announce＝発表する。雪のない暮らしを思い描けないという気持ちを表さない。", "❌ receive＝受け取る。living を受け取るという形はここでは使えない。", "❌ hear＝聞く。雪のない場所での暮らしを想像する話とは異なる。", "✅ imagine＝想像する。雪好きのアンナは雪のない暮らしを思い描けない→正解。"],
     "💡imagine V-ing は「～することを想像する」で、to V は続けない。a place where ... の where は場所を説明する関係副詞。It is hard for A to V は「Aが～するのは難しい」。"),
    ("Dale wanted to buy a new smartphone on sale, but all the stores were selling them for the same price. There was no ( 9 ) on smartphones anywhere.",
     "デールは新しいスマートフォンを安売りで買いたかったのですが、どの店も同じ値段で売っていました。どこにもスマートフォンの ( 9 ) はありませんでした。",
     ["record", "hero", "deal", "brain"], ["記録", "英雄", "お買い得品・有利な取引", "脳"], 3,
     ["❌ record＝記録。安い価格で買える機会を表さない。", "❌ hero＝英雄。スマートフォンの販売価格とは無関係。", "✅ deal＝お買い得品・有利な取引。どの店にも安く買える機会がなかった→正解。", "❌ brain＝脳。商品の割引やお買い得な販売を表す語ではない。"],
     "💡a deal on＋商品は「その商品のお買い得な売り出し」。on sale は「特売で」。but の前の安く買いたい希望と、後ろのどこも同じ価格という事実を対比する。"),
    ("A : What is your speech about, Dave?\nB : Well, I'm going to talk about the differences between cats and dogs. Its ( 10 ) will be about the history of each type of animal.",
     "A：デイブ、スピーチは何についてですか。\nB：猫と犬の違いについて話すつもりです。その ( 10 ) では、それぞれの動物の歴史を取り上げます。",
     ["observation", "translation", "collection", "introduction"], ["観察", "翻訳", "収集", "導入・序論"], 4,
     ["❌ observation＝観察。スピーチの冒頭の部分を表さない。", "❌ translation＝翻訳。別の言語に訳す話はしていない。", "❌ collection＝収集。スピーチの構成要素の名称ではない。", "✅ introduction＝導入・序論。猫と犬の歴史を紹介する冒頭部分を指す→正解。"],
     "💡introduction は話や文章の「導入部分」。Its は your speech を受ける所有格。the differences between A and B は「AとBの違い」。each の後は単数形 type。"),
    ("A : It's time to leave now, Tim.\nB : ( 11 ), Dad. I can't find my cap.",
     "A：ティム、もう出発する時間ですよ。\nB：お父さん、( 11 )。帽子が見つからないんです。",
     ["Hold on", "Set up", "Drop by", "Join in"], ["待って", "設置する", "立ち寄る", "参加する"], 1,
     ["✅ Hold on＝待って。帽子が見つからず、出発を待ってほしい→正解。", "❌ Set up＝設置する。出発を待つよう頼む表現ではない。", "❌ Drop by＝立ち寄る。すでに一緒にいる父親への返答に合わない。", "❌ Join in＝参加する。出発の準備ができていない理由とつながらない。"],
     "💡Hold on は会話で「ちょっと待って」。It's time to V は「～する時間だ」。can't find は「探しても見つからない」で、出発を待つ理由になる。"),
    ("A : Do you want to play for the company's softball team, Jen?\nB : No. I'm ( 12 ) playing sports, but I'd love to go and watch.",
     "A：ジェン、会社のソフトボールチームでプレーしたいですか。\nB：いいえ。スポーツをするのは ( 12 ) ですが、ぜひ観戦には行きたいです。",
     ["aware of", "jealous of", "poor at", "mad at"], ["～に気づいている", "～をうらやむ", "～が苦手な", "～に腹を立てている"], 3,
     ["❌ aware of＝～に気づいている。プレーを断る能力面の理由にならない。", "❌ jealous of＝～をうらやむ。スポーツが苦手で観戦したいという流れと異なる。", "✅ poor at＝～が苦手な。自分はプレーせず、観戦したいという返答に合う→正解。", "❌ mad at＝～に腹を立てている。スポーツをする技能の不得意を表さない。"],
     "💡be poor at＋名詞・動名詞は「～が苦手だ」。at は前置詞なので playing。反対は be good at。I'd love to V は「ぜひ～したい」という気持ち。"),
    ("When Peggy was making bread the other day, she realized that she was ( 13 ) flour. She had to go to the supermarket to get some more.",
     "先日ペギーがパンを作っていると、小麦粉が ( 13 ) と気づきました。もっと買うためにスーパーへ行かなければなりませんでした。",
     ["angry at", "bad for", "unable to", "short of"], ["～に腹を立てている", "～によくない", "～できない", "～が不足している"], 4,
     ["❌ angry at＝～に腹を立てている。小麦粉を買い足す必要の説明にならない。", "❌ bad for＝～によくない。小麦粉の不足を表す形ではない。", "❌ unable to＝～できない。後ろには動詞の原形が必要で、flour は名詞。", "✅ short of＝～が不足している。小麦粉が足りず、買い足す必要があった→正解。"],
     "💡be short of＋名詞は「～が不足している」。the other day は「先日」。When 節の was making は過去進行形で、その途中に realized という気づきが起きている。"),
    ("The school principal decided that ( 14 ) of rain, the sports festival would be held inside the school gym.",
     "校長先生は、雨の ( 14 )、体育祭を学校の体育館内で行うことに決めました。",
     ["at present", "by way", "for sure", "in case"], ["現在は", "経由で（by way of）", "確かに", "～の場合に（in case of）"], 4,
     ["❌ at present＝現在は。後ろの of rain とつながる条件表現にならない。", "❌ by way＝経由で（by way of）。雨を経由するという意味ではない。", "❌ for sure＝確かに。of rain を伴って雨天の条件を示すことはできない。", "✅ in case＝～の場合に。in case of rain で雨天の場合を表す→正解。"],
     "💡in case of＋名詞は「～の場合に」。in case of rain 全体で雨天時の対応を示す。would be held は過去の decided に合わせた未来の受動態で、hold の過去分詞は held。"),
    ("A : I have to go now, but I will call you later.\nB : OK. Before you go, ( 15 ) my phone number so you won't forget it.",
     "A：もう行かなければなりませんが、後で電話します。\nB：分かりました。忘れないように、行く前に私の電話番号を ( 15 ) してください。",
     ["write down", "jump up", "throw away", "calm down"], ["書き留める", "跳び上がる", "捨てる", "落ち着く"], 1,
     ["✅ write down＝書き留める。電話番号を忘れないよう記録する→正解。", "❌ jump up＝跳び上がる。番号を覚えておくための行動ではない。", "❌ throw away＝捨てる。番号を忘れないための行動と逆になる。", "❌ calm down＝落ち着く。電話番号を記録する意味はない。"],
     "💡write down は「書き留める」。名詞なら write down my number、代名詞なら write it down。so you won't forget it は、番号を書き留める目的を説明する。"),
]

SHARED = "A : Hello. I'm planning to attend your company event on Wednesday, but I've heard there has been ( 19 ). Is that correct?\nB : Thank you for calling, sir. Yes, I'm afraid Ms. Linda Smith cannot attend because of a family problem.\nA : That's too bad. I was looking forward to her presentation.\nB : I know. But Mr. Wilson Kuroda, a popular author on business communication, will be giving a talk instead of her.\nA : Oh, I've read all his books. What ( 20 )?\nB : He'll be sharing ideas on how to get along with new employees.\nA : That sounds very interesting. How long will his presentation last?\nB : About forty-five minutes, followed by a fifteen-minute question and answer session."
SHARED_JA = "A：こんにちは。水曜日の御社のイベントに参加する予定ですが、( 19 ) があったと聞きました。本当ですか。\nB：お電話ありがとうございます。はい、残念ですが、リンダ・スミスさんは家庭の事情で参加できません。\nA：それは残念です。彼女の発表を楽しみにしていました。\nB：そうですね。でも、ビジネスコミュニケーションについて書く人気作家のウィルソン・クロダさんが、彼女に代わって講演します。\nA：ああ、彼の本は全て読みました。何を ( 20 )。\nB：新しい従業員とうまく付き合う方法について、考えを紹介する予定です。\nA：とても面白そうですね。講演はどのくらい続きますか。\nB：約45分で、その後に15分の質疑応答があります。"
PART2 = [
    ("A : Excuse me, I'd like to buy this scarf. I love the blue color.\nB : Great choice! It just came in this morning. It looks great on you.\nA : Thanks, but ( 16 ). Could you wrap it as a gift?\nB : Of course. Does she like pink? The pink box would look great with the blue scarf.",
     "A：すみません、このスカーフを買いたいです。青い色がとても気に入りました。\nB：よいお選びですね。今朝入荷したばかりです。よくお似合いです。\nA：ありがとうございます。でも、( 16 )。贈り物として包装してもらえますか。\nB：もちろんです。その方はピンクがお好きですか。ピンクの箱は青いスカーフとよく合うでしょう。",
     ["I want to try a blue scarf", "your scarf is blue and pink", "it's a present for my sister", "my mother gave it to me"],
     ["青いスカーフを試したいです", "あなたのスカーフは青とピンクです", "妹（姉）へのプレゼントです", "母が私にくれました"], 3,
     ["青いスカーフを試したいです→試着の希望だけでは、贈り物の包装や次の she につながらない。", "あなたのスカーフは青とピンクです→店員のスカーフを説明する話ではない。", "妹（姉）へのプレゼントです→正解。💡wrap it as a gift と Does she like pink? が、女性への贈り物を示す。", "母が私にくれました→今この店で買う品を、すでにもらったとは言えない。"],
     "💡but は「自分に似合う」という店員の見方を、贈り物であることへ切り替える。Could you V? は丁寧な依頼。as a gift は「贈り物として」で、she は sister を指す。"),
    ("A : Excuse me, how much is this T-shirt?\nB : It is twenty dollars with a special discount only for today. It is usually twenty-five dollars.\nA : That is great! Do you ( 17 )?\nB : Yes, we do. It is on the counter over there, so I can bring one for you right now.",
     "A：すみません、このTシャツはいくらですか。\nB：今日だけの特別割引で20ドルです。普段は25ドルです。\nA：それはいいですね。( 17 ) か。\nB：はい。向こうのカウンターにあるので、今すぐ1枚お持ちできます。",
     ["take orders online", "take credit cards", "have it in black", "have a fitting room"],
     ["オンラインで注文を受け付けています", "クレジットカードを受け付けています", "それの黒色があります", "試着室があります"], 3,
     ["オンラインで注文を受け付けています→カウンターから1枚持ってくるという返答につながらない。", "クレジットカードを受け付けています→支払方法の質問に、Tシャツを持ってくるとは答えない。", "それの黒色があります→正解。💡I can bring one が、別の色のTシャツを持ってくることを示す。", "試着室があります→試着室をカウンターから持ってくることはできない。"],
     "💡have it in＋色は「その商品の～色を置いている」。後ろの one は a T-shirt を受ける代名詞。空所の後の返答で、店員が持ってこられる物に注目する。"),
    ("A : Hi. I'd like to get new glasses. How long will it take?\nB : If you've shopped with us before, it takes about thirty minutes. If not, we'll need to check your eyes first, so please allow around sixty minutes.\nA : Hmm, I'm not sure if I have.\nB : No problem. Please feel free to ( 18 ) while I check your order history. I hope you find something you like.",
     "A：こんにちは。新しい眼鏡を買いたいのですが、どのくらいかかりますか。\nB：以前当店で購入された方なら約30分です。そうでなければ最初に目の検査が必要なので、約60分見込んでください。\nA：うーん、以前買ったかどうか分かりません。\nB：大丈夫です。購入履歴を調べる間、ご自由に ( 18 ) ください。気に入るものが見つかるといいですね。",
     ["see an eye doctor", "take off your glasses", "try out some glasses", "give me any advice"],
     ["眼科医に診てもらって", "眼鏡を外して", "いくつか眼鏡を試して", "私に何か助言をして"], 3,
     ["眼科医に診てもらって→履歴を調べる間に店内で商品を選ぶ流れに合わない。", "眼鏡を外して→I hope you find something you like という商品選びにつながらない。", "いくつか眼鏡を試して→正解。💡履歴確認を待つ間、気に入る眼鏡を試してほしいという案内。", "私に何か助言をして→商品を求めている客に、店員への助言を頼む場面ではない。"],
     "💡feel free to V は「遠慮なく～してください」。while S＋V は「～している間」。I'm not sure if I have の if は「～かどうか」で、条件の if とは役割が異なる。"),
    (SHARED, SHARED_JA,
     ["an update to the place of the event", "another workshop added to the event", "a delay in the event schedule", "a change in the guest speaker"],
     ["イベント会場の変更", "イベントへの別のワークショップの追加", "イベント日程の遅れ", "ゲスト講演者の変更"], 4,
     ["イベント会場の変更→会場が変わるという説明はなく、欠席する講演者の話をしている。", "イベントへの別のワークショップの追加→講演者の代役であり、講座を追加する話ではない。", "イベント日程の遅れ→講演時間の説明はあるが、日程を遅らせるとは言っていない。", "ゲスト講演者の変更→正解。💡Smith cannot attend と Kuroda ... instead of her が、講演者の交代を示す。"],
     "💡there has been＋名詞は、現在までに起きた変更を示す現在完了。instead of＋名詞・代名詞は「～の代わりに」。最初の質問に対する返答と代役の紹介を結びつける。"),
    (SHARED, SHARED_JA,
     ["is the order of his speech", "is the title of his new book", "will he be talking about", "will he do before the event"],
     ["彼のスピーチの順番は何ですか", "彼の新しい本の題名は何ですか", "彼は何について話す予定ですか", "彼はイベント前に何をする予定ですか"], 3,
     ["彼のスピーチの順番は何ですか→返答は何番目かではなく、話す内容を説明している。", "彼の新しい本の題名は何ですか→本の題名ではなく、新しい従業員との関わり方が話題。", "彼は何について話す予定ですか→正解。💡He'll be sharing ideas on how to get along with new employees が講演内容を答える。", "彼はイベント前に何をする予定ですか→イベント前の行動ではなく、講演のテーマを尋ねている。"],
     "💡What will he be talking about? は未来進行形による講演内容の質問。get along with＋人は「人とうまく付き合う」。how to V は「～する方法」で、ideas の内容を示す。"),
]


def questions(rows, start):
    return [dict(number=n, text=r[0], translation=r[1], choices=r[2],
                 choiceTranslations=r[3], answer=r[4], choiceAnalysis=r[5], grammar=r[6])
            for n, r in enumerate(rows, start)]


def build():
    p, m = module("passages"), module("materials")
    sections = [
        dict(name="大問1", nameEn="Part 1", type="vocabulary",
             instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", questions=questions(PART1, 1)),
        dict(name="大問2", nameEn="Part 2", type="vocabulary",
             instruction="次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", questions=questions(PART2, 16)),
        dict(name="大問3", nameEn="Part 3", type="passage-fill",
             instruction="次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=p.PASSAGES[:1]),
        dict(name="大問4", nameEn="Part 4", type="reading-comprehension",
             instruction="次の英文A，Bの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=p.PASSAGES[1:]),
    ]
    listening = [3,3,2,3,3,2,3,3,1,1,3,3,4,1,3,4,3,3,1,2,1,4,4,2,3,2,4,1,1,4]
    return dict(grade="準2級", year="2026", session="2-sat",
                title="2026年度 第2回（土曜準会場）英検準2級 リーディング",
                vocabulary=m.vocabulary(), sections=sections, lessonPlan=m.lessonplan(p.PASSAGES),
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)})


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(OUT)
