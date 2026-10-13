# Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it, sgit.ai

> On 7 October Microsoft made Microsoft Execution Containers (MXC) generally available: a containment layer for AI agents, declared in JSON and enforced by the operating system. With its companion, the Agent Control Specification (ACS), it is the most complete platform control for agents I have seen, and it confirms the direction of travel: the policy sits outside the agent, the agent cannot grant itself more, and you observe before you enforce. This article is a briefing on how the two actually work, field by field, and a map from them to RiskMandate's Agent Behaviour Policy. My argument is the shared responsibility model, applied to agents. Every platform draws its line where it can see and touch: files, network addresses and ports, the desktop, and with ACS the arguments of a tool call. Above that line is what a business actually runs on: what a Gmail label means, whose voice an email goes out in, how many refunds in a day is normal, which customer this run is for. Eight scenarios, each run three ways (a plain agent, an agent with a behaviour policy, and an agent with a behaviour policy on top of MXC and ACS), show what the platform turns into boundaries, what it hands back to the business, and what only a named person can accept. The platform is an important stage of the climb, not the summit.

*Source: <https://newsroom.sgit.ai/articles/where-the-platform-draws-the-line.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it

# Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/where-the-platform-draws-the-line.md) · [sgit.ai v0.7.42](https://sgit.ai/admin/versions.md) · riskmandateagent-behaviour-policymicrosoftmxcexecution-containersagent-control-specificationcontainmentshared-responsibilitybusiness-logicbarriersbriefingarticle

***Abstract:** On 7 October Microsoft made Microsoft Execution Containers (MXC) generally available: a containment layer for AI agents, declared in JSON and enforced by the operating system. With its companion, the Agent Control Specification (ACS), it is the most complete platform control for agents I have seen, and it confirms the direction of travel: the policy sits outside the agent, the agent cannot grant itself more, and you observe before you enforce. This article is a briefing on how the two actually work, field by field, and a map from them to RiskMandate's Agent Behaviour Policy. My argument is the shared responsibility model, applied to agents. Every platform draws its line where it can see and touch: files, network addresses and ports, the desktop, and with ACS the arguments of a tool call. Above that line is what a business actually runs on: what a Gmail label means, whose voice an email goes out in, how many refunds in a day is normal, which customer this run is for. Eight scenarios, each run three ways (a plain agent, an agent with a behaviour policy, and an agent with a behaviour policy on top of MXC and ACS), show what the platform turns into boundaries, what it hands back to the business, and what only a named person can accept. The platform is an important stage of the climb, not the summit.*

The shared responsibility model, drawn for agents. Each layer can only name what it can see. MXC names files, network addresses and the desktop; ACS names tool calls and their arguments; the business logic and the authority above them are the deployer's, and that is where the Agent Behaviour Policy works.

On 7 October Microsoft announced that [Microsoft Execution Containers are generally available](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/). I read it the day after Satya Nadella's post on models as insider risks, which I answered in [The same argument, in our words](the-same-argument-in-our-words.md) and [Authority outside the model](authority-outside-the-model.md), and I recorded a voice memo straight away, because the question it raises for RiskMandate is obvious: if the platform now does containment, what is left for us to do?

My answer is that this is the shared responsibility model again, and that it is good news. But a voice memo is a first reaction, so this article does two jobs. First, it is a briefing: what Microsoft has actually shipped and how it works, built from the announcement, the [MXC repository](https://github.com/microsoft/mxc) and its schema, and the [Agent Control Specification announcement](https://commandline.microsoft.com/agent-control-specification-runtime-governance/). Where my memo guessed and the documents disagreed, the documents win, and I say so. Second, it is the practical companion to the two Nadella articles: where the platform's line sits, what lies above it, and where RiskMandate fits.

## In short

- **The direction of travel is right, and now it is shipping.** Microsoft's own announcement states the principle this site has built on: an agent must not be the one that decides its own limits. MXC puts the policy outside the workload, enforces it in the operating system, denies by default, and lets you watch an agent in a permissive mode before you enforce. That is the enforcer test, footprint and "instrument before you enforce", built into a platform.
- **MXC is a JSON policy, a set of SDKs and several sandboxes.** A versioned request names the container, the command, the paths the workload may read, write or never touch, the network egress and ingress, and the desktop. The SDKs (Rust, .NET, Node) and the process container run on Windows, macOS and Linux; the session container, learning-mode reports and Intune management are Windows only. It is open source, under the MIT licence. It is Microsoft's schema, not an industry standard.
- **ACS is the layer above it, and it climbs toward ours.** The Agent Control Specification is a portable manifest that evaluates a policy, usually Rego, at eight points in the agent loop, including before every tool call, with the session's context passed in. Its worked example is an email rule. It supplies the hooks, the inputs and the enforcement contract. It deliberately does not supply the rules.
- **This is the shared responsibility model again.** Cloud providers drew their line where they had control: security *of* the cloud is theirs, security *in* the cloud is yours. Platforms for agents do the same, and not out of bad faith: they draw the line at the granularity they can touch. MXC's unit is a path, a numeric address and port, the desktop. ACS's unit is a tool call. What a label in a mailbox means to the business, whose voice a message carries, and how many of an action is normal in a day sit above both.
- **Run the same agent three ways and the layers separate cleanly.** In eight scenarios, a plain agent has an open path in all eight. A behaviour policy names all eight and makes none of them a boundary on its own. Put the same policy on top of MXC and ACS, and three become operating-system boundaries, four become boundaries if the business writes the rule into ACS or the tool, and one stays where only a named person can accept it.
- **This is the move we wanted.** RiskMandate has always said it is not inline, and that the customer's own stack enforces. MXC and ACS are a large part of that stack arriving at once. Rows of a behaviour policy that were hope, kept by the agent, can now become boundaries, kept by the platform. The policy is what says which rows, and what to write into them.

## What Microsoft shipped: a briefing

### The problem it states

Microsoft's announcement frames the choice customers feel they have: give agents unrestricted access and hope, or block them and lose the productivity. Its answer is three platform capabilities: containment (what an agent can access and do), identity (telling an agent's activity apart from a person's) and manageability (letting organisations govern and monitor agents). MXC is the containment layer, and it is generally available now. The other two are announced as coming: Microsoft Entra telling agent activity apart from user activity, and Agent 365 controls extending to local agents.

The sentence that matters most is the one this whole site agrees with: **"An agent cannot be its own security authority."** And its example is the right one. A coding agent asked to update a website needs to read and write the repository, and may need to read the production server's configuration, but should not be able to change it. Without a boundary, the agent might decide that changing the server configuration is the fastest way to finish. That would be reasonable from the agent's point of view, and still beyond what its developer meant to grant. In RiskMandate's terms, that is a row of the gap, and the announcement's answer is to make it a boundary.

### What MXC is, mechanically

MXC is an SDK that an agent, or the application that hosts it, builds in. The application hands MXC a request naming the container type, the containment rules and the command to run. MXC validates it, picks a backend, and launches the workload inside a container that enforces the rules. The policy is held outside the workload, so the agent, or code it generated, cannot grant itself more.

The request is JSON, validated against a versioned schema: the stable schema is 1.0.0, and a 1.1.0 preview version carries experimental features. Here is what a policy for Microsoft's own website example could look like. The field names are the schema's; the paths and the command are ours, for illustration:

```

{
  "version": "1.0.0",
  "containerId": "website-update",
  "containment": "processcontainer",
  "process": {
    "commandLine": "agent-run --task update-homepage",
    "cwd": "C:/src/website",
    "timeout": 600000
  },
  "filesystem": {
    "readwritePaths": ["C:/src/website"],
    "readonlyPaths":  ["C:/deploy/server-config", "C:/tools/git"],
    "deniedPaths":    ["C:/Users/me/Documents", "C:/Users/me/.ssh"]
  },
  "network": {
    "egress":  { "default": "deny" },
    "ingress": { "default": "deny", "hostLoopback": "deny" }
  },
  "ui": { "disable": true },
  "processContainer": { "leastPrivilege": true }
}

```

This example validates against the stable 1.0.0 schema in the repository, and it is published with this article as [JSON](data/where-the-platform-draws-the-line__mxc-website-policy.json). Read it as five policy areas, which is how Microsoft's announcement presents them:

| Policy area | What it controls | What it can name |
|---|---|---|
| **Containment** | Which sandbox the workload runs in | `processcontainer`, a session container, WSL, a microVM |
| **Process** | The command, working directory, environment, timeout | One command line and its settings |
| **File system** | Paths the workload may change, read, or never touch | Paths |
| **Network** | Outbound and inbound connectivity, host loopback | Allow or deny by default; numeric address ranges, protocols and ports; or a proxy |
| **User interface** | Desktop, clipboard, input | On or off, read or not |

Two details from the repository matter for what follows. Containers are **deny by default**: when the network section is left out, outbound traffic is denied. And the network rules are **numeric**: an address range, a protocol and a port. Filtering by host name, or by anything above that, is left to a proxy the caller runs. MXC itself does not see what the traffic says.

That last detail is very familiar. The day before writing this, we ran [five synthetic users](how-to-run-synthetic-users.md) through newsroom.sgit.ai, and to keep them from touching anything real we wrote exactly that proxy, at the request level: every request to the site was answered from a verified local copy, and every request that was not a read, or that went to any other host, was refused and logged. MXC would have given us the sandbox around it. The rule that mattered, "read this one site, change nothing", was ours to write.

### Four sandboxes, one schema

The same request maps to the right sandbox on each platform:

| Backend | Where | What it is |
|---|---|---|
| **Process container** | Windows 11, macOS, Linux | The platform's own process sandbox: AppContainer on Windows, Seatbelt on macOS, Bubblewrap on Linux |
| **Session container** | Windows 11 only | A separate Windows account and session: its own desktop, clipboard, input and identity |
| **WSL container** | Windows 11 only | A Linux environment through the Windows Subsystem for Linux |
| **MicroVM** | Windows 11 and Linux, experimental | A hardware-backed virtual machine boundary |

So my memo's guess, that this is a Windows thing and not a standard, was half right. The schema, the SDKs and the lightest sandbox are cross-platform, and the code is MIT-licensed on GitHub. But the parts that make it manageable across an organisation, the session container, the learning-mode reports and the coming Intune policy, are Windows only, and the schema is Microsoft's own rather than a standards body's.

### Observe, then enforce

The feature closest to our own method is the three operating modes:

| Mode | Ungranted access | Recorded | Use |
|---|---|---|---|
| **Enforcement** | Blocked | No | Production |
| **Learning** | Blocked and recorded | Yes, as a JSON activity report | Find what the policy is missing without loosening it |
| **Permissive** | Allowed and recorded | Yes | Watch everything the agent would touch if nothing were blocked |

Permissive mode answers, on the machine, the question an Agent Behaviour Policy's reach answers on paper: what would this agent touch if nothing stopped it? Learning mode is calibration against reality. The repository is candid that permissive mode weakens containment, and flags it as security-sensitive whenever it is used. Activity reports are Windows only.

### Developer policy, organisation policy, agent identity

An agent developer declares what the workload needs. The organisation can then narrow it through management policy, with Intune support announced as coming for process containers on Windows 11, so the same agent runs inside different enterprise boundaries without the developer encoding each company's posture. Microsoft asks agent developers to expect the organisation to be stricter, and to explain a blocked task rather than fail silently. Agent identity through Entra is announced as coming, so that a misbehaving agent's access can be cut without cutting the employee's. GitHub Copilot, OpenAI Codex, Replit and others support MXC now; Anthropic's Claude Code is listed among those releasing support.

### The layer above: the Agent Control Specification

MXC answers what a workload can reach on the machine. It cannot answer whether a particular email should be sent, because to MXC an email is an encrypted connection to an allowed address on port 443. Microsoft's answer for that is a separate project, published in June: the [Agent Control Specification](https://commandline.microsoft.com/agent-control-specification-runtime-governance/) (ACS), an MIT-licensed specification and SDK in Microsoft's Agent Governance Toolkit, pitched as an open, vendor-neutral standard.

ACS's own explanation of why it exists is the clearest statement of the problem I have seen from a vendor. Traditional access control can say whether a credential may call a resource; it has no way to ask, in its words, **"given everything this agent has touched in this conversation, is this call still safe?"** ACS defines eight interception points in the agent loop: startup, input, before and after each model call, before and after each tool call, output, and shutdown. At each one, the host passes a snapshot of the session (the actor, prior tool calls, data sensitivity, approval state); ACS shapes it into a standard input, gathers evidence from classifiers or other services, runs a policy engine (usually Rego), and returns allow, warn, deny or escalate, failing closed if anything breaks. A manifest file binds policies to points and ships with the agent, and adapters exist for most agent frameworks. Its worked example is an email agent whose policy denies sending to external recipients.

That is a real step up the stack. It is the same layer as the [second reader](a-second-reader-the-agent-cannot-skip.md) on our own drafts: a check on the tool call, outside the model, failing closed. And it has the same property we found there: whether it is a boundary depends on who owns the installation. ACS is enforced by the host that runs the agent loop. If the agent can edit the manifest, or the host, it is a setting. Same code, different owner.

ACS is also explicit about what it is not. It owns where, when and how a policy is evaluated. The rules themselves, it says, come from whoever authors them. Which is exactly where this article is going.

## The shared responsibility model, applied to agents

Every security professional knows this move. Cloud providers drew a line: security *of* the cloud (the hardware, the hypervisor, the network) is theirs; security *in* the cloud (your configuration, your identities, your data) is yours. AWS put it on [a page](https://aws.amazon.com/compliance/shared-responsibility-model/) that everyone in this industry has seen. It was a good model. It was also, inevitably, a line drawn exactly where the provider's control ended. A company draws its responsibility around what it can touch. That is not bad faith. It is the only line it can honestly draw.

Platforms for agents are drawing the same line, at the granularity they can touch. MXC's unit is a path, a numeric address and port, a desktop. ACS's unit is a tool call and its arguments. RiskMandate's [Lab 01](https://riskmandate.ai/lab-connector-grants.html) found the same shape in the connectors themselves: the narrowest Gmail scope that reads one message reads every message, and no scope filters by sender, label or date. The unit of restriction is the application and the tool. It is not the data, and it is not the business.

The problem is that a business does not run at that granularity. In [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md), I described what happens a few layers into any real policy: you stop writing about files and ports, and start writing about how this company does email, which steps an invoice goes through, who a client is this week. For decades those rules lived in software, enforced by the screen that did not show the button. Software was the law. An agent calls the API the button would have called, and the rule is gone, unless somebody writes it down and something enforces it. Three examples from our own work show the gap.

**A label is a decision.** To a platform, applying or removing a Gmail label is one call that changes one property of one message. To a business, labels are the filing system: in Gmail a label is a folder, and filters, workflows, retention and delegation hang off them. Remove an invoices-to-pay label from forty messages, for example, and they leave somebody's queue, and the bills go unpaid. The [connector twin](connector-twin-before-you-deploy-an-agent.md) can put every one of those labels back exactly; it cannot put back the missed payments. MXC sees an allowed connection to Google. ACS can see the call and its arguments, but nothing in it knows which label means what. That is business knowledge, and only the business has it.

**Sending depends on who, from whom, and in whose voice.** ACS's own example denies email to external recipients, which is a good rule, and a real boundary if the host enforces it. But the failure we actually had was different. [Two emails went out](a-second-reader-the-agent-cannot-skip.md) to a legitimate external contact, in my voice and signed with my name. An external-recipient rule would not have stopped them. The rule that mattered was ours: agents draft, a person sends. Who may be written to, on whose behalf, about what, and whether a model may speak as a person are business rules.

**Quantity is context.** One database call is fine; fifty in a minute is something else. One refund is service; a hundred is a loss. MXC cannot count. ACS can, if the host passes the history in its snapshot. But what number is normal for this agent, this customer, this day, is not something a platform can know. In [Hope or enforcement](hope-or-enforcement.md), the limits that made the difference were the business's: 100 GBP per order, a 2,000 GBP daily circuit breaker on all automatic refunds, and, proposed after the run, 250 GBP per customer in 30 days.

## One agent, three ways: eight scenarios

To make the layers concrete, take eight things an agent might do, four from a coding agent like Microsoft's example and four from agents on a mailbox and a shop's support inbox, and run each through three designs:

- **A plain agent**, running as the signed-in user, with a long and careful prompt.
- **The same agent with an Agent Behaviour Policy**: reach measured, mandate written, every row of the gap named with its barrier. On its own, a policy turns nothing into a boundary. It turns unknowns into named rows, and most rows into honest expectations.
- **The same policy on top of MXC and ACS**, with each row placed at the lowest layer that can enforce it.
Eight scenarios, three designs. The plain agent leaves every path open. The behaviour policy names every row but bounds none on its own. On top of MXC and ACS, three rows become operating-system boundaries, four become boundaries once the business's rule is written into ACS or the tool, and one stays inside the mandate, where only a named person can accept it.

| # | Scenario | Plain agent | With an ABP | ABP on top of MXC and ACS |
|---|---|---|---|---|
| 1 | Coding agent rewrites the production server config to finish faster | Open: runs as the user | Named row; barrier is an expectation | **Boundary, OS:** config path read-only |
| 2 | Coding agent reads the user's SSH keys or Documents | Open | Named row; expectation | **Boundary, OS:** denied paths |
| 3 | Generated code posts the repository to an unknown host | Open | Named row; expectation | **Boundary, OS:** egress denied by default |
| 4 | Coding agent force-pushes to main on the allowed code host | Open | Mandate says one branch; expectation | MXC cannot tell (same address, same port). **Boundary if** the rule is written into ACS or the code host's branch protection |
| 5 | Mailbox agent removes a payables label from forty messages | Open | Mandate lists the labels it may change; expectation | MXC sees an allowed connection. **Boundary if** ACS or the tool encodes which labels are protected; the twin can restore the labels, not the late payments |
| 6 | Agent sends a reply in a person's voice to a real external contact | Open | Mandate says draft, never send; expectation | An external-recipient rule does not catch it. **Boundary if** there is no send tool, or a second reader gates the draft at the harness |
| 7 | Support agent issues fifty refunds in an afternoon | Open, no limit | Limits written down; expectation | MXC cannot count. **Boundary if** the limit lives in the refund tool or an ACS policy given the history |
| 8 | A real customer's compromised mailbox asks for a new address and refunds | Open | Inside the mandate; named, with proposed boundaries | No platform rule applies: every call is allowed. **Bounded and accepted:** confirmation link, per-customer cap, named owner |

Read down the right-hand column and the layers separate. Rows 1 to 3 are the platform's, and MXC handles them well: by construction, outside the agent's reach. Rows 4 to 7 are where the two halves meet. The hook exists, in ACS, in the tool, in the code host, but the content of the rule (which branch, which labels, whose voice, how many) comes from the business's mandate. Row 8 is inside the mandate altogether. No platform rule can refuse a genuine customer's account asking for something the agent is authorised to do. The policy names it, proposes the boundaries that shrink it, and the [risk that is left](every-risk-is-already-accepted.md) is accepted by a named person for a stated interval.

To be clear about what this table is: the scenarios are reasoned from the published behaviour of MXC and ACS and from our own policies and vaults; they are not a test run. Rows 5 to 8 come from [Hope or enforcement](https://sgit.ai/demos/vaults/hope-or-enforcement/index.md), the [connector twin](https://sgit.ai/demos/vaults/connector-twin/index.md) and our own agent team. The eight rows are published as [data](data/where-the-platform-draws-the-line__scenarios.json). The next step is to publish them as a vault with every row computed, the way Hope or enforcement was.

## How MXC and ACS map to an Agent Behaviour Policy

MXC in one page: the policy file, the modes, and where each piece lands in the Agent Behaviour Policy. Permissive mode measures the reach; learning mode calibrates it; enforcement mode turns rows into boundaries. ACS adds the tool-call layer, and whether it is a boundary depends on who owns the host.

| Agent Behaviour Policy | MXC | ACS |
|---|---|---|
| **Reach**, measured | Permissive mode's activity report: what the workload tried to touch with nothing blocked | Post-tool-call and shutdown records |
| **Calibration** against reality | Learning mode: blocked and recorded | Evidence providers and logged verdicts |
| **Mandate** | Not expressed. A policy says what the workload may touch, not what it is for | Not expressed. The manifest says where checks run; the rules come from the author |
| **Gap** | Derived only if a mandate exists to compare against | The same |
| **Barrier: boundary** | Paths, address ranges, ports, desktop, enforced by the OS, outside the workload | Tool-call verdicts enforced by the host, if the agent cannot edit the host or manifest |
| **Barrier: setting** | A developer policy file the agent itself can edit | A manifest inside the agent's own writable files |
| **Owner and expiry** | Organisation policy through Intune (coming) | Not expressed |

For RiskMandate, three things follow.

**MXC and ACS are barrier sources.** When an ABP row has a matching MXC deny that the agent cannot change, the barrier is a boundary, and the policy can say so with evidence: the JSON, its version, and who installed it. One warning goes with that. An MXC policy file sitting inside a coding agent's own read-write path is a setting, not a boundary. We have lived that one: the rule that let our synthetic users drive a browser sits in a settings file the agent's own account can write, so by our own test it is a setting with a person's approval on record. The policy file must live where the workload cannot write.

**Activity reports are footprint.** Permissive and learning-mode reports are exactly the evidence the [footprint](footprint-and-blast-radius.md) proposal asks for: what the agent actually did, read afterwards, with nobody inline. Read against a mandate, they produce the two findings that matter: a near miss, and a dormant mandate.

**The policy is what writes the rules.** ACS needs Rego; MXC needs paths and ranges; the refund tool needs a number. None of them can say what the numbers should be. An ABP row such as "removes labels only from the support queue; never from finance labels; at most twenty a run" is the source that compiles down into an MXC path, an ACS policy and a tool limit. Generating MXC JSON and ACS policies from an ABP is a design today, not a product. It is the integration RiskMandate's model was built for, since [we are not inline](riskmandate-ten-questions.md), and the customer's own stack enforces.

## Not the summit

MXC and ACS are the most complete platform controls for agents I have seen, and they should be in place wherever agents run on Windows, and on the other platforms the process container covers. With them, rows that a behaviour policy can only describe as hope become boundaries that the agent cannot argue with. That is the move [Hope or enforcement](hope-or-enforcement.md) measured, from 97% hope to 23%, and here it is arriving as platform features rather than custom code. This is a big deal, and I want to be clear about that.

But it is a stage of the climb, not the top. Above the platform's line sit the layers a business actually runs on: the function, the process, the client, and what the company says it is for. Each refines the one below, inside the room the one below allows, and each has its own owner. The platform cannot write those layers, and should not try: it does not know what a label means here. The business can, and the behaviour policy is where it does. Where the platform draws its line, the business's work starts.

## Where to start

- **Turn on MXC for coding agents now,** deny by default, and keep the policy file outside every path the agent can write.
- **Run new agents in permissive mode first,** read the activity report as the agent's reach, and write the mandate against it before you enforce.
- **Put the external-facing tool calls behind ACS or an equivalent,** installed by somebody other than the agent's owner, failing closed.
- **Write the business rules down,** layer by layer: which labels, which recipients, whose voice, how many per day, which customer. They are the content the platform's hooks are waiting for.
- **Mark each rule with what enforces it,** and count what is still hope. That count is what the platform has not covered yet.
- **Name the owner of what is left,** and the date it is next accepted.

If you are rolling out MXC or ACS and want to try writing the layer above it for one of your agents, let's talk: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded after reading Microsoft's announcement. I asked an agent in a separate Claude session to check the memo against Microsoft's own material and this network's pages, and to draft this article with its figures and data; this site's agent then rewrote it in the voice of this site and added what we learned this week. The argument is mine, and so is the editorial responsibility. The briefing is built from Microsoft's [announcement of 7 October 2026](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/) (Windows Developer Blog), the [MXC repository](https://github.com/microsoft/mxc) as of 11 October 2026 (README, configuration schema documentation, learning-mode documentation and the 1.0.0 contract fixtures, MIT licence), and Microsoft's [ACS announcement](https://commandline.microsoft.com/agent-control-specification-runtime-governance/) of 2 June 2026 (Command Line) with the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit). Microsoft's material is paraphrased throughout and quoted twice. The JSON example uses the schema's field names with illustrative paths, and validates against the 1.0.0 schema. The eight scenarios are reasoned, not run. Also: AWS's [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/); on this site, [The same argument, in our words](the-same-argument-in-our-words.md), [Authority outside the model](authority-outside-the-model.md), [the business logic](the-behaviour-policy-is-the-business-logic.md), [Hope or enforcement](hope-or-enforcement.md), [A second reader the agent cannot skip](a-second-reader-the-agent-cannot-skip.md), [the connector twin](connector-twin-before-you-deploy-an-agent.md), [Footprint and blast radius](footprint-and-blast-radius.md), [Every risk is already accepted](every-risk-is-already-accepted.md), [How to run synthetic users](how-to-run-synthetic-users.md) and [Ten hard questions for RiskMandate, answered](riskmandate-ten-questions.md); RiskMandate's [Lab 01, the grant is user-shaped, not data-shaped](https://riskmandate.ai/lab-connector-grants.html); and the vaults [Hope or enforcement](https://sgit.ai/demos/vaults/hope-or-enforcement/index.md) and [Connector Twin](https://sgit.ai/demos/vaults/connector-twin/index.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#where-the-platform-draws-the-line)

### Builds on

- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.

### Continued by

- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 70 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=70)

**Posting this article on LinkedIn?** The cover is [where-the-platform-draws-the-line.jpg](banners/where-the-platform-draws-the-line.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-the-platform-draws-the-line.html)*
