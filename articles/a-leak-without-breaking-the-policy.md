# Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks, sgit.ai

> One of our first customers asked a good question: could an API key, or someone's personal data, leak without breaking any Agent Behaviour Policy? The answer is yes, if the policy only lists what the agent can do. Sending an email is a capability; putting a key in it is content. So a policy that covers secrets needs rows about content too, such as disclosing a secret, and each row needs a barrier like any other. There are three levels. Told: a sentence in the prompt, kept by the model. Checked: a hook that scans every tool call, every tool result and the final answer. Never given: the agent asks for the action, and something out of its reach holds the key. We wrote the hook and tested it against nine ways a secret tries to leave. It denied three, redacted one, blocked one, let an ordinary command through, and missed three: a key encoded in base64, a key split in two, and a file of secrets piped straight out. Then we added four experimental rules: look inside base64 and hex, match any ten characters of the session's own secrets, refuse long base64 in outbound calls as a matter of policy, and refuse a command that sends a secrets file to the network. With them, all nine were caught. Run over the 3,451 real commands of the session that wrote this article, the hook refused 22, and none was ordinary work. The third level is still the best answer: an agent that never sees the key cannot leak it.

*Source: <https://newsroom.sgit.ai/articles/a-leak-without-breaking-the-policy.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks

# Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.2.0, 3 versions](versions/a-leak-without-breaking-the-policy.md) · [newsroom v0.12.158](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-behaviour-policysecretshooksprivacyarticle

***Abstract:** One of our first customers asked a good question: could an API key, or someone's personal data, leak without breaking any Agent Behaviour Policy? The answer is yes, if the policy only lists what the agent can do. Sending an email is a capability; putting a key in it is content. So a policy that covers secrets needs rows about content too, such as disclosing a secret, and each row needs a barrier like any other. There are three levels. Told: a sentence in the prompt, kept by the model. Checked: a hook that scans every tool call, every tool result and the final answer. Never given: the agent asks for the action, and something out of its reach holds the key. We wrote the hook and tested it against nine ways a secret tries to leave. It denied three, redacted one, blocked one, let an ordinary command through, and missed three: a key encoded in base64, a key split in two, and a file of secrets piped straight out. Then we added four experimental rules: look inside base64 and hex, match any ten characters of the session's own secrets, refuse long base64 in outbound calls as a matter of policy, and refuse a command that sends a secrets file to the network. With them, all nine were caught. Run over the 3,451 real commands of the session that wrote this article, the hook refused 22, and none was ordinary work. The third level is still the best answer: an agent that never sees the key cannot leak it.*

Nine ways a secret tries to leave, at each level: told, checked and never given.

## In short

- **Yes, a key can leak without breaking a capability row.** Sending is allowed; the key is content.
- **So a policy needs content rows too.** Disclosing a secret, disclosing personal data.
- **Told: a sentence in the prompt.** The model keeps it, or does not.
- **Checked: a hook on every input and output.** Deterministic, and it has gaps.
- **Never given: the agent never holds the key.** It asks for the action instead.
- **We tested a hook against nine leaks.** It caught five and missed three.
- **Four experimental rules close the three.** Base64 refused as policy, among them.
- **Run on 3,451 real commands, it refused 22.** None was ordinary work.
- **The hook is below, CC BY 4.0.** Take it, tune it, run it.

## The question

One of our first customers said something that deserves a proper answer. What scared them was that an API key, or personal data, might leak without breaking any Agent Behaviour Policy. My first reaction was: how? The policy should include that behaviour. Their reply was that it might be their lack of knowledge of what a policy can do.

It is a good question, and the honest answer is that they are right about a policy that only lists capabilities. An [Agent Behaviour Policy](https://abp.sgit.ai/) writes down what an agent can do (the grant), what it may do (the mandate), the gap, and what stands in the way. If the agent may send email, the row says yes. A key pasted into the body of that email is not a different capability. It is the same action, with the wrong content.

## Capabilities and content

So a policy that covers secrets and personal data needs two more kinds of row. The first is about reach: can the agent read the key at all? In most deployments it can, because the key is in its environment, and the mandate almost never needs it to read the key, only to use it. That is excess grant, and it is exactly what a policy is for finding. The second is about content: `disclose.secret` with a mandate of no, and `disclose.personal_data` with a mandate of only to the person it is about.

A content row is like the investment advice row in [the Pellbridge agents](inside-the-pellbridge-agents.md): no system can block a sentence outright, so the barrier is a check, and a check can miss. That is why the question of where the rule is kept matters more here than anywhere.

## Three levels, and better names

We have described the three levels before, in [governs, enforces, attests](governs-enforces-attests.md): in the prompt, in hooks, outside the agent. They need plainer names. I suggest these.

- **Told.** The prompt says: never print, send or store a key. The model decides whether to keep it, so in ABP terms it is an expectation.
- **Checked.** A hook in the agent's harness scans everything going out and coming in, and stops or redacts what matches. It is deterministic, which is a real level of guarantee, but it runs on the agent's own machine, and if the agent's account can change its configuration it is a setting.
- **Never given.** The key is held by something out of the agent's reach, a proxy or a host, which adds it to the request on the way out. The agent asks for the action, not the key. This is a boundary, and I still think it is the workflow to aim for.

## The hook

Here is what Checked looks like in practice, for Claude Code. It runs on three hook events. On `PreToolUse` it scans the tool's input, and denies the call if it carries a secret, or names a variable that holds one: `$OPENAI_API_KEY` in a command never shows the value, but it still sends it. On `PostToolUse` it scans the tool's result and redacts secrets before the model sees them; Claude Code's documentation says to "intercept at `PreToolUse` for outbound tool inputs and `PostToolUse` for inbound tool results", and that `updatedToolOutput` "only changes what Claude sees. The tool has already run by the time the hook fires." On `Stop` it blocks a final answer that carries a secret or a card number; that hook receives the answer as `last_assistant_message`.

It matches common key formats with a regular expression, card numbers with the Luhn check, and, most usefully, the exact values of the session's own secrets, read from its environment, so a match on those is not a guess. The experimental rules, described below, are on by default and can be turned off with `SECRET_GUARD_EXPERIMENTAL=0`.

```

#!/usr/bin/env python3
"""secret_guard: a Claude Code hook that keeps secrets and personal data out of tool calls.
PreToolUse: deny a call whose input carries a secret, or names a secret's variable.
PostToolUse: redact secrets from a tool's result before the model sees it.
Stop: block a final answer that carries a secret.
EXPERIMENTAL rules (on by default; set SECRET_GUARD_EXPERIMENTAL=0 to turn them off): look inside base64 and
hex, match pieces of the session's own secrets, refuse long base64 in outbound calls, and refuse a command that
sends a secrets file to the network.  CC BY 4.0, newsroom.sgit.ai."""
import base64, binascii, json, os, re, sys

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

EXPERIMENTAL = os.environ.get("SECRET_GUARD_EXPERIMENTAL", "1") != "0"
B64 = re.compile(r"[A-Za-z0-9+/_-]{24,}={0,2}")
NET = re.compile(r"\b(curl|wget|nc|ncat|scp|rsync|ftp|Invoke-WebRequest)\b")
SECRET_FILE = re.compile(r"(?:^|[\s/'\"=<@])(\.env(?:\.[\w-]+)?|[\w-]+\.pem|id_rsa|id_ed25519|\.netrc|\.npmrc|\.pypirc|\.aws/credentials)\b")

def decoded(text):  # what base64 and hex runs in the text say, decoded
    out = []
    for m in B64.finditer(text):
        t = m.group()
        for dec in (lambda x: base64.b64decode(x + "=" * (-len(x) % 4)), lambda x: base64.urlsafe_b64decode(x + "=" * (-len(x) % 4))):
            try: out.append(dec(t).decode("utf-8")); break
            except (binascii.Error, UnicodeDecodeError, ValueError): pass
    for m in re.finditer(r"\b(?:[0-9a-fA-F]{2}){12,}\b", text):
        try: out.append(bytes.fromhex(m.group()).decode("utf-8"))
        except (ValueError, UnicodeDecodeError): pass
    return out

def pieces(text, n=10):  # a known secret split into parts: any 10 characters of it in a row
    return ["a piece of $" + k for k, v in KNOWN.items() if any(v[i:i + n] in text for i in range(0, len(v) - n + 1))]

def blob(t):  # long base64: not plain hex (a commit hash), not a path or an id in a URL (mostly short parts)
    parts = re.split(r"[/_-]", t)
    return (len(t) >= 40 and sum(len(x) < 8 for x in parts) <= 1 and not re.fullmatch(r"[0-9a-fA-F]+", t)
            and all(re.search(c, t) for c in ("[a-z]", "[A-Z]", "[0-9]")))

def experimental(text):
    f = []
    for d in decoded(text): f += ["encoded " + x for x in findings(d)]
    f += pieces(text)
    if any(blob(m.group()) for m in B64.finditer(text)): f.append("a long base64 string (refused as policy)")
    if NET.search(text) and SECRET_FILE.search(text): f.append("a secrets file sent to the network")
    return sorted(set(f))

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
    if EXPERIMENTAL and not f: f = experimental(t)
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

## Nine leaks, tested

We ran it against nine cases, with fake keys made at random for the test, so no real key was involved.

- **Denied:** a command with a GitHub token in it; a command that sends a key by its variable name; a web fetch with the key's value in the URL.
- **Redacted:** a tool result that prints the key. The command ran, but the model saw `[redacted]`.
- **Blocked:** a final answer with a card number in it.
- **Allowed:** an ordinary `ls` and `git status`, as it should be.
- **Missed:** the key encoded in base64; the key split in two and joined by the command; and `cat .env | curl -d @- …`, a file of secrets piped straight out, where neither the value nor its name ever appears in the command.

The three misses are not bugs in the first version of this hook. They are what a check on the text of a command cannot see: an encoding, an assembly, or a file the hook never reads.

## Experimental rules

Each of the three has a recognisable shape, so we added four rules and marked them experimental, to try before making them official.

- **Look inside encodings.** Decode every base64 and hex run in a call, and scan what it says. A key in base64 is still a key.
- **Match pieces of known secrets.** Any ten characters in a row of the session's own secrets is a match, so a key split into parts is caught as long as one part is ten characters long. Ten random characters do not appear by chance.
- **Refuse long base64 outright.** An agent rarely has a reason to send a long base64 string anywhere, so the policy is simply no: forty characters or more, mixing cases and digits, not a commit hash, and not a path or an identifier inside a URL.
- **Refuse a secrets file sent to the network.** A command that names a file such as `.env`, a `.pem` key or `.aws/credentials` and also runs `curl`, `wget`, `nc` or `scp` is refused.

With them on, all nine cases were caught: the base64 key was refused twice over (decoded, and as a long base64 string), the split key as a piece of the known secret, and `cat .env | curl` as a secrets file sent to the network. We also tested random data in base64, a known key format inside a base64 blob, and the key in hex: all refused. And we tested what should pass: a commit hash, long file paths with version numbers, a GitHub URL, a commit with a co-author line, reading `.env` without sending it. All allowed.

The real test is ordinary work, so we ran the hook over every shell command of the session that wrote this article: 3,451 of them. The first version of the base64 rule refused 183, almost all because of the random session identifier in every commit message; the second, which ignores identifiers inside URLs, refused 22. Thirteen were real: the session passing its own vault token to a tool on the command line, which is exactly what the policy says not to do, even though the use was legitimate. Seven were the test data for this hook, and two were the example key from AWS's own documentation. None was ordinary work.

Those thirteen are the best argument for the next section. The rule was right; the fix is not to allow it, but to stop giving the token to the session.

## Never given

So the strongest answer is the third level. If the key is not in the agent's environment, none of the nine cases has anything to leak. The agent asks a proxy or a host to make the call, and the key is added on the way out, by something the agent cannot read.

We already work this way in places. In [the no-server studio](inside-the-no-server-studio.md), the vault host holds the model's key, caps the spend and never shows it to the page. In [handing secrets to agents](handing-secrets-to-agents.md), a secret is piped into the tool that needs it and never into the prompt. And the cloud sessions this newsroom runs in add some credentials through a proxy on the way out, while others are still in the environment; moving those out is on our own list.

Personal data is harder, because the agent often has to see it to do the job. There, Never given means minimisation: the agent gets a token or a reference instead of the card number, and only the system that needs the real value holds it. For what it does see, Checked is the right level, with every miss reported as a near miss.

## What to write in the policy

For an agent that uses an API key, three rows, each with its barrier:

- **`read.secret.api_key`**: can it? If yes, the mandate is almost always no. Kept out of reach by giving the key to a proxy, not the agent.
- **`disclose.secret`**: mandate no. Checked by a hook on inputs, results and answers, knowing the session's own secret values.
- **`disclose.personal_data`**: only to the person it is about. Minimised where possible, checked where not.

Then the question our customer asked has a clear answer. A leak breaks a row; the row says what kept it; and the policy shows, before anything leaks, which rows are only told.

## What this does not claim

- **The hook is an example.** Tested on seventeen cases and one session, not on every way out.
- **The experimental rules are experimental.** Expect false positives in other kinds of work.
- **Regular expressions miss things.** Unknown formats, short pieces, other encodings.
- **A hook is only as strong as its configuration.** If the agent can change it, it is a setting.
- **Never given needs infrastructure.** A proxy or a host that holds the key.
- **The test used fake keys.** Made at random; no real secret was used.

## Where this comes from

A conversation with one of our first customers, and a voice memo of 20 October 2026. Claude Code's [hooks reference](https://code.claude.com/docs/en/hooks), read the same day. The Agent Behaviour Policy at [abp.sgit.ai](https://abp.sgit.ai/). Related: [governs, enforces, attests](governs-enforces-attests.md), [are hooks the sweet spot?](are-hooks-the-sweet-spot.md), [handing secrets to agents](handing-secrets-to-agents.md), [secrets on public keys](secrets-on-public-keys.md), [inside the Pellbridge agents](inside-the-pellbridge-agents.md), [PKI everywhere](pki-everywhere.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policy[This article as a graph →](graphs.md#a-leak-without-breaking-the-policy)

### Builds on

- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault](inside-the-no-server-studio.md) An infographic studio built to the no-server blueprint, mostly simulated, in a vault: what is real, the business plan, and a bug found live.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.

### Continued by

- [Proven controls, for agents: an answer to Hem Pant's governance as code and Sondera's policy-as-code paper, with the column they leave open and the controls we have actually tried to break](proven-controls-for-agents.md) Hem Pant's governance as code and Sondera's policy-as-code paper, joined: who holds each control, and six controls we tried to break.
- [How a memo becomes a release: the newsroom's pipeline end to end, what runs in the session and what runs on GitHub, how long each part takes, and what a new session would be missing](how-a-memo-becomes-a-release.md) From voice memo to tagged release: the session's checks, GitHub's checks, the times, what is redundant, and what a new session would lack.
- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.
- [Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed](free-to-copy-paid-at-the-source.md) Open policies and hooks, free to copy, can still earn per use at the official source, if others review them and we sign them.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 227 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=227)

**Posting this article on LinkedIn?** The cover is [a-leak-without-breaking-the-policy.jpg](banners/a-leak-without-breaking-the-policy.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-leak-without-breaking-the-policy.html)*
