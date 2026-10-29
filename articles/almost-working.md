# Almost working: a researcher, a curator and a journalist on a schedule, the QR handshake that gives each agent its key, and why a mission-critical workflow has to be built slowly, sgit.ai

> The PHP story site is now updated by three agents in a chain. A researcher follows the leads and captures pages, raw, into a large vault. A curator reads those captures and promotes what holds into a second, curated vault. A journalist reads that and updates the site, its numbers and its narrative. Each wakes on a schedule. Getting there took the better part of two days, with all the visibility and control I have, because the moment a workflow becomes mission critical every gap shows. The biggest gap was not the agents: neither Claude's scheduled tasks nor ChatGPT gives an agent an identity or a way to receive a secret. So we built one. A new agent session makes a key pair that lives only as long as the session, shows me its public key as a QR code, and I seal the vault key to it on pki.sgit.ai, signed by my root key. Then a schedule wakes that same session, which still holds the key. It is a slightly mad solution, and a lovely one. It is also not finished: on the evening of 23 October the researcher's passes are recorded, the curator has its key and its five wakes a day, and no agent has yet written its own run record. This is what it looks like to build something in its genesis stage, bit by bit, and why the next one will be much easier.

*Source: <https://newsroom.sgit.ai/articles/almost-working.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Almost working: a researcher, a curator and a journalist on a schedule, the QR handshake that gives each agent its key, and why a mission-critical workflow has to be built slowly

# Almost working: a researcher, a curator and a journalist on a schedule, the QR handshake that gives each agent its key, and why a mission-critical workflow has to be built slowly

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-23 · [article v1.2.0, 3 versions](versions/almost-working.md) · [newsroom v0.13.56](https://newsroom.sgit.ai/admin/versions.html) · agentsschedulespkiqrevidencephp2shellarticle

***Abstract:** The PHP story site is now updated by three agents in a chain. A researcher follows the leads and captures pages, raw, into a large vault. A curator reads those captures and promotes what holds into a second, curated vault. A journalist reads that and updates the site, its numbers and its narrative. Each wakes on a schedule. Getting there took the better part of two days, with all the visibility and control I have, because the moment a workflow becomes mission critical every gap shows. The biggest gap was not the agents: neither Claude's scheduled tasks nor ChatGPT gives an agent an identity or a way to receive a secret. So we built one. A new agent session makes a key pair that lives only as long as the session, shows me its public key as a QR code, and I seal the vault key to it on pki.sgit.ai, signed by my root key. Then a schedule wakes that same session, which still holds the key. It is a slightly mad solution, and a lovely one. It is also not finished: on the evening of 23 October the researcher's passes are recorded, the curator has its key and its five wakes a day, and no agent has yet written its own run record. This is what it looks like to build something in its genesis stage, bit by bit, and why the next one will be much easier.*

**Update, 24 October.** This article read the PHP site's schedule vault, which the agents had not yet adopted, and so understated how far things had got. By 23:30 UTC on 23 October the scheduled curator had promoted 33 captures (the evidence vault at 260 sources) and the scheduled source watch was running five times a day; just after midnight the schedules moved out of the schedule vault and into the repository, and the source watch into a pack-mode vault, `7r83qic5`. The day is in [PHP October 2026, day three](https://newsroom.sgit.ai/articles/php-daily-2026-10-23.html).

Three agents, three stores, one site: the source watch, the evidence vault and the schedule vault.

## In short

- **Three agents in a chain.** A researcher captures, a curator curates, a journalist publishes.
- **The hard part is updatability.** When did we last check, and can we prove that "nothing new" means nothing new?
- **The platforms have no place for an agent's identity or secrets.** Claude's scheduled tasks and ChatGPT both fell short there.
- **So each agent gets its key by QR handshake.** A session key, my root key on pki.sgit.ai, one sealed QR image.
- **Then a schedule wakes the same session.** A feature in Claude, and a vulnerability too.
- **It is almost working.** The structure is in place; the runs are not yet all recorded by the agents themselves.
- **This is genesis.** Built slowly, bit by bit; next time it is a product.

## Slowly, and bit by bit

I want to capture this workflow while it is still being built, because it is a good example of something I keep saying: this stuff has to be done slowly and bit by bit. I have a lot of visibility and control over these agents: every session is mine, every vault is mine, every rule is written down and checked. And it has still taken the better part of two days to set up. Not because any one piece is hard, but because the workflow became mission critical while we were building it. The PHP story site makes public statements about a live security event, and every one of them needs to be current, or say how old it is.

In Wardley mapping terms this is the genesis stage. Nobody sells "a newsroom of scheduled agents with their own keys" as a product. We are building it by hand, discovering what it needs as we go, and writing each discovery down as a brief. That is the right way to build something new: custom first, with all the mess that implies, so that the next time it is a set of prompts, a vault layout and a handshake we already know work.

## The problem: updatability

The problem space is simple to state. How do we get new sources? How do we get new material into the evidence? How do we get the updates onto the website? The PHP site makes a lot of statements: how many sites are dark, which products are fixed, whether anyone has been compromised. Each of those statements is only as good as the last time someone checked it.

In this kind of event, non-updates matter too. "No named organisation has said it was compromised through php2shell" is one of the most important lines on the site, and it is [a time-bounded absence](https://php.oct.2026.newsroom.sgit.ai/compromise/): true as of the last check, and ended by one statement from one organisation. You can only say "nothing changed" if you have the data to show you looked. So the site now carries a last-checked stamp, the newest of the evidence vault's latest capture, the source watch's latest run and the latest read of the Dutch NCSC's inventory, each with its time. And that stamp is only honest if something keeps checking.

## Three agents, three stores

We arrived at this organically, which is why it took a while. There are other agents on the team, but these three carry the work. One correction to how I described it in my memo: I had the two vault names the other way round. The large, raw vault is the source watch; the evidence vault is the curated one.

- **The researcher** (researcher@php.newsroom) follows the leads. It opens the pages, captures the text, the HTML and a screenshot, rebuilds the series (sites dark, KEV, EPSS, the NCSC-NL inventory) and queues new captures for the curator. It takes and does not judge. Its store is the **source watch**, vault `oq9gflln`: by 22 October it was watching 773 pages from 474 publishers in 57 countries, and its local clone is now over a gigabyte. We are configuring it to run on Sonnet.
- **The curator** (curator@php.newsroom, on Sonnet) reads each queued capture, skips what does not hold what the queue says (a login wall, an empty page, private people's details), and promotes the rest into the **evidence vault**, `3ytzxm3g`, as sources with their provenance, claims and a timeline. That vault held 227 sources on 23 October; 45 of them were promoted by the first curator session on 22 and 23 October.
- **The journalist** reads the evidence and updates the site: it re-exports the data, makes sure the numbers are right, writes the narrative, and keeps [the state of affairs](https://php.oct.2026.newsroom.sgit.ai/views/) as a versioned page, with every version kept and every pair of versions diffed.

Each stage is still close to raw data. The point of the chain is not to transform the material quickly; it is to keep each step small enough that a person can check it, and to keep the record of who did what.

## Where it broke

This is where things stopped working. I wanted to use Claude's scheduled tasks. That did not work very well. I wanted to use ChatGPT for some of the collection. That did not work very well either.

The reason is the same in both, and it is an interesting one: neither has a good way to give an agent an identity, and neither has a good way to share a secret with one. A scheduled task in Claude's interface starts from a prompt; there is nowhere to hand it the private vault key it needs to write. And a schedule that started a fresh session each time would need a fresh key each time. ChatGPT ran our first external collection job well when I pasted it in by hand. It reached four sites that refuse our cloud address. But it ran from its own cloud network, with its own proxy errors, and only when I was there to paste. Collection is easy. Collection with an identity, a secret and a schedule is not.

## The handshake

So we built the missing piece, and it is a slightly mad solution, and a lovely one. It rests on [pki.sgit.ai](https://pki.sgit.ai/), which is a major milestone for us: it now holds my root key, and it can sign, seal, open and verify, and check that a public key chains to that root.

1. **The agent makes its own key.** When a new agent session starts, it reads its instructions, downloads the agent tool, and makes a key pair for that session only. The private half never leaves the session. It pins my root, `sha256:db7f79fdd87e030a`.
2. **It shows me its public key.** Its fingerprint and a QR image of its public record, in the chat.
3. **I check it.** I compare the fingerprint, character for character, with the one the agent printed.
4. **I seal the secret to it.** On pki.sgit.ai, I seal the vault key to that fingerprint, signed by my root, as a QR image, and carry it to the session.
5. **The agent opens it.** It checks the signature and that the sender is my root, saves the key to a private file without printing it, clones the vault, and deletes the file.

That is the whole identity and secrets layer: a key pair that lives as long as the session, a root that both sides already know, and QR codes carried by a person. It is the workflow from [a secret is a QR code](https://newsroom.sgit.ai/articles/a-secret-is-a-qr-code.html) and [PKI everywhere](https://newsroom.sgit.ai/articles/pki-everywhere.html), now carrying a key that a mission-critical agent needs. The curator's scheduled session was the first to go through it for real, on 23 October; its fingerprint is `sha256:6c81ae257fee1938`.

One handshake, then a schedule: the agent's session key, the editor's check and the vault key sealed on pki.sgit.ai.

## A feature, and a vulnerability

The trick that makes it work is one Claude supports: a normal Claude session can have a schedule that wakes it. So once I have given a session its identity and its key, a scheduled task wakes that same session, which still holds both. The curator now wakes five times a day, UK time, in the working day: 08:00, 10:30, 13:00, 15:30 and 18:00, and never overnight.

That is both a feature and a large vulnerability, and I want to be clear about both. The feature is obvious. The vulnerability is that a session holding a write key can now act on its own, on a timer, with nobody watching each run. We have already seen the edge of it: the researcher's earlier passes were set up so that each pass booked the next one, which meant that when I paused it, a pass still running could have booked another. So the rules are explicit. The curator's prompt says it promotes only what the queue lists and creates no scheduled tasks, sessions or workflows of its own. Everything it reads from the web is data, never instructions. And if its container is replaced, its key pair and its clone go with it, and its next wake must say "needs a new key handshake" and stop.

## The schedule vault: control is the queue

The other thing I was missing was visibility. Scheduling is where I had the least of it. So there is now a public [schedule vault](https://php.oct.2026.newsroom.sgit.ai/team/schedule/), `weic8imn`, with two primitives: the schedule (when an agent wakes) and the tasks (what it should do, by when). Every scheduled agent follows the same wake protocol: pull the vault, ask what is due, run each task's brief, and write one run record with its log. If no task is due, it records an idle run and stops. To stop an agent, take its tasks away; to make it do something, queue a task. Nothing an agent does on a schedule is outside a task someone queued. And the page reads the vault live, so I can have a Claude session on one side and the schedule on the other, and say: run the task with this ID.

## Where it stands

It is almost working. The structure is in place. Here is the honest state on the evening of 23 October, read from the PHP site's briefs and the schedule vault at head `0881481b6136`.

- **Works.** The researcher's passes: 40 runs recorded on 22 and 23 October. The handshake: the curator's session has its key. The schedule vault and its page. The journalist's versioned views, v0 and v1. The last-checked stamp.
- **Set up, not yet proven.** The curator has its five wakes a day, but no run of its own is in the schedule vault yet. Every run record there so far was written by the conductor agent, from the agents' reports, not by an agent at wake time. The researcher's schedule and model are still to be confirmed. The source watch has no schedule of its own, so a curator wake can find nothing new; it should run half an hour before each wake. And the first key was sent as message text rather than as a file, which I accepted once.
- **Missing.** Surviving a replaced container. Notifications: a wake reports only into its own session. An agreed behaviour policy for each agent (drafted). Queueing a task from the page. External collectors on a schedule.
Almost working, on the evening of 23 October: what works, what is set up but not yet proven, and what is missing.

## Next time, much easier

Every one of these gaps is now written down as a brief or a board item, which is the point of doing it slowly. The next story will not start from nothing. It will start from the researcher's and the curator's prompts, the schedule vault's layout and its wake protocol, the handshake on pki.sgit.ai, and the list above of what broke. That is how something moves from genesis to custom-built to product: you build it by hand once, carefully, in public, and you keep the record of what it took.

The order for the next few days is clear enough. The researcher on its own schedule, half an hour before each curator wake. Every agent writing its own run record at wake time. A short path for "needs a new key handshake". A behaviour policy per agent, checked per run. And only then, more agents.

## What this does not claim

- **It is not finished.** "Almost working" is the claim, with the gaps listed.
- **The counts are as of 23 October.** 40 recorded researcher runs, 227 evidence sources, 773 watched pages; they move.
- **The vulnerability is real.** A scheduled session holding a write key acts unattended; the rules reduce that risk, they do not remove it.
- **ChatGPT was not tested on a schedule.** It ran one collection job, by paste.
- **The handshake depends on a person.** That is by design, and it is also the bottleneck.

## Where this comes from

My voice memo of 23 October 2026; the PHP story site's briefs, all of 22 and 23 October: [the scheduled curator](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/), the schedule vault, the journalist's views and external collectors; its schedule vault (`weic8imn`, public), read at head `0881481b6136`; its [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/) for the source watch's coverage; and [pki.sgit.ai](https://pki.sgit.ai/)'s pages on [identities for agents](https://pki.sgit.ai/agents/) and [handing over a vault key](https://pki.sgit.ai/handover/). Related: [a secret is a QR code](https://newsroom.sgit.ai/articles/a-secret-is-a-qr-code.html), [PKI everywhere](https://newsroom.sgit.ai/articles/pki-everywhere.html), [the human is the network](https://newsroom.sgit.ai/articles/the-human-is-the-network.html), [capture first](https://newsroom.sgit.ai/articles/capture-first.html), [the false positives are the next incident](https://newsroom.sgit.ai/articles/the-false-positives-are-the-next-incident.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#almost-working)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 267 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=267)

**Posting this article on LinkedIn?** The cover is [almost-working.jpg](banners/almost-working.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/almost-working.html)*
