/* Grade 4 2024-2 Saturday in an isolated browser: word order, reading, lessons, audio, PDFs.
   Usage: node scripts/test_g4_2024_2_sat.cjs <base-url> [--allow-missing-audio] */
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const base=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://localhost:8085').replace(/\/$/,'');
const allowMissingAudio=process.argv.includes('--allow-missing-audio');
const exam='2024-2-sat',folder=`data/grade4/${exam}`;
// Clickable rows: notice 8 (title heading excluded; date and three schedule lines included),
// e-mail bodies 22 (greeting, sentences, sign-off and name), story 15.
const SPANS=45;
const PRACTICE_PAGES=11,GUIDE_PAGES=4;
const practicePdf=`output/pdf/ReadPass_EIKEN_Grade4_${exam}_Practice_Exam_Large_Type_v1.pdf`;
const guidePdf=`output/pdf/ReadPass_EIKEN_Grade4_${exam}_Grammar_Guide_v1.pdf`;
const out=path.resolve(__dirname,'../tmp/qa-grade4-2024-2-sat');
fs.mkdirSync(out,{recursive:true});

(async()=>{
  const browser=await chromium.launch({channel:'chrome',headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1365,height:1000}});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.setDefaultTimeout(15000);
    const hasAudio=(await page.request.get(`${base}/${folder}/audio/q1.mp3`)).status()===200;
    assert.ok(hasAudio||allowMissingAudio,`audio missing: run python -I ${folder}/_gen_tts.py (or pass --allow-missing-audio)`);
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
    await page.locator('.grade-card').filter({hasText:'A1（4級相当）'}).click();
    const card=page.locator(`.exam-card[href*="grade=grade4&exam=${exam}&"]`);
    assert.equal(await card.count(),1);
    assert.match(await card.innerText(),/2024年度 第2回（土曜準会場）/);
    await card.click();
    await page.waitForSelector('#q35',{state:'attached'});
    assert.match(await page.locator('#examLabel').innerText(),/2024年度 第2回（土曜準会場）/);
    assert.equal(await page.locator('.exam-question').count(),35);
    assert.equal(await page.locator('.exam-choice-btn').count(),140);
    assert.equal(await page.locator('.choice-analysis-item').count(),140);
    assert.equal(await page.locator('.exam-question .q-audio-btn').count(),25);
    assert.equal(await page.locator('.fp-card').count(),4);
    assert.equal(await page.locator('.fp-audio-btn').count(),4);
    assert.equal(await page.locator('.sentence-span').count(),SPANS);
    assert.match(await page.locator('#vocabProgressText').innerText(),/30/);
    assert.equal(await page.locator('#penpassLink').isVisible(),false);
    const data=await page.evaluate(async f=>(await (await fetch(`${f}/data.json`)).json()),folder);

    // Tap every original chunk, including the two-word chunks "my room", "his friends" and
    // "the corner", into all 5 slots. (21) has no frame before the slots and (24) starts a
    // new sentence after "Excuse me." with the lower-case chunk "which".
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
    assert.equal(await page.locator('#q21 .so-prefix').innerText(),'');
    assert.equal(await page.locator('#q24 .so-prefix').innerText(),'Excuse me.');
    assert.ok((await page.locator('#q24 .so-word-btn').allTextContents()).some(t=>/\bwhich\b/.test(t)));
    await page.locator('#btnAnswers').click();
    assert.equal(await page.locator('.choice-analysis:not(.hidden)').count(),35);
    assert.match(await page.locator('#q24 .grammar-note').innerText(),/Excuse me\. Which train goes to Kyoto\?/);
    await page.locator('#q23').screenshot({path:path.join(out,'order.png')});
    await page.screenshot({path:path.join(out,'order-view.png')});
    if(hasAudio){
      const qAudio=page.locator('#q25 .q-audio-btn');
      await qAudio.click();
      assert.ok(await qAudio.evaluate(e=>e.classList.contains('playing')));
      await qAudio.click();
    }
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
    assert.equal(await wordButton.count(),1);
    if(hasAudio){
      await wordButton.click();
      assert.ok(await wordButton.evaluate(e=>e.classList.contains('playing')));
      await wordButton.click();
    }
    await page.locator(`#vocabChoices .choice-btn[data-value="${meaning}"]`).click();
    assert.equal(await page.locator('.vocab-result.correct').count(),1);
    const exampleButton=page.locator('.result-example .vocab-audio-btn');
    assert.equal(await exampleButton.count(),1);
    if(hasAudio){
      await exampleButton.click();
      assert.ok(await exampleButton.evaluate(e=>e.classList.contains('playing')));
      await exampleButton.click();
    }

    await page.locator('[data-tab="part4"]').click();
    await page.locator('#btnTranslation').click();
    assert.match(await page.locator('.notice-heading').innerText(),/TO ALL STUDENTS/);
    for(const line of ['October 1','From today, the school library will open at different times.','Monday to Friday: 8:00 a.m. to 7:00 p.m.','Saturday: 9:00 a.m. to 5:00 p.m.','Sunday: Closed'])
      assert.equal(await page.locator('.notice-frame .sentence-span').filter({hasText:line}).count(),1,line);
    // Each schedule line is its own block, so the three lines never run together.
    const tops=await page.locator('.notice-frame .sentence-span').filter({hasText:/^(Monday to Friday|Saturday|Sunday):/}).evaluateAll(es=>es.map(e=>Math.round(e.getBoundingClientRect().top)));
    assert.equal(new Set(tops).size,3);
    assert.equal(await page.locator('.email-meta').count(),2);
    assert.match(await page.locator('.email-meta').first().innerText(),/From: Elizabeth Young/);
    assert.match(await page.locator('.email-meta').nth(1).innerText(),/Date: April 26/);
    const sentence=page.locator('.sentence-span').filter({hasText:'You must ask a teacher before you use them.'});
    await sentence.click();
    assert.equal(await page.locator('.slash-reading-display').count(),1);
    assert.match(await page.locator('.slash-reading-display').innerText(),/先生に尋ねなければなりません/);
    assert.equal(await page.locator('.slash-reading-display .main-verb').first().innerText(),'ask');
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
    for(const q of data.sections[3].passages.flatMap(p=>p.questions)){
      await page.locator(`#q${q.number} .correct-item`).click();
      const evidence=(await page.locator('.evidence-hl').allTextContents()).join(' ').replace(/\s+/g,'');
      for(const e of q.sourceEvidence)assert.ok(evidence.includes(e.replace(/\s+/g,'')),`Q${q.number} highlighted evidence: ${e}`);
    }
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
    if(hasAudio){
      await page.locator('#fp-fp3 .fp-audio-btn').click();
      await page.waitForFunction(()=>document.querySelector('#fp-fp3 .fp-audio-duration').textContent!=='0:00');
      await page.locator('#fp-fp3 .fp-audio-btn').click();
      const audio=await page.evaluate(async f=>{
        const d=await (await fetch(`${f}/data.json`)).json();
        const refs=[...d.sections.flatMap(s=>(s.questions||[]).map(q=>q.questionAudio)),...d.vocabulary.flatMap(v=>[v.wordAudio,v.exampleAudio]),...d.lessonPlan.focusPoints.flatMap(fp=>[...fp.examples.map(e=>e.audio),fp.sourceQuoteAudio,fp.practicePassage.audioFile])];
        const ctx=new AudioContext();
        try{return await Promise.all(refs.map(async ref=>{
          const r=await fetch(`${f}/${ref}`);
          if(!r.ok)throw Error(`${ref}: HTTP ${r.status}`);
          const decoded=await ctx.decodeAudioData(await r.arrayBuffer());
          return {ref,duration:decoded.duration};
        }));}finally{await ctx.close();}
      },folder);
      assert.equal(audio.length,105);
      assert.ok(audio.every(a=>a.duration>0.2));
      console.log('AUDIO_DECODE_OK',audio.length,Math.min(...audio.map(a=>a.duration)),Math.max(...audio.map(a=>a.duration)));
    }else console.log(`AUDIO_SKIPPED (--allow-missing-audio): run python -I ${folder}/_gen_tts.py`);
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
    const mobileQ=data.sections[2].questions[2];
    for(const i of mobileQ.correctOrder)await page.locator(`#q23 .so-word-btn[data-widx="${i-1}"]`).click();
    assert.deepEqual(await page.locator('#q23 .so-slot').allTextContents(),mobileQ.correctOrder.map(i=>mobileQ.words[i-1]));
    await page.locator('#q23 .so-reset-btn').click();
    await page.locator('#q23 .so-frame').evaluate(e=>e.scrollIntoView({block:'center'}));
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
    await page.locator(`#examCheckboxes input[value="${exam}"]`).check();
    const pdfUrls=[guidePdf,practicePdf];
    // The grammar-guide row appears once output/pdf/grammar_guides.json has 'grade4/2024-2-sat'.
    const guideListed=Boolean((await (await page.request.get(`${base}/output/pdf/grammar_guides.json`)).json())[`grade4/${exam}`]);
    if(guideListed){
      assert.match(await page.locator(`.teacher-material-row[data-exam="${exam}"]`).innerText(),/A4縦4枚（1枚に1つの文法事項）/);
      const guideHref=await page.locator(`.teacher-material-row[data-exam="${exam}"] a`).first().getAttribute('href');
      assert.match(guideHref,/Grade4_2024-2-sat_Grammar_Guide/);
      pdfUrls.push(guideHref);
    }else{
      assert.equal(await page.locator(`.teacher-material-row[data-exam="${exam}"]`).count(),0);
      console.log(`GRAMMAR_GUIDE_ROW_SKIPPED: add 'grade4/${exam}' to output/pdf/grammar_guides.json (${GUIDE_PAGES} pages); the guide PDF itself is checked below`);
    }
    // The fixed-PDF row appears once print.js FIXED_EXAM_PDFS has 'grade4/2024-2-sat'.
    const printJs=await (await page.request.get(`${base}/print.js`)).text();
    const fixedRegistered=printJs.includes(`'grade4/${exam}': {`);
    if(fixedRegistered){
      await page.locator('#generateBtn').click();
      await page.waitForSelector('.fixed-exam-card');
      const href=await page.locator('.fixed-exam-actions a').first().getAttribute('href');
      assert.match(href,/Grade4_2024-2-sat_Practice_Exam_Large_Type_v1/);
      assert.match(await page.locator(`.teacher-material-row[data-fixed-exam="${exam}"]`).innerText(),new RegExp(`A4縦${PRACTICE_PAGES}ページ`));
      pdfUrls.push(href);
    }else console.log(`FIXED_PDF_ROW_SKIPPED: add FIXED_EXAM_PDFS['grade4/${exam}'] (${PRACTICE_PAGES} pages) to print.js; the practice PDF itself is checked below`);
    for(const url of pdfUrls){
      const response=await page.request.get(`${base}/${url}`);
      assert.equal(response.status(),200,url);
      assert.equal((await response.body()).subarray(0,5).toString(),'%PDF-');
    }
    // Page counts of the two files themselves (reportlab writes one /Type /Page object per page).
    for(const [file,pages] of [[guidePdf,GUIDE_PAGES],[practicePdf,PRACTICE_PAGES]]){
      const bytes=fs.readFileSync(path.resolve(__dirname,'..',file)).toString('latin1');
      assert.equal((bytes.match(/\/Type\s*\/Page(?![s\w])/g)||[]).length,pages,file);
    }
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
    console.log(`UI OK: catalog order, 35 questions, order scratch pad/reset/slots, original frames (empty and sentence-ending prefixes), normal/easy explanations, all reading evidence, 4 focus points, ${hasAudio?'105 decoded audio':'audio skipped'}, mobile, ${fixedRegistered?'fixed practice PDF row, ':''}${guideListed?'grammar guide row, ':''}practice PDF ${PRACTICE_PAGES} pages + grammar guide PDF ${GUIDE_PAGES} pages, 2025-3 regression`);
    console.log('QA screenshots:',out);
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
