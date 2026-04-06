"""Generate Q26-27 for Pre-2 2023-2 (page 5 - Part 3A: Stephen's New School)"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

passage_3a = {
    "title": "Stephen's New School",
    "passage": "Stephen's family recently moved to a new city, and Stephen had to change schools. He did not know anyone at his new school, and he felt lonely every day. He ( 26 ) about his problem. Stephen's mother said that he would make new friends soon, and his father suggested joining one of the clubs at his new school. However, Stephen did not like sports, music, or art, so he did not know what to do.\nOne day, Stephen saw a poster at school for a games club. The members met three times a week to play board games and card games. Stephen really liked playing games, so he joined the club. The members were very kind, and Stephen quickly made friends. Recently, Stephen decided to ( 27 ). He has been working hard to make the rules and the other things he will need for the game. Once it is ready, he plans to try it with the other members of the club.",
    "passageTranslation": "スティーブンの家族は最近新しい都市に引っ越し、スティーブンは転校しなければならなかった。新しい学校には知り合いがおらず、毎日寂しく感じていた。彼は自分の問題について( 26 )。スティーブンの母はすぐに新しい友達ができると言い、父は新しい学校のクラブに入ることを勧めた。しかしスティーブンはスポーツ、音楽、美術が好きではなく、何をすべきかわからなかった。\nある日、スティーブンは学校でゲームクラブのポスターを見た。メンバーは週3回集まってボードゲームやカードゲームをしていた。スティーブンはゲームが大好きだったのでクラブに入った。メンバーはとても親切で、スティーブンはすぐに友達ができた。最近、スティーブンは( 27 )することに決めた。ゲームのルールや必要な物を一生懸命作っている。準備ができたらクラブのメンバーと一緒に試すつもりだ。",
    "questions": [
        {"number":26,"text":"( 26 )","translation":"( 26 )に入る最も適切なもの","choices":["read several books","wrote a long letter","saw a doctor","talked to his parents"],"choiceTranslations":["本を数冊読んだ","長い手紙を書いた","医者に行った","両親に話した"],"answer":4,"choiceAnalysis":["❌ 1。その後母と父が助言→話した","❌ 2。文脈に合わない","❌ 3。病気ではない","✅ 4＝両親に話した→正解。母と父の助言に繋がる"],"grammar":"💡 talk to＝～に話す。suggest doing＝～することを提案する。"},
        {"number":27,"text":"( 27 )","translation":"( 27 )に入る最も適切なもの","choices":["create his own game","join another club","change schools again","get more exercise"],"choiceTranslations":["自分のゲームを作る","別のクラブに入る","また転校する","もっと運動する"],"answer":1,"choiceAnalysis":["✅ 1＝自分のゲームを作る→正解。ルールを作りメンバーと試す","❌ 2。ゲームクラブを気に入っている","❌ 3。文脈に合わない","❌ 4。ゲームクラブの話"],"grammar":"💡 decide to＝～することに決める。work hard to＝～するために一生懸命努力する。"}
    ]
}

out = r"c:\Users\makoto\Documents\アプリ開発\ReadPass-Pro_Local\data\grade-pre2\2023-2"
with open(os.path.join(out, "_q26_27.json"), "w", encoding="utf-8") as f:
    json.dump(passage_3a, f, ensure_ascii=False, indent=2)
print(f"Saved Q26-27 (3A): {len(passage_3a['questions'])} questions")
