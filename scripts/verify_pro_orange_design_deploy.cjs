/* Verify production bytes against the design commit, and keep homework intact. */
const {execFileSync}=require('node:child_process');
const {createHash}=require('node:crypto');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const git=(...args)=>execFileSync('git',['-c','safe.directory='+root.replaceAll('\\','/'),'-C',root,...args],{maxBuffer:10*1024*1024});
const blob=file=>git('show','HEAD:'+file);
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const base=(process.argv[2]||'https://read-pass-pro.vercel.app').replace(/\/$/,'');
(async()=>{
  const changed=git('diff','--name-only','HEAD^','HEAD').toString().trim().split(/\r?\n/);
  if(changed.some(f=>/^(data\/|output\/|print\.(js|css)$|app\.js$|top\.js$|scripts\/(build_homework|test_homework))/.test(f)))
    throw Error('The design commit contains unrelated assessment/homework changes');
  const files=[...changed.filter(f=>!f.startsWith('scripts/')),
    'app.js','top.js','print.js','print.css','data/homework/index.json','output/pdf/grammar_guides.json'];
  if(files.length!==35||new Set(files).size!==35)throw Error('Expected 35 distinct design/integration assets');
  const commit=git('rev-parse','HEAD').toString().trim();
  const queue=[...files],errors=[];let matched=0;
  await Promise.all(Array.from({length:5},async()=>{
    while(queue.length){
      const file=queue.shift();
      try{
        const response=await fetch(base+'/'+file+'?verify='+commit,{signal:AbortSignal.timeout(30000)});
        if(!response.ok)throw Error('HTTP '+response.status);
        if(hash(Buffer.from(await response.arrayBuffer()))!==hash(blob(file)))throw Error('SHA256 differs from committed blob');
        matched++;
      }catch(e){errors.push(file+': '+e.message);}
    }
  }));
  console.log('PRODUCTION '+matched+'/'+files.length+' committed assets match '+commit);
  errors.forEach(e=>console.error(e));if(errors.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
