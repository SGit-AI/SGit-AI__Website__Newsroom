# Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen, sgit.ai

> The reading meter on sgit.ai keeps everything in the reader's browser, so anyone can cheat it: edit the balance, open a private window, or credit themselves £5 by opening the page a payment returns to with a made-up reference. This piece goes one level below "who are you protecting against". None of the people here are attackers. They are readers, from engineers who are invisible by habit to people who can barely click, with agents moving between the levels in seconds. For each kind we estimate how many there are, from published figures, what they could do to the meter and whether they will. The answer is that cheating will happen, rarely, and costs nothing that reaches the site, while the risks that will actually happen are quieter: a shared computer showing someone's reading history, a reader confused by a number, and ordinary card fraud on the payment link. Security and usability are aimed at the readers who will pay, not at the ones who never would.

*Source: <https://newsroom.sgit.ai/articles/who-will-game-the-reading-meter.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen

# Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.1.0, 2 versions](versions/who-will-game-the-reading-meter.md) · securitythreat-modellingmicropaymentslocal-firstprivacyusabilityusersagentsarticle

***Abstract:** The reading meter on sgit.ai keeps everything in the reader's browser, so anyone can cheat it: edit the balance, open a private window, or credit themselves £5 by opening the page a payment returns to with a made-up reference. This piece goes one level below "who are you protecting against". None of the people here are attackers. They are readers, from engineers who are invisible by habit to people who can barely click, with agents moving between the levels in seconds. For each kind we estimate how many there are, from published figures, what they could do to the meter and whether they will. The answer is that cheating will happen, rarely, and costs nothing that reaches the site, while the risks that will actually happen are quieter: a shared computer showing someone's reading history, a reader confused by a number, and ordinary card fraud on the payment link. Security and usability are aimed at the readers who will pay, not at the ones who never would.*

Eight kinds of reader, from invisible to barely clicking, with how many of them there are, what each could do to a meter kept in the browser, and how likely they are to bother.

## In short

- **Everything is in the reader's browser, so the reader can change anything.** Nine ways to cheat or leak are listed below. All are documented and accepted.
- **None of the people who could cheat are attackers.** This is [who are you protecting against](who-are-you-protecting-against.md) one level down: not tiers of threat, but kinds of reader, all of them non-malicious.
- **Eight kinds of reader**, from the invisible (Tor, VPNs, clean browsers, mostly engineers) to the struggling (people who can barely click), with agents able to move between levels in a single request.
- **Cheating will happen, rarely, and costs the site nothing.** Every way of cheating changes a number only the cheater sees, and takes away a payment that was never coming.
- **The risks that will actually happen are quieter:** a shared computer that shows what someone read, a reader confused or worried by a negative number, and card fraud on the Stripe link.
- **So the design is aimed at the middle of the ladder,** the readers who will weigh it up and pay, and at not frightening the bottom steps, rather than at stopping the top.

## The question one level down

[Who are you protecting against](who-are-you-protecting-against.md) argued that the first question in security is who, not how much: draw the line where the attacker is, not above it, and don't design against a nation state when you have no backups. Its ladder was of attackers, from your own mistakes to states.

A reading meter needs the same question asked about people who are not attackers at all. Nobody breaks a meter that blocks nothing to steal a page they can already read. The people who could change their balance are readers, with different skills, habits and reasons. The useful question is not "could they?" but "will they, how many of them are there, and what does it cost if they do?"

[Going live with the reading meter](going-live-with-the-reading-meter.md) sets out how it works: charged by depth, a balance allowed below zero, no blocking, a refusal with a reason, a £5 Stripe top-up credited by a page that cannot check the payment. Here is who will meet it.

## Eight kinds of reader

The figures below come from different surveys with different methods and they overlap. One person can be in several rows, and in different rows on different days. They are for sizing, not for adding up.

| # | Who | How many, roughly | What they could do to the meter | Will they? |
|---|---|---|---|---|
| 1 | **The invisible.** Engineers with VPNs, clean browsers, private windows by default, sometimes Tor | Professional developers are about 0.6% of internet users; Tor has about 3.1 to 3.3 million direct users a day | Anything: edit storage, forge the return page, never keep state at all | They will not bother to cheat. Most will never have a balance long enough to matter, because their browser forgets it |
| 2 | **Agents.** Software reading on someone's behalf | Not counted; growing | Read the markdown twin, which is not metered; or drive a browser and do anything step 1 can | They move between levels in seconds. Today they are outside the meter by design |
| 3 | **Enthusiasts and power users.** NordVPN, ad blockers, privacy-aware, not developers | VPN users, about 23% of internet users; ad blockers, about 29% | Clear site data, use privacy extensions that wipe storage on close | Some will reset without meaning to. A few will look in developer tools out of curiosity |
| 4 | **Instruction followers.** Not technical, but will follow a recipe to save money or protect privacy | Unknown, likely large | Follow a post that says "open this URL to get free credit" | The cohort where publishing the gap matters. We published it ourselves |
| 5 | **Pragmatic payers.** Want the thing, happy to pay, make their own risk assessment | The audience this is for | Pay £5 on Stripe | This is who the meter is built for |
| 6 | **Little understanding.** Use the web without a model of what it stores | Private browsing used daily by about 12% in the UK (2023) | Reset it without knowing, by using a private window | They will never cheat. They will sometimes see £5.00 again and wonder why |
| 7 | **Normal and mixed.** Most readers, most of the time | Most of the ladder | Nothing deliberate | They will read, see a number, and decide |
| 8 | **Struggling.** Can barely use a computer | In the OECD's tests, 26% of adults could not use a computer and 14% were below the lowest level | Nothing | The risk is not cheating. It is being frightened by a negative balance, or thinking they owe money |

Two of those figures say more together than apart. SlashData counted 36.5 million professional developers in early 2025, and the ITU estimated about 6.0 billion internet users in November 2025: about 0.6%, by our arithmetic. At the other end, the OECD's Survey of Adult Skills, as summarised by the Nielsen Norman Group, found that across 33 rich countries 26% of adults could not use a computer, 14% were below Level 1, 29% at Level 1, 26% at Level 2 and only 5% at Level 3, the level of a skilled user. The people who could cheat this meter with no effort are a sliver of one step; the people who could be confused by it are most of the bottom three.

## Agents change level in a single request

An agent is not a step; it is a lift. The same agent can fetch a page's markdown twin as a plain HTTP client, which no meter sees, then drive a full browser that runs the meter, then reset that browser's storage between tasks without anyone deciding to. It can follow an instruction to "get credit" at step 4 and execute it at step 1.

That is why agents are outside the meter for now, on purpose, rather than inside it badly. Reading the [markdown twin](going-live-with-the-reading-meter.md) of a page, or the newsroom's [wire](../newsroom/index.md#agents), costs nothing. Metering agents properly would be a different design: priced per question rather than per page, paid by whoever runs the agent, and argued in [a token bill nobody is sending](token-bill-nobody-is-sending.md). A browser meter that tried to charge agents would mostly charge the ones honest enough to run it.

## Nine ways to cheat or leak

| # | What a reader can do | Who can | What it costs the site | What it costs the reader |
|---|---|---|---|---|
| 1 | Edit their balance in developer tools | Steps 1 to 3, and 4 with a recipe | Nothing it would have had | Nothing |
| 2 | Open a private window or another browser and start again at £5.00 | Everyone, often by accident | Nothing | Their history and picks |
| 3 | Open the page a payment returns to with any reference, and get £5 of credit, once per reference | Steps 1 to 4 | Nothing: no money moves, and the credit is only on their screen | Nothing |
| 4 | Replay the same return URL | Anyone | Blocked once per reference; a new reference is trivial, so see 3 | None |
| 5 | Clear site data to wipe a negative balance | Steps 1 to 3 | Nothing; there was never a debt | Their history |
| 6 | Read as an agent, through the markdown twin or the wire | Agents | Unmetered by design | None |
| 7 | Read someone else's history and personas on a shared computer | Anyone with the computer | None | Privacy |
| 8 | A script injected into the site reads the history | Needs a hole in the site first | Reputation | Privacy |
| 9 | Card testing, fraud or chargebacks on the Stripe link | Ordinary payment fraud | Fees and disputes | None |

Rows 1 to 6 are the cheating. Every one of them changes a number that only the person who changed it can see, and that number unlocks nothing. The site loses only a payment that the person was, by doing it, already not going to make. That is why they are accepted, and why the return page in row 3 is deliberately unprotected: protecting it would need a server, and the only thing the server would protect is a number on the cheater's own screen. What we did do is make the payment the default route everywhere. No button leads to the free one.

## The risks that will actually happen

Ranked by how likely they are, not by how interesting.

All a reader below zero sees: a small balance in the top bar, in a warmer colour, linking to an explanation. No banner, no count, no request.

1. **Confusion at the bottom of the ladder.** A reader on step 6 to 8 sees a negative balance and thinks they owe money, or sees £5.00 again and wonders where their history went. This is the most likely problem, and it is a usability problem. That is why the balance is small and links to an explanation, why its tooltip says nothing is blocked, why nothing pops up, and why the account page says on every visit that the meter lives in this browser only. The struggling reader is protected by the meter asking nothing of them.
2. **A shared computer shows what someone read.** Row 7. A family computer or a library terminal keeps the history of whoever used it last, including the pages they declined and why. It is the only risk here that harms a reader, and the mitigations are theirs: "Start again" on the account page clears it, and a private window keeps nothing. We say so on the account page rather than pretending storage is private.
3. **Card fraud on the payment link.** Row 9. Small payment links are used to test stolen card numbers. It is the one risk that costs real money, and it is the one that is not ours to solve: Stripe's own controls handle it, and the link can be switched off in a minute. It is also H4 in the going-live article's hypotheses: a dispute that is not plain card fraud would tell us the meter has started to matter in a way we did not plan.
4. **Cheating.** Rows 1 to 6. It will happen, a few times, mostly out of curiosity and mostly by steps 1 to 3. It costs nothing that reaches us. It is last on this list because it is least worth worrying about, not because it is least likely.
5. **A script on the site reads the history.** Row 8. It needs a hole in the site first. The meter sets everything it shows as text, never as markup, and the only third-party code on this site is the in-browser Python on [the try page](https://sgit.ai/try/index.md), loaded from a pinned version. It would be a serious bug if it happened. Nothing about the meter makes it more likely.

## Aim at the readers who will pay

The mistake to avoid is the one the earlier piece warned about: drawing the line above the attacker. Here, that would mean building for step 1: a server to verify every payment, an account to hold the balance, a sign-in to keep the history. Every one of those would stop nobody on step 1, who can still not pay and still read, and every one would make the meter worse for steps 5 to 8, the readers who might pay and the readers who must not be frightened.

So the line is drawn where the readers are. For the pragmatic payer on step 5, the meter is honest and the payment is one click. For the instruction follower on step 4, the gap is published by us, next to the reason it does not matter. For steps 6 to 8, the meter is quiet, never blocks, never shames and never asks. For steps 1 to 3, it is a number they can change, and they are welcome to.

## What would change the answer

- **If the balance unlocked anything,** a page, a download, an answer from an agent, cheating would stop being free, and rows 1, 3 and 5 would need a server or a signed receipt. That is a different meter.
- **If the history synced between devices,** it would be kept in an encrypted vault whose key only the reader holds, so the site still could not read it, and row 7 would get a lock.
- **If cheating showed up where we can see,** in the Stripe dashboard, we would have learned that someone found a way to make it matter. [The anchors](going-live-with-the-reading-meter.md#the-anchors-what-we-expect-and-what-would-prove-us-wrong) say in advance what number would mean that.

The library's own version of this is [SG Meter's security model](../meter/security.md), for a site adding it.

*Written from a voice note by Dinis Cruz, who set out the ladder of readers and has editorial responsibility, by a Claude Code session working as the sgit.ai newsroom, on 10 October 2026. Sources: developers, SlashData (early 2025); internet users, ITU (November 2025); Tor, metrics.torproject.org (3 to 7 October 2026); VPN and ad-blocker use, GWI (Q2 2025, via DataReportal, a secondary source); private browsing in the UK, Statista (2023); computer skills, the OECD Survey of Adult Skills as summarised by the [Nielsen Norman Group](https://www.nngroup.com/articles/computer-skill-levels/). The ratio of developers to internet users is our own arithmetic from the first two.*

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#who-will-game-the-reading-meter)

### Builds on

- [Who are you protecting against? Draw the security line where the attacker is, not above it](who-are-you-protecting-against.md) Before deciding how secure to be, name the attacker: a six-tier ladder, an air-gapped Mac mini read against it, and eight startups drawing their line.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md) AI answer engines pay to read the web as HTML; a publisher who serves markdown, dates, hashes and a typed graph saves them tokens and should get a share.

### Continued by

- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 61 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=61)

**Posting this article on LinkedIn?** The cover is [who-will-game-the-reading-meter.jpg](banners/who-will-game-the-reading-meter.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-will-game-the-reading-meter.html)*
