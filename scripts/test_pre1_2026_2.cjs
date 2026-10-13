/* Headless, isolated regression checks; never touches a user's browser profile.
 * Usage: node scripts/test_pre1_2026_2.cjs http://127.0.0.1:8094
 * Set PW_CHROMIUM_PATH to use a bundled Chromium instead of installed Chrome. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://127.0.0.1:8094';
const out = path.resolve(__dirname, '../tmp/qa-grade-pre1-2026-2');
fs.mkdirSync(out, {recursive:true});
const dataUrl = 'data/pre-grade1/2026-2/data.json';

(async () => {
  const launchOptions = process.env.PW_CHROMIUM_PATH
    ? {executablePath: process.env.PW_CHROMIUM_PATH, headless: true}
    : {channel: 'chrome', headless: true};
  const browser = await chromium.launch(launchOptions);
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').filter({hasText:'B2（準1級相当）'}).click();
    const card = page.locator('.exam-card[href*="grade=pre-grade1&exam=2026-2&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2026年度 第2回/);
    await card.click();
    await page.waitForSelector('#q31',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2026年度 第2回$/);

    const data = await page.evaluate(async url => (await fetch(url)).json(), dataUrl);
    const hasAudio = data.vocabulary.every(v => v.wordAudio);
    const pairCount = data.sections.flatMap(s => s.passages || []).reduce((n, p) => n + p.sentencePairs.length, 0);
    assert.equal(await page.locator('.exam-question').count(),31);
    assert.equal(await page.locator('.exam-choice-btn').count(),124);
    assert.equal(await page.locator('.choice-analysis-item').count(),124);
    assert.equal(await page.locator('.fp-card').count(),5);
    assert.equal(await page.locator('.fp-audio-btn').count(),hasAudio ? 5 : 0);
    assert.equal(await page.locator('.sentence-span').count(),pairCount);
    assert.match(await page.locator('#vocabProgressText').innerText(),/80/);

    await page.locator('[data-tab="vocab"]').click();
    const word = await page.locator('.vocab-word').evaluate(e=>e.firstChild.textContent.trim());
    const meaning = data.vocabulary.find(v=>v.word===word).meaning;
    assert.equal(await page.locator('.vocab-word .vocab-audio-btn').count(),hasAudio ? 1 : 0);
    await page.locator(`#vocabChoices .choice-btn[data-value="${meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);

    for (const [part,count] of [['part1',18],['part2',6],['part3',7]]) {
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),count);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),31);
    await page.locator('#btnTranslation').click();
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#tab-part3 .sentence-span').first().click();
    assert.equal(await page.locator('.slash-reading-display').count(),1);
    assert.match(await page.locator('.slash-reading-display').innerText(),/低所得のアメリカ人/);
    assert.match(await page.locator('.slash-reading-display .main-verb').first().innerText(),/rely on/);
    await page.locator('#tab-part3 .sentence-span').first().click();
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),5);
    assert.ok(await page.locator('#tab-part3 .grammar-hl').count()>0);
    await page.locator('[data-tab="part2"]').click();
    assert.ok(await page.locator('#tab-part2 .grammar-hl').count()>0);
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#q28 .correct-item').click();
    assert.ok(await page.locator('.evidence-hl').count()>0);
    await page.screenshot({path:path.join(out,'reading-view.png')});

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),15);
    assert.equal(await page.locator('.fp-q').count(),20);
    for (let i=1;i<=5;i++) await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),5);
    await page.locator('#fp-fp1').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'lesson-view.png')});

    if (hasAudio) {
      const audio = await page.evaluate(async () => {
        const d=await (await fetch('data/pre-grade1/2026-2/data.json')).json();
        const refs=[...d.vocabulary.map(v=>v.wordAudio),...d.lessonPlan.focusPoints.map(f=>f.practicePassage.audioFile)];
        const ctx=new AudioContext();
        try {
          return await Promise.all(refs.map(async ref=>{
            const r=await fetch(`data/pre-grade1/2026-2/${ref}`);
            if (!r.ok) throw new Error(ref+': '+r.status);
            const buffer=await ctx.decodeAudioData(await r.arrayBuffer());
            return {ref,duration:buffer.duration};
          }));
        } finally {await ctx.close();}
      });
      assert.equal(audio.length,85);
      assert.ok(audio.every(a=>a.duration>0.2));
      console.log('AUDIO_DECODE_OK',audio.length);
    } else {
      console.log('AUDIO_SKIPPED: run data/pre-grade1/2026-2/_gen_tts.py to add audio');
    }

    for (let i=0;i<data.sections.length;i++) {
      const part=`part${i+1}`, section=data.sections[i];
      const qs=section.questions || section.passages.flatMap(p=>p.questions);
      await page.locator(`[data-tab="${part}"]`).click();
      for (const q of qs) await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${qs.length} / ${qs.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),31);

    await page.locator('#btnTheme').click();
    for (const width of [320,390,600]) {
      await page.setViewportSize({width,height:844});
      for (const part of ['part1','part2','part3','lesson']) {
        await page.locator(`[data-tab="${part}"]`).click();
        assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1), `overflow at ${width}px on ${part}`);
      }
    }
    await page.screenshot({path:path.join(out,'mobile-view.png')});

    await page.setViewportSize({width:1365,height:1000});
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:'B2（準1級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2026-2"]').check();
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const pdfHref=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(pdfHref,/GradePre1_2026-2_/);
    const response=await page.request.get(`${base}/${pdfHref}`);
    assert.equal(response.status(),200);
    assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});

    // The previous session must still load unchanged.
    await page.goto(`${base}/index.html?grade=pre-grade1&exam=2026-1&nav=1`);
    await page.waitForSelector('#q31',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2026年度 第1回$/);
    assert.deepEqual(errors,[]);
    console.log('UI OK: catalog, 31 questions, translations, slash reading, verb, evidence, markers, 5 focus points, mobile, fixed PDF');
    console.log('QA screenshots:',out);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
