# The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed, sgit.ai

> With the reader's vault live on newsroom.sgit.ai, the next brief is about what a reader does with it, and it starts from one image: the site is an inbox that starts empty. Every piece that arrives, an article this site wrote or a story the wire aggregated, is something I have not decided about yet, and the first thing I do with it is decide, in a second, with nothing loaded: read now, read later, not for me, more of this, less of this, comment, move it to another persona. That is the inbox mode, and it is thinking fast. Reading is the slow mode, and it is where the marks live: highlights of different kinds, not one or two as Medium has but interesting, great phrase, not sure, fact, evidence, question, each a node in a graph the reader owns and that connects to the graphs this site already publishes for every article; the pane on the right becomes about the piece in front of you; the piece can be shown with every term a link, or classified sentence by sentence. The signals that come free, scroll depth, time while awake, where you came from and went to, are kept the way the meter keeps them: in the browser, in the vault when you ask, shown to an agent only by your read key. Comments for the newsroom go down the write-only lane, signed by the persona's key, with a copy kept. None of it is gamified: a decision is offered where you would take it, never at the end of a page to make you scroll there. The brief is the second part. The first part is why I could not have written it two days ago: the properties of what runs are the constraints I think with, and the constraints are what let me think.

*Source: <https://newsroom.sgit.ai/articles/the-site-is-an-inbox.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed

# The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/the-site-is-an-inbox.md) · [sgit.ai v0.7.67](https://sgit.ai/admin/versions.md) · newsroomreadinginboxpersonasgraphsfeedback-loophighlightssignalsprivacyvaultspkibriefarticle

***Abstract:** With the reader's vault live on newsroom.sgit.ai, the next brief is about what a reader does with it, and it starts from one image: the site is an inbox that starts empty. Every piece that arrives, an article this site wrote or a story the wire aggregated, is something I have not decided about yet, and the first thing I do with it is decide, in a second, with nothing loaded: read now, read later, not for me, more of this, less of this, comment, move it to another persona. That is the inbox mode, and it is thinking fast. Reading is the slow mode, and it is where the marks live: highlights of different kinds, not one or two as Medium has but interesting, great phrase, not sure, fact, evidence, question, each a node in a graph the reader owns and that connects to the graphs this site already publishes for every article; the pane on the right becomes about the piece in front of you; the piece can be shown with every term a link, or classified sentence by sentence. The signals that come free, scroll depth, time while awake, where you came from and went to, are kept the way the meter keeps them: in the browser, in the vault when you ask, shown to an agent only by your read key. Comments for the newsroom go down the write-only lane, signed by the persona's key, with a copy kept. None of it is gamified: a decision is offered where you would take it, never at the end of a page to make you scroll there. The brief is the second part. The first part is why I could not have written it two days ago: the properties of what runs are the constraints I think with, and the constraints are what let me think.*

Two modes. The inbox mode decides what happens to a piece with nothing loaded; the reading mode is where the marks and the signals live. Everything stays in the reader's browser and vault, and the reader chooses what an agent sees.

The vault is live, and I have a brief for what to do with it. But the brief is the second half of this article, because the first half is about why I have it at all.

## In short

- **I could not have written this brief two days ago.** Not for lack of time or ideas. For lack of constraints. Until the passkey worked and the sign-in was not needed, until a door was per path, until the sync was one file per device, I did not know the properties of the thing I would be writing for. The properties are what let me think.
- **The site is an inbox, and it starts empty.** Every piece that arrives, an article this site wrote or a story the wire brought in, is something the reader has not decided about. Deciding is the work; reading is one of the decisions.
- **Two modes.** The inbox mode decides, fast, with nothing loaded: read now, read later, not for me, more like this, less like this, comment, move to a persona. The reading mode does, slowly, with the piece open and its context loaded.
- **No gamification.** A decision is offered where the reader would take it, never at the end of a page so that they scroll there. A signal the site engineered is not a signal.
- **Marks build the reader's own graph.** Not one highlight but kinds: interesting, great phrase, not sure, fact, evidence, question. Each is a node, connected to the graphs this site already publishes for every article. Meaning comes from connectivity, and the reader's graph is worth more the more it is used.
- **The signals come free and stay yours.** Scroll depth, time while awake, where you came from and went to. Kept as the meter keeps everything: in the browser, in the vault when you press Update, seen by an agent only through a read key you gave it.
- **Personas have keys.** Each persona is disposable and has its own key pair, so a comment to the newsroom is signed by the persona that made it, goes down the write-only lane, and leaves a copy in your vault. The reply is a new version of the article.
- **The test is simple.** It works if reading here, with a graph that grows, is better than reading without one.

## Part one: the constraints are what let me think

[The vault is live](the-vault-is-live.md) ends with a sentence I want to start from, because this article is the proof of it. The brief below did not exist on 10 October. I had the ideas; some of them are years old. What I did not have was the shape of the thing they would run on, and without the shape I could not hold them.

This is not the usual point about agents making things cheap to build, true as that is, and I made it in [Pay after you read](pay-after-you-read.md): the more you have, the faster you go. It is a point about thinking. When the vault did not exist, "a reader's marks on an article" was an open question in every direction: where would they live, who could read them, what would it cost, would the reader have to sign in, could a mark be sent to us and by whom. Each of those questions is big enough to stop a brief. Now each has an answer, and the answers are not mine, they are the properties of what runs. Marks live in the reader vault, in a file per device. Nobody can read them but the reader, and an agent the reader gives a read key to. Writing them costs one commit when the reader presses a button. There is no sign-in. A persona can have a key pair in the master, so a mark can be signed. Those five facts close off most of the design space, and what is left is small enough to think about in a morning.

I did not expect this, and I think it is the more important half of the feedback loop. I had it as: use it, miss it, build it, use it again. It is also: build it, learn its properties, and only then have the next idea, because the next idea is made of the properties. The constraints limit what I can write, and without that limit I would write everything and finish nothing. So the order matters. Ship first, think second, and do not pretend the thinking could have come first.

## Part two: the brief

*For the session that runs newsroom.sgit.ai. Written by the sgit.ai site session for Dinis Cruz, 12 October 2026, on top of the vault pane at v0.11.0. Dinis decides what ships, and is the first user.*

### The site is an inbox

Start from this image and most of the rest follows. The site has two kinds of content now: the articles it writes, and the [wire](two-agents-one-vault.md) it reads from a vault that other agents keep, which will grow into sources the reader chooses to follow. For a reader, both arrive the same way: as pieces they have not decided about. So the site, for that reader, is an inbox. It starts empty, cleared, nothing to see. As pieces arrive, each one waits for a decision. When the decision is made, the piece leaves the inbox and the decision becomes a record. The state the site should always be able to return to is empty.

This is a different thing from a front page, and it is why the front page can stay the Editor's: the inbox is the reader's view of the same pieces, and it is personal because the decisions are.

### Two modes, and the science behind the split

Kahneman's distinction between thinking fast and thinking slow is the right frame, and I would build the two modes to match it.

**The inbox mode** is fast. The reader meets a headline, a line, and where it came from, and nothing is loaded: not the article, not its graph, not the reader's context for it. The only thing to do is decide what happens next, and the decision should take a second: read now; read later; not for me; more like this; less like this; comment; move it to another persona. Each is one tap, offered at the piece, and each clears the piece from the inbox. For the wire especially, "not for me" is the most important button, and the most useful signal: it says which concern the join got wrong.

**The reading mode** is slow. The piece is open, its context is loaded, and the pane on the right, which today holds the vault and the meter, becomes about this piece: its graph beside the text, the reader's marks on it, the decisions already taken, and what it cost. This is where the reader does something with the piece, and it is where the next three sections happen.

The split matters because today the newsroom asks for the reader's judgment at the end of the article, where the meter's card is. That was the right place for a rating that sets a price, and it is the wrong place for a decision, because a decision at the end is a reason to scroll to the end, and that is gamification: a signal we engineered, which is then not a signal. The rule for both modes is that a decision is offered at the moment the reader would take it, and nothing is placed to make them go somewhere.

### Marks, and the reader's own graph

The reader's graph is made of marks, each with a kind; the marks land on the public graphs this site already publishes; a chosen slice goes to the newsroom, signed; a new version comes back.

Medium lets you highlight, and I used it, and what I did not like is that it had one or two kinds of highlight and I have six. When I read, I mark things for different reasons: this is interesting; this is a great phrase; I am not sure about this; this is a fact; this is evidence; this is a question. Each of those is a different kind of node, and the moment the site lets me say which, I am not highlighting any more. I am building my graph.

- **A mark is a node.** It carries the phrase, the article and its version, the persona that made it, the kind, and the time. A comment is a node with an edge to the phrase it is about. An inbox decision is an edge from the persona to the piece.
- **Marks land on the public graphs.** Every article here already has [a graph as JSON](https://newsroom.sgit.ai/articles/graphs.html) beside it, and every wire story has entities, claims and a quote. A mark on a phrase links to the node that phrase belongs to, so "not sure" on a claim is an edge to that claim, and a reader who marks the same claim in two articles has connected them without naming anything.
- **Meaning comes from connectivity.** A phrase marked three times, from three articles, is a topic the reader did not have to declare. That is what [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md) are for, and what Obsidian users already know: the graph is a by-product of use, and it is the most valuable thing the reader makes.
- **The vocabulary view, on demand.** Not always on, because it is noisy. But a switch that turns every term in the piece into a link into the vocabulary, the facts, the connections, the way some of our vaults already do, so that the reader can walk from a word to everything it touches, including their own marks.
- **The piece, classified.** Another switch: the same text shown by what its sentences are, facts, observations, evidence, claims, questions, and by tone or confidence. The site's agents already read its articles this way, as [five readers](one-article-five-readers.md); the reader should see that view and be able to disagree with it, sentence by sentence, and the disagreement is a mark.

This is where the economics of the whole thing sit, and I want to say it plainly. The more a reader marks, the more they use the site; the more they use it, the more they pay, by the meter; and the more they pay, the more their own graph is worth to them, because it is theirs and it is connected. That loop only closes if one thing is true: reading here, with a graph that grows, is a better experience than reading without one. Every feature in this brief is a bet on that sentence, and the vault is what makes the graph the reader's rather than ours.

### The signals that come free

The reading mode can record four things without asking, and it should, because they are useful to the reader first.

1. **How far.** The scroll depth, which the meter already charges by. The bottom of the page means read; a little means glanced. Shown to the reader as a simple "you read this" or "you read a third of this", which is the information I most often want about my own past reading.
2. **How long, awake.** Time on the piece counted only while there is movement, scroll or pointer or key, so that a tab left open for an hour is not an hour of reading. This is an experiment: whether movement is a good enough proxy for attention is something to measure, not assume.
3. **From and to.** The page the reader came from and the page they went to. The site already knows the latter; the former is what lets it answer "how did I get here", and give the reader back and forward through their own reading, which will matter more once search works.
4. **The decisions.** Every inbox decision and every mark, with the persona and the time.

All of it is kept the way the meter keeps everything today: in local storage as it happens, in the reader vault when they press Update, as records and never totals, and shown to any agent only through a read key the reader gave it. The reader can see every record, which is the other half of not gamifying: the signals are the reader's, and they can watch what they produce.

### Personas with keys, and the lane to the newsroom

The reason this brief needs the vault and not just local storage is in two places.

The first is personas. I will have several, and one of them is the newsroom's editor: I read every article, I see what works, I review it, and I need to comment on everything. That is a different lens from my CISO persona or my founder persona or my general-interest one, and the inbox mode's "move to a persona" is how a piece gets to the right one. Personas should be disposable, and each should have a key pair of its own, kept in the master vault as [the passkey design](the-passkey-opens-the-vault.md) describes: one to sign, one to receive. What the editor persona signs is not what the CISO persona signs, and a persona can be handed to an agent as a read key to its slice of the graph, and only its slice.

The second is the lane. A mark or a comment the reader addresses to the newsroom, "not sure" on a claim, a wrong flag on a wire story, a comment on a sentence, goes the way [sending your reading](https://newsroom.sgit.ai/account/share.html) already goes: encrypted in the browser to the newsroom's published key, into a write-only lane only the newsroom's agent reads. Two things are new. It is signed by the persona's key, so the newsroom knows which of my personas said it and that it was me. And a copy stays in the reader's vault, so the reader always knows what was sent, which is the privacy property: the user controls what goes, and can see it afterwards. The reply, as with [the brief in I miss it](i-miss-it.md), is a new version of the article, and the version page shows it.

In my own case I will go further and give the agent that edits the site a read key to my editor persona's vault, so that it sees every mark I make as the editor, not only the ones I send. That is my choice, as a reader, and it is the point: the same mechanism serves a reader who sends nothing and a reader who shares everything.

### What to build, in order

1. **The inbox mode on the front page and the wire**: the seven decisions as one tap at each piece, clearing it, recorded as an edge in local storage. Test with the wire first, where "not for me" is the signal the join needs.
2. **The pane about the piece.** On an article, the right-hand pane shows the article's graph, the reader's marks and decisions on it, and what it cost. The vault and the meter move to a tab of the same pane.
3. **Marks with kinds.** Select a phrase, choose a kind, see it in the pane and in the graph. Six kinds to start; the reader can add one.
4. **The free signals**: depth as "you read this", awake time, from and to, in the reader's records, visible to the reader on the account page.
5. **The persona key pairs** in the master, as the passkey design specifies, generated at random on first use, one pair per persona.
6. **The signed lane**: a mark addressed to the newsroom, signed, sent, copied to the vault; and the reply as a version.
7. **The views**: vocabulary on demand, and the piece classified, starting from the five readers' output where it exists.
8. **An experiment per feature.** Each of these is small enough to ship in two versions and compare, and that is how they should be built: a synthetic reader, two variants, a measurement, and the one that holds. The inbox decisions, the kinds of mark and the awake-time proxy are the first three to test.

### What not to build

No decision placed at the end of a page to make the reader reach it. No signal sent anywhere without the reader pressing something. No mark the reader cannot see in their own records. No server of ours.

## What this does not claim

- **None of the brief is built.** The vault, the meter, the personas, the share lane, the article graphs and the five readers' views exist; the inbox mode, the marks, the signals and the signed lane are a design.
- **The science is a frame, not a finding.** Thinking fast and slow is a useful way to split the two modes; whether readers behave that way on this site is what the experiments are for.
- **Awake time is a guess.** Movement as a proxy for attention is an assumption to measure.
- **The economics are a bet.** The loop closes only if reading with a graph is better than reading without one, and one reader's experience, mine, is where that will first be tested.

If you build reading tools, or you want to be a reader whose marks build a graph you own, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on the morning of 12 October 2026, recorded after the newsroom's overnight releases and before I had tested the vault pane myself, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The brief builds on what runs: the vault pane and the activity vault design at newsroom.sgit.ai v0.11.0, the meter, the personas, the share lane and the article graphs, as described in [The vault is live](the-vault-is-live.md), [Pay after you read](pay-after-you-read.md) and [Two agents, one vault](two-agents-one-vault.md). The two figures were drawn for this article. Related: [The passkey opens the vault](the-passkey-opens-the-vault.md), [I miss it, so it is working](i-miss-it.md), [Fractal Semantic Graphs](introducing-fractal-semantic-graphs.md) and [One article, five readers](one-article-five-readers.md).

## Threads

News & evidenceGraphs & knowledgeVaults & method[This article as a graph →](graphs.md#the-site-is-an-inbox)

### Builds on

- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.

### Continued by

- [The briefs so far: sixty-five things this newsroom has asked of itself, what is built, and where each next session starts](the-briefs-so-far.md) Sixty-five briefs this newsroom has asked of itself, audited from the code: 11 built, 21 partly, 32 not, each open one with a session brief.
- [The vault, opened: merging devices, reading every call to the vault server, browsing your vaults, and one viewer that every reader vault links and opens with](the-vault-opened.md) Merging devices, every call to the vault server named and opened, a page to browse your vaults, and one shared viewer that every reader vault opens with.
- [The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks](the-wire-as-a-graph.md) Design the wire from what the reader sees: every name a link with a long-lived ID, every sentence a claim, stories of stories, folders by gravity.
- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.
- [The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it](the-vault-crosses-chrome-profiles.md) The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [Firing journalists is the worst thing a publication can do: what a hiring decision says about where a publisher is going, and who to hire instead](firing-journalists.md) A hiring decision is a direction of travel: fire the journalists and the centre of gravity moves to packaging, where the metric makes clickbait by construction.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 82 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=82)

**Posting this article on LinkedIn?** The cover is [the-site-is-an-inbox.jpg](banners/the-site-is-an-inbox.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-site-is-an-inbox.html)*
