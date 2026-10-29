---
title: A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: In December 2010, at OWASP's IBWAS conference in Lisbon, I gave a keynote called A 'Web Application Security' Challenge to Portugal. It had 168 slides, five proposed focuses and twelve proposed actions for government and industry, from allowing ethical hacking and publishing security score cards to liability for software, an independent vulnerability-disclosure agency, paying for open-source security and proper SSL for half of all websites. It ended with an argument that Portugal, which had nothing to lose, could become the Switzerland of hacking. Reading it again sixteen years later, more of it came true than I expected, though mostly from Brussels rather than Lisbon: software now falls under strict product liability, Europe has its own vulnerability database, manufacturers must report exploited vulnerabilities, and encrypted connections are the norm. What I got wrong was the mechanism. I thought fear of disasters would move governments; what moved them was regulation built slowly over a decade. And the part about Portugal itself, an open, ethical security industry as a way out of a depressed economy, is still mostly to do. This is the first of a series of articles on the talks I have given about Portugal, ahead of a new edition of Hacking Portugal.
version: v0.12.78
license: https://creativecommons.org/licenses/by/4.0/
tags: portugal, owasp, application-security, talks, history, regulation, europe, open-source, hacking-portugal, article
status: published
---

!shot pt-2010-slides.webp | images/ | Twelve slides from the IBWAS 2010 keynote in Lisbon: the five focuses, the twelve actions and Portugal as Switzerland. | comparison

## In short {#in-short}

- **December 2010, Lisbon.** The IBWAS keynote: 168 slides, five focuses, twelve actions.
- **Software deserves respect.** Treat application security as health and safety.
- **Twelve actions.** Ethical hacking, score cards, liability, disclosure, paying for open source.
- **Portugal could be the Switzerland of hacking.** Because it had nothing to lose.
- **More came true than I expected.** Mostly from Brussels, slowly, through regulation.
- **The mechanism was wrong.** Fear did not move governments; ten years of law did.
- **The Portugal part is still to do.**

## The talk {#talk}

On 17 December 2010 I gave the keynote at [IBWAS'10](https://wiki.owasp.org/images/0/0d/Dcruz.pdf), OWASP's Ibero-American web application security conference, at ISCTE in Lisbon. Its title was *A 'Web Application Security' Challenge to Portugal, and others that care about application security*, and its first slide was a disclaimer: "this is my personal opinion". A few weeks later [I wrote](https://diniscruz.blogspot.com/2011/01/keynote-at-owasp-ibwas-conference-lots.html) that "There are a lot of thought provoking ideas in there, and I don't expect that some of them will become reality any time soon." The press picked up one line: Portugal could be the "Switzerland of hacking".

The deck has four movements: a new paradigm, as five focuses and twelve actions; a section on fear, with the disasters that would follow if we kept ignoring software; examples from Portuguese websites; and a challenge to Portugal. This article goes through them with what I think today.

## Five focuses {#focuses}

The five focuses were: treat software and application security "with the respect and care that it deserves"; view application security as business intelligence; view it as competitive advantage; make the application security market "work"; and use OWASP as a resource and enabler.

**What still stands.** All five, and the second one more than I could have known. "Application security as business intelligence" was the idea that understanding how your software really works is valuable in itself, beyond finding bugs. Today that is exactly what I argue for agents and graphs: the value of GenAI is that it can understand, and a security team's job is to understand reality. The fourth, a market that works, is still the weakest: buyers still cannot easily tell secure software from insecure software.

## Twelve actions {#actions}

The twelve actions were for government or industry: allow ethical hacking; publish the results of security reviews as score cards; put security requirements in procurement; introduce liability for government and publicly traded companies; create an independent vulnerability-disclosure agency; rewrite computer laws; pay for open-source security; demand that widely used end-of-life applications, like IE6, be open sourced; create an insurance market; reduce the assets held, secrets and private data; improve journalism; and "'Proper' SSL support for 50% of websites".

**What came true, mostly from Brussels.**

- **Liability.** From 9 December 2026, the EU's new [Product Liability Directive](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive) brings software, standalone or embedded, under strict, no-fault liability. My slide said government and listed companies; the law went further.
- **Disclosure.** Europe has its own [vulnerability database](https://digital-strategy.ec.europa.eu/en/news/eu-launches-european-vulnerability-database-boost-its-digital-security), run by ENISA since May 2025, and since 11 September 2026 the [Cyber Resilience Act](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/cyber-resilience-act-reporting-obligations-apply-from-11-september-2026) requires manufacturers to report actively exploited vulnerabilities within 24 hours. Not quite an independent agency, but the same idea: disclosure as a public good.
- **Procurement, and Portugal.** Portugal's new cybersecurity law, [Decreto-Lei 125/2025](https://www.pwc.pt/pt/temas-actuais/dl-125-2025.html), which transposes NIS2, came into force on 3 April 2026, with the national cybersecurity centre as its authority.
- **Proper SSL.** Achieved, and then some: Google's [transparency report](https://transparencyreport.google.com/https/overview) shows most pages loaded in Chrome now use HTTPS, far past my 50%.

**What did not.** Score cards for software, an insurance market that prices application security well, and paying for open-source security at the scale it needs. On the last one I [wrote this month](/articles/open-source-is-not-free.html) that open source receives a tiny share of its value in investment. Reducing the assets held is the one I would put first today: the best way to protect data is not to have it, or to hold only ciphertext, which is [what sgit does](/articles/the-value-of-constraints.html).

## The fear section {#fear}

The middle of the deck was deliberately scary: everything is broken, "Its software everywhere", "How many many people will have to die before we take application security seriously?", and a game, "Bring the internet down for a day", a country-wide fire drill. I compared software to health and safety: we expect a minimum level of quality from water, food, cars and planes, and have laws that regulate them; "But, we have very little (if anything) in software and web applications".

**What I got wrong.** The analogy was right, and the mechanism was wrong. I thought fear, and a big enough incident, would move governments quickly. What moved them was a decade of slow, unglamorous regulation. Health and safety for software is arriving the way health and safety arrived for everything else: through liability and reporting duties, not through a single disaster.

## The challenge to Portugal {#portugal}

The last part was personal and blunt. I talked about my frustration with Portugal, a country I described as depressed, "and really needs new ideas", and argued that application security could be one of the solutions, "by showing how an open, vibrant, ethical, multi-cultural industry can work and flourish". Portugal had "nothing to lose (it is already rock-bottom)"; what I was asking for "doesn't cost any money"; "It only takes courage, focus and commitment". And: Portugal could become the "Switzerland of Hacking".

**What still stands.** The core of it: a small country can choose a sector and lead in it. Sixteen years later I made the same argument in [Judo for small countries](/articles/judo-for-small-countries.html), about AI. Portugal is no longer the depressed country of 2010, and some of the bluntness reads differently now. But Portugal did not become the Switzerland of hacking. That is the thread the next talks pick up: [Hacking Portugal in 2016](/articles/portugal-2016-hacking-portugal.html), and [GenAI in Portuguese in 2024](/articles/portugal-2024-genai-in-portuguese.html).

## What this does not claim {#limits}

- **Not that the talk caused any of it.** The EU's laws have their own long history.
- **The commentary is mine, now.** The slides are from 2010, unchanged.
- **The video seems to be gone.** The slides are the record.

If you were at IBWAS in 2010 and remember it differently, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the commentary and the editorial responsibility are mine. The slides, [A 'Web Application Security' Challenge to Portugal](https://wiki.owasp.org/images/0/0d/Dcruz.pdf), December 2010, on the OWASP wiki, and [my blog post](https://diniscruz.blogspot.com/2011/01/keynote-at-owasp-ibwas-conference-lots.html) of 12 January 2011. For today: the Product Liability Directive, via [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive); the European Commission on the [EUVD](https://digital-strategy.ec.europa.eu/en/news/eu-launches-european-vulnerability-database-boost-its-digital-security), 13 May 2025; the Cyber Resilience Act's reporting duties, via [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/cyber-resilience-act-reporting-obligations-apply-from-11-september-2026); Decreto-Lei 125/2025, via [PwC Portugal](https://www.pwc.pt/pt/temas-actuais/dl-125-2025.html). Read on 16 October 2026.
