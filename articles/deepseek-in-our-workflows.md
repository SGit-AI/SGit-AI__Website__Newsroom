# DeepSeek in our workflows and on sovereign websites: what DeepSeek offers today, open weights under MIT, an API that answers calls from the browser and speaks both OpenAI's and Anthropic's formats, at a fraction of the price, where its data goes and where else it can run, and a proposal for a sovereign website that loads Wikipedia articles and draws them as graphs, with DeepSeek doing the reading and code doing the checking, sgit.ai

> The model is a choice the owner makes, and DeepSeek should be one of the choices, used with open eyes. Its models are open weights under the MIT licence; its API speaks OpenAI's format and Anthropic's, so the same agents and even Claude Code can point at it; it answers calls straight from a browser, which we checked; and its Flash model costs 0.30 dollars per million tokens in and 1.20 out, half that off-peak. We have used it already: DeepSeek was one of the four open-weight models in the Swarm's 216 calls. The other side is just as clear: DeepSeek's own service stores data in China and lists training among its purposes, and several governments have restricted its app. So the rule is simple: public data can go to DeepSeek's API; anything private goes to the same open weights on a host and in a region the owner chooses, or to a small model on the device. The natural first fit is public data, and Wikipedia is the obvious one: a sovereign website that loads an article, asks DeepSeek to extract its facts, people, places and relations, checks every quote in code, anchors entities to Wikidata and draws the graph, building on the HTML graph and Wikidata work we have already done.

*Source: <https://newsroom.sgit.ai/articles/deepseek-in-our-workflows.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / DeepSeek in our workflows and on sovereign websites: what DeepSeek offers today, open weights under MIT, an API that answers calls from the browser and speaks both OpenAI's and Anthropic's formats, at a fraction of the price, where its data goes and where else it can run, and a proposal for a sovereign website that loads Wikipedia articles and draws them as graphs, with DeepSeek doing the reading and code doing the checking

# DeepSeek in our workflows and on sovereign websites: what DeepSeek offers today, open weights under MIT, an API that answers calls from the browser and speaks both OpenAI's and Anthropic's formats, at a fraction of the price, where its data goes and where else it can run, and a proposal for a sovereign website that loads Wikipedia articles and draws them as graphs, with DeepSeek doing the reading and code doing the checking

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/deepseek-in-our-workflows.md) · [newsroom v0.14.193](https://newsroom.sgit.ai/admin/versions.html) · deepseekmodelswikipediasovereign-websiteopen-weightgraphsarticle

***Abstract:** The model is a choice the owner makes, and DeepSeek should be one of the choices, used with open eyes. Its models are open weights under the MIT licence; its API speaks OpenAI's format and Anthropic's, so the same agents and even Claude Code can point at it; it answers calls straight from a browser, which we checked; and its Flash model costs 0.30 dollars per million tokens in and 1.20 out, half that off-peak. We have used it already: DeepSeek was one of the four open-weight models in the Swarm's 216 calls. The other side is just as clear: DeepSeek's own service stores data in China and lists training among its purposes, and several governments have restricted its app. So the rule is simple: public data can go to DeepSeek's API; anything private goes to the same open weights on a host and in a region the owner chooses, or to a small model on the device. The natural first fit is public data, and Wikipedia is the obvious one: a sovereign website that loads an article, asks DeepSeek to extract its facts, people, places and relations, checks every quote in code, anchors entities to Wikidata and draws the graph, building on the HTML graph and Wikidata work we have already done.*

A Wikipedia explorer on DeepSeek: code loads, the model reads, code checks, and the run is kept.

## In short

- **DeepSeek should be one of the owner's choices,** used with open eyes.
- **Open weights under MIT,** an API in OpenAI's and Anthropic's formats, callable from the browser.
- **Flash costs 0.30 dollars per million tokens in, 1.20 out,** half that off-peak.
- **DeepSeek's own service stores data in China;** private data goes to the open weights elsewhere.
- **First fit, public data:** a sovereign website that reads Wikipedia and draws it as a graph.

## Why DeepSeek

A sovereign website's brain is a choice the owner makes, like the host ([a European brain for a sovereign website](a-european-brain.md)). Mistral is the European option. DeepSeek is a different one, and a strong one: open weights, capable models and very low prices. We have used it already: in the Swarm's scale run, 216 model calls on four open-weight models for 6.8 cents, one of the four was DeepSeek ([pennies against dollars](pennies-against-dollars.md)). Making it a choice on purpose, with the facts in front of the owner, is the sovereign way to use it.

## What DeepSeek offers today

- **Two models on its API.** `deepseek-flash`, which is V4.1-Flash, takes images as well as text; `deepseek-v4-pro` is text only. Both have a context of a million tokens and think by default ([models and pricing](https://api-docs.deepseek.com/quick_start/pricing)).
- **Open weights under MIT.** V4.1-Flash and V4-Pro are both published under the MIT licence ([V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)), so anyone can host them.
- **Two formats.** An OpenAI-compatible endpoint, and an Anthropic-compatible one at `/anthropic`, where Claude model names map to DeepSeek's; DeepSeek documents how to point Claude Code at it ([Anthropic API](https://api-docs.deepseek.com/guides/anthropic_api)).
- **The price.** Flash is 0.30 dollars per million input tokens and 1.20 output, 0.006 for cached input; Pro is 1.32 and 3.96. Outside peak hours every price is halved ([pricing](https://api-docs.deepseek.com/quick_start/pricing)).
- **Calls from the browser.** We sent a preflight request to its API from another origin on 21 November: it answered with that origin allowed, for `POST` with an `authorization` header. So a static page can call DeepSeek with the visitor's own key, as the Mistral site calls Mistral ([one night on Mistral](one-night-on-mistral.md)).

## Where the data goes

This has to be said plainly. DeepSeek's privacy policy says "we directly collect, process and store your Personal Data in People's Republic of China", and lists training its models among the purposes ([privacy policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)). Its platform terms are governed by Chinese law ([terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html)). Several governments acted against its app in 2025: Italy's data protection authority blocked it, and Australia, Taiwan, the Czech Republic and the Netherlands restricted it on government devices or in public administration ([a summary](https://www.insurancejournal.com/news/international/2026/01/07/853376.htm)).

None of that is a reason not to use DeepSeek. It is a reason to choose where it runs, which is exactly what open weights allow:

- **DeepSeek's own API** for public data, where low cost matters and nothing private is sent.
- **The same weights on a host you choose.** OpenRouter lists dozens of providers serving V4.1-Flash, though not through its EU in-region routing ([providers](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017/providers)); Microsoft Foundry offers V4-Flash and V4-Pro ([Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-deepseek-v4-flash-and-v4-pro-in-microsoft-foundry/4515174)). Each under that host's terms and region.
- **On the device.** DeepSeek's distilled R1 models run on a laptop through Ollama, from 1.1 GB ([tags](https://ollama.com/library/deepseek-r1/tags)), and the 1.5B one runs in a browser tab with WebGPU ([the ONNX build](https://huggingface.co/onnx-community/DeepSeek-R1-Distill-Qwen-1.5B-ONNX)).

The owner sees which of the three a page uses before anything is sent.

## In our workflows

Because the API speaks the formats our tools already use, DeepSeek can sit behind the same one interface as every other provider ([LangGraph and us](langgraph-and-us.md)):

- **In the Swarm and in evals,** as one of the models a brief runs on side by side, measured on our own jobs, as we did with five Mistral models.
- **For bulk work on public data:** extraction, classification and first drafts over captures in a vault, where price matters and the data is already public.
- **Under the same rules as every model:** a behaviour policy, a budget, a ledger of every call, and code checking what code can check.

## A Wikipedia explorer

The first sovereign website I would build on DeepSeek reads Wikipedia, which is public, openly licensed and built for exactly this, and draws each article as a graph:

1. **Load, in code.** The page summary and links from Wikipedia's APIs, and Wikidata identifiers; both answer calls from the browser, and both ask clients to identify themselves with an `Api-User-Agent` header ([User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy)) and to respect their rate limits ([rate limits](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits)).
2. **Read, with DeepSeek.** Flash, on the visitor's own key, extracts the article's facts, people, places, dates and relations, each with the sentence it came from.
3. **Check, in code.** Every quote must appear in the article word for word, or it is dropped; every entity is anchored to its Wikidata identifier where one exists, so graphs from different articles join instead of multiplying.
4. **Draw.** The graph of the article and its links, using the renderers we already built in our [HTML graph service](https://github.com/the-cyber-boardroom/MGraph-AI__Service__Html__Graph), which turns any HTML page into graphs drawn six ways.
5. **Keep.** Each run saved with the article's revision, the model, the prompt, the output and the cost, so it replays with no key and anyone can see how a graph was made.

This builds on work we have done before: the HTML graph service, and this summer's work on graphing text, where Wikidata became the shared concept layer that stops graphs from exploding. The site would credit Wikipedia under CC BY-SA 4.0 on every page, link each article, and say what was changed ([reusing Wikipedia content](https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content)). And it would be independent of DeepSeek, saying so on every page, and checking DeepSeek's brand rules before using its name in an address.

## What this does not claim

- **Nothing here has been built yet;** the explorer is a proposal.
- **We checked the browser preflight only,** not a full call with a key.
- **Prices, models and terms are as DeepSeek's pages showed on 21 November 2026.**
- **Hosting elsewhere moves the data,** under that host's own terms; it is not automatically private.

## Where this comes from

My own thinking in writer-10's session on 21 November 2026; DeepSeek's documentation, privacy policy, terms and model cards; OpenRouter's, Microsoft's, Ollama's and Hugging Face's pages; Wikimedia's API documentation and policies, all read that day, with the browser preflights to DeepSeek's API and Wikipedia's run from our environment. Related: [a European brain for a sovereign website](a-european-brain.md), [one night on Mistral](one-night-on-mistral.md), [pennies against dollars](pennies-against-dollars.md), [LangGraph and us](langgraph-and-us.md), [free models, your own key](free-models-your-own-key.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#deepseek-in-our-workflows)

### Builds on

- [A European brain for a sovereign website: why the model is a choice the owner makes, like the host, how Mistral fits at every level, from Ministral 3 running on a Pi Pro to Mistral Small 4 on an EU endpoint for the team inside the site, what its terms say about where data goes, the one licence to watch, what we have already run on Mistral, and how we could work with it](a-european-brain.md) Why a sovereign website's model is the owner's choice, and how Mistral fits: Ministral 3 on the device, Mistral Small 4 on an EU endpoint.
- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [One night on Mistral: how an agent team turned "a European brain for a sovereign website" into a working site overnight, for the Mistral Vibe Hackathon in London, with 33 demos in the browser, from a shoebox of files to a website and five Mistral models drawn side by side, evals that found which model catches a scam note, the Swarm moved onto Mistral, about 41 cents of Mistral usage, and why this is where I want to start working with Mistral](one-night-on-mistral.md) An agent team turned the European brain article into a working Mistral site overnight: 33 browser demos, evals, the Swarm on Mistral, about 41 cents.
- [LangGraph and us: how the way we build agent pipelines maps to LangChain, LangGraph, LangSmith and the agent testing toolkits, what is the same, what we do differently, code for each function and every step saved to a vault, what we can learn from them, and where they could run inside our own pipelines](langgraph-and-us.md) How our agent pipelines map to LangGraph, LangChain and the eval toolkits: the same ideas, a more deterministic default, and what to learn and use.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 523 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=523)

**Posting this article on LinkedIn?** The cover is [deepseek-in-our-workflows.jpg](banners/deepseek-in-our-workflows.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/deepseek-in-our-workflows.html)*
