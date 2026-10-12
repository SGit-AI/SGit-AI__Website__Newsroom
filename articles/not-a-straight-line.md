# Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted, sgit.ai

> Today I spent most of the day dictating voice memos and improving the workflow that turns them into articles, and I would argue I was working for RiskMandate the whole time. This is the meta-strategy behind that. Progress does not go in a straight line, so "focus on one thing only" is good advice that assumes something false. I do focus, with undivided attention, on whichever thing has the highest leverage, and that is the one with users and feedback loops. RiskMandate is where the commercial opportunity is, and its oldest technical problem, where to keep the master vault's key, had resisted six months of attempts that kept failing my simplicity test. The newsroom solved it in two days, because the newsroom had the momentum to need it. The newsroom is also solving the agentic follow-up workflows RiskMandate will need, and becoming the public example of an Agent Behaviour Policy and a licence to operate that customer work can never be. And it has a history: The Cyber Boardroom, where I learned what personas and customised output are worth and paused because it needed somewhere to keep confidential data; MyFeeds, where I built personalised feeds on semantic graphs, found the industry silent and paused again; the writing from 2025 that the newsroom now stands on. I am going back to publishers with an end-to-end example. If it does not land in 2026, I will try in 2027, and the thinking will still be there, because it is open source.

*Source: <https://newsroom.sgit.ai/articles/not-a-straight-line.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted

# Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/not-a-straight-line.md) · [sgit.ai v0.7.82](https://sgit.ai/admin/versions.md) · strategyfocusleveragestartupsnewsroomriskmandateopen-sourcefeedback-looppublishingvaultspasskeysagent-behaviour-policyarticle

***Abstract:** Today I spent most of the day dictating voice memos and improving the workflow that turns them into articles, and I would argue I was working for RiskMandate the whole time. This is the meta-strategy behind that. Progress does not go in a straight line, so "focus on one thing only" is good advice that assumes something false. I do focus, with undivided attention, on whichever thing has the highest leverage, and that is the one with users and feedback loops. RiskMandate is where the commercial opportunity is, and its oldest technical problem, where to keep the master vault's key, had resisted six months of attempts that kept failing my simplicity test. The newsroom solved it in two days, because the newsroom had the momentum to need it. The newsroom is also solving the agentic follow-up workflows RiskMandate will need, and becoming the public example of an Agent Behaviour Policy and a licence to operate that customer work can never be. And it has a history: The Cyber Boardroom, where I learned what personas and customised output are worth and paused because it needed somewhere to keep confidential data; MyFeeds, where I built personalised feeds on semantic graphs, found the industry silent and paused again; the writing from 2025 that the newsroom now stands on. I am going back to publishers with an end-to-end example. If it does not land in 2026, I will try in 2027, and the thinking will still be there, because it is open source.*

Three projects, one path that is not a straight line. The Cyber Boardroom learned what personas are worth and paused for want of a data store; MyFeeds built personalised feeds on semantic graphs and paused when the industry was silent; the writing stayed. The newsroom, where the energy is now, solved RiskMandate's master vault in two days, and is becoming its public example. Dashed boxes are next, and already unblocked.

## In short

- **Progress is not a straight line.** "Focus on one thing only" is good advice that assumes the shortest path to a goal runs through that goal. It often does not.
- **I do focus, on the place of highest leverage.** Undivided attention, on one thing at a time, chosen because it has users and feedback loops now. The [last article on this](places-of-highest-leverage.md) is the method; this one is the case.
- **The newsroom solved RiskMandate's oldest problem.** Where to keep the master vault's key had resisted six months of attempts that kept failing my simplicity test. The newsroom needed it badly enough to solve it, and solved it in two days.
- **RiskMandate did not have the momentum to need it.** Its engagements are still close to forward-deployed engineering, so handing users their vault keys works at today's volumes. My instinct, when there is not enough momentum to solve a problem, is not to solve it.
- **The newsroom is also building RiskMandate's workflows and its public example.** Agentic follow-ups, outreach, a publishing pipeline: a CRM, in effect. And an ecosystem that runs on behaviour policies in the open, which customer work can never show.
- **The thinking is never wasted.** The Cyber Boardroom and MyFeeds paused, and what they taught is in everything the newsroom does. Because it was open and written down, it was there when the moment came.

## Am I getting better?

My measure is always the same question: am I getting better? Are we discovering new things, new capabilities, and discovering them at the right altitude, the one that leads to other things? Right now I feel we are in a really good spot, and most of the energy has been going into the newsroom: the articles, the voice memos, the workflow that turns a memo into a published piece with its graph, its figures and its release. Someone looking at the commit log would say I am focused on the newsroom. I would say I am focused on RiskMandate, and the commit log is the more interesting half of the story.

RiskMandate is where most of the commercial opportunity is. It is where the interest is, and where we are starting to get good engagement. And it has a number of problems I need to solve technically for it to work at scale. So the obvious advice is: focus on that, and only that. I agree with the principle and disagree with the assumption under it, which is that things move in a straight line, and that the shortest path to solving RiskMandate's problems runs through RiskMandate.

## Six months on one problem, then two days

The clearest example is the master vault. Every user, in RiskMandate and in a lot of other places in my infrastructure, needs a vault of their own, and that vault needs a key. Where that key lives, so that the user can open their vault on any device without us holding it, has been a problem for about six months. I tried several ways to solve it. There is a trail of proofs of concept that I worked on for a while and then stopped, not because they did not work but because they did not pass the simplicity test I have learned to trust. Each one was getting too complicated, and complicated is how security designs fail.

Then, in the last couple of days, we solved it. A passkey's PRF output computes a door; the door holds the master vault's key; there is a door per path, because a phone over QR gives different bytes from the device's own passkey; and there is no server of ours in the chain. [The passkey opens the vault](the-passkey-opens-the-vault.md) is the design, corrected by a lab, and [The vault is live](the-vault-is-live.md) is the evening it went from design to a reader's vault on newsroom.sgit.ai. It was built for the newsroom. It applies everywhere else, starting with RiskMandate.

So I could argue that while I was working on the newsroom, I was working on RiskMandate. That is the non-linear sequence, and it is not an accident.

## Why the newsroom could solve it and RiskMandate could not

The rule I follow is to always follow the users, even when the user is me, and to follow the feedback loops: do the thing that gets a reaction straight away. On that rule, RiskMandate and the newsroom are in very different places.

RiskMandate's traction is real, and it is still very connected to forward-deployed engineering: a lot of the work is direct, customised, done with the customer. We have not reached the point where people serve themselves from the website. We will, and we are not there yet. That means we can get away without per-user vaults. The volumes are not large, so we give users their vault keys, which works. There is not enough momentum to solve that problem, and my instinct when there is not enough momentum is: do not solve it. A problem solved before anybody needs it is solved in the abstract, and abstract solutions are where the complexity creeps in.

The newsroom is the opposite. It has readers on every device I own, it has a reading meter, personas, an encrypted share and a pay-after-you-read model that only work if every reader has a vault that follows them. [I miss it, so it is working](i-miss-it.md) is the moment I noticed I was using it every day and it was failing me in a way I could feel. That is momentum, and momentum is what makes a hard problem solvable in two days, because every attempt gets tested by somebody who wants it to work.

## The newsroom is RiskMandate's workflow, and its example

The master vault is the clearest case, and not the only one. The newsroom has forced me to improve the agentic workflow itself: agents that follow up people, follow up threads, draft, publish, and keep a record. RiskMandate has reasons to email users and to follow them up, but not at volumes that would push the workflow to mature. The newsroom does, because it is finally something that adds value to a lot of people, and the outreach I want to do for it intersects closely with RiskMandate's audience. A very effective newsroom is, underneath, a very effective CRM and a very effective publishing workflow, which is exactly what RiskMandate needs.

And it solves a problem RiskMandate will have that I did not see coming until today. RiskMandate sells [Agent Behaviour Policies](https://riskmandate.ai/agent-behaviour-policy.html) and [licences to operate](https://riskmandate.ai/licence-to-operate.html) for agents. The hardest part of selling them is showing them in action, because as we work with customers, most of those examples cannot be shared. The ecosystem around the newsroom, this site's agents, their behaviour policy, the status report at the end of every few answers, the leak scan before every commit, the releases with their logs, is the best public example we have of a behaviour policy running in practice. [The mandate stack](the-mandate-stack.md) described it; the newsroom is where it is under real load every day. That is a nice problem to have.

## The line that runs back

The newsroom also has a history, and the history is the best evidence I have that the thinking is never wasted.

I have been interested in publishing for as long as I have been writing, which is a long time, from the books I put on [Leanpub](https://leanpub.com/secdevops) to the writing on [docs.diniscruz.ai](https://docs.diniscruz.ai/). In particular I have always cared about the idea that people should be paid for creating content. I create content; I love ideas and connecting them; I think I am good at it.

[The Cyber Boardroom](https://thecyberboardroom.com) came first. It was a GenAI platform to help boards and executives with cyber security, with an advisor called Athena, and it is where I discovered the value of customisation, of personas and of shaping the output to the person reading it. You can draw a direct line from those experiments to the personas in RiskMandate and in the newsroom today. We shipped real things. What it needed and did not have was an environment to store data: nobody wants to put confidential board material into an environment somebody else runs, and although I solved the deployment so it could run anywhere, it was a hard sell. Ironically, what The Cyber Boardroom needed is what I eventually built as sgit. That circle is closing, and as far as I can see the market is still there.

It also needed data feeds. It was open source, so I could pivot, and I did: into MyFeeds, customised data feeds, which will sound familiar. Take the news, build semantic graphs of it, and personalise it from the article all the way to the reader's persona. That is when I went deep on semantic graphs, and when I realised that language models were how graphs could scale. I built a good proof of concept, with graphs of the user and graphs of the personas. Then I took it to the industry and there was silence. Nobody I reached out to had momentum for it. I realised it needed micropayments, paying for the graph and paying the people who made the content, and the industry was not there; it is not fully there today. I was not big enough to move an industry that was not yet excited about semantic graphs, about micropayments, about paying the people who write. And I could not show it working end to end, because I did not have the technology yet, and at best the sources had RSS feeds, with licensing questions I could not answer from where I stood. So I paused it.

What stayed was the thinking. The pieces I wrote in 2025 on [monetising trust and knowledge](https://docs.diniscruz.ai/2025/02/02/monetising-trust-and-knowledge-for-news-providers.html), on [fact provenance](https://docs.diniscruz.ai/2025/02/05/the-future-of-news-building-trust-through-fact-provenance.html) and on [micro and nano payments](https://docs.diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html) are the foundations the newsroom now stands on. [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) and [Pay after you read](pay-after-you-read.md) are those pieces, built. And the company I created in Portugal for MyFeeds is being closed, because running a company with little revenue in Portugal is expensive in a way it is not in England; I am looking at Lithuania for the next one, for its digital advantages, which is a small instance of [this afternoon's argument](judo-for-small-countries.md).

## Going back, with something that works

The difference now is that it is practical. I can go back, even to people I spoke to a year ago, with an end-to-end example: content, semantic graphs, a reading meter, personas, micropayments, a vault per reader, all running, all open source. A year ago I was, in hindsight, asking them to do too much: I had an idea and a proof of concept, and they would have had to build the rest. Now the rest exists, and the feedback from the people I am reaching out to is already much better. I am about to do another, larger round of outreach to publishers and to people in the news industry.

If it works, good. If it does not, I will try again in 2027. Everything is open source; anybody can take it and run with it, and I know there is attrition even when something is free. But more importantly, I now know I do not need it to work in the news industry for the work to have been worth it, because the newsroom is already making RiskMandate better. I am solving RiskMandate's problems in a context with active energy, active development and active feedback loops, which is the thing that matters most and the thing RiskMandate on its own cannot give me yet.

## The thinking is never wasted

The last point is about why I write all this down. I do my best thinking when I am faced with a real problem, and the memos and the materials are how that thinking survives. The newsroom has already benefited from five or ten articles I wrote a year ago, articles I wrote when there was no way to build what they described. If the publisher conversations do not find momentum now, I can come back in six months and the thinking will already be done, and the intersection between the newsroom and RiskMandate will be even tighter.

That is the power of doing this in the open. I can run the experiments, leave the assets, pause without losing anything, and pick up where I left off when the moment comes. Focus, for me, is undivided attention on the place of highest leverage. It is not the same thing as working on only one product, and the difference is the whole of this article.

## What this does not claim

- **The six months and the two days are my account.** The design, the lab and the evening it went live are in the linked articles; the earlier attempts are not published.
- **RiskMandate's traction is described, not measured here.** Engagements, volumes and the move to self-service are my reading of where it is.
- **The Cyber Boardroom and MyFeeds are summarised from memory.** The links are to what is public; the proofs of concept are not all published.
- **The company move is a consideration, not a decision.** Lithuania is being looked at; nothing has been registered.
- **This is one person's method.** It works for me because I write things down and work in the open; it may not transfer to a team that does neither.

If you are in the news industry and want to see the end-to-end example, or you are building on RiskMandate and want to see a behaviour policy running in public, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, at the end of a day spent mostly on voice memos, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The passkey design and its test are in [The passkey opens the vault](the-passkey-opens-the-vault.md) and [The vault is live](the-vault-is-live.md); the method in [Places of highest leverage](places-of-highest-leverage.md); the earlier writing on news at [docs.diniscruz.ai](https://docs.diniscruz.ai/). The Cyber Boardroom is at [thecyberboardroom.com](https://thecyberboardroom.com).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#not-a-straight-line)

### Builds on

- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 95 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=95)

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/not-a-straight-line.html)*
