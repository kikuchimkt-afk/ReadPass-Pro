"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("cousin","いとこ","名詞","My cousin lives in Osaka.","私のいとこは大阪に住んでいます。",["おじ","おば","息子"],"大問1 Q1","cousin"),
    ("picnic","ピクニック","名詞","Let's go on a picnic tomorrow.","明日ピクニックに行きましょう。",["算数","電車","先生"],"大問1 Q2","picnic"),
    ("answer","答える・（電話に）出る","動詞","Please answer my question.","私の質問に答えてください。",["料理する","飲む","行く"],"大問1 Q3","answer"),
    ("jump","跳ぶ・ジャンプする","動詞","My dog can jump very well.","私の犬はとても上手に跳べます。",["書く","飲む","走る"],"大問1 Q4","jump"),
    ("rabbit","ウサギ","名詞","The white rabbit is eating a carrot.","その白いウサギはニンジンを食べています。",["地図","ペン","ネコ"],"大問1 Q5","rabbit"),
    ("clock","時計","名詞","There is a big clock in the station.","駅に大きな時計があります。",["テーブル","カップ","カレンダー"],"大問1 Q6","clock"),
    ("late","遅れた・遅い","形容詞","Don't be late for school.","学校に遅れないでね。",["速い","短い","難しい"],"大問1 Q7","late"),
    ("glass","グラス・コップ","名詞","I drink a glass of milk every morning.","私は毎朝コップ1杯の牛乳を飲みます。",["硬貨","カメラ","口"],"大問1 Q8","glass"),
    ("at home","家に・家で","熟語","I study at home on Sundays.","私は日曜日には家で勉強します。",["学校で","外で","公園で"],"大問1 Q9","at home"),
    ("a lot of","たくさんの","熟語","There are a lot of books in the library.","図書館にはたくさんの本があります。",["少しの","いくつかの","1つの"],"大問1 Q10","a lot of"),
    ("after school","放課後","熟語","We clean the classroom after school.","私たちは放課後に教室をそうじします。",["授業の前に","昼休みに","毎朝"],"大問1 Q11","after school"),
    ("stand up","立ち上がる","熟語","Please stand up, everyone.","皆さん、立ってください。",["座る","歌う","ほほえむ"],"大問1 Q12","stand up"),
    ("dance","踊る","動詞","Can you dance well?","あなたは上手に踊れますか。",["歌う","泳ぐ","走る"],"大問1 Q13","dance"),
    ("quiet","静かな","形容詞","Please be quiet in the library.","図書館では静かにしてください。",["うるさい","明るい","速い"],"大問1 Q14","quiet"),
    ("how","どう・どのように","疑問詞","How is the weather in Sapporo?","札幌の天気はどうですか。",["どこ","いつ","何"],"大問1 Q15","How"),
    ("gym","体育館","名詞","We play basketball in the gym.","私たちは体育館でバスケットボールをします。",["台所","教室","公園"],"大問2 Q16","gym"),
    ("Wednesday","水曜日","名詞","We have a music class on Wednesday.","私たちは水曜日に音楽の授業があります。",["月曜日","金曜日","日曜日"],"大問2 Q17","Wednesday"),
    ("hungry","おなかがすいた","形容詞","I'm hungry. Let's eat lunch.","おなかがすきました。昼食を食べましょう。",["眠い","のどがかわいた","うれしい"],"大問2 Q20","hungry"),
    ("grandmother","祖母・おばあさん","名詞","My grandmother likes flowers.","私の祖母は花が好きです。",["祖父","おば","母"],"大問3 Q23","grandmother"),
    ("breakfast","朝食","名詞","I eat bread for breakfast.","私は朝食にパンを食べます。",["昼食","夕食","おやつ"],"大問3 Q25","breakfast"),
]

def vocabulary():
    result=[]
    for i,(word,meaning,pos,example,ja,distractors,source,form) in enumerate(VOCAB,1):
        slug=re.sub(r"[^a-z0-9]+","_",word.lower()).strip("_")
        result.append(dict(word=word,meaning=meaning,pos=pos,level="5級",example=example,exampleJa=ja,
                           distractors=distractors,source=source,sourceForm=form,
                           wordAudio=f"audio/vocab/w_{i:03}_{slug}.mp3",exampleAudio=f"audio/vocab/ex_{i:03}_{slug}.mp3"))
    return result

def lessonplan(sections):
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2025-1_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="前後の手がかりと語の「組み合わせ」で選ぶ",subtitle="Context Clues, Set Phrases & Word Forms",color="#4f8cff",label="手がかりと組み合わせ",
             explanation="大問1は空所の前後に手がかりがある。Q1 は He's my uncle Bob's son.（おじの息子）から cousin、Q6 は What time is it now? と on the wall から clock、Q7 は I can't wait. と I'm coming right now. から late を選ぶ。Q2 の have a picnic、Q3 の answer the phone、Q8 の a glass of ～、Q9 の at home、Q10 の a lot of ～、Q11 の after school、Q12 の stand up は語の組み合わせで覚える。Q13 は one sister を受けて She、Q14 は please の命令文なので原形の be、Q15 は Good, thank you. と答えているので How。意味の手がかりを見つけてから、語の形も確かめる。",
             simple="あきのまえとあとをよもう。『おじさんのむすこ』なら cousin、『かべのとけい』なら clock。have a picnic、answer the phone、a glass of、at home、a lot of、stand up はセットでおぼえよう。『しずかにしてね』は please be quiet、『げんき？』は How are you? だよ。",
             source="大問1 Q1・Q3・Q8・Q9・Q10",quote="He's my uncle Bob's son. / Can you answer the phone, please? / Can I have a glass of orange juice, Mom? / My sister is always at home in the morning. / Helen has a lot of comic books.",
             examples=[(filled(1),"A：あれはあなたのお兄さん（弟さん）ですか。\nB：いいえ、あれは私のいとこです。彼は私のおじのボブの息子です。","uncle（おじ）の son（息子）は自分の cousin（いとこ）。後ろの文が答えの手がかりになっている。","おじさんのむすこは、いとこだね。"),
                       (filled(8),"A：お母さん、オレンジジュースをグラス1杯もらえますか。\nB：ええ、はい、どうぞ。","a glass of ～ で『グラス1杯の～』。Here you are. は物を手渡すときの言い方。","a glass of で『コップ1ぱいの』だね。"),
                       (filled(10),"ヘレンはたくさんの漫画本を持っています。","a lot of ～ で『たくさんの～』。ここでは comic books（漫画本）の数が多いことを表している。","a lot of で『たくさんの』だね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [1,3,8,9,10,13,14,15]),
             passageJa="【Q1】あれは兄弟ではなく、おじのボブの息子で、いとこにあたる。\n【Q3】姉（妹）がここにいないので、電話に出てくれるよう頼む。\n【Q8】オレンジジュースをグラス1杯もらえるか母に頼み、母が手渡す。\n【Q9】姉（妹）は朝はいつも家にいて、出かけない。\n【Q10】ヘレンはたくさんの漫画本を持っている。\n【Q13】私には姉妹が1人いて、彼女はとても上手に踊れる。\n【Q14】トムにここでは静かにするよう言い、トムが謝る。\n【Q15】朝のあいさつで調子を尋ね、元気だと答える。",
             patterns=["cousin","answer the phone","a glass of","at home","a lot of","She can","be quiet","How are you"],
             questions=[("Q1で cousin を選ぶ手がかりは？","B の He's my uncle Bob's son.。おじ（uncle）の息子（son）は、自分のいとこ（cousin）にあたる。"),
                        ("Q10で many ではなく lot を選ぶのはなぜ？","空所の前に a、後ろに of があり、a lot of ～（たくさんの～）の形になるから。a many of とは言わない。"),
                        ("Q14で is や are ではなく be を選ぶのはなぜ？","please を付けた命令文では動詞の原形を使うから。be動詞の原形は be なので please be quiet。")],
             easyQuestions=[("at home はどんないみ？","いえに（いる）、だよ。"),("a glass of orange juice はどんないみ？","コップ1ぱいのオレンジジュース、だよ。"),("How are you? はどんないみ？","『げんき？』ときくあいさつだよ。")]),
        dict(title="会話は「質問の種類」と「答え方」を合わせる",subtitle="Question Words & Matching Replies",color="#34d399",label="会話のつながり",
             explanation="大問2では、相手のセリフが何を尋ねたり求めたりしているかを確かめる。Q16 の Where（どこ）には場所を答える In the school gym.、Q17 の What day（何曜日）には It's Wednesday.、Q18 の what are you cooking?（何を料理しているか）には作っている料理を答える Some soup for lunch.。Q19 は Please don't run（走らないで）という注意に All right.（分かりました）で応じる。Q20 は空所の後ろの Do you want some? と、女の子の I'm very hungry. から、食べ物を作っている I'm making cookies. を選ぶ。",
             simple="Where（どこ）にはばしょ、What day（なんようび）にはようびでこたえよう。『はしらないでね』には All right.（わかりました）。『おなかがすいた』から、クッキーをつくっているとわかるね。",
             source="大問2 Q16～Q20",quote="In the school gym. / It's Wednesday. / Some soup for lunch. / All right. / I'm making cookies.",
             examples=[(filled(16),"女の子：ジミーは今どこにいますか。\n男の子：学校の体育館です。","Where（どこ）の質問には、in＋場所で答える。gym は『体育館』。","『どこ？』に、ばしょでこたえるね。"),
                       (filled(17),"男の子：リンダ、今日は何曜日ですか。\n女の子：水曜日です。","What day is it today? は曜日を尋ねる質問。It's＋曜日で答える。","『なんようび？』に、ようびでこたえるね。"),
                       (filled(20),"男の子：私はクッキーを作っています。少しほしいですか。\n女の子：はい、お願いします。とてもおなかがすいています。","some は作っているクッキーの一部を指す。I'm very hungry. も、食べ物の話だと分かる手がかり。","some はクッキーのことだよ。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】ジミーは今、学校の体育館にいる。\n【Q17】リンダは、今日は水曜日だと答える。\n【Q18】父は昼食のスープを作っている。\n【Q19】プールのそばで走らないよう注意され、生徒が分かりましたと答える。\n【Q20】クッキーを作っている男の子が少しほしいか尋ね、おなかがすいた女の子がお願いする。",
             patterns=["Where is","In the school gym","What day","It's Wednesday","Some soup","All right","making cookies"],
             questions=[("Q16で At noon. が合わないのはなぜ？","At noon.（正午に）は時を答える言い方だから。Where（どこ）と場所を聞かれているので、In the school gym. が合う。"),
                        ("Q19の All right. はどんな気持ちを表す？","『分かりました』と、注意や頼みを受け入れる気持ち。プールのそばで走らないでという注意に応じている。"),
                        ("Q20で I'm making cookies. を選ぶ手がかりは？","空所の後ろの Do you want some? と、女の子の I'm very hungry.。食べ物を作っていて、それを少し分けようとしていると分かる。")],
             easyQuestions=[("Where はどんないみ？","どこ、だよ。"),("What day is it today? はなにをきいている？","きょうはなんようび？ときいているよ。"),("All right. はどんないみ？","わかりました、だよ。")]),
        dict(title="並べかえ——「だれが」と動詞のかたまりから組み立てる",subtitle="Word Order: Subjects, Verbs & Phrases",color="#a78bfa",label="整序の型",
             explanation="Q21 は our cat is ten years old（主語＋is＋年齢）、Q24 は Chris is from Australia（be from ～で『～の出身』）。Q23 は My grandmother lives in Tokyo、Q25 は Mr. Reed swims before breakfast で、どちらも主語の後ろに s の付いた動詞を置く。Q22 は Who が主語の疑問文で、Who is walking with ～? と who のすぐ後ろに is を置く。our cat・years old・Mr. Reed はそれぞれ1つのかたまり。固定の My や文末の Mr. Suzuki?・every day. は数えず、4つの空所の1番目と3番目を答える。完成文を確かめてから、2つの位置を選択肢と照合する。",
             simple="まず『だれが』をきめて、そのあとに is や lives、swims をおこう。『～さい』は is ten years old、『～しゅっしん』は is from ～ だよ。My や every day. はかぞえないよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Our cat is ten years old. / My grandmother lives in Tokyo. / Mr. Reed swims before breakfast every day.",
             examples=[(filled(21),"私達のネコは10歳です。","空所は our cat→is→ten→years old。1番目②our cat、3番目④ten。","our cat はひとつのかたまりだよ。"),
                       (filled(22),"鈴木先生と歩いているのはだれですか。","who→is→walking→with。1番目④who、3番目①walking。Who が主語なので、すぐ後ろに is を置く。","Who is walking ～? のじゅんだね。"),
                       (filled(25),"リードさんは，毎日朝食前に泳ぎます。","Mr. Reed→swims→before→breakfast。1番目④Mr. Reed、3番目③before。every day. は固定部分。","every day. はかぞえないよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】私達のネコは10歳です。\n【Q22】鈴木先生と歩いているのはだれですか。\n【Q23】私の祖母は東京に住んでいます。\n【Q24】クリスはオーストラリア出身です。\n【Q25】リードさんは，毎日朝食前に泳ぎます。",
             patterns=["years old","Who is walking","lives in","is from","before breakfast"],
             questions=[("Q21の1番目と3番目は？","our cat→is→ten→years old なので、②our cat と④ten。選択肢1。"),
                        ("Q22で who のすぐ後ろに is を置くのはなぜ？","Who（だれが）がそのまま主語になる疑問文だから。Who is walking with Mr. Suzuki? で、1番目④who、3番目①walking。選択肢4。"),
                        ("Q23の My は1番目に数える？","数えない。My は最初から書かれている固定部分。空所は grandmother→lives→in→Tokyo で、1番目①grandmother、3番目④in。選択肢3。")],
             easyQuestions=[("our cat は2つにわける？","わけないよ。ひとつのかたまりだね。"),("『～しゅっしん』はえいごで？","be from ～ だよ。Chris is from Australia. だね。"),("every day. もかぞえる？","かぞえないよ。あいている4つのところだけだね。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],
                           explanationSimple=s["simple"],sourceQuote=s["quote"],sourceLocation=s["source"],
                           sourceQuoteAudio=f"audio/fp{n}_source.mp3",
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy,audio=f"audio/fp{n}_ex{i}.mp3") for i,(en,ja,note,easy) in enumerate(s["examples"],1)],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"],audioFile=f"audio/practice_pp{n}.mp3"),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],
                           practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(title="英検5級 2025年度 第1回（土曜準会場）",focusPoints=points)
