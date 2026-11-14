---
title: Town planners for mission-critical code: the US ground stop of 13 November is a case for teams that read, certify and test every line, and for using AI to make that work scale, not to skip it
date: 2026-11-14
author: Dinis Cruz
author_url: about/index.html
summary: On 13 November a change to the private network that links US air traffic control was followed by a reboot, a crash and about five hours with no departures. Vincent Lextrait posted that it was "most likely" AI slop, pointing at L3Harris, which runs the network, and at its technology chief's enthusiasm for vibe coding. I agreed with the direction and added two caveats, and this expands them. First, we need evidence: so far the reports point to a software update and security patches that overwhelmed old routers, officials say the FAA's own AI systems played no role, and nothing yet ties the change to AI-written code. Aviation investigates well, so we should eventually know. Second, whatever wrote the change, systems like this belong to what Simon Wardley calls town planners: every line read, certified and fully tested, not by "a human" but by a team of experienced engineers, architects, designers, testers, and resilience and security specialists. Where AI belongs in that world is not the line of code that ships. It is everything around it: understanding a large old codebase, mapping what a change can reach, aligning every rule with the check that holds it, and testing far more than a team could by hand. Used there, AI raises quality and resilience instead of lowering them.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: wardley-maps, town-planners, resilience, aviation, ai-coding, nfrs, testing, reply, article
status: published
---

!shot tpm-spectrum.webp | images/ | Explorers, villagers and town planners, and where an air traffic communications network sits among them. | concept

## In short {#in-short}

- **What happened:** on 13 November, an update to the private network that links US air traffic control was followed by a reboot, a crash and a nationwide ground stop of about five hours.
- **The claim:** that AI-written code caused it. **The evidence so far:** a software update and security patches on an old network; no evidence yet that AI wrote the change.
- **My first caveat:** we need the investigation's evidence, and aviation investigates well.
- **My second caveat:** whatever wrote it, this is town planner territory, where every line is read, certified and tested by an experienced, multidisciplinary team.
- **Where AI belongs there:** understanding, connecting, aligning and testing around the code, at a scale people cannot reach by hand.

## The post and my reply {#reply}

Vincent Lextrait, founder of METASPEX, posted on LinkedIn that, "Thanks most likely to AI slop", the US sky had been empty for hours, that "a botched software update prepared by L3Harris Technologies triggered a system reboot and subsequent crash", and that the company's leadership encourages its engineers to use AI-assisted coding tools. He called it "yet another disastrous sign of global software ensh*tt*f*cation due to AI".

I agree with the worry. My reply:

> Agree, but in this case we really need evidence of what happened (since it could had nothing to do with that AI focus by that company). I guess the good news is that at least the airline industry does really good investigations, so we should (eventually) really find out what happened
>
> and yes, for mission critical systems like this (which should be managed in a "Town Planner" mode (aka #WardleyMaps)) every line of code needs to be read, certified and fully tested, not just by a 'human', but by a highly experienced and knowledgeable team of engineers, architects, designers, testers, resilience and security

## What we know so far {#facts}

From the reporting on 13 and 14 November:

- **The stop:** about five hours. Flightradar24 counted about 3,100 aircraft in the air bound for US airports when it began; FlightAware listed more than 10,000 delays and over 4,000 cancellations that day ([CBS News](https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/)). Flights resumed at 8:15 pm Eastern after the FAA said it had "thoroughly tested our systems".
- **The cause, as reported:** multiple sources told CBS News that "an update to the private communications network" caused the system to reboot, leading to a crash. The network is operated by L3Harris, which had not commented.
- **What officials said:** the Transportation Secretary blamed "an incredibly old air traffic control system" and overloaded routers; the Homeland Security Secretary said new security patches appeared to "overwhelm" the routers, and that there was no cyberattack.
- **The investigation:** Bloomberg reported that the FBI is looking at a software update as a potential cause, and officials said the FAA's recently deployed AI systems played no role ([SecurityWeek](https://www.securityweek.com/no-signs-of-hacking-in-faa-ground-stop-as-fbi-reportedly-probes-software-update/)).
- **On AI at L3Harris:** the quote about vibe coding is from the company's CTO, Andrew Puryear (not Andrew Boyd, as the post had it), on [a Shield Capital podcast](https://shieldcap.com/episodes/l3harris) of 4 December 2025: "I love the trend of vibe coding because it really does help accelerate workflows", and, in the same answer, that studies of its quality have "somewhat mixed reviews".

So the honest position today is: a change went into an old, critical network and it fell over. Who wrote the change, how it was tested and how it was rolled out are exactly the questions the investigation will answer.

## Town planner territory {#town-planners}

A month ago I suggested [explorer coding](/articles/explorer-coding.html) as a better name for vibe coding, using Simon Wardley's three kinds of people: explorers, who find what is possible; villagers, who turn it into products people rely on; and town planners, who run what everything else depends on.

Explorer coding is the best thing to happen to software in a long time. It is also the wrong mode for a network that keeps a country's aircraft in contact with the ground. That network is the far end of the line: a commodity everyone depends on, where the code should be as deterministic as possible, every change rehearsed and reversible, and every line read.

And "read by a human" is not enough. A single reviewer, however good, cannot hold an old telecommunications stack, its routers, its patches and its failure modes in their head. Town planner work is done by a team: engineers who know the code, architects who know the system, designers who know the operators, testers who know how it breaks, and resilience and security specialists who know what happens when it does.

## Where AI belongs in that pipeline {#ai}

!shot tpm-pipeline.webp | images/ | A town planner pipeline with AI in it: map the reach, check the rules, test hard, people certify, roll out in stages. | process

This is the part I most want to add to the debate. The answer to "AI wrote risky code" is not "no AI near critical systems". It is to put AI where it raises the quality bar, in the work around the code that ships, which is where teams always run out of time:

- **Understanding.** Reading a large, old codebase and explaining what a change really does, in the words of the people who will certify it.
- **Connecting.** Keeping a graph from every line of code up to the service, the story and the requirement it serves, so a change to one router's software shows everything it can reach. I described that climb in [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html): one fix, read upwards, reaching nine of a tool's 72 commands.
- **Alignment.** Writing every rule as intent and mapping it to the check that holds it, so the gaps are visible. When we measured our own house rules, none of the 31 had a passing CI guard ([coding standards are behaviour policies](/articles/coding-standards-are-behaviour-policies.html)). A town planner team cannot afford that gap; AI makes closing it affordable.
- **Testing.** Far more cases, replayed traffic, a digital twin of the network, load and failure drills, run on every change, not once a quarter.
- **The non-functional requirements.** Version control, reliability, resilience, security, backups, consistency, explainability and documentation: the scaffolding every critical system needs and few have enough people to maintain.

Used there, AI does not replace the team that certifies a change. It gives that team more evidence than it has ever had, in time to use it.

## What this does not claim {#limits}

- **It does not claim to know the cause.** The investigation has not reported; the facts above are from news reports on 13 and 14 November.
- **It does not describe L3Harris's or the FAA's process,** which I do not know; the pipeline is a proposal.
- **It does not claim AI was or was not involved** in the change.

## Where this comes from {#sources}

Vincent Lextrait's LinkedIn post and my reply to it, 14 November 2026. [CBS News](https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/), 13 November 2026; [SecurityWeek](https://www.securityweek.com/no-signs-of-hacking-in-faa-ground-stop-as-fbi-reportedly-probes-software-update/), 14 November 2026; [Shield Capital, Episode 12: L3Harris](https://shieldcap.com/episodes/l3harris), 4 December 2025. Earlier on this site: [explorer coding](/articles/explorer-coding.html), [ephemeral town planner services](/articles/ephemeral-town-planner-services.html), [coding standards are behaviour policies](/articles/coding-standards-are-behaviour-policies.html), [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html).
