# SG Meter: a reading meter you can add to any website, sgit.ai

> One web component that charges readers a few pence a page from a balance kept in their own browser, by how far down the page they read; never blocks, allows a negative balance, lets a reader decline with a reason. Install, views, config, events, storage, theming, Stripe.

*Source: <https://newsroom.sgit.ai/meter/index.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Docs](https://sgit.ai/docs/index.md) / SG Meter

A library · v1.3.1

# SG Meter: a reading meter you can add to any website

One web component that charges readers a few pence a page from a balance kept in their own browser, by how far down the page they read. It never blocks a page, it lets the balance go below zero, it lets a reader decline to pay for a page and say why, and it turns what they read into personas: named, drawn as a graph, curated by the reader, and as many as they want. No server, no account, no cookies, no third-party script. It is what runs on this site: the balance in the top bar is it.

**What it is, and what it is not.** An honesty box, not a paywall. Everything it knows is in the reader's browser, so a reader can change their own balance, and the page a payment returns to cannot check the payment. That is a choice, made because of who reads a site like this one and what cheating would cost; it is argued in [the security model](security.md) and, with the numbers, in [who will game the reading meter](../articles/who-will-game-the-reading-meter.md). If you need a meter that holds money, this is the wrong library.

## Install

Copy two folders into your site, keeping their paths: the component and the base class it extends (it imports the base by a relative path).

```
assets/components/base/v1/v1.0/v1.0.0/sg-component.js
assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js
assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter-core.js
assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.tpl
assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.css
```

The paths are versioned and immutable, as in [the estate's JavaScript guidance](https://coding.sgit.ai/javascript/index.html): a fix is a new path, so a page that works today keeps loading the same files. Read them first; they are short: [the rules](../assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter-core.js) (no rendering), [the element](../assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js), [its styles](../assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.css), [the base class](../assets/components/base/v1/v1.0/v1.0.0/sg-component.js).

Then, on every page, load the module once, give it a config, and say what the page is:

```
<!-- in the top bar -->
<sg-meter view="balance"></sg-meter>

<!-- at the end of the text: charges this page, shows what it cost and the "don't charge me" choice -->
<sg-meter view="page" kind="article" date="2026-10-10" topics="news pricing" title="The page's title"></sg-meter>

<script type="application/json" id="sg-meter-config">
{ "storageKey": "mysite.meter.v1", "start": 500,
  "prices": { "article_new": 10, "article": 5, "page": 1, "free": 0 },
  "topup": { "amount": 500, "link": "https://buy.stripe.com/your-link" },
  "picks": { "feed": "articles/feed.json", "base": "articles/" } }
</script>
<script type="module" src="/assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js"></script>
```

Every key has a default, so an empty config works. Put `data-root` on `<html>` (for example `data-root="../"`) if your pages are not all at the top level; links the component writes are prefixed with it. This site loads the module with a dynamic `import()` from an inline script instead of a `src`, because its own build forbids script tags that point at files; either works.

## The eleven views

One element, one shared meter: an ES module is evaluated once per page, so however many `<sg-meter>` elements a page has, it is charged once.

| view | What it shows | Attributes |
|---|---|---|
| `balance` | The balance as a small link to the account. Shown in a warmer colour below zero, with a tooltip that says nothing is blocked. Nothing else: no banner, no count of articles read. |  |
| `page` | Opens this page on the meter and charges it by scroll depth. At the foot of the text, a reader card (v1.3): what the page has cost, the share read, the reading list, three five-step ratings (how useful, more like this, level of detail), and last, as the exception, "Don't charge me" with a reason. | `kind`, `date` (YYYY-MM-DD), `topics` (space separated), `title`, `quiet` (charge, show nothing) |
| `account` | Balance, pages opened, spend, what was declined, picks, spend by topic, the history with the depth read, top-ups; the top-up button and export as JSON. Version 1.3 also had pause and start again; version 1.4.0, which this site runs, does not. |  |
| `topup` | With `topup.link` set, one button to the payment page. Without, a simulated cart (packs, cart, review, receipt) that says it is simulated. |  |
| `topped-up` | The page a payment link returns to. Adds `topup.amount` once per `session_id` in the URL. It does not verify the payment; see [the security model](security.md#return). |  |
| `picks` | Unread pages for the active persona. Hidden until there is something to pick from. | `count` (default 4) |
| `newsroom` | The reader's own front page (v1.1): their personas as chips, the active one's name and description, its picks with Keep and Not for this persona on each, what was kept in it or put out, and its graph. | `count` (default 9) |
| `personas` | Rename, switch and remove personas, and add one from a preset or a blank one (v1.1). |  |
| `graph` | A persona drawn as an SVG graph (v1.1): the persona in the middle, its topics sized by weight, the pages behind each topic, and the citations between those pages, from the feed's `links_out`. Each page is a link, with its title and depth read as a tooltip. | `persona` (default the active one) |
| `link` | One line linking to the newsroom, named for the active persona (v1.1). |  |
| `share` | Shows the reader exactly what their reading looks like as text (a summary, then the same data as JSON), copies it to the clipboard, or sends it with their name and email, encrypted in the browser to the public key in `share.contact` and written to that file's append lane (v1.2). Sends nothing until the reader asks and ticks consent; never includes payment references. |  |

This site's own: [newsroom](../account/newsroom.md), [share](../account/share.md), [personas](../account/personas.md), [account](../account/index.md), [top-up](../account/top-up.md), [topped-up](../account/topped-up.md) (opened without a payment reference, it adds nothing and says so), and the link on [the front page](../articles/index.md).

## The rules it charges by

- **By depth.** A page costs its price times the deepest point the reader has scrolled to, measured on the page's `main` element and rounded to 5%, never less than `minDepth` (default a tenth), so opening a page is not free. Read half, pay half.
- **Once per page per session.** Scrolling further later in the same browser session tops the same charge up; coming back does not start a second one.
- **Below zero is allowed.** Nothing is blocked and nothing nags. The balance is shown, that is all.
- **Usefulness sets the price (v1.3).** The reader rates how useful the page was from 1 to 5, starting in the middle: 1 is free, 2 half, 3 the price, 4 one and a half times, 5 double (`rating.price`). "More like this" (1 to 5) moves the page's topics and tags in the active persona (`rating.more`); "level of detail" is kept as the persona's preference and shown in the newsroom. The scales start in the middle, drawn as an outline until the reader touches them.
- **The reading list (v1.3).** An article opened for the first time joins the active persona's reading list (`autoKeep`), unless the reader put it out of that persona; one tap removes it.
- **Declining is allowed.** A reader can refuse to pay for a page, with a reason: the headline promised more than the page gave, not relevant to me, I did not really read it, another reason. The charge is refunded and the reason kept in their history; "not relevant" counts against that page's topics in the picks.
- **New costs more.** An `article` whose `date` is within `newDays` is priced at `article_new`, judged in the reader's browser, so prices age without a rebuild. Any other `kind` is looked up in `prices`, falling back to `page`.
- **Storage may fail.** In a browser that blocks storage the page still works, and the account says it cannot keep a balance.

## Personas (v1.1)

A reader has one or more personas and one is active. They are a way to manage focus: the same reader reads differently as a founder and as a security lead, and wants different picks for each.

- **"me" always exists.** It is built from everything the reader reads, weighted by what each page cost them (so by depth), and named from the topics it reads most until the reader names it: with `names` set to `{"agents-and-policy": "The Policy Architect", …}`, a reader of agents and graphs becomes *The Policy Architect, with a streak of the Cartographer*.
- **Presets.** A site can offer starting personas in `personas.presets`: a name, a label, a colour, a description, a few topic weights and a handful of articles. Adding one makes it active.
- **Reading counts towards the active persona.** Each page opened records the persona that was active; a persona's profile is its preset, plus what was read while it was active, plus its curation.
- **Curation.** Any article can be kept in a persona (its topics and tags +5) or put out of it (−3, and never picked). The page view has "Keep in your persona"; the newsroom has Keep and Not for this persona on every pick.
- **Picks** score unread articles by the persona's topic weights plus twice its tag weights, so two personas on the same topics still differ.
- **Moving them.** The account view exports everything as JSON and restores it in another browser. Nothing syncs on its own yet.

This site's five presets (founder, journalist, security lead, AI builder, board member) are `PERSONAS` in its build, which refuses a preset that names an article that does not exist. Why personas, and why they are what a reader would pay to keep: [pay to keep your persona](../articles/pay-to-keep-your-persona.md).

## Config reference

| Key | Default | Meaning |
|---|---|---|
| `storageKey` | `"sg.meter.v1"` | The localStorage key. Use your own per site. (This site keeps `sgit.meter.v1`, the key its first meter used, so balances carried over.) |
| `start` | `500` | Starting credit, in pence or cents. |
| `symbol` | `"£"` | Shown before amounts. |
| `prices` | 10 / 5 / 3 / 2 / 2 / 1 / 0 | Price of a page read to the end, by kind: `article_new`, `article`, `issue`, `note`, `collection`, `page`, `free`. Add your own kinds. |
| `newDays` | `7` | How long an article is new. |
| `depth` | `true` | Charge by scroll depth. `false` charges the whole price on opening. |
| `minDepth` | `0.1` | The least share of a page that is charged. |
| `topup` | `{"amount": 500, "link": ""}` | The payment link and what it adds. Empty link: the simulated cart. |
| `packs` | `[{"id":"p5","price":500,"bonus":0}]` | The simulated cart's packs. |
| `links` | `{"account": "account/index.html", "topup": "account/top-up.html"}` | Where your account and top-up pages are, relative to `data-root`. |
| `picks` | `{"feed": "", "base": ""}` | A JSON feed of `{"articles": [{slug, title, date, teaser, topics}], "topics": [{id, label}]}`, and the folder an article's `slug + ".html"` is in. Empty feed: no picks. This site uses [articles/graphs.json](../articles/graphs.json). |

Config can also be given as `window.SG_METER_CONFIG` before the module loads.

## Events

Dispatched on `document`, bubbling and composed, named `<namespace>:<noun>.<verb>`. Event names are API: renaming one is a major version.

| Event | detail |
|---|---|
| `sg:meter.charged` | `{path, depth, cost, balance}`, each time a charge grows |
| `sg:meter.declined` | `{path, reason, balance}` |
| `sg:meter.toppedup` | `{credit, source, balance}`; source is `simulated` or `link` |
| `sg:meter.reset` | `{}` |
| `sg:meter.persona` | `{active, what}`; what is `active`, `added`, `renamed`, `removed` or `curated` (v1.1) |
| `sg:meter.rated` | `{path, field, value, cost, balance}`; field is `useful`, `more` or `detail` (v1.3) |
| `sg:meter.shared` | `{how, pages}`; how is `copied` or `sent` (v1.2) |
| `sg:meter.restored` | `{reads}`, after a restore from an export (v1.1) |
| `sg:meter.changed` | `{balance}`, on any saved change; the elements repaint on it |
| `sg-meter:error` | `{why}`, if the component's markup or styles failed to load; the element also gets `data-state="error"` |

Nothing listens to these on this site: there is no analytics. They are there so a site that wants to count, for example, how many readers decline and why, can do it in its own code and say so.

## What is stored

One JSON value under `storageKey` in localStorage, and a map of this session's pages under `storageKey + ".seen"` in sessionStorage. The reader can export it from the account page.

```
{ "v": 3, "created": "2026-10-10T09:00:00.000Z",
  "balance": -12.5, "spent": 512.5, "reads": 91, "declined": 14, "paused": false,
  "log": [ { "id": "…", "at": "…", "path": "/articles/x.html", "title": "…", "kind": "article",
             "topics": ["news"], "price": 10, "depth": 0.55, "cost": 5.5, "persona": "me",
             "rating": { "useful": 4, "more": 5, "detail": 4 },
             "declined": { "reason": "clickbait", "at": "…", "refunded": 4 } } ],
  "topups":   [ { "ref": "cs_…", "at": "…", "credit": 500, "source": "link" } ],
  "sessions": [ "cs_…" ], "cart": [],
  "active": "security-mv2h4bb2",
  "personas": [ { "id": "me", "name": "", "on": [], "off": [] },
                { "id": "security-mv2h4bb2", "preset": "security", "name": "",
                  "on": ["footprint-and-blast-radius"], "off": ["a-mac-of-the-agents-own"] } ] }
```

The log keeps the last 500 pages. Earlier states (versions 1 and 2) are read and upgraded in place; an upgraded state gets the "me" persona and keeps everything else.

## Theming

The component draws in a shadow root, so your stylesheet cannot reach in, but CSS custom properties cross the boundary and every colour reads one first: `--fg`, `--dim`, `--line`, `--line2`, `--panel`, `--accent`, `--accent-dk`, `--warm` (the colour of a negative balance), `--mono`, `--serif`, `--sans`. Each has a neutral fallback, so a site with none of them still gets a readable meter. The host element is yours to place and size: `sg-meter { display: block }`, and the root is exposed as `::part(root)`.

## Taking real payments with a Stripe Payment Link

1. In Stripe, create a product (for example "£5 of reading") and a **Payment Link** for it.
2. In the link's **After payment** settings, choose not to show Stripe's confirmation page and to redirect to your site, with this URL (Stripe fills in the placeholder):
`https://your.site/account/topped-up.html?session_id={CHECKOUT_SESSION_ID}`
3. Put the link in the config as `topup.link`, and the credit it buys as `topup.amount`.
4. Make a page at that path with `<sg-meter view="topped-up"></sg-meter>` on it.

Stripe's own guidance is that fulfilment should come from the `checkout.session.completed` webhook, not from the redirect, because a redirect can be skipped or faked. A static site has nowhere to receive a webhook, so this library credits on the redirect and says so. On a £5 payment with a standard UK card Stripe's listed fee is 1.5% + 20p, about 27.5p, or 5.5%; premium and international cards cost more. The arithmetic for this site is in [going live with the reading meter](../articles/going-live-with-the-reading-meter.md).

## Where its rules come from

The first version ran on [pt.newsroom.sgit.ai](https://pt.newsroom.sgit.ai/carteira/) as its wallet: says up front what it is, never blocks, one charge per page per session, storage allowed to fail. Its code follows [coding.sgit.ai's JavaScript guidance](https://coding.sgit.ai/javascript/index.html): ES modules, native web components on a shared base class, markup and styles in sibling files, page data set only as text, events as API. And two carried over from [the NFRs](https://nfrs.sgit.ai/), whose rule is "generate or date every number": the balance and the spend are running totals, but the log of every charge that made them sits beside them in the same export (the last 500), so a reader can check one against the other; and "a restore that has never been performed is not a backup", so the export is plain JSON a reader can open and read, the only copy of their history there is.

## Changelog

- **v1.3.1** (10 October 2026, site v0.7.36). The share view's Send button stays disabled until the reader ticks the box that lets the site keep the data; copying needs no box.
- **v1.3.0** (10 October 2026, site v0.7.34). The reader card at the foot of a page: three five-step ratings starting in the middle, usefulness setting the price (free to double), more-like-this moving the persona, level of detail kept as a preference; articles join the reading list when first opened; "don't charge me" moved to the end as the exception. Ratings are in what a reader shares. Events: `sg:meter.rated`. Config: `rating`, `autoKeep`, `links.how`.
- **v1.2.0** (10 October 2026, site v0.7.31). Sharing: the `share` view, `shareData()` in the core, the `share` config and the `sg:meter.shared` event. A reader sees the exact text, copies it, or sends it encrypted (sgit's hybrid envelope v2, RSA-OAEP-SHA256 and AES-256-GCM, with Web Crypto) into an append lane, with the fingerprint recomputed from the published key before anything is sent. The newsroom and account link to it.
- **v1.1.0** (10 October 2026, site v0.7.28). Personas: a default one built from all reading and named from its topics, presets offered by the site, as many as the reader wants, reading credited to the active one, Keep and Not for this persona. Four new views: `newsroom`, `personas`, `graph`, `link`. Picks score tags as well as topics. The account view draws the reader's graph and can restore an export. State version 3. v1.0.0 stays at its own path.
- **v1.0.0** (10 October 2026, site v0.7.26). First packaged release: scroll-depth charging, negative balances, decline with a reason, the balance view, the Stripe return page, picks that count "not relevant" against a topic. Replaces this site's `assets/meter.js` (v0.7.24), which charged on opening and showed a bar when credit ran out.

Next, not yet: rating a page, classifying it and keeping a note on it, all in the same local history; personas and a balance that follow a reader between devices, and to their agent, through an encrypted vault only they hold the key to. [Security model](security.md) · [this site's account page](../account/index.md).


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/meter/index.html)*
