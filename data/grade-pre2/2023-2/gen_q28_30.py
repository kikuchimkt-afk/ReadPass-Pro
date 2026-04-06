"""Generate Q28-30 for Pre-2 2023-2 (page 6 - Part 3B: The Return of Greeting Cards)"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

passage_3b = {
    "title": "The Return of Greeting Cards",
    "passage": "During the 20th century, people often sent paper greeting cards to friends and family members on birthdays or at other special times. Greeting cards usually have a picture on the front and a message inside. In the 1990s, however, people began communicating online. Sending an electronic message by e-mail or through social media is quicker and easier than sending a paper greeting card. In addition, most greeting cards are thrown away. This creates a lot of trash. As a result, some people prefer online communication because they think it is ( 28 ).\nFor several years, sales of greeting cards in the United States went down. Recently, though, young adults have become interested in greeting cards. Many of them think that it is too easy to send a message online. Sending a greeting card to a person ( 29 ). It shows that you really care about that person. Because of this, Americans still buy around 6.5 billion greeting cards every year.\nAlthough people once thought that the Internet might be bad for sales of greeting cards, it may actually be helping them. This is because people who use social media are often ( 30 ). For example, they may be sent a message to tell them that one of their friends has a birthday or wedding anniversary soon. As a result, they remember to buy a greeting card and send it to their friend.",
    "passageTranslation": "20世紀、人々は誕生日やその他の特別な時に友人や家族に紙のグリーティングカードを送ることが多かった。グリーティングカードは通常、表に絵があり中にメッセージがある。しかし1990年代にはオンラインでコミュニケーションするようになった。メールやソーシャルメディアで電子メッセージを送る方が紙のカードより速くて簡単だ。さらにほとんどのカードは捨てられ、多くのゴミになる。そのため、オンラインの方が( 28 )と考える人もいる。\n数年間、アメリカでのグリーティングカードの売り上げは下がった。しかし最近、若い大人がグリーティングカードに関心を持つようになった。オンラインでメッセージを送るのは簡単すぎると考える人も多い。人にカードを送ることは( 29 )。その人のことを本当に大切に思っていることを示す。そのためアメリカ人は今でも毎年約65億枚のカードを購入している。\nインターネットがカードの売り上げに悪影響を与えるかもしれないと思われていたが、実際には助けになっているかもしれない。ソーシャルメディアを使う人々はしばしば( 30 )からだ。たとえば友人の誕生日や結婚記念日が近いというメッセージが送られることがある。その結果、グリーティングカードを買って友人に送ることを思い出す。",
    "questions": [
        {"number":28,"text":"( 28 )","translation":"( 28 )に入る最も適切なもの","choices":["easier to talk in private","better for the environment","creating many jobs","new and exciting"],"choiceTranslations":["プライベートで話しやすい","環境に良い","多くの仕事を生んでいる","新しくてワクワクする"],"answer":2,"choiceAnalysis":["❌ 1。プライベートの話ではない","✅ 2＝環境に良い→正解。カードがゴミになる問題を受けて","❌ 3。雇用の話ではない","❌ 4。文脈に合わない"],"grammar":"💡 be better for the environment＝環境に良い。throw away＝捨てる。trash＝ゴミ。"},
        {"number":29,"text":"( 29 )","translation":"( 29 )に入る最も適切なもの","choices":["takes more effort","can lead to problems","is not always possible","may not change anything"],"choiceTranslations":["より多くの労力がかかる","問題を引き起こしうる","常に可能ではない","何も変わらないかも"],"answer":1,"choiceAnalysis":["✅ 1＝より多くの労力がかかる→正解。簡単すぎるオンラインとの対比","❌ 2。問題の話ではない","❌ 3。文脈に合わない","❌ 4。大切に思っている証拠の話"],"grammar":"💡 take effort＝労力がかかる。care about＝～を大切に思う。"},
        {"number":30,"text":"( 30 )","translation":"( 30 )に入る最も適切なもの","choices":["invited to play games","sent photos of food","reminded about events","shown advertisements"],"choiceTranslations":["ゲームに招待される","食べ物の写真を送られる","イベントを思い出させられる","広告を見せられる"],"answer":3,"choiceAnalysis":["❌ 1。ゲームの話ではない","❌ 2。食べ物の話ではない","✅ 3＝イベントを思い出させられる→正解。誕生日・記念日の通知","❌ 4。広告の話ではない"],"grammar":"💡 be reminded about＝～を思い出させられる。anniversary＝記念日。"}
    ]
}

out = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2"
with open(os.path.join(out, "_q28_30.json"), "w", encoding="utf-8") as f:
    json.dump(passage_3b, f, ensure_ascii=False, indent=2)
print(f"Saved Q28-30 (3B): {len(passage_3b['questions'])} questions")
