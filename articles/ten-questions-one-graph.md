# Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open, sgit.ai

> Phil Venables has written down ten questions a CISO's management tool should be able to answer, from where an extra £250k would reduce the most risk to which 100 humans and 100 agents would do the most damage if they went bad. His point is that most tools cannot, and that answering them needs an enterprise knowledge graph, precise risk models and measured data, not an LLM wrapper with dashboards. I agree, and I think the questions show something more: every one of them is a graph question. None can be answered from one part of the company; all of them can be answered from the whole, once the connections are there, and then the answer becomes obvious, the way the end of a whodunit does. Our past work on risk acceptance already has half of this: every risk has a holder, every holder has a boss, every path ends at the board, and there is no deny button, only accept for an interval, fund or fix. So we built a twin of an invented retailer, put its board, risks, holders, processes, systems, suppliers, channels, controls, incidents and 100 humans and agents in one graph, and answered all ten questions on it, each with the part of the graph it came from, its evidence, and the decisions it proposes, traced to the board. It is in a vault you can open.

*Source: <https://newsroom.sgit.ai/articles/ten-questions-one-graph.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open

# Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-19 · [article v1.0.0](versions/ten-questions-one-graph.md) · [newsroom v0.12.137](https://newsroom.sgit.ai/admin/versions.html) · cisographsrisk-acceptancevaultsagentsarticle

***Abstract:** Phil Venables has written down ten questions a CISO's management tool should be able to answer, from where an extra £250k would reduce the most risk to which 100 humans and 100 agents would do the most damage if they went bad. His point is that most tools cannot, and that answering them needs an enterprise knowledge graph, precise risk models and measured data, not an LLM wrapper with dashboards. I agree, and I think the questions show something more: every one of them is a graph question. None can be answered from one part of the company; all of them can be answered from the whole, once the connections are there, and then the answer becomes obvious, the way the end of a whodunit does. Our past work on risk acceptance already has half of this: every risk has a holder, every holder has a boss, every path ends at the board, and there is no deny button, only accept for an interval, fund or fix. So we built a twin of an invented retailer, put its board, risks, holders, processes, systems, suppliers, channels, controls, incidents and 100 humans and agents in one graph, and answered all ten questions on it, each with the part of the graph it came from, its evidence, and the decisions it proposes, traced to the board. It is in a vault you can open.*

Question 9 on the Thistlewood twin's graph: who are the humans and agents with the largest blast radius? Everything the answer does not use has faded. What is left is the plot: three identity admins and five deploy agents, the secrets store and staff sign-on they can reach, the risks those open, customer personal data exposed among them, and the path up to the board.

Thistlewood: ten questions, one graph

Phil Venables' ten questions for a CISO's management tool, answered on one graph: the reply, a tour of the vault, and the vault itself to use.

[you are here1 · The replyTen questions, one graphWhy his questions are graph questions, and how our risk acceptance work and vaults answer them.](ten-questions-one-graph.md)[2 · The tourInside the Thistlewood twinThe ten answers one by one: the plot on the graph, the evidence, and the decisions they propose.](inside-the-thistlewood-twin.md)

3 · The twinThe Thistlewood decision twinPick a question and watch the graph fade to the answer; read every decision up to the board.[Use it](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_32e4f88c6dbc68ae6e2566223008671cc6525ad78ef89482ab4f8b44cb28a07f%3A6v7kyxf4)[His article ↗](https://www.philvenables.com/post/a-cisos-ideal-management-tool)

## In short

- **Phil Venables asks ten hard questions.** A CISO's tool should answer them with evidence, not dashboards.
- **Every one is a graph question.** None can be answered from one part of the company.
- **With the right connections, the answer is obvious.** Fade what is not relevant, and the plot is left.
- **Our risk acceptance work is half of it.** A holder for every risk, a chain to the board, accept, fund or fix.
- **So we built a twin, and answered all ten.** An invented retailer, one graph, a deterministic engine.
- **Every answer ends in a decision.** Held by one person, with an interval, visible all the way up.
- **Vaults, behaviour policies and back-testing fit in.** Decisions recorded, agents' reach measured, models checked.
- **It is in a vault you can open.** With a tour, and this reply.

## Ten questions a tool should answer

Phil Venables' new essay, [A CISO's Ideal Management Tool](https://www.philvenables.com/post/a-cisos-ideal-management-tool), starts from a problem every security leader recognises: many tools for CISOs are old governance and compliance platforms with AI added on top, and in his words some are "quite terrible with the AI sprinkling simply magnifying the horror of the original bad tool". A large company's CISO does not sit in dashboards all day; like a CFO, they need "insights not just data". And because specialist teams keep their own tools, the CISO's tool has to be "an orchestrator and a means of context graph federation".

Then he writes down the acid test: ten questions the tool should answer "with high accuracy, repeatability and evidence". Where would an extra $250k reduce the most risk, and where could $250k be cut with the least harm? What are the five most exposed business processes, and what are the three things to do now for each? Which issues keep recurring, and why? Which accepted risks need revisiting because a competitor had an incident, a regulation is changing, or a control became cheaper? Which controls could be made cheaper and deployed further at the same cost? What are the minimum viable business processes, and the most severe plausible scenario they cannot withstand? Which ten suppliers, down for five days, would hurt customers most? Who are the 100 humans and 100 agents whose going bad would have the largest blast radius, "including the compromise potential of their extended graph of privileges"? And which digital channels, if unavailable, would lose the most revenue over the busiest five days?

His bar for answering them is the right one: "an enterprise knowledge graph, precise risk models, comprehensive real time micro-level data aggregation", "all based on measured reality vs. human self-assessments", with model validation and back-testing. A tool that cannot do that "is likely just an LLM wrapper with some fancy dashboards."

## Every question is a graph question

Look at what each question has to touch. The budget questions need risks, controls, their cost and their coverage. The process questions need processes, the systems under them, the suppliers under those, and the channels and sales above them. The blast-radius question needs every human and agent, what they can reach, and what they can act as. The accepted-risk question needs the acceptances, who made them, until when, and the events that change their assumptions.

Ten questions, one graph. Each of Phil Venables' questions against the parts of the company it has to traverse: risks and holders, controls and cost, processes, systems, suppliers, channels and sales, humans and agents, incidents and causes, acceptances and events. No question is answered by one part alone; all of them are answered by the whole.

No question can be answered from one part of the company. All of them can be answered from the whole, if the whole is connected. That is the point of [the graph companies](the-graph-companies.md): once a graph has the right connections, you remove the nodes that are not relevant, and the answer becomes obvious, like the end of a whodunit. All the clues were there. What changes at the end is that the right ones are connected and the rest fall away.

It is also why Phil's phrase "context graph federation" matters. The specialist teams will keep their own tools and their own vocabularies, and they should. The CISO's tool does not need them to agree on one schema. It needs the edges between their worlds, which is what [fractal semantic graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html) are for: everything connects to everything, and nobody has to share a schema.

## Half of this already exists: risk acceptance

Our earlier work on risk acceptance, in [every risk is already accepted](every-risk-is-already-accepted.md), has most of the structure these questions need. A risk exists the moment the exposure does, so it is always being carried; the only questions are who has accepted it, and until when. There is no deny button, only three doors: accept for a stated interval, fund the work, or fix it. Every risk has a holder, every holder has a boss, and every path ends at the board. Risks are fractal: a board line such as "loss of customer trust" opens into business, operational and technical risks, each with its own holder, down to the configuration that makes it true.

The role risk map in the Risk Graph Explorer vault, from that earlier work. Every risk is assigned to somebody, and every risk reaches the board: each role shows what it holds and what passes through it on the way up.

Read Phil's questions with that in mind and several of them are acceptance questions. Cutting £250k is accepting more risk, so someone has to hold that acceptance. The accepted risks to revisit are acceptances whose assumptions changed. A cheaper control is a reason to reopen an acceptance that was made at the old price. And every answer to every question ends the same way: someone has to accept, fund or fix, and their boss should see it arrive.

## The twin

So we built one. [The Thistlewood decision twin](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html) is an invented retailer at the start of its busiest season. Its board holds four risks. Under them are sixteen business, operational and technical risks, each with a holder and a status, nine of them accepted until a date. The company runs 9 business processes on 16 systems and 12 suppliers, sells through four channels, and has 15 controls with their costs and coverage, 38 incidents in the last year, and 100 identities, 60 humans and 40 agents, with what each can reach and act as. Everything in it is synthetic.

A small deterministic engine answers the ten questions on that graph, and every answer comes with three things: the part of the graph it used, the evidence it rests on, and the decisions it proposes, each with its holder and the chain to the board. On the twin, an extra £250k goes to warehouse backups, hardware keys for staff and a second payment provider, and cuts the expected annual loss by about a million pounds. The £250k cut comes from long log retention and the awareness programme, for about £30k a year of extra risk, which someone has to accept. Twenty-nine of the forty agents can reach systems their behaviour policy says they do not need. The worst plausible scenario the minimum viable processes cannot withstand is ransomware in the warehouse. [The tour](inside-the-thistlewood-twin.md) goes through all ten.

The graph view is where the whodunit happens. Pick a question, and everything the answer did not use fades out; what is left is the plot, from the people or the supplier at one end to the board at the other.

Question 7 on the graph: the minimum viable processes, and the most severe plausible scenario they cannot withstand. Ransomware in the warehouse system, run by one supplier with no fallback, stops pick, pack and ship.

## How our workflow fits

The twin is small, but each step in it is something we already do elsewhere.

From a question to a decision the board can see. Ask; query the graph; see the plot, with what is not relevant faded; decide, accept for an interval, fund or fix, with one holder; record the decision in a vault with its evidence and hash; back-test the model against what happened, and recalibrate. Underneath each step, the work it comes from: fractal semantic graphs, the whodunit view, risk acceptance, sgit vaults, measured evidence.

- **Each decision is a record.** In the twin, every proposed decision is a file in `decisions/`, with the question, the answer, the evidence, the holder, the door and the interval. In practice each material risk deserves a vault of its own, the evidence pack of the decision, readable by each audience with its own key.
- **Agents are in the graph, with their policies.** Phil's question 9 asks for 100 agents as well as 100 humans. When every agent has an [Agent Behaviour Policy](governs-enforces-attests.md), its mandate is data, so its reach can be compared with it, which is how the twin finds the 29 agents that can reach beyond what they need.
- **Measured, then back-tested.** Every answer lists its sources, and in the twin they are measured ones: the access review, supplier status history, incident tickets, contracts, sales logs, control configuration. The back-test compares the model with last year's incidents and shows where it is wrong: it under-estimates supplier bank fraud by about half. That is the check Phil asks for, and it is what keeps the answers honest.
- **Federated, not merged.** The twin's graph is one file because it is a twin. In a real company each part would stay in its specialist tool, connected by edges, which is the federation Phil describes.

## What this does not claim

- **The twin is invented.** Thistlewood Retail, its people, agents, suppliers and every number are synthetic.
- **The model is simple on purpose.** Base exposure reduced by controls in proportion to their coverage; a real one needs the measured data Phil asks for.
- **It answers the questions; it is not the tool.** It shows what an answer looks like when it comes from a graph.
- **Phil's questions are his.** The reading of them as graph and acceptance questions is mine.

## Where this comes from

Phil Venables, [A CISO's Ideal Management Tool](https://www.philvenables.com/post/a-cisos-ideal-management-tool), 19 October 2026, read that day; the quotations are from it. The earlier work: [every risk is already accepted](every-risk-is-already-accepted.md), the [Risk Graph Explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/views/index.html) and [Risk Acceptance Office](https://sgit.ai/demos/vaults/risk-acceptance/index.html) vaults, and [fractal risk registers](https://graphs.sgit.ai/v1/docs/fractal-risk-registers.html). Related: [the graph companies](the-graph-companies.md), [governs, enforces, attests](governs-enforces-attests.md), [inside the Thistlewood twin](inside-the-thistlewood-twin.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Graphs & knowledgeAgents & policy[This article as a graph →](graphs.md#ten-questions-one-graph)

### Builds on

- [The graph companies: many of the most valuable companies in the world are graphs, of links, people, products, payments and ontologies, and the graphs never scaled for everyone else because they were built to lock in](the-graph-companies.md) Four of the ten most valuable companies are graph companies. Graphs never scaled for everyone else because they were built to lock in. Now they can.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes](inside-the-thistlewood-twin.md) The ten answers on an invented retailer's graph: where £250k goes, what keeps recurring, who has the largest blast radius, and the 29 decisions to the board.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.

### Continued by

- [Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes](inside-the-thistlewood-twin.md) The ten answers on an invented retailer's graph: where £250k goes, what keeps recurring, who has the largest blast radius, and the 29 decisions to the board.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 217 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=217)

**Posting this article on LinkedIn?** The cover is [ten-questions-one-graph.jpg](banners/ten-questions-one-graph.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/ten-questions-one-graph.html)*
