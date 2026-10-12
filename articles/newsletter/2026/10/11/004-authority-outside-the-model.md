# Issue 4: Authority outside the model: Satya Nadella on models as insider risks, the platforms that now enforce, and the controls we run on our own agents, SGit Newsroom

> The CEO of one of the largest AI vendors published seven principles for treating models as insider risks, and Microsoft shipped containers and a control specification for agents. Both say what this network has been arguing: an agent's limits must sit outside the agent. Eight articles on what that means in practice. An answer to the seven principles, one by one, with what runs and what is only designed; the same argument translated into the language of behaviour policies; where the platform draws its line and why the business logic sits above it; ten hard questions for RiskMandate; and the controls we run on our own agents every day, from a second reader that fails closed to a desktop of their own.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/11/004-authority-outside-the-model.html> · sgit.ai v0.7.70 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 4

SGit Newsroom · Issue 4 · 2026-10-11

# Authority outside the model: Satya Nadella on models as insider risks, the platforms that now enforce, and the controls we run on our own agents

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** The CEO of one of the largest AI vendors published seven principles for treating models as insider risks, and Microsoft shipped containers and a control specification for agents. Both say what this network has been arguing: an agent's limits must sit outside the agent. Eight articles on what that means in practice. An answer to the seven principles, one by one, with what runs and what is only designed; the same argument translated into the language of behaviour policies; where the platform draws its line and why the business logic sits above it; ten hard questions for RiskMandate; and the controls we run on our own agents every day, from a second reader that fails closed to a desktop of their own.*

When an agent breaks a rule, the first question is who was keeping the rule. If the answer is the agent, it was not a rule, it was a hope. This week that argument went mainstream: Satya Nadella published seven principles for treating models as insider risks, and Microsoft shipped the containers to enforce some of them. This issue is eight articles on what it takes for an agent's limits to sit outside the agent. It is the second of three on what was published between 9 and 11 October, after [pay after you read](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/003-pay-after-you-read.html) and before [no server, by design](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/005-no-server-by-design.html).

Authority outside the model in six pictures, one from each of the first six articles

## Seven principles, answered

[Authority outside the model](https://newsroom.sgit.ai/articles/authority-outside-the-model.html) answers Satya Nadella's seven principles one by one: what stands behind each on this network today, what runs, what is a published design, and what is only argued, with a table that keeps the three apart. It names five things the list leaves out, starting with the mandate, because watching an agent tells you what it did, not whether it was allowed. Its core is the test this network has used for a while:

>

a control bounds a grant only if it is enforced by something the grant does not include.

Nadella's seven principles, and what stands behind each one on this network today.

[The same argument, in our words](https://newsroom.sgit.ai/articles/the-same-argument-in-our-words.html) translates his post idea by idea into the vocabulary of behaviour policies, reach, mandate, gap, barriers and accepted risk, and finds that his ending and ours are the same sentence read from opposite ends:

>

the more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it.

## Where the platform draws the line

[Where the platform draws the line](https://newsroom.sgit.ai/articles/where-the-platform-draws-the-line.html) reads Microsoft's new execution containers and agent control specification field by field. The platform puts the policy outside the workload and enforces it in the operating system, and it can only name what it can see: files, addresses, processes. That is the shared responsibility model again, and the business logic sits above the line:

>

an agent must not be the one that decides its own limits.

The shared responsibility model, drawn for agents: each layer can only name what it can see.

Run the same agent three ways, it finds, and rows of a behaviour policy that were hope can now become boundaries kept by the platform. [Ten hard questions for RiskMandate](https://newsroom.sgit.ai/articles/riskmandate-ten-questions.html) is where that policy comes from: the questions a co-founder brought back from a conference, about bypasses, liability, insurance and what a customer is actually paying for, answered in a two-hour interview.

>

RiskMandate defines the risk that comes with the mandate a business gives an agent.

## The controls we run on our own agents

The principles are easy to state. These four articles are what keeping them looks like on a real system, every day.

[A second reader the agent cannot skip](https://newsroom.sgit.ai/articles/a-second-reader-the-agent-cannot-skip.html) starts with two emails that went out in my voice despite a written rule, and ends with a hook that makes a second model approve every draft, run by the harness rather than the agent, failing closed:

>

A rule kept by the agent it governs is hope.

[Re-anchoring](https://newsroom.sgit.ai/articles/re-anchoring-agent-behaviour-policies.html) deals with the forgetting. A long session is summarised again and again, each time replacing most of what the agent had in view, and nothing says what was kept. So the rules live in a file, printed back after every summary, with a short report every few answers to show it is still working:

>

The rules are restored, not remembered.

Every summary in the session that runs this site, read from its own transcript: each turned about 785,000 tokens into 9,000 to 19,000, and all eighteen were automatic.

[How I work with Claude](https://newsroom.sgit.ai/articles/how-i-work-with-claude.html) is the practical guide behind all of it: one session per topic, named agents with a role file, curated memory, vaults, and policy before connectors.

>

Memory is what the session reads.

And [a Mac of the agent's own](https://newsroom.sgit.ai/articles/a-mac-of-the-agents-own.html) is the next dedicated resource after a mailbox, a code-host account and a Claude account: a desktop, read against what Apple's licence allows, built clean for every run from vaults and erased at the end.

>

The vaults are the state.

## The eight articles

### The principles

Models as insider risks, answered and translated.

- [**Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan**](../../../../authority-outside-the-model.md). Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [**The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate**](../../../../the-same-argument-in-our-words.md). Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.

### The platform and the policy

What the operating system can now enforce, and the behaviour policy above it.

- [**Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it**](../../../../where-the-platform-draws-the-line.md). Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [**Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not**](../../../../riskmandate-ten-questions.md). Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.

### On our own agents

A second reader, rules that survive summaries, the daily routine, and a desktop of their own.

- [**A second reader the agent cannot skip: how two wrong emails became a gate on every draft**](../../../../a-second-reader-the-agent-cannot-skip.md). Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [**Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not**](../../../../re-anchoring-agent-behaviour-policies.md). Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [**How I work with Claude: one session per topic, agents with names, and memory you curate**](../../../../how-i-work-with-claude.md). A practical guide from a year of daily use: one Claude session per topic, named agents with a role.md, curated memory, vaults, and policy before connectors.
- [**A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies**](../../../../a-mac-of-the-agents-own.md). A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.

*This is issue 4 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [004-authority-outside-the-model.jpg](../../../../banners/004-authority-outside-the-model.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. LinkedIn drops images from a paste, so add these where they appear, in this order, with the caption under each:

1. [004-2026-10-11-authority.jpg](../../../../banners/collages/004-2026-10-11-authority.jpg) Authority outside the model in six pictures, one from each of the first six articles
2. [om-seven.webp](../../../../images/om-seven.webp) Nadella's seven principles, and what stands behind each one on this network today.
3. [pl-stack.webp](../../../../images/pl-stack.webp) The shared responsibility model, drawn for agents: each layer can only name what it can see.
4. [ra-compactions.webp](../../../../images/ra-compactions.webp) Every summary in the session that runs this site, read from its own transcript: each turned about 785,000 tokens into 9,000 to 19,000, and all eighteen were automatic.

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/004-authority-outside-the-model.html)*
