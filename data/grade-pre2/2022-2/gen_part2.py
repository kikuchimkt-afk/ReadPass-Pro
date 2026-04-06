"""Generate sections 2-3 (大問3+4) + vocabulary for 2022-2"""
import json, os

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2022-2"
data = json.load(open(os.path.join(base, "_part1.json"), "r", encoding="utf-8"))

# Section 2: 大問3 passage-fill (A:2問 B:3問)
section3 = {
    "name": "大問3", "nameEn": "Part 3", "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A", "title": "A Voice from the Past",
            "paragraphs": [
                "Every year, volunteers in Brisbane, Australia, meet to clean up the beach. This year, John and his father joined the group. They worked hard all morning to pick up garbage. Near lunchtime, John noticed a glass bottle on the beach. The bottle was old and dirty. It looked like ( 26 ). John picked up the bottle and gave it to his father. His father opened it and took out a piece of paper. He told John that it was a message.",
                "John's father showed the message to John. It said, \"My name is Paul, and I am 10 years old. I am from Canada. I am traveling to Australia on a ship called the Fair Star. Please ( 27 ).\" On their way home, John and his father bought a postcard to send to Paul. A few weeks later, they got a reply. Paul said he was now 50, and it was amazing that John had found his message after such a long time."
            ],
            "translations": [
                "毎年、オーストラリアのブリスベンでボランティアがビーチの清掃活動に集まる。今年、ジョンと父親がグループに参加した。彼らは午前中ずっとゴミ拾いに励んだ。お昼近く、ジョンはビーチでガラス瓶に気づいた。その瓶は古くて汚かった。中に( 26 )ように見えた。ジョンは瓶を拾い、父親に渡した。父親はそれを開けて紙を取り出した。それはメッセージだと言った。",
                "父親はメッセージをジョンに見せた。そこにはこう書かれていた。「僕の名前はポールで、10歳です。カナダから来ました。フェアスターという船でオーストラリアに旅行中です。( 27 )」帰り道、ジョンと父親はポールに送るハガキを買った。数週間後、返事が届いた。ポールは今50歳で、ジョンが長い年月を経てメッセージを見つけたことに驚いていた。"
            ],
            "sentencePairs": [
                ["Every year, volunteers in Brisbane, Australia, meet to clean up the beach.", "毎年、オーストラリアのブリスベンでボランティアがビーチの清掃活動に集まる。"],
                ["This year, John and his father joined the group.", "今年、ジョンと父親がグループに参加した。"],
                ["They worked hard all morning to pick up garbage.", "彼らは午前中ずっとゴミ拾いに励んだ。"],
                ["Near lunchtime, John noticed a glass bottle on the beach.", "お昼近く、ジョンはビーチでガラス瓶に気づいた。"],
                ["The bottle was old and dirty.", "その瓶は古くて汚かった。"],
                ["John picked up the bottle and gave it to his father.", "ジョンは瓶を拾い、父親に渡した。"],
                ["His father opened it and took out a piece of paper.", "父親はそれを開けて紙を取り出した。"],
                ["He told John that it was a message.", "それはメッセージだと言った。"],
                ["On their way home, John and his father bought a postcard to send to Paul.", "帰り道、ジョンと父親はポールに送るハガキを買った。"],
                ["A few weeks later, they got a reply.", "数週間後、返事が届いた。"],
                ["Paul said he was now 50, and it was amazing that John had found his message after such a long time.", "ポールは今50歳で、長い年月を経てメッセージを見つけたことに驚いていた。"]
            ],
            "questions": [
                {"number": 26, "choices": ["it had been made recently", "it was full of red wine", "there might be more bottles nearby", "there was something inside it"], "choiceTranslations": ["最近作られたもの", "赤ワインがいっぱい入っている", "近くにもっと瓶があるかもしれない", "中に何かが入っている"], "answer": 4, "choiceAnalysis": ["最近作られた→古くて汚いと矛盾", "赤ワインがいっぱい→次の文で紙を取り出すので不適切", "近くにもっと瓶がある→瓶を開ける展開に繋がらない", "中に何かが入っている→正解。💡 父親が開けて紙を取り出す展開が根拠"], "grammar": "💡 It looked like ～＝～のように見えた。inside＝中に。a piece of paper＝1枚の紙"},
                {"number": 27, "choices": ["write to me at this address", "have a nice time on vacation", "take this bottle to my family", "help me to get back home"], "choiceTranslations": ["この住所に手紙をください", "休暇を楽しんでください", "この瓶を私の家族に届けてください", "家に帰るのを助けてください"], "answer": 1, "choiceAnalysis": ["この住所に手紙をください→正解。💡 ジョンがハガキを送り返事が来た＝住所があったから連絡できた", "休暇を楽しんで→メッセージの依頼としては弱い", "瓶を家族に届ける→カナダまで届けるのは非現実的", "帰る助け→旅行中で助けを求める文脈ではない"], "grammar": "💡 write to ～＝～に手紙を書く。address＝住所。postcard＝ハガキ。reply＝返事"}
            ]
        },
        {
            "label": "B", "title": "Hungry Hikers",
            "paragraphs": [
                "People are having a bigger and bigger effect on wild animals. As a result, new laws and special parks are being created to protect nature. Some changes have been very successful. For example, there were about 170 wild elephants in 1980 in Yunnan, China. These days, experts think that there are around 300 elephants there. However, the elephants have ( 28 ). As cities get bigger and more farms are needed to feed people, there are not as many places for animals like elephants.",
                "Big animals can cause big problems for people. Because there is not enough food in protected areas, elephants often leave these areas to take food from farms. In fact, a group of about 14 elephants from Yunnan went on a 500-kilometer walk to look for food during 2020 and 2021. The elephants sometimes went through towns trying to find food. They appeared on the TV news and the Internet. As a result, they ( 29 ) China. People were interested to find out what would happen to them next.",
                "Finally, the elephants returned to a protected area in Yunnan. However, to try to prevent similar adventures in the future, experts have designed a special \"food court\" for elephants. The food court cost $15 million to build and is about 670,000 square meters. It has five ponds where elephants can drink, and all the plants that elephants need to eat to stay healthy. The experts hope that it will be enough to ( 30 )."
            ],
            "translations": [
                "人々は野生動物にますます大きな影響を与えている。その結果、自然を守るために新しい法律や特別な公園が作られている。一部の変化は非常に成功している。例えば、1980年の中国雲南省には約170頭の野生の象がいた。現在、専門家はそこに約300頭の象がいると考えている。しかし、象は( 28 )。都市が大きくなり人々を養うためにより多くの農地が必要になるにつれ、象のような動物のための場所は減っている。",
                "大きな動物は人々に大きな問題を引き起こすことがある。保護区に十分な食料がないため、象はしばしばこれらの区域を出て農場から食料を取る。実際、2020年と2021年に雲南省から約14頭の象のグループが食料を探すために500キロの旅に出た。象は時に町を通り抜けて食料を探そうとした。テレビのニュースやインターネットに登場した。その結果、彼らは中国で( 29 )。人々は次に何が起こるか知りたがっていた。",
                "最終的に、象は雲南省の保護区に戻った。しかし、将来の同様の冒険を防ぐために、専門家は象のための特別な「フードコート」を設計した。フードコートは建設に1500万ドルかかり、約67万平方メートルの広さだ。象が飲める5つの池と、象が健康を保つために食べる必要のあるすべての植物がある。専門家は、それが( 30 )のに十分であることを期待している。"
            ],
            "sentencePairs": [
                ["People are having a bigger and bigger effect on wild animals.", "人々は野生動物にますます大きな影響を与えている。"],
                ["As a result, new laws and special parks are being created to protect nature.", "その結果、自然を守るために新しい法律や特別な公園が作られている。"],
                ["For example, there were about 170 wild elephants in 1980 in Yunnan, China.", "例えば、1980年の中国雲南省には約170頭の野生の象がいた。"],
                ["These days, experts think that there are around 300 elephants there.", "現在、専門家はそこに約300頭の象がいると考えている。"],
                ["As cities get bigger and more farms are needed to feed people, there are not as many places for animals like elephants.", "都市が大きくなり人々を養うためにより多くの農地が必要になるにつれ、象のような動物のための場所は減っている。"],
                ["Because there is not enough food in protected areas, elephants often leave these areas to take food from farms.", "保護区に十分な食料がないため、象はしばしばこれらの区域を出て農場から食料を取る。"],
                ["In fact, a group of about 14 elephants from Yunnan went on a 500-kilometer walk to look for food during 2020 and 2021.", "実際、2020年と2021年に雲南省から約14頭の象のグループが食料を探すために500キロの旅に出た。"],
                ["The elephants sometimes went through towns trying to find food.", "象は時に町を通り抜けて食料を探そうとした。"],
                ["They appeared on the TV news and the Internet.", "テレビのニュースやインターネットに登場した。"],
                ["People were interested to find out what would happen to them next.", "人々は次に何が起こるか知りたがっていた。"],
                ["Finally, the elephants returned to a protected area in Yunnan.", "最終的に、象は雲南省の保護区に戻った。"],
                ["The food court cost $15 million to build and is about 670,000 square meters.", "フードコートは建設に1500万ドルかかり、約67万平方メートルの広さだ。"],
                ["It has five ponds where elephants can drink, and all the plants that elephants need to eat to stay healthy.", "象が飲める5つの池と、象が健康を保つために食べる必要のあるすべての植物がある。"]
            ],
            "questions": [
                {"number": 28, "choices": ["fewer chances to see people", "less space to live in", "shorter lives than before", "smaller numbers of babies"], "choiceTranslations": ["人に会う機会が減った", "住む場所が減った", "以前より寿命が短くなった", "赤ちゃんの数が減った"], "answer": 2, "choiceAnalysis": ["人に会う機会が減った→都市拡大では人との接触は増える", "住む場所が減った→正解。💡 次の文で都市拡大と農地需要で動物の場所が減ると説明", "寿命が短くなった→寿命についての言及はない", "赤ちゃんの数が減った→数は170→300に増加している"], "grammar": "💡 less space＝より少ないスペース（不可算名詞にはless）。fewer＝より少ない（可算名詞に使う）"},
                {"number": 29, "choices": ["tried some food from", "were kept in zoos outside", "decided to travel to", "got a lot of attention in"], "choiceTranslations": ["～の食べ物を試した", "～の外の動物園に入れられた", "～に旅行することにした", "～で大きな注目を集めた"], "answer": 4, "choiceAnalysis": ["食べ物を試した→テレビ出演の結果としては不自然", "動物園に入れられた→動物園の言及はない", "旅行することにした→すでに旅に出ている", "大きな注目を集めた→正解。💡 テレビやネットに登場し、人々が次の展開に興味を持った"], "grammar": "💡 get attention＝注目を集める。appear on TV＝テレビに出る。be interested to ～＝～することに興味がある"},
                {"number": 30, "choices": ["attract more human visitors", "stop people from killing animals", "keep the elephants in the area", "make the elephants sleepy"], "choiceTranslations": ["より多くの人間の訪問者を引きつける", "人々が動物を殺すのを止める", "象をその地域に留める", "象を眠くさせる"], "answer": 3, "choiceAnalysis": ["人間の訪問者を引きつける→フードコートの目的は象のため", "動物殺害を止める→殺害の言及はない", "象をその地域に留める→正解。💡 フードコートで十分な食料を提供し、象が保護区から出ないようにする", "象を眠くさせる→フードコートの目的ではない"], "grammar": "💡 keep ～ in ...＝～を…に留める。prevent＝防ぐ。be enough to ～＝～するのに十分である"}
            ]
        }
    ]
}

# Section 3: 大問4 reading-comprehension (A:email 3問, B:4問)
section4 = {
    "name": "大問4", "nameEn": "Part 4", "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "A", "title": "Movie Festival", "format": "email",
            "meta": {"from": "Alan Reznick", "to": "Jeff Teanaway", "date": "October 9", "subject": "Movie festival"},
            "paragraphs": [
                "Thanks for letting me borrow your DVD of Burning Fist. It's such an exciting movie. I really liked the part when the hero is riding a cool bike and being chased by bad guys. After watching it last Saturday, my mom took me to a bookstore. I found a book about Burning Fist and bought it. It's really interesting. I'll lend it to you when I finish reading it.",
                "While I was at the bookstore, I saw a poster for an action movie festival. It will be held next month at the Old Lawrence Theater, near the Elm Street subway station. It's close to the Mexican restaurant that we went to on your birthday last year. The poster said that the director of Burning Fist will be at the festival. She'll answer fans' questions about her movies and talk about her next movie.",
                "Eight movies are going to be shown over two days at the festival. They've all been chosen by the director of Burning Fist. Some of them are old action movies from the 1980s and 1990s. There will also be some new movies, too. I think it sounds great, so I'm definitely going to buy a ticket for the festival. Should I get one for you, too?"
            ],
            "translations": [
                "DVDの『バーニング・フィスト』を貸してくれてありがとう。とてもエキサイティングな映画だね。主人公がクールなバイクに乗って悪者に追われるところが好きだった。先週の土曜日にそれを見た後、ママが本屋に連れて行ってくれた。バーニング・フィストについての本を見つけて買ったよ。とても面白い。読み終わったら貸すね。",
                "本屋にいた時、アクション映画祭のポスターを見た。来月、エルム通り地下鉄駅の近くのオールド・ローレンス・シアターで開催されるんだ。去年の君の誕生日に行ったメキシカンレストランの近くだよ。ポスターによると、バーニング・フィストの監督がフェスティバルに来るらしい。ファンの質問に答えて、次の映画について話すんだって。",
                "フェスティバルでは2日間で8本の映画が上映される予定。全部バーニング・フィストの監督が選んだんだ。1980年代や1990年代の古いアクション映画もあるし、新しい映画もある。すごく面白そうだから、絶対チケットを買うつもり。君の分も買おうか？"
            ],
            "sentencePairs": [
                ["Thanks for letting me borrow your DVD of Burning Fist.", "DVDの『バーニング・フィスト』を貸してくれてありがとう。"],
                ["I really liked the part when the hero is riding a cool bike and being chased by bad guys.", "主人公がクールなバイクに乗って悪者に追われるところが好きだった。"],
                ["After watching it last Saturday, my mom took me to a bookstore.", "先週の土曜日にそれを見た後、ママが本屋に連れて行ってくれた。"],
                ["I found a book about Burning Fist and bought it.", "バーニング・フィストについての本を見つけて買ったよ。"],
                ["I'll lend it to you when I finish reading it.", "読み終わったら貸すね。"],
                ["While I was at the bookstore, I saw a poster for an action movie festival.", "本屋にいた時、アクション映画祭のポスターを見た。"],
                ["It will be held next month at the Old Lawrence Theater, near the Elm Street subway station.", "来月、エルム通り地下鉄駅の近くのオールド・ローレンス・シアターで開催される。"],
                ["The poster said that the director of Burning Fist will be at the festival.", "ポスターによると、バーニング・フィストの監督がフェスティバルに来るらしい。"],
                ["She'll answer fans' questions about her movies and talk about her next movie.", "ファンの質問に答えて、次の映画について話すんだって。"],
                ["Eight movies are going to be shown over two days at the festival.", "フェスティバルでは2日間で8本の映画が上映される予定。"],
                ["They've all been chosen by the director of Burning Fist.", "全部バーニング・フィストの監督が選んだんだ。"],
                ["I think it sounds great, so I'm definitely going to buy a ticket for the festival.", "すごく面白そうだから、絶対チケットを買うつもり。"],
                ["Should I get one for you, too?", "君の分も買おうか？"]
            ],
            "questions": [
                {"number": 31, "question": "What did Alan do last Saturday?", "questionTranslation": "アランは先週の土曜日に何をしましたか？", "choices": ["He went to a bookstore with Jeff.", "He bought a book about a movie.", "He rode a friend's cool bike.", "He lent one of his DVDs to Jeff."], "choiceTranslations": ["ジェフと一緒に本屋に行った。", "映画についての本を買った。", "友達のクールなバイクに乗った。", "ジェフにDVDを1枚貸した。"], "answer": 2, "choiceAnalysis": ["ジェフと本屋に→母親と行った。ジェフとではない", "映画についての本を買った→正解。💡 「I found a book about Burning Fist and bought it」が根拠", "バイクに乗った→映画の中の場面で実際には乗っていない", "DVDを貸した→ジェフがアランに貸した（逆）"], "grammar": "💡 last Saturday＝先週の土曜日。found and bought＝見つけて買った（過去形の並列）"},
                {"number": 32, "question": "Last year, Jeff and Alan", "questionTranslation": "昨年、ジェフとアランは", "choices": ["tried Mexican food for the first time.", "watched a movie at the Old Lawrence Theater.", "met the director of Burning Fist.", "went to a restaurant for Jeff's birthday."], "choiceTranslations": ["初めてメキシコ料理を食べた。", "オールド・ローレンス・シアターで映画を見た。", "バーニング・フィストの監督に会った。", "ジェフの誕生日にレストランに行った。"], "answer": 4, "choiceAnalysis": ["初めてメキシコ料理→初めてとは書いていない", "シアターで映画を見た→シアターでの映画はフェスティバルの話（来月）", "監督に会った→監督はフェスティバルで来る予定（まだ会っていない）", "ジェフの誕生日にレストランに行った→正解。💡 「the Mexican restaurant that we went to on your birthday last year」が根拠"], "grammar": "💡 go to a restaurant＝レストランに行く。on one's birthday＝～の誕生日に"},
                {"number": 33, "question": "What is one thing Alan says about the festival?", "questionTranslation": "アランがフェスティバルについて言っていることの一つは何ですか？", "choices": ["He has already bought tickets for it.", "All the movies are old action movies.", "The movies were chosen by local movie fans.", "It will be held on more than one day."], "choiceTranslations": ["すでにチケットを買った。", "映画はすべて古いアクション映画だ。", "映画は地元の映画ファンが選んだ。", "1日以上にわたって開催される。"], "answer": 4, "choiceAnalysis": ["すでにチケットを買った→「going to buy」でまだ買っていない", "すべて古いアクション映画→新しい映画もあると明記", "地元ファンが選んだ→監督が選んだ", "1日以上にわたって開催→正解。💡 「over two days」＝2日間にわたって"], "grammar": "💡 over two days＝2日間にわたって。more than one day＝1日以上（パラフレーズ）"}
            ]
        },
        {
            "label": "B", "title": "Spicy Soda",
            "paragraphs": [
                "Ginger ale is a spicy soft drink. It was invented in Ireland in the 1850s. However, the type that is most popular today was created by a man called John McLaughlin who lived in Toronto, Canada. After he graduated from college in Canada, he went to study in New York City. While studying, he worked part-time at a drugstore. He noticed that many people were buying soda water from the store and mixing it with different fruit flavors.",
                "McLaughlin returned to Toronto in 1890 and started a soda water company. It became very successful. One reason was that his advertisements said the water provided by the city was dangerous and caused diseases. He recommended that people drink his fruit-flavored soda water instead. He also made machines called soda fountains. People could use them to buy McLaughlin's drinks. The machines became popular with shoppers in busy department stores, especially on hot summer days.",
                "McLaughlin had poor health, and he had to stop being the manager of his company. However, he continued inventing new drinks. He knew about ginger ale from Ireland, but many of his customers did not like its sweet flavor. McLaughlin spent three years trying to create the perfect kind of ginger ale. Finally, by 1904, he had created a lighter, spicier drink. McLaughlin's wife liked it so much that she said it was \"the champagne of ginger ales.\"",
                "McLaughlin's \"Canada Dry Pale Ginger Ale\" was a success. As well as being delicious on its own, it could also be mixed with other drinks. Some people like to drink it rather than beer or other alcoholic drinks. Moreover, the ginger can help people with stomachaches or sore throats. It has been over 100 years since Canada Dry Pale Ginger Ale was invented. In that time, its popularity has spread from Canada, through the United States, and around the world."
            ],
            "translations": [
                "ジンジャーエールはスパイシーな清涼飲料水だ。1850年代にアイルランドで発明された。しかし、今日最も人気のあるタイプは、カナダのトロントに住んでいたジョン・マクラフリンという男性によって作られた。カナダの大学を卒業した後、ニューヨーク市に留学した。勉強しながらドラッグストアでアルバイトをしていた。多くの人がソーダ水を買って、さまざまなフルーツフレーバーと混ぜていることに気づいた。",
                "マクラフリンは1890年にトロントに戻り、ソーダ水の会社を始めた。非常に成功した。一つの理由は、彼の広告が市が提供する水は危険で病気を引き起こすと述べたことだ。代わりに自分のフルーツ味のソーダ水を飲むよう勧めた。彼はまたソーダファウンテンと呼ばれる機械も作った。人々はそれを使ってマクラフリンの飲み物を買うことができた。特に暑い夏の日には、忙しいデパートの買い物客に人気だった。",
                "マクラフリンは体調が悪く、会社の経営者をやめなければならなかった。しかし、新しい飲み物の発明を続けた。アイルランドのジンジャーエールのことは知っていたが、多くの顧客はその甘い味が好きではなかった。マクラフリンは完璧なジンジャーエールを作るために3年を費やした。ついに1904年までに、より軽く、よりスパイシーな飲み物を作り上げた。マクラフリンの妻はそれがとても気に入り、「ジンジャーエールのシャンパンだ」と言った。",
                "マクラフリンの「カナダドライ・ペール・ジンジャーエール」は成功を収めた。そのまま飲んでもおいしいだけでなく、他の飲み物と混ぜることもできた。ビールやその他のアルコール飲料の代わりに飲む人もいる。さらに、ジンジャーは腹痛や喉の痛みにも効果がある。カナダドライ・ペール・ジンジャーエールが発明されてから100年以上が経った。その間に、その人気はカナダからアメリカを経て、世界中に広がった。"
            ],
            "sentencePairs": [
                ["Ginger ale is a spicy soft drink.", "ジンジャーエールはスパイシーな清涼飲料水だ。"],
                ["It was invented in Ireland in the 1850s.", "1850年代にアイルランドで発明された。"],
                ["After he graduated from college in Canada, he went to study in New York City.", "カナダの大学を卒業した後、ニューヨーク市に留学した。"],
                ["While studying, he worked part-time at a drugstore.", "勉強しながらドラッグストアでアルバイトをしていた。"],
                ["He noticed that many people were buying soda water from the store and mixing it with different fruit flavors.", "多くの人がソーダ水を買ってさまざまなフルーツフレーバーと混ぜていることに気づいた。"],
                ["McLaughlin returned to Toronto in 1890 and started a soda water company.", "マクラフリンは1890年にトロントに戻り、ソーダ水の会社を始めた。"],
                ["One reason was that his advertisements said the water provided by the city was dangerous and caused diseases.", "一つの理由は、広告が市の水は危険で病気を引き起こすと述べたことだ。"],
                ["He recommended that people drink his fruit-flavored soda water instead.", "代わりに自分のフルーツ味のソーダ水を飲むよう勧めた。"],
                ["People could use them to buy McLaughlin's drinks.", "人々はそれを使ってマクラフリンの飲み物を買うことができた。"],
                ["The machines became popular with shoppers in busy department stores, especially on hot summer days.", "特に暑い夏の日には、忙しいデパートの買い物客に人気だった。"],
                ["McLaughlin had poor health, and he had to stop being the manager of his company.", "マクラフリンは体調が悪く、会社の経営者をやめなければならなかった。"],
                ["However, he continued inventing new drinks.", "しかし、新しい飲み物の発明を続けた。"],
                ["McLaughlin spent three years trying to create the perfect kind of ginger ale.", "マクラフリンは完璧なジンジャーエールを作るために3年を費やした。"],
                ["Finally, by 1904, he had created a lighter, spicier drink.", "ついに1904年までに、より軽く、よりスパイシーな飲み物を作り上げた。"],
                ["As well as being delicious on its own, it could also be mixed with other drinks.", "そのまま飲んでもおいしいだけでなく、他の飲み物と混ぜることもできた。"],
                ["Some people like to drink it rather than beer or other alcoholic drinks.", "ビールやその他のアルコール飲料の代わりに飲む人もいる。"],
                ["Moreover, the ginger can help people with stomachaches or sore throats.", "さらに、ジンジャーは腹痛や喉の痛みにも効果がある。"],
                ["In that time, its popularity has spread from Canada, through the United States, and around the world.", "その間に、その人気はカナダからアメリカを経て、世界中に広がった。"]
            ],
            "questions": [
                {"number": 34, "question": "What did John McLaughlin notice while he was in New York City?", "questionTranslation": "ジョン・マクラフリンはニューヨーク市にいる間、何に気づきましたか？", "choices": ["People from Ireland liked to drink ginger ale.", "It was easier to find work there than in Canada.", "Adding different flavors to soda water was popular.", "Drugstores there sold more things than drugstores in Toronto."], "choiceTranslations": ["アイルランド出身の人はジンジャーエールが好きだった。", "カナダより仕事が見つけやすかった。", "ソーダ水にさまざまなフレーバーを加えることが人気だった。", "そこのドラッグストアはトロントより多くのものを売っていた。"], "answer": 3, "choiceAnalysis": ["アイルランド人がジンジャーエール好き→NY時代の気づきではない", "仕事が見つけやすい→仕事の難易度の言及はない", "ソーダ水に異なるフレーバーを加えるのが人気→正解。💡 「many people were buying soda water and mixing it with different fruit flavors」が根拠", "トロントより品揃えが多い→品揃えの比較はない"], "grammar": "💡 notice (that) ～＝～に気づく。mix A with B＝AをBと混ぜる"},
                {"number": 35, "question": "What is one reason that people bought McLaughlin's drinks?", "questionTranslation": "人々がマクラフリンの飲み物を買った理由の一つは何ですか？", "choices": ["They heard that soda water could sometimes cause diseases.", "There was an unusually hot summer in the year 1890.", "McLaughlin told them that the water in Toronto was not safe.", "McLaughlin sold his drinks outside busy department stores."], "choiceTranslations": ["ソーダ水が病気を引き起こすことがあると聞いた。", "1890年に異常に暑い夏があった。", "マクラフリンがトロントの水は安全でないと伝えた。", "マクラフリンが忙しいデパートの外で飲み物を売った。"], "answer": 3, "choiceAnalysis": ["ソーダ水が病気を引き起こす→市の水が危険と言ったのであってソーダ水ではない", "異常に暑い夏→1890年の夏についての言及はない", "トロントの水は安全でないと伝えた→正解。💡 「advertisements said the water provided by the city was dangerous」が根拠", "デパートの外で売った→デパート内のソーダファウンテンで売った"], "grammar": "💡 advertise＝宣伝する。provide＝提供する。recommend (that) ～＝～を勧める"},
                {"number": 36, "question": "What was one result of McLaughlin's poor health?", "questionTranslation": "マクラフリンの体調不良の結果の一つは何ですか？", "choices": ["He quit his job as manager.", "He went on a trip to Ireland.", "He started eating more ginger.", "He stopped drinking champagne."], "choiceTranslations": ["経営者の仕事を辞めた。", "アイルランドに旅行に行った。", "もっとジンジャーを食べるようになった。", "シャンパンを飲むのをやめた。"], "answer": 1, "choiceAnalysis": ["経営者の仕事を辞めた→正解。💡 「he had to stop being the manager of his company」が根拠。quit＝stopのパラフレーズ", "アイルランドに旅行→旅行の言及はない", "ジンジャーを食べる→食事療法の言及はない", "シャンパンを飲むのをやめた→妻のコメントで比喩的に使っただけ"], "grammar": "💡 quit＝やめる（stop のパラフレーズ）。poor health＝体調不良。manager＝経営者"},
                {"number": 37, "question": "Some people like to drink \"Canada Dry Pale Ginger Ale\"", "questionTranslation": "一部の人が「カナダドライ・ペール・ジンジャーエール」を好んで飲むのは", "choices": ["because other drinks give them stomachaches.", "instead of drinks such as beer or wine.", "when they go traveling in other countries.", "to stay awake when they have to work or study."], "choiceTranslations": ["他の飲み物が胃痛を起こすから。", "ビールやワインなどの飲み物の代わりに。", "他の国に旅行に行く時に。", "仕事や勉強をしなければならない時に起きていることに。"], "answer": 2, "choiceAnalysis": ["他の飲み物で胃痛→ジンジャーが胃痛に効くとは書いてあるが他の飲み物が原因とは言っていない", "ビールやワインの代わりに→正解。💡 「Some people like to drink it rather than beer or other alcoholic drinks」が根拠", "旅行時→旅行中の飲用については言及なし", "起きていられるために→カフェインや覚醒効果の言及なし"], "grammar": "💡 rather than ～＝～よりもむしろ、～の代わりに。instead of ～と同義のパラフレーズ"}
            ]
        }
    ]
}

data["sections"].append(section3)
data["sections"].append(section4)

# Vocabulary (42語)
data["vocabulary"] = [
    # 大問1 (15語)
    {"word": "peace", "meaning": "平和", "pos": "名詞", "level": "準2級", "example": "The two countries signed a peace agreement after years of conflict.", "distractors": ["信仰", "名誉", "問題"]},
    {"word": "fit", "meaning": "合う、フィットする", "pos": "動詞", "level": "準2級", "example": "These shoes don't fit me anymore because my feet have grown.", "distractors": ["縫う", "治す", "得る"]},
    {"word": "approach", "meaning": "近づく", "pos": "動詞", "level": "準2級", "example": "As we approached the mountain, the view became more beautiful.", "distractors": ["祝う", "分離する", "研究する"]},
    {"word": "furniture", "meaning": "家具", "pos": "名詞", "level": "準2級", "example": "We need to buy new furniture for the living room.", "distractors": ["雰囲気", "宗教", "貧困"]},
    {"word": "rapidly", "meaning": "急速に", "pos": "副詞", "level": "準2級", "example": "Technology is changing rapidly in the 21st century.", "distractors": ["正確に", "心地よく", "公平に"]},
    {"word": "advantage", "meaning": "利点", "pos": "名詞", "level": "準2級", "example": "One advantage of living in the city is the easy access to public transport.", "distractors": ["破壊", "実験室", "集中"]},
    {"word": "represent", "meaning": "表す、代表する", "pos": "動詞", "level": "準2級", "example": "The color red often represents danger or love.", "distractors": ["開発する", "交換する", "案内する"]},
    {"word": "deliver", "meaning": "届ける", "pos": "動詞", "level": "準2級", "example": "The pizza shop delivers food to your home in 30 minutes.", "distractors": ["バランスを取る", "操作する", "取り替える"]},
    {"word": "find out", "meaning": "調べる、見つけ出す", "pos": "句動詞", "level": "準2級", "example": "I need to find out what time the train leaves.", "distractors": ["つける", "育てる", "起き上がる"]},
    {"word": "keep on", "meaning": "～し続ける", "pos": "句動詞", "level": "準2級", "example": "If you keep on practicing, you will get better at playing the guitar.", "distractors": ["つける", "育てる", "起き上がる"]},
    {"word": "apply for", "meaning": "～に応募する", "pos": "句動詞", "level": "準2級", "example": "She applied for a scholarship to study abroad.", "distractors": ["～について", "～によって", "～を横切って"]},
    {"word": "hang up", "meaning": "電話を切る", "pos": "句動詞", "level": "準2級", "example": "She said goodbye and hung up the phone.", "distractors": ["実行する", "片付ける", "先に進む"]},
    {"word": "at the sight of", "meaning": "～を見て", "pos": "熟語", "level": "準2級", "example": "The child laughed at the sight of the funny clown.", "distractors": ["命をかけて", "光の中で", "寸前に"]},
    {"word": "in detail", "meaning": "詳しく", "pos": "熟語", "level": "準2級", "example": "The teacher explained the rules of the game in detail.", "distractors": ["場合に", "手に持って", "連絡して"]},
    {"word": "make money", "meaning": "お金を稼ぐ", "pos": "熟語", "level": "準2級", "example": "Many students make money by working part-time jobs.", "distractors": ["誇りを持つ", "出産する", "速度を落とす"]},
    # 大問2 (5語)
    {"word": "pick up", "meaning": "迎えに行く、拾う", "pos": "句動詞", "level": "準2級", "example": "Can you pick me up at the station at 6 o'clock?", "distractors": ["持ってくる", "話しかける", "温めておく"]},
    {"word": "vegetarian", "meaning": "菜食主義の", "pos": "形容詞", "level": "準2級", "example": "The restaurant has a special vegetarian menu for customers who don't eat meat.", "distractors": ["辛い", "冷凍の", "有機の"]},
    {"word": "presentation", "meaning": "プレゼンテーション、発表", "pos": "名詞", "level": "準2級", "example": "She prepared a presentation about climate change for her class.", "distractors": ["レポート", "実験", "討論"]},
    {"word": "grow", "meaning": "育てる", "pos": "動詞", "level": "準2級", "example": "My grandmother grows tomatoes and herbs in her garden.", "distractors": ["収穫する", "料理する", "買う"]},
    {"word": "topic", "meaning": "話題、トピック", "pos": "名詞", "level": "準2級", "example": "What topic did you choose for your research paper?", "distractors": ["結論", "要約", "序論"]},
    # 大問3 (8語)
    {"word": "volunteer", "meaning": "ボランティア", "pos": "名詞", "level": "準2級", "example": "Volunteers cleaned up the park after the festival.", "distractors": ["観光客", "警備員", "記者"]},
    {"word": "garbage", "meaning": "ゴミ", "pos": "名詞", "level": "準2級", "example": "Please put the garbage in the recycling bin.", "distractors": ["宝物", "手荷物", "郵便物"]},
    {"word": "message", "meaning": "メッセージ、伝言", "pos": "名詞", "level": "準2級", "example": "I left a message for her on the answering machine.", "distractors": ["手紙", "小包", "切手"]},
    {"word": "protect", "meaning": "守る、保護する", "pos": "動詞", "level": "準2級", "example": "We must protect endangered species from extinction.", "distractors": ["攻撃する", "傷つける", "追い出す"]},
    {"word": "expert", "meaning": "専門家", "pos": "名詞", "level": "準2級", "example": "The expert gave advice on how to save energy at home.", "distractors": ["初心者", "見習い", "愛好家"]},
    {"word": "attention", "meaning": "注目、注意", "pos": "名詞", "level": "準2級", "example": "The new product got a lot of attention from the media.", "distractors": ["批判", "無関心", "懸念"]},
    {"word": "prevent", "meaning": "防ぐ", "pos": "動詞", "level": "準2級", "example": "Wearing a mask can help prevent the spread of disease.", "distractors": ["許可する", "促進する", "増やす"]},
    {"word": "reply", "meaning": "返事、返答する", "pos": "名詞/動詞", "level": "準2級", "example": "I sent him an email but he hasn't replied yet.", "distractors": ["質問", "要求", "提案"]},
    # 大問4 (14語)
    {"word": "borrow", "meaning": "借りる", "pos": "動詞", "level": "準2級", "example": "Can I borrow your pen for a moment?", "distractors": ["貸す", "盗む", "壊す"]},
    {"word": "director", "meaning": "監督、ディレクター", "pos": "名詞", "level": "準2級", "example": "The director of the movie won an award at the film festival.", "distractors": ["俳優", "脚本家", "プロデューサー"]},
    {"word": "festival", "meaning": "祭り、フェスティバル", "pos": "名詞", "level": "準2級", "example": "The music festival attracts thousands of visitors every year.", "distractors": ["展覧会", "講演会", "卒業式"]},
    {"word": "poster", "meaning": "ポスター", "pos": "名詞", "level": "準2級", "example": "There was a poster for the concert on the wall of the train station.", "distractors": ["看板", "チラシ", "パンフレット"]},
    {"word": "invent", "meaning": "発明する", "pos": "動詞", "level": "準2級", "example": "Thomas Edison invented the light bulb in 1879.", "distractors": ["発見する", "改良する", "模倣する"]},
    {"word": "advertisement", "meaning": "広告", "pos": "名詞", "level": "準2級", "example": "I saw an advertisement for the new smartphone on TV.", "distractors": ["記事", "番組", "ドキュメンタリー"]},
    {"word": "recommend", "meaning": "勧める", "pos": "動詞", "level": "準2級", "example": "The doctor recommended that I get more exercise.", "distractors": ["禁止する", "反対する", "警告する"]},
    {"word": "customer", "meaning": "顧客", "pos": "名詞", "level": "準2級", "example": "The shop has many regular customers who come every week.", "distractors": ["従業員", "経営者", "株主"]},
    {"word": "flavor", "meaning": "味、風味", "pos": "名詞", "level": "準2級", "example": "This ice cream comes in many different flavors.", "distractors": ["色", "香り", "食感"]},
    {"word": "spread", "meaning": "広がる、広める", "pos": "動詞", "level": "準2級", "example": "The news of the accident spread quickly through the town.", "distractors": ["縮小する", "停止する", "集中する"]},
    {"word": "popularity", "meaning": "人気", "pos": "名詞", "level": "準2級", "example": "The popularity of online shopping has grown rapidly.", "distractors": ["品質", "価格", "供給"]},
    {"word": "alcoholic", "meaning": "アルコールの", "pos": "形容詞", "level": "準2級", "example": "Children under 20 are not allowed to buy alcoholic drinks in Japan.", "distractors": ["炭酸の", "有機の", "冷凍の"]},
    {"word": "disease", "meaning": "病気", "pos": "名詞", "level": "準2級", "example": "Washing your hands regularly can help prevent disease.", "distractors": ["怪我", "アレルギー", "疲労"]},
    {"word": "manager", "meaning": "経営者、マネージャー", "pos": "名詞", "level": "準2級", "example": "The manager of the store is responsible for all the staff.", "distractors": ["従業員", "顧客", "株主"]}
]

# Save
with open(os.path.join(base, "_part2.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

total_q = sum(len(s.get("questions",[])) for s in data["sections"]) + sum(len(p.get("questions",[])) for s in data["sections"] for p in s.get("passages",[]))
print(f"Part 2 saved: {total_q} questions, {len(data['vocabulary'])} vocab")
