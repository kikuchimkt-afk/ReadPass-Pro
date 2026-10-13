/* Every Saturday sub-venue exam ('-sat') is labelled （土曜準会場） the same way on the
   top.html card, the exam page header, print.html (venue chip, fixed PDF list) and the
   grammar guide manifest. Headless and isolated; never touches a user's browser profile. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const base = process.argv[2] || 'http://127.0.0.1:8085';
const satLabel = examId => {
  const [year, session] = examId.split('-');
  return `${year}年度 第${session}回（土曜準会場）`;
};

(async () => {
  const browser = await chromium.launch({channel:'chrome', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);

    // top.html: collect every '-sat' card, grade by grade.
    await page.goto(`${base}/top.html`);
    const gradeCount = await page.locator('.grade-card:not(.disabled)').count();
    const satExams = [];
    for (let i = 0; i < gradeCount; i++) {
      await page.locator('.grade-card:not(.disabled)').nth(i).click();
      for (const card of await page.locator('.exam-card[href*="-sat&"]').all()) {
        const params = new URL(await card.getAttribute('href'), base).searchParams;
        const exam = {grade:params.get('grade'), id:params.get('exam'), label:await card.locator('.exam-label').innerText()};
        assert.equal(exam.label, satLabel(exam.id), `${exam.grade}/${exam.id} card`);
        satExams.push(exam);
      }
      await page.locator('#backToGrades').click();
    }
    assert.ok(satExams.length >= 31, `${satExams.length} Saturday exams`);
    console.log('TOP_OK', satExams.length);

    // The exam page header ends with exactly the card label.
    for (const exam of satExams) {
      await page.goto(`${base}/index.html?grade=${exam.grade}&exam=${exam.id}&nav=1`);
      await page.waitForSelector('.exam-question', {state:'attached'});
      const header = await page.locator('#examLabel').innerText();
      assert.ok(header.endsWith(` · ${exam.label}`), `${exam.grade}/${exam.id} header: ${header}`);
    }
    console.log('HEADER_OK', satExams.length);

    // print.html: the venue chip says 土曜準会場 and the checkbox carries the same label.
    await page.goto(`${base}/print.html`);
    let printSat = 0;
    for (const chip of await page.locator('.grade-chip').all()) {
      await chip.click();
      for (const input of await page.locator('#examCheckboxes input[value$="-sat"]').all()) {
        const examId = await input.getAttribute('value');
        assert.equal(await input.getAttribute('aria-label'), satLabel(examId), examId);
        assert.equal(await input.locator('xpath=..').locator('span').innerText(), '土曜準会場', examId);
        printSat++;
      }
    }
    assert.equal(printSat, satExams.length);

    // Fixed practice-exam PDFs (print.js) and grammar guides (manifest) use the PDF header label.
    const printJs = await (await page.request.get(`${base}/print.js`)).text();
    const fixed = [...printJs.matchAll(/'([\w-]+)\/(\d{4}-\d-sat)': \{\s*label: '([^']+)'/g)];
    assert.ok(fixed.length >= 31, `${fixed.length} fixed Saturday PDFs`);
    for (const [, grade, examId, label] of fixed) {
      assert.ok(label.endsWith(` ${satLabel(examId)}`), `${grade}/${examId} fixed PDF: ${label}`);
    }
    const manifest = await (await page.request.get(`${base}/output/pdf/grammar_guides.json`)).json();
    const guides = Object.entries(manifest).filter(([key]) => key.endsWith('-sat'));
    assert.ok(guides.length >= 31, `${guides.length} Saturday grammar guides`);
    for (const [key, guide] of guides) {
      assert.ok(guide.label.endsWith(` ${satLabel(key.split('/')[1])}`), `${key} grammar guide: ${guide.label}`);
    }
    assert.equal(printJs.includes('（準会場）'), false);
    assert.equal(JSON.stringify(manifest).includes('（準会場）'), false);
    console.log('PRINT_OK', printSat, 'fixed PDFs', fixed.length, 'grammar guides', guides.length);

    assert.deepEqual(errors,[]);
    console.log('UI OK: （土曜準会場） on cards, exam headers, print chips, fixed PDFs and grammar guides');
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
