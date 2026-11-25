---
title: A startup we found in our own work: how the Web Summit chasm made us zoom in from agentic cells to one thing we can sell for £50, why the Sovereign Website has an advantage the platforms cannot easily copy, and why it only works because of AgentiCCells, RiskMandate's behaviour policies, signed decisions and PKI
date: 2026-11-25
author: Dinis Cruz
author_url: about/index.html
summary: At Web Summit people understood what we showed them, the agents, the policies, the difference between a mandate and a grant, and then nothing happened next. Good leads, nobody bought, because there was no small first step. Agentic cells is still a powerful idea, but it is too big to buy on the spot. So we zoomed in, again, to find one thing we can sell, make it very cheap and almost give it away so that people want it: a website that is theirs, made by a team of agents in five designs, for £50 or €50 once. When we mapped it against eleven website platforms, only one said the same about owning your site, and it is a tool for people who code. That is a startup we discovered inside our own work. But it is important to say why it is possible: the agent behaviour policies that let many agents work together without it backfiring, the decisions agent that signs my words, the keys on pki.sgit.ai, and a pipeline that makes a site in seconds. The same layers let the PrompTugal data platform go from 9 to 30 sources in five days. This is the strategy, the map and the honest gaps.
version: v0.14.214
license: https://creativecommons.org/licenses/by/4.0/
tags: strategy, sovereign-website, agenticcells, riskmandate, abp, pki, promptugal, article
status: published
---

!shot dsu-chasm.webp | images/ | The stand and the chasm after it: interest, then no small first step. The bridge is a website. | figure

## In short {#in-short}

- **The summit showed the chasm:** people got it, and there was nothing small to buy next.
- **We zoomed in** from agentic teams to one product: a Sovereign Website, £50 or €50 once.
- **The advantage is ownership:** of eleven platforms mapped, only one says you can take the site away, and it is for coders.
- **It only works because of the layers underneath:** AgentiCCells, RiskMandate's behaviour policies, signed decisions, PKI and the site factory.
- **The same layers made PrompTugal's data grow** from 9 to 30 sources in five days.

## The chasm {#chasm}

Our stand at Web Summit, 9 to 12 November, had a journey I have told many times since. Someone stops: "Ooh, what's that?" They see the agents, around 250 of them, more than 60 at once. We show them the policies, what each agent may and may not do, and the difference between a mandate and a grant. We say "if you have agents, we can help you control them", with the prices. And then nothing. The sherpa agent wrote it up as the first finding: "between 'impressed' and 'bought' there was no small first step and nowhere to try the policies." In my words: "We didn't have a good way for them to come out of it and experiment and policy. And that's why these websites are about." I wrote about what the summit validated and what it showed was missing in [the way in](/articles/the-way-in.html); this is what we did about it.

## Zooming in {#zoom}

AgentiCCells is about selling agentic teams, and I still think that is powerful. But a team is not something you buy at a stand. A startup has to find something very easy, very narrow and able to scale ([simple on top of years](/articles/simple-on-top-of-years.html)). On 19 November we named it: "we're selling sovereign websites". The record of that day says it in one line: "AgentiCCells sells agentic teams; SAW sells one thing, a website built by agents and owned by the person it is for."

On the same day agenticcells.ai briefly became a sovereign website site, and by the evening I had pulled it back: AgentiCCells should point to sovereign websites "as a powerful example … just one of the multiple ones that we sell". The website is the small cell; the teams are the business behind it. On 23 November I set the launch price at £50, and €50 on European sites, paid once, with £500 as the published anchor and no subscription ([sovereign agentic website](/articles/sovereign-agentic-website.html)).

!shot dsu-pricing.webp | images/ | sovereignwebsite.ai: "Paid once. Yours for good." and, plainly, "Nothing is sold yet." | screenshot

The idea is to make it so cheap that it is almost given away, so that people want it, and to make it the bridge from the stand: a site on something the visitor already likes, football, CVEs, their own work, where they see the policies working on something they care about.

## The map {#map}

!shot dsu-market.webp | images/ | The strategy agent's market page: eleven platforms and what each says about taking your site away. | screenshot

The strategy agent read the public pages of eleven website products on 23 November and asked one question: can you take the site away? Wix: "your site must run on Wix's servers". Squarespace, in part: some content as an XML file. Webflow: HTML and CSS on paid plans, but "Dynamic content (CMS items/pages) can't be exported". Fliplet's terms allow no transfer. Its conclusion: of the eleven, "only Lovable says the same, and it is a tool for people who code."

The market is big and under-served. In the UK, 78% of businesses have a website, which means more than one in five do not; a census of 6,266 Google listings in 12 UK towns found 33% with no working site. In the EU, 79.0% of firms with ten or more staff have one. A freelancer build costs £500 to £1,500, with maintenance at £50 to £300 a month. Against that, £50 once for a site you own, in five designs, that your own AI can edit, is a different offer, and I think a crazy one. That is why I call this a startup we discovered: it was sitting in our own work, waiting to be named ([sovereign websites, the investment case](/articles/sovereign-websites-the-investment-case.html)).

## Why it is possible {#why}

!shot dsu-stack.webp | images/ | Why a £50 website is possible: the product is the thin layer on top of months of work underneath. | figure

A £50 website made by a team of agents is only possible because of what is underneath, and this is the part I want to be clear about.

- **AgentiCCells.** Teams of agents that you own, can see and can stop: maestros, conductors, keepers, a site per agent ([who runs the agents](/articles/who-runs-the-agents.html)). The website is one thing such a team does.
- **RiskMandate's agent behaviour policies.** Every agent and every pipeline has a policy that lists what it may do; anything not listed is refused. Since 21 November every site carries its own `abp.json`. This is what lets dozens of agents work in the same organisation without it backfiring, and what lets a pipeline create repositories without a person in the loop for each one ([almost a hundred repositories](/articles/almost-a-hundred-repositories.html)).
- **Signed decisions.** The decisions agent records my words with their scope and signs them; agents act only on a record they have checked, reviewed by a panel of five real agents. I can delegate routine yeses without losing track of who allowed what ([lawyers in the loop](/articles/lawyers-in-the-loop.html)).
- **PKI and SGit.** My key on pki.sgit.ai anchors a chain: it operates the decisions key, which endorses each maestro's key. Every commit we checked in the factory, the hub, decisions and strategy is signed. Vaults hold what is private ([the primitives of trust](/articles/the-primitives-of-trust.html)).

None of these was built for a £50 website. Together they are why one can exist, and why the speed is the moat: the code is open, and what is hard to copy is a team that can make, check and hand over a site in a day, inside rules anyone can read.

## The same layers, another product {#data}

!shot dsu-data.webp | images/ | PrompTugal's data: 9 sources on 17 November, 30 by 21 November, from weather to a city's transport and tide. | chart

The PrompTugal data platform shows the same effect on a different product. On 17 November it collected 9 sources, mostly the Portuguese weather service and storm warnings. By 21 November it had 30, each with its own collector and card: cyber vulnerabilities from CISA, NVD and ENISA's EUVD; public contracts from Portal BASE and Contracts Finder; Eurostat; cameras and events; and a live London set, TfL status, bikes, roads, the Thames tide and the grid's carbon intensity. Twelve ran hourly, twelve every six hours, five daily. A register lists 146 more candidates.

And then I stopped it. On 23 November I stopped every schedule, 41 of them. Nothing was wrong with the collectors: we are still working out the best way to collect, we do not have many readers yet, and I want to move the work to a different account and refactor it. Until then, collecting every hour was mostly a way to spend tokens. Being able to stop a whole data platform with one decision, and start it again when it is ready, is part of the same power ([start, stop, slow down](/articles/start-stop-slow-down.html)). Eleven sites read from it, from weather to cyber to civic data ([from a feed to meaning](/articles/from-a-feed-to-meaning.html), [sites on the data](/articles/sites-on-the-data.html)).

## What this does not claim {#limits}

- **Nothing is sold yet,** as sovereignwebsite.ai says; the £50 offer is a launch price set on 23 November.
- **The stand journey is my account,** written up by an agent, not measured.
- **The market figures are the strategy agent's,** from public sources read on 23 November; the platform comparison is what each page says, not a test of each product.
- **Collection is stopped for now,** on purpose: data.promptugal.news shows data read on 21 November.
- **Editing a site yourself needs a Claude plan,** or a partner, as the price page says.

## Where this comes from {#sources}

[sovereignwebsite.ai](https://sovereignwebsite.ai/) and its [prices](https://sovereignwebsite.ai/pricing.html), [the market page](https://strategy.agents.sovereignweb.site/accounts/b/market/) of the strategy agent and its map of the sovereign website, the [decisions](https://decisions.agents.sovereignweb.site/) site and [pki.sgit.ai](https://pki.sgit.ai/), read on 25 November 2026. In [PrompTugal__News__Website](https://github.com/PrompTugal/PrompTugal__News__Website): `board/team/sherpa.d/needs/journey-the-stand.md` and `board/team/maestro.b/decisions/2026-11-19-sovereign-website.md`. AgentiCCells__Website's `board/briefs/2026-11-19-refactor-agentic-cells.md`. SovereignWebsite__IaC's `board/2026-11-21__agent-behaviour-policy-on-every-site.md`. [PrompTugal__News__Data](https://github.com/PrompTugal/PrompTugal__News__Data) (`sources/*/card.json`, `register/sources.json`). Related: [the way in](/articles/the-way-in.html), [simple on top of years](/articles/simple-on-top-of-years.html), [sovereign agentic website](/articles/sovereign-agentic-website.html), [the intersection](/articles/the-intersection.html), [almost a hundred repositories](/articles/almost-a-hundred-repositories.html), [who runs the agents](/articles/who-runs-the-agents.html).
