---
title: Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: At an event this week a speaker described policy as code as the way to scale governance and AI innovation together, and it clicked. Policy as code is right, and it is where agent governance has to end up. But for agents it answers one question, is this request allowed, and the questions a business, an auditor or an insurer asks are the ones around it, the ones an Agent Behaviour Policy holds. What can this agent reach, measured. What was it asked to do, and why. Where the two differ. Which rules can no engine ever see. And the one that surprised me when I checked: for every rule that is code, who can change that code. A rule the agent can rewrite is a setting, not a control. Because an ABP has those columns, it can be written in both directions. From the policy, generate code: for this article, five rows of a real ABP became a Rego policy that Open Policy Agent ran against seven requests, denying a push to the wrong repository, a commit without a leak scan and a model id in a diff, asking before a pull request, and allowing a sentence no engine can judge. From what exists, reverse engineer the policy: parse the code back, and the gaps show on both sides, a row with no code and a rule nobody wrote a reason for. I did it to this session's own policy: of its eleven rules, eight have some code behind them, and only one has code the agent cannot change. Fractal semantic graphs are what make the round trip work across paper, spreadsheets, regulations and code, because each keeps its own vocabulary and the edges between them carry verbs both ways.
version: v0.12.35
license: https://creativecommons.org/licenses/by/4.0/
tags: policy-as-code, agent-behaviour-policy, open-policy-agent, rego, fractal-semantic-graphs, governance, enforcement, reverse-engineering, agents, article
status: published
---

!shot pq-altitudes.webp | images/ | One policy at three altitudes. At the top, the business's words: a board policy, a row of a control spreadsheet, an article of a regulation. In the middle, the ABP row for one agent in one deployment: reach, mandate, gap, barrier and owner. At the bottom, the code where decisions are made: a Rego rule, a hook, a validator check. Generating code walks down; reverse engineering walks up; a node with no edge is a gap. | architecture

## In short {#in-short}

- **Policy as code is right, and it answers one question.** Is this request allowed. For agents, the governance questions are around it.
- **An ABP holds what the engine does not.** The reach, measured; the mandate and its reason; the gap; the rules no engine can see; the owner; and who can change each rule's code.
- **A rule the agent can rewrite is a setting.** This session's policy has eleven rules; eight have code behind them; only one has code the agent cannot change.
- **Generate code from the policy.** Five ABP rows became a 35-line Rego policy; Open Policy Agent decided seven requests: three denied, one asked, three allowed.
- **Reverse engineer the policy from the code.** Parsing the Rego back found a row with no code and a rule with no row, the two gaps that matter.
- **The same works from paper and spreadsheets.** A control spreadsheet became a graph joined to the law it maps to; a role file becomes both a published table and a check.
- **Fractal semantic graphs make the round trip work.** Each altitude keeps its own vocabulary, and every edge reads both ways.
- **The four jobs.** Enabler, scaling, enforcer and decision-maker: an ABP does the first and keeps the other three honest.

## Policy as code, and the question it answers {#question}

At an event this week, one of the speakers described policy as code as the way to scale governance and AI innovation at the same time. I agree, and I think it is where agent governance has to end up: rules that are versioned, tested, reviewed like code and enforced by something other than the model's good behaviour.

The best known engine for it describes the idea well. Open Policy Agent, a Cloud Native Computing Foundation graduated project, [lets you](https://www.openpolicyagent.org/docs/philosophy) "decouple policy from that software service": services "offload policy decisions to OPA by executing queries", policies "are written in a high-level declarative language", and a decision can be "arbitrary structured data", not only allow or deny.

That is exactly the right shape for the moment an agent acts. An agent asks to push, to send, to read a table; the engine answers. But it answers one question, is this request allowed, and when something goes wrong with an agent, that is rarely the question anyone asks first.

## What an agent behaviour policy adds {#adds}

The questions a board, an auditor or an insurer asks about an agent are the ones around the decision, and they are the columns of an Agent Behaviour Policy, as [Footprint and blast radius](/articles/footprint-and-blast-radius.html) set them out.

- **The reach, measured.** What the agent can actually do, from its connectors and accounts. A policy engine only sees the requests that are routed through it; the reach includes the ones that are not.
- **The mandate, with its reason.** What the agent was asked to do, and why each rule exists. Code holds the condition; the reason lives, at best, in a comment.
- **The gap.** Reach minus mandate, derived. It is the list of things the agent could do that nobody asked for, which is where the rules should come from.
- **The rules no engine can see.** "Great, not perfect." "The tone is mine." Some rows will always be expectations, kept by a second reader, and an ABP lists them instead of silently leaving them out.
- **The owner.** Who answers for each row, which is what [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html) argued decides where liability lands.
- **Who can change the code.** For every rule that is code, whether the agent's own account could rewrite it. The barrier column types it: "A boundary is enforced above the agent's reach, so it cannot flip it. A setting is a switch the agent's own account could flip."

That last one is the column I did not expect to matter so much, until I checked this session.

## Reverse engineering this session's own policy {#session}

!shot pq-session.webp | images/ | This session's own policy, reverse engineered from its code. Eleven rules; for each, the code that enforces it, who can change that code, and the barrier that results. Eight have some code behind them; only one, never pushing to sgit.ai, has code the agent cannot change. | comparison

The agent writing this site works under a written policy, eleven rules, reloaded after every summary, as [Re-anchoring](/articles/re-anchoring-agent-behaviour-policies.html) describes. So I did the exercise on it: for each rule, find the code that enforces it, in the session's hooks, its leak scan, the site's validators and its git configuration, and then ask who can change that code.

Eight of the eleven have some code behind them. The leak scan refuses a staged diff with a key-shaped string, a model id outside the byline, an em-dash in an article or a name on a private list. The validator fails the build on the ladder word and warns on absolutes. A hook prints the policy back after every summary and supplies the status report. Three rules have no code at all: masking keys in output, not using anyone else's credential, and answering when asked for the policy's status.

Then the second question, and the honest answer. Nearly all of that code is code the agent can change. The leak scan and the hooks are files in its own home directory; the validators are in the repository it pushes to and in a clone on its own disk. By the policy's own definitions, those rules are settings. Even "never push to sgit.ai", enforced by a push address set to nothing, is a setting on its own, because the agent could set it back. What makes that one rule a boundary is something the agent cannot touch: this session's access to GitHub is scoped to the newsroom's repository by the platform it runs on. One rule in eleven.

None of that is a failure; it is the session's real state, and most organisations' agents would look the same if anyone drew the table. It is also why policy as code alone would have scored this session as well governed: most of its rules are code. The ABP is what shows that the code is the agent's own.

And reverse engineering finds the reasons where they hide. The validator's rule against em-dashes carries its reason in a comment: readers find them off-putting, "and 2,900 of them do not stay gone without a rule". The rule against absolutes is advisory, and its message says why: "say what was found, not what nobody has". That is the paper policy, scattered through the code. Walking up from the code collects it into rows.

## Generating code from the policy {#generate}

!shot pq-roundtrip.webp | images/ | A round trip through Open Policy Agent. Five ABP rows as data, generated into a 35-line Rego policy, evaluated against seven requests, then parsed back with OPA's own parser and compared with the ABP: one row with no code, one rule with no row. | architecture

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

## From spreadsheets and paper {#paper}

Code is not the only thing to reverse engineer, and this site has done the other two.

From a spreadsheet: when Jan van Dijke published the [AI Baseline Control Framework](/articles/ai-baseline-control-framework.html), twenty controls mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act, its CSV became, on the day, "a semantic graph with an ontology", "joined to the EU AI Act's own text", and "the six things the graph found that the CSV does not say". [Four frameworks, one agent](/articles/four-frameworks-one-agent.html) did the same for four frameworks and one agent, as a mapping file with a row for every element and its status.

From paper, in both directions at once: sgit.ai's newsroom roles are written as files, and the check that gates a release reads them. In the words of the check itself, "The policy is the `writes` and `edits` lists in `admin/content/newsroom/roles/<role>.md`, the same files the `/newsroom/policies.html` table is generated from." One source, rendered as a page people read and as a check a release must pass. That is the pattern I would want for every agent: the ABP is the source, the table and the code are renderings, and neither can drift from the other because neither is edited by hand.

## Why it needs fractal semantic graphs {#fsg}

A round trip like this breaks if every format has to share one schema. A board policy is written in the board's words; a regulation in the legislator's; a control spreadsheet in the auditor's; an ABP in reach, mandate, gap and barrier; Rego in packages, rules and conditions. Asking any of them to adopt the others' vocabulary is why mapping exercises become workshops.

[Fractal semantic graphs](/articles/introducing-fractal-semantic-graphs.html) are the answer this site has been building: "Zoom into any node and you enter a new world with its own node types, its own verbs, its own taxonomy." Each altitude keeps its own vocabulary; the edges between them are verbs with inverses, so a row answers a policy and the policy is answered by the row; a rule enforces a row and the row is enforced by the rule. Then the questions that matter are walks, not workshops. "A question can cross formats without a join table." Which board policies have no row? Which rows have no code? Which code has no row? Which rows are enforced only by code the agent's own account can change? And when a regulation changes, supersede the node, never delete it, and every row and rule that rested on it becomes the answer to a query.

That is what makes reverse engineering practical at scale: the code, the spreadsheet and the paper do not need to be converted, only connected. And it is what makes generation safe: the code that comes out carries an edge back to the row it came from, so the next person can ask why.

## The four jobs {#jobs}

The speaker's framing was policy as code as an enabler, a way to scale, an enforcer and a basis for decisions. With an ABP as the source, each one gets sharper.

- **Enabler.** A written mandate lets a team ship an agent without a review meeting per agent, because the review was of the policy. [The behaviour policy is the business logic](/articles/the-behaviour-policy-is-the-business-logic.html): writing it is the work.
- **Scaling.** One source, rendered into as many engines and agents as needed, versioned and diffable, with every generated rule traceable to its row.
- **Enforcer.** Rows compiled into boundaries, and the barrier column saying, honestly, which ones still are not. [Hope or enforcement](/articles/hope-or-enforcement.html) measured what that is worth: one agent's rules kept only by good behaviour fell from 97% to 23% as they moved into the platform.
- **Decision-maker.** Every decision returns the row it came from, allow, deny or ask, and every ask goes to a named person, as [The human in the loop](/articles/the-human-in-the-loop.html) argued, with the record of decisions moving the line over time.

## What this does not claim {#limits}

- **The round trip is a demonstration.** Five rows, a short generator and seven requests, run for this article; it is not a product, and real agents need their requests routed through the engine for any of it to bind.
- **The session table is one agent's.** Counted from this session's hooks, scripts, validators and configuration on 14 October 2026; other agents will look different, and I expect most to look similar.
- **The GitHub scope was not tested by trying.** It is how this session's access is configured; pushing to sgit.ai to prove it is exactly what the policy forbids.
- **Some rows will never be code.** That is a feature of the method, not a gap in it: an ABP says which rows rely on a person.
- **The speaker is not named.** I took the idea from a talk and have not checked how they would put it.

If you have policies in code, spreadsheets or paper and want to see the agent behaviour policy they imply, or the code an ABP implies, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, from an event where a speaker described policy as code as a way to scale governance and AI innovation; written by this site's agent in the voice of this site, and the argument and the editorial responsibility are mine. The round trip was run for this article with Open Policy Agent 1.21.2: a JSON file of five rows from this session's policy, a generator written for the purpose, `opa check`, `opa eval` on seven requests and `opa parse` to read it back. The session table is from this session's own policy (v0.3, eleven rules), its hooks, its leak scan, sgit.ai's validator and policy check, and its git configuration. OPA's description is from its [philosophy page](https://www.openpolicyagent.org/docs/philosophy), read on 14 October 2026.
