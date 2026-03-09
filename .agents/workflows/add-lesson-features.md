---
description: 英検リーディングアプリに文法解析・教材機能を追加するワークフロー
---

# 英検リーディング 文法解析・教材機能の追加

// turbo-all

## 概要
大問2・3のパッセージを分析し、文法・構文の着目点を抽出して、対話型の教材コンテンツ（レッスンプラン、ハイライト、文訳ポップアップ、単語カード）をアプリに追加する手順。

---

## 1. パッセージの文法・構文分析

1. `data/{grade}/{exam}/data.json` を開き、大問2・3（`passage-fill` / `reading-comprehension`）のパッセージ本文を精査する
2. **5個の着目点（Focus Point）を抽出する。構成は以下の通り：**
   - **FP1〜4: 文法・構文トピック**（パッセージから特徴的な文法を抽出）
   - **FP5: 今回の重要なパラフレーズ**（固定テーマ、毎回必須）

3. **FP1〜4 のトピック選定ルール（重要！）：**
   - **同じ級の他の試験回と文法トピックが重複しないようにする**
   - 新しい試験を追加する前に、同じ級の既存 `data.json` を確認し、使用済みのトピック一覧を把握する
   - トピック例（各級で網羅的にカバーすること）：
     - 相関接続詞（not only A but also B, either A or B, neither A nor B）
     - 比較構文（the + 比較級 the + 比較級, as ~ as, 最上級表現）
     - ディスコースマーカー（Therefore, However, In this way, As a result...）
     - 受動態と分詞構文（being + 過去分詞, having + 過去分詞）
     - 関係詞（制限用法 vs 非制限用法, what / which の使い分け）
     - 仮定法（If + 過去, I wish, as if）
     - 不定詞・動名詞（to不定詞の形容詞的用法, 動名詞の慣用表現）
     - 接続詞と従属節（although, while, unless, provided that）
     - 無生物主語構文（This enables A to ~, The discovery led to ~）
     - 強調構文（It is ~ that, What ~ is）
     - 倒置（Not only did ~, Never has ~, Only when ~）
     - 同格（the fact that ~, the idea that ~）
     - 使役・知覚動詞（make/let/have + O + C, see/hear + O + 原形/~ing）
     - 分裂文・疑似分裂文
     - 時制の一致と話法

4. **FP5: パラフレーズの作成ルール：**
   - タイトルは「今回の重要なパラフレーズ」（固定）
   - **必ず当該試験の大問2・3のパッセージから実際のパラフレーズを抽出する**
   - 本文中の表現と、選択肢や他の段落での言い換え表現をペアにする
   - `sourceQuote` には ①②③… 番号付きで、各パラフレーズペアを改行(\n)区切りで記載
   - `examples` には一般的なパラフレーズ例文を3つ程度
   - `practicePassage` には当該試験から抽出したパラフレーズペアの対比練習

5. 各着目点について以下を作成する：
   - タイトル・サブタイトル・解説文
   - 出典箇所（sourceQuote, sourceLocation）
   - 例文（英語＋和訳＋注釈）
   - **★ 練習パッセージ（英語＋和訳＋Q&A）— 全FPに必須（欠落厳禁）**
   - ハイライトパターン（highlightPatterns, highlightColor, highlightLabel）

> **⚠ 全5つのFPに必ず `practicePassage`（en/ja）と `practiceQuestions`（3〜4問）を含めること。1つでも欠落すると文法タブで「練習パッセージ」セクションが空白になる。**
>
> - 各パッセージは **5〜7文** の短いパラグラフ
> - **本文とは異なるオリジナルトピック** で、当該FPの文法・構文が自然に複数回使われていること
> - 英語＋日本語訳のペア
> - 3〜4個の `practiceQuestions`（`{"q": "...", "a": "..."}` 形式）と対にする

## 2. data.json への lessonPlan データ追加

1. Pythonスクリプト（`c:\tmp\add_lesson_plan.py`）を作成し、`data.json` の `lessonPlan` オブジェクトに `focusPoints` 配列を追加する
2. 各 focusPoint のデータ構造：
```json
{
    "title": "着目点タイトル",
    "subtitle": "英語サブタイトル",
    "explanation": "解説文",
    "sourceQuote": "本文の該当箇所",
    "sourceLocation": "Part 2A 第1段落",
    "examples": [
        {
            "en": "English example",
            "ja": "日本語訳",
            "note": "文法解説ノート"
        }
    ],
    "practicePassage": {
        "en": "Practice passage text",
        "ja": "練習パッセージ和訳"
    },
    "practiceQuestions": [
        { "q": "質問", "a": "回答" }
    ],
    "highlightPatterns": ["パターン1", "パターン2"],
    "highlightColor": "rgba(R,G,B,0.25)",
    "highlightLabel": "ラベル名"
}
```
3. スクリプトを実行してデータを追加する

## 3. 文訳ポップアップデータの追加

1. Pythonスクリプト（`c:\tmp\fix_sentence_pairs.py`）を作成
2. Part 2/3 の各パッセージに `sentencePairs` を追加する
   - `sentencePairs` は `[[英文, 和訳], ...]` の配列
   - 各英文は**パッセージ本文と完全一致する文字列**であること（regex分割ではなく直接マッチ）
   - `Mr.` や `U.K.` など略語に注意し、文の区切りを正確に指定する
3. スクリプトを実行

## 4. app.js の実装

### 4a. 文法ハイライト機能
- `hlState` 変数でアクティブ状態を管理
- `toggleHighlight()` — 全ハイライトのON/OFF
- `buildHighlightLegend()` — 凡例バーの動的生成
- `applyHighlights()` — パッセージテキスト内のパターンを `<mark>` タグで囲む（最長一致優先）
- `removeHighlights()` — 元のテキストに復元

### 4b. 文訳ポップアップ機能
- `_sentTrans` 配列 — 翻訳テキストをインデックスで管理（HTML属性に直接入れない）
- `wrapSentences(paragraph, passageData)` — sentencePairs を使い、英文を直接テキスト検索してクリック可能な `<span>` でラップ
- `setupSentencePopups(container)` — クリックイベントでツールチップを表示/非表示
- **重要**: `data-tidx` 属性でインデックスを参照し、日本語テキストをHTML属性に入れないこと（`( 18 )` 等の置換処理でHTML属性が壊れるため）

### 4c. レッスンプラン表示
- `renderLessonPlan()` — focusPoints をカード形式で表示
- 「文法」タブで表示

### 4d. 印刷機能
- `printLessonPlan()` — 問題ページと解答ページを分離
- `printLessonRef()` — 講師用の解説プリント
- 各Focus Pointごとに改ページ

## 5. 単語カードアプリ

1. `vocab-cards.html` を作成（スタンドアロンHTML）
2. 機能：
   - `?data=path/to/data.json` クエリパラメータでデータを読み込む
   - 3Dフリップカード（表: 英単語、裏: 和訳＋例文）
   - 自己評価（覚えた / まだ）
   - localStorage で進捗保存
   - 出現順 / ランダム切替
   - 結果画面（覚えた数 / もう一度の数）
3. メインアプリのツールバーに「単語カード」ボタンを追加
4. `APP.openVocabCards()` で `window.open()` により別ウィンドウで開く
   - URLは `vocab-cards.html?data=data/{grade.path}/{examId}/data.json` と構築

## 6. CSS スタイル追加箇所

- `.sentence-span` / `.sentence-tooltip` — 文訳ポップアップ
- `.grammar-hl` / `.highlight-legend` — 文法ハイライト
- `.answer-indicator.hidden` — 正解バッジの表示/非表示
- `.fp-card` / `.fp-header` / `.fp-example` / `.fp-passage` / `.fp-qa` — レッスンプランUI

## 7. 注意事項・過去の落とし穴

- **文訳ポップアップ**: 翻訳テキストを `data-trans="..."` 属性に直接入れると、問題番号 `( 18 )` の置換処理時にHTML属性が壊れる → `data-tidx` でインデックス参照する方式を使う
- **文分割**: regexで `.` ごとに分割すると `Mr.` や `U.K.` で誤分割される → `sentencePairs` で英文を明示的に指定し、`indexOf()` で直接マッチする
- **正解バッジ**: `.answer-indicator.hidden { display: none; }` のCSSルールが無いと、`hidden` クラスが付いていても表示される
- **settings リセット**: `resetAll()` で `settings.showAnswers` を `false` に戻し、ツールバーボタンも同期する
- **単語カードURL**: `examSelect` の値は短いID（例: `2025-3`）のため、`GRADE_MAP` と組み合わせてフルパスを構築する
- **focusPoint のキー名統一（重要）**: データ生成時に以下のキー名を必ず使うこと。異なるキー名を使うと `renderLessonPlan` でエラーになり、文法タブが空白になる：
  - `examples`（❌ `exampleSentences` は不可）
  - `explanation`（❌ `why` は不可）
  - `practiceQuestions`（`practicePassage` の中ではなく、focusPoint の直下に配置。❌ `practicePassage.questions` は不可）
  - `renderLessonPlan` はフォールバック対応済み（両方のキーを参照する）だが、新規データは正しいキー名を使うこと
- **sourceQuote の改行**: `\n` で区切ると `<br>` に変換されて見やすく表示される。矢印(→)でパラフレーズペアを繋ぐ場合は番号付き（①②③…）で1行ずつ書く
