/* Verify every production asset against committed Git blobs, not CRLF copies. */
const {execFileSync}=require('node:child_process');
const {createHash}=require('node:crypto');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const git=(...args)=>execFileSync('git',['-c',`safe.directory=${root.replaceAll('\\','/')}`,'-C',root,...args],{maxBuffer:10*1024*1024});
const blob=file=>git('show',`HEAD:${file}`);
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
const base=(process.argv[2]||'https://read-pass-pro.vercel.app').replace(/\/$/,'');

(async()=>{
  const commit=git('rev-parse','HEAD').toString().trim();
  const folder='data/grade4/2026-2-sat';
  const d=JSON.parse(blob(`${folder}/data.json`));
  const refs=[...d.sections.flatMap(s=>(s.questions||[]).map(q=>q.questionAudio)),
    ...d.vocabulary.flatMap(v=>[v.wordAudio,v.exampleAudio]),
    ...d.lessonPlan.focusPoints.flatMap(f=>[...f.examples.map(e=>e.audio),f.sourceQuoteAudio,f.practicePassage.audioFile])];
  const files=['app.js','index.html','style.css','top.js','top.html','print.js','print.html',`${folder}/data.json`,
    'output/pdf/ReadPass_EIKEN_Grade4_2026-2-sat_Practice_Exam_Large_Type_v1.pdf',...refs.map(ref=>`${folder}/${ref}`)];
  if(files.length!==114||new Set(files).size!==114)throw Error('Expected 114 unique committed production assets');
  const failures=[],queue=[...files];
  let matched=0;
  await Promise.all(Array.from({length:6},async()=>{
    while(queue.length){
      const file=queue.shift();
      try{
        const response=await fetch(`${base}/${file}?verify=${commit}`,{signal:AbortSignal.timeout(30000)});
        if(!response.ok)throw Error(`HTTP ${response.status}`);
        const bytes=Buffer.from(await response.arrayBuffer());
        if(sha(bytes)!==sha(blob(file)))throw Error('SHA256 differs from committed blob');
        if(file.endsWith('.pdf')&&!response.headers.get('content-type')?.includes('application/pdf'))throw Error('Wrong PDF content type');
        matched++;
      }catch(e){failures.push(`${file}: ${e.message}`);}
    }
  }));
  console.log(`PRODUCTION ${matched}/${files.length} committed assets match ${commit}`);
  failures.forEach(f=>console.error(f));
  if(failures.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
