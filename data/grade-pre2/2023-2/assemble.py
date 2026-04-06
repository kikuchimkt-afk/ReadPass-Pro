"""Assemble all parts into final data.json for Pre-2 2023-2"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2"

# Load all parts
q1_10 = json.load(open(os.path.join(base, "_q01_10.json"), encoding="utf-8"))
q11_20 = json.load(open(os.path.join(base, "_q11_20.json"), encoding="utf-8"))
q21_25 = json.load(open(os.path.join(base, "_q21_25.json"), encoding="utf-8"))
p3a = json.load(open(os.path.join(base, "_q26_27.json"), encoding="utf-8"))
p3b = json.load(open(os.path.join(base, "_q28_30.json"), encoding="utf-8"))
p4a = json.load(open(os.path.join(base, "_q31_33.json"), encoding="utf-8"))
p4b = json.load(open(os.path.join(base, "_q34_37.json"), encoding="utf-8"))

# Build vocabulary list (40 words from all sections)
vocab_words = [
    # 大問1 (Q1-10)
    {"word":"struck","meaning":"打った","pos":"動詞","level":"準2級","example":"He struck the ball as hard as he could.","distractors":["混ぜた","噛んだ","コピーした"],"source":"大問1"},
    {"word":"fever","meaning":"熱","pos":"名詞","level":"準2級","example":"I think I have a fever.","distractors":["等級","驚き","習慣"],"source":"大問1"},
    {"word":"transport","meaning":"輸送する","pos":"動詞","level":"準2級","example":"Most companies use ships to transport their products overseas.","distractors":["設計する","相談する","拒否する"],"source":"大問1"},
    {"word":"encouraged","meaning":"励まされた","pos":"動詞","level":"準2級","example":"He felt encouraged to hear that he was doing a good job.","distractors":["怖がった","配達された","従った"],"source":"大問1"},
    {"word":"hired","meaning":"雇われた","pos":"動詞","level":"準2級","example":"I was hired two weeks ago.","distractors":["集められた","交換された","運ばれた"],"source":"大問1"},
    {"word":"region","meaning":"地域","pos":"名詞","level":"準2級","example":"Kansai is a region in western Japan.","distractors":["安全","テーマ","洗濯"],"source":"大問1"},
    {"word":"solve","meaning":"解く","pos":"動詞","level":"準2級","example":"I couldn't solve the last question.","distractors":["修理する","逃す","発明する"],"source":"大問1"},
    {"word":"essays","meaning":"エッセイ","pos":"名詞","level":"準2級","example":"Kelly writes two essays every month.","distractors":["勝利","システム","奇跡"],"source":"大問1"},
    {"word":"cheaply","meaning":"安く","pos":"副詞","level":"準2級","example":"The store sells clothes very cheaply.","distractors":["力強く","最近","勇敢に"],"source":"大問1"},
    {"word":"wealth","meaning":"富","pos":"名詞","level":"準2級","example":"He uses most of his wealth to help people.","distractors":["痛み","ナンセンス","文学"],"source":"大問1"},
    # 大問1 (Q11-20)
    {"word":"suffering from","meaning":"～に苦しんでいる","pos":"熟語","level":"準2級","example":"He was suffering from a bad cold.","distractors":["頼っている","あきらめている","専攻している"],"source":"大問1"},
    {"word":"pay attention","meaning":"注意を払う","pos":"熟語","level":"準2級","example":"Please pay attention in class.","distractors":["握手する","意味をなす","順番にやる"],"source":"大問1"},
    {"word":"in place of","meaning":"～の代わりに","pos":"熟語","level":"準2級","example":"They had to take buses in place of trains.","distractors":["代理で","恐れで","経由で"],"source":"大問1"},
    {"word":"by mistake","meaning":"間違えて","pos":"熟語","level":"準2級","example":"I must have taken it by mistake.","distractors":["現在","無料で","簡単に"],"source":"大問1"},
    {"word":"one another","meaning":"お互いに","pos":"代名詞","level":"準2級","example":"They write to one another at least once a month.","distractors":["他のどの","1つおきの","もう1つ"],"source":"大問1"},
    {"word":"hoping for","meaning":"～を望んでいる","pos":"句動詞","level":"準2級","example":"We are hoping for a girl.","distractors":["引き継いでいる","片付けている","見せびらかしている"],"source":"大問1"},
    {"word":"agree on","meaning":"～について合意する","pos":"句動詞","level":"準2級","example":"They could not agree on a name.","distractors":["注ぎ出す","轢く","持ちこたえる"],"source":"大問1"},
    # 大問2
    {"word":"last order","meaning":"ラストオーダー","pos":"名詞","level":"準2級","example":"The last order was 10 minutes ago.","distractors":["テーブル","初日","アイスクリーム"],"source":"大問2"},
    {"word":"skateboard","meaning":"スケートボード","pos":"名詞","level":"準2級","example":"I got a new skateboard at the department store.","distractors":["金の指輪","車","弁当箱"],"source":"大問2"},
    {"word":"pillow","meaning":"枕","pos":"名詞","level":"準2級","example":"I want a new pillow for my bed.","distractors":["ネックレス","カーペット","絵筆"],"source":"大問2"},
    # 大問3A
    {"word":"lonely","meaning":"寂しい","pos":"形容詞","level":"準2級","example":"He felt lonely every day at his new school.","distractors":["忙しい","嬉しい","退屈な"],"source":"大問3A"},
    {"word":"poster","meaning":"ポスター","pos":"名詞","level":"準2級","example":"Stephen saw a poster at school for a games club.","distractors":["教科書","黒板","ノート"],"source":"大問3A"},
    # 大問3B
    {"word":"greeting card","meaning":"グリーティングカード","pos":"名詞","level":"準2級","example":"Americans still buy around 6.5 billion greeting cards every year.","distractors":["手紙","はがき","招待状"],"source":"大問3B"},
    {"word":"electronic","meaning":"電子の","pos":"形容詞","level":"準2級","example":"Sending an electronic message is quicker.","distractors":["紙の","手書きの","口頭の"],"source":"大問3B"},
    {"word":"trash","meaning":"ゴミ","pos":"名詞","level":"準2級","example":"This creates a lot of trash.","distractors":["資源","エネルギー","材料"],"source":"大問3B"},
    {"word":"remind","meaning":"思い出させる","pos":"動詞","level":"準2級","example":"People are reminded about events on social media.","distractors":["招待する","無視する","忘れる"],"source":"大問3B"},
    # 大問4A
    {"word":"camping","meaning":"キャンプ","pos":"名詞","level":"準2級","example":"I thought we could go camping by Mirror Lake.","distractors":["ハイキング","水泳","釣り"],"source":"大問4A"},
    {"word":"fishing","meaning":"釣り","pos":"名詞","level":"準2級","example":"Have you ever been fishing before?","distractors":["サーフィン","乗馬","登山"],"source":"大問4A"},
    {"word":"practice","meaning":"練習する","pos":"動詞","level":"準2級","example":"We can go to a park to practice throwing and catching.","distractors":["試合する","観戦する","休む"],"source":"大問4A"},
    # 大問4B
    {"word":"comfortable","meaning":"快適な","pos":"形容詞","level":"準2級","example":"She might be more comfortable sitting in her own car.","distractors":["不便な","危険な","退屈な"],"source":"大問4B"},
    {"word":"screen","meaning":"スクリーン","pos":"名詞","level":"準2級","example":"He put a screen and some speakers in his yard.","distractors":["ステージ","テーブル","椅子"],"source":"大問4B"},
    {"word":"popular","meaning":"人気のある","pos":"形容詞","level":"準2級","example":"Drive-in movie theaters soon became popular.","distractors":["不人気の","珍しい","古い"],"source":"大問4B"},
    {"word":"bother","meaning":"困らせる","pos":"動詞","level":"準2級","example":"Children could run around without bothering other people.","distractors":["助ける","褒める","招待する"],"source":"大問4B"},
    {"word":"playground","meaning":"遊び場","pos":"名詞","level":"準2級","example":"Some drive-in theaters even had playgrounds.","distractors":["駐車場","売店","出口"],"source":"大問4B"},
    {"word":"rent","meaning":"レンタルする","pos":"動詞","level":"準2級","example":"People could rent videos to watch at home.","distractors":["購入する","修理する","捨てる"],"source":"大問4B"},
    {"word":"owner","meaning":"オーナー","pos":"名詞","level":"準2級","example":"Many owners decided to sell their theaters.","distractors":["従業員","顧客","俳優"],"source":"大問4B"},
]

# Add wordAudio paths
for i, v in enumerate(vocab_words):
    safe = v["word"].replace(" ", "_").replace("'", "")
    v["wordAudio"] = f"audio/vocab/w_{i+1:03d}_{safe}.mp3"

# Build sections
sec1 = {
    "name": "大問1", "nameEn": "Part 1", "type": "vocabulary",
    "instruction": "次の(1)から(20)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": q1_10 + q11_20
}

sec2 = {
    "name": "大問2", "nameEn": "Part 2", "type": "vocabulary",
    "instruction": "次の四つの会話文を完成させるために，(21)から(25)に入るものとして最も適切なものを選びなさい。",
    "questions": q21_25
}

sec3 = {
    "name": "大問3", "nameEn": "Part 3", "type": "reading-comprehension",
    "instruction": "次の英文 A , B を読み，その文意にそって(26)から(30)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {"label": "A", "title": p3a["title"], "passage": p3a["passage"], "passageTranslation": p3a["passageTranslation"], "questions": p3a["questions"]},
        {"label": "B", "title": p3b["title"], "passage": p3b["passage"], "passageTranslation": p3b["passageTranslation"], "questions": p3b["questions"]}
    ]
}

sec4 = {
    "name": "大問4", "nameEn": "Part 4", "type": "reading-comprehension",
    "instruction": "次の英文 A , B の内容に関して，(31)から(37)までの質問に対して最も適切なもの，または文を完成させるのに最も適切なものを1，2，3，4の中から一つ選び，その番号を解答用紙の所定欄にマークしなさい。",
    "passages": [
        {"label": "A", "title": p4a["title"], "emailHeader": p4a["emailHeader"], "passage": p4a["passage"], "passageTranslation": p4a["passageTranslation"], "questions": p4a["questions"]},
        {"label": "B", "title": p4b["title"], "passage": p4b["passage"], "passageTranslation": p4b["passageTranslation"], "questions": p4b["questions"]}
    ]
}

# Lesson Plan
lesson_plan = {
    "focusPoints": [
        {"id":"fp1","title":"感情と問題解決の表現","description":"感情を表す表現と問題解決への道筋を読み取る力を養う"},
        {"id":"fp2","title":"比較と対比の論理展開","description":"ものごとを比較・対比して述べる表現パターンを学ぶ"},
        {"id":"fp3","title":"時間経過と変化の表現","description":"時間の経過に伴う変化を表す接続表現と構文を学ぶ"},
        {"id":"fp4","title":"理由と結果の因果関係","description":"原因・理由から結果を説明する論理展開を読み取る力を養う"},
        {"id":"fp5","title":"今回の重要なパラフレーズ","description":"本文と選択肢の言い換え表現（パラフレーズ）を見抜く力を養う"}
    ]
}

# Assemble final data
data = {
    "grade": "準2級",
    "year": "2023",
    "session": "2",
    "title": "2023年度 第2回 英検準2級 リーディング",
    "vocabulary": vocab_words,
    "sections": [sec1, sec2, sec3, sec4],
    "lessonPlan": lesson_plan
}

# Save
with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

total_q = len(sec1["questions"]) + len(sec2["questions"])
for s in [sec3, sec4]:
    for p in s["passages"]:
        total_q += len(p["questions"])

print(f"data.json saved!")
print(f"  Vocabulary: {len(vocab_words)} words")
print(f"  Questions: {total_q}")
print(f"  Sections: {len(data['sections'])}")
print(f"  Focus Points: {len(lesson_plan['focusPoints'])}")
