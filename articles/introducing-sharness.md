# SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback, sgit.ai

> For a long time we have said that an agent's rules need a secure harness that sits outside the agent's own environment, outside RiskMandate's and outside the hook. We looked for one and did not find it, so I sat down with a few Claude agents and we built it, and it is now released, at sharness.ai, with sharness-ai 0.2.0 on PyPI. SHarness is what our Agent Behaviour Policies become when they are executed rather than read. An Agent Behaviour Policy describes what an agent is mandated to do, what it can actually reach, the gap between the two, and what stands in the way of each capability. A Process Behaviour Policy applies the same model to every process the agent starts: what it may read, write, run, connect to and spend, written as a small policy, hashed to one name the person supplies from outside, and enforced by something the process does not include, the Linux kernel or a small separate service. A tricked agent cannot widen it, because the kernel was told before the process started. That turns Settings and Expectations into Boundaries, which is the only kind of control an insurer can price, and it puts the permission prompt last: yes to what the policy allows, silence for what it refuses, and a question only for what it cannot hold. The design is a launcher and five doors, files, network, keys, shell and model, each a small service with its own user and its own certificate, and the same policy can be written for bubblewrap, Docker, Kubernetes or Claude Code's sandbox, with the list of what each cannot hold. Today the kernel locks run, two doors run as early versions, and a real Linux kernel boots in a browser tab and refuses what the policy refuses; the launcher that binds the agent itself is still the design. It is open source, and what I would most like now is feedback.

*Source: <https://newsroom.sgit.ai/articles/introducing-sharness.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback

# SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-29 · [article v1.0.0](versions/introducing-sharness.md) · [newsroom v0.13.131](https://newsroom.sgit.ai/admin/versions.html) · sharnessbehaviour-policiesagent-behaviour-policyprocess-behaviour-policylinuxlandlocksecurityagentsopen-sourcearticle

***Abstract:** For a long time we have said that an agent's rules need a secure harness that sits outside the agent's own environment, outside RiskMandate's and outside the hook. We looked for one and did not find it, so I sat down with a few Claude agents and we built it, and it is now released, at sharness.ai, with sharness-ai 0.2.0 on PyPI. SHarness is what our Agent Behaviour Policies become when they are executed rather than read. An Agent Behaviour Policy describes what an agent is mandated to do, what it can actually reach, the gap between the two, and what stands in the way of each capability. A Process Behaviour Policy applies the same model to every process the agent starts: what it may read, write, run, connect to and spend, written as a small policy, hashed to one name the person supplies from outside, and enforced by something the process does not include, the Linux kernel or a small separate service. A tricked agent cannot widen it, because the kernel was told before the process started. That turns Settings and Expectations into Boundaries, which is the only kind of control an insurer can price, and it puts the permission prompt last: yes to what the policy allows, silence for what it refuses, and a question only for what it cannot hold. The design is a launcher and five doors, files, network, keys, shell and model, each a small service with its own user and its own certificate, and the same policy can be written for bubblewrap, Docker, Kubernetes or Claude Code's sandbox, with the list of what each cannot hold. Today the kernel locks run, two doors run as early versions, and a real Linux kernel boots in a browser tab and refuses what the policy refuses; the launcher that binds the agent itself is still the design. It is open source, and what I would most like now is feedback.*

From a policy the agent reads to a policy the kernel holds: four kinds of barrier, three things that bind.

## In short

- **We needed a secure harness outside the agent, and could not find one.** So we built it: [sharness.ai](https://sharness.ai/), and `sharness-ai` 0.2.0 on [PyPI](https://pypi.org/project/sharness-ai/), released on 29 October 2026.
- **It is our behaviour policies, executed.** An Agent Behaviour Policy describes an agent; a Process Behaviour Policy is enforced underneath it, on every process it starts.
- **Three things make a policy binding.** The text, its hash supplied by the person from outside, and an enforcer the agent does not include.
- **That is the business case.** Only an enforced control is a Boundary, and only a Boundary is something an insurer, an auditor or a board can count.
- **The prompt goes last.** Yes to what the policy allows, silence for what it refuses, a question only for what it cannot hold.
- **One policy, many enforcers.** The same file can be written for bubblewrap, Docker, Kubernetes or Claude Code's sandbox, with what each cannot hold.
- **The architecture is a launcher and five doors.** Files, network, keys, shell and model, each a small service with its own user, policy and certificate.
- **It runs today, in part.** The kernel locks, two doors, the levels, and a Linux kernel in a browser tab that held six of six.
- **What does not run yet is said plainly.** The launcher that binds the agent itself is the design.
- **We would like your feedback.** Run `hello`, read the design, tell us what is wrong.

## Why we built it

For months, every time we talked about agent behaviour policies, the same point came back: a policy the agent reads is only as strong as the agent's willingness to keep it. We need a secure harness that sits outside the agent's environment, outside RiskMandate's environment and outside the hook. We have measured how far we are from that on our own agents. When this newsroom's writer took its own eleven rules and tried to move them into hooks, in [are hooks the sweet spot?](are-hooks-the-sweet-spot.md), only one was kept by something other than the agent. When it took apart the 57 checks its releases pass, in [behaviour policies from the checks](behaviour-policies-from-the-checks.md), 22 were expectations, 34 were settings and one was a boundary. And [hooks are kernel code](hooks-are-kernel-code.md) put the last level of its maturity model "off the machine": the rule kept by something the agent's machine does not control.

So we looked for that something. There is a lot of good work in this space, and sharness.ai's own [market analysis](https://sharness.ai/landscape/market/index.html) surveys it: sandboxes and microVMs, shell sandboxes in the coding agents, MCP gateways, LLM gateways, secret brokers, guardrails, enterprise platforms. What we did not find was the piece we kept asking for: a policy written once, hashed, supplied by the person, and enforced on every process the agent starts by something the agent cannot switch off. The site's [enforceability matrix](https://sharness.ai/landscape/enforceability/index.html) says it in one line: "The column no product fills is 'who enforces': in every shell sandbox the agent's own process reads the settings."

After not finding one, I took the time, sat down with a couple of Claude agents for a really productive session, and we built one. It started on the morning of 24 October 2026 with a narrow problem in sgit, and five days later it is a website, a design, a security register, an open source CLI on PyPI and a team of agents that keeps all of it moving. I think it is a super powerful capability, and this article is its introduction: the strategy first, then what it does and the many ways it works, then the architecture, getting more technical as it goes.

## What SHarness is, in one paragraph

SHarness runs an agent and its tools as small, single-purpose processes, each locked down by the kernel and talking to the others only over allowed, mutually authenticated connections. Each process runs under a Process Behaviour Policy: what it may read, write, run and connect to, named by one hash the person supplies and enforced by the Linux kernel. In the site's own words, "A tricked agent cannot widen it, because the kernel was told before the process started." A secret lives in one place, a key service that never hands out a clear key, and a tricked process can only do its one job. The name is the idea: a **s**ecure **harness**, the layer agents run inside so that they can run securely. (It is unrelated to Sharness, the shell testing library.)

## From Agent Behaviour Policies to Process Behaviour Policies

SHarness is the natural next step from the work we have done on [Agent Behaviour Policies](https://riskmandate.ai/abp.html). An Agent Behaviour Policy, an ABP, is a description in four objects: the **mandate** (what the business asked the agent to do), the **grant** (what it can actually reach), the **delta** (the reach nobody asked for) and the **barrier** on each capability (what stands in its way). The barrier comes in four kinds: **None**; an **Expectation**, which is prose the agent reads; a **Setting**, which the subject could flip; and a **Boundary**, enforced from above the subject. Most of what stands in the way of an agent today is the agent itself, reading its instructions and choosing to follow them.

A [Process Behaviour Policy](https://sharness.ai/design/pbp/index.html), a PBP, is "the Agent Behaviour Policy model applied to one process": the same four objects, with the mandate written as rows for one process and the grant measured by probing what that process can do before any policy. The site's one-line distinction is the one I would keep: "An ABP *describes* an agent's behaviour; a PBP is that description *executed*, underneath the agent." This newsroom first built one in [process behaviour policies](process-behaviour-policies.md), the most locked-down process we could make inside Claude's own cloud container, and measured it; SHarness is that idea grown into a harness.

Three things make a PBP binding, and if one is lost, it is an ABP again, a policy the subject reads:

1. **The text.** A small JSON object in canonical form (sorted keys, no whitespace, integers only), so the same policy hashes the same in every language. It was measured identical in Python, in the browser and in a Linux guest on 25 October 2026.
2. **The hash, from outside.** The person supplies `sha256:…`, and the enforcer refuses anything else. "A prompt-injected agent cannot widen what it cannot rename."
3. **An enforcer the subject does not include.** The kernel, or a separate process. "Who enforces decides the barrier kind": a policy a process applies to its own child is a Boundary for the child and only a Setting for the process.

That last rule is the one SHarness never lets go of. Every result it prints says which kind of barrier it was, including the uncomfortable cases. It is why the site says, on every page that matters, that the launcher which binds the agent itself is still the design.

## Why this matters to a business

Strategically, the point is not a better sandbox. It is that a behaviour policy can now be held, row by row, by something that is not the agent, and that changes what the policy is worth.

**Only an enforced control counts.** In the insuring agents series I argued, in [a payout for every row](a-payout-for-every-row.md), that an agent behaviour policy can be read as an insurance policy, and that "A line in the prompt earns nothing": only a control that something enforces lowers a row's premium. SHarness is how a row moves from Expectation to Boundary. A policy that says "this agent writes only to this workspace and talks only to these hosts", held by the kernel and a network door, is a row an underwriter can price, an auditor can check and a board can be told about.

**Two numbers in every summary.** The ABP's number is unbounded excess, the reach nobody asked for and nothing bounds. A PBP adds a second: unheld rows, the mandate rows no Boundary holds. A policy never claims a row is held when nothing holds it; the rows no door holds in a given deployment stay in the policy as Expectations, counted. The site puts it well: "The second number is the business case for the next door."

**The permission prompt goes last.** The prompts coding agents show today are, in ABP terms, Settings: the agent's own process asks the agent's own user, and the same account can turn them off. ux.sgit.ai's finding [UX-059](https://ux.sgit.ai/findings/UX-059.html) shows they fail as decisions too, and that repeated prompts teach people to press Allow without reading. SHarness's [decision at the door](https://sharness.ai/design/decision/index.html) moves the decision to launch, in the person's own nouns (this workspace, these sites, these secrets), made once and hashed. After that: "yes to what the policy allows, silence for what it refuses, and a question only for what it cannot hold." An approved question becomes a learned row, so the policy grows from the approvals people actually give.

**The enterprise story has no product in the request path.** A policy can be written at several levels, from a sentence down to the kernel (below). The vendor ships the profiles with its tool, the organisation runs the step that names its own proxies, databases and twins, and the laptop runs the step down to its kernel. Because levels compose by intersection, a developer cannot name a target the organisation does not offer. And it costs nothing per request: the expansion runs once, at launch.

**And the cloud providers could run it.** The real power comes when some of these components run as a service, outside the machine the agent is on. The design's last [deployment topology](https://sharness.ai/design/architecture/index.html) is the platform providing the key service and the session identity, with no key in the container at all. It is the same ask as in [agents have an identity now](agents-have-an-identity-now.md): today no such service is known to exist, and it is a small thing for a provider to offer.

## The many ways it works

This is where SHarness differs most from a product. The site's [landscape](https://sharness.ai/landscape/index.html) starts from one position: at the heart of all this are the behaviour policies, and SHarness is a **reference implementation** of Process Behaviour Policies, "small enough to read in one sitting". Any environment that can enforce the same rows is a valid enforcer, so the other products are "less competitors than integration points". The question to ask of each one is not whether it competes, but "which rows of a policy can it enforce, natively, and how do I translate the policy into its form?"

That question is a command. `sharness-ai policy translate` writes the same policy as a bubblewrap command line, a `docker run`, a Claude Code sandbox `settings.json` fragment, or a Kubernetes Pod and NetworkPolicy, and ends every output with the list of what that target does not enforce. The matrix behind it is honest in both directions. Writes, no network, no new privileges and memory caps run almost anywhere. An execute allowlist, TCP port rules without a proxy, roles on the connections between processes, the secret in a process the agent cannot reach, and a hash checked above the subject are the rows only SHarness holds today, and they are the reason it exists.

The second way it works is by levels, because the full policy schema is more than most people will ever write.

The levels: one policy written as a sentence, a profile, plain rows, doors or mechanisms, each compiling into the next.

You write at the level you need. At the top, a sentence with blanks: "contain my agent to *this workspace*, *these sites*, *these secrets*". `sharness-ai contain --workspace . --sites github.com -- CMD` takes that sentence, compiles it down to the policy the kernel holds, prints what it became at each level with one hash, and runs the command under it. "A simpler level is never a weaker one": the person supplies the hash of what they wrote, and every expansion below it is recomputed. Each level reports in its own nouns, so at the top the report reads like "it can reach 14 things you did not ask for", and any row from a lower level can be written in when one row needs to go deeper.

The third way is where you start. In a browser, with nothing installed, [the playground](https://sharness.ai/code/playground/index.html) puts `pip install sharness-ai` in Pyodide next to a shell on a real Linux kernel. On Linux, `pip install sharness-ai` and `sharness-ai hello`. In a Claude Code session, a skill runs `probe` and `hello` inside the session, with the caveat stated: the session itself is not bound.

## The architecture

The design is a launcher and a small set of single-purpose components. Its theme is "one role, one noun, one uid, one policy, one certificate."

SHarness's moving parts as designed: a launcher outside every domain, the app, and five doors under mutual TLS.

**The person** supplies one policy hash out of band. **The launcher**, outside every domain, refuses to start unless the manifest hashes to that value; it makes one Linux user per component, a session certificate authority and one certificate per role, then destroys the authority's private key, so the set of identities is closed. **The harnessed app**, which might be sgit's CLI, a Claude Code session or your own loop, sits on top and routes: it holds no keys, has no network and writes nothing itself. Around it are the doors:

| Door | Its one job (designed) |
|---|---|
| `sharness.fs` | the only writer of protected folders; refuses anything that parses as a clear key, a private key or a token |
| `sharness.net` | the only network client and the TLS client, with host, endpoint and id allowlists |
| `sharness.bash` | each shell command in a fresh sandbox under a profile, output filtered |
| `sharness.llm` | the only client of the model API; pins the tool list, filters secrets out of every tool result, adds the real key |
| `sharness.kms` | holds the private keys in a `memfd_secret` page, frozen between calls; re-seals to one-time keys; never returns a clear key |

Every connection between them is mutual TLS 1.3 with the role in the certificate (as a SPIFFE ID), and both sides check that the pair is in the edge list, which denies by default. The app never talks to the key service; only the network and model doors do, and the key service never returns a clear key to either: it returns derived keys sealed to a one-time key made for that one request. The site measured what that costs on 24 October 2026: about 3.2 ms for a mutual TLS handshake between two local processes, about 10 ms for the three handshakes of an sgit command, against 146 ms the command already spends importing Python. A disposable user for a session was about 49 ms.

It all started with what the site calls [the last metre](https://sharness.ai/design/why/index.html). Our [PKI handover](https://pki.sgit.ai/handover.md) protects a vault key while it travels, sealed to the receiving agent's public key, and stops protecting it the moment it arrives: on disk, on the command line, and in the agent's transcript. "For an AI agent the worst leak is not the disk. It is the **transcript**." In the design, the sealed message itself becomes the file on disk, the key service opens it inside its own process, and the agent sees a command, ciphertext, fingerprints and a status line, never a key. Nothing in that fix turned out to be specific to sgit, and that generalisation is SHarness.

The same components and the same protocol run in five topologies, and only the launcher changes: one machine with a user per component (what was measured), one container per component, one Kubernetes pod with identities from SPIRE and a NetworkPolicy that mirrors the edges, a remote key service in a cloud function in front of a hardware-backed key, and the platform providing it all.

## The doors, more technically

A Process Behaviour Policy has two kinds of row, and the rule that joins them is the most important technical idea in the design.

**Capability rows** bound what a process can reach: path prefixes to read, write and execute; TCP ports; no network; memory and process caps; no new privileges. The kernel holds them, with Landlock, namespaces, rlimits and cgroups. These are the v0 policy, and they run today.

**Behaviour rows** bound what the process does with a reach it has: append only to this file; this field within this range, never negative; connect only to this host, this endpoint, this vault; at most so many per interval; this operation only with fresh approval. A door holds them. And the rule: "A behaviour row is a Boundary only when the subject has no path to the resource except through the door that holds the row." So every behaviour row has preconditions made of capability rows. An append-only rule on a ledger, held by `sharness.fs`, is a Boundary only if the app's own write rows exclude that file and the app has an edge to the door. If the preconditions do not hold, the row is still well formed, and it gets the barrier kind Expectation, counted. That is "what can currently be controlled", derived from the policy rather than hoped.

The language for those rows is deliberately closed: append only, a section, content by JSON Schema, a numeric range, count and rate, ordering, fresh approval. "A policy that can express arbitrary logic is code, and code in the policy is a rules engine in the trusted path." Anything more is a door of its own, under its own policy. A business that needs "transaction amount within range, daily total under X" writes that as a small door.

The doors form a tree of names, `sharness.<door>.<target>`, where the door is the vocabulary and the target is where it sends. `sharness.fs.disk` writes to the local disk, `sharness.fs.s3` to S3, and `sharness.net.git` holds remote, branch, ref and push, "never force, never main". A target can be the real system, a relay, or a twin, and `.twin` on the end of any name means it is simulated: `sharness.db.postgres.twin` reads as a development world without decoding anything. Development and production are one policy tree with different targets, so a run's hash says which world it ran in. Each door declares what it accepts and what it emits, and a chain is valid only when each hop emits what the next accepts. That is why the network door, which accepts TCP and `CONNECT`, cannot hold a URL row, and an HTTP door below it can.

`sharness.net` shows why the doors are processes and not filters. The kernel only sees a connect to a port, so a relay that forwarded bytes would let the process inside choose the server name itself, which is domain fronting. So the network door is the TLS client: it sends the `CONNECT`, checks the name in the TLS hello against the host, and keeps one audit line per request. The process gets a policy whose only network row is the door's port, so a direct connect is refused by the kernel before a packet leaves.

## What runs today

The site's [status page](https://sharness.ai/evidence/status/index.html) keeps the honest column, and I will keep it here. As of 29 October 2026:

- **`sharness-ai` 0.2.0 on PyPI.** Python standard library only; 6,041 lines in the package and 243 tests, run in CI on Python 3.11 to 3.13.
- **The kernel locks, on one process.** `sharness-ai run --policy FILE --expect-hash sha256:… -- CMD` applies Landlock file and execute rules (a writable path is never executable), TCP port rules, no network, memory and process caps, and refuses to run anything if the hash does not match.
- **The acceptance test.** `sharness-ai hello` runs six probes under a deny-all policy. It held 6 of 6 in five places on 25 October: a cloud session, my browser, headless Chromium, Node and a chroot on the host kernel.
- **The levels in the terminal.** `contain`, `profile` and `explain`.
- **Two doors as early versions.** `sharness.fs`, the only writer, under mutual TLS with 18 conformance vectors; and `sharness.net`, an allowlisting proxy.
- **The launcher's first slice.** `sharness-ai shell --workspace . --sites pypi.org` starts a shell as a fresh user, with its own network namespace holding only loopback, the network door as its only way out, and a live page of every refusal. It was checked on 29 October: pypi.org allowed through the door, example.com refused, a direct connect to 1.1.1.1 refused, a name lookup found nothing.
- **A real Linux kernel in a browser tab.** I asked this site's agent to open the [E09 page](https://sharness.ai/code/browser/demo/index.html) in a headless browser on 29 October. An Alpine guest with Linux 6.18 booted on an emulated CPU, and `hello` ran 111 seconds in:
sharness-ai hello under a Linux kernel in a browser tab, 29 October 2026: six probes, six held.

Read the last line of that output, because it is the project's character in one sentence: "applied by a process to its own child: a Boundary for the child, a Setting for the parent, who could have skipped it. The launcher that binds the agent too is the design, not code."

What is not built: the key service, the shell door, the model door, the launcher's manifest, and the launcher above the agent. seccomp, per-component users for every door, and hostnames in the policy itself are still to come. Nothing yet binds the agent itself.

## How it was built

SHarness is also a demonstration of how we now build. It is one person and a team of agents, each with a role, a behaviour policy in the ABP shape, a status file it keeps itself and, where it holds secrets, a key on pki.sgit.ai: a CLI agent that builds the package, a website agent that owns the site and its gate, a policy agent that holds the definition of the PBP, a security agent that keeps the register, a developer agent writing the policy standard in other languages, a conductor and a Sherpa. Their board, briefs, commit notes and runs are all [public](https://sharness.ai/admin/index.html).

Two things in how it was built matter for whether you can trust it. First, the security register. The site's rule is that "nobody reviewing SHarness should find something it does not already say about itself." The first review, on 25 October, recorded 25 findings, five of them High, all five fixed with a test that fails if the hole opens again. The second, on 29 October, before the release, found two High issues in the shell (it could reach other hosts on the proxy's port, and a process of the shell could outlive it), fixed with tests before 0.2.0 went out. Second, standards with test vectors: the policy's canonical form and hash are a written standard with 28 vectors that the Python, JavaScript and Go implementations all pass, so a policy hashed in one language is the same policy in another.

## What we would like feedback on

This is the part I care about most. SHarness is at the experiments stage, it is open source, and the fastest way for it to get better is for people who did not build it to push on it.

1. **Run `hello` on your machine.** `pip install sharness-ai`, then `sharness-ai hello --json`, and [report it](https://github.com/SHarness-AI/SHarness-AI__CLI/issues/new?template=hello-report.yml). Every machine becomes a row on [hello on your machine](https://sharness.ai/evidence/machines/index.html), and as the project says, "a refusal that did not happen is the most useful thing you can send."
2. **Try to break the shell.** `sharness-ai shell --sites` with one host, and see whether anything leaves on another. Report privately through [GitHub's vulnerability reporting](https://github.com/SHarness-AI/SHarness-AI__CLI/security/advisories/new).
3. **Tell us who should run the launcher.** The agent itself (every lock is then a Setting), a script above it on a laptop (a Boundary), or the platform (a Boundary all the way down). The design wants the third and starts with the second.
4. **If you build a sandbox, a gateway or an agent platform,** tell us which rows of a policy you hold natively, and whether the translation is right.
5. **If you run agents in a business,** write the sentence: which workspace, which sites, which secrets. What the levels make of it, and what is left unheld, is exactly what I would like to see.

## What this does not claim

- **Most of SHarness is designed, not built.** The kernel locks, the levels, two doors and the launcher's first slice run; the key service, the shell and model doors, and the launcher above the agent do not.
- **Nothing binds the agent itself yet.** A policy applied by a process to its own child is a Boundary for the child and a Setting for the process.
- **It does not protect against root or a compromised kernel.** The design trusts the kernel; anything with root can read a process's ordinary memory.
- **The measurements are the project's own.** Each is from one environment on one date, with method on sharness.ai's [evidence](https://sharness.ai/evidence/index.html) page. The one run here is the E09 page in a headless browser on 29 October 2026; the CLI was not run on this site's own machine.
- **The translations have not been run against their targets.** Each matrix cell is what the target's documentation says.
- **"Integration point" is not a partnership.** No vendor named on sharness.ai has agreed to anything.
- **The security reviews were done by an agent of the project.** They are a register for an outside review to start from, not a replacement for one.
- **The cloud service is a proposal.** No provider offers it, and nothing here describes any provider's plans.

If you run agents that read untrusted data, build a sandbox or a platform, or would price the risk of one agent at a time, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

My request of 29 October 2026, kept word for word in this site's repository under `admin/notes/2026-10-29__sharness/`, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine.

sharness.ai was read in full on 29 October 2026, at site v0.6.33, from its [llms.txt](https://sharness.ai/llms.txt) and the markdown of every page: [the brief](https://sharness.ai/design/index.html), [Why: the last metre](https://sharness.ai/design/why/index.html), [Architecture](https://sharness.ai/design/architecture/index.html), [the components](https://sharness.ai/components/index.html), [the PBP on one page](https://sharness.ai/design/pbp/index.html), [the levels](https://sharness.ai/design/levels/index.html), [the decision at the door](https://sharness.ai/design/decision/index.html), [the landscape](https://sharness.ai/landscape/index.html), [enforceability](https://sharness.ai/landscape/enforceability/index.html), [Security](https://sharness.ai/security/index.html), [what exists today](https://sharness.ai/evidence/status/index.html) and [the members](https://sharness.ai/admin/members/index.html); the quotes are from those pages, and the moving-parts figure is sharness.ai's own, re-rendered here with a narrower font (CC BY 4.0). The CLI was read at [SHarness-AI__CLI](https://github.com/SHarness-AI/SHarness-AI__CLI), `dev` at commit 7ea23c6, and its release dates from PyPI. The hello figure is the E09 page's own console output, captured by this site's agent in headless Chromium on 29 October 2026 and set as text. My first article on SHarness, of 24 October 2026, is [a secure harness for agents](https://sharness.ai/articles/secure-harness-for-agents.html) on sharness.ai. On this site: [process behaviour policies](process-behaviour-policies.md), [are hooks the sweet spot?](are-hooks-the-sweet-spot.md), [hooks are kernel code](hooks-are-kernel-code.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [a payout for every row](a-payout-for-every-row.md) and [agents have an identity now](agents-have-an-identity-now.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#introducing-sharness)

### Builds on

- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [Process behaviour policies: the most locked-down Linux process we could build inside Claude's own cloud container, derived from one traced run, enforced by the kernel, for about a tenth of a second](process-behaviour-policies.md) The most locked-down Linux process we could build inside Claude's cloud container: a policy traced from one run, seven kernel walls, 0.1 s.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.

### Continued by

- [Joining Algarve Evolution: The Cyber Boardroom takes the startup membership, and what we can share with the region, our workflows and our technology, all of it open source](joining-algarve-evolution.md) Joining Algarve Evolution: The Cyber Boardroom takes the startup membership and shares its workflows and technology, all open source.
- [Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent](villager-services-for-explorer-coders.md) Villager services for explorer coders: founders with ten years of checklists build the apps; we sell everything behind them in finite packs.
- [Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today](lovable-with-sharness.md) Lovable with SHarness, and the trojanised Claude Code extension: where a policy boundary has to sit, and what SHarness can stop today.
- [Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way](seven-iam-predictions-already-here.md) Sunnykumar K.'s seven IAM predictions for 2027, checked against agent teams that run today: four already here, one agreed, two different bets.
- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.
- [Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break](proven-controls-for-agents.md) Hem Pant's governance as code and Sondera's policy-as-code paper, joined: who holds each control, and six controls we tried to break.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 323 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=323)

**Posting this article on LinkedIn?** The cover is [introducing-sharness.jpg](banners/introducing-sharness.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/introducing-sharness.html)*
