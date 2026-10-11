# An open AI governance framework, and what its licence let us build, sgit.ai

> Jan van Dijke published the AI Baseline Control Framework on 2 October 2026, twenty controls for organisations that deploy AI, in five categories and three types, each with why it matters and how to put it in place, mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act, and licensed CC BY-SA 4.0. Part one is about the framework, what it does well, what it adds that the three it maps to do not, and why an open licence matters more for a control framework than for most documents. Part two is what the licence made possible on the day: the CSV export converted into a semantic graph with an ontology, a SKOS taxonomy, JSON-LD and Turtle, eighty hyperlinked documents and a database that runs in the browser, joined to the EU AI Act's own text, published as a vault under the same licence, with a fractal graph view that walks from the framework down to a paragraph of law, and the six things the graph found that the CSV does not say.

*Source: <https://newsroom.sgit.ai/articles/ai-baseline-control-framework.html> · sgit.ai v0.7.61 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An open AI governance framework, and what its licence let us build

# An open AI governance framework, and what its licence let us build

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.0.1, 2 versions](versions/ai-baseline-control-framework.md) · [sgit.ai v0.6.86](https://sgit.ai/admin/versions.md) · ai-governanceai-bcfeu-ai-actnist-ai-rmfiso-42001open-licencecreative-commonssemantic-graphsfractal-semantic-graphssqlitevaultsarticle

***Abstract:** Jan van Dijke published the AI Baseline Control Framework on 2 October 2026, twenty controls for organisations that deploy AI, in five categories and three types, each with why it matters and how to put it in place, mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act, and licensed CC BY-SA 4.0. Part one is about the framework, what it does well, what it adds that the three it maps to do not, and why an open licence matters more for a control framework than for most documents. Part two is what the licence made possible on the day: the CSV export converted into a semantic graph with an ontology, a SKOS taxonomy, JSON-LD and Turtle, eighty hyperlinked documents and a database that runs in the browser, joined to the EU AI Act's own text, published as a vault under the same licence, with a fractal graph view that walks from the framework down to a paragraph of law, and the six things the graph found that the CSV does not say.*

The framework on one page: twenty controls in five categories, coloured by type, with the frameworks each one cites. The Access column cites none of the three. Built from the framework's CSV export, CC BY-SA 4.0.

Jan van Dijke [introduced the AI Baseline Control Framework](https://aibcf.org/) on LinkedIn this week with a sentence that explains most of what follows: he could not find a practical AI governance framework for the organisations he works with, so he wrote one. Twenty controls, five categories, free and open, each with why it matters and how to put it in place, mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act.

I asked three questions under the post: did you use semantic graphs, is there an API to consume it, and what formats is the data published in? His answer was honest and useful: "for now there is only Export as CSV on https://aibcf.org/controls/ on the top right. Good suggestions!"

That answer turned out to be enough, because of the licence on the page. This article has two parts. The first is about the framework: what is good about it, what it brings, and the power of the licence it was published under. The second is what we built from it on the same day, and what that showed.

## Part one: the framework

### What is good about it

**It is written for deployers.** The site says who it is for in its first paragraph: organisations that deploy (use) AI, rather than those that build it. Much of what is written about AI governance is aimed at providers, model builders or regulators. The organisation that has bought three AI products, given a team a coding assistant and wired an agent into its ticketing system is the much larger group, and it has had less written for it. AI BCF names CISOs, IT directors and AI officers as its readers, and it reads like it was written for them.

**Twenty controls is a number a person can hold.** Five categories, Govern, Comply, Register, Access and Track, cover AI governance from policy down to the day-to-day tracking of deployed systems. Each control is one sentence. A board can read the list in a meeting, and a security team can audit against it.

**The three types make it proportionate.** Ten controls are Baseline and apply to every organisation that uses AI. Six are Tier II, optional depth for organisations with more mature governance or more exposure. Four are Trigger controls, which apply only when a stated condition is true: AI in decisions about hiring, firing, promotion, pay or access to services; a public body using AI in those decisions; AI systems that act autonomously with their own access. If the condition does not hold, the control does not apply. That is the shape a framework needs if it is going to be used by organisations of very different sizes without telling the small ones to do everything.

**Every control says why and how.** The why is the argument a control owner will need when somebody asks why the control exists. The how is a practical next step, written for a person who has to do it on Monday. Frameworks often give the what and leave the why to a consultant.

**It is mapped, and the mapping is in the data.** Each control lists the clauses of the NIST AI RMF, ISO/IEC 42001 Annex A and the EU AI Act it corresponds to, in a Sources column, with fifty-four distinct clauses cited fifty-nine times. Where there is no equivalent, it says so.

**It is current.** The home page says it reflects EU law as of October 2026, the AI Act as amended by Regulation (EU) 2026/1744, and that it is not legal advice. Both statements are the right ones to make.

**The site practises what it governs.** It sets no cookies, runs no analytics and loads no third-party scripts or fonts, and it says so on a short privacy page. A governance framework published from a site that tracks its readers would have been a small contradiction; this one is not.

**And it can be exported.** The CSV on the controls page has one row per control, nine columns, the sources in one of them and a URL per control. There is also a one-page PDF overview. A CSV is the least glamorous format there is, and it is what made part two possible.

### What it brings: the Access category

The most interesting row in the crosswalk is the empty one. The four Access controls cite nothing in the NIST AI RMF, ISO/IEC 42001 or the AI Act. The framework says so in its own Sources column: "No equivalent in NIST AI RMF, ISO/IEC 42001 or the EU AI Act."

- **AC.1** An access review is conducted before an AI system inherits users' access rights.
- **AC.2** AI systems with separate access rights are given a named identity, and these rights are limited to a documented scope.
- **AC.3** Each autonomous AI system is assigned a named owner who is accountable for its actions.
- **AC.4** Access rights for AI systems are granted according to the organisation's access control model.

These are not exotic. They are what an identity and access management practice would ask of any new account, and the framework's author works at an identity and access management consultancy. Their absence from the three big references says something about where those references come from: risk management, management systems and product regulation, rather than the operational question of what an AI system can reach once it is switched on. The category description on the AI BCF home page puts it in one line: AI that acts with its own credentials or autonomously needs the same access discipline as any other account.

That is the question this site has been writing about for months. In the [Agent Behaviour Policy](https://riskmandate.ai/abp.html), the grant is everything an agent can technically reach and the mandate is what it is authorised to do; the gap between them is where incidents come from. AC.1 sizes the grant before an AI inherits it. AC.2 makes the grant something that can be read. AC.3 gives the mandate an owner, and its how asks the organisation to document which actions the system may take without human approval, which is writing the mandate down. Articles here have made the same argument from the other direction: [Six agents, one inbox](six-agents-one-inbox.md) on the account as the blast radius, [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md) on an identity per agent, [Where is the why?](where-is-the-why.md) on approvals given without the reason. It is good to see the same controls written by somebody who arrived at them through client work rather than through running agents.

### The power of an open licence

AI BCF is licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Anybody may share and adapt it, for any purpose, including commercially, on three conditions: credit the author and link the licence, say what was changed, and license what you share under the same terms.

The framework and the three it maps to, by what their terms allow. Only AI BCF is under a licence written for adaptation that also keeps adaptations open. A summary of published terms, not legal advice.

Set that beside the three frameworks it maps to. The NIST AI RMF is a work of the US government and can be read and reused freely. The EU AI Act is on EUR-Lex in every EU language, and the Commission authorises reuse with the source acknowledged; this site already turned it into a graph, in the [Regulation Graph vault](https://sgit.ai/demos/vaults/regulation-graph/index.md). ISO/IEC 42001 is sold per copy and its text is under ISO's copyright; a graph built on it can carry the clause numbers that other documents cite, and none of its words without permission.

For a control framework, the licence matters more than for most documents, for three reasons.

**A framework is worth the tools built on it.** A framework is rarely implemented by reading it. It is implemented through a spreadsheet of controls, a self-assessment, a mapping to the standard their auditor uses, a register, a ticket template, a dashboard. Each of those is an adaptation. A licence that permits adaptation in advance means each of those can be built, and shared, without asking.

**ShareAlike keeps the tools open.** BY-SA requires that what is shared from an adaptation carries the same licence. A self-check built on AI BCF and published stays as open as the framework, so the next person can build on the tool as well as the source. That is how a framework grows an ecosystem rather than a set of private forks.

**Time.** The CSV was downloaded on 7 October. The same day it was a graph, a database, eighty documents and a published vault, with the attribution on every page. There was no permission to request, no fee to agree and no wait. That is part two.

## Part two: what we did with it

**The vault.** [AI BCF as a graph](https://sgit.ai/demos/vaults/aibcf-graph/index.md), vault `lop5iqzw`, published with its read key and licensed CC BY-SA 4.0. It opens as an app in the browser. Nothing in it is an official AI BCF product, and its author has not reviewed it.

### One CSV in, five shapes out

The conversion. The CSV is kept byte for byte with its SHA-256; one deterministic script builds every other file from it; the AI Act citations are joined to the law's text in another vault.

The CSV is kept unchanged, with its SHA-256 recorded. One script, `tools/build.py`, reads it and writes everything else, so the same inputs give the same bytes and a v1.1 of the framework rebuilds the whole set. Before trusting the CSV, the build compared it with the twenty control pages on aibcf.org: they match field for field except one space before a closing bracket in RG.3.

- **A semantic graph.** 127 nodes and 239 edges: the framework, its categories, types, controls and triggers, the three external frameworks, their groups and the fifty-four cited clauses, ten nodes of EU law, and an overlay. Fourteen verbs, each with a stated inverse: `cites` and `is_cited_by`, `groups` and `is_grouped_in`, `applies_when` and `activates`.
- **An ontology and a taxonomy.** `ontology.json` lists the classes, the verbs and their inverses, the partitions and the grammar. `taxonomy.skos.jsonld` publishes the categories and types as SKOS concept schemes, so any taxonomy tool can load them.
- **Linked data.** The whole graph as JSON-LD and as Turtle, for triple stores.
- **Hyperlinked documents.** Eighty Markdown pages: one per control, per category and per cited clause, each linking to the others, each carrying the attribution. Reading a clause's page tells you every control that cites it.
- **A database.** `aibcf.sqlite`, three tables, controls, nodes and edges. The app builds the same tables in the browser with sql.js, so the database runs where the reader is.

Every edge is in one of five partitions, by where it came from: from the framework's own data (123), structure the build adds, such as category membership (67), parsed from the prose (9), joined to the law (24), and the sgit.ai overlay (16). The partition is on every edge and in every view, so a reader can tell what the framework says from what we added.

### A fractal semantic graph in action

The idea of a [fractal semantic graph](introducing-fractal-semantic-graphs.md) is that the same small grammar holds at every level of detail, so one view and one query language serve the whole thing, from the top of a framework to a paragraph of law. This conversion turned out to be a clean demonstration of it.

Five altitudes of the same graph, captured from the vault's graph view: the framework, a category, a control, a cited clause, and the paragraph of the AI Act it resolves to. Each altitude has its own question; the grammar does not change.

The graph view puts one node in the centre and draws its neighbours grouped by verb, reading incoming edges through their inverse. Above the drawing is the question that altitude answers. At the top, *what does the framework contain?* Five categories and three types. Click Comply: *which controls does it group?* Four. Click CM.3: *what does it cite, depend on and connect to?* Five clauses, a trigger, a category, an overlay, and three other controls the law links it to. Click Article 26: *which controls cite it, and where does it sit?* It is part of the AI Act and resolves to a node in another vault. Click that, and the view is now showing a node from the Regulation Graph, with the article's own text in the side panel.

Two things make that walk possible. The first is the grammar, five rules: every edge is a verb with a stated inverse; no `relates_to`; properties carry data, never meaning; supersede, never delete; render the answer to a question, not the whole graph. The second is that the Regulation Graph uses the same grammar, so joining the two was a matter of matching ids, `eu-ai-act:art-26` to `eu-2024-1689/art_026`, rather than agreeing on a schema. Two vaults, built months apart, became one walk.

The app has three journeys that walk these paths for you: from the framework down into the law; the controls the big three do not have; and two controls the law connects.

### What the graph found that the CSV does not say

These needed no cleverness, only the relationships made explicit. They are computed by the build and listed in `findings.json`.

1. **Four controls have no equivalent in the three frameworks the rest cite.** AC.1 to AC.4, the whole Access category. Visible in the crosswalk as four empty rows.
2. **The law connects controls the framework lists separately.** The AI Act's own cross-references link four pairs of Comply controls, by seven paths. CM.3 (high-risk use logged, overseen and disclosed) cites Article 26, which cites Article 50, which CM.2 (AI content marked as AI) cites. CM.3 cites Article 26, which cites Articles 27 and 49, which CM.4 (the fundamental rights impact assessment) cites. CM.3 cites Article 79, which cites Article 5, which CM.1 cites. And CM.1 cites Article 5, which cites Articles 27 and 49, which CM.4 cites. An organisation implementing CM.3 is, by the law's own wiring, close to CM.2 and CM.4 as well.
3. **Four of the eight cited AI Act articles were amended by Regulation (EU) 2026/1744:** Articles 4, 5, 27 and 50, according to the Regulation Graph's record. The controls citing them, GV.3, CM.1, CM.2 and CM.4, are the ones to re-read first the next time the Act moves. The framework says it already reflects the amendment; the graph makes it cheap to check.
4. **Nine references between controls sit in the prose.** "See RG.1" in the how of RG.2, for instance. Made into `refers_to` edges, they show that Track leans on Govern: TR.2 and TR.3 point at GV.2, GV.3 and GV.4.
5. **Four clauses are cited by more than one control,** so one change upstream touches several controls: ISO/IEC 42001 A.3.3 (GV.2, TR.2, TR.3), A.4.4 (RG.1, RG.2), A.9.4 (CM.3, RG.2), and NIST GOVERN 4.3 (TR.2, TR.3).
6. **Two small data notes.** RG.2 cites ISO A.9.4 twice, which a list hides and a graph shows as a duplicate edge. And two citations name subparagraphs of Article 50(4) that the Regulation Graph does not model, so they resolve one level up, to the paragraph, and the join says so.
The crosswalk view: one column per NIST function, ISO Annex A group and AI Act article. The four empty rows are the Access controls.

### Two ways to ask, in the browser

The same graph can be asked in two languages, both running in the page with nothing sent anywhere.

SQLite in the browser: which controls cite an article the 2026 amendment changed. Seven rows, in a few milliseconds.

The SQL console has six saved queries, the ones behind the findings above, and takes any SQL. The triple console treats the graph as statements, `subject verb object`, with `?names` for what you want found, joined on shared names. Because every edge is stored with its inverse, a question can be asked from either end: `category:access groups ?control` works because `is_grouped_in` declared its inverse.

The triple-pattern console: three patterns, joined on shared names, from control to clause to law to the amending act.

### The overlay, kept apart

The last partition is ours. Sixteen edges link nine controls to the words of the Agent Behaviour Policy and to articles on this site: AC.3 addresses the mandate and the owner and is discussed in Where is the why?; CM.3 addresses the barrier, because human oversight is a barrier only if it is meaningful; TR.3 addresses the footprint, because logged errors are what an agent did, read afterwards; GV.4 is discussed in [Every risk is already accepted](every-risk-is-already-accepted.md). Each overlay edge carries a one-line why, sits in the `overlay` partition, and is drawn with its own line style and labelled as an sgit.ai reading, not part of AI BCF, wherever it appears. That separation is what lets a reading sit next to a source without being mistaken for it, which is the same discipline the [code review graphs](code-review-as-a-fractal-semantic-graph.md) and the [PCI DSS](https://sgit.ai/demos/vaults/pci-dss-graph/index.md) and [AIUC-1](https://sgit.ai/demos/vaults/aiuc-1-graph/index.md) graph vaults keep.

A control page: the framework's text verbatim, the "no equivalent" note from its own Sources column, and the overlay set apart and labelled.

### What the licence asked of us, and how the vault answers

- **Attribution.** The framework, its author, version and licence are named on the app's overview, on every control page, at the foot of every document, in the README and in `LICENSE.md`.
- **Changes indicated.** `LICENSE.md` lists them: the conversion, the parsing of the Sources column, the references made into edges, the join, the overlay. No control text was altered.
- **ShareAlike.** The vault is CC BY-SA 4.0. Anybody can take the graph, the database or the documents and build the next thing, on the same terms.
- **No endorsement.** It says, on the overview and in the licence file, that it is not an official AI BCF product.

### Back to the three questions

Did you use semantic graphs, is there an API, what formats? The vault is one answer, offered back to the framework: a graph whose verbs and partitions are declared, a set of formats that existing tools already read, and a database a browser can query, all rebuilt from the CSV by one script. None of it needed anything from the framework's author except the two things he already gave it: an export, and a licence that says yes in advance.

If AI BCF publishes its own graph one day, it should be the authoritative one, and this vault should be superseded by it, not merged into it; that is the fourth rule. Until then, the CSV, the licence and the build script are enough for anybody to do what we did, better.

*Drafted from Jan van Dijke's post, his reply, and a request from Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026. The framework's text quoted here is from aibcf.org, AI BCF v1.0 by Jan van Dijke, CC BY-SA 4.0. The licence summaries are of terms as published and are not legal advice. The vault's figures come from its build output and from live screenshots of its app. No key or token appears in any figure or file except the published read key on the vault's page.*

## Threads

Graphs & knowledgeAgents & policy[This article as a graph →](graphs.md#ai-baseline-control-framework)

### Builds on

- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.

### Continued by

- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 36 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=36)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [ai-baseline-control-framework.jpg](banners/ai-baseline-control-framework.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/ai-baseline-control-framework.html)*
