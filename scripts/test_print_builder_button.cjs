/* Study page プリント作成 button: opens print.html in a new tab with the grade and exam selected,
   and stays hidden for students who came from a QR code (no nav=1).
   Headless, separate Chrome profile: never use the user's open browser.
   Usage: node scripts/test_print_builder_button.cjs http://127.0.0.1:8085 */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=(process.argv[2]||'http://127.0.0.1:8085').replace(/\/$/,'');
const out=path.resolve(__dirname,'../tmp/print-builder-qa');
fs.mkdirSync(out,{recursive:true});

// One main exam and one Saturday exam, so both venue checkboxes are covered.
const CASES=[['grade3','2025-3'],['grade-pre2','2024-2-sat']];

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const context=await browser.newContext({viewport:{width:1280,height:900}});
    const errors=[];
    context.on('page',p=>p.on('pageerror',e=>errors.push(`${p.url()}: ${e.message}`)));
    const page=await context.newPage();
    page.on('pageerror',e=>errors.push(`${page.url()}: ${e.message}`));
    page.setDefaultTimeout(15000);

    for(const [grade,exam] of CASES){
      // Teacher view (links from the top page add nav=1): the button sits next to 印刷.
      await page.goto(`${base}/index.html?grade=${grade}&exam=${exam}&nav=1`);
      const btn=page.locator('#btnPrintBuilder');
      await btn.waitFor({state:'visible'});
      assert.equal((await btn.innerText()).replace(/\s+/g,' ').trim(),'edit_document プリント作成');
      assert.equal(await page.locator('.instructor-toolbar .tool-btn:visible').last().getAttribute('id'),'btnPrintBuilder');
      if(grade==='grade3')await page.locator('.instructor-toolbar').screenshot({path:path.join(out,'toolbar-teacher.png')});

      const [popup]=await Promise.all([context.waitForEvent('page'),btn.click()]);
      await popup.waitForLoadState('load');
      const url=new URL(popup.url());
      assert.equal(url.pathname.replace(/^.*\//,''),'print.html');
      assert.equal(url.searchParams.get('grade'),grade);
      assert.equal(url.searchParams.get('exam'),exam);
      // The study page stays where it was.
      assert.match(page.url(),new RegExp(`grade=${grade}&exam=${exam}`));
      // The new tab has no handle back to the study page.
      assert.equal(await popup.evaluate(()=>window.opener),null);

      const checked=popup.locator('#examCheckboxes input[type="checkbox"]:checked');
      await checked.first().waitFor({state:'attached'});
      assert.deepEqual(await checked.evaluateAll(b=>b.map(x=>x.value)),[exam]);
      const chips=popup.locator('.grade-chip.active');
      assert.equal(await chips.count(),1);
      // The checked box is on screen without scrolling.
      assert.ok(await checked.first().evaluate(b=>{const r=b.getBoundingClientRect();return r.top>=0&&r.bottom<=innerHeight;}));
      // Same state as a teacher's clicks: the generate button and the materials for this exam are ready.
      assert.equal(await popup.locator('#generateBtn').isDisabled(),false);
      await popup.locator(`.teacher-material-row[data-exam="${exam}"]`).waitFor();
      if(grade==='grade3')await popup.screenshot({path:path.join(out,'print-preselected.png')});
      await popup.close();

      // Student view from a QR code (no nav): no button, and the home link is hidden as before.
      await page.goto(`${base}/index.html?grade=${grade}&exam=${exam}`);
      await page.locator('#examLabel').filter({hasText:'年度'}).waitFor();
      await page.locator('.exam-question, .passage-block').first().waitFor({state:'attached'});
      assert.equal(await page.locator('#btnPrintBuilder').isVisible(),false);
      assert.equal(await page.locator('.home-link').isVisible(),false);
      assert.equal(await page.locator('#btnPrint').isVisible(),true);
      if(grade==='grade3')await page.locator('.instructor-toolbar').screenshot({path:path.join(out,'toolbar-qr.png')});
    }

    // Phone width: the toolbar still scrolls sideways instead of widening the page.
    await page.setViewportSize({width:390,height:844});
    await page.goto(`${base}/index.html?grade=grade3&exam=2025-3&nav=1`);
    await page.locator('#btnPrintBuilder').waitFor({state:'visible'});
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));

    // Plain print.html and homework deep links are unchanged: nothing preselected without grade/exam.
    const plain=await context.newPage();
    await plain.goto(`${base}/print.html`);
    await plain.locator('.grade-chip').first().waitFor();
    assert.equal(await plain.locator('.grade-chip.active').count(),0);
    await plain.close();

    assert.deepEqual(errors,[]);
    console.log(`PRINT BUILDER OK: ${CASES.length} exams open print.html in a new tab with grade and exam selected; hidden for QR access; phone width`);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
