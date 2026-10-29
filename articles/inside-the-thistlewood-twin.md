# Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes, sgit.ai

> A tour of the vault behind ten questions, one graph. Thistlewood Retail is invented: four board risks, sixteen risks beneath them, nine accepted until a date, nine business processes on sixteen systems and twelve suppliers, four sales channels, fifteen controls, 38 incidents and 100 humans and agents. A deterministic engine answers each of Phil Venables' ten questions on that graph. An extra £250k goes to warehouse backups, hardware keys for staff and a second payment provider, and takes about a million pounds a year off the expected loss; the £250k cut is long log retention and the awareness programme, for about £30k a year of extra risk that someone has to accept. Eight accepted risks need revisiting after three events. Cheaper passkeys and bundled hardware keys could cover almost everyone at the same spend. Ransomware in the warehouse is the scenario the minimum viable processes cannot withstand. Identity admins and deploy agents have the largest blast radius, and 29 of 40 agents can reach beyond their mandate. Every answer shows the part of the graph it came from, and proposes decisions, 29 in all, each held by one person with a chain to the board. The back-test shows where the model is wrong.

*Source: <https://newsroom.sgit.ai/articles/inside-the-thistlewood-twin.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes

# Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-19 · [article v1.1.0, 2 versions](versions/inside-the-thistlewood-twin.md) · [newsroom v0.12.137](https://newsroom.sgit.ai/admin/versions.html) · cisographsrisk-acceptancevaultstwinarticle

***Abstract:** A tour of the vault behind ten questions, one graph. Thistlewood Retail is invented: four board risks, sixteen risks beneath them, nine accepted until a date, nine business processes on sixteen systems and twelve suppliers, four sales channels, fifteen controls, 38 incidents and 100 humans and agents. A deterministic engine answers each of Phil Venables' ten questions on that graph. An extra £250k goes to warehouse backups, hardware keys for staff and a second payment provider, and takes about a million pounds a year off the expected loss; the £250k cut is long log retention and the awareness programme, for about £30k a year of extra risk that someone has to accept. Eight accepted risks need revisiting after three events. Cheaper passkeys and bundled hardware keys could cover almost everyone at the same spend. Ransomware in the warehouse is the scenario the minimum viable processes cannot withstand. Identity admins and deploy agents have the largest blast radius, and 29 of 40 agents can reach beyond their mandate. Every answer shows the part of the graph it came from, and proposes decisions, 29 in all, each held by one person with a chain to the board. The back-test shows where the model is wrong.*

The Thistlewood decision twin opened read-only from its vault in the official vault UI: the case and the ten questions.

Thistlewood: ten questions, one graph

Phil Venables' ten questions for a CISO's management tool, answered on one graph: the reply, a tour of the vault, and the vault itself to use.

[1 · The replyTen questions, one graphWhy his questions are graph questions, and how our risk acceptance work and vaults answer them.](ten-questions-one-graph.md)[you are here2 · The tourInside the Thistlewood twinThe ten answers one by one: the plot on the graph, the evidence, and the decisions they propose.](inside-the-thistlewood-twin.md)

3 · The twinThe Thistlewood decision twinPick a question and watch the graph fade to the answer; read every decision up to the board.[Use it](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_32e4f88c6dbc68ae6e2566223008671cc6525ad78ef89482ab4f8b44cb28a07f%3A6v7kyxf4)[His article ↗](https://www.philvenables.com/post/a-cisos-ideal-management-tool)

## In short

- **An invented retailer, as one graph.** Board, risks, holders, processes, systems, suppliers, channels, controls, incidents, 100 identities.
- **A deterministic engine.** Each question is a query; every answer replays exactly.
- **Every answer shows its plot.** Pick a question and the rest of the graph fades.
- **Every answer proposes decisions.** 29 in all, each with one holder and the chain to the board.
- **The back-test shows where it is wrong.** And the model is simple on purpose.

## The company

Thistlewood Retail sells through a web store, a mobile app, marketplace listings and the phone, £920k a day across the four at peak. Its busiest five days run from Black Friday to Cyber Monday. Its board holds four risks: loss of customer trust after a breach, lost revenue at peak, a regulatory penalty, and fraud. Under them sit four business risks and twelve operational and technical ones, each with a holder; nine are accepted until a date, one is funded, one fixed, and the rest open. Fifteen controls reduce them, each with a cost a year and a coverage, such as hardware keys on 40 of 140 staff with production access.

There are 100 identities: 60 humans, from platform engineers to service agents, and 40 agents, from deploy agents to a refund agent, each with the systems it can reach directly and the identities it can act as. One of each kind of agent was set up under a behaviour policy and holds only its mandate; the rest hold more. Everything is invented, and nothing calls a model.

The whole company as one graph, before any question: risks, controls, processes, systems, suppliers, humans and agents.

## 1 and 2: where £250k goes, and where it can come from

The engine prices every option and picks the one that removes the most expected loss per pound, until the budget runs out. An extra £250k goes to immutable warehouse backups with a tested restore (£70k, about £338k a year of loss avoided), hardware keys for 100 more staff (£100k, about £378k) and a second payment provider for every channel (£80k, about £298k). The expected annual loss falls from about £3.5 million to about £2.5 million.

The cut runs the other way: remove what adds the least risk per pound saved. Log retention beyond 400 days (£140k, about £4.5k a year of extra risk) and the awareness programme (£180k, about £26k) together save £320k. Both decisions are acceptances, and the ledger gives each one to its holder for twelve months, then revisit.

## 3: the five most exposed processes

Exposure is the security risk carried by a process plus the reliability risk of the suppliers under it. Pick, pack and ship comes first, at about £1.6 million a year, then taking an order and payment, releasing software, customer sign-in and marketing email. Each gets its three things to do now, with cost and loss avoided: for pick, pack and ship, warehouse backups, a second courier, and a fallback for the warehouse supplier, still to price.

Question 3: the five most exposed processes, the three things to do now, then the evidence and the decisions proposed.

## 4: what keeps recurring, and why

The 38 incidents of the last year come from eight recurring causes. The top three are credential stuffing on customer login (9 incidents), bot surges at checkout (7) and expired TLS certificates (6). Each cause is followed five levels down, and the last level is rarely technical: "The acceptance assumed the old price", "The cost case was never redone", "The risk was accepted in 2024 and never revisited". That last level is where the fix belongs, and it has a holder.

Question 4: each recurring cause with its count and cost, followed five levels down to the decision behind it.

## 5 and 6: acceptances whose assumptions changed

Three things happened this month in the twin: a competitor disclosed credential stuffing, the regulator confirmed that customer data used for analytics must be masked, and the passkey provider cut its price by two thirds while hardware keys came bundled with staff laptops. Eight accepted risks are touched, from credential stuffing to the refund agent that can pay more than was paid; each goes back to its holder to accept again, fund or fix within fourteen days.

The cheaper controls are question 6. At the same spend, hardware keys can go from 40 to 133 of 140 staff, and passkeys from one channel to all three, taking about £350k and £320k a year off the expected loss respectively.

## 7, 8 and 10: what fails, and what it costs

The minimum viable processes are taking an order and payment, customer sign-in, and pick, pack and ship. Of eight severe but plausible scenarios, the worst they cannot withstand is ransomware in the warehouse system, run by one supplier with no fallback: about £2.3 million of sales at peak. A day without the cloud region stops all three processes, for about £570k.

The suppliers whose five-day outage would hurt customers most are the cloud host and the warehouse operator, about £2.8 million each, then the payment provider, softened by its fallback. Over the busiest five days, losing the web store would cost about £1.26 million, the app £853k, the marketplace £675k and phone orders £60k, and every channel has the cloud host and the warehouse operator as single points of failure.

## 9: 100 humans and 100 agents

Phil asks for 100 of each; the twin has 60 humans and 40 agents. Blast radius weighs every system an identity can reach, directly, through the identities it can act as, through the secrets store and through staff sign-on: customer records times sensitivity, plus the sales its processes carry. The three identity admins top the humans, because staff sign-on reaches everything. The deploy agents top the agents: each reaches seven systems, six of them beyond what its behaviour policy says it needs. Across the company, 29 of the 40 agents reach beyond their mandate.

Question 9: the humans and agents with the largest blast radius, and the systems and identities each can reach.

## The decisions, up to the board

The ten answers propose 29 decisions. The ledger lists them by holder, each with its door, fund, fix, accept or revisit, and its interval, and shows how many pass through each level on the way up: all 29 reach the chief executive and the board, eight pass through the chief operating officer, eight through the chief technology officer, and seven through the CISO. Nobody accepts on anybody else's behalf; their boss sees it arrive. In the vault, each is a file in `decisions/`.

The ledger: every proposed decision by the person who holds it, with the chain to the board and the roles on the way.

## Evidence, and where the model is wrong

Every answer lists the sources it rests on, and in the twin they are measured ones: the access review, supplier status history, incident tickets, billing and contracts, sales logs, and the configuration of every control. A questionnaire is listed too, because a real company has one, with the rule that it fills gaps, labelled, and never replaces a measurement.

The back-test compares what the model predicts for a year with the last twelve months of incidents. Two causes are close. Supplier bank fraud cost about twice what the model predicts, and four others cost far less, the leaked pipeline secret and the courier misses most of all. A near miss is not a loss, and the model should know the difference before anyone relies on those answers.

Evidence and back-test: the measured sources behind the answers, and the model's prediction against past incidents.

## How it is built

The vault holds the app, `index.html`, with the data and the engine inlined; `content.json`, the graph; `engine.js`, the engine, where `ThistlewoodTwin.make(content).ask(n)` answers question n; `answers/` and `decisions/`, written by the engine; and `tools/`, the scripts that build it all. Change the graph and rebuild, and every answer and decision follows. [The vault's page](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html) has the read key, a button to open it, and the app to use in place.

## What this does not claim

- **Everything is synthetic.** The company, people, agents, suppliers, incidents and numbers are invented.
- **The model is deliberately simple.** Controls reduce a base exposure in proportion to their coverage.
- **Some dependencies are missing.** The courier's failure is a risk in the register, not a dependency of the systems, so the scenario where it cannot collect shows no lost sales; a fuller model would add it.
- **Sixty and forty, not a hundred and a hundred.** The question asks for 100 of each; the twin is smaller.
- **No model is called.** The answers are computed, so they replay exactly.

## Where this comes from

Phil Venables, [A CISO's Ideal Management Tool](https://www.philvenables.com/post/a-cisos-ideal-management-tool), 19 October 2026, for the ten questions. The twin, its engine and every number in this article are from [the Thistlewood decision twin](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html), built for this article. Related: [ten questions, one graph](ten-questions-one-graph.md), [every risk is already accepted](every-risk-is-already-accepted.md), [the graph companies](the-graph-companies.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Graphs & knowledgeVaults & method[This article as a graph →](graphs.md#inside-the-thistlewood-twin)

### Builds on

- [Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open](ten-questions-one-graph.md) Phil Venables' ten questions for a CISO's tool are graph questions. Risk acceptance is half the answer; a twin in a vault answers all ten.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [The graph companies: many of the most valuable companies in the world are graphs, of links, people, products, payments and ontologies, and the graphs never scaled for everyone else because they were built to lock in](the-graph-companies.md) Four of the ten most valuable companies are graph companies. Graphs never scaled for everyone else because they were built to lock in. Now they can.

### Continued by

- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open](ten-questions-one-graph.md) Phil Venables' ten questions for a CISO's tool are graph questions. Risk acceptance is half the answer; a twin in a vault answers all ten.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 216 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=216)

**Posting this article on LinkedIn?** The cover is [inside-the-thistlewood-twin.jpg](banners/inside-the-thistlewood-twin.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/inside-the-thistlewood-twin.html)*
