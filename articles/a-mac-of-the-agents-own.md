# A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies, sgit.ai

> Our agents already have dedicated resources with a small blast radius: their own mailbox, their own code-host account, their own Claude account. The next one is a desktop of their own, and it should be a Mac, because that is where most agent desktop apps arrive first. This is a business plan for somebody else to build, following our earlier research on renting an agent a desktop. It started as a pool of Macs rented by the minute, and Apple's licence rules that out: a leased Mac must be held for at least 24 hours, for developer services, by one customer, and virtual copies may not be time-shared. So the plan is the shapes that are allowed: a dedicated Mac per customer, run for them, with a per-minute meter on top and a clean desktop per run built from encrypted vaults; developer agents on leased Macs; software for the Mac mini you keep; and a request to Apple for terms. The reason to want any of it is in the three behaviour policies: the same customer service agent on your own Mac, on a dedicated Mac and on a hardened one, where the excess nothing bounds falls from 23 rows to 11 to 3.

*Source: <https://newsroom.sgit.ai/articles/a-mac-of-the-agents-own.html> · sgit.ai v0.7.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies

# A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-09 · [article v1.2.0, 3 versions](versions/a-mac-of-the-agents-own.md) · [sgit.ai v0.7.16](https://sgit.ai/admin/versions.md) · agentsagent-desktopsmacosbusiness-planagent-behaviour-policylicensingvaultspkisgitwardley-mapsisolationcoworkcomputer-usearticle

***Abstract:** Our agents already have dedicated resources with a small blast radius: their own mailbox, their own code-host account, their own Claude account. The next one is a desktop of their own, and it should be a Mac, because that is where most agent desktop apps arrive first. This is a business plan for somebody else to build, following our earlier research on renting an agent a desktop. It started as a pool of Macs rented by the minute, and Apple's licence rules that out: a leased Mac must be held for at least 24 hours, for developer services, by one customer, and virtual copies may not be time-shared. So the plan is the shapes that are allowed: a dedicated Mac per customer, run for them, with a per-minute meter on top and a clean desktop per run built from encrypted vaults; developer agents on leased Macs; software for the Mac mini you keep; and a request to Apple for terms. The reason to want any of it is in the three behaviour policies: the same customer service agent on your own Mac, on a dedicated Mac and on a hardened one, where the excess nothing bounds falls from 23 rows to 11 to 3.*

The same customer service agent on three desktops, in the published behaviour-policy grammar: on your own Mac, on a dedicated remote Mac, and on a hardened one. What changes is not the agent; it is what the desktop holds and what stands in the way.

**Where this comes from.** It follows [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md), and it is written, like the other [business plans on this site](https://sgit.ai/startups/business-plans.md), so that anybody could build it. It names no provider. The whole plan, with the numbers, the policies and a calculator, is in [the Agent Desk vault](https://sgit.ai/demos/vaults/agent-desk/index.md).

## In short

- **The next dedicated resource is a desktop.** Our agents already have their own mailbox, their own code-host account and their own Claude account, which in practice is dedicated compute. A desktop of their own is the next step, because I will not run them on [my own machine](why-my-agents-do-not-run-on-my-laptop.md).
- **It should be a Mac.** Most agent desktop apps arrive on the Mac first, it is the desktop most people already know, and it is the one you cannot rent by the minute today.
- **Apple's licence decides the shape.** A leased Mac must be held for at least 24 hours, only for developer services, by one customer at a time; virtual copies may not be time-shared. The pool of Macs rented by the minute that I first imagined is not allowed.
- **The shapes that are allowed** are a dedicated Mac per customer, run for them, with a per-minute meter on top; developer agents on leased Macs; software for a Mac you keep; and a request to Apple for written terms.
- **The vaults are the state.** Boot a clean Mac, install sgit, hand it one key, clone one set-up vault, and everything else comes from there: profiles, allowlists, the policy, the agent's slice of code and data, and the record of what it did.
- **The reason to want it is the behaviour policy.** For one customer service agent, the excess over the mandate that nothing bounds is 23 rows on your own Mac, 11 on a dedicated Mac and 3 on a hardened one.

## The next dedicated resource

The way we run agents has been moving in one direction: each agent gets resources of its own, with a small blast radius. A [dedicated mailbox](six-agents-one-inbox.md) instead of mine. A dedicated code-host account. A dedicated Claude account, which in practice is dedicated compute. [The agent team as it runs](the-agent-team-as-it-runs.md) shows what that looks like day to day.

The natural next step is a desktop. Claude's desktop app and Cowork are very capable on a desktop, and these days Claude can drive desktop applications well: mail, messages, a browser, creative and video tools. But [I do not run agents on my laptop](why-my-agents-do-not-run-on-my-laptop.md), because everything I have is on it. The agent needs a desktop of its own: one machine, one application, one set-up, holding only what the agent is meant to have.

## Why a Mac

Three reasons. The providers of agent desktop apps tend to ship to the Mac first and prefer it, so it is the best environment to be in. It is the desktop most people already know. And it is the one that is hard to get on demand: ironically, Windows and Linux run happily as virtual machines, by the hour, from many places, and a Mac never has been. That gap is the business.

It is also a better place to put controls than a person's own machine. A Mac whose only user is an agent does not need to be usable by a person, apart from a browser for watching it. It can be supervised, profiled, allowlisted and logged far beyond what anybody would tolerate on their own laptop.

## What Apple's licence allows

This is where the first version of the idea died, and it is better to say so on the first page than to discover it after building. The research is in the vault, with every clause quoted from Apple's licences for macOS 15, 26 and 27. The short version, and it is a reading, not legal advice:

- **Leasing a Mac is allowed only for developer services.** Section 3 allows a lease "for the sole purpose of providing Permitted Developer Services", defined as "continuous integration services, including but not limited to software development, building software from source, automated testing during software development".
- **For at least a day, to one customer.** "Each lease period must be for a minimum period of twenty-four (24) consecutive hours", and the customer must have "sole and exclusive use and control" of the software and the hardware.
- **Virtual copies are limited, and may not be time-shared.** Up to two additional copies in virtual machines on a Mac you own or control, for software development, testing, macOS Server or personal, non-commercial use, and not "in connection with service bureau, time-sharing, terminal sharing, relay service or other similar types of services".
- **One user at a time.** "Only one user may use the Apple Software at a time."
- **And one practical limit:** a virtual machine's saved state is tied to the Mac it was saved on, so a pool could not move a running desktop between Macs anyway.

So a shared pool of Macs whose desktops are rented by the minute to many customers, for general agent work, is out. Two things soften that. The macOS 27 licence now opens its virtualisation and leasing clauses with "except as otherwise provided in writing, signed, or issued by an authorized representative of Apple", which is a route to written terms for a use Apple wants to support. And an agent desktop used for email or office work, rather than development, is a question for a lawyer before it is a product.

## The shapes that are allowed

| Shape | What it is | How it sits against the licence |
|---|---|---|
| **A. Your Mac, run for you** | The customer owns or finances the Macs; the operator hosts and runs them | The cleanest: the customer's own Mac, one agent desktop at a time on it |
| **B. A dedicated Mac, metered** | One customer leases a Mac for a day or a month; desktop time inside it is metered by the minute | Allowed for developer services; general office work needs legal advice |
| **C. Developer agents** | Coding agents on leased Macs, including in virtual machines | The licence's own purpose |
| **D. Ask Apple** | Written terms for agent desktops | The route macOS 27's new wording opens |
| **E. Software, not hosting** | The same set-up as software for a Mac mini you keep | Your own Mac; virtual machines for personal use or development |

The plan's recommendation: build **A** and **C**, give away **E**, ask for **D**, and do not build the pool. Per-minute pricing survives, as a meter on a Mac one customer holds, never as a share of a Mac that others use.

## A clean Mac, a key, and everything else from the vaults

One Apple silicon Mac per customer, one agent desktop at a time, and up to two virtual machines where the work is development. Keys come from the owner, encrypted to each desktop's own key; set-up, code, data and policy come from vaults; every request goes through a proxy and gateway, and every event goes to an audit vault.

The part I like most is how little is new. We already have a great solution for saving state: [encrypted vaults](encrypted-memory-for-isolated-agents.md). So the desktop needs very little of its own. Boot a clean macOS, install sgit, give it one key, and clone one set-up vault. A small program in that vault does the rest.

Each run starts from a clean macOS on a Mac that belongs to one customer. The desktop's own key unlocks one set-up vault; a signed program in it applies the profiles, starts the proxy and the logging, and clones the agent's slice of the other vaults. At the end, results and the record are pushed and the session is erased.

The vaults divide the work, the way a supply chain should, with each party holding only its slice:

- **A set-up vault**: the signed entry program, configuration profiles, the egress and binary allowlists, and the behaviour policy.
- **Code and data vaults**, each cloned with [only the folder the task needs](https://sgit.ai/docs/partial-clones.md).
- **A mandate vault**, owned by the customer, which says what the agent is for.
- **Keys by PKI.** Each desktop has its own key pair; the vault keys it needs are encrypted to its public key and decrypted inside the running desktop, and the private key lives in the desktop's keychain. That is [authorisation by encryption, not by privilege](riskmandate-ten-questions.md), using the [PKI already in sgit](https://sgit.ai/docs/pki.md).
- **An audit vault**, where every process, network and file event goes as it happens, off the machine.

The vault includes the bootstrap itself, a short readable script. Its key-handling steps were run for this article with sgit 0.20.0 on Linux: a key pair generated, a read key encrypted to it and decrypted, an entry program signed and verified, a tampered one refused. Nothing has run on a Mac yet; the plan says so.

**The architecture, Mermaid source**

[rendered image](images/ad-arch.webp)

```
flowchart LR
  subgraph cust["The customer"]
    direction TB
    OWN["Owner<br/>holds the vault keys"]
    POL["Mandate vault<br/>the ABP, the allowlists"]
  end
  subgraph op["The operator: Agent Desk"]
    direction TB
    subgraph host["Apple silicon Mac, dedicated to one customer"]
      direction TB
      VM1["Agent a1 desktop<br/>Claude desktop or Cowork<br/>one user at a time"]
      VM2["Up to two VMs<br/>for development work"]
    end
    PX["Egress proxy and MCP gateway<br/>allowlist, logs"]
    OBS["Observability<br/>process, network, file events"]
  end
  subgraph vaults["Encrypted vaults: ciphertext only on the server"]
    direction TB
    SV[("Set-up")]
    CV[("Code")]
    DV[("Data, scoped per agent")]
    AV[("Audit log")]
  end
  NET["Only the services<br/>the mandate needs"]
  OWN -- "keys, encrypted to<br/>each desktop's PKI key" --> VM1
  POL --> VM1
  VM1 --> SV & CV & DV
  VM1 -- "every request" --> PX --> NET
  VM1 --> OBS --> AV
  VM2 --> PX
```

**The boot sequence, Mermaid source**

[rendered image](images/ad-boot.webp)

```
sequenceDiagram
  autonumber
  participant U as Customer or scheduler
  participant H as Dedicated Mac: one customer
  participant V as Clean macOS session
  participant K as Key delivery
  participant S as Set-up vault
  participant O as Other vaults
  U->>H: start a desktop for agent a1
  H->>V: erase and boot clean, or clone a golden image for a development VM
  K->>V: this desktop's private key, into the keychain
  V->>V: install sgit, then read the vault key decrypted with the desktop's key
  V->>S: sgit clone the set-up vault, scoped
  S-->>V: bootstrap program, profiles, allowlists, the ABP
  V->>V: apply profiles, start the egress proxy and logging
  V->>O: clone code, data and mandate vaults, each scoped to a1
  Note over V: the agent app starts and works its task
  V->>O: commit and push results and the audit log
  U->>H: stop, then erase or discard
  Note over H: nothing secret stays on the host
```

## Three desktops, one agent

The reason to want any of this is the behaviour policy. The vault takes the customer service agent from [Hope or enforcement](hope-or-enforcement.md), the same fictional shop and the same mandate, and puts it on three desktops, writing each as an [Agent Behaviour Policy](https://abp.sgit.ai/) in the published grammar: the grant, the mandate, the delta, and what stands in the way of each row, from none, through an expectation and a setting, to a boundary, which is the only kind that is a control.

|  | Your own Mac | A dedicated remote Mac | A hardened dedicated Mac |
|---|---|---|---|
| Grant, of 33 rows | 33 | 22 | 22 |
| Unbounded excess | 23 | 11 | 3 |
| Of which cannot be undone | 15 | 6 | 1 |
| Rows held by a boundary | 0 | 1 | 9 |
| Hostile inputs stopped by a boundary or an empty grant, of 22 | 0 | 2 | 12 |

- **On your own Mac**, the behaviour policy is enormous, because the grant is everything you have: your mail, your files, your browser sessions, your keychain, your messages. Nothing is held by a boundary.
- **On a dedicated Mac**, it is still Claude doing the work, and the policy is already much smaller, because there are no other secrets on the machine. The only secrets are the ones the agent is supposed to have.
- **On a hardened Mac**, third-party controls do the rest: a standard account on a supervised Mac with profiles it cannot remove, an egress proxy that allows only the mandate's hosts, a binary allowlist, mail through a gateway that allows only the assigned thread and a reply to its sender, and every event streamed to the audit vault. The tools are the kind RiskMandate has written [business cases](https://riskmandate.ai/business-cases.html) for, and open-source macOS controls.

What is left on the hardened Mac is mostly one thing: the shop's admin screen, which shows every customer. That is a finding about the shop's software, not about the desktop, and it is the kind of finding a behaviour policy exists to produce. One more is a limit of macOS itself: screen recording, which computer use needs, cannot be granted by a profile, so a person has to approve it once, in the image.

The customer service agent's 22 hostile inputs, 16 from the Hope or enforcement mailbox and 6 written for a desktop, on the three desktops: what stopped each one, and what still depends on the agent.

## The numbers

The calculator: usage, the meter, and five options a month. Every number except Apple's prices is a labelled assumption, with its arithmetic in the vault.

My own use is the test case: four scheduled runs a day of about half an hour, plus two interactive hours on working days, about 104 desktop hours a month. On the plan's assumptions, a dedicated Mac with the meter costs about £211 a month; a Mac mini bought and run yourself about £119, counting your own time; daily 24-hour leases about £390, using 17% of each day you pay for. The dedicated Mac wins once looking after your own takes more than about four hours a month, and beats daily leases once you need a Mac on more than about twelve days a month. The interesting customer is not the person with one Mac mini; it is the team that would otherwise buy, set up, secure and maintain several, and the team doing browser automation that should not be doing it on anybody's laptop.

## The map

The agent's desktop moves from custom-built to product, on parts that are already products or commodities: Apple silicon Macs, the macOS virtual machine, the models, the desktop agent apps. State, keys and lock-down move with it, because the vaults, the PKI and the policies already exist as parts.

**The map, Mermaid wardley-beta source**

[rendered image](images/ad-map.webp)

```
wardley-beta
  title Agent Desk: productising the agent's desktop, on parts that are already commodities
  anchor "A business running agents" [0.97, 0.62]
  component "Work done by agents" [0.88, 0.52]
  component "Agent Behaviour Policy" [0.78, 0.34]
  component "Agent desktop, on demand" [0.70, 0.24]
  component "Desktop agent apps" [0.62, 0.62]
  component "Observability and lock-down" [0.52, 0.40]
  component "Credentials by key, PKI" [0.44, 0.36]
  component "State in vaults" [0.36, 0.48]
  component "macOS virtual machine" [0.28, 0.56]
  component "Models" [0.22, 0.76]
  component "Apple silicon Mac" [0.12, 0.86]
  "A business running agents" --> "Work done by agents"
  "Work done by agents" --> "Agent Behaviour Policy"
  "Work done by agents" --> "Desktop agent apps"
  "Work done by agents" --> "Agent desktop, on demand"
  "Desktop agent apps" --> "Models"
  "Agent desktop, on demand" --> "Desktop agent apps"
  "Agent desktop, on demand" --> "Observability and lock-down"
  "Agent desktop, on demand" --> "Credentials by key, PKI"
  "Agent desktop, on demand" --> "State in vaults"
  "Agent desktop, on demand" --> "macOS virtual machine"
  "Agent Behaviour Policy" --> "Observability and lock-down"
  "macOS virtual machine" --> "Apple silicon Mac"
  evolve "Agent desktop, on demand" 0.60
  evolve "State in vaults" 0.72
  evolve "Credentials by key, PKI" 0.66
  evolve "Observability and lock-down" 0.64
```

## What we are looking for

From a company that rents or hosts Macs, or wants to:

- **Dedicated Macs per customer, by the day or the month**, with an API to erase and re-provision between runs, so a clean desktop per run takes minutes.
- **A meter inside**, so a customer pays a fixed fee for the Mac and a per-minute price for the desktop time, with a higher price for the first hour or two and a taper after.
- **A developer-agent offer**, squarely inside the licence: coding agents on leased Macs and in virtual machines.
- **A joint approach to Apple** for written terms covering agent desktops, which the macOS 27 wording now makes possible.
- **The stack, open**: the bootstrap, the vault layout, the behaviour policies and the profiles are all in the vault, to take and run. What we would bring is the policies, the vaults, the keys, and [RiskMandate](https://riskmandate.ai/) to write the policy for each customer.

## Where to start

- **Read the licence section of the plan first**, then talk to a lawyer about your shape.
- **Start with shape A or C**, where the licence is clearest.
- **Write the behaviour policy before the product**: it is the argument, and it tells you which controls matter.
- **Measure the boot**: the plan assumes about five minutes from request to a working desktop; it has not been timed yet.
- **Keep state out of the machine**: one key in, vaults for everything else, and an erase at the end.

## One Mac, many agents: what changes when you queue them

*Added on 10 October 2026, after a question from the plan's author.*

The obvious next question: if a leased Mac must be held for at least 24 hours, can one customer fill that day with many agents, one at a time, cleaning up after each? The cleaning-up part is easy. With the bootstrap above, everything an agent touched comes from vaults and goes back to vaults, so wiping between runs is a deletion, not a project. And the agents in our own team already run on a schedule, several times a day.

The licence, read again with that question, cares about two things that queueing does not change: **what the Mac is used for**, and **who is using macOS**.

Six scenarios against the clauses that decide them. Queueing satisfies "one user at a time"; the purpose of a lease, and who the user is, decide the rest. A reading of Apple's text, not legal advice.

**Purpose.** A lease is valid only "for the sole purpose of providing Permitted Developer Services", which Apple defines as "continuous integration services, including but not limited to software development, building software from source, automated testing during software development, and running necessary developer tools to support such activities." So a queue of coding agents on a leased Mac fits: it is what a continuous integration runner already does, many jobs for one customer in a row. A queue of office agents, working in mail, a browser and desktop apps, is outside the lease however carefully it is scheduled.

**Who.** If my agents, with my credentials, do the work and my customers buy the result, I am the user of macOS. That holds for developer work on a lease even when the work is for clients: a consultancy's build machine. If my customers' own agents, with their own credentials, get slots on my Mac, my customers are using macOS in turn, which is the "service bureau, time-sharing" the licence excludes "whether such services are being provided within your own organization or to third parties", and each of them would need a lease of their own of at least 24 hours.

**The case worth a lawyer's hour.** On a Mac you own, Section 2B(ii) lets a business run macOS "by multiple individuals on a single shared Mac Computer that you own or control", alongside "only one user may use the Apple Software at a time". A queue of your own agents on your own Mac, wiped between runs, is the closest fit for office agents. Two words decide it: whether automated agents are "individuals", and whether rotating them is time-sharing "within your own organization".

**What would need Apple's written terms.** Two cases: office agents on a leased Mac, and customers' agents sharing one Mac. The macOS 27 licence adds "except as otherwise provided in writing, signed, or issued by an authorized representative of Apple" to the virtualisation and leasing clauses, which is the route. The narrow ask is easier than the broad one: one organisation, a lease of 24 hours or more, sole use, one agent at a time, wiped between runs, for non-developer work. It keeps every condition Apple already sets except the purpose.

So the plan's shapes hold, with one refinement. The dedicated Mac per customer (shape B) is needed whenever the agents are the customer's. When the agents are the operator's, doing work the customer buys, one Mac can serve many of them in turn, and for developer work that is already within the licence.

*Drafted from a voice memo by Dinis Cruz, who is the author of the idea and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 9 October 2026. The licence quotes are from Apple's macOS 15, 26 and 27 licences as published on apple.com; the reading of them is ours and is not legal advice. Mac prices are from Apple's UK store on 9 October 2026; every other number is an assumption, labelled in the vault. No provider is named, at the request of the author.*

## Threads

Startups & strategyAgents & policyVaults & method[This article as a graph →](graphs.md#a-mac-of-the-agents-own)

### Builds on

- [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md) Nine properties a safe agent desktop needs, nine products against them, the macOS day-long lease, and the startup credits that would pay for testing it.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [a-mac-of-the-agents-own.jpg](banners/a-mac-of-the-agents-own.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-mac-of-the-agents-own.html)*
