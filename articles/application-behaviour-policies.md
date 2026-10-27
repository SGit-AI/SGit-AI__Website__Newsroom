# Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius, sgit.ai

> We write Agent Behaviour Policies to see what an agent can reach, what it was asked to do, and the gap between the two, because whoever takes the agent over inherits its reach and ignores its mandate. A remote code execution flaw does exactly that to an application. With php2shell, anyone on the internet who could only read a website's pages could, on an unpatched server, run commands as the website itself, with everything the website can reach. So the same method applies. An application behaviour policy writes down, for one application, what it can reach: its files, its database, its mail, its network, its secrets, the other systems that trust it; what it is for; the gap; the barrier in front of each row; and the blast radius of each row if the whole application were taken over, with whether there is a way back. Decision and workflow policies say who accepts that blast radius and in what order things happen. This matters today for a practical reason. Organisations took websites offline as a precaution, and the question in front of them now is not only whether they have patched. It is: if this site were taken over anyway, what would we lose? With the map, the decision to bring a site back is a decision about known rows, with the cheap ones cut first and the signals to watch named. The worked example is invented; the method, the PHP evidence and our own sites are not. Updated with the story site's compromise map: as of 20:50 UTC, millions of attempts, three vendors reporting exploitation without naming a victim, and no named organisation saying php2shell was the way in. That silence lowers the likelihood; it does not change the blast radius.

*Source: <https://newsroom.sgit.ai/articles/application-behaviour-policies.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius

# Application behaviour policies: what a website can reach, what it is for, and what it would cost if it were fully taken over, so the sites switched off for php2shell can come back with a known blast radius

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-22 · [article v1.2.0, 3 versions](versions/application-behaviour-policies.md) · [newsroom v0.13.45](https://newsroom.sgit.ai/admin/versions.html) · abpphp2shellapplicationsblast-radiusappsecarticle

***Abstract:** We write Agent Behaviour Policies to see what an agent can reach, what it was asked to do, and the gap between the two, because whoever takes the agent over inherits its reach and ignores its mandate. A remote code execution flaw does exactly that to an application. With php2shell, anyone on the internet who could only read a website's pages could, on an unpatched server, run commands as the website itself, with everything the website can reach. So the same method applies. An application behaviour policy writes down, for one application, what it can reach: its files, its database, its mail, its network, its secrets, the other systems that trust it; what it is for; the gap; the barrier in front of each row; and the blast radius of each row if the whole application were taken over, with whether there is a way back. Decision and workflow policies say who accepts that blast radius and in what order things happen. This matters today for a practical reason. Organisations took websites offline as a precaution, and the question in front of them now is not only whether they have patched. It is: if this site were taken over anyway, what would we lose? With the map, the decision to bring a site back is a decision about known rows, with the cheap ones cut first and the signals to watch named. The worked example is invented; the method, the PHP evidence and our own sites are not. Updated with the story site's compromise map: as of 20:50 UTC, millions of attempts, three vendors reporting exploitation without naming a victim, and no named organisation saying php2shell was the way in. That silence lowers the likelihood; it does not change the blast radius.*

What a remote code execution flaw does to the grant: a visitor requests pages before, and runs commands after.

**Updated at 21:30 UTC.** With the story site's new [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html): what it searched, what it found, three readings of the silence, and whether this is where everyone should be looking. The report that the fix might be incomplete has also been answered.

## In short

- **An exploit hands over the application's reach.** And ignores what it was for.
- **So map the application like an agent.** Reach, mandate, gap, barrier, blast radius.
- **Blast radius is defined over the reach.** Plus one more axis: is there a way back?
- **Decision and workflow policies complete it.** Who accepts the risk, and in what order.
- **This is the bring-back question.** Not only "have we patched?", but "what if it is taken over anyway?"
- **Cut the cheap rows first.** Egress, credentials, mail, metadata, admin.
- **Name the signals before you switch it on.** The footprint tells you when a row is being used.
- **Millions of attempts, no named compromise.** A finding in itself, as of 20:50 UTC on 22 October.
- **The silence lowers the likelihood, not the blast radius.** And it may be partly silence.

## The question in front of the offline sites

On 22 October, organisations took websites offline as a precaution against [php2shell](https://newsroom.sgit.ai/articles/php-october-at-8pm.html), the two critical flaws in PHP: the Dutch national cyber security centre's own site, UK councils, a set of game wikis whose servers were off for 13 hours, and others in [the impact ledger](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) of the story's own site. Several government agencies advised exactly that for anyone who could not patch.

Now they want them back. The obvious question is "have we installed the fix?", and it is necessary. It is not sufficient. The report that the fix might be incomplete was answered by PHP's security team on the morning of 22 October as an unrelated crash bug, but there will be another flaw after this one; and some sites run on versions of PHP that have no ready-made fix. The question that actually lets someone sign off a restore is a different one: if this website were completely taken over anyway, today, what would we lose, and could we get it back?

Almost nobody can answer that quickly, because almost nobody has written down what their website can reach. That is the same problem we found with agents.

## What the compromise map shows

From attempts to a named compromise, as of 20:50 UTC on 22 October, with the sources the PHP site watches behind it.

There is also a second half to the bring-back decision: how likely is the takeover? This evening the story's site published a page that answers that as well as anyone can today: [the compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html). It takes one statement, "No named organisation has said it was compromised through php2shell", as of 20:50 UTC on 22 October, and lays out the evidence behind it, row by row: 33 statements, each with who said it, when, in their words, and where the capture is.

What it searched is the part I want people to notice. The evidence vault's 184 sources. A source watch of 773 pages from 474 publishers in 57 countries and 34 languages, checked hourly, with 339 pages read in their own language. 3,444 news items scanned from 1,621 publishers. And 295 sites somebody had named as taken offline, probed every 30 minutes.

And what it found, in layers:

- **Attempts: millions.** Cloudflare's chief executive, Amazon, watchTowr, CERT.LV and others report attempts against sensors, honeypots and their edges.
- **Exploitation reported, no victim named: three vendors.** Hadrian, Patchstack and Amazon say exploitation is happening. None names a victim.
- **Named organisations saying they were attacked: one.** The Czech Technical University said it faced an attack that was "part of worldwide attempts to hit PHP sites", and that "the active attack was stopped". Whether it succeeded is not stated.
- **Named organisations saying php2shell was the way in: none.** One Japanese company reported a break-in without stating a cause; another first blamed the PHP flaw, then corrected itself: the attackers had used a flaw in its own service.
- **No success known.** CISA, the PHP Foundation, Huntress and the governments or national agencies of Germany, the Netherlands, Japan, Switzerland, Belgium and Austria say they know of no successful attack, each within what it can see.
- **The official signals.** At 18:16 UTC, CISA's catalogue of known exploited vulnerabilities did not list either flaw. CISA's own assessment on the CVE records says exploitation: none; automatable: no; technical impact: total. And FIRST's exploit prediction score puts the modelled probability of exploitation activity in the next 30 days at 0.053 and 0.058.

The page is careful, and so should we be: this is "a time-bounded absence, not a confirmed fact". One statement from one organisation would end it, and the page lists what would: a named organisation's own notice, a cause stated by the companies that reported incidents, a listing in the catalogue, a regulator's breach notice, a vendor naming a victim with consent.

## Three readings of the silence

Even so, I think it is an important finding. About 31 hours after the flaws were disclosed, with exploit attempts in the millions and, by one scanner's count on the day of the release, more than a million and a half hosts still unpatched, you would expect to see compromises. We do not. There are three readings, and they are not exclusive:

1. **The flaws are harder to use than they look.** The CVE records rate the attack complexity high, and the site's fact-check desk records the researchers' view that triggering the bug is much easier than turning it into code execution. Add the edge protections that went up within hours. If that is the explanation, the likelihood is lower than the 9.2 suggests, and so is the risk.
2. **Compromises are happening and not being disclosed.** Most organisations have no obligation to say quickly, and in public, that they were broken into; where a rule exists, it usually runs to a regulator first and in days, not hours. This is the same pressure I keep writing about with software companies, from [the SaaS apocalypse](https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) onwards: they have every reason to stay quiet if they can. It is also why I keep coming back to aviation, which, as I argued in [a policy beside the prompt](https://newsroom.sgit.ai/articles/a-policy-beside-the-prompt.html), got safe because crashes became news. In software, most crashes still do not.
3. **The attackers are quiet too.** That is the strange part. Mass exploitation is often noisy: defacements, ransom notes, botnets, sales of access. Quiet is what a careful attacker with a valuable target would choose, but it is not what we normally see.

For the application behaviour policy, the conclusion does not depend on which reading is right. The silence lowers the likelihood; it does nothing to the blast radius. A site owner who reads the compromise map can reasonably decide that the probability of a takeover today is lower than the headlines suggested, and still has to know what a takeover would cost. And because public silence is not evidence that nothing happened to you, your own footprint is the only evidence that is about your site.

## Is this where everyone should be looking?

There is a wider question too. php2shell has had governments telling organisations to switch websites off, and live pages in the national press. In the same weeks, as I noted in [the attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html), CISA's catalogue was filling with flaws in VPN gateways, mail gateways and firewalls that were exploited, some as zero-days. If php2shell, with millions of attempts, has no named victim yet, while quieter flaws in edge devices are in the catalogue because they were used, then attention and actual exploitation may be pointing at different places. I am asking another researcher to collect the flaws of the last week and what is known about their exploitation, so we can answer that with data rather than impression.

## The same method, a different subject

In [footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html) we set out the words of an Agent Behaviour Policy. Reach is what the agent can do, measured. Mandate is what you asked it to do. The gap is the difference. The barrier in front of each row of the gap is typed honestly: a boundary, a setting, an expectation, or nothing. Footprint is what it actually did, read afterwards. And blast radius is what it would cost if a row were used in full, "defined over the reach, because whoever takes the agent over inherits its reach and ignores its mandate", with a second axis: whether there is a way back.

Every one of those words fits an application:

- **Reach** is what the application's process can do on the server: the files it can read and write, the database user it connects as, the mail it can send, the network it can open connections to, the secrets in its configuration, the cloud credentials on its machine, and the other systems that trust requests from it.
- **Mandate** is what the website is for: serve these pages, accept this form, send this confirmation email, let these editors publish.
- **The gap** is everything it can reach and does not need to. A website that serves pages and takes one form rarely needs to write its own code files, open connections to the internet, read the whole database, or send mail to anyone.
- **The barrier** is what stops each row of the gap, typed the same way. A firewall rule outside the server is a boundary. A configuration setting the application's own user can change is a setting. A rule in a wiki is an expectation.
- **Footprint** is the application's actual behaviour, read from its logs: what it connected to, what it wrote, what it sent.
- **Blast radius** is what each row would cost if an attacker used it in full, and whether there is a way back.

A remote code execution flaw shows it directly. Before it, an anonymous visitor's grant is tiny: request a page, submit a form. On an unpatched server, the same visitor runs commands as the application. Their grant becomes the application's reach. In [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html) I made the same point about code: every piece of it has its own grant, and it is "usually far larger than the policy above it". An exploit is the moment somebody else starts using the difference.

## Three policies, not one

Three policies for an application: behaviour, decision and workflow, with the gap and blast radius per row.

For agents we use three kinds of policy, and an application needs all three:

- **The behaviour policy** is the map: reach, mandate, gap, barriers and blast radius, row by row.
- **The decision policy** says who decides what. Who may accept the blast radius of each row that stays open; who decides the site comes back; which actions inside the application need a person, such as creating an administrator or changing where payments go. [Approved business mandates](https://newsroom.sgit.ai/articles/approved-business-mandates.html) made the point that companies already have these rules for people; the application has to follow them too.
- **The workflow policy** says in what order things happen. For the bring-back: patch, map, cut, set the signals, decide, restore, watch. Inside the application: a form submission is stored, then a confirmation is sent, never the other way round, and nothing in that flow ever needs to write a code file.

## A worked example

An application behaviour policy for an invented council website on PHP: ten rows of reach, with the barrier and the cut.

To make it concrete, here is an invented example: a council website running a PHP content management system on a virtual machine in a cloud. It serves pages, has a contact form and a search box, and a few editors publish news. Nothing here describes any real council. The rows are typical of how such sites are often set up, which is exactly why they are worth mapping:

1. **Serve pages; accept the contact form.** The mandate. If taken over: defacement and false notices. Way back: yes, redeploy.
2. **Write its own code files.** Not in the mandate; most sites only need to write uploads. If taken over: a persistent backdoor that survives the patch. Way back: only by rebuilding from a known-good source. Cut: make the code read-only to the web server's user.
3. **Read and write the whole database.** The configuration file holds a database user that can do everything. If taken over: every resident's form submission, every editor's password hash. Way back: none for data already read. Cut: a database user limited to what the site does, and old submissions moved out.
4. **Send mail as the council.** If taken over: phishing from a trusted domain. Way back: partial, after reputational damage. Cut: send through a relay that allows only the confirmation template, to the address on the form, at a set rate.
5. **Open connections to the internet.** If taken over: downloading tools, sending data out, joining a botnet. Cut: deny outbound traffic at the network, except to named services. This is the single cheapest row to cut, and the most useful.
6. **Reach the internal network.** If the server can see other council systems, a takeover is a foothold. Cut: put it in its own segment.
7. **Read the cloud's instance credentials.** On many clouds a process on a virtual machine can ask for the machine's credentials. If those can read storage or start machines, the blast radius is the cloud account. Cut: block or require tokens for the metadata service, and give the machine a role that can do almost nothing.
8. **Hold administrator sessions.** Editors log in on the same site. If taken over: their sessions and passwords. Cut: a separate administration host, or an administration path reachable only from the council's network.
9. **See the backups.** If backups are mounted on the server, an attacker can read or delete them. Way back depends on this row. Cut: backups pushed out, never readable back.
10. **Hold third-party keys.** A payment or mapping key in the configuration. If taken over: whatever that key allows. Cut: keys with the narrowest scope, or calls made from somewhere else.

Read the table and the decision changes shape. Before the cuts, a takeover of this site is a data breach, a phishing campaign and possibly the cloud account. After rows 2, 4, 5, 7 and 9 are cut, which are configuration changes rather than projects, the worst case is defacement and the data in the database, with a way back from everything except what was read. That is a blast radius a council's risk owner can accept or refuse knowingly, and the decision policy names who.

## Our own sites, as a measured contrast

This newsroom and the PHP story's site are static pages served by GitHub Pages. Their application behaviour policy at run time is short: no PHP, no database, no server process of ours, no mail, no secrets on a server. If the pages were taken over, the worst case is false content, with a way back by redeploying a known commit. That is what [the attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html) argued from the other side.

But the blast radius did not disappear; it moved to the pipeline. Whoever controls what is deployed controls the site. That is why the policy for this repository, in [the rules of the game](https://newsroom.sgit.ai/articles/the-rules-of-the-game.html), puts the workflow and the validator in their own zone, and why [the sidecar repository](https://newsroom.sgit.ai/articles/the-sidecar-repository.html) moves deployment out of the agents' reach. The same method found the row that matters for us.

## Bringing a site back

Bringing a site back, in order: patch, map the reach, cut rows, name the signals, decide, restore, read the footprint.

So the workflow for a site switched off for php2shell, written as a policy:

1. **Patch.** To PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or a supplier's fixed build. On an older branch with no fix, the rest of this list matters more, not less.
2. **Map the reach.** One row per thing the application can do, from the server itself: its user, its files, its database grants, its mail, its network routes, its credentials.
3. **Write the mandate.** What the site is for, in a few lines, from the people who own it.
4. **Cut the cheap rows.** Outbound traffic, write access to code, mail, cloud credentials, mounted backups. Each is a configuration change with a large effect on the blast radius.
5. **Name the signals.** For each row left open, the trace it would leave if used. For php2shell, the story's site already collects [detection signals](https://php.oct.2026.newsroom.sgit.ai/defence/index.html) with their sources: a PHP worker starting a shell, memory errors outside any script, crashes in clusters, uploads to pages that take none. Add the rows' own: new outbound connections, new files in the code directories, new administrator accounts, mail volume.
6. **Decide.** The owner named in the decision policy accepts the blast radius of what remains, or does not, with the likelihood as the evidence stands: for php2shell, the compromise map.
7. **Restore, and read the footprint.** In the first hours, then weekly. A row the footprint never uses is a candidate to cut; a row used outside the mandate is a near miss.

## What is new, and what is not

None of the pieces is new. Least privilege, network segmentation, threat modelling and business impact analysis are long-standing practice, and many organisations do parts of this already. What I think is new is writing them as one policy per application, in the same five words we use for agents, with the barrier typed honestly and the blast radius per row, so that the same people, tools and reviews work for both. An agent and an application are both code acting with a grant. The day an exploit is published, the difference between them stops mattering.

## What this does not claim

- **The council example is invented.** Typical rows, not a real site; no real council is described.
- **The cuts reduce the blast radius; they do not remove the flaw.** Patch first.
- **The signals are evidence, not a guarantee.** A careful attacker leaves fewer traces.
- **We have not mapped any third party's site.** Our own are the only measured example.
- **The PHP facts are as the story's site records them.** The compromise map is as of 20:50 UTC on 22 October, at site v0.5.9.
- **The three readings are mine.** The compromise map makes no assessment of risk, and says so.

## Where this comes from

My voice memo of 22 October 2026; the method in [footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html) and [the code you do not ship](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html); the impact ledger, detection signals, fact-check and [compromise map](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html) of [php.oct.2026.newsroom.sgit.ai](https://php.oct.2026.newsroom.sgit.ai/) at v0.5.9, read from its repository at 21:06 UTC; and this site's own deployment. Related: [PHP October 2026, at 8pm](https://newsroom.sgit.ai/articles/php-october-at-8pm.html), [approved business mandates](https://newsroom.sgit.ai/articles/approved-business-mandates.html), [the rules of the game](https://newsroom.sgit.ai/articles/the-rules-of-the-game.html), [the attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#application-behaviour-policies)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 262 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=262)

**Posting this article on LinkedIn?** The cover is [application-behaviour-policies.jpg](banners/application-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/application-behaviour-policies.html)*
