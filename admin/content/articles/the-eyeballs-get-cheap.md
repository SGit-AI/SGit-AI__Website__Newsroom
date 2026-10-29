---
title: The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: For as long as I have worked in security there has been no clear winner between open source and proprietary software. Open source had the code in view, and fixes that sweep a bug's variants; it also had very few people and almost no budget for the slow, expensive reviews that find the hard bugs. Proprietary software had the budget, and the cover of being hidden, and got away with a lot. That balance just moved. Models can now run deep security reviews over and over, on every project, at a cost that used to buy one consultant for a day. The thing open source lacked was paid attention, and that is the thing that just became abundant. I thought Chainguard had started publishing the projects where its AI found nothing; I could not find that. What I found is better: the maintainer of curl writing about a year in which AI review first drowned his project in noise, then produced hundreds of real fixes, then a frontier scan that found a single low-severity bug, and then, today, deeper tools finding more. That is what a project getting harder to break looks like. Put it next to two things I have argued before, that sovereignty needs open code and open schemas, and that the business is maintaining the version each customer actually runs, and three forces meet at one place: the least amount of code in production.
version: v0.12.53
license: https://creativecommons.org/licenses/by/4.0/
tags: open-source, security, ai-security-review, vulnerabilities, curl, sovereignty, business-models, wardley-maps, supply-chain, article
status: published
---

!shot ox-balance.webp | images/ | Open source against proprietary: the balance that moved when model-driven security review became cheap and deep. | comparison

## In short {#in-short}

- **No clear winner, until now.** Open source had visibility and few reviewers; proprietary had budget and cover.
- **The eyeballs get cheap.** Deep security review by models, repeated on every change, is the attention open source could never pay for.
- **curl shows the shape.** Noise, then hundreds of real fixes, then a frontier scan that found one bug, then deeper tools finding more.
- **The scale is real.** Over a thousand projects scanned by one lab; thousands of patches by one coalition; maintainers asking for it to slow down.
- **Higher bars, fewer and better projects.** Low-hanging fruit disappears; contributions need proof; provenance matters.
- **Three forces meet.** Secure, sovereign and paid for, all pointing at the same place.
- **The least code in production.** What the maintainer sells, what the customer runs, and what security wants.

## No clear winner, until now {#balance}

The argument for open source security has always been Eric Raymond's, from The Cathedral and the Bazaar: "Given enough eyeballs, all bugs are shallow." The argument against it has always been that the eyeballs were not there. Most open source is understaffed and unpaid; in Tidelift's 2024 survey, as The Register reported, "The portion of respondents who reported they are unpaid hobbyists remains at 60 percent". Projects used by companies with thousands of developers are maintained by a handful of people with almost no revenue. Nobody pays for the slow security review that takes weeks, the kind I have done many times, where finding the bug, proving it and documenting it is work you cannot do in five minutes. The low-hanging fruit was eaten fast; the deep work often never happened.

Proprietary software had the opposite profile. It had budget for security teams and paid reviews. It also had cover: code nobody outside could read, fewer attackers looking, products hidden behind other environments. A lot of software got away with things that would not have survived being public. If the source of some of the major SaaS products were exposed tomorrow, a lot would be found.

What open source did have was efficiency. Anyone can read the code, and when a serious bug is reported publicly, the fix rarely stops at the one bug: the variations get hunted down too. We know how to build secure systems; the proof is the number that survive very motivated attackers. The question was always who could afford the attention.

## The eyeballs get cheap {#cheap}

That is what changed. I now run security reviews with models on the products I work on, and the depth is remarkable: it finds real issues, I can point it at particular areas, we argue about what it found, and we fix it. That used to take a specialist weeks. It now takes an afternoon, and it can run again on the next change.

The thing open source lacked was paid attention, and that is the thing that just became abundant. The thing proprietary software had, being hidden, is worth less every month, because the same reviews run on whatever ships, leaks or can be reverse engineered. That is the move: open source on steroids.

The numbers are already large. Anthropic's update on its Project Glasswing in May reported scanning "more than 1,000 open-source projects" and estimated "6,202 high- or critical-severity vulnerabilities" among the findings; the bottleneck, it said, is now "how quickly we can verify, disclose, and patch", and "some have even asked us to slow down" the rate of disclosures. Chainguard's Athena coalition reported, at its launch in June, "2,000 patches across 500 projects", and its harness, which [Chainguard, mapped](/articles/chainguard-mapped.html) described, has been run "against over 65 projects and validated over 680 findings". In DARPA's AI Cyber Challenge final in 2025, the systems "discovered 54 unique synthetic vulnerabilities" and also found "18 real, non-synthetic vulnerabilities".

## What it looks like from inside one project {#curl}

!shot ox-curl.webp | images/ | One project, one year of machine eyeballs: curl, from its maintainer's own posts. | comparison

I went looking for something I thought I had seen, Chainguard publishing the projects where its AI hunting found nothing, with curl among them. I could not find it, from Chainguard or anyone else. What I found tells the story better, in the words of curl's maintainer, Daniel Stenberg.

First the noise. curl ended its bug bounty on 31 January 2026. Over its life it had found "87 confirmed vulnerabilities", but by 2025 "Not even one in twenty was real." Low-effort, machine-written reports were swamping a small team.

Then the real wave. In the autumn of 2025, AI-assisted reports from careful researchers and tools started landing real bugs, and by May he counted that earlier tools had "triggered somewhere between two and three hundred bugfixes".

Then the quiet scan. In May, a frontier model's scan of curl found one vulnerability, "yes, as in singular one", of low severity, and its report said "Zero memory-safety vulnerabilities found." His conclusion was the right one: "Any project that has not scanned their source code with AI powered tooling will likely find huge number of flaws".

And then, today, more. An audit with AI tooling produced "no less than thirty-five published curl vulnerabilities", a high-severity bug was found by Anthropic "using their new OSS Scanner", and curl 8.23.0 shipped with 24 security fixes.

That is not a project failing. It is a project getting harder to break, wave by wave, with each better tool finding what the last one could not, and the fixes sweeping the variants. The cost has moved from paying for attention to judging it: the maintainers' time is now the bottleneck, which is why curl's contribution rules now say that "If you asked an AI tool to find problems in curl, you **must** make sure to reveal this fact in your report."

## What changes for open source {#changes}

So I expect the bar to rise everywhere. More findings, with more proof. Contributions held to a much higher standard, because the small fixes a newcomer used to send can now be done by anyone with a model, and should be. Fewer projects, and better ones. The long tail of tiny packages and single-purpose libraries, the dependency trees with hundreds of entries, will shrink, because a lot of very specific little APIs can now be written in place, better.

What will not go away is security research by people motivated to find what the tools miss, domain experts who understand what a project is for, and maintainers who keep it working. And provenance will matter more: where a piece of code came from, who wrote it, who reviewed it. In Simon Wardley's terms, you do not want mission-critical code written at explorer speed; you want it industrialised. In [his words](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html), "Town Planners are brilliant people. They are able to take something and industrialise it". Accountable code, reviewed up to the line, is what makes all of this scale, and it is the same graph from story to line that [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html) draws.

## Three forces, one place {#forces}

!shot ox-forces.webp | images/ | Three forces meeting at the least code in production: secure, sovereign and commercially maintained open source. | architecture

Put this next to two things I have argued before, and they line up.

**Secure.** The eyeballs open source never had, at last, and a higher bar for everything that goes in.

**Sovereign.** You cannot have sovereignty without open source and open schemas. [Sovereignty is the ability to move](/articles/sovereignty-is-the-ability-to-move.html): move the data, the compute and the applications. You can only move what you can read and run elsewhere, and with competition on service rather than lock-in, the bigger companies should win because they serve better, not because the customer cannot leave.

**Paid for.** The business model I already run in my sgit environments, in vaults and in RiskMandate: the customer gets a private repository with their deployment, their configuration and only the features they actually use, and pays for it to be maintained. They could do it themselves, and then they would have to keep doing it. [The SaaS apocalypse](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) made the same point from the other side: what people really bought was never the features, it was that the thing is maintained, and the future is companies that take what was built and run it. This is not a free-for-all; open source is a licence, as [What open source is, and is not](/articles/what-open-source-is-and-is-not.html) explained, and [Open source is not free](/articles/open-source-is-not-free.html) measured how little of its value comes back to it. Maintenance as the product is how more of it can.

## The least code in production {#least-code}

Here is the irony where the three meet. The customer wants only the features they use. The maintainer who sells the customised version wants as little as possible to maintain. Security wants as little as possible to review, patch and attack. Everyone ends up aligned on running the least amount of code in production, which is the argument of [The minimum code below](/articles/the-minimum-code-below.html), where removing what a use case never runs took one real tool from 1,500 files to 428.

For the first time, the incentives of the people who write open source, the people who sell it and the people who secure it point the same way. That is the intersection I think we are at: open source that is more secure because the eyeballs finally got cheap, required because sovereignty needs it, and paid for because maintaining exactly what each customer runs is a business.

## What this does not claim {#limits}

- **No list of clean projects.** I could not find Chainguard or anyone else publishing the projects where AI hunting found nothing; curl's story is the evidence instead.
- **curl is not clean.** It is a well-run project being found harder to break, and still having bugs found, as of today.
- **The counts are the reporters' own.** Anthropic's, Chainguard's and DARPA's figures are as they published them.
- **The cost and depth of model review are my experience.** On the products I work on; others will see different results.
- **The future part is an argument.** Fewer and better projects, a shrinking long tail, and maintenance as the business are predictions.

If you maintain an open source project and want help with review at this new scale, or you want your version of one maintained for you, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. A research agent gathered the evidence and the quotes were checked on the primary pages. Daniel Stenberg's [blog](https://daniel.haxx.se/blog/), including [the end of the curl bug bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/), [the May scan](https://daniel.haxx.se/blog/2026/05/11/), [a UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/) and [a curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/), and curl's [contribution rules](https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md); Anthropic, [Project Glasswing: an initial update](https://www.anthropic.com/news/glasswing-initial-update); Chainguard, [the first disclosure from its harness](https://www.chainguard.dev/unchained/the-first-disclosure-from-our-mythos-harness); Help Net Security on [the Athena coalition](https://helpnetsecurity.com/2026/06/17/chainguard-athena-coalition-fix-open-source-vulnerabilities/); DARPA, [AIxCC results](https://www.darpa.mil/news/2025/aixcc-results); The Register on [the Tidelift survey](https://www.theregister.com/2024/09/18/open_source_maintainers_underpaid/); Eric S. Raymond, [The Cathedral and the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html). All read on 14 October 2026.
