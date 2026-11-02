---
title: False positives and the harness: an answer to a question at hack::soho, why a behaviour policy that runs from the network up to the business logic should refuse less of what is right and more of what is wrong, and why a policy that changes with the code becomes a calibrator for bugs
date: 2026-11-02
author: Dinis Cruz
author_url: about/index.html
summary: After my talk at hack::soho, one of the attendees asked a good question: what are the false positive rates of SHarness, the secure harness that enforces behaviour policies at a low level? There is no measured rate yet; most of SHarness is a design, and its site says so. But the design is built in a way that should handle false positives well, and this is why. A low-level control refuses things without knowing what the application is for, which is where false positives come from. SHarness's policies can be layered, from the network, to the database, to one application's tables and fields, each narrower than the one above, until the policy describes how the application actually behaves: this field, only positive, only in this range. That is the same move as Type_Safe in our Python code, where checking values at the gate let us delete defensive code in the wrong places. A policy that knows the business refuses less of what is right and catches more of what is wrong. It can learn: a gap found in testing is a row added. And if a CI pipeline updates the policy whenever the code changes, the policy becomes a calibrator: a change that moves the policy when you did not expect it, or does not when you did, is a bug.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sharness, false-positives, process-behaviour-policies, behaviour-policies, type-safe, ci, databases, security, article
status: published
---

!shot fph-layers.webp | images/ | One policy, layered: each door narrower than the one above, until the last one knows the business. | architecture

## In short {#in-short}

- **The question:** what are SHarness's false positive rates?
- **The honest answer:** there is no measured rate; most of SHarness is a design.
- **Why the design should do well:** false positives come from controls that do not know what the application is for.
- **Layer the policy,** from the network to the database to one application's fields, until it describes how the application behaves.
- **Like Type_Safe:** check at the gate, and the defensive code in the wrong places goes away.
- **It learns:** a gap found in testing or in use becomes a row.
- **Tie it to CI,** and an unexpected policy change, or a missing one, is a bug.
- **The line is known:** what the policy cannot say, the application checks, and the policy says so.

## The question {#question}

I gave a talk at [hack::soho](https://www.ioactive.com/event/hacksoho-july-2025-ai-agents-blast-radius-and-the-mcp-horror-story-dinis-cruz-london-uk/), IOActive's monthly event in London, and one of the attendees asked about [SHarness](/articles/introducing-sharness.html), the secure harness that runs an agent's processes under behaviour policies the Linux kernel enforces. Controls that work at a low level have a reputation: they block things that should be allowed. So what is the false positive rate?

First, the honest part. There is no rate to give. The sharness.ai site never claims one, and it is clear about how much is built: its policy page says "No SHarness component is built", and that the v0 policy, its hash and the hello command "are the only runnable parts". What follows is why I think the design will handle false positives well, and what would show that I am wrong.

## Where false positives come from {#where}

A false positive is a control refusing something it should have allowed. Google's static analysis teams defined the version that matters, the effective false positive: "any report from the tool where a user chooses not to take action to resolve the report". Their rule for checks shown in code review was "less than 10% effective false positives", and they dropped a tool when "the presence of effective false positives caused developers to lose confidence in the tool".

In security operations it is worse. A USENIX Security 2022 study of analysts who reported false positive rates as high as 99% found that most were "benign triggers", true alarms "explained by legitimate behavior in the organization's environment". In other words, the control saw something real, but it did not know the business, so it could not tell normal from wrong.

That is the core of it. A control that only knows ports and paths refuses without knowing what the application is for. The fix is not a smarter guess. It is giving the control the business context.

## A policy in layers {#layers}

This is where SHarness's design differs from most low-level tools. A policy is not one wall. It is a chain of doors, each a separate process with its own policy, named as a tree, `sharness.<door>.<target>`, and each door can only narrow what the one above allows.

Take an application that edits orders in a database:

1. **The network door** allows only TCP to the database host and port. Nothing else leaves the process.
2. **The database door** allows only that database, with that application's credentials.
3. **The tables and operations:** only the orders table, only select and update, never delete.
4. **The application's rules:** only the quantity and status fields; quantity a positive number, within a range; status only from one value to the next.

The first layer knows nothing about orders. The last one describes how the application behaves. SHarness's behaviour rows are made for that last step: its design lists "this field within this range, never negative", "append only", "content valid against this schema", count and rate per interval, ordering, and fresh approval.

Two details from the design keep this honest. A door should "never parse SQL or Cypher": either the application sends structured requests (this table, these columns, this filter) and the door holds the rows, or the database enforces them itself, with Postgres row-level security or a CHECK constraint such as `price > 0`, and the door only checks that configuration against the policy's hash. And a row only counts if there is no way around it: "A behaviour row is a Boundary only when the subject has no path to the resource except through the door that holds the row."

## The same move as Type_Safe {#type-safe}

We did this before, in our own Python code. [Type_Safe](https://github.com/owasp-sbot/OSBot-Utils), in OSBot-Utils, checks types on every assignment, with primitives such as `Safe_Str` and `Safe_Int` that carry their own rules; a `Safe_Int__Positive` has a minimum of 1. When we started to trust it, the code got simpler. A lot of validation and defensive checks, often in the wrong place, could go, because the value had already been checked at the gate.

A behaviour policy is the same idea one level out. The checks that every function was doing defensively, is this number positive, is this field allowed, can live in the policy, once, enforced by something the application cannot change. The application gets simpler, and the policy becomes the place where the business rules are written down.

## False negatives too {#negatives}

The same layering catches more of what is wrong. A network rule cannot see that a quantity went negative, or that a status jumped from new to refunded. A row that knows the business can. The more of the application's behaviour the policy mirrors, the narrower the space where a bad action looks normal.

## A policy that learns {#learns}

Policies are not written once. In testing, and in real use, you will find gaps: a legitimate action refused, or a wrong one allowed. Each is a row to add or change. SHarness's design makes a refusal cheap, "A refusal is nothing, not damage": the action does not happen, the agent gets an error and says so, and there is an audit line. When a person approves a refused action, the design writes it into the policy as a row, "monitor mode with a person in it".

There is a known risk, and the older tools name it. SELinux's audit2allow, which turns denials into rules, warns against "blindly implementing the sometimes broad changes recommended by this utility". SHarness has already met it once: a learned policy trimmed by hand "dropped a path the run needs, and the run then failed with an unhelpful error rather than a clear refusal". That is a false positive, caused by editing, and the design's rule since then is that a learned policy is generated from every successful run and never trimmed by hand.

## The policy as a calibrator {#calibrator}

!shot fph-ci.webp | images/ | Tie the policy to the code: CI derives it on every change, and a surprise in either direction is a bug. | process

Writing policies used to be too much work to keep up. Not any more. A CI pipeline can derive the policy from the test suite on every change, diff it against the last release, and fail when the footprint grows without a matching policy change. That is in SHarness's design: the pipeline runs each subcommand's tests under trace, drafts the policy, puts it through human review, and "CI fails if footprint grows without a matching policy change".

That turns the policy into a calibrator for the code:

- **A change that moves the policy when you did not expect it** means the code does something new. You changed a report, and suddenly the policy wants write access to the orders table. That is a bug, or a design change nobody decided.
- **A change that does not move the policy when you expected it** is also a bug. You added a feature that should touch a new table, and the footprint is unchanged: the feature is not doing what you think.

Either way, the policy tells you whether the system behaves the way you expect, and whether your changes had the effect you meant.

## Where to draw the line {#line}

How far do you go? In principle, all the way to the application's behaviour. In practice, SHarness keeps the row language small on purpose: "A policy that can express arbitrary logic is code, and code in the policy is a rules engine in the trusted path." A rule the language cannot say becomes a door of its own, under its own policy, or it stays in the application.

That is not a weakness. It is a known boundary. You know which rules the policy holds and which the application holds, and a level of the design "never hides what it cannot hold: it reports the unheld rows in its own nouns". The question is no longer whether there are blind spots, but where they are, and that you can write down.

## Where it sits {#fits}

SHarness's process behaviour policies sit below the agent behaviour policies, which describe what an agent may do at a high level. Beside them are the decision and workflow policies, who chooses and in what order, which I mapped in [three policies for an agent](/articles/three-policies-for-an-agent.html). Together they run from the kernel to the business: the lowest layer refuses a connection, the highest refuses a decision, and every layer in between can only narrow.

## What this does not claim {#limits}

- **There is no measured false positive rate** for SHarness; this is an argument from the design.
- **Most of SHarness is proposed:** behaviour rows, doors, the layering and the CI pipeline are designs, not running code.
- **The order example is illustrative,** not a deployed policy.
- **Type_Safe's effect on our code** is our own experience, not a measurement.
- **Learned policies can bake in bad behaviour;** human review is part of the design for that reason.

## Where this comes from {#sources}

My answer to a question at hack::soho, in this site's repository under `admin/notes/2026-11-02__sharness-false-positives/`. SHarness: [Process Behaviour Policies](https://sharness.ai/design/pbp/index.html), [the policies pipeline](https://sharness.ai/design/policies/index.html), [the decision at the door](https://sharness.ai/design/decision/index.html), [the levels](https://sharness.ai/design/levels/index.html), [the architecture](https://sharness.ai/design/architecture/index.html). [OSBot-Utils and Type_Safe](https://github.com/owasp-sbot/OSBot-Utils). Google: [Tricorder (ICSE 2015)](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43322.pdf) and [Lessons from building static analysis tools at Google (CACM 2018)](https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf). [Alahmadi et al., USENIX Security 2022](https://www.usenix.org/system/files/sec22-alahmadi.pdf). PostgreSQL: [row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). [Security Profiles Operator recording](https://github.com/kubernetes-sigs/security-profiles-operator/blob/main/doc/recording.md); audit2allow(1). [IOActive on hack::soho](https://www.ioactive.com/event/hacksoho-july-2025-ai-agents-blast-radius-and-the-mcp-horror-story-dinis-cruz-london-uk/). All read 2 November 2026.
