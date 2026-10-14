/* Lossy web encoding only: no retouching, cropping, compositing or AI substitutes.
 * The monogram is native SVG, and icon PNG/ICO variants are generated from it.
 */
const fs=require('node:fs/promises');
const path=require('node:path');
const sharp=require('sharp');
const root=path.resolve(__dirname,'..');
const sourceDir=process.argv[2];
if(!sourceDir)throw Error('Provide the built-in image generator output directory');
(async()=>{
  const manifest=JSON.parse(await fs.readFile(path.join(root,'assets/pro-design/sources.json'),'utf8'));
  for(const item of manifest.images){
    const output=path.join(root,item.output);
    await fs.mkdir(path.dirname(output),{recursive:true});
    await sharp(path.join(sourceDir,item.sourceFile)).webp({quality:85,effort:5}).toFile(output);
    console.log(item.output,(await fs.stat(output)).size);
  }
  const svg=await fs.readFile(path.join(root,'assets/icons/readpass-pro.svg'));
  const png=async(size,output)=>sharp(svg).resize(size,size).png().toFile(path.join(root,output));
  await png(16,'favicon-16.png');
  await png(32,'favicon-32.png');
  await png(180,'apple-touch-icon.png');
  await png(192,'assets/icons/readpass-pro-192.png');
  await png(512,'assets/icons/readpass-pro-512.png');
  const inset=await sharp(svg).resize(352,352).png().toBuffer();
  await sharp({create:{width:512,height:512,channels:4,background:'#202326'}})
    .composite([{input:inset,left:80,top:80}]).png().toFile(path.join(root,'assets/icons/readpass-pro-maskable-512.png'));
  const sizes=[16,32,48],frames=await Promise.all(sizes.map(n=>sharp(svg).resize(n,n).png().toBuffer()));
  const header=Buffer.alloc(6+16*frames.length);
  header.writeUInt16LE(1,2);header.writeUInt16LE(frames.length,4);
  let offset=header.length;
  frames.forEach((frame,i)=>{
    const n=6+i*16;header[n]=sizes[i];header[n+1]=sizes[i];
    header.writeUInt16LE(1,n+4);header.writeUInt16LE(32,n+6);
    header.writeUInt32LE(frame.length,n+8);header.writeUInt32LE(offset,n+12);offset+=frame.length;
  });
  await fs.writeFile(path.join(root,'favicon.ico'),Buffer.concat([header,...frames]));
  console.log('Design assets: 9 photographs + SVG/PNG/ICO home-screen icons');
})().catch(e=>{console.error(e);process.exitCode=1;});
