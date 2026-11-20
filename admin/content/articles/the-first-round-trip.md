---
title: The first round trip: a sovereign website made for Kate Curtis-Evans during our call, five designs from a design agent of its own, then handed over so she edits it herself from her own Claude, the friction that took multiple rounds to get through, what it says about over-privilege, and the next step, a signed and sealed channel from her site straight to the agent
date: 2026-11-20
author: Dinis Cruz
author_url: about/index.html
summary: Earlier today we had the first complete round trip of Sovereign Website with someone from outside. Kate Curtis-Evans, a founder I am collaborating with, understood the idea at once; I asked if she wanted a website, she said yes, and it was made during our call, in five designs, with a design agent that now runs on its own and on a schedule doing much better than design done inside the builder's session. Then the handover: Kate has a GitHub account, and the goal is that she edits her own site from her own Claude. It worked, and her Claude pushed its first change about 35 minutes after she accepted the invitation, but it was far harder than it should have been, and it took multiple rounds. Our earlier users were from the summit and already in the organisation; Kate was the first from outside, and getting her in meant making her a member of the organisation, a small piece of the over-privilege our platforms force on everyone. That is the lesson of always shipping: you only find where the friction is by doing it end to end. And it showed the next step: before anyone touches GitHub, a channel from the site itself to the agent, signed with a key the owner gets by QR code and sealed so only the agent can read it, the way VoiceDebrief already sent a message from an iPad to the conductor and got the answer back.
version: v0.14.186
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, handover, design-agent, github, append-lanes, always-be-shipping, article
status: published
---

!shot kfr-home.webp | images/ | Kate's site, made during our call: The Workflow Board, one of five designs. | screenshot

## In short {#in-short}

- **The first round trip with someone from outside:** a site made, handed over and edited by its owner.
- **Made during the call,** in five designs, from a [hub](https://hub.sovereignweb.site/) entry to a live address.
- **A design agent of its own,** running by itself and on a schedule, did much better than design inside the builder.
- **The handover worked,** her Claude's first change about 35 minutes after she accepted, but it took multiple rounds.
- **The friction was over-privilege:** she had to become a member of the organisation.
- **Next, a channel from the site to the agent,** signed by a key from a QR code, sealed for the agent.

## What happened {#what}

[Kate Curtis-Evans](https://kate-curtis-evans.founder.sovereignweb.site/) is a practising legal transcriber who built a live transcription platform, Audio Genius, without knowing how to code, and is now looking for a technical co-founder. She is a great founder, and I am collaborating with her. When I explained Sovereign Website, she understood the value at once: a site that is hers, its files, its history and its address. I asked if she wanted one. She said yes, and we made it during our call.

The site's own history tells the rest. The material went in at 14:33 UTC, the first draft at 14:37, eight design rounds through the afternoon, the handover page at 15:15, and from 16:30 six changes pushed by Kate's own Claude. It is listed on the [hub](https://hub.sovereignweb.site/) as handed over: "Kate edits it herself on GitHub, since 20 Nov 2026."

## A design agent of its own {#design}

This is a clear example of the power of separate agents. The first round of design, done by the agent building the site inside its own session, was fine, but not very good. In the past we gave design a whole session of its own. This time I made a design agent that is focused only on design and runs by itself, and it is now on a schedule, improving the designs of every site. Its rounds are in the history, from contrast and target fixes to "Round 6, wow not bland: visual chooser and four bold redesigns". The result is five designs of the same facts, from a workflow board to a printable brief ([a website that is her](/articles/a-website-that-is-her.html)).

## The handover {#handover}

!shot kfr-start.webp | images/ | The start page: Kate's step-by-step takeover, rewritten from what tripped her up. | screenshot

The end point is simple to say: the customer edits their own site, from their own Claude or ChatGPT, on GitHub ([the website cell](/articles/the-website-cell.html)). Kate has a GitHub account, so we tried. It worked: her Claude changed the photo credit, committed and pushed it, and it was live in about a minute. That is the whole flow, end to end, and a major milestone.

But it was far harder than it should have been, and it took multiple rounds. The site's [handover notes](https://github.com/SovereignWebsite/Site__Founder__Kate-Curtis-Evans/blob/dev/docs/handover.md) list what tripped her up: a warning that GitHub had refused Claude's check of her access, a settings page only an organisation owner could use, a "Switch GitHub account" button she did not need, a first clone that was read-only, and terminal steps that were not available to her in the browser.

## The power of always shipping {#shipping}

Sovereign Website is only days old. It would have been easy to wait. But this is exactly why you ship as soon as something is a bit ready: our earlier users were from the summit and were already in the organisation, so none of this had shown up. Kate was the first from the outside world. People think these things just happen. They do not: doing it end to end is the only way to find where it should be easy and is not, and that is where the real product gets made. The start page has already been rewritten in the order that worked.

## Over-privilege, again {#privilege}

Part of the fix was to make Kate a member of the organisation, with the organisation's base permission set to none so membership gives her nothing beyond her own repository. It works, but why should a customer need to join our organisation to edit her own site? That is the typical over-privilege that today's authentication and authorisation push on everyone: to get one thing to work you grant more than it needs, and that gap is where problems come from ([feature behaviour policies](/articles/feature-behaviour-policies.html)).

## Next: talk to the agent from the site {#channel}

!shot kfr-message.webp | images/ | Message the site's agent: signed with the owner's key, sealed so only the agent can read it. | screenshot

The handover showed that GitHub cannot be the first step. So the first step becomes the site itself. The owner, or a future owner, talks directly with an agent from my team, from their own site:

- **An inbox lane.** Requests from the site arrive in an append lane ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)), are logged on a board, reviewed, and sent to the agent's lane.
- **A key by QR code.** The owner's browser makes its own key pair, and a QR code carries the authorisation that lets that key speak ([a key for every person](/articles/a-key-for-every-person.html)). Messages are signed by the owner and sealed for the agent.
- **Replies back.** Append lanes have read keys, so the answer comes back the same way: almost a chat between the owner and Claude.
- **Within a policy.** The agent acts only on messages signed by the owner or me, and only on words, tasks and photos; everything else is kept as a note.

The first version of that page is already on Kate's site; I still need to try it. And we have done this before: in VoiceDebrief, on the iPad app, with Apple's built-in transcriber and a little Apple Intelligence, I sent a message from the iPad to the conductor through an append lane and received the answer through another ([build on VoiceDebrief](/articles/build-on-voicedebrief.html)). Sometimes an experiment turns out to be the prototype of something else.

## The milestones {#milestones}

1. **The design moment:** five designs, and "wow, this is really cool".
2. **The first change:** from the site, by message, and "wow, I can make changes": a few images, more material.
3. **The transition:** only then, moving to their own Claude, ChatGPT or another way to edit, and the environment made theirs.

## What this does not claim {#limits}

- **One founder, one afternoon.** The times are from the site's own history.
- **The message page is a first version,** not yet tried end to end.
- **The organisation membership is a workaround,** not the design we want.

## Where this comes from {#sources}

My debrief in writer-10's session on 20 November 2026, Kate's site at [kate-curtis-evans.founder.sovereignweb.site](https://kate-curtis-evans.founder.sovereignweb.site/), its public repository [Site__Founder__Kate-Curtis-Evans](https://github.com/SovereignWebsite/Site__Founder__Kate-Curtis-Evans) (its history and docs/handover.md), and the [hub](https://hub.sovereignweb.site/), read that day. Related: [a website that is her](/articles/a-website-that-is-her.html), [the website cell](/articles/the-website-cell.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [a key for every person](/articles/a-key-for-every-person.html), [build on VoiceDebrief](/articles/build-on-voicedebrief.html).
