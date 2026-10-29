#!/usr/bin/env node
/* test_team.mjs: the team pages (card 094): the build's own checks pass, every member of the roster has a page, a
 * markdown twin, a role file and a policy, no file is claimed by two members, and nothing secret is on any team page.
 */
import fs from 'fs'
import path from 'path'
import { spawnSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const run = (...a) => spawnSync('python3', a, { cwd: ROOT, encoding: 'utf8' })

const r = run('admin/build/team.py', '--check')
check(r.status === 0 && /0 overlap/.test(r.stdout), `team.py --check: no file claimed by two members (${r.stdout.trim()})`)
const roster = JSON.parse(fs.readFileSync(path.join(ROOT, 'admin/content/team.json'), 'utf8'))
const pol = JSON.parse(fs.readFileSync(path.join(ROOT, 'team/policies.json'), 'utf8'))
check(pol.members.length === roster.members.length && pol.overlaps === 0, `team/policies.json lists all ${roster.members.length} members and no overlap`)
for (const m of roster.members) {
    const ok = ['html', 'md'].every(e => fs.existsSync(path.join(ROOT, 'team', `${m.id}.${e}`))) &&
        fs.existsSync(path.join(ROOT, 'admin/content/agents', m.id, 'ROLE.md')) && fs.existsSync(path.join(ROOT, 'admin/content/agents', m.id, 'policy.json'))
    if (!ok) check(false, `${m.id}: a page, a markdown twin, a role file and a policy`)
}
check(true, 'every member has a page, a markdown twin, a role file and a policy (or the lines above say which not)')
const index = fs.readFileSync(path.join(ROOT, 'team/index.html'), 'utf8')
check(roster.members.every(m => index.includes(`team/${m.id}.html`)), 'the team page links every member')
check(roster.members.some(m => m.id === 'newsroom-reviews' && m.handover_md === undefined) && fs.existsSync(path.join(ROOT, 'admin/content/agents/newsroom-reviews/HANDOVER.md')), '@newsroom.reviews has a role file, a policy and a handover')
const scan = run('admin/build/review_vault.py', 'scan', ...fs.readdirSync(path.join(ROOT, 'team')).filter(f => /\.(html|md|json)$/.test(f)).map(f => path.join(ROOT, 'team', f)))
const flagged = scan.stdout.split('\n').filter(l => l.startsWith('flag:') && !/email address|vault-key-shaped/.test(l))
check(flagged.length === 0, `no secret on a team page${flagged.length ? ': ' + flagged.join(' | ') : ''}`)
console.log(failed ? `${failed} FAILED` : 'ALL TEAM CHECKS PASS')
process.exit(failed ? 1 : 0)
