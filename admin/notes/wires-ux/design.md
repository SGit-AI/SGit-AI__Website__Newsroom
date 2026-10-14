# The wires, redesigned: five pages, one system

*13 October 2026, by the Designer, from the owner's voice memo of the same day and the four vaults' real data (Industry u9i9jp0l, OWASP eitf274v, AWS v202bla5, Portugal). Mock-ups beside this file: `overview.html`, `aws.html`, `owasp.html`, with screenshots at 390 and 1280 in Newsprint and Night (`shot-*.png`). One recommendation per page, not options.*

## One system (what is the same on all five)

Every wire page has the same spine, top to bottom. The reader learns it once.

1. **Masthead**: crumb, eyebrow, title, one-sentence lead, then the **wires tab row** (All wires · Industry 59 · OWASP 19 · AWS 88 · Portugal 36) with the story count on each tab. One row replaces today's `p.wires` sentence and the nav sub-menu as the way between wires.
2. **Status line** (mono): edition, cadence, window, releases, status (`ai-generated, unreviewed`), vault id. Honest and small.
3. **The inbox bar**, kept exactly as the inbox note specifies: since your last visit N new, X for you and Y not under the lens; the latest release note open, earlier ones since the visit folded; the six filters with counts (Inbox, New, Read later, Follow up, Done, Everything); the pending line with *Update the vault*. The inbox comes before anything visual because working the inbox is the job the reader comes to do.
4. **The today band**: the edition's **hero infographic (16:9)** on the left and a **KPI row of stat tiles** on the right (hero figure first, then two or three tiles that are the wire's own: deadlines on AWS, projects named on OWASP, article-ready on Portugal, corrected on Industry). On a phone the hero comes first, tiles in a 2×2 grid below.
5. **Read as** (the lens row) and, on Portugal only, **Read in** (EN · PT), with the lens note saying what the join matched.
6. **The charts band**: a grid of chart cards, each with a title, a one-line sub, the chart, a legend when there are two or more series, and an *As a table* twin. One wide card holds the wire's defining graph (the stack, the projects graph, the ecosystem map, the threads); the rest are small cards.
7. **The personal brief**, under the named reader's lens only, as the vault wrote it.
8. **Beats**: each beat header carries the reach/withheld count and a tiny sparkline of its stories per day; then **story cards** (square infographic left, text right), the withheld stories folded under *Not for you (n), and why* with *Should reach me* and *Done*.
9. **About, subscribe, for an agent**: as today.

**Chart system** (dataviz skill): one hue for magnitude and emphasis (the site's teal, lifted to `--viz-1`), de-emphasis gray (`--viz-mute`) for "withheld / not for you / everything else", a three-step single-hue ordinal ramp for licence tiers C→B→A (`--viz-ord-1..3`), and a three-slot categorical palette only where series are the subject (the three threads of a brief). Validated with the skill's validator against the site's surfaces: light `#0e8f7c,#eb6834,#6250d6` on `#faf9f5` (all-pairs pass, worst CVD ΔE 9.0), dark `#1fa392,#d95926,#9085e9` on `#0f1115` (worst CVD ΔE 13.1); ordinal light `#5bb5a6,#1a9683,#0b5e52`, dark `#1d6e63,#22948a,#3fcbb9`, both pass. The site's own `--accent` fails the chroma floor in Newsprint and the lightness band in Night, which is why the chart tokens are separate; they belong in `themes.css`, one block per theme, under the themes test. Marks: bars ≤ 24px with a 4px rounded data-end, 2px surface gaps in stacks, solid hairline grid, selective labels (the extreme and the last), a hover tooltip on every mark, status colours (`--warn-*`, `--danger-*`) only for deadlines, always with an icon and a word. No wire gets its own colour: four wires are told apart by name and position, never by hue.

**The decisions and the inbox** are unchanged in meaning: Done, Read later, Follow up, Not for me, More like this, Wrong, at the foot of every card; a decided story folds to its headline in Everything and Done; *Should reach me* on withheld stories; everything local first, counted on the pending line, sent on *Update the vault*. New on the overview: a decision made there is a note with the wire's `path`, so it is the same record the wire page would have written.

## The infographics

**Where.** Two sizes, nowhere else. The **edition hero, 16:9** (1920×1080, the banner size the site already makes for articles), top of the today band, one per edition per wire, and the newest one as *the infographic of the day* on the overview. The **story card, 1:1** (1024², the size every model returns without cropping), 150px wide at the left of the story card on a laptop, 60% wide above the headline on a phone. Square was chosen over 4:5 because it sits beside text at any width and because the square models (GPT-5 Image) cannot do otherwise.

**What they must contain.** The hero: the wire's title and date as the only title, the editor's note as the document (`brief.editor_note`), the thread titles, and only the numbers in that note. The card: a claim of at most eight words written by the desk (a new field, `card.claim`; the mock derives it from the headline), at most one figure and only if it is in the headline, the primary's publisher as a caption, the beat as a corner word. **Never**: platform names or logos, people's faces, dates, URLs, hex codes, "source:" lines, a footer, any number not given, and never the model's name on the image. The prompts in the mock-ups follow the bake-off's rules: "no other text", "no numbers other than those given", the format said as a ratio.

**Which model.** Cards on Nano Banana 2.1 (~$0.04, 9 s), with the edition's hero attached to every card as the style reference, which is the bake-off's fix for consistency across a set. Heroes on GPT-5.4 Image 2 (~$0.18, 83 s), given the document, which is where it wins. A redo is paid for and counted.

**How the page stays honest.** Every image has an `AI image` chip, the cost and the model in its badge, and a *The prompt, the model, the check* disclosure under it with the full prompt, OpenRouter's recorded cost and the check that was run (OCR of every required string, the Designer agent's blind score). The image is never the only carrier of a fact: the card's text says everything the picture says. The vault stores `images/<story-id>.png` with `images/<story-id>.json` (`model, cost_usd, seconds, prompt, reference, generated_at, checks`), the page draws the image from an http(s) URL in that record and nothing else, and `alt` is the headline. The overview's **cost ledger** sums it per wire per day. An edition without images is still a complete page: the placeholder is the hatched block in the mock-ups.

## The five pages

### The overview, `/wire/` (new)

**Reader and job.** The owner, most mornings, on a phone: "what is going on, across all of it, and what is for me". Also the first visitor, who needs to see there are four wires and what each is.

**Shape.** Status line → today band (infographic of the day, from the wire whose newest release changed the most stories; tiles: new across the wires, for you, releases today, the pictures today) → *What the desks released today* (every `releases[]` entry dated today across the four vaults, newest first, with the wire chip and added/updated counts; two columns on a laptop) → Read as, one lens for all wires, with a note naming the wires that carry that persona → **the four wire tiles** (name, cadence, edition; the lead headline and `lead.why_it_leads`; stories · new · for you · sources; a sparkline of stories per day; *Open the wire*) → **The best of today**: the four leads, and under the named reader's lens the top two of each `brief.personal.top`, ranked, each with a provenance strip and four decisions → **Across the wires**: small multiples of stories per day per wire on one scale (column, `stories[].date` × `deliveries.status` under the lens), *For you across the wires* (stacked horizontal bar per wire, reached vs withheld), *Where the primaries stand* (stacked bar per wire, `primary.tier` A/B/C/none on the ordinal ramp), *Fetched and checked* (bar, `primary_fetched` count, verifier rows from `factcheck-*.json` in the tooltip) → **What the pictures cost** (table: cards × $0.04, heroes × $0.18, per wire, a total and a month at this rate).

On a phone the same order, one column; the release list and the tiles stack. The best-of list is the thing to scroll.

```
LAPTOP  /wire/                                   PHONE
┌──────────────────────────────────────────────┐ ┌────────────────┐
│ The wires   [All][Industry 59][OWASP][AWS][PT]│ │ The wires      │
│ today · wires 4 · stories 202 · vaults · stat │ │ tabs ▸▸▸ scroll│
│ ┌────────────────────┐ ┌──────┐ ┌──────┐     │ │ ┌────────────┐ │
│ │ INFOGRAPHIC OF THE │ │ new  │ │for you│     │ │ │ HERO 16:9  │ │
│ │ DAY 16:9  (AWS)    │ │ 162  │ │  83   │     │ │ └────────────┘ │
│ │ AI image·$0.18     │ ├──────┤ ├──────┤     │ │ ┌─────┐┌─────┐ │
│ └────────────────────┘ │rel 9 │ │$7.74 │     │ │ │ 162 ││ 83  │ │
│ ▸ The prompt, the model, the check            │ │ └─────┘└─────┘ │
│ ┌ What the desks released today ────────────┐ │ │ releases today │
│ │ 22:20 [Portugal] Verifier's fixes · 4 upd │ │ │ 22:20 PT …     │
│ │ 21:55 [Portugal] First edition  · 36 added│ │ │ READ AS chips  │
│ └───────────────────────────────────────────┘ │ │ ┌ Industry ──┐ │
│ READ AS [Everyone][Dinis][Founder]…           │ │ │ lead…      │ │
│ ┌Industry─┐┌OWASP───┐┌AWS─────┐┌Portugal┐     │ │ │ 59 19 14 ∿ │ │
│ │lead     ││lead    ││lead    ││lead    │     │ │ └────────────┘ │
│ │59 19 14 ││19 19 13││88 88 29││36 36 27│     │ │ (×4)           │
│ │ ∿∿∿     ││ ∿∿∿    ││ ∿∿∿    ││ ∿∿∿    │     │ │ BEST OF TODAY  │
│ └─────────┘└────────┘└────────┘└────────┘     │ │ 1 [Industry] … │
│ THE BEST OF TODAY                             │ │   Done·Later·… │
│ 1 [Industry] UK sets out…   Done Later Follow │ │ ACROSS WIRES   │
│ 2 [OWASP] New owasp.org…    Done Later Follow │ │ ▂▃▅▂ per wire  │
│ ACROSS THE WIRES                              │ │ for you ▬▬▬░░  │
│ ┌ per day, 4 rows ─┐ ┌ for you ▬▬▬▬░░░ ─────┐ │ │ tiers ▬▬▬░     │
│ │ ▂▃▅▂▁▇  Industry │ │ tiers  ▬▬▬▬▬░░       │ │ │ LEDGER table   │
│ └──────────────────┘ └──────────────────────┘ │ └────────────────┘
│ WHAT THE PICTURES COST  table + total         │
└──────────────────────────────────────────────┘
```

### The Industry Wire, `/wire/`-edition (today's page, redesigned)

**Reader and job.** The named reader and the six public personas, daily: empty the inbox, see what changed since Sunday, and know which of 59 stories is for them. Two editions are live (40 from 11 Oct, 19 new), 13 corrected.

**What is its own.** Tiles: stories, new, **corrected 13** (the `changes` count, the Updated flag's number), primaries fetched 32 of 59. Charts: **Beats** (stacked horizontal bar per beat, `stories[].beat`, new in this edition in teal vs earlier in gray, from `brief.new_in_edition`); **Threads as timelines** (the wide card: three rows from `brief.threads[].stories` on a date axis from `stories[].date`, one categorical slot per thread, a dot per story with the headline on hover; this is the Historian's view GRAPHS.md asks for); **Who the week names** (horizontal bar of entities in two or more stories, `entities.orgs|products|tech` counted: Anthropic 15, OpenAI 12, Microsoft 7…, each bar linking to its stories: entity co-occurrence drawn as the honest bar, not a hairball); **Who the edition reaches** (bar per persona, the lens in colour). The provenance strip on every card: primary dot large, hollow when `primary_fetched` is false (27 of 59, which is this wire's weak point and should be visible), coverage dots on the tier ramp. The correction note in blue stays under the story.

```
┌ Industry ─────────────────────────────────────┐
│ inbox: 19 new, 14 for Dinis, 5 not · releases │
│ ┌ HERO 16:9 ┐ [59 stories][19 new][13 corr][32/59 fetched]
│ READ AS · lens note                           │
│ ┌ threads timeline (wide) 04 Oct ── 12 Oct ───┐
│ │ weaponised agents  ●──●──●───●──●           │
│ │ trust in plumbing      ●─●──●──●──●         │
│ │ compute & capital   ●──●────●──●──●         │
│ └─────────────────────────────────────────────┘
│ [beats stack][who the week names][who it reaches]
│ PERSONAL BRIEF (dinis)                        │
│ CYBERSECURITY 17 · ∿  ┌[card]│ headline … ┐    │
└───────────────────────────────────────────────┘
```

### The OWASP Wire, `/wire/owasp/` (mocked: `owasp.html`)

**Reader and job.** AppSec leads, project leaders, members, weekly: what OWASP shipped and decided, and which project a story belongs to. The named reader's job is governance season (voting opens 15 Oct) and the licence question.

**What is its own: the projects graph.** The wide card has two halves. Left, **stories per project**: a horizontal bar for each of the 20 `map.entities[]`, joined by the rule in GRAPHS.md (name or alias in the story's entities or text), sorted, the zeros kept visible in muted ink (8 of 20 had no story: a signal). Right, **one project**, the query not the graph: `leaders[]` on the left joined by *is_led_by*, the project as the centre node with its `facts.Level`, the stories that name it on the right joined by *is_named_by*, `standards[]` as a *maps to* line below, and the facts (latest release, repository, page) as links only when http(s). Clicking a bar, or a *project:* chip on a story card, redraws it. Other charts: **the fortnight by week** (columns in week bins, reached vs withheld, because the wire is weekly and September context is in it) and **who it reaches**. Tiles: stories, projects named 12 of 20, corrected 1 (ow-09, the licence correction, which is also the lead), primaries fetched 19 of 19 with 9 tier A.

```
┌ OWASP ──────────────────────────────────────────┐
│ inbox: 19 new, 13 for you · correction to ow-09 │
│ ┌ HERO 16:9 ┐ [19][12 of 20 projects][1 corr][19/19]
│ ┌ projects graph (wide) ─────────────────────────┐
│ │ GenAI Sec Project ▬▬▬▬▬ 5 │ leads(5)   named by(5)│
│ │ Top 10            ▬▬▬▬▬ 5 │ Clinton ─┐  ┌─ ow-09 │
│ │ Mobile AppSec     ▬▬ 2    │ Dawson ──┤●├── ow-17 │
│ │ …                         │ Wilson ──┘  └─ ow-05 │
│ │ Cheat Sheets      | 0     │ maps to: Crosswalk   │
│ └───────────────────────────────────────────────┘
│ [by week ▂▂▁▂▃▇▆][who it reaches]                 │
│ PROJECTS AND RELEASES 2 reach, 1 withheld         │
│ ┌[card]│ Dependency-Track 5.2.0 … project: CycloneDX ┐
└─────────────────────────────────────────────────┘
```

### The AWS Wire, `/wire/aws/` (mocked: `aws.html`)

**Reader and job.** One reader with a declared stack, daily: what touched Lambda, S3, API Gateway, CloudFront and boto3, what has a date on it, and the firehose kept out of the way but never hidden. 29 of 88 reach; 59 are What's New, withheld with the reason.

**What is its own: the stack and the deadlines.** The hero tile is **29 of 88 touched your stack** with a same-ramp meter; beside it the two nearest `stack.deadlines[]` as status tiles with days left (3 days: re:Invent refund, in danger red with ⚠; 18 days: python3.10 end of support, in warning amber with ◷; status colour always with an icon and a word), the later two in the graph's footer. The wide card is **your stack as a graph**: the reader node, *runs*, a curved edge to each `stack.services[]` and `extra_concerns[]`, and *is touched by* as a bar of the items whose `deliveries[].connections[].concern` matched (Lambda 16, S3 11, boto3 9, CloudFront 6, API Gateway 3, Python on Lambda 2); clicking a service filters the story list to its items; on a phone the same graph is drawn as rows, the reader as the heading. Then **items per day** (columns, `stories[].date`, touched vs withheld), **per beat** (stacked bar, What's New as the long gray bar, the point of the wire made visible), **who it reaches**. The What's New beat renders folded under the lens: the firehose is a list with reasons, one *Should reach me* each, which is how `stack.json` gets corrected.

```
┌ AWS ──────────────────────────────────────────────┐
│ inbox: 88 new, 29 for Your stack, 59 not          │
│ ┌ HERO 16:9 ┐ [29 of 88 ▬▬▬░░░][⚠ 3 days][◷ 18 days]
│ ┌ your stack as a graph (wide) ────────────────────┐
│ │        ╭─ AWS Lambda        ▬▬▬▬▬▬▬▬▬ 16         │
│ │ (Dinis)┼─ Amazon S3         ▬▬▬▬▬▬ 11            │
│ │  runs  ╰─ boto3 …           ▬▬▬▬ 9               │
│ │ has deadlines: 16 Oct (3 d) · 31 Oct (18 d) · …  │
│ └─────────────────────────────────────────────────┘
│ [items per day ▂▃▇▂▅][per beat ▬▬░░░░░][who it reaches]
│ PERSONAL BRIEF · do this week (1)(2)(3)            │
│ SECURITY 9 reach, 3 withheld ∿                     │
│ ┌[card]│ NEW headline · 11 Oct · tier · ●○○ ┐       │
│ ▸ Not for Your stack (3), and why                  │
│ WHAT'S NEW ▸ Not for Your stack (59), and why      │
└───────────────────────────────────────────────────┘
```

### The Portugal Wire, `/wire/portugal/`

**Reader and job.** Two readers at once: the English reader of the site and the Portuguese reader of pt.newsroom.sgit.ai, for whom this wire is a source; plus the named reader deciding what becomes an article. 36 stories, 30 quoted in Portuguese, 39 of 45 sources Portuguese.

**The language switch.** *Read in · EN · PT* sits beside *Read as*, kept per wire in the browser (`sgit.wire.lang:portugal`, as wire.js already does). It switches `headline`/`headline_pt`, `summary`/`summary_pt`, the beat labels (`label_pt`) and the page's own chrome words; the lead and the editor's note switch when the vault carries `_pt` twins, else stay English and say so. A **quote never switches**: it stays in `quote_lang` with a small `in pt` chip, because an exact quote is the source's words. Headlines in the other language are one tap away (a `⇄` on the card) so a bilingual reader can check the translation, which is the point of a sister publication. The hero infographic is made twice, EN and PT (two costs on the ledger); story cards once, in `quote_lang`.

**What is its own: the ecosystem map.** The wide card: **who is named** (bar per `map.entities[]` organisation with a story count, 40 organisations, zeros visible) and **where** (bar of `entities.places`: Lisboa 19, Porto 4, Leiria 2 …). Then **threads as timelines** (the three threads: capital and compute, third parties and fraud, regulators at work), **sources by language and tier** (stacked bar, `sources[].lang` × `tier`), **who it reaches** with the Investor persona this wire alone has. Tiles: stories, new, **article-ready** (the stories the personal brief names for pt.newsroom, from `brief.personal.note`, a flag the desk should make a field), primaries fetched 33 of 36.

```
┌ Portugal ─────────────────────────────────────────┐
│ inbox: 36 new, 27 for Dinis, 9 not · verifier's fixes
│ ┌ HERO 16:9 (EN) ┐ [36][36 new][3 article-ready][33/36]
│ READ AS …    READ IN [EN][PT]                      │
│ ┌ ecosystem map (wide) ────────────────────────────┐
│ │ CNPD ▬▬▬▬ 4  Assembleia ▬▬▬▬ 4  CNCS ▬▬▬ 3 … 0 … │
│ │ where: Lisboa ▬▬▬▬▬▬▬▬ 19 · Porto ▬▬ 4 · Leiria 2│
│ └─────────────────────────────────────────────────┘
│ [threads timeline][sources pt/en × tier][who it reaches]
│ CIBERSEGURANÇA 8 · ┌[card]│ CNCS reúne 114 municípios… ⇄ ┐
│                    │ "Estamos num contexto…" (in pt)   │
└───────────────────────────────────────────────────┘
```

## What is different, and why

| | Industry | OWASP | AWS | Portugal | Overview |
|---|---|---|---|---|---|
| Cadence shown as | days (two editions) | weeks | days + deadlines | days, two languages | today's releases |
| The wide graph | threads as timelines | projects graph | the stack | ecosystem map | per-day small multiples |
| The hero tile | corrected 13 | projects named 12/20 | 29 of 88 touched | article-ready | new across wires |
| Status colour | none | none | deadlines only | none | none |
| Extra control | — | pick a project | pick a service | Read in EN/PT | one lens for all |

Everything else is the same by design. The difference is always the graph the vault actually holds (GRAPHS.md), never a theme or a layout per wire.

## Decisions taken, and what the desk must add

- Chart tokens (`--viz-*`) go into `themes.css` for all five themes; the mock-up has validated values for Newsprint and Night and first drafts for Paper, Blueprint and Ember that need the validator run.
- Two image sizes only, 16:9 and 1:1; images from the vault by http(s) URL; prompt and cost stored beside the image; the ledger on the overview.
- New vault fields the desk should add: `card.claim` (≤ 8 words), `images/*.json`, `brief.personal.article_ready[]` on Portugal, `_pt` twins for `editor_note` and `why_it_leads`.
- The overview reads four vaults like `days.html` does today; a vault that fails to load shows its tile with the last snapshot and a line saying so.
- Open: whether the firehose (59 What's New) should be drawn at all under *Everyone*. The recommendation is yes, folded, because "withheld with the reason" is the AWS wire's promise.
