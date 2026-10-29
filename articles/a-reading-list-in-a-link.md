# From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work, sgit.ai

> I want to send people I know, founders I mentor, potential clients, other publishers, a link that says: from Dinis, for Steve, here are the articles I think you should read, the ones worth a look, and the ones to follow. The newsroom's curation is close, but it is not personal, and the last 10 to 20% is the part that starts a conversation. This article is three things. A brief for the newsroom: a reading list in a link, with the names and the article numbers in the part of the URL the server never sees, a stable number for every article, a page that opens the list as a persona the reader can keep or remove, and a page to make a list for someone else, which is a business model of its own. A brief for the RiskMandate agent, which already keeps my contacts: choose the person, choose the articles and the reasons, build and test the link, draft the email, and let me send it. And the part I find most interesting: the loop. A feature like this crosses editorial, product, engineering, sales and the founder, which in most companies takes weeks of meetings. Here each hand-off is a written brief, each part is a session with its own repository or vault and its own gates, and the loop closes in a day. This week it closed several times, and it is worth showing how, and what it costs.

*Source: <https://newsroom.sgit.ai/articles/a-reading-list-in-a-link.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work

# From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/a-reading-list-in-a-link.md) · [sgit.ai v0.7.51](https://sgit.ai/admin/versions.md) · newsroompersonascurationreading-listbriefscrmoutreachworkflowfeedback-loopagentsproductarticle

***Abstract:** I want to send people I know, founders I mentor, potential clients, other publishers, a link that says: from Dinis, for Steve, here are the articles I think you should read, the ones worth a look, and the ones to follow. The newsroom's curation is close, but it is not personal, and the last 10 to 20% is the part that starts a conversation. This article is three things. A brief for the newsroom: a reading list in a link, with the names and the article numbers in the part of the URL the server never sees, a stable number for every article, a page that opens the list as a persona the reader can keep or remove, and a page to make a list for someone else, which is a business model of its own. A brief for the RiskMandate agent, which already keeps my contacts: choose the person, choose the articles and the reasons, build and test the link, draft the email, and let me send it. And the part I find most interesting: the loop. A feature like this crosses editorial, product, engineering, sales and the founder, which in most companies takes weeks of meetings. Here each hand-off is a written brief, each part is a session with its own repository or vault and its own gates, and the loop closes in a day. This week it closed several times, and it is worth showing how, and what it costs.*

What a reading list from one person to another could look like, opened on newsroom.sgit.ai: three articles to read, in order, one to look at, and a persona to follow. An illustrative mock of the design below; it is not built yet.

I have a long list of people I want to send the newsroom to. Founders I mentor. People I give advice to. Potential clients and users. Publishers and journalists I have been talking to about where news could go. For each of them, I know roughly what they care about, and I know which of the articles here they should read.

The newsroom already does a lot of that work. It has [personas](pay-to-keep-your-persona.md), it can [open as one of them from a link](a-link-to-a-persona.md), it builds a front page for each reader, and it is about to let readers customise more. But the curation is not personal. It is close, and it is missing the last 10 to 20%, and that last part is exactly what turns "here is a site" into the beginning of a conversation.

So I want one small feature. I want to send somebody an email with a link, and when they open it, the newsroom says: **from Dinis, for Steve, here are the articles I think you should read, here are a couple worth a look, and here is what to follow.** One article, or five, or twenty. And it does not have to be from me: anyone can make a list for someone else, which is a business model the newsroom enables almost by accident.

The feature is simple. What is interesting is everything it touches. It has to be built on the newsroom, deployed and tested, and fit the workflows already there. Then the agent that keeps my contacts has to understand it, research the person, choose the articles, and draft the email for me to send. Then the reply has to come back somewhere. That is three parts of a company and a founder, and the way they work together is the real subject of this article. So it is in three parts: two briefs, and the loop.

## In short

- **The feature: a reading list in a link.** `newsroom.sgit.ai/for/#from=Dinis&to=Steve&r=61,44,70&s=52&f=founder`. The names and the article numbers are in the fragment, the part after the `#`, which browsers do not send to the server. The page builds the list in the browser, and offers to keep it as a persona.
- **Every article gets a number.** Short, assigned once in publication order, in a public file that only ever grows. A number is never changed or reused, so a link written today still works in a year. That number is the contract between the newsroom and anyone who builds links to it.
- **Anyone can make a list.** A page on the newsroom to pick articles, type two names and copy the link. Curating for someone else is a service people already pay for; this makes it a link.
- **The RiskMandate agent uses it.** It already keeps my contacts. It chooses the person with me, researches what is public, picks the articles and writes down why, builds and tests the link, and drafts the email. Agents draft; I send.
- **Nothing tracks the reader.** The link carries two first names and some numbers, and nothing is sent anywhere when it opens. We will not know whether it was opened. The conversation starts when they reply.
- **The loop is the point.** Memo, article and briefs, feature, outreach, reply, and back: five parts of a company, and a day. This week the same loop shipped personas by link 17 hours after their brief, and corrected three articles 32 minutes after payments went live.
- **It is not free.** Parts drift out of sync, sessions run out of budget and wait, and one person still decides what goes out in their name. The loop is fast because those costs are written down, not because they are gone.

## Part one: the brief for the newsroom

*For the session that runs newsroom.sgit.ai. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Dinis decides what ships.*

### What to build

A page at `/for/` that opens a reading list from one person to another, carried entirely in the URL fragment; a stable number for every article; and a page to make a list. Nothing on a server, nothing new to deploy except files, in the same shape as everything else on the site ([No server, by design](no-server-by-design.md)).

The link, part by part. Everything after the # stays in the browser. The article numbers are the contract; the names are display text; nothing in the link should be private, because the link travels in an email.

### 1. A number for every article

- **Assign each article a number**, in the order articles were first published, starting at 1. New articles take the next number.
- **Keep the numbers in a public file**, `articles/ids.json`: `{"n": 61, "slug": "pay-after-you-read", "title": "...", "date": "2026-10-10", "teaser": "...", "topics": [...], "personas": [...]}`. It only ever grows.
- **A gate in the build**: every published article has a number; numbers are unique; a number that existed in the last release still points at the same article; a number is never reused, even if an article is withdrawn (a withdrawn article's number opens a short note saying so).
- **Show the number** small at the foot of each article ("No. 61"), and list numbers in `llms.txt`, so a person or an agent can build a list without scraping.

### 2. The page that opens a list

- **Read the fragment**, never the query string: `from`, `to`, `r` (read, in order), `s` (take a look), `f` (follow: persona slugs such as `founder`, or collections as `c:how-agents-decide`), and an optional `n` (a one-sentence note).
- **Validate everything.** Names: up to 40 characters, letters, spaces, hyphens and apostrophes, rendered with `textContent`, never as HTML. Numbers: integers that exist in `ids.json`. A list holds 1 to 50 articles. Anything malformed is dropped, and the page says what it ignored.
- **Show the list**: "For Steve, from Dinis", then each group with the article's number, title, teaser, price and reading time, in the order given.
- **Make it a persona**, the way [a link to a persona](a-link-to-a-persona.md) already does: added to the reader's personas as a visitor, named "Steve's list, from Dinis", with the read list as its reading list and its picks, active while they are on the page, and removable in one tap. "Start reading" opens the first article.
- **Say what it is not.** One line at the foot: the names are whatever the link says, and nothing about this list has been sent anywhere. A signed list, so the sender can be proved, is a later step, on the keys of [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md).
- **A way back**: an optional `e` field with the sender's own address turns on a "Reply to Dinis" button, a plain `mailto:`; without it there is no button. The reply is how the sender learns anything.
- **No fragment**: the page explains what a reading list is, shows an example, and links to the page that makes one.
- **Prices do not change.** The recipient reads at the newsroom's normal prices from their own £5 of credit. Paying for someone else's reading is a later idea, and a good one.

### 3. The page that makes a list

- `/for/make.html`: search or browse articles by title, topic and persona; tick each into "read" or "take a look", and drag to order; pick what to follow; type the two names; copy the link.
- **It runs in the browser** and sends nothing. It is the same tool for me, for the RiskMandate agent, and for any reader who wants to curate for a friend, a team or a client.

### 4. How to know it works

- **Parser tests**: valid links, every malformed field, oversized lists, names with markup in them, unknown numbers.
- **The build gate** on numbers, run on every release.
- **A synthetic recipient**: run the [synthetic-user](how-to-run-synthetic-users.md) method with one persona, a founder called Steve who has just received the link by email, on a phone and on a laptop. Do they understand who it is from, why, and what to do next? Do they find "remove"?
- **Acceptance**: the example link in this brief opens on the live site, on a phone and a desktop, with no page errors; the list becomes a visitor persona; removing it leaves the reader's own personas untouched; and the make page produces a link that opens the same list.

### 5. What not to build

No accounts. No server endpoint. No open tracking, pixels or link shorteners that count clicks. No storage of who sent what to whom, anywhere. Nothing in the link that would embarrass anyone if the email were forwarded.

## Part two: the brief for the RiskMandate agent

*For the RiskMandate agent that keeps Dinis's contacts. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Use this once the newsroom's `/for/` page is live; until then, build the lists and keep them as drafts.*

### What you are doing

Starting conversations with people Dinis knows, one person at a time, by sending them a reading list made for them. The list is the opening line; the conversation is the point.

### The steps

1. **Choose the person with Dinis.** Propose names from the contacts you keep, with one line each on why now. Dinis approves who gets a list. Do not send to anyone who has asked not to hear from Dinis.
2. **Research what is public.** What they are working on, what they have written or said recently, what they would want to know next. Use public sources only, and write down where each fact came from.
3. **Choose the articles.** From `articles/ids.json`. Usually three to seven to read, in an order that tells a story; one or two to look at; a persona or collection to follow if one fits. For each article, write one line on why it is for them. The reasons stay in your records, not in the link.
4. **Build the link, and test it.** First names only. A note only if it adds something, one sentence, nothing private. Check every number exists, open the link on the live site, and check the names, the order and the persona.
5. **Draft the email in Dinis's voice.** Short and personal: why this, why now, the link, and one line each on two or three of the articles. **Draft, never send.** The draft goes through the [second reader](a-second-reader-the-agent-cannot-skip.md) before Dinis sees it, and Dinis sends it.
6. **Record it.** Who, when, which list, which articles and why, and when to follow up.
7. **Close the loop.** When they reply, record what they said, and what it tells us about the list. When something about the feature got in the way, write it up for the newsroom as a pitch or a brief. When a kind of reader keeps coming up, propose a persona for it.

### Rules

- **One person, one list, one email.** No mass sends, no sequences, no tracking.
- **Nothing private in the link.** It is a URL in an email; assume it will be forwarded.
- **Never write as Dinis without Dinis.** Every message in Dinis's name is approved and sent by Dinis.
- **Public research only**, with its source; nothing scraped from behind a login.

## Part three: the loop

This is the part I actually wanted to write about.

One feature, five parts of a company, and the loop that connects them. Each hand-off is a written brief, each part tests what it receives, and the feedback comes back the same way. The four dates are from this week.

Look at what this small feature needs. Someone has to see the need: that is me, with my contacts and my reasons. Someone has to turn it into a design that others can build from: that is this article. Someone has to build it, test it and deploy it, on a site with its own rules and its own release gates: that is the newsroom's session. Someone has to use it, with knowledge of the people and the judgement to pick the right articles: that is the RiskMandate agent, with the contacts it already keeps. And someone has to read it and reply: that is the person at the other end. Editorial, product, engineering, sales and the founder.

In most companies, that is weeks. A meeting to explain the idea, a ticket, a sprint, a review, a launch, a sales enablement session, a CRM field nobody fills in, and a quarterly review where somebody asks whether it worked. Each hand-off loses some of the intent, and the loop from "I want this" to "here it is, in use, and here is what we learned" is so long that by the time it closes, the reason for it has changed. I wrote about this in [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md): the people with the vision were always describing the software, "they were vibe coding. They just did it in an environment with a catastrophically slow loop."

Here, the loop is a day. Not because anybody is working harder, but because of how the parts are connected.

- **Every hand-off is written down.** A voice memo becomes an article; the article contains the briefs; each brief says what to build, how to know it works, and what not to do. It is public, versioned and dated, so each part can act on it without a meeting, and anyone can see what was asked.
- **Each part owns its own place.** This site, the newsroom, the RiskMandate agent and its contacts each have their own repository or vault, their own rules and their own gates. Nobody edits anybody else's work; they hand it a brief.
- **The contracts are small and explicit.** An article number that never changes is a contract. So is a URL format, a persona slug, or a file like `ids.json`. Two parts that agree on a contract can move independently.
- **Each part tests what it receives.** The build validates; the release checks the live site; [synthetic readers](how-to-run-synthetic-users.md) try the thing before a real person does; the second reader checks a draft before it goes out in my name.
- **The feedback comes back the same way.** A reply goes into the contacts; what was hard goes back to the newsroom as a pitch; what readers did becomes the next article. The loop closes in writing, so the next turn starts from what was learned.

And this is not a plan. It is what happened this week:

- **A brief became a feature overnight.** [A link to a persona](a-link-to-a-persona.md) was published as a design at 16:57 on 10 October. At 09:53 the next morning, 17 hours later, the newsroom released v0.7.0: "links that open the newsroom as a persona", five of them, in a simpler form than the brief asked for (the personas live in the site, not yet in a vault; the newsroom's [ledger of what runs](https://newsroom.sgit.ai/shipped/index.html) says so). The simpler form was the right call, and the brief made it possible to see the difference.
- **A test found what nobody had noticed.** Five synthetic readers found that 51 of 527 figures had not survived the newsroom's move to its own domain, because one of them was reading a page where a picture should have been.
- **A fact changed, and the record followed.** Payments went live on the newsroom on 11 October; 32 minutes after this site had published an article saying they were not live yet, that article, two others and a figure said so.
- **Outside events became answers.** Satya Nadella published a post on models as insider risks on 10 October; by the next morning, a separate session had researched and drafted [two answers](the-same-argument-in-our-words.md), and this one had rewritten them in this site's voice and published them.

### What it costs

It would be dishonest to make this sound effortless.

- **The parts drift.** While I was writing the [page for publishers](../publishers/index.md), another session released two versions of this site, and the newsroom moved on as well; the page and the newsroom were briefly out of step. Working from one source of truth per thing, and checking the live site at the end of every release, keeps the drift small. It does not remove it.
- **Sessions run out.** Each session works within a budget, and when it runs out, the work waits. Today some of it is waiting for a reset, and then for a handover: the writing of articles is moving from this site's session to the newsroom's own agents, written down like everything else.
- **One person is still the router.** I decide who gets a list, what goes out in my name, and which brief goes first. That is the right place for a person, and it is also the bottleneck. The way to widen it is not to remove the person; it is to make every decision they take smaller, better prepared and quicker to check.
- **Trust in names has to be earned.** Two emails once went out [in my voice](a-second-reader-the-agent-cannot-skip.md) when they should not have. That is why this brief says, twice, that agents draft and I send.

### Why it matters

The interesting thing is not that a reading list is clever. It is that a small idea, which touches every part of how this operation works, can go from a voice memo to a working feature to a conversation with a real person in a day or two, and come back as feedback that shapes the next turn. With a loop that fast, you can afford to try things that would never survive a quarterly planning cycle, keep the ones that work, and drop the rest without regret. That is what lets a site with no team, in the usual sense, ship a newsroom with payments, personas and its own desk of agents in a few weeks.

If you run a team, a newsroom, or a company, and you want to compare how your loops work with this one, or you would like a reading list made for you, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded on 11 October 2026, asking for two briefs and an explanation of the workflow, written by this site's agent in the voice of this site. The argument and the decisions are mine, and so is the editorial responsibility. The figures were drawn for this article; the reading list page in the first figure is an illustrative mock of the design, not the built feature, and its article numbers are examples. The dates and times in the loop figure are from the git logs of this site and of the newsroom. The fragment behaviour is RFC 3986, section 3.5. Related articles: [A link to a persona](a-link-to-a-persona.md), [Pay to keep your persona](pay-to-keep-your-persona.md), [No server, by design](no-server-by-design.md), [How to run synthetic users](how-to-run-synthetic-users.md), [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md), [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md), [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md) and [The same argument, in our words](the-same-argument-in-our-words.md).

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#a-reading-list-in-a-link)

### Builds on

- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [A link to a persona: send people to the newsroom as someone, not as nobody](a-link-to-a-persona.md) Send a CISO to the newsroom as a CISO: personas kept in a vault by the newsroom's agents, opened from a link, followed or forked.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md) Incumbents and newcomers have the same AI; what separates them is how much past success each has to protect, so inertia decides which SaaS companies survive.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.

### Continued by

- [A newsroom for one: the reading list I send by email became the first page of this newsroom for the people I write to, so it now says what it is, shows what they have read, and asks for an answer](a-newsroom-for-one.md) The reading list I send by email is the first page people see of this newsroom, so it now explains itself, shows what was read, and asks for an answer.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [Brief the agent too: the people I talk to work with agents, so what I send has to reach both](brief-the-agent-too.md) The people I advise read through agents. Content needs a second package, a brief for their agent, and memory, so it reads what changed, not everything.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 74 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=74)

**Posting this article on LinkedIn?** The cover is [a-reading-list-in-a-link.jpg](banners/a-reading-list-in-a-link.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-reading-list-in-a-link.html)*
