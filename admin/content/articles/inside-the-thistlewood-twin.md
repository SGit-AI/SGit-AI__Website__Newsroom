---
title: Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: A tour of the vault behind ten questions, one graph. Thistlewood Retail is invented: four board risks, sixteen risks beneath them, nine accepted until a date, nine business processes on sixteen systems and twelve suppliers, four sales channels, fifteen controls, 38 incidents and 100 humans and agents. A deterministic engine answers each of Phil Venables' ten questions on that graph. An extra £250k goes to warehouse backups, hardware keys for staff and a second payment provider, and takes about a million pounds a year off the expected loss; the £250k cut is long log retention and the awareness programme, for about £30k a year of extra risk that someone has to accept. Eight accepted risks need revisiting after three events. Cheaper passkeys and bundled hardware keys could cover almost everyone at the same spend. Ransomware in the warehouse is the scenario the minimum viable processes cannot withstand. Identity admins and deploy agents have the largest blast radius, and 29 of 40 agents can reach beyond their mandate. Every answer shows the part of the graph it came from, and proposes decisions, 29 in all, each held by one person with a chain to the board. The back-test shows where the model is wrong.
version: v0.12.137
license: https://creativecommons.org/licenses/by/4.0/
tags: ciso, graphs, risk-acceptance, vaults, twin, article
status: published
---

!shot tt-live.webp | images/ | The Thistlewood decision twin, opened from its vault in the official vault UI, read-only, with the published key: the case, with the expected annual loss computed from the graph, 100 humans and agents, nine of sixteen risks accepted, sales of £920k a day at peak, and the ten questions. | screenshot

!trail thistlewood

## In short {#in-short}

- **An invented retailer, as one graph.** Board, risks, holders, processes, systems, suppliers, channels, controls, incidents, 100 identities.
- **A deterministic engine.** Each question is a query; every answer replays exactly.
- **Every answer shows its plot.** Pick a question and the rest of the graph fades.
- **Every answer proposes decisions.** 29 in all, each with one holder and the chain to the board.
- **The back-test shows where it is wrong.** And the model is simple on purpose.

## The company {#company}

Thistlewood Retail sells through a web store, a mobile app, marketplace listings and the phone, £920k a day across the four at peak. Its busiest five days run from Black Friday to Cyber Monday. Its board holds four risks: loss of customer trust after a breach, lost revenue at peak, a regulatory penalty, and fraud. Under them sit four business risks and twelve operational and technical ones, each with a holder; nine are accepted until a date, one is funded, one fixed, and the rest open. Fifteen controls reduce them, each with a cost a year and a coverage, such as hardware keys on 40 of 140 staff with production access.

There are 100 identities: 60 humans, from platform engineers to service agents, and 40 agents, from deploy agents to a refund agent, each with the systems it can reach directly and the identities it can act as. One of each kind of agent was set up under a behaviour policy and holds only its mandate; the rest hold more. Everything is invented, and nothing calls a model.

!shot tt-graph-all.webp | images/ | The whole company as one graph, before any question: the board, business risks, operational and technical risks, recurring causes, controls, processes, systems, suppliers and channels, and the five humans and five agents with the largest reach. Edges run from cause to effect. | screenshot

## 1 and 2: where £250k goes, and where it can come from {#budget}

The engine prices every option and picks the one that removes the most expected loss per pound, until the budget runs out. An extra £250k goes to immutable warehouse backups with a tested restore (£70k, about £338k a year of loss avoided), hardware keys for 100 more staff (£100k, about £378k) and a second payment provider for every channel (£80k, about £298k). The expected annual loss falls from about £3.5 million to about £2.5 million.

The cut runs the other way: remove what adds the least risk per pound saved. Log retention beyond 400 days (£140k, about £4.5k a year of extra risk) and the awareness programme (£180k, about £26k) together save £320k. Both decisions are acceptances, and the ledger gives each one to its holder for twelve months, then revisit.

## 3: the five most exposed processes {#processes}

Exposure is the security risk carried by a process plus the reliability risk of the suppliers under it. Pick, pack and ship comes first, at about £1.6 million a year, then taking an order and payment, releasing software, customer sign-in and marketing email. Each gets its three things to do now, with cost and loss avoided: for pick, pack and ship, warehouse backups, a second courier, and a fallback for the warehouse supplier, still to price.

!shot tt-q3.webp | images/ | Question 3: the five most exposed processes, the security and reliability exposure of each, and the three things to do now, each with its holder, cost and loss avoided; then the evidence, and the decisions it proposes, each with the chain to the board. | screenshot

## 4: what keeps recurring, and why {#recurring}

The 38 incidents of the last year come from eight recurring causes. The top three are credential stuffing on customer login (9 incidents), bot surges at checkout (7) and expired TLS certificates (6). Each cause is followed five levels down, and the last level is rarely technical: "The acceptance assumed the old price", "The cost case was never redone", "The risk was accepted in 2024 and never revisited". That last level is where the fix belongs, and it has a holder.

!shot tt-q4.webp | images/ | Question 4: each recurring cause with its count and cost, followed five levels down, from what happened to the decision that let it keep happening. | screenshot

## 5 and 6: acceptances whose assumptions changed {#acceptances}

Three things happened this month in the twin: a competitor disclosed credential stuffing, the regulator confirmed that customer data used for analytics must be masked, and the passkey provider cut its price by two thirds while hardware keys came bundled with staff laptops. Eight accepted risks are touched, from credential stuffing to the refund agent that can pay more than was paid; each goes back to its holder to accept again, fund or fix within fourteen days.

The cheaper controls are question 6. At the same spend, hardware keys can go from 40 to 133 of 140 staff, and passkeys from one channel to all three, taking about £350k and £320k a year off the expected loss respectively.

## 7, 8 and 10: what fails, and what it costs {#resilience}

The minimum viable processes are taking an order and payment, customer sign-in, and pick, pack and ship. Of eight severe but plausible scenarios, the worst they cannot withstand is ransomware in the warehouse system, run by one supplier with no fallback: about £2.3 million of sales at peak. A day without the cloud region stops all three processes, for about £570k.

The suppliers whose five-day outage would hurt customers most are the cloud host and the warehouse operator, about £2.8 million each, then the payment provider, softened by its fallback. Over the busiest five days, losing the web store would cost about £1.26 million, the app £853k, the marketplace £675k and phone orders £60k, and every channel has the cloud host and the warehouse operator as single points of failure.

## 9: 100 humans and 100 agents {#identities}

Phil asks for 100 of each; the twin has 60 humans and 40 agents. Blast radius weighs every system an identity can reach, directly, through the identities it can act as, through the secrets store and through staff sign-on: customer records times sensitivity, plus the sales its processes carry. The three identity admins top the humans, because staff sign-on reaches everything. The deploy agents top the agents: each reaches seven systems, six of them beyond what its behaviour policy says it needs. Across the company, 29 of the 40 agents reach beyond their mandate.

!shot tt-q9.webp | images/ | Question 9: the humans and the agents with the largest blast radius, how many systems they reach directly and in all, how many other identities they can act as, and, for agents, how many systems lie beyond their behaviour policy's mandate. | screenshot

## The decisions, up to the board {#decisions}

The ten answers propose 29 decisions. The ledger lists them by holder, each with its door, fund, fix, accept or revisit, and its interval, and shows how many pass through each level on the way up: all 29 reach the chief executive and the board, eight pass through the chief operating officer, eight through the chief technology officer, and seven through the CISO. Nobody accepts on anybody else's behalf; their boss sees it arrive. In the vault, each is a file in `decisions/`.

!shot tt-decisions.webp | images/ | The ledger: every proposed decision by the person who holds it, with the door, the interval and the chain to the board, and on the right how many decisions pass through each role on the way up. | screenshot

## Evidence, and where the model is wrong {#backtest}

Every answer lists the sources it rests on, and in the twin they are measured ones: the access review, supplier status history, incident tickets, billing and contracts, sales logs, and the configuration of every control. A questionnaire is listed too, because a real company has one, with the rule that it fills gaps, labelled, and never replaces a measurement.

The back-test compares what the model predicts for a year with the last twelve months of incidents. Two causes are close. Supplier bank fraud cost about twice what the model predicts, and four others cost far less, the leaked pipeline secret and the courier misses most of all. A near miss is not a loss, and the model should know the difference before anyone relies on those answers.

!shot tt-evidence.webp | images/ | Evidence and back-test: the measured sources the answers rest on, and the model's prediction for each recurring cause against the last twelve months of incidents, with the ratio. | screenshot

## How it is built {#built}

The vault holds the app, `index.html`, with the data and the engine inlined; `content.json`, the graph; `engine.js`, the engine, where `ThistlewoodTwin.make(content).ask(n)` answers question n; `answers/` and `decisions/`, written by the engine; and `tools/`, the scripts that build it all. Change the graph and rebuild, and every answer and decision follows. [The vault's page](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html) has the read key, a button to open it, and the app to use in place.

## What this does not claim {#limits}

- **Everything is synthetic.** The company, people, agents, suppliers, incidents and numbers are invented.
- **The model is deliberately simple.** Controls reduce a base exposure in proportion to their coverage.
- **Some dependencies are missing.** The courier's failure is a risk in the register, not a dependency of the systems, so the scenario where it cannot collect shows no lost sales; a fuller model would add it.
- **Sixty and forty, not a hundred and a hundred.** The question asks for 100 of each; the twin is smaller.
- **No model is called.** The answers are computed, so they replay exactly.

## Where this comes from {#sources}

Phil Venables, [A CISO's Ideal Management Tool](https://www.philvenables.com/post/a-cisos-ideal-management-tool), 19 October 2026, for the ten questions. The twin, its engine and every number in this article are from [the Thistlewood decision twin](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html), built for this article. Related: [ten questions, one graph](/articles/ten-questions-one-graph.html), [every risk is already accepted](/articles/every-risk-is-already-accepted.html), [the graph companies](/articles/the-graph-companies.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
