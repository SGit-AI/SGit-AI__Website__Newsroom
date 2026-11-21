---
title: The SGit Server Factory, a brief: an agent and a pipeline that deploy SG/Send and sgit servers the way the site factory makes websites, a request file in and a live, tested server out, in any AWS region and any account, as an ephemeral Lambda, a Lambda on S3, an EC2 appliance or Fargate, with one bootstrap stack to onboard a new account and no keys anywhere
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: The site factory turned a website into a request file: merge it, and a pipeline makes the repository, the address and the live site. Vaults need the same for their servers. Teams that put sensitive data in sgit vaults want the server in their own account and the region their assessment needs, and the pieces already exist: one image, sg-send-vault, CloudFormation templates for Lambda, Fargate and EC2, and the OIDC pattern from the site factory. This is the brief for the SGit Server Factory, an agent and a pipeline that put those pieces together. A request file names the account, the region, the shape, the storage, how long it should live and who owns it. The pipeline checks, assumes that account's deploy role with no keys, copies the image into that region, deploys, smoke-tests by pushing and cloning a vault, records the result and tears ephemeral servers down when their time is up. Onboarding a new account is one bootstrap stack its owner runs, in CloudFormation or Terraform. GitHub is needed for the factory itself, not for each server. It is one of the last pieces of the puzzle.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, sg-send, aws, lambda, deployment, factory, brief, article
status: published
---

!shot sgf-flow.webp | images/ | The SGit Server Factory: a request in, a tested server out, in any account and region. | concept

## In short {#in-short}

- **A factory for sgit servers,** as the site factory is for websites.
- **A request file in, a live and tested server out,** in any region and any account.
- **Four shapes:** ephemeral Lambda, Lambda on S3, EC2 appliance, Fargate.
- **One bootstrap stack onboards a new account;** no AWS keys anywhere.
- **GitHub for the factory, not for each server.**
- **Built in phases,** our own account and one region first.

## Why a factory {#why}

The [site factory](/articles/the-site-factory-works.html) showed what happens when a manual, painful process becomes a request file: a website went from merge to live in 87 seconds. Vaults need the same for their servers. Teams that want to keep sensitive data in sgit ask first where it lives and who runs the server, and the honest answer can be: you do, in your own account, in your region ([deploy sgit from CI](/articles/deploy-sgit-from-ci.html)). The server stores ciphertext it cannot read; running your own changes where the ciphertext is, not who can read it.

Everything needed is already written. The SG/Send server is one image, `sg-send-vault`, configured by environment variables. Its repository has CloudFormation templates for a Lambda with a function URL, an EC2 appliance with its own TLS, and Fargate behind a load balancer, plus a bootstrap template for the OIDC role ([SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send), `deploy/aws/`). And the site factory already solved running real changes to AWS from CI without keys. What is missing is the factory that joins them, so that deploying a server is as easy as asking for a site.

## The name {#name}

I would call it the **SGit Server Factory**: it makes servers, the way the Site Factory makes sites, and the name says so. "Vault factory" would suggest it makes vaults, which it does not, and `sgit-deploy` is better kept for the GitHub Action inside it. Its agent would be `factory.server`, under its own behaviour policy.

## The request {#request}

A request is a folder, `requests/<date>__<label>/`, with one file, `server.json`, reviewed and merged like a site request:

```json
{
  "label": "vault-eu-west-2-demo",
  "account": "acme-prod",
  "region": "eu-west-2",
  "shape": "lambda",
  "storage": "s3",
  "ttl_hours": null,
  "domain": null,
  "owner": "the owner's public key, for the access token"
}
```

The account is a name from the factory's accounts list, not a number typed into a request. The access token is never in the request, the repository or the stack: the factory makes it, seals it to the owner's public key and delivers it the way a site key is delivered.

## Four shapes {#shapes}

- **Ephemeral.** A Lambda with `memory` storage and a time to live, for agents, demos, a hackathon or a test: nothing persisted, nothing to clean up but the stack, which the factory deletes when the time is up.
- **Lambda on S3.** The default: pay per request, scales to zero, ciphertext in a bucket named after the account and region, kept on purpose when the stack is deleted.
- **EC2 appliance.** One instance with its own domain and automatic TLS, disk storage, snapshotted on delete.
- **Fargate.** Long-running and several replicas, in its own VPC, removed completely on delete.

Same image, same access token, same smoke test, whichever shape ([ephemeral town planner services](/articles/ephemeral-town-planner-services.html)).

## The pipeline {#pipeline}

1. **Validate** the request against a schema and the accounts list.
2. **Check, changing nothing:** assume that account's deploy role through OpenID Connect, print who it is, list the `sg-send-*` stacks.
3. **Copy the image** into that region's ECR, because Lambda needs it in the same account and region.
4. **Deploy** the stack for the shape, with the token as a parameter from the run, not stored.
5. **Prove it:** health returns ok, then push and clone a small vault through the new server.
6. **Record** a `status.json` in the request folder: the URL, the shape, the stack, the health result, the expiry. No secrets.
7. **Tear down** on expiry, or on a teardown request, and assert the account is clean.

Every job that changes anything runs in a protected `deploy` environment with a person's approval, as in the site factory.

## Any account {#accounts}

Onboarding a new account should be one step its owner takes once, and then the factory can deploy there:

- **A bootstrap stack,** run by the account owner: the GitHub OIDC provider, and a deploy role whose trust names the factory's repository and its `deploy` environment exactly, with a policy scoped to `sg-send-*` stacks, their ECR repository and their bucket. It starts from the existing `github-oidc-role.cfn.yml`, narrowed.
- **For an organisation,** the same template as a CloudFormation StackSet, so new accounts get it automatically.
- **For teams that use Terraform,** the same in a small module, so it fits how they already manage accounts.
- **Then one line in the factory's `accounts.json`:** a name, the account id, the role ARN and the allowed regions. No keys anywhere.

Removing an account is deleting that stack: the factory can no longer reach it.

## Any region {#regions}

Everything in the templates derives from the account and the region, so a new region is a request, not a project. The image is copied into that region's ECR on first use. One caveat stays: a CloudFront certificate for a custom domain on Lambda must be in `us-east-1`; it holds a certificate, not data.

## Does it need GitHub? {#github}

The factory does: it is a repository, its requests are reviewed as pull requests, its pipeline runs in GitHub Actions, and GitHub is what AWS trusts through OIDC. Each server does not: there is no repository per server, only a request folder and its status. A customer who wants their own pipeline instead gets the `sgit-deploy` Action and a skill, and runs the same steps in their own repository.

## The phases {#phases}

1. **Our account, one region, Lambda on S3:** the full cycle green, deploy to teardown.
2. **Ephemeral servers** with a time to live and automatic teardown.
3. **Any region,** with the image copied on first use.
4. **A second account,** onboarded with the bootstrap stack, as the test of the whole idea.
5. **Customers' accounts,** StackSets and the Terraform module.
6. **The Action and the skill,** for teams that run it themselves.

## The brief for the agent {#prompt}

```
You are factory.server, the agent of the SGit Server Factory.
Goal: a request file merged in requests/<date>__<label>/server.json
becomes a live, smoke-tested SG/Send and sgit server in the named
account and region, recorded in status.json, and torn down on expiry.
Read first: deploy/aws/ and deploy-full-cycle.yml in
SGraph-AI__App__Send; docs/SETUP.md and docs/aws-oidc.md in the
AgentiCCells site factory; the newsroom articles "Deploy sgit from CI"
and "The site factory works".
Rules: no AWS keys, OIDC only; every changing job in the protected
deploy environment; the access token never written anywhere, only
sealed to the owner; least privilege, scoped to sg-send-* stacks;
check before deploy; prove with a vault push and clone; never delete
an S3 bucket without a person's word.
Start with phase 1 in our own account, eu-west-2, Lambda on S3, and
report after each step.
```

## What this does not claim {#limits}

- **It is a brief;** nothing here has been built yet.
- **The templates are beta,** with live-account validation still in progress.
- **The request format and the account list are proposals,** to be settled in phase 1.

## Where this comes from {#sources}

My brief in writer-10's session on 21 November 2026; the SGraph-AI__App__Send repository's `deploy/aws/` README and templates, read that day; and earlier articles. Related: [deploy sgit from CI](/articles/deploy-sgit-from-ci.html), [the site factory works](/articles/the-site-factory-works.html), [CI behaviour policies](/articles/ci-behaviour-policies.html), [from SG/Send to sgit](/articles/from-send-to-sgit.html), [ephemeral town planner services](/articles/ephemeral-town-planner-services.html).
