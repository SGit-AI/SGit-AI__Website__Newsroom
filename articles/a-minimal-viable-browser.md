# A minimal viable browser: why Firefox is the one that can build it, and what it would take, sgit.ai

> The browser is the biggest program most of us run, the largest attack surface on the machine, and the place we now want to put agents. It does far more than any single job needs. A kiosk running one application, an agent filling in one form, and a person reading the news all get the same enormous engine, with every feature on. This follows the argument of the code you do not ship to its most visible case. A minimal viable browser has a small kernel, reviewed hardest and changed least, and loads components only when a page or an agent needs them, so its attack surface grows only as it is used. A browser for one application has no extensions, no media and no downloads. A browser for one agent has no accounts, no extensions and no file access, which is a practical defence against prompt injection: an agent cannot leak what its browser cannot reach. And every extension runs in its own box, with only the access its job needs, instead of the "read and change all your data on all websites" that so many hold today. Several projects already do part of this, from hardened Firefox forks to headless browsers built for agents. But I think Mozilla is uniquely placed to do all of it: it has its own engine, privacy is its brand, it runs on the client, and its revenue still does not depend on knowing more about its users. The pitch to Mozilla, though, should not be security. It should be speed: a browser that only has the code it needs is a browser that starts instantly and uses a fraction of the memory.

*Source: <https://newsroom.sgit.ai/articles/a-minimal-viable-browser.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A minimal viable browser: why Firefox is the one that can build it, and what it would take

# A minimal viable browser: why Firefox is the one that can build it, and what it would take

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.2.0, 3 versions](versions/a-minimal-viable-browser.md) · [newsroom v0.12.106](https://newsroom.sgit.ai/admin/versions.html) · browsersfirefoxmozillaminimal-codeagentsprompt-injectionextensionsattack-surfacearticle

***Abstract:** The browser is the biggest program most of us run, the largest attack surface on the machine, and the place we now want to put agents. It does far more than any single job needs. A kiosk running one application, an agent filling in one form, and a person reading the news all get the same enormous engine, with every feature on. This follows the argument of the code you do not ship to its most visible case. A minimal viable browser has a small kernel, reviewed hardest and changed least, and loads components only when a page or an agent needs them, so its attack surface grows only as it is used. A browser for one application has no extensions, no media and no downloads. A browser for one agent has no accounts, no extensions and no file access, which is a practical defence against prompt injection: an agent cannot leak what its browser cannot reach. And every extension runs in its own box, with only the access its job needs, instead of the "read and change all your data on all websites" that so many hold today. Several projects already do part of this, from hardened Firefox forks to headless browsers built for agents. But I think Mozilla is uniquely placed to do all of it: it has its own engine, privacy is its brand, it runs on the client, and its revenue still does not depend on knowing more about its users. The pitch to Mozilla, though, should not be security. It should be speed: a browser that only has the code it needs is a browser that starts instantly and uses a fraction of the memory.*

A minimal viable browser: a small kernel, components loaded only when needed, and three shapes from the same engine.

Less code: a series in four parts

Code is a liability: remove what each use case does not call, apply it to the browser, and build on small blocks you did not have to write.

[1 · MeasuredThe minimum code belowOne real use case of sgit, under coverage: 428 of 1,500 files ran, and a tree of only those passed.](the-minimum-code-below.md)[2 · Less codeThe code you do not shipThe worst bugs sit in features nobody needed; models make removing them safe, and someone can be paid to keep it small.](the-code-you-do-not-ship.md)[you are here3 · The browserA minimal viable browserA small kernel and components loaded when needed: a browser for one app, one agent, or a reader, sold as speed.](a-minimal-viable-browser.md)[4 · Small blocksCloudflare as Lego blocksStorage, compute, models, email and identity as blocks, and an sgit vault server in 83 lines.](cloudflare-as-lego-blocks.md)

## In short

- **The browser is the biggest attack surface we run.** And now we want to give it to agents.
- **One engine, every feature on, for every job.** A kiosk, an agent and a reader all get the same.
- **A minimal viable browser.** A small kernel, and components loaded only when needed.
- **A browser for one agent is a prompt-injection defence.** An agent cannot leak what its browser cannot reach.
- **Every extension in its own box.** Only the sites and the powers its job needs.
- **Parts of this exist.** Hardened forks, headless browsers for agents, kiosk modes.
- **Mozilla can do all of it.** Its own engine, a privacy brand, the client, and money not tied to profiling.
- **Sell it as speed, not security.** Only the code it needs starts instantly.

## The biggest program we run

The browser is where most of us spend the day, and it carries every capability the web has ever needed: a JavaScript engine with a just-in-time compiler, WebAssembly, WebGL, media codecs, PDF, fonts, downloads, extensions, sync, accounts. A page that shows text and a form gets all of it, on, by default.

The cost of that shows up in the bug counts. In May, Mozilla wrote that it [fixed 423 security bugs in Firefox in April 2026](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/), against roughly 20 to 30 a month through 2025. 271 of them were found with an Anthropic model and fixed in Firefox 150: 180 rated high, 80 moderate, 11 low. A number of them were sandbox escapes, written assuming the content process was already compromised and going after the privileged parent process through IPC, IndexedDB and image decoding. Chrome is seeing the same: one update on 6 October 2026 [fixed 247 vulnerabilities](https://www.malwarebytes.com/blog/bugs/2026/10/update-chrome-and-chromeos-to-fix-critical-security-issues). Counted from NVD by the organisation that filed them, Google's Chrome team filed 202 CVEs in 2025 and 3,246 in 2026 up to 17 October; Mozilla's filed 213 and 675 (Mozilla's also cover Thunderbird and other products). This is [the code you do not ship](the-code-you-do-not-ship.md) argument at its largest: models now find what was always there, and every feature in the engine is a place to look.

The vendors already know that less code is safer, because they ship it as a mode. Microsoft Edge's [enhanced security mode](https://learn.microsoft.com/deployedge/microsoft-edge-security-browse-safer) turns off the V8 just-in-time compiler, after Microsoft said in 2021 that [45% of V8 CVEs in 2019 were JIT-related](https://therecord.media/microsoft-announces-new-super-duper-secure-mode-for-edge/). GrapheneOS's Vanadium browser has the [JIT disabled by default](https://grapheneos.org/features), with a per-site toggle. Apple's [Lockdown Mode](https://support.apple.com/en-us/105120) blocks "certain complex web technologies". Tor Browser's Safest level turns off JavaScript altogether. Each is a minimal browser for one threat, switched on by hand. What does not exist is the general version: a browser that starts small and only grows when it has to.

## What a minimal viable browser looks like

The shape is the same as [the minimal viable code path](the-code-you-do-not-ship.md#path), applied to one program.

- **A small kernel.** Networking, TLS, parsing, layout, and process isolation. This is the part that is reviewed hardest and changed least.
- **Components, loaded when needed.** JavaScript, with or without the JIT; WebAssembly; media; WebGL; PDF; downloads; extensions; sync. A page or an agent asks for one, and the browser loads it, for that site.
- **A profile that says what it is for.** One application, one agent, or a person browsing. The profile decides what can be loaded at all.

Three browsers come out of the same engine. A browser for one application has no extensions, no media and no downloads: a kiosk, a till, an internal tool. A browser for one agent has the same, plus no accounts and no file access. And the reader's own browser loads what they use as they use it, with each extension in its own box.

Firefox has had pieces of this, and dropped some of them. It had a site-specific browser, behind a hidden preference, and [removed it in Firefox 86](https://bugzilla.mozilla.org/show_bug.cgi?id=1682593) in 2021, [citing](https://www.thurrott.com/dev/246716/firefox-85-is-here-but-mozilla-is-killing-pwa-features) known bugs and weak user research. It has a kiosk mode, started with `--kiosk`. It has had [site isolation](https://wiki.mozilla.org/Project_Fission) on for every desktop user since Firefox 95, which is the process boundary a component model needs. And Servo, the engine Mozilla started in Rust, is now an [embeddable library](https://servo.org/blog/2026/04/13/servo-0.1.0-release/), published as 0.1.0 in April 2026 under Linux Foundation Europe.

## A browser for one agent

This is where the argument stops being about tidiness. We are now giving browsers to agents, and the agent reads everything the page says.

The vendors say plainly that this will not be fixed. OpenAI wrote in December 2025 that prompt injection, "much like scams and social engineering on the web, is unlikely to ever be fully 'solved'" ([TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)). Google's Chrome security team wrote in December 2025 that ["the primary new threat facing all agentic browsers is indirect prompt injection"](https://blog.google/security/architecting-security-for-agentic/). Gartner told most organisations to [block AI browsers for now](https://www.theregister.com/2025/12/08/gartner_recommends_ai_browser_ban/).

The incidents show where the damage comes from. In March 2026, Zenity Labs disclosed [PleaseFix](https://www.businesswire.com/news/home/20260303909038/en/Zenity-Labs-Discloses-PleaseFix-Vulnerability-Family-in-Perplexity-Comet-and-Other-Agentic-Browsers), a zero-click hijack of Perplexity's Comet through a calendar invite that reached local files and password-manager workflows. The fix was to restrict `file://` access: not a smarter model, a smaller browser. At Black Hat in August, the same researchers showed [zero-click chains](https://www.darkreading.com/cyber-risk/ai-browsers-zero-click-agent-hijacking) against the agents in Chrome, Edge, Comet and ChatGPT Atlas; some vendors patched, others called it intended behaviour.

The better defences already point the same way. Atlas has a logged-out mode that runs the agent with no cookies or logins. Brave runs its AI browsing [in an isolated profile](https://brave.com/blog/ai-browsing/) with its own cookies and storage, and recommends isolating agentic browsing from normal browsing. Chrome adds Agent Origin Sets, which limit the sites an agent's task can touch, and a second model that checks proposed actions.

A minimal browser makes that the default rather than a setting. An agent's browser that has no accounts, no extensions, no file access and only the origins its task needs cannot leak a password it never had or a file it cannot open. In the terms of [what can your agent reach](what-can-your-agent-reach.md), the grant shrinks to the mandate, and the injection that gets through finds nothing to take.

## Every extension in its own box

Extensions are the part of the browser that users add, and they are where much of the recent damage came from. LayerX's 2025 report found [99% of enterprise users](https://go.layerxsecurity.com/hubfs/LayerX_Enterprise_Browser_Extension_Security_Report_2025.pdf) have an extension installed, and 53% have at least one with high or critical permissions.

The pattern in the incidents is not malicious code at install. It is a trusted extension that changes. Koi's ShadyPanda report, as [The Hacker News relayed it](https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html), covers about 4.3 million installs across 145 extensions (20 for Chrome and 125 for Edge, Koi's count of one phase), some of them "Featured" or "Verified", that were legitimate for years and then were weaponised through auto-update. Urban VPN Proxy, with a Featured badge, [began harvesting every prompt and reply](https://www.theregister.com/2025/12/16/chrome_edge_privacy_extensions_quietly/) on ChatGPT, Claude, Gemini and Copilot from a July 2025 update, with no off switch. Firefox is not immune: Koi's later [DarkSpectre](https://cybernews.com/security/darkspectre-malicious-browser-extension-campaign/) attribution includes Firefox add-ons.

An extension in its own box gets only the sites and the powers its job needs, and a change to either is a new request, not a silent update. Firefox has started down this road. In Manifest V3 it made host permissions [opt-in and controllable per site](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_host_permissions), and new extensions must declare their [data collection](https://blog.mozilla.org/addons/2025/10/23/data-collection-consent-changes-for-new-firefox-extensions/) at install. It has also [kept the blocking webRequest API](https://blog.mozilla.org/addons/2024/03/13/manifest-v3-manifest-v2-march-2024-update/) that Chrome removed, which is why full uBlock Origin still runs on Firefox. The next steps are a process per extension, and a permission model that is an [Agent Behaviour Policy](three-policies-for-an-agent.md) in all but name: what this extension may do, on which sites, and who approved it.

## Parts of this exist

None of this is new as an idea, and much of it ships today, in pieces.

- **Hardened Firefox builds.** LibreWolf, with less telemetry; Mullvad Browser, built with the Tor Project for anti-fingerprinting; Tor Browser itself; Waterfox, which ships with no AI.
- **Smaller Firefox interfaces.** Zen, with about 45,000 stars on GitHub, and Floorp.
- **A paid minimal browser.** [Brave Origin](https://www.privacyguides.org/news/2026/06/07/brave-launches-paid-minimalist-brave-origin-browser/), launched in June 2026 for about $60 one-time, removes the AI assistant, news, rewards, wallet, VPN, Tor and playlist and keeps the blocker. People will pay for less.
- **Chromium with things taken out.** [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium), and Vanadium, with the JIT off.
- **New engines.** [Ladybird](https://ladybird.org/), still in development and funded by donations, and Servo.
- **Browsers for machines.** [Lightpanda](https://github.com/lightpanda-io/browser), written from scratch for agents and automation; Chrome's [headless shell](https://developer.chrome.com/blog/chrome-headless-shell), a separate thin binary; and hosted browsers such as Cloudflare's [Browser Rendering](https://developers.cloudflare.com/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/).
- **Shells for one app.** [Tauri](https://v2.tauri.app/start/) uses the system web view, and says a minimal app can be under 600KB.

What is missing is the same engine, from the same vendor, in all three shapes, with the components as the unit.

## Why Mozilla

I think Mozilla is better placed than anyone to build this, for four reasons.

**It has its own engine.** Gecko is the only independent engine with a large user base that is not Chromium or WebKit. A component model goes all the way down into the engine; a fork of someone else's cannot set that direction.

**Privacy is the brand.** Mozilla's [state of Mozilla](https://stateof.mozilla.org/ledger) report puts Firefox at about 200 million monthly users, and the company has already shipped the instinct this needs: Firefox 148 added a [switch that turns off](https://blog.mozilla.org/en/firefox/ai-controls/) current and future generative AI features. Its [Smart Window](https://blog.mozilla.org/en/firefox/firefox-smart-window/) is opt-in and does not act on pages yet. That is a company that already sells "you choose what runs".

**It runs on the client.** An agent's browser that holds nothing and reaches only what it needs is a client-side product. It does not need a server that sees the browsing, which is the same design as [sgit](from-send-to-sgit.md).

**Its money does not come from knowing more about you.** Here the memo needs a correction: Mozilla's revenue is not independent. Mark Surman said in April that search was until recently [about 95 to 98% of revenue](https://www.medianama.com/2026/04/223-mozilla-ai-search-future-revenue-diversification-mark-surman/), with privacy-preserving ads now about 10 to 12%, and most of the search money comes from Google. The court remedies in the Google case let those payments continue but limit default deals to one year at a time, and both sides have appealed. What holds is the part that matters here: Mozilla is paid for a search box, not for profiling its users, and it has [about $1.4 billion in reserves](https://stateof.mozilla.org/ledger) and a plan to run its products as separate companies, each with its own accounts. A minimal browser for agents and applications is a product someone pays for directly, the way Brave Origin is, and it is the kind of revenue Mozilla says it wants.

## Sell it as speed

The pitch to Mozilla should not be security. Security has rarely been enough to make people switch browsers, and Firefox at [2.8% of the market](https://gs.statcounter.com/browser-market-share/monthly/worldwide) in September 2026 knows it.

The pitch is that a browser with only the code it needs is fast. It starts at once, it uses a fraction of the memory, and an agent can run many of them. Lightpanda's own benchmark, which is the vendor's, claims 123MB against 2GB of peak memory for 100 pages, and 5 seconds against 46. A kiosk that boots in a second, an agent that opens a hundred clean browsers on a laptop, a reader whose browser does not load a PDF engine until they open a PDF: those are features people notice. The security comes with them, the way [encryption made sgit better](the-value-of-constraints.md) rather than being the reason to use it.

Firefox now ships every two weeks, from Firefox 155. A component that loads on demand is a component that can ship, and be pulled, on that cadence too.

## What this does not claim

- **No minimal viable browser exists in this form.** The pieces do; the design is a proposal.
- **Mozilla has not said it will build it.** Nothing here is from Mozilla beyond what is linked.
- **Smaller is not safe.** A kernel still has bugs, and an agent with no file access can still be talked into a bad form submission.
- **The CVE counts are ours.** Counted from NVD by filing organisation on 18 October 2026; the 2026 rise reflects AI-assisted bug finding as much as new bugs.
- **Some figures are the vendor's own.** Lightpanda's benchmark, Brave's and Mozilla's user counts, LayerX's survey.
- **Mozilla's 2024 and 2025 revenue split is from interviews and its ledger page.** Its ledger page links its 2024 audited statements.
- **Loading components on demand has costs.** Fingerprinting is one: a browser that loads different parts for different sites can look different to each, which is why Mullvad removed its security-level button.

If you work on a browser and want to try a component model for agents, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026. The research, read on 18 October 2026: Mozilla, [hardening Firefox](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/), 7 May 2026; [state of Mozilla 2025/26](https://stateof.mozilla.org/ledger) and [its blog post](https://blog.mozilla.org/en/mozilla/state-of-mozilla-25-26/), 27 January 2026; [AI controls](https://blog.mozilla.org/en/firefox/ai-controls/); [Smart Window](https://blog.mozilla.org/en/firefox/firefox-smart-window/), 18 August 2026; [Manifest V3 update](https://blog.mozilla.org/addons/2024/03/13/manifest-v3-manifest-v2-march-2024-update/), 13 March 2024; [data collection consent](https://blog.mozilla.org/addons/2025/10/23/data-collection-consent-changes-for-new-firefox-extensions/), 23 October 2025; [Project Fission](https://wiki.mozilla.org/Project_Fission); MediaNama, [interview with Mark Surman](https://www.medianama.com/2026/04/223-mozilla-ai-search-future-revenue-diversification-mark-surman/), 4 April 2026; StatCounter, [browser market share](https://gs.statcounter.com/browser-market-share/monthly/worldwide), September 2026; Servo, [0.1.0](https://servo.org/blog/2026/04/13/servo-0.1.0-release/), 13 April 2026; Microsoft, [browse safer with Edge](https://learn.microsoft.com/deployedge/microsoft-edge-security-browse-safer), and The Record on [the 2021 JIT figure](https://therecord.media/microsoft-announces-new-super-duper-secure-mode-for-edge/); GrapheneOS, [features](https://grapheneos.org/features); Apple, [Lockdown Mode](https://support.apple.com/en-us/105120); OpenAI's statement as reported by [TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/), 22 December 2025; Google, [architecting security for agentic capabilities in Chrome](https://blog.google/security/architecting-security-for-agentic/), 8 December 2025; Brave, [AI browsing](https://brave.com/blog/ai-browsing/) and [unseeable prompt injections](https://brave.com/blog/unseeable-prompt-injections/), 21 October 2025; Zenity Labs, [PleaseFix](https://www.businesswire.com/news/home/20260303909038/en/Zenity-Labs-Discloses-PleaseFix-Vulnerability-Family-in-Perplexity-Comet-and-Other-Agentic-Browsers), 3 March 2026; Dark Reading, [zero-click agent hijacking](https://www.darkreading.com/cyber-risk/ai-browsers-zero-click-agent-hijacking), August 2026; The Register, [Gartner on AI browsers](https://www.theregister.com/2025/12/08/gartner_recommends_ai_browser_ban/), 8 December 2025, and [Urban VPN](https://www.theregister.com/2025/12/16/chrome_edge_privacy_extensions_quietly/), 16 December 2025; LayerX, [extension security report 2025](https://go.layerxsecurity.com/hubfs/LayerX_Enterprise_Browser_Extension_Security_Report_2025.pdf); The Hacker News on [Koi's ShadyPanda report](https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html), December 2025; Cybernews, [DarkSpectre](https://cybernews.com/security/darkspectre-malicious-browser-extension-campaign/); Privacy Guides, [Brave Origin](https://www.privacyguides.org/news/2026/06/07/brave-launches-paid-minimalist-brave-origin-browser/), 7 June 2026; Malwarebytes, [Chrome update](https://www.malwarebytes.com/blog/bugs/2026/10/update-chrome-and-chromeos-to-fix-critical-security-issues), October 2026; Thurrott on [Firefox 85](https://www.thurrott.com/dev/246716/firefox-85-is-here-but-mozilla-is-killing-pwa-features); Lightpanda, [repository](https://github.com/lightpanda-io/browser); Chrome, [headless shell](https://developer.chrome.com/blog/chrome-headless-shell); Tauri, [start](https://v2.tauri.app/start/); NVD, CVE counts by source identifier. Related: [the code you do not ship](the-code-you-do-not-ship.md), [what can your agent reach](what-can-your-agent-reach.md), [cloudflare as Lego blocks](cloudflare-as-lego-blocks.md), [the value of constraints](the-value-of-constraints.md). Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#a-minimal-viable-browser)

### Builds on

- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults](from-send-to-sgit.md) Eight months of SG/Send, checked against its own briefs and commits: how file sharing became sgit and vaults, the pace, and what the market said.
- [The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think](the-value-of-constraints.md) sgit's encryption and open source matter less as features than as constraints: they remove the temptations that lead to server code, lock-in and bad decisions.
- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.

### Continued by

- [A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working](a-browser-for-one.md) An iPhone app that only reads my newsroom: WebKit in the UK, a paid membership and a Mac to build it, one passkey test first, and someone else to maintain it.
- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 179 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=179)

**Posting this article on LinkedIn?** The cover is [a-minimal-viable-browser.jpg](banners/a-minimal-viable-browser.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-minimal-viable-browser.html)*
