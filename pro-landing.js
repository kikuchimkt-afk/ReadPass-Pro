/* Presentation/navigation only; the exam catalog remains unchanged. */
(() => {
  'use strict';
  const gallery=document.getElementById('heroSlideshow');
  if(!gallery)return;
  const slides=[...gallery.querySelectorAll('.hero-slide')];
  const status=document.getElementById('heroSlideStatus');
  const pause=document.getElementById('heroPause');
  const reduce=matchMedia('(prefers-reduced-motion: reduce)');
  let current=0,paused=false,timer=null,inView=true,decoding=false;
  gallery.dataset.current='0';
  gallery.dataset.interval='3000';
  function buttonState(){
    pause.disabled=reduce.matches;
    pause.textContent=paused||reduce.matches?'▶':'Ⅱ';
    pause.setAttribute('aria-pressed',String(paused));
    pause.setAttribute('aria-label',reduce.matches?'動きを減らす設定のため自動切り替えは停止中':paused?'写真の自動切り替えを開始':'写真の自動切り替えを停止');
  }
  function schedule(){
    clearTimeout(timer);timer=null;
    if(!paused&&!document.hidden&&!reduce.matches&&inView)timer=setTimeout(()=>select(current+1),3000);
  }
  async function select(index){
    clearTimeout(timer);timer=null;
    if(decoding)return;
    const next=(index+slides.length)%slides.length;
    if(next===current){schedule();return;}
    decoding=true;
    try{await slides[next].decode();}
    catch{decoding=false;schedule();return;}
    slides[current].classList.remove('is-active');
    slides[next].classList.add('is-active');
    current=next;decoding=false;
    gallery.dataset.current=String(current);
    status.textContent=(current+1)+' / '+slides.length;
    gallery.dispatchEvent(new CustomEvent('pro:herochange',{detail:{index:current}}));
    schedule();
  }
  document.getElementById('heroPrev').addEventListener('click',()=>select(current-1));
  document.getElementById('heroNext').addEventListener('click',()=>select(current+1));
  pause.addEventListener('click',()=>{paused=!paused;buttonState();schedule();});
  reduce.addEventListener('change',()=>{buttonState();schedule();});
  document.addEventListener('visibilitychange',schedule);
  window.addEventListener('pagehide',()=>clearTimeout(timer));
  if('IntersectionObserver' in window)new IntersectionObserver(entries=>{
    inView=entries[0].isIntersecting;schedule();
  },{threshold:0}).observe(gallery);
  buttonState();schedule();
  const mode=new URLSearchParams(location.search).get('study');
  const copy={
    cards:['単語カードのレベルを選ぶ','級と回を選んで、音声付きの単語フラッシュカードを開きます。'],
    review:['復習するレベルを選ぶ','級と回を選んで、文法・構文の学習ポイントを復習します。'],
    homework:['宿題プリントのレベルを選ぶ','級と回を選ぶと、次回の授業日を入れて宿題プリントを作成できます。宿題プリントがある回だけを表示します。']
  }[mode];
  if(copy){
    document.getElementById('gradeSectionTitle').textContent=copy[0];
    document.getElementById('gradeSectionDescription').textContent=copy[1];
    const list=document.getElementById('examList');
    let homework=null; // data/homework/index.json, built by scripts/build_homework.py
    function updateLinks(){
      for(const a of list.querySelectorAll('.exam-card')){
        const url=new URL(a.href,location.href);
        if(mode==='cards')url.pathname=url.pathname.replace(/index\.html$/, 'vocab-cards.html');
        else if(mode==='homework'){
          // Homework prints are made in print.html, which opens the dialog for this grade and exam.
          const grade=url.searchParams.get('grade'),exam=url.searchParams.get('exam');
          if(homework&&!homework[grade+'/'+exam]){a.remove();continue;}
          url.pathname=url.pathname.replace(/[^/]*$/,'print.html');url.search='';
          url.searchParams.set('grade',grade);url.searchParams.set('exam',exam);url.searchParams.set('homework','1');
        }
        else url.searchParams.set('study','review');
        if(a.href!==url.href)a.href=url.href;
      }
    }
    new MutationObserver(updateLinks).observe(list,{childList:true});
    updateLinks();
    if(mode==='homework')fetch('data/homework/index.json',{cache:'no-cache'})
      .then(r=>r.ok?r.json():{}).then(index=>{homework=index||{};updateLinks();})
      .catch(()=>{});
  }
  for(const card of document.querySelectorAll('.grade-card:not(.disabled)')){
    card.setAttribute('role','button');card.tabIndex=0;
    card.addEventListener('keydown',event=>{
      if(event.key==='Enter'||event.key===' '){event.preventDefault();card.click();}
    });
  }
})();
