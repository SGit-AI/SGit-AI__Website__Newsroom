# The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying, sgit.ai

> A follow-up to One article, five readers, with the numbers. The five readers turned 17,949 words into layers of graph, and the biggest layer, the Librarian's catalogue, is 2.8 times the size of the articles it catalogues. That looks like the opposite of compression, until you measure what an agent actually loads to answer a question. Across all 45 concepts in the topic, the graph answers in a median of 2,579 tokens, with every item anchored to its sentence, against 25,698 to read the five articles: 90% less. Then the hypothesis: the more content there is, the more it compresses, because the graphs reuse each other. Tested on this site's 70 articles, it fails for the graphs no one curated (928 node labels, 908 of them unique) and holds for the one a Cartographer merged (114 concept mentions, 45 concepts, the last article reusing 25 and adding one). Projected to 100,000 articles, a curated index is 150 to 2,700 times smaller than the corpus, and a question costs about 13,000 tokens whatever the size, while search reads 59,000 and finds 2% of what is there. Compression is earned by curation, and curation is the work worth paying for. So the economic model: today the agent pays to process the raw web and guesses at its meaning; a publisher that serves meaning, a projection fitted to the agent's persona and objective, and claims signed with an expiry date, saves the agent more than it charges. The agent pays not to pay. This article lays out the arithmetic, the payment rails that exist, and what it does not yet prove.

*Source: <https://newsroom.sgit.ai/articles/the-agent-is-the-reader.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying

# The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/the-agent-is-the-reader.md) · [sgit.ai v0.7.43](https://sgit.ai/admin/versions.md) · newsroomeconomicsagentsmicropaymentsfractal-semantic-graphscompressionpersonastokensprovenancesigned-claimslibrariancartographerarticle

***Abstract:** A follow-up to One article, five readers, with the numbers. The five readers turned 17,949 words into layers of graph, and the biggest layer, the Librarian's catalogue, is 2.8 times the size of the articles it catalogues. That looks like the opposite of compression, until you measure what an agent actually loads to answer a question. Across all 45 concepts in the topic, the graph answers in a median of 2,579 tokens, with every item anchored to its sentence, against 25,698 to read the five articles: 90% less. Then the hypothesis: the more content there is, the more it compresses, because the graphs reuse each other. Tested on this site's 70 articles, it fails for the graphs no one curated (928 node labels, 908 of them unique) and holds for the one a Cartographer merged (114 concept mentions, 45 concepts, the last article reusing 25 and adding one). Projected to 100,000 articles, a curated index is 150 to 2,700 times smaller than the corpus, and a question costs about 13,000 tokens whatever the size, while search reads 59,000 and finds 2% of what is there. Compression is earned by curation, and curation is the work worth paying for. So the economic model: today the agent pays to process the raw web and guesses at its meaning; a publisher that serves meaning, a projection fitted to the agent's persona and objective, and claims signed with an expiry date, saves the agent more than it charges. The agent pays not to pay. This article lays out the arithmetic, the payment rails that exist, and what it does not yet prove.*

What five articles became, in tokens. The full catalogue is nearly three times the size of the articles, because every item carries its sentence. An agent does not load it whole: asking about one concept, it loads a median of 2,579 tokens of anchored graph instead of 25,698 of prose.

[One article, five readers](one-article-five-readers.md) ended with a list of what to do next, and with one question it did not ask. It counted what the five readers produced and what they cost: about 1.1 million tokens for five articles. It did not ask who would pay for that, or why.

This article is the answer I have been circling in my voice memos for a few weeks, and I think it is a big one. The readers of this site are increasingly not people. They are agents, sent by people. Today, an agent that reads the web pays to process all of it, and then guesses at what it means. What the five readers build is the thing that makes that reading cheap: an index of meaning, with provenance, that gets more efficient as it gets larger. A reader that saves money by using it will pay for it, not out of goodwill but because paying is cheaper than not paying. That is an economic model, and in this article I try to put numbers on it.

The data comes from the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md), cloned with its published read key, and from the source of this site's 70 articles. Tokens are estimated at four characters each, the same way for every layer, so the ratios are fair even where the absolute numbers are approximate. The model and its outputs are published as [data](data/the-agent-is-the-reader__model.json).

## In short

- **The graph looks big, and it is.** The Librarian's catalogue of five articles is 72,000 tokens against 25,700 for the articles: 2.8 times larger, because every one of its 662 items carries the sentence it came from. That is an index with provenance. It is not meant to be loaded whole.
- **What an agent loads is small.** For each of the topic's 45 concepts, the graph's answer (the concept, its edges and every anchored item behind them) is a median of 2,579 tokens. Reading the five articles is 25,698. That is 90% less, and the graph's answer comes with citations the prose does not have.
- **The readers check each other, and knowing when to stop matters.** The Librarian found 32 problems in published articles, at about 12,600 tokens each; the Cartographer sent back 37 corrections, at 7,100 each; the Historian found one systematic error, for 154,000. Each pass verifies the one before, and the third cost twenty times more per finding than the first two, which is why the roles have limits.
- **Compression with scale is real, but only where someone curates.** This site's 70 per-article graphs have 928 node labels, 908 of them unique: no reuse, no compression. The topic the Cartographer merged has 114 concept mentions over 45 concepts, and new concepts per article fell 17, 11, 5, 11, 1.
- **Projected to 100,000 articles,** a curated concept index is 150 to 2,700 times smaller than the corpus, depending on how fast new concepts slow down. A question about a mid-frequency concept costs about 13,000 tokens at any size. Search reads 59,000, and at that size sees 2% of the articles that mention it.
- **This is PageRank with meaning.** Google won by extracting crude meaning from links. A textbook PageRank over this site's own links puts two articles that only cite each other at the top. Typed edges, each citing the sentence it rests on, say what the link means.
- **The agent pays not to pay.** If a publisher saves an agent more tokens than it charges, paying is rational. Building the graph cost about 220,000 tokens an article and saves about 23,000 per question, so an article's graph pays for itself after about ten questions about it.
- **Two more things can be sold.** A projection fitted to the agent's persona and objective, so the agent gets the slice it needs. And a signed claim: a cryptographic statement that this site still stands behind a sentence as of a date, with an expiry, renewed for a fee.
- **The rails exist.** HTTP 402 payments in stablecoins moved to a Linux Foundation project in April 2026; Stripe charges agents per request; this site's reading meter charges people by the share of a page they read. What is missing is the demand, and the demand comes from the saving.

## What five articles became

The five readers turned five articles into layers. Measured in tokens:

| Layer | Who made it | Tokens | Against the articles |
|---|---|---|---|
| The five articles | the Journalist | 25,698 | 1.0× |
| Catalogue, full JSON, 662 items | Librarian | 72,152 | 2.8× |
| Catalogue, statements only | Librarian | 18,891 | 0.74× |
| Anchors, the sentences items came from | Librarian | 16,979 | 0.66× |
| Decks, 45 slides | Storyteller | 13,011 | 0.51× |
| Article ontologies, five | Cartographer | 10,088 | 0.39× |
| Topic ontology, 45 concepts and 78 edges | Cartographer | 8,262 | 0.32× |
| Historian notes, five | Historian | 2,990 | 0.12× |
| Concept index, one line per concept | Cartographer | 1,818 | 0.07× |
| Two-minute versions, five | Explainer | 1,753 | 0.07× |
| Edge list, subject verb object | Cartographer | 678 | 0.03× |

Two things are true at once. The full graph is larger than the text, and it should be: the catalogue is a promise that every claim, number and question in the articles can be found, with the exact sentence it came from. And almost every useful way of reading it is much smaller than the text. The concept index that tells an agent what the five articles are about is 7% of them. The edge list that says how the ideas connect is 3%.

For the economics, the question that matters is not how big the graph is. It is how much an agent has to load to answer a question. So I measured it, for every concept. For each of the 45, the graph's answer is the concept index (to find it), the concept's own entry, every edge that touches it, and every catalogue item those cite, each as its one-line statement and its anchor. The alternative is the prose: either the articles the concept appears in, if the agent somehow knows which, or all five.

| Route to an answer about one concept | Median tokens | Range |
|---|---|---|
| The graph: concept, edges, anchored items | **2,579** | 2,147 to 4,027 |
| Read the articles it appears in (if you know which) | 10,617 | up to 25,698 |
| Read all five articles | 25,698 |  |

Against reading everything, the graph saves between 84% and 92% on every one of the 45 concepts, with a median of 90%. Against reading only the right articles, which an agent cannot know without an index, the median saving is 78%. And the graph's answer is better as well as cheaper: every statement arrives with its anchor, so the agent can quote and cite without a second pass. The same shape appeared in [the bridge, followed to the end](the-bridge-followed-to-the-end.md), where a routing agent's question was answered from the story's graph in 583 tokens, against about 45,000 for searching and reading.

## The readers check each other

The part of the five readers' run I like best is the part we did not design. To anchor every item, the Librarian had to read every sentence, and it found a total that did not add up, a list shorter than its count, and a claim the article never supported: 32 flags in published articles. The Cartographer, building the ontology from those catalogues, sent the Librarian 37 corrections: claims that were really three claims, a method the article calls a proposal. And the Historian caught the Cartographer out: its "new" concepts were new to the five articles, not to the site.

The readers check each other. Each pass is a verification of the one before: 12,600 tokens per flag for the Librarian, 7,100 per correction for the Cartographer, 154,000 for the Historian's one systematic catch. The loop is worth running; it is also worth stopping.

Making the map turned out to be the verification. That matters for the economics in two ways. First, it is part of what a buyer gets: a graph whose items have been read against their source by one agent, and against each other by another, is worth more than a summary. Second, it has a cost curve. The first two passes found 69 problems between them, at under 13,000 tokens each; the third found one, valuable, at 154,000. Run the loop again on the same articles, and the yield will fall further. That is why every role has a failure sentence, a word limit and a stopping rule, and why the next step is to make the stopping rule a number: stop a pass when it costs more per finding than the finding is worth.

(The loop also caught something in this site's own writing, while this article was being prepared. One article, five readers said the 1.1 million tokens were "most of it the Cartographer", and its own table says the five Librarians used 403,000 and the Cartographer 264,000. That sentence is now corrected, and the correction is in the article's version history.)

## Does it compress as it grows?

The hypothesis from my voice memo was that the more content there is, the more it compresses, because the graphs reuse each other: each new article adds fewer new concepts and more connections, so the index grows more slowly than the corpus. If that is true, the economics improve with scale, which is the opposite of what happens to an agent reading raw text, where more content means more context, more cost, more latency and more missed.

I tested it on this site's 70 articles, from 17 August to today, using two kinds of graph. And the honest answer is that I was half right.

**The graphs no one curated do not compress.** Every article on this site has its own small graph, written with the article. Across the 70, they have 928 node labels, and after lower-casing and stripping punctuation, 908 are unique. Each article names its ideas in its own words, and nothing merges them. The tags are no better: 672 tag uses, 320 distinct tags, and new tags per article have not fallen: 4.4 per article in the first half of the site's life, 4.7 in the second. Left alone, the index grows at least as fast as the corpus.

**The graph a Cartographer curated does.** The topic ontology for the five articles on behaviour policies has 114 concept mentions over 45 concepts, each concept used in 2.5 articles on average. New concepts per article, in date order, fell 17, 11, 5, 11, 1; the last article reused 25 and introduced one. That is the reuse the hypothesis needs, and it exists only because the Cartographer merged five names for the same method into one.

So the hypothesis holds for the curated layer and fails for the rest. Compression with scale is not a property of graphs. It is a property of curation. And that makes the economic argument stronger, not weaker, because curation is exactly the work that someone has to do, and can be paid for.

Projected from 5 to 100,000 articles. The corpus grows in a straight line. An uncurated index grows with it. A curated index grows more slowly, at a rate fitted on five articles and shown as a band. The cost of a question flattens in the graph and rises, or loses recall, in the prose.

To see what that means at scale, I fitted the growth of the curated concepts to the usual curve for vocabularies, where the number of distinct terms grows as the corpus size raised to a power below one. On five articles, the power comes out at 0.62. That is too few points to trust, so the projection uses a band from 0.5 to 0.75. With the site's average article of 5,914 tokens, and the measured 40 tokens per concept in the index:

| Articles | Corpus tokens | Curated index, against the corpus | Uncurated, against the corpus | A question in the graph | Search, top ten | What search sees |
|---|---|---|---|---|---|---|
| 5 | 29,600 | 13× to 19× smaller | 11× | 2,900 | 11,800 | all of it |
| 70 | 414,000 | 24× to 70× | 11× | 11,700 | 23,700 | all of it |
| 1,000 | 5.9 million | 47× to 266× | 11× | 12,400 | 29,600 | all of it |
| 10,000 | 59 million | 84× to 841× | 11× | 12,900 | 59,100 | 20% |
| 100,000 | 591 million | 150× to 2,660× | 11× | 12,900 | 59,100 | 2% |

The question is about a mid-frequency concept, one that appears in 0.5% of the articles. The graph's answer is the agent's slice of the index (its persona's 250 nearest concepts), the concept and its edges, and up to 40 anchored items, with counts of the rest. Search reads the ten best-ranked articles in full. Both are assumptions, and they are in the data file. The shape is not an assumption. As the corpus grows, the curated index falls further behind it, the cost of a question in the graph stops growing, and an agent that reads prose either pays in proportion to the corpus or reads a shrinking share of what is there.

## Meaning, not just compression

Compression is not the whole of it. Google's insight with PageRank was that links carry meaning: a page that many pages point to is probably important. It was crude, it missed a great deal, and it worked, because a crude signal of meaning across the whole web beat raw text.

A textbook PageRank over this site's own article links shows both halves. The most-linked articles are the ones you would expect: Fractal Semantic Graphs and Six agents, one inbox, with 21 inbound links each, and Every risk is already accepted and Footprint and blast radius, with 20. But the top two places go to two articles that cite only each other: a loop that traps the rank. The link says "related". It does not say how.

The Cartographer's edges do. `enforces`, `undermines`, `replaces`, `depends-on`, `evidences`: 24 verbs, each with its inverse, each edge citing the catalogue items it rests on. An agent that follows one knows what the connection is, and which sentence proves it; the topic ontology adds which article introduced each concept. That is the difference between a web of links and a web of meaning. It is also why what the readers produce is not a compressed copy of the article. It is the article's argument, made addressable.

## Agents are personas too

This site already serves people as someone rather than as nobody. Readers build [personas](pay-to-keep-your-persona.md) from what they read, and [a link can land someone as a persona](a-link-to-a-persona.md): a CISO, as a CISO. The step I am arguing for here is small. An agent is a reader with a persona too, and usually with a sharper one, because it arrives with an objective.

A CISO's agent asking whether its company's coding agents need behaviour policies does not need 70 articles. It needs the slice of the graph around reach, mandate, barrier and boundary, at the altitude of a decision, with the anchored claims and their dates. A service that builds that slice once, for that persona and that objective, and keeps it current, is doing the work the agent would otherwise do badly and expensively on every visit. That is what the persona is worth to an agent: not personalisation as a courtesy, but a smaller, better context.

There is a connection here to the most expensive thing agents do to themselves. When a long session runs out of room, the model summarises its own context to keep going, and [re-anchoring](re-anchoring-agent-behaviour-policies.md) is about what that loses: the rules. That summary is compression done without knowing what matters: best effort, with no feedback, and no one maintaining it. The session that runs this site has been through it twice this week, and both times it was the re-anchored policy, not the summary, that brought the rules back. What the readers do is the same operation done the other way round: compression with context, curated, checked by a second reader, kept up to date, with provenance on every item. The first is free and lossy. The second is worth paying for.

## The agent pays not to pay

Today the economics of agent reading run one way. The agent, or the company behind it, pays to fetch, parse and tokenise the raw page, and then pays again to work out what it means, every time, on every site. [The token bill nobody is sending](token-bill-nobody-is-sending.md) put numbers on the first half: 16,000 fetches a week of one small publisher's pages, a markdown twin 62% cheaper than the HTML on this site, and a proposal that providers share the saving. This article is about the second half, the meaning, which is larger.

The rule is simple. An agent pays a fee F for a graph answer if F is less than what it would have spent without it: the token price times the tokens saved, plus whatever the better answer is worth. For the five articles, the saving is about 23,000 tokens per question against reading them. At the list prices used in the token bill article, $1 and $2 per million input tokens, that is $0.02 to $0.05 a question. Small, and the whole point of micropayments is that small adds up.

The agent pays not to pay. The fee is a share of the tokens it saves; the publisher's cost is building and maintaining the graph; the price passes through to whoever the agent works for; and a signed claim is a second product, with an expiry date that makes it a subscription.

Three numbers make it a business rather than a gesture:

- **Break-even.** Building the graph cost about 220,000 tokens an article in the five readers' run, most of it the five Librarians and the Cartographer. At 23,000 tokens saved per question, an article's graph pays for itself after about ten questions about it, whatever the token price, because both sides are in tokens. And the cost per article falls as the site ontology settles, and each new article only has to map onto it.
- **At scale.** At 100,000 articles, a question saves about 46,000 tokens against searching and reading the top ten. Per thousand agent questions, that is $46 to $93 of the agent's money not spent, and a 30% share of it is $14 to $28 to the publisher.
- **Volume.** One small publisher's site saw 16,000 agent fetches in a week. If even a fraction of those became paid graph answers, the publisher would have a revenue line that grows with being read, instead of a bandwidth bill.

The payment rails are no longer the obstacle. [x402](https://eco.com/support/en/articles/14839402-x402-protocol-explained), which turns HTTP's 402 Payment Required status into a stablecoin payment, mostly in USDC, was moved by Coinbase into a Linux Foundation project in April 2026. Stripe [previewed charging agents](https://forklog.com/en/stripe-unveils-payments-for-ai-agents-using-usdc-and-x402-protocol/) per request on it in February. Cloudflare's pay per crawl and pay per use, covered in the token bill article, price the fetch. And for people, this site's [reading meter](pay-after-you-read.md) already charges by the share of a page read, after the reader says what it was worth. What is missing is demand, and the demand has to come from the saving. Few will pay a site out of fairness, at the scale of millions of agent requests. They will pay when it is cheaper than the alternative, the way anyone buys a service they could, in principle, do themselves.

### The price passes through

The fee does not have to be uniform, and it does not stay with the agent. An agent works for someone, and the cost of what it reads is part of what it charges them, the way a research service passes on the cost of its data. That means the graph's price can reflect its source. A graph built from a financial daily's reporting, the Financial Times for example, will cost more than one from a local paper or a blog, and it should. The other direction holds too: one person who is the expert on a narrow field can charge a great deal for a graph of their work, because an agent that needs it has nowhere cheaper to get it. Price follows value, and value is measured in what the agent would otherwise spend, and what a wrong answer would cost the person it works for.

## Signed claims, with an expiry date

There is a second product, and it may be the larger one. When somebody takes a claim from this site and uses it, in a report, a filing, or an agent's answer to a client, they are relying on it. Today they have no way to ask whether the site still stands behind it.

A signed claim is that question, answered and made portable. The publisher's agent re-reads the claim against its anchor and its sources, and if it still holds, returns a statement signed with the publisher's key: this claim, this sentence, this hash of the source, true as we understand it on 11 October 2026, and we vouch for it until 11 April 2027. After the expiry the signature still verifies, but it no longer says what the publisher thinks now; to keep it fresh, you ask again. [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) sets out the two ways this site could add the public-key cryptography that makes the signature checkable.

The expiry is what makes it an economic product rather than a badge. Claims age: a number gets revised, a vendor changes its terms, a study is retracted. A publisher that re-checks a claim every quarter and signs it is doing work, and the people who rely on the claim are the ones who benefit, so they pay. The price can follow the claim: one about the date a bridge reopens is cheap and short-lived; one a regulator will read is worth more, and for longer. And the expiry is, quietly, the same idea as RiskMandate's acceptance with an interval: a statement is trusted for a stated period by a named party, and then it has to be renewed.

## What would Wikipedia do?

For me, the organisation best placed to test this is Wikipedia. It is the source agents read most. Its editors already do the Librarian's and the Cartographer's work by hand: citations on every claim, categories, links that mean something. And it already sells reliability at scale to the largest re-users, through Wikimedia Enterprise, an API with guarantees. What this model adds is two things: selling the meaning, a typed and anchored graph of what the encyclopedia says, to every agent per question rather than to a few platforms per contract; and making the price a share of what the agent saves. If Wikipedia did this, the equation for the commons would change, from a cost carried by donors to a revenue line that grows with the reading. It is the same equation for every site with content worth reading, and a small site can start on its own pages, as this one has.

## What this does not show

- **Tokens are estimated.** Four characters per token, the same rule for every layer. The ratios are fair; the absolute numbers would move a little with a real tokenizer.
- **The projection rests on five articles.** The curated growth rate is fitted on five points, which is why it is shown as a band. The topic was also unusually tight. A site-wide ontology across 70 articles is the real test, and it is the next step from One article, five readers anyway.
- **The query model is a model.** The persona slice of 250 concepts, the cap of 40 items, and search reading the top ten in full are assumptions, and different ones move the numbers. They are in the data file, to be changed.
- **The saving is measured on our side.** What an answer engine actually spends on our pages is in its logs, not ours, as the token bill article said. The publisher's half of the experiment is running; the provider's half is not.
- **No agent has paid yet.** The rails exist, and the arithmetic works on paper. Demand is the open question, and the only way to answer it is to offer the graph and see whether agents take it.
- **Signed claims are a design.** The key infrastructure is an RFC, not a release.

## What comes next

1. **Build the site altitude.** One ontology across all 70 articles, so the reuse test can be run on a real corpus rather than five articles, and so "new" means new.
2. **Publish an agent's door.** Today the door is [/llms.txt](../llms.txt) and a markdown twin of every page. The next one is a page per persona that tells an agent how to navigate the graph, with the concept index, the edge list and the anchors as plain files, and the cost of each in tokens in the header.
3. **Price one question.** Put a graph answer behind a 402 response at a fraction of a cent, and count how many agents pay rather than read.
4. **Sign one claim.** Pick ten claims from the five articles, re-check them, sign them with an expiry, and publish the signatures so that anyone can verify them.
5. **Measure the stopping rule.** Run a second Librarian pass applying the Cartographer's feedback, and record the tokens per finding, to see where the loop stops paying.

The articles stay long; the readers make them findable; and the hypothesis that started this, that the work should pay for itself because it saves the reader money, is now a set of numbers that anyone can check. If you publish something agents read, and you want to try selling them the meaning rather than the page, let's talk: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine. I asked an agent in a separate Claude session to run the numbers and draft this article with its figures and data; this site's agent then rewrote it in the voice of this site, softened two figures' wording, and corrected the sentence in One article, five readers that the work turned up. The argument is mine, and so is the editorial responsibility. The layer, query and reuse measurements are computed from the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md), cloned with its published read key, and from this site's article sources and graphs as of 11 October 2026. The projection and the economics are a model, and every assumption is in the [data file](data/the-agent-is-the-reader__model.json). The payment rails come from secondary sources, using only the facts several of them agree on: [x402 protocol explained](https://eco.com/support/en/articles/14839402-x402-protocol-explained) (Linux Foundation, April 2026) and [Stripe's machine payments preview](https://forklog.com/en/stripe-unveils-payments-for-ai-agents-using-usdc-and-x402-protocol/) (February 2026); and [Wikimedia Enterprise](https://enterprise.wikimedia.com/). On this site: [One article, five readers](one-article-five-readers.md), [The token bill nobody is sending](token-bill-nobody-is-sending.md), [The bridge, followed to the end](the-bridge-followed-to-the-end.md), [Pay to keep your persona](pay-to-keep-your-persona.md), [A link to a persona](a-link-to-a-persona.md), [Pay after you read](pay-after-you-read.md), [Re-anchoring](re-anchoring-agent-behaviour-policies.md), [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md), [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md), [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) and [The future of news is the story vault](future-of-news-story-vault-not-paywall.md).

## Threads

News & evidenceStartups & strategy[This article as a graph →](graphs.md#the-agent-is-the-reader)

### Builds on

- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [A link to a persona: send people to the newsroom as someone, not as nobody](a-link-to-a-persona.md) Send a CISO to the newsroom as a CISO: personas kept in a vault by the newsroom's agents, opened from a link, followed or forked.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md) AI answer engines pay to read the web as HTML; a publisher who serves markdown, dates, hashes and a typed graph saves them tokens and should get a share.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.

### Continued by

- [The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks](the-wire-as-a-graph.md) Design the wire from what the reader sees: every name a link with a long-lived ID, every sentence a claim, stories of stories, folders by gravity.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [Firing journalists is the worst thing a publication can do: what a hiring decision says about where a publisher is going, and who to hire instead](firing-journalists.md) A hiring decision is a direction of travel: fire the journalists and the centre of gravity moves to packaging, where the metric makes clickbait by construction.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [Brief the agent too: the people I talk to work with agents, so what I send has to reach both](brief-the-agent-too.md) The people I advise read through agents. Content needs a second package, a brief for their agent, and memory, so it reads what changed, not everything.
- [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](a-model-in-the-tab.md) Chrome now ships a language model any page can prompt, offline, on capable desktops. The last piece of the client-side puzzle, with rough edges.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 71 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=71)

**Posting this article on LinkedIn?** The cover is [the-agent-is-the-reader.jpg](banners/the-agent-is-the-reader.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-agent-is-the-reader.html)*
