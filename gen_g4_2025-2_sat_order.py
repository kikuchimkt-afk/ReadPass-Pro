"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"恵理は昨日，彼女の叔母に会う時間がありませんでした。",["have","did","time","not","to"],[2,4,1,3,5],"Eri","see her aunt yesterday.",["⑤−④","③−④","④−③","⑤−①"],3,
     "主語 Eri の後ろに did not を置いて過去の否定文にする。did not の後ろは動詞の原形 have。have time to＋動詞の原形で『～する時間がある』。to の後ろに固定の see her aunt が続く。",
     "『じかんがなかった』は did not have time。time のあとに to をおいて、see her aunt『おばにあう』につなげよう。"),
    (22,"私の庭にはたくさんの種類の花があります。",["flowers","in","kinds","many","of"],[4,3,5,1,2],"I have","my garden.",["④−②","②−⑤","③−①","④−③"],3,
     "日本文は『～があります』だが、英語は固定の I have（私は持っている）で表す。many kinds of＋名詞で『たくさんの種類の～』。kinds は kind の複数形で many と合う。in my garden が場所。",
     "many kinds of flowers は『たくさんのしゅるいのはな』。そのあとに in my garden『わたしのにわに』をつけよう。"),
    (23,"すてきなお葉書をどうもありがとうございました。",["for","very","the nice","much","you"],[5,2,4,1,3],"Thank","postcard.",["④−②","⑤−③","②−①","③−④"],3,
     "Thank you very much で『どうもありがとう』。very much は very→much の順。お礼の理由は for＋名詞で後ろに加える。the nice は1つの語句で、文末の postcard とつながり the nice postcard（すてきな葉書）になる。",
     "Thank you very much は『どうもありがとう』のセット。for のあとに、おれいのりゆう『すてきなはがき』をつなげよう。"),
    (24,"キャシー，何か手伝いましょうか。",["do","need","some","you","help"],[1,4,2,3,5],"Kathy,","?",["④−③","④−⑤","①−②","①−③"],1,
     "英語では Do you need some help?（手助けが必要ですか）と尋ねて、手伝いを申し出る。一般動詞 need の疑問文なので do→you→need の順。some help で『いくらかの手助け』。",
     "『てつだおうか？』は、えいごでは『てつだいがいる？』ときくよ。do you need のじゅんばんで、さいごに some help だね。"),
    (25,"私は母から料理を学びました。",["to","my","learned","from","cook"],[3,1,5,4,2],"I","mother.",["①−④","①−②","③−⑤","③−④"],1,
     "主語 I の後ろに learn の過去形 learned。learn to＋動詞の原形で『～するようになる・～を身につける』なので learned to cook。from my mother は『母から』で、教わった相手を示す。",
     "learned to cook は『りょうりをまなんだ』。from my mother『おかあさんから』をあとにつけよう。"),
]


def completed(q):
    s=" ".join([q["framePrefix"],*[q["words"][i-1] for i in q["correctOrder"]],q["frameSuffix"]]).strip()
    s=re.sub(r"\s+([.,?!])",r"\1",s)
    return s[0].upper()+s[1:]


def questions():
    result=[]
    for n,ja,words,order,prefix,suffix,choices,answer,note,simple in ROWS:
        q=dict(number=n,text=ja,words=words,correctOrder=order,framePrefix=prefix,
               frameSuffix=suffix,answerSlots=[2,4],choices=choices,answer=answer,questionAudio=f"audio/q{n}.mp3")
        sent=completed(q)
        good=[order[1],order[3]]
        trail="→".join(f"{CIRCLES[i-1]}{words[i-1]}" for i in order)
        q["grammar"]=f"完成文は「{sent}」。{note} 語句の順序は {trail}。空所2番目は{CIRCLES[good[0]-1]}「{words[good[0]-1]}」、4番目は{CIRCLES[good[1]-1]}「{words[good[1]-1]}」。"
        q["grammarSimple"]=f"「{sent}」が正しい文。{simple} 2ばんめは「{words[good[0]-1]}」、4ばんめは「{words[good[1]-1]}」だよ。"
        normal,easy=[],[]
        for index,c in enumerate(choices,1):
            nums=[CIRCLES.index(x)+1 for x in c if x in CIRCLES]
            a,b=[words[i-1] for i in nums]
            positions=f"2番目={CIRCLES[nums[0]-1]}「{a}」、4番目={CIRCLES[nums[1]-1]}「{b}」。"
            if index==answer:
                normal.append("○ "+positions+f"{sent} の語順に一致する。")
                easy.append(f"○ 2ばんめ「{a}」、4ばんめ「{b}」。正しい文になるね。")
            else:
                errors=[f"{slot}番目は「{words[g-1]}」が必要で「{words[v-1]}」ではない" for slot,g,v in zip([2,4],good,nums) if g!=v]
                normal.append(positions+"。".join(errors)+f"。{note}")
                easy.append(f"2ばんめ「{a}」、4ばんめ「{b}」ではならびがくずれるよ。正しくは「{words[good[0]-1]}」と「{words[good[1]-1]}」。")
        q["choiceAnalysis"],q["choiceAnalysisSimple"]=normal,easy
        result.append(q)
    return result
