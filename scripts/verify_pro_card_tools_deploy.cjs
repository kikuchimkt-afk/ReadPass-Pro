/* Verify only this navigation/QR commit, never mix in another app's homework. */
const {execFileSync}=require('node:child_process');
const {createHash}=require('node:crypto');
const assert=require('node:assert/strict');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const git=(...args)=>execFileSync('git',['-c','safe.directory='+root.replaceAll('\\','/'),'-C',root,...args],{maxBuffer:10*1024*1024});
const blob=(ref,file)=>git('show',ref+':'+file);
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const base=(process.argv[2]||'https://read-pass-pro.vercel.app').replace(/\/$/,'');
(async()=>{
  const changed=git('diff','--name-only','HEAD^','HEAD').toString().trim().split(/\r?\n/).sort();
  const allowed=['top.js','top.html','vocab-cards.html','pro-card-tools.js','pro-card-tools.css',
    'scripts/test_pro_card_tools.cjs','scripts/verify_pro_card_tools_deploy.cjs'].sort();
  assert.deepEqual(changed,allowed,'Only card navigation/QR paths may be committed');
  const catalog=bytes=>bytes.toString().match(/const EXAM_CATALOG = (\[[\s\S]*?\n    \]);/)[1];
  assert.equal(catalog(blob('HEAD','top.js')),catalog(blob('HEAD^','top.js')),'Exam entries must be untouched');
  const files=[...changed.filter(f=>!f.startsWith('scripts/')),
    'pro-landing.js','pro-theme.css','assets/pro-design/hero-05.webp','manifest.webmanifest',
    'app.js','print.js','print.css','data/homework/index.json','output/pdf/grammar_guides.json'];
  const commit=git('rev-parse','HEAD').toString().trim();
  const queue=[...files],errors=[];let matched=0;
  await Promise.all(Array.from({length:5},async()=>{
    while(queue.length){
      const file=queue.shift();
      try{
        const response=await fetch(base+'/'+file+'?verify='+commit,{signal:AbortSignal.timeout(30000)});
        if(!response.ok)throw Error('HTTP '+response.status);
        if(hash(Buffer.from(await response.arrayBuffer()))!==hash(blob('HEAD',file)))throw Error('SHA256 differs from committed blob');
        matched++;
      }catch(e){errors.push(file+': '+e.message);}
    }
  }));
  console.log('PRODUCTION '+matched+'/'+files.length+' card/design/integration assets match '+commit);
  errors.forEach(e=>console.error(e));if(errors.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
