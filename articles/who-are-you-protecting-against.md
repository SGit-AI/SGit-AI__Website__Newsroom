# Who are you protecting against? Draw the security line where the attacker is, not above it, sgit.ai

> An entrepreneur doing everything they can to be secure bought a Mac mini for a customer, decided it would never touch the internet and that nothing would be installed on it, and ended up writing the application in the Perl that ships with macOS. The question that decides whether that is wise is not how secure the design is, but who it protects against. This article sets out the three questions that answer it, who the threat agent is, what the attack vector is, and how sophisticated they are, and a ladder of six tiers from your own mistakes to states, grounded in NIST SP 800-30, the NCSC's commodity, targeted and elevated threats, and MITRE ATT&CK. It notes that the UK's new AI Risk Management Toolkit asks "Who are the new threat actors?" without defining them. It reads the Mac mini against the ladder, where the air gap stops attackers that no inbound ports and patches also stop while adding a USB path and removing backups, monitoring and mainstream tooling; makes the same argument about keeping systems on premises for security; and argues that you should sell something better than what the customer has, not something beyond what they need, because drawing the line too high is a disservice to both sides. With it ships a vault of eight fictional startups, each with its assets, an attack tree mapped to ATT&CK techniques, and where it should draw the line, plus a questionnaire to draw your own.

*Source: <https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html> · sgit.ai v0.7.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who are you protecting against? Draw the security line where the attacker is, not above it

# Who are you protecting against? Draw the security line where the attacker is, not above it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-08 · [article v1.1.0, 2 versions](versions/who-are-you-protecting-against.md) · [sgit.ai v0.7.3](https://sgit.ai/admin/versions.md) · securitythreat-modellingthreat-agentsattack-treesmitre-attacknistncscstartupsfoundersair-gapcloudvaultsarticle

***Abstract:** An entrepreneur doing everything they can to be secure bought a Mac mini for a customer, decided it would never touch the internet and that nothing would be installed on it, and ended up writing the application in the Perl that ships with macOS. The question that decides whether that is wise is not how secure the design is, but who it protects against. This article sets out the three questions that answer it, who the threat agent is, what the attack vector is, and how sophisticated they are, and a ladder of six tiers from your own mistakes to states, grounded in NIST SP 800-30, the NCSC's commodity, targeted and elevated threats, and MITRE ATT&CK. It notes that the UK's new AI Risk Management Toolkit asks "Who are the new threat actors?" without defining them. It reads the Mac mini against the ladder, where the air gap stops attackers that no inbound ports and patches also stop while adding a USB path and removing backups, monitoring and mainstream tooling; makes the same argument about keeping systems on premises for security; and argues that you should sell something better than what the customer has, not something beyond what they need, because drawing the line too high is a disservice to both sides. With it ships a vault of eight fictional startups, each with its assets, an attack tree mapped to ATT&CK techniques, and where it should draw the line, plus a questionnaire to draw your own.*

Six tiers of attacker, from your own mistakes to elevated threats, with what stops each. Most startups plan for everything up to organised crime for money, and write down what they accept above it.

**Where this comes from.** A voice memo I recorded after reading a report from an entrepreneur who is trying hard to do security properly and is learning fast. They are not named and their project is not described beyond the design choice the memo is about. The ladder, the scenarios and the questionnaire are in a vault published with this article, [Threat-sized security](https://sgit.ai/demos/vaults/threat-sized-security/index.md); the scenarios in it are fictional and the sources are real.

## In short

- **The question is who, not how much.** Before deciding how secure a design must be, answer three questions: who is the threat agent, what is the attack vector, and how sophisticated are they.
- **Attackers come in tiers.** Your own mistakes, opportunistic automation, activists, organised crime for money, targeted commercial attackers and insiders, and elevated threats from high-end crime and states. NIST SP 800-30, the NCSC and MITRE ATT&CK give the vocabulary.
- **The basics beat most of the ladder.** In the NCSC's words, "Organisations that defend effectively against commodity threats present a very hard target for all attackers". At the top tier, very few commercial organisations can hold out, whatever they build.
- **The air-gapped Mac mini protects against an attacker who has easier ways in**, while it adds a USB path and removes backups, monitoring, patches and mainstream tooling. Isolate it; do not disconnect it.
- **Sell better than what the customer has, not beyond what they need.** Drawing the line too high slows everything down, can create new holes, and can stop the technology being used at all. That is a disservice to both sides.

## A Mac mini that will never touch the internet

The design is easy to admire. A founder building an AI assistant for a customer buys a dedicated Mac mini. To keep the customer's files safe, it will never be connected to the internet. To avoid a supply chain, nothing will be installed on it. So the application is written in the one language that is already there: the Perl that ships with macOS. Files go in and out on a USB stick.

The side effect is the problem. Perl, as shipped with macOS, is there, in Apple's own words, "for compatibility with legacy software"; Apple said in 2019 that future versions might not include it and that software depending on a scripting language should bundle its own runtime. I would go further: it is probably one of the worst choices you could make today for an application like this. Not only because of the language, but because of everything around it. Compared with Python or Node, there are far fewer maintained libraries for the things an AI assistant needs, PDFs, spreadsheets, model APIs, HTTP, and far less of the tooling that makes code good: tests, linters, dependency scanners, the pipelines that check every change. The design buys a great deal of engineering and technical debt.

What does it buy with it? That depends entirely on who it is protecting against.

## Three questions before any control

Security starts with three questions, and most over-engineering comes from skipping them:

1. **Who is the threat agent?** A bot, a criminal crew, a competitor, an insider, a state.
2. **What is the attack vector?** How they would actually get to the thing you care about.
3. **How sophisticated are they?** What they can afford to spend, and how patient they are.

The UK government's new [AI Risk Management Toolkit](https://www.gov.uk/government/publications/ai-risk-management-toolkit/ai-risk-management-toolkit-guidance), which we [mapped](https://sgit.ai/demos/vaults/dsit-ai-risk-toolkit/index.md) when it was published, asks the right question in its section on security: "Who are the new threat actors?" It does not define them. It points to the risk management section of the government's Cyber Assessment toolkit instead. So the definitions in this article come from three older and well-tested places: NIST SP 800-30, the guide most risk assessments are built on, whose taxonomy of threat sources separates adversarial, accidental, structural and environmental sources and rates an adversary's capability on five levels from very low to very high; the NCSC, which separates un-targeted from targeted attacks, commodity from bespoke capability, and commodity from elevated threats; and MITRE ATT&CK, which names the techniques.

## The ladder

There is a well-known sequence, and the vault turns it into six tiers. Each has a NIST type and capability, a motive, a way of choosing targets, the ATT&CK techniques it typically uses, and the controls that stop it.

- **T0, your own mistakes.** A secret committed to a repository, a bucket left public, a table deleted with no backup. NIST calls these accidental sources. They are the most common loss, and nothing about them is sophisticated.
- **T1, opportunistic automation.** The script kiddies of the old vocabulary, now mostly bots: scanners, credential stuffing, mass phishing. The NCSC describes un-targeted attackers as those who "indiscriminately target as many devices, services or users as possible", and says "every organisation connected to the Internet should assume they will be a victim" of them. Patching, MFA and nothing listening that does not need to beat them.
- **T2, ideology and attention.** Hacktivists and protest groups, who pick targets by cause. Most startups are not on their list.
- **T3, organised crime for money.** Ransomware, extortion and access brokers, run as businesses, choosing victims by ability to pay and by how much the data hurts. Commodity tools, used industrially. This is the realistic ceiling for most startups that hold anything of value.
- **T4, targeted commercial.** Competitors, the other side in a dispute and the hack-for-hire services they pay, and insiders. In a targeted attack, says the NCSC, "your organisation is singled out because the attacker has a specific interest in your business, or has been paid to target you".
- **T5, elevated threats.** The NCSC: these "can only be realised by large, well-funded groups (such as high-end organised crime and state sponsored groups)". Zero-days, supply chains, hardware, people, and years of patience.

At the top of the ladder the honest answer is uncomfortable. Very few commercial organisations can withstand a determined state attacker, and almost none at the level of investment a startup's technology team can make. That is not a reason to give up; it is a reason to stop designing as if you were the target, unless you are. If you sell into an environment where that tier is real, a government department, defence, critical infrastructure, the customer already owns the controls for it, and your job is to run well inside their accredited environment, not to build a parallel fortress.

At the bottom, the NCSC's point is the encouraging one: "Regardless of their technical capability and motivation, attackers will often turn to commodity tools and techniques first. Organisations that defend effectively against commodity threats present a very hard target for all attackers." The basics, done consistently, are most of the job.

## The Mac mini, read against the ladder

The vault's comparison: the air-gapped, nothing-installed design against an isolated-not-disconnected one, tier by tier. The air gap stops the bots, which no inbound ports and patches also stop; adds a USB path; and gives up backups, monitoring and tooling that would catch the most likely losses.

The report did not say who the customer was, so in the vault I gave the case a fictional one, a twelve-person accounting firm, and walked it up the ladder. The air gap looks different from each tier.

Against **your own mistakes**, it is worse. The most likely loss for a small firm is an accident: a file overwritten, a machine that fails, a script nobody else can fix. A design with no automated backups, no monitoring and code few people can maintain makes those more likely and harder to undo.

Against **opportunistic automation**, it works, but so does the ordinary alternative. Bots need an inbound service or an unpatched one. A machine with no inbound ports, an outbound allowlist and automatic updates stops them as well as a cable that is never plugged in.

Against **organised crime**, it mostly misses. Ransomware gets into a small accounting firm through a member of staff's email and laptop, not through a dedicated machine in a cupboard. If the laptops are not protected, the air gap does not help; if anything, the USB stick that carries files between the laptops and the Mac mini is now the path, and removable media is how air gaps have been crossed before (ATT&CK T1091).

Against **elevated threats**, it does not hold. If an attacker at that tier is really after this firm, they will use hardware, people or that USB stick. In the words of my memo, if the attacker is trying to hit you, you have much bigger problems than that, and the air gap is not really going to save you. Running something properly air-gapped is a very hard discipline, and the mistakes made along the way create their own vulnerabilities.

So the air gap protects against an attacker who, for a firm like this, does not really exist, and pays for it with the tools that defend against the attackers who do. The better design is isolated, not disconnected: no inbound ports; outbound only to an allowlist of updates, backups and the model provider; software from a package manager, pinned, scanned and run in containers; disk encryption, automatic updates, and logs shipped somewhere someone reads them. Docker or Compose inside the machine, or inside a VM on it, is enough to start; Kubernetes later if it is needed. The point of using best-in-breed technology is visibility: it lets you ship good security tools and good security practices with the application, instead of writing them by hand in a language that has few of them.

## The same mistake, one size up: local versus cloud

This is the debate between running things locally and going to the cloud, at a smaller scale. "We will not go to the cloud, because the cloud is insecure", and then the organisation runs local infrastructure with more holes than Swiss cheese, because it does not have the expertise to run it securely and cannot hire it. In my experience the result is often more vulnerabilities inside the company, not fewer. A small team cannot compete, on quality or on security, with the people who run the major platforms full time. Decentralised does not mean safer; it usually means fewer people watching each part.

## Sell better than what they have, not beyond what they need

One primitive matters more than any control: what is the customer's baseline today? An accounting firm runs Windows laptops, a shared drive and email. A club runs spreadsheets and a noticeboard. A therapist keeps notes on a home laptop. A solution that is clearly better than that, and that does the basics well, is already an improvement in security for the customer.

There is no point spending time and money building something far beyond the customer's security requirements. And I say that as a security person: I am not arguing against security. I am arguing that you have to know where to draw the line. Draw it too high and you do a disservice to both sides. You protect against an attacker who is not there; you slow everything down; you may create new problems, as the USB stick does; and you may stop the technology being used at all, which leaves the customer with the weaker setup they had before. Most teams building at startup level, especially with vibe-coded applications, are not ready to deploy into the most sensitive accounts and environments without the customer's own controls around them, and should not be asked to pretend otherwise. When that is the market, meet the customer's baseline and deploy inside it.

## Eight startups, eight lines

The vault's compare view: eight fictional startups against the six tiers, the tiers in scope filled and each ceiling marked.

The vault maps this out for eight fictional startups, because the line moves with the business, not with how careful the founder is.

| Fictional startup | Ceiling | Why |
|---|---|---|
| A booking app for padel clubs | T1 | Member contact details; nothing that pays a ransom |
| AI bookkeeping reading bank feeds | T3 | Financial data and live tokens: ransomware and extortion |
| Session notes for independent therapists | T3, with T4 for insiders | The harm is to patients; the 2020 Vastaamo case shows how |
| The Mac mini at an accounting firm | T3 | Ransomware starts at the staff laptops |
| Document review for law firms in disputes | T4 | Hack-for-hire against litigants is documented |
| Energy monitoring with optional control | T3 | Keep the dangerous capability off by default |
| A popular open-source library | T5 | The target is everyone downstream; the xz Utils backdoor is the precedent |
| AI drafting for a government department | T5 | Set by the customer, who already owns the controls |

One scenario in full: the accounting firm assistant's assets, its attack tree with an ATT&CK technique on every branch, and the line, with what must be done, what should, what is over the line and why, and the under-engineering to avoid.

Each scenario has an [attack tree](https://www.schneier.com/academic/archives/1999/12/attack_trees.html), the form Bruce Schneier described in 1999, "with the goal as the root node and different ways of achieving that goal as leaf nodes". Every branch carries the ATT&CK technique it uses, the tier of attacker who would use it, and a rough cost. Walk the tree and the line draws itself: the branches below the ceiling get controls; the branches above it are written down as accepted, with a reason. Two startups have a ceiling at the top tier, and the reasons are instructive. One is a two-person open-source project, because one malicious release reaches everyone who installs it. The other sells to government, where the customer sets the line and already owns the controls.

## Draw your own line

The questionnaire: five questions about what you hold, who would pay to attack you, who you sell to, how far one breach reaches and what your customers use today, and the ceiling they point to, with the controls for every tier up to it.

The vault ends with five questions: what is the most valuable thing an attacker could take or break; who would pay, or spend months, to attack you specifically; what environment you sell into; how many organisations one breach of you reaches; and what your customers use today. The highest tier any answer points to is your ceiling. Below it, the controls are listed. Above it is a risk you accept and write down, which is a decision, not a failure; [every risk is already accepted](every-risk-is-already-accepted.md), and the only question is by whom.

Then do the part most people skip: write the threat model down, on one page, publish it, and ask the community whether you are making the right compromises. Somebody who has seen the attack before will tell you quickly whether your line is too low, or too high.

## Where to start

- **Name your attackers.** Use the ladder. If you cannot name anyone above T1 who would pay to attack you specifically, that is your answer for now.
- **Draw one attack tree** for the thing you would least like to lose, with a technique on every branch.
- **Do the basics consistently.** Patching, MFA, backups restored in a drill, secrets out of code, nothing listening that does not need to.
- **Look at your customer's baseline**, and make sure you are clearly better than it.
- **Write down what you accept** above your ceiling, and when you will look again.
- **Prefer isolation and visibility over disconnection.** Mainstream tools, containers, logs someone reads.
- **Publish the threat model and ask.**

*Drafted from a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 8 October 2026. The entrepreneur whose design prompted it is not named. Quotations are from the NCSC's Common Cyber Attacks: Reducing the Impact and Design guidelines for high assurance products, NIST SP 800-30 Rev. 1, Apple's macOS Catalina 10.15 release notes, DSIT's AI Risk Management Toolkit guidance and Bruce Schneier's Attack Trees, each read on 8 October 2026 and listed with links in the vault's sources. ATT&CK is a registered trademark of The MITRE Corporation. The eight startups in the vault are fictional; the precedents they cite are real.*

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#who-are-you-protecting-against)

### Builds on

- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.

### Continued by

- [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](who-will-game-the-reading-meter.md) Eight kinds of reader, none of them attackers, nine ways to cheat a browser meter, and the quieter risks that will actually happen.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [How agents decide, and when they stop](collections/how-agents-decide.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [who-are-you-protecting-against.jpg](banners/who-are-you-protecting-against.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html)*
