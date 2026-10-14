"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"ケイト，どちらがあなたの筆箱ですか。",["is","pencil case","which","your"],[3,1,4,2],"Kate,","?",["③−④","③−①","①−④","①−②"],1,
     "『どちらがあなたの筆箱ですか』は Which is your pencil case? の形。which のすぐ後ろに is を置き、その後に your pencil case（あなたの筆箱）を続けて which→is→your→pencil case の順に並べる。pencil case は1つのかたまり。Kate, はケイトへの呼びかけで、4つの空所の位置には数えない。",
     "『どちらが？』は Which。Which is your pencil case? のじゅんだよ。pencil case はひとつのかたまり。Kate, はさいしょからかいてあるので、かぞえないよ。"),
    (22,"今日は曇っていません。",["it","cloudy","is","not"],[1,3,4,2],"","today.",["④−②","②−③","①−④","③−④"],3,
     "天気を言うときは、このように it を主語にすることが多い。この it は『それ』と訳さない。be動詞の否定文なので is の後ろに not を置き、it→is→not→cloudy の順に並べる。cloudy は『曇った』。固定の today.（今日は）につなぐ。",
     "てんきをいうときは、it ではじめることがおおいよ。『くもっていない』は is not cloudy。not は is のあとにおくよ。"),
    (23,"私の絵はその壁にかかっています。",["on","wall","the","is"],[4,1,3,2],"My picture",".",["①−④","④−③","②−①","③−④"],2,
     "主語 My picture（私の絵）の後ろに be動詞 is を置き、場所を表す on the wall（その壁に）を続けて is→on→the→wall の順に並べる。on は物の表面にくっついていることを表し、壁にかかっている絵にも使う。the は wall の前に置く。My picture と文末の . は固定部分。",
     "『わたしのえは かべにある』は My picture is on the wall.。on は『～にくっついて』。the は wall のまえだよ。My picture はかぞえないよ。"),
    (24,"エミは，あなたの誕生パーティーに来ることができますか。",["come to","Emi","can","your"],[3,2,1,4],"","birthday party?",["④−①","②−④","③−①","③−④"],3,
     "『～できますか』は Can＋主語＋動詞の原形 ～? の疑問文。can を主語 Emi の前に出し、can→Emi→come to→your の順に並べて、固定の birthday party? につなぐ。come to ～ は『～に来る』で1つのかたまり。主語が Emi でも、can の後ろの come は原形のまま。",
     "『～できますか』は Can ではじめるよ。Can Emi come to ～? のじゅん。come to はひとつのかたまりだね。"),
    (25,"恵子のクラスには生徒が20人います。",["class","Keiko's","twenty","has"],[2,1,4,3],"","students.",["②−③","④−①","①−④","②−④"],4,
     "日本文は『～には…がいる』だが、英語では Keiko's class（恵子のクラス）を主語にして has（持っている）で表す。主語の Keiko's class は3人称単数なので have ではなく has。Keiko's→class→has→twenty の順に並べ、固定の students.（生徒）につなぐ。twenty students は『20人の生徒』。",
     "『けいこのクラスには せいとが20にんいる』は、クラスがせいとを『もっている』とかんがえて has をつかうよ。Keiko's class has twenty students. のじゅんだね。"),
]

def completed(q):
    s=" ".join([q["framePrefix"],*[q["words"][i-1] for i in q["correctOrder"]],q["frameSuffix"]]).strip()
    s=re.sub(r"\s+([.,?!])",r"\1",s)
    return s[0].upper()+s[1:]

def questions():
    result=[]
    for n,ja,words,order,prefix,suffix,choices,answer,note,simple in ROWS:
        q=dict(number=n,text=ja,translation=ja,words=words,correctOrder=order,framePrefix=prefix,
               frameSuffix=suffix,answerSlots=SLOTS.copy(),choices=choices,answer=answer,questionAudio=f"audio/q{n}.mp3")
        sent=completed(q);good=[order[s-1] for s in SLOTS]
        assert choices[answer-1]=="−".join(CIRCLES[i-1] for i in good)
        trail="→".join(f"{CIRCLES[i-1]}{words[i-1]}" for i in order)
        q["grammar"]=f"完成文は「{sent}」。{note} 語句の順序は {trail}。空所1番目は{CIRCLES[good[0]-1]}「{words[good[0]-1]}」、3番目は{CIRCLES[good[1]-1]}「{words[good[1]-1]}」。"
        q["grammarSimple"]=f"「{sent}」が正しい文。{simple} 1ばんめは「{words[good[0]-1]}」、3ばんめは「{words[good[1]-1]}」だよ。"
        normal,easy=[],[]
        for index,c in enumerate(choices,1):
            nums=[CIRCLES.index(x)+1 for x in c if x in CIRCLES]
            a,b=[words[i-1] for i in nums]
            positions=f"1番目={CIRCLES[nums[0]-1]}「{a}」、3番目={CIRCLES[nums[1]-1]}「{b}」。"
            if index==answer:
                normal.append("○ "+positions+f"{sent} の語順に一致する。")
                easy.append(f"○ 1ばんめ「{a}」、3ばんめ「{b}」。正しい文になるね。")
            else:
                errors=[f"{slot}番目は「{words[g-1]}」が必要で「{words[v-1]}」ではない" for slot,g,v in zip(SLOTS,good,nums) if g!=v]
                normal.append(positions+"。".join(errors)+f"。{note}")
                easy.append(f"1ばんめ「{a}」、3ばんめ「{b}」ではセットがくずれるよ。正しくは「{words[good[0]-1]}」と「{words[good[1]-1]}」。")
        q["choiceAnalysis"],q["choiceAnalysisSimple"]=normal,easy
        result.append(q)
    return result
