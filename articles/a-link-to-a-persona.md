# A link to a persona: send people to the newsroom as someone, not as nobody, sgit.ai

> When I send someone to the newsroom today, they land on a front page made for nobody. I would rather send a CISO to the newsroom as a CISO, a data protection officer as a DPO, a developer as a developer, and one particular person as a persona made for them. This is the brief for doing that with nothing but a link. Personas move out of the site's code into an encrypted vault, opened in the reader's browser with a published read key, so a persona can be added or updated by the newsroom's agents without a single change to the site. A few personas get a page of their own, /persona/ciso/; any number more are reached through the part of the link after the #, which browsers never send to a server; and a persona for one person can live in a vault of its own, readable only by whoever has the link. The reader can follow the persona as it is kept up to date, or fork it and make it theirs. It draws on what Netflix, Bluesky, Mastodon, Apple News and Brave News learned about profiles, starter packs and personalisation on the device, and it stays entirely client side.

*Source: <https://newsroom.sgit.ai/articles/a-link-to-a-persona.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A link to a persona: send people to the newsroom as someone, not as nobody

# A link to a persona: send people to the newsroom as someone, not as nobody

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.0.0](versions/a-link-to-a-persona.md) · newsroompersonaspersonalisationvaultslocal-firstprivacyonboardingagentsbriefarticle

***Abstract:** When I send someone to the newsroom today, they land on a front page made for nobody. I would rather send a CISO to the newsroom as a CISO, a data protection officer as a DPO, a developer as a developer, and one particular person as a persona made for them. This is the brief for doing that with nothing but a link. Personas move out of the site's code into an encrypted vault, opened in the reader's browser with a published read key, so a persona can be added or updated by the newsroom's agents without a single change to the site. A few personas get a page of their own, /persona/ciso/; any number more are reached through the part of the link after the #, which browsers never send to a server; and a persona for one person can live in a vault of its own, readable only by whoever has the link. The reader can follow the persona as it is kept up to date, or fork it and make it theirs. It draws on what Netflix, Bluesky, Mastodon, Apple News and Brave News learned about profiles, starter packs and personalisation on the device, and it stays entirely client side.*

A link to a persona: the newsroom's agents keep personas in a vault; a link names one; the reader's browser opens the vault with a read key, shows the newsroom as that persona, and lets the reader follow it or make it their own.

## In short

- **A link should land someone as someone.** Instead of the front page, send a CISO to the newsroom as a CISO, a DPO as a DPO, or one person as a persona made for them.
- **Personas move into a vault.** Not the site's code. The newsroom's agents add and update them in an encrypted vault; the reader's browser opens it with a published read key. No change to the site, no git push, for any persona.
- **Three kinds of link.** A page of its own for the few personas everyone uses (`/persona/ciso/`); a fragment for any number more (`/persona/#dpo`); and a private persona in its own vault, readable only by whoever holds the link.
- **Follow or fork.** A visitor can keep the persona as it is kept up to date, or copy it and make it their own, with their reading on top.
- **Kept by the newsroom.** Every article published and every newsletter issued updates the personas it belongs to. A persona is a curated, living reading list.
- **All client side.** GitHub Pages serves the files, the vault host stores ciphertext it cannot read, and everything else happens in the reader's browser.

## Landing as nobody

When I email someone about an article, I link to the article. When I want them to look around, I link to the front page, and they land on a page made for nobody in particular: the latest articles, whatever the editor put at the top, sixty-odd pieces across six topics. Some of it is exactly what they would want and most of it is not, and they have no way to know which is which.

The personas that went live today fix that for a reader who stays: [pay to keep your persona](pay-to-keep-your-persona.md) described how a reader's own reading builds a persona, and how five starting personas, from the founder to the board member, give a new reader somewhere to begin. But a starting persona still has to be found and chosen. The better move is for the person who sends the link to choose it: I know I am writing to a CISO, so the link should open the newsroom as a CISO.

## Three kinds of link

**A page of its own, for the personas everyone uses.** `/persona/ciso/`, `/persona/cto/`, `/persona/dpo/`, `/persona/sgit-developer/`. Each is a tiny static page that knows one name. What the persona contains, its topics, its articles, its description, is not in the page; it is fetched from the vault when the page opens. So the page is created once, and the persona behind it can change every day without touching the site.

**A fragment, for any number more.** The site is static pages on GitHub Pages, so there is no server to answer `/persona/owasp-chapter-leader/` unless a page exists at that path. The fragment solves it: `/persona/#owasp-chapter-leader`. The page at `/persona/` reads the name after the `#`, looks it up in the vault, and opens the newsroom as that persona. With no fragment, it asks which persona you would like. A new persona is a new file in the vault, and its link works the moment the vault is pushed.

**A private persona, for one person.** A persona made for one person, from what I know about them or from the reading they sent us, should not sit in a public vault where anyone can see that it exists. It can live in a vault of its own, and the link carries what is needed to open it: `/persona/#v=<vault id>&k=<read key>&p=<name>`. That works because of how fragments are defined. RFC 3986 says "the fragment identifier is separated from the rest of the URI prior to a dereference" and is "dereferenced solely by the user agent, regardless of the URI scheme": the browser keeps it, and GitHub Pages never sees it. The vault host sees a request for some ciphertext from that vault, and nothing it can read. Whoever has the link can open the persona; whoever does not, cannot, and cannot find out it exists.

## What happens when the link opens

1. **The page shows who you are reading as**: the persona's name, its description, who keeps it and when it was last updated. "You are reading as Sam, the security lead, kept by the SGit Newsroom, updated 10 October."
2. **The newsroom opens as that persona**: its picks, its reading list, its graph, the same views [your newsroom](../account/newsroom.md) has today.
3. **The persona is added to the reader's personas straight away, as a visitor**, marked as one, because removing it is one tap and asking first is one more step between the link and the reading. It becomes the active persona while they are on the page.
4. **Then the reader chooses what it is.** *Follow* keeps it linked to the vault, so the next visit brings the latest version. *Make it mine* forks it: a copy that starts from the curated version and from then on moves with their own reading, their own Keep and Not for this persona, and their own ratings. *Remove* takes it away and leaves their history untouched.

Follow and fork are the two halves of the design, and they come straight from git: a persona is a reading list with a history, and you either track the upstream or branch from it.

## The vault, and who keeps it

The personas live in an sgit vault: encrypted before upload, versioned like git, opened in the browser with a read key that cannot write. This site already opens thirty-odd vaults that way, with nothing but an endpoint, a vault id and a read key, using the reader the site has had for months in `assets/vault-docs.js`. A persona vault is one more.

```

personas/
  index.json          the listed personas: id, label, name, theme, one line, updated
  ciso.json           one persona
  dpo.json
  sgit-developer.json
  ...
  changes.jsonl       one line per update: which persona, what changed, why, by which role

```

A persona file is what the [five starting personas](../account/personas.md) already are, plus what a living persona needs: who keeps it, when it changed, and a version.

```

{ "id": "ciso", "label": "The CISO", "name": "Sam", "theme": "#b91c1c",
  "blurb": "Agents as insiders: who you are protecting against, blast radius, identity, incidents.",
  "topics": { "agents-and-policy": 3, "vaults-and-method": 1 },
  "articles": ["who-are-you-protecting-against", "footprint-and-blast-radius", "..."],
  "tags": ["threat-modelling", "insider-threat", "blast-radius"],
  "keeper": "SGit Newsroom", "updated": "2026-10-10", "version": 7, "listed": true }

```

**The newsroom's agents keep it.** The newsroom already runs as a desk of roles with behaviour policies: an editor who places, a journalist who writes, a historian who connects, a designer and a developer. Keeping personas is one more job on the desk. Every time an article is published, the persona keeper reads its graph and adds it to the personas it belongs to; every newsletter issue is a reason to review the lead articles of each; and every reading history a reader sends us through [the share page](../account/share.md) is a chance to see whether a persona matches the people it is meant for. Each change is a vault commit, with a line in `changes.jsonl` saying what changed and why.

**No git push to the site.** This is the point of putting personas in a vault rather than in the site's code. Adding or changing a persona is an `sgit commit` and an `sgit push` to the vault, done by the agent that owns it, without a release of the website, a build, or a deploy. The site's code knows only the vault's id and read key, which are public on purpose.

**More than articles, later.** A persona can carry more than links to the site's own articles: a short list of outside reading, industry developments, security news that matters to a CISO this week, each with its source. The same vault, the same keeper, and the same persona page show them. That is how a newsroom with sixty articles can serve a dozen audiences well without writing a dozen times as much.

## What others learned, and what it means here

**Netflix, 2013: profiles.** Netflix launched Profiles on 1 August 2013, up to five per account, so that each person in a household got their own suggestions instead of the account holder's. The Christian Science Monitor put it simply: "Now Netflix subscribers can create as many as five different profiles within a single account." The lesson for us is the one in [pay to keep your persona](pay-to-keep-your-persona.md): people do want several, one per way they watch or read, and they have to be simple to make and to switch.

**Bluesky, 2024: starter packs.** Bluesky's starter packs, launched on 26 June 2024, are, in its words, "personalized invites that allow you to bring friends directly into your slice of Bluesky!" Each holds up to 150 people and three custom feeds, has its own link, and someone without an account can "join via a friend's starter pack and get started with their recommended customizations", then add or remove them. That is the closest thing to a link to a persona that anyone has shipped at scale, and two things carry over: the link is the onboarding, and what the link sets up belongs to the newcomer afterwards. The difference is in time. A starter pack is a one-off list; a custom feed is ongoing. Our follow and fork are those two, for the same object.

**Mastodon: follow packs, and consent.** On Mastodon, community "follow packs" were CSV files of up to 35 accounts that a user downloaded and imported, and the project has announced a native version whose people can opt out of being included and are told when they are. For us the consent question is sharper, because a persona can be made for, or named after, a real person. A persona about a person goes in a private vault and is sent only to them; a public persona describes a role, never a named individual, unless they have agreed.

**Apple News and Brave News: personalisation on the device.** Apple's privacy page for News says "Recommendations in Apple News are made based on the information stored on your device", and that it uses iCloud to sync a reader's history across their devices. Brave says of Brave News: "All the learning and personalization happens exclusively in your browser." Both still run servers to deliver the content, and Apple runs one to sync. The direction is the same as ours; the difference is who holds the copy that travels between devices. Here the content is static files and the personas are ciphertext; the only thing a server holds that a reader chose is nothing at all, until we offer to keep their personas in a vault of their own, which is the thing [worth paying for](pay-to-keep-your-persona.md).

**Personas as a design tool.** In product design, a persona has for a long time meant a fictional user that a team designs for. This turns it inside out: the persona is not a description the team keeps in a slide; it is a reading list the reader wears, and can change.

## Risks, and how the design answers them

- **A persona that reveals someone.** "Jane at Acme, interested in leaving her vendor" in a public vault is a leak. Personas about people go in private vaults, sent to them; public personas are roles.
- **A link that is forwarded.** Anyone with a private persona link can open it. That is the nature of a link, and the same as forwarding the email; the persona holds reading suggestions, not secrets. Do not put anything in a persona that the recipient would mind being forwarded.
- **A persona from somewhere else.** A private link can point at any vault. The page says plainly where the persona came from, and marks any vault that is not the newsroom's own, so a forged persona cannot pass itself off as ours.
- **A stale persona.** Every persona shows when it was last updated and by whom, and the keeper's policy says how often each is reviewed.
- **Not knowing whether it works.** There is no analytics, by design. What we will know is what readers choose to send through the share page, and whether people we send persona links to write back. That is enough for this stage.

## How to build it

1. **The vault.** Create the persona vault, publish its read key, put the five existing starting personas in it with the schema above, and keep a copy in the site as a fallback for when the vault host cannot be reached. The vault key goes to the key registry through the [send a vault key](https://sgit.ai/docs/send-a-vault-key.md) flow, never into a chat.
2. **The pages.** `/persona/` with the fragment, and a page of its own for each listed persona; both read the vault in the browser.
3. **Follow, fork and remove**, in the next version of [SG Meter](../meter/index.md): a visiting persona, a followed persona that refreshes from the vault, and a forked one that is the reader's own.
4. **The keeper.** A newsroom role with a behaviour policy: what it may change, how it records each change, and what it must never put in a public persona.
5. **Private personas.** The `v`, `k` and `p` fragment, a vault per recipient, and the plain statement of where the persona came from.
6. **Beyond articles.** Outside reading, with sources, carried by the persona.

It should be built where the newsroom is going: [newsroom.sgit.ai](https://sgit.ai/docs/briefs/newsroom-move-to-newsroom-sgit-ai.md), as the step after the reader account has moved. The vault and the schema can be made first, because they do not depend on which site reads them.

## Why this matters beyond a link

It turns every introduction into a better first visit, and it gives the newsroom a reason to write for more audiences than it has articles: the persona keeper decides what a CISO should read this week from everything published, and the CISO gets that, from a link, with nothing installed and no account. It is also a demonstration of the thing the site is about. Content that changes without a deploy, shared with exactly the people who hold the key, opened and decrypted in their browser, and kept by agents whose every change is a commit anyone with the key can read.

*Written from a voice note by Dinis Cruz, who is the author of the idea and has editorial responsibility, by a Claude Code session working as the sgit.ai newsroom, on 10 October 2026. Sources: RFC 3986, section 3.5; Bluesky's announcement of starter packs, 26 June 2024, and its FAQ; the Christian Science Monitor on Netflix Profiles, 1 August 2013; the Mastodon Migration blog's follow packs and coverage of Mastodon's announced Packs; Apple's privacy page for Apple News; Brave's page for Brave News. Apple's and Brave's descriptions of their own products are their claims, not independent audits.*

## Threads

Startups & strategyVaults & method[This article as a graph →](graphs.md#a-link-to-a-persona)

### Builds on

- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.

### Continued by

- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [Brief the agent too: the people I talk to work with agents, so what I send has to reach both](brief-the-agent-too.md) The people I advise read through agents. Content needs a second package, a brief for their agent, and memory, so it reads what changed, not everything.
- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 66 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=66)

**Posting this article on LinkedIn?** The cover is [a-link-to-a-persona.jpg](banners/a-link-to-a-persona.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-link-to-a-persona.html)*
