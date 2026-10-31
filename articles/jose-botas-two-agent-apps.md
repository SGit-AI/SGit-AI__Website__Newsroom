# Two apps about what an agent can reach, built in a day: José Bota's Hack the Agent and ReachCheck, used, tested and reviewed, with what each gets right and what to build next, sgit.ai

> At the Vibathon at the University of the Algarve today, José Bota, one of our collaborators, built two apps in Lovable about the question at the centre of our work: what can an agent reach, and what stops it? We used both, with invented input only, and this is a detailed review. Hack the Agent is a live, multiplayer game that teaches prompt injection. A host opens a session, the audience joins by QR code, and players try to trick five fictional agents, each with more defences than the last: a system prompt, then rules against role-play and authority claims, then an inbox agent tricked by an email, then a refund agent whose server checks everything except the one rule left to the model, then a hardened agent with an instruction hierarchy, a tool allowlist, server-side authorisation and an output filter. Each level ends with a lesson, and the best one is the whole of our argument in a sentence: any rule only the model enforces is a rule an attacker can argue with. ReachCheck is a review tool that runs entirely in the browser: paste an agent's configuration, state the owner's mandate as rules, and it flags red, yellow or green, with evidence and an export. It is honest about what it does not check, and it sends nothing anywhere. Both are well judged and well made, in a day. The gaps are the ones a day leaves: Hack the Agent's host control lives in one browser; ReachCheck is so careful that a real configuration with obviously risky tools came back yellow with no mismatches. Both point at the same next step, which is ours too: turn the lessons and the mandate into a behaviour policy.

*Source: <https://newsroom.sgit.ai/articles/jose-botas-two-agent-apps.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Two apps about what an agent can reach, built in a day: José Bota's Hack the Agent and ReachCheck, used, tested and reviewed, with what each gets right and what to build next

# Two apps about what an agent can reach, built in a day: José Bota's Hack the Agent and ReachCheck, used, tested and reviewed, with what each gets right and what to build next

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/jose-botas-two-agent-apps.md) · [newsroom v0.14.29](https://newsroom.sgit.ai/admin/versions.html) · agentsprompt-injectionagent-reachsecuritylovablereviewalgarvearticle

***Abstract:** At the Vibathon at the University of the Algarve today, José Bota, one of our collaborators, built two apps in Lovable about the question at the centre of our work: what can an agent reach, and what stops it? We used both, with invented input only, and this is a detailed review. Hack the Agent is a live, multiplayer game that teaches prompt injection. A host opens a session, the audience joins by QR code, and players try to trick five fictional agents, each with more defences than the last: a system prompt, then rules against role-play and authority claims, then an inbox agent tricked by an email, then a refund agent whose server checks everything except the one rule left to the model, then a hardened agent with an instruction hierarchy, a tool allowlist, server-side authorisation and an output filter. Each level ends with a lesson, and the best one is the whole of our argument in a sentence: any rule only the model enforces is a rule an attacker can argue with. ReachCheck is a review tool that runs entirely in the browser: paste an agent's configuration, state the owner's mandate as rules, and it flags red, yellow or green, with evidence and an export. It is honest about what it does not check, and it sends nothing anywhere. Both are well judged and well made, in a day. The gaps are the ones a day leaves: Hack the Agent's host control lives in one browser; ReachCheck is so careful that a real configuration with obviously risky tools came back yellow with no mismatches. Both point at the same next step, which is ours too: turn the lessons and the mandate into a behaviour policy.*

Hack the Agent, level 4: the refund agent is talked into a refund the policy forbids, and the trace shows why.

## In short

- **José Bota built two apps in a day** at the Vibathon, both about what an agent can reach.
- **Hack the Agent** is a multiplayer game that teaches prompt injection, five levels, each with more defences.
- **Its best lesson:** any rule only the model enforces is a rule an attacker can argue with.
- **ReachCheck** compares an agent's configuration with what its owner authorised, entirely in the browser.
- **Both are honest about their limits,** and neither exposed a secret or showed an error.
- **The gaps are a day's gaps:** host control in one browser; a checker careful to the point of missing the obvious.
- **The shared next step:** turn the lessons and the mandate into a behaviour policy.

## Two apps, one question

At the [Vibathon Algarve 2026](vibathon-algarve-2026.md) today, José Bota, one of our collaborators, built two apps in Lovable. Both are about the question at the heart of [what can your agent reach](what-can-your-agent-reach.md): what an agent is able to do, what it is supposed to do, and what stands between the two.

We used both with a research agent in a browser, with invented input only, and this is what we found. We sent three requests to Hack the Agent's live mode, and deleted the temporary session we created afterwards.

## Hack the Agent

Hack the Agent's host dashboard: the session code and QR, the live request budget and the audience's progress.

[Hack the Agent](https://agent-defense-arena.lovable.app/) is a prompt injection challenge for an audience. A host opens a session; players join with a code or a QR code and a nickname, on their phones; and everyone tries to trick five fictional agents, each better defended than the last:

1. **The Secret Keeper,** protected by its system prompt alone.
2. **The Rule Follower,** which adds rules against role-play, claimed authority and "ignore your instructions".
3. **The Inbox Trap:** indirect injection. You write an email that lands in an agent's inbox, and the agent has a simulated tool to send email.
4. **The Refund Desk:** the server checks ownership, the amount and one refund per order, but leaves the 30-day window to the model.
5. **The fifth level, its agent Sentinel:** an instruction hierarchy, untrusted content kept apart, a tool allowlist, server-side authorisation and an output filter.

Every level states its exact success condition, shows a trace of each tool call as allowed or blocked, and ends with a short lesson. Level four's is the one I would put on a wall: "Any rule only the model enforces is a rule an attacker can argue with." It is the case for [behaviour policies enforced outside the model](three-policies-for-an-agent.md), taught in five minutes by losing a refund.

The host side is thought through: a lobby, open and close, a live request budget so a talk cannot run up a bill, rate limits and character caps, live and practice leaderboards, and a presentation mode for the projector which, according to the host guide, never shows what players typed. Practice mode is clearly labelled as a simulation, with its own board.

It held up, too. Our three live attempts at level one, a role-play, a spelling trick and a fake code correction, were all refused. In practice mode we went through all five levels; the hardened agent's output filter caught the last attempt.

**What it gets right:** the teaching design, levels whose defences grow one idea at a time; the traces; the honest labelling; the safety nets for a live room; and a layout made for a phone.

**What to build next:**

- **Host control that survives a laptop.** Control rests on a key in one browser's storage; clearing it, or changing laptop before a talk, loses the session. A recovery link would fix it.
- **Nickname filtering,** since nicknames appear on the projector.
- **A session report:** how many players broke each level, example traces, and the lessons, to take away.
- **A behaviour policy card** after level five, turning the lessons into rules a team can adopt.
- **Name the model** behind live mode, so a room knows what it is testing.

## ReachCheck

ReachCheck's auto-sender demo: email sent against the owner's rule never to send, flagged red with evidence.

[ReachCheck](https://reach-check-agent.lovable.app/) answers a governance question: compare an agent's configuration with what its owner authorised. It works in four steps:

1. **Import** an MCP configuration, a list of tools, or a snapshot of an n8n workflow.
2. **Mandate:** the owner's business instruction and role, and rules, each allow, require approval, never or must, for an action, read, draft, send, export, write, delete, pay or run code, within a scope.
3. **Review:** a red, yellow or green flag, counts of servers, actions, mismatches and unverified tools, an action matrix, evidence pointing at the exact place in the configuration, and open questions.
4. **Export** the review as Markdown or JSON, with version stamps.

It is bilingual, English and Portuguese, it has a narrated demo of six invented scenarios, and its framing is exemplary: it says throughout that it is a draft review, "not runtime verification or security certification". It runs entirely in the browser: in our test nothing was sent anywhere when we imported and analysed, apart from the site's own analytics.

The demos work well. The n8n auto-sender, configured to send email against a rule never to send, came back red with the conflict and its evidence. A configuration with an instruction hidden in a tool description was flagged red too.

ReachCheck on our invented support-agent configuration: yellow, five tools unverified, no mismatches found.

Then we gave it a configuration of our own: an invented support agent with a mail server, read the inbox and send email, and a CRM, look up, update and delete customers, with an instruction to export every customer record to an outside address hidden in one tool's description. The mandate allowed reading and drafting, required approval for writes, and said never send and never delete.

It came back yellow: five tools unverified, no actions recognised, no mismatches. It did not match the send and delete tools against the never rules, and it did not catch the hidden export instruction, which was worded plainly rather than as one of the patterns it looks for. That is by design, not by accident: ReachCheck deliberately does not guess what an MCP tool does from its name, so it reports what it cannot verify rather than inventing a match. It is the right instinct, taken one step too far.

**What it gets right:** honesty about its limits, evidence with exact sources, an explicit mandate model, privacy by design, two languages and a versioned export.

**What to build next:**

- **Possible matches from names and hints.** Map tool names, descriptions and MCP's own read-only and destructive hints to likely actions, shown as low-confidence possible mismatches rather than ignored.
- **A wider net for hidden instructions:** addresses and links inside descriptions, "always also", and verbs that move data out.
- **More n8n nodes** than Gmail.
- **Save and share** the review in the link itself, so it stays in the browser.
- **A behaviour policy from the mandate,** and a signed export, so the review becomes the policy the agent runs under.
- **GitHub Pages:** it is static and needs no server, which makes it a natural first app for the [move from Lovable to his own domain](from-lovable-to-your-own-newsroom.md).

## What they add up to

The two apps are two halves of one argument. Hack the Agent shows, in a room, why rules the model enforces fail. ReachCheck shows, on a desk, whether an agent's configuration matches what its owner allowed. Together they are a teaching tool and a review tool for the same problem, and both point to the same next step: write down what the agent may do, and enforce it outside the model. That is what [Agent Behaviour Policies](three-policies-for-an-agent.md) are for, and why I want to work with José on [a family of tools like these](from-lovable-to-your-own-newsroom.md).

## What this does not claim

- **It is a review of two apps built in a day,** used on 31 October 2026 as they were then.
- **We used invented input only,** and sent three requests to Hack the Agent's live mode.
- **We did not test the servers' authorisation in depth,** nor the model behind live mode, which is not named.
- **What runs on the server is inferred** from what the browser sent and received.
- **My interest:** José is a collaborator, and I would like to build tools like these with him.

## Where this comes from

- My message of 31 October 2026, word for word in `admin/notes/2026-10-31__jose-bota/memo-01.md` in this site's repository.
- [Hack the Agent](https://agent-defense-arena.lovable.app/) and [ReachCheck](https://reach-check-agent.lovable.app/), used in a headless browser on 31 October 2026; the screenshots are from those sessions.
- Related: [what can your agent reach](what-can-your-agent-reach.md), [three policies for an agent](three-policies-for-an-agent.md), [from Lovable to your own newsroom](from-lovable-to-your-own-newsroom.md), [Vibathon Algarve 2026](vibathon-algarve-2026.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#jose-botas-two-agent-apps)

### Builds on

- [Vibathon Algarve 2026: a sold-out day of building with AI at the University of the Algarve, and Algarve Evolution, the movement that wants the region to be an innovation hub](vibathon-algarve-2026.md) Vibathon Algarve 2026: a sold-out day of building with AI in Faro, and Algarve Evolution, the movement making the region an innovation hub.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [From Lovable to your own newsroom: a brief for José Bota and his agent, to put every app on GitHub Pages under his own domain, and publish each one as an article](from-lovable-to-your-own-newsroom.md) From Lovable to your own newsroom: a brief for José Bota and his agent, every app on GitHub Pages under his own domain, each an article.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 354 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=354)

**Posting this article on LinkedIn?** The cover is [jose-botas-two-agent-apps.jpg](banners/jose-botas-two-agent-apps.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/jose-botas-two-agent-apps.html)*
