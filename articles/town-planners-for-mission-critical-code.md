# Town planners for mission-critical code: the US ground stop of 13 November is a case for teams that read, certify and test every line, and for using AI to make that work scale, not to skip it, sgit.ai

> On 13 November a change to the private network that links US air traffic control was followed by a reboot, a crash and about five hours with no departures. Vincent Lextrait posted that it was "most likely" AI slop, pointing at L3Harris, which runs the network, and at its technology chief's enthusiasm for vibe coding. I agreed with the direction and added two caveats, and this expands them. First, we need evidence: so far the reports point to a software update and security patches that overwhelmed old routers, officials say the FAA's own AI systems played no role, and nothing yet ties the change to AI-written code. Aviation investigates well, so we should eventually know. Second, whatever wrote the change, systems like this belong to what Simon Wardley calls town planners: every line read, certified and fully tested, not by "a human" but by a team of experienced engineers, architects, designers, testers, and resilience and security specialists. Where AI belongs in that world is not the line of code that ships. It is everything around it: understanding a large old codebase, mapping what a change can reach, aligning every rule with the check that holds it, and testing far more than a team could by hand. Used there, AI raises quality and resilience instead of lowering them.

*Source: <https://newsroom.sgit.ai/articles/town-planners-for-mission-critical-code.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Town planners for mission-critical code: the US ground stop of 13 November is a case for teams that read, certify and test every line, and for using AI to make that work scale, not to skip it

# Town planners for mission-critical code: the US ground stop of 13 November is a case for teams that read, certify and test every line, and for using AI to make that work scale, not to skip it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-14 · [article v1.0.0](versions/town-planners-for-mission-critical-code.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · wardley-mapstown-plannersresilienceaviationai-codingnfrstestingreplyarticle

***Abstract:** On 13 November a change to the private network that links US air traffic control was followed by a reboot, a crash and about five hours with no departures. Vincent Lextrait posted that it was "most likely" AI slop, pointing at L3Harris, which runs the network, and at its technology chief's enthusiasm for vibe coding. I agreed with the direction and added two caveats, and this expands them. First, we need evidence: so far the reports point to a software update and security patches that overwhelmed old routers, officials say the FAA's own AI systems played no role, and nothing yet ties the change to AI-written code. Aviation investigates well, so we should eventually know. Second, whatever wrote the change, systems like this belong to what Simon Wardley calls town planners: every line read, certified and fully tested, not by "a human" but by a team of experienced engineers, architects, designers, testers, and resilience and security specialists. Where AI belongs in that world is not the line of code that ships. It is everything around it: understanding a large old codebase, mapping what a change can reach, aligning every rule with the check that holds it, and testing far more than a team could by hand. Used there, AI raises quality and resilience instead of lowering them.*

Explorers, villagers and town planners, and where an air traffic communications network sits among them.

## In short

- **What happened:** on 13 November, an update to the private network that links US air traffic control was followed by a reboot, a crash and a nationwide ground stop of about five hours.
- **The claim:** that AI-written code caused it. **The evidence so far:** a software update and security patches on an old network; no evidence yet that AI wrote the change.
- **My first caveat:** we need the investigation's evidence, and aviation investigates well.
- **My second caveat:** whatever wrote it, this is town planner territory, where every line is read, certified and tested by an experienced, multidisciplinary team.
- **Where AI belongs there:** understanding, connecting, aligning and testing around the code, at a scale people cannot reach by hand.

## The post and my reply

Vincent Lextrait, founder of METASPEX, posted on LinkedIn that, "Thanks most likely to AI slop", the US sky had been empty for hours, that "a botched software update prepared by L3Harris Technologies triggered a system reboot and subsequent crash", and that the company's leadership encourages its engineers to use AI-assisted coding tools. He called it "yet another disastrous sign of global software ensh*tt*f*cation due to AI".

I agree with the worry. My reply:

Agree, but in this case we really need evidence of what happened (since it could had nothing to do with that AI focus by that company). I guess the good news is that at least the airline industry does really good investigations, so we should (eventually) really find out what happened

>

and yes, for mission critical systems like this (which should be managed in a "Town Planner" mode (aka #WardleyMaps)) every line of code needs to be read, certified and fully tested, not just by a 'human', but by a highly experienced and knowledgeable team of engineers, architects, designers, testers, resilience and security

## What we know so far

From the reporting on 13 and 14 November:

- **The stop:** about five hours. Flightradar24 counted about 3,100 aircraft in the air bound for US airports when it began; FlightAware listed more than 10,000 delays and over 4,000 cancellations that day ([CBS News](https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/)). Flights resumed at 8:15 pm Eastern after the FAA said it had "thoroughly tested our systems".
- **The cause, as reported:** multiple sources told CBS News that "an update to the private communications network" caused the system to reboot, leading to a crash. The network is operated by L3Harris, which had not commented.
- **What officials said:** the Transportation Secretary blamed "an incredibly old air traffic control system" and overloaded routers; the Homeland Security Secretary said new security patches appeared to "overwhelm" the routers, and that there was no cyberattack.
- **The investigation:** Bloomberg reported that the FBI is looking at a software update as a potential cause, and officials said the FAA's recently deployed AI systems played no role ([SecurityWeek](https://www.securityweek.com/no-signs-of-hacking-in-faa-ground-stop-as-fbi-reportedly-probes-software-update/)).
- **On AI at L3Harris:** the quote about vibe coding is from the company's CTO, Andrew Puryear (not Andrew Boyd, as the post had it), on [a Shield Capital podcast](https://shieldcap.com/episodes/l3harris) of 4 December 2025: "I love the trend of vibe coding because it really does help accelerate workflows", and, in the same answer, that studies of its quality have "somewhat mixed reviews".

So the honest position today is: a change went into an old, critical network and it fell over. Who wrote the change, how it was tested and how it was rolled out are exactly the questions the investigation will answer.

## Town planner territory

A month ago I suggested [explorer coding](explorer-coding.md) as a better name for vibe coding, using Simon Wardley's three kinds of people: explorers, who find what is possible; villagers, who turn it into products people rely on; and town planners, who run what everything else depends on.

Explorer coding is the best thing to happen to software in a long time. It is also the wrong mode for a network that keeps a country's aircraft in contact with the ground. That network is the far end of the line: a commodity everyone depends on, where the code should be as deterministic as possible, every change rehearsed and reversible, and every line read.

And "read by a human" is not enough. A single reviewer, however good, cannot hold an old telecommunications stack, its routers, its patches and its failure modes in their head. Town planner work is done by a team: engineers who know the code, architects who know the system, designers who know the operators, testers who know how it breaks, and resilience and security specialists who know what happens when it does.

## Where AI belongs in that pipeline

A town planner pipeline with AI in it: map the reach, check the rules, test hard, people certify, roll out in stages.

This is the part I most want to add to the debate. The answer to "AI wrote risky code" is not "no AI near critical systems". It is to put AI where it raises the quality bar, in the work around the code that ships, which is where teams always run out of time:

- **Understanding.** Reading a large, old codebase and explaining what a change really does, in the words of the people who will certify it.
- **Connecting.** Keeping a graph from every line of code up to the service, the story and the requirement it serves, so a change to one router's software shows everything it can reach. I described that climb in [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md): one fix, read upwards, reaching nine of a tool's 72 commands.
- **Alignment.** Writing every rule as intent and mapping it to the check that holds it, so the gaps are visible. When we measured our own house rules, none of the 31 had a passing CI guard ([coding standards are behaviour policies](coding-standards-are-behaviour-policies.md)). A town planner team cannot afford that gap; AI makes closing it affordable.
- **Testing.** Far more cases, replayed traffic, a digital twin of the network, load and failure drills, run on every change, not once a quarter.
- **The non-functional requirements.** Version control, reliability, resilience, security, backups, consistency, explainability and documentation: the scaffolding every critical system needs and few have enough people to maintain.

Used there, AI does not replace the team that certifies a change. It gives that team more evidence than it has ever had, in time to use it.

## What this does not claim

- **It does not claim to know the cause.** The investigation has not reported; the facts above are from news reports on 13 and 14 November.
- **It does not describe L3Harris's or the FAA's process,** which I do not know; the pipeline is a proposal.
- **It does not claim AI was or was not involved** in the change.

## Where this comes from

Vincent Lextrait's LinkedIn post and my reply to it, 14 November 2026. [CBS News](https://www.cbsnews.com/news/faa-issues-nationwide-ground-stop/), 13 November 2026; [SecurityWeek](https://www.securityweek.com/no-signs-of-hacking-in-faa-ground-stop-as-fbi-reportedly-probes-software-update/), 14 November 2026; [Shield Capital, Episode 12: L3Harris](https://shieldcap.com/episodes/l3harris), 4 December 2025. Earlier on this site: [explorer coding](explorer-coding.md), [ephemeral town planner services](ephemeral-town-planner-services.md), [coding standards are behaviour policies](coding-standards-are-behaviour-policies.md), [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#town-planners-for-mission-critical-code)

### Builds on

- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Coding standards are behaviour policies: describe how your agents should write code as intent, map it across every language and team with a fractal graph, and see which rules are kept by a barrier and which only by habit](coding-standards-are-behaviour-policies.md) A coding standard is a behaviour policy: write it as intent, see what holds each rule, and map it across teams with a graph.
- [Ephemeral town planner services: a better name than serverless, now that serverless includes things that bill you by the hour](ephemeral-town-planner-services.md) Serverless meant scale to zero and pay per use; now it covers hourly bills. A better name: ephemeral town planner services, and a test for it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 396 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=396)

**Posting this article on LinkedIn?** The cover is [town-planners-for-mission-critical-code.jpg](banners/town-planners-for-mission-critical-code.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/town-planners-for-mission-critical-code.html)*
