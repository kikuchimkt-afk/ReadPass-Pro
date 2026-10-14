/* Headless QA only: isolated Chrome, no access to the user's browser. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=(process.argv[2]||'http://127.0.0.1:8099').replace(/\/$/,'');
const out=path.resolve(__dirname,'../tmp/pro-card-tools-qa');
fs.mkdirSync(out,{recursive:true});
(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const context=await browser.newContext({viewport:{width:1280,height:950}});
    const errors=[];context.on('page',p=>p.on('pageerror',e=>errors.push(e.message)));
    const page=await context.newPage();page.setDefaultTimeout(20000);
    const expected=(grade,exam)=>base+'/vocab-cards.html?grade='+grade+'&exam='+exam;
    async function qrReady(p,grade,exam){
      await p.waitForFunction(()=>!document.getElementById('cardQrSave').hidden);
      assert.equal(await p.locator('#cardQrGrade').inputValue(),grade);
      assert.equal(await p.locator('#cardQrExam').inputValue(),exam);
      assert.equal(await p.locator('#cardQrOpen').getAttribute('href'),expected(grade,exam));
      assert.match(await p.locator('#cardQrSave').getAttribute('href'),/^data:image\/png;base64,/);
    }
    async function decodeQR(p){
      // Independent decoder verifies the actual PNG, not just its link label.
      if(!await p.evaluate(()=>!!window.jsQR))
        await p.addScriptTag({url:'https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js'});
      return p.evaluate(async()=>{
        const img=new Image();img.src=document.getElementById('cardQrSave').href;await img.decode();
        const c=document.createElement('canvas');c.width=img.width;c.height=img.height;
        const ctx=c.getContext('2d');ctx.drawImage(img,0,0);
        const pixels=ctx.getImageData(0,0,c.width,c.height);
        const decoded=window.jsQR(pixels.data,c.width,c.height);
        return {text:decoded?.data,width:c.width,height:c.height,corner:[...ctx.getImageData(0,0,1,1).data]};
      });
    }
    await page.goto(base+'/top.html?study=cards');
    await page.locator('.grade-card').filter({hasText:'3級相当'}).click();
    await page.waitForSelector('.card-qr-button');
    assert.match(page.url(),/grade=grade3#examSection$/);
    assert.equal(await page.locator('.card-qr-button').count(),await page.locator('.exam-card').count());
    const row=page.locator('.card-exam-option').filter({has:page.locator('.exam-card[href*="grade=grade3&exam=2026-2-sat"]')});
    await row.locator('.card-qr-button').click();
    await qrReady(page,'grade3','2026-2-sat');
    assert.deepEqual(await decodeQR(page),{text:expected('grade3','2026-2-sat'),width:280,height:280,corner:[255,255,255,255]});
    const catalog=await page.evaluate(()=>window.READPASS_EXAM_CATALOG);
    assert.equal(catalog.length,7);
    // Every grade exposes exactly its existing catalog, not a invented session.
    for(const grade of catalog){
      await page.locator('#cardQrGrade').selectOption(grade.id);
      const choices=await page.locator('#cardQrExam option').evaluateAll(nodes=>nodes.map(n=>n.value).sort());
      assert.deepEqual(choices,grade.exams.map(e=>e.id).sort());
    }
    await page.locator('#cardQrGrade').selectOption('grade-pre2plus');
    await page.locator('#cardQrExam').selectOption('2026-2');
    await qrReady(page,'grade-pre2plus','2026-2');
    assert.equal((await decodeQR(page)).text,expected('grade-pre2plus','2026-2'));
    await page.screenshot({path:path.join(out,'qr-desktop.png')});
    for(const width of [320,390]){
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'modal overflow '+width);
      assert.ok(await page.locator('#cardQrDialog').evaluate(e=>e.scrollWidth<=e.clientWidth+1),'dialog internal overflow '+width);
    }
    await page.screenshot({path:path.join(out,'qr-mobile.png')});
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#cardQrDialog').evaluate(e=>e.open),false);
    await page.setViewportSize({width:1280,height:950});
    await row.locator('.exam-card').click();
    await page.waitForFunction(()=>+document.getElementById('statTotal').textContent>0);
    await page.locator('#cardReturn').click();
    await page.waitForURL(/top\.html.*grade=grade3/);
    await page.waitForSelector('#examSection:not(.hidden)');
    assert.match(await page.locator('#examSectionTitle').innerText(),/3級相当/);
    // Cold reload also restores the grade's exam selection.
    await page.reload();
    await page.waitForSelector('#examSection:not(.hidden) .card-qr-button');
    await page.locator('#backToGrades').click();
    assert.equal(new URL(page.url()).searchParams.has('grade'),false);

    // A scanned/direct link has no opener/referrer: return to the same exam.
    const direct=await context.newPage();
    await direct.goto(expected('grade3','2026-2-sat'));
    await direct.waitForFunction(()=>+document.getElementById('statTotal').textContent>0);
    assert.equal(await direct.locator('#cardReturn').getAttribute('href'),base+'/index.html?grade=grade3&exam=2026-2-sat&nav=1');
    await direct.locator('#cardShowQr').click();await qrReady(direct,'grade3','2026-2-sat');
    await direct.locator('.card-qr-close').click();
    // Audio URL resolves identically for grade/exam and legacy data parameters.
    const d=await (await direct.request.get(base+'/data/grade3/2026-2-sat/data.json')).json();
    assert.ok(d.vocabulary[0].wordAudio);
    await direct.evaluate(()=>{
      window.qaAudioSrc=null;
      window.Audio=class {constructor(src){window.qaAudioSrc=src;this.paused=false;}play(){return Promise.resolve();}pause(){this.paused=true;}};
    });
    await direct.locator('.btn-start').click();
    await direct.waitForFunction(()=>window.qaAudioSrc!==null);
    assert.equal(await direct.evaluate(()=>window.qaAudioSrc),'data/grade3/2026-2-sat/'+d.vocabulary[0].wordAudio);
    assert.ok(await direct.locator('#cardReturn').isVisible());
    await direct.locator('.btn-reveal').click();
    assert.equal(await direct.locator('#flipCard').getAttribute('class'),'flip-card flipped');
    await direct.locator('.btn-known').click();
    assert.match(await direct.locator('#cardProgress').innerText(),/^2 \/ /);
    await direct.locator('.btn-end').click();
    assert.equal(await direct.locator('#statDone').innerText(),'1');
    await direct.screenshot({path:path.join(out,'cards-navigation.png')});
    for(const width of [320,390]){
      await direct.setViewportSize({width,height:844});
      assert.ok(await direct.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'cards overflow '+width);
    }
    await direct.locator('#cardReturn').click();
    await direct.waitForSelector('#q1',{state:'attached'});
    assert.equal(new URL(direct.url()).searchParams.get('grade'),'grade3');
    assert.equal(new URL(direct.url()).searchParams.get('exam'),'2026-2-sat');

    // Ignore off-origin return targets. Legacy data URLs infer current grade.
    const unsafe=await context.newPage();
    await unsafe.goto(base+'/vocab-cards.html?data='+encodeURIComponent('data/grade3/2026-2-sat/data.json')+'&return='+encodeURIComponent('https://example.com/'));
    await unsafe.waitForSelector('#cardShowQr');
    assert.equal(await unsafe.locator('#cardReturn').getAttribute('href'),base+'/index.html?grade=grade3&exam=2026-2-sat&nav=1');
    await unsafe.locator('#cardShowQr').click();await qrReady(unsafe,'grade3','2026-2-sat');
    await unsafe.close();

    // Real toolbar popup returns to its existing opener with answer state intact.
    await page.goto(base+'/index.html?grade=grade3&exam=2026-2-sat&nav=1');
    await page.waitForSelector('#q1 .exam-choice-btn',{state:'attached'});
    await page.locator('[data-tab="part1"]').click();
    await page.locator('#q1 .exam-choice-btn[data-val="1"]').click();
    const selected=await page.locator('#q1 .exam-choice-btn[data-val="1"]').getAttribute('class');
    const [popup]=await Promise.all([page.waitForEvent('popup'),page.locator('#btnVocabCards').click()]);
    await popup.waitForSelector('#cardShowQr');
    await popup.locator('#cardShowQr').click();await qrReady(popup,'grade3','2026-2-sat');
    await popup.locator('.card-qr-close').click();
    await Promise.all([popup.waitForEvent('close'),popup.locator('#cardReturn').click()]);
    assert.equal(await page.locator('#q1 .exam-choice-btn[data-val="1"]').getAttribute('class'),selected);
    assert.deepEqual(errors,[]);
    console.log('CARD TOOLS OK: actual QR decode, all 7 catalogs, grade/exam changes, PNG quiet zone, Escape, mobile, source selection restore, safe direct return, legacy data URLs, popup answer preservation, audio, flip/progress/end.');
    console.log('Screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
