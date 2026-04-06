# -*- coding: utf-8 -*-
import json, os

data = {
    'grade': '準2級', 'year': '2023', 'session': '3',
    'title': '2023年度 第3回 英検準2級 リーディング',
    'vocabulary': [], 'sections': [], 'lessonPlan': {}
}

# Helper
def vq(n,t,tr,c,ct,a,ca,g):
    return {'number':n,'text':t,'translation':tr,'choices':c,'choiceTranslations':ct,'answer':a,'choiceAnalysis':ca,'grammar':g}

# === SECTION 1: 大問1 (20問 vocabulary) ===
s1 = {'name':'大問1','nameEn':'Part 1','type':'vocabulary',
      'instruction':'次の(1)から(20)までの(　)に入れるのに最も適切なものを1，2，3，4の中から一つ選びなさい。',
      'questions':[]}
Q = s1['questions']

Q.append(vq(1,'Silvia tried to buy some concert tickets online. However, she could not ( ) the website because many other people were trying to use it at the same time.','シルビアはコンサートのチケットをオンラインで買おうとした。しかし、同時に多くの人がサイトを使おうとしていたため、サイトに( )できなかった。',['deliver','access','increase','embarrass'],['配達する','アクセスする','増加させる','恥ずかしくさせる'],2,['❌ deliver＝配達する。サイトに不適','✅ access＝アクセスする→正解','❌ increase＝増加させる。不適','❌ embarrass＝恥ずかしくさせる。無関係'],'💡 access＝～にアクセスする（他動詞）。名詞でも使える。'))

Q.append(vq(2,'A : Oh no! A page of my math textbook has fallen out!\\nB : Don\\'t worry. We can fix it with some of this ( ).','A：大変！教科書のページが外れた！\\nB：心配しないで。この( )で直せるよ。',['bacon','tape','soil','mass'],['ベーコン','テープ','土','かたまり'],2,['❌ bacon＝ベーコン。無関係','✅ tape＝テープ→正解','❌ soil＝土。不適','❌ mass＝かたまり。不適'],'💡 fall out＝外れる。fix＝修理する。'))

Q.append(vq(3,'A : Are you happy that you moved to a different part of the city?\\nB : Yes, I am. I like my new ( ). It\\'s quiet, the people who live there are friendly, and it\\'s convenient for shopping, too.','A：市内の別の場所に引っ越して嬉しい？\\nB：うん。新しい( )が気に入ってる。静かで人もフレンドリーで買い物にも便利。',['climate','entrance','neighborhood','monument'],['気候','入口','近所・地域','記念碑'],3,['❌ climate＝気候。不適','❌ entrance＝入口。不適','✅ neighborhood＝近所→正解','❌ monument＝記念碑。無関係'],'💡 neighborhood＝近所、地域。convenient for ～＝～に便利な。'))

Q.append(vq(4,'A : Excuse me. How do I get to Parkville Station?\\nB : First, take this train to Anderson Station. Then, you need to ( ) to one of the trains that go to Colby Station. They all stop at Parkville Station.','A：すみません。パークビル駅にはどう行けばいいですか？\\nB：まずアンダーソン駅まで行き、コルビー駅行きの電車に( )してください。',['boil','transfer','cause','achieve'],['沸騰させる','乗り換える','引き起こす','達成する'],2,['❌ boil＝沸騰。無関係','✅ transfer＝乗り換える→正解','❌ cause＝引き起こす。不適','❌ achieve＝達成する。不適'],'💡 transfer to ～＝～に乗り換える。'))

Q.append(vq(5,'Harvey is so tall that he can touch the ( ) of his bedroom even when he is standing on the floor.','ハーヴィーはとても背が高く、床に立っているだけでも寝室の( )に手が届く。',['ceiling','crossing','medium','stadium'],['天井','交差点','中間','スタジアム'],1,['✅ ceiling＝天井→正解','❌ crossing＝交差点。不適','❌ medium＝中間。不適','❌ stadium＝スタジアム。無関係'],'💡 so...that～構文。ceiling＝天井（⇔floor＝床）。'))

Q.append(vq(6,'The company\\'s profits have grown ( ) because sales of its products have gone up by about 5 percent each year for the last 10 years.','その会社の利益は( )成長してきた。過去10年間、毎年約5%ずつ売上が伸びている。',['steadily','willingly','falsely','angrily'],['着実に','進んで','偽って','怒って'],1,['✅ steadily＝着実に→正解','❌ willingly＝進んで。不適','❌ falsely＝偽って。不適','❌ angrily＝怒って。不適'],'💡 steadily＝着実に。go up by ～＝～だけ上がる。'))

Q.append(vq(7,'A : Was your soccer game ( ) by the heavy rain?\\nB : No. Luckily, the game had already finished by the time it started raining.','A：サッカーの試合は大雨の( )を受けた？\\nB：幸い、雨が降り始めた頃にはもう試合は終わっていた。',['hoped','supposed','affected','warned'],['望んだ','想定した','影響を受けた','警告した'],3,['❌ hoped＝望んだ。不適','❌ supposed＝想定した。不適','✅ affected＝影響を受けた→正解','❌ warned＝警告した。不適'],'💡 be affected by ～＝～に影響を受ける。'))

Q.append(vq(8,'Brenda loves fantasy stories about witches. Yesterday, she read a story about a girl who had ( ) powers and used them to help her friends.','ブレンダは魔女のファンタジー物語が好きだ。昨日、( )な力を持ち友達を助ける少女の物語を読んだ。',['magic','general','wealthy','bitter'],['魔法の','一般的な','裕福な','苦い'],1,['✅ magic＝魔法の→正解','❌ general＝一般的な。不適','❌ wealthy＝裕福な。不適','❌ bitter＝苦い。不適'],'💡 magic powers＝魔法の力。'))

Q.append(vq(9,'Although Mike and his older brother often fought when they were young, their ( ) has gotten better since they grew up. These days, they get along very well.','マイクと兄は幼い頃よくケンカしたが、大人になり( )は良くなった。最近はとても仲良くしている。',['population','material','relationship','chapter'],['人口','素材','関係','章'],3,['❌ population＝人口。無関係','❌ material＝素材。不適','✅ relationship＝関係→正解','❌ chapter＝章。不適'],'💡 get along (well)＝仲良くやる。'))

Q.append(vq(10,'A : Honey, what do you think of this blue dress?\\nB : It\\'s perfect for you! It ( ) the color of your eyes.','A：ねえ、この青いドレスどう思う？\\nB：ぴったりよ！目の色に( )しているわ。',['matches','joins','lifts','serves'],['合う','参加する','持ち上げる','提供する'],1,['✅ matches＝合う→正解','❌ joins＝参加する。不適','❌ lifts＝持ち上げる。不適','❌ serves＝提供する。不適'],'💡 match＝～に合う、調和する。'))

Q.append(vq(11,'Paul\\'s family is ( ) five people. They are Paul, his mother, his father, and his two sisters.','ポールの家族は5人( )。ポール、母、父、そして2人の姉妹だ。',['in the habit of','given in to','made up of','with regard to'],['～する習慣がある','～に屈した','～で構成されている','～に関して'],3,['❌ in the habit of＝習慣がある。不適','❌ given in to＝屈した。不適','✅ made up of＝構成されている→正解','❌ with regard to＝～に関して。不適'],'💡 be made up of ～＝～で構成されている（= consist of）。'))

Q.append(vq(12,'Frank was walking happily home after school. ( ), he remembered that he had left his smartphone in his desk, so he ran back to get it.','フランクは放課後楽しく歩いて帰っていた。( )、机にスマホを忘れたことを思い出し取りに戻った。',['Up to date','In the old days','All of a sudden','For the moment'],['最新の','昔は','突然','当分の間'],3,['❌ Up to date＝最新の。不適','❌ In the old days＝昔は。不適','✅ All of a sudden＝突然→正解','❌ For the moment＝当分の間。不適'],'💡 All of a sudden＝突然（= suddenly）。'))

Q.append(vq(13,'Grant was ( ) of going to the airport to meet Alice when he got a phone call from her. She told him that her flight had been canceled.','グラントはアリスを迎えに空港に行こう( )とき、彼女から電話があった。フライトがキャンセルされたと言われた。',['at the sight','in the way','by the end','on the point'],['～を見て','邪魔で','～の終わりに','まさに～しようとして'],4,['❌ at the sight＝見て。不適','❌ in the way＝邪魔で。不適','❌ by the end＝終わりに。不適','✅ on the point＝まさに～しようとして→正解'],'💡 be on the point of doing＝まさに～しようとしている（= be about to do）。'))

Q.append(vq(14,'Heather wanted to go camping with her friends last weekend. However, it was ( ) because she had an important test on Monday, and she needed to study.','ヘザーは先週末友達とキャンプに行きたかった。しかし月曜に大事なテストがあり勉強が必要だったため( )だった。',['by any chance','out of the question','at any cost','for the most part'],['もしかして','問題外で','何としても','大部分は'],2,['❌ by any chance＝もしかして。不適','✅ out of the question＝問題外→正解','❌ at any cost＝何としても。不適','❌ for the most part＝大部分は。不適'],'💡 out of the question＝問題外、不可能（= impossible）。'))

Q.append(vq(15,'Barry\\'s mother told Barry that it was not healthy to spend so long indoors. She said that it would ( ) to go outside and get some fresh air.','バリーの母は長時間室内にいるのは健康に良くないと言った。外に出て新鮮な空気を吸うと( )と言った。',['take him seriously','do him good','see him off','call him up'],['彼を真剣に受け止める','彼のためになる','彼を見送る','彼に電話する'],2,['❌ take him seriously＝真剣に受け止める。不適','✅ do him good＝彼のためになる→正解','❌ see him off＝見送る。不適','❌ call him up＝電話する。不適'],'💡 do someone good＝～のためになる。fresh air＝新鮮な空気。'))

Q.append(vq(16,'Sally enjoys doing math problems in her free time. She has fun trying to ( ) what the answers are.','サリーは暇な時に数学の問題を解くのを楽しんでいる。答えを( )のが楽しいのだ。',['apply for','turn over','figure out','stand by'],['申し込む','ひっくり返す','解明する','待機する'],3,['❌ apply for＝申し込む。不適','❌ turn over＝ひっくり返す。不適','✅ figure out＝解明する→正解','❌ stand by＝待機する。不適'],'💡 figure out＝理解する、解明する。have fun doing＝～するのを楽しむ。'))

Q.append(vq(17,'Jane and Tim were planning to go on a date last Friday, but Jane was not feeling well. They decided to ( ) their date until next week.','ジェーンとティムは先週金曜にデートする予定だったがジェーンの体調が悪く、来週までデートを( )ことにした。',['carry on','give away','sit up','put off'],['続ける','ただで与える','起き上がる','延期する'],4,['❌ carry on＝続ける。不適','❌ give away＝与える。不適','❌ sit up＝起き上がる。不適','✅ put off＝延期する→正解'],'💡 put off＝延期する（= postpone）。put off A until B＝AをBまで延期する。'))

Q.append(vq(18,'A : Do you want me to finish all this work today?\\nB : No, you ( ) rush. There are still a few days before it has to be ready.','A：この仕事を全部今日終わらせましょうか？\\nB：いいえ、( )急がなくていいよ。あと数日あるから。',['won\\'t','couldn\\'t','needn\\'t','didn\\'t'],['～しないだろう','～できなかった','～する必要はない','～しなかった'],3,['❌ won\\'t＝しないだろう。不適','❌ couldn\\'t＝できなかった。不適','✅ needn\\'t＝必要はない→正解','❌ didn\\'t＝しなかった。不適'],'💡 needn\\'t＝～する必要はない（= don\\'t need to）。'))

Q.append(vq(19,'Some people hold a small umbrella in summer so as ( ) getting sunburn.','日焼けを( )ために、夏に小さな傘を持つ人もいる。',['avoid','avoiding','to avoid','be avoiding'],['避ける（原形）','避けること','避けるために','避けている'],3,['❌ avoid＝原形。so asの後にはto不定詞が必要','❌ avoiding＝動名詞。不適','✅ to avoid＝to不定詞→正解','❌ be avoiding＝進行形。不適'],'💡 so as to do＝～するために（= in order to do）。'))

Q.append(vq(20,'Only a few of Sarah\\'s friends were going to come to her party, so Sarah did not think it was worth ( ) a very big cake.','パーティーに来る友達は数人だけだったので、大きなケーキを( )価値はないと思った。',['made','making','make','makes'],['作った','作ること','作る（原形）','作る（三単現）'],2,['❌ made＝過去形。worthの後は動名詞','✅ making＝動名詞→正解','❌ make＝原形。不適','❌ makes＝三単現。不適'],'💡 be worth doing＝～する価値がある。worthの後は動名詞。'))

data['sections'].append(s1)
print(f'Section1 done: {len(Q)} questions')

# Save partial
with open('_partial.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
print('Partial saved locally')
