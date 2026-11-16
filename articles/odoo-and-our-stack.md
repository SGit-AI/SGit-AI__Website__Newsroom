# Odoo's agents can now write to the system of record: how our stack fits around Odoo 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, a module that measures the grant, and a first showcase for SHarness, sgit.ai

> Odoo is the open-source business system that a very large number of small and medium companies run their sales, accounts, stock and websites on, and in September Odoo 20 gave its AI agents the ability to create and update records, on their own, from automated and scheduled actions, and to be reached through a native MCP server. That is exactly the line I keep writing about, where an agent moves from assisting to executing in a system of record, and it is now arriving at small-business scale. An agent's power in Odoo comes from the tools it is given and the access of the user behind it; Odoo's documentation, as quoted by an integrator, says the AI does not enforce business rules; and agent conversations are kept for up to 30 days. So here is how our stack could integrate with Odoo. RiskMandate writes a behaviour policy for each Odoo agent, with the grant measured from Odoo itself, ideally by an Odoo module. AgentiCCells sells an Odoo cell on its usual ladder. SGit holds the plan, the approval and the result of every agent write, signed, for as long as the business needs it, with a small broker applying changes after a person approves. PKI gives each agent a key and each approval a signature. SHarness could get its first showcase bounding the Odoo server or the coding agent beside it. And VoiceDebrief can turn a meeting into a CRM note. The plan starts with a demo on a self-hosted Odoo.

*Source: <https://newsroom.sgit.ai/articles/odoo-and-our-stack.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Odoo's agents can now write to the system of record: how our stack fits around Odoo 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, a module that measures the grant, and a first showcase for SHarness

# Odoo's agents can now write to the system of record: how our stack fits around Odoo 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, a module that measures the grant, and a first showcase for SHarness

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/odoo-and-our-stack.md) · [newsroom v0.14.118](https://newsroom.sgit.ai/admin/versions.html) · odooerpabpriskmandateagenticcellssgitsharnessstrategyarticle

***Abstract:** Odoo is the open-source business system that a very large number of small and medium companies run their sales, accounts, stock and websites on, and in September Odoo 20 gave its AI agents the ability to create and update records, on their own, from automated and scheduled actions, and to be reached through a native MCP server. That is exactly the line I keep writing about, where an agent moves from assisting to executing in a system of record, and it is now arriving at small-business scale. An agent's power in Odoo comes from the tools it is given and the access of the user behind it; Odoo's documentation, as quoted by an integrator, says the AI does not enforce business rules; and agent conversations are kept for up to 30 days. So here is how our stack could integrate with Odoo. RiskMandate writes a behaviour policy for each Odoo agent, with the grant measured from Odoo itself, ideally by an Odoo module. AgentiCCells sells an Odoo cell on its usual ladder. SGit holds the plan, the approval and the result of every agent write, signed, for as long as the business needs it, with a small broker applying changes after a person approves. PKI gives each agent a key and each approval a signature. SHarness could get its first showcase bounding the Odoo server or the coding agent beside it. And VoiceDebrief can turn a meeting into a CRM note. The plan starts with a demo on a self-hosted Odoo.*

Our stack around Odoo: a policy per agent, an Odoo cell, a vault for the record, keys, kernel limits, debriefs.

## In short

- **Odoo 20 agents can write:** create and update records, from automated and scheduled actions, and through a native MCP server.
- **That is the assist-to-execute line, at small-business scale,** in the system that holds the sales, the accounts and the stock.
- **RiskMandate:** a behaviour policy for each Odoo agent, with the grant measured from Odoo, ideally by an Odoo module.
- **AgentiCCells:** an Odoo cell, from one agent on one workflow at £500 to a network at £20,000.
- **SGit and PKI:** plan in a vault, a person signs, a broker applies, and the record lasts.
- **SHarness and VoiceDebrief:** kernel limits around the Odoo server; meetings into the CRM.

## Why Odoo, and why now

[Odoo](https://www.odoo.com/) is an open-source suite of business applications, from CRM and accounting to inventory, documents and websites, used by a very large number of small and medium companies; third-party estimates put it at well over a hundred thousand customers, though I have not seen an official figure. In Portugal, it runs the national allocation of school teachers.

What changed is the AI. Odoo 19 introduced agents that "can learn from your documents and perform actions" ([Odoo 19 release notes](https://www.odoo.com/odoo-19-release-notes)). Odoo 20, released at Odoo Experience on 24 September 2026, goes further: you can ask an agent to create records, and "agents can be summoned by automated and scheduled actions"; and you can "connect to your database via MCP" ([Odoo 20 release notes](https://www.odoo.com/odoo-20-release-notes)). In other words, agents now execute in the system of record, on their own schedule.

That is the line I described in [where assist becomes execute](where-assist-becomes-execute.md): from summarising data to changing a system of record. It is where controls have to tighten, and it is now arriving in the business system of a great many small companies.

## Where the gap is

Three things stand out, from Odoo's own documentation and release notes and from integrators' summaries:

- **An agent's power comes from its tools and the user behind it.** An API key carries the issuing user's permissions, so an integration user set up as an administrator gives an agent an administrator's reach. Odoo's documentation, as an integrator quotes it, says the AI "does not enforce business rules, modify records directly, or guarantee the correctness of the operation": the tools do the work.
- **Approvals exist, but per agent and per tool.** Odoo 20 agents can ask for permission and stop at a tool-call limit; what a given agent may save without asking depends on how it was configured.
- **The record is short.** "Conversations with agents are now stored for up to 30 days after the last message was sent." For a business that has to explain a posted bill a year later, that is not an audit trail.

None of this is a criticism of Odoo; it is the same gap every agent platform has, and the reason [Agent Behaviour Policies](https://abp.sgit.ai/) exist.

## RiskMandate: a behaviour policy for every Odoo agent

An illustration: a behaviour policy for an Odoo vendor bills agent, with its grant, mandate, gap and barriers.

A behaviour policy for an Odoo agent records four things. The grant is what it can reach: the integration user's access groups and record rules, the agent's tools, and what the MCP connection exposes. The mandate is what the business asked for: for a bills agent, read incoming PDFs and draft vendor bills. The gap is the difference: it can post bills, create partners, read bank journals and send email, none of which it was asked to do. And the barrier is what stands in the way: Odoo's access rights are a boundary; the tool list is a setting an admin can change; the prompt is only an expectation ([what actually stands in the way](https://abp.sgit.ai/model/barriers/index.html)).

The strongest product idea here is to measure the grant automatically. Odoo stores its access rules as data, so an Odoo module could read the access groups, record rules, agent tools and API-key users, and write the grant section of each agent's policy, the way we read an agent's reach elsewhere ([what can your agent reach?](what-can-your-agent-reach.md)). Distributed through Odoo's apps store, it would put RiskMandate in front of the people who need it, at the moment they switch agents on.

## AgentiCCells: an Odoo cell

[AgentiCCells](the-intersection.md) sells agentic teams on a fixed ladder, and Odoo is a natural place for them to work. At £500, one agent on one Odoo workflow, vendor bills, lead triage or invoice reminders, with a narrowly scoped integration user and a behaviour policy. At £1,500, the same set up with the customer in two sessions and handed over. At £5,000, a team across sales, accounts and stock, with a conductor and a board. At £20,000, a network across companies or subsidiaries. The site factory can also make the small public sites that read products and events from Odoo ([the site factory works](the-site-factory-works.md)).

## SGit and PKI: plan, then apply, with a record that lasts

Plan, then apply, for writes to Odoo: snapshot, plan, policy check, signed approval, broker, record.

For consequential writes, the safest pattern is the one we already use for infrastructure: plan, then apply ([CI behaviour policies](ci-behaviour-policies.md)). The agent works from a snapshot of the records it needs, in a vault, and writes its proposed changes to a lane. The behaviour policy checks them against the mandate and its limits. A person approves, signing with their key ([a key for every person](a-key-for-every-person.md)). A small broker applies the change through Odoo's API, as a narrow user. And the vault keeps the plan, the approval and the result, signed, for as long as the business needs, readable by anyone with the key ([how a vault works](how-a-vault-works.md)).

That also answers the 30-day problem: the conversation can expire; the record does not.

## SHarness, VoiceDebrief and PrompTugal.news

- **SHarness:** Odoo is a Python server that many companies host themselves, and coding agents now work beside it. A kernel-enforced Process Behaviour Policy for the Odoo worker, or for the coding agent, bounds what either can read, write, run and connect to ([SHarness](https://sharness.ai/)). It could be SHarness's first real showcase.
- **VoiceDebrief:** a meeting becomes a transcript and a debrief, and then, through Odoo's API, a note and activities on the right CRM record, under a behaviour policy.
- **PrompTugal.news:** the Algarve's businesses and Odoo's partners in Portugal are both readers and stories, and PrompTugal's own outreach could run on Odoo as a worked example ([every story has an address](every-story-has-an-address.md)).

## The plan

1. **A demo:** a self-hosted Odoo, one agent on vendor bills, its behaviour policy published as RiskMandate's next example, and an article here.
2. **The pattern:** the vault-and-lane broker for Odoo writes, and the signed record.
3. **The offer:** an Odoo cell on AgentiCCells' ladder; the measured grant in RiskMandate.
4. **The channel:** Odoo partners, who implement Odoo for their customers and will need an answer for its agents; then the apps store.

## What to watch

- **Odoo moves fast:** agents, MCP and AI credits are its own. We are the governance layer around them, not a rival agent.
- **Plan gates:** on Odoo Online, the external API is available only on custom plans, so the first customers are likely Odoo.sh or self-hosted.
- **Old APIs are going:** the legacy XML-RPC and JSON-RPC are deprecated in favour of the JSON-2 API; sources disagree on the removal date. Build on JSON-2 or MCP.

## What this does not claim

- **This is a strategy,** not an integration that exists; nothing has been built or sold.
- **The policy in the figure is an illustration,** not one measured from a real Odoo database.
- **Pricing, credits and which editions include agents** come partly from integrators' summaries; I would confirm them, and the MCP server's access controls, on a real instance first.
- **Customer numbers for Odoo are third-party estimates.**

## Where this comes from

[Odoo 20 release notes](https://www.odoo.com/odoo-20-release-notes) and [Odoo 19 release notes](https://www.odoo.com/odoo-19-release-notes), read 16 November 2026; summaries of Odoo's AI features and API by [Carly](https://www.usecarly.com/blog/odoo-ai/), [Teqstars](https://teqstars.com/blog/news-6/odoo-sh-meets-ai-odoo-19-ai-features-for-developers-business-14) and [Cybrosys](https://www.cybrosys.com/blog/overview-of-api-integration-in-odoo-19); Odoo's documentation on [the legacy RPC deprecation](https://github.com/odoo/documentation/commit/ae753161cdbd11e3052d314f56cddd02bf24b1aa); the [Portuguese teacher allocation case study](https://www.casestudies.com/company/odoo/case-study/portugals-annual-school-teacher-allocation-handled-by-open-source-erp). Earlier on this site: [the intersection](the-intersection.md), [where assist becomes execute](where-assist-becomes-execute.md), [CI behaviour policies](ci-behaviour-policies.md), [the site factory works](the-site-factory-works.md), [what can your agent reach?](what-can-your-agent-reach.md), [a key for every person](a-key-for-every-person.md), [how a vault works](how-a-vault-works.md), [every story has an address](every-story-has-an-address.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#odoo-and-our-stack)

### Builds on

- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [Every story has an address: a design proposal for PrompTugal.news as a ground-up newsroom, where news is filed where it happens and climbs to the region and the country with its proof, mocked up from the live data of 19 local editions](every-story-has-an-address.md) A design proposal for PrompTugal.news as a ground-up newsroom: every story filed at an address, climbing with its proof. Mockups from live data.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 428 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=428)

**Posting this article on LinkedIn?** The cover is [odoo-and-our-stack.jpg](banners/odoo-and-our-stack.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/odoo-and-our-stack.html)*
