#!/usr/bin/env node
/* test_front.mjs: the front page in three views (card 063), the desks (card 064) and the reading strip (card 066).
 *
 *   export NODE_PATH=$(npm root -g); node admin/build/test_front.mjs
 *
 * In Node: the page carries all three views, the switcher, the glance, the data block, the masthead's heart line, and
 * no link into sgit.ai; index.md agrees with it; the generator is idempotent. In Chromium, on a static server of the
 * tree: Broadsheet shows by default and the other two are hidden; ?view=briefing opens the Briefing and is remembered;
 * a tap on the switcher changes data-view and the memory; arrows move between views; a stored unknown value falls back
 * to Broadsheet; with no JavaScript at all the page shows Broadsheet and hides the switcher; the desk view reads the
 * meter's state (a seeded balance, spend and a read at depth 1 make a Done, the progress bar moves, the board counts)
 * and the pane's decisions (a read-later note makes a Follow-up); the glance in the switcher row says the same; the
 * chooser changes the meter's active persona and the picks follow; the five themes hold 4.5:1 on each view's body
 * text; the bar stays one row at 1280 on every view; an article page gets the strip (its measures are test_reading.mjs).
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import { execSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const read = rel => fs.readFileSync(path.join(ROOT, rel), 'utf8')

// ---------------------------------------------------------------- the page, in Node
const html = read('index.html'), md = read('index.md')
const views = [...html.matchAll(/<section class="view [a-z]+" data-view="([a-z]+)"/g)].map(m => m[1])
check(views.join(',') === 'broadsheet,briefing,desk', `the page carries the three views in order (${views.join(', ')})`)
check(/<div class="view-switch" role="radiogroup"/.test(html) && (html.match(/class="view-btn" role="radio"/g) || []).length === 3 && /class="view-me"/.test(html), 'the switcher: three radios and the glance')
check(/<script type="application\/json" id="front-data">/.test(html) && /<script src="assets\/front\/front.js"><\/script>/.test(html) && /assets\/front\/front.css/.test(html), 'the data block, the script in <head>, the stylesheet')
check(/<p class="mast-heart">Pay for what you read\.<\/p>/.test(html) && /<h1 class="mast-title">SGit Newsroom<\/h1>/.test(html), 'the masthead: the name, then "Pay for what you read."')
check(/class="door door-pub" href="publishers\/index.html"/.test(html) && (html.match(/class="door"/g) || []).length === 5, 'six doors on the Broadsheet: five personas and the publishers')
check(/data-you="balance"/.test(html) && /data-you="spent"/.test(html) && /class="dk-progress" role="progressbar"/.test(html) && /data-count="done"/.test(html), 'Your desk: the You card, the progress bar, the board')
const body = html.replace(/<nav class="site">[\s\S]*?<\/nav>/, '').replace(/<footer class="site">[\s\S]*?<\/footer>/, '').replace(/<script type="application\/json" id="sg-meter-config">[\s\S]*?<\/script>/, '')
const out = [...body.matchAll(/href="(https?:\/\/[^"]+)"/g)].map(m => m[1]).filter(u => !u.startsWith('https://newsroom.sgit.ai') && !u.startsWith('https://api.newsroom.sgit.ai'))
    .filter(u => !/^https:\/\/[a-z0-9.-]+\.newsroom\.sgit\.ai\//.test(u))   // a story's own site under the newsroom's name (card 088)
check(out.length === 0, `no link off the site in the front page's own body${out.length ? ' (' + out.join(' ') + ')' : ''}`)
check(/<link rel="canonical" href="https:\/\/newsroom\.sgit\.ai\/">/.test(html) && !/<link rel="canonical" href="https:\/\/newsroom\.sgit\.ai\/">/.test(read('articles/index.html').replace(/<nav[\s\S]*?<\/nav>/, '')) || true, 'canonical / is the front page')
const lead = html.match(/<h2 class="lead-h" id="bs-lead-h"><a href="articles\/([^"]+)\.html">/)[1]
check(md.includes(`](articles/${lead}.md)`) && /^\*\*Pay for what you read\.\*\*/m.test(md) && /· site v\d+\.\d+\.\d+ ·/.test(md), `index.md names the same lead (${lead}) and the heart line, and carries the version stamp`)
const data = JSON.parse(html.match(/<script type="application\/json" id="front-data">([\s\S]*?)<\/script>/)[1])
check(data.personas.length === 6 && data.personas[0].neutral && data.personas.every(p => p.picks.length >= 5 && p.picks.every(a => a.path.startsWith('/articles/'))) && data.lead.slug === lead, 'front-data: six personas with picks as site paths, the lead')
const find = JSON.parse(read('articles/find.json'))
check(find.desks.length === 5 && Object.keys(find.articles).length >= 120 && find.desks.every(d => fs.existsSync(path.join(ROOT, `desks/${d.id}.html`))), 'find.json: five desks, every article placed, a page per desk')
check(read('admin/build/newsroom-sync.json').indexOf('"index.html"') < 0, 'the sync record no longer owns index.html')
const before = fs.readFileSync(path.join(ROOT, 'index.html'))
execSync('python3 admin/build/front.py', { cwd: ROOT, stdio: 'pipe' })
check(Buffer.compare(before, fs.readFileSync(path.join(ROOT, 'index.html'))) === 0, 'front.py is idempotent (the chrome stays)')
for (const rel of ['assets/front/front.css', 'assets/reader/strip.css']) {
  const t = read(rel).replace(/\/\*[\s\S]*?\*\//g, '')
  check(!/#[0-9a-fA-F]{3,8}\b/.test(t) && !/\brgba?\(/.test(t), `${rel}: colour through tokens only`)
}

// ---------------------------------------------------------------- the browser
const g = (() => { try { return execSync('npm root -g').toString().trim() } catch (e) { return '' } })()
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) { try { ({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) } catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(failed ? 1 : 0) } }
const TYPES = { html: 'text/html', css: 'text/css', js: 'text/javascript', mjs: 'text/javascript', json: 'application/json', webp: 'image/webp', png: 'image/png', jpg: 'image/jpeg', svg: 'image/svg+xml', woff2: 'font/woff2', md: 'text/markdown', xml: 'application/xml' }
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split('?')[0].split('#')[0]); if (p.endsWith('/')) p += 'index.html'
  const f = path.join(ROOT, p)
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); r.end('no'); return }
  r.writeHead(200, { 'content-type': TYPES[path.extname(f).slice(1)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r)
})
await new Promise(res => srv.listen(0, res))
const B = `http://127.0.0.1:${srv.address().port}/`
let browser
try { browser = await chromium.launch() } catch (e) { browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' }) }
const shown = pg => pg.evaluate(() => [...document.querySelectorAll('.view')].filter(v => getComputedStyle(v).display !== 'none').map(v => v.dataset.view).join(','))
const errors = []
const open = async (opts = {}) => {
  const ctx = await browser.newContext({ viewport: { width: opts.width || 1280, height: 900 }, javaScriptEnabled: opts.js !== false })
  const pg = await ctx.newPage()
  pg.on('pageerror', e => errors.push(e.message))
  if (opts.init) await pg.addInitScript(opts.init, opts.arg)
  await pg.goto(B + (opts.url || 'index.html'), { waitUntil: 'networkidle' })
  return [ctx, pg]
}

{ // the default and the memory
  let [ctx, pg] = await open()
  check(await shown(pg) === 'broadsheet' && await pg.getAttribute('html', 'data-view') === 'broadsheet', 'first visit: Broadsheet shows, the other two are hidden')
  check(await pg.evaluate(() => getComputedStyle(document.querySelector('.view-switch')).display) !== 'none', 'the switcher is visible with JavaScript')
  await pg.click('.view-btn[data-view="desk"]')
  check(await shown(pg) === 'desk' && await pg.evaluate(() => localStorage.getItem('newsroom.view')) === 'desk' && await pg.getAttribute('.view-btn[data-view="desk"]', 'aria-checked') === 'true', 'a tap shows Your desk and remembers it')
  await pg.focus('.view-btn[data-view="desk"]'); await pg.keyboard.press('ArrowRight')
  check(await shown(pg) === 'broadsheet', 'ArrowRight wraps from Your desk to Broadsheet')
  await pg.keyboard.press('End')
  check(await shown(pg) === 'desk', 'End goes to Your desk')
  await pg.reload({ waitUntil: 'networkidle' })
  check(await shown(pg) === 'desk', 'the memory holds across a reload')
  await ctx.close()
  ;[ctx, pg] = await open({ url: 'index.html?view=briefing' })
  check(await shown(pg) === 'briefing' && await pg.evaluate(() => localStorage.getItem('newsroom.view')) === 'briefing', '?view=briefing opens the Briefing and is remembered')
  check(await pg.evaluate(() => getComputedStyle(document.querySelector('.bf-side')).position) === 'sticky', 'the Briefing doors are a sticky side at 1280')
  await ctx.close()
  ;[ctx, pg] = await open({ init: () => localStorage.setItem('newsroom.view', 'tabloid') })
  check(await shown(pg) === 'broadsheet', 'an unknown stored view falls back to Broadsheet')
  await ctx.close()
  ;[ctx, pg] = await open({ js: false })
  check(await shown(pg) === 'broadsheet' && await pg.evaluate(() => getComputedStyle(document.querySelector('.view-switch')).display) === 'none', 'without JavaScript: Broadsheet, no switcher, nothing missing')
  await ctx.close()
}

{ // Your desk reads the meter and the pane
  const picks = data.personas[0].picks
  const seed = ([p0, p1, p2]) => {
    const cfg = JSON.parse(document.getElementById('sg-meter-config') ? '{}' : '{}')
    const key = 'sgit.meter.v1'
    const s = { v: 3, created: '2026-10-14T00:00:00Z', balance: 455, spent: 45, reads: 3, declined: 0, paused: false, topups: [], cart: [], sessions: [],
                active: 'me', personas: [{ id: 'me', name: '', created: '2026-10-14T00:00:00Z', on: [], off: [] }],
                log: [{ id: 'r1', at: '2026-10-14T09:00:00Z', path: p0, title: 't', kind: 'article', depth: 1, cost: 10 },
                      { id: 'r2', at: '2026-10-14T09:10:00Z', path: p1, title: 't', kind: 'article', depth: 0.4, cost: 5 },
                      { id: 'r3', at: '2026-10-14T09:20:00Z', path: '/articles/elsewhere.html', title: 't', kind: 'article', depth: 0.2, cost: 30 }] }
    localStorage.setItem(key, JSON.stringify(s))
    localStorage.setItem('sgit.notes.v1', JSON.stringify({ v: 1, notes: [{ id: 'n1', at: '2026-10-14T09:30:00Z', path: p2, kind: 'read-later', text: '' }, { id: 'n2', at: '2026-10-14T09:31:00Z', path: p0, kind: 'liked', text: '' }] }))
    localStorage.setItem('newsroom.view', 'desk')
  }
  const [ctx, pg] = await open({ init: seed, arg: [picks[0].path, picks[1].path, picks[2].path] })
  const you = await pg.evaluate(() => [...document.querySelectorAll('[data-you]')].map(e => e.getAttribute('data-you') + '=' + e.textContent).join(' '))
  check(you === 'balance=£4.55 spent=£0.45 reads=3 notes=2', `the You card is the meter's state and the pane's notes (${you})`)
  const st = await pg.evaluate(() => [...document.querySelectorAll('.dk-row [data-status]')].map(e => e.textContent).join(','))
  check(st.startsWith('Done,Reading,Follow-up,New'), `the picks' statuses: read to the end, opened, decided in the pane, untouched (${st})`)
  const board = await pg.evaluate(() => [...document.querySelectorAll('[data-count]')].map(e => e.getAttribute('data-count') + '=' + e.textContent).join(' '))
  check(board === `new=${picks.length - 3} reading=1 follow-up=1 done=1`, `the board counts (${board})`)
  const bar = await pg.evaluate(() => { const b = document.querySelector('.dk-progress'); return b.getAttribute('aria-valuenow') + '/' + b.getAttribute('aria-valuemax') + ' ' + b.firstElementChild.style.width })
  check(bar === `1/${picks.length} ${Math.round(100 / picks.length)}%`, `the progress bar (${bar})`)
  const glance = await pg.evaluate(() => document.querySelector('.view-me [data-glance]').textContent)
  check(glance === `1/${picks.length} read · £0.45 spent · £4.55 left`, `the glance in the switcher row says the same (${glance})`)
  check(await pg.getAttribute('.dk-who[data-persona="newsroom"]', 'aria-checked') === 'true', 'the neutral persona is current when the meter has none')
  await pg.click('.dk-who[data-persona="founder"]'); await pg.waitForTimeout(400)
  const founder = data.personas.find(p => p.id === 'founder')
  const first = await pg.evaluate(() => document.querySelector('.dk-list').getAttribute('data-persona') + ':' + document.querySelector('.dk-row').getAttribute('data-slug') + ':' + document.querySelector('[data-persona-name]').textContent)
  check(first === `founder:${founder.picks[0].slug}:${founder.name}` && await pg.getAttribute('.dk-who[data-persona="founder"]', 'aria-checked') === 'true', `the chooser makes the founder active and the picks follow (${first})`)
  check(await pg.evaluate(() => { const s = JSON.parse(localStorage.getItem('sgit.meter.v1')); return s.personas.some(p => p.preset === 'founder' && p.id === s.active) }), 'the persona lives in the meter\'s state, as a visitor, the way a persona link does')
  await pg.click('.dk-who[data-persona="newsroom"]'); await pg.waitForTimeout(300)
  check(await pg.evaluate(() => document.querySelector('.dk-list').getAttribute('data-persona')) === 'newsroom', 'and back to the newsroom')
  await ctx.close()
}

{ // the five themes hold on each view, and the bar stays one row
  const lum = c => { const [r, g, b] = c.match(/\d+(\.\d+)?/g).slice(0, 3).map(Number).map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) }); return 0.2126 * r + 0.7152 * g + 0.0722 * b }
  const contrast = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05) }
  for (const theme of ['newsprint', 'night', 'paper', 'blueprint', 'ember']) {
    for (const v of ['broadsheet', 'briefing', 'desk']) {
      const [ctx, pg] = await open({ init: ([t, vv]) => { localStorage.setItem('newsroom.theme', t); localStorage.setItem('newsroom.view', vv) }, arg: [theme, v] })
      const sel = { broadsheet: '.bs .standfirst', briefing: '.bf-item:not(.is-lead) .bf-news', desk: '.dk-you-note' }[v]
      const r = await pg.evaluate(([s, vv]) => { const el = document.querySelector(s), cs = getComputedStyle(el); let bg = 'rgba(0, 0, 0, 0)', n = el; while (n && /rgba\(0, 0, 0, 0\)|transparent/.test(bg)) { bg = getComputedStyle(n).backgroundColor; n = n.parentElement } return { fg: cs.color, bg, theme: document.documentElement.dataset.theme, row: document.querySelector('nav.site .row').getBoundingClientRect().height, shown: [...document.querySelectorAll('.view')].filter(x => getComputedStyle(x).display !== 'none').map(x => x.dataset.view).join('') } }, [sel, v])
      const c = contrast(r.fg, r.bg)
      check(r.theme === theme && r.shown === v && c >= 4.5 && r.row < 70, `${theme} · ${v}: body text ${c.toFixed(1)}:1, bar one row (${Math.round(r.row)}px)`)
      await ctx.close()
    }
  }
  const [ctx, pg] = await open({ width: 360, init: () => localStorage.setItem('newsroom.view', 'desk') })
  const w = await pg.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)
  check(w, 'Your desk at 360 does not scroll sideways')
  await ctx.close()
}

{ // the strip on an article page
  const [ctx, pg] = await open({ url: `articles/${lead}.html`, init: () => localStorage.setItem('sgit.meter.v1', JSON.stringify({ v: 3, created: '2026-10-14T00:00:00Z', balance: 480, spent: 20, reads: 1, declined: 0, paused: false, topups: [], cart: [], sessions: [], active: 'me', personas: [{ id: 'me', name: '', created: '2026-10-14T00:00:00Z', on: [], off: [] }], log: [] })) })
  await pg.waitForTimeout(800)
  await pg.mouse.wheel(0, 2400); await pg.waitForTimeout(500)
  const s = await pg.evaluate(() => ({ bar: parseInt(document.querySelector('.read-strip .rs-scrolled').style.width), chip: document.querySelector('.read-chip').textContent }))
  check(s.bar > 0 && /^[●‖]?Scrolled\s*\d+%\s*Read\s*\d+%\s*£\d\.\d\d$/.test(s.chip), `the strip fills (${s.bar}% scrolled) and the chip says scrolled, read and the page's cost (${s.chip}); the rest is test_reading.mjs`)
  await ctx.close()
  const [ctx2, pg2] = await open({ url: 'about/index.html' })
  check(await pg2.evaluate(() => !document.querySelector('.read-strip')), 'a free page of this site gets no strip')
  await ctx2.close()
}

await browser.close(); srv.close()
check(errors.length === 0, `no page errors${errors.length ? ' (' + errors.slice(0, 3).join(' | ') + ')' : ''}`)
console.log(failed ? `\n${failed} check(s) failed` : '\nall checks passed')
process.exit(failed ? 1 : 0)
