#!/usr/bin/env python3
"""Wording check: flags superlative self-claims and overstatement in article text.

"The clearest example I have seen", "the best case study I can think of", "the best brief ever written":
phrases like these claim more than an article can show, and they cost it credibility. The check is a
list of patterns, not a judgement; a hit is a line to reread, and the fix is usually a plainer word
("a good example", "a useful test").

  python3 admin/build/wording.py                 scan every article, graph and summary; report hits
  python3 admin/build/wording.py FILE...         scan these files
  python3 admin/build/wording.py --staged        scan only lines added in the staged diff; exit 1 on a hit
  python3 admin/build/wording.py --since DATE    scan articles dated on or after DATE (YYYY-MM-DD)

A line can opt out with the marker "wording-ok", or by an exact substring in admin/build/wording-allow.txt,
for a phrase that was reviewed and kept (a ranking inside a stated set, a quote that must stay verbatim).
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, 'admin', 'content', 'articles')

PATTERNS = [
    (r"\b(the )?(clearest|best|finest|strongest|most (complete|important|striking|powerful|elegant|honest))\b[^.;:\n]{0,60}\bI (have|'ve) (ever )?(seen|read|found|met|come across)", 'superlative + "I have seen"'),
    (r"\bI (can|could) think of\b", '"I can think of"'),
    (r"(?<!some of )\bthe (clearest|best|finest|strongest)\b[^.;:\n]{0,40}\b(ever|anyone will|anywhere|in the world|of all time)\b", 'superlative + "ever"'),
    (r"\b(ever|anyone will (ever )?)(written|write|get)\b", '"ever written / will ever get"'),
    (r"(?<!in )\bthe (clearest|best) (example|case|case study|statement|account|evidence|illustration|explanation|demonstration)\b", 'superlative example'),
    (r"\bone of the (clearest|best|finest|strongest)\b", '"one of the clearest/best"'),
    (r"\b(is|are) the clearest\b", '"is the clearest"'),
    (r"\b(groundbreaking|game[- ]chang\w*|revolutionary|unprecedented|mind[- ]blowing|incredible|stunning|jaw[- ]dropping)\b", 'hype word'),
    (r"(?<!not )(?<!not a )\b(perfect|perfectly)\b(?! the)", '"perfect" (use "great")'),
]
PATTERNS = [(re.compile(p, re.I), why) for p, why in PATTERNS if why]
SKIP = re.compile(r'wording-ok')
ALLOW_FILE = os.path.join(ROOT, 'admin', 'build', 'wording-allow.txt')   # one exact substring per line: reviewed and kept
ALLOW = [l.strip() for l in open(ALLOW_FILE, encoding='utf-8') if l.strip() and not l.startswith('#')] if os.path.exists(ALLOW_FILE) else []


def hits(text):
    for n, line in enumerate(text.splitlines(), 1):
        if SKIP.search(line) or any(a in line for a in ALLOW):
            continue
        for rx, why in PATTERNS:
            m = rx.search(line)
            if m:
                s = max(0, m.start() - 40)
                yield n, why, line[s:m.end() + 40].strip()


def files_since(date):
    out = []
    for f in sorted(os.listdir(ART)):
        if not f.endswith('.md') or f == 'README.md':
            continue
        m = re.search(r'^date:\s*(\S+)', open(os.path.join(ART, f)).read(), re.M)
        if m and m.group(1) >= date:
            slug = f[:-3]
            out += [os.path.join(ART, f)] + [p for p in (os.path.join(ART, d, slug + '.json') for d in ('graphs', 'summaries')) if os.path.exists(p)]
    return out


def all_files():
    out = [os.path.join(ART, f) for f in sorted(os.listdir(ART)) if f.endswith('.md') and f != 'README.md']
    for d in ('graphs', 'summaries'):
        p = os.path.join(ART, d)
        out += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith('.json')]
    return out


def main(argv):
    if argv[:1] == ['--staged']:
        diff = subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '-U0', '--', 'admin/content/articles'], capture_output=True, text=True).stdout
        found, cur = 0, ''
        for line in diff.splitlines():
            if line.startswith('+++ '):
                cur = line[6:]
            elif line.startswith('+') and not line.startswith('+++') and not cur.endswith('README.md'):   # the README states the rule, with examples
                for _, why, ctx in hits(line[1:]):
                    print(f'WORDING {cur}: {why}: ...{ctx}...'); found += 1
        return 1 if found else 0
    files = files_since(argv[1]) if argv[:1] == ['--since'] else (argv or all_files())
    found = 0
    for f in files:
        for n, why, ctx in hits(open(f, encoding='utf-8').read()):
            print(f'{os.path.relpath(f, ROOT)}:{n}: {why}: ...{ctx}...'); found += 1
    print(f'wording: {found} hit(s) in {len(files)} file(s)')
    return 1 if found else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
