"""Original four chunks/fixed frames (2026-2 main venue); derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"ジョン，どちらのカレンダーが欲しいですか？",["do","calendar","you","want"],[2,1,3,4],"John, which","?",["①−②","②−③","④−②","③−①"],2,
     "which＋名詞で『どちらの～』。続けて疑問文の語順 do you want を置く。calendar→do→you→want の順。John, which は固定部分で、空所の位置に数えない。",
     "『どちらのカレンダー』は which calendar。そのあとに do you want（ほしいですか）。John, which はかぞえないよ。"),
    (22,"私の母はうまく踊ることができません。",["well","can't","dance","my mother"],[4,2,3,1],"",".",["④−③","③−②","①−②","②−①"],1,
     "can't＋動詞の原形で『～できない』。主語 my mother の後ろに can't と原形 dance を続け、『上手に』の well は最後に置く。my mother→can't→dance→well の順。",
     "『わたしのははは』の my mother からはじめよう。『おどれない』は can't dance。well は『じょうずに』で、さいごにおくよ。"),
    (23,"あのバレーボール選手はイタリア出身です。",["is","volleyball","player","from"],[2,3,1,4],"That","Italy.",["①−②","③−④","①−④","②−①"],4,
     "be from＋場所で『～の出身だ』。主語は That volleyball player。volleyball→player→is→from の順。固定の That と Italy. は空所の位置に数えない。",
     "『あのバレーボールせんしゅ』は That volleyball player。『～しゅっしん』は is from。That と Italy はかぞえないよ。"),
    (24,"映画の券はいくらですか。",["is","a movie ticket","how","much"],[3,4,1,2],"","?",["③−①","③−②","②−①","②−④"],1,
     "How much is ～? は『～はいくらですか』と値段を尋ねる形。how much の後ろに is、最後に主語 a movie ticket を置く。how→much→is→a movie ticket の順。",
     "『いくら？』は How much のセット。そのあとに is、さいごに a movie ticket（えいがのけん）をおくよ。"),
    (25,"私は今，パソコンを使っていません。",["the computer","not","I'm","using"],[3,2,4,1],"","now.",["①−③","①−②","③−④","③−①"],3,
     "現在進行形の否定文は be動詞＋not＋動詞のing形。I'm（I am）のすぐ後ろに not を置く。I'm→not→using→the computer の順。固定の now. は空所の位置に数えない。",
     "『つかっていない』は I'm not using のじゅんばん。I'm のすぐあとに not をおくよ。now はかぞえないよ。"),
]

def completed(q):
    s=" ".join([q["framePrefix"],*[q["words"][i-1] for i in q["correctOrder"]],q["frameSuffix"]]).strip()
    s=re.sub(r"\s+([.,?!])",r"\1",s)
    return s[0].upper()+s[1:]

def questions():
    result=[]
    for n,ja,words,order,prefix,suffix,choices,answer,note,simple in ROWS:
        q=dict(number=n,text=ja,translation=ja,words=words,correctOrder=order,framePrefix=prefix,
               frameSuffix=suffix,answerSlots=SLOTS.copy(),choices=choices,answer=answer)
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
