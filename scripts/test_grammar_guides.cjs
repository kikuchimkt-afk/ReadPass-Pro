/* Headless, isolated checks for the teacher grammar-guide buttons on print.html. */
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://127.0.0.1:8085';
const out = path.resolve(__dirname, '../tmp/qa-grammar-guides');
fs.mkdirSync(out, {recursive:true});

(async () => {
  const browser = await chromium.launch({channel:'chrome', headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1365,height:1000}, acceptDownloads:true});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.setDefaultTimeout(15000);

    // Every manifest entry must point to a real PDF with the advertised page count.
    const manifest = await (await page.request.get(`${base}/output/pdf/grammar_guides.json`)).json();
    const entries = Object.entries(manifest);
    assert.ok(entries.length >= 120, `manifest has ${entries.length} exams`);
    for (const [key, guide] of entries) {
      const response = await page.request.get(`${base}/${guide.path}`);
      assert.equal(response.status(), 200, key);
      const body = await response.body();
      assert.equal(body.subarray(0, 5).toString(), '%PDF-', key);
      const pages = (body.toString('latin1').match(/\/Type \/Page[^s]/g) || []).length;
      assert.equal(pages, guide.pages, `${key}: ${pages} pages`);
      assert.ok(guide.pages >= guide.focusPoints, key);
    }
    console.log('MANIFEST_OK', entries.length);

    await page.goto(`${base}/print.html`);
    assert.equal(await page.locator('#teacherMaterials').isVisible(), false);
    await page.locator('.grade-chip').filter({hasText:'A2（準2級相当）'}).click();
    assert.equal(await page.locator('#teacherMaterials').isVisible(), false);
    await page.locator('#examCheckboxes input[value="2025-1-sat"]').check();
    await page.locator('#examCheckboxes input[value="2025-1"]').check();
    const rows = page.locator('.teacher-material-row');
    assert.equal(await rows.count(), 2);
    const satRow = page.locator('.teacher-material-row[data-exam="2025-1-sat"]');
    assert.match(await satRow.innerText(), /文法解説プリント（講師用）/);
    assert.match(await satRow.innerText(), /2025年度 第1回（準会場） ／ A4縦5枚（1枚に1つの文法事項）/);

    // 閲覧 opens the PDF in a new tab; DL saves it under the readable file name.
    const view = satRow.getByRole('link', {name:/閲覧/});
    assert.equal(await view.getAttribute('target'), '_blank');
    const [popup] = await Promise.all([page.waitForEvent('popup'), view.click()]);
    assert.match(popup.url(), /GradePre2_2025-1-sat_Grammar_Guide_v1\.pdf/);
    await popup.close();
    const [download] = await Promise.all([page.waitForEvent('download'), satRow.getByRole('link', {name:/ダウンロード/}).click()]);
    assert.equal(download.suggestedFilename(), 'ReadPass_EIKEN_GradePre2_2025-1-sat_Grammar_Guide_v1.pdf');
    const saved = path.join(out, download.suggestedFilename());
    await download.saveAs(saved);
    assert.equal(fs.readFileSync(saved).subarray(0, 5).toString(), '%PDF-');
    await page.locator('#teacherMaterials').screenshot({path:path.join(out,'teacher-materials.png')});

    // A focus point split over two pages is described honestly.
    await page.locator('.grade-chip').filter({hasText:'5級'}).click();
    await page.locator('#examCheckboxes input[value="2026-1"]').first().check();
    assert.match(await page.locator('.teacher-material-row').first().innerText(), /A4縦4枚（文法事項3つ）/);

    // Unchecking every exam hides the panel again.
    await page.locator('#examCheckboxes input[value="2026-1"]').first().uncheck();
    assert.equal(await page.locator('#teacherMaterials').isVisible(), false);

    await page.locator('.grade-chip').filter({hasText:'A2（準2級相当）'}).click();
    await page.locator('#examCheckboxes input[value="2025-1-sat"]').check();
    for (const width of [320,390]) {
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`horizontal scroll at ${width}px`);
    }
    await page.locator('#teacherMaterials').screenshot({path:path.join(out,'teacher-materials-mobile.png')});
    assert.deepEqual(errors,[]);
    console.log('UI OK: teacher materials panel, 閲覧 popup, DL file name, split description, mobile');
    console.log('QA screenshots:',out);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
