/* Headless, isolated regression checks; never touches a user's browser profile. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://127.0.0.1:8085';
const out = path.resolve(__dirname, '../tmp/qa-grade-pre2-2026-2');
const dataUrl = 'data/grade-pre2/2026-2/data.json';
fs.mkdirSync(out, {recursive:true});

(async () => {
  const browser = await chromium.launch({channel:'chrome', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);
    const data = await (await page.request.get(`${base}/${dataUrl}`)).json();
    const sentences = data.sections.flatMap(s=>s.passages||[]).reduce((n,p)=>n+p.sentencePairs.length,0);
    const hasAudio = data.vocabulary.every(v=>v.wordAudio && v.exampleAudio);

    await page.goto(`${base}/top.html`);
    // Every grade lists its exams newest first; the main venue precedes the sub-venue.
    const gradeNames = await page.locator('.grade-card:not(.disabled)').evaluateAll(cards=>cards.map(c=>c.innerText.split('\n')[0]));
    for (const name of gradeNames) {
      await page.locator('.grade-card').filter({hasText:name}).first().click();
      const ids = await page.locator('.exam-card').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
      const keys = ids.map(id=>{const m=id.match(/^(\d{4})-(\d+)(-.+)?$/);return Number(m[1])*100+Number(m[2])*10+(m[3]?0:1);});
      assert.deepEqual(keys,[...keys].sort((a,b)=>b-a),`${name}: ${ids.join(',')}`);
      await page.locator('#backToGrades').click();
    }
    console.log('NEWEST_FIRST_OK',gradeNames.length,'grades');
    await page.locator('.grade-card').filter({hasText:'A2（準2級相当）'}).click();
    const card = page.locator('.exam-card[href*="grade=grade-pre2&exam=2026-2&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2026年度 第2回/);
    const order = await page.locator('.exam-card[href*="grade=grade-pre2&"]').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
    assert.deepEqual(order.slice(0,4),['2026-2','2026-2-sat','2026-1','2026-1-sat']);
    await card.click();
    await page.waitForSelector('#q29',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2026年度 第2回$/);
    assert.equal(await page.locator('.exam-question').count(),29);
    assert.equal(await page.locator('.exam-choice-btn').count(),116);
    assert.equal(await page.locator('.choice-analysis-item').count(),116);
    assert.equal(await page.locator('.fp-card').count(),5);
    assert.equal(await page.locator('.fp-audio-btn').count(),hasAudio ? 5 : 0);
    assert.equal(await page.locator('.sentence-span').count(),sentences);
    assert.match(await page.locator('#vocabProgressText').innerText(),/40/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);

    await page.locator('[data-tab="vocab"]').click();
    assert.equal(await page.locator('.vocab-word .vocab-audio-btn').count(),hasAudio ? 1 : 0);
    for (const [part,count] of [['part1',15],['part2',5],['part3',2],['part4',7]]) {
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),count);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),29);
    await page.locator('#btnTranslation').click();
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#tab-part3 .sentence-span').first().click();
    assert.equal(await page.locator('.slash-reading-display').count(),1);
    assert.match(await page.locator('.slash-reading-display').innerText(),/ジョイス/);
    assert.match(await page.locator('.slash-reading-display .main-verb').first().innerText(),/^was$/);
    await page.locator('#tab-part3 .sentence-span').first().click();

    // Every highlight pattern must be visible, and each focus point on its own.
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),5);
    const unmatched = await page.evaluate(d=>{
      const marks=[...document.querySelectorAll('mark.grammar-hl')].map(m=>m.textContent.replace(/\s+/g,' ').toLowerCase());
      return d.lessonPlan.focusPoints.flatMap(fp=>fp.highlightPatterns.filter(p=>!marks.some(m=>m.includes(p.toLowerCase()))).map(p=>`${fp.id}: ${p}`));
    },data);
    console.log('HIGHLIGHT_UNMATCHED',JSON.stringify(unmatched));
    assert.deepEqual(unmatched,[]);
    for (let i=1;i<=5;i++) {
      for (let j=1;j<=5;j++) if (j!==i) await page.locator(`.hl-legend-item[data-fpid="fp${j}"]`).click();
      assert.ok(await page.locator('mark.grammar-hl').count()>0,`fp${i} has no visible highlight`);
      for (let j=1;j<=5;j++) if (j!==i) await page.locator(`.hl-legend-item[data-fpid="fp${j}"]`).click();
    }
    await page.locator('[data-tab="part4"]').click();
    await page.locator('#q25 .correct-item').click();
    assert.ok(await page.locator('.evidence-hl').count()>0);
    await page.locator('#tab-part4').screenshot({path:path.join(out,'reading.png')});
    const emailHeaders = await page.locator('.email-meta').first().innerText();
    assert.match(emailHeaders,/<megan.white-0211@w.g-college.net>/);
    assert.match(emailHeaders,/<alan.jones-0427@w.g-college.net>/);
    assert.match(emailHeaders,/A film event/);

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),15);
    assert.equal(await page.locator('.fp-q').count(),20);
    for (let i=1;i<=5;i++) await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),5);
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    if (hasAudio) {
      const audio = await page.evaluate(async url => {
        const d=await (await fetch(url)).json();
        const dir=url.replace(/data\.json$/,'');
        const refs=[...d.vocabulary.flatMap(v=>[v.wordAudio,v.exampleAudio]),...d.lessonPlan.focusPoints.map(f=>f.practicePassage.audioFile)];
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
      assert.equal(audio.length,85);
      assert.ok(audio.every(a=>a.duration>0.2));
      console.log('AUDIO_DECODE_OK',audio.length);
    } else {
      console.log('AUDIO_SKIPPED: run data/grade-pre2/2026-2/_gen_tts.py to add audio');
    }
    for (let i=0;i<data.sections.length;i++) {
      const part=`part${i+1}`, section=data.sections[i];
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
    await page.locator('#examCheckboxes input[value="2026-2"]').check();
    assert.match(await page.locator('.teacher-material-row[data-exam="2026-2"]').innerText(),/A4縦5枚（1枚に1つの文法事項）/);
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const pdfHref=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(pdfHref,/GradePre2_2026-2_Practice_Exam/);
    for (const href of [pdfHref, await page.locator('.teacher-material-row[data-exam="2026-2"] a').first().getAttribute('href')]) {
      const response=await page.request.get(`${base}/${href}`);
      assert.equal(response.status(),200,href);
      assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    }
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    assert.deepEqual(errors,[]);
    console.log(`UI OK: catalog order, 29 questions, ${sentences} slash-reading sentences, evidence, markers, 5 focus points, ${hasAudio ? '85 decoded audio' : 'no audio buttons yet'}, mobile, practice and grammar PDFs`);
    console.log('QA screenshots:',out);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
