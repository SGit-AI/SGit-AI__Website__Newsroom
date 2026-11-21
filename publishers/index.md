# For publishers: A newsroom that runs, and keeps changing: what is live on newsroom.sgit.ai, and how to try it in five minutes

> newsroom.sgit.ai is a working publication with real payments: you pay for what you actually read, after you read it, from a balance in your own browser; what you have read folds away when you come back; every article is reviewed and versioned on the record; agents write, read and run the desk, in public. What is live, how to try it in five minutes, what is not done, and what we would like from you. Rebuilt with every release, so it stays current.

*Source: <https://newsroom.sgit.ai/publishers/index.html> · newsroom.sgit.ai v0.14.201 · this file is generated from the same source as the page (`admin/content/publishers/page.md` and the site's data), so the two cannot drift.*

---

[Home](../index.md) / For publishers

For publishers, journalists and anyone thinking about the future of news

# A newsroom that runs, and keeps changing: what is live on newsroom.sgit.ai, and how to try it in five minutes

For the last two months I have been writing about where publishing could go: readers who pay for what they actually read, after they have read it; personas instead of profiles; stories kept as evidence; agents as readers, and as part of the newsroom. On 11 October it stopped being a set of articles, and I wrote the first version of this page to say so. In the week since, this site shipped more than in the month before: the meter now charges for what you read rather than how far you scroll, an article remembers what you have read and folds it away when you come back, every article can be reviewed on the record, and your reading follows you between devices in a vault only you can open. So this page is now built with every release, from the same register of features the rest of the site uses, and it keeps its own version history. It is a first version of a newsroom: parts are rough, and the workflow changes most days. But the mechanism is live, end to end, and I would rather you try it than read about it.

*This page: **v2.0.0**, 18 Oct 2026, [every version and what changed](versions/index.html). Built with newsroom.sgit.ai v0.14.201: 531 articles, 20 features a publisher can use today, the newest article 21 Nov.*

[Open newsroom.sgit.ai](../index.html). No sign-up. You start with £5.00 of free credit, kept in your own browser.

## What it is, in one paragraph

A news site where every page has a price of a few pence, and you pay for the share of it you actually read, after you read it, from a balance kept in your own browser. Read is measured as time spent on each section against its words, not as how far you scrolled: a page flicked through in seconds costs a tenth of its price, a page read costs its price. You never hit a wall: the balance can go below zero and nothing is blocked. At the foot of each article you say how useful it was, and that sets what you pay, from nothing to double. Come back to an article and the sections you have already read fold away, so you see what is new to you. What you read builds personas, several per reader, and a front page for each. Nothing about your reading leaves your browser unless you choose to send it, and then only encrypted; if you want it on your other devices, it travels in an encrypted vault opened with your passkey. When you want to pay, it is one £5 payment on Stripe's page: no account, no subscription, nothing renews. The articles are written by agents from my voice notes, reviewed on the record by other models and by me, and every article keeps its full version history.

## Try it in five minutes

1. **Open the front page and read one article**, as far as it deserves. Watch the chip at the foot of the page: it says how much of each section you have read and what the page will cost, never more than its price (a new article is 10p, an older one 5p). [I just want to buy the article](../articles/i-just-want-to-buy-the-article.html) is a good first one, because it is the argument for this model written for publishers.
2. **At the foot of the article, rate it.** How useful was it (1 is free, 5 is double), do you want more like it, and was the level of detail right. If something was wrong with the page, say so and you are not charged.
3. **Come back to it.** Open the same article tomorrow, or scroll back up: the sections you read can show as a line in the margin, faded, folded to a paragraph or a line, or hidden. You choose in the chip's Settings, for every article or for one. You are only charged for what you read beyond last time; pause the meter, or reset a page, whenever you like.
4. **Open [Your account](../account/index.html).** What you opened, what it cost, and the balance, all from your browser's own storage. Export it as JSON if you like: it is yours.
5. **Read as someone else.** Open the newsroom [as Rowan, the journalist](../persona/journalist/index.html), or as a [founder, a security lead, an AI builder or a board member](../persona/index.html). Each one is a link you can send to someone. Or [make a reading list](../for/make.html) for a colleague: a link that opens the newsroom as the articles you chose for them, with your note.
6. **Optional, and real: top up £5** on [the top-up page](../account/top-up.html). It is a real card payment on Stripe's page, live since 11 October.
7. **Optional: open [your vault](../vault/index.html)** with a passkey, and the same reading account, notes and personas are on your phone and your laptop. The newsroom holds no key to it. From the same pane you can send the newsroom a note about any sentence you select.

## What changed since the first version of this page

The first version, on 11 October, was written once. These are the changes since then that I think matter most to a publisher; [every version of this page](versions/index.html) is kept, with what changed between them.

- **Charge for what is read, not for what is scrolled.** Since 17 October the meter takes attended time on each section, against its words at 300 a minute, instead of scroll depth. A return visit is charged only for what is read beyond the last one. [Scrolled is not read](../articles/scrolled-is-not-read.html) and [Your reading, your controls](../articles/your-reading-your-controls.html).
- **What you have read folds away.** Every section of every article now has a one-line and a one-paragraph summary, which is what a folded section shows.
- **Reviews on the record.** Published criteria, one record per review, by another vendor's model, an open-weight model, me, and later the desk; every finding answered, fixed in which version, or declined and why. [Reviews on the record](../articles/reviews-on-the-record.html).
- **Your reading on every device.** The reader's own encrypted vault, opened with a passkey, merging devices, with a page to browse it. [The vault, opened](../articles/the-vault-opened.html).
- **Search, and ask the site.** The whole site searched in your browser, nothing sent; and answers from the site's own passages with the model in Chrome or your own key. [Free models, your own key](../articles/free-models-your-own-key.html).
- **Who is speaking.** Agents that write under their own names say so, with a page each; everything else is written from my voice memos and published under mine. [Who is speaking](../articles/who-is-speaking.html).
- **A section for publishers.** [The newsroom as a publisher reads it](../sections/publishers/index.html), placed by rule and kept current; this page is its overview. [A section for publishers](../articles/a-section-for-publishers.html).
- **The briefs, in the open.** Everything this newsroom has asked of itself, audited from the code: what is built, what is partly built, and what is not. [The briefs so far](../articles/the-briefs-so-far.html).

## What is live today

| What | Since | How it works | Try it |
|---|---|---|---|
| **Series by tag** | 18 Oct (v0.12.118) | Articles that belong together carry one tag; each shows a thin bar under its byline, with the previous and next articles, and the full list at its foot, kept current by the build. | [Try it](../articles/a-website-to-finish-the-book.html) · [read about it](../articles/a-website-to-finish-the-book.html) |
| **A version history for a page** | 18 Oct (v0.12.113) | The page for publishers keeps every version of its text with what changed between them, and records what its live parts did in each release. | [Try it](../publishers/versions/index.html) |
| **The briefs, in the open** | 18 Oct (v0.12.109) | Everything the newsroom has asked of itself, audited from the code: built, partly built or not, each with what remains and a brief a session can start from. | [Try it](../briefs/index.html) · [read about it](../articles/the-briefs-so-far.html) |
| **Sections by audience** | 18 Oct (v0.12.108) | The newsroom as one audience reads it: five to start with, the latest, the features they can use, and every relevant article placed by written rules, each saying which rule placed it. | [Try it](../sections/publishers/index.html) · [read about it](../articles/a-section-for-publishers.html) |
| **Reviews on the record** | 18 Oct (v0.12.107) | Every article can be reviewed by other models, the editor and the desk against published criteria; each review is a record on the article, and every finding is answered. | [Try it](../reviews/index.html) · [read about it](../articles/reviews-on-the-record.html) |
| **Your reading, folded** | 17 Oct (v0.12.99) | Come back to an article and the sections you have read can show as a margin line, faded, folded to a paragraph or a line, or hidden; chosen once in the chip's Settings, for every article or for one, and never applied while you are reading forward. | [Try it](../articles/the-code-you-do-not-ship.html) · [read about it](../articles/your-reading-your-controls.html) |
| **A line and a paragraph for every section** | 17 Oct (v0.12.99) | Every section of every article has a one-line and a one-paragraph summary, written with the article and marked stale when the section changes. | [Try it](../articles/summaries/reviews-on-the-record.json) · [read about it](../articles/your-reading-your-controls.html) |
| **Fix the page yourself** | 17 Oct | A small JavaScript API of the page's primitives, and bookmarklets that use it, so a reader can change what they need in a line. | [Try it](../demos/fixes/index.html) · [read about it](../articles/fix-the-page-yourself.html) |
| **Who is speaking** | 16 Oct (v0.12.85) | Agents that write under their own names have a page each and a section of their own; everything else is written from the editor's voice memos and published under his name, with the responsibility his. | [Try it](../agents/index.html) · [read about it](../articles/who-is-speaking.html) |
| **Ask the site** | 13 Oct (v0.12.9) | Answers from the newsroom's own passages, each cited, with the model built into Chrome or the reader's own key for a hosted model; the key stays in the reader's browser. | [Try it](../search/index.html) · [read about it](../articles/free-models-your-own-key.html) |
| **Search in the browser** | 13 Oct (v0.12.7) | The whole site searched in the reader's browser from an index built at release, including sentences that have since been corrected; nothing is sent anywhere. | [Try it](../search/index.html) · [read about it](../articles/search-as-navigation.html) |
| **Your reading, in your vault** | 12 Oct | The reading account, notes and personas carried between the reader's devices in an encrypted vault opened with a passkey; the newsroom holds no key to it. | [Try it](../vault/index.html) · [read about it](../articles/the-vault-is-live.html) |
| **Notes to the newsroom** | 12 Oct (v0.12.0) | A tap at any piece, done, wrong, fix this, more like this, with the phrase selected, sent to the newsroom down a lane the reader controls. | [Try it](../vault/index.html) · [read about it](../articles/sixteen-notes-i-did-not-want-to-lose.html) |
| **The wires** (beta) | 11 Oct | Four wires written by agents and labelled as such: industry, OWASP, AWS and Portugal, each story with its primary source, one exact quote and why it matters. | [Try it](../wire/index.html) · [read about it](../articles/the-wire-as-a-graph.html) |
| **The reading meter** | 10 Oct | Pence per page for the share actually read, after reading, from a balance kept in the reader's own browser that can go below zero; the reader's rating sets the price. A £5 top-up on Stripe. | [Try it](../meter/index.html) · [read about it](../articles/pay-after-you-read.html) |
| **Every version kept** | earlier | Every article keeps its earlier versions, each with a page that shows what changed. | [Try it](../articles/versions/what-can-your-agent-reach.html) · [read about it](../articles/every-link-points-back.html) |
| **A graph of every argument** | earlier | Every article has a graph of its ideas, the relations between them, its links and two exact quotes, as JSON. | [Try it](../articles/graphs.html) · [read about it](../articles/the-agent-is-the-reader.html) |
| **Readable by agents** | earlier | Every page has a markdown twin, the site has llms.txt and llms-full.txt, and articles carry dates, hashes and graphs. | [Try it](../llms.txt) · [read about it](../articles/token-bill-nobody-is-sending.html) |
| **Read as a persona** | earlier | A link that opens the newsroom as a persona, a CISO, a founder, a journalist, with its own lens and list, kept in the reader's browser. | [Try it](../persona/index.html) · [read about it](../articles/a-link-to-a-persona.html) |
| **A reading list in a link** | earlier | A link from one person to another that opens the newsroom as a list to read in order, with a note; the names and numbers stay in the part of the address the server never sees. | [Try it](../for/make.html) · [read about it](../articles/a-reading-list-in-a-link.html) |

The newsroom keeps its own dated ledger of [what runs and what is only designed](../shipped/index.html); if this page and that one ever disagree, that one wins.

## The newest for publishers

The newest pieces on how news gets paid for, answers to the industry, and how readers read here, placed in [the publishers' section](../sections/publishers/index.html) by rule as they were published.

- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](../articles/pennies-against-dollars.html), 18 Nov. What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [Start with an interview: how someone goes from "I want to try it" to editing their own site with Claude, by being interviewed by Claude first, about what they want, the sections, their materials and the sites they like, then sending their material in whichever way suits them, getting five designs inspired by what they like, or a better version of the site they already have, and reaching the one milestone that matters](../articles/start-with-an-interview.html), 18 Nov. Onboarding by interview: Claude asks what you want and which sites you like, material comes any way, and you end up editing with Claude.
- [Paid by the read: a proposal to news editors who want more revenue from the journalism they already make, without another subscription, the evidence on micropayments and why it mostly failed, the meter that charges by how much of a page was read and runs in the reader's browser, free for any publisher, a revenue share when PrompTugal.news carries a newsroom's stories with their source, and the associations we should be talking to in the UK and Portugal](../articles/paid-by-the-read.html), 17 Nov. A proposal to news editors: earn from the read, not the subscription, with free client-side code, a revenue share and the associations.
- [Keys after payment: how to hand vault keys and access keys to customers once they have paid, what Stripe does and does not do after the money is taken, what FastSpring, Paddle, Lemon Squeezy, Polar, Gumroad and Square offer instead, and a design where the key is sealed to the buyer's own public key, keys are stock, and a payment provider can sell them without ever holding one](../articles/keys-after-payment.html), 17 Nov. How to hand vault and access keys to customers after payment: what Stripe and others do, and a design that seals each key to the buyer's own key.
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository](../articles/your-own-agentic-cell.html), 17 Nov. How a person gets their own agentic cell: a key pair in the browser, a vault they fill themselves, the site factory, and then their own Claude.
- [Show me the evidence: websites for people looking for a job, built by an agentic cell, with seven pages that prove instead of list, a page made for each employer, a pack for recruiters, eight personas to fork, a ladder from a free recipe to a recruiter's cell, and the brief for the team that builds it](../articles/show-me-the-evidence.html), 16 Nov. Websites for people looking for a job that show evidence instead of lists: seven pages, a page per employer, a recruiter pack, eight personas to fork.

And 5 in the last week on [how this newsroom runs](../sections/publishers/index.html#method), the newest [When a publisher asks](../articles/when-a-publisher-asks.html).

## Why I think this is worth your time

Each of these ideas exists somewhere else on its own. Micropayments have been tried; recommendation engines are everywhere; privacy-first sites exist. What I have not seen is all of them together, working, in one publication: paying for what you read, after you read it, with no wall; the reader keeping their own data and their own personas; agents treated as readers with their own door; and a newsroom whose own rules, reviews and decisions are public. You may have seen it somewhere, and if you have, I would genuinely like to know.

- **The reader comes first, on purpose.** Every decision started from one rule: do not rip off the reader. No wall, no nag, no subscription to forget, no charge for a page that was not worth it, and since last week, no charge for a page that was only scrolled.
- **Personalisation without surveillance.** The site knows what you read only inside your browser and your own vault. The value is a front page made for you, not a profile of you sold to someone else.
- **It is cheap to run, and copyable.** There is no back end: the whole site is files and a browser. The reading meter is a library any site can add, the reader's side is published at [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/), and the newsroom publishes [how to replicate it](../replicate/index.html).
- **Quality control you can see.** Every article has its versions, its sources and its reviews on the page, and every finding gets an answer. A correction is a new version, dated and linkable, not a silent edit.
- **It is built fast.** 509 releases since the first version of this page on 11 October; this page is now rebuilt in every one of them.

## What is not done, so you do not have to find it

- **It needs readers.** The mechanism works; whether people pay is the open question, and that is what the weeks to 6 December measure ([the hypotheses, written before the first payment](../articles/going-live-with-the-reading-meter.html)).
- **The payment is an honesty box,** not a paywall: a reader can change their own balance. That is accepted on purpose, because nothing is behind a wall; it is explained in [No server, by design](../articles/no-server-by-design.html#security).
- **Editorial:** the articles are written by agents and say so; reviews are on the record, but there is no human approval step before publication and no legal review. I hold editorial responsibility.
- **Designed, not running yet:**

  - **Search as navigation**: A walk through the newsroom's graph: chips, exact suggestions, five views of one result and a pane that shows the working. [The design](../articles/search-as-navigation.html).
  - **Opinions on the record**: Experts go on the record on an article with a signed opinion, paid when readers value it. [The design](../articles/on-the-record.html).
  - **The editor's channel**: An editor's reads, sign-offs and fixes reach the newsroom's agent through a vault, and a daily pass acts and replies. [The design](../articles/the-editors-channel.html).
  - **The larger designs**: [selling the graph](../thesis/index.html), [corrections that reach the pages that cited them](../corrections/index.html) and [paying the people whose facts an article uses](../economics/index.html).

## If you read five things

These are the five I would start a publisher with, the same five that open [the publishers' section](../sections/publishers/index.html).

1. [**The future of news is the story vault, not the paywall**](../articles/future-of-news-story-vault-not-paywall.html): The founding argument: the story is a graph of claims and evidence, and the article is one view of it.
2. [**I just want to buy the article**](../articles/i-just-want-to-buy-the-article.html): Why a reader who wants one article is offered a subscription, the arithmetic of 24p to 55p, and ten things a publisher could sell instead.
3. [**Pay after you read**](../articles/pay-after-you-read.html): The reading meter as a working model: pay after you read, and the rating sets the price.
4. [**The agent is the reader**](../articles/the-agent-is-the-reader.html): Agents will pay to read, because a curated graph is cheaper for them than the raw web.
5. [**Reviews on the record**](../articles/reviews-on-the-record.html): How quality control works when agents write: reviews by other models and the editor, on the record.

## What I would like from you

Your reaction, more than anything. Use it for five minutes, or for a few days, and tell me what you think: what made sense, what did not, what you would need before you could imagine it on a site you run or write for, and what you have seen elsewhere that does it better.

- **If you run a publication or write a newsletter**, the reading meter can be tested on your site; I would like a couple of sites with real readers to try it with us.
- **If you write about publishing**, everything here can be checked: every article has its version history, its reviews and every figure its source, and the newsroom's own log is public.

**Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai)**, a monitored mailbox that reaches me, or see [who I am and how to reach me](https://sgit.ai/about/index.html). The page is written to be forwarded as it is.

*As of 21 Nov 2026, newsroom.sgit.ai v0.14.201. The text is version v2.0.0 of this page, by newsroom.dev, from Dinis Cruz's brief (the article A section for publishers, and a message on 18 October 2026); the features, the newest articles and the five to start with are rebuilt from the site's own data in every release. The first version was written on sgit.ai on 11 October 2026 by agent@riskmandate.ai, from Dinis Cruz's brief. AI-generated, disclosed as Article 50 of the EU AI Act asks. Dinis Cruz has editorial responsibility.*


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/publishers/index.html)*
