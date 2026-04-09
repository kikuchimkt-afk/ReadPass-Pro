"""Add vocabulary and lessonPlan to 2023-1 data.json"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2023-1\data.json"
data = json.load(open(path, "r", encoding="utf-8"))

# Vocabulary - 20 key words from this exam with Japanese distractors
data["vocabulary"] = [
    {"word": "name", "meaning": "名前", "pos": "名詞", "level": "5級",
     "example": "Please write your name here.", "distractors": ["とり", "ドア", "とけい"],
     "wordAudio": "audio/vocab/w_001_name.mp3"},
    {"word": "subject", "meaning": "教科", "pos": "名詞", "level": "5級",
     "example": "Which subject do you like?", "distractors": ["ちーむ", "まど", "ばしょ"],
     "wordAudio": "audio/vocab/w_002_subject.mp3"},
    {"word": "shop", "meaning": "店", "pos": "名詞", "level": "5級",
     "example": "Let's go to a cake shop.", "distractors": ["じてんしゃ", "たまご", "いす"],
     "wordAudio": "audio/vocab/w_003_shop.mp3"},
    {"word": "game", "meaning": "ゲーム", "pos": "名詞", "level": "5級",
     "example": "Students play games in class.", "distractors": ["でんわ", "とけい", "カメラ"],
     "wordAudio": "audio/vocab/w_004_game.mp3"},
    {"word": "breakfast", "meaning": "朝食", "pos": "名詞", "level": "5級",
     "example": "Alice eats toast for breakfast.", "distractors": ["しんぶん", "おんがく", "ゆき"],
     "wordAudio": "audio/vocab/w_005_breakfast.mp3"},
    {"word": "fan", "meaning": "ファン", "pos": "名詞", "level": "5級",
     "example": "Jessica is a big fan.", "distractors": ["テーブル", "やま", "はこ"],
     "wordAudio": "audio/vocab/w_006_fan.mp3"},
    {"word": "fish", "meaning": "魚", "pos": "名詞", "level": "5級",
     "example": "Look at that red fish.", "distractors": ["ボール", "はな", "かわ"],
     "wordAudio": "audio/vocab/w_007_fish.mp3"},
    {"word": "have", "meaning": "持つ・過ごす", "pos": "動詞", "level": "5級",
     "example": "Have a nice day.", "distractors": ["たべる", "いく", "くる"],
     "wordAudio": "audio/vocab/w_008_have.mp3"},
    {"word": "right", "meaning": "正しい", "pos": "形容詞", "level": "5級",
     "example": "That's right.", "distractors": ["げんき", "ちいさい", "うれしい"],
     "wordAudio": "audio/vocab/w_009_right.mp3"},
    {"word": "about", "meaning": "〜について", "pos": "前置詞", "level": "5級",
     "example": "Kelly talks about her dream.", "distractors": ["〜のそばに", "〜から", "〜のしたに"],
     "wordAudio": "audio/vocab/w_010_about.mp3"},
    {"word": "night", "meaning": "夜", "pos": "名詞", "level": "5級",
     "example": "She does homework at night.", "distractors": ["あさ", "ひる", "ゆうがた"],
     "wordAudio": "audio/vocab/w_011_night.mp3"},
    {"word": "year", "meaning": "年・歳", "pos": "名詞", "level": "5級",
     "example": "She is 13 years old.", "distractors": ["くだもの", "て", "おんなのこ"],
     "wordAudio": "audio/vocab/w_012_year.mp3"},
    {"word": "help", "meaning": "手伝う", "pos": "動詞", "level": "5級",
     "example": "Please help me.", "distractors": ["おしえる", "みる", "きく"],
     "wordAudio": "audio/vocab/w_013_help.mp3"},
    {"word": "letter", "meaning": "手紙", "pos": "名詞", "level": "5級",
     "example": "I'm writing a letter.", "distractors": ["ほん", "えんぴつ", "でんわ"],
     "wordAudio": "audio/vocab/w_014_letter.mp3"},
    {"word": "cook", "meaning": "料理する", "pos": "動詞", "level": "5級",
     "example": "We cook dinner every Sunday.", "distractors": ["あらう", "あそぶ", "はしる"],
     "wordAudio": "audio/vocab/w_015_cook.mp3"},
    {"word": "dictionary", "meaning": "辞書", "pos": "名詞", "level": "5級",
     "example": "Can I use your dictionary?", "distractors": ["えんぴつ", "きょうかしょ", "ノート"],
     "wordAudio": "audio/vocab/w_016_dictionary.mp3"},
    {"word": "homework", "meaning": "宿題", "pos": "名詞", "level": "5級",
     "example": "Today's homework is hard.", "distractors": ["テスト", "じゅぎょう", "やすみ"],
     "wordAudio": "audio/vocab/w_017_homework.mp3"},
    {"word": "close", "meaning": "閉める", "pos": "動詞", "level": "5級",
     "example": "Close the window, please.", "distractors": ["あける", "とめる", "つける"],
     "wordAudio": "audio/vocab/w_018_close.mp3"},
    {"word": "walk", "meaning": "歩く", "pos": "動詞", "level": "5級",
     "example": "Who is walking with you?", "distractors": ["はしる", "とぶ", "およぐ"],
     "wordAudio": "audio/vocab/w_019_walk.mp3"},
    {"word": "find", "meaning": "見つける", "pos": "動詞", "level": "5級",
     "example": "I can't find my pen.", "distractors": ["かう", "もつ", "おく"],
     "wordAudio": "audio/vocab/w_020_find.mp3"}
]

# LessonPlan with 4 Focus Points
data["lessonPlan"] = {
    "focusPoints": [
        {
            "id": "fp1",
            "title": "名詞と意味の対応",
            "titleSimple": "ことばのいみをおぼえよう",
            "explanation": "英語の名詞は、場面に合った単語を選ぶことが大切です。name（名前）、subject（教科）、breakfast（朝食）など、日常で使う言葉を覚えましょう。",
            "explanationSimple": "えいごのことばは、ばめんにあったものをえらぶことがだいじ！name（なまえ）、breakfast（あさごはん）など、まいにちのことばをおぼえよう！",
            "sourceQuote": "Please write your name and telephone number here.",
            "sourceQuoteTranslation": "ここにあなたの名前と電話番号を書いてください。",
            "examples": [
                {"en": "Which subject do you like at school?", "ja": "学校でどの教科が好きですか？"},
                {"en": "Alice eats toast for breakfast.", "ja": "アリスは朝食にトーストを食べます。"},
                {"en": "Jessica is a big fan of soccer.", "ja": "ジェシカはサッカーの大ファンです。"}
            ],
            "sourceQuoteAudio": "audio/sq_fp1.mp3",
            "practicePassage": {
                "en": "My name is Tom. I like many subjects at school. My favorite subject is science. I eat breakfast every morning. I like toast and milk. My sister is a big fan of basketball.",
                "ja": "ぼくの名前はトムです。学校のたくさんの教科が好きです。いちばん好きな教科は理科です。毎朝、朝食を食べます。トーストと牛乳が好きです。姉はバスケットボールの大ファンです。"
            }
        },
        {
            "id": "fp2",
            "title": "前置詞の使い方",
            "titleSimple": "ばしょやじかんのことば",
            "explanation": "前置詞は場所や時間を表す小さな言葉です。about（～について）、at night（夜に）、near（～の近くで）など、どの前置詞がどの場面で使われるかを覚えましょう。",
            "explanationSimple": "about は「～について」、at night は「よるに」、near は「ちかくで」だよ！ちいさいことばだけど、とてもだいじ！",
            "sourceQuote": "Kelly often talks about her future dream.",
            "sourceQuoteTranslation": "ケリーはよく将来の夢について話します。",
            "examples": [
                {"en": "Yoshiko does her homework at night.", "ja": "よし子は夜に宿題をします。"},
                {"en": "I play baseball near my house.", "ja": "家の近くで野球をします。"},
                {"en": "It's on the table.", "ja": "テーブルの上にあります。"}
            ],
            "sourceQuoteAudio": "audio/sq_fp2.mp3",
            "practicePassage": {
                "en": "I often talk about my future dream with my friends. I want to be a teacher. I do my homework at night. My house is near the school. My books are on my desk.",
                "ja": "ぼくはよく将来の夢について友達と話します。先生になりたいです。夜に宿題をします。家は学校の近くです。本は机の上にあります。"
            }
        },
        {
            "id": "fp3",
            "title": "代名詞の格変化",
            "titleSimple": "I, my, me, mine のつかいわけ",
            "explanation": "I（私は）、my（私の）、me（私を）、mine（私のもの）は、文の中での役割によって使い分けます。help me のように動詞の後ろでは me を使います。",
            "explanationSimple": "「わたしは」→ I、「わたしの」→ my、「わたしを」→ me、「わたしのもの」→ mine だよ！「てつだって」は help me！",
            "sourceQuote": "Dad, please help me.",
            "sourceQuoteTranslation": "お父さん、私を手伝ってください。",
            "examples": [
                {"en": "I cook dinner every Sunday.", "ja": "私は毎週日曜日に夕食を作ります。"},
                {"en": "What are you doing?", "ja": "あなたは何をしていますか？"},
                {"en": "How about this afternoon?", "ja": "午後はどうですか？"}
            ],
            "sourceQuoteAudio": "audio/sq_fp3.mp3",
            "practicePassage": {
                "en": "I like cooking. My sister and I cook dinner every Sunday. My mother helps me sometimes. She says my food is very good. That makes me happy.",
                "ja": "わたしは料理が好きです。姉と毎週日曜日に夕食を作ります。お母さんが時々手伝ってくれます。わたしの料理はとてもおいしいと言ってくれます。うれしくなります。"
            }
        },
        {
            "id": "fp4",
            "title": "疑問詞を使った文",
            "titleSimple": "しつもんのしかた",
            "explanation": "how（どうやって）、what（何を）、who（だれ）、where（どこ）などの疑問詞を文頭に置いて質問を作ります。語順は「疑問詞＋助動詞/be動詞＋主語＋動詞」です。",
            "explanationSimple": "「どうやって？」→ How、「なにを？」→ What、「だれ？」→ Who だよ！しつもんするときのじゅんばんをおぼえよう！",
            "sourceQuote": "How does your sister practice the piano?",
            "sourceQuoteTranslation": "あなたのお姉さんはどうやってピアノを練習しますか？",
            "examples": [
                {"en": "What are you doing?", "ja": "あなたは何をしていますか？"},
                {"en": "Who is walking with Mr. Suzuki?", "ja": "鈴木先生と歩いているのはだれですか？"},
                {"en": "Where do you play baseball?", "ja": "どこで野球をしますか？"}
            ],
            "sourceQuoteAudio": "audio/sq_fp4.mp3",
            "practicePassage": {
                "en": "How does your sister study English? She watches English movies. What do you do after school? I play baseball near my house. Who is your best friend? My best friend is Tom.",
                "ja": "あなたのお姉さんはどうやって英語を勉強しますか？英語の映画を見ます。放課後は何をしますか？家の近くで野球をします。いちばんの友達はだれですか？いちばんの友達はトムです。"
            }
        }
    ]
}

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ Updated data.json: {os.path.getsize(path)} bytes")
print(f"   Vocabulary: {len(data['vocabulary'])} words")
print(f"   FocusPoints: {len(data['lessonPlan']['focusPoints'])}")
