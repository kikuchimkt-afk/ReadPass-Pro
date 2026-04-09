"""Generate data.json for Grade 5 2023-1 exam"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Answer key from user's image:
# 大問1: (1)2 (2)3 (3)1 (4)1 (5)2 (6)1 (7)3 (8)4 (9)3 (10)1 (11)1 (12)2 (13)3 (14)2 (15)1
# 大問2: (16)4 (17)1 (18)3 (19)1 (20)3
# 大問3: (21)4 (22)3 (23)2 (24)1 (25)4

data = {
    "title": "英検5級 2023年度 第1回",
    "grade": "grade5",
    "exam": "2023-1",
    "sections": [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(15)までの（　）に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",
            "questions": [
                {
                    "number": 1,
                    "text": "A: Please write your (　) and telephone number here.\nB: OK.",
                    "choices": ["bird", "name", "door", "watch"],
                    "answer": 2,
                    "grammar": "「ここにあなたの○○と電話番号を書いてください」→ name（名前）。申込書等に名前と電話番号を書く場面。",
                    "grammarSimple": "「○○とでんわばんごうをかいてね」→ name（なまえ）！",
                    "choiceAnalysis": [
                        "bird＝鳥。",
                        "○ name＝名前。名前と電話番号を書く。",
                        "door＝ドア。",
                        "watch＝腕時計。"
                    ],
                    "choiceAnalysisSimple": [
                        "「とり」はちがうよ。",
                        "○「なまえ」がぴったり！",
                        "「ドア」はちがうよ。",
                        "「うでどけい」はちがうよ。"
                    ],
                    "questionAudio": "audio/q1.mp3",
                    "translation": "A: ここにあなたの（　）と電話番号を書いてください。\nB: わかりました。",
                    "choiceTranslations": ["鳥", "名前", "ドア", "腕時計"]
                },
                {
                    "number": 2,
                    "text": "A: Kyoko, which (　) do you like at school, science or math?\nB: Math.",
                    "choices": ["team", "window", "subject", "place"],
                    "answer": 3,
                    "grammar": "「学校でどの○○が好き？理科それとも算数？」→ subject（教科）。",
                    "grammarSimple": "「がっこうでどの○○がすき？」→ subject（きょうか）！",
                    "choiceAnalysis": [
                        "team＝チーム。",
                        "window＝窓。",
                        "○ subject＝教科。理科か算数かを聞いている。",
                        "place＝場所。"
                    ],
                    "choiceAnalysisSimple": [
                        "「チーム」はちがうよ。",
                        "「まど」はちがうよ。",
                        "○「きょうか」がぴったり！",
                        "「ばしょ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q2.mp3",
                    "translation": "A: きょうこ、学校でどの（　）が好き？理科それとも算数？\nB: 算数。",
                    "choiceTranslations": ["チーム", "窓", "教科", "場所"]
                },
                {
                    "number": 3,
                    "text": "A: Let's go to a new cake (　), Tina.\nB: That's a good idea.",
                    "choices": ["shop", "bike", "egg", "chair"],
                    "answer": 1,
                    "grammar": "「新しいケーキ○○に行こうよ」→ shop（店）。cake shop＝ケーキ屋。",
                    "grammarSimple": "「あたらしいケーキ○○にいこう！」→ shop（おみせ）！",
                    "choiceAnalysis": [
                        "○ shop＝店。cake shop でケーキ屋。",
                        "bike＝自転車。",
                        "egg＝卵。",
                        "chair＝椅子。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「おみせ」がぴったり！",
                        "「じてんしゃ」はちがうよ。",
                        "「たまご」はちがうよ。",
                        "「いす」はちがうよ。"
                    ],
                    "questionAudio": "audio/q3.mp3",
                    "translation": "A: 新しいケーキ（　）に行こうよ、ティナ。\nB: いい考えね。",
                    "choiceTranslations": ["店", "自転車", "卵", "椅子"]
                },
                {
                    "number": 4,
                    "text": "Students often play (　) in Mr. Brown's English class.",
                    "choices": ["games", "phones", "clocks", "cameras"],
                    "answer": 1,
                    "grammar": "「ブラウン先生の英語の授業では、生徒はよく○○をする」→ games（ゲーム）。play games＝ゲームをする。",
                    "grammarSimple": "「えいごのじゅぎょうで○○をするよ」→ games（ゲーム）！",
                    "choiceAnalysis": [
                        "○ games＝ゲーム。play games で「ゲームをする」。",
                        "phones＝電話。",
                        "clocks＝時計。",
                        "cameras＝カメラ。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「ゲーム」がぴったり！",
                        "「でんわ」はちがうよ。",
                        "「とけい」はちがうよ。",
                        "「カメラ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q4.mp3",
                    "translation": "生徒たちはブラウン先生の英語の授業でよく（　）をする。",
                    "choiceTranslations": ["ゲーム", "電話", "時計", "カメラ"]
                },
                {
                    "number": 5,
                    "text": "Alice eats toast for (　).",
                    "choices": ["newspaper", "breakfast", "music", "snow"],
                    "answer": 2,
                    "grammar": "「アリスは○○にトーストを食べる」→ breakfast（朝食）。for breakfast＝朝食に。",
                    "grammarSimple": "「○○にトーストをたべるよ」→ breakfast（あさごはん）！",
                    "choiceAnalysis": [
                        "newspaper＝新聞。",
                        "○ breakfast＝朝食。for breakfast で「朝食に」。",
                        "music＝音楽。",
                        "snow＝雪。"
                    ],
                    "choiceAnalysisSimple": [
                        "「しんぶん」はちがうよ。",
                        "○「あさごはん」がぴったり！",
                        "「おんがく」はちがうよ。",
                        "「ゆき」はちがうよ。"
                    ],
                    "questionAudio": "audio/q5.mp3",
                    "translation": "アリスは（　）にトーストを食べる。",
                    "choiceTranslations": ["新聞", "朝食", "音楽", "雪"]
                },
                {
                    "number": 6,
                    "text": "Jessica is a big (　) of her hometown's soccer team.",
                    "choices": ["fan", "table", "mountain", "box"],
                    "answer": 1,
                    "grammar": "「ジェシカは地元のサッカーチームの大○○だ」→ fan（ファン）。a big fan of＝～の大ファン。",
                    "grammarSimple": "「じもとのサッカーチームの○○だよ」→ fan（ファン）！",
                    "choiceAnalysis": [
                        "○ fan＝ファン。a big fan of で「～の大ファン」。",
                        "table＝テーブル。",
                        "mountain＝山。",
                        "box＝箱。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「ファン」がぴったり！",
                        "「テーブル」はちがうよ。",
                        "「やま」はちがうよ。",
                        "「はこ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q6.mp3",
                    "translation": "ジェシカは地元のサッカーチームの大（　）だ。",
                    "choiceTranslations": ["ファン", "テーブル", "山", "箱"]
                },
                {
                    "number": 7,
                    "text": "Look at that red (　). It's swimming very fast.",
                    "choices": ["ball", "flower", "fish", "river"],
                    "answer": 3,
                    "grammar": "「あの赤い○○を見て。とても速く泳いでいるよ」→ fish（魚）。泳いでいるもの＝魚。",
                    "grammarSimple": "「あのあかい○○をみて！はやくおよいでいるよ」→ fish（さかな）！",
                    "choiceAnalysis": [
                        "ball＝ボール。泳がない。",
                        "flower＝花。泳がない。",
                        "○ fish＝魚。泳いでいるのは魚。",
                        "river＝川。川は泳がない。"
                    ],
                    "choiceAnalysisSimple": [
                        "「ボール」はおよがないよ。",
                        "「はな」はおよがないよ。",
                        "○「さかな」がぴったり！",
                        "「かわ」はおよがないよ。"
                    ],
                    "questionAudio": "audio/q7.mp3",
                    "translation": "あの赤い（　）を見て。とても速く泳いでいるよ。",
                    "choiceTranslations": ["ボール", "花", "魚", "川"]
                },
                {
                    "number": 8,
                    "text": "A: Bye, Brenda. (　) a nice day.\nB: Thanks.",
                    "choices": ["Eat", "Go", "Come", "Have"],
                    "answer": 4,
                    "grammar": "「バイバイ、ブレンダ。○○良い一日を」→ Have（過ごしてね）。Have a nice day.＝良い一日を。",
                    "grammarSimple": "「○○よいいちにちを！」→ Have！「ハヴ ア ナイス デイ」！",
                    "choiceAnalysis": [
                        "Eat＝食べる。",
                        "Go＝行く。",
                        "Come＝来る。",
                        "○ Have＝過ごす。Have a nice day.は挨拶の定型表現。"
                    ],
                    "choiceAnalysisSimple": [
                        "「たべる」はちがうよ。",
                        "「いく」はちがうよ。",
                        "「くる」はちがうよ。",
                        "○「Have a nice day!」はおきまりのことば！"
                    ],
                    "questionAudio": "audio/q8.mp3",
                    "translation": "A: バイバイ、ブレンダ。（　）良い一日を。\nB: ありがとう。",
                    "choiceTranslations": ["食べなさい", "行きなさい", "来なさい", "過ごしなさい"]
                },
                {
                    "number": 9,
                    "text": "A: Are you from England, Katie?\nB: That's (　). I'm from London.",
                    "choices": ["well", "little", "right", "happy"],
                    "answer": 3,
                    "grammar": "「イギリス出身ですか？」「その通りです。ロンドン出身です」→ right（正しい）。That's right.＝その通りです。",
                    "grammarSimple": "「そのとおり！」→ right（ただしい）！",
                    "choiceAnalysis": [
                        "well＝元気・上手に。",
                        "little＝小さい。",
                        "○ right＝正しい。That's right.＝「その通りです」。",
                        "happy＝幸せな。"
                    ],
                    "choiceAnalysisSimple": [
                        "「げんき」はちがうよ。",
                        "「ちいさい」はちがうよ。",
                        "○「そのとおり！」がぴったり！",
                        "「しあわせ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q9.mp3",
                    "translation": "A: イギリス出身ですか、ケイティ？\nB: その（　）です。ロンドン出身です。",
                    "choiceTranslations": ["元気な", "小さい", "正しい", "幸せな"]
                },
                {
                    "number": 10,
                    "text": "Kelly often talks (　) her future dream.",
                    "choices": ["about", "by", "from", "under"],
                    "answer": 1,
                    "grammar": "「ケリーはよく将来の夢○○話す」→ about（について）。talk about＝～について話す。",
                    "grammarSimple": "「しょうらいのゆめ○○はなすよ」→ about（について）！",
                    "choiceAnalysis": [
                        "○ about＝～について。talk about で「～について話す」。",
                        "by＝～のそばに・～によって。",
                        "from＝～から。",
                        "under＝～の下に。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「について」がぴったり！",
                        "「～のそばに」はちがうよ。",
                        "「～から」はちがうよ。",
                        "「～のしたに」はちがうよ。"
                    ],
                    "questionAudio": "audio/q10.mp3",
                    "translation": "ケリーはよく将来の夢（　）話す。",
                    "choiceTranslations": ["〜について", "〜のそばに", "〜から", "〜の下に"]
                },
                {
                    "number": 11,
                    "text": "Yoshiko sometimes does her homework (　) night.",
                    "choices": ["at", "off", "for", "to"],
                    "answer": 1,
                    "grammar": "「よし子は時々夜○○宿題をする」→ at（に）。at night＝夜に。",
                    "grammarSimple": "「よるに○○しゅくだいをするよ」→ at！「at night」＝「よるに」！",
                    "choiceAnalysis": [
                        "○ at＝～に。at night で「夜に」。",
                        "off＝離れて。",
                        "for＝～のために。",
                        "to＝～へ。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「at night」で「よるに」！",
                        "「はなれて」はちがうよ。",
                        "「～のために」はちがうよ。",
                        "「～へ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q11.mp3",
                    "translation": "よし子は時々（　）夜に宿題をする。",
                    "choiceTranslations": ["〜に", "離れて", "〜のために", "〜へ"]
                },
                {
                    "number": 12,
                    "text": "Megumi is 13 (　) old. She's a junior high school student.",
                    "choices": ["fruits", "years", "hands", "girls"],
                    "answer": 2,
                    "grammar": "「めぐみは13○○だ。中学生だ」→ years（歳）。13 years old＝13歳。",
                    "grammarSimple": "「13○○！ちゅうがくせいだよ」→ years（さい）！",
                    "choiceAnalysis": [
                        "fruits＝果物。",
                        "○ years＝年・歳。13 years old で「13歳」。",
                        "hands＝手。",
                        "girls＝女の子。"
                    ],
                    "choiceAnalysisSimple": [
                        "「くだもの」はちがうよ。",
                        "○「さい」がぴったり！",
                        "「て」はちがうよ。",
                        "「おんなのこ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q12.mp3",
                    "translation": "めぐみは13（　）だ。中学生だ。",
                    "choiceTranslations": ["果物", "歳", "手", "女の子"]
                },
                {
                    "number": 13,
                    "text": "A: Dad, please help (　). Today's homework is very hard.\nB: OK.",
                    "choices": ["I", "my", "me", "mine"],
                    "answer": 3,
                    "grammar": "「お父さん、○○を手伝って。今日の宿題はとても難しいの」→ me（私を）。help me＝私を助けて。",
                    "grammarSimple": "「○○をてつだって！」→ me（わたしを）！",
                    "choiceAnalysis": [
                        "I＝私は（主格）。動詞の後に置けない。",
                        "my＝私の（所有格）。",
                        "○ me＝私を（目的格）。help me で「私を助けて」。",
                        "mine＝私のもの（所有代名詞）。"
                    ],
                    "choiceAnalysisSimple": [
                        "「わたしは」はちがうよ。",
                        "「わたしの」はちがうよ。",
                        "○「わたしを」がぴったり！",
                        "「わたしのもの」はちがうよ。"
                    ],
                    "questionAudio": "audio/q13.mp3",
                    "translation": "A: お父さん、（　）を手伝って。今日の宿題はとても難しいの。\nB: わかった。",
                    "choiceTranslations": ["私は", "私の", "私を", "私のもの"]
                },
                {
                    "number": 14,
                    "text": "A: Cathy, (　) are you doing?\nB: I'm writing a letter to my friend.",
                    "choices": ["whose", "what", "when", "who"],
                    "answer": 2,
                    "grammar": "「キャシー、○○しているの？」「友達に手紙を書いているの」→ what（何を）。What are you doing?＝何をしていますか。",
                    "grammarSimple": "「○○してるの？」→ what（なにを）！",
                    "choiceAnalysis": [
                        "whose＝誰の。",
                        "○ what＝何を。What are you doing? は定型表現。",
                        "when＝いつ。",
                        "who＝誰。"
                    ],
                    "choiceAnalysisSimple": [
                        "「だれの」はちがうよ。",
                        "○「なにを」がぴったり！",
                        "「いつ」はちがうよ。",
                        "「だれ」はちがうよ。"
                    ],
                    "questionAudio": "audio/q14.mp3",
                    "translation": "A: キャシー、（　）しているの？\nB: 友達に手紙を書いているの。",
                    "choiceTranslations": ["誰の", "何を", "いつ", "誰が"]
                },
                {
                    "number": 15,
                    "text": "My sister and I (　) dinner every Sunday.",
                    "choices": ["cook", "cooks", "cooking", "to cook"],
                    "answer": 1,
                    "grammar": "「姉と私は毎週日曜日に夕食を○○」→ cook（料理する）。主語が複数（My sister and I）なので原形。",
                    "grammarSimple": "「まいしゅうにちようびにゆうしょくを○○」→ cook（りょうりする）！",
                    "choiceAnalysis": [
                        "○ cook＝料理する（原形）。主語が複数なので三単現のsは不要。",
                        "cooks＝三単現のs付き。主語は複数なので不可。",
                        "cooking＝動名詞/現在分詞。文法的に不可。",
                        "to cook＝不定詞。文法的に不可。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「りょうりする」がぴったり！2人いるから cook！",
                        "「cooks」は1人のときだよ。",
                        "「cooking」だけだとぶんにならないよ。",
                        "「to cook」だけだとぶんにならないよ。"
                    ],
                    "questionAudio": "audio/q15.mp3",
                    "translation": "姉と私は毎週日曜日に夕食を（　）。",
                    "choiceTranslations": ["料理する", "料理する（三単現）", "料理すること", "料理するために"]
                }
            ]
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "conversation",
            "instruction": "次の(16)から(20)までの会話について，（　）に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",
            "questions": [
                {
                    "number": 16,
                    "text": "Teacher: Where do you usually play baseball, Jack?\nBoy: (　) Mr. Parker.",
                    "choices": ["In the morning,", "Goodbye,", "You're here,", "Near my house,"],
                    "answer": 4,
                    "grammar": "「どこで野球をしますか？」→場所を答える。Near my house＝家の近くで。",
                    "grammarSimple": "「どこでやきゅうするの？」→「いえのちかくで」！",
                    "choiceAnalysis": [
                        "In the morning＝朝に。時間であって場所ではない。",
                        "Goodbye＝さようなら。質問への答えにならない。",
                        "You're here＝あなたはここにいます。答えとして不自然。",
                        "○ Near my house＝家の近くで。場所を答えている。"
                    ],
                    "choiceAnalysisSimple": [
                        "「あさに」はばしょじゃないよ。",
                        "「さようなら」はへんだよ。",
                        "「あなたはここ」はへんだよ。",
                        "○「いえのちかくで」がぴったり！"
                    ],
                    "questionAudio": "audio/q16.mp3",
                    "translation": "先生: ジャック、ふだんどこで野球をしますか？\n男の子: （　）パーカー先生。",
                    "choiceTranslations": ["朝に、", "さようなら、", "あなたはここにいます、", "家の近くで、"]
                },
                {
                    "number": 17,
                    "text": "Girl: Mom, let's go to the shopping mall.\nMother: I'm busy now. (　)\nGirl: OK.",
                    "choices": ["How about this afternoon?", "Is that your bag?", "Which color do you like?", "Who can go with you?"],
                    "answer": 1,
                    "grammar": "「買い物に行こうよ」「今忙しいの。○○」「わかった」→ 代替案を提示。How about this afternoon?＝午後はどう？",
                    "grammarSimple": "「いまいそがしいの。○○」→「ごごはどう？」！",
                    "choiceAnalysis": [
                        "○ How about this afternoon?＝午後はどう？忙しい今の代わりに提案。",
                        "Is that your bag?＝あれはあなたのバッグ？文脈に合わない。",
                        "Which color do you like?＝何色が好き？文脈に合わない。",
                        "Who can go with you?＝誰と行ける？不自然。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「ごごはどう？」がぴったり！",
                        "「あれはカバン？」はへんだよ。",
                        "「なにいろがすき？」はへんだよ。",
                        "「だれといける？」はへんだよ。"
                    ],
                    "questionAudio": "audio/q17.mp3",
                    "translation": "女の子: お母さん、ショッピングモールに行こうよ。\nお母さん: 今忙しいの。（　）\n女の子: わかった。",
                    "choiceTranslations": ["午後はどう？", "あれはあなたのカバン？", "何色が好き？", "誰と行ける？"]
                },
                {
                    "number": 18,
                    "text": "Father: Do you know those boys over there, Fred?\nBoy: Yes, Dad. (　)",
                    "choices": ["We're going home now.", "I can't see them.", "They're my friends.", "It's for school."],
                    "answer": 3,
                    "grammar": "「あそこの男の子たち知ってる？」「うん。○○」→ They're my friends.＝彼らは友達だよ。",
                    "grammarSimple": "「あのこたちしってる？」「うん。○○」→「ともだちだよ！」",
                    "choiceAnalysis": [
                        "We're going home now.＝今帰るところ。質問と関係ない。",
                        "I can't see them.＝彼らが見えない。知っているのに見えないは矛盾。",
                        "○ They're my friends.＝彼らは友達だ。知っている理由。",
                        "It's for school.＝それは学校用。文脈に合わない。"
                    ],
                    "choiceAnalysisSimple": [
                        "「いまかえるよ」はへんだよ。",
                        "「みえない」はへんだよ。",
                        "○「ともだちだよ！」がぴったり！",
                        "「がっこうのだよ」はへんだよ。"
                    ],
                    "questionAudio": "audio/q18.mp3",
                    "translation": "お父さん: あそこの男の子たち知ってる、フレッド？\n男の子: うん、お父さん。（　）",
                    "choiceTranslations": ["今帰るところだよ。", "彼らが見えないよ。", "彼らは友達だよ。", "それは学校用だよ。"]
                },
                {
                    "number": 19,
                    "text": "Girl: Can I use your dictionary, Eddie?\nBoy: (　) I'm using it now.",
                    "choices": ["I'm sorry.", "You're OK.", "I'm 150 cm.", "It's for you."],
                    "answer": 1,
                    "grammar": "「辞書を使ってもいい？」「○○今使っているの」→ I'm sorry.＝ごめんなさい。断っている。",
                    "grammarSimple": "「じしょかしてもいい？」「○○いまつかってるの」→「ごめんね」！",
                    "choiceAnalysis": [
                        "○ I'm sorry.＝ごめんなさい。今使っているので貸せない。",
                        "You're OK.＝あなたは大丈夫。不自然。",
                        "I'm 150 cm.＝身長150cm。文脈に合わない。",
                        "It's for you.＝あなたのためのもの。不自然。"
                    ],
                    "choiceAnalysisSimple": [
                        "○「ごめんね」がぴったり！",
                        "「だいじょうぶだよ」はへんだよ。",
                        "「150センチだよ」はへんだよ。",
                        "「あなたのだよ」はへんだよ。"
                    ],
                    "questionAudio": "audio/q19.mp3",
                    "translation": "女の子: エディ、辞書を使ってもいい？\n男の子: （　）今使っているの。",
                    "choiceTranslations": ["ごめんなさい。", "あなたは大丈夫。", "身長150cmです。", "あなたのためのものです。"]
                },
                {
                    "number": 20,
                    "text": "Girl: Dad, I can't find my red pen.\nFather: Look. (　)",
                    "choices": ["That's nice.", "It has five colors.", "It's on the table.", "Let's go after lunch."],
                    "answer": 3,
                    "grammar": "「赤いペンが見つからない」「見て。○○」→ It's on the table.＝テーブルの上にあるよ。場所を教えている。",
                    "grammarSimple": "「ペンがない！」「みて。○○」→「テーブルのうえだよ」！",
                    "choiceAnalysis": [
                        "That's nice.＝いいね。ペンを探している場面に不適切。",
                        "It has five colors.＝5色ある。文脈に合わない。",
                        "○ It's on the table.＝テーブルの上にある。場所を教えている。",
                        "Let's go after lunch.＝昼食後に行こう。文脈に合わない。"
                    ],
                    "choiceAnalysisSimple": [
                        "「いいね」はへんだよ。",
                        "「5いろあるよ」はへんだよ。",
                        "○「テーブルのうえだよ」がぴったり！",
                        "「おひるのあといこう」はへんだよ。"
                    ],
                    "questionAudio": "audio/q20.mp3",
                    "translation": "女の子: お父さん、赤いペンが見つからないの。\nお父さん: 見て。（　）",
                    "choiceTranslations": ["いいね。", "5色あるよ。", "テーブルの上にあるよ。", "昼食後に行こう。"]
                }
            ]
        },
        {
            "name": "大問3",
            "nameEn": "Part 3",
            "type": "sentence-order",
            "instruction": "次の(21)から(25)までの日本文の意味を表すように①から④までを並べかえて（　）の中に入れなさい。そして，1番目と3番目にくるものの最も適切な組合せを1，2，3，4の中から一つ選び，その番号のマーク欄をぬりつぶしなさい。",
            "questions": [
                {
                    "number": 21,
                    "text": "ジュディ，あなたのお姉さんはどうやってピアノを練習しますか。",
                    "framePrefix": "Judy,",
                    "frameSuffix": "the piano?",
                    "words": ["practice", "how", "your sister", "does"],
                    "correctOrder": [2, 4, 3, 1],
                    "answer": 4,
                    "answerSlots": [1, 3],
                    "grammar": "疑問詞 how を使った疑問文。How does your sister practice the piano? 語順: 疑問詞+助動詞+主語+動詞。",
                    "grammarSimple": "「どうやって？」は how！ How does your sister practice...？",
                    "choiceAnalysis": [
                        "③ ─ ④: your sister – does → 語順が違う。",
                        "① ─ ③: practice – your sister → 語順が違う。",
                        "② ─ ①: how – practice → does と主語が抜ける。",
                        "○ ② ─ ③: how – your sister → Judy, how does your sister practice the piano?"
                    ],
                    "choiceAnalysisSimple": [
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "○ Judy, how does your sister practice the piano？"
                    ],
                    "questionAudio": "audio/q21.mp3",
                    "translation": "ジュディ，あなたのお姉さんはどうやってピアノを練習しますか。"
                },
                {
                    "number": 22,
                    "text": "私はいつも朝6時に起きます。",
                    "framePrefix": "I always",
                    "frameSuffix": "in the morning.",
                    "words": ["up", "get", "six", "at"],
                    "correctOrder": [2, 1, 4, 3],
                    "answer": 3,
                    "answerSlots": [1, 3],
                    "grammar": "get up＝起きる、at six＝6時に。I always get up at six in the morning.",
                    "grammarSimple": "「おきる」は get up！「6じに」は at six！",
                    "choiceAnalysis": [
                        "③ ─ ②: six – get → 語順が違う。",
                        "④ ─ ①: at – up → 語順が違う。",
                        "○ ② ─ ④: get – at → I always get up at six in the morning.",
                        "① ─ ②: up – get → 語順が逆。"
                    ],
                    "choiceAnalysisSimple": [
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "○ I always get up at six in the morning.！",
                        "じゅんばんがちがうよ。"
                    ],
                    "questionAudio": "audio/q22.mp3",
                    "translation": "私はいつも朝6時に起きます。"
                },
                {
                    "number": 23,
                    "text": "私たちは毎日，教室を掃除します。",
                    "framePrefix": "",
                    "frameSuffix": "every day.",
                    "words": ["clean", "classroom", "our", "we"],
                    "correctOrder": [4, 1, 3, 2],
                    "answer": 2,
                    "answerSlots": [1, 3],
                    "grammar": "We clean our classroom every day. 主語+動詞+目的語の基本語順。",
                    "grammarSimple": "「わたしたちは」は We！「きょうしつをそうじする」は clean our classroom！",
                    "choiceAnalysis": [
                        "② ─ ①: classroom – clean → 語順が違う。",
                        "○ ④ ─ ③: we – our → We clean our classroom every day.",
                        "① ─ ③: clean – our → 主語がない。",
                        "② ─ ④: classroom – we → 語順が違う。"
                    ],
                    "choiceAnalysisSimple": [
                        "じゅんばんがちがうよ。",
                        "○ We clean our classroom every day.！",
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。"
                    ],
                    "questionAudio": "audio/q23.mp3",
                    "translation": "私たちは毎日，教室を掃除します。"
                },
                {
                    "number": 24,
                    "text": "窓を閉めてくれますか。",
                    "framePrefix": "",
                    "frameSuffix": ", please?",
                    "words": ["you", "close", "can", "the window"],
                    "correctOrder": [3, 1, 2, 4],
                    "answer": 1,
                    "answerSlots": [1, 3],
                    "grammar": "Can you close the window, please? 依頼のCan you...?の語順。",
                    "grammarSimple": "「～してくれる？」は Can you...？",
                    "choiceAnalysis": [
                        "○ ③ ─ ②: can – close → Can you close the window, please?",
                        "③ ─ ①: can – you → close が3番目に来ない。",
                        "④ ─ ①: the window – you → 語順が違う。",
                        "④ ─ ③: the window – can → 語順が違う。"
                    ],
                    "choiceAnalysisSimple": [
                        "○ Can you close the window, please？",
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。"
                    ],
                    "questionAudio": "audio/q24.mp3",
                    "translation": "窓を閉めてくれますか。"
                },
                {
                    "number": 25,
                    "text": "鈴木先生と歩いているのはだれですか。",
                    "framePrefix": "",
                    "frameSuffix": "Mr. Suzuki?",
                    "words": ["walking", "is", "with", "who"],
                    "correctOrder": [4, 2, 1, 3],
                    "answer": 4,
                    "answerSlots": [1, 3],
                    "grammar": "Who is walking with Mr. Suzuki? 現在進行形の疑問文。疑問詞+be動詞+動詞ing。",
                    "grammarSimple": "「だれがあるいているの？」は Who is walking...？",
                    "choiceAnalysis": [
                        "③ ─ ②: with – is → 語順が違う。",
                        "① ─ ③: walking – with → 主語がない。",
                        "② ─ ③: is – with → walking が抜ける。",
                        "○ ④ ─ ①: who – walking → Who is walking with Mr. Suzuki?"
                    ],
                    "choiceAnalysisSimple": [
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "じゅんばんがちがうよ。",
                        "○ Who is walking with Mr. Suzuki？"
                    ],
                    "questionAudio": "audio/q25.mp3",
                    "translation": "鈴木先生と歩いているのはだれですか。"
                }
            ]
        }
    ],
    "vocabulary": [],
    "lessonPlan": {}
}

out_path = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade5\2023-1\data.json"
import os
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"✅ data.json generated: {os.path.getsize(out_path)} bytes")
print(f"   Sections: {len(data['sections'])}")
for s in data['sections']:
    print(f"   - {s['name']} ({s['type']}): {len(s['questions'])} questions")
