#!/usr/bin/env node
// newsroom.sgit.ai pre-release gate. Run from anywhere: node admin/build/validate.js
// Checks, in order:
//   1. version agreement — admin/build/version.txt vs every page's version badge,
//      the versions table, llms.txt and index.md
//   2. internal links — every relative href/src in every .html file resolves to a
//      file in the tree (fragments stripped; external and mailto links skipped)
//   3. canonical host — every <link rel="canonical"> and og:url points at the host
//      in CNAME (or, for a verbatim republication, at the stated source host — see
//      check 8), and every page declares one
//   4. the agent surface — every section hub is named in llms.txt, and the sitemap
//      and the tree agree in both directions
//   5. key-leak tripwire — nothing in the tree may look like an sgit vault key
//   6. div balance — every page opens and closes the same number of <div>s
//   7. every page ends with an agent block — the house rule inherited from
//      issues-fs.sgit.ai
//   8. the provenance contract — every page carrying a republished-material block
//      (class="provenance") states a first-published date and a source link. This
//      is the site's own central argument (most articles do not provide evidence,
//      the link is never followed) applied to itself. See briefs/02.
//   9. the redaction watch-list — nothing Tier 3 in briefs/08__source-manifest.csv
//      (named VC, live product pricing, an infra account number) may appear
//      anywhere in the published tree.
//  10. no build tooling is gitignored — a generated page whose generator is not in
//      the repository cannot be rebuilt by anyone who clones it. This has now
//      happened twice from the same cause (see .gitignore), so it is a check.
//  11. the imported newsroom is unedited — every file admin/build/sync_newsroom.py
//      brought in from sgit.ai still hashes to what it recorded, once this site's own
//      nav, footer and version stamp are set aside. The brief's rule, "do not edit moved
//      content on the new side, or the two will drift", as a check.
//  12. the article numbers hold — every published article has a number in articles/ids.json,
//      numbers and addresses are unique, a number is never reused, and no number that was in
//      the last commit has moved. A link written today names articles by these numbers and
//      has to open the same list in a year.
//  13. the vendored vault library is unedited — every file of assets/vendor/sg-vault/v0.2.3
//      hashes to what its VENDOR.md records; one code base, pinned, refreshed from upstream.
// Any failure exits 1: no tag, no publish.
'use strict';
const fs   = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT   = path.resolve(__dirname, '..', '..');
const errors = [];

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    if (name === '.git' || name === '.github' || name === 'node_modules' || name === '.sg_vault') continue;
    // An archive of pages is not a set of pages: briefs/summit-archive/ holds copies as served
    // at v0.3.12, whose relative links resolve against the site root they were cut from and
    // whose version badge is deliberately frozen. Checking them as live pages produced 413
    // errors the first time it existed, every one of them a correct observation about a copy.
    if (name === 'summit-archive') continue;
    // world-news-day/vault-app/ is the application that ships INSIDE the encrypted vault. It
    // has no site nav, no canonical and no version badge on purpose: it renders in the
    // SG/Send host from the vault's own bytes, not on this domain. Checking it as a page of
    // this site is checking the wrong thing, in the same way summit-archive/ was.
    if (name === 'vault-app') continue;
    const p  = path.join(dir, name);
    const st = fs.statSync(p);
    if (st.isDirectory()) walk(p, out);
    else out.push(p);
  }
  return out;
}

const files     = walk(ROOT);
const htmlFiles = files.filter(f => f.endsWith('.html'));
const rel       = f => path.relative(ROOT, f).split(path.sep).join('/');

// --- 1. version agreement -------------------------------------------------
const VERSION = fs.readFileSync(path.join(ROOT, 'admin/build/version.txt'), 'utf8').trim();
if (!/^v\d+\.\d+\.\d+$/.test(VERSION)) {
  errors.push(`version.txt does not carry a vX.Y.Z version: "${VERSION}"`);
}
for (const f of htmlFiles) {
  const t = fs.readFileSync(f, 'utf8');
  const badges = [...t.matchAll(/class="ver"[^>]*>(v\d+\.\d+\.\d+)</g)].map(m => m[1]);
  for (const b of badges) if (b !== VERSION) {
    errors.push(`${rel(f)}: version badge ${b} != ${VERSION}`);
  }
}
for (const extra of ['llms.txt', 'index.md']) {
  const t = fs.readFileSync(path.join(ROOT, extra), 'utf8');
  if (!t.includes(VERSION)) errors.push(`${extra} does not mention ${VERSION}`);
}
const versTable = fs.readFileSync(path.join(ROOT, 'admin/versions.html'), 'utf8');
if (!versTable.includes(`class="vnum">${VERSION}<`)) {
  errors.push(`admin/versions.html has no row for ${VERSION}`);
}
const rows = [...versTable.matchAll(/class="vnum">(v\d+\.\d+\.\d+)</g)].map(m => m[1]);
for (const v of rows) if (rows.filter(x => x === v).length > 1) {
  errors.push(`admin/versions.html lists ${v} more than once`);
  break;
}

// --- 2. internal links ----------------------------------------------------
// Attributes of real tags only. A code sample is escaped text (&lt;script src="/x"&gt;): it is
// something a reader copies, not a link this site serves. Reading it as a link made this check
// fail on SG Meter's install snippet, and in v0.6.0 it made the import's bug look like a fix:
// the import had rewritten the snippet's path into one that resolved, so the check passed.
const realTagAttrs = t => [...t.matchAll(/<[a-zA-Z][^<>]*>/g)]
  .flatMap(tag => [...tag[0].matchAll(/(?:href|src|data-src)="([^"#]+)(?:#[^"]*)?"/g)]);
for (const f of htmlFiles) {
  const t   = fs.readFileSync(f, 'utf8');
  const dir = path.dirname(f);
  for (const m of realTagAttrs(t)) {
    const target = m[1];
    if (/^(https?:|mailto:|data:|\/\/)/.test(target) || target === '') continue;
    if (!fs.existsSync(path.resolve(dir, target))) {
      errors.push(`${rel(f)}: broken link -> ${target}`);
    }
  }
}

// --- 2b. figures and trail images resolve ------------------------------------
// sgit.ai's authoring contract forbids a declarative <img src>, so a figure is a placeholder,
//   <figure class="shot" data-shot="x.webp" data-dir="../demos/vaults/agent-desk/images/">
// and assets/shots.js sets img.src = data-dir + data-shot at runtime (data-dir defaults to
// images/). A card thumbnail is a background set the same way from data-trail-img. Check 2 reads
// href, src and data-src, and none of these is any of them, so a figure whose image was never
// copied passed every check on this site and showed "screenshot unavailable" to the reader.
// That is exactly what v0.6.0 and v0.6.1 shipped: 51 figures in 10 articles, and the 66
// thumbnails on the front page at /, found by five synthetic readers and not by this gate.
const FIGURE = /<figure\b[^>]*\bclass="[^"]*\bshot\b[^"]*"[^>]*>/g;
const attr   = (tag, name) => { const m = tag.match(new RegExp(`\\s${name}="([^"]*)"`)); return m ? m[1] : null; };
for (const f of htmlFiles) {
  const t   = fs.readFileSync(f, 'utf8');
  const dir = path.dirname(f);
  for (const m of t.matchAll(FIGURE)) {
    const shot = attr(m[0], 'data-shot');
    if (!shot) continue;
    const base = attr(m[0], 'data-dir') ?? 'images/';
    if (/^(https?:|\/\/|data:)/.test(base) || /^(https?:|\/\/|data:)/.test(shot)) continue;
    if (!fs.existsSync(path.resolve(dir, base + shot))) {
      errors.push(`${rel(f)}: figure image missing -> ${base}${shot}`);
    }
  }
  for (const m of t.matchAll(/<[a-zA-Z][^<>]*\sdata-trail-img="([^"]+)"[^<>]*>/g)) {
    if (/^(https?:|\/\/|data:)/.test(m[1])) continue;
    if (!fs.existsSync(path.resolve(dir, m[1]))) errors.push(`${rel(f)}: trail image missing -> ${m[1]}`);
  }
}

// --- 2c. scripts a page loads at runtime exist ---------------------------------
// The same blind spot as 2b, for code instead of images. sgit.ai's pages load their behaviour from
// inline loaders, import('x/y.js') and fetch('x/y.js'), and a vault page builds the name at runtime:
//   ['vault-ui-embed.js'].forEach(function (f) { fetch('../../../assets/' + f)... })
// None of that is an href or a src. The study page imported at v0.6.2 asked for assets/vault-ui-embed.js,
// which was not here, so its "See it live" section, the reason the page exists, silently did nothing.
// Only patterns that name a .js file are checked, and only as the page's own relative path.
const RUNTIME_SCRIPT = [
  /\b(?:fetch|import)\(\s*'([^'+]*\.m?js)(?:\?[^']*)?'\s*\)/g,
];
const NAME_LIST = /\[((?:\s*'[A-Za-z0-9_.-]+\.js'\s*,?)+)\s*\]\.forEach\(function \(f\) \{[\s\S]{0,240}?fetch\('([^']*)'\s*\+\s*f\)/g;
for (const f of htmlFiles) {
  const t   = fs.readFileSync(f, 'utf8');
  const dir = path.dirname(f);
  const wanted = [];
  for (const re of RUNTIME_SCRIPT) for (const m of t.matchAll(re)) wanted.push(m[1]);
  for (const m of t.matchAll(NAME_LIST)) {
    for (const n of m[1].matchAll(/'([^']+)'/g)) wanted.push(m[2] + n[1]);
  }
  for (const w of new Set(wanted)) {
    if (/^(https?:|\/\/|\/)/.test(w)) continue;
    if (!fs.existsSync(path.resolve(dir, w))) errors.push(`${rel(f)}: loads a script at runtime that does not exist -> ${w}`);
  }
}

// --- 2d. a payment link on a page is a live one --------------------------------
// The meter config carries the top-up link. A Stripe test-mode link (buy.stripe.com/test_...) takes
// no money and a mistyped one takes the reader somewhere else, and either would sit on a page that
// says "pay". sync_newsroom.py refuses to write anything but the live shape; this refuses to ship it.
for (const f of htmlFiles) {
  const t = fs.readFileSync(f, 'utf8');
  for (const m of t.matchAll(/"topup": \{"amount": \d+, "link": "([^"]*)"\}/g)) {
    if (m[1] !== '' && !/^https:\/\/buy\.stripe\.com\/[A-Za-z0-9]+$/.test(m[1])) {
      errors.push(`${rel(f)}: the top-up link is not a live Stripe Payment Link -> ${m[1]}`);
    }
  }
}

// --- 3. canonical host ----------------------------------------------------
// A verbatim republication of docs.diniscruz.ai material points its canonical at
// the ORIGINAL, per briefs/02 §3.4 — that page is exempt from the CNAME-host rule
// and marked instead with data-canonical-is-source on the <html> tag.
const HOST = fs.readFileSync(path.join(ROOT, 'CNAME'), 'utf8').trim();
if (!/^[a-z0-9.-]+$/.test(HOST)) errors.push(`CNAME does not carry a hostname: "${HOST}"`);
for (const f of htmlFiles) {
  const t = fs.readFileSync(f, 'utf8');
  const exempt = /data-canonical-is-source/.test(t);
  const claimed = [
    ...[...t.matchAll(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/g)].map(m => m[1]),
    ...[...t.matchAll(/<meta[^>]+property="og:url"[^>]+content="([^"]+)"/g)].map(m => m[1]),
  ];
  if (!exempt) {
    for (const url of claimed) if (!url.startsWith(`https://${HOST}/`)) {
      errors.push(`${rel(f)}: canonical/og:url is not on ${HOST} -> ${url}`);
    }
  }
  if (!/rel="canonical"/.test(t)) errors.push(`${rel(f)}: no canonical link`);
}

// --- 4. the agent surface -------------------------------------------------
const llms = fs.readFileSync(path.join(ROOT, 'llms.txt'), 'utf8');
const hubs = htmlFiles.map(rel).filter(p => p.endsWith('/index.html') && p.split('/').length === 2);
for (const h of hubs) if (!llms.includes(h)) {
  errors.push(`llms.txt does not name the section hub /${h} — for an agent that page does not exist`);
}
const sitemap = fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8');
const listed  = [...sitemap.matchAll(new RegExp(`<loc>https://${HOST}/([^<]+)</loc>`, 'g'))].map(m => m[1]);
for (const p of listed) if (!fs.existsSync(path.join(ROOT, p))) {
  errors.push(`sitemap.xml lists a page that does not exist: /${p}`);
}
for (const f of htmlFiles) if (!listed.includes(rel(f))) {
  errors.push(`sitemap.xml is missing ${rel(f)}`);
}

// --- 5. key-leak tripwire --------------------------------------------------
// Three shapes, because the first one alone would not have caught a real key.
//
// The original pattern assumed a UUID vault id. When this site's first vaults were
// actually created at v0.4.4, sgit issued keys of the form
// `sgit_private_vault_<base32ish>:<8 hex>` — which the UUID pattern does not match at
// all. A tripwire that is satisfied by the absence of a shape nobody uses is not a
// tripwire, so the real prefixes are now matched by name, and the archive is NOT
// exempt: a key committed into an archived copy is exactly as leaked.
//
// READ keys are publishable and are deliberately not matched: they are bare hex and
// carry no passphrase, so there is nothing here to strip. Vault keys never are.
const KEY_SHAPES = [
  [/[A-Za-z0-9_-]{20,}:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/,
   'a vault-key-shaped string (uuid vault id)'],
  [/sgit_private_vault_[A-Za-z0-9_-]{8,}\s*:\s*[A-Za-z0-9]{4,}/,
   'an sgit PRIVATE VAULT KEY — that is write access to everything in the vault'],
  // Precise, not stricter. This fired on `sgit clone sgit_public_read_<64hex>:<id>` — the
  // exact line a published vault page MUST carry — which is sgit.ai's own recorded mistake:
  // "our own tripwire banned the string we needed in order to teach people to recognise it;
  // make the rule precise, not stricter". A public read key is publishable by definition, so
  // it is excluded by name and everything else in that position still fires.
  //
  // sgit_rk1_ is the same thing in sgit's first key format, still in circulation: sgit.ai's
  // own credential checker (admin/build/check_credential.py there) classifies it as a read
  // key. It reached this tree in v0.6.0, quoted in a published diff of the EU AI Act vault's
  // read key inside an imported article's version history.
  [/\bsgit\s+(?:clone|init)\s+(?!sgit_public_read_|sgit_rk1_)[A-Za-z0-9_-]{16,}:[A-Za-z0-9]{4,}/,
   'a command line carrying a credential that is not a published read key'],
];
for (const f of files) {
  if (/\.(png|jpg|jpeg|gif|webp|ico|woff2?|zip|svg|pdf)$/.test(f)) continue;
  const t = fs.readFileSync(f, 'utf8');
  for (const [shape, what] of KEY_SHAPES) {
    if (shape.test(t)) { errors.push(`${rel(f)}: contains ${what}`); break; }
  }
}

// --- 5b. the chrome is actually applied ------------------------------------
// A page is generated with EMPTY nav and footer blocks and chrome.py fills them. Skip
// chrome.py in a build cycle and every regenerated page ships with no navigation, no
// version badge and no footer — and every other check here still passed, because they all
// test what a page SAYS rather than whether it has any furniture at all. That happened
// once, at v0.5.0, and was caught by reading a diff rather than by this file.
for (const f of htmlFiles) {
  const t = fs.readFileSync(f, 'utf8');
  if (!/<nav class="site">[\s\S]*class="brand"[\s\S]*<\/nav>/.test(t)) {
    errors.push(`${rel(f)}: the nav block is empty — run admin/build/chrome.py`);
  }
  if (!/<footer class="site">[\s\S]*class="verline"[\s\S]*<\/footer>/.test(t)) {
    errors.push(`${rel(f)}: the footer block is empty — run admin/build/chrome.py`);
  }
}

// --- 6. div balance ----------------------------------------------------
for (const f of htmlFiles) {
  const t     = fs.readFileSync(f, 'utf8');
  const open  = (t.match(/<div\b/g)   || []).length;
  const close = (t.match(/<\/div>/g)  || []).length;
  if (open !== close) {
    errors.push(`${rel(f)}: ${open} <div> vs ${close} </div> — a block is not closed`);
  }
}

// --- 7. every page ends with an agent block --------------------------------
for (const f of htmlFiles) {
  const r = rel(f);
  // documents/index.html is a hand-written hub and owes an agent block like any other
  // page; documents/<slug>.html are generated projections of raw markdown (gen_documents.py)
  // and are exempt, the same exemption issues-fs.sgit.ai makes for its reader pages.
  if (r.startsWith('admin/') || r === 'about/participant.html') continue;
  if (r.startsWith('documents/') && r !== 'documents/index.html') continue;
  const t = fs.readFileSync(f, 'utf8');
  // A page imported from sgit.ai serves agents the way sgit.ai does: an llms.txt chip at the
  // top and a declared markdown twin. That is the same obligation met in another form, so it
  // counts, but only when BOTH are present and the twin exists. A page with neither still fails.
  const twin = (t.match(/<link rel="alternate" type="text\/markdown" href="([^"]+)"/) || [])[1];
  const sgitSurface = /class="llmschip"/.test(t) && twin && fs.existsSync(path.resolve(path.dirname(f), twin));
  if (!/class="agent"/.test(t) && !sgitSurface) {
    errors.push(`${r}: no "for an agent" block — every page on this site owes one`);
  }
}

// --- 8. the provenance contract --------------------------------------------
// briefs/02 is the load-bearing file in this site's own brief pack: a page that
// republishes or derives from previously published material must carry a visible
// provenance block naming the original date and linking to the original.
for (const f of htmlFiles) {
  const t = fs.readFileSync(f, 'utf8');
  for (const m of t.matchAll(/<div class="provenance"[^>]*>([\s\S]*?)<\/div>/g)) {
    const block = m[1];
    if (!/First published/.test(block)) {
      errors.push(`${rel(f)}: a provenance block has no "First published" date`);
    }
    if (!/href="https?:\/\//.test(block)) {
      errors.push(`${rel(f)}: a provenance block has no link to the original source`);
    }
  }
}

// --- 9. the redaction watch-list --------------------------------------------
// briefs/06 §2 and briefs/08 Tier 3 rows. Literal strings that must never appear
// anywhere in the published tree — a named VC, live B2B pricing, an infra account.
// Two things about this list were wrong until v0.2.2 and are worth stating so they are
// not reintroduced:
//
//   1. briefs/ used to be exempt, on the reasoning that "the pack documents the
//      watch-list by naming these". That reasoning is inverted. The watch-list names
//      each item in the course of FORBIDDING its publication, so publishing the pack
//      verbatim published exactly what the pack forbids — a real leak that reached the
//      live site. The published pack is now checked like every other file, and the
//      redactions are recorded in briefs/PUBLIC.md.
//   2. The pricing patterns were written from memory of the brief's prose rather than
//      against the strings actually in the files, so they matched nothing. Every entry
//      below is now a literal that was verified to appear in the source before masking.
const REDACTED = [
  '33N Ventures', '33n-ventures',
  '745506449035',
  'investor.myfeeds.ai', 'investor-myfeeds-ai',
  '£2k–£50k', '£2k-£50k', 'GBP2k-50k', '£2,000-50,000',
];
for (const f of files) {
  if (f === path.join(ROOT, 'admin/build/validate.js')) continue; // this file necessarily names what it bans
  if (/\.(png|jpg|jpeg|gif|webp|ico|woff2?|zip|svg|pdf)$/.test(f)) continue;
  const t = fs.readFileSync(f, 'utf8');
  for (const bad of REDACTED) if (t.includes(bad)) {
    errors.push(`${rel(f)}: contains redacted material "${bad}" — see briefs/06__boundaries-and-house-style.md §2`);
  }
}

// --- 10. no build tooling is gitignored ------------------------------------
// v0.1.0 shipped with admin/build/ silently excluded by a bare `build/` rule in a
// generic Python .gitignore; CI failed with MODULE_NOT_FOUND and the path was
// re-included by name. governance/build/ was created at v0.2.6 and hit the SAME rule,
// and because its generated HTML was committed the site kept deploying correctly while
// build.py, floor.py and gates.py were dropped from every commit for three releases.
// It surfaced only when a published document linked to floor.py on GitHub and 404'd.
// Fixing the instance twice would have guaranteed a third time, so the rule is now
// root-anchored AND this check exists: a generated page whose generator is not in the
// repository cannot be rebuilt by anyone who clones it.
try {
  const ignored = execFileSync('git', ['ls-files', '--others', '--ignored', '--exclude-standard'],
                               { cwd: ROOT, encoding: 'utf8' })
    .split('\n').map(s => s.trim()).filter(Boolean);
  for (const p of ignored) {
    if (/(^|\/)__pycache__\//.test(p) || /\.pyc$/.test(p)) continue;   // real build output
    if (/(^|\/)build\//.test(p) || /\.(py|js|mjs)$/.test(p)) {
      errors.push(`${p}: build tooling is excluded by .gitignore — it would not reach the ` +
                  `repository, and the pages it generates could not be rebuilt from a clone`);
    }
  }
} catch (e) {
  // Not a git checkout, or git unavailable. Not a failure — just unverifiable here.
  console.warn('validate: check 10 skipped (git not available)');
}

// --- 11. the imported newsroom is unedited -----------------------------------
// The newsroom is built on sgit.ai and imported here until cutover. Editing an imported page
// on this side makes the two copies disagree silently, and the next sync then either loses
// the edit or, worse, a reader trusts a page that says something sgit.ai's does not. The
// normalisation below must match NORMALISE in admin/build/sync_newsroom.py exactly.
{
  const crypto = require('crypto');
  const recordPath = path.join(ROOT, 'admin/build/newsroom-sync.json');
  if (fs.existsSync(recordPath)) {
    const record = JSON.parse(fs.readFileSync(recordPath, 'utf8'));
    const NORMALISE = [
      [/<nav class="site">[\s\S]*?<\/nav>/, '<nav class="site"></nav>'],
      [/<footer class="site">[\s\S]*?<\/footer>/, '<footer class="site"></footer>'],
      [/<span class="llmschip-m">[^<]*<\/span>/, '<span class="llmschip-m"></span>'],
      [/\u00b7 site v\d+\.\d+\.\d+ \u00b7/, '\u00b7 site \u00b7'],
      [/<span>newsroom\.sgit\.ai &middot; v\d+\.\d+\.\d+<\/span>/, '<span>newsroom.sgit.ai &middot; </span>'],
    ];
    let edited = 0;
    for (const [rel, entry] of Object.entries(record.files)) {
      const p = path.join(ROOT, rel);
      if (!fs.existsSync(p)) { errors.push(`${rel}: imported from sgit.ai and now missing — re-run the sync`); continue; }
      let buf = fs.readFileSync(p);
      if (/\.(html|md)$/.test(rel)) {
        let text = buf.toString('utf8');
        for (const [re, repl] of NORMALISE) text = text.replace(re, repl);
        buf = Buffer.from(text, 'utf8');
      }
      const got = crypto.createHash('sha256').update(buf).digest('hex');
      if (got !== entry.sha256) {
        if (edited++ < 20) errors.push(`${rel}: imported from sgit.ai and edited here — fix it on sgit.ai and re-sync`);
      }
    }
    if (edited > 20) errors.push(`… and ${edited - 20} more imported files edited here`);
  }
}

// --- 12. the article numbers hold ---------------------------------------------
// A reading list in a link (/for/#r=61,44,70) names articles by number, so the number is the
// contract: assigned once, in the order articles were first published, never changed, never
// reused. admin/build/ids.py keeps the file; this reads it as a stranger would.
{
  const idsPath = path.join(ROOT, 'articles/ids.json');
  const graphsPath = path.join(ROOT, 'articles/graphs.json');
  if (fs.existsSync(graphsPath)) {
    if (!fs.existsSync(idsPath)) errors.push('articles/ids.json is missing; run admin/build/ids.py');
    else {
      const doc = JSON.parse(fs.readFileSync(idsPath, 'utf8'));
      const entries = doc.articles || [];
      const live = JSON.parse(fs.readFileSync(graphsPath, 'utf8')).articles.map(a => a.slug);
      const byN = new Map(), bySlug = new Map();
      for (const e of entries) {
        if (!Number.isInteger(e.n) || e.n < 1) errors.push(`articles/ids.json: ${e.slug}: "${e.n}" is not a number from 1`);
        if (byN.has(e.n)) errors.push(`articles/ids.json: number ${e.n} is given to both ${byN.get(e.n)} and ${e.slug}`);
        if (bySlug.has(e.slug)) errors.push(`articles/ids.json: ${e.slug} has two numbers`);
        byN.set(e.n, e.slug); bySlug.set(e.slug, e.n);
      }
      for (const slug of live) if (!bySlug.has(slug)) errors.push(`articles/ids.json: ${slug} has no number; run admin/build/ids.py`);
      for (const e of entries) {
        if (!live.includes(e.slug) && !e.withdrawn) errors.push(`articles/ids.json: ${e.slug} is no longer published and is not marked withdrawn`);
        if (live.includes(e.slug) && e.withdrawn) errors.push(`articles/ids.json: ${e.slug} is published and marked withdrawn`);
      }
      const top = Math.max(0, ...entries.map(e => e.n));
      if (!(doc.next > top)) errors.push(`articles/ids.json: "next" (${doc.next}) is not above the highest number (${top}); a number would be reused`);
      // Against the last commit: no number moved, none dropped. In CI the working tree is the commit,
      // so this compares with its parent; before a commit it compares with HEAD.
      const prior = ref => { try {
        return JSON.parse(execFileSync('git', ['-C', ROOT, 'show', `${ref}:articles/ids.json`], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }));
      } catch (e) { return null; } };
      const same = JSON.stringify(entries.map(e => [e.n, e.slug]));
      let base = prior('HEAD');
      if (base && JSON.stringify((base.articles || []).map(e => [e.n, e.slug])) === same) base = prior('HEAD^') || base;
      if (base) {
        for (const e of base.articles || []) {
          const now = bySlug.get(e.slug);
          if (now === undefined) errors.push(`articles/ids.json: number ${e.n} (${e.slug}) was in the last release and is gone`);
          else if (now !== e.n) errors.push(`articles/ids.json: ${e.slug} was number ${e.n} in the last release and is now ${now}`);
        }
        if (doc.next < (base.next || 0)) errors.push(`articles/ids.json: "next" went down from ${base.next} to ${doc.next}`);
      }
    }
  }
}

// --- 13. the vendored vault library is unedited -------------------------------
// assets/vendor/sg-vault/v0.2.3 is the library that runs dev.vault.sgraph.ai, pinned at a commit and
// never edited here (one code base: a fix goes upstream and the copy is refreshed). VENDOR.md records
// each file's SHA-256; this recomputes them. A local addition lives in ../local/, which is not covered.
{
  const nodeCrypto = require('crypto');
  const vendorDir = path.join(ROOT, 'assets/vendor/sg-vault/v0.2.3');
  const vendorMd = path.join(vendorDir, 'VENDOR.md');
  if (fs.existsSync(vendorMd)) {
    const rows = [...fs.readFileSync(vendorMd, 'utf8').matchAll(/\| `([^`]+)` \| `([0-9a-f]{64})` \|/g)];
    if (rows.length !== 12) errors.push(`assets/vendor/sg-vault/v0.2.3/VENDOR.md records ${rows.length} files, not 12`);
    for (const [, relFile, want] of rows) {
      const p = path.join(vendorDir, relFile);
      if (!fs.existsSync(p)) { errors.push(`vendored vault library: ${relFile} is missing`); continue; }
      const got = nodeCrypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
      if (got !== want) errors.push(`vendored vault library: ${relFile} was edited here (hash differs from VENDOR.md); fix it upstream or refresh the copy`);
    }
  } else {
    errors.push('assets/vendor/sg-vault/v0.2.3/VENDOR.md is missing');
  }
}

// --- report ---------------------------------------------------------------
if (errors.length) {
  console.error(`validate: ${errors.length} error(s)`);
  for (const e of errors) console.error('  ✗ ' + e);
  process.exit(1);
}
console.log(`validate: OK — ${VERSION} on ${HOST}, ${htmlFiles.length} pages, ` +
            `${hubs.length} hubs in llms.txt, sitemap agrees, links resolve, blocks balanced, ` +
            `every page carries an agent block, provenance blocks sourced, no redacted material, ` +
            `no key-shaped strings, the imported newsroom unedited, the article numbers hold`);
