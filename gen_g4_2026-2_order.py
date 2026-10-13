"""Original word banks/frames/pairs (2026-2 main venue); explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"ピーターはサッカーの試合の前にボールを蹴る練習をしました。",["the ball","kicking","the soccer game","practiced","before"],[4,2,1,5,3],"Peter",".",["①−③","②−⑤","③−②","④−②"],2,
     "主語 Peter の後ろに過去形 practiced。practice＋～ing で『～する練習をする』なので practiced kicking the ball。before the soccer game（試合の前に）は最後に置く。",
     "practiced kicking the ball は『ボールをけるれんしゅうをした』。さいごに before the soccer game をつけよう。"),
    (22,"図書館では静かにしなくてはいけません。",["in","must","you","quiet","be"],[3,2,5,4,1],"","the library.",["②−④","②−⑤","⑤−①","⑤−④"],1,
     "主語 You の後ろに助動詞 must。must の後ろは動詞の原形なので be を置き、be quiet で『静かにする』。in the library は場所を表し、in の後ろに the library が続く。",
     "You must は『あなたは～しなければならない』。must のあとは be quiet で『しずかにする』。さいごに in the library だよ。"),
    (23,"私は昨日の朝，5時に家を出て学校へ向かいました。",["at","school","left","for","home"],[3,5,4,2,1],"I","five o'clock yesterday morning.",["①−⑤","⑤−②","③−④","③−⑤"],2,
     "主語 I の後ろに leave の過去形 left。leave home for school で『学校へ向かって家を出る』となり、for は向かう先を示す。at を最後に置き、five o'clock（5時に）につなぐ。",
     "left home は『いえをでた』。for school で『がっこうへむかって』。at five o'clock は『5じに』だよ。"),
    (24,"あの店にはたくさんの種類のアイスクリームがあります。",["kinds","has","of","that shop","many"],[4,2,5,1,3],"","ice cream.",["①−④","②−①","⑤−③","③−④"],2,
     "主語 That shop の後ろに動詞 has。店に品物があると言うときは have（has）を使える。many kinds of ～ で『たくさんの種類の～』となり、many→kinds→of の順は崩さない。",
     "That shop has は『あのおみせには～がある』。many kinds of は『たくさんのしゅるいの』というセットだよ。"),
    (25,"この机はジャックには大きすぎます。",["is","for","big","too","desk"],[5,1,4,3,2],"This","Jack.",["①−③","④−①","②−⑤","⑤−③"],1,
     "主語 This desk の後ろに be 動詞 is。too＋形容詞＋for＋人で『人にとって～すぎる』となり、too big for Jack は『ジャックには大きすぎる』。desk は This の直後に置き、主語のまとまりを作る。",
     "This desk is は『このつくえは～だ』。too big は『おおきすぎる』。for Jack で『ジャックには』だよ。"),
]


def completed(q):
    s=" ".join([q["framePrefix"],*[q["words"][i-1] for i in q["correctOrder"]],q["frameSuffix"]]).strip()
    s=re.sub(r"\s+([.,?!])",r"\1",s)
    return s[0].upper()+s[1:]


def questions():
    result=[]
    for n,ja,words,order,prefix,suffix,choices,answer,note,simple in ROWS:
        q=dict(number=n,text=ja,words=words,correctOrder=order,framePrefix=prefix,
               frameSuffix=suffix,answerSlots=[2,4],choices=choices,answer=answer)
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
                easy.append(f"2ばんめ「{a}」、4ばんめ「{b}」ではセットがくずれるよ。正しくは「{words[good[0]-1]}」と「{words[good[1]-1]}」。")
        q["choiceAnalysis"],q["choiceAnalysisSimple"]=normal,easy
        result.append(q)
    return result
