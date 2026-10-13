"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points (2026-2, main venue).

Audio references are added later by data/grade5/2026-2/_gen_tts.py.
"""

VOCAB=[
    ("nice","すてきな","形容詞","This is a nice picture.","これはすてきな絵です。",["遅れた","申し訳なく思って","早い"],"大問1 Q1","nice"),
    ("garden","庭","名詞","We have flowers in our garden.","私たちの庭には花があります。",["飲み物","食べ物","料理人"],"大問1 Q2","garden"),
    ("practice","練習する","動詞","I practice the piano every day.","私は毎日ピアノを練習します。",["教える","忘れる","買う"],"大問1 Q3","practices"),
    ("hot","暑い・熱い","形容詞","It is hot today.","今日は暑いです。",["背が高い","親切な","甘い"],"大問1 Q4","hot"),
    ("daughter","娘","名詞","Mr. Brown has a daughter.","ブラウンさんには娘が1人います。",["息子","おじ","祖母"],"大問1 Q5","daughter"),
    ("zoo","動物園","名詞","There are many animals in the zoo.","動物園にはたくさんの動物がいます。",["レストラン","バス停","浴室"],"大問1 Q6","zoo"),
    ("second","2番目の","形容詞","My room is on the second floor.","私の部屋は2階にあります。",["怒った","若い","簡単な"],"大問1 Q7","second"),
    ("of course","もちろん","熟語","Of course, you can use my pen.","もちろん、私のペンを使っていいですよ。",["たぶん","ときどき","いつも"],"大問1 Q8","of course"),
    ("sit down","座る","熟語","Please sit down here.","ここに座ってください。",["立ち上がる","起きる","話す"],"大問1 Q9","sit down"),
    ("stand up","立ち上がる","熟語","Please stand up, everyone.","みなさん、立ってください。",["座る","寝る","見る"],"大問1 Q10","stand up"),
    ("over there","あそこに","熟語","My school is over there.","私の学校はあそこにあります。",["ここに","家に","中に"],"大問1 Q11","over there"),
    ("what time","何時","表現","What time do you get up?","あなたは何時に起きますか。",["何曜日","何月","どこで"],"大問1 Q12","what time"),
    ("lunch","昼食","名詞","We eat lunch at noon.","私たちは正午に昼食を食べます。",["朝食","夕食","おやつ"],"大問1 Q14","lunch"),
    ("How are you?","元気ですか。","表現","Hi, Ken. How are you?","やあ、ケン。元気ですか。",["何歳ですか。","どこにいますか。","だれですか。"],"大問1 Q15","How are you"),
    ("test","テスト","名詞","We have a math test today.","今日は数学のテストがあります。",["授業","休み","宿題"],"大問2 Q16","test"),
    ("every day","毎日","熟語","I read books every day.","私は毎日本を読みます。",["ときどき","毎週","一度も～ない"],"大問2 Q17","every day"),
    ("window","窓","名詞","Please close the window.","窓を閉めてください。",["ドア","机","いす"],"大問2 Q18","window"),
    ("start","始まる","動詞","The movie starts at seven.","その映画は7時に始まります。",["終わる","休む","帰る"],"大問2 Q19","start"),
    ("dance","踊る","動詞","Let's dance at the party.","パーティーで踊りましょう。",["歌う","泳ぐ","走る"],"大問3 Q22","dance"),
    ("how much","いくら","表現","How much is this cap?","この帽子はいくらですか。",["何時","いくつ","どのくらいの長さ"],"大問3 Q24","How much"),
]

def vocabulary():
    return [dict(word=word,meaning=meaning,pos=pos,level="5級",example=example,exampleJa=ja,
                 distractors=distractors,source=source,sourceForm=form) for word,meaning,pos,example,ja,distractors,source,form in VOCAB]

def lessonplan(sections):
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2026-2_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="手がかりの語とセット表現で選ぶ",subtitle="Clue Words & Set Phrases",color="#4f8cff",label="基本セット表現",
             explanation="大問1は空所の前後にある手がかりを探す。Q2 は a lot of snow から garden、Q4 は We need some drinks から hot、Q5 は They always eat dinner together から daughter。Q8 の of course、Q9 の sit down、Q10 の stand up、Q11 の over there、Q12 の what time はセット。Q13 は Does の質問に No で答えるので doesn't、Q14 は is＋～ing の現在進行形 eating、Q15 は I'm fine. に合う How。",
             simple="あなのまえとあとをよんで、ヒントをさがそう。『のみものがいる』なら hot（あつい）。Of course、sit down、stand up はセット。Does のしつもんに「いいえ」なら doesn't でこたえるよ。",
             source="大問1 Q4・Q13・Q14",quote="Julia, today is too hot. / No, she doesn't. / He is eating lunch.",
             examples=[(filled(4),"A：ジュリア、今日は暑すぎるね。\nB：そうね。飲み物が必要だわ。","We need some drinks（飲み物が必要）が理由になる。too hot は『暑すぎる』。","のみものがいるのは、あついからだね。"),
                       (filled(13),"A：エミリーはスキーが好きですか。\nB：いいえ、好きではありません。彼女は水泳が好きです。","Does で聞かれたら does を使って答える。No の答えは doesn't。主語が she なので don't にはしない。","Does のしつもんに No なら doesn't だよ。"),
                       (filled(14),"A：ジャック、お兄さん（弟さん）は今何をしていますか。\nB：昼食を食べています。","What is ... doing now? には is＋～ing（現在進行形）で答える。is の後ろは eating。","いましていることは is eating だね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [2,4,8,9,10,12]),
             passageJa="【Q2】雪がたくさん積もった庭を見て、外で遊ぼうと言う。\n【Q4】今日は暑すぎるので、飲み物が必要。\n【Q8】英語が好きかと聞かれ、もちろんと答える。\n【Q9】ウィリアムズさんがジェームズに座るように言う。\n【Q10】トムに、立ってこの質問に答えるように言う。\n【Q12】次の電車は何時かと聞き、午前10時30分に来ると答える。",
             patterns=["a lot of snow","too hot","of course","sit down","stand up","what time"],
             questions=[("Q5で daughter を選ぶ手がかりは？","They always eat dinner together（いつも一緒に夕食を食べる）。一緒に暮らして食事をするのは人なので daughter（娘）。"),
                        ("Q13で doesn't を選ぶ理由は？","質問が Does で始まり、主語が she だから。No, she doesn't. と答える。"),
                        ("Q15で How を選ぶ理由は？","返事が I'm fine（元気です）だから。How are you? は『元気ですか』と調子を聞く。")],
             easyQuestions=[("sit down はどんないみ？","すわる、だよ。"),("stand up はどんないみ？","たちあがる、だよ。"),("Of course. はどんないみ？","もちろん、だよ。")]),
        dict(title="会話は疑問詞と答えの組み合わせで選ぶ",subtitle="Question Words & Answers",color="#34d399",label="疑問詞と答え",
             explanation="大問2は質問の最初の語に注目する。Q16 の When（いつ）には Next Friday、Q19 の When does ... start? には At six o'clock、Q20 の Where（どこで）には In the park。Q17 は I like your pen. へのお礼の後に I use it every day.（it＝pen）。Q18 は Please open the window. という頼みに OK, Mom. と応じる。",
             simple="しつもんのさいしょのことばをみよう。When は『いつ』、Where は『どこ』。いつ？には Next Friday や At six o'clock、どこ？には In the park とこたえるよ。",
             source="大問2 Q16・Q19・Q20",quote="When is the test, Mr. Rogers? / When does the soccer game start, Nick? / Where do you play baseball?",
             examples=[(filled(16),"生徒：ロジャーズ先生、テストはいつですか。\n先生：次の金曜日です。午後2時に始まります。","When は『いつ』。日にちを答える Next Friday が合い、It starts at 2 p.m. と時刻が続く。","『いつ？』に『つぎのきんようび』とこたえるね。"),
                       (filled(19),"女性：ニック、サッカーの試合はいつ始まるの？\n男性：6時だよ。","When does ... start? は始まる時を尋ねる。At six o'clock と時刻で答える。At school は場所。","はじまるじかんだから At six o'clock だね。"),
                       (filled(20),"女の子：あなたはどこで野球をするの？\n男の子：公園でだよ。","Where は『どこで』。場所を答える In the park が合う。In the afternoon は時を表す。","『どこ？』だから、ばしょの In the park だよ。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】テストは次の金曜日で、午後2時に始まる。\n【Q17】ペンをほめられ、お礼を言って毎日使っていると答える。\n【Q18】母が窓を開けてと頼み、テッドはいいよと答える。\n【Q19】サッカーの試合が始まるのは6時。\n【Q20】野球をする場所は公園。",
             patterns=["Next Friday.","I use it every day.","OK, Mom.","At six o'clock.","In the park."],
             questions=[("Q19で In the office. が合わない理由は？","質問は When（いつ）で、始まる時を聞いている。In the office は場所を表す。"),
                        ("Q20で On Sunday morning. が合わない理由は？","質問は Where（どこで）なので場所を答える。On Sunday morning は時を表す。"),
                        ("Q17の it は何を指す？","your pen（相手がほめたペン）。I use it every day. で『毎日使っている』。")],
             easyQuestions=[("When はどんないみ？","いつ、だよ。"),("Where はどんないみ？","どこ、だよ。"),("OK, Mom. はどんなときにいう？","おかあさんのおねがいに『いいよ』とこたえるときだよ。")]),
        dict(title="並べ替え——主語と動詞から組み立てる",subtitle="Building Sentences from Subject & Verb",color="#a78bfa",label="整序の型",
             explanation="Q21 は which calendar（どちらのカレンダー）の後に do you want の疑問文。Q22 は My mother can't dance well（can't＋動詞の原形）。Q23 は That volleyball player is from Italy（be from＋国）。Q24 は How much is a movie ticket?（値段を聞く）。Q25 は I'm not using the computer（現在進行形の否定）。空所内の1番目と3番目を答え、固定の John, which・That・now. は数えない。",
             simple="まず『だれが』『どうする』をきめよう。can't のあとはもとの形の dance。How much は『いくら』。I'm not using は『つかっていない』だよ。さいしょからかいてあることばは、かぞえないよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="John, which calendar do you want? / That volleyball player is from Italy. / How much is a movie ticket?",
             examples=[(filled(22),"私の母はうまく踊ることができません。","can't の後ろは動詞の原形 dance。well は dance の後ろに置く。1番目④my mother、3番目③dance。","can't のあとは dance だね。"),
                       (filled(23),"あのバレーボール選手はイタリア出身です。","be from＋国で『～出身』。volleyball player がひとつのまとまり。1番目②volleyball、3番目①is。","That はかぞえず、volleyball が1ばんめだよ。"),
                       (filled(24),"映画の券はいくらですか。","How much is＋もの? で値段を聞く。1番目③how、3番目①is。","How much は『いくら』だよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】ジョン、どちらのカレンダーが欲しいですか。\n【Q22】私の母はうまく踊ることができない。\n【Q23】あのバレーボール選手はイタリア出身だ。\n【Q24】映画の券はいくらですか。\n【Q25】私は今、パソコンを使っていない。",
             patterns=["calendar do you want","can't dance well","is from Italy","How much is","not using"],
             questions=[("Q21の1番目と3番目は？","which の後に calendar→do→you→want と続くので、②calendar と③you。選択肢2。"),
                        ("Q24で is を how much の後に置くのはなぜ？","How much で始まる疑問文なので、次に be動詞 is、その後に主語 a movie ticket を置く。"),
                        ("Q25の1番目と3番目は？","I'm→not→using→the computer なので、③I'm と④using。選択肢3。")],
             easyQuestions=[("How much はどんないみ？","いくら、だよ。"),("can't のあとはどんなかたち？","dance のような、もとのかたちだよ。"),("どこをこたえる？","あいているところの1ばんめと3ばんめだよ。")]),
    ]
    points=[]
    for n,s in enumerate(specs,1):
        points.append(dict(id=f"fp{n}",title=s["title"],subtitle=s["subtitle"],explanation=s["explanation"],
                           explanationSimple=s["simple"],sourceQuote=s["quote"],sourceLocation=s["source"],
                           examples=[dict(en=en,ja=ja,note=note,noteSimple=easy) for en,ja,note,easy in s["examples"]],
                           practicePassage=dict(en=s["passage"],ja=s["passageJa"],source=s["source"]),
                           highlightPatterns=s["patterns"],highlightColor=s["color"],highlightLabel=s["label"],
                           practiceQuestions=[dict(q=q,a=a) for q,a in s["questions"]],
                           practiceQuestionsSimple=[dict(q=q,a=a) for q,a in s["easyQuestions"]]))
    return dict(title="英検5級 2026年度 第2回",focusPoints=points)
