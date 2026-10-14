"""Original word banks/frames/pairs; explanatory positions are derived, not guessed."""
import re

CIRCLES="①②③④⑤"
ROWS=[
    (21,"私たちにあなたの北海道旅行について話してください。",["about","tell","us","to","your trip"],[2,3,1,5,4],"Please","Hokkaido.",["①−⑤","③−①","③−⑤","②−①"],3,
     "固定の Please の後ろに動詞の原形 tell を置いて『～してください』の文にする。tell＋人＋about＋話題で『人に～について話す』なので tell us about。your trip to Hokkaido で『あなたの北海道への旅行』。to は文末の Hokkaido の直前に置く。",
     "Please tell us は『わたしたちにはなしてください』。about your trip『あなたのりょこうについて』のあとに、to Hokkaido『ほっかいどうへの』をつなげよう。"),
    (22,"愛はよく彼女の家の隣のレストランで夕食を食べます。",["at","next","to","dinner","the restaurant"],[4,1,5,2,3],"Ai often eats","her house.",["①−②","④−③","⑤−①","①−④"],1,
     "固定の Ai often eats の直後に、食べる物 dinner を置く。場所は at the restaurant（レストランで）。next to ～で『～の隣の』となり、next to her house が the restaurant を後ろから説明して『彼女の家の隣のレストラン』になる。",
     "eats dinner は『ばんごはんをたべる』。at the restaurant『レストランで』のあとに、next to her house『いえのとなりの』をつなげよう。"),
    (23,"私の父は今週末，車を洗うつもりです。",["going","father","to","wash","is"],[2,5,1,3,4],"My","his car this weekend.",["①−②","⑤−②","⑤−③","④−①"],3,
     "固定の My の後ろに father を置いて主語 My father を作る。be going to＋動詞の原形で『～するつもりだ』。主語が三人称単数なので be 動詞は is。to の後ろは動詞の原形 wash で、固定の his car this weekend が続く。",
     "My father is going to wash は『ちちは～をあらうつもりだ』。is going to のあとは、うごきのことばのもとの形 wash だよ。"),
    (24,"私は今日の午後，郵便局へ行かなくてはなりません。",["the post office","to","this","have","go to"],[4,2,5,1,3],"I","afternoon.",["④−⑤","③−④","①−⑤","②−①"],4,
     "have to＋動詞の原形で『～しなければならない』。have to の後ろに go to the post office（郵便局へ行く）を置く。『今日の午後』は this afternoon なので、this は文末の afternoon の直前に置く。go to と the post office はそれぞれ1つの語句として数える。",
     "have to go は『いかなくてはならない』。go to the post office『ゆうびんきょくへいく』のあと、this afternoon『きょうのごご』でおわるよ。"),
    (25,"佐藤先生の日本語の授業では，英語を話さないでください。",["English","in","speak","Ms. Sato's","don't"],[5,3,1,2,4],"Please","Japanese class.",["⑤−②","⑤−④","③−①","③−②"],4,
     "Please don't＋動詞の原形で『～しないでください』。don't の後ろに speak English（英語を話す）を置く。in Ms. Sato's Japanese class で『佐藤先生の日本語の授業で』。Ms. Sato's（佐藤先生の）は文末の Japanese class の直前に置く。",
     "Please don't speak English は『えいごをはなさないでください』。そのあとに in Ms. Sato's Japanese class『さとうせんせいのにほんごのじゅぎょうで』をつけよう。"),
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
