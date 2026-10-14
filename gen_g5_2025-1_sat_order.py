"""Original four chunks/fixed frames; derive the first/third answer positions."""
import re

CIRCLES="①②③④"
SLOTS=[1,3]
ROWS=[
    (21,"私達のネコは10歳です。",["is","our cat","years old","ten"],[2,1,4,3],"",".",["②−④","④−③","②−③","④−②"],1,
     "年齢は『主語＋be動詞＋数＋years old』で表す。主語 our cat（私達のネコ）は1匹なので be動詞は is。our cat→is→ten→years old の順に並べる。our cat と years old はそれぞれ1つのかたまり。( ) の中では文頭の語も小文字なので、our は完成文では Our と大文字で書き始める。",
     "『～さいです』は is ten years old のじゅんだよ。our cat（わたしたちのネコ）と years old は、それぞれひとつのかたまりだね。"),
    (22,"鈴木先生と歩いているのはだれですか。",["walking","is","with","who"],[4,2,1,3],"","Mr. Suzuki?",["③−②","①−③","②−③","④−①"],4,
     "『だれが～していますか』は、Who を主語にした疑問文 Who is＋～ing ...?（現在進行形）で表す。Who が主語なので、is のすぐ後ろに walking を続ける。who→is→walking→with の順に並べ、with を固定の Mr. Suzuki? の前に置いて『鈴木先生と一緒に』とする。",
     "『だれ？』は Who。Who is walking ～?（だれがあるいているの？）のじゅんだよ。with は『～といっしょに』で、Mr. Suzuki のまえにおくよ。"),
    (23,"私の祖母は東京に住んでいます。",["grandmother","Tokyo","lives","in"],[1,3,4,2],"My",".",["④−②","③−②","①−④","②−①"],3,
     "固定の My の後ろに grandmother を続けて、主語 My grandmother（私の祖母）を作る。live in＋場所で『～に住んでいる』。主語が he・she と同じ3人称単数なので lives と s が付く。grandmother→lives→in→Tokyo の順に並べる。My は最初から書かれているので、4つの空所の位置には数えない。",
     "My grandmother（わたしのそぼ）が『だれが』のぶぶん。lives in Tokyo で『とうきょうにすんでいる』だよ。My はさいしょからかいてあるので、かぞえないよ。"),
    (24,"クリスはオーストラリア出身です。",["Australia","Chris","from","is"],[2,4,3,1],"",".",["③−④","①−④","①−②","②−③"],4,
     "be from＋場所で『～の出身である』。主語 Chris に合わせて be動詞は is を使い、Chris→is→from→Australia の順に並べる。from は Australia の前に置く。Chris や Australia のような人名・国名は、文の途中でも大文字で始める。",
     "『～しゅっしん』は is from ～ だよ。Chris is from Australia. のじゅんにならべよう。"),
    (25,"リードさんは，毎日朝食前に泳ぎます。",["swims","breakfast","before","Mr. Reed"],[4,1,3,2],"","every day.",["④−③","③−①","①−③","②−④"],1,
     "主語 Mr. Reed（リードさん）の後ろに動詞 swims（泳ぐ）を置く。主語が3人称単数で、毎日していることを表すので swims と s が付く。before breakfast は『朝食の前に』で、before を breakfast の前に置く。Mr. Reed→swims→before→breakfast の順に並べ、固定の every day.（毎日）につなぐ。Mr. Reed は1つのかたまり。",
     "Mr. Reed（リードさん）が『だれが』のぶぶん。swims（およぐ）のあとに before breakfast（あさごはんのまえに）をつけるよ。every day. はさいしょからかいてあるね。"),
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
