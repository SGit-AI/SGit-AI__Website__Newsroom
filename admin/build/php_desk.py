#!/usr/bin/env python3
"""The PHP desk's admin page, /admin/php-oct-2026/ (card 089): the work, the roles, the evidence vault.

    python3 admin/build/php_desk.py [--from <clone of the evidence vault>]

With --from, it first reads a clone of the vault (a read-key clone is enough) and writes what the page
shows about it to admin/content/php-oct-2026/vault.json: the head, the latest commits on the head's
line, the top level of the tree, the sources by writer and by kind, the captures and hashed files.
Without --from it renders from the files alone (offline, deterministic).

Inputs: admin/content/php-oct-2026/work.json and roles.json (edited by commit),
admin/content/vaults/php-evidence.json (the public read key and the scan), php-flaws/data/transition.json
(the move, written by php-flaws/build/track.py). The build refuses a work row whose owner is not in the
roles, or a done row with no proof. The nav and footer are left for chrome.py.
"""
import argparse, collections, html, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'admin/content/php-oct-2026'
OUT = ROOT / 'admin/php-oct-2026/index.html'
HOST = 'https://newsroom.sgit.ai'
E = lambda s: html.escape(str(s if s is not None else ''), quote=True)
STATUS_ORDER = ['doing', 'blocked', 'open', 'done', 'dropped']


def export(vault):
    vault = pathlib.Path(vault)
    log = subprocess.run(['sgit', 'history', 'log', '--oneline'], cwd=vault, capture_output=True, text=True).stdout
    commits = []
    for line in log.splitlines():
        m = re.match(r'\s*([0-9a-f]{12})(?:\s+\(HEAD\))?\s+(.*?)(?:\s{2,}[+~-].*)?$', line)
        if m:
            commits.append({'id': m.group(1), 'subject': m.group(2).strip()})
    tree = []
    for p in sorted(vault.iterdir()):
        if p.name.startswith('.sg_vault'):
            continue
        files = [f for f in (p.rglob('*') if p.is_dir() else [p]) if f.is_file()]
        tree.append({'path': p.name + ('/' if p.is_dir() else ''), 'files': len(files), 'bytes': sum(f.stat().st_size for f in files)})
    by_writer, by_kind, caps, hashed = collections.Counter(), collections.Counter(), 0, 0
    for s in (vault / 'sources').glob('*/source.json'):
        r = json.loads(s.read_text())
        by_writer[r.get('added_by') or 'unknown'] += 1
        by_kind[r.get('kind') or 'other'] += 1
    for pv in (vault / 'sources').glob('*/captures/*/provenance.json'):
        caps += 1
        hashed += len(json.loads(pv.read_text()).get('files', {}))
    out = {'what': 'The evidence vault as php_desk.py --from last read it. Written by the build; do not edit.',
           'head': commits[0] if commits else None, 'commits': commits[:12],
           'sources': sum(by_writer.values()), 'captures': caps, 'hashed_files': hashed,
           'files': sum(t['files'] for t in tree), 'bytes': sum(t['bytes'] for t in tree),
           'by_writer': dict(by_writer.most_common()), 'by_kind': dict(by_kind.most_common()),
           'claims': sum(len(json.loads(p.read_text())) for p in (vault / 'claims').glob('*.json')),
           'events': sum(len(json.loads(p.read_text())) for p in (vault / 'timeline').glob('*.json')),
           'has_app': (vault / 'index.html').exists(), 'tree': tree}
    (CONTENT / 'vault.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print(f"php_desk: vault {out['head']['id'] if out['head'] else '?'}: {out['sources']} sources, {caps} captures, {out['files']} files")


def mb(n):
    return f'{n / 1e6:.1f} MB' if n >= 1e5 else f'{n / 1e3:.0f} KB'


def proof_html(p):
    k, r = p['kind'], p['ref']
    href = {'card': f'../../engineering/issues/{r}.html', 'release': f'../../engineering/releases/{r}.html',
            'article': f'../../articles/{r}.html', 'page': f'../../{r}', 'source': f'../../php-flaws/sources.html#{r}',
            'site': r}.get(k)
    label = {'card': f'card {r}', 'release': r, 'vault-commit': f'vault {r}', 'commit': f'commit {r}'}.get(k, r)
    return f'<a href="{E(href)}">{E(label)}</a>' if href else f'<code>{E(label)}</code>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='vault')
    a = ap.parse_args()
    if a.vault:
        export(a.vault)
    roles = json.loads((CONTENT / 'roles.json').read_text())['roles']
    work = json.loads((CONTENT / 'work.json').read_text())['work']
    vault = json.loads((CONTENT / 'vault.json').read_text())
    key = json.loads((ROOT / 'admin/content/vaults/php-evidence.json').read_text())
    tf = ROOT / 'php-flaws/data/transition.json'
    move = json.loads(tf.read_text()) if tf.exists() else None

    names = {r['name'] for r in roles}
    bad = [f"{w['id']}: owner {w['owner']!r} is not in roles.json" for w in work if w['owner'] not in names]
    bad += [f"{w['id']}: done with no proof" for w in work if w['status'] == 'done' and not w['proof']]
    bad += [f"{w['id']}: status {w['status']!r}" for w in work if w['status'] not in STATUS_ORDER]
    if bad:
        sys.exit('php_desk: refused:\n  ' + '\n  '.join(bad))

    counts = collections.Counter(w['status'] for w in work)
    per_owner = collections.defaultdict(collections.Counter)
    for w in work:
        per_owner[w['owner']][w['status']] += 1
    order = sorted(work, key=lambda w: (STATUS_ORDER.index(w['status']), -(int(w['id'][2:]) if w['status'] == 'done' else -int(w['id'][2:]))))
    rows = ''.join(
        f'<tr class="pd-{E(w["status"])}"><td><span class="pd-st">{E(w["status"])}</span></td><td><b>{E(w["what"])}</b>'
        + (f'<br><small>{E(w["note"])}</small>' if w.get('note') else '')
        + f'</td><td>{E(w["owner"])}</td><td class="pd-when">{E(w.get("opened") or "")}'
        + (f'<br>{E(w["closed"])}' if w.get('closed') else '') + f'</td><td>{" ".join(proof_html(p) for p in w["proof"])}</td></tr>'
        for w in order)
    owners = ''.join(f'<li><b>{E(o)}</b> {", ".join(f"{n} {s}" for s, n in sorted(c.items(), key=lambda x: STATUS_ORDER.index(x[0])))}</li>'
                     for o, c in sorted(per_owner.items(), key=lambda x: -sum(x[1].values())))
    role_cards = ''.join(
        f'<div class="pd-role" id="role-{E(re.sub(r"[^a-z0-9]+", "-", r["name"].lower()))}"><p class="pd-kind">{E(r["kind"])}</p><h3>{E(r["name"])}</h3>'
        f'<p>{E(r["responsible"])}</p><dl><dt>May change</dt><dd>{E(r["may"])}</dd>'
        + (f'<dt>Must not</dt><dd>{E(r["must_not"])}</dd>' if r.get('must_not') else '')
        + f'<dt>Works in</dt><dd>{E(r["works_in"])}</dd><dt>Record</dt><dd>{E(r["record"])}</dd>'
        + (f'<dt>Also known as</dt><dd>{E(", ".join(r["aka"]))}: {E(r.get("aka_note"))}</dd>' if r.get('aka') else '')
        + '</dl></div>' for r in roles)
    move_html = ''
    if move:
        checks = ''.join(f'<li class="{"ok" if c["ok"] else "todo"}">{"&#10003;" if c["ok"] else "&#9675;"} {E(c["label"])} <small>{E(c["detail"])}</small></li>' for c in move['checks'])
        move_html = (f'<h2 id="move">The move to the story&rsquo;s own site</h2><p>The facts live on <a href="{E(move["site"])}">php.oct.2026.newsroom.sgit.ai</a> '
                     f'(v{E(move.get("version"))}, data as of {E(move.get("data_as_of"))}). <a href="../../php-flaws/index.html">/php-flaws/</a> retires into a pointer when '
                     f'these pass; {move["passed"]} of {move["total"]} did when last checked, {E(move["checked_utc"])}.</p><ul class="pd-checks">{checks}</ul>')
    writers = ''.join(f'<tr><td>{E(k)}</td><td class="n">{v}</td></tr>' for k, v in vault['by_writer'].items())
    kinds = ''.join(f'<tr><td>{E(k)}</td><td class="n">{v}</td></tr>' for k, v in vault['by_kind'].items())
    tree = ''.join(f'<tr><td><code>{E(t["path"])}</code></td><td class="n">{t["files"]}</td><td class="n">{mb(t["bytes"])}</td></tr>' for t in vault['tree'])
    commits = ''.join(f'<li><code>{E(c["id"])}</code> {E(c["subject"])}</li>' for c in vault['commits'])
    scan = key['scan']
    noted = ''.join(f'<li>{E(n)}</li>' for n in scan['noted'])
    head = vault['head']['id'] if vault['head'] else ''

    body = f'''<div class="crumb"><a href="../../index.html">newsroom.sgit.ai</a> / <a href="../index.html">admin</a> / php desk</div>
<h1>The PHP desk</h1>
<p class="lead">The admin page for the PHP flaws story of October 2026 as this newsroom covers it: the work and who did it, the roles of the people and agents on the story, and the evidence vault, which anyone can now open read-only. The facts themselves live on <a href="https://php.oct.2026.newsroom.sgit.ai/">the story&rsquo;s own site</a>; how the coverage started is in <a href="../../articles/capture-first.html">Capture first</a>; the design of this page is <a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/admin/notes/2026-10-22__the-php-desk.md">its brief</a>.</p>
<div class="proof">
<div class="n"><b>{counts["done"]}</b><span>pieces of work done</span><em>each with its proof</em></div>
<div class="n"><b>{counts["open"] + counts["doing"] + counts["blocked"]}</b><span>open, in progress or blocked</span><em>{counts["blocked"]} blocked</em></div>
<div class="n"><b>{len(roles)}</b><span>people and agents</span><em>roles and responsibilities</em></div>
<div class="n"><b>{vault["sources"]}</b><span>sources in the vault</span><em>{vault["captures"]} captures, {vault["hashed_files"]} hashed files</em></div>
</div>

<h2 id="work">The work</h2>
<p>One row per piece of work, from <code>admin/content/php-oct-2026/work.json</code>. Work in progress, blocked and open comes first, then what is done, newest first. Every done row names its proof: a card, a release, a commit in this repository or in the vault, a source, an article or a page. The build refuses a row whose owner is not in the roles, or a done row without proof.</p>
<div class="tablewrap"><table class="pd-table"><thead><tr><th>Status</th><th>What</th><th>Owner</th><th>Opened / closed (UTC)</th><th>Proof</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="pd-owners-h">By owner</p><ul class="pd-owners">{owners}</ul>
{move_html}

<h2 id="roles">The roles</h2>
<p>Everyone who has worked on the story, from <code>admin/content/php-oct-2026/roles.json</code>: what each is responsible for, what each may and may not change, where each works, and the record that shows it. Drawn from the git logs and the vault&rsquo;s commit messages. The editorial responsibility is always Dinis&rsquo;s.</p>
<div class="pd-roles">{role_cards}</div>

<h2 id="vault">The evidence vault, open to everyone</h2>
<p>Every source the story rests on, captured as its publisher served it: the raw page, the rendered page, its text, a full-page screenshot and the headers, each file hashed at capture. The vault is <b>public and read-only</b> since {E(key["published"])}, by the editor&rsquo;s decision. The key below can read every file and every commit and cannot write. Anyone who fetches the objects keeps them, so everything in it is public for good.</p>
<div class="pd-key">
<p><a class="btn primary" href="#browse">Browse it on this page &darr;</a> <a class="btn" href="{E(key["browse"])}">Open it in the SG/App vault browser</a> <small>The vault carries its own app. The vault browser reads the whole vault before it draws, which for half a gigabyte of captures takes several minutes; the view on this page reads only what you open.</small></p>
<p class="pd-k">Public read key</p><pre><code>{E(key["read_key"])}</code></pre>
<p class="pd-k">Clone it</p><pre><code>pip install sgit-ai
{E(key["clone"])}</code></pre>
<p><small>Vault <code>{E(key["vault_id"])}</code> on <code>{E(key["remote"])}</code>, opened {E(key["opened"])}. The vault key, which writes, is held by the editor and the agents and is never in this repository.</small></p>
</div>
<h3 id="browse">Browse it here</h3>
<p>The vault, read live in this page with the key above: the manifest first, then each source&rsquo;s notes, its captures, a thumbnail of each, and the full screenshot or the text when asked for. Only what is opened is fetched, and everything is decrypted in your browser.</p>
<div id="vault-view" class="vv" data-config="{E(json.dumps({'remote': key['remote'], 'vault_id': key['vault_id'], 'read_key': key['read_key']}))}"><p class="vv-status">This view needs JavaScript; without it, clone the vault with the command above.</p></div>
<script type="module" src="vault-view.js"></script>
<h3 id="scan">The scan before the key</h3>
<p>On {E(scan["date"])}, at vault head <code>{E(scan["vault_head"])}</code>, all {scan["files"]} files, captures included, were searched for: {E("; ".join(scan["searched_for"]))}. Found: <b>{E(scan["found"])}</b>. Noted:</p>
<ul>{noted}</ul>
<p>{E(scan["action"][0].upper() + scan["action"][1:])}.</p>
<h3 id="contents">What is in it</h3>
<p>At vault head <code>{E(head)}</code>: {vault["files"]} files, {mb(vault["bytes"])}; {vault["sources"]} sources, {vault["captures"]} captures, {vault["hashed_files"]} files hashed at capture, {vault["claims"]} claims and {vault["events"]} timeline events in per-agent files{", and the vault&rsquo;s own app" if vault["has_app"] else ""}.</p>
<div class="pd-grid">
<div><p class="pd-k">Sources by writer</p><table class="pd-table pd-small"><tbody>{writers}</tbody></table></div>
<div><p class="pd-k">Sources by kind</p><table class="pd-table pd-small"><tbody>{kinds}</tbody></table></div>
<div><p class="pd-k">The top level</p><table class="pd-table pd-small"><thead><tr><th>Path</th><th>Files</th><th>Size</th></tr></thead><tbody>{tree}</tbody></table></div>
</div>
<p class="pd-k">The latest commits on the head&rsquo;s line</p><ul class="pd-commits">{commits}</ul>
<p>The protocol every writer follows is the vault&rsquo;s <code>README.md</code>; the hashes of every capture are also listed on <a href="../../php-flaws/sources.html">the section&rsquo;s sources page</a>.</p>

<h2 id="not">Not on this page</h2>
<ul><li><b>Visitor logging</b> with an append lane is the story site&rsquo;s own work, by the editor&rsquo;s decision; it is row w-22 above.</li>
<li><b>Writing from the page.</b> The page reads; the work and the roles change by commit.</li></ul>

<div class="agent"><h4>For an agent</h4><p>The data: <code>admin/content/php-oct-2026/work.json</code>, <code>roles.json</code>, <code>vault.json</code>; the key and the scan in <code>admin/content/vaults/php-evidence.json</code>; the move in <code>php-flaws/data/transition.json</code>. Rebuild with <code>python3 admin/build/php_desk.py --from &lt;clone&gt;</code>, where the clone can be made with the public read key above. To add work, append a row to work.json with an owner from roles.json and, when done, its proof.</p></div>'''

    title = 'The PHP desk: work, roles and the evidence vault'
    desc = 'The admin page for the PHP flaws story of October 2026: the work and who did it, the roles of the people and agents, and the evidence vault opened with a public read key.'
    url = f'{HOST}/admin/php-oct-2026/index.html'
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} &middot; newsroom.sgit.ai</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta name="twitter:card" content="summary">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="stylesheet" href="../../assets/site.css">
<link rel="stylesheet" href="desk.css">
</head>
<body>

<nav class="site"></nav>

<main class="doc">
{body}
</main>

<footer class="site"></footer>
</body>
</html>
'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    old = OUT.read_text() if OUT.exists() else None
    # chrome.py fills the nav and footer in place; compare with them emptied so a rerun is a no-op
    strip = lambda t: re.sub(r'<footer class="site">.*?</footer>', '<footer class="site"></footer>',
                             re.sub(r'<nav class="site">.*?</nav>', '<nav class="site"></nav>', t, flags=re.S), flags=re.S)
    if old is None or strip(old) != page:
        OUT.write_text(page)
        print(f'php_desk: wrote admin/php-oct-2026/index.html ({len(work)} rows, {len(roles)} roles)')
    else:
        print('php_desk: unchanged')


if __name__ == '__main__':
    main()
