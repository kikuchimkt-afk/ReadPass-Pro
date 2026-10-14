/* Navigation and QR links only. Reuse the canonical landing catalog. */
(() => {
  'use strict';
  const catalog=window.READPASS_EXAM_CATALOG||[];
  if(!catalog.length)return;
  const params=new URLSearchParams(location.search);
  // The study toolbar uses ?data=...; QR/home links use ?grade=...&exam=....
  const dataMatch=(params.get('data')||'').match(/(?:^|\/)data\/([^/]+)\/([^/]+)\/data\.json$/);
  const dataGrade=dataMatch&&catalog.find(g=>g.dataPath===dataMatch[1]);
  const currentGrade=params.get('grade')||dataGrade?.id;
  const currentExam=params.get('exam')||dataMatch?.[2];
  const isCards=document.body.dataset.surface==='cards';
  let qrLoading=null,renderToken=0;
  const dialog=document.createElement('dialog');
  dialog.className='card-qr-dialog';dialog.id='cardQrDialog';
  dialog.setAttribute('aria-labelledby','cardQrTitle');
  dialog.innerHTML='<div class="card-qr-heading"><h2 id="cardQrTitle">単語カードのQRコード</h2><button type="button" class="card-qr-close" aria-label="QRモーダルを閉じる">×</button></div>'+
    '<p class="card-qr-help">級と回を選んでください。スマートフォンで読み取ると、選んだ回の単語カードを開けます。</p>'+
    '<div class="card-qr-fields"><label>級<select id="cardQrGrade"></select></label><label>回<select id="cardQrExam"></select></label></div>'+
    '<div class="card-qr-frame" id="cardQrImage"></div><span class="card-qr-url" id="cardQrUrl"></span>'+
    '<div class="card-qr-actions"><a class="card-qr-open" id="cardQrOpen">単語カードを開く</a><a id="cardQrSave" hidden>QR画像を保存</a></div>'+
    '<p class="card-qr-status" id="cardQrStatus" role="status"></p>';
  document.body.append(dialog);
  const gradeSelect=dialog.querySelector('#cardQrGrade'),examSelect=dialog.querySelector('#cardQrExam');
  const image=dialog.querySelector('#cardQrImage'),urlText=dialog.querySelector('#cardQrUrl');
  const open=dialog.querySelector('#cardQrOpen'),save=dialog.querySelector('#cardQrSave');
  const status=dialog.querySelector('#cardQrStatus');
  catalog.forEach(g=>gradeSelect.add(new Option(g.name,g.id)));
  function newest(exams){
    const key=e=>{const m=e.id.match(/^(\d{4})-(\d+)(-.+)?$/);return m?[+m[1],+m[2],m[3]?1:0]:[0,0,0];};
    return [...exams].sort((a,b)=>{const x=key(a),y=key(b);return y[0]-x[0]||y[1]-x[1]||x[2]-y[2];});
  }
  function fillExams(examId){
    const grade=catalog.find(g=>g.id===gradeSelect.value);
    examSelect.replaceChildren();
    newest(grade.exams).forEach(e=>examSelect.add(new Option(e.label,e.id)));
    if(grade.exams.some(e=>e.id===examId))examSelect.value=examId;
  }
  function qrLibrary(){
    if(window.QRCode)return Promise.resolve();
    if(qrLoading)return qrLoading;
    qrLoading=new Promise((resolve,reject)=>{
      const script=document.createElement('script');
      script.src='https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js';
      script.onload=resolve;script.onerror=()=>{qrLoading=null;script.remove();reject(Error('QR library unavailable'));};
      document.head.append(script);
    });
    return qrLoading;
  }
  async function renderQR(){
    const token=++renderToken;
    const grade=catalog.find(g=>g.id===gradeSelect.value);
    const exam=grade.exams.find(e=>e.id===examSelect.value);
    if(!exam)return;
    const url=new URL('vocab-cards.html',location.href);
    url.searchParams.set('grade',grade.id);url.searchParams.set('exam',exam.id);
    image.replaceChildren();save.hidden=true;status.textContent='QRコードを準備しています…';
    open.href=url.href;urlText.textContent=url.href;
    try{
      await qrLibrary();
      if(token!==renderToken)return;
      new window.QRCode(image,{text:url.href,width:224,height:224,colorDark:'#111111',colorLight:'#ffffff',correctLevel:window.QRCode.CorrectLevel.M});
      const source=image.querySelector('canvas');
      if(source){
        // Include a real white quiet zone in the downloaded image, too.
        const canvas=document.createElement('canvas');canvas.width=canvas.height=280;
        const ctx=canvas.getContext('2d');ctx.fillStyle='#fff';ctx.fillRect(0,0,280,280);ctx.drawImage(source,28,28);
        save.href=canvas.toDataURL('image/png');save.download='ReadPass_words_'+grade.id+'_'+exam.id+'.png';save.hidden=false;
      }
      status.textContent=grade.name+' / '+exam.label;
    }catch{
      if(token===renderToken)status.textContent='QRコードを読み込めませんでした。下のボタンから単語カードを開けます。';
    }
  }
  function showQR(gradeId,examId){
    gradeSelect.value=catalog.some(g=>g.id===gradeId)?gradeId:catalog[0].id;
    fillExams(examId);dialog.showModal();renderQR();
  }
  gradeSelect.addEventListener('change',()=>{fillExams();renderQR();});
  examSelect.addEventListener('change',renderQR);
  dialog.querySelector('.card-qr-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
  function safeReturn(candidate){
    try{
      const url=new URL(candidate,location.href);
      return url.origin===location.origin&&/\/(?:index|top|print|guide)\.html$/.test(url.pathname)?url:null;
    }catch{return null;}
  }
  if(isCards){
    const referrer=safeReturn(document.referrer);
    const explicit=params.has('return')?safeReturn(params.get('return')):null;
    let target=explicit||referrer;
    if(!target){
      target=new URL('index.html',location.href);
      const grade=currentGrade,exam=currentExam;
      if(grade&&exam){target.searchParams.set('grade',grade);target.searchParams.set('exam',exam);target.searchParams.set('nav','1');}
      else target=new URL('top.html',location.href);
    }
    const nav=document.createElement('nav');nav.className='card-top-nav';nav.setAttribute('aria-label','単語カードの案内');
    const back=document.createElement('a');back.id='cardReturn';back.href=target.href;back.textContent='← 元のページへ';
    back.addEventListener('click',event=>{
      try{
        if(window.opener&&!window.opener.closed&&window.opener.location.origin===location.origin){
          event.preventDefault();window.opener.focus();window.close();
          setTimeout(()=>{if(!window.closed)location.assign(target.href);},150);return;
        }
      }catch{/* Same-origin checks failed: use the safe link instead. */}
      if(referrer&&history.length>1){event.preventDefault();history.back();}
    });
    const home=document.createElement('a');home.href='top.html';home.textContent='ホーム';
    const qr=document.createElement('button');qr.type='button';qr.id='cardShowQr';qr.textContent='QRコード';
    qr.addEventListener('click',()=>showQR(currentGrade,currentExam));
    nav.append(back,home,qr);document.querySelector('.container').prepend(nav);
  }
  if(params.get('study')==='cards'&&document.getElementById('examList')){
    const list=document.getElementById('examList'),buttons=[...document.querySelectorAll('.grade-card')];
    buttons.forEach((button,i)=>button.addEventListener('click',()=>{
      const url=new URL(location.href);url.searchParams.set('grade',catalog[i].id);url.hash='examSection';history.replaceState(null,'',url);
    }));
    document.getElementById('backToGrades').addEventListener('click',()=>{
      const url=new URL(location.href);url.searchParams.delete('grade');url.hash='gradeSection';history.replaceState(null,'',url);
    });
    function enhanceRows(){
      for(const link of list.querySelectorAll('.exam-card')){
        const url=new URL(link.href,location.href);
        const grade=url.searchParams.get('grade'),exam=url.searchParams.get('exam');
        const origin=new URL('top.html',location.href);origin.searchParams.set('study','cards');origin.searchParams.set('grade',grade);origin.hash='examSection';
        url.searchParams.set('return',origin.pathname.split('/').pop()+origin.search+origin.hash);
        if(link.href!==url.href)link.href=url.href;
        if(link.parentElement.classList.contains('card-exam-option'))continue;
        const row=document.createElement('div');row.className='card-exam-option';
        link.before(row);row.append(link);
        const qr=document.createElement('button');qr.type='button';qr.className='card-qr-button';qr.textContent='QRコード';
        qr.setAttribute('aria-label',link.querySelector('.exam-label').textContent+'の単語カードQRコード');
        qr.addEventListener('click',()=>showQR(grade,exam));row.append(qr);
      }
    }
    new MutationObserver(enhanceRows).observe(list,{childList:true,subtree:true});
    enhanceRows();
    const index=catalog.findIndex(g=>g.id===params.get('grade'));
    if(index>=0)buttons[index]?.click();
  }
})();
