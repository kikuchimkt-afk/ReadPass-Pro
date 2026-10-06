/* Isolated browser; exercise the repaired word-order implementation end to end. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=process.argv[2]||'http://127.0.0.1:8096';
const out=path.resolve(__dirname,'../tmp/qa-grade4-2026-2-sat');
fs.mkdirSync(out,{recursive:true});

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1365,height:1000}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    await page.goto(`${base}/top.html`);
    await page.locator('.grade-card').filter({hasText:'A1（4級相当）'}).click();
    const card=page.locator('.exam-card[href*="grade=grade4&exam=2026-2-sat&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2026年度 第2回（土曜準会場）/);
    await card.click();
    await page.waitForSelector('#q35',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/第2回（土曜準会場）/);
    assert.equal(await page.locator('.exam-question').count(),35);
    assert.equal(await page.locator('.exam-choice-btn').count(),140);
    assert.equal(await page.locator('.choice-analysis-item').count(),140);
    assert.equal(await page.locator('.exam-question .q-audio-btn').count(),25);
    assert.equal(await page.locator('.fp-card').count(),4);
    assert.equal(await page.locator('.fp-audio-btn').count(),4);
    assert.equal(await page.locator('.sentence-span').count(),37);
    assert.match(await page.locator('#vocabProgressText').innerText(),/30/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);
    const data=await page.evaluate(async()=>(await (await fetch('data/grade4/2026-2-sat/data.json')).json()));

    // Tap every original chunk, including multi-word chunks, into all 5 slots.
    await page.locator('[data-tab="part3"]').click();
    assert.match(await page.locator('#part3Instruction').innerText(),/2番目と4番目/);
    assert.match(await page.locator('#part3Instruction').innerText(),/小文字/);
    for(const q of data.sections[2].questions){
      const root=page.locator(`#q${q.number}`);
      assert.equal(await root.locator('.so-slot').count(),5);
      assert.deepEqual(await root.locator('.so-slot-answer').allTextContents(),['2番目','4番目']);
      assert.equal(await root.locator('.so-prefix').innerText(),q.framePrefix);
      assert.equal(await root.locator('.so-suffix').innerText(),q.frameSuffix);
      assert.equal(await root.locator('.so-word-btn').count(),5);
      for(const word of q.correctOrder)await root.locator(`.so-word-btn[data-widx="${word-1}"]`).click();
      assert.deepEqual(await root.locator('.so-slot').allTextContents(),q.correctOrder.map(i=>q.words[i-1]));
      assert.equal(await root.locator('.so-word-used').count(),5);
      // Used chunks intentionally have pointer-events:none; also test the guard.
      assert.equal(await root.locator('.so-word-used').first().evaluate(e=>getComputedStyle(e).pointerEvents),'none');
      await page.evaluate(([n,i])=>window._soClickWord(n,i),[q.number,q.correctOrder[0]-1]);
      assert.equal(await root.locator('.so-slot-filled').count(),5);
      await root.locator('.so-reset-btn').click();
      assert.equal(await root.locator('.so-slot-filled').count(),0);
      assert.deepEqual(await root.locator('.so-slot-answer').allTextContents(),['2番目','4番目']);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),35);
    await page.locator('#q25').screenshot({path:path.join(out,'order.png')});
    await page.screenshot({path:path.join(out,'order-view.png')});
    const qAudio=page.locator('#q25 .q-audio-btn');
    await qAudio.click();
    assert.ok(await qAudio.evaluate(e=>e.classList.contains('playing')));
    await qAudio.click();
    await page.locator('#btnSimpleMode').click();
    for(const s of data.sections){
      const qs=s.questions||s.passages.flatMap(p=>p.questions);
      for(const q of qs){
        assert.equal(await page.locator(`#q${q.number} .grammar-note`).textContent(),'📝 '+q.grammarSimple);
        assert.deepEqual(await page.locator(`#q${q.number} .choice-analysis-item`).allTextContents(),q.choiceAnalysisSimple.map((a,i)=>`${i+1}. ${a}`));
      }
    }
    assert.equal(await page.locator('.correct-item').count(),35);
    assert.equal(await page.locator('.fp-q').count(),12);
    await page.locator('#btnSimpleMode').click();

    await page.locator('[data-tab="vocab"]').click();
    const word=await page.locator('.vocab-word').evaluate(e=>e.firstChild.textContent.trim());
    const meaning=data.vocabulary.find(v=>v.word===word).meaning;
    const wordButton=page.locator('.vocab-word .vocab-audio-btn');
    await wordButton.click();
    assert.ok(await wordButton.evaluate(e=>e.classList.contains('playing')));
    await wordButton.click();
    await page.locator(`#vocabChoices .choice-btn[data-value="${meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);
    const exampleButton=page.locator('.result-example .vocab-audio-btn');
    await exampleButton.click();
    assert.ok(await exampleButton.evaluate(e=>e.classList.contains('playing')));
    await exampleButton.click();

    await page.locator('[data-tab="part4"]').click();
    await page.locator('#btnTranslation').click();
    assert.equal(await page.locator('.email-meta').count(),2);
    assert.match(await page.locator('.email-meta').first().innerText(),/From: Charlotte Green/);
    assert.match(await page.locator('.email-meta').nth(1).innerText(),/Date: October 21/);
    const sentence=page.locator('.sentence-span').filter({hasText:'Our second store on Sun Street will open on September 11.'});
    await sentence.click();
    assert.equal(await page.locator('.slash-reading-display').count(),1);
    assert.match(await page.locator('.slash-reading-display').innerText(),/9月11日/);
    assert.equal(await page.locator('.slash-reading-display .main-verb').first().innerText(),'will');
    await sentence.click();
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('.hl-legend-item').count(),4);
    assert.ok(await page.locator('#tab-part4 .grammar-hl').count()>0);
    await page.locator('.hl-legend-item[data-fpid="fp4"]').click();
    await page.locator('.hl-legend-item[data-fpid="fp4"]').click();
    await page.locator('#btnHighlight').click();
    assert.equal(await page.locator('#tab-part4 .grammar-hl').count(),0);
    await page.locator('#btnHighlight').click();
    assert.ok(await page.locator('#tab-part4 .grammar-hl').count()>0);
    // Restore normal rendering to retain the delegated evidence target attrs.
    await page.reload();
    await page.waitForSelector('#q35',{state:'attached'});
    await page.locator('[data-tab="part4"]').click();
    await page.locator('#btnAnswers').click();
    await page.locator('#q30 .correct-item').click();
    assert.ok(await page.locator('.evidence-hl').count()>0);
    await page.locator('#tab-part4').screenshot({path:path.join(out,'reading.png')});
    await page.screenshot({path:path.join(out,'reading-view.png')});

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),12);
    assert.equal(await page.locator('.fp-q').count(),12);
    for(let i=1;i<=4;i++)await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),4);
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    await page.locator('#fp-fp3').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'lesson-view.png')});
    await page.locator('#fp-fp3 .fp-audio-btn').click();
    await page.waitForFunction(()=>document.querySelector('#fp-fp3 .fp-audio-duration').textContent!=='0:00');
    await page.locator('#fp-fp3 .fp-audio-btn').click();
    const audio=await page.evaluate(async()=>{
      const d=await (await fetch('data/grade4/2026-2-sat/data.json')).json();
      const refs=[...d.sections.flatMap(s=>(s.questions||[]).map(q=>q.questionAudio)),...d.vocabulary.flatMap(v=>[v.wordAudio,v.exampleAudio]),...d.lessonPlan.focusPoints.flatMap(f=>[...f.examples.map(e=>e.audio),f.sourceQuoteAudio,f.practicePassage.audioFile])];
      const ctx=new AudioContext();
      try{return await Promise.all(refs.map(async ref=>{
        const r=await fetch(`data/grade4/2026-2-sat/${ref}`);
        if(!r.ok)throw Error(`${ref}: HTTP ${r.status}`);
        const decoded=await ctx.decodeAudioData(await r.arrayBuffer());
        return {ref,duration:decoded.duration};
      }));}finally{await ctx.close();}
    });
    assert.equal(audio.length,105);
    assert.ok(audio.every(a=>a.duration>0.2));
    console.log('AUDIO_DECODE_OK',audio.length,Math.min(...audio.map(a=>a.duration)),Math.max(...audio.map(a=>a.duration)));
    for(let i=0;i<data.sections.length;i++){
      const part=`part${i+1}`,s=data.sections[i],qs=s.questions||s.passages.flatMap(p=>p.questions);
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),qs.length);
      for(const q of qs)await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${qs.length} / ${qs.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),35);
    await page.locator('#btnTheme').click();
    await page.setViewportSize({width:390,height:844});
    await page.locator('[data-tab="part3"]').click();
    const mobileQ=data.sections[2].questions[4];
    for(const i of mobileQ.correctOrder)await page.locator(`#q25 .so-word-btn[data-widx="${i-1}"]`).click();
    assert.deepEqual(await page.locator('#q25 .so-slot').allTextContents(),mobileQ.correctOrder.map(i=>mobileQ.words[i-1]));
    await page.locator('#q25 .so-reset-btn').click();
    await page.locator('#q25 .so-frame').evaluate(e=>e.scrollIntoView({block:'center'}));
    await page.screenshot({path:path.join(out,'mobile-order-view.png')});
    await page.screenshot({path:path.join(out,'mobile-order.png'),fullPage:true});
    for(const width of [390,320,600]){
      await page.setViewportSize({width,height:844});
      const size=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));
      assert.ok(size.scroll<=size.width+1,`mobile overflow ${JSON.stringify(size)}`);
    }

    await page.setViewportSize({width:1365,height:1000});
    await page.goto(`${base}/print.html`);
    await page.locator('.grade-chip').filter({hasText:'A1（4級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2026-2-sat"]').check();
    await page.locator('#generateBtn').click();
    await page.waitForSelector('.fixed-exam-card');
    const href=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
    assert.match(href,/Grade4_2026-2-sat/);
    const response=await page.request.get(`${base}/${href}`);
    assert.equal(response.status(),200);
    assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    // Regression against the exact 2025 word-order fix requested by the user.
    await page.goto(`${base}/index.html?grade=grade4&exam=2025-3&nav=1`);
    await page.waitForSelector('#q35',{state:'attached'});
    await page.locator('[data-tab="part3"]').click();
    const old=await page.evaluate(async()=>(await (await fetch('data/grade4/2025-3/data.json')).json()).sections[2]);
    for(const q of old.questions){
      assert.equal(await page.locator(`#q${q.number} .so-prefix`).innerText(),q.framePrefix);
      assert.equal(await page.locator(`#q${q.number} .so-suffix`).innerText(),q.frameSuffix);
      for(const i of q.correctOrder)await page.locator(`#q${q.number} .so-word-btn[data-widx="${i-1}"]`).click();
      assert.deepEqual(await page.locator(`#q${q.number} .so-slot`).allTextContents(),q.correctOrder.map(i=>q.words[i-1]));
    }
    assert.deepEqual(errors,[]);
    console.log('UI OK: 35 questions, repaired order scratch pad/reset/slots, original frames, normal/easy explanations, 4 focus points, 105 decoded audio, mobile, 11-page PDF, 2025-3 regression');
    console.log('QA screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
