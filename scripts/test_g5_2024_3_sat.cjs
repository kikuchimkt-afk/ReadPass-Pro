/* Grade 5 2024-3 Saturday venue in an isolated browser: word order, lessons, audio, PDFs. */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const args=process.argv.slice(2);
const base=args.find(a=>!a.startsWith('--'))||'http://localhost:8085';
// Audio is required. --allow-missing-audio only lets the other checks run before _gen_tts.py has succeeded.
const allowMissingAudio=args.includes('--allow-missing-audio');
const out=path.resolve(__dirname,'../tmp/qa-grade5-2024-3-sat');
fs.mkdirSync(out,{recursive:true});

(async()=>{
  const pauseBeforeStopping=()=>new Promise(resolve=>setTimeout(resolve,500));
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1365,height:1000}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    const hasAudio=(await page.request.get(`${base}/data/grade5/2024-3-sat/audio/q1.mp3`)).ok();
    assert.ok(hasAudio||allowMissingAudio,'audio missing: run python -I data/grade5/2024-3-sat/_gen_tts.py (or pass --allow-missing-audio to run the other checks)');
    await page.goto(`${base}/top.html`);
    // Every grade lists its exams newest first; the main venue precedes the Saturday venue.
    const gradeNames=await page.locator('.grade-card:not(.disabled)').evaluateAll(cards=>cards.map(c=>c.innerText.split('\n')[0]));
    for(const name of gradeNames){
      await page.locator('.grade-card').filter({hasText:name}).first().click();
      const ids=await page.locator('.exam-card').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
      const keys=ids.map(id=>{const m=id.match(/^(\d{4})-(\d+)(-.+)?$/);return Number(m[1])*100+Number(m[2])*10+(m[3]?0:1);});
      assert.deepEqual(keys,[...keys].sort((a,b)=>b-a),`${name}: ${ids.join(',')}`);
      await page.locator('#backToGrades').click();
    }
    await page.locator('.grade-card').filter({hasText:'Pre-A1（5級相当）'}).click();
    const order=await page.locator('.exam-card').evaluateAll(cards=>cards.map(c=>new URL(c.href).searchParams.get('exam')));
    assert.equal(order.indexOf('2024-3-sat'),order.indexOf('2024-3')+1,order.join(','));
    const card=page.locator('.exam-card[href*="grade=grade5&exam=2024-3-sat&"]');
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2024年度 第3回（土曜準会場）/);
    await card.click();
    await page.waitForSelector('#q25',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2024年度 第3回（土曜準会場）/);
    assert.equal(await page.locator('.exam-question').count(),25);
    assert.equal(await page.locator('.exam-choice-btn').count(),100);
    assert.equal(await page.locator('.choice-analysis-item').count(),100);
    assert.equal(await page.locator('.exam-question .q-audio-btn').count(),25);
    assert.equal(await page.locator('.fp-card').count(),3);
    assert.equal(await page.locator('.fp-audio-btn').count(),3);
    assert.equal(await page.locator('.sentence-span').count(),0);
    assert.match(await page.locator('#vocabProgressText').innerText(),/20/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);
    const data=await page.evaluate(async()=>(await (await fetch('data/grade5/2024-3-sat/data.json')).json()));

    // Tap four intact chunks; fixed prefix/suffix never count as answer slots.
    await page.locator('[data-tab="part3"]').click();
    assert.match(await page.locator('#part3Instruction').innerText(),/1番目と3番目/);
    assert.match(await page.locator('#part3Instruction').innerText(),/小文字/);
    for(const q of data.sections[2].questions){
      const root=page.locator(`#q${q.number}`);
      assert.equal(await root.locator('.so-slot').count(),4);
      assert.deepEqual(await root.locator('.so-slot-answer').allTextContents(),['1番目','3番目']);
      assert.equal(await root.locator('.so-prefix').innerText(),q.framePrefix);
      assert.equal(await root.locator('.so-suffix').innerText(),q.frameSuffix);
      assert.equal(await root.locator('.so-word-btn').count(),4);
      for(const word of q.correctOrder)await root.locator(`.so-word-btn[data-widx="${word-1}"]`).click();
      assert.deepEqual(await root.locator('.so-slot').allTextContents(),q.correctOrder.map(i=>q.words[i-1]));
      assert.equal(await root.locator('.so-word-used').count(),4);
      // Used chunks intentionally have pointer-events:none; also test the guard.
      assert.equal(await root.locator('.so-word-used').first().evaluate(e=>getComputedStyle(e).pointerEvents),'none');
      await page.evaluate(([n,i])=>window._soClickWord(n,i),[q.number,q.correctOrder[0]-1]);
      assert.equal(await root.locator('.so-slot-filled').count(),4);
      await root.locator('.so-reset-btn').click();
      assert.equal(await root.locator('.so-slot-filled').count(),0);
      assert.deepEqual(await root.locator('.so-slot-answer').allTextContents(),['1番目','3番目']);
    }
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),25);
    await page.locator('#q25').screenshot({path:path.join(out,'order.png')});
    await page.screenshot({path:path.join(out,'order-view.png')});
    if(hasAudio){
      const qAudio=page.locator('#q25 .q-audio-btn');
      await qAudio.click();
      assert.ok(await qAudio.evaluate(e=>e.classList.contains('playing')));
      await pauseBeforeStopping();
      await qAudio.click();
    }
    await page.locator('#btnSimpleMode').click();
    for(const s of data.sections){
      const qs=s.questions;
      for(const q of qs){
        assert.equal(await page.locator(`#q${q.number} .grammar-note`).textContent(),'📝 '+q.grammarSimple);
        assert.deepEqual(await page.locator(`#q${q.number} .choice-analysis-item`).allTextContents(),q.choiceAnalysisSimple.map((a,i)=>`${i+1}. ${a}`));
      }
    }
    assert.equal(await page.locator('.correct-item').count(),25);
    assert.equal(await page.locator('.fp-q').count(),9);
    await page.locator('#btnSimpleMode').click();
    for(const section of data.sections)for(const q of section.questions){
      assert.equal(await page.locator(`#q${q.number} .grammar-note`).textContent(),'📝 '+q.grammar);
      assert.deepEqual(await page.locator(`#q${q.number} .choice-analysis-item`).allTextContents(),q.choiceAnalysis.map((a,i)=>`${i+1}. ${a}`));
    }

    await page.locator('[data-tab="vocab"]').click();
    const word=await page.locator('.vocab-word').evaluate(e=>e.firstChild.textContent.trim());
    const meaning=data.vocabulary.find(v=>v.word===word).meaning;
    const wordButton=page.locator('.vocab-word .vocab-audio-btn');
    assert.equal(await wordButton.count(),1);
    if(hasAudio){
      await wordButton.click();
      assert.ok(await wordButton.evaluate(e=>e.classList.contains('playing')));
      await pauseBeforeStopping();
      await wordButton.click();
    }
    await page.locator(`#vocabChoices .choice-btn[data-value="${meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);
    const exampleButton=page.locator('.result-example .vocab-audio-btn');
    assert.equal(await exampleButton.count(),1);
    if(hasAudio){
      await exampleButton.click();
      assert.ok(await exampleButton.evaluate(e=>e.classList.contains('playing')));
      await pauseBeforeStopping();
      await exampleButton.click();
    }

    await page.locator('[data-tab="lesson"]').click();
    assert.equal(await page.locator('.fp-example').count(),9);
    assert.equal(await page.locator('.fp-q').count(),9);
    for(let i=1;i<=3;i++)await page.locator(`#fp-fp${i} .fp-header`).click();
    assert.equal(await page.locator('.fp-card.open').count(),3);
    for(const [index,simple] of [false,true,false].entries()){
      if(index>0)await page.locator('#btnSimpleMode').click();
      for(const fp of data.lessonPlan.focusPoints){
        const root=page.locator(`#fp-${fp.id}`);
        assert.equal(await root.locator('.fp-why').textContent(),simple?fp.explanationSimple:fp.explanation);
        assert.deepEqual(await root.locator('.fp-example-note').allTextContents(),fp.examples.map(e=>'💡 '+(simple?e.noteSimple:e.note)));
        assert.deepEqual(await root.locator('.fp-q').allTextContents(),(simple?fp.practiceQuestionsSimple:fp.practiceQuestions).map((q,i)=>`Q${i+1}. ${q.q}`));
        assert.deepEqual(await root.locator('.fp-a').allTextContents(),(simple?fp.practiceQuestionsSimple:fp.practiceQuestions).map(q=>q.a));
      }
    }
    // Mode switching re-renders cards, so reopen before interaction checks.
    for(let i=1;i<=3;i++)if(!await page.locator(`#fp-fp${i}`).evaluate(e=>e.classList.contains('open')))await page.locator(`#fp-fp${i} .fp-header`).click();
    await page.locator('#fp-fp3 .fp-a-toggle').first().click();
    assert.equal(await page.locator('#fp-fp3 .fp-a.show').count(),1);
    await page.locator('#fp-fp3 .fp-trans-btn').click();
    assert.ok(await page.locator('#pp-fp3-ja').isVisible());
    assert.equal(await page.locator('#pp-fp3-ja').innerText(),data.lessonPlan.focusPoints[2].practicePassage.ja);
    await page.locator('#fp-fp3 .fp-trans-btn').click();
    assert.equal(await page.locator('#pp-fp3-ja').isVisible(),false);
    await page.locator('#fp-fp3 .fp-pattern-hl-btn').click();
    assert.ok(await page.locator('#pp-fp3 .fp-hl-mark').count()>0);
    await page.locator('#fp-fp3 .fp-pattern-hl-btn').click();
    assert.equal(await page.locator('#pp-fp3 .fp-hl-mark').count(),0);
    await page.locator('#tab-lesson').screenshot({path:path.join(out,'lesson.png')});
    await page.locator('#fp-fp3').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(out,'lesson-view.png')});
    if(hasAudio){
    await page.locator('#fp-fp3 .fp-audio-btn').click();
    await page.waitForFunction(()=>document.querySelector('#fp-fp3 .fp-audio-duration').textContent!=='0:00');
    await pauseBeforeStopping();
    await page.locator('#fp-fp3 .fp-audio-btn').click();
    const audio=await page.evaluate(async()=>{
      const d=await (await fetch('data/grade5/2024-3-sat/data.json')).json();
      const refs=[...d.sections.flatMap(s=>(s.questions||[]).map(q=>q.questionAudio)),...d.vocabulary.flatMap(v=>[v.wordAudio,v.exampleAudio]),...d.lessonPlan.focusPoints.flatMap(f=>[...f.examples.map(e=>e.audio),f.sourceQuoteAudio,f.practicePassage.audioFile])];
      const ctx=new AudioContext();
      try{return await Promise.all(refs.map(async ref=>{
        const r=await fetch(`data/grade5/2024-3-sat/${ref}`);
        if(!r.ok)throw Error(`${ref}: HTTP ${r.status}`);
        const decoded=await ctx.decodeAudioData(await r.arrayBuffer());
        return {ref,duration:decoded.duration};
      }));}finally{await ctx.close();}
    });
    assert.equal(audio.length,80);
    assert.ok(audio.every(a=>a.duration>0.2));
    console.log('AUDIO_DECODE_OK',audio.length,Math.min(...audio.map(a=>a.duration)),Math.max(...audio.map(a=>a.duration)));
    }else console.log('AUDIO_SKIPPED (--allow-missing-audio): run data/grade5/2024-3-sat/_gen_tts.py, then rerun without the flag');
    for(let i=0;i<data.sections.length;i++){
      const part=`part${i+1}`,s=data.sections[i],qs=s.questions;
      await page.locator(`[data-tab="${part}"]`).click();
      assert.equal(await page.locator(`#tab-${part} .exam-question`).count(),qs.length);
      for(const q of qs)await page.locator(`.exam-choice-btn[data-q="${q.number}"][data-val="${q.answer}"]`).click();
      await page.locator(`#${part}Submit`).click();
      assert.equal(await page.locator(`#${part}Results .big-score`).innerText(),`${qs.length} / ${qs.length}`);
    }
    assert.equal(await page.locator('.exam-choice-btn.correct').count(),25);
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
    await page.locator('.grade-chip').filter({hasText:'英検5級'}).click();
    await page.locator('#examCheckboxes input[value="2024-3-sat"]').check();
    const practicePdf='output/pdf/ReadPass_EIKEN_Grade5_2024-3-sat_Practice_Exam_Large_Type_v1.pdf';
    const guidePdf='output/pdf/ReadPass_EIKEN_Grade5_2024-3-sat_Grammar_Guide_v1.pdf';
    const pdfUrls=[practicePdf,guidePdf];
    // The fixed-PDF entry (print.js) and the grammar guide manifest are registered after this
    // exam is built; until then only those two rows are skipped and the PDF files are checked directly.
    const fixedRegistered=(await (await page.request.get(`${base}/print.js`)).text()).includes("'grade5/2024-3-sat': {");
    const guideListed=Boolean((await (await page.request.get(`${base}/output/pdf/grammar_guides.json`)).json())['grade5/2024-3-sat']);
    if(guideListed){
      assert.match(await page.locator('.teacher-material-row[data-exam="2024-3-sat"]').innerText(),/A4縦3枚（1枚に1つの文法事項）/);
      pdfUrls.push(await page.locator('.teacher-material-row[data-exam="2024-3-sat"] a').first().getAttribute('href'));
    }else console.log('SKIPPED: grammar-guide print row (grammar_guides.json has no grade5/2024-3-sat entry yet); the guide PDF file is checked directly');
    if(fixedRegistered){
      assert.match(await page.locator('.teacher-material-row[data-fixed-exam="2024-3-sat"]').innerText(),/A4縦6ページ/);
      await page.locator('#generateBtn').click();
      await page.waitForSelector('.fixed-exam-card');
      const href=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
      assert.match(href,/Grade5_2024-3-sat_Practice_Exam_Large_Type_v1\.pdf/);
      pdfUrls.push(href);
    }else console.log('SKIPPED: fixed-PDF print rows (print.js FIXED_EXAM_PDFS has no grade5/2024-3-sat entry yet); the practice PDF file is checked directly');
    for(const url of pdfUrls){
      const response=await page.request.get(`${base}/${url}`);
      assert.equal(response.status(),200,url);
      assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-',url);
    }
    await page.screenshot({path:path.join(out,'print.png'),fullPage:true});
    // Regression against the exact 2025 word-order fix requested by the user.
    await page.goto(`${base}/index.html?grade=grade5&exam=2025-3&nav=1`);
    await page.waitForSelector('#q25',{state:'attached'});
    await page.locator('[data-tab="part3"]').click();
    const old=await page.evaluate(async()=>(await (await fetch('data/grade5/2025-3/data.json')).json()).sections[2]);
    for(const q of old.questions){
      assert.equal(await page.locator(`#q${q.number} .so-slot`).count(),4);
      assert.deepEqual(await page.locator(`#q${q.number} .so-slot-answer`).allTextContents(),['1番目','3番目']);
      assert.equal(await page.locator(`#q${q.number} .so-prefix`).innerText(),q.framePrefix);
      assert.equal(await page.locator(`#q${q.number} .so-suffix`).innerText(),q.frameSuffix);
      for(const i of q.correctOrder)await page.locator(`#q${q.number} .so-word-btn[data-widx="${i-1}"]`).click();
      assert.deepEqual(await page.locator(`#q${q.number} .so-slot`).allTextContents(),q.correctOrder.map(i=>q.words[i-1]));
    }
    assert.deepEqual(errors,[]);
    console.log(`UI OK: catalog order, 25 questions, four intact chunks, first/third slots, reset/frames, normal/easy explanations, 3 focus points, ${hasAudio?'80 decoded audio':'AUDIO SKIPPED'}, mobile, practice and grammar PDFs${fixedRegistered&&guideListed?' (print rows)':' (print rows SKIPPED until registered)'}, 2025-3 regression`);
    console.log('QA screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
