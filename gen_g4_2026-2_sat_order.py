"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"あなたのクラスで一番背が高いのはだれですか。",["who","in","the","tallest","is"],[1,5,3,4,2],"","your class?",["③−①","⑤−①","②−③","⑤−④"],4,
     "who が主語で、is が動詞。the tallest は『一番背が高い』という最上級。in your class が比べる範囲。who→is→the tallest→in your class の順に組み立てる。",
     "だれ、は who。is のあとに『いちばんせがたかい』の the tallest。そのあとに『あなたのクラスで』をつけよう。"),
    (22,"イアンは中学生の時，自転車に乗って学校へ行きました。",["when","to","rode","school","his bike"],[3,5,2,4,1],"Ian","he was in junior high school.",["⑤−②","①−②","⑤−④","③−④"],3,
     "主語 Ian の後ろに、ride の過去形 rode。rode his bike は『自転車に乗った』、to school は行き先。when he was ... は『～だった時』で、文の最後に時期を加える。",
     "Ian のあとに『のった』の rode。his bike をつけて『じてんしゃにのった』。to school は『がっこうへ』、when は『～のとき』だよ。"),
    (23,"テレビを見るのをやめて寝なさい，マイク。",["watching","and","stop","TV","go to"],[3,1,4,2,5],"","bed, Mike.",["①−②","①−⑤","③−⑤","⑤−②"],1,
     "命令文は動詞 Stop から始める。stop watching TV は『テレビを見るのをやめる』。and で次の命令 go to bed（寝る）につなぐ。stop の後ろは watching で、原形 watch にはしない。",
     "Stop watching TV は『テレビをみるのをやめて』。and でつないで go to bed は『ねなさい』。さいごの Mike は、よびかけだよ。"),
    (24,"生徒たちは校歌を歌い始めました。",["to","began","school song","their","sing"],[2,1,5,4,3],"The students",".",["①−④","②−⑤","①−③","②−③"],1,
     "主語 The students の後ろは begin の過去形 began。begin to＋動詞の原形で『～し始める』なので began to sing。目的語は their school song で、their が school song を前から説明する。",
     "『うたいはじめた』は began to sing のセット。さいごに『じぶんたちのこうか』の their school song をつけよう。"),
    (25,"ライアンは台所で水を一杯飲んでいました。",["water","drinking","of","was","a glass"],[4,2,5,3,1],"Ryan","in the kitchen.",["②−④","⑤−④","②−③","⑤−①"],3,
     "主語 Ryan の後ろに was drinking で『飲んでいた』という過去進行形。a glass of water は『コップ一杯の水』で、a glass→of→water を崩さない。最後の in the kitchen は場所。",
     "was drinking は『のんでいた』。a glass of water は『コップいっぱいのみず』のセット。さいごに『だいどころで』をつけよう。"),
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
                easy.append(f"2ばんめ「{a}」、4ばんめ「{b}」ではセットがくずれるよ。正しくは「{words[good[0]-1]}」と「{words[good[1]-1]}」。")
        q["choiceAnalysis"],q["choiceAnalysisSimple"]=normal,easy
        result.append(q)
    return result
