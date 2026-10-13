#!/usr/bin/env node
/* test_themes.mjs: the five themes and the top bar, in Chromium (cards 036, 037, 038).
 *
 *   node admin/build/test_themes.mjs
 *
 * What it checks, and why each check exists:
 *
 *   1. themes.css defines every token in every theme. A theme with a hole inherits Newsprint's value for
 *      it silently, which is how a dark theme ships with one light panel nobody noticed (VoiceDebrief's
 *      check_themes.py, the rule this copies).
 *   2. The stylesheets this site owns write no literal colour outside the themes file, the terminal
 *      palette and the few signal colours listed below. Card 038's rule, as a gate.
 *   3. On a page of each look (an imported article, a page written here, a legacy page): the picker
 *      lists the five; choosing one sets data-theme on <html>, is kept in localStorage under
 *      newsroom.theme, and is still there on the next page; a stored value that is not a theme is
 *      ignored; the page's background and ink actually change; and the computed ink on the page, the
 *      link colour on the page and the ink on the accent each hold 4.5:1 in every theme (WCAG AA, the
 *      contrast the design states).
 *   4. The bar is one row at every width from 1200 up in both looks, collapses behind Menu below, and
 *      nothing overflows the viewport at any width down to 390 (card 037's measured claim).
 *
 * Skips (exit 0) when Playwright or Chromium is missing, and says so. No vault, no network.
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import { execSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const THEMES = ['newsprint', 'night', 'paper', 'blueprint', 'ember']

/* ---- 1. every token in every theme ---- */
const css = fs.readFileSync(path.join(ROOT, 'assets/themes/themes.css'), 'utf8').replace(/\/\*[\s\S]*?\*\//g, '')
const blocks = {}
for (const m of css.matchAll(/:root(?:\[data-theme="([a-z]+)"\])?\s*\{([^}]*)\}/g)) {
    const name = m[1] || 'newsprint'
    if (m.index > css.indexOf('@media print')) continue
    blocks[name] = new Set([...m[2].matchAll(/--([a-z0-9-]+)\s*:/g)].map(x => x[1]))
}
check(THEMES.every(t => blocks[t]), `themes.css declares the five themes: ${Object.keys(blocks).join(', ')}`)
const all = new Set(THEMES.flatMap(t => [...(blocks[t] || [])]))
for (const t of THEMES) {
    const missing = [...all].filter(k => !blocks[t].has(k))
    check(missing.length === 0, `${t} defines every token (${blocks[t].size})${missing.length ? ': missing ' + missing.join(', ') : ''}`)
}

/* ---- 2. no literal colour outside the themes file ---- */
const OWN = ['assets/site.css', 'assets/site-nav.css', 'assets/vault-pane/vault-pane.css', 'assets/search/search.css', 'assets/search/ask.css',
             'assets/search/search-nav.css', 'wire/wire.css', 'for/for.css', 'passkey/lab.css', 'assets/fonts.css', 'engineering/engineering.css', 'assets/components/sg-meter/v1/v1.4/v1.4.1/sg-meter.css']
// the signals that stay literal on purpose: the vault button's dots, the wire's amber "new" flag and its ink, the terminal
// panel (and its text), the print page, and the sg-meter's neutral fallbacks inside var(), which the token overrides
const ALLOWED = /#(b8bcc4|8be0c2|f0a020|f0c070|ffd38a|14161a|a6e3c3|e6e8ec|1c1d21|0d1117|c9d1d9|3fb950|d29922|fff)\b/
for (const rel of OWN) {
    const t = fs.readFileSync(path.join(ROOT, rel), 'utf8').replace(/\/\*[\s\S]*?\*\//g, '')
    const body = rel === 'assets/site.css' ? t.slice(t.indexOf('*{box-sizing')) : t
    const literals = [...body.matchAll(/var\([^)]*\)|(#[0-9a-fA-F]{3,8}\b)/g)].map(m => m[1]).filter(Boolean).filter(h => !ALLOWED.test(h))
    check(literals.length === 0, `${rel}: no literal colour outside a token${literals.length ? ' (' + [...new Set(literals)].join(' ') + ')' : ''}`)
}

/* ---- the browser ---- */
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) {
    try { const g = execSync('npm root -g').toString().trim(); ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) }
    catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) }
}
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.tpl': 'text/plain', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' }
const server = http.createServer((req, res) => {
    let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
    if (f.startsWith(ROOT) && fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html')
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' })
    fs.createReadStream(f).pipe(res)
})
await new Promise(r => server.listen(0, '127.0.0.1', r))
const B = `http://localhost:${server.address().port}/`
let browser
try { browser = await chromium.launch() } catch (e) {
    try { browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' }) }
    catch (e2) { console.log('SKIP: Chromium is not available'); server.close(); process.exit(0) }
}

// WCAG contrast from two computed rgb() strings
const lum = s => { const [r, g, b] = s.match(/[\d.]+/g).map(Number).slice(0, 3).map(v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4 }); return .2126 * r + .7152 * g + .0722 * b }
const contrast = (a, b) => { const [x, y] = [lum(a), lum(b)]; return (Math.max(x, y) + .05) / (Math.min(x, y) + .05) }

// the paragraph measured is a body paragraph, not the crumb or a .dim line, which are secondary text on purpose
const PAGES = [['an imported article', 'articles/the-vault-crosses-chrome-profiles.html', 'main.doc p:not([class])'],
               ['a page written here', 'engineering/index.html', 'main.doc p:not([class])'],
               ['a legacy page', 'about/participant.html', 'main.doc p:not([class])']]
try {
    /* ---- 3. the picker, the memory, the contrast ---- */
    for (const [what, rel, para] of PAGES) {
        const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } })
        const pg = await ctx.newPage(); const errors = []
        pg.on('pageerror', e => errors.push(e.message)); pg.on('console', m => { if (m.type() === 'error' && !/404/.test(m.text())) errors.push(m.text()) })
        await pg.goto(B + rel)
        check((await pg.getAttribute('html', 'data-theme')) === 'newsprint', `${what}: Newsprint with nothing stored (light system)`)
        check((await pg.$$('.theme-pick li button')).length === 5, `${what}: the picker lists five themes`)
        check(await pg.evaluate(() => document.querySelector('.theme-pick ul').hidden), `${what}: the menu is closed until asked`)
        await pg.click('.theme-pick > button')
        check(await pg.evaluate(() => !document.querySelector('.theme-pick ul').hidden && document.activeElement.getAttribute('data-theme') === 'newsprint'), `${what}: the menu opens with the current theme focused`)
        const before = await pg.evaluate(() => getComputedStyle(document.body).backgroundColor)
        await pg.click('.theme-pick [data-theme="night"]')
        check((await pg.getAttribute('html', 'data-theme')) === 'night' && (await pg.evaluate(() => localStorage.getItem('newsroom.theme'))) === 'night', `${what}: choosing Night sets data-theme and stores it under newsroom.theme`)
        check((await pg.evaluate(() => getComputedStyle(document.body).backgroundColor)) !== before, `${what}: the page repaints`)
        check(await pg.evaluate(() => document.querySelector('.theme-pick > button .name').textContent === 'Night' && document.querySelector('.theme-pick ul').hidden), `${what}: the button names Night and the menu closed`)
        await pg.goto(B + 'search/index.html')
        check((await pg.getAttribute('html', 'data-theme')) === 'night', `${what}: Night is still the theme on the next page`)
        await pg.evaluate(() => localStorage.setItem('newsroom.theme', 'javascript:alert(1)'))
        await pg.goto(B + rel)
        check((await pg.getAttribute('html', 'data-theme')) === 'newsprint', `${what}: a stored value that is not a theme is ignored`)
        for (const t of THEMES) {
            await pg.evaluate(t => window.__newsroomTheme.set(t), t)
            const m = await pg.evaluate(sel => {
                const cs = getComputedStyle(document.body), p = document.querySelector(sel), a = document.querySelector('main a[href]') || document.querySelector('a.nl')
                const root = getComputedStyle(document.documentElement)
                return { bg: cs.backgroundColor, fg: cs.color, text: p ? getComputedStyle(p).color : cs.color, link: a ? getComputedStyle(a).color : cs.color,
                         accent: root.getPropertyValue('--accent').trim(), on: root.getPropertyValue('--on-accent').trim(), head: root.getPropertyValue('--head').trim() }
            }, para)
            const probe = await pg.evaluate(([a, on, head]) => { const d = document.createElement('div'); d.style.cssText = `background:${a};color:${on}`; document.body.appendChild(d); const cs = getComputedStyle(d); const r = [cs.backgroundColor, cs.color]; d.style.color = head; r.push(getComputedStyle(d).color); d.remove(); return r }, [m.accent, m.on, m.head])
            const c = { fg: contrast(m.fg, m.bg), text: contrast(m.text, m.bg), head: contrast(probe[2], m.bg), link: contrast(m.link, m.bg), on: contrast(probe[1], probe[0]) }
            const ok = Object.values(c).every(v => v >= 4.5)
            check(ok, `${what} in ${t}: ink ${c.fg.toFixed(1)}:1, text ${c.text.toFixed(1)}:1, headings ${c.head.toFixed(1)}:1, links ${c.link.toFixed(1)}:1, ink on accent ${c.on.toFixed(1)}:1 (all at least 4.5)`)
        }
        check(errors.length === 0, `${what}: no page errors${errors.length ? ': ' + errors.join(' | ') : ''}`)
        await ctx.close()
    }

    /* ---- 4. the bar ---- */
    for (const [look, rel] of [['newsroom look', 'engineering/index.html'], ['legacy look', 'about/participant.html']]) {
        for (const w of [2000, 1600, 1440, 1366, 1280, 1200, 1199, 1024, 768, 390]) {
            const ctx = await browser.newContext({ viewport: { width: w, height: 900 } })
            const pg = await ctx.newPage(); await pg.goto(B + rel)
            await pg.evaluate(() => document.fonts ? document.fonts.ready : null)
            const m = await pg.evaluate(() => ({ h: Math.round(document.querySelector('nav.site .row').getBoundingClientRect().height),
                collapsed: getComputedStyle(document.querySelector('.nav-toggle')).display !== 'none',
                overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth }))
            if (w >= 1200) check(m.h < 62 && !m.collapsed, `${look} at ${w}: one row (${m.h}px), not collapsed`)
            else check(m.collapsed, `${look} at ${w}: collapsed behind Menu (${m.h}px)`)
            check(!m.overflow, `${look} at ${w}: nothing wider than the viewport`)
            if (w === 768) {
                await pg.click('.nav-toggle')
                check(await pg.evaluate(() => getComputedStyle(document.querySelector('.nav-items')).display === 'flex' && document.querySelectorAll('.nav-items .ni').length === 8), `${look} at ${w}: Menu opens the eight groups`)
            }
            await ctx.close()
        }
    }
} finally {
    await browser.close(); server.close()
}
console.log(failed ? `test_themes: ${failed} failure(s)` : 'test_themes: OK')
process.exit(failed ? 1 : 0)
