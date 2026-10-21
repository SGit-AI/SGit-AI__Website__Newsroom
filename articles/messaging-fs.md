# Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line, sgit.ai

> In the early versions of what is now the append lane, the API was called the inbox, and two agent teams used it to send each other signed, encrypted messages in both directions. It worked, and it was crude. I think we now have a much better way of doing it. Every user will have a vault, their billing vault or a comms vault, and every vault can have append lanes: write-only channels that anyone holding a token can write to and only the owner can read. Put that together with PKI and you have a full messaging system between vaults. It is not quite peer to peer, because everything still goes through the server, but the server only ever sees ciphertext, its size and its time. Each message is encrypted to the recipient's public key and signed by the sender, so we always know who sent what. On top of that transport sits a schema, which I would call Messaging-FS, alongside Issues-FS and Email-FS: a conversation is one JSON file, updated as each message and reply arrives, where an email is one file at a time. The same messages can be sent and read from a web messenger or from the command line. This maps out the workflow, what exists, and what we would build.

*Source: <https://newsroom.sgit.ai/articles/messaging-fs.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line

# Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/messaging-fs.md) · [newsroom v0.13.15](https://newsroom.sgit.ai/admin/versions.html) · vaultsmessagingpkiappend-lanesarchitectureproposalarticle

***Abstract:** In the early versions of what is now the append lane, the API was called the inbox, and two agent teams used it to send each other signed, encrypted messages in both directions. It worked, and it was crude. I think we now have a much better way of doing it. Every user will have a vault, their billing vault or a comms vault, and every vault can have append lanes: write-only channels that anyone holding a token can write to and only the owner can read. Put that together with PKI and you have a full messaging system between vaults. It is not quite peer to peer, because everything still goes through the server, but the server only ever sees ciphertext, its size and its time. Each message is encrypted to the recipient's public key and signed by the sender, so we always know who sent what. On top of that transport sits a schema, which I would call Messaging-FS, alongside Issues-FS and Email-FS: a conversation is one JSON file, updated as each message and reply arrives, where an email is one file at a time. The same messages can be sent and read from a web messenger or from the command line. This maps out the workflow, what exists, and what we would build.*

Messaging between two vaults. Each vault has a lane for the other: Alice encrypts to Bob and writes to the lane on Bob's vault, Bob does the same into Alice's. Each owner drains its own lane, checks the signature, and commits the message to its own copy of the thread.

## In short

- **We have done this before, crudely.** The append lane used to be called the inbox, and agents messaged each other over it.
- **Every user now has a vault.** And every vault can have append lanes.
- **Lanes plus PKI make a messenger.** Encrypted to the recipient, signed by the sender.
- **Not quite peer to peer.** It goes through the server, which sees only ciphertext, size and time.
- **Messaging-FS is the schema.** One JSON file per conversation, next to Issues-FS and Email-FS.
- **Web and command line, the same messages.** A messenger in the browser, or a terminal.
- **It is a proposal.** The transport exists; the schema and the commands are to build.

## Where we started: the inbox

This is something we have already done once. In the early versions of SG/Send's vault API, the channel that is now called the append lane was called the inbox, and it was renamed in v0.32.7. On 25 and 26 September 2026, two agent teams used it to send each other signed, encrypted messages in both directions, without either holding the other's vault key, and one of them a Claude Code session that could keep no secret between sessions. sgit.ai published [the write-up](https://sgit.ai/docs/append-lane-messaging.html), and the [vault messaging guide](https://sgit.ai/docs/vault-messaging.html) that came out of it.

It worked, and it was crude. Reading the write-up again, the rough edges are clear:

- **The lane address was agreed by hand.** The design is that a sender works out your lane from your public key; that step "is not yet wired end to end", so a token was generated and handed over.
- **The payload was encoded twice.** The encrypted file is base64 text, and the request sent base64 of that.
- **Adding a sender replaced the list.** Configure "replaces the anchor list", so adding one sender meant sending all of them again.
- **The signature covered only part of the envelope.** The inner ciphertext, not the wrapped key, the IV or the recipient.
- **Everyone wrote their own tools.** In the write-up's words, "two independent teams each wrote the same tooling".

Those are exactly the things a messenger would fix, and most of them are written down as recommendations to the sgit team in the same document.

## The idea: a messenger between vaults

What has changed since is that every user will have a vault: the billing vault in [the user keeps the meter](the-user-keeps-the-meter.md), or a comms vault, some storage of their own. And every vault can have append lanes, which we already use to process and communicate: from readers to this newsroom's editor in [the editor's channel](the-editors-channel.md), and between agents.

Put a lane on each user's vault, and PKI on top, and you have a full messaging system between vaults. A vault sends a message to another vault. Once you have that, you can have the equivalent of a messenger: a typical web-based one, or one on the command line, because sending and receiving are just calls.

It is not peer to peer, strictly: every message goes through the server. But it is end to end encrypted. In the guide's words, what the server can see is "that a lane received something, how big it was, and when. What it cannot see: the content, or the recipient's private key, which never leaves their machine."

## How one message travels

The transport already exists, as six calls on the vault API, and the reason it works is that four capabilities are kept apart. From sgit.ai's API page:

- **The append token, held by the sender.** It can write to one lane, and nothing else: not list, not fetch, not read.
- **The enum key, held by the vault owner.** It can list, fetch and mark messages processed, and cannot write.
- **The write key, held by the vault owner.** It configures the lanes and purges them.
- **The private key, held by the vault owner.** It decrypts, and it is "never sent to the server".

So a sender "can put something into your vault and learn nothing at all, not the contents, not the volume, not whether anyone else writes there". The write call answers with exactly `{"ok": true}`.

One message, step by step. Alice encrypts to Bob's public key, signs with her own key, keeps a copy in her thread, and writes to Bob's lane. The server answers only "ok". Bob lists and fetches with his enum key, decrypts, checks that the signature, the lane and the sender agree, adds the message to his copy of the thread, and marks it processed.

## Messaging-FS and Email-FS

The transport carries bytes; it does not say what they mean. The guide is plain about it: "The client decides what the bytes mean." What a messenger needs on top is a schema, a convention for the files on each side, the same way we already have [Issues-FS](https://newsroom.sgit.ai/articles/memory-is-not-a-spectator-sport.html), where an issue is a folder whose history is the vault's history, and Email-FS, where a message is a file with email headers.

I think both models have a place here:

- **Messaging-FS: a conversation is one file.** Messages are small and thread-like. A conversation is one JSON file, updated with each new message and each reply.
- **Email-FS: a message is one file.** An email is bigger, and arrives a file at a time, with its headers, into an inbox folder, then done, with an outbox for what goes out. Full-blown emails between vaults work the same way.

The layout on each side could be as simple as this:

```

messages/                      Messaging-FS
  contacts.json                who, their key fingerprint, their vault and lane
  threads/
    bob.json                   one conversation, rewritten as messages arrive

mail/                          Email-FS
  inbox/  done/  outbox/
    2026-10-21T10-00_a3f8.eml  one message, one file

```

And a thread, as a sketch, not a format:

```

{
  "thread": "alice-bob",
  "with": { "name": "Bob", "fingerprint": "Bob's signing key", "vault": "Bob's vault id" },
  "messages": [
    { "id": "the server's file id", "from": "alice", "at": "2026-10-21T10:00:00Z",
      "text": "Shall we look at the billing flow on Thursday?" },
    { "id": "the server's file id", "from": "bob", "at": "2026-10-21T10:04:00Z",
      "reply_to": "the first message's id", "text": "Yes, at ten." }
  ]
}

```

The server names each file it stores by the time it arrived, as `{epoch_ms}_{24-hex}.enc`, so messages sort in the order they landed, which is what a thread needs.

## Each vault writes only its own files

The design avoids conflicts the same way the billing design does: each side writes only its own vault. Alice's thread with Bob lives in Alice's vault; Bob's lives in Bob's. When Alice sends, she writes to Bob's lane and adds the message to her own copy of the thread. When Bob's browser drains his lane, it adds the message to his copy and commits it.

The lane itself sits beside the version-controlled tree, not inside it. From the API page: "appends never touch a branch and never conflict with a push." Only the owner's drainer moves a message from the lane into the vault, and when it does, it is an ordinary, versioned commit. So the history of a conversation is the vault's history, as it is for an issue in Issues-FS.

## Who sent it

PKI is what turns a channel into a messenger you can trust. Every message is encrypted to the recipient's public key and signed with the sender's key, and the write-up's rule is a good one to keep: "the lane says who holds the token, the signature says who holds the key, and the From: header must match both."

The keys themselves come from the same place as everything else now, as in [PKI everywhere](pki-everywhere.md): made on the device, published in a register anyone can check, and pinned the first time you talk to someone. Verify by fingerprint, not by name. And the pattern from [the user keeps the meter](the-user-keeps-the-meter.md) carries over: pin the first commit of a vault you share with someone, and every later commit can be checked for who wrote it.

## On the web, and on the command line

The same messages can be sent and read from two kinds of client.

**In the browser.** A vault app already has the six calls, through `sg.append`. One detail shapes the design: from an app, `write` can reach any vault, but `list`, `fetch` and the rest act only on the vault that is open, because listing someone else's lane would need their enum key, and shipping that in a page "would give every visitor read access to the whole lane". That is exactly the right shape for a messenger: you write to other people's lanes and read only your own.

**On the command line.** Today it takes two steps: `sgit pki encrypt` to the recipient, then an HTTP call to write. sgit-ai 0.23.0 has the `pki` commands, to encrypt, decrypt, sign, verify and keep contacts, but no command for lanes yet. The write-up asked for one: "sgit lane / sgit inbox CLI: open, send, drain, close, rotate". With that, a terminal messenger is a few commands: send, drain, and show a thread.

I think the main use case is the web. But it is the same append lane either way, and the same files.

## What would make it a messenger

Most of what is needed is already listed in the write-up's recommendations, which makes this a short list:

- **Derive the lane address from the public key.** So a sender needs only your public key and vault id, not a token handed over by hand.
- **One encoding.** Send the encrypted file once, not base64 of base64.
- **Add and remove senders.** Without resending the whole list.
- **Sign the whole envelope.** The wrapped key, the IV and the recipient, not only the ciphertext.
- **Report the signer's fingerprint.** Because names repeat.
- **A command for lanes.** Open, send, drain, close, rotate.
- **The routes in production.** Today the append routes are on dev.send.sgraph.ai, at v0.34.1; send.sgraph.ai, at v0.32.4, still has the older inbox routes.
- **The Messaging-FS schema itself.** Threads, contacts, replies, and receipts sent as messages.

## What it is not

The guide says what the transport is not, and it is worth keeping in view: "Not a chat protocol, not a queue with delivery guarantees, and not anonymous, the server sees lane activity and timing even though it cannot read content." Messaging-FS is the chat protocol on top; delivery is confirmed by a reply or a receipt, not by the server; and the timing of messages is visible to the server even when nothing else is.

There are limits too: 5 MB per message, and 1,000 waiting messages per sender's lane, after which the server refuses more until the owner drains. For a message, that is plenty; a large file is better shared as a vault of its own, with the message carrying the link.

## Where it fits

Once vaults can message each other, a lot of what we already do becomes the same thing. The validation notes in the billing design are messages from us to a user's vault. A reader writing to the editor is a message. Agents handing work to each other, as in the September write-up, are messages. And so is a person writing to a person, which is where a messenger starts.

## What this does not claim

- **Messaging-FS does not exist yet.** It is a proposed schema; Email-FS lite and Issues-FS are in use.
- **The transport exists.** On dev.send.sgraph.ai, used both ways by two agent teams in September.
- **The CLI has no lane command.** As of sgit-ai 0.23.0.
- **The rough edges are from the write-up.** Some may have been fixed since; the server versions were read on 21 October 2026.
- **It is not anonymous.** The server sees when and how much, not what.

## The diagrams, as source

The two diagrams above are Mermaid, rendered for this page. Here is their source, to reuse or correct.

```

flowchart LR
  A["Alice's browser<br/>or command line"]
  subgraph AV["Alice's vault"]
    AL["Lane from Bob"]
    AT["threads/bob.json"]
  end
  subgraph BV["Bob's vault"]
    BL["Lane from Alice"]
    BT["threads/alice.json"]
  end
  B["Bob's browser<br/>or command line"]
  A -->|encrypt to Bob, sign, write| BL
  B -->|encrypt to Alice, sign, write| AL
  AL -->|drain, verify, commit| AT
  BL -->|drain, verify, commit| BT

```

```

sequenceDiagram
  participant A as Alice's browser
  participant S as Server
  participant B as Bob's browser
  A->>A: Encrypt to Bob's public key, sign with Alice's key
  A->>A: Add the message to Alice's copy of the thread
  A->>S: Write to Bob's lane, with Alice's append token
  S-->>A: ok, and nothing else
  B->>S: List Bob's lanes, with Bob's enum key
  B->>S: Fetch the new message
  B->>B: Decrypt, check the signature, the lane and the sender agree
  B->>B: Add it to Bob's copy of the thread, commit
  B->>S: Mark it processed

```

## Where this comes from

A voice memo of 21 October 2026. sgit.ai's [append lanes API](https://sgit.ai/api/append-lanes.html), [vault messaging guide](https://sgit.ai/docs/vault-messaging.html) and [append-lane messaging between agents](https://sgit.ai/docs/append-lane-messaging.html), version 3, of 26 September 2026; [memory is not a spectator sport](https://newsroom.sgit.ai/articles/memory-is-not-a-spectator-sport.html), for Issues-FS and Email-FS lite. The API description of dev.send.sgraph.ai and send.sgraph.ai, and the commands of sgit-ai 0.23.0, read the same day. Related: [the user keeps the meter](the-user-keeps-the-meter.md), [the editor's channel](the-editors-channel.md), [PKI everywhere](pki-everywhere.md), [agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Vaults & method[This article as a graph →](graphs.md#messaging-fs)

### Builds on

- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault](the-editors-channel.md) A key makes a browser an editor's: reads, sign-offs and fixes go to a vault, a daily pass acts and replies, and five lanes set what any reader sends.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.

### Continued by

- [The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed](the-attack-surface-you-do-not-have.md) Every CVE makes me smile: moving to the client side took my servers out of the news, and the constraint turned out to be speed.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 235 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=235)

**Posting this article on LinkedIn?** The cover is [messaging-fs.jpg](banners/messaging-fs.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/messaging-fs.html)*
