# Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine, sgit.ai

> Most of the rules we give agents today are hope-based security: written in the prompt, kept only if the model keeps them. The agent writing this site works under a behaviour policy of eleven rules, and only one of them is kept by something other than the agent. So I asked the question directly: in October 2026, are hooks the sweet spot? Can we move the rules out of the prompt and into small deterministic programs the agent's harness runs before and after every action, and keep them there until enforcement moves into a gateway or the platform itself? I took this session's own policy and tried, rule by rule, in a throwaway repository. Four rules moved into hooks fully, two mostly, three partly and two not at all, and the tests found a gap in the check I trust most. Hooks are the first layer that does not rely on the model and the last that still sees the action in the agent's own terms, which is why I think they are the right place to start, provided they are installed where the agent cannot edit them and set to fail closed. The open hook collections that exist block dangerous commands; the step that is missing is generating hooks from a written policy, and testing them, so the same rules can later be enforced by a gateway. We already need this for our own agents, so we can be among its heaviest users.

*Source: <https://newsroom.sgit.ai/articles/are-hooks-the-sweet-spot.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine

# Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/are-hooks-the-sweet-spot.md) · [newsroom v0.12.43](https://newsroom.sgit.ai/admin/versions.html) · hooksagentsagent-behaviour-policyenforcementpolicy-as-codeclaude-codeguardrailsowaspsecurityarticle

***Abstract:** Most of the rules we give agents today are hope-based security: written in the prompt, kept only if the model keeps them. The agent writing this site works under a behaviour policy of eleven rules, and only one of them is kept by something other than the agent. So I asked the question directly: in October 2026, are hooks the sweet spot? Can we move the rules out of the prompt and into small deterministic programs the agent's harness runs before and after every action, and keep them there until enforcement moves into a gateway or the platform itself? I took this session's own policy and tried, rule by rule, in a throwaway repository. Four rules moved into hooks fully, two mostly, three partly and two not at all, and the tests found a gap in the check I trust most. Hooks are the first layer that does not rely on the model and the last that still sees the action in the agent's own terms, which is why I think they are the right place to start, provided they are installed where the agent cannot edit them and set to fail closed. The open hook collections that exist block dangerous commands; the step that is missing is generating hooks from a written policy, and testing them, so the same rules can later be enforced by a gateway. We already need this for our own agents, so we can be among its heaviest users.*

The eleven rules of this site's writing session, rule by rule. Today one rule is kept by a hook, one in part by a disabled push URL, and the rest by the agent's good behaviour. Moved into hooks and tested on fixed inputs in a throwaway repository: four fully, two mostly, three partly, two not at all.

## In short

- **Most agent rules are hope.** Written in the prompt, kept only if the model keeps them.
- **This session's own policy, measured.** Eleven rules; one kept by a hook, one in part by a setting, the rest by the agent.
- **Moved into hooks and tested.** Four fully, two mostly, three partly, two not at all.
- **The tests found a gap.** The leak scan blocked the key shapes it knows and let a GitHub token shape through.
- **Hooks sit at the right place, for now.** The first layer that does not rely on the model, and the last that sees the action as the agent meant it.
- **Only if the agent cannot edit them.** Installed by the organisation, outside the agent's reach, and set to fail closed.
- **The missing step is generation.** Hook packs exist; hooks generated from a written policy, with tests, mostly do not.
- **The same rules can move off the machine later.** A gateway answers the same allow, deny or ask.

## The question

[Agent hooks in October 2026](agent-hooks-october-2026.md) was the debrief: what each platform's hooks can see, stop and change, and where they fail. This is the question I actually wanted answered. Most of the rules we give agents today are what I call hope-based security. They are in the prompt, or in a policy the prompt points to, and they hold because the model follows them. [Hope or enforcement](hope-or-enforcement.md) measured how far that goes for one customer service agent: built the obvious way, 97% of its rules were kept only by the model's good behaviour.

Real enforcement will end up outside the agent: in a proxy that every tool call passes through, in the sandbox, in the platform, in credentials that cannot do the wrong thing. That is being built, and it is not where most teams are today. So, in October 2026, are hooks the sweet spot in between? How much of an agent's policy can move from the prompt into a hook now?

## This session's own policy

The agent writing this site works under an [agent behaviour policy](footprint-and-blast-radius.md) of eleven rules, and each rule says what keeps it: an expectation, which the agent keeps; a setting, which something configurable keeps; or a boundary, which is out of the agent's reach. Ten of the eleven say expectation. The one setting is the status report you see at the end of its answers: a hook supplies it, and a second hook, run when the agent stops, asks once if it is missing. In this session it has asked. One more rule is kept in part by a setting: the push URL for the sgit.ai repository is disabled, so a push there fails.

Everything else, never leaking a key, scanning before every commit, keeping model names out of commits, asking before opening a pull request, is the agent keeping its word. That has mostly worked, and not always. The commit that published the first hooks article today carried the wrong model name in its trailer. The rule says the trailer is the one the session gives; the leak scan looks for model ids, not names; nothing compared the two. It is a small slip, and exactly the kind a hook exists to catch.

## Rule by rule, in a sandbox

So I tried. In a throwaway repository with two bare remotes, one allowed and one forbidden, I wrote one small hook per rule and fed each one fixed inputs, the JSON a harness would send. My own session's settings were not changed.

- **Rule 2, the leak scan before every commit.** A hook before each shell command looks for `git commit` and runs the scan itself; if it fails, the hook exits with code 2 and the commit does not happen. It let a clean change through and blocked [AWS's documented example key](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html). It also let a GitHub token shape through, because the scan's patterns were written for this site's own secrets and do not know that shape. A hook is only as good as the check it runs.
- **Rule 5, no model ids outside the byline.** A hook reads the commit message: an id in the body was refused, the agreed byline allowed. Checking the trailer against the one the session was given is one more line.
- **Rule 9, release only to the newsroom.** Two layers. A hook before `git push` checks the remote, and git's own pre-push hook, in the repository, refuses any destination but the allowed one, by name or by URL, whatever started the push.
- **Rule 3, mask keys in output.** A hook after each command rewrites what the model reads, masking anything shaped like a key. The first version broke the output's shape; Claude Code's reference is clear that the replacement "must match the tool's output shape", and the fixed version keeps it. The same reference says what this cannot do: "The tool has already run by the time the hook fires."
- **Rule 7, no pull request or issue without asking.** A hook on those tools answers "ask", and the person decides. Contacting nobody and naming nobody on a private list stay judgement, with the leak scan checking the names.

The rest moved partly or not at all. Never leaking a key is covered where it would leave by a commit or reach the model, and not anywhere else. Using no credential but the session's own is better kept by not having other credentials in reach. Wording rules can be checked on the files an agent writes, and the site's validator already does part of it. Research before writing is judgement, not a check at a moment of action, and stays with the agent and the review.

## Where a hook sits

Where a rule can be kept. From the prompt, which sees everything and enforces nothing, through agent hooks and the tools' own hooks, to the sandbox, a gateway off the machine, and the service itself. Each layer down is harder for the agent to change and sees less of what the agent meant to do.

That result is why I think hooks are the sweet spot for now. They are the first layer that does not depend on the model: the same input gets the same answer every time, at no model cost. And they are the last layer that still sees the action as the agent meant it: a tool call by name, a commit with its message, a pull request with its title. A sandbox sees files and hosts. A gateway sees requests. Further down, enforcement is stronger and the intent is harder to read.

The limits are the ones the first article listed, and the vendors say them plainly. Trail of Bits, whose configuration ships two blocking hooks: "Hooks are not a security boundary -- a prompt injection can work around them." The safety net hook collection describes itself as "not a sandbox". On Claude Code, by default, "a policy hook with a wrong path or a crashing script lets everything through". And its sandbox has a matching limit in the other direction: "The sandbox covers shell commands only."

So a hook is a setting, in the policy's own terms, and what matters is who can change it. A hook in a file the agent can write is a setting the agent keeps, which is very close to an expectation. This session's own hooks live in a folder the agent can write. A hook the organisation installs where the agent cannot write, with only the organisation's hooks allowed to run (`allowManagedHooksOnly` in Claude Code, `allow_managed_hooks_only` in Codex) and a failure set to block (`onFailure` in Claude Code, `failClosed` in Cursor), is as strong as a hook gets. It still runs on the same machine with the user's permissions, and it still sees only what is routed through it. Git's own hooks have the same question: by default they live in `.git/hooks`, which the agent can usually write.

## Chained, not ordered

A policy of many rules becomes many hooks, so how they combine matters, and the platforms agree on more than I expected. On Claude Code, "All matching hooks run in parallel", and "When multiple PreToolUse hooks return different decisions, precedence is `deny` > `defer` > `ask` > `allow`." Cursor merges hooks from every source the same way: "any deny wins over ask, and ask wins over allow, regardless of source." Codex runs matching hooks concurrently, so one cannot stop another from starting.

That suits a policy. Each rule becomes one small hook with one job; they run side by side; the most restrictive answer wins. What it rules out is a chain where one hook depends on another's output, or on running first. A hook pack should be a set of independent checks, not a pipeline.

## Who else is doing this

The open collections that exist are mostly about dangerous commands. Trail of Bits' [configuration](https://github.com/trailofbits/claude-code-config) blocks `rm -rf` and direct pushes to the main branch. The [safety net](https://github.com/kenryu42/claude-code-safety-net) blocks destructive git and file commands and access to sensitive files, across several agents. [Lasso Security's hooks](https://github.com/lasso-security/claude-hooks) look for prompt injection in tool output: "The defender scans all tool outputs and warns Claude when suspicious patterns are detected." Those are good, and they are the same rules for everyone.

Generating hooks from a team's own rules has started too. [claudecode-rule2hook](https://github.com/zxdxjtu/claudecode-rule2hook) says: "Convert natural language project rules into Claude Code hooks automatically!" Anthropic's [hookify](https://github.com/anthropics/claude-code/tree/main/plugins/hookify) plugin writes rules from an instruction, or "Analyzes recent conversation" to find behaviour you corrected. Off the machine, AWS's [AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) does the same for a gateway: rules in plain English become Cedar, and every action through the gateway is "evaluated at the boundary" outside the agent's code. Docker's [MCP Gateway](https://docs.docker.com/reference/cli/docker/mcp/gateway/gateway_run) can block secrets and network access for the tools behind it.

And OWASP has the piece that joins them. The [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/), in the OWASP GenAI Security Project, "defines how agent platforms expose middleware hooks and how safety policies can be enforced through them". Its decisions are the hooks' decisions, allow, deny, modify, ask, defer, with a policy engine such as OPA or Cedar behind them. It is early, and its own [repository](https://github.com/GenAI-Security-Project/agent-control-standard) says so: "Two of ACS's nineteen hook methods are evaluated live". So the question is not whether OWASP should start a project on hooks; one exists, and the useful contribution is real policies and real hooks to test it with.

## A hook pack generated from a policy

What I have not found is the whole loop, and it is the one I would build. Start from the written policy, one row per rule, with its barrier. Generate one hook per row that can be checked at a moment of action, with fixed inputs that must be allowed and fixed inputs that must be blocked, run as tests on every change. Install the pack where the agent cannot write, with only managed hooks allowed and failures set to block. Then read the pack back against the policy, the same round trip [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) ran with Open Policy Agent: every rule with no hook is still hope, and every hook with no rule is a control nobody can explain.

The description stays the source, as Sean Turner's control for skills does in [A policy for every skill](a-policy-for-every-skill.md): change the rule, regenerate the hook, rerun the tests. And because a hook's answer is the same allow, deny or ask that a gateway gives, the same rows can later be compiled for the gateway, and each rule moves off the machine when something off the machine can keep it. The barrier column of the policy records where each rule is kept today, so moving a rule is one edit, and the gap it leaves is visible.

We already need this for our own agents, which is the best reason to build it. A session like this one, with a written policy, a leak scan, a release process and a report that proves the policy is still loaded, can be among the heaviest users of hooks, and every gap we find is one a customer does not.

## What this does not claim

- **The tests were fixtures, not a live harness.** Each hook was run on the JSON a harness would send, in a throwaway repository; the composition rules are from the vendors' documentation.
- **Hooks are not a boundary.** They run on the same machine with the user's permissions and see only what is routed through them; they make rules harder to break, not impossible.
- **The counts are for one policy.** Four, two, three and two are this session's eleven rules; another policy will divide differently.
- **The pack is a proposal.** The generator, the tests on every change and the gateway compilation are not built.
- **Collections and products move fast.** Read on 14 October 2026; star counts and features change.

If you are moving an agent's rules into hooks, or building the gateway they should move to next, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The hooks were written and tested for this article in a throwaway repository, against this session's own behaviour policy, without changing the session's settings. A research agent gathered the collections, gateways and standards, and the quotes were re-checked on the pages themselves. Anthropic, [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) and [sandboxing](https://code.claude.com/docs/en/sandboxing); OpenAI, [Codex hooks](https://learn.chatgpt.com/docs/hooks); Cursor, [hooks](https://cursor.com/docs/agent/hooks); OWASP GenAI Security Project, [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/). All read on 14 October 2026.

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#are-hooks-the-sweet-spot)

### Builds on

- [Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail](agent-hooks-october-2026.md) A debrief on agent hooks across ten platforms: what each can see, stop and change, where they run, and the failure modes every vendor admits.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.

### Continued by

- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [A briefing for the WestCap CISO Summit: what RiskMandate and Agent Behaviour Policies are, said for each kind of person in the room, where we add value, and what to read next](a-briefing-for-the-ciso-summit.md) A briefing for the WestCap CISO Summit: Agent Behaviour Policies and RiskMandate, said for six kinds of person in the room, with what to read next.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [The tokens hook: a token behaviour policy that shows what every session reads, caches, writes and costs, why a prompt cannot do it, and a brief for tokens.hook.sgit.ai](the-tokens-hook.md) A token behaviour policy as a 132-line hook: the user sees what each session reads, caches and costs; a prompt cannot do it.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills](skill-behaviour-policy.md) A skill behaviour policy compares what a skill says, what it can do and what it is given, then generates the control; measured on 899 skills.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [System prompts as behaviour policies: Claude's published prompt and a leaked ChatGPT one, mapped into rows, a taxonomy of rules, and a JSON file a harness could enforce](system-prompts-as-behaviour-policies.md) Claude's published system prompt as 82 policy rows in eight kinds: 36 could be held by the harness, 21 partly by classifiers, 25 stay with the model.
- [The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it](the-agents-write-too.md) The newsroom's agents get their own bylines: lessons every agent loads, debriefs as source material, a page for every agent, and a conductor.
- [Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail](agent-hooks-october-2026.md) A debrief on agent hooks across ten platforms: what each can see, stop and change, where they run, and the failure modes every vendor admits.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 115 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=115)

**Posting this article on LinkedIn?** The cover is [are-hooks-the-sweet-spot.jpg](banners/are-hooks-the-sweet-spot.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/are-hooks-the-sweet-spot.html)*
