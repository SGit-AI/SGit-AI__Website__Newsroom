# The passkey opens the vault: touch a passkey, and a master vault for every user, with no server of ours, no account and no email, sgit.ai

> The missing piece of the client-side puzzle is a user who can open their own vaults on any device, in a few seconds, with nothing to remember and nothing to sign up for. This is the design. A passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site, and from those bytes the browser computes the key of a small door vault, which holds the key of your master vault, which holds the keys of everything else, starting with your newsroom vault. There is no sign-in: the page makes and uses the passkey through the browser's own API, with no Google app, no OAuth and no server, and it never learns your email or your name. The question I could not answer, where the encrypted vault key is stored, has a simple answer: nowhere. sgit vault keys are made in the client, so the door's key and its id can be computed from the passkey on any device, before anything is fetched, and there is no chicken and egg. A recovery code makes a second door to the same master. PRF is now supported by Google Password Manager, iCloud Keychain, Windows Hello and Firefox. The unlock costs up to six key derivations, measured. The first part is the technical design and the brief for the MVP on newsroom.sgit.ai, end to end; the second is what it enables: accounts with no server and no identity, for this site and for any other.

*Source: <https://newsroom.sgit.ai/articles/the-passkey-opens-the-vault.html> · sgit.ai v0.7.61 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The passkey opens the vault: touch a passkey, and a master vault for every user, with no server of ours, no account and no email

# The passkey opens the vault: touch a passkey, and a master vault for every user, with no server of ours, no account and no email

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.2.0, 3 versions](versions/the-passkey-opens-the-vault.md) · [sgit.ai v0.7.55](https://sgit.ai/admin/versions.md) · passkeyswebauthnprfvaultskey-managementgoogle-sign-inclient-sidenewsroomarchitecturebriefsecretsarticle

***Abstract:** The missing piece of the client-side puzzle is a user who can open their own vaults on any device, in a few seconds, with nothing to remember and nothing to sign up for. This is the design. A passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site, and from those bytes the browser computes the key of a small door vault, which holds the key of your master vault, which holds the keys of everything else, starting with your newsroom vault. There is no sign-in: the page makes and uses the passkey through the browser's own API, with no Google app, no OAuth and no server, and it never learns your email or your name. The question I could not answer, where the encrypted vault key is stored, has a simple answer: nowhere. sgit vault keys are made in the client, so the door's key and its id can be computed from the passkey on any device, before anything is fetched, and there is no chicken and egg. A recovery code makes a second door to the same master. PRF is now supported by Google Password Manager, iCloud Keychain, Windows Hello and Firefox. The unlock costs up to six key derivations, measured. The first part is the technical design and the brief for the MVP on newsroom.sgit.ai, end to end; the second is what it enables: accounts with no server and no identity, for this site and for any other.*

The key chain. The passkey's PRF output derives a door vault, the door holds the master vault's key, and the master holds the keys of everything else. Nothing secret is stored anywhere to be fetched, and the vault server sees ciphertext at every step.

This is the missing piece of the puzzle. In [I miss it, so it is working](i-miss-it.md) I described the feature I miss: the newsroom on every device, in sync, through my own encrypted vault. In [No server, by design](no-server-by-design.md) I listed identity as one of the last things that still seemed to need a server. This article joins the two, in detail.

The experience I want is simple. I open newsroom.sgit.ai in a new browser. I am asked to touch my passkey. And my reading account opens, the same as on every other device, because it is now in a vault only I can open. Two steps, one of them a gesture, no server of ours anywhere, and nothing to sign up for.

I had one question I could not answer: where is the vault key kept? The short answer, after the research, is that it is not kept anywhere. It is computed. The rest of this article is why that works, the design end to end, and what it makes possible for every other site we run.

## In short

- **No sign-in, no account, no email.** The page makes and uses the passkey itself, through the browser's WebAuthn API: no Google app, no OAuth loop, no server. The reader's passkey provider syncs it between their devices; the site never learns who they are.
- **That is a privacy feature, with a price.** We cannot email the reader, and there is no "forgot password": recovery is the recovery code and a second passkey. A purchase has no identity to hang on. I think it is the right trade.
- **The passkey is what opens the vault.** With the WebAuthn PRF extension, a passkey returns 32 bytes that only your authenticator can produce, for this site, and the same bytes on every device the passkey syncs to.
- **Where is the vault key stored? Nowhere.** sgit vault keys are made in the client, a passphrase and a vault id. So the browser computes a door vault's key and id from the PRF bytes, opens it, and finds the master vault's key inside. No chicken and egg, no new storage, only vault APIs.
- **One master vault per user.** It holds the keys of your other vaults (the newsroom vault first), your access key, your key pair and the list of your doors.
- **Every passkey is a door, and so is a recovery code.** An iPhone and a Windows laptop with different passkeys get two doors to the same master. A 128-bit recovery code, shown once, is a third. Lose them all and no one, including us, can open it.
- **Support is good enough to build on, and where the passkey lives decides what the reader gets.** PRF works in Google Password Manager, iCloud Keychain (Safari 18 and macOS 15), Windows Hello (since February 2026) and Firefox. A synced provider or a hardware key gives the same newsroom on every device; a clean browser with neither gives one device plus the recovery code, and Chrome's own store returns no PRF bytes at all, so the page checks at creation and offers a ladder of alternatives.
- **One rule the design depends on:** the whole origin loads no third-party scripts, on any page, because browser storage is per origin and a script on one page can read what another page kept. The vault code is vendored into the reader repository, not loaded from anywhere else.
- **It is not just for the newsroom.** Every site we build needs the same thing: an account with no server, data nobody else can read, on every device. This is that, as a pattern.

## Part one: the design

### What each piece actually gives you

It helps to separate the pieces, because they are easy to blur.

| Piece | What it gives the page | What it does not give |
|---|---|---|
| **Sign in with Google** (later, optional, on its own origin) | Continuity: a stable account id for support, a Drive backup, a reference for purchases | Any key. It is not in the MVP and not needed to open anything |
| **A passkey for this site** | A gesture (touch, face, PIN), a signature, and with PRF, 32 bytes computed from a secret the authenticator keeps for this site and this passkey | The bytes to anyone but the page on this site that asked, after the gesture |
| **The passkey provider** | Sync: Google Password Manager across your Chrome and Android devices, iCloud Keychain across your Apple devices, or none (a hardware key) | Anything about what the bytes are for |
| **sgit** | Vault keys made in the client (a 24-character passphrase and an 8-character vault id), read and write keys derived from them, ciphertext on the server | A way to find a vault you have no key for |
| **The access key** | The right to create vaults and write to them on the vault server, the thing people will buy | Any way to read a vault |

One clarification that matters. What people call "the Google passkey" is a passkey **for this site**, registered by this page under this site's name, which your provider stores and syncs: Google Password Manager if you use Chrome, iCloud Keychain on Apple devices. It is not the passkey you use to sign in to Google, and a website cannot get PRF bytes from that one. There is no sign-in in this flow at all: the page registers a discoverable credential with a random user handle, and the only login involved is the one you already have with your passkey provider, which syncs it. The site learns a credential id, a public key and, after your gesture, 32 bytes. Not your email, not your name, not which account syncs it.

### Where the vault key lives: nowhere

The places the key could live, and how you would find each before you could open it. Deriving the door from the passkey needs nothing to be found; the stored options become backups.

Every option for storing an encrypted vault key has the same problem: you have to find the encrypted key before you can open it, so it has to live somewhere you can reach with only what you have at that moment, which is your Google sign-in and your passkey.

- **Inside the vault itself:** you need the key to read the vault. The chicken and the egg.
- **An SG/Send transfer:** if the transfer id is assigned on upload, you need to have stored the id somewhere first.
- **Google Drive's app-data folder:** this is the "application data" I had in mind. It is a private, hidden folder per app in the user's own Drive, reached with the `drive.appdata` scope, which Google lists as recommended and non-sensitive. It works from the browser, with the user present for each token. It needs Google sign-in, which the MVP does not have, and it only helps if what it holds is wrapped under something other than the passkey: wrapped under the recovery code, it is a second copy of the recovery door, useful if the vault server loses data, and no help for a lost key. A later **availability backup**, not the main path.
- **A bucket keyed by the account id:** the design [secrets.sgit.ai](https://secrets.sgit.ai/) has, with Identity Platform and Cloud Storage. It works, and it is a cloud project per environment.
- **Inside the passkey (`largeBlob`):** support is too uneven to depend on.

And then the option that needs none of it. **sgit vault keys are generated in the client**: a random passphrase and a random vault id, and `sgit init` accepts a key it is given. So instead of generating a door vault's key at random and storing it, the browser **computes** it from the PRF bytes: the passphrase, and the vault id, with HKDF. On any device where the passkey is available, the same gesture gives the same bytes, the same door id and the same door key. The browser knows where to look and how to open it before it has fetched anything. The door holds one thing, the master vault's key, which is random and made once. The master holds everything else.

So the answer to my question: the vault key is not stored, it is derived; the master key is stored, inside a vault that only the passkey can find; and Google's app-data folder can keep a backup copy, encrypted, for the day something goes wrong.

### The derivation

For the newsroom MVP, with the relying party ID `newsroom.sgit.ai`:

1. **The PRF input** is a fixed, public value: `SHA-256("newsroom.sgit.ai/door/v1")`. An input is not a secret; only the authenticator can turn it into the 32 bytes.
2. **The door seed** is `HKDF-SHA256(ikm = PRF bytes, salt = SHA-256("newsroom.sgit.ai"), info = "sgit/door/v1")`.
3. **The door's passphrase and vault id** are two more HKDF outputs from the seed. sgit accepts any printable ASCII passphrase up to 256 characters, so the passphrase is the hex of 32 bytes (`info = ".../passphrase"`), keeping all 256 bits. The vault id has to be lowercase letters and digits, 4 to 24 of them, so 8 characters are drawn from a third output (`info = ".../id"`) with rejection sampling, so that no character is favoured.
4. **The door vault key** is the sgit vault key made of those two, and from there, sgit's own derivation gives the read and write keys, exactly as the command line does: PBKDF2-HMAC-SHA256 at 600,000 iterations, once for the read key and once for the write key. That is the cost of this design. Door, master and newsroom vault need up to six derivations; measured in headless Chromium on a four-core machine, one takes about 105 ms and six run together about 640 ms, and a phone is several times slower, so a cold unlock can spend two to four seconds deriving keys before it fetches anything. The brief measures it on a phone, derives each vault's keys once per session, runs them in a worker, and derives a write key only when there is something to write.
5. **The recovery door** is the same, with the recovery code in place of the PRF bytes: 26 characters of base32, 128 bits, made by the page and shown once. It is long so that it needs no password stretching, as in the secrets.sgit.ai keyring design.
6. **Collisions** are not a practical worry with 36⁸ possible ids, but the page checks: a derived id that already holds something it cannot open is skipped, with a counter in the HKDF info.

The browser and the command line must agree byte for byte, so the brief includes test vectors: the same inputs through the browser code and through sgit in Python, with the same keys out.

### What is in each vault

- **A door vault:** one file, the master vault's key, and what kind of door it is (which passkey, or the recovery code).
- **The master vault:** the keys of your other vaults, by site; your access key; your key pair (the public key in the clear, the private key as a JWK); the list of your doors, so a lost passkey's door can be retired; and your Google account id, so the page can tell you if you have signed in as someone else.
- **The newsroom vault:** one log per device, appended, never edited: pages read and how far, ratings, personas, the reading list, notes, receipts by payment reference. Every device computes the same state from all the logs, as described in [I miss it](i-miss-it.md).

### The flows

The first run, a new device, and adding a passkey or recovering. Every step runs in the browser, against the user's passkey provider for the gesture, and the vault server for ciphertext.

**First run.** Create a passkey for the site with `prf` enabled; if the authenticator cannot do PRF, the page says which kinds can and offers another. Touch it: the PRF bytes give the door. Generate the master key, the newsroom vault key, a key pair and a recovery code. Paste the access key. Create the door, the master, the newsroom vault and the recovery door. Move the reading account from the browser's storage into the newsroom vault. Show the recovery code once, behind "I have written it down".

**A new device.** Touch the passkey, synced to this device or used from a phone by QR. The PRF bytes give the same door, the door gives the master, the master gives the newsroom vault. Reading needs no access key; the access key comes out of the master, so this device can write as well. Merge this browser's reading into its own log.

**A second provider.** An iPhone with iCloud Keychain and a Windows laptop with Windows Hello have different passkeys. While unlocked on one, register the other: its PRF bytes make a second door to the same master.

**Lost a passkey.** Type the recovery code; it derives the recovery door; register a new passkey; retire the old door in the master's list.

**Signing out and locking.** Keys exist only in the page's memory: cleared on sign-out, after a period of inactivity, and when the page is closed. The browser's own copy of the reading account stays as it is today.

### Security, said plainly

- **What each party sees.** The vault server: ciphertext, sizes, times and ids that look random. Google: nothing, in the MVP. Your passkey provider: that a credential exists for this site. Only this page, in your browser, after your gesture, holds the PRF bytes and the keys.
- **The origin loads no third-party scripts, on any page.** Storage is per origin, so a script on a sign-in page could read what the account page keeps. If sign-in with Google is added later, it runs on an origin of its own and hands back an account id; the newsroom's pages load only code from the reader repository, with the vault code vendored into it rather than loaded from the vault web app or tools.sgraph.ai.
- **The relying party ID is a trust boundary.** A passkey for `sgit.ai` would work on every `*.sgit.ai` site, and any of those sites could ask it for PRF bytes, so every one of them would have to be as strict as the strictest. The MVP uses `newsroom.sgit.ai` exactly, as secrets.sgit.ai uses its own host. Sharing across sites is part two.
- **Passkeys cannot be phished across sites.** They are bound to the site's name; a look-alike domain gets nothing.
- **Losing everything is final.** Every passkey and the recovery code gone means no one can open the vaults. That is the property that makes the design worth having, and the first run says so before it shows the code.
- **Availability is not secrecy.** The vault server could delete or roll back ciphertext. It cannot read it. The local copy and the Drive backup cover the first; nothing is needed for the second.
- **Agents do not have passkeys.** An agent that should read part of a user's data gets a read key for one vault, given by the user from the master, never the master itself.

### Where PRF works today

As of October 2026, from vendor documentation and published tests (see the sources):

| Passkey provider | PRF |
|---|---|
| Google Password Manager (Chrome, Edge and Samsung Internet; Android) | Yes, by default; desktop Chrome from version 136 |
| iCloud Keychain (Safari 18, macOS 15) | Yes |
| Windows Hello | Yes, since the February 2026 update to Windows 11 |
| Firefox | Yes, on macOS from version 139 and Windows from version 148 |
| Hardware security keys | Yes through `hmac-secret`, but not with YubiKeys in Safari |
| Chrome's own profile authenticator | No |

The page checks `prf.enabled` when it creates the passkey, and never guesses: if it is false, it says so and offers another authenticator or the recovery code.

### What happens in a clean browser

The table above is about browsers. The question that matters to a reader is about devices: will the newsroom I opened on my laptop be the same one on my phone? That depends on where the passkey lives, which is a choice the reader made long before they met this site, usually without noticing.

Where a passkey can live, what each place needs, whether the passkey travels, whether it can return the PRF bytes, and what that means for the reader. The ladder below the table is what the page offers when PRF is off.

| Where the passkey lives | Needs | Travels? | PRF | What the reader gets |
|---|---|---|---|---|
| **Google Password Manager** (Chrome signed in, Android) | A Google account | Yes, to every device signed in to it | Yes | The same newsroom everywhere |
| **iCloud Keychain** (Safari, iPhone, iPad, Mac) | An Apple ID | Yes, across Apple devices | Yes, Safari 18 and macOS 15 | The same newsroom on every Apple device |
| **Windows Hello** (Windows 11) | The device; a Microsoft account to sync | Device-bound, unless synced | Yes, since February 2026 | This PC, or every PC on the account |
| **A hardware key** (YubiKey and others) | The key, and its PIN | Yes, wherever the key is plugged in | Yes, through `hmac-secret`; not with YubiKeys in Safari | No account anywhere; a few dozen passkeys per key |
| **Your phone, by QR** (the hybrid flow) | A passkey on the phone, in its own provider | Yes, one scan at a time | Where the phone's provider does | A clean laptop opens with the phone beside it |
| **Chrome's own profile store** (a clean Chrome, no provider) | Nothing | No: this browser, on this computer | No, in 2026 tests | Signs, returns no bytes: the door cannot be derived |

So the rule, in one line: **the same newsroom on every device needs a synced provider or a hardware key in your pocket.** A clean browser with neither gives you this device, plus the recovery code. A passkey made there still works, as a passkey; it is stored by the device, tied to that browser profile on that computer, and deleted with it. The catch for this design is the last row: Chrome's own store, used when there is no provider (a clean Chrome on Linux, or on a Mac with iCloud Keychain off), signs but returns no PRF bytes in 2026 tests, so the door cannot be derived there at all.

Two things follow. The page learns which case it is in at creation, from `prf.enabled`, and never guesses. And when PRF is off, it offers a ladder, in this order: sign in to a provider, so the passkey syncs from now on; use your phone by QR, one scan at a time; plug in a hardware key; or stay on this device, where the browser's own copy keeps working and the recovery code is the way back. That is a real limitation of PRF today, not of the design, and the article would be dishonest without it. One caveat on the Chrome-profile row: it comes from a vendor's published tests, so the brief includes a five-minute check on a clean profile before anyone depends on it.

### The brief for the MVP

*For the session that runs newsroom.sgit.ai. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Dinis decides what ships, and is the first user.*

1. **No sign-in.** The first screen is the passkey. Google sign-in is a later phase, on its own origin, and only for what it is good for: continuity for support, a Drive backup, a reference for purchases.
2. **The passkey**: create with `rp.id = newsroom.sgit.ai`, a resident key, user verification required, `extensions.prf`; get with the fixed PRF input; check `prf.enabled`. When it is false, the ladder: sign in to a provider, your phone by QR, a hardware key, or this device only with the recovery code, each explained in one line.
3. **The derivation** in part one, with test vectors shared with the sgit command line.
4. **The vaults**: door, master, newsroom and recovery door, created with the access key, using the browser code that already reads and writes vaults, taken from the [vault web app](https://vault.sgraph.ai/) and [tools.sgraph.ai](https://tools.sgraph.ai/) and vendored into the reader repository.
5. **The move**: the reading account from the browser's storage into the newsroom vault, as the first device's log.
6. **The right-hand side**: once open, show the vault: the master's list of vaults and doors, and the newsroom vault's contents, so the user can see what is kept and where.
7. **Tests**: Chromium's virtual authenticator with PRF in the build (secrets.sgit.ai found it works in Chromium 141); the first run, a new device and the recovery code, end to end; a clean Chrome profile with no provider, to confirm what its own store returns for `prf.enabled` and that the ladder appears; two devices editing offline and agreeing; a [synthetic reader](how-to-run-synthetic-users.md) who has never heard of a vault key.
8. **Not in the MVP**: Google sign-in, the Drive backup, sharing across sites, anything on a server of ours.

The acceptance test is the experience in the second paragraph of this article: a new browser, a gesture, and my reading account, on my iPhone, my iPad, my laptops and my iMac.

## Part two: what this enables

Once these dots are connected, we have something we did not have before: an end-to-end path from a login with a second factor to a vault, entirely in the browser, on commodity pieces. And just about every site and project we build needs exactly that.

- **Accounts with no server, and no identity.** A static site gets a user who can open their own data on any device, and keep it private from the site's operator. No account database, no password, no email, no back end.
- **Data the operator cannot read.** Not as a promise in a privacy policy, but as a property: the vault server holds ciphertext, and the keys are on the user's devices.
- **One master, many vaults.** The newsroom vault is the first. The same master can hold the key to [secrets.sgit.ai](https://secrets.sgit.ai/)'s keyring, a RiskMandate customer's policies, the memory of an agent the user runs, or the notes a reader sends to the newsroom.
- **Sharing without shared secrets.** The key pair in the master is what [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) needs: give someone a vault key by encrypting it to their public key, with no secret sent in a chat.
- **One account across sites.** Two ways, later. A key hub, such as secrets.sgit.ai, holds the master and hands a site only the key to its own vault, after the user approves it in a pop-up, the way a wallet connects to a site. Or, across different domains, WebAuthn's Related Origin Requests let one passkey work on a list of related sites, in Chrome and Safari today.
- **For anyone else.** None of this is specific to us. Any static site, on any host, could use Google sign-in, a passkey with PRF and a vault, and give its users the same thing. I would like it to become a small, open component, the way [SG Meter](pay-after-you-read.md) is for reading.

This is why I think it matters more than a login feature. It is the moment the client-side pattern stops needing anyone's server for identity and storage, and becomes something other sites can use.

## What this does not claim

- **None of it is built yet.** The pieces exist (sgit, vaults, the vault web app, passkeys with PRF, the secrets.sgit.ai design and its passkey lab), and this is the design that joins them.
- **The support table is a snapshot.** It is from vendor documentation and published tests in 2026, and some of it, Firefox and Microsoft's own password manager in particular, is still moving.
- **Deriving the door is a choice with a cost.** A door is lost with its passkey; the recovery code and a second passkey are what cover it.

If you build sites that need accounts without a back end, or you work on passkeys or password managers and want to try this with us, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded on 11 October 2026, asking for the design and for research into what a passkey gives a website and where an encrypted vault key could be kept; written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The design builds on secrets.sgit.ai's published design ([how it works](https://secrets.sgit.ai/how-it-works/), [the keyring format](https://secrets.sgit.ai/keyring/), [passkeys, WebAuthn and PRF](https://secrets.sgit.ai/learn/passkeys/) and [keys](https://secrets.sgit.ai/learn/keys/)), and on how sgit generates and parses vault keys in the client (`generate_vault_key` and `parse_vault_key` in the sgit command line); the unlock cost was measured with WebCrypto PBKDF2 in headless Chromium on 11 October 2026. The research: Corbado, [Passkeys and WebAuthn PRF for end-to-end encryption (2026)](https://www.corbado.com/blog/passkeys-prf-webauthn) and [WebAuthn L3 support in credential managers](https://www.corbado.com/blog/webauthn-l3-credential-manager-support); Yubico, [Developer's guide to PRF](https://developers.yubico.com/WebAuthn/Concepts/PRF_Extension/Developers_Guide_to_PRF.html); Mozilla, [support for the WebAuthn PRF extension](https://bugzilla.mozilla.org/show_bug.cgi?id=1863819); Chromium, [intent to ship the PRF extension](https://groups.google.com/a/chromium.org/g/blink-dev/c/iTNOgLwD2bI); web.dev, [passkey reuse across sites with Related Origin Requests](https://web.dev/articles/webauthn-related-origin-requests); Google, [choosing Google Drive API scopes](https://developers.google.com/workspace/drive/api/guides/api-specific-auth) and [authorising for the web](https://developers.google.com/identity/oauth2/web/guides/overview). Related articles: [I miss it, so it is working](i-miss-it.md), [No server, by design](no-server-by-design.md), [Where the vault keys live](where-the-vault-keys-live.md), [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) and [How to run synthetic users](how-to-run-synthetic-users.md).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-passkey-opens-the-vault)

### Builds on

- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.

### Continued by

- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 77 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=77)

**Posting this article on LinkedIn?** The cover is [the-passkey-opens-the-vault.jpg](banners/the-passkey-opens-the-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-passkey-opens-the-vault.html)*
