"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("practice","練習する","動詞","My brother practices soccer every Sunday.","私の兄（弟）は毎週日曜日にサッカーを練習します。",["会う","閉める","飲む"],"大問1 Q1","practices"),
    ("letter","手紙","名詞","This letter is from my aunt.","この手紙はおばからです。",["切手","テーブル","ノート"],"大問1 Q2","letters"),
    ("box","箱","名詞","My cat likes this box.","私の猫はこの箱が好きです。",["スプーン","鳥","砂糖"],"大問1 Q3","box"),
    ("draw","（絵や図を）かく","動詞","My sister draws cats very well.","私の姉（妹）は猫の絵をとてもじょうずにかきます。",["料理する","聞く","食べる"],"大問1 Q4","draws"),
    ("violin","バイオリン","名詞","I play the violin on Sundays.","私は日曜日にバイオリンをひきます。",["ピアノ","フルート","ドラム"],"大問1 Q5","violin"),
    ("team","チーム","名詞","Our soccer team is very strong.","私たちのサッカーチームはとても強いです。",["台所","時計","帽子"],"大問1 Q6","team"),
    ("exciting","わくわくさせる・おもしろい","形容詞","This game is very exciting.","この試合はとてもわくわくします。",["つまらない","難しい","静かな"],"大問1 Q7","exciting"),
    ("have a good day","よい1日を","表現","Have a good day at school!","学校でよい1日を過ごしてね。",["おやすみなさい","はじめまして","ごめんなさい"],"大問1 Q8","Have a good day"),
    ("in the morning","朝に・午前中に","熟語","I drink milk in the morning.","私は朝に牛乳を飲みます。",["夜に","午後に","放課後に"],"大問1 Q9","in the morning"),
    ("at school","学校で","熟語","We eat lunch at school.","私たちは学校で昼食を食べます。",["家で","駅で","公園で"],"大問1 Q10","at school"),
    ("stand up","立ち上がる","熟語","Please stand up, everyone.","皆さん、立ってください。",["すわる","走る","待つ"],"大問1 Q11","stand up"),
    ("from","～から","前置詞","I swim from ten to eleven.","私は10時から11時まで泳ぎます。",["～まで","～の間","～の上に"],"大問1 Q12","from 7 p.m. to 9 p.m."),
    ("sometimes","ときどき","副詞","I sometimes eat lunch in the park.","私はときどき公園で昼食を食べます。",["いつも","たいてい","一度も～ない"],"大問1 Q13","sometimes"),
    ("speak","話す","動詞","My mother can speak French.","私の母はフランス語を話すことができます。",["書く","読む","聞く"],"大問1 Q14","speak"),
    ("when","いつ","疑問詞","When is your birthday?","あなたの誕生日はいつですか。",["どこ","だれ","何"],"大問1 Q15","When"),
    ("usually","ふだん・たいてい","副詞","I usually get up at six.","私はたいてい6時に起きます。",["ときどき","すぐに","ゆっくり"],"大問2 Q17","usually"),
    ("just","～だけ","副詞","I have just one pen.","私はペンを1本だけ持っています。",["もっと","たくさん","いつも"],"大問2 Q18","Just"),
    ("class","クラス","名詞","My class has thirty students.","私のクラスには30人の生徒がいます。",["学校","先生","宿題"],"大問2 Q19","class"),
    ("over there","あそこに","熟語","Look at that bird over there.","あそこにいるあの鳥を見て。",["ここに","家に","上に"],"大問3 Q21","over there"),
    ("whose","だれの","疑問詞","Whose pen is that?","あれはだれのペンですか。",["だれ","どこ","いつ"],"大問3 Q25","Whose"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2024-3_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="前の文の手がかりと「組み合わせ」で選ぶ",subtitle="Context Clues, Set Phrases & Word Forms",color="#4f8cff",label="手がかりと組み合わせ",
             explanation="大問1は、空所の前後や前の文に手がかりがある。Q1 は Tom likes music. と the guitar から practices、Q4 は Bob likes art. と pictures から draws、Q5 は loves music と the guitar から the violin を選ぶ。Q8 の Have a good day.、Q9 の in the morning、Q10 の at school、Q11 の stand up、Q12 の from ～ to … は語の組み合わせで覚える。Q13 は play を使う疑問文で主語が your father なので Does、Q14 は can の後ろなので原形 speak。意味の手がかりを見つけてから、語の形も確かめる。",
             simple="あきの まえと あとを よもう。『おんがくが すき』なら ギターを れんしゅうする、『びじゅつが すき』なら えを かく、だね。Have a good day.、in the morning、at school、stand up、from ～ to は セットで おぼえよう。can の あとは もとの かたちだよ。",
             source="大問1 Q1・Q4・Q8・Q12・Q14",quote="He practices the guitar every day. / He draws pictures every weekend. / Have a good day. / He studies it from 7 p.m. to 9 p.m. every day. / He can speak English very well.",
             examples=[(filled(1),"トムは音楽が好きです。彼は毎日ギターを練習します。","前の文の music と、後ろの the guitar が手がかり。practice は『練習する』。","おんがくが すきだから、ギターを れんしゅうするんだね。"),
                       (filled(12),"ケンは英語が好きです。彼は毎日、午後7時から午後9時まで英語を勉強します。","from A to B で『AからBまで』。p.m. は『午後』。","from ～ to … で『～から …まで』だね。"),
                       (filled(14),"カイトは英語が大好きです。彼は英語をとてもじょうずに話すことができます。","can の後ろは動詞の原形。主語が He でも speaks にはしない。","can の あとは もとの かたちの speak だよ。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [1,4,8,9,10,11,12,14]),
             passageJa="【Q1】トムは音楽が好きで、毎日ギターを練習する。\n【Q4】ボブは美術が好きで、毎週末に絵をかく。\n【Q8】学校に行くベンに、母が『よい1日を』と声をかける。\n【Q9】毎週末の朝にテニスをする。\n【Q10】ヨウコとケンジは学校で国語を勉強し、先生はナカムラ先生。\n【Q11】先生がケイトに、立って黒板のところまで来るよう言う。\n【Q12】ケンは毎日、午後7時から9時まで英語を勉強する。\n【Q14】カイトは英語をとてもじょうずに話せる。",
             patterns=["practices the guitar","draws pictures","Have a good day","in the morning","at school","stand up","from 7 p.m. to 9 p.m.","can speak"],
             questions=[("Q1で practices を選ぶ手がかりは？","前の文 Tom likes music.（トムは音楽が好き）と、後ろの the guitar。音楽好きのトムが毎日ギターを『練習する』。"),
                        ("Q12の from はどんな意味？","『～から』。from 7 p.m. to 9 p.m. で『午後7時から午後9時まで』と、時間の始まりと終わりを表す。"),
                        ("Q14で speaks ではなく speak を選ぶのはなぜ？","can の後ろの動詞は原形を使うから。主語が He でも can speak となる。")],
             easyQuestions=[("draw pictures は どんな いみ？","えを かく、だよ。"),("stand up は どんな いみ？","たちあがる、だよ。"),("in the morning は どんな いみ？","あさに、だよ。")]),
        dict(title="会話は「質問の形」に合う答えを選ぶ",subtitle="Dialogue Responses: Question Words & Short Answers",color="#34d399",label="会話の受け答え",
             explanation="大問2では、質問の始めの語を見て答え方を決める。Q16 の How are you today? は調子を尋ねるあいさつなので Good, thanks.。Q17 の Where（どこ）には場所を答える In the city pool.。Q18 の Do you want milk and sugar ～? には、入れるものを伝える Just milk, please.。Q19 の Is Ken ～? には Ken を he で受けて Yes, he is.、Q20 の Is this ～? には this を it で受けて No, it isn't が合う。Is ～? の質問に No, I don't. とは答えない。続くセリフ（I like him a lot. / It's John's.）も手がかりになる。",
             simple="しつもんの はじめの ことばを みよう。How are you? には『げんきです』、Where には ばしょ、Is ～? には is や isn't で こたえるよ。あとの セリフも ヒントだね。",
             source="大問2 Q16～Q20",quote="Good, thanks. / In the city pool. / Just milk, please. / Yes, he is. / No, it isn't, Ms. Brown.",
             examples=[(filled(17),"男の子：ヨウコ、あなたはふだんどこで泳ぎますか。\n女の子：市のプールでです。","Where（どこ）の質問に、泳ぐ場所を答えている。At night. は時の答え。","『どこ？』に、ばしょで こたえるね。"),
                       (filled(19),"女の子1：今年、ケンはあなたのクラスにいますか。\n女の子2：はい、います。私は彼のことがとても好きです。","Is Ken ～? には Ken を he で受けて Yes, he is.。him も Ken を指す。","Is で きかれたら is で こたえるよ。"),
                       (filled(20),"先生：ケン、これはあなたの帽子ですか。\n生徒：いいえ、ちがいます、ブラウン先生。ジョンのものです。","Is this ～? には it で答える。It's John's. から、自分の帽子ではないと分かる。","ジョンの ものだから、No だね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】先生に今日の調子を聞かれ、元気だと答える。\n【Q17】ヨウコはふだん、市のプールで泳ぐ。\n【Q18】コーヒーにはミルクだけを入れてほしいと答える。\n【Q19】ケンは今年同じクラスで、彼のことがとても好きだと話す。\n【Q20】帽子は自分のものではなく、ジョンのものだと先生に答える。",
             patterns=["Good, thanks","In the city pool","Just milk, please","Yes, he is","No, it isn't"],
             questions=[("Q17で At night. が合わないのはなぜ？","At night. は『夜に』と時を答える言い方。Where（どこ）は場所を尋ねているので、In the city pool. が合う。"),
                        ("Q19で No, I don't. が合わないのはなぜ？","質問が be動詞の Is で始まっているから。Is Ken ～? には Ken を he で受けて Yes, he is. と答える。No, I don't. は Do you ～? への答え方。"),
                        ("Q20で No, it isn't を選ぶ手がかりは？","続く It's John's.（ジョンのものです）。自分の帽子ではないので、Is this ～? に No, it isn't と答える。")],
             easyQuestions=[("How are you? には なんと こたえる？","Good, thanks.（げんきです、ありがとう）など だよ。"),("Where は どんな いみ？","どこ、だよ。"),("Just milk, please. は どんな いみ？","ミルクだけ ください、だよ。")]),
        dict(title="並べかえ——疑問詞・Let's・「～の…」のかたまりから組み立てる",subtitle="Word Order: Question Words, Let's & Noun Phrases",color="#a78bfa",label="整序の型",
             explanation="Q21 は Who are＋主語?（疑問詞のすぐ後ろに be動詞）、Q25 は Whose＋名詞（Whose baseball cap）をひとまとまりにして is this? へ続ける。Q23 は Let's＋動詞の原形で『～しましょう』。Q22 と Q24 は『主語→動詞→～を』の順で、Q22 は最後に before dinner（夕食前に）を置く。my homework・telephone number は1つのかたまりで、Mr. Tanner's の 's は『～の』。固定の I や文末の over there?・lunch.・this? は数えず、4つの空所の1番目と3番目を答える。完成文を確かめてから、2つの位置を選択肢と照合する。",
             simple="4つの ことばを ならべよう。『だれ？』は Who、『だれの～？』は Whose で はじめるよ。『～しましょう』は Let's の あとに make。my homework や telephone number は ひとつの かたまりだね。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Who are those boys over there? / Let's make spaghetti for lunch. / Whose baseball cap is this?",
             examples=[(filled(21),"あそこにいるあの男の子たちは誰ですか。","空所は who→are→those→boys。1番目④who、3番目②those。主語 those boys が複数なので are。","『だれ？』の Who から はじめるよ。"),
                       (filled(23),"昼食にスパゲッティを作りましょう。","let's→make→spaghetti→for。1番目③let's、3番目①spaghetti。Let's の後ろは動詞の原形 make。","Let's の あとは make だね。"),
                       (filled(25),"これはだれの野球帽ですか。","whose→baseball→cap→is。1番目③whose、3番目②cap。Whose baseball cap がひとまとまり。","Whose baseball cap で『だれの やきゅうぼう』だよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】あそこにいるあの男の子たちは誰ですか。\n【Q22】私は夕食前に宿題をします。\n【Q23】昼食にスパゲッティを作りましょう。\n【Q24】私はタナーさんの電話番号を知っています。\n【Q25】これはだれの野球帽ですか。",
             patterns=["Who are","do my homework","Let's make","know Mr. Tanner's","Whose baseball cap"],
             questions=[("Q21で is ではなく are を使うのはなぜ？","主語の those boys（あの男の子たち）が複数だから。who→are→those→boys で、1番目④who、3番目②those。選択肢2。"),
                        ("Q22の1番目と3番目は？","do→my homework→before→dinner なので、②do と③before。選択肢2。"),
                        ("Q25で baseball を cap の前に置くのはなぜ？","baseball cap で『野球帽』。cap の前に baseball を置いて、帽子の種類を表している。whose→baseball→cap→is で、1番目③whose、3番目②cap。選択肢2。")],
             easyQuestions=[("my homework は 2つに わける？","わけないよ。ひとつの かたまりだね。"),("『～しましょう』は なにで はじめる？","Let's で はじめるよ。"),("this? も かぞえる？","かぞえないよ。あいている 4つの ところだけだね。")]),
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
    return dict(title="英検5級 2024年度 第3回（土曜準会場）",focusPoints=points)
