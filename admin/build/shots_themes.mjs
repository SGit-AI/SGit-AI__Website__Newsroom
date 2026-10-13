#!/usr/bin/env node
/* shots_themes.mjs: the five themes, photographed (cards 036 and 037).
 *
 *   node admin/build/shots_themes.mjs            the screenshots, and the collage
 *   node admin/build/shots_themes.mjs --sweep    only the bar's width sweep, as a table
 *
 * Serves this tree on a local port, opens the wire, an article and a legacy page in Chromium with each theme
 * stored the way the picker stores it, and writes:
 *
 *   engineering/shots/036-<theme>-wire.png          the wire in each theme, 1440x900, for the card
 *   engineering/shots/036-picker.png                the picker open, on the wire
 *   engineering/shots/037-bar-<width>.png           the bar at the widths that matter, for the nav card
 *   admin/content/articles/images/tm-night.webp     the article's figure of Night, 1400 wide
 *   admin/content/articles/images/tm-collage.webp   the five together
 *   admin/content/articles/images/tm-picker.webp    the picker, open
 *   admin/content/articles/images/tm-bar-*.webp     the bar at 2000 and at 1279
 *
 * The webp files are made from the png by PIL (python3), which this container has; sharp is not needed.
 * The wire reads the real vault, so in a sandbox whose TLS is intercepted set CHROMIUM_SPKI_ALLOW as
 * test_wire.mjs describes; without the vault the wire shows its error box and the shot is taken anyway.
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import { execSync, execFileSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
const SWEEP_ONLY = process.argv.includes('--sweep')
const THEMES = ['newsprint', 'night', 'paper', 'blueprint', 'ember']

let chromium
try { ({ chromium } = await import('playwright')) } catch (e) {
    try { const g = execSync('npm root -g').toString().trim(); ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) }
    catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) }
}
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.tpl': 'text/plain', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' }
const server = http.createServer((req, res) => {
    let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
    if (f.startsWith(ROOT) && fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html')
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' })
    fs.createReadStream(f).pipe(res)
})
await new Promise(r => server.listen(0, '127.0.0.1', r))
const B = `http://localhost:${server.address().port}/`
const args = process.env.CHROMIUM_SPKI_ALLOW ? [`--ignore-certificate-errors-spki-list=${process.env.CHROMIUM_SPKI_ALLOW}`] : []
let browser
try { browser = await chromium.launch({ args }) } catch (e) {
    try { browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium', args }) }
    catch (e2) { console.log('SKIP: Chromium is not available'); server.close(); process.exit(0) }
}

const shotsDir = path.join(ROOT, 'engineering/shots'), imgDir = path.join(ROOT, 'admin/content/articles/images')
fs.mkdirSync(shotsDir, { recursive: true }); fs.mkdirSync(imgDir, { recursive: true })
const wireReady = pg => pg.waitForFunction(() => document.documentElement.getAttribute('data-wire') === 'ready' || document.querySelector('.wire-err'), null, { timeout: 60000 }).catch(() => {})
const settle = pg => pg.evaluate(() => document.fonts ? document.fonts.ready.then(() => new Promise(r => setTimeout(r, 250))) : new Promise(r => setTimeout(r, 250)))

async function open(theme, width = 1440, height = 900) {
    const ctx = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1 })
    await ctx.addInitScript(t => { try { localStorage.setItem('newsroom.theme', t) } catch (e) {} }, theme)
    const pg = await ctx.newPage()
    return { ctx, pg }
}

/* ---- the sweep: the bar on one row wherever the stylesheet says it fits ---- */
const WIDTHS = [2000, 1600, 1440, 1400, 1366, 1280, 1279, 1200, 1024, 820, 768, 520, 390, 360]
console.log('width  look      rows  bar-h  collapsed  overflow')
for (const [look, rel] of [['newsroom', 'wire/index.html'], ['legacy', 'about/participant.html']]) {
    for (const w of WIDTHS) {
        const { ctx, pg } = await open('newsprint', w, 900)
        await pg.goto(B + rel); if (rel.startsWith('wire')) await wireReady(pg); await settle(pg)
        const m = await pg.evaluate(() => {
            const row = document.querySelector('nav.site .row'), brand = document.querySelector('nav.site .brand')
            const items = [...row.children].filter(e => e.offsetParent !== null && !/LINK|SCRIPT|STYLE/.test(e.tagName))
            const tops = new Set(items.map(e => Math.round(e.getBoundingClientRect().top)))
            const toggle = document.querySelector('.nav-toggle')
            return { rows: tops.size, h: Math.round(row.getBoundingClientRect().height), collapsed: toggle && getComputedStyle(toggle).display !== 'none',
                     overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth }
        })
        console.log(`${String(w).padEnd(6)} ${look.padEnd(9)} ${String(m.rows).padEnd(5)} ${String(m.h).padEnd(6)} ${String(m.collapsed).padEnd(10)} ${m.overflow}`)
        if (!SWEEP_ONLY && look === 'newsroom' && [2000, 1440, 1280, 1279, 768, 390].includes(w)) {
            await pg.screenshot({ path: path.join(shotsDir, `037-bar-${w}.png`), clip: { x: 0, y: 0, width: w, height: Math.min(140, m.h + 40) } })
        }
        await ctx.close()
    }
}
if (SWEEP_ONLY) { await browser.close(); server.close(); process.exit(0) }

/* ---- the themes ---- */
const pngs = []
for (const theme of THEMES) {
    const { ctx, pg } = await open(theme)
    await pg.goto(B + 'wire/index.html'); await wireReady(pg); await settle(pg)
    const p = path.join(shotsDir, `036-${theme}-wire.png`)
    await pg.screenshot({ path: p }); pngs.push([theme, p])
    if (theme === 'night') {
        await pg.click('.theme-pick > button'); await settle(pg)
        await pg.screenshot({ path: path.join(shotsDir, '036-picker.png'), clip: { x: 640, y: 0, width: 800, height: 420 } })
    }
    await pg.goto(B + 'articles/the-vault-crosses-chrome-profiles.html'); await settle(pg)
    await pg.screenshot({ path: path.join(shotsDir, `036-${theme}-article.png`) })
    await pg.goto(B + 'about/participant.html'); await settle(pg)
    await pg.screenshot({ path: path.join(shotsDir, `036-${theme}-legacy.png`) })
    await ctx.close()
    console.log(`shot  ${theme}`)
}
await browser.close(); server.close()

/* ---- webp for the article, and the collage, by PIL ---- */
const py = `
from PIL import Image
import sys
shots, img = sys.argv[1], sys.argv[2]
themes = ${JSON.stringify(THEMES)}
# the article shows Night on its own and the five together; the cards carry every theme as png
im = Image.open(f"{shots}/036-night-wire.png").convert("RGB")
im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
im.save(f"{img}/tm-night.webp", "WEBP", quality=82, method=6)
pk = Image.open(f"{shots}/036-picker.png").convert("RGB")
pk = pk.resize((1400, round(pk.height * 1400 / pk.width)), Image.LANCZOS)
pk.save(f"{img}/tm-picker.webp", "WEBP", quality=85, method=6)
# the bar for the nav card's article figures: the widest, the last one-row width, and a phone
for w, name in ((2000, "bar-2000"), (1279, "bar-1279")):
    b = Image.open(f"{shots}/037-bar-{w}.png").convert("RGB")
    b = b.resize((1400, round(b.height * 1400 / b.width)), Image.LANCZOS) if b.width > 1400 else b
    b.save(f"{img}/tm-{name}.webp", "WEBP", quality=85, method=6)
# the collage: five crops of the top of the wire, tiled two by three with the picker's own labels
tiles = [Image.open(f"{shots}/036-{t}-wire.png").convert("RGB").crop((0, 0, 1440, 600)) for t in themes]
W, H, gap = 700, 292, 12
sheet = Image.new("RGB", (W * 2 + gap * 3, H * 3 + gap * 4), (34, 36, 42))
for i, tile in enumerate(tiles):
    tile = tile.resize((W, H), Image.LANCZOS)
    x = gap + (i % 2) * (W + gap); y = gap + (i // 2) * (H + gap)
    sheet.paste(tile, (x, y))
sheet.save(f"{img}/tm-collage.webp", "WEBP", quality=82, method=6)
sheet.save(f"{shots}/036-collage.png", "PNG")
print("webp written")
`
execFileSync('python3', ['-I', '-c', py, shotsDir, imgDir], { stdio: 'inherit' })
console.log('done')
