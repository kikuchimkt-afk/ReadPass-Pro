---
description: 2級のリスニング過去問をAudiPassに追加する
---

# ReadPass Pro — 2級 新規試験追加ワークフロー

// turbo-all

## 概要
英検2級のリーディング過去問PDFから `data.json` を生成し、ReadPass Pro に新しい試験回を追加するための完全手順。
**このワークフローを上から順に実行すれば、一発で確実に実装できる。**

---

## 前提条件

- 過去問PDFが `G:\マイドライブ\text\bookshelf\英検過去問\2級\{exam_folder}\` に配置済み
- `exam_folder` 名は `2級{year}-{session}` 形式（例: `2級2025-2`）
- 出力先: `g:\マイドライブ\eiken practice\data\grade2\{exam_id}\data.json`
  - `exam_id` は `{year}-{session}` 形式（例: `2025-2`）
- 開発サーバ: `npx -y http-server "g:\マイドライブ\eiken practice" -p 8085 -c-1`

---

## Step 0: 既存データの確認（重複回避）

1. `g:\マイドライブ\eiken practice\data\grade2\` 配下の全 `data.json` を確認
2. 既存試験回の `lessonPlan.focusPoints` タイトル一覧を取得
3. **新規試験のFP1-4は、既存試験と文法トピックが重複しないようにする**

```python
import json, os
base = r"g:\マイドライブ\eiken practice\data\grade2"
for exam in sorted(os.listdir(base)):
    path = os.path.join(base, exam, "data.json")
    if os.path.exists(path):
        d = json.load(open(path, "r", encoding="utf-8"))
        fps = d.get("lessonPlan", {}).get("focusPoints", [])
        print(f"\n{exam}:")
        for fp in fps:
            print(f"  {fp.get('id','?')}: {fp.get('title','?')}")
```

---

## Step 1: PDF テキスト抽出

PyMuPDF で各ページのテキストを抽出する。

```python
import fitz, sys, os
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"G:\マイドライブ\text\bookshelf\英検過去問\2級\2級YYYY-S\問題.pdf"  # パス調整
output_dir = r"G:\マイドライブ\text\bookshelf\英検過去問\2級\2級YYYY-S\new problem"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
```

**ページ構成（2級標準）:**
| ページ | 内容 |
|--------|------|
| 3-6 | Part 1（語彙・文法 17問） |
| 7-8 | Part 2（長文穴埋め 2パッセージ 6問） |
| 9-11 | Part 3（長文読解 2パッセージ 8問） |
| 12+ | Writing / Summary（参考用） |

---

## Step 2: data.json 生成スクリプト作成

**必ずPythonスクリプトで生成する**（手動編集は誤りの原因）。
スクリプトは `C:\tmp\gen_g2_{exam_id}.py` に作成する。

### 2a. トップレベル構造

```python
import json

data = {
    "grade": "2級",
    "year": "YYYY",
    "session": "S",
    "title": "YYYY年度 第S回 英検2級 リーディング",
    "vocabulary": [],  # Step 2b で追加
    "sections": [],    # Step 2c-2e で追加
    "lessonPlan": {}   # Step 3 で追加
}
```

### 2b. vocabulary 配列（★51語以上・全大問から均等抽出）

各単語は以下の形式:
```json
{
    "word": "abandon",
    "meaning": "～を捨てる",
    "pos": "動詞",
    "level": "2級",
    "example": "She decided to abandon the project.",
    "distractors": ["～を始める", "～を続ける", "～を完成させる"]
}
```

#### ★★★ 語彙抽出ルール（最重要）★★★

> **⚠ 大問1だけから単語を抽出してはならない。必ず大問2・大問3のパッセージからもバランスよく抽出すること。**

| 抽出元 | 目標語数 | 説明 |
|--------|----------|------|
| 大問1（語彙・文法） | 17〜25語 | 選択肢の正答＋重要な誤答から抽出 |
| 大問2（長文穴埋め） | 10〜15語 | パッセージ A・B の本文中の重要語を抽出 |
| 大問3（長文読解） | 10〜15語 | パッセージ A・B の本文中の重要語を抽出 |
| **合計** | **51語以上** | 全大問からバランスよく収録 |

- **P2/P3からの抽出を忘れると検証で不合格になる（過去の頻発ミス）**
- Part 2/3 の単語はパッセージのテーマに関連する専門語・重要語を選ぶ
- 熟語（句動詞）も `"on me"` `"break in"` のようにフレーズ全体を `word` に入れる（前置詞単体は不可）
- **example は試験本文とは異なるオリジナル例文を作成する**
- `distractors` は意味が紛らわしい3つの誤選択肢（和訳）

### 2c. Section 0: 大問1（vocabulary 型）

```json
{
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(17)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "問題文 ( 1 ) を含むテキスト",
            "translation": "和訳テキスト",
            "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
            "answer": 1  // ★1-indexed（正答表の番号そのまま）
        }
    ]
}
```

**注意:**
- `answer` は **1-indexed**（正答表の番号をそのまま使う）
- キー名は `choices`（`options` は不可）、`answer`（`correctAnswer` は不可）
- `translation` キーで和訳を追加
- 問題番号 `( 1 )` は半角スペース入りで記載（`( 1 )` → 表示時に赤枠付きに変換される）

### 2d. Section 1: 大問2（passage-fill 型）

```json
{
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(18)から(23)までの(　)に入れるのに最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "パッセージタイトル",
            "paragraphs": ["段落1のテキスト", "段落2のテキスト"],
            "translations": ["和訳段落1", "和訳段落2"],
            "sentencePairs": [
                ["English sentence 1.", "日本語訳1。"],
                ["English sentence 2.", "日本語訳2。"]
            ],
            "questions": [
                {
                    "number": 18,
                    "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
                    "answer": 1  // ★1-indexed
                }
            ]
        }
    ]
}
```

**sentencePairs の注意事項（★最重要）:**
- 英文は **パッセージ `paragraphs` 内のテキストと完全一致** すること
- `Mr.` `U.K.` `St.` 等の略語内のピリオドで文を分割しないこと
- `( 18 )` 等の問題番号マーカーを含む文も、そのまま元の文として記載する
- 各文は重複なく、パッセージ全体をカバーする

### 2e. Section 2: 大問3（reading-comprehension 型）

```json
{
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，質問に対して最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "タイトル",
            "format": "email",  // "email" or 省略
            "meta": {"from": "Name", "to": "Name", "date": "Date", "subject": "Subject"},
            "paragraphs": ["段落1", "段落2"],
            "translations": ["和訳1", "和訳2"],
            "sentencePairs": [["en", "ja"]],
            "questions": [
                {
                    "number": 24,
                    "question": "質問テキスト",
                    "choices": ["A", "B", "C", "D"],
                    "answer": 1  // ★1-indexed
                }
            ]
        }
    ]
}
```

**大問3 パッセージAの特徴:**
- `format: "email"` の場合、`meta` オブジェクト（From/To/Date/Subject）が必要
- 手紙・お知らせ等がフォーマットされて表示される

### 2f. スクリプト実行と保存

```python
import os
output_dir = r"g:\マイドライブ\eiken practice\data\grade2\YYYY-S"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "data.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"Saved to {output_path}")
```

---

## Step 3: lessonPlan（文法解析・教材）追加

### 3a. focusPoints 構造

**5つのFocusPointを追加する。各FPには必ず `id` を含める（★重要）：**

```json
{
    "id": "fp1",          // ★必須！ "fp1"～"fp5"
    "title": "構文名",
    "subtitle": "English Subtitle",
    "explanation": "解説文",     // ★キー名 "explanation"（"why"は不可）
    "sourceQuote": "出典箇所の引用",
    "sourceLocation": "Part 2A 第1段落",
    "examples": [               // ★キー名 "examples"（"exampleSentences"は不可）
        {
            "en": "Example sentence.",
            "ja": "例文和訳。",
            "note": "文法解説ノート"
        }
    ],
    "practicePassage": {       // ★★★ 全FPに必須（欠落厳禁）★★★
        "en": "Practice paragraph (5-7 sentences, original topic)...",
        "ja": "練習パッセージ和訳..."
    },
    "practiceQuestions": [       // ★focusPointの直下（practicePassage内ではない）
        {"q": "質問", "a": "回答"},
        {"q": "質問", "a": "回答"},
        {"q": "質問", "a": "回答"}
    ],
    "highlightPatterns": [      // フレーズレベルの長い文字列（1語だけは不可）
        "the entire relevant phrase from passage"
    ],
    "highlightColor": "#4f8cff",
    "highlightLabel": "短いラベル名"
}
```

### 3b. FP構成ルール

| FP | 内容 | ルール |
|----|------|--------|
| fp1-fp4 | **文法・構文トピック** | 同じ級の他試験と重複しないトピックを選ぶ |
| fp5 | **パラフレーズ（必須）** | タイトル固定「今回の重要なパラフレーズ」 |

#### ★★★ FP品質ルール（最重要）★★★

> **⚠ FP1〜4は必ず文法・構文トピックにすること。内容テーマ（語彙・トピック）ベースのFPは不可。**

**✅ 正しいFPタイトルの例（文法・構文）：**
- 比較・類似の表現（Comparison & Similarity Patterns）
- 提案のthat節と仮定法現在（Suggest + Subjunctive Present）
- 非人称受動態 It is believed / hoped that
- ディスコースマーカーと文章展開
- 使役動詞と知覚動詞の構文
- 同格表現と名詞の言い換え
- 時制の使い分けと歴史叙述

**❌ 不可なFPタイトルの例（内容・語彙ベース）：**
- ~~珍しいペットの語彙と英語表現~~
- ~~句動詞・イディオム集中特訓~~
- ~~音楽の歴史：Delta Blues → Chicago Blues~~
- ~~環境テーマの読解：芝ペンキと持続可能性~~
- ~~古代文明と考古学の語彙~~
- ~~花言葉と感情表現の語彙~~

**FP5は必ず「今回の重要なパラフレーズ」をタイトルにし、本文と選択肢の対応を番号付きで記載する。**

#### ★★★ practicePassage 必須ルール（最重要）★★★

> **⚠ 全5つのFPに必ず `practicePassage`（en/ja）と `practiceQuestions`（3〜4問）を含めること。欠落は検証で不合格になる。**

- 各パッセージは **5〜7文** の短いパラグラフ（本文とは異なるオリジナルトピック）
- 当該FPの文法・構文が **自然に複数回使われている** こと
- 英語＋日本語訳のペア
- 3〜4個の `practiceQuestions` と対にする

### 3c. highlightPatterns の品質基準

- **フレーズレベル**のハイライト（単語1つだけではなく、文脈のある長いフレーズ）
- 各FPにつき **11〜15パターン** を目標
- 大問2と大問3の両方のパッセージからパターンを抽出
- 2025-3 exam のハイライトを品質参照基準とする

### 3d. highlightColor の標準色

| FP | 色名 | HEX値 |
|----|------|-------|
| fp1 | Blue | `#4f8cff` |
| fp2 | Green | `#34d399` |
| fp3 | Pink | `#f472b6` |
| fp4 | Yellow/Amber | `#fbbf24` |
| fp5 | Orange | `#f59e0b` |

### 3e. FP5（パラフレーズ）の固定ルール

- `title`: `"今回の重要なパラフレーズ"`
- `sourceQuote`: 番号付き（①②③…）で各パラフレーズペアを `\n` 区切り
- `examples`: 一般的なパラフレーズ例文を3つ
- `practiceQuestions`: 4問
- `highlightColor`: `"#f59e0b"`
- `highlightLabel`: `"パラフレーズ"`

---

## Step 4: top.js にエントリ追加

`g:\マイドライブ\eiken practice\top.js` の `EXAM_CATALOG` に新しい試験を追加。

**並び順ルール: 古い試験が上、新しい試験が下**

```javascript
exams: [
    { id: '2024-3', label: '2024年度 第3回', sub: '一次試験リーディング' },
    { id: '2025-1', label: '2025年度 第1回', sub: '一次試験リーディング' },
    { id: '2025-2', label: '2025年度 第2回', sub: '一次試験リーディング' },
    { id: '2025-3', label: '2025年度 第3回', sub: '一次試験リーディング' }  // 最新が最下部
]
```

---

## Step 5: 検証

### 5a. 構造検証スクリプト

```python
import json

def verify(path):
    d = json.load(open(path, "r", encoding="utf-8"))
    errors = []

    # 1. トップレベルキーチェック
    for k in ["grade", "year", "session", "title", "vocabulary", "sections", "lessonPlan"]:
        if k not in d:
            errors.append(f"Missing top-level key: {k}")
    vocab = d.get("vocabulary", [])
    if len(vocab) < 50:
        errors.append(f"vocabulary count = {len(vocab)}, must be 50+")

    # 2. sections チェック
    types = {s["type"] for s in d.get("sections", [])}
    for t in ["vocabulary", "passage-fill", "reading-comprehension"]:
        if t not in types:
            errors.append(f"Missing section type: {t}")

    # 3. focusPoints チェック
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5:
        errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        if "id" not in fp:
            errors.append(f"FP{i+1}: missing 'id' (MUST be 'fp{i+1}')")
        for key in ["explanation", "examples", "practicePassage", "practiceQuestions", "highlightPatterns", "highlightColor", "highlightLabel"]:
            if key not in fp:
                errors.append(f"FP{i+1} '{fp.get('title','')}': missing '{key}'")
        if "practicePassage" in fp:
            pp = fp["practicePassage"]
            if not pp.get("en") or not pp.get("ja"):
                errors.append(f"FP{i+1}: practicePassage missing 'en' or 'ja'")
        pq = fp.get("practiceQuestions", [])
        if len(pq) < 3:
            errors.append(f"FP{i+1}: only {len(pq)} practiceQuestions (need 3-4)")
        hp = fp.get("highlightPatterns", [])
        if len(hp) < 3:
            errors.append(f"FP{i+1}: only {len(hp)} highlight patterns (recommend 11-15)")

    # 4. sentencePairs チェック
    for s in d.get("sections", []):
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND in passage: '{pair[0][:50]}...'")

    # 5. correctAnswer 範囲チェック
    for s in d.get("sections", []):
        qs = s.get("questions", [])
        for p in s.get("passages", []):
            qs += p.get("questions", [])
        for q in qs:
            ca = q.get("correctAnswer")
            if ca is not None and (ca < 0 or ca > 3):
                errors.append(f"Q{q.get('number')}: correctAnswer={ca} out of range 0-3")

    if errors:
        print("⚠ VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ ALL CHECKS PASSED")

verify(r"g:\マイドライブ\eiken practice\data\grade2\YYYY-S\data.json")
```

### 5b. ブラウザ検証チェックリスト

| # | テスト項目 | 確認手順 |
|---|-----------|---------|
| 1 | トップページ表示 | `localhost:8085/top.html` → 新試験が表示される |
| 2 | 単語タブ | 4択クイズが全17問表示される |
| 3 | 大問1タブ | 17問の空所補充が表示される |
| 4 | 大問2タブ | 2つのパッセージ＋6問が表示される |
| 5 | 大問3タブ | 2つのパッセージ＋8問が表示される |
| 6 | 文法タブ | 5つのfocusPointカードが表示される |
| 7 | 文訳ポップアップ | 大問2/3の本文をクリック → 和訳が表示される |
| 8 | マーカーON | ツールバー「文法マーカー」→ 5色のハイライトが表示される |
| 9 | 凡例個別トグル | 凡例の各項目をクリック → 該当色のみON/OFF |
| 10 | 正解表示/非表示 | ツールバーで切替 → 正解バッジの表示/非表示 |
| 11 | 印刷メニュー | 印刷ボタン → 8種類のメニューが表示される |
| 12 | 単語カード | ツールバー → 別ウィンドウで単語カードが開く |
| 13 | ライトモード | テーマ切替 → ハイライト・凡例が見やすい |

---

## 過去の落とし穴と対策一覧

| 問題 | 原因 | 対策 |
|------|------|------|
| 凡例の個別選択不可 | focusPoints に `"id"` キーがない | **各FPに必ず `"id": "fp1"` ~ `"fp5"` を付ける** |
| 文法タブが空白 | キー名の不一致（`why`/`exampleSentences`） | `explanation`, `examples`, `practiceQuestions` を使う |
| 文訳ポップアップが壊れる | 翻訳テキストを `data-trans` 属性に直接格納 | `data-tidx` でインデックス参照方式を使う（app.js側対応済み） |
| 文分割の誤り | `Mr.` 等の略語でピリオド分割 | `sentencePairs` で英文を明示指定、`indexOf()` でマッチ |
| 各タブが空白になる | `sections.type` の値が間違っている | `vocabulary`, `passage-fill`, `reading-comprehension` を正確に |
| ハイライトが薄い | パターンが単語1つだけ | フレーズレベル（11-15パターン）で設定する |
| 印刷のレッスンプランが空 | `lessonPlan.focusPoints` がない | Step 3 で必ず追加する |
| 単語が大問1に偏る | P2/P3パッセージからの抽出漏れ | **大問2から10-15語、大問3から10-15語を必ず抽出する** |
| FPが内容ベース | 語彙・トピックテーマのFPを作った | **FP1-4は文法構文トピックのみ。語彙/テーマ名は不可** |
| FP5がパラフレーズでない | FP5にも文法トピックを入れた | **FP5は必ず「今回の重要なパラフレーズ」固定** |
| 前置詞単体が単語カードに出る | `on` のように前置詞1語だけをwordに入れた | **`on me` のようにフレーズ全体を入れる** |
| **練習パッセージが表示されない** | `practicePassage` キーが欠落 | **全5 FPに必ず `practicePassage`（en/ja）を追加** |
| **確認問題が空** | `practiceQuestions` が無い or 0件 | **全5 FPに3〜4問の `practiceQuestions` を追加** |

---

## ファイル構成

```
g:\マイドライブ\eiken practice\
├── top.js            ← EXAM_CATALOG にエントリ追加
├── app.js            ← 変更不要（共通ロジック）
├── index.html        ← 変更不要
├── style.css         ← 変更不要
├── vocab-cards.html  ← 変更不要
└── data/
    └── grade2/
        └── {exam_id}/
            └── data.json   ← Step 2-3 で生成
```
