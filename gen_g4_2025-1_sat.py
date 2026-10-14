# -*- coding: utf-8 -*-
"""Reproduce Grade 4 2025-1 Saturday; booklet pp. 2-11, page images + text layer."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade4/2025-1-sat/data.json"


def module(suffix):
    spec=importlib.util.spec_from_file_location(suffix,ROOT/f"gen_g4_2025-1_sat_{suffix}.py")
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, translation, choices, meanings, answer, normal/simple grammar,
# choice-specific reasons. All four normal/simple analyses retain meanings.
ROWS = [
    ("Sarah works at a high school. She (　) French and Spanish.",
     "サラは高校で働いています。彼女はフランス語とスペイン語を (　)。",
     ["pays","swims","flies","teaches"],["支払う","泳ぐ","飛ぶ","教える"],4,
     "1文目の works at a high school（高校で働いている）がヒント。高校で働くサラが French and Spanish（フランス語とスペイン語）に対してすることは teaches（教える）。選択肢はどれも主語 She に合わせた三人称単数現在の形なので、意味で選ぶ。pays・swims・flies では、言語を目的語にとる意味にならない。",
     "サラはこうこうではたらいているよ。フランスごとスペインごを teaches『おしえる』んだね。",
     ["お金を払う意味で、『フランス語を払う』とは言わない。","泳ぐ意味で、フランス語やスペイン語とつながらない。","飛ぶ意味で、言語とつながらない。","高校で働く人として、言語を教えている。"],
     ["おかねをはらう、ではないよ。","およぐ、ではないよ。","とぶ、ではないよ。","ことばをおしえているんだね。"]),
    ("A: Can I (　) that pencil?\nB: Sure. Please give it back to me after class.",
     "A：その鉛筆を (　) もいいですか。\nB：いいですよ。授業の後で返してくださいね。",
     ["borrow","follow","remember","spread"],["借りる","ついて行く・従う","覚えている・思い出す","広げる・塗る"],1,
     "Can I ～? は『～してもいいですか』と許可を求める言い方。B が Please give it back to me after class.（授業の後で返してね）と答えているので、鉛筆を一時的に使わせてもらう borrow（借りる）が合う。give ～ back は『～を返す』。follow・remember・spread では、後で返すという流れにならない。",
     "『あとでかえしてね』といっているから、えんぴつを borrow『かりる』んだね。かりたものは、あとでかえすよ。",
     ["借りた物は後で返すので、B の返事とつながる。","鉛筆について行く、という意味にはならない。","覚えているかどうかは、返す話とつながらない。","鉛筆を広げることはできず、返す話とも合わない。"],
     ["えんぴつをかりるんだね。","ついていく、ではないよ。","おぼえる、ではないよ。","ひろげる、ではないよ。"]),
    ("Gina is very (　), so she doesn't talk very much.",
     "ジーナはとても (　) ので、あまり話しません。",
     ["fast","shy","light","next"],["速い","恥ずかしがりの・内気な","軽い・明るい","次の"],2,
     "A, so B は『A なので B』。so の後ろの doesn't talk very much（あまり話さない）が結果なので、その理由になる shy（恥ずかしがりの）が合う。fast・light・next では、あまり話さない理由として意味がつながらない。",
     "ジーナははずかしがりやだから、あまりはなさないんだね。so は『だから』だよ。",
     ["速いことは、あまり話さない理由にならない。","恥ずかしがりなので、あまり話さない。","軽いことは、あまり話さない理由にならない。","『次の』では人の様子を表せない。"],
     ["はやい、ではないよ。","はずかしがりやだから、あまりはなさないね。","かるい、ではないよ。","『つぎの』では、いみがつながらないよ。"]),
    ("Japan has many (　). The four main ones are Honshu, Hokkaido, Shikoku, and Kyushu.",
     "日本にはたくさんの (　) があります。主な4つは、本州、北海道、四国、九州です。",
     ["islands","cucumbers","shows","activities"],["島","キュウリ","番組・ショー","活動"],1,
     "2文目の ones は、前の文の空所に入る名詞をくり返さずに指す語。主な4つが本州・北海道・四国・九州なので islands（島）。many の後ろなので複数形になっている。cucumbers（キュウリ）・shows（番組）・activities（活動）では、本州などの名前と合わない。",
     "ほんしゅう、ほっかいどう、しこく、きゅうしゅうは『しま』だね。island は『しま』だよ。",
     ["本州・北海道・四国・九州は島。","野菜で、本州などの名前とつながらない。","番組やショーで、本州などの名前とつながらない。","活動で、本州などの名前とつながらない。"],
     ["しまのなまえだね。","やさいのなまえではないよ。","テレビばんぐみではないよ。","かつどうではないよ。"]),
    ("A: Did you like the dinner at Tom's party?\nB: Yes. I asked his mother many (　) about the food.",
     "A：トムのパーティーの夕食は気に入りましたか。\nB：はい。彼のお母さんに料理についてたくさん (　) をしました。",
     ["gifts","clothes","days","questions"],["贈り物","服","日","質問"],4,
     "ask は『尋ねる』なので、何を尋ねたかとして questions（質問）が合う。ask＋人＋questions で『（人）に質問する』。夕食が気に入ったので、料理について（about the food）トムのお母さんにたくさん質問した。gifts・clothes・days では ask とつながらない。",
     "りょうりがきにいったから、おかあさんにたくさんしつもんしたんだね。ask は『たずねる』、question は『しつもん』だよ。",
     ["贈り物を尋ねる、とは言わない。","服は尋ねるものではなく、料理の話とつながらない。","日を尋ねる、では料理の話とつながらない。","ask と合わせて、料理についてたくさん質問した。"],
     ["プレゼントをたずねる、とはいわないよ。","ふくのことではないよ。","ひにちのことではないよ。","りょうりについてしつもんしたね。"]),
    ("Jack wants to become a famous (　) and be in action movies.",
     "ジャックは有名な (　) になって、アクション映画に出たいと思っています。",
     ["boat","actor","omelet","snack"],["ボート","俳優","オムレツ","軽食・おやつ"],2,
     "become a famous ～ で『有名な～になる』。be in action movies（アクション映画に出る）とあるので、映画に出る仕事の actor（俳優）。boat・omelet・snack は乗り物や食べ物で、人がなるものではない。",
     "アクションえいがにでたいジャック。なりたいのは actor『はいゆう』だね。",
     ["乗り物で、人がなるものではない。","映画に出る仕事なので、アクション映画とつながる。","料理で、人がなるものではない。","食べ物で、人がなるものではない。"],
     ["のりものには、なれないよ。","えいがにでる、はいゆうだね。","たべものには、なれないよ。","おやつには、なれないよ。"]),
    ("Jenny is a new (　) of the tennis club. She practices twice a week.",
     "ジェニーはテニス部の新しい (　) です。彼女は週に2回練習します。",
     ["member","building","school","world"],["一員・メンバー","建物","学校","世界"],1,
     "a member of ～ で『～の一員』。a new member of the tennis club で『テニス部の新しい部員』。週に2回練習するという2文目とも合う。building・school・world は人を表さないので、主語 Jenny とつながらない。",
     "ジェニーはテニスぶのあたらしい member『メンバー』。しゅうに2かいれんしゅうしているよ。",
     ["テニス部の一員で、週に2回練習している。","建物で、人である Jenny を表さない。","学校で、人である Jenny を表さない。","世界で、人である Jenny を表さない。"],
     ["テニスぶのメンバーだね。","たてものではないよ。","がっこうではないよ。","せかいではないよ。"]),
    ("A: Jack! Our train is coming. Hurry (　)!\nB: OK, Dad.",
     "A：ジャック！電車が来るよ。急いで (　)！\nB：分かったよ、お父さん。",
     ["much","to","for","up"],["たくさん・とても","～へ","～のために","上へ"],4,
     "Hurry up! で『急いで！』という決まった言い方。電車が来ているので、父がジャックを急がせている。空所の後ろに語がないので、後ろに語句が必要な to や for は使えない。much も hurry と合わせて『急いで』の意味にならない。",
     "でんしゃがくるから『いそいで！』。Hurry up! でおぼえよう。",
     ["much では『急いで』の決まった言い方にならない。","to は後ろに行き先などの語句が必要で、ここでは使えない。","for は後ろに語句が必要で、ここでは使えない。","Hurry up! で『急いで！』。"],
     ["much では、このいいかたにならないよ。","to では、このいいかたにならないよ。","for では、このいいかたにならないよ。","Hurry up! で『いそいで！』だね。"]),
    ("A: Who is the girl in this old picture, Karen? She really (　) like you.\nB: Oh, that's my mother when she was 15 years old.",
     "A：カレン、この古い写真の女の子は誰ですか。本当にあなたのように (　)。\nB：ああ、それは15歳のときの私の母です。",
     ["takes","gives","finds","looks"],["取る・持って行く","与える","見つける","見える"],4,
     "look like ～ で『～に似ている・～のように見える』。写真の女の子がカレンに似ているので、A は誰なのかを尋ねている。B の答えから、その女の子は15歳のころのカレンの母。主語 She に合わせて looks。takes・gives・finds は like you と合わせても『似ている』の意味にならない。",
     "look like は『～ににている』。しゃしんのおんなのこは、カレンににているね。じつは15さいのときのおかあさんだったよ。",
     ["取る・持って行くでは、似ているという意味にならない。","与えるでは、似ているという意味にならない。","見つけるでは、似ているという意味にならない。","looks like you で『あなたに似ている』。"],
     ["とる、ではないよ。","あげる、ではないよ。","みつける、ではないよ。","looks like で『ににている』だね。"]),
    ("Last summer, Ted took a (　) to America. He visited New York and Los Angeles.",
     "去年の夏、テッドはアメリカへ (　) をしました。彼はニューヨークとロサンゼルスを訪れました。",
     ["trip","time","country","park"],["旅行","時間","国","公園"],1,
     "take a trip to ～ で『～へ旅行する』。took は take の過去形。2文目でニューヨークとロサンゼルスを訪れたとあり、旅行の内容と合う。time・country・park では、took a ～ to America で『アメリカへ旅行した』という意味にならない。",
     "take a trip は『りょこうする』。テッドはアメリカりょこうで、ニューヨークとロサンゼルスにいったよ。",
     ["took a trip to America でアメリカへ旅行した。","時間では、アメリカへ行ったことを表せない。","国を持って行く、という意味になってしまう。","公園を持って行く、という意味になってしまう。"],
     ["アメリカりょこうにいったんだね。","『じかん』では、りょこうのいみにならないよ。","『くに』では、りょこうのいみにならないよ。","『こうえん』では、りょこうのいみにならないよ。"]),
    ("A: Well, Jim, can we meet tomorrow?\nB: Yes. Tomorrow is (　) with me.",
     "A：ねえ、ジム、明日会えますか。\nB：はい。明日なら私は (　) です。",
     ["heavy","dark","fine","rainy"],["重い","暗い","大丈夫な・よい","雨の"],3,
     "～ is fine with me で『私は～で大丈夫だ・かまわない』。明日会えるかと聞かれて Yes と答えているので fine が合う。heavy・dark は会う都合を表さない。rainy は天気を表す語で、会う約束の返事にならない。",
     "『あしたあえる？』『うん、あしたならだいじょうぶ』。fine with me は『わたしはだいじょうぶ』だよ。",
     ["重さを表す語で、会う都合を表さない。","暗さを表す語で、会う都合を表さない。","is fine with me で『私は大丈夫』。","天気を表す語で、会えるかどうかの返事にならない。"],
     ["おもい、ではないよ。","くらい、ではないよ。","あしたならだいじょうぶ、だね。","あめのてんきのことではないよ。"]),
    ("A: What kind of sports do you like?\nB: I like many kinds of sports. (　) example, I like soccer, baseball, and basketball.",
     "A：どんな種類のスポーツが好きですか。\nB：たくさんの種類のスポーツが好きです。(　) 例えば、サッカー、野球、バスケットボールが好きです。",
     ["For","In","Of","To"],["～のために・～として","～の中に","～の","～へ"],1,
     "For example, ～ で『例えば～』。B は many kinds of sports（たくさんの種類のスポーツ）が好きだと言った後、具体例としてサッカー・野球・バスケットボールを挙げている。In・Of・To を example の前に置いても『例えば』の意味にならない。",
     "For example は『たとえば』。すきなスポーツのれいを、サッカー、やきゅう、バスケットボールとあげているね。",
     ["For example で『例えば』。具体例を挙げている。","In では『例えば』の意味にならない。","Of では『例えば』の意味にならない。","To では『例えば』の意味にならない。"],
     ["For example で『たとえば』だね。","In では『たとえば』にならないよ。","Of では『たとえば』にならないよ。","To では『たとえば』にならないよ。"]),
    ("I take many subjects at school, but I like English (　) of all.",
     "私は学校でたくさんの教科を取っていますが、すべての中で英語が (　) 好きです。",
     ["good","best","well","better"],["よい","最もよく・いちばん","よく・上手に","よりよく"],2,
     "like A best of all で『すべての中で A がいちばん好き』。of all（すべての中で）があるので最上級の best を使う。better は比較級で、2つを比べるときの形。good と well は原級で『いちばん』の意味を表さない。",
     "of all は『ぜんぶのなかで』。えいごがいちばんすき、だから best だね。",
     ["原級の形容詞で、『いちばん』の意味にならない。","of all と合わせて『いちばん好き』。","原級で、『いちばん』の意味にならない。","比較級で、of all（すべての中で）とは合わない。"],
     ["『いちばん』ではないよ。","いちばんすき、だね。","『いちばん』ではないよ。","『もっと』は、2つをくらべるときだよ。"]),
    ("A: Ben, is this your sister's bag?\nB: No, (　) is red.",
     "A：ベン、これはあなたのお姉さん（妹さん）のかばんですか。\nB：いいえ、(　) は赤です。",
     ["hers","she","her","theirs"],["彼女のもの","彼女は","彼女の・彼女を","彼らのもの"],1,
     "hers は『彼女のもの』で、ここでは her bag（姉（妹）のかばん）を1語で表す。No と答え、姉（妹）のかばんは赤いと説明している。she（彼女は）では『彼女は赤い』になってしまう。her（彼女の・彼女を）は、後ろに bag などの名詞がないと主語にならない。theirs は『彼らのもの』で、1人の姉（妹）を指さない。",
     "hers は『かのじょのもの』。おねえさん（いもうと）のかばんは、あかいんだね。",
     ["her bag の代わりになり、『彼女のかばんは赤い』。","『彼女は赤い』という意味になってしまう。","『彼女の』の意味では後ろに名詞が必要で、her だけでは主語にならない。","複数の人のもので、1人の姉（妹）を指さない。"],
     ["かのじょのかばんは、あかいんだね。","『かのじょは』では、いみがかわるよ。","her のあとには、もののなまえがいるよ。","『かれらのもの』ではないよ。"]),
    ("A: Stop (　) messages to your friends and study for your math test!\nB: OK, Dad.",
     "A：友だちにメッセージを (　) のはやめて、数学のテストの勉強をしなさい！\nB：分かったよ、お父さん。",
     ["send","sending","sent","sends"],["送る（原形）","送ること（-ing形）","送った（過去形）","送る（三人称単数現在）"],2,
     "stop＋動詞の -ing 形で『～するのをやめる』。Stop sending messages で『メッセージを送るのをやめなさい』。父がテスト勉強をするように言っている。send・sent・sends は stop の直後に置いても『～するのをやめる』の形にならない。",
     "stop のあとは ing の形。stop sending で『おくるのをやめる』だよ。",
     ["原形は stop の直後に置いても『～するのをやめる』にならない。","stop sending で『送るのをやめる』。","過去形は stop の直後に置かない。","三人称単数現在形は stop の直後に置かない。"],
     ["stop のあとに send はおかないよ。","stop sending で『おくるのをやめる』だね。","むかしの形ではないよ。","s のついた形ではないよ。"]),
    ("Father: Do you want some more spaghetti, Laura?\nDaughter: No, Dad, (　)",
     "父：ローラ、スパゲッティをもう少しどうですか。\n娘：いいえ、お父さん、(　)",
     ["I'm here.","I don't have one.","I'm full.","I don't know it."],["私はここにいます。","私は1つも持っていません。","おなかがいっぱいです。","私はそれを知りません。"],3,
     "スパゲッティのおかわりをすすめられ、No と断っている。断る理由として I'm full.（おなかがいっぱいです）が合う。full は『満腹の』。I'm here. や I don't know it. では、おかわりを断る理由にならない。",
     "『もうすこしたべる？』『ううん、おなかいっぱい』。full は『おなかがいっぱい』だよ。",
     ["居場所を伝える言葉で、おかわりを断る理由にならない。","持っていない、では食べるかどうかの返事にならない。","満腹なので、おかわりを断っている。","知らない、ではおかわりの返事にならない。"],
     ["ここにいる、ではないよ。","もっていない、ではないよ。","おなかいっぱいだから、いらないんだね。","しらない、ではないよ。"]),
    ("Mother: You don't look well, Jack. Are you OK?\nSon: (　) I didn't sleep well last night.",
     "母：ジャック、具合がよくなさそうね。大丈夫？\n息子：(　) 昨夜はよく眠れなかったんだ。",
     ["It's time for dinner.","This is for you.","It's on TV.","I'm tired."],["夕食の時間です。","これはあなたにです。","それはテレビでやっています。","疲れています。"],4,
     "don't look well は『具合が悪そうだ』。母が心配して Are you OK? と尋ね、息子は I'm tired.（疲れている）と答えて、昨夜よく眠れなかったという理由を続けている。ほかの選択肢は体の調子を答えていない。",
     "『だいじょうぶ？』『つかれているんだ。よくねむれなかったから』。tired は『つかれた』だよ。",
     ["夕食の時間を知らせる言葉で、体調の返事にならない。","物を渡すときの言葉で、体調の返事にならない。","テレビ番組の話で、体調の返事にならない。","疲れている理由として、よく眠れなかったと続く。"],
     ["ごはんのじかん、ではないよ。","プレゼントをわたすことばではないよ。","テレビのはなしではないよ。","ねむれなくて、つかれているんだね。"]),
    ("Girl: How many brothers and sisters do you have?\nBoy: I have one brother. (　)",
     "女の子：兄弟姉妹は何人いますか。\n男の子：兄（弟）が1人います。(　)",
     ["It's very early.","I'll take three.","His name is Ben.","They're very kind."],["とても早いです。","3つください。","彼の名前はベンです。","彼らはとても親切です。"],3,
     "男の子は兄弟が1人いると答え、続けてその兄（弟）について His name is Ben.（彼の名前はベンです）と説明している。His は one brother を指す。They're は複数の人を指すので、1人の兄（弟）には合わない。I'll take three. は買い物で数を伝えるときの言い方。",
     "きょうだいは1にん。そのこのなまえはベンだよ、とせつめいしているね。",
     ["時刻が早いという話で、兄弟の話とつながらない。","買い物で数を伝える言い方で、会話に合わない。","His が one brother を指し、その名前を伝えている。","They're は複数を指し、1人の兄（弟）に合わない。"],
     ["じかんのはなしではないよ。","かいものではないよ。","きょうだいのなまえをおしえているね。","1にんなのに『かれら』はおかしいよ。"]),
    ("Woman 1: Where were you born, Julie?\nWoman 2: (　) I'll take you there someday.",
     "女性1：ジュリー、あなたはどこで生まれたのですか。\n女性2：(　) いつかあなたをそこへ連れて行きますね。",
     ["On a business trip.","In a small town near here.","When I moved to New York.","Twenty-five years old."],
     ["出張で。","この近くの小さな町で。","私がニューヨークに引っ越したときに。","25歳です。"],2,
     "Where were you born? は生まれた場所を尋ねる質問。場所を答える In a small town near here.（この近くの小さな町で）が合う。続く there（そこへ）はその町を指す。When I moved to New York. は時、Twenty-five years old. は年齢を答えている。",
     "『どこでうまれたの？』『このちかくのちいさなまちだよ』。there『そこ』は、そのまちのことだね。",
     ["出張の話で、生まれた場所の答えにならない。","生まれた場所を答え、there がその町を指す。","時を答えていて、場所の答えにならない。","年齢を答えていて、場所の答えにならない。"],
     ["しゅっちょうのはなしではないよ。","うまれたまちをこたえているね。","いつ、をこたえているよ。","なんさい、をこたえているよ。"]),
    ("Mother: You look much better today, Tim. (　)\nSon: I'm fine, thanks.",
     "母：ティム、今日はずっと元気そうね。(　)\n息子：元気だよ、ありがとう。",
     ["When will you go?","What do you like?","How do you feel?","Where is your school?"],
     ["いつ行くのですか。","何が好きですか。","気分はどうですか。","あなたの学校はどこですか。"],3,
     "息子の答え I'm fine, thanks.（元気だよ、ありがとう）は気分や体調を伝える返事なので、How do you feel?（気分はどう？）が合う。much better は『ずっとよい』で、前より元気になった様子。When・What・Where の質問なら、時・物・場所を答える流れになる。",
     "『きぶんはどう？』『げんきだよ、ありがとう』。How do you feel? は『きぶんはどう？』だよ。",
     ["時を聞く質問で、元気だという返事に合わない。","好きな物を聞く質問で、元気だという返事に合わない。","気分を尋ね、元気だと答えている。","場所を聞く質問で、元気だという返事に合わない。"],
     ["いつ、をきいていないよ。","すきなもの、ではないよ。","きぶんをきいているね。","がっこうのばしょではないよ。"]),
]


def build():
    p,o,m=module("passages"),module("order"),module("materials")
    qs=[]
    for n,r in enumerate(ROWS,1):
        text,ja,choices,meanings,answer,grammar,simple,reasons,easy=r
        qs.append(dict(number=n,text=text,translation=ja,choices=choices,
                       choiceTranslations=meanings,answer=answer,grammar=grammar,grammarSimple=simple,
                       choiceAnalysis=[("○ " if i==answer else "")+f"{c}＝{t.rstrip('。')}。{why}" for i,(c,t,why) in enumerate(zip(choices,meanings,reasons),1)],
                       choiceAnalysisSimple=[("○ " if i==answer else "")+f"{t.rstrip('。')}。{why}" for i,(t,why) in enumerate(zip(meanings,easy),1)],
                       questionAudio=f"audio/q{n}.mp3"))
    sections=[
        dict(name="大問1",nameEn="Part 1",type="vocabulary",instruction="次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[:15]),
        dict(name="大問2",nameEn="Part 2",type="vocabulary",instruction="次の(16)から(20)までの会話について，(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",questions=qs[15:]),
        dict(name="大問3",nameEn="Part 3",type="sentence-order",instruction="次の(21)から(25)までの日本文の意味を表すように①から⑤までを並べかえて□の中に入れなさい。そして，2番目と4番目にくるものの最も適切な組合せを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。※ただし，(　)の中では，文のはじめにくる語も小文字になっています。",questions=o.questions()),
        dict(name="大問4",nameEn="Part 4",type="reading-comprehension",instruction="次の掲示・Eメール・英文を読み、それぞれの問いに答えなさい。",passages=p.PASSAGES),
    ]
    listening=[1,3,2,3,1,1,1,2,3,3,4,4,3,1,3,4,4,1,4,2,3,1,3,2,1,1,2,2,2,1]
    return dict(grade="grade4",year="2025",session="2025-1-sat",exam="2025-1-sat",
                title="英検4級 2025年度 第1回（土曜準会場）",sections=sections,
                listening={f"part{i+1}":dict(zip(map(str,range(10*i+1,10*i+11)),listening[10*i:10*i+10])) for i in range(3)},
                vocabulary=m.vocabulary(),lessonPlan=m.lessonplan(sections))


if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),ensure_ascii=False,indent=4)+"\n",encoding="utf-8")
    print(OUT)
