# A chat box on a site with no server, the plan, and the trade it makes, sgit.ai

> Nineteen sibling sites is too many to browse, so the directory now answers questions. The design problem is that sgit.ai has no server and no vault host, which means the honest options are a local matcher, a key in your browser, or moving the page into a vault, and only one of those is free.

*Source: <https://newsroom.sgit.ai/articles/chat-on-a-static-site.html> · site v0.7.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A chat box on a site with no server, the plan, and the trade it makes

# A chat box on a site with no server, the plan, and the trade it makes

2026-08-27 · [article v1.2.2, 5 versions](versions/chat-on-a-static-site.md) · [site v0.2.47](https://sgit.ai/admin/versions.md) · chatllmbyokplan

***Abstract:** Nineteen sibling sites is too many to browse, so the directory now answers questions. The design problem is that sgit.ai has no server and no vault host, which means the honest options are a local matcher, a key in your browser, or moving the page into a vault, and only one of those is free.*

The [network directory](https://sgit.ai/network/index.md) now has a chat box. It answers one question, *which of these nineteen sites is mine?*, and it works with no key, no account and no network call.

That last part took the most thought, so this is the plan behind it: what shipped, what it costs, and what would remove the cost.

The panel on the directory. The default tier is a local matcher; the key is opt-in and clearly labelled.

## The constraint nobody can design around

`sgit.ai` is a static site on GitHub Pages. There is no server, no session, no place to keep a secret. Every sibling on `*.sgit.ai` is the same.

That matters because the usual way to put a chat box on a website is to call a model from a backend that holds the API key. There is no backend here to hold one. So the real options are only three, and it is worth being blunt about which is which.

## The three tiers

**Tier 0, match. Shipped, on by default, needs nothing.**

A deterministic scorer runs in the browser against the catalogue of all nineteen sites, emitted at build time from the same data the cards and the table are built from. Type *"I have to sign off a risk"* and it points at [risks.sgit.ai](https://sgit.ai/network/index.md#risk-governance), and shows you which words it matched on.

It is not clever. It is instant, free, private, works offline, and, the part that made it the default, **it tells you why it chose**. An LLM answer does not give you that. The scorer weights a hit in a site's thesis or domain above one in its summary, and stops there.

The important property: a reader should never have to hold a credential to use an index.

**Tier 1, bring your own key. Shipped, opt-in, and it costs you something.**

Paste an OpenRouter key and the browser calls `https://openrouter.ai/api/v1/chat/completions` directly, streaming, with the catalogue as the system prompt. This is not a new pattern here, the [SG/Vault workbench vault](https://sgit.ai/demos/vaults/index.md) already does exactly this, using the same endpoint and the versioned `sg-llm-request` module served from `dev.tools.sgraph.ai`, so this reuses a proven client rather than inventing one.

The cost is real and the UI states it rather than burying it: **with no host, there is no permission floor, so the key lives in this page's origin.** It goes into `localStorage` and into a `fetch` to `openrouter.ai`. It is never sent to sgit.ai, there is no server here to send it to, but the page cannot protect it the way a vault app can. That is a trust decision, and it belongs to the reader, so it is presented as one.

When the model call fails, the panel falls back to Tier 0 and says so. Degrading to something that works beats an error message.

**Tier 2, the bridge. Not built, and the one that removes the trade.**

Serve the directory as a **vault app** and the problem disappears. [llms.sgit.ai](https://sgit.ai/network/index.md#agents-ai) documents the contract: the key lives in `.vault/llm/config.json`, *below the permission floor*, the host makes the call, and the app never sees the credential. Its API is `sg.llm.available / chat / cancel / models / usage`, with grants defaulting to deny.

The striking detail in that documentation is that there are **three** chat surfaces, and two of them need no application code at all, the vault chat panel, and the same panel beside any running app. *"Every existing vault app gets this without being changed."*

The qualification has to travel with the claim, and llms.sgit.ai insists on this in its own words: *"The bridge protects your key; it is not yet a boundary that prevents all egress."* It protects the credential you trusted it with. It does not yet stop a malicious app calling a provider with a credential of its own.

## What would need building

Tier 2 is not a rewrite, but it is not free either. Honestly scoped:

| Piece | State | Note |
|---|---|---|
| The catalogue | **Done** | Emitted at build from `admin/content/sites/*.md`; nineteen entries |
| Tier 0 matcher | **Done** | `assets/network-chat.js`, no dependencies |
| BYOK client | **Done** | Streams from OpenRouter; the workbench vault's proven pattern |
| A vault build of the directory | **Not started** | The generator already emits a `.md` twin of every page; a vault app is a different target, not a different site |
| `sg.llm` detection | **Not started** | The panel should prefer the bridge when it exists and fall back when it does not, the same shape as the Tier 1 → Tier 0 fallback already in the file |
| Shared component | **Partly, 7 September** | A site-wide pane now sits on every page here, and its model can *call tools* over the site's own index and markdown twins (v0.2.63). Still one site's copy rather than a versioned module the other eighteen can load |

That last row is the one that decides whether this was worth doing. A chat box on one site is a feature. The same panel on all nineteen, reading each site's own catalogue, is the thing that makes a network of nineteen sites navigable, and it is why the catalogue is generated rather than written.

## Addendum, 7 September, the pane grew tools

The directory chooser above answers one question. Ten days later every page carries a pane (*Ask this site*, bottom right) whose model does not read a catalogue pasted into its prompt. It is given **seven tools** as function definitions: `search_site`, `read_page`, `list_vaults`, `list_sites`, `latest_updates`, `get_board`, `current_page`. Each call runs in the page, over an index the build emits from the same data as `llms.txt`, the vaults table, the network directory, the feed and the board, and the pane shows every call it made. With no key, the same tools run directly: type words to search, or `/vaults`, `/board`, `/read PATH`. The three tiers are unchanged; Tier 2 is still not wired, and is now on the board as T11.

## What it does not do

It does not answer questions *about* the subjects. Ask it how to threat-model a payment gateway and it will point you at a site, not teach you. The scope is routing, deliberately: the sites already contain the arguments, and a summary that drifts from them is worse than a link that does not.

It also does not know anything that is not in the catalogue. Nineteen theses, nineteen summaries, nineteen categories, all quoted from each site's own words rather than paraphrased, which is the same rule the [directory](https://sgit.ai/network/index.md) follows.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0.*

## Threads

Site & engineering[This article as a graph →](graphs.md#chat-on-a-static-site)

### Continued by

- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [chat-on-a-static-site.jpg](banners/chat-on-a-static-site.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/chat-on-a-static-site.html)*
