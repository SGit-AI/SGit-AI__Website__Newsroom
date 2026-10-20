# A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills, sgit.ai

> I saw a video today that said "1 in 20 Claude skills are built to hack your computer". It is an overstatement of a real study, and the real finding is interesting enough: in one large study of public marketplaces, 5.2% of the skills analysed showed "high-severity patterns strongly suggesting malicious intent". It made me think about what an agent behaviour policy can do for skills. A skill behaviour policy looks at three things. The mandate the description promises; the mandate the skill actually has, from what its instructions and files can do, treated as features; and the grant, which depends on where it runs. The gap between the first two is the suspicious part; the gap between the last two is the reach nobody asked for. Then the policy becomes a control: a hook and a sandbox setting, generated from the described mandate, that bring the grant down to what you expected. I built a static calculator and ran it on 899 public skills from three sources: 812 can reach something beyond their own scripts, 782 of them through one third-party tool server, and 39 have a feature their description does not mention. None was obfuscated. The clearest case was honest: a skill that reads your Claude Code chat history, searches HackerNews and sends a report to Slack has the whole lethal trifecta, says so, and still needs a control. NVIDIA's scanner rated it safe, which is right for the question a scanner asks. A policy asks a different one.

*Source: <https://newsroom.sgit.ai/articles/skill-behaviour-policy.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills

# A skill behaviour policy: what a skill says it does, what it can do, what it is given, and the control that closes the gap, measured on 899 skills

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/skill-behaviour-policy.md) · [newsroom v0.12.51](https://newsroom.sgit.ai/admin/versions.html) · agent-skillsskill-behaviour-policyagent-behaviour-policyhookssandboxlethal-trifectasupply-chainskillspectormcparticle

***Abstract:** I saw a video today that said "1 in 20 Claude skills are built to hack your computer". It is an overstatement of a real study, and the real finding is interesting enough: in one large study of public marketplaces, 5.2% of the skills analysed showed "high-severity patterns strongly suggesting malicious intent". It made me think about what an agent behaviour policy can do for skills. A skill behaviour policy looks at three things. The mandate the description promises; the mandate the skill actually has, from what its instructions and files can do, treated as features; and the grant, which depends on where it runs. The gap between the first two is the suspicious part; the gap between the last two is the reach nobody asked for. Then the policy becomes a control: a hook and a sandbox setting, generated from the described mandate, that bring the grant down to what you expected. I built a static calculator and ran it on 899 public skills from three sources: 812 can reach something beyond their own scripts, 782 of them through one third-party tool server, and 39 have a feature their description does not mention. None was obfuscated. The clearest case was honest: a skill that reads your Claude Code chat history, searches HackerNews and sends a report to Slack has the whole lethal trifecta, says so, and still needs a control. NVIDIA's scanner rated it safe, which is right for the question a scanner asks. A policy asks a different one.*

A skill behaviour policy: three mandates, two gaps, one control. What the description says, what the skill's files and instructions can do, and what the environment grants. Actual minus described is the suspicious part; grant minus actual is the reach nobody asked for; the control brings the grant down to the described mandate.

## In short

- **The claim, corrected.** Not 1 in 20 Claude skills built to hack you: 5.2% of 31,132 marketplace skills in one study showed patterns "strongly suggesting malicious intent".
- **Three mandates.** Described, actual and granted; the gaps between them are the findings.
- **Features, not verdicts.** An upload can be exfiltration or a login; the policy records which, and why.
- **The grant depends on where it runs.** On Claude Code, a skill has the network of any program; in the API, none.
- **Measured on 899 skills.** 812 can reach beyond their own scripts; 782 through one third-party tool server; 39 with an undescribed feature; none obfuscated.
- **An honest skill can still need a control.** Chat history in, HackerNews in, Slack out: the whole lethal trifecta, all described.
- **The policy becomes a control.** A hook and a sandbox setting, generated from the description and tested on fixed inputs.
- **A scanner and a policy answer different questions.** One asks if a skill looks malicious; the other asks what it needs and what it gets.

## The claim, and what the study found

The video said "1 in 20 Claude skills are built to hack your computer", and connected it to a scanner. Both halves need correcting. The number comes from [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338), a study published in January that ran its own scanner, SkillScan, over public marketplaces: "collecting 42,447 skills from two major marketplaces and systematically analyzing 31,132". It found "26.1% of skills contain at least one vulnerability", and "5.2% of skills exhibit high-severity patterns strongly suggesting malicious intent". So: marketplace skills, not Claude's own; suggesting intent, not proving it. The scanner in the video is a different tool, NVIDIA's [SkillSpector](https://github.com/NVIDIA/SkillSpector), built to check skills before they are installed or published; NVIDIA did not produce that number.

The corrected version is still worth taking seriously, and the study's own phrase is the reason: skills "execute with implicit trust and minimal vetting". Anthropic's guidance says the same thing from the other side: "Use Skills only from trusted sources", and treat installing one like installing software.

## Three mandates

A skill is instructions an agent follows, often with scripts beside them, with whatever reach the agent has. [A policy for every skill](a-policy-for-every-skill.md) described Sean Turner's control for reviewing contributed skills against a written policy. This is the measurement underneath it: three mandates for every skill.

- **The described mandate.** What the description promises. It is the only part a person reads when choosing a skill, and the only part the agent reads until the skill is used.
- **The actual mandate.** What the instructions and bundled files can make the agent do: reach the network, upload, read credentials, read outside the workspace, install packages, change shell startup files, call a remote tool server. Each is a feature, found in the text.
- **The grant.** What the environment lets it do, which is different in each place. Anthropic's documentation is plain about it: on Claude Code, "Skills have the same network access as any other program on the user's computer"; through the API, skills run in "a sandboxed container with no network access"; on claude.ai, network access follows the workspace's settings.

Two gaps fall out. Actual minus described is the part to look at: features the description never mentions. Grant minus actual is the reach nobody asked for: even an honest skill, on a laptop, runs with everything the agent can do. In the language of this site's [behaviour policies](footprint-and-blast-radius.md), the mandate is smaller than the reach, and the difference is the risk.

One detail makes the grant worse than it looks. A skill can declare `allowed-tools`, and it does not mean what it sounds like: Claude Code's documentation says "It does not restrict which tools are available", it pre-approves them, and "A skill can grant itself broad tool access". A skill can widen its own grant.

## Features, not verdicts

The important design choice is that every finding is a feature, not a verdict. A skill that uploads a file to a URL could be stealing data, or logging you into an account to do what you asked. A skill that reads `~/.claude` could be harvesting your sessions, or analysing your work because you asked it to. Context decides, and the policy is where the context is written down: each feature becomes a row, with what it does, why the description needs it, and whether the description says so at all. A feature the description explains is a row with a reason. A feature it does not explain is a finding.

## 899 skills, read statically

899 skills from three public sources, every file read as text and nothing run: what they can reach, and what their descriptions leave out. 812 can reach something beyond their own scripts, 782 of them through one third-party tool server; 39 have a feature their description does not mention; none was obfuscated, and none sets allowed-tools.

So I built the calculator's first half and ran it. It reads a skill folder as text, never runs anything, finds features by pattern in the instructions and every bundled file, finds the features the description declares by its words, and reports the difference. I ran it on three public sources, read on 14 October: Anthropic's own [skills repository](https://github.com/anthropics/skills) (20 skills), a popular methodology collection, [obra/superpowers](https://github.com/obra/superpowers) (15), and a large community catalogue, [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (864).

- **812 of 899 can reach something beyond their own scripts.** Network, installs, credentials, files outside the workspace, or a remote tool server.
- **782 do it through one third-party tool server.** Most of the community catalogue is instructions only: 850 of its 864 skills ship no code, and 778 declare that they need the same remote MCP server, which holds the connections to each service. The reach of those skills is not in the skill at all; it is whatever accounts you have connected to that server.
- **39 have a feature their description does not mention.** Mostly installs (a PDF skill that runs `pip install`), paths outside the workspace, and example credentials in reference files. Ten name a service but not the third-party server every call goes through; nine of them are business and finance skills, such as QuickBooks, NetSuite, Xero, Ramp and Coinbase.
- **None was obfuscated, and none sets `allowed-tools`.**

These are curated public sources, not a marketplace sample, so the absence of obvious malice is what you would expect. What they show is the other thing: how often the description and the reach differ, even when everyone means well.

## One skill, end to end

One skill, end to end: developer-growth-analysis. An honest description and the whole lethal trifecta: it reads your Claude Code chat history, searches HackerNews, and sends a report to Slack through a third-party tool server. The policy states the minimal grant and the reach on Claude Code, and generates a hook, tested on nine fixed inputs, with what it cannot see and what stays an expectation.

The clearest case in the set was an honest one. `developer-growth-analysis` describes itself as a skill that "Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a personalized growth report to your Slack DMs." Its instructions read `~/.claude/history.jsonl`, search HackerNews and post to Slack, all through a third-party tool server. That is [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), private data, untrusted content and a way out, in one skill, and the description says so. The only thing it leaves out is the server in the middle.

Its skill behaviour policy is short. The minimal grant: read one file, run a search, send one message to yourself. The reach on Claude Code: the network of any program, every file you can read, including the rest of `~/.claude` and `~/.ssh`, and every account you have connected to the server. Four rows: read only the history file outside the workspace; ask before anything is sent; treat HackerNews text as data, not instructions; never touch shell startup files.

From those rows I generated a hook and tested it on nine fixed inputs, the JSON the harness would send. It allowed reading the history file, the search, and a write in the workspace. It denied reading an SSH key, `cat .env`, any other file under `~/.claude`, and writes to `~/.bashrc` and `~/.zshrc`. And it asked before the tool server's execute call, because that is where a message leaves.

The policy also says what the hook cannot do. A hook sees the tool call, not what a script does once it runs, so the network of scripts belongs to the sandbox, where Claude Code can limit shell commands to an allowlist of domains. And the tool server itself runs outside the sandbox ("The sandbox covers shell commands only. Claude's file tools, MCP servers, and hooks run outside it."), so its calls can be asked about, not blocked by the network. The row about HackerNews text stays an expectation: nothing outside the model can see whether it obeyed a page. That row is the honest statement of where the remaining risk is, which is the job [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md) gave the barrier column, and the reason [Hooks are kernel code](hooks-are-kernel-code.md) wants these hooks managed like kernel code.

## A scanner and a policy

I ran NVIDIA's SkillSpector, version 2.12.0, on five of the same skills, with `--no-llm`, which its README describes as the way "to keep contents local (static analysis only)". The two tools agreed where they looked at the same thing, and differed where they ask different questions.

- **developer-growth-analysis.** Score 8, low, recommendation "SAFE", with one medium finding on "automatically send", flagged as autonomous decision making. The policy finds the whole trifecta and a third-party server.
- **langsmith-fetch.** Score 18, with a high finding: a YARA rule for backdoor persistence matched the line that tells you to append your API key to `~/.bashrc`. The policy found the same line: a write to a shell startup file, and a secret stored in plain text, neither mentioned in the description. Same line, different words; the policy's are the more accurate here, because the instruction is to help you, and the risk is real anyway.
- **The PDF skill.** A medium finding that it "declares no tool scope ('permissions' or 'allowed-tools')". A declared scope is good for intent, but on Claude Code `allowed-tools` pre-approves rather than restricts, so declaring it would widen the grant. The control has to come from somewhere else.
- **connect and quickbooks-automation.** Score 0 for both, no findings. The policy finds a described mandate of "Gmail, Slack, GitHub, Notion, and 1000+ services" for one, and an accounting system reached through an undescribed third party for the other.

This is not a criticism of the scanner, and its optional model stage may find more. A scanner asks whether a skill looks malicious, and for these skills the right answer is mostly no. A policy asks what the skill needs, what it gets in this environment, and what control makes the two meet. NVIDIA's own framing of verified skills fits the second question: "Verified skills govern capabilities that enter the workflow."

## A service, and a standard

Put together, this is a service we can offer and an open format we can publish. For any skill: the described mandate, the actual mandate with its evidence, the minimal grant, what more it could do on Claude Code, on claude.ai and through the API, and the hook and sandbox settings that bring the grant down to what the description promised, with their tests. The calculator is static and cheap; a model can read the description against the features where judgement helps; the controls are generated, tested and published, the way [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) generated Rego from rows. And the same policy is what a company like Chainguard, whose agent skills product plans to let organisations "define and enforce their own skill security policies", as [Chainguard, mapped](chainguard-mapped.md) quoted, would need written down.

## What this does not claim

- **Pattern matching gives lower bounds.** The calculator finds features by text patterns; it misses what it has no pattern for, and some matches are examples in documentation.
- **Three curated sources, not a marketplace.** The 899 are public collections read on 14 October 2026; marketplace rates will differ.
- **The policy and the hook are for one skill.** The rows were written for this article; the hook was tested on fixed inputs, not in a live session.
- **SkillSpector ran without its model stage.** Five skills, static only; its full mode may find more.
- **No skill here is called malicious.** A feature is a feature until the context says otherwise.

If you publish skills, review them for an organisation, or want a policy and a control for the ones you run, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, after a video and a fact-check thread, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The calculator, the policy and the hook were built for this article; the skills were downloaded into an isolated folder and read as text, never run. A research agent verified the study, the scanner and the documentation, and the quotes were checked on the pages themselves. Liu et al., [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338), January 2026; NVIDIA, [SkillSpector](https://github.com/NVIDIA/SkillSpector) and [verified agent skills](https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/); Anthropic, [Claude Code skills](https://code.claude.com/docs/en/skills), [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [sandboxing](https://code.claude.com/docs/en/sandboxing). All read on 14 October 2026.

## Threads

Agents & policy[This article as a graph →](graphs.md#skill-behaviour-policy)

### Builds on

- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in](chainguard-mapped.md) Chainguard mapped from OS to agents, its public feeds counted, and the context layer above the package where an open policy and a vault fit.

### Continued by

- [A briefing for the WestCap CISO Summit: what RiskMandate and Agent Behaviour Policies are, said for each kind of person in the room, where we add value, and what to read next](a-briefing-for-the-ciso-summit.md) A briefing for the WestCap CISO Summit: Agent Behaviour Policies and RiskMandate, said for six kinds of person in the room, with what to read next.
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP](cedar-and-the-policy-vault.md) Cedar is mature and adopted; it lacks the why, the version in force and the evidence. A vault carries all three, and the demo shows it working.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 123 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=123)

**Posting this article on LinkedIn?** The cover is [skill-behaviour-policy.jpg](banners/skill-behaviour-policy.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/skill-behaviour-policy.html)*
