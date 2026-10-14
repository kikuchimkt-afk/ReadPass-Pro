/* Homework print (A4 portrait, four fixed pages: questions 2 + explanations 2) in an isolated headless browser. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=process.argv[2]||'http://127.0.0.1:8085';
const out=path.resolve(__dirname,'../tmp/qa-homework');
fs.mkdirSync(out,{recursive:true});
const TARGET={chip:'準1級',grade:'pre-grade1',exam:'2026-2',title:'英検準1級 2026年度 第2回'};

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const page=await browser.newPage({viewport:{width:1365,height:1000}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    const index=await (await page.request.get(`${base}/data/homework/index.json`)).json();
    const hw=await (await page.request.get(`${base}/${index[`${TARGET.grade}/${TARGET.exam}`].path}`)).json();

    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:TARGET.chip}).first().click();
    await page.locator(`#examCheckboxes input[value="${TARGET.exam}"]`).check();
    const row=page.locator(`.teacher-material-row[data-homework="${TARGET.exam}"]`);
    assert.match(await row.innerText(),/宿題プリント（文法事項の確認）/);
    assert.match(await row.innerText(),new RegExp(`A4縦4ページ（問題${hw.questions.length}問・うち全訳${hw.questions.filter(q=>q.translate).length}問：問題2ページ・解答解説2ページ）`));
    // The grammar-guide row keeps its own selector for the existing tests.
    assert.equal(await page.locator(`.teacher-material-row[data-exam="${TARGET.exam}"]`).count(),1);

    // Dialog defaults: next week, same grade, the next older session.
    await row.locator('.homework-open').click();
    const dialog=page.locator('#homeworkDialog');
    assert.ok(await dialog.evaluate(d=>d.open));
    assert.equal(await page.locator('#hwTarget').innerText(),TARGET.title);
    const expectedDate=await page.evaluate(()=>{const d=new Date();d.setDate(d.getDate()+7);return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;});
    assert.equal(await page.locator('#hwNextDate').inputValue(),expectedDate);
    assert.equal(await page.locator('input[name="hwGrade"]:checked').inputValue(),TARGET.grade);
    const examIds=await page.locator('input[name="hwExam"]').evaluateAll(xs=>xs.map(x=>x.value));
    const keys=examIds.map(id=>{const m=id.match(/^(\d{4})-(\d+)(-.+)?$/);return Number(m[1])*100+Number(m[2])*10+(m[3]?0:1);});
    assert.deepEqual(keys,[...keys].sort((a,b)=>b-a),'sessions newest first');
    assert.equal(await page.locator('input[name="hwExam"]:checked').inputValue(),examIds[examIds.indexOf(TARGET.exam)+1]);
    assert.equal(await page.locator('input[name="hwGrade"]').count(),7);
    // Switching the grade lists that grade's sessions; switch back and choose 2026-1.
    await page.locator('input[name="hwGrade"][value="grade3"]').check();
    assert.ok(await page.locator('input[name="hwExam"][value="2026-2-sat"]').count()===1);
    await page.locator('input[name="hwGrade"][value="pre-grade1"]').check();
    await page.locator('#hwNextDate').fill('2026-10-21');
    await page.locator('input[name="hwExam"][value="2026-1"]').check();
    await dialog.screenshot({path:path.join(out,'dialog.png')});
    await page.locator('#hwCreate').click();

    const pages=page.locator('.hw-page');
    await page.waitForFunction(()=>document.querySelectorAll('.hw-ex').length>0&&document.querySelector('.hw-qr img, .hw-qr canvas'));
    assert.equal(await pages.count(),4);
    assert.equal(await page.locator('#previewLabel').innerText(),'宿題プリント（A4縦4ページ：問題2・解答解説2）');
    assert.equal(await page.locator('.hw-pages.hw-overflow').count(),0,'all items flowed within four pages');
    for(let i=0;i<4;i++){
      const fit=await pages.nth(i).evaluate(p=>{
        const footer=p.querySelector('.hw-page-no').getBoundingClientRect().top;
        const last=[...p.children].filter(c=>!c.classList.contains('hw-page-no')).pop().getBoundingClientRect().bottom;
        const right=p.getBoundingClientRect().right;
        const wide=[...p.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().right>right+1).map(e=>e.className||e.tagName);
        return {scroll:p.scrollHeight,client:p.clientHeight,gap:footer-last,wide};
      });
      assert.ok(fit.scroll<=fit.client+1,`page ${i+1} overflow ${JSON.stringify(fit)}`);
      assert.deepEqual(fit.wide,[],`page ${i+1} horizontal overflow`);
      assert.ok(fit.gap>=0,`page ${i+1} content runs into the footer ${JSON.stringify(fit)}`);
      console.log(`PAGE ${i+1} spare space above footer: ${Math.round(fit.gap)}px`);
    }
    const p1=pages.nth(0),p2=pages.nth(1),p3=pages.nth(2),p4=pages.nth(3);
    // Questions flow over pages 1-2 in order; explanations over pages 3-4.
    const qNums=hw.questions.map(q=>`(${q.number})`);
    assert.deepEqual(await page.locator('.hw-page-questions .hw-q .hw-q-num').allTextContents(),qNums);
    assert.deepEqual(await page.locator('.hw-page-answers .hw-ex .hw-q-num').allTextContents(),qNums);
    for(const pg of [p1,p2])assert.ok(await pg.locator('.hw-q').count()>0,'both question pages are used');
    for(const pg of [p3,p4])assert.ok(await pg.locator('.hw-ex').count()>0,'both explanation pages are used');
    assert.equal(await page.locator('.hw-page-questions .hw-write').count(),hw.questions.filter(q=>q.translate).length);
    assert.equal(await page.locator('.hw-page-questions .hw-q .hw-star').count(),hw.questions.filter(q=>q.translate).length);
    assert.equal(await p2.locator('.hw-answer-row').count(),1,'answer boxes after the last question');
    assert.equal(await page.locator('.hw-answer-row b').count(),hw.questions.length);
    assert.match(await p1.innerText(),/提出日\s*10月21日（水）/);
    assert.deepEqual(await p3.locator('.hw-key b').allTextContents(),hw.questions.map(q=>String(q.answer)));
    for(const [i,q] of hw.questions.entries()){
      const ex=page.locator('.hw-page-answers .hw-ex').nth(i);
      const text=await ex.innerText();
      assert.ok(text.includes(`正解 ${q.answer}`)&&text.includes(q.choices[q.answer-1]),`Q${q.number} answer`);
      for(const part of [q.translation,q.explanation,q.tip])assert.ok(text.includes(part),`Q${q.number} explanation parts`);
    }
    const next=p4.locator('.hw-next');
    assert.match(await next.innerText(),/次回の授業：10月21日（水）/);
    assert.match(await next.innerText(),/英検準1級 2026年度 第1回/);
    const qrUrl=await p4.locator('.hw-qr').getAttribute('data-url');
    assert.equal(qrUrl,'https://read-pass-pro.vercel.app/vocab-cards.html?data='+encodeURIComponent('data/pre-grade1/2026-1/data.json'));
    assert.ok(await p4.locator('.hw-qr img, .hw-qr canvas').count()>0,'QR image rendered');
    const flash=await page.request.get(`${base}/data/pre-grade1/2026-1/data.json`);
    assert.equal(flash.status(),200);
    for(let i=0;i<4;i++)await pages.nth(i).screenshot({path:path.join(out,`page${i+1}.png`)});

    // Printing yields exactly two A4 pages.
    await page.emulateMedia({media:'print'});
    const pdf=await page.pdf({path:path.join(out,'homework.pdf'),preferCSSPageSize:true,printBackground:true});
    const pageCount=(pdf.toString('latin1').match(/\/Type\s*\/Page[^s]/g)||[]).length;
    assert.equal(pageCount,4,'printed page count');
    await page.emulateMedia({media:'screen'});

    // Without the next-lesson block: no QR and an empty submission date.
    await row.locator('.homework-open').click();
    await page.locator('#hwNoNext').check();
    assert.ok(await page.locator('#hwNextDate').isDisabled());
    await page.locator('#hwCreate').click();
    await page.waitForFunction(()=>document.querySelectorAll('.hw-page').length===4&&document.querySelectorAll('.hw-ex').length>0&&!document.querySelector('.hw-next'));
    assert.match(await page.locator('.hw-page').first().innerText(),/提出日\s*月\s*日/);

    // Cancel keeps the current preview; switching exams clears it.
    await row.locator('.homework-open').click();
    await page.locator('#hwCancel').click();
    assert.equal(await dialog.evaluate(d=>d.open),false);
    assert.equal(await page.locator('.hw-page').count(),4);

    await page.setViewportSize({width:390,height:844});
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'mobile horizontal scroll');
    assert.deepEqual(errors,[]);
    console.log(`HOMEWORK UI OK: ${hw.questions.length} questions (${hw.questions.filter(q=>q.translate).length} translations), 4 fitted A4 pages (questions 2 + explanations 2), answers, tips, next lesson QR, no-QR mode, PDF ${pageCount} pages`);
    console.log('QA output:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
