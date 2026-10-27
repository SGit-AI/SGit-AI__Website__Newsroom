---
title: Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement path, and a marketplace for the consultants who deliver it
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: After Thursday's talk at Agentic Engineering Live in London, I think we are ready to sell this. The talk ran itself, twenty-six slides on a clock, most of them live pages that animated their own explanation, and the whole thing was built by the method it described: a Ruflo hive whose workers were Claude Code subagents, an sgit vault per run that kept everything they made, encrypted and versioned, and Agent Behaviour Policies that say what each role may do. ruv.sgit.ai has the five articles written straight after it, the talk, and four offers with published prices. So this article maps the market before we go into it. Who else sells agentic services: the big consultancies with agent platforms, the model vendors with partner networks and forward-deployed engineers, Cognitum with its own four-week discovery, and boutiques selling £2,500 audits and €2,900 sprints. Where the gap is: Gartner expects more than 40% of agentic projects to be cancelled by the end of 2027 for cost, unclear value or weak risk controls. Our position is the evidence: every run leaves a vault and a ledger the client keeps. The engagement path starts with a run and two hours of expert time, and grows to a four-day pilot and a maintained setup. And the delivery needs people, so the last part is a marketplace for consultants: Mondweep Chakravorty, co-founder of the Agentics Foundation's London chapter, and I are the first two; this is the invitation to the rest of the community, with the onboarding we propose.
version: v0.12.73
license: https://creativecommons.org/licenses/by/4.0/
tags: agentics, agentic-workflows, consulting, ruflo, sgit, agent-behaviour-policy, go-to-market, pricing, marketplace, consultants, agentics-foundation, article
status: published
---

!shot gx-market.webp | images/ | Where agentic services sit in October 2026, by price of a first engagement and how much rests on evidence. | comparison

## In short {#in-short}

- **The demonstration is done.** A talk built and run by a governed agent hive, with its evidence published.
- **The market is crowded at the top and thin on evidence.** Platforms, partner networks, forward-deployed engineers, boutiques.
- **The gap is trust.** More than 40% of agentic projects are expected to be cancelled by 2027.
- **Our position: evidence first.** Every run ends in a vault and a ledger the client keeps.
- **The path starts small.** A run, two hours, a day, a four-day pilot, then run it yourself.
- **It needs people.** A marketplace of consultants who deliver it, Mondweep and me first.
- **Who else wants to join?** The onboarding is below.

## What we showed {#showed}

On Thursday evening, 15 October, I gave the first community talk at [Agentic Engineering Live](https://ruv.sgit.ai/talk/), after rUv's keynote, for the Agentics Foundation's London chapter. The talk was called *Autonomy with a mandate and a memory*, and it ran itself: twenty-six slides on a clock, most of them live web pages that animate themselves and read their numbers from the site's own data, while I spoke over them. [The long read](https://ruv.sgit.ai/articles/the-talk-long-read.html) goes through it slide by slide; [the talk, live](https://ruv.sgit.ai/articles/the-talk-live.html) puts thirteen of its animations on one page, each with its own controls.

What matters more than the talk is how it was made. [How it was made](https://ruv.sgit.ai/articles/how-it-was-made.html) tells it from the record: about a day from an empty repository, a Ruflo hive whose workers were Claude Code subagents, nine runs each with its own ephemeral sgit vault, and a ledger of every run: 28 workers, 57 vault commits, no plaintext found in anything the server stored, every fresh clone identical, every vault deleted at the end. [The talk player](https://ruv.sgit.ai/articles/the-talk-player.html) explains how a talk becomes a file of beats, and [walking backwards](https://ruv.sgit.ai/articles/walking-backwards.html) shows how its features arrived, one request at a time. The articles are honest about what was not done, and so should this be: the runs were not gated by a compiled behaviour policy; that was shown separately, in the first proof of concept, where the same eleven actions went through Ruflo's policy engine in enforce mode and six were stopped: four denied and two sent to a person.

That is the product: **a hive, a memory and a mandate**. Ruflo gives the many hands; an sgit vault gives the memory, encrypted, versioned and kept by the client; an [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) gives each role its mandate. I have been calling it agentic workflows; I think **agentics** is the better word for what we sell, because it is the practice, not one workflow.

## Who else is selling this {#market}

The market for agentic services is real and crowded, and it is crowded at the top. The large consultancies have each built an agent platform or a factory to sell: Accenture's AI Refinery and its agent "trust score", Deloitte's Zora AI, PwC's agent OS, EY's agentic platform, IBM's Consulting Advantage, Capgemini's agentic customer work, Thoughtworks' Agent/works, which sells "a single control plane and a governed runtime for their AI agents". The model vendors sell through partners and their own engineers. Anthropic's [Claude Partner Network](https://www.anthropic.com/news/claude-partner-network), launched in March, committed "an initial $100 million to this network for 2026", is open to "Any organization that is bringing Claude to market", and certifies its first architects; OpenAI's consulting was reported in 2025 to start at about $10 million a client, delivered by forward-deployed engineers, the model Palantir made famous. Agent platforms such as Sierra and Decagon sell implementation with the product.

rUv's own company, [Cognitum](https://cognitum.one/consulting), sells consulting on the same stack we build on: "Not generic AI consulting. These are the components we build and maintain", starting with a four-week discovery, then three months of deployment and a production term of one to three years, with "attestation over every agent action". Prices are by scope, and it is building a certified partner network.

At the other end, boutiques sell small, fixed-price engagements, and their prices are the useful benchmark for us. In London, [Templab](https://www.templab.ai/) sells a one-week discovery audit for £2,500 and a two-week pilot agent from £8,000. In Germany, [Pragma-Code](https://www.pragma-code.de/en/blog-ai-agent-cost-sme) sells a 14-day AI sprint for €2,900. [AIGist24](https://www.aigist24.com/services/ai-assessment-service) sells a two-week assessment for $4,999. The pattern is the same everywhere: a free call, a paid discovery, a fixed-price pilot, a build, a monthly retainer.

## Where the gap is {#gap}

The demand is not the problem. Gartner predicted in June 2025 that ["Over 40% of agentic AI projects will be canceled by the end of 2027"](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), citing "escalating costs, unclear business value or inadequate risk controls", and warned of "agent washing" by vendors with little real capability. MIT's NANDA initiative reported in 2025 that most organisations saw no measurable return from their generative AI pilots. The people we want to help are the ones in between: they are curious, they have support from the top and projects under way, and they are struggling to make agents work, or to show anyone that they do.

What they lack is not another platform. It is evidence: a run they can inspect, a record of what each agent did and was allowed to do, and the output in a form they keep. Most offers in the market promise governance; few hand the client the record. That is our position: **evidence first**. Every engagement leaves a vault the client keeps, with the work, the history and the ledger, and a behaviour policy that says what each agent was allowed to do. [The demonstration is the sales process](https://ruv.sgit.ai/articles/ruv-sgit-business-model.html), and the demonstration is checkable.

## The engagement path {#path}

!shot gx-path.webp | images/ | The engagement path: from a free conversation and a first run to a pilot and a maintained repository. | architecture

ruv.sgit.ai already publishes [four offers](https://ruv.sgit.ai/business/): task runs from £10 to £50, dedicated compute by the eight-hour block, a maintained repository of the whole setup from £149 a month, and expert time at £500 for about two hours, £1,500 for a day, and £5,000 for four days setting it up in the client's own environment. Expert time sits exactly in the band I would like to start with, £1,500 to £5,000, and in the middle of the boutiques' prices.

So the path is: a conversation, free, about what the client wants agents to do and what they must never do; a first run on a real problem, which costs pounds, not thousands, and leaves a vault; two hours to steer it, or a day to write the behaviour policy for one team; a four-day pilot in their own environment; and then the maintained setup, so they can run it themselves. Each step is small enough to say yes to, and each ends with something they keep. The plan is honest about where it stands: no paid run yet, nothing automated end to end, and [the pricing](https://ruv.sgit.ai/articles/ruv-sgit-business-model.html) is a set of hypotheses to test with the first ten customers.

## A marketplace for the people who deliver it {#marketplace}

!shot gx-market-place.webp | images/ | A marketplace for the people who deliver it: clients pick a project type, then the consultants. | architecture

This only scales with people. Agentic engagements need someone who knows the client's world and can steer a hive in it, and there are many more of those people in the community than there are hours in my week. So alongside the offers, the idea is a marketplace: a small, curated list of consultants who deliver agentic engagements on this stack, where a client picks the kind of project first and then the people.

**The first two.** Mondweep Chakravorty, co-founder of the [Agentics Foundation's London chapter](https://london.agentics.org/), which runs the meetups where all of this was shown, and me. We are not taking bookings yet: we need to align our diaries first, so for now the page will say *register interest*, not *book*.

**The project types**, to start: a first run with a guide; a behaviour policy for one team's agents; a four-day pilot in the client's environment; a talk or workshop built the way ours was; and a review of an agent that is already running. Each has a scope, a duration and a price within the band, set by the consultant.

**How to join.** The markets that work have converged on the same few steps, and we can copy them. Toptal [publishes](https://www.toptal.com/top-3-percent) that fewer than 3% of applicants pass its five stages; A.Team sends a client "two to three profiles" to interview; n8n's experts programme asks for at least three customers using the product. For us:

1. **Apply** with a profile and the project types you offer.
2. **Show proof of work**: a public vault or repository of a real run you did, with its ledger.
3. **Peer review**: two members read it.
4. **Interview**: thirty to forty-five minutes, with a scenario.
5. **Pilot**: your first engagement, shadowed by a member.
6. **Standards**: ratings, delivery on time, and a behaviour policy for consultants that you sign, the same idea we apply to agents.

**The money**, as a proposal: the consultant sets the price within the band and keeps most of it; a small platform share pays for the catalogue, the runs and the vetting. For reference, Malt [charges freelancers 5%](https://help.malt.com/hc/en-150/articles/29539691425938), Upwork [0% to 15%](https://support.upwork.com/hc/en-us/articles/211062538), and Braintrust a 15% fee to the client; most markets sit between 5% and 20% in total.

**Who else wants to join?** If you build with agents, know an industry well, and want to deliver engagements like these, write to the address at the end with what you would offer and a link to something you have built.

## A brief for the marketplace page {#brief}

1. **One page on sgit.ai**, linked from ruv.sgit.ai's offers: *Agentics engagements*.
2. **The catalogue first**: the five project types, each with scope, duration and price band.
3. **Then the people**: one card per consultant, with project types, prices, stack, proof-of-work vaults and availability.
4. **No checkout**: *register interest* and *book availability* by email, until diaries are set.
5. **Join**: the six steps, the code of conduct, and the platform share, published.
6. **Evidence on every card**: a link to a public vault of a real run.

## What this does not claim {#limits}

- **No paid engagement yet.** The offers and prices are published; nobody has bought one.
- **The runs were not policy-gated.** Enforcement was shown in a separate proof of concept.
- **The market map is a judgement.** Positions are ours; prices are from public pages.
- **Some market figures are reported.** Gartner's and OpenAI's are from press releases and coverage.
- **The marketplace is a design.** Nothing is built; the platform share is a proposal.
- **This is not rUv's or Cognitum's offer.** It builds on their open-source stack.

If you want an engagement, or want to join as a consultant, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. ruv.sgit.ai: [the talk](https://ruv.sgit.ai/talk/), [the articles](https://ruv.sgit.ai/articles/), [the offers](https://ruv.sgit.ai/business/) and [the business plan](https://ruv.sgit.ai/articles/ruv-sgit-business-model.html), read on 16 October 2026. Market sources: Anthropic, [Claude Partner Network](https://www.anthropic.com/news/claude-partner-network), 12 March 2026; Gartner, [press release of 25 June 2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027); The Decoder on [OpenAI's consulting](https://the-decoder.com/openai-is-charging-at-least-10-million-per-client-for-its-enterprise-ai-consulting-services/); iTWire on [Thoughtworks Agent/works](https://itwire.com/business-it-news/security/thoughtworks-launches-agent-works-to-govern-and-run-enterprise-ai-agents-across-any-cloud); [Cognitum consulting](https://cognitum.one/consulting); [Templab](https://www.templab.ai/), [Pragma-Code](https://www.pragma-code.de/en/blog-ai-agent-cost-sme), [AIGist24](https://www.aigist24.com/services/ai-assessment-service). Marketplaces: [Toptal](https://www.toptal.com/top-3-percent), [A.Team](https://www.a.team/how-it-works), [n8n experts](https://n8n.io/experts/), [Malt](https://help.malt.com/hc/en-150/articles/29539691425938), [Upwork](https://support.upwork.com/hc/en-us/articles/211062538). The Agentics Foundation [London chapter](https://london.agentics.org/).
