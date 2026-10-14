# Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map, sgit.ai

> Since 2022 I have said that Wardley maps changed how I think, and this site has quietly become a place where I draw them: eleven so far in the articles, seven in a vault, five in a conference talk. This is the best of them, with the context each one came from, and the reasons the technique matters to me. A map is a graph with two kinds of context, a value chain that starts with a user and an evolution axis that says how mature each piece is, and the second axis does not have to run from genesis to commodity. The map tells you what is moving the needle, whether you are optimising at the wrong altitude, what to build and what to buy, and whether a market exists at all: a commoditised layer is a hard sell, and custom building on top of it is where the market is. Two worked examples, sgit and RiskMandate. Then one map read step by step, as a story, because that is what a map is for. Then the fractal: every node on a map is a map, and the dot's place on the parent is the anchor of the child. Two decks you can print to PDF from your browser, and the maps published as data so anyone can take them.

*Source: <https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map

# Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/why-i-love-wardley-maps.md) · [sgit.ai v0.7.77](https://sgit.ai/admin/versions.md) · wardley-mapsstrategystartupsmapsfractal-semantic-graphsagentssgitriskmandatebuild-vs-buyarticle

***Abstract:** Since 2022 I have said that Wardley maps changed how I think, and this site has quietly become a place where I draw them: eleven so far in the articles, seven in a vault, five in a conference talk. This is the best of them, with the context each one came from, and the reasons the technique matters to me. A map is a graph with two kinds of context, a value chain that starts with a user and an evolution axis that says how mature each piece is, and the second axis does not have to run from genesis to commodity. The map tells you what is moving the needle, whether you are optimising at the wrong altitude, what to build and what to buy, and whether a market exists at all: a commoditised layer is a hard sell, and custom building on top of it is where the market is. Two worked examples, sgit and RiskMandate. Then one map read step by step, as a story, because that is what a map is for. Then the fractal: every node on a map is a map, and the dot's place on the parent is the anchor of the child. Two decks you can print to PDF from your browser, and the maps published as data so anyone can take them.*

Nine of the maps drawn on this site since September 2026. Every one is a claim about something real: a product that shipped, a plan that is published, a mistake that became a rule. The ninth is three maps deep.

## In short

- **A Wardley map is a graph with context in two directions.** Down the page is the value chain, from a user's need to the things it depends on. Across the page is evolution, how mature each piece is. Nothing else about the drawing matters much; those two kinds of context are what make it useful.
- **The evolution axis is a choice.** Genesis to commodity is the usual one, and it is the one on every map here, but risk, data and governance can each be an axis. The map is a way of placing things against a scale you chose because it answers your question.
- **The map tells you where the market is.** A layer that has become a commodity is a hard sell. A layer where everyone is custom building on top of a commodity is where the money and the attention are. sgit and RiskMandate are the two examples below, and the second one moved in the last year.
- **A map is a story.** The best use of one is not to show it finished but to read it out: here is the user, here is what is new, here is what it stands on, here is where it is going. One of the maps on this site is read that way below, frame by frame.
- **Maps nest.** Every node is a map of its own, the way every node in a fractal semantic graph is a graph. The place a dot holds on the evolution axis of the parent is where the child's anchor sits. The figure near the end shows three altitudes of this business.
- **Everything here is published as data.** Every figure on this site now sits in the article's graph with its caption and kind, so "every Wardley map on sgit.ai" is one query, not a reading list.

## What a map is, to me

The short description I use is that a Wardley map is a graph with two axes of context. The first is vertical: a value chain, anchored at the top on a user and a need, with each component drawn under the components that need it. The second is horizontal: evolution, how far each component has travelled from a new idea nobody has built to something you buy by the unit without thinking. Simon Wardley's four stages, genesis, custom built, product and commodity, are the scale on every map on this site.

That second axis is the part people argue about and the part I think is the least fixed. In 2022, at the Open Security Summit, I gave a talk called [Why Wardley Maps changed how I think](https://www.youtube.com/watch?v=6gpgnYo6M14), and the argument was that the mapping habit produces a set of shifts in how you see a problem, eleven of them in that talk. Around the same time I wrote about alternative evolution scales: risk as the axis, data as the axis, governance as the axis, and others. I went looking for that post while writing this and did not find it, so I will not quote it; if you have it, send it. The point survives without the text. The horizontal axis is a scale you choose because it answers the question you have, and genesis to commodity is one good answer, not the only one.

What does not change is that the map must be based in reality. Every dot on every map here is a claim: that thing exists, it sits there in the chain, and it is about that mature. The captions say so, and the footer on most of them says "a map, not a measurement", because the positions are judgements and the judgements are the argument. A map you cannot be wrong about is a diagram.

## Why they are so powerful

The talk's eleven shifts are a longer list; these are the ones I use every week.

- **What is moving the needle.** On a map you can see which components are moving, and which movement matters to the user at the top. Most activity is in places the user never sees. The question "what moved this week, and did anything above it notice" is answered by looking.
- **Altitude.** A great deal of effort is spent optimising at the wrong altitude: polishing a component three layers below the need while the layer the user touches has not changed. The vertical axis makes that visible, and the fractal view below makes it precise: pick the altitude first, then the dot.
- **Build or buy.** Anything in product or commodity, buy, rent or vendor it. Anything in genesis or custom built that sits on your path to the user, build it, because nobody else will build it the way you need. Most build-or-buy arguments are two people drawing the same component in different columns, and the map settles which column it is in.
- **Does the market exist.** This is the one I find most people have never asked of their own product. A layer that is commoditised is a hard sell: the buyer already has it, and cheaper. A layer where everyone is custom building, on top of commodities, is a market: each of those builders would rather buy. The examples are below, because the map answers differently for sgit and for RiskMandate.
- **Flow and attrition.** A map shows the flow from the need down to the things that serve it, and where that flow leaks. The attrition points are the dependencies that are slow, immature or owned by somebody else: on [Places of highest leverage](places-of-highest-leverage.md) the one custom layer we had to add sat exactly where a provider was not yet mature, and that is exactly where the work slowed.
- **Who the players are, and where to hook.** The components at the commodity end have names: Apple, Google, Stripe, git. Drawing them puts the people you depend on, and the people you could plug into, on the same page as your own pieces. Where to hook is a question of which mature component you can stand on so that your custom piece is small.
- **A common language.** Two people with a map argue about positions. Two people without one argue about words. The mandate stack maps below were drawn twice, from the outside and from the inside, because the people on each side of the team see a different chain, and the two maps made the difference discussable.
- **Start with the user.** Every map here has a person at the top. It is a discipline, not a convention: the moment the anchor is "the platform" or "the roadmap" the map stops being able to tell you whether anything matters.
- **Many maps, not one.** The same business from different angles and altitudes: a user's chain, a team's chain, a feature's chain, a day's chain. None of them is the map. This article has nine because that is how they are used.
- **Peace.** This is the one I say least often in public. Once a thing is on a map, placed and connected, I stop carrying it in my head. The zen of a map is that the anxiety about what to do next has somewhere to go, and most of it turns out to be about things far from the user.

## The best of ours

Each map below is in the article it came from, with that article's argument around it. Here they are together, with a line of context each, in the order they were drawn.

### The mandate stack, from the outside and from the inside

Map one, from the outside. The anchor is a person who writes to the team. What they see, a reply with a name on it, is custom. What they do not see, the vaults, the sessions, Workspace and encrypted storage, is product or commodity. Rendered with Mermaid wardley-beta.Map two, from the inside. The anchor is the person running the business. The dashed arrows are the movement the team is making: shared memory and the sgit CLI toward commodity, the behaviour policies, the graphs and the custom interfaces from genesis toward product. Everything rests on encrypted storage, which is already a commodity.

[The mandate stack](the-mandate-stack.md) is a team of agents described as a stack, and these were the first two maps on this site that were drawn as a pair on purpose. The person writing in sees one chain; the person running the team sees another, with the same components in different places. The second map carries movement, which is the part of a Wardley map that most diagrams cannot do: the arrows are claims about where things are going, and they were checkable within weeks. They were rendered with Mermaid's Wardley map syntax, so the source is in the article, which matters for the community point at the end.

### Pay after you read: an afternoon as a map

The reading meter at the end of 10 October, as a Wardley map: everything added that afternoon sits on the left, built on components that already existed on the right.

[Pay after you read](pay-after-you-read.md) shipped a reading meter, pay by depth, personas and an encrypted share in one afternoon, and the map is of that afternoon. It is the clearest example here of the build-or-buy reading: every new thing is on the left, and every one of them stands on something on the right that already existed, including the site's own vaults, git and a Stripe link. The frame-by-frame version of this map, one release at a time, is the one read as a story below.

### Agentic cost: the problem, the service, where it goes

The map in three frames: the problem as most companies have it, what the service adds from what is already there, and where it goes. Agents in production on the explorer side, billed by the token, with logs nobody reads together; then the footprint, the twin, the policy and the graph; then cost as a discipline.

The 3 frames, one image each: [1](images/ac-wardley-1.webp) [2](images/ac-wardley-2.webp) [3](images/ac-wardley-3.webp).

[Agentic cost is an engineering problem](agentic-cost-is-an-engineering-problem.md) is a business plan, and the three frames are the plan's argument. The first frame is a market: the person paying the bill at the top, commodity model APIs at the bottom, and between them a blob of custom built things nobody owns. The second frame adds the service, and shows that it adds very little that is new; it reads what is there. The third is the movement. The controls under the figure let you stop on any of the three, which is the whole reason the animated version was replaced today.

### Places of highest leverage: which shoulders

Which shoulders the passkey work stands on. Almost everything under it is a product or a commodity someone else matured; our piece is the door and a door per path; the one custom layer we had to add is the phone by QR, where a provider is not yet mature.

[Places of highest leverage](places-of-highest-leverage.md) asks where to focus when agents can go in every direction, and this map is the answer to "why was it fast". The passkey work went from a design to a product in a day because the shoulders were mature: synced passkeys, the PRF extension, Web Crypto, the vault library, the server. The map also shows the one place it was slow, and that place is the one immature dependency. It is the attrition reading in one picture.

### A Mac of the agent's own

The agent's desktop moves from custom-built to product, on parts that are already products or commodities: Apple silicon Macs, the macOS virtual machine, the models, the desktop agent apps. State, keys and lock-down move with it, because the vaults, the PKI and the policies already exist as parts.

[A Mac of the agent's own](a-mac-of-the-agents-own.md) is the plan for a desktop per agent, and the map is a build-or-buy map with Apple's licence drawn in. Every heavy component is bought; the custom part is the bootstrap that assembles them and the record that leaves the machine. The published plan is in the [Agent Desk vault](https://sgit.ai/demos/vaults/agent-desk/index.md), map included.

### Every mistake added a rule: the verification, twice

Map one: the verification as it runs. The person preparing the install needs confidence the tool is safe, which comes from a report, which rests on the tool's tests and on a team of agents. The six things that keep failing sit in a blob on the left, each rebuilt by hand inside a prompt every session. Files, hashes and git sit at the far right, unused.Map two: the same verification with each piece of process made small and drawn moving right. The tool's tests and the judgment in the report stay custom, because that is the work. Everything else becomes boring on purpose, leaning on files, hashes and git.

[Every mistake added a rule](every-mistake-added-a-rule.md) is about a workflow that kept failing in the same six ways. The two maps are the before and after, and the after is the altitude reading: the custom work is kept where it is the work, the judgement and the tests, and everything else is pushed right onto files, hashes and git that were already there and unused. The blob on the left of map one is what "optimising at the wrong altitude" looks like when you draw it.

### The ones that live in vaults

Three more sets are not in articles but in published vaults, each with its read key on the page. [Strategy Maps](https://sgit.ai/demos/vaults/strategy-maps/index.md) holds the SG/Send strategy as seven Wardley maps, the ones I published on LinkedIn in May 2026, served live from an encrypted vault; its republish story is on [The strategy in seven maps](https://sgit.ai/demos/strategy-maps.md). [ThreatModCon 2025](https://sgit.ai/demos/vaults/threatmodcon-2025/index.md) has five Wardley map walkthroughs inside a threat modelling talk, which is where the mapping habit and the security habit met for me. And the Agent Desk vault above carries its map as an app view. They are listed here because the best-of should include the maps that were not drawn for an article.

## Two examples of "does the market exist"

**sgit.** Take sgit apart and every layer is mature. Storage is a commodity. Version control is a commodity; git won. Encryption is a commodity; AES-GCM and HKDF are in every browser. Each of those is a hard sell on its own, because the buyer has it, cheaper, from somebody with a bigger name. The map says do not sell those. What the map also shows is what sits above them: everyone who wants a private, versioned, shareable unit of work is custom building one, out of a bucket, a repository and a key management story that never quite lands. That is the vault. The market for sgit is not the three commodities; it is the custom building that is happening on top of them, and the product is the piece that lets a customer keep custom building above a vault instead of below it. Every vault on this site is somebody's custom layer, and that is the evidence that the market is there.

**RiskMandate.** [RiskMandate](https://riskmandate.ai) is a productised thing: a mandate, a footprint, a behaviour policy, a record of what an agent did against what it was allowed. It connects to agents, and a year ago agents were a product at best, and the companies building them were the customers. In the last year agents became a commodity: every platform ships one, by the token. On a map that moves the whole dot to the right, and the opportunity moves up. The market for agent behaviour, what an agent is allowed, what it touched, who can prove it, is all genesis and custom built right now; every team running agents is building their own version of it inside prompts and spreadsheets. That is the shape of a market that exists. The map told us the layer below had commoditised before the invoices did.

The two answers are different, and that is the point of asking. For sgit the market is above the product; for RiskMandate the product is at the market and the layer below it just moved.

## Reading one map, as a story

A map is fundamentally a way to tell a story, and the best way I know to show that is to read one out. These are the eight frames of the afternoon from Pay after you read. Use the controls to stop on each one; the second deck below walks the same frames with one question per slide.

The afternoon as a Wardley map, one release at a time: what already existed, then each feature as it was added and what it was built on, ending with what comes next. Times are UTC, from the commits.

The 8 frames, one image each: [1](images/pv-wardley-1.webp) [2](images/pv-wardley-2.webp) [3](images/pv-wardley-3.webp) [4](images/pv-wardley-4.webp) [5](images/pv-wardley-5.webp) [6](images/pv-wardley-6.webp) [7](images/pv-wardley-7.webp) [8](images/pv-wardley-8.webp).

1. **Frame one, before.** Where is the user? At the top: the reader, on every device. What exists? Everything on the right: the articles and the build, git, browser storage, vaults, the sealed envelope, Stripe. Nothing on the left. What am I seeing is a business whose user touches only mature things, which is comfortable and not a strategy.
2. **Frame two, a meter.** The first new dot appears at genesis, close to the user, and it stands on browser storage. One question: is anything above it? Yes, the user. So this is at the right altitude.
3. **Frame three, it goes live.** Pay by depth, below zero with no block, a Stripe link. Three new dots and every edge from them runs to the right. The build-or-buy reading is clean: nothing new was built below the line.
4. **Frame four, personas.** The dot that matters is not the persona but the edge: it connects to the articles, the thing the site already had most of. Where to hook was answered by the oldest component on the map.
5. **Frame five, versions.** A small dot, and it stands on git. It cost almost nothing because its shoulder was a commodity. This is the frame I use to explain why some features are free.
6. **Frame six, the encrypted share.** The first dot that stands on a vault. Here is where the map starts to pay for itself: the custom thing we had to build sits on the one product we had made ourselves, so the chain under it is ours end to end.
7. **Frame seven, the reader card.** Usefulness sets the price. Nothing new under it; it is a change at the top of the chain, where the user is. The flow reading: everything below now has a reason to exist that the user can see.
8. **Frame eight, next.** Dashed dots: real payments, a persona in your own vault, other sites. The story's last line is always the same question: which of these moves first, and what does it stand on.

That is the whole method. Where is the user, what is new, what does it stand on, where did the movement happen, where did we walk back, where would somebody else hook in, what is next. Seven questions, one picture, and a reader who did not know the business now knows what it is.

## A map inside a map inside a map

Three altitudes of one business. The vault is a dot on the business map; zoom in and it is the anchor of the vault map, at the same place on the evolution axis; the door is a dot on that map; zoom in and it is the anchor of the door map. Up from the top is the market the business sits in, down from the bottom is a key derivation, and the axes and the reading do not change.

The last reading is the one this site is built around. In [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md) every node of a graph is itself a graph, and the altitude you read at decides which vocabulary you are in. Wardley maps have the same property, and drawing it makes the altitude argument precise. Every node on a map is a Wardley map. Zoom into a dot and it becomes the anchor of the next map, and the place it held on the parent's evolution axis is where the child's anchor sits, because the maturity of a thing does not change when you look inside it.

The figure goes three levels down. At the business altitude the anchor is a person who holds something others must read, and the vault is one dot among the site, the meter and the articles. Inside the vault, the anchor is the vault, and the door is one dot among the keys, the CLI and the library. Inside the door, the anchor is the door, and the phone by QR is one dot among the passkey providers. Each child map is what [The passkey opens the vault](the-passkey-opens-the-vault.md) and [Where the vault keys live](where-the-vault-keys-live.md) describe at length; the figure is those articles at three altitudes.

It goes up as well as down. Above the business map is the market it sits in, where the whole of sgit.ai is one dot on somebody else's chain, and that is the map the "does the market exist" section was reading. Which altitude to draw is the first decision, and most of the wrong decisions I have seen on maps were made by drawing the right map at the wrong altitude.

## Two decks

The maps are better presented than read, so there are two decks, both plain pages on this site with the figures in them, and both print to PDF from your browser: open the deck, press the print button or your usual shortcut, and choose "Save as PDF". One slide per page, landscape, nothing uploaded anywhere.

- [Why I love Wardley maps](decks/why-i-love-wardley-maps.md): the explanation, using the maps above as the examples. Twelve slides.
- [Reading one map](decks/reading-one-map.md): the eight frames of the afternoon, one question per slide. How do I think about this, what am I seeing, where do I focus.

## The maps as data

A reader asked today whether collecting these should have been a simple query, and it should have been. Every article on this site has a graph beside it, published at [articles/graphs](graphs.md), and as of this release each graph also lists the article's figures: the file, its URL, the caption, the kind the author gave it, and for a multi-frame figure every frame in order. The Wardley maps are tagged. So "every Wardley map on sgit.ai, with its context" is one read of [articles/graphs.json](graphs.json) and a filter on kind, and the next best-of can be drawn by an agent from that file rather than by rereading the articles. The same change is why the animated maps on this site now have play, pause, step and numbered buttons rather than a loop nobody could stop.

## For the mapping community

There is a serious community around Wardley mapping, and most of what is on this site has not reached it. Three things might be of use there. The maps above are source, not pictures: two were written in Mermaid's Wardley syntax and the rest are drawn from small scripts, so the placements are in a form that can be disagreed with line by line. The evolution axis as a choice, with risk, data and governance as alternatives, is an argument I would like to have again with people who map for a living. And the nested reading, maps all the way down with the dot as the next anchor, is either already a well-known practice I have not seen written up or an extension worth testing on somebody else's business. If you map, and any of that is wrong, that is exactly what the maps are for.

## What this does not claim

- **Positions are judgements.** Every placement on every map here is a claim by the author, not a measurement of anything. The captions and the footers say so.
- **The eleven shifts are a 2022 list.** The talk is linked; the list in this article is the shorter one I use now, and it is not the same list.
- **The alternative-axis post is not quoted.** It was not found while writing this, so the claim that it exists is from memory and the argument is restated, not cited.
- **The two market readings are ours.** They are how we read our own maps, and they can be wrong in the usual way maps are wrong: the layer moves, and the map was drawn before it did.
- **The fractal rule is a practice, not a theorem.** Keeping the child's anchor at the parent dot's position is how we draw it; there are cases, when the inside of a thing is much more or less mature than the thing, where it will be worth breaking.

If you map, and want to compare one of these with yours, or want the maps as data for something of your own, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The maps are from the articles linked beside them, all on this site, and from the three vaults named above; none was drawn new for this piece except the three-altitude figure and the collage. The 2022 talk is [Why Wardley Maps changed how I think](https://open-security-summit.org/sessions/2022/mini-summits/jul/wardley-maps/why-wardley-maps-changed-how-i-think/), Open Security Summit, 14 July 2022, recorded on [YouTube](https://www.youtube.com/watch?v=6gpgnYo6M14). The build change that indexes the figures, and the frame controls, shipped with this article in site v0.7.77.

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#why-i-love-wardley-maps)

### Builds on

- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md) A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.

### Continued by

- [The citizen developer is good news: the spreadsheet grown up, the best briefs ever written, and the handover from explorers to villagers and town planners that makes them last](the-citizen-developer.md) The citizen developer is the spreadsheet grown up: the best briefs ever written, handed to villagers and town planners, carried in versioned vaults.
- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 90 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=90)

**Posting this article on LinkedIn?** The cover is [why-i-love-wardley-maps.jpg](banners/why-i-love-wardley-maps.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html)*
