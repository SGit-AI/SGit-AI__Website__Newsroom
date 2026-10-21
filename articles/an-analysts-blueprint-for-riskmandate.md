# An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer, sgit.ai

> One of our power users, an analyst, sent us a note from the WestCap CISO Summit: what RiskMandate should borrow from the companies on the backdrop. It is a good piece of work, and I agree with most of it. Its thesis, control what AI agents do, not just what they can access, is the Agent Behaviour Policy's grant against mandate in other words. Its best question, which agent action would a CISO never permit even with valid credentials, is the argument we published this week. And its advice to start with one workflow and a handful of policies is how our first-customer programme already works. It also found something important: Drata announced AI Agent Governance in August, with plain-English policies enforced inline, and Endor Labs, Socket, Sondera, AWS and the gateway makers are all moving into the same space. Where I would change the plan is its first build item: intercepting tool calls ourselves. What we provide is wider than any one control: an understanding of each environment, a risk analysis, and the set of controls that fits it. Some environments need only a line in the prompt, some a hook, and some a gateway, monitoring and a person to approve; our job is to know which, and to generate the rules for all of them. So these companies arriving is good news: each has a centre of gravity around its own tooling, and our remit runs across them. Many open their enforcement points; we open the policy above them. Bluntly, what we need now are the customers, and the use cases, to do this with, for real.

*Source: <https://newsroom.sgit.ai/articles/an-analysts-blueprint-for-riskmandate.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer

# An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.1.0, 2 versions](versions/an-analysts-blueprint-for-riskmandate.md) · [newsroom v0.13.31](https://newsroom.sgit.ai/admin/versions.html) · riskmandatestrategyagentssecuritymarketarticle

***Abstract:** One of our power users, an analyst, sent us a note from the WestCap CISO Summit: what RiskMandate should borrow from the companies on the backdrop. It is a good piece of work, and I agree with most of it. Its thesis, control what AI agents do, not just what they can access, is the Agent Behaviour Policy's grant against mandate in other words. Its best question, which agent action would a CISO never permit even with valid credentials, is the argument we published this week. And its advice to start with one workflow and a handful of policies is how our first-customer programme already works. It also found something important: Drata announced AI Agent Governance in August, with plain-English policies enforced inline, and Endor Labs, Socket, Sondera, AWS and the gateway makers are all moving into the same space. Where I would change the plan is its first build item: intercepting tool calls ourselves. What we provide is wider than any one control: an understanding of each environment, a risk analysis, and the set of controls that fits it. Some environments need only a line in the prompt, some a hook, and some a gateway, monitoring and a person to approve; our job is to know which, and to generate the rules for all of them. So these companies arriving is good news: each has a centre of gravity around its own tooling, and our remit runs across them. Many open their enforcement points; we open the policy above them. Bluntly, what we need now are the customers, and the use cases, to do this with, for real.*

Who does what, by their own description: Drata, Endor Labs, Socket, Bedrock Data, Sondera, AWS AgentCore Policy, the agent gateways, the testers and the incident responders, against the analyst's four layers, discover, evaluate, enforce and prove; and RiskMandate as the policy each layer is configured from.

## In short

- **An analyst sent us a blueprint.** What RiskMandate should borrow from the summit's companies.
- **Most of it, I agree with.** Control what agents do, not just what they can access.
- **The vendors are already moving.** Drata, Endor Labs, Socket, Sondera, AWS, the gateways.
- **Their architecture maps onto ours.** Discover, evaluate, enforce, prove.
- **Our offer is the controls fitted to the context.** A prompt, a hook, a gateway, or all of them.
- **More players is good news.** Each has gravity around its tooling; our remit runs across them.
- **What we need now is customers.** And use cases, one workflow each.

## The note

My business partner is at the [WestCap CISO Summit](a-briefing-for-the-ciso-summit.md) in New York this week, and one of our power users, an analyst, sent us a note from it: what RiskMandate should borrow from the companies whose logos were on the backdrop. In short, it says:

- **Study seven companies.** Socket for risky tools and packages, Endor Labs for prioritising by what is reachable, Drata for continuous controls and evidence, Bedrock Data for what data agents can reach, Bishop Fox for adversarial testing, Kroll for incident investigation, and Optiv for reaching CISOs through existing budgets. Its own caveat: these are analogies, not claims that the products work alike.
- **Combine three of them.** Socket's view of capabilities, Drata's machine-testable controls and Bedrock Data's map of data exposure, so that RiskMandate governs what an agent may do, with which data, in which circumstances, and with what consequences.
- **Notice who is moving.** Drata and Endor Labs are extending into agent security, so generic discovery and skill scanning will not be defensible on their own.
- **Build a control plane** in four layers, discover, evaluate, enforce and prove, with the differentiation in evaluate: recognising a dangerous sequence of actions that are each allowed on their own.
- **Start small.** One framework, one high-risk workflow, five to ten enforceable policies.
- **Ask CISOs one question.** Which agent action would you never permit autonomously, even if the agent already had valid credentials?

## Where we agree

A lot of it lines up with what we already do and have published:

- **The thesis is the behaviour policy.** "What it can access" against "what it does" is the grant against the mandate, and the gap between them is what an [Agent Behaviour Policy](what-can-your-agent-reach.md) is written to show.
- **The CISO question is our argument.** It is the point of [the key is not the risk](the-key-is-not-the-risk.md): on the Pellbridge bank's day, seven of nine incidents were legitimate calls with legitimate credentials that the agent should not have made.
- **Starting small is how we start.** [Our first customers](our-first-customers.md) name one agent, measure its grant, write its mandate in their own words, and find the first gap.
- **The sequence of actions is the hard part.** The analyst's example, an agent that reads customer records, exports them and sends them outside, each step allowed, is exactly where a check on one call at a time falls short.

## Who is already there

The note's most useful finding is that the space is filling. From each company's own pages:

- **Drata** announced [AI Agent Governance](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents) on 4 August 2026: agent discovery, policy "authored as plain-English intent, compiled into machine-enforceable rules, and enforced inline", through an MCP proxy that "sits at the point every agent's tool call passes through", with simulation and an evidence feed. Two caveats from the same release: it is "available now in Limited Availability to qualified enterprises running agents on Anthropic", and it can surface "recommended actions for manual approval" as well as enforce them.
- **Endor Labs** offers [governance for AI coding agents](https://www.endorlabs.com/learn/agent-governance): visibility of every agent, model, MCP server and skill, and policy to stop unsafe actions.
- **Socket** has an MCP server and a Claude Code hook that blocks high-risk packages before they install, which it calls "a best-effort guardrail, not a complete defense."
- **Bedrock Data** has moved into governing the data AI agents can reach.
- **Sondera**, whose argument we answered in [commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md), checks Cedar policies before each action: "Sondera Harness evaluates Cedar policies before your agent's actions execute." It is open source, and a denied action comes back with a reason so the agent can try something else.
- **AWS AgentCore Policy** evaluates each agent request at its gateway, in Cedar, as we covered in [Cedar and the policy vault](cedar-and-the-policy-vault.md); Ping Identity and Docker have agent and MCP gateways of their own.
- **Bishop Fox and Optiv** test AI and agentic systems; **Kroll and Sygnia** respond to incidents.

The analyst read the logos from a photograph, and some I could not match to a company, so they are left out here.

## Their architecture, our pieces

Their architecture, our pieces: discover is the grant, measured; evaluate is the mandate and the delta; enforce is hooks in the agent's harness and rules compiled to Cedar for gateways; prove is a receipt per decision, a replayable day, and a holder for every gap. And the roadmap adds risk acceptance and insurance.

Laid against [our proposed roadmap](the-riskmandate-roadmap.md), the four layers are already there in some form:

- **Discover is the grant, measured.** What each agent can actually reach, from probes where the customer may run them and from vendor documentation where not. That is the roadmap's "understand" stage.
- **Evaluate is the mandate and the delta.** What the agent may do, in the customer's words, and what it can do and may not.
- **Enforce is the hooks, and the rules compiled for gateways.** This is the part that has moved: we now give customers hooks for the agent's own harness, which can block an action before it runs.
- **Prove is the receipts.** In [the Pellbridge vault](inside-the-pellbridge-agents.md), every decision has a receipt chained to the one before, and the whole day can be replayed; every gap has a holder and a decision.

And two things the four layers leave out, which our roadmap adds: risk acceptance, who carries each remaining risk and until when, and insurance, the evidence that lets someone cover the agent.

## The controls fitted to the context

The controls fitted to the context: a line in the prompt where little is at stake; a hook in the harness where the agent acts alone; a gateway or proxy where it reaches systems that matter; monitoring and a person where money, customers or regulators are involved. The same behaviour policy feeds all four.

This is the part of our positioning I most want to be clear about, because it is what makes it different from any single product on that backdrop. What we provide is a map of the whole situation: a good understanding of each environment, a risk analysis of each agent in it, and the set of security controls that fits that context.

That matters because the right control depends on what is at stake. There are environments where all you need is a line in the prompt: nothing goes outward, and a person reads every output. There are environments where a hook in the agent's harness is the right answer: the agent acts on its own, but the rule has to hold every time. And there are environments where you need a gateway or a proxy, monitoring, an evidence trail and a person to approve the irreversible actions, because money, customers or regulators are involved. Most of the companies above sell one of those answers. We help a customer work out which one each agent needs, and the behaviour policy says so row by row, so a rule can move from the prompt to a hook to a gateway as the stakes rise.

## Not another box in the middle

Here is where I would change the plan. Its first build item is intercepting agents' tool calls ourselves. I think that is the wrong first bet for us, for three reasons.

First, it puts us in line. As we argued in [the key is not the risk](the-key-is-not-the-risk.md), a proxy in the middle is a single point of failure, and it usually lacks the context to judge a request that looks valid; the state lives in the application. Second, the space is full: Drata, Sondera, AWS and the gateway makers all intercept tool calls already, and the customers we want already run some of them. Third, it is not what we are best at. As abp.sgit.ai puts it, a behaviour policy is "not a guardrail. It is what guardrails are compiled from."

But that does not mean we only describe. We have started to play in block and prevent, in two ways that do not put a new box in the customer's path:

- **Hooks in the agent's own harness.** They see each tool call before it runs and can block it. They can also keep state across a session, so the analyst's sequence, read, export, send, can be one rule. Honestly labelled, a hook the agent's account can change is a setting, not a boundary, and the policy says so.
- **The same rules, compiled for the enforcement points customers already run.** We have already compiled our rules to Cedar and tested them, the language Sondera and AWS evaluate. Kept by a gateway outside the agent's reach, the same rule becomes a boundary.

And we map the environment first, so the customer knows which of their agents needs which, and why.

## Where to start

Where to start: the analyst's first build list, and our order. Tool-call interception through the hooks and the customer's own gateways; behavioural policies, which we have; cross-step detection in hooks that keep state; allow, block and approve generated from the policy; audit and replay, which we have; and partners for skill and MCP risk scoring.

So the list becomes: use the hooks and the gateways customers already have; keep building the policy, which is the part nobody else does openly; make the hooks hold the sequences; and partner for the rest, Socket and Endor Labs on skills and dependencies, exactly as the analyst suggests. The analyst's own conclusion is that RiskMandate's best opportunity is to be the layer those platforms integrate with. I agree, with one change of words: the policy layer, not another runtime layer.

## More players is good news

I do not see these companies moving into our space as a bad thing. I see it as a good one. It means the problem is real, and that budgets are forming around it. And each of these companies has a centre of gravity around its own tooling: Drata around its trust platform, Socket around packages, a gateway around its gateway. That is natural, and it is also the limit. Our remit is wider: the whole set of agents, environments and controls, across whichever of these tools a customer runs. Even the simplest version of what we do, connecting a lot of those tools to one policy, is valuable on its own.

## Who plays open source

Who plays open source, and what they open: agentgateway, Docker's MCP gateway and Sondera's harness are open; AWS opens its Cedar language, Socket and Endor Labs their agent tooling; no public code was found for Drata's, Bedrock Data's or Ping's agent products. RiskMandate opens the vocabulary, the policies, the engine and the apps.

We play open source, and that is a design choice: everything we make is meant to be used by the customer, in their own hands. So it is worth asking how many of these companies do the same. From their public repositories and documentation:

- **The enforcement points are often open.** [agentgateway](https://agentgateway.dev/docs/) is a Linux Foundation project under Apache 2.0; Docker's MCP gateway and Sondera's harness are MIT; AWS's policy language, Cedar, is Apache 2.0, though AgentCore Policy itself is a service.
- **The tooling around a service is partly open.** Socket's MCP server and command line, and Endor Labs' agent kit, are MIT, and both need their companies' services behind them.
- **The governance platforms mostly are not.** We found no public code for the agent products of Drata, Bedrock Data or Ping, nor agent-governance code from the testers and responders.

So the honest picture is not that we are the only ones who are open. It is that what we open is a different layer: the policy above the enforcement points, the analysis that decides which control fits, and the vocabulary to say it, under CC BY 4.0, with the code under Apache 2.0. That is exactly the layer the open gateways need something to feed them, and the closed platforms could adopt without giving anything up.

## The more mature, the less we are needed?

We have talked about this before. The more mature a company is, in a way, the less of what we do it might need: it already has its gateways, its monitoring and its governance. That is true, and there is still a lot of value to add: the risk analysis across all of it, the gaps between the tools, the rows nobody holds, and the evidence that ties it together for a board or an insurer. And for the many companies that are not mature yet, we are the place to start.

The platform we now have is very mouldable: policies, hooks, vaults, compiled rules, replayable evidence. What it needs is lots of use cases.

## What we need now

Bluntly, what we need now are the customers, to do this for real. We have a plan that should work, and the pieces exist. What is missing is three to five teams, each with one real workflow and one agent, who will let us map it, write its policy, put the hooks in, and see what happens.

The analyst's closing question is the best way to find them: which agent action would you never permit autonomously, even with valid credentials? Every answer is the first row of a mandate. If you have one, the [customer programme](https://customers.riskmandate.ai/) starts with it, and if you want to help in other ways, [how to help](how-to-help.md) has six steps.

## What this does not claim

- **The note is the analyst's.** Paraphrased, not quoted; the reading of it is mine.
- **The vendors' capabilities are their own claims.** Read from their pages on 21 October 2026, not tested.
- **Our dots are rings.** In the figure, RiskMandate supplies the policy for each layer, not a product in it.
- **The hooks are settings.** Kept by the agent's own harness; a boundary needs something outside it.
- **Our evidence trail is a demo.** The Pellbridge bank is invented.
- **The open-source check is of public code.** Repositories and documentation we could read; some may hold more.

## Where this comes from

An analyst's note to us from the WestCap CISO Summit, 21 October 2026, paraphrased. Drata's [announcement of 4 August 2026](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents); Endor Labs' [agent governance](https://www.endorlabs.com/learn/agent-governance); Socket's MCP server and hook documentation; Bedrock Data's announcement of March 2026; [Sondera's documentation](https://docs.sondera.ai); and the pages of AWS, Ping Identity, Docker, Bishop Fox, Optiv, Kroll and Sygnia, and the public repositories of agentgateway, Docker, Sondera, Cedar, Socket and Endor Labs, all read the same day. Related: [a briefing for the WestCap CISO Summit](a-briefing-for-the-ciso-summit.md), [the RiskMandate roadmap](the-riskmandate-roadmap.md), [the key is not the risk](the-key-is-not-the-risk.md), [commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md), [Cedar and the policy vault](cedar-and-the-policy-vault.md), [our first customers](our-first-customers.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#an-analysts-blueprint-for-riskmandate)

### Builds on

- [A briefing for the WestCap CISO Summit: what RiskMandate and Agent Behaviour Policies are, said for each kind of person in the room, where we add value, and what to read next](a-briefing-for-the-ciso-summit.md) A briefing for the WestCap CISO Summit: Agent Behaviour Policies and RiskMandate, said for six kinds of person in the room, with what to read next.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [The key is not the risk: credential injection for AI agents is a good pattern, and the first question is still what an attacker can do with the agent](the-key-is-not-the-risk.md) Credential injection for AI agents is a good pattern; the first question is still what an attacker can make the agent do.
- [Our first customers: an early access programme for Agent Behaviour Policies, with credit to spend, a start-here site, daily follow-up, and a list for the next batch](our-first-customers.md) Agent Behaviour Policies move to execution: a first batch of customers with credit, a start-here site, daily follow-up, and a list for the next batch.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and a brief for the MVP](cedar-and-the-policy-vault.md) Cedar is mature and adopted; it lacks the why, the version in force and the evidence. A vault carries all three, and the demo shows it working.
- [A proposed roadmap for RiskMandate: policies, understand, risk acceptance, contain, manage and insure, a spectrum of trust we would walk with each customer](the-riskmandate-roadmap.md) A proposed strategy for RiskMandate, a spectrum of trust: policies, understand, risk acceptance, contain, manage, insure.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [How to help: six steps for anyone who wants to be involved with sgit, Risk Mandate or this newsroom, and what they get back](how-to-help.md) Six steps for anyone who wants to help or be involved with sgit, Risk Mandate or this newsroom, and what they get back.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 251 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=251)

**Posting this article on LinkedIn?** The cover is [an-analysts-blueprint-for-riskmandate.jpg](banners/an-analysts-blueprint-for-riskmandate.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-analysts-blueprint-for-riskmandate.html)*
