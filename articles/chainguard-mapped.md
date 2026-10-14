# Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in, sgit.ai

> Chainguard is one of the companies doing the most interesting work in software supply chain security, and much of it is open: the Wolfi distribution, public advisory feeds, Sigstore in its lineage, and a growing set of products for agents. So I mapped it: the company, what it builds from the operating system up to agents, what data it publishes that anyone can read, and how deep that data goes. I read the feeds and counted them. 12,480 advisories covering 12,125 distinct CVEs; in a sample, about seven in ten findings marked fixed and one in five marked as not applying. And in the archived Wolfi advisories, where the reasons were public, 2,850 determinations that a vulnerability did not apply, of which 177 gave a reason about context: the vulnerable code is not in the execution path, an attacker cannot control it, or it is mitigated. That is where the graph stops, and it is the question that matters to me. As with everything in security, it is about context. An image with many vulnerabilities is fine if the application on top never reaches them; one reachable flaw is not. Deciding which images are non-negotiable and which can ship today needs a graph from the user story, through the code and its dependencies, to the container. That context layer is where an open behaviour policy and an encrypted vault fit, next to the agent products Chainguard is now shipping, which already talk about policies. I make the case for each.

*Source: <https://newsroom.sgit.ai/articles/chainguard-mapped.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in

# Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encrypted vault could plug in

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-14 · [article v1.0.0](versions/chainguard-mapped.md) · [newsroom v0.12.47](https://newsroom.sgit.ai/admin/versions.html) · chainguardsupply-chaincontainersvulnerabilitiesvexosvcontextagent-behaviour-policysgitopen-sourceagentsarticle

***Abstract:** Chainguard is one of the companies doing the most interesting work in software supply chain security, and much of it is open: the Wolfi distribution, public advisory feeds, Sigstore in its lineage, and a growing set of products for agents. So I mapped it: the company, what it builds from the operating system up to agents, what data it publishes that anyone can read, and how deep that data goes. I read the feeds and counted them. 12,480 advisories covering 12,125 distinct CVEs; in a sample, about seven in ten findings marked fixed and one in five marked as not applying. And in the archived Wolfi advisories, where the reasons were public, 2,850 determinations that a vulnerability did not apply, of which 177 gave a reason about context: the vulnerable code is not in the execution path, an attacker cannot control it, or it is mitigated. That is where the graph stops, and it is the question that matters to me. As with everything in security, it is about context. An image with many vulnerabilities is fine if the application on top never reaches them; one reachable flaw is not. Deciding which images are non-negotiable and which can ship today needs a graph from the user story, through the code and its dependencies, to the container. That context layer is where an open behaviour policy and an encrypted vault fit, next to the agent products Chainguard is now shipping, which already talk about policies. I make the case for each.*

Chainguard, mapped. From the operating system to agents: what it builds, the public data a third party can read today, and where an open policy and an encrypted vault could add the context that decides whether an image can ship.

## In short

- **A company built in the open.** Founded in 2021 by people who worked on Sigstore, SLSA and distroless images at Google; Wolfi's build recipes are Apache 2.0.
- **From the operating system to agents.** Images, libraries, hardened CI actions, and now MCP servers, isolated workspaces, checks and a vulnerability-hunting harness for agents.
- **Its data is public, and I counted it.** 12,480 advisories over 12,125 CVEs; in a sample, 71% of findings fixed, 19% marked as not applying.
- **The graph stops at the package.** Of 2,850 recorded "does not apply" decisions, 177 give a reason about context.
- **Context decides.** A vulnerability the application never reaches can wait; one it reaches cannot.
- **The context layer is open ground.** A graph from the user story to the container, written as a policy row per image.
- **Where we plug in.** Behaviour policies for its agent products, vaults for the data between stages, and an open format for deployment decisions.

## Why Chainguard

I have written about Chainguard twice already. In [Attacks rewritten as mandates](attacks-rewritten-as-mandates.md), its record of supply chain attacks was the example, and the controls it sells would by my reading have held in most of them. In [The minimum code below](the-minimum-code-below.md) I argued that security built from the bottom up stops where the application starts. This article is the map underneath both: what the company does, what it publishes, and where others can build on it.

It matters to me as a user too. Projects like sgit ship containers, and the case for hardened base images is easy to make. What I want to understand is how far the context goes, and where it does not.

## The company

Chainguard was founded in October 2021. Its co-founders, according to [Contrary Research](https://research.contrary.com/company/chainguard), worked together on securing Google's software supply chain, including SLSA, Sigstore and one of the original distroless container images. In April 2025 it raised a $356 million Series D at a $3.5 billion valuation, as [SecurityWeek](https://www.securityweek.com/chainguard-raises-hefty-356m-series-d-at-3-5-billion-valuation/) reported. Its open-source lineage is in the products: Wolfi, the distribution its images are built from, publishes its build recipes under the Apache License; Chainguard maintains apko, melange and gitsign; and it now runs [EmeritOSS](https://www.chainguard.dev/unchained/introducing-chainguard-emeritoss), "stability-focused maintenance for select unmaintained and archived open source projects", and the [Athena](https://chainguard.dev/athena) coalition, "an industry coalition for the orchestrated defense of open source software".

## What it builds

From the bottom of the stack up:

- **Operating system and packages.** Wolfi and Chainguard OS, packages rebuilt from source, and virtual machine images.
- **Images.** Minimal, hardened container images. A free tier, [Catalog Starter](https://www.chainguard.dev/unchained/introducing-chainguard-catalog-starter), gives "Five free container images of your choice", and customers can tailor images with Custom Assembly.
- **Libraries.** Java, Python and JavaScript dependencies rebuilt from source, with Go and .NET [announced on 14 October](https://www.chainguard.dev/unchained/chainguard-libraries-expands-to-go-and-dotnet).
- **CI.** [Chainguard Actions](https://www.chainguard.dev/unchained/chainguard-actions-is-generally-available-hardening-1-000-github-actions-and-removing-transitive-ci-cd-risks), generally available since 6 October: "the Chainguard Actions catalog now spans over 1,000 continuously verified and hardened actions".
- **Agents.** This is the new part, and the most relevant here. [Agent Skills](https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills), in beta since March, is "a continuously maintained catalog of hardened AI agent skills". And four products announced on 14 October: [MCP servers](https://www.chainguard.dev/unchained/introducing-chainguard-mcp-for-secure-agentic-development) that any MCP-compatible client can reach "using a standard OAuth login", one of which "verifies organization policy, entitlements, and attestation data programmatically"; [Workspaces](https://www.chainguard.dev/unchained/introducing-chainguard-workspaces), isolated development environments for people and agents, where with an egress policy "the proxy blocks and logs any outbound request to an endpoint you haven't explicitly allowed"; [Checks](https://www.chainguard.dev/unchained/introducing-chainguard-checks), where "every run executes in a hardware-isolated microVM that produces a signed attestation of what ran"; and [Harness](https://www.chainguard.dev/unchained/introducing-chainguard-harness), which uses one of Anthropic's frontier models to "hunt down exploitable vulnerabilities".

That last group is a company moving from securing what agents install to governing what agents do. The Agent Skills announcement even names the next step: "custom best-practices configurations that let organizations define and enforce their own skill security policies".

## What it publishes

The part I care about most is the data, because data is what others can build on. I read the public feeds on 14 October 2026 and counted them.

- **An advisory feed in OSV format.** Chainguard started "publishing its security advisory feed in the Open Source Vulnerabilities (OSV) format" in 2024. The [index](https://advisories.cgr.dev/chainguard/v2/osv/all.json) lists 12,480 advisories, covering 12,125 distinct CVEs. A second index lists 1,224,077 records, one per advisory and package.
- **A status per component.** Each record names the package, the components inside it, where each sits in the image (for example a Go module inside a specific binary), and its latest status. In a random sample of 300 records, holding 377 components, 71% were fixed, 19% marked as false positives, 6% waiting for an upstream fix and 4% marked as fix not planned.
- **VEX for libraries.** An [OpenVEX index](https://libraries.cgr.dev/openvex/v1/all.json) of 732 documents: 675 for Maven, 42 for PyPI, 9 for npm and 6 for Go.
- **The reasons, until January.** The [Wolfi advisories](https://github.com/wolfi-dev/advisories) were kept in a public repository with a reason for each decision; its last change was in January 2026, it is now archived, and it points to Chainguard's security site instead.

The public records say what the status is. In the current feed, a "false positive" carries no reason. The archived repository did, and it is the best evidence of how deep the analysis goes.

## How deep the graph goes

How far up the stack the context goes. Chainguard's data describes packages and the components inside them; the decision whether an image can ship today is about the application above: is the vulnerable code reachable from what is exposed? A context layer from the user story to the code would sort each finding into must fix, ship now with a reason, and ship now and watch.

The archive holds 30,030 advisories across 1,616 packages, and 2,850 decisions that a vulnerability did not apply. Their reasons, counted:

- **1,462: the vulnerable code is not included in the package.**
- **546: the vulnerable version is not used.**
- **542: the vulnerability record does not match the component.**
- **123: the vulnerability record itself is contested.**
- **80: the vulnerable code is not in the execution path.**
- **77: the vulnerable code cannot be controlled by an adversary.**
- **20: mitigations exist inline.**

So 177 of the 2,850, about 6%, are reasons about context, and the analysis behind them can be good. For one busybox vulnerability the note says it needs a specific configuration flag: "We don't use that configuration flag, so the free logic isn't called". But that context is about how the package was built, not about the application that runs on it. The graph stops at the package.

And that is the question I care about. From a security point of view, I care about exploit paths: the vulnerabilities that can be exploited in a particular situation. If an application sits on a container with a large number of vulnerabilities, but its exposed ports and its code never reach them, that is acceptable. The reverse is also true: one reachable flaw in an otherwise clean image is not. And updating is not free. A new version, even a fix, can change the behaviour of the application, which means code changes upstream, which means CI and tests and people. So the real decision is which images are non-negotiable, must be fixed before they ship, and which are fine to deploy today.

## The context layer

That decision needs a graph that goes higher than the package: from the user story, to the exposed surface, to the code paths, to the library functions they call, to the components in the image. It is the graph [The minimum code below](the-minimum-code-below.md) proposed for removing code, and that [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) drew from the story to the method. Applied to vulnerabilities, it sorts every finding into one of three answers: must fix before it ships, because it is reachable and not mitigated; ship now with a reason, because it is present and unreachable or mitigated; and ship now and watch, because it is unreachable today and a named change would re-open it.

It is a variation of the [agent behaviour policies](footprint-and-blast-radius.md) we write, used as controls for an image instead of an agent. The mandate is what the service is for; the reach is what is exposed and what the code can call; the gap is the vulnerabilities inside that reach; and the barrier is whatever stands in front of each one: a mitigation, a configuration, the code not calling it. One row per image and finding, with its evidence, and its answer.

The format to carry the answer already exists. A VEX statement can say "not affected" with a justification, and Chainguard already publishes VEX. What is missing is the application-level justification, which only the application's owner can write, and the evidence behind it.

## Where we plug in

That is where the open work we do fits, and I think each piece makes a case for using Chainguard's platform, not for replacing any of it.

**Behaviour policies for its agent products.** Agent Skills plans to let organisations "define and enforce their own skill security policies"; the MCP servers verify organisation policy; Workspaces enforces an egress policy and keeps credentials outside the environment. Those are the barrier column of a behaviour policy, enforced as boundaries. The rows they enforce need to be written somewhere a person can read, a model can check and an auditor can point to. [A policy for every skill](a-policy-for-every-skill.md) described a control for contributed skills in exactly those terms. An open behaviour policy is a natural source for the policies these products enforce, and the signed attestations from Checks are the record of what actually ran, the footprint to compare with it.

**Vaults for the data between stages.** Advisories, VEX statements, attestations and the context decisions move between stages and teams, and some of them are sensitive: which reachable vulnerability you have not fixed yet is not something to leave in a build log. [sgit in a CI pipeline](sgit-in-a-ci-pipeline.md) showed vaults carrying data in and out of GitHub Actions, scoped to one folder per stage and encrypted per key. Hardened actions carrying encrypted vaults is a good combination.

**An open format for deployment decisions.** The three answers, with their evidence, as an open file per image and release: generated from the context graph, signed, and published as VEX where it can be. And the reasons published with every status, as Wolfi used to, because a status without a reason is a decision nobody can check.

**And for open-source projects.** I could not find a dedicated programme for open-source maintainers. When Chainguard changed its free developer tier in 2024, it told affected projects that "we would love to discuss how we can support you and your project's needs", and Catalog Starter gives five free images today. Projects like ours would like to run on its images; a clear route for open-source projects would make that easy.

## What this does not claim

- **The counts are from public data.** Read on 14 October 2026; the security site and customer data may hold more, including reasons the public feed does not carry.
- **The status shares are from a sample.** 300 random records of the 1.22 million.
- **The reason counts are from an archive.** Its last change was in January 2026; current practice may differ.
- **The context layer is a proposal.** Chainguard may be building something like it; I found nothing public that reaches the application.
- **Products are as announced.** Several are in beta; I have not used them.
- **Company history is from third parties.** Founders and funding are from Contrary Research and SecurityWeek.

If you work at Chainguard, or run its images and want the context layer above them, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

Two voice memos of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The feeds were downloaded and counted for this article the same day: the OSV indexes and a random sample of 300 records, the libraries' OpenVEX index, and a shallow clone of the archived wolfi-dev/advisories repository. Research agents gathered the company and product facts, and the quotes were checked on Chainguard's own pages. Chainguard, [Unchained](https://www.chainguard.dev/unchained) (product announcements linked above), [OSV advisory feed announcement](https://www.chainguard.dev/unchained/chainguard-enhances-security-with-osv-advisory-feed), [changes to the developer tier](https://chainguard.dev/unchained/changes-to-chainguard-images-developer-tier); Contrary Research, [Chainguard](https://research.contrary.com/company/chainguard); SecurityWeek, [Chainguard raises $356m Series D](https://www.securityweek.com/chainguard-raises-hefty-356m-series-d-at-3-5-billion-valuation/).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#chainguard-mapped)

### Builds on

- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](attacks-rewritten-as-mandates.md) 28 supply-chain attacks read as reach beyond mandate: what a hardened registry stops, what only a written mandate can, and why agents change it.
- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.

### Continued by

- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 119 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=119)

**Posting this article on LinkedIn?** The cover is [chainguard-mapped.jpg](banners/chainguard-mapped.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/chainguard-mapped.html)*
