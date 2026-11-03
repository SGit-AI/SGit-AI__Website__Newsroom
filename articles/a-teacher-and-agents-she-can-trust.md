# A teacher and agents she can trust: a brief for an independent online English teacher's site, the workflows around every lesson, an Agent Behaviour Policy for every agent, the plumbing behind it, and content made for each student, sgit.ai

> Think of an independent English teacher in Portugal who teaches adults online. She is very good at what she does: her lesson plans, her materials and her students' results are the business. Around the lessons, though, everything runs on spreadsheets, Meet and memory, and she has no time to find students, follow up, or turn a good explanation into something a student can use again. Agents can do most of that now. But give her open-ended agents that can email her students, change her calendar and invent a rule of grammar, and the first time one goes wrong she will go back to pen and paper, because at least she controls that. So this brief gives her the opposite: a site she owns, a loop around every lesson where agents draft and she decides, and an Agent Behaviour Policy for every agent, saying what it is for, what it can reach, and what holds each line. No agent can send an email; the ones that read her calendar and inbox cannot change them; every payment link comes from a key that cannot refund. Then the part that makes it worth doing: with the plumbing handled, she can be as creative as she likes, publishing every good explanation as a lesson page that earns, and building practice that fits each student's goal and level, guided by what learning research supports. A worked example, English with Inês, is in a vault.

*Source: <https://newsroom.sgit.ai/articles/a-teacher-and-agents-she-can-trust.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A teacher and agents she can trust: a brief for an independent online English teacher's site, the workflows around every lesson, an Agent Behaviour Policy for every agent, the plumbing behind it, and content made for each student

# A teacher and agents she can trust: a brief for an independent online English teacher's site, the workflows around every lesson, an Agent Behaviour Policy for every agent, the plumbing behind it, and content made for each student

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-03 · [article v1.0.0](versions/a-teacher-and-agents-she-can-trust.md) · [newsroom v0.14.42](https://newsroom.sgit.ai/admin/versions.html) · educationteachersagentsbehaviour-policiesriskmandatevaultssmall-businessbriefarticle

***Abstract:** Think of an independent English teacher in Portugal who teaches adults online. She is very good at what she does: her lesson plans, her materials and her students' results are the business. Around the lessons, though, everything runs on spreadsheets, Meet and memory, and she has no time to find students, follow up, or turn a good explanation into something a student can use again. Agents can do most of that now. But give her open-ended agents that can email her students, change her calendar and invent a rule of grammar, and the first time one goes wrong she will go back to pen and paper, because at least she controls that. So this brief gives her the opposite: a site she owns, a loop around every lesson where agents draft and she decides, and an Agent Behaviour Policy for every agent, saying what it is for, what it can reach, and what holds each line. No agent can send an email; the ones that read her calendar and inbox cannot change them; every payment link comes from a key that cannot refund. Then the part that makes it worth doing: with the plumbing handled, she can be as creative as she likes, publishing every good explanation as a lesson page that earns, and building practice that fits each student's goal and level, guided by what learning research supports. A worked example, English with Inês, is in a vault.*

The loop around every lesson: agents draft, the teacher decides, the student practises.

## In short

- **A great teacher with an inefficient business:** spreadsheets, Meet, memory, no time.
- **Agents could do most of it,** and open-ended agents would send her back to pen and paper.
- **So every agent gets a policy:** what it is for, what it can reach, what it may not do, and what holds each line.
- **No agent sends email, changes her calendar or refunds a payment.** They draft; she decides.
- **The plumbing:** Workspace, Claude, GitHub, her domain, a private vault, Stripe and a reading meter.
- **The point:** time to be creative, every explanation published, practice that fits each student.
- **A worked example is in [a vault](https://dev.vault.sgraph.ai/#sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc%3A3d0fw3dl),** described in [English with Inês](inside-english-with-ines.md).

## The teacher

She teaches English online to adults in Portugal, one to one and in small groups. She is the kind of professional I meet all the time: very good at the work itself, with materials she has refined for years, lesson plans that work, and students who stay with her and send their friends. Around the lessons, though, it is all by hand. Enquiries in her inbox, bookings by message, a spreadsheet of who has paid for what, follow-ups when she remembers, and a lesson that was brilliant on Tuesday that nobody can see again on Wednesday.

It is the same shape as [the site for my brother](a-website-for-my-brother.md): someone who creates something valuable every day, and has no system to find the people who need it, or to let it keep working after the moment it was made.

## Why open-ended agents would fail her

Everything she does around the lessons can now be done, or drafted, by an agent. That is exactly the danger. Give her an agent that can read her inbox, email her students, book and move lessons, write materials and take payments, and sooner or later it will send the wrong email to the wrong student, move a lesson she did not want moved, or teach a rule of grammar that is not true. She did not build it and cannot see inside it, so the first time it goes wrong she will stop trusting it, and go back to pen and paper and plain email, because those she controls.

The answer is not fewer agents. It is agents she can trust because each one can do only what she asked, and what holds that is written down. That is what an [Agent Behaviour Policy](what-can-your-agent-reach.md) is: the mandate (what she wants), the grant (what it can reach), the delta (what it could reach that nobody asked for), and the barrier that holds each line, marked as a Boundary when something the agent cannot change enforces it, a Setting when an account can change it, and an Expectation when it is only in the instructions.

## The loop around every lesson

1. **Found.** A student finds a free lesson page, from a reel, a search or a friend.
2. **Trial booked.** They book a free trial on her Google booking page. Google runs the booking; no agent is involved.
3. **The lesson,** on Meet. Afterwards she records two minutes of voice notes: what went well, what to practise.
4. **Materials.** An agent drafts the student's practice set from the notes, and a lesson page if the explanation is new. She approves before anything is published.
5. **Follow-up.** An agent drafts the follow-up email: the summary, the practice link, the next date. She reads it and sends it.
6. **Practice.** The student practises between lessons: experiments, exercises, cards that come back when they are about to be forgotten, and a tutor that answers about that lesson only.
7. **Next lesson.** Before it, she sees the student's progress on a map of concepts and what the plan suggests next. She decides.
8. **Renewal.** When a package is nearly used, a renewal email and a payment link are drafted. She sends them.

In every step where something reaches a student, a person is between the agent and the student.

## Seven agents, seven policies

Two of the seven policies in the worked example: what each agent may do, and what holds each line.

| Agent | Mandate | What holds it |
|---|---|---|
| Tutor | Answer a student's questions about the current lesson, at their level | It sees only that lesson's text; the vault host caps the spend; it has no other tool |
| Follow-up | Draft the email after each lesson | It has no email tool at all; drafts are files she pastes and sends |
| Scheduler | Read the calendar, suggest times, spot clashes | Claude's Calendar connector reads only; students book on Google's page |
| Materials | Turn her notes into practice sets and lesson pages | It writes to a drafts branch; only she can merge to the live site |
| Pipeline | Keep each student's record and stage | Records live in an encrypted vault, never in the public repository |
| Billing | Create payment links and draft renewals | A restricted Stripe key: products and links only, no refunds |
| Weekly brief | One page every Monday: who needs her, what is due | At most three decisions, each with a recommendation; nothing decided for her |

Two facts from the platforms make these lines stronger than they look. Anthropic documents its Gmail connector as read-only: "Claude reads and searches email only; it can't create, send, or modify messages", and the Calendar one the same way. And Claude's tool settings let each tool be set to "Always allow, Needs approval, or Blocked". The design does not rely on the second, because a setting the account can change is a Setting, not a Boundary. It relies on agents that do not have the tool at all.

## The plumbing, once

Behind the scenes, in an afternoon, by us with her:

- **Google Workspace on her own domain.** Business Starter is enough: her email, her calendar and, in Google's words, "a single booking page". Reminders and payments on the booking page need a higher plan, so payments go through a link instead.
- **A Claude account** with the Calendar connector, which only reads, and Claude Code working on her repository and her private vault.
- **A GitHub account and the site's repository,** published with GitHub Pages: her site from markdown, a drafts branch for the agents, and only her merging to live. GitHub Pages is free for public repositories; GitHub's terms say it is not for running "an online business" or a site "primarily directed at either facilitating commercial transactions", which is why the payments happen on Stripe's pages, not hers.
- **Her domain,** pointing at the site, and the mail records for Workspace.
- **A private vault** for the pipeline, her notes and each student's record, encrypted, never in the public repository.
- **A practice vault** for students, like [the worked example](https://dev.vault.sgraph.ai/#sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc%3A3d0fw3dl).
- **Stripe,** with no monthly fee ("A Stripe não cobra tarifas de configuração nem mensalidades"), cards and MB WAY at 1.5% + €0.25 a payment, and a restricted key for the billing agent.
- **The reading meter** on her lesson pages, through [api.newsroom.sgit.ai](sellable-units.md).
- **A policy page per agent,** agreed with her, and the first weekly brief the Monday after.

## Paid for, three ways

- **Lessons,** in packages paid by a link: a free trial, then 5, 10 or 20 lessons.
- **Lesson pages,** by the reading meter: a few pence a page by how much was read, with the basics free, the way I described for [sellable units](sellable-units.md).
- **Everything else she can make once and sell many times:** workbooks from the lessons she already has, group courses for companies, exam preparation sets, and a licence for schools to use her materials.

## Now she can be creative

This is the reason for all of it. With the plumbing handled and the agents held, her time goes back to what she is good at, and she can try what she never had time for:

- **Every good explanation becomes a page.** When she explains the present perfect in a way that finally lands, it is published that evening, with its exercise, and it earns. It is what I do with these articles: people retain part of what I say, and a page lets them come back to it at their own pace.
- **Experiments and animations** that explain by moving: a window of time that slides past "now", a particle that fills, grows or appears. The agents build them from her description; she judges whether they teach.
- **Practice built for each student,** from their goal, their level, their pace and what they prefer to do, from the same core material: mass customisation of content, by a teacher with agents.

And it should follow what the research supports, not what is fashionable. Matching lessons to a "learning style" is not supported: Pashler and colleagues concluded in 2008 that "there is no adequate evidence base to justify incorporating learning-styles assessments into general educational practice", and a 2024 meta-analysis found the benefits "too small and too infrequent to justify". What is supported is testing yourself and spacing it out: "Testing is a powerful means of improving learning, not just assessing it", and a 2013 review rated practice testing and distributed practice of "high utility". So every student's practice is built on retrieval and spacing; what changes is the goal, the examples, the level and the format.

## A map of what she teaches

The next step is to capture her teaching as a knowledge graph: each concept, what it needs first, and which of her materials teach it. Once that exists, a student's progress is a projection of the graph: what they have mastered, what is next, and which of her pages fits them now. The worked example has a small one, thirteen concepts across three levels, and each student's path is drawn from it. It does not replace her judgement; it shows her, before each lesson, where the student is.

## She is not replaced

None of this takes the teacher out of the work. The lessons are hers, the judgement is hers, and every message to a student goes through her. What changes is that she stops being the bottleneck for everything around the lessons, and that her best work keeps working after the lesson ends. That is how one teacher reaches more students, and finds the ones who need her.

## What this does not claim

- **The teacher in the worked example is fictional;** the flows are designs, and the setup has not yet been done for a real teacher.
- **Some barriers are Expectations,** such as the tutor staying on its lesson; they are marked, not hidden.
- **Prices and plan features** were read on 3 November 2026 and change.
- **The CEFR levels** used are the standard A1 to C2; the Council of Europe's own pages did not load for checking.
- **Whether a site that sells lessons fits GitHub Pages' terms** is a judgement; payments stay on Stripe for that reason.

## Where this comes from

My brief of 3 November 2026, in this site's repository under `admin/notes/2026-11-03__teacher-site/`. Google: [appointment schedules compared](https://support.google.com/calendar/answer/16287038). Anthropic: [the Gmail connector](https://claude.com/docs/connectors/google/gmail), [the Calendar connector](https://claude.com/docs/connectors/google/calendar), [tool permissions](https://claude.com/docs/connectors/getting-started.md). [Stripe pricing in Portugal](https://stripe.com/pt/pricing). GitHub: [plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) and [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). [Pashler et al. 2008](https://pubmed.ncbi.nlm.nih.gov/26162104/), [Clinton-Lisell and Litzinger 2024](https://www.frontiersin.org/articles/10.3389/fpsyg.2024.1428732/full), [Roediger and Karpicke 2006](https://pubmed.ncbi.nlm.nih.gov/16507066/), [Dunlosky et al. 2013](https://pubmed.ncbi.nlm.nih.gov/26173288/). The worked example: `sgit clone sgit_public_read_e498d6f492ebb96e701b78d6b808e6ec29cac1a0c4fe9c86084b93f1ebf399cc:3d0fw3dl english-with-ines`. All read 3 November 2026.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#a-teacher-and-agents-she-can-trust)

### Builds on

- [English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy](inside-english-with-ines.md) English with Inês, a teacher's site as a vault app: experiments, spaced cards, a tutor bound to one lesson, a concept map and every agent's policy.
- [A website for my brother: a brief for Gabriel DaCruz's Claude, to rebuild gabrieldacruz.com on GitHub Pages and Google Workspace, interview him every day, and tell the story of a musician who will not tell it himself](a-website-for-my-brother.md) A brief for Gabriel DaCruz's Claude: his site on GitHub Pages, Google Workspace, daily interviews and a newsroom.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Sellable units: applying api.newsroom.sgit.ai to my brother's website, the reading meter on a composer's site that does not look like a newsroom, the pathways from a viewer to a buyer, and every lesson, score and master as something to sell](sellable-units.md) The newsroom's reading meter on a composer's site: sellable units, pathways to a buyer, and CC BY with a paid licence.

### Continued by

- [The shop that sells time: the padel shop's path to market, sell one and fulfil it before anything else, start with the customers who already trust you, promise late and deliver early, a few products you vouch for, and no stock until the orders make you](the-shop-that-sells-time.md) The padel shop's path to market: sell one and fulfil it, sell time and trust, promise late, few products, and no stock until orders force it.
- [English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy](inside-english-with-ines.md) English with Inês, a teacher's site as a vault app: experiments, spaced cards, a tutor bound to one lesson, a concept map and every agent's policy.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 371 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=371)

**Posting this article on LinkedIn?** The cover is [a-teacher-and-agents-she-can-trust.jpg](banners/a-teacher-and-agents-she-can-trust.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-teacher-and-agents-she-can-trust.html)*
