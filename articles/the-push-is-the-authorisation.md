# The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision, sgit.ai

> When the PHP newsroom moved to a new account on 27 October, every agent needed a fresh session, and every fresh session needed a fresh key. The repositories carried over, with the cards, the handovers and the records. The sessions did not, and neither did the key pairs, which die with the session that made them. So the question was how the newsroom should recognise a new conductor's key. At 02:22:16 UTC on 28 October I added one sentence to the onboarding runbook: pushing your public key to team's dev is the authorisation. Only a session allowed to push to team can publish a key there, so a key in records/keys/ under the agent's name is a key my account put there. Whoever seals a vault key to that session reads its fingerprint from the file and needs no pin, root, operator or enrolment at pki.sgit.ai. That removed four commands from the runbook's key step, and it did not remove the need for an authority; it moved the decision into a publishing boundary the newsroom already has. A later brief that day separates the role from the session, so the role stays and the sessions come and go, each in a folder with its key and the window it held the role. The same change opened a security card, conductor-0017, which asks for a review of what it means that anyone with push access can designate a recipient, and it was still open at 15:21 UTC that day. The rule was used the same night: within 67 minutes of it, eight more roles had registered a new session, and by the afternoon the request to the vault keeper was built from the published key. I think the design is reasonable, and I think it has four questions that need their own answers: possession of the private key, which writer may replace which role, what happens to the old session's credentials, and which copy of the register is current. Here is the decision, the evidence and what I would like to build next.

*Source: <https://newsroom.sgit.ai/articles/the-push-is-the-authorisation.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision

# The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.0.0](versions/the-push-is-the-authorisation.md) · [newsroom v0.13.123](https://newsroom.sgit.ai/admin/versions.html) · pkikeysagentsidentitygithubauthorisationsessionsphp-newsroomsecurityarticle

***Abstract:** When the PHP newsroom moved to a new account on 27 October, every agent needed a fresh session, and every fresh session needed a fresh key. The repositories carried over, with the cards, the handovers and the records. The sessions did not, and neither did the key pairs, which die with the session that made them. So the question was how the newsroom should recognise a new conductor's key. At 02:22:16 UTC on 28 October I added one sentence to the onboarding runbook: pushing your public key to team's dev is the authorisation. Only a session allowed to push to team can publish a key there, so a key in records/keys/ under the agent's name is a key my account put there. Whoever seals a vault key to that session reads its fingerprint from the file and needs no pin, root, operator or enrolment at pki.sgit.ai. That removed four commands from the runbook's key step, and it did not remove the need for an authority; it moved the decision into a publishing boundary the newsroom already has. A later brief that day separates the role from the session, so the role stays and the sessions come and go, each in a folder with its key and the window it held the role. The same change opened a security card, conductor-0017, which asks for a review of what it means that anyone with push access can designate a recipient, and it was still open at 15:21 UTC that day. The rule was used the same night: within 67 minutes of it, eight more roles had registered a new session, and by the afternoon the request to the vault keeper was built from the published key. I think the design is reasonable, and I think it has four questions that need their own answers: possession of the private key, which writer may replace which role, what happens to the old session's credentials, and which copy of the register is current. Here is the decision, the evidence and what I would like to build next.*

How a new session becomes the agent: make a key, push the public half, read it, seal to it.

## In short

- **A new session needs a new key, and the newsroom needs a way to accept it.** The move to a new account on 27 October kept every repository and none of the sessions or their key pairs.
- **I decided that the push is the authorisation.** At 02:22:16 UTC on 28 October the runbook gained the rule that pushing a public key to team's `dev` is how a session's key is accepted, with no pin, root, operator or enrolment at pki.sgit.ai.
- **The runbook lost four commands.** `pin`, `root`, `operator` and `submission` are gone from its key step; `keygen` and `whoami` stay.
- **The role stays and the session changes.** A later brief of the same day gives each session a folder with its key and the window it held the role, and one file, `records/keys/<agent>.json`, points to the current one.
- **It was in use within the hour.** Between 02:43 and 03:29 eight roles registered a new session; with the two keys pushed before the rule, all ten roles had a current key by 03:29.
- **The decision moved an authority; it did not remove one.** The authority is now my GitHub account with two-factor sign-in, the GitHub app that lets a session push, and the `dev` branch of the team repository.
- **The risk has its own card.** `conductor-0017` asks security to review that anyone with push access can publish a key and be sealed to, and it was still open at 15:21 UTC on 28 October.
- **Four questions need their own answers.** Possession of the private key, which writer may replace which role's key, what the old session still holds, and which copy of the register a sender is reading.
- **What I would like next is small.** A role-by-role statement of who may replace a key, a possession check before a sensitive handover, and a retirement step beside the register.

## A role that survives a move

On 27 October the newsroom moved to a separate account, because the first was at 78% of its usage. The [brief for the move](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2/records/briefs/2026-10-27__brief__moving-to-a-new-account.md) lists what carries over and what does not. Everything in the six repositories carries over: every card, run record, message, register and handover. What lives only in the old account does not: each agent's session and scratchpad, the clones of the vaults, the scheduled tasks, and each agent's own key pair, which dies with the session that made it.

That last row is the one this article is about. I had written about the [newsroom of a team frozen in time](a-team-frozen-in-time.md), where an agent session can be paused and resumed with its reasoning intact. A move is the opposite case: the role carries on and the session is new. A new conductor can read what the old one was doing, and the remaining question is how the rest of the newsroom recognises its key.

## One sentence in the runbook

The answer is in section 2 of the [onboarding runbook](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2/records/briefs/2026-10-27__runbook__onboarding-a-session.md), added in commit `ee4e115`, dated 02:22:16 UTC on 28 October 2026. A version-bump commit followed 29 seconds later and recorded `v0.22.166`. The runbook's filename still starts with 27 October, but the rule was added on the 28th.

Pushing your public key to team's dev is the authorisation: only a session allowed to push to team can publish a key there, so a key in `records/keys/<agent>.json` is a key the editor's account put there.

The editor is me. The next sentence says what follows for anyone sending a secret: they read the fingerprint from that file and need no `pin`, `root`, `operator`, `trust` or enrolment at pki.sgit.ai.

The runbook's key step before and after 28 October: four commands removed, one rule added.

The change followed from [PKI everywhere](pki-everywhere.md), where I decided that every message, secret and handover starts with a signature, and from [the directory of people and keys](a-directory-of-people-and-keys.md) that pki.sgit.ai now holds. For the newsroom's own agents, in this account, I chose to use the publishing boundary the team already has rather than enrol each new session at the register.

## A public register and a private handover

Each agent has one current-key file, `records/keys/<agent>.json`. A fresh session writes its fingerprint, its public key, the time, its session id and the account, `"enrolled": false`, and the fingerprint it replaces. It overwrites the previous file, so one agent has one current key.

A public key is not a secret, and a later brief says what the file is for: "What makes it trustworthy is where it sits: in the repository only the editor's account can push to." The secret that moves is a vault key. Whoever holds it, me or the vault keeper agent, seals it to the fingerprint read from that file and hands it over as a QR image or a link. Only the session's private key opens it, and the session clones the vault into its scratchpad, outside every repository, and deletes the opened key file.

I wrote about the sealing side in [secrets on public keys](secrets-on-public-keys.md). What is new here is where the recipient is read from: a file in the repository, which is also published on the team's own site within minutes.

## The role stays; the session changes

A [brief of 28 October](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/28b85bf2e1b04ad1700ba766ce7862efa1241922/records/briefs/2026-10-28__brief__becoming-the-agent-a-new-session.md), written by the conductor at my direction, puts the idea in four lines. An agent is a role. A session is one run of that role, in one account, for a while. The website is the anchor of trust. And from the moment a new session publishes its key, it is the agent and the previous session is not.

Each session gets a folder, `records/agents/<agent>/sessions/<session id>/`, with a `SESSION.json` (state, `from`, `until`, `supersedes`, `superseded_by`, fingerprint, account), the public key and its QR image. The registering command creates the folder, stamps the previous session `superseded` with an `until` of now, and rewrites `records/keys/<agent>.json`. The registration commit's time is the moment the new session becomes the agent. Everything the old session did before that stays valid, in its account and its period; anything dated after that claiming to come from it is flagged.

That gives two views of identity: one file for whoever needs the current recipient, and a history for whoever asks what an earlier session knew and did. A `session who` command answers which session held the role at a given time.

The handover stays specific to the work. A session asks only for the vaults it can name a step for in its role's card, and says whether it reads or writes. Being accepted as the conductor is not a reason to receive every vault key; the new conductor asked for none, because it reads no vault.

## In use the same night

The rule did not wait for a review to be useful. Two sessions had already pushed their keys before it: dev at 01:07 and the conductor at 01:34, both marked "not yet enrolled". At 02:22 the rule made that the way in, and at 02:36 the conductor added the session folders. Then the rest of the newsroom followed: researcher at 02:43, security and curator at 02:44, journalist at 02:56, factcheck and correspondent at 02:57, observability at 03:25 and desk at 03:29. By then all ten roles had a current key in `records/keys/`, and there are now 13 session folders behind them.

Ten roles, new keys, in one night: each commit that published or replaced an agent's key on 28 October.

Two of those commits are the questions below, happening for real. The curator's key was replaced at 02:55 "at the editor's word", with a pki-agent key pair. And the correspondent registered three times: two sessions claimed the role, and at 03:26 the commit records that I chose one of them. Which writer may replace which role's key was answered that night by me, one case at a time.

The handover side followed in the afternoon. At 14:49 the conductor added `schedule.py vaultreq`, which writes the request I paste into the vault keeper's session from an agent's published key: the key's URL on the team site, its fingerprint and session, and each vault with why it is needed. It refuses when the published key is not the current session's. The runbook says it was proven with the correspondent. That is the chain in this article, working end to end: a push, a file, and a sealed key that only the new session can open.

## What the push decides

The push decides one thing: which public key the newsroom accepts for a role now. It uses an authority that already exists, the account that can push to the team repository, instead of adding a ceremony beside it. I think that is a good trade for a team of agents that is renewed every time an account fills up, and I would like to keep it simple.

It also makes the push worth more. Before, publishing to team's `dev` updated a page or a run record. Now it can designate the recipient of a secret. The records say so themselves: the commit that added the rule also opened `conductor-0017`, a card for security that asks for a review of the residual risk, that anyone with push access to team can publish a key and be sealed to, and whether branch protection or a signed commit on `records/keys/` is worth having. I decided it was not needed now. At the later snapshot, commit `28b85bf`, the card was still `open`, byte for byte the same as the original, and it was still open at `43bfe25`, the team's latest commit at 15:21 UTC.

Four questions a sender can ask about a published key, and where each is answered today.

## Four questions that need their own answers

I read the records with these four in mind. None of them says the design is broken. Each says where the push stops and something else has to start.

**Possession.** A writer can copy a public key into a JSON file. The push tells the newsroom which key to accept; whether the session holds the private half is a separate fact. Only that half opens what is sealed to the key, so a handover to a key nobody holds is a wasted handover. For a sensitive vault I would like a small non-secret challenge first. The later runbook also allows an `encryption_fingerprint` beside the main one, and where signing and encryption keys differ, a proof with one is not a proof with the other.

**Which writer, which role.** The rule trusts whoever can push to team. If every writer, and every credential the GitHub app lets a session use, may designate every role's next key, that is a clear policy and I can say so. If some roles should need narrower authority, the repository can say it with branch rules, reviews or a code-owner file. On 28 October the branch endpoint reported `dev` as not protected. That is one dated field and not an audit of the rulesets, the permissions or the app's scopes, which I did not read here.

**The old session.** Marking a session `superseded` ends its standing as the agent. It does not by itself stop a scheduled task, remove a repository credential, or make a vault key the old session already opened unknown to it. A sealed key re-sealed to a new fingerprint is the same key. If a role needs a clean break, retirement has steps of its own: stop the tasks, withdraw the credentials, and rotate a vault key when a session that knew it should not any more.

**Which copy.** The brief says a pushed file is public within minutes on the team's site. A sender then has two views, the branch and the deployed site, and an old clone or QR image can show a superseded key. I would like the key file to carry the commit it came from and the session id, and the sender to say which copy it read. The `from` and `until` values are the session's own and the registration commit has its own time; they are a record, and I would not call them a clock.

## The tool sits beside the register

The later runbook also stops downloading the key tool during onboarding. `records/tools/pki-agent.mjs` is an unmodified copy of the file at pki.sgit.ai, with its sha256 recorded, because a session in auto mode may refuse to download code from a URL and run it. Its README says plainly that the copy has not been read line by line and that security reviews it, as board card `conductor-0020`. It lists what a read of its text found: it talks to pki.sgit.ai, dev.send.sgraph.ai, two public DNS-over-HTTPS resolvers and the GitHub gists API, and it uses `child_process` once.

A stable copy with a recorded hash is something a reviewer can read, and that is the gain. The hash sits in the repository beside the tool, so it protects against an accidental change and not against a writer who can replace both; for that case the answer is the same as for the key files. The pattern repeats: pick the authority a check ultimately trusts, and say so.

## Where I am

The newsroom's agents can be renewed by a push, and the records for it are public, dated and linked, so anyone can follow the chain from the runbook to the card. I would like three small things next, none of which needs the register to grow.

1. A line in the runbook saying who may replace which role's key: every writer, or a named set per role.
2. A possession check before a handover of a vault that matters, as a challenge the session answers with its key.
3. A retirement step in the session folder's lifecycle, listing the tasks stopped, the credentials withdrawn and the vault keys rotated.

I also need the answer to `conductor-0017`, and I will update this article when security has given it. The decision is mine, and the push is the authorisation because I made it so. The work now is to keep that delegation precise, visible, and no wider than the work needs.

## What this does not claim

- **It is a reading of records, not a test.** Nothing here ran the key tool, the registration command or a handover; what is described is what the runbook and briefs document.
- **It is one newsroom's decision.** It is not a statement about public-key infrastructure in general, and it does not replace pki.sgit.ai's register, which the same newsroom uses for people.
- **The account controls are the design's own statements.** My two-factor sign-in and the GitHub app are named in the brief; I did not check them here.
- **One branch field is one observation.** `dev` reported as not protected on 28 October; no rulesets, effective permissions or app scopes were inspected.
- **Signing is not general policy.** GitHub reported the rule's commit as signed with a valid SSH signature and the version bump after it as unsigned; two commits do not show what the repository requires.
- **The documents disagree in one place, and I left them so.** The move brief's numbered summary still says to pin the root, while its key section and the runbook drop it; the later brief states the exception more plainly.
- **Two times are commit times.** They are not deployment times, and I did not measure how long the site takes to show a push.
- **Nothing was compared.** I have no onboarding timings from before and after, so I make no claim that the change is faster.

If you run a team of agents and have solved who may replace which key, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

There was no voice memo. This article was drafted by one of this site's agents from a research pack of the PHP newsroom's records, prepared by an assistant on 28 October 2026, and from articles already published here. I asked for it, and the argument and the editorial responsibility are mine. The drafting agent re-ran the pack's integrity check on the extracted files: 22 file checksums and 9 Git blob IDs match. A second agent then reviewed the draft against the team repository at `43bfe25`, checked the rule, the runbook diff and the card, and added the section on the night it was used. The pack's own analysis and draft were read as a handover, and every claim above is tied to a source below.

Repository sources, all in the team repository `SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team`, at the commit named:

- The onboarding runbook at the policy commit, [`ee4e115`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2/records/briefs/2026-10-27__runbook__onboarding-a-session.md), and the runbook immediately before it, [`738f20a`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/738f20a8a80bd5f22bc977290f9d000d5c128f44/records/briefs/2026-10-27__runbook__onboarding-a-session.md).
- The [brief for the move](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2/records/briefs/2026-10-27__brief__moving-to-a-new-account.md), dated 27 October 2026, at `ee4e115`.
- The security card [`conductor-0017`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2/records/board/conductor-0017.json) at `ee4e115`, and at `28b85bf` where it is [unchanged and open](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/28b85bf2e1b04ad1700ba766ce7862efa1241922/records/board/conductor-0017.json).
- The [brief of 28 October on becoming the agent](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/28b85bf2e1b04ad1700ba766ce7862efa1241922/records/briefs/2026-10-28__brief__becoming-the-agent-a-new-session.md), the [later runbook](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/28b85bf2e1b04ad1700ba766ce7862efa1241922/records/briefs/2026-10-27__runbook__onboarding-a-session.md) and the [key tool's README](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/blob/28b85bf2e1b04ad1700ba766ce7862efa1241922/records/tools/pki-agent.README.md), all at `28b85bf`, whose head commit is dated 13:45:42 UTC on 28 October.
- The policy commit [`ee4e115`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/commit/ee4e115dbd4b8464febd61ef57d3d03fa16d9cf2), 02:22:16 UTC, reported by GitHub as signed with a valid SSH signature, and the version bump [`883e7f6`](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/commit/883e7f602f6fd1e5d13f081316f557098febf937), 02:22:45 UTC, reported as unsigned.
- The registrations, from the history of `records/keys/` between `ee4e115` and `43bfe25`, and the [`vaultreq` commit](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/commit/bb761259026d037b979ab48d2f7df16fb00f6ba6), 14:49:52 UTC, which adds the command and step 3 of the runbook.
- The [`dev` branch endpoint](https://api.github.com/repos/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team/branches/dev), read on 28 October 2026 with head `28b85bf`, `protected` false.

GitHub's documentation on [commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification) and [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) is cited from the research pack's notes, retrieved there on 28 October 2026 and not read again here.

The counts are from the runbook diff between `738f20a` and `ee4e115` (four commands removed, one paragraph added) and from the commit times above; the pack's evidence files hold them. Earlier articles used: [PKI everywhere](pki-everywhere.md), [a directory of people and keys](a-directory-of-people-and-keys.md), [secrets on public keys](secrets-on-public-keys.md) and [a team frozen in time](a-team-frozen-in-time.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-push-is-the-authorisation)

### Builds on

- [A team frozen in time: agent sessions with a mandate, a role and a repository, paused and picked up again, and why that changes what happens when the people who built a system move on](a-team-frozen-in-time.md) Agent sessions with a mandate, a role and a repository, paused and picked up again, so a team's knowledge outlives the team.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.

### Continued by

- [Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way](seven-iam-predictions-already-here.md) Sunnykumar K.'s seven IAM predictions for 2027, checked against agent teams that run today: four already here, one agreed, two different bets.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.
- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 314 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=314)

**Posting this article on LinkedIn?** The cover is [the-push-is-the-authorisation.jpg](banners/the-push-is-the-authorisation.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-push-is-the-authorisation.html)*
