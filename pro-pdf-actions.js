/* Independent controls: don't change the PDF or homework builders. */
(() => {
  'use strict';
  function enhance(){
    for(const group of document.querySelectorAll('.teacher-material-actions,.fixed-exam-actions')){
      for(const save of group.querySelectorAll('a[download]')){
        let url;
        try{url=new URL(save.href,location.href);}catch{continue;}
        if(!['https:','http:','blob:'].includes(url.protocol))continue;
        let view=[...group.querySelectorAll('a:not([download])')].find(a=>a.href===save.href);
        if(!view){view=document.createElement('a');view.href=save.href;group.insertBefore(view,save);}
        view.classList.add('pdf-view-link');
        view.target='_blank';view.rel='noopener noreferrer';
        const text=/解答|解説/.test(save.textContent)?'解答・解説を閲覧':'PDFを閲覧';
        if(view.textContent!==text)view.textContent=text;
        if(!view.hasAttribute('aria-label'))view.setAttribute('aria-label',text+'（別タブで開く）');
        if(save.textContent.trim()==='DL')save.textContent='PDFを保存';
      }
    }
    // Dynamic homework sheets are HTML print previews, not saved PDFs.
    for(const button of document.querySelectorAll('.homework-open')){
      if(button.textContent.trim()==='作成'){
        button.textContent='作成して閲覧';
        button.title='次回の授業日を指定して、印刷用プレビューを開きます';
      }
    }
  }
  new MutationObserver(enhance).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['href','download']});
  enhance();
})();
