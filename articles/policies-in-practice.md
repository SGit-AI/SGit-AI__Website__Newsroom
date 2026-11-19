# Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open, sgit.ai

> Feature behaviour policies are an idea until they are used on something real. This piece takes four. First, one of our own keys. Its reach is five Google APIs across four hosts, open to any session on its environment; the feature that uses it, the replays feed, needs one API. Only one row of that gap has a real boundary; the rest are settings and expectations. Second, the factory's CI changes: a feature policy that says create this repository, make this change and nothing else, signed, and handed to the agent that runs it, so that the agent enforces its own mandate. Third, requests that carry the signed policies they act under, so that a server, or an observer without the context, can check a call against what it was meant to do. Fourth, release notes written as bug behaviour policies, using three fixes from this newsroom's own releases today: each says what it closed, what it kept, and what it must not open. In each case the policy is the description, the permission set and the test.

*Source: <https://newsroom.sgit.ai/articles/policies-in-practice.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open

# Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/policies-in-practice.md) · [newsroom v0.14.168](https://newsroom.sgit.ai/admin/versions.html) · behaviour-policiesabpsecuritykeyscisigningrelease-notesarticle

***Abstract:** Feature behaviour policies are an idea until they are used on something real. This piece takes four. First, one of our own keys. Its reach is five Google APIs across four hosts, open to any session on its environment; the feature that uses it, the replays feed, needs one API. Only one row of that gap has a real boundary; the rest are settings and expectations. Second, the factory's CI changes: a feature policy that says create this repository, make this change and nothing else, signed, and handed to the agent that runs it, so that the agent enforces its own mandate. Third, requests that carry the signed policies they act under, so that a server, or an observer without the context, can check a call against what it was meant to do. Fourth, release notes written as bug behaviour policies, using three fixes from this newsroom's own releases today: each says what it closed, what it kept, and what it must not open. In each case the policy is the description, the permission set and the test.*

One real key: what it allows, what the replays feature uses, and the barrier on each row, typed.

## In short

- **A real key:** reach of five APIs on four hosts; the feature uses one. One row has a boundary; the rest are settings and expectations.
- **The factory's CI changes:** a signed feature policy, handed to the agent that runs it.
- **Requests that carry their policies,** so a server or an observer can check a call against its purpose.
- **Release notes as bug policies:** what each fix closed, kept and must not open.
- **In each case the policy is the description, the permission set and the test.**

This follows [feature behaviour policies](feature-behaviour-policies.md), which proposed writing a behaviour policy for every feature, fix and resource.

## The gap, measured on one real key

On the night of 18 November I set up a Google Cloud project for the PrompTugal team. Its key is restricted to five APIs: YouTube Data, Fact Check Tools, Knowledge Graph Search, PageSpeed Insights and Books. It is held as a network secret on one cloud environment, and the proxy adds it to requests for four Google hosts, so the key itself is never in a file, a page or a message. That is good practice. Now write it as a resource behaviour policy and set it beside the feature that uses it, the replays feed that data.b@ collects from the organiser's own channel.

The rows tell the story. The key's reach is five APIs; the replays feature needs one. The difference is held by a real boundary, Google's own restriction on the key. But the key is also reachable from any session on that environment, and the only thing keeping the others away is the team's rule that agents ask the conductor first: an expectation. Books is reachable too, and its terms forbid charging a fee, which rules it out on the one site that bills; that is held by the licensing register, another expectation. The paid search key has no spend cap that covers it, and Google's per-minute quotas cannot be lowered, so the limit is the caller's own code, 50 searches a run and never from CI: a setting.

None of that is a criticism. It is what the method is for: the gap is written down row by row, and each barrier is typed honestly. Only a boundary is a control. Each row that rests on a setting or an expectation is a decision someone has to make: tighten it, or accept it.

## A feature policy for the factory's CI changes

Our site factory's agents can now change CI pipelines. In [CI behaviour policies](ci-behaviour-policies.md) I wrote that the factory's pipeline, to create one repository and one DNS record per request, holds a token that can create, change or delete every repository in the organisation. Letting agents change that pipeline is exactly the kind of capability that needs a feature policy before it is used widely. Written out, it is short:

- **For:** create this repository, or make this named change to this pipeline.
- **Reads:** the repository it is changing, and the template it starts from.
- **Writes:** that repository's workflow files, on a branch, never anywhere else.
- **Never:** add a secret, widen a permission, or change another repository's pipeline.
- **Signed** by the person or agent who approved the change, and **handed to the agent that runs it.**

The agent then enforces its own mandate: before it pushes, it checks its diff against the policy, and refuses what is outside it. The same policy is what a reviewer reads to approve the change, and what a test checks afterwards. It is the description, the permission set and the test, in one file.

## Requests that carry their policies

The next step is for a request to carry the signed policy, or policies, it is acting under. The client sends only what its feature's policy allows, which already cuts the noise the server sees. The server checks the call against the policy it carries. And an observer without the whole context, a gateway or a monitoring agent, can still look at a request and its policy and ask whether the one fits the other.

We already have the pieces for the signing. This newsroom's writer signs every commit with its registered key, and the check that verifies it runs in CI before anything is released. A policy is a smaller thing to sign than a commit. What it adds is that a bug or an attack becomes visible as what it is: a call outside the policy that came with it.

## Release notes as bug behaviour policies

A fix is a change of behaviour, so it can be described as one: the path it closes, what it keeps as it was, and what it must not open. Three fixes from this newsroom's own releases today, written that way:

- **The signature check.** *Closes:* a commit adding the key it is signed with, and a writer's merge commit slipping past. *Keeps:* the writer's existing tree signature. *Must not open:* any exemption by name or subject; commits that are not the writer's are listed as warnings, not passed silently.
- **A page too wide for a phone.** *Closes:* a repository name too long to wrap, which made one article 400 pixels wide on a 390-pixel screen. *Keeps:* the link to the repository, now as link text. *Must not open:* any article wider than the screen, which the release gate checks.
- **The front page's lists.** *Closes:* taps landing on the section label instead of the article. *Keeps:* the label, as a smaller link to its section. *Must not open:* a list where the label competes with the title.

Read this way, a release note is a set of small policies, and each one is a test: the path it closed should stay closed.

## What this does not claim

- **The key's rows are read from the team's own brief and register** of 19 November 2026; they describe the set-up, not a test of Google's enforcement.
- **The factory policy is a proposal,** written for the capability as I have described it; it is not yet in use.
- **Requests carrying signed policies are not built;** the signing of commits is.

## Where this comes from

PrompTugal__News__Website on its dev branch, read on 19 November 2026: `board/briefs/2026-11-19-google-cloud-apis.md` (the keys, hosts and controls) and `board/team/rights/findings.md` (R6, R7). This newsroom's notes on signed commits, `admin/notes/2026-11-19__signed-commits/notes.md`, and its releases of 19 November. Earlier: [feature behaviour policies](feature-behaviour-policies.md), [CI behaviour policies](ci-behaviour-policies.md), [application behaviour policies](application-behaviour-policies.md), [a page we never charge](a-page-we-never-charge.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#policies-in-practice)

### Builds on

- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.
- [Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius](application-behaviour-policies.md) Map an application the way we map an agent, so a site switched off for php2shell can come back with a known blast radius.
- [A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits](a-page-we-never-charge.md) YouTube forbids charging to watch an embedded player, so promptugal.news, which bills, will show the replays on a page it never charges.

### Continued by

- [Your own registrar: which domain registrar to recommend to a small business in Europe taking its website's domain into its own name, sixteen compared on price and renewal, .eu, .pt and .ai, privacy, and APIs safe enough to hand to an agent, why AWS now sells .ai but is still a heavy choice, and the three we would put forward](your-own-registrar.md) Which registrar a small business in Europe should hold its own domain at: sixteen compared, and OVHcloud, Hostinger and INWX.
- [The second run: a forensic look at why a release of this newsroom takes about 24 minutes, measured stage by stage over two timed releases and 437 CI runs since 18 October, what each check protects, what runs twice, what can run side by side, and why, if nothing changed, the second run should do almost no work at all](the-second-run.md) Why a release takes 24 minutes, measured stage by stage, and why a second run with nothing changed should do almost no work.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 491 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=491)

**Posting this article on LinkedIn?** The cover is [policies-in-practice.jpg](banners/policies-in-practice.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/policies-in-practice.html)*
