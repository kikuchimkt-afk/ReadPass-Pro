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


CITY = passage("A", "The Dying City", [
    [
        ("イタリアにはチヴィタ・ディ・バニョレージョという小さな町があり、ときに「死にゆく町」として知られている。", "is", 'In Italy, there is a small city|イタリアには小さな町がある||called Civita di Bagnoregio,|チヴィタ・ディ・バニョレージョという||sometimes known as "the dying city."|ときに「死にゆく町」として知られる'),
        ("ローマの約120キロメートル北にある丘の上に位置している。", "stands", "It stands on a hill|それは丘の上に位置している||about 120 kilometers north of Rome.|ローマの約120キロメートル北にある"),
        ("何百年も前には、この村はもっと大きく、何千人もの人々が住んでいた。", "was", "Hundreds of years ago,|何百年も前には||the village was much larger|その村はもっと大きかった||and home to thousands of people.|そして何千人もの人々が住んでいた"),
        ("時がたつにつれて、自然災害によって村の広さと人口は徐々に減少した。", "reduced", "Over time,|時がたつにつれて||natural disasters slowly reduced|自然災害が徐々に減らした||the village's size and population.|村の広さと人口を"),
        ("今日、そこに住む人はわずかしかいない。", "live", "Today, only a few people|今日、わずかな人だけが||live there.|そこに住んでいる"),
        ("( 18 )、人々が村はまもなく消えてしまうかもしれないと聞くにつれ、観光客が来るようになった。", "started", "( 18 ), as people heard|（18）、人々が聞くにつれ||that the village might disappear very soon,|村がまもなく消えてしまうかもしれないと||visitors started coming.|観光客が来るようになった"),
        ("今や、その村は人気の観光地になっている。", "has become", "Now, the village has become|今や、その村はなっている||a popular tourist destination.|人気の観光地に"),
    ], [
        ("これらの観光客から恩恵を得るため、村は存続を助ける新しい計画を導入した。", "introduced", "To benefit from these tourists,|これらの観光客から恩恵を得るために||the village introduced a new plan|村は新しい計画を導入した||to help itself survive.|自らの存続を助けるための"),
        ("2013年、観光客から少額の入場料を取るようになった。", "started", "In 2013, they started charging visitors|2013年、観光客から取るようになった||a small entrance fee.|少額の入場料を"),
        ("何度か値上げした後、今では観光客は入場するために、日によって3ユーロか5ユーロを支払う。", "pay", "After a few increases,|何度か値上げした後||tourists now pay three or five euros to enter,|今では観光客は入場するため3ユーロか5ユーロを支払う||depending on the day.|日によって"),
        ("この料金は ( 19 )。", "", "This fee|この料金は||( 19 ).|（19）"),
        ("村の管理者は、村は引き続き大勢の観光客を引きつけ、課金制度は観光客に地域でより慎重に行動するよう促したと述べた。", "said", "A manager of the village said|村の管理者は述べた||it continued to attract large crowds|村は引き続き大勢の観光客を引きつけたと||and that the charging system encouraged tourists|そして課金制度は観光客に促したと||to behave more carefully in the area.|地域でより慎重に行動するように"),
        ("実際、観光の質は全体として向上している。", "has improved", "In fact, the quality of tourism|実際、観光の質は||has improved as a whole.|全体として向上している"),
    ], [
        ("観光は ( 20 ) をもたらした。", "has brought", "Tourism has brought|観光はもたらした||( 20 ).|（20）を"),
        ("第一に、集められた入場料は、地域の土地を保護し、自然災害に対処するために使われている。", "have been used", "First, the entrance fees collected|第一に、集められた入場料は||have been used to protect the land|土地を保護するために使われている||and deal with natural disasters in the area.|そして地域の自然災害に対処するために"),
        ("さらに、ホテルやレストラン、店などの新しい事業が多くの雇用を生み、村の失業率を下げている。", "have created", "In addition, new businesses,|さらに、新しい事業が||including hotels, restaurants, and shops,|ホテルやレストラン、店などの||have created many jobs,|多くの雇用を生み出した||lowering the village's unemployment rate.|村の失業率を下げながら"),
        ("観光は、よりよい医療や障害のある人々がより利用しやすい交通機関など、地域のサービスを向上させることにも役立っている。", "has also helped", "Tourism has also helped improve local services,|観光は地域のサービス向上にも役立っている||such as better medical care|よりよい医療などの||and easier transportation for people with disabilities.|そして障害のある人々がより利用しやすい交通機関"),
        ("このように、観光は村と住民を助け、かつて「死にゆく町」と呼ばれた町に新たな命を与えている。", "has helped", 'In this way, tourism has helped the village and its people,|このように、観光は村と住民を助けてきた||giving new life to the city|町に新たな命を与えながら||once called "the dying city."|かつて「死にゆく町」と呼ばれた'),
    ],
])

HONEY = passage("B", "Honey", [
    [
        ("はちみつは、紅茶に風味を加えることから料理に使うことまで、多くの方法で楽しまれる人気の食品だ。", "is", "Honey is a popular food|はちみつは人気の食品だ||enjoyed in many ways,|多くの方法で楽しまれる||from adding flavor to tea to using it in cooking.|紅茶に風味を加えることから料理に使うことまで"),
        ("それは ( 21 ) 食品だとよく考えられている。", "is often believed", "It is often believed|それはよく考えられている||to be a food that ( 21 ).|（21）食品だと"),
        ("実際、米国政府は、主に品質の目安として、はちみつは約2年間保存できるとしている。", "suggests", "In fact, the US government suggests|実際、米国政府は示している||that honey can be stored for about two years,|はちみつは約2年間保存できると||mainly as a guide to quality.|主に品質の目安として"),
        ("粘りが増したり固まったりしても、依然として安全に食べられる。", "is", "Even when it becomes thick or solid,|粘りが増したり固まったりしても||it is still safe to eat.|依然として安全に食べられる"),
        ("このため、はちみつは非常に長く持つ特別な性質で知られている。", "is known", "For this reason, honey is known|このため、はちみつは知られている||for its special ability to last a very long time.|非常に長く持つ特別な性質で"),
    ], [
        ("はちみつがそれほど長く新鮮さを保つ理由は、その独特な性質にある。", "lies", "The reason honey stays fresh for so long|はちみつがそれほど長く新鮮さを保つ理由は||lies in its unique nature.|その独特な性質にある"),
        ("食品が腐るとき、それは通常、細菌などの小さな生物がその上で増殖したことを意味する。", "means", "When food spoils,|食品が腐るとき||it usually means|それは通常意味する||that small living things, such as bacteria,|細菌などの小さな生物が||have grown on it.|その上で増殖したことを"),
        ("細菌は暖かく湿った環境を好む。", "prefer", "Bacteria prefer|細菌は好む||warm and wet environments.|暖かく湿った環境を"),
        ("しかし、はちみつはそのような条件を提供しない。", "does not provide", "Yet, honey does not provide|しかし、はちみつは提供しない||such conditions.|そのような条件を"),
        ("はちみつに含まれるいくつかの要因は ( 22 )。", "", "Several factors in honey|はちみつに含まれるいくつかの要因は||( 22 ).|（22）"),
        ("例えば、はちみつは水分が非常に少なく、糖分も多い。", "contains", "For example, honey contains very little water|例えば、はちみつは水分が非常に少ない||and also has high levels of sugar.|また糖分も多い"),
        ("さらに、はちみつには少量の酸が含まれており、それも細菌の増殖を難しくしている。", "has", "In addition, honey has a small amount of acid,|さらに、はちみつには少量の酸が含まれている||which also makes it hard|それも難しくしている||for bacteria to grow.|細菌が増殖することを"),
    ], [
        ("それでも、はちみつがあらゆる変化から完全に守られているわけではない。", "is", "Still, honey is not completely safe|それでも、はちみつは完全に守られているわけではない||from all changes.|あらゆる変化から"),
        ("はちみつの瓶を開けたままにしたり、使ったスプーンを中に入れたりすると、空気や水、細菌が入り込み、品質を下げることがある。", "can get", "If a bottle of honey is left open|はちみつの瓶を開けたままにしたり||or a used spoon is dipped into it,|使ったスプーンを中に入れたりすると||air, water, or bacteria can get inside|空気や水、細菌が入り込むことがある||and lower its quality.|そして品質を下げる"),
        ("いくつかの研究によれば、誤った方法で保存したり加熱しすぎたりすることも、品質や健康への利点を減らす変化を引き起こす可能性がある。", "may also cause", "According to some research,|いくつかの研究によれば||storing honey in the wrong way or heating it too much|誤った方法での保存や加熱のしすぎも||may also cause changes|変化を引き起こす可能性がある||that reduce its quality or health benefits.|品質や健康への利点を減らす"),
        ("( 23 )、はちみつは何年も持つとはいえ、注意して扱うのが最善だ。", "is", "( 23 ), even though honey can last for years,|（23）、はちみつは何年も持つとはいえ||it is best to handle it with care.|注意して扱うのが最善だ"),
    ],
])

EMAIL = passage("A", "About your appointment at our clinic", [
    [
        ("ロイ様", "", "Dear Roy,|ロイ様"),
        ("Dr. King Clinicのオリヴィア・キングです。", "is", "This is Olivia King|オリヴィア・キングです||from Dr. King Clinic.|Dr. King Clinicの"),
        ("予約変更についてのご連絡をありがとうございます。", "", "Thank you for your message|ご連絡をありがとうございます||regarding the change to your appointment.|予約の変更についての"),
        ("8月25日への変更をご希望と承知しております。", "understand", "I understand|私は承知しております||that you would like to move it to August 25.|8月25日への変更をご希望だと"),
        ("予定を確認しましたが、申し訳ありませんが、その日は予約をお受けできません。", "have checked", "I have checked my schedule,|予定を確認しました||but I am afraid|しかし申し訳ありませんが||that date is not available.|その日は予約をお受けできません"),
        ("8月23日から27日まで夏の会議に出席するため不在となり、その間は診療所を休診します。", "will be", "I will be away for a summer conference|夏の会議に出席するため不在となります||from August 23 to 27,|8月23日から27日まで||so the clinic will be closed during that period.|そのため、その間は診療所を休診します"),
    ], [
        ("代わりに、8月18日午後2時をご提案いたします。", "would like", "Instead, I would like to suggest|代わりに、ご提案いたします||August 18 at 2 p.m.|8月18日午後2時を"),
        ("この時間のご都合が悪い場合は、帰ってから間もなくの別の予約をご案内できます。", "can offer", "If this time is not convenient for you,|この時間のご都合が悪い場合は||I can offer another appointment|別の予約をご案内できます||soon after my return.|帰ってから間もなくの"),
        ("最も早く予約をお受けできる日は、9月1日の午後1時30分です。", "is", "The earliest available date is|最も早く予約をお受けできる日は||September 1 at 1:30 p.m.|9月1日の午後1時30分です"),
        ("今回の来院では、通常の健康診断を行います。", "will proceed", "At this visit, we will proceed|今回の来院では、行います||with your regular checkup.|通常の健康診断を"),
        ("健康診断の所要時間は30分以内を見込んでいます。", "is expected", "The checkup is expected|健康診断は見込まれています||to take no more than thirty minutes.|30分以内で済むと"),
    ], [
        ("どちらの予約時間も、8月14日まではあなたのために確保しておきます。", "will hold", "I will hold both appointment times for you|どちらの予約時間もあなたのために確保しておきます||until August 14.|8月14日まで"),
        ("それまでにお返事がなければ、それらの時間は他の患者様にご案内します。", "will be offered", "If I do not hear back from you by then,|それまでにお返事がなければ||those times will be offered|それらの時間はご案内されます||to other patients.|他の患者様に"),
        ("予約日が近づいていますので、ご希望の時間を確認するため、お電話でのご連絡をお勧めします。", "recommend", "As your appointment date is approaching,|予約日が近づいていますので||we recommend contacting us by phone|お電話でのご連絡をお勧めします||to confirm your preferred time.|ご希望の時間を確認するために"),
        ("メールによる予約変更には迅速に対応できない可能性があるので、お電話で予約を変更していただけます。", "can change", "Because we may not be able to process appointment changes by email quickly enough,|メールによる予約変更には十分迅速に対応できない可能性があるので||you can change your appointment|予約を変更していただけます||by giving us a call.|お電話をいただくことで"),
    ], [
        ("よろしくお願いいたします。", "", "Thank you,|よろしくお願いいたします"),
        ("オリヴィア・キング", "", "Olivia King|オリヴィア・キング"),
    ],
], format="email")
# Preserve the original mail headers and line breaks, not HTML markup.
EMAIL["meta"] = {"from":"Olivia King <contact@drking-clinic.com>",
                 "to":"Roy Turner <roy.turner.0327@e.letters-world.com>",
                 "date":"August 12", "subject":"About your appointment at our clinic"}
EMAIL["paragraphs"][0] = EMAIL["paragraphs"][0].replace("Dear Roy, ", "Dear Roy,\n", 1)
EMAIL["translations"][0] = EMAIL["translations"][0].replace("ロイ様", "ロイ様\n", 1)
EMAIL["paragraphs"][-1] = "Thank you,\nOlivia King"
EMAIL["translations"][-1] = "よろしくお願いいたします。\nオリヴィア・キング"

DOGS = passage("B", "Dogs and Heat", [
    [
        ("人間は汗をかくことで体温を調節する。", "control", "Humans control their body temperature|人間は体温を調節する||by sweating.|汗をかくことで"),
        ("汗腺と呼ばれる皮膚の小さな部分が汗を作り出し、それが体を冷やすのを助ける。", "produce", "Tiny parts of the skin called sweat glands|汗腺と呼ばれる皮膚の小さな部分が||produce sweat,|汗を作り出す||which helps cool the body.|それが体を冷やすのを助ける"),
        ("犬にも汗腺がある。", "have", "Dogs also have|犬にもある||sweat glands.|汗腺が"),
        ("しかし、それらは人間の汗腺ほどよく働かない。", "do not work", "However, they do not work as well|しかし、それらは同じほどよく働かない||as human sweat glands.|人間の汗腺と"),
        ("これは、犬は涼しく過ごすために発汗に頼れないということを意味する。", "means", "This means|これは意味する||dogs cannot depend on sweating|犬は発汗に頼れないと||to stay cool.|涼しく過ごすために"),
        ("人間には快適に感じられる日でも、犬は暑さで苦しむことがある。", "may suffer", "Even on days that feel comfortable to humans,|人間には快適に感じられる日でも||dogs may suffer from heat.|犬は暑さで苦しむことがある"),
        ("そのため専門家は、暑い天候の中で犬を外に置いておくことは非常に危険で、十分な注意が必要だと警告する。", "warn", "Therefore, experts warn|そのため、専門家は警告する||that leaving dogs outside in hot weather|暑い天候の中で犬を外に置いておくことは||is very dangerous and requires careful attention.|非常に危険で、十分な注意が必要だと"),
    ], [
        ("犬の皮膚には確かに汗腺があるものの、全ての種類の汗腺が体温を下げるのに役立つわけではない。", "help", "While dogs do have sweat glands on their skin,|犬の皮膚には確かに汗腺があるものの||not all types of sweat glands|全ての種類の汗腺が||help lower body temperature.|体温を下げるのに役立つわけではない"),
        ("エクリン腺と呼ばれる特定の種類がその役割を担うが、それらは犬の足の裏と鼻にしかない。", "is", "A particular kind, called eccrine glands,|エクリン腺と呼ばれる特定の種類が||is responsible for the role,|その役割を担う||but they can only be found|しかし、それらはしかない||on the bottoms of dogs' feet and on their noses.|犬の足の裏と鼻に"),
        ("エクリン腺はそのような狭い部位に少ししかないため、体を冷やすのにあまり効果的ではない。", "are", "Because there are so few eccrine glands in such small areas,|エクリン腺はそのような狭い部位に少ししかないため||they are not very effective|それらはあまり効果的ではない||in cooling the body.|体を冷やすのに"),
        ("このため、発汗は犬が体温を調節する主な方法ではない。", "is", "This is why|このため||sweating is not the main way|発汗は主な方法ではない||that dogs keep their body temperature under control.|犬が体温を調節する"),
    ], [
        ("その代わり、犬は主にパンティングで自分の体を冷やす。", "cool", "Instead, dogs mainly cool themselves|その代わり、犬は主に自分の体を冷やす||by panting.|パンティングで"),
        ("短い呼吸を素早く繰り返すこの行動によって、犬は口と鼻を通して熱を逃がせる。", "allows", "This behavior of breathing quickly with short breaths|短い呼吸を素早く繰り返すこの行動は||allows dogs to release heat|犬が熱を逃がすことを可能にする||through the mouth and nose.|口と鼻を通して"),
        ("しかし、全ての犬がこの方法で体を冷やすのが得意なわけではない。", "are", "However, not all dogs are good|しかし、全ての犬が得意なわけではない||at cooling themselves in this way.|この方法で自分の体を冷やすのが"),
        ("その違いは鼻の形に関係している。", "is related", "The difference is related|その違いは関係している||to the shape of their noses.|鼻の形に"),
        ("鼻がより短い犬は、体を冷やすのがより難しい。", "have", "Dogs with shorter noses|鼻がより短い犬は||have more difficulty cooling down.|体を冷やすのがより難しい"),
        ("研究によれば、そうした犬は鼻がより長い犬の約4倍、暑さによる問題を起こしやすい。", "show", "Studies show|研究は示している||they are about four times more likely to get heat problems|そうした犬は約4倍、暑さによる問題を起こしやすいと||than dogs with longer noses.|鼻がより長い犬より"),
        ("これは、鼻が短いと、体から熱を逃がすのがより難しくなるためだ。", "is", "This is because|これはためだ||short noses make it harder|鼻が短いとより難しくなる||to let heat escape from the body.|体から熱を逃がすのが"),
    ], [
        ("飼い主の中には、寒い冬の間は犬の散歩を減らす人もいる。", "walk", "Some owners walk their dogs less|飼い主の中には犬の散歩を減らす人もいる||during the cold winter.|寒い冬の間は"),
        ("暖かくなると、犬をより長い時間、より頻繁に散歩させるようになる。", "start", "When it warms up,|暖かくなると||they start walking dogs|犬を散歩させるようになる||longer and more often.|より長い時間、より頻繁に"),
        ("専門家は、この急な運動量の増加は犬に負担となり得るので、避けるべきだと考えている。", "believe", "Experts believe|専門家は考えている||that this sudden increase in exercise|この急な運動量の増加は||can be hard for dogs and should be avoided.|犬に負担となり得るので、避けるべきだと"),
        ("暑さによる問題の危険を減らすため、飼い主は犬に十分な水を与え、毛が熱をため込みすぎないように定期的にブラッシングするべきだとも述べている。", "say", "To reduce the risk of heat problems,|暑さによる問題の危険を減らすために||they also say|専門家はまた述べている||that owners should give their dogs plenty of water|飼い主は犬に十分な水を与えるべきだと||and brush them regularly|そして定期的にブラッシングするべきだと||to prevent fur from trapping too much heat.|毛が熱をため込みすぎないように"),
        ("犬にこのような環境を与えることは、安全と健康を保つのに役立つ。", "helps", "Providing dogs with such an environment|犬にこのような環境を与えることは||helps keep them safe and healthy.|安全と健康を保つのに役立つ"),
    ],
])


def question(number, choices, translations, answer, analysis, evidence, grammar,
             stem=None, stem_ja=None):
    q = dict(number=number, choices=choices, choiceTranslations=translations,
             answer=answer, choiceAnalysis=analysis, sourceEvidence=evidence, grammar=grammar)
    if stem is not None:
        q.update(question=stem, questionTranslation=stem_ja)
    return q


CITY["questions"] = [
    question(18, ["In the same way", "At least", "Especially", "However"],
             ["同じように", "少なくとも", "特に", "しかし"], 4,
             ["In the same way＝同じように。人口減少と観光客の増加は同じ流れではない。", "At least＝少なくとも。最低限の数や救いとなる事実を述べる接続ではない。", "Especially＝特に。前の例を強調する文ではなく、流れが転換する。", "However＝しかし→正解。💡住民は少ない一方、消えると聞いた観光客は増えた。"],
             ["Today, only a few people live there.", "visitors started coming."],
             "💡村の衰退から観光客の増加へ転じる逆接。as people heard ... は、知らせが広まるにつれて起きた変化を示す。"),
    question(19, ["did not stop tourists from coming", "did not bring the village good reviews", "created frustration among tourists", "encouraged tourists to choose other destinations"],
             ["観光客が来るのを妨げなかった", "村に良い評判をもたらさなかった", "観光客の間に不満を生んだ", "観光客に他の目的地を選ぶよう促した"], 1,
             ["来訪を妨げなかった→正解。💡continued to attract large crowds と一致する。", "良い評判をもたらさなかった。評判の悪化は述べられず、観光の質は向上した。", "不満を生んだ。より慎重に行動するようになったのであり、不満の記述はない。", "他の目的地を選ばせた。引き続き大勢を引きつけたことと矛盾する。"],
             ["it continued to attract large crowds", "the quality of tourism has improved as a whole."],
             "💡stop A from V-ing は「Aが～するのを妨げる」。否定すると、入場料を取っても来訪が続いたという意味になる。"),
    question(20, ["issues for the businesses in the area", "positive results for tourists over locals", "hard times for people with little money", "several advantages to the village"],
             ["地域の事業にとっての問題", "地元住民よりも観光客にとっての良い結果", "お金の少ない人々にとっての苦しい時期", "村へのいくつかの利点"], 4,
             ["地域の事業の問題。新しい事業は雇用を生んでおり、問題として描かれない。", "観光客を住民より優先した利益。土地保護や失業率低下など、村への利益が列挙される。", "お金の少ない人の苦境。そのような苦境は本文にない。", "村への利点→正解。💡土地保護・雇用増・地域サービス向上が具体例。"],
             ["have been used to protect the land and deal with natural disasters in the area.", "have created many jobs, lowering the village's unemployment rate.", "Tourism has also helped improve local services"],
             "💡has brought＋目的語。「観光がもたらしたもの」を、First / In addition / also の列挙からまとめる。"),
]
HONEY["questions"] = [
    question(21, ["does not go bad easily", "hardly needs care before eating it", "rarely needs to be replaced", "does not keep its original form"],
             ["簡単には腐らない", "食べる前にほとんど注意が要らない", "めったに取り替える必要がない", "元の形を保たない"], 1,
             ["簡単には腐らない→正解。💡長く保存でき、固まっても安全に食べられる。", "注意がほぼ要らない。第3段落では扱い方によって品質が下がると述べる。", "取り替える必要がない。交換の頻度ではなく、食品が長持ちする性質を説明する。", "元の形を保たない。固まる話はあるが、この段落の主旨は長く安全に食べられること。"],
             ["honey can be stored for about two years", "it is still safe to eat.", "its special ability to last a very long time."],
             "💡go bad は「腐る」。a food that ... の that は food を修飾する関係代名詞。後続の具体例で性質を判断する。"),
    question(22, ["help increase its temperature", "help stop bacteria from surviving", "allow more bacteria to grow", "allow it to get even sweeter"],
             ["温度を上げるのを助ける", "細菌の生存を妨げるのを助ける", "より多くの細菌の増殖を可能にする", "さらに甘くなるのを可能にする"], 2,
             ["温度を上げる。水分・糖・酸の説明は温度上昇の話ではない。", "細菌の生存を妨げる→正解。💡水分の少なさや糖・酸が、細菌の増殖を難しくする。", "細菌の増殖を可能にする。makes it hard for bacteria to grow と逆。", "さらに甘くする。糖分が多いのは事実だが、甘さが増す変化は述べていない。"],
             ["honey does not provide such conditions.", "honey contains very little water and also has high levels of sugar.", "which also makes it hard for bacteria to grow."],
             "💡help＋動詞の原形。stop A from V-ing は「Aが～するのを妨げる」。細菌が好む条件と、はちみつの条件の対比を読む。"),
    question(23, ["For example", "Instead", "However", "Therefore"],
             ["例えば", "その代わりに", "しかし", "したがって"], 4,
             ["For example＝例えば。保存方法の具体例を加えるのでなく、扱い方の結論を述べる。", "Instead＝その代わりに。別の行動へ置き換える文ではない。", "However＝しかし。直前の品質低下の危険から、注意すべきだと結論づける関係。", "Therefore＝したがって→正解。💡品質が下がり得るので、長持ちしても注意して扱うべき。"],
             ["storing honey in the wrong way or heating it too much may also cause changes that reduce its quality or health benefits.", "it is best to handle it with care."],
             "💡Therefore は理由から結論へつなぐ。even though ... は「～とはいえ」という譲歩で、長持ちと注意の必要を両立させる。"),
]
EMAIL["questions"] = [
    question(24, ["he could move his appointment to the date he had requested.", "no appointments could be made from August 23 to 27.", "she would not be available on his original appointment date.", "she would be attending a conference starting on August 25."],
             ["希望した日に予約を変更できると", "8月23日から27日までは予約ができないと", "元の予約日には彼女が対応できないと", "8月25日に始まる会議に出席すると"], 2,
             ["希望日に変更できる。8月25日は not available と明記されている。", "23～27日は予約不可→正解。💡会議で不在となり、診療所が休診する期間。", "元の予約日に対応できない。元の予約日は本文に示されていない。", "25日開始の会議。会議のため不在となるのは23日から27日。"],
             ["I will be away for a summer conference from August 23 to 27, so the clinic will be closed during that period."],
             "💡told＋人＋that節は伝えた内容。requested date（変更希望日）と original appointment date（元の予約日）を混同しない。",
             "Olivia King told Roy Turner that", "オリヴィア・キングはロイ・ターナーに何と伝えましたか。"),
    question(25, ["August 18 is one of the dates offered for an appointment.", "September 1 is the earliest possible date suggested.", "The appointment will probably take over half an hour.", "The regular checkup will be skipped this time."],
             ["8月18日は予約日として提案された日の一つだ", "9月1日が提案された最も早い日だ", "予約での診察はおそらく30分を超える", "今回は通常の健康診断を省略する"], 1,
             ["8月18日も候補→正解。💡August 18 at 2 p.m. が最初に提案されている。", "9月1日が最も早い。これは帰任後の候補で、8月18日も提案されている。", "30分を超える。no more than thirty minutes は「30分以内」。", "健康診断を省く。proceed with your regular checkup と明記されている。"],
             ["Instead, I would like to suggest August 18 at 2 p.m."],
             "💡earliest available date は直前の after my return の範囲で読む。no more than＋数は「多くても～・～以内」。",
             "What is true about Roy's appointment?", "ロイの予約について正しいことは何ですか。"),
    question(26, ["Visit the clinic on August 14 for his new appointment.", "Contact her after August 14 to tell her the date he prefers.", "Send back an email before August 14 with his choice of visit.", "Call the clinic by August 14 to arrange his appointment."],
             ["新しい予約のため8月14日に診療所へ行く", "希望日を伝えるため8月14日より後に彼女に連絡する", "来院日の希望を書いて8月14日より前にメールを返信する", "予約を調整するため8月14日までに診療所へ電話する"], 4,
             ["14日に来院する。14日は候補を確保する期限であり、診察日ではない。", "14日より後に連絡する。期限後は他の患者に候補の時間を提供する。", "メールで返信する。メールでは迅速に処理できない可能性があり、電話を勧めている。", "14日までに電話→正解。💡候補の確保期限と contacting us by phone を合わせる。"],
             ["I will hold both appointment times for you until August 14.", "we recommend contacting us by phone to confirm your preferred time."],
             "💡until は確保の継続期限、by は連絡を済ませる期限。recommend V-ing で contacting。日付と連絡方法の両方を確認する。",
             "What does Olivia suggest to Roy?", "オリヴィアはロイに何を勧めていますか。"),
]
DOGS["questions"] = [
    question(27, ["They may have a poor system for sensing heat.", "They can cool down too quickly by sweating.", "They are sensitive to the heat as they are not good at sweating.", "They generally feel cold whenever they go outside."],
             ["暑さを感じる仕組みが不十分かもしれない", "汗をかくことで急速に冷えすぎることがある", "汗をかくのが得意でないため暑さに弱い", "外へ出るといつでもたいてい寒く感じる"], 3,
             ["暑さを感じる仕組みが弱い。問題は感知ではなく、発汗による冷却が不十分なこと。", "汗で冷えすぎる。発汗には頼れないとあり、逆の内容。", "発汗が苦手で暑さに弱い→正解。💡汗腺の働きが弱く、人に快適な日でも苦しむ。", "外ではいつでも寒い。本文は暑さに苦しむ危険を説明している。"],
             ["they do not work as well as human sweat glands.", "dogs cannot depend on sweating to stay cool.", "dogs may suffer from heat."],
             "💡as they are ... の as は理由。「発汗に頼れない」ため「暑さに弱い」という因果をまとめる。",
             "What seems to be a problem for dogs?", "犬にとって問題と思われることは何ですか。"),
    question(28, ["They are found throughout their lower body.", "They have little effect on controlling body temperature.", "They are the only type of sweat gland dogs have.", "They are located in large numbers on their bodies."],
             ["体の下半身全体にある", "体温調節にはほとんど効果がない", "犬にある唯一の種類の汗腺だ", "体に大量に存在する"], 2,
             ["下半身全体にある。犬の足の裏と鼻にしかない。", "体温調節の効果が小さい→正解。💡狭い部位に少ししかなく、冷却にあまり効果的でない。", "唯一の汗腺。not all types とあり、汗腺には他の種類もある。", "大量にある。so few eccrine glands と逆。"],
             ["there are so few eccrine glands in such small areas", "they are not very effective in cooling the body."],
             "💡not very effective を have little effect と言い換えている。little は不可算名詞 effect の量が少ないことを示す。",
             "What is true about the eccrine glands of dogs?", "犬のエクリン腺について正しいことは何ですか。"),
    question(29, ["It refers to taking a deep breath to let the air flow through the body.", "It helps all dogs equally to control their body temperature.", "It describes the behavior of dogs running fast over a short distance.", "It means dogs are trying to release heat quickly from their body."],
             ["体に空気を通すため深呼吸することを指す", "全ての犬に等しく体温調節を助ける", "犬が短い距離を速く走る行動を表す", "犬が体から素早く熱を逃がそうとしていることを意味する"], 4,
             ["深呼吸する。本文は短い呼吸を素早く繰り返す行動と説明する。", "全ての犬に同じ効果。鼻の形により冷却の得意さが異なる。", "短距離を速く走る。パンティングは走り方でなく呼吸の行動。", "熱を素早く逃がす→正解。💡短い呼吸を繰り返し、口と鼻を通して放熱する。"],
             ["This behavior of breathing quickly with short breaths allows dogs to release heat through the mouth and nose."],
             "💡allow A to V は「Aが～することを可能にする」。panting の定義は呼吸の方法と放熱の働きから読む。",
             "How can dogs' panting be described?", "犬のパンティングはどのように説明できますか。"),
    question(30, ["not give their dogs too much water at any time.", "not fail to brush their dogs regularly.", "stop going for walks with their dogs in summer.", "prepare their dogs for a sudden rise in temperature."],
             ["いつでも犬に水を与えすぎない", "定期的なブラッシングを怠らない", "夏には犬との散歩をやめる", "気温の急上昇に犬を備えさせる"], 2,
             ["水を与えすぎない。本文は plenty of water を与えるよう勧める。", "ブラッシングを怠らない→正解。💡毛が熱をため込まないよう、定期的に手入れする。", "夏の散歩をやめる。急な運動量増加を避けるのであり、散歩を全面禁止していない。", "気温の急上昇に備える。sudden increase は運動量の増加で、気温ではない。"],
             ["brush them regularly to prevent fur from trapping too much heat."],
             "💡not fail to V は「忘れずに～する・～を怠らない」。本文の should brush regularly を否定表現で言い換えている。",
             "To keep dogs safe and healthy, experts suggest that owners should", "犬の安全と健康を保つため、専門家は飼い主がどうするべきだと勧めていますか。"),
    question(31, ["The length of a dog's nose is related to the control of body temperature.", "Sweating is the most important method for dogs to control their body temperature.", "It is generally believed that humans cannot handle heat as well as dogs.", "Dog owners are advised to wet their dogs' noses to cool them down during summer."],
             ["犬の鼻の長さは体温調節に関係する", "犬の体温調節で最も重要な方法は発汗だ", "人間は犬ほど暑さに対処できないと一般に考えられている", "夏に犬を冷やすため鼻をぬらすよう飼い主に助言されている"], 1,
             ["鼻の長さと体温調節が関連→正解。💡短い鼻の犬は冷却が難しく、暑さによる問題が起きやすい。", "発汗が最重要。発汗は main way ではなく、主にパンティングで冷やす。", "人間の方が暑さに弱い。犬の汗腺は人間ほど働かず、人に快適な日でも苦しむ。", "鼻をぬらすべき。水を与えることやブラッシングはあるが、鼻をぬらす指示はない。"],
             ["The difference is related to the shape of their noses.", "Dogs with shorter noses have more difficulty cooling down."],
             "💡be related to は「～に関係する」。shape の説明を shorter / longer noses と合わせて、鼻の長さによる違いとしてまとめる。",
             "What do we learn from the passage?", "本文からどのようなことが分かりますか。"),
]

PASSAGES = [CITY, HONEY, EMAIL, DOGS]
