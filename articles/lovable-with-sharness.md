# Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today, sgit.ai

> Colin Nwachukwu Ife of Geordie AI posted about a tampered copy of the Claude Code extension for VS Code, served through Cursor's extension marketplace on 29 October for about eleven hours. It ran as soon as the editor loaded it, tried to add an attacker's SSH key and open a reverse tunnel, set itself to start again, and sent details of the machine, including the names of its environment variables, to a server. Cursor's own notice says the versions were 2.1.312 and 2.1.313, that they were not developed by Anthropic, and that uninstalling may not be enough. The post's point is the right one: the agent did not misbehave, the extension hosting it was backdoored, and securing the agentic stack is an end-to-end problem. I was asked two things: how to use Lovable, the AI app builder, with SHarness, our secure harness, and whether SHarness could protect against this kind of exploit. The honest answers are these. Lovable builds and hosts in its own cloud, so SHarness cannot reach inside it; but Lovable syncs every project to GitHub in both directions, and the local half of the work, your clone, your coding agent and your package installs, can run in a SHarness shell that writes only the workspace and reaches only the sites it names. Against this exploit, the rows of a Process Behaviour Policy would refuse each step it took, and two of them run today. But SHarness runs only on Linux, the tampered build targeted macOS and Windows, and the launcher that would bind an editor or an agent is not built yet. So today it would not have stopped this. What it shows is where the boundary has to be.

*Source: <https://newsroom.sgit.ai/articles/lovable-with-sharness.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today

# Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/lovable-with-sharness.md) · [newsroom v0.14.18](https://newsroom.sgit.ai/admin/versions.html) · sharnesslovablesupply-chainextensionsprocess-behaviour-policysecurityagentsarticle

***Abstract:** Colin Nwachukwu Ife of Geordie AI posted about a tampered copy of the Claude Code extension for VS Code, served through Cursor's extension marketplace on 29 October for about eleven hours. It ran as soon as the editor loaded it, tried to add an attacker's SSH key and open a reverse tunnel, set itself to start again, and sent details of the machine, including the names of its environment variables, to a server. Cursor's own notice says the versions were 2.1.312 and 2.1.313, that they were not developed by Anthropic, and that uninstalling may not be enough. The post's point is the right one: the agent did not misbehave, the extension hosting it was backdoored, and securing the agentic stack is an end-to-end problem. I was asked two things: how to use Lovable, the AI app builder, with SHarness, our secure harness, and whether SHarness could protect against this kind of exploit. The honest answers are these. Lovable builds and hosts in its own cloud, so SHarness cannot reach inside it; but Lovable syncs every project to GitHub in both directions, and the local half of the work, your clone, your coding agent and your package installs, can run in a SHarness shell that writes only the workspace and reaches only the sites it names. Against this exploit, the rows of a Process Behaviour Policy would refuse each step it took, and two of them run today. But SHarness runs only on Linux, the tampered build targeted macOS and Windows, and the launcher that would bind an editor or an agent is not built yet. So today it would not have stopped this. What it shows is where the boundary has to be.*

Colin Nwachukwu Ife's post about the trojanised Claude Code extension in Cursor's marketplace.

## In short

- **A tampered copy of the Claude Code extension** was served through Cursor's extension marketplace on 29 October, for about eleven hours.
- **It ran when the editor loaded it,** tried to add an SSH key and a tunnel, persisted, and sent the machine's details out.
- **The agent did not misbehave.** The extension hosting it was backdoored, as the post says.
- **Lovable builds in its own cloud,** so SHarness cannot reach inside it. Its Git sync brings the local half of the work to you.
- **That local half can run in a SHarness shell:** the workspace writable, only named sites reachable, your coding agent inside.
- **Against this exploit, a policy would refuse every step it took.** Two of those rows run today.
- **But not here, not yet.** SHarness is Linux-only, the build targeted macOS and Windows, and the launcher that binds an editor is design.

## What happened

The post that prompted this is Colin Nwachukwu Ife's, Head of AI Risk at Geordie AI, and Geordie AI's [advisory](https://www.geordie.ai/resources/technical-advisory-trojanized-claude-code-vs-code-extension/) gives the indicators and the clean-up. The primary source is [Cursor's own security notice](https://cursor.com/blog/claude-code-extension-security-notice), dated 29 October and updated on 30 October. From the notice, read today:

- **What and where.** Versions 2.1.312 and 2.1.313 of the Claude Code extension, for Windows and macOS, in "the Cursor VS Code Extension Marketplace", between about 2:27 am and 1:35 pm Pacific time on 29 October. Cursor says: "These malicious versions of the extension were not developed by Anthropic."
- **What it collected.** The host name, user name, operating system, home directory, the names of environment variables, working directories, the Git email and the public IP address. Names, not values; Cursor adds that this "does not rule out later credential access over the backdoor."
- **The backdoor.** It added an SSH key, tried to enable the SSH service and opened a reverse tunnel, with a LaunchAgent on macOS or a scheduled task on Windows to start again. Cursor says that, unless Cursor was running with administrator rights, errors in the code meant this step would fail.
- **The clean-up.** Remove the key, the persistence and the tunnels, consider a rebuild, and rotate credentials from a trusted system. "Uninstalling the extension may not be sufficient."
- **What Cursor did.** It removed the versions, shut down and rebuilt the marketplace, rotated its keys, and audited the other extensions. The notice does not say how the tampered versions got there.

Some details differ between sources, and I would rather say so than smooth them over. The post and Geordie's advisory name 2.1.313; Cursor's notice now names 2.1.312 and 2.1.313. The post gives "up to 5,000 users according to Cursor's own advisory"; we could not find that figure in the notice's current text, which may have changed in its update. Early reports placed the build on Open VSX; Cursor's notice names only its own marketplace, and [StepSecurity](https://www.stepsecurity.io/blog/claude-code-extension-trojanized) reports that Anthropic said the version was never published to Open VSX or Microsoft's marketplace. No official statement says who did it, and we do not speculate.

## The point the post makes

The post's conclusion is the part I agree with most: the agent did not misbehave, the extension hosting it was backdoored, and securing the agentic stack is an end-to-end problem. An editor's extensions run in the editor's extension host, and [Microsoft's own documentation](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) says the extension host "has the same permissions as VS Code itself". There is no per-extension permission model. Whatever the user can do, a loaded extension can do, before any agent has said a word.

That is exactly the gap SHarness was built for: a boundary that sits outside the process it constrains, set before the process starts, which a tricked or tampered process cannot widen. [Introducing SHarness](introducing-sharness.md) describes it; here is how it meets this case.

## Could SHarness have stopped it?

The tampered build's steps against the policy row that would refuse each, and what of SHarness runs today.

Step by step, a Process Behaviour Policy has a row for each thing the build did:

- **Writing a key to `~/.ssh/authorized_keys`** is a write outside the project. A policy that lets the process write only its workspace refuses it. That rule, Landlock path rules applied by the Linux kernel, runs today in `sharness-ai run`.
- **Planting persistence,** a LaunchAgent, a scheduled task or a cron entry, is also a write outside the workspace, and the same rule refuses it; SHarness also never lets a writable path be executable.
- **Beaconing to an address and opening a tunnel** need the network. A policy with no network, or only the network door to named sites, refuses both. `sharness-ai shell --workspace . --sites github.com` runs today: a shell as a fresh user, in a network namespace that holds only loopback, with the door as its only way out.
- **Reading the names of secrets** works because the secrets were in the environment. In SHarness's design, keys are held by a door and never handed to the process. The key service is not built.
- **Running on load, inside the editor,** is the root of it. The boundary has to be around the editor's extension host itself, and the launcher that would bind an agent or an editor is design, not code.

So the honest answer is no, not today. SHarness runs only on Linux, and on macOS it refuses to run and says so; the tampered build targeted macOS and Windows; and nothing in SHarness yet confines an editor. What the table shows is that every step this build took is one a written policy refuses, which is the argument for having one.

## What you can do today

On Linux, the nearest thing is to move the editor's working half into a box. VS Code's remote development runs "workspace extensions" in a remote extension host, inside a container or a remote machine, and in a dev container [extensions are installed and run inside the container](https://code.visualstudio.com/docs/devcontainers/containers); interface extensions still run locally. A container whose policy came from `sharness-ai policy translate --to docker`, writing only the workspace and reaching only named sites, would have held the key, the persistence and the tunnel inside a box you can throw away. `policy translate` also prints what the target does not enforce, so you know which rows are Boundaries and which are only Settings.

And for any machine, the lesson of the clean-up list is to keep fewer secrets where extensions run. A backdoor reads what the user can read.

## Lovable with SHarness

Lovable builds in its cloud; the local work happens in a SHarness shell that reaches only what it names.

[Lovable](https://docs.lovable.dev/) is a platform for building web applications from natural language. Its agent writes the app; its Cloud backend, built on Supabase's open-source foundation, holds the database, authentication, storage and functions; and it runs security scans on every publish, while its documentation says plainly that the scans "cannot guarantee complete security". All of that runs in Lovable's cloud, where SHarness cannot reach.

What brings it within reach is [Git sync](https://docs.lovable.dev/integrations/git-sync-overview). Lovable syncs a project to GitHub, GitLab or Bitbucket in both directions, and its documentation describes the local loop: clone the repository, edit with your own editor or coding assistant, push, and the commits appear in the Lovable project, through the same checks. That local loop is where a developer's machine, editor, extensions, agent and package installs meet the code, and it is exactly what SHarness is for. On Linux:

1. **Clone the Lovable project's repository** into a workspace, on a feature branch, as Lovable's documentation advises.
2. **Open a SHarness shell on it:** `sharness-ai shell --workspace . --sites github.com,registry.npmjs.org`, adding `mcp.lovable.dev` if your agent should use Lovable's MCP server.
3. **Run your coding agent and the build inside it.** It can write the workspace and reach only those sites; a dependency or a tool that tries to write your SSH keys, plant a start-up entry or call another address is refused, and the shell's page shows each refusal.
4. **Push the branch** and merge it in Lovable, where its scans run again.

Two properties make the pairing better than either alone. **The production secrets stay in Lovable:** its secrets are encrypted, write-only and injected into its functions, so the developer's machine holds the code, not the keys, and a backdoored tool there finds less to take. And **the local half has a boundary,** set from outside, that a tampered package or extension cannot widen.

## What this does not claim

- **SHarness would not have stopped this incident.** It is Linux-only, and the tampered build targeted macOS and Windows; nothing in SHarness confines an editor yet.
- **SHarness is early.** sharness-ai 0.2.0, from 29 October, is marked by its own package as an early development release; the key service, the launcher above the agent, seccomp and hostnames in the policy are not built.
- **The Lovable workflow is proposed, not tested.** It rests on Lovable's documented Git sync and SHarness's first launcher slice; we have not run it end to end.
- **The incident's details are from the notices and reports cited,** read on 31 October 2026; where they differ, we say so. How the tampered versions reached the marketplace is not stated by anyone official.
- **My interest:** I build SHarness. Claude Code is made by Anthropic, whose models write this newsroom.

## Where this comes from

- My message of 31 October 2026 and the post it shares, word for word with the screenshot, in `admin/notes/2026-10-31__lovable-sharness/` in this site's repository.
- Opened on 31 October 2026: [Cursor's security notice](https://cursor.com/blog/claude-code-extension-security-notice) (29 October, updated 30 October); [Geordie AI's advisory](https://www.geordie.ai/resources/technical-advisory-trojanized-claude-code-vs-code-extension/) (30 October); [StepSecurity's report](https://www.stepsecurity.io/blog/claude-code-extension-trojanized), including Anthropic's statement as it reports it; Microsoft's [extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security), [remote extensions](https://code.visualstudio.com/api/advanced-topics/remote-extensions) and [dev containers](https://code.visualstudio.com/docs/devcontainers/containers); Lovable's documentation on [Git sync](https://docs.lovable.dev/integrations/git-sync-overview), [Cloud](https://docs.lovable.dev/features/cloud), [security](https://docs.lovable.dev/features/security) and [secrets](https://docs.lovable.dev/features/secrets); [sharness.ai](https://sharness.ai/llms.txt), its [status page](https://sharness.ai/evidence/status/index.html) and [sharness-ai on PyPI](https://pypi.org/project/sharness-ai/).
- Related: [introducing SHarness](introducing-sharness.md), [selling less code](selling-less-code.md), [proven controls for agents](proven-controls-for-agents.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#lovable-with-sharness)

### Builds on

- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue](selling-less-code.md) The economics of customised open source: the customer pays for the features they use, the maker certifies it, and the pipeline is tied to revenue.
- [Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break](proven-controls-for-agents.md) Hem Pant's governance as code and Sondera's policy-as-code paper, joined: who holds each control, and six controls we tried to break.

### Continued by

- [From a checklist to an app you calibrate: your list is already an information system, so build its smallest version in half an hour, use it, log every run, and let it grow](from-a-checklist-to-an-app.md) From a checklist to an app you calibrate: build the smallest version in half an hour, use it tomorrow, log every run, and let it grow.
- [Vibathon Algarve 2026: a sold-out day of building with AI at the University of the Algarve, and Algarve Evolution, the movement that wants the region to be an innovation hub](vibathon-algarve-2026.md) Vibathon Algarve 2026: a sold-out day of building with AI in Faro, and Algarve Evolution, the movement making the region an innovation hub.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 340 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=340)

**Posting this article on LinkedIn?** The cover is [lovable-with-sharness.jpg](banners/lovable-with-sharness.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/lovable-with-sharness.html)*
