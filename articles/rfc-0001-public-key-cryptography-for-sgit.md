# RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer, sgit.ai

> A Request for Comments, before anything is built. Today an sgit vault is protected by one symmetric read key and a write key that only the server checks, so anyone who holds the read key and can write to the store, the host or a mirror for example, can author history that clients accept. sgit's own threat model says so, and a test performs the attack. This RFC proposes two designs. Native PKI vault mode uses two key pairs, one for reading and one for writing, so a reader cannot write, a host cannot forge, and a write-only depositor becomes possible. Sealed files add an inner envelope to any vault, so chosen files can be read only by named people, whose private keys can live in a key file, an ssh key, a hardware key, or a remote service that logs and approves each decryption. We set out both, what they cost, what they cannot do, the services that could hold the private keys today, and fourteen questions where an outside view would change the design.

*Source: <https://newsroom.sgit.ai/articles/rfc-0001-public-key-cryptography-for-sgit.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer

# RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-09 · [article v1.0.0](versions/rfc-0001-public-key-cryptography-for-sgit.md) · [sgit.ai v0.7.17](https://sgit.ai/admin/versions.md) · rfcsgitpkipublic-key-cryptographyencryptionsignaturesed25519x25519hpkeagesealed-fileskey-managementthreat-modelrequest-for-commentsarticle

***Abstract:** A Request for Comments, before anything is built. Today an sgit vault is protected by one symmetric read key and a write key that only the server checks, so anyone who holds the read key and can write to the store, the host or a mirror for example, can author history that clients accept. sgit's own threat model says so, and a test performs the attack. This RFC proposes two designs. Native PKI vault mode uses two key pairs, one for reading and one for writing, so a reader cannot write, a host cannot forge, and a write-only depositor becomes possible. Sealed files add an inner envelope to any vault, so chosen files can be read only by named people, whose private keys can live in a key file, an ssh key, a hardware key, or a remote service that logs and approves each decryption. We set out both, what they cost, what they cannot do, the services that could hold the private keys today, and fourteen questions where an outside view would change the design.*

**RFC 0001 · Status: open for comment · Nothing here is implemented.** These are proposals for the sgit command line and the vault format, written by the sgit CLI agent for Dinis Cruz from a design session on 9 October 2026. There is no code and no release date. The full design documents are in the sgit repository: [native PKI vault mode](https://github.com/SGit-AI/SGit-AI__CLI/blob/48a608f/team/humans/dinis_cruz/claude-code-web/10/09/design__native-pki-vault-mode.md), [sealed files](https://github.com/SGit-AI/SGit-AI__CLI/blob/48a608f/team/humans/dinis_cruz/claude-code-web/10/09/design__sealed-files-layer.md), and [the analysis that led to both](https://github.com/SGit-AI/SGit-AI__CLI/blob/dev/team/humans/dinis_cruz/claude-code-web/10/09/design-analysis__read-write-keys-as-pki.md). **To comment**, [open an issue on the sgit repository](https://github.com/SGit-AI/SGit-AI__CLI/issues/new?title=RFC%200001%3A%20) with a title starting "RFC 0001:", or write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai). [The questions](#questions) are at the end.

Today: one symmetric read key that encrypts everything, and a write key that only the server checks. Because the read key is symmetric, whoever can read can also create data that decrypts and looks genuine.

**Today's keys, Mermaid source**

[rendered image](images/rfc-today.webp)

```
flowchart LR
  VK["Vault key<br/>passphrase : vault id"]
  RK["Read key<br/>AES-256-GCM<br/>encrypts everything"]
  WK["Write key<br/>sent to the server<br/>on every write"]
  SRV["Server<br/>stores ciphertext<br/>compares the write key"]
  C["Every client<br/>decrypts with the read key<br/>checks content hashes"]
  X["Read-key holder<br/>who can also write to the store:<br/>the host, a mirror, an attacker"]
  VK -- "PBKDF2" --> RK
  VK -- "PBKDF2" --> WK
  RK --> C
  WK --> SRV
  X -- "makes objects and branch pointers<br/>that decrypt under the read key" --> SRV
  SRV -- "clients accept them as genuine" --> C
```

## In short

- **The gap.** An sgit vault's read key is symmetric, so whoever can read can also produce data every client accepts. The write key is a password the server compares, and no client can check it. Anyone who holds the read key and can write to the store without that check, the host, someone who has compromised it, a static mirror, can author history.
- **The obvious fix does not work.** "Make the read key a public key and the write key a private key" fails, because whatever decrypts must be secret, and the public half can always be derived from the private half. **Two key pairs work.**
- **Design 1, native PKI vault mode**, a second way to run a vault: a read key pair and a write key pair, neither derivable from the other. A reader cannot write, a host cannot forge, and a **write-only depositor** becomes possible.
- **Design 2, sealed files**, an optional layer on any vault, today's included: chosen files are sealed to named people's public keys. Other vault members see that the file exists, not what is in it. The private key can live anywhere, **including a remote service that logs and approves each decryption**.
- **Both share a first step**: a writer signature on today's vaults, which closes the forgery gap without changing the data format.
- **Limits stay**: a host can still withhold data or serve an older signed state; a reader you remove keeps what they already read; with sealed files, names, paths, sizes and history stay visible to vault members.

## How sgit protects a vault today

A vault key is `passphrase : vault_id`. From the passphrase, PBKDF2-SHA256 with 600,000 iterations derives two keys. The **read key** encrypts everything in the vault with AES-256-GCM before it leaves the machine: every file, folder listing, commit and branch pointer. The server stores only ciphertext, which we have [checked on a self-hosted server](encrypted-memory-for-isolated-agents.md). Every stored object is named by the hash of its ciphertext, so a client can check that the server returned exactly what was stored, with no key and no trust. The **write key** is not used for any cryptography: the server compares it with the one it saw first and refuses writes that do not match. Commits are also signed, with ECDSA P-256, by the key of the clone that made them.

## The honest problem

The read key is symmetric: whoever can decrypt can also encrypt. A read-key holder can therefore produce objects, branch pointers and even signing-key files that every client accepts as genuine. Commit signatures do not save the day, because a signing key is trusted when its file decrypts under the read key, and a read-key holder can make such a file.

What stops a read-only holder from rewriting history today is the server's write-key check. So the risk is real whenever someone holds the read key and can write to the store without that check: the host itself, anyone who compromises it, a static mirror, anyone the host colludes with. And read-only shares, the [`sgit_public_read_` keys this site publishes](https://sgit.ai/docs/credentials.md), are read-key holders.

sgit's threat model lists this openly as a by-design risk. It carries a test that performs the forgery against an in-memory host and asserts that it still succeeds, so the gap cannot be quietly forgotten: when it closes, the test fails and the risk register has to change.

## The obvious idea, and the correction

The natural idea is to make the read key public and the write key private. A key pair supports two operations, and in each the direction is fixed:

| Operation | Done with | Undone or checked with | What it gives |
|---|---|---|---|
| encrypt, then decrypt | the **public** key | the **private** key | confidentiality to the private-key holder |
| sign, then verify | the **private** key | the **public** key | proof that the private-key holder wrote it |

Two facts settle it. The private half always yields the public half, so whichever key goes to the less trusted party must be the public one. And "decrypting with the public key" is not confidentiality; it is signing, which anyone with the public key can undo. So one key pair can give you *who wrote it*, but not secrecy. **Add a second key pair for reading, and every property falls out.**

## The first step both designs share: a writer signature

Before either design, today's vaults can get a **vault signing key**: an Ed25519 key derived from the passphrase along a third path, not from the write key (the server knows that) and not from the read key (read-only shares hold that). Writers sign the branch pointers and the branch index; every client verifies them. The objects underneath are content-addressed, so signing the roots authenticates the whole tree. No data is re-encrypted; vaults opt in. Ed25519 is chosen because its signatures are deterministic, so the browser and the command line can share byte-for-byte test vectors.

It closes the forgery gap for writers who share the passphrase, and its hard part is not the cryptography but downgrade resistance: a host must not be able to strip the signatures or the feature flag, so a signed vault gets a new key version that tells even a fresh clone that signatures are mandatory. The analysis estimates one and a half to two weeks for the command line, with the same work in the web UI.

## Design 1: native PKI vault mode

Two key pairs, neither derivable from the other: one for reading, one for writing. The data key is sealed to the read public key, heads are signed with the write private key, and the vault id is derived from the write public key.

**Design 1, Mermaid source**

[rendered image](images/rfc-design1.webp)

```
flowchart LR
  M["Owner seed M"]
  subgraph pairs["Two key pairs, neither derivable from the other"]
    direction TB
    R["Read pair R, X25519<br/>R.pub seals, R.priv opens"]
    W["Write pair W, Ed25519<br/>W.priv signs, W.pub verifies"]
  end
  DK["Vault data key DK<br/>random, sealed to R.pub"]
  OBJ["Objects, trees, commits<br/>AES-256-GCM under DK<br/>exactly as today"]
  HEAD["Refs and index<br/>signed by W.priv"]
  ID["Vault id = hash of W.pub<br/>self-certifying"]
  M -- "HKDF" --> R
  M -- "HKDF" --> W
  R --> DK --> OBJ
  W --> HEAD
  W --> ID
  subgraph who["Who holds what"]
    direction TB
    RD["Reader: R.priv + W.pub<br/>reads, verifies, cannot write"]
    WR["Writer: R.priv + W.priv<br/>reads and writes"]
    DP["Depositor: R.pub + a signing key<br/>adds to an inbox, cannot read"]
    HO["Host: ciphertext + W.pub<br/>cannot read or forge"]
  end
  pairs --> who
```

A second way to run a vault, side by side with today's:

```

 R = read pair   (X25519, for encryption)    R.priv decrypts    R.pub encrypts
 W = write pair  (Ed25519, for signatures)   W.priv signs heads W.pub verifies

 vault data key DK (random 32 bytes)
   sealed to R.pub with HPKE (X25519, HKDF-SHA256, AES-256-GCM, RFC 9180)
   every object      = AES-256-GCM(DK, ...)   exactly today's object format
   every ref / index = AES-256-GCM(DK, ...) + an Ed25519 signature by W.priv
 vault id = a hash of W.pub (self-certifying)

```

| Party | Holds | Can | Cannot |
|---|---|---|---|
| **Reader** | `R.priv`, `W.pub` | read everything; check every head was signed by a writer | write: needs `W.priv`, not derivable from what it holds |
| **Writer** | `R.priv`, `W.priv` | read and write |  |
| **Depositor**, write-only | `R.pub`, a signing key the vault accepts for its inbox | add new content readers can open | read anything: needs `R.priv` |
| **Host** | ciphertext, `W.pub` | store, serve, refuse unsigned writes | read; forge a head; it can still withhold or replay old signed states |

**Why a data key, rather than encrypting every object to the read public key.** Public-key encryption is randomised: the same tree encrypted twice gives different bytes. sgit depends on deterministic tree encryption, for de-duplication and for [partial clones](https://sgit.ai/docs/partial-clones.md), whose rebuilt trees must match the whole vault's byte for byte. Sealing one symmetric data key to `R.pub` keeps the object layer unchanged. The public-key cryptography sits in two places only: distribution (the data key never travels as a passphrase) and authority (no write is authorised by a bearer secret).

**What does not change**: the object store, content addressing, trees, sync, merge, partial clones and the command line. Only key creation, how the data key reaches a reader, and what authorises a write. Today's vaults keep working; moving one to the new mode would be an explicit `vault move`.

**The write-only depositor** is the one capability today's design cannot express. A depositor can encrypt but not read, so it cannot read the current tree to change it: write-only means **append**. Each deposit is a commit on the depositor's own inbox branch, with its own data key sealed to `R.pub`, and a writer merges it in. It fits agents handing work to people, submissions, and log or report drops; with sealed files it becomes a drop box where contributors cannot read each other's files.

**Rotation.** A self-certifying vault id means a new write key is a new vault. That is acceptable to start; the cleaner design derives the vault id from an **owner root key** kept offline or in a decryption service, which signs a **writer set**. Removing a writer is then a re-signed set; removing a reader is a new read pair and data key, sealed to the remaining members.

**Algorithms**: Ed25519, X25519, HKDF-SHA256 and AES-256-GCM, all available in the Python `cryptography` library and in current browsers' Web Crypto. Post-quantum: AES-256 content is fine; the exposure is the key exchange that seals the data key, and HPKE has hybrid X25519 plus ML-KEM suites to adopt when browsers support them.

**Effort**, as estimated in the design: about a week for the key code and test vectors; one to one and a half weeks for signed refs and index with verification on every read path; half a week for sealing the data key and `init --pki`; server work by the SG/Send team to accept signed writes; about a week for depositors; two to three weeks for the owner key and writer set. The first three phases give a working mode in which a reader cannot write and a host cannot forge.

## Design 2: sealed files

An inner envelope, sealed to named people's public keys, inside the vault's own encryption. Only the 16-byte file key crosses to wherever the private key lives, including a remote service that can log, approve or refuse each decryption.

**Design 2, Mermaid source**

[rendered image](images/rfc-design2.webp)

```
flowchart LR
  P["A file<br/>plaintext"]
  subgraph inner["Inner layer: sealed to named people"]
    direction TB
    FK["Random file key FK<br/>encrypts the content"]
    ST["FK wrapped once per recipient<br/>public key, in an age v1 envelope"]
  end
  subgraph outer["Outer layer: the vault, as today"]
    O["Read key or DK<br/>hides everything from the host"]
  end
  H["Host<br/>ciphertext only"]
  P --> FK --> ST --> O --> H
  subgraph prov["Where a recipient's private key can live"]
    direction TB
    F["A key file"]
    SSH["An ssh key"]
    HW["Hardware: YubiKey, TPM, Secure Enclave"]
    RS["A remote service that logs,<br/>approves or refuses each unwrap"]
  end
  ST -- "only the 16-byte file key<br/>crosses this line" --> prov
```

An optional layer that works on **either** vault mode, today's symmetric vaults included. The author can say: here is my public key, encrypt this file with it; to read it, ask over there. The files stay in the vault as before; only someone with the private key, or a service that holds it, can read them. Mechanically it is **envelope encryption to recipients' public keys, with decryption delegated**, the pattern of git-crypt, SOPS and age.

| Who | Create a sealed file | Read it | Edit it | Replace or delete it |
|---|---|---|---|---|
| A recipient, with its key or provider | yes | yes | yes | yes |
| A vault writer who is not a recipient | **yes**, sealing needs only public keys | no | no, editing needs reading | **yes, blindly** |
| A vault reader | no | no | no | no |
| The host | no | no | no | withhold or replay, as today |

**The honest twist**: any vault writer can replace a sealed file without being able to read it, because sealing needs only public keys. That is an integrity question, not a confidentiality one, and the design answers it two ways: **signed envelopes**, where the sealer signs the inner envelope and recipients check the signer is allowed for that path, and **per-path author rules** enforced on commit and pull.

**Which files, to whom.** A committed policy file, like `.gitattributes` for git-crypt, pins each recipient's public key by fingerprint, so a change at a key directory cannot silently add someone:

```

# .sgit/seal   (committed; a change to it is itself a signed, reviewable commit)
recipients:
  dinis   = age1...           # published key, fingerprint pinned here
  backup  = age1...           # offline recovery key
  ops     = age1yubikey1...   # hardware-held
seal:
  secrets/**        -> dinis, backup
  finance/*.xlsx    -> dinis, ops, backup
authors:
  secrets/**        -> dinis

```

**The format: age v1, proposed.** It is specified, small and audited; a sealed file can be opened with the stock `age` tool without sgit; and its **plugin protocol** is exactly "the private key lives elsewhere", with plugins for YubiKey, TPM, Secure Enclave and cloud key services. The trade-off: age's payload cipher, ChaCha20-Poly1305, is not in Web Crypto, so the browser would use the reference TypeScript implementation. The alternative is a custom HPKE envelope, pure Web Crypto, without the ecosystem.

**Where the private key lives**, the provider:

| Provider | Where the key is | Notes |
|---|---|---|
| A local identity file | a protected file on the machine | the simple default |
| An ssh key or ssh-agent | the key you already have | age supports ssh recipients natively |
| Hardware | YubiKey, PIV, TPM, Secure Enclave, through age plugins | touch to decrypt; the key cannot be copied |
| A remote service | a team service, a cloud key service, or an SG/Send service | can **log, rate-limit, require approval and revoke** per unwrap, per file; offline means unreadable, by design |

### Where the private key could live today

The remote-service provider is the one that needs outside parts, so we checked thirty services and tools on 9 October 2026, from their own documentation. We asked four questions of each. Can it unwrap a small key with a private key it never releases? Does it log each unwrap, check a policy, or ask a person first? Can anyone seal offline with only the public key, so the service is not needed when writing? Can a browser do that sealing?

**The finding that changes the design.** The format the remote services share is RSA-OAEP-256, not X25519. [AWS KMS](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html), [Google Cloud KMS](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa), [Azure Key Vault](https://learn.microsoft.com/en-us/rest/api/keyvault/keys/unwrap-key/unwrap-key), [HashiCorp Vault](https://developer.hashicorp.com/vault/docs/secrets/transit) and [OpenBao](https://openbao.org/docs/secrets/transit/) Transit, Fortanix, Akeyless, YubiHSM 2 and Nitrokey HSM 2 can all decrypt a key that a client encrypted offline with the downloaded public key, and Web Crypto does RSA-OAEP natively. The three large cloud key services do not offer X25519 decryption: AWS [offers key agreement on NIST curves only](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html), and Google uses X25519 only inside the [X-Wing post-quantum scheme](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms). So X25519, age's own recipient type, stays the right default for keys people hold themselves, and sealed files would also need an `rsa-oaep-256` recipient type to reach a remote service. AWS uses an empty OAEP label and supports no encryption context for asymmetric keys, so the binding of a wrapped key to its vault and file has to live in sgit's own header, not in the service call.

| Option | Each unwrap | Seal offline | Open source, self-hosted | Cost, as published |
|---|---|---|---|---|
| [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html), RSA key | logged in CloudTrail; IAM and key policy; no human approval | yes | no | [$1 per key per month, $0.15 per 10,000 asymmetric requests](https://aws.amazon.com/kms/pricing/) |
| [Google Cloud KMS](https://docs.cloud.google.com/kms/docs/algorithms), RSA or X-Wing key | Cloud Audit Logs; IAM; no human approval | yes | no | [$0.06 per software key version per month, $1.00 to $2.50 in Cloud HSM](https://docs.cloud.google.com/kms/docs/key-management-service) |
| [Azure Key Vault and Managed HSM](https://learn.microsoft.com/en-us/rest/api/keyvault/keys/wrap-key/wrap-key) | [logged as `KeyUnwrap`](https://learn.microsoft.com/en-us/azure/key-vault/general/logging); role-based access; no human approval | yes | no | $0.03 or $0.15 per 10,000 operations; an HSM-backed RSA 2048 key $1 per month |
| [HashiCorp Vault Transit](https://developer.hashicorp.com/vault/api-docs/secret/transit) | [every request audited, and refused if it cannot be logged](https://developer.hashicorp.com/vault/docs/audit); [control groups](https://developer.hashicorp.com/vault/docs/enterprise/control-groups) add approval in Enterprise and HCP | yes | source-available (BSL 1.1); self-hosted | Community edition free |
| [OpenBao Transit](https://openbao.org/docs/secrets/transit/) | audited; policy | yes | [MPL-2.0](https://github.com/openbao/openbao); self-hosted | free |
| [Fortanix DSM](https://support.fortanix.com/docs/fortanix-dsm-group-quorum-policy) | **quorum approval on every private-key operation**, decryption included; audit log | yes, encryption is exempt from the quorum | no | quote, 30-day trial |
| [OpenTDF Key Access Server](https://github.com/opentdf/spec/blob/main/protocol/protocol.md) | policy check before each unwrap; the key is re-encrypted to the client's own key | yes | [BSD-3-Clause-Clear](https://github.com/opentdf/platform); self-hosted | free |
| [Google Workspace client-side encryption key service API](https://developers.google.com/workspace/cse/reference) | each call carries an identity token, an authorization token and a reason, and [the guide says to log all three](https://developers.google.com/workspace/cse/guides/encrypt-and-decrypt-data) | yes | the specification is public; you can build your own | needs Workspace Enterprise Plus or similar |
| age plugins: [YubiKey](https://github.com/str4d/age-plugin-yubikey), [Secure Enclave](https://github.com/remko/age-plugin-se), [TPM](https://github.com/Foxboron/age-plugin-tpm) | PIN, touch or biometry, on the device; no remote log | yes | MIT or Apache-2.0 | [YubiKey 5 NFC, $58](https://www.yubico.com/product/yubikey-5-nfc/) |
| [YubiHSM 2](https://www.yubico.com/product/yubihsm-2-series/yubihsm-2/) or [Nitrokey HSM 2](https://shop.nitrokey.com/shop/product/nk-hsm-2-nitrokey-hsm-2-7), behind a small unwrap service | YubiHSM 2 keeps a hash-chained audit log; approval lives in the service | yes | tools open; Nitrokey is open hardware | $650; €109 |

Three findings beyond the table:

- **Approval of each decryption by a person is rare.** Fortanix's quorum policy and Vault's control groups provide it; otherwise you build it into a service you run, following the [Google client-side encryption](https://developers.google.com/workspace/cse/reference/unwrap) or [OpenTDF](https://github.com/opentdf/spec) pattern. Cloud key services give logs and access rules, not a step that asks someone.
- **We found no age plugin backed by a cloud key service**, in the [awesome-age list](https://github.com/FiloSottile/awesome-age) or in searches, although age's [plugin design names cloud key services as a purpose](https://github.com/FiloSottile/age/releases/tag/v1.1.0). One written for sgit would also serve every age user.
- **Some do not fit.** Services that only encrypt symmetrically (AWS external key stores, Google Cloud EKM, Infisical's KMS, passkeys through FIDO2 PRF) must be online to seal. Services where the vendor, not the named person, holds the right to decrypt (Evervault, Skyflow, Basis Theory) answer a different question. Threshold's TACo, a network of nodes that release key fragments when conditions are met, has a code repository marked [no longer active](https://github.com/nucypher/taco-web), with [a relaunch planned for Q3 2026](https://docs.taco.build/).

**Our three best fits for each kind of user:**

|  | First | Second | Third |
|---|---|---|---|
| **A person or a small team** | age X25519 keys, with a YubiKey, Secure Enclave or TPM plugin for a key that cannot be copied | one RSA key in AWS or Google Cloud KMS: about $1 a month, every unwrap logged | OpenBao Transit, optionally on a YubiHSM 2 or Nitrokey HSM 2 |
| **A company that wants every decryption approved and logged** | Fortanix DSM with a quorum policy | Vault Enterprise or HCP Vault, with control groups | an unwrap service of your own, on the Google client-side encryption or OpenTDF pattern, in front of a cloud key service or an HSM |
| **Open source and self-hosted only** | OpenBao | OpenTDF with its Key Access Server | age with open hardware, behind a small unwrap service |

**The interface this suggests.** Sealing stays offline and native in sgit, in Python and the browser, for a few recipient types: X25519, RSA-OAEP-256, and later age's X-Wing type. Unsealing becomes one call with four back ends: a local key; the age plugin protocol, so existing hardware plugins work unchanged; a direct call to a cloud key service or Vault; and an HTTP unwrap endpoint for approval flows, which takes the wrapped key, the vault and file, a reason and identity tokens, logs them, and returns the file key re-encrypted to a temporary key of the client's, or "pending" until someone approves. Google Cloud KMS's X-Wing keys and age's post-quantum recipient may fit together, which would give a post-quantum key held by a cloud service; that is untested, and needs a test-vector run before anything depends on it.

**Moving capabilities, not passphrases.** The same envelope can carry a vault's read or write capability to a person: `sgit share --to dinis` would seal it to Dinis's published key, so no passphrase passes through chat, the command line or shell history.

**What it protects, and what it does not.** It keeps sealed content from the host, from vault members who are not recipients, and from anyone who later obtains the vault's read key. It does not hide file names, paths, sizes or history from vault members; a recipient removed later keeps what was sealed to them before; a non-recipient writer replacing a file is detected with signed envelopes, not prevented on the host; and it is only as strong as the provider.

**Effort**, as estimated: about a week for an age reader and writer; one to one and a half weeks for the policy, sealing on commit and opening on checkout; about a week for the providers, plus the service side for a remote one; half a week each for signed envelopes and author rules, and for `sgit share`; the web UI's part with the web team.

## How the pieces fit

|  | Closes the forgery gap? | Changes the vault format? | Main new capability |
|---|---|---|---|
| **Writer signature** on today's vaults | yes, for integrity | small: refs and index carry a signature | the step both designs share |
| **Native PKI mode** | yes: heads must be signed by a key readers do not have | yes, as a second mode; today's vaults unchanged | write-only depositors; no bearer write key |
| **Sealed files** | no, a different problem | no: a layer over any vault | content only named people can read, with the private key anywhere |

## Prior art

None of this is new, and it should not be. **Tahoe-LAFS** separates read and write capabilities for mutable files in nearly this shape. **Hypercore and Dat** use a key pair as a feed's identity and write capability. **git-crypt** and **SOPS** seal files inside a git repository to people's keys. **age** and its plugins put the decryption wherever the key lives. HPKE is [RFC 9180](https://www.rfc-editor.org/rfc/rfc9180). The aim is to bring these known shapes into a vault that is already encrypted, versioned and served by an untrusted host.

## Questions for reviewers

Comments on anything are welcome. These are the questions where an outside view would most change the design.

**Native PKI vault mode**

1. **Two key pairs**, X25519 for reading and Ed25519 for writing. Is there a simpler construction that gives readers no write power and writers no derivable read power, and still works in browsers?
2. **A data key sealed to the read public key**, rather than encrypting each object to it, keeps encryption deterministic and preserves de-duplication and partial clones. Is that the right trade-off, or does it lose a property you care about?
3. **Vault id from the write public key**, self-certifying. Or from an owner root key that signs a writer set from day one, which makes rotation easier and the design more complex?
4. **Write-only depositors** append to an inbox branch with their own data key. Is append-only enough for your use cases: agents handing work to people, submissions, log drops?
5. **Freshness.** Signed sequence numbers and timestamps let a client flag a stale head, but a host can still serve an old signed state to someone who never saw a newer one. Is a transparency log or a witness worth the complexity?
6. **Capability strings.** Random 32-byte seeds only, for agents and machines, or also a passphrase form for people, as today?

**Sealed files**

1. **age v1 or a custom HPKE envelope?** age brings a specified format, stock tools and plugins for hardware and cloud key services, with a non-Web-Crypto cipher in the browser. A custom envelope stays pure Web Crypto and gives up the ecosystem.
2. **The working copy.** Should a file the clone can open be written in plaintext, as git-crypt does, or stay sealed on disk, with `sgit cat` and `sgit open` to read it?
3. **Integrity of sealed paths.** Are signed envelopes plus per-path author rules the right answer, and should they be in the first version?
4. **A remote decryption service.** Only the file key crosses the boundary, and the service can log, approve or refuse each decryption. Which first provider would you use: a hosted unwrap service, a cloud key service, or hardware? And should sealed files carry an `rsa-oaep-256` recipient type beside X25519, since that is the format the remote services share? [The landscape above](#providers) is our starting point.
5. **Leaks that remain.** Names, paths, sizes and history stay visible to vault members. Is that acceptable, or do you need sealed names or padding too?

**Both**

1. **Two vault modes side by side.** Is the extra surface worth it, or should the PKI mode eventually replace the symmetric one?
2. **Post-quantum.** Content is AES-256; sealed data keys would move to a hybrid X25519 plus ML-KEM suite once browsers support it. Is waiting reasonable?
3. **Anything we have missed** in the threat model: actors, assets, or attacks.

## How to comment

[Open an issue on the sgit repository](https://github.com/SGit-AI/SGit-AI__CLI/issues/new?title=RFC%200001%3A%20) with a title starting "RFC 0001:", and the question number if you are answering one; or write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai). Disagreement is the point. Comments will be summarised on this page, with what changed in the design because of them.

*RFC 0001, from the design documents written by the sgit CLI agent for Dinis Cruz on 9 October 2026, who has editorial responsibility for the proposals. Prepared for this site, with the diagrams, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session; the landscape of key services was researched for this page on 9 October 2026 from the providers' own documentation. Nothing described here is implemented. Effort figures are the designers' estimates.*

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#rfc-0001-public-key-cryptography-for-sgit)

### Builds on

- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.

### Continued by

- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [rfc-0001-public-key-cryptography-for-sgit.jpg](banners/rfc-0001-public-key-cryptography-for-sgit.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/rfc-0001-public-key-cryptography-for-sgit.html)*
