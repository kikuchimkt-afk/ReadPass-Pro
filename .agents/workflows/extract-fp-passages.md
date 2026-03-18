---
description: FP練習パッセージを問題長文から抜き出す方式で作成・更新するワークフロー
---

# FP練習パッセージの長文抜き出しワークフロー

## 概要
文法タブ（`lessonPlan.focusPoints`）の `practicePassage` を、問題の長文パッセージ（大問2・3）から抜き出して作成する方法。
FPの選定自体を含む全面刷新にも対応。

## ルール

### 1. FP選定の制約
- FPは**必ず大問2/3の長文読解パッセージに含まれる文法ポイント**から選定する
- **大問1（vocabulary）からFPを選定してはいけない**
- 4つのFPはできるだけ**異なるパッセージ**（異なる長文タイトル）から選定する
- やむを得ず同じパッセージを使う場合は、**異なる段落**を選ぶ

### 2. パッセージ長
- 各FPにつき**代表的な1段落のみ**を使用する（複数段落は不可）

### 3. 空所補充の完成文化
- 大問2の passage-fill パッセージを使用する場合、`( 21 )` のような空所を**正解の選択肢で埋めた完成文**にする
- 正解は `data.json` の `sections[passage-fill].passages[].questions[].answer` と `choices` から取得

### 4. データ構造
各FPの必須フィールド（**全て更新すること**）:
```json
{
    "id": "fp1",
    "title": "FPタイトル（日本語+英語）",
    "subtitle": "English Subtitle",
    "explanation": "なぜこの構文が重要かの説明（文字列）",
    "sourceQuote": "出典引用（文字列、配列ではない）",
    "sourceLocation": "Part 3B",
    "highlightLabel": "ハイライトラベル",
    "highlightColor": "#FF6B6B",
    "examples": [
        {"en": "英語例文", "ja": "日本語訳", "note": "文法ポイント解説"}
    ],
    "practicePassage": {
        "en": "[出典: パッセージタイトル]\n完成された英文1段落",
        "ja": "日本語訳1段落",
        "audioFile": "audio/practice_pp1.mp3"
    },
    "highlightPatterns": ["パッセージ内に実在するFPターゲット表現"],
    "practiceQuestions": [
        {"q": "確認問題", "a": "解答"}
    ]
}
```

> [!CAUTION]
> `sourceQuote` は**文字列型**であること。配列にするとフロントエンド(app.js 1034行目)で `.replace()` エラーが発生し、文法タブが空白になる。

### 5. highlightPatterns
- **FPのターゲット文法パターンそのもの**を指定する（テーマに無関係な単語をHLにしない）
- `highlightPatterns` は**選択した1段落内に実際に存在する表現のみ**を指定する

### 6. 確認問題
- 各FPにつき**4問**作成
- FPのテーマ（因果関係、譲歩、比較・程度、条件文、パラフレーズ等）に焦点を当てた問題

### 7. 例文
- 各FPにつき**3つ**の例文（en/ja/note）を作成
- 例文の1つは必ず**Passage内から引用**する（検証スクリプトで含有チェックされる）
- `note` にFPのターゲット文法のポイントを簡潔に記載

### 8. 音声ファイル
- 新しい `practicePassage.en` テキストで gTTS により MP3 を再生成
- `[出典: ...]` ラベル行は音声から除外する
- `audioFile` のパスは既存の命名規則に従う（例: `audio/practice_pp1.mp3`）

### 9. 日本語訳
- practicePassage.ja は**正確な翻訳**を提供する
- 例文の日本語訳も正確にする
- 確認問題の解答も日本語として自然な文にする

## 実装手順

// turbo-all

### Step 1: 全パッセージの文法ポイント分析
対象の `data.json` を読み込み、大問2・3の全パッセージ全段落を出力して、文法ポイントを分析する。

```javascript
// 全パッセージを空所補充→完成文にして出力
const fs = require('fs');
const d = JSON.parse(fs.readFileSync('<data.jsonパス>', 'utf-8'));
for (const s of d.sections) {
    if (s.type !== 'passage-fill' && s.type !== 'reading-comprehension') continue;
    console.log(`\n=== ${s.name} (${s.type}) ===`);
    for (const p of (s.passages || [])) {
        const answers = {};
        if (s.type === 'passage-fill' && p.questions) {
            for (const q of p.questions) answers[q.number] = q.choices[q.answer - 1];
        }
        console.log(`\n--- ${p.label || p.title} ---`);
        for (let i = 0; i < (p.paragraphs || []).length; i++) {
            let en = Array.isArray(p.paragraphs[i]) ? p.paragraphs[i][0] : p.paragraphs[i];
            for (const [num, ans] of Object.entries(answers)) {
                en = en.replace(new RegExp(`\\(\\s*${num}\\s*\\)`, 'g'), ans);
            }
            console.log(`  [Para ${i}]: ${en}`);
        }
    }
}
```

### Step 2: FP選定と段落割り当て
- 各段落から2級レベルの重要文法ポイントを抽出
- 4つのFPを選定（全て大問2/3の長文から）
- 各FPに最適な1段落を割り当て
- パッセージの重複を最小化

**FP選定基準:**
- 2級の文法・構文として重要度が高い
- 長文の中で文法ポイントが自然に使われている
- highlightPatternsとして明確にマーキングできる
- 学習者にとって有用なターゲット構文がある

### Step 3: データ更新スクリプト作成・実行
- Node.jsスクリプトで以下を更新:
  - `title`, `subtitle`, `explanation`, `sourceQuote`, `sourceLocation`
  - `highlightLabel`, `highlightColor`
  - `examples[]` (en/ja/note)
  - `practicePassage` (en/ja/audioFile)
  - `highlightPatterns[]`
  - `practiceQuestions[]` (q/a)

> [!IMPORTANT]
> **全フィールドを更新すること**。一部だけ更新すると旧データとの不整合でレンダリングエラーが発生する。

### Step 4: 音声再生成
```python
from gtts import gTTS
import json, os, re

base = r'<exam directory>'
with open(os.path.join(base, 'data.json'), 'r', encoding='utf-8') as f:
    d = json.load(f)

for fp in d['lessonPlan']['focusPoints']:
    if fp['id'] == 'fp5': continue
    pp = fp.get('practicePassage', {})
    en = pp.get('en', '')
    audio = pp.get('audioFile', '')
    if not en or not audio: continue
    text = re.sub(r'\[出典:\s*.+?\]\s*\n?', '', en).strip()
    tts = gTTS(text, lang='en')
    tts.save(os.path.join(base, audio))
    print(f"✅ {fp['id']}: {audio}")
```

### Step 5: 検証スクリプト実行
```bash
node tools/verify-fp-passages.js <grade>
```
全FPが**OK**であることを確認。

### Step 6: ブラウザ検証
- `http://localhost:8085` で文法タブを開き、各FPの表示を確認
- ハイライト機能（FPをハイライトボタン）
- 翻訳トグル（日本語訳を表示ボタン）
- 音声再生
- 確認問題の表示と解答表示

## トラブルシューティング

### 文法タブが空白になる場合
1. `sourceQuote` が配列になっていないか確認（文字列であること）
2. data.json が有効なJSONか確認（`JSON.parse` でエラーが出ないこと）
3. 全FPの必須フィールドが揃っているか確認
