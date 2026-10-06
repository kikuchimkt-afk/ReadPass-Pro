/* Compare production assets with COMMITTED blobs (not Windows CRLF copies). */
const {execFileSync} = require('node:child_process');
const {createHash} = require('node:crypto');
const path = require('node:path');
const root = path.resolve(__dirname,'..');
const git = (...args)=>execFileSync('git',['-c',`safe.directory=${root.replaceAll('\\','/')}`,'-C',root,...args],{maxBuffer:10*1024*1024});
const blob = file=>git('show',`HEAD:${file}`);
const sha = bytes=>createHash('sha256').update(bytes).digest('hex');
const base = (process.argv[2] || 'https://read-pass-pro.vercel.app').replace(/\/$/,'');

(async()=>{
  const commit=git('rev-parse','HEAD').toString().trim();
  const folder='data/grade-pre2/2026-2-sat';
  const d=JSON.parse(blob(`${folder}/data.json`));
  const files=['app.js','index.html','style.css','top.js','top.html','print.js','print.html',
    `${folder}/data.json`,
    'output/pdf/ReadPass_EIKEN_GradePre2_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',
    ...d.vocabulary.flatMap(v=>[`${folder}/${v.wordAudio}`,`${folder}/${v.exampleAudio}`]),
    ...d.lessonPlan.focusPoints.map(f=>`${folder}/${f.practicePassage.audioFile}`)];
  const failures=[];
  let matched=0;
  const queue=[...files];
  await Promise.all(Array.from({length:6},async()=>{
    while(queue.length){
      const file=queue.shift();
      try {
        const r=await fetch(`${base}/${file}?verify=${commit}`,{signal:AbortSignal.timeout(30000)});
        if(!r.ok) throw new Error(`HTTP ${r.status}`);
        const bytes=Buffer.from(await r.arrayBuffer());
        if(sha(bytes)!==sha(blob(file))) throw new Error('SHA256 differs from committed blob');
        if(file.endsWith('.pdf') && !r.headers.get('content-type')?.includes('application/pdf')) throw new Error('wrong PDF content type');
        matched++;
      } catch(error){failures.push(`${file}: ${error.message}`);}
    }
  }));
  console.log(`PRODUCTION ${matched}/${files.length} committed assets match ${commit}`);
  for(const failure of failures)console.error(failure);
  if(failures.length)process.exitCode=1;
})().catch(error=>{console.error(error);process.exitCode=1;});
