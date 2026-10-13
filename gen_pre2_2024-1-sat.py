"""Build ReadPass data for EIKEN Grade Pre-2 2024-1 Saturday sub-venue."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "data" / "grade-pre2" / "2024-1-sat" / "data.json"
OFFICIAL_ANSWERS = [
    4, 1, 1, 1, 1, 3, 1, 1, 1, 3,
    1, 2, 3, 4, 1, 4, 3, 4, 3, 2,
    1, 4, 1, 2, 2, 1, 4, 2, 3,
]


def _analyses(number: int, answer: int, explanations: list[str]) -> list[str]:
    if len(explanations) != 4:
        raise ValueError("Every question needs four choice explanations")
    if number <= 15:
        return [
            ("✅ " if index == answer else "❌ ") + explanation
            for index, explanation in enumerate(explanations, start=1)
        ]

    analyses = []
    for index, explanation in enumerate(explanations, start=1):
        if index == answer:
            head, separator, detail = explanation.partition("。")
            explanation = f"{head}→正解。💡{detail}" if separator else f"{explanation}→正解。💡"
        analyses.append(explanation)
    return analyses


def question(
    number: int,
    text: str,
    translation: str,
    choices: list[str],
    choice_translations: list[str],
    answer: int,
    explanations: list[str],
    grammar: str,
) -> dict:
    if len(choices) != 4 or len(choice_translations) != 4:
        raise ValueError(f"Question {number} must have four choices")
    return {
        "number": number,
        "text": text,
        "translation": translation,
        "choices": choices,
        "choiceTranslations": choice_translations,
        "answer": answer,
        "choiceAnalysis": _analyses(number, answer, explanations),
        "grammar": grammar,
    }


def passage_question(
    number: int,
    prompt: str | None,
    prompt_translation: str | None,
    choices: list[str],
    choice_translations: list[str],
    answer: int,
    explanations: list[str],
    grammar: str,
) -> dict:
    item = {
        "number": number,
        "choices": choices,
        "choiceTranslations": choice_translations,
        "answer": answer,
        "choiceAnalysis": _analyses(number, answer, explanations),
        "grammar": grammar,
    }
    if prompt is not None:
        item = {
            "number": number,
            "question": prompt,
            "questionTranslation": prompt_translation,
            **{key: value for key, value in item.items() if key != "number"},
        }
    return item


def audio_slug(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", word.lower()).strip("_")


def vocab(
    index: int,
    word: str,
    meaning: str,
    pos: str,
    example: str,
    distractors: list[str],
) -> dict:
    if len(distractors) != 3:
        raise ValueError(f"Vocabulary {index} must have three distractors")
    return {
        "word": word,
        "meaning": meaning,
        "pos": pos,
        "level": "準2級",
        "example": example,
        "distractors": distractors,
        "wordAudio": f"audio/vocab/w_{index:03d}_{audio_slug(word)}.mp3",
    }


def build_sections() -> list[dict]:
    part1 = [
        question(
            1,
            "A : I can't decide what kind of job to do in the future.\nB : You should talk to Ms. Simpson. She knows a lot about careers. I'm sure she can give you some good ( 1 ).",
            "A：将来どんな仕事をすればよいか決められません。\nB：シンプソン先生に相談するといいですよ。先生は職業についてよく知っています。きっとよい（1）をくれるでしょう。",
            ["emotion", "style", "nature", "advice"],
            ["感情", "様式・スタイル", "自然・性質", "助言"],
            4,
            [
                "emotionは『感情』。give someone emotionとは通常言わない",
                "styleは『様式・スタイル』。進路相談でもらうものとして不自然",
                "natureは『自然・性質』。give some natureとは言わない",
                "adviceは『助言』。give 人 some good adviceで『人によい助言をする』となる",
            ],
            "💡 adviceは数えられない名詞。give + 人 + advice＝人に助言する。career＝職業・経歴。",
        ),
        question(
            2,
            "Money is a ( 2 ) problem for Bob. He never seems to have enough to buy books for his college classes, and he is always asking his parents to lend him some.",
            "お金はボブにとって（2）問題です。大学の授業用の本を買うお金がいつも足りないようで、両親に貸してほしいといつも頼んでいます。",
            ["constant", "jealous", "smooth", "remote"],
            ["絶え間ない", "嫉妬深い", "なめらかな", "遠く離れた"],
            1,
            [
                "constantは『絶え間ない』。never enoughとalways askingが繰り返す問題を示す",
                "jealousは『嫉妬深い』。problemの継続性を表せない",
                "smoothは『なめらかな・順調な』。お金の問題の説明に合わない",
                "remoteは『遠く離れた』。金銭問題を修飾する語として不自然",
            ],
            "💡 constant problem＝絶えず続く問題。neverとalwaysが継続を判断する手がかり。",
        ),
        question(
            3,
            "A : Excuse me. I don't like sitting by the window. Would you ( 3 ) seats with me?\nB : Sure. I prefer to sit in the window seat.",
            "A：すみません。窓際に座るのが好きではありません。私と席を（3）していただけますか。\nB：もちろんです。私は窓側の席の方が好きです。",
            ["switch", "dump", "quote", "wonder"],
            ["交換する", "捨てる", "引用する", "不思議に思う"],
            1,
            [
                "switchは『交換する』。switch seats with 人で『人と席を替わる』",
                "dumpは『捨てる』。席を替わる依頼には使えない",
                "quoteは『引用する』。seatsを目的語に取る意味ではない",
                "wonderは『不思議に思う』。Would you wonder seatsとは言わない",
            ],
            "💡 switch seats with + 人＝人と席を交換する（席を替わる）。交換するのでseatsと複数形になる点に注意。Would you ...?は丁寧な依頼。",
        ),
        question(
            4,
            "A : Have you chosen a topic for your ( 4 ) yet, Andy?\nB : Yes, Ms. Brown. I'm going to talk about airplanes. I found a great book about them in the school library.",
            "A：アンディ、もう（4）のテーマは選びましたか。\nB：はい、ブラウン先生。飛行機について話すつもりです。学校の図書館でよい本を見つけました。",
            ["presentation", "destination", "invitation", "association"],
            ["発表", "目的地", "招待", "協会・関連"],
            1,
            [
                "presentationは『発表』。topicを選び、about airplanesを話す文脈に合う",
                "destinationは『目的地』。話すテーマを選ぶ活動ではない",
                "invitationは『招待』。topic for an invitationとは通常言わない",
                "associationは『協会・関連』。学校での発表場面に合わない",
            ],
            "💡 choose a topic for a presentation＝発表のテーマを選ぶ。be going to talk about＝～について話す予定。",
        ),
        question(
            5,
            "A : How would you ( 5 ) your mother?\nB : She's tall and has brown hair and brown eyes. Also, she's very kind.",
            "A：あなたのお母さんをどのように（5）しますか。\nB：背が高く、茶色の髪と目をしています。それに、とても親切です。",
            ["describe", "calculate", "access", "possess"],
            ["描写する", "計算する", "利用する", "所有する"],
            1,
            [
                "describeは『描写する』。外見と性格を説明する返答に合う",
                "calculateは『計算する』。人の特徴を述べる意味ではない",
                "accessは『利用する・接続する』。人を説明する文脈に合わない",
                "possessは『所有する』。How would you possess 人とは言わない",
            ],
            "💡 describe + 人＝人の特徴を説明する。How would you describe ...?＝～をどのように表しますか。",
        ),
        question(
            6,
            "Mr. Baker always writes ( 6 ) on his students' homework. He tells them what they did well and how they could do better.",
            "ベーカー先生はいつも生徒の宿題に（6）を書きます。よくできた点と、どうすればもっとよくなるかを伝えます。",
            ["accents", "gestures", "comments", "purchases"],
            ["アクセント", "身ぶり", "コメント", "購入品"],
            3,
            [
                "accentsは『アクセント』。宿題への評価を書き込むものではない",
                "gesturesは『身ぶり』。write gesturesとは言わない",
                "commentsは『コメント』。よい点と改善点を書いて伝える説明に合う",
                "purchasesは『購入品』。宿題に書く内容ではない",
            ],
            "💡 write comments on ...＝～にコメントを書く。what they did wellは間接疑問の語順。",
        ),
        question(
            7,
            "Apples are ( 7 ) water. In fact, water makes up about 86 percent of an ordinary apple.",
            "リンゴは（7）水でできています。実際、普通のリンゴの約86パーセントを水が占めます。",
            ["mainly", "safely", "lastly", "slightly"],
            ["主に", "安全に", "最後に", "わずかに"],
            1,
            [
                "mainlyは『主に』。水が86パーセントという説明に合う",
                "safelyは『安全に』。構成物を表すare safely waterとは言わない",
                "lastlyは『最後に』。列挙の順序を示す副詞",
                "slightlyは『わずかに』。86パーセントという大部分と矛盾する",
            ],
            "💡 mainly＝主に。make up ... percent of ～＝～の…パーセントを占める。",
        ),
        question(
            8,
            "A : Did you learn anything at the doctor's today?\nB : Well, he ( 8 ) my shoulder, but nothing unusual showed up. He suggested getting another test if the pain continues.",
            "A：今日、医者で何かわかりましたか。\nB：ええと、先生は私の肩を（8）しましたが、異常は見つかりませんでした。痛みが続くなら別の検査を受けるよう勧めました。",
            ["examined", "jumped", "held", "heard"],
            ["診察した", "跳んだ", "持った", "聞いた"],
            1,
            [
                "examinedは『診察した』。医師が肩を調べる場面に合う",
                "jumpedは『跳んだ』。shoulderを目的語に取れない",
                "heldは『持った』。検査結果の説明につながらない",
                "heardは『聞いた』。hear my shoulderとは言わない",
            ],
            "💡 examine + 身体部位＝身体の部位を診察する。suggest doing＝～することを勧める。",
        ),
        question(
            9,
            "There is a tall hill behind John's house that blocks the wind. He has nothing to ( 9 ) during storms because it protects the house from any bad weather.",
            "ジョンの家の後ろには風を遮る高い丘があります。その丘が家を悪天候から守るので、嵐の間も（9）ことは何もありません。",
            ["fear", "serve", "waste", "check"],
            ["恐れる", "仕える・出す", "無駄にする", "確認する"],
            1,
            [
                "fearは『恐れる』。丘が家を守るため怖がるものがないという因果に合う",
                "serveは『仕える・提供する』。nothing to serveでは文意が通らない",
                "wasteは『無駄にする』。嵐の危険についての説明と合わない",
                "checkは『確認する』。丘が守ることとの因果がない",
            ],
            "💡 have nothing to fear＝何も恐れるものがない。that blocks the windはhillを説明する関係代名詞節。",
        ),
        question(
            10,
            "Kevin wants to become an engineer. To do that, he needs to go to university and get a ( 10 ) in engineering.",
            "ケビンは技術者になりたいと思っています。そのためには大学へ行き、工学の（10）を取得する必要があります。",
            ["contact", "salary", "degree", "factor"],
            ["連絡・接触", "給料", "学位", "要因"],
            3,
            [
                "contactは『連絡・接触』。大学で取得する資格ではない",
                "salaryは『給料』。go to university and get a salaryという流れではない",
                "degreeは『学位』。get a degree in engineeringで『工学の学位を取る』",
                "factorは『要因』。取得する学位の意味にならない",
            ],
            "💡 get a degree in + 分野＝～分野の学位を取得する。To do that＝そうするためには（目的を表す不定詞。thatは前文のbecome an engineerを指す）。",
        ),
        question(
            11,
            "A : Thank you for inviting us to your party, Bob.\nB : No problem. Please ( 11 ) to drinks over there.",
            "A：パーティーに招いてくれてありがとう、ボブ。\nB：どういたしまして。あちらの飲み物を（11）ください。",
            ["help yourself", "give way", "leave it", "catch up"],
            ["自由に取る", "道を譲る", "そのままにする", "追いつく"],
            1,
            [
                "help yourselfは『自由に取る』。help yourself to food/drinksの定型表現",
                "give wayは『道を譲る』。to drinksと組み合わせない",
                "leave itは『そのままにする』。飲み物を勧める発言にならない",
                "catch upは『追いつく』。to drinksとはつながらない",
            ],
            "💡 help yourself to ...＝～を自由に取ってください。もてなしの場面で使う。",
        ),
        question(
            12,
            "A : Coach, I hurt my foot while I was practicing for the race.\nB : I see. Well, you shouldn't run anymore. ( 12 ) over there, and I'll have a look at it in a few minutes.",
            "A：コーチ、レースの練習中に足を痛めました。\nB：わかりました。もう走らない方がいいですね。あそこで（12）ください。数分後に診ます。",
            ["Ask a favor", "Take a rest", "Play a part", "Make a change"],
            ["頼み事をする", "休憩する", "役割を果たす", "変更する"],
            2,
            [
                "Ask a favorは『頼み事をする』。けがへの指示として不自然",
                "Take a restは『休憩する』。足を痛め、走らないよう言われた場面に合う",
                "Play a partは『役割を果たす』。治療までの行動ではない",
                "Make a changeは『変更する』。over thereと結びつく具体的行動にならない",
            ],
            "💡 take a rest＝休む。while + 主語 + was doing＝～している間に。have a look at＝～を見る。",
        ),
        question(
            13,
            "Jack likes to play basketball with his friends every weekend. ( 13 ) his sister, she likes to spend her time reading books.",
            "ジャックは毎週末、友達とバスケットボールをするのが好きです。（13）彼の姉（妹）は、読書をして時間を過ごすのが好きです。",
            ["Right by", "Up to", "As for", "Because of"],
            ["すぐそばに", "～次第で", "～について言えば", "～のために"],
            3,
            [
                "Right byは『すぐそばに』。話題を対比して導く働きはない",
                "Up toは『～次第で・～まで』。his sisterを話題として提示できない",
                "As forは『～について言えば』。ジャックから姉（妹）へ話題を移す表現",
                "Because ofは『～のために』。後半は理由ではなく対比",
            ],
            "💡 As for + 名詞＝～について言えば。話題を切り替えるときに使い、ここではジャックと姉（妹）の過ごし方を対比している。",
        ),
        question(
            14,
            "In the village where Alice lives, there are very few trains or buses, so most people use cars or bicycles to ( 14 ).",
            "アリスが住む村では電車やバスがほとんどないので、ほとんどの人は（14）ために車や自転車を使います。",
            ["show up", "hang on", "reach out", "get around"],
            ["姿を見せる", "つかまる・待つ", "手を差し伸べる", "移動する"],
            4,
            [
                "show upは『現れる』。交通手段を使う目的として不自然",
                "hang onは『つかまる・待つ』。村内の移動を表さない",
                "reach outは『手を差し伸べる』。cars or bicyclesの用途ではない",
                "get aroundは『あちこち移動する』。公共交通が少ないため車や自転車を使う文脈に合う",
            ],
            "💡 get around＝移動する。where Alice livesはvillageを説明する関係副詞節。",
        ),
        question(
            15,
            "A : I'd like to join the tennis club, Coach Wilson, but I'm not a very good tennis player.\nB : No problem! It ( 15 ) whether you're good at tennis or not. Everyone is welcome to join.",
            "A：ウィルソンコーチ、テニスクラブに入りたいのですが、あまり上手ではありません。\nB：問題ありません。テニスが上手かどうかは（15）。誰でも参加できます。",
            ["makes no difference", "has no choice", "sees no point", "waits a moment"],
            ["違いはない・問題ではない", "選択の余地がない", "意味がないと思う", "少し待つ"],
            1,
            [
                "makes no differenceは『問題ではない』。Everyone is welcomeという結論に合う",
                "has no choiceは『選択の余地がない』。whether節の内容を受ける意味ではない",
                "sees no pointは『意味がないと思う』。主語Itでは人の判断を表しにくい",
                "waits a momentは『少し待つ』。上手さと参加条件の説明にならない",
            ],
            "💡 It makes no difference whether A or not＝Aかどうかは問題ではない。whetherは名詞節を作る。",
        ),
    ]

    shared_bicycle_dialogue = (
        "A : Welcome to George's Bicycles, ma'am. How can I help you?\n"
        "B : I'm looking for a new bicycle for my grandson. It's his 10th birthday next month.\n"
        "A : Do you know what kind of bicycle he would like?\n"
        "B : His mother says that he really ( 19 ).\n"
        "A : There are many in the store for you to choose from.\n"
        "B : Do you have any red ones? His favorite color is red.\n"
        "A : Sure. Can you tell me ( 20 )?\n"
        "B : Well, I'm not sure, but he's 135 centimeters tall."
    )
    shared_bicycle_translation = (
        "A：ジョージ自転車店へようこそ。どのようなご用件でしょうか。\n"
        "B：孫のための新しい自転車を探しています。来月10歳の誕生日なのです。\n"
        "A：お孫さんがどのような自転車を欲しがっているかわかりますか。\n"
        "B：母親によると、本人は本当に（19）そうです。\n"
        "A：店内にはたくさんありますので、お選びいただけます。\n"
        "B：赤いものはありますか。あの子の好きな色は赤です。\n"
        "A：もちろんです。（20）教えていただけますか。\n"
        "B：はっきりとはわかりませんが、身長は135センチです。"
    )

    part2 = [
        question(
            16,
            "A : What are you ( 16 ), Scarlett?\nB : I've got my swimsuit, a large towel, my sunglasses, and a book.\nA : We should buy some sandwiches and drinks on the way.\nB : Yeah. It will be fun to have a picnic on the sand.",
            "A：スカーレット、何を（16）のですか。\nB：水着、大きなタオル、サングラス、それに本を持っています。\nA：途中でサンドイッチと飲み物を買いましょう。\nB：うん。砂浜でピクニックをするのは楽しそうです。",
            [
                "looking for in that closet",
                "getting for Mom's birthday",
                "wearing at tonight's dinner party",
                "taking with you to the beach",
            ],
            [
                "あのクローゼットで探している",
                "母の誕生日用に用意している",
                "今夜の夕食会で着る",
                "海辺へ持っていく",
            ],
            4,
            [
                "クローゼットで探しているなら、すでに持っている物の列挙と合わない",
                "母の誕生日用品ではなく、水着やタオルなど海辺の持ち物を挙げている",
                "夕食会で水着や大きなタオルを身につけるのは不自然",
                "海辺へ持っていく物。swimsuit、towel、picnic on the sandが決め手",
            ],
            "💡 take A with you to B＝AをBへ持っていく。on the way＝途中で。",
        ),
        question(
            17,
            "A : Good morning. I ( 17 ) in your store's window display.\nB : Have you ever done anything similar before?\nA : Yes. I used to help at my parent's grocery store when I was a high school student.\nB : Great. Please complete this form, and I'll get the manager.",
            "A：おはようございます。お店のショーウィンドウで（17）。\nB：以前に似たようなことをした経験はありますか。\nA：はい。高校生のとき、親の食料品店を手伝っていました。\nB：わかりました。この用紙に記入してください。店長を呼んできます。",
            [
                "want to put this poster",
                "would like to buy the puppy",
                "saw the job advertisement",
                "noticed a large crack",
            ],
            [
                "このポスターを貼りたい",
                "その子犬を買いたい",
                "求人広告を見た",
                "大きなひびを見つけた",
            ],
            3,
            [
                "ポスターを貼る許可を求めるなら、仕事の経験を聞かれたり、用紙への記入を求められたりする流れにならない",
                "子犬を買いに来たのなら、仕事の経験を聞かれたり、用紙に記入して店長を待つように言われたりする流れにならない",
                "求人広告を見た。過去の経験、申込用紙、店長を呼ぶ流れが就職応募を示す",
                "ひびの報告なら、過去の仕事経験を尋ねる必要がない",
            ],
            "💡 job advertisement＝求人広告。used to + 動詞＝以前は～したものだった。Have you ever done ...?＝経験。",
        ),
        question(
            18,
            "A : Did you have a nice weekend, Bianca?\nB : I ( 18 ).\nA : Oh no! I hope you get well soon.\nB : It's not so bad, and I still won a prize.",
            "A：よい週末を過ごしましたか、ビアンカ。\nB：私は（18）。\nA：まあ大変。早くよくなるといいですね。\nB：それほどひどくないですし、それでも賞を取りました。",
            [
                "got first place in a photo contest",
                "burned my hand while making dinner",
                "slipped on the street and hit my head",
                "hurt my knee in a dance competition",
            ],
            [
                "写真コンテストで1位になった",
                "夕食を作っているときに手をやけどした",
                "通りで滑って頭を打った",
                "ダンス大会で膝を痛めた",
            ],
            4,
            [
                "1位になっただけならget well soonと言われる理由がなく、still won a prize（それでも賞を取った）の『それでも』にもつながらない",
                "やけどならけがには合うが、賞を取ったという後続文につながらない",
                "転倒ならけがには合うが、大会で賞を取ったという情報と結びつかない",
                "ダンス大会で膝を痛めた。けがと受賞の両方を同時に説明できる",
            ],
            "💡 hurt one's knee＝膝を痛める。still＝それでも。get well soon＝早くよくなる。",
        ),
        question(
            19,
            shared_bicycle_dialogue,
            shared_bicycle_translation,
            [
                "looks after his bike",
                "needs it to get to work",
                "wants a mountain bike",
                "hopes to sell it soon",
            ],
            [
                "自転車の世話をする",
                "仕事へ行くために必要としている",
                "マウンテンバイクを欲しがっている",
                "すぐに売りたいと思っている",
            ],
            3,
            [
                "自転車を大切に扱っているという内容は、どんな自転車が欲しいかという質問の答えにならない",
                "孫は10歳で、通勤用という説明は不自然",
                "マウンテンバイクを欲しがっている。直後のmanyから種類を選ぶ流れに合う",
                "新しい自転車を買う場面なので、売りたいという意味は逆",
            ],
            "💡 want + 名詞＝～が欲しい。what kind of bicycle he would likeは間接疑問文。",
        ),
        question(
            20,
            shared_bicycle_dialogue,
            shared_bicycle_translation,
            [
                "how much you want to spend",
                "what size he needs",
                "where it should be delivered",
                "when you want it",
            ],
            [
                "いくら使いたいか",
                "彼にどのサイズが必要か",
                "どこへ配達すべきか",
                "いつ欲しいか",
            ],
            2,
            [
                "返答は予算ではなく身長なので、金額の質問ではない",
                "必要なサイズ。135 centimeters tallという返答から体格に合うサイズを尋ねている",
                "配達先を尋ねたなら住所が答えになるはず",
                "時期を尋ねたなら日付や時間が答えになるはず",
            ],
            "💡 Can you tell me + 間接疑問文。what size he needsは疑問詞の後が平叙文語順。",
        ),
    ]

    maria_paragraphs = [
        "Maria loves baking with her grandmother. Maria's grandmother heard about a local baking contest. She asked Maria to take part in the contest with her. Maria was very happy. On the day of the contest, Maria and her grandmother were both really excited. They started getting ready early. They put flour, eggs, chocolate chips, and other things in a basket. They were planning to make their favorite chocolate chip cookies. However, when they got to the contest, they discovered that they had ( 21 ). They hoped that the chocolate chips would make the cookies sweet enough, so they made them anyway.",
        "To their surprise, they won third prize. The judges said that they really liked the cookies because they were not too sweet. Maria and her grandmother were so happy. Afterward, they ( 22 ) with the other people there. Everyone liked the taste of the cookies that Maria and her grandmother had made.",
    ]
    maria_translations = [
        "マリアは祖母と一緒にお菓子を焼くのが大好きです。祖母は地元のお菓子作りコンテストについて聞き、マリアに一緒に参加してほしいと頼みました。マリアはとても喜びました。コンテスト当日、二人はとてもわくわくして、早くから準備を始めました。小麦粉、卵、チョコレートチップなどをかごに入れ、大好きなチョコチップクッキーを作る予定でした。しかし会場に着くと、（21）ことに気づきました。チョコレートチップだけでも十分甘くなることを願い、そのまま作りました。",
        "驚いたことに、二人は3位に入りました。審査員は、甘すぎなかったのでクッキーがとても気に入ったと言いました。マリアと祖母は大喜びでした。その後、会場にいたほかの人たちと（22）。みんな、二人が作ったクッキーの味を気に入りました。",
    ]
    maria_pairs = [
        ["Maria loves baking with her grandmother.", "マリアは祖母と一緒にお菓子を焼くのが大好きです。"],
        ["Maria's grandmother heard about a local baking contest.", "祖母は地元のお菓子作りコンテストについて聞きました。"],
        ["She asked Maria to take part in the contest with her.", "祖母はマリアに、一緒にコンテストに参加してほしいと頼みました。"],
        ["Maria was very happy.", "マリアはとても喜びました。"],
        ["On the day of the contest, Maria and her grandmother were both really excited.", "コンテスト当日、マリアと祖母は二人ともとてもわくわくしていました。"],
        ["They started getting ready early.", "二人は早くから準備を始めました。"],
        ["They put flour, eggs, chocolate chips, and other things in a basket.", "二人は小麦粉、卵、チョコレートチップなどをかごに入れました。"],
        ["They were planning to make their favorite chocolate chip cookies.", "二人は大好きなチョコチップクッキーを作る予定でした。"],
        ["However, when they got to the contest, they discovered that they had ( 21 ).", "しかし会場に着くと、二人は（21）ことに気づきました。"],
        ["They hoped that the chocolate chips would make the cookies sweet enough, so they made them anyway.", "チョコレートチップで十分甘くなることを願い、そのままクッキーを作りました。"],
        ["To their surprise, they won third prize.", "驚いたことに、二人は3位に入りました。"],
        ["The judges said that they really liked the cookies because they were not too sweet.", "審査員は、甘すぎなかったのでクッキーがとても気に入ったと言いました。"],
        ["Maria and her grandmother were so happy.", "マリアと祖母は大喜びしました。"],
        ["Afterward, they ( 22 ) with the other people there.", "その後、二人は会場のほかの人たちと（22）。"],
        ["Everyone liked the taste of the cookies that Maria and her grandmother had made.", "みんな、マリアと祖母が作ったクッキーの味を気に入りました。"],
    ]
    part3 = {
        "name": "大問3",
        "nameEn": "Part 3",
        "type": "passage-fill",
        "instruction": "次の英文を読み，その文意にそって(21)と(22)の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
        "passages": [
            {
                "label": "",
                "title": "Maria's Baking Adventure",
                "paragraphs": maria_paragraphs,
                "translations": maria_translations,
                "sentencePairs": maria_pairs,
                "questions": [
                    passage_question(
                        21,
                        None,
                        None,
                        [
                            "forgotten to bring sugar",
                            "just ten minutes to prepare",
                            "to make a cake as well",
                            "gone to the wrong place",
                        ],
                        [
                            "砂糖を持ってくるのを忘れた",
                            "準備時間が10分しかなかった",
                            "ケーキも作ることになっていた",
                            "間違った場所へ行ってしまった",
                        ],
                        1,
                        [
                            "砂糖を忘れた。直後の文でチョコレートチップだけで十分甘くなることを願っているので、砂糖がなかったとわかる",
                            "準備時間が短いなら、sweet enoughという甘さの問題につながらない",
                            "ケーキも作る予定なら、砂糖の代わりを心配する説明にならない",
                            "場所を間違えたなら、そのまま会場でクッキーを作る展開と矛盾する",
                        ],
                        "💡 forget to do＝～するのを忘れる。had forgottenは会場到着より前の出来事を示す過去完了。",
                    ),
                    passage_question(
                        22,
                        None,
                        None,
                        ["bought some drinks", "cleaned the tables", "took many photos", "shared the cookies"],
                        ["飲み物を買った", "テーブルを片付けた", "たくさん写真を撮った", "クッキーを分け合った"],
                        4,
                        [
                            "飲み物を買ったこととEveryone liked the tasteは結びつかない",
                            "テーブルを片付けただけでは、ほかの人がクッキーを味わえない",
                            "写真を撮ったことはクッキーの味への評価につながらない",
                            "クッキーを分け合った。直後のEveryone liked the tasteが直接の根拠",
                        ],
                        "💡 share A with B＝AをBと分け合う。Afterward＝その後。",
                    ),
                ],
            }
        ],
    }

    email_paragraphs = [
        "Hi Jenny, I hope you're having a good week. Last Saturday, I went to a market in my neighborhood, and it was amazing! I bought some records from the 1960s and 1970s. They sound great on my dad's old record player. Also, I got a couple of comic books. One of them is from the series that you were telling me about when I visited your house. I thought of you when I found them because I know how much you love comic books.",
        "There's going to be another market next weekend in a different part of the city. I've heard it will be even bigger than the one last Saturday. There might be more records, comic books, and other interesting stuff to look at and buy. How about we go together and see what we can find? I think we'd have fun searching through the items, even if they're too expensive for us to buy.",
        "Are you free next Saturday? The market is a little far away, but I asked my dad, and he said he would drive us there. We can go to a café for lunch and then take a bus back in the afternoon. Let me know what you think. Best wishes, Steve",
    ]
    email_translations = [
        "ジェニーへ。元気に過ごしているといいな。先週の土曜日、近所のマーケットへ行ったんだけど、すばらしかったよ。1960年代と1970年代のレコードを何枚か買った。父の古いレコードプレーヤーで聴くと、とてもよい音なんだ。それから、漫画本も2冊買った。そのうち1冊は、前に君の家を訪ねたときに話してくれたシリーズのものだよ。君が漫画本をとても好きだと知っているから、それを見つけたとき君のことを思い出した。",
        "来週末、市内の別の場所でもマーケットが開かれる予定だ。先週土曜日のものよりさらに大きいらしい。レコードや漫画本など、見たり買ったりできる面白い物がもっとあるかもしれない。一緒に行って何が見つかるか見てみない？ たとえ高すぎて買えなくても、品物を探して回るだけで楽しめると思う。",
        "次の土曜日は空いている？ マーケットは少し遠いけれど、父に頼んだら車で連れていってくれると言ってくれた。昼食はカフェで食べて、午後はバスで帰れるよ。どう思うか知らせてね。ではまた。スティーブ",
    ]
    email_pairs = [
        ["I hope you're having a good week.", "よい1週間を過ごしているといいなと思います。"],
        ["Last Saturday, I went to a market in my neighborhood, and it was amazing!", "先週の土曜日、近所のマーケットへ行きましたが、すばらしい場所でした。"],
        ["I bought some records from the 1960s and 1970s.", "1960年代と1970年代のレコードを何枚か買いました。"],
        ["They sound great on my dad's old record player.", "父の古いレコードプレーヤーで聴くと、とてもよい音がします。"],
        ["Also, I got a couple of comic books.", "それから、漫画本も2冊買いました。"],
        ["One of them is from the series that you were telling me about when I visited your house.", "そのうち1冊は、以前あなたの家を訪ねたときに話してくれたシリーズのものです。"],
        ["I thought of you when I found them because I know how much you love comic books.", "あなたが漫画本をとても好きだと知っているので、それを見つけたときあなたのことを思い出しました。"],
        ["There's going to be another market next weekend in a different part of the city.", "来週末、市内の別の場所で別のマーケットが開かれる予定です。"],
        ["I've heard it will be even bigger than the one last Saturday.", "先週土曜日のものよりさらに大きいと聞いています。"],
        ["There might be more records, comic books, and other interesting stuff to look at and buy.", "レコードや漫画本など、見たり買ったりできるおもしろい物がもっとあるかもしれません。"],
        ["How about we go together and see what we can find?", "一緒に行って何が見つかるか見てみませんか。"],
        ["I think we'd have fun searching through the items, even if they're too expensive for us to buy.", "たとえ高すぎて買えなくても、品物を探して回るだけで楽しめると思います。"],
        ["Are you free next Saturday?", "次の土曜日は空いていますか。"],
        ["The market is a little far away, but I asked my dad, and he said he would drive us there.", "マーケットは少し遠いですが、父に頼むと車で連れていってくれると言いました。"],
        ["We can go to a café for lunch and then take a bus back in the afternoon.", "昼食はカフェで食べ、その後午後にバスで帰れます。"],
        ["Let me know what you think.", "どう思うか教えてください。"],
    ]

    gaudi_paragraphs = [
        "Antoni Gaudí was born in Spain and became famous as a designer of buildings. As a child, Gaudí was often in poor health. He had to rest at his family's house in the countryside instead of going to school. While he was there, he enjoyed looking at nature. He got many ideas for his designs for buildings from nature. He thought that using natural shapes and colors, such as those of leaves and seashells, could give buildings a special beauty.",
        "The Sagrada Família is a church in Barcelona that Gaudí designed. Although it is made from stone, glass, and metal, it looks like a picture of Gaudí's childhood memories. The towers of the Sagrada Família are like huge trees. Inside, the columns that support the roof make people feel like they are in a forest. Construction began in the late nineteenth century, but it has still not finished. Workers are using Gaudí's original designs to complete the building.",
        "Park Güell is another place that Gaudí designed. The park is not just an area with trees and grass for people to walk, rest, and play. It also has strange, colorful objects and unusual buildings. For example, there is a long bench that looks like a snake. Because of these things, visiting the park can be a fun experience. Interestingly, there is a tall, pink building in the park called the Casa Museu Gaudí, where Gaudí lived for many years.",
        "Even after Gaudí's death, his special approach to designing buildings is a source of ideas for designers around the world. Every year, many people visit Barcelona to see the Sagrada Família and the other buildings that Gaudí designed. These places have helped to make Barcelona famous as a center of art and design. Some of them are so important to the city that they have become UNESCO World Heritage Sites.",
    ]
    gaudi_translations = [
        "アントニ・ガウディはスペインで生まれ、建築物の設計者として有名になりました。子どものころは体が弱く、学校へ行く代わりに田舎にある家族の家で休まなければなりませんでした。そこで自然を見ることを楽しみ、建築デザインの多くの着想を自然から得ました。葉や貝殻のような自然の形や色を使えば、建物に特別な美しさを与えられると考えたのです。",
        "サグラダ・ファミリアは、ガウディが設計したバルセロナの教会です。石、ガラス、金属でできていますが、ガウディの子ども時代の記憶を描いた絵のように見えます。塔は巨大な木々のようで、内部では屋根を支える柱が、人々に森の中にいるような感覚を与えます。建設は19世紀後半に始まりましたが、まだ完成していません。作業員はガウディの元の設計図を使って建物を完成させようとしています。",
        "グエル公園もガウディが設計した場所です。木や芝生があり、人々が歩いたり休んだり遊んだりするだけの場所ではありません。奇妙で色鮮やかな物や珍しい建物もあります。例えば、ヘビのように見える長いベンチがあります。このため、公園を訪れることは楽しい体験になります。興味深いことに、公園にはガウディの家博物館と呼ばれる背の高いピンク色の建物があり、ガウディは長年そこに住んでいました。",
        "ガウディの死後も、建築設計への独特の取り組み方は世界中の設計者に着想を与えています。毎年、多くの人がサグラダ・ファミリアなどガウディが設計した建物を見るためにバルセロナを訪れます。これらの場所により、バルセロナは芸術とデザインの中心地として有名になりました。そのうちいくつかは市にとって非常に重要で、ユネスコ世界遺産になっています。",
    ]
    gaudi_pairs = [
        ["Antoni Gaudí was born in Spain and became famous as a designer of buildings.", "アントニ・ガウディはスペインで生まれ、建築物の設計者として有名になりました。"],
        ["As a child, Gaudí was often in poor health.", "子どものころ、ガウディはよく体調を崩していました。"],
        ["He had to rest at his family's house in the countryside instead of going to school.", "学校へ行く代わりに、田舎にある家族の家で休まなければなりませんでした。"],
        ["While he was there, he enjoyed looking at nature.", "そこにいる間、ガウディは自然を眺めることを楽しみました。"],
        ["He got many ideas for his designs for buildings from nature.", "建物の設計について多くの着想を自然から得ました。"],
        ["He thought that using natural shapes and colors, such as those of leaves and seashells, could give buildings a special beauty.", "葉や貝殻のような自然の形や色を使えば、建物に特別な美しさを与えられると考えました。"],
        ["The Sagrada Família is a church in Barcelona that Gaudí designed.", "サグラダ・ファミリアは、ガウディが設計したバルセロナの教会です。"],
        ["Although it is made from stone, glass, and metal, it looks like a picture of Gaudí's childhood memories.", "石、ガラス、金属でできていますが、ガウディの子ども時代の記憶を描いた絵のように見えます。"],
        ["The towers of the Sagrada Família are like huge trees.", "サグラダ・ファミリアの塔は、巨大な木々のようです。"],
        ["Inside, the columns that support the roof make people feel like they are in a forest.", "内部では屋根を支える柱が、人々に森の中にいるような感覚を与えます。"],
        ["Construction began in the late nineteenth century, but it has still not finished.", "建設は19世紀後半に始まりましたが、まだ完成していません。"],
        ["Workers are using Gaudí's original designs to complete the building.", "作業員はガウディの元の設計図を使って建物を完成させようとしています。"],
        ["Park Güell is another place that Gaudí designed.", "グエル公園もガウディが設計した場所です。"],
        ["The park is not just an area with trees and grass for people to walk, rest, and play.", "この公園は、人々が歩いたり休んだり遊んだりするための、木や芝生があるだけの場所ではありません。"],
        ["It also has strange, colorful objects and unusual buildings.", "奇妙で色鮮やかな物や、珍しい建物もあります。"],
        ["For example, there is a long bench that looks like a snake.", "例えば、ヘビのように見える長いベンチがあります。"],
        ["Because of these things, visiting the park can be a fun experience.", "こうしたものがあるので、公園を訪れるのは楽しい体験になります。"],
        ["Interestingly, there is a tall, pink building in the park called the Casa Museu Gaudí, where Gaudí lived for many years.", "興味深いことに、公園にはガウディの家博物館と呼ばれる背の高いピンク色の建物があり、ガウディは長年そこに住んでいました。"],
        ["Even after Gaudí's death, his special approach to designing buildings is a source of ideas for designers around the world.", "ガウディの死後も、建物の設計に対する彼の独特な取り組み方は、世界中の設計者にとって着想の源になっています。"],
        ["Every year, many people visit Barcelona to see the Sagrada Família and the other buildings that Gaudí designed.", "毎年、多くの人がサグラダ・ファミリアやガウディが設計したほかの建物を見るためにバルセロナを訪れます。"],
        ["These places have helped to make Barcelona famous as a center of art and design.", "これらの場所により、バルセロナは芸術とデザインの中心地として有名になりました。"],
        ["Some of them are so important to the city that they have become UNESCO World Heritage Sites.", "そのうちいくつかは市にとって非常に重要で、ユネスコ世界遺産になっています。"],
    ]

    part4 = {
        "name": "大問4",
        "nameEn": "Part 4",
        "type": "reading-comprehension",
        "instruction": "次の英文Ａ，Ｂの内容に関して，(23)から(29)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
        "passages": [
            {
                "label": "A",
                "title": "A question",
                "format": "email",
                "meta": {
                    "from": "Steve Potter <steve.musiclover@mailme.com>",
                    "to": "Jenny King <jennyk1234@zmail.com>",
                    "date": "June 1",
                    "subject": "A question",
                },
                "paragraphs": email_paragraphs,
                "translations": email_translations,
                "sentencePairs": email_pairs,
                "questions": [
                    passage_question(
                        23,
                        "What made Steve think of Jenny last Saturday?",
                        "先週土曜日、何がきっかけでスティーブはジェニーのことを思い出しましたか。",
                        [
                            "He bought a book from a series that she knew.",
                            "He saw a record player like her dad's old one.",
                            "He heard some music that he knew she liked.",
                            "He found a way for her to sell her records.",
                        ],
                        [
                            "彼女が知っているシリーズの本を買った。",
                            "彼女の父親の古いものに似たレコードプレーヤーを見た。",
                            "彼女が好きだと知っている音楽を聞いた。",
                            "彼女がレコードを売る方法を見つけた。",
                        ],
                        1,
                        [
                            "彼女が知っているシリーズの本を買った。Jennyが話していたシリーズの漫画本を見つけたことが、Jennyを思い出した直接の理由",
                            "古いレコードプレーヤーはSteveの父親のもので、Jennyの父親ではない",
                            "Jennyが好きなのはcomic booksで、音楽の好みについては書かれていない",
                            "Jennyがレコードを売る話はなく、一緒にマーケットへ行く提案をしている",
                        ],
                        "💡 One of themはa couple of comic booksの一冊を指す。that she knewはthe series that you were telling me aboutの言い換え。",
                    ),
                    passage_question(
                        24,
                        "What does Steve say about the market next weekend?",
                        "スティーブは来週末のマーケットについて何と言っていますか。",
                        [
                            "It will be held at the same place as the one he went to on Saturday.",
                            "He and Jenny might enjoy looking through the things that are for sale.",
                            "People can exchange records and comic books instead of buying them.",
                            "Most of the items there will probably be too expensive for him to buy.",
                        ],
                        [
                            "先週土曜日に行った場所と同じ所で開かれる。",
                            "スティーブとジェニーは売られている物を見て回って楽しめるかもしれない。",
                            "人々はレコードや漫画本を買う代わりに交換できる。",
                            "ほとんどの品物はおそらく彼には高すぎて買えない。",
                        ],
                        2,
                        [
                            "different part of the cityとあるため、同じ場所ではない",
                            "売り物を見て回るのを楽しめるかもしれない。we'd have fun searching through the itemsとあり、高くて買えなくても品物を探して見て回るだけで楽しいだろうと書かれている",
                            "交換できるとは書かれず、look at and buyとある",
                            "even if they're too expensiveは仮定で、ほとんどが高すぎるという断定ではない",
                        ],
                        "💡 search through the items＝品物を探して見て回る。even if＝たとえ～でも。",
                    ),
                    passage_question(
                        25,
                        "Steve says that his father",
                        "スティーブは父親について何と言っていますか。",
                        [
                            "will take a bus to work next Saturday.",
                            "has agreed to give Steve and Jenny a ride.",
                            "told him about a great café near the market.",
                            "gave him some items to sell at the market.",
                        ],
                        [
                            "次の土曜日にバスで仕事へ行く。",
                            "スティーブとジェニーを車で送ることに同意した。",
                            "マーケット近くのすばらしいカフェを教えた。",
                            "マーケットで売る品物をスティーブに渡した。",
                        ],
                        2,
                        [
                            "バスに乗るのはSteveたちが午後に帰るときで、父親の通勤ではない",
                            "二人を車で送ることに同意した。he said he would drive us thereの言い換え",
                            "カフェの提案はSteve自身で、父親から聞いたとは書かれていない",
                            "父親が売り物を渡した記述はない",
                        ],
                        "💡 give 人 a ride＝人を車に乗せて送る。he said he would drive us thereの言い換え。",
                    ),
                ],
            },
            {
                "label": "B",
                "title": "Antoni Gaudí",
                "paragraphs": gaudi_paragraphs,
                "translations": gaudi_translations,
                "sentencePairs": gaudi_pairs,
                "questions": [
                    passage_question(
                        26,
                        "Antoni Gaudí's experiences as a child",
                        "アントニ・ガウディの子ども時代の経験は、",
                        [
                            "gave him a lot of the ideas that he used in his work.",
                            "taught him to take special care of his health.",
                            "led him to get involved in protecting nature.",
                            "made him want to stay inside as much as possible.",
                        ],
                        [
                            "仕事で使った多くの着想を彼に与えた。",
                            "健康に特別な注意を払うことを教えた。",
                            "自然保護に関わるよう導いた。",
                            "できるだけ屋内にいたいと思わせた。",
                        ],
                        1,
                        [
                            "仕事で使った多くの着想を得た。子どものころ田舎で自然を見るのを楽しみ、その自然から建築デザインの多くの着想を得たと書かれている",
                            "体調を崩した経験は書かれるが、健康管理を学んだとは書かれていない",
                            "自然から着想を得たが、自然保護活動に関わったとは書かれていない",
                            "田舎で自然を見るのを楽しんでおり、屋内にいたいという意味ではない",
                        ],
                        "💡 get ideas from ...＝～から着想を得る。as a child＝子どものころ。",
                    ),
                    passage_question(
                        27,
                        "What is one thing that is true of the Sagrada Família?",
                        "サグラダ・ファミリアについて正しいことの一つは何ですか。",
                        [
                            "Workers have recently discovered the original designs.",
                            "The roof is supported by trees from a nearby forest.",
                            "Its design came from a picture drawn by one of Gaudí's children.",
                            "Construction of the building has not yet been completed.",
                        ],
                        [
                            "作業員が最近、元の設計図を発見した。",
                            "近くの森の木々が屋根を支えている。",
                            "ガウディの子どもの一人が描いた絵から設計が生まれた。",
                            "建物の建設はまだ完了していない。",
                        ],
                        4,
                        [
                            "作業員は元の設計図を使用しているが、最近発見したとは書かれていない",
                            "本文では屋根を支えるのはcolumns（柱）で、近くの森の木ではない。木のようだと述べられているのはtowers（塔）である",
                            "childhood memoriesの絵のように見えるが、子どもが描いた絵ではない",
                            "建設はまだ完了していない。Construction ... has still not finishedとあり、建設は今も終わっていない",
                        ],
                        "💡 has not yet been completed＝まだ完成していない。本文has still not finishedの受動態による言い換え。",
                    ),
                    passage_question(
                        28,
                        "What is special about Casa Museu Gaudí?",
                        "ガウディの家博物館について特別なことは何ですか。",
                        [
                            "It contains a park where people can see wild animals.",
                            "It used to be one of the houses where Gaudí lived.",
                            "It is full of the strange objects that Gaudí collected.",
                            "It was designed as a place for children to have fun.",
                        ],
                        [
                            "野生動物を見られる公園が中にある。",
                            "かつてガウディが住んだ家の一つだった。",
                            "ガウディが集めた奇妙な物でいっぱいである。",
                            "子どもが楽しむ場所として設計された。",
                        ],
                        2,
                        [
                            "建物は公園内にあるが、建物の中に野生動物の公園があるとは書かれていない",
                            "かつてガウディが住んでいた家の一つだった。where Gaudí lived for many yearsとあり、ガウディが長年住んでいた建物である",
                            "公園に奇妙な物があるが、Gaudíが収集し、建物内にあるとは書かれていない",
                            "公園は楽しい体験になるが、建物が子ども向けに設計されたとは書かれていない",
                        ],
                        "💡 used to be＝以前は～だった。where Gaudí livedはhousesを説明する関係副詞節。",
                    ),
                    passage_question(
                        29,
                        "What has been one effect of Gaudí's work?",
                        "ガウディの仕事がもたらした影響の一つは何ですか。",
                        [
                            "The number of visitors to Barcelona has decreased.",
                            "Designers have had to change the way that they do their work.",
                            "Barcelona has become well-known for art and design.",
                            "His ideas have been used in World Heritage Sites around the world.",
                        ],
                        [
                            "バルセロナへの訪問者数が減った。",
                            "設計者は仕事の進め方を変えざるを得なくなった。",
                            "バルセロナは芸術とデザインで有名になった。",
                            "彼の着想が世界各地の世界遺産で使われた。",
                        ],
                        3,
                        [
                            "毎年many people visitとあり、訪問者が減ったとは書かれていない",
                            "設計者への着想源だが、仕事の仕方を変えざるを得ないとは書かれていない",
                            "バルセロナが芸術とデザインで有名になった。helped to make Barcelona famous as a center of art and designの直接の言い換え",
                            "世界遺産になったのはバルセロナにあるガウディの建物の一部で、彼の着想が世界各地の世界遺産で使われたとは書かれていない",
                        ],
                        "💡 help to make A B＝AをBにするのに役立つ。become well-known forはbecome famous asの言い換え。",
                    ),
                ],
            },
        ],
    }

    return [
        {
            "name": "大問1",
            "nameEn": "Part 1",
            "type": "vocabulary",
            "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "questions": part1,
        },
        {
            "name": "大問2",
            "nameEn": "Part 2",
            "type": "vocabulary",
            "instruction": "次の四つの会話文を完成させるために，(16)から(20)に入るものとして最も適切なものを1，2，3，4の中から一つ選びなさい。",
            "questions": part2,
        },
        part3,
        part4,
    ]


def build_vocabulary() -> list[dict]:
    entries = [
        ("advice", "助言", "名詞", "My teacher gave me useful advice about my future.", ["感情", "様式", "自然"]),
        ("constant", "絶え間ない", "形容詞", "The constant noise made it hard to study.", ["嫉妬深い", "なめらかな", "遠く離れた"]),
        ("switch", "交換する・切り替える", "動詞", "Could we switch seats before the movie starts?", ["捨てる", "引用する", "不思議に思う"]),
        ("presentation", "発表", "名詞", "Aya gave a presentation about airplanes.", ["目的地", "招待", "協会"]),
        ("describe", "描写する・説明する", "動詞", "Please describe the person you saw.", ["計算する", "利用する", "所有する"]),
        ("comments", "コメント・意見", "名詞", "The teacher wrote helpful comments on my essay.", ["アクセント", "身ぶり", "購入品"]),
        ("mainly", "主に", "副詞", "This drink is made mainly from fruit.", ["安全に", "最後に", "わずかに"]),
        ("examine", "診察する・調べる", "動詞", "The doctor examined my throat and said it was a cold.", ["跳ぶ", "持つ", "聞く"]),
        ("fear", "恐れる", "動詞", "There is nothing to fear in this safe building.", ["仕える", "無駄にする", "確認する"]),
        ("degree", "学位", "名詞", "My aunt has a degree in music.", ["連絡", "給料", "要因"]),
        ("help yourself", "自由に取る", "句", "Please help yourself to some cake.", ["道を譲る", "そのままにする", "追いつく"]),
        ("take a rest", "休憩する", "句", "You should take a rest after the race.", ["頼み事をする", "役割を果たす", "変更する"]),
        ("as for", "～について言えば", "句", "As for me, I like summer better than winter.", ["すぐそばに", "～次第で", "～のために"]),
        ("get around", "移動する", "句動詞", "It is easy to get around Tokyo by train.", ["姿を見せる", "つかまる", "手を差し伸べる"]),
        ("make no difference", "違いはない・問題ではない", "句", "It makes no difference to me whether we go by bus or by train.", ["選択の余地がない", "意味がないと思う", "少し待つ"]),
        ("take with you", "持っていく", "句", "Don't forget to take an umbrella with you.", ["探す", "贈り物にする", "身につける"]),
        ("window display", "ショーウィンドウの展示", "名詞", "The shop put new winter coats in its window display.", ["申込用紙", "店長", "食料品店"]),
        ("job advertisement", "求人広告", "名詞", "Ken answered a job advertisement at a local store.", ["販売ポスター", "商品案内", "修理の連絡"]),
        ("get well", "元気になる・回復する", "句", "My grandmother got well after a week of rest.", ["賞を取る", "転ぶ", "料理をする"]),
        ("mountain bike", "マウンテンバイク", "名詞", "My brother rides his mountain bike in the hills every weekend.", ["通勤用バス", "配達車", "子ども用ヘルメット"]),
        ("bake", "焼く", "動詞", "My father bakes bread every Sunday morning.", ["煮る", "刻む", "凍らせる"]),
        ("take part in", "～に参加する", "句動詞", "More than 100 students took part in the speech contest.", ["～を延期する", "～を片付ける", "～を断る"]),
        ("flour", "小麦粉", "名詞", "Mix the flour and milk in a large bowl.", ["塩", "牛乳", "油"]),
        ("chocolate chip", "チョコレートチップ", "名詞", "She put chocolate chips in the cookie dough.", ["貝殻", "小麦粉", "彫刻"]),
        ("discover", "気づく・発見する", "動詞", "When I got home, I discovered that I had lost my key.", ["隠す", "届ける", "測る"]),
        ("sweet enough", "十分に甘い", "句", "This tea is sweet enough without sugar.", ["甘すぎる", "十分に大きい", "少し苦い"]),
        ("to one's surprise", "驚いたことに", "句", "To my surprise, the math test was very easy.", ["残念ながら", "いつものように", "その結果"]),
        ("judge", "審査員", "名詞", "The judges chose Ken's speech as the best one.", ["参加者", "設計者", "販売員"]),
        ("share", "分け合う", "動詞", "I shared my umbrella with a friend on the way home.", ["予約する", "比較する", "修理する"]),
        ("neighborhood", "近所・地域", "名詞", "There are two parks in my neighborhood.", ["田舎", "建設現場", "博物館"]),
        ("record", "レコード", "名詞", "My uncle has a large collection of old records.", ["楽器", "漫画本", "設計図"]),
        ("comic book", "漫画本", "名詞", "My brother has more than 100 comic books.", ["教科書", "写真集", "新聞記事"]),
        ("series", "シリーズ・連作", "名詞", "This comic book is part of a popular series.", ["市場", "世紀", "思い出"]),
        ("market", "市場・マーケット", "名詞", "We bought fresh vegetables at the market this morning.", ["教会", "図書館", "公園"]),
        ("item", "品物", "名詞", "This store sells many items for the kitchen.", ["着想", "柱", "体調"]),
        ("countryside", "田舎", "名詞", "My grandparents live in a quiet house in the countryside.", ["市街地", "海岸", "工場地帯"]),
        ("natural shape", "自然の形", "名詞", "The roof of the station has a natural shape, like a big leaf.", ["人工の光", "古い機械", "直線道路"]),
        ("support", "支える", "動詞", "Four strong legs support the heavy table.", ["完成する", "減少する", "発見する"]),
        ("construction", "建設", "名詞", "The construction of the new station will take three years.", ["健康", "記憶", "招待"]),
        ("World Heritage Site", "世界遺産", "名詞", "Mount Fuji became a World Heritage Site in 2013.", ["住宅地", "自然公園", "工業地帯"]),
    ]
    return [vocab(index, *entry) for index, entry in enumerate(entries, start=1)]


FOCUS_COLORS = {
    "fp1": "#4f8cff",
    "fp2": "#f472b6",
    "fp3": "#34d399",
    "fp4": "#fbbf24",
    "fp5": "#f59e0b",
}


def focus_point(
    point_id: str,
    title: str,
    subtitle: str,
    explanation: str,
    source_quote: str,
    source_location: str,
    examples: list[dict],
    passage_en: str,
    passage_ja: str,
    patterns: list[str],
    label: str,
    questions: list[dict],
) -> dict:
    return {
        "id": point_id,
        "title": title,
        "subtitle": subtitle,
        "explanation": explanation,
        "sourceQuote": source_quote,
        "sourceLocation": source_location,
        "examples": examples,
        "practicePassage": {
            "en": passage_en,
            "ja": passage_ja,
            "audioFile": f"audio/practice_pp{int(point_id[2:])}.mp3",
        },
        "highlightPatterns": patterns,
        "highlightColor": FOCUS_COLORS[point_id],
        "highlightLabel": label,
        "practiceQuestions": questions,
    }


def build_lesson_plan() -> dict:
    points = [
        focus_point(
            "fp1",
            "逆接・因果・予想外の結果",
            "Contrast, Cause & Unexpected Result",
            "Howeverで問題を提示し、soで判断と行動をつなぎ、To their surpriseで予想外の結果へ転じる物語の流れです。becauseは審査員がクッキーを評価した理由を示します。",
            "However / so they made them anyway / To their surprise / because they were not too sweet",
            "大問3「Maria's Baking Adventure」第1・2段落",
            [
                {"en": "However, when they got to the contest, they discovered that they had forgotten to bring sugar.", "ja": "しかし会場に着くと、砂糖を持ってくるのを忘れたことに気づきました。", "note": "Howeverは前向きな準備から問題発生への逆接。had forgottenは過去完了。"},
                {"en": "They hoped that the chocolate chips would make the cookies sweet enough, so they made them anyway.", "ja": "チョコレートチップで十分甘くなることを願い、そのまま作りました。", "note": "soは期待から行動への因果。anywayは『それでも』。"},
                {"en": "To their surprise, they won third prize.", "ja": "驚いたことに、二人は3位に入りました。", "note": "To one's surpriseは予想外の結果を導く定型句。"},
            ],
            "[出典: Maria's Baking Adventure 第1・2段落]\nHowever, when they got to the contest, they discovered that they had forgotten to bring sugar. They hoped that the chocolate chips would make the cookies sweet enough, so they made them anyway. To their surprise, they won third prize. The judges said that they really liked the cookies because they were not too sweet.",
            "しかし会場に着くと、砂糖を持ってくるのを忘れたことに気づきました。チョコレートチップで十分甘くなることを願い、そのまま作りました。驚いたことに、二人は3位に入りました。審査員は、甘すぎなかったのでクッキーがとても気に入ったと言いました。",
            ["However, when they got to the contest", "so they made them anyway", "To their surprise", "because they were not too sweet"],
            "展開・因果",
            [
                {"q": "Howeverは物語のどの変化を示しますか？", "a": "準備が順調だった場面から、砂糖を忘れた問題の発生へ転じます。"},
                {"q": "soの前後にはどのような因果がありますか？", "a": "チョコレートチップで甘くなると期待したため、砂糖なしでも作ったという因果です。"},
                {"q": "To their surpriseが導く結果は何ですか？", "a": "砂糖を忘れたのに3位に入ったという予想外の結果です。"},
                {"q": "becauseが示す審査員の評価理由は何ですか？", "a": "クッキーが甘すぎなかったことです。"},
            ],
        ),
        focus_point(
            "fp2",
            "代名詞の指示先と関係代名詞",
            "Reference Words & Relative Clauses",
            "them、oneなどの指示先を直前の名詞から追い、関係代名詞節がどの名詞を説明しているかを確認すると、メールの情報関係を正確に読めます。",
            "One of them / the series that you were telling me about / when I found them",
            "大問4A メール第1段落",
            [
                {"en": "Also, I got a couple of comic books. One of them is from the series that you were telling me about.", "ja": "それから漫画本を2冊買いました。そのうち1冊は、あなたが話していたシリーズのものです。", "note": "themはcomic books、oneはそのうち1冊。関係代名詞thatの節がseriesを説明。"},
                {"en": "I thought of you when I found them because I know how much you love comic books.", "ja": "あなたが漫画本をとても好きだと知っているので、それを見つけたときあなたのことを思い出しました。", "note": "themはcomic books。because以下が思い出した理由。"},
                {"en": "They sound great on my dad's old record player.", "ja": "それらは父の古いレコードプレーヤーで聴くと、とてもよい音です。", "note": "Theyは直前のrecordsを指す。"},
            ],
            "[出典: A question 第1段落]\nI bought some records from the 1960s and 1970s. They sound great on my dad's old record player. Also, I got a couple of comic books. One of them is from the series that you were telling me about when I visited your house. I thought of you when I found them because I know how much you love comic books.",
            "1960年代と1970年代のレコードを何枚か買いました。それらは父の古いレコードプレーヤーで聴くと、とてもよい音です。それから漫画本も2冊買いました。そのうち1冊は、私があなたの家を訪ねたときにあなたが話してくれたシリーズのものです。あなたが漫画本をとても好きだと知っているので、それを見つけたときあなたのことを思い出しました。",
            ["They sound great", "One of them", "the series that you were telling me about", "when I found them"],
            "指示語",
            [
                {"q": "最初のTheyは何を指しますか？", "a": "1960年代と1970年代のrecordsです。"},
                {"q": "One of themのoneとthemは何を指しますか？", "a": "oneは漫画本1冊、themはa couple of comic booksです。"},
                {"q": "that you were telling me aboutは何を説明しますか？", "a": "the seriesを説明する関係代名詞節です。"},
                {"q": "when I found themのthemは何を指しますか？", "a": "Steveが市場で見つけたcomic booksを指します。"},
            ],
        ),
        focus_point(
            "fp3",
            "提案（How about）・譲歩（even if）・would",
            "Suggestion, Concession & would",
            "How about ...?で提案し、even ifで不利な条件でも楽しめることを示します。wouldは控えめな見込み、said he wouldは過去から見た未来を表します。",
            "How about we go together / we'd have fun / even if / he said he would drive us there",
            "大問4A メール第2・3段落",
            [
                {"en": "How about we go together and see what we can find?", "ja": "一緒に行って何が見つかるか見てみませんか。", "note": "How about + 文で相手への提案。"},
                {"en": "I think we'd have fun searching through the items, even if they're too expensive for us to buy.", "ja": "たとえ高すぎて買えなくても、品物を探して楽しめると思います。", "note": "even ifは仮定的な譲歩『たとえ～でも』。"},
                {"en": "I asked my dad, and he said he would drive us there.", "ja": "父に頼むと、車で連れていってくれると言いました。", "note": "wouldはsaidの時点から見た未来。drive 人 there＝人を車でそこへ送る。"},
            ],
            "[出典: A question 第2・3段落]\nHow about we go together and see what we can find? I think we'd have fun searching through the items, even if they're too expensive for us to buy. Are you free next Saturday? The market is a little far away, but I asked my dad, and he said he would drive us there. We can go to a café for lunch and then take a bus back in the afternoon.",
            "一緒に行って何が見つかるか見てみませんか。たとえ高すぎて買えなくても、品物を探して楽しめると思います。次の土曜日は空いていますか。マーケットは少し遠いですが、父に頼むと車で連れていってくれると言いました。昼食はカフェで食べ、その後午後にバスで帰れます。",
            ["How about we go together", "we'd have fun", "even if they're too expensive for us to buy", "he said he would drive us there"],
            "提案・譲歩",
            [
                {"q": "How about we go togetherは何を表しますか？", "a": "SteveがJennyに一緒に市場へ行こうと提案しています。"},
                {"q": "even ifが示す不利な条件は何ですか？", "a": "品物が二人には高すぎて買えない可能性です。"},
                {"q": "he said he would drive us thereはどのように言い換えられますか？", "a": "His father agreed to give Steve and Jenny a ride. と言い換えられます。"},
                {"q": "we'd have funのwouldはどのような意味ですか？", "a": "一緒に品物を探せば楽しめるだろう、という控えめな見込みを表します。"},
            ],
        ),
        focus_point(
            "fp4",
            "現在完了・使役のmake・so ... that構文",
            "Present Perfect, Causative make & so ... that",
            "現在完了（have/has＋過去分詞）は、過去に始まったことが今どうなっているかを表します。has still not finishedは『始まってから今もまだ終わっていない』という意味です。make＋人＋動詞の原形は『人に～させる』、so＋形容詞＋that ...は『とても～なので…』と、原因と結果を結びます。",
            "make people feel / has still not finished / so important to the city that they have become",
            "大問4B「Antoni Gaudí」第2・4段落",
            [
                {"en": "Inside, the columns that support the roof make people feel like they are in a forest.", "ja": "内部では、屋根を支える柱が、人々に森の中にいるように感じさせます。", "note": "make＋人＋動詞の原形＝人に～させる。feelの前にtoは付けない。"},
                {"en": "Construction began in the late nineteenth century, but it has still not finished.", "ja": "建設は19世紀後半に始まりましたが、今もまだ終わっていません。", "note": "has still not finishedは現在完了。過去に始まり、今も完成していないことを表す。"},
                {"en": "Some of them are so important to the city that they have become UNESCO World Heritage Sites.", "ja": "そのうちいくつかは市にとって非常に重要なので、ユネスコ世界遺産になっています。", "note": "so＋形容詞＋that ...＝とても～なので…。have becomeは現在完了で、今は世界遺産であることを表す。"},
            ],
            "[出典: Antoni Gaudí 第2段落]\nThe Sagrada Família is a church in Barcelona that Gaudí designed. Although it is made from stone, glass, and metal, it looks like a picture of Gaudí's childhood memories. The towers of the Sagrada Família are like huge trees. Inside, the columns that support the roof make people feel like they are in a forest. Construction began in the late nineteenth century, but it has still not finished. Workers are using Gaudí's original designs to complete the building.",
            "サグラダ・ファミリアは、ガウディが設計したバルセロナの教会です。石、ガラス、金属でできていますが、ガウディの子ども時代の記憶を描いた絵のように見えます。サグラダ・ファミリアの塔は、巨大な木々のようです。内部では、屋根を支える柱が、人々に森の中にいるように感じさせます。建設は19世紀後半に始まりましたが、今もまだ終わっていません。作業員は、ガウディの元の設計図を使って建物を完成させようとしています。",
            ["make people feel", "has still not finished", "so important to the city that", "they have become UNESCO World Heritage Sites"],
            "完了・使役・程度",
            [
                {"q": "make people feel like they are in a forestで、feelの前にtoがないのはなぜですか？", "a": "make＋人＋動詞の原形の形で、『人に～させる』という意味になるからです。"},
                {"q": "it has still not finishedは、建設についてどのようなことを表していますか？", "a": "19世紀後半に始まった建設が、今もまだ終わっていないことを表しています。"},
                {"q": "has still not finishedを、yetを使って言い換えるとどうなりますか？", "a": "has not finished yetです。Q27の正解では、has not yet been completedと言い換えられています。"},
                {"q": "so important to the city that ...の文で、原因と結果はそれぞれ何ですか？", "a": "原因は建物が市にとってとても重要であること、結果はそれらがユネスコ世界遺産になったことです。"},
            ],
        ),
        focus_point(
            "fp5",
            "今回の重要なパラフレーズ",
            "Key Paraphrases in This Exam",
            "大問4の正解の選択肢は、本文と同じ内容を別の語句で言い換えていることがよくあります。たとえばQ29のBarcelona has become well-known for art and design.は、第4段落のhave helped to make Barcelona famous as a center of art and designの言い換えで、famousがwell-knownに変わっています。反対に、本文の語句を使っていても、主語・増減・場所などの内容が本文と違う選択肢は不正解です。根拠の文と意味が同じかどうかを確かめて選びましょう。",
            "①have helped to make Barcelona famous as a center of art and design → Barcelona has become well-known for art and design（芸術とデザインの中心地として有名にした→芸術とデザインで知られるようになった）\n②it has still not finished → has not yet been completed（まだ終わっていない→まだ完成していない）\n③where Gaudí lived for many years → It used to be one of the houses where Gaudí lived（長年住んでいた→かつて住んでいた家の一つだった）\n④he said he would drive us there → has agreed to give Steve and Jenny a ride（車で連れていくと言った→車に乗せることに同意した）\n⑤we'd have fun searching through the items → might enjoy looking through the things that are for sale（品物を探して楽しむ→売り物を見て回るのを楽しむ）",
            "大問4A・4B（Q24・Q25・Q27〜Q29）",
            [
                {"en": "These places have helped to make Barcelona famous as a center of art and design.", "ja": "これらの場所によって、バルセロナは芸術とデザインの中心地として有名になりました。", "note": "Q29：make Barcelona famous as a center of art and design → Barcelona has become well-known for art and design。famous → well-known。"},
                {"en": "Construction began in the late nineteenth century, but it has still not finished.", "ja": "建設は19世紀後半に始まりましたが、今もまだ終わっていません。", "note": "Q27：it has still not finished → Construction of the building has not yet been completed。finish → be completed、still not → not yet。"},
                {"en": "Interestingly, there is a tall, pink building in the park called the Casa Museu Gaudí, where Gaudí lived for many years.", "ja": "興味深いことに、公園にはガウディの家博物館と呼ばれる背の高いピンク色の建物があり、ガウディは長年そこに住んでいました。", "note": "Q28：a building ... where Gaudí lived for many years → It used to be one of the houses where Gaudí lived。building → house、lived → used to be（以前は～だった）。"},
            ],
            "[出典: Antoni Gaudí 第4段落]\nEven after Gaudí's death, his special approach to designing buildings is a source of ideas for designers around the world. Every year, many people visit Barcelona to see the Sagrada Família and the other buildings that Gaudí designed. These places have helped to make Barcelona famous as a center of art and design. Some of them are so important to the city that they have become UNESCO World Heritage Sites.",
            "ガウディの死後も、建物の設計に対する彼の独特な取り組み方は、世界中の設計者にとって着想の源になっています。毎年、多くの人がサグラダ・ファミリアやガウディが設計したほかの建物を見るためにバルセロナを訪れます。これらの場所によって、バルセロナは芸術とデザインの中心地として有名になりました。そのうちいくつかは市にとって非常に重要なので、ユネスコ世界遺産になっています。",
            ["These places have helped to make Barcelona famous as a center of art and design", "many people visit Barcelona", "a source of ideas for designers around the world", "where Gaudí lived for many years", "searching through the items"],
            "パラフレーズ",
            [
                {"q": "Q29で、have helped to make Barcelona famous as a center of art and designを言い換えた正解の選択肢はどれですか？", "a": "Barcelona has become well-known for art and design.です。famousがwell-knownに言い換えられています。"},
                {"q": "『バルセロナへの訪問者数が減った』という選択肢は正しいですか？", "a": "誤りです。Every year, many people visit Barcelonaとあり、減ったという記述はありません。"},
                {"q": "a source of ideas for designers around the worldを『設計者は仕事の方法を変えざるを得なくなった』と言い換えてよいですか？", "a": "いいえ。本文は設計者の着想の源になっていると述べているだけで、仕事の方法を変えざるを得なかったとは書かれていません。"},
                {"q": "ユネスコ世界遺産になったのは何ですか？", "a": "ガウディが設計したバルセロナの建物のうちのいくつか（Some of them）です。『彼の着想が世界各地の世界遺産で使われた』という選択肢は、場所を変えた誤りです。"},
            ],
        ),
    ]
    return {"focusPoints": points}


def build_data() -> dict:
    data = {
        "grade": "準2級",
        "year": "2024",
        "session": "1",
        "title": "2024年度 第1回（土曜準会場） 英語資格検定準2級 リーディング",
        "vocabulary": build_vocabulary(),
        "sections": build_sections(),
        "lessonPlan": build_lesson_plan(),
    }
    answers: list[int] = []
    numbers: list[int] = []
    for section in data["sections"]:
        for item in section.get("questions", []):
            numbers.append(item["number"])
            answers.append(item["answer"])
        for passage in section.get("passages", []):
            for item in passage["questions"]:
                numbers.append(item["number"])
                answers.append(item["answer"])
    if numbers != list(range(1, 30)):
        raise ValueError(f"Unexpected question numbers: {numbers}")
    if answers != OFFICIAL_ANSWERS:
        raise ValueError(f"Official answer mismatch: {answers}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build_data()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
