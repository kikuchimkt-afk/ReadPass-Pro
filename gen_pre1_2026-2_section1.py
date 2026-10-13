# -*- coding: utf-8 -*-
"""Install the official 2026-2 Grade Pre-1 Part 1 into ReadPass data."""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "pre-grade1" / "2026-2" / "data.json"


QUESTIONS = [
    {
        "number": 1,
        "text": "The cabin crew was forced to ( 1 ) a passenger on the airplane when he started to become violent toward a person sitting near him.",
        "translation": "ある乗客が近くに座っていた人に暴力をふるい始めたため、客室乗務員は機内でその乗客を ( 1 ) せざるを得なかった。",
        "choices": ["restrain", "recharge", "resume", "reflect"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ restrain＝取り押さえる・拘束する → 正解。💡 started to become violent toward a person から、暴れ出した乗客の動きを力で抑える場面だと分かる。",
            "❌ recharge＝再充電する → 電池や体力を回復させる語で、暴れる乗客を目的語にとるのは不自然。",
            "❌ resume＝再開する → 中断していた活動や会議を目的語にとる語で、人を目的語にして「乗客を再開する」とは言えない。",
            "❌ reflect＝反映する・反射する → 光や意見を映し出す意味で、機内で暴れる人への対応には合わない。",
        ],
        "grammar": "💡 be forced to + 動詞の原形は「〜せざるを得ない」。start to become ～ は「～になり始める」、violent toward ～ は「～に対して暴力的な」。sitting near him は a person を後ろから修飾する現在分詞句。",
    },
    {
        "number": 2,
        "text": "Luna looked out of the window at the winter landscape, with its ( 2 ) trees and empty fields.",
        "translation": "ルナは窓から冬の景色を眺めた。そこには ( 2 ) 木々と何もない畑が広がっていた。",
        "choices": ["dizzy", "keen", "fussy", "bare"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ dizzy＝めまいがする → 人の体調を表す形容詞で、木の様子を描写する語ではない。",
            "❌ keen＝熱心な・鋭い → be keen to do や a keen eye のように人の意欲や感覚に使い、冬の木々の描写には合わない。",
            "❌ fussy＝好みがうるさい → 人の性格を表す語で、景色の中の木には使えない。",
            "✅ bare＝葉のない・むき出しの → 正解。💡 winter landscape と empty fields から、葉が落ちて枝だけになった寂しい冬の木々が自然。",
        ],
        "grammar": "💡 with its ～ は直前の the winter landscape を補足し、「（その景色には）～がある」と付帯的な特徴を加える。( 2 ) trees と empty fields が and で並列され、どちらも冬の寂しさを描いている。",
    },
    {
        "number": 3,
        "text": "Emir and Corinne were disappointed that they had to change their vacation ( 3 ), but it was necessary for them to take a different route because of the storm.",
        "translation": "エミールとコリーヌは休暇の ( 3 ) を変更しなければならないことにがっかりしたが、嵐のため別のルートを取る必要があった。",
        "choices": ["dignity", "controversy", "monarchy", "itinerary"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ dignity＝威厳・尊厳 → 休暇の予定を変更するという文脈とは関係がない。",
            "❌ controversy＝論争 → 社会的な議論を表す語で、vacation と結びついて「変更する対象」にはならない。",
            "❌ monarchy＝君主制 → 政治体制を表す語で、旅行の話には合わない。",
            "✅ itinerary＝旅程・旅行計画 → 正解。💡 take a different route（別のルートを取る）が、旅程を変更せざるを得なかった理由を説明している。",
        ],
        "grammar": "💡 be disappointed that S V は「SがVすることにがっかりする」。it was necessary for them to take ... は形式主語構文で、for them が不定詞 to take の意味上の主語。",
    },
    {
        "number": 4,
        "text": "The couple took regular walks to ( 4 ) themselves with their new neighborhood. They wanted to learn their way around as quickly as possible.",
        "translation": "その夫婦は新しい近所に ( 4 ) ために、定期的に散歩をした。できるだけ早く周辺の道を覚えたかったのだ。",
        "choices": ["confine", "inhibit", "familiarize", "seize"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ confine＝閉じ込める・限定する → confine oneself to ～（～に限定する）の形で使い、with とは結びつかない。散歩で近所を知る文脈にも合わない。",
            "❌ inhibit＝抑制する・妨げる → 自分を抑えることになり、近所に早く慣れたいという第2文と矛盾する。",
            "✅ familiarize＝慣れさせる・精通させる → 正解。💡 familiarize oneself with ～ は「～に慣れる・～をよく知る」。learn their way around（周辺の道を覚える）が言い換えになっている。",
            "❌ seize＝つかむ・押収する → seize themselves with ～ という言い方はなく、近所に慣れる意味にはならない。",
        ],
        "grammar": "💡 familiarize oneself with ～ は「～に慣れる・～をよく知る」。to familiarize は目的を表す不定詞の副詞的用法。learn one's way around は「（場所の）勝手を覚える」。",
    },
    {
        "number": 5,
        "text": "A: Can we discuss that problem next week?\nB: No, I’m sorry. It’s a matter of great ( 5 ), so I need to have your answer today.",
        "translation": "A：その問題は来週話し合えますか。\nB：いいえ、すみません。非常に ( 5 ) の問題なので、今日中にお返事をいただく必要があります。",
        "choices": ["diversion", "maneuver", "urgency", "contempt"],
        "answer": 3,
        "choiceAnalysis": [
            "❌ diversion＝気晴らし・迂回 → 来週まで待てない理由にはならない。",
            "❌ maneuver＝策略・巧みな操作 → 問題の性質として「今日中に答えが必要」という結論につながらない。",
            "✅ urgency＝緊急性 → 正解。💡 next week ではなく I need to have your answer today と急いでいることから、「緊急を要する問題」だと分かる。",
            "❌ contempt＝軽蔑 → 相手や問題への感情を表す語で、返事を急ぐ理由にはならない。",
        ],
        "grammar": "💡 a matter of great + 抽象名詞 は「非常に～な事柄」。a matter of great urgency＝a very urgent matter。so は結果を表し「だから（今日答えが必要だ）」とつながる。",
    },
    {
        "number": 6,
        "text": "The huge Christmas tree in the town square was a great sight in itself, but the colorful ( 6 ) that decorated it made it truly beautiful.",
        "translation": "町の広場の巨大なクリスマスツリーはそれ自体がすばらしい光景だったが、それを飾るカラフルな ( 6 ) が、ツリーを本当に美しいものにしていた。",
        "choices": ["dwellings", "refuges", "prospects", "ornaments"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ dwellings＝住居 → 人が住む建物であり、クリスマスツリーを飾るものではない。",
            "❌ refuges＝避難所・保護区 → 危険から逃れる場所を表し、ツリーの装飾には使えない。",
            "❌ prospects＝見込み・展望 → 将来の可能性を表す抽象名詞で、colorful や decorated it と結びつかない。",
            "✅ ornaments＝飾り・装飾品 → 正解。💡 that decorated it（それを飾った）とクリスマスツリーから、ツリーにつるす飾りだと分かる。",
        ],
        "grammar": "💡 in itself は「それ自体で」。that decorated it は ( 6 ) を修飾する関係代名詞節で、the colorful ( 6 ) that decorated it 全体が made の主語。make O C は「OをCにする」。",
    },
    {
        "number": 7,
        "text": "Peter spends most of his time at work doing ( 7 ) tasks, like typing letters, answering phones, and filing documents.",
        "translation": "ピーターは職場での時間のほとんどを、手紙のタイピング、電話応対、書類のファイリングといった ( 7 ) 仕事に費やしている。",
        "choices": ["rugged", "clerical", "majestic", "apt"],
        "answer": 2,
        "choiceAnalysis": [
            "❌ rugged＝起伏の多い・頑丈な → 地形や外見を表す語で、事務作業の性質を表さない。",
            "✅ clerical＝事務の → 正解。💡 typing letters, answering phones, filing documents という具体例が、典型的な事務作業を示している。",
            "❌ majestic＝雄大な・威厳のある → 山や建物などの壮大さを表す語で、日常の仕事には合わない。",
            "❌ apt＝適切な・～しがちな → apt to do や an apt description の形で使い、仕事の種類を説明する語ではない。",
        ],
        "grammar": "💡 spend + 時間 + doing は「～して時間を過ごす」。like ～ は具体例を挙げる前置詞「～のような」で、typing / answering / filing の動名詞が並列されている。",
    },
    {
        "number": 8,
        "text": "The teacher warned the students not to ( 8 ) in front of the school after classes, as it made the school look bad.",
        "translation": "先生は生徒たちに、放課後に学校の前で ( 8 ) ないよう注意した。学校の印象が悪くなるからだ。",
        "choices": ["loiter", "scratch", "mourn", "applaud"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ loiter＝ぶらつく・たむろする → 正解。💡 in front of the school after classes と made the school look bad から、放課後に校門前でたむろする行為を注意していると分かる。",
            "❌ scratch＝ひっかく・かく → 体をかいたり物をひっかいたりする動作で、放課後に校門の前で行うと学校の印象が悪くなる行為としては不自然。",
            "❌ mourn＝嘆き悲しむ・悼む → 死や喪失を悲しむ語で、学校の評判を気にして禁止する行為ではない。",
            "❌ applaud＝拍手する・称賛する → 学校の印象を悪くする行為ではない。",
        ],
        "grammar": "💡 warn O not to do は「Oに～しないよう警告する」。不定詞の否定は not を to の直前に置く。as は理由「～なので」、make O look bad は使役の make + O + 動詞の原形で「Oの見た目を悪くする」。",
    },
    {
        "number": 9,
        "text": "The woman was so ( 9 ) with thoughts about her sick child that she did not notice when her husband arrived home.",
        "translation": "その女性は病気の子どものことで頭がとても ( 9 ) ので、夫が帰宅したことに気づかなかった。",
        "choices": ["preoccupied", "trespassed", "grated", "endorsed"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ preoccupied＝心を奪われた・頭がいっぱいの → 正解。💡 be preoccupied with ～ は「～のことで頭がいっぱいだ」。夫の帰宅に気づかなかったという結果と自然につながる。",
            "❌ trespassed＝不法侵入した → trespass on ～ の形で場所に使い、「考えに不法侵入する」という意味にはならない。",
            "❌ grated＝すりおろされた・いらだたせた → be grated with thoughts という言い方はなく、心配で周りが見えない状態を表せない。",
            "❌ endorsed＝支持された・承認された → 公的な支持を表す語で、子どもを心配する気持ちの描写には合わない。",
        ],
        "grammar": "💡 so ～ that S V は「とても～なのでSはVする」という程度・結果の構文。when her husband arrived home は notice の目的語になる名詞節で「夫がいつ帰宅したか」→「夫の帰宅」。",
    },
    {
        "number": 10,
        "text": "The government official’s ( 10 ) of the factory revealed that it was polluting the local river. The factory was soon ordered to stop.",
        "translation": "政府職員による工場の ( 10 ) によって、その工場が地元の川を汚染していることが明らかになった。工場はまもなく操業停止を命じられた。",
        "choices": ["column", "succession", "inaction", "inspection"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ column＝柱・コラム → 新聞のコラムなどを表し、工場の汚染を明らかにする行為ではない。",
            "❌ succession＝連続・継承 → 地位の継承などを表し、the official’s succession of the factory では意味が通らない。",
            "❌ inaction＝何もしないこと・無策 → 何もしないことで汚染が明らかになることはない。",
            "✅ inspection＝検査・査察 → 正解。💡 revealed that it was polluting から、職員が工場を調べた結果、汚染が判明したと分かる。",
        ],
        "grammar": "💡 The government official’s inspection of the factory は「政府職員が工場を査察したこと」という名詞化表現。所有格が動作主、of の後が対象。無生物主語 + revealed that ～ は「～によって…が明らかになった」と訳すと自然。",
    },
    {
        "number": 11,
        "text": "The young politician was very ( 11 ). He believed he could solve every social problem, but most of the older politicians thought his ideas were impractical.",
        "translation": "その若い政治家はとても ( 11 ) だった。彼はあらゆる社会問題を解決できると信じていたが、年配の政治家の大半は彼の考えを非現実的だと思っていた。",
        "choices": ["soothing", "punctual", "clumsy", "idealistic"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ soothing＝心を落ち着かせる → 音楽や声などに使う語で、政治家の考え方の特徴を表さない。",
            "❌ punctual＝時間に正確な → 時間を守る性質であり、どんな問題でも解決できるという信念とは関係がない。",
            "❌ clumsy＝不器用な → 動作のぎこちなさを表す語で、考えが impractical だという評価と直接つながらない。",
            "✅ idealistic＝理想主義的な → 正解。💡 he could solve every social problem と impractical の対比から、現実離れした理想を抱く人物像が読み取れる。",
        ],
        "grammar": "💡 第2文が第1文の具体的な説明になっている。every + 単数名詞は「あらゆる～」。thought (that) his ideas were impractical は that の省略と時制の一致。",
    },
    {
        "number": 12,
        "text": "The horse has a ( 12 ) habit of trying to chase its own tail. The owner has never seen any other horse do something so odd.",
        "translation": "その馬には自分のしっぽを追いかけようとする ( 12 ) 癖がある。飼い主は、ほかの馬がそんな奇妙なことをするのを一度も見たことがない。",
        "choices": ["peculiar", "conceited", "fragrant", "transparent"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ peculiar＝奇妙な・独特の → 正解。💡 第2文の something so odd が ( 12 ) の言い換えになっている。",
            "❌ conceited＝うぬぼれた → 人の性格を表す語で、馬の癖の描写には合わない。",
            "❌ fragrant＝香りのよい → 花などに使う語で、行動の癖を表さない。",
            "❌ transparent＝透明な・見え透いた → 物の透明さや意図の分かりやすさを表し、奇妙な行動の描写には合わない。",
        ],
        "grammar": "💡 a habit of doing は「～する癖」。see O do は知覚動詞の構文で「Oが～するのを見る」。has never seen は経験の現在完了。",
    },
    {
        "number": 13,
        "text": "The CEO of the company was a man of great ( 13 ) in society. His connections with famous politicians and celebrities were well-known.",
        "translation": "その会社のCEOは、社会で大きな ( 13 ) を持つ人物だった。有名な政治家や著名人とのつながりはよく知られていた。",
        "choices": ["distress", "referral", "detention", "prominence"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ distress＝苦悩・苦痛 → 有名人とのつながりが知られているという第2文と結びつかない。",
            "❌ referral＝紹介・照会 → 医師の紹介状などを表し、a man of great referral という言い方はしない。",
            "❌ detention＝拘留・居残り → 社会的な地位の高さとは逆の内容になる。",
            "✅ prominence＝著名さ・名声 → 正解。💡 connections with famous politicians and celebrities were well-known から、社会的に目立つ有名人物だと分かる。",
        ],
        "grammar": "💡 a man of + 抽象名詞 は「～を持つ人」。of + 抽象名詞は形容詞の働きをし、a man of great prominence＝a very prominent man となる。",
    },
    {
        "number": 14,
        "text": "The author provided an ( 14 ) of his new book on his website. He hoped that readers would enjoy the sample and buy the full version.",
        "translation": "その作家は自分のウェブサイトで新刊の ( 14 ) を公開した。読者がその試し読みを楽しみ、完全版を買ってくれることを期待していた。",
        "choices": ["inheritance", "excerpt", "odor", "agenda"],
        "answer": 2,
        "choiceAnalysis": [
            "❌ inheritance＝遺産・相続 → 本の一部をウェブサイトで公開するという内容とは関係がない。",
            "✅ excerpt＝抜粋 → 正解。💡 the sample と the full version の対比から、本の一部を抜き出したものだと分かる。",
            "❌ odor＝におい → 本の内容をウェブサイトで提供するものではない。",
            "❌ agenda＝議題・協議事項 → 会議で扱う項目のことで、本の試し読みにはならない。",
        ],
        "grammar": "💡 an があるので母音で始まる語が入るが、4つの選択肢はすべて母音で始まるため冠詞は決め手にならない。He hoped that readers would ～ は時制の一致で、would は過去から見た未来。",
    },
    {
        "number": 15,
        "text": "After long discussions, the two sides were finally able to ( 15 ) a deal that was acceptable to both of them.",
        "translation": "長い話し合いの末、双方はようやく、両者にとって受け入れ可能な合意を ( 15 ) ことができた。",
        "choices": ["hammer out", "jump in", "weed out", "step aside"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ hammer out＝（協議を重ねて）まとめ上げる → 正解。💡 After long discussions と a deal から、時間をかけた交渉で合意をまとめたと分かる。hammer out a deal は定番のコロケーション。",
            "❌ jump in＝割り込む・飛び込む → 自動詞的に使い、a deal を目的語にとって「合意をまとめる」という意味にはならない。",
            "❌ weed out＝取り除く・ふるい落とす → 不要なものを排除する語で、双方が受け入れられる合意を成立させる意味と逆になる。",
            "❌ step aside＝身を引く・脇へ寄る → 目的語をとらず、合意を成立させる意味もない。",
        ],
        "grammar": "💡 be able to do は「～することができる」。that was acceptable to both of them は a deal を修飾する主格の関係代名詞節。both of them は交渉した the two sides を指す。",
    },
    {
        "number": 16,
        "text": "Miranda plans to become a politician someday, so she is careful not to do anything that could be ( 16 ) her in the future. She does not want a scandal to affect her chances of getting elected.",
        "translation": "ミランダはいつか政治家になるつもりなので、将来自分に ( 16 ) 可能性のあることは一切しないよう気をつけている。スキャンダルが当選の可能性に影響することを望んでいないのだ。",
        "choices": ["held against", "kept from", "grown into", "sailed through"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ held against＝（hold A against B の受動態）不利な材料とされる → 正解。💡 a scandal が当選の可能性に影響することを避けたいという第2文から、将来不利に使われるような行動を避けていると分かる。",
            "❌ kept from＝（keep A from B の受動態）Bに隠される・Bから遠ざけられる → 「彼女に隠されうること」では、スキャンダルを避けるという第2文につながらない。",
            "❌ grown into＝成長して～になる・（服が）合うようになる → anything that could be grown into her では意味が通らない。",
            "❌ sailed through＝楽々と切り抜ける → 人を目的語にして「彼女を楽々と切り抜ける」とは言えない。",
        ],
        "grammar": "💡 hold A against B は「AのことでBを悪く思う・Bに不利に扱う」。受動態にすると A be held against B となり、anything that could be held against her は「彼女に不利に使われうるもの」。want O to do は「Oに～してほしい」。",
    },
    {
        "number": 17,
        "text": "Debt adds up quickly, so people with credit cards must be careful not to ( 17 ) large bills before checking how much they have spent.",
        "translation": "借金はすぐに膨らむので、クレジットカードを持つ人は、自分がいくら使ったかを確認する前に高額の請求を ( 17 ) ないよう注意しなければならない。",
        "choices": ["phase out", "swear by", "rub in", "run up"],
        "answer": 4,
        "choiceAnalysis": [
            "❌ phase out＝段階的に廃止する → 制度や製品を少しずつなくす語で、請求額について注意する内容に合わない。",
            "❌ swear by＝～を信頼して推奨する → 効果を信じている物事に使い、large bills とは結びつかない。",
            "❌ rub in＝すり込む・（嫌なことを）しつこく言う → rub it in の形で使うことが多く、請求を重ねる意味はない。",
            "✅ run up＝（借金・請求額を）ためる → 正解。💡 Debt adds up quickly と how much they have spent から、使いすぎて高額の請求をためることへの注意だと分かる。",
        ],
        "grammar": "💡 add up は「（少しずつ）積み重なる」。be careful not to do は「～しないよう気をつける」。how much they have spent は間接疑問で checking の目的語。",
    },
    {
        "number": 18,
        "text": "When the villagers heard a major typhoon was coming, they ( 18 ) preparing for the storm. They knew they had to hurry for their own safety.",
        "translation": "大型の台風が近づいていると聞くと、村人たちは嵐への備えに ( 18 ) 。自分たちの安全のために急がなければならないと分かっていたのだ。",
        "choices": ["set about", "took after", "brought down", "called on"],
        "answer": 1,
        "choiceAnalysis": [
            "✅ set about＝～に取りかかる → 正解。💡 set about doing は「～し始める・～に取りかかる」。後ろに動名詞 preparing が続き、第2文の had to hurry とも合う。",
            "❌ took after＝～に似ていた → 親族などに外見や性格が似ている意味で、準備を始める行動を表さない。",
            "❌ brought down＝～を倒した・下げた → 「準備を倒した」では意味が通らない。",
            "❌ called on＝～を訪問した・～に求めた → call on O to do の形で使い、preparing を目的語にとって準備を始める意味にはならない。",
        ],
        "grammar": "💡 set about doing は「～に取りかかる」。heard (that) a major typhoon was coming は接続詞 that の省略と時制の一致で、過去進行形 was coming は「近づいてきている」という近い未来を表す。",
    },
]

SECTION = {
    "name": "大問1",
    "nameEn": "Part 1",
    "type": "vocabulary",
    "instruction": "次の(1)から(18)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。",
    "questions": QUESTIONS,
}


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Base data does not exist: {DATA_PATH}. Run gen_pre1_2026-2.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    sections = data.get("sections")
    if not isinstance(sections, list):
        raise ValueError("data.json must contain a top-level 'sections' list")

    retained = [
        section
        for section in sections
        if not (
            isinstance(section, dict)
            and (section.get("type") == "vocabulary" or section.get("name") == "大問1")
        )
    ]
    data["sections"] = [SECTION, *retained]

    with DATA_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)
        handle.write("\n")

    print(f"Installed Part 1 (Q1-Q18) in {DATA_PATH}")


if __name__ == "__main__":
    main()
