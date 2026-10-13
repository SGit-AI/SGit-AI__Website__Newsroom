#!/usr/bin/env node
/* test_issues.mjs: the foot of every newsletter issue, as imported (sync_newsroom.py item 15).
 *
 *   node admin/build/test_issues.mjs
 *
 * The subscribe paragraph is copied into LinkedIn with the body, so it must name this site and link it absolutely;
 * the "Posting this issue on LinkedIn?" box keeps the cover alone, because copy and paste of images works now.
 * Reads the pages on disk. No network, no browser.
 */
import fs from 'fs'
import path from 'path'
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
const DIR = path.join(ROOT, 'articles/newsletter')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const count = (s, sub) => s.split(sub).length - 1

const issues = []
const walk = d => fs.readdirSync(d, { withFileTypes: true }).forEach(e => {
  const p = path.join(d, e.name)
  if (e.isDirectory()) walk(p)
  else if (/^\d{3}-.+\.(html|md)$/.test(e.name)) issues.push(p)
})
walk(DIR)
check(issues.length >= 10 && issues.length % 2 === 0, `every issue has a page and a markdown twin (${issues.length} files)`)

for (const f of issues.sort()) {
  const t = fs.readFileSync(f, 'utf8'), rel = path.relative(ROOT, f), html = f.endsWith('.html')
  const site = html ? '<a href="https://newsroom.sgit.ai/articles/index.html">newsroom.sgit.ai</a>' : '[newsroom.sgit.ai](https://newsroom.sgit.ai/articles/index.html)'
  const sub = html ? '<a href="https://newsroom.sgit.ai/subscribe/">subscribe at newsroom.sgit.ai/subscribe</a>' : '[subscribe at newsroom.sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/)'
  check(count(t, site) === 1 && count(t, sub) === 1, `${rel}: the foot names newsroom.sgit.ai and its subscribe page, linked absolutely`)
  check(!/subscribe at sgit\.ai\/subscribe|>sgit\.ai<\/a>, with its sources|\[sgit\.ai\]\([^)]*\), with its sources/.test(t), `${rel}: the foot no longer names sgit.ai`)
  const box = html ? count(t, '<aside class="lkit"') : count(t, '**Posting this issue on LinkedIn?**')
  check(box === 1, `${rel}: one LinkedIn box`)
  check(!t.includes('lkit-imgs') && !t.includes('LinkedIn drops images from a paste'), `${rel}: the box names the cover alone, no image list`)
  check(/banners\/\d{3}-[^"/)]+\.jpg/.test(t), `${rel}: the box links the cover`)
}

console.log(failed ? `${failed} FAILED` : 'ALL ISSUE CHECKS PASS')
process.exit(failed ? 1 : 0)
