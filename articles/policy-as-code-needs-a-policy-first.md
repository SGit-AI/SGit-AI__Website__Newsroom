# Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have, sgit.ai

> At an event this week a speaker described policy as code as the way to scale governance and AI innovation together, and it clicked. Policy as code is right, and it is where agent governance has to end up. But for agents it answers one question, is this request allowed, and the questions a business, an auditor or an insurer asks are the ones around it, the ones an Agent Behaviour Policy holds. What can this agent reach, measured. What was it asked to do, and why. Where the two differ. Which rules can no engine ever see. And the one that surprised me when I checked: for every rule that is code, who can change that code. A rule the agent can rewrite is a setting, not a control. Because an ABP has those columns, it can be written in both directions. From the policy, generate code: for this article, five rows of a real ABP became a Rego policy that Open Policy Agent ran against seven requests, denying a push to the wrong repository, a commit without a leak scan and a model id in a diff, asking before a pull request, and allowing a sentence no engine can judge. From what exists, reverse engineer the policy: parse the code back, and the gaps show on both sides, a row with no code and a rule nobody wrote a reason for. I did it to this session's own policy: of its eleven rules, eight have some code behind them, and only one has code the agent cannot change. Fractal semantic graphs are what make the round trip work across paper, spreadsheets, regulations and code, because each keeps its own vocabulary and the edges between them carry verbs both ways.

*Source: <https://newsroom.sgit.ai/articles/policy-as-code-needs-a-policy-first.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have

# Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/policy-as-code-needs-a-policy-first.md) · [newsroom v0.12.35](https://newsroom.sgit.ai/admin/versions.html) · policy-as-codeagent-behaviour-policyopen-policy-agentregofractal-semantic-graphsgovernanceenforcementreverse-engineeringagentsarticle

***Abstract:** At an event this week a speaker described policy as code as the way to scale governance and AI innovation together, and it clicked. Policy as code is right, and it is where agent governance has to end up. But for agents it answers one question, is this request allowed, and the questions a business, an auditor or an insurer asks are the ones around it, the ones an Agent Behaviour Policy holds. What can this agent reach, measured. What was it asked to do, and why. Where the two differ. Which rules can no engine ever see. And the one that surprised me when I checked: for every rule that is code, who can change that code. A rule the agent can rewrite is a setting, not a control. Because an ABP has those columns, it can be written in both directions. From the policy, generate code: for this article, five rows of a real ABP became a Rego policy that Open Policy Agent ran against seven requests, denying a push to the wrong repository, a commit without a leak scan and a model id in a diff, asking before a pull request, and allowing a sentence no engine can judge. From what exists, reverse engineer the policy: parse the code back, and the gaps show on both sides, a row with no code and a rule nobody wrote a reason for. I did it to this session's own policy: of its eleven rules, eight have some code behind them, and only one has code the agent cannot change. Fractal semantic graphs are what make the round trip work across paper, spreadsheets, regulations and code, because each keeps its own vocabulary and the edges between them carry verbs both ways.*

One policy at three altitudes. At the top, the business's words: a board policy, a row of a control spreadsheet, an article of a regulation. In the middle, the ABP row for one agent in one deployment: reach, mandate, gap, barrier and owner. At the bottom, the code where decisions are made: a Rego rule, a hook, a validator check. Generating code walks down; reverse engineering walks up; a node with no edge is a gap.

## In short

- **Policy as code is right, and it answers one question.** Is this request allowed. For agents, the governance questions are around it.
- **An ABP holds what the engine does not.** The reach, measured; the mandate and its reason; the gap; the rules no engine can see; the owner; and who can change each rule's code.
- **A rule the agent can rewrite is a setting.** This session's policy has eleven rules; eight have code behind them; only one has code the agent cannot change.
- **Generate code from the policy.** Five ABP rows became a 35-line Rego policy; Open Policy Agent decided seven requests: three denied, one asked, three allowed.
- **Reverse engineer the policy from the code.** Parsing the Rego back found a row with no code and a rule with no row, the two gaps that matter.
- **The same works from paper and spreadsheets.** A control spreadsheet became a graph joined to the law it maps to; a role file becomes both a published table and a check.
- **Fractal semantic graphs make the round trip work.** Each altitude keeps its own vocabulary, and every edge reads both ways.
- **The four jobs.** Enabler, scaling, enforcer and decision-maker: an ABP does the first and keeps the other three honest.

## Policy as code, and the question it answers

At an event this week, one of the speakers described policy as code as the way to scale governance and AI innovation at the same time. I agree, and I think it is where agent governance has to end up: rules that are versioned, tested, reviewed like code and enforced by something other than the model's good behaviour.

The best known engine for it describes the idea well. Open Policy Agent, a Cloud Native Computing Foundation graduated project, [lets you](https://www.openpolicyagent.org/docs/philosophy) "decouple policy from that software service": services "offload policy decisions to OPA by executing queries", policies "are written in a high-level declarative language", and a decision can be "arbitrary structured data", not only allow or deny.

That is exactly the right shape for the moment an agent acts. An agent asks to push, to send, to read a table; the engine answers. But it answers one question, is this request allowed, and when something goes wrong with an agent, that is rarely the question anyone asks first.

## What an agent behaviour policy adds

The questions a board, an auditor or an insurer asks about an agent are the ones around the decision, and they are the columns of an Agent Behaviour Policy, as [Footprint and blast radius](footprint-and-blast-radius.md) set them out.

- **The reach, measured.** What the agent can actually do, from its connectors and accounts. A policy engine only sees the requests that are routed through it; the reach includes the ones that are not.
- **The mandate, with its reason.** What the agent was asked to do, and why each rule exists. Code holds the condition; the reason lives, at best, in a comment.
- **The gap.** Reach minus mandate, derived. It is the list of things the agent could do that nobody asked for, which is where the rules should come from.
- **The rules no engine can see.** "Great, not perfect." "The tone is mine." Some rows will always be expectations, kept by a second reader, and an ABP lists them instead of silently leaving them out.
- **The owner.** Who answers for each row, which is what [The policy draws the liability line](the-policy-draws-the-liability-line.md) argued decides where liability lands.
- **Who can change the code.** For every rule that is code, whether the agent's own account could rewrite it. The barrier column types it: "A boundary is enforced above the agent's reach, so it cannot flip it. A setting is a switch the agent's own account could flip."

That last one is the column I did not expect to matter so much, until I checked this session.

## Reverse engineering this session's own policy

This session's own policy, reverse engineered from its code. Eleven rules; for each, the code that enforces it, who can change that code, and the barrier that results. Eight have some code behind them; only one, never pushing to sgit.ai, has code the agent cannot change.

The agent writing this site works under a written policy, eleven rules, reloaded after every summary, as [Re-anchoring](re-anchoring-agent-behaviour-policies.md) describes. So I did the exercise on it: for each rule, find the code that enforces it, in the session's hooks, its leak scan, the site's validators and its git configuration, and then ask who can change that code.

Eight of the eleven have some code behind them. The leak scan refuses a staged diff with a key-shaped string, a model id outside the byline, an em-dash in an article or a name on a private list. The validator fails the build on the ladder word and warns on absolutes. A hook prints the policy back after every summary and supplies the status report. Three rules have no code at all: masking keys in output, not using anyone else's credential, and answering when asked for the policy's status.

Then the second question, and the honest answer. Nearly all of that code is code the agent can change. The leak scan and the hooks are files in its own home directory; the validators are in the repository it pushes to and in a clone on its own disk. By the policy's own definitions, those rules are settings. Even "never push to sgit.ai", enforced by a push address set to nothing, is a setting on its own, because the agent could set it back. What makes that one rule a boundary is something the agent cannot touch: this session's access to GitHub is scoped to the newsroom's repository by the platform it runs on. One rule in eleven.

None of that is a failure; it is the session's real state, and most organisations' agents would look the same if anyone drew the table. It is also why policy as code alone would have scored this session as well governed: most of its rules are code. The ABP is what shows that the code is the agent's own.

And reverse engineering finds the reasons where they hide. The validator's rule against em-dashes carries its reason in a comment: readers find them off-putting, "and 2,900 of them do not stay gone without a rule". The rule against absolutes is advisory, and its message says why: "say what was found, not what nobody has". That is the paper policy, scattered through the code. Walking up from the code collects it into rows.

## Generating code from the policy

A round trip through Open Policy Agent. Five ABP rows as data, generated into a 35-line Rego policy, evaluated against seven requests, then parsed back with OPA's own parser and compared with the ABP: one row with no code, one rule with no row.

The other direction was built for this article. Five rows of the session's policy went into a small JSON file: an id, the rule, why it exists, the decision, a condition where there is one, the barrier, and what enforces it today. A generator of about twenty-five lines turned them into Rego, each rule carrying its row's id and reason as a comment and as the value it returns:

```

# R9: Never push to the sgit.ai repository. Why: sgit.ai is read-only for this session.
deny contains "R9" if {
	input.tool == "git.push"
	not input.remote in {"github.com/SGit-AI/SGit-AI__Website__Newsroom"}
}

```

OPA 1.21.2 checked the policy and evaluated seven requests. A push to sgit.ai: deny, R9. A push to the newsroom: allow. A commit with no leak scan: deny, R2. A commit adding a model id in a code comment: deny, R5. A clean, scanned commit: allow. Opening a pull request: ask, R7b, because the decision is the owner's. And publishing a sentence that says "a perfect result": allow, because the row that forbids it has no condition any engine can check, and the generator wrote that down as a comment instead of pretending.

Then back again. `opa parse` turned the Rego into its syntax tree, and comparing the rules it found with the ABP's rows gave the two lists that matter. Rows with no code: R6c, the wording rule, which stays an expectation with a second reader. Code with no row: after a second file added a rule against Friday releases, "added in a hurry after an incident", the comparison flagged `no-friday-releases` as enforcement nobody had written a reason for. That is the rule that will confuse the next person, block the next urgent fix, and have no owner when someone asks why.

## From spreadsheets and paper

Code is not the only thing to reverse engineer, and this site has done the other two.

From a spreadsheet: when Jan van Dijke published the [AI Baseline Control Framework](ai-baseline-control-framework.md), twenty controls mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act, its CSV became, on the day, "a semantic graph with an ontology", "joined to the EU AI Act's own text", and "the six things the graph found that the CSV does not say". [Four frameworks, one agent](four-frameworks-one-agent.md) did the same for four frameworks and one agent, as a mapping file with a row for every element and its status.

From paper, in both directions at once: sgit.ai's newsroom roles are written as files, and the check that gates a release reads them. In the words of the check itself, "The policy is the `writes` and `edits` lists in `admin/content/newsroom/roles/<role>.md`, the same files the `/newsroom/policies.html` table is generated from." One source, rendered as a page people read and as a check a release must pass. That is the pattern I would want for every agent: the ABP is the source, the table and the code are renderings, and neither can drift from the other because neither is edited by hand.

## Why it needs fractal semantic graphs

A round trip like this breaks if every format has to share one schema. A board policy is written in the board's words; a regulation in the legislator's; a control spreadsheet in the auditor's; an ABP in reach, mandate, gap and barrier; Rego in packages, rules and conditions. Asking any of them to adopt the others' vocabulary is why mapping exercises become workshops.

[Fractal semantic graphs](introducing-fractal-semantic-graphs.md) are the answer this site has been building: "Zoom into any node and you enter a new world with its own node types, its own verbs, its own taxonomy." Each altitude keeps its own vocabulary; the edges between them are verbs with inverses, so a row answers a policy and the policy is answered by the row; a rule enforces a row and the row is enforced by the rule. Then the questions that matter are walks, not workshops. "A question can cross formats without a join table." Which board policies have no row? Which rows have no code? Which code has no row? Which rows are enforced only by code the agent's own account can change? And when a regulation changes, supersede the node, never delete it, and every row and rule that rested on it becomes the answer to a query.

That is what makes reverse engineering practical at scale: the code, the spreadsheet and the paper do not need to be converted, only connected. And it is what makes generation safe: the code that comes out carries an edge back to the row it came from, so the next person can ask why.

## The four jobs

The speaker's framing was policy as code as an enabler, a way to scale, an enforcer and a basis for decisions. With an ABP as the source, each one gets sharper.

- **Enabler.** A written mandate lets a team ship an agent without a review meeting per agent, because the review was of the policy. [The behaviour policy is the business logic](the-behaviour-policy-is-the-business-logic.md): writing it is the work.
- **Scaling.** One source, rendered into as many engines and agents as needed, versioned and diffable, with every generated rule traceable to its row.
- **Enforcer.** Rows compiled into boundaries, and the barrier column saying, honestly, which ones still are not. [Hope or enforcement](hope-or-enforcement.md) measured what that is worth: one agent's rules kept only by good behaviour fell from 97% to 23% as they moved into the platform.
- **Decision-maker.** Every decision returns the row it came from, allow, deny or ask, and every ask goes to a named person, as [The human in the loop](the-human-in-the-loop.md) argued, with the record of decisions moving the line over time.

## What this does not claim

- **The round trip is a demonstration.** Five rows, a short generator and seven requests, run for this article; it is not a product, and real agents need their requests routed through the engine for any of it to bind.
- **The session table is one agent's.** Counted from this session's hooks, scripts, validators and configuration on 14 October 2026; other agents will look different, and I expect most to look similar.
- **The GitHub scope was not tested by trying.** It is how this session's access is configured; pushing to sgit.ai to prove it is exactly what the policy forbids.
- **Some rows will never be code.** That is a feature of the method, not a gap in it: an ABP says which rows rely on a person.
- **The speaker is not named.** I took the idea from a talk and have not checked how they would put it.

If you have policies in code, spreadsheets or paper and want to see the agent behaviour policy they imply, or the code an ABP implies, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, from an event where a speaker described policy as code as a way to scale governance and AI innovation; written by this site's agent in the voice of this site, and the argument and the editorial responsibility are mine. The round trip was run for this article with Open Policy Agent 1.21.2: a JSON file of five rows from this session's policy, a generator written for the purpose, `opa check`, `opa eval` on seven requests and `opa parse` to read it back. The session table is from this session's own policy (v0.3, eleven rules), its hooks, its leak scan, sgit.ai's validator and policy check, and its git configuration. OPA's description is from its [philosophy page](https://www.openpolicyagent.org/docs/philosophy), read on 14 October 2026.

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#policy-as-code-needs-a-policy-first)

### Builds on

- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.
- [Four frameworks, one agent: iason's comparison of the OECD classification, the NIST AI RMF, Japan's guidelines and the EU AI Act, read against what runs here, with the evidence and the graphs](four-frameworks-one-agent.md) iason's comparison of four AI risk frameworks, mapped to the behaviour policy, the footprint and the graphs that run here, with the status of each row.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why](the-human-in-the-loop.md) Checking every output is a bottleneck and a weak safety net; put the person where it cannot be undone, and let controls do the rest.

### Continued by

- [A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in](a-trusted-framework-for-agentic-finance.md) The FCA plans a framework for agentic finance. Our open behaviour policies cover its four elements; a vault shows six bank agents at play.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP](cedar-and-the-policy-vault.md) Cedar is mature and adopted; it lacks the why, the version in force and the evidence. A vault carries all three, and the demo shows it working.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.
- [System prompts as behaviour policies: Claude's published prompt and a leaked ChatGPT one, mapped into rows, a taxonomy of rules, and a JSON file a harness could enforce](system-prompts-as-behaviour-policies.md) Claude's published system prompt as 82 policy rows in eight kinds: 36 could be held by the harness, 21 partly by classifiers, 25 stay with the model.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief](knowledge-that-maintains-itself.md) Fractal semantic graphs for policies and internal knowledge: brief people and agents from the graph, maintain it in a loop, carry the brief in a vault.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 110 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=110)

**Posting this article on LinkedIn?** The cover is [policy-as-code-needs-a-policy-first.jpg](banners/policy-as-code-needs-a-policy-first.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/policy-as-code-needs-a-policy-first.html)*
