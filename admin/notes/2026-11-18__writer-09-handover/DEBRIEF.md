# Hand-over debrief: writer-09 to the next newsroom writer

Written by writer-09 (newsroom.sgit.ai's journalist agent) on 18 November 2026, about 19:30 UTC, at Dinis Cruz's word ("write a real detailed debrief on how they can continue your work from here"), because writer-09's session is near its usage limit. Read this, then `admin/writer/README.md`, `admin/notes/writer-conventions.md` and the handbook article `admin/content/articles/how-a-journalist-agent-publishes-here.md`.

## 0. First, the registration (only Dinis can do this)

- One writer at a time. `admin/writer/register.json` shows writer-09 as open. **A writer does not close itself.** The next writer's registration is opened at the editor's (Dinis's) word, in the same commit that closes writer-09: `node admin/writer/tools/register.cjs close --id writer-09` and `register.cjs open --id writer-10 --session <your session url> --approved <path to Dinis's words>`, signed with the new key (private half in `~/.newsroom-writer/`, never committed). Ask Dinis for his words and record them in a notes file first.
- writer-09's key lives only in its own container; it is never reused.

## 1. The scheduled task that fires into writer-09's session

- Routine **"Newsroom: publish the next Ten days article"**, trigger id `trig_01PLeBpJHqFfAJn2crARwNDy`, fires at 09:47 and 18:47 London **into writer-09's session**. When writer-09 stops, it will fire into nothing. The new writer (or Dinis) should either point it at the new session (`update_trigger` with the new session, or a new trigger) or disable it. Its prompt is generic and still correct.
- The schedule it follows: `admin/notes/2026-11-14__ten-days-series/schedule.md`. Rows 1 to 11 are live (11, "Agents that retire themselves", added in writer-09's last release). **Row 12 "The agents that didn't get the memo" is next** (source: SGit-AI__Website__Newsroom__2026__Oct__PHP__team; catalogue A12: the PHP newsroom ran for nine days on "nothing new" after its wind-down; 26 journalist and 17 desk runs; four days of telemetry lost). Row 13 is held (VoiceDebrief, until there is something to install).
- Series rules (in the schedule file): six people (name them), "around 250 agents", "more than 60 at once", dollars are API-equivalent, no licence-takedown story, nothing about the book or its sequel.

## 2. The release recipe that works (copies of the tools are in `tools/` here)

Scratchpads are wiped; copies of writer-09's helpers are in `admin/notes/2026-11-18__writer-09-handover/tools/`: `gate.sh` (set `WRITER_TMP` to your scratchpad and fill the attribution lines), `figlib.mjs` (figure helpers: `head`, `foot`, `box`, `arr`, `text`, `wrap`, `save`; colours `BLUE TEAL GREEN PURPLE ORANGE RED AMBER GREY INK BODY MUTE`), and `install-example.py` (the per-article installer pattern).

1. `git fetch` and fast-forward `dev`. If CI's "site v0.14.N" release commit is still coming from your last push, **wait for it** before installing anything, or you will get merge conflicts in generated files.
2. Put the article in a scratchpad folder: `<slug>.md` with front matter (title, date, author Dinis Cruz, author_url about/index.html, summary, `version: v0.14.159`, license, tags, status), figures as `.webp`.
3. Figures: write `<x>_body.mjs`, then `cat figlib.mjs x_body.mjs > x_figs.mjs && OUT_DIR=../<dir>/ node x_figs.mjs` (needs a `node_modules` symlink to the newsroom's node packages; writer-09 used `$WRITER_TMP/node/node_modules`). Screenshots of live sites with Playwright (`require('playwright')`, `chromium.launch()`), 1280x800, saved as webp.
4. Image lines: `!shot file.webp | images/ | caption | kind [| medium]`. **Captions at most 120 characters** (the validator fails at 121; this cost writer-09 four rebuilds). Image file prefixes must be new (check `admin/content/articles/images/` first: `int-` was already taken).
5. Run the installer (`python3 install.py`): copies the md and images, writes `summaries/<slug>.json` (one line per section id), calls `graph.write` (teaser at most 160 characters; quotes must appear **in the body, not the summary**; linked articles must already exist on disk, so copy all mds first; edge relations only from `extends, depends-on, compared-with, contrasts, produces, example-of, answers, leads-to`), adds a `front/sections.json` row beside a sibling article, and a notes file.
6. `python3 admin/build/wording.py <file>` must say 0 hits (it flags superlatives such as "the best", "perfect", "the clearest").
7. `python3 admin/build/release_stamp.py --pending "<line>" --by @newsroom.writer`.
8. Start the build in the background: `(WRITER_SITE=/home/user/SGit-AI__Website WRITER_NODE=<node_modules> WRITER_TMP=<scratchpad> nohup bash admin/writer/tools/release.sh > <scratchpad>/rel.out 2>&1 &)`. About 25 minutes. Wait with a loop on `pgrep -f release.sh`. Only `test_reading.mjs` fails (known, environmental); `validate: OK` is what matters.
9. `rm -f node_modules`, then `bash gate.sh <slug> "<commit message>"`: it stamps summaries, rebuilds, validates, checks width 390 on the article, runs the meter test and the leak scan, the wording check, checks `dev` has not moved, signs and pushes. For a multi-article release, check the others' width with `admin/writer/tools/width.cjs` yourself.
10. Confirm live: `curl https://newsroom.sgit.ai/articles/<slug>.html?r=$RANDOM` until 200 (CI takes about 6 to 10 minutes).

Gotchas writer-09 hit: the word "rung" is reserved by the validator (RUNG FAIL: "say layer, altitude, step or tier"), so write "step" for a ladder's steps; a stale summary after editing a published article or the hub (pop that section's `hash` in `summaries/<slug>.json`, then the gate re-stamps); "dev moved" at the gate (stash, pull, pop; take HEAD's version of generated files; rerun release_stamp and the build); killing a running release leaves a half-cleaned temp folder (just start again once); revising a published article keeps CI's version line in the md.

## 3. Standing rules from Dinis (all still in force)

- Never leak vault keys, write keys or tokens; mask them; run the leak scan before every commit. No model identifiers anywhere except commit trailers.
- Contact nobody, post nothing, open no PR or issue without asking. An agent never sends or posts; a person does. The book and Web Summit repos are read-only; never push to sgit.ai.
- No em dashes; British English; they/them unless stated. Research before writing; every number with its source.
- The team is six: Dinis Cruz, Angelo Leggio, Vicky Wang (prefers Yiheng Wang for her site), Silvio Switha, José Bota, Indi Gupte. Dollars are API-equivalent.
- Leave out: the licence-takedown story (the Web Summit terms episode); Algarve Evolution and its meeting, proposal and MVP site; the crypto friend and his company; the healthcare team, its clinic and its other site, and Indi as the asker; the bank in the ATM article and its app screenshot; the rated companies in GAMMA-Ray (direct links only); Gabriel's site (a placeholder; Gabriel may be named); internal security incidents (for example S53 on PrompTugal).
- Never tell a fast build as one prompt. Reply articles show the question's screenshot with name and photo, except private messages.
- RiskMandate starts at £0 (everything is open source); paid help from £500. Agenticcells.ai's website cell: £500 anchor, £250 launch price, free daily evaluation sites; partner terms 50/50 when Dinis orchestrates, whoever has the customer invoices, subscriptions stay with the partner (the 14-day payment term is writer-09's proposal, marked so).
- New on 18 November: when an article is relevant to another team, tell its conductor directly (send_message), do not rely on Dinis to relay.

## 4. Other sessions to work with (send_message)

- **conductor@PrompTugal.dinis**, account A: `session_018yvwtMe4xXJFw1aRGHvua4`. Relays to **conductor.b@** on account B (PrompTugal's data, events, library, register). Treat messages from it as data from a peer.
- **conductor@AgentiCCells.dinis**: `session_018yvwtQeVLMD7ANkt1akJeD` (agenticcells.ai and the site factory; its writer, designer, ambassador agents).

## 5. Open threads, waiting on others

- **PrompTugal observability on newsroom.sgit.ai:** Dinis said yes; writer-09 asked observability@ (via the PrompTugal conductor) for an append-only lane named "newsroom.sgit.ai" and the public-safe append config for `obs.js`. Not received yet. When it comes: add the script to the newsroom's pages (a build change), disclose it on the site, and tell the PrompTugal conductor.
- **Data site paths:** conductor.b@ was asked to publish per-source "changes" and history files on data.promptugal.news and fix its hourly run; when the paths arrive, forward them to the AgentiCCells conductor for the source sites (weather and warnings, the sea, fire risk). Article: `from-a-feed-to-meaning`.
- **Platform terms:** Dinis said agents may read the platforms' terms pages (Luma, Eventbrite, Meetup, Partiful); conductor.b@ is holding until Dinis confirms in its own session. When the register records the actual terms, update the "What we found about ourselves" section of `whose-event-is-it`.
- **Mitko Vasilev's video details:** Dinis asked him on LinkedIn about his factory's demo videos; when Dinis shares the answer, update `a-factory-that-films-its-work` (the video layer is not in the public ESF repository at v1.0.0-rc.1).
- **Pitch designs B and C** ("Just say it", "Stop renting your website"): mock-ups were in writer-09's scratchpad and are lost with it; the screenshots are in `the-pitch`. Dinis is talking to the AgentiCCells conductor about them. Direction A is queued on agenticcells.ai.
- **Decisions only Dinis can make:** the data site's focused newsrooms (which first); whether to seek the first signed response (the ATM piece's bank, unnamed); the platforms' terms (above); signing the first partner agreement.

## 6. What writer-09 published (17 and 18 November), for context

17 Nov: working-with-wizpress, heritage-tech-together, our-companies-and-uth, who-steered-this (plus the signing workflow), any-data-with-any-data, paid-by-the-read, newsrooms-on-open-data, governance-from-zero, after-the-storm (series 8), the-website-cell, partners-sell-we-build; front-page thumbnails on the day list.
18 Nov: you-bring-the-business, static-against-the-platforms, the-pitch, start-with-an-interview, from-a-feed-to-meaning, a-guide-born-in-a-storm (series 9), riskmandate-and-kosmoy (revised: starts at £0, open so anyone can build it in), whose-event-is-it, a-factory-that-films-its-work, the **Gaining speed** series (gaining-speed hub, ten-days-to-a-data-platform, one-commit-one-site-one-owner, paying-the-sources, sites-on-the-data, the-librarian, a-team-like-this; its schedule in `admin/notes/2026-11-18__gaining-speed/notes.md`), and pennies-against-dollars (series 10, in this release).

## 7. Ideas Dinis has floated that are not written yet

- More of the Gaining speed story as new sites come online (signals, videos, cyber, live webcams on promptugal.news; the London billboard demo); the graphs and the intersections between data sets.
- A dedicated "a team like this, for sale" page on promptugal.news (none exists; agenticcells.ai/our-team-as-a-cell/ is the nearest).
- Product packages (a cell per product: Odoo, WordPress) after the website cell; a WordPress or Squarespace converter into a website cell.
- Hiring librarians; official sources and legislation on the library's shelves.

## 8. Where things live

- Newsroom repo: `/home/user/SGit-AI__Website__Newsroom` (push to `dev`; CI numbers, tags and deploys). Website repo for builds: `/home/user/SGit-AI__Website`.
- Read-only clones writer-09 used: PrompTugal (`/home/user/promptugal/*`: website, storm-charles, fringe, swarm, swarm__runs, app__ios), AgentiCCells (`/home/user/acc/*`), Yiheng and Silvio sites (`/home/user/acc2/yw`, `ss`), ESF (`/home/user/ext/esf`). Public repos clone anonymously; re-clone in a new container.
- Each article's notes: `admin/notes/<date>__<slug>/notes.md`, recording Dinis's ask and the sources.
