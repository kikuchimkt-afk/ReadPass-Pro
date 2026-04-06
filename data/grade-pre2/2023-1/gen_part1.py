"""準2級 2023-1 data.json 一括生成 Part 1: 基本構造 + 大問1 + 大問2"""
import json, os

data = {
    "grade": "grade-pre2",
    "year": "2023",
    "session": "1",
    "title": "2023年度 第1回 英検準2級 リーディング",
    "sections": [],
    "vocabulary": [],
    "lessonPlan": {"focusPoints": []}
}

# ===== 大問1: 語彙・文法 (20問) =====
sec1 = {
    "name": "大問1", "type": "vocabulary",
    "instruction": "次の(1)から(20)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "questions": [
        {"number":1,"text":"The teacher ( ) his notes from the blackboard before Ruth was able to finish copying them into her notebook. She had to ask another student for help.","choices":["erased","excused","escaped","extended"],"answer":1,"translation":"先生はルースがノートに写し終る前に黒板のメモを消してしまった。彼女は別の生徒に助けを求めなければならなかった。",
         "choiceAnalysis":{"1":"erased（消した）が正解。黒板のメモを消すという文脈に合う。","2":"excused（許した）は文脈に合わない。","3":"escaped（逃げた）は意味が異なる。","4":"extended（延長した）は文脈に合わない。"},
         "grammar":{"point":"erase は「消す」の意味の他動詞","detail":"erase は黒板やデータなどを「消す」という意味。過去形は erased。"}},
        {"number":2,"text":"A : Why did you cancel the picnic? I was looking forward to it.\nB : So was I, but it's going to rain. We have no ( ) over the weather.","choices":["issue","grade","fever","control"],"answer":4,"translation":"A：なぜピクニックをキャンセルしたの？楽しみにしていたのに。\nB：私もだよ、でも雨が降りそうなんだ。天気はどうにもならないからね。",
         "choiceAnalysis":{"1":"issue（問題）は have no control の文脈に合わない。","2":"grade（成績）は無関係。","3":"fever（熱）は無関係。","4":"control（支配・制御）が正解。have no control over ～ で「～をどうにもできない」。"},
         "grammar":{"point":"have no control over ～","detail":"「～をコントロールできない」という意味の重要表現。"}},
        {"number":3,"text":"A : It's really cold this winter, isn't it?\nB : I know! I have four ( ) on my bed, and I am still cold at night.","choices":["locks","blankets","moments","husbands"],"answer":2,"translation":"A：今年の冬は本当に寒いね。\nB：そうだよね！ベッドに毛布を4枚かけているけど、夜はまだ寒いんだ。",
         "choiceAnalysis":{"1":"locks（錠前）は文脈に合わない。","2":"blankets（毛布）が正解。ベッドにかけるもの。","3":"moments（瞬間）は意味が異なる。","4":"husbands（夫）は意味が異なる。"},
         "grammar":{"point":"blanket は「毛布」","detail":"ベッドの上にかけるものとして自然な名詞。"}},
        {"number":4,"text":"The new TV show Amazing Plants is very ( ). Children who watch it can learn about lots of strange plants.","choices":["modern","lonely","violent","educational"],"answer":4,"translation":"新しいテレビ番組「Amazing Plants」はとても教育的だ。見た子供たちは多くの珍しい植物について学べる。",
         "choiceAnalysis":{"1":"modern（現代的な）は文脈に合わない。","2":"lonely（孤独な）は無関係。","3":"violent（暴力的な）は子供が学べる内容に不適切。","4":"educational（教育的な）が正解。learn about に対応。"},
         "grammar":{"point":"educational（教育的な）","detail":"educate（教育する）の形容詞形。-al がつく。"}},
        {"number":5,"text":"Mr. Suzuki's vacation in Hawaii was like a wonderful dream. However, he knew that he would have to go back to the ( ) of his job in Tokyo.","choices":["origin","suggestion","reality","coast"],"answer":3,"translation":"鈴木さんのハワイでの休暇は素晴らしい夢のようだった。しかし、東京での仕事という現実に戻らなければならないことは分かっていた。",
         "choiceAnalysis":{"1":"origin（起源）は文脈に合わない。","2":"suggestion（提案）は無関係。","3":"reality（現実）が正解。dreamとの対比。","4":"coast（海岸）は文脈に合わない。"},
         "grammar":{"point":"dream vs reality の対比","detail":"「夢のような休暇」と「仕事の現実」という対比構造。"}},
        {"number":6,"text":"Wesley offered to buy Sarah's guitar from her, but she ( ). She did not want to sell it because it was a gift from her father.","choices":["employed","existed","retired","refused"],"answer":4,"translation":"ウェスリーはサラのギターを買いたいと申し出たが、彼女は断った。父からの贈り物だったので売りたくなかったのだ。",
         "choiceAnalysis":{"1":"employed（雇った）は文脈に合わない。","2":"existed（存在した）は無関係。","3":"retired（引退した）は無関係。","4":"refused（断った）が正解。butの逆接と合致。"},
         "grammar":{"point":"refuse は「断る」","detail":"offer（申し出る）に対して refuse（断る）という対比。"}},
        {"number":7,"text":"Andrew looks forward to visiting his grandparents on the weekend because he always has interesting ( ) with them. They always talk about history.","choices":["consumers","approaches","muscles","discussions"],"answer":4,"translation":"アンドリューは週末に祖父母を訪ねるのを楽しみにしている。いつも面白い話し合いができるからだ。いつも歴史について話している。",
         "choiceAnalysis":{"1":"consumers（消費者）は無関係。","2":"approaches（アプローチ）は文脈に合わない。","3":"muscles（筋肉）は無関係。","4":"discussions（議論・話し合い）が正解。talk about に対応。"},
         "grammar":{"point":"have discussions with ～","detail":"「～と議論する」という意味の表現。"}},
        {"number":8,"text":"Simon's homework is to write about someone who he ( ). Simon has decided to write about his favorite baseball player because he is Simon's hero.","choices":["respects","locates","assists","combines"],"answer":1,"translation":"サイモンの宿題は、尊敬する人について書くことだ。サイモンは大好きな野球選手について書くことにした。その選手はサイモンのヒーローだからだ。",
         "choiceAnalysis":{"1":"respects（尊敬する）が正解。heroに対応。","2":"locates（場所を突き止める）は無関係。","3":"assists（手伝う）は文脈に合わない。","4":"combines（結合する）は無関係。"},
         "grammar":{"point":"respect は「尊敬する」","detail":"someone who he respects で「彼が尊敬する人」。関係代名詞の目的格。"}},
        {"number":9,"text":"When Dennis arrived at his aunt's house, she ( ) him at the door with a hug.","choices":["greeted","promised","required","interviewed"],"answer":1,"translation":"デニスが叔母の家に着くと、彼女はドアのところで抱擁して迎えてくれた。",
         "choiceAnalysis":{"1":"greeted（迎えた）が正解。with a hugと合致。","2":"promised（約束した）は文脈に合わない。","3":"required（要求した）は文脈に合わない。","4":"interviewed（面接した）は文脈に合わない。"},
         "grammar":{"point":"greet ～ with a hug","detail":"「抱擁で迎える」。greet は「挨拶する・迎える」。"}},
        {"number":10,"text":"A : I think you're sitting in the seat that I reserved.\nB : Oh! I'm ( ) sorry. I'll find somewhere else to sit.","choices":["equally","terribly","calmly","safely"],"answer":2,"translation":"A：私が予約した席に座っていると思うのですが。\nB：ああ！本当に申し訳ありません。別の場所を探します。",
         "choiceAnalysis":{"1":"equally（等しく）は sorry の強調に不適切。","2":"terribly（ひどく）が正解。terribly sorry で「本当に申し訳ない」。","3":"calmly（穏やかに）は sorry の修飾に不適切。","4":"safely（安全に）は無関係。"},
         "grammar":{"point":"terribly sorry","detail":"terribly は副詞で「非常に」の意味。sorry を強調する定番表現。"}},
        {"number":11,"text":"Casey and his sister ( ) washing the dishes. He washes them after breakfast and she washes them after dinner.","choices":["take turns","give applause","pass around","have faith"],"answer":1,"translation":"ケイシーと姉は交代で皿洗いをしている。彼は朝食後に、姉は夕食後に洗う。",
         "choiceAnalysis":{"1":"take turns（交代でする）が正解。交互に担当する文脈に合致。","2":"give applause（拍手する）は無関係。","3":"pass around（回す）は文脈に合わない。","4":"have faith（信頼する）は無関係。"},
         "grammar":{"point":"take turns ～ing","detail":"「交代で～する」という意味の重要熟語。"}},
        {"number":12,"text":"Alan went to Hawaii last week, but he could not enjoy any of the beaches because he was there ( ).","choices":["at least","by heart","for good","on business"],"answer":4,"translation":"アランは先週ハワイに行ったが、出張だったのでビーチを楽しめなかった。",
         "choiceAnalysis":{"1":"at least（少なくとも）は文脈に合わない。","2":"by heart（暗記して）は無関係。","3":"for good（永久に）は文脈に合わない。","4":"on business（出張で）が正解。ビーチを楽しめない理由として適切。"},
         "grammar":{"point":"on business（出張で）","detail":"for business とも言うが、on business が定型表現。"}},
        {"number":13,"text":"After work on Friday night, Jason did not want to cook at home. He ( ) having dinner with his friends, so he invited three of them to a restaurant.","choices":["looked like","felt like","passed by","ran by"],"answer":2,"translation":"金曜日の夜、仕事の後、ジェイソンは家で料理したくなかった。友達と夕食を食べたい気分だったので、3人をレストランに誘った。",
         "choiceAnalysis":{"1":"looked like（～のように見えた）は文脈に合わない。","2":"felt like（～したい気分だった）が正解。feel like ～ing で「～したい気分」。","3":"passed by（通り過ぎた）は無関係。","4":"ran by（走り過ぎた）は無関係。"},
         "grammar":{"point":"feel like ～ing","detail":"「～したい気分だ」という意味の重要表現。"}},
        {"number":14,"text":"A : Gina, could I go to one of your photography club meetings and see what it's like?\nB : Sure. Our meetings ( ) on the first Saturday of each month.","choices":["take place","grow up","come true","put off"],"answer":1,"translation":"A：ジーナ、写真部のミーティングに一度行ってみてもいい？\nB：もちろん。ミーティングは毎月第1土曜日に行われるよ。",
         "choiceAnalysis":{"1":"take place（行われる）が正解。会議の開催を表す。","2":"grow up（成長する）は無関係。","3":"come true（実現する）は文脈に合わない。","4":"put off（延期する）は文脈に合わない。"},
         "grammar":{"point":"take place（行われる）","detail":"イベントや会議が「開催される」という意味の重要熟語。"}},
        {"number":15,"text":"After Suzanne graduated from college, she did not plan to ( ) her parents. She got a job so she could live by herself.","choices":["lay out","rely on","turn in","get over"],"answer":2,"translation":"スザンヌは大学卒業後、両親に頼るつもりはなかった。一人で暮らせるように仕事を見つけた。",
         "choiceAnalysis":{"1":"lay out（並べる）は文脈に合わない。","2":"rely on（頼る）が正解。live by herself と対比。","3":"turn in（提出する）は無関係。","4":"get over（乗り越える）は文脈に合わない。"},
         "grammar":{"point":"rely on ～（～に頼る）","detail":"depend on と同義の重要熟語。"}},
        {"number":16,"text":"A : What are you going to wear at the Christmas party?\nB : I'm going to ( ) as a snowman. My mom is helping me to make my costume.","choices":["turn off","hold back","dress up","break out"],"answer":3,"translation":"A：クリスマスパーティーで何を着るの？\nB：雪だるまの仮装をするつもり。お母さんが衣装を作るのを手伝ってくれている。",
         "choiceAnalysis":{"1":"turn off（消す）は無関係。","2":"hold back（抑える）は文脈に合わない。","3":"dress up（仮装する）が正解。as a snowman / costume に対応。","4":"break out（勃発する）は無関係。"},
         "grammar":{"point":"dress up as ～","detail":"「～に仮装する」という意味。costume（衣装）と一緒に使われる。"}},
        {"number":17,"text":"Dan gave a presentation in his science class today. He ( ) his main ideas with data from research.","choices":["pulled away","called out","wished for","backed up"],"answer":4,"translation":"ダンは今日、理科の授業でプレゼンテーションをした。研究のデータで自分の主な考えを裏付けた。",
         "choiceAnalysis":{"1":"pulled away（引き離した）は文脈に合わない。","2":"called out（叫んだ）は無関係。","3":"wished for（～を望んだ）は文脈に合わない。","4":"backed up（裏付けた）が正解。data from research に対応。"},
         "grammar":{"point":"back up（裏付ける・支持する）","detail":"主張やアイデアをデータや証拠で「裏付ける」という意味。"}},
        {"number":18,"text":"Mike cried when he broke the toy truck that his mother ( ) him for his birthday.","choices":["has given","was giving","was given","had given"],"answer":4,"translation":"マイクは、誕生日に母親がくれたおもちゃのトラックを壊した時に泣いた。",
         "choiceAnalysis":{"1":"has given は時制が合わない。","2":"was giving は進行形で不適切。","3":"was given は受動態で主語が合わない。","4":"had given（あげていた）が正解。壊す前にもらっていたので過去完了。"},
         "grammar":{"point":"過去完了形（had + 過去分詞）","detail":"「壊した」時点より前に「もらった」ので、過去完了形を使う。大過去。"}},
        {"number":19,"text":"Bobby wanted to play catch, so he asked his parents, his brother, and his sister if they had time to play with him. However, ( ) did because they were all too busy.","choices":["nobody","everybody","anybody","somebody"],"answer":1,"translation":"ボビーはキャッチボールがしたかったので、両親、兄、姉に一緒に遊ぶ時間があるか聞いた。しかし、全員忙しかったので誰もできなかった。",
         "choiceAnalysis":{"1":"nobody（誰も～ない）が正解。Howeverの逆接と「全員忙しい」に合致。","2":"everybody（みんな）は逆接に合わない。","3":"anybody（誰か）は肯定文では不適切。","4":"somebody（誰か）は文脈に合わない。"},
         "grammar":{"point":"nobody + 肯定動詞","detail":"nobody did = 誰もしなかった。否定の代名詞で肯定形の動詞と使う。"}},
        {"number":20,"text":"On Saturdays, Beth volunteers at her local community center. She enjoys ( ) with events for the people in her area.","choices":["to help","helps","helping","helped"],"answer":3,"translation":"土曜日、ベスは地元のコミュニティセンターでボランティアをしている。地域の人々のためのイベントを手伝うのを楽しんでいる。",
         "choiceAnalysis":{"1":"to help は enjoy の後に不定詞は取れない。","2":"helps は動詞の原形で不適切。","3":"helping が正解。enjoy ～ing の形。","4":"helped は過去形で不適切。"},
         "grammar":{"point":"enjoy ～ing（～するのを楽しむ）","detail":"enjoyの後は動名詞（-ing形）のみ。不定詞は取れない。メガフェプスの一つ。"}}
    ]
}

# ===== 大問2: 会話文空所補充 (5問) =====
sec2 = {
    "name": "大問2", "type": "vocabulary",
    "instruction": "次の四つの会話文を完成させるために，(21)から(25)に入るものとして最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "questions": [
        {"number":21,"text":"A : Here is your room key, sir. You're in Room 403 on the fourth floor.\nB : Is there anywhere that I can ( 21 )?\nA : You should find some bottles of water in the fridge in your room, and there's also a vending machine here in the lobby, sir.\nB : Thanks!","choices":["leave my bags for a few hours","find out more about the city","buy an English newspaper","get something to drink"],"answer":4,"translation":"A：お部屋の鍵です。4階の403号室です。\nB：どこか飲み物が手に入る場所はありますか？\nA：お部屋の冷蔵庫に水のボトルがありますし、ロビーに自販機もございます。\nB：ありがとう！",
         "choiceAnalysis":{"1":"荷物を預ける場所の質問だが、回答が飲み物について。","2":"街の情報は回答と無関係。","3":"新聞は回答と無関係。","4":"get something to drink（飲み物を手に入れる）が正解。水や自販機の回答に対応。"},
         "grammar":{"point":"get something to drink","detail":"「飲み物を手に入れる」。something to ～ で「～するための何か」。"}},
        {"number":22,"text":"A : Are you leaving already?\nB : Yes. I want to be home by 7:30 so that I can ( 22 ).\nA : Oh, is that tonight? I forgot about that.\nB : It's going to be really exciting. It's between the two best teams in the world.","choices":["watch the international rugby game","make dinner for my wife","read a bedtime story to my kids","take a bath and go to bed early"],"answer":1,"translation":"A：もう帰るの？\nB：うん。7時半までに帰って国際ラグビーの試合を見たいんだ。\nA：ああ、今夜だったの？忘れていた。\nB：すごく盛り上がるよ。世界の2大チームの対戦だから。",
         "choiceAnalysis":{"1":"watch the international rugby game が正解。exciting / two best teams に対応。","2":"夕食作りは exciting や teams の話に合わない。","3":"bedtime story は試合の話と無関係。","4":"入浴は試合の話と無関係。"},
         "grammar":{"point":"so that S can ～","detail":"「Sが～できるように」という目的を表す接続詞。"}},
        {"number":23,"text":"A : Hi. Do you have ( 23 ) in the library?\nB : Yes. Do you want to see photos of famous ones?\nA : No. I want to find out how to grow bigger vegetables.\nB : In that case, try looking in section E3 on the second floor.","choices":["books about movie actors","anything about gardens","advice about food shopping","information about paintings"],"answer":2,"translation":"A：こんにちは。図書館に庭に関するものはありますか？\nB：はい。有名な庭の写真をご覧になりますか？\nA：いいえ。もっと大きな野菜の育て方を知りたいんです。\nB：それなら、2階のE3セクションを見てみてください。",
         "choiceAnalysis":{"1":"映画俳優は vegetables / gardens に無関係。","2":"anything about gardens（庭に関するもの）が正解。famous ones＝有名な庭、grow vegetables に対応。","3":"食品の買い物は野菜の育て方に合わない。","4":"絵画は文脈に合わない。"},
         "grammar":{"point":"anything about ～","detail":"「～に関する何か」。図書館での検索に使われる表現。"}},
        {"number":24,"text":"A : Honey, have you seen my smartphone? I can't find it anywhere.\nB : No, I haven't. Do you want me to ( 24 )?\nA : Yes, please. Hopefully, we'll be able to hear where it is.\nB : OK. It's ringing now.","choices":["buy a new one for you","set an alarm","try calling it","search upstairs"],"answer":3,"translation":"A：ねえ、私のスマホ見なかった？どこにもないの。\nB：見てないよ。電話してみようか？\nA：お願い。どこにあるか音で分かるかも。\nB：OK。鳴ってるよ。",
         "choiceAnalysis":{"1":"新しいのを買うのは hear where it is に合わない。","2":"アラームをセットは ringing に合わない。","3":"try calling it（電話してみる）が正解。hear / ringing に対応。","4":"2階を探すは音で探す文脈に合わない。"},
         "grammar":{"point":"try ～ing（試しに～してみる）","detail":"try calling＝試しに電話してみる。try to call＝電話しようとする、とは意味が異なる。"}},
        {"number":25,"text":"A : I can hear it. The sound is coming from ( 25 ).\nB : How did it get there?\nA : I must have left it there by accident when I was putting away the food we bought at the supermarket.\nB : Well, I'm glad that we've found it.","choices":["under the bed","one of the kitchen cabinets","behind the bookshelves","the laundry basket"],"answer":2,"translation":"A：聞こえる。音はキッチンの棚の一つから聞こえてくる。\nB：どうしてそこに？\nA：スーパーで買った食品を片付けている時にうっかり置き忘れたに違いない。\nB：見つかってよかった。",
         "choiceAnalysis":{"1":"ベッドの下は食品の片付けに無関係。","2":"one of the kitchen cabinets（キッチンの棚）が正解。putting away food / supermarket に対応。","3":"本棚の後ろは食品に無関係。","4":"洗濯かごは食品に無関係。"},
         "grammar":{"point":"must have + 過去分詞","detail":"「～したに違いない」。過去の行為に対する強い推量。"}}
    ]
}

data["sections"].append(sec1)
data["sections"].append(sec2)

outdir = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-1"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "_part1.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"✅ Part1 saved: {len(sec1['questions'])} + {len(sec2['questions'])} = {len(sec1['questions'])+len(sec2['questions'])} questions")
