#!/usr/bin/env python3
"""Track the move of the PHP flaws story to its own site, and the site's progress.

    python3 php-flaws/build/track.py [--sources <sources.json>] [--out <transition.json>]

Reads the dedicated site LIVE, php.oct.2026.newsroom.sgit.ai, and writes
php-flaws/data/transition.json: the site's version, when its data is from, its counts, and the
checks that must all pass before /php-flaws/ is retired and becomes a pointer (card 088). It is
the one networked step; build.py and front.py read the file it writes and stay offline.

The site is asked for /status.json first, the contract in the briefing pack
(briefs/php-oct-2026/); until it publishes one, the site's own data/vault.json,
data/versions.json and data/sources.json are read instead, and the check for status.json fails.
"""
import argparse, json, pathlib, subprocess, datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / 'php-flaws' / 'data'
SITE = 'https://php.oct.2026.newsroom.sgit.ai'
REPO = 'https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP'


def get(path):
    """(HTTP status, parsed JSON or None) for a path on the site, through curl so the proxy settings apply."""
    r = subprocess.run(['curl', '-sS', '-L', '--max-time', '30', '-w', '\n%{http_code}', SITE + path],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition('\n')
    code = int(code) if code.isdigit() else 0
    try:
        return code, json.loads(body) if code == 200 and path.endswith('.json') else None
    except json.JSONDecodeError:
        return code, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sources', default=str(DATA / 'sources.json'), help="the section's sources.json")
    ap.add_argument('--out', default=str(DATA / 'transition.json'))
    a = ap.parse_args()
    home, _ = get('/')
    st_code, status = get('/status.json')
    _, vault = get('/data/vault.json')
    _, versions = get('/data/versions.json')
    _, theirs = get('/data/sources.json')
    ours = json.loads(pathlib.Path(a.sources).read_text())
    their_slugs = {s['slug'] for s in theirs or []}
    missing = sorted(s['slug'] for s in ours if s['slug'] not in their_slugs)
    version = (status or {}).get('version') or (versions or {}).get('current')
    counts = (status or {}).get('counts') or ({'sources': vault.get('sources'), 'captures': vault.get('captures'),
                                                'hashed_files': vault.get('hashed_files')} if vault else {})
    checks = [
        {'id': 'live', 'label': 'The site answers at its own domain', 'ok': home == 200, 'detail': f'HTTP {home}'},
        {'id': 'status-json', 'label': 'The site publishes /status.json for this newsroom to read', 'ok': st_code == 200 and bool(status),
         'detail': f'HTTP {st_code}'},
        {'id': 'sources', 'label': 'Every source the section lists is on the site', 'ok': theirs is not None and not missing,
         'detail': f'{len(ours) - len(missing)} of {len(ours)}' + (f'; missing {", ".join(missing[:5])}' if missing else '')},
        {'id': 'front-page', 'label': 'The newsroom\'s front page links to the site', 'ok': True,
         'detail': 'the Developing strip, from admin/content/front/developing.json'},
        {'id': 'pointer', 'label': 'The section is replaced by a page that points to the site', 'ok': False,
         'detail': 'the last step, done here once the checks above pass'},
    ]
    out = {
        'what': 'The PHP flaws story on its own site, as last checked by php-flaws/build/track.py. Read by build.py and front.py.',
        'site': SITE + '/', 'repo': REPO,
        'checked_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
        'version': version, 'released': ((versions or {}).get('versions') or [{}])[0].get('date'),
        'data_as_of': (status or {}).get('data_as_of') or (vault or {}).get('latest_capture'),
        'vault_commit': (status or {}).get('vault_commit') or ((vault or {}).get('head') or {}).get('commit'),
        'counts': counts, 'releases': len((versions or {}).get('versions') or []),
        'checks': checks, 'passed': sum(c['ok'] for c in checks), 'total': len(checks),
        'ready_to_retire': all(c['ok'] for c in checks if c['id'] != 'pointer'),
    }
    pathlib.Path(a.out).write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print(f"site v{version}, {out['passed']}/{out['total']} checks; ready to retire the section: {out['ready_to_retire']}")
    for c in checks:
        print(f"  {'ok ' if c['ok'] else '-- '} {c['label']}: {c['detail']}")


if __name__ == '__main__':
    main()
