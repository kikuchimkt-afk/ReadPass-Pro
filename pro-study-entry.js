/* Deep link from the review menu; leave the assessment engine untouched. */
(() => {
  if(new URLSearchParams(location.search).get('study')!=='review')return;
  function openReview(){
    if(!document.querySelector('.fp-card'))return false;
    document.querySelector('.tab-btn[data-tab="lesson"]')?.click();return true;
  }
  if(openReview())return;
  const observer=new MutationObserver(()=>{if(openReview())observer.disconnect();});
  observer.observe(document.getElementById('app'),{childList:true,subtree:true});
})();
