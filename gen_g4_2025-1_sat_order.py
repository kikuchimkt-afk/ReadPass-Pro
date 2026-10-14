"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"明子は英語とロシア語の両方を話すことができます。",["both","speak","English","can","and"],[4,2,1,3,5],"Akiko","Russian.",["④−①","④−⑤","②−③","②−④"],3,
     "主語 Akiko の後ろに助動詞 can、その後ろに動詞の原形 speak を置く。both A and B で『A と B の両方』なので、both English and の後ろに固定の Russian が続く。",
     "can speak は『はなすことができる』。both A and B『AとBのりょうほう』のかたちで、English と Russian をつなごう。"),
    (22,"私の家族は8月に車で北海道に行きました。",["to","my family","Hokkaido","by","went"],[2,5,1,3,4],"","car in August.",["③−⑤","③−②","⑤−①","⑤−③"],4,
     "主語は my family（私の家族）で、空所の最初に置く（文のはじめでも、選択肢では小文字）。went to＋場所で『～へ行った』。by＋乗り物で『～で（交通手段）』なので、by を固定の car の直前に置く。in August が時を表す。",
     "my family went to Hokkaido は『かぞくはほっかいどうへいった』。by car は『くるまで』だよ。"),
    (23,"私の姉は料理が得意ではありません。",["not","at","is","cooking","good"],[3,1,5,2,4],"My sister",".",["①−②","④−③","①−⑤","②−④"],1,
     "be good at ～ で『～が得意だ』。be 動詞の否定文は be 動詞の後ろに not を置くので is not good at。at の後ろに cooking（料理すること）を置く。",
     "good at は『～がとくい』。とくいではない、は is not good at だよ。さいごに cooking『りょうり』をおこう。"),
    (24,"妹は私よりじょうずにギターを弾きます。",["better","I","the guitar","plays","than"],[4,3,1,5,2],"My sister","do.",["④−②","③−④","③−⑤","①−④"],3,
     "主語 My sister は三人称単数なので plays。play the guitar で『ギターを弾く』。well（じょうずに）の比較級 better を使い、better than ～ で『～よりじょうずに』。than の後ろに I を置き、固定の do で終わる。do は play the guitar のくり返しを避けた語。",
     "plays the guitar『ギターをひく』のあとに better than I『わたしよりじょうずに』をつなげよう。"),
    (25,"私はこの面白い物語を何回も読みました。",["interesting story","and","this","again","read"],[5,3,1,4,2],"I","again.",["④−③","③−②","③−④","⑤−④"],3,
     "主語 I の後ろに動詞 read。過去のことなので過去形だが、read は過去形も同じつづり。目的語は this interesting story（この面白い物語）。again and again で『何度も』なので、again and の後ろに固定の again が続く。",
     "again and again は『なんども』。read this interesting story『このおもしろいものがたりをよんだ』のあとにつなげよう。"),
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
