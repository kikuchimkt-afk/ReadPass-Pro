---
description: FP練習パッセージを問題長文から抜き出す方式で作成・更新するワークフロー
---

# FP練習パッセージの長文抜き出しワークフロー

## 概要
文法タブ（`lessonPlan.focusPoints`）の `practicePassage` を、問題の長文パッセージ（大問2・3）から抜き出して作成する方法。

## ルール

### 1. 抜き出し元の制約
- **大問2（passage-fill）および大問3（reading-comprehension）のみ**を抜き出し元とする
- **大問1（vocabulary）は抽出候補に含めない**

### 2. パッセージ長
- 各FPにつき**代表的な1段落のみ**を使用する（複数段落は不可）

### 3. パッセージの分散
- **各FPでできるだけ異なるパッセージ（異なる長文タイトル）を使用する**
- やむを得ず同じパッセージを使う場合は、**異なる段落**を選ぶ
- 同じパッセージの同じ段落は避ける

### 4. 空所補充の完成文化
- 大問2の passage-fill パッセージを使用する場合、`( 21 )` のような空所を**正解の選択肢で埋めた完成文**にする
- 正解は `data.json` の `sections[passage-fill].passages[].questions[].answer` と `choices` から取得

### 5. データ構造
各FPの `practicePassage` は以下の構造:
```json
{
    "practicePassage": {
        "en": "[出典: パッセージタイトル]\n完成された英文1段落",
        "ja": "日本語訳1段落",
        "audioFile": "audio/practice_pp1.mp3"
    },
    "highlightPatterns": ["パッセージ内に実在するパターン1", "パターン2"],
    "practiceQuestions": [
        {"q": "確認問題", "a": "解答"}
    ]
}
```

### 6. highlightPatterns
- `highlightPatterns` は**選択した1段落内に実際に存在する表現のみ**を指定する
- パッセージに存在しないパターンは削除する

### 7. 確認問題
- 各FPにつき**4問**作成
- FPのテーマ（因果関係、譲歩、比較・程度、条件文、パラフレーズ等）に焦点を当てた問題
- 同じパッセージを複数FPで使う場合は、**確認問題でテーマの違いを出す**

### 8. 音声ファイル
- 新しい `practicePassage.en` テキストで gTTS により MP3 を再生成
- `[出典: ...]` ラベル行は音声から除外する
- `audioFile` のパスは既存の命名規則に従う（例: `audio/practice_pp1.mp3`）

## 実装手順

// turbo-all

### Step 1: パターン照合分析
対象の `data.json` を読み込み、各FPの `highlightPatterns` が大問2・3のどのパッセージのどの段落に存在するか照合する。

```python
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

dp = r'<data.jsonのパス>'
d = json.load(open(dp, 'r', encoding='utf-8'))

# passage-fill / reading-comprehension のパッセージを収集
for s in d['sections']:
    if 'passages' not in s: continue
    for p in s['passages']:
        for i, para in enumerate(p['paragraphs']):
            # 各FPのhighlightPatternsと照合
            for fp in d['lessonPlan']['focusPoints']:
                for pat in fp.get('highlightPatterns', []):
                    if pat.lower() in para.lower():
                        print(f"{fp['id']}: '{pat}' → {s['type']}/{p['label']} para {i}")
```

### Step 2: パッセージ割り当て決定
- 分析結果をもとに、各FPに最適な1段落を割り当て
- パッセージの重複を最小化
- 大問1は除外

### Step 3: データ更新スクリプト作成・実行
- 空所補充の正解取得 → 完成文化
- practicePassage (en/ja)、highlightPatterns、practiceQuestions を更新
- data.json に書き込み

### Step 4: 音声再生成
- gTTS で各FPの practice audio を再生成

### Step 5: ブラウザ検証
- `http://localhost:8085` で文法タブを開き、各FPの表示を確認
- ハイライト機能、翻訳トグル、音声再生、確認問題の表示をチェック
