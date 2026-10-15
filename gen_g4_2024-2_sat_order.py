"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"今夜は早くお風呂に入ったほうがいいですよ。",["bath","you","a","should","take"],[2,4,5,3,1],"","early tonight.",["④−③","②−④","⑤−①","③−①"],1,
     "should＋動詞の原形で『～したほうがよい』。主語 you の後ろに should、その後ろに動詞の原形 take を置く。take a bath で『お風呂に入る』。文のはじめにくる you も（　）の中では小文字で書かれている。",
     "『～したほうがいい』は should。you should take a bath『おふろにはいったほうがいい』とならべよう。"),
    (22,"私は放課後，自分の部屋をそうじしなければいけません。",["clean","have","after","my room","to"],[2,5,1,4,3],"I","school.",["⑤−④","②−①","⑤−③","②−④"],1,
     "have to＋動詞の原形で『～しなければならない』。主語 I の後ろに have to、その後ろに動詞の原形 clean と、そうじする物 my room を続ける。after school で『放課後』。my room は1つの語句として数える。",
     "『～しなければいけない』は have to。have to clean my room『へやをそうじしなければ』のあとに after school『ほうかご』だよ。"),
    (23,"雪が降っていたので，デールは友達とテニスをすることができませんでした。",["tennis","his friends","because","play","with"],[4,1,5,2,3],"Dale couldn't","it was snowing.",["④−⑤","③−①","③−②","①−②"],4,
     "couldn't（could not の短縮形）の後ろは動詞の原形なので play。play tennis with his friends で『友達とテニスをする』。because＋主語＋動詞で『～なので』と理由を加えるので、because の後ろに文末の it was snowing（雪が降っていた）が続く。his friends は1つの語句として数える。",
     "couldn't play tennis『テニスができなかった』。with his friends『ともだちと』のあとに because『～なので』をおこう。"),
    (24,"すみません。京都へ行く電車はどれですか。",["Kyoto","train","which","to","goes"],[3,2,5,4,1],"Excuse me.","?",["②−④","④−③","⑤−①","⑤−③"],1,
     "Which＋名詞で『どの～』。この文では Which train（どの電車）が主語なので、その後ろに動詞 goes を続ける。go to ～で『～へ行く』。Excuse me. で文が一度終わり、which から新しい文が始まるが、（　）の中では文のはじめの語も小文字で書かれている。",
     "『どのでんしゃ』は which train。そのあとに goes to Kyoto『きょうとへいく』をつづけよう。"),
    (25,"私はこの通りの角でジャックに会いました。",["of","Jack","the corner","met","at"],[4,2,5,3,1],"I","this street.",["②−③","④−②","②−①","④−③"],1,
     "主語 I の後ろに meet の過去形 met と、会った相手 Jack を置く。at the corner of ～で『～の角で』となり、of の後ろに文末の this street が続く。the corner は1つの語句として数える。",
     "I met Jack『ジャックにあった』。at the corner of this street『このとおりのかどで』とつづけよう。"),
]


def completed(q):
    chunks=[q["words"][i-1] for i in q["correctOrder"]]
    # A frame that already ends a sentence ("Excuse me.") is followed by a new sentence,
    # whose first word the booklet prints in lower case inside the parentheses.
    if re.search(r"[.?!]$",q["framePrefix"]): chunks[0]=chunks[0][:1].upper()+chunks[0][1:]
    s=" ".join([q["framePrefix"],*chunks,q["frameSuffix"]]).strip()
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
