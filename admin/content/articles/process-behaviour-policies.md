---
title: Process behaviour policies: the most locked-down Linux process we could build inside Claude's own cloud container, derived from one traced run, enforced by the kernel, for about a tenth of a second
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: The behaviour policy family has policies for agents, decisions, workflows, skills and applications. This one is for a process. It started with sgit and keys: we want sgit to work with PKI keys rather than holding a vault key, so the vault key has to live somewhere else, in a small process acting as a key service or a network broker. That only helps if sgit's own process cannot reach the key, which led to a bigger question. Inside a cloud container, everything runs as root, which is bad practice and no defence in depth. So what is the most locked-down process Linux lets us build there? We built it, in this newsroom's own Claude Code container, and measured it. A policy is derived from one traced run: every file the process reads, every system call it makes, every host it talks to. Then the kernel enforces it with seven walls: a user that exists for one run, an empty read-only root holding only the listed files, its own namespaces, Landlock, a seccomp allowlist, a network broker that only opens tunnels to the policy's hosts, and limits. A probe that, as root, could read /etc/shadow, the agent's home and the internet could do none of it under the policy. The cost was 92 to 187 milliseconds a run. And the size of the policy is a measure of the software: Hello World in C needs 1 file and 12 system calls; sgit needs 1,025 files and 58.
version: v0.13.68
license: https://creativecommons.org/licenses/by/4.0/
tags: behaviour-policies, linux, least-privilege, sandboxing, sgit, landlock, seccomp, article
status: published
---

!shot px-walls.webp | images/ | Seven walls around one process, set from its policy and enforced by Linux inside this cloud container: an ephemeral user with no capabilities; an empty, read-only root holding only the listed files; its own namespaces; Landlock for paths, exec and TCP ports; a seccomp allowlist of the system calls the traced run made; a network broker that only opens tunnels to the policy's hosts; and cgroup limits. | concept

## In short {#in-short}

- **A new member of the family.** Policies for agents, decisions, workflows, skills and applications; now one for a process.
- **It started with sgit's keys.** If sgit should not hold the vault key, its process must not be able to reach it.
- **In a cloud container, everything runs as root.** So we built the most locked-down process Linux allows there.
- **The policy is derived, not written.** One traced run lists every file, system call and host the process needs.
- **The kernel enforces it.** Seven walls, set from the policy; the policy itself executes nothing.
- **It held.** A probe that could do 13 of 14 things as root could do none of them under the policy.
- **It is cheap.** 92 to 187 milliseconds a run, measured.
- **The policy's size measures the software.** 1 file and 12 system calls for Hello World; 1,025 files and 58 for sgit.

## Why a process {#why}

We already have [agent behaviour policies](https://newsroom.sgit.ai/articles/a-policy-beside-the-prompt.html), [decision and workflow policies](https://newsroom.sgit.ai/articles/three-policies-for-an-agent.html), [skill behaviour policies](https://newsroom.sgit.ai/articles/skill-behaviour-policy.html) and, since php2shell, [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html). I want to add one more, for the thing everything else eventually runs as: a process. On Windows and on Linux, it is all processes.

This came from a practical question. We want to run sgit with PKI keys rather than vault keys. The logic is that we do not want to give the vault key to the sgit process, but it has to live somewhere. So the idea is a small separate process, an agent of its own, acting like a key management service, or a network broker that adds what is needed to a request on the way out. [The key is not the risk](https://newsroom.sgit.ai/articles/the-key-is-not-the-risk.html) made the general point: credential injection is a good pattern, and the first question is still what the process can do. Because if we do this, we need to make sure the sgit process itself cannot reach the key, the broker's memory or its files.

And that is where it gets uncomfortable. Inside a cloud container like the one this newsroom's agent runs in, processes run as root. Every process can read every file, signal every other process and talk to anything on the network. That is bad practice, and it is not defence in depth. So why not give sgit a process of its own, and while we are at it, lock it down properly: define everything it may do, and have the operating system refuse everything else?

## The question, made concrete {#question}

What is the most locked-down process we can create today, with whatever this environment offers? If a process prints "Hello World", or runs a Python program that needs a few files, it should not be able to do anything else. It should have, in effect, an immutable file system. It should run as a user that exists only for that run, with access to a couple of directories, a couple of hosts, and nothing else Linux provides: no other executables, no other processes, no way to look around.

And the policy should list every file the process needs, every dependency, all the way down. This is the blast radius idea, the [footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html) of an agent, applied to a process: reverse-engineer what it actually needs, and make that the limit.

## What the container offers {#container}

This newsroom's agent runs in a Claude Code cloud container: Ubuntu 24.04 in a Firecracker microVM, Linux 6.18, as root with nearly every capability. That microVM is already a wall around the whole container. What we wanted was walls inside it, around one process. We checked what was available, and it is a lot:

- **Landlock, at ABI 7.** The kernel's own sandbox for a process, which needs no privileges: read, write and execute per path, TCP connect per port, and no signals to processes outside it.
- **seccomp,** for an allowlist of system calls.
- **Namespaces:** mount, process, IPC, hostname, cgroup and network.
- **cgroups** (version 1 here), for process and memory limits.
- **iptables,** which can match on the user that owns a connection.
- **useradd, chroot, strace and a C compiler** with static libraries.

Nothing extra needed installing.

## Derive the policy from a run {#derive}

The policy is not written by hand. A script runs the command once under `strace -f` and reads what it did: every file it opened successfully, every directory it listed, every program it executed, every system call it made, every connection it opened. It adds what the trace cannot see, the ELF interpreter the kernel loads for each binary and the interpreter named on a script's first line, and writes it all down as a policy.

The smallest one, for Hello World in C, reads in full: one file, the program itself; no directories; no devices; no network; and twelve system calls, from `arch_prctl` to `write`. Nothing else. The policy also records the user (ephemeral, no groups, no capabilities, no new privileges), what the process may see of other processes (nothing), and its limits (64 processes, 512 MB, two minutes).

## Enforce it with seven walls {#enforce}

A second script takes the policy and builds the process's world, then a small static launcher applies the last walls from inside it and starts the program:

1. **An ephemeral user.** `useradd` makes one for this run, and it is removed afterwards. The launcher drops to it, with no groups and no capabilities, and sets no_new_privs, so nothing it runs can gain privileges.
2. **An empty, read-only root.** A fresh, tiny filesystem in which each file the policy lists is bind-mounted read-only at its own path. Then the whole root is made read-only, and the process is put inside it. For Hello World, the root holds one file. `/etc/shadow`, `/root` and `/bin/sh` are not refused: they do not exist.
3. **Its own namespaces.** Mount, process, IPC, hostname and cgroup. Inside, the process sees one process: itself. If the policy has no network, it also gets a network namespace with nothing in it.
4. **Landlock.** Read access to the listed files, execute access only to the listed programs, write access only to the listed folders, TCP connect only to the broker's port, and no signals to anything outside.
5. **A seccomp allowlist.** Only the system calls the traced run made. Everything else returns "not permitted".
6. **A network broker.** When the policy names hosts, the process's only way out is a small proxy, run outside the sandbox, that opens a tunnel to those hosts and refuses everything else, plus an iptables rule that rejects any other connection from that one user.
7. **Limits.** A cgroup caps the number of processes and the memory; a timer caps the run.

The broker is the shape of the key service. In this test it only decides where a process may go. The next step is for it to hold the credential, so the process never does.

## Did it hold? {#probe}

To find out, we wrote a probe: a small program that tries everything a sandboxed process should never do, and reports each result. We ran it three ways.

!shot px-probe.webp | images/ | What the probe tried, and what stopped it: as root in the container today, it could read /etc/shadow and the agent's home, write to /usr/lib and /tmp, see 92 processes, start a shell, mount a filesystem, make a user namespace, reach the internet and the agent's proxy, and open a netlink socket; under the Hello World policy, all of it was refused; with seccomp and Landlock switched off, the other walls still refused all but the netlink socket. | comparison

- **As root, today.** It could do 13 of its 14 attempts. Only tracing process 1 was refused.
- **Under the policy.** It could do none of them.
- **With seccomp and Landlock switched off.** The other walls still refused all but two. The files were not there, `/tmp` was read-only, it saw one process, and there was no network. The two it got through: opening a netlink socket, and signalling process 1, which inside its namespace is the probe itself.

That is the point of defence in depth. No single wall has to be right, and switching one off does not open the door.

We also tested the parts that do not show in that table:

- **The broker.** Under a policy for a Python script that fetches one page, the script fetched send.sgraph.ai, and the broker refused example.com and api.anthropic.com with a 403. When the probe ran under the same policy and tried to go around the broker, Landlock refused the connection. With Landlock off, the firewall rule for that user refused it.
- **The process limit.** A loop of forks stopped at 63 processes. With seccomp on, it could not fork at all, because the traced Hello World never did.

## sgit, under its own policy {#sgit}

Then the real target. We traced sgit initialising a vault, committing a file and checking its status, in one working folder, and ran the same thing under the policy. It worked: the vault was created, the file committed. And the trace caught something worth knowing. `sgit status` talks to the server even when there is nothing to push, so the policy needed its host, dev.send.sgraph.ai, through the broker. A policy derived from a run tells you what the software actually does, not what you assumed.

## What it costs {#cost}

We expected the setup to be the expensive part, and at first it was: building the root with a shell script, calling `mount` three times per file, took 1.7 seconds for 169 files. Doing the same with direct system calls from one small program brought it to about 60 milliseconds, whatever the number of files.

!shot px-cost.webp | images/ | The size of a policy, and what it costs: Hello World in C, 1 file, 12 system calls, no hosts, 5 ms bare, 103 ms of policy overhead; Hello World in Python, 37 files, 34 system calls, 30 ms bare, 92 ms overhead; Python fetching one page, 169 files, 44 system calls, one host, 565 ms bare, 149 ms overhead; sgit init, commit and status, 1,025 files, 58 system calls, one host, 3,495 ms bare, 187 ms overhead. | comparison

The overhead, the median of five runs, is between 92 and 187 milliseconds: making the user, the firewall rule and the limits, building the root, and cleaning up. The run itself is within noise of the bare run. For sgit, whose clone already takes from seconds to tens of seconds, that is 5% on a three-and-a-half-second job. And most of it can be done in advance: the user, the rules and the root can be prepared before they are needed. Making the user alone is about 20 milliseconds, and a uid that simply is not in use would do without it.

## A policy of policies {#policy-of-policies}

This is also a great example of a policy of policies. There is a policy for the operating system, one for the environment, one for Python, one for sgit, and one for this execution. Each narrows the one before it and never widens it, the way [decisions at every level](https://newsroom.sgit.ai/articles/approve-at-altitude.html) may narrow the level above. The process gets only what is left.

!shot px-layers.webp | images/ | A policy of policies: the operating system (what Linux can do here), the environment (this container's proxy, CA bundle and paths), the runtime (Python and its standard library), the application (sgit, its dependencies and its server), and this execution (one command, one folder, one host, one user for one run), each narrowing the one above. | concept

And, as with hooks, the policy executes nothing. It says what is allowed; the runtime enforces it. [Hooks are kernel code](https://newsroom.sgit.ai/articles/hooks-are-kernel-code.html) argued that an agent's rules should move from hope into enforcement. This is the same move, one level down, into the kernel itself.

## The size of the policy measures the software {#measure}

There is a bonus. Once a process has a policy, you can see how well engineered it is by the size of what it needs. The smallest possible Linux process has a tiny policy: Hello World in C needs one file and twelve system calls. Hello World in Python needs 37 files and 34. A Python script that fetches one page needs 169 files. sgit needs 1,025 files, 66 MB and 58 system calls: 544 files of its own modules, 231 from Python's standard library, 122 from osbot_utils and 85 from cryptography, 15 MB on its own.

That is not a criticism; it is a map. It says where the attack surface is, which dependencies carry the weight, and what a smaller, purpose-built sgit for one job could drop. It is all about least privilege, and you cannot have least privilege until you know what the least is.

## What this does not claim {#limits}

- **One run is not every path.** A trace sees only what that run did; error paths and rare branches need more runs, ideally the test suite, which is one more reason to have one.
- **seccomp filters by call, not by argument.** The netlink socket got through because `socket` was allowed; filtering on the arguments is the next step.
- **This is a prototype.** About 350 lines of Python and C, run in one container, not a hardened tool.
- **The microVM is still the outer wall.** This adds walls inside it; it does not replace it.
- **The key service is not built.** The broker here decides where a process may go; it does not yet hold a credential.
- **The numbers are this machine's.** Four cores, one container; sgit-ai 0.21.0 as installed here.

## Where this comes from {#sources}

My voice memo of 24 October 2026. The experiment, run that day in this newsroom's Claude Code cloud container by this site's agent: the code, the four policies and the results are in [the data pack](/articles/data/process-behaviour-policies__pack.json). The kernel interfaces are documented in the Linux kernel's [Landlock](https://docs.kernel.org/userspace-api/landlock.html) and [seccomp](https://docs.kernel.org/userspace-api/seccomp_filter.html) pages. Related: [application behaviour policies](https://newsroom.sgit.ai/articles/application-behaviour-policies.html), [a skill behaviour policy](https://newsroom.sgit.ai/articles/skill-behaviour-policy.html), [allowed is not right](https://newsroom.sgit.ai/articles/allowed-is-not-right.html), [a policy beside the prompt](https://newsroom.sgit.ai/articles/a-policy-beside-the-prompt.html), [approve at altitude](https://newsroom.sgit.ai/articles/approve-at-altitude.html), [hooks are kernel code](https://newsroom.sgit.ai/articles/hooks-are-kernel-code.html), [the key is not the risk](https://newsroom.sgit.ai/articles/the-key-is-not-the-risk.html), [footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
