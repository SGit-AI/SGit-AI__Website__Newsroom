# The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why, sgit.ai

> Someone shaping a roundtable in London asked me this week for my thoughts on a question that keeps coming up: is the human in the loop a safety net or a bottleneck? Plenty of companies have agent pilots that look great, and very few trust an agent to make a real decision without someone checking every output. My answer is that a person checking every output is both, and is mostly neither: it is a bottleneck because it does not scale, and it is a weak safety net because people approve almost everything they are shown, which Anthropic measured at 93% of permission prompts. The question is not whether there is a human in the loop. It is which outputs need one, what that person is given to decide with, and what moves the line over time. Put the person where an output cannot be undone and the blast radius is large, sending an email in my name, typing a password, spending money. Everywhere else, replace the human check with controls that do not get tired: a validator, a second reader the agent cannot skip, a policy whose rows are enforced outside the model, and a record read afterwards. Make the review a quality step that fixes the source, not a sign-off. And let the record move the line: trust is built from drafts nobody had to change. This is how far I have got in production. On the day I am writing this, the newsroom shipped fourteen releases, every commit made by an agent, with nobody approving each one before it went live, while the agents that run my correspondence draft every email and send none of them: I do.

*Source: <https://newsroom.sgit.ai/articles/the-human-in-the-loop.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why

# The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-13 · [article v1.1.0, 2 versions](versions/the-human-in-the-loop.md) · [newsroom v0.12.19](https://newsroom.sgit.ai/admin/versions.html) · human-in-the-loopagentsagencyapproval-fatigueagent-behaviour-policyblast-radiusproductiontrustgovernanceroundtablearticle

***Abstract:** Someone shaping a roundtable in London asked me this week for my thoughts on a question that keeps coming up: is the human in the loop a safety net or a bottleneck? Plenty of companies have agent pilots that look great, and very few trust an agent to make a real decision without someone checking every output. My answer is that a person checking every output is both, and is mostly neither: it is a bottleneck because it does not scale, and it is a weak safety net because people approve almost everything they are shown, which Anthropic measured at 93% of permission prompts. The question is not whether there is a human in the loop. It is which outputs need one, what that person is given to decide with, and what moves the line over time. Put the person where an output cannot be undone and the blast radius is large, sending an email in my name, typing a password, spending money. Everywhere else, replace the human check with controls that do not get tired: a validator, a second reader the agent cannot skip, a policy whose rows are enforced outside the model, and a record read afterwards. Make the review a quality step that fixes the source, not a sign-off. And let the record move the line: trust is built from drafts nobody had to change. This is how far I have got in production. On the day I am writing this, the newsroom shipped fourteen releases, every commit made by an agent, with nobody approving each one before it went live, while the agents that run my correspondence draft every email and send none of them: I do.*

Where the person belongs. Two questions place every output an agent produces: can it be undone, and how much would it cost if it went wrong. The person goes where the answers are no and a lot. Everywhere else, controls that do not get tired do the checking, and the person reads the record afterwards. Examples from the newsroom and from my own agent team.

**What came next.** [The human in the loop is a spectrum](how-cheap-is-it-to-undo.md) takes the last section further: why this newsroom ships on its own while my email waits for me, and how both of those can move.

## In short

- **Checking every output is both, and mostly neither.** It is a bottleneck because it does not scale, and a weak safety net because people approve almost everything: Anthropic measured 93% of permission prompts approved.
- **The question is where, not whether.** Which outputs need a person, what that person is given to decide with, and what moves the line.
- **Put the person where it cannot be undone and the blast radius is large.** Sending in my name, typing a secret, spending money, deleting what has no backup.
- **Replace the other human checks with controls that do not get tired.** Validators, a second reader the agent cannot skip, policy rows enforced outside the model, and a record read afterwards.
- **A review should fix the source, not sign the output.** A correction that becomes a rule is worth more than a hundred approvals.
- **The record moves the line.** Trust is built from drafts nobody had to change, and the record is what lets a business give the agent more.
- **How far I have got.** Fourteen releases of this site in one day, every commit made by an agent, none approved one by one; and an agent team that drafts all my email and sends none of it.

## The question

Someone who is shaping a roundtable in London sent me a message this week. The topic that keeps coming up in their conversations is the human in the loop: safety net or bottleneck? Their observation, paraphrased, is that plenty of companies have AI pilots that look great, and very few trust an agent to make a real decision without someone checking every output. They asked what I thought, and how far I had got with AI in production. I said I had a lot of thoughts on this, and that I would put them in an article. This is it.

## Checking every output is both, and mostly neither

A person checking every output is a bottleneck, obviously. The whole point of an agent is that it does more work than a person can, and if every piece of that work waits for a person, the agent runs at the speed of the person. That is the pilot that looks great and never scales.

The less obvious part is that it is also a weak safety net. People approve almost everything they are asked to approve. Anthropic, writing about its own coding agent in March 2026, opened with the number: ["Claude Code users approve 93% of permission prompts"](https://www.anthropic.com/engineering/claude-code-auto-mode). In October 2025 it had already named the effect, ["approval fatigue"](https://www.anthropic.com/engineering/claude-code-sandboxing), where people "might not pay close attention to what they're approving", and reported that sandboxing "safely reduces permission prompts by 84%". The fix the vendor reached for was fewer prompts, not more attentive people, and I think that is right.

I wrote about the deeper problem in [Agency is not a yes](agency-is-not-a-yes.md). Most human-in-the-loop designs ask the person for a yes or a no, with little context, no time and no authority over the system that produced the request. Below a certain level on that scale, the person is not a safety net at all. They are where the liability lands for a decision the system made, and the accountability belongs to whoever designed the decision point. [Where is the why?](where-is-the-why.md) is the same argument about one permission prompt that asked me to decide and kept the reason.

So the honest answer to the roundtable's question is: checking every output gives you the cost of a bottleneck and the protection of a rubber stamp.

## The question is where, not whether

The useful question is not whether there is a human in the loop. It is which outputs need one. Two questions place every output an agent produces: can it be undone, and how much would it cost if it were wrong? That second one is what [Footprint and blast radius](footprint-and-blast-radius.md) calls the blast radius, what it would cost the business if a row of the agent's reach were used in full, today.

Where the output cannot be undone and the blast radius is large, put a person there, and make it a real decision. In my own setup, as [Replicating the agentic inbox](replicating-the-agentic-inbox.md) describes, that is sending: the agents write drafts, and I read, change and press send, because an email in my name cannot be recalled and, as I argued in [Who owns the words](who-owns-the-words.md), the responsibility for it is mine. In [the subscriptions service](stop-the-bleeding-then-ask-for-it-back.md) it is two things: the freelancer types every secret, and sends every draft. Spending money and deleting what has no backup belong in the same place.

Everywhere else, the person is the wrong control.

## Replace the other checks with controls that do not get tired

How far I have got in production, as it ran on 13 October 2026. For each kind of output, who or what checks it before it counts, and what happens afterwards. Only two rows have a person before the fact.

An article on this site is a good example, because it can be undone: a correction is a new version, with a page that shows what changed. So nobody approves an article before it goes live. What stands in the way instead is a set of controls that never get tired: a validator that fails the build on a broken link, a quote that is not word for word in its source, a banned word or a missing figure; browser tests; a leak scan on every commit that refuses a key or a name on the private list. I read every article, but I read it after it is live, and what I find becomes a new version and, if it is about wording, a rule.

For outputs that matter more, the control can be another reader. After two emails went out in my voice that should not have, the fix was [a second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md): every draft passes a separate model call that sees only the rules, the sources and the draft, and anything but an explicit pass stops it. Banks call that maker-checker. It is a check on every output, and it is not a person.

And the strongest control is the one that makes the bad output impossible. [Hope or enforcement](hope-or-enforcement.md) took one customer service agent and redesigned it three times; the share of its policy kept only by the model's good behaviour fell from 97% to 23%, and the reach of one run fell from 38,000 customer records to one customer. Every row moved from hope to a boundary is a row nobody has to check by hand. That is also the argument of [A policy beside the prompt](a-policy-beside-the-prompt.md): write the rules down, and get the platform to enforce as many of them as it can see.

## A review should fix the source, not sign the output

When a person does review, the review should be worth more than a yes. In [Agency is not a yes](agency-is-not-a-yes.md) the higher levels of the scale are where a review stops being a sign-off and becomes a quality step: each draft is a chance to fix whatever produced it, the rule, the prompt, the data, rather than the draft itself.

That is how I review this site. When a word jars, it becomes a rule in the session's behaviour policy, and I never see it again; [How the voice works](how-the-voice-works.md) counted the effect, with almost all of my corrections now about content and direction rather than words. A human in the loop who fixes the source makes the loop need them less every week. A human who approves outputs makes it need them exactly as much forever.

## The record moves the line

The last piece is what lets a business give an agent more room over time. Trust in my email agents is not a feeling; it is a record of drafts I did not have to change, the draft's hash beside the email that went out, read whenever I want. When that record says a kind of message has gone out unchanged for long enough, that kind of message is a candidate to leave the human step, by a decision written into the policy, with an owner and a date. The agent team has exactly one such exception today: a security agent may send one email, to one address, to put the team on hold. Everything else is still a draft.

The same record catches what the person would have missed. Reading the footprint afterwards against the mandate finds the near misses, the times the agent went somewhere it was not asked to go and nothing stopped it, which no approval prompt would have shown.

## How far I have got in production

So, to the second half of the question. On 13 October 2026, the day I am writing this, the newsroom shipped fourteen releases, v0.12.5 to v0.12.18. Every commit in them was made by an agent session: one writes the articles, one works on the reading experience, one runs the wire. Five articles were written and published in this repository. The four written by this session were each researched, checked against their sources, given their figures and graph, built, validated, tested and leak-scanned by an agent, and none was approved by a person before it went live. I read them afterwards, and corrected them, as new versions.

At the same time, the twelve agents that run my correspondence, [the agent team as it runs](the-agent-team-as-it-runs.md), draft every email and send none; the one exception in their policy is a security agent allowed one email, to one address, to put the team on hold. That is not a contradiction. It is the same rule applied to two different blast radii. An article can be corrected tomorrow. An email cannot.

## Questions for the roundtable

If I were in the room, these are the questions I would bring:

1. Which of your agent's outputs can be undone, and which cannot? Is the person only on the second kind?
2. What is the person shown when they approve? Could they say no, and would anybody notice if they did?
3. What share of your approvals are yes? If it is above ninety per cent, what is the check for?
4. Which of your human checks could be a validator, a second model or a boundary in the platform instead?
5. When a reviewer corrects an output, does the correction change the source, or only that output?
6. What record would let you remove a human check next quarter, and who decides?

## What this does not claim

- **The 93% is one vendor's figure for one product.** It is about permission prompts in a coding agent; other approval flows may differ.
- **My production is small.** One person, one newsroom, one agent team. The pattern is what I would defend, not the scale.
- **Some outputs need a person by law or by their nature.** Medicine, law and money moved on someone else's behalf have rules of their own; this is not an argument for removing those.
- **"Nobody approved each release" is not "nobody was responsible".** I own what the agents publish, and the controls are mine; I chose where to put myself.
- **The roundtable question is paraphrased.** It came in a private message, and its author is not named.

If you are running agent pilots and want to work out where your people belong, or you are in the roundtable and want to compare notes, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A question in a private message on 13 October 2026 from someone shaping a roundtable in London, paraphrased and not named, and my reply that I would answer it in an article. There was no voice memo: this article was assembled by this site's agent from my published positions, in the voice of this site, and the argument and the editorial responsibility are mine. Anthropic's figures: [How we built Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode), 25 March 2026, and [Beyond permission prompts](https://www.anthropic.com/engineering/claude-code-sandboxing), 20 October 2025. The production counts are from the newsroom repository's git log for 13 October 2026.

## Threads

Agents & policy[This article as a graph →](graphs.md#the-human-in-the-loop)

### Builds on

- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Who owns the words: agents can make decisions, but they cannot hold responsibility](who-owns-the-words.md) Agents in loops make real decisions, but responsibility stays with whoever granted the reach; disclosure is a label, not a team to manage.
- [Stop the bleeding, then ask for it back: a helper, an agent and a friendly letter for the subscriptions you keep and do not use](stop-the-bleeding-then-ask-for-it-back.md) A helper and an agent ask what you used, ask nicely for a pause and a refund, stop the payments either way, and publish what each company did.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [How the voice works: why these articles sound like me, with a section in which Claude explains it from its side](how-the-voice-works.md) Why these articles sound like their author: a corpus, the voice memos, seven wording rules and a reader who corrects, with Claude explaining it from its side.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.

### Continued by

- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 103 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=103)

**Posting this article on LinkedIn?** The cover is [the-human-in-the-loop.jpg](banners/the-human-in-the-loop.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-human-in-the-loop.html)*
