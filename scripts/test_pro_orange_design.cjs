/* Headless, separate Chrome profile: never use the user's open browser. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=(process.argv[2]||'http://127.0.0.1:8099').replace(/\/$/,'');
const out=path.resolve(__dirname,'../tmp/pro-orange-design-qa');
fs.mkdirSync(out,{recursive:true});
(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const page=await browser.newPage({viewport:{width:1280,height:950}});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    await page.goto(base+'/top.html');
    await page.locator('.grade-card').first().waitFor();
    await page.evaluate(()=>document.fonts.ready);
    assert.equal(await page.locator('.hero-slide').count(),5);
    assert.equal(await page.locator('.top-action-link').count(),4);
    assert.equal(await page.locator('.grade-card').count(),7);
    assert.equal(await page.locator('.grade-card[role="button"][tabindex="0"]').count(),7);
    assert.equal(await page.locator('.update-history').count(),1);
    assert.equal(await page.locator('.hero-title-name').evaluate(e=>getComputedStyle(e).color),'rgb(255, 158, 67)');
    assert.equal(await page.locator('.hero-slide').first().evaluate(e=>getComputedStyle(e).transitionDuration),'1s');
    const images=await page.locator('.hero-slide').evaluateAll(async images=>{
      await Promise.all(images.map(img=>img.decode()));
      return images.map(img=>({src:img.getAttribute('src'),width:img.naturalWidth,height:img.naturalHeight}));
    });
    assert.equal(new Set(images.map(i=>i.src)).size,5);
    assert.ok(images.every(i=>i.width>=1200&&i.height>=700));
    // Real browser timings: 5 different frames, 3-second cadence, wrap to first.
    await page.evaluate(()=>{
      window.heroEvents=[];
      document.getElementById('heroSlideshow').addEventListener('pro:herochange',e=>window.heroEvents.push({index:e.detail.index,at:performance.now()}));
    });
    await page.waitForFunction(()=>window.heroEvents.length>=6,{},{timeout:23000});
    const events=await page.evaluate(()=>window.heroEvents);
    assert.deepEqual(events.slice(0,5).map(e=>e.index),[1,2,3,4,0]);
    for(let i=1;i<events.length;i++)assert.ok(events[i].at-events[i-1].at>=2850&&events[i].at-events[i-1].at<=3400,JSON.stringify(events));
    await page.locator('#heroPause').click();
    const stopped=await page.locator('#heroSlideshow').getAttribute('data-current');
    await page.waitForTimeout(3200);
    assert.equal(await page.locator('#heroSlideshow').getAttribute('data-current'),stopped);
    await page.locator('#heroNext').click();await page.waitForTimeout(1100);
    assert.equal(await page.locator('#heroSlideshow').getAttribute('data-current'),String((Number(stopped)+1)%5));
    await page.locator('#heroPrev').click();await page.waitForTimeout(1100);
    assert.equal(await page.locator('#heroSlideshow').getAttribute('data-current'),stopped);
    for(let i=0;i<5;i++){
      await page.screenshot({path:path.join(out,'hero-'+i+'.png')});
      await page.locator('#heroNext').click();await page.waitForTimeout(1100);
    }
    await page.screenshot({path:path.join(out,'home-desktop.png'),fullPage:true});
    const manifest=await (await page.request.get(base+'/manifest.webmanifest')).json();
    assert.equal(manifest.name,'ReadPass Pro');assert.equal(manifest.start_url,'/top.html');
    assert.equal(manifest.icons.length,3);
    for(const icon of manifest.icons){
      const r=await page.request.get(base+icon.src);assert.equal(r.status(),200);
      const bytes=await r.body();assert.equal(bytes.subarray(1,4).toString(),'PNG');
      const size=Number(icon.sizes.split('x')[0]);assert.equal(bytes.readUInt32BE(16),size);assert.equal(bytes.readUInt32BE(20),size);
    }
    const ico=await (await page.request.get(base+'/favicon.ico')).body();
    assert.equal(ico.readUInt16LE(2),1);assert.equal(ico.readUInt16LE(4),3);
    assert.equal((await (await page.request.get(base+'/apple-touch-icon.png')).body()).readUInt32BE(16),180);
    for(const width of [390,320,768]){
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'home mobile overflow '+width);
      if(width===390)await page.screenshot({path:path.join(out,'home-mobile.png'),fullPage:true});
    }
    await page.setViewportSize({width:1280,height:950});
    await page.goto(base+'/top.html?study=cards#gradeSection');
    await page.locator('.grade-card').filter({hasText:'3級相当'}).click();
    const card=page.locator('.exam-card[href*="grade=grade3&exam=2026-2-sat"]');
    assert.match(await card.getAttribute('href'),/vocab-cards\.html/);
    await card.click();await page.locator('.btn-start').waitFor();
    await page.screenshot({path:path.join(out,'vocab-cards.png')});
    await page.goto(base+'/top.html?study=review#gradeSection');
    await page.locator('.grade-card').filter({hasText:'3級相当'}).focus();
    await page.keyboard.press('Enter');
    await page.locator('.exam-card[href*="grade=grade3&exam=2026-2-sat"]').click();
    await page.waitForSelector('#q30',{state:'attached'});
    await page.waitForFunction(()=>document.querySelector('#tab-lesson').classList.contains('active'));
    assert.equal(await page.locator('.fp-card').count(),4);
    await page.locator('[data-tab="part1"]').click();
    const d=await (await page.request.get(base+'/data/grade3/2026-2-sat/data.json')).json();
    for(const q of d.sections[0].questions)await page.locator('.exam-choice-btn[data-q="'+q.number+'"][data-val="'+q.answer+'"]').click();
    await page.locator('#part1Submit').click();
    assert.equal(await page.locator('#part1Results .big-score').innerText(),'15 / 15');
    await page.screenshot({path:path.join(out,'study-dark.png')});
    await page.locator('#btnTheme').click();
    assert.equal(await page.locator('.app-header').evaluate(e=>getComputedStyle(e).backgroundImage),'none');
    assert.equal(await page.locator('body').evaluate(e=>getComputedStyle(e).backgroundImage),'none');
    assert.equal(await page.locator('.app-title').evaluate(e=>getComputedStyle(e).color),'rgb(39, 43, 44)');
    await page.screenshot({path:path.join(out,'study-light.png')});
    await page.goto(base+'/print.html');
    await page.locator('.grade-chip').filter({hasText:'3級相当'}).click();
    await page.locator('#examCheckboxes input[value="2026-2-sat"]').check();
    await page.waitForSelector('.teacher-material-actions .pdf-view-link');
    for(const group of await page.locator('.teacher-material-actions').all()){
      for(const save of await group.locator('a[download]').all()){
        const href=await save.getAttribute('href');
        const view=group.locator('a:not([download])').filter({hasText:/閲覧/});
        assert.ok(await view.count()>=1);
        assert.equal(await view.first().getAttribute('href'),href);
        assert.equal(await view.first().getAttribute('target'),'_blank');
      }
    }
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const fixed=page.locator('.fixed-exam-actions .pdf-view-link');
    assert.equal(await fixed.innerText(),'PDFを閲覧');
    const href=await fixed.getAttribute('href');
    const pdf=await page.request.get(new URL(href,base).href);
    assert.equal(pdf.status(),200);assert.equal((await pdf.body()).subarray(0,5).toString(),'%PDF-');
    await page.screenshot({path:path.join(out,'print-desktop.png'),fullPage:true});
    // Future/pre-built homework and answer PDF links, including a Blob URL.
    await page.evaluate(()=>{
      const row=document.createElement('div');row.id='qaHomework';row.className='teacher-material-actions';
      const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['%PDF-1.4\n%%EOF'],{type:'application/pdf'}));
      a.download='answers.pdf';a.textContent='解答・解説を保存';row.append(a);
      document.getElementById('teacherMaterialList').append(row);
    });
    const answerView=page.locator('#qaHomework .pdf-view-link');
    await answerView.waitFor();assert.equal(await answerView.innerText(),'解答・解説を閲覧');
    assert.equal(await answerView.getAttribute('download'),null);
    await page.evaluate(()=>document.getElementById('qaHomework').remove());
    for(const width of [390,320]){
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'print mobile overflow '+width);
    }
    await page.setViewportSize({width:1280,height:950});
    await page.emulateMedia({media:'print'});
    const styles=()=>page.evaluate(()=>({bodyColor:getComputedStyle(document.body).color,bg:getComputedStyle(document.body).backgroundColor,panel:getComputedStyle(document.getElementById('settingsPanel')).display}));
    const withTheme=await styles();
    await page.locator('link[href*="pro-theme.css"]').evaluate(e=>e.disabled=true);
    assert.deepEqual(await styles(),withTheme,'printed styles must be unchanged');
    await page.emulateMedia({media:'screen'});
    await page.goto(base+'/guide.html');await page.screenshot({path:path.join(out,'guide.png')});
    const reduced=await browser.newPage({viewport:{width:1280,height:950},reducedMotion:'reduce'});
    await reduced.goto(base+'/top.html');await reduced.waitForSelector('.grade-card');
    await reduced.waitForTimeout(3400);
    assert.equal(await reduced.locator('#heroSlideshow').getAttribute('data-current'),'0');
    assert.ok(await reduced.locator('#heroPause').isDisabled());
    await reduced.locator('#heroNext').click();
    await reduced.waitForFunction(()=>document.getElementById('heroSlideshow').dataset.current==='1');
    assert.equal(await reduced.locator('.hero-slide').first().evaluate(e=>getComputedStyle(e).transitionDuration),'0s');
    await reduced.close();
    assert.deepEqual(errors,[]);
    console.log('UI OK: 5-photo 3-second cycle, pause/manual/reduced-motion, 4 menus, 7 keyboard-accessible grades, review/word links, scoring, mobile, PDF view/save, future Blob links, icons, unchanged print styles');
    console.log('Screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
