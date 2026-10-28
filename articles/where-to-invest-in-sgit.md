# Where to invest in sgit: the tool, a hub for vaults, or open core, with the history of developer platforms, the evidence of use, three business plans, and the investor deck as a vault, sgit.ai

> If money goes into sgit, where should it go? The tool and its open format, a hub for vaults (SGitHub, the way GitHub is for code and Hugging Face for models), or open core in the GitLab style? I asked this site's agent to look at it as an investor would, with the history of developer platforms, what they were worth and how they captured the value, the state of sgit on 28 October 2026, and the evidence of use, including what is not there yet. The history says the network beats the host (SourceForge sold for about $20M, GitHub for $7.5B), registries struggle alone, hosting is where open source gets paid, and the hub of public work is the moat (Hugging Face, $12.93B to Nvidia, pending). Git is under strain from agents (Anthropic replaced it with Scion), and capital is following (Entire's $60M seed). My answer is the hub, with the format open and self-hosting always possible. The deck, the thesis, three business plans, the data and the evidence are in a public vault that runs as an app, and is meant to be forked for each investor.

*Source: <https://newsroom.sgit.ai/articles/where-to-invest-in-sgit.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where to invest in sgit: the tool, a hub for vaults, or open core, with the history of developer platforms, the evidence of use, three business plans, and the investor deck as a vault

# Where to invest in sgit: the tool, a hub for vaults, or open core, with the history of developer platforms, the evidence of use, three business plans, and the investor deck as a vault

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.0.0](versions/where-to-invest-in-sgit.md) · [newsroom v0.13.122](https://newsroom.sgit.ai/admin/versions.html) · sgitinvestmentstartupsopen-sourceplatformsvaultssgithubpitcharticle

***Abstract:** If money goes into sgit, where should it go? The tool and its open format, a hub for vaults (SGitHub, the way GitHub is for code and Hugging Face for models), or open core in the GitLab style? I asked this site's agent to look at it as an investor would, with the history of developer platforms, what they were worth and how they captured the value, the state of sgit on 28 October 2026, and the evidence of use, including what is not there yet. The history says the network beats the host (SourceForge sold for about $20M, GitHub for $7.5B), registries struggle alone, hosting is where open source gets paid, and the hub of public work is the moat (Hugging Face, $12.93B to Nvidia, pending). Git is under strain from agents (Anthropic replaced it with Scion), and capital is following (Entire's $60M seed). My answer is the hub, with the format open and self-hosting always possible. The deck, the thesis, three business plans, the data and the evidence are in a public vault that runs as an app, and is meant to be forked for each investor.*

Three ways to build a company on sgit, and the companies that went each way before.

## In short

- **The question:** where should investment in sgit go: the tool, a hub for vaults, or open core?
- **The history:** the network beats the host; registries struggle alone; hosting is where open source gets paid.
- **The hub of public work is the moat:** GitHub sold for $7.5B, and Nvidia is buying Hugging Face for $12.93B.
- **Why now:** Anthropic replaced Git for its monorepo, and "git for agents" startups are being funded.
- **Where sgit is:** 99 releases since March, Git parity mostly done, and features Git cannot match.
- **The gap:** no paying customer of sgit itself yet; most production use is our own.
- **My answer:** fund the hub (SGitHub), keep the format open, sell self-host support as the bridge.
- **The deck is a vault:** it runs as an app, carries its evidence, and is forked per investor.

## The question

I am running several versions of this at the same time, so the question is a real one. If an investor puts money into sgit, where does it do the most good? There are three candidates:

1. **The tool and the format.** sgit itself, the command line and the open vault format, Apache-2.0.
2. **The hub.** A hosted home for vaults, where people and agents share, fork, discover and run them. I have been calling it SGitHub: what GitHub is for code and Hugging Face is for models, for the work agents produce.
3. **Open core.** A server teams run themselves, with paid features on top, the way GitLab did it.

I asked this site's agent to research it as an investor would: the history of developer platforms and what they were worth, the market now, the state of sgit, and the evidence that anyone uses it. I have a stake, so read this with that in mind. sgit is ours.

## Git is being pushed to its limits

On 13 October Anthropic published [how it redesigned source control](https://www.anthropic.com/research/redesigning-source-control), which I wrote about in [Scion and sgit](scion-and-sgit.md). Merges into its monorepo went from about 2,500 a day in May to more than 30,000 a day in September, and Git was "actively undermining our ability to scale". A team of seven built Scion and migrated in five months. Anthropic is clear that it is "by no means a suitable replacement for git for general use".

The companies that outgrew Git built their own; startups building version control for agents are being funded.

Google and Meta built their own long ago. What is new is the money for everyone else. Entire raised a $60M seed at a $300M valuation in February, a record for developer tools. GitButler raised a $17M Series A, Pierre (Code.Storage) $22M. Cursor bought Graphite, and Hugging Face bought XetHub for its storage. None of them encrypt the work from the host, and none treat the work itself (data, app, history and sources) as the thing you hand over.

## What developer platforms were worth

The agent's research covers sixteen companies, with a source for every number and a label for how far to trust it. The pattern is clearer than I expected.

What developer platforms were worth, and how they captured it, on a log scale.

- **The network beats the host.** SourceForge hosted open source first, never owned the workflow, and was sold for about $20M in 2012. GitHub owned the workflow (forks, pull requests, profiles) and sold to Microsoft for $7.5B in stock in 2018, after two priced rounds.
- **Registries struggle alone.** npm had about $3M of revenue in 2019 and went to GitHub. Docker Hub won the habit and sold its enterprise business to Mirantis.
- **The hub of public work is the moat.** Hugging Face built the hub of public models and datasets, and Nvidia announced a $12.93B acquisition on 3 September 2026. The deal is pending.
- **Hosting is where open source gets paid.** MongoDB went from a ~$1.2B IPO to about $31B on Atlas. Supabase, fully open source, raised at $10.5B in June. Vercel owns Next.js and hosts it, at $9.3B.
- **Open infrastructure has strategic buyers.** Red Hat (~$34B), HashiCorp ($6.4B) and Confluent (~$11B) all went to IBM. HashiCorp's licence change did not protect its value.
- **Open core works, and makes a different company.** GitLab listed at about $11B and had $955M of revenue in its last fiscal year, on a proprietary enterprise tier.

There is also an open-source premium. A Linux Foundation study of more than 800 commercial open-source companies found Series A valuations 1.6 times those of closed peers, twice the chance of going from seed to Series A, and a median acquisition of $482M against $34M.

## Three paths, and my answer

The tool on its own is Git's story: enormous value, and no company. Open core is GitLab's, but sgit's rule is that there is no proprietary tier, which I set out in [open source what you build](open-source-so-you-keep-it.md); for us, that path becomes support and certification, the way Red Hat did it.

**My answer is the hub.** Fund SGitHub, keep the format open, and make self-hosting always possible. The open standard feeds the hub; the hub is what is sold; and support for teams that must run their own server is the bridge to revenue while the hub grows.

The reasons are the ones in the history. The network of public work is the moat, and the public vaults with read keys are already its seed: 54 on sgit.ai, more here. Vault apps make opening a vault the same as running it. Agents are the users who will grow fastest, and every surface of sgit is built for them first. And a hub that cannot read its users' vaults makes a different promise from GitHub's, which is a reason to trust it. Leaving is always possible, because the format and the server are open.

## Where sgit stands

Commits per month on the CLI's dev branch and releases per month on PyPI, March to October 2026.

sgit has had 99 releases on PyPI since 20 March, the latest (0.26.5) this morning. The repository has 1,757 commits across all branches and 5,032 test functions, and [cli.sgit.ai](https://cli.sgit.ai/) lists 174 commands. The work comes in bursts, and the October one was driven by our own largest vault, which is the story of [a tangent that shipped](a-tangent-that-shipped.md).

Git parity on 28 October 2026, from the CLI team's roadmap.

On Git parity, the CLI team's roadmap of 28 October has most of the client done, line-level merge and partial commits shipped on dev today, and seven more designs (signing with your own key, renames, blame, bisect, grep, cherry-pick, hooks, rebase, worktree) at about 36 to 40 days of work. What Git has no equivalent for is in [what sgit does that Git does not](what-sgit-does-that-git-does-not.md): a host that reads nothing, read keys, write-only lanes, custody without access, policy carried by the vault, byte-range clones and vault apps.

## Real use, and what is not there yet

sgit in use, measured, and what is not there yet.

The production use is real and mostly ours. The PHP newsroom's source-watch vault holds 79,465 files and 2.7 GB; as a pack vault it clones in 95 seconds where it took 13 minutes 47. Ten agents and one person share [one vault](one-vault-ten-agents.md) of about 35,000 objects. The RiskMandate inbox team runs on [a vault per workflow](the-inbox-team-as-a-recipe.md). Health-related projects use vaults too; the OmKneeHealth scenario is the public one. Outside our own work, [Ruflo merged a pull request](our-first-pr-in-ruflo.md) for sgit memory checkpoints, and the [KGELL working group](knowledge-graphs-for-kgell.md) has a vault of 309 graphs.

What is not there yet matters as much. There is no paying customer of sgit itself; when [SG/Send](from-send-to-sgit.md) first charged, its briefs recorded that users bought credits, tested once and did not come back. The 13,915 PyPI downloads since April are downloads, not users. The public PKI register has no real keys in it yet, and the web app cannot open a pack vault. An investor should see all of that, so the deck says it.

## How we got here

From sending a file to a hub for vaults: the concepts in the order they arrived in 2026.

The ideas came before the features. The vault and the data room were named in February, before folders and Git's model. Read keys, mirrors and vault-carried policy came in early October; PKI a few days later; pack mode and byte-range clones in the last week, because a real vault needed them. The hub is the next step on the same line.

## The deck is a vault

The investor deck, running from its vault: the title slide and the three business plans side by side.

Everything is in a public vault, and the vault is the pitch. Open it and a 20-slide deck runs as a vault app, with a PDF of the same deck beside it. Clone it and you get what is behind every slide:

- **THESIS.md:** the argument in full.
- **plans/:** three business plans. A, the open standard; B, SGitHub, the hub (the one I would fund); C, self-host and support.
- **data/:** the product measured, and every platform figure with its source and confidence label.
- **articles/:** the newsroom articles the numbers come from.
- **IDEAS.md:** ideas to create investor interest, and to pick the right investors before the first meeting.
- **personalise.py:** forks the deck for one investor, with their name and the slides that matter to them first.

That last one is the point. Each investor gets their own vault, forked from this one, with its own keys. They can see exactly what was changed for them and what was not, and point their own agent at the evidence before we meet. The ask (round size, instrument, use of funds) is left blank, as it is on [sgit.ai/investors](https://sgit.ai/investors/), until I state it.

Open it in the [vault browser](https://dev.vault.sgraph.ai/#sgit_public_read_0b60bf869fb5e4cea1f98a6ae99afa3e7503107cda83d07eca5d433913bbb2d0%3Aj0oob7zp), or clone it with `pip install sgit-ai` and `sgit clone sgit_public_read_0b60bf869fb5e4cea1f98a6ae99afa3e7503107cda83d07eca5d433913bbb2d0:j0oob7zp sgit-investor-briefing`. It will move to cli.sgit.ai and be forked and rekeyed from there, which is itself a demonstration.

## Creating interest, and choosing investors

A few of the ideas in the vault, all of them the product selling itself:

- **A write-only front door.** An append lane where an investor leaves a short note (their thesis, their overlap with the git-for-agents companies, what they want to see in 18 months) and learns nothing about anyone else's.
- **A data room that is a vault,** which their agent can read and the host cannot.
- **Open the big vault in the meeting:** one folder of a 2.7 GB vault, cloned in seconds.
- **Ask three questions first:** do you back open source with no proprietary tier, do you see agents as the main users of developer infrastructure, and are you comfortable with a pitch that is public?
- **Check for conflicts early,** with funds already in Entire, GitButler or Pierre.

## What this does not claim

- **It is a thesis, not a forecast.** The milestones and plans are proposals for discussion, not commitments.
- **SGitHub is not built.** The CLI team's roadmap names it as the future server product.
- **The valuations are other companies',** from filings, company posts and press; some are labelled as estimates, and the Hugging Face deal is pending.
- **I have a stake,** and most of the production evidence is my own companies' use.

## Where this comes from

[Anthropic on Scion](https://www.anthropic.com/research/redesigning-source-control) (13 October 2026); [PyPI](https://pypi.org/project/sgit-ai/) and [pypistats](https://pypistats.org/packages/sgit-ai), read 28 October; the [sgit CLI repository](https://github.com/SGit-AI/SGit-AI__CLI) and its Git parity roadmap of 28 October; [cli.sgit.ai](https://cli.sgit.ai/); [sgit.ai/investors](https://sgit.ai/investors/); [pki.sgit.ai](https://pki.sgit.ai/). Every platform figure, with its URL, quote and confidence label, is in the vault's data/platforms.json; the Linux Foundation's study of commercial open source is from August 2025. Research by this site's agent, under my direction.

## Threads

Startups & strategyVaults & method[This article as a graph →](graphs.md#where-to-invest-in-sgit)

### Builds on

- [Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it](scion-and-sgit.md) Anthropic's Scion replaced Git for agents inside one company; sgit, open source and encrypted, shares its core ideas, measured on a 35,000-object vault.
- [Open source what you build, even while you are employed: nobody copies it, and it is the only way you get to keep using it](open-source-so-you-keep-it.md) Nobody copies your open source ideas; the real advantage is that you keep using your own work from job to job, and a rough public history protects you.
- [A tangent that shipped: how sgit's pack mode went from a slow clone to a release in ten days, and took the PHP story's biggest vault from a 13-minute clone to 95 seconds the day after](a-tangent-that-shipped.md) How a tangent about zips became sgit's pack mode in ten days, and took the PHP story's biggest vault from a 13-minute clone to 95 seconds.
- [What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead](what-sgit-does-that-git-does-not.md) Ten sgit releases turned minutes into seconds; the honest map of what sgit does that Git does not, and where Git is ahead.
- [One vault, ten agents, 35,000 objects: what sgit does when the repository is big and the clients are many, measured on the vault behind this newsroom](one-vault-ten-agents.md) The vault behind this newsroom, 35,000 objects and ten agents, measured eight ways: one folder in 13 seconds, history as the edge, storage as the bottleneck.
- [The inbox team as a recipe: how the RiskMandate agents run my email and CRM, written down by one of them so a second team can copy it](the-inbox-team-as-a-recipe.md) The RiskMandate inbox team, written down by its own agent so a second team can copy it.
- [Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there](our-first-pr-in-ruflo.md) rUv merged Mondweep's pull request #4239: one docs page, the first commit on Ruflo's main branch to mention SGit or an ABP. The four pieces, shown.
- [Knowledge graphs in the era of LLMs: what the KGELL COST Action is doing, and what 309 graphs built by agents in a working newsroom can bring to its working group on construction](knowledge-graphs-for-kgell.md) What the KGELL COST Action is doing, and 309 agent-built graphs offered to its working group on construction.
- [From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults](from-send-to-sgit.md) Eight months of SG/Send, checked against its own briefs and commits: how file sharing became sgit and vaults, the pace, and what the market said.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 313 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=313)

**Posting this article on LinkedIn?** The cover is [where-to-invest-in-sgit.jpg](banners/where-to-invest-in-sgit.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-to-invest-in-sgit.html)*
