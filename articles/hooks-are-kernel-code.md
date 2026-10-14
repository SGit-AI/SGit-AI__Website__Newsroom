# Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run, sgit.ai

> The hooks we are now going to deploy are code, and very critical code. They are also a very good example of code that is simple in many ways: a hook can be five lines. That makes them the best case study I can think of for everything we do on code review, code practices, semantic graphs and change blast radius, because the problem is small enough to do completely. A hook runs on every matching action, with the user's permissions, and can see, block or rewrite what the agent does; we should treat it like kernel code. Hooks also range from completely deterministic scripts to hooks that call a model or a whole agent, so I propose a maturity model: five levels from the prompt to off the machine, and three questions for every hook, how much power it has, which legs of the lethal trifecta it touches, and how much sandbox it runs in. I mapped the first ten: three this session runs, five tested in a sandbox, two proposed. They are between 4 and 26 lines, and the smallest of them depend on much more: the eleven-line commit hook calls a 37-line scan, so one line changed in the scan moves the commit gate for every session. And this is a brief for a site and a feed to manage them, like a skills manager: every hook from its intent, with its graph, tests, version and signature, installable anywhere, and a billing model where nobody pays to run a hook, but paying buys state.

*Source: <https://newsroom.sgit.ai/articles/hooks-are-kernel-code.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run

# Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.1.0, 2 versions](versions/hooks-are-kernel-code.md) · [newsroom v0.12.48](https://newsroom.sgit.ai/admin/versions.html) · hooksagentskernelmaturity-modelcode-reviewfractal-semantic-graphsblast-radiuslethal-trifectabillingagent-behaviour-policybriefarticle

***Abstract:** The hooks we are now going to deploy are code, and very critical code. They are also a very good example of code that is simple in many ways: a hook can be five lines. That makes them the best case study I can think of for everything we do on code review, code practices, semantic graphs and change blast radius, because the problem is small enough to do completely. A hook runs on every matching action, with the user's permissions, and can see, block or rewrite what the agent does; we should treat it like kernel code. Hooks also range from completely deterministic scripts to hooks that call a model or a whole agent, so I propose a maturity model: five levels from the prompt to off the machine, and three questions for every hook, how much power it has, which legs of the lethal trifecta it touches, and how much sandbox it runs in. I mapped the first ten: three this session runs, five tested in a sandbox, two proposed. They are between 4 and 26 lines, and the smallest of them depend on much more: the eleven-line commit hook calls a 37-line scan, so one line changed in the scan moves the commit gate for every session. And this is a brief for a site and a feed to manage them, like a skills manager: every hook from its intent, with its graph, tests, version and signature, installable anywhere, and a billing model where nobody pays to run a hook, but paying buys state.*

The first ten hooks. Three this session runs, five tested in a sandbox, and two proposed: a hook that checks the other hooks, and an agent hook that reviews a push on the most capable model, read-only and without network. Between 4 and 26 lines of code each, and every one runs on every matching action, with the user's permissions.

## In short

- **Hooks are code, and critical code.** Small, and with kernel reach: every matching action, the user's permissions, the power to block or rewrite.
- **The best case study we have.** Small enough to apply code review, graphs and change blast radius completely.
- **Deterministic and not.** A hook can be five lines of script, or a call to a model, or an agent that runs other agents.
- **A maturity model.** Five levels from the prompt to off the machine, and three questions: power, the lethal trifecta, the sandbox.
- **The first ten, mapped.** 4 to 26 lines each; the eleven-line commit hook calls a 37-line scan.
- **Hooks of hooks.** A hook that checks the other hooks; a scan that several hooks depend on. The graph is fractal.
- **A site and a feed.** Every hook from its intent, with its graph, tests, version and signature, like a skills manager.
- **Pay for state, never to run.** Installs are free and work offline; paying buys history, alerts, attestations and updates.

## Kernel code

[Agent hooks in October 2026](agent-hooks-october-2026.md) mapped what hooks can do, and [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md) moved this site's own rules into them. Now we are going to deploy them, and that changes how they should be treated.

A hook is fundamentally code. But look at where it runs. It is called by the harness on every matching event, before and after every tool call, at every prompt and every stop. It runs with the user's permissions. It sees the action in the agent's own terms, and it can block it, ask a person, or rewrite what the model reads. In an operating system, the code with that position is the kernel. [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md) put it plainly: "An operating system has two hard walls, the kernel and the user." Hooks are the agent's kernel, and today we write them like scripts.

So we should manage them like kernel code. As small as possible. Reviewed by more than one person. Versioned, tested against fixed inputs on every change, signed, installed where the agent cannot write, and rolled out with care. And we should map their deployment and the harness around them, not only their source.

## The best case study we have

They are also the best case study I can think of for the way we want to do code review. The work on [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md), which started at [secrets.sgit.ai](https://secrets.sgit.ai/) in its [review graphs](https://secrets.sgit.ai/review/), draws a change from the method it touched up to the stories that can reach it. On a large codebase that graph is big. A hook can be five lines. The whole graph, from the intent it serves to every line it runs and everything it calls, fits on one page, so we can do all of it, completely, and show it working.

Here is what the first ten look like (figure above). The three this session runs are in one 216-line file: re-anchoring the policy after a summary in 9 lines, the prompt summary in 14, and the stop check in 26. The five tested in [the sandbox](are-hooks-the-sweet-spot.md) are 4 to 17 lines each. And the two I propose are the interesting ones:

- **A hook of hooks.** A hook at session start that checks every installed hook against a signed list of hashes, and refuses to start if one has changed. It is the integrity check the others need, and it is itself a hook.
- **A security review agent.** An agent hook, which Claude Code's reference describes as one that can "spawn a subagent that can use tools like Read, Grep, and Glob to verify conditions before returning a decision", reviewing a push before it leaves. This is where the most capable model belongs: a security review should be as effective as possible. It is also where the reach must be smallest: read-only tools, no network.

## Hooks of hooks

The size on the page is not the size of the hook. The eleven-line commit hook does one thing: it runs the leak scan. The scan is 37 lines, reads a list of secrets and a list of names that live elsewhere, and decides what a secret looks like. In the sandbox, that is where the gap was: the scan let a GitHub token shape through because its patterns were written for this site's own secrets. The hook was correct; the code below it was not complete.

That is the fractal part. A hook calls a script, which reads configuration, which someone maintains. A hook can call other hooks, a model, or an agent that runs other agents in sequence. So each hook needs its graph: the intent it serves, a row of a behaviour policy; the event and matcher it sees; what it calls; what it reads; what it can decide. And with the graph, the change blast radius becomes a walk. In the code review article's words, "The blast radius of a change is the climb from the methods it touched to the stories that can reach them". Change one pattern in the shared scan, and the climb reaches the commit gate for every session that installs it. Change the hook's matcher, and it reaches every event it stops seeing. Some changes are a line and some are large; the graph shows which is which, whatever the size of the diff.

## A maturity model

A maturity model for hooks: five levels of how a rule is kept, from the prompt to off the machine, and three questions for every hook at every level: its power, the legs of the lethal trifecta it touches, and its sandbox. The less deterministic a hook is, the less it should be able to reach.

Hooks run from completely deterministic to completely not. Claude Code lists five kinds of handler: a command, an HTTP call, an MCP tool, a prompt hook, which sends "a prompt to a Claude model for single-turn evaluation", and an agent. There is a time and a place for each, including the ones that look like black magic. So the model has two parts.

The levels say how the rule is kept, building on the barrier types of a behaviour policy:

- **L0, in the prompt.** No hook; the model keeps the rule or not.
- **L1, a model decides.** A prompt or agent hook; non-deterministic, useful where judgement is the point.
- **L2, a deterministic script.** Same input, same answer; usually installed where the agent can edit it, and failing open by default.
- **L3, managed and proven.** Tested with fixtures, versioned, signed, installed by the organisation where the agent cannot write, and failing closed.
- **L4, off the machine.** The same rule in a gateway or the service itself, with the hook kept as an early warning.

And three questions for every hook, at any level. How much power does it have: observe, add context, ask, block, rewrite, act? Which legs of the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) does it touch: private data, untrusted content, the ability to communicate out? And how much sandbox is it in: network, filesystem, which model? The rule of thumb that comes out of it is simple. The less deterministic a hook is, the less it should be able to reach. A five-line script that blocks a push can run anywhere. An agent hook that reads the diff should have no network at all. Full internet access for an agent inside a hook is, to me, hard to justify.

All ten hooks in the figure are L2 or proposed. None is L3 yet: this session's own hooks live in a folder the agent can write. Getting them to L3 is the first job of the site below.

It is the same move [Sovereignty is the ability to move](sovereignty-is-the-ability-to-move.md) made with a maturity model for every dependency: say where each one is today, and what the next level needs.

## Where hooks run

Hooks also need somewhere to run that is not the developer's machine. The isolated environments that companies such as Chainguard now ship for agents, mapped in [Chainguard, mapped](chainguard-mapped.md), are a natural place: an environment where every run is isolated and produces a signed record of what ran is exactly where a hook's tests should run, and where an agent hook that should not touch the network can be kept from it. Whether hooks can run inside those environments, and with what attestation, is part of the research for the site.

## A site and a feed

A hooks site and feed, run like a kernel tree. Every hook starts as an intent, a row of a behaviour policy, and is published with its graph, tests, version and signature. The feed lists every hook with its level, power, trifecta legs, version and hash; the change blast radius view climbs from a change to the intents and sessions it affects; installs are free and can run inside an organisation with no call home; paying buys state.

So the proposal is a site and a feed to manage the hooks we deploy, the hooks equivalent of a skills manager. [A policy for every skill](a-policy-for-every-skill.md) argued that "Skills are the new dependency"; hooks are the dependency that guards the others. Every hook on the site starts from an intent, the row of the behaviour policy it serves, and carries its graph, its fixtures, its version, its hash and its signature. The feed is one file that people, agents and installers can read:

```

{
  "id": "scan-before-commit",
  "intent": "ABP v0.3 rule 2: leak scan before every commit",
  "event": "PreToolUse", "matcher": "Bash", "when": "git commit",
  "handler": "command", "lines": 11,
  "calls": ["leakscan.sh (37 lines)"], "reads": ["secrets list", "names list"],
  "power": "block", "level": "L2", "next_level": "L3: managed install, fail closed",
  "trifecta": {"private_data": true, "untrusted_content": false, "communicates_out": false},
  "network": false, "model": null,
  "fixtures": {"must_block": ["AWS example key"], "must_allow": ["clean change"], "known_gap": ["GitHub token shape"]},
  "version": "0.1.0", "status": "tested"
}

```

## Pay for state, never to run

The site should also have a billing model from the start, and the same principle as the reading meter on sgit.ai: nobody is forced to pay. [Pay after you read](pay-after-you-read.md) described "a balance that never blocks", and [Pay to keep your persona](pay-to-keep-your-persona.md) argued that "readers should pay because it helps them, not because they feel they should". For hooks, what helps is state.

Installing and running a hook is free, and it works offline, including deployed inside an organisation with no call home. If you choose to report usage, every decision a hook makes, which hook, which rule, allow or block, becomes a record. And the record is what is worth paying for: the history of every decision, alerts when a hook blocks something important, the footprint of what the agent actually did compared with the policy it runs under, signed attestations of which hook versions ran, and managed updates when a hook changes. If you do not report, nothing is tracked, and you do not get any of that. The more state the site can keep for you, the more reason there is to pay for it.

## The brief

*For the session that builds the hooks site. Written by @newsroom.writer for Dinis Cruz, 14 October 2026, on top of v0.12.47.*

1. **The ten hooks as code.** A repository with the ten hooks in the figure, each with its fixtures; the five sandbox hooks and their fixtures are the start. The two proposed ones are built here: the integrity hook first.
2. **A record per hook.** The JSON shape above: intent, event, handler, lines, calls, reads, power, level, trifecta, network, model, fixtures, version, status.
3. **The graph per hook.** From the intent to every line and everything called, in the fractal semantic graph shape this site already uses.
4. **Change blast radius.** For every change to a hook or anything it calls, the climb to the intents and installs it affects, shown on the change.
5. **Releases like a kernel tree.** Tests on every change; a version, a hash and a signature per release; the integrity hook checks them at session start.
6. **The feed and the site.** `hooks.json` and a page per hook. Where it lives is the owner's call; abp.sgit.ai, where the behaviour policy is published, is a natural home.
7. **Install.** Managed settings for a team, with only managed hooks allowed and failures set to block; a path to L3 for this session's own hooks.
8. **Billing.** A usage record that is off by default and never blocks; what reporting buys, listed plainly.
9. **Research.** Whether hooks and their tests can run inside isolated agent environments with signed records, and which hook collections exist to learn from.

What to be careful about. Hooks are kernel code: no hook is published without fixtures, and no change to a shared script ships without its blast radius. Nothing in the feed or a usage record carries a key, a secret or the content the hook saw, only the decision. The security review agent runs read-only with no network. And the site publishes defensive hooks, not ways around them.

## What this does not claim

- **Nothing in the brief is built.** The site, the feed, the graph per hook and the billing are proposals.
- **The ten hooks are this session's.** Three in use, five tested on fixed inputs, two proposed; none is L3.
- **Line counts are non-blank code lines.** The three session hooks were counted inside their shared file.
- **The maturity model is a proposal.** Its levels build on the barrier types this site uses; others would draw them differently.
- **The memo was cut short.** It was exported before it finished; this covers what it said.
- **Corrected on 14 October.** The first version said the review work started on sgit.ai; it started at secrets.sgit.ai, now linked.

If you are deploying hooks and want to manage them like kernel code, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The hooks were written and counted in this session, and the handler types are from Anthropic's [Claude Code hooks reference](https://code.claude.com/docs/en/hooks), read the same day. The billing principle is from this site's reading meter articles, linked above.

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#hooks-are-kernel-code)

### Builds on

- [Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail](agent-hooks-october-2026.md) A debrief on agent hooks across ten platforms: what each can see, stop and change, where they run, and the failure modes every vendor admits.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in](chainguard-mapped.md) Chainguard mapped from OS to agents, its public feeds counted, and the context layer above the package where an open policy and a vault fit.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.

### Continued by

- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 120 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=120)

**Posting this article on LinkedIn?** The cover is [hooks-are-kernel-code.jpg](banners/hooks-are-kernel-code.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/hooks-are-kernel-code.html)*
