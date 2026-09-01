# -*- coding: utf-8 -*-
"""Install the official 2026-1 Grade Pre-1 Part 1 into ReadPass data."""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-1" / "data.json"


QUESTIONS = [
    {
        "number": 1,
        "text": "In order to illustrate how a cell functions, the biology teacher drew a detailed ( 1 ) on the board showing all of its parts.",
        "translation": "細胞がどのように機能するかを説明するため、生物の先生は、そのすべての部分を示す詳細な ( 1 ) を黒板に描いた。",
        "choices": ["cemetery", "diagram", "equation", "forecast"],
        "answer": 2,
        "choiceAnalysis": [
            "❌ cemetery＝墓地 → 細胞の各部分を黒板に描いて示す場面なので、場所を表す「墓地」は文脈に合わない。",
            "✅ diagram＝図・図解 → 正解。💡 drew on the board と showing all of its parts から、細胞の構造を示す「詳細な図」が自然。",
            "❌ equation＝方程式 → 数式なら solve や calculate などと結びつくが、ここでは細胞の全部位を視覚的に示している。",
            "❌ forecast＝予測・予報 → 将来の出来事を予測する語であり、細胞の構造を説明する絵には使えない。",
        ],
        "grammar": "💡 in order to + 動詞は「〜するために」。how a cell functions は「細胞がどのように機能するか」という間接疑問で、showing 以下は diagram の内容を補足する分詞句。",
    },
    {
        "number": 2,
        "text": "A: I think this sentence in your essay is ( 2 ).\nB: Oh, you're right. It's almost the same as what I said in the previous paragraph.",
        "translation": "A：あなたの作文のこの文は ( 2 ) だと思います。\nB：ああ、その通りです。前の段落で述べたこととほとんど同じですね。",
        "choices": ["possessive", "horizontal", "redundant", "drastic"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ possessive＝所有の・独占欲の強い → 文の内容が前段落と重なるという指摘とは関係がない。",
            "❌ horizontal＝水平の → 位置や方向を表す形容詞で、作文中の文の重複を評価する語ではない。",
            "✅ redundant＝重複している・余分な → 正解。💡 almost the same as what I said in the previous paragraph が、同じ内容を繰り返していて不要だと示している。",
            "❌ drastic＝抜本的な・急激な → drastic change のように大きな変化を表す語で、この文が前の内容と重なることは表せない。",
        ],
        "grammar": "💡 the same as ... は「〜と同じ」。what I said は「私が述べたこと」で、what が先行詞を含む関係代名詞として said の目的語になっている。",
    },
    {
        "number": 3,
        "text": "In some countries, governments ( 3 ) the media in order to prevent criticism of them from being published.",
        "translation": "一部の国では、政府は自分たちへの批判が公表されるのを防ぐためにメディアを ( 3 ) する。",
        "choices": ["haul", "envy", "subtract", "censor"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ haul＝強く引く・運搬する → 物を引っ張ったり運んだりする動詞で、報道内容を制限する行為にはならない。",
            "❌ envy＝うらやむ → governments envy the media では、批判の公表を防ぐという目的につながらない。",
            "❌ subtract＝差し引く → 数量を引く意味であり、政府とメディアの関係を表す目的語 the media には不適切。",
            "✅ censor＝検閲する → 正解。💡 criticism ... from being published を防ぐために、政府がメディアの内容を審査・制限する文脈。",
        ],
        "grammar": "💡 prevent A from -ing は「Aが〜するのを防ぐ」。ここでは A が criticism of them、being published は受動態の動名詞で「公表されること」。",
    },
    {
        "number": 4,
        "text": "The scholarship is only available to students who meet its requirements. A ( 4 ) must have excellent grades and be from a low-income background.",
        "translation": "その奨学金を利用できるのは条件を満たす学生だけである。( 4 ) は、成績が優秀で、低所得の家庭の出身でなければならない。",
        "choices": ["referral", "recipient", "bouncer", "successor"],
        "answer": 2,
        "choiceAnalysis": [
            "❌ referral＝紹介・照会 → 人そのものではなく、専門家への紹介や問い合わせを表す名詞なので、奨学金を受ける学生を指せない。",
            "✅ recipient＝受給者・受取人 → 正解。💡 scholarship の条件を満たして実際に受け取る人について、成績と家庭状況の要件を述べている。",
            "❌ bouncer＝用心棒・入場整理係 → 店や会場で入場を管理する人で、奨学金制度の対象者ではない。",
            "❌ successor＝後継者 → 役職や地位を引き継ぐ人を表し、奨学金を受け取る人という意味にはならない。",
        ],
        "grammar": "💡 students who meet its requirements の who は students を修飾する主格の関係代名詞。must have ... and be ... では、助動詞 must が have と be の両方にかかる。",
    },
    {
        "number": 5,
        "text": "The scientist was accused of ( 5 ) his data after experts attempted to copy his experiments but were unable to produce the same results.",
        "translation": "専門家たちがその科学者の実験を再現しようとしたものの同じ結果を得られなかったため、彼はデータを ( 5 ) したとして非難された。",
        "choices": ["triggering", "fabricating", "conserving", "renouncing"],
        "answer": 2,
        "choiceAnalysis": [
            "❌ triggering＝引き起こすこと → trigger data という結びつきは不自然で、他の専門家が結果を再現できない理由にならない。",
            "✅ fabricating＝捏造すること → 正解。💡 同じ実験結果を再現できなかったため、データを作り上げたのではないかと accused of された。",
            "❌ conserving＝保存すること・保護すること → データを保存することは通常の研究行為であり、再現不能を受けた非難の内容にならない。",
            "❌ renouncing＝放棄すること → 権利や主張を正式に捨てる意味で、data を目的語にして実験結果の不正を表す語ではない。",
        ],
        "grammar": "💡 be accused of -ing は「〜したとして非難される」。attempt to + 動詞は「〜しようとする」、be unable to + 動詞は「〜することができない」。",
    },
    {
        "number": 6,
        "text": "Last week, a police officer stopped Javier and gave him a traffic ( 6 ) for driving faster than the speed limit.",
        "translation": "先週、警察官がハビエルを止め、制限速度を超えて運転したことで交通 ( 6 ) を渡した。",
        "choices": ["ransom", "specimen", "cavity", "citation"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ ransom＝身代金 → 誘拐された人を解放するための金銭であり、速度違反に対する警察の処分ではない。",
            "❌ specimen＝標本・検体 → 研究や検査のための試料を指すため、traffic と結びつかない。",
            "❌ cavity＝空洞・虫歯 → 身体や物体の穴を表す名詞で、警察が運転者に渡すものではない。",
            "✅ citation＝違反切符・召喚状 → 正解。💡 traffic citation は交通違反切符。driving faster than the speed limit が交付理由を示す。",
        ],
        "grammar": "💡 give 人 物 は「人に物を与える」。for -ing はここでは理由を表し、for driving faster than ... で「制限速度を超えて運転したため」。",
    },
    {
        "number": 7,
        "text": "Because some ( 7 ) was expected, the captain turned on the seat belt sign and asked all the passengers to return to their seats.",
        "translation": "多少の ( 7 ) が予想されたため、機長はシートベルト着用サインを点灯し、すべての乗客に座席へ戻るよう求めた。",
        "choices": ["distortion", "generosity", "turbulence", "conjecture"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ distortion＝歪み・曲解 → 形や情報がゆがむことは、機内でシートベルトを着用させる直接の理由にならない。",
            "❌ generosity＝寛大さ → 人の気前のよさを表し、飛行中に予想される気象・機体状況ではない。",
            "✅ turbulence＝乱気流 → 正解。💡 captain、seat belt sign、return to their seats から、飛行機が揺れる乱気流への備えだと分かる。",
            "❌ conjecture＝推測・憶測 → 推測が予想された、という意味では不自然で、乗客の安全確保とも結びつかない。",
        ],
        "grammar": "💡 Because some turbulence was expected は受動態で理由を示す節。ask 人 to + 動詞は「人に〜するよう求める」。",
    },
    {
        "number": 8,
        "text": "After several years with almost no rain, the area became a ( 8 ) wasteland where no trees or other plants could survive.",
        "translation": "ほとんど雨が降らない年が数年続いた後、その地域は木も他の植物も生き残れない ( 8 ) 荒れ地になった。",
        "choices": ["nutritious", "diverse", "barren", "coincidental"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ nutritious＝栄養価の高い → 食物などに用いる語で、植物が一切生存できない荒れ地の状態とは反対。",
            "❌ diverse＝多様な → no trees or other plants とあるため、生物や植物が多様に存在する状況ではない。",
            "✅ barren＝不毛の → 正解。💡 almost no rain と no ... plants could survive が、植物の育たない不毛な土地を具体的に説明している。",
            "❌ coincidental＝偶然一致した → 出来事同士の偶然の一致を表す形容詞で、wasteland の土地状態を表せない。",
        ],
        "grammar": "💡 become + 名詞句で「〜になる」。where は a barren wasteland を先行詞とする関係副詞で、その場所では植物が生き残れないと説明する。",
    },
    {
        "number": 9,
        "text": "When Simon pulled on the rope, it suddenly became ( 9 ). He realized that it must have come untied at the other end.",
        "translation": "サイモンがロープを引くと、それは突然 ( 9 ) になった。彼は、反対側の端でほどけてしまったに違いないと気づいた。",
        "choices": ["slack", "sparse", "vast", "vital"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ slack＝緩んだ・たるんだ → 正解。💡 ロープの反対側が untied になったため張力がなくなり、引いたときにたるんだ状態になった。",
            "❌ sparse＝まばらな → 人口や植物などの密度が低いことを表す語で、ロープの張り具合には用いない。",
            "❌ vast＝広大な → 面積や規模の大きさを表すため、ほどけたロープの状態を説明できない。",
            "❌ vital＝極めて重要な・生命の → 重要性を表す語で、became の後に置いてロープの物理的変化を表すのは不自然。",
        ],
        "grammar": "💡 must have + 過去分詞は、過去の出来事への強い推量「〜したに違いない」。come untied は「結び目がほどけた状態になる」。",
    },
    {
        "number": 10,
        "text": "The patient was diagnosed with a vitamin ( 10 ). The doctor said she would need to take supplements until her vitamin levels were normal again.",
        "translation": "その患者はビタミン ( 10 ) と診断された。医師は、ビタミン値が再び正常になるまでサプリメントを摂る必要があると述べた。",
        "choices": ["descendant", "triumph", "emission", "deficiency"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ descendant＝子孫 → 人の血縁関係を示す名詞で、vitamin の不足状態や診断名にはならない。",
            "❌ triumph＝勝利・大成功 → 健康上の問題を表さず、サプリメントを必要とする理由にもならない。",
            "❌ emission＝排出・放出 → gas emissions などに用い、体内のビタミン値が低い状態を指さない。",
            "✅ deficiency＝不足・欠乏 → 正解。💡 vitamin deficiency は「ビタミン欠乏症」。levels が normal になるまで supplements を摂るという治療内容とも一致する。",
        ],
        "grammar": "💡 be diagnosed with ... は「〜と診断される」。until S V は「SがVするまで」で、正常値に戻る時点まで服用が続く。",
    },
    {
        "number": 11,
        "text": "Tanya seemed shy and nervous when she entered her new school, but she is now ( 11 ) socially and has made a lot of friends.",
        "translation": "ターニャは新しい学校に入ったとき内気で不安そうだったが、今では社交面で ( 11 ) しており、多くの友達ができた。",
        "choices": ["flourishing", "pledging", "scattering", "drooping"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ flourishing＝順調に成長している・活躍している → 正解。💡 shy and nervous だった以前と対照的に、now と has made a lot of friends が社交面でうまくいっていることを示す。",
            "❌ pledging＝誓約している → promise の意味で、socially と結びつけて友人関係が良好な状態を表すことはできない。",
            "❌ scattering＝散らしている・散らばっている → 人や物が分散する動作で、友達が増えたという前向きな変化に合わない。",
            "❌ drooping＝垂れ下がっている・元気を失っている → 植物や姿勢がしおれる様子で、has made a lot of friends と意味が反対。",
        ],
        "grammar": "💡 seem + 形容詞は「〜のように見える」。but を境に過去 entered と現在 is now / has made が対比され、環境への適応を表す。",
    },
    {
        "number": 12,
        "text": "The art student showed her ( 12 ) to the gallery owner. It contained samples of her paintings, drawings, and photographs.",
        "translation": "その美術学生はギャラリーのオーナーに自分の ( 12 ) を見せた。それには絵画、素描、写真の見本が収められていた。",
        "choices": ["reptile", "glacier", "blockade", "portfolio"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ reptile＝爬虫類 → 動物の分類名であり、作品見本を収めるものではない。",
            "❌ glacier＝氷河 → 地形・自然現象を指すため、美術学生がオーナーに提示する資料にはならない。",
            "❌ blockade＝封鎖 → 交通や物資の流れを遮断する行為・障害で、paintings などを収録できない。",
            "✅ portfolio＝作品集・ポートフォリオ → 正解。💡 paintings, drawings, and photographs の samples をまとめ、gallery owner に実力を示す作品集を指す。",
        ],
        "grammar": "💡 show A to B は「AをBに見せる」。It は直前の portfolio を受け、contained samples of ... がその中身を説明する。",
    },
    {
        "number": 13,
        "text": "The teacher asked the student to ( 13 ) his essay. She said it should be about half the length it was.",
        "translation": "先生はその生徒に作文を ( 13 ) するよう求めた。長さを元のおよそ半分にすべきだと言った。",
        "choices": ["abbreviate", "attest", "carve", "yield"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ abbreviate＝短縮する → 正解。💡 essay を half the length にするという指示なので、内容を短くまとめることを求めている。",
            "❌ attest＝証明する・証言する → 事実が正しいと保証する意味で、作文の長さを半分にする作業ではない。",
            "❌ carve＝彫る・切り分ける → 木や石、肉などを物理的に切る語で、essay を短く編集する意味には通常使わない。",
            "❌ yield＝産出する・譲る → 結果を生む、道を譲るなどの意味で、文章量を減らす指示と一致しない。",
        ],
        "grammar": "💡 ask 人 to + 動詞は「人に〜するよう頼む」。half the length it was は「以前の長さの半分」で、the length の後に関係詞 that が省略されている。",
    },
    {
        "number": 14,
        "text": "The patient was in so much pain that the dentist had no choice but to ( 14 ) the patient's damaged tooth.",
        "translation": "患者は非常に強い痛みに苦しんでいたため、歯科医は患者の傷んだ歯を ( 14 ) するほかなかった。",
        "choices": ["radiate", "magnify", "extract", "impart"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ radiate＝放射する・発する → 光や熱を外へ出す意味で、dentist が damaged tooth に行う処置ではない。",
            "❌ magnify＝拡大する → 見え方や重要性を大きくする語で、激痛を解消する歯科治療にならない。",
            "✅ extract＝抜き取る・抜歯する → 正解。💡 damaged tooth と so much pain から、歯科医が痛みの原因となる歯を抜く処置だと分かる。",
            "❌ impart＝与える・伝える → 知識や性質を人・物に与える語で、歯を取り除く意味はない。",
        ],
        "grammar": "💡 so ... that S V は「とても…なのでSはVする」。have no choice but to + 動詞は「〜するほか選択肢がない」。",
    },
    {
        "number": 15,
        "text": "The company was badly affected by the financial crisis and nearly ( 15 ), but it has now recovered and is making a profit again.",
        "translation": "その会社は金融危機で深刻な影響を受け、危うく ( 15 ) ところだったが、今では回復して再び利益を上げている。",
        "choices": ["sank in", "let out", "went under", "lived off"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ sank in＝徐々に理解された・身にしみた → 情報や現実が人に理解されるときに使い、会社が危機で倒産しかける意味ではない。",
            "❌ let out＝外に出した・漏らした → 人を解放する、声を発するなどの意味で、会社の経営破綻を表さない。",
            "✅ went under＝倒産した → 正解。💡 financial crisis で badly affected された後、recovered and is making a profit again とあるため、会社が破綻寸前だったという対比になる。",
            "❌ lived off＝〜を生活の糧にした → 資金源に頼って暮らす意味で、nearly の後に置いて会社の危機的状態を表す語句ではない。",
        ],
        "grammar": "💡 go under は企業について「倒産する」。nearly + 過去形で「もう少しで〜するところだった」、but 以下の現在完了 has recovered と現在進行形が現在の回復を示す。",
    },
    {
        "number": 16,
        "text": "The police officer became suspicious of the man because his story did not ( 16 ). He was later found to have lied to the police.",
        "translation": "その警察官は、男の話が ( 16 ) なかったため、彼を疑うようになった。男は後に警察にうそをついていたことが判明した。",
        "choices": ["add up", "read into", "take off", "fall out"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ add up＝つじつまが合う → 正解。💡 story did not add up は「話の筋が通らなかった」。後に lied と分かったことが警官の疑いを裏づける。",
            "❌ read into＝〜を深読みする → 通常 read too much into ... のように人が物事を過度に解釈する表現で、story 自体を主語にできない。",
            "❌ take off＝離陸する・急に成功する・脱ぐ → 飛行機や衣服などに用いる句動詞で、話の論理的一貫性を表さない。",
            "❌ fall out＝仲たがいする・抜け落ちる → 人間関係や物の脱落を表し、story did not ... の補語としては不自然。",
        ],
        "grammar": "💡 become suspicious of ... は「〜を疑うようになる」。be found to have + 過去分詞は「〜していたことが判明する」で、発覚より前の行為を完了不定詞で示す。",
    },
    {
        "number": 17,
        "text": "The patient tried to ( 17 ) from the hospital without anyone noticing, but the nurse saw him and stopped him.",
        "translation": "その患者は誰にも気づかれずに病院から ( 17 ) しようとしたが、看護師に見つかって止められた。",
        "choices": ["slip away", "tear up", "drop out", "follow up"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ slip away＝こっそり立ち去る → 正解。💡 without anyone noticing が、人目につかないよう病院を抜け出そうとしたことを明示している。",
            "❌ tear up＝引き裂く → 紙などをばらばらにする他動詞的な句で、from the hospital と結びついて退出を表せない。",
            "❌ drop out＝中退する・脱落する → 学校や競技などを途中でやめる語で、患者がその場からこっそり去る動作とは異なる。",
            "❌ follow up＝追跡調査する・追加対応する → 情報や治療を後から確認する意味で、病院から逃げる行為にはならない。",
        ],
        "grammar": "💡 try to + 動詞は「〜しようとする」。without + 名詞 + -ing で「名詞が〜することなく」となり、without anyone noticing は独立した意味上の主語を含む。",
    },
    {
        "number": 18,
        "text": "A: Our meeting prep took longer than expected.\nB: Yeah, the budget review really ( 18 ) most of our afternoon.",
        "translation": "A：会議の準備は予想より長くかかりました。\nB：ええ、予算の見直しに午後の大半を本当に ( 18 ) しまいました。",
        "choices": ["fed off", "burnt out", "fell through", "ate up"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ fed off＝〜を餌・エネルギー源にした → 生物や感情が何かを糧にする表現で、review が時間を大量に使う意味にはならない。",
            "❌ burnt out＝燃え尽きた・疲れ果てた → 人や機器の消耗を表す句で、most of our afternoon を目的語に取って時間消費を表せない。",
            "❌ fell through＝失敗に終わった → 計画や取引が成立しない意味。会議準備が長引いたのであり、予算見直しが中止になったとは述べていない。",
            "✅ ate up＝大量に消費した → 正解。💡 took longer than expected と most of our afternoon から、budget review が午後の時間の大半を使ったことを表す。",
        ],
        "grammar": "💡 eat up は食べ物だけでなく、time や money を「大量に消費する」という比喩的用法がある。take longer than expected は「予想より長くかかる」。",
    },
]


SECTION = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(18)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": QUESTIONS,
}


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Base data does not exist: {DATA_PATH}. Run gen_pre1_2026-1.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    sections = data.get("sections")
    if not isinstance(sections, list):
        raise ValueError("data.json must contain a top-level 'sections' list")

    retained = [
        section
        for section in sections
        if not (
            isinstance(section, dict)
            and (section.get("type") == "vocabulary" or section.get("name") == "大問1")
        )
    ]
    data["sections"] = [SECTION, *retained]

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"Installed Part 1 (Q1-Q18) in {DATA_PATH}")


if __name__ == "__main__":
    main()
