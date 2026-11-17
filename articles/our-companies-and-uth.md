# Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these, sgit.ai

> Earlier today I mapped how our open-source stack could plug into UAlgTec Heritage, UTH, the University of the Algarve's new European centre of excellence for heritage science and technology. This is the other half of that map, company by company. UTH's aim is not only a platform: it is a HeritageTech sector, the way FinTech and HealthTech became sectors, and a sector is made of companies. We have spent this year building a set of small companies that each do one thing and together go end to end. SGit and SG/Send keep evidence encrypted and versioned; pki.sgit.ai gives every person and agent a key; SHarness puts a kernel-enforced boundary round every process an agent starts; Agent Behaviour Policies, sold by RiskMandate, say what each agent may do; AgentiCCells sets up small agentic teams and, through its site factory, a website per project; GAMMA-Ray rates agents against named standards; VoiceDebrief turns voice notes into records on the phone; PrompTugal.news files news by place; and this newsroom explains all of it. Here is what each could do for a heritage team, with its website, the layer it sits in, and a first use; and why companies like these are what a sector is made of.

*Source: <https://newsroom.sgit.ai/articles/our-companies-and-uth.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these

# Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/our-companies-and-uth.md) · [newsroom v0.14.140](https://newsroom.sgit.ai/admin/versions.html) · heritagearchaeologyalgarvestrategysgitsharnessabpriskmandateagenticcellspromptugalvoicedebriefpartnershipsarticle

***Abstract:** Earlier today I mapped how our open-source stack could plug into UAlgTec Heritage, UTH, the University of the Algarve's new European centre of excellence for heritage science and technology. This is the other half of that map, company by company. UTH's aim is not only a platform: it is a HeritageTech sector, the way FinTech and HealthTech became sectors, and a sector is made of companies. We have spent this year building a set of small companies that each do one thing and together go end to end. SGit and SG/Send keep evidence encrypted and versioned; pki.sgit.ai gives every person and agent a key; SHarness puts a kernel-enforced boundary round every process an agent starts; Agent Behaviour Policies, sold by RiskMandate, say what each agent may do; AgentiCCells sets up small agentic teams and, through its site factory, a website per project; GAMMA-Ray rates agents against named standards; VoiceDebrief turns voice notes into records on the phone; PrompTugal.news files news by place; and this newsroom explains all of it. Here is what each could do for a heritage team, with its website, the layer it sits in, and a first use; and why companies like these are what a sector is made of.*

Our companies and websites, each mapped to a need of an AI-first heritage platform, by layer.

## In short

- **UTH wants a HeritageTech sector,** and a sector is made of companies.
- **We have built a set of small companies,** each doing one thing, together end to end.
- **Each maps to a heritage need:** evidence, identity, boundaries, policies, teams, ratings, field notes, the public story.
- **All of them run for real** in our own work, with live websites.
- **The open parts are free to adopt;** the companies sell setup, policies and teams.
- **A model for the sector:** small, specialised companies on a shared, open trust layer.

## Why companies

In [HeritageTech, together](heritage-tech-together.md) I mapped our stack onto UTH's plans: an AI-first heritage platform needs evidence that cannot be quietly changed, records signed by the person who made them, data from many teams that does not collide, agents with limits, and claims a reader can follow back to the find.

But UTH's stated goal is bigger than a platform. It wants a European HeritageTech sector, the way FinTech and HealthTech became sectors. Sectors are made of companies, usually small ones, each doing one thing well on top of shared infrastructure. That is exactly how we have built ours this year: separate companies, each with its own website and its own customers, that use each other for real ([the intersection](the-intersection.md)). So here they are, one by one, with what each could do for heritage.

## The foundations

- **[SGit](https://sgit.ai/)** is git for encrypted vaults: a vault is a unit of work, its data, history and sources, versioned and handed over with a single read key ([how a vault works](how-a-vault-works.md)). **For heritage:** an evidence vault per site or collection, owned by the project, opened by a key, never by the host; sensitive locations kept out of the public copy.
- **SG/Send** is the server the vaults live on, with append lanes that accept writes and return nothing, and it can be self-hosted ([deploy sgit from CI](deploy-sgit-from-ci.md)). **For heritage:** each team on a dig writes into the project without reading or changing the rest; a European project runs it in an EU region.
- **[pki.sgit.ai](https://pki.sgit.ai/)** gives every person and every agent a key, made in the browser, and passes keys and sealed links as QR codes ([a key for every person](a-key-for-every-person.md)). **For heritage:** a signature on every context sheet and find record, and a QR code on every find bag.
- **[SHarness](https://sharness.ai/)** puts a Process Behaviour Policy round every process an AI agent starts, enforced by the Linux kernel ([introducing SHarness](introducing-sharness.md)). **For heritage:** the platform's agents can only touch the records they are meant to, whatever a prompt says.

## The standard and its seller

- **[Agent Behaviour Policies](https://abp.sgit.ai/)** describe, for one agent, what it can reach, what it was asked to do, the gap, and what stands in the way ([where assist becomes execute](where-assist-becomes-execute.md)). **For heritage:** a written policy for each agent of the AI-first platform, the one that classifies finds, the one that drafts reports, the one that answers visitors, readable by a director, a funder or an ethics board.
- **[RiskMandate](https://riskmandate.ai/)** sells those policies, from a downloadable pack to one corrected for your situation and signed by a professional ([know the reach](know-the-reach.md)). **For heritage:** the policies for a European-funded platform, reviewed before it goes live, the kind of evidence a Horizon Europe project is asked for.

## Teams and sites

- **[AgentiCCells](https://agenticcells.ai/)** sets up small teams of AI agents as fixed-price cells, each agent with a key and a policy ([the cell is the unit](the-cell-is-the-unit.md)). **For heritage:** an agentic cell per research group or per startup in the centre's programme, set up in days, seen and stoppable.
- **The site factory** at agenticcells.site makes a repository, an address and a website from one commit, in minutes ([the site factory works](the-site-factory-works.md)), and a person's own vault can feed it ([your own agentic cell](your-own-agentic-cell.md)). **For heritage:** a site for every excavation, project and researcher, made from the vault, kept up by its owner's own agent.

## Checking and recording

- **[GAMMA-Ray](https://gamma-ray.sgit.ai/)** rates agents and companies against named standards, with every rating carrying its evidence ([agents rating agents](agents-rating-agents.md)). **For heritage:** the platform's agents and partners checked against the heritage and data standards they must follow, with the gaps listed, not hidden.
- **[VoiceDebrief](https://voicedebrief.ai/)** turns a voice note into a transcript and a debrief on the phone, offline, kept in a vault the user owns ([build on VoiceDebrief](build-on-voicedebrief.md)). **For heritage:** field notes spoken on site, where there is often no signal, recorded and signed the same day.

## The public story

- **[PrompTugal.news](https://promptugal.news/)** files news where it happens, with an agent for every town in the Algarve, and shows who wrote, checked and signs each piece ([PrompTugal.news by place](promptugal-news-by-place.md)). **For heritage:** heritage news by place, from every town that has a site, with the proof attached, and local outlets certifying national stories about their patch.
- **This newsroom, newsroom.sgit.ai,** explains every piece of the stack, every release signed. **For heritage:** the public, readable record of how the platform is built, the way this one records ours.
- **Native apps,** built by agents for iPhone, iPad and Android ([native apps by agents](native-apps-by-agents.md)). **For heritage:** a visitor app for a site or a museum, made from the same vault.

## How they fit together

One find, through our companies: spoken, signed, stored, checked, explained, published.

Take one find. An archaeologist speaks a note on site, and VoiceDebrief transcribes it on the phone. They sign the record with their key from pki.sgit.ai, and a QR code goes on the find bag. The record lands in the site's SGit vault through their team's lane on SG/Send. The platform's agents, each under a behaviour policy from RiskMandate and a SHarness boundary, classify it and add it to the site's graph. GAMMA-Ray checks those agents against the standards. And the find reaches the public through the site's own website from the factory, and through PrompTugal.news, with its proof.

## A model for the sector

What UTH could take from this is not only the tools but the shape: small, specialised companies, each with one job and one website, on a shared, open trust layer that none of them owns. That is how a sector forms around a centre of excellence. The open parts, SGit, SG/Send, pki.sgit.ai, SHarness and the policy standard, are free to adopt; the companies sell setup, policies, teams and checks. A HeritageTech startup in UTH's programme could start on the same layer on its first day.

## What this does not claim

- **This is a proposal;** we have not spoken to UTH, and nothing is agreed.
- **None of these companies has worked on heritage yet;** every "for heritage" is a proposed use.
- **"Separate companies" is how I think about them;** their legal structure is not described here.

## Where this comes from

Our own sites: [sgit.ai](https://sgit.ai/), [pki.sgit.ai](https://pki.sgit.ai/), [sharness.ai](https://sharness.ai/), [abp.sgit.ai](https://abp.sgit.ai/), [riskmandate.ai](https://riskmandate.ai/), [agenticcells.ai](https://agenticcells.ai/), [gamma-ray.sgit.ai](https://gamma-ray.sgit.ai/), [voicedebrief.ai](https://voicedebrief.ai/) and [promptugal.news](https://promptugal.news/). UTH's form, [Let's build HeritageTech together](https://tally.so/r/PR9lOV), and the reporting in [HeritageTech, together](heritage-tech-together.md), 17 November 2026. Earlier on this site: [the intersection](the-intersection.md), [how a vault works](how-a-vault-works.md), [deploy sgit from CI](deploy-sgit-from-ci.md), [a key for every person](a-key-for-every-person.md), [introducing SHarness](introducing-sharness.md), [where assist becomes execute](where-assist-becomes-execute.md), [know the reach](know-the-reach.md), [the cell is the unit](the-cell-is-the-unit.md), [the site factory works](the-site-factory-works.md), [your own agentic cell](your-own-agentic-cell.md), [agents rating agents](agents-rating-agents.md), [build on VoiceDebrief](build-on-voicedebrief.md), [PrompTugal.news by place](promptugal-news-by-place.md), [native apps by agents](native-apps-by-agents.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#our-companies-and-uth)

### Builds on

- [HeritageTech, together: how our open-source stack could plug into UAlgTec Heritage, the University of the Algarve's new European centre of excellence for heritage science and technology, mapped from the dig to the museum, with encrypted evidence vaults per site, signed finds, graphs of every excavation, agents with written policies, and what I would write in its "start a conversation" form](heritage-tech-together.md) How our open-source trust stack could plug into UAlgTec Heritage, the Algarve's new European centre for heritage science and technology.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [Deploy sgit in your own environment, from a CI pipeline: one Docker image, ciphertext in your own S3 bucket in the region you choose, an access token only you hold, and the pipeline pattern we learned building the AgentiCCells site factory, a protected environment, AWS through OpenID Connect with no keys, a role that trusts one repository and one environment, check workflows before anything real, and a full cycle that deploys, tests and tears down](deploy-sgit-from-ci.md) Run your own sgit server in your own AWS account and region, deployed from CI with the site factory's pattern: OIDC, no keys, checks first.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [Know the Reach: RiskMandate has a song on Spotify, and its music video is being made with AI, shot by shot, from about 2,300 words of human direction; this is how the first part was made](know-the-reach.md) RiskMandate's song Know the Reach is on Spotify; the first 53 seconds of its video were made with AI from about 2,300 words of direction.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository](your-own-agentic-cell.md) How a person gets their own agentic cell: a key pair in the browser, a vault they fill themselves, the site factory, and then their own Claude.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.
- [Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code](build-on-voicedebrief.md) VoiceDebrief's techniques for any voice app: record without loss, transcribe offline, debrief with Apple Intelligence, voice control, CI.
- [PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI](promptugal-news-by-place.md) PrompTugal.news goes local: Portugal, the Algarve and every Algarve town, each on its own subdomain, each a lens on one graph, every story tied to AI.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 457 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=457)

**Posting this article on LinkedIn?** The cover is [our-companies-and-uth.jpg](banners/our-companies-and-uth.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/our-companies-and-uth.html)*
