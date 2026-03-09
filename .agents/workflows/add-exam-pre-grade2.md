---
description: 準2級のリーディング過去問をReadPass Proに追加する
---

# ReadPass Pro — 準2級 新規試験追加ワークフロー

// turbo-all

## 概要
英検準2級のリーディング過去問PDFから `data.json` を生成し、ReadPass Pro に新しい試験回を追加するための完全手順。
**このワークフローを上から順に実行すれば、一発で確実に実装できる。**

---

## 他の級との主な差異

| 項目 | 準2級 | 2級 | 準1級 |
|------|-------|-----|-------|
| 語彙数 | **40語以上** | 51語以上 | 80語以上 |
| 大問1 | **15問（短文空所補充）** | 17問 | 18問 |
| 大問2 | **5問（会話文空所補充）** | 6問（長文穴埋め） | 6問（長文穴埋め） |
| 大問3 | **2問（長文穴埋め1パッセージ）** | 8問（長文読解） | 7問（長文読解） |
| 大問4 | **7問（長文読解 A:email3問 B:4問）** | — | — |
| 合計 | **29問** | 31問 | 31問 |
| choiceAnalysis | **あり（必須）** | あり | あり＋sourceEvidence |
| 選択肢和訳 | なし | なし | choiceTranslations必須 |
| データパス | `data/grade-pre2/` | `data/grade2/` | `data/pre-grade1/` |
| EXAM_CATALOG id | `grade-pre2` | `grade2` | `pre-grade1` |

### ★ 準2級 固有の特徴
1. **大問2は「会話文の文空所補充」** — 2つの会話（A:2問, B:3問）。app.jsでは `vocabulary` タイプで実装する（text + choices形式、translationあり）
2. **大問3は長文穴埋め1パッセージのみ**（2問）
3. **大問4がメインの長文読解**（A=email3問、B=4問）
4. **vocabulary レベルは `"準2級"` を使用**

---

## 前提条件

- 過去問PDFが `G:\マイドライブ\text\bookshelf\英検過去問\準2級\準2級{year}-{session}\` に配置済み
  - ファイル名: `{year}-{session}-1ji-p2kyu.pdf`
  - 正答表: `{year}{session}Fp2kyu.pdf`
- 出力先: `g:\マイドライブ\ReadPass Pro\data\grade-pre2\{exam_id}\data.json`
  - `exam_id` は `{year}-{session}` 形式（例: `2025-3`）
- 開発サーバ: `npx -y http-server "g:\マイドライブ\ReadPass Pro" -p 8085 -c-1`

---

## Step 0: 既存データの確認（重複回避）

1. `g:\マイドライブ\ReadPass Pro\data\grade-pre2\` 配下の全 `data.json` を確認
2. 既存試験回の `lessonPlan.focusPoints` タイトル一覧を取得
3. **新規試験のFP1-4は、既存試験と文法トピックが重複しないようにする**

```python
import json, os
base = r"g:\マイドライブ\ReadPass Pro\data\grade-pre2"
if not os.path.exists(base):
    print("No exams yet")
else:
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

pdf_path = r"G:\マイドライブ\text\bookshelf\英検過去問\準2級\準2級YYYY-S\YYYY-S-1ji-p2kyu.pdf"
output_dir = r"G:\マイドライブ\text\bookshelf\英検過去問\準2級\準2級YYYY-S\new problem"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
```

**ページ構成（準2級 2024年度改訂後）:**
| ページ | 内容 |
|--------|------|
| 3-4 | 大問1（語彙・文法 15問） |
| 5 | 大問2（会話文空所補充 5問） |
| 6 | 大問3（長文穴埋め 1パッセージ 2問） |
| 7-9 | 大問4（長文読解 2パッセージ 7問） |
| 10-11 | ライティング（参考用） |
| 12+ | リスニング（参考用） |

---

## Step 2: data.json 生成スクリプト作成

**必ずPythonスクリプトで生成する**（手動編集は誤りの原因）。
スクリプトは `C:\tmp\gen_p2kyu_{exam_id}.py` に作成する。

### 2a. トップレベル構造

```python
import json

data = {
    "grade": "準2級",
    "year": "YYYY",
    "session": "S",
    "title": "YYYY年度 第S回 英検準2級 リーディング",
    "vocabulary": [],  # Step 2b で追加
    "sections": [],    # Step 2c-2f で追加
    "lessonPlan": {}   # Step 3 で追加
}
```

### 2b. vocabulary 配列（★40語以上・全大問から均等抽出）

各単語は以下の形式:
```json
{
    "word": "joy",
    "meaning": "喜び",
    "pos": "名詞",
    "level": "準2級",
    "example": "She was filled with joy when she heard the news.",
    "distractors": ["技術", "音声", "家賃"]
}
```

#### ★★★ 語彙抽出ルール（最重要）★★★

> **⚠ 大問1だけから単語を抽出してはならない。必ず大問3・大問4のパッセージからもバランスよく抽出すること。**

| 抽出元 | 目標語数 | 説明 |
|--------|----------|------|
| 大問1（語彙・文法） | 15〜20語 | 選択肢の正答＋重要な誤答から抽出 |
| 大問2（会話文） | 5〜8語 | 会話文中の重要語・イディオムを抽出 |
| 大問3（長文穴埋め） | 5〜8語 | パッセージ本文中の重要語を抽出 |
| 大問4（長文読解） | 10〜15語 | パッセージ A・B の本文中の重要語を抽出 |
| **合計** | **40語以上** | 全大問からバランスよく収録 |

- **P3/P4からの抽出を忘れると検証で不合格になる（過去の頻発ミス）**
- 熟語（句動詞）も `"laugh at"` `"all over"` のようにフレーズ全体を `word` に入れる
- **example は試験本文とは異なるオリジナル例文を作成する**
- `distractors` は意味が紛らわしい3つの誤選択肢（和訳）

### 2c. Section 0: 大問1（vocabulary 型・15問）

```json
{
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(15)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "問題文 ( 1 ) を含むテキスト",
            "translation": "和訳テキスト",
            "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
            "choiceTranslations": ["和訳1", "和訳2", "和訳3", "和訳4"],
            "answer": 1,
            "choiceAnalysis": ["❌ 選択肢1＝意味。不正解の理由", "❌ 選択肢2＝意味。不正解の理由", "✅ 選択肢3＝意味。正解の理由", "❌ 選択肢4＝意味。不正解の理由"],
            "grammar": "💡 重要表現の解説（例: be filled with ～＝～でいっぱいになる）"
        }
    ]
}
```

**注意:**
- `answer` は **1-indexed**（正答表の番号そのまま使う）
- キー名は `choices`（`options` は不可）、`answer`（`correctAnswer` は不可）
- `translation` キーで和訳を追加
- 問題番号 `( 1 )` は半角スペース入りで記載

### 2d. Section 1: 大問2（vocabulary 型・5問・会話文空所補充）

**★ 準2級固有セクション: 会話文の空所補充**

```json
{
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "vocabulary",
    "instruction": "次の(16)から(20)までの会話文の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 16,
            "text": "A : .... ( 16 ) ...\nB : ....",
            "translation": "A：...（16）...\nB：...",
            "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
            "choiceTranslations": ["和訳1", "和訳2", "和訳3", "和訳4"],
            "answer": 1,
            "choiceAnalysis": ["和訳1→正解。💡 根拠", "和訳2→不正解の理由", "和訳3→不正解の理由", "和訳4→不正解の理由"],
            "grammar": "💡 ..."
        }
    ]
}
```

**★ 会話文のフォーマット:**
- `text` に A: / B: の会話全体を含める（改行 `\n` で区切る）
- `translation` に会話全体の和訳を追加
- 選択肢は文レベル（フレーズや文）
- 2つの会話（A:2問＋B:3問）を5問の `questions` 配列に入れる

### 2e. Section 2: 大問3（passage-fill 型・2問）

```json
{
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "passage-fill",
    "instruction": "次の英文の(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "passages": [
        {
            "label": "",
            "title": "パッセージタイトル",
            "paragraphs": ["段落1のテキスト", "段落2のテキスト"],
            "translations": ["和訳段落1", "和訳段落2"],
            "sentencePairs": [
                ["English sentence 1.", "日本語訳1。"],
                ["English sentence 2.", "日本語訳2。"]
            ],
            "questions": [
                {
                    "number": 21,
                    "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
                    "choiceTranslations": ["選択肢1和訳", "選択肢2和訳", "選択肢3和訳", "選択肢4和訳"],
                    "answer": 3,
                    "choiceAnalysis": [
                        "選択肢1和訳→不正解の理由",
                        "選択肢2和訳→不正解の理由",
                        "選択肢3和訳→正解。💡 本文の根拠となる英文が直接の根拠",
                        "選択肢4和訳→不正解の理由"
                    ],
                    "grammar": "💡 ..."
                }
            ]
        }
    ]
}
```

**★ 準2級の大問3は1パッセージのみ（2級は2パッセージ）**
- `label` は空文字列
- 2問のみ

### 2f. Section 3: 大問4（reading-comprehension 型・7問）

```json
{
    "name": "大問4",
    "nameEn": "Part 4",
    "type": "reading-comprehension",
    "instruction": "次のＡ，Ｂの内容に関して，質問に対して最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "メールタイトル",
            "format": "email",
            "meta": {"from": "Name", "to": "Name", "date": "Date", "subject": "Subject"},
            "paragraphs": ["段落1", "段落2"],
            "translations": ["和訳1", "和訳2"],
            "sentencePairs": [["en", "ja"]],
            "questions": [
                {
                    "number": 23,
                    "question": "質問テキスト",
                    "questionTranslation": "質問の日本語訳",
                    "choices": ["A", "B", "C", "D"],
                    "choiceTranslations": ["選択肢1和訳", "選択肢2和訳", "選択肢3和訳", "選択肢4和訳"],
                    "answer": 1,
                    "choiceAnalysis": [
                        "選択肢1和訳→正解。💡 本文の根拠英文が直接の根拠",
                        "選択肢2和訳→不正解の理由",
                        "選択肢3和訳→不正解の理由",
                        "選択肢4和訳→不正解の理由"
                    ],
                    "grammar": "💡 ..."
                }
            ]
        },
        {
            "label": "B",
            "title": "タイトル",
            "paragraphs": ["段落1", "段落2", "段落3"],
            "translations": ["和訳1", "和訳2", "和訳3"],
            "sentencePairs": [["en", "ja"]],
            "questions": [
                {
                    "number": 26,
                    "question": "質問テキスト",
                    "questionTranslation": "質問の日本語訳",
                    "choices": ["A", "B", "C", "D"],
                    "choiceTranslations": ["選択肢1和訳", "選択肢2和訳", "選択肢3和訳", "選択肢4和訳"],
                    "answer": 2,
                    "choiceAnalysis": [
                        "選択肢1和訳→不正解の理由",
                        "選択肢2和訳→正解。💡 本文の根拠英文が直接の根拠",
                        "選択肢3和訳→不正解の理由",
                        "選択肢4和訳→不正解の理由"
                    ],
                    "grammar": "💡 ..."
                }
            ]
        }
    ]
}
```

**大問4の特徴:**
- パッセージA: email形式（`format: "email"`, `meta`あり）、3問
- パッセージB: 一般長文、4問
- 2級の大問3と同じ構造

### 2g. プロ講師のアドバイス（解説）品質ガイドライン

> **⚠ 全問に `choiceAnalysis` と `grammar` を必ず追加すること。欠落は検証で不合格になる。**

#### 大問1（vocabulary型・単語選択）の解説形式

```json
"choiceAnalysis": [
    "❌ architect＝建築家。新聞社の編集職とは無関係",
    "❌ engineer＝技術者。記事を決める仕事ではない",
    "✅ editor＝編集者。記事の掲載を決めるのが仕事→正解",
    "❌ astronaut＝宇宙飛行士。全く関係ない"
],
"grammar": "💡 editor＝編集者。edit（動詞：編集する）の名詞形。edition＝版。"
```

**ルール:**
- 正解: `"✅ 単語＝意味。正解の理由→正解"`
- 不正解: `"❌ 単語＝意味。不正解の理由"`
- grammar: `"💡 重要表現の解説（類義語・反意語・用法のポイント）"`

#### 大問2（vocabulary型・会話文の文選択）の解説形式

> **⚠ 大問2の選択肢は文レベルなので、choiceTranslationsで和訳が表示される。choiceAnalysisでは英文を繰り返さず、和訳→理由の形式にする。**

```json
"choiceAnalysis": [
    "長くいられない→正解。💡 5:30に帰ると言っているので文脈に最適",
    "昼食の時間がない→放課後の文脈に合わない",
    "特にすることがない→帰る必要がある会話に矛盾",
    "この町を出る→大げさすぎる"
],
"grammar": "💡 won't be able to ～＝～できないだろう。will not + be able toで未来の能力・可能性を否定"
```

**ルール:**
- 正解: `"和訳→正解。💡 根拠"`
- 不正解: `"和訳→不正解の理由（簡潔に）"`
- grammar: `"💡 重要表現の解説"`

#### 大問3・大問4（passage-fill / reading-comprehension型）の解説形式

```json
"questionTranslation": "設問の日本語訳",
"choiceTranslations": [
    "選択肢1の日本語訳。",
    "選択肢2の日本語訳。",
    "選択肢3の日本語訳。",
    "選択肢4の日本語訳。"
],
"choiceAnalysis": [
    "選択肢1和訳→不正解の理由",
    "選択肢2和訳→正解。💡 本文の根拠となる英文が直接の根拠",
    "選択肢3和訳→不正解の理由",
    "選択肢4和訳→不正解の理由"
],
"grammar": "💡 設問タイプの解法アドバイス（例: Why問題は目的を問う→本文冒頭の表現に着目）"
```

**ルール:**
- `choiceTranslations`: 各選択肢の日本語訳を配列で追加（和訳ON時に各選択肢の下に表示）
- `questionTranslation`: 設問文の日本語訳
- 正解: `"和訳→正解。💡 本文中の根拠英文が直接の根拠"`
- 不正解: `"和訳→不正解の理由（簡潔に）"`
- grammar: `"💡 設問タイプ別の解法アドバイス"`
- ★ `choiceAnalysis`の正解の行には「✅」「❌」を使わず、「→正解。💡」形式を使う

### 2h. スクリプト実行と保存

```python
import os
output_dir = r"g:\マイドライブ\ReadPass Pro\data\grade-pre2\YYYY-S"
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
    "id": "fp1",
    "title": "構文名",
    "subtitle": "English Subtitle",
    "explanation": "解説文",
    "sourceQuote": "出典箇所の引用",
    "sourceLocation": "Part 3 第1段落",
    "examples": [
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
    "highlightPatterns": [
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

**✅ 準2級向けFPタイトル例（文法・構文）：**
- 接続詞 because / when / if の基本用法
- 比較級・最上級の表現
- 不定詞の名詞用法・形容詞用法
- 動名詞と不定詞の使い分け
- 受動態の基本パターン
- 関係代名詞 who / which / that
- 時制の一致と過去形・現在完了形
- there is/are 構文と存在表現
- 助動詞の基本用法 can / should / have to

**❌ 不可なFPタイトルの例（内容・語彙ベース）：**
- ~~ビーバーの生態と環境への影響~~
- ~~メール返信の書き方~~
- ~~スペインの文化と友情~~

#### ★★★ practicePassage 必須ルール（最重要）★★★

> **⚠ 全5つのFPに必ず `practicePassage`（en/ja）と `practiceQuestions`（3〜4問）を含めること。欠落は検証で不合格になる。**

- 各パッセージは **5〜7文** の短いパラグラフ（本文とは異なるオリジナルトピック）
- 当該FPの文法・構文が **自然に複数回使われている** こと
- 英語＋日本語訳のペア
- 3〜4個の `practiceQuestions` と対にする
- **準2級レベルの語彙・文法で書くこと**（準1級レベルの高度な表現は避ける）

### 3c. highlightPatterns の品質基準

- **フレーズレベル**のハイライト（単語1つだけではなく、文脈のある長いフレーズ）
- 各FPにつき **8〜12パターン** を目標（準2級は大問3が1パッセージのため少なめ）
- 大問3と大問4の両方のパッセージからパターンを抽出

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

`g:\マイドライブ\ReadPass Pro\top.js` の `EXAM_CATALOG` の `grade-pre2` エントリに試験を追加。

**並び順ルール: 古い試験が上、新しい試験が下**

```javascript
{
    id: 'grade-pre2',
    name: 'CEFR A2（準2級相当）',
    nameEn: 'CSE 1728',
    icon: 'A2',
    color: '#10b981',
    colorRgb: '16, 185, 129',
    dataPath: 'grade-pre2',
    exams: [
        { id: '2025-3', label: '2025年度 第3回', sub: '一次試験リーディング' }
    ]
}
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
    if len(vocab) < 40:
        errors.append(f"vocabulary count = {len(vocab)}, must be 40+")

    # 2. sections チェック（準2級は4つのsection）
    sections = d.get("sections", [])
    if len(sections) != 4:
        errors.append(f"sections count = {len(sections)}, expected 4")
    expected_types = ["vocabulary", "vocabulary", "passage-fill", "reading-comprehension"]
    for i, s in enumerate(sections):
        if i < len(expected_types) and s.get("type") != expected_types[i]:
            errors.append(f"Section {i}: type='{s.get('type')}', expected '{expected_types[i]}'")

    # 3. 問題数チェック（29問）
    total_q = 0
    for s in sections:
        total_q += len(s.get("questions", []))
        for p in s.get("passages", []):
            total_q += len(p.get("questions", []))
    if total_q != 29:
        errors.append(f"Total questions = {total_q}, expected 29")

    # 4. 大問1: 15問, 大問2: 5問
    if len(sections) >= 2:
        q1 = len(sections[0].get("questions", []))
        q2 = len(sections[1].get("questions", []))
        if q1 != 15:
            errors.append(f"大問1: {q1} questions, expected 15")
        if q2 != 5:
            errors.append(f"大問2: {q2} questions, expected 5")

    # 5. focusPoints チェック
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
            errors.append(f"FP{i+1}: only {len(hp)} highlight patterns (recommend 8-12)")

    # 6. sentencePairs チェック
    for s in sections:
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND in passage: '{pair[0][:50]}...'")

    # 7. answer 範囲チェック (1-indexed: 1-4)
    for s in sections:
        qs = list(s.get("questions", []))
        for p in s.get("passages", []):
            qs += list(p.get("questions", []))
        for q in qs:
            a = q.get("answer")
            if a is not None and (a < 1 or a > 4):
                errors.append(f"Q{q.get('number')}: answer={a} out of range 1-4")
            if not q.get("choiceAnalysis"):
                errors.append(f"Q{q.get('number')}: missing choiceAnalysis")
            if not q.get("grammar"):
                errors.append(f"Q{q.get('number')}: missing grammar")

    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, focusPoints={len(fps)}")

    if errors:
        print("⚠ VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ ALL CHECKS PASSED")

verify(r"g:\マイドライブ\ReadPass Pro\data\grade-pre2\YYYY-S\data.json")
```

### 5b. ブラウザ検証チェックリスト

| # | テスト項目 | 確認手順 |
|---|-----------| ---------|
| 1 | トップページ表示 | `localhost:8085/top.html` → 準2級が表示される |
| 2 | 単語タブ | 4択クイズが全40語以上表示される |
| 3 | 大問1タブ | 15問の空所補充が表示される |
| 4 | 大問2タブ | 5問の会話文空所補充が表示される |
| 5 | 大問3タブ | 1パッセージ＋2問が表示される |
| 6 | 大問4タブ | 2パッセージ（email＋一般）＋7問が表示される |
| 7 | 文法タブ | 5つのfocusPointカード＋practicePassageが表示される |
| 8 | 文訳ポップアップ | 大問3/4の本文をクリック → 和訳が表示される |
| 9 | マーカーON | ツールバー「文法マーカー」→ 5色のハイライトが表示される |
| 10 | 凡例個別トグル | 凡例の各項目をクリック → 該当色のみON/OFF |
| 11 | 正解表示/非表示 | ツールバーで切替 → 正解バッジの表示/非表示 |
| 12 | 印刷メニュー | 印刷ボタン → メニューが表示される |
| 13 | 単語カード | ツールバー → 別ウィンドウで単語カードが開く |
| 14 | ライトモード | テーマ切替 → ハイライト・凡例が見やすい |

---

## 過去の落とし穴と対策一覧

| 問題 | 原因 | 対策 |
|------|------|------|
| 凡例の個別選択不可 | focusPoints に `"id"` キーがない | **各FPに必ず `"id": "fp1"` ~ `"fp5"` を付ける** |
| 文法タブが空白 | キー名の不一致（`why`/`exampleSentences`） | `explanation`, `examples`, `practiceQuestions` を使う |
| 各タブが空白になる | `sections.type` の値が間違っている | `vocabulary`, `passage-fill`, `reading-comprehension` を正確に |
| ハイライトが薄い | パターンが単語1つだけ | フレーズレベル（8-12パターン）で設定する |
| 単語が大問1に偏る | P3/P4パッセージからの抽出漏れ | **大問3から5-8語、大問4から10-15語を必ず抽出する** |
| FPが内容ベース | 語彙・トピックテーマのFPを作った | **FP1-4は文法構文トピックのみ。語彙/テーマ名は不可** |
| FP5がパラフレーズでない | FP5にも文法トピックを入れた | **FP5は必ず「今回の重要なパラフレーズ」固定** |
| 前置詞単体が単語カードに出る | `on` のように前置詞1語だけをwordに入れた | **`laugh at` のようにフレーズ全体を入れる** |
| **練習パッセージが表示されない** | `practicePassage` キーが欠落 | **全5 FPに必ず `practicePassage`（en/ja）を追加** |
| **確認問題が空** | `practiceQuestions` が無い or 0件 | **全5 FPに3〜4問の `practiceQuestions` を追加** |
| 文訳ポップアップが壊れる | 翻訳テキストを `data-trans` 属性に直接格納 | `data-tidx` でインデックス参照方式を使う（app.js側対応済み） |
| 文分割の誤り | `Mr.` 等の略語でピリオド分割 | `sentencePairs` で英文を明示指定、`indexOf()` でマッチ |
| **解説が表示されない** | `choiceAnalysis`/`grammar` が欠落 | **全29問に必ず `choiceAnalysis`（✅/❌配列）と `grammar`（💡文）を追加** |
| **大問4のタブがない** | app.jsが3タブ固定だった | **動的タブ生成に改修済み（2025-3以降対応済）** |

---

## ファイル構成

```
g:\マイドライブ\ReadPass Pro\
├── top.js            ← EXAM_CATALOG の grade-pre2 にエントリ追加
├── app.js            ← 変更不要（共通ロジック）
├── index.html        ← 変更不要
├── style.css         ← 変更不要
├── vocab-cards.html  ← 変更不要
└── data/
    └── grade-pre2/
        └── {exam_id}/
            └── data.json   ← Step 2-3 で生成
```
