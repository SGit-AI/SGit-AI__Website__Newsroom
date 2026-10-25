---
title: Software is now a product: what the EU's new Product Liability Directive actually says about software, SaaS and updates, how it would apply to php2shell, and the questions it leaves open
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: Lauren Zabierek shared a card on LinkedIn about the EU's new Product Liability Directive, 2024/2853: the 1985 directive never named software, and the new one makes it a product, subject to strict, no-fault liability that a EULA cannot waive, for products placed on the market after 9 December 2026. I asked under the post how it applies to SaaS, so I read the directive itself. Software is a product "irrespective of the mode of its supply", and the recitals name SaaS. Updates matter: a manufacturer cannot escape liability by saying the defect came later if it is due to software, an update, or a lack of updates needed to maintain safety, while the product is in its control; and an attacker's exploit does not reduce its liability. But the directive is narrower than it sounds. Only natural persons can claim, and only for death or injury, property not used only for work, or data destroyed or corrupted that is not used for work. A data leak is not on the list, and a company cannot claim for its own losses. Applied to php2shell, the PHP project is out of scope; a vendor or SaaS that leaves a known, fixed flaw unpatched and lets attackers wipe consumers' files is likely in. Patching does not bring an old product into scope, but a new one that is not patched has no defence. Here is what the articles say, and the questions they leave.
version: v0.13.81
license: https://creativecommons.org/licenses/by/4.0/
tags: regulation, liability, software, saas, cybersecurity, php2shell, briefing, article
status: published
---

!shot lz-card.webp | images/ | Lauren Zabierek's post on LinkedIn, 25 October 2026: a card, R-05, on the Product Liability Directive. The 1985 directive never named software; Directive 2024/2853 makes standalone software, SaaS, AI systems and digital manufacturing files products, subject to strict, no-fault liability; courts can presume defectiveness and causation where a defect is too complex to prove; the liability cannot be waived by a EULA; it applies to products placed on the EU market from 9 December 2026. | small | aside

## In short {#in-short}

- **Software is now a product,** "irrespective of the mode of its supply", SaaS included.
- **Updates count.** A lack of updates needed for safety is no defence, while the product is in the maker's control.
- **An attacker's exploit does not reduce liability.** A EULA cannot exclude it.
- **But only people can claim,** and only for injury, private property, and private data destroyed or corrupted.
- **A data leak is not covered, and neither is a company's own loss.**
- **php2shell:** the PHP project is out; a vendor or SaaS that leaves the fixed flaw unpatched is likely in.
- **Patching does not pull an old product into scope.** Not patching a new one has no defence.

## Why I read it {#why}

[Lauren Zabierek](https://www.linkedin.com/posts/laurenz1010_share-7520128390050529280-M2XB/) shared a card on LinkedIn that summarises the new directive. Under the post I asked whether there was a mapping of how it applies to SaaS. Rather than wait, I read [Directive (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng) itself, articles and recitals, and tested it against the story we have been following on [the PHP site](https://php.oct.2026.newsroom.sgit.ai/). This is a briefing and a list of questions, from an engineer reading the text. It is not legal advice, and courts in 27 member states will decide what it means.

The card is accurate. Two small precisions: the articles name software and digital manufacturing files as products, while SaaS and AI systems are named in the recitals that explain them; and the directive applies to products placed on the market "after", not from, 9 December 2026.

## What the articles say {#articles}

!shot lz-tests.webp | images/ | Does the new Product Liability Directive bite? Six questions, in order: is it a product (software is, including SaaS; services as such and mere source code are not); was it placed on the market after 9 December 2026; was it supplied in a commercial activity (non-commercial open source is excluded); is the injured person a natural person; is the damage covered (injury, private property, private data destroyed or corrupted); is the product defective (judged with safety-relevant cybersecurity requirements). Then the defences, and what is not a defence. | concept

**Software is a product.** Article 4(1): "'product' means all movables … it includes electricity, digital manufacturing files, raw materials and software". Recital 13 removes any doubt about delivery: software is a product "irrespective of the mode of its supply or usage, and therefore irrespective of whether the software is stored on a device, accessed through a communication network or cloud technologies, or supplied through a software-as-a-service model". Two exclusions in the same recital: information is not a product, nor is "the mere source code of software". And recital 17: the directive "should not apply to services as such", though a digital service integrated into a product, a "related service", counts as a component of it.

**Only for new products.** Article 2(1): it applies "to products placed on the market or put into service after 9 December 2026". The 1985 directive keeps applying to anything placed earlier (Article 21). But a product "substantially modified", including "through a software update or upgrade", is treated as placed on the market again when the modification is made (recital 40).

**Open source, outside commerce, is out.** Article 2(2) excludes "free and open-source software that is developed or supplied outside the course of a commercial activity". When a manufacturer builds such software into a commercial product, that manufacturer can be liable for it, not the project (recital 15).

**Only people, and only some damage.** Article 5 gives the right to compensation to "any natural person". Article 6 lists the damage: death or personal injury, "including medically recognised damage to psychological health"; damage to property, except the product itself and property "used exclusively for professional purposes"; and "destruction or corruption of data that are not used for professional purposes". Recital 22 goes further: data used for professional purposes "even if not exclusively so" is excluded.

**Defective, with cybersecurity.** Article 7: a product is defective when it "does not provide the safety that a person is entitled to expect", judged with all circumstances, including "safety-relevant cybersecurity requirements" and, where the manufacturer keeps control, "the moment in time when the product left the control of the manufacturer". Recital 32: a product "can also be found to be defective on account of its cybersecurity vulnerability".

**Easier to prove.** The defendant can be ordered to disclose evidence (Article 9). Defectiveness is presumed if it fails to, if the product breaks mandatory safety rules, or if there is an obvious malfunction (Article 10(2)); and a court shall presume defectiveness or causation where technical complexity makes proof excessively difficult and the claimant shows it is likely (Article 10(4)).

**Updates, and the defences that are gone.** A manufacturer is normally not liable if it proves the defect probably did not exist when the product was placed on the market (Article 11(1)(c)). But Article 11(2) removes that defence where the defect is due to "software, including software updates or upgrades" or "a lack of software updates or upgrades necessary to maintain safety", provided it is within the manufacturer's control; and "control" includes having "the ability to supply software updates or upgrades" (Article 4(5)(b)). A third party exploiting the defect does not reduce liability (Article 13(1); recital 55 names "a third party exploiting a cybersecurity vulnerability"), while an injured person who negligently failed to install an update can see it reduced (Article 13(2)). No contract can limit or exclude it (Article 15). Claims expire 10 years after the product was placed on the market (Article 17).

## php2shell, under the new rules {#php}

!shot lz-php.webp | images/ | php2shell under the new directive: the PHP project, no, open source outside a commercial activity; a vendor shipping an appliance or app on unpatched PHP, likely, for a consumer's injury, property or personal data destroyed; a SaaS whose unpatched PHP lets attackers wipe or encrypt consumers' personal files, likely; the same SaaS if attackers only steal the data, not under this directive; a business that loses its own data, no claim under this directive; a product shipped on end-of-life PHP 7.4, hard to defend. A reading of the text, not legal advice. | concept

The PHP story gives us real cases. The two flaws were fixed in PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12 on 21 October 2026; the end-of-life branches, 7.4 to 8.1, got backport branches but no release. The Dutch NCSC's list tracks [674 products](https://github.com/NCSC-NL/php2shell) that ship or depend on PHP: 206 marked vulnerable, 418 still under investigation and 46 fixed, as the site recorded it. And, as of 25 October, no named organisation has said it was compromised.

The directive would not apply to any of this today, because none of these products was placed on the market after 9 December 2026. But suppose the same flaw were found in 2027, in products placed on the market after that date. Our reading:

- **The PHP project:** out of scope, as free and open-source software developed outside a commercial activity.
- **A vendor whose product runs on PHP,** an appliance, a control panel or an app, that ships or leaves the flaw unpatched after the fix is public: likely liable to a consumer for injury, private property or private data destroyed. It cannot say the defect came later, because the lack of an update was within its control.
- **A SaaS whose unpatched PHP lets attackers wipe or encrypt its consumer users' files:** likely liable. SaaS software is a product, corrupted personal data is a covered damage, and the attacker does not reduce its liability.
- **The same SaaS, if attackers only steal the data:** not under this directive. A leak is not destruction or corruption; the GDPR and contract law apply instead, and the directive says it does not affect them (Article 2(4)).
- **A business customer that loses its own data or systems:** no claim under this directive. It is not a natural person, and its data is professional. Contract and national law still apply.
- **A product placed on the market on end-of-life PHP 7.4,** with no official release of the fix: hard to defend. The flaw is public, so the defence that the state of knowledge could not discover it (Article 11(1)(e)) is gone.

So, the question I started with: would a company with evidence of exposure to php2shell, which did not patch and then got compromised, be liable? Under this directive, for a product placed on the market after 9 December 2026, to consumers, for the covered damages: likely, yes. To its business customers, or for a leak: not under this directive.

## Will it stop companies updating? {#incentives}

The worry is a perverse incentive: if updating brings a product into scope, do not update, or shut it down. The text makes that weaker than it sounds.

- **A security patch is unlikely to be a "substantial modification".** Article 4(18) defines one as a change to the product's "original performance, purpose or type" that was not foreseen in the manufacturer's risk assessment and that changes or increases the hazard. A patch that closes a flaw does the opposite. Updates that are not substantial "should not affect the expiry period" (recital 58).
- **For new products, not updating is no defence.** Article 11(2)(c) makes the lack of a needed security update the manufacturer's problem, as long as it can still supply one.
- **The directive does not oblige anyone to provide updates** (recital 51). The incentive comes from liability, not a duty.
- **Shutting down limits future damage, not past.** Claims run for 10 years from when the product was placed on the market.

## The questions it leaves {#questions}

- **When is a SaaS "placed on the market"?** At launch, or never fully, because it never leaves the manufacturer's control? A SaaS launched before 9 December 2026 and updated daily may stay under the old directive for years, unless some update is "substantial".
- **Where does a product end and a service begin?** The directive covers SaaS software but not "services as such" (recital 17). Is a web application a product, and the hosting a service?
- **Who is the manufacturer of a self-hosted WordPress site?** The open-source project is out; the agency that built and sells it, or the host that runs it, may be in.
- **What about end of support?** One commenter under Lauren's post noted that a product's end of support under the Cyber Resilience Act does not end its liability under this directive. "Control" means the ability to supply updates; can a manufacturer end that ability, and with it the liability, before the 10 years are up?
- **How does it line up with the Cyber Resilience Act?** The CRA's reporting duties already apply since 11 September 2026 and the rest from 11 December 2027 ([Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng), Article 71), and its "safety-relevant cybersecurity requirements" will help courts judge defectiveness. But the CRA leaves out websites and cloud services developed outside a product's manufacturer, including SaaS (its recital 12), which this directive includes.
- **Will it reach business losses at all?** As written, no. The pressure on SaaS will come from consumers, insurers and the CRA, more than from companies suing each other.

## What this does not claim {#limits}

- **This is a reading of the text, not legal advice.** Member states transpose it by 9 December 2026, and courts will interpret it.
- **The php2shell cases are hypothetical:** today's products are under the old directive.
- **Lauren Zabierek's post is quoted from the card in the screenshot;** the rest of the post needs a sign-in.

## Where this comes from {#sources}

Lauren Zabierek's [post on LinkedIn](https://www.linkedin.com/posts/laurenz1010_share-7520128390050529280-M2XB/), 25 October 2026, from a screenshot, and its public comments; my voice memo of the same day. [Directive (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng) on liability for defective products, Official Journal of 18 November 2024, and [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng), the Cyber Resilience Act, both read on EUR-Lex on 25 October 2026. The PHP story site's data on affected versions, the NCSC-NL product list and compromises, at release v0.22.2. Related: [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), [simplified, or outsourced?](https://newsroom.sgit.ai/articles/simplified-or-outsourced.html), [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), [the policy draws the liability line](https://newsroom.sgit.ai/articles/the-policy-draws-the-liability-line.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
