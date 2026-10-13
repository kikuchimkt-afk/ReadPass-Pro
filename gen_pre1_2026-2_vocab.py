# -*- coding: utf-8 -*-
"""Install the deterministic 80-item vocabulary set for Grade Pre-1 2026-2.

Audio paths (wordAudio) are added by data/pre-grade1/2026-2/_gen_tts.py once
the MP3 files exist, so the app never shows a play button for missing audio.
"""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"

# The first 72 rows are all four choices from official Part 1 Q1-Q18, in order.
# The final eight rows are important expressions from the reading passages.
VOCAB_ROWS = [
    ("restrain", "取り押さえる・抑える", "動詞", "Two guards had to restrain the angry fan.", "2人の警備員が怒ったファンを取り押さえなければならなかった。", ["再充電する", "再開する", "反映する"]),
    ("recharge", "再充電する・（英気を）養う", "動詞", "I need to recharge my phone before the trip.", "旅行の前に携帯電話を充電し直す必要がある。", ["取り押さえる", "再開する", "反射する"]),
    ("resume", "再開する", "動詞", "The meeting will resume after a short break.", "会議は短い休憩の後に再開する。", ["中断する", "拘束する", "再充電する"]),
    ("reflect", "反映する・反射する", "動詞", "The survey results reflect the views of young voters.", "その調査結果は若い有権者の考えを反映している。", ["再開する", "抑え込む", "再充電する"]),
    ("dizzy", "めまいがする・ふらふらする", "形容詞", "She felt dizzy after standing up too quickly.", "彼女は急に立ち上がったせいでめまいがした。", ["熱心な", "好みがうるさい", "葉のない"]),
    ("keen", "熱心な・鋭い", "形容詞", "He is keen to learn about Japanese history.", "彼は日本の歴史について学ぶことに熱心だ。", ["めまいがする", "むき出しの", "気難しい"]),
    ("fussy", "好みがうるさい・細かいことにこだわる", "形容詞", "My son is a fussy eater who refuses most vegetables.", "息子は好き嫌いが激しく、ほとんどの野菜を食べようとしない。", ["熱心な", "めまいがする", "裸の"]),
    ("bare", "葉のない・むき出しの・裸の", "形容詞", "The bare branches shook in the cold wind.", "葉の落ちた枝が冷たい風に揺れた。", ["生い茂った", "熱心な", "めまいがする"]),
    ("dignity", "威厳・尊厳", "名詞", "The old man accepted his defeat with dignity.", "その老人は威厳を保って敗北を受け入れた。", ["論争", "君主制", "旅程"]),
    ("controversy", "論争・物議", "名詞", "The new law caused a great deal of controversy.", "新しい法律は大きな論争を引き起こした。", ["威厳", "旅程", "合意"]),
    ("monarchy", "君主制・君主国", "名詞", "The country has been a constitutional monarchy for centuries.", "その国は何世紀にもわたって立憲君主制である。", ["民主制", "論争", "尊厳"]),
    ("itinerary", "旅程・旅行計画", "名詞", "Our itinerary includes three days in Kyoto.", "私たちの旅程には京都での3日間が含まれている。", ["論争", "君主制", "威厳"]),
    ("confine", "閉じ込める・限定する", "動詞", "Please confine your comments to the topic of the meeting.", "発言は会議の議題に限ってください。", ["慣れさせる", "つかむ", "抑制する"]),
    ("inhibit", "抑制する・妨げる", "動詞", "Fear of failure can inhibit creativity.", "失敗への恐れは創造性を妨げることがある。", ["促進する", "閉じ込める", "慣れさせる"]),
    ("familiarize", "慣れさせる・精通させる", "動詞", "New employees need time to familiarize themselves with the system.", "新入社員がシステムに慣れるには時間が必要だ。", ["閉じ込める", "抑制する", "押収する"]),
    ("seize", "つかむ・押収する", "動詞", "The police seize illegal goods at the border every year.", "警察は毎年、国境で違法な品物を押収している。", ["手放す", "慣れさせる", "抑制する"]),
    ("diversion", "気晴らし・迂回路・転換", "名詞", "Drivers had to follow a diversion because the bridge was closed.", "橋が閉鎖されていたため、運転手は迂回路を通らなければならなかった。", ["緊急性", "軽蔑", "策略"]),
    ("maneuver", "策略・巧みな操作", "名詞", "The pilot performed a difficult maneuver to avoid the storm.", "パイロットは嵐を避けるために難しい操縦を行った。", ["緊急性", "気晴らし", "軽蔑"]),
    ("urgency", "緊急性・切迫", "名詞", "The doctor spoke with a sense of urgency.", "医師は切迫感を持って話した。", ["軽蔑", "迂回", "策略"]),
    ("contempt", "軽蔑・侮辱", "名詞", "He looked at the cheaters with contempt.", "彼は不正をした者たちを軽蔑のまなざしで見た。", ["尊敬", "緊急性", "気晴らし"]),
    ("dwellings", "住居・住まい（dwelling の複数形）", "名詞", "Many ancient dwellings were built from mud and stone.", "多くの古代の住居は泥と石で造られていた。", ["飾り", "避難所", "見込み"]),
    ("refuges", "避難所・保護区（refuge の複数形）", "名詞", "The mountains served as refuges for rare birds.", "山々は希少な鳥たちの避難所となった。", ["住居", "装飾品", "展望"]),
    ("prospects", "見込み・展望（prospect の複数形）", "名詞", "Her job prospects improved after she learned Chinese.", "中国語を学んでから、彼女の就職の見通しは良くなった。", ["飾り", "住居", "避難所"]),
    ("ornaments", "飾り・装飾品（ornament の複数形）", "名詞", "The children hung glass ornaments on the tree.", "子どもたちはツリーにガラスの飾りをつるした。", ["住居", "避難所", "見込み"]),
    ("rugged", "起伏の多い・ごつごつした・頑丈な", "形容詞", "The hikers crossed the rugged mountains in three days.", "ハイカーたちは3日かけて険しい山々を越えた。", ["事務の", "雄大な", "適切な"]),
    ("clerical", "事務の・事務員の", "形容詞", "She was hired to handle clerical work at the clinic.", "彼女は診療所で事務作業をするために雇われた。", ["肉体労働の", "険しい", "雄大な"]),
    ("majestic", "雄大な・威厳のある", "形容詞", "We watched the sun set over the majestic mountains.", "私たちは雄大な山々に沈む夕日を眺めた。", ["事務の", "適切な", "険しい"]),
    ("apt", "適切な・～しがちな", "形容詞", "“Unforgettable” is an apt description of the concert.", "「忘れがたい」はそのコンサートにぴったりの表現だ。", ["雄大な", "事務の", "頑丈な"]),
    ("loiter", "ぶらつく・たむろする", "動詞", "Teenagers often loiter outside the convenience store at night.", "10代の若者が夜にコンビニの外でたむろしていることがよくある。", ["嘆き悲しむ", "拍手する", "引っかく"]),
    ("scratch", "引っかく・かく", "動詞", "Try not to scratch the mosquito bite.", "蚊に刺されたところをかかないようにしなさい。", ["ぶらつく", "嘆き悲しむ", "拍手する"]),
    ("mourn", "嘆き悲しむ・悼む", "動詞", "The whole nation will mourn the loss of the great writer.", "国中がその偉大な作家の死を悼むだろう。", ["祝う", "ぶらつく", "拍手する"]),
    ("applaud", "拍手する・称賛する", "動詞", "The audience stood up to applaud the performers.", "観客は立ち上がって演者に拍手を送った。", ["ぶらつく", "引っかく", "嘆き悲しむ"]),
    ("preoccupied", "心を奪われた・頭がいっぱいの", "形容詞", "He was too preoccupied with his exams to enjoy the party.", "彼は試験のことで頭がいっぱいで、パーティーを楽しめなかった。", ["不法侵入した", "支持された", "すりおろされた"]),
    ("trespassed", "不法侵入した（trespass の過去形）", "動詞", "The hunters trespassed on private land.", "猟師たちは私有地に不法侵入した。", ["夢中になった", "支持した", "すりおろした"]),
    ("grated", "すりおろした・いらだたせた（grate の過去形）", "動詞", "She grated some cheese over the pasta.", "彼女はパスタの上にチーズを少しすりおろした。", ["不法侵入した", "支持した", "心を奪われた"]),
    ("endorsed", "支持した・承認した（endorse の過去形）", "動詞", "Several famous athletes endorsed the new shoes.", "何人かの有名な運動選手がその新しい靴を推奨した。", ["拒絶した", "不法侵入した", "すりおろした"]),
    ("column", "柱・（新聞の）コラム・縦列", "名詞", "She writes a weekly column for the local newspaper.", "彼女は地元の新聞に毎週コラムを書いている。", ["検査", "継承", "無策"]),
    ("succession", "連続・継承", "名詞", "The team won a succession of games in May.", "そのチームは5月に試合で連勝した。", ["検査", "柱", "無策"]),
    ("inaction", "何もしないこと・無策", "名詞", "The government was criticized for its inaction on climate change.", "政府は気候変動への無策を批判された。", ["行動", "検査", "継承"]),
    ("inspection", "検査・査察", "名詞", "The restaurant passed its health inspection.", "そのレストランは衛生検査に合格した。", ["無策", "継承", "柱"]),
    ("soothing", "心を落ち着かせる・なだめるような", "形容詞", "The soothing music helped the baby fall asleep.", "心地よい音楽のおかげで赤ん坊は眠りについた。", ["理想主義的な", "時間に正確な", "不器用な"]),
    ("punctual", "時間に正確な", "形容詞", "Our teacher is always punctual for class.", "私たちの先生はいつも授業の時間を守る。", ["不器用な", "理想主義的な", "なだめるような"]),
    ("clumsy", "不器用な・ぎこちない", "形容詞", "I am so clumsy that I often drop my phone.", "私はとても不器用なので、よく携帯電話を落とす。", ["器用な", "時間に正確な", "理想主義的な"]),
    ("idealistic", "理想主義的な", "形容詞", "The idealistic student wanted to end poverty in one year.", "その理想主義的な学生は、1年で貧困をなくしたいと思っていた。", ["現実的な", "不器用な", "時間に正確な"]),
    ("peculiar", "奇妙な・独特の", "形容詞", "There was a peculiar smell coming from the kitchen.", "台所から奇妙なにおいがしていた。", ["うぬぼれた", "香りのよい", "透明な"]),
    ("conceited", "うぬぼれた", "形容詞", "The conceited actor talked only about himself.", "そのうぬぼれた俳優は自分のことばかり話した。", ["謙虚な", "奇妙な", "透明な"]),
    ("fragrant", "香りのよい", "形容詞", "The garden was full of fragrant roses.", "庭は香りのよいバラでいっぱいだった。", ["悪臭のする", "奇妙な", "うぬぼれた"]),
    ("transparent", "透明な・透明性のある", "形容詞", "The company promised to be transparent about its finances.", "その会社は財務について透明性を保つと約束した。", ["不透明な", "香りのよい", "奇妙な"]),
    ("distress", "苦悩・苦痛・困窮", "名詞", "The loud noise caused the animals great distress.", "大きな音は動物たちに大きな苦痛を与えた。", ["名声", "紹介", "拘留"]),
    ("referral", "紹介・照会", "名詞", "My doctor gave me a referral to a heart specialist.", "かかりつけ医は心臓の専門医への紹介状を書いてくれた。", ["拘留", "著名さ", "苦悩"]),
    ("detention", "拘留・居残り（の罰）", "名詞", "The student was given detention for being late again.", "その生徒はまた遅刻したため居残りの罰を受けた。", ["釈放", "紹介", "著名さ"]),
    ("prominence", "著名さ・目立つこと", "名詞", "The scientist rose to prominence after her discovery.", "その科学者は発見の後、名声を得た。", ["苦悩", "拘留", "紹介"]),
    ("inheritance", "遺産・相続", "名詞", "He used his inheritance to start a small business.", "彼は相続した遺産を使って小さな事業を始めた。", ["抜粋", "におい", "議題"]),
    ("excerpt", "抜粋・引用", "名詞", "The newspaper printed an excerpt from her speech.", "新聞は彼女の演説の抜粋を掲載した。", ["全文", "遺産", "議題"]),
    ("odor", "におい・悪臭", "名詞", "A strange odor filled the old house.", "古い家には奇妙なにおいが立ち込めていた。", ["抜粋", "遺産", "議題"]),
    ("agenda", "議題・協議事項・（隠れた）意図", "名詞", "The budget is the first item on the agenda.", "予算が議題の最初の項目だ。", ["抜粋", "におい", "遺産"]),
    ("hammer out", "（協議を重ねて）まとめ上げる", "句動詞", "The two companies worked through the night to hammer out an agreement.", "2社は合意をまとめるために徹夜で作業した。", ["取り除く", "身を引く", "割り込む"]),
    ("jump in", "割り込む・（話や活動に）飛び込む", "句動詞", "Feel free to jump in if you have any questions.", "質問があれば遠慮なく話に加わってください。", ["まとめ上げる", "ふるい落とす", "辞任する"]),
    ("weed out", "取り除く・ふるい落とす", "句動詞", "The first interview helps us weed out weak candidates.", "1次面接は力不足の候補者をふるい落とすのに役立つ。", ["まとめ上げる", "割り込む", "身を引く"]),
    ("step aside", "身を引く・辞任する・脇へ寄る", "句動詞", "The chairman decided to step aside for a younger leader.", "会長は若いリーダーに道を譲るために退くことを決めた。", ["まとめ上げる", "取り除く", "割り込む"]),
    ("held against", "（hold A against B の受動態）Bに不利に扱われる・Bの不利な材料とされる", "句動詞", "His past mistakes were never held against him.", "彼の過去の過ちが、彼に不利に扱われることは一度もなかった。", ["～から遠ざけられる", "成長して～になる", "～を楽々と切り抜ける"]),
    ("kept from", "（keep A from B の受動態）Bから遠ざけられる・Bに隠される", "句動詞", "The bad news was kept from the patient.", "その悪い知らせは患者には伏せられた。", ["～に不利に扱われる", "成長して～になる", "～を楽々とこなす"]),
    ("grown into", "成長して～になる・（服などが）合うほど大きくなる", "句動詞", "The small shop has grown into a national chain.", "その小さな店は全国チェーンへと成長した。", ["～から遠ざけられる", "～に不利に扱われる", "～を楽々とこなす"]),
    ("sailed through", "～を楽々と切り抜けた・難なく通過した", "句動詞", "She sailed through the exam without any trouble.", "彼女は何の苦もなく試験を突破した。", ["成長して～になった", "～に隠された", "～に不利に扱われた"]),
    ("phase out", "段階的に廃止する", "句動詞", "The city plans to phase out plastic bags by 2030.", "市は2030年までにレジ袋を段階的に廃止する予定だ。", ["（借金を）ためる", "絶大な信頼を置く", "しつこく言い立てる"]),
    ("swear by", "～に絶大な信頼を置く・～を強く推奨する", "句動詞", "Many runners swear by this brand of shoes.", "多くのランナーがこのブランドの靴を絶賛している。", ["段階的に廃止する", "（借金を）ためる", "しつこく言い立てる"]),
    ("rub in", "すり込む・（rub it in で）嫌なことをしつこく言う", "句動詞", "Rub in the cream gently until it disappears.", "クリームが見えなくなるまでやさしくすり込んでください。", ["（借金を）ためる", "段階的に廃止する", "絶大な信頼を置く"]),
    ("run up", "（借金・請求額を）ためる", "句動詞", "It is easy to run up debt with a credit card.", "クレジットカードでは借金をためやすい。", ["段階的に廃止する", "絶大な信頼を置く", "返済する"]),
    ("set about", "～に取りかかる", "句動詞", "After breakfast, we set about cleaning the garage.", "朝食後、私たちはガレージの掃除に取りかかった。", ["～に似ていた", "～を倒した", "～を訪問した"]),
    ("took after", "～に似ていた（take after の過去形）", "句動詞", "Everyone said that the boy took after his grandfather.", "誰もがその少年は祖父に似ていると言った。", ["～に取りかかった", "～を倒した", "～に求めた"]),
    ("brought down", "倒した・下げた（bring down の過去形）", "句動詞", "The scandal brought down the government.", "そのスキャンダルで政権は倒れた。", ["～に取りかかった", "～に似ていた", "～を訪問した"]),
    ("called on", "～を訪問した・～に求めた（call on の過去形）", "句動詞", "The mayor called on residents to save water.", "市長は住民に節水を呼びかけた。", ["～に似ていた", "～に取りかかった", "～を倒した"]),
    ("malfunction", "誤作動・故障", "名詞", "A computer malfunction delayed all flights at the airport.", "コンピューターの誤作動で空港の全便が遅れた。", ["正常な作動", "設計図", "予算案"]),
    ("viability", "存続可能性・実行可能性", "名詞", "Investors questioned the viability of the project.", "投資家たちはその計画の実現可能性を疑問視した。", ["危険性", "透明性", "緊急性"]),
    ("savory", "風味豊かな・塩気のある", "形容詞", "I prefer savory snacks to sweet ones.", "私は甘いお菓子より塩味のスナックのほうが好きだ。", ["甘ったるい", "苦い", "味のない"]),
    ("receptor", "受容体", "名詞", "Taste receptors on the tongue send signals to the brain.", "舌の味覚受容体は脳に信号を送る。", ["化合物", "血流", "分泌物"]),
    ("eligibility", "資格・適格性", "名詞", "Your income determines your eligibility for the scholarship.", "奨学金を受ける資格があるかどうかは収入によって決まる。", ["就業率", "給付金", "依存"]),
    ("recession", "景気後退・不況", "名詞", "Many people lost their jobs during the recession.", "景気後退の間に多くの人が職を失った。", ["好景気", "物価上昇", "制度改革"]),
    ("invasive species", "外来侵入種", "名詞", "Invasive species can push native plants to extinction.", "外来侵入種は在来植物を絶滅に追い込むことがある。", ["在来種", "絶滅危惧種", "家畜"]),
    ("surveillance", "監視", "名詞", "The prisoner was kept under constant surveillance.", "その囚人は常に監視下に置かれていた。", ["釈放", "追放", "救出"]),
]


def build_vocabulary() -> list[dict[str, object]]:
    return [
        {
            "word": word,
            "meaning": meaning,
            "pos": pos,
            "level": "準1級",
            "example": example,
            "distractors": distractors,
            "exampleJa": example_ja,
        }
        for word, meaning, pos, example, example_ja, distractors in VOCAB_ROWS
    ]


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Base data does not exist: {DATA_PATH}. Run gen_pre1_2026-2.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    data["vocabulary"] = build_vocabulary()

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)
        handle.write("\n")

    print(f"Installed {len(data['vocabulary'])} vocabulary items in {DATA_PATH}")


if __name__ == "__main__":
    main()
