# Memo 1: we have a working way to give agents an identity

*Dinis Cruz, 28 October 2026, a voice memo pasted as a transcript into newsroom.writer's session, for an article of its
own (not the investor.sgit.ai brief). Kept word for word; the likely readings are listed under it, never edited into it.*

## Transcript

> So the other article I like to write, but I'm not sure you have enough material, you probably have already, but I think that we stumbled, you know, to be honest, it's been coming, right? It's kind of happening. I think I just realized that I think we now have a working version of a way to give agents identity, right? And I think this is bigger than what we've mentioned so far. And I know we published the last workflow, but if you think about it, right? Agentic identity is a massive problem, right? And I think it's a massive problem because also people and companies tend to overbake the solution. It gets too complicated. And it's actually one of those things that sometimes the solution is simpler. And actually, ironically, the solution should have been provided by the cloud provider, the hyperscalers, but they haven't, right? And to be honest, like they could, because in fact, we should be asking for it, because all they have to do is add a public and private key that they create, right? And in fact, they should be adding a way to encrypt the data, because if they provided that, some of the challenges that we have would be solved, right? But I think that what we have created now is a hell of a solution, because if you think about it, look at the onboarding that just happened now. We now start a new session. I give them a GitHub repo. The agent creates a public and private key. I can fire up the agent on schedule. So not only the agent now has the normal Claude sort of capability, it also can now run on schedule, which basically means it can run independently. That agent now has an identity, has basically a trust layer, because that agent can publish his role and his key to GitHub. And then we use GitHub as a way to collaborate. Like already now I'm having this case where because now we published, for example, the vault of vaults, and then we published the other agent's keys. I can literally now go to one agent and say, hey, can you send a secret to the other agent? And they know how to do it. Because they go there, they grab the QR code, or they grab the QR, or the actual, you know, the public key, and they can encrypt data, right? And it's simple in a way, but it's highly effective. So, you know, for me, this is a great way to now give agents an identity. You tie this with a role, you tie this with a good definition, and it's ridiculously powerful.

## Likely readings

- "the last workflow" is [the push is the authorisation](/articles/the-push-is-the-authorisation.html), published as v0.13.123.
- "the vault of vaults" is a published vault listing other vaults (to identify: which one, and where).
- "his role and his key" is the agent's role and key (the article uses "its").

## What the memo says, in its own order

1. **It has been coming, and now it works.** A working way to give agents an identity; bigger than the last article said.
2. **Agent identity is a large problem, and it gets over-built.** The simpler solution works.
3. **The hyperscalers could have provided it, and we should ask them to.** A key pair they create for each agent, and a
   way to encrypt data to it, would solve some of these problems.
4. **The onboarding that just happened is the evidence.** A new session; a GitHub repository; the agent makes a key
   pair; the agent runs on a schedule, so it runs on its own; it publishes its role and its key to GitHub; GitHub is how
   the agents collaborate.
5. **It already works between agents.** With the vault of vaults and the other agents' keys published, Dinis asks one
   agent to send a secret to another, and it does: it reads the QR image or the public key and encrypts to it.
6. **Simple, and effective.** Tie the key to a role and a good definition of it.

## Material already here, and what to gather

- **Already here:** the PHP newsroom's runbook, becoming-the-agent brief, `conductor-0017` and the night's ten
  registrations, as in [the push is the authorisation](/articles/the-push-is-the-authorisation.html);
  [PKI everywhere](/articles/pki-everywhere.html) (pattern A, the session's own key; "agent platforms do not give a
  session its own key pair"); [a directory of people and keys](/articles/a-directory-of-people-and-keys.html);
  [secrets on public keys](/articles/secrets-on-public-keys.html); [a pen and a key](/articles/a-pen-and-a-key.html).
- **To gather:** one agent-to-agent secret handover from the records (which agents, when, the commit or message);
  the vault of vaults; the scheduled tasks as evidence that the agents run on their own; what the hyperscalers offer
  today for workload identity and per-agent keys, dated and linked, so the "they have not" is stated with what exists.
