#!/usr/bin/env node
/* test_reading.mjs: scrolled is not read (card 073), highlights (card 074), on a real article page.
 *
 *   export NODE_PATH=$(npm root -g); node admin/build/test_reading.mjs
 *
 * In Chromium, on a static server of the tree, with Playwright's clock so a minute of reading takes milliseconds:
 * a fast scroll gives a high scrolled and a low read; time on one section with the reader active raises read for
 * that section only; an idle reader and a hidden tab add nothing; scrolling up never lowers scrolled; the foot of
 * the page counts the last sections; a second visit adds to the first in sgit.reading.v1; the chip does not move
 * over a scroll and carries no balance; it opens the page's map and Escape closes it; a selection becomes a
 * highlight that is stored, drawn with the CSS Custom Highlight API, kept across a reload and removable; a free page
 * gets neither the strip nor the highlight button. The stylesheet's colours are checked by test_themes.mjs.
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import { execSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const SLUG = 'the-tokens-hook', PATH = `/articles/${SLUG}.html`

const g = (() => { try { return execSync('npm root -g').toString().trim() } catch (e) { return '' } })()
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) { try { ({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) } catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) } }
const TYPES = { html: 'text/html', css: 'text/css', js: 'text/javascript', mjs: 'text/javascript', json: 'application/json', webp: 'image/webp', png: 'image/png', jpg: 'image/jpeg', svg: 'image/svg+xml', woff2: 'font/woff2' }
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
const errors = []
const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } })
const open = async (url = PATH) => {
  const pg = await ctx.newPage(); pg.on('pageerror', e => errors.push(e.message))
  await pg.clock.install()
  await pg.goto(B + url.replace(/^\//, ''), { waitUntil: 'networkidle' })
  await pg.clock.runFor(1500)
  return pg
}
const R = pg => pg.evaluate(() => ({ scrolled: window.SgitReading.scrolled(), read: window.SgitReading.read(), sections: window.SgitReading.sections() }))
const scrollTo = (pg, y) => pg.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y)
// read a section: put it in the band and stay, moving the pointer every 10 seconds
const dwell = async (pg, secs, active = true) => { for (let t = 0; t < secs; t += 10) { if (active) await pg.mouse.move(300 + t % 50, 400); await pg.clock.runFor(10000) } }

{ // a fast scroll is scrolled, not read
  const pg = await open()
  const H = await pg.evaluate(() => document.documentElement.scrollHeight)
  for (let i = 1; i <= 10; i++) { await scrollTo(pg, Math.round(H * i / 11)); await pg.mouse.move(200, 200 + i); await pg.clock.runFor(400) }
  const r = await R(pg)
  check(r.sections.length >= 8 && r.sections[0].id === 'top', `the article is read as its sections (${r.sections.length}, from "${r.sections[0].label}")`)
  check(r.scrolled > 0.8 && r.read < 0.05, `a fast scroll: ${Math.round(r.scrolled * 100)}% scrolled, ${Math.round(r.read * 100)}% read`)
  const chip = await pg.evaluate(() => document.querySelector('.read-chip').textContent)
  check(/^Scrolled\s*\d+%\s*Read\s*\d+%\s*£\d\.\d\d$/.test(chip) && !/left/.test(chip), `the chip says scrolled, read and this page's cost, and no balance (${chip})`)
  await scrollTo(pg, 0); await pg.clock.runFor(1500)
  const up = await R(pg)
  check(up.scrolled >= r.scrolled, 'scrolling back to the top does not lower scrolled')
  await scrollTo(pg, H); await pg.clock.runFor(1500)
  const end = await R(pg)
  check(Math.round(end.scrolled * 100) === 100, `the foot of the page counts the last sections (${Math.round(end.scrolled * 100)}%)`)
  await pg.close()
}

let sec, needMs
{ // time on one section, active, raises that section only; idle and hidden add nothing
  await ctx.clearCookies(); const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => localStorage.clear()); await pg0.close()
  const pg = await open()
  sec = await pg.evaluate(() => { const h = [...document.querySelectorAll('main > h2')][3]; const r = h.getBoundingClientRect(); window.scrollTo({ top: window.scrollY + r.top - 140, behavior: 'instant' }); return h.id })
  await pg.clock.runFor(1200)
  const before = await R(pg)
  await dwell(pg, 60)
  const after = await R(pg)
  const s0 = before.sections.find(s => s.id === sec), s1 = after.sections.find(s => s.id === sec)
  needMs = s1.words / 300 * 60000
  const gained = s1.ms - s0.ms, others = after.sections.filter(s => s.id !== sec).reduce((a, s) => a + s.ms, 0) - before.sections.filter(s => s.id !== sec).reduce((a, s) => a + s.ms, 0)
  check(gained > 25000 && after.read > before.read, `a minute on "${s1.label}" while active: ${Math.round(gained / 1000)}s to it, read ${Math.round(before.read * 100)}% to ${Math.round(after.read * 100)}%`)
  check(gained + others <= 61000, `the minute is shared, not counted twice (${Math.round((gained + others) / 1000)}s in all)`)
  const idle0 = await R(pg)
  await dwell(pg, 180, false)
  const idle1 = await R(pg)
  const idleGain = idle1.sections.reduce((a, s) => a + s.ms, 0) - idle0.sections.reduce((a, s) => a + s.ms, 0)
  check(idleGain <= 61000 && idleGain >= 40000, `three idle minutes count only the first (${Math.round(idleGain / 1000)}s)`)
  await pg.evaluate(() => { Object.defineProperty(document, 'visibilityState', { configurable: true, get: () => 'hidden' }); document.dispatchEvent(new Event('visibilitychange')) })
  const h0 = await R(pg)
  await dwell(pg, 60)
  const h1 = await R(pg)
  check(h1.sections.reduce((a, s) => a + s.ms, 0) === h0.sections.reduce((a, s) => a + s.ms, 0), 'a hidden tab adds nothing, even with input')
  const stored = await pg.evaluate(p => JSON.parse(localStorage.getItem('sgit.reading.v1')).pages[p], PATH)
  check(stored && stored.visits === 1 && stored.sections.find(s => s.id === sec).ms >= 25000 && typeof stored.read === 'number', `kept in sgit.reading.v1: one visit, the section's time, the two measures`)
  await pg.close()
  const pg2 = await open()
  await pg2.evaluate(id => { const h = document.getElementById(id); const r = h.getBoundingClientRect(); window.scrollTo({ top: window.scrollY + r.top - 140, behavior: 'instant' }) }, sec)
  await pg2.clock.runFor(1200)
  await dwell(pg2, 30)
  await pg2.evaluate(() => window.SgitReading.save())
  const again = await pg2.evaluate(p => JSON.parse(localStorage.getItem('sgit.reading.v1')).pages[p], PATH)
  const ms2 = again.sections.find(s => s.id === sec).ms
  check(again.visits === 2 && ms2 >= stored.sections.find(s => s.id === sec).ms + 15000, `a second visit adds to the first (${Math.round(ms2 / 1000)}s on the section, ${again.visits} visits)`)
  // the chip does not move
  const H = await pg2.evaluate(() => document.documentElement.scrollHeight), lefts = new Set()
  for (let i = 1; i <= 20; i++) { await scrollTo(pg2, Math.round(H * i / 21)); await pg2.mouse.move(100, 100 + i); await pg2.clock.runFor(1100); lefts.add(await pg2.evaluate(() => Math.round(document.querySelector('.read-chip').getBoundingClientRect().left))) }
  check(lefts.size === 1, `the chip holds still over twenty scroll steps (${lefts.size} position${lefts.size === 1 ? '' : 's'})`)
  await pg2.click('.read-chip')
  const map = await pg2.evaluate(() => ({ open: !document.querySelector('.read-map').hidden, rows: document.querySelectorAll('.read-map .rm-list li').length, exp: document.querySelector('.read-chip').getAttribute('aria-expanded') }))
  const n = (await R(pg2)).sections.length
  check(map.open && map.rows === n && map.exp === 'true', `the chip opens the page as its sections (${map.rows} rows)`)
  await pg2.keyboard.press('Escape')
  check(await pg2.evaluate(() => document.querySelector('.read-map').hidden), 'Escape closes it')
  await pg2.close()
}

{ // highlights
  const pg = await open()
  const exact = await pg.evaluate(() => {
    const h = [...document.querySelectorAll('main > h2')][4]; let el = h.nextElementSibling; while (el && el.tagName !== 'P') el = el.nextElementSibling
    el.scrollIntoView({ block: 'center', behavior: 'instant' })
    const t = document.createTreeWalker(el, NodeFilter.SHOW_TEXT).nextNode(), end = Math.min(t.data.length, 60)
    const r = document.createRange(); r.setStart(t, 0); r.setEnd(t, end); const s = getSelection(); s.removeAllRanges(); s.addRange(r)
    return r.toString()
  })
  await pg.clock.runFor(400)
  check(await pg.evaluate(() => { const b = document.querySelector('.hl-btn'); return !b.hidden && b.textContent === 'Highlight' }), 'a selection in the article offers Highlight')
  await pg.click('.hl-btn')
  const kept = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.highlights.v1')).items)
  check(kept.length === 1 && kept[0].exact === exact && kept[0].path === '/articles/the-tokens-hook.html' && kept[0].section && kept[0].prefix !== undefined, `kept as a quote with its context and section ("${exact.slice(0, 40)}…", ${kept[0] && kept[0].section})`)
  const drawn = () => pg.evaluate(() => !!(window.CSS && CSS.highlights && CSS.highlights.get('sgit-highlight') && CSS.highlights.get('sgit-highlight').size))
  check(await drawn(), 'drawn with the CSS Custom Highlight API')
  check(await pg.evaluate(t => document.querySelector('main').textContent.includes(t) && !document.querySelector('main mark'), exact), 'the page itself is not changed')
  await pg.reload({ waitUntil: 'networkidle' }); await pg.clock.runFor(1500)
  check(await drawn(), 'still there after a reload')
  const box = await pg.evaluate(() => { const x = window.SgitHighlights.forPage()[0]; const ix = document.querySelector('main'); const r = [...CSS.highlights.get('sgit-highlight')][0]; r.startContainer.parentElement.scrollIntoView({ block: 'center', behavior: 'instant' }); const q = r.getClientRects()[0]; return { x: q.left + 5, y: q.top + q.height / 2 } })
  await pg.mouse.click(box.x, box.y); await pg.clock.runFor(200)
  check(await pg.evaluate(() => document.querySelector('.hl-btn').textContent === 'Remove highlight' && !document.querySelector('.hl-btn').hidden), 'a tap on it offers Remove highlight')
  await pg.click('.hl-btn')
  check(await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.highlights.v1')).items.length === 0) && !(await drawn()), 'and removes it from the store and the page')
  await pg.close()
}

{ // a free page of this site gets neither
  const pg = await open('about/index.html')
  check(await pg.evaluate(() => !document.querySelector('.read-chip') && !document.querySelector('.hl-btn') && !window.SgitReading), 'a free page gets no strip and no highlight button')
  await pg.close()
}

await browser.close(); srv.close()
check(errors.length === 0, `no page errors${errors.length ? ' (' + errors.slice(0, 3).join(' | ') + ')' : ''}`)
console.log(failed ? `\n${failed} check(s) failed` : '\nall checks passed')
process.exit(failed ? 1 : 0)
