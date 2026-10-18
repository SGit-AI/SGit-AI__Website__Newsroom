---
title: Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: The hooks we are now going to deploy are code, and very critical code. They are also a very good example of code that is simple in many ways: a hook can be five lines. That makes them a good case study for everything we do on code review, code practices, semantic graphs and change blast radius, because the problem is small enough to do completely. A hook runs on every matching action, with the user's permissions, and can see, block or rewrite what the agent does; we should treat it like kernel code. Hooks also range from completely deterministic scripts to hooks that call a model or a whole agent, so I propose a maturity model: five levels from the prompt to off the machine, and three questions for every hook, how much power it has, which legs of the lethal trifecta it touches, and how much sandbox it runs in. I mapped the first ten: three this session runs, five tested in a sandbox, two proposed. They are between 4 and 26 lines, and the smallest of them depend on much more: the eleven-line commit hook calls a 37-line scan, so one line changed in the scan moves the commit gate for every session. And this is a brief for a site and a feed to manage them, like a skills manager: every hook from its intent, with its graph, tests, version and signature, installable anywhere, and a billing model where nobody pays to run a hook, but paying buys state.
version: v0.12.80
license: https://creativecommons.org/licenses/by/4.0/
tags: hooks, agents, kernel, maturity-model, code-review, fractal-semantic-graphs, blast-radius, lethal-trifecta, billing, agent-behaviour-policy, brief, article
status: published
---

!shot hk-first10.webp | images/ | The first ten hooks. Three this session runs, five tested in a sandbox, and two proposed: a hook that checks the other hooks, and an agent hook that reviews a push on the most capable model, read-only and without network. Between 4 and 26 lines of code each, and every one runs on every matching action, with the user's permissions. | comparison

## In short {#in-short}

- **Hooks are code, and critical code.** Small, and with kernel reach: every matching action, the user's permissions, the power to block or rewrite.
- **A good case study.** Small enough to apply code review, graphs and change blast radius completely.
- **Deterministic and not.** A hook can be five lines of script, or a call to a model, or an agent that runs other agents.
- **A maturity model.** Five levels from the prompt to off the machine, and three questions: power, the lethal trifecta, the sandbox.
- **The first ten, mapped.** 4 to 26 lines each; the eleven-line commit hook calls a 37-line scan.
- **Hooks of hooks.** A hook that checks the other hooks; a scan that several hooks depend on. The graph is fractal.
- **A site and a feed.** Every hook from its intent, with its graph, tests, version and signature, like a skills manager.
- **Pay for state, never to run.** Installs are free and work offline; paying buys history, alerts, attestations and updates.

## Kernel code {#kernel}

[Agent hooks in October 2026](/articles/agent-hooks-october-2026.html) mapped what hooks can do, and [Are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html) moved this site's own rules into them. Now we are going to deploy them, and that changes how they should be treated.

A hook is fundamentally code. But look at where it runs. It is called by the harness on every matching event, before and after every tool call, at every prompt and every stop. It runs with the user's permissions. It sees the action in the agent's own terms, and it can block it, ask a person, or rewrite what the model reads. In an operating system, the code with that position is the kernel. [Why my agents do not run on my laptop](/articles/why-my-agents-do-not-run-on-my-laptop.html) put it plainly: "An operating system has two hard walls, the kernel and the user." Hooks are the agent's kernel, and today we write them like scripts.

So we should manage them like kernel code. As small as possible. Reviewed by more than one person. Versioned, tested against fixed inputs on every change, signed, installed where the agent cannot write, and rolled out with care. And we should map their deployment and the harness around them, not only their source.

## A good case study {#case-study}

They are also a good case study for the way we want to do code review. The work on [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html), which started at [secrets.sgit.ai](https://secrets.sgit.ai/) in its [review graphs](https://secrets.sgit.ai/review/), draws a change from the method it touched up to the stories that can reach it. On a large codebase that graph is big. A hook can be five lines. The whole graph, from the intent it serves to every line it runs and everything it calls, fits on one page, so we can do all of it, completely, and show it working.

Here is what the first ten look like (figure above). The three this session runs are in one 216-line file: re-anchoring the policy after a summary in 9 lines, the prompt summary in 14, and the stop check in 26. The five tested in [the sandbox](/articles/are-hooks-the-sweet-spot.html) are 4 to 17 lines each. And the two I propose are the interesting ones:

- **A hook of hooks.** A hook at session start that checks every installed hook against a signed list of hashes, and refuses to start if one has changed. It is the integrity check the others need, and it is itself a hook.
- **A security review agent.** An agent hook, which Claude Code's reference describes as one that can "spawn a subagent that can use tools like Read, Grep, and Glob to verify conditions before returning a decision", reviewing a push before it leaves. This is where the most capable model belongs: a security review should be as effective as possible. It is also where the reach must be smallest: read-only tools, no network.

## Hooks of hooks {#fractal}

The size on the page is not the size of the hook. The eleven-line commit hook does one thing: it runs the leak scan. The scan is 37 lines, reads a list of secrets and a list of names that live elsewhere, and decides what a secret looks like. In the sandbox, that is where the gap was: the scan let a GitHub token shape through because its patterns were written for this site's own secrets. The hook was correct; the code below it was not complete.

That is the fractal part. A hook calls a script, which reads configuration, which someone maintains. A hook can call other hooks, a model, or an agent that runs other agents in sequence. So each hook needs its graph: the intent it serves, a row of a behaviour policy; the event and matcher it sees; what it calls; what it reads; what it can decide. And with the graph, the change blast radius becomes a walk. In the code review article's words, "The blast radius of a change is the climb from the methods it touched to the stories that can reach them". Change one pattern in the shared scan, and the climb reaches the commit gate for every session that installs it. Change the hook's matcher, and it reaches every event it stops seeing. Some changes are a line and some are large; the graph shows which is which, whatever the size of the diff.

## A maturity model {#maturity}

!shot hk-maturity.webp | images/ | A maturity model for hooks: five levels of how a rule is kept, from the prompt to off the machine, and three questions for every hook at every level: its power, the legs of the lethal trifecta it touches, and its sandbox. The less deterministic a hook is, the less it should be able to reach. | architecture

Hooks run from completely deterministic to completely not. Claude Code lists five kinds of handler: a command, an HTTP call, an MCP tool, a prompt hook, which sends "a prompt to a Claude model for single-turn evaluation", and an agent. There is a time and a place for each, including the ones that look like black magic. So the model has two parts.

The levels say how the rule is kept, building on the barrier types of a behaviour policy:

- **L0, in the prompt.** No hook; the model keeps the rule or not.
- **L1, a model decides.** A prompt or agent hook; non-deterministic, useful where judgement is the point.
- **L2, a deterministic script.** Same input, same answer; usually installed where the agent can edit it, and failing open by default.
- **L3, managed and proven.** Tested with fixtures, versioned, signed, installed by the organisation where the agent cannot write, and failing closed.
- **L4, off the machine.** The same rule in a gateway or the service itself, with the hook kept as an early warning.

And three questions for every hook, at any level. How much power does it have: observe, add context, ask, block, rewrite, act? Which legs of the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) does it touch: private data, untrusted content, the ability to communicate out? And how much sandbox is it in: network, filesystem, which model? The rule of thumb that comes out of it is simple. The less deterministic a hook is, the less it should be able to reach. A five-line script that blocks a push can run anywhere. An agent hook that reads the diff should have no network at all. Full internet access for an agent inside a hook is, to me, hard to justify.

All ten hooks in the figure are L2 or proposed. None is L3 yet: this session's own hooks live in a folder the agent can write. Getting them to L3 is the first job of the site below.

It is the same move [Sovereignty is the ability to move](/articles/sovereignty-is-the-ability-to-move.html) made with a maturity model for every dependency: say where each one is today, and what the next level needs.

## Where hooks run {#where}

Hooks also need somewhere to run that is not the developer's machine. The isolated environments that companies such as Chainguard now ship for agents, mapped in [Chainguard, mapped](/articles/chainguard-mapped.html), are a natural place: an environment where every run is isolated and produces a signed record of what ran is exactly where a hook's tests should run, and where an agent hook that should not touch the network can be kept from it. Whether hooks can run inside those environments, and with what attestation, is part of the research for the site.

## A site and a feed {#site}

!shot hk-site.webp | images/ | A hooks site and feed, run like a kernel tree. Every hook starts as an intent, a row of a behaviour policy, and is published with its graph, tests, version and signature. The feed lists every hook with its level, power, trifecta legs, version and hash; the change blast radius view climbs from a change to the intents and sessions it affects; installs are free and can run inside an organisation with no call home; paying buys state. | architecture

So the proposal is a site and a feed to manage the hooks we deploy, the hooks equivalent of a skills manager. [A policy for every skill](/articles/a-policy-for-every-skill.html) argued that "Skills are the new dependency"; hooks are the dependency that guards the others. Every hook on the site starts from an intent, the row of the behaviour policy it serves, and carries its graph, its fixtures, its version, its hash and its signature. The feed is one file that people, agents and installers can read:

```json
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

## Pay for state, never to run {#billing}

The site should also have a billing model from the start, and the same principle as the reading meter on sgit.ai: nobody is forced to pay. [Pay after you read](/articles/pay-after-you-read.html) described "a balance that never blocks", and [Pay to keep your persona](/articles/pay-to-keep-your-persona.html) argued that "readers should pay because it helps them, not because they feel they should". For hooks, what helps is state.

Installing and running a hook is free, and it works offline, including deployed inside an organisation with no call home. If you choose to report usage, every decision a hook makes, which hook, which rule, allow or block, becomes a record. And the record is what is worth paying for: the history of every decision, alerts when a hook blocks something important, the footprint of what the agent actually did compared with the policy it runs under, signed attestations of which hook versions ran, and managed updates when a hook changes. If you do not report, nothing is tracked, and you do not get any of that. The more state the site can keep for you, the more reason there is to pay for it.

## The brief {#brief}

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

## What this does not claim {#limits}

- **Nothing in the brief is built.** The site, the feed, the graph per hook and the billing are proposals.
- **The ten hooks are this session's.** Three in use, five tested on fixed inputs, two proposed; none is L3.
- **Line counts are non-blank code lines.** The three session hooks were counted inside their shared file.
- **The maturity model is a proposal.** Its levels build on the barrier types this site uses; others would draw them differently.
- **The memo was cut short.** It was exported before it finished; this covers what it said.

If you are deploying hooks and want to manage them like kernel code, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, written by this site's writer agent in the voice of this site; the argument and the editorial responsibility are mine. The hooks were written and counted in this session, and the handler types are from Anthropic's [Claude Code hooks reference](https://code.claude.com/docs/en/hooks), read the same day. The billing principle is from this site's reading meter articles, linked above.
