---
title: Simple on top of years: why a startup has to find something very easy, very narrow and able to scale, why building from the bottom up, from provenance, understanding and determinism, ended in a simple product anyway, and how a website in five designs opened from a QR code sits on a CI pipeline, zero-knowledge sharing, sgit, vaults, keys and agentic teams, each learnt on its own
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: My view of startups has always been that you have to find something very easy: a narrow use case, at scale, that somebody can just use. What is odd is how I got to one. For the last couple of years I have been building from the bottom up, starting from provenance, from understanding and from determinism, because I do not want the black magic. You would expect that to end in something complicated. It ended in something simple: a person scans a QR code and sees their own website in five designs, and if they say yes it becomes theirs, with a team of agents inside it. That simple thing sits on layers I learnt one at a time, each for its own reason: a CI pipeline and tests on every change, almost the first thing I built; a file-sharing service where the server never holds the key, which taught me pricing and payments and also that "the technology worked, the use case was not there yet"; sgit, Git's model encrypted; vaults a web page can open; keys and secrets as QR codes; agentic teams with briefs and behaviour policies; and a factory that turns one commit into a site. None was built for this. Connecting them is the product, and the learning is the moat.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: startups, strategy, sovereign-website, sgit, agentic, determinism, article
status: published
---

!shot sty-layers.webp | images/ | Simple on top, years underneath: the layers under a website opened from a QR code. | concept

## In short {#in-short}

- **A startup needs something very easy:** narrow, at scale, that somebody can just use.
- **I built from the bottom up:** provenance, understanding, determinism, no black magic.
- **It ended in something simple anyway:** your website, five designs, from a QR code.
- **Each layer under it was learnt on its own,** for its own reason.
- **Connecting them is the product;** the learning is the part nobody can copy.

## What a startup needs {#need}

I have said it for a long time: a startup has to find something super easy. A narrow use case, one that can scale, that somebody can just use, without a meeting, a manual or a migration. The ideas that fail are rarely bad ideas; they ask too much of the person before they give anything back.

I learnt that the hard way this year too. SG/Send, the file-sharing service that became sgit, had paying customers within a month of its first commit, and by 5 March its own briefs said it plainly: "Users buy credits, test once, and don't come back." The technology worked. The use case was not there yet ([from sending a file to sgit](/articles/from-send-to-sgit.html)).

## From the bottom up {#bottom-up}

The odd thing is the direction I came from. I have been starting from the bottom: from provenance, where everything came from and who changed it; from understanding, being able to explain every step; and from determinism, the same inputs giving the same result. I do not want the black magic, the parts that work but nobody can say why.

You would expect that to end in something complicated, a platform for engineers. It ended in the opposite. A person scans a QR code and sees their own website, in five designs, made by agents ([your website, from a vault](/articles/your-website-from-a-vault.html)). If they say yes, it becomes theirs, with a team of agents inside it ([a website with a team inside](/articles/a-website-with-a-team-inside.html)). That is about as easy as it gets.

## The layers {#layers}

None of the layers was built for this. Each was learnt on its own, for its own reason, and that is the point:

- **CI, tests and a release on every change** was almost the first thing I built, and everything since runs on it: this newsroom releases about ten times a day because every change is checked ([the second run](/articles/the-second-run.html)).
- **Zero knowledge:** SG/Send's first specification, on 8 February, said the decryption key is never sent to the server. That rule is why a demo can now sit in a vault that nobody but its recipient can read.
- **Selling it:** taking SG/Send to market taught me Stripe, pricing and everything else a real product needs, by 2 March, long before the newsroom needed it.
- **sgit,** Git's model with everything encrypted, named on 16 March, so that work and its history live in a vault.
- **Vaults a web page can open,** file by file or as an app in a sandbox ([how a vault works](/articles/how-a-vault-works.html)), which is what makes a website in a vault possible.
- **Keys and secrets as QR codes,** tried on 21 October ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)), which is how a demo reaches someone.
- **Agentic teams,** with briefs, roles and a behaviour policy for every agent ([governance from zero](/articles/governance-from-zero.html)), which is who builds the five designs.
- **The site factory,** one commit to a repository, an address and its owner ([the site factory works](/articles/the-site-factory-works.html)), which is how a demo becomes a real site.

## Connecting the dots {#dots}

I could connect them because I had lived each one. I was experiencing it, learning how to use Claude, learning how each piece behaves when it fails. Nobody planned a demo opened from a QR code in February; it became possible only because each layer was already there, tested and understood, when the idea arrived.

That is also why I am not in love with any of the technology. The open source habit is to make things easier and simpler, and to drop whatever stands in the way. A layer earns its place by making the thing on top simpler for the person using it.

## Why this is the moat {#moat}

Almost all of this is open source, so anyone can copy the code. What they cannot copy is the order in which it was learnt, or the speed that comes from having learnt it: PrompTugal's investment case says it in one line: "A competitor who forks our code gets our position as of today", not our velocity. The simple product on top is what sells. The years underneath are why it works, and why we can keep making it simpler.

## What this does not claim {#limits}

- **The dates are as recorded** in this newsroom's articles and their sources; most layers kept changing after them.
- **The demo pipeline and the vault drop page are not built yet;** the layers under them are.
- **"Simple" is a claim about the person's experience,** not about what runs underneath.

## Where this comes from {#sources}

My own thinking, in writer-10's session on 19 November 2026. The dates and quotes come from [from sending a file to sgit](/articles/from-send-to-sgit.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [how a vault works](/articles/how-a-vault-works.html), [the site factory works](/articles/the-site-factory-works.html) and [the second run](/articles/the-second-run.html); PrompTugal's investor deck, The investment case (slide 7), in its public repository; related: [governance from zero](/articles/governance-from-zero.html), [a team like this](/articles/a-team-like-this.html), [your website, from a vault](/articles/your-website-from-a-vault.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html).
