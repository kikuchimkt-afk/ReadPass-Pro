/* ===== ReadPass Pro ===== */
(function () {
  'use strict';

  const GRADE_MAP = {
    'pre-grade1': { name: 'CEFR B2（準1級相当）', path: 'pre-grade1' },
    grade2: { name: 'CEFR B1（2級相当）', path: 'grade2' },
    'grade-pre2plus': { name: 'CEFR A2（準2級プラス相当）', path: 'grade-pre2plus' },
    'grade-pre2': { name: 'CEFR A2（準2級相当）', path: 'grade-pre2' },
    grade3: { name: 'CEFR A1（3級相当）', path: 'grade3' },
    grade4: { name: 'CEFR A1（4級相当）', path: 'grade4' },
    grade5: { name: 'CEFR Pre-A1（5級相当）', path: 'grade5' }
  };
  let currentGradeId = null;
  let currentExamId = null;
  let DATA = null;
  let vocabState = { idx: 0, score: 0, answered: false, items: [] };
  let examAnswers = {};
  let settings = { projector: false, showAnswers: false, showTranslation: false, simpleMode: false, practiceMode: false };
  let timerState = { seconds: 300, remaining: 300, running: false, interval: null };
  let projState = { part1: 0 };
  let hlState = { active: false, focusActive: {} };

  const APP = {};
  window.APP = APP;

  // ===== INIT =====
  async function init() {
    const params = new URLSearchParams(window.location.search);
    // パラメータなしでアクセスされた場合はトップページへリダイレクト
    if (!params.get('grade') && !params.get('data')) { window.location.href = 'top.html'; return; }
    const gradeId = params.get('grade') || 'grade2';
    const examId = params.get('exam') || '2025-3';
    const grade = GRADE_MAP[gradeId];
    if (!grade) { window.location.href = 'top.html'; return; }
    currentGradeId = gradeId;
    currentExamId = examId;

    // Update header label — handles sub-venue IDs like '2025-3-sat'
    const label = document.getElementById('examLabel');
    if (label) {
      const m = examId.match(/^(\d{4})-(\d+)(?:-(.+))?$/);
      if (m) {
        const suffix = m[3] === 'sat' ? '（準会場）' : (m[3] ? `(${m[3]})` : '');
        label.textContent = `${grade.name} · ${m[1]}年度 第${m[2]}回${suffix}`;
      } else {
        label.textContent = `${grade.name} · ${examId}`;
      }
    }

    setupTabs();
    await loadExam(gradeId, examId);

    // QRロックモード: ?nav=1 がない場合（QRコードからの直接アクセス）
    // ホームリンクのみ非表示にする
    if (!params.get('nav')) {
      applyLockedMode();
    }
  }

  function applyLockedMode() {
    // ホームリンク（🏠アイコン）を非表示
    const homeLink = document.querySelector('.home-link');
    if (homeLink) homeLink.style.display = 'none';
  }

  async function loadExam(gradeId, examId) {
    const grade = GRADE_MAP[gradeId];
    try { const r = await fetch(`data/${grade.path}/${examId}/data.json`); DATA = await r.json(); } catch (e) { return; }
    resetAll(); buildDynamicSections(); renderVocab(); renderLessonPlan();
    // Show simple mode button if data has grammarSimple
    const hasSimple = DATA.sections.some(s => (s.questions || []).some(q => q.grammarSimple) || (s.passages || []).some(p => p.questions.some(q => q.grammarSimple)));
    const btnSM = document.getElementById('btnSimpleMode');
    if (btnSM) btnSM.style.display = hasSimple ? '' : 'none';
  }

  // ===== QUESTION AUDIO PLAYBACK =====
  let _qAudioEl = null;
  let _qAudioBtn = null;
  APP.playQuestionAudio = function(btn, audioPath) {
    const grade = GRADE_MAP[currentGradeId];
    if (!grade) return;
    const src = `data/${grade.path}/${currentExamId}/${audioPath}`;
    // If same button is playing, stop it
    if (_qAudioEl && _qAudioBtn === btn && !_qAudioEl.paused) {
      _qAudioEl.pause();
      _qAudioEl.currentTime = 0;
      btn.classList.remove('playing');
      _qAudioEl = null;
      _qAudioBtn = null;
      return;
    }
    // Stop any previous
    if (_qAudioEl) {
      _qAudioEl.pause();
      if (_qAudioBtn) _qAudioBtn.classList.remove('playing');
    }
    _qAudioEl = new Audio(src);
    _qAudioBtn = btn;
    btn.classList.add('playing');
    _qAudioEl.play();
    _qAudioEl.onended = () => {
      btn.classList.remove('playing');
      _qAudioEl = null;
      _qAudioBtn = null;
    };
  };

  // ===== DYNAMIC SECTIONS (supports any number of sections) =====
  const _SECTION_ICONS = { vocabulary: 'edit_note', 'passage-fill': 'article', 'reading-comprehension': 'library_books', 'sentence-order': 'reorder' };

  function buildDynamicSections() {
    const tabNav = document.getElementById('tabNav');
    const lessonBtn = tabNav.querySelector('[data-tab="lesson"]');
    tabNav.querySelectorAll('.tab-btn[data-tab^="part"]').forEach(b => b.remove());
    const dynContainer = document.getElementById('dynamicSections');
    dynContainer.innerHTML = '';

    DATA.sections.forEach((sec, idx) => {
      const partId = 'part' + (idx + 1);
      const icon = _SECTION_ICONS[sec.type] || 'description';
      const name = sec.name || ('大問' + (idx + 1));
      const btn = document.createElement('button');
      btn.className = 'tab-btn';
      btn.dataset.tab = partId;
      btn.innerHTML = `<span class="material-symbols-rounded">${icon}</span><span class="tab-label">${name}</span>`;
      tabNav.insertBefore(btn, lessonBtn);

      const pane = document.createElement('section');
      pane.id = 'tab-' + partId;
      pane.className = 'tab-pane';
      let progressHtml = '';
      if (sec.type === 'vocabulary' || sec.type === 'sentence-order') {
        const qc = (sec.questions || []).length;
        progressHtml = `<div class="exam-progress"><div class="progress-bar"><div class="progress-fill" id="${partId}Progress"></div></div><span class="progress-text" id="${partId}ProgressText">0 / ${qc}</span></div>`;
        progressHtml += `<div class="projector-nav" id="${partId}ProjNav" style="display:none"><button class="btn btn-secondary" onclick="window.APP.projPrev('${partId}')"><span class="material-symbols-rounded">arrow_back</span> 前</button><span class="proj-counter" id="${partId}ProjCounter">1 / ${qc}</span><button class="btn btn-primary" onclick="window.APP.projNext('${partId}')">次 <span class="material-symbols-rounded">arrow_forward</span></button></div>`;
      }
      pane.innerHTML = `<div class="section-header"><h2>${sec.name}${sec.nameEn ? ' — ' + sec.nameEn : ''}</h2><p class="section-desc" id="${partId}Instruction"></p></div>${progressHtml}<div id="${partId}Area" class="exam-area"></div><div class="exam-controls"><button id="${partId}Submit" class="btn btn-primary"><span class="material-symbols-rounded">check</span> 採点する</button></div><div id="${partId}Results" class="results-area" style="display:none"></div>`;
      dynContainer.appendChild(pane);

      if (sec.type === 'vocabulary') renderVocabSection(sec, partId);
      else if (sec.type === 'sentence-order') renderSentenceOrderSection(sec, partId);
      else if (sec.type === 'passage-fill') renderPassageSection(sec, partId);
      else if (sec.type === 'reading-comprehension') renderReadingSection(sec, partId);
    });
    // Re-apply simple mode if active
    if (settings.simpleMode) applySimpleMode();
    setupTabs();
    // Re-apply practice mode: hide submit buttons if active
    if (settings.practiceMode) {
      document.querySelectorAll('.exam-controls .btn-primary').forEach(btn => {
        btn.style.display = 'none';
      });
    }
  }

  function getGrammar(q) { return settings.simpleMode && q.grammarSimple ? q.grammarSimple : (q.grammar || ''); }
  function getAnalysis(q) { return settings.simpleMode && q.choiceAnalysisSimple ? q.choiceAnalysisSimple : (q.choiceAnalysis || []); }

  function renderVocabSection(sec, partId) {
    document.getElementById(partId + 'Instruction').textContent = sec.instruction;
    const area = document.getElementById(partId + 'Area');
    area.innerHTML = sec.questions.map(q => {
      const txt = q.text.replace(/\(　\)/g, '<span class="blank">(　)</span>');
      const transHtml = q.translation ? `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${q.translation}</div>` : '';
      const gramHtml = q.grammar ? `<div class="grammar-note${settings.showAnswers ? '' : ' hidden'}">📝 ${getGrammar(q)}</div>` : '';
      const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${getAnalysis(q).map((a, i) => `<div class="choice-analysis-item ${i + 1 === q.answer ? 'correct-item' : 'wrong-item'}">${i + 1}. ${a}</div>`).join('')}</div>` : '';
      const audioBtn = q.questionAudio ? `<button class="q-audio-btn" onclick="window.APP.playQuestionAudio(this, '${q.questionAudio}')" title="問題を聞く"><span class="material-symbols-rounded" style="font-size:18px">volume_up</span><span>聞いてみよう</span></button>` : '';
      return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">問題 (${q.number}) ${audioBtn}<span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div><div class="exam-q-text">${txt}</div>${transHtml}${gramHtml}<div class="exam-choices">${q.choices.map((c, i) => { const ct = (q.choiceTranslations || [])[i]; return `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}${ct ? `<span class="choice-translation${settings.showTranslation ? '' : ' hidden'}">${ct}</span>` : ''}</span></button>`; }).join('')}</div>${analysisHtml}</div>`;
    }).join('');
    // Progress
    const updateProg = () => {
      const ans = area.querySelectorAll('.exam-choice-btn.selected').length;
      const tot = sec.questions.length;
      const pe = document.getElementById(partId + 'Progress');
      const pt = document.getElementById(partId + 'ProgressText');
      if (pe) pe.style.width = (ans / tot * 100) + '%';
      if (pt) pt.textContent = `${ans} / ${tot}`;
    };
    updateProg();
    document.getElementById(partId + 'Submit').onclick = () => gradePart(partId, sec.questions);
    document.getElementById(partId + 'Submit').style.display = '';
    document.getElementById(partId + 'Results').style.display = 'none';
  }

  // ===== SENTENCE ORDER (語順整序) =====
  function renderSentenceOrderSection(sec, partId) {
    document.getElementById(partId + 'Instruction').textContent = sec.instruction;
    const area = document.getElementById(partId + 'Area');
    area.innerHTML = sec.questions.map(q => {
      const words = q.words || [];
      const slots = q.correctOrder ? q.correctOrder.length : 5;
      const ansSlots = q.answerSlots || [2, 4];
      const prefix = q.framePrefix || '';
      const suffix = q.frameSuffix || '';
      const gramHtml = q.grammar ? `<div class="grammar-note${settings.showAnswers ? '' : ' hidden'}">📝 ${getGrammar(q)}</div>` : '';
      const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${getAnalysis(q).map((a, i) => `<div class="choice-analysis-item ${i + 1 === q.answer ? 'correct-item' : 'wrong-item'}">${i + 1}. ${a}</div>`).join('')}</div>` : '';
      // Scratch pad: word buttons + slots
      let slotsHtml = '';
      for (let s = 0; s < slots; s++) {
        const isAns = ansSlots.includes(s + 1);
        slotsHtml += `<span class="so-slot${isAns ? ' so-slot-answer' : ''}" data-qso="${q.number}" data-slot="${s}">${isAns ? (s + 1) + '番目' : ''}</span>`;
      }
      const wordBtnsHtml = words.map((w, i) => `<button class="so-word-btn" data-qso="${q.number}" data-widx="${i}" onclick="window._soClickWord(${q.number},${i})">${String.fromCharCode(0x2460 + i)}${w}</button>`).join('');
      const soAudioBtn = q.questionAudio ? `<button class="q-audio-btn" onclick="window.APP.playQuestionAudio(this, '${q.questionAudio}')" title="問題を聞く"><span class="material-symbols-rounded" style="font-size:18px">volume_up</span><span>聞いてみよう</span></button>` : '';
      return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">問題 (${q.number}) ${soAudioBtn}<span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div><div class="exam-q-text so-japanese">${q.text}</div><div class="so-wordlist">（${words.map((w,i) => String.fromCharCode(0x2460+i) + ' ' + w).join('　')}）</div><div class="so-frame"><span class="so-prefix">${prefix}</span>${slotsHtml}<span class="so-suffix">${suffix}</span></div><div class="so-scratch"><div class="so-scratch-label">▼ 単語をタップして並べよう <button class="so-reset-btn" onclick="window._soReset(${q.number})">リセット</button></div><div class="so-word-btns" data-qso="${q.number}">${wordBtnsHtml}</div></div>${gramHtml}<div class="exam-choices">${q.choices.map((c, i) => `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}</span></button>`).join('')}</div>${analysisHtml}</div>`;
    }).join('');
    // Scratch pad logic
    const soState = {};
    window._soClickWord = function(qn, widx) {
      if (!soState[qn]) soState[qn] = { placed: [], wordUsed: [] };
      const st = soState[qn];
      const q = sec.questions.find(x => x.number === qn);
      if (!q) return;
      if (st.wordUsed[widx]) return;
      const slots = q.correctOrder ? q.correctOrder.length : 5;
      if (st.placed.length >= slots) return;
      st.wordUsed[widx] = true;
      st.placed.push(widx);
      // Update slot display
      const slotEls = area.querySelectorAll(`.so-slot[data-qso="${qn}"]`);
      slotEls[st.placed.length - 1].textContent = q.words[widx];
      slotEls[st.placed.length - 1].classList.add('so-slot-filled');
      // Dim word button
      const btn = area.querySelector(`.so-word-btn[data-qso="${qn}"][data-widx="${widx}"]`);
      if (btn) btn.classList.add('so-word-used');
    };
    window._soReset = function(qn) {
      soState[qn] = { placed: [], wordUsed: [] };
      const q = sec.questions.find(x => x.number === qn);
      if (!q) return;
      const ansSlots = q.answerSlots || [2, 4];
      area.querySelectorAll(`.so-slot[data-qso="${qn}"]`).forEach((el, i) => {
        const isAns = ansSlots.includes(i + 1);
        el.textContent = isAns ? (i + 1) + '番目' : '';
        el.classList.remove('so-slot-filled');
      });
      area.querySelectorAll(`.so-word-btn[data-qso="${qn}"]`).forEach(b => b.classList.remove('so-word-used'));
    };
    // Progress
    const updateProg = () => {
      const ans = area.querySelectorAll('.exam-choice-btn.selected').length;
      const tot = sec.questions.length;
      const pe = document.getElementById(partId + 'Progress');
      const pt = document.getElementById(partId + 'ProgressText');
      if (pe) pe.style.width = (ans / tot * 100) + '%';
      if (pt) pt.textContent = `${ans} / ${tot}`;
    };
    updateProg();
    document.getElementById(partId + 'Submit').onclick = () => gradePart(partId, sec.questions);
    document.getElementById(partId + 'Submit').style.display = '';
    document.getElementById(partId + 'Results').style.display = 'none';
  }

  function renderPassageSection(sec, partId) {
    document.getElementById(partId + 'Instruction').textContent = sec.instruction;
    const area = document.getElementById(partId + 'Area');
    area.innerHTML = sec.passages.map(p => {
      let html = `<div class="passage-block"><span class="passage-label">${p.label}</span><div class="passage-title">${p.title}</div>`;
      p.paragraphs.forEach((para, pi) => {
        let pHtml = wrapSentences(para, p);
        p.questions.forEach(q => { pHtml = pHtml.replace(new RegExp(`\\(\\s*${q.number}\\s*\\)`), `<span class="blank-inline">( ${q.number} )</span>`); });
        html += `<p class="passage-text">${pHtml}</p>`;
        if (p.translations && p.translations[pi]) html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${p.translations[pi]}</div>`;
      });
      html += '</div>';
      html += p.questions.map(q => {
        if (q.sourceEvidence) _evidenceMap[q.number] = q.sourceEvidence;
        const hasEv = !!q.sourceEvidence;
        const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${q.choiceAnalysis.map((a, i) => { const isCor = i + 1 === q.answer; return `<div class="choice-analysis-item ${isCor ? 'correct-item' : 'wrong-item'}"${isCor && hasEv ? ` data-evq="${q.number}" style="cursor:pointer"` : ''}>${i + 1}. ${a}</div>`; }).join('')}</div>` : '';
        const ct2 = q.choiceTranslations || [];
        return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">問題 (${q.number}) <span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div><div class="exam-choices">${q.choices.map((c, i) => `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}${ct2[i] ? `<span class="choice-translation${settings.showTranslation ? '' : ' hidden'}">${ct2[i]}</span>` : ''}</span></button>`).join('')}</div>${analysisHtml}</div>`;
      }).join('');
      return html;
    }).join('');
    document.getElementById(partId + 'Submit').onclick = () => { const qs = sec.passages.flatMap(p => p.questions); gradePart(partId, qs); };
    document.getElementById(partId + 'Submit').style.display = '';
    document.getElementById(partId + 'Results').style.display = 'none';
    setupSentencePopups(area);
    setupEvidenceHighlight(area);
  }

  function renderReadingSection(sec, partId) {
    document.getElementById(partId + 'Instruction').textContent = sec.instruction;
    const area = document.getElementById(partId + 'Area');
    area.innerHTML = sec.passages.map(p => {
      let html = `<div class="passage-block">`;
      html += `<span class="passage-label">${p.label}</span>`;
      html += `<div class="passage-title">${p.title}</div>`;

      // --- Notice format (3A: 掲示物) ---
      if (p.format === 'notice') {
        html += `<div class="notice-frame">`;
        p.paragraphs.forEach((para, pi) => {
          if (pi === 0) {
            // Title line - centered and bold
            html += `<div class="notice-heading">${para}</div>`;
          } else if (para.includes('When:') || para.includes('Where:') || para.includes('Date:')) {
            // Info lines with bold labels
            html += `<div class="notice-info">${para.replace(/\n/g, '<br>').replace(/(When:|Where:|Date:|Time:|Place:)/g, '<strong>$1</strong>')}</div>`;
          } else {
            const pHtml = wrapSentences(para, p);
            html += `<p class="passage-text">${pHtml}</p>`;
          }
          if (p.translations && p.translations[pi]) html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${p.translations[pi].replace(/\n/g, '<br>')}</div>`;
        });
        html += `</div>`;

      // --- Multi-email format (3B: メール) ---
      } else if (p.format === 'multi-email' && p.emails) {
        p.emails.forEach((email, ei) => {
          html += `<div class="email-block">`;
          html += `<div class="email-meta">`;
          html += `<div><strong>From:</strong> ${email.meta.from}</div>`;
          html += `<div><strong>To:</strong> ${email.meta.to}</div>`;
          html += `<div><strong>Date:</strong> ${email.meta.date}</div>`;
          html += `<div><strong>Subject:</strong> ${email.meta.subject}</div>`;
          html += `</div>`;
          const bodyHtml = wrapSentences(email.body, p);
          html += `<div class="email-body">${bodyHtml.replace(/\n/g, '<br>')}</div>`;
          if (email.translation) html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${email.translation.replace(/\n/g, '<br>')}</div>`;
          html += `</div>`;
        });

      // --- Standard format (single email, long passage) ---
      } else {
        let metaHtml = '';
        if (p.format === 'email' && p.meta) {
          metaHtml = `<div class="email-meta"><div><strong>From:</strong> ${p.meta.from}</div><div><strong>To:</strong> ${p.meta.to}</div><div><strong>Date:</strong> ${p.meta.date}</div><div><strong>Subject:</strong> ${p.meta.subject}</div></div>`;
        }
        html += metaHtml;
        p.paragraphs.forEach((para, pi) => {
          const pHtml = wrapSentences(para, p);
          html += `<p class="passage-text">${pHtml}</p>`;
          if (p.translations && p.translations[pi]) html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${p.translations[pi]}</div>`;
        });
      }

      html += '</div>';
      // Questions
      html += p.questions.map(q => {
        if (q.sourceEvidence) _evidenceMap[q.number] = q.sourceEvidence;
        const hasEv = !!q.sourceEvidence;
        const analysis = getAnalysis(q);
        const gramHtml = q.grammar ? `<div class="grammar-note${settings.showAnswers ? '' : ' hidden'}">\ud83d\udcdd ${getGrammar(q)}</div>` : '';
        const analysisHtml = (q.choiceAnalysis || q.choiceAnalysisSimple) ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${analysis.map((a, i) => { const isCor = i + 1 === q.answer; return `<div class="choice-analysis-item ${isCor ? 'correct-item' : 'wrong-item'}"${isCor && hasEv ? ` data-evq="${q.number}" style="cursor:pointer"` : ''}>${i + 1}. ${a}</div>`; }).join('')}</div>` : '';
        const qTrans = q.questionTranslation ? `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${q.questionTranslation}</div>` : '';
        const ct3 = q.choiceTranslations || [];
        return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">\u554f\u984c (${q.number}) <span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">\u6b63\u89e3: ${q.answer}</span></div><div class="exam-q-text">${q.question}</div>${qTrans}${gramHtml}<div class="exam-choices">${q.choices.map((c, i) => `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}${ct3[i] ? `<span class="choice-translation${settings.showTranslation ? '' : ' hidden'}">${ct3[i]}</span>` : ''}</span></button>`).join('')}</div>${analysisHtml}</div>`;
      }).join('');
      return html;
    }).join('');
    document.getElementById(partId + 'Submit').onclick = () => { const qs = sec.passages.flatMap(p => p.questions); gradePart(partId, qs); };
    document.getElementById(partId + 'Submit').style.display = '';
    document.getElementById(partId + 'Results').style.display = 'none';
    setupSentencePopups(area);
    setupEvidenceHighlight(area);
  }


  function resetAll() {
    vocabState = { idx: 0, score: 0, answered: false, items: DATA?.vocabulary ? shuffle([...DATA.vocabulary]) : [] };
    examAnswers = {};
    projState = { part1: 0 };
    _sentTrans = [];
    settings.showAnswers = false;
    settings.showTranslation = false;
    settings.projector = false;
    // Sync toolbar buttons
    const btnAns = document.getElementById('btnAnswers');
    if (btnAns) { btnAns.classList.remove('active'); const ic = btnAns.querySelector('.material-symbols-rounded'); if (ic) ic.textContent = 'visibility_off'; const sp = btnAns.querySelector('span:last-child'); if (sp) sp.textContent = '正解非表示'; }
    const btnTr = document.getElementById('btnTranslation');
    if (btnTr) { btnTr.classList.remove('active'); }
    const btnProj = document.getElementById('btnProjector');
    if (btnProj) { btnProj.classList.remove('active'); }
    ['part1Results', 'part2Results', 'part3Results'].forEach(id => { const el = document.getElementById(id); if (el) el.style.display = 'none'; });
  }

  // ===== TABS =====
  function setupTabs() {
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
      });
    });
  }

  // ===== INSTRUCTOR TOOLS =====
  APP.toggleProjector = function () {
    settings.projector = !settings.projector;
    document.body.classList.toggle('projector-mode', settings.projector);
    const btn = document.getElementById('btnProjector');
    btn.classList.toggle('active', settings.projector);
    btn.querySelector('span:last-child').textContent = settings.projector ? '画面縮小' : '画面拡大';
    // Show/hide projector nav
    const nav1 = document.getElementById('part1ProjNav');
    nav1.style.display = settings.projector ? 'flex' : 'none';
    if (settings.projector) applyProjectorView('part1');
    else document.querySelectorAll('.exam-question.proj-hidden').forEach(el => el.classList.remove('proj-hidden'));
  };

  APP.toggleAnswers = function () {
    settings.showAnswers = !settings.showAnswers;
    const btn = document.getElementById('btnAnswers');
    btn.classList.toggle('active', settings.showAnswers);
    const icon = btn.querySelector('.material-symbols-rounded');
    icon.textContent = settings.showAnswers ? 'visibility' : 'visibility_off';
    btn.querySelector('span:last-child').textContent = settings.showAnswers ? '正解表示中' : '正解非表示';
    // Show/hide answer indicators
    document.querySelectorAll('.answer-indicator').forEach(el => {
      el.classList.toggle('hidden', !settings.showAnswers);
    });
    document.querySelectorAll('.choice-analysis').forEach(el => {
      el.classList.toggle('hidden', !settings.showAnswers);
    });
    document.querySelectorAll('.grammar-note').forEach(el => {
      el.classList.toggle('hidden', !settings.showAnswers);
    });
  };

  // ===== SIMPLE MODE (dual explanation toggle) =====
  APP.toggleSimpleMode = function () {
    settings.simpleMode = !settings.simpleMode;
    const btn = document.getElementById('btnSimpleMode');
    btn.classList.toggle('active', settings.simpleMode);
    const icon = btn.querySelector('.material-symbols-rounded');
    icon.textContent = settings.simpleMode ? 'child_care' : 'child_care';
    btn.querySelector('span:last-child').textContent = settings.simpleMode ? 'やさしいON' : 'やさしい説明';
    applySimpleMode();
  };

  function applySimpleMode() {
    // Re-render grammar notes and choice analysis with current mode
    document.querySelectorAll('.grammar-note').forEach(el => {
      const qEl = el.closest('.exam-question');
      if (!qEl) return;
      const qNum = parseInt((qEl.id || '').replace('q', ''));
      const q = findQuestion(qNum);
      if (q) el.innerHTML = '📝 ' + getGrammar(q);
    });
    document.querySelectorAll('.choice-analysis').forEach(el => {
      const qEl = el.closest('.exam-question');
      if (!qEl) return;
      const qNum = parseInt((qEl.id || '').replace('q', ''));
      const q = findQuestion(qNum);
      if (q) {
        const analysis = getAnalysis(q);
        el.innerHTML = analysis.map((a, i) => {
          const isCor = i + 1 === q.answer;
          return `<div class="choice-analysis-item ${isCor ? 'correct-item' : 'wrong-item'}">${i + 1}. ${a}</div>`;
        }).join('');
      }
    });
    // Re-render lesson plan with current mode
    renderLessonPlan();
  }

  function findQuestion(qNum) {
    if (!DATA || !DATA.sections) return null;
    for (const sec of DATA.sections) {
      if (sec.questions) {
        const found = sec.questions.find(q => q.number === qNum);
        if (found) return found;
      }
      if (sec.passages) {
        for (const p of sec.passages) {
          const found = (p.questions || []).find(q => q.number === qNum);
          if (found) return found;
        }
      }
    }
    return null;
  }

  APP.toggleTranslation = function () {
    settings.showTranslation = !settings.showTranslation;
    const btn = document.getElementById('btnTranslation');
    btn.classList.toggle('active', settings.showTranslation);
    btn.querySelector('span:last-child').textContent = settings.showTranslation ? '和訳ON' : '和訳OFF';
    document.querySelectorAll('.translation-block').forEach(el => {
      el.classList.toggle('hidden', !settings.showTranslation);
    });
    document.querySelectorAll('.choice-translation').forEach(el => {
      el.classList.toggle('hidden', !settings.showTranslation);
    });
  };

  // ===== MODE TOGGLE (演習 / テスト) =====
  APP.toggleMode = function () {
    const toggle = document.getElementById('modeToggle');
    settings.practiceMode = toggle.checked;
    const labelTest = document.getElementById('modeLabelTest');
    const labelPractice = document.getElementById('modeLabelPractice');
    if (settings.practiceMode) {
      labelTest.classList.remove('active');
      labelPractice.classList.add('active');
    } else {
      labelTest.classList.add('active');
      labelPractice.classList.remove('active');
    }
    // Toggle submit buttons visibility
    document.querySelectorAll('.exam-controls .btn-primary').forEach(btn => {
      // Only hide submit buttons for sections that haven't been graded yet
      const partId = btn.id.replace('Submit', '');
      const resultsEl = document.getElementById(partId + 'Results');
      if (resultsEl && resultsEl.style.display !== 'none' && resultsEl.style.display !== '') return;
      btn.style.display = settings.practiceMode ? 'none' : '';
    });
  };

  APP.openVocabCards = function () {
    if (!currentGradeId || !currentExamId) return;
    const grade = GRADE_MAP[currentGradeId];
    if (!grade) return;
    const dataUrl = `data/${grade.path}/${currentExamId}/data.json`;
    window.open(`vocab-cards.html?data=${encodeURIComponent(dataUrl)}`, '_blank', 'width=520,height=760');
  };

  APP.toggleTheme = function () {
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    const newTheme = isLight ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('eikenTheme', newTheme);
    const btn = document.getElementById('btnTheme');
    if (btn) {
      btn.querySelector('.material-symbols-rounded').textContent = newTheme === 'light' ? 'dark_mode' : 'light_mode';
      btn.querySelector('span:last-child').textContent = newTheme === 'light' ? 'ダーク' : 'ライト';
    }
  };

  // Restore saved theme
  (function () {
    const saved = localStorage.getItem('eikenTheme');
    if (saved === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
      setTimeout(() => {
        const btn = document.getElementById('btnTheme');
        if (btn) {
          btn.querySelector('.material-symbols-rounded').textContent = 'dark_mode';
          btn.querySelector('span:last-child').textContent = 'ダーク';
        }
      }, 0);
    }
  })();

  // ===== TIMER =====
  APP.toggleTimer = function () {
    const bar = document.getElementById('timerBar');
    const btn = document.getElementById('btnTimer');
    if (bar.style.display === 'none') { bar.style.display = 'block'; btn.classList.add('active'); }
    else { bar.style.display = 'none'; btn.classList.remove('active'); APP.resetTimer(); }
  };

  APP.setTimer = function (sec) {
    if (timerState.running) APP.startStopTimer();
    timerState.seconds = sec; timerState.remaining = sec;
    updateTimerDisplay();
  };

  APP.startStopTimer = function () {
    const btn = document.getElementById('timerStartBtn');
    if (timerState.running) {
      clearInterval(timerState.interval); timerState.running = false;
      btn.textContent = '▶ 開始'; btn.classList.add('primary');
    } else {
      timerState.running = true; btn.textContent = '⏸ 一時停止'; btn.classList.remove('primary');
      timerState.interval = setInterval(() => {
        timerState.remaining--;
        if (timerState.remaining <= 0) { timerState.remaining = 0; APP.startStopTimer(); }
        updateTimerDisplay();
      }, 1000);
    }
  };

  APP.resetTimer = function () {
    if (timerState.running) APP.startStopTimer();
    timerState.remaining = timerState.seconds;
    updateTimerDisplay();
  };

  function updateTimerDisplay() {
    const m = Math.floor(timerState.remaining / 60);
    const s = timerState.remaining % 60;
    document.getElementById('timerValue').textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    const pct = (timerState.remaining / timerState.seconds) * 100;
    document.getElementById('timerProgressFill').style.width = pct + '%';
    const bar = document.getElementById('timerBar');
    bar.classList.remove('warning', 'danger');
    if (timerState.remaining <= 10) bar.classList.add('danger');
    else if (timerState.remaining <= 30) bar.classList.add('warning');
  }

  // ===== PROJECTOR VIEW =====
  function applyProjectorView(part) {
    const section = DATA.sections.find(s => s.type === 'vocabulary');
    if (!section) return;
    const cards = document.querySelectorAll('#part1Area .exam-question');
    cards.forEach((c, i) => { c.classList.toggle('proj-hidden', i !== projState.part1); });
    document.getElementById('part1ProjCounter').textContent = `${projState.part1 + 1} / ${cards.length}`;
  }

  APP.projNext = function (part) {
    const cards = document.querySelectorAll('#part1Area .exam-question');
    if (projState.part1 < cards.length - 1) { projState.part1++; applyProjectorView(part); }
  };
  APP.projPrev = function (part) {
    if (projState.part1 > 0) { projState.part1--; applyProjectorView(part); }
  };

  // ===== GRAMMAR HIGHLIGHT =====
  APP.toggleHighlight = function () {
    hlState.active = !hlState.active;
    const btn = document.getElementById('btnHighlight');
    btn.classList.toggle('active', hlState.active);
    btn.querySelector('span:last-child').textContent = hlState.active ? 'マーカーON' : '文法マーカー';
    const legend = document.getElementById('highlightLegend');
    if (hlState.active) {
      buildHighlightLegend();
      legend.classList.add('show');
      // activate all focus points by default
      const fps = DATA.lessonPlan?.focusPoints || [];
      fps.forEach(fp => { hlState.focusActive[fp.id] = true; });
      applyHighlights();
    } else {
      legend.classList.remove('show');
      removeHighlights();
      hlState.focusActive = {};
    }
  };

  function buildHighlightLegend() {
    const legend = document.getElementById('highlightLegend');
    const fps = DATA.lessonPlan?.focusPoints || [];
    legend.innerHTML = `<span style="font-size:0.72rem;color:var(--text-secondary);font-weight:600">凡例：</span>` +
      fps.map((fp, i) => {
        const active = hlState.focusActive[fp.id] !== false;
        return `<button class="hl-legend-item ${active ? 'active' : ''}" style="${active ? 'background:' + fp.highlightColor + '30;border-color:' + fp.highlightColor : ''}" data-fpid="${fp.id}" onclick="window.APP.toggleFocusHL('${fp.id}')">
          <span class="hl-swatch" style="background:${fp.highlightColor}"></span>
          ${fp.highlightLabel || fp.title}
        </button>`;
      }).join('');
  }

  APP.toggleFocusHL = function (fpId) {
    hlState.focusActive[fpId] = !hlState.focusActive[fpId];
    buildHighlightLegend();
    removeHighlights();
    applyHighlights();
  };

  function applyHighlights() {
    const fps = DATA.lessonPlan?.focusPoints || [];
    const activeFps = fps.filter(fp => hlState.focusActive[fp.id] && fp.highlightPatterns);
    if (!activeFps.length) return;

    // Build all patterns sorted longest first
    const allPatterns = [];
    activeFps.forEach(fp => {
      fp.highlightPatterns.forEach(pat => {
        allPatterns.push({ pattern: pat, color: fp.highlightColor, label: fp.highlightLabel || fp.title });
      });
    });
    allPatterns.sort((a, b) => b.pattern.length - a.pattern.length);

    // Apply to passage text in Part 2 and Part 3
    document.querySelectorAll('#part2Area .passage-text, #part3Area .passage-text').forEach(el => {
      // Store original if not yet stored
      if (!el.dataset.originalHtml) el.dataset.originalHtml = el.innerHTML;
      let html = el.dataset.originalHtml;

      allPatterns.forEach(({ pattern, color }) => {
        const escaped = pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const re = new RegExp(`(${escaped})`, 'gi');
        html = html.replace(re, `<mark class="grammar-hl" style="background:${color}40;color:#fff;border-bottom:2px solid ${color}">$1</mark>`);
      });

      el.innerHTML = html;
    });
  }

  function removeHighlights() {
    document.querySelectorAll('#part2Area .passage-text, #part3Area .passage-text').forEach(el => {
      if (el.dataset.originalHtml) el.innerHTML = el.dataset.originalHtml;
    });
  }

  // ===== VOCAB QUIZ =====
  function renderVocab() {
    const items = vocabState.items;
    if (!items.length) return;
    const area = document.getElementById('vocabQuizArea');
    const nextBtn = document.getElementById('vocabNext');
    const restartBtn = document.getElementById('vocabRestart');
    const scoreEl = document.getElementById('vocabScore');
    updateVocabProgress();
    scoreEl.innerHTML = '';
    nextBtn.style.display = 'none';
    restartBtn.style.display = 'none';

    if (vocabState.idx >= items.length) {
      area.innerHTML = '';
      scoreEl.innerHTML = `結果: <span class="score-num">${vocabState.score}</span> / ${items.length}`;
      restartBtn.style.display = 'inline-flex';
      restartBtn.onclick = () => { vocabState = { idx: 0, score: 0, answered: false, items: shuffle([...DATA.vocabulary]) }; renderVocab(); };
      return;
    }

    const item = items[vocabState.idx];
    const allOpts = shuffle([item.meaning, ...item.distractors.slice(0, 3)]);
    const levelClass = item.level === '2級' ? 'g2' : 'gp2';
    const sourceTag = item.source ? `<span class="vocab-level" style="background:rgba(251,191,36,0.2);color:#fbbf24;margin-left:4px">${item.source}</span>` : '';

    const wordAudioBtn = item.wordAudio ? `<button class="q-audio-btn vocab-audio-btn" onclick="window.APP.playQuestionAudio(this, '${item.wordAudio}')" title="発音を聞く"><span class="material-symbols-rounded" style="font-size:20px">volume_up</span></button>` : '';

    area.innerHTML = `
      <div class="vocab-card">
        <div class="vocab-word">${item.word} ${wordAudioBtn}</div>
        <div class="vocab-meta">
          <span class="vocab-pos">${item.pos}</span>
          <span class="vocab-level ${levelClass}">${item.level}</span>${sourceTag}
        </div>
        <div class="vocab-prompt">この単語の意味は？</div>
        <div class="choices-list" id="vocabChoices">
          ${allOpts.map((o, i) => `
            <button class="choice-btn" data-value="${esc(o)}" onclick="window._vocabAns('${esc(o)}','${esc(item.meaning)}')">
              <span class="choice-num">${i + 1}</span><span>${o}</span>
            </button>
          `).join('')}
        </div>
        <div id="vocabFeedback"></div>
      </div>
    `;
    vocabState.answered = false;
  }

  window._vocabAns = function (sel, correct) {
    if (vocabState.answered) return;
    vocabState.answered = true;
    const item = vocabState.items[vocabState.idx];
    const ok = sel === correct;
    if (ok) vocabState.score++;
    document.querySelectorAll('#vocabChoices .choice-btn').forEach(btn => {
      btn.classList.add('disabled');
      const v = btn.dataset.value;
      if (v === correct) btn.classList.add('correct');
      else if (v === sel && !ok) btn.classList.add('wrong');
      else btn.classList.add('faded');
    });
    document.getElementById('vocabFeedback').innerHTML = `
      <div class="vocab-result ${ok ? 'correct' : 'wrong'}">
        <div class="result-icon">${ok ? '✓ 正解！' : '✗ 不正解'}</div>
        <div><strong>${item.word}</strong> = ${item.meaning}</div>
        <div class="result-example">例: ${item.example}</div>
      </div>
    `;
    updateVocabProgress();
    const nb = document.getElementById('vocabNext');
    nb.style.display = 'inline-flex';
    nb.onclick = () => { vocabState.idx++; renderVocab(); };
  };

  function updateVocabProgress() {
    const t = vocabState.items.length;
    const d = Math.min(vocabState.idx + (vocabState.answered ? 1 : 0), t);
    document.getElementById('vocabProgress').style.width = (d / t * 100) + '%';
    document.getElementById('vocabProgressText').textContent = `${d} / ${t}`;
  }

  // ===== PART 1 =====
  function renderPart1() {
    const sec = DATA.sections.find(s => s.type === 'vocabulary');
    if (!sec) return;
    document.getElementById('part1Instruction').textContent = sec.instruction;
    const area = document.getElementById('part1Area');
    area.innerHTML = sec.questions.map(q => {
      const txt = q.text.replace(/\(　\)/g, '<span class="blank">(　)</span>');
      const transHtml = q.translation ? `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${q.translation}</div>` : '';
      const gramHtml = q.grammar ? `<div class="grammar-note${settings.showAnswers ? '' : ' hidden'}">📝 ${q.grammar}</div>` : '';
      const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${q.choiceAnalysis.map((a, i) => `<div class="choice-analysis-item ${i + 1 === q.answer ? 'correct-item' : 'wrong-item'}">${i + 1}. ${a}</div>`).join('')}</div>` : '';
      return `
        <div class="exam-question" id="q${q.number}">
          <div class="exam-q-number">問題 (${q.number}) <span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div>
          <div class="exam-q-text">${txt}</div>
          ${transHtml}
          ${gramHtml}
          <div class="exam-choices">
            ${q.choices.map((c, i) => `
              <button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})">
                <span class="choice-num">${i + 1}</span><span>${c}</span>
              </button>
            `).join('')}
          </div>
          ${analysisHtml}
        </div>
      `;
    }).join('');
    updatePart1Progress();
    document.getElementById('part1Submit').onclick = () => gradePart('part1', sec.questions);
    document.getElementById('part1Submit').style.display = '';
    document.getElementById('part1Results').style.display = 'none';
  }

  function updatePart1Progress() {
    const sec = DATA.sections.find(s => s.type === 'vocabulary');
    if (!sec) return;
    const t = sec.questions.length;
    const a = sec.questions.filter(q => examAnswers[q.number]).length;
    document.getElementById('part1Progress').style.width = (a / t * 100) + '%';
    document.getElementById('part1ProgressText').textContent = `${a} / ${t}`;
  }

  // ===== PART 2 =====
  function renderPart2() {
    const sec = DATA.sections.find(s => s.type === 'passage-fill');
    if (!sec) return;
    document.getElementById('part2Instruction').textContent = sec.instruction;
    const area = document.getElementById('part2Area');
    area.innerHTML = sec.passages.map(p => {
      let html = `<div class="passage-block"><span class="passage-label">${p.label}</span><div class="passage-title">${p.title}</div>`;
      p.paragraphs.forEach((para, pi) => {
        let pHtml = wrapSentences(para, p);
        p.questions.forEach(q => { pHtml = pHtml.replace(new RegExp(`\\(\\s*${q.number}\\s*\\)`), `<span class="blank-inline">( ${q.number} )</span>`); });
        html += `<p class="passage-text">${pHtml}</p>`;
        if (p.translations && p.translations[pi]) {
          html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${p.translations[pi]}</div>`;
        }
      });
      html += '</div>';
      html += p.questions.map(q => {
        if (q.sourceEvidence) _evidenceMap[q.number] = q.sourceEvidence;
        const hasEv = !!q.sourceEvidence;
        const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${q.choiceAnalysis.map((a, i) => { const isCor = i + 1 === q.answer; return `<div class="choice-analysis-item ${isCor ? 'correct-item' : 'wrong-item'}"${isCor && hasEv ? ` data-evq="${q.number}" style="cursor:pointer"` : ''}>${i + 1}. ${a}</div>`; }).join('')}</div>` : '';
        const ct2 = q.choiceTranslations || [];
        return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">問題 (${q.number}) <span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div><div class="exam-choices">${q.choices.map((c, i) => `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}${ct2[i] ? `<span class="choice-translation${settings.showTranslation ? '' : ' hidden'}">${ct2[i]}</span>` : ''}</span></button>`).join('')}</div>${analysisHtml}</div>`;
      }).join('');
      return html;
    }).join('');
    document.getElementById('part2Submit').onclick = () => { const qs = sec.passages.flatMap(p => p.questions); gradePart('part2', qs); };
    document.getElementById('part2Submit').style.display = '';
    document.getElementById('part2Results').style.display = 'none';
    setupSentencePopups(area);
    setupEvidenceHighlight(area);
  }

  // ===== PART 3 =====
  function renderPart3() {
    const sec = DATA.sections.find(s => s.type === 'reading-comprehension');
    if (!sec) return;
    document.getElementById('part3Instruction').textContent = sec.instruction;
    const area = document.getElementById('part3Area');
    area.innerHTML = sec.passages.map(p => {
      let metaHtml = '';
      if (p.format === 'email' && p.meta) {
        metaHtml = `<div class="email-meta"><div><strong>From:</strong> ${p.meta.from}</div><div><strong>To:</strong> ${p.meta.to}</div><div><strong>Date:</strong> ${p.meta.date}</div><div><strong>Subject:</strong> ${p.meta.subject}</div></div>`;
      }
      let html = `<div class="passage-block"><span class="passage-label">${p.label}</span><div class="passage-title">${p.title}</div>${metaHtml}`;
      p.paragraphs.forEach((para, pi) => {
        const pHtml = wrapSentences(para, p);
        html += `<p class="passage-text">${pHtml}</p>`;
        if (p.translations && p.translations[pi]) {
          html += `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${p.translations[pi]}</div>`;
        }
      });
      html += '</div>';
      html += p.questions.map(q => {
        if (q.sourceEvidence) _evidenceMap[q.number] = q.sourceEvidence;
        const hasEv = !!q.sourceEvidence;
        const analysisHtml = q.choiceAnalysis ? `<div class="choice-analysis${settings.showAnswers ? '' : ' hidden'}">${q.choiceAnalysis.map((a, i) => { const isCor = i + 1 === q.answer; return `<div class="choice-analysis-item ${isCor ? 'correct-item' : 'wrong-item'}"${isCor && hasEv ? ` data-evq="${q.number}" style="cursor:pointer"` : ''}>${i + 1}. ${a}</div>`; }).join('')}</div>` : '';
        const qTrans = q.questionTranslation ? `<div class="translation-block${settings.showTranslation ? '' : ' hidden'}">${q.questionTranslation}</div>` : '';
        const ct3 = q.choiceTranslations || [];
        return `<div class="exam-question" id="q${q.number}"><div class="exam-q-number">問題 (${q.number}) <span class="answer-indicator${settings.showAnswers ? '' : ' hidden'}" style="background:var(--success);color:#000;padding:1px 8px;border-radius:10px;font-size:0.7rem;margin-left:8px">正解: ${q.answer}</span></div><div class="exam-q-text">${q.question}</div>${qTrans}<div class="exam-choices">${q.choices.map((c, i) => `<button class="exam-choice-btn" data-q="${q.number}" data-val="${i + 1}" onclick="window._selExam(${q.number},${i + 1})"><span class="choice-num">${i + 1}</span><span>${c}${ct3[i] ? `<span class="choice-translation${settings.showTranslation ? '' : ' hidden'}">${ct3[i]}</span>` : ''}</span></button>`).join('')}</div>${analysisHtml}</div>`;
      }).join('');
      return html;
    }).join('');
    document.getElementById('part3Submit').onclick = () => { const qs = sec.passages.flatMap(p => p.questions); gradePart('part3', qs); };
    document.getElementById('part3Submit').style.display = '';
    document.getElementById('part3Results').style.display = 'none';
    setupSentencePopups(area);
    setupEvidenceHighlight(area);
  }

  // ===== EVIDENCE HIGHLIGHT =====
  const _evidenceMap = {};
  function setupEvidenceHighlight(container) {
    container.addEventListener('click', function (e) {
      const item = e.target.closest('.correct-item[data-evq]');
      if (!item) return;
      e.stopPropagation();
      // Clear any existing evidence highlights
      clearEvidenceHighlights();
      // Toggle: if already active, just clear
      if (item.classList.contains('evidence-active')) {
        item.classList.remove('evidence-active');
        return;
      }
      // Remove active from all
      document.querySelectorAll('.evidence-active').forEach(el => el.classList.remove('evidence-active'));
      item.classList.add('evidence-active');
      // Parse evidence patterns from global map
      const qNum = parseInt(item.dataset.evq);
      const patterns = _evidenceMap[qNum];
      if (!patterns || !patterns.length) return;
      // Find the nearest passage-block (look up from the question)
      const question = item.closest('.exam-question');
      if (!question) return;
      let passageBlock = question.previousElementSibling;
      while (passageBlock && !passageBlock.classList.contains('passage-block')) {
        passageBlock = passageBlock.previousElementSibling;
      }
      if (!passageBlock) return;
      // Highlight matching text using textContent matching approach
      const passageTexts = passageBlock.querySelectorAll('.passage-text');
      passageTexts.forEach(el => {
        const fullText = el.textContent;
        patterns.forEach(pat => {
          const idx = fullText.toLowerCase().indexOf(pat.toLowerCase());
          if (idx === -1) return;
          const matchEnd = idx + pat.length;
          // Walk text nodes and wrap matching range
          highlightTextRange(el, idx, matchEnd);
        });
      });
      // Scroll the passage into view
      passageBlock.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  function highlightTextRange(container, startOffset, endOffset) {
    const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null);
    let currentOffset = 0;
    const nodesToWrap = [];
    while (walker.nextNode()) {
      const node = walker.currentNode;
      const nodeLen = node.textContent.length;
      const nodeStart = currentOffset;
      const nodeEnd = currentOffset + nodeLen;
      // Check overlap with [startOffset, endOffset)
      if (nodeEnd > startOffset && nodeStart < endOffset) {
        const wrapStart = Math.max(0, startOffset - nodeStart);
        const wrapEnd = Math.min(nodeLen, endOffset - nodeStart);
        nodesToWrap.push({ node, wrapStart, wrapEnd });
      }
      currentOffset += nodeLen;
      if (currentOffset >= endOffset) break;
    }
    // Apply wrapping in reverse to avoid shifting issues
    for (let i = nodesToWrap.length - 1; i >= 0; i--) {
      const { node, wrapStart, wrapEnd } = nodesToWrap[i];
      const text = node.textContent;
      const before = text.substring(0, wrapStart);
      const match = text.substring(wrapStart, wrapEnd);
      const after = text.substring(wrapEnd);
      const frag = document.createDocumentFragment();
      if (before) frag.appendChild(document.createTextNode(before));
      const mark = document.createElement('mark');
      mark.className = 'evidence-hl';
      mark.textContent = match;
      frag.appendChild(mark);
      if (after) frag.appendChild(document.createTextNode(after));
      node.parentNode.replaceChild(frag, node);
    }
  }

  function clearEvidenceHighlights() {
    document.querySelectorAll('mark.evidence-hl').forEach(mark => {
      const parent = mark.parentNode;
      while (mark.firstChild) parent.insertBefore(mark.firstChild, mark);
      parent.removeChild(mark);
      parent.normalize(); // merge adjacent text nodes
    });
  }

  // Clear evidence highlights when clicking elsewhere
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.correct-item[data-evq]') && !e.target.closest('.evidence-hl')) {
      clearEvidenceHighlights();
      document.querySelectorAll('.evidence-active').forEach(el => el.classList.remove('evidence-active'));
    }
  });

  // ===== SENTENCE POPUP =====
  let _sentTrans = [];

  function wrapSentences(paragraph, passageData) {
    const pairs = passageData?.sentencePairs;
    if (!pairs || !pairs.length) return paragraph;
    let html = paragraph;
    // Process longest sentences first to avoid partial matches
    const sorted = pairs.map((pair, i) => ({ en: pair[0], ja: pair[1], i }))
      .sort((a, b) => b.en.length - a.en.length);
    const placeholders = {};
    sorted.forEach(({ en, ja }) => {
      const idx = html.indexOf(en);
      if (idx === -1) return;
      const tidx = _sentTrans.length;
      _sentTrans.push(ja);
      const ph = `\x00SENT${tidx}\x00`;
      placeholders[ph] = `<span class="sentence-span" data-tidx="${tidx}">${en}</span>`;
      html = html.substring(0, idx) + ph + html.substring(idx + en.length);
    });
    // Restore placeholders
    Object.entries(placeholders).forEach(([ph, val]) => {
      html = html.replace(ph, val);
    });
    return html;
  }

  function setupSentencePopups(container) {
    let tooltip = null;
    container.addEventListener('click', function (e) {
      const span = e.target.closest('.sentence-span');
      if (tooltip) { tooltip.remove(); tooltip = null; }
      document.querySelectorAll('.sentence-span.active').forEach(el => el.classList.remove('active'));
      if (!span || span.dataset.tidx === undefined) return;
      e.stopPropagation();
      span.classList.add('active');
      const trans = _sentTrans[parseInt(span.dataset.tidx)];
      if (!trans) return;
      tooltip = document.createElement('div');
      tooltip.className = 'sentence-tooltip';
      tooltip.textContent = trans;
      document.body.appendChild(tooltip);
      const rect = span.getBoundingClientRect();
      let top = rect.bottom + 6;
      let left = rect.left;
      if (left + tooltip.offsetWidth > window.innerWidth - 10) left = window.innerWidth - tooltip.offsetWidth - 10;
      if (left < 10) left = 10;
      if (top + tooltip.offsetHeight > window.innerHeight - 10) top = rect.top - tooltip.offsetHeight - 6;
      tooltip.style.top = top + 'px';
      tooltip.style.left = left + 'px';
    });
    document.addEventListener('click', function (e) {
      if (tooltip && !e.target.closest('.sentence-span')) {
        tooltip.remove(); tooltip = null;
        document.querySelectorAll('.sentence-span.active').forEach(el => el.classList.remove('active'));
      }
    });
  }

  // ===== EXAM SELECT =====
  window._selExam = function (qn, val) {
    // 演習モードで既に回答済みの問題はスキップ
    if (settings.practiceMode && examAnswers[qn] !== undefined) {
      const qEl = document.getElementById('q' + qn);
      if (qEl && qEl.querySelector('.exam-choice-btn.disabled')) return;
    }
    examAnswers[qn] = val;
    document.querySelectorAll(`[data-q="${qn}"]`).forEach(b => {
      b.classList.remove('selected');
      if (parseInt(b.dataset.val) === val) b.classList.add('selected');
    });
    updatePart1Progress();
    // Update all dynamic section progress bars
    if (DATA && DATA.sections) {
      DATA.sections.forEach((sec, idx) => {
        if (sec.type === 'sentence-order' || sec.type === 'vocabulary') {
          const partId = 'part' + (idx + 1);
          const qs = sec.questions || [];
          const ans = qs.filter(q => examAnswers[q.number]).length;
          const pe = document.getElementById(partId + 'Progress');
          const pt = document.getElementById(partId + 'ProgressText');
          if (pe) pe.style.width = (ans / qs.length * 100) + '%';
          if (pt) pt.textContent = `${ans} / ${qs.length}`;
        }
      });
    }
    // ===== 演習モード: 即時フィードバック =====
    if (settings.practiceMode) {
      practiceGradeQuestion(qn, val);
    }
  };

  function practiceGradeQuestion(qn, userAnswer) {
    const q = findQuestion(qn);
    if (!q) return;
    const ok = userAnswer === q.answer;
    const qEl = document.getElementById('q' + qn);
    if (!qEl) return;

    // 1) 選択肢に正誤スタイルを適用 & disabled化
    qEl.querySelectorAll('.exam-choice-btn').forEach(b => {
      b.classList.add('disabled');
      const v = parseInt(b.dataset.val);
      if (v === q.answer) b.classList.add('correct');
      else if (v === userAnswer && !ok) b.classList.add('wrong');
      else b.classList.add('faded');
    });

    // 2) 問題カードにボーダーアクセント
    qEl.classList.add(ok ? 'practice-correct' : 'practice-wrong');

    // 3) 正解インジケーター表示
    qEl.querySelectorAll('.answer-indicator').forEach(el => el.classList.remove('hidden'));

    // 4) 解説(grammar-note)を表示
    qEl.querySelectorAll('.grammar-note').forEach(el => {
      el.classList.remove('hidden');
      el.classList.add('practice-feedback');
    });

    // 5) 選択肢分析(choice-analysis)を表示
    qEl.querySelectorAll('.choice-analysis').forEach(el => {
      el.classList.remove('hidden');
      el.classList.add('practice-feedback');
    });

    // 6) 和訳(translation-block)をこの問題内だけ表示
    qEl.querySelectorAll('.translation-block').forEach(el => {
      el.classList.remove('hidden');
      el.classList.add('practice-feedback');
    });
    // 選択肢の翻訳も表示
    qEl.querySelectorAll('.choice-translation').forEach(el => {
      el.classList.remove('hidden');
      el.classList.add('practice-feedback');
    });

    // 7) passage-fill / reading-comprehension: 直前のpassage-blockの和訳も表示
    const passageBlock = findPrecedingPassageBlock(qEl);
    if (passageBlock) {
      // Check if ALL questions for this passage have been answered
      const passageQuestions = [];
      let sibling = passageBlock.nextElementSibling;
      while (sibling && sibling.classList.contains('exam-question')) {
        const qNum = parseInt((sibling.id || '').replace('q', ''));
        if (qNum) passageQuestions.push(qNum);
        sibling = sibling.nextElementSibling;
      }
      const allAnswered = passageQuestions.every(num => examAnswers[num] !== undefined);
      if (allAnswered) {
        passageBlock.querySelectorAll('.translation-block').forEach(el => {
          el.classList.remove('hidden');
          el.classList.add('practice-feedback');
        });
      }
    }
  }

  function findPrecedingPassageBlock(qEl) {
    let el = qEl.previousElementSibling;
    while (el) {
      if (el.classList.contains('passage-block')) return el;
      el = el.previousElementSibling;
    }
    return null;
  }

  // ===== GRADING =====
  function gradePart(partId, questions) {
    let correct = 0;
    questions.forEach(q => {
      const ua = examAnswers[q.number]; const ok = ua === q.answer;
      if (ok) correct++;
      document.querySelectorAll(`[data-q="${q.number}"]`).forEach(b => {
        b.classList.add('disabled');
        const v = parseInt(b.dataset.val);
        if (v === q.answer) b.classList.add('correct');
        else if (v === ua && !ok) b.classList.add('wrong');
        else b.classList.add('faded');
      });
      // Show analysis after grading
      const qEl = document.getElementById('q' + q.number);
      if (qEl) { qEl.querySelectorAll('.choice-analysis').forEach(el => el.classList.remove('hidden')); }
    });
    const rEl = document.getElementById(partId + 'Results');
    rEl.style.display = 'block';
    rEl.innerHTML = `<div class="results-summary"><div class="big-score">${correct} / ${questions.length}</div><div class="score-label">正解数</div></div><div class="results-detail">${questions.map(q => { const ua = examAnswers[q.number]; const ok = ua === q.answer; return `<div class="result-row ${ok ? 'correct-row' : 'wrong-row'}"><span class="q-num">(${q.number})</span><span>正解: ${q.answer} ${ua ? (ok ? '' : `　解答: ${ua}`) : '(未回答)'}</span><span class="q-status">${ok ? '✓' : '✗'}</span></div>`; }).join('')}</div>`;
    document.getElementById(partId + 'Submit').style.display = 'none';
    rEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // ===== PRINT =====
  APP.showPrintMenu = function () {
    // Dynamically update section buttons based on DATA.sections
    const modal = document.getElementById('printModal');
    const btns = modal.querySelectorAll('.print-menu-btn');
    // Section button indices: btn[2]=Part1, btn[3]=Part2, btn[4]=Part3, +Part4 if exists
    const sectionBtnStart = 2; // 0=vocabList, 1=vocabTest, 2=Part1, 3=Part2, 4=Part3
    const sections = DATA.sections || [];
    // Remove any previously added Part4 button
    const existingP4 = modal.querySelector('[data-part4-btn]');
    if (existingP4) existingP4.remove();
    // Update Part 1-3 buttons
    const sectionLabels = { 'vocabulary': '語彙・文法', 'sentence-order': '並べ替え', 'passage-fill': '長文空所補充', 'reading-comprehension': '長文読解' };
    for (let i = 0; i < 3; i++) {
      const btn = btns[sectionBtnStart + i];
      if (!btn) continue;
      if (i < sections.length) {
        const sec = sections[i];
        btn.style.display = '';
        btn.textContent = `📝 ${sec.name}　${sectionLabels[sec.type] || sec.nameEn || ''}`;
      } else {
        btn.style.display = 'none';
      }
    }
    // Add Part4 button if sections[3] exists
    if (sections.length >= 4) {
      const sec = sections[3];
      const p4Btn = document.createElement('button');
      p4Btn.className = 'print-menu-btn';
      p4Btn.setAttribute('data-part4-btn', 'true');
      p4Btn.style.cssText = btns[sectionBtnStart].style.cssText;
      p4Btn.textContent = `📝 ${sec.name}　${sectionLabels[sec.type] || sec.nameEn || ''}`;
      p4Btn.onclick = function() { window.APP.printPart4(); };
      // Insert after Part3 button
      const afterBtn = btns[sectionBtnStart + 2];
      if (afterBtn && afterBtn.nextSibling) {
        afterBtn.parentNode.insertBefore(p4Btn, afterBtn.nextSibling);
      }
    }
    modal.style.display = 'flex';
  };
  APP.closePrintMenu = function () { document.getElementById('printModal').style.display = 'none'; };

  function doPrint(html) {
    const frame = document.getElementById('printFrame');
    frame.innerHTML = html;
    APP.closePrintMenu();
    // Generate QR codes if any .qr-container exists
    const qrContainers = frame.querySelectorAll('.qr-container');
    if (qrContainers.length > 0 && typeof QRCode !== 'undefined') {
      qrContainers.forEach(c => {
        new QRCode(c, { text: c.dataset.url, width: 72, height: 72, colorDark: '#1a1a1a', colorLight: '#ffffff', correctLevel: QRCode.CorrectLevel.M });
      });
      setTimeout(() => window.print(), 300);
    } else {
      setTimeout(() => window.print(), 200);
    }
  }

  APP.printVocabList = function () {
    const rows = DATA.vocabulary.map(v => `<tr><td>${v.word}</td><td>${v.pos}</td><td>${v.meaning}</td><td>${v.level}</td><td>${v.source || '大問1'}</td><td>${v.example}</td></tr>`).join('');
    doPrint(`<h2>${DATA.title} — 単語リスト</h2><table><tr><th>単語</th><th>品詞</th><th>意味</th><th>レベル</th><th>出典</th><th>例文</th></tr>${rows}</table>`);
  };

  APP.printVocabTest = function () {
    const rows = DATA.vocabulary.map((v, i) => `<tr><td>${i + 1}</td><td>${v.word}</td><td>${v.pos}</td><td>${v.source || '大問1'}</td><td style="min-width:120px"></td></tr>`).join('');
    doPrint(`<h2>${DATA.title} — 単語テスト</h2><p>次の英単語の意味を日本語で書きなさい。</p><table><tr><th>#</th><th>単語</th><th>品詞</th><th>出典</th><th>意味</th></tr>${rows}</table>`);
  };

  APP.printPart1 = function () { printSectionByIndex(0); };
  APP.printPart2 = function () { printSectionByIndex(1); };
  APP.printPart3 = function () { printSectionByIndex(2); };
  APP.printPart4 = function () { printSectionByIndex(3); };

  function printSectionByIndex(idx) {
    const sec = DATA.sections[idx];
    if (!sec) { alert(`大問${idx + 1} のデータがありません`); return; }

    if (sec.type === 'vocabulary') {
      // Vocabulary / conversation fill-in-the-blank
      const html = sec.questions.map(q => `<div class="print-q"><div class="print-q-num">(${q.number})</div><div class="print-q-text">${q.text.replace(/\(　\)/g, '(\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000)').replace(/\n/g, '<br>')}</div><ul class="print-choices">${q.choices.map((c, i) => `<li>${i + 1}　${c}</li>`).join('')}</ul></div>`).join('');
      doPrint(`<h2>${DATA.title} — ${sec.name}</h2><p>${sec.instruction}</p>${html}`);
    }
    else if (sec.type === 'sentence-order') {
      // Sentence ordering - compact test-style layout
      const circled = ['①','②','③','④','⑤'];
      const html = sec.questions.map(q => {
        const slots = q.answerSlots || [2, 4];
        const numWords = q.words.length;
        const wordsLine = '（ ' + q.words.map((w, i) => circled[i] + ' ' + w).join('　') + ' ）';
        const slotLabelsRow = Array.from({length: numWords}, (_, i) =>
          `<td style="text-align:center;font-size:7pt;color:#888;padding:0 2px;border:none">${slots.includes(i+1) ? (i+1)+'番目' : ''}</td>`
        ).join('');
        const boxesRow = Array.from({length: numWords}, () =>
          `<td style="padding:0 1px;border:none"><div style="border:1px solid #333;height:18px;min-width:50px"></div></td>`
        ).join('');
        const choicesLine = q.choices.map((c, i) =>
          `<span style="margin-right:24px">${i + 1}　${c}</span>`
        ).join('');
        return `<div style="margin-bottom:14px;padding-bottom:6px">
<div style="margin-bottom:3px"><b>(${q.number})</b>　${q.text}</div>
<div style="font-size:10pt;margin:2px 0">${wordsLine}</div>
<table style="margin:2px 0 4px 10px;border-collapse:collapse;border:none"><tr>${slotLabelsRow}</tr><tr>${boxesRow}${q.frameSuffix ? `<td style="padding-left:4px;font-size:10pt;border:none">${q.frameSuffix}</td>` : ''}</tr></table>
<div style="font-size:10pt;margin-top:2px">${choicesLine}</div>
</div>`;
      }).join('');
      doPrint(`<h2>${DATA.title} — ${sec.name}</h2><p style="font-size:9pt">${sec.instruction}</p>${html}`);
    }
    else if (sec.type === 'passage-fill') {
      // Passage fill (準2級以上)
      let html = '';
      sec.passages.forEach(p => {
        html += `<h3>${p.label}　${p.title}</h3>`;
        p.paragraphs.forEach(para => { html += `<div class="print-passage">${para}</div>`; });
        p.questions.forEach(q => {
          html += `<div class="print-q"><div class="print-q-num">(${q.number})</div><ul class="print-choices">${q.choices.map((c, i) => `<li>${i + 1}　${c}</li>`).join('')}</ul></div>`;
        });
      });
      doPrint(`<h2>${DATA.title} — ${sec.name}</h2><p>${sec.instruction}</p>${html}`);
    }
    else if (sec.type === 'reading-comprehension') {
      // Reading comprehension
      let html = '';
      sec.passages.forEach(p => {
        html += `<h3>${p.label}　${p.title}</h3>`;
        if (p.format === 'email' && p.meta) {
          html += `<div style="border:1px solid #999;padding:8px;margin-bottom:8px;font-size:10pt"><div>From: ${p.meta.from}</div><div>To: ${p.meta.to}</div><div>Date: ${p.meta.date}</div><div>Subject: ${p.meta.subject}</div></div>`;
        }
        p.paragraphs.forEach(para => { html += `<div class="print-passage">${para}</div>`; });
        p.questions.forEach(q => {
          html += `<div class="print-q"><div class="print-q-num">(${q.number}) ${q.question}</div><ul class="print-choices">${q.choices.map((c, i) => `<li>${i + 1}　${c}</li>`).join('')}</ul></div>`;
        });
      });
      doPrint(`<h2>${DATA.title} — ${sec.name}</h2><p>${sec.instruction}</p>${html}`);
    }
    else {
      alert(`未対応のセクションタイプ: ${sec.type}`);
    }
  }

  APP.printAnswerKey = function () {
    const allQs = DATA.sections.flatMap(sec => {
      if (sec.questions) return sec.questions;
      if (sec.passages) return sec.passages.flatMap(p => p.questions);
      return [];
    });
    const rows = allQs.map(q => `<tr><td>(${q.number})</td><td style="font-weight:700">${q.answer}</td></tr>`).join('');
    doPrint(`<h2>${DATA.title} — 解答一覧</h2><table style="max-width:300px"><tr><th>問題</th><th>正解</th></tr>${rows}</table>`);
  };

  APP.printLessonPlan = function () {
    const lp = DATA.lessonPlan;
    if (!lp) return;
    let questionsPage = `<h2>${DATA.title} — 文法ワークシート</h2>`;
    let answersPage = '';

    lp.focusPoints.forEach((fp, idx) => {
      const n = idx + 1;
      const pb = idx > 0 ? 'page-break-before:always;' : '';
      // === Questions Page ===
      questionsPage += `<h3 style="${pb}">Focus ${n}: ${fp.title}</h3>`;
      questionsPage += `<p style="font-size:10pt;color:#666">${fp.subtitle}</p>`;

      // Example sentences (English only, students fill in the translation)
      const exArr = fp.examples || fp.exampleSentences;
      if (exArr) {
        questionsPage += `<h4>■ 例文</h4>`;
        exArr.forEach((ex, ei) => {
          questionsPage += `<div style="margin-bottom:8px"><strong>(${ei + 1})</strong> ${ex.en}</div>`;
          questionsPage += `<div style="border-bottom:1px dashed #999;height:24px;margin-bottom:6px"></div>`;
        });
      }

      // Practice passage + questions
      const pp = fp.practicePassage;
      if (pp) {
        questionsPage += `<h4>■ 練習パッセージ</h4>`;
        questionsPage += `<div style="border:1px solid #ccc;padding:10px;margin-bottom:10px;font-size:10pt;line-height:1.8;white-space:pre-wrap">${pp.en}</div>`;
        const pqs = fp.practiceQuestions || (pp && pp.questions) || [];
        questionsPage += `<h4>■ 確認問題</h4>`;
        pqs.forEach((q, qi) => {
          questionsPage += `<div style="margin-bottom:10px"><strong>Q${qi + 1}.</strong> ${q.q}</div>`;
          questionsPage += `<div style="border-bottom:1px dashed #999;height:28px;margin-bottom:6px"></div>`;
        });
      }

      // === Answers Page ===
      answersPage += `<h3 style="page-break-before:always;">Focus ${n}: ${fp.title}　【解答】</h3>`;

      // Example sentences with translations
      const exArr2 = fp.examples || fp.exampleSentences;
      if (exArr2) {
        answersPage += `<h4>■ 例文　解答</h4>`;
        exArr2.forEach((ex, ei) => {
          answersPage += `<div style="margin-bottom:6px"><strong>(${ei + 1})</strong> ${ex.en}</div>`;
          answersPage += `<div style="margin-bottom:4px;color:#333">→ ${ex.ja}</div>`;
          if (ex.note) answersPage += `<div style="font-size:9pt;color:#888;margin-bottom:8px">💡 ${ex.note}</div>`;
        });
      }

      // Practice passage translation + answers
      if (pp) {
        answersPage += `<h4>■ 参考和訳</h4>`;
        answersPage += `<div style="border:1px solid #ccc;padding:10px;margin-bottom:10px;font-size:9pt;line-height:1.7;white-space:pre-wrap;color:#333">${pp.ja}</div>`;
        const pqs2 = fp.practiceQuestions || (pp && pp.questions) || [];
        answersPage += `<h4>■ 確認問題　解答</h4>`;
        pqs2.forEach((q, qi) => {
          answersPage += `<div style="margin-bottom:6px"><strong>Q${qi + 1}.</strong> ${q.q}</div>`;
          answersPage += `<div style="margin-bottom:10px;color:#006600;font-weight:600">A. ${q.a}</div>`;
        });
      }
    });

    doPrint(questionsPage + answersPage);
  };

  APP.printLessonRef = function () {
    const lp = DATA.lessonPlan;
    if (!lp) return;
    const qrUrl = `https://read-pass-pro.vercel.app/index.html?grade=${currentGradeId}&exam=${currentExamId}`;
    let html = `<div style="float:right;text-align:center;margin:0 0 8px 12px"><div class="qr-container" data-url="${qrUrl}"></div><div style="font-size:7pt;color:#888;margin-top:2px">ReadPass Pro</div></div><h2>${DATA.title} — 文法解説プリント</h2><p style="font-size:9pt;color:#888">講師用参考資料｜大問2・3の読解に必要な重要文法・構文</p>`;

    lp.focusPoints.forEach((fp, idx) => {
      const n = idx + 1;
      const pb = idx > 0 ? 'page-break-before:always;' : '';

      html += `<h3 style="${pb}margin-top:10px;border-bottom:2px solid #333;padding-bottom:4px">Focus ${n}　${fp.title}</h3>`;
      html += `<p style="font-size:10pt;color:#555;margin-bottom:8px">${fp.subtitle}</p>`;

      // Why section
      const whyText = fp.explanation || fp.why || '';
      html += `<div style="margin-bottom:10px"><h4 style="font-size:10pt;color:#333;margin-bottom:4px">▶ ポイント解説</h4>`;
      html += `<p style="font-size:9.5pt;line-height:1.7;color:#333">${whyText}</p></div>`;

      // Source quote
      html += `<div style="border-left:3px solid #6c63ff;padding:8px 12px;margin-bottom:10px;background:#f5f3ff;font-style:italic;font-size:9.5pt;line-height:1.6">${fp.sourceQuote}</div>`;
      html += `<p style="text-align:right;font-size:8pt;color:#888;margin-bottom:12px">— ${fp.sourceLocation}</p>`;

      // Categories table (for discourse markers)
      if (fp.categories) {
        html += `<h4 style="font-size:10pt;color:#333;margin-bottom:6px">▶ カテゴリ一覧</h4>`;
        html += `<table style="width:100%;border-collapse:collapse;margin-bottom:12px;font-size:9pt">`;
        html += `<tr style="background:#f0f0f0"><th style="border:1px solid #ccc;padding:5px;text-align:left">種類</th><th style="border:1px solid #ccc;padding:5px;text-align:left">マーカー</th><th style="border:1px solid #ccc;padding:5px;text-align:left">機能</th></tr>`;
        fp.categories.forEach(c => {
          html += `<tr><td style="border:1px solid #ccc;padding:5px;font-weight:700">${c.type}</td><td style="border:1px solid #ccc;padding:5px">${c.markers.join(' / ')}</td><td style="border:1px solid #ccc;padding:5px;color:#555">${c.ja}</td></tr>`;
        });
        html += `</table>`;
      }

      // Example sentences with full explanations
      const refExArr = fp.examples || fp.exampleSentences;
      if (refExArr) {
        html += `<h4 style="font-size:10pt;color:#333;margin-bottom:6px">▶ 例文と解説</h4>`;
        refExArr.forEach((ex, ei) => {
          html += `<div style="margin-bottom:10px;padding:8px 10px;background:#fafafa;border:1px solid #e0e0e0;border-radius:4px">`;
          html += `<div style="font-size:10pt;font-weight:600;margin-bottom:3px">(${ei + 1}) ${ex.en}</div>`;
          html += `<div style="font-size:9pt;color:#444;margin-bottom:2px">→ ${ex.ja}</div>`;
          if (ex.note) html += `<div style="font-size:8.5pt;color:#6c63ff;font-weight:600">💡 ${ex.note}</div>`;
          html += `</div>`;
        });
      }

      // Practice passage with translation
      const pp = fp.practicePassage;
      if (pp) {
        html += `<h4 style="font-size:10pt;color:#333;margin-bottom:6px">▶ 練習パッセージ</h4>`;
        html += `<div style="border:1px solid #ccc;padding:10px;margin-bottom:6px;font-size:9.5pt;line-height:1.8;white-space:pre-wrap">${pp.en}</div>`;
        html += `<div style="border:1px solid #ddd;padding:10px;margin-bottom:10px;font-size:8.5pt;line-height:1.7;white-space:pre-wrap;color:#555;background:#fafafa">【参考和訳】${pp.ja}</div>`;

        // Q&A
        html += `<h4 style="font-size:10pt;color:#333;margin-bottom:6px">▶ 確認問題と模範解答</h4>`;
        const refPqs = fp.practiceQuestions || (pp && pp.questions) || [];
        refPqs.forEach((q, qi) => {
          html += `<div style="margin-bottom:8px">`;
          html += `<div style="font-size:9.5pt;font-weight:600">Q${qi + 1}. ${q.q}</div>`;
          html += `<div style="font-size:9pt;color:#006600;font-weight:600;padding:3px 0 0 16px">A. ${q.a}</div>`;
          html += `</div>`;
        });
      }
    });

    doPrint(html);
  };

  // ===== LESSON PLAN =====
  function renderLessonPlan() {
    const area = document.getElementById('lessonPlanArea');
    if (!area) return;
    // Dynamically update lesson tab header/text for Grade 4
    const isG4Header = currentGradeId === 'grade4' || currentGradeId === 'grade5';
    const lessonTab = document.querySelector('[data-tab="lesson"]');
    if (lessonTab) {
      const tabLabel = lessonTab.querySelector('.tab-label');
      if (tabLabel) tabLabel.textContent = isG4Header ? 'レッスン' : '文法';
    }
    const lessonH2 = area.closest('#tab-lesson')?.querySelector('.section-header h2');
    if (lessonH2) lessonH2.textContent = isG4Header ? '🌟 英語の表現を学ぼう' : '📚 文法・構文フォーカス';
    const lessonDesc = area.closest('#tab-lesson')?.querySelector('.section-header .section-desc');
    if (lessonDesc) lessonDesc.textContent = isG4Header ? 'この試験に出てくる英語の表現を楽しく学ぼう！' : '大問2・3の読解に必要な重要文法を例文・例パッセージで学習します';
    const lp = DATA.lessonPlan;
    if (!lp) { area.innerHTML = '<p style="color:var(--text-secondary)">この試験回のデータはまだありません。</p>'; return; }
    area.innerHTML = lp.focusPoints.map((fp, idx) => {
      let categoriesHtml = '';
      if (fp.categories) {
        categoriesHtml = `<div class="fp-section-label"><span class="material-symbols-rounded">category</span>カテゴリ一覧</div><div class="fp-categories">${fp.categories.map(c => `<div class="fp-cat"><div class="fp-cat-type">${c.type}</div><div class="fp-cat-markers">${c.markers.join(' / ')}</div><div class="fp-cat-ja">${c.ja}</div></div>`).join('')}</div>`;
      }
      const examples = fp.examples || fp.exampleSentences || [];
      const examplesHtml = examples.map(ex => {
        const note = settings.simpleMode && ex.noteSimple ? ex.noteSimple : (ex.note || '');
        const audioBtn = ex.audio ? `<button class="q-audio-btn vocab-audio-btn" onclick="window.APP.playQuestionAudio(this, '${ex.audio}')" title="聞いてみよう">🔊</button>` : '';
        return `<div class="fp-example"><div class="fp-example-en">${ex.en} ${audioBtn}</div><div class="fp-example-ja">${ex.ja}</div>${note ? `<div class="fp-example-note">💡 ${note}</div>` : ''}</div>`;
      }).join('');
      const whyText = settings.simpleMode && fp.explanationSimple ? fp.explanationSimple : (fp.explanation || fp.why || '');
      const sourceQuoteText = (fp.sourceQuote || '').replace(/\n/g, '<br>');
      const sqAudioBtn = fp.sourceQuoteAudio ? `<button class="q-audio-btn vocab-audio-btn" onclick="window.APP.playQuestionAudio(this, '${fp.sourceQuoteAudio}')" title="聞いてみよう" style="margin-left:8px">🔊</button>` : '';
      const sourceQuoteHtml = sourceQuoteText + sqAudioBtn;
      const pp = fp.practicePassage;
      const pqs = settings.simpleMode && fp.practiceQuestionsSimple ? fp.practiceQuestionsSimple : (fp.practiceQuestions || (pp && pp.questions) || []);
      const fpUid = `pp-${fp.id || idx}`;
      const isG4 = currentGradeId === 'grade4' || currentGradeId === 'grade5';
      const audioLabel = isG4 ? '🔊 聞いてみよう！' : '🔊 音読用音声を再生';
      const audioBtn = pp && pp.audioFile ? `
        <div class="fp-audio-player">
          <button class="fp-audio-btn" onclick="window.APP.playPracticeAudio(this, '${pp.audioFile}')" title="音声を再生">
            <span class="material-symbols-rounded" style="font-size:18px">play_circle</span>
            <span class="fp-audio-label">${audioLabel}</span>
          </button>
          <div class="fp-audio-controls">
            <span class="fp-audio-time fp-audio-current">0:00</span>
            <input type="range" class="fp-audio-seek" value="0" step="0.1" min="0" max="100" 
              oninput="window.APP.seekPracticeAudio(this)" 
              onchange="window.APP.seekPracticeAudioEnd(this)" 
              disabled>
            <span class="fp-audio-time fp-audio-duration">0:00</span>
          </div>
        </div>` : '';
      const highlightBtn = (pp && !isG4) ? `
          <button class="fp-pron-hl-btn" onclick="window.APP.togglePronHL('${fpUid}')" title="発音ポイントをハイライト">
            <span class="material-symbols-rounded" style="font-size:18px">highlight</span>
            <span>発音ポイントを表示</span>
          </button>` : '';
      const fpHlLabel = isG4 ? 'キーワードをハイライト' : 'FPをハイライト';
      const fpHlBtn = (pp && fp.highlightPatterns && fp.highlightPatterns.length) ? `
          <button class="fp-pattern-hl-btn" onclick="window.APP.toggleFPHL('${fpUid}', ${esc(JSON.stringify(fp.highlightPatterns))})" title="重点表現をハイライト表示">
            <span class="material-symbols-rounded" style="font-size:18px">format_ink_highlighter</span>
            <span>${fpHlLabel}</span>
          </button>` : '';
      const transBtn = pp && pp.ja ? `
          <button class="fp-trans-btn" onclick="window.APP.togglePassageTrans('${fpUid}-ja')" title="日本語訳を表示">
            <span class="material-symbols-rounded" style="font-size:18px">translate</span>
            <span>日本語訳を表示</span>
          </button>` : '';
      const passageHtml = pp ? `
        <div class="fp-section-label"><span class="material-symbols-rounded">description</span>${isG4 ? '読んでみよう！' : '練習パッセージ'}</div>
        <div class="fp-passage">
          <div class="fp-passage-en" id="${fpUid}" data-original="${(pp.en || '').replace(/"/g, '&quot;')}">${(pp.en || '').replace(/\n/g, '<br>')}</div>
          <div class="fp-passage-btns">
            ${audioBtn}
            ${highlightBtn}
            ${fpHlBtn}
            ${transBtn}
          </div>
          <div class="fp-passage-ja" id="${fpUid}-ja" style="display:none">${(pp.ja || '').replace(/\n/g, '<br>')}</div>
          ${pp.source ? `<div class="fp-passage-source">📌 出典: ${pp.source}</div>` : ''}
        </div>
        ${(currentGradeId !== 'grade3' && currentGradeId !== 'grade4' && currentGradeId !== 'grade5') ? `<div class="fp-pronunciation-tips">
          <div class="fp-section-label"><span class="material-symbols-rounded">record_voice_over</span>音読のポイント</div>
          <div class="fp-pron-grid">
            <div class="fp-pron-card">
              <div class="fp-pron-title">🔗 リエゾン（Linking）</div>
              <div class="fp-pron-desc">単語の末尾の子音と次の単語の先頭の母音がつながって発音されます。</div>
              <div class="fp-pron-examples">
                <div class="fp-pron-ex"><span class="fp-pron-orig">pick<u>ed</u> <u>u</u>p →</span> <span class="fp-pron-sound">/pɪk<b>tʌ</b>p/（ピクタップ）</span></div>
                <div class="fp-pron-ex"><span class="fp-pron-orig">look<u>ed</u> <u>a</u>t →</span> <span class="fp-pron-sound">/lʊk<b>tæ</b>t/（ルクタット）</span></div>
                <div class="fp-pron-ex"><span class="fp-pron-orig">a<u>n</u> <u>i</u>mportant →</span> <span class="fp-pron-sound">/ə<b>nɪ</b>mpɔːrtənt/（アニンポータント）</span></div>
              </div>
            </div>
            <div class="fp-pron-card">
              <div class="fp-pron-title">🔇 リダクション（Reduction）</div>
              <div class="fp-pron-desc">機能語（冠詞・前置詞・代名詞など）が弱く短く発音されます。母音が曖昧な「ə（シュワ）」に変わります。</div>
              <div class="fp-pron-examples">
                <div class="fp-pron-ex"><span class="fp-pron-orig">to →</span> <span class="fp-pron-sound">/tə/（トゥ→タ）</span></div>
                <div class="fp-pron-ex"><span class="fp-pron-orig">the →</span> <span class="fp-pron-sound">/ðə/（ザ→ダ）</span></div>
                <div class="fp-pron-ex"><span class="fp-pron-orig">of →</span> <span class="fp-pron-sound">/əv/（オブ→アヴ）</span></div>
                <div class="fp-pron-ex"><span class="fp-pron-orig">can →</span> <span class="fp-pron-sound">/kən/（キャン→カン）</span></div>
              </div>
            </div>
          </div>
          <div class="fp-hl-legend" id="${fpUid}-legend" style="display:none">
            <span class="fp-hl-legend-item"><span class="fp-hl-swatch liaison"></span>リエゾン（子音→母音）</span>
            <span class="fp-hl-legend-item"><span class="fp-hl-swatch reduction"></span>リダクション（弱化）</span>
          </div>
          <div class="fp-pron-tip">💡 音声を聞いて、リエゾンとリダクションが起きている箇所を意識しながら音読しましょう。</div>
        </div>` : ''}
        ${pqs.length ? `<div class="fp-section-label"><span class="material-symbols-rounded">help</span>${isG4 ? 'チャレンジ！' : '確認問題'}</div>
        ${pqs.map((q, qi) => `
          <div class="fp-qa">
            <div class="fp-q">Q${qi + 1}. ${q.q}</div>
            <button class="fp-a-toggle" onclick="this.nextElementSibling.classList.toggle('show')"><span class="material-symbols-rounded" style="font-size:14px">visibility</span> 解答を見る</button>
            <div class="fp-a">${q.a}${q.audio ? ` <button class="q-audio-btn vocab-audio-btn" onclick="window.APP.playQuestionAudio(this, '${q.audio}')" title="聞いてみよう">🔊</button>` : ''}</div>
          </div>
        `).join('')}` : ''}
      ` : '';
      return `
        <div class="fp-card" id="fp-${fp.id}">
          <div class="fp-header" onclick="this.parentElement.classList.toggle('open')">
            <div class="fp-num">${idx + 1}</div>
            <div class="fp-title-group">
              <div class="fp-title">${fp.title}</div>
              <div class="fp-subtitle">${fp.subtitle}</div>
            </div>
            <span class="material-symbols-rounded fp-toggle">expand_more</span>
          </div>
          <div class="fp-body"><div class="fp-inner">
            <div class="fp-section-label"><span class="material-symbols-rounded">info</span>${isG4 ? 'どんなときに使うの？' : 'なぜこの構文が重要か'}</div>
            <div class="fp-why">${whyText}</div>
            <div class="fp-source-quote">${sourceQuoteHtml}</div>
            <div class="fp-source-loc">— ${fp.sourceLocation}</div>
            ${categoriesHtml}
            <div class="fp-section-label"><span class="material-symbols-rounded">edit_note</span>${isG4 ? 'こんなふうに使うよ' : '例文'}</div>
            ${examplesHtml}
            ${passageHtml}
          </div></div>
        </div>
      `;
    }).join('');
  }
  // ===== PRONUNCIATION HIGHLIGHT =====
  const _VOWELS = new Set('aeiouAEIOU'.split(''));
  const _CONSONANTS = new Set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'.split(''));
  // Only the most commonly reduced function words (keep list short to avoid clutter)
  const _REDUCTION_WORDS = new Set([
    'a', 'an', 'the',
    'to', 'of', 'for', 'at', 'in', 'on', 'from',
    'and', 'or', 'but',
    'is', 'are', 'was', 'were',
    'has', 'have', 'had',
    'can', 'could', 'would', 'should',
    'not',
    'him', 'her', 'them', 'us',
    'his', 'your', 'our', 'their'
  ]);

  const _pronHLState = {};

  APP.togglePronHL = function (uid) {
    const el = document.getElementById(uid);
    if (!el) return;
    const legend = document.getElementById(uid + '-legend');
    const btn = el.closest('.fp-passage')?.querySelector('.fp-pron-hl-btn');

    if (_pronHLState[uid]) {
      el.innerHTML = el.dataset.original.replace(/\n/g, '<br>');
      _pronHLState[uid] = false;
      if (legend) legend.style.display = 'none';
      if (btn) {
        btn.querySelector('span:last-child').textContent = '発音ポイントを表示';
        btn.classList.remove('active');
      }
      return;
    }

    const text = el.dataset.original;
    el.innerHTML = highlightPronunciation(text);
    _pronHLState[uid] = true;
    if (legend) legend.style.display = 'flex';
    if (btn) {
      btn.querySelector('span:last-child').textContent = 'ハイライトOFF';
      btn.classList.add('active');
    }
  };

  function highlightPronunciation(text) {
    // Split text into sentences (by period, then process each)
    // Tokenize: words + non-words
    const tokens = text.match(/[a-zA-Z'']+|[^a-zA-Z'']+/g) || [];

    // First pass: identify which word tokens exist
    const wordIndices = [];
    tokens.forEach((t, i) => {
      if (/^[a-zA-Z'']+$/.test(t)) wordIndices.push(i);
    });

    // Detect liaison pairs (consecutive word tokens where word1 ends consonant + word2 starts vowel)
    const liaisonPairs = new Set(); // stores index of first word in pair
    for (let wi = 0; wi < wordIndices.length - 1; wi++) {
      const idx1 = wordIndices[wi];
      const idx2 = wordIndices[wi + 1];
      const w1 = tokens[idx1];
      const w2 = tokens[idx2];
      // Check only if separated by single space (not across sentences)
      const between = tokens.slice(idx1 + 1, idx2).join('');
      if (between.trim() !== '' || !between.includes(' ')) continue;
      if (between !== ' ') continue;

      const lastChar = w1[w1.length - 1];
      const firstChar = w2[0];
      if (_CONSONANTS.has(lastChar) && _VOWELS.has(firstChar)) {
        liaisonPairs.add(idx1);
      }
    }

    // Build output
    let result = '';
    let i = 0;
    while (i < tokens.length) {
      const token = tokens[i];
      const isWord = /^[a-zA-Z'']+$/.test(token);

      if (!isWord) {
        result += token;
        i++;
        continue;
      }

      // Check if this word starts a liaison pair
      if (liaisonPairs.has(i) && i + 2 < tokens.length) {
        const w1 = tokens[i];
        const space = tokens[i + 1];
        const w2 = tokens[i + 2];
        // Render as linked pair with arc connector
        result += `<span class="pron-link-pair"><span class="pron-link-w1">${w1}</span><span class="pron-link-arc">⌢</span><span class="pron-link-w2">${w2}</span></span>`;
        i += 3;
        continue;
      }

      // Check if this word is a reduction target
      const wordLower = token.toLowerCase().replace(/'/g, '');
      if (_REDUCTION_WORDS.has(wordLower)) {
        result += `<span class="pron-weak">${token}</span>`;
      } else {
        result += token;
      }
      i++;
    }

    return result;
  }

  // ===== PASSAGE TRANSLATION TOGGLE =====
  APP.togglePassageTrans = function (jaId) {
    const el = document.getElementById(jaId);
    if (!el) return;
    const btn = el.closest('.fp-passage')?.querySelector('.fp-trans-btn');
    if (el.style.display === 'none') {
      el.style.display = 'block';
      if (btn) {
        btn.querySelector('span:last-child').textContent = '日本語訳を隠す';
        btn.classList.add('active');
      }
    } else {
      el.style.display = 'none';
      if (btn) {
        btn.querySelector('span:last-child').textContent = '日本語訳を表示';
        btn.classList.remove('active');
      }
    }
  };

  // ===== FP HIGHLIGHT TOGGLE =====
  const _fpHLState = {};
  APP.toggleFPHL = function (uid, patterns) {
    const el = document.getElementById(uid);
    if (!el) return;
    const btn = el.closest('.fp-passage')?.querySelector('.fp-pattern-hl-btn');

    if (_fpHLState[uid]) {
      // Turn off
      el.innerHTML = el.dataset.original.replace(/\n/g, '<br>');
      _fpHLState[uid] = false;
      if (btn) {
        btn.querySelector('span:last-child').textContent = 'FPをハイライト';
        btn.classList.remove('active');
      }
      return;
    }

    // Turn on
    let text = el.dataset.original;
    if (patterns && Array.isArray(patterns)) {
      // Sort patterns by length descending to match longer phrases first
      const sorted = [...patterns].sort((a, b) => b.length - a.length);
      sorted.forEach((pat, i) => {
        try {
          // Escape regex characters cleanly
          const safePat = pat.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
          // Use word boundaries \b to avoid partial word highlighting, 
          // but only if the pattern starts/ends with a word character
          let regexPrefix = /^\w/.test(pat) ? '\\b' : '';
          let regexSuffix = /\w$/.test(pat) ? '\\b' : '';
          
          const regex = new RegExp(`(${regexPrefix}${safePat}${regexSuffix})`, 'gi');
          text = text.replace(regex, `\x00MRK${i}\x00$1\x01MRK${i}\x01`);
        } catch (e) {}
      });
      text = text.replace(/\n/g, '<br>');
      sorted.forEach((_, i) => {
        text = text.replace(new RegExp(`\x00MRK${i}\x00`, 'g'), '<mark class="fp-hl-mark">');
        text = text.replace(new RegExp(`\x01MRK${i}\x01`, 'g'), '</mark>');
      });
    } else {
      text = text.replace(/\n/g, '<br>');
    }
    el.innerHTML = text;
    _fpHLState[uid] = true;
    if (btn) {
      btn.querySelector('span:last-child').textContent = 'ハイライトOFF';
      btn.classList.add('active');
    }
  };

  // ===== PRACTICE AUDIO =====
  let _practiceAudio = null;
  let _practiceAudioBtn = null;
  let _isSeeking = false;

  function formatAudioTime(seconds) {
    if (isNaN(seconds) || !isFinite(seconds)) return "0:00";
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }

  APP.playPracticeAudio = function (btn, audioFile) {
    const grade = GRADE_MAP[currentGradeId];
    const fullPath = `data/${grade.path}/${currentExamId}/${audioFile}`;
    const playerContainer = btn.closest('.fp-audio-player');
    const seekSlider = playerContainer ? playerContainer.querySelector('.fp-audio-seek') : null;
    const currentTimeEl = playerContainer ? playerContainer.querySelector('.fp-audio-current') : null;
    const durationEl = playerContainer ? playerContainer.querySelector('.fp-audio-duration') : null;

    // If same button clicked and already playing, pause
    if (_practiceAudio && _practiceAudioBtn === btn && !_practiceAudio.paused) {
      _practiceAudio.pause();
      btn.querySelector('.material-symbols-rounded').textContent = 'play_circle';
      btn.querySelector('.fp-audio-label').textContent = '🔊 再開';
      return;
    }

    // If same button, resume
    if (_practiceAudio && _practiceAudioBtn === btn && _practiceAudio.paused && _practiceAudio.currentTime > 0) {
      _practiceAudio.play();
      btn.querySelector('.material-symbols-rounded').textContent = 'pause_circle';
      btn.querySelector('.fp-audio-label').textContent = '⏸ 一時停止';
      return;
    }

    // Stop any existing audio
    if (_practiceAudio) {
      _practiceAudio.pause();
      _practiceAudio.currentTime = 0;
      if (_practiceAudioBtn) {
        _practiceAudioBtn.querySelector('.material-symbols-rounded').textContent = 'play_circle';
        _practiceAudioBtn.querySelector('.fp-audio-label').textContent = '🔊 音読用音声を再生';
        const oldPlayer = _practiceAudioBtn.closest('.fp-audio-player');
        if (oldPlayer) {
          const oldSeek = oldPlayer.querySelector('.fp-audio-seek');
          if (oldSeek) { oldSeek.value = 0; oldSeek.disabled = true; }
        }
      }
    }

    // Play new
    _practiceAudio = new Audio(fullPath);
    _practiceAudioBtn = btn;
    btn.querySelector('.material-symbols-rounded').textContent = 'pause_circle';
    btn.querySelector('.fp-audio-label').textContent = '⏸ 一時停止';
    
    // Setup seek bar updates
    if (seekSlider && currentTimeEl && durationEl) {
      seekSlider.disabled = false;
      
      _practiceAudio.addEventListener('loadedmetadata', () => {
        seekSlider.max = _practiceAudio.duration;
        durationEl.textContent = formatAudioTime(_practiceAudio.duration);
      });
      
      _practiceAudio.addEventListener('timeupdate', () => {
        if (!_isSeeking) {
          seekSlider.value = _practiceAudio.currentTime;
          currentTimeEl.textContent = formatAudioTime(_practiceAudio.currentTime);
        }
      });
    }

    _practiceAudio.addEventListener('ended', () => {
      btn.querySelector('.material-symbols-rounded').textContent = 'play_circle';
      btn.querySelector('.fp-audio-label').textContent = '🔊 もう一度再生';
      if (seekSlider) seekSlider.value = 0;
      _practiceAudio = null;
      _practiceAudioBtn = null;
    });

    _practiceAudio.play().catch(() => {
      btn.querySelector('.material-symbols-rounded').textContent = 'play_circle';
      btn.querySelector('.fp-audio-label').textContent = '❌ 音声なし';
    });
  };

  APP.seekPracticeAudio = function(slider) {
    _isSeeking = true;
    const playerContainer = slider.closest('.fp-audio-player');
    if (playerContainer) {
      const currentTimeEl = playerContainer.querySelector('.fp-audio-current');
      if (currentTimeEl) currentTimeEl.textContent = formatAudioTime(parseFloat(slider.value));
    }
  };

  APP.seekPracticeAudioEnd = function(slider) {
    if (_practiceAudio && _practiceAudioBtn === slider.closest('.fp-audio-player').querySelector('.fp-audio-btn')) {
      _practiceAudio.currentTime = parseFloat(slider.value);
    }
    _isSeeking = false;
  };

  // ===== HELPERS =====
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1));[a[i], a[j]] = [a[j], a[i]]; } return a; }
  function esc(s) { return s.replace(/'/g, "\\'").replace(/"/g, "&quot;"); }

  document.addEventListener('DOMContentLoaded', init);
})();
