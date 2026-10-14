/* Top page homework menu and update-history accordion.
   Headless, separate Chrome profile: never use the user's open browser.
   Usage: node scripts/test_top_homework.cjs http://127.0.0.1:8085 */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=(process.argv[2]||'http://127.0.0.1:8085').replace(/\/$/,'');
const out=path.resolve(__dirname,'../tmp/top-homework-qa');
fs.mkdirSync(out,{recursive:true});

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const page=await browser.newPage({viewport:{width:1280,height:950}});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    const index=await (await page.request.get(`${base}/data/homework/index.json`)).json();

    // Card 02 is the homework print menu.
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').first().waitFor();
    assert.equal(await page.locator('.top-action-link').count(),4);
    const card=page.locator('.top-action-link').nth(1);
    assert.equal(await card.locator('strong').innerText(),'宿題プリント');
    assert.equal(await card.locator('.action-index').innerText(),'02 / HOMEWORK');
    assert.equal(await card.getAttribute('href'),'top.html?study=homework#gradeSection');
    assert.notEqual(await card.evaluate(e=>getComputedStyle(e).backgroundImage),'none');
    assert.equal(await page.getByText('授業の復習',{exact:true}).count(),0);

    // Update history: an accordion, newest open, the rest closed; summaries work with the keyboard.
    const entries=page.locator('.update-history-entry details');
    const total=await entries.count();
    assert.ok(total>=10,`history entries ${total}`);
    assert.deepEqual(await entries.evaluateAll(ds=>ds.map(d=>d.open)),[true,...Array(total-1).fill(false)]);
    const dates=await page.locator('.update-history-entry time').evaluateAll(ts=>ts.map(t=>t.getAttribute('datetime')));
    assert.deepEqual(dates,[...dates].sort().reverse(),'newest first');
    const second=entries.nth(1);
    assert.equal(await second.locator('.update-history-body').isVisible(),false);
    await second.locator('summary').click();
    assert.ok(await second.evaluate(d=>d.open));
    assert.ok(await second.locator('.update-history-body p').isVisible());
    await second.locator('summary').focus();
    await page.keyboard.press('Enter');
    assert.equal(await second.evaluate(d=>d.open),false);
    const first=entries.first();
    assert.match(await first.locator('h3').innerText(),/宿題プリント/);
    assert.deepEqual(await first.locator('.update-history-meta dt').allTextContents(),['担当モデル（指定）','推論レベル（指定）']);
    assert.deepEqual(await first.locator('.update-history-meta dd').allTextContents(),['Claude Opus 5.5','xhigh']);
    await page.locator('.update-history').screenshot({path:path.join(out,'history-desktop.png')});
    await page.locator('.top-actions').screenshot({path:path.join(out,'menu-desktop.png')});

    // Homework mode lists only exams that have a homework print, and links to print.html.
    await card.click();
    await page.waitForURL(/study=homework/);
    assert.equal(await page.locator('#gradeSectionTitle').innerText(),'宿題プリントのレベルを選ぶ');
    await page.locator('.grade-card').filter({hasText:'3級相当'}).click();
    const expected=Object.keys(index).filter(k=>k.startsWith('grade3/')).map(k=>k.split('/')[1]);
    await page.waitForFunction(n=>document.querySelectorAll('#examList .exam-card').length===n,expected.length);
    const hrefs=await page.locator('#examList .exam-card').evaluateAll(as=>as.map(a=>a.getAttribute('href')));
    const exams=hrefs.map(h=>{
      const url=new URL(h,`${base}/top.html`);
      assert.match(url.pathname,/\/print\.html$/);
      assert.equal(url.searchParams.get('grade'),'grade3');
      assert.equal(url.searchParams.get('homework'),'1');
      return url.searchParams.get('exam');
    });
    assert.deepEqual([...exams].sort(),[...expected].sort());

    // The link opens the dialog for that grade and exam; creating it yields the four pages.
    await page.locator('#examList .exam-card').first().click();
    await page.waitForURL(/print\.html/);
    const dialog=page.locator('#homeworkDialog');
    await page.waitForFunction(()=>document.getElementById('homeworkDialog').open);
    assert.equal(await page.locator('.grade-chip.active').count(),1);
    assert.match(await page.locator('.grade-chip.active').innerText(),/3級/);
    assert.deepEqual(await page.locator('#examCheckboxes input:checked').evaluateAll(cs=>cs.map(c=>c.value)),[exams[0]]);
    assert.equal(await page.locator(`.teacher-material-row[data-homework="${exams[0]}"]`).count(),1);
    assert.match(await page.locator('#hwTarget').innerText(),/3級/);
    await page.locator('#hwCreate').click();
    await page.waitForFunction(()=>document.querySelectorAll('.hw-page').length===4&&document.querySelector('.hw-qr img, .hw-qr canvas'));
    assert.equal(await dialog.evaluate(d=>d.open),false);
    assert.equal(await page.locator('.hw-pages.hw-overflow').count(),0);

    // A plain print.html visit does not open the dialog.
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').first().waitFor();
    await page.waitForTimeout(800);
    assert.equal(await dialog.evaluate(d=>d.open),false);

    // Phone width: no horizontal scroll; history rows stay readable.
    await page.setViewportSize({width:390,height:844});
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').first().waitFor();
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'mobile horizontal scroll');
    await page.locator('.update-history').screenshot({path:path.join(out,'history-mobile.png')});
    assert.deepEqual(errors,[]);
    console.log(`TOP HOMEWORK OK: menu card, ${total} history entries (accordion, keyboard), ${expected.length} Grade 3 homework exams linked, dialog deep link, mobile`);
    console.log('QA output:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
