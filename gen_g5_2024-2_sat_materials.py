"""Existing Grade 5 format: 20 vocabulary items and three bilingual focus points."""
import re

VOCAB=[
    ("notebook","ノート","名詞","I write new words in my notebook.","私は新しい単語をノートに書きます。",["花","かばん","カメラ"],"大問1 Q1","notebook"),
    ("know","知っている","動詞","I know that girl. She is my classmate.","私はあの女の子を知っています。彼女は私のクラスメートです。",["すわる","住む","始める"],"大問1 Q2","know"),
    ("locker","ロッカー","名詞","My locker is in the classroom.","私のロッカーは教室にあります。",["自転車","机","箱"],"大問1 Q3","locker"),
    ("money","お金","名詞","I put my money in my bag.","私はお金をかばんに入れます。",["紙","魚","音楽"],"大問1 Q4","money"),
    ("homework","宿題","名詞","I do my homework after dinner.","私は夕食のあとに宿題をします。",["机","電車","果物"],"大問1 Q5","homework"),
    ("kitchen","台所","名詞","My mother is cooking in the kitchen.","母は台所で料理をしています。",["ソファー","床","寝室"],"大問1 Q6","kitchen"),
    ("write","書く","動詞","My sister writes a letter to Grandma every month.","私の姉（妹）は毎月おばあちゃんに手紙を書きます。",["見る","洗う","食べる"],"大問1 Q7","writing"),
    ("how much","いくら","表現","How much is this cake?","このケーキはいくらですか。",["いくつ","何歳","どれくらい長い"],"大問1 Q8","How much"),
    ("cup","カップ","名詞","My father drinks a cup of tea every morning.","父は毎朝お茶を1杯飲みます。",["チーム","名前","フォーク"],"大問1 Q9","cup"),
    ("take a bath","お風呂に入る","熟語","I take a bath at nine.","私は9時にお風呂に入ります。",["歯をみがく","顔を洗う","寝る"],"大問1 Q10","takes a bath"),
    ("look at","～を見る","熟語","Look at that big dog!","あの大きな犬を見て！",["～を聞く","～を待つ","～をさがす"],"大問1 Q11","Look at"),
    ("that's right","そのとおり","表現","That's right. I'm from Canada.","そのとおりです。私はカナダの出身です。",["ごめんなさい","どういたしまして","はじめまして"],"大問1 Q12","That's right"),
    ("weekend","週末","名詞","We go to the park on weekends.","私たちは週末に公園に行きます。",["平日","夏休み","誕生日"],"大問1 Q13","weekends"),
    ("when","いつ","疑問詞","When do you play soccer?","あなたはいつサッカーをしますか。",["どこ","だれ","どれ"],"大問1 Q14","When"),
    ("careful","注意深い・気をつける","形容詞","Be careful! That cup is hot.","気をつけて！そのカップは熱いよ。",["うれしい","ねむい","静かな"],"大問1 Q15","careful"),
    ("how long","どれくらい（の長さ）","表現","How long is the movie?","その映画はどれくらいの長さですか。",["いくら","何歳","いくつ"],"大問2 Q16","How long"),
    ("lesson","レッスン・授業","名詞","I have a piano lesson on Fridays.","私は金曜日にピアノのレッスンがあります。",["試合","宿題","休み"],"大問2 Q17","lessons"),
    ("tomorrow","明日","副詞","I have a soccer game tomorrow.","私は明日サッカーの試合があります。",["昨日","今日","毎日"],"大問2 Q18","tomorrow"),
    ("color","色","名詞","What color is your bag?","あなたのかばんは何色ですか。",["形","大きさ","名前"],"大問3 Q21","color"),
    ("walk to school","歩いて学校へ行く","熟語","My sister walks to school with her friends.","私の姉（妹）は友達と歩いて学校へ行きます。",["バスで学校へ行く","学校で走る","家に帰る"],"大問3 Q25","walk to school"),
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
    spec=importlib.util.spec_from_file_location("order",Path(__file__).with_name("gen_g5_2024-2_sat_order.py"))
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    qs=[q for s in sections for q in s["questions"]]
    def filled(n):
        q=qs[n-1]
        return o.completed(q) if "words" in q else q["text"].replace("(　)",q["choices"][q["answer"]-1])
    specs=[
        dict(title="相手の答えと前後の語を手がかりに選ぶ",subtitle="Context Clues, Set Phrases & Word Forms",color="#4f8cff",label="手がかりと組み合わせ",
             explanation="大問1は、空所の前後や相手の答えに手がかりがある。Q1 は I'm drawing a picture in it now. から notebook、Q3 は I keep my coat and books in it. から locker、Q4 は I want some ice cream. から money を選ぶ（in it の it は空所の物を指す）。Q9 の a cup of、Q10 の take a bath、Q11 の look at、Q12 の That's right. は語の組み合わせで覚える。Q13 は with の後ろなので目的格の them、Q15 は Please の後ろなので原形の be。意味の手がかりを見つけてから、語の形も確かめる。",
             simple="あきの まえと あとを よもう。『その なかに えを かいている』なら ノート、『コートと ほんを いれている』なら ロッカーだね。a cup of、take a bath、look at、That's right. は セットで おぼえよう。with の あとは them の ような かたち（ここでは them）、Please の あとは もとの かたち（ここでは be）だよ。",
             source="大問1 Q1・Q3・Q4・Q9・Q10・Q11・Q13・Q15",quote="Ben, can I use your notebook? / I keep my coat and books in it. / Yuko takes a bath every night before bedtime. / Jane sometimes goes to the pool with them on weekends. / Please be careful.",
             examples=[(filled(3),"A：カレン、あなたは学校にロッカーがありますか。\nB：はい。その中にコートと本を入れています。","B の I keep my coat and books in it. が手がかり。it は locker を指す。","コートと ほんを いれておく ものだから ロッカーだね。"),
                       (filled(10),"ユウコは毎晩、寝る前にお風呂に入ります。","take a bath で『お風呂に入る』。主語が Yuko なので takes。","take a bath で『おふろに はいる』だよ。"),
                       (filled(13),"ジェーンの兄弟たちは水泳が好きです。ジェーンは週末にときどき彼らといっしょにプールに行きます。","with の後ろは目的格の them。them は Jane's brothers を指す。","with の あとは them。ジェーンの きょうだいたちの ことだね。")],
             passage="\n\n".join(f"[出典: 大問1 Q{n}]\n"+filled(n) for n in [1,3,4,9,10,11,13,15]),
             passageJa="【Q1】ベンは今ノートに絵をかいているので、貸せないと答える。\n【Q3】カレンは学校のロッカーにコートと本を入れている。\n【Q4】アイスクリームがほしいケビンが、お母さんにお金を持っているか尋ねる。\n【Q9】店でクッキーとコーヒー1杯を注文する。\n【Q10】ユウコは毎晩、寝る前にお風呂に入る。\n【Q11】テレビで踊っているロボットを見るように言う。\n【Q13】ジェーンは週末にときどき兄弟たちとプールに行く。\n【Q15】自転車で公園に行くケリーに、母が気をつけるように言う。",
             patterns=["drawing a picture in it","keep my coat and books in it","want some ice cream","a cup of coffee","takes a bath","Look at","with them","Please be careful"],
             questions=[("Q1で notebook を選ぶ手がかりは？","B の I'm drawing a picture in it now.（今それに絵をかいているところ）。中に絵をかける物なので notebook（ノート）。"),
                        ("Q13で they ではなく them を選ぶのはなぜ？","with（～といっしょに）の後ろには目的格を置くから。them は Jane's brothers（ジェーンの兄弟たち）を指す。"),
                        ("Q15で is ではなく be を選ぶのはなぜ？","Please＋動詞の原形で『～してください』となるから。careful（注意深い）は形容詞なので、be動詞の原形 be を使って Please be careful. とする。")],
             easyQuestions=[("take a bath は どんな いみ？","おふろに はいる、だよ。"),("look at ～ は どんな いみ？","～を みる、だよ。"),("a cup of coffee は どんな いみ？","コーヒー いっぱい、だよ。")]),
        dict(title="会話は「疑問詞」と空所の前後のセリフで答えを決める",subtitle="Dialogue Responses: How long / Where & Do-Questions",color="#34d399",label="会話の受け答え",
             explanation="大問2では、質問の始めの語と、空所の前後のセリフを手がかりにする。Q16 の How long is ～?（どれくらいの長さ）には長さの 400 meters.、Q20 の Where（どこ）には場所の In the park. が合う（In the afternoon. や On Sunday morning. は時の答え）。Q19 は女性の答え Mexico.（国名）から、空所に Where are you from? を入れる。Q18 の Do you have ～? には Yes, I do.。Q17 は、空所の後ろの They're fun. の They が guitar lessons を指すので、I go to guitar lessons. を選ぶ。",
             simple="しつもんの はじめの ことばを みよう。How long には ながさ、Where には ばしょ、Do you ～? には Yes, I do. か No, I don't. で こたえるよ。くうしょの あとの セリフも ヒントだね。",
             source="大問2 Q16～Q20",quote="400 meters. / I go to guitar lessons. / Yes, I do. / Where are you from? / In the park.",
             examples=[(filled(16),"生徒：ワトソン先生、この橋はどれくらいの長さですか。\n先生：400メートルです。","How long is ～? は長さを尋ねる言い方。長さを数字と単位で答えている。","『どのくらい ながい？』に『400メートル』と こたえているね。"),
                       (filled(19),"男性：私は日本の出身です。あなたはどこの出身ですか。\n女性：メキシコです。","答えの Mexico.（国名）から、出身地を尋ねる Where are you from? を選ぶ。","くにの なまえで こたえているから『どこの しゅっしん？』だね。"),
                       (filled(20),"女の子：あなたはどこで野球をしますか。\n男の子：公園でです。","Where（どこ）には場所で答える。In the afternoon. や On Sunday morning. は時の答え。","『どこ？』に ばしょで こたえるね。")],
             passage="\n\n".join(f"[出典: 大問2 Q{n}]\n"+filled(n) for n in range(16,21)),
             passageJa="【Q16】ワトソン先生が、橋の長さは400メートルだと答える。\n【Q17】キャロルはギターのレッスンに通っていて、楽しいと話す。\n【Q18】ルークは明日の午前中に英語のテストがある。\n【Q19】日本出身の男性が出身地を尋ね、女性はメキシコと答える。\n【Q20】男の子は公園で野球をする。",
             patterns=["400 meters","I go to guitar lessons","Yes, I do","Where are you from","In the park"],
             questions=[("Q16で In the morning. が合わないのはなぜ？","In the morning. は『午前中に』と時を答える言い方。How long is this bridge? は橋の長さを尋ねているので、400 meters. が合う。"),
                        ("Q17の They're fun. の They は何を指す？","guitar lessons（ギターのレッスン）。lessons が複数なので They で受けている。だから空所には I go to guitar lessons. が入る。"),
                        ("Q18で Yes, you are. が合わないのはなぜ？","質問が Do you have ～? と do で始まっているから。you と聞かれたら I で答え、Yes, I do. とする。Yes, you are. は Am I ～? のような be動詞の質問への答え方。")],
             easyQuestions=[("How long は どんな いみ？","どのくらい ながい、だよ。"),("Where are you from? は どんな いみ？","どこの しゅっしんですか、だよ。"),("Do you ～? には なんと こたえる？","Yes, I do. か No, I don't. だよ。")]),
        dict(title="並べかえ——疑問詞・命令文・否定文の語順で組み立てる",subtitle="Word Order: What color, Don't / Let's & Negatives",color="#a78bfa",label="整序の型",
             explanation="Q21 は What color（何色）をひとまとまりにして、do you like と疑問文の語順を続ける。Q22 は Kate is の後ろに my sister's friend（私の姉の友達）を置き、's は『～の』。Q23 は Don't＋動詞の原形で『～してはいけません』、Q24 は Let's＋動詞の原形で『～しましょう』と go camping on Saturday を続ける。Q25 は 主語 I＋don't＋動詞の原形 walk の否定文。the chair は1つのかたまりで、固定の What や Let's、文末の , Nancy?・friend.・school. は数えず、4つの空所の1番目と3番目を答える。完成文を確かめてから、2つの位置を選択肢と照合する。",
             simple="4つの ことばを ならべよう。『なにいろ？』は What color、『～しては いけません』は Don't、『～しましょう』は Let's で はじめるよ。『わたしは ～しません』は I don't の あとに うごきの ことばだね。",
             source="大問3 Q21～Q25（並べ替え後の完成文）",quote="What color do you like, Nancy? / Don't stand on the chair. / I don't walk to school.",
             examples=[(filled(21),"ナンシーさん，あなたは何色が好きですか。","空所は color→do→you→like。1番目③color、3番目④you。What color で『何色』。","『なにいろ？』は What color で はじめるよ。"),
                       (filled(23),"椅子の上に立ってはいけません。","don't→stand→on→the chair。1番目③don't、3番目④on。Don't＋動詞の原形で『～してはいけません』。","Don't の あとは stand だね。"),
                       (filled(25),"私は学校へ歩いて行きません。","I→don't→walk→to。1番目④I、3番目③walk。don't の後ろは動詞の原形 walk。","I don't の あとに walk だよ。")],
             passage="\n\n".join(f"[出典: 大問3 Q{n} 完成文]\n"+filled(n) for n in range(21,26)),
             passageJa="【Q21】ナンシーさん，あなたは何色が好きですか。\n【Q22】ケイトは私の姉の友達です。\n【Q23】椅子の上に立ってはいけません。\n【Q24】土曜日にキャンプに行きましょう。\n【Q25】私は学校へ歩いて行きません。",
             patterns=["What color","my sister's friend","Don't stand","Let's go camping","don't walk"],
             questions=[("Q21の1番目と3番目は？","color→do→you→like なので、③color と④you。選択肢2。What color で『何色』。"),
                        ("Q24で go の後ろに camping を置くのはなぜ？","go camping で『キャンプに行く』というまとまりだから。固定の Let's の後ろが go→camping→on→Saturday で、1番目①go、3番目②on。選択肢3。"),
                        ("Q25で don't の後ろに walk を置くのはなぜ？","主語が I の一般動詞の否定文は 主語＋don't＋動詞の原形 だから。I→don't→walk→to で、1番目④I、3番目③walk。選択肢2。")],
             easyQuestions=[("『なにいろ？』は なにで はじめる？","What color で はじめるよ。"),("『～しては いけません』は なにで はじめる？","Don't で はじめるよ。"),("school. も かぞえる？","かぞえないよ。あいている 4つの ところだけだね。")]),
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
    return dict(title="英検5級 2024年度 第2回（土曜準会場）",focusPoints=points)
