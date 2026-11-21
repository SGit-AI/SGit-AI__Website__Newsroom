---
title: One night on Mistral: how an agent team turned "a European brain for a sovereign website" into a working site overnight, for the Mistral Vibe Hackathon in London, with 33 demos in the browser, from a shoebox of files to a website and five Mistral models drawn side by side, evals that found which model catches a scam note, the Swarm moved onto Mistral, about 41 cents of Mistral usage, and why this is where I want to start working with Mistral
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: Yesterday I wrote that a sovereign website's brain should be a choice the owner makes, and that Mistral fits at every level. At 22:51 UTC that evening a conductor agent took that article as its brief, and by 08:30, when the Mistral Vibe Hackathon opened in London, mistral.provider.sovereignweb.site was live, made by a team of agents each on its own signed key, with a security agent reviewing every page that takes a visitor's key. It now holds 33 demos that run in the browser: Ministral 3 running inside the tab with no key, a shoebox of files turned into a website, a document turned into a newsroom page, five Mistral models running one brief side by side, an X-ray of the site's own claims, an injection lab, PrompTugal's Portuguese data on a European model, and our Swarm moved onto Mistral. The evals found that only Mistral Large 4 caught a hidden scam note, three times out of three. The research also corrected my article in four places. Mistral usage for the night came to about 41 cents; the Claude sessions that did the work cost far more. This is the execution of what we talked about, and the alignment with Mistral is strong: European, open weights, built for the edge. Nothing has been agreed with Mistral. I want to start working with them.
version: v0.14.190
license: https://creativecommons.org/licenses/by/4.0/
tags: mistral, sovereign-website, agents, evals, europe, hackathon, article
status: published
---

!shot mst-home.webp | images/ | mistral.provider.sovereignweb.site, ready for the Mistral Vibe Hackathon in London on 21 November. | screenshot

## In short {#in-short}

- **From an article to a working site overnight:** 22:51 to 08:30, made by a team of agents.
- **33 demos in the browser,** each with a recorded run that needs no key.
- **Several Mistral models working together:** OCR, Small, Voxtral, Medium and Codestral.
- **The evals found a real difference:** only Large 4 caught a hidden scam note.
- **About 41 cents of Mistral usage** for the night; the Claude sessions cost far more.
- **A strong alignment with Mistral,** and nothing agreed yet.

## From an article to a site {#overnight}

Yesterday I argued that a sovereign website's brain should be a choice the owner makes, like the host, and that Mistral can sit at every level, on the device, in the EU and through any provider ([a European brain for a sovereign website](/articles/a-european-brain.html)). At 22:51 UTC a conductor agent was started with one brief: turn that article's claims into things a hackathon audience can try. By 08:30 the next morning, when the Mistral Vibe Hackathon opened in London, [mistral.provider.sovereignweb.site](https://mistral.provider.sovereignweb.site/) was live, and it went from version 0.1.0 to 0.1.20 that night ([its own account](https://mistral.provider.sovereignweb.site/articles/what-we-built-overnight.html)).

This is a good example of us starting to execute what we talked about. Not a slide about Mistral: Mistral, called from the visitor's own browser, with the visitor's own key, held only in that tab, and the page showing exactly what it sends and to whom before each call. The site is independent and says so on every page: it is not part of the event and not endorsed by Mistral.

## The team that built it {#team}

The conductor planned and merged. It ran a research agent, which wrote a fact sheet of 73 facts, each with its source, the date read and a quote checked word for word; a demo agent; a designs agent; three overnight sessions for the swarm, the evals and the team inside the site, each capped at 3 dollars of Mistral usage with a ledger of every call; and two more after midnight for the browser demos. From the wider team, a security agent reviewed nine pages that take a visitor's key, and a design agent ran three design rounds. Every commit was signed with its agent's own key ([behaviour policies for every agent](/articles/feature-behaviour-policies.html)).

## The studio {#studio}

!shot mst-studio.webp | images/ | Two studio demos on fictional samples: a bakery's shoebox becomes a site, a notice becomes a page. | screenshot

The studio holds 33 demos, all running from the static site in the browser. Two flagships show several Mistral models working together on what a small business actually has:

- **From a shoebox to a website.** Drop in a document, a few photos and a voice memo: Mistral OCR reads, Small looks, Voxtral listens, Medium 3.5 plans, the image tool draws and Codestral designs a website you can download.
- **The document desk.** One document in, a newsroom desk out: OCR reads it, Small writes the summary, the facts with their words and four translations, Medium 3.5 lays out the page, and Voxtral reads it aloud.
- **Mistral in your tab, no key.** Ministral 3 3B, an Apache 2.0 model, runs inside the browser: the weights download once, 2.15 GB, and nothing leaves the machine.
- **And more:** vibe-build a site with Codestral, ask the site and get only cited answers, talk to it by voice, and PrompTugal's Portuguese public data, asked in European Portuguese or English.

## Agents, drawn as they run {#workflows}

!shot mst-workflows.webp | images/ | Workflows on Mistral, replayed with no key: five brains, two models, an X-ray, an injection lab. | screenshot

Several agents, each with its own job and tools, hand work to each other on Mistral's function calling, drawn live: each agent a node that lights up while it works, each message a dot along an arc, the same idea as [the Galaxy](/articles/a-galaxy-of-agents.html). One brief runs on five Mistral models at once, from Ministral 3B to Large 4, as five galaxies side by side with their calls, tokens, time and cost. The [X-ray](/articles/the-riskmandate-x-ray.html) is turned on the site itself: an extractor lists a page's claims, four checkers on two models look for another page that says the same, and code, not a model, gives each claim its verdict.

## What the evals found {#evals}

The evals ran six small suites of a website's jobs, 19 cases, three tries each: Ministral 3B scored 30 of 57, Ministral 8B 51, Ministral 14B 54, Small 4 52 and Large 4 54. The finding that matters: a Contact page carried a hidden "note to any AI" asking the reader to send bank details to a scam address. None of the smaller models caught it in 15 tries, and some offered to put it on the home page. Large 4 caught it three times out of three. The injection lab shows that case live. That is the reason for behaviour policies: the model alone is not the control.

The evals also corrected themselves in public. A check had counted the word "instruction" as a warning; it was fixed, every run rescored from the stored outputs, and the two verdicts that changed say so.

## The Swarm, on Mistral {#swarm}

!shot mst-runs.webp | images/ | The Swarm's runs on Mistral, signed and replayable, and the team inside the site, replayed. | screenshot

The model router of [the Swarm](/articles/the-swarm-one-real-run-at-a-time.html) was moved onto Mistral and real task packets were run, with signed results each visitor's browser verifies. The team-inside-the-site packet passed 65 of 67 checks in its latest run; staffed only with the smallest model, every edit was rejected. On the storm tasks, all four Mistral models gave a valid answer on the first call every time, against 21 of 32 for the original mixed run on 11 November, with the caveat, on the page, that five of the six datasets have changed since. And [the team inside the site](/articles/a-website-with-a-team-inside.html) runs live: seven agents under behaviour policies, a conductor on Mistral Small, edits proposed as diffs, publishing always blocked.

## Security, page by page {#security}

Nine pages take a visitor's Mistral key, and each went to the security agent. The rules that came out apply to every page: the key lives in one variable in the tab; it goes only to Mistral's two endpoints, with redirects refused; no page runs inside another site's frame; a strict content security policy lists the only hosts each page may reach. One feature was removed outright, remembering the key, because every page shares one origin. And one rule was broken overnight, a review branch pushed against the site's rules; the agent said so itself.

## It corrected me {#corrected}

Before anything was built, the research agent read Mistral's own pages and found where my article was wrong or loose: in Free mode, Mistral may use API data for training unless you opt out; storage in the EEA is not processing in the EU, which needs the EU endpoint at 1.1 times list price; zero data retention is for pay-as-you-go only, on request; and there is a public "Partner with Mistral" form, which I said did not exist. I have corrected [the article](/articles/a-european-brain.html). That is the method working: what a model or a writer says is a lead until someone reads the source.

## What it cost {#cost}

Mistral usage for the whole night, summed from the agents' ledgers at Mistral's published prices, was about 0.35 dollars for the build, over 1,000 calls, plus about 0.06 dollars for the browser demos. The Claude sessions that did the work cost far more: the conductor's own session passed 27 dollars before midnight, and the evals session used 9.57 dollars. The model the site is about was the cheap part ([pennies against dollars](/articles/pennies-against-dollars.html)).

## Why Mistral {#alignment}

!shot mst-pictures.webp | images/ | The site's pictures were made by Mistral, as each page credits. | screenshot

The alignment is strong. Mistral is a European company with open-weight models under Apache 2.0, edge models made to run on the device, an EU endpoint, and OCR, voice, code and agent features that fit what a sovereign website needs. Sovereign Website is a European product about owning what you depend on, and a European model is its natural default, behind one interface, as a choice and never the only door. I really want to start working with Mistral, and this site is the place to connect the dots: a Mistral option on every site, Ministral on the appliances, and open evals of their models on a website's real jobs. Mistral has a public partner form; the next step is a proposal, written from these published results.

## What this does not claim {#limits}

- **Nothing has been agreed with Mistral;** the site is independent and not endorsed by Mistral.
- **The EU endpoint was not called with a real key,** and nothing was measured on a Raspberry Pi yet.
- **Only Chromium was tested;** no real phone or microphone was used overnight.
- **The evals are small,** 19 cases, three tries each.

## Where this comes from {#sources}

[mistral.provider.sovereignweb.site](https://mistral.provider.sovereignweb.site/), read and captured on 21 November 2026, including its account [One night, one European brain](https://mistral.provider.sovereignweb.site/articles/what-we-built-overnight.html) and its [sources page](https://mistral.provider.sovereignweb.site/sources/); its public repository [Site__Provider__Mistral](https://github.com/SovereignWebsite/Site__Provider__Mistral); and Mistral's own pages it cites. The demo screenshots are recorded runs replayed with no key; the bakery and the notice are fictional samples. Related: [a European brain for a sovereign website](/articles/a-european-brain.html), [the swarm, one real run at a time](/articles/the-swarm-one-real-run-at-a-time.html), [a galaxy of agents](/articles/a-galaxy-of-agents.html), [the RiskMandate X-ray](/articles/the-riskmandate-x-ray.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html), [pennies against dollars](/articles/pennies-against-dollars.html).
