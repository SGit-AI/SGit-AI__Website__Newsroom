# Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist, sgit.ai

> We write behaviour policies for agents and, since php2shell, for applications. I think the next step is to write them for every feature. When we hand someone a new feature to test, we usually hand them the whole app; instead we could hand them the feature's behaviour policy, which says what the feature is for and what it does. That policy is the feature's description, and the difference between two versions of it is what changed. It is also what the application enforces, in context, because the same behaviour can be fine in one place and a serious problem in another. Enforced on the client, it cuts the noise that reaches the server; signed and carried with each request, it lets the server, and anyone watching the traffic, see a bug or an attack as a path outside the policy. The reverse is a resource behaviour policy: everything a key, an account or an API lets you do. The gap between the two is the risk, and the application, where features combine, is where new behaviour appears. Agent and user behaviour policies are then the same feature policies plus a workflow; only who runs them differs. Policies become the permission sets for the custom interfaces we build per task. Next, we map them onto our own capabilities.

*Source: <https://newsroom.sgit.ai/articles/feature-behaviour-policies.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist

# Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/feature-behaviour-policies.md) · [newsroom v0.14.167](https://newsroom.sgit.ai/admin/versions.html) · behaviour-policiesabpsecurityfeaturestestingsigningagentsarticle

***Abstract:** We write behaviour policies for agents and, since php2shell, for applications. I think the next step is to write them for every feature. When we hand someone a new feature to test, we usually hand them the whole app; instead we could hand them the feature's behaviour policy, which says what the feature is for and what it does. That policy is the feature's description, and the difference between two versions of it is what changed. It is also what the application enforces, in context, because the same behaviour can be fine in one place and a serious problem in another. Enforced on the client, it cuts the noise that reaches the server; signed and carried with each request, it lets the server, and anyone watching the traffic, see a bug or an attack as a path outside the policy. The reverse is a resource behaviour policy: everything a key, an account or an API lets you do. The gap between the two is the risk, and the application, where features combine, is where new behaviour appears. Agent and user behaviour policies are then the same feature policies plus a workflow; only who runs them differs. Policies become the permission sets for the custom interfaces we build per task. Next, we map them onto our own capabilities.*

A tree of behaviour policies: resources, features and fixes, the application, and the agents and users who run it.

## In short

- **Test a feature, not an app:** hand the tester the feature's behaviour policy.
- **The policy is the description,** and what changed is the difference between two policies.
- **Context decides** whether a behaviour is fine or a problem; the policy carries the context.
- **Enforce it at every layer.** On the client it cuts the noise; signed on each request, it makes a bug or an attack a path outside the policy.
- **Resources have policies too:** everything a key or an API lets you do. The gap between that and what the feature needs is the risk.
- **Agent and user behaviour policies** are feature policies plus a workflow; only who runs them differs.

## Test a feature, not an app

When we ask someone to test something, we usually think in terms of the application: here is the app, the website, the iOS build, go and test it. But what changed was one feature, or one new capability. I think the unit we hand over should be that feature, with its behaviour policy: what it is for, what it does, what it reads and writes, who may use it, and what it must never do.

That policy is also the feature's description. Ask "what does it do?" and the answer is in the policy. Ask "what changed?" and the answer is the difference between this version of the policy and the last. A tester can start from the policy, and a tool can build the environment to test it in: the data, the permissions and the starting state that the policy names.

## Context decides

The hard part of security, and of every decision about what to enforce, has always been understanding the behaviour: the business logic, what we are trying to do, and the context. The same behaviour can be fine in one place and a serious problem in another. Exporting a customer list is a feature in the CRM and an incident in the public newsletter page.

A behaviour policy written per feature carries that context with it. It is the mandate, in the words we already use for agents and applications ([application behaviour policies](application-behaviour-policies.md)): reach is what something can do, mandate is what you asked it to do, and the gap between them is where the risk lives.

## Enforce it everywhere

A policy that says what a feature does can be enforced wherever the feature runs, client side included. The usual reply is that client-side checks can always be bypassed, and they can. But they still do something valuable: they cut the noise. If the client only sends what the feature's policy allows, the traffic that reaches the server is the traffic the features meant to send. Everything else stands out.

A client sends a request with its signed policy; an observer and the server check that the request fits.

Now sign the policies, as we are starting to sign everything, commits and code included. A request from the client can carry the policy, or the policies, it is acting under. The server can check the request against them. And someone who does not have the whole context, an observer looking at the traffic, can still look at a request and its policy and say: this does not make sense, this is not supposed to happen here.

That changes what a bug or an attack looks like. Both are a path that was never supposed to exist: a request outside the policy, a step the feature does not have. The pieces of the pipeline that can see the policy can find it.

## The resource side

There is a reverse to the feature policy. Take a key that gives access to a service, an OAuth grant to a mailbox, or a model API behind a key. Our cloud sessions now hold keys this way: a key is saved for a host, and the network proxy adds it to requests to that host, so the session never sees the key. That is a good step. But once the request is authorised, the service at the other end can do far more than the one call we wanted.

I would call that a resource behaviour policy: everything the resource lets you do. It is the reach, written from the receiving side. A vulnerability, in these terms, is a way to bypass it, but it still describes behaviour, and still says what can be done.

Put the two side by side and the method is the one we already use. The resource behaviour policy is the reach; the feature behaviour policy is the mandate; the difference between them is the gap. That gap is where the vulnerabilities live. And the application behaviour policy, the features combined, is where some of them only appear: behaviour that no single feature has, that shows up only when two or three are connected.

## Bugs, too

A bug fix is a change of behaviour as well, so it can have a policy too: the path it closes, what it must leave as it was, and what it must not open. Fixes then join the same tree, and "what changed in this release" reads the same way for a feature and for a fix.

## Agents, users and interfaces

Seen this way, an agent behaviour policy is a combination of these smaller policies, the features and resources the agent may use, together with the workflow we want it to follow. A user behaviour policy is almost the same thing. The difference is who is executing it, and what drives them.

That also fits where our interfaces are going. We are building more of them per task, per person and per focus, rather than one app for everyone ([a browser for one](a-browser-for-one.md)). Behaviour policies are what define what each of those interfaces may do, and what must be enforced. In practice the policies become the permission sets, and an interface can be built from the policies it is allowed to carry.

## What comes next

We should start using this on our own capabilities now. Two examples:

- **The factory's CI changes.** Our agents can now change CI pipelines in the site factory. That deserves a feature behaviour policy (create this repository, make this change, nothing else), signed, and given to the code and the agents that enforce it.
- **Keys injected by host.** Each saved key should be linked to the features that need it, the resource behaviour policy of the service it opens, and the permissions those features actually use.

I am asking the agent that maintains our agent behaviour policies to map where this applies across the team's capabilities. I think there are several more articles in this: one per kind of policy, and one on the gap between a resource and a feature, measured on a real key.

## What this does not claim

- **These are proposals,** not a standard or a finished tool; the words follow the behaviour policies published at abp.sgit.ai.
- **Client-side enforcement is not a boundary;** its value here is cutting noise so the rest stands out.
- **Signing policies on requests is not built yet;** the commits of this newsroom's writer are signed as of 19 November 2026.

## Where this comes from

My own thinking, dictated on 19 November 2026, building on [application behaviour policies](application-behaviour-policies.md) (22 October 2026) and the behaviour policies at [abp.sgit.ai](https://abp.sgit.ai/). Related: [approve at altitude](approve-at-altitude.md), on decisions that may narrow the level above and never widen it, and [a page we never charge](a-page-we-never-charge.md), a resource's terms checked against a feature before anything was built.

## Threads

Agents & policy[This article as a graph →](graphs.md#feature-behaviour-policies)

### Builds on

- [Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius](application-behaviour-policies.md) Map an application the way we map an agent, so a site switched off for php2shell can come back with a known blast radius.
- [A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working](a-browser-for-one.md) An iPhone app that only reads my newsroom: WebKit in the UK, a paid membership and a Mac to build it, one passkey test first, and someone else to maintain it.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits](a-page-we-never-charge.md) YouTube forbids charging to watch an embedded player, so promptugal.news, which bills, will show the replays on a page it never charges.

### Continued by

- [LangGraph and us: how the way we build agent pipelines maps to LangChain, LangGraph, LangSmith and the agent testing toolkits, what is the same, what we do differently, code for each function and every step saved to a vault, what we can learn from them, and where they could run inside our own pipelines](langgraph-and-us.md) How our agent pipelines map to LangGraph, LangChain and the eval toolkits: the same ideas, a more deterministic default, and what to learn and use.
- [One night on Mistral: how an agent team turned "a European brain for a sovereign website" into a working site overnight, for the Mistral Vibe Hackathon in London, with 33 demos in the browser, from a shoebox of files to a website and five Mistral models drawn side by side, evals that found which model catches a scam note, the Swarm moved onto Mistral, about 41 cents of Mistral usage, and why this is where I want to start working with Mistral](one-night-on-mistral.md) An agent team turned the European brain article into a working Mistral site overnight: 33 browser demos, evals, the Swarm on Mistral, about 41 cents.
- [The way in: why sovereign websites matter so much to RiskMandate, what Web Summit validated and what it showed was missing, something to buy now, how every technology I have been building meets in one product, and why nobody deploys agents they have not touched, seen and been able to stop, so the personal customer becomes the way to the corporate one](the-way-in.md) Why sovereign websites are the way into RiskMandate: something to buy now, where people touch agents under policies before they bring them to work.
- [The first round trip: a sovereign website made for Kate Curtis-Evans during our call, five designs from a design agent of its own, then handed over so she edits it herself from her own Claude, the friction that took multiple rounds to get through, what it says about over-privilege, and the next step, a signed and sealed channel from her site straight to the agent](the-first-round-trip.md) The first round trip of Sovereign Website with someone from outside: a site made during a call, handed over, and edited by its owner's own Claude.
- [Transcription for a sector, sold as a team: extending VoiceDebrief with what we have learnt from sovereign websites, a bundle for one industry, a repository the customer's own AI runs, with the whole pipeline from dropping a recording to a reviewed document and a team of agents certified by people from that sector, sold by small AI companies who know the industry, open source underneath, from £50 to £5,000](transcription-for-a-sector.md) Transcription for one sector, sold as a bundle: a repository the customer's own AI runs, with a team of agents certified by people from the sector.
- [The RiskMandate X-ray: type a company's name and see what its AI helpers can reach, what they were asked to do and where the two do not match, how four search agents and a collector built it for the stand at Web Summit, why only facts whose sources were read reach the page, what it cost, about 1.13 dollars for thirteen companies, and how the four models compared on accuracy](the-riskmandate-x-ray.md) The RiskMandate X-ray: type a company, see its AI helpers' reach, mandate and gap, built by four search agents for about a dime a company.
- [A galaxy of agents: the Universe we showed at Web Summit, a live 3D solar system of the RiskMandate team where people are suns, their agents orbit them and their messages travel between them as arcs of light, read from the repositories as it happens, with each agent's behaviour policy one click away, and Gravity, the library it became, which can draw any system the same way](a-galaxy-of-agents.md) The Galaxy from Web Summit: the RiskMandate team as a live 3D solar system of people, agents and messages, and the library it became.
- [What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer](what-is-a-sovereign-website.md) What a sovereign website is: owned and movable, commodity only, seven principles, a maturity model from rented to proven, and every host.
- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.
- [Designing sovereignwebsite.ai: the brief for the team that will build the site of our first mass-market product, how the stack now has four layers, SGit, RiskMandate, AgentiCCells and Sovereign Website, six ways to say what it is, the ten pages, the sovereignty maturity model at its centre, how to build the site as a sovereign website itself, and five homepage designs to choose from](designing-sovereignwebsite-ai.md) The brief for sovereignwebsite.ai: a four-layer stack, six messages, ten pages, the sovereignty maturity model and five designs.
- [Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open](policies-in-practice.md) Four uses of feature behaviour policies: a real key's gap, signed CI changes, requests carrying policies, and release notes as fixes.
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, change or delete every repository in the organisation and to point any subdomain anywhere, and why pipelines now need the same behaviour policies as agents](ci-behaviour-policies.md) Our site factory's pipeline needs one repository and one DNS record per request, yet holds power over the whole organisation. Pipelines need ABPs too.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 490 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=490)

**Posting this article on LinkedIn?** The cover is [feature-behaviour-policies.jpg](banners/feature-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/feature-behaviour-policies.html)*
