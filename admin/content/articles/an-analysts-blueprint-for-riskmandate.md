---
title: An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: One of our power users, an analyst, sent us a note from the WestCap CISO Summit: what RiskMandate should borrow from the companies on the backdrop. It is a good piece of work, and I agree with most of it. Its thesis, control what AI agents do, not just what they can access, is the Agent Behaviour Policy's grant against mandate in other words. Its best question, which agent action would a CISO never permit even with valid credentials, is the argument we published this week. And its advice to start with one workflow and a handful of policies is how our first-customer programme already works. It also found something important: Drata announced AI Agent Governance in August, with plain-English policies enforced inline, and Endor Labs, Socket, Sondera, AWS and the gateway makers are all moving into the same space. Where I would change the plan is its first build item: intercepting tool calls ourselves. We would rather be the policy every one of those enforcement points is configured from, use the hooks in the agent's own harness to block and prevent, and compile the same rules for the gateways customers already run. We are compatible with all of them, and that is the point. Bluntly, what we need now are the customers to do this with, for real.
version: v0.13.31
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, strategy, agents, security, market, article
status: published
---

!shot wb-landscape.webp | images/ | Who does what, by their own description: Drata, Endor Labs, Socket, Bedrock Data, Sondera, AWS AgentCore Policy, the agent gateways, the testers and the incident responders, against the analyst's four layers, discover, evaluate, enforce and prove; and RiskMandate as the policy each layer is configured from. | comparison

## In short {#in-short}

- **An analyst sent us a blueprint.** What RiskMandate should borrow from the summit's companies.
- **Most of it, I agree with.** Control what agents do, not just what they can access.
- **The vendors are already moving.** Drata, Endor Labs, Socket, Sondera, AWS, the gateways.
- **Their architecture maps onto ours.** Discover, evaluate, enforce, prove.
- **Where I would change the plan:** do not build another box in the middle.
- **Be the policy they are all configured from.** Hooks to block; rules compiled for gateways.
- **What we need now is customers.** One workflow each, for real.

## The note {#note}

My business partner is at the [WestCap CISO Summit](/articles/a-briefing-for-the-ciso-summit.html) in New York this week, and one of our power users, an analyst, sent us a note from it: what RiskMandate should borrow from the companies whose logos were on the backdrop. In short, it says:

- **Study seven companies.** Socket for risky tools and packages, Endor Labs for prioritising by what is reachable, Drata for continuous controls and evidence, Bedrock Data for what data agents can reach, Bishop Fox for adversarial testing, Kroll for incident investigation, and Optiv for reaching CISOs through existing budgets. Its own caveat: these are analogies, not claims that the products work alike.
- **Combine three of them.** Socket's view of capabilities, Drata's machine-testable controls and Bedrock Data's map of data exposure, so that RiskMandate governs what an agent may do, with which data, in which circumstances, and with what consequences.
- **Notice who is moving.** Drata and Endor Labs are extending into agent security, so generic discovery and skill scanning will not be defensible on their own.
- **Build a control plane** in four layers, discover, evaluate, enforce and prove, with the differentiation in evaluate: recognising a dangerous sequence of actions that are each allowed on their own.
- **Start small.** One framework, one high-risk workflow, five to ten enforceable policies.
- **Ask CISOs one question.** Which agent action would you never permit autonomously, even if the agent already had valid credentials?

## Where we agree {#agree}

A lot of it lines up with what we already do and have published:

- **The thesis is the behaviour policy.** "What it can access" against "what it does" is the grant against the mandate, and the gap between them is what an [Agent Behaviour Policy](/articles/what-can-your-agent-reach.html) is written to show.
- **The CISO question is our argument.** It is the point of [the key is not the risk](/articles/the-key-is-not-the-risk.html): on the Pellbridge bank's day, seven of nine incidents were legitimate calls with legitimate credentials that the agent should not have made.
- **Starting small is how we start.** [Our first customers](/articles/our-first-customers.html) name one agent, measure its grant, write its mandate in their own words, and find the first gap.
- **The sequence of actions is the hard part.** The analyst's example, an agent that reads customer records, exports them and sends them outside, each step allowed, is exactly where a check on one call at a time falls short.

## Who is already there {#landscape}

The note's most useful finding is that the space is filling. From each company's own pages:

- **Drata** announced [AI Agent Governance](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents) on 4 August 2026: agent discovery, policy "authored as plain-English intent, compiled into machine-enforceable rules, and enforced inline", through an MCP proxy that "sits at the point every agent's tool call passes through", with simulation and an evidence feed. Two caveats from the same release: it is "available now in Limited Availability to qualified enterprises running agents on Anthropic", and it can surface "recommended actions for manual approval" as well as enforce them.
- **Endor Labs** offers [governance for AI coding agents](https://www.endorlabs.com/learn/agent-governance): visibility of every agent, model, MCP server and skill, and policy to stop unsafe actions.
- **Socket** has an MCP server and a Claude Code hook that blocks high-risk packages before they install, which it calls "a best-effort guardrail, not a complete defense."
- **Bedrock Data** has moved into governing the data AI agents can reach.
- **Sondera**, whose argument we answered in [commander's intent is a behaviour policy](/articles/commanders-intent-is-a-behaviour-policy.html), checks Cedar policies before each action: "Sondera Harness evaluates Cedar policies before your agent's actions execute." It is open source, and a denied action comes back with a reason so the agent can try something else.
- **AWS AgentCore Policy** evaluates each agent request at its gateway, in Cedar, as we covered in [Cedar and the policy vault](/articles/cedar-and-the-policy-vault.html); Ping Identity and Docker have agent and MCP gateways of their own.
- **Bishop Fox and Optiv** test AI and agentic systems; **Kroll and Sygnia** respond to incidents.

The analyst read the logos from a photograph, and some I could not match to a company, so they are left out here.

## Their architecture, our pieces {#map}

!shot wb-map.webp | images/ | Their architecture, our pieces: discover is the grant, measured; evaluate is the mandate and the delta; enforce is hooks in the agent's harness and rules compiled to Cedar for gateways; prove is a receipt per decision, a replayable day, and a holder for every gap. And the roadmap adds risk acceptance and insurance. | comparison

Laid against [our proposed roadmap](/articles/the-riskmandate-roadmap.html), the four layers are already there in some form:

- **Discover is the grant, measured.** What each agent can actually reach, from probes where the customer may run them and from vendor documentation where not. That is the roadmap's "understand" stage.
- **Evaluate is the mandate and the delta.** What the agent may do, in the customer's words, and what it can do and may not.
- **Enforce is the hooks, and the rules compiled for gateways.** This is the part that has moved: we now give customers hooks for the agent's own harness, which can block an action before it runs.
- **Prove is the receipts.** In [the Pellbridge vault](/articles/inside-the-pellbridge-agents.html), every decision has a receipt chained to the one before, and the whole day can be replayed; every gap has a holder and a decision.

And two things the four layers leave out, which our roadmap adds: risk acceptance, who carries each remaining risk and until when, and insurance, the evidence that lets someone cover the agent.

## Not another box in the middle {#inline}

Here is where I would change the plan. Its first build item is intercepting agents' tool calls ourselves. I think that is the wrong first bet for us, for three reasons.

First, it puts us in line. As we argued in [the key is not the risk](/articles/the-key-is-not-the-risk.html), a proxy in the middle is a single point of failure, and it usually lacks the context to judge a request that looks valid; the state lives in the application. Second, the space is full: Drata, Sondera, AWS and the gateway makers all intercept tool calls already, and the customers we want already run some of them. Third, it is not what we are best at. As abp.sgit.ai puts it, a behaviour policy is "not a guardrail. It is what guardrails are compiled from."

But that does not mean we only describe. We have started to play in block and prevent, in two ways that do not put a new box in the customer's path:

- **Hooks in the agent's own harness.** They see each tool call before it runs and can block it. They can also keep state across a session, so the analyst's sequence, read, export, send, can be one rule. Honestly labelled, a hook the agent's account can change is a setting, not a boundary, and the policy says so.
- **The same rules, compiled for the enforcement points customers already run.** We have already compiled our rules to Cedar and tested them, the language Sondera and AWS evaluate. Kept by a gateway outside the agent's reach, the same rule becomes a boundary.

And we map the environment first, so the customer knows which of their agents needs which, and why.

## Where to start {#start}

!shot wb-start.webp | images/ | Where to start: the analyst's first build list, and our order. Tool-call interception through the hooks and the customer's own gateways; behavioural policies, which we have; cross-step detection in hooks that keep state; allow, block and approve generated from the policy; audit and replay, which we have; and partners for skill and MCP risk scoring. | comparison

So the list becomes: use the hooks and the gateways customers already have; keep building the policy, which is the part nobody else does openly; make the hooks hold the sequences; and partner for the rest, Socket and Endor Labs on skills and dependencies, exactly as the analyst suggests. The analyst's own conclusion is that RiskMandate's best opportunity is to be the layer those platforms integrate with. I agree, with one change of words: the policy layer, not another runtime layer.

## Compatible with all of them {#compatible}

That is why I think we are in a good position. An Agent Behaviour Policy is open, CC BY 4.0, with code under Apache 2.0, and it is written so any of these products can use it: Drata's plain-English policies, Sondera's and AWS's Cedar, a gateway's rules, a red team's test plan, an incident responder's starting point. A customer who wants to go in the direction the analyst describes can do it with us, whichever of these they already run.

## What we need now {#customers}

Bluntly, what we need now are the customers, to do this for real. We have a plan that should work, and the pieces exist. What is missing is three to five teams, each with one real workflow and one agent, who will let us map it, write its policy, put the hooks in, and see what happens.

The analyst's closing question is the best way to find them: which agent action would you never permit autonomously, even with valid credentials? Every answer is the first row of a mandate. If you have one, the [customer programme](https://customers.riskmandate.ai/) starts with it, and if you want to help in other ways, [how to help](/articles/how-to-help.html) has six steps.

## What this does not claim {#limits}

- **The note is the analyst's.** Paraphrased, not quoted; the reading of it is mine.
- **The vendors' capabilities are their own claims.** Read from their pages on 21 October 2026, not tested.
- **Our dots are rings.** In the figure, RiskMandate supplies the policy for each layer, not a product in it.
- **The hooks are settings.** Kept by the agent's own harness; a boundary needs something outside it.
- **Our evidence trail is a demo.** The Pellbridge bank is invented.

## Where this comes from {#sources}

An analyst's note to us from the WestCap CISO Summit, 21 October 2026, paraphrased. Drata's [announcement of 4 August 2026](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents); Endor Labs' [agent governance](https://www.endorlabs.com/learn/agent-governance); Socket's MCP server and hook documentation; Bedrock Data's announcement of March 2026; [Sondera's documentation](https://docs.sondera.ai); and the pages of AWS, Ping Identity, Docker, Bishop Fox, Optiv, Kroll and Sygnia, all read the same day. Related: [a briefing for the WestCap CISO Summit](/articles/a-briefing-for-the-ciso-summit.html), [the RiskMandate roadmap](/articles/the-riskmandate-roadmap.html), [the key is not the risk](/articles/the-key-is-not-the-risk.html), [commander's intent is a behaviour policy](/articles/commanders-intent-is-a-behaviour-policy.html), [Cedar and the policy vault](/articles/cedar-and-the-policy-vault.html), [our first customers](/articles/our-first-customers.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
