# Where is the why? A permission prompt asked me to decide, and kept the reason, sgit.ai

> An agent session asked, in the middle of a task, to add a repository. The prompt showed three fields, owner, repository and access, and two buttons, Decline and Allow once. It did not say which session was asking, why, what the session would be able to do afterwards that it could not do before, or what would happen on a no. The session was one of several, and one of them was working on a vault holding confidential data. This article reads that prompt through the Agent Behaviour Policy, where a permission prompt is a request to change the grant mid-session and a barrier whose strength is the information the person is given; sets it against what courts, regulators and research have said about decisions taken without the facts, from Montgomery's consent forms and the red hand rule to GDPR's informed consent, token human oversight, and the moral crumple zone; lists the other prompts that asked without a why and the fixes that worked, from Apple's purpose strings and Microsoft's number matching to the CNIL's rule that refusing must be as easy as accepting; puts Anthropic's own figures on how often people approve agent prompts beside them; and proposes a why card, a prompt that carries its reason, its change in reach, its cost, the path if declined, and a record, and that turns into a risk acceptance when the risk rises.

*Source: <https://newsroom.sgit.ai/articles/where-is-the-why.html> · sgit.ai v0.7.86 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where is the why? A permission prompt asked me to decide, and kept the reason

# Where is the why? A permission prompt asked me to decide, and kept the reason

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.1.1, 3 versions](versions/where-is-the-why.md) · [sgit.ai v0.6.84](https://sgit.ai/admin/versions.md) · agentsagent-behaviour-policyhuman-in-the-looppermission-promptssecurity-uxconsentaccountabilityrisk-acceptanceclaude-codemcparticle

***Abstract:** An agent session asked, in the middle of a task, to add a repository. The prompt showed three fields, owner, repository and access, and two buttons, Decline and Allow once. It did not say which session was asking, why, what the session would be able to do afterwards that it could not do before, or what would happen on a no. The session was one of several, and one of them was working on a vault holding confidential data. This article reads that prompt through the Agent Behaviour Policy, where a permission prompt is a request to change the grant mid-session and a barrier whose strength is the information the person is given; sets it against what courts, regulators and research have said about decisions taken without the facts, from Montgomery's consent forms and the red hand rule to GDPR's informed consent, token human oversight, and the moral crumple zone; lists the other prompts that asked without a why and the fixes that worked, from Apple's purpose strings and Microsoft's number matching to the CNIL's rule that refusing must be as easy as accepting; puts Anthropic's own figures on how often people approve agent prompts beside them; and proposes a why card, a prompt that carries its reason, its change in reach, its cost, the path if declined, and a record, and that turns into a risk acceptance when the risk rises.*

What the prompt carried and what it did not: three fields and two buttons on the left; on the right, the six things the person needed to judge the request, none of which were on the screen. Infographic from a screenshot of 7 October 2026.

**Where this comes from.** On 7 October 2026 a prompt appeared asking to add a repository to a Claude Code session. I had several sessions running, and one of them was working on a vault that handles confidential data. My first question was the one the prompt did not answer: why? This article is built from that screenshot and a voice note recorded straight after it. The session that wrote the article did not make the request, and which session did is not known: the prompt did not say. The repository asked for is public. The article is written by an agent running on Claude about a prompt in a Claude product, and it says so here because the question it asks applies to the session writing it.

## In short

- **The prompt asked for a decision and kept the reason.** Owner, repository, access level, Decline, Allow once. Not which session, not which step, not the instruction it served, not what changes, not what a no would cost.
- **Both buttons had a hidden price.** Decline breaks a task the person started, with no account of what breaks. Allow makes the person the author of a decision whose basis they could not see.
- **Read through the policy, a prompt is a grant change.** The question is not whether the repository is safe, but what the session becomes once it holds this and what it already holds. Read access to a public repository adds almost nothing. Write access to the same repository, from a session holding confidential data, adds a publishing channel.
- **The prompt is a real barrier, and a weak one.** It is enforced by the host, not the model, so the agent cannot click it. Its strength is the person's judgement, and the person was given three fields to judge with.
- **The record mostly puts the duty on whoever asks.** Consent forms signed routinely, clicks on unexplained buttons, onerous terms in small print and token human sign-offs have each been held not to carry the weight the asker wanted. In practice the blame still lands on the nearest person.
- **The fixes that worked put the why into the prompt.** Purpose strings on phones, number matching and location on sign-in pushes, refusal made as easy as acceptance on cookie banners.
- **The proposal is a why card.** Every field on it is something the agent already knows when it asks. When the risk rises, the card becomes a risk acceptance, with a holder, an interval and a record.

## The prompt

The prompt as it appeared on 7 October 2026: "Claude wants to add a repository to this session", with the owner, the repository, the access level, and two buttons. Screenshot, cropped.

The text was: Claude wants to add a repository to this session. Owner SGit-AI. Repository SGit-AI__Website. Access read. Decline, or Allow once.

That is everything the person had. The tool the agent calls to make this request, as listed in the session that wrote this article, takes the same three values, owner, repository and access, and nothing else. There is no field for a reason, so there is no reason to show.

Three things the prompt did right deserve saying first. It asked for read rather than write, the narrower of the two. It is enforced by the host rather than by the model, so the agent cannot approve its own request. And it offered Allow once rather than Allow always. Each of those is a control. None of them is visible to the person as a control, because the prompt does not say what the alternative would have been.

## The choice it offered

Decline breaks the work; Allow buys accountability without information; the third answer, a reason, was not offered. From the voice note of 7 October 2026.

The person asked the agent to do something, and the agent was getting on with it. The prompt arrived in the middle. Declining stops or derails a task the person started, and nothing on the screen says which step fails, whether the work so far survives, or how to resume. Allowing lets the task continue and makes the person the one who approved it, on the basis of a repository name and the word read.

Neither is a decision in the sense that matters. It is a choice between two costs that the prompt does not state. The answer that would have removed both costs, a sentence saying why, was not on the screen.

## The same request, read through the policy

The request through the Agent Behaviour Policy's words: the grant before and after, the mandate, the gap, the barrier, the blast radius and the kind of decision, for read access and for write access to the same public repository.

The [Agent Behaviour Policy](https://riskmandate.ai/abp.html) describes an agent with four words: the grant, everything it can technically reach; the mandate, what it is authorised to do; the gap between them; and the barrier that stops the excess. [Footprint and blast radius](footprint-and-blast-radius.md) adds two more: what the agent actually did, read afterwards, and what a row would cost if used in full.

A permission prompt is a request to change the grant in the middle of a session. That reframes the question. It is not "is this repository safe". It is "what does this session become once it holds this as well as what it already holds".

For read access to a public repository the answer is: very little. The session can read files anyone on the internet can read. The request tool's own documentation, in the session that wrote this, notes that read access to a public repository is often available without attaching anything at all. The blast radius is low and reversible, and the right record is a line in the session card.

For write access to the same repository the answer is different. A public repository is a publishing channel. A session that already holds a vault key for confidential data, and gains the ability to push to a public repository, has gained an exfiltration path: confidential data in, a public commit out, copied, cached and indexed within minutes. That is not a convenience. It is a risk, and under the policy a change that raises the blast radius of the session as a whole is a decision to accept a risk. [Every risk is already accepted](every-risk-is-already-accepted.md) argues that such a decision should name who accepts it, for how long, and what would end it.

The person could not tell which of these two they were being asked, because the prompt does not show the session's existing reach, and does not say that read was chosen over write or why.

The barrier, in the policy's terms, is the prompt itself. It is enforced outside the model, which makes it a boundary rather than an expectation. But a boundary whose enforcement is a human judgement is exactly as strong as the information that human is given. Withhold the why, and the boundary becomes a habit.

## How often people say yes

The numbers on that habit are now public, from the vendor of the product in the screenshot.

In October 2025 Anthropic wrote that sandboxing "safely reduces permission prompts by 84%" in its internal use, and that constant approving "can lead to 'approval fatigue', where users might not pay close attention to what they're approving". In March 2026, introducing auto mode, it wrote that "Claude Code users approve 93% of permission prompts". In August 2026, making auto mode the default from 14 August, it reported a study of 1,053 paid testers in which a single prompt was swapped for a clearly dangerous command: "The testers caught the dangerous command just 13.6% of the time", about 17% early in a session and about 5% after fifty or more prompts. These are vendor-run studies and have not been independently replicated.

Anthropic's answer is fewer prompts, decided by a classifier. That is a reasonable answer to fatigue, and it has a consequence: the prompts that remain are, by design, the ones the classifier could not settle, which makes them the ones where a person most needs the reason. Anthropic's own write-up of where its classifier fails is close to the argument of this article. The misses, it says, are about "whether a real consent signal in the session actually covers this action"; the classifier "finds approval-shaped evidence and stops short of checking whether it's consent for the blast radius of the action". A request that carried its reason, quoting the instruction it serves, is what would let either a classifier or a person check exactly that.

On accountability, the clearest statement is an exchange. In August 2025 Checkmarx showed that a malicious command could be hidden in a long Claude Code permission prompt. Anthropic's reply, which Checkmarx published as a screenshot in September 2025, treated it as outside its threat model and said: "Users are responsible for carefully reviewing all permission prompts (including scrolling up to see the entire prompt) before accepting them." Checkmarx's summary of the general problem was that "a human can only respond to what the agent prompts them with".

The same pattern, approvals that follow a prompt without following the reason, shows up in 2026 preprints on agent permissions: in one, 13 of 16 participants used "Always Allow" simply to dismiss prompts; in another, of 148 overreach actions executed under user-written policies, 133 went through after a person approved them. Both are preprints with small or simulated samples.

## Who is accountable

Who carries a decision taken without the information: courts, regulators and research from 1956 to 2023, grouped by where they put the burden. Not legal advice; sources in the Sources section.

The question in the voice note was direct: if a person is asked to make a decision and is not given the information to make it, who is liable, the person who clicked or the one who asked? Agents are new to this question. The question is not new. What follows is the shape of the record, not legal advice.

**The one who asks, and holds the information, has to disclose it in a usable form.** In medicine, the UK Supreme Court in Montgomery (2015) held that a doctor must make the patient aware of material risks, judged from the patient's position, and that the duty is not fulfilled "by bombarding the patient with technical information which she cannot reasonably be expected to grasp, let alone by routinely demanding her signature on a consent form". In contract, Denning's red hand rule (1956) says the more unreasonable a clause, "the greater the notice which must be given of it", and Interfoto (1987) that an onerous term binds only if "fairly brought to the attention" of the other party. Online, the Ninth Circuit in Berman (2022) held that "merely clicking on a button on a webpage, viewed in the abstract, does not signify a user's agreement to anything" unless the user is told what the click means, and in Nguyen (2014) that "the onus must be on website owners to put users on notice". In consumer law, the Consumer Rights Act 2015 says a trader "must ensure" a written term is transparent. In data protection, GDPR Article 7(1) puts the burden of demonstrating consent on the controller, and the EDPB's 2020 guidelines say that without accessible information "user control becomes illusory and consent will be an invalid basis".

**A token sign-off is not a human decision.** The Article 29 Working Party's guidance on automated decisions says the controller "cannot avoid the Article 22 provisions by fabricating human involvement", and that oversight must be "meaningful, rather than just a token gesture", by someone with "the authority and competence to change the decision". The Court of Justice in SCHUFA (2023) held that a machine output given "a determining role" is an automated decision even when a person signs. The EU AI Act's Article 14 requires that people overseeing high-risk systems be enabled to understand their limits and to "remain aware of the possible tendency of automatically relying or over-relying" on the output; those duties now apply from December 2027 after this year's amendment.

**The decider is not excused when they could have asked.** In Smith v Van Gorkom (Delaware, 1985), directors who approved a sale after two hours, without seeing the agreement or a valuation, lost the protection of the business judgment rule, which presumes an "informed basis". In UK financial services, a senior manager is liable for a contravention in their area if they "did not take such steps as a person in the senior manager's position could reasonably be expected to take". Both judge the decider on what they could have done. A prompt that offers no way to ask removes most of what they could have done.

**In practice, the blame lands on the nearest person.** Madeleine Clare Elish named this the moral crumple zone: the human in an automated system "bears the brunt of the moral and legal responsibilities when the overall system malfunctions", protecting the system "at the expense of the nearest human operator". The Post Office Horizon cases are the British example at scale: sub-postmasters had "no way of disputing shortfalls within Horizon", and the Court of Appeal found that the Post Office "effectively sought to reverse the burden of proof".

Read for a permission prompt, the asker is the agent and the product around it, which hold the context; the decider is the person. The doctrine, across these fields, puts the duty to make the information usable on the asker, and the duty to ask on the decider when asking is possible. In practice, the click is the record, and the click has the person's name on it. Which of the two wins is decided by the design of the prompt.

## Others who asked without a why, and what fixed it

Prompts that asked without a why, and the fixes that worked: purpose strings, number matching and context, refusal as easy as acceptance; and the ones still open, from OAuth scopes to agent prompts. Sources and dates in the article.

This is not the first prompt to ask without a reason, and several have been fixed. The fixes have the same shape.

**Mobile permissions.** Android's own documentation says the system dialog "says what permission your app wants, but doesn't say why", and tells developers to explain why before asking, in context. Apple went further: an app that accesses the camera, the microphone, contacts or location must declare a purpose string, a message that "tells people why the app is requesting access", and without one the access fails and the app can crash. App Review asks that purpose strings "clearly and completely describe your use of the data". The why is a required field, checked before the prompt can be shown.

**Sign-in approvals.** In September 2022 an attacker who had a contractor's password at Uber kept triggering approval pushes until, in Uber's words, "the contractor accepted one". Microsoft's answer was to put context into the prompt that only the real requester has: number matching, enforced for all Authenticator push notifications from 8 May 2023, and the application name and location of the sign-in shown on the prompt.

**Cookie banners.** In January 2022 the CNIL fined Google €150 million and Facebook €60 million because "several clicks are required to refuse all cookies, in contrast to a single one to accept them", and ordered a way of refusing "as simple as" accepting. Refusing must not cost more than accepting. The decline path of an agent prompt is the same problem: a person who knows the work survives a no can afford to say no.

**The ones still open.** Google requires a justification for every sensitive OAuth scope, but the justification goes to Google's reviewers; the person clicking sees "Read, compose, send, and permanently delete all your email from Gmail". GitHub's docs describe the permissions an app requests, and carry a justification only in the fine-grained token approval flow, as an optional field. The Model Context Protocol's specification says users "should understand what each tool does before authorizing its use", but its tool annotations say read-only or destructive, carry no reason, and "should be considered untrusted". And the research on warnings explains what happens meanwhile: 70.2% of Chrome's certificate warnings clicked through across more than 25 million impressions (2013); 51 seconds spent on terms of service that take fifteen minutes to read (2018); 85 to 99% of hospital alarms needing no action, and 80 deaths in 98 alarm-related events reported to the Joint Commission between 2009 and 2012.

Herley's 2009 paper put the rational version plainly: users' rejection of security advice "is entirely rational from an economic perspective". A prompt that cannot be judged will be clicked. Böhme and Grossklags (2011) called attention "a scarce resource" and every unnecessary prompt a cost imposed on the others who need that attention.

## The why card

A proposal: the same request as a why card, with the session and step, the reason quoting the instruction, the change in reach, the cost, the path if declined, the scope and the record; buttons to allow for the task, decline and continue, ask a question, or park it. The reason shown is illustrative.

Every field on the card is something the agent already knows at the moment it asks. Nothing on it needs a new capability, only that the request carry the context the agent is holding.

- **Who is asking.** The session, the task it was given and when, and the step it is on. With several sessions running, this is the first thing a person needs and the prompt in the screenshot did not have it.
- **Why.** The step that needs the access, and the instruction it serves, quoted. This is the field a classifier or a person needs to check that consent covers the action. It should be required: no reason, no prompt, the way a phone app with no purpose string gets no camera.
- **What changes.** The reach the session gains, shown next to the reach it already holds, and what was not requested. Read, not write, is a control only if the person can see it was a choice.
- **What it could cost.** The worst use of the new reach, and whether it can be undone.
- **If you decline.** What the agent will do instead, and whether the work survives. This is the CNIL's rule applied to agents: declining must not cost more than allowing.
- **Scope and record.** How long the grant lasts, and where the request, the reason and the answer are written. The record pairs the reason given with what the session then did, which is the footprint; a reason that does not match the footprint is a finding.
- **Buttons.** Allow for this task. Decline and continue without it. Ask a question first. Park it and ask at the end. The third is the one the screenshot lacked: a way to ask why.

When the change raises the blast radius of the session as a whole, write to a public repository from a session holding confidential data being the example, the card should stop being a prompt and become a risk acceptance: who accepts it, for how long, what would end it, recorded as such. The [risk acceptance vault](https://sgit.ai/demos/vaults/risk-acceptance/index.md) is a worked example of that record, and [RiskMandate's acceptable-risk page](https://riskmandate.ai/acceptable.html) is the product end of it.

## What this site's own team already does, and what it does not

The agent team described in [The Mandate Stack](the-mandate-stack.md) asks its person for decisions too, and the format it settled on is close to a why card: a decision draft in the email thread, with the question, lettered options and an answer box, read back on the next run. Its session cards count the tools, files and network calls each session used and flag anything outside the mandate, which is the record half of the card. What it does not have is a required reason on a mid-session grant change: a session that needs a new repository, connector or vault asks the same way the screenshot did. [Six agents, one inbox](six-agents-one-inbox.md) and [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) are the earlier work on fixing grants before a session starts, which is the other way to need fewer prompts.

## What is not known

- Which session made the request in the screenshot, and why. The prompt did not say, and nothing recorded it where the person could see.
- Whether the fields of this prompt can be configured by the person or an administrator. The documentation consulted for this article does not describe a reason field.
- How well Anthropic's figures generalise. They are the vendor's own studies; the one independent comment found asked for independent confirmation.
- The law. The cases and rules above are cited for the shape of the reasoning, across several jurisdictions, and none of them has been applied to an agent permission prompt by a court that this research found. This is not legal advice.

## Threads woven here

- [Footprint and blast radius](footprint-and-blast-radius.md) and [the brief that proposed them](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.md): the words the policy reading uses, and the record that pairs a reason with what was done.
- [Every risk is already accepted](every-risk-is-already-accepted.md) and [the risk acceptance vault](https://sgit.ai/demos/vaults/risk-acceptance/index.md): what a grant change becomes when it raises the risk, and how to record it.
- [The ultimate insider](ultimate-insider-three-collisions.md): why the infrastructure around agents has not caught up with what they can reach.
- [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md): the same prompts on a laptop, where the grant is the person's whole account.
- [The Mandate Stack](the-mandate-stack.md) and [The agent team as it runs](the-agent-team-as-it-runs.md): decision drafts and session cards, the nearest thing this site's team has to a why card.
- [Six agents, one inbox](six-agents-one-inbox.md) and [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md): fixing the grant before the session, so fewer grant changes are asked for during it.
- [A personal agent that keeps your secrets](a-personal-agent-that-keeps-your-secrets.md): the policy as the permission authority, the barrier that would decide grant changes outside the agent.
- [The sandbox brief](https://sgit.ai/docs/briefs/riskmandate-sandbox-twins-and-tokens.md): a place where a policy, and a prompt, can be tested rather than read.

## Sources

- The screenshot and a voice note by Dinis Cruz, 7 October 2026. The repository's visibility was checked against GitHub's public API on the same day.
- Medicine and contract: [Montgomery v Lanarkshire Health Board [2015] UKSC 11](https://supremecourt.uk/uploads/uksc_2013_0136_judgment_fd5635b4cd.pdf), paras 87 to 90; J Spurling Ltd v Bradshaw [1956] 1 WLR 461 and Interfoto Picture Library v Stiletto Visual Programmes [1989] QB 433, quoted from secondary sources; [Berman v Freedom Financial Network, 9th Cir., 5 April 2022](https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/05/20-16900.pdf); [Nguyen v Barnes & Noble, 9th Cir., 18 August 2014](https://cdn.ca9.uscourts.gov/datastore/opinions/2014/08/18/12-56628.pdf); [Consumer Rights Act 2015, s.64](https://www.legislation.gov.uk/ukpga/2015/15/section/64) and [s.68](https://www.legislation.gov.uk/ukpga/2015/15/section/68).
- Data protection and automated decisions: [GDPR Article 4](https://www.legislation.gov.uk/eur/2016/679/article/4/adopted) and Article 7; [EDPB Guidelines 05/2020 on consent](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf); [Article 29 Working Party, WP251rev.01](https://ec.europa.eu/newsroom/article29/redirection/document/49826); [CJEU SCHUFA, C-634/21, 7 December 2023](https://curia.europa.eu/jcms/upload/docs/application/pdf/2023-12/cp230186en.pdf); EU AI Act, Regulation 2024/1689, Articles 14 and 26, with application dates as amended by Regulation 2026/1744, per [Cooley, 3 August 2026](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/).
- Decisions by those accountable: Smith v Van Gorkom, 488 A.2d 858 (Del. 1985), from secondary sources; [Companies Act 2006, s.174](https://www.legislation.gov.uk/ukpga/2006/46/section/174); [Financial Services and Markets Act 2000, s.66A](https://www.legislation.gov.uk/ukpga/2000/8/section/66A); [Hamilton v Post Office, 23 April 2021](https://www.judiciary.uk/wp-content/uploads/2022/07/Hamilton-Others-v-Post-Office-judgment-230421.pdf); [Elish, "Moral Crumple Zones", Engaging Science, Technology, and Society, 2019](https://estsjournal.org/index.php/ests/article/view/260).
- Prompts and their fixes: [Apple, requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) and [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/); [Android, request runtime permissions](https://developer.android.com/training/permissions/requesting); [Uber, security update, September 2022](https://www.uber.com/newsroom/security-update/); Microsoft number matching as reported by [BleepingComputer, 8 May 2023](https://www.bleepingcomputer.com/news/microsoft/microsoft-enforces-number-matching-to-fight-mfa-fatigue-attacks/) and [additional context on Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-additional-context); the CNIL decisions of January 2022 as reported by [SCL, 11 January 2022](https://www.scl.org/12482-french-data-protection-regulator-fines-google-and-facebook-for-making-it-harder-to-refuse-cookies-than-to-accept-them/); [Google, sensitive scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification); [GitHub, managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens); [Model Context Protocol specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28).
- Research on warnings and attention: [Akhawe and Felt, "Alice in Warningland", USENIX Security 2013](https://www.usenix.org/system/files/conference/usenixsecurity13/sec13-paper_akhawe.pdf); [Felt et al., SOUPS 2012](https://cups.cs.cmu.edu/soups/2012/proceedings/a3_Felt.pdf); Obar and Oeldorf-Hirsch, "The biggest lie on the Internet", Information, Communication & Society, 2018; [Herley, NSPW 2009](https://gwern.net/doc/cs/security/2009-herley.pdf); Böhme and Grossklags, NSPW 2011; [Cranor, UPSEC 2008](https://www.usenix.org/legacy/event/upsec/tech/full_papers/cranor/cranor.pdf); The Joint Commission, Sentinel Event Alert 50, April 2013.
- Agent prompts: [Anthropic, "Beyond permission prompts", 20 October 2025](https://www.anthropic.com/engineering/claude-code-sandboxing); [Anthropic, "How we built Claude Code auto mode", 25 March 2026](https://www.anthropic.com/engineering/claude-code-auto-mode); [Anthropic, auto mode as the default, 7 August 2026](https://claude.com/blog/auto-mode-default-in-claude-code); [Claude Code permission modes](https://code.claude.com/docs/en/permission-modes); [Checkmarx, "Lies-in-the-Loop", 15 September 2025](https://checkmarx.com/zero-post/bypassing-ai-agent-defenses-with-lies-in-the-loop/); the preprints arXiv 2605.11360 and 2608.27443.

*Drafted from a screenshot and a voice note by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026, with a research agent in the same session verifying the cases, rules and figures against primary sources where they could be reached; the ones taken from secondary sources are marked as such. The screenshot is the real prompt; the why card is a proposal, and the reason on it is illustrative. No key or token appears in any figure or file.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policy[This article as a graph →](graphs.md#where-is-the-why)

### Builds on

- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.

### Continued by

- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md) Nine properties a safe agent desktop needs, nine products against them, the macOS day-long lease, and the startup credits that would pay for testing it.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 39 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=39)

## From the desk

- [How agents decide, and when they stop](collections/how-agents-decide.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [where-is-the-why.jpg](banners/where-is-the-why.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-is-the-why.html)*
