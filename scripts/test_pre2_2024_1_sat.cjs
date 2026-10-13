/* Headless, isolated regression checks; never touches a user's browser profile. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://127.0.0.1:8085';
const out = path.resolve(__dirname, '../tmp/qa-grade-pre2-2024-1-sat');
const dataUrl = 'data/grade-pre2/2024-1-sat/data.json';
fs.mkdirSync(out, {recursive:true});

(async () => {
  const browser = await chromium.launch({channel:'chrome', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').filter({hasText:'A2（準2級相当）'}).click();
    const card = page.locator('.exam-card[href*="grade=grade-pre2&exam=2024-1-sat&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2024年度 第1回（土曜準会場）/);
    // Saturday sits between the main 2024-1 and 2024-2 sessions.
    const order = await page.locator('.exam-card[href*="grade=grade-pre2&"]').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
    assert.deepEqual(order.slice(order.indexOf('2024-1'),order.indexOf('2024-1')+3),['2024-1','2024-1-sat','2024-2']);
    await card.click();
    await page.waitForSelector('#q29',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2024年度 第1回/);
    assert.equal(await page.locator('.exam-question').count(),29);
    assert.equal(await page.locator('.exam-choice-btn').count(),116);
    assert.equal(await page.locator('.choice-analysis-item').count(),116);
    assert.equal(await page.locator('.fp-card').count(),5);
    assert.equal(await page.locator('.fp-audio-btn').count(),5);
    assert.equal(await page.locator('.sentence-span').count(),53);
    assert.match(await page.locator('#vocabProgressText').innerText(),/40/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);

    // Word audio is the 2024 format; there is no example audio button.
    await page.locator('[data-tab="vocab"]').click();
    const word = await page.locator('.vocab-word').evaluate(e=>e.firstChild.textContent.trim());
    const meaning = await page.evaluate(async ([url,word])=>{
      const d=await (await fetch(url)).json();
      return d.vocabulary.find(v=>v.word===word).meaning;
    },[dataUrl,word]);
    const wordButton=page.locator('.vocab-word .vocab-audio-btn');
    await wordButton.click();
    assert.ok(await wordButton.evaluate(e=>e.classList.contains('playing')));
    await wordButton.click();
    await page.locator(`#vocabChoices .choice-btn[data-value="${meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);
    assert.equal(await page.locator('.result-example .vocab-audio-btn').count(),0);

    for (const [part,count] of [['part1',15],['part2',5],['part3',2],['part4',7]]) {
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),count);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),29);
    await page.locator('#btnTranslation').click();
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#tab-part3 .sentence-span').first().click();
    assert.match(await page.locator('.sentence-tooltip').innerText(),/マリア/);
    await page.locator('#tab-part3 .sentence-span').first().click();

    // Every focus point must light up at least one phrase in Parts 3-4.
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),5);
    const unmatched = await page.evaluate(async url=>{
      const d=await (await fetch(url)).json();
      const marks=[...document.querySelectorAll('mark.grammar-hl')].map(m=>m.textContent.replace(/\s+/g,' ').toLowerCase());
      return d.lessonPlan.focusPoints.flatMap(fp=>fp.highlightPatterns
        .filter(p=>!marks.some(m=>m.includes(p.toLowerCase())))
        .map(p=>`${fp.id}: ${p}`));
    },dataUrl);
    console.log('HIGHLIGHT_UNMATCHED',JSON.stringify(unmatched));
    for (let i=1;i<=5;i++) {
      for (let j=1;j<=5;j++) if (j!==i) await page.locator(`.hl-legend-item[data-fpid="fp${j}"]`).click();
      assert.ok(await page.locator('mark.grammar-hl').count()>0,`fp${i} has no visible highlight`);
      for (let j=1;j<=5;j++) if (j!==i) await page.locator(`.hl-legend-item[data-fpid="fp${j}"]`).click();
    }
    await page.locator('[data-tab="part4"]').click();
    await page.locator('#tab-part4').screenshot({path:path.join(out,'reading.png')});
    const emailHeaders = await page.locator('.email-meta').first().innerText();
    assert.match(emailHeaders,/<steve.musiclover@mailme.com>/);
    assert.match(emailHeaders,/<jennyk1234@zmail.com>/);
    assert.match(await page.locator('#tab-part4').innerText(),/Park Güell/);

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),15);
    assert.equal(await page.locator('.fp-q').count(),20);
    for (let i=1;i<=5;i++) await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),5);
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    await page.locator('#fp-fp1 .fp-audio-btn').click();
    await page.waitForFunction(()=>document.querySelector('#fp-fp1 .fp-audio-duration').textContent!=='0:00');
    await page.locator('#fp-fp1 .fp-audio-btn').click();
    const audio = await page.evaluate(async url => {
      const d=await (await fetch(url)).json();
      const dir=url.replace(/data\.json$/,'');
      const refs=[...d.vocabulary.map(v=>v.wordAudio),...d.lessonPlan.focusPoints.map(f=>f.practicePassage.audioFile)];
      const ctx=new AudioContext();
      try {
        return await Promise.all(refs.map(async ref=>{
          const r=await fetch(dir+ref);
          if (!r.ok) throw new Error(ref+': '+r.status);
          const buffer=await ctx.decodeAudioData(await r.arrayBuffer());
          return {ref,duration:buffer.duration};
        }));
      } finally {await ctx.close();}
    },dataUrl);
    assert.equal(audio.length,45);
    assert.ok(audio.every(a=>a.duration>0.2));
    console.log('AUDIO_DECODE_OK',audio.length,Math.min(...audio.map(a=>a.duration)),Math.max(...audio.map(a=>a.duration)));
    const sections=await page.evaluate(async url=> (await (await fetch(url)).json()).sections,dataUrl);
    for (let i=0;i<sections.length;i++) {
      const part=`part${i+1}`, section=sections[i];
      const qs=section.questions || section.passages.flatMap(p=>p.questions);
      await page.locator(`[data-tab="${part}"]`).click();
      for (const q of qs) await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${qs.length} / ${qs.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),29);
    await page.locator('#btnTheme').click();
    await page.setViewportSize({width:390,height:844});
    await page.locator('[data-tab="part2"]').click();
    await page.evaluate(()=>window.scrollTo(0,0));
    await page.screenshot({path:path.join(out,'mobile-view.png')});
    for (const width of [320,390,600]) {
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`horizontal scroll at ${width}px`);
    }

    await page.setViewportSize({width:1365,height:1000});
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:'A2（準2級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2024-1-sat"]').check();
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const pdfHref=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(pdfHref,/GradePre2_2024-1-sat/);
    const response=await page.request.get(`${base}/${pdfHref}`);
    assert.equal(response.status(),200);
    assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    assert.deepEqual(errors,[]);
    console.log('UI OK: catalog order, 29 questions, translations, tooltip, 5 focus-point highlights, 45 decoded audio, mobile, fixed PDF');
    console.log('QA screenshots:',out);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
