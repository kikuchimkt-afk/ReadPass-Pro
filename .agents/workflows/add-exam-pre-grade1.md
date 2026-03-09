---
description: 準1級のリーディング過去問をReadPass Proに追加する
---

# ReadPass Pro — 準1級 新規試験追加ワークフロー

// turbo-all

## 概要
英検準1級のリーディング過去問PDFから `data.json` を生成し、ReadPass Pro に新しい試験回を追加するための完全手順。
**このワークフローを上から順に実行すれば、一発で確実に実装できる。**

---

## 2級との主な差異

| 項目 | 2級 | 準1級 |
|------|-----|-------|
| 語彙数 | 51語以上 | **80語以上（準1レベル優先）** |
| 大問1 | 17問 | **18問（短文空所補充）** |
| 大問2 | 6問（2パッセージ） | **6問（2パッセージ）** |
| 大問3 | 8問（2パッセージ、A=email可） | **7問（2パッセージ、email形式なし）** |
| 合計 | 31問 | **31問** |
| choiceAnalysis | あり | **あり＋sourceEvidence（根拠ハイライト）** |
| 選択肢和訳 | なし | **choiceTranslations必須（P2/P3）** |
| 設問和訳 | なし | **questionTranslation必須（P3）** |
| データパス | `data/grade2/` | **`data/pre-grade1/`** |
| GRADE_MAP | `grade2` | **`pre-grade1`** |

---

## 前提条件

- 過去問PDFが `G:\マイドライブ\text\bookshelf\英検過去問\準1級\準1級{year}-{session}\` に配置済み
- 出力先: `g:\マイドライブ\eiken practice\data\pre-grade1\{exam_id}\data.json`
  - `exam_id` は `{year}-{session}` 形式（例: `2025-3`）
- 開発サーバ: `npx -y http-server "g:\マイドライブ\eiken practice" -p 8085 -c-1`

---

## Step 0: 既存データの確認（重複回避）

1. `g:\マイドライブ\eiken practice\data\pre-grade1\` 配下の全 `data.json` を確認
2. 既存試験回の `lessonPlan.focusPoints` タイトル一覧を取得
3. **新規試験のFP1-4は、既存試験と文法トピックが重複しないようにする**

```python
import json, os
base = r"g:\マイドライブ\eiken practice\data\pre-grade1"
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

pdf_path = r"G:\マイドライブ\text\bookshelf\英検過去問\準1級\準1級YYYY-S\問題.pdf"  # パス調整
output_dir = r"G:\マイドライブ\text\bookshelf\英検過去問\準1級\準1級YYYY-S\new problem"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    text = doc[i].get_text()
    with open(os.path.join(output_dir, f"page_{i+1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Page {i+1}: {len(text)} chars")
doc.close()
```

**ページ構成（準1級標準）:**
| ページ | 内容 |
|--------|------|
| 3-7 | Part 1（語彙 18問） |
| 8-9 | Part 2（長文穴埋め 2パッセージ 6問） |
| 10-13 | Part 3（長文読解 2パッセージ 7問） |
| 14+ | Writing / Summary（参考用） |

---

## Step 2: data.json 生成スクリプト作成

**必ずPythonスクリプトで生成する**（手動編集は誤りの原因）。
スクリプトは `C:\tmp\gen_p1kyu_{exam_id}.py` に作成する。

### 2a. トップレベル構造

```python
import json

data = {
    "grade": "準1級",
    "year": "YYYY",
    "session": "S",
    "title": "YYYY年度 第S回 英検準1級 リーディング",
    "vocabulary": [],  # Step 2b で追加
    "sections": [],    # Step 2c-2e で追加
    "lessonPlan": {}   # Step 3 で追加
}
```

### 2b. vocabulary 配列（★80語以上・準1レベル優先・全大問から均等抽出）

各単語は以下の形式:
```json
{
    "word": "evade",
    "meaning": "～を巧みに逃れる",
    "pos": "動詞",
    "level": "準1級",
    "example": "The spy managed to evade capture for months.",
    "distractors": ["～を追跡する", "～を発見する", "～に従う"]
}
```

#### ★★★ 語彙抽出ルール（最重要）★★★

> **⚠ 大問1だけから単語を抽出してはならない。必ず大問2・大問3のパッセージからもバランスよく抽出すること。**

| 抽出元 | 目標語数 | 説明 |
|--------|----------|------|
| 大問1（語彙） | 35〜45語 | 選択肢の正答＋重要な誤答から抽出 |
| 大問2（長文穴埋め） | 15〜20語 | パッセージ A・B の本文中の重要語を抽出 |
| 大問3（長文読解） | 15〜20語 | パッセージ A・B の本文中の重要語を抽出 |
| **合計** | **80語以上** | 準1級レベル優先で全大問からバランスよく |

- **P2/P3からの抽出を忘れると検証で不合格になる（過去の頻発ミス）**
- `level` は `"準1級"` または `"2級上位"` を使う（準1レベル優先）
- 熟語（句動詞）も `"make for"` `"take on"` のようにフレーズ全体を `word` に入れる
- **example は試験本文とは異なるオリジナル例文を作成する**
- `distractors` は意味が紛らわしい3つの誤選択肢（和訳）

### 2c. Section 0: 大問1（vocabulary 型・18問）

```json
{
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(18)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": [
        {
            "number": 1,
            "text": "問題文 ( 1 ) を含むテキスト",
            "translation": "和訳テキスト",
            "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
            "answer": 1,
            "grammar": "💡 evade は「巧みに逃れる」。escape from prison の後、evade the police の流れが自然。",
            "choiceAnalysis": [
                "✅ evaded＝巧みに逃れた。文脈に最適",
                "❌ sterilized＝殺菌した。医療文脈で不適切",
                "❌ wrecked＝破壊した。文脈に合わない",
                "❌ commuted＝通勤した。文が成立しない"
            ]
        }
    ]
}
```

**注意:**
- `answer` は **1-indexed**（正答表の番号そのまま使う）
- キー名は `choices`（`options` は不可）、`answer`（`correctAnswer` は不可）
- `translation` キーで和訳を追加
- `grammar` キーで 💡 付きの文法ノートを追加（★2級にはないが準1級では必須）
- `choiceAnalysis` で各選択肢の解説（✅正解、❌不正解）

### 2d. Section 1: 大問2（passage-fill 型・6問）

```json
{
    "name": "大問2",
    "nameEn": "Part 2",
    "type": "passage-fill",
    "instruction": "次の英文A，Bを読み，その文意にそって(19)から(24)までの(　)に入れるのに最も適切なものを選びなさい。",
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
                    "number": 19,
                    "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
                    "choiceTranslations": ["同様に", "それにもかかわらず", "その結果", "予想外に"],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ Similarly＝同様に。因果関係なので不適切",
                        "❌ Nevertheless＝それにもかかわらず。逆接は不適切",
                        "✅ Consequently＝その結果。前文の論理から自然",
                        "❌ Unexpectedly＝予想外に。予想できる展開なので不適切"
                    ],
                    "sourceEvidence": ["providing children from low-income families with the basic skills"]
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

### 2e. Section 2: 大問3（reading-comprehension 型・7問）

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
            "paragraphs": ["段落1", "段落2", "段落3"],
            "translations": ["和訳1", "和訳2", "和訳3"],
            "sentencePairs": [["en", "ja"]],
            "questions": [
                {
                    "number": 25,
                    "question": "Which of the following is true based on the first paragraph?",
                    "questionTranslation": "第1段落に基づいて正しいものはどれか？",
                    "choices": ["選択肢A", "選択肢B", "選択肢C", "選択肢D"],
                    "choiceTranslations": ["和訳A", "和訳B", "和訳C", "和訳D"],
                    "answer": 3,
                    "choiceAnalysis": [
                        "❌ 不正解の理由...",
                        "❌ 不正解の理由...",
                        "✅ 正解の根拠...",
                        "❌ 不正解の理由..."
                    ],
                    "sourceEvidence": ["researchers are constantly looking for alternative crop-protection methods"]
                }
            ]
        }
    ]
}
```

**★ 2級との違い:**
- `questionTranslation`: 設問の和訳（和訳ONで表示）
- `choiceTranslations`: 各選択肢の和訳（和訳ONで表示、translation-block風スタイル）
- `sourceEvidence`: 正解行クリック→本文の根拠箇所を黄色ハイライト＋自動スクロール
- 準1級のPart 3Aは**email形式なし**（2級のような `format: "email"` は不要）
- Part 3A: 3段落＋3問、Part 3B: 3段落＋4問が標準

### 2f. choiceAnalysis & sourceEvidence のルール

#### choiceAnalysis（全31問必須）
- `✅` で正解、`❌` で不正解のプレフィクスを使う
- 正答は根拠を簡潔に説明、誤答は不適切な理由を説明
- Part 1は `grammar` キーに 💡 付きワンポイント解説も追加

#### sourceEvidence（P2/P3の13問必須）
- 本文中の**正解の根拠となるフレーズ**を配列で指定
- クリックで本文の該当箇所が黄色ハイライト＋自動スクロール
- **アポストロフィ（`'`）を含むテキストもそのまま記載可**（グローバルマップ方式で処理）
- テキストは `textContent` ベースでマッチ（HTMLタグは無視される）

### 2g. スクリプト実行と保存

```python
import os
output_dir = r"g:\マイドライブ\eiken practice\data\pre-grade1\YYYY-S"
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

### 3b. FP構成ルール（2級と共通）

| FP | 内容 | ルール |
|----|------|--------|
| fp1-fp4 | **文法・構文トピック** | 同じ級の他試験と重複しないトピックを選ぶ |
| fp5 | **パラフレーズ（必須）** | タイトル固定「今回の重要なパラフレーズ」 |

#### ★★★ FP品質ルール（最重要）★★★

> **⚠ FP1〜4は必ず文法・構文トピックにすること。内容テーマ（語彙・トピック）ベースのFPは不可。**

**✅ 準1級向けFPタイトル例（文法・構文）：**
- 譲歩・逆接の論理展開（Concessive & Contrastive Logic）
- 受動態の多様な形式（Advanced Passive Constructions）
- 分詞構文と分詞の後置修飾（Participle Clauses & Post-modification）
- 因果関係の接続表現（Cause-Effect Connectors）
- 仮定法過去完了と混合仮定法
- 無生物主語構文
- 同格のthat節と関係代名詞の使い分け

**❌ 不可なFPタイトルの例（内容・語彙ベース）：**
- ~~害虫防除の科学用語~~
- ~~労働運動の歴史的語彙~~
- ~~幼児教育政策のキーワード~~

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

Pre-Grade 1 のカタログエントリ:
```javascript
{
    id: 'pre-grade1',
    name: 'Pre-Grade 1',
    cefr: 'CEFR B2',
    color: '#2563eb',
    path: 'pre-grade1',
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
    if len(vocab) < 80:
        errors.append(f"vocabulary count = {len(vocab)}, must be 80+")

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

    # 6. P3の questionTranslation / choiceTranslations チェック
    for s in d.get("sections", []):
        if s["type"] == "reading-comprehension":
            for p in s.get("passages", []):
                for q in p.get("questions", []):
                    if "questionTranslation" not in q:
                        errors.append(f"Q{q.get('number')}: missing questionTranslation")
                    if "choiceTranslations" not in q:
                        errors.append(f"Q{q.get('number')}: missing choiceTranslations")

    # 7. P2の choiceTranslations チェック
    for s in d.get("sections", []):
        if s["type"] == "passage-fill":
            for p in s.get("passages", []):
                for q in p.get("questions", []):
                    if "choiceTranslations" not in q:
                        errors.append(f"Q{q.get('number')}: missing choiceTranslations")

    # 8. focusPoints チェック
    fps = d.get("lessonPlan", {}).get("focusPoints", [])
    if len(fps) != 5:
        errors.append(f"focusPoints count = {len(fps)}, expected 5")
    for i, fp in enumerate(fps):
        if "id" not in fp:
            errors.append(f"FP{i+1}: missing 'id'")
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

    # 9. sentencePairs チェック
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

    # 10. 語彙バランスチェック
    p1_count = sum(1 for v in vocab if "Part 1" in str(v.get("example","")) or v.get("level","") in ["準1級","2級上位"])
    print(f"INFO: vocabulary={len(vocab)}, questions={total_q}, choiceAnalysis={ca_count}, sourceEvidence={ev_count}")

    if errors:
        print("⚠ VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ ALL CHECKS PASSED")

verify(r"g:\マイドライブ\eiken practice\data\pre-grade1\YYYY-S\data.json")
```

### 5b. ブラウザ検証チェックリスト

| # | テスト項目 | 確認手順 |
|---|-----------|---------|
| 1 | トップページ表示 | `localhost:8085/top.html` → Pre-Grade 1 が表示される |
| 2 | 単語タブ | 4択クイズが表示される（80語） |
| 3 | 大問1タブ | 18問の空所補充＋choiceAnalysis＋grammar表示 |
| 4 | 大問2タブ | 2つのパッセージ＋6問が表示される |
| 5 | 大問3タブ | 2つのパッセージ＋7問が表示される |
| 6 | 文法タブ | 5つのfocusPointカードが表示される |
| 7 | 文訳ポップアップ | 大問2/3の本文をクリック → 和訳が表示される |
| 8 | マーカーON | ツールバー「文法マーカー」→ 5色のハイライトが表示 |
| 9 | 正解表示 | 正解表示ON → choiceAnalysis表示、✅/❌形式 |
| 10 | **根拠ハイライト** | 正解の緑テキストをクリック → 本文が黄色ハイライト＋自動スクロール |
| 11 | **和訳ON** | 和訳ON → P3の設問和訳＋選択肢和訳がトーンダウンで表示 |
| 12 | 印刷メニュー | 印刷ボタン → メニューが表示される |
| 13 | ライトモード | テーマ切替 → ハイライト・凡例が見やすい |

---

## 過去の落とし穴と対策一覧

| 問題 | 原因 | 対策 |
|------|------|------|
| 凡例の個別選択不可 | focusPoints に `"id"` キーがない | **各FPに必ず `"id": "fp1"` ~ `"fp5"` を付ける** |
| 文法タブが空白 | キー名の不一致 | `explanation`, `examples`, `practiceQuestions` を使う |
| 根拠ハイライトが動かない | `esc()` がアポストロフィを壊す | **`_evidenceMap` グローバルマップ方式で処理済み（data-evidence属性は使わない）** |
| 選択肢和訳が表示されない | `toggleTranslation` に `.choice-translation` 未追加 | **app.js で `.choice-translation` もトグル対象に含める** |
| ページがリダイレクトされる | `GRADE_MAP` に `pre-grade1` がない | **app.js の `GRADE_MAP` に `'pre-grade1'` エントリを追加する** |
| 単語が大問1に偏る | P2/P3パッセージからの抽出漏れ | **大問2から15-20語、大問3から15-20語を必ず抽出する** |
| FPが内容ベース | 語彙・トピックテーマのFPを作った | **FP1-4は文法構文トピックのみ。語彙/テーマ名は不可** |
| FP5がパラフレーズでない | FP5にも文法トピックを入れた | **FP5は必ず「今回の重要なパラフレーズ」固定** |
| **練習パッセージが表示されない** | `practicePassage` キーが欠落 | **全5 FPに必ず `practicePassage`（en/ja）を追加** |
| **確認問題が空** | `practiceQuestions` が無い or 0件 | **全5 FPに3〜4問の `practiceQuestions` を追加** |

---

## ファイル構成

```
g:\マイドライブ\eiken practice\
├── top.js            ← EXAM_CATALOG にエントリ追加
├── app.js            ← GRADE_MAP に pre-grade1 追加済み
├── index.html        ← 変更不要
├── style.css         ← 変更不要
├── vocab-cards.html  ← 変更不要
└── data/
    └── pre-grade1/
        └── {exam_id}/
            └── data.json   ← Step 2-3 で生成
```
