---
title: sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job
date: 2026-10-14
author: Dinis Cruz
author_url: about/index.html
summary: Getting data in and out of a CI pipeline is harder than it should be. GitHub Actions has artifacts, kept 90 days by default and deleted with their run; caches, 10 GB per repository and evicted after a week unused; and job outputs, at most 1 MB per job. Each is fine for its job, and none is a versioned, encrypted record that a person, an auditor or another pipeline can read from outside GitHub. This article maps how sgit vaults fill that gap, and every pattern in it was run for the article against a local vault server. A job pushes what it produced to a vault, and anything with the read key can clone it from anywhere, with history. Jobs pass data to each other through the same vault, each cloning only the folders it needs with --path, which is a large saving in time and in what lands on the runner, though it is a speed setting rather than a boundary. The boundaries are the keys: a read key clones and cannot commit; an append token, one per test shard, adds to its own write-only inbox and reads nothing; and each job can have its own key pair, so a deploy configuration encrypted to the deploy job fails to decrypt anywhere else, and a signed manifest fails verification once it is changed. Even done a little loosely, that turns wiring mistakes into loud failures. The keys come from secrets on stdin, and only the ciphertext half of a vault ever leaves the runner. And when you would rather not depend on a hosted server, the vault server runs as a sidecar whose storage folder holds only ciphertext: archive it into the Actions cache, an artifact or a git branch, and the next run restores it with its full history.
version: v0.12.34
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, ci, github-actions, pipelines, vaults, append-lanes, pki, secrets, scoped-clone, supply-chain, artifacts, article
status: published
---

!shot vc-pipeline.webp | images/ | A pipeline whose stages talk through a vault. Each job clones only the folders it needs, with only the key it needs: build writes with the vault key, test shards append to write-only inboxes, the summary reads the lane, release and deploy read with the read key and their own key pairs, and anyone outside GitHub can clone the results with a read key. What leaves a runner is ciphertext. | architecture

## In short {#in-short}

- **CI data has three exits, none of them a record.** Artifacts, caches and job outputs each have limits on size, life and who can reach them, and none is versioned or readable from outside GitHub.
- **A vault is data in and out.** A job pushes its outputs; a person or another pipeline clones them with a read key, with history, from anywhere.
- **Jobs talk through the vault.** Each clones only its folders with `--path`; the release job in the test never downloaded the build archive it did not need.
- **`--path` is speed, keys are boundaries.** A scoped clone limits what lands on the runner. What a job can do is set by its key: a read-key clone refused to commit.
- **Append lanes for shards.** One token per test shard, each adding to its own inbox, none able to read; a summary job lists them with a separate key.
- **A key pair per job.** A file encrypted to the deploy job failed to decrypt in the test job; a changed manifest failed its signature check.
- **Keys from secrets, on stdin.** `echo "$SGIT_VAULT_KEY" | sgit clone - …`. Only `.sg_vault/bare`, the ciphertext, is ever cached or uploaded.
- **No hosted server needed.** The vault server runs as a sidecar; its storage, ciphertext only, goes into the cache or a branch and comes back next run with its history.

## Why CI data is awkward {#why}

Every pipeline produces things somebody wants later: the build, its manifest and bill of materials, test reports, coverage, timings, the signed release. GitHub Actions gives you three ways to keep them, and each is right for something narrower than that.

[Artifacts](https://github.com/actions/upload-artifact) "are retained for 90 days by default", are immutable since version 4, and are meant to "share that data with another job in the same workflow"; delete the run and they go with it. The [dependency cache](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) is 10 GB per repository, and "GitHub will remove any cache entries that have not been accessed in over 7 days"; runs "cannot restore caches created for child branches or sibling branches". [Job outputs](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) "can be a maximum of 1 MB per job", and "outputs containing secrets are redacted on the runner". All three live inside GitHub, readable by whoever can read the repository's runs, and none is a versioned history you can hand to someone outside it.

What I would like from a pipeline is closer to what this site wants from its agents, in [Encrypted memory for isolated agents](/articles/encrypted-memory-for-isolated-agents.html): compute that is gone after the task, and a memory that is not. A CI job is exactly that kind of compute.

## What was tested {#tested}

Everything below was run for this article with sgit 0.21.0 against a local vault server, version 0.34.0 of the same package the `diniscruz/sg-send-vault` image runs, with disk storage and an access token. Each "job" ran in its own empty home directory, so nothing carried over except what went through the vault. The workflow file at the end is a sketch built from those commands; it has not been run on GitHub Actions.

## Data in and out {#in-out}

The simplest use is an exit. The build job clones the run's vault, copies its outputs in, commits and pushes:

```
echo "$SGIT_VAULT_KEY" | sgit clone - run --base-url "$SGIT_BASE_URL" --token "$SGIT_TOKEN" --path build
cp dist/* run/build/
cd run && sgit commit "build 1.2.3" && sgit push --token "$SGIT_TOKEN"
```

The `-` makes `sgit clone` read the key from stdin, which keeps it out of the process list and the shell history. In the test, the push went through and a second, empty home cloned the same history back. From then on the outputs are wherever the vault is: a release manager, an auditor or another company's pipeline can clone them with a read key, see every run as a commit, and diff two releases, without a GitHub account and long after the artifact would have expired. The server sees ciphertext; [Encrypted memory for isolated agents](/articles/encrypted-memory-for-isolated-agents.html) searched a server's storage for the plaintext and found none, and so did this test.

Data comes in the same way. A configuration, a dataset or a set of fixtures that a pipeline needs, maintained by people who should not have write access to the repository, can live in a vault they own; the pipeline clones it with a read key.

## Between jobs, and only what each job needs {#between}

Inside a run, the vault is how jobs hand work to each other. In the test, the build job pushed `build/`, holding a 200 KB archive and a manifest. The test job cloned only `build/` and `test/`:

```
echo "$SGIT_VAULT_KEY" | sgit clone - run --base-url "$SGIT_BASE_URL" --token "$SGIT_TOKEN" --path build --path test
```

It wrote its report into `test/`, committed and pushed. The release job cloned with the read key, scoped to `test/`, and on its disk there was one file, the report: the archive was never downloaded. When it tried to commit, sgit answered "This vault was cloned read-only. To write, re-clone with the full vault key."

That is the speed and the shape of the thing. `--path` holds only the named folders; "other folders are carried by id and never downloaded; commits and pulls touch only the held folders". A vault that accumulates every run's outputs stays cheap to use, because each job only pays for its own folders. It also keeps data off runners that do not need it, which is worth a lot on shared or third-party runners.

But a scoped clone is not a wall. A job holding the full vault key can widen its clone with `sgit fetch <folder>`; [Encrypted memory for isolated agents](/articles/encrypted-memory-for-isolated-agents.html) says it plainly: "A scoped clone is a speed setting, not a boundary." The boundaries are the keys.

## The keys are the boundaries {#keys}

!shot vc-keys.webp | images/ | Which job holds which key. Build and the summary hold the vault key, release, deploy and outside readers the read key, each test shard one append token, the summary the lane's enum key, and the jobs that sign or decrypt their own key pair. The server access token opens a private server's door for everyone; it is not a vault permission. | comparison

sgit gives a pipeline four kinds of key, and the useful design question is which job holds which.

- **The vault key** reads and writes. In sgit's code the read key and the write key are derived separately from the vault's passphrase, and a clone made with a read key holds no write key: that is why the release job's commit was refused.
- **The read key** clones and reads, nothing else. It is what release, deploy and anyone outside the pipeline should hold.
- **An append token** adds to one inbox of the vault's append lane and can read nothing, not even what it wrote.
- **A job's own key pair** encrypts to and signs as that job.

And one thing that is not a vault permission at all: the server's access token. On a private server it is the door, and every route needs it; in the test, an append without it was refused with 401. Every job that reaches the server holds it, whatever its keys allow inside.

This is the same move as [Hope or enforcement](/articles/hope-or-enforcement.html) and [Attacks rewritten as mandates](/articles/attacks-rewritten-as-mandates.html): a pipeline where every job can do anything, and the YAML promises it will not, is a mandate kept by hope. A pipeline where each job's key only allows what its step is for has written the mandate down as a barrier.

## Append lanes for shards {#lanes}

Test matrices are where CI data is most awkward: a dozen shards each produce a report, and something has to gather them. An append lane does it without giving the shards anything they could misuse. The lane is configured once with the write key: a list of hashes of append tokens, one per shard, and the hash of a separate key that can list and fetch. Each shard then posts its result with its own token.

In the test, three shards each appended one entry with their token. An unknown token was refused with 403. Listing a shard's inbox needed the enumeration key, and a wrong one was refused with 403. Reconfiguring the lane with a wrong write key was refused with 403. The server caps an entry at 5 MB and an inbox at 1,000 waiting entries, and lists at most 200 at a time.

Two details matter in practice. The server stores the payload as it is sent, so a shard should encrypt its result to the summary job's public key first; that is how this newsroom's reading meter shares a summary, encrypting it in the browser to the recipient's published key before it appends, as [Sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html) describes. And because a token can only add to its own inbox, a compromised shard can at worst add noise to one inbox; it cannot read the other shards' results, or anything else in the vault.

## A key pair for every job {#pki}

The more advanced pattern gives each job an identity. `sgit pki keygen` makes an encryption and a signing key pair, the private keys protected by a passphrase; `sgit pki export` gives the public half as a small JSON file that can sit in the vault's `keys/` folder for every job to import.

In the test, three jobs each made a pair. The build job encrypted a deploy configuration to the deploy job's key and signed it: the result held none of the plaintext. The test job tried to decrypt it and got "Decryption failed". The deploy job decrypted it and, once it had imported the build job's public key, reported the signature as verified, signer `stage:build`. The build job also signed its manifest; the deploy job verified it as valid, and after one line was appended to the manifest the same check returned "Signature INVALID".

To give a job its identity, the key folder, about 5 KB once packed, and its passphrase go into that job's secrets. That is not perfect key management, and it does not need to be to pay for itself. Even if every job's keys were reachable from the same environment, a pipeline wired this way fails loudly when a step reads something that was not meant for it, instead of quietly working until the day it leaks. A configuration that only the deploy job can decrypt is a bug that cannot ship to the wrong place.

## No hosted server {#no-server}

!shot vc-noserver.webp | images/ | No hosted server. The vault server runs as a container inside the job with its storage in a folder; the folder holds only ciphertext, so it can be saved to the Actions cache, an artifact, a release asset or a git branch, and the next run restores it and clones with its full history. Reading needs no server at all; pushing needs the server's API, which the sidecar provides. | architecture

Not every team wants its pipeline to depend on a vault server somewhere else. It does not have to.

The vault server is one container, and in a job it can run beside the steps, on localhost, with its storage in a folder. In the test, the server's storage after the build and test jobs was 388 KB in 19 files, and a search of it found none of the file names or contents. Archived, it was 208 KB. Restored into a new folder, under a new server, a clone from a fresh home came back with all three commits, the build and the test report. So the folder can live wherever a CI system keeps bytes: the Actions cache, an artifact, a release asset, or a branch of the repository, which keeps it indefinitely and as ciphertext.

Reading does not even need the sidecar. `sgit clone --transport local` reads a vault from a folder, `--transport static` from any plain web host, and `sgit vault attach` binds a key from a secret to a bare checkout, such as the `.sg_vault/bare` folder of a vault committed to a repository. In the test, a copy of only the bare folder, with the key attached in a fresh home, read the vault's history without any network. Writing is different: pushing needs the server's API, and sgit refuses to push to a folder or a static host, with an error that says so. The sidecar is how a pipeline keeps writes without a hosted server.

Two cautions belong here. The sidecar is per job, so it suits a single job or one run after another; jobs running in parallel need a server they can all reach. And when archiving, archive the server's storage, or a vault's `.sg_vault/bare`, never `.sg_vault/local`: that folder holds the vault key in clear, the server token and the clone's own private key. In the test it was the only place the passphrase was found.

## A workflow sketch {#workflow}

Built from the commands above, not yet run on GitHub Actions. It assumes a server the jobs can reach, its URL in a repository variable and its token, the vault key and the read key in secrets.

```
env:
  SGIT_BASE_URL: ${{ vars.SGIT_BASE_URL }}
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install 'sgit-ai==0.21.0'
      - run: make build                    # writes dist/
      - name: Push the build to the vault
        env:
          SGIT_VAULT_KEY: ${{ secrets.SGIT_VAULT_KEY }}
          SGIT_TOKEN:     ${{ secrets.SGIT_SERVER_TOKEN }}
        run: |
          echo "$SGIT_VAULT_KEY" | sgit clone - run --base-url "$SGIT_BASE_URL" --token "$SGIT_TOKEN" --path build
          mkdir -p run/build && cp dist/* run/build/
          cd run && sgit commit "build ${GITHUB_SHA::7}" && sgit push --token "$SGIT_TOKEN"
  release:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: pip install 'sgit-ai==0.21.0'
      - name: Read the build, read-only
        env:
          SGIT_READ_KEY: ${{ secrets.SGIT_READ_KEY }}
          SGIT_TOKEN:    ${{ secrets.SGIT_SERVER_TOKEN }}
        run: echo "$SGIT_READ_KEY" | sgit clone - run --base-url "$SGIT_BASE_URL" --token "$SGIT_TOKEN" --path build
```

For the sidecar version, restore the storage folder from the cache, start the server with `docker run -d -p 8080:8080 -e SEND__STORAGE_MODE=disk -e SEND__DISK_PATH=/data -e SGRAPH_SEND__ACCESS_TOKEN=… -v "$PWD/vault-store:/data" diniscruz/sg-send-vault:<version>`, run the same steps against `http://localhost:8080`, and save the folder under a new cache key at the end, since caches cannot be changed once written. Secrets can come from GitHub's own store or from any manager that sets an environment variable, such as HashiCorp Vault.

This newsroom already uses parts of this. Its deploy workflow installs sgit 0.21.0 for a round trip through a vault in its tests; the script that reads readers' notes takes its read key "from the environment (NEWSROOM_LANE_KEY) or from stdin with --key -, never from a file in this repository, and it is never printed"; and the wires are drawn from vaults this site can only read, as in [Two agents, one vault](/articles/two-agents-one-vault.html).

## What this does not claim {#limits}

- **Tested locally, not on GitHub Actions.** Every result here is from a local server and separate home directories standing in for runners; the workflow is a sketch.
- **`--path` is not access control.** It limits what is downloaded; the key decides what is allowed.
- **The sidecar does not serve parallel jobs.** Each job's sidecar is its own; parallel jobs need a shared server.
- **Per-job keys in secrets are only as separate as the secrets.** If one job can read another's secrets, the keys help with correctness, not with containment.
- **Append payloads are stored as sent.** Encrypt before appending if the content matters.
- **GitHub's redaction of secrets is "not guaranteed",** in its own words; keeping keys off the command line and out of uploaded folders still matters.

If you are moving CI data through something you would rather not, or you want to try a vault in a pipeline, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The commands were run for this article with sgit 0.21.0 and the vault server package sgraph-ai-app-send 0.34.0, on a local server with disk storage; the append lane's routes and limits are from the server's source. GitHub: [dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching), [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) on outputs and service containers, [using secrets](https://docs.github.com/en/actions/concepts/security/secrets), and [upload-artifact](https://github.com/actions/upload-artifact), all read on 14 October 2026.
