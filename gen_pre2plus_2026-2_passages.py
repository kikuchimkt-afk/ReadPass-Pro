# -*- coding: utf-8 -*-
"""Original passages transcribed from page images; bilingual reading units.

Rows: natural Japanese, main finite verb phrase, English|Japanese reading
units. The same rows generate paragraphs, translations and sentencePairs.
"""


def passage(label, title, blocks, **extra):
    paragraphs, translations, pairs = [], [], []
    for block in blocks:
        english, japanese = [], []
        for ja, verb, slash in block:
            en = " ".join(unit.split("|",1)[0] for unit in slash.split("||"))
            pairs.append([en, ja, slash, verb])
            english.append(en)
            japanese.append(ja)
        paragraphs.append(" ".join(english))
        translations.append("".join(japanese))
    return dict(label=label, title=title, paragraphs=paragraphs,
                translations=translations, sentencePairs=pairs, questions=[], **extra)


MOOSE = passage("A", "Accidents with Giant Animals", [
    [
        ("ヘラジカはシカ科の中で最も大きな動物だ。", "is", "The moose is the biggest animal|ヘラジカは最も大きな動物だ||in the deer family.|シカ科の中で"),
        ("大人のヘラジカは人間よりはるかに大きく、体重は数百キログラムになることもある。", "is", "An adult moose is much larger than a human|大人のヘラジカは人間よりはるかに大きい||and can weigh several hundred kilograms.|そして体重は数百キログラムになることもある"),
        ("頭についている角は大きく、幅が2メートル近くに達することもある。", "are", "The antlers attached to its head|頭についている角は||are large|大きい||and can reach almost two meters wide.|そして幅が2メートル近くに達することもある"),
        ("ヘラジカは巨大な体をしているが、とても上手に動くことができる。", "can move", "Although the moose has a huge body,|ヘラジカは巨大な体をしているが||it can move very well.|とても上手に動くことができる"),
        ("陸上では、ヘラジカは最高で時速50キロメートルで走ることができる。", "can run", "On land,|陸上では||the moose can run|ヘラジカは走ることができる||up to fifty kilometers per hour.|最高で時速50キロメートルで"),
        ("( 18 )、ヘラジカは泳ぎの名手として知られている。", "is known", "( 18 ),|（18）||it is known as an excellent swimmer.|泳ぎの名手として知られている"),
        ("湖や川で長い距離を移動でき、何秒もの間、完全に水中に潜ることさえできる。", "can travel", "It can travel long distances|長い距離を移動できる||in lakes or rivers|湖や川で||and even go completely under the water|そして完全に水中に潜ることさえできる||for many seconds.|何秒もの間"),
    ], [
        ("車の運転手とヘラジカの間の事故が数多く報告されている。", "have been reported", "Many accidents between car drivers and moose|車の運転手とヘラジカの間の多くの事故が||have been reported.|報告されている"),
        ("例えばカナダでは、そうした事故が一年中起きている。", "happen", "In Canada, for example,|例えばカナダでは||such accidents happen throughout the year.|そうした事故が一年中起きている"),
        ("その大部分は ( 19 ) 起きている。", "occur", "Most of them occur|その大部分は起きている||( 19 ).|（19）"),
        ("これは、ヘラジカが最も活発に動く時間帯だ。", "is", "This is when|これは時間帯だ||the moose is most active.|ヘラジカが最も活発に動く"),
        ("特に、多くの衝突事故は晴れた夜や、まっすぐな道路で起きている。", "occur", "In particular, many crashes occur|特に、多くの衝突事故が起きている||on clear nights and on straight roads.|晴れた夜や、まっすぐな道路で"),
        ("いくつかの研究によれば、道路が曲がっているときや天候が悪いときには、運転手はたいていより注意深くなる。", "are", "According to some studies,|いくつかの研究によれば||drivers are usually more careful|運転手はたいていより注意深い||when roads are curved|道路が曲がっているときや||or when the weather is poor.|天候が悪いときには"),
        ("しかし、晴れた夜には、運転手はあまり注意を払わないことが多い。", "pay", "However, on clear nights,|しかし、晴れた夜には||drivers often pay less attention.|運転手はあまり注意を払わないことが多い"),
        ("このことが、ヘラジカとの事故につながることがある。", "can lead", "This can lead|このことはつながることがある||to accidents with the animal.|その動物との事故に"),
    ], [
        ("ヘラジカとの事故のもう一つの理由は ( 20 ) だ。", "is", "Another reason for moose accidents is|ヘラジカとの事故のもう一つの理由は||( 20 ).|（20）だ"),
        ("ヘラジカは脚が長いため、運転手が視界の中でその体をとらえるのは難しい。", "is", "Because the moose has long legs,|ヘラジカは脚が長いため||it is difficult for drivers|運転手にとって難しい||to see its body within their vision.|視界の中でその体を見ることは"),
        ("夜間、運転手はたいてい、車のヘッドライトを反射する動物の目を見ることができる。", "can usually see", "At night,|夜間||drivers can usually see an animal's eyes|運転手はたいてい動物の目を見ることができる||reflecting a vehicle's headlights.|車のヘッドライトを反射している"),
        ("しかし、ヘラジカの目はふつうとても高い位置にあるため、ライトが目に当たって反射することがない。", "are generally positioned", "However, a moose's eyes are generally positioned so high|しかし、ヘラジカの目はふつうとても高い位置にあるので||that the lights cannot reflect off them.|ライトが目に当たって反射できない"),
        ("さらに、暗い色の毛のせいで、夜間のヘラジカは極めて見えにくい。", "makes", "In addition, its dark-colored fur|さらに、その暗い色の毛は||makes it extremely hard to see|ヘラジカを極めて見えにくくする||at night.|夜間に"),
        ("こうした理由から、運転手が道路上でヘラジカにぶつかる可能性は高い。", "are", "For these reasons,|こうした理由から||the chances of drivers hitting a moose on the road|運転手が道路上でヘラジカにぶつかる可能性は||are high.|高い"),
    ],
])

LOTUS = passage("B", "Lotus Leaves", [
    [
        ("ハスは、世界の多くの地域、特にアジアで育つ水生植物だ。", "is", "The lotus is a water plant|ハスは水生植物だ||that grows in many parts of the world,|世界の多くの地域で育つ||especially in Asia.|特にアジアで"),
        ("これらの地域の人々は、何千年もの間ハスを栽培してきた。", "have been growing", "People in these areas|これらの地域の人々は||have been growing the lotus|ハスを栽培してきた||for thousands of years.|何千年もの間"),
        ("この植物のさまざまな部分が料理に使われている。", "are used", "Various parts of the plant|この植物のさまざまな部分が||are used in cooking.|料理に使われている"),
        ("例えば、その根（レンコン）はよくスープに入れられる。", "are often added", "For example, its roots are often added|例えば、その根はよく加えられる||to soups.|スープに"),
        ("食べられること ( 21 )、ハスは熱などの病気の治療に役立つことから、長い間、伝統医療の一部となってきた。", "has long been", "( 21 ) being eaten,|食べられること（21）||the lotus has long been part of traditional medicine|ハスは長い間、伝統医療の一部となってきた||because it can help treat sicknesses|病気の治療に役立ち得るので||such as fever.|熱などの"),
        ("今日、科学者たちはハスのもう一つの特別な特徴に関心を寄せている。", "are", "Today, scientists are interested|今日、科学者たちは関心を寄せている||in another special feature of the lotus.|ハスのもう一つの特別な特徴に"),
    ], [
        ("ハスの葉の独特な特徴の一つは、( 22 ) 能力だ。", "is", "One unique feature of lotus leaves|ハスの葉の独特な特徴の一つは||is their ability to ( 22 ).|（22）能力だ"),
        ("この特徴は、汚れが葉に付着するのを防ぐのに役立つ。", "helps", "This feature helps|この特徴は役立つ||prevent dirt from sticking to them.|汚れが葉に付着するのを防ぐのに"),
        ("ハスの葉の表面は非常に細かく凸凹しており、さらに葉は一種の天然のろうも作り出す。", "has", "A lotus leaf has a very fine, bumpy surface,|ハスの葉は非常に細かく凸凹した表面をもつ||and it also produces a type of natural wax.|そして一種の天然のろうも作り出す"),
        ("これは、葉に落ちた水が水滴の形のままでいることを意味する。", "means", "This means|これは意味する||that water that lands on the leaf|葉に落ちた水が||stays in the form of drops.|水滴の形のままでいることを"),
        ("風が吹いたり重力が引っ張ったりすると、これらの水滴は葉の上を流れ落ちる。", "run", "When the wind blows or gravity pulls them,|風が吹いたり重力が水滴を引っ張ったりすると||these drops run down the leaf.|これらの水滴は葉の上を流れ落ちる"),
        ("水滴は移動しながら、ほこりや汚れを洗い流す。", "wash away", "As they move,|水滴は移動しながら||the drops wash away dust and dirt.|ほこりや汚れを洗い流す"),
        ("このおかげで、ハスは泥の多い場所でも清潔さを保つことができる。", "helps", "This helps the lotus stay clean|これはハスが清潔さを保つのに役立つ||even in muddy places.|泥の多い場所でさえ"),
    ], [
        ("ハスの葉のこの独特な特徴は ( 23 )。", "", "This unique feature of lotus leaves|ハスの葉のこの独特な特徴は||has ( 23 ).|（23）"),
        ("科学者たちは似た発想を使って、ガラスや布地、建物用のコーティング剤など、自ら汚れを落とす素材を作り出してきた。", "have used", "Scientists have used similar ideas|科学者たちは似た発想を使ってきた||to create self-cleaning materials,|自ら汚れを落とす素材を作り出すために||such as glass, fabrics, and coatings for buildings.|ガラスや布地、建物用のコーティング剤など"),
        ("これらの発明品の中には、表面の小さな傷を修復できるものまであり、そのおかげでより長持ちする。", "can even repair", "Some of these inventions|これらの発明品の中には||can even repair minor surface damage,|表面の小さな傷を修復できるものさえある||which enables them to last longer.|そしてそのことがより長持ちすることを可能にする"),
        ("また、水や洗浄用の化学薬品の使用を減らすのに役立つものもあり、それは環境のためになる。", "help", "Others help reduce the use|ほかのものは使用を減らすのに役立つ||of water and cleaning chemicals,|水や洗浄用の化学薬品の||which benefits the environment.|そしてそれは環境のためになる"),
        ("これらの例は、自然を研究することが人間の問題に対する実用的な解決策につながり得ることを示しており、植物の単純な特徴が日常生活で幅広く応用され得ることを証明している。", "show", "These examples show|これらの例は示している||that studying nature can lead|自然を研究することがつながり得ることを||to practical solutions for human problems,|人間の問題に対する実用的な解決策に||proving that a simple feature of a plant|そして植物の単純な特徴が||can have wide-ranging applications in everyday life.|日常生活で幅広い応用をもち得ることを証明している"),
    ],
])

EMAIL = passage("A", "Invitation to the award ceremony", [
    [
        ("マーカス様", "", "Dear Marcus,|マーカス様"),
        ("セイント・フォール市役所のケイト・ダニエルズです。", "is", "This is Kate Daniels|ケイト・ダニエルズです||from Saint Fall City Hall.|セイント・フォール市役所の"),
        ("先週はお電話でお話しできてうれしかったです。", "was", "It was nice speaking with you|あなたとお話しできてうれしかったです||on the phone last week.|先週、電話で"),
        ("あなたの作品が市の賞を受賞したという知らせをお伝えできて光栄でした。", "was", "It was an honor to share the news|知らせをお伝えできて光栄でした||that your artwork received a city award.|あなたの作品が市の賞を受賞したという"),
        ("作品が選ばれたのは、あなたのすばらしい創造性のためです。", "was chosen", "It was chosen|それは選ばれました||because of your great creativity.|あなたのすばらしい創造性のために"),
        ("本日ご連絡したのは、市がウィットモア・ロビーで授賞式を開くことを決定したことをお知らせするためで、ぜひあなたにご出席いただきたいと考えています。", "writing", "I'm writing today to inform you|本日はお知らせするためにご連絡しています||that the city has decided to hold an award ceremony|市が授賞式を開くことを決定したことを||in the Witmore Lobby,|ウィットモア・ロビーで||and we would like to invite you to attend.|そして、あなたにご出席いただきたいと考えています"),
    ], [
        ("式典は4月23日の夕方に行われます。", "will take place", "The ceremony will take place|式典は行われます||on the evening of April 23.|4月23日の夕方に"),
        ("ほかの受賞者やご家族、先生方、市の職員も出席します。", "will also attend", "Other winners, family members, teachers, and city staff|ほかの受賞者、ご家族、先生方、市の職員も||will also attend.|出席します"),
        ("皆で集まり、芸術と若い才能をたたえます。", "will gather", "Everyone will gather|皆が集まります||to celebrate art and young talent.|芸術と若い才能をたたえるために"),
        ("あなたは壇上で賞を受け取り、市長と一緒に写真を撮る機会もあります。", "will receive", "You will receive your award on stage|あなたは壇上で賞を受け取ります||and have the chance to take photos with the mayor.|そして市長と一緒に写真を撮る機会があります"),
        ("さらに、市の職員による短いインタビューがあり、あなたのコメントの一部は来月の市の新聞に掲載されます。", "will be", "In addition, there will be a short interview|さらに、短いインタビューがあります||with city staff,|市の職員との||and some of your comments will be published|そしてあなたのコメントの一部は掲載されます||in the city's newspaper next month.|来月、市の新聞に"),
    ], [
        ("もう一つお願いがあります。", "have", "We have one more request.|もう一つお願いがあります"),
        ("私たちは、市の多くの人々にあなたの作品を見て楽しんでもらいたいと願っています。", "hope", "We hope|私たちは願っています||that many people in the city|市の多くの人々が||will see and enjoy your work.|あなたの作品を見て楽しむことを"),
        ("そこで、式典の後しばらくの間、作品をウィットモア・ロビーに展示することを検討しています。", "are considering", "Therefore, we are considering displaying it|そこで、作品を展示することを検討しています||in the Witmore Lobby|ウィットモア・ロビーに||for some time after the ceremony.|式典の後しばらくの間"),
        ("これは地域の人々にあなたの作品を楽しむ機会を与え、ほかの生徒たちにも刺激を与えるでしょう。", "will give", "This will give the community an opportunity|これは地域の人々に機会を与えるでしょう||to enjoy your work|あなたの作品を楽しむ||and inspire other students.|そしてほかの生徒たちに刺激を与えるでしょう"),
        ("展示の準備を始められるよう、これにご同意いただけるかどうかお知らせください。", "let", "Please let us know|お知らせください||if you agree to this|これにご同意いただけるかどうか||so that we can start preparing for the display.|展示の準備を始められるように"),
    ], [
        ("よろしくお願いいたします。", "", "Thank you,|よろしくお願いいたします"),
        ("ケイト・ダニエルズ", "", "Kate Daniels|ケイト・ダニエルズ"),
    ],
], format="email")
# Preserve the original mail headers and line breaks, not HTML markup.
EMAIL["meta"] = {"from":"Kate Daniels <contact@saint-fall.com>",
                 "to":"Marcus Jennings <m.jennings@speed-message.net>",
                 "date":"April 14", "subject":"Invitation to the award ceremony"}
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Dear Marcus, ", "Dear Marcus,\n", 1)
EMAIL["translations"][0] = EMAIL["translations"][0].replace("マーカス様", "マーカス様\n", 1)
EMAIL["paragraphs"][-1] = "Thank you,\nKate Daniels"
EMAIL["translations"][-1] = "よろしくお願いいたします。\nケイト・ダニエルズ"

FARM = passage("B", "Staying on the Farm", [
    [
        ("アグリツーリズム（農業体験型の観光）とは、人々が農場やその他の田舎の事業所を訪れ、農場の生活や地域の文化、食べ物を体験する旅行の一種だ。", "is", "Agritourism is a type of travel|アグリツーリズム（農業体験型の観光）は旅行の一種だ||in which people visit farms or other countryside businesses|人々が農場やその他の田舎の事業所を訪れる||to experience farm life, local culture, and food.|農場の生活や地域の文化、食べ物を体験するために"),
        ("こうした訪問を通じて、旅行者は、農場の家に泊まったり、農産物で作られた食事を食べたり、果物や野菜の収穫といった日々の農作業に参加したりするなど、体験型の活動を楽しむことができる。", "can enjoy", "Through these visits,|こうした訪問を通じて||travelers can enjoy hands-on activities,|旅行者は体験型の活動を楽しむことができる||such as staying at a house on the farm,|例えば農場の家に泊まったり||eating meals made from farm products,|農産物で作られた食事を食べたり||or participating in daily farm tasks|日々の農作業に参加したり||like picking fruits and vegetables.|果物や野菜の収穫のような"),
        ("アグリツーリズムは、単なる旅行のスタイルというよりも、地元の農家を支えながら本物の農場体験をする方法を提供するものだ。", "offers", "Rather than being just a style of travel,|単なる旅行のスタイルであるというよりも||agritourism offers a way|アグリツーリズムは方法を提供する||to have authentic farm experiences|本物の農場体験をする||while supporting local farmers.|地元の農家を支えながら"),
    ], [
        ("農業と観光を組み合わせたこの取り組みは、訪問者と農家の双方に多くの利点をもたらし得る。", "can offer", "This approach,|この取り組みは||which combines farming and tourism,|農業と観光を組み合わせた||can offer many advantages|多くの利点をもたらし得る||for both visitors and farmers.|訪問者と農家の双方に"),
        ("農業をよりよく理解することで、訪問者（その多くは都市から来る人々だ）は自然とのつながりをより強く感じることができ、それは心の健康によい。", "can feel", "By understanding farming better,|農業をよりよく理解することで||visitors, many of them from cities,|訪問者は、その多くが都市から来ているが||can feel more connected to nature,|自然とのつながりをより強く感じられる||which is good for their mental health.|そしてそれは心の健康によい"),
        ("一方、農家にとっては、追加の収入を得て事業を成長させる手段となる。", "is", "On the other hand, for farmers,|一方、農家にとっては||it is a way|それは手段だ||to earn extra money and grow their businesses.|追加の収入を得て事業を成長させる"),
        ("また、地域経済に新しい機会を生み出すこともできる。", "can also create", "It can also create new opportunities|それはまた新しい機会を生み出すことができる||for the local economy.|地域経済にとっての"),
        ("都市から来た人々は、地元のコーヒーショップやレストラン、店をよく訪れる。", "visit", "People from cities often visit|都市から来た人々はよく訪れる||local coffee shops, restaurants, and stores.|地元のコーヒーショップやレストラン、店を"),
        ("つまり、アグリツーリズムはさまざまな形で地域全体を支えているのだ。", "supports", "In short, agritourism supports the whole community|つまり、アグリツーリズムは地域全体を支えている||in many ways.|さまざまな形で"),
    ], [
        ("アグリツーリズムが、特に都市に住む人々の間でより人気になった理由はいくつかある。", "are", "There are several reasons|いくつかの理由がある||why agritourism has become more popular,|アグリツーリズムがより人気になった||especially among people in cities.|特に都市の人々の間で"),
        ("一つの理由は、ソーシャルメディアや有名人の影響だ。", "is", "One reason is|一つの理由は||the influence of social media and celebrities.|ソーシャルメディアや有名人の影響だ"),
        ("多くの有名人が農場での体験をインターネット上で共有しており、それがファンに同じことを試してみるよう促している。", "share", "Many celebrities share their farm experiences online,|多くの有名人が農場での体験をネット上で共有している||which encourages their fans|そしてそれがファンを促している||to try the same.|同じことを試してみるように"),
        ("もう一つの理由として、専門家によると、人々は休暇中に心の健康を向上させたいと考えており、それが農場滞在への関心を高めてきたという。", "is", "Another reason is that experts say|もう一つの理由は、専門家によると||people want to improve their mental well-being|人々が心の健康を向上させたいと考えていることだ||during vacations,|休暇中に||which has increased interest in farm stays.|そしてそれが農場滞在への関心を高めてきた"),
        ("これはおそらく、多くの人々が現代生活のストレスや混雑した都市から逃れたいと思っているという事実に関係しているのだろう。", "is likely to relate", "This is likely to relate|これはおそらく関係している||to the fact|事実に||that many people want to escape|多くの人々が逃れたいと思っているという||the stress of modern life and crowded cities.|現代生活のストレスや混雑した都市から"),
    ], [
        ("ある研究によると、世界のアグリツーリズム市場は2032年までに約2,000億ドルに達する可能性がある。", "may reach", "According to one study,|ある研究によると||the global agritourism market may reach|世界のアグリツーリズム市場は達する可能性がある||around 200 billion dollars by 2032.|2032年までに約2,000億ドルに"),
        ("これは2019年の市場規模のほぼ3倍だ。", "is", "This is almost three times the size|これはほぼ3倍の規模だ||of the market in 2019.|2019年の市場の"),
        ("さらに近年、農場でのより長い滞在を楽しむ人が増えている。", "have been enjoying", "Moreover, in recent years,|さらに近年||more people have been enjoying|より多くの人々が楽しむようになっている||longer stays on farms.|農場でのより長い滞在を"),
        ("アメリカでは、2019年から2024年の間に、農場滞在の広告が約70パーセント増加した。", "increased", "In the United States,|アメリカでは||advertisements for farm stays increased by about 70 percent|農場滞在の広告が約70パーセント増加した||between 2019 and 2024.|2019年から2024年の間に"),
        ("このことは、今日人々が家で過ごす時間が増えるにつれて、屋外、特に自然や農業の中で時間を過ごすことへの関心が高まっていることを示しているのかもしれない。", "may show", "This may show|このことは示しているのかもしれない||that as people spend more time at home today,|今日人々が家で過ごす時間が増えるにつれて||they are becoming more interested|より関心をもつようになっていることを||in spending time outside,|屋外で時間を過ごすことに||especially in nature and farming.|特に自然や農業の中で"),
    ],
])


def question(number, choices, translations, answer, analysis, evidence, grammar,
             stem=None, stem_ja=None):
    q = dict(number=number, choices=choices, choiceTranslations=translations,
             answer=answer, choiceAnalysis=analysis, sourceEvidence=evidence, grammar=grammar)
    if stem is not None:
        q.update(question=stem, questionTranslation=stem_ja)
    return q


MOOSE["questions"] = [
    question(18, ["Instead", "What is more", "As a result", "Otherwise"],
             ["その代わりに", "さらに", "その結果", "さもなければ"], 2,
             ["Instead＝その代わりに。走ることをやめて泳ぐという置き換えの関係ではない。", "What is more＝さらに→正解。💡陸上で速く走れることに加えて、泳ぎも得意だという能力を付け加えている。", "As a result＝その結果。速く走れることが、泳ぎが得意なことの原因になっているわけではない。", "Otherwise＝さもなければ。前の内容が成り立たない場合を述べる文脈ではない。"],
             ["Although the moose has a huge body, it can move very well.", "On land, the moose can run up to fifty kilometers per hour.", "it is known as an excellent swimmer."],
             "💡What is more は「さらに・その上」と情報を付け加える表現。巨体でもよく動けるという内容の具体例として、陸上で速く走れること（run）に、泳ぎが得意なこと（swimmer）を加えている。"),
    question(19, ["while it is raining very hard", "especially in times of heavy traffic", "during the dark hours of the day", "early in the summer morning"],
             ["雨が非常に激しく降っている間に", "特に交通量が多い時間帯に", "一日のうちの暗い時間帯に", "夏の早朝に"], 3,
             ["激しい雨の間。本文は、天候が悪いときは運転手がむしろ注意深くなると述べている。", "交通量が多い時間帯。交通量についての記述はない。", "一日の暗い時間帯→正解。💡直後でヘラジカが最も活発な時間帯とし、特に晴れた夜に事故が多いと述べている。", "夏の早朝。事故は一年中起きるとあり、季節や早朝に限る記述はない。"],
             ["This is when the moose is most active.", "In particular, many crashes occur on clear nights and on straight roads."],
             "💡This is when ～ は「これは～する時だ」。when は先行詞 the time を含む関係副詞（＝the time when）で、This が空所の「時間帯」を指している。続く In particular（特に）が on clear nights と具体的に示している。"),
    question(20, ["a certain unique behavior of the moose", "how the moose walks on the road", "vehicles with broken headlights", "some of the moose's physical characteristics"],
             ["ヘラジカのある独特な行動", "ヘラジカが道路をどのように歩くか", "ヘッドライトが壊れた車両", "ヘラジカの身体的特徴のいくつか"], 4,
             ["独特な行動。挙げられているのは脚の長さや目の位置、毛の色で、行動ではない。", "道路での歩き方。歩き方についての説明はない。", "ヘッドライトが壊れた車。ライトの故障ではなく、目の位置が高いため光が反射しないと述べている。", "身体的特徴→正解。💡長い脚、高い位置にある目、暗い色の毛が、夜に見えにくい理由として挙げられている。"],
             ["Because the moose has long legs, it is difficult for drivers to see its body within their vision.", "However, a moose's eyes are generally positioned so high that the lights cannot reflect off them.", "In addition, its dark-colored fur makes it extremely hard to see at night."],
             "💡so ～ that ... は「とても～なので…」。脚の長さ（Because ～）、目の位置の高さ（so high that ～）、毛の色（In addition ～）の3点を physical characteristics（身体的特徴）とまとめている。"),
]
LOTUS["questions"] = [
    question(21, ["In addition to", "Instead of", "Despite", "Far from"],
             ["～に加えて", "～の代わりに", "～にもかかわらず", "～からほど遠い"], 1,
             ["In addition to＝～に加えて→正解。💡料理に使われることに加え、伝統医療にも使われてきたと用途を付け足している。", "Instead of＝～の代わりに。直前で料理に使われると述べており、食べることをやめたわけではない。", "Despite＝～にもかかわらず。食べられることと薬として使われることは対立する内容ではない。", "Far from＝～からほど遠い・決して～ではない。根がスープに入れられるなど、実際に食べられている。"],
             ["Various parts of the plant are used in cooking.", "For example, its roots are often added to soups.", "the lotus has long been part of traditional medicine"],
             "💡In addition to は前置詞と同じはたらきをするので、後ろに名詞や動名詞が来る。being eaten は受け身の動名詞で「食べられること」。料理（食用）と伝統医療（薬用）という2つの用途を並べている。"),
    question(22, ["clean dirty water", "float on water", "contain a lot of water", "keep themselves clean"],
             ["汚れた水をきれいにする", "水に浮く", "多くの水を含む", "自らを清潔に保つ"], 4,
             ["汚れた水をきれいにする。水滴が洗い流すのは葉の上のほこりや汚れで、水を浄化する話ではない。", "水に浮く。葉が水に浮くことについての説明はない。", "多くの水を含む。葉に落ちた水は水滴の形のまま流れ落ちると述べており、水をためる話ではない。", "自らを清潔に保つ→正解。💡汚れが付きにくく、泥の多い場所でも清潔さを保てると述べている。"],
             ["This feature helps prevent dirt from sticking to them.", "As they move, the drops wash away dust and dirt.", "This helps the lotus stay clean even in muddy places."],
             "💡their ability to V は「それら（葉）が～する能力」。prevent A from V-ing は「Aが～するのを防ぐ」。段落最後の stay clean（清潔なままでいる）が keep themselves clean の言い換えになっている。"),
    question(23, ["been used in many countries", "inspired new technologies", "led more students to biology", "caused the lotus population to drop"],
             ["多くの国で使われてきた", "新しい技術を生み出すきっかけとなった", "より多くの学生を生物学へ導いた", "ハスの数を減少させた"], 2,
             ["多くの国で使われてきた。使われた国の数ではなく、似た発想から作られた素材を説明している。", "新しい技術のきっかけ→正解。💡ハスの葉と似た発想から、自ら汚れを落とす素材が作られた。", "生物学を学ぶ学生が増えた。学生や進路についての記述はない。", "ハスの数が減った。ハスの数の変化は述べられていない。"],
             ["Scientists have used similar ideas to create self-cleaning materials, such as glass, fabrics, and coatings for buildings.", "These examples show that studying nature can lead to practical solutions for human problems"],
             "💡has＋過去分詞の現在完了で、これまでに生じた結果を表す。inspire は「（新しいもの）を生み出すきっかけ（着想のもと）となる」。直後の self-cleaning materials（自ら汚れを落とす素材）などの具体例を new technologies とまとめている。"),
]
EMAIL["questions"] = [
    question(24, ["he had been invited to the city's award ceremony.", "the city had chosen him for an award for his artwork.", "an award ceremony would be held in the Witmore Lobby.", "his art talent should be celebrated by the city."],
             ["彼が市の授賞式に招待されていると", "市が作品の賞に彼を選んだと", "授賞式がウィットモア・ロビーで開かれると", "彼の芸術の才能は市にたたえられるべきだと"], 2,
             ["授賞式に招待された。招待は先週の電話ではなく、今日のメールで伝えている内容。", "作品の賞に選ばれた→正解。💡先週の電話で、作品が市の賞を受賞したという知らせを伝えた。", "ロビーで式典を開く。式典の開催が決まったことは、今日のメールで知らせている内容。", "才能は市がたたえるべき。先週伝えたのは受賞の知らせで、このような意見を伝えたとは書かれていない。"],
             ["It was nice speaking with you on the phone last week.", "It was an honor to share the news that your artwork received a city award."],
             "💡It was an honor to share ～ は形式主語の it で「～を伝えられて光栄だった」。the news that ～ の that は同格で「～という知らせ」。last week（先週の電話）と today（今日のメール）で伝えた内容を区別する。",
             "Kate Daniels told Marcus Jennings last week that", "ケイト・ダニエルズは先週、マーカス・ジェニングスに何と伝えましたか。"),
    question(25, ["There will be a quick interview with the mayor.", "The award ceremony will be held in the morning.", "City staff will take pictures of Marcus and his family.", "An interview for the city newspaper will be arranged."],
             ["市長との短いインタビューがある", "授賞式は午前中に開かれる", "市の職員がマーカスと家族の写真を撮る", "市の新聞のためのインタビューが設けられる"], 4,
             ["市長とのインタビュー。インタビューの相手は市の職員で、市長とは一緒に写真を撮る。", "午前中の開催。式典は4月23日の夕方に行われる。", "職員が家族の写真を撮る。写真は市長と一緒に撮る機会があると述べている。", "新聞のためのインタビュー→正解。💡市の職員との短いインタビューがあり、コメントの一部が来月の市の新聞に載る。"],
             ["The ceremony will take place on the evening of April 23.", "In addition, there will be a short interview with city staff, and some of your comments will be published in the city's newspaper next month."],
             "💡there will be ～ は「～がある（予定だ）」。正解4は、本文の a short interview with city staff と some of your comments will be published in the city's newspaper を、An interview for the city newspaper will be arranged と言い換えている。選択肢1は short を quick と言い換えているが、インタビューの相手を the mayor にすり替えている。インタビューの相手（city staff）と写真の相手（the mayor）を区別する。",
             "What will happen on April 23?", "4月23日には何がありますか。"),
    question(26, ["allow the city to exhibit his work for a while.", "hold an art event for others after the ceremony.", "give away his art piece to the city.", "show her more of his art pieces."],
             ["市が作品をしばらく展示することを許可する", "式典の後にほかの人のための芸術イベントを開く", "作品を市に譲る", "彼女にもっと作品を見せる"], 1,
             ["作品の展示を許可する→正解。💡式典の後しばらくウィットモア・ロビーに展示することへの同意を求めている。", "芸術イベントを開く。マーカスにイベントを開くよう頼む記述はない。", "作品を市に譲る。依頼は一定期間の展示で、作品を譲ることではない。", "もっと作品を見せる。ほかの作品を見せるよう頼んではいない。"],
             ["Therefore, we are considering displaying it in the Witmore Lobby for some time after the ceremony.", "Please let us know if you agree to this so that we can start preparing for the display."],
             "💡ask＋人＋if ～ は「人に～かどうか尋ねる」。本文の let us know if you agree to this（同意するかどうか知らせてほしい）が依頼にあたる。display を exhibit、for some time を for a while と言い換えている。",
             "Kate asks Marcus if he could", "ケイトはマーカスに何をしてもらえないかと尋ねていますか。"),
]
FARM["questions"] = [
    question(27, ["It focuses on relaxing in nature, with little activity in farm work.", "It offers visitors some lessons to prepare for a career in agriculture.", "Visitors receive some money while staying on a farm to work.", "Visitors experience a farm lifestyle through work or local food."],
             ["農作業はほとんどせず、自然の中でくつろぐことに重点を置いている", "訪問者に農業の仕事に就く準備のための授業を提供する", "訪問者は農場に滞在して働く間、いくらかのお金を受け取る", "訪問者は作業や地元の食べ物を通じて農場の生活様式を体験する"], 4,
             ["自然の中でくつろぐのが中心で農作業は少ない。本文は日々の農作業への参加を体験の例に挙げている。", "農業の仕事に就く準備の授業。職業訓練についての記述はない。", "滞在中にお金を受け取る。収入を得るのは農家の側で、訪問者がお金を受け取るとは書かれていない。", "作業や食べ物で農場生活を体験→正解。💡農産物で作られた食事や収穫などの農作業を通じて、農場の生活を体験する。"],
             ["Agritourism is a type of travel in which people visit farms or other countryside businesses to experience farm life, local culture, and food.", "Through these visits, travelers can enjoy hands-on activities, such as staying at a house on the farm, eating meals made from farm products, or participating in daily farm tasks like picking fruits and vegetables."],
             "💡a type of travel in which ～ の in which は「前置詞＋関係代名詞」で、「その旅行の中で人々が～する」と前の名詞を説明する。such as のあとに staying / eating / participating の動名詞が並び、具体的な体験を挙げている。",
             "What is true about agritourism?", "アグリツーリズムについて正しいことは何ですか。"),
    question(28, ["It makes farmers rely on local businesses like coffee shops.", "It helps farmers replace traditional farming with a tourism business.", "It benefits visitors' mental well-being through contact with nature.", "It encourages visitors to start new businesses in the countryside."],
             ["農家をコーヒーショップのような地元の店に頼らせる", "農家が従来の農業を観光業に切り替えるのを助ける", "自然との触れ合いを通じて訪問者の心の健康に役立つ", "訪問者に田舎で新しい事業を始めるよう促す"], 3,
             ["農家が地元の店に頼る。地元の店を訪れるのは都市から来た人々で、地域経済への効果として述べている。", "農業を観光業に切り替える。本文は農業と観光を組み合わせる取り組みと説明しており、農業をやめるとは述べていない。", "自然との触れ合いで心の健康→正解。💡自然とのつながりを感じられることが心の健康によいと述べている。", "訪問者が田舎で起業する。新しい機会は地域経済に生まれるもので、訪問者が起業するという記述はない。"],
             ["By understanding farming better, visitors, many of them from cities, can feel more connected to nature, which is good for their mental health."],
             "💡, which is good for ～ の which は、前の内容（自然とのつながりを感じられること）を受ける非制限用法の関係代名詞。is good for their mental health を benefits visitors' mental well-being と言い換えている。",
             "What is one effect that agritourism brings?", "アグリツーリズムがもたらす効果の一つは何ですか。"),
    question(29, ["people are influenced by farm experiences shared online.", "people are worried about rising food prices in cities.", "visitors are offered lessons to learn modern farming methods.", "visitors are invited to move from cities to rural areas."],
             ["人々がネット上で共有された農場体験に影響を受けていること", "人々が都市の食料価格の上昇を心配していること", "訪問者が現代的な農法を学ぶ授業を受けられること", "訪問者が都市から農村部へ移り住むよう誘われていること"], 1,
             ["ネットで共有された体験の影響→正解。💡有名人が農場での体験をネットで共有し、それがファンに同じことを試すよう促している。", "食料価格の上昇への心配。食料価格についての記述はない。", "現代的な農法を学ぶ授業。農法の授業についての記述はない。", "農村部への移住の誘い。本文は訪問や滞在の話で、移住を勧める記述はない。"],
             ["One reason is the influence of social media and celebrities.", "Many celebrities share their farm experiences online, which encourages their fans to try the same."],
             "💡, which encourages ～ の which は前の内容全体を受ける。encourage A to V は「Aに～するよう促す」。本文の share ... online を、選択肢では shared online（ネットで共有された）という過去分詞の後置修飾で言い換えている。",
             "One of the reasons agritourism is getting popular is that", "アグリツーリズムが人気になっている理由の一つは何ですか。"),
    question(30, ["The agritourism market has stopped growing in most countries.", "People are staying longer on farms and spending more time outside.", "More advertisements focus on city attractions instead of farms.", "Farm stays are becoming less popular in the United States today."],
             ["アグリツーリズム市場はほとんどの国で成長が止まっている", "人々は農場により長く滞在し、屋外でより多くの時間を過ごしている", "農場ではなく都市の観光地を取り上げる広告が増えている", "今日アメリカでは農場滞在の人気が下がっている"], 2,
             ["市場の成長が止まった。2032年までに2019年のほぼ3倍に達する可能性があると述べている。", "長期滞在と屋外で過ごす時間→正解。💡農場での長期滞在を楽しむ人が増え、屋外で過ごすことへの関心も高まっている。", "都市の観光地の広告が増加。増えたのは農場滞在の広告で、都市の観光地の広告については述べていない。", "アメリカで人気が低下。農場滞在の広告は約70％増えており、合わない。"],
             ["Moreover, in recent years, more people have been enjoying longer stays on farms.", "they are becoming more interested in spending time outside, especially in nature and farming."],
             "💡have been enjoying は現在完了進行形で「（今まで）ずっと楽しんでいる」。in recent years（近年）とともに、今も続いている最近の傾向を表す。be becoming more interested in V-ing は「～することにより関心をもつようになってきている」。",
             "How is the recent situation of agritourism?", "アグリツーリズムの最近の状況はどうですか。"),
    question(31, ["Both farmers' lives and the local economy could be improved through agritourism.", "Agritourism attracts mainly famous people who want to share their experiences online.", "Fewer people have enjoyed spending a longer time on farms in recent years.", "Areas where agritourism takes place often face negative reactions from the locals."],
             ["アグリツーリズムによって農家の生活と地域経済の両方が改善され得る", "アグリツーリズムは主に、体験をネットで共有したい有名人を引きつけている", "近年、農場で長い時間を過ごすことを楽しむ人は減っている", "アグリツーリズムが行われる地域は、しばしば地元の人々から否定的な反応を受ける"], 1,
             ["農家の生活と地域経済の改善→正解。💡農家は追加の収入を得て事業を伸ばせ、地域経済にも新しい機会が生まれる。", "主に有名人を引きつける。有名人は体験を発信してファンを促す存在で、参加者の中心が有名人とは述べていない。", "長期滞在を楽しむ人が減った。近年は長期滞在を楽しむ人が増えている。", "地元の否定的な反応。地域全体を支えると述べており、反発の記述はない。"],
             ["On the other hand, for farmers, it is a way to earn extra money and grow their businesses.", "It can also create new opportunities for the local economy.", "In short, agritourism supports the whole community in many ways."],
             "💡Both A and B は「AとBの両方」。could be improved は「改善され得る」という可能性を表す受け身。農家の収入（earn extra money）と地域経済（the local economy）という2つの利点を1文にまとめている。",
             "What do we learn from the passage?", "本文からどのようなことが分かりますか。"),
]

PASSAGES = [MOOSE, LOTUS, EMAIL, FARM]
