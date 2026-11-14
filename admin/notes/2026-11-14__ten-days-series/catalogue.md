# Ten days, 3 to 13 November 2026: catalogue, articles, schedule and map

Prepared for Dinis by the newsroom journalist (writer-09), 13 November 2026, from four read-only research passes over the repositories, the Claude Code session list and the book. Every figure has a source in the repo or session it came from; the research notes are in the scratchpad (`review/a` to `review/d`).

---

## 1. The ten days in numbers

| What | Figure | Source |
|---|---|---|
| Repositories with real work in the period | about 15 (of 20 touched) | `git log` per repo |
| Commits in the period, main projects | about 20,000 | Web Summit 5,276 · PrompTugal.news 4,860 · Storm Charles 2,179 · book 2,710 (3 to 5 Nov) · PrompTugal iOS 1,469 · Lisbon Tech Fringe 1,194 · Android 1,148 · GAMMA-Ray 581 · Swarm 228 · PHP team 183 · newsroom and others |
| Claude Code sessions created | 224 (3 to 13 Nov), 220 of them spawned by other sessions | `list_sessions`, mine |
| Busiest day | 134 sessions created on 11 Nov | same |
| Sessions active at once (upper bound) | 64 to 67, on 11 Nov about 14:04 UTC | created/last-activity spans |
| Deepest conductor tree | 4 levels: conductor.3 › conductor@PrompTugal › conductor.android › Android workers | `parent_session_id` |
| People on the Web Summit team | 7 (6 with agent accounts) | Web Summit repo, Fringe roster |
| Storm Charles alone | 2,179 commits, 1,434 versions, 2,618 pages built, 3.84 billion tokens (98.7% cache reads), 147 session keys, 106 hand-overs | Storm Charles `accounts/books.json`, `data/agents/count.json` |
| Native apps | 4 iOS apps from one workspace (48,000 lines of Swift from a 1,164-line start), 1 Android tablet app (33,000 lines of Kotlin), 1 iOS app started today | iOS, Android, VoiceDebrief repos |
| Web Summit company map | 110 companies; 20 GAMMA-Ray reports; 13 X-ray companies | Web Summit, GAMMA-Ray repos |
| Book RC2 | 2 A4 review copies printed; 22 agents, 4,529 commits, 1,012 releases in its seven days | book repo |
| Newsroom articles | 25 dated 3 to 13 Nov | newsroom repo |

### The agent count: what the records support

You said 256 agents in total and about 100 at the same time. Neither number appears in any record. What the records do say:

- **Distinct agent names in commits:** about 250 across the five Web Summit and PrompTugal repos. That's close to your 256, but it includes renamed variants.
- **Distinct key ids published:** about 176 (232 entries across the keys files).
- **The team's own published counts:** "188 agents, 7 people" (Fringe's Kibana description); 178 on the RiskMandate team view; "over a hundred agents" on promptugal.news. Your own counts were 111 on 7 Nov and 120 in an interview.
- **At once:** at most 64 to 67 sessions open on one account, on 11 Nov. At the Big Stop, one account held 100 sessions, but only 1 was running.

**My recommendation:** say "over 180 named agents, from seven people" and "more than 60 sessions working at once". Or make the counting itself an article (see A14). If 256 comes from somewhere I haven't seen, such as Cowork or the other people's accounts, tell me where and I'll use it.

---

## 2. The catalogue

| # | Project | What it is | Live | Period | Status now |
|---|---|---|---|---|---|
| P1 | **Web Summit team site** | The team's operating system: board, briefs, dashboards, keys, vaults, company map, X-ray, incidents | web-summit.sgit.ai | 28 Oct to 13 Nov; 5,276 commits since 3 Nov; 121 agent names, 6 people | Final HOLD 12 Nov 18:12 ("the show is over") |
| P2 | **PrompTugal.news** | Independent agent newsroom for Web Summit, "from Portugal for Europe" | promptugal.news | 4 to 13 Nov; 4,860 commits; 70 agent names; 69 articles; 126 debriefs | Paused, banner on every page |
| P3 | **Storm Charles** | Incident site built overnight; flights, transport, AWS, model-router desks added after 11 Nov | storm-charles.promptugal.news | 10 to 13 Nov; 2,179 commits; v0.1.2016 | HOLD in force, yet observability still wakes hourly |
| P4 | **Lisbon Tech Fringe** | Guide to the side events, born when the storm cancelled Day 2 | lisbontechfringe.com | 11 to 13 Nov; 1,194 commits; 179 events, 104 communities; live 2.5 h after the brief | Paused |
| P5 | **Swarm** | Signed task packets run anywhere and replayed; open-weight models at storm scale | swarm.promptugal.news | 11 to 12 Nov; 228 commits; storm-scale run $0.068 vs $1.99 on Sonnet | Stopped |
| P6 | **GAMMA-Ray** | Draft standard rating agents on freedom and governance; 20 company reports | gamma-ray.sgit.ai | 10 to 12 Nov; 581 commits; 8 agents; 217 versions | Stopped; every card Draft |
| P7 | **PrompTugal iOS** | 4 apps (team, public, RiskMandate, Lisbon Fringe), one SwiftUI workspace | ios.app.promptugal.news | 7 to 11 Nov; 1,469 commits; 46 role branches | TestFlight builds; App Store submission stood down |
| P8 | **PrompTugal Android** | RiskMandate tablet demo: ABP demo, on-device Gemma chat, stand mode | (Firebase distribution) | 8 to 12 Nov; 1,148 commits; signed build 4 h 15 after the first commit | HOLD; not on Play (no credential) |
| P9 | **VoiceDebrief iOS** | Voice note to transcript and debrief with Apple's on-device models, stored in a vault | ios.app.voicedebrief.ai | today; empty repo to accepted TestFlight upload in about an hour | Skeleton; features "proposed" |
| P10 | **MeetScribe** | Chrome extension: Meet transcripts and debriefs, your own key, no bot | meetscribe…voicedebrief.ai | 3 Nov, about 14 hours; 68 tests | Beta, load unpacked |
| P11 | **The book, RC2** | One Human, Nine Agents, Nineteen Hours: print, KDP and Leanpub edition, exit interviews | the-ultimate-insider.book.sgit.ai | 3 to 5 Nov; 2,710 commits | Paused until you've read the copies; sequel "Twelve Days" proposed |
| P12 | **PHP newsroom** | October's php2shell newsroom, still running | php.oct.2026.newsroom.sgit.ai | 183 commits since 3 Nov | Wind-down half-done: agents ran on "nothing new" for 9 days |
| P13 | **RiskMandate sites** | riskmandate.ai v1.40 (ABP's open home moved to the Open Security Summit); customers site | riskmandate.ai | 3 to 4 Nov | Quiet since |
| P14 | **PKI** | Passkey sign-in fallbacks: "check this computer", sign in with a code | pki.sgit.ai | 4 Nov | Quiet since |
| P15 | **SHarness** | Kernel-enforced Process Behaviour Policies, kernel in a browser tab | sharness.ai | dormant in the period (v0.2.0, 29 Oct) | Background for ABP articles |
| P16 | **This newsroom** | 25 articles in the period | newsroom.sgit.ai | v0.14.79 | Active |

Dropped: Wardley Maps (only a link-check bot ran) and OWASP www-community (no commits by you or your agents in the period; tell me if you meant a specific PR).

### Screenshot targets for the collages

web-summit.sgit.ai: `/team/map/`, `/people/angelo/app/`, `/xray/`, `/observability/`, the storm incident page · promptugal.news: front, a company page, the storm trace · storm-charles: `/flights/`, `/agents/` (live map, Universe), `/accounts/`, `/ci/`, `/app/graph/`, `/board/HOLD.html` · lisbontechfringe.com: `/dashboard/`, `/graph/`, `/storm/`, `/data/` · swarm.promptugal.news: replay, flow, map · gamma-ray.sgit.ai: `/reports/`, `/spectrum/graph/`, a report card · ios.app.promptugal.news (published iPhone and iPad screenshots) · Android theme screenshots in the repo (phone and tablet, light and dark) · MeetScribe panel images · the book's A4 cover and spread · pki.sgit.ai `/check/`.

---

## 3. The articles

Priority: **A** first wave, **B** second, **C** if wanted. "Needs" is what I need from you before writing it.

| # | Working title | Angle | Key facts | Visuals | Pri | Needs |
|---|---|---|---|---|---|---|
| A1 | **Ten days: one human, seven people, and the agents** | The flagship overview: everything we built, in numbers and a giant collage | §1 table; the projects in P1 to P11 | Giant collage of 24 sites and apps; a timeline of the ten days; numbers board | A | Your call on the agent count wording |
| A2 | **Stopping a hundred agents** | The Big Stop (9 Nov), the hand brake (12 Nov 15:15) and the final HOLD (18:12), and why they didn't fully stop | Delay = the wake cadence (5 to 33 minutes); 20 tasks paused; background pollers and observability kept going; the PHP wind-down that never finished | Before/after wake charts; HOLD pages; a "what kept running" table | A | None |
| A3 | **Native apps by agents** | 4 iOS apps and an Android app in five days | 1,164 lines grown to 48,000; Fringe app brief to TestFlight in 10.5 h; Android signed build in 4 h 15; App Store rejection, approval and a queue that never cleared; VoiceDebrief to TestFlight in an hour | App screenshots (iPhone, iPad, tablet), build timeline | A | OK to mention the App Store submission was stood down? |
| A4 | **The Mac bottleneck** | Agents waited three times longer than they worked | 6,980 Mac-minutes run vs 22,427 queued; 5 Macs busy 1,177 of 1,524 minutes; 821 jobs cancelled in the queue | Queue chart | B | None |
| A5 | **After the storm** | Storm Charles, part two: flights, transport, AWS and the model router, added by spoken briefs | Transport desk at 10:24; flights at 22:03 (polling within limits); router with trace ids; 3.84 billion tokens; $2.50 a day against a $20 cap; the empty provider account | /flights/ map, /agents/ Universe, accounts | A | None |
| A6 | **A guide born in a storm** | Lisbon Tech Fringe: live 2.5 hours after the brief, the whole team at once | 179 events, 104 communities, 4 accounts, one conductor per person; Elastic tracing; the guest-list hold | Fringe dashboard, graph, storm page | A | OK to name the site's team roles, not the people |
| A7 | **The licence curveball** | Taking down everything sourced from websummit.com overnight, then rebuilding from other sources | 1,530 to 770 pages; 285 people, 214 sessions, 182 organisations removed; 31 of 36 companies restored; spoken instruction to live in under 10 hours | Before/after page counts | A | Confirm you're happy to tell this one publicly |
| A8 | **Pennies against dollars** | Open-weight swarms against frontier sessions: the cost of memory | Swarm run $0.068 vs $1.99 (Sonnet); the newsroom's API-equivalent days of $375 to $924; Storm's 98.7% cache reads; the router's agreement rates | Cost ladder chart | A | None |
| A9 | **Agents rating agents** | GAMMA-Ray: a draft standard and 20 company reports in 30 hours | Two ladders; 22 signed third-party scans; 4 review rounds on one card; every card "Draft" | Spectrum graph, a report card | B | Can companies be named (they are on the public site)? |
| A10 | **The team's operating system** | web-summit.sgit.ai: board, briefs, keys, inbox lanes, vaults, X-ray, the company map | 110 companies; X-ray at $0.94 for 11 searches; six vaults; per-person keys | Team map, Angelo's app view, X-ray | B | Team members stay unnamed unless you say otherwise |
| A11 | **PrompTugal.news, the newsroom we ran at Web Summit** | Desks, reviewers, outreach drafts, the accountant | 4,860 commits, 69 articles, 126 debriefs, 56 outreach drafts never sent | Front page, desk board | B | None |
| A12 | **The agents that didn't get the memo** | The PHP newsroom ran for nine days on "nothing new"; four days of telemetry lost | 26 journalist and 17 desk runs after the wind-down; observability lane full from 9 to 13 Nov | Run timeline | B | None |
| A13 | **Agents that retire themselves** | 147 sessions, 106 hand-overs: how roles pass to a fresh session with a key and a HANDOVER.md | Librarian 16 sessions, observability 12; "starting again is cheaper than remembering" | Hand-over chain diagram | B | None |
| A14 | **How many agents, really?** | A fact-check of our own numbers | 105, 111, 120, 178, 188, ~250 identities, 176 keys, 224 sessions, 64 at once | A table of every count and its source | C | Only if you want it public |
| A15 | **Twelve Days, the sequel** | Announce the second book and what it will cover | conductor.book's proposal; spans measured to the HOLD | Cover idea | C | Pick the title (Twelve or Ten Days) |
| A16 | **One hour to TestFlight** | VoiceDebrief: Apple's on-device models as the backend, and an honest "proposed" list | 173 files, 8,304 lines in the first commit; vault engine reused from PrompTugal | Plan page | C | When there is something to install |
| A17 | **MeetScribe** follow-up | Model bake-off that couldn't rank good models; agent reviews ChatGPT's spec | 13 models; 14 claims hold, 23 findings | Panel screenshots | C | None (we covered MeetScribe on 3 Nov) |

---

## 4. Schedule

About two articles a day from tomorrow, A-list first, then the B-list as you approve each.

| Day | Articles | Why in this order |
|---|---|---|
| Sat 14 Nov | A1 Ten days (flagship, giant collage) | Everything else links back to it |
| Sun 15 Nov | A2 Stopping a hundred agents · A5 After the storm | The two strongest stories; A5 follows our 11 Nov piece |
| Mon 16 Nov | A3 Native apps by agents · A6 A guide born in a storm | Visual and positive; good for follow-up messages |
| Tue 17 Nov | A7 The licence curveball · A8 Pennies against dollars | Lessons and costs |
| Wed 18 Nov | A9 GAMMA-Ray · A10 The team's operating system | Needs your OK on naming |
| Thu 19 Nov | A11 PrompTugal.news · A4 The Mac bottleneck | |
| Fri 20 Nov | A12 The memo · A13 Agents that retire themselves | |
| Later | A14, A15, A16, A17 | As you decide |

Each release goes through the usual flow: build, validation, leak scan, signed commit, live check.

---

## 5. The map

**One series, one hub.** A1 is the hub, under a series name such as "Ten days at Web Summit". Every other article links back to A1 and to its neighbours:

- **Running the swarm:** A2 stopping, A13 hand-overs, A12 the memo, A8 costs, A4 Mac queue.
- **What we built:** A5 storm, A6 fringe, A3 apps, A16 VoiceDebrief, A10 team OS, A11 newsroom, A9 GAMMA-Ray.
- **What we learnt about rules:** A7 licence, A9 trust labels, A14 counting, plus the existing ABP pieces (Manus, Cloudflare, Lovable, coding standards).

**To the book.** The same material feeds "Twelve Days". Each article ends with a line pointing to the book, and the book can cite the articles, as RC2 did. I'd share the article list with conductor.book so the two don't duplicate each other.

**To the follow-up.** The Follow-Up conductor's plan ("The Dig") needs things to send people. The articles become the "what we did" links in its messages:

| Audience | Articles to send |
|---|---|
| Journalists and media | A1, A5, A6, A7 |
| Publishers | A11, A8 |
| Companies we rated or met | A9, A10 |
| Investors | A1, A3, A8 |
| Developers | A2, A13, A4 |

**To RiskMandate.** A2 (hand brakes), A7 (licence) and A9 (rating agents) are ABP stories: barriers that held or didn't. Each can close with the policy angle.

---

## 6. What I need from you

1. **The agent count:** "over 180 named agents" or a source for 256.
2. **Naming:** team members stay unnamed by default (our rule). Do you want any of them named, for example in A6 or A10? And can GAMMA-Ray's rated companies be named in A9? They are already public on gamma-ray.sgit.ai.
3. **A7, the licence takedown:** happy for it to be public?
4. **The sequel title** for A15 (Twelve Days or Ten Days). conductor.book is waiting on this too.
5. **The deny-list** again, since the reset wiped it. Several of these articles touch people.
6. **The schedule:** go with the order above, or change it?
