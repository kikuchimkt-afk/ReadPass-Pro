/* Grade 3 2026-2 (main venue): established learning features, in an isolated browser profile. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=process.argv[2]||'http://127.0.0.1:8098';
const out=path.resolve(__dirname,'../tmp/qa-grade3-2026-2');
const compact=s=>s.replace(/\s+/g,'');
fs.mkdirSync(out,{recursive:true});

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try{
    const page=await browser.newPage({viewport:{width:1365,height:1000}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    const data=await (await page.request.get(`${base}/data/grade3/2026-2/data.json`)).json();
    const hasAudio=data.vocabulary.every(v=>v.wordAudio);
    await page.goto(`${base}/top.html`);
    // Every grade lists its exams newest first; the main venue precedes the sub-venue.
    const gradeNames=await page.locator('.grade-card:not(.disabled)').evaluateAll(cards=>cards.map(c=>c.innerText.split('\n')[0]));
    for(const name of gradeNames){
      await page.locator('.grade-card').filter({hasText:name}).first().click();
      const ids=await page.locator('.exam-card').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
      const keys=ids.map(id=>{const m=id.match(/^(\d{4})-(\d+)(-.+)?$/);return Number(m[1])*100+Number(m[2])*10+(m[3]?0:1);});
      assert.deepEqual(keys,[...keys].sort((a,b)=>b-a),`${name}: ${ids.join(',')}`);
      await page.locator('#backToGrades').click();
    }
    await page.locator('.grade-card').filter({hasText:'A1（3級相当）'}).click();
    const card=page.locator('.exam-card[href*="grade=grade3&exam=2026-2&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2026年度 第2回(?!（)/);
    await card.click();
    await page.waitForSelector('#q30',{state:'attached'});
    await page.evaluate(()=>document.fonts.ready);
    const d=await page.evaluate(async()=>(await (await fetch('data/grade3/2026-2/data.json')).json()));
    const qs=[...d.sections.slice(0,2).flatMap(s=>s.questions),...d.sections[2].passages.flatMap(p=>p.questions)];
    assert.match(await page.locator('#examLabel').innerText(),/第2回(?!（)/);
    assert.equal(await page.locator('.exam-question').count(),30);
    assert.equal(await page.locator('.exam-choice-btn').count(),120);
    assert.equal(await page.locator('.choice-analysis-item').count(),120);
    assert.equal(await page.locator('.exam-question .q-audio-btn').count(),0);
    assert.equal(await page.locator('.so-slot').count(),0);
    assert.equal(await page.locator('.fp-card').count(),4);
    assert.equal(await page.locator('.sentence-span').count(),63);
    assert.match(await page.locator('#vocabProgressText').innerText(),/30/);
    await page.locator('#btnAnswers').click();
    await page.locator('#btnTranslation').click();
    for(const q of qs){
      assert.equal(await page.locator(`#q${q.number} .grammar-note`).textContent(),'📝 '+q.grammar);
      assert.deepEqual(await page.locator(`#q${q.number} .choice-analysis-item`).allTextContents(),q.choiceAnalysis.map((a,i)=>`${i+1}. ${a}`));
      assert.equal(await page.locator(`#q${q.number} > .translation-block`).innerText(),q.translation||q.questionTranslation);
      assert.deepEqual(await page.locator(`#q${q.number} .choice-translation`).allTextContents(),q.choiceTranslations);
    }
    await page.locator('#btnSimpleMode').click();
    for(const q of qs){
      assert.equal(await page.locator(`#q${q.number} .grammar-note`).textContent(),'📝 '+q.grammarSimple);
      assert.deepEqual(await page.locator(`#q${q.number} .choice-analysis-item`).allTextContents(),q.choiceAnalysisSimple.map((a,i)=>`${i+1}. ${a}`));
    }
    for(const fp of d.lessonPlan.focusPoints){
      assert.equal(await page.locator(`#fp-${fp.id} .fp-why`).textContent(),fp.explanationSimple);
      assert.deepEqual(await page.locator(`#fp-${fp.id} .fp-example-note`).allTextContents(),fp.examples.map(e=>'💡 '+e.noteSimple));
      assert.deepEqual(await page.locator(`#fp-${fp.id} .fp-q`).allTextContents(),fp.practiceQuestionsSimple.map((q,i)=>`Q${i+1}. ${q.q}`));
    }
    await page.locator('#btnSimpleMode').click();
    assert.equal(await page.locator('.correct-item').count(),30);
    await page.locator('[data-tab="part3"]').click();
    assert.equal(await page.locator('.email-meta').count(),3);
    for(let i=0;i<3;i++){
      const m=d.sections[2].passages[1].emails[i].meta;
      const text=await page.locator('.email-meta').nth(i).innerText();
      for(const k of ['from','to','date','subject'])assert.ok(text.includes(m[k]),`email ${i} ${k}`);
      assert.equal(await page.locator('.email-block .translation-block').nth(i).innerText(),d.sections[2].passages[1].emails[i].translation);
    }
    // Every clickable original row keeps its explicit bilingual slash data.
    const rows=d.sections[2].passages.flatMap(p=>p.sentencePairs);
    const spans=page.locator('.sentence-span');
    for(let i=0;i<63;i++){
      const span=spans.nth(i),en=await span.innerText(),r=rows.find(r=>r[0]===en);
      assert.ok(r,`original sentence ${en}`);
      await span.click();
      const display=span.locator('.slash-reading-display');
      assert.equal(await display.count(),1);
      const units=r[2].split('||').map(s=>s.split('|'));
      assert.deepEqual(await display.locator('.slash-en').allTextContents(),units.map(u=>u[0]));
      assert.deepEqual(await display.locator('.slash-ja').allTextContents(),units.map(u=>u[1]));
      if(r[3])assert.equal((await display.locator('.main-verb').first().innerText()).toLowerCase(),r[3].toLowerCase());
      else assert.equal(await display.locator('.main-verb').count(),0);
      await span.click();
    }
    console.log('SLASH_OK: all 63 clickable rows (77 bilingual rows include title/heading/headers)');
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),4);
    assert.ok(await page.locator('#tab-part3 .grammar-hl').count()>0);
    await page.locator('.hl-legend-item[data-fpid="fp3"]').click();
    await page.locator('.hl-legend-item[data-fpid="fp3"]').click();
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('#tab-part3 .grammar-hl').count(),0);
    // Reload to restore delegated evidence attributes after highlight rendering.
    await page.reload();
    await page.waitForSelector('#q30',{state:'attached'});
    await page.locator('[data-tab="part3"]').click();
    await page.locator('#btnAnswers').click();
    for(const q of qs.slice(20)){
      await page.locator(`#q${q.number} .correct-item`).click();
      const evidence=compact((await page.locator('.evidence-hl').allTextContents()).join(' '));
      assert.equal(evidence,compact(q.sourceEvidence.join(' ')),`Q${q.number} exact highlighted source evidence`);
    }
    await page.locator('#tab-part3').screenshot({path:path.join(out,'reading.png')});
    await page.screenshot({path:path.join(out,'reading-view.png')});
    await page.locator('[data-tab="vocab"]').click();
    const word=await page.locator('.vocab-word').evaluate(e=>e.firstChild.textContent.trim());
    const v=d.vocabulary.find(v=>v.word===word),wordButton=page.locator('.vocab-word .vocab-audio-btn');
    assert.equal(await wordButton.count(),hasAudio?1:0);
    if(hasAudio){
      await wordButton.click();
      await page.waitForTimeout(600);
      assert.ok(await wordButton.evaluate(e=>e.classList.contains('playing')));
      await wordButton.click();
    }
    await page.locator(`#vocabChoices .choice-btn[data-value="${v.meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);
    assert.ok((await page.locator('.result-example').innerText()).includes(v.example));
    assert.equal(await page.locator('.result-example .vocab-audio-btn').count(),0);
    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),12);
    assert.equal(await page.locator('.fp-q').count(),12);
    for(const f of d.lessonPlan.focusPoints){
      await page.locator(`#fp-${f.id} .fp-header`).click();
      assert.equal(await page.locator(`#fp-${f.id} .fp-why`).textContent(),f.explanation);
      assert.deepEqual(await page.locator(`#fp-${f.id} .fp-example-note`).allTextContents(),f.examples.map(e=>'💡 '+e.note));
    }
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    assert.equal(await page.locator('#tab-lesson .vocab-audio-btn, #tab-lesson .fp-audio-btn').count(),hasAudio?20:0);
    if(hasAudio){
    const exButton=page.locator('#fp-fp3 .fp-example .vocab-audio-btn').nth(2);
    await exButton.click();await page.waitForTimeout(600);
    assert.ok(await exButton.evaluate(e=>e.classList.contains('playing')));await exButton.click();
    const sourceButton=page.locator('#fp-fp4 .fp-source-quote .vocab-audio-btn');
    await sourceButton.click();await page.waitForTimeout(600);
    assert.ok(await sourceButton.evaluate(e=>e.classList.contains('playing')));await sourceButton.click();
    await page.locator('#fp-fp4 .fp-audio-btn').click();
    await page.waitForFunction(()=>document.querySelector('#fp-fp4 .fp-audio-duration').textContent!=='0:00');
    await page.waitForTimeout(600);await page.locator('#fp-fp4 .fp-audio-btn').click();
    const durations=await page.evaluate(async()=>{
      const d=await (await fetch('data/grade3/2026-2/data.json')).json();
      const refs=[...d.vocabulary.map(v=>v.wordAudio),...d.lessonPlan.focusPoints.flatMap(f=>[...f.examples.map(e=>e.audio),f.sourceQuoteAudio,f.practicePassage.audioFile])];
      const ctx=new AudioContext();
      try{return await Promise.all(refs.map(async ref=>{
        const r=await fetch(`data/grade3/2026-2/${ref}`);if(!r.ok)throw Error(`${ref}: HTTP ${r.status}`);
        return (await ctx.decodeAudioData(await r.arrayBuffer())).duration;
      }));}finally{await ctx.close();}
    });
    assert.equal(durations.length,50);assert.ok(durations.every(s=>s>0.2));
    console.log('AUDIO_DECODE_OK',durations.length,Math.min(...durations),Math.max(...durations));
    }else console.log('AUDIO_SKIPPED: run data/grade3/2026-2/_gen_tts.py to add audio');
    for(let i=0;i<3;i++){
      const part=`part${i+1}`,s=d.sections[i],items=s.questions||s.passages.flatMap(p=>p.questions);
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),items.length);
      for(const q of items)await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${items.length} / ${items.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),30);
    await page.locator('#btnTheme').click();
    for(const width of [390,320,600]){
      await page.setViewportSize({width,height:844});
      for(const tab of ['part1','part2','part3','lesson','vocab']){
        await page.locator(`[data-tab="${tab}"]`).click();
        const size=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));
        assert.ok(size.scroll<=size.width+1,`${tab} mobile overflow ${JSON.stringify(size)}`);
      }
    }
    await page.setViewportSize({width:390,height:844});
    await page.locator('[data-tab="part3"]').click();
    await page.locator('.email-meta').nth(2).scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'mobile-email-view.png')});
    await page.setViewportSize({width:1365,height:1000});
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:'A1（3級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2026-2"]').check();
    assert.match(await page.locator('.teacher-material-row[data-exam="2026-2"]').innerText(),/A4縦4枚（1枚に1つの文法事項）/);
    await page.locator('#generateBtn').click();await page.waitForSelector('.fixed-exam-card');
    const href=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(href,/Grade3_2026-2_Practice_Exam/);
    for(const url of [href,await page.locator('.teacher-material-row[data-exam="2026-2"] a').first().getAttribute('href')]){
      const response=await page.request.get(`${base}/${url}`);
      assert.equal(response.status(),200,url);assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    }
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    await page.goto(`${base}/index.html?grade=grade3&exam=2026-2-sat&nav=1`);
    await page.waitForSelector('#q30',{state:'attached'});
    assert.equal(await page.locator('.exam-question').count(),30);
    assert.equal(await page.locator('.email-meta').count(),3);
    assert.equal(await page.locator('.fp-card').count(),4);
    assert.deepEqual(errors,[]);
    console.log(`UI OK: catalog order, 30 questions, 3 complete emails, normal/easy explanations, 63 slash popups, evidence, 4 focus points, ${hasAudio?'50 decoded audio':'no audio buttons yet'}, 320/390/600px, practice and grammar PDFs, Saturday 2026-2 regression`);
    console.log('QA screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
