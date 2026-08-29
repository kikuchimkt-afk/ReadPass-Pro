# -*- coding: utf-8 -*-
"""2026-1-sat 2級: 対訳・根拠・文法・メール全文・リスニング正答を補完する。"""
from __future__ import annotations

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "grade2", "2026-1-sat", "data.json",
)
DATA_PATH = os.environ.get("READPASS_G2_SAT_DATA_PATH", DEFAULT_DATA_PATH)

OFFICIAL_READING = {
    1: 3, 2: 2, 3: 3, 4: 3, 5: 1, 6: 3, 7: 3, 8: 1, 9: 4, 10: 3,
    11: 3, 12: 3, 13: 4, 14: 2, 15: 3, 16: 1, 17: 1,
    18: 4, 19: 2, 20: 3, 21: 1, 22: 4, 23: 3,
    24: 4, 25: 1, 26: 3, 27: 1, 28: 3, 29: 4, 30: 2, 31: 1,
}

CHOICE_TRANSLATIONS = {
    1: ["口論", "印象", "出来事・事件", "結果"],
    2: ["目的地", "量", "犠牲", "業績"],
    3: ["こぼす", "～に似ている", "かき混ぜる", "楽しませる"],
    4: ["脅かされた", "増やされた", "好まれた", "救助された"],
    5: ["ケーブル・電線", "跳躍", "雑誌・日誌", "調査"],
    6: ["好み", "勝利", "感謝", "失望"],
    7: ["発見した", "感染させた", "叱った", "つかんだ"],
    8: ["見積もる", "断る・減少する", "刺激する", "怠る"],
    9: ["合法的に", "乱暴に・おおよそ", "かろうじて", "辛抱強く"],
    10: ["否定的な", "不在の", "現在の", "突然の"],
    11: ["途中で", "結局", "今まで", "～のために"],
    12: ["それどころか", "念のため", "言うまでもなく", "言い換えれば"],
    13: ["進む", "息を止める", "彼の代わりをする", "かんしゃくを起こす"],
    14: ["彼女の手に入る", "幸運を祈っている", "彼女の息をのませる", "決心している"],
    15: ["～をすまなく思う", "～に似ている", "～に自信がある", "～にうんざりしている"],
    16: ["～から離れない・～を守る", "手渡す", "成し遂げる・脱ぐ", "横になる"],
    17: ["～への影響", "～との比較", "～への責任", "～への反応"],
    18: ["同様に", "さもなければ", "例えば", "その代わりに"],
    19: ["新しい歩道を使って報酬を得る", "変化を体験して意見を伝える", "変化に気づかずに地域を歩く", "試行前に変化について話す"],
    20: ["教育上の問題を引き起こす", "都市を環境に優しくする", "子どもたちのために楽しい場所をつくる", "他都市の運転者のために機能する"],
    21: ["木の中に入って卵を産む", "枯れ木に近づかない", "キノコを食べて遠くへ飛ぶ", "木が再び成長するのを助ける"],
    22: ["これにもかかわらず", "対照的に", "平均して", "さらに"],
    23: ["柔らかい地面の広い場所で", "高山近くの空気が薄い場所で", "乾燥した気候や乾季に", "森林地帯の涼しい朝に"],
    24: ["工場の歴史をさらに学ぶため。", "学校の課題用に無料のペットボトルを依頼するため。", "工場での生徒向け職業体験について尋ねるため。", "生徒がその工場へ行きたがる理由を説明するため。"],
    25: ["ほかの曜日は授業がもっと遅く終わるから。", "彼女が授業後に生徒を工場へ連れて行けるから。", "その日は生徒にとって交通の便がよりよいから。", "工場が毎週金曜日に限定ツアーを行うから。"],
    26: ["訪問時に必要な特別な服装を事前に詳しく知らせる。", "訪問前に書面を提出すべきか知らせる。", "金曜のツアーが可能な日時と持参物を知らせる。", "ツアーに学校のカメラを持参するよう勧める。"],
    27: ["温暖な気候でくつろぎ、パーティーに参加し、英気を養うため。", "湾の近くで定期開催された自然に関する会合へ出席するため。", "バイアを訪れた専門家や学者と意見を交わすため。", "著名な詩人から詩を学び、詩の大会に参加するため。"],
    28: ["周辺に新しい火山ができるのを可能にした。", "その地域で農業を成功させることを不可能にした。", "町の一部を徐々に水中へ沈ませた。", "新しい観光客を呼ぶ温泉をさらに生み出した。"],
    29: ["湾の近くで大きな彫刻に気づいた歴史研究者たちによって。", "保護海域の絵を描いていた子どもたちによって。", "古代船を探していたスキューバダイバーの探索によって。", "湾の上空を飛行していたパイロットが撮った写真によって。"],
    30: ["ガイドなしで自由に潜り、遺跡を探すこと。", "ツアーボートの特殊なガラス越しに海上から見ること。", "ローマに新設された歴史博物館をガイド付きで訪れること。", "町の遺跡と構造物博物館の両方を見せるツアーに参加すること。"],
    31: ["バイアが沈んだ区域は、発見後に保護されるようになった。", "バイアは混雑しすぎて、ハドリアヌス帝は滞在できなかった。", "湖や川の冷たい水が、夏にローマ人をバイアへ引きつけた。", "バイアの多くの部分は、1940年代以降ゆっくり沈み続けている。"],
}

GRAMMAR = {
    1: "💡 no + 複数名詞で「一つも～ない」。problems と a very smooth journey が incidents（出来事・問題）がなかったことを示す。",
    2: "💡 a small quantity＝少量。How many と enough for an apple pie が、必要なリンゴの量を尋ねる文脈を作る。",
    3: "💡 tell A to V＝AにVするよう言う。so that ... would not stick は「鍋底につかないように」で、stir が目的に合う。",
    4: "💡 be favored by A＝Aに好まれる。professional players と serious amateurs の両方が使うことが high-quality の根拠。",
    5: "💡 関係代名詞 that provided electricity が先行詞を説明する。repair them の them も複数の cables を指す。",
    6: "💡 show one's appreciation for ～＝～への感謝を示す。present を贈った目的を表す定型表現。",
    7: "💡 scold A for doing＝Aを～したことで叱る。broken window と in a loud voice が叱責の場面を示す。",
    8: "💡 estimate that S + V＝～だと見積もる。about three hours という所要時間の推定に使われる。",
    9: "💡 However が動揺した乗客と Michael を対比する。not in a hurry なので patiently（辛抱強く）が合う。",
    10: "💡 current price＝現在の価格。this year と last year の比較が「現在の」を選ぶ手がかり。",
    11: "💡 Up until now は現在完了 has been と結びつき「今までずっと」。but next week が今後の変化を示す。",
    12: "💡 Needless to say＝言うまでもなく。全員が主役を望んでも全員はなれない、という当然の結果を導く。",
    13: "💡 lose one's temper＝かっとなる。be more patient / stay calm と反対の状態なので正答を特定できる。",
    14: "💡 keep one's fingers crossed that ...＝～となるよう幸運を祈る。出願後に合格を願う場面。",
    15: "💡 be confident of ～＝～に自信がある。never doubts himself が confident の直接的な言い換え。",
    16: "💡 keep to the path＝道から外れない・道を守る。Going off the paths can be dangerous と対比される。",
    17: "💡 have an effect on ～＝～に影響を与える。スキルと自信を得た返答が大学進学の影響を具体化する。",
    18: "💡 Instead は前文の cars are banned と、代わりに children can walk を対比する接続副詞。",
    19: "💡 have the opportunity to V＝Vする機会を持つ。opinions and observations が experience the changes and give feedback の根拠。",
    20: "💡 not only A but also B で make the streets safe と create a fun place を並列する。them は children を指す。",
    21: "💡 allow A to V＝AがVするのを可能にする。lay eggs の結果、new insects begin to grow する流れ。",
    22: "💡 Additionally は追加を表す。生きている間の炭素吸収に加え、枯れた後も炭素を蓄える働きを述べる。",
    23: "💡 in these conditions の conditions は dry climates / dry seasons を指す。lack moisture と catch fire easily が決め手。",
    24: "💡 連絡の目的は第1段落で示される。生徒の関心と工場を訪れて学びたい理由を説明している。",
    25: "💡 earlier than on other days の比較を、classes finish later on other days と反対側から言い換えている。",
    26: "💡 let me know if ... と tell us what ... は丁寧な間接疑問。希望日時と持参・準備物への回答を求める。",
    27: "💡 enjoyed parties, hot springs, and the warm climate と restore their energy を relax / recharge に言い換える。",
    28: "💡 cause A to V＝AにVさせる。sink underground gradually が slowly sink beneath the water に言い換えられる。",
    29: "💡 while flying low と the picture he took が、低空飛行中のパイロットによる写真で発見されたことを示す。",
    30: "💡 through the glass bottom of boats を through special glass on a tour boat と言い換えている。with guides と without a guide の対比にも注意。",
    31: "💡 1940年代に注目・発見され、2000年代初頭以降は protected marine area として管理された時系列を確認する。",
}

QUESTION_TRANSLATIONS = {
    24: "ジェシカ・ジェンキンスがジェームズ・ホワイトに連絡しているのはなぜですか。",
    25: "ジェシカが、生徒が金曜日に工場見学できるか尋ねるのはなぜですか。",
    26: "ジェシカはジェームズに何をしてほしいのですか。",
    27: "なぜ多くの裕福なローマ人はバイアを訪れたのですか。",
    28: "バイアにおける地面のゆるやかな動きは、",
    29: "水中に消えていたバイアの町の一部は、どのように発見されましたか。",
    30: "観光客が古代都市バイアを見る方法の一つは、",
    31: "次のうち正しいものはどれですか。",
}

SOURCE_EVIDENCE = {
    18: [
        "Now, cars are banned from this street when children go to school.",
        "( 18 ), during the school arrival time from 7:30 to 8:00 a.m., children can walk to school on their own.",
    ],
    19: [
        "Residents, parents, and school officials can have the opportunity to ( 19 ).",
        "Based on all the opinions and observations, designers can develop more permanent solutions using better materials.",
    ],
    20: [
        "These urban improvements not only make the streets safe for children but also ( 20 ).",
        "These art elements are changing spaces that used to be mainly for cars into community areas where children can actively play together.",
    ],
    21: [
        "This allows insects to ( 21 ).",
        "In turn, new insects and other creatures begin to grow.",
    ],
    22: [
        "While still alive, trees absorb carbon and help lower the amount of CO₂ in the air.",
        "( 22 ), they serve as natural carbon storage after they die.",
    ],
    23: [
        "This is especially important ( 23 ).",
        "In these conditions, dead trees lack moisture and can catch fire easily, causing serious damage.",
    ],
    24: [
        "Our students have been learning about manufacturing in social studies class, and one of my students has shown a strong interest in how everyday products, such as plastic bottles, are made.",
        "After doing some research on his own, he would like to visit your factory to learn more.",
    ],
    25: [
        "His last class of the day ends at 2:00 p.m. on Fridays, which is earlier than on other days.",
    ],
    26: [
        "Please let me know if there is an available date and time for a tour on a Friday in the next two months.",
        "Could you also tell us what he should bring or prepare in advance?",
    ],
    27: [
        "As it was conveniently located just about thirty kilometers from Naples on the west coast of Italy, wealthy people in Rome visited the city and enjoyed parties, hot springs, and the warm climate.",
        "Famous poets, speakers, and experts on nature also had their houses near the bay or public baths to restore their energy.",
    ],
    28: [
        "As is common in areas with volcanoes, the surface of the land rose and sank over many centuries.",
        "This caused more and more parts of the land to sink underground gradually.",
    ],
    29: [
        "An Italian military pilot discovered mysterious structures under the water in the bay while flying low.",
        "Walls and roads in the water were seen clearly in the picture he took.",
    ],
    30: [
        "Divers can explore the ancient Roman city in the water with guides.",
        "When the ocean is calm, visitors can see the structures in the water through the glass bottom of boats.",
    ],
    31: [
        "It was not until the 1940s that this underwater part of the city began attracting attention.",
        "Later investigations revealed a room filled with large sculptures, and since the early 2000s, the part of the city that sank into the sea has been managed as a protected marine area.",
    ],
}

LISTENING = {
    "part1": {str(i): answer for i, answer in enumerate(
        [4, 4, 1, 1, 4, 4, 4, 3, 3, 2, 4, 1, 1, 1, 4], start=1)},
    "part2": {str(i): answer for i, answer in enumerate(
        [1, 2, 2, 3, 4, 2, 2, 3, 4, 4, 3, 2, 4, 2, 1], start=16)},
}

# 2025年度2級と同じ sentencePairs の4要素形式。
# 各要素は (自然なスラッシュ読み, 主動詞・主要句) で、段落内の文順に並べる。
SENTENCE_ENRICHMENT = {
    "Child-Friendly City": [
        (
            "In Bratislava, a central city in Slovakia,|スロバキアの中心都市ブラチスラバでは、||efforts have been made|取り組みが行われてきた||to create a child-friendly city|子どもに優しい都市をつくるための||through the “City for Children” program.|「City for Children」プログラムを通じて。",
            "have been made",
        ),
        (
            "Many schools were surrounded by dangers,|多くの学校が危険に囲まれ、||and safety measures were taken|安全対策が取られた||as a trial.|試験的に。",
            "were surrounded",
        ),
        (
            "One successful example is Nevädzová Street,|成功例の一つがネヴァヅォヴァー通りで、||which used to be crowded|かつて混雑していた||with dozens of cars|何十台もの車で||driven by parents|親が運転する||trying to drop off children at school.|学校に子どもを送り届けようとする。",
            "is",
        ),
        (
            "Now,|現在では、||cars are banned from this street|この通りへの車の乗り入れが禁止されている||when children go to school.|子どもが登校するときには。",
            "are banned",
        ),
        (
            "( 18 ),|( 18 )、||during the school arrival time from 7:30 to 8:00 a.m.,|午前7時30分から8時までの登校時間帯には、||children can walk to school on their own.|子どもたちは自分たちだけで歩いて学校へ行くことができる。",
            "can walk",
        ),
        (
            "In Bratislava,|ブラチスラバでは、||any idea is tested|どんなアイデアも検証される||on a trial basis|試験的に||before being introduced permanently.|恒久的に導入される前に。",
            "is tested",
        ),
        (
            "Residents, parents, and school officials|住民、保護者、学校関係者は||can have the opportunity|機会を持つことができる||to ( 19 ).|( 19 )ための。",
            "can have",
        ),
        (
            "City officials use colorful paint and plastic poles|市の職員はカラフルなペンキとプラスチック製ポールを使う||to show new walking areas|新しい歩行エリアを示し||and indicate changed traffic patterns.|変更された交通パターンを示すために。",
            "use",
        ),
        (
            "Based on all the opinions and observations,|すべての意見と観察に基づいて、||designers can develop more permanent solutions|設計者はより恒久的な解決策を開発できる||using better materials.|より良い材料を使って。",
            "can develop",
        ),
        (
            "This careful approach leads to a final design|この慎重なアプローチは最終的な設計につながる||that meets the needs of the community|地域社会のニーズを満たし||and helps avoid expensive mistakes.|費用のかかる失敗を避けるのに役立つ。",
            "leads",
        ),
        (
            "These urban improvements|これらの都市の改善は||not only make the streets safe for children|通りを子どもにとって安全にするだけでなく||but also ( 20 ).|さらに( 20 )。",
            "make",
        ),
        (
            "Art on the streets makes the space beautiful|通りのアートは空間を美しくし||and clearly shows|そしてはっきりと示す||where people can and should not walk.|人々がどこを歩いてよく、どこを歩くべきでないかを。",
            "makes",
        ),
        (
            "In some schools,|いくつかの学校では、||professional artists produced artwork|プロの芸術家が作品を制作した||that reflected children's ideas|子どもたちの考えを反映した||about the community.|地域社会についての。",
            "produced",
        ),
        (
            "Some works are playful|作品の中には遊び心のあるものもある||in that they use flower art|花のアートを使って||to guide children|子どもたちを導くという点で||toward places around the neighborhood.|近所の場所へ。",
            "are playful",
        ),
        (
            "These art elements are changing spaces|これらのアートの要素は空間を変えつつある||that used to be mainly for cars|かつて主に車のためのものだった||into community areas|地域の場へと||where children can actively play together.|子どもたちが一緒に活発に遊べる。",
            "are changing",
        ),
    ],
    "Dead Trees": [
        ("Dead trees|枯れ木は||are often full of life.|しばしば生命に満ちあふれている。", "are"),
        (
            "In the woods, for example,|例えば森の中では、||they support many different animals and insects|枯れ木は多くの異なる動物や昆虫を支えている||in various ways.|さまざまな方法で。",
            "support",
        ),
        (
            "When a tree is no longer alive or standing,|木が生きていなかったり立っていなかったりすると、||it becomes a habitat,|それは生息地になる||or a place to live,|つまり住む場所に||for many living things.|多くの生き物にとっての。",
            "becomes",
        ),
        ("First,|まず、||mushrooms help break down the tree.|キノコが木の分解を助ける。", "help break down"),
        ("This allows insects|これにより昆虫は||to ( 21 ).|( 21 )ことができる。", "allows"),
        (
            "In turn,|すると今度は、||new insects and other creatures|新しい昆虫やその他の生き物が||begin to grow.|育ち始める。",
            "begin to grow",
        ),
        (
            "Some small animals hide|小動物の中には隠れるものもいる||under bark|樹皮の下に||that has fallen off the tree.|木から剥がれ落ちた。",
            "hide",
        ),
        ("Some birds build their houses|鳥の中には巣を作るものもいる||in holes in the wood.|木の穴に。", "build"),
        (
            "Dead trees not only provide homes for animals|枯れ木は動物に住みかを提供するだけでなく||but also help keep forests healthy.|森林を健康に保つのにも役立つ。",
            "provide",
        ),
        (
            "While still alive,|生きている間、||trees absorb carbon|木は炭素を吸収し||and help lower the amount of CO₂|CO₂の量を減らすのに役立つ||in the air.|空気中の。",
            "absorb",
        ),
        (
            "( 22 ),|( 22 )、||they serve as natural carbon storage|枯れ木は天然の炭素貯蔵庫として役割を果たす||after they die.|枯れた後も。",
            "serve",
        ),
        (
            "When the wood breaks down,|木材が分解されると、||carbon and other elements eventually return to the ground,|炭素やその他の元素は最終的に地面に戻り||helping young plants grow.|若い植物の成長を助ける。",
            "return",
        ),
        (
            "These substances are important|これらの物質は重要である||for maintaining rich forest soil.|豊かな森林土壌を維持するために。",
            "are",
        ),
        (
            "In this way,|このように、||dead trees are an important part|枯れ木は重要な一部である||of the natural forest cycle.|自然の森林サイクルの。",
            "are",
        ),
        (
            "While it is true|事実ではあるが||that dead trees are helpful to the environment,|枯れ木が環境に役立つことは、||they can also create problems|問題を引き起こすこともある||in some situations.|状況によっては。",
            "can also create",
        ),
        (
            "For instance,|例えば、||it might be necessary to remove them|枯れ木を取り除く必要があるかもしれない||from places such as parks, campgrounds, and roadsides|公園、キャンプ場、道路沿いなどの場所から||for safety reasons.|安全上の理由で。",
            "might be necessary",
        ),
        ("This is especially important|これは特に重要である||( 23 ).|( 23 )。", "is"),
        (
            "In these conditions,|こうした状況では、||dead trees lack moisture|枯れ木は水分を欠き||and can catch fire easily,|簡単に火がつくことがあり||causing serious damage.|深刻な被害をもたらす。",
            "lack",
        ),
        (
            "Removing dead trees where necessary|必要な場所で枯れ木を取り除くことは||can help prevent more serious issues|より深刻な問題を防ぐのに役立つ||in the future.|将来の。",
            "can help prevent",
        ),
    ],
    "Inquiry about the factory": [
        ("Dear|親愛なる||James White,|ジェームズ・ホワイト様", ""),
        (
            "My name is Jessica Jenkins,|私はジェシカ・ジェンキンスと申します、||and I teach|そして教えています||at Riverstone High School.|リバーストーン高校で。",
            "teach",
        ),
        (
            "Our students have been learning about manufacturing|本校の生徒たちは製造業について学んでおり||in social studies class,|社会科の授業で、||and one of my students has shown a strong interest|生徒の一人が強い興味を示しています||in how everyday products, such as plastic bottles, are made.|ペットボトルなどの日用品がどのように作られるかに。",
            "have been learning",
        ),
        (
            "He found your factory's information online|彼はオンラインで貴工場の情報を見つけ||and was impressed|そして感銘を受けました||by the work you did.|皆さまの仕事に。",
            "found",
        ),
        (
            "After doing some research on his own,|自分なりに調べた後、||he would like to visit your factory|彼は貴工場を見学したいと考えています||to learn more.|さらに学ぶために。",
            "would like to visit",
        ),
        (
            "I am writing to ask|お尋ねしたく、ご連絡しております||whether it would be possible|可能かどうかを||for the student to join one of the factory tours|その生徒が工場見学ツアーの一つに参加することが||held on Fridays|金曜日に開催される||by himself.|一人で。",
            "am writing",
        ),
        (
            "His last class of the day ends at 2:00 p.m. on Fridays,|金曜日は彼のその日の最後の授業が午後2時に終わり||which is earlier|それは早い時間です||than on other days.|他の曜日よりも。",
            "ends",
        ),
        (
            "As the school is within walking distance of your factory,|学校は貴工場から徒歩圏内にありますので、||if he leaves right after the class,|授業後すぐに出発すれば、||he should be able to arrive|到着できるはずです||by 2:30 p.m.|午後2時30分までに。",
            "should be able to arrive",
        ),
        (
            "Please let me know|教えてください||if there is an available date and time|参加できる日時があるかどうか||for a tour on a Friday|金曜日のツアーで||in the next two months.|今後2か月以内に。",
            "let me know",
        ),
        (
            "Could you also tell us|また教えていただけますでしょうか||what he should bring or prepare|彼が何を持参または準備すべきかを||in advance?|事前に。",
            "tell us",
        ),
        (
            "He would like to take a few photos|彼は写真を数枚撮りたいと考えています||for his class report,|授業のレポート用に、||so please let us know|ですのでお知らせください||whether photography is permitted|写真撮影が許可されているかどうかを||during the tour.|ツアー中に。",
            "would like to take",
        ),
        (
            "Thank you very much|誠にありがとうございます||for your time and consideration.|お時間とご配慮をいただき。",
            "Thank you",
        ),
        ("I look forward|私は楽しみにしております||to hearing from you.|あなたからのお返事を。", "look forward to hearing"),
        (
            "Sincerely,|敬具||Jessica Jenkins|ジェシカ・ジェンキンス||Riverstone High School|リバーストーン高校",
            "",
        ),
    ],
    "The Lost City": [
        (
            "About two thousand years ago,|約2000年前、||the city of Baia was|バイアの町は～だった||like the Las Vegas of the Roman Empire.|ローマ帝国のラスベガスのような存在。",
            "was",
        ),
        (
            "As it was conveniently located|便利な場所にあったため||just about thirty kilometers from Naples|ナポリからわずか約30キロの||on the west coast of Italy,|イタリア西海岸で、||wealthy people in Rome visited the city|ローマの裕福な人々がこの町を訪れ||and enjoyed parties, hot springs, and the warm climate.|パーティーや温泉、温暖な気候を楽しんだ。",
            "visited",
        ),
        (
            "Famous poets, speakers, and experts on nature|有名な詩人、弁論家、自然の専門家たちも||also had their houses|家を持っていた||near the bay or public baths|湾や公衆浴場の近くに||to restore their energy.|英気を養うために。",
            "had",
        ),
        (
            "Baia has been known as a hot spring resort|バイアは温泉リゾートとして知られてきており||since ancient times,|古代から、||and its name remains in history.|その名は歴史に残っている。",
            "has been known",
        ),
        ("Even Emperor Hadrian|皇帝ハドリアヌスでさえ||spent his last years in Baia.|晩年をバイアで過ごした。", "spent"),
        (
            "Baia had a volcano and hot springs,|バイアには火山と温泉があり||which attracted visitors|それらが訪問者を引きつけ||and made the city popular and successful.|町を人気のある繁栄した場所にした。",
            "had",
        ),
        (
            "However,|しかし、||this volcano caused the city's collapse|この火山が町の崩壊を引き起こした||eventually.|最終的には。",
            "caused",
        ),
        (
            "As is common in areas with volcanoes,|火山のある地域ではよくあることだが、||the surface of the land rose and sank|土地の表面は隆起と沈降を繰り返した||over many centuries.|何世紀にもわたって。",
            "rose and sank",
        ),
        (
            "This caused more and more parts of the land|これにより土地のますます多くの部分が||to sink underground gradually.|徐々に地中へ沈んでいった。",
            "caused",
        ),
        (
            "Over the past two thousand years,|過去2000年の間に、||many parts of Baia have sunk,|バイアの多くの部分が沈み||and about half of the city's structures|そして町の建造物の約半分が||are now underwater.|現在では水中にある。",
            "have sunk",
        ),
        (
            "It was not until the 1940s|1940年代になって初めて||that this underwater part of the city|この町の水中部分が||began attracting attention.|注目を集め始めた。",
            "began attracting",
        ),
        (
            "An Italian military pilot discovered mysterious structures|イタリア軍のパイロットが謎の構造物を発見した||under the water in the bay|湾の水中にある||while flying low.|低空飛行中に。",
            "discovered",
        ),
        (
            "Walls and roads in the water|水中の壁や道路が||were seen clearly|はっきりと写っていた||in the picture he took.|彼が撮影した写真に。",
            "were seen",
        ),
        (
            "However,|しかし、||investigation in the water only began|水中での調査は初めて始まった||after scuba devices were advanced enough.|スキューバ装備が十分に進歩した後に。",
            "only began",
        ),
        (
            "Later investigations revealed a room|その後の調査で部屋が発見され||filled with large sculptures,|大きな彫刻で満たされた、||and since the early 2000s,|そして2000年代初頭以降、||the part of the city that sank into the sea|海に沈んだ町の部分は||has been managed as a protected marine area.|保護海域として管理されている。",
            "revealed",
        ),
        (
            "Currently,|現在、||tourists can experience|観光客は体験できる||this underwater part of the city|この町の水中部分を||in various ways.|さまざまな方法で。",
            "can experience",
        ),
        (
            "Divers can explore the ancient Roman city|ダイバーは古代ローマ都市を探検できる||in the water|水中の||with guides.|ガイドと一緒に。",
            "can explore",
        ),
        (
            "When the ocean is calm,|海が穏やかなときは、||visitors can see the structures|訪問者は構造物を見ることができる||in the water|水中の||through the glass bottom of boats.|船のガラス底を通して。",
            "can see",
        ),
        (
            "In addition to the underwater sites,|水中の遺跡に加えて、||some ruins on land,|陸上に残るいくつかの遺跡も||such as dome-shaped public baths,|ドーム型の公衆浴場など、||can be visited on foot.|徒歩で訪れることができる。",
            "can be visited",
        ),
        (
            "Visiting Baia offers a rare chance|バイアを訪れることは貴重な機会を提供してくれる||to experience both ancient Roman history|古代ローマの歴史と||and the beauty of the sea|海の美しさの両方を体験できる||in one place.|一つの場所で。",
            "offers",
        ),
    ],
}


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


with open(DATA_PATH, encoding="utf-8") as handle:
    data = json.load(handle)

questions = {}
passages = []
for section in data.get("sections", []):
    for question in section.get("questions", []):
        questions[question["number"]] = question
    for passage in section.get("passages", []):
        passages.append(passage)
        for question in passage.get("questions", []):
            questions[question["number"]] = question

if sorted(questions) != list(range(1, 32)):
    raise SystemExit(f"question numbers mismatch: {sorted(questions)}")

for number, question in questions.items():
    if question.get("answer") != OFFICIAL_READING[number]:
        raise SystemExit(f"Q{number}: official answer mismatch")
    if len(question.get("choices", [])) != 4:
        raise SystemExit(f"Q{number}: choices must be four")
    question["choiceTranslations"] = CHOICE_TRANSLATIONS[number]
    question["grammar"] = GRAMMAR[number]
    if number in QUESTION_TRANSLATIONS:
        question["questionTranslation"] = QUESTION_TRANSLATIONS[number]
    if number in SOURCE_EVIDENCE:
        question["sourceEvidence"] = SOURCE_EVIDENCE[number]

    analyses = question.get("choiceAnalysis", [])
    if len(analyses) != 4:
        raise SystemExit(f"Q{number}: choiceAnalysis must be four")
    for choice, analysis in enumerate(analyses, 1):
        if analysis.startswith(("✅", "❌", "○")):
            raise SystemExit(f"Q{number} choice{choice}: leading marker is forbidden")
        has_correct_marker = "→正解。💡" in analysis
        if has_correct_marker != (choice == question["answer"]):
            raise SystemExit(f"Q{number} choice{choice}: correct marker mismatch")

# Eメールの呼びかけと署名を原本どおり本文・対訳・sentencePairsへ含める。
email = next((p for p in passages if p.get("title") == "Inquiry about the factory"), None)
if email is None:
    raise SystemExit("email passage not found")

greeting_en = "Dear James White,"
greeting_ja = "ジェームズ・ホワイト様"
closing_en = "Sincerely,\nJessica Jenkins\nRiverstone High School"
closing_ja = "敬具\nジェシカ・ジェンキンス\nリバーストーン高校"

if email["paragraphs"][0].startswith("My name is Jessica Jenkins"):
    email["paragraphs"][0] = greeting_en + "\n" + email["paragraphs"][0]
    email["translations"][0] = greeting_ja + "\n" + email["translations"][0]
if email["paragraphs"][0].startswith(greeting_en) and email["paragraphs"][-1] != closing_en:
    email["paragraphs"].append(closing_en)
    email["translations"].append(closing_ja)
if email["sentencePairs"][0][0] != greeting_en:
    email["sentencePairs"].insert(0, [greeting_en, greeting_ja])
if email["sentencePairs"][-1][0] != closing_en:
    email["sentencePairs"].append([closing_en, closing_ja])

# In turn は時間経過ではなく「すると今度は」という因果・連鎖。
dead_trees = next((p for p in passages if p.get("title") == "Dead Trees"), None)
if dead_trees is None:
    raise SystemExit("Dead Trees passage not found")
dead_trees["translations"][0] = dead_trees["translations"][0].replace(
    "やがて、新しい昆虫やその他の生き物が育ち始める。",
    "すると今度は、新しい昆虫やその他の生き物が育ち始める。",
)
for pair in dead_trees["sentencePairs"]:
    if pair[0] == "In turn, new insects and other creatures begin to grow.":
        pair[1] = "すると今度は、新しい昆虫やその他の生き物が育ち始める。"

# on their own は移動手段ではなく、子どもたちが「自分たちだけで」
# 登校できることを表す。段落訳と全文対訳を同じ表現にそろえる。
child_friendly = next((p for p in passages if p.get("title") == "Child-Friendly City"), None)
if child_friendly is None:
    raise SystemExit("Child-Friendly City passage not found")
old_walk_translation = (
    "( 18 )、午前7時30分から8時までの登校時間帯には、"
    "子どもたちは自分の足で歩いて学校に行くことができる。"
)
new_walk_translation = (
    "( 18 )、午前7時30分から8時までの登校時間帯には、"
    "子どもたちは自分たちだけで歩いて学校へ行くことができる。"
)
if old_walk_translation not in child_friendly["translations"][0]:
    raise SystemExit("Child-Friendly City paragraph translation source text changed")
child_friendly["translations"][0] = child_friendly["translations"][0].replace(
    old_walk_translation, new_walk_translation
)
for pair in child_friendly["sentencePairs"]:
    if pair[0] == (
        "( 18 ), during the school arrival time from 7:30 to 8:00 a.m., "
        "children can walk to school on their own."
    ):
        pair[1] = new_walk_translation


NO_MAIN_VERB_ENGLISH = {
    "Dear James White,",
    "Sincerely,\nJessica Jenkins\nRiverstone High School",
}


def contains_token_bounded_phrase(english: str, phrase: str) -> bool:
    """語句を英数字トークンの途中ではなく完全な境界で照合する。"""
    return bool(
        re.search(r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])", english)
    )

# 全文を2025年度2級と同じ4要素
# [English, Japanese, natural slash reading, main verb/phrase] に統一する。
pair_total = 0
used_titles = set()
for passage in passages:
    title = passage.get("title")
    specs = SENTENCE_ENRICHMENT.get(title)
    if specs is None:
        raise SystemExit(f"{title}: sentence enrichment is missing")
    used_titles.add(title)
    pairs = passage.get("sentencePairs", [])
    if len(pairs) != len(specs):
        raise SystemExit(
            f"{title}: sentence enrichment count {len(specs)} != pairs {len(pairs)}"
        )
    for index, (pair, spec) in enumerate(zip(pairs, specs), 1):
        if len(pair) < 2:
            raise SystemExit(f"{title} pair {index}: English/Japanese is missing")
        slash_reading, main_verb = spec
        slash_english = []
        slash_chunks = slash_reading.split("||")
        if len(slash_chunks) < 2:
            raise SystemExit(
                f"{title} pair {index}: slash reading must contain multiple meaning units"
            )
        for chunk_index, chunk in enumerate(slash_chunks, 1):
            if chunk.count("|") != 1:
                raise SystemExit(
                    f"{title} pair {index} chunk {chunk_index}: "
                    "slash chunk must be English|Japanese"
                )
            english_unit, japanese_unit = chunk.split("|", 1)
            if not english_unit.strip() or not japanese_unit.strip():
                raise SystemExit(
                    f"{title} pair {index} chunk {chunk_index}: empty slash unit"
                )
            slash_english.append(english_unit)
        if compact(" ".join(slash_english)) != compact(pair[0]):
            raise SystemExit(
                f"{title} pair {index}: slash English does not reconstruct source"
            )
        if pair[0] in NO_MAIN_VERB_ENGLISH:
            if main_verb != "":
                raise SystemExit(
                    f"{title} pair {index}: non-sentence must have an empty main verb"
                )
        elif not main_verb or not contains_token_bounded_phrase(pair[0], main_verb):
            raise SystemExit(
                f"{title} pair {index}: main verb/phrase is not a source token phrase: "
                f"{main_verb!r}"
            )
        pair[:] = [pair[0], pair[1], slash_reading, main_verb]
        pair_total += 1

if used_titles != set(SENTENCE_ENRICHMENT):
    raise SystemExit(
        "unused sentence enrichment titles: "
        + repr(sorted(set(SENTENCE_ENRICHMENT) - used_titles))
    )
if pair_total != 68:
    raise SystemExit(f"sentence pair total {pair_total} != 68")

# 本文完全一致の根拠と全文対訳を生成時にも検証する。
for passage in passages:
    corpus = " ".join(passage.get("paragraphs", []))
    for question in passage.get("questions", []):
        for phrase in question.get("sourceEvidence", []):
            if phrase not in corpus:
                raise SystemExit(f"Q{question['number']}: evidence not in source: {phrase!r}")
    pairs = passage.get("sentencePairs", [])
    if compact(" ".join(pair[0] for pair in pairs)) != compact(corpus):
        raise SystemExit(f"{passage['title']}: English sentencePairs do not cover full text")
    if compact(" ".join(pair[1] for pair in pairs)) != compact(" ".join(passage.get("translations", []))):
        raise SystemExit(f"{passage['title']}: Japanese sentencePairs do not cover full text")

data["listening"] = LISTENING

with open(DATA_PATH, "w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=4)

print(f"✅ SAT enrichment saved: {DATA_PATH}")
print("  choiceTranslations=31 grammar=31 sourceEvidence=14 listening=30")
