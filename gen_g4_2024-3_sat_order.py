"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"あなたはきのう何時に帰宅しましたか。",["get","home","did","you","time"],[5,3,4,1,2],"What","yesterday?",["⑤−④","③−①","①−⑤","③−②"],2,
     "What time ～? で『何時に～』。一般動詞の過去の疑問文なので、What time の後ろに did＋主語 you＋動詞の原形 get を続ける。get home で『家に着く・帰宅する』。この home は『家へ』という意味なので、前に to を置かない。",
     "『なんじに』は What time。そのあとに did you get home『いえにかえった？』とつづけよう。"),
    (22,"私は祖母の絵を描き終えました。",["drawing","finished","picture","a","of"],[2,1,4,3,5],"I","my grandmother.",["⑤−④","②−①","②−③","①−③"],4,
     "主語 I の後ろに finish の過去形 finished。finish の後ろに『～すること』を続けるときは -ing 形にするので finished drawing（描き終えた）。a picture of ～で『～の絵』となり、文末の my grandmother とつながる。",
     "『かきおえた』は finished drawing。a picture of my grandmother は『おばあちゃんのえ』だよ。"),
    (23,"私は紅茶を飲む時はこのカップを使います。",["drink","use","when","this cup","I"],[2,4,3,5,1],"I","tea.",["④−⑤","④−③","①−④","①−②"],1,
     "文の中心は I use this cup（私はこのカップを使う）。『～する時』は when＋主語＋動詞で後ろに加えるので、when I drink tea（紅茶を飲む時）となる。this cup は1つの語句として数える。",
     "まず I use this cup『このカップをつかう』。そのあとに when I drink tea『こうちゃをのむとき』をつけよう。"),
    (24,"叔父は今日私を博物館に連れて行ってくれました。",["took","a museum","uncle","me","to"],[3,1,4,5,2],"My","today.",["④−②","④−⑤","①−③","①−⑤"],4,
     "主語は My uncle（私の叔父）。take＋人＋to＋場所で『人を～へ連れて行く』。過去のことなので take の過去形 took を使い、took me to a museum となる。a museum は1つの語句として数える。",
     "My uncle『おじ』のあとに took me to『わたしを～へつれていった』。さいごに a museum『はくぶつかん』だね。"),
    (25,"サリー，あなたの春休みについて話してください。",["about","me","your","spring vacation","tell"],[5,2,1,3,4],"Sally, please",".",["④−①","②−④","④−⑤","②−③"],4,
     "please＋動詞の原形で『～してください』。tell＋人＋about ～で『人に～について話す』。話を聞くのは私なので tell me about your spring vacation となる。spring vacation（春休み）は1つの語句として数える。",
     "please tell me は『わたしにはなしてください』。そのあとに about your spring vacation『あなたのはるやすみについて』をつづけよう。"),
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
