---
description: 準2級プラスのリーディング過去問をReadPass Proに追加する
---

# ReadPass Pro — 準2級プラス 新規試験追加ワークフロー

// turbo-all

## 概要
英検準2級プラスのリーディング過去問PDFから `data.json` を生成し、ReadPass Pro に新しい試験回を追加するための完全手順。
**このワークフローを上から順に実行すれば、一発で確実に実装できる。**

---

## 2級との主な差異

| 項目 | 2級 | 準2級プラス |
|------|-----|-------------|
| 語彙数 | 51語以上 | **55語（固定）** |
| 大問1 | 17問 | **17問（語彙・文法）** |
| 大問2 | 6問（2パッセージ） | **6問（2パッセージ）** |
| 大問3 | 8問（2パッセージ、A=email可） | **8問（2パッセージ、A=email可）** |
| 合計 | 31問 | **31問** |
| choiceAnalysis | P1のみ | **全31問（P1/P2/P3）** |
| sourceEvidence | なし | **P2/P3の全問に必須** |
| 選択肢和訳 | なし | **choiceTranslations（P2/P3）** |
| 設問和訳 | なし | **questionTranslation（P3のみ）** |
| grammar ノート | なし | **P1の全問に💡付き解説** |
| データパス | `data/grade2/` | **`data/grade-pre2plus/`** |
| GRADE_MAP | `grade2` | **`grade-pre2plus`** |

---

## 前提条件

- 過去問PDFが `G:\マイドライブ\text\bookshelf\英検過去問\準2級プラス\準2級プラス{year}-{session}\` に配置済み
- 出力先: `g:\マイドライブ\ReadPass Pro\data\grade-pre2plus\{exam_id}\data.json`
  - `exam_id` は `{year}-{session}` 形式（例: `2025-3`）
  - 土曜日開催は `{year}-{session}-sat`（例: `2025-1-sat`）
- 開発サーバ: `npx -y http-server "g:\マイドライブ\ReadPass Pro" -p 8765 --cors`

---

## Step 0: 既存データの確認（重複回避）

1. `g:\マイドライブ\ReadPass Pro\data\grade-pre2plus\` 配下の全 `data.json` を確認
2. 既存試験回の `lessonPlan.focusPoints` タイトル一覧を取得
3. **新規試験のFP1-4は、既存試験と文法トピックが重複しないようにする**

```python
import json, os
base = r"g:\マイドライブ\ReadPass Pro\data\grade-pre2plus"
for exam in sorted(os.listdir(base)):
    path = os.path.join(base, exam, "data.json")
    if os.path.exists(path):
        d = json.load(open(path, "r", encoding="utf-8"))
        fps = d.get("lessonPlan", {}).get("focusPoints", [])
        print(f"\n{exam}: vocab={len(d.get('vocabulary',[]))}")
        for fp in fps:
            print(f"  {fp.get('id','?')}: {fp.get('title','?')}")
```

---

## Step 1: PDF テキスト抽出

PyMuPDF で各ページのテキストを抽出する。

```python
import fitz, sys, os
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"G:\マイドライブ\text\bookshelf\英検過去問\準2級プラス\準2級プラスYYYY-S\問題.pdf"  # パス調整
output_dir = r"G:\マイドライブ\text\bookshelf\英検過去問\準2級プラス\準2級プラスYYYY-S\new problem"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
```

**ページ構成（準2級プラス標準）:**
| ページ | 内容 |
|--------|------|
| 3-6 | Part 1（語彙・文法 17問） |
| 7-8 | Part 2（長文穴埋め 2パッセージ 6問） |
| 9-12 | Part 3（長文読解 2パッセージ 8問） |
| 13+ | Writing / Summary（参考用） |

---

## Step 2: data.json 生成スクリプト作成

**必ずPythonスクリプトで生成する**（手動編集は誤りの原因）。
スクリプトは `C:\tmp\gen_pre2p_{exam_id}.py` に作成する。

### 2a. トップレベル構造

```python
import json

data = {
    "grade": "準2級プラス",
    "year": "YYYY",
    "session": "S",
    "title": "YYYY年度 第S回 英検準2級プラス リーディング",
    "vocabulary": [],  # Step 2b で追加
    "sections": [],    # Step 2c-2e で追加
    "lessonPlan": {}   # Step 3 で追加
}
```

### 2b. vocabulary 配列（★55語固定・全大問から均等抽出）

各単語は以下の形式:
```json
{
    "word": "refuse",
    "meaning": "拒否する",
    "pos": "動詞",
    "level": "準2級プラス",
    "example": "She refused to accept the offer.",
    "distractors": ["同意する", "提案する", "計画する"],
    "source": "大問1"
}
```

#### ★★★ 語彙抽出ルール（最重要）★★★

> **⚠ 大問1だけから単語を抽出してはならない。必ず大問2・大問3のパッセージからもバランスよく抽出すること。**

| 抽出元 | 目標語数 | 説明 |
|--------|----------|------|
| 大問1（語彙・文法） | 20〜25語 | 選択肢の正答＋重要な誤答から抽出 |
| 大問2（長文穴埋め） | 15〜18語 | パッセージ A・B の本文中の重要語を抽出 |
| 大問3（長文読解） | 15〜18語 | パッセージ A・B の本文中の重要語を抽出 |
| **合計** | **55語（固定）** | 全大問からバランスよく収録 |

- **P2/P3からの抽出を忘れると検証で不合格になる（過去の頻発ミス）**
- `level` は `"準2級プラス"` を使う
- `source` にどの大問から取ったか記録（例: `"大問1"`, `"大問2A"`, `"大問3B"`）
- 熟語（句動詞）もフレーズ全体を `word` に入れる（例: `"put on"`, `"give away"`）
- **example は試験本文とは異なるオリジナル例文を作成する**
- `distractors` は意味が紛らわしい3つの誤選択肢（和訳）

### 2c. Section 0: 大問1（vocabulary 型・17問）

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
            "answer": 4,
            "choiceAnalysis": [
                "❌ gained＝得た",
                "❌ chased＝追いかけた",
                "❌ seated＝座らせた",
                "✅ refused＝拒否した。皿洗いを拒否→母が怒った"
            ],
            "grammar": "💡 refuse to do＝～することを拒否する。decline（類義語）。"
        }
    ]
}
```

**注意:**
- `answer` は **1-indexed**（正答表の番号そのまま使う）
- キー名は `choices`（`options` は不可）、`answer`（`correctAnswer` は不可）
- `translation` キーで和訳を追加
- `grammar` キーで 💡 付きの文法ノートを追加（★準2級プラスでは必須）
- `choiceAnalysis` で各選択肢の解説（✅正解、❌不正解）

### 2d. Section 1: 大問2（passage-fill 型・6問）

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
                    "choiceTranslations": ["和訳1", "和訳2", "和訳3", "和訳4"],
                    "answer": 4,
                    "choiceAnalysis": [
                        "❌ On the other hand=一方で→逆接ではない",
                        "❌ Moreover=さらに→追加情報ではなく因果関係",
                        "❌ To be sure=確かに→譲歩ではない",
                        "✅ Therefore=したがって→正解。因果関係"
                    ],
                    "sourceEvidence": [
                        "a terrible disease was causing problems",
                        "the original purpose was to improve people's lives"
                    ]
                }
            ]
        }
    ]
}
```

**★ 2級との違い:**
- `choiceTranslations`: 各選択肢の和訳配列（和訳ONで表示）
- `choiceAnalysis`: 各選択肢の解説（正解表示ONで表示）
- `sourceEvidence`: 正解解説クリック時に本文でハイライトされる根拠テキスト配列

### 2e. Section 2: 大問3（reading-comprehension 型・8問）

```json
{
    "name": "大問3",
    "nameEn": "Part 3",
    "type": "reading-comprehension",
    "instruction": "次の英文A，Bの内容に関して，(24)から(31)までの質問に対して最も適切なものを選びなさい。",
    "passages": [
        {
            "label": "A",
            "title": "Writing Contest",
            "format": "email",
            "meta": {
                "from": "Jacob Francis <general@queens-fall.com>",
                "to": "Maria Stone <maria.stone.123@ocean-network.com>",
                "date": "November 12",
                "subject": "Writing contest"
            },
            "paragraphs": ["段落1", "段落2", "段落3"],
            "translations": ["和訳1", "和訳2", "和訳3"],
            "sentencePairs": [["en", "ja"]],
            "questions": [
                {
                    "number": 24,
                    "question": "Why did Jacob Francis send an e-mail?",
                    "questionTranslation": "ジェイコブがメールを送った理由は？",
                    "choices": ["A", "B", "C", "D"],
                    "choiceTranslations": ["和訳A", "和訳B", "和訳C", "和訳D"],
                    "answer": 2,
                    "choiceAnalysis": [
                        "❌ 不正解の理由...",
                        "✅ 正解の根拠...",
                        "❌ 不正解の理由...",
                        "❌ 不正解の理由..."
                    ],
                    "sourceEvidence": ["the essay you wrote has been chosen for the first prize"]
                }
            ]
        }
    ]
}
```

**★ 大問3の特徴:**
- `questionTranslation`: 設問の和訳（和訳ONで表示）
- `choiceTranslations`: 各選択肢の和訳
- `sourceEvidence`: 正解行クリック→本文の根拠箇所をハイライト
- Part 3A: email形式可（`format: "email"` + `meta` オブジェクト）。3段落＋3問
- Part 3B: 通常形式。4段落＋5問が標準

### 2f. スクリプト実行と保存

```python
import os
output_dir = r"g:\マイドライブ\ReadPass Pro\data\grade-pre2plus\YYYY-S"
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
    "sourceLocation": "Part 2A 第1段落",
    "examples": [
        {
            "en": "Example sentence.",
            "ja": "例文和訳。",
            "note": "文法解説ノート"
        }
    ],
    "practicePassage": {
        "en": "Practice paragraph in English...",
        "ja": "練習パッセージ和訳..."
    },
    "practiceQuestions": [
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

**✅ 準2級プラス向けFPタイトル例（文法・構文）：**
- 因果関係の接続表現（Cause & Effect Connectors）
- 否定・譲歩の表現（Negation & Concession Patterns）
- 比較・程度を表す表現（Comparison & Degree Expressions）
- 条件文と仮定表現（Conditionals & Hypothetical Expressions）
- 受動態の多様な用法（Various Passive Constructions）
- 逆接・対比の接続表現（Contrast & Opposition Connectors）
- 追加・補足の接続表現（Addition & Supplementation）
- 関係代名詞と修飾構造（Relative Pronouns & Modification）
- 目的・理由を表す表現（Purpose & Reason Expressions）
- 依頼・提案の丁寧表現（Polite Requests & Suggestions）
- メール文の定型表現と依頼パターン（Email Conventions）
- 論理展開の接続表現（Logical Development Connectors）

**❌ 不可なFPタイトルの例（内容・語彙ベース）：**
- ~~オリーブオイル産業の語彙~~
- ~~ホッキョクグマの生態用語~~

### 3c. practicePassage の品質基準（★重要）

各FPには**オリジナルの練習パッセージ**を必ず含める。パッセージは：
- 5〜7文の短いパラグラフ（本文とは異なるトピック）
- 当該FPの文法・構文が自然に複数回使われている
- 英語＋日本語訳のペア
- 3〜4個の `practiceQuestions` と対にする

### 3d. highlightPatterns の品質基準

- **フレーズレベル**のハイライト（単語1つだけではなく、文脈のある長いフレーズ）
- 各FPにつき **5〜15パターン** を目標
- 大問1〜3の各パートからパターンを抽出

### 3e. highlightColor の標準色

| FP | 色名 | HEX値 |
|----|------|-------|
| fp1 | Blue | `#4f8cff` |
| fp2 | Pink | `#f472b6` |
| fp3 | Green | `#34d399` |
| fp4 | Yellow/Amber | `#fbbf24` |
| fp5 | Orange | `#f59e0b` |

### 3f. FP5（パラフレーズ）の固定ルール

- `title`: `"今回の重要なパラフレーズ"`
- `subtitle`: `"Key Paraphrases in This Exam"`
- `sourceQuote`: 番号付き（①②③…）で各パラフレーズペアを `\n` 区切り
- `examples`: 一般的なパラフレーズ例文を3つ
- `practicePassage`: パラフレーズ練習用のオリジナルパッセージ
- `practiceQuestions`: 4問（「～を言い換えると？」形式）
- `highlightColor`: `"#f59e0b"`
- `highlightLabel`: `"パラフレーズ"`

---

## Step 4: top.js にエントリ追加

`g:\マイドライブ\ReadPass Pro\top.js` の `EXAM_CATALOG` に新しい試験を追加。

**並び順ルール: 古い試験が上、新しい試験が下。土曜日は本試験の直後。**

```javascript
{
    id: 'grade-pre2plus',
    name: 'Pre-Grade 2 Plus',
    cefr: 'CEFR A2-B1',
    color: '#7c3aed',
    path: 'grade-pre2plus',
    exams: [
        { id: '2025-1', label: '2025年度 第1回', sub: '一次試験リーディング' },
        { id: '2025-1-sat', label: '2025年度 第1回（土曜）', sub: '一次試験リーディング' },
        { id: '2025-2', label: '2025年度 第2回', sub: '一次試験リーディング' },
        { id: '2025-2-sat', label: '2025年度 第2回（土曜）', sub: '一次試験リーディング' },
        { id: '2025-3', label: '2025年度 第3回', sub: '一次試験リーディング' },
        { id: '2025-3-sat', label: '2025年度 第3回（土曜）', sub: '一次試験リーディング' }
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
    if len(vocab) != 55:
        errors.append(f"vocabulary count = {len(vocab)}, must be 55")

    # 2. sections チェック
    types = {s["type"] for s in d.get("sections", [])}
    for t in ["vocabulary", "passage-fill", "reading-comprehension"]:
        if t not in types:
            errors.append(f"Missing section type: {t}")

    # 3. 問題数チェック
    total_q = 0
    for s in d.get("sections", []):
        total_q += len(s.get("questions", []))
        for p in s.get("passages", []):
            total_q += len(p.get("questions", []))
    if total_q != 31:
        errors.append(f"Total questions = {total_q}, expected 31")

    # 4. choiceAnalysis チェック（全問必須）
    ca_count = 0
    for s in d.get("sections", []):
        for q in s.get("questions", []):
            if "choiceAnalysis" in q: ca_count += 1
            else: errors.append(f"Q{q.get('number')}: missing choiceAnalysis")
        for p in s.get("passages", []):
            for q in p.get("questions", []):
                if "choiceAnalysis" in q: ca_count += 1
                else: errors.append(f"Q{q.get('number')}: missing choiceAnalysis")

    # 5. sourceEvidence チェック（P2/P3の全問必須）
    ev_count = 0
    for s in d.get("sections", []):
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                for q in p.get("questions", []):
                    if "sourceEvidence" in q:
                        ev_count += 1
                    else:
                        errors.append(f"Q{q.get('number')}: missing sourceEvidence")

    # 6. P1 grammar チェック
    for s in d.get("sections", []):
        if s["type"] == "vocabulary":
            for q in s.get("questions", []):
                if "grammar" not in q:
                    errors.append(f"Q{q.get('number')}: missing grammar (💡 note)")

    # 7. P2 choiceTranslations チェック
    for s in d.get("sections", []):
        if s["type"] == "passage-fill":
            for p in s.get("passages", []):
                for q in p.get("questions", []):
                    if "choiceTranslations" not in q:
                        errors.append(f"Q{q.get('number')}: missing choiceTranslations")

    # 8. P3 questionTranslation / choiceTranslations チェック
    for s in d.get("sections", []):
        if s["type"] == "reading-comprehension":
            for p in s.get("passages", []):
                for q in p.get("questions", []):
                    if "questionTranslation" not in q:
                        errors.append(f"Q{q.get('number')}: missing questionTranslation")
                    if "choiceTranslations" not in q:
                        errors.append(f"Q{q.get('number')}: missing choiceTranslations")

    # 9. focusPoints チェック
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5:
        errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        if "id" not in fp:
            errors.append(f"FP{i+1}: missing 'id'")
        for key in ["explanation", "examples", "practicePassage", "practiceQuestions", "highlightPatterns", "highlightColor", "highlightLabel"]:
            if key not in fp:
                errors.append(f"FP{i+1} '{fp.get('title','')}': missing '{key}'")

    # 10. sentencePairs チェック
    for s in d.get("sections", []):
        if s["type"] in ["passage-fill", "reading-comprehension"]:
            for p in s.get("passages", []):
                sp = p.get("sentencePairs", [])
                if not sp:
                    errors.append(f"Passage '{p.get('title','')}': NO sentencePairs")
                text = " ".join(p.get("paragraphs", []))
                for pair in sp:
                    if pair[0] not in text:
                        errors.append(f"sentencePair NOT FOUND: '{pair[0][:50]}...'")

    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, choiceAnalysis={ca_count}, sourceEvidence={ev_count}")

    if errors:
        print("⚠ VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ ALL CHECKS PASSED")

verify(r"g:\マイドライブ\ReadPass Pro\data\grade-pre2plus\YYYY-S\data.json")
```

### 5b. ブラウザ検証チェックリスト

| # | テスト項目 | 確認手順 |
|---|-----------|---------|
| 1 | トップページ表示 | `localhost:8765/top.html` → Pre-Grade 2 Plus が表示される |
| 2 | 単語タブ | 4択クイズが全55語表示される |
| 3 | 大問1タブ | 17問の空所補充＋choiceAnalysis＋grammar表示 |
| 4 | 大問2タブ | 2つのパッセージ＋6問＋choiceTranslations表示 |
| 5 | 大問3タブ | 2つのパッセージ＋8問＋questionTranslation表示 |
| 6 | 文法タブ | 5つのfocusPointカード＋練習パッセージ＋確認問題表示 |
| 7 | 文訳ポップアップ | 大問2/3の本文をクリック → 和訳が表示される |
| 8 | マーカーON | ツールバー「文法マーカー」→ 5色のハイライトが表示 |
| 9 | **根拠ハイライト** | 正解の緑テキストをクリック → 本文が黄色ハイライト＋自動スクロール |
| 10 | **和訳ON** | 和訳ON → P2選択肢和訳＋P3設問和訳＋選択肢和訳がトーンダウンで表示 |
| 11 | 印刷メニュー | 印刷ボタン → メニューが表示される |
| 12 | ライトモード | テーマ切替 → ハイライト・凡例が見やすい |
| 13 | 単語カード | ツールバー → 別ウィンドウで単語カードが開く |

---

## 過去の落とし穴と対策一覧

| 問題 | 原因 | 対策 |
|------|------|------|
| 凡例の個別選択不可 | focusPoints に `"id"` キーがない | **各FPに必ず `"id": "fp1"` ~ `"fp5"` を付ける** |
| 文法タブが空白 | キー名の不一致 | `explanation`, `examples`, `practiceQuestions` を使う |
| 練習パッセージが表示されない | `practicePassage` キーがない | **各FPに必ず `practicePassage` を追加（en/ja）** |
| 根拠ハイライトが動かない | `sourceEvidence` が未設定 | P2/P3の全問に `sourceEvidence` を含める |
| 選択肢和訳が表示されない | `choiceTranslations` がない | P2/P3の全問に `choiceTranslations` を追加 |
| 単語が大問1に偏る | P2/P3パッセージからの抽出漏れ | **大問2から15-18語、大問3から15-18語を必ず抽出する** |
| FPが内容ベース | 語彙・トピックテーマのFPを作った | **FP1-4は文法構文トピックのみ。語彙/テーマ名は不可** |
| FP5がパラフレーズでない | FP5にも文法トピックを入れた | **FP5は必ず「今回の重要なパラフレーズ」固定** |
| 語彙数が55でない | 重複単語の追加や抽出漏れ | **検証スクリプトで `!= 55` をチェックする** |

---

## ファイル構成

```
g:\マイドライブ\ReadPass Pro\
├── top.js            ← EXAM_CATALOG にエントリ追加
├── app.js            ← 変更不要（共通ロジック）
├── index.html        ← 変更不要
├── style.css         ← 変更不要
├── vocab-cards.html  ← 変更不要
└── data/
    └── grade-pre2plus/
        ├── 2025-1/
        │   └── data.json
        ├── 2025-1-sat/
        │   └── data.json
        ├── 2025-2/
        │   └── data.json
        ├── 2025-2-sat/
        │   └── data.json
        ├── 2025-3/
        │   └── data.json
        └── 2025-3-sat/
            └── data.json
```
