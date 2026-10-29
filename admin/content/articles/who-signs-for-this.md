---
title: Who signs for this? Accountability maps from the hardware to the business, what is measured and what is declared, and why the parts nobody signs are the blind spots worth paying to see
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: My article on who maintains the PHP you run argued for versions signed off by the people who maintain them. On LinkedIn, Andrey Lazarev, co-founder and CEO/CTO of TactiQ AI, took it a step further. A maintainer's signature says who stands behind a version, not whether that version is what the device actually booted. That needs a measured boot record, checked against the signed reference by someone other than the supplier. And the context of where it runs splits in two: what the device can measure itself, and what it cannot see, which has to be declared and signed by an operator or an auditor. A certificate stays honest when it keeps the two apart and names who signed each line. I think that is exactly right, and it generalises. Once people sign for what they are accountable for, they also define what they do not sign for. Map every layer, from the hardware to the business contract, and each line ends either in somebody who signed, or in a blind spot. That map is a fractal graph of signed certificates, and complexity is not the objection: how much of it you need depends on how much the application matters. The point is to make the blind spots visible, so the business and its insurers can decide whether they are comfortable with them, and so the experts who close them get paid. And when the person who signed leaves, the gap shows.
version: v0.13.69
license: https://creativecommons.org/licenses/by/4.0/
tags: accountability, signatures, attestation, supply-chain, maintenance, fractal-graphs, article
status: published
---

!shot ky-map.webp | images/ | An accountability map from the business to the hardware: who signs each layer, with the building signed by nobody. | concept

## In short {#in-short}

- **A signature says who stands behind a version.** It does not say that the version is what is running.
- **Andrey Lazarev's split.** Some context the device can measure; the rest has to be declared and signed by someone.
- **Somebody has to be accountable.** The person you pay to maintain it, patch it, fix it and handle its incidents.
- **Signers define the gaps.** What they sign, and what they do not, is the shared responsibility model taken all the way up and down.
- **Every line is a graph of its own.** A fractal graph of signed certificates, across hardware, software, products and contracts.
- **The point is the blind spots.** The lines nobody signs, made visible, so someone decides whether they are acceptable.
- **The experts who close them get paid.** And when the person who signed leaves, the gap shows.

## The thread {#thread}

!shot ky-thread.webp | images/ | The LinkedIn thread under my post sharing "Who maintains the PHP you run?", 24 October 2026. | small | aside

I shared [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html) on LinkedIn, and it started a thread worth more than a reply. Andrey Lazarev, co-founder and CEO/CTO of TactiQ AI, wrote:

> "the sign-off you describe answers “who stands behind this version”. The step after it is “is that version what the device actually booted”. On a device that is a measured boot record checked against the signed reference, by someone other than the supplier."

Without that, as he put it, the buyer holds a maintainer's signature for something they cannot prove is running. I replied that once we can make somebody accountable for what is running, we will also need to certify where it runs and its context, for example how secure the deployment is. His answer is the one this article is built on:

> "In my view that part splits in two. Some of the context the device can measure itself: firmware, bootloader, kernel configuration, and which hardware root signed the record. The rest it cannot see: who can reach it physically, what network it sits on, what is plugged into it. That part is a declaration by the operator or an auditor, signed by them. I think a certificate stays honest when it keeps the two apart and names who signed each line."

I called it a fractal graph architecture: in this case, a big graph of signed certificates. Here is what I meant.

## Somebody has to be accountable {#accountable}

When we talk about making people accountable for code by signing it, the point is not the signature. The point is that somebody has to be accountable. Some person or company will be looking at each part of the infrastructure, and what we do not want is a part that nobody is looking at.

And we know who that should be. It is the person who maintains it, the person you pay for it: responsible for patching it, fixing it, handling its security incidents, being able to rebuild it, replicate it and move it. All of the non-functional requirements. That is the same argument as [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html): the ability to change a system safely has to belong to someone.

## Signers define the gaps {#gaps}

Here is the interesting part. Once people sign off, they define the gaps. They say what they sign for, and, just as important, what they do not.

We already do this between companies and cloud providers. AWS calls it [the shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/): security "of" the cloud versus security "in" the cloud. AWS is "responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud", its "hardware, software, networking, and facilities", and some controls a customer simply inherits: "Physical and Environmental controls". [Microsoft](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) says the same in its words, "For all cloud deployment types, you own your data and identities", and [Google](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) goes a step further with "shared fate", where it works more closely with the customer on the customer's side of the line. And the providers do sign: [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) hands customers the SOC reports and ISO certificates that attest to AWS's side, while reminding them they remain "responsible for developing or obtaining documents that demonstrate the security and compliance of their companies".

What I am saying is that this model should go all the way to the top. Not only the infrastructure, but the application, the product, and the business. A cloud provider can sign that a customer's use is within its guidance, with this level of security capability and these controls. A maintainer can sign the version. A product owner can sign that what was delivered is what was asked for. A business owner can sign that the application does what the contract says. And it goes down as well, all the way to the hardware. You can go in every direction.

## What is measured, and what is declared {#measured}

Andrey's split is what keeps this honest. Some lines can be measured; others can only be declared.

On a device, the measured line has a well-defined shape. The firmware writes a hash of each thing it loads into the TPM's registers and an event log: "The preboot firmware maintains an event log that gets new entries every time something gets hashed by it to any of the PCR registers", in the [Linux kernel's description](https://docs.kernel.org/security/tpm/tpm_event_log.html). Remote attestation then has named roles, set out by the IETF in [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334): an Attester produces Evidence; a Verifier "appraises the validity of Evidence about an Attester and produces Attestation Results to be used by a Relying Party"; an Endorser, "typically a manufacturer", vouches for the hardware; a Reference Value Provider supplies the "known-good values" the measurements should match. Every role is someone who signs. That is Andrey's "checked against the signed reference, by someone other than the supplier".

Software has its own measured lines. [SLSA](https://slsa.dev/spec/v1.2/build-provenance) provenance describes "how an artifact or set of artifacts was produced" so consumers can "verify that the artifact was built according to expectations", and since version 1.2 its source track goes up to level 4, "Require code review". [in-toto](https://in-toto.io/) records "what steps were performed, by whom and in what order". [Sigstore](https://docs.sigstore.dev/about/overview/) puts signing events in a transparency log so they "can be publicly audited". And this week we built a small version for a running process: a [process behaviour policy](https://newsroom.sgit.ai/articles/process-behaviour-policies.html), traced from one run, listing every file, system call and host a process needs, and enforced by the kernel.

The declared lines are the rest: who can reach the machine, what network it sits on, what is plugged into it, whether the product does what the business needed. Those cannot be measured from inside. They are statements, and their value is exactly who signed them. ISO/IEC 27001 has a whole group of physical controls, from perimeters and entry to monitoring and the disposal of equipment, and an auditor signs that they are in place. The honest certificate keeps the two kinds apart, and names the signer of each.

## A fractal graph of signed certificates {#fractal}

!shot ky-fractal.webp | images/ | Every signed line is a graph of its own: the device line opens into measurement, reference, verifier and endorsement. | concept

This is why I call it fractal. It is the same idea as [fractal semantic graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html): there are multiple universes, multiple domains, each a graph that can be opened into more graph. Here the domains are hardware, software, business applications and even business contracts. Is the application actually doing what it is supposed to do? Have the business owners signed that? Have the product owners signed what was delivered? Has someone read the code that went live? Is the release the one the maintainers stand behind? Is it what booted? Every one of those is a line, every line has a signer, and every signature can be opened into its own graph of evidence and the people who stand behind it.

## The blind spots {#blind-spots}

The point of all this is to identify the areas nobody is responsible for. Those blind spots are where the risk is, and where the commercial opportunity is.

Take physical security. If you host in a data centre, the provider signs for it. If your server sits somewhere else, then whoever maintains that physical security should be signing off, on the record, connected to the system they protect. Otherwise you have black magic: a piece of the puzzle that nobody can account for.

A blind spot is not automatically a failure. It is a decision: is the business comfortable with that blind spot, and that level of assurance? Are the insurers? That is ultimately what we pay for. But today those blind spots exist without anyone deciding about them, because nobody can see them.

A lot of people look at this and say it is too complex. I do not think so. It means that, depending on how important the application is and its context, you want more or less of it. A hobby site needs one line. A payment system needs the whole map. The problem right now is that organisations spend a lot of money on highly critical applications without visibility of their blind spots. My point is to make those visible: somebody is paying attention, somebody is certifying something, and where nobody is, that is a blind spot, named.

## The experts sign, and get paid {#experts}

The people who should sign are the experts: the people who actually understand each layer. Doing it in a scalable way means the experts get the money, and the money funds the work. That is the [commercial model](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html) of signed versions, extended to every line of the map.

It also says something about who can sign what. In the language of [explorers, villagers and town planners](https://newsroom.sgit.ai/articles/explorer-coding.html), an explorer team can only give so many guarantees, and should say so. Town planners can sign for much more, because that is their job. The map makes the difference visible: did somebody read the code that goes live? Are the people who wrote it still in the building?

## When the person who signed leaves {#leaves}

Here is an interesting consequence. If a certification is connected to a person, and that person leaves the company with nobody to replace them, then nobody certifies that code any more. The line goes from signed to blind spot, and everyone can see it.

That would do wonders for something we rarely measure. Companies would think twice before letting the talent that holds a system together walk out of the door, or before cutting it because they can and do not see the risk, until the whole thing blows up and the people who could fix it are not in the building any more. Research on open source shows how thin that line already is: in a study of 133 popular GitHub projects, 65% had a [truck factor](https://arxiv.org/abs/1604.06766) of two or fewer, "the minimal number of developers that have to be hit by a truck (or quit) before a project is incapacitated". A signed map makes that visible before the truck arrives. It is also why [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html) matters: agent sessions that keep a system's knowledge can be part of who stands behind it.

There is a precedent for tying a signature to a person. In the UK, the FCA's [Senior Managers and Certification Regime](https://www.fca.org.uk/firms/senior-managers-certification-regime) exists to make "individuals more accountable for their conduct and competence". In the US, [Sarbanes-Oxley](https://www.law.cornell.edu/uscode/text/15/7241) has the chief executive and the chief financial officer certify that they have reviewed each report and "are responsible for establishing and maintaining internal controls". We already accept that someone signs for the numbers. The systems that produce the numbers deserve the same.

## What this does not claim {#limits}

- **The map is an illustration.** It is the shape of the argument, not an audit of any system.
- **Measured is not the same as safe.** A boot record proves what booted, not that it is free of flaws.
- **A signature can be wrong.** It makes someone accountable, which is the point, not infallible.
- **The software tools are partial.** SLSA, in-toto and Sigstore cover build and source; nothing yet signs "the product does what the contract says" in the same way.
- **The ISO 27001 detail is from a secondary source.** The standard itself sits behind ISO's paywall.
- **Andrey's comments are quoted from the LinkedIn thread,** shown in the screenshot; the first is cut where LinkedIn truncates it.

## Where this comes from {#sources}

The LinkedIn thread under my post sharing [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), 24 October 2026, with Andrey Lazarev's comments quoted from it; and my voice memos the same evening. Sources, read on 24 October 2026: IETF [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334); the Linux kernel's [TPM event log](https://docs.kernel.org/security/tpm/tpm_event_log.html); Microsoft on [measured boot and host attestation](https://learn.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation) and [shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility); AWS's [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) and [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html); Google Cloud's [shared responsibility and shared fate](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate); [SLSA 1.2](https://slsa.dev/spec/v1.2/build-provenance); [in-toto](https://in-toto.io/); [Sigstore](https://docs.sigstore.dev/about/overview/); URM Consulting on [ISO/IEC 27001:2022 physical controls](https://urmconsulting.com/blog/iso-27001-2022-annex-a-physical-controls); Avelino, Passos, Hora and Valente, [A Novel Approach for Estimating Truck Factors](https://arxiv.org/abs/1604.06766), ICPC 2016; the FCA on [SM&CR](https://www.fca.org.uk/firms/senior-managers-certification-regime); [15 U.S.C. § 7241](https://www.law.cornell.edu/uscode/text/15/7241). Related: [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html), [process behaviour policies](https://newsroom.sgit.ai/articles/process-behaviour-policies.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), [a team frozen in time](https://newsroom.sgit.ai/articles/a-team-frozen-in-time.html), [introducing fractal semantic graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html), [underwriting the agent economy, reviewed](https://newsroom.sgit.ai/articles/underwriting-the-agent-economy-reviewed.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
