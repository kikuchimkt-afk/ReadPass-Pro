/**
 * ReadPass Pro — 過去問プリント生成
 * 級・年度・回を選んでA4の問題PDFを表示
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
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-2', label: '2026年度 第2回' }
            ]
        },
        {
            id: 'grade2', name: 'CEFR B1（2級相当）', nameEn: 'CSE 1980', icon: 'B1',
            color: '#4f8cff', colorRgb: '79, 140, 255', dataPath: 'grade2',
            exams: [
                { id: '2022-1', label: '2022年度 第1回' },
                { id: '2022-2', label: '2022年度 第2回' },
                { id: '2022-3', label: '2022年度 第3回' },
                { id: '2023-1', label: '2023年度 第1回' },
                { id: '2023-2', label: '2023年度 第2回' },
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-1-sat', label: '2024年度 第1回（土曜準会場）' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-2-sat', label: '2024年度 第2回（土曜準会場）' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2024-3-sat', label: '2024年度 第3回（土曜準会場）' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（土曜準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（土曜準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（土曜準会場）' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
            ]
        },
        {
            id: 'grade-pre2plus', name: 'CEFR A2（準2級プラス相当）', nameEn: 'CSE 1850', icon: 'A2+',
            color: '#8b5cf6', colorRgb: '139, 92, 246', dataPath: 'grade-pre2plus',
            exams: [
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（土曜準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（土曜準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（土曜準会場）' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
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
                { id: '2024-1-sat', label: '2024年度 第1回（土曜準会場）' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-1-sat', label: '2025年度 第1回（土曜準会場）' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-2-sat', label: '2025年度 第2回（土曜準会場）' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2025-3-sat', label: '2025年度 第3回（土曜準会場）' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
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
                { id: '2024-1-sat', label: '2024年度 第1回（土曜準会場）' },
                { id: '2024-2-sat', label: '2024年度 第2回（土曜準会場）' },
                { id: '2024-3-sat', label: '2024年度 第3回（土曜準会場）' },
                { id: '2025-1-sat', label: '2025年度 第1回（土曜準会場）' },
                { id: '2025-2-sat', label: '2025年度 第2回（土曜準会場）' },
                { id: '2025-3-sat', label: '2025年度 第3回（土曜準会場）' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
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
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
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
                { id: '2023-3', label: '2023年度 第3回' },
                { id: '2024-1', label: '2024年度 第1回' },
                { id: '2024-2', label: '2024年度 第2回' },
                { id: '2024-3', label: '2024年度 第3回' },
                { id: '2025-1', label: '2025年度 第1回' },
                { id: '2025-2', label: '2025年度 第2回' },
                { id: '2025-3', label: '2025年度 第3回' },
                { id: '2026-1', label: '2026年度 第1回' },
                { id: '2026-1-sat', label: '2026年度 第1回（土曜準会場）' },
                { id: '2026-2', label: '2026年度 第2回' },
                { id: '2026-2-sat', label: '2026年度 第2回（土曜準会場）' }
            ]
        }
    ];

    const BASE_URL = 'https://read-pass-pro.vercel.app/';
    const FIXED_EXAM_PDFS = {
        'pre-grade1/2021-1': {
            label: '英検準1級 2021年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2021-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2021-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2021-2': {
            label: '英検準1級 2021年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2021-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2021-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2021-3': {
            label: '英検準1級 2021年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2021-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2021-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2022-1': {
            label: '英検準1級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2022-2': {
            label: '英検準1級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2022-3': {
            label: '英検準1級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2023-1': {
            label: '英検準1級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2023-2': {
            label: '英検準1級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2023-3': {
            label: '英検準1級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'pre-grade1/2024-1': {
            label: '英検準1級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2024-2': {
            label: '英検準1級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2024-3': {
            label: '英検準1級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2025-1': {
            label: '英検準1級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2025-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2025-2': {
            label: '英検準1級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2025-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2025-3': {
            label: '英検準1級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2025-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2026-1': {
            label: '英検準1級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre1-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'pre-grade1/2026-2': {
            label: '英検準1級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre1_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-eiken-pre1-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre1_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade5/2021-1': {
            label: '英検5級 2021年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2021-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2021-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2021-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2021-2': {
            label: '英検5級 2021年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2021-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2021-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2021-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2021-3': {
            label: '英検5級 2021年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2021-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2021-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2021-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2022-1': {
            label: '英検5級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2022-2': {
            label: '英検5級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2022-3': {
            label: '英検5級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade5-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2023-1': {
            label: '英検5級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2023-2': {
            label: '英検5級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2023-3': {
            label: '英検5級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2024-1': {
            label: '英検5級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2024-2': {
            label: '英検5級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2024-3': {
            label: '英検5級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade5-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2025-1': {
            label: '英検5級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade5_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2025-2': {
            label: '英検5級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade5_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2025-3': {
            label: '英検5級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade5_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2026-1': {
            label: '英検5級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2026-1-sat': {
            label: '英検5級 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2026-2': {
            label: '英検5級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-grade5-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 6
        },
        'grade5/2026-2-sat': {
            label: '英検5級 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade5_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-grade5-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_Grade5_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 6,
        },
        'grade4/2022-1': {
            label: '英検4級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade4-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2022-2': {
            label: '英検4級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade4-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2022-3': {
            label: '英検4級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade4-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2023-1': {
            label: '英検4級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2023-2': {
            label: '英検4級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2023-3': {
            label: '英検4級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2024-1': {
            label: '英検4級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2024-2': {
            label: '英検4級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2024-3': {
            label: '英検4級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade4-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2025-1': {
            label: '英検4級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade4_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2025-2': {
            label: '英検4級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade4_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2025-3': {
            label: '英検4級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260912-eiken-grade45-2025-word-order-v2',
            downloadName: 'ReadPass_EIKEN_Grade4_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2026-1': {
            label: '英検4級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2026-1-sat': {
            label: '英検4級 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2026-2': {
            label: '英検4級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-grade4-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade4/2026-2-sat': {
            label: '英検4級 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade4_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-grade4-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_Grade4_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2022-1': {
            label: '英検2級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade2-2022-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2022-2': {
            label: '英検2級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260902-eiken-grade2-2022-2-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2022-3': {
            label: '英検2級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260902-eiken-grade2-2022-3-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2023-1': {
            label: '英検2級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2023-2': {
            label: '英検2級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2023-3': {
            label: '英検2級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 13
        },
        'grade2/2024-1': {
            label: '英検2級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2024-2': {
            label: '英検2級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2024-3': {
            label: '英検2級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-1': {
            label: '英検2級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-2': {
            label: '英検2級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-3': {
            label: '英検2級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade2-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2026-1': {
            label: '英検2級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade2-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2025-1': {
            label: '英検準2級プラス 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2plus-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2025-2': {
            label: '英検準2級プラス 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2plus-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2025-3': {
            label: '英検準2級プラス 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2plus-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2026-1': {
            label: '英検準2級プラス 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-pre2plus-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2/2021-1': {
            label: '英検準2級 2021年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2021-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2021-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2021-2': {
            label: '英検準2級 2021年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2021-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2021-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2021-3': {
            label: '英検準2級 2021年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2021-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2021-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2021-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2022-1': {
            label: '英検準2級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2022-2': {
            label: '英検準2級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2022-3': {
            label: '英検準2級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-pre2-2022-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2023-1': {
            label: '英検準2級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2023-2': {
            label: '英検準2級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2023-3': {
            label: '英検準2級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2023-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 12
        },
        'grade-pre2/2024-1': {
            label: '英検準2級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2024-2': {
            label: '英検準2級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2024-3': {
            label: '英検準2級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-2024-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-1': {
            label: '英検準2級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-2': {
            label: '英検準2級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-3': {
            label: '英検準2級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-pre2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2026-1': {
            label: '英検準2級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-pre2-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2022-1': {
            label: '英検3級 2022年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2022-1_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade3-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2022-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2022-2': {
            label: '英検3級 2022年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2022-2_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade3-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2022-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2022-3': {
            label: '英検3級 2022年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2022-3_Practice_Exam_Large_Type_v1.pdf?v=20260901-eiken-grade3-2022-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2022-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2023-1': {
            label: '英検3級 2023年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2023-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2023-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2023-2': {
            label: '英検3級 2023年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2023-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2023-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2023-3': {
            label: '英検3級 2023年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2023-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2023-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2023-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-1': {
            label: '英検3級 2024年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-1_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-2': {
            label: '英検3級 2024年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-2_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-3': {
            label: '英検3級 2024年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-3_Practice_Exam_Large_Type_v1.pdf?v=20260828-eiken-grade3-2024-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-3_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-1-sat': {
            label: '英検3級 2024年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-2-sat': {
            label: '英検3級 2024年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2024-3-sat': {
            label: '英検3級 2024年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2024-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2024-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2025-1': {
            label: '英検3級 2025年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-1_Practice_Exam_Large_Type_v3.pdf?v=20260828-eiken-blank-v3',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-1_Practice_Exam_Large_Type_v3.pdf',
            pages: 10
        },
        'grade3/2025-2': {
            label: '英検3級 2025年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-2_Practice_Exam_Large_Type_v3.pdf?v=20260828-eiken-blank-v3',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-2_Practice_Exam_Large_Type_v3.pdf',
            pages: 10
        },
        'grade3/2025-3': {
            label: '英検3級 2025年度 第3回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-3_Practice_Exam_Large_Type_v3.pdf?v=20260828-eiken-blank-v3',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-3_Practice_Exam_Large_Type_v3.pdf',
            pages: 10
        },
        'grade3/2025-1-sat': {
            label: '英検3級 2025年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2025-2-sat': {
            label: '英検3級 2025年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2025-3-sat': {
            label: '英検3級 2025年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2025-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2025-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2026-1': {
            label: '英検3級 2026年度 第1回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2026-1_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2026-1_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2026-1-sat': {
            label: '英検3級 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-grade345-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2026-2': {
            label: '英検3級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-grade3-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade3/2026-2-sat': {
            label: '英検3級 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade3_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-grade3-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_Grade3_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2024-1-sat': {
            label: '英検準2級 2024年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2024-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2024-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-1-sat': {
            label: '英検準2級 2025年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-2-sat': {
            label: '英検準2級 2025年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2025-3-sat': {
            label: '英検準2級 2025年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2025-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2025-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2026-1-sat': {
            label: '英検準2級 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20260829-eiken-pre2-2026-1-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2026-2': {
            label: '英検準2級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-pre2-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2/2026-2-sat': {
            label: '英検準2級 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-pre2-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 10
        },
        'grade-pre2plus/2025-1-sat': {
            label: '英検準2級プラス 2025年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2025-2-sat': {
            label: '英検準2級プラス 2025年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2025-3-sat': {
            label: '英検準2級プラス 2025年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2025-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2025-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2026-1-sat': {
            label: '英検準2級プラス 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2026-2': {
            label: '英検準2級プラス 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-pre2plus-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade-pre2plus/2026-2-sat': {
            label: '英検準2級プラス 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_GradePre2Plus_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-pre2plus-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_GradePre2Plus_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2024-1-sat': {
            label: '英検2級 2024年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2024-2-sat': {
            label: '英検2級 2024年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2024-3-sat': {
            label: '英検2級 2024年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2024-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2024-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-1-sat': {
            label: '英検2級 2025年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-2-sat': {
            label: '英検2級 2025年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2025-3-sat': {
            label: '英検2級 2025年度 第3回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2025-3-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2025-3-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2026-1-sat': {
            label: '英検2級 2026年度 第1回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2026-1-sat_Practice_Exam_Large_Type_v1.pdf?v=20261013-sat-venue-label-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2026-1-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2026-2': {
            label: '英検2級 2026年度 第2回',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2026-2_Practice_Exam_Large_Type_v1.pdf?v=20261013-grade2-2026-2-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2026-2_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        },
        'grade2/2026-2-sat': {
            label: '英検2級 2026年度 第2回（土曜準会場）',
            path: 'output/pdf/ReadPass_EIKEN_Grade2_2026-2-sat_Practice_Exam_Large_Type_v1.pdf?v=20261006-grade2-2026-2-sat-v1',
            downloadName: 'ReadPass_EIKEN_Grade2_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
            pages: 11
        }
    };

    // DOM
    const gradeChips = document.getElementById('gradeChips');
    const examCheckboxes = document.getElementById('examCheckboxes');
    const sectionCheckboxes = document.getElementById('sectionCheckboxes');
    const generateBtn = document.getElementById('generateBtn');
    const printBtn = document.getElementById('printBtn');
    const printPreview = document.getElementById('printPreview');
    const printContent = document.getElementById('printContent');
    const previewLabel = document.getElementById('previewLabel');
    const fixedExamNotice = document.getElementById('fixedExamNotice');
    const teacherMaterials = document.getElementById('teacherMaterials');
    const teacherMaterialList = document.getElementById('teacherMaterialList');

    let selectedGrade = null;
    let activeFixedExam = null;
    // Grammar guide PDFs built by scripts/build_grammar_guide_pdf.py --all.
    let grammarGuides = {};

    fetch('output/pdf/grammar_guides.json', { cache: 'no-cache' })
        .then(resp => (resp.ok ? resp.json() : {}))
        .then(manifest => {
            grammarGuides = manifest || {};
            renderTeacherMaterials();
        })
        .catch(err => console.warn('文法解説プリントの一覧を読み込めませんでした', err));

    // Homework prints validated and listed by scripts/build_homework.py.
    let homeworkIndex = {};

    fetch('data/homework/index.json', { cache: 'no-cache' })
        .then(resp => (resp.ok ? resp.json() : {}))
        .then(index => {
            homeworkIndex = index || {};
            renderTeacherMaterials();
            openHomeworkFromUrl();
        })
        .catch(err => console.warn('宿題プリントの一覧を読み込めませんでした', err));

    // Deep link from the top page's homework menu: print.html?grade=…&exam=…&homework=1
    // selects the grade and exam, then opens the homework dialog.
    function openHomeworkFromUrl() {
        const params = new URLSearchParams(location.search);
        const gradeId = params.get('grade');
        const examId = params.get('exam');
        if (params.get('homework') !== '1' || !homeworkIndex[`${gradeId}/${examId}`]) return;
        const grades = EXAM_CATALOG.filter(g => g.exams.length);
        const chip = gradeChips.querySelectorAll('.grade-chip')[grades.findIndex(g => g.id === gradeId)];
        if (!chip) return;
        chip.click();
        const box = [...examCheckboxes.querySelectorAll('input[type="checkbox"]')].find(cb => cb.value === examId);
        if (!box) return;
        box.checked = true;
        box.dispatchEvent(new Event('change'));
        teacherMaterials.scrollIntoView({ block: 'center' });
        openHomeworkDialog(examId);
    }

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
        clearGeneratedPreview();
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
            label.querySelector('input').addEventListener('change', () => {
                clearGeneratedPreview();
                updateGenerateBtn();
            });
            sectionCheckboxes.appendChild(label);
        });
    }

    // ===== Render Exam Checkboxes =====
    function renderExamCheckboxes(grade) {
        examCheckboxes.innerHTML = '';

        const toolbar = document.createElement('div');
        toolbar.className = 'exam-toolbar';

        const guide = document.createElement('p');
        guide.className = 'exam-guide';
        guide.textContent = '年度ごとに、印刷したい回を選択してください';
        toolbar.appendChild(guide);

        const allBtn = document.createElement('button');
        allBtn.className = 'select-all-btn';
        allBtn.type = 'button';
        allBtn.textContent = 'すべて選択';
        allBtn.addEventListener('click', () => {
            const boxes = examCheckboxes.querySelectorAll('input[type="checkbox"]');
            const allChecked = [...boxes].every(b => b.checked);
            boxes.forEach(b => { b.checked = !allChecked; });
            allBtn.textContent = allChecked ? 'すべて選択' : 'すべて解除';
            clearGeneratedPreview();
            updateGenerateBtn();
        });
        toolbar.appendChild(allBtn);
        examCheckboxes.appendChild(toolbar);

        const examsByYear = new Map();
        grade.exams.forEach(exam => {
            const match = exam.id.match(/^(\d{4})-([123])(?:-(.+))?$/);
            if (!match) return;

            const [, year, session, variant] = match;
            if (!examsByYear.has(year)) {
                examsByYear.set(year, { 1: [], 2: [], 3: [] });
            }
            examsByYear.get(year)[session].push({ exam, variant });
        });

        const tableWrap = document.createElement('div');
        tableWrap.className = 'exam-table-wrap';

        const table = document.createElement('table');
        table.className = 'exam-table';
        table.innerHTML = `
            <thead>
                <tr>
                    <th scope="col">年度</th>
                    <th scope="col">第1回</th>
                    <th scope="col">第2回</th>
                    <th scope="col">第3回</th>
                </tr>
            </thead>
        `;

        const tbody = document.createElement('tbody');
        [...examsByYear.entries()]
            .sort(([yearA], [yearB]) => Number(yearB) - Number(yearA))
            .forEach(([year, sessions]) => {
                const row = document.createElement('tr');

                const yearCell = document.createElement('th');
                yearCell.scope = 'row';
                yearCell.className = 'exam-year';
                yearCell.innerHTML = `<strong>${year}</strong><span>年度</span>`;
                row.appendChild(yearCell);

                ['1', '2', '3'].forEach(session => {
                    const cell = document.createElement('td');
                    const sessionExams = sessions[session]
                        .sort((a, b) => Number(Boolean(a.variant)) - Number(Boolean(b.variant)));

                    if (sessionExams.length === 0) {
                        cell.className = 'exam-unavailable';
                        cell.textContent = '—';
                    } else {
                        sessionExams.forEach(({ exam, variant }) => {
                            const label = document.createElement('label');
                            label.className = 'exam-option';
                            label.title = exam.label;

                            const venueLabel = variant
                                ? (variant === 'sat' ? '土曜準会場' : '準会場')
                                : '本会場';

                            label.innerHTML = `
                                <input type="checkbox" value="${exam.id}" aria-label="${exam.label}">
                                <span>${venueLabel}</span>
                            `;
                            label.querySelector('input').addEventListener('change', () => {
                                clearGeneratedPreview();
                                updateGenerateBtn();
                            });
                            cell.appendChild(label);
                        });
                    }

                    row.appendChild(cell);
                });

                tbody.appendChild(row);
            });

        table.appendChild(tbody);
        tableWrap.appendChild(table);
        examCheckboxes.appendChild(tableWrap);
    }

    function getFixedExam(examIds = getSelectedExams()) {
        if (!selectedGrade || examIds.length !== 1) return null;
        return FIXED_EXAM_PDFS[`${selectedGrade.id}/${examIds[0]}`] || null;
    }

    function clearGeneratedPreview() {
        activeFixedExam = null;
        printPreview.classList.remove('homework-mode');
        printPreview.style.display = 'none';
        printBtn.style.display = 'none';
        printBtn.textContent = '🖨️ 印刷する';
        previewLabel.textContent = 'プレビュー';
    }

    function setFixedExamMode(examPdf) {
        const controlledGroups = [
            sectionCheckboxes.closest('.setting-group'),
            document.querySelector('.option-toggles')?.closest('.setting-group')
        ].filter(Boolean);

        controlledGroups.forEach(group => {
            group.classList.toggle('fixed-mode-disabled', Boolean(examPdf));
            group.setAttribute('aria-disabled', examPdf ? 'true' : 'false');
            group.querySelectorAll('input').forEach(input => {
                input.disabled = Boolean(examPdf);
            });
        });

        if (!examPdf) {
            fixedExamNotice.hidden = true;
            fixedExamNotice.innerHTML = '';
            return;
        }

        fixedExamNotice.hidden = false;
        fixedExamNotice.innerHTML = `
            <strong>固定レイアウトの過去問PDFを使用します</strong>
            <span>${examPdf.label}の問題本文・設問・選択肢と、最終ページの正解一覧を収録したA4・${examPdf.pages}ページのPDFです。</span>
        `;
    }

    // ===== Update Generate Button =====
    function updateGenerateBtn() {
        const checkedExams = getSelectedExams();
        const checkedSections = getSelectedSections();
        const fixedExam = getFixedExam(checkedExams);
        setFixedExamMode(fixedExam);
        generateBtn.disabled = !selectedGrade
            || checkedExams.length === 0
            || (!fixedExam && checkedSections.length === 0);
        if (generateBtn.dataset.loading !== 'true') {
            generateBtn.textContent = fixedExam ? '過去問PDFを表示' : 'プリントを生成';
        }
        renderTeacherMaterials();
    }

    // ===== Materials per selected exam: past-exam PDF and grammar guide (閲覧 / DL), homework print (作成) =====
    function renderTeacherMaterials() {
        const rows = selectedGrade
            ? getSelectedExams()
                .map(examId => ({
                    examId,
                    fixed: FIXED_EXAM_PDFS[`${selectedGrade.id}/${examId}`],
                    guide: grammarGuides[`${selectedGrade.id}/${examId}`],
                    homework: homeworkIndex[`${selectedGrade.id}/${examId}`]
                }))
                .filter(row => row.fixed || row.guide || row.homework)
            : [];
        teacherMaterials.hidden = rows.length === 0;
        teacherMaterialList.innerHTML = rows.map(({ examId, fixed, guide, homework }) => {
            const examLabel = selectedGrade.exams.find(e => e.id === examId)?.label || examId;
            let html = '';
            if (fixed) {
                html += `
                <div class="teacher-material-row" data-fixed-exam="${esc(examId)}">
                    <div class="teacher-material-info">
                        <strong>過去問PDF（問題・正解一覧）</strong>
                        <span>${esc(examLabel)} ／ A4縦${fixed.pages}ページ（正解一覧は最終ページ）</span>
                    </div>
                    <div class="teacher-material-actions">
                        <a href="${esc(fixed.path)}" target="_blank" rel="noopener"
                           aria-label="${esc(examLabel)}の過去問PDFを閲覧">閲覧</a>
                        <a class="download" href="${esc(fixed.path)}" download="${esc(fixed.downloadName)}"
                           aria-label="${esc(examLabel)}の過去問PDFをダウンロード">DL</a>
                    </div>
                </div>`;
            }
            if (guide) {
                const pagesText = guide.pages === guide.focusPoints
                    ? `A4縦${guide.pages}枚（1枚に1つの文法事項）`
                    : `A4縦${guide.pages}枚（文法事項${guide.focusPoints}つ）`;
                html += `
                <div class="teacher-material-row" data-exam="${esc(examId)}">
                    <div class="teacher-material-info">
                        <strong>文法解説プリント（講師用）</strong>
                        <span>${esc(examLabel)} ／ ${pagesText}</span>
                    </div>
                    <div class="teacher-material-actions">
                        <a href="${esc(guide.path)}" target="_blank" rel="noopener"
                           aria-label="${esc(examLabel)}の文法解説プリントを閲覧">閲覧</a>
                        <a class="download" href="${esc(guide.path)}" download="${esc(guide.downloadName)}"
                           aria-label="${esc(examLabel)}の文法解説プリントをダウンロード">DL</a>
                    </div>
                </div>`;
            }
            if (homework) {
                html += `
                <div class="teacher-material-row homework-row" data-homework="${esc(examId)}">
                    <div class="teacher-material-info">
                        <strong>宿題プリント（${esc(homework.title)}）</strong>
                        <span>${esc(examLabel)} ／ A4縦4ページ（問題${homework.questions}問・うち全訳${homework.translations}問：問題2ページ・解答解説2ページ）</span>
                    </div>
                    <div class="teacher-material-actions">
                        <button type="button" class="homework-open" data-exam="${esc(examId)}"
                                aria-label="${esc(examLabel)}の宿題プリントを作成">作成</button>
                    </div>
                </div>`;
            }
            return html;
        }).join('');
    }

    function getSelectedExams() {
        return [...examCheckboxes.querySelectorAll('input[type="checkbox"]:checked')].map(cb => cb.value);
    }

    function getSelectedSections() {
        return [...sectionCheckboxes.querySelectorAll('input[type="checkbox"]:checked')].map(cb => cb.value);
    }

    // Section checkbox change
    sectionCheckboxes.querySelectorAll('input').forEach(cb => {
        cb.addEventListener('change', () => {
            clearGeneratedPreview();
            updateGenerateBtn();
        });
    });

    document.querySelectorAll('.option-toggles input').forEach(cb => {
        cb.addEventListener('change', clearGeneratedPreview);
    });

    // ===== Generate Print =====
    generateBtn.addEventListener('click', async () => {
        if (!selectedGrade) return;

        const examIds = getSelectedExams();
        const sectionTypes = getSelectedSections();
        const showChoices = document.getElementById('optChoices').checked;
        const showPassage = document.getElementById('optPassage').checked;
        const showQR = document.getElementById('optQR').checked;
        const fixedExam = getFixedExam(examIds);

        generateBtn.dataset.loading = 'true';
        generateBtn.textContent = fixedExam ? '過去問PDFを準備中...' : '読み込み中...';
        generateBtn.disabled = true;

        try {
            if (fixedExam) {
                renderFixedExam(fixedExam);
                delete generateBtn.dataset.loading;
                updateGenerateBtn();
                return;
            }

            activeFixedExam = null;
            printPreview.classList.remove('homework-mode');
            previewLabel.textContent = 'プレビュー';
            printBtn.textContent = '🖨️ 印刷する';
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
            delete generateBtn.dataset.loading;
            updateGenerateBtn();
            printPreview.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (err) {
            console.error(err);
            alert('データの読み込みに失敗しました: ' + err.message);
            delete generateBtn.dataset.loading;
            updateGenerateBtn();
        }
    });

    function renderFixedExam(examPdf) {
        activeFixedExam = examPdf;
        printPreview.classList.remove('homework-mode');
        printContent.innerHTML = `
            <section class="fixed-exam-card">
                <div class="fixed-exam-summary">
                    <span class="fixed-exam-badge">ReadPass 過去問演習</span>
                    <h2>${examPdf.label}</h2>
                    <p>A4・${examPdf.pages}ページ／モノクロ印刷用／正解は最終ページ</p>
                    <p class="fixed-exam-note">事前生成したPDFを使用するため、印刷する端末や回数によって問題の位置・改ページは変わりません。</p>
                    <div class="fixed-exam-actions">
                        <a href="${examPdf.path}" target="_blank" rel="noopener">PDFを開く</a>
                        <a href="${examPdf.path}" download="${examPdf.downloadName}">PDFを保存</a>
                    </div>
                </div>
                <iframe class="fixed-exam-frame" src="${examPdf.path}#view=FitH" title="${examPdf.label} 過去問PDF"></iframe>
            </section>
        `;
        previewLabel.textContent = 'ReadPass 過去問PDF';
        printPreview.style.display = '';
        printBtn.textContent = '過去問PDFを開く（印刷）';
        printBtn.style.display = '';
        printPreview.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // ===== Create Print Sheet =====
    function createPrintSheet(data, examLabel, examId, sectionTypes, showChoices, showPassage, showQR) {
        const sheet = document.createElement('div');
        sheet.className = 'print-sheet';

        // Header
        const header = document.createElement('div');
        header.className = 'sheet-header';
        header.innerHTML = `
            <div class="sheet-title">${selectedGrade.name} リーディング 問題プリント</div>
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

    function appendPassageContent(passageEl, passage, showPassage) {
        if (!showPassage) return;

        if (passage.format === 'multi-email' && Array.isArray(passage.emails)) {
            const emailsEl = document.createElement('div');
            emailsEl.className = 'print-email-list';
            emailsEl.innerHTML = passage.emails.map(email => {
                const meta = email.meta || email;
                const metaRows = [
                    ['From', meta.from],
                    ['To', meta.to],
                    ['Date', meta.date],
                    ['Subject', meta.subject],
                ].filter(([, value]) => value);
                return `<div class="print-email">
                    <div class="print-email-meta">${metaRows.map(([label, value]) => `<div><strong>${label}:</strong> ${esc(value)}</div>`).join('')}</div>
                    <div class="print-email-body">${esc(email.body || '').replace(/\n/g, '<br>')}</div>
                </div>`;
            }).join('');
            passageEl.appendChild(emailsEl);
            return;
        }

        if (passage.paragraphs) {
            const textEl = document.createElement('div');
            textEl.className = 'passage-text';
            textEl.innerHTML = passage.paragraphs.map(p => `<p>${esc(p)}</p>`).join('');
            passageEl.appendChild(textEl);
        }
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
            appendPassageContent(passageEl, passage, showPassage);

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
            appendPassageContent(passageEl, passage, showPassage);

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
            const prefixSpacer = q.framePrefix ? '<td></td>' : '';
            const suffixSpacer = q.frameSuffix ? '<td></td>' : '';
            const prefixCell = q.framePrefix
              ? `<td style="padding-right:4px;font-size:9pt;white-space:nowrap">${esc(q.framePrefix)}</td>`
              : '';
            const suffixCell = q.frameSuffix
              ? `<td style="padding-left:4px;font-size:9pt;white-space:nowrap">${esc(q.frameSuffix)}</td>`
              : '';

            let html = `<div class="q-number">(${q.number})</div>`;
            html += `<div class="q-text">${esc(q.text)}</div>`;
            if (q.words) {
                html += `<div style="font-size:9pt;margin:2px 0">${wordsLine}</div>`;
                html += `<table style="margin:2px 0 4px 0;border-collapse:collapse"><tr>${prefixSpacer}${slotLabelsRow}${suffixSpacer}</tr><tr>${prefixCell}${boxesRow}${suffixCell}</tr></table>`;
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

    // ===== Homework print: A4 portrait, exactly four pages =====
    // Pages 1-2: aim, goals and Part-1-style questions on the lesson's grammar (★ = also translate).
    // Pages 3-4: answer, translation, explanation, choice notes and a tutor's tip for every
    // question, a closing message, and the next lesson's flash-card QR (chosen in the dialog).
    // Items flow page by page by measured height, so longer grades simply use more of page 2/4.
    const EIKEN_NAMES = {
        'pre-grade1': '英検準1級', grade2: '英検2級', 'grade-pre2plus': '英検準2級プラス',
        'grade-pre2': '英検準2級', grade3: '英検3級', grade4: '英検4級', grade5: '英検5級'
    };
    const homeworkDialog = document.getElementById('homeworkDialog');
    const homeworkForm = document.getElementById('homeworkForm');
    const hwTarget = document.getElementById('hwTarget');
    const hwNextDate = document.getElementById('hwNextDate');
    const hwGradeOptions = document.getElementById('hwGradeOptions');
    const hwExamOptions = document.getElementById('hwExamOptions');
    const hwNoNext = document.getElementById('hwNoNext');
    let homeworkTarget = null;

    function examSortKey(id) {
        const m = String(id).match(/^(\d{4})-(\d+)(-.+)?$/);
        return m ? Number(m[1]) * 100 + Number(m[2]) * 10 + (m[3] ? 0 : 1) : 0;
    }

    function newestFirst(exams) {
        return [...exams].sort((a, b) => examSortKey(b.id) - examSortKey(a.id));
    }

    function isoDate(date) {
        const pad = n => String(n).padStart(2, '0');
        return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
    }

    function jaDate(iso) {
        const [y, m, d] = iso.split('-').map(Number);
        return `${m}月${d}日（${'日月火水木金土'[new Date(y, m - 1, d).getDay()]}）`;
    }

    function examTitle(grade, examId) {
        const label = grade.exams.find(e => e.id === examId)?.label || examId;
        return `${EIKEN_NAMES[grade.id] || grade.name} ${label}`;
    }

    function renderHomeworkExamOptions(gradeId, checkedId) {
        const grade = EXAM_CATALOG.find(g => g.id === gradeId);
        hwExamOptions.innerHTML = newestFirst(grade.exams).map(exam => `
            <label class="hw-radio">
                <input type="radio" name="hwExam" value="${esc(exam.id)}"${exam.id === checkedId ? ' checked' : ''}>
                <span>${esc(exam.label)}</span>
            </label>`).join('');
        syncHomeworkNext();
    }

    function syncHomeworkNext() {
        const off = hwNoNext.checked;
        [hwNextDate, ...hwGradeOptions.querySelectorAll('input'), ...hwExamOptions.querySelectorAll('input')]
            .forEach(input => { input.disabled = off; });
        homeworkDialog.classList.toggle('hw-next-off', off);
    }

    function openHomeworkDialog(examId) {
        homeworkTarget = { grade: selectedGrade, examId };
        hwTarget.textContent = examTitle(selectedGrade, examId);
        const nextWeek = new Date();
        nextWeek.setDate(nextWeek.getDate() + 7);
        hwNextDate.value = isoDate(nextWeek);
        hwNoNext.checked = false;
        hwGradeOptions.innerHTML = EXAM_CATALOG.filter(g => g.exams.length).map(grade => `
            <label class="hw-radio">
                <input type="radio" name="hwGrade" value="${esc(grade.id)}"${grade.id === selectedGrade.id ? ' checked' : ''}>
                <span>${esc(EIKEN_NAMES[grade.id] || grade.name)}</span>
            </label>`).join('');
        // Suggest the next older session of the same grade, the usual order of lessons.
        const ordered = newestFirst(selectedGrade.exams);
        const index = ordered.findIndex(e => e.id === examId);
        renderHomeworkExamOptions(selectedGrade.id, (ordered[index + 1] || ordered[0]).id);
        homeworkDialog.showModal();
    }

    hwGradeOptions.addEventListener('change', event => {
        if (event.target.name !== 'hwGrade') return;
        const grade = EXAM_CATALOG.find(g => g.id === event.target.value);
        renderHomeworkExamOptions(grade.id, newestFirst(grade.exams)[0].id);
    });
    hwNoNext.addEventListener('change', syncHomeworkNext);
    document.getElementById('hwCancel').addEventListener('click', () => homeworkDialog.close());

    teacherMaterialList.addEventListener('click', event => {
        const button = event.target.closest('.homework-open');
        if (button && selectedGrade) openHomeworkDialog(button.dataset.exam);
    });

    homeworkForm.addEventListener('submit', async event => {
        event.preventDefault();
        let next = null;
        if (!hwNoNext.checked) {
            const gradeId = homeworkForm.querySelector('input[name="hwGrade"]:checked')?.value;
            const examId = homeworkForm.querySelector('input[name="hwExam"]:checked')?.value;
            if (!hwNextDate.reportValidity() || !gradeId || !examId) return;
            const grade = EXAM_CATALOG.find(g => g.id === gradeId);
            next = {
                date: hwNextDate.value,
                title: examTitle(grade, examId),
                url: `${BASE_URL}vocab-cards.html?data=${encodeURIComponent(`data/${grade.dataPath}/${examId}/data.json`)}`
            };
        }
        homeworkDialog.close();
        await renderHomework(homeworkTarget, next);
    });

    async function renderHomework(target, next) {
        const entry = homeworkIndex[`${target.grade.id}/${target.examId}`];
        try {
            const resp = await fetch(entry.path, { cache: 'no-cache' });
            if (!resp.ok) throw new Error(`Failed to load ${entry.path}`);
            const hw = await resp.json();
            activeFixedExam = null;
            printContent.innerHTML = '';
            const pages = createHomeworkPages(hw, examTitle(target.grade, target.examId), next);
            printContent.appendChild(pages.wrap);
            printPreview.classList.add('homework-mode');
            previewLabel.textContent = '宿題プリント（A4縦4ページ：問題2・解答解説2）';
            printBtn.textContent = '🖨️ 宿題プリントを印刷';
            // The flow measures real layout, so the preview must be visible and fonts loaded.
            printPreview.style.display = '';
            printBtn.style.display = '';
            await document.fonts.ready;
            // A page group (questions / explanations) that does not fit gets up to two steps of
            // slightly smaller type and spacing; this also absorbs font differences between PCs.
            const flowGroup = (areas, items) => {
                if (flowHomeworkItems(areas, items)) return true;
                for (const step of ['hw-tight', 'hw-tighter']) {
                    areas.forEach(area => area.closest('.hw-page').classList.add(step));
                    if (flowHomeworkItems(areas, items)) return true;
                }
                return false;
            };
            const questionsFit = flowGroup(pages.questionAreas, pages.questionItems);
            const explanationsFit = flowGroup(pages.explanationAreas, pages.explanationItems);
            const fits = questionsFit && explanationsFit;
            pages.wrap.classList.toggle('hw-overflow', !fits);
            if (!fits) console.warn('宿題プリントが4ページに収まりません。問題数か解説の長さを見直してください。');
            await generateAllQRCodes();
            printPreview.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (err) {
            console.error(err);
            alert('宿題プリントの読み込みに失敗しました: ' + err.message);
        }
    }

    function homeworkPageOverflows(area) {
        const page = area.closest('.hw-page');
        return page.scrollHeight > page.clientHeight + 1;
    }

    // Fill the first page, then move the item that does not fit (and the rest) to the next.
    // A part heading left at the bottom of a page moves on with the item that follows it.
    function flowHomeworkItems(areas, items) {
        let index = 0;
        items.forEach(item => {
            areas[index].appendChild(item);
            while (homeworkPageOverflows(areas[index]) && index < areas.length - 1) {
                const heading = item.previousElementSibling;
                index += 1;
                if (heading && heading.classList.contains('hw-part')) areas[index].appendChild(heading);
                areas[index].appendChild(item);
            }
        });
        return areas.every(area => !homeworkPageOverflows(area));
    }

    function blankHtml(text) {
        return esc(text).replace('(　)', '<span class="hw-blank">(　　　　)</span>');
    }

    function htmlElement(html) {
        const template = document.createElement('template');
        template.innerHTML = html.trim();
        return template.content.firstElementChild;
    }

    function nextBlock(next) {
        return next ? `
                    <div class="hw-next">
                        <div class="hw-next-text">
                            <strong>次回の授業：${esc(jaDate(next.date))}</strong>
                            <span>${esc(next.title)}</span>
                            <span>QRコードを読み取って、次回の単語をフラッシュカードで予習しておきましょう。</span>
                        </div>
                        <div class="qr-container hw-qr" data-url="${esc(next.url)}" data-size="84"></div>
                    </div>` : '';
    }

    // Four-line handwriting guide (英語4線). `model` is printed in light grey for tracing.
    function fourLine(model = '') {
        return `<span class="hw-4line">${model ? `<span class="hw-4line-model">${esc(model)}</span>` : ''}<i></i><i></i><i></i></span>`;
    }

    function spellingHint(word) {
        return word.split(' ').map(part => part[0] + '_'.repeat(Math.max(part.length - 1, 1))).join(' ');
    }

    // Writing-heavy layout for Grade 3 and below: words, model sentences and ★ sentences are
    // written on four-line guides; pages 3-4 keep the same answer and explanation format.
    function createWritingPages(hw, title, next) {
        const wrap = document.createElement('div');
        wrap.className = 'hw-pages hw-layout-writing';
        const circled = n => '①②③④⑤⑥⑦⑧⑨⑩⑪⑫'[n - 1] || `(${n})`;
        const running = side => `
                <div class="hw-running"><span>${esc(title)}　${side}</span><span>テーマ：${esc(hw.theme)}</span></div>`;
        const star = q => (q.copy ? '<span class="hw-star" title="書き写し問題">★</span>' : '');
        const heading = (label, instruction) => htmlElement(`
                    <div class="hw-item hw-part"><h3 class="hw-h">${label}</h3><p class="hw-instruction">${esc(instruction)}</p></div>`);
        // One four-line row holds about 48 characters of a junior-high student's handwriting.
        const copyRows = text => (text.length > 48 ? 2 : 1);
        const questionItems = [
            heading('Part 1　単語を書こう', 'うすい字をなぞってから、右の4線に2回書きましょう。'),
            ...hw.words.map(w => htmlElement(`
                    <div class="hw-item hw-word">
                        <span class="hw-word-ja">${esc(w.meaning)}</span>
                        ${fourLine(w.word)}${fourLine()}${fourLine()}
                    </div>`)),
            heading('Part 2　例文を書き写そう', '授業で学んだ文です。意味を確かめてから、4線に書き写しましょう。'),
            ...hw.sentences.map((s, i) => htmlElement(`
                    <div class="hw-item hw-copy">
                        <p class="hw-copy-head"><span class="hw-q-num">${circled(i + 1)}</span><span class="hw-en hw-copy-en">${esc(s.en)}</span></p>
                        <p class="hw-copy-ja">${esc(s.ja)}　<span class="hw-copy-point">${esc(s.point)}</span></p>
                        <div class="hw-4lines">${Array.from({ length: copyRows(s.en) }, () => fourLine()).join('')}</div>
                    </div>`)),
            heading('Part 3　問題', hw.instruction),
            ...hw.questions.map(q => htmlElement(`
                    <div class="hw-item hw-q">
                        <p class="hw-q-stem"><span class="hw-q-num">(${q.number})</span>${star(q)}<span class="hw-en">${blankHtml(q.text)}</span></p>
                        <p class="hw-choices">${q.choices.map((c, i) => `<span><b>${i + 1}</b> <span class="hw-en">${esc(c)}</span></span>`).join('')}</p>
                        ${q.copy ? `<div class="hw-4lines">${Array.from({ length: copyRows(q.text) }, () => fourLine()).join('')}</div>` : ''}
                    </div>`)),
            htmlElement(`
                    <div class="hw-item hw-answer-row"><span class="hw-answer-label">Part 3 解答欄</span>${hw.questions.map(q => `<span><i>(${q.number})</i><b></b></span>`).join('')}</div>`),
            heading('Part 4　日本語を見て英語を書こう', '日本語の意味に合う英語を4線に書きましょう。最初の文字がヒントです。'),
            htmlElement(`
                    <div class="hw-item hw-spell">${hw.words.map((w, i) => `
                        <div class="hw-spell-cell"><span class="hw-spell-q"><span class="hw-q-num">${circled(i + 1)}</span>${esc(w.meaning)}<span class="hw-spell-hint">${esc(spellingHint(w.word))}</span></span>${fourLine()}</div>`).join('')}
                    </div>`)
        ];
        const explanationItems = [
            ...hw.questions.map(q => htmlElement(`
                <section class="hw-item hw-ex">
                    <p class="hw-ex-stem"><span class="hw-q-num">(${q.number})</span>${star(q)}<span class="hw-en">${blankHtml(q.text)}</span></p>
                    <p class="hw-correct">正解 ${q.answer}　<span class="hw-en">${esc(q.choices[q.answer - 1])}</span></p>
                    <p class="hw-ex-line"><span class="hw-label">訳：</span>${esc(q.translation)}</p>
                    <p class="hw-ex-line"><span class="hw-label">解説：</span>${esc(q.explanation)}</p>
                    <p class="hw-ex-notes">選択肢：${q.choiceNotes.map(esc).join('　/　')}</p>
                    <p class="hw-tip"><strong>講師のひとこと：</strong>${esc(q.tip)}</p>
                </section>`)),
            htmlElement(`
                <div class="hw-item hw-spell-key"><h3 class="hw-h">Part 4 の答え</h3><div>${hw.words.map((w, i) => `<span><span class="hw-q-num">${circled(i + 1)}</span>${esc(w.meaning)} → <b class="hw-en">${esc(w.word)}</b></span>`).join('')}</div></div>`),
            htmlElement(`
                <div class="hw-item hw-copy-key"><h3 class="hw-h">Part 2 例文のポイント</h3>${hw.sentences.map((s, i) => `
                    <p><span class="hw-q-num">${circled(i + 1)}</span><span class="hw-en">${esc(s.en)}</span><br><span class="hw-copy-note">${esc(s.note)}</span></p>`).join('')}</div>`),
            htmlElement(`
                <div class="hw-item hw-bottom">
                    <div class="hw-closing"><strong>講師から生徒へのひとこと</strong><p>${esc(hw.closing)}</p></div>${nextBlock(next)}
                </div>`)
        ];
        wrap.innerHTML = `
            <article class="hw-page hw-page-questions">
                ${running('宿題プリント')}
                <header class="hw-title">
                    <h2>${esc(title)}</h2>
                    <p>宿題プリント　${esc(hw.title)}</p>
                </header>
                <div class="hw-name-row"><span>名前</span><b class="hw-name"></b><span>提出日</span><b class="hw-date">${next ? esc(jaDate(next.date)) : '　　月　　日'}</b></div>
                <h3 class="hw-h">この宿題のねらい</h3>
                <p class="hw-aim">${esc(hw.aim)}</p>
                <ul class="hw-goals">${hw.goals.map(g => `<li>□ ${esc(g)}</li>`).join('')}</ul>
                <div class="hw-flow hw-questions"></div>
                <div class="hw-page-no">1</div>
            </article>
            <article class="hw-page hw-page-questions">
                ${running('宿題プリント')}
                <div class="hw-flow hw-questions"></div>
                <div class="hw-page-no">2</div>
            </article>
            <article class="hw-page hw-page-answers">
                ${running('解答・解説')}
                <div class="hw-key-row"><h3 class="hw-h">解答・解説（Part 3）</h3><div class="hw-key">${hw.questions.map(q => `<span><i>(${q.number})</i><b>${q.answer}</b></span>`).join('')}</div></div>
                <div class="hw-flow hw-ex-list"></div>
                <div class="hw-page-no">3</div>
            </article>
            <article class="hw-page hw-page-answers">
                ${running('解答・解説')}
                <div class="hw-flow hw-ex-list"></div>
                <div class="hw-page-no">4</div>
            </article>`;
        return {
            wrap,
            questionAreas: [...wrap.querySelectorAll('.hw-page-questions .hw-flow')],
            explanationAreas: [...wrap.querySelectorAll('.hw-page-answers .hw-flow')],
            questionItems,
            explanationItems
        };
    }

    function createHomeworkPages(hw, title, next) {
        if (hw.layout === 'writing') return createWritingPages(hw, title, next);
        const wrap = document.createElement('div');
        wrap.className = 'hw-pages';
        const running = side => `
                <div class="hw-running"><span>${esc(title)}　${side}</span><span>テーマ：${esc(hw.theme)}</span></div>`;
        const star = q => (q.translate ? '<span class="hw-star" title="全訳問題">★</span>' : '');
        const questionItems = hw.questions.map(q => htmlElement(`
                    <div class="hw-item hw-q">
                        <p class="hw-q-stem"><span class="hw-q-num">(${q.number})</span>${star(q)}<span class="hw-en">${blankHtml(q.text)}</span></p>
                        <p class="hw-choices">${q.choices.map((c, i) => `<span><b>${i + 1}</b> <span class="hw-en">${esc(c)}</span></span>`).join('')}</p>
                        ${q.translate ? '<div class="hw-write" aria-label="全訳を書く欄"><span></span><span></span><span></span></div>' : ''}
                    </div>`));
        questionItems.push(htmlElement(`
                    <div class="hw-item hw-answer-row"><span class="hw-answer-label">解答欄</span>${hw.questions.map(q => `<span><i>(${q.number})</i><b></b></span>`).join('')}</div>`));
        const explanationItems = hw.questions.map(q => htmlElement(`
                <section class="hw-item hw-ex">
                    <p class="hw-ex-stem"><span class="hw-q-num">(${q.number})</span>${star(q)}<span class="hw-en">${blankHtml(q.text)}</span></p>
                    <p class="hw-correct">正解 ${q.answer}　<span class="hw-en">${esc(q.choices[q.answer - 1])}</span></p>
                    <p class="hw-ex-line"><span class="hw-label">訳：</span>${esc(q.translation)}</p>
                    <p class="hw-ex-line"><span class="hw-label">解説：</span>${esc(q.explanation)}</p>
                    <p class="hw-ex-notes">選択肢：${q.choiceNotes.map(esc).join('　/　')}</p>
                    <p class="hw-tip"><strong>講師のひとこと：</strong>${esc(q.tip)}</p>
                </section>`));
        explanationItems.push(htmlElement(`
                <div class="hw-item hw-bottom">
                    <div class="hw-closing"><strong>講師から生徒へのひとこと</strong><p>${esc(hw.closing)}</p></div>${nextBlock(next)}
                </div>`));
        wrap.innerHTML = `
            <article class="hw-page hw-page-questions">
                ${running('宿題プリント')}
                <header class="hw-title">
                    <h2>${esc(title)}</h2>
                    <p>宿題プリント　${esc(hw.title)}</p>
                </header>
                <div class="hw-name-row"><span>名前</span><b class="hw-name"></b><span>提出日</span><b class="hw-date">${next ? esc(jaDate(next.date)) : '　　月　　日'}</b></div>
                <h3 class="hw-h">この宿題のねらい</h3>
                <p class="hw-aim">${esc(hw.aim)}</p>
                <ul class="hw-goals">${hw.goals.map(g => `<li>□ ${esc(g)}</li>`).join('')}</ul>
                <h3 class="hw-h">Part 1　短文の語句空所補充</h3>
                <p class="hw-instruction">${esc(hw.instruction)}</p>
                <div class="hw-flow hw-questions"></div>
                <div class="hw-page-no">1</div>
            </article>
            <article class="hw-page hw-page-questions">
                ${running('宿題プリント')}
                <div class="hw-flow hw-questions"></div>
                <div class="hw-page-no">2</div>
            </article>
            <article class="hw-page hw-page-answers">
                ${running('解答・解説')}
                <div class="hw-key-row"><h3 class="hw-h">解答・解説</h3><div class="hw-key">${hw.questions.map(q => `<span><i>(${q.number})</i><b>${q.answer}</b></span>`).join('')}</div></div>
                <div class="hw-flow hw-ex-list"></div>
                <div class="hw-page-no">3</div>
            </article>
            <article class="hw-page hw-page-answers">
                ${running('解答・解説')}
                <div class="hw-flow hw-ex-list"></div>
                <div class="hw-page-no">4</div>
            </article>`;
        return {
            wrap,
            questionAreas: [...wrap.querySelectorAll('.hw-page-questions .hw-flow')],
            explanationAreas: [...wrap.querySelectorAll('.hw-page-answers .hw-flow')],
            questionItems,
            explanationItems
        };
    }

    // ===== Generate QR Codes =====
    async function generateAllQRCodes() {
        const containers = printContent.querySelectorAll('.qr-container');
        for (const container of containers) {
            const url = container.dataset.url;
            const size = Number(container.dataset.size) || 80;
            try {
                new QRCode(container, {
                    text: url,
                    width: size,
                    height: size,
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
        if (activeFixedExam) {
            window.open(activeFixedExam.path, '_blank', 'noopener');
            return;
        }
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
