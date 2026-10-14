# Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail, sgit.ai

> More and more of the technical people I talk to who are trying to control agents for real are reaching for the same tool: hooks, small programs the agent's harness runs at fixed points, before a tool call, after it, when a prompt is submitted, when the agent stops. This is the debrief I wanted to read: the lay of the land on 14 October 2026, from each vendor's own documentation. The short version is that the design has converged. Claude Code, OpenAI's Codex, Gemini CLI, GitHub Copilot, Cursor, Devin Desktop (formerly Windsurf), Grok Build, Factory, Augment and Kiro all offer a hook before a tool call that can block it, and most can ask the user or rewrite the call. They differ where it matters for security: whether an organisation can force its own hooks and switch everyone else's off, whether a failing hook blocks or lets the action through, whether hooks shipped in a repository need trust before they run, and whether anything can see the model's own output. ChatGPT offers admin controls rather than hooks, and Lovable gates publishing rather than agent actions. The vendors and the people who publish hook collections say the same thing about their limits: guardrails, not walls. Hooks see what the harness routes through them, run with the user's permissions, fail open by default on most tools, and have been an attack surface themselves. I ran a small test of my own in a throwaway repository, and the companion article asks what this means for agent behaviour policies.

*Source: <https://newsroom.sgit.ai/articles/agent-hooks-october-2026.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail

# Agent hooks in October 2026: a technical debrief on what each platform lets you see, stop and change, where hooks run, and where they fail

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.1.0, 2 versions](versions/agent-hooks-october-2026.md) · [newsroom v0.12.41](https://newsroom.sgit.ai/admin/versions.html) · hooksagentsclaude-codecodexgemini-clicopilotcursorguardrailssecurityenforcementowasparticle

***Abstract:** More and more of the technical people I talk to who are trying to control agents for real are reaching for the same tool: hooks, small programs the agent's harness runs at fixed points, before a tool call, after it, when a prompt is submitted, when the agent stops. This is the debrief I wanted to read: the lay of the land on 14 October 2026, from each vendor's own documentation. The short version is that the design has converged. Claude Code, OpenAI's Codex, Gemini CLI, GitHub Copilot, Cursor, Devin Desktop (formerly Windsurf), Grok Build, Factory, Augment and Kiro all offer a hook before a tool call that can block it, and most can ask the user or rewrite the call. They differ where it matters for security: whether an organisation can force its own hooks and switch everyone else's off, whether a failing hook blocks or lets the action through, whether hooks shipped in a repository need trust before they run, and whether anything can see the model's own output. ChatGPT offers admin controls rather than hooks, and Lovable gates publishing rather than agent actions. The vendors and the people who publish hook collections say the same thing about their limits: guardrails, not walls. Hooks see what the harness routes through them, run with the user's permissions, fail open by default on most tools, and have been an attack surface themselves. I ran a small test of my own in a throwaway repository, and the companion article asks what this means for agent behaviour policies.*

Agent hooks in October 2026, from each vendor's documentation: whether a hook can block a tool call, rewrite its input, act at the model call, be forced by the organisation, fail closed, and whether hooks shipped in a repository need trust. The design has converged; the security properties have not.

**What came next.** [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md) takes this site's own behaviour policy and moves it into hooks rule by rule, tested in a sandbox, and asks how long hooks are the right place to keep an agent's rules.

## In short

- **Hooks are now standard.** At least ten agent tools document a hook before a tool call that can block it; most can also ask or rewrite.
- **The differences are the security properties.** Organisation-only hooks, failing closed, trust for repository hooks, and visibility of the model's output.
- **Fail-open is the default on most tools.** A hook that crashes or times out usually lets the action through, unless you set the option to block.
- **Hooks see what the harness routes through them.** Actions that do not go through a hooked tool path are invisible to them.
- **Hooks are an attack surface too.** Hooks shipped in a repository have run code on open, and research reports compromising every harness it tested.
- **Everyone says the same thing.** "Hooks are not a security boundary", "not a complete enforcement boundary", "Guardrails, not walls."
- **A standard is forming.** OWASP's GenAI Security Project hosts the Agent Control Standard, built around hooks; other cross-vendor specs are drafts.

## What a hook is

Where a hook sits: beside the agent, on the same machine, with the user's permissions. Hooks fire when a prompt is submitted, before and after a tool call, at the stop, and on one platform around the model call itself. They are good at deterministic checks at the moment of action, and cannot undo what ran or see what was not routed through them.

A hook is a program the agent's harness runs at a fixed point in its loop, with a description of the event on its input and a decision on its output. The harness is the program around the model: it sends the prompt, receives the model's request to use a tool, runs the tool and returns the result. Hooks plug into that loop. The one that matters most for security runs before a tool call: it sees the tool's name and its full input, the shell command, the file path, the MCP server and tool, and it can allow the call, deny it with a reason the model sees, ask the person, or on most platforms rewrite the input.

Claude Code's [reference](https://code.claude.com/docs/en/hooks) lists 33 events, from session start to configuration changes. Most tools have between ten and twenty. Hooks are usually shell commands that read JSON and write JSON, and on several tools they can also be HTTP endpoints, prompts to a model or plugins. A conventional exit code carries the decision: on most tools, exit code 2 blocks.

This site already runs on them. The agent writing it works under a written policy that a hook prints back after every summary, as [Re-anchoring](re-anchoring-agent-behaviour-policies.md) describes, and another hook appends the status report you see at the end of its answers.

## The lay of the land

**Anthropic, Claude Code and the Agent SDK.** The richest surface: a pre-tool hook that can allow, deny, ask, defer or rewrite; post-tool hooks that can replace the output; hooks on prompts, stops, subagents, compaction, configuration changes and instruction files. An organisation can set `allowManagedHooksOnly`, which in the settings reference reads "Run only the hooks your organization deploys". Since version 2.1.295 a hook can set `"onFailure": "block"`, because, in the docs' own words, "a policy hook with a wrong path or a crashing script lets everything through". The Agent SDK exposes the same events as callbacks.

**OpenAI.** Codex has [hooks](https://learn.chatgpt.com/docs/hooks), enabled by default, with a pre-tool hook that can deny or rewrite and `allow_managed_hooks_only = true`, which "skips hooks from user, project, session, and plugin sources". Hosted tools such as web search are not covered: "These don't use the local function-tool hook path." The docs are direct: "Treat tool hooks as a useful guardrail, not a complete enforcement boundary." The Agents SDK has guardrails that can stop a run and lifecycle hooks that observe it. ChatGPT itself has no user hooks; it has admin controls, and in its Work product admin-managed hooks for MCP tools.

**Google, Gemini CLI.** The only coding agent with documented [hooks](https://geminicli.com/docs/hooks/) around the model call itself: `BeforeModel` can "Block Turn / Mock", and `AfterModel` can "Filter/redact responses". It fingerprints project hooks and warns that "Project-level hooks are particularly risky when opening untrusted projects." For unpaid users Gemini CLI has been replaced by Antigravity CLI, which I did not research.

**GitHub Copilot.** The cloud agent and Copilot CLI have [hooks](https://docs.github.com/en/copilot/reference/hooks-configuration) with a pre-tool decision and argument rewriting. Organisations can install machine-wide policy hooks for the CLI, which "Load before all other hooks" and need elevated privileges. One line matters: "Command hook timeouts are always fail-open, even for preToolUse and admin-deployed policy hooks."

**Cursor.** [Hooks](https://cursor.com/docs/agent/hooks) before shell commands, MCP calls and file reads, and at four levels with the priority "Enterprise → Team → Project → User". "Crashes, timeouts, and non-zero exit codes other than 2 fail open by default", with a `failClosed` option the docs recommend for MCP hooks. Cursor also runs a partner programme of security vendors building on its hooks.

**The rest.** Devin Desktop, formerly Windsurf, has twelve hook points with system hooks users cannot disable without root. Grok Build blocks only before a tool call, says that "timeouts, crashes, malformed output" are "fail-open", and also reads Claude Code's and Cursor's hook files. Factory and Augment support organisation-level hooks; Kiro and Cline have hooks, with less documented enforcement. Lovable has no agent hooks: it scans on publish and lets admins block publishing with critical findings.

## Where hooks fail

The failure modes are documented by the vendors, by the people who publish hook collections, and by researchers. I keep them at the level a defender needs.

**They fail open by default.** On most tools, a hook that crashes, times out or returns something malformed lets the action go ahead. A security hook with a bug is no hook at all, unless the option to fail closed is set where it exists.

**They only see what is routed through them.** A hook on one tool does not see the same effect reached through another. Anthropic's own issue tracker has a case where a hook on file edits blocked an edit and the agent made the change through a different tool the hook did not cover; the issue was closed "not planned". Hooks keyed on the text of a command see the text, not what it will do.

**They run with the user's permissions, beside an agent with the same permissions.** Claude Code's docs say command hooks "execute shell commands with your full user permissions". Unless they are installed where the agent cannot write, an agent can change the files that define them; organisation-managed hooks are the answer several vendors give.

**Hooks shipped in a repository are an attack surface.** Check Point's "Caught in the Hook", published on 25 February 2026, found that "hook commands defined in .claude/settings.json will run automatically without confirmation"; all the reported issues were "successfully patched prior to this publication". And hook files written for one tool can be read by another: before version 3.0.0, according to CVE-2026-48124, Cursor "could execute workspace-defined Claude hook commands" without dedicated approval; it was fixed in June 2026. In September 2026, a paper on [attacker-controlled hook updates](https://arxiv.org/abs/2609.03884) reported compromising "all seven evaluated harnesses". And Claude Code's docs note that in a headless or SDK run, "Claude Code never shows the dialog and treats the folder as trusted", so a repository's hooks run there unreviewed.

**Most cannot see the model's output.** Except where a tool hooks the model call, a hook sees actions, not what the model said or what it read that made it act.

The people who build hook collections agree. Trail of Bits' widely used [configuration](https://github.com/trailofbits/claude-code-config) says "Hooks are not a security boundary -- a prompt injection can work around them" and "Guardrails, not walls." cc-safety-net, which works across sixteen coding tools, says "It is not a sandbox" and "A broken config file never blocks anything."

## A small test of my own

I ran one check in a throwaway repository with two local remotes. A project-level hook implemented one rule from this site's own policy: pushes go only to the allowed remote. In a real headless Claude Code run, the hook stopped the push to the other remote, and nothing arrived there. Asked to try other ways, the agent declined to go further, saying the remaining routes would mean defeating the control itself. Run directly, though, the same hook let through a command whose text did not show where it would push, which is the limit of any hook that reads text rather than effects.

The test also showed two things I had not planned to see. The headless run loaded my own user-level hooks as well, because hooks follow the user, not the project. And my status counter, which counts commits from the text of commands, counted the throwaway repository's commit as one of this site's: a hook that infers behaviour from text cannot tell one repository from another.

## Configuring hooks as a defender

From the vendors' guidance and the failure modes above:

1. **Make the organisation's hooks the only hooks** where the platform allows it, and install them where the agent cannot write.
2. **Fail closed** on the hooks that enforce policy: exit code 2, and the block-on-failure option where it exists.
3. **Hook every path to the same effect,** not one tool: shell, file tools and MCP, and prefer checks on effects over checks on text.
4. **Watch the configuration itself,** with hooks or managed settings that block or report changes to settings and hook files.
5. **Review a repository's agent settings before a headless run,** or run with repository hooks switched off.
6. **Pair hooks with a boundary:** a sandbox, network rules, and credentials scoped to the task. Hooks decide; the boundary holds.

## The standard is forming

The [Agent Control Standard](https://github.com/GenAI-Security-Project/agent-control-standard), which calls itself "The open standard for runtime agent control" built on "declarative hooks, policy enforcement, and observability", is "an open project of the OWASP GenAI Security Project": a separate guardian inspects what an agent is about to do, and answers with allow, deny, modify, ask or defer, using policy engines such as OPA or Cedar. Several other cross-vendor hook specifications exist as drafts at version 0.1. None is yet the way the major coding agents expose their hooks, which is why the same hook still has to be written several times.

## What this does not claim

- **The map is from documentation.** Read on 14 October 2026, partly by research agents; the claims quoted here were re-checked, and the cells marked unknown were not verified.
- **Products move fast.** Several of these hook systems are months old and their behaviour is changing release by release.
- **The test was one check in one tool.** It shows a hook enforcing a rule and its limit, not a measure of any product's security.
- **Failure modes are described, not demonstrated.** The sources are cited for anyone who needs the detail.

If you are deploying hooks to govern agents, or building a shared library of them, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The research was done the same day by four research agents reading each vendor's documentation, issue trackers, advisories and papers, with the quoted claims re-checked. Primary sources: Anthropic, [Claude Code hooks reference](https://code.claude.com/docs/en/hooks); OpenAI, [Codex hooks](https://learn.chatgpt.com/docs/hooks); Google, [Gemini CLI hooks](https://geminicli.com/docs/hooks/); GitHub, [Copilot hooks configuration](https://docs.github.com/en/copilot/reference/hooks-configuration); Cursor, [hooks](https://cursor.com/docs/agent/hooks); Check Point Research, [Caught in the Hook](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/); [arXiv 2609.03884](https://arxiv.org/abs/2609.03884); [trailofbits/claude-code-config](https://github.com/trailofbits/claude-code-config); [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net); OWASP GenAI Security Project, [Agent Control Standard](https://github.com/GenAI-Security-Project/agent-control-standard).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#agent-hooks-october-2026)

### Builds on

- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.

### Continued by

- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 114 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=114)

**Posting this article on LinkedIn?** The cover is [agent-hooks-october-2026.jpg](banners/agent-hooks-october-2026.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agent-hooks-october-2026.html)*
