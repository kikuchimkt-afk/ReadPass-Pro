"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"ぼくの部屋でこのCDを聞こう。",["listen","in","this CD","to"],[1,4,3,2],"Let's","my room.",["①−②","④−②","③−④","①−③"],4,
     "Let's＋動詞の原形で『～しよう』。listen to＋聞くもの、in＋場所をセットにし、listen→to→this CD→in の順に並べる。Let's と my room. は固定部分で、4つの空所の位置には数えない。",
     "Let's は『～しよう』。listen to は『～をきく』、in my room は『ぼくのへやで』。this CD はひとつのかたまり。Let's はばんごうにかぞえないよ。"),
    (22,"アダムズさんは，昼食前に走りに行きます。",["lunch","running","goes","before"],[3,2,4,1],"Mr. Adams",".",["④−②","②−③","③−④","①−②"],3,
     "go running は『走りに行く』。主語が Mr. Adams なので goes running とする。before lunch は『昼食前に』。goes→running→before→lunch の順で、固定の Mr. Adams は空所の位置には数えない。",
     "『はしりにいく』は goes running のセット。『おひるごはんのまえ』は before lunch。Mr. Adams は、さいしょからかいてあるのでかぞえないよ。"),
    (23,"私の兄はマンガをたくさん持っています。",["has","of","my brother","a lot"],[3,1,4,2],"","comic books.",["④−①","④−③","③−②","③−④"],4,
     "主語 My brother の後ろに has（持っている）。my brother は三人称単数なので have ではなく has。a lot of＋名詞で『たくさんの～』。my brother→has→a lot→of と並べ、固定の comic books. につなぐ。",
     "まず『わたしのあに』の my brother、そのあとに『もっている』の has。a lot of は『たくさんの』。my brother と a lot は、それぞれひとつのかたまりだよ。"),
    (24,"おじいさん，お茶の時間ですよ。",["time","it's","tea","for"],[2,1,4,3],"Grandpa,",".",["①−③","②−④","④−①","③−②"],2,
     "It's time for＋名詞で『～の時間です』。it's→time→for→tea と並べる。Grandpa, はおじいさんへの呼びかけで、4つの空所には含めない。it's は it is を短くした形。",
     "『おちゃのじかん』は it's time for tea のセット。Grandpa は『おじいさん』へのよびかけで、あきのばんごうにはかぞえないよ。it's はひとつのかたまりだね。"),
    (25,"あなたのお兄さんはデジタルカメラを持っていますか。",["a","have","does","your brother"],[3,4,2,1],"","digital camera?",["②−③","①−②","④−③","③−②"],4,
     "一般動詞の疑問文は Does＋三人称単数の主語＋動詞の原形。主語 your brother の前に Does、後ろに原形 have を置く。a digital camera が『1台のデジタルカメラ』。does→your brother→have→a の順に並べる。",
     "『もっていますか』ときくので、Does からはじめよう。your brother のあとに、もとの形の have。your brother はひとつのかたまり。さいごの a はカメラにつながるよ。"),
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
