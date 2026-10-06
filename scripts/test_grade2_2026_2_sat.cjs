/* Headless, isolated regression checks; never touches a user's browser profile. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://127.0.0.1:8094';
const out = path.resolve(__dirname, '../tmp/qa-grade2-2026-2-sat');
fs.mkdirSync(out, {recursive:true});

(async () => {
  const browser = await chromium.launch({channel:'chrome', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').filter({hasText:'B1（2級相当）'}).click();
    const card = page.locator('.exam-card[href*="grade=grade2&exam=2026-2-sat&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2026年度 第2回（土曜準会場）/);
    await card.click();
    await page.waitForSelector('#q31',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/第2回（土曜準会場）/);
    assert.equal(await page.locator('.exam-question').count(),31);
    assert.equal(await page.locator('.exam-choice-btn').count(),124);
    assert.equal(await page.locator('.choice-analysis-item').count(),124);
    assert.equal(await page.locator('.fp-card').count(),5);
    assert.equal(await page.locator('.fp-audio-btn').count(),5);
    assert.equal(await page.locator('.sentence-span').count(),76);
    assert.match(await page.locator('#vocabProgressText').innerText(),/55/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);

    for (const [part,count] of [['part1',17],['part2',6],['part3',8]]) {
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),count);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),31);
    await page.locator('#btnTranslation').click();
    await page.locator('[data-tab="part2"]').click();
    await page.locator('#tab-part2 .sentence-span').first().click();
    assert.equal(await page.locator('.slash-reading-display').count(),1);
    assert.match(await page.locator('.slash-reading-display').innerText(),/専門家/);
    assert.match(await page.locator('.slash-reading-display .main-verb').first().innerText(),/have developed/);
    await page.locator('#tab-part2 .sentence-span').first().click();
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),5);
    assert.ok(await page.locator('#tab-part2 .grammar-hl').count()>0);
    await page.locator('.hl-legend-item[data-fpid="fp2"]').click();
    await page.locator('.hl-legend-item[data-fpid="fp2"]').click();
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#q25 .correct-item').click();
    assert.ok(await page.locator('.evidence-hl').count()>0);
    await page.locator('#tab-part3').screenshot({path:path.join(out,'reading.png')});
    await page.screenshot({path:path.join(out,'reading-view.png')});
    const emailHeaders = await page.locator('.email-meta').first().innerText();
    assert.match(emailHeaders,/<marco@speedwaymotors.com>/);
    assert.match(emailHeaders,/<srodriguez@fastlink.com>/);

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),15);
    assert.equal(await page.locator('.fp-q').count(),20);
    for (let i=1;i<=5;i++) await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),5);
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    await page.locator('#fp-fp1').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'lesson-view.png')});
    await page.locator('#fp-fp1 .fp-audio-btn').click();
    await page.waitForFunction(()=>document.querySelector('#fp-fp1 .fp-audio-duration').textContent!=='0:00');
    await page.locator('#fp-fp1 .fp-audio-btn').click();
    const audio = await page.evaluate(async () => {
      const d=await (await fetch('data/grade2/2026-2-sat/data.json')).json();
      const refs=[...d.vocabulary.map(v=>v.wordAudio),...d.lessonPlan.focusPoints.map(f=>f.practicePassage.audioFile)];
      const ctx=new AudioContext();
      try {
        return await Promise.all(refs.map(async ref=>{
          const r=await fetch(`data/grade2/2026-2-sat/${ref}`);
          if (!r.ok) throw new Error(ref+': '+r.status);
          const buffer=await ctx.decodeAudioData(await r.arrayBuffer());
          return {ref,duration:buffer.duration};
        }));
      } finally {await ctx.close();}
    });
    assert.equal(audio.length,60);
    assert.ok(audio.every(a=>a.duration>0.2));
    console.log('AUDIO_DECODE_OK',audio.length,Math.min(...audio.map(a=>a.duration)),Math.max(...audio.map(a=>a.duration)));
    const sections=await page.evaluate(async()=> (await (await fetch('data/grade2/2026-2-sat/data.json')).json()).sections);
    for (let i=0;i<sections.length;i++) {
      const part=`part${i+1}`, section=sections[i];
      const qs=section.questions || section.passages.flatMap(p=>p.questions);
      await page.locator(`[data-tab="${part}"]`).click();
      for (const q of qs) await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${qs.length} / ${qs.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),31);
    await page.locator('#btnTheme').click();
    await page.setViewportSize({width:390,height:844});
    await page.locator('[data-tab="part2"]').click();
    await page.screenshot({path:path.join(out,'mobile.png'),fullPage:true});
    await page.evaluate(()=>window.scrollTo(0,0));
    await page.screenshot({path:path.join(out,'mobile-view.png')});
    const mobile = await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,overflow:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).slice(0,15).map(e=>({tag:e.tagName,cls:e.className,right:e.getBoundingClientRect().right,text:e.textContent.slice(0,50)}))}));
    console.log('MOBILE_LAYOUT',JSON.stringify(mobile));
    assert.ok(mobile.scroll<=mobile.width+1);

    await page.setViewportSize({width:1365,height:1000});
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:'B1（2級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2026-2-sat"]').check();
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const pdfHref=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(pdfHref,/Grade2_2026-2-sat/);
    const response=await page.request.get(`${base}/${pdfHref}`);
    assert.equal(response.status(),200);
    assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    // Shared email escaping must retain the existing exam's text and label.
    await page.goto(`${base}/index.html?grade=grade2&exam=2026-1-sat&nav=1`);
    await page.waitForSelector('#q31',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/第1回（準会場）/);
    await page.locator('[data-tab="part3"]').click();
    assert.match(await page.locator('.email-meta').first().innerText(),/<jjenkins@riverstonehigh.edu>/);
    assert.deepEqual(errors,[]);
    console.log('UI OK: catalog, 31 questions, translations, slash reading, verb, evidence, markers, 5 focus points, 60 decoded audio, mobile, fixed PDF');
    console.log('QA screenshots:',out);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
