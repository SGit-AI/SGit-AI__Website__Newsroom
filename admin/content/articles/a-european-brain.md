---
title: A European brain for a sovereign website: why the model is a choice the owner makes, like the host, how Mistral fits at every level, from Ministral 3 running on a Pi Pro to Mistral Small 4 on an EU endpoint for the team inside the site, what its terms say about where data goes, the one licence to watch, what we have already run on Mistral, and how we could work with it
date: 2026-11-20
author: Dinis Cruz
author_url: about/index.html
summary: When I shared the Sovereign Agentic Website idea, someone I sent it to came back with the right challenge: if we really want to claim the word sovereign, abstract the AI provider, and let people use other models, including European ones such as Mistral. I agree completely. A site whose files are yours but whose brain can only be one American provider has a part in the middle that you do not control. So the model becomes a choice the owner makes, like the host: one standard interface, the OpenAI-style API that Mistral, OpenRouter and local servers all speak, and a European option at every level. On the Pro appliances, Ministral 3, an Apache 2.0 model built for the edge, running on the device. For the team inside the site, Mistral's API on its EU endpoint, where data is hosted in the EEA by default and processing stays in the EU, on its EU endpoint, at a small premium, and the owner can opt out of API data being used for training. For everything else, the owner's own key. We have already run Mistral in production without saying so: it was one of four open-weight models in the Swarm's 216 calls, and its free mode passed our browser test in October. The one thing to watch is licences: the Apache 2.0 models are clean, while Mistral Large 4 needs a commercial licence to be served as a service. And there is a partnership to propose.
version: v0.14.184
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereignty, mistral, europe, models, sovereign-website, open-weight, article
status: published
---

!shot mis-layers.webp | images/ | The brain is a choice too: a European option on the device, in the EU, and through any provider. | concept

## In short {#in-short}

- **The challenge:** if we claim sovereign, abstract the AI provider.
- **The model is a choice the owner makes,** like the host.
- **Mistral at every level:** Ministral 3 on the device, Mistral Small 4 on an EU endpoint.
- **We have already run Mistral,** in the Swarm and in the browser.
- **One licence to watch:** Large 4 needs a commercial licence to be served as a service.
- **A partnership to propose,** with Europe at its heart.

## The challenge {#challenge}

When I sent the [Sovereign Agentic Website](/articles/sovereign-agentic-website.html) idea to someone who works in this field, the answer was short and right: if you really want to claim the word sovereign, abstract the AI provider part, and allow people to use other models and European AI like Mistral. That would be a very powerful sovereign play.

It follows from our own principles ([what is a sovereign website](/articles/what-is-a-sovereign-website.html)). One proprietary part in the middle is enough to lock a site in, and the model that builds and changes the site is a part in the middle. If it can only ever be one provider, the site is sovereign in its files and rented in its brain.

## The model is a choice {#choice}

So the design is the one we already use for hosts: one standard interface, several providers. Mistral, OpenRouter and local model servers all speak the same OpenAI-style API; Mistral's own documentation shows its endpoint used with the OpenAI client ([chat completion](https://docs.mistral.ai/inference/conversations/chat-completion)). The agents and tools on a sovereign website call that interface, and the owner chooses what sits behind it:

- **On the device.** On the Pro appliances, a local model, so a site can be built and changed with nothing leaving the house ([launching the sovereign website appliance](/articles/launching-the-sovereign-website-appliance.html)).
- **In Europe.** A European provider for the team inside the site ([a website with a team inside](/articles/a-website-with-a-team-inside.html)).
- **Any provider.** The owner's own key, through OpenRouter, for Claude, Gemini, open-weight models, or Mistral's again.

## Mistral at every level {#levels}

Mistral, a French company founded in April 2023 ([about](https://mistral.ai/about/)), now covers all three:

- **On the device: Ministral 3.** Released in December 2025 in 3B, 8B and 14B sizes, with text and vision, under Apache 2.0, and built for the edge ([Mistral 3](https://mistral.ai/news/mistral-3)). Our estimate, to test on [the Raspberry Pi](/articles/a-sovereign-website-on-a-raspberry-pi.html): the 3B and 8B, compressed to about 2 to 5GB, should run on a 16GB Pi 5, the 8B slowly; on a tablet, the 3B is the realistic one.
- **In Europe: Mistral's API.** Data is hosted in the EEA by default ([where data is stored](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)), with an EU endpoint generally available since August 2026 ([regional endpoints](https://mistral.ai/news/regional-inference-open-models-new-compute/)). Hosting is not processing: inference stays in the EU only on the EU endpoint, api.eu.mistral.ai, billed at 1.1 times list price ([regional inference](https://docs.mistral.ai/inference/regional-inference)). Its inference page says "data sent through our API isn't used for model training" ([inference](https://mistral.ai/cloud/inference/)), but in Free mode Mistral may use inputs and outputs for training unless you opt out ([its help centre](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)). Ministral 3 8B is listed at 0.15 dollars per million tokens ([its page](https://docs.mistral.ai/models/ministral-3-8b-25-12)); Mistral Small 4, an Apache 2.0 model with 119 billion parameters, 6.5 billion active, at 0.15 and 0.60 ([its page](https://docs.mistral.ai/models/mistral-small-4-0-26-03)).
- **For voice:** the Story Studio's spoken answers ([the swarm](/articles/the-swarm-one-real-run-at-a-time.html)) could be transcribed by Mistral's Voxtral models, some open-weight and some on its API.
- **For agents:** function calling, structured outputs and an agents API ([function calling](https://docs.mistral.ai/studio/conversations/function-calling)), and connectors to remote MCP servers in preview ([connectors](https://docs.mistral.ai/studio/connectors/overview)).

## What its terms say {#terms}

- **Retention:** API inputs and outputs are kept for 30 days for abuse monitoring, unless zero data retention is switched on ([privacy policy](https://legal.mistral.ai/terms/privacy-policy/)); zero data retention is for pay-as-you-go accounts only, on request, for stateless calls, and not for agents, conversations or files ([privacy policy](https://legal.mistral.ai/terms/privacy-policy/)).
- **Where data goes:** some features may move data temporarily to processors outside the EU, which Enterprise customers can turn off ([where data is stored](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)).
- **Certifications:** Mistral states SOC 2 Type II and ISO 27001 and 27701 ([certifications](https://help.mistral.ai/en/articles/347638-do-you-have-soc-2-or-iso-27001-certification)).

## The licence to watch {#licence}

Not every open-weight model is equally open. Ministral 3, Mistral Small 4 and Voxtral Small are Apache 2.0, which is as clean as it gets. Mistral Large 4 is under Mistral's own modified MIT licence, which allows commercial use but requires a separate commercial licence for a company serving it as a model-as-a-service ([Large 4](https://mistral.ai/news/mistral-large-4-oss/)). If we host models for customers' sites, that line matters. Apache 2.0 models first.

## We have already run it {#already}

We have used Mistral without making a point of it. In October, Mistral's free mode was one of four APIs that passed our test of what a reader can call from the browser with their own key ([free models, your own key](/articles/free-models-your-own-key.html)). And in the Swarm's scale run at Web Summit, 216 model calls on four open-weight models for 6.8 cents, one of the four was Mistral ([pennies against dollars](/articles/pennies-against-dollars.html)). What changes now is that it becomes a choice we offer on purpose, and name.

## Working with Mistral {#collaborate}

What I would propose to Mistral is simple: Sovereign Website is a European product about owning what you depend on, and a European model is its natural default. Concretely:

- **A Mistral option on every site,** in the team inside and in the build page, where the same brief can run on Mistral beside other models as an open eval ([watch your website being built](/articles/watch-your-website-being-built.html)).
- **Ministral 3 on the Pro appliances,** measured on the Pi and published, which shows their edge models doing real work.
- **The European stretch goals of the Kickstarter,** each country with a European model behind it.
- **Credits for the evals and the demo sites,** and a joint story if it works.

Mistral lists strategic, ecosystem and integration partners and has a public "Partner with Mistral" form ([partners](https://mistral.ai/partners/)), so this can start there; its ambassador programme offers API credits to practitioners ([ambassadors](https://docs.mistral.ai/resources/ambassadors)).

## Not one company either {#not-one}

Sovereignty cannot rest on one company, European or not. France's finance minister said as much in September: "if European AI is just about Mistral, then we're doomed" ([reported](https://www.malaymail.com/amp/news/tech-gadgets/2026/09/03/were-doomed-french-minister-warns-against-relying-on-mistral-for-ai/233729)). Mistral's platform also serves models made elsewhere, and it has a large American partner in Microsoft ([the partnership](https://news.microsoft.com/source/2026/07/21/microsoft-and-mistral-expand-strategic-partnership-to-give-enterprises-and-regulated-industries-frontier-ai-they-can-control/)). That is why the design is a choice behind one interface, not a new dependency: Mistral as the European default, never the only door.

## What this does not claim {#limits}

- **Nothing has been agreed with Mistral;** this is a proposal.
- **The fit on a Pi or a tablet is an estimate,** to be measured.
- **Terms and prices are as Mistral's pages showed on 20 November 2026;** the retention detail was read partly through a search snippet.
- **Corrected on 21 November:** the research agent that built [Mistral's provider site](https://mistral.provider.sovereignweb.site/) found that Free mode may train on API data, that EU processing needs the EU endpoint, that zero data retention is pay-as-you-go only, and that there is a public partner form. Each is fixed above.

## Where this comes from {#sources}

A reply to the Sovereign Agentic Website idea, my own thinking in writer-10's session on 20 November 2026, and Mistral's own pages linked above, read that day. Related: [what is a sovereign website](/articles/what-is-a-sovereign-website.html), [free models, your own key](/articles/free-models-your-own-key.html), [pennies against dollars](/articles/pennies-against-dollars.html), [a sovereign website on a Raspberry Pi](/articles/a-sovereign-website-on-a-raspberry-pi.html), [watch your website being built](/articles/watch-your-website-being-built.html).
