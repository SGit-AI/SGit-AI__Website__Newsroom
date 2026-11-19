---
title: Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: We write behaviour policies for agents and, since php2shell, for applications. I think the next step is to write them for every feature. When we hand someone a new feature to test, we usually hand them the whole app; instead we could hand them the feature's behaviour policy, which says what the feature is for and what it does. That policy is the feature's description, and the difference between two versions of it is what changed. It is also what the application enforces, in context, because the same behaviour can be fine in one place and a serious problem in another. Enforced on the client, it cuts the noise that reaches the server; signed and carried with each request, it lets the server, and anyone watching the traffic, see a bug or an attack as a path outside the policy. The reverse is a resource behaviour policy: everything a key, an account or an API lets you do. The gap between the two is the risk, and the application, where features combine, is where new behaviour appears. Agent and user behaviour policies are then the same feature policies plus a workflow; only who runs them differs. Policies become the permission sets for the custom interfaces we build per task. Next, we map them onto our own capabilities.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: behaviour-policies, abp, security, features, testing, signing, agents, article
status: published
---

!shot fbp-tree.webp | images/ | A tree of behaviour policies: resources, features and fixes, the application, and the agents and users who run it. | concept

## In short {#in-short}

- **Test a feature, not an app:** hand the tester the feature's behaviour policy.
- **The policy is the description,** and what changed is the difference between two policies.
- **Context decides** whether a behaviour is fine or a problem; the policy carries the context.
- **Enforce it at every layer.** On the client it cuts the noise; signed on each request, it makes a bug or an attack a path outside the policy.
- **Resources have policies too:** everything a key or an API lets you do. The gap between that and what the feature needs is the risk.
- **Agent and user behaviour policies** are feature policies plus a workflow; only who runs them differs.

## Test a feature, not an app {#feature}

When we ask someone to test something, we usually think in terms of the application: here is the app, the website, the iOS build, go and test it. But what changed was one feature, or one new capability. I think the unit we hand over should be that feature, with its behaviour policy: what it is for, what it does, what it reads and writes, who may use it, and what it must never do.

That policy is also the feature's description. Ask "what does it do?" and the answer is in the policy. Ask "what changed?" and the answer is the difference between this version of the policy and the last. A tester can start from the policy, and a tool can build the environment to test it in: the data, the permissions and the starting state that the policy names.

## Context decides {#context}

The hard part of security, and of every decision about what to enforce, has always been understanding the behaviour: the business logic, what we are trying to do, and the context. The same behaviour can be fine in one place and a serious problem in another. Exporting a customer list is a feature in the CRM and an incident in the public newsletter page.

A behaviour policy written per feature carries that context with it. It is the mandate, in the words we already use for agents and applications ([application behaviour policies](/articles/application-behaviour-policies.html)): reach is what something can do, mandate is what you asked it to do, and the gap between them is where the risk lives.

## Enforce it everywhere {#enforce}

A policy that says what a feature does can be enforced wherever the feature runs, client side included. The usual reply is that client-side checks can always be bypassed, and they can. But they still do something valuable: they cut the noise. If the client only sends what the feature's policy allows, the traffic that reaches the server is the traffic the features meant to send. Everything else stands out.

!shot fbp-request.webp | images/ | A client sends a request with its signed policy; an observer and the server check that the request fits. | process

Now sign the policies, as we are starting to sign everything, commits and code included. A request from the client can carry the policy, or the policies, it is acting under. The server can check the request against them. And someone who does not have the whole context, an observer looking at the traffic, can still look at a request and its policy and say: this does not make sense, this is not supposed to happen here.

That changes what a bug or an attack looks like. Both are a path that was never supposed to exist: a request outside the policy, a step the feature does not have. The pieces of the pipeline that can see the policy can find it.

## The resource side {#resource}

There is a reverse to the feature policy. Take a key that gives access to a service, an OAuth grant to a mailbox, or a model API behind a key. Our cloud sessions now hold keys this way: a key is saved for a host, and the network proxy adds it to requests to that host, so the session never sees the key. That is a good step. But once the request is authorised, the service at the other end can do far more than the one call we wanted.

I would call that a resource behaviour policy: everything the resource lets you do. It is the reach, written from the receiving side. A vulnerability, in these terms, is a way to bypass it, but it still describes behaviour, and still says what can be done.

Put the two side by side and the method is the one we already use. The resource behaviour policy is the reach; the feature behaviour policy is the mandate; the difference between them is the gap. That gap is where the vulnerabilities live. And the application behaviour policy, the features combined, is where some of them only appear: behaviour that no single feature has, that shows up only when two or three are connected.

## Bugs, too {#bugs}

A bug fix is a change of behaviour as well, so it can have a policy too: the path it closes, what it must leave as it was, and what it must not open. Fixes then join the same tree, and "what changed in this release" reads the same way for a feature and for a fix.

## Agents, users and interfaces {#agents}

Seen this way, an agent behaviour policy is a combination of these smaller policies, the features and resources the agent may use, together with the workflow we want it to follow. A user behaviour policy is almost the same thing. The difference is who is executing it, and what drives them.

That also fits where our interfaces are going. We are building more of them per task, per person and per focus, rather than one app for everyone ([a browser for one](/articles/a-browser-for-one.html)). Behaviour policies are what define what each of those interfaces may do, and what must be enforced. In practice the policies become the permission sets, and an interface can be built from the policies it is allowed to carry.

## What comes next {#next}

We should start using this on our own capabilities now. Two examples:

- **The factory's CI changes.** Our agents can now change CI pipelines in the site factory. That deserves a feature behaviour policy (create this repository, make this change, nothing else), signed, and given to the code and the agents that enforce it.
- **Keys injected by host.** Each saved key should be linked to the features that need it, the resource behaviour policy of the service it opens, and the permissions those features actually use.

I am asking the agent that maintains our agent behaviour policies to map where this applies across the team's capabilities. I think there are several more articles in this: one per kind of policy, and one on the gap between a resource and a feature, measured on a real key.

## What this does not claim {#limits}

- **These are proposals,** not a standard or a finished tool; the words follow the behaviour policies published at abp.sgit.ai.
- **Client-side enforcement is not a boundary;** its value here is cutting noise so the rest stands out.
- **Signing policies on requests is not built yet;** the commits of this newsroom's writer are signed as of 19 November 2026.

## Where this comes from {#sources}

My own thinking, dictated on 19 November 2026, building on [application behaviour policies](/articles/application-behaviour-policies.html) (22 October 2026) and the behaviour policies at [abp.sgit.ai](https://abp.sgit.ai/). Related: [approve at altitude](/articles/approve-at-altitude.html), on decisions that may narrow the level above and never widen it, and [a page we never charge](/articles/a-page-we-never-charge.html), a resource's terms checked against a feature before anything was built.
