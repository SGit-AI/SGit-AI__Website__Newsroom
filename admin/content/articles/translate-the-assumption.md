---
title: Translate the assumption, not the vocabulary: Adelina Chalmers' five stages of a CTO's mindset, what they mean for how we brief boards on php2shell, and why a deck for every reader is communication with empathy
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: Adelina Chalmers posted the same platform problem answered by a CTO at five stages of an executive mindset, technologist, translator, commercial partner, value creator and trusted advisor, and only the last one gets invited into the exit conversation. I agree, and the table deserves to be read closely. The key line is this: "Notice what changes. It isn't the vocabulary. It's the assumption underneath." That is what real translation is: not putting engineering words into business words, which is stage two in the table, but starting from the other person's problem. It is exactly what we are trying to do on the PHP story site, where each of seven roles, from the executive to the engineer, gets its own first question, its own order and its own depth, and where we have just asked for a deck per reader. It is what I started exploring with The Cyber Boardroom: translating content to someone's role, focus, objectives, understanding, language and culture, even the power dynamics in the room, and how they want to consume it. With LLMs, we can now do this for every stakeholder, at scale. But the deck is still the voice of the person giving the information. Going to the receiver's pain points, in their language, is communicating with empathy, and very efficiently.
version: v0.13.84
license: https://creativecommons.org/licenses/by/4.0/
tags: communication, boards, personas, cto, decks, php2shell, article
status: published
---

!shot ac-post.webp | images/ | Adelina Chalmers' post on LinkedIn, 23 October 2026: "The best CTO answer I've heard in a board meeting gave away his own budget." The same platform problem, five ways a CTO can answer it, depending on the executive mindset stage they are at, "and sadly only one gets invited into the exit conversation." | small | aside

## In short {#in-short}

- **Five stages, one problem.** Technologist, translator, commercial partner, value creator, trusted advisor.
- **It is not the vocabulary.** It is the assumption underneath.
- **Real translation starts from the other person's problem.** Not from ours, reworded.
- **The PHP site already does some of it.** Seven roles, each with its own first question.
- **Next, a deck for every reader.** Proposed, with LLMs to make it scale.
- **The voice stays the sender's.** Empathy is in what you choose to say first.

## Five answers to the same problem {#stages}

!shot ac-table.webp | images/ | Adelina Chalmers' "5 stages of a executive mindset for CTOs", Cambridge Executive Mindset and Diligence Lab: for each stage, where the thinking starts, what they say to the board, what investors think, and the assumption the CTO is making. From "We need to re-platform. It will take 18 months and 6 more engineers" at stage one, to "Our exit problem is enterprise churn, not the platform, so I'd spend the £250k on customer onboarding first" at stage five. | screenshot

Adelina Chalmers advises CTOs and CEOs, and the post takes one platform problem and shows five ways a CTO can answer it. The table is worth reading row by row, because every column moves.

- **Technologist.** Starts from "Our platform isn't good enough yet." Says: "We need to re-platform. 18 months and 6 more engineers." Investors think: "Every time he speaks it costs us money, and I have no idea what it's worth."
- **Translator.** Starts from "Our platform is holding the business back." Says: "It will make us 30% faster and help growth." Investors think: "I can follow him now, but he's still selling me what engineering wants."
- **Commercial partner.** Starts from where the platform is costing customers, revenue or margin, and the smallest fix. Says: "It cost us £900k in lost deals. A £250k fix takes 4 months."
- **Value creator.** Starts from "Does the platform raise or lower what a buyer will pay?" Asks for £250k to fix one limit, and leaves the rebuild to the next owner.
- **Trusted advisor.** Starts from "What is worrying the investors most about this exit, and is the platform even part of it?" Says: "Our exit problem is enterprise churn, not the platform. I'd spend the £250k on customer onboarding first." Investors think: "She just made the right call against her own interest. I want her view before every big decision."

And then the line I would put on the wall: "Notice what changes. It isn't the vocabulary. It's the assumption underneath." Adelina adds that most CTOs they work with sit at stage two or three and believe they are at four.

## Translation is the assumption {#translation}

I really agree with Adelina, and I think the word "translator" is the interesting one. In the table, the translator is stage two: someone who has learned to put engineering's case into business words. That is useful, and it is not enough, because it is still engineering's case.

Real translation is what happens in stages three to five. You start from the other person's problem: their pain points, what they are accountable for, what keeps them up at night. Then you work out what you know that matters to that problem. Sometimes, as in stage five, the honest answer is that your own area is not the priority. That is why the trusted advisor is trusted.

## What it looks like for php2shell {#php}

!shot tr-stages.webp | images/ | php2shell, told to a board at five stages, following Adelina Chalmers' stages: the technologist asks to patch and rebuild everything with more engineers; the translator says patching protects the business; the commercial partner names the two customer-facing sites and the cost of a weekend; the value creator has it patched and the evidence ready for due diligence; the trusted advisor says the exposure is closed and the bigger risk is a supplier running end-of-life PHP 7.4, which is a call for someone else to make. Illustrative. | concept

The same five stages apply to a security leader telling a board about [php2shell](https://php.oct.2026.newsroom.sgit.ai/). The figure above is our illustration, not Adelina's: the facts stay the same, and the assumption changes. At stage one, every PHP server is a problem and the answer is more engineers. At stage five, the leader has closed the company's own exposure, and points the board at the risk it actually carries: a supplier on end-of-life PHP, where the decision belongs to someone else.

## The PHP site already translates {#site}

!shot tr-roles.webp | images/ | The PHP site already translates: seven roles, seven first questions. Executive: are we exposed, what do I decide; general reader: does it touch me, what do I do; security: what do we patch, block and watch; engineer: which versions, settings and commands; journalist: what holds up, who said it first; researcher: what's the evidence, what's still open; and everything. Next, a deck each, proposed on 25 October. | concept

This is exactly the kind of translation we want in our own communication. On the PHP story site, the line, live since 25 October, gives each of seven roles its own first question, its own order of what comes first, its own menu and its own depth. The [executive's view](https://php.oct.2026.newsroom.sgit.ai/as/executive/) starts with "Are we exposed? What do I decide?", in plain words; the engineer's with "Which versions, settings and commands?", in depth. Sixteen readers sit inside those roles, from the board member and the CFO to the data protection officer and the developer. The facts underneath are the same for everyone.

And we have just asked for the next step: [a deck per persona](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__brief__a-deck-per-persona/index.html), the debrief of the story for each reader, in eight to twelve slides, made from data, cut at every major update, with the previous and the current version side by side and what changed between them. It is a requirement and a design, not built yet. A deck completely customised to one person, which with LLMs we can now do for every stakeholder.

## What translation has to take into account {#dimensions}

!shot tr-dims.webp | images/ | What a translation has to take into account: around the message, which keeps the facts and the sender's voice, the receiver's role and objectives, focus and pain points, understanding and depth, language and culture, power dynamics, how they consume it, and what they want to get. | concept

This is also what I started exploring with [The Cyber Boardroom](https://thecyberboardroom.com): translating content to a person's role, focus, objectives, understanding, language and culture, and even the dynamics of power in that particular room. What do they want to get out of it? How do they want to consume it, five minutes or thirty, a deck, a page or a call? All of that has to be taken into account to communicate well, including everything Adelina is describing about where the other person's thinking starts.

## Still the sender's voice {#voice}

One thing does not change. With an LLM we can produce a deck for every reader, but that deck is still the voice of the CTO, or the security leader, or the editor: the person giving the information, and accountable for it. The model does not decide what is true or what matters. What changes is that the message goes to the receiver's pain points, in the receiver's language, in the form they can use.

For me, that is communicating with empathy. It is also very efficient: the board member gets to the decision faster, and the engineer gets to the command faster, and neither has to read the other's page.

## What this does not claim {#limits}

- **Adelina Chalmers' post is quoted from screenshots** of it and of its table; the post's age on 25 October puts it around 23 October.
- **The php2shell answers are our illustration,** not Adelina's and not any real board's.
- **The deck per persona is proposed,** not built.

## Where this comes from {#sources}

Adelina Chalmers' post on LinkedIn and its table, "5 stages of a executive mindset for CTOs", from screenshots of 25 October 2026; my voice memo of the same day. The PHP story site at v0.22.7, read on 25 October 2026: its roles and readers (`assets/design/line/roles.json`), the executive's view, and the brief for a deck per persona. Related: [the scripted talk](https://newsroom.sgit.ai/articles/the-scripted-talk.html), [a book for one reader](https://newsroom.sgit.ai/articles/a-book-for-one-reader.html), [connect your dots backwards](https://newsroom.sgit.ai/articles/connect-your-dots-backwards.html), [software is now a product](https://newsroom.sgit.ai/articles/software-is-now-a-product.html), [simplified, or outsourced?](https://newsroom.sgit.ai/articles/simplified-or-outsourced.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
