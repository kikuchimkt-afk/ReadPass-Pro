# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2026-2 Saturday; original booklet pp. 2-11, image-verified."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2026-2-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2026-2_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("The (　) of the water in the aquarium is too low for the fish.",
     "水槽の水の (　) は、その魚にとって低すぎます。",
     ["hometown","address","village","temperature"], ["故郷","住所","村","温度"],4,
     "水の状態を表し、too low（低すぎる）がヒント。temperature of the water は『水温』。魚に合う温度より低いという意味になる。住所や村は水の状態を示さない。",
     "おみずがさむすぎる、というおはなし。temperature は『おんど』。さかなにあうおんどより、ひくいんだね。",
     ["水そのものの故郷という意味ではない。","水の温度を住所では表せない。","水が低すぎる状態を村とは言わない。","too low が水温の低さを示す。"],
     ["おみずのふるさとではないよ。","じゅうしょのことではないよ。","むらのことではないよ。","おみずのおんどがひくすぎるんだね。"]),
    ("A: When will your summer vacation (　)?\nB: On September 1.",
     "A：夏休みはいつ (　) か。\nB：9月1日です。",
     ["end","draw","build","hear"],["終わる","描く","建てる","聞く"],1,
     "When will ...? は未来の時期を尋ねる。夏休みが9月1日に終わるので end。will の後ろは動詞の原形を置く。vacation が絵を描いたり建物を建てたりするわけではない。",
     "『なつやすみは、いつおわる？』ときいているよ。end は『おわる』。9がつ1にち、というこたえにつながるね。",
     ["休みが終わる時期を尋ねる形になる。","休みが絵を描くとは言えない。","休みが何かを建てる話ではない。","休みが聞く動作をするわけではない。"],
     ["なつやすみがおわるひをきいているね。","えをかくおはなしではないよ。","たてものをつくることではないよ。","おとをきくことではないよ。"]),
    ("Schools in this city will (　) for summer vacation on July 20.",
     "この市の学校は、7月20日に夏休みのため (　)。",
     ["say","close","dance","stand"],["言う","閉まる・休みになる","踊る","立つ"],2,
     "for summer vacation が学校が休みになる理由を示す。close はここでは『休校になる』。will close で今後の予定を表す。学校が話す・踊る・立つという内容ではない。",
     "がっこうが、なつやすみに入るおはなしだよ。close は『しまる』。この文では『おやすみになる』ということだね。",
     ["学校が何かを言う話ではない。","夏休みに入り、学校が休みになる。","学校の建物が踊ることはない。","学校が立つという意味ではない。"],
     ["なにかをいうことではないよ。","なつやすみで、がっこうがおやすみになるね。","おどるおはなしではないよ。","たつことではないよ。"]),
    ("I like Mr. Baker's class very much. He often (　) us funny stories in his lessons.",
     "私はベイカー先生の授業が大好きです。先生は授業で、よく私たちに面白い話を (　)。",
     ["tells","calls","rides","stops"],["話す","呼ぶ","乗る","止める"],1,
     "tell 人 stories は『人に話をする』。us が聞き手、funny stories が話す内容。主語が He なので tells とする。call は名前を呼ぶなどの動詞で、話を語る意味にはならない。",
     "せんせいが、みんなにおもしろいおはなしをしてくれるよ。tells us stories は『わたしたちに、おはなしをする』というセットだね。",
     ["tell us stories で私たちに話をする。","名前を呼ぶ意味で、話を語る形にはならない。","何かに乗ることで、話をする意味はない。","動きを止める意味で、物語を語ることではない。"],
     ["みんなにおはなしをする、といういみだね。","なまえをよぶことではないよ。","のりものにのることではないよ。","とめるおはなしではないよ。"]),
    ("A: What did you do in New York last weekend?\nB: I went to visit my cousin. I stayed at her (　).",
     "A：先週末、ニューヨークで何をしましたか。\nB：いとこに会いに行きました。彼女の (　) に泊まりました。",
     ["game","apartment","concert","vacation"],["ゲーム・試合","アパート","コンサート","休暇"],2,
     "stayed at（～に泊まった）の後ろには宿泊する場所が必要。her apartment は『彼女のアパート』。いとこを訪問し、その住まいに泊まったというつながりで読む。",
     "いとこのいえに、とまったんだね。apartment は『アパート』。ゲームやおやすみには、とまれないよ。",
     ["ゲームや試合は宿泊する住まいではない。","いとこの住まいに泊まったという内容になる。","コンサートは公演で、住まいではない。","休暇は期間で、泊まる場所ではない。"],
     ["ゲームにとまることはできないよ。","いとこのアパートに、とまったんだね。","コンサートは、すむいえではないよ。","おやすみは、ばしょではないよ。"]),
    ("Wendy went to Hawaii last winter. She did not need a coat there because the weather was (　).",
     "ウェンディは去年の冬にハワイへ行きました。天気が (　) だったので、そこではコートが必要ありませんでした。",
     ["angry","warm","ready","useful"],["怒っている","暖かい","準備ができた","役に立つ"],2,
     "did not need a coat（コートが必要なかった）がヒント。暖かければコートは不要なので warm。because の後ろは、その理由。angry は人の感情、ready は準備の状態を示す。",
     "コートをきなくてよかったのは、あたたかかったからだね。warm は『あたたかい』。weather は『てんき』だよ。",
     ["天気が怒るという意味ではない。","暖かいのでコートがいらなかった。","準備ができたことは、コート不要の理由にならない。","役立つことでは、気温の高さを示せない。"],
     ["おこっているひとのことではないよ。","あたたかいから、コートはいらないね。","じゅんびのことではないよ。","べんり、といういみではないよ。"]),
    ("A: I didn't hear you. Can you (　) your question, please?\nB: OK. I'll say it again.",
     "A：聞こえませんでした。質問を (　) してもらえますか。\nB：分かりました。もう一度言います。",
     ["repeat","receive","clean","meet"],["繰り返す","受け取る","掃除する","会う"],1,
     "I didn't hear you と say it again（もう一度言う）がヒント。repeat your question で『質問を繰り返す』。Can you ...? は依頼。受け取る・掃除するでは返答につながらない。",
     "きこえなかったから、もういちどいってほしいんだね。repeat は『くりかえす』。say it again も『もういちどいう』だよ。",
     ["say it again と同じく、もう一度言うこと。","質問を受け取る意味では、聞き直しにならない。","質問を掃除するとは言えない。","質問に会うという使い方はしない。"],
     ["もういちどいう、ということだね。","うけとることではないよ。","そうじをすることではないよ。","だれかにあうことではないよ。"]),
    ("On Sunday, my grandmother made cookies. I watched her (　) a long time. I love her cookies.",
     "日曜日に祖母がクッキーを作りました。私は長い時間 (　)、祖母を見ていました。祖母のクッキーが大好きです。",
     ["at","of","by","for"],["～で・～に","～の","～までに・～によって","～の間"],4,
     "a long time は時間の長さ。for a long time で『長い間』となる。at は時刻、by は期限などを示すが、ここでは見ていた時間の長さを表したい。",
     "ながいあいだ、おばあちゃんをみていたよ。for a long time は『ながいあいだ』というセット。for をつかおう。",
     ["at は時刻などを示すが、長い間という長さには合わない。","of は『～の』で、動作の続く時間を示さない。","by は期限などを示し、時間の長さではない。","for＋時間で、見ていた期間を示す。"],
     ["なんじ、というときなどにつかうよ。","『～の』では、ながいあいだにならないよ。","いつまでに、といういみなどにつかうよ。","for は『～のあいだ』だね。"]),
    ("A: Ann really (　) like her sister.\nB: Yes. They are both tall and have long black hair.",
     "A：アンは本当にお姉さん（妹）のように (　)。\nB：はい。2人とも背が高くて、長い黒髪です。",
     ["looks","gives","finds","shows"],["見える","与える","見つける","見せる"],1,
     "looks like＋人は『人に似ている』。背の高さや髪の色が共通なので、見た目が似ていると分かる。主語 Ann は三人称単数で、look に s を付ける。",
     "2人はせがたかくて、くろいかみ。にているんだね。looks like は『～ににている』というセットだよ。",
     ["looks like her sister で姉妹の見た目が似ている。","何かを与える話ではない。","誰かを見つけた話ではない。","何かを見せる意味で、似ているとは言えない。"],
     ["おねえさんやいもうとに、にているんだね。","なにかをあげることではないよ。","みつけることではないよ。","みせることではないよ。"]),
    ("A: Did you meet the new baseball coach?\nB: Yes, I (　) with him this morning. He's nice.",
     "A：新しい野球のコーチに会いましたか。\nB：はい、今朝彼と (　)。親切な人です。",
     ["joined","asked","picked","talked"],["参加した","尋ねた","選んだ・摘んだ","話した"],4,
     "talk with＋人は『人と話す』。this morning の出来事なので talked。コーチと話して人柄が分かった、という流れになる。ask 人なら with を挟まず、尋ねた内容も必要になる。",
     "けさ、コーチとおはなしをしたんだね。talked with him は『かれとはなした』。talk のむかしの形は talked だよ。",
     ["join with はここでコーチに会って話した意味にならない。","ask him なら with は不要で、会話をした表現とは異なる。","物を選ぶ・摘む意味で、コーチとの会話ではない。","talked with him で彼と話したことを示す。"],
     ["なかまにはいることではないよ。","しつもんしたことだけをいっていないよ。","なにかをえらぶことではないよ。","コーチとおはなしをしたんだね。"]),
    ("A: Can we go fishing on Sunday, Grandpa?\nB: Sure. Sunday is (　) with me.",
     "A：おじいちゃん、日曜日に釣りに行けますか。\nB：もちろん。私は日曜日で (　)。",
     ["tired","dark","fine","dirty"],["疲れた","暗い","都合がよい・よい","汚れた"],3,
     "Sure で日曜日の予定を承諾している。Sunday is fine with me は『日曜日で私は大丈夫』。fine with 人は、その人にとって都合がよいという意味。暗さや汚れの話ではない。",
     "にちようびなら、だいじょうぶだよ、とこたえているね。fine with me は『わたしはそれでいいよ』といういいかただよ。",
     ["日曜日が疲れたとは言わず、予定への承諾にもならない。","暗いかどうかではなく、日程への返答。","日曜日で都合がよい、と承諾している。","汚れていることは予定への返答にならない。"],
     ["つかれたひとのことではないよ。","くらさをきいていないよ。","にちようびでだいじょうぶ、といっているね。","よごれのことではないよ。"]),
    ("I got a new CD for my birthday. It's great. I want to listen to it again (　) again.",
     "誕生日に新しいCDをもらいました。とてもよいCDです。何度も (　)、繰り返し聴きたいです。",
     ["if","than","and","but"],["もし～なら","～より","そして","しかし"],3,
     "again and again は『何度も何度も』という決まった表現。CDが気に入って繰り返し聴きたいことを示す。if は条件、than は比較、but は逆接なので、この連語を作れない。",
     "すきなCDを、なんどもききたいんだね。again and again は『なんどもなんども』。まんなかは and だよ。",
     ["if は条件を示し、again and again という連語にならない。","than は比較に使い、繰り返しを表さない。","again and again で何度も繰り返すこと。","but は逆接で、繰り返しの連語には使わない。"],
     ["『もし』では、このセットにならないよ。","『～より』ではないよ。","again and again で、なんどもなんどもだね。","『しかし』では、このセットにならないよ。"]),
    ("After studying for two hours, Taro (　) some water and went back to his homework.",
     "2時間勉強した後、太郎は水を (　)、宿題に戻りました。",
     ["to drink","drinks","drank","drink"],["飲むこと・飲むために","飲む（三人称単数現在）","飲んだ","飲む（原形）"],3,
     "and went back の went が過去の行動を示す。水を飲んだことも同じ過去の出来事なので drank。drink の過去形は drank。現在形 drinks や不定詞 to drink では時制・文型が合わない。",
     "むかしのできごとだから『のんだ』の drank。あとにある went もむかしの形。drink→drank とおぼえよう。",
     ["to drink だけでは主語 Taro の動詞にならない。","現在形で、went と同じ過去の行動にならない。","drink の過去形で、went と時制がそろう。","原形のままでは過去の行動を表せない。"],
     ["これだけでは『のんだ』にならないよ。","いまの形ではなく、むかしの形がいるね。","drank が『のんだ』だね。","drink は、むかしの形ではないよ。"]),
    ("A: Are those Lynne's boots?\nB: No. (　) are red.",
     "A：あれはリンのブーツですか。\nB：いいえ。(　) は赤色です。",
     ["Hers","Its","Her","She"],["彼女のもの","それの","彼女の・彼女を","彼女は"],1,
     "Lynne's boots を繰り返さず『彼女のもの』と言うので所有代名詞 Hers。Hers＝her boots で、boots が複数だから are が続く。Her なら後ろに名詞が必要、She は本人を指す。",
     "『かのじょのブーツは、あかいよ』というこたえ。Hers は『かのじょのもの』。Her だけでは『もの』までいえないよ。",
     ["her boots を受け、彼女のブーツを指せる。","『それの』で、リンのブーツを指す所有代名詞ではない。","『彼女の』なら後ろに boots などの名詞が必要。","本人を指し、複数のブーツの代わりにはならない。"],
     ["『かのじょのもの』で、ブーツのことだね。","『それの』では、リンのものにならないよ。","Her のあとは、もののなまえがいるよ。","リン本人ではなく、ブーツのことだよ。"]),
    ("A: Do you want to play basketball this afternoon?\nB: That sounds fun, but I have to (　) to the doctor.",
     "A：今日の午後、バスケットボールをしたいですか。\nB：面白そうですが、医者に (　) 必要があります。",
     ["go","goes","going","went"],["行く（原形）","行く（三人称単数現在）","行くこと・行っている","行った"],1,
     "have to＋動詞の原形は『～しなければならない』。主語 I の後ろの have to につながるのは go。go to the doctor は受診すること。goes・going・went は原形ではない。",
     "have to のあとは、もとの形の go をつかうよ。go to the doctor は『おいしゃさんにいく』ということだね。",
     ["have to go と原形でつなげる。","have to の後ろに三人称単数の s は付けない。","have to の後ろは -ing 形ではなく原形。","have to の後ろは過去形ではなく原形。"],
     ["go が、もとの形だね。","s をつけないよ。","ing をつけないよ。","went ではなく go だよ。"]),
    ("Daughter: This soup is delicious, Mom.\nMother: Thank you. (　)\nDaughter: Yes, please.",
     "娘：お母さん、このスープはおいしいです。\n母：ありがとう。(　)\n娘：はい、お願いします。",
     ["Are you free today?","Do you want some more?","Did you cook?","Is this your spoon?"],
     ["今日は暇ですか。","もう少し欲しいですか。","料理しましたか。","これはあなたのスプーンですか。"],2,
     "Yes, please. は食べ物などを勧められたときの『はい、お願いします』。スープが気に入った娘に、おかわりを勧める Do you want some more? が合う。料理した人やスプーンの持ち主を尋ねる流れではない。",
     "『もうすこしいる？』『はい、おねがいします』とつながるよ。おいしいスープのおかわりを、すすめているんだね。",
     ["予定を尋ねる質問に please を添えて受け取る返答は合わない。","スープのおかわりの勧めに Yes, please と答えている。","料理したかには通常 Yes, I did と答える。","持ち主の確認に Yes, please とは答えない。"],
     ["ひまかどうかのおはなしではないよ。","おかわりがほしい、とこたえているね。","つくったかどうかをきいていないよ。","スプーンがだれのものかではないよ。"]),
    ("Man 1: Mark, what time is it?\nMan 2: It's 4:30.\nMan 1: Oh, (　) It's time for the meeting.",
     "男性1：マーク、何時ですか。\n男性2：4時30分です。\n男性1：ああ、(　) 会議の時間です。",
     ["I wasn't there.","I don't know his name.","we must go now.","we had lunch at the café."],
     ["私はそこにいませんでした。","彼の名前を知りません。","今すぐ行かなければなりません。","私たちはカフェで昼食を取りました。"],3,
     "It's time for the meeting. が今すぐ移動する理由。we must go now は『今行かなければならない』。時刻を聞いて会議に向かう流れで、昔の昼食や名前の話ではない。",
     "もうかいぎのじかん。だから『いまいかなきゃ』だね。must go は『いかなければならない』だよ。",
     ["過去にその場にいなかった話は、会議の時間とつながらない。","名前が分からない話は時刻と無関係。","会議の時間なので、今すぐ行く必要がある。","昔の昼食の話では、今の会議に向かう流れにならない。"],
     ["むかしそこにいたかではないよ。","なまえをきいていないよ。","かいぎだから、いまいくんだね。","おひるごはんのことではないよ。"]),
    ("Man: Look! It's raining. (　)\nWoman: Yes, it's in my bag.",
     "男性：見て。雨が降っています。(　)\n女性：はい、かばんの中にあります。",
     ["Are you cold?","Did you bring your umbrella?","Do you like rain?","Shall we wait a little longer?"],
     ["寒いですか。","傘を持ってきましたか。","雨は好きですか。","もう少し待ちましょうか。"],2,
     "it's in my bag の it は持ち物を指す。雨が降っているので、その持ち物は umbrella（傘）。持ってきたかを聞く Did you bring ...? が、Yes と場所の説明につながる。",
     "あめだから、かさをもってきたかきいているよ。『はい、かばんにあるよ』の it は、かさのことだね。",
     ["寒いという状態をかばんの中にあるとは言わない。","傘を持ってきたかに答え、傘の場所も伝えている。","雨の好みには、かばんの中という返答は合わない。","待つ提案には、持ち物の場所を答える必要がない。"],
     ["さむさは、かばんにははいらないよ。","かさが、かばんにあるんだね。","あめがすきかどうかではないよ。","まつかどうかではないよ。"]),
    ("Boy: You look sad. What's wrong?\nGirl: (　) It's too difficult.",
     "男の子：悲しそうですね。どうしましたか。\n女の子：(　) 難しすぎます。",
     ["This tomato is not good.","The party starts soon.","I can't read this book.","I'm sick."],
     ["このトマトはよくありません。","パーティーがもうすぐ始まります。","この本が読めません。","具合が悪いです。"],3,
     "It's too difficult. は『難しすぎる』。本の内容が難しくて読めない I can't read this book が合う。it は this book を受ける。味・開始時刻・病気を difficult とは説明しない。",
     "ほんがむずかしすぎて、よめないんだね。can't read は『よめない』。トマトのあじや、びょうきのおはなしではないよ。",
     ["トマトの味が悪いことを difficult とは説明しない。","開始時刻と、難しすぎて困ることはつながらない。","本が難しくて読めないことが、悲しそうな理由になる。","体調不良の理由を、この本のように difficult とは説明しない。"],
     ["トマトのあじを『むずかしい』とはいわないね。","はじまるじかんのおはなしではないよ。","ほんがむずかしくて、よめないんだね。","びょうきだから、ではないよ。"]),
    ("Father: Cindy, (　) You're late for school.\nDaughter: OK, Dad. I'm coming.",
     "父：シンディ、(　) 学校に遅れていますよ。\n娘：分かった、お父さん。今行きます。",
     ["at our house.","hurry up.","for an hour.","I'm fine, thank you."],
     ["私たちの家で。","急いで。","1時間の間。","元気です、ありがとう。"],2,
     "You're late for school. が急がせる理由。hurry up は『急いで』という命令で、I'm coming. と応じる流れに合う。場所や時間の長さだけでは、急ぐよう求める文にならない。",
     "がっこうにおくれているから『いそいで』だね。hurry up は『いそいで』。『いまいくよ』というこたえにつながるよ。",
     ["場所を述べるだけでは、急ぐよう頼む文にならない。","遅れている娘に、急ぐよう呼びかけている。","時間の長さだけでは命令にならない。","父親の体調を尋ねる会話ではない。"],
     ["いえのばしょをいうことではないよ。","いそいで、とこえをかけているね。","1じかん、とはいっていないよ。","げんきかどうかのおはなしではないよ。"]),
]


def build():
    p,o,m=module("passages"),module("order"),module("materials")
    qs=[]
    for n,r in enumerate(ROWS,1):
        text,ja,choices,meanings,answer,grammar,simple,reasons,easy=r
        qs.append(dict(number=n,text=text,translation=ja,choices=choices,
                       choiceTranslations=meanings,answer=answer,grammar=grammar,grammarSimple=simple,
                       choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t}。{why}" for i,(c,t,why) in enumerate(zip(choices,meanings,reasons),1)],
                       choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t}。{why}" for i,(t,why) in enumerate(zip(meanings,easy),1)],
                       questionAudio=f"audio/q{n}.mp3"))
    sections=[
        dict(name="大問1",nameEn="Part 1",type="vocabulary",instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[:15]),
        dict(name="大問2",nameEn="Part 2",type="vocabulary",instruction="次の(16)から(20)までの会話について，(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[15:]),
        dict(name="大問3",nameEn="Part 3",type="sentence-order",instruction="次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて□の中に入れなさい。そして，2番目と4番目にくるものの最も適切な組合せを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。※ただし，(　)の中では，文のはじめにくる語も小文字になっています。",questions=o.questions()),
        dict(name="大問4",nameEn="Part 4",type="reading-comprehension",instruction="次の掲示・Eメール・英文を読み、それぞれの問いに答えなさい。",passages=p.PASSAGES),
    ]
    listening=[3,3,1,3,3,2,3,2,3,2,4,2,3,4,2,2,3,2,3,4,2,3,4,3,1,1,2,4,1,3]
    return dict(grade="grade4",year="2026",session="2026-2-sat",exam="2026-2-sat",
                title="英検4級 2026年度 第2回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)
