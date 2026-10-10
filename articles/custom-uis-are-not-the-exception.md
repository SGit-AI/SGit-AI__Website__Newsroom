# Custom UIs are not the exception: the inbox in 2026, where every message has its own universe, sgit.ai

> Following up is harder than doing the work, because every person has a different context and the thread you share hides its own structure. This article weaves the site's threads into one argument. Every message has a graph, with altitudes from the block to the contact. Email is a medium, so a message is designed for the recipient's moment, not the sender's thread. A custom interface per message or moment is not an exception; it is how interfaces now get made, each one commoditising the next. Ten agents and one human built more than a dozen of them in eight days. The future of email is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph. And an interface is an agent surface, so it gets a policy.

*Source: <https://newsroom.sgit.ai/articles/custom-uis-are-not-the-exception.html> · site v0.7.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Custom UIs are not the exception: the inbox in 2026, where every message has its own universe

# Custom UIs are not the exception: the inbox in 2026, where every message has its own universe

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-01 · updated 2026-10-02 · [article v1.6.1, 8 versions](versions/custom-uis-are-not-the-exception.md) · [site v0.6.29](https://sgit.ai/admin/versions.md) · inboxemailcustom-uifractal-semantic-graphsvault-appsappend-lanesemail-fswardley-mapsagentsriskmandatearticle

***Abstract:** Following up is harder than doing the work, because every person has a different context and the thread you share hides its own structure. This article weaves the site's threads into one argument. Every message has a graph, with altitudes from the block to the contact. Email is a medium, so a message is designed for the recipient's moment, not the sender's thread. A custom interface per message or moment is not an exception; it is how interfaces now get made, each one commoditising the next. Ten agents and one human built more than a dozen of them in eight days. The future of email is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph. And an interface is an agent surface, so it gets a policy.*

Every message has a graph, and the graph has altitudes: the contact, the company, the conversation, the message, the block inside the message. Below, the Wardley strip that governs the interfaces built on it: a new interface is genesis; the second time it is custom; the fifth time it is a product you just send; eventually it is a commodity you stop noticing. A custom interface per message is not an exception. It is the left edge of that strip.

**Where this comes from.** A voice memo on 1 October 2026, recorded after a week in which an agent built a drag-and-drop page for a set of PDFs I owed somebody, and I realised the page was the point. The article weaves that memo together with the threads this site has been pulling for months. Links go to the articles, vaults and sites where each thread was worked out. Revised on 2 October after a review by the RiskMandate agent team, who pointed out that the earlier draft described one page and one afternoon when the page was one item in an eight-day stream; their timeline, team map and mock-ups appear below. Counts come from the vaults' commit history; no contact is named and no message is quoted.

## In short

- **Following up is the hard part.** Not the work: the keeping of context for every person in every conversation, each of whom has a different environment, a different history with you and a different thing they need to do next.
- **Every message has a graph.** Actions, questions, statements, decisions, concepts. Extract them and a thread becomes a graph, and the graph has altitudes: the block, the message, the conversation, the company, the contact. That is a [fractal semantic graph](introducing-fractal-semantic-graphs.md), and this is where the idea was always going.
- **Email is a medium.** The design brief for a message is the recipient's moment when they open it, not the sender's thread. Send what they need, in the shape they need it, and let the thread go. HTML means the shape can be anything.
- **Custom interfaces are not the exception.** They are how interfaces get made now, exactly as [Wardley maps](https://sgit.ai/demos/vaults/strategy-maps/index.md) describe anything getting made: you are always either building a new one or recycling one you built before, and each one you build is a thing you will next time just send.
- **The to-do and the place to act are one page.** The worked example is a page that lists the PDFs still owed and gives a place to drop them, through a [vault's append lane](https://sgit.ai/api/append-lanes.md). No context switch, no second tool, no email.
- **It compounds, and it has to be governed.** Each interface teaches the agent how its user wants to work. Automation creates more work than an inbox can hold, so the interface becomes the prioritisation. And an interface is an agent surface, so it gets a [policy](https://riskmandate.ai/abp.html) like any other.
- **It is the beginning of what email becomes.** The transport stays, SMTP or a vault's append lane. Above it, the message is a node in a graph, shaped for each reader's moment: one word or the whole map, in their language, at their urgency. The human and the agents improve those shapes in a loop.
- **The future of email** is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph. No install on day one; a plain email still works. The pieces are published.

## The follow-up problem

Here is the problem as it feels from the inside. I am in conversations with dozens of people and a growing number of agents. Each person has their own context: what they know about the work, which tools they use, what they agreed to last time, what they are waiting on from me and what I am waiting on from them. The medium we share is, mostly, an email thread, and a thread is a terrible place to keep any of that. It holds a huge amount of information, and the information has a structure the thread does not show: actions somebody took on, questions that went unanswered, statements of fact, decisions that were made in a subordinate clause three replies ago, ideas that were good and went nowhere.

The problem gets worse the moment vaults and agents enter. When I create a vault for somebody, that vault is a whole new universe: its own files, its own activities, its own flows, its own things to do, none of which fit in a thread. When I write an [Agent Behaviour Policy](https://riskmandate.ai/abp.html) with somebody, their environment is different from the last person's: one is on Gmail, one lives in Claude, one builds in Lovable, one has a Workspace admin and one does not, and the policy that is honest for one is wrong for another. The [six agents on one inbox](six-agents-one-inbox.md) made this concrete: what broke first was not a permission but the follow-up, because the reader agent that must never reply had to reply when the message was from me, and nothing in the thread said so.

So the question is not how to do the work. It is how to follow all of this up, for every person, in a way that makes sense to that person.

## Every message has a graph

The thing I already do, in one of the interfaces this site runs on, is to take every email and every message and extract the structure that was always there: the actions, the questions, the statements, the decisions, the concepts. Do that and a thread stops being a thread. It becomes a graph.

And the graph has altitudes. There is a graph for the block inside a message, the fenced `decision` or `answer` or `status` that [Email-FS-lite](https://sgit.ai/docs/append-lane-messaging.md) already uses so that agents can read each other's asks without parsing prose. There is a graph for the message. There is a graph for the conversation. There is a graph for the company the person works for, and for the contact themself, and for the topic, the question, the initiative, the thing to do that spans all of them. Each altitude has its own nodes and its own verbs, each is navigable on its own, and each points down into the one below and up into the one above.

That is exactly what [the introduction to fractal semantic graphs](introducing-fractal-semantic-graphs.md) described, with its test worked from a risk register down to a TCP packet and its eleven altitudes across seven live vaults. What I did not say clearly enough then is that the inbox is where the idea bites first. The inbox already has the altitudes; we started drawing them. The [company X-ray](https://sgit.ai/demos/vaults/company-xray/index.md) plan does it for a company's documents, every finding tied to its evidence. The [Evidence Dispatch](https://sgit.ai/demos/vaults/evidence-dispatch/index.md) does it for news, with a claim ledger and a graph of declared relationships. The inbox is the same move, pointed at the one data set every working person already has.

## Email is a medium, so design for the recipient's moment

Once the graph exists, a different question becomes possible. Not "what do I reply?" but: when this person opens this message, what is their context, what do they need, and what do I want them to do?

That is a design brief, and the thread fails it in every way. The way email's interface works, the recipient reads the newest text, then scrolls down to reconstruct the context, past five layers of quoted replies in different colours and a reply typed into the middle of somebody else's paragraph. By the time a conversation has a dozen turns the thread is pointless. Everything relevant in it could be captured, actions, open questions, decisions made, the one thing you are asking for now, and shown in an interface that fits.

Two consequences follow, and the second one is the strange one. The first: send the summary, not the thread. Send the person a page shaped for them: here is where we are, here is what was decided, here is the one thing I need from you, here is where to do it. Fold the history underneath for anyone who wants it. The second: the recipient still holds the thread you sent them, in their inbox, so if they did not reply, you can rewrite the history of the email you sent. Not change what happened, but re-present it: a new message that carries the whole state, so the old thread is no longer what they have to read.

We have done this before, in another domain, without calling it that. The [story vault](future-of-news-story-vault-not-paywall.md) argues that an article is one projection of a graph, for one audience, at one moment, and that the vault, not the article, is the record. A message to a person is the same thing: a projection of the conversation graph, for one reader, at the moment they open it. The [connector twin](connector-twin-before-you-deploy-an-agent.md) makes the same point from the agent's side: what matters is not the raw stream of calls but what the agent actually saw, replayed into the view it had. A thread is the raw stream. The projection is what somebody can act on.

And we have HTML. Every one of these projections can be an interface: a card, a checklist, a form, a board, a page. The picture below is one we now send in first emails instead of an explanation, because a reader opening a cold email has about a minute, and a minute is enough for one picture, one link and one easy ask.

An Agent Behaviour Policy in one picture, as it goes out in a first email: what the agent can do, what you asked it to do, the gap between them, what actually stops the rest, and who accepts the gap until when. No data in it; it is the explanation, shaped for the recipient's minute.

## It starts with the user

One user, many interfaces, each shaped for the moment: Now cards on a phone between meetings, a voice prompt behind an encrypted link on a walk, boards at a desk, a contact page, a drop zone, Gmail drafts the human sends, a chat with an agent, and the email itself. Some threads are agentic, some deterministic, some information, some for thinking. The map starts at the user and works down to the components.

The interfaces in this piece have one thing in common: they start with me. Not with the tool, the data model or the agent that built them, but with how I want to work at that moment. Between meetings I am on my phone and need two things to do, blockers first. On a walk I want to talk, so the brief comes as a voice prompt behind an encrypted link and the summary goes back to the agent. At a desk I want the board: who is waiting on whom. When I owe somebody a document, I want the list of what I owe and the place to drop it, on the same page.

So there is not one UX. There are many, one per moment, and each is a mix of threads: some agentic, where an agent drafted it; some deterministic, computed from the vaults and the same every time; some purely informational; some for thinking. Mapped the Wardley way, the map starts at the user and works down to the components, not the other way round.

This is what human-in-the-loop looks like when it works. The human is not a bottleneck approving everything; the human is made faster, because the surface in front of them matches their focus right now, and every decision they make is one tap that writes a record.

The test is simple, and it is the measurable version of this article's title. Every time I ask an agent in chat for something a page could have shown me, that is the next interface. Ask the same question twice and an agent builds the card.

## Custom interfaces are not the exception

The instinct, trained by twenty years of software, is that a custom interface is expensive, so it is reserved for the product and everybody else gets the generic one. The inbox, the ticket, the form. The memo's claim is that this is now backwards: a custom interface per message, per thread, per topic, per question is not an exception. It is how interfaces get made.

The reason it is not madness is the way [Wardley maps](https://sgit.ai/demos/vaults/strategy-maps/index.md) describe anything getting made. Everything moves from genesis, through custom-built, to product, to commodity. When an agent and I build a new interface for a thing, we are at genesis. The second time the same shape is needed, we recycle it, and it is custom. The fifth time, it is a product: a thing with a name that I just send. Eventually it is a commodity, something so ordinary that I become a user of it and stop noticing it exists. At any moment I am doing one of two things: developing a new interface, or recycling one that already exists. And every new one I develop is a thing I am commoditising for next time.

It has already happened on this site, without anyone deciding it should. In a chat session, an agent started using cards to say "here is the thing that matters, here is the most important piece". The cards were a way of thinking. Then they became a way of communicating between sessions: we send screenshots of what one session built to the next one as the brief. Then they ended up in an email. The [board vault](https://sgit.ai/demos/vaults/board/index.md) began as a way to keep this site's own tasks and became a kanban app the site renders from, cards as files, five columns. The [voice debrief](https://sgit.ai/demos/vaults/voice-debrief/index.md) is four interfaces in one vault, from raw recording to structured debrief, each built because the previous one was not enough. The [nine vault-app proofs of concept](https://sgit.ai/demos/vaults/vault-app-pocs/index.md) are the genesis end of the strip, kept so the next builder does not start from nothing. The [deployment documentation vault](https://sgit.ai/demos/vaults/deploy-docs/index.md) updates with a push and no site deploy, which is an interface for one reader, the person deploying. And the [Kit Bag](https://sgit.ai/demos/vaults/kit-bag/index.md) plan this week put the thesis in a sentence for software generally: the open-source app is the starting point, an agent customises it per person, and the vault is the distribution channel. The [agent as webmaster](https://sgit.ai/demos/vaults/agent-webmaster/index.md) plan is the same thesis for a small business's website: changed by asking.

None of these was an exception. They were the strip, moving.

## The page that is both the to-do and the place to act

Here is the example that made me record the memo.

One of my current jobs requires me to produce and share a number of PDFs and images with a particular session: documents it needs, in a sequence, over a few weeks. The session lives in a vault, and the vault has an [append lane](https://sgit.ai/api/append-lanes.md): a write-only channel anyone with the token can drop a file into, which the vault's owner drains and processes. A vault app can send a file back to its vault two ways, directly or as an append message, and for the main vault the append message is the better one, because it goes to a queue and gets processed in order rather than landing in the tree.

So I asked for an interface, and an agent built one in an afternoon. The page does two things. It lists the PDFs that are still missing, which is to say it is my to-do list, exact and current, for this one job. And it gives me a place to drop them. I open the page, I see precisely what I owe, and I do it, there, without changing context, without opening another tool, without an email. The drop goes down the lane; the list shortens.

Think about how much that does. The to-do and the place to act are one page. The page knows my context because it was built for exactly this job. Nothing else is on it. And the "place to act" could have been anything: dropping PDFs this time, but equally answering three questions, ticking a set of boxes, choosing between two designs, writing a paragraph, approving a decision. Those are the blocks, the same `decision`, `answer` and `status` blocks that agent messages carry, except rendered as an interface for a human. The question the agent is answering when it builds the page is: what is the best interface, HTML in most cases, for this person to give me this feedback? The cheap end of that question is the [chat on a static site](chat-on-a-static-site.md), a local matcher and no server at all. The rich end is a vault app with the [bridge](https://llms.sgit.ai/) that lets it call a model without holding a key, as the [RiskMandate vault](https://sgit.ai/demos/vaults/risk-mandate/index.md) does. Both are the same move.

Two of the interfaces, as mock-ups with placeholder names. Left: the Now card on a phone, computed from the vaults, blockers first, at most two actions, one tap to decide. Right: the sibling of the PDF drop page in the RiskMandate workspace, a list of what is owed that is also the drop zone; each drop goes down the append lane, an agent files it, the row disappears. The user never asks "what do I owe?" in chat. The page answers before the question, and the answer is also the button.

The drop page has a sibling, built from the same pattern in the RiskMandate workspace: a list of the people whose documents are still owed, fed by a view of the CRM, where each row is also the place to drop. Each card started as a question in chat. When the same question came up twice, an agent built the card.

## Eight days, not one afternoon

The workflow as it happened, 25 September to 2 October 2026. Every column is a day; each line is something that now exists and is in use: an agent, a vault, an interface release, a workflow. The counts at the bottom are from the vaults' commit history. The PDF drop page is one item in this stream.

The drop page was built in an afternoon. That is true, and it undersells what happened. It was one item in a stream.

In eight days, from 25 September to 2 October 2026, a small team of agents and I went from an empty vault to a working way of doing outreach: the agents and their accounts; the connections to email; an inbox agent that drafts and another that sends only what I approve; a CRM in its own vault with one folder per person; several versions of the CRM's interface, sixteen releases in all; vault apps; voice prompts delivered as encrypted links; phone cards; boards; a channel to my LinkedIn data; the first Agent Behaviour Policy we wrote for somebody else's agent; and a rotation of four vault keys in a single day after an agent's own leak check caught an exposed key. Around 230 commits and more than 550 messages between agents, all in files, all versioned.

None of it was planned as a product. Each piece was the answer to "this is how I want to work now", built by whichever agent owned that part of the job. The speed is the point: when an interface costs an afternoon, you stop asking whether it is worth building and start asking which moment it is for.

## Why it compounds

The speed matters, and it is not the point. Three other things are.

**Every interface you build makes the next one better.** Not metaphorically: the page is a file in a vault, the next job that needs a drop list starts from it, and the strip moves one step right. Nothing is reinvented. This is the [seven vaults, one method](seven-vaults-one-method.md) lesson applied to interfaces: do a thing seven times and you have a method, and the method is faster and safer than the first attempt by a distance.

**Each one teaches the agent how its user wants to work.** When I ask for a drop page rather than a form, when I want the missing items at the top and the done ones folded away, when I prefer to approve by clicking and explain by voice, I am discovering how I want to work, and the agent is learning it with me. That reduces my cognitive load, which is the humane reason to do it. It is also the economical reason: the agent can ask itself what the best way is for this person to give it what it needs, and build that, rather than making the person adapt to a generic tool.

**Automation creates more work than any inbox can hold.** This is the one people do not see coming. Once agents are running, they produce tasks, activities and asks faster than a person can read them, because a model will simply execute. The inbox, which was already failing as a place to hold context, fails completely as a place to hold volume. So the interface stops being a convenience and becomes the prioritisation: the filter, the index, the board. I have kanban boards for this. I have an interface where a model inside the vault, with access to the CRM, answers questions about who said what and what is owed. When a feature is missing, I add it; when one is unused, I remove it. The interface is customised to how I work because it was built from how I work, and at some point it stabilises and I am simply a user of a tool we did not have a month ago.

## This is the beginning of what email becomes

One message, many shapes. The message is a node in a graph; each reader gets the shape their moment needs: one word, a card with two actions, a familiar email, a three-minute voice prompt, a board, or the whole graph. The shape adapts to urgency, focus, language and culture, the relationship, and whether the reader is a person or an agent reading for one. Placeholder names.

Step back and look at what all of this is. I am still using email. The agents in this article talk to each other in messages with a sender, a recipient, a subject and a body, one file each, and it is a very efficient way to work. Some of those messages go out over SMTP. Some go down a vault's append lane. Same message, same file. The transport is a detail, and it is not going anywhere.

What is changing is everything above the transport. The message is a node in a graph, and each reader gets it in the shape their moment needs. Sometimes the right shape is one word. Sometimes it is a card with two buttons, a familiar email, a three-minute voice prompt, a board, or the whole graph. The medium is as simple as the moment allows and as complex as the situation requires, and the second half of that sentence matters as much as the first: the world is complex, and squeezing a complex situation into a short email loses exactly the part that mattered.

The shape adapts to more than the device. It adapts to urgency, a blocker now or context for later. To focus: between meetings, on a walk, at a desk. To language and culture: their language first; direct or indirect; a call or an asynchronous reply. To the relationship, because a first contact reads differently from somebody I have worked with for years. And to who is reading, because more and more often the reader is an agent reading on somebody's behalf.

This is where fractal semantic graphs stop being a theory. Every node opens into its own graph: the block into the message, the message into the thread, the thread into the company and the person. Each reader, person or agent, stops at the altitude they need. The context does not have to be squeezed into the email, because it travels with it as the graph. Earlier I called email a medium, and in the sense that matters to a sender it still is: a reply by email is the easiest thing to ask of most people, and very often email is the right view. But the thing that carries the meaning has moved. The graph is the medium. Email, cards, voice and boards are views of it.

Every tap teaches the next interface. A moment gets a shape; the shape gets a decision; the decision is written to the vault as a record; the record shapes the next version. Interfaces mature at different speeds: the drop zone is new and still changing, the Now card is reshaped often, the who-is-waiting board has settled, and the email is a commodity you just send. Positions indicative.

And the views keep improving, because the human and the agents work in a loop. A moment, "this is how I want to work now", gets a shape. The shape gets a decision: one tap, one reply or one spoken answer. The decision is written to the vault as a record, and the record shapes the next version of the interface. Some interfaces are new and change every few days, some have settled, and some have become so ordinary that we just send them. The UX does not ship once. It evolves with the person.

Better models make the loop faster: more refactoring of content, better shapes, more done inside each narrow mandate. The structure is what lets them: the files, the records, the scoped roles, a policy for each agent. Without it, a better model just produces more email faster.

## The future of email

"The future of email" has been announced before, by Wave, by AMP for Email, by Slack, by Hey, and the inbox outlived every one of them, because the inbox is the lowest common denominator everybody already has. Any version of the claim that needs the recipient to install something, or to see HTML that mail clients sandbox, dies the same way. So here is the version that does not need that.

Two things are true in 2026 that were not true when those earlier claims were made. The first is that more and more messages are read by an agent on somebody's behalf. Gmail, Apple Mail and Outlook now summarise and reshape mail at the receiving end, whether the sender wanted it or not. So the per-reader shape no longer depends on the sender guessing the recipient's moment. The recipient's own agent knows the moment, and renders for it. The second is that those agents are reshaping badly, because the message gives them nothing to work with: a thread of quoted replies with the decision in a subordinate clause, which they summarise by guessing. That is the problem [the token bill article](token-bill-nobody-is-sending.md) found for websites: agents fetching unstructured pages and paying for it in tokens and in errors. The answer there was publisher-served structure. The answer here is the same, one word changed.

**The future of email is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph.** The message carries its actions, questions, decisions and status as blocks, so the agent reading it can render one word, a card or the whole graph with fidelity instead of inference. Email-FS is that structure. [Agent Contact](https://sgit.ai/docs/agent-contact.md) is how two agents find each other's keys to exchange it. The vault is where the graph lives when the message is only a view of it. And none of it asks the recipient to install anything on the first day, because a plain email still works; it asks their agent to recognise the structure when it is there, and to fall back to the text when it is not.

It can fail in two ways. If recipients' agents never learn to read sender-served structure, or if senders never bother to send it, the inbox stays a thread and the earlier announcements will have one more companion. The pieces are published, and the next year will show which way it goes.

## Who builds them

Ten agents and one human, each with a scoped role, as of 2 October 2026. Most share the same reach, one account and many tools, and differ in mandate. Each writes only its own folders and talks to the others in files. Six already have a written Agent Behaviour Policy. Names generalised; no keys, contacts or message content shown.

Readers will ask who builds all these interfaces. Behind them is a team of ten agents with narrow jobs and one human who decides. One builds the interfaces, one reads the inbox and drafts, one sends only what I have approved, one keeps the CRM, one researches people one at a time, one runs the others on a schedule, one holds my LinkedIn data, one is about to become a WhatsApp channel. They talk to each other in files, each writes only its own folders, and six of them already have a written Agent Behaviour Policy, including the WhatsApp agent, whose policy was written before any action was switched on.

The work flows in one direction: a memo from me, the CRM routes it, the briefs agent writes, the CRM registers it, the mailbox agent drafts, I approve, the inbox agent sends, replies land in the CRM, and the next interface is built for whatever got stuck. That last step is the whole article in a sentence.

## An interface is an agent surface, so it gets a policy

One more thread, because without it this is a story about convenience, and it is not. The same rule runs the team above: the smaller and clearer the mandate, the more an agent can be trusted to do on its own. A page that drops files into a vault, answers questions on my behalf, or lets a model read my CRM is an agent surface. It has a grant: what the page can reach. It has a mandate: what it is for. There is a delta, and there are barriers, and most of them are expectations rather than controls, exactly as [the Kit Bag policy](https://sgit.ai/demos/vaults/kit-bag/index.md) found for a browser extension and [The ultimate insider](ultimate-insider-three-collisions.md) argued for agents generally.

So every custom interface gets what every agent gets. It runs against a vault, so the record is append-only and the host cannot read it. It uses a read key or a lane token, never a vault key, so the worst it can do is bounded by the credential it holds. Its calls to a model go through a bridge that holds no key. And it has a policy, short, because the interface is small, that says what it can reach, what it is for, and what stands in the way. Different people's environments, Gmail or Claude or Lovable, produce different policies, and that is fine; the point is that the policy is written, and that the customising agent knows what it must not loosen.

## What this looks like from here

An inbox where every thread has folded into its actions, decisions and open questions, at the altitude you need, and the thread itself is history you can open if you want to. Messages designed for the moment the person opens them, each one a projection of the conversation for one reader. Email as one view of a graph, chosen when it is the right one, and a card, a voice prompt or a board when those are. A library of interfaces growing in a vault, each born in a chat, reused in a session, sent in an email, and eventually so ordinary it has a name and is never built again. Agents that learn how each person wants to work and build for that. And a policy on each of them, because the thing that makes this powerful is the thing that makes it dangerous.

Most of this exists today, in pieces: the graphs, the lanes, the vault apps, the agents, the policy method, the boards, the contact pages, the Now cards, the drop zones, the voice prompts behind encrypted links. The inbox that joins them is being built now, out of those pieces, and it is being built the way everything in this article was built: one custom interface at a time, each one the answer to a question I asked in chat that a page could have answered, none of them an exception.

## Threads woven here

- [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md), the altitudes and the grammar.
- [Six agents, one inbox](six-agents-one-inbox.md), where the follow-up broke before the permissions did.
- [Append lanes](https://sgit.ai/api/append-lanes.md) and [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md), the write-only channel and the Email-FS-lite blocks; [Agent Contact](https://sgit.ai/docs/agent-contact.md), agents writing to agents.
- [The future of news is the story vault](future-of-news-story-vault-not-paywall.md), the article as a projection for one audience at one moment.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md), what the agent saw, replayed.
- [Chat on a static site](chat-on-a-static-site.md), the cheapest custom interface.
- [Seven vaults, one method](seven-vaults-one-method.md), how repetition becomes method.
- Vaults: [the board](https://sgit.ai/demos/vaults/board/index.md), [voice debrief](https://sgit.ai/demos/vaults/voice-debrief/index.md), [vault app proofs of concept](https://sgit.ai/demos/vaults/vault-app-pocs/index.md), [deployment docs](https://sgit.ai/demos/vaults/deploy-docs/index.md), [RiskMandate](https://sgit.ai/demos/vaults/risk-mandate/index.md), [strategy in seven Wardley maps](https://sgit.ai/demos/vaults/strategy-maps/index.md), [Company X-ray](https://sgit.ai/demos/vaults/company-xray/index.md), [Kit Bag](https://sgit.ai/demos/vaults/kit-bag/index.md), [Agent as webmaster](https://sgit.ai/demos/vaults/agent-webmaster/index.md), [The Evidence Dispatch](https://sgit.ai/demos/vaults/evidence-dispatch/index.md).
- [The token bill nobody is sending](token-bill-nobody-is-sending.md), publisher-served structure, the same answer one word changed.
- [The ultimate insider](ultimate-insider-three-collisions.md), why the surface needs a policy; [RiskMandate.ai](https://riskmandate.ai/) for the policy itself.
- Sites: [graphs.sgit.ai](https://graphs.sgit.ai/), [llms.sgit.ai](https://llms.sgit.ai/), [twins.sgit.ai](https://twins.sgit.ai/), [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/).

*Drafted from a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session. Revised on 2 October 2026 after two reviews by the RiskMandate agent team's CRM agent, the second on the founder's direction, whose timeline, team map, mock-ups and the two figures on what email becomes are the figures with placeholder names; the counts in them come from the vaults' commit history and files.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Graphs & knowledgeAgents & policy[This article as a graph →](graphs.md#custom-uis-are-not-the-exception)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [A chat box on a site with no server, the plan, and the trade it makes](chat-on-a-static-site.md) sgit.ai has no server, so its directory chat runs a local matcher by default, takes your own key as an opt-in, and leaves the vault bridge unbuilt.
- [Seven vaults, one method](seven-vaults-one-method.md) Publishing seven encrypted vaults in a fortnight produced a method, and every rule in it exists because something went wrong first.
- [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md) AI answer engines pay to read the web as HTML; a publisher who serves markdown, dates, hashes and a typed graph saves them tokens and should get a share.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.

### Continued by

- [Liquid content needs water: liquefy the journalist's notebook, not the finished product](liquid-content-needs-water.md) A reply to FT Strategies on liquid content: the water is the reporting, so liquefy the journalist's notebook, keep the writing theirs, and pay per use.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md) End an email reply with the state of the thread for this reader, not the quoted wall: decided, open, next, who is on copy, with links to the record.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Thinking with a Wardley map](collections/wardley-maps.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [custom-uis-are-not-the-exception.jpg](banners/custom-uis-are-not-the-exception.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/custom-uis-are-not-the-exception.html)*
