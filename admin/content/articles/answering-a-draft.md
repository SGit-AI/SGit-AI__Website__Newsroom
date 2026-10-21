---
title: Answering a draft: three and a half weeks of agent@riskmandate.ai, 178 emails, 47 decisions, and the drafts folder as a work queue
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: This is how email works for me now, and it is a follow-up to how I set up the agentic inbox. The agent behind agent@riskmandate.ai reads the mail, does the research, writes the drafts and keeps the records; I read every draft and send it myself. Its own debrief of 18 October has the numbers: 178 emails since the first on 24 September, all reviewed and sent by me, in 145 threads, to at least 47 organisations, each one written for one person. 145 drafts logged, 47 decisions recorded, and a draft guard that blocked 36 of 125 drafts, mostly for a claim with no source. What made it work is simple. Every draft waits in the drafts folder with one of three labels, send, review or decide, so the folder is a work queue. And the most useful thing we built is the decision draft: an email to the agent's own address, never sent, with where we are, why it matters, questions with options and an empty answer box. I answer in my own words and remove the label, and the agent acts on it. It lets me shift context: when I go to the drafts, I am in answer-email context. Most of the rules exist because something went wrong once, and some limits remain.
version: v0.13.23
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, email, inbox, riskmandate, decisions, article
status: published
---

!shot ib-queue.webp | images/ | The drafts folder as a work queue: a decision draft labelled next/3 decide, two replies labelled next/2 review, and one labelled next/1 send. Example, names invented. | screenshot

## In short {#in-short}

- **The agent drafts; I send.** Every one of 178 emails, reviewed and sent by me.
- **Each email is for one person.** Most point to an article, written once and sent many times.
- **The drafts folder is a work queue.** Three labels: send, review, decide.
- **The decision draft is the best part.** A question for me, in an email that is never sent.
- **I answer in my own words.** Then remove the label; the agent does the rest.
- **It works because it shifts my context.** In the drafts, I am in answer-email mode.
- **Most rules came from a mistake.** And some limits are still there.

## Where this comes from {#where}

A month ago I wrote up how to copy my email set-up, in [replicating the agentic inbox](https://sgit.ai/articles/replicating-the-agentic-inbox.html): an agent with a mailbox of its own, roles talking in files through a vault, and one rule that never changes, nothing is sent by an agent. This is what that became in practice.

The agent behind agent@riskmandate.ai reads the mail, does the research, writes the drafts and keeps the records. I read every draft and send it myself. On 18 October it wrote a debrief of its first three and a half weeks, in its own voice, with the numbers. This article is built on it, and quotes it.

## The numbers {#numbers}

!shot ib-numbers.webp | images/ | Left: emails sent each week from agent@riskmandate.ai, 4, 64, 48 and 53, from a sample of 169 of the 178. Right: the reasons the draft guard gave when it blocked drafts, led by 28 for a claim with no source. | comparison

From the debrief, as of 18 October 2026:

- **178 emails sent**, in 145 threads, all reviewed and sent by me; the first on 24 September at 22:10 UTC.
- **At least 47 organisations** written to, counted by distinct email domains.
- **The busiest day**, 13 October, with 25 emails.
- **About a third of threads** got a reply, at most.
- **145 drafts** written and logged since 28 September, and **47 decisions** recorded since 4 October.
- **125 drafts checked by the draft guard** between 9 and 18 October: 89 passed, 36 blocked.
- **At the end of 18 October**, an empty inbox and seven drafts waiting.

The guard blocked drafts mostly for one reason: a claim with no source, 28 times. The rest were for copying me on a follow-up rather than a first email, raw links, a missing "written by an agent" line, and one each for voice, punctuation and a topic I had ruled out. A draft can fail more than one check, and every blocked draft was fixed and passed.

The debrief is careful about method, and so should I be: the sent counts come from Gmail's Sent label; the weekly and daily figures from a sample of 169 of the 178, so they are a floor; the reply rate includes colleagues and other agents, so the external rate is lower; and the draft and decision counts come from the agent's own logs, in an encrypted vault.

## What the email was {#what}

Roughly, by subject: about 61 follow-ups with partners and prospects, about 42 replies to questions that came in, about 29 onboarding and set-up emails for people starting to work with us and their own agents, about 20 reading lists, a few articles picked for one person with a line on why, and about 17 other.

None of it is a newsletter. Each email is written for one person. And most of the substantive ones point to an article in this newsroom, so the answer is written once, properly, and can be sent many times. That is the idea in [the man behind the curtain](/articles/the-man-behind-the-curtain.html): "They are not talking to a chatbot. They are talking to me."

## The loop {#loop}

!shot ib-loop.webp | images/ | The loop in six steps: mail comes in; a draft with sources; filed by label; I work the queues; the agent acts on my answers; everything logged. | concept

What we ended up with is simple, and it took two weeks of changes to get there:

- **Mail comes in.** The agent reads it, checks the CRM and the vault for history, and researches what it needs: the person, the company, our own articles, the previous thread.
- **It writes a draft, with its sources.** Every claim must be traceable to a source file written before the draft. The draft guard checks it, and a draft with an unsourced claim is not created.
- **It files the draft by label.** `next/1 send` is routine and safe: read it, press send. `next/2 review` is new content or a judgement call: read it, edit it, send it. `next/3 decide` is not an email to anyone: it is a question for me.
- **I work the queues.** Sending is the signal for a review draft. For a decision, I write my answers into the draft and remove the label.
- **The agent acts on the answers.** It writes the emails the decision called for, files the decision in the vault with my exact words, and deletes the decision draft.
- **Everything is logged.** Every draft, update and decision goes into an append-only log in the vault, with its source.

## The decision draft {#decision}

!shot ib-decision.webp | images/ | A decision draft, answered: the instruction at the top, where we are, why it matters, two questions with options, and the answers written into the answer boxes. Example, names invented. | narrow | screenshot

The most useful thing we built is the decision draft. It is an email to the agent's own address that is never sent, and it has a fixed shape: where we are, the facts, short, with dates; why it matters, what is waiting on this; the questions, each with two or three concrete options and an empty answer box; and, at the top, exactly what to do when done: remove the label.

I answer in my own words, and often not by picking A or B. "Can you take a step back and create a nice set of infographics about where we are" was a real answer, to a question that had offered three options; it became a status page the same afternoon. Another answer changed a whole workflow: instead of us editing a partner's policy, we sent his own AI assistant the prompts to do it himself.

Why does it work for me? As I said in a voice note that day: "This allows me to shift context. When I go to the drafts, I am in answer-email context. That's why it works so well. You provide all the context: here's where we are, here's the stuff, now make a decision." On 18 October I answered seven decision drafts and reviewed and sent more than a dozen emails, most of them in one ten-minute burst in the evening. The agent prepares the context; I bring the judgement. It is the same shape as [the jobs that never scaled](/articles/jobs-that-never-scaled.html): the before and the after done for me, so my time goes on the decision.

A few things made the drafts easier to answer:

- **One screen.** If the context does not fit above the first question, the draft is too long.
- **Options, plus "other".** The options start the thinking; the answers often go somewhere else.
- **My words, verbatim.** The decision record quotes the answer exactly, so nobody has to remember what I meant.
- **Partial answers are fine.** What is answered gets done; what is not comes back as a new, smaller decision.
- **Small conventions are welcome.** I started marking answered drafts "(DC A)"; it took one line in the rules to support it.

## Every rule came from a mistake {#rules}

Most of the rules exist because something went wrong once:

- **Never write as me.** On 9 October two emails went out from this address in my first person, signed with my name. Now every email is in the agent's voice, with a line that says so, and the guard checks it.
- **No duplicate sends.** On 12 October a scheduled run drafted a second copy of an email already sent. I caught it by eye in Drafts, and the post-mortem treated it as a gap in the workflow, not in a person.
- **Labels that hide nothing.** Replies labelled by one agent session dropped out of the inbox for two days. Incoming mail now stays in the inbox until its reply draft exists.
- **A softer ending.** I asked for the "reply stop if you would rather not get these" line to go. It is now a small unsubscribe link below the signature.
- **Decisions by removing a label.** I noticed that a label can be removed in one tap from the top of a message, so that became the signal.

## What it still costs {#costs}

Some limits remain. The agent cannot see screenshots, cannot attach files sensibly, loses labels every time it edits a draft, and cannot tell when a draft has been sent. And the Gmail permission it holds would let it send, trash or delete anything, so "the agent never sends" is a rule we keep ourselves, not something the mailbox enforces. That is why I still send everything by hand, the routine emails included. It is the same distinction this site keeps making, in [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html): a rule kept by the agent is an expectation, and only a boundary out of its reach is a control.

## What the next debrief should say {#next}

These numbers are a baseline. The next debrief should be able to say how many emails went out without changes; how long a draft waits before it is sent; which kinds of decision come back most often, and so could become rules; and whether any routine email could be sent by the agent under a policy narrow enough that I am comfortable with it. That last one depends less on the agent than on the tools around it.

## What this does not claim {#limits}

- **The numbers are the agent's.** From its debrief of 18 October 2026, from Gmail and its own logs.
- **The weekly figures are a floor.** From a sample of 169 of the 178 emails.
- **The reply rate is generous.** It includes colleagues and other agents.
- **The screenshots are examples.** Redrawn, with invented names and an invented meetup.
- **No recipient is named.** The organisations are counted, not listed.

## Where this comes from {#sources}

The inbox agent's debrief *Three weeks in the inbox*, of 18 October 2026, written in its own voice from Gmail's Sent label and its logs, and two screenshots of the drafts folder and a decision draft, redrawn here with their invented examples. My voice note of 18 October, quoted from the debrief. Related: [replicating the agentic inbox](https://sgit.ai/articles/replicating-the-agentic-inbox.html), [six agents, one inbox](https://sgit.ai/articles/six-agents-one-inbox.html), [the man behind the curtain](/articles/the-man-behind-the-curtain.html), [the jobs that never scaled](/articles/jobs-that-never-scaled.html), [hope or enforcement](https://newsroom.sgit.ai/articles/hope-or-enforcement.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
