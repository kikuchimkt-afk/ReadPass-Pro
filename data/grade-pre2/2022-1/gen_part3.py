"""Generate lessonPlan with 5 focusPoints for Pre-Grade 2 2022-1"""
import json, os
base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-1"
data = json.load(open(os.path.join(base, "_part2.json"), "r", encoding="utf-8"))

# 2022-1で使える新トピック: 使役動詞let/make, 知覚動詞, 現在完了進行形, 関係代名詞that(後置修飾), be worth ~ing / look forward to ~ing

data["lessonPlan"] = {"focusPoints": [
    {
        "id":"fp1","title":"使役動詞 let の用法","subtitle":"Causative Verb: let + O + V",
        "explanation":"let + 目的語 + 動詞原形で「Oに～させる（許可する）」を表します。make + O + V（強制）やhave + O + V（依頼）と区別しましょう。",
        "sourceQuote":"Rick's mom would not let him watch TV","sourceLocation":"Part 1 Q19",
        "examples":[
            {"en":"Rick's mom would not let him watch TV until he had finished cleaning his room.","ja":"リックの母親は部屋の掃除を終えるまでテレビを見させなかった。","note":"let + him + watch（原形）= 見ることを許可する"},
            {"en":"Please let me check, Mr. Mason.","ja":"確認させてください、メイソン様。","note":"let + me + check = 確認させてください"},
            {"en":"Let me know if you're interested.","ja":"興味があったら教えてね。","note":"let + me + know = 知らせてね"}
        ],
        "practicePassage":{
            "en":"[出典: Visit to Museum 第3段落]\nMy mom says there is a natural history museum here in Chicago, too. She said that she would take you, me, and my brother there when you come to visit the United States next month. We can spend the whole day at the museum if we go early. Let me know if you're interested. I can't wait to see you!",
            "ja":"ママがシカゴにも自然史博物館があるって言ってた。来月あなたがアメリカに来る時、私たちを連れて行ってくれるって。早く行けば一日中博物館で過ごせるよ。興味があったら教えてね。会えるのが待ちきれない！",
            "audioFile":"audio/practice_pp1.mp3"
        },
        "practiceQuestions":[
            {"q":"「let him watch」の watch が原形なのはなぜ？","a":"let は使役動詞で、let + O + 原形の形を取る。to watch とはしない"},
            {"q":"「Let me check」を丁寧に言い換えると？","a":"Could you let me check? / May I check?"},
            {"q":"let と make の違いは？","a":"let＝許可（させてあげる）、make＝強制（させる）。She let me go.（行かせてくれた）vs She made me go.（行かせた）"},
            {"q":"「Let me know」はどんな場面で使いますか？","a":"相手に情報を教えてほしい時の定番表現。= Please tell me"}
        ],
        "highlightPatterns":[
            "Let me know if you're interested",
            "She said that she would take you, me, and my brother there when you come to visit the United States next month",
            "Please let me check, Mr. Mason"
        ],
        "highlightColor":"#4f8cff","highlightLabel":"使役動詞"
    },
    {
        "id":"fp2","title":"現在完了進行形 have been ~ing","subtitle":"Present Perfect Continuous",
        "explanation":"have been ～ingは「（過去から今まで）ずっと～している」を表します。動作の継続を強調する表現です。現在完了形（have + 過去分詞）が結果や経験を表すのに対し、進行形は動作そのものの継続に焦点を当てます。",
        "sourceQuote":"Hiroko and three of her friends have been working on a project","sourceLocation":"Part 3A 第1段落",
        "examples":[
            {"en":"Hiroko and three of her friends have been working on a project for school.","ja":"ヒロコと3人の友達は学校のプロジェクトに取り組んでいる。","note":"have been working = ずっと取り組んでいる（継続）"},
            {"en":"They have been doing research on the history of their town.","ja":"町の歴史について調査を行っている。","note":"have been doing = ずっと行っている"},
            {"en":"Every day after school, they have been getting together in the school library.","ja":"放課後毎日、学校の図書館に集まっている。","note":"have been getting together = ずっと集まっている"}
        ],
        "practicePassage":{
            "en":"[出典: Good Friends 第1段落]\nHiroko and three of her friends have been working on a project for school. They have been doing research on the history of their town, and they must give a presentation about it in class next week. Every day after school, they have been getting together in the school library. They have been discussing what information to use and how to make a great presentation. They had some good ideas, and they were looking forward to talking in front of their classmates.",
            "ja":"ヒロコと3人の友達は学校のプロジェクトに取り組んでいる。町の歴史について調査を行い、来週クラスで発表しなければならない。放課後毎日、学校の図書館に集まっている。どの情報を使うか、どうすれば素晴らしい発表ができるかを話し合ってきた。良いアイデアがあり、クラスメートの前で話すのを楽しみにしていた。",
            "audioFile":"audio/practice_pp2.mp3"
        },
        "practiceQuestions":[
            {"q":"「have been working」と「have worked」の違いは？","a":"have been working＝今も続いている動作の継続を強調。have worked＝完了・結果を強調"},
            {"q":"「have been getting together」はどんな意味？","a":"（過去から今まで）ずっと集まり続けている。every dayと相まって習慣的な継続を表す"},
            {"q":"現在完了進行形が使えない動詞は？","a":"状態動詞（know, like, believe, belong等）は進行形にできない"},
            {"q":"「They have been discussing」を過去形にすると？","a":"They were discussing / They discussed（過去の時点での継続動作）"}
        ],
        "highlightPatterns":[
            "Hiroko and three of her friends have been working on a project for school",
            "They have been doing research on the history of their town",
            "they have been getting together in the school library",
            "They have been discussing what information to use"
        ],
        "highlightColor":"#34d399","highlightLabel":"現在完了進行形"
    },
    {
        "id":"fp3","title":"知覚動詞 watch / see + O + 原形/~ing","subtitle":"Perception Verbs with Object Complement",
        "explanation":"watch, see, hear, feelなどの知覚動詞は「O + 原形」（動作の全体）または「O + ～ing」（動作の途中）の形を取ります。知覚動詞の後にto不定詞は使いません。",
        "sourceQuote":"museum visitors can watch them","sourceLocation":"Part 4A 第2段落",
        "examples":[
            {"en":"Museum visitors can watch them.","ja":"来館者は彼ら（科学者）を見学できる。","note":"watch + them（目的語）= 彼らが作業するのを見る"},
            {"en":"Emma enjoyed watching the sun go down and the stars come out.","ja":"エマは夕日が沈み星が出るのを見て楽しんだ。","note":"watch + the sun + go down = 太陽が沈むのを見る（知覚動詞+O+原形）"},
            {"en":"I think that watching fish swim can be very relaxing.","ja":"魚が泳ぐのを見るのはとてもリラックスできると思う。","note":"watching + fish + swim = 魚が泳ぐのを見ること"}
        ],
        "practicePassage":{
            "en":"[出典: Visit to Museum 第2段落]\nOne day, it rained, so we decided to go into the city and see the natural history museum there. The museum was cool because it has many dinosaur bones. It also has an amazing collection of colorful rocks. My favorite part was the \"PaleoLab,\" though. There, scientists prepare old bones from dinosaurs and other animals for the museum. The scientists work in a special room with a large window, so museum visitors can watch them.",
            "ja":"ある日雨が降ったので、街に行って自然史博物館を見ることにした。恐竜の骨がたくさんあってすごかった。色とりどりの石のコレクションも素晴らしかった。でも一番好きだったのは「パレオラボ」。そこでは科学者が恐竜や他の動物の古い骨を博物館用に準備している。大きな窓のある特別な部屋で作業するから、来館者は見学できる。",
            "audioFile":"audio/practice_pp3.mp3"
        },
        "practiceQuestions":[
            {"q":"「watch the sun go down」でなぜ go は原形？","a":"知覚動詞watch + O + 原形の形。to go とはしない。動作の始まりから終わりまでを見る意味"},
            {"q":"「watching fish swim」と「watching fish swimming」の違いは？","a":"swim（原形）= 泳ぐ行為の全体。swimming（～ing）= 泳いでいる途中の様子"},
            {"q":"知覚動詞が受動態になるとどう変わる？","a":"原形がto不定詞に変わる。I saw him run. → He was seen to run."},
            {"q":"「see the natural history museum」のseeは知覚動詞ですか？","a":"ここでは「見に行く＝訪問する」の意味で、知覚動詞ではなく一般動詞"}
        ],
        "highlightPatterns":[
            "museum visitors can watch them",
            "watching the sun go down and the stars come out",
            "watching fish swim can be very relaxing"
        ],
        "highlightColor":"#f472b6","highlightLabel":"知覚動詞"
    },
    {
        "id":"fp4","title":"動名詞を取る重要表現","subtitle":"Key Expressions Followed by Gerunds",
        "explanation":"be worth ～ing（～する価値がある）、look forward to ～ing（～するのを楽しみにする）、feel like ～ing（～したい気分だ）など、動名詞（-ing形）を取る重要表現があります。to の後でも動名詞を使う点に注意しましょう。",
        "sourceQuote":"It was worth visiting","sourceLocation":"Part 1 Q20",
        "examples":[
            {"en":"They were looking forward to talking in front of their classmates.","ja":"クラスメートの前で話すのを楽しみにしていた。","note":"look forward to ～ing = ～するのを楽しみにする（toの後に動名詞）"},
            {"en":"She was sorry for not being able to do anything more.","ja":"これ以上何もできなくて申し訳なく思った。","note":"be sorry for ～ing = ～して申し訳なく思う"},
            {"en":"These people are afraid of entering army training centers.","ja":"軍の訓練施設に入ることを恐れている。","note":"be afraid of ～ing = ～するのを恐れる"}
        ],
        "practicePassage":{
            "en":"[出典: Good Friends 第2段落]\nHowever, Hiroko broke her leg during volleyball practice yesterday. Now, she must stay in the hospital for five days. She called her friends and said that she was sorry for not being able to do anything more to help them with the presentation. They told her not to worry. They said that their teacher is going to make a video of their presentation. That way, Hiroko will be able to watch it afterwards. Hiroko thanked her friends and wished them good luck.",
            "ja":"しかし、ヒロコは昨日バレーボールの練習中に足を骨折した。今、5日間入院しなければならない。友達に電話して、発表の手伝いがもうできなくて申し訳ないと言った。友達は心配しないでと言った。先生が発表のビデオを撮ってくれるから、ヒロコも後で見ることができると言った。ヒロコは友達に感謝し、幸運を祈った。",
            "audioFile":"audio/practice_pp4.mp3"
        },
        "practiceQuestions":[
            {"q":"「look forward to」の to の後になぜ動名詞？","a":"この to は前置詞（不定詞のtoではない）。前置詞の後には名詞/動名詞が来る"},
            {"q":"「be sorry for not being able to」の構造は？","a":"be sorry for + 動名詞。notが動名詞の前に付いて否定を表す"},
            {"q":"「be afraid of entering」を be afraid to enter と言い換え可能？","a":"ほぼ同じだが、be afraid of ～ingは恐れの感情、be afraid to ～は恐れて行動しないニュアンス"},
            {"q":"他に「前置詞+動名詞」のパターンを挙げてみましょう","a":"be good at ～ing, be interested in ～ing, thank you for ～ing, insist on ～ing"}
        ],
        "highlightPatterns":[
            "they were looking forward to",
            "she was sorry for not being able to do anything more",
            "these people are afraid of entering army training centers"
        ],
        "highlightColor":"#fbbf24","highlightLabel":"動名詞表現"
    },
    {
        "id":"fp5","title":"原因・理由を示す構文パターン","subtitle":"Expressing Cause and Reason",
        "explanation":"because（～なので）、because of（～のために）、as a result（その結果）、the result was that（その結果は～だった）など、原因と結果を示す表現は読解の鍵です。",
        "sourceQuote":"The result was that there were fewer people and more safe places","sourceLocation":"Part 4B 第2段落",
        "examples":[
            {"en":"Farmers hunted wolves because they sometimes killed the farmers' sheep.","ja":"農家の羊を殺すことがあったため、農家はオオカミを狩った。","note":"because + S + V = ～なので（接続詞）"},
            {"en":"As a result, it has a unique culture.","ja":"その結果、独自の文化がある。","note":"As a result = その結果（前文の原因を受ける）"},
            {"en":"The result was that there were fewer people and more safe places for deer.","ja":"その結果、人が減りシカにとって安全な場所が増えた。","note":"The result was that ～ = その結果は～だった"}
        ],
        "practicePassage":{
            "en":"[出典: The Return of the Wolves 第2段落]\nIn the 1980s and 1990s, European countries made laws to protect wildlife and created special areas for wild animals. At the same time, many people left their farms in eastern Europe to take jobs abroad. The result was that there were fewer people and more safe places for deer and other animals that wolves like to eat. As the number of these animals increased, the number of wolves increased, too. The wolves spread west, and in 2001, they were found living in Germany again.",
            "ja":"1980年代と1990年代、ヨーロッパ諸国は野生生物を守る法律を作り、特別区域を作った。同時に、東ヨーロッパでは多くの人が海外で仕事をするために農場を離れた。その結果、人が少なくなり、オオカミが好むシカなどの動物にとって安全な場所が増えた。これらの動物の数が増えると、オオカミの数も増えた。オオカミは西に広がり、2001年にドイツで再び見つかった。",
            "audioFile":"audio/practice_pp5.mp3"
        },
        "practiceQuestions":[
            {"q":"「because」と「because of」の違いは？","a":"because + S + V（節）、because of + 名詞（句）。Because it rained. / Because of the rain."},
            {"q":"「The result was that ～」を「As a result」で言い換えると？","a":"As a result, there were fewer people and more safe places."},
            {"q":"「As the number increased, the number of wolves increased, too」はどんな因果関係？","a":"As ～ = ～するにつれて。シカが増える→オオカミも増えるという連鎖的因果関係"},
            {"q":"本文中の原因→結果の流れをまとめると？","a":"法律制定＋農場離れ→人が減る→シカが増える→オオカミが増える→ドイツに戻る"}
        ],
        "highlightPatterns":[
            "farmers hunted wolves because they sometimes killed the farmers' sheep",
            "As a result, it has a unique culture",
            "The result was that there were fewer people and more safe places for deer and other animals that wolves like to eat",
            "As the number of these animals increased, the number of wolves increased, too"
        ],
        "highlightColor":"#a78bfa","highlightLabel":"原因・結果"
    }
]}

# Save final data.json
with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"data.json saved. FPs: {len(data['lessonPlan']['focusPoints'])}")
for fp in data['lessonPlan']['focusPoints']:
    print(f"  {fp['id']}: {fp['title']} ({len(fp['highlightPatterns'])} patterns)")
