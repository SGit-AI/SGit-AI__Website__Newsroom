#!/usr/bin/env node
/* test_reading.mjs: scrolled is not read (card 073), highlights (card 074), the reader's controls (card 081),
 * what has been read shown on the page (card 082) and the meter charging by what was read (card 080), on a real article page.
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
  check(/^[●‖✓]?Scrolled\s*\d+%\s*Read\s*\d+%\s*£\d\.\d\d$/.test(chip) && !/left/.test(chip), `the chip says scrolled, read and this page's cost, and no balance (${chip})`)
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

{ // the reader's controls: pause (kept across a reload), reset, a section marked read or unread (card 081)
  const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => localStorage.clear()); await pg0.close()
  let pg = await open()
  const sec = await pg.evaluate(() => { const h = [...document.querySelectorAll('main > h2')][2]; const r = h.getBoundingClientRect(); window.scrollTo({ top: window.scrollY + r.top - 140, behavior: 'instant' }); return h.id })
  await pg.clock.runFor(1200)
  await pg.click('.read-chip')
  await pg.click('.read-map [data-act="pause"]')
  check(await pg.evaluate(() => localStorage.getItem('sgit.reading.paused') === '1' && document.querySelector('.read-chip').classList.contains('is-paused') && document.querySelector('.read-chip [data-k="state"]').textContent === '‖'), 'Pause: kept in this browser, and the chip says so')
  const p0 = await R(pg); await dwell(pg, 60); const p1 = await R(pg)
  check(p1.sections.reduce((a, s) => a + s.ms, 0) === p0.sections.reduce((a, s) => a + s.ms, 0), 'paused, a minute of reading adds nothing')
  await pg.reload({ waitUntil: 'networkidle' }); await pg.clock.runFor(1500)
  check(await pg.evaluate(() => window.SgitReading.paused() && document.querySelector('.read-chip').classList.contains('is-paused')), 'still paused after a reload')
  await pg.evaluate(() => window.SgitReading.setPaused(false))
  await pg.evaluate(id => { const h = document.getElementById(id); const r = h.getBoundingClientRect(); window.scrollTo({ top: window.scrollY + r.top - 140, behavior: 'instant' }) }, sec)
  await pg.clock.runFor(1200); await dwell(pg, 60)
  check((await R(pg)).sections.find(s => s.id === sec).ms > 25000, 'resumed, reading counts again')
  await pg.click('.read-chip')
  const unread = await pg.evaluate(() => window.SgitReading.sections().find(s => s.state !== 'read').id)
  await pg.click(`.read-map [data-mark="read"][data-id="${unread}"]`)
  let s = (await R(pg)).sections.find(x => x.id === unread)
  check(s.state === 'read' && s.mark === 'read', `a section marked read by hand counts as read (${unread})`)
  await pg.click(`.read-map [data-mark="unread"][data-id="${unread}"]`)
  s = (await R(pg)).sections.find(x => x.id === unread)
  check(s.ms === 0 && s.mark === 'unread', 'and marked unread, its time goes back to zero')
  const events = []
  await pg.exposeFunction('__ev', d => events.push(d))
  await pg.evaluate(() => window.addEventListener('sgit-reading', e => window.__ev(e.detail)))
  await pg.click('.read-map [data-act="reset"]')
  const after = await R(pg)
  check(after.read === 0 && after.scrolled === 0 && events.some(e => e.reset === true), 'Reset: the page is unread again, and the meter is told (reset: true)')
  const stored = await pg.evaluate(p => JSON.parse(localStorage.getItem('sgit.reading.v1')).pages[p].sections.every(x => x.ms === 0), PATH)
  check(stored, 'the reset is kept')
  await pg.close()
}

{ // what has been read, on the page: never while reading forward; a pass after a scroll back up, once the page is still; on a return (cards 082, 084)
  const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => localStorage.clear()); await pg0.close()
  let pg = await (async () => { const p = await ctx.newPage(); p.on('pageerror', e => errors.push(e.message)); await p.addInitScript(() => localStorage.setItem('sgit.reading.view', 'line')); await p.clock.install(); await p.goto(B + PATH.slice(1), { waitUntil: 'networkidle' }); await p.clock.runFor(1500); return p })()
  const secs = (await R(pg)).sections
  for (const s of secs.slice(0, 4)) await pg.evaluate(id => window.SgitReading.mark(id, 'read'), s.id)
  const H = await pg.evaluate(() => document.documentElement.scrollHeight)
  for (let i = 1; i <= 6; i++) { await scrollTo(pg, Math.round(H * i / 10)); await pg.clock.runFor(1500) }
  check(await pg.evaluate(() => !window.SgitFolds.active() && !document.querySelector('.rf-fold, .rf-gone')), 'reading forward: nothing folds, however long the reader stops')
  let y = await pg.evaluate(() => window.scrollY)
  // the reader scrolls back up and keeps scrolling: nothing changes while the page moves
  for (let i = 1; i <= 8; i++) { await scrollTo(pg, y - i * 150); await pg.clock.runFor(300) }
  check(await pg.evaluate(() => !document.querySelector('.rf-fold')), 'scrolling back up: nothing changes while the page is still moving')
  await pg.clock.runFor(1200)
  check(await pg.evaluate(() => window.SgitFolds.active() && document.querySelectorAll('.rf-fold').length > 0 && !document.querySelector('.read-bar')), 'once the page is still, the sections read above fold, and no bar appears')
  await pg.close()
  // a return visit, in each view
  for (const [mode, expect] of [['full', 'nothing'], ['margin', 'marks'], ['fade', 'faded'], ['para', 'folds'], ['line', 'folds'], ['hide', 'marker']]) {
    pg = await ctx.newPage(); pg.on('pageerror', e => errors.push(e.message))
    await pg.addInitScript(m => localStorage.setItem('sgit.reading.view', m), mode)
    await pg.clock.install(); await pg.goto(B + PATH.slice(1), { waitUntil: 'networkidle' }); await pg.clock.runFor(2500)
    const r = await pg.evaluate(() => ({ folds: document.querySelectorAll('.rf-fold:not(.rf-hidden-run)').length, run: document.querySelectorAll('.rf-hidden-run').length, gone: document.querySelectorAll('.rf-gone').length, marks: document.querySelectorAll('.rf-m.rf-done').length, faded: document.querySelectorAll('.rf-fade').length, line: (document.querySelector('.rf-fold .rf-l') || {}).textContent || '', para: (document.querySelector('.rf-fold .rf-p') || {}).textContent || '' }))
    const ok = { nothing: r.folds + r.marks + r.faded + r.gone === 0, marks: r.marks > 0 && r.gone === 0 && r.faded === 0, faded: r.faded > 0 && r.gone === 0, folds: r.folds === 4 && r.gone > 0 && (mode === 'line' ? r.line.split(' ').length <= 12 : r.para.split(' ').length >= 10), marker: r.run === 1 && r.folds === 0 && r.gone > 0 }[expect]
    check(ok, `a return visit in ${mode}: ${expect} (${r.folds} folds, ${r.marks} marks, ${r.faded} faded, ${r.gone} hidden)${mode === 'line' ? ': "' + r.line + '"' : ''}`)
    if (mode === 'line') {
      await pg.click('.rf-fold .rf-show'); await pg.clock.runFor(300)
      check(await pg.evaluate(() => document.querySelectorAll('.rf-fold:not(.rf-hidden-run)').length === 3), 'Show opens a folded section where it is')
      // the view is a setting, in the panel: for every article, and for this one
      await pg.click('.read-chip'); await pg.click('.read-map [data-tab="settings"]')
      check(await pg.evaluate(() => document.querySelectorAll('.read-map .rv-opt[data-scope="all"]').length === 6 && document.querySelector('.read-map .rv-opt[data-view="line"]').getAttribute('aria-checked') === 'true'), 'Settings: the six views for every article, with the current one chosen')
      await pg.click('.read-map [data-scope="page"][data-view="hide"]'); await pg.clock.runFor(300)
      check(await pg.evaluate(p => localStorage.getItem('sgit.reading.view') === 'line' && JSON.parse(localStorage.getItem('sgit.reading.views'))[p] === 'hide' && document.querySelectorAll('.rf-hidden-run').length === 1, PATH), 'this article alone can have its own view, kept in this browser')
      await pg.reload({ waitUntil: 'networkidle' }); await pg.clock.runFor(2500)
      check(await pg.evaluate(() => window.SgitFolds.mode() === 'hide' && window.SgitFolds.allMode() === 'line'), 'and it holds across a reload, while every other article keeps the general one')
      await pg.click('.read-chip'); await pg.click('.read-map [data-tab="settings"]')
      await pg.click('.read-map [data-scope="page"][data-view=""]'); await pg.clock.runFor(300)
      check(await pg.evaluate(() => window.SgitFolds.mode() === 'line' && !localStorage.getItem('sgit.reading.views') && document.querySelectorAll('.rf-fold:not(.rf-hidden-run)').length >= 3), '"As every article" takes the override away')
      await pg.click('.read-map [data-scope="all"][data-view="para"]'); await pg.clock.runFor(300)
      check(await pg.evaluate(() => localStorage.getItem('sgit.reading.view') === 'para' && document.querySelector('.rf-fold .rf-p')), 'choosing for every article changes this one, which has no view of its own')
      await pg.evaluate(() => localStorage.setItem('sgit.reading.view', 'line'))
    }
    if (mode === 'fade') {
      const part = await pg.evaluate(() => window.SgitReading.sections().filter(s => s.state === 'part').length)
      check(await pg.evaluate(() => window.SgitReading.sections().every(s => s.state === 'read' || !s.nodes.some(n => n.classList.contains('rf-fade')))), `Faded fades only sections read in full, never one part read (${part} part read)`)
    }
    await pg.close()
  }
  const sum = JSON.parse(fs.readFileSync(path.join(ROOT, `articles/summaries/${SLUG}.json`), 'utf8'))
  check(sum.sections.length >= 8 && sum.sections.every(s => s.line && s.para), `the article's summaries: a line and a paragraph for each of its ${sum.sections.length} sections (${sum.sections.filter(s => s.by !== 'extract').length} written, ${sum.sections.filter(s => s.by === 'extract').length} extracted)`)
}

{ // the margin is live: a colour that follows the share read, from pale to solid, with a tick when read (card 084)
  const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => localStorage.clear()); await pg0.close()
  const pg = await open()
  check(await pg.evaluate(() => window.SgitFolds.mode() === 'margin'), 'the margin is the view when nothing is chosen')
  const id = await pg.evaluate(() => { const h = [...document.querySelectorAll('main > h2')][3]; const r = h.getBoundingClientRect(); window.scrollTo({ top: window.scrollY + r.top - 140, behavior: 'instant' }); return h.id })
  const pc = () => pg.evaluate(id => { const h = document.getElementById(id); return { p: parseInt(h.style.getPropertyValue('--rf-p') || '-1', 10), m: h.classList.contains('rf-m'), done: h.classList.contains('rf-done'), far: [...document.querySelectorAll('main > h2')].slice(-1)[0].classList.contains('rf-m') } }, id)
  await pg.clock.runFor(1500)
  const a = await pc()
  await dwell(pg, 20); const b = await pc()
  await dwell(pg, 200); const c = await pc()
  check(a.m && a.p >= 0 && a.p < b.p && b.p < 100 && !b.done, `the line beside the section follows what is read as it is read (${a.p}% then ${b.p}%), in steps of 5% (${b.p % 5 === 0})`)
  check(c.p === 100 && c.done, 'read in full: the solid line and the tick')
  check(!a.far, 'a section not reached yet has no line')
  check(await pg.evaluate(() => /color-mix/.test(getComputedStyle(document.querySelector('.rf-m'), '::before').backgroundColor) || getComputedStyle(document.querySelector('.rf-m'), '::before').transitionDuration !== '0s'), 'the colour moves slowly, not in jumps')
  await pg.close()
}

{ // a slow scroll is reading: the text that passes no faster than the reading pace counts, a fast one does not (card 084)
  const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => localStorage.clear()); await pg0.close()
  const pg = await open()
  const [H, vh, words] = await pg.evaluate(() => [document.documentElement.scrollHeight, innerHeight, window.SgitReading.sections().reduce((a, s) => a + s.words, 0)])
  // a reader scrolls by words, not pixels: a little faster than the 300 words a minute the time asks for, slower
  // over dense text than past a figure; each second the page moves by the height of about 5.3 words at the line
  const byWords = (wpm) => pg.evaluate(wpm => {
    const vh = innerHeight, H = document.documentElement.scrollHeight, y = scrollY, at = y + vh * Math.min(1, y / Math.max(1, H - vh))
    const s = window.SgitReading.sections().find(s => { const a = s.nodes[0].getBoundingClientRect(), b = s.nodes[s.nodes.length - 1].getBoundingClientRect(); return a.top + y <= at && b.bottom + y >= at })
    let pxPerWord = 4
    if (s) { const a = s.nodes[0].getBoundingClientRect(), b = s.nodes[s.nodes.length - 1].getBoundingClientRect(); pxPerWord = (b.bottom - a.top) / s.words }
    window.scrollTo({ top: y + Math.max(2, pxPerWord * wpm / 60 / (1 + vh / Math.max(1, H - vh))), behavior: 'instant' })
    return scrollY + vh >= H - 2
  }, wpm)
  let steps = 0
  while (!(await byWords(320)) && steps < 2000) { steps++; if (steps % 5 === 0) await pg.mouse.move(300 + steps % 40, 400); await pg.clock.runFor(1000) }
  await pg.clock.runFor(1500)
  const r = await R(pg)
  check(r.read >= 0.995, `scrolled slowly to the end at about 320 words a minute: ${Math.round(r.read * 100)}% read`)
  check(r.sections.every(s => s.paced === s.words), `every section has been passed at a reading pace (${r.sections.map(s => Math.round(s.paced / s.words * 100)).join(', ')}%)`)
  check(await pg.evaluate(() => { const c = document.querySelector('.read-chip'); return c.classList.contains('is-done') && /^✓/.test(c.textContent) }), 'at the end, 100% read, and the chip says so with a tick')
  await pg.evaluate(() => window.SgitReading.reset()); await pg.clock.runFor(500)
  // the same article scrolled through at four times the pace
  await scrollTo(pg, 0); await pg.clock.runFor(1000)
  for (let i = 0; !(await byWords(1280)) && i < 2000; i++) { if (i % 5 === 0) await pg.mouse.move(300 + i % 40, 400); await pg.clock.runFor(1000) }
  const f = await R(pg)
  check(f.read < 0.3 && f.sections.reduce((a, s) => a + s.paced, 0) <= 120, `scrolled at four times the pace: by pace no more than the first few seconds, ${Math.round(f.read * 100)}% read by time in view (paced ${f.sections.map(s => s.paced).join(",")}; ms ${f.sections.map(s => Math.round(s.ms / 1000)).join(",")})`)
  await pg.evaluate(() => window.SgitReading.reset()); await pg.clock.runFor(60000); await pg.mouse.move(200, 200)
  await scrollTo(pg, Math.round(H * 0.6)); await pg.clock.runFor(1500)
  check((await R(pg)).sections.every(s => s.paced === 0), 'a jump of more than a window (a link, the map) counts nothing')
  await pg.evaluate(() => { window.SgitReading.reset(); window.SgitReading.setPaused(true) }); await pg.clock.runFor(60000)
  for (let i = 1; i <= 30; i++) { await byWords(320); await pg.mouse.move(300 + i, 400); await pg.clock.runFor(1000) }
  check((await R(pg)).sections.every(s => s.paced === 0 && s.ms === 0), 'paused, a slow scroll counts nothing either')
  await pg.evaluate(() => window.SgitReading.setPaused(false))
  await pg.close()
}

{ // the words in view never move: a smooth scroll back up, in real time, with the views folding the sections above (card 084)
  for (const mode of ['line', 'hide']) {
    const c2 = await browser.newContext({ viewport: { width: 1280, height: 800 } })
    const pg = await c2.newPage(); pg.on('pageerror', e => errors.push(e.message))
    await pg.addInitScript(m => { if (!localStorage.getItem('sgit.reading.view')) localStorage.setItem('sgit.reading.view', m) }, mode)
    await pg.goto(B + PATH.slice(1), { waitUntil: 'networkidle' }); await pg.waitForTimeout(600)
    const ids = await pg.evaluate(() => window.SgitReading.sections().map(s => s.id))
    for (const id of ids.slice(0, 6)) await pg.evaluate(id => window.SgitReading.mark(id, 'read'), id)
    await pg.evaluate(id => window.scrollTo({ top: document.getElementById(id).getBoundingClientRect().top + scrollY - 100, behavior: 'instant' }), ids[8])
    await pg.waitForTimeout(1200)
    const f = await pg.evaluate(async id => {
      const h = document.getElementById(id), out = []
      window.scrollBy({ top: -1400, behavior: 'smooth' })
      const t0 = performance.now()
      await new Promise(res => { (function step() { out.push([h.getBoundingClientRect().top, document.querySelectorAll('.rf-fold').length]); if (performance.now() - t0 < 3500) requestAnimationFrame(step); else res() })() })
      return out
    }, ids[7])
    let worst = 0, back = 0
    for (let i = 1; i < f.length; i++) { const d = f[i][0] - f[i - 1][0]; worst = Math.max(worst, Math.abs(d)); if (d < -1) back++ }
    const at = f.findIndex(x => x[1] > 0), moving = f.slice(0, Math.max(at, 1)).some((x, i, a) => i && Math.abs(x[0] - a[i - 1][0]) > 0.5)
    check(at > 0 && worst < 150 && back === 0 && Math.abs(f[f.length - 1][0] - (f[0][0] + 1400)) < 3, `${mode}: a smooth scroll back up of 1400px moves the words in view by 1400px and nothing more (largest step ${Math.round(worst)}px, ${back} steps the wrong way, folded at frame ${at})`)
    check(moving && Math.abs(f[at][0] - f[at - 1][0]) < 1, `${mode}: the sections above fold after the scroll has stopped, and the words in view stay where they are`)
    await c2.close()
  }
}

{ // the meter charges for what was read (sg-meter v1.5.0, card 080)
  const pg0 = await ctx.newPage(); await pg0.goto(B); await pg0.evaluate(() => { localStorage.clear(); sessionStorage.clear() }); await pg0.close()
  const pg = await open()
  const entry = () => pg.evaluate(p => { const s = JSON.parse(localStorage.getItem('sgit.meter.v1')); return s.log.find(e => e.path === p) }, PATH)
  await pg.clock.runFor(1500)
  const e0 = await entry()
  check(e0 && e0.cost === Math.round(e0.price * 0.1 * 10) / 10, `opened: the minimum, a tenth of ${e0 && e0.price}p (${e0 && e0.cost}p)`)
  const H = await pg.evaluate(() => document.documentElement.scrollHeight)
  for (let i = 1; i <= 10; i++) { await scrollTo(pg, Math.round(H * i / 10)); await pg.mouse.move(100, 100 + i); await pg.clock.runFor(500) }
  await pg.evaluate(() => window.SgitReading.save()); await pg.clock.runFor(300)
  const e1 = await entry()
  check(e1.cost === e0.cost && e1.depth <= 0.05, `scrolled to the end in seconds: still the minimum (${e1.cost}p, ${Math.round(e1.depth * 100)}% read)`)
  for (const s of (await R(pg)).sections) await pg.evaluate(id => window.SgitReading.mark(id, 'read'), s.id)
  await pg.clock.runFor(300)
  const e2 = await entry()
  check(e2.depth === 1 && e2.cost === e2.price && e2.by === 'read', `read in full: the full price (${e2.cost}p)`)
  await pg.evaluate(() => window.SgitReading.reset()); await pg.clock.runFor(300)
  const e3 = await entry()
  check(e3.cost === e0.cost, `reset: refunded to the minimum (${e3.cost}p)`)
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
