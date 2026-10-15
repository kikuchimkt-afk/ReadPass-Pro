"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"ナンシーさん，あなたは何色が好きですか。",["like","do","color","you"],[3,2,4,1],"What",", Nancy?",["②−③","③−④","③−①","①−②"],2,
     "『何色』は What color で表し、固定の What の後ろに color を続けて1つのまとまりにする。そのあとに一般動詞の疑問文の形 do＋主語 you＋動詞 like（好きだ）を続け、color→do→you→like の順に並べる。固定の , Nancy? は名前の呼びかけ。",
     "『なにいろ？』は What color。そのあとに do you like（すきですか）を つづけるよ。さいごの Nancy は よびかけだね。"),
    (22,"ケイトは私の姉の友達です。",["Kate","my","is","sister's"],[1,3,2,4],"","friend.",["①−②","③−④","④−②","②−①"],1,
     "主語 Kate の後ろに be動詞 is を置き、『私の姉の友達』を my sister's friend で表して Kate→is→my→sister's の順に並べる。sister's の 's は『～の』で、固定の friend. が最後に来る。sister は『姉』にも『妹』にも使う。",
     "『ケイトは～です』は Kate is。『わたしの あねの ともだち』は my sister's friend だよ。's は『～の』だね。"),
    (23,"椅子の上に立ってはいけません。",["the chair","stand","don't","on"],[3,2,4,1],"",".",["②−④","③−①","③−④","②−①"],3,
     "『～してはいけません』は Don't＋動詞の原形の命令文。don't の後ろに stand（立つ）を置き、場所を表す on the chair（椅子の上に）を続けて don't→stand→on→the chair の順に並べる。the chair は1つのかたまり。文の始めの don't も（　）の中では小文字で書かれている。",
     "『～しては いけません』は Don't で はじめるよ。そのあとに stand（たつ）、on the chair（いすの うえに）だね。"),
    (24,"土曜日にキャンプに行きましょう。",["go","on","Saturday","camping"],[1,4,2,3],"Let's",".",["②−④","③−④","①−②","④−①"],3,
     "Let's＋動詞の原形で『～しましょう』と誘う文。固定の Let's の後ろに go を置き、go camping（キャンプに行く）をまとまりにして、曜日を表す on Saturday（土曜日に）を最後に続け、go→camping→on→Saturday の順に並べる。『～曜日に』は on＋曜日 で表し、Saturday は曜日の名前なので大文字で始まる。",
     "Let's の あとは go。go camping で『キャンプに いく』、on Saturday で『どようびに』だよ。"),
    (25,"私は学校へ歩いて行きません。",["don't","to","walk","I"],[4,1,3,2],"","school.",["③−①","④−③","①−②","②−①"],2,
     "主語が I の一般動詞の否定文は 主語＋don't＋動詞の原形（主語が he・she などなら doesn't を使う）。主語 I の後ろに don't、動詞 walk（歩く）を続け、walk to school（歩いて学校へ行く）となるように to を置いて I→don't→walk→to の順に並べる。固定の school. が最後に来る。I（私は）は文のどこでも大文字で書く。",
     "『わたしは～しません』は I don't。walk to school で『あるいて がっこうへ いく』だよ。"),
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
