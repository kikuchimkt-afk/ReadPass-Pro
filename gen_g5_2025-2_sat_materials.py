"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("or","～か…・または","接続詞","Do you want tea or coffee?","紅茶とコーヒーのどちらがほしいですか。",["しかし","だから","～へ"],"大問1 Q1","or"),
    ("Monday","月曜日","名詞","I have a piano lesson on Monday.","私は月曜日にピアノのレッスンがあります。",["日曜日","金曜日","6月"],"大問1 Q2","Monday"),
    ("yellow","黄色（の）","形容詞","My new bag is yellow.","私の新しいかばんは黄色です。",["赤（い）","青（い）","白（い）"],"大問1 Q3","yellow"),
    ("bed","ベッド","名詞","My cat is sleeping on the bed.","私の猫はベッドの上で眠っています。",["机","いす","本棚"],"大問1 Q4","bed"),
    ("March","3月","名詞","My birthday is in March.","私の誕生日は3月です。",["2月","8月","12月"],"大問1 Q5","March"),
    ("people","人々","名詞","There are many people at the station.","駅にはたくさんの人がいます。",["本","塔","かばん"],"大問1 Q6","people"),
    ("hair","髪","名詞","My sister has short hair.","私の姉（妹）は髪が短いです。",["目","手","顔"],"大問1 Q7","hair"),
    ("a little","少し","熟語","This bag is a little big.","このかばんは少し大きいです。",["とても","たくさんの","いちばん"],"大問1 Q8","a little"),
    ("after school","放課後","熟語","I play soccer after school.","私は放課後にサッカーをします。",["授業の前に","昼食の時間に","毎朝"],"大問1 Q9","after school"),
    ("listen to","～を聞く","熟語","I listen to music every night.","私は毎晩音楽を聞きます。",["～を見る","～を開ける","～を書く"],"大問1 Q10","listens to"),
    ("how about","～はどうですか","表現","How about this red cap?","この赤い帽子はどうですか。",["いくらですか","何時ですか","だれのものですか"],"大問1 Q11","How about"),
    ("take a picture","写真を撮る","熟語","Let's take a picture here.","ここで写真を撮りましょう。",["手紙を書く","絵を見る","店に行く"],"大問1 Q12","take a picture"),
    ("quiet","静かな","形容詞","The library is very quiet.","図書館はとても静かです。",["うるさい","明るい","大きい"],"大問1 Q13","quiet"),
    ("mine","私のもの","代名詞","That blue bike is mine.","あの青い自転車は私のものです。",["彼のもの","あなたのもの","彼女のもの"],"大問1 Q14","mine"),
    ("where","どこ","疑問詞","Where is my cap?","私の帽子はどこですか。",["いつ","だれ","どのように"],"大問1 Q15","Where"),
    ("name","名前","名詞","My dog's name is Pochi.","私の犬の名前はポチです。",["友達","家","学校"],"大問2 Q16","name"),
    ("ask","尋ねる・聞く","動詞","Please ask your teacher.","先生に聞いてください。",["答える","買う","書く"],"大問2 Q17","ask"),
    ("shoes","くつ","名詞","I want new shoes.","私は新しいくつがほしいです。",["ぼうし","かさ","かばん"],"大問2 Q18","shoes"),
    ("kind","親切な","形容詞","My teacher is very kind.","私の先生はとても親切です。",["背が高い","忙しい","新しい"],"大問3 Q21","kind"),
    ("practice","練習する","動詞","I practice the guitar every day.","私は毎日ギターを練習します。",["教える","聞く","作る"],"大問3 Q23","practice"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2025-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="前後の文の手がかりと「組み合わせ」で選ぶ",subtitle="Clues, Set Phrases & Word Forms",color="#4f8cff",label="手がかりと組み合わせ",
             explanation="大問1は空所の前後に手がかりがある。Q4 は can't sleep well から bed、Q5 は the third month of the year から March を選ぶ。Q8 の a little difficult、Q9 の after school、Q10 の listen to、Q11 の How about ～?、Q12 の take a picture of ～ は語の組み合わせで覚える。Q13 は命令文なので原形の Be、Q14 は yours と聞かれて mine、Q15 は In Los Angeles と場所を答えているので Where。意味の手がかりを見つけてから、語の形も確かめる。",
             simple="あきのまえとあとをよもう。『よくねむれない』なら bed、『3ばんめのつき』なら March。a little、after school、How about、take a picture はセットでおぼえよう。『しずかにして』は Be quiet.、『わたしのもの』は mine だよ。",
             source="大問1 Q8・Q11・Q13・Q14・Q15",quote="The questions are always a little difficult. / How about pizza? / Be quiet, everyone. / It's not mine. / Where does Kate live?",
             examples=[(filled(8),"私は毎週金曜日に数学のテストがあります。問題はいつも少し難しいです。","a little＋形容詞で『少し～』。difficult の程度を表している。","a little で『すこし』だね。"),
                       (filled(11),"A：昼食の時間です。ピザはどうですか。\nB：いい考えですね。チーズがのったものがほしいです。","How about＋名詞? で提案し、Good idea. で賛成している。","How about ～? は『～はどう？』だね。"),
                       (filled(14),"A：これはだれの教科書ですか。あなたのものですか。\nB：私のものではありません。ジョンのものです。","yours（あなたのもの）と聞かれ、mine（私のもの）で答える。John's も『ジョンのもの』。","mine は『わたしのもの』だね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [8,9,10,11,12,13,14,15]),
             passageJa="【Q8】毎週金曜日の数学のテストは、いつも少し難しい。\n【Q9】チャーリーは放課後、たいていテニスをする。\n【Q10】ケンタはジャズが好きで、よく部屋で聞く。\n【Q11】昼食にピザを提案し、チーズがのったピザがほしいと答える。\n【Q12】とても美しい花の写真を撮ろうと誘う。\n【Q13】皆に静かにするよう言い、会議を始める。\n【Q14】教科書は自分のものではなく、ジョンのもの。\n【Q15】ケイトはロサンゼルスに住んでいる。",
             patterns=["a little","after school","listens to","How about","take a picture","Be quiet","mine","Where does"],
             questions=[("Q8の a little difficult はどんな意味？","『少し難しい』。a little が difficult の程度を表している。"),
                        ("Q13で Are ではなく Be を選ぶのはなぜ？","命令文では動詞の原形を使うから。be動詞の原形は be なので Be quiet。"),
                        ("Q15で Where を選ぶ手がかりは？","B の In Los Angeles.。住んでいる場所を答えているので、場所を尋ねる Where。")],
             easyQuestions=[("after school はどんないみ？","がっこうのあと（ほうかご）、だよ。"),("しゃしんをとる、はえいごで？","take a picture だよ。"),("mine はどんないみ？","わたしのもの、だよ。")]),
        dict(title="会話は「質問の種類」と「続くセリフ」で選ぶ",subtitle="Dialogue Responses & Follow-up Lines",color="#34d399",label="会話のつながり",
             explanation="大問2では、相手の質問の種類と、空所の前後のセリフをつなげて考える。Q16 の Who is that girl? には名前を伝える Her name is Tomoko.。Q17 は Mom has many kinds of pens. を受けて Please ask her.（her＝Mom）。Q18 は I like your shoes とほめられて Thank you.。Q19 は often（よく）の質問に Yes と答えた後、I play every Sunday. と具体的に続ける。Q20 は You can use this one. の後に、ペンを貸せる理由として I have two. が続く。",
             simple="まえのセリフとあとのセリフをつなげよう。『だれ？』にはなまえ、ほめられたら Thank you.、『よくする？』には『まいしゅうにちようびにするよ』。ペンを2ほんもっているから、かしてあげられるね。",
             source="大問2 Q16～Q20",quote="Her name is Tomoko. / Please ask her. / Thank you. / I play every Sunday. / I have two.",
             examples=[(filled(16),"父：あの女の子はだれですか。\n女の子：彼女の名前はトモコです。私の友達です。","Who（だれ）の質問に、名前と自分との関係を答えている。","『だれ？』に、なまえでこたえるね。"),
                       (filled(17),"女の子：お父さん、赤いペンが必要です。\n父：お母さんがいろいろな種類のペンを持っています。お母さんに聞いてください。","her は直前の Mom を指す。ペンを持っている人に聞くよう勧めている。","her は おかあさんのことだよ。"),
                       (filled(20),"男の子：困った。ペンを持っていません。\n女の子：これを使っていいですよ。2本持っています。","I have two. が、ペンを貸せる理由になっている。this one の one はペンを指す。","2ほんあるから、かしてあげられるね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】あの女の子の名前はトモコで、自分の友達だと説明する。\n【Q17】赤いペンが必要な娘に、父はペンをたくさん持っている母に聞くよう言う。\n【Q18】くつをほめられてお礼を言い、新しいくつだと話す。\n【Q19】スティーブはテニスをよくして、毎週日曜日にしている。\n【Q20】ペンがない男の子に、2本持っている女の子がペンを貸す。",
             patterns=["Her name is Tomoko","Please ask her","Thank you","I play every Sunday","I have two"],
             questions=[("Q16で Nice to meet you. が合わないのはなぜ？","初めて会った相手へのあいさつで、父の『あの女の子はだれ？』という質問に答えていないから。"),
                        ("Q17の her はだれのこと？","直前の Mom（お母さん）。ペンをたくさん持っている母に聞くよう勧めている。"),
                        ("Q19で I play basketball. が合わないのはなぜ？","テニスをよくするかと聞かれて Yes と答えているので、続くのはテニスをする日を伝える I play every Sunday.。")],
             easyQuestions=[("ほめられたら、なんといえばいい？","Thank you.（ありがとう）だよ。"),("every Sunday はどんないみ？","まいしゅうにちようび、だよ。"),("I have two. はどんないみ？","2ほんもっている、だよ。")]),
        dict(title="並べかえ——疑問詞・命令文・be動詞の「型」から組み立てる",subtitle="Word Order: Questions, Commands & be-Verbs",color="#a78bfa",label="整序の型",
             explanation="Q21 は you are very kind（主語＋be動詞＋very＋形容詞）。Q22 は When is＋主語?、Q24 は When do you＋動詞の原形?、Q23 は How does＋主語＋動詞の原形?。この3問では、疑問詞のすぐ後ろに be動詞や do・does を置く。Q25 は Don't＋動詞の原形で『～しないで』。your sister は1つのかたまり。固定の George,・Judy,・Don't や文末の語句は数えず、4つの空所の1番目と3番目を答える。完成文を確かめてから、2つの位置を選択肢と照合する。",
             simple="4つのことばをならべよう。『いつ？』は When、『どうやって？』は How ではじめるよ。『～しないで』は Don't のあとに eat。George, や Judy, はかぞえないよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="George, you are very kind. / Judy, how does your sister practice the piano? / Don't eat cookies before dinner.",
             examples=[(filled(21),"ジョージ，あなたはとても親切です。","空所は you→are→very→kind。1番目②you、3番目①very。","George, はかぞえず、you が1ばんめだよ。"),
                       (filled(23),"ジュディ，あなたのお姉さんはどうやってピアノを練習しますか。","how→does→your sister→practice。1番目②how、3番目③your sister。does の後ろは原形 practice。","your sister はひとつのかたまりだよ。"),
                       (filled(25),"夕飯前にはクッキーを食べないで。","eat→cookies→before→dinner。1番目①eat、3番目②before。Don't の後ろは動詞の原形。","Don't のあとは eat だね。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】ジョージ，あなたはとても親切です。\n【Q22】あなたのピアノのコンサートはいつですか。\n【Q23】ジュディ，あなたのお姉さんはどうやってピアノを練習しますか。\n【Q24】あなたはいつ野球をしますか。\n【Q25】夕飯前にはクッキーを食べないで。",
             patterns=["you are very kind","When is","how does","When do","Don't eat"],
             questions=[("Q21の1番目は George, ではないの？","George, は固定の呼びかけ。空所だけを数え、you が1番目、very が3番目。選択肢1。"),
                        ("Q23で practice に s を付けないのはなぜ？","主語 your sister に合わせて does を使っているので、その後ろの動詞は原形 practice。1番目②how、3番目③your sister で選択肢4。"),
                        ("Q24の1番目と3番目は？","when→do→you→play なので、④when と②you。選択肢2。")],
             easyQuestions=[("your sister は2つにわける？","わけないよ。ひとつのかたまりだね。"),("『～しないで』はなにではじめる？","Don't ではじめるよ。"),("Judy, もかぞえる？","かぞえないよ。あいている4つのところだけだね。")]),
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
    return dict(title="英検5級 2025年度 第2回（土曜準会場）",focusPoints=points)
