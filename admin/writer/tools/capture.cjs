// capture.cjs <targets.json> <outdir>
// targets.json: [{ "id": "garfield-law", "site": "https://www.garfield.law", "pages": ["https://...", ...] }]
// For each: a screenshot and the visible text of every page, robots.txt and llms.txt as fetched, and a manifest of
// sha256 hashes with the capture time. Pages are public marketing pages; nothing is submitted, no login is used.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
(async () => {
  const targets = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')), out = process.argv[3];
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 }, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36 newsroom.sgit.ai-evidence' });
  for (const t of targets) {
    const dir = path.join(out, t.id); fs.mkdirSync(dir, { recursive: true });
    const man = { id: t.id, site: t.site, captured_at: new Date().toISOString(), files: [] };
    const add = (name, buf, extra = {}) => { fs.writeFileSync(path.join(dir, name), buf); man.files.push({ name, bytes: buf.length, sha256: sha(buf), ...extra }); };
    for (const extra of ['robots.txt', 'llms.txt']) {
      try {
        const r = await fetch(new URL('/' + extra, t.site), { redirect: 'follow', signal: AbortSignal.timeout(20000) });
        const body = Buffer.from(await r.arrayBuffer());
        const ok = r.status === 200 && !/<html/i.test(body.slice(0, 400).toString());
        man[extra] = { status: r.status, url: r.url, present: ok };
        if (ok) add(extra, body, { url: r.url });
      } catch (e) { man[extra] = { status: 'error', error: String(e).slice(0, 120) }; }
    }
    let i = 0;
    for (const u of t.pages || [t.site]) {
      i++;
      const p = await ctx.newPage();
      try {
        const resp = await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await p.waitForTimeout(2500);
        const png = await p.screenshot({ fullPage: false });
        add(`page${i}.png`, png, { url: u, final_url: p.url(), status: resp ? resp.status() : null, title: (await p.title()).slice(0, 200) });
        const txt = Buffer.from((await p.evaluate(() => document.body ? document.body.innerText : '')).slice(0, 400000));
        add(`page${i}.txt`, txt, { url: u });
      } catch (e) { man.files.push({ name: `page${i}`, url: u, error: String(e).slice(0, 160) }); }
      await p.close();
    }
    fs.writeFileSync(path.join(dir, 'manifest.json'), JSON.stringify(man, null, 1));
    console.log(t.id, man.files.filter(f => !f.error).length, 'files', 'robots', man['robots.txt'] && man['robots.txt'].status, 'llms', man['llms.txt'] && man['llms.txt'].status);
  }
  await b.close();
})();
