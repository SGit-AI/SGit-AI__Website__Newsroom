# The wire's first screen: a front page, not a console

*15 October 2026, the designer agent's spec for @newsroom.wire, from the owner's ask of 14 October ("clean up that industry wire homepage... think of this as a user that arrives here for the first time... make it look as professional and as powerful as possible... send screenshots... including on emails"). Implemented in v0.12.70 as written, for all four wires; the screenshots of the real page are beside this note under `shots/first-screen-*`. Paths in the spec are the designer's scratch folder; the mock-up itself was not kept, the page is the record.*

# The Industry Wire home: the first screen, cleaned up

*15 October 2026, by the Designer for @newsroom.wire, from the owner's brief ("clean up that industry wire homepage… think of a user that arrives here for the first time… make it look as professional and as powerful as possible… I will send screenshots"). Everything here is against the page as it is this morning (edition of 2026-10-15, 97 stories, 18 new, read live from vault u9i9jp0l at 07:47 UTC) and the pictures under `wire/infographics/`. Files beside this one: `mockup.html` (the first screen as static HTML on the real data, the site's own stylesheets copied beside it plus `mock.css`, which is section 9 verbatim), the screenshots `mockup-{newsprint,night}-{desk,phone,share}.png` and the full-page `…-desk-full.png` / `…-phone-full.png`, the images it uses, and `live.json` (the live page's header dumped as text, 07:47 UTC).*

## 1. What a first-time visitor sees today, measured

At 1280 wide the page goes: nav (57 px) · crumb · eyebrow "INDUSTRY NEWS, READ FROM A VAULT · BETA" · h1 · a three-line blurb · the wires strip · **a grey mono box** ("Read from vault u9i9jp0l at 07:47 UTC · commit baaaaf0e20d8: 2026-10-15.1 morning edition… 9 objects fetched, 0 from cache · 97 stories in 5 beats · [Check for a new commit]") · the edition box with a long meta line ("daily edition: news from late 14 and early 15 October not yet on the wire, plus re-checks… · covers 2026-10-14 to 2026-10-15 · ai-generated, unreviewed · 97 stories from 269 publishers") · the editor's note in a callout · the hero at 560 px · the cost line · the corrections callout (blue, ~180 px) · the verifier's three records (green, ~330 px) · three thread cards · three folded graphs · the inbox bar (first-visit line, the whole release note open, six filters, the amber "only in this browser" box, ~420 px) · the lens row · the lens note · and then **The lead**, at about 2,900 px. On a phone the first story is at roughly 9,000 px. The fold at 1280×800 holds the crumb, the eyebrow, the title, the blurb, the strip, the grey box and the first lines of the meta line: plumbing, and not one headline. On a phone the fold holds the eyebrow, the title and the blurb.

Nothing on that list is wrong to have on the page. It is in the wrong order for someone who does not yet know what the page is, and for a screenshot.

## 2. The rule

**News first, record second, plumbing last.** The first screen is a masthead and today's edition: the wire's name, the date, the hero, the editor's note, the three threads, the lead. The desk's record (corrections, the verifier, the graphs, the edition's description) is one folded row under it. The reader's own state (the inbox bar) appears when there is state. The site's plumbing (vault id, commit, fetch counts, the re-check button, what the pictures cost) is one quiet line at the foot, with an anchor from the masthead for anyone who wants it. Every feature stays; nothing from the vault is drawn differently (text nodes only); the status *ai-generated, unreviewed* stays on the first screen, in the dateline.

## 3. The first screen at 1280×800, element by element

Top to bottom. "DOM" names what exists in `wire.py` / `wire.js` today; "change" is what moves. The screenshot is `mockup-newsprint-desk.png` / `mockup-night-desk.png`.

| # | Element | DOM | Change |
|---|---|---|---|
| 1 | Site nav | `nav.site` (chrome.py) | none |
| 2 | Crumb "Home / The Industry Wire" | `main.doc > p.crumb` (page.py) | none; tighter margin (CSS) |
| 3 | **The wires strip** as the eyebrow: "The wires: **The Industry Wire** · The AWS Wire · The OWASP Wire · The Portugal Wire · Day by day · The charter · For the desks" | `p.eyebrow > span.wires` | wire.py: `edition_page()` passes `eyebrow=wires_strip(cfg, tag="span")` and drops the strip from `body`; `wires_strip()` gains a `tag` argument (`p` today, `span` here). The old eyebrow text goes; "beta" moves to the dateline (5) |
| 4 | **The title** "The Industry Wire" | `main.doc > h1` | none; 2.5rem (CSS). The three-line `p.lead` blurb under it is **removed**: `lead=""` for the edition page; its sentence already opens "What this is" at the foot (make sure the beats sentence is there, it is: `about`) |
| 5 | **The dateline**: "EDITION OF THURSDAY 15 OCTOBER 2026 · DAILY · BETA" | `.edition > p.k` | wire.js: `Edition of ` + `h('time', { datetime: brief.edition }, longDate(brief.edition))` + (`wireMeta.cadence` when the vault gives one) + ` · beta`. `longDate` formats a value that passes `EDITION` (`/^\d{4}-\d{2}-\d{2}$/`) with `toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' })` and returns the value unchanged otherwise; the ISO date stays in `datetime`. The vault's value is kept, only displayed long |
| 6 | **The status line**: "97 stories from 269 publishers · 18 new in this edition, 9 updated · ai-generated, unreviewed · live from the wire's vault" | `.edition > p.meta` | wire.js: `brief.counts`, `brief.new_in_edition.length`, `updatedIds.size`, `brief.status` as written, then `h('a', { href: '#wire-status' }, 'live from the wire\'s vault')`. The sentence that is `brief.kind` and the window move to the "This edition" fold (12). A 2px rule under it closes the masthead (CSS) |
| 7 | **The hero**, 400 px square at the left | `.edition .today > figure.ig.hero` (from `picture()`) | wire.js: a new wrapper `div.today` holds the hero and `div.side`. `picture()` draws the caption as `chip` + ` ${model} · ${usd(cost)} ` + `details.ig-prompt` whose summary is `· the prompt` (the separator inside the summary, so the share view can hide it). The seconds and the sentence "The text is the record; the picture illustrates it." leave the caption and are said once, at the cost line (18) |
| 8 | **"THE EDITOR'S NOTE"** kicker and the note, serif, bare | `.today > .side > p.k` + `p.note` | wire.js: the kicker is a new `p.k`; the note is the existing `p.note` (`brief.editor_note`, unchanged). CSS strips newsroom.css's `.note` callout |
| 9 | **The three threads** as one-line rows: title, "6 stories", a triangle; open to the note and the ids | `.side > div.threads > details.thread > summary > b` + `span.n`; body `p` + `div.ids` | wire.js: `h('details', { class: 'thread' }, h('summary', {}, h('b', {}, t.title), h('span', { class: 'n' }, \`${ids.length} stories\`)), t.note ? h('p', {}, t.note) : null, h('div', { class: 'ids' }, …))`. Same text nodes, now folded |
| 10 | **The lead line**: "THE LEAD XBOW used OpenAI's public GPT-5.6 Sol… The 96 other stories, by beat, below · Subscribe by email" | `.side > p.leadline > b` + `a[href=#sec-24]` + `span.more > a[href=#subscribe]` | wire.js: new; headline is `tx(lead, 'headline')` as text, the link is to the story card on the page (the primary link is on the card) |
| 11 | *(the fold at 800 px falls here)* | | |
| 12 | **The desk's record, folded**, one row: "▸ This edition · ▸ Corrections and updates (9) · ▸ Checked independently (27 stories) · ▸ The edition as graphs (3)" | `.edition > div.folds > details` ×4 | wire.js: wrapper `div.folds`. "This edition" holds the old `p.meta` text (`brief.kind` · covers from–to). "Corrections and updates (N)" holds the existing `p.corrections` (N = `updatedIds.size`, omitted when 0). "Checked independently (N stories)" holds the existing `div.checks#wire-checks` (N = rows across the records). "The edition as graphs (3)" is `details.graphs#wire-graphs` wrapping the three existing `details.graph` (`#wire-byday`, `#wire-threads`, `#wire-entities`) with their summaries unchanged. Each is drawn only when its content exists, as today |
| 13 | **The inbox bar**, quiet | `section.inbox#wire-inbox` | see section 6 |
| 14 | **Read as** row and the lens note | `div.lens`, `p.lens-note`, `div.lens.langs` on Portugal | none but spacing |
| 15 | **The lead** story card, then the beats | `h2.beat` "The lead", `article.story.lead`, … | none. The story's own card picture floats right as today |
| 16 | Map / stack extras (OWASP, AWS) | `details.extra` | none; they stay after the bar, before the stories |
| 17 | **The status line** at the foot: "Read from vault u9i9jp0l at 07:47 UTC · commit baaaaf0e20d8: 2026-10-15.1 morning edition… · 9 objects fetched, 0 from cache · 97 stories in 5 beats · [Check for a new commit]" | `div#wire-status.wire-status` | wire.py `loader()`: write the div **after** `#wire-mount`, not before (all four `data-wire` pages; the mount's own "Opening the vault…" placeholder covers the loading state). CSS: a line with a top rule, not a box |
| 18 | **What the pictures cost** | `p.ig-cost#wire-pictures` | wire.js: drawn after the mount's content (append to `mount` last, or to `status`'s parent); text as today plus the sentence "The text is the record; the picture illustrates it." once |
| 19 | What this is · Subscribe · Where it comes from · For an agent | as today | none |

Deadlines (the AWS wire's `div.deadlines#wire-deadlines`) go into `div.side` above the threads: they are dated and they are that wire's point. The personal brief (`section.personal`) is unchanged, under the named reader's lens.

## 4. The first screen on a phone (390×844)

`mockup-newsprint-phone.png` / `mockup-night-phone.png`. The nav is two rows on a phone (site chrome, 95 px). Then crumb, the wires strip on one scrolling line with a fade at the right edge (CSS mask, no literal colour), the title at 2.05rem, the dateline on two lines, the status line on three, the rule, then the **hero at full width (358 px)** which ends at 715 px, its caption, the kicker "THE EDITOR'S NOTE" and the first two lines of the note. So the phone's first screen is masthead + hero + the note beginning; the three threads, the lead line and the folded row follow on the first scroll; the inbox bar and the lens are at about 1,500 px; the lead story at about 1,900 px (today: about 9,000 px). The `.today` grid is one column under 760 px; everything else is the same DOM.

## 5. The masthead, the hero, the note, the lead, the disclosure

- **Masthead.** The strip of wires (small, dim) over the title (serif, 2.5rem) over the dateline (accent, uppercase, letterspaced) over the status line (mono, dim) over a 2px rule in `--fg`. It reads as a newspaper's front: name, date, edition, and the one honest line that says what it is. "Beta" and "ai-generated, unreviewed" are on the first screen in both views.
- **The hero and the note share the band.** The picture at the left (400 px, 1:1 as the models return it), the note at the right in the serif at 1.06rem, bare, under a small kicker. The two say the same thing twice on purpose: the picture is the note drawn, the text is the record. On a phone the picture comes first because it is the thing people will share, and the note under it.
- **The threads** are the "three lines" the owner's screenshot needs: three titles the desk wrote, each with its story count, each opening to the desk's note and the story ids. They are drawn folded so the band stays four things: picture, note, three lines, the lead.
- **The lead** is one line in the band (kicker + headline, linked to its card) and the full card first under the beats, as today, with *Why it leads*. The band does not repeat the card.
- **The AI-image disclosure** stays under every picture, on the first screen and in the share crop: the `AI image` chip, the model, the cost to the cent, and *the prompt* on request. It is one short mono line at .74rem under a 400 px picture, which is visible and not loud. The seconds and the explanatory sentence move to the cost line at the foot, which also carries the edition's, the month's and the running totals, as today. Honesty is kept per picture; the explanation is said once.

## 6. The inbox bar: when it shows what

`drawBar()` gets three states, decided by `const hasState = !!visit.prev || N.list().length > 0 || pending().count > 0`.

1. **First visit, no state** (the mock-up): one line, `p.since#wire-since`: "Your first visit to the wire in this browser: **97 stories, all new**. Decide at each story (done, read later, follow up…) and this bar becomes your inbox; choose who you read as to split the stories into for you and not for you." Then the desk's latest release note **folded**: `details.releases#wire-releases` with the summary `b` title · stamp · edition and the body `p.sum` + the Added/Updated id lists (same text nodes as today, inside a details). No filters (they would all say 97), no amber "only in this browser" box, no "Nothing decided here yet" (CSS hides `.pending.ok`; the seen-only state is said at the foot status line: "97 stories seen in this browser only, not yet in your vault").
2. **A returning visit** (`visit.prev` set): the "Since your last visit… N new, X for you" line as today; the releases since the visit as `details.releases` **open** when there are any; the six filters with counts; the pending line only when `pending().count > 0` (a decision is waiting), with *Update the vault* and *Open the vault* as today.
3. **Any decision made in this visit**: as 2, and the toast (`p.toast#wire-kept`) as today.

The bar keeps its id, its classes and its role; it sits after the folded row and before the lens, as today.

## 7. The shareable view

**The first screen done right is enough for a casual screenshot** (`mockup-*-desk.png` is one), but a promotional picture wants no nav, no crumb, no strip and a fixed size, so the page gets a **`?share` view, no new page**: one line in `wire()`, `if (new URLSearchParams(location.search).has('share')) document.documentElement.setAttribute('data-share', '')`, and the `html[data-share]` rules in section 9. The view is the masthead (title, dateline, status line) and the band (hero at 430 px, the note, the three thread titles with counts, the lead line); everything else is `display:none`. At **1200×630** it fills the frame with 30 px to spare at the foot (`mockup-newsprint-share.png`, `mockup-night-share.png`); at 1280×800 the same view leaves white space under the band, so for a laptop-shaped picture screenshot the plain page's first screen instead. The disclosure chip stays in the crop; the prompt link does not (it is a control, not a fact).

To take one: `node shot_wire.mjs <root> 'wire/?share' out` with a 1200×630 context (the tool's sizes are fixed today; add `[1200, 630, 'share']` to its list when the page is `wire/?share`). The same view is what a build step could screenshot into `og/wire-<edition>.jpg` for the page's `og:image` later; not asked for here.

On a phone, `?share` is the same one-column band; a 390×844 shot of it is masthead + hero + the note.

## 8. A finding while reading the pictures: cards vanish between editions

`pictures(edition)` reads only `infographics/<brief.edition>/ledger.json`. This morning the vault moved to 2026-10-15 before that edition's ledger existed, so the live page showed **no hero and no cards at all**, including the thirteen 13 October cards whose stories are still on the page. The lead says a story keeps its card across editions; the page does not read them. Fix in `pictures()`: read `infographics/ledger.json` first, take `Object.keys(total.editions)` sorted newest first, read each edition's ledger, build `byStory` by first-seen (newest edition wins, `at` newest first within one), and take the **hero from the current edition only** (an older hero under a newer dateline would be wrong; the page is complete without one). File paths become `infographics/${e.edition}/${e.file}`, so each ledger entry carries its edition when merged. Six lines.

## 9. Tokens and CSS

This is `mock.css` verbatim: the rules to add to `wire/wire.css` (which loads before `themes.css`, so the tokens resolve for all five themes). No literal colours; the two new wrappers (`div.today`, `div.folds`) and the new elements (`p.leadline`, `details.thread`, `details.releases`, `details.graphs`, `p.eyebrow > span.wires`) are the ones section 3 names; nothing changes a text node. The rules in `wire.css` today that these override: `.edition`, `.edition .k`, `.edition .meta`, `.edition .note`, `.threads`, `.thread`, `.thread b`, `.edition .ig.hero`, `.inbox`, `.inbox .releases`, `.wire-status`, `.edition details.graph`, `.wires`. The old `.wires` rule (`margin: -.4rem 0 1.2rem`) and `.edition .ig-cost` can be deleted.

```css
/* 1. The masthead: the strip of wires is the eyebrow, the title, then the dateline. The edition header loses
      its box: at the top of a page a box is a notice, and the edition is the page. */
main.doc .crumb { margin-bottom: .35rem; }
main.doc .eyebrow { margin: 0 0 .15rem; }
main.doc .wires { display: block; font: 400 .8rem/1.6 var(--sans); letter-spacing: 0; text-transform: none; color: var(--dim); white-space: nowrap; overflow-x: auto; scrollbar-width: none; }
main.doc .wires a { margin-right: .75rem; }
main.doc h1 { margin: 0 0 .2rem; font-size: 2.5rem; line-height: 1.1; letter-spacing: -.012em; }
.edition { padding: 0; border: 0; border-radius: 0; background: none; margin: 0 0 1.1rem; }
.edition .k { margin: 0; font: 700 .74rem/1.6 var(--sans); letter-spacing: .16em; text-transform: uppercase; color: var(--accent-dk); }
.edition .meta { margin: .05rem 0 0; padding: 0 0 .65rem; border-bottom: 2px solid var(--fg); font: .78rem/1.6 var(--mono); color: var(--dim); }
.edition .meta a { color: var(--accent-dk); text-decoration: none; }

/* 2. The today band: the hero at the left, the editor's note and the threads at the right; one column on a phone. */
.edition .today { display: grid; grid-template-columns: minmax(0, 400px) minmax(0, 1fr); gap: 1rem 2rem; align-items: start; margin: .9rem 0 0; }
.edition .ig.hero { max-width: none; margin: 0; }
.edition .ig.hero img { border-radius: 6px; }
.edition .ig figcaption { margin-top: .35rem; font-size: .74rem; }
.edition .today .note { margin: 0 0 .8rem; padding: 0; border: 0; border-radius: 0; background: none; box-shadow: none; font: 1.06rem/1.52 var(--serif); color: var(--fg); }
.edition .today .side > .k { margin: .1rem 0 .2rem; }
.threads { display: block; margin: 0; border-top: 1px solid var(--line); }
.thread { padding: .5rem 0; border: 0; border-bottom: 1px solid var(--line); border-radius: 0; background: none; font-size: .88rem; }
.thread > summary { cursor: pointer; list-style: none; display: flex; align-items: baseline; gap: .55rem; }
.thread > summary::-webkit-details-marker { display: none; }
.thread > summary::before { content: '\25B8'; color: var(--accent); font-size: .8em; flex: none; }
.thread[open] > summary::before { content: '\25BE'; }
.thread b { display: inline; margin: 0; font: 700 1.02rem/1.35 var(--serif); color: var(--head); }
.thread .n { margin-left: auto; font: .72rem/1.5 var(--mono); color: var(--dim2); white-space: nowrap; }
.thread > p { margin: .35rem 0 0; color: var(--text); }
.thread .ids { margin-top: .3rem; }
.edition .leadline { margin: .8rem 0 0; font-size: .95rem; line-height: 1.45; }
.edition .leadline > b { display: inline-block; margin-right: .5rem; font: 700 .7rem/1.6 var(--sans); letter-spacing: .14em; text-transform: uppercase; color: var(--accent-dk); vertical-align: .08em; }
.edition .leadline a { font: 700 1.05rem/1.4 var(--serif); color: var(--head); text-decoration: none; }
.edition .leadline a:hover { color: var(--accent-dk); text-decoration: underline; }
.edition .leadline .more { margin-left: .5rem; font-size: .82rem; color: var(--dim); }

/* 3. The desk's record for the edition, folded into one row: corrections, the verifier, the graphs. The texts
      and their classes are unchanged; only the wrapper and the summaries are new. */
.edition .folds { display: flex; flex-wrap: wrap; gap: .2rem 1.3rem; margin: .9rem 0 0; padding: .45rem 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); font-size: .84rem; }
.edition .folds > details { margin: 0; flex: 0 1 auto; }
.edition .folds > details[open] { flex: 1 1 100%; }
.edition .folds > details > summary { cursor: pointer; color: var(--accent-dk); }
.edition .folds > details[open] > summary { font-weight: 600; }
.edition .folds .corrections, .edition .folds .checks { margin: .5rem 0 .4rem; }
.edition .folds .corrections > b, .edition .folds .checks > b { display: none; }   /* the summary already says it */
.edition details.graph { margin: 0; }
.edition .folds .graphs > .graph { margin: .5rem 0 .3rem; }
.edition .folds .graph > figure, .edition .folds .graph > .graph { margin: .6rem 0 .4rem; }

/* 4. The inbox bar: one quiet line on a first visit; the release note folded; the filters only once there is
      something to filter (wire.js draws them when the reader has state; the mock-up shows the first visit). */
.inbox { margin: 1rem 0 .9rem; padding: .55rem .9rem; font-size: .86rem; }
.inbox p.since { margin: 0; }
.inbox details.releases { margin: .35rem 0 0; padding: .3rem .7rem; }
.inbox details.releases > summary { cursor: pointer; }
.inbox details.releases > summary b { color: var(--fg); }
.inbox details.releases > .release { margin-top: .4rem; }
.inbox .filters { margin: .45rem 0 0; }
.inbox .pending.ok { display: none; }

/* 5. The lens row and the note under it: one line each, tighter. */
.lens { margin: 0 0 .5rem; }
.lens-note { margin: 0 0 1rem; font-size: .82rem; }

/* 6. The foot: the status line as a line, not a box, and the cost of the pictures beside it. */
.wire-status { margin: 1.8rem 0 .3rem; padding: .55rem 0 0; border: 0; border-top: 1px solid var(--line); border-radius: 0; background: none; font-size: .76rem; }
main.doc .ig-cost { margin: 0 0 1.2rem; font: .78rem/1.5 var(--mono); color: var(--dim); }

/* 7. The share view: ?share on the address sets html[data-share]; the page becomes the masthead and the band,
      1200 wide, for a 1200×630 screenshot. Nothing else changes. */
html[data-share] nav.site, html[data-share] footer.site, html[data-share] main.doc > :not(h1):not(#wire-mount),
html[data-share] #wire-mount > :not(.edition), html[data-share] .edition .folds, html[data-share] .edition .leadline .more, html[data-share] .ig-prompt { display: none; }
html[data-share] main.doc { max-width: 1200px; padding: 26px 44px 30px; }
html[data-share] main.doc h1 { font-size: 2.5rem; }
html[data-share] .edition .today { grid-template-columns: 430px 1fr; gap: 1rem 2.2rem; margin-top: .9rem; }
html[data-share] .edition .today .note { font-size: 1.02rem; line-height: 1.5; }
html[data-share] .thread .ids, html[data-share] .thread > p { display: none; }
html[data-share] .edition .leadline { margin-top: .6rem; }

/* 8. The phone. */
@media (max-width: 760px) {
  main.doc .wires { mask-image: linear-gradient(90deg, var(--fg) 88%, transparent); -webkit-mask-image: linear-gradient(90deg, var(--fg) 88%, transparent); padding-right: 2rem; }
  main.doc h1 { font-size: 2.05rem; }
  .edition .today { grid-template-columns: 1fr; gap: .8rem; }
  .edition .today .note { font-size: 1.02rem; }
  .edition .folds { gap: .2rem .9rem; }
}
```

`.eyebrow` in newsroom.css is uppercase, letterspaced and accent-coloured; the `.wires` rule above resets the three so the strip reads as a line of links. The mask on the phone is an alpha mask: any opaque colour works, so `var(--fg)` is used rather than a literal. The `.flag.new` and `.story.new` literals already in wire.css (`#f0a020`, `#f0c070`) are not mine but are the only literal colours on the page; a `--mark`/`--warn-line` swap would close that.

## 10. The hour, in order (wire.js and wire.py)

1. `wire.py`: `wires_strip(cfg, up=None, tag="p")`; `edition_page()` passes `eyebrow=wires_strip(cfg, tag="span")`, drops the strip from `body`, passes `lead=""`; `loader()` writes `#wire-status` after `#wire-mount`. Sources/how/reach pages keep their eyebrow and lead.
2. `wire.js` `edition()`: build `header` as `section.edition` with `p.k` (dateline, `longDate`), `p.meta` (counts, new, updated, status, the `#wire-status` link), `div.today` (`picture(… 'hero')` when `pics.hero`; `div.side` with `p.k` "The editor's note", `p.note`, `div.deadlines` when any, `div.threads` of `details.thread`, `p.leadline` when `brief.lead.story` is on the page), `div.folds` (details "This edition", corrections, checks, `details.graphs` of the three graphs). Same data, same text nodes, two wrappers and a handful of `details`.
3. `picture()`: caption = chip, model, cost, `details.ig-prompt` with summary "· the prompt"; the seconds and the sentence go to the `ig-cost` line, which is appended after `body` (last in the mount).
4. `drawBar()`: the `hasState` branch of section 6; `details.releases` instead of `div.releases` (open when `releases.length` and the visit is not the first).
5. `wire()`: the `?share` line; the status `foot()` text gains the seen-only clause when `pending().any && !pending().count`.
6. `pictures()`: the cross-edition merge of section 8.
7. `wire.css`: section 9 added, the five superseded rules removed.
8. Test with the shot tool at 1280×800, 390×844 and `wire/?share` at 1200×630, in Newsprint and Night; compare with the `mockup-*.png` here.

## 11. What the mock-up is and is not

`mockup.html` is the proposed DOM with the real text of the 15 October edition (editor's note, threads, lead, counts, the release note, the verifier's words, three stories of the first beat) and the real pictures: the 15 October hero (`edition.abcc840d.webp`, made at 07:46 this morning) and the cards for ai-15 and ai-16 (the first two the run made). Mocked, because the 15 October ledger was not written when this was built: the hero's cost is shown as $0.24 (the 13 October hero's figure and the plan's estimate) and the cards' as $0.14 (the plan's); the three graph bodies are placeholders; the nav tools are static pills; the provenance strip on the lead is a four-dot stand-in. Everything else is text copied from the live page (`live.json`). It was shot three times and corrected between rounds (the note's callout box removed, the hero sized so the lead line clears the 800 px fold, the record row made one line, the prompt link shortened, the phone strip made one scrolling line with a fade); the final shots are the ones kept.

## Summary

The Industry Wire's home should open as a front page, not a console: the strip of wires, the title, a dateline that says the day, the cadence and *ai-generated, unreviewed*, then one band with the edition's hero at the left and, at the right, the editor's note, the three threads as three folded lines with their story counts, and the lead's headline. Under that band the desk's record (this edition's description, corrections, the verifier, the graphs) folds into one row; the inbox bar shows one line on a first visit and its full self once the reader has state; the vault id, commit, fetch counts, the re-check button and the picture ledger become one quiet line at the foot, linked from the dateline. Every feature stays, every vault value is drawn as the same text, and the AI-image chip with model and cost stays under every picture. A `?share` switch (one JS line, ten CSS lines) turns the page into masthead-plus-band for a 1200×630 screenshot, which the mock-up shows is sendable in Newsprint and Night; the plain first screen at 1280×800 and 390×844 is sendable too. One bug surfaced on the way: `pictures()` reads only the current edition's ledger, so this morning every 13 October card vanished from the page; it should merge every edition's ledger for the cards and take the hero from the current edition alone.
