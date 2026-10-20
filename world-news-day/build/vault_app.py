#!/usr/bin/env python3
"""world-news-day/ — the vault app.

    python3 world-news-day/build/vault_app.py      (build.py runs it)

Writes world-news-day/vault-app/{index.html, app.json, app-data.json}, which vault.py places
at the root of the corpus vault. Opening the vault then launches this instead of showing a
file tree: the finding, the twenty-one pieces, every sentence typed and anchored, and the
vocabulary — rendered from the vault's own encrypted bytes, in the reader's browser, with no
server and no account.

That is the argument this section makes, executed rather than described. The corpus is
evidence somebody else published; the app is a projection of it; the vault is both the
storage and the distribution. Sharing the key IS sharing the app.

THE AUTHORING CONTRACT, which is not optional. Vault HTML runs in an iframe from a blob: URL,
so the browser fetches resources before the vault bridge exists. Therefore:

  · all CSS and JS are inlined — no <link href> and no <script src> against a vault path;
  · nothing is fetched declaratively; data comes from `sg.vfs.readText()` at runtime;
  · `fetch()` of a vault path is NOT patched and will 404, so it is only ever the first hop
    of a fallback chain;
  · a compact FALLBACK is inlined so the page also works saved to disk or previewed outside
    App Mode;
  · the page posts `sg-app-ready` when it has rendered, or the host shows a spinner forever.

The fallback carries the headline numbers and the list of pieces; the full claim and term
detail is read from app-data.json inside the vault, which is what makes this an app over a
vault rather than a page with a copy of the data glued to it.
"""
import json
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
OUT = SEC / "vault-app"
SITE = "https://newsroom.sgit.ai/world-news-day"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


def build_data():
    corpus, lic, ana = load("corpus.json"), load("licences.json"), load("analysis.json")
    claims, terms, aff = load("claims.json"), load("terms.json"), load("affiliations.json")
    reg, graph = load("register.json"), load("graph.json")
    by_art = {}
    for c in claims["claims"]:
        by_art.setdefault(c["article"], []).append(
            {"n": c["n"], "t": c["type"], "a": c["anchor"], "k": c["terms"]})
    themes = {}
    nodes = {n["id"]: n for n in graph["nodes"]}
    for e in graph["edges"]:
        if e["verb"] == "touches":
            themes.setdefault(e["source"].split(":", 1)[1], []).append(nodes[e["target"]]["label"])
    roles = {r["author"]: r for r in aff["people"]}
    src = {s["id"]: s for s in reg["sources"]}

    pieces = []
    for a in sorted(corpus["articles"], key=lambda x: x["order_in_announcement"]):
        pieces.append({
            "n": a["order_in_announcement"], "slug": a["slug"], "title": a["title"],
            "url": a["url"], "published": a["published"][:10], "words": a["words"],
            "by": [{"name": b,
                    "role": roles.get(b, {}).get("role_as_printed", ""),
                    "orgs": roles.get(b, {}).get("organisations", [])} for b in a["byline"]],
            "links": a["outbound_links"],
            "themes": sorted(themes.get(a["slug"], [])),
            "sha256": src.get(a["source_page"], {}).get("sha256", ""),
            "claims": by_art.get(a["slug"], []),
        })
    return {
        "title": "World News Day 2026",
        "subtitle": "Twenty-one op-eds, one permission, no licence",
        "snapshot": corpus["snapshot"],
        "site": SITE,
        "counts": {
            "articles": corpus["count"], "words": corpus["total_words"],
            "frozen": reg["count"],
            "named_licence": lic["counts"]["carrying_a_named_public_licence"],
            "ldjson": lic["counts"]["with_ld_json"],
            "ldjson_licence": lic["counts"]["whose_ld_json_declares_a_licence"],
            "wordings": lic["counts"]["distinct_prose_statements"],
            "nolinks": ana["evidence"]["with_no_outbound_link_at_all"],
            "total_links": ana["evidence"]["total_links"],
            "domains": ana["evidence"]["distinct_domains"],
            "claims": claims["counts"]["claims"],
            "proposals": claims["counts"]["by_type"].get("proposal", 0),
            "assertions": claims["counts"]["by_type"].get("assertion", 0),
            "definitions": terms["counts"]["definitions_found"],
            "by_type": claims["counts"]["by_type"],
        },
        "statement": lic["the_statement"][0]["text"],
        "announcement": lic["the_two_statements"]["on_the_announcement"],
        "licence_rows": [
            ["Pieces in the corpus", lic["counts"]["articles"]],
            ["…carrying a prose permission to republish", lic["counts"]["carrying_a_prose_permission"]],
            ["…carrying a named public licence", lic["counts"]["carrying_a_named_public_licence"]],
            ["…mentioning Creative Commons", lic["counts"]["carrying_a_creative_commons_reference"]],
            ["…carrying rel=\"license\"", lic["counts"]["carrying_rel_license"]],
            ["…carrying a copyright notice", lic["counts"]["carrying_a_copyright_notice"]],
            ["…shipping schema.org JSON-LD", lic["counts"]["with_ld_json"]],
            ["…whose JSON-LD declares the terms", lic["counts"]["whose_ld_json_declares_a_licence"]],
        ],
        "terms": [{"t": x["term"], "n": x["articles"], "o": x["occurrences"],
                   "def": x["defined_in"]} for x in terms["terms"]],
        "definition_finding": terms["the_finding"],
        "claim_rules": [{"id": r["id"], "label": r["label"], "means": r["means"]}
                        for r in claims["rules"]],
        "pieces": pieces,
    }


APP_JSON = {
    "entry": "index.html",
    "present": True,
    "auto_open": True,
    "title": "World News Day 2026 — the corpus",
    "permissions": {},
    "hud": {"mode": "default", "show": {"print": True}},
}

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>World News Day 2026 — the corpus</title>
<style>
:root{
  --paper:#faf9f7; --panel:#fff; --ink:#17181b; --dim:#5c5f66; --dim2:#8a8d94;
  --line:#e7e4dd; --line2:#d8d4cb; --red:#b91c1c; --teal:#0f766e; --amber:#b45309;
  --purple:#7c3aed; --blue:#1d4ed8; --cyan:#0369a1;
  --serif:ui-serif,Georgia,'Iowan Old Style',serif;
  --sans:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --measure:720px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}
a{color:var(--teal);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:var(--measure);margin:0 auto;padding:0 1.2rem}
.wide{max-width:1080px;margin:0 auto;padding:0 1.2rem}

header.hero{background:#241416;color:#f6f2ee;padding:3.4rem 0 2.6rem;
  background-image:radial-gradient(ellipse at 20% -10%,#3a1e22 0%,#241416 60%)}
header.hero .eyebrow{font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;
  color:#e0a0a0;font-weight:700;margin:0 0 .8rem}
header.hero h1{font-family:var(--serif);font-size:clamp(1.9rem,4.6vw,2.9rem);
  line-height:1.15;margin:0 0 .7rem;letter-spacing:-.015em}
header.hero p{color:#cfc5bd;margin:0;font-size:1.02rem;max-width:34em}
header.hero .meta{margin-top:1.2rem;font-family:var(--mono);font-size:.7rem;
  color:#9c8f88;letter-spacing:.04em}

nav.sticky{position:sticky;top:0;z-index:40;background:rgba(250,249,247,.94);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
nav.sticky .row{max-width:1080px;margin:0 auto;padding:.55rem 1.2rem;display:flex;
  gap:1.3rem;overflow-x:auto;scrollbar-width:none}
nav.sticky .row::-webkit-scrollbar{display:none}
nav.sticky a{font-size:.82rem;color:var(--dim);white-space:nowrap;padding:.15rem 0;
  border-bottom:2px solid transparent}
nav.sticky a.on{color:var(--ink);font-weight:600;border-bottom-color:var(--red)}

section{padding:2.8rem 0;scroll-margin-top:58px}
section.alt{background:#f4f1ec;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
h2{font-family:var(--serif);font-size:1.62rem;margin:0 0 .5rem;letter-spacing:-.01em}
h3{font-size:1.02rem;margin:1.6rem 0 .5rem}
.lead{font-size:1.06rem;color:#31333a}
.dim{color:var(--dim)} .small{font-size:.86rem}
.mono{font-family:var(--mono)}

.stats{display:grid;gap:.7rem;grid-template-columns:repeat(auto-fit,minmax(158px,1fr));margin:1.4rem 0}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:.85rem .9rem}
.stat b{display:block;font-size:1.45rem;color:var(--teal);letter-spacing:-.02em;line-height:1.1}
.stat b.bad{color:var(--red)}
.stat span{display:block;font-size:.78rem;color:var(--dim);line-height:1.4;margin-top:.25rem}
.stat em{display:block;font-style:normal;font-family:var(--mono);font-size:.62rem;
  color:var(--dim2);margin-top:.35rem;line-height:1.45}

.claimbox{font-family:var(--serif);font-size:1.12rem;line-height:1.6;background:var(--panel);
  border-left:4px solid var(--red);border-radius:0 10px 10px 0;padding:1rem 1.2rem;margin:1.3rem 0;
  border-top:1px solid var(--line);border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
.quote{font-family:var(--serif);font-size:1rem;background:var(--panel);border:1px solid var(--line);
  border-left:3px solid var(--amber);border-radius:0 10px 10px 0;padding:.9rem 1.1rem;margin:.9rem 0}
.quote b{display:block;font-family:var(--sans);font-size:.72rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--amber);margin-bottom:.4rem}

table{width:100%;border-collapse:collapse;font-size:.9rem;background:var(--panel);
  border:1px solid var(--line);border-radius:11px;overflow:hidden}
th{background:#f1eee8;text-align:left;padding:.55rem .8rem;font-size:.68rem;letter-spacing:.09em;
  text-transform:uppercase;color:var(--dim);font-weight:700}
td{padding:.52rem .8rem;border-top:1px solid var(--line);vertical-align:top}
td.num{font-family:var(--mono);font-weight:700;color:var(--teal);width:3.5rem}
td.num.z{color:var(--red)}
.tw{overflow-x:auto}

.pieces{display:grid;gap:.6rem;margin:1.2rem 0}
.piece{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:.8rem .95rem;
  cursor:pointer;transition:border-color .12s ease,transform .12s ease}
.piece:hover{border-color:var(--red)}
.piece .t{font-family:var(--serif);font-size:1.02rem;margin:0 0 .25rem;color:var(--ink)}
.piece .by{font-size:.8rem;color:var(--dim)}
.piece .tags{margin-top:.45rem;display:flex;gap:.3rem;flex-wrap:wrap}
.tag{font-family:var(--mono);font-size:.62rem;padding:.1rem .4rem;border-radius:99px;
  border:1px solid var(--line2);color:var(--dim)}
.tag.z{color:var(--red);border-color:#e3b9b9}
.piece .n{float:right;font-family:var(--mono);font-size:.72rem;color:var(--dim2)}

.sheet{position:fixed;inset:0;z-index:90;background:rgba(20,16,15,.55);display:none;
  align-items:flex-end;justify-content:center}
.sheet.open{display:flex}
.sheet .inner{background:var(--paper);width:min(880px,100%);max-height:92vh;overflow-y:auto;
  border-radius:16px 16px 0 0;padding:1.4rem 1.3rem 2.4rem;box-shadow:0 -8px 40px rgba(0,0,0,.3)}
.sheet .x{float:right;border:1px solid var(--line2);background:var(--panel);border-radius:8px;
  font-size:.8rem;padding:.25rem .6rem;cursor:pointer;color:var(--dim)}
.sheet h3{font-family:var(--serif);font-size:1.3rem;margin:.2rem 0 .4rem}
.cl{display:flex;gap:.55rem;padding:.35rem 0;border-top:1px solid var(--line);align-items:baseline}
.cl .i{font-family:var(--mono);font-size:.68rem;color:var(--dim2);min-width:2rem}
.cl .k{font-family:var(--mono);font-size:.6rem;text-transform:uppercase;letter-spacing:.06em;
  padding:.05rem .35rem;border-radius:99px;border:1px solid currentColor;white-space:nowrap}
.cl .a{font-size:.88rem;color:#31333a}

.bar{height:.55rem;border-radius:4px;background:var(--teal);display:inline-block;vertical-align:middle}
.bar.z{background:var(--red)}

footer{background:#241416;color:#bdb0a9;padding:2.4rem 0;font-size:.88rem}
footer b{color:#f0e8e2}
footer .lock{display:inline-block;vertical-align:-2px;margin-right:.4rem}
@media(max-width:620px){ section{padding:2rem 0} .sheet .inner{max-height:96vh} }
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <p class="eyebrow">World News Day · 28 September 2026</p>
    <h1 id="hTitle">Twenty-one op-eds, one permission, no licence</h1>
    <p id="hSub">Loading…</p>
    <p class="meta" id="hMeta"></p>
  </div>
</header>

<nav class="sticky"><div class="row" id="nav"></div></nav>

<section id="finding"><div class="wrap">
  <h2>The finding</h2>
  <p class="lead" id="findLead"></p>
  <div class="stats" id="stats"></div>
  <div class="claimbox" id="claim"></div>
</div></section>

<section id="terms-of-use" class="alt"><div class="wrap">
  <h2>The terms, quoted</h2>
  <p class="small dim">The only statement of terms anywhere on a piece, and the announcement's
  different wording. Both read from frozen, hashed bytes.</p>
  <div id="quotes"></div>
  <div class="tw" style="margin-top:1.2rem"><table>
    <thead><tr><th>Of the twenty-one</th><th>Count</th></tr></thead>
    <tbody id="licRows"></tbody></table></div>
</div></section>

<section id="pieces"><div class="wide">
  <h2>The twenty-one</h2>
  <p class="small dim">In the order the announcement lists them. Tap any piece for every
  sentence in it, typed and anchored. <b>The prose is not here</b> — each piece links to its
  original.</p>
  <div class="pieces" id="list"></div>
</div></section>

<section id="vocabulary" class="alt"><div class="wrap">
  <h2>The vocabulary</h2>
  <div class="claimbox" id="defFinding"></div>
  <div class="tw"><table>
    <thead><tr><th>Term</th><th>Pieces</th><th>Uses</th><th>Defined?</th></tr></thead>
    <tbody id="termRows"></tbody></table></div>
</div></section>

<section id="shapes"><div class="wrap">
  <h2>What the sentences do</h2>
  <p class="small dim">Every sentence typed by a published formula, first match wins. A type
  says this sentence has this shape — not that it is true, and not that the author is biased.
  An op-ed is supposed to evaluate and propose.</p>
  <div class="tw"><table>
    <thead><tr><th>Shape</th><th>Count</th><th>Share</th><th>What it means</th></tr></thead>
    <tbody id="shapeRows"></tbody></table></div>
</div></section>

<div class="sheet" id="sheet"><div class="inner" id="sheetInner"></div></div>

<footer><div class="wrap">
  <p><span class="lock">&#128274;</span><b>This page is a little HTML on top of an encrypted
  vault, rendered straight from it.</b> There is no server and no account: the link-holder
  holds the key, and SGraph never sees the contents. The corpus, the description, the code
  that produced it and the gate that checks it are all in here together — the experience and
  the evidence are the same artifact.</p>
  <p class="small">Our description is CC BY 4.0. The twenty-one op-eds are not ours and are
  not relicensed; their terms are on their own pages, and none of their prose is reproduced
  here. <span id="foot"></span></p>
</div></footer>

<script>
const FALLBACK = /*__DATA__*/{};
const TYPE_COLOUR = {assertion:'#5c5f66',hypothesis:'#7c3aed',quantified:'#0f766e',
  evaluation:'#b45309',question:'#1d4ed8',attribution:'#0369a1',proposal:'#b91c1c'};

async function getData(){
  // sg.vfs is the ONLY supported way to read a vault file; fetch() is not patched.
  try{
    if (window.sg && sg.vfs && sg.vfs.readText){
      const t = await sg.vfs.readText('app-data.json');
      const j = JSON.parse(t);
      if (j && j.pieces) return j;
    }
  }catch(e){ console.warn('[app] vfs read failed, using inlined copy', e); }
  try{
    const r = await fetch('app-data.json',{cache:'no-store'});
    if (r.ok){ const j = await r.json(); if (j && j.pieces) return j; }
  }catch(e){}
  return FALLBACK;
}

function el(t,c,h){const e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e;}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));}
function n(x){return Number(x).toLocaleString('en-GB');}

function build(d){
  const c = d.counts;
  document.getElementById('hTitle').textContent = d.subtitle;
  document.getElementById('hSub').textContent =
    c.articles + ' commissioned op-eds, fetched and frozen on one day. ' + n(c.words) +
    ' words held here, and not one of them republished.';
  document.getElementById('hMeta').textContent =
    'snapshot ' + d.snapshot + ' · ' + c.frozen + ' frozen files, each hashed';

  const secs = [['finding','The finding'],['terms-of-use','The terms'],['pieces','The twenty-one'],
                ['vocabulary','Vocabulary'],['shapes','Sentence shapes']];
  const nav = document.getElementById('nav');
  secs.forEach(([id,label])=>{ const a=el('a',null,label); a.href='#'+id; a.dataset.s=id; nav.appendChild(a); });

  document.getElementById('findLead').textContent =
    'All ' + c.articles + ' of these pieces say you may republish them. Not one says so under ' +
    'a licence with a name — nothing with a version and a URL that a machine could match or a ' +
    'lawyer could read.';

  const stats = [
    [c.articles, 'op-eds, frozen and hashed', n(c.words)+' words, none republished', false],
    [c.named_licence, 'carry a named public licence', 'no Creative Commons, no version, no URL', true],
    [c.ldjson_licence+' of '+c.ldjson, 'declare terms in their JSON-LD', 'the structured data is already there', true],
    [c.nolinks+' of '+c.articles, 'offer the reader no link at all', c.total_links+' links across the whole corpus', true],
    [c.domains, 'distinct domains cited', 'none reached by two pieces', false],
    [c.proposals+' of '+n(c.claims), 'sentences propose anything', c.assertions+' are flat assertions', true],
    [c.definitions, 'places a word is defined', 'over '+n(c.claims)+' sentences', true],
  ];
  const sg_ = document.getElementById('stats');
  stats.forEach(([v,l,e,bad])=>{
    const s = el('div','stat');
    s.appendChild(el('b', bad?'bad':null, esc(v)));
    s.appendChild(el('span',null,esc(l)));
    s.appendChild(el('em',null,esc(e)));
    sg_.appendChild(s);
  });

  document.getElementById('claim').innerHTML =
    'The terms are stated three different ways. The articles require republication <b>in full</b> ' +
    'and never mention credit; the announcement requires <b>appropriate credit</b> and never says ' +
    'in full. A newsroom that follows one is not following the other.';

  const q = document.getElementById('quotes');
  q.appendChild(el('div','quote','<b>On each article</b>“'+esc(d.statement)+'”'));
  q.appendChild(el('div','quote','<b>On the announcement</b>“'+esc(d.announcement)+'”'));

  const lr = document.getElementById('licRows');
  d.licence_rows.forEach(([label,v])=>{
    const tr = el('tr'); tr.appendChild(el('td',null,esc(label)));
    tr.appendChild(el('td','num'+(v===0?' z':''),String(v))); lr.appendChild(tr);
  });

  const list = document.getElementById('list');
  d.pieces.forEach(p=>{
    const card = el('div','piece');
    card.appendChild(el('span','n','#'+p.n));
    card.appendChild(el('p','t',esc(p.title)));
    card.appendChild(el('p','by',esc(p.by.map(b=>b.name).join(' · ')) +
      (p.by[0] && p.by[0].orgs.length ? ' — '+esc(p.by[0].orgs.join(', ')) : '')));
    const tags = el('div','tags');
    tags.appendChild(el('span','tag',p.claims.length+' sentences'));
    tags.appendChild(el('span','tag'+(p.links.length?'':' z'),
      p.links.length ? p.links.length+' links' : 'no links offered'));
    (p.themes||[]).slice(0,3).forEach(t=>tags.appendChild(el('span','tag',esc(t))));
    card.appendChild(tags);
    card.addEventListener('click',()=>openPiece(p));
    list.appendChild(card);
  });

  document.getElementById('defFinding').textContent = d.definition_finding;
  const tr_ = document.getElementById('termRows');
  d.terms.slice().sort((a,b)=>b.n-a.n||b.o-a.o).forEach(t=>{
    const r = el('tr');
    r.appendChild(el('td',null,'<b>'+esc(t.t)+'</b>'));
    r.appendChild(el('td','num',String(t.n)));
    r.appendChild(el('td','num',String(t.o)));
    r.appendChild(el('td','small dim', t.def && t.def.length ? 'yes' : '—'));
    tr_.appendChild(r);
  });

  const sr = document.getElementById('shapeRows');
  const tot = c.claims || 1;
  (d.claim_rules||[]).forEach(r=>{
    const v = (c.by_type||{})[r.id] || 0;
    const row = el('tr');
    const col = TYPE_COLOUR[r.id] || '#5c5f66';
    row.appendChild(el('td',null,'<span style="display:inline-block;width:.6em;height:.6em;'+
      'border-radius:50%;background:'+col+';margin-right:.45em"></span>'+esc(r.label)));
    row.appendChild(el('td','num',String(v)));
    row.appendChild(el('td',null,'<span class="bar'+(r.id==='proposal'?' z':'')+
      '" style="width:'+Math.max(2,Math.round(160*v/tot))+'px"></span> '+
      '<span class="small dim mono">'+Math.round(100*v/tot)+'%</span>'));
    row.appendChild(el('td','small dim',esc(r.means)));
    sr.appendChild(row);
  });

  document.getElementById('foot').innerHTML =
    'Everything here is published at <a href="'+esc(d.site)+'/">newsroom.sgit.ai</a>.';

  wireNav(secs.map(s=>s[0]));
  ready();
}

function openPiece(p){
  const s = document.getElementById('sheet'), i = document.getElementById('sheetInner');
  i.innerHTML = '';
  const x = el('button','x','Close'); x.addEventListener('click',closeSheet); i.appendChild(x);
  i.appendChild(el('h3',null,esc(p.title)));
  i.appendChild(el('p','small dim',
    p.by.map(b=>'<b>'+esc(b.name)+'</b>'+(b.role?' — '+esc(b.role):'')).join('<br>')));
  i.appendChild(el('p','small', 'Published '+esc(p.published)+' · '+n(p.words)+' words · '+
    '<a href="'+esc(p.url)+'">read it at worldnewsday.org →</a>'));
  i.appendChild(el('p','small dim mono','sha256 '+esc((p.sha256||'').slice(0,32))+'…'));
  if (p.themes && p.themes.length)
    i.appendChild(el('p','small dim','Themes: '+esc(p.themes.join(', '))));
  i.appendChild(el('p','small dim', p.links.length
    ? 'Offers the reader '+p.links.length+' link'+(p.links.length>1?'s':'')+'.'
    : 'Offers the reader no link at all.'));
  i.appendChild(el('h3',null,'Every sentence'));
  i.appendChild(el('p','small dim','An anchor is at most eight words, verbatim, so you can '+
    'find the sentence in the original. The sentence itself is not stored here.'));
  p.claims.forEach(c=>{
    const row = el('div','cl');
    row.appendChild(el('span','i',String(c.n)));
    const k = el('span','k',esc(c.t)); k.style.color = TYPE_COLOUR[c.t]||'#5c5f66';
    row.appendChild(k);
    row.appendChild(el('span','a','“'+esc(c.a)+'…”'));
    i.appendChild(row);
  });
  s.classList.add('open');
  i.scrollTop = 0;
}
function closeSheet(){ document.getElementById('sheet').classList.remove('open'); }
document.getElementById('sheet').addEventListener('click', e=>{
  if (e.target.id === 'sheet') closeSheet();
});
document.addEventListener('keydown', e=>{ if (e.key === 'Escape') closeSheet(); });

function wireNav(ids){
  const links = Array.from(document.querySelectorAll('nav.sticky a'));
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es=>{
    es.forEach(e=>{
      if (e.isIntersecting){
        links.forEach(a=>a.classList.toggle('on', a.dataset.s === e.target.id));
      }
    });
  }, {rootMargin:'-55px 0px -70% 0px'});
  ids.forEach(id=>{ const n2 = document.getElementById(id); if (n2) io.observe(n2); });
}

function ready(){
  try{ window.parent && window.parent.postMessage({type:'sg-app-ready'},'*'); }catch(e){}
}

getData().then(build).catch(err=>{
  console.error('[app] build failed', err);
  document.getElementById('hSub').textContent = 'Could not load the corpus data.';
  ready();
});
</script>
</body>
</html>
"""


def main():
    OUT.mkdir(exist_ok=True)
    data = build_data()
    compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    assert "\n" not in compact, "a raw newline leaked into the inlined fallback"
    (OUT / "app-data.json").write_text(json.dumps(data, ensure_ascii=False) + "\n",
                                       encoding="utf-8")
    (OUT / "app.json").write_text(json.dumps(APP_JSON, indent=2) + "\n", encoding="utf-8")
    html = HTML.replace("const FALLBACK = /*__DATA__*/{}",
                        "const FALLBACK = /*__DATA__*/" + compact)
    assert "/*__DATA__*/{}" not in html, "the fallback placeholder was not replaced"
    (OUT / "index.html").write_text(html, encoding="utf-8")
    kb = len(html.encode()) / 1024
    print(f"vault app: index.html {kb:.0f} KB (fallback inlined), "
          f"app-data.json {len(compact) / 1024:.0f} KB, {len(data['pieces'])} pieces")
    return data


if __name__ == "__main__":
    main()
