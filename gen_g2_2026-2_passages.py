# -*- coding: utf-8 -*-
"""Source-verified original passages plus the four-field teaching translations.

Grade 2, 2026 session 2 (main venue). Each row contains natural Japanese, the
main finite verb phrase, and bilingual reading units. English paragraphs and
sentencePairs are derived from these same units so punctuation cannot be
broken by automatic segmentation.
"""


def passage(label, title, blocks, **extra):
    paragraphs, translations, pairs = [], [], []
    for block in blocks:
        english, japanese = [], []
        for ja, verb, slash in block:
            en = " ".join(unit.split("|", 1)[0] for unit in slash.split("||"))
            pairs.append([en, ja, slash, verb])
            english.append(en)
            japanese.append(ja)
        paragraphs.append(" ".join(english))
        translations.append("".join(japanese))
    return dict(label=label, title=title, paragraphs=paragraphs,
                translations=translations, sentencePairs=pairs, questions=[], **extra)


MOUNTAIN = passage("A", "A New Service on the Mountain", [
    [
        ("2020年代初め、タンザニア政府は、人々が利用できるように、キリマンジャロ山に高速インターネットの接続ポイントを設置した。", "installed", "In the early 2020s,|2020年代初めに||the Tanzanian government installed high-speed Internet access points|タンザニア政府は高速インターネットの接続ポイントを設置した||on Mount Kilimanjaro|キリマンジャロ山に||for people to use.|人々が利用できるように"),
        ("最初の接続ポイントは、山の斜面の高い所にあるホロンボ・ハットに設置された。", "was set up", "The first one was set up|最初のものが設置された||at Horombo Huts,|ホロンボ・ハットに||high on the mountain's slopes.|山の斜面の高い所にある"),
        ("その後、登山ルートに沿って、さらに多くの接続ポイントが設置された。", "were placed", "Later,|その後||more access points were placed|さらに多くの接続ポイントが設置された||along the climbing route.|登山ルートに沿って"),
        ("これにより、登山者はガイドに連絡したり、緊急時に救助を要請したりしやすくなった。", "made", "This made it easier for climbers|これにより登山者にとって容易になった||to contact their guides|ガイドに連絡することが||and request rescue|そして救助を要請することが||in case of emergencies.|緊急時に"),
        ("また、山で働く人々がルート案内について連絡を取り合い、( 18 ) ことも可能になった。", "enabled", "It also enabled mountain workers|それはまた山で働く人々に可能にした||to communicate about navigation|ルート案内について連絡を取り合うことを||and to ( 18 ).|そして（18）ことを"),
        ("これにより、彼らは山での急な変化に備えることができ、安全の確保にもつながる。", "can prepare", "This can prepare them|これは彼らに備えさせることができる||for sudden changes on the mountain,|山での急な変化に||ensuring their safety.|そして彼らの安全を確保する"),
    ], [
        ("キリマンジャロ山でインターネットを使えるようにしたもう一つの目的は、観光業を活性化することだった。", "was", "Another purpose|もう一つの目的は||of making the Internet available on Mount Kilimanjaro|キリマンジャロ山でインターネットを使えるようにすることの||was to boost the tourism industry.|観光業を活性化することだった"),
        ("キリマンジャロ山は長年、人気の観光地であり、世界中から多くの訪問者を引きつけてきた。", "has long been", "Mount Kilimanjaro has long been a popular tourist destination,|キリマンジャロ山は長年人気の観光地である||attracting many visitors|多くの訪問者を引きつけながら||from around the world.|世界中から"),
        ("観光客は今では、登山中に写真や動画を投稿できる。", "can now post", "Tourists can now post pictures and videos|観光客は今では写真や動画を投稿できる||during their climb.|登山中に"),
        ("( 19 )、彼らは自分の体験をリアルタイムで共有し、山で経験した困難を見せることができる。", "can share", "( 19 ), they can share their experiences|（19）、彼らは自分の体験を共有できる||in real time|リアルタイムで||and show the challenges|そして困難を見せることができる||they had on the mountain.|山で経験した"),
        ("観光客にとって幸いなことに、キリマンジャロ山のインターネット接続は、現在では山頂まで拡大されている。", "has now been expanded", "Fortunately for tourists,|観光客にとって幸いなことに||Internet access on Mount Kilimanjaro|キリマンジャロ山のインターネット接続は||has now been expanded|現在では拡大されている||all the way to its summit.|山頂まで"),
    ], [
        ("しかし、誰もが喜んだわけではなかった。", "was", "However,|しかし||not everyone was happy.|誰もが喜んだわけではなかった"),
        ("政府は観光客のほうに多くの関心を向けている、と言う批判的な人々もいた。", "said", "Some critics said|一部の批判的な人々は言った||the government was giving more attention|政府がより多くの関心を向けていると||to tourists.|観光客に"),
        ("タンザニアの多くの農村地域は ( 20 )。", "", "Many rural communities in Tanzania|タンザニアの多くの農村地域は||( 20 ).|（20）"),
        ("そのため、そうした資源は地元住民のための通信サービスを改善することにもっと使われるべきだ、という批判があった。", "were", "Therefore,|そのため||there were criticisms|批判があった||that the resources should be used more|そうした資源がもっと使われるべきだという||to improve communication services|通信サービスを改善するために||for local residents.|地元住民のための"),
        ("一方で、山での安全面の利点や緊急時の連絡手段を理由に、この新しいサービスを歓迎する人々もいた。", "welcomed", "On the other hand,|一方で||some people welcomed the new service|この新しいサービスを歓迎する人々もいた||for its safety benefits and emergency communication|安全面の利点や緊急時の連絡を理由に||on the mountain.|山での"),
        ("要するに、この事業は議論を引き起こしたが、キリマンジャロ山の登山中に人々が安全を保つ方法や、旅の様子をリアルタイムで共有する方法を変えもした。", "has caused", "In short,|要するに||the project has caused debate,|この事業は議論を引き起こした||but it has also changed|しかしそれはまた変えた||how people stay safe|人々が安全を保つ方法を||while climbing Mount Kilimanjaro|キリマンジャロ山に登っている間に||and how they share their journeys|そして旅の様子を共有する方法を||in real time.|リアルタイムで"),
    ],
])

BATS = passage("B", "Bats", [
    [
        ("コウモリは、自然環境と人々の生活の両方にとって重要な役割を果たしている。", "play", "Bats play an important role|コウモリは重要な役割を果たしている||both for the natural environment and people's lives.|自然環境と人々の生活の両方にとって"),
        ("コウモリは、ハエやガなど、植物に害を与える多くの昆虫を食べる。", "eat", "They eat many insects,|コウモリは多くの昆虫を食べる||such as flies and moths,|ハエやガなど||that harm plants.|植物に害を与える"),
        ("1匹のコウモリが一晩に何千匹もの昆虫を食べられるため、農家は作物に使う化学薬品の量を減らすことができる。", "can reduce", "Since one bat can eat thousands of insects a night,|1匹のコウモリが一晩に何千匹もの昆虫を食べられるため||farmers can reduce the amount of chemicals|農家は化学薬品の量を減らすことができる||they use on their crops.|作物に使う"),
        ("さらに、コウモリは ( 21 ) ことによって、多くの植物が育つのを助けている。", "help", "In addition,|さらに||bats help many plants grow|コウモリは多くの植物が育つのを助けている||by ( 21 ).|（21）ことによって"),
        ("これにより、新しい植物が親の植物から遠く離れた場所で育ち始めることができる。", "allows", "This allows new plants to start growing|これにより新しい植物が育ち始めることができる||far from the parent plant.|親の植物から遠く離れた場所で"),
        ("残念なことに、コウモリの個体数は世界中で減少している。", "are falling", "Unfortunately,|残念なことに||bat populations are falling|コウモリの個体数は減少している||across the globe.|世界中で"),
        ("その数が減り続ければ、環境や食料生産に深刻な問題が起こるかもしれない。", "might occur", "If the number continues to decline,|その数が減り続ければ||a serious problem might occur|深刻な問題が起こるかもしれない||for the environment and food production.|環境や食料生産にとって"),
    ], [
        ("北米の一部の地域では、多くのコウモリが白鼻症候群と呼ばれる病気で死んでいる。", "are dying", "In some parts of North America,|北米の一部の地域では||many bats are dying|多くのコウモリが死んでいる||from a disease called white-nose syndrome.|白鼻症候群と呼ばれる病気で"),
        ("この名前は、眠っているコウモリの顔や翼に見られる白い斑点に由来する。", "comes", "The name comes|この名前は由来する||from white marks|白い斑点に||on the faces or wings of sleeping bats.|眠っているコウモリの顔や翼にある"),
        ("この病気は、コウモリが冬の間眠る洞窟やトンネルの中で広がる。", "spreads", "It spreads|それは広がる||in the caves and tunnels|洞窟やトンネルの中で||where bats sleep for the winter.|コウモリが冬の間眠る"),
        ("この病気は、コウモリを冬眠から目覚めさせてしまう。", "wakes up", "The disease wakes up the bats|この病気はコウモリを目覚めさせる||from their winter sleep.|冬眠から"),
        ("( 22 )、いったん目覚めると、コウモリは動き回り始め、そのせいで蓄えておいた体脂肪を失ってしまう。", "begin", "( 22 ), once awake,|（22）、いったん目覚めると||they begin to move around,|コウモリは動き回り始める||causing them to lose the body fat|そしてそのせいで体脂肪を失う||that they have stored.|蓄えておいた"),
        ("冬の間は十分な食料がないため、多くのコウモリが最終的に死んでしまう。", "end up", "Since there are not enough food sources|十分な食料源がないため||during the winter,|冬の間は||many bats end up dying.|多くのコウモリが最終的に死んでしまう"),
    ], [
        ("科学者や活動家たちは、コウモリの個体数を守るためにさまざまな対策を講じている。", "are taking", "Scientists and activists are taking various measures|科学者や活動家たちはさまざまな対策を講じている||to protect the bat population.|コウモリの個体数を守るために"),
        ("例えば、冬に洞窟に入り、コウモリの数を数えたり様子を観察したりしている。", "enter", "For example,|例えば||they enter caves in winter|彼らは冬に洞窟に入る||to count and monitor the bats.|コウモリの数を数えたり観察したりするために"),
        ("また、コウモリに安全な休息場所を与えるため、人工の洞窟などの特別な生息環境も作られている。", "have also been created", "Special habitats, such as artificial caves,|人工の洞窟などの特別な生息環境も||have also been created|作られている||to give bats safe places to rest.|コウモリに安全な休息場所を与えるために"),
        ("さらに、専門家たちは、さまざまなコウモリが ( 23 ) ために何を必要としているのかを研究している。", "are studying", "Also,|さらに||experts are studying|専門家たちは研究している||what various bats need to ( 23 ).|さまざまなコウモリが（23）ために何を必要とするかを"),
        ("小型の追跡装置を取り付けて活動を観察し、これらのコウモリが冬の数か月間にどのようにエネルギーを保っているのかを理解しようとしている。", "attach", "They attach small tracking devices|彼らは小型の追跡装置を取り付ける||to monitor their activities|コウモリの活動を観察するために||and understand|そして理解するために||how these bats maintain energy|これらのコウモリがどのようにエネルギーを保つかを||during the winter months.|冬の数か月間に"),
    ],
])

EMAIL = passage("A", "Question about some furniture", [
    [
        ("ジョージ・ヘンダーソン様", "", "Dear George Henderson,|ジョージ・ヘンダーソン様"),
        ("ケイティ・ルイスと申します。隣の市でクラフトショップを経営しております。", "is", "My name is Katy Lewis,|私の名前はケイティ・ルイスです||and I run a craft shop|そしてクラフトショップを経営しています||in the neighboring city.|隣の市で"),
        ("当店は改装を予定しており、家具の一部をお譲りしたいと考えております。", "are going to renovate", "We are going to renovate our shop|当店は改装する予定です||and want to give away|そして譲りたいと考えています||some of the furniture.|家具の一部を"),
        ("現在、テーブルと棚がいくつかございます。", "have", "Currently,|現在||we have some tables and shelves.|テーブルと棚がいくつかあります"),
        ("店の配置が変わるため、それらはもう必要なくなります。", "no longer need", "We'll no longer need them|それらはもう必要なくなります||as the shop's layout is being changed.|店の配置が変更されるため"),
        ("家具はどれも状態が良く、貴店のような中古品店なら引き取っていただけるのではないかと考えました。", "is", "The furniture is all in good condition,|家具はすべて状態が良いです||and I thought|そして私は考えました||a secondhand shop like yours|貴店のような中古品店なら||might be able to accept it.|それを引き取れるかもしれないと"),
    ], [
        ("全部で5点ございます。", "have", "We have five pieces|5点あります||in total.|全部で"),
        ("どれも木製で大きすぎず、一般的な広さのお店にちょうどよい大きさです。", "are made", "They are made of wood|それらは木製です||and are not too big,|そして大きすぎません||just the right size|ちょうどよい大きさです||for a regular-sized shop.|一般的な広さの店に"),
        ("いくつか傷はありますが、修理が必要なほど大きな傷ではありません。", "have", "They have some scratches,|いくつか傷があります||but not large scratches|しかし大きな傷ではありません||that require repair.|修理を必要とするような"),
        ("一つ一つはそれほど大きくありませんが、5点すべてを合わせると、やはりトラックなしで運ぶには重すぎます。", "are", "Even though each one isn't very large,|一つ一つはそれほど大きくありませんが||all five together are still too heavy|5点すべてを合わせるとやはり重すぎます||to carry without a truck.|トラックなしで運ぶには"),
        ("引き取りに来ていただけますか。", "come", "Could you come|来ていただけますか||to pick them up?|それらを引き取りに"),
        ("その場合、費用はかかりますか。", "be", "Would there be a cost|費用はかかりますか||for doing that?|そうすることに対して"),
    ], [
        ("もし引き取っていただけない場合は、ほかの店が必要としているかどうかを確認しなければなりません。", "will need", "In case you are unable to accept the items,|もし品物を引き取れない場合は||I will need to check|確認する必要があります||whether other shops might want them.|ほかの店がそれらを欲しがるかどうかを"),
        ("まだ使っていただける方がいるのであれば、捨てたくはありません。", "don't want", "I don't want to throw the items away|品物を捨てたくはありません||if someone can still use them.|まだ誰かが使えるのであれば"),
        ("ほかの店に連絡して返事を待つには時間がかかるかもしれないので、早めにお知らせいただけるとありがたいです。", "may take", "Contacting other shops|ほかの店に連絡すること||and waiting for their replies|そして返事を待つことは||may take some time,|時間がかかるかもしれません||so I would appreciate it|ですのでありがたく思います||if you could let me know soon.|早めにお知らせいただけると"),
        ("改装業者が2週間後に作業を始めるため、今週の金曜日までに、この件についてのお考えをお知らせください。", "let", "Since the renovation crew will start working|改装業者が作業を始めるので||in two weeks,|2週間後に||please let me know|お知らせください||what you think about this|この件についてどうお考えかを||by this Friday.|今週の金曜日までに"),
    ], [
        ("敬具", "", "Sincerely,|敬具"),
        ("ケイティ・ルイス", "", "Katy Lewis|ケイティ・ルイス"),
        ("ムーンウェーブ・クラフトショップ", "", "Moonwave Craft Shop|ムーンウェーブ・クラフトショップ"),
    ],
], format="email", meta={"from": "Katy Lewis <klewis@moonwave.com>", "to": "George Henderson <ghenderson@earthlinker.com>", "date": "February 8", "subject": "Question about some furniture"})
# Retain line breaks in the original greeting and closing/signature, without
# changing paragraph boundaries.
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Dear George Henderson, ", "Dear George Henderson,\n", 1)
EMAIL["paragraphs"][-1] = "Sincerely,\nKaty Lewis\nMoonwave Craft Shop"
EMAIL["translations"][0] = EMAIL["translations"][0].replace("ジョージ・ヘンダーソン様", "ジョージ・ヘンダーソン様\n", 1)
EMAIL["translations"][-1] = "敬具\nケイティ・ルイス\nムーンウェーブ・クラフトショップ"

CARTS = passage("B", "Shopping Carts", [
    [
        ("ショッピングカートは、1930年代にシルバン・ゴールドマンによって発明された。", "was invented", "The shopping cart was invented|ショッピングカートは発明された||by Sylvan Goldman|シルバン・ゴールドマンによって||in the 1930s.|1930年代に"),
        ("彼は、かごが重くなりすぎて持てなくなるために、買い物客が買い物を続けにくくなっていることに気づき、解決策を探した。", "noticed", "He noticed|彼は気づいた||that shoppers had difficulty continuing shopping|買い物客が買い物を続けるのに苦労していることに||because their baskets became too heavy to carry,|かごが重くなりすぎて持てなくなるため||and he looked for a solution.|そして解決策を探した"),
        ("彼の最初のショッピングカートは、折りたためる簡素ないすで作られていた。", "was made", "His first shopping cart was made|彼の最初のショッピングカートは作られていた||of a simple chair|簡素ないすで||that could be folded.|折りたたむことができる"),
        ("それには、2つのかごと車輪が付いていた。", "had", "It had|それには付いていた||two baskets and wheels.|2つのかごと車輪が"),
        ("このショッピングカートのおかげで、人々はもう重いかごを持ち運ぶ必要がなくなった。", "did not have to carry", "With this shopping cart,|このショッピングカートがあれば||people did not have to carry heavy baskets anymore.|人々はもう重いかごを持ち運ぶ必要がなかった"),
        ("その代わりに、カートを押せばよかった。", "could push", "They could push the cart|彼らはカートを押すことができた||instead.|その代わりに"),
        ("その後まもなく、彼は自分の店にそのカートを導入し、人々の買い物の仕方を変えたいと願った。", "introduced", "Soon after,|その後まもなく||he introduced the carts at his store|彼は自分の店にそのカートを導入した||and hoped to change the way|そして方法を変えたいと願った||people shopped.|人々が買い物をする"),
    ], [
        ("この発明以前、人々は買い物の間、かごを腕に抱えて持ち歩いていた。", "carried", "Before the invention,|この発明以前は||people carried baskets around with their arms|人々はかごを腕で持ち歩いていた||while shopping.|買い物の間"),
        ("そのため、一度にたくさんの品物を買うのは難しく、かごが重くなりすぎて持てなくなると、買い物をやめてしまうことが多かった。", "was difficult", "Therefore,|そのため||it was difficult to shop for many items at once,|一度にたくさんの品物を買うのは難しかった||and they often stopped shopping|そして人々はしばしば買い物をやめた||once the basket was too heavy to carry.|かごが重くなりすぎて持てなくなると"),
        ("スーパーマーケットが大型化し、車を運転する人が増えるにつれて、人々は1回の買い物でより多くの品物を買うようになった。", "started", "As supermarkets grew larger|スーパーマーケットが大きくなるにつれて||and more people began driving cars,|そしてより多くの人々が車を運転し始めるにつれて||people started buying more items|人々はより多くの品物を買い始めた||in a single shopping trip.|1回の買い物で"),
        ("ショッピングカートは、楽に便利に買い物ができる買い物客と、売り上げを伸ばせるスーパーマーケットの経営者の両方にとって、役立つものになり得た。", "could be", "Shopping carts could be helpful|ショッピングカートは役に立ち得た||to both shoppers,|買い物客にとっても||who could shop easily and conveniently,|買い物客は楽に便利に買い物ができ||and supermarket owners,|そしてスーパーマーケットの経営者にとっても||who could increase their sales.|経営者は売り上げを伸ばすことができた"),
    ], [
        ("しかし、当初、買い物客はショッピングカートを使いたがらなかった。", "did not like", "However, at first,|しかし当初は||shoppers did not like using shopping carts.|買い物客はショッピングカートを使うのを好まなかった"),
        ("ショッピングカートが、赤ちゃんを乗せて運ぶためのベビーカーのように見えると考える女性もいれば、自分でかごを持たずにカートを使うと男らしくなく見えると考える男性もいた。", "thought", "Some women thought|一部の女性は考えた||shopping carts looked like baby strollers,|ショッピングカートがベビーカーのように見えると||which were used for carrying babies,|ベビーカーは赤ちゃんを運ぶために使われていた||and some men thought|そして一部の男性は考えた||using the carts without holding baskets themselves|自分でかごを持たずにカートを使うことは||would make them look less manly.|自分を男らしくなく見せるだろうと"),
        ("ゴールドマンは、人々の考えを変える巧みな方法を見つけなければならなかった。", "had to find", "Goldman had to find a clever way|ゴールドマンは巧みな方法を見つけなければならなかった||to change their minds.|人々の考えを変える"),
        ("彼は人を雇い、ショッピングカートを押しながら店内を歩き回って、カートがいかに便利かを実演してもらった。", "hired", "He hired people|彼は人々を雇った||who walked around his store|店内を歩き回る||pushing the shopping carts|ショッピングカートを押しながら||and demonstrating|そして実演しながら||how useful the carts were.|カートがいかに便利かを"),
        ("ほかの人が快適にカートを使っているのを見ると、客たちも使い始めた。", "started", "When customers saw others|客たちがほかの人を見ると||using the carts comfortably,|カートを快適に使っているのを||they started using them too.|彼らもそれを使い始めた"),
        ("まもなくショッピングカートは人気を集めて広く受け入れられ、ほかの店も自分の店の客のためにカートを買いたがった。", "became", "Soon,|まもなく||shopping carts became popular and widely accepted,|ショッピングカートは人気を集め広く受け入れられた||and other stores wanted to buy them|そしてほかの店もそれを買いたがった||for their own customers.|自分の店の客のために"),
    ], [
        ("ショッピングカートは、時代とともに改良されてきた。", "have been improved", "Shopping carts have been improved|ショッピングカートは改良されてきた||over time.|時とともに"),
        ("20世紀半ばには、より狭い場所に多くのカートを収納できるよう、新しいカートが設計された。", "was designed", "In the middle of the twentieth century,|20世紀半ばに||a new cart was designed|新しいカートが設計された||so that many carts could be stored|多くのカートを収納できるように||in a smaller area.|より狭い場所に"),
        ("その後、人々が幼い子どもを連れてより安全に買い物をする方法を求めるようになったことから、子ども用の座席に安全ベルトも付けられた。", "was also added", "Later,|その後||a safety belt for children's seats was also added|子ども用の座席の安全ベルトも付けられた||as people looked for safer ways|人々がより安全な方法を求めたので||to shop with young children.|幼い子どもを連れて買い物をする"),
        ("今日では、何百万台ものショッピングカートが世界中の店で広く使われている。", "are widely used", "Nowadays,|今日では||millions of shopping carts are widely used|何百万台ものショッピングカートが広く使われている||in stores around the world.|世界中の店で"),
        ("ショッピングカートの発明は、買い物をずっと楽にし、店の大型化を可能にし、人々が食料品やほかの日用品を買う方法を根本的に変えた。", "made", "The invention of shopping carts|ショッピングカートの発明は||made shopping much easier,|買い物をずっと楽にした||allowed stores to grow larger,|店がより大きくなることを可能にした||and fundamentally changed the way|そして方法を根本的に変えた||people buy groceries and other household goods.|人々が食料品やほかの日用品を買う"),
    ],
])


def question(p, number, choices, translations, answer, analysis, grammar,
             evidence_indexes, stem=None, stem_ja=None):
    q = dict(number=number, choices=choices, choiceTranslations=translations,
             answer=answer, choiceAnalysis=analysis, grammar=grammar,
             sourceEvidence=[p["sentencePairs"][i][0] for i in evidence_indexes])
    if stem is not None:
        q.update(question=stem, questionTranslation=stem_ja)
    p["questions"].append(q)


question(MOUNTAIN, 18,
         ["check the current weather", "carry extra equipment", "take photos of the mountain", "arrange accommodation in town"],
         ["現在の天気を確認する", "予備の装備を運ぶ", "山の写真を撮る", "町で宿泊先を手配する"], 1,
         ["現在の天気を確認する→正解。💡次の文の「山での急な変化に備えられる」と自然につながる。", "予備の装備を運ぶ。インターネットで連絡を取り合う話で、装備の運搬とは関係がない。", "山の写真を撮る。写真の投稿は第2段落の観光客の話で、山で働く人々の安全とは結びつかない。", "町で宿泊先を手配する。山での急な変化への備えにつながらない。"],
         "💡enable＋人＋to V は「人が～できるようにする」で、to communicate と to ( 18 ) が and で並ぶ。次の文の prepare＋人＋for ～「人に～への備えをさせる」と sudden changes（急な変化）が、天気の確認と結びつく手がかり。", [4,5])
question(MOUNTAIN, 19, ["Instead", "By doing so", "In contrast", "Otherwise"],
         ["その代わりに", "そうすることで", "対照的に", "そうでなければ"], 2,
         ["その代わりに。投稿をやめて別のことをするという流れではない。", "そうすることで→正解。💡写真や動画を投稿することで、体験をリアルタイムで共有できるという手段と結果の関係。", "対照的に。前の文と対立する内容ではなく、投稿の効果を述べている。", "そうでなければ。投稿しない場合の結果を述べる文ではない。"],
         "💡by doing so の so は前の文の post pictures and videos を受け、「そうする（写真や動画を投稿する）ことによって」という手段を表す。can share ... and show ～ と動詞が and で並ぶ。", [8,9])
question(MOUNTAIN, 20,
         ["always share pictures with tourists", "recently built new public schools", "already use the Internet freely", "still lack reliable Internet access"],
         ["いつも観光客と写真を共有している", "最近新しい公立学校を建てた", "すでに自由にインターネットを使っている", "いまだに安定したインターネット接続がない"], 4,
         ["観光客と写真を共有している。地元住民の通信サービスを改善すべきだという次の文の批判につながらない。", "新しい公立学校を建てた。学校の話は本文になく、通信サービスへの批判と関係がない。", "すでに自由にインターネットを使っている。それなら地元向けの通信改善を求める批判とつながらない。", "いまだに安定した接続がない→正解。💡次の文で、資源を地元住民の通信サービス改善に使うべきだという批判が続く。"],
         "💡次の文の Therefore は「そのため」で、( 20 ) の内容が批判の理由になる。there were criticisms that ～ の that 節は criticisms の内容を説明する同格節。lack は他動詞なので、前置詞なしで目的語をとる。", [13,14])

question(BATS, 21,
         ["keeping their flowers and leaves clean", "living under the leaves of large plants", "eating the unnecessary leaves of plants", "carrying their seeds to different places"],
         ["花や葉をきれいに保つ", "大きな植物の葉の下で暮らす", "植物の不要な葉を食べる", "種をさまざまな場所へ運ぶ"], 4,
         ["花や葉をきれいに保つ。新しい植物が親から離れて育つという次の文につながらない。", "大きな植物の葉の下で暮らす。すみかの話で、植物の成長を助ける方法ではない。", "植物の不要な葉を食べる。コウモリが食べるのは昆虫で、葉を食べるとは書かれていない。", "種をさまざまな場所へ運ぶ→正解。💡次の文の「親の植物から遠く離れて育ち始める」と一致。"],
         "💡help＋目的語＋動詞の原形 は「～が…するのを助ける」。by の後は動名詞（～ing）で手段を表す。次の文の This は ( 21 ) の内容を指し、allow＋目的語＋to V「～が…できるようにする」と続く。", [3,4])
question(BATS, 22, ["For this purpose", "As a result", "Likewise", "On the other hand"],
         ["この目的のために", "その結果", "同様に", "一方で"], 2,
         ["この目的のために。コウモリが目覚めるのは目的ではなく、病気によって起こること。", "その結果→正解。💡病気で冬眠から目覚めた結果、動き回って体脂肪を失うという因果関係。", "同様に。前の文と似た別の事柄を並べているわけではない。", "一方で。前の文と対照的な内容ではない。"],
         "💡once awake は once they are awake の省略で「いったん目覚めると」。causing them to lose ～ は分詞構文で、動き回ることが結果として体脂肪を失わせることを表す。that they have stored は the body fat を説明する関係代名詞節。", [10,11])
question(BATS, 23,
         ["travel to warmer countries", "survive the cold winter", "give birth in the caves", "sleep in large groups"],
         ["より暖かい国へ移動する", "寒い冬を生き延びる", "洞窟で子どもを産む", "大きな集団で眠る"], 2,
         ["より暖かい国へ移動する。追跡装置で調べるのは冬の間のエネルギーの保ち方で、移動先ではない。", "寒い冬を生き延びる→正解。💡次の文の「冬の数か月間にどのようにエネルギーを保つか」と一致。", "洞窟で子どもを産む。出産については本文に書かれていない。", "大きな集団で眠る。集団の大きさについては述べられていない。"],
         "💡what various bats need to ～ は間接疑問で「さまざまなコウモリが～するために何を必要としているか」。to ( 23 ) は目的を表す不定詞。次の文の maintain energy during the winter months が手がかり。", [16,17])

question(EMAIL, 24,
         ["Because she is searching for furniture that suits her new layout.", "Because she is planning to sell her shop to someone in the city.", "Because she wants to offer some used items for his shop.", "Because she hopes to sell handmade items at his secondhand shop."],
         ["新しい配置に合う家具を探しているから。", "市内の誰かに自分の店を売ることを計画しているから。", "彼の店に中古の品物を提供したいから。", "彼の中古品店で手作りの品を売りたいから。"], 3,
         ["新しい配置に合う家具を探している。家具を探すのではなく、不要になる家具を譲ろうとしている。", "店を売る計画。店は売るのではなく改装する予定。", "中古の品物を提供したい→正解。💡家具の一部を譲りたいと書き、貴店なら引き取れるかもしれないと考えている。", "手作りの品を売りたい。クラフトショップを経営しているが、譲りたいのは店の家具。"],
         "💡give away は「（無償で）譲る、手放す」。I thought ～ might be able to accept it の might は控えめな推量で、相手に配慮した言い方。選択肢の used items は本文の furniture（tables and shelves）の言い換え。", [2,5],
         "Why does Katy Lewis write this email to George Henderson?", "ケイティ・ルイスがジョージ・ヘンダーソンにこのメールを書いているのはなぜですか。")
question(EMAIL, 25,
         ["she cannot transport all five items without the shop's help.", "she cannot sell the items without having them checked beforehand.", "the shop cannot receive her payment through an online system.", "the shop cannot accept items delivered by mail or in person."],
         ["店の手助けがなければ、5点すべてを運ぶことができないから。", "事前に点検してもらわなければ、品物を売ることができないから。", "店がオンラインのシステムで彼女からの支払いを受け取れないから。", "店が郵送や持ち込みで届けられた品物を受け付けられないから。"], 1,
         ["店の手助けなしでは5点を運べない→正解。💡5点合わせるとトラックなしでは重すぎると書き、引き取りに来てほしいと頼んでいる。", "事前の点検が必要。点検の話はなく、修理が必要な大きな傷もないと述べている。", "オンラインで支払いを受け取れない。オンラインでの支払いについての記述はなく、尋ねているのは引き取りに費用がかかるかどうか。", "郵送や持ち込みを受け付けない。ジョージの店の受け入れ方法については書かれていない。"],
         "💡Even though は「～だけれども」と譲歩を表す。too heavy to carry は「重すぎて運べない」。Could you ～? は丁寧な依頼で、pick ～ up は「～を引き取る」。設問の wish (that)＋主語＋would＋動詞の原形 は「（主語が）～してくれたらと願う」で、ここでは somebody from George's shop が主語。", [9,10],
         "Katy wishes somebody from George's shop would visit her because", "ケイティがジョージの店のだれかに来てほしいと願っているのは、～。")
question(EMAIL, 26,
         ["she should close the shop permanently on that day as planned.", "she may need time to ask other shops if they are interested.", "the renovation team may want to use the furniture.", "the renovation work will begin sometime this week."],
         ["予定どおり、その日で店をたたむ（永久に閉める）ことになっているから。", "ほかの店に興味があるかどうかを尋ねる時間が必要になるかもしれないから。", "改装チームがその家具を使いたがるかもしれないから。", "改装工事が今週中に始まるから。"], 2,
         ["その日で店をたたむ。店はたたむのではなく改装する予定。", "ほかの店に尋ねる時間が必要→正解。💡ほかの店への連絡と返事待ちに時間がかかるかもしれないと書いている。", "改装チームが家具を使う。改装業者について述べているのは作業開始の時期だけ。", "今週中に工事が始まる。作業開始は2週間後で、今週ではない。"],
         "💡In case ～ は「～の場合には」。Contacting ... and waiting ... は動名詞の主語で、may take some time は「時間がかかるかもしれない」。I would appreciate it if you could ～ は「～していただけるとありがたい」という丁寧な依頼。", [12,14,15],
         "Katy wants a reply by Friday because", "ケイティが金曜日までに返事をほしいと考えているのは、～。")

question(CARTS, 27,
         ["a rolling chair with one fixed basket that people could not fold.", "a folding chair with wheels and two baskets used for easy shopping.", "a chair with two handles that came off easily and four wheels.", "a chair with one large basket under the seat and no wheels."],
         ["固定されたかごが1つ付いた、折りたためない車輪付きのいすだった。", "楽に買い物をするために使われる、車輪と2つのかごが付いた折りたたみいすだった。", "簡単に外れる2つの取っ手と、4つの車輪が付いたいすだった。", "座面の下に大きなかごが1つあり、車輪のないいすだった。"], 2,
         ["折りたためない、かご1つのいす。本文では折りたためるいすで、かごは2つ。", "車輪と2つのかごが付いた折りたたみいす→正解。💡折りたためる簡素ないすに、2つのかごと車輪が付いていた。", "外れやすい取っ手と4つの車輪。取っ手や車輪の数については書かれていない。", "大きなかご1つで車輪なし。本文ではかごは2つで、車輪も付いていた。"],
         "💡be made of ～ は「～で作られている」。that could be folded は chair を説明する関係代名詞節で「折りたたむことができる」。選択肢の folding chair（折りたたみいす）がこれを言い換えている。", [2,3],
         "The first shopping cart designed by Sylvan Goldman was", "シルバン・ゴールドマンが設計した最初のショッピングカートは、～。")
question(CARTS, 28,
         ["The size of the supermarkets and the number of shoppers with cars increased.", "Supermarkets began to provide shopping baskets that shoppers could take home.", "Store owners offered various discounts for those people who bought large amounts.", "People's lifestyles became busier, and they could not find time for shopping."],
         ["スーパーマーケットの規模と、車を持つ買い物客の数が増えたから。", "スーパーマーケットが、買い物客が持ち帰れる買い物かごを提供し始めたから。", "店の経営者が、大量に買う人々にさまざまな割引を提供したから。", "人々の生活が忙しくなり、買い物の時間が取れなくなったから。"], 1,
         ["スーパーの大型化と車を使う買い物客の増加→正解。💡スーパーが大きくなり、車を運転する人が増えたとある。", "持ち帰れるかごの提供。かごを持ち帰れるという記述はない。", "大量購入への割引。割引についての記述はない。", "生活が忙しくなった。生活の忙しさについては書かれていない。"],
         "💡As は「～するにつれて」と変化に伴う関係を表す接続詞。grew larger（大きくなった）と more people began driving cars が、選択肢の The size ... increased と the number of shoppers with cars increased に言い換えられている。", [9],
         "Why did people start buying more items in a single shopping trip?", "人々が1回の買い物でより多くの品物を買い始めたのはなぜですか。")
question(CARTS, 29,
         ["offering them special discounts for using the carts.", "changing their design to make the carts more appealing.", "showing men using the carts in the store in advertisements.", "hiring people to demonstrate using the carts in the store."],
         ["カートを使う客に特別な割引を提供すること。", "カートをより魅力的にするために、デザインを変えること。", "店内でカートを使う男性の姿を、広告で見せること。", "人を雇って、店内でカートを使う様子を実演させること。"], 4,
         ["特別な割引の提供。割引についての記述はない。", "デザインの変更。考えを変えるために行ったのは実演で、デザインの変更ではない。", "男性がカートを使う広告。男性の抵抗感は述べられているが、広告は出てこない。", "人を雇って実演させる→正解。💡カートを押して店内を歩き、便利さを実演する人を雇った。"],
         "💡who walked around ... は people を説明する関係代名詞節。pushing と demonstrating は「～しながら」を表す分詞。demonstrating how useful the carts were は「カートがいかに便利かを実際にやって見せる」。", [13,14],
         "Goldman convinced shoppers to use shopping carts by", "ゴールドマンが買い物客にショッピングカートを使うよう説得した方法は、～。")
question(CARTS, 30,
         ["shoppers had to pay an extra cost for using shopping carts inside supermarkets.", "supermarkets prohibited young children from sitting in shopping carts.", "shoppers could put more items in shopping carts because a new cart was designed.", "supermarkets could save space for shopping carts thanks to the new cart design."],
         ["買い物客は、スーパーマーケット内でショッピングカートを使うのに追加料金を払わなければならなかった。", "スーパーマーケットは、幼い子どもがショッピングカートに座ることを禁止した。", "新しいカートが設計されたので、買い物客はより多くの品物をカートに入れられるようになった。", "新しいカートの設計のおかげで、スーパーマーケットはショッピングカートを置く場所を節約できるようになった。"], 4,
         ["追加料金が必要。カートの利用料金についての記述はない。", "子どもが座るのを禁止。後に子ども用座席に安全ベルトが付いたとあり、禁止とは逆。", "より多くの品物を入れられる。新しい設計の目的は、多くのカートを狭い場所に収納すること。", "カートの置き場所を節約→正解。💡多くのカートをより狭い場所に収納できるよう設計された。"],
         "💡so that ～ can [could] … は「～が…できるように」と目的を表す。stored in a smaller area（より狭い場所に収納される）が、選択肢の save space（場所を節約する）に言い換えられている。", [18],
         "In the middle of the twentieth century,", "20世紀半ばには、～。")
question(CARTS, 31,
         ["Shopping carts were thought to be beneficial for both shoppers and supermarket owners.", "Shopping carts were invented so that people could buy large items like furniture.", "Goldman's initial shopping cart design had a child seat with a safety belt.", "Many women preferred to use their baby strollers as shopping carts."],
         ["ショッピングカートは、買い物客とスーパーマーケットの経営者の両方にとって有益だと考えられた。", "ショッピングカートは、人々が家具のような大きな品物を買えるように発明された。", "ゴールドマンの最初のショッピングカートの設計には、安全ベルト付きの子ども用座席があった。", "多くの女性が、ベビーカーをショッピングカートとして使うことを好んだ。"], 1,
         ["買い物客と経営者の両方に有益→正解。💡カートは楽に買い物ができる客と、売り上げを伸ばせる経営者の両方に役立ち得たとある。", "家具のような大きな品物のため。重くなるかごの問題を解決するためで、家具の記述はない。", "最初の設計に安全ベルト付きの座席。安全ベルトは後になって追加されたもの。", "ベビーカーをカート代わりに使った。カートがベビーカーに見えるとして嫌がった女性がいたという話。"],
         "💡both A and B は「AとBの両方」。shoppers, who ～ と supermarket owners, who ～ はコンマ付きの関係代名詞（非制限用法）で、それぞれにとっての利点を補足している。could be helpful が選択肢では were thought to be beneficial に言い換えられている。", [10],
         "Which of the following statements is true?", "次の記述のうち、正しいものはどれですか。")

PASSAGES = [MOUNTAIN, BATS, EMAIL, CARTS]
