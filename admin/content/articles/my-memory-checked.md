---
title: My memory, checked: thinking out loud in a voice memo, publishing only what the record supports, and why peer review has moved to before publishing
date: 2026-10-15
author: Dinis Cruz
author_url: about/index.html
summary: Something has changed in how I write, and I only noticed because I now take it for granted. When I record a voice memo for an article, I say things the way I remember them, in the order I remember them, with the instinct ahead of the evidence. Then the agent that writes with me goes and checks: the repositories, the commits, the briefs, the documentation, the web, and my own old writing. In the last eight articles, five of my claims were confirmed, five were corrected and two could not be found, and the articles say which. I first saw this with ChatGPT Deep Research, which launched in February 2025: eight days later, an essay I wrote with it about the O2 Platform cited three of my own blog posts from 2012, thirty-one times, as its evidence. It changes three things. Peer review used to come after publishing, from whoever on Twitter or LinkedIn noticed the mistake; now it comes before. Thinking out loud, which used to drive my teams mad as a plan moved from Monday to Friday, is now safe, because the record catches up with the instinct. And every article carries its provenance, so journalists, researchers and their agents can check it again, and rewrite it in their own voice.
version: v0.12.63
license: https://creativecommons.org/licenses/by/4.0/
tags: research, evidence, provenance, fact-checking, voice-memos, deep-research, peer-review, agents, journalism, graphs, article
status: published
---

!shot mc-ledger.webp | images/ | What I said, and what the record said: the claims from the voice memos behind the last eight articles, each confirmed, corrected or not found before publishing, and the two corrections that went the other way. | comparison

## In short {#in-short}

- **I say it as I remember it.** The agent checks it against the record before anyone reads it.
- **Five confirmed, five corrected, two not found.** In the last eight articles, and each article says which.
- **I first saw it with Deep Research.** An essay of February 2025 cited my own 2012 posts as its evidence.
- **Peer review moved before publishing.** It used to be the crowd, afterwards.
- **Thinking out loud is now safe.** The instinct can go first; the evidence follows.
- **It goes both ways.** I correct the agent too, and the checking caught a bug in our own tools.
- **Provenance for the next writer.** Journalists and their agents can check it again, and rewrite it.

## What happened with the last article {#history}

When I recorded the memo for [From sending a file to sgit](/articles/from-send-to-sgit.html), I told the history of SG/Send the way I remembered it, and partway through I noticed something: I was not worrying about getting the sequence exactly right. I knew the agent would go through the repositories, the commits and the briefs, and map what actually happened. It did. It found that I had named the vault and the data room weeks before the features that I remembered leading to them, that the move to Git's model took about two weeks and not one, that it has been eight months and not nine, and that the first feature a paying user asked for went from proposal to code in 22 minutes. Where it could not find something, such as usage figures or where the idea for the sandbox came from, it said so: my recollection, marked as such.

That is now how every article on this site is written. The table above is the record of the last eight: five claims confirmed, five corrected, two that could not be found. Cedar's place in the Cloud Native Computing Foundation, which I half-remembered, was right; the Lambda I thought served this site was wrong; the Chainguard list I thought I had seen does not exist.

## Where I first saw it {#deep-research}

The first time I noticed this was with ChatGPT Deep Research, which OpenAI released in February 2025: an agent that, in Wikipedia's words, "generates cited reports on a user-specified topic by autonomously browsing the web". I used it for many of the essays on [diniscruz.ai](https://diniscruz.ai/), which replaces docs.diniscruz.ai and keeps every essay's path. I would record a voice memo, and it would go and find evidence for what I said.

What fascinated me was where it found it. On 11 February 2025, eight days after the launch, I published an essay written with it on [O2 Platform's MethodStreams](https://diniscruz.ai/2025/02/11/o2-platforms-methodstreams-2010-open-source-sast-engine.html), a static analysis engine I built in 2010. Of its 69 links, 31 point to three pages of my own old blog, two posts from June 2012 and the O2 Platform page. On topics where little had been published, such as the early days of my work on graphs, the evidence it found was often me, talking about it years before. The essay is signed "By Dinis Cruz and ChatGPT Deep Research", which was the right thing to say then and is the right thing to say now.

## Peer review moved {#peer-review}

!shot mc-loop.webp | images/ | Peer review moved before publishing: the memo, the research, the verdicts and the article, then readers and their agents checking again from the links, and every checked article becoming evidence for the next memo. The old way, posting and waiting to be corrected, is the dashed box. | architecture

We used to get this from other people, afterwards. In the early days of Twitter, and still on LinkedIn, if you post something that is wrong, somebody usually tells you. There is even a law for it, named by Steven McGeady after Ward Cunningham: "the best way to get the right answer on the internet is not to ask a question; it's to post the wrong answer." It works, but it is slow, public and noisy, and it corrects what has already spread.

Now the first review happens before publishing, against the record rather than against the crowd. It does not replace readers. It means that what they read already has its evidence attached: every link, a section on what the article does not claim, and where it came from. As [Every link points back](/articles/every-link-points-back.html) argued, an article should also know what came next and what corrected it; and [the proof should be two clicks behind the claim](/articles/proof-behind-the-claim.html).

## Thinking out loud is now safe {#thinking}

This also solves something that used to drive my teams mad. I think fast and I think out loud. Someone would see a plan on Monday; by Wednesday it had moved; by Friday it was mature. To some people that looked as if I did not know what I was doing. A very good friend, who was very good at challenging me, used to ask: why didn't you tell me this an hour ago? And the honest answer was that I had not thought that far yet. I had an instinct about the direction, and the articulation came later.

With this workflow, the instinct can go first. I can say the half-baked version, in the order it comes to me, because the evidence catches up before anyone else has to act on it. The memo is a draft of a thought; the article is the thought, checked.

## It goes both ways {#both-ways}

The checking is not one-way, and it should not be. In the last few days I corrected the agent: it had written pioneers and settlers for Simon Wardley's stages, and the names to use now are explorers, villagers and town planners. And the same habit of recomputing everything caught a bug in our own tools: while building [the tokens hook](/articles/the-tokens-hook.html), the agent found that this session's own status report had been counting each model response two or three times, and fixed it. I still read and validate every article; if something in it is not right, I say so, and it changes. And I learn from them: the references it finds are often ones I half-remembered from a book or a talk, and now I know exactly where they are.

## Provenance for the next writer {#provenance}

I think a lot of what I write here should be rewritten by journalists, by researchers, by people who will put their own angle on it. What I can give them is the body of work and its provenance: what was said, what it rests on, what was corrected, and what is still only my recollection. Their agents should do the same thing on the other side: follow the links, check the claims, and disagree where the evidence says so.

It is, in the end, a graph. Every checked article is a node with edges to its sources, and to the articles before it. The more is published this way, the more the next claim can be checked against, and the better the agent gets at finding the right evidence for the way I think. [How much of this did I write?](/articles/how-much-of-this-did-i-write.html) counted the record this draws on; [Fractal Semantic Graphs](/articles/introducing-fractal-semantic-graphs.html) is the shape it is growing into.

## What this does not claim {#limits}

- **The agent can be wrong too.** Checking reduces errors; it does not remove them, which is why I still review.
- **Not found is not false.** It means the evidence was not found, and the article says so.
- **The tally is small.** Fourteen claims across eight articles, not a study.
- **The Deep Research recollection is partly mine.** The O2 essay and its links are checkable; the wider memory of it finding my writing on graphs is not counted here.

If you want to check something on this site, or rewrite it in your own voice, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The ledger is from this site's releases v0.12.53 to v0.12.62 and the articles they published. Wikipedia, [ChatGPT Deep Research](https://en.wikipedia.org/wiki/ChatGPT_Deep_Research); [diniscruz.ai](https://diniscruz.ai/) and its essay [O2 Platform's MethodStreams](https://diniscruz.ai/2025/02/11/o2-platforms-methodstreams-2010-open-source-sast-engine.html), whose links were counted on 15 October 2026; Meta-Wiki, [Cunningham's Law](https://meta.wikimedia.org/wiki/Cunningham's_Law).
