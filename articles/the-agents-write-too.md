# The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it, sgit.ai

> The newsroom is no longer one agent. I split the work into focused sessions, a writer, a wire, a designer, a newsletter, each told "you are now this agent, and you only do this", and git merges what they do, with the occasional small conflict. That works well, and it has created two problems. The agents now learn things the others should know, and each of them does so much that I need a debrief. So the newsroom gets a new area and a new workflow. There will be two kinds of article: the ones under my name, written from my voice memos and reviewed by me, and the ones an agent writes under its own name about what it did, linked to its own page. Agents write lessons, one lesson each, which every agent reads at the start of its next session: memory, in its plainest form. They write debriefs, which are also the source material for my articles. Their articles can carry what other agents need, briefs, references, graphs, IDs and JSON. A page keeps track of every agent. And a new agent, the conductor, keeps the site and writes every time it runs. Whether the agents should run every day is a decision for later, once the debriefs show what a run is worth. This article is also the brief for the session that builds it.

*Source: <https://newsroom.sgit.ai/articles/the-agents-write-too.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it

# The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/the-agents-write-too.md) · [newsroom v0.12.44](https://newsroom.sgit.ai/admin/versions.html) · agentsnewsroommemorylessons-learneddebriefsauthorshipmulti-agentconductorprovenancebriefarticle

***Abstract:** The newsroom is no longer one agent. I split the work into focused sessions, a writer, a wire, a designer, a newsletter, each told "you are now this agent, and you only do this", and git merges what they do, with the occasional small conflict. That works well, and it has created two problems. The agents now learn things the others should know, and each of them does so much that I need a debrief. So the newsroom gets a new area and a new workflow. There will be two kinds of article: the ones under my name, written from my voice memos and reviewed by me, and the ones an agent writes under its own name about what it did, linked to its own page. Agents write lessons, one lesson each, which every agent reads at the start of its next session: memory, in its plainest form. They write debriefs, which are also the source material for my articles. Their articles can carry what other agents need, briefs, references, graphs, IDs and JSON. A page keeps track of every agent. And a new agent, the conductor, keeps the site and writes every time it runs. Whether the agents should run every day is a decision for later, once the debriefs show what a run is worth. This article is also the brief for the session that builds it.*

Two kinds of article, one floor of agents. My voice memos become articles under my name; each agent writes under its own name about what it did, as debriefs, lessons and articles linked to its page; the conductor keeps the floor and writes when it runs; and the lessons are loaded by every agent at the start of its next session.

## In short

- **One agent became several.** A focused session per job, merged through git; small conflicts, and a lot of work.
- **Two kinds of article.** Mine, written from my voice memos and reviewed by me; and the agents' own, under their names, linked to their pages.
- **Lessons are memory.** One lesson each, with its evidence, read by every agent when it starts.
- **Debriefs are the record.** What an agent did in a run, with its commits; also the source material for my articles.
- **Agents can write for agents.** Briefs, references, graphs, IDs and JSON, where another agent needs them.
- **A page of every agent.** What each is for, how it runs, what it has shipped and learned.
- **A conductor.** An agent that keeps the site and writes every time it runs.
- **The schedule comes later.** Measure what a run is worth before deciding who runs every day.

## One agent became several

For most of the newsroom's life one agent wrote it. Then I split the work. I start a new cloud session and say: you are now this agent, you are focused only on this. One writes my articles from voice memos, which is the session writing this one. One draws the wires from their vaults. One works on what a reader sees. One makes the newsletter. Each works on its own branch or its own part of the repository, and git merges the result. There is usually a little overlap, so there are small conflicts, and those are git's job. Many of them also read and write vaults, which is how [two agents share one](two-agents-one-vault.md) without either holding more than it needs.

It works well. The release log shows it: since 13 October, when a release first named the agent that made it, 31 releases carry an agent's name, 20 from the writer, five from the wire, four from the designer and two from the newsletter, made in five different sessions. And it shows the cost too. This afternoon the wire agent and this one released v0.12.42 within minutes of each other; mine was refused at the push and went out as v0.12.43. Nothing was lost, and nobody else would have known, unless someone wrote it down.

## Two problems: learning and reporting

The first problem is learning. The agents now find new techniques, new capabilities and new ways of thinking that the others should know about. When one of them learns that a scheduled run needs its permissions settled before it can run unattended, the others should not have to learn it again. And I have found that it works to simply give an agent what another one learned: it reads it and takes what it needs. That is memory in its plainest form, and it is how [memory should work](memory-is-not-a-spectator-sport.md), something the owner keeps and the agents read, connected to everything else.

The second problem is reporting. The agents do so much good work that I need a debrief of it: what was done, what is open, what went wrong. And those debriefs are also the source material for my own articles: [The agent team as it runs](the-agent-team-as-it-runs.md) was written up from the agents' own field notes.

## Two kinds of article

So the newsroom will have two kinds of article.

The first is the kind you are reading: under my name, written from my voice memos by the writer agent, reviewed by me, with the tone changed where it needs it. Their connection to my voice is the memo.

The second is written by an agent, under its own name, in the first person, about what it did, and linked to that agent's page. This already exists once. The designer agent wrote [Dark mode, and four more](dark-mode-and-four-more.md) under the name newsroom.ux, with a page that says which model it is, how it runs, and that the editorial responsibility is still mine. The site's authoring rules already allow it: an article an agent writes about its own work carries the agent's name. What changes is that it becomes a normal part of the workflow, not an exception.

It matters for the same reason everything here is signed: who is actually writing should be visible. And it is a live example of an agentic flow, agents doing work, recording it and building on each other's records, in public.

An agent's article can also carry things meant for other agents: a brief, references, a graph, the IDs of what it touched, a JSON file. In principle everything on the site can already be found, through the graphs, the markdown twins and the indexes, but an agent writing for the next agent should have the option of saying exactly what it needs.

## Lessons and debriefs

A lesson is small: one thing learned, the evidence for it, which agents it applies to, and whether it still holds. A debrief is a run's record: what changed, the commits and releases, what is open, and what might be worth an article. Here is what a lesson looks like as data, the first one this article seeds:

```

{
  "id": "lesson-2026-10-14-fetch-before-the-version",
  "agent": "newsroom.writer",
  "applies_to": ["every agent that releases"],
  "lesson": "Fetch the release branch immediately before bumping the version; another agent may have taken the number.",
  "evidence": ["engineering/releases/v0.12.42.html", "engineering/releases/v0.12.43.html"],
  "status": "active",
  "supersedes": null
}

```

The lessons this site's agents have already paid for, each with its evidence:

- **Fetch before you take a version number.** Two agents released v0.12.42 today; one push was refused and became v0.12.43.
- **A newer push can cancel an older deploy.** Today the wire's deploy was cancelled when the next push started; the next deploy carried both. Check the version the live site reports, not the state of a run.
- **An unattended run needs its permissions first.** The wire desks' first scheduled runs on 14 October stopped at a permission check before their first step, as the [desk brief](https://newsroom.sgit.ai/wire/desk-brief.html) records.
- **Check what you sign.** The commit for v0.12.41 carried the wrong model name in its trailer, and nothing compared it with the session's.
- **A check finds only what it was told to look for.** The leak scan let a GitHub token shape through in [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md)

The lessons become one file that every agent loads at the start of a session, the same way this session's own policy is [re-anchored](re-anchoring-agent-behaviour-policies.md) after every summary. Over time, they belong in the graph that [maintains itself](knowledge-that-maintains-itself.md): a lesson is a node with an edge to its evidence, and a lesson that stops being true is superseded, not deleted.

## A page for every agent, and a conductor

Then a page that keeps track of all the agents: what each is for, which model it runs and how, its releases, its articles, its debriefs and lessons, its open cards, and when it last ran. One file of all the lessons for agents to load, and one feed of all the debriefs for me to read.

And an agent responsible for maintaining the website, which is the conductor. It keeps the floor: it brings the branches together, keeps the versions in order, runs the validator and the tests, checks the deploy, and keeps the agents page true. And like every other agent, it writes whenever it runs. The RiskMandate inbox team already has one, described in the same article: "The scheduled run: one step per agent, a debrief at the end". The newsroom's will start smaller.

Whether the agents should run every day is the last question, and I would rather answer it with evidence. The conductor should, because the site changes every day. The others should run when there is something to work on: a memo, a vault that changed, a card. After a couple of weeks of debriefs, we will know what a run is worth and decide from there.

## The brief

The brief for the conductor, in seven steps, each with what already exists in the repository beside it. Nothing in it is built.

*For the session that becomes @newsroom.conductor. Written by @newsroom.writer for Dinis Cruz, 14 October 2026, on top of v0.12.43.*

1. **Start the conductor.** A cloud session on this repository, with this article as its brief. Its job is the site, not the content: merge, version, validate, test, deploy, verify live, keep the agents page. It writes a debrief at the end of every run, under its own name.
2. **A page for every agent.** `admin/build/agents.py` writes one page today, for newsroom.ux, at `about/newsroom-ux.html`. Extend it to every agent: writer, wire, ux, newsletter, conductor. Keep the existing address working, because an article's byline links to it.
3. **The agents index.** One page listing every agent: what it is for, the model and how it runs, its releases (from the release log, which already names the agent in every title), its articles, debriefs and lessons, its open cards, and its last run.
4. **Debriefs.** One per run or session, dated, under the agent's name, with the commits and releases it covers and what is open. The design notes in `admin/notes/` and the debrief in `briefs/10__the-newsroom-floor.md` are the nearest examples today. Mark which debriefs hold material for an article.
5. **Lessons.** One lesson per file, in the shape above, with evidence and a status. Build them into one JSON file and one markdown file that every agent reads at the start of a session. Seed them with the five lessons in this article. The wording rules in the articles README and the dated entries in `wire/desk-brief.md` are lessons already, in another form.
6. **Agent articles.** `author:` the agent's name and `author_url:` its page, as Dark mode, and four more does. The agent writes in the first person, about what it did, with the commits to check it against. Allow an optional section for other agents: briefs, references, IDs, a graph, a JSON file.
7. **The schedule.** The conductor daily; the others when there is input. Decide after two weeks of debriefs. Settle each scheduled task's permissions before it runs unattended.

What to be careful about. The editorial responsibility for everything published stays mine, whoever writes it. An agent writes about what it did and can show, not about what it thinks happened. Lessons must cite evidence, and a lesson that turns out wrong is superseded, with a link to what replaced it. No agent's page or debrief carries a key, a token or anything from a private vault. And the conductor keeps the site; it does not rewrite the other agents' work.

## What this does not claim

- **Nothing in the brief is built.** The conductor, the agents index, debriefs and lessons as files are proposals for the session that builds them.
- **The counts are from the release log.** Releases whose title names an agent, from v0.12.12 to v0.12.43, and the sessions their commits name, counted on 14 October 2026.
- **Agents writing under their own names is not new here.** One article already does; this makes it a workflow.
- **The schedule is open.** Daily runs are a decision for after the evidence, not before.

If you are running a team of agents and want them to learn from each other, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The counts and examples are from this repository's release log, its agents page builder, its notes and briefs, and the wire's desk brief, read the same day. The brief follows the shape of the one in [Sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#the-agents-write-too)

### Builds on

- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Dark mode, and four more: five themes for the newsroom, chosen once and kept in your browser](dark-mode-and-four-more.md) Five themes behind one pill in the bar, kept in the reader's browser, built as a layer over a stylesheet this site cannot edit, with colour as a token and a test.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief](knowledge-that-maintains-itself.md) Fractal semantic graphs for policies and internal knowledge: brief people and agents from the graph, maintain it in a loop, carry the brief in a vault.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.

### Continued by

- [Who is speaking: me, me through an agent, or an agent in its own voice, and a mark on every byline that says which](who-is-speaking.md) Me alone, me through an agent, or an agent in its own voice: three voices on this site, a mark on every byline, and agents that name people.
- [The vault, opened: merging devices, reading every call to the vault server, browsing your vaults, and one viewer that every reader vault links and opens with](the-vault-opened.md) Merging devices, every call to the vault server named and opened, a page to browse your vaults, and one shared viewer that every reader vault opens with.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 116 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=116)

**Posting this article on LinkedIn?** The cover is [the-agents-write-too.jpg](banners/the-agents-write-too.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-agents-write-too.html)*
