"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("season","季節","名詞","Spring is my favorite season.","春は私のいちばん好きな季節です。",["月","天気","週末"],"大問1 Q1","season"),
    ("zoo","動物園","名詞","There are many animals at the zoo.","動物園にはたくさんの動物がいます。",["図書館","駅","公園"],"大問1 Q2","zoo"),
    ("see","見る・見える","動詞","I can see the moon tonight.","今夜は月が見えます。",["ほしい","踊る","遊ぶ"],"大問1 Q3","see"),
    ("fly","飛ぶ","動詞","That bird can fly high.","あの鳥は高く飛ぶことができます。",["泳ぐ","走る","料理する"],"大問1 Q4","flying"),
    ("early","早く","副詞","My father gets up early.","私の父は早く起きます。",["遅く","速く","高く"],"大問1 Q5","early"),
    ("black","黒","名詞","Black is my favorite color.","黒は私のいちばん好きな色です。",["白","青","赤"],"大問1 Q6","black"),
    ("walk","歩く","動詞","I walk to the park with my dog.","私は犬と公園まで歩いて行きます。",["走る","座る","泳ぐ"],"大問1 Q7","walk"),
    ("live","住む","動詞","My aunt lives in Osaka.","私のおばは大阪に住んでいます。",["立つ","知っている","働く"],"大問1 Q8","live"),
    ("how much","いくら","表現","How much is this cap?","この帽子はいくらですか。",["いくつ","何時","どのくらい長く"],"大問1 Q9","How much"),
    ("of course","もちろん","表現","Of course, you can come with us.","もちろん、あなたも私たちと一緒に来ていいですよ。",["ごめんなさい","はじめまして","おやすみなさい"],"大問1 Q10","Of course"),
    ("how long","どのくらい長く","表現","How long do you sleep every night?","あなたは毎晩どのくらい眠りますか。",["いくら","何歳","いつ"],"大問1 Q11","how long"),
    ("all right","分かりました・よろしい","表現","All right, let's go.","分かりました、行きましょう。",["ありがとう","ごめんなさい","さようなら"],"大問1 Q12","All right"),
    ("every day","毎日","熟語","I read a book every day.","私は毎日本を読みます。",["毎週","ときどき","週末に"],"大問1 Q13","every day"),
    ("birthday","誕生日","名詞","Today is my mother's birthday.","今日は私の母の誕生日です。",["週末","休み","祭り"],"大問1 Q14","birthday"),
    ("help","手伝う・助ける","動詞","I often help my mother in the kitchen.","私はよく台所で母を手伝います。",["教える","聞く","呼ぶ"],"大問1 Q15","help"),
    ("sport","スポーツ","名詞","Tennis is a fun sport.","テニスは楽しいスポーツです。",["楽器","教科","遊び"],"大問2 Q16","sports"),
    ("ready","準備ができた","形容詞","Are you ready for school?","学校へ行く準備はできていますか。",["忙しい","眠い","おなかがすいた"],"大問2 Q19","ready"),
    ("dictionary","辞書","名詞","I use a dictionary in English class.","私は英語の授業で辞書を使います。",["教科書","ノート","消しゴム"],"大問2 Q20","dictionary"),
    ("pencil case","筆箱","名詞","My pencil case is on the desk.","私の筆箱は机の上にあります。",["かばん","消しゴム","定規"],"大問3 Q21","pencil case"),
    ("cloudy","曇った","形容詞","It is cloudy in Tokyo now.","東京は今、曇っています。",["晴れた","雨の","雪の"],"大問3 Q22","cloudy"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2025-3_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="答えの形から「疑問詞」と「決まった言い方」を選ぶ",subtitle="Question Words, Answers & Set Phrases",color="#4f8cff",label="質問と答えのセット",
             explanation="大問1の Q9～Q15 は会話の問題。空所が A の質問にあるときは、B の答えから質問の形を決める。Q9 は 400 yen と値段を答えているので How much、Q11 は For two hours と時間の長さを答えているので How long、Q14 は It's April 5 と日付を答えているので When。Q13 の Do you ～? には Yes, I do.。Q10 の Of course.（もちろん）と Q12 の All right.（分かりました）は、返事の決まった言い方として覚える。Q15 は help の後ろなので『私を』の me。答えの中の手がかりを見つけてから、選択肢を確かめる。",
             simple="B のこたえをさきによもう。400えんなら How much、2じかんなら How long、4がつ5にちなら When だよ。Do you ～? には Yes, I do.。『もちろん』は Of course.、『わかりました』は All right. だね。",
             source="大問1 Q9・Q10・Q11・Q13・Q14",quote="How much are these apples? / Of course. / Yoko, how long do you study English every day? / Yes, I do. / When is your father's birthday, Tom?",
             examples=[(filled(9),"A：これらのリンゴはいくらですか。\nB：400円です。","How much で値段を尋ね、B が 400 yen と値段で答えている。","ねだんをきくときは How much だね。"),
                       (filled(11),"A：ヨウコ、あなたは毎日どのくらい長く英語を勉強しますか。\nB：2時間です。","How long で時間の長さを尋ね、For two hours（2時間）と答えている。","How long は『どのくらいながく』だね。"),
                       (filled(14),"A：トム、あなたのお父さんの誕生日はいつですか。\nB：4月5日です。","日付を答えているので、時を尋ねる When。father's の 's は『～の』。","『いつ？』は When だね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in range(9,16)),
             passageJa="【Q9】リンゴの値段を尋ね、400円だと答える。\n【Q10】消しゴムを使っていいかと聞かれ、もちろんと答える。\n【Q11】ヨウコは毎日2時間英語を勉強する。\n【Q12】問題に答えるよう言われ、分かりましたと答える。\n【Q13】ヒロコは毎日テニスをする。\n【Q14】トムのお父さんの誕生日は4月5日。\n【Q15】宿題がとても難しいので、お父さんに手伝ってほしいと頼む。",
             patterns=["How much","Of course","how long","All right","Yes, I do","When is","help me"],
             questions=[("Q9で How much を選ぶ手がかりは？","B の 400 yen.。値段を答えているので、値段を尋ねる How much。"),
                        ("Q13で does ではなく do を選ぶのはなぜ？","Do you ～? と聞かれ、答えの主語が I だから。I には does ではなく do を使い、Yes, I do. と答える。"),
                        ("Q15で I ではなく me を選ぶのはなぜ？","help の後ろで『私を』を表すので me。I は『私は』と主語に使う形。")],
             easyQuestions=[("『もちろん』はえいごで？","Of course. だよ。"),("How long はどんないみ？","どのくらいながく、だよ。"),("『いつ？』ときくことばは？","When だよ。")]),
        dict(title="会話は「聞かれたこと」と「前後のセリフ」をつなげて選ぶ",subtitle="Dialogue: Answers That Fit the Next Line",color="#34d399",label="会話のつながり",
             explanation="大問2では、何を聞かれたかと、空所の前後のセリフをつなげて考える。Q16 は空所の後の But I play the trumpet. につながる I don't play any sports.。Q17 は every day（毎日）の質問に No と答え、only on Sundays（日曜日だけ）と続ける。Q18 は What color の質問なので、色を答える She's white.。Q19 は後ろの Let's eat. から、夕食の準備ができたと伝える Dinner is ready,。Q20 は辞書をほめられて Thank you. と言った後、I often use it.（よく使います）と続ける。",
             simple="まえとあとのセリフをつなげよう。『でもトランペットはふく』のまえは『スポーツはしない』。『なにいろ？』には、いろでこたえる。『たべよう』のまえは『ごはんができたよ』だね。",
             source="大問2 Q16～Q20",quote="I don't play any sports. / only on Sundays. / She's white. / Dinner is ready, Sally. / I often use it.",
             examples=[(filled(16),"男の子1：私は野球をします。あなたはどうですか。\n男の子2：私はスポーツを何もしません。でも、私はトランペットを吹きます。","But（でも）の前後で、『スポーツはしない』と『トランペットは吹く』を対比している。","But は『でも』。スポーツはしないけど、トランペットはふくんだね。"),
                       (filled(17),"男の子：あなたは毎日コンピューターゲームをしますか。\n女の子：いいえ、日曜日だけです。","every day の質問に No と答え、only on Sundays でゲームをする日を伝えている。","only は『～だけ』。にちようびだけするんだね。"),
                       (filled(19),"祖母：夕食の準備ができましたよ、サリー。食べましょう。\n女の子：分かった、今行きます。","Dinner is ready（夕食の準備ができた）を受けて Let's eat.、I'm coming. と話が進む。","ready は『じゅんびができた』。I'm coming. は『いまいくよ』だね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】野球をする男の子に、もう1人の男の子はスポーツはしないが、トランペットを吹くと話す。\n【Q17】女の子はコンピューターゲームを毎日ではなく、日曜日だけする。\n【Q18】男の子のネコは白い。\n【Q19】祖母が夕食の準備ができたとサリーを呼び、サリーは今行くと答える。\n【Q20】辞書をほめられたマイクは、お礼を言い、よく使うと話す。",
             patterns=["I don't play any sports","only on Sundays","She's white","Dinner is ready","I often use it"],
             questions=[("Q16で Yes, I am. が合わないのはなぜ？","Yes, I am. は Are you ～? への答えだから。後ろに But I play the trumpet. と続くので、スポーツはしないと答える I don't play any sports. が合う。"),
                        ("Q17で I'm not. が合わないのはなぜ？","Do you ～? の質問には do を使って答えるから。I'm not. は Are you ～? への答え。"),
                        ("Q19で Dinner is ready, を選ぶ手がかりは？","後ろの Let's eat.（食べましょう）と、サリーの OK, I'm coming.（今行きます）。夕食に呼んでいる場面だと分かる。")],
             easyQuestions=[("I often use it. はどんないみ？","それをよくつかうよ、だよ。"),("only on Sundays はどんないみ？","にちようびだけ、だよ。"),("What color ときかれたら、なにでこたえる？","いろでこたえるよ。")]),
        dict(title="並べかえ——疑問文・否定文・場所の「型」から組み立てる",subtitle="Word Order: Questions, Negatives & Places",color="#a78bfa",label="整序の型",
             explanation="Q21 は Which is ～?（どちらが～ですか）で、which のすぐ後ろに is を置く。Q24 は Can＋主語＋動詞の原形 ～? で、can を主語 Emi の前に出す。Q22 は天気の it を主語にして、is の後ろに not を置く否定文。Q23 は be動詞＋on the wall で『壁にかかっている』という場所を表す。Q25 は『～には…がいる』を Keiko's class has ～ と has で表す。pencil case・come to は1つのかたまり。固定の Kate,・My picture や文末の語句は数えず、4つの空所の1番目と3番目を答える。",
             simple="『どちらが？』は Which ではじめて、すぐあとに is。『～できますか』は Can ではじめるよ。『くもっていない』は It is not cloudy。『かべに』は on the wall。Kate, や My picture はかぞえないよ。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="Kate, which is your pencil case? / It is not cloudy today. / Can Emi come to your birthday party?",
             examples=[(filled(21),"ケイト，どちらがあなたの筆箱ですか。","空所は which→is→your→pencil case。1番目③which、3番目④your。","Kate, はかぞえず、which が1ばんめだよ。"),
                       (filled(23),"私の絵はその壁にかかっています。","is→on→the→wall。1番目④is、3番目③the。My picture は固定部分。","My picture はかぞえないよ。is が1ばんめだね。"),
                       (filled(25),"恵子のクラスには生徒が20人います。","Keiko's→class→has→twenty。1番目②Keiko's、3番目④has。主語 Keiko's class は3人称単数なので has。","クラスがせいとを『もっている』とかんがえて has をつかうよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】ケイト，どちらがあなたの筆箱ですか。\n【Q22】今日は曇っていません。\n【Q23】私の絵はその壁にかかっています。\n【Q24】エミは，あなたの誕生パーティーに来ることができますか。\n【Q25】恵子のクラスには生徒が20人います。",
             patterns=["which is","It is not","is on the wall","Can Emi","has twenty"],
             questions=[("Q21の1番目は Kate, ではないの？","Kate, は固定の呼びかけ。空所だけを数え、which が1番目、your が3番目。選択肢1。"),
                        ("Q22で not はどこに置く？","be動詞 is の後ろ。It is not cloudy today. で、1番目①it、3番目④not。選択肢3。"),
                        ("Q24で can を Emi の前に置くのはなぜ？","『～できますか』と尋ねる疑問文だから。Can Emi come to ～? の順で、1番目③can、3番目①come to。選択肢3。")],
             easyQuestions=[("pencil case は2つにわける？","わけないよ。ひとつのかたまりだね。"),("『～できますか』はなにではじめる？","Can ではじめるよ。"),("My picture もかぞえる？","かぞえないよ。あいている4つのところだけだね。")]),
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
    return dict(title="英検5級 2025年度 第3回（土曜準会場）",focusPoints=points)
