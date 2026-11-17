---
title: Deploy sgit in your own environment, from a CI pipeline: one Docker image, ciphertext in your own S3 bucket in the region you choose, an access token only you hold, and the pipeline pattern we learned building the AgentiCCells site factory, a protected environment, AWS through OpenID Connect with no keys, a role that trusts one repository and one environment, check workflows before anything real, and a full cycle that deploys, tests and tears down
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: More teams now want to use sgit vaults for sensitive data, health data included, and the first real question they ask is where the data lives and who runs the server. The answer can be: you do, in your own cloud account, in the region your data protection assessment needs. sgit's server is one Docker image, configured only by environment variables, that stores ciphertext it cannot read, in memory, on a disk or in Amazon S3; on AWS the bucket is named after your account and your region, and a single access token, kept in your CI's secret store, gates every route. The keys never reach it. CloudFormation templates for Lambda, ECS Fargate and EC2 are written, in beta, in a public repository. What makes it repeatable is the pipeline, and that is what we learned the hard way building the AgentiCCells site factory: deploy jobs that run only in a protected GitHub environment with a person's approval; AWS reached through OpenID Connect, so no AWS key is stored anywhere; a role that trusts one repository and one environment, not any branch; permissions limited to its own stacks; check workflows that prove the setup before anything real runs; and a full cycle that deploys, smoke-tests and destroys. There are a lot of moving parts, and the pain is worth it, because once it works the whole thing is automated. Here is how it works, step by step, a proposal to package it as a GitHub Action and a skill, and a prompt for your own Claude. I am deploying it in my own account first, to prove the steps.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, vaults, deployment, aws, github-actions, oidc, ci, healthcare, article
status: published
---

!shot dep-shape.webp | images/ | Your own sgit server: your devices encrypt, your account runs one image, your region holds the ciphertext. | concept

## In short {#in-short}

- **Run your own sgit server,** in your own cloud account and the region you need.
- **One Docker image,** configured by environment variables; ciphertext in S3; one access token gates every route.
- **Keys never reach it:** the operator sees opaque ids, sizes and timing, never content.
- **Deploy it from CI, not by hand,** with the pattern we learned on the site factory.
- **No AWS keys anywhere:** OpenID Connect, a narrow role, a protected environment, a person's approval.
- **Check first, then deploy, smoke-test and record;** and be able to tear it all down.
- **Next: a GitHub Action and a skill,** so this becomes one step.

## Why your own environment {#why}

When a team starts to put sensitive data into vaults, health data for example, the first serious questions are not about cryptography. They are: where is the data stored, in which region, who runs the server, and what happens when we want it gone? For a data protection impact assessment, "our own AWS account, in eu-west-2, run by our own pipeline" is a much easier answer than "a service someone else runs".

With sgit it is also an honest answer. Every file, file name and commit message is encrypted on the user's device with AES-256-GCM, from keys derived on the device; the server stores ciphertext and hashes only, and can see which vault ids exist, their sizes and the timing, never contents and never keys ([what sgit does that git does not](/articles/what-sgit-does-that-git-does-not.html)). Running your own server changes who holds the ciphertext and where. It does not change who can read it: only the key holders.

## What you deploy {#what}

The SG/Send server, which sgit pushes to, is open source (Apache 2.0) and ships as one image, `diniscruz/sg-send-vault` on Docker Hub, for amd64 and arm64. It serves the API and the vault web UI from one process, and its whole configuration is environment variables:

- **`SEND__STORAGE_MODE`:** `memory` (nothing persisted, ideal for agents and air-gapped runs), `disk` (a mounted volume), or `s3` (durable, for production).
- **`SEND__S3_BUCKET`:** by default `{account}--sgraph-send-transfers--{region}`, so two regions never collide and the region is in the name.
- **`SGRAPH_SEND__ACCESS_TOKEN`:** when set, every route, reads included, needs it. It is given at deploy time and stored nowhere on the server side; keep it in your CI's secret store, a password manager, or a vault.
- **TLS and port settings,** for running the container directly.

The fastest way to see it is one command on a laptop, `docker run --rm -p 8080:8080 diniscruz/sg-send-vault:latest`, then open `http://localhost:8080/`. For production on AWS there are CloudFormation templates, written, lint-clean and in beta, in the [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send) repository under `deploy/aws/`: a Lambda with a function URL (pay per request, scales to zero), ECS Fargate behind a load balancer (its own VPC, so deleting the stack removes everything), and an EC2 appliance. The deployment guides themselves live in an encrypted vault whose read key [sgit.ai/deploy](https://sgit.ai/deploy/) publishes. If you only need people to read a vault, not write to it, a vault can also be published as static files to S3 and CloudFront, with no server at all.

## The pipeline pattern {#pipeline}

!shot dep-pipeline.webp | images/ | The site factory pattern: protected environment, OIDC, narrow trust, least privilege, checks, teardown. | process

The AgentiCCells site factory was the first time we properly sorted out running real changes to GitHub and AWS from CI: a commit becomes a repository, a DNS record in Route 53 and a live site in about a minute ([the site factory works](/articles/the-site-factory-works.html)). It has a lot of moving parts. Each one is there for a reason, and the same seven pieces deploy an sgit server.

1. **A protected environment.** Every job that changes anything runs in a GitHub environment, say `deploy`, that only one branch can use, with you as a required reviewer. Each real run waits for your Approve.
2. **AWS through OpenID Connect, with no keys.** The job asks GitHub for a short-lived identity token and exchanges it for an AWS role for an hour. There is no AWS access key in GitHub, so there is none to leak. The OIDC provider is added once per AWS account.
3. **Trust one repository and one environment.** The role's trust policy names the subject exactly: `repo:<org>@<org id>/<repo>@<repo id>:environment:deploy`, the numeric form GitHub sends, which we read from a check run. The server repository's own bootstrap template trusts `repo:<org>/<repo>:*`, any branch and any workflow; for anything holding real data, narrow it to the environment, as the factory does.
4. **Least privilege.** The factory's role can change CNAME records under one zone and nothing else; the apex and every other record type stay a person's job. The sgit deploy role is scoped to its own `sg-send-*` stacks and what they create. Write the policy as tightly as you can, and keep its JSON in the repository's docs.
5. **Check before anything real.** Two manual workflows in the factory change nothing unless asked: one proves the GitHub App can mint and use its token, one proves the AWS role, and with a write test ticked creates and deletes a test record and confirms that what should be refused is refused. Run them until they say OK. Only then merge the first real request.
6. **Deploy, smoke-test, record.** The deploy job runs CloudFormation with the access token passed as a parameter from the environment's secrets, then checks `GET /api/info/health` returns `{"status":"ok"}`, pushes and clones a small vault through the new server, and writes the result back to the repository, as the factory writes each request's `status.json`.
7. **Tear down cleanly.** The server repository's `Deploy Full Cycle` workflow builds the image, pushes it to your ECR, deploys a stack, runs the smoke suite against the live URL, destroys the stack and asserts the account is clean. A green run is the proof the account is set up. For production, keep the S3 bucket: the Lambda stack retains it on delete, on purpose.

## Step by step, on AWS {#steps}

For a team deploying into its own account and region, the order is:

1. **Choose the region** your assessment needs, for example `eu-west-2` (London). Everything derives from account and region; nothing in the templates is region-specific. One caveat: a CloudFront certificate for a custom domain must be in `us-east-1`, which holds a certificate, not data.
2. **Add the GitHub OIDC provider** in IAM, once per account (`https://token.actions.githubusercontent.com`, audience `sts.amazonaws.com`).
3. **Create the deploy role** from `deploy/aws/github-oidc-role.cfn.yml`, then tighten its trust to your repository's `deploy` environment.
4. **In your repository,** create the `deploy` environment (one branch, you as reviewer); add the role's ARN and the region as environment variables, and the access token (`openssl rand -hex 32`) as an environment secret.
5. **Put the image in your region's ECR** (Lambda needs it there), with the four commands in the new-region runbook.
6. **Run a check workflow:** assume the role, print who you are, list the stacks; change nothing.
7. **Deploy** with `aws cloudformation deploy` and `StorageMode=s3`, then the smoke test, then write the status back.
8. **Point sgit at it:** `sgit clone <vault-key> --base-url <your URL> --token <access token>`.

A job in that pipeline looks like this sketch, to be validated in a real account before anyone relies on it:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: deploy            # one branch, a required reviewer
    permissions:
      id-token: write              # for OpenID Connect
      contents: write              # to record the result
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ vars.SGIT_DEPLOY_ROLE_ARN }}
          aws-region: ${{ vars.SGIT_REGION }}
      - run: |
          aws cloudformation deploy \
            --template-file deploy/aws/lambda.cfn.yml \
            --stack-name sg-send-lambda --capabilities CAPABILITY_IAM \
            --parameter-overrides ImageUri=${{ vars.SGIT_IMAGE_URI }} \
              StorageMode=s3 AccessToken=${{ secrets.SGIT_ACCESS_TOKEN }}
      - run: ./scripts/smoke.sh    # health, then a vault push and clone
```

## Package it: an Action and a skill {#package}

Once it works, nobody should have to repeat it by hand. Two packages would make it one step:

- **A GitHub Action, `sgit-deploy`,** with inputs for the target (lambda, fargate, ec2, static), the region, the storage mode, the role ARN and the access token secret, and outputs for the URL and the health result. It would wrap the templates, the smoke test and the status record, and refuse to run outside a protected environment.
- **A skill for agents,** in the same shape as sgit's existing skills: how to set up the role and the environment, the checks to run, and the traps already hit, so a team's own Claude can do the setup with them, step by step.

The factory already shows the third option: a request committed to a repository, and the pipeline does the rest.

## The prompt for your Claude {#prompt}

```
Help me deploy my own sgit (SG/Send) server into my AWS account, in
region [region], from GitHub Actions, for [what the vaults will hold].
Read first:
- https://sgit.ai/deploy/ (and the deploy guides vault it links)
- https://github.com/the-cyber-boardroom/SGraph-AI__App__Send:
  deploy/aws/*.cfn.yml and .github/workflows/deploy-full-cycle.yml
- https://github.com/AgentiCCells/AgentiCCells__Site__Factory:
  docs/SETUP.md and docs/aws-oidc.md (the pipeline pattern)
Then, one step at a time, waiting for me after each:
1. the GitHub environment and its protection;
2. the OIDC provider and a deploy role whose trust names my repository
   and environment exactly, with a least-privilege policy;
3. a check workflow that changes nothing;
4. a deploy workflow with StorageMode=s3, a smoke test and a status file;
5. how to point sgit at the new server.
Never ask me to paste a secret into this conversation: tell me where
to set it.
```

## What this does not claim {#limits}

- **The AWS templates are beta:** written and lint-clean, with live-account validation still in progress; Docker is the path that works exactly as documented today.
- **The job above is a sketch;** I am deploying it in my own account first, and will publish what changes.
- **Self-hosting moves the ciphertext, not the trust model:** losing a vault key still loses that vault.
- **Other clouds:** the image runs anywhere with a container runtime; durable storage outside AWS is not yet documented.

## Where this comes from {#sources}

The SG/Send deployment guides (the vault published at [sgit.ai/deploy](https://sgit.ai/deploy/), read with its public read key on 17 November 2026: configuration, storage modes, security model, the Docker, Lambda, Fargate and static-hosting guides, and the new-account and new-region runbooks); the repository [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send) (`deploy/aws/` and `deploy-full-cycle.yml`); the repository AgentiCCells__Site__Factory (`docs/SETUP.md`, `docs/aws-oidc.md`, its workflows); [sgit.ai](https://sgit.ai/) and the sgit-ai CLI. Earlier on this site: [the site factory works](/articles/the-site-factory-works.html), [CI behaviour policies](/articles/ci-behaviour-policies.html), [what sgit does that git does not](/articles/what-sgit-does-that-git-does-not.html).
