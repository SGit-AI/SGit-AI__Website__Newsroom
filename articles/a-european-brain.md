# A European brain for a sovereign website: why the model is a choice the owner makes, like the host, how Mistral fits at every level, from Ministral 3 running on a Pi Pro to Mistral Small 4 on an EU endpoint for the team inside the site, what its terms say about where data goes, the one licence to watch, what we have already run on Mistral, and how we could work with it, sgit.ai

> When I shared the Sovereign Agentic Website idea, Angelo came back with the right challenge: if we really want to claim the word sovereign, abstract the AI provider, and let people use other models, including European ones such as Mistral. I agree completely. A site whose files are yours but whose brain can only be one American provider has a part in the middle that you do not control. So the model becomes a choice the owner makes, like the host: one standard interface, the OpenAI-style API that Mistral, OpenRouter and local servers all speak, and a European option at every level. On the Pro appliances, Ministral 3, an Apache 2.0 model built for the edge, running on the device. For the team inside the site, Mistral's API on its EU endpoint, where data is hosted in the EEA by default and API data is not used for training. For everything else, the owner's own key. We have already run Mistral in production without saying so: it was one of four open-weight models in the Swarm's 216 calls, and its free mode passed our browser test in October. The one thing to watch is licences: the Apache 2.0 models are clean, while Mistral Large 4 needs a commercial licence to be served as a service. And there is a partnership to propose.

*Source: <https://newsroom.sgit.ai/articles/a-european-brain.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A European brain for a sovereign website: why the model is a choice the owner makes, like the host, how Mistral fits at every level, from Ministral 3 running on a Pi Pro to Mistral Small 4 on an EU endpoint for the team inside the site, what its terms say about where data goes, the one licence to watch, what we have already run on Mistral, and how we could work with it

# A European brain for a sovereign website: why the model is a choice the owner makes, like the host, how Mistral fits at every level, from Ministral 3 running on a Pi Pro to Mistral Small 4 on an EU endpoint for the team inside the site, what its terms say about where data goes, the one licence to watch, what we have already run on Mistral, and how we could work with it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-20 · [article v1.0.0](versions/a-european-brain.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · sovereigntymistraleuropemodelssovereign-websiteopen-weightarticle

***Abstract:** When I shared the Sovereign Agentic Website idea, Angelo came back with the right challenge: if we really want to claim the word sovereign, abstract the AI provider, and let people use other models, including European ones such as Mistral. I agree completely. A site whose files are yours but whose brain can only be one American provider has a part in the middle that you do not control. So the model becomes a choice the owner makes, like the host: one standard interface, the OpenAI-style API that Mistral, OpenRouter and local servers all speak, and a European option at every level. On the Pro appliances, Ministral 3, an Apache 2.0 model built for the edge, running on the device. For the team inside the site, Mistral's API on its EU endpoint, where data is hosted in the EEA by default and API data is not used for training. For everything else, the owner's own key. We have already run Mistral in production without saying so: it was one of four open-weight models in the Swarm's 216 calls, and its free mode passed our browser test in October. The one thing to watch is licences: the Apache 2.0 models are clean, while Mistral Large 4 needs a commercial licence to be served as a service. And there is a partnership to propose.*

The brain is a choice too: a European option on the device, in the EU, and through any provider.

## In short

- **Angelo's challenge:** if we claim sovereign, abstract the AI provider.
- **The model is a choice the owner makes,** like the host.
- **Mistral at every level:** Ministral 3 on the device, Mistral Small 4 on an EU endpoint.
- **We have already run Mistral,** in the Swarm and in the browser.
- **One licence to watch:** Large 4 needs a commercial licence to be served as a service.
- **A partnership to propose,** with Europe at its heart.

## The challenge

When I sent Angelo the [Sovereign Agentic Website](sovereign-agentic-website.md) idea, his answer was short and right: if you really want to claim the word sovereign, abstract the AI provider part, and allow people to use other models and European AI like Mistral. That would be a very powerful sovereign play.

It follows from our own principles ([what is a sovereign website](what-is-a-sovereign-website.md)). One proprietary part in the middle is enough to lock a site in, and the model that builds and changes the site is a part in the middle. If it can only ever be one provider, the site is sovereign in its files and rented in its brain.

## The model is a choice

So the design is the one we already use for hosts: one standard interface, several providers. Mistral, OpenRouter and local model servers all speak the same OpenAI-style API; Mistral's own documentation shows its endpoint used with the OpenAI client ([chat completion](https://docs.mistral.ai/inference/conversations/chat-completion)). The agents and tools on a sovereign website call that interface, and the owner chooses what sits behind it:

- **On the device.** On the Pro appliances, a local model, so a site can be built and changed with nothing leaving the house ([launching the sovereign website appliance](launching-the-sovereign-website-appliance.md)).
- **In Europe.** A European provider for the team inside the site ([a website with a team inside](a-website-with-a-team-inside.md)).
- **Any provider.** The owner's own key, through OpenRouter, for Claude, Gemini, open-weight models, or Mistral's again.

## Mistral at every level

Mistral, a French company founded in April 2023 ([about](https://mistral.ai/about/)), now covers all three:

- **On the device: Ministral 3.** Released in December 2025 in 3B, 8B and 14B sizes, with text and vision, under Apache 2.0, and built for the edge ([Mistral 3](https://mistral.ai/news/mistral-3)). Our estimate, to test on [the Raspberry Pi](a-sovereign-website-on-a-raspberry-pi.md): the 3B and 8B, compressed to about 2 to 5GB, should run on a 16GB Pi 5, the 8B slowly; on a tablet, the 3B is the realistic one.
- **In Europe: Mistral's API.** Data is hosted in the EEA by default ([where data is stored](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)), with an EU endpoint generally available since August 2026 ([regional endpoints](https://mistral.ai/news/regional-inference-open-models-new-compute/)), and "data sent through our API isn't used for model training" ([inference](https://mistral.ai/cloud/inference/)). Ministral 3 8B is listed at 0.15 dollars per million tokens ([its page](https://docs.mistral.ai/models/ministral-3-8b-25-12)); Mistral Small 4, an Apache 2.0 model with 119 billion parameters, 6.5 billion active, at 0.15 and 0.60 ([its page](https://docs.mistral.ai/models/mistral-small-4-0-26-03)).
- **For voice:** the Story Studio's spoken answers ([the swarm](the-swarm-one-real-run-at-a-time.md)) could be transcribed by Mistral's Voxtral models, some open-weight and some on its API.
- **For agents:** function calling, structured outputs and an agents API ([function calling](https://docs.mistral.ai/studio/conversations/function-calling)), and connectors to remote MCP servers in preview ([connectors](https://docs.mistral.ai/studio/connectors/overview)).

## What its terms say

- **Retention:** API inputs and outputs are kept for 30 days for abuse monitoring, unless zero data retention is switched on ([privacy policy](https://legal.mistral.ai/terms/privacy-policy/)); that option is available on paid plans for stateless calls only, not for agents, conversations or files ([zero data retention](https://docs.mistral.ai/admin/monitor-comply/zero-data-retention.md)).
- **Where data goes:** some features may move data temporarily to processors outside the EU, which Enterprise customers can turn off ([where data is stored](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)).
- **Certifications:** Mistral states SOC 2 Type II and ISO 27001 and 27701 ([certifications](https://help.mistral.ai/en/articles/347638-do-you-have-soc-2-or-iso-27001-certification)).

## The licence to watch

Not every open-weight model is equally open. Ministral 3, Mistral Small 4 and Voxtral Small are Apache 2.0, which is as clean as it gets. Mistral Large 4 is under Mistral's own modified MIT licence, which allows commercial use but requires a separate commercial licence for a company serving it as a model-as-a-service ([Large 4](https://mistral.ai/news/mistral-large-4-oss/)). If we host models for customers' sites, that line matters. Apache 2.0 models first.

## We have already run it

We have used Mistral without making a point of it. In October, Mistral's free mode was one of four APIs that passed our test of what a reader can call from the browser with their own key ([free models, your own key](free-models-your-own-key.md)). And in the Swarm's scale run at Web Summit, 216 model calls on four open-weight models for 6.8 cents, one of the four was Mistral ([pennies against dollars](pennies-against-dollars.md)). What changes now is that it becomes a choice we offer on purpose, and name.

## Working with Mistral

What I would propose to Mistral is simple: Sovereign Website is a European product about owning what you depend on, and a European model is its natural default. Concretely:

- **A Mistral option on every site,** in the team inside and in the build page, where the same brief can run on Mistral beside other models as an open eval ([watch your website being built](watch-your-website-being-built.md)).
- **Ministral 3 on the Pro appliances,** measured on the Pi and published, which shows their edge models doing real work.
- **The European stretch goals of the Kickstarter,** each country with a European model behind it.
- **Credits for the evals and the demo sites,** and a joint story if it works.

Mistral lists strategic, ecosystem and integration partners ([partners](https://mistral.ai/partners/)) but no public application, so this starts as a conversation; its ambassador programme offers API credits to practitioners ([ambassadors](https://docs.mistral.ai/resources/ambassadors)).

## Not one company either

Sovereignty cannot rest on one company, European or not. France's finance minister said as much in September: "if European AI is just about Mistral, then we're doomed" ([reported](https://www.malaymail.com/amp/news/tech-gadgets/2026/09/03/were-doomed-french-minister-warns-against-relying-on-mistral-for-ai/233729)). Mistral's platform also serves models made elsewhere, and it has a large American partner in Microsoft ([the partnership](https://news.microsoft.com/source/2026/07/21/microsoft-and-mistral-expand-strategic-partnership-to-give-enterprises-and-regulated-industries-frontier-ai-they-can-control/)). That is why the design is a choice behind one interface, not a new dependency: Mistral as the European default, never the only door.

## What this does not claim

- **Nothing has been agreed with Mistral;** this is a proposal.
- **The fit on a Pi or a tablet is an estimate,** to be measured.
- **Terms and prices are as Mistral's pages showed on 20 November 2026;** the retention detail was read partly through a search snippet.

## Where this comes from

Angelo's reply to the Sovereign Agentic Website idea, my own thinking in writer-10's session on 20 November 2026, and Mistral's own pages linked above, read that day. Related: [what is a sovereign website](what-is-a-sovereign-website.md), [free models, your own key](free-models-your-own-key.md), [pennies against dollars](pennies-against-dollars.md), [a sovereign website on a Raspberry Pi](a-sovereign-website-on-a-raspberry-pi.md), [watch your website being built](watch-your-website-being-built.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#a-european-brain)

### Builds on

- [Sovereign Agentic Website: the name for what we have been building, a website built by agents and owned by the person it is for, an open pattern anyone can use without paying us as WordPress was, a hosted version on sovereignwebsite.site, and why sovereign and agentic are the two words that make it different from the web of 2000](sovereign-agentic-website.md) Sovereign Agentic Website: built by agents, owned by you; an open pattern anyone can use, and a hosted version on sovereignwebsite.site.
- [What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer](what-is-a-sovereign-website.md) What a sovereign website is: owned and movable, commodity only, seven principles, a maturity model from rented to proven, and every host.
- [Launching the sovereign website appliance: the plan for a Kickstarter campaign that sells a sovereign website on a configured Android tablet or a Raspberry Pi, five tiers from a £50 supporter to £1,000, the two Pro tiers running local AI models that can build a website on the device itself, the hardware we would buy in the UK today, a European tablet, the UK as the base goal with countries and iOS as stretch goals, and why we launch alone](launching-the-sovereign-website-appliance.md) The Kickstarter plan: a sovereign website on a Raspberry Pi or a tablet, five tiers from £50 to £1,000, local AI on the Pro tiers.
- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.
- [A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes](a-sovereign-website-on-a-raspberry-pi.md) The experiment: a sovereign website, its local model, its build and its signed updates, all on one Raspberry Pi 5 at home.
- [The swarm, one real run at a time: the Web Summit demo that showed agents, the loops they start and the model calls they make, run for real, signed and replayed, step by step from one person and one agent to 24 loops at once, 216 model calls for 6.8 cents, the same work under a harness with 3 of 12 risky actions still possible instead of 11, and the Story Studio, where a spoken answer became a deck in front of you](the-swarm-one-real-run-at-a-time.md) The Swarm from Web Summit: agents run for real, signed and replayed, 216 model calls for 6.8 cents, a harness test, and a voice-to-deck studio.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.
- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from](watch-your-website-being-built.md) A page that builds a first version of a sovereign website in your browser, showing every agent, behaviour policy and penny, then hands back a zip.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 514 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=514)

**Posting this article on LinkedIn?** The cover is [a-european-brain.jpg](banners/a-european-brain.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-european-brain.html)*
