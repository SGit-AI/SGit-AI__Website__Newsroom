# SG Meter security model, sgit.ai

> What a reader can do to a meter kept in their own browser (edit the balance, start again, credit themselves through the unprotected return page), what each costs the site and the reader, and why every gap is accepted.

*Source: <https://newsroom.sgit.ai/meter/security.html> · sgit.ai v0.7.61 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Docs](https://sgit.ai/docs/index.md) / [SG Meter](index.md) / Security model

SG Meter · security model

# SG Meter's security model: what a reader can do to it, and why that is allowed

Everything the meter knows is in the reader's browser, so the reader controls it completely. This page lists what that lets them do, what it costs the site, and what it costs them. The short version: every way of cheating changes a number only the cheater can see, and costs the site a payment it was never going to get.

## What is being protected, and from whom

Not money. The meter never blocks a page, so there is nothing behind it to steal: a reader who never pays reads exactly what a reader who pays reads. What it protects is narrower: the reader's own history (what they read, what they declined and why) from other people, and the site's honesty about what it records. The first question of [who are you protecting against](../articles/who-are-you-protecting-against.md) applies, and the answer here is "a reader's flatmate, and our own mistakes", not "a determined attacker", because a determined attacker gains nothing. Who might try anyway, and how many of them there are, is in [who will game the reading meter](../articles/who-will-game-the-reading-meter.md).

## Known gaps, all accepted

| # | What a reader can do | Effort | What it costs the site | What it costs the reader |
|---|---|---|---|---|
| 1 | Edit their balance in the browser's developer tools (Application → Local Storage) | A minute, for someone who knows devtools exist | Nothing it would otherwise have had | Nothing |
| 2 | Open a private window or another browser and start again at £5.00 | One keystroke | Nothing | Their history and picks, which stay behind |
| 3 | Open the topped-up page with any `session_id` and get £5 of credit, once per id | Read this page, type a URL | Nothing: no money moves, and the credit is only on their screen | Nothing |
| 4 | Replay the same topped-up URL | none | Blocked: each id is credited once per browser (but a new id is trivial, see 3) | none |
| 5 | Clear site data to wipe a negative balance | Two clicks | Nothing; there was never a debt | Their history |
| 6 | Read as an agent: fetch the markdown twin or the newsroom wire | None; it is the intended route for agents | Unmetered by design, for now | none |
| 7 | Someone else on a shared computer opens the account or newsroom and sees what was read and declined, and the reader's personas | Sit down at it | none | Privacy. Mitigations: clearing this site's data in the browser removes it; a private window keeps nothing |
| 8 | A script injected into the site (XSS) reads the history | Needs a hole in the site first | Reputation | Privacy. Mitigations: the meter sets page data only as text; the only third-party code on this origin is the in-browser Python on [the try page](https://sgit.ai/try/index.md), loaded from a pinned version, so that page shares the same storage and the same trust |
| 9 | Card testing, fraud or chargebacks against the Stripe link | Ordinary payment fraud | Fees and disputes, held by Stripe's own controls (Radar) | none |

## Why the topped-up page is unprotected

Because protecting it would need a server, and the one thing a server would protect is a number on a reader's own screen that unlocks nothing. Stripe's recommended way to know a payment happened is a webhook from Stripe to a server you run, and the honest alternative to building one is to say plainly that the return page trusts its URL. So it does, and here it is said. What we did do is keep the default route the real one: every top-up button goes to the payment page, the return URL is not linked as a way to get credit, and the page adds nothing when opened without a reference.

## What would change this

- **If the balance unlocked something** (a page, a download, a reply from an agent), it would have to be held by a server or a signed receipt, and gaps 1, 3 and 5 would stop being acceptable.
- **If the history synced between devices**, it would be kept in an encrypted vault whose key only the reader holds, so the site would still not be able to read it.
- **If cheating showed up in the one place we can see** (the Stripe dashboard: payments, amounts, repeat payers), we would know the honesty box was not working, and the hypotheses in [going live with the reading meter](../articles/going-live-with-the-reading-meter.md) say in advance what number would mean that.

[← SG Meter](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/meter/security.html)*
