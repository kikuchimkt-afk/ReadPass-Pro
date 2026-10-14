"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"ジョージ，あなたはとても親切です。",["very","you","kind","are"],[2,4,1,3],"George,",".",["②−①","④−③","③−④","①−③"],1,
     "主語 you に合う be動詞は are。be動詞の後ろに very kind（とても親切な）を続け、you→are→very→kind の順に並べる。very は kind の前に置いて意味を強める。George, はジョージへの呼びかけで、4つの空所の位置には数えない。",
     "『あなたは とても しんせつ』は you are very kind。very は kind のまえにおくよ。George, はさいしょからかいてあるので、かぞえないよ。"),
    (22,"あなたのピアノのコンサートはいつですか。",["is","when","your","piano"],[2,1,3,4],"","concert?",["①−②","②−③","③−①","④−②"],2,
     "『いつ』を尋ねる When で始まる疑問文。be動詞 is を主語の前に出し、when→is→your→piano の順に並べる。主語は your piano concert（あなたのピアノのコンサート）で、固定の concert? につなぐ。",
     "『いつ？』は When。そのあとに is、つぎに your piano とつづけて、さいごの concert? につなぐよ。"),
    (23,"ジュディ，あなたのお姉さんはどうやってピアノを練習しますか。",["practice","how","your sister","does"],[2,4,3,1],"Judy,","the piano?",["③−④","①−③","②−①","②−③"],4,
     "How は『どうやって』。一般動詞の疑問文なので、how の後ろに does＋主語 your sister＋動詞の原形 practice を置き、how→does→your sister→practice の順に並べる。your sister は1つのかたまり。Judy, は呼びかけで、空所の位置には数えない。",
     "『どうやって？』は How。How does your sister practice ～? のじゅんだよ。your sister はひとつのかたまり。Judy, はかぞえないよ。"),
    (24,"あなたはいつ野球をしますか。",["play","you","do","when"],[4,3,2,1],"","baseball?",["③−①","④−②","②−③","①−④"],2,
     "When do you＋動詞の原形 ～? で『あなたはいつ～しますか』。when→do→you→play の順に並べ、固定の baseball? につなぐ。play baseball は『野球をする』。",
     "『いつ？』の When からはじめて、do you play とつづけるよ。play baseball は『やきゅうをする』だね。"),
    (25,"夕飯前にはクッキーを食べないで。",["eat","before","dinner","cookies"],[1,4,2,3],"Don't",".",["①−②","①−③","②−①","②−③"],1,
     "Don't＋動詞の原形で『～しないで』という否定の命令文。Don't の後ろに eat、食べない物 cookies、時を表す before dinner（夕飯前に）を続け、eat→cookies→before→dinner の順に並べる。Don't と文末の . は固定部分。",
     "『～しないで』は Don't のあとに うごきのことば。eat cookies（クッキーをたべる）のあとに before dinner（ゆうはんのまえ）をつけるよ。"),
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
