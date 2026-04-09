/**
 * ReadPass Pro — 宿題プリント生成
 * 級・試験・大問を選んでA4プリントを生成
 */
(function () {
    'use strict';

    // ===== EXAM CATALOG (same as top.js) =====
    const EXAM_CATALOG = [
        {
            id: 'pre-grade1', name: 'CEFR B2（準1級相当）', nameEn: 'CSE 2304', icon: 'B2',
            color: '#f59e0b', colorRgb: '245, 158, 11', dataPath: 'pre-grade1',
            exams: [
                { id: '2021-1', label: '2021年度 第1回' },
                { id: '2021-2', label: '2021年度 第2回' },
                { id: '2021-3', label: '2021年度 第3回' },
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-3', label: '2025年度 第3回' }
            ]
        },
        {
            id: 'grade2', name: 'CEFR B1（2級相当）', nameEn: 'CSE 1980', icon: 'B1',
            color: '#4f8cff', colorRgb: '79, 140, 255', dataPath: 'grade2',
            exams: [
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-1-sat', label: '2024年度 第1回（準会場）' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-2-sat', label: '2024年度 第2回（準会場）' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2024-3-sat', label: '2024年度 第3回（準会場）' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（準会場）' }
            ]
        },
        {
            id: 'grade-pre2plus', name: 'CEFR A2（準2級プラス相当）', nameEn: 'CSE 1850', icon: 'A2+',
            color: '#8b5cf6', colorRgb: '139, 92, 246', dataPath: 'grade-pre2plus',
            exams: [
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（準会場）' }
            ]
        },
        {
            id: 'grade-pre2', name: 'CEFR A2（準2級相当）', nameEn: 'CSE 1728', icon: 'A2',
            color: '#10b981', colorRgb: '16, 185, 129', dataPath: 'grade-pre2',
            exams: [
                { id: '2021-1', label: '2021年度 第1回' },
                { id: '2021-2', label: '2021年度 第2回' },
                { id: '2021-3', label: '2021年度 第3回' },
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（準会場）' }
            ]
        },
        {
            id: 'grade3', name: 'CEFR A1（3級相当）', nameEn: 'CSE 1456', icon: 'A1',
            color: '#f472b6', colorRgb: '244, 114, 182', dataPath: 'grade3',
            exams: [
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2024-1-sat', label: '2024年度 第1回（準会場）' },
                { id: '2024-2-sat', label: '2024年度 第2回（準会場）' },
                { id: '2024-3-sat', label: '2024年度 第3回（準会場）' },
                { id: '2025-1-sat', label: '2025年度 第1回（準会場）' },
                { id: '2025-2-sat', label: '2025年度 第2回（準会場）' },
                { id: '2025-3-sat', label: '2025年度 第3回（準会場）' }
            ]
        },
        {
            id: 'grade4', name: 'CEFR A1（4級相当）', nameEn: 'CSE 1180', icon: 'A1',
            color: '#a78bfa', colorRgb: '167, 139, 250', dataPath: 'grade4',
            exams: [
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' }
            ]
        },
        {
            id: 'grade5', name: '英検5級',
            color: '#f472b6', colorRgb: '244, 114, 182', dataPath: 'grade5',
            exams: [
                { id: '2021-1', label: '2021年度 第1回' },
                { id: '2021-2', label: '2021年度 第2回' },
                { id: '2021-3', label: '2021年度 第3回' },
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' }
            ]
        }
    ];

    const BASE_URL = 'https://read-pass-pro.vercel.app/';

    // DOM
    const gradeChips = document.getElementById('gradeChips');
    const examCheckboxes = document.getElementById('examCheckboxes');
    const sectionCheckboxes = document.getElementById('sectionCheckboxes');
    const generateBtn = document.getElementById('generateBtn');
    const printBtn = document.getElementById('printBtn');
    const printPreview = document.getElementById('printPreview');
    const printContent = document.getElementById('printContent');

    let selectedGrade = null;

    // ===== Render Grade Chips =====
    function renderGradeChips() {
        gradeChips.innerHTML = '';
        EXAM_CATALOG.forEach(grade => {
            if (grade.exams.length === 0) return;
            const chip = document.createElement('button');
            chip.className = 'grade-chip';
            chip.textContent = grade.name;
            chip.style.setProperty('--chip-color', grade.color);
            chip.addEventListener('click', () => selectGrade(grade, chip));
            gradeChips.appendChild(chip);
        });
    }

    function selectGrade(grade, chip) {
        selectedGrade = grade;
        document.querySelectorAll('.grade-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        renderExamCheckboxes(grade);
        renderSectionCheckboxes(grade);
        updateGenerateBtn();
    }

    // ===== Render Section Checkboxes (dynamic per grade) =====
    function renderSectionCheckboxes(grade) {
        const gid = grade.id;
        sectionCheckboxes.innerHTML = '';
        let items;
        if (gid === 'grade5') {
            // 5級: 大問1(vocabulary) + 大問2(会話vocabulary) + 大問3(語順整序)
            items = [
                { value: 'sec-0', label: '大問1（たん語・ぶんぽう）' },
                { value: 'sec-1', label: '大問2（会話）' },
                { value: 'sec-2', label: '大問3（ならべかえ）' }
            ];
        } else if (gid === 'grade4') {
            // 4級: 大問1(vocabulary) + 大問2(会話vocabulary) + 大問3(語順整序) + 大問4(読解)
            items = [
                { value: 'sec-0', label: '大問1（語彙・文法）' },
                { value: 'sec-1', label: '大問2（会話）' },
                { value: 'sec-2', label: '大問3（並べ替え）' },
                { value: 'sec-3', label: '大問4（長文読解）' }
            ];
        } else {
            // 3級以上: type-based (従来通り)
            items = [
                { value: 'vocabulary', label: '大問1（語彙・文法）' },
                { value: 'passage-fill', label: '大問2（空所補充）' },
                { value: 'sentence-order', label: '大問3（並べ替え）' },
                { value: 'reading-comprehension', label: '大問3/4（長文読解）' }
            ];
        }
        items.forEach(item => {
            const label = document.createElement('label');
            label.className = 'checkbox-label';
            label.innerHTML = `<input type="checkbox" value="${item.value}" checked> ${item.label}`;
            label.querySelector('input').addEventListener('change', updateGenerateBtn);
            sectionCheckboxes.appendChild(label);
        });
    }

    // ===== Render Exam Checkboxes =====
    function renderExamCheckboxes(grade) {
        examCheckboxes.innerHTML = '';
        const allBtn = document.createElement('button');
        allBtn.className = 'select-all-btn';
        allBtn.textContent = '全選択';
        allBtn.addEventListener('click', () => {
            const boxes = examCheckboxes.querySelectorAll('input[type="checkbox"]');
            const allChecked = [...boxes].every(b => b.checked);
            boxes.forEach(b => { b.checked = !allChecked; });
            allBtn.textContent = allChecked ? '全選択' : '全解除';
            updateGenerateBtn();
        });
        examCheckboxes.appendChild(allBtn);

        grade.exams.forEach(exam => {
            const label = document.createElement('label');
            label.className = 'exam-checkbox-label';
            label.innerHTML = `<input type="checkbox" value="${exam.id}"><span>${exam.label}</span>`;
            label.querySelector('input').addEventListener('change', updateGenerateBtn);
            examCheckboxes.appendChild(label);
        });
    }

    // ===== Update Generate Button =====
    function updateGenerateBtn() {
        const checkedExams = getSelectedExams();
        const checkedSections = getSelectedSections();
        generateBtn.disabled = !selectedGrade || checkedExams.length === 0 || checkedSections.length === 0;
    }

    function getSelectedExams() {
        return [...examCheckboxes.querySelectorAll('input[type="checkbox"]:checked')].map(cb => cb.value);
    }

    function getSelectedSections() {
        return [...sectionCheckboxes.querySelectorAll('input[type="checkbox"]:checked')].map(cb => cb.value);
    }

    // Section checkbox change
    sectionCheckboxes.querySelectorAll('input').forEach(cb => {
        cb.addEventListener('change', updateGenerateBtn);
    });

    // ===== Generate Print =====
    generateBtn.addEventListener('click', async () => {
        if (!selectedGrade) return;

        const examIds = getSelectedExams();
        const sectionTypes = getSelectedSections();
        const showChoices = document.getElementById('optChoices').checked;
        const showPassage = document.getElementById('optPassage').checked;
        const showQR = document.getElementById('optQR').checked;

        generateBtn.textContent = '読み込み中...';
        generateBtn.disabled = true;

        try {
            const examDataList = [];
            for (const examId of examIds) {
                const url = `data/${selectedGrade.dataPath}/${examId}/data.json`;
                const resp = await fetch(url);
                if (!resp.ok) throw new Error(`Failed to load ${url}`);
                const data = await resp.json();
                examDataList.push({ examId, data, label: selectedGrade.exams.find(e => e.id === examId)?.label || examId });
            }

            printContent.innerHTML = '';
            for (const { examId, data, label } of examDataList) {
                const sheet = createPrintSheet(data, label, examId, sectionTypes, showChoices, showPassage, showQR);
                printContent.appendChild(sheet);
            }

            if (showQR) {
                await generateAllQRCodes();
            }

            printPreview.style.display = '';
            printBtn.style.display = '';
            generateBtn.textContent = 'プリントを生成';
            generateBtn.disabled = false;
            printPreview.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (err) {
            console.error(err);
            alert('データの読み込みに失敗しました: ' + err.message);
            generateBtn.textContent = 'プリントを生成';
            generateBtn.disabled = false;
        }
    });

    // ===== Create Print Sheet =====
    function createPrintSheet(data, examLabel, examId, sectionTypes, showChoices, showPassage, showQR) {
        const sheet = document.createElement('div');
        sheet.className = 'print-sheet';

        // Header
        const header = document.createElement('div');
        header.className = 'sheet-header';
        header.innerHTML = `
            <div class="sheet-title">${selectedGrade.name} リーディング 宿題プリント</div>
            <div class="sheet-subtitle">${examLabel} 一次試験リーディング</div>
        `;
        sheet.appendChild(header);

        // Info row
        const infoRow = document.createElement('div');
        infoRow.className = 'sheet-info-row';
        infoRow.innerHTML = `
            <div>名前: <span class="name-field">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
            <div>日付: <span class="date-field">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
        `;
        sheet.appendChild(infoRow);

        // QR Code
        if (showQR) {
            const qrSection = document.createElement('div');
            qrSection.className = 'qr-section';
            const qrDiv = document.createElement('div');
            qrDiv.className = 'qr-container';
            qrDiv.dataset.url = `${BASE_URL}index.html?grade=${selectedGrade.id}&exam=${examId}`;
            qrSection.appendChild(qrDiv);
            const qrText = document.createElement('div');
            qrText.className = 'qr-text';
            qrText.innerHTML = `📱 QRコードをスマホ・タブレットで読み取って学習しましょう<br><strong>ReadPass Pro</strong> で問題を解いて自動採点できます`;
            qrSection.appendChild(qrText);
            sheet.appendChild(qrSection);
        }

        // Sections
        const allQuestions = [];

        if (!data.sections) { sheet.innerHTML += '<p>データにセクション情報がありません</p>'; return sheet; }

        data.sections.forEach((section, secIdx) => {
            // Filter: support both index-based (sec-0, sec-1...) and type-based filters
            const indexKey = `sec-${secIdx}`;
            const matchesIndex = sectionTypes.includes(indexKey);
            const matchesType = sectionTypes.includes(section.type);
            if (!matchesIndex && !matchesType) return;

            const sectionEl = document.createElement('div');
            sectionEl.className = 'section-block';

            // Section title
            const title = document.createElement('div');
            title.className = 'section-title';
            title.textContent = `${section.name}（${section.nameEn}）`;
            sectionEl.appendChild(title);

            // Section instruction
            if (section.instruction) {
                const instr = document.createElement('div');
                instr.className = 'section-instruction';
                instr.textContent = section.instruction;
                sectionEl.appendChild(instr);
            }

            // Type: vocabulary
            if (section.type === 'vocabulary') {
                renderVocabularySection(sectionEl, section, showChoices, allQuestions);
            }
            // Type: passage-fill
            else if (section.type === 'passage-fill') {
                renderPassageFillSection(sectionEl, section, showChoices, showPassage, allQuestions);
            }
            // Type: reading-comprehension
            else if (section.type === 'reading-comprehension') {
                renderReadingSection(sectionEl, section, showChoices, showPassage, allQuestions);
            }
            // Type: sentence-order
            else if (section.type === 'sentence-order') {
                renderSentenceOrderSection(sectionEl, section, showChoices, allQuestions);
            }

            sheet.appendChild(sectionEl);
        });

        // Answer Grid
        if (allQuestions.length > 0) {
            const gridSection = document.createElement('div');
            gridSection.className = 'answer-grid-section';
            gridSection.innerHTML = `<div class="answer-grid-title">解答欄</div>`;
            const grid = document.createElement('div');
            grid.className = 'answer-grid';

            allQuestions.forEach(q => {
                const numChoices = q.numChoices || 4;
                const cell = document.createElement('div');
                cell.className = 'answer-cell';
                let bubblesHtml = '';
                for (let i = 1; i <= numChoices; i++) {
                    bubblesHtml += `<div class="bubble">${i}</div>`;
                }
                cell.innerHTML = `<span class="answer-num">(${q.number})</span><div class="answer-bubbles">${bubblesHtml}</div>`;
                grid.appendChild(cell);
            });

            gridSection.appendChild(grid);
            sheet.appendChild(gridSection);
        }

        // Footer
        const footer = document.createElement('div');
        footer.className = 'sheet-footer';
        footer.textContent = '© ECCベストワン藍住：北島中央 — ReadPass Pro';
        sheet.appendChild(footer);

        return sheet;
    }

    // ===== Render Vocabulary Section =====
    function renderVocabularySection(container, section, showChoices, allQuestions) {
        section.questions.forEach(q => {
            allQuestions.push({ number: q.number, numChoices: q.choices ? q.choices.length : 4 });
            const block = document.createElement('div');
            block.className = 'q-block';

            let html = `<div class="q-number">(${q.number})</div>`;
            html += `<div class="q-text">${esc(q.text).replace(/\(\u3000\)/g, '(\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000)').replace(/\n/g, '<br>')}</div>`;

            if (showChoices && q.choices) {
                const isShort = q.choices.every(c => c.length < 20);
                html += `<div class="q-choices${isShort ? ' inline' : ''}">
                    ${q.choices.map((c, i) => `<div class="q-choice">${i + 1}. ${esc(c)}</div>`).join('')}
                </div>`;
            }

            block.innerHTML = html;
            container.appendChild(block);
        });
    }

    // ===== Render Passage-Fill Section =====
    function renderPassageFillSection(container, section, showChoices, showPassage, allQuestions) {
        if (!section.passages) return;

        section.passages.forEach(passage => {
            const passageEl = document.createElement('div');
            passageEl.className = 'passage-block';

            // Passage label & title
            let headerHtml = `<div class="passage-label">${passage.label || ''}${passage.title ? ' — ' + esc(passage.title) : ''}</div>`;
            passageEl.innerHTML = headerHtml;

            // Passage text
            if (showPassage && passage.paragraphs) {
                const textEl = document.createElement('div');
                textEl.className = 'passage-text';
                textEl.innerHTML = passage.paragraphs.map(p => `<p>${esc(p)}</p>`).join('');
                passageEl.appendChild(textEl);
            }

            // Questions
            if (passage.questions) {
                passage.questions.forEach(q => {
                    allQuestions.push({ number: q.number, numChoices: q.choices ? q.choices.length : 4 });
                    const block = document.createElement('div');
                    block.className = 'q-block';

                    let html = `<div class="q-number">(${q.number})</div>`;

                    if (showChoices && q.choices) {
                        html += `<div class="q-choices">
                            ${q.choices.map((c, i) => `<div class="q-choice">${i + 1}. ${esc(c)}</div>`).join('')}
                        </div>`;
                    }

                    block.innerHTML = html;
                    passageEl.appendChild(block);
                });
            }

            container.appendChild(passageEl);
        });
    }

    // ===== Render Reading Comprehension Section =====
    function renderReadingSection(container, section, showChoices, showPassage, allQuestions) {
        if (!section.passages) return;

        section.passages.forEach(passage => {
            const passageEl = document.createElement('div');
            passageEl.className = 'passage-block';

            // Passage label & title
            let headerHtml = `<div class="passage-label">${passage.label || ''}${passage.title ? ' — ' + esc(passage.title) : ''}</div>`;
            if (passage.title) {
                headerHtml += `<div class="passage-title">${esc(passage.title)}</div>`;
            }
            passageEl.innerHTML = headerHtml;

            // Passage text
            if (showPassage && passage.paragraphs) {
                const textEl = document.createElement('div');
                textEl.className = 'passage-text';
                textEl.innerHTML = passage.paragraphs.map(p => `<p>${esc(p)}</p>`).join('');
                passageEl.appendChild(textEl);
            }

            // Questions
            if (passage.questions) {
                passage.questions.forEach(q => {
                    allQuestions.push({ number: q.number, numChoices: q.choices ? q.choices.length : 4 });
                    const block = document.createElement('div');
                    block.className = 'q-block';

                    let html = `<div class="q-number">(${q.number})</div>`;

                    // Question text
                    if (q.question) {
                        html += `<div class="q-question-text">${esc(q.question)}</div>`;
                    }

                    if (showChoices && q.choices) {
                        html += `<div class="q-choices">
                            ${q.choices.map((c, i) => `<div class="q-choice">${i + 1}. ${esc(c)}</div>`).join('')}
                        </div>`;
                    }

                    block.innerHTML = html;
                    passageEl.appendChild(block);
                });
            }

            container.appendChild(passageEl);
        });
    }

    // ===== Render Sentence Order Section =====
    function renderSentenceOrderSection(container, section, showChoices, allQuestions) {
        const circled = ['\u2460','\u2461','\u2462','\u2463','\u2464'];
        section.questions.forEach(q => {
            allQuestions.push({ number: q.number, numChoices: q.choices ? q.choices.length : 4 });
            const block = document.createElement('div');
            block.className = 'q-block';

            const slots = q.answerSlots || [2, 4];
            const numWords = q.words ? q.words.length : 0;
            const wordsLine = q.words ? '\uff08 ' + q.words.map((w, i) => circled[i] + ' ' + w).join('\u3000') + ' \uff09' : '';
            const slotLabelsRow = Array.from({length: numWords}, (_, i) =>
              `<td style="text-align:center;font-size:7pt;color:#888;padding:0 2px">${slots.includes(i+1) ? (i+1)+'\u756a\u76ee' : ''}</td>`
            ).join('');
            const boxesRow = Array.from({length: numWords}, () =>
              `<td style="padding:0 1px"><div style="border:1px solid #666;height:18px;min-width:50px"></div></td>`
            ).join('');

            let html = `<div class="q-number">(${q.number})</div>`;
            html += `<div class="q-text">${esc(q.text)}</div>`;
            if (q.words) {
                html += `<div style="font-size:9pt;margin:2px 0">${wordsLine}${q.frameSuffix ? '\u3000' + esc(q.frameSuffix) : ''}</div>`;
                html += `<table style="margin:2px 0 4px 0;border-collapse:collapse"><tr>${slotLabelsRow}</tr><tr>${boxesRow}${q.frameSuffix ? `<td style="padding-left:4px;font-size:9pt">${esc(q.frameSuffix)}</td>` : ''}</tr></table>`;
            }

            if (showChoices && q.choices) {
                const isShort = q.choices.every(c => c.length < 20);
                html += `<div class="q-choices${isShort ? ' inline' : ''}">
                    ${q.choices.map((c, i) => `<div class="q-choice">${i + 1}. ${esc(c)}</div>`).join('')}
                </div>`;
            }

            block.innerHTML = html;
            container.appendChild(block);
        });
    }

    // ===== Generate QR Codes =====
    async function generateAllQRCodes() {
        const containers = printContent.querySelectorAll('.qr-container');
        for (const container of containers) {
            const url = container.dataset.url;
            try {
                new QRCode(container, {
                    text: url,
                    width: 80,
                    height: 80,
                    colorDark: '#1a1a1a',
                    colorLight: '#ffffff',
                    correctLevel: QRCode.CorrectLevel.M
                });
            } catch (e) {
                console.error('QR generation error:', e);
            }
        }
    }

    // ===== Print =====
    printBtn.addEventListener('click', () => {
        window.print();
    });

    // ===== Utility =====
    function esc(text) {
        if (!text) return '';
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    // ===== Init =====
    renderGradeChips();

})();
