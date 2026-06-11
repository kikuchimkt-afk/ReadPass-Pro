# -*- coding: utf-8 -*-
"""
2026年度 第1回（本会場）英検3級 data.json
大問3（reading-comprehension）Q21〜30 — 解説・和訳付き
一次ソース: 2026-1(本会場）/3級.pdf / 3級解答.pdf
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade3", "2026-1", "data.json",
)

section3 = {
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次のA，B，Cの内容に関して，質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Mr. Chen's Cooking Classes",
            "format": "notice",
            "paragraphs": [
                "Mr. Chen's Cooking Classes",
                "Are you interested in traditional Chinese dishes?",
                "Next March, Evansfield Cultural Center will hold cooking classes for people who want to learn about Chinese recipes. We will invite Mr. Chen as a special teacher.",
                "●Remember to bring an apron and a notebook.",
                "Place\nEvansfield Cultural Center",
                "Classes\n(For adults) Fridays, 7:00 p.m. to 9:00 p.m.\n(For teenagers) Saturdays, 2:00 p.m. to 3:30 p.m.",
                "About the teacher\nMr. Chen is one of the best chefs in our city. He has won some international cooking contests. He was also chosen as Great Young Chef of the Year last year.",
            ],
            "translations": [
                "チェン先生の料理教室",
                "伝統的な中国料理に興味はありますか？",
                "来月3月、エヴァンスフィールド文化センターでは、中国のレシピを学びたい人のための料理教室を開催します。チェン先生を特別講師として招きます。",
                "●エプロンとノートを持参してください。",
                "場所\nエヴァンスフィールド文化センター",
                "クラス\n（大人向け）金曜日 午後7時〜9時\n（10代向け）土曜日 午後2時〜3時30分",
                "講師について\nチェン先生は市内でも最高のシェフの一人です。国際的な料理コンテストでいくつか優勝したことがあります。昨年は「今年の優秀な若手シェフ」にも選ばれました。",
            ],
            "questions": [
                {
                    "number": 21,
                    "question": "What should the members of the classes do?",
                    "questionTranslation": "クラスの参加者は何をすべき？",
                    "choices": [
                        "Bring a notebook.",
                        "Wash the dishes after cooking.",
                        "Buy Mr. Chen's recipe book.",
                        "Learn to speak Chinese.",
                    ],
                    "answer": 1,
                    "sourceEvidence": ["Remember to bring an apron and a notebook."],
                    "grammar": "持参するもの＝apron and a notebook。選択肢1はノートを持参。",
                    "grammarSimple": "エプロンとノートをもっていくように書いてあるよ。",
                    "choiceAnalysis": [
                        "✅ Bring a notebook.＝ノートを持参。Remember to bring an apron and a notebook. の notebook と一致→正解",
                        "❌ Wash the dishes after cooking.＝料理後の皿洗い。wash dishes の記述なし",
                        "❌ Buy Mr. Chen's recipe book.＝レシピ本購入。recipe book の記述なし",
                        "❌ Learn to speak Chinese.＝中国語学習。Chinese recipes を学ぶが speak Chinese とは異なる",
                    ],
                    "choiceAnalysisSimple": [
                        "○ ノートをもっていく！",
                        "さらあらいとは書いてないよ。",
                        "レシピ本をかうとは書いてないよ。",
                        "中国語をまなぶ話じゃないよ。",
                    ],
                    "choiceTranslations": [
                        "ノートを持参する。",
                        "料理後に皿を洗う。",
                        "チェン先生のレシピ本を買う。",
                        "中国語を学ぶ。",
                    ],
                },
                {
                    "number": 22,
                    "question": "Mr. Chen is a chef who",
                    "questionTranslation": "チェン先生はどんなシェフ？",
                    "choices": [
                        "gave lessons to students online.",
                        "taught teenagers on Saturday mornings.",
                        "invited his friends to the cooking classes.",
                        "won some cooking contests.",
                    ],
                    "answer": 4,
                    "sourceEvidence": ["He has won some international cooking contests."],
                    "grammar": "He has won some international cooking contests＝料理コンテストで優勝した経験がある。",
                    "grammarSimple": "国際的な料理コンテストでかちとったことがあるよ。",
                    "choiceAnalysis": [
                        "❌ gave lessons to students online.＝オンライン授業。online lessons の記述なし",
                        "❌ taught teenagers on Saturday mornings.＝土曜の朝。Classes は Saturdays, 2:00 p.m.（午後）",
                        "❌ invited his friends to the cooking classes.＝友達招待。invite friends の記述なし",
                        "✅ won some cooking contests.＝He has won some international cooking contests. と一致→正解",
                    ],
                    "choiceAnalysisSimple": [
                        "オンラインの授業とは書いてないよ。",
                        "土曜の朝ではなく午後だよ。",
                        "ともだちをしょうたいとは書いてないよ。",
                        "○ 料理コンテストでかった！",
                    ],
                    "choiceTranslations": [
                        "オンラインで生徒に授業をした。",
                        "土曜の朝に10代を教えた。",
                        "友達を料理教室に招待した。",
                        "料理コンテストで優勝した。",
                    ],
                },
            ],
        },
        {
            "label": "B",
            "title": "Winter sale",
            "format": "multi-email",
            "emails": [
                {
                    "meta": {
                        "from": "Judy Smith",
                        "to": "Ann Smith",
                        "date": "December 8",
                        "subject": "Winter sale",
                    },
                    "body": (
                        "Dear Grandma,\n"
                        "Thank you for giving me a lovely present last month. I really like the wallet!\n"
                        "Yesterday, I visited a department store near the station. They were having a winter sale! "
                        "You said you wanted a brown sweater, right? I looked for one, but I couldn't find any brown ones. "
                        "However, I saw a nice scarf and bought it for you! I also bought a coat for myself. "
                        "Can I bring the scarf to you? Will you be home this Saturday?\n"
                        "Write back soon,\n"
                        "Judy"
                    ),
                    "translation": (
                        "おばあちゃんへ\n"
                        "先月、素敵なプレゼントをありがとう。財布、とても気に入ったよ！\n"
                        "昨日、駅の近くのデパートに行ったら、冬のセールをやっていたよ！"
                        "茶色のセーターが欲しいって言ってたよね？探したけど茶色はなかった。"
                        "でも、いいマフラーが見つかって、おばあちゃんに買ったよ！自分にもコートを買った。"
                        "マフラーを持っていってもいい？今週の土曜日、家にいる？\n"
                        "早く返事してね、\n"
                        "ジュディより"
                    ),
                },
                {
                    "meta": {
                        "from": "Ann Smith",
                        "to": "Judy Smith",
                        "date": "December 8",
                        "subject": "Thank you!",
                    },
                    "body": (
                        "Dear Judy,\n"
                        "I am glad to hear that you like the wallet. I found it at a shopping mall next to the museum. "
                        "Thank you for the scarf! Yes, I will be home this Saturday, and my old friend Linda will also visit my house that day! "
                        "I have not seen her since she moved to another city two years ago. Do you remember her? "
                        "You often met her at my house when you were little. You can see her this Saturday if you come here. "
                        "By the way, will your mom come with you that day?\n"
                        "Love,\n"
                        "Grandma"
                    ),
                    "translation": (
                        "ジュディへ\n"
                        "財布が気に入ってくれてうれしいわ。博物館の隣のショッピングモールで見つけたの。"
                        "マフラーありがとう！土曜日は家にいるわ。古い友達のリンダもその日うちに来るの！"
                        "2年前に別の街に引っ越してから会っていないの。覚えてる？小さいとき、よくうちで会ってたわ。"
                        "土曜日に来ればリンダにも会えるわ。その日、お母さんも一緒に来る？\n"
                        "愛を込めて、\n"
                        "おばあちゃんより"
                    ),
                },
                {
                    "meta": {
                        "from": "Judy Smith",
                        "to": "Ann Smith",
                        "date": "December 8",
                        "subject": "Great!",
                    },
                    "body": (
                        "Dear Grandma,\n"
                        "Yes, I remember Linda! She was very kind to me! Linda often told me stories when you were cooking in the kitchen. "
                        "They were so interesting! I want to meet her, too! But my mom cannot come with me that day because she has to work. "
                        "I will visit you alone by bus. Yesterday, I also found a new cake shop near the park, "
                        "so I will buy some cakes for you and Linda before I visit your house.\n"
                        "See you soon,\n"
                        "Judy"
                    ),
                    "translation": (
                        "おばあちゃんへ\n"
                        "うん、リンダのこと覚えてる！とても親切だったよ！おばあちゃんが台所で料理しているとき、"
                        "リンダがよく物語を話してくれた。とてもおもしろかった！私も会いたい！"
                        "でも、その日お母さんは仕事で一緒に来られない。バスで一人で行くよ。"
                        "昨日、公園の近くに新しいケーキ屋さんも見つけたから、うちに行く前に"
                        "おばあちゃんとリンダのケーキを買うね。\n"
                        "またね、\n"
                        "ジュディより"
                    ),
                },
            ],
            "paragraphs": [
                "Judy thanks her grandmother for a wallet, shops at a winter sale, and plans to visit on Saturday.",
            ],
            "translations": [
                "ジュディはおばあちゃんに財布のお礼をし、冬のセールで買い物をして、土曜日に訪ねる予定だ。",
            ],
            "questions": [
                {
                    "number": 23,
                    "question": "What did Judy do at the department store yesterday?",
                    "questionTranslation": "ジュディは昨日デパートで何をした？",
                    "choices": [
                        "She bought a coat and a scarf.",
                        "She found a nice wallet.",
                        "She bought a brown sweater.",
                        "She worked as a staff member.",
                    ],
                    "answer": 1,
                    "sourceEvidence": ["I saw a nice scarf and bought it for you! I also bought a coat for myself."],
                    "grammar": "マフラーをおばあちゃんに、コートを自分に買った。",
                    "grammarSimple": "マフラーをおばあちゃんに、コートをじぶんにかったよ。",
                    "choiceAnalysis": [
                        "✅ She bought a coat and a scarf.＝bought it for you（scarf）＋bought a coat for myself と一致→正解",
                        "❌ She found a nice wallet.＝財布発見。wallet はおばあちゃんのプレゼントでデパートでの行動ではない",
                        "❌ She bought a brown sweater.＝茶色セーター。couln't find any brown ones と矛盾",
                        "❌ She worked as a staff member.＝店員として勤務。staff member の記述なし",
                    ],
                    "choiceAnalysisSimple": [
                        "○ コートとマフラーをかった！",
                        "財布はおばあちゃんのプレゼントだよ。",
                        "茶色のセーターはみつからなかったよ。",
                        "店員としてはたらいた話はないよ。",
                    ],
                    "choiceTranslations": [
                        "コートとマフラーを買った。",
                        "いい財布を見つけた。",
                        "茶色のセーターを買った。",
                        "店員として働いた。",
                    ],
                },
                {
                    "number": 24,
                    "question": "Judy's grandmother bought the wallet",
                    "questionTranslation": "ジュディのおばあちゃんは財布をどこで買った？",
                    "choices": [
                        "at a shop in the park.",
                        "at a shopping mall beside the museum.",
                        "at a shop next to her house.",
                        "at a department store in Linda's city.",
                    ],
                    "answer": 2,
                    "sourceEvidence": ["I found it at a shopping mall next to the museum."],
                    "grammar": "おばあちゃんのメールで財布の購入場所を説明。",
                    "grammarSimple": "博物館のとなりのショッピングモールでかったって書いてあるよ。",
                    "choiceAnalysis": [
                        "❌ at a shop in the park.＝公園の店。park は後の cake shop の場所",
                        "✅ at a shopping mall beside the museum.＝I found it at a shopping mall next to the museum. と一致→正解",
                        "❌ at a shop next to her house.＝家の隣の店。next to her house の記述なし",
                        "❌ at a department store in Linda's city.＝リンダの街のデパート。department store は Judy の買い物場所",
                    ],
                    "choiceAnalysisSimple": [
                        "公園の店とは書いてないよ。",
                        "○ 博物館のとなりのモール！",
                        "家のとなりとは書いてないよ。",
                        "リンダの街のデパートとは書いてないよ。",
                    ],
                    "choiceTranslations": [
                        "公園の店で。",
                        "博物館の隣のショッピングモールで。",
                        "家の隣の店で。",
                        "リンダの街のデパートで。",
                    ],
                },
                {
                    "number": 25,
                    "question": "What did Judy often do when her grandmother was cooking?",
                    "questionTranslation": "おばあちゃんが料理しているとき、ジュディはよく何をした？",
                    "choices": [
                        "She shared a cake with Linda.",
                        "She visited a park with her mother.",
                        "She listened to Linda's stories.",
                        "She helped her grandmother in the kitchen.",
                    ],
                    "answer": 3,
                    "sourceEvidence": ["Linda often told me stories when you were cooking in the kitchen."],
                    "grammar": "料理中＝Linda often told me stories（リンダの物語を聞いた）。",
                    "grammarSimple": "おばあちゃんが料理しているとき、リンダの物語をきいていたよ。",
                    "choiceAnalysis": [
                        "❌ She shared a cake with Linda.＝ケーキ共有。cakes は訪問前に買う予定で料理中の行動ではない",
                        "❌ She visited a park with her mother.＝公園訪問。mother は仕事で同行しない（第三通メール）",
                        "✅ She listened to Linda's stories.＝Linda often told me stories when you were cooking と一致→正解",
                        "❌ She helped her grandmother in the kitchen.＝台所手伝い。told me stories（物語を聞く）と異なる",
                    ],
                    "choiceAnalysisSimple": [
                        "ケーキをわけた話は土曜日のよていだよ。",
                        "公園に行った話はないよ。",
                        "○ リンダの物語をきいていた！",
                        "台所でてつだった話じゃないよ。",
                    ],
                    "choiceTranslations": [
                        "リンダとケーキを分け合った。",
                        "母と公園を訪れた。",
                        "リンダの物語を聞いた。",
                        "おばあちゃんを台所で手伝った。",
                    ],
                },
            ],
        },
        {
            "label": "C",
            "title": "Never Too Late",
            "format": "passage",
            "paragraphs": [
                "Anna Mary Robertson Moses, also known as Grandma Moses, was an American artist. She was born in 1860 on a farm in New York. As a girl, Anna worked hard on the farm and took care of her family. She liked to play outside with her brothers in her free time. She also loved making things with her hands. She often enjoyed drawing pictures on paper her father bought for her.",
                "Anna married Thomas Moses in 1887 and lived on the local farm she loved. Even after Thomas died in 1927, she kept working on her farm with the help of her youngest son. But when she got older, it was hard for her to do some things on the farm because her hands hurt. So, she decided to try painting instead. She was already over seventy-five years old then.",
                "Anna painted all the things she loved from her farm life. She often painted green fields, snowy winters, and happy people living in nature. Her paintings were so unique and full of happiness that a lot of people wanted to see them. They felt so warm and happy when they saw her works painted in a simple way with many colors.",
                "Anna kept painting until about 1960. She created more than 1,500 works of art in her life, and her paintings became popular across the country. Even today, many people come to see her paintings in museums. Anna and her paintings show that anyone can try something new at any time in their life.",
            ],
            "translations": [
                "アンナ・メアリー・ロバートソン・モーゼスは、グランマ・モーゼスとして知られるアメリカの画家だった。1860年、ニューヨークの農場に生まれた。少女のころ、アンナは農場で一生懸命働き、家族の世話をした。自由な時間には兄弟と外で遊ぶのが好きだった。手で物を作るのも好きで、父が買ってくれた紙に絵を描くのをよく楽しんだ。",
                "アンナは1887年にトーマス・モーゼスと結婚し、愛する地元の農場で暮らした。1927年にトーマスが亡くなった後も、末の息子の助けを借りて農場で働き続けた。しかし年を取ると、手が痛くて農場での作業が難しくなった。そこで絵を描くことに挑戦することにした。当時、すでに75歳を超えていた。",
                "アンナは農場生活で愛したものをすべて絵に描いた。緑の野原、雪の冬、自然の中で暮らす幸せな人々をよく描いた。彼女の絵はとても独特で幸せに満ちていたため、多くの人が見に来た。多くの色でシンプルに描かれた作品を見ると、人々は温かく幸せな気持ちになった。",
                "アンナは1960年頃まで絵を描き続けた。生涯で1,500点以上の作品を残し、絵は全国で人気になった。今でも多くの人が博物館で彼女の絵を見に来る。アンナと彼女の絵は、人生のいつでも誰でも新しいことに挑戦できることを示している。",
            ],
            "questions": [
                {
                    "number": 26,
                    "question": "What did Anna like when she was a child?",
                    "questionTranslation": "アンナは子どものころ何が好きだった？",
                    "choices": [
                        "Drawing on paper.",
                        "Taking pictures.",
                        "Buying gifts for her father.",
                        "Playing games at home.",
                    ],
                    "answer": 1,
                    "sourceEvidence": ["She often enjoyed drawing pictures on paper her father bought for her."],
                    "grammar": "drawing pictures on paper＝紙に絵を描くこと。",
                    "grammarSimple": "父がかってくれた紙にえをかくのがすきだったよ。",
                    "choiceAnalysis": [
                        "✅ Drawing on paper.＝drawing pictures on paper her father bought for her と一致→正解",
                        "❌ Taking pictures.＝写真撮影。taking pictures の記述なし",
                        "❌ Buying gifts for her father.＝父への贈り物。father bought paper for her（父が紙を買った）",
                        "❌ Playing games at home.＝家でゲーム。played outside with her brothers と外で遊ぶ",
                    ],
                    "choiceAnalysisSimple": [
                        "○ 紙にえをかくのがすき！",
                        "写真をとった話はないよ。",
                        "プレゼントをかう話はないよ。",
                        "外であそんでいたよ。",
                    ],
                    "choiceTranslations": [
                        "紙に絵を描くこと。",
                        "写真を撮ること。",
                        "父への贈り物を買うこと。",
                        "家でゲームをすること。",
                    ],
                },
                {
                    "number": 27,
                    "question": "Why did Anna begin painting?",
                    "questionTranslation": "アンナはなぜ絵を描き始めた？",
                    "choices": [
                        "She had to teach art to her son.",
                        "She had a problem with her hands.",
                        "She did not want to look old.",
                        "She did not enjoy living on her farm.",
                    ],
                    "answer": 2,
                    "sourceEvidence": ["it was hard for her to do some things on the farm because her hands hurt"],
                    "grammar": "手が痛くて農作業が難しくなった→絵を描くことにした。",
                    "grammarSimple": "てがいたくてのうさぎがむずかしくなったから、えをかくことにしたよ。",
                    "choiceAnalysis": [
                        "❌ She had to teach art to her son.＝美術指導。teach art の記述なし",
                        "✅ She had a problem with her hands.＝because her hands hurt. So, she decided to try painting と一致→正解",
                        "❌ She did not want to look old.＝老けたくない。look old の記述なし",
                        "❌ She did not enjoy living on her farm.＝農場が嫌。loved the local farm she loved と矛盾",
                    ],
                    "choiceAnalysisSimple": [
                        "むすこにおしえる話はないよ。",
                        "○ てがいたくてのうさぎがむずかしかった！",
                        "としをとりたくない話はないよ。",
                        "のうじょうがきらいだったわけじゃないよ。",
                    ],
                    "choiceTranslations": [
                        "息子に美術を教えなければならなかったから。",
                        "手に問題があったから。",
                        "老けたくなかったから。",
                        "農場での生活を楽しんでいなかったから。",
                    ],
                },
                {
                    "number": 28,
                    "question": "The paintings Anna created",
                    "questionTranslation": "アンナが描いた絵はどんなもの？",
                    "choices": [
                        "made her much poorer.",
                        "made people free.",
                        "were sold to farmers.",
                        "had a lot of colors.",
                    ],
                    "answer": 4,
                    "sourceEvidence": ["painted in a simple way with many colors"],
                    "grammar": "with many colors＝多くの色を使った絵。",
                    "grammarSimple": "たくさんの色をつかって、かんたんなしかたでかかれたよ。",
                    "choiceAnalysis": [
                        "❌ made her much poorer.＝貧しくした。became popular across the country と成功の話",
                        "❌ made people free.＝人を自由に。made people free の記述なし",
                        "❌ were sold to farmers.＝農民に売却。sold to farmers の記述なし",
                        "✅ had a lot of colors.＝painted in a simple way with many colors と一致→正解",
                    ],
                    "choiceAnalysisSimple": [
                        "貧しくなった話じゃないよ。",
                        "自由にした話はないよ。",
                        "のうみんにうった話はないよ。",
                        "○ たくさんの色があった！",
                    ],
                    "choiceTranslations": [
                        "彼女をずっと貧しくした。",
                        "人々を自由にした。",
                        "農民に売られた。",
                        "多くの色があった。",
                    ],
                },
                {
                    "number": 29,
                    "question": "What did Anna do in her life?",
                    "questionTranslation": "アンナは生涯で何をした？",
                    "choices": [
                        "She tried to travel across America.",
                        "She invented new colors.",
                        "She created many works of art.",
                        "She built a famous museum.",
                    ],
                    "answer": 3,
                    "sourceEvidence": ["She created more than 1,500 works of art in her life"],
                    "grammar": "1,500点以上の作品を残した＝多くの芸術作品を作った。",
                    "grammarSimple": "しょうがいで1500いじょうのさくひんをつくったよ。",
                    "choiceAnalysis": [
                        "❌ She tried to travel across America.＝アメリカ横断。travel across America の記述なし",
                        "❌ She invented new colors.＝新色発明。invented colors の記述なし",
                        "✅ She created many works of art.＝created more than 1,500 works of art in her life と一致→正解",
                        "❌ She built a famous museum.＝博物館建設。come to see her paintings in museums（既存の博物館）",
                    ],
                    "choiceAnalysisSimple": [
                        "アメリカをたびした話はないよ。",
                        "新しい色をはつめいした話はないよ。",
                        "○ たくさんのさくひんをつくった！",
                        "博物館をたてた話じゃないよ。",
                    ],
                    "choiceTranslations": [
                        "アメリカ横断の旅をしようとした。",
                        "新しい色を発明した。",
                        "多くの芸術作品を作った。",
                        "有名な博物館を建てた。",
                    ],
                },
                {
                    "number": 30,
                    "question": "What is this story about?",
                    "questionTranslation": "この話は何について？",
                    "choices": [
                        "A woman who loved her grandmother.",
                        "A popular artist in America.",
                        "How to live on a farm.",
                        "How to help older people.",
                    ],
                    "answer": 2,
                    "sourceEvidence": ["was an American artist", "her paintings became popular across the country"],
                    "grammar": "グランマ・モーゼスというアメリカの人気画家の生涯。",
                    "grammarSimple": "アメリカでにんきのがか、グランマ・モーゼスのお話だよ。",
                    "choiceAnalysis": [
                        "❌ A woman who loved her grandmother.＝おばあちゃん愛。Grandma Moses はAnnaのあだ名",
                        "✅ A popular artist in America.＝American artist、paintings became popular across the country と一致→正解",
                        "❌ How to live on a farm.＝農場生活の仕方。farm life は背景の一部",
                        "❌ How to help older people.＝高齢者支援。anyone can try something new が主テーマ",
                    ],
                    "choiceAnalysisSimple": [
                        "おばあちゃんの話じゃないよ。",
                        "○ アメリカのにんきがかのお話！",
                        "のうじょうのくらしかただけじゃないよ。",
                        "お年寄りのたすけ方じゃないよ。",
                    ],
                    "choiceTranslations": [
                        "おばあちゃんを愛した女性。",
                        "アメリカの人気画家。",
                        "農場での暮らし方。",
                        "高齢者の助け方。",
                    ],
                },
            ],
        },
    ],
}

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

new_sections = []
replaced = False
for sec in data.get("sections", []):
    if sec.get("name") == "大問3":
        new_sections.append(section3)
        replaced = True
    else:
        new_sections.append(sec)
if not replaced:
    new_sections.append(section3)

data["sections"] = new_sections

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

q_count = sum(len(p["questions"]) for p in section3["passages"])
print(f"Wrote section3 ({q_count} questions, 3 passages) to {DATA_PATH}")
