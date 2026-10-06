"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("milk","牛乳","名詞","I drink milk every morning.","私は毎朝牛乳を飲みます。",["かばん","学校","犬"],"大問1 Q1","milk"),
    ("people","人々","名詞","Many people visit this park.","たくさんの人がこの公園を訪れます。",["机","鉛筆","木々"],"大問1 Q2","people"),
    ("try again","もう一度試す","熟語","Please try again.","もう一度試してください。",["すぐに会う","踊り始める","手を洗う"],"大問1 Q3","try again"),
    ("class","授業","名詞","Our English class starts at nine.","私たちの英語の授業は9時に始まります。",["水","地図","机"],"大問1 Q4","class"),
    ("see","見る・見える","動詞","Can you see the bird?","その鳥が見えますか。",["開ける","歌う","書く"],"大問1 Q5","see"),
    ("draw","描く","動詞","I like to draw pictures.","私は絵を描くのが好きです。",["跳ぶ","言う","歌う"],"大問1 Q6","drawing"),
    ("door","ドア","名詞","Please open the door.","ドアを開けてください。",["消しゴム","歌手","Tシャツ"],"大問1 Q7","door"),
    ("all right","よい・いいですよ","表現","All right. You can use my pen.","いいですよ。私のペンを使ってもいいです。",["初めまして","おやすみなさい","どういたしまして"],"大問1 Q8","All right"),
    ("from A to B","AからBまで","熟語","We go from Tokyo to Osaka.","私たちは東京から大阪へ行きます。",["Aの下にB","AとBの間に","Aの後ろにB"],"大問1 Q9","from Tokyo to Osaka"),
    ("get up","起きる","熟語","I get up at six.","私は6時に起きます。",["見上げる","帰宅する","座る"],"大問1 Q10","get up"),
    ("how long","どのくらいの長さ・期間","表現","How long is your music lesson?","音楽のレッスンはどのくらいの長さですか。",["何歳","どのくらいの高さ","だれのもの"],"大問1 Q11","How long"),
    ("what about you","あなたはどうですか","表現","I like cats. What about you?","私は猫が好きです。あなたはどうですか。",["どこにいますか","何歳ですか","だれのものですか"],"大問1 Q12","What about you"),
    ("whose","だれの・だれのもの","疑問詞","Whose bag is this?","これはだれのかばんですか。",["いつ","どこ","どうやって"],"大問1 Q13","Whose"),
    ("mine","私のもの","代名詞","This pencil is mine.","この鉛筆は私のものです。",["彼のもの","あなたのもの","彼らのもの"],"大問1 Q14","mine"),
    ("be quiet","静かにする・静かにして","熟語","Please be quiet in the library.","図書館では静かにしてください。",["急ぐ","入る","立つ"],"大問1 Q15","be quiet"),
    ("before","～の前に","前置詞","I study English before school.","私は学校が始まる前に英語を勉強します。",["～の後に","～の下に","～の中に"],"大問2 Q17","Before"),
    ("newspaper","新聞","名詞","My mother reads a newspaper.","母は新聞を読みます。",["教科書","手紙","地図"],"大問2 Q18","newspaper"),
    ("textbook","教科書","名詞","This is my English textbook.","これは私の英語の教科書です。",["ノート","新聞","鉛筆"],"大問2 Q19","textbook"),
    ("listen to","～を聞く","熟語","Let's listen to music.","音楽を聞きましょう。",["～を見る","～を描く","～を書く"],"大問3 Q21","listen to"),
    ("a lot of","たくさんの～","熟語","I have a lot of books.","私は本をたくさん持っています。",["1冊の～","少しの～","～の前に"],"大問3 Q23","a lot of"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2026-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="空所の前後を読んで「セット」で選ぶ",subtitle="Context Clues & Set Phrases",color="#4f8cff",label="基本セット表現",
             explanation="大問1は空所だけでなく前後の文を読む。Q1 の drinks it なら飲み物 milk、Q6 の a picture なら drawing。Q8 は All right、Q9 は from A to B、Q10 は get up、Q12 は What about you のセット。Q11 の thirty minutes は時間の長さなので How long、Q13 の Ted's は持ち主なので Whose。Q14 は my notebook を mine に置き換え、Q15 の命令文は be の原形を使う。意味の手がかりを探してから、決まり文句と動詞の形を確かめる。",
             simple="まず、あきのまえとあともよもう。のむものなら milk、えをかくなら draw。All right、get up、What about you はセット。30ぷんはながさ、Ted's はもちぬし。『しずかにして』は Be quiet. だよ。",
             source="大問1 Q8・Q9・Q11・Q13・Q15",quote="All right. You can. / from Tokyo to Osaka / How long is your guitar lesson today, Kana? / Whose is it? / Just be quiet.",
             examples=[(filled(8),"A：リサ、コンピューターを使ってもいいですか。\nB：いいですよ。使ってもかまいません。","Can I ...? の許可に All right と応じる。","All right. は『いいよ』だね。"),
                       (filled(11),"A：カナ、今日のギターのレッスンはどのくらいの長さですか。\nB：30分です。その後、公園で遊びましょう。","minutes は時間の長さ。How old の年齢とは区別する。","30ぷんだから、How long だね。"),
                       (filled(15),"A：エミリー、図書館で話さないでください。ただ静かにしてね。\nB：分かりました。ごめんなさい。","命令文は動詞の原形 be。相手が you でも are にしない。","Be quiet. をセットでおぼえよう。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [8,9,10,11,12,13,14,15]),
             passageJa="【Q8】コンピューターを使う許可を求め、いいですよと答える。\n【Q9】姉（妹）は大阪に住み、私は東京から大阪へ電車で訪ねる。\n【Q10】毎朝7時に起きて学校へ行く。\n【Q11】ギターのレッスンは30分で、その後公園で遊ぶ。\n【Q12】日本の音楽が好きで、相手も好きだと答える。\n【Q13】カメラはテッドのもの。\n【Q14】ノートは私のもの。\n【Q15】図書館では静かにする。",
             patterns=["All right","from Tokyo to Osaka","get up","How long","What about you","Whose","mine","be quiet"],
             questions=[("Q11で How long を選ぶ手がかりは？","thirty minutes。レッスンの時間の長さを答えている。"),
                        ("Q13で Whose を選ぶ理由は？","It's Ted's. が持ち主を答える文だから。When・Where は時期・場所を尋ねる。"),
                        ("Q15は相手が Emily なのに are を使わないのはなぜ？","命令文は動詞の原形を使う。be動詞の原形は be なので Be quiet.。")],
             easyQuestions=[("get up はどんないみ？","おきる、だよ。"),("mine はどんないみ？","わたしのもの、だよ。"),("しずかにして、はえいごで？","Be quiet. だよ。")]),
        dict(title="会話は「場面」と「次のセリフ」で選ぶ",subtitle="Dialogue Situations & Flow",color="#34d399",label="会話のつながり",
             explanation="大問2では直前の質問と直後の返答をつなぐ。Q16 の Good idea は Let's get some flowers という提案への賛成。Q17 の When には Before school と時期を答える。For two hours は時間の長さで別の質問。Q18 の what are you reading には読む物 Today's newspaper。Q19 の Is this your textbook には物を受ける it を使い Yes, it is。Q20 は家を訪問したあいさつ Good evening から Is John home?、Come in と続く。",
             simple="つぎのセリフがヒントだよ。Good idea は『いいかんがえ』だから、Let's でさそおう。When は『いつ』、what は『なに』。きょうかしょは it。いえにきたら、まずあいさつするね。",
             source="大問2 Q16～Q20",quote="Let's get some flowers. / Before school. / Today's newspaper. / Yes, it is. / Good evening, Mrs. Smith.",
             examples=[(filled(16),"姉妹1：お母さんの誕生日です。花を買いましょう。\n姉妹2：いい考えですね。","Let's の提案を Good idea が受ける。","おはなをかおう、いいかんがえだね、というつながり。"),
                       (filled(17),"男の子：いつ英語を勉強しますか。\n女の子：学校が始まる前に。","When は時期。For two hours の長さとは違う。","『いつ』に『がっこうのまえ』とこたえるね。"),
                       (filled(19),"先生：ジェイコブ、これはあなたの教科書ですか。\n生徒：はい、そうです。ありがとうございます、ウィリアムズ先生。","this が指す textbook を返答では it で受ける。","きょうかしょだから、he ではなく it だね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】母の誕生日に花を買おうと提案し、賛成する。\n【Q17】英語を勉強するのは学校が始まる前。\n【Q18】母が読んでいるのは今日の新聞。\n【Q19】自分の教科書だと答え、先生にお礼を言う。\n【Q20】こんばんはとあいさつし、ジョンが家にいるかを尋ねる。中へどうぞと招かれる。",
             patterns=["Let's get some flowers","Before school","Today's newspaper","Yes, it is","Good evening"],
             questions=[("Q16はなぜ That's great. ではない？","感想だけでは具体的な提案がない。Good idea. は花を買う提案に賛成している。"),
                        ("Q17の For two hours は何を答える？","時間の長さ。When の時期ではなく、How long の質問に答える。"),
                        ("Q19で No, he isn't. が合わない理由は？","he は男性で、質問の教科書を指さない。物の textbook は it で受ける。")],
             easyQuestions=[("Good idea. はどんないみ？","いいかんがえだね、だよ。"),("おかあさんがよんでいるのは？","きょうのしんぶんだよ。"),("Good evening はいつのあいさつ？","よるに、こんばんはとあいさつするよ。")]),
        dict(title="並べ替え——5つの「型」を先に思い出す",subtitle="Sentence Order Patterns (4 words)",color="#a78bfa",label="整序の型",
             explanation="Q21 は Let's listen to＋聞くもの＋in＋場所。Q22 は goes running＋before lunch。Q23 は My brother has＋a lot of＋持ち物。Q24 は It's time for＋名詞。Q25 は Does＋主語＋原形 have＋a digital camera?。4つの語句を並べ、空所内の1番目と3番目を答える。this CD・my brother・a lot・your brother は各1つのかたまり。固定の Let's、Mr. Adams、Grandpa, や文末の語句は数えない。完成文を確かめてから、2つの位置を選択肢と照合する。",
             simple="4つのことばのかたまりをならべよう。my brother や a lot は、わけないよ。さいしょからある Let's などは、かぞえない。あいているところの1ばんめと3ばんめをこたえよう。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Let's listen to this CD in my room. / My brother has a lot of comic books. / Does your brother have a digital camera?",
             examples=[(filled(21),"ぼくの部屋でこのCDを聞こう。","空所は listen→to→this CD→in。1番目①listen、3番目③this CD。","Let's はかぞえず、listen が1ばんめだよ。"),
                       (filled(23),"私の兄はマンガをたくさん持っています。","主語 My brother に has。a lot of はセット。1番目③my brother、3番目④a lot。","my brother と a lot は、それぞれひとつだよ。"),
                       (filled(25),"あなたのお兄さんはデジタルカメラを持っていますか。","Does→your brother→have→a。1番目③does、3番目②have。Does の後ろは原形 have。","しつもんは Does から。have はもとの形だね。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】ぼくの部屋でこのCDを聞こう。\n【Q22】アダムズさんは昼食前に走りに行く。\n【Q23】私の兄はマンガをたくさん持っている。\n【Q24】おじいさん、お茶の時間ですよ。\n【Q25】あなたのお兄さんはデジタルカメラを持っていますか。",
             patterns=["listen to","goes running","before lunch","a lot of","it's time for","your brother have"],
             questions=[("Q21の1番目は Let's ではないの？","Let's は固定部分。4つの空所だけを数え、listen が1番目、this CD が3番目。選択肢4。"),
                        ("Q22の1番目と3番目は？","goes→running→before→lunch なので、③goes と④before。固定の Mr. Adams は数えない。選択肢3。"),
                        ("Q25で has ではなく have を使うのはなぜ？","Does が三人称単数の疑問文を作るので、その後ろの動詞は原形 have。1番目③does、3番目②have で選択肢4。")],
             easyQuestions=[("your brother は2つにわける？","わけないよ。ひとつのかたまりだね。"),("さいしょの Grandpa, もかぞえる？","かぞえないよ。あいている4つのところだけだね。"),("どこをこたえる？","あいているところの1ばんめと3ばんめだよ。")]),
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
    return dict(title="英検5級 2026年度 第2回（土曜準会場）",focusPoints=points)
