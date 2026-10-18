# Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot, sgit.ai

> I want readers of this newsroom to be able to talk to it with a capable model, for free, without us paying for their questions and without us ever holding their key. The newsroom already answers questions from its own passages, with Chrome's built-in model or the reader's own OpenRouter key, and OpenRouter's free models stop at 50 requests a day until you buy credits. So we looked at every free inference offer we could find, as it stands on 18 October 2026, for material that is not private. Two things decide whether a provider works for this. Can anyone start free without a card? And can a web page call it directly, so the key goes from the reader's browser to the provider and nowhere else? We read each provider's pricing, limits and terms, and tested every API from the newsroom's own address. Four pass both tests: Groq, Google's Gemini API through AI Studio, Mistral's free mode, and OpenRouter's free models, which also offer a sign-in flow so the reader never copies a key. Cohere's trial and Pollinations pass too, with smaller limits. Cloudflare Workers AI has the most generous free allowance and does not train on what you send, but a page cannot call it, so it needs a small server the reader can deploy. NVIDIA's catalogue is strong and free, but it fails both tests that matter here, and its terms say trial use only. And a lot changed in 2026: GitHub Models was retired, Hugging Face stopped giving free accounts credits, and Cerebras and SambaNova now need a card. This is the map, what is possible, what is not, and what we will build.

*Source: <https://newsroom.sgit.ai/articles/free-models-your-own-key.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot

# Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.0.0](versions/free-models-your-own-key.md) · [newsroom v0.12.104](https://newsroom.sgit.ai/admin/versions.html) · llmfree-modelsapi-keyscorsgroqgeminimistralopenrouterown-keyresearcharticle

***Abstract:** I want readers of this newsroom to be able to talk to it with a capable model, for free, without us paying for their questions and without us ever holding their key. The newsroom already answers questions from its own passages, with Chrome's built-in model or the reader's own OpenRouter key, and OpenRouter's free models stop at 50 requests a day until you buy credits. So we looked at every free inference offer we could find, as it stands on 18 October 2026, for material that is not private. Two things decide whether a provider works for this. Can anyone start free without a card? And can a web page call it directly, so the key goes from the reader's browser to the provider and nowhere else? We read each provider's pricing, limits and terms, and tested every API from the newsroom's own address. Four pass both tests: Groq, Google's Gemini API through AI Studio, Mistral's free mode, and OpenRouter's free models, which also offer a sign-in flow so the reader never copies a key. Cohere's trial and Pollinations pass too, with smaller limits. Cloudflare Workers AI has the most generous free allowance and does not train on what you send, but a page cannot call it, so it needs a small server the reader can deploy. NVIDIA's catalogue is strong and free, but it fails both tests that matter here, and its terms say trial use only. And a lot changed in 2026: GitHub Models was retired, Hugging Face stopped giving free accounts credits, and Cerebras and SambaNova now need a card. This is the map, what is possible, what is not, and what we will build.*

Every free inference offer we checked on 18 October 2026, placed by two questions. Across: can a web page call the provider directly, with the reader's key? Up: can anyone start free without a card? Top right are Groq, Gemini through AI Studio, Mistral's free mode and OpenRouter's free models, with Cohere's trial and Pollinations; Alibaba Model Studio is there with a catch. Top left, free but needing a server in between: Cloudflare Workers AI, Z.ai and NVIDIA. Bottom, a card, credits or gone: Cerebras, Together, Hugging Face, Fireworks, DeepInfra, SambaNova and the retired GitHub Models.

## In short

- **The goal.** A reader talks to the newsroom with a capable model, free, on their own key, which we never hold.
- **Two tests decide it.** Free without a card, and callable from a web page directly.
- **Four pass both.** Groq, Gemini through AI Studio, Mistral's free mode, OpenRouter's free models.
- **Two more, smaller.** Cohere's trial, and Pollinations, which answered without any key.
- **Cloudflare is the most generous, and needs a server.** A page cannot call it; a Worker the reader deploys can.
- **NVIDIA fails both tests that matter.** A strong free catalogue, but no browser access, a phone check, and trial-only terms.
- **2026 took a lot away.** GitHub Models retired; Hugging Face credits gone; Cerebras and SambaNova need a card.
- **Free means they may learn from it.** Fine for what this newsroom publishes; never for anything private.

## What we want

The newsroom can already answer a question. The [search page](https://newsroom.sgit.ai/search/index.html) finds the passages that match, and a model answers from them alone, citing each one, with the passages shown beside the answer. There are two engines today. Chrome's built-in model runs on the reader's own machine with no key and sends nothing anywhere, but only in browsers that have it. Otherwise the reader pastes their own OpenRouter key, which stays in their browser and goes only to OpenRouter. The idea is not new here: [a chat box on a site with no server](chat-on-a-static-site.md) set out the trade, and [the key is the billing system](the-key-is-the-billing-system.md) showed a whole product built on the user's own key.

The gap is the first step. OpenRouter's free models allow 50 requests a day until you have bought at least $10 of credit. Someone who just wants to try it should not need a card.

So the question for this research: as of October 2026, where can a member of the public sign up, get a key, and call a frontier or near-frontier model for free, from a web page, with the key going from their browser to the provider and nowhere else? The material is this newsroom's published articles, so privacy is not the concern. We assume the provider may keep and learn from what is sent, and we say where it does.

## How we checked

Two research agents read each provider's own pricing, rate-limit, model and terms pages on 18 October 2026, and called the live model lists where they could. Where a fact came only from a third party, it is marked as reported.

Then we tested the one thing documentation rarely says: whether a web page can call the API at all. A browser will only send a request with a key to another site if that site answers a preflight check saying it allows it, the rule called CORS. We sent that preflight to every provider's chat endpoint, from the newsroom's own address, `https://newsroom.sgit.ai`, and recorded the answer. A provider that does not answer it cannot be called from a page, whatever its docs say.

One caution about names. Many of the model names below, Gemini 3.8 Flash, Qwen 3.8, Kimi K2.5 and others, are newer than what the agent that wrote this was trained on. They are given exactly as the providers' live pages and model lists show them.

## What changed in 2026

- **GitHub Models was retired on 30 July 2026.** The playground, catalogue and inference API are gone, for everyone. It had been the easiest free option for anyone with a GitHub account.
- **Hugging Face free accounts no longer get monthly credits** for Inference Providers. Its pricing page lists "None" for free users, who can buy credits; we did not find the date of the change.
- **Cerebras now needs a verified payment method.** New accounts get $5 of credit, which expires 30 days after it is granted; the earlier free tier with no card is gone.
- **SambaNova needs a card and bought credits** before the first request, from about 14 August 2026, as reported; its rate-limit docs still describe a free tier.
- **OpenRouter's free list changed.** Today's free models are NVIDIA's Nemotron 3 family, Google's Gemma 4 and some smaller ones; the free DeepSeek, Qwen, Kimi and gpt-oss variants are not on it.
- **Google changed Gemini keys.** From 28 May 2026, new AI Studio keys are "auth keys", and the API rejects requests from unrestricted standard keys.
- **Mistral renamed its free tier.** La Plateforme is now Mistral AI Studio, and the Experiment plan is now Free mode.

## What works from the browser today

### Groq

Free, with no card. Limits are per model and shown in the console; the published table gives `openai/gpt-oss-120b` 30 requests a minute, 1,000 a day and 200,000 tokens a day, though the page does not say which plan that table is for. Models include `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b` and `llama-3.3-70b-versatile`. It is OpenAI-compatible at `https://api.groq.com/openai/v1`. Requests are not retained by default; Groq may log them for up to 30 days to troubleshoot or investigate abuse. The browser test allows any page.

It is fast, and gpt-oss-120b is a capable open model. For a reader trying it, this is the simplest start.

### Google Gemini API, through AI Studio

Free with a Google account, from 18, with no card. Free models include `gemini-3.8-flash`, `gemini-3.6-flash` and `gemini-3.5-flash-lite`, and Gemma 4; Gemini 4 and the Pro previews are not free. Limits are no longer published and are shown only inside AI Studio. There is an OpenAI-compatible endpoint, under `/v1beta/openai/` on `generativelanguage.googleapis.com`. The browser test allows the newsroom's address.

Two things to say plainly. On the free tier, Google uses what you send "to provide, improve, and develop Google products and services and machine learning technologies", and "human reviewers may read, annotate, and process your API input and output". And the terms carve out the UK, the EEA and Switzerland, where the paid data terms apply to all use, and where apps offered to users must use paid services. A reader in London using their own free key for their own questions is a different case from an app offering Gemini to everyone, and our guidance would need to say so.

### Mistral, free mode

New accounts start in free mode, "with no credit card required". Limits are shown in the admin console; the docs do not publish them. Which models are free is not stated; the current API includes `mistral-medium-latest`, `mistral-small-latest` and `mistral-large-4`. It is OpenAI-style at `https://api.mistral.ai/v1`. Requests may be used to improve the models unless you switch off "Anonymous improvement data" in the admin privacy settings. The browser test allows any page.

### OpenRouter's free models

Free with an account, from 18. Free models allow 20 requests a minute and 50 a day, or 1,000 a day once you have bought at least $10 of credit at some point. The free list on 18 October had 19 entries, including `nvidia/nemotron-3-ultra-550b-a55b:free`, `nvidia/nemotron-3-super-120b-a12b:free`, `google/gemma-4-31b-it:free`, and `openrouter/free`, which picks a free model for you. Whether a free model's provider keeps or learns from your words depends on the model, and OpenRouter has a separate privacy setting for free models. The browser test allows any page.

OpenRouter has one thing the others lack: a proper sign-in for apps. The page sends the reader to OpenRouter, they approve, and the page receives a key of their own, through OAuth with PKCE. The reader never copies or pastes a key, and can revoke it at OpenRouter. The newsroom already uses OpenRouter, so this is the shortest step.

### Also direct, with smaller limits

- **Cohere's trial key.** Free on registration: 1,000 calls a month, chat at 20 a minute, with the Command A family. Its own API, not OpenAI's shape. The browser test allows any page.
- **Pollinations.** In our test, a chat request with no key at all was answered. Its docs say keys are expected, so we would treat keyless use as tolerated, not promised. It also has a "Sign in with Pollinations" flow, OAuth with PKCE, where the reader approves an app and it receives a key with its own budget. The browser test allows any page.

## Usable, with a catch

- **Cloudflare Workers AI.** The most generous free allowance we found: 10,000 "neurons" a day on a free Cloudflare account, which by its own rates is very roughly 100,000 to 300,000 tokens of gpt-oss-120b a day. Free models include `@cf/moonshotai/kimi-k2.5`, `@cf/openai/gpt-oss-120b`, `@cf/zai-org/glm-4.7-flash` and Llama 4 Scout. And "Cloudflare does not use Customer Content processed by Workers AI to train AI models." The catch: its REST API refused the browser preflight, so a page cannot call it. A Worker can, and a reader can deploy one into their own free account; then nobody else sees their key.
- **Alibaba Model Studio, international.** About a million free tokens per model, for 90 days, for first activations from 8 September 2026, on models including `qwen3.8-max` and `deepseek-v4.1-flash`, and the browser test allows the newsroom's address. It says it "will never use your data for model training". The catches: account details must be completed, and the "Free Quota Only" switch is now off by default, so a reader must turn it on or be billed once the free quota runs out.
- **Z.ai.** `glm-4.7-flash` and `glm-4.5-flash` are priced free, and are reported to allow one request at a time. The API does not answer the browser preflight, so it needs a server in between.
- **Fireworks and DeepInfra** answer the browser preflight, but offer only small starter credits: Fireworks $1, after which the account is suspended without a payment method.

## What does not work for this

- **NVIDIA, build.nvidia.com.** You can sign up free, with no card, though many reports say a phone number is needed for the key. The live catalogue is strong: `moonshotai/kimi-k2.6`, `z-ai/glm-5.3`, `deepseek-ai/deepseek-v4.1-flash`, the Nemotron 3 family, 81 models in all. But it fails the browser test: no CORS header. Its trial terms say access is "for limited trial purposes only and without use of the API Service or Generated Content in production", and that NVIDIA collects "User Content and Generated Content to improve NVIDIA products and services, including AI models". It is a good place for a developer to try models from a script. It is not something to offer readers from a page.
- **SambaNova.** No browser access, and a card and bought credits before the first request.
- **Cerebras.** A card, and $5 that lasts 30 days.
- **Together.** A $5 minimum purchase.
- **Hugging Face Inference Providers.** No free credits for free accounts.
- **GitHub Models.** Retired.

## The two tests, side by side

| Provider | Free, no card | From the page | Learns from it |
|---|---|---|---|
| Groq | Yes | Yes | Not kept by default |
| Gemini, AI Studio | Yes | Yes | Yes, human review; not in UK, EEA |
| Mistral free mode | Yes | Yes | Yes, opt-out |
| OpenRouter free | Yes, 50 a day | Yes | Depends on model |
| Cohere trial | Yes, 1,000 a month | Yes | Opt-out |
| Pollinations | Yes, even keyless | Yes | Not found |
| Alibaba Model Studio | Yes, 90 days | Yes | No |
| Cloudflare Workers AI | Yes | No, needs a Worker | No |
| Z.ai | Yes | No | Not found |
| NVIDIA | Yes, phone | No | Yes |
| Cerebras, SambaNova | No, card | Cerebras yes |  |
| Together, Hugging Face | No | Yes |  |
| GitHub Models | Retired |  |  |

"From the page" is our preflight test on 18 October 2026, from `https://newsroom.sgit.ai`. "Learns from it" is each provider's terms for free use, in short; the sections above quote them.

## The key, and where it lives

medium

The design is bring your own key, and the newsroom never holds it.

- **Where it is kept.** In this browser's storage for the session, or for longer if the reader asks, or in the reader's own vault, so it follows them across devices. The [vault pane](https://newsroom.sgit.ai/vault/index.html) already keeps a reader's account that way.
- **Where it goes.** From the reader's browser to the provider, with the question and the passages, and nowhere else. The page shows what it sent and which model answered, as the search page does today.
- **What protects it.** A key in a page can be read by any script on that page, so the page that holds it must load nothing it does not control. Google's own docs say "never expose keys client-side in production"; that advice is for a developer shipping their key inside an app to everyone. Here it is the reader's key, in the reader's browser, used by the reader. Even so, the safest keys are the ones a sign-in issues, scoped to this use and revocable, and the ones with a spending limit of zero because they are free.

## Can an agent create the account?

I asked whether an agent could do the sign-up for a reader. I think it should not, for three reasons. Most sign-ups now ask for a phone number or a captcha, on purpose. OpenRouter's terms forbid "multiple accounts as a single user, for purposes of bypassing or circumventing use limits", and an agent creating accounts at scale is the obvious way to do that. And NVIDIA's forum moderators already report ten to twenty automated rate-limit requests a day written by AI agents; providers are watching for exactly this.

What an agent can do well is guide: open the right page, explain each step and each setting, point at the privacy switch, check that the key works, and store it where the reader chooses. The account, and the agreement to its terms, stay the reader's. The sign-in flows from OpenRouter and Pollinations are the cleanest version: the reader approves once, and nothing is copied.

## What is possible, and what is not

**Possible today, from a page, for free:**

- A capable open model answering from the newsroom's passages: gpt-oss-120b or Qwen 3.8 on Groq, Gemini 3.8 Flash, Mistral Medium, or Nemotron 3 Ultra on OpenRouter.
- A sign-in instead of a pasted key, with OpenRouter or Pollinations.
- A key kept by the reader, in their browser or their vault, that we never see.

**Possible, with a server the reader runs:**

- Cloudflare's larger free allowance and models such as Kimi K2.5, through a Worker in the reader's own account.

**Not possible, as far as we found:**

- A free, keyless, dependable frontier model for everyone. Pollinations comes closest, and says it is not guaranteed.
- Calling NVIDIA, SambaNova or Z.ai from a page.
- Promising any of these limits for long. In 2026, four free offers we would have recommended at the start of the year disappeared or gained a card: GitHub Models, Hugging Face's credits, Cerebras and SambaNova.
- Anything private. On the free tiers, assume your words may be kept, learned from and, on Gemini, read.

## What we will build

Later, and in this order:

1. **Add Groq, Gemini and Mistral beside OpenRouter** on the search page, each with a short guide: where to sign up, which setting to check, which model to choose, and what the provider does with your words.
2. **Use OpenRouter's sign-in** instead of a pasted key.
3. **Let the key live in the reader's vault**, as well as in this browser.
4. **Publish a Worker** a reader can deploy for Cloudflare, with the steps.
5. **Recheck this map every quarter**, because it will change.

## What this does not claim

- **A snapshot.** Everything here is as of 18 October 2026, and free tiers change often.
- **Limits move.** Several providers show limits only inside their consoles; we report what is published.
- **Third-party facts are marked.** Phone checks at NVIDIA, SambaNova's date and Z.ai's concurrency are reported, not confirmed.
- **The browser test is one test.** A preflight from our address; a provider can change its headers at any time.
- **Not legal advice.** The UK, EEA and Swiss carve-outs in Gemini's terms are summarised, not interpreted.

If you know a free offer we missed, or one that has changed, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026, and research by this site's agent the same day: two research agents reading each provider's pages, and a CORS preflight to every endpoint from `https://newsroom.sgit.ai`. The main sources, all read on 18 October 2026: Groq, [rate limits](https://console.groq.com/docs/rate-limits), [models](https://console.groq.com/docs/models) and [your data](https://console.groq.com/docs/your-data); Google, [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), [terms](https://ai.google.dev/gemini-api/terms) and [API keys](https://ai.google.dev/gemini-api/docs/api-key); Mistral, [activating an API key](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key.md) and [usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits.md); OpenRouter, [limits](https://openrouter.ai/docs/api/reference/limits), [OAuth PKCE](https://openrouter.ai/docs/guides/overview/auth/oauth), [logging](https://openrouter.ai/docs/guides/privacy/logging) and [terms](https://openrouter.ai/terms); Cloudflare, [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) and [data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/); Alibaba Cloud, [Model Studio free quota](https://www.alibabacloud.com/help/en/model-studio/new-free-quota); Z.ai, [pricing](https://docs.z.ai/guides/overview/pricing); Cohere, [rate limits](https://docs.cohere.com/docs/rate-limits); Pollinations, [API docs](https://github.com/pollinations/pollinations/blob/main/APIDOCS.md); NVIDIA, [API trial terms of service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf) and [the forum thread on rate limits](https://forums.developer.nvidia.com/t/368420), 29 April 2026; Cerebras, [rate limits](https://inference-docs.cerebras.ai/support/rate-limits); SambaNova, [plans](https://cloud.sambanova.ai/plans); Hugging Face, [Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing); GitHub, [GitHub Models is now retired](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/), 30 July 2026. Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Agents & policy[This article as a graph →](graphs.md#free-models-your-own-key)

### Builds on

- [A chat box on a site with no server, the plan, and the trade it makes](chat-on-a-static-site.md) sgit.ai has no server, so its directory chat runs a local matcher by default, takes your own key as an opt-in, and leaves the vault bridge unbuilt.
- [The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it](the-key-is-the-billing-system.md) VoiceDebrief runs with no server on the user's own key; the one thing it cannot sell is a capped key, and this maps who could allow it and what to ask them.

### Continued by

- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 177 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=177)

**Posting this article on LinkedIn?** The cover is [free-models-your-own-key.jpg](banners/free-models-your-own-key.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/free-models-your-own-key.html)*
