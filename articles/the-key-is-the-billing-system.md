# The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it, sgit.ai

> VoiceDebrief.ai turns a voice note into a transcript, a translation and a debrief in one pass, in the browser, on the user's own OpenRouter key, with no account, no server and nothing stored; a 42-second note costs about a third of a penny. It was built in the open in three weeks of August 2026, 239 commits and 27 releases in the first three weeks, and then it stopped: eleven commits the week after, three the week after that. The handbrake was the commercial model, which was never meant to be a billing system. A user pays five pounds, we keep our cut at the moment of payment, and the rest becomes the credit limit on a key we hand them; the provider meters it and there is nothing of ours to run. OpenRouter's Management API describes that mechanism, "unique API keys for each customer instance", and OpenRouter's terms forbid using it to resell access to models, so the plan was dead on the page that documented it. This is the same shape as the Agent Desk finding, where Apple's licence stops a Mac being leased for less than a day: the product is possible, the licence is the blocker. This article is the state of the union: what runs, why no server is not a preference but the product, what a backend would cost in complexity, what every speech-to-text provider's terms and docs say about a capped key in a user's hand, and the four routes left. ElevenLabs is the nearest fit, with per-key credit limits, OEM terms for making the service available to end users, and a grants programme. It ends with the brief for the agents that will write to the providers, with one sentence to ask each of them.

*Source: <https://newsroom.sgit.ai/articles/the-key-is-the-billing-system.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it

# The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/the-key-is-the-billing-system.md) · [sgit.ai v0.7.71](https://sgit.ai/admin/versions.md) · voicedebriefno-serverclient-sidebyokapi-keysbillingopenrouterelevenlabsspeech-to-textlicensingstartupsbriefarticle

***Abstract:** VoiceDebrief.ai turns a voice note into a transcript, a translation and a debrief in one pass, in the browser, on the user's own OpenRouter key, with no account, no server and nothing stored; a 42-second note costs about a third of a penny. It was built in the open in three weeks of August 2026, 239 commits and 27 releases in the first three weeks, and then it stopped: eleven commits the week after, three the week after that. The handbrake was the commercial model, which was never meant to be a billing system. A user pays five pounds, we keep our cut at the moment of payment, and the rest becomes the credit limit on a key we hand them; the provider meters it and there is nothing of ours to run. OpenRouter's Management API describes that mechanism, "unique API keys for each customer instance", and OpenRouter's terms forbid using it to resell access to models, so the plan was dead on the page that documented it. This is the same shape as the Agent Desk finding, where Apple's licence stops a Mac being leased for less than a day: the product is possible, the licence is the blocker. This article is the state of the union: what runs, why no server is not a preference but the product, what a backend would cost in complexity, what every speech-to-text provider's terms and docs say about a capped key in a user's hand, and the four routes left. ElevenLabs is the nearest fit, with per-key credit limits, OEM terms for making the service available to end users, and a grants programme. It ends with the brief for the agents that will write to the providers, with one sentence to ask each of them.*

What each provider's terms and docs say, in October 2026, about a capped key in a user's hand, and the four routes: the one that was planned and forbidden, the one to ask for, the one that runs today, and the backend the product was built to avoid.

This is the second article on this site with the same underlying theme, and I did not plan to write it twice. In [An agent desktop by the minute](an-agent-desktop-by-the-minute.md) we set out to rent a Mac to an agent for the minutes it works, found that every technical piece existed, and found that Apple's macOS licence forbids leasing a Mac for less than a day. The product was possible; the licence was the blocker. This article is about [VoiceDebrief](https://voicedebrief.ai/), a product I am also involved in, where the same thing happened to the commercial model, and where I want to map what is possible, who could allow it, and what to ask them.

## In short

- **VoiceDebrief works.** Drop a voice note or any audio file; get a transcript, a translation, a debrief and, if you ask, an infographic, in one pass, in your browser, on your own OpenRouter key. No account, no upload to us, nothing stored. A 42-second note costs about a third of a penny.
- **No server is the product, not a preference.** We never see the audio, so there is nothing to govern, leak, maintain, scale or be woken up for. The newsroom now runs the same way, and so does the reader's vault.
- **The commercial model was never meant to be a billing system.** A user pays five pounds; we keep our cut at the moment of payment; the rest becomes the credit limit on a key we hand them; the provider meters it. The model is a property of the key.
- **That is exactly what OpenRouter's Management API describes, and exactly what its terms forbid.** "Unique API keys for each customer instance" in the docs; "reselling API access to Models" in section 7(4) of the terms. The plan stopped there, and so did the project's commit history.
- **Most speech-to-text providers cannot do it either**, for a different reason: their keys do not carry a spend cap. Groq, Mistral and OpenAI cap the organisation or the workspace; Deepgram's keys expire but do not meter; AWS budgets act after the fact.
- **ElevenLabs is the nearest fit.** Per-key credit limits in the docs, OEM terms that let a business make the service available to its own end users at its own price, Scribe at $0.22 an hour, and a grants programme of twelve months for startups with a monetised use. What is missing is a sentence that says a capped key may be handed to a user who paid us.
- **Four routes remain**: the forbidden one; the one to ask for; the bring-your-own-key page that runs today; and a metering proxy, which is the backend the product exists to avoid.
- **The ask to every provider is one sentence.** Let the credit limit be a property of a key that a user can buy, so that we never hold the audio and never run the meter. The brief for the agents that will send it is at the end.

## What VoiceDebrief is

voicedebrief.ai on 12 October 2026. One recording in, four artefacts out, in the browser, on the user's own key; the maximum a pass can cost is quoted before it starts.

The home page says it in one line: "Drop a voice note or an audio file. Get the debrief. One pass, in your browser. No account, no upload to us, nothing to install." The file format is read from the bytes, not the name, so a WhatsApp voice message, an iPhone memo, an Android recording, a meeting export or a dictaphone file all work. The page asks for the key when you press run, quotes the maximum a pass can cost before it starts, and keeps nothing when you close the tab. A workbench on its own page does everything else: ask questions of the transcript, read the declared workflow with the model each step uses and its spending ceiling, see every raw call to OpenRouter with its tokens and cost, edit the prompts. There is also a WhatsApp number: forward a voice message and a transcription comes back, through an n8n workflow behind a Cloudflare Worker, which is the one part of the product with a server, and it is not the part this article is about.

It was built in the open, and the repository says how fast. The first commit is on 28 July 2026. The week beginning 27 July has 48 commits and 14 tagged releases; the week of 3 August, 127 commits and 10 releases; the week of 10 August, 64 commits and 3 releases. The updates page, written by the team's Journalist role as it happened, has its last entries on 14 August: a running pass that shows its work and can be stopped, five colour schemes, the infographic fixed, the library menu repaired. Then the week of 17 August has no commits at all. The week after, eleven. Then three. The last commit is on 7 September, a release record. Two hundred and fifty-seven commits and thirty-two tags, and a handbrake you can see from across the room.

## Why no server is the product

The page that gets a user from nothing to a working key, and its one instruction in bold: set a credit limit on the key, because a key with a limit cannot cost you more than the limit. The ceiling is the user's, not ours.

I want to be exact about why the product has no server, because it is easy to read as a preference, or as laziness from someone who builds backends for breakfast. It is neither. It is the product.

With no server, we never see the audio. That one fact removes, at a stroke: data custody and the governance that comes with it; a place where a breach can happen; a shared key that an abuser could drain; key management on our side; a billing system; a database of users; a thing that has to scale; a single point of failure; a thing that has to be up at three in the morning, and a person to wake. The page is static. As long as GitHub Pages or an S3 bucket is serving it, it is up, for one user or a million, at the same cost, which is nothing. The user's key is in their browser's storage, with a ceiling they set and can revoke in one click at the provider, and we are not in the payment path, so we add no margin and could not add one if we wanted to.

Add a server, and every item on that list comes back at once. Not gradually: at once. The moment audio passes through something we run, we hold it, we must govern it, we can be breached for it, we must meter it, bill for it, scale it and watch it. That is not one feature; it is a different company, with a different cost base and a different risk register. [No server, by design](no-server-by-design.md) made this case for the newsroom, and the newsroom has kept to it through a reading meter, personas, reading lists, a wire read from another agent's vault, and now [a reader's vault opened with a passkey](the-vault-is-live.md), with nothing of ours running anywhere. VoiceDebrief is the same pattern, one product earlier, and the reason it matters is that the complexity of the moving parts is what decides how fast you can move. The commit history above is what moving fast looks like. What stopped it was not a server. It was the lack of one.

## The commercial model that was never a billing system

The model was written down on 28 July, the day the product started, in a brief whose heading I still like: "Billing by not building billing." A user buys credit with a card, through a Stripe link. A one-shot workflow then creates a key for that user whose credit limit is their share of what they paid, and hands it over. The provider meters consumption against that limit; when it is spent, the key stops. Our take is a fixed share of the net, kept at the moment of payment. There is a float, because all the keys draw on one pooled balance that we pre-fund, and there is a minimum top-up of five pounds, because a card fee with a fixed component makes a one-pound purchase return about 59 pence of inference. Everything else is the provider's problem, by design.

Compare the two shapes, because the comparison is the argument. On one side: a billing system that meters every call, keeps a ledger per user, handles disputes, refunds, abuse and fraud, holds the audio while it meters, and charges a bit at a time. On the other: a payment, a cut, a key with a ceiling, and nothing else. The second is not only simpler to build; it is more profitable per pound, because the margin is taken once, up front, and never has to be collected. It is why a router like OpenRouter does well: it sells credit, keeps a margin, and meters on behalf of everyone else.

And OpenRouter has the mechanism. Its [Management API](https://openrouter.ai/docs/features/provisioning-api-keys) creates keys with an optional credit limit, a limit that can reset daily, and usage counters per key, and its own docs list the use case: SaaS applications that "Automatically create unique API keys for each customer instance", and "Track key usage and automatically disable keys that exceed limits." The plan was written against those docs. The [terms of service](https://openrouter.ai/terms), last updated 31 August 2026, say in section 7(4) that you may not "access the Site or Service for purposes of reselling API access to Models or otherwise developing a competing service", in 4.4 that "Credits are non-transferable, including between accounts", and in 7(14) that you may not sell or transfer the access granted. A Hacker News thread from about six months ago quotes the same reselling clause, so I cannot say from outside whether the 31 August update changed it or whether it was there and we built against the docs rather than the terms. The effect is the same. The enterprise agreement, separately, grants a licence to make the service available to a customer's own end customers and bars renting or reselling it, which reads as a door that an agreement could open and the standard terms keep shut.

So a product that could sell a five-pound key tomorrow with no server cannot, and the alternative, a backend that buys credit wholesale and meters it per user, is the company we did not want to be. That is the handbrake in the commit history, and it is why the memo that started this article asked for a map.

## The map: every provider, from their own pages

What matters for the model is two things per provider: can a single key carry a spend ceiling, and may that key be handed to a user who paid us. The table in the figure is from the providers' own terms, docs and pricing pages, read on 12 October 2026, and I will say where a page did not answer.

- **OpenRouter.** Per-key limits: yes, and designed for exactly this. Handing a key to a customer: forbidden by the standard terms, possibly permitted under an enterprise agreement. Audio: through the models that take it. Startup programme: none found.
- **ElevenLabs.** Per-key limits: yes. The [API keys page](https://elevenlabs.io/docs/overview/administration/workspaces/api-keys) lists three restrictions on a key, "Scope restriction: limit which API endpoints the key can access", "Credit quota: set a custom credit limit to control usage", and IP allowlisting, and the docs show a key stopping at its own limit while the account still has credit. Speech to text: Scribe v2 at $0.22 an hour batch and $0.39 realtime, with four and a half hours free, billed in dollars not credits. Handing a key to a user: the [terms](https://elevenlabs.io/terms-of-use) of 9 October 2026 make the licence non-sublicensable, say "You may not share or permit others to use your individual account credentials", and make prepaid credits non-transferable; but ElevenLabs also publishes [OEM terms](https://elevenlabs.io/oem-terms), under which a business entity on Scale or above may "Make Available" the services to its own end users, with an end-user agreement, and "Customer will independently establish the subscription price of the Bundled Service for its End Users." That is the closest any provider comes to our model in writing. Startup programme: [Grants](https://elevenlabs.io/grants), twelve months, 33 million characters, for companies under 25 people with a monetised use case; characters "cannot be exchanged or resold".
- **AssemblyAI.** Universal models at about $0.15 to $0.21 an hour. Keys belong to projects and carry rate and concurrency limits; I found no spend cap on a key. A startup programme of twelve months of recurring credits. I did not find its resale terms.
- **Deepgram.** Nova-3 at about $0.26 an hour batch. Keys can be set to expire by date or duration, and the docs recommend 30-second tokens for client-side use, but there is no spend cap on a key. The terms forbid making the service available "on a stand-alone basis" and allow integration into a product that adds "meaningful functionality", which VoiceDebrief does. A startup programme is reported by third parties.
- **Groq.** Whisper large v3 turbo at $0.04 an hour, the cheapest transcription on the list. The spend limit "applies organization-wide across all API keys", so no cap on a key.
- **Mistral.** Voxtral at about $0.003 a minute. Spending limits are "per workspace"; keys live inside workspaces. No cap on a key.
- **OpenAI.** gpt-4o-mini-transcribe at $0.18 an hour. The Admin API sets a monthly hard limit for the organisation, returning 429 when reached, and alerts per project. Its key-safety page says "the sharing of API keys is against the Terms of Use."
- **AWS, Google, Azure.** Budgets and alerts that act after a threshold is crossed; AWS can attach a deny policy to a user when a budget is exceeded, which is a cost control, not a ceiling on a key. None has a prepaid key with a cap.
- **Gateways.** Portkey's [budget limits](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits) put a dollar or token cap on a provider integration and "automatically expire the key" when it is spent, on the Enterprise plan or for selected Pro customers; LiteLLM and others do the same, self-hosted. A gateway is a per-key meter that someone else runs. It is also a server the audio passes through, which changes the privacy story from "we never see it" to "a third party we chose sees it".
- **Puter.** Not a transcription provider, but the nearest precedent for the shape: its "User Pays" model lets a page call models with the user's own Puter account paying, keyless, from the browser. That is the arrangement, seen from the account side rather than the key side.

The pattern is clear enough to state. The two providers whose keys carry a ceiling, OpenRouter and ElevenLabs, are the two whose terms say the most about resale, because a capped key is the thing that makes resale easy. The providers whose terms are silent are silent because their keys cannot be sold on anyway.

## The four routes

1. **Buy a capped OpenRouter key per user.** The plan. Forbidden by the standard terms; the enterprise agreement might allow it, and that is a question to ask rather than assume.
2. **A provider that sells the capped key itself, or lets us issue one under its terms.** ElevenLabs has the key, the OEM terms and the programme. The gap is one sentence: that a key with a credit limit, issued from our account under the OEM terms, may be given to an end user who paid us, with the audio going from their browser to ElevenLabs and never to us. Scribe is a transcription model only, so the debrief and the infographic would go to a second provider, which is fine: the pass already declares the model for each step.
3. **Bring your own key, kept.** What runs today. Honest, private, no margin, and the five minutes it takes to get a key is where most people stop. The key page is good; it is still a wall.
4. **A metering proxy.** A gateway or a worker that holds one provider key and meters per user. It is the smallest possible backend, and it is a backend: the audio passes through it, so custody, governance, scaling and on-call all return, and the privacy sentence on the home page has to change. It is the last resort, and it is also the only route that needs nobody's permission.

What we can do without anyone's permission, today, is keep route 3 and make the key page shorter. What we need someone's permission for is route 2, and the rest of this article is how to ask.

## The brief for the agents that will write to them

*For the RiskMandate agent and the VoiceDebrief team. Written by the sgit.ai site session for Dinis Cruz, 12 October 2026. Agents draft; Dinis sends.*

**The principles**, which every message carries, in this order:

1. We have no server, on purpose. The audio goes from the user's browser to the provider and never to us. We want to keep it that way.
2. The commercial model is a property of the key. A user pays us once; we keep our share at that moment; the rest is the credit limit on a key the user holds. The provider meters. We never meter.
3. The user owns the ceiling. They can see what the key has spent and revoke it at the provider. We cannot spend on their behalf.
4. We will sign an end-user agreement, name the provider as a third party beneficiary, and put the provider's prohibited-use policy in front of every user, as OEM terms ask.
5. We will show every call: the model, the cost, the quote before the pass starts. Nothing hidden from the user or the provider.
6. Everything we build is open, so the provider can read what their key is used for.

**The ask**, one sentence, the same to each: let the credit limit be a property of a key that a user can buy through us, so that we never hold the audio and never run the meter.

**Per provider:**

- **ElevenLabs.** Apply to Grants with the monetised use case. Ask, in the same message: under the OEM terms, may a key with a custom credit limit, issued from our workspace, be given to an end user who has paid us, for Scribe only, with the audio sent from their browser? If the answer is yes with conditions, the conditions are the product. If they would rather sell the capped key themselves and pay a referral, better.
- **OpenRouter.** Ask whether an enterprise agreement, which licenses making the service available to our end customers, covers Management keys with a credit limit handed to a paying user, and what the minimum is. Note that their own docs describe the use case.
- **AssemblyAI and Deepgram.** Apply to the startup programmes. Ask for one feature: a spend cap on a key, set at creation through the API. Without it there is nothing to hand over. Deepgram's terms already allow integration that adds meaningful functionality; the missing piece is the cap.
- **Groq and Mistral.** The cheapest transcription on the list, and the same one feature request: a cap on a key rather than on the organisation or the workspace.
- **Portkey, and gateways like it.** Ask the honest question: is there a mode in which the gateway meters a key without the audio passing through it, for example by issuing the provider's own capped key? If not, the gateway is route 4 run by someone else, and we should say so to users.
- **Puter.** Ask whether the user-pays model can front a transcription provider, because it is the same arrangement from the account side.

**What to send with the message:** this article, the [Agent Desk article](an-agent-desktop-by-the-minute.md), the [VoiceDebrief key page](https://voicedebrief.ai/openrouter-key/), and the repository. The Agent Desk article is what got replies last time, because a provider that can see the research already done tends to answer the question that was actually asked.

**What to record:** every answer in the VoiceDebrief repository, as an issue, with the date, so that the map in this article can be updated as a new version rather than a new article.

## What this does not claim

- **The terms are read, not interpreted.** Every clause above is quoted from the provider's page on 12 October 2026; none of this is legal advice, and OEM and enterprise terms are agreements to be negotiated, not features to be assumed.
- **I do not know when OpenRouter's clause arrived.** It is in the terms dated 31 August 2026 and in a forum thread from about six months earlier. Whether the 31 August update changed it, I cannot tell from outside.
- **Three providers' terms were not read**: AssemblyAI, Groq and Mistral. Their keys cannot be capped, which made the question moot for this map, but the agents should read them before writing.
- **The commit counts are the counts.** They show when the work stopped, not why; the why is my account, as someone involved.
- **Route 2 may not exist.** ElevenLabs' OEM terms are the closest fit in writing, and they were written for bundling, not for a key a user buys. The answer may be no, and then route 4 is where we go, with the privacy sentence changed honestly.

If you run a model or transcription API and this is the arrangement you would be willing to offer, or you are building a product with no server and have hit the same wall, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine, and I am involved in VoiceDebrief. The product description and prices are from [voicedebrief.ai](https://voicedebrief.ai/), its [key page](https://voicedebrief.ai/openrouter-key/), its updates and engineering pages, read on 12 October 2026; the commit and tag counts are from its [public repository](https://github.com/sgraph-ai/SGraph-AI__SaaS__WhatsApp__Audio__Transcription), counted by week on the same day; the commercial model is from the project's brief pack of 28 July 2026 in that repository. Provider facts: [OpenRouter terms](https://openrouter.ai/terms) (31 August 2026) and [Management API docs](https://openrouter.ai/docs/features/provisioning-api-keys); [ElevenLabs terms](https://elevenlabs.io/terms-of-use) (9 October 2026), [OEM terms](https://elevenlabs.io/oem-terms) (28 February 2025), [API keys](https://elevenlabs.io/docs/overview/administration/workspaces/api-keys), [API pricing](https://elevenlabs.io/pricing/api) and [Grants](https://elevenlabs.io/grants); [Deepgram terms](https://deepgram.com/terms) and [key docs](https://developers.deepgram.com/docs/create-additional-api-keys); [Groq spend limits](https://console.groq.com/docs/spend-limits) and [Whisper pricing](https://console.groq.com/docs/model/whisper-large-v3-turbo); [Mistral workspaces](https://docs.mistral.ai/admin/quickstarts/manage-workspaces); [OpenAI Admin APIs](https://developers.openai.com/api/docs/guides/admin-apis) and [key safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety); [AssemblyAI startup programme](https://www.assemblyai.com/contact/startup-program); [AWS Budgets actions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-controls.html); [Portkey budget limits](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits); [Puter's AI gateway](https://developer.puter.com/ai/). Transcription prices for AssemblyAI, Deepgram and Mistral are from 2026 comparison pages and should be checked against each vendor before use. The figure was drawn for this article. Related: [An agent desktop by the minute](an-agent-desktop-by-the-minute.md), [No server, by design](no-server-by-design.md), [The vault is live](the-vault-is-live.md) and [Pay after you read](pay-after-you-read.md).

## Threads

Startups & strategySite & engineeringAgents & policy[This article as a graph →](graphs.md#the-key-is-the-billing-system)

### Builds on

- [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md) Nine properties a safe agent desktop needs, nine products against them, the macOS day-long lease, and the startup credits that would pay for testing it.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.

### Continued by

- [How the newsletter is made: twenty-three articles, three issues, and every quote checked, written by the agent that makes it](how-the-newsletter-is-made.md) The agent that writes the newsletter on how issues 7 to 9 were planned, read, checked and released, and the ninety-six articles still waiting.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.
- [sgit in GitHub Actions, side by side: a showcase repository and site that runs four ways of moving a vault between jobs on every run, measured, with a budget for its LLM steps](sgit-actions-side-by-side.md) A showcase repository that runs four ways of moving a vault between GitHub Actions jobs side by side, measured, with a budget for its LLM steps.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 85 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=85)

**Posting this article on LinkedIn?** The cover is [the-key-is-the-billing-system.jpg](banners/the-key-is-the-billing-system.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-key-is-the-billing-system.html)*
