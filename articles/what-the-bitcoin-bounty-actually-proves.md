# What the $2,000 bitcoin bounty actually proves: php2shell's real timeline, whether a firewall could have seen it coming, and what hardening can and cannot do without the patch, sgit.ai

> A researcher won a public "steal my bitcoin" bounty against a deliberately vulnerable PHP server, a rare independent, live confirmation that php2shell gives an attacker full control of a machine. I wanted to know more than that it worked. How hard was it, really, once the target was actually reachable? Could a web application firewall have blocked it, given how many vendors say they already detect it? And if you cannot patch today, does hardening the server around PHP, rather than PHP itself, actually protect you? The answers, checked against the operator's own site, the researcher's public write-up, five vendors' own advisories and GrapheneOS's own record of a server it chose to take offline rather than trust its own mitigations: the bounty took three hours once there was a page to attack, not the nineteen the headlines reported; every vendor's own detection coverage comes with a gap it names itself; and every hardening measure anyone has published is described by its own authors as partial. Patching remains the only complete fix.

*Source: <https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What the $2,000 bitcoin bounty actually proves: php2shell's real timeline, whether a firewall could have seen it coming, and what hardening can and cannot do without the patch

# What the $2,000 bitcoin bounty actually proves: php2shell's real timeline, whether a firewall could have seen it coming, and what hardening can and cannot do without the patch

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-26 · [article v1.0.0](versions/what-the-bitcoin-bounty-actually-proves.md) · [newsroom v0.13.97](https://newsroom.sgit.ai/admin/versions.html) · php2shellsecurityexploitationdetectionwafarticle

***Abstract:** A researcher won a public "steal my bitcoin" bounty against a deliberately vulnerable PHP server, a rare independent, live confirmation that php2shell gives an attacker full control of a machine. I wanted to know more than that it worked. How hard was it, really, once the target was actually reachable? Could a web application firewall have blocked it, given how many vendors say they already detect it? And if you cannot patch today, does hardening the server around PHP, rather than PHP itself, actually protect you? The answers, checked against the operator's own site, the researcher's public write-up, five vendors' own advisories and GrapheneOS's own record of a server it chose to take offline rather than trust its own mitigations: the bounty took three hours once there was a page to attack, not the nineteen the headlines reported; every vendor's own detection coverage comes with a gap it names itself; and every hardening measure anyone has published is described by its own authors as partial. Patching remains the only complete fix.*

The real timeline: the challenge launched at 08:21 UTC on 21 October with no page that executed PHP at all, so the flaw could not be reached; the operator added one at 22:00 JST on 25 October; it was solved about three hours later, at 00:47 JST on 26 October, not the "19.28 hours" the site's own counter and most press reports gave.

## In short

- **A real, independent, live win.** Not a lab claim: a researcher broke into a deliberately vulnerable public server and published how.
- **The real number is three hours, not nineteen.** The target had no PHP-executing page to attack for most of that time.
- **It needed an exact build.** The published method is tuned to one specific PHP image; a different one and it fails outright.
- **It is a race, not a certainty.** The author's own repeated runs against their lab succeeded about seven times in ten.
- **Every vendor names its own gap.** Cloudflare, AWS, Azure, Emerging Threats and Sophos each publish detection, and each publishes what it does not catch.
- **Hardening is partial, by its authors' own account.** No published config change, container limit or edge rule is called a fix by the people who wrote it.
- **GrapheneOS tried three mitigations, then chose to go offline anyway.** Patched and back within seven hours.
- **The method leaves a signature.** It depends on deliberately forcing PHP past its own memory limit, which is loud, not silent.

## What actually happened

On 25 October a researcher using the handle "killa" (named in press coverage as the UK pentester Jaydip Modhwadia) won a public bounty run at stealmybitcoin.com: break into a server left deliberately unpatched, and the bitcoin on it is yours. He recovered a private key through php2shell and the site posted "Challenge won"; the pot was 0.02511679 BTC, then worth $2,021.22. The win was logged at 15:47 UTC on 25 October (00:47 Japan time on the 26th). His own write-up, a single Python file published on GitHub, is public: it builds the requests itself, checks each step before moving on, and records the exact HTTP bytes from a fresh run, so the claim is checkable, not just asserted.

That matters on its own. Every claim so far had been "we reproduced this in our lab." This is the first I have seen where an independent outsider, against a target they did not build, with no special access, got to command execution and published enough that others can check the account. It is also, importantly, a game with a consenting target: the server was built to fall, and the "victim" offered the prize. The real-world count of named organisations compromised through php2shell is still zero, as the newsroom's own [reader-question pieces](https://newsroom.sgit.ai/articles/php-daily-2026-10-26.html) on the PHP story site have covered. This article is about a narrower question: now that it has been done once, in public, how hard was it, could it have been caught, and can you protect a server you cannot yet patch?

## The real timeline is three hours, not nineteen

The headline number, repeated across the coverage, is "stolen after 19.28 hours": the site's own elapsed-time counter since the challenge launched. That number answers how long the page sat up, not how hard the exploit was, and it is worth separating the two.

The target launched at 08:21 UTC on 21 October carrying **no page that executed PHP at all**. For most of the following day and a half, there was nothing php2shell could reach, whatever anyone tried. One report puts it plainly: after more than 17 hours, nobody had solved it, because "the original server did not expose any page that executed PHP programs." The operator added a PHP-executing page at around 22:00 Japan time on 25 October. Killa solved it roughly three hours after that, at 00:47 JST on 26 October.

Three hours, against a target that was actually reachable, by one specialist, working from a published method, is the number that answers your question. Nineteen hours is mostly the story of a target that could not yet be attacked.

## How hard was it, really

The published write-up is explicit about its own limits, which is unusual and useful. A few things it says about itself, as the author wrote them:

- **It needs an exact build, not just a version number.** The method is calibrated against one specific PHP image and worker model. A different build that reports the identical version string is not a safe substitute, and the author's own tooling checks a fingerprint before it will proceed, specifically to reject a mismatch rather than fail confusingly later.
- **It is a race.** Run ten times against the author's own lab, with nothing else happening and no retries, it succeeded about seven times in ten. The rest either produced no result (the stage that needs a specific happen-to-be-reused process did not land) or reached the final step without the markers that confirm it worked.
- **It needs few requests, but they must be shaped exactly right.** The author's own count is twenty HTTP requests at most for a full run: one health check, two batches of pipelined requests, and one final request. That small number is itself informative: this is not a brute-force or a scan, it is a short, precise sequence.
- **The original run was against the live, non-lab target**, and the author is candid that the full outgoing request from that specific run was not fully captured at the time; what is published is a reconstruction from the same code, plus the artefacts the original run did leave behind, not a byte-for-byte original capture.

None of that makes the exploit a hoax or a stunt. It makes it what the [correspondent's own reporting on the PHP story site](https://php.oct.2026.newsroom.sgit.ai/articles/steal-my-bitcoin/index.html) already said: real proof the flaw gives an attacker full control of a machine, from a specialist, against a cooperative, purpose-built target, not an off-the-shelf weapon that anyone could point at an arbitrary production server and expect to work.

## What kind of access did it actually get

You asked, reasonably, what "shell" means here. By the author's own account, the final step runs one operating-system command and returns its output over the connection that is already open: in that run, the command printed a fresh marker so the run could be told apart from any other, the output of `id` (confirming which user the PHP process was running as), and a hash of a file on the target, as independent evidence the command genuinely executed where the write-up said it did. That is command execution as the PHP process's own user, demonstrated once per run, not a standing interactive shell and not a reverse connection back out to the attacker. Whether a given production deployment running as a lower-privileged user would hand over anything less useful is a separate, real question the write-up does not answer, because the lab and the challenge were both set up to run as a privileged account.

## Could a firewall have seen it coming

Could a firewall have seen it coming? Cloudflare, AWS WAF, Azure Front Door, Emerging Threats and Sophos each publish detection coverage for php2shell, and each names its own gap: request-only inspection, header amplification under a size cap, a rule disabled by default, signatures a reshaped request can dodge, or no specific rule at all.

You asked, in a LinkedIn comment at the time, whether any web application firewall could see this coming a mile away. The honest answer is: several vendors say they already do, and each says so with a caveat attached, in their own words, not mine.

- **Cloudflare** had rules live from 03:02 UTC on 21 October, nine hours before PHP's own public advisory. It later added inspection of the server's response, not only the request, because request data alone "could not always tell an exploit from ordinary traffic." Cloudflare also reports that attackers changed their payloads to test its defences.
- **AWS WAF** ships two rules in its PHP managed rule group, inspecting the request body, defaulting to Block. AWS's own blog names the gap: many small part headers can expand far more inside PHP's memory than their size on the wire suggests, which can stay under its size-restriction rule, and a rate-based rule "reduces the volume an exploit needs, but it doesn't stop a single successful request."
- **Azure Front Door's** managed rule for this is disabled by default and was still rolling out as of 28 October. A rule that exists but is off protects nobody until someone turns it on.
- **Emerging Threats** published IDS signatures for both CVEs on 22 October. Signature matching, by its nature, can be dodged by a request reshaped just enough to miss the pattern.
- **Sophos's** intrusion-prevention signatures detect exploitation attempts, but by its own advisory its Web Application Firewall product carries no rule specific to these flaws.

So: not "any WAF could see that coming", and not "nothing can see it coming" either. The honest middle is that detection exists, arrived fast in at least one case, and every vendor who published it also published where it falls short. That is close to what [the newsroom's own earlier piece on the PHP story](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html) already said: detection does not look mature yet, and the inconsistency between huge attempt counts and near-silent compromise counts is itself a data gap worth tracking, not a reason to assume either extreme.

## Hardening without patching: what actually holds

Hardening without patching: session.upload_progress=0, memory_limit=-1, blocking multipart requests at the edge, and a container or cgroup memory cap are each described by their own authors as partial. GrapheneOS deployed and tested the first three, decided not to trust them, and took its only PHP service offline instead, patching and returning within about seven hours.

This is the question I most wanted answered: if upgrading breaks things and people are nervous about it, can you harden the environment around PHP, invisibly to the application, and be safe without touching the PHP binary? The published record says: not fully, and the people who wrote these mitigations say so themselves.

- **Turning off session upload progress** (`session.upload_progress.enabled=0`) closes the path tied to one of the two CVEs. PHP's own advisory is explicit that the other flaw uses a separate path this setting does not touch. A PHP core developer put it more bluntly in public: "the only mitigation is patching / upgrading PHP. I sadly know too much."
- **Raising or removing the memory limit** (`memory_limit=-1`) removes one way the flaw gets triggered. PHP's own caveat: an underlying allocation failure further down can still reach the vulnerable code even with the limit raised.
- **Blocking multipart uploads at the edge**, if your application does not need them, closes paths that depend on a file upload. It does not close a path that one of the CVEs can reach through ordinary warning or logging behaviour, which needs no multipart body at all.
- **A container or cgroup memory limit** bounds the blast radius of a worker crashing, ideally configured to kill only the affected process rather than take the whole service down. That is containment, not prevention: it limits the mess, it does not stop the command from running first.

The most useful real-world test of this is [GrapheneOS's own record](https://bsky.app/profile/grapheneos.org/post/3myepsdnhpc2u), which I read directly from its public feed rather than through a summary. At 08:21 UTC on 21 October it took its discussion forum, its only service running PHP, offline, in its own words "due to vulnerability details already being available and proof of concept exploits being developed." Thirty-three minutes later it posted that it had in fact deployed three specific mitigations (upload progress off, multipart blocking, and a set of Zend memory-manager debug flags), tested them, and decided to turn the forum off anyway rather than rely on them. At 15:30 UTC, having patched to PHP 8.5.12, the forum came back up. Total time offline: about seven hours.

That is a team that could plausibly have run any of the published stopgaps, chose to test them, and judged that none of them earned enough trust to keep the service up while waiting for the real fix. I have not found a single public account of someone relying on configuration or edge hardening alone and being confirmed safe against a live, motivated attempt; I have found several of people trying it and still taking the service down.

## What a defender would actually see

Your question about logs and crashes has a general, public answer, without needing the exploit's internals. The published method depends on deliberately forcing PHP past its own configured memory limit, more than once, as one of its steps. That is not a quiet technique: PHP's own fatal-error path for an exhausted memory limit is exactly what you would expect to see, repeated, from the same client, in a short window, alongside a worker process that gets reused in a way that is unusual for ordinary traffic. A defender watching PHP's own error log for repeated memory-exhaustion fatals from one source has a real signal available to them today, independent of any WAF vendor's rule. Whether anyone is actually watching for that pattern, as opposed to the generic access log, is the open question, and it is the same gap the newsroom's earlier piece named: the data on real-world detection is thin, because almost nobody is publishing it.

## What this does not claim

- **This is one bounty, one researcher, one target.** It is strong evidence the flaw is exploitable in the real world by a skilled person; it is not a measurement of how common successful attacks are.
- **No named organisation has reported a real compromise through php2shell**, separately from this voluntary challenge, as of the newsroom's latest check.
- **Vendor detection coverage changes quickly.** What is listed here is current as of the dates given; several vendors were still rolling out or revising rules through late October.
- **I have not independently reproduced any part of the exploit.** What is reported here about its mechanism and limits comes from the author's own published account of his own work.
- **The GrapheneOS timeline is read from the organisation's own public posts,** not from a secondary summary, but it describes one team's one decision, not a general rule for every deployment.

## Where this comes from

My voice memo of 26 October 2026. The challenge site [stealmybitcoin.com](https://stealmybitcoin.com/) and the researcher's own write-up and proof-of-concept, [KillaBoi/StealMyBitcoin-PoC](https://github.com/KillaBoi/StealMyBitcoin-PoC) on GitHub; press coverage of the win from [Cybersecurity News](https://cybersecuritynews.com/php2shell-flaws-exploited/), [Cryptopolitan](https://www.cryptopolitan.com/hacker-wins-bitcoin-php-challenge-19-hours/), [daily.dev](https://daily.dev/posts/uk-pentester-killa-claims-2k-bitcoin-prize-in-php2shell-capture-the-flag-contest-rhnd8wp6d) and [BigGo](https://finance.biggo.com/news/ff3909cf-4557-44f3-8780-68f21e74f6ae); vendor detection posts from [Cloudflare (via PPC Land)](https://ppc.land/cloudflare-blocks-php2shell-exploits-9-hours-before-php-flaws-went-public/) and [Technobezz](https://www.technobezz.com/news/cloudflare-waf-adds-php2shell-protection-across-plans), [AWS](https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/), [Emerging Threats](https://community.emergingthreats.net/t/detection-coverage-php2shell-cve-2026-109618-and-cve-2026-109619/3488), and [Sophos's advisory](https://www.sophos.com/en-us/security-advisories/sophos-sa-20261021-php2shell); a reading of [GrapheneOS's own posts on Bluesky](https://bsky.app/profile/grapheneos.org) from 21 October 2026, taken directly from its public feed; analysis of PHP's own mitigation guidance via [lilting.ch](https://lilting.ch/en/articles/php2shell-official-patch); the CISA Known Exploited Vulnerabilities catalogue, checked directly, which did not list either CVE as of its 23 October snapshot. Related: [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [PHP October 2026, update 4](https://newsroom.sgit.ai/articles/php-daily-2026-10-26.html), [the PHP story site's own piece on the bounty](https://php.oct.2026.newsroom.sgit.ai/articles/steal-my-bitcoin/index.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

News & evidenceAgents & policy[This article as a graph →](graphs.md#what-the-bitcoin-bounty-actually-proves)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 299 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=299)

**Posting this article on LinkedIn?** The cover is [what-the-bitcoin-bounty-actually-proves.jpg](banners/what-the-bitcoin-bounty-actually-proves.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html)*
