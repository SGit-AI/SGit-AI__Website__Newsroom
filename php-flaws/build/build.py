#!/usr/bin/env python3
"""The PHP flaws section (/php-flaws/): an investigation built on a private evidence vault.

    python3 php-flaws/build/build.py [--from <clone of the evidence vault>]

With --from, it first exports the vault's METADATA into php-flaws/data/: every source's row
(sources/*/source.json), the sha256 of every capture as provenance.json recorded it, and
the agents' claims/*.json and timeline/*.json merged. It never copies a captured page,
screenshot or text: those are third-party works kept as evidence, and the vault is private.
What is published is that each capture exists, when it was made, and its hash, so anyone
the vault is later opened to can check that the bytes are the ones we saw.

Without --from it renders the pages from php-flaws/data/ alone (offline, deterministic).
The editor's words are php-flaws/data/story.json; edit that, never the pages.
The nav and footer are left empty for admin/build/chrome.py to fill.
"""
import argparse, html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SEC = ROOT / 'php-flaws'
DATA = SEC / 'data'
HOST = 'https://newsroom.sgit.ai'
E = lambda s: html.escape(str(s or ''), quote=True)


def export(vault):
    vault = pathlib.Path(vault)
    rows = []
    for p in sorted((vault / 'sources').glob('*/source.json')):
        r = json.loads(p.read_text())
        caps = []
        cdir = p.parent / 'captures'
        for c in sorted(cdir.iterdir()) if cdir.exists() else []:
            prov = c / 'provenance.json'
            if not prov.exists():
                continue
            pv = json.loads(prov.read_text())
            caps.append({'stamp': c.name, 'started_utc': pv.get('started_utc'), 'status': pv.get('status'),
                         'final_url': pv.get('final_url'), 'error': pv.get('error'),
                         'sha256': pv.get('files', {})})
        raw = p.parent / 'raw' / 'SHA256SUMS'
        rows.append({k: r.get(k) for k in ('slug', 'url', 'publisher', 'kind', 'title', 'published',
                                           'status', 'primary', 'added_by')}
                    | {'captures': caps,
                       'raw_sha256': dict(reversed(l.split(None, 1)) for l in raw.read_text().split('\n') if l.strip()) if raw.exists() else {}})
    def merged(folder, key):
        out = []
        for p in sorted((vault / folder).glob('*.json')):
            for item in json.loads(p.read_text()):
                out.append(item | {'agent': p.stem})
        return sorted(out, key=key)
    timeline = merged('timeline', lambda t: str(t.get('at', '')))
    claims = merged('claims', lambda c: (c.get('agent', ''), c.get('id', '')))
    for name, obj in (('sources', rows), ('timeline', timeline), ('claims', claims)):
        (DATA / f'{name}.json').write_text(json.dumps(obj, indent=1, ensure_ascii=False) + '\n')
    print(f'exported {len(rows)} sources, {len(timeline)} events, {len(claims)} claims')


def page(rel, title, desc, body, dated):
    url = f'{HOST}/php-flaws/{rel}'
    ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': title, 'description': desc,
          'url': url, 'isPartOf': {'@type': 'WebSite', 'name': 'newsroom.sgit.ai', 'url': HOST},
          'license': 'https://creativecommons.org/licenses/by/4.0/', 'dateModified': dated,
          'copyrightNotice': 'CC BY 4.0 covers this page\'s own text, timeline and tables. Quoted words '
                             'are their authors\', with a link to each; no third-party page is reproduced here.'}
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} &middot; newsroom.sgit.ai</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta name="twitter:card" content="summary">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="php-flaws.css">
<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
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


def src_link(slug, by_slug):
    s = by_slug.get(slug)
    if not s:
        return E(slug)
    return f'<a href="{E(s["url"])}" rel="noopener">{E(s.get("publisher") or slug)}</a>'


def moved_panel():
    """The story's move to its own site, from data/transition.json (written by track.py); empty without it."""
    tf = DATA / 'transition.json'
    if not tf.exists():
        return ''
    t = json.loads(tf.read_text())
    c = t.get('counts') or {}
    rows = ''.join(f'<li class="{"ok" if k["ok"] else "todo"}"><span>{"&#10003;" if k["ok"] else "&#9675;"}</span> '
                   f'{E(k["label"])} <small>{E(k["detail"])}</small></li>' for k in t['checks'])
    return (f'<div class="pf-moved"><p class="pf-moved-k">This story has its own site</p>'
            f'<h2><a href="{E(t["site"])}">php.oct.2026.newsroom.sgit.ai</a></h2>'
            f'<p>The facts are now kept there, built from the same evidence vault, with a page per source and per party, the numbers, '
            f'the agencies compared and a briefing for each kind of reader. This section was the first step; it will be retired, and '
            f'this address will point to the site, once every check below passes. The newsroom keeps the context and the opinion: '
            f'<a href="../articles/capture-first.html">how the coverage started</a>.</p>'
            f'<p class="pf-moved-n">Site v{E(t.get("version"))} &middot; {E(c.get("sources"))} sources, {E(c.get("captures"))} captures '
            f'&middot; data as of {E(t.get("data_as_of"))} &middot; checked {E(t["checked_utc"])} &middot; <a href="{E(t["repo"])}">repository</a> '
            f'&middot; <a href="../briefs/php-oct-2026.zip">the briefing pack for the site\'s team</a> '
            f'&middot; <a href="../admin/php-oct-2026/index.html">the desk: work, roles, the open vault</a></p>'
            f'<p class="pf-moved-k">Retiring this section: {t["passed"]} of {t["total"]} checks pass</p><ul class="pf-checks">{rows}</ul></div>')


def render():
    story = json.loads((DATA / 'story.json').read_text())
    sources = json.loads((DATA / 'sources.json').read_text())
    timeline = json.loads((DATA / 'timeline.json').read_text())
    claims = json.loads((DATA / 'claims.json').read_text())
    by_slug = {s['slug']: s for s in sources}
    ncap = sum(len(s['captures']) for s in sources)
    primary = sum(1 for s in sources if s.get('primary'))
    agents = sorted({s.get('added_by') for s in sources if s.get('added_by')} | {c['agent'] for c in claims})
    dated = story['updated'][:10]

    def srcs(slugs):
        return ', '.join(src_link(x, by_slug) for x in slugs)

    b = [f'<div class="crumb"><a href="../index.html">newsroom.sgit.ai</a> / php flaws</div>',
         moved_panel(),
         f'<p class="pf-status"><b>{E(story["status"])}</b> &middot; updated {E(story["updated"])}</p>',
         f'<h1>{E(story["title"])}</h1>',
         f'<p class="lead">{story["lead_html"]}</p>',
         '<div class="proof">'
         f'<div class="n"><b>{len(sources)}</b><span>sources in the evidence vault</span><em>{primary} primary</em></div>'
         f'<div class="n"><b>{ncap}</b><span>dated captures, each hashed</span><em>screenshot, raw and rendered page</em></div>'
         f'<div class="n"><b>{len(claims)}</b><span>claims tracked to their source</span><em>{sum(1 for c in claims if c.get("status") == "unverified")} not verified</em></div>'
         f'<div class="n"><b>{len(timeline)}</b><span>events on the timeline</span><em>{len(agents)} agents writing</em></div>'
         '</div>',
         f'<div class="warnbox"><p style="margin-top:0">{story["caveat_html"]}</p></div>',
         '<h2 id="know">What we know so far</h2>', '<ul class="pf-list">']
    for k in story['known']:
        b.append(f'<li>{k["html"]} <span class="pf-src">{srcs(k["sources"])}</span></li>')
    b += ['</ul>', '<h2 id="open">What we do not know yet</h2>', '<ul class="pf-list">']
    b += [f'<li>{q}</li>' for q in story['open_html']]
    b += ['</ul>', '<h2 id="timeline">The timeline</h2>',
          '<p>Each event is dated as its source states it. Where we worked a date out ourselves, it is marked <i>inferred</i>.</p>',
          '<div class="tablewrap"><table class="pf-table"><thead><tr><th>When</th><th>What</th><th>Source</th></tr></thead><tbody>']
    for t in timeline:
        conf = ' <i>(inferred)</i>' if t.get('confidence') == 'inferred' else ''
        note = f'<br><small>{E(t["note"])}</small>' if t.get('note') else ''
        b.append(f'<tr><td class="pf-when">{E(t["at"])}{conf}</td><td>{E(t["event"])}{note}</td><td>{srcs(t.get("sources", []))}</td></tr>')
    b += ['</tbody></table></div>', '<h2 id="claims">The claims, and who makes them</h2>',
          '<p>A claim stays <i>reported</i> until a primary source confirms it, and <i>unverified</i> where even the reporting outlet says it could not check it.</p>',
          '<div class="tablewrap"><table class="pf-table"><thead><tr><th>Claim</th><th>By</th><th>Status</th><th>Source</th></tr></thead><tbody>']
    for c in claims:
        note = f'<br><small>{E(c["note"])}</small>' if c.get('note') else ''
        b.append(f'<tr><td>{E(c["claim"])}{note}</td><td>{E(c.get("by"))}</td><td><span class="pf-st pf-{E(c.get("status"))}">{E(c.get("status"))}</span></td><td>{srcs(c.get("sources", []))}</td></tr>')
    b += ['</tbody></table></div>',
          '<h2 id="evidence">How the evidence is kept</h2>', story['method_html'],
          '<p><a class="go" href="sources.html">Every source, every capture and its hashes &rarr;</a></p>',
          f'<div class="agent"><h4>For an agent</h4><p>The data behind this page is <a href="data/sources.json">data/sources.json</a>, '
          '<a href="data/timeline.json">data/timeline.json</a>, <a href="data/claims.json">data/claims.json</a> and the editor\'s '
          '<a href="data/story.json">data/story.json</a>. <code>php-flaws/build/build.py --from &lt;vault clone&gt;</code> re-exports the '
          'vault\'s metadata and rebuilds both pages. The captures themselves are in a private sgit vault and are not published; '
          'each one\'s sha256 is listed on the sources page.</p></div>']
    (SEC / 'index.html').write_text(page('index.html', story['title'], story['description'], '\n'.join(b), dated))

    s = ['<div class="crumb"><a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">php flaws</a> / sources</div>',
         '<h1>The sources, and the captures</h1>',
         f'<p class="lead">{len(sources)} sources and {ncap} captures. Each capture is a dated folder in the private evidence vault: '
         'the page as served, the page after it ran in Chromium, its text, a full-page screenshot and the response headers. '
         'Each file\'s sha256 was recorded when it was captured. A live page is captured again each time we look, so the '
         'series of captures shows how the page changed.</p>']
    kinds = {}
    for x in sources:
        kinds.setdefault(x.get('kind') or 'other', []).append(x)
    order = ['advisory', 'cve', 'vendor', 'researcher', 'government', 'news-live', 'news', 'social', 'forum', 'code', 'other']
    for kind in sorted(kinds, key=lambda k: order.index(k) if k in order else 99):
        s.append(f'<h2 id="{E(kind)}">{E(kind.replace("-", " ").capitalize())} ({len(kinds[kind])})</h2>')
        for x in kinds[kind]:
            s.append(f'<div class="pf-src-card" id="{E(x["slug"])}"><h3><a href="{E(x["url"])}" rel="noopener">{E(x.get("title") or x["url"])}</a></h3>'
                     f'<p class="pf-meta">{E(x.get("publisher"))} &middot; published {E(x.get("published") or "not stated")} &middot; '
                     f'<span class="pf-st pf-{E(x.get("status"))}">{E(x.get("status"))}</span>{" &middot; primary" if x.get("primary") else ""}'
                     f' &middot; added by {E(x.get("added_by"))} &middot; <code>{E(x["slug"])}</code></p>')
            if x['captures']:
                s.append('<details><summary>' + f'{len(x["captures"])} capture(s)</summary><ul class="pf-caps">')
                for c in x['captures']:
                    hs = ''.join(f'<li><code>{E(f)}</code> <code class="pf-h">{E(h)}</code></li>' for f, h in sorted(c['sha256'].items()))
                    err = f' &middot; {E(c["error"])}' if c.get('error') else ''
                    s.append(f'<li><b>{E(c["started_utc"])}</b> &middot; HTTP {E(c.get("status"))}{err}<ul>{hs}</ul></li>')
                s.append('</ul></details>')
            s.append('</div>')
        s.append('')
    s.append('<div class="agent"><h4>For an agent</h4><p>This page is rendered from <a href="data/sources.json">data/sources.json</a>. '
             'To check a capture, ask for the vault and compare a file\'s sha256 with the one listed here.</p></div>')
    (SEC / 'sources.html').write_text(page('sources.html', 'The PHP flaws: sources and captures',
                                           'Every source in the PHP flaws evidence vault, with each dated capture and the sha256 of its files.',
                                           '\n'.join(s), dated))
    print(f'rendered php-flaws/index.html and sources.html ({len(sources)} sources, {ncap} captures)')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='vault')
    a = ap.parse_args()
    if a.vault:
        export(a.vault)
    render()
