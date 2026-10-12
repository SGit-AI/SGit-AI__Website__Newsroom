# Seven vaults, one method, sgit.ai

> Publishing seven encrypted vaults in a fortnight turned an ad-hoc process into a repeatable one. Every rule in it exists because something went wrong first, including three vault keys submitted for publication that would have handed the world write access.

*Source: <https://newsroom.sgit.ai/articles/seven-vaults-one-method.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Seven vaults, one method

# Seven vaults, one method

2026-08-19 · [article v1.2.1, 4 versions](versions/seven-vaults-one-method.md) · vaultspublishingmethod

***Abstract:** Publishing seven encrypted vaults in a fortnight turned an ad-hoc process into a repeatable one. Every rule in it exists because something went wrong first, including three vault keys submitted for publication that would have handed the world write access.*

Between 14 and 18 August this site published seven vaults. Each one is a real encrypted vault you can open in a browser from a read key printed on its page: [a photo gallery](https://sgit.ai/demos/vaults/algarve-may-2026/index.md), [field notes](https://sgit.ai/demos/vaults/field-notes/index.md), [a patient-held supplement record](https://sgit.ai/demos/vaults/supplement-stack/index.md), [a risk register](https://sgit.ai/demos/vaults/risk-mandate/index.md), [a browser-isolation risk graph](https://sgit.ai/demos/vaults/agentic-browser-isolation/index.md), [a fact-to-risk explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/index.md), and [the catalogue that indexes them](https://sgit.ai/catalogue/index.md), itself a vault.

By the third one it was obvious that we were repeating ourselves badly. By the seventh there was a method, and every rule in it exists because something went wrong first.

## The rule that matters most

**Classify the credential before it touches anything.**

Three of the seven vaults arrived as a *vault key* described as a read key. A vault key is write access. Publishing one would have handed anybody who read the page the ability to rewrite the vault, and because a vault key is also the address and the encryption root, there is no revocation, no rotation, and no undo.

They were caught by shape. A read key is 64 hex characters; a vault key is a generated passphrase, which is 24 lowercase alphanumerics. That catch depended on somebody looking, which is not a control. So it became [a script](https://sgit.ai/demos/vaults/publishing.md):

```

$ python3 admin/build/check_credential.py '<credential>'
  form      : vault key (legacy passphrase:vault_id)
  publish?  : NO
  why       : 24 characters before the colon and not 64 hex, so it is a
              passphrase — a WRITE credential

```

Exit 0 means publishable. Exit 1 means stop. It never echoes what it was given.

Behind it sits a second line: the release validator scans every tracked file for any key-shaped string and for the actual passphrases, read at build time from a gitignored tier. That tripwire has caught its own author three times, each time writing the prefix in prose, in documentation explaining what a write credential looks like. Which is the point: a rule that only catches other people is not a rule.

## Derive rather than refuse

The interesting part of the vault-key catch is what happens next. A read key is **derived one-way** from a vault key, so a submission that cannot be published can still become one that can:

```

c = Vault__Crypto()
pw, vid  = c.parse_vault_key(vault_key)
read_key = c.derive_keys(pw, vid)['read_key']

```

The vault key goes into a gitignored tier that the tripwire then scans for. The derived read key gets published. It is one-way: nobody can turn it back.

That is the whole shape of the thing this project is about, a capability you can hand over that is *strictly less* than the one you hold, with the reduction enforced by mathematics rather than by policy. The seven vaults span the range deliberately, from one that requests no permissions at all to one that can write a single folder.

## Audit with the key you are about to publish

Not with the vault key. With **exactly the credential a reader will have**, across every file.

This caught a real problem. One vault carried a sealed LLM credential, and a published read key in front of a metered capability is an open tab on somebody else's budget. Rather than reasoning about whether the sealing was sound, we took the published read key and attempted to open the credential with it. AES-GCM refused, `InvalidTag`, so no budget was exposed. Checked rather than assumed, and recorded either way.

That rule did not come from us. It came from the sixth vault, [Risk Graph Explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/index.md), which is the first one here that was **public by design**: it carries its own `PUBLIC.md` whose three rules its build enforces, and the third, *no metered capability behind a published read key*, was not in our guidance. It is now.

## Capture evidence by driving the real product

Every screenshot on a vault page is taken by opening the actual vault in a real browser with the published read key, performing the navigation, and cropping the result. No mock-ups.

This is slower than it sounds and worth every minute, because it repeatedly disagreed with what we were about to write. The rig grew a `appProbe` step for exactly that reason, ask the running app what its elements are called instead of guessing and burning a capture run per guess:

```

probe [class*=node] -> 37
  shapes ["g.cnode.inh","g.cnode","g.cnode.corp"]
  text   ["R1 An autonomous system operates in the es","R2 Stopping the agent is itself…"]

```

The alternative is a page that describes a product as its author remembers it.

## Describe, show, then admit

Every vault page ends with what the vault does *not* do. Not as a disclaimer at the bottom in small type, as a section with the same weight as the features.

This is the part that is tempting to skip and never should be. A published vault is an argument that this way of working is sound; an argument that omits its own edges is a brochure. The [limitations page](https://sgit.ai/docs/limitations.md) is the same instinct at site level, and the [comparison pages](https://sgit.ai/compare/index.md) go further still, they include rows where vaults lose.

## What it cost, and what it bought

Seven vaults, roughly four days of work, and the method is now [written down as a playbook](https://sgit.ai/demos/vaults/publishing.md) aimed at another site's agent rather than at us, which was the real test of whether it was a method or just a habit.

The honest ledger:

- **Three vault keys caught.** None published. Each would have been unrecoverable.
- **One budget exposure checked and cleared**, by attempting the attack rather than reasoning about it.
- **One upstream rule adopted** from a vault that was stricter than our guidance.
- **Three bugs found by testing rather than assumption** on a single page, a malformed selector that silently produced no images at all, escape sequences leaking as literal text, and a page that never loaded the component it depended on. All three would have shipped.

The last line is the one to keep. Every rule above is short and specific because it was learned by getting something wrong, in public, and writing down what it cost.

*The full method, step by step, is on [the publishing playbook](https://sgit.ai/demos/vaults/publishing.md). The vaults themselves are in [the catalogue](https://sgit.ai/catalogue/index.md), each with the read key that opens it.*

*© 2026 Dinis Cruz and the sgit.ai team. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Vaults & method[This article as a graph →](graphs.md#seven-vaults-one-method)

### Continued by

- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 2 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=2)

**Posting this article on LinkedIn?** The cover is [seven-vaults-one-method.jpg](banners/seven-vaults-one-method.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/seven-vaults-one-method.html)*
