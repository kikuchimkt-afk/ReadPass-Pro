"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"あそこにいるあの男の子たちは誰ですか。",["are","those","boys","who"],[4,1,2,3],"","over there?",["②−③","④−②","②−④","④−①"],2,
     "人を尋ねる Who（誰）で始まる疑問文。who の後ろに be動詞 are、主語 those boys（あの男の子たち）を続け、who→are→those→boys の順に並べる。主語 those boys が複数なので be動詞は are。those は that の複数形で『あれらの・あの』。固定の over there?（あそこに）につなぐ。",
     "『だれ？』は Who。そのあとに are、つぎに those boys（あの おとこのこたち）だよ。さいごの over there? は『あそこに』だね。"),
    (22,"私は夕食前に宿題をします。",["dinner","do","before","my homework"],[2,4,3,1],"I",".",["①−③","②−③","②−④","④−③"],2,
     "do my homework で『宿題をする』。固定の主語 I の後ろに動詞 do、目的語 my homework を続け、時を表す before dinner（夕食前に）を最後に置いて do→my homework→before→dinner の順に並べる。before は『～の前に』で、後ろに dinner を置く。my homework は1つのかたまり。I と文末の . は固定部分。",
     "『しゅくだいを する』は do my homework。そのあとに before dinner（ゆうしょくの まえに）を つけるよ。I は さいしょから かいてあるね。"),
    (23,"昼食にスパゲッティを作りましょう。",["spaghetti","for","let's","make"],[3,4,1,2],"","lunch.",["②−①","②−④","③−①","③−④"],3,
     "Let's＋動詞の原形で『～しましょう』と誘う文。let's の後ろに make（作る）、作る物 spaghetti を続け、for lunch（昼食に）につなげて let's→make→spaghetti→for の順に並べる。for lunch の for は『～用に・～として』。文の始めの let's も（　）の中では小文字で書かれている。",
     "『～しましょう』は Let's。Let's make spaghetti（スパゲッティを つくろう）の あとに for lunch（ちゅうしょくに）が つづくよ。"),
    (24,"私はタナーさんの電話番号を知っています。",["Mr. Tanner's","I","telephone number","know"],[2,4,1,3],"",".",["①−④","②−①","③−①","④−②"],2,
     "主語 I＋動詞 know（知っている）の後ろに、知っているもの Mr. Tanner's telephone number（タナーさんの電話番号）を置き、I→know→Mr. Tanner's→telephone number の順に並べる。Mr. Tanner's の 's は『～の』。telephone number は1つのかたまり。文末の . は固定部分。",
     "『わたしは しっている』は I know。そのあとに Mr. Tanner's telephone number（タナーさんの でんわばんごう）を おくよ。's は『～の』だね。"),
    (25,"これはだれの野球帽ですか。",["is","cap","whose","baseball"],[3,4,2,1],"","this?",["②−①","③−②","③−①","④−③"],2,
     "『だれの～』は Whose＋名詞。Whose baseball cap（だれの野球帽）を1つのまとまりとして文の始めに置き、be動詞 is と固定の this? を続けて whose→baseball→cap→is の順に並べる。baseball cap は『野球帽』で、baseball が cap の前に来る。",
     "『だれの やきゅうぼう？』は Whose baseball cap。そのあとに is this? を つづけるよ。"),
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
