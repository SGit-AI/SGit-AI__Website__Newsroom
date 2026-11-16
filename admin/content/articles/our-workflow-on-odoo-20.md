---
title: Our workflow on Odoo 20, built and measured: a bills agent with no Odoo credential, a policy check that allowed two proposals and stopped three, a signed approval, a narrow broker, a grant measured from Odoo itself by a new module, and what Odoo's default user role quietly allows
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: I asked a separate agent, odoo@AgentiCCells.dinis, to build an MVP of our workflow on Odoo and to map our Agent Behaviour Policies onto it. It did, end to end, on the official Odoo 20 image, in 98 seconds from nothing to teardown. A bills agent read four supplier PDFs and, holding no Odoo credential at all, proposed five operations. A policy check, written from its behaviour policy, allowed two draft bills, refused the creation of a new supplier, held that supplier's bill, and escalated one above the limit. An approval, simulated in this MVP and clearly labelled, signed the allowed operations; a broker verified the signature and created exactly two draft bills through Odoo's JSON-2 API, as a narrow user, with the source PDFs attached and an Agent provenance tab on each. Every step was committed to a vault. The agent then measured the broker's grant from Odoo itself, with 25 live probes and a new module, abp_grant, that turns Odoo's access rules into behaviour policy rows. The findings matter. A create-only grant is impossible in Odoo; posting is refused by Odoo's own code, a real boundary; but Odoo's default user role lets even a narrow integration user edit a draft after approval, read supplier bank accounts and email the supplier through the chatter. Odoo's own agents and MCP server are Enterprise-only, and agents triggered automatically write without asking. The same scripts ran on Odoo 19 and 17.
version: v0.14.122
license: https://creativecommons.org/licenses/by/4.0/
tags: odoo, abp, agents, erp, mvp, riskmandate, agenticcells, vaults, article
status: published
---

!shot odm-flow.webp | images/ | Our workflow on Odoo 20: the agent never touches Odoo; a check, an approval and a broker stand between. | process

## In short {#in-short}

- **Built, not described:** our workflow on Odoo 20, in 98 seconds from nothing to teardown.
- **The agent holds no Odoo credential:** it reads PDFs and writes a plan; a policy check, a signed approval and a narrow broker do the rest.
- **Five proposals, four verdicts:** two drafts allowed and applied; one refused, one held, one escalated.
- **The grant, measured from Odoo** by 25 probes and a new module, abp_grant.
- **The surprise:** Odoo's default user role lets a narrow integration user email the supplier and read bank accounts.
- **Odoo's own agents and MCP are Enterprise-only;** agents triggered automatically write without asking.

## What was built {#built}

In [Odoo and our stack](/articles/odoo-and-our-stack.html) I mapped how our workflow fits around Odoo, and an agent in this session brought Odoo 12 to 19 up in under a minute each. Then I asked a separate agent, odoo@AgentiCCells.dinis, in its own session, to build a real MVP and to map our behaviour policies onto it, so that the newsroom could stay focused on writing ([specialist agents for every team](/articles/specialist-agents-for-every-team.html)). Its report came back this afternoon.

It built on the official `odoo:20.0` image, published on 12 November. A clean run brings up Odoo with CRM and Invoicing, sets up a narrow integration user, runs the bills agent through plan, check, approval and broker, measures the grant and tears everything down: 98 seconds, of which 75 are Odoo installing itself. The plan-then-apply steps add about four seconds per batch, half of it vault commits.

The shape is the one we use for anything that writes to a system of record ([CI behaviour policies](/articles/ci-behaviour-policies.html)):

- **The agent** reads the supplier PDFs and a snapshot of the records it may see, and writes a plan. It holds no Odoo credential, so it cannot change anything in Odoo, whatever it is told.
- **The policy check** compares each operation with the agent's behaviour policy: vendor bills only, existing suppliers only, no state set, no duplicate reference, at most 5,000 per bill.
- **The approval** is signed over the plan and the check. In this MVP it was simulated by a script with its own key, and it says so everywhere: in the vault, on the bill and on the review page. No person approved anything.
- **The broker** verifies the signature, re-applies its own allowlist, creates the approved bills through Odoo's JSON-2 API as a narrow user, attaches the source PDF, reads each bill back, and writes the result.

It also added a better interface on top of Odoo, the kind of prototype I said Odoo is good for ([integrate with whatever is on the other side](/articles/integrate-with-whatever-is-on-the-other-side.html)): an "Agent drafts" menu and list, an "Agent provenance" tab on each bill with the plan, the approval and the source document's hash, and a review page an approver would sign from.

## Five proposals, four verdicts {#results}

!shot odm-results.webp | images/ | Five proposals, four verdicts: two drafts allowed and applied, a new supplier refused, one held, one escalated. | table

Four supplier PDFs went in, and the agent proposed five operations. It was written to be slightly over-eager on purpose: for an unknown supplier, it proposed creating one, so that the check, not the agent's manners, had to stop it. Two draft bills were allowed, approved and applied, and stayed drafts, with totals matching to the penny. The new supplier was refused, because it is not in the mandate; its bill was held; and a bill of 8,970 was escalated, above the limit. Only the two approved operations reached Odoo.

## The grant, measured from Odoo {#grant}

!shot odm-gap.webp | images/ | The grant measured from Odoo: the mandate, what Odoo refuses, and the excess its default user role allows. | comparison

The second half of the job was the behaviour policy ([Agent Behaviour Policies](https://abp.sgit.ai/)). The mandate was written by hand: read supplier documents, propose draft vendor bills for existing suppliers, and never post, pay, email, create a supplier or touch anything else. The grant was measured, from Odoo, in two ways: 25 live probes, each recorded as observed, and a static read of the 172 models the broker's user can reach.

The split between the two holders is the point. The agent holds no Odoo key, so every Odoo barrier it faces is a boundary, enforced outside its reach. The broker's user is narrow, but the findings are worth knowing for anyone connecting agents to Odoo:

- **A create-only grant is impossible.** Odoo will not create a bill with lines unless the user can also update journal items, so the narrowest workable grant is create, read and update on draft vendor bills. Editing a draft after approval is therefore in the grant; only the broker's allowlist and the signed hashes stop it.
- **Posting is refused by Odoo's own code,** because it needs the accounting group. That is a real boundary, and one a reader that looks only at access rows would miss.
- **Odoo's default user role brings a lot.** Even this narrow user could read every supplier bank account, create attachments, templates and scheduled messages, and email the supplier by posting on the bill's chatter: the probe queued a real email, which failed only because the test instance had no mail server. On a production instance, that is a send to the world with no barrier at all.
- **It cannot widen itself.** Adding itself to an accounting group, creating keys, scheduled jobs, server actions and system parameters were all refused.

The fix is clear: keep the agent keyless; narrow the broker's user further, or restrict mail and bank accounts for it; re-read every bill after apply; and check approved drafts every night until a person posts them.

## A module that measures the grant {#module}

In the earlier article I said the strongest product idea was a module that writes the grant section of a policy from Odoo itself. The agent built it. `abp_grant` installs on Odoo 20 in 3.8 seconds and measures a user in a tenth of a second. It reads what Odoo actually enforces, adds the code-level cases such as posting, lists the user's API keys by name and scope only, and turns all of it into behaviour policy rows, each with its undo class and barrier. It also applies the enforcer test automatically: if the user can change its own access, no denial counts as a boundary ([where assist becomes execute](/articles/where-assist-becomes-execute.html)). Its rows agreed with the live probes.

It also found a gap in our grammar: reading, creating, writing and deleting records in a tenant's system of record are not yet among the published capabilities. The agent proposes them, with its probe as the evidence.

## What Odoo itself does {#native}

Some of what the earlier article leaned on turned out to be Enterprise-only: Odoo's agents, its MCP server, Documents and full Accounting are not in the Community edition, so the MVP used Community Invoicing and an inbox folder, and Odoo's own agents were described from Odoo's documentation, not run. Three points from that documentation matter for policies:

- **Agents triggered automatically act without asking:** Odoo says they "perform their tasks directly, without requesting user approval before creating or updating records".
- **An agent's tools are server actions,** which can run any code, so an agent's grant is the user it runs as plus whatever its tools' code does.
- **MCP control is per tool, not per model,** and a tool marked read-only only advises the client.

Odoo 20 also replaced its access rules with a single new model, moved the legacy APIs into an add-on scheduled for removal in Odoo 22, in autumn 2028, and charges credits, at a euro each, for all AI features.

## Every version {#versions}

The same scripts ran on Odoo 19, through JSON-2, in 91 seconds, and on Odoo 17, through XML-RPC with an API key, in 68. On 17 the test database had no suppliers, and the policy check failed safe: every bill was refused or held rather than inventing a supplier. With the suppliers added, 17 gave the same result as 20. It took six small version branches to run one workflow on three versions, which is the argument for putting version differences in the broker, not in the agent.

## What comes next {#next}

1. **Replace the simulated approval** with a real signature by a named person, on the review page ([a key for every person](/articles/a-key-for-every-person.html)).
2. **Close the excess:** a narrower group for the broker's user, re-measured with the module; a re-read after apply; a nightly drift check.
3. **Measure Odoo's own agents and MCP server** on an Enterprise trial, with the same probe and module.
4. **Propose the record capabilities to abp.sgit.ai,** with the probe as evidence.
5. **Turn the module into a product:** per agent and per MCP key, a measured grant, a stored mandate and the gap shown inside Odoo.

## What this does not claim {#limits}

- **The approval was simulated.** No person approved anything.
- **Odoo's own agents and MCP server were not run;** they are Enterprise-only, and what is said of them comes from Odoo's documentation.
- **No email was delivered;** the queued message proves the capability, not delivery.
- **The agent's extraction was rule-based by design;** what was under test was the governance path, not reading PDFs.

## Where this comes from {#sources}

The report of odoo@AgentiCCells.dinis, 16 November 2026, from its own session: its scripts, runs, probes and screenshots, built on the official [odoo:20.0](https://hub.docker.com/_/odoo) image and Odoo's documentation, including the [Odoo 20 release notes](https://www.odoo.com/odoo-20-release-notes). Earlier on this site: [Odoo and our stack](/articles/odoo-and-our-stack.html), [integrate with whatever is on the other side](/articles/integrate-with-whatever-is-on-the-other-side.html), [specialist agents for every team](/articles/specialist-agents-for-every-team.html), [CI behaviour policies](/articles/ci-behaviour-policies.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [a key for every person](/articles/a-key-for-every-person.html).
