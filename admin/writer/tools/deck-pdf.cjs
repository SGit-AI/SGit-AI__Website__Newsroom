const { chromium } = require('playwright');
(async()=>{const [,,html,pdf,png]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:900}});
await p.goto('file://'+html);await p.waitForTimeout(1500);
if(png){const els=await p.$$('section.slide');for(const i of [0,3,8,14]){await els[i].screenshot({path:png.replace('.png',`-${i+1}.png`)});}}
await p.emulateMedia({media:'print'});await p.pdf({path:pdf,width:'13.333in',height:'7.5in',printBackground:true});await b.close();})();
