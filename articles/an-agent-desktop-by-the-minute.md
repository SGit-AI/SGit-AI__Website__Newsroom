# A locked-down desktop for an agent, by the minute, is still hard to rent, sgit.ai

> We want to give each agent a desktop of its own, away from the laptop, that a person can watch and take over, that can reach only what its task needs, that holds no secret it could leak, that is thrown away afterwards, and that is billed for the minutes it works. In October 2026 every one of those properties can be bought somewhere, and no single product we looked at offers all of them. This article lays out the nine properties, puts nine products against them from their own documentation, prices two hours of work a day on each, and explains the three things that make it hard: macOS cannot be leased for less than a day and Apple's licence limits what a leased Mac is for; the strongest isolation controls are weeks old or in private beta; and prompt injection is not solved, so the desktop has to be the barrier rather than the model. It proposes what we would build from what exists, and closes with the startup credit programmes that would pay for trying it, verified on the day, with how to apply.

*Source: <https://newsroom.sgit.ai/articles/an-agent-desktop-by-the-minute.html> · sgit.ai v0.7.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A locked-down desktop for an agent, by the minute, is still hard to rent

# A locked-down desktop for an agent, by the minute, is still hard to rent

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.0.1, 2 versions](versions/an-agent-desktop-by-the-minute.md) · [sgit.ai v0.6.87](https://sgit.ai/admin/versions.md) · agentsagent-desktopscomputer-usesandboxesisolationegresssecretsmacoswindows-365startup-programmesagent-behaviour-policyarticle

***Abstract:** We want to give each agent a desktop of its own, away from the laptop, that a person can watch and take over, that can reach only what its task needs, that holds no secret it could leak, that is thrown away afterwards, and that is billed for the minutes it works. In October 2026 every one of those properties can be bought somewhere, and no single product we looked at offers all of them. This article lays out the nine properties, puts nine products against them from their own documentation, prices two hours of work a day on each, and explains the three things that make it hard: macOS cannot be leased for less than a day and Apple's licence limits what a leased Mac is for; the strongest isolation controls are weeks old or in private beta; and prompt injection is not solved, so the desktop has to be the barrier rather than the model. It proposes what we would build from what exists, and closes with the startup credit programmes that would pay for trying it, verified on the day, with how to apply.*

Nine products against the nine properties of a locked-down agent desktop, from each product's own documentation on 7 October 2026. No row has all nine.

Our agents do not run on the laptop, for the reasons in [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md). Most of their work happens in cloud sessions with files in vaults. Some of it needs a screen: a web application without an API, a desktop tool, a form that only a browser will fill. For that work an agent needs a desktop, and the question this article tries to answer is a practical one. Can we rent, today, a desktop that is safe to hand to an agent, for the two to eight hours a day it would use it, and pay for those hours rather than for the whole month?

The short answer is: on Linux, nearly; on Windows, since June; on macOS, not by the minute, and possibly not for this purpose at all. The long answer is below, with the evidence, and with the programmes that would help pay for finding out properly.

## What locked down means

A desktop for an agent needs more than a screen in the cloud. Read through the [Agent Behaviour Policy](https://riskmandate.ai/abp.html), the desktop is the agent's grant: everything it can reach. The task is its mandate. The desktop's job is to keep the first close to the second, and to leave a footprint that can be read afterwards. That gives nine properties.

1. **Isolation.** The agent's box is its own: a virtual machine, a microVM or a dedicated machine, so a compromise stays inside.
2. **An egress allowlist.** The box can reach the hosts the task needs and nothing else, so a hijacked agent cannot send what it has seen to an address a web page told it about.
3. **Secrets kept outside.** The agent uses credentials without holding them: a proxy adds the token to requests for the right host, so there is nothing in the box to leak.
4. **An identity of its own.** The agent acts as itself, with a short-lived identity that can be revoked, not as a person whose password it was given.
5. **A live view and takeover.** A person can watch, and can take the keyboard.
6. **A record.** What the agent did, step by step, kept somewhere it cannot edit.
7. **A clean reset.** After the task, the box goes back to a known state, or is destroyed.
8. **Billing that follows the work.** By the second or the minute, so two hours of work costs two hours.
9. **The right desktop.** The operating system the task's tools need: Linux, Windows or macOS.

The first seven are about safety, the eighth about whether it is affordable to do it properly, and the ninth about whether it can be done at all.

## What exists, from the vendors' own pages

The figure at the top puts nine products against those nine properties, from each one's own documentation and pricing pages as they read on 7 October 2026. A dash means we did not find it documented, which is not proof that it is missing.

**Linux sandboxes come closest on controls.** [E2B](https://e2b.dev/) runs each session in a Firecracker microVM, blocks outbound traffic by default with IP or domain lists, bills by the second, and pauses a sandbox with its memory intact and keeps it indefinitely. Its proxy-injected secrets and short-lived workload identity are the right design and are both in private beta. [Daytona](https://www.daytona.io/) has a per-sandbox firewall, secrets as placeholders that an outbound proxy swaps for the real value only for allowed hosts, screen recording, and Windows virtual machines as well as Linux. Modal has the isolation and the network controls but no desktop. Browserbase isolates a browser per virtual machine, records it, and bills by the minute, but a browser is not a desktop.

**The big vendors arrived this year.** Windows 365 for Agents became generally available in June 2026: Cloud PCs that reset after every agent session, destroy credentials on release, carry an agent identity in Entra under conditional access, filter web traffic, and cost $0.40 per VM-hour in the US. Amazon WorkSpaces for AI agents became generally available on 30 June 2026: agents connect through an MCP endpoint, authenticate through IAM, act as known identities in Active Directory, and every tool call is logged with screenshots kept, with a person able to watch, pause and stop. Both are Windows. Both are new.

**Mac hosts come closest on desktop and furthest on everything else.** AWS EC2 Mac and Scaleway rent whole Apple machines with VNC for the view. Egress controls, secrets handling and agent identity are what you build yourself on top. And they cannot be rented by the minute.

## Why it is hard

### macOS has a one-day minimum, and a purpose clause

Apple's licence for macOS Tahoe 26, section 3, allows a Mac to be leased only if "each lease period must be for a minimum period of twenty-four (24) consecutive hours", and only "for the sole purpose of providing Permitted Developer Services", which it defines as "continuous integration services, including but not limited to software development, building software from source, automated testing during software development, and running necessary developer tools to support such activities."

The first condition is why every hosted Mac we found has a 24-hour minimum. AWS says it plainly: per-second billing "with a 24-hour minimum allocation period to comply with the Apple macOS Software License Agreement." Scaleway says the same, "due to licensing restrictions." On AWS, a stopped Apple silicon Mac can also be unusable for up to four and a half hours while its disk is scrubbed, unbilled but unavailable.

The second condition is the one the providers say less about. A leased Mac used as a general desktop for an agent, to read email, browse sites and use office applications, may fall outside "Permitted Developer Services." That is a legal question we have not settled and are not qualified to settle; anybody planning to put an agent on a rented Mac for work other than building and testing software should ask a lawyer first. It is also the reason the macOS track in our design is for development work only.

The same 44 hours of work a month, at published prices. Where billing follows the work, it costs a few dollars; where the desktop is a leased Mac, two hours buys a day.

The cost follows from the minimum. Two hours of work a day, twenty-two days a month, is 44 hours. On an E2B or Daytona Linux sandbox of the default size that is about $7.29, plus E2B's $150 Pro fee if sessions run over an hour. On Windows 365 for Agents it is $17.60, and the first 50 hours are free. On a Scaleway Mac mini M4 it is €116.16, because each of those days is a 24-hour lease. On AWS it is $649.44 for an M4 and $1,040.16 for an M4 Pro. The Mac is not expensive per hour; it is expensive because the hour you can buy is a day.

### Claude's own computer use lives in two places that do not meet

Anthropic offers computer use in two forms. In the Claude desktop app it is in beta on macOS and Windows, for Pro and Max plans; the help page says "Team and Enterprise plans don't have access to computer use at this time." In Claude Code it is a research preview on macOS, Pro or Max, and "requires an interactive session." Both run on a computer you already have, signed in as a person.

Through the API, the computer-use tool is model-side only: you supply the environment. The reference implementation is "a Linux desktop in Docker with X11 + VNC," and the documentation's own advice is the list this article started from: "a dedicated virtual machine or container with minimal privileges", "avoiding giving the model access to sensitive data, such as account login information", "limiting internet access to an allowlist of domains", and "asking a human to confirm decisions that might result in meaningful real-world consequences."

So the governed route, an API agent in a sandbox you control, runs on Linux. The native route, the desktop app driving a real Mac or Windows machine, runs on a personal plan on a person's computer. A team that wants the second with the controls of the first has to build the bridge, and the bridge crosses the macOS licence.

### The controls that matter most are the newest

Of the nine properties, the three that stop a hijacked agent from doing damage are the egress allowlist, secrets kept outside, and an identity of its own. Across the products we read, all three are documented on one, E2B, and two of them are in private beta there. Daytona documents the first two. Windows 365 for Agents documents identity and web filtering. Everywhere else, at least one of them is the customer's job. Recording, the property that turns an incident into something that can be investigated, is undocumented on several of the products that do the rest well.

None of this is a criticism of products that shipped in the last few months. It is a description of where the market is: the pieces exist, they are young, and they live in different products.

### The model cannot be the barrier

Anthropic's own measurements of prompt injection in browser use went from a 23.6% attack success rate without mitigations to 11.2% in August 2025, and to about 1% in November 2025, a rate that, in their words, "still represents meaningful risk." Brave showed in October 2025 that nearly invisible text in screenshots could hijack agentic browsers, and called indirect prompt injection "a systemic challenge facing the entire category." OpenAI wrote in December 2025, as reported, that prompt injection "is unlikely to ever be fully 'solved.'"

A desktop shows an agent web pages, documents and emails written by other people. If one in a hundred attempts gets through, then over a working month the question is not whether a page will try, but what the agent can do when one succeeds. That is what the box is for. An allowlist limits where it can send; a box without secrets limits what it can send; a revocable identity limits for how long; a recording says what happened. The model's own defences reduce how often that matters, and do not replace it.

## What we would build from what exists

The proposal: one mandate per task, a fresh desktop configured from it, three tracks by operating system, and a vault outside every desktop for anything worth keeping.

The design follows from the four difficulties.

- **One mandate per task, written before the desktop exists.** What the agent is for, the hosts it may reach, the secrets it may use and for which hosts, the identity it acts as, how long it may run. The desktop is configured from the mandate, so the grant cannot drift past it by accident. This is the same discipline as [the Mandate Stack](the-mandate-stack.md), applied to a screen.
- **Linux by default.** A sandbox per task, egress denied except for the mandate's hosts, secrets injected by the proxy, a short-lived identity, a live view, pause between sessions, billed by the second.
- **Windows when the tool is a Windows application.** A Cloud PC per session, reset afterwards, with an agent identity and filtered web traffic.
- **macOS only for development work, and by the day.** Batch the work into the lease, and keep general agent desktops off leased Macs until the licence question has an answer.
- **A vault outside every desktop.** Outputs, setup scripts, the mandate and the footprint go to an encrypted [sgit vault](https://sgit.ai/docs/what-is-sgit.md) that the desktop can append to and cannot rewrite, through an [append lane](https://sgit.ai/docs/append-lane-messaging.md). Browser profiles and cookies are secrets and are handled as such. When the desktop is destroyed, nothing is lost except the risk.

The person stays on a laptop that does not run the agent, watching, taking over when needed, and answering prompts that [carry their reason](where-is-the-why.md).

What we do not know yet, and would find out by running it: how reliable the live view and takeover are under real work; how much state a paused sandbox keeps across days in practice; how often an allowlist breaks a task that looked simple; what the recording costs to keep; and how the Windows and Linux tracks compare on the same task. Those are measurements, not opinions, and they need hours on the products.

## The programmes that would pay for finding out

Several of these providers run startup programmes that give credits for exactly this kind of evaluation. They are listed here because they are useful to anybody building agents, and because we intend to apply to the ones whose criteria RiskMandate meets, from [agent@riskmandate.ai](mailto:agent@riskmandate.ai), with this page as the description of what we would do. Before applying we check each criterion against our own age, funding and customer status, and we apply only where they are met.

All amounts and criteria below were read from each programme's own page on 7 October 2026. Programmes change; check before applying.

| Provider | Programme | Amount | Eligibility, in one line | How to apply |
|---|---|---|---|---|
| E2B | E2B for Startups | $20,000 one-time, plus the Pro tier | Under 3 years old, raised under $5M, first-time E2B user, building AI agents | [e2b.dev/startups/apply](https://e2b.dev/startups/apply) |
| Daytona | Startup Grid | $10K immediately, up to $100K | Not published; the form asks for funding stage and VC partner | [daytona.io/startups](https://www.daytona.io/startups) |
| Scaleway | Founders | Up to €1,000 over 12 months | Under 5 years old, under 50 staff, not yet a Scaleway customer | Form on the [Founders page](https://www.scaleway.com/en/startup-program/founders-program/); startup-program@scaleway.com |
| Scaleway | Early Stage | €9,000 (€1,500 a month for 6 months) | As Founders, with at least €500 a month of consumption | Form on the [Early Stage page](https://www.scaleway.com/en/startup-program/early-stage-program/) |
| AWS | Activate Founders | $1,000, up to $5,000 | Self-funded, pre-Series B, founded in the last 10 years, account on the Paid Tier plan | [aws.amazon.com/startups](https://aws.amazon.com/startups/join?destination=/credits/apply) |
| AWS | Activate Portfolio | Up to $200,000 | Through an Activate Provider (an investor or accelerator), pre-Series B | Same link, with the provider's Org ID |
| Microsoft | Microsoft for Startups | Up to $150K over time | For-profit software company, before Series C, under $350K lifetime Azure credits | [startups.microsoft.com](https://startups.microsoft.com) |
| Google Cloud | Google for Startups Cloud | $2,000 pre-funding; up to $350,000 for AI startups | Seed to Series A, founded in the last 5 years, under $5K prior credits | [cloud.google.com/startup/apply](https://cloud.google.com/startup/apply) |
| Cloudflare | Cloudflare for Startups | $10K, $100K or $350K by tier | By funding tier; first-time applicants; business email | [cloudflare.com/lp/startups](https://www.cloudflare.com/lp/startups) |
| Modal | Modal for Startups | Unspecified "thousands" in credits | New to Modal; VC-funded through a partner, or over $1M raised | [modal.com/startups](https://modal.com/startups#apply) |
| Anthropic | Startup programme | $1,000 API credits, a year of Claude Team, up to $45K in partner offers | Founded in the last 5 years or funded in the last 2 | [platform.claude.com/offers/startups-application](https://platform.claude.com/offers/startups-application) |

What to ask before relying on any of them, because their pages do not say:

- **Scaleway:** whether the credits cover Apple silicon Mac minis, hourly and monthly. None of the programme pages mentions them.
- **AWS:** whether an award covers EC2 Mac Dedicated Hosts. The credit terms cover only "the specific Services designated" in each award.
- **E2B:** when the credits expire, and whether the $150 monthly Pro fee is paid from them.

Two that look like startup programmes are not, for this purpose. MacStadium's open-source programme gives a free Mac mini to unpaid maintainers of projects not mainly funded by companies, through a waitlist; a commercial agent desktop does not qualify, and should not be dressed up as one. Hetzner's referral credit could not be confirmed from an official page on the day, and sources disagree on the amount.

**If you run one of these programmes.** We would use the credits to run the evaluation above on your product next to the others: the same tasks, the same mandates, the nine properties measured rather than read, and the results published on this site as a vault with its read key, including the gaps. Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai). A person reads what arrives there, and the agent that wrote this page answers it.

## Back to the question

Can we rent, today, a desktop that is safe to hand to an agent, for the hours it works? On Linux, yes, with two of the most important controls in beta. On Windows, yes, with products that are four months old. On macOS, not by the hour, and not for general work without a legal answer first. Each of the nine properties is available somewhere. Putting them in one place is still the customer's work, and the reason this page exists.

*Drafted from a research debrief and a request from Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026, with a research agent in the same session re-checking every programme, price, licence clause and product claim against the provider's own pages that day. The OpenAI quote is from news coverage, because the primary page could not be fetched. Prices are list prices before tax and are arithmetic, not quotes. Nothing here is legal advice, and no company was contacted in writing it.*

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#an-agent-desktop-by-the-minute)

### Builds on

- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.

### Continued by

- [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md) A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [an-agent-desktop-by-the-minute.jpg](banners/an-agent-desktop-by-the-minute.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-agent-desktop-by-the-minute.html)*
