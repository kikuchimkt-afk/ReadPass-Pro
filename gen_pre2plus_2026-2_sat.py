# -*- coding: utf-8 -*-
"""Image-verified, reproducible source: Pre-2 Plus, 2026-2 Saturday.

Original booklet pp. 3-11 and separate official answer sheet. Run this file
to reproduce data.json including deterministic audio references.
"""
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/grade-pre2plus/2026-2-sat/data.json"


def module(suffix):
    spec = importlib.util.spec_from_file_location(suffix, ROOT / f"gen_pre2plus_2026-2_sat_{suffix}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


# stem, blank-preserving translation, four choices/translations, answer,
# four contextual explanations, grammar note
PART1 = [
    ("A : What are your daily ( 1 ) at home? Do you often help your parents?\nB : Yes. I usually clean the bathroom and do the laundry on weekends.",
     "A：家で毎日する ( 1 ) は何ですか。よく両親を手伝いますか。\nB：はい。週末にはたいてい浴室を掃除したり、洗濯をしたりします。",
     ["factors", "chores", "documents", "mistakes"], ["要因", "家事・雑用", "書類", "間違い"], 2,
     ["factors＝要因。両親を手伝う具体的な作業を指す語ではない。", "chores＝家事→正解。💡浴室の掃除と洗濯が、家庭で行う家事の例。", "documents＝書類。掃除や洗濯は書類ではない。", "mistakes＝間違い。日々の手伝いを間違いとは呼ばない。"],
     "💡daily chores は「毎日の家事」。do the laundry は「洗濯をする」。What are ...? の答えとして、次の発言で具体例が示される。"),
    ("The library in the town is very old, so the city is planning to ( 2 ) it next year. They will make it bigger and more modern.",
     "町の図書館はとても古いので、市は来年それを ( 2 ) する計画を立てています。もっと大きく、もっと現代的にする予定です。",
     ["reward", "explain", "annoy", "renovate"], ["報いる", "説明する", "いら立たせる", "改修する"], 4,
     ["reward＝報いる。図書館への褒美の話ではない。", "explain＝説明する。建物を大きく新しくする行為にならない。", "annoy＝いら立たせる。感情を持つ人ではなく図書館が目的語。", "renovate＝改修する→正解。💡古い図書館を大きく現代的にする計画に合う。"],
     "💡plan to V は「～する計画を立てる」。make＋目的語＋形容詞で「～を…にする」。bigger と more modern はともに比較級。"),
    ("The weather report said that the mountains would be covered with snow, but when the hikers arrived, the mountains were ( 3 ) and there was no snow at all.",
     "天気予報では山々は雪で覆われると言っていましたが、登山者たちが着くと山々は ( 3 ) で、雪は全くありませんでした。",
     ["firm", "dull", "bare", "late"], ["堅い・しっかりした", "退屈な・鈍い", "覆いのない", "遅い"], 3,
     ["firm＝堅い。雪で覆われているかどうかを表さない。", "dull＝退屈な・鈍い。雪が全くないという説明につながらない。", "bare＝覆いのない→正解。💡no snow at all が、山に雪の覆いがないことを説明する。", "late＝遅い。山の表面の状態には使わない。"],
     "💡be covered with は「～で覆われる」。but の前の予報と後の実際の状態を対比する。not ... at all は「全く～ない」。"),
    ("A : I'm so glad that summer vacation starts next week.\nB : Me, too. I'm really looking forward to having some ( 4 ) time.",
     "A：来週夏休みが始まるので、とてもうれしいです。\nB：私もです。( 4 ) の時間を持てるのを本当に楽しみにしています。",
     ["honesty", "fraction", "leisure", "currency"], ["正直さ", "一部分・分数", "余暇", "通貨"], 3,
     ["honesty＝正直さ。休暇の自由な時間を表さない。", "fraction＝一部分・分数。leisure time のような意味にはならない。", "leisure＝余暇→正解。💡夏休みに自由に過ごせる時間を楽しみにしている。", "currency＝通貨。休暇に得られる時間とは関係がない。"],
     "💡look forward to＋名詞・動名詞は「～を楽しみにする」。to は前置詞なので having。leisure time は「余暇の時間」。"),
    ("In the new video game Conquest, players must ( 5 ) monsters to get gold stars. If they beat a boss monster, they get 100 stars.",
     "新しいビデオゲーム『Conquest』では、プレーヤーは金の星を得るためにモンスターと ( 5 ) しなければなりません。ボスのモンスターを倒すと、星を100個得ます。",
     ["filter", "spread", "battle", "glance"], ["ろ過する", "広げる", "戦う", "ちらりと見る"], 3,
     ["filter＝ろ過する。モンスターを倒す動作ではない。", "spread＝広げる。敵を倒して報酬を得る内容に合わない。", "battle＝戦う→正解。💡次の文の beat a boss monster が、敵と戦う行動を示す。", "glance＝ちらりと見る。通常 glance at の形で、戦う意味にもならない。"],
     "💡battle＋相手は「相手と戦う」。to get は目的の不定詞。If S＋V, S＋V はゲームでの条件と結果を述べる。"),
    ("A : How much will you pay me if I work at your restaurant?\nB : We will give you a ( 6 ) of $1,500 a month.",
     "A：あなたのレストランで働いたら、いくら支払ってもらえますか。\nB：月1,500ドルの ( 6 ) を支払います。",
     ["shame", "gift", "record", "salary"], ["恥", "贈り物", "記録", "給与"], 4,
     ["shame＝恥。労働への毎月の支払いではない。", "gift＝贈り物。働く対価として定期的に支払うお金とは異なる。", "record＝記録。金額を示す毎月の報酬にならない。", "salary＝給与→正解。💡働く対価として月1,500ドルを支払う。"],
     "💡a salary of＋金額は「～の給与」。a month は「1か月につき」。未来の条件でも if 節では現在形 work を使う。"),
    ("The teacher told her students that they should not have any ( 7 ) against people from different countries. They should be friendly to everyone.",
     "先生は生徒たちに、異なる国の人々に対して ( 7 ) を持つべきではないと言いました。誰にでも親切に接するべきなのです。",
     ["envelope", "desert", "prejudice", "surgery"], ["封筒", "砂漠", "偏見", "手術"], 3,
     ["envelope＝封筒。人に対する態度を表さない。", "desert＝砂漠。異なる国の人への気持ちとは関係がない。", "prejudice＝偏見→正解。💡国にかかわらず誰にでも親切にするべき、という次の文が根拠。", "surgery＝手術。人に持つ否定的な見方を表さない。"],
     "💡prejudice against＋人は「人に対する偏見」。should not V は「～すべきでない」。friendly to＋人は「人に親切な」。"),
    ("A : Hello. I'd like to buy a new computer.\nB : Sure. I'd be happy to ( 8 ) you with your choice if you could tell me what you need it for.",
     "A：こんにちは。新しいコンピューターを買いたいのですが。\nB：もちろんです。何に使うのか教えていただければ、選ぶのを喜んで ( 8 ) します。",
     ["attach", "assist", "happen", "demand"], ["取り付ける", "手伝う", "起こる", "要求する"], 2,
     ["attach＝取り付ける。客の選択を支援する意味にならない。", "assist＝手伝う→正解。💡使用目的を聞き、コンピューター選びを手伝う店員の返答。", "happen＝起こる。自動詞で、you を目的語に取れない。", "demand＝要求する。選択を手伝うという丁寧な応対に合わない。"],
     "💡assist＋人＋with＋事柄は「人の～を手伝う」。what you need it for は「何のために必要か」という間接疑問。could は丁寧な条件表現。"),
    ("The volcano in the national park ( 9 ) last year. It sent a lot of smoke and rocks into the sky.",
     "国立公園内の火山は昨年 ( 9 ) しました。大量の煙と岩を空中へ吹き出しました。",
     ["promised", "repaired", "erupted", "explored"], ["約束した", "修理した", "噴火した", "探検した"], 3,
     ["promised＝約束した。火山が約束する話ではない。", "repaired＝修理した。火山が煙や岩を出す現象にならない。", "erupted＝噴火した→正解。💡大量の煙と岩を空中へ吹き出したことが根拠。", "explored＝探検した。火山自体が探検するとは言えない。"],
     "💡erupt は「噴火する」という自動詞。last year があるので過去形。sent ... into the sky は「～を空中へ送り出した」。"),
    ("Takeshi did not get home until after midnight. He tried to move ( 10 ) so as not to wake up his wife.",
     "タケシが帰宅したのは真夜中を過ぎてからでした。妻を起こさないように ( 10 ) 動こうとしました。",
     ["silently", "eagerly", "firmly", "honestly"], ["静かに・音を立てずに", "熱心に", "しっかりと", "正直に"], 1,
     ["silently＝音を立てずに→正解。💡眠っている妻を起こさないという目的に合う。", "eagerly＝熱心に。妻を起こさないために必要な動き方ではない。", "firmly＝しっかりと。音を立てない意味にはならない。", "honestly＝正直に。動く音の大きさを表さない。"],
     "💡not ... until は「～して初めて…する／～まで…しない」。so as not to V は「～しないように」という否定の目的。副詞が move を修飾する。"),
    ("A : Why did you stop working at the bookstore, Jenny?\nB : I wanted to keep working there, but my parents made me quit ( 11 ).",
     "A：ジェニー、どうして書店で働くのをやめたの。\nB：そこで働き続けたかったけれど、両親に ( 11 ) やめさせられたの。",
     ["in the air", "in a hurry", "against my will", "with a smile"], ["空中で・未決定で", "急いで", "自分の意志に反して", "笑顔で"], 3,
     ["in the air＝空中で・未決定で。意に反してやめたことを表さない。", "in a hurry＝急いで。早さではなく、希望と現実の食い違いが焦点。", "against my will＝意志に反して→正解。💡続けたかったのに両親にやめさせられた。", "with a smile＝笑顔で。本人の望みに反するという対比を表せない。"],
     "💡make＋人＋動詞の原形は「人に～させる」。made me quit に to は付けない。keep V-ing は「～し続ける」。"),
    ("A : What did you have for Christmas dinner?\nB : We had roast beef, mashed potatoes, and green beans. The whole meal ( 12 ) traditional Christmas foods.",
     "A：クリスマスの夕食には何を食べたの。\nB：ローストビーフ、マッシュポテト、インゲン豆を食べたよ。食事全体は伝統的なクリスマス料理で ( 12 ) いたよ。",
     ["spoke about", "stared at", "consisted of", "worried about"], ["～について話した", "～をじっと見た", "～から成っていた", "～を心配した"], 3,
     ["spoke about＝話した。食事自体が話すわけではない。", "stared at＝じっと見た。食事が料理を見るという意味になる。", "consisted of＝～から成る→正解。💡挙げられた料理が食事全体の構成要素。", "worried about＝心配した。食事自体は心配しない。"],
     "💡consist of＋構成要素は「～から成る」。能動形で使う。whole は「全体の」。have ... for dinner は「夕食に～を食べる」。"),
    ("A : Why is Tom still so upset after class today?\nB : His classmate ( 13 ) breaking the window during lunch.",
     "A：どうしてトムは今日、授業後もあんなに腹を立てているの。\nB：昼食時間に窓を割ったと、クラスメートが彼を ( 13 ) したんだ。",
     ["advised him of", "accused him of", "warned him of", "convinced him of"], ["彼に～を知らせた", "彼を～のことで非難した", "彼に～を警告した", "彼に～を確信させた"], 2,
     ["advised him of＝彼に知らせた。窓を割った責任を問われて怒る文脈に合わない。", "accused him of＝彼を非難した→正解。💡窓を割ったと責められたため腹を立てている。", "warned him of＝彼に警告した。既に行ったとされる行為への非難とは違う。", "convinced him of＝彼に確信させた。窓を割ったと責める意味にならない。"],
     "💡accuse＋人＋of＋名詞・動名詞は「人を～のことで非難する」。of の後ろなので breaking。upset はここでは「腹を立てた」。"),
    ("The town of Westport ( 14 ) after the summer festival started. People filled the streets, music played from loudspeakers, and there were smiles everywhere.",
     "夏祭りが始まると、ウェストポートの町は ( 14 )。通りは人であふれ、拡声器から音楽が流れ、あちこちに笑顔が見られました。",
     ["fell into silence", "came to mind", "took a chance", "came to life"], ["静まり返った", "思い浮かんだ", "思い切ってやってみた", "活気づいた"], 4,
     ["fell into silence＝静まり返った。人と音楽でにぎわう次の文と逆。", "came to mind＝思い浮かんだ。町のにぎわいの変化を表さない。", "took a chance＝思い切ってやった。町が危険を冒す話ではない。", "came to life＝活気づいた→正解。💡人々・音楽・笑顔が、町のにぎわいを具体的に示す。"],
     "💡come to life は「生き生きする・活気づく」。after 節は祭りが始まった時点を示す。次の文は3つの様子を並べて説明している。"),
    ("Many animals are ( 15 ) of becoming extinct because of environmental changes. Conservation groups are trying to protect them.",
     "環境の変化のため、多くの動物が絶滅する ( 15 ) にあります。自然保護団体はそれらを守ろうとしています。",
     ["on board", "in charge", "by force", "at risk"], ["乗って・参加して", "責任を負って", "力ずくで", "危険にさらされて"], 4,
     ["on board＝乗って。絶滅のおそれを表さない。", "in charge＝責任を負って。動物が絶滅の責任者なのではない。", "by force＝力ずくで。絶滅する危険という状態にならない。", "at risk＝危険にさらされて→正解。💡絶滅のおそれがあるため、保護団体が守ろうとしている。"],
     "💡at risk of V-ing は「～する危険にさらされて」。become extinct は「絶滅する」。because of の後ろは名詞 environmental changes。"),
    ("A : Are you ready to leave for school now? Have you tidied up your room?\nB : Almost. I just need to ( 16 ) and grab my bag.",
     "A：もう学校へ出かける準備はできた。部屋は片付けた。\nB：もう少し。あとは ( 16 ) して、かばんを持つだけだよ。",
     ["make my bed", "close my eyes", "read a book", "wash the car"], ["ベッドを整える", "目を閉じる", "本を読む", "車を洗う"], 1,
     ["make my bed＝ベッドを整える→正解。💡部屋の片付けと登校準備の最後の作業として自然。", "close my eyes＝目を閉じる。部屋を片付けて登校する準備にならない。", "read a book＝本を読む。片付けの残り作業ではない。", "wash the car＝車を洗う。自分の部屋の片付けとは関係がない。"],
     "💡make one's bed は「ベッドを整える」。Have you tidied up ...? は現在完了で完了を確認する。need to V は「～する必要がある」。"),
    ("The new president of the company does not ( 17 ) many of the other employees. He has his own office at the top of the building.",
     "その会社の新しい社長は、他の多くの従業員と ( 17 ) することがありません。建物の最上階に自分専用のオフィスがあります。",
     ["take the place of", "take full advantage of", "come into contact with", "fall in love with"], ["～に取って代わる", "～を最大限に利用する", "～と接触する", "～と恋に落ちる"], 3,
     ["take the place of＝取って代わる。多数の従業員の代わりになる話ではない。", "take full advantage of＝最大限に利用する。離れたオフィスの説明から導けない。", "come into contact with＝接触する→正解。💡最上階の専用オフィスにいて、他の従業員と会う機会が少ない。", "fall in love with＝恋に落ちる。会社での交流の少なさとは関係がない。"],
     "💡come into contact with＋人は「人と接触する」。does not の後ろは原形 come。his own office は「自分専用のオフィス」。"),
]


def build():
    p = module("passages")
    m = module("materials")
    questions = [dict(number=n, text=r[0], translation=r[1], choices=r[2],
                      choiceTranslations=r[3], answer=r[4], choiceAnalysis=r[5], grammar=r[6])
                 for n, r in enumerate(PART1, 1)]
    sections = [
        dict(name="大問1", nameEn="Part 1", type="vocabulary",
             instruction="次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", questions=questions),
        dict(name="大問2", nameEn="Part 2", type="passage-fill",
             instruction="次の英文A，Bを読み，その文意にそって(18)から(23)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=p.PASSAGES[:2]),
        dict(name="大問3", nameEn="Part 3", type="reading-comprehension",
             instruction="次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。", passages=p.PASSAGES[2:]),
    ]
    listening = [3,2,1,2,3,2,1,4,2,4,2,2,4,1,1,1,4,1,3,4,1,2,1,3,3,4,1,4,2,2]
    return dict(grade="準2級プラス", year="2026", session="2-sat",
                title="2026年度 第2回（土曜準会場）英検準2級プラス リーディング",
                vocabulary=m.vocabulary(), sections=sections, lessonPlan=m.lessonplan(p.PASSAGES),
                listening={"part1":dict(zip(map(str,range(1,16)),listening[:15])),
                           "part2":dict(zip(map(str,range(16,31)),listening[15:]))})


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(OUT)
