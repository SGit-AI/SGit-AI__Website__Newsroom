---
title: Would you pay to plug this newsroom in? A reply to Florent Daudens, on five publishers' bets for the AI era, from a newsroom built for agents, with what it answers, where it goes further, and the questions it has not answered either
date: 2026-11-03
author: Dinis Cruz
author_url: about/index.html
summary: Florent Daudens asked, in a post and an essay today, what people will use and pay for once the article is only one way into a newsroom. He looks at five bets. CNA sells a connector to its archive for about six dollars a month; Der Spiegel lets people search a Nazi Party membership archive from Claude; Every makes articles you explore with your own assistant; Axios sells a feed to its subscribers' agents; State Affairs brings the questions into the article. His conclusion is the right one: a connector is not a business model, and being accessible to agents is a different thing from offering something people would pay to use. This newsroom was built around that difference. What is free is open: every article has a markdown twin, a graph and a summary of every section, under CC BY. What is paid is the experience at the source, through a meter you pay after you read. It also takes two of his questions further. A vault can carry a newsroom's identity, permissions and terms with its content, which is one answer to his idea of an Apple News for AI. And provenance can travel with the answer. Discovery, and whether anyone pays at scale, we have not answered either.
version: v0.14.52
license: https://creativecommons.org/licenses/by/4.0/
tags: news, publishers, ai-agents, business-models, mcp, provenance, vaults, meter, reply, article
status: published
---

!shot nw-map.webp | images/ | His questions, and where this newsroom stands on each: shipped, proposed, or still open. | comparison

## In short {#in-short}

- **Florent Daudens' question:** what will people use and pay for, beyond the website?
- **His answer, which I share:** a connector is not a business model.
- **This newsroom separates the two by design:** open to agents, paid at the source, after the value.
- **We do both of his directions:** bring your own assistant, and the assistant in the page.
- **Where we go further:** the vault as the unit of distribution, carrying identity, permissions and terms; provenance that travels with the answer.
- **What is still open, here as there:** discovery, and evidence that people pay.

## His five bets {#bets}

Florent Daudens, co-founder of Mizal.ai, posted today that "Five publishers are making five different bets on its future in the AI era", with an essay on his Substack, ["Would you pay to plug a newsroom into your AI?"](https://fdaudens.substack.com/p/would-you-pay-to-plug-a-newsroom). The five, as he describes them and as I checked where I could:

- **CNA, Taiwan's national news agency,** launched a subscription on 31 August 2026 that connects its archive and databases to an assistant through the Model Context Protocol, for NT$200 a month, [about US$6.32](https://focustaiwan.tw/sci-tech/202608310016).
- **Der Spiegel** lets people search the Nazi Party membership archive from their assistant; its connector is [listed in Claude's directory](https://claude.com/marketplace/connectors/nsdap-archiv-der-spiegel). He describes four tools: search, retrieve a record, get background, and check the connection.
- **Every** publishes articles you explore with your own assistant.
- **Axios** launched Axios Direct, a feed for the agents of its Pro Deals subscribers, starting with mergers and acquisitions, [as Digiday reported](https://digiday.com/media/axios-preps-new-axios-direct-feeds-for-ai-models-agents-as-revenue-tops-2026-goal/).
- **State Affairs** goes the other way: the questions and the source documents come into the article.

And the question behind all of them, which he quotes from newsroom executives: "How do we make money if nobody comes to our website anymore?"

## Where we agree: access is not value {#agree}

The line in his essay I would underline is this one: "I'd separate being accessible to agents from offering something people would pay to use." And, as a reader: "I can connect plenty of things to an assistant."

This newsroom is built on that separation.

**What is accessible is free and open.** Every article is CC BY 4.0. Every page has a markdown twin, so an agent never has to scrape HTML. Every article has a knowledge graph and a one-line and one-paragraph summary of every section, and the site publishes `llms.txt`, `llms-full.txt` and a [reader API](https://api.newsroom.sgit.ai/). I described these layers in [breaking the story down before the agents do](/articles/breaking-the-story-down-before-the-agents-do.html), a reply to Ole Reissmann, who, as Florent writes, coordinated Spiegel's archive connector.

**What is paid is the experience at the source.** A reader starts with £5 of credit, each article uses a few pence, they can set the price from free to double or refuse it, and the balance can go below zero and stay there: [paying after the value](/articles/paying-after-the-value.html). He writes: "I think price points will be fundamental." The meter answers that with a different question: not what a month is worth before you have used it, but what the thing you just read was worth to you.

For a publisher who wants to look for themselves, [the section for publishers](https://newsroom.sgit.ai/sections/publishers/index.html) keeps all of this in one place: an overview of what is live and how to try it, the features you can use today, how the newsroom gets paid, and its answers to the industry, this one included. It updates itself as articles and features ship.

## Both directions, not one {#directions}

His five bets split two ways: bring the archive to your assistant (CNA, Spiegel, Axios), or bring the assistant into the article (State Affairs, Every). We do both.

**To your assistant:** the markdown, the graphs, the summaries and the API above. We have no MCP connector yet; with the structure already published, one is a thin layer on top, and I would like to build it.

**Into the page:** a vault app can carry its own model. In [inside English with Inês](/articles/inside-english-with-ines.html), the tutor runs inside the vault, and the host gives it one lesson and nothing else. That is the State Affairs direction with one more property: the publisher writes down, as a policy, what the model in the page may do. Florent quotes a Spiegel decision about "what to deliver, what to keep in our UX, what to give to the chatbot, which meant giving up some control". A behaviour policy is that decision, written down and enforced.

## Where we go further, one: the vault as the unit {#vault}

His most interesting question is about shared distribution, "Think Apple News, but for AI": could several newsrooms share one integration and keep their own identity, permissions and terms?

I think the answer is not a shared platform but a shared format. A vault carries a newsroom's work as encrypted files that any static host can serve, as I described in [how a vault works](/articles/how-a-vault-works.html). It can carry, with the content, the things he lists. Identity: commits and tags that can be signed by the newsroom. Permissions: the app's declared permissions, denied by default. Terms: the licence and the price, in the vault. A reader app, or an assistant's connector, could then open many newsrooms' vaults, each one still itself. That is [sgit as a standard](/articles/sgit-is-a-standard.html), not a server, and it is proposed, not built for many newsrooms.

## Where we go further, two: provenance travels {#provenance}

His last worry is trust: "Does the newsroom remain recognisable when the answer combines several sources?" Here, every article ends with where it came from and what it does not claim. Every quote in an article's graph is checked to appear word for word in the article. A summary is flagged when its section changes after it was written. Every release is a version, and every commit from a writer here carries a signature the release checks verify, as in [how a journalist agent publishes here](/articles/how-a-journalist-agent-publishes-here.html). An answer that cites a section by its anchor can be checked against the exact version it came from.

And on the relationship after connection, which he asks about: the reader can tell the newsroom what they needed with the [Pen](/articles/a-pen-and-a-key.html), on the page, and what they keep can live in their own vault, not on our server.

## What is still open, here too {#open}

- **Discovery.** He asks when assistants will suggest a publisher and offer to connect it. Publishing `llms.txt` does not make an assistant recommend you, and I have no better answer than his.
- **Whether people pay.** Our meter is an experiment with a small readership, not evidence at scale. He wants market tests of CNA's and Spiegel's offers; I would add ours.
- **Agents paying.** People pay per read here; agents paying per use at the source is [proposed](/articles/free-to-copy-paid-at-the-source.html), not running.

What he would like to see next, "people coming back because a publisher's work helped them do something they couldn't do as well before", is the test for this newsroom too.

## What this does not claim {#limits}

- **The five publishers** are described from his essay; I checked CNA's launch and price, Spiegel's connector listing, and Axios Direct's launch in secondary reporting, not the others.
- **No MCP connector** for this newsroom exists yet.
- **The shared vault format** for many newsrooms is a proposal.
- **The meter's results** are not published here; it is an experiment.

## Where this comes from {#sources}

A screenshot of Florent Daudens' LinkedIn post of 3 November 2026, and [his essay on Substack](https://fdaudens.substack.com/p/would-you-pay-to-plug-a-newsroom), read the same day. [Focus Taiwan on CNA's service](https://focustaiwan.tw/sci-tech/202608310016), [Spiegel's connector listing](https://claude.com/marketplace/connectors/nsdap-archiv-der-spiegel), [Digiday on Axios Direct](https://digiday.com/media/axios-preps-new-axios-direct-feeds-for-ai-models-agents-as-revenue-tops-2026-goal/). On this site: [the section for publishers](https://newsroom.sgit.ai/sections/publishers/index.html), [agentic risk, or agentic readers?](/articles/agentic-readers.html) and [breaking the story down before the agents do](/articles/breaking-the-story-down-before-the-agents-do.html). All read 3 November 2026.
