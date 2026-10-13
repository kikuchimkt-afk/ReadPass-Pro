# -*- coding: utf-8 -*-
"""40 source-balanced vocabulary items and five original-based lesson cards (Pre-2 2026-2, main venue).

Audio references are added later by data/grade-pre2/2026-2/_gen_tts.py.
"""
import re

# word, meaning, pos, new example, three distractors, literal source form.
# Part 1:17, Part 2:6, Part 3:6, Part 4:11.
WORDS = [
    ("roof", "屋根", "名詞", "Snow covered the roof of our house.", "四角形／ヒント／胸", "roof"),
    ("unlikely", "ありそうもない", "形容詞", "It is unlikely that the store is open this late.", "簡単な／誠実な／合図", "unlikely"),
    ("regard", "（～を…と）みなす", "動詞", "Many people regard him as a great leader.", "一時停止する／波に乗る／溶ける", "regards"),
    ("select", "選ぶ", "動詞", "Please select one answer from the list.", "悩ませる／分け合う／気づく", "select"),
    ("connect", "つなぐ", "動詞", "Connect the camera to your computer with this cable.", "生産する／探検する／打つ", "connect"),
    ("tunnel", "トンネル", "名詞", "The train passed through a long tunnel.", "ヘリコプター／海岸／砂漠", "tunnel"),
    ("suggest", "提案する", "動詞", "I suggest we take a short break.", "輸出する／想像する／取り替える", "suggest"),
    ("tightly", "しっかりと・きつく", "副詞", "Hold the rope tightly.", "かなり／無作為に／明るく", "tightly"),
    ("plate", "皿", "名詞", "She put the cake on a white plate.", "エンジン／門／道具", "plates"),
    ("inconvenience", "不便・迷惑", "名詞", "The heavy snow caused a lot of inconvenience to drivers.", "国境／観光／目的", "inconvenience"),
    ("for nothing", "むだに", "熟語", "I waited an hour for nothing because the shop was closed.", "ついに／偶然に／平均して", "for nothing"),
    ("at length", "長々と・詳しく", "熟語", "The teacher explained the rules at length.", "誤って／徒歩で／対照的に", "at length"),
    ("be responsible for", "～を担当する・～に責任がある", "熟語", "Who is responsible for cleaning this room?", "～に緊張している／～に飽きている／～をからかう", "be responsible for"),
    ("plenty of", "たくさんの", "熟語", "Drink plenty of water on hot days.", "～に詳しい／～より前に／～を確信している", "plenty of"),
    ("be caught in a shower", "にわか雨にあう", "熟語", "We were caught in a shower on the way to school.", "泳ぐことで知られる／店で見つかる／部分に分けられる", "caught in a shower"),
    ("forecast", "予報", "名詞", "I always check the weather forecast before I go hiking.", "記録／警報／気温", "forecast"),
    ("crowd", "人混み・群衆", "名詞", "A large crowd gathered in front of the station.", "行列／座席／交通量", "crowd"),
    ("audience", "観客・聴衆", "名詞", "The audience clapped after the speech.", "出演者／舞台／入場券", "audience"),
    ("instrument", "楽器", "名詞", "Can you play any musical instruments?", "指揮者／楽譜／衣装", "instruments"),
    ("avoid", "避ける", "動詞", "Try to avoid sweet drinks before bed.", "選ぶ／続ける／勧める", "avoid"),
    ("eat out", "外食する", "熟語", "We usually eat out on Sunday evenings.", "出前を取る／料理を作る／食べ残す", "eating out"),
    ("freezing", "凍えるほど寒い", "形容詞", "It was freezing outside this morning.", "蒸し暑い／涼しい／暖かい", "freezing"),
    ("shut down", "閉鎖する・停止する", "熟語", "The factory will shut down next year.", "開業する／拡大する／移転する", "shut down"),
    ("professional", "プロの", "形容詞", "He wants to become a professional soccer player.", "趣味の／初心者の／一時的な", "professional"),
    ("come true", "実現する", "熟語", "Her dream of studying abroad came true.", "あきらめる／忘れる／延期する", "come true"),
    ("confident", "自信のある", "形容詞", "She felt confident before the speech contest.", "不安な／退屈した／恥ずかしい", "confident"),
    ("talent", "才能", "名詞", "He has a talent for drawing.", "経験／努力／運", "talent"),
    ("regret", "後悔する", "動詞", "I regret not studying harder for the test.", "期待する／感謝する／自慢する", "regret"),
    ("waste", "むだにする", "動詞", "Don't waste your money on things you don't need.", "節約する／貯める／貸す", "wasted"),
    ("remind", "思い出させる", "動詞", "Please remind me to call my grandmother.", "命令する／説得する／許可する", "remind"),
    ("documentary", "ドキュメンタリー（記録作品）", "名詞", "We watched a documentary about whales.", "喜劇／アニメ／広告", "documentary"),
    ("community", "地域社会", "名詞", "The festival brings the whole community together.", "政府／会社／学校", "community"),
    ("wildlife", "野生生物", "名詞", "This national park is home to a lot of wildlife.", "家畜／植物園／ペット", "wildlife"),
    ("reservation", "予約", "名詞", "I made a reservation for dinner at seven.", "支払い／注文／招待", "reservation"),
    ("propose", "提案する", "動詞", "She proposed a new plan for the school trip.", "反対する／延期する／中止する", "proposed"),
    ("habit", "習慣", "名詞", "Reading before bed is a good habit.", "規則／趣味／目標", "habits"),
    ("fat", "脂肪", "名詞", "This kind of meat has a lot of fat.", "たんぱく質／塩分／ビタミン", "fat"),
    ("greenhouse gas", "温室効果ガス", "名詞", "Burning coal produces greenhouse gases.", "水蒸気／酸素／排水", "greenhouse gases"),
    ("gradually", "次第に", "副詞", "The weather gradually became warmer.", "突然に／一時的に／めったに", "Gradually"),
    ("complain", "不満を言う", "動詞", "He complained that the room was too cold.", "ほめる／謝る／認める", "complain"),
]


def vocabulary():
    result = []
    for n, (word, meaning, pos, example, distractors, form) in enumerate(WORDS, 1):
        result.append(dict(word=word, meaning=meaning, pos=pos, level="準2級",
                           source="大問1" if n <= 17 else "大問2" if n <= 23 else "大問3" if n <= 29 else "大問4",
                           sourceForm=form, example=example, distractors=distractors.split("／")))
    return result


def example(en, ja, note):
    return dict(en=en, ja=ja, note=note)


def lessonplan(passages):
    dream, email, meat = passages

    def quote(p, start, note):
        row = next(r for r in p["sentencePairs"] if r[0].startswith(start))
        return example(row[0], row[1], note)

    def practice(p, index):
        # One whole original paragraph; Part 3 blanks are filled with the correct answer.
        en, ja = p["paragraphs"][index], p["translations"][index]
        for q in p["questions"]:
            en = en.replace(f"( {q['number']} )", q["choices"][q["answer"] - 1])
            ja = re.sub(rf"\s*\( {q['number']} \)\s*", q["choiceTranslations"][q["answer"] - 1], ja)
        return dict(en=f"[出典: {p['title']} 第{index + 1}段落]\n{en}", ja=ja)

    fps = [
        dict(id="fp1", title="過去完了と過去完了進行形（had been training / had not come true / had met）",
             subtitle="Past Perfect and Past Perfect Progressive",
             explanation="大問3の第1段落は、過去のある時点（友人からメッセージを受け取った日）を基準に、それより前のことを過去完了で表しています。had been training hard for years は過去完了進行形で、『その時点まで何年も練習を続けていた』という意味です。her dream had not come true yet は『その時点ではまだ夢がかなっていなかった』、a friend she had met through dancing は『（それより前に）ダンスを通して知り合っていた友人』、he had gotten a job は『（知らせを聞く前に）仕事を得ていた』です。過去の基準の時点を見つけ、その前か後かを考えながら読むと、出来事の順番が整理できます。",
             sourceQuote="She had been training hard for years to become a professional dancer, but her dream had not come true yet. One day, she received a message from a friend she had met through dancing.",
             sourceLocation="大問3「A Dream」第1段落", highlightLabel="過去完了", highlightColor="#4f8cff",
             examples=[quote(dream, "She had been training hard", "had been training は過去完了進行形。過去の時点まで練習が続いていたことを表す。"),
                       example("I had been waiting for an hour when the bus finally came.", "バスがようやく来たとき、私は1時間待ち続けていた。", "バスが来た時点まで待つことが続いていた。"),
                       example("When I arrived, the movie had already started.", "私が着いたとき、映画はすでに始まっていた。", "着いた時点より前に映画が始まっていたので had started。")],
             practicePassage=practice(dream, 0),
             practiceQuestions=[
                 {"q": "She had been training hard for years は、どのような意味ですか。", "a": "『（友人からの知らせを受けた時点まで）何年も一生懸命練習を続けていた』という意味です。過去の時点まで続いていた動作を表します。"},
                 {"q": "a friend she had met through dancing で、had met と過去完了になっているのはなぜですか。", "a": "メッセージを受け取った時点より前に、ダンスを通して知り合っていたからです。she had met の前には目的格の関係代名詞が省略されています。"},
                 {"q": "When she learned that he had gotten a job as a dancer の2つの出来事は、どちらが先ですか。", "a": "友人がダンサーの仕事を得たことが先で、ジョイスがそれを知ったのが後です。先の出来事を had gotten で表しています。"},
                 {"q": "Q21の正解 her smile disappeared completely の根拠になる文はどれですか。", "a": "直後の She became less confident and thought she did not have enough talent like him. です。最初は喜んだものの、自信をなくしたという変化から、笑顔が消えたことがわかります。"}],
             highlightPatterns=["had been training hard for years", "her dream had not come true yet", "a friend she had met through dancing", "he had gotten a job as a dancer"]),
        dict(id="fp2", title="even if の譲歩・関係代名詞の省略・間接疑問（even if things didn't turn out / the time and effort she had put into / how much she loved）",
             subtitle="even if and Omitted Relative Pronouns",
             explanation="大問3の第2段落では、父親の言葉でジョイスの気持ちが変わります。her efforts were never wasted, even if things didn't turn out as she hoped は、even if『たとえ～でも』が条件を認めたうえで、それでも努力はむだにならないと伝えています。as she hoped の as は『～のように』です。all the time and effort she had put into dancing は、time and effort の後ろに目的格の関係代名詞 that が省略された形で、『ダンスに注いできたすべての時間と努力』という意味になります。how much she loved dancing は『どれほどダンスが好きか』という名詞のまとまりで、remembered の目的語です。",
             sourceQuote="He told her that her efforts were never wasted, even if things didn't turn out as she hoped. At that moment, she realized she did not have to regret all the time and effort she had put into dancing.",
             sourceLocation="大問3「A Dream」第2段落", highlightLabel="譲歩・省略", highlightColor="#34d399",
             examples=[quote(dream, "He told her that her efforts", "even if は『たとえ～でも』。結果が思いどおりでなくても、努力はむだではないと伝えている。"),
                       example("Even if it rains tomorrow, the game will be held.", "たとえ明日雨が降っても、試合は行われる。", "even if の後ろは条件。主節で、その条件でも変わらないことを述べる。"),
                       example("The book I borrowed from the library was interesting.", "私が図書館で借りた本はおもしろかった。", "book の後ろに目的格の関係代名詞 that（which）が省略されている。")],
             practicePassage=practice(dream, 1),
             practiceQuestions=[
                 {"q": "even if things didn't turn out as she hoped の意味を答えてください。", "a": "『たとえ物事が彼女の望んだとおりにならなかったとしても』という意味です。思いどおりにならない場合を認めたうえで、努力はむだではないと述べています。"},
                 {"q": "all the time and effort she had put into dancing で、省略されている語は何ですか。", "a": "目的格の関係代名詞 that（または which）です。the time and effort (that) she had put into dancing となります。"},
                 {"q": "She remembered how much she loved dancing. の how much 以下は、文の中でどのような働きをしていますか。", "a": "remembered の目的語になる名詞のまとまり（間接疑問）で、『どれほどダンスが好きか』という意味です。"},
                 {"q": "Q22の正解 felt saved by his words の根拠を答えてください。", "a": "父親の言葉を聞いて、時間と努力を後悔しなくてよいと気づいたこと、そして最後の Thanks to him, she was ready to try again. です。父親の言葉に救われたことがわかります。"}],
             highlightPatterns=["even if things didn't turn out as she hoped", "all the time and effort she had put into dancing", "how much she loved dancing"]),
        dict(id="fp3", title="条件の if と In that case（if you want to come / In that case / even without a reservation）",
             subtitle="Conditions with if and In that case",
             explanation="メールの第3段落では、条件によって手続きが分かれています。if you want to come や if you have friends who are interested は『もし～なら』という条件です。In that case は『その場合は』で、直前に述べた場合を指します。1つ目の In that case は『興味のある友人がいる場合』で、水曜日までに名前を送るよう頼んでいます。2つ目の But in that case は『予約なしで参加する場合』で、入口でチケット代を払う必要があると伝えています。even without a reservation は『予約がなくても』です。それぞれの In that case がどの場合を指すかを確かめると、手続きを正しく読み取れます。",
             sourceQuote="Also, if you have friends who are interested, I can save two more seats for free. In that case, please send me their names by Wednesday.",
             sourceLocation="大問4A「A film event」第3段落", highlightLabel="条件・場合", highlightColor="#f472b6",
             examples=[quote(email, "Also, if you have friends", "if は条件『もし～なら』。friends who are interested の who は friends を説明する関係代名詞。"),
                       example("If you are free tomorrow, let's go shopping. In that case, I'll meet you at the station.", "明日ひまなら、買い物に行こう。その場合は、駅で待ち合わせよう。", "In that case は直前の条件（明日ひまな場合）を受ける。"),
                       example("You can enter the museum even without a ticket on Sundays.", "日曜日は、チケットがなくても博物館に入ることができる。", "even without ～は『～がなくても』。前置詞 without の後ろは名詞。")],
             practicePassage=practice(email, 2),
             practiceQuestions=[
                 {"q": "1つ目の In that case は、どのような場合を指していますか。", "a": "アランに、イベントに興味のある友人がいる場合です。その場合は、水曜日までに友人の名前を送るよう頼んでいます。"},
                 {"q": "2つ目の But in that case は、どのような場合を指していますか。", "a": "予約なしで参加する場合です。その場合は、入口でチケット代を払う必要があります。"},
                 {"q": "This is a paid event, but I can give you a free ticket if you want to come. から、アランについてわかることは何ですか。", "a": "有料のイベントですが、アランが来たいなら無料のチケットをもらえるということです。"},
                 {"q": "Q25の正解 should inform her if he wants free seats for friends の根拠を答えてください。", "a": "if you have friends who are interested, I can save two more seats for free. In that case, please send me their names by Wednesday. です。友人の無料の席がほしい場合は、名前を知らせる必要があります。"}],
             highlightPatterns=["if you want to come", "if you have friends who are interested", "In that case, please send me their names", "even without a reservation", "But in that case, you will need to pay"]),
        dict(id="fp4", title="be allowed to / be free to と目的の in order to（not allowed to eat / free to choose / in order to make）",
             subtitle="be allowed to, be free to and in order to",
             explanation="大問4Bの第4段落は、ミートレス・マンデーに反対する意見です。children are not allowed to eat meat は be allowed to V『～することを許されている』の否定で、『子どもたちは肉を食べることを許されていない』という意味です。should be free to choose what they eat は be free to V『自由に～できる』の後に、what they eat『自分たちが食べるもの（何を食べるか）』という名詞のまとまりが続いた形で、『自分が食べるものを自由に選べるべきだ』となります。最後の in order to make Meatless Monday more widely accepted は目的『～するために』で、make＋O＋C（ミートレス・マンデーをより広く受け入れられたものにする）の形を含みます。may need to be considered は、need to be＋過去分詞『～される必要がある』に may『～かもしれない』がついた形です。",
             sourceQuote="For example, some people complain that children are not allowed to eat meat in their school lunches on certain days. They believe children and their parents should be free to choose what they eat.",
             sourceLocation="大問4B「Days Without Meat」第4段落", highlightLabel="許可・目的", highlightColor="#fbbf24",
             examples=[quote(meat, "For example, some people complain", "be not allowed to V は『～することを許されていない』。complain that ... は『～だと不満を言う』。"),
                       example("Students are not allowed to use phones during the test.", "生徒はテスト中に電話を使うことを許されていない。", "be allowed to V の否定。規則で禁止されていることを表す。"),
                       example("You are free to choose any seat you like.", "好きな席を自由に選んでかまいません。", "be free to V は『自由に～できる』。")],
             practicePassage=practice(meat, 3),
             practiceQuestions=[
                 {"q": "children are not allowed to eat meat は、どのような意味ですか。", "a": "『子どもたちは（特定の日の給食で）肉を食べることを許されていない』という意味です。be allowed to V の否定です。"},
                 {"q": "should be free to choose what they eat の what は、どのような働きをしていますか。", "a": "『～もの』という意味の関係代名詞と考えると、what they eat は『自分たちが食べるもの』という名詞のまとまりです（『何を食べるか』と訳すこともできます）。choose の目的語になっています。"},
                 {"q": "in order to make Meatless Monday more widely accepted で、make の目的語と補語は何ですか。", "a": "目的語は Meatless Monday、補語は more widely accepted です。『ミートレス・マンデーをより広く受け入れられたものにするために』という意味です。"},
                 {"q": "Q29の正解 They think children should be allowed to decide their own food. に対応する本文の表現を答えてください。", "a": "They believe children and their parents should be free to choose what they eat. です。be free to choose が be allowed to decide に、what they eat が their own food に言い換えられています。"}],
             highlightPatterns=["children are not allowed to eat meat", "should be free to choose what they eat", "in order to make Meatless Monday more widely accepted"]),
        dict(id="fp5", title="今回の重要なパラフレーズ", subtitle="Key Paraphrases in This Exam",
             explanation="大問4の正解の選択肢は、本文と同じ内容を別の語句で表していることがよくあります。例えば、本文の took in about 15 percent more fat than they should（とるべき量より約15%多く脂肪をとっていた）は、Q27の正解では had too much fat in their diet（食事で脂肪をとりすぎていた）と言い換えられています。数値は消えていますが、『必要以上に多い』という意味は同じです。反対に、本文の語句（avoiding meat や health problems など）を使っていても、内容が本文と食い違っている選択肢は不正解です。例えば Q27の選択肢1 は『肉を避けると健康問題が起きる』としていますが、本文では脂肪のとりすぎが健康問題につながり、肉を避けると余分な脂肪を減らせるとしています。根拠の文と意味が同じかどうかを確かめて選びましょう。",
             sourceQuote="① I am writing to remind you about the film event → share the information about an event（Q23）\n② There were no words in the film, but I tried to tell a message through the images and sounds → It expresses the theme without using spoken words（Q24）\n③ if you have friends who are interested, I can save two more seats for free. In that case, please send me their names → should inform her if he wants free seats for friends（Q25）\n④ has spread to over forty countries / continues to influence the eating habits of many people → helps change the way people eat in many countries（Q26）\n⑤ took in about 15 percent more fat than they should → had too much fat in their diet（Q27）\n⑥ understood these problems and started to see Meatless Monday as a simple way to help the environment → realized it could help solve some environmental problems（Q28）\n⑦ children and their parents should be free to choose what they eat → children should be allowed to decide their own food（Q29）",
             sourceLocation="大問4A Q23〜25／大問4B Q26〜29", highlightLabel="パラフレーズ", highlightColor="#f59e0b",
             examples=[quote(meat, "An American who came up with the idea", "took in about 15 percent more fat than they should を、Q27では had too much fat in their diet とまとめている。"),
                       example("He ate more than he needed. / He ate too much.", "彼は必要以上に食べた。／彼は食べすぎた。", "more than ～ needed（必要以上に）を too much（～しすぎる）で言い換える。"),
                       example("Many people now eat less meat. / People's eating habits have changed.", "今では多くの人が肉を食べる量を減らしている。／人々の食習慣が変わった。", "具体的な行動を、より一般的な言い方（食習慣の変化）にまとめる。")],
             practicePassage=practice(meat, 1),
             practiceQuestions=[
                 {"q": "Q27の正解 he discovered that people in America had too much fat in their diet に対応する本文の表現を答えてください。", "a": "learned that people in the United States took in about 15 percent more fat than they should です。learned が discovered に、took in ... more fat than they should が had too much fat に言い換えられています。"},
                 {"q": "Q27の選択肢4 he believed people could get enough fat by eating meat once a week が不正解なのはなぜですか。", "a": "本文では、週に1日肉を避けることで余分な脂肪を減らせると考えたと書かれています。『週1回肉を食べれば十分な脂肪がとれる』という内容は書かれておらず、考えの向きが逆になっています。"},
                 {"q": "which could lead to serious health problems の which は何を受けていますか。", "a": "前の内容全体（アメリカの人々がとるべき量より約15%多く脂肪をとっていたこと）です。それが深刻な健康問題につながる可能性がある、と付け加えています。"},
                 {"q": "reduce the extra fat taken in の taken in は、どのような働きをしていますか。", "a": "extra fat を後ろから説明する過去分詞で、『摂取された余分な脂肪』という意味です。"}],
             highlightPatterns=["took in about 15 percent more fat than they should", "which could lead to serious health problems", "avoiding meat just one day a week", "reduce the extra fat taken in"]),
    ]
    return dict(focusPoints=fps)
