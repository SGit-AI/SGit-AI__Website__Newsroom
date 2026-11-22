# Memo 03, 22 November 2026: the deploy, the private lists, and the next two articles

Dinis's words to newsroom.d (writer-11), dictated, about 11:58 UTC on 22 November 2026, after the release of v0.14.204 failed to deploy (GitHub Pages: "No artifacts named github-pages"):

> Okay, so yes, can you write a simple commit to see if you can trigger and block it? Can you check with the maestro where that list came from originally? Because the what's it called? That should be on a public website, so you shouldn't have to do it here. And then, yes, write the whole laxity article next. The next article I'd like you to write is an interesting article that if you take a look at the work we've been doing now with the, again, check the main to explain to you in terms of delegating authority and the way the architecture we are doing, which is really cool, based on PKI, based on my key, and based on introducing a decisions agent, which is the one that's going to have access. And then when we then use it to extend it to the idea of delegated authority, and then we extend the idea of power of attorney, and then we extend the idea of lawyers, or agent that should also be here, and also the idea that that agent eventually should be integrated with a lawyer, either a freelancer or a company. [...] only humans can have accountability, and companies have accountability, and that's what you pay for also [...] I now can scale the consumption of lawyers [...] I would like to, for example, know how much would it cost to have this signed and certificated by a company, and then signed a review by a human in there, and actually which human in there, and which company, and which flow, and then I should be able to pay for it, right? So if you think about it, that would be a great way to scale law firms and professional services.

(The full message is in newsroom.d's session; "whole laxity" is the dictation of "holacracy", and "the main" of "the maestro".)

## What was done

- **The deploy:** by 11:59 UTC it had already happened. @newsroom.accountant's push at 07:43 UTC (v0.14.205) deployed everything on dev, and both articles and their six images return 200. No trigger commit was needed; this commit records the memo and claims.
- **The private lists:** maestro.d asked at 12:0x UTC where the leak scan's lists came from and whether a public copy exists.
- **The architecture for the second article:** maestro.d asked for the repositories, files and decisions to read.
- **Claims** in CLAIMS.md: the holacracy article (holacracy.d's brief, relayed by maestro.d) and the delegated-authority article.
