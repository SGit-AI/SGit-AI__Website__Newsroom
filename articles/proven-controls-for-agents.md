# Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break, sgit.ai

> Two pieces reached me on the same day and they belong together. Hem Pant, a CISO who has spent two decades leading security at global banks, wrote that policies don't protect institutions, proven controls do, and asked for one unbroken line from Board intent to live evidence, with every control tested by a deliberately non-compliant change that fails the build if it is not caught. Sondera's paper on the autoformalization of agent instructions into policy-as-code does a large part of that line for agents: it turns an agent's prompt, its tool descriptions and a policy document into Cedar policies, checks them with a hard and a soft critic, and enforces them outside the context window, failing closed. I agree with both, and this is the unifying theme: the policy has to leave the PDF and the prompt and become something that runs and can be tested. What I would add, from what we run every day with Agent Behaviour Policies, is one column both leave open: who holds each control. A rule the agent can change or skip is a Setting, and a test proves only that it ran; a rule held from above the agent is a Boundary, and only that can be proven not to be switched off. Our own numbers show why it matters: when this newsroom walked its 57 checks up to the behaviours they protect, 22 were expectations, 34 settings and one a boundary. So here is the line with that column added, what we have generated, mapped and enforced, and six controls we tried to break, including the release gate that failed our own build tonight. And an answer to Hem's invitation for a common, machine-readable way to express controls and evidence: the Agent Behaviour Policy is an open project, and its process form now has a written standard with test vectors.

*Source: <https://newsroom.sgit.ai/articles/proven-controls-for-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break

# Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-29 · [article v1.0.0](versions/proven-controls-for-agents.md) · [newsroom v0.13.133](https://newsroom.sgit.ai/admin/versions.html) · governance-as-codepolicy-as-codeagent-behaviour-policycedarassurancecontrolssharnessagentsarticle

***Abstract:** Two pieces reached me on the same day and they belong together. Hem Pant, a CISO who has spent two decades leading security at global banks, wrote that policies don't protect institutions, proven controls do, and asked for one unbroken line from Board intent to live evidence, with every control tested by a deliberately non-compliant change that fails the build if it is not caught. Sondera's paper on the autoformalization of agent instructions into policy-as-code does a large part of that line for agents: it turns an agent's prompt, its tool descriptions and a policy document into Cedar policies, checks them with a hard and a soft critic, and enforces them outside the context window, failing closed. I agree with both, and this is the unifying theme: the policy has to leave the PDF and the prompt and become something that runs and can be tested. What I would add, from what we run every day with Agent Behaviour Policies, is one column both leave open: who holds each control. A rule the agent can change or skip is a Setting, and a test proves only that it ran; a rule held from above the agent is a Boundary, and only that can be proven not to be switched off. Our own numbers show why it matters: when this newsroom walked its 57 checks up to the behaviours they protect, 22 were expectations, 34 settings and one a boundary. So here is the line with that column added, what we have generated, mapped and enforced, and six controls we tried to break, including the release gate that failed our own build tonight. And an answer to Hem's invitation for a common, machine-readable way to express controls and evidence: the Agent Behaviour Policy is an open project, and its process form now has a written standard with test vectors.*

Hem Pant's LinkedIn article of 29 October 2026: Policy, Standard, Control, Evidence.

## In short

- **Two pieces, one theme.** Hem Pant's governance as code and Sondera's policy-as-code paper both say the policy has to become something that runs and can be tested.
- **Hem asks for proof, not presence.** "Most organisations can show that a control exists. Far fewer can prove it works."
- **Sondera turns agent instructions into enforced policy.** Prompt, tools and policy documents become Cedar, enforced outside the context window.
- **Agents need one more column: who holds each control.** A control the agent can change is a Setting; only a Boundary can be proven not to be switched off.
- **The policy has to come first.** Policy as code answers "is this allowed?"; the mandate says why, and what nothing can see.
- **Proven means tried and broken.** Six of our controls, with the deliberate violations and what happened, misses included.
- **Tonight our own gate proved itself.** The release to main failed on a change it was built to catch.
- **There is an answer to Hem's invitation.** An open behaviour policy format, and a standard with test vectors.

## Two pieces that belong together

Hem Pant [published on LinkedIn](https://www.linkedin.com/pulse/policies-dont-protect-institutions-proven-controls-do-hem-pant-9pjee) on 29 October 2026, from "more than two decades leading security at global banks". His starting point will be familiar to anyone who has sat through an audit: "We write excellent policies. Committees approve them. Then the estate moves on, and the policy stays still." When a supervisor asks to be shown that a control works, "teams go looking for screenshots." His answer is to treat policies, standards and architecture as code, on "One unbroken line, from Board intent to live evidence": Policy, Standard, Control, Evidence.

On the same day, Sondera's paper, [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649) by Adam Mondl, Matthew Maisel and John H. Brock, accepted at an ICML 2026 workshop, reached me too. It is the same idea applied to agents, and it is a serious piece of work.

Sondera's paper on arXiv: agent instructions turned into Cedar policies by a generator-critic loop.

I think there is a unifying theme here, and it is the one we have been working on all year with [Agent Behaviour Policies](https://riskmandate.ai/abp.html): a policy that lives in a PDF, or in a prompt, is read and hoped for; a policy that runs can be checked, and a policy that runs and is tested can be proven. Both pieces make that move. What I would like to add is what we have learned from doing it with agents, every day, on our own work, with real examples rather than a framework.

## What Hem asks for

Hem's line is worth stating precisely, because each step is a commitment. "Every statement a Board approves links to a requirement. Every requirement links to controls that prevent (in the deployment pipeline), detect (in the live environment) and guard (across the organisation). Every control produces evidence automatically and continuously." One control can then answer ISO 27001, NIST CSF, NCSC CAF, the CRI Profile, cloud security standards and DORA at once. "No screenshots. No archaeology. One version of the truth."

Then the sentence I think matters most: "Most organisations can show that a control exists. Far fewer can prove it works." And his test for it: "Every control must catch a deliberately non-compliant change. If it doesn't, the build fails." He expects leading institutions to "Use AI agents to maintain the governance estate, with humans approving every change", and he ends with a challenge and an invitation. The challenge: "pick one policy. Trace it to one live control. Prove that control catches a breach." The invitation, to regulators, standard-setters and technology partners: "the industry would benefit from a common, machine-readable way to express controls and evidence."

I agree with all of it. And I think agents make it both more urgent and more possible: more urgent because an agent changes the estate faster than any team, and more possible because an agent's reach can be measured, written down and held, row by row.

## What Sondera built

Sondera's paper does a large part of Hem's line for an agent. Its starting point is the same diagnosis: "most existing approaches either rely on probabilistic guardrails (fine-tuned classifiers, prompt-based steering) that offer no formal guarantees, or on hand-coded symbolic enforcement that does not scale to the breadth of real policy specifications."

Their pipeline, which they call the Verification Sandwich, takes an agent's system prompt, its MCP tool definitions and a natural-language policy document, and turns them into policies in Cedar, the policy language AWS open-sourced. A grounding layer generates a Cedar schema from the tool definitions. A model generates candidate policies. A hard critic, Cedar's own tooling, checks syntax, schema, contradictions and vacuous policies, and a soft critic, an LLM as judge, checks that the policies still mean what the text meant. At run time, a deterministic engine evaluates every tool call. The paper's own sentence on why that matters: "Because the policies sit outside the context window and are enforced by a deterministic policy evaluator, an attacker cannot 'convince' the security layer to ignore its rules." And it fails closed: if the engine or the harness errors, the action is blocked.

The results are on MedAgentBench, a benchmark of tool-using medical-records agents, against a synthetic policy of 88 rules for which prior work had hand-coded guardrails for 23. The autoformalized policies covered more of the 88, and blocked 85.7% (42 of 49) of the adversarial trajectories that got past the prior work's hard gating; counting only trajectories that attempted a write, the block rate was between 94.0% and 100%. The paper is honest about what Cedar cannot see: it "can deny tool calls but not dialog-only behavior", and it is stateless, so rules about ordering and memory across a session are future work. And they released the [harness](https://github.com/sondera-ai/sondera-harness-python) as open source.

This is close to what we have been arguing. In [system prompts as behaviour policies](system-prompts-as-behaviour-policies.md) we took a published system prompt of 4,255 words, found 82 rules in it, and sorted them: 36 could be held by the harness rather than by the model's good behaviour. In [Cedar and the policy vault](cedar-and-the-policy-vault.md) I said Cedar is the policy language we should adopt rather than compete with. Sondera has built the bridge from the prompt to Cedar, and measured it.

## One line, with the column agents add

Put the two side by side, and add what we run, and Hem's line has a fourth row and one new column.

Hem Pant's line from Board intent to evidence, with Sondera's pipeline, our work, and who holds each rule.

For an agent, Hem's **policy** is the mandate: what the business asked the agent to do, and why. His **standard** is the rows: each capability the agent can reach, with its limit and the reason it exists. His **control** is the barrier on each row. His **evidence** is a deliberate violation, refused, with the record of who refused it. That is the shape of an Agent Behaviour Policy: the mandate, the grant (what the agent can actually reach, measured), the delta between them, and the barrier on each capability.

The column that both pieces leave open is in the barrier: **who holds the control**. Our behaviour policies give it four values. **None**. An **Expectation**, which is prose the agent reads. A **Setting**, which is a control the subject could change or skip: a hook in the agent's own harness, a check in a pipeline the same team can edit, a sandbox setting in the agent's own configuration. And a **Boundary**, held from above the subject, by something it does not include.

This is the difference between Hem's "exists" and "works", made precise. An Expectation can be shown to exist; a screenshot does that. A Setting can be shown to have run. Only a Boundary can be shown to hold when the subject would rather it did not, which is the case that matters when the subject is an agent that a web page has just talked into something.

We measured how far our own agents are from that. When this newsroom walked its 57 checks up to the behaviours they protect, in [behaviour policies from the checks](behaviour-policies-from-the-checks.md), 22 were expectations, 34 were settings, and one was a boundary: the session's GitHub access scoped to one repository. The CI checks are settings, because the validator, the tests and the workflow live in the same repository the agent pushes to. In [policy as code needs a policy first](policy-as-code-needs-a-policy-first.md), of one session's eleven rules, eight had code behind them, and only one had code the agent could not change. That is a real organisation, ours, honestly counted.

## Where Sondera's control sits

This is where I would build on Sondera's work rather than argue with it. Their policies sit outside the context window, so the model cannot talk its way past them. That is exactly right, and it is the first adversary. There is a second one: the process. An agent that is allowed a shell, or a tool that runs code, can do things no tool-call policy sees, and a policy check that runs as middleware inside the agent's own process is, in our terms, a Setting for whoever controls that process.

The harness's own README gives a good example of the gap: a Cedar `forbid` whose condition is `context.parameters_json like "*rm -rf*"`, with the line "This policy stops your agent from running `rm -rf`, every time." It stops that string. The same command written as `rm -fr`, or `rm -r -f`, does not contain it. That is not a flaw in Cedar or in Sondera's pipeline; it is what happens to any rule written about a command's text. Our design work on [the decision at the door](https://sharness.ai/design/decision/index.html) puts it in one line: "A parser is not a sandbox." A rule about intent belongs at the policy engine, and the kernel bound behind it is what holds when the rule is routed around.

That is why we built [SHarness](introducing-sharness.md), which we released today: the same behaviour policy, executed as a Process Behaviour Policy on every process the agent starts, hashed to one name the person supplies from outside, and enforced by the Linux kernel or by a small separate service the agent cannot reach. The two fit together well. Sondera's Cedar decides which tool calls are allowed, in the business's own nouns. SHarness makes sure that, whatever the tool does once it runs, it can only write where the policy says, connect where it says, and never reach the key. Its landscape page already lists Cedar under the engines whose decisions it should consume, not replace, and its `policy translate` command is the kind of bridge a Cedar policy set could go through.

And the other direction matters too. Sondera's fail-closed rule covers an engine that errors. One thing we found when we put Cedar policies in a versioned vault, in [Cedar and the policy vault](cedar-and-the-policy-vault.md), is subtler: Cedar skips a single policy whose evaluation errors, so a `forbid` that refers to a missing attribute lets the action through, with the error only in the diagnostics. Sondera's hard critic validates the schema before deployment, which is exactly the mitigation. It is the kind of thing Hem's test would find, which is the point of the test.

## Controls we proved by trying to break them

Hem's test is the right one, so here it is applied to our own agents. Each of these is published with its method, misses included.

Six of our controls, each tested with a deliberate violation, and what happened, misses included.

- **A leak hook.** In [can a key leak without breaking the policy?](a-leak-without-breaking-the-policy.md) we wrote a hook and tried nine ways for a secret to leave an agent's session. It stopped five, let an ordinary command through, and missed three: a key in base64, a key split in two, and a file of secrets piped out. With four more rules, it caught all nine. Then we ran it over the 3,451 real commands of the session that wrote that article: it refused 22, and none was ordinary work.
- **Policy as code, both ways.** Five rows of a real behaviour policy became a 35-line Rego policy; Open Policy Agent decided seven requests, denying three, asking for one and allowing three. Parsing it back found a row with no code and a rule with no row, the two gaps that matter.
- **Cedar in a vault.** An old-shape request against a new `forbid` was allowed, for the reason above. Validate before you deploy, and deny on error.
- **Our own 57 checks.** One boundary, honestly counted.
- **SHarness `hello`.** Six probes under a deny-all policy: a read allowed, two writes, a network connect, a 400 MiB allocation under a 128 MiB cap and a wrong policy hash, all refused, each result naming who refused it, the kernel or the tool. It held six of six in five places on 25 October, and again tonight in a Linux kernel booted inside a browser tab.
- **Our release gate.** Tonight, the release of this site to its main branch failed. One agent's commit had set the version to the pending placeholder without regenerating the front page, so the page no longer matched its sources. The test that regenerates the page caught it, the build failed on dev and on main, nothing was released, and the fix was one line. Hem's sentence, "If it doesn't, the build fails", is not hypothetical here. It is what happened at about eleven o'clock tonight.

The last one is also a lesson about the column. That gate is a Setting: it lives in the repository the agents push to. It held because nobody tried to weaken it. A Boundary would hold even if someone did.

## The policy comes first

One more thing I would add to both pieces, from [policy as code needs a policy first](policy-as-code-needs-a-policy-first.md). Policy as code answers one question very well: is this request allowed? The questions a board, an auditor or an insurer asks are the ones around it. What can this agent reach, measured? What was it asked to do, and why? Where do the two differ? Which rules can no engine ever see? And, for every rule that is code, who can change that code?

That is why the mandate has to be written first, and why it has to say why. Sondera's soft critic checks that a Cedar policy still means what the text meant; a mandate with a reason on every row is what makes that check possible for a person too. It is also what lets the line run in both directions: from the policy, generate the code; from the code, reverse-engineer the policy, and see the rows nobody wrote a reason for.

It is also what makes the evidence worth something. In [a payout for every row](a-payout-for-every-row.md) I argued that an agent behaviour policy can be read as an insurance policy, row by row, and that "A line in the prompt earns nothing": only a control that something enforces lowers a row's premium. Hem's "defensible decisions" and an insurer's price are the same thing seen from two sides.

## Humans approving every change

Hem expects agents to maintain the governance estate, with humans approving every change. That is how this site already runs, and it is worth saying what "approving" has to mean for it to be a control rather than a ritual.

A person cannot approve two hundred policies, or read every diff an agent produces. What works, in [approve at altitude](approve-at-altitude.md), is approving at the right level: the board signs off its appetite once, a function its budget and licence to operate within it, a team its workflow within that, and each level may narrow the one above and never widen it. SHarness does the same with a policy: a person can write one sentence, "contain my agent to this workspace, these sites, these secrets", and approve its hash, and every level below it is compiled from that sentence and checked against the hash. The approval is one value the agent cannot change. That is a human approving every change, at a cost a human can actually pay.

## An answer to the invitation

Hem invites "regulators, standard-setters and technology partners" to a common, machine-readable way to express controls and evidence. I would like to take him up on it, with what already exists.

The [Agent Behaviour Policy](https://riskmandate.ai/abp.html) is being [moved to the Open Security Summit](agent-behaviour-policies-move-to-the-open-security-summit.md) as an open project, because a description of what an agent can do should not belong to the company that sells it. Its process form, the Process Behaviour Policy, has a [written standard](https://sharness.ai/code/standards/policy-v0/index.html) for its canonical form and hash, with 28 test vectors that the Python, JavaScript and Go implementations all pass, so a policy hashed in one language is the same policy in another. And Cedar, which Sondera targets, is the language I think the rules themselves should be written in where an engine decides them.

So the pieces of Hem's line exist for agents: the mandate and the rows, written and open; generation into Cedar, measured by Sondera; enforcement from above, released today in SHarness; and evidence by deliberate violation, in public. What is missing is the conversation that joins them, and I would very much like to have it.

## Hem's challenge, taken

"Pick one policy. Trace it to one live control. Prove that control catches a breach." Here is ours.

The policy: an agent may write only in its workspace and may reach only the sites it was given. The live control: SHarness's shell, where the agent's process runs as a user made for it, in a network namespace with only loopback, and its only way out is a network door with a host allowlist. The breach: a request to a host off the list, and a direct connection to an address, bypassing the door. On 29 October, sharness.ai's own agent recorded it: pypi.org allowed through the door, example.com refused, a direct connect to 1.1.1.1 refused, and a name lookup found nothing. And the honest finding, which Hem's challenge is designed to surface: today that is a Boundary for the shell the tool starts, not yet for the agent itself, because the launcher that would sit above the agent is still the design. If you cannot prove it, Hem says, "that may be your most important finding this year." This is ours, and it is written down.

## What this does not claim

- **It reads Hem's article and Sondera's paper as published.** Nothing here is their view of our work.
- **Sondera's figures are theirs.** They are from the paper, on its benchmark and its synthetic policy; they were not re-run here.
- **The `rm -rf` example is from the harness's README.** It illustrates a limit of rules about a command's text, not a measured weakness of Sondera's product.
- **Our tests are on our own agents.** One newsroom and one project; each is published with its date and method.
- **Most of SHarness is designed, not built.** The kernel locks, two doors and the levels run; the launcher above the agent does not.
- **The open project is a proposal in progress.** The Agent Behaviour Policy's move to the Open Security Summit needs its charter and steering group written down.

If you are working on governance as code, policy as code for agents, or the evidence a supervisor would accept, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

My request of 29 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Hem Pant's article, [Policies don't protect institutions. Proven controls do.](https://www.linkedin.com/pulse/policies-dont-protect-institutions-proven-controls-do-hem-pant-9pjee), was read in full on 29 October 2026; the quotes are his, and the screenshot of its opening is from my phone. Sondera's paper, [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649) (arXiv:2606.26649, submitted 25 June 2026, accepted at the Second Workshop on Agents in the Wild, ICML 2026), was read in full the same day from its PDF, and the README of the [Sondera Harness](https://github.com/sondera-ai/sondera-harness-python) from GitHub. On this site: [introducing SHarness](introducing-sharness.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [policy as code needs a policy first](policy-as-code-needs-a-policy-first.md), [Cedar and the policy vault](cedar-and-the-policy-vault.md), [system prompts as behaviour policies](system-prompts-as-behaviour-policies.md), [can a key leak without breaking the policy?](a-leak-without-breaking-the-policy.md), [a payout for every row](a-payout-for-every-row.md), [approve at altitude](approve-at-altitude.md) and [Agent Behaviour Policies move to the Open Security Summit](agent-behaviour-policies-move-to-the-open-security-summit.md). The release gate's failure is runs 395 and 397 of this site's pipeline, fixed in v0.13.132.

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#proven-controls-for-agents)

### Builds on

- [System prompts as behaviour policies: Claude's published prompt and a leaked ChatGPT one, mapped into rows, a taxonomy of rules, and a JSON file a harness could enforce](system-prompts-as-behaviour-policies.md) Claude's published system prompt as 82 policy rows in eight kinds: 36 could be held by the harness, 21 partly by classifiers, 25 stay with the model.
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP](cedar-and-the-policy-vault.md) Cedar is mature and adopted; it lacks the why, the version in force and the evidence. A vault carries all three, and the demo shows it working.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [Agent Behaviour Policies move to the Open Security Summit: the first hosted project of a community interest company, with RiskMandate as a founding contributor](agent-behaviour-policies-move-to-the-open-security-summit.md) The Agent Behaviour Policy moves to the Open Security Summit CIC as its first hosted project, with a charter and an independent steering majority to come.

### Continued by

- [Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today](lovable-with-sharness.md) Lovable with SHarness, and the trojanised Claude Code extension: where a policy boundary has to sit, and what SHarness can stop today.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 324 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=324)

**Posting this article on LinkedIn?** The cover is [proven-controls-for-agents.jpg](banners/proven-controls-for-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/proven-controls-for-agents.html)*
