# No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitive rented as a commodity or run in the user's browser over encrypted vaults, sgit.ai

> There is an engineering elegance in an application with no real backend, and sgit is what makes it possible, because what it gives you is an encrypted data store. The honest way to say it is not that there is no backend. You still need somewhere to serve the pages and somewhere to keep the encrypted files, and sometimes a model provider or an agent platform. But those are commodity services, each doing a few things, run by someone whose job it is. The only tech stack you maintain is an HTML application: the HTML, the CSS and the JavaScript. And you lose very little. Data files live on fast storage, and in a vault they are immutable, so they can be cached for ever. A query that needs a database runs on a database in the browser. A passkey identifies the user, so there is no user data on a server to protect. Append lanes carry messages, PKI encrypts between users, and models run in the browser or behind a host that holds the key. The missing piece is a clean way to give keys to the client. The constraint forces simpler designs, and the server holds nothing worth stealing.

*Source: <https://newsroom.sgit.ai/articles/no-tech-stack-to-maintain.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitive rented as a commodity or run in the user's browser over encrypted vaults

# No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitive rented as a commodity or run in the user's browser over encrypted vaults

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-03 · [article v1.0.0](versions/no-tech-stack-to-maintain.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · architectureno-backendsgitvaultspasskeyspkiwebassemblystatic-hostingsimplicityarticle

***Abstract:** There is an engineering elegance in an application with no real backend, and sgit is what makes it possible, because what it gives you is an encrypted data store. The honest way to say it is not that there is no backend. You still need somewhere to serve the pages and somewhere to keep the encrypted files, and sometimes a model provider or an agent platform. But those are commodity services, each doing a few things, run by someone whose job it is. The only tech stack you maintain is an HTML application: the HTML, the CSS and the JavaScript. And you lose very little. Data files live on fast storage, and in a vault they are immutable, so they can be cached for ever. A query that needs a database runs on a database in the browser. A passkey identifies the user, so there is no user data on a server to protect. Append lanes carry messages, PKI encrypts between users, and models run in the browser or behind a host that holds the key. The missing piece is a clean way to give keys to the client. The constraint forces simpler designs, and the server holds nothing worth stealing.*

What a backend usually does, and where it goes instead: a commodity service, or the browser.

## In short

- **It is not that there is no backend.** It is that there is no tech stack of your own to maintain.
- **What you own:** the HTML, the CSS and the JavaScript.
- **What you rent:** a static host, an encrypted file store, and, when you need them, a model provider or an agent platform.
- **What runs in the browser:** the database, the user's identity, the encryption between users.
- **The constraint is a design tool.** With no server-side data, you are pushed to simpler solutions.
- **The gap:** a clean way to give keys to the client.
- **The result:** fewer moving parts, and a server that holds nothing worth stealing.

## Not no backend: no stack of your own

I have been trying to find the right way to say this. "No backend" is not quite true. A web application still needs somewhere to serve its pages from, and somewhere to keep its data. Sometimes it needs a way to call a model, or to run an agent. Those are backends.

But each of them is a commodity: a service that does a few things, that many companies sell, and that someone else patches at three in the morning. What you do not have is a tech stack of your own: no application server, no framework on a server, no database server with a schema and migrations, no password store, no queue. The only code you maintain is an HTML application. The HTML, the CSS and the JavaScript.

That is what sgit makes possible, because what it gives you, in the end, is an encrypted data store that a static page can read and write. I wrote up [how a vault works](how-a-vault-works.md) today; this is what that design is for.

## You keep the primitives

The usual objection is that without a backend you lose what a backend gives you. Go through them one by one, and almost every one is still there.

**Data, on fast storage, cached for ever.** The data is files, and the files sit on cloud storage built to serve files quickly. In a vault, every object except one is immutable and named by the hash of its own ciphertext, so a browser or a CDN can keep it for as long as it likes. HTTP has had a word for that since 2017: RFC 8246's `immutable` extension "allows servers to identify resources that will not be updated". To see whether anything changed, the page re-reads one small file.

**A database, in the browser.** If a question is better answered by a database, run the database on the client. Load the data, put it in the database, and query it in the page. This site already runs [two real database engines with no server](https://newsroom.sgit.ai/databases/index.html), SQLite and a SPARQL store, compiled to WebAssembly. "DuckDB-Wasm brings DuckDB to every browser thanks to WebAssembly", and PGlite, an "Embeddable Postgres", is 3 MB gzipped and runs in the browser too. It works better than people expect.

**Users, with nothing on a server to protect.** A passkey on the user's device identifies them. And the WebAuthn PRF extension, part of the Level 3 Recommendation of 25 August 2026, gives the page a value that only that passkey can produce. MDN's description is the point: it "can be used to generate a symmetric key for encrypting sensitive data, and that can only be decrypted by a user who has the seed and the associated authenticator". So you can have a whole user experience, accounts, preferences, history, without a user table on a server that you then have to defend. That is how [the passkey opens the vault](the-passkey-opens-the-vault.md) on this site.

**Messages and events.** Vaults have append lanes: an append-only inbox that other people, agents or a service can write to, and the owner reads. A message to a user, an event from a background job, feedback on a page: each one lands as an entry in a lane, encrypted, on the same store. We measured a hundred writers landing a thousand entries in one lane, in [agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md).

**Sharing between users.** PKI does what a server usually mediates. sgit's `pki` commands generate an RSA-4096 key pair, and encrypt to a recipient's public key with RSA-OAEP wrapping AES-256-GCM, so only the recipient can decrypt. Publish public keys, as [a pen and a key](a-pen-and-a-key.md) does with the register at pki.sgit.ai, and two users can exchange data through storage that cannot read it.

**Models.** A model can run in the browser: Chrome's built-in AI is described as "your browser provides and manages foundation and expert models". Or the page calls a provider through a host that holds the key, as a [vault app does](how-a-vault-works.md) through `sg.llm`, where the app never sees the key.

## Agents: rent the loop

When a workflow really needs an agent, a loop that runs, reads, decides and writes, I would not build that infrastructure either. Depending on scale, I would run it on one of the main cloud agent platforms. You get the intelligence of the platform, and you get provenance: the platform keeps the record of what the agent did, which is evidence you did not have to build. This newsroom is written that way: an agent session in the cloud, writing to a repository, every step committed.

And remember why we use models at all. My logic is that you use LLMs so that you do not have to use LLMs: as much of the work as possible should become deterministic code, and whatever can run on the client should.

Illustrative: the moving parts you own with a backend, and with a static app over vaults.

## Fewer moving parts, better design

The elegance is not only that there are fewer things to patch. It is what the constraint does to the design.

When there is no server-side data, you cannot reach for a table and a background job every time something is awkward. You have to find the solution that works with files, keys and the browser, and those solutions tend to be simpler: data shaped for reading, computed once at build time; state that belongs to the user, held by the user; events as entries in a lane, not as calls into a service that must be up. None of it is complicated on the client side.

And the security story follows. As I wrote in [the attack surface you do not have](the-attack-surface-you-do-not-have.md), the server only stores encrypted data. If it had a catastrophic failure and someone had all of it, they would have ciphertext.

## Vaults as distribution

There is one more part. The application itself can live in a vault. A static page on a domain of mine opens a vault, and the app inside it runs. To update the app, update the vault; the next visit picks it up. The same vault can hold the data the app needs, and PKI can carry what users send each other.

Where should the static page live? For a free tool, a demo, documentation or a site like this one, GitHub Pages is very easy. For a product that sells, it is not allowed: GitHub's own page says it is "not intended for or allowed to be used as a free web-hosting service to run your online business", which includes commercial software as a service. The same folder moves to Cloudflare Pages, Netlify or any static host, as I found for [the padel shop](the-shop-that-sells-time.md). That is the other benefit of having only static files: moving host is a copy.

## What is still missing

The main gap is a clean way to give keys to the client. A model provider's key in a page is a key in every visitor's browser; Anthropic's own SDK disables browser use by default "to avoid exposing your secret API credentials". Today the answers are the user's own key, a host that holds the key, as vault apps use, or a key handed to one browser through a sealed drop, as in [handing secrets to agents and browsers](handing-secrets-to-agents.md). I think this is temporary: the industry has not caught up with applications that have no server of their own. Apart from that, it all works.

## What this does not claim

- **The comparison figure is illustrative,** not a count of any real system.
- **There is still a backend;** it is rented, and an outage of a commodity service is still an outage.
- **Not every application fits.** Heavy shared writes, large joins across every user's data, and work that must run when no browser is open need more.
- **Browser support** for the passkey PRF extension and for on-device models varies by browser and device.
- **The server still sees metadata:** object counts, sizes and timings.

## Where this comes from

My conversation of 3 November 2026, in this site's repository under `admin/notes/2026-11-03__no-tech-stack/`. [RFC 8246, HTTP immutable responses](https://www.rfc-editor.org/rfc/rfc8246.html). [DuckDB-Wasm](https://github.com/duckdb/duckdb-wasm) and [PGlite](https://github.com/electric-sql/pglite). [Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/) and [MDN on WebAuthn extensions](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions). [Chrome's built-in AI](https://developer.chrome.com/docs/ai/built-in). [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). [Anthropic's TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript). sgit-ai version 0.21.0: `cli/CLI__PKI.py` and `crypto/PKI__Crypto.py`. Earlier on this site: [the no-server startup](the-no-server-startup.md). All read 3 November 2026.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#no-tech-stack-to-maintain)

### Builds on

- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.
- [A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a note can be checked as mine](a-pen-and-a-key.md) Every article now has a Pen to mark it, comment and tell the newsroom, and a browser key pki.sgit.ai vouches for signs each note as mine.
- [The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed](the-attack-surface-you-do-not-have.md) Every CVE makes me smile: moving to the client side took my servers out of the news, and the constraint turned out to be speed.
- [The shop that sells time: the padel shop's path to market, sell one and fulfil it before anything else, start with the customers who already trust you, promise late and deliver early, a few products you vouch for, and no stock until the orders make you](the-shop-that-sells-time.md) The padel shop's path to market: sell one and fulfil it, sell time and trust, promise late, few products, and no stock until orders force it.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 379 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=379)

**Posting this article on LinkedIn?** The cover is [no-tech-stack-to-maintain.jpg](banners/no-tech-stack-to-maintain.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/no-tech-stack-to-maintain.html)*
