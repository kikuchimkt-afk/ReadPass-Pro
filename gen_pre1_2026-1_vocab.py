# -*- coding: utf-8 -*-
"""Install the deterministic 80-item vocabulary set for Grade Pre-1 2026-1."""

from __future__ import annotations

import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-1" / "data.json"

# The first 72 rows are all four choices from official Part 1 Q1-Q18, in order.
# The final eight rows are important expressions from the reading passages.
VOCAB_ROWS = [
    ("cemetery", "墓地", "名詞", "The old cemetery lies behind the village church.", "その古い墓地は村の教会の裏にある。", ["博物館", "研究所", "駅舎"]),
    ("diagram", "図・図解", "名詞", "The report includes a diagram of the human heart.", "その報告書には人間の心臓の図が含まれている。", ["予報", "墓地", "方程式"]),
    ("equation", "方程式・等式", "名詞", "The students solved the equation in several steps.", "生徒たちは数段階に分けてその方程式を解いた。", ["図解", "標本", "後継者"]),
    ("forecast", "予測・予報", "名詞", "The weather forecast predicts heavy rain tonight.", "天気予報では今夜の大雨が予想されている。", ["墓地", "方程式", "作品集"]),
    ("possessive", "所有の・独占欲の強い", "形容詞", "The possessive form of the noun needs an apostrophe.", "その名詞の所有格にはアポストロフィーが必要だ。", ["水平の", "重複した", "急激な"]),
    ("horizontal", "水平の", "形容詞", "Draw a horizontal line across the center of the page.", "ページの中央に水平線を引きなさい。", ["垂直の", "所有の", "不毛の"]),
    ("redundant", "余分な・重複している", "形容詞", "The editor removed a redundant sentence from the article.", "編集者は記事から重複した文を削除した。", ["不可欠な", "多様な", "栄養価の高い"]),
    ("drastic", "抜本的な・急激な", "形容詞", "The company took drastic action to reduce its losses.", "会社は損失を減らすため抜本的な措置を取った。", ["控えめな", "偶然の", "水平な"]),
    ("haul", "強く引く・運搬する", "動詞", "Workers haul the fishing nets onto the boat each morning.", "作業員は毎朝、漁網を船へ引き上げる。", ["検閲する", "差し引く", "うらやむ"]),
    ("envy", "うらやむ", "動詞", "Some people envy her ability to remain calm under pressure.", "重圧の中でも冷静でいられる彼女の能力をうらやむ人もいる。", ["運搬する", "省略する", "放射する"]),
    ("subtract", "差し引く", "動詞", "Subtract the service fee from the total amount.", "合計額からサービス料を差し引きなさい。", ["拡大する", "検閲する", "彫る"]),
    ("censor", "検閲する", "動詞", "The regime tried to censor reports that criticized its policies.", "その政権は政策を批判する報道を検閲しようとした。", ["称賛する", "運搬する", "保存する"]),
    ("referral", "紹介・照会", "名詞", "You need a doctor's referral to see the specialist.", "その専門医を受診するには医師の紹介状が必要だ。", ["受給者", "後継者", "入場整理係"]),
    ("recipient", "受取人・受給者", "名詞", "Each scholarship recipient must submit an annual report.", "奨学金の各受給者は年次報告書を提出しなければならない。", ["紹介状", "標本", "用心棒"]),
    ("bouncer", "用心棒・入場整理係", "名詞", "The bouncer checked everyone's identification at the entrance.", "入場整理係は入口で全員の身分証を確認した。", ["受給者", "後継者", "子孫"]),
    ("successor", "後継者", "名詞", "The board selected her as the retiring director's successor.", "取締役会は彼女を退任する理事の後継者に選んだ。", ["紹介者", "違反者", "受取人"]),
    ("triggering", "引き起こしている・誘発している", "動詞", "The sudden price increase is triggering public concern.", "突然の値上げが市民の懸念を引き起こしている。", ["保存している", "放棄している", "捏造している"]),
    ("fabricating", "捏造している・作り上げている", "動詞", "The researcher was dismissed for fabricating test results.", "その研究者は試験結果を捏造したことで解雇された。", ["保護している", "証明している", "差し引いている"]),
    ("conserving", "保存している・節約している", "動詞", "The new system is conserving both water and energy.", "新しいシステムは水とエネルギーの両方を節約している。", ["浪費している", "捏造している", "放棄している"]),
    ("renouncing", "放棄している・正式に捨てている", "動詞", "By renouncing the title, he gave up its privileges as well.", "その称号を放棄することで、彼はその特権も手放した。", ["獲得している", "保存している", "引き起こしている"]),
    ("ransom", "身代金", "名詞", "The kidnappers demanded a large ransom for the hostage.", "誘拐犯は人質のために多額の身代金を要求した。", ["罰金", "標本", "違反切符"]),
    ("specimen", "標本・検体", "名詞", "The laboratory examined a blood specimen from the patient.", "研究所は患者の血液検体を調べた。", ["身代金", "虫歯", "予報"]),
    ("cavity", "空洞・虫歯", "名詞", "The dentist found a small cavity in one of my teeth.", "歯科医は私の歯の一本に小さな虫歯を見つけた。", ["検体", "方程式", "封鎖"]),
    ("citation", "引用・違反切符・召喚状", "名詞", "The driver received a citation for parking illegally.", "運転者は違法駐車で違反切符を切られた。", ["身代金", "作品集", "氷河"]),
    ("distortion", "歪み・曲解", "名詞", "The rumor was a serious distortion of what she had said.", "そのうわさは彼女の発言をひどく曲解したものだった。", ["寛大さ", "乱気流", "推測"]),
    ("generosity", "寛大さ・気前のよさ", "名詞", "Her generosity helped the shelter remain open.", "彼女の寛大さのおかげで、その保護施設は運営を続けられた。", ["歪み", "欠乏", "封鎖"]),
    ("turbulence", "乱気流・激しい変動", "名詞", "The plane encountered severe turbulence over the mountains.", "飛行機は山脈上空で激しい乱気流に遭遇した。", ["寛大さ", "憶測", "安定"]),
    ("conjecture", "推測・憶測", "名詞", "The claim is based on conjecture rather than evidence.", "その主張は証拠ではなく憶測に基づいている。", ["確証", "寛大さ", "放出"]),
    ("nutritious", "栄養価の高い", "形容詞", "Beans are an inexpensive and nutritious source of protein.", "豆は安価で栄養価の高いたんぱく源だ。", ["不毛の", "有毒な", "水平の"]),
    ("diverse", "多様な", "形容詞", "The region is home to a diverse range of wildlife.", "その地域には多様な野生生物が生息している。", ["単一の", "不毛の", "偶然の"]),
    ("barren", "不毛の・実りのない", "形容詞", "Years of drought left the farmland barren.", "何年もの干ばつで農地は不毛になった。", ["肥沃な", "多様な", "栄養豊富な"]),
    ("coincidental", "偶然一致した", "形容詞", "The similarity between the two designs was purely coincidental.", "二つのデザインが似ていたのはまったくの偶然だった。", ["意図的な", "不毛の", "不可欠な"]),
    ("slack", "緩んだ・たるんだ", "形容詞", "The rope became slack when the anchor came loose.", "いかりが外れるとロープは緩んだ。", ["張り詰めた", "まばらな", "広大な"]),
    ("sparse", "まばらな・希薄な", "形容詞", "Vegetation is sparse in this dry region.", "この乾燥地域では植生がまばらだ。", ["密集した", "緩んだ", "重要な"]),
    ("vast", "広大な・莫大な", "形容詞", "A vast desert stretches beyond the town.", "町の向こうには広大な砂漠が広がっている。", ["狭い", "まばらな", "偶然の"]),
    ("vital", "極めて重要な・生命の", "形容詞", "Clean water is vital to public health.", "きれいな水は公衆衛生に不可欠だ。", ["不要な", "緩んだ", "広大な"]),
    ("descendant", "子孫", "名詞", "A descendant of the founder still manages the company.", "創業者の子孫が今もその会社を経営している。", ["祖先", "勝利", "欠乏"]),
    ("triumph", "勝利・大成功", "名詞", "The successful rescue was a triumph of teamwork.", "その救助の成功はチームワークの大きな成果だった。", ["敗北", "排出", "子孫"]),
    ("emission", "排出・放出", "名詞", "The factory reduced its carbon emissions through new technology.", "その工場は新技術によって炭素排出量を減らした。", ["吸収", "欠乏", "勝利"]),
    ("deficiency", "不足・欠乏", "名詞", "Iron deficiency can cause persistent fatigue.", "鉄分不足は持続的な疲労を引き起こすことがある。", ["過剰", "排出", "成功"]),
    ("flourishing", "繁栄している・順調に成長している", "形容詞", "The neighborhood now has a flourishing arts community.", "その地域には今、活気ある芸術コミュニティーがある。", ["衰退している", "誓約している", "垂れ下がっている"]),
    ("pledging", "誓約している・約束している", "動詞", "Several countries are pledging additional aid.", "数か国が追加支援を約束している。", ["撤回している", "散らしている", "繁栄している"]),
    ("scattering", "散らしている・まき散らしている", "動詞", "The wind is scattering leaves across the road.", "風が道路一面に葉をまき散らしている。", ["集めている", "誓っている", "しおれている"]),
    ("drooping", "垂れ下がっている・しおれている", "形容詞", "The drooping flowers needed water immediately.", "しおれた花にはすぐに水が必要だった。", ["まっすぐな", "繁栄している", "散らばった"]),
    ("reptile", "爬虫類", "名詞", "The crocodile is a large reptile found in tropical regions.", "ワニは熱帯地域に生息する大型の爬虫類だ。", ["両生類", "氷河", "作品集"]),
    ("glacier", "氷河", "名詞", "The glacier has retreated rapidly over the past decade.", "その氷河は過去10年間に急速に後退した。", ["火山", "爬虫類", "封鎖"]),
    ("blockade", "封鎖", "名詞", "The blockade prevented food from reaching the city.", "封鎖によって食料が市内へ届かなくなった。", ["開放", "作品集", "氷河"]),
    ("portfolio", "作品集・ポートフォリオ", "名詞", "Applicants must submit a portfolio of their design work.", "応募者は自分のデザイン作品集を提出しなければならない。", ["封鎖", "爬虫類", "紹介状"]),
    ("abbreviate", "短縮する・略す", "動詞", "Writers often abbreviate the term to save space.", "書き手は場所を節約するためその用語をよく短縮する。", ["詳述する", "証明する", "産出する"]),
    ("attest", "証明する・証言する", "動詞", "Several witnesses can attest to her honesty.", "数人の証人が彼女の誠実さを証言できる。", ["省略する", "彫る", "差し引く"]),
    ("carve", "彫る・切り分ける", "動詞", "The artist used a small knife to carve the figure from wood.", "芸術家は小刀で木からその像を彫り出した。", ["拡大する", "譲る", "検閲する"]),
    ("yield", "産出する・譲る", "動詞", "These fields yield enough rice to feed the entire village.", "これらの田畑は村全体を養える量の米を産出する。", ["消費する", "省略する", "証言する"]),
    ("radiate", "放射する・発する", "動詞", "The dark surface can radiate heat at night.", "その暗い表面は夜間に熱を放射できる。", ["吸収する", "抜き取る", "拡大する"]),
    ("magnify", "拡大する・誇張する", "動詞", "This lens can magnify tiny details ten times.", "このレンズは微細な部分を10倍に拡大できる。", ["縮小する", "放射する", "伝える"]),
    ("extract", "抜き取る・抽出する", "動詞", "Doctors had to extract the damaged tooth.", "医師たちは傷んだ歯を抜かなければならなかった。", ["埋め込む", "拡大する", "伝授する"]),
    ("impart", "与える・伝える", "動詞", "Good mentors impart practical knowledge to younger workers.", "優れた指導者は若い働き手に実践的な知識を伝える。", ["隠す", "抜き取る", "放射する"]),
    ("sank in", "徐々に理解された・身にしみた", "句動詞", "The seriousness of the situation finally sank in.", "事態の深刻さがようやく実感された。", ["倒産した", "外へ出した", "頼って暮らした"]),
    ("let out", "外へ出した・漏らした", "句動詞", "She let out a sigh of relief after the exam.", "彼女は試験後に安堵のため息を漏らした。", ["理解された", "倒産した", "食い尽くした"]),
    ("went under", "倒産した・沈んだ", "句動詞", "Several small businesses went under during the recession.", "不況の間にいくつかの小企業が倒産した。", ["回復した", "外へ出した", "頼って暮らした"]),
    ("lived off", "〜を頼りに生活した", "句動詞", "For months, the family lived off its savings.", "その家族は数か月間、貯金を頼りに暮らした。", ["〜を使い果たした", "〜を理解した", "〜を破産させた"]),
    ("add up", "つじつまが合う・合計になる", "句動詞", "His explanation did not add up, so the police questioned him again.", "彼の説明はつじつまが合わず、警察は再び彼に質問した。", ["深読みする", "離陸する", "仲たがいする"]),
    ("read into", "〜を深読みする", "句動詞", "Do not read into her brief reply more than she intended.", "彼女の短い返答を意図以上に深読みしてはいけない。", ["合計する", "脱ぐ", "抜け落ちる"]),
    ("take off", "離陸する・脱ぐ・急に成功する", "句動詞", "The plane will take off as soon as the runway is clear.", "滑走路が空き次第、その飛行機は離陸する。", ["着陸する", "つじつまが合う", "深読みする"]),
    ("fall out", "仲たがいする・抜け落ちる", "句動詞", "Close friends can fall out over a minor misunderstanding.", "親しい友人でも小さな誤解で仲たがいすることがある。", ["和解する", "離陸する", "合計する"]),
    ("slip away", "こっそり立ち去る", "句動詞", "He tried to slip away before anyone noticed him.", "彼は誰にも気づかれる前にこっそり立ち去ろうとした。", ["追跡する", "引き裂く", "中退する"]),
    ("tear up", "引き裂く", "句動詞", "Please do not tear up the original document.", "原本を引き裂かないでください。", ["貼り合わせる", "立ち去る", "追加対応する"]),
    ("drop out", "中退する・脱落する", "句動詞", "Financial pressure forced him to drop out of college.", "経済的な圧力で彼は大学を中退せざるを得なかった。", ["卒業する", "追跡調査する", "こっそり去る"]),
    ("follow up", "追跡調査する・追加対応する", "句動詞", "The clinic will follow up with each patient next week.", "診療所は来週、各患者に追加の連絡をする。", ["放置する", "引き裂く", "中退する"]),
    ("fed off", "〜を糧にした・餌にした", "句動詞", "The insects fed off the leaves throughout the summer.", "その昆虫は夏の間ずっと葉を餌にした。", ["〜を使い果たした", "〜に失敗した", "〜を追跡した"]),
    ("burnt out", "燃え尽きた・疲れ果てた", "句動詞", "After months without a break, she felt completely burnt out.", "何か月も休みがなく、彼女は完全に疲れ果てた。", ["元気を取り戻した", "大量に消費した", "実現した"]),
    ("fell through", "失敗に終わった・実現しなかった", "句動詞", "The agreement fell through at the last minute.", "その合意は土壇場で成立しなかった。", ["成立した", "燃え尽きた", "餌にした"]),
    ("ate up", "大量に消費した・使い尽くした", "句動詞", "Unexpected repairs ate up most of our budget.", "予想外の修理が予算の大半を使い果たした。", ["節約した", "失敗に終わった", "餌にした"]),
    ("birth order", "出生順位・きょうだいの中で生まれた順番", "名詞", "Researchers examined whether birth order affects personality.", "研究者たちは出生順位が性格に影響するかを調べた。", ["出生率", "平均寿命", "家系図"]),
    ("stereotype", "固定観念・紋切り型のイメージ", "名詞", "The study challenges the stereotype that firstborn children are always more responsible.", "その研究は、第一子は常により責任感が強いという固定観念に異議を唱えている。", ["科学的証明", "個人差", "実物模型"]),
    ("virtual reconstruction", "仮想復元・デジタル復元", "名詞", "A virtual reconstruction shows how the ancient palace may have looked.", "仮想復元は、古代の宮殿がどのような姿だった可能性があるかを示している。", ["現地調査", "物理的解体", "口頭伝承"]),
    ("sovereign", "主権を有する・独立した／君主・主権者", "形容詞・名詞", "A sovereign nation has authority over its own territory.", "主権国家は自国の領土に対する統治権を持つ。", ["従属した", "一時的な", "地方の"]),
    ("irrigation canal", "灌漑用水路", "名詞", "The irrigation canal carried river water to distant fields.", "その灌漑用水路は川の水を遠くの畑へ運んだ。", ["城壁", "地下墓地", "交易路"]),
    ("cuneiform", "楔形文字", "名詞", "The clay tablet was covered with cuneiform.", "その粘土板は楔形文字で覆われていた。", ["象形文字", "音声記号", "暗号文"]),
    ("genetic manipulation", "遺伝子操作", "名詞", "Genetic manipulation could alter traits inherited by future generations.", "遺伝子操作は将来世代が受け継ぐ形質を変える可能性がある。", ["自然淘汰", "行動観察", "環境保全"]),
    ("animal uplift", "動物の知能・能力を人為的に向上させること", "名詞", "Animal uplift raises difficult questions about rights and responsibility.", "動物の能力向上は、権利と責任について難しい問題を提起する。", ["動物保護区", "家畜化", "種の絶滅"]),
]


def slugify(word: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", word.casefold()).strip("_")
    if not slug:
        raise ValueError(f"Cannot create an audio slug for {word!r}")
    return slug


def build_vocabulary() -> list[dict[str, object]]:
    vocabulary: list[dict[str, object]] = []
    for index, (word, meaning, pos, example, example_ja, distractors) in enumerate(
        VOCAB_ROWS, start=1
    ):
        vocabulary.append(
            {
                "word": word,
                "meaning": meaning,
                "pos": pos,
                "level": "準1級",
                "example": example,
                "distractors": distractors,
                "wordAudio": f"audio/vocab/w_{index:03d}_{slugify(word)}.mp3",
                "exampleJa": example_ja,
            }
        )
    return vocabulary


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Base data does not exist: {DATA_PATH}. Run gen_pre1_2026-1.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    data["vocabulary"] = build_vocabulary()

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"Installed {len(data['vocabulary'])} vocabulary items in {DATA_PATH}")


if __name__ == "__main__":
    main()
