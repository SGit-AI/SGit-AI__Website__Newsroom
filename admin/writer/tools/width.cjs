// NODE_PATH=$WRITER_NODE node width.cjs <absolute path to a built page>: the page's scroll width at a 390px phone viewport.
// 390 means no horizontal scroll; anything larger is a figure, table or code block that overflows.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 390, height: 800 } });
  await p.goto('file://' + process.argv[2]); console.log(await p.evaluate(() => document.documentElement.scrollWidth)); await b.close();
})();
