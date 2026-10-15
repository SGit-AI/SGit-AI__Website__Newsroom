# The passkey opens the vault: a door per path, a master vault for every user, and no server of ours, sgit.ai

> The missing piece of the client-side puzzle is a user who can open their own vaults on any device, in a few seconds, with nothing to remember and nothing to sign up for. This is the design, in its third version, and this one has been tested. A passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site, and from those bytes the browser computes the key and the address of a small door vault, which holds the key of your master vault, which holds the keys of everything else: your reading vault, the read keys you have been given, your access key, and your key pairs, which are generated at random and never derived from the passkey. A review on 11 October took the door out of the design as a layer too many; a test on newsroom.sgit.ai on 11 and 12 October put it back, for a reason the review could not have known. One Google Password Manager passkey gave the same bytes on a Mac and an iPhone through the provider on each device, and the derivation agreed with sgit's Python byte for byte; the same passkey, answering a QR code from an iPad and from that same Mac, gave a different set of bytes, consistently, with the same credential id. Apple's forums report the same for iCloud Keychain since late 2024. So the claim is narrower than I wrote: the same passkey gives the same bytes through the same kind of path. The unit of the design is the path, not the passkey: a door per set of bytes, each recording where it came from, added in a normal first-week step that moves no key through a person, with the recovery code as the way in where no door opens yet, and an unknown door address meaning no door here yet, never an error. The platform path, which an iCloud Keychain passkey gave identically across a Mac, an iPad and an iPhone in Safari and Chrome, is the common case and works.

*Source: <https://newsroom.sgit.ai/articles/the-passkey-opens-the-vault.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The passkey opens the vault: a door per path, a master vault for every user, and no server of ours

# The passkey opens the vault: a door per path, a master vault for every user, and no server of ours

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · updated 2026-10-12 · [article v1.4.0, 5 versions](versions/the-passkey-opens-the-vault.md) · [sgit.ai v0.7.64](https://sgit.ai/admin/versions.md) · passkeyswebauthnprfvaultskey-managementpkiclient-sidenewsroomarchitecturebriefsecretslabarticle

***Abstract:** The missing piece of the client-side puzzle is a user who can open their own vaults on any device, in a few seconds, with nothing to remember and nothing to sign up for. This is the design, in its third version, and this one has been tested. A passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site, and from those bytes the browser computes the key and the address of a small door vault, which holds the key of your master vault, which holds the keys of everything else: your reading vault, the read keys you have been given, your access key, and your key pairs, which are generated at random and never derived from the passkey. A review on 11 October took the door out of the design as a layer too many; a test on newsroom.sgit.ai on 11 and 12 October put it back, for a reason the review could not have known. One Google Password Manager passkey gave the same bytes on a Mac and an iPhone through the provider on each device, and the derivation agreed with sgit's Python byte for byte; the same passkey, answering a QR code from an iPad and from that same Mac, gave a different set of bytes, consistently, with the same credential id. Apple's forums report the same for iCloud Keychain since late 2024. So the claim is narrower than I wrote: the same passkey gives the same bytes through the same kind of path. The unit of the design is the path, not the passkey: a door per set of bytes, each recording where it came from, added in a normal first-week step that moves no key through a person, with the recovery code as the way in where no door opens yet, and an unknown door address meaning no door here yet, never an error. The platform path, which an iCloud Keychain passkey gave identically across a Mac, an iPad and an iPhone in Safari and Chrome, is the common case and works.*

The key chain, after the test. The passkey's PRF output, by one path, computes a door; the door holds the master vault's key and a record of where it came from; the master holds the keys of everything else and the list of its doors. A different path to the same passkey can give different bytes, and gets a door of its own.

This is the missing piece of the puzzle. In [I miss it, so it is working](i-miss-it.md) I described the feature I miss: the newsroom on every device, in sync, through my own encrypted vault. In [No server, by design](no-server-by-design.md) I listed identity as one of the last things that still seemed to need a server. This article joins the two, in detail.

It is the third version, and the first with a test behind it. The first version had a door vault between the passkey and the master. A review on 11 October asked where the requirement for that layer was, found none in our use case, and took it out. On 11 and 12 October the newsroom built [a lab](https://newsroom.sgit.ai/passkey/) with every step of the design as a card you can press, ran it on a Mac, an iPhone and an iPad, and found the requirement: the same passkey, reached two different ways, gives two different sets of bytes. The door is back, and it is now the unit of the design. What changed is listed at the end, and the lab's own [note](https://newsroom.sgit.ai/admin/notes/2026-10-12__one-door-per-passkey-path.md) has the runs.

The experience I want is unchanged. I open newsroom.sgit.ai in a new browser. I am asked to touch my passkey. And my reading account opens, the same as on every other device, because it is now in a vault only I can open. Two steps, one of them a gesture, no server of ours anywhere, and nothing to sign up for.

## In short

- **You are already signed in, somewhere else.** On a Mac you are signed in to Apple, in Chrome to Google, on Windows to Microsoft, and that is where your passkeys live. The site does not need you to sign in to it. It asks the passkey store you already use, and the vault goes wherever that store goes.
- **The passkey is what opens the vault, through a path.** With the WebAuthn PRF extension, a passkey returns 32 bytes that only your authenticator can produce for this site. The same passkey gives the same bytes on every device it syncs to, **through the same kind of path**. A different path, a phone answering a QR code instead of the provider on the device, can give different bytes, and in our test it did.
- **Where is the door key stored? Nowhere.** sgit vault keys are made in the client, a passphrase and a vault id. So the browser computes the door's key and address from the PRF bytes, opens it, and finds the master vault's key inside. No chicken and egg, no new storage, only vault APIs. The lab did this against a real vault server and opened the door again.
- **A door per set of bytes.** Every door holds the master's key and records its provider, its path, its credential id, the device and the date. The master lists its doors with their keys, so any door can be retired from any other.
- **Adding a door is a normal first-week step, and no key passes through a person.** While unlocked on a device where both paths run, a Mac with Chrome, ask for the bytes by the other path and the page writes the new door from memory. Where no device has both paths, the recovery code opens the recovery door and the new door is written from there.
- **"No door here yet" is not an error.** A device that derives an address and finds nothing is on a path that has no door. The page says so and offers the two ways in.
- **The master is the keyring, and the passkey is a lock, not an identity.** The master holds the keys of your reading vault and your notes vault, the read keys you have been given, your access key, and your key pairs, which are generated at random and never derived from the passkey. Change a lock and the identity is untouched.
- **Several passkeys for several roles are several masters.** An admin passkey on a hardware key and a reader passkey in the cloud open different masters, chosen in the provider's own picker. Keys move between masters by copying; a door is retired by deleting its one file, never by destroying its address.
- **Support is good enough to build on, and where the passkey lives decides what the reader gets.** PRF works in Google Password Manager, iCloud Keychain, Windows Hello and Firefox. The platform path is the common case: an iCloud Keychain passkey gave the same bytes on a Mac, an iPad and an iPhone, in Safari and in Chrome. A clean browser with no store gives one device, and Chrome's own store returns no PRF bytes, so the page checks at creation and offers a ladder.
- **One rule the design depends on:** the whole origin loads no third-party scripts, on any page, because browser storage is per origin and a script on one page can read what another page kept. The vault code is vendored into the reader repository, not loaded from anywhere else.
- **It is not just for the newsroom.** Every site we build needs the same thing: an account with no server, data nobody else can read, on every device. This is that, as a pattern.

## Part one: the design

### The test

The lab has seven cards: what the browser can do; make a passkey for this site with PRF; touch it and show a fingerprint of the bytes; derive the door; make a recovery code; compare the derivation with sgit's Python, value by value; and create the door on a vault server, open it again as a new device would, and delete its file. On 11 and 12 October it was run with one Google Password Manager passkey, made on the Mac and synced, and with one iCloud Keychain passkey.

What held:

- **The platform path.** The Google passkey gave the same bytes in Chrome on the Mac, answered by Google Password Manager with Touch ID, and in Safari on the iPhone, answered by the same provider with Face ID. The iCloud Keychain passkey gave the same bytes on the Mac, the iPad and the iPhone, in Safari and in Chrome.
- **The derivation.** From the bytes to a door address and passphrase, and from those to sgit's read and write keys, the browser and sgit's own Python agreed on every value, from a fixed test vector and from the live bytes.
- **The door.** With an access key, the page created the door at its derived address on the vault server, wrote its one file, the master's key encrypted under the door's read key, opened it again the way a new device would, and deleted the file.

What did not hold:

| Run | Client | How the passkey answered | Bytes |
|---|---|---|---|
| 1 | Chrome on a Mac | Google Password Manager on the Mac, Touch ID | A |
| 2 | Safari on an iPhone | Google Password Manager on the phone, Face ID | A |
| 3 | Safari on an iPad | A QR code, scanned by the iPhone; the phone's provider answered | B |
| 4 | Chrome on the same Mac, "use a phone, tablet or security key" | A QR code, scanned by the same iPhone; the same provider answered | B |

Same credential id, same user handle, same input, same flags. Runs 1 and 2 share the platform path and share a result; runs 3 and 4 share the hybrid path and share the other. Run 1 and run 4 are the same browser on the same machine, minutes apart, differing only in which way the phone's provider was reached. Each path was deterministic; the two paths disagreed.

This is a known class of bug. Apple's developer forums carry the same symptom for iCloud Keychain passkeys since late 2024: one PRF value when the passkey is used on the device, another when an iPhone or iPad scans a QR code shown by a Mac, for the same credential and the same salt. An Apple engineer called it a bug, pointed at the extension's two seeds, one for when the user was verified and one for when not, and said a fix was in the iOS 18.4 and macOS 15.4 betas; a later tester reported it persisting. Our passkey was Google's, served to the QR flow through iOS's cross-device role for third-party providers, so either the bridge or the provider behaves differently on that path, and the lab cannot tell which. What it can tell, now, is which path a result came from, because the browser reports whether the authenticator was platform or cross-platform, and the card shows it.

The thing to notice is how long this has sat. A defect in the one property that makes PRF useful for encryption, visible to anyone who tries two paths, would not survive long under real load. The reasonable inference is that few people derive encryption keys from passkeys across the hybrid path in production. That is not a reason to avoid the technique. It is a reason to design as if the bytes are a key a provider lends for one path, and to keep every door replaceable.

### What each piece actually gives you

It helps to separate the pieces, because they are easy to blur.

| Piece | What it gives the page | What it does not give |
|---|---|---|
| **The account you are already signed in to** (Apple, Google, Microsoft) | Nothing, directly. It is what syncs your passkey store between your devices, so the passkey you make on one device is on the others | Anything to the site: not your name, not your email, not that you have an account |
| **A passkey for this site** | A gesture (touch, face, PIN), a signature, and with PRF, 32 bytes computed from a secret the authenticator keeps for this site and this passkey | The bytes to anyone but the page on this site that asked, after the gesture; and not, in 2026, the same bytes by every path |
| **The path** | How the passkey was reached: the provider on this device, a phone over the hybrid link, a hardware key | A guarantee that two paths compute the same bytes |
| **The passkey store** | Where the passkey lives: Google Password Manager, iCloud Keychain, Windows Hello, a hardware key, or the browser's own profile | Anything about what the bytes are for |
| **sgit** | Vault keys made in the client (a 24-character passphrase and an 8-character vault id), read and write keys derived from them, ciphertext on the server, files that can be deleted, and vaults that can be destroyed | A way to find a vault you have no key for; a way to reuse a destroyed id |
| **The access key** | The right to create vaults and write to them on the vault server, the thing people will buy | Any way to read a vault |

One clarification that matters. What people call "the Google passkey" is a passkey **for this site**, registered by this page under this site's name, which your store keeps and syncs. It is not the passkey you use to sign in to Google, and a website cannot get PRF bytes from that one. There is no sign-in to the site at all: the page registers a discoverable credential with a user handle it chose, and the only login involved is the one you already have with your platform, which syncs the store. The site learns a credential id, a public key and, after your gesture, 32 bytes. Not your email, not your name, not which account syncs it.

That is also why the vault travels. If you are signed in to Apple on your iPhone, your iPad and your Mac, the passkey you make on one is on the others, and so is the door it opens, as long as each device reaches it the same way. The choice of store is the choice of where the vault goes, and the reader made it long before they met this site.

### Where the door key lives: nowhere

The places the key could live, and how you would find each before you could open it. Deriving the door from the passkey needs nothing to be found; the stored options become backups.

Every option for storing an encrypted vault key has the same problem: you have to find the encrypted key before you can open it, so it has to live somewhere you can reach with only what you have at that moment, which is your passkey.

- **Inside the vault itself:** you need the key to read the vault. The chicken and the egg.
- **An SG/Send transfer:** if the transfer id is assigned on upload, you need to have stored the id somewhere first.
- **A cloud folder in the user's own account**, such as Google Drive's app-data folder: it works from the browser, with the user present for each token, and it needs a sign-in to that account, which this design does not have. If it is ever used, it is an availability backup of an encrypted copy, not the main path.
- **A bucket keyed by the account id:** the design [secrets.sgit.ai](https://secrets.sgit.ai/) has, with Identity Platform and Cloud Storage. It works, and it is a cloud project per environment.
- **Inside the passkey (`largeBlob`):** support is too uneven to depend on.

And then the option that needs none of it. **sgit vault keys are generated in the client**: a random passphrase and a random vault id, and `sgit init` accepts a key it is given. So instead of generating the door's key at random and storing it, the browser **computes** it from the PRF bytes: the passphrase, and the vault id, with HKDF. On any device where the passkey is reached by the same path, the same gesture gives the same bytes, the same address and the same key. The browser knows where to look and how to open it before it has fetched anything. The door holds the master vault's key, which is random and made once. The master holds everything else.

The review on 11 October asked why the master's key was not computed from the bytes directly, with no door. In our use case there was no requirement for it, and I agreed. The test is the requirement. If the master's key were derived from the bytes directly, a path that gives other bytes would derive another master, and nothing could join the two. With the door in between, a second path is one more small vault holding the same master key, written once. The layer costs one vault per path and one derivation on unlock, and buys independence from how any provider computes its bytes on any day.

### The derivation

For the newsroom, with the relying party ID `newsroom.sgit.ai`, as the lab runs it:

1. **The PRF input** is a fixed, public value: `SHA-256("newsroom.sgit.ai/door/v1")`. An input is not a secret; only the authenticator can turn it into the 32 bytes.
2. **The door seed** is `HKDF-SHA256(ikm = PRF bytes, salt = SHA-256("newsroom.sgit.ai"), info = "sgit/door/v1")`.
3. **The door's passphrase and vault id** are two more HKDF outputs from the seed. sgit accepts any printable ASCII passphrase up to 256 characters, so the passphrase is the hex of 32 bytes (`info = ".../passphrase"`), keeping all 256 bits. The vault id has to be lowercase letters and digits, 4 to 24 of them, so 8 characters are drawn from a third output (`info = ".../id"`) with rejection sampling, so that no character is favoured. The id is the door's address.
4. **The door vault key** is the sgit vault key made of those two, and from there, sgit's own derivation gives the read and write keys, exactly as the command line does: PBKDF2-HMAC-SHA256 at 600,000 iterations, once for the read key and once for the write key. That is the cost of this design. Door, master and reading vault need up to six derivations; measured in headless Chromium on a four-core machine, one takes about 105 ms and six run together about 640 ms, and a phone is several times slower, so a cold unlock can spend two to four seconds deriving keys before it fetches anything. The page derives each vault's keys once per session, runs them in a worker, and derives a write key only when there is something to write.
5. **The recovery door** is the same, with the recovery code in place of the PRF bytes: 26 characters of base32, 128 bits, made by the page and shown once. It is long so that it needs no password stretching, as in the secrets.sgit.ai keyring design.
6. **Collisions** are not a practical worry with 36⁸ possible ids, but the page checks: a derived address that already holds something it cannot open is skipped, with a counter in the HKDF info.

The browser and the command line agree byte for byte: the lab's test vectors run the same derivation from a fixed, fake PRF output through the browser code and through sgit in Python, and compare every value when the page opens.

### What is in each vault

- **A door:** one file. The master vault's key, encrypted under the door's read key, and a small record: the kind of door (a passkey, or the recovery code), the provider as the browser named it, the path (platform or cross-platform), the credential id, which is public, a device label the reader typed, and the date.
- **The master vault:** the keyring. The keys of the vaults below it, by site and purpose: the reading vault first, then the notes-to-the-agent vault, then whatever an agent creates for the reader. Read keys the reader has been given. The access key: a read-only clone needs no token, so after the unlock the browser finds the access key here, and the reader pastes it once, on the first device. The key pairs for this site: a signing pair and an encryption pair, as [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) separates them, and plausibly one per persona, each with a label, a purpose, a date and a status. And the list of doors, each with its own vault key, so that from any open door the page can read, rewrite or delete every other door.
- **The reading vault:** one log per device, appended, never edited: pages read and how far, ratings, personas, the reading list, notes, receipts by payment reference. Every device computes the same state from all the logs, as described in [I miss it](i-miss-it.md).

The key pairs are generated at random and stored. They are never derived from the passkey, and after the test that is more obviously right than it was: a key pair derived from bytes that depend on the path would be a different identity on the iPad than on the Mac. The passkey is a lock, not an identity. It opens a door and does nothing else. Everything that represents the person survives any change of lock, a new passkey, a second path, a hardware key, a recovery, a provider's fix. The trade-off against a non-extractable Web Crypto key is real: a non-extractable key is stronger on one device, but it is one device, and an identity that has to be the same on the phone, the iPad and the iMac has to travel. The private keys exist in browser memory only while the master is open.

### A door per path

The unit of the design is the path. Whatever produced a distinct set of bytes gets a distinct door: a passkey through its provider on the device, the same passkey through a phone over the hybrid link, a hardware key, a second passkey for the same role, the recovery code. Every door points at the same master and says where it came from.

**Adding a door moves no key through a person.** The page is unlocked, so the master's key is in its memory. The reader asks for the PRF bytes again by the other path. The page derives the new door from those bytes, encrypts the master's key under the new door's read key, writes the door's one file with the access key, and adds the door to the master's list. The provider that answered sees a PRF request and returns bytes; it never sees the master's key, a vault key or a passphrase. Nothing is typed, nothing is pasted, nothing public carries a key. A Mac with Chrome is where both paths run in one session, as run 4 showed: the provider on the Mac answers locally, and "use a phone, tablet or security key" reaches the same passkey over the hybrid link. So the setup for the phone-by-QR path is two gestures on the Mac, in the first week: open the door you have, then add the QR path as a door. Afterwards the iPad, or any browser that reaches the phone by QR, derives that door and finds the master.

**Where no device has both paths, the recovery code is the way in.** A new tablet whose only route is the QR path, before that path has a door, derives an address and finds nothing. The page says "no door here for this path yet" and offers two ways in: add the door from a device that is already open, or type the recovery code. The code derives the recovery door, which holds the master's key; the page is now unlocked; the new path's door is written as above. The recovery code is the one secret a person ever types, and only on a device where no door opens.

**An unknown address is not an error.** A derived address with nothing at it means a path with no door yet. The page never treats it as a failure, because a provider's fix can move a path's bytes at any time: if Apple or Google changes one path so that its bytes match the other, the door for the path that moved stops opening and the door for the other path takes over, with no loss. If a change moves a path's bytes to something new, that path finds no door, says so, and the reader adds one. The design never has to guess which output was correct. It only has to keep every door replaceable.

**Providers without PRF hold the recovery code, and are not doors.** A provider that returns no PRF bytes, Chrome's own store today and any password manager whose passkeys do not support the extension, cannot be a door, because there are no bytes to derive one from. It can hold the recovery code as a secure note. That makes it a holder of a door's passphrase, which is a weaker thing: whoever can read the note can open the recovery door. It is a fair place for the code for a reader who already trusts that manager with their passwords, and the page describes it as what it is.

**A lost device.** From any open door, delete the lost device's door, its file on the server and its entry in the list. That stops that path from finding the master from the next unlock on. It does not undo a copy of the master's key the lost device may have had in memory; the full answer is to rotate the master's key and rewrite the doors that are kept, which is designed and not built.

### Several passkeys, several masters

Doors are paths to one master. A second passkey for a different role is a second master, with its own doors. The facts that make this work, and the one that trips people up:

- **The store dedupes by user handle.** When a passkey is created, the site gives it a user id and a display name. iCloud Keychain and Google Password Manager treat a new passkey with the same user id for the same site as a replacement for the old one. So two passkeys that must coexist get two user ids and two names, "Dinis · admin" and "Dinis · reader".
- **The picker is the switch.** When the page asks for an assertion without naming a credential, the store shows its own sheet listing the passkeys it holds for this site, and the person picks one. If the page remembers a credential id and a label in local storage, which are not secret, it can offer "Unlock admin" and ask for that passkey by id, with the sheet as the fallback.
- **Two stores in one browser.** In Chrome on a Mac the sheet offers both iCloud Keychain and Google Password Manager, plus a phone by QR and a hardware key, so one person can have a reader passkey in one store and an admin passkey in the other, on the same site in the same browser. Safari offers iCloud Keychain, hardware keys and a phone, not Google's store.

An admin master holds what the desk needs: access keys, the write side of the newsroom's vaults, the publishing key pair. A reader master holds the reading vault, the notes vault and the persona key pairs. The admin passkey lives on a hardware key in a drawer, or in a different store from the reader one, so that the keys that can publish are not available every time the keys that can read are. The page shows which master is open, with a lock button that clears memory.

**Moving keys between masters.** A master is a small file of entries, so a move is: unlock A, copy the entry into B, delete it from A. The catch is history. Vaults keep their versions, so an entry deleted from A is still in A's past for anyone who can open A. The rule: keys that move for security reasons get rotated, which for a vault key means `sgit rekey`, a new vault with a new id and the content re-pushed, and the references in every master updated; keys that move for tidiness do not.

**Retiring, and the one thing never to destroy.** sgit can delete a file from a vault, and it can destroy a vault, `sgit vault delete-on-remote`, with the write key and a typed confirmation. A destroyed vault id can never be used again. That is the right tool for a master or a reading vault being retired for good, because their ids are random. It is the wrong tool for a door, because a door's address is derived from the passkey and the path: destroy it and that passkey can never open a door by that path again. So a door is retired by deleting its one file, and the address is left free for the day a door is wanted there again. Retiring a master is: move or rotate what it held, delete its doors' files, destroy the master and the vaults below it that are not kept, delete the saved recovery code, then delete the passkey in the store's own settings, because a site cannot delete a passkey, only the person can.

### The flows

The first device, a new device on a path that has a door, adding a door while unlocked, a new device on a path with no door yet, and a lost device. Every step runs in the browser, against the passkey store for the gesture and the vault server for ciphertext.

1. **First device.** Make a passkey, named for its role. Get its bytes. Derive the door. Paste the access key. Make the master's key, the reading vault's key and the key pairs at random, and a recovery code. Create the door, the master, the reading vault and the recovery door. Move the reading account from this browser's storage into the reading vault. Show the recovery code once. The master records one passkey door and the recovery door.
2. **Second path, same device, in the first week.** Unlocked on the Mac. Ask for the bytes by the other path, the phone by QR. Derive. Write a second door with the same master key. The master now records three doors.
3. **A new device that reaches an existing door.** Ask for the bytes, derive, open the door, read the master, read the reading vault. Reading needs no access key; the access key comes out of the master, so this device can write too. Merge this browser's reading into its own log. Nothing to set up.
4. **A new device that reaches only a path with no door.** The page derives an address, finds nothing, and says "no door here for this path yet". Type the recovery code. The recovery door opens the master. Add this path as a door. From now on this device opens without the code.
5. **A lost device.** From any open door, delete the lost door from the master's list and the server. Rotate the master's key when that is built.

**Signing out and locking.** Keys exist only in the page's memory: cleared on lock, after a period of inactivity, and when the page is closed. The browser's own copy of the reading account stays as it is today.

### Security, said plainly

- **What each party sees.** The vault server: ciphertext, sizes, times and ids that look random. Your platform account: that a passkey exists for this site, under the name you gave it, and a secret it never sees used. The provider that answers a PRF request: the request, and that it answered. Not which key pairs exist, not what they signed, not which personas they belong to. Only this page, in your browser, after your gesture, holds the PRF bytes and the keys.
- **Whoever can use the passkey by a path that has a door can reach everything below the master.** That is exactly the passkey's protection, the biometric, the device and the store, and nothing in our stack adds to it or weakens it. A second passkey for the admin master is how the reach is split.
- **A path's bytes are a key a provider lends.** The test showed that two paths can compute different bytes from one credential, and that a provider's fix could change either. The door layer is what makes that survivable: no door is the only way in, and every door can be replaced from any other or from the recovery code.
- **The origin loads no third-party scripts, on any page.** Storage is per origin, so a script on any page of the site could read what the account page keeps. The newsroom's pages load only code from the reader repository, with the vault code vendored into it rather than loaded from the vault web app or tools.sgraph.ai. The lab lists every call it makes to a vault server as it happens.
- **The relying party ID is a trust boundary.** A passkey for `sgit.ai` would work on every `*.sgit.ai` site, and any of those sites could ask it for PRF bytes, so every one of them would have to be as strict as the strictest. The lab uses `newsroom.sgit.ai` exactly, as secrets.sgit.ai uses its own host. Sharing across sites is part two.
- **Passkeys cannot be phished across sites.** They are bound to the site's name; a look-alike domain gets nothing.
- **Losing everything is final.** Every door's passkey and the recovery code gone means no one can open the vaults. That is the property that makes the design worth having, and the first run says so before it shows the code.
- **Availability is not secrecy.** The vault server could delete or roll back ciphertext. It cannot read it. The local copy covers the first; nothing is needed for the second.
- **Agents do not have passkeys.** An agent that should read part of a user's data gets a read key for one vault, given by the user from the master, never the master itself.

### Where PRF works today

As of October 2026, from vendor documentation, published tests and our own (see the sources):

| Passkey provider | PRF |
|---|---|
| Google Password Manager (Chrome, Edge and Samsung Internet; Android) | Yes, by default; desktop Chrome from version 136. Tested: the same bytes on a Mac and an iPhone by the platform path; different bytes by the QR path |
| iCloud Keychain (Safari 18, macOS 15) | Yes. Tested: the same bytes on a Mac, an iPad and an iPhone, in Safari and Chrome, by the platform path |
| Windows Hello | Yes, since the February 2026 update to Windows 11 |
| Firefox | Yes, on macOS from version 139 and Windows from version 148 |
| Hardware security keys | Yes through `hmac-secret`, but not with YubiKeys in Safari |
| Chrome's own profile authenticator | No |

The page checks `prf.enabled` when it creates the passkey, and never guesses: if it is false, it says so and offers another authenticator.

### What happens in a clean browser

The table above is about browsers. The question that matters to a reader is about devices: will the newsroom I opened on my laptop be the same one on my phone? That depends on where the passkey lives, which is a choice the reader made long before they met this site, usually without noticing, and now also on how each device reaches it.

Where a passkey can live, what each place needs, whether the passkey travels, whether it can return the PRF bytes, and what that means for the reader. The ladder below the table is what the page offers when PRF is off.

| Where the passkey lives | Needs | Travels? | PRF | What the reader gets |
|---|---|---|---|---|
| **Google Password Manager** (Chrome signed in, Android) | A Google account | Yes, to every device signed in to it | Yes | The same newsroom everywhere, by the platform path |
| **iCloud Keychain** (Safari, iPhone, iPad, Mac) | An Apple ID | Yes, across Apple devices | Yes, Safari 18 and macOS 15 | The same newsroom on every Apple device, by the platform path; tested |
| **Windows Hello** (Windows 11) | The device; a Microsoft account to sync | Device-bound, unless synced | Yes, since February 2026 | This PC, or every PC on the account |
| **A hardware key** (YubiKey and others) | The key, and its PIN | Yes, wherever the key is plugged in | Yes, through `hmac-secret`; not with YubiKeys in Safari | No account anywhere; a few dozen passkeys per key |
| **Your phone, by QR** (the hybrid flow) | A passkey on the phone, in its own store | Yes, one scan at a time | Where the phone's store does, and with bytes of its own | A door of its own, added once from an open device or with the recovery code; then a clean laptop or an iPad opens with the phone beside it |
| **Chrome's own profile store** (a clean Chrome, no store signed in) | Nothing | No: this browser, on this computer | No, in 2026 tests | Signs, returns no bytes: no door can be derived; it can hold the recovery code |

So the rule, in one line: **the same newsroom on every device needs a synced store or a hardware key in your pocket, and a door for each way your devices reach it.** A clean browser with neither gives you this device, plus the recovery code. A passkey made there still works, as a passkey; it is stored by the device, tied to that browser profile on that computer, and deleted with it. The catch is the last row: Chrome's own store, used when there is no provider (a clean Chrome on Linux, or on a Mac with iCloud Keychain off), signs but returns no PRF bytes in 2026 tests, so no door can be derived there at all.

Two things follow. The page learns which case it is in at creation, from `prf.enabled`, and never guesses. And when PRF is off, it offers a ladder, in this order: sign in to a store, so the passkey syncs from now on; use your phone by QR, one scan at a time, with its own door; plug in a hardware key; or stay on this device, where the browser's own copy keeps working and the recovery code is the way back. That is a real limitation of PRF today, not of the design, and the article would be dishonest without it.

### The brief for the MVP

*For the session that runs newsroom.sgit.ai. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026, revised the same day, and revised again on 12 October after the lab. Dinis decides what ships, and is the first user.*

What the lab has already built, as cards: the browser check, making a passkey with PRF, getting the bytes with the path shown, the derivation, the recovery code, the test vectors against sgit's Python, and one door created, opened and deleted on a vault server. What follows is the rest.

1. **Signed in where you already are.** The first screen is the passkey, and the page says in one line that the passkey lives in the store you already use and goes where it goes. No sign-in to the site, no OAuth, no email.
2. **The passkey**: create with `rp.id = newsroom.sgit.ai`, a resident key, user verification required, `extensions.prf`, a user handle and display name chosen for the role; get with the fixed PRF input; check `prf.enabled`; record the path the browser reports. When PRF is off, the ladder, each step explained in one line.
3. **The derivation** in part one, with the lab's test vectors, kept.
4. **The vaults**: the door, the master, the reading vault and the recovery door, created with the access key, using the browser code that already reads and writes vaults, vendored into the reader repository. Each door's one file holds the master's key and its record; the master holds the keys below it, the access key, the key pairs and the list of doors with their keys.
5. **The identity**: generate a signing pair and an encryption pair at random on the first device, store them in the master with a label, a purpose, a date and a status, and publish the public halves where the share page and the subscribe lane need them. Never derive a key pair from the passkey.
6. **Add a door**: a card that takes an open master and the other path's bytes and writes the second door, with no key typed; it is the lab's door-writing card with the master's key taken from memory instead of made at random. Offer it on the first device, in the first week, as "add your phone by QR".
7. **No door here yet**: when a derived address holds nothing, say so in those words and offer the two ways in, a device that is already open or the recovery code. Never an error.
8. **The move**: the reading account from the browser's storage into the reading vault, as the first device's log.
9. **The right-hand side**: once open, show the master: its entries by name and purpose, its doors by provider, path, device and date, and the reading vault's contents, with a lock button and the name of the door that opened it. Retire a door from here.
10. **Several passkeys**: a second passkey with its own handle and name computes its own door to its own master; a move screen that is a copy with a sentence about history; a retire screen that walks the order in part one, deletes door files, destroys only random ids, and ends by sending the person to their store's settings to delete the passkey.
11. **Tests**: Chromium's virtual authenticator with PRF in the build; the first device, a new device on an existing path, adding the QR path as a door on a Mac, a new device that reaches only a path with no door, and a lost device, end to end; the four runs in the table, repeated, so that a provider's fix is noticed the day it lands; a clean Chrome profile with no store; two devices editing offline and agreeing; a [synthetic reader](how-to-run-synthetic-users.md) who has never heard of a vault key.
12. **Report it**: the mismatch is reproducible with the lab in a few minutes. File it with Apple through Feedback Assistant, with logs from both devices as their engineers asked, and with Google against Password Manager's PRF handling on iOS.
13. **Not in the MVP**: any sign-in to the site, a cloud backup, sharing across sites, rotating the master's key, anything on a server of ours.

The acceptance test is the experience in the fourth paragraph of this article: a new browser, a gesture, and my reading account, on my iPhone, my iPad, my laptops and my iMac, with the iPad's door added once from the Mac.

## Part two: what this enables

Once these dots are connected, we have something we did not have before: an end-to-end path from a gesture to a vault, entirely in the browser, on commodity pieces, and now tested against a real vault server. And just about every site and project we build needs exactly that.

- **Accounts with no server, and no identity.** A static site gets a user who can open their own data on any device, and keep it private from the site's operator. No account database, no password, no email, no back end.
- **Data the operator cannot read.** Not as a promise in a privacy policy, but as a property: the vault server holds ciphertext, and the keys are on the user's devices.
- **One master, many vaults.** The reading vault is the first. The same master can hold the key to [secrets.sgit.ai](https://secrets.sgit.ai/)'s keyring, a RiskMandate customer's policies, the memory of an agent the user runs, or the notes a reader sends to the newsroom.
- **Sharing without shared secrets.** The key pairs in the master are what [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) needs: give someone a vault key by encrypting it to their public key, with no secret sent in a chat.
- **One account across sites.** Two ways, later. A key hub, such as secrets.sgit.ai, holds the master and hands a site only the key to its own vault, after the user approves it in a pop-up, the way a wallet connects to a site. Or, across different domains, WebAuthn's Related Origin Requests let one passkey work on a list of related sites, in Chrome and Safari today.
- **For anyone else.** None of this is specific to us. Any static site, on any host, could use a passkey with PRF and a vault, and give its users the same thing. I would like it to become a small, open component, the way [SG Meter](pay-after-you-read.md) is for reading, and the lab is the start of it.

If a site ever needs a stronger statement of who the user is, for a purchase that must be refunded to a person or a support case that must find them, a sign-in with Google or Apple can be added on an origin of its own, handing back an account id and nothing else. With no back end to hold that id, I am not sure we will ever need it, and the design does not depend on it.

This is why I think it matters more than a login feature. It is the moment the client-side pattern stops needing anyone's server for identity and storage, and becomes something other sites can use.

## What this does not claim

- **The lab is a lab.** It shows each step as a card, and it created, opened and deleted one door on a real vault server. The master vault, its door list, adding a door, the reading vault and the move are not built.
- **The support table is a snapshot, and so is the test.** The vendor rows are from documentation and published tests in 2026. Our own rows are two passkeys, three devices and two days. A provider's fix could change the QR path's bytes tomorrow, which is why the design treats an unknown address as "no door here yet".
- **The lab cannot say which path is right.** Both outputs need the credential's secret to check against the specification. It can say that each path was deterministic and that the two disagreed.
- **Computing the door is a choice with a cost.** A door is lost with its passkey, or with its path; the other doors and the recovery code are what cover it.
- **What changed in this version.** The door is back, as a door per path rather than per passkey, and each door records where it came from. The claim about synced passkeys is narrowed to the same kind of path. Adding a door is a first-week step with no key typed; an unknown address means no door yet. The recovery door is back, and providers without PRF hold the code rather than being doors. A door is retired by deleting its file, never by destroying its derived address. The key pairs stay random, sign-in stays out, and several passkeys for several roles are several masters.

If you build sites that need accounts without a back end, or you work on passkeys or password managers and can tell us which side of the QR path owns the mismatch, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded on 11 October 2026, asking for the design and for research into what a passkey gives a website and where an encrypted vault key could be kept; a review conversation the same day that removed the door and the sign-in; and the newsroom's test on 11 and 12 October, written up in [One door per passkey path](https://newsroom.sgit.ai/admin/notes/2026-10-12__one-door-per-passkey-path.md) and visible in [the passkey lab](https://newsroom.sgit.ai/passkey/), which put the door back; written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The four runs in the table, the credential ids and flags, and the fact that the fingerprints differed are from the lab as run on 12 October; the iCloud Keychain result across a Mac, an iPad and an iPhone is from the same days. The design builds on secrets.sgit.ai's published design ([how it works](https://secrets.sgit.ai/how-it-works/), [the keyring format](https://secrets.sgit.ai/keyring/), [passkeys, WebAuthn and PRF](https://secrets.sgit.ai/learn/passkeys/) and [keys](https://secrets.sgit.ai/learn/keys/)), and on how sgit generates and parses vault keys in the client (`generate_vault_key` and `parse_vault_key`), destroys a vault (`sgit vault delete-on-remote`) and rotates a key (`sgit rekey`), read from the sgit command line's source; the unlock cost was measured with WebCrypto PBKDF2 in headless Chromium on 11 October 2026. The mismatch across paths is reported for iCloud Keychain on Apple's developer forums: [Different PRF output when using platform or cross-platform authentication attachment](https://developer.apple.com/forums/thread/764730), [Passkey PRF inconsistency between Apple devices](https://developer.apple.com/forums/thread/774111) and [PRF extension not supported in Safari's cross-device WebAuthn flow](https://developer.apple.com/forums/thread/774112). The research: Corbado, [Passkeys and WebAuthn PRF for end-to-end encryption (2026)](https://www.corbado.com/blog/passkeys-prf-webauthn) and [WebAuthn L3 support in credential managers](https://www.corbado.com/blog/webauthn-l3-credential-manager-support); Yubico, [Developer's guide to PRF](https://developers.yubico.com/WebAuthn/Concepts/PRF_Extension/Developers_Guide_to_PRF.html); Mozilla, [support for the WebAuthn PRF extension](https://bugzilla.mozilla.org/show_bug.cgi?id=1863819); Chromium, [intent to ship the PRF extension](https://groups.google.com/a/chromium.org/g/blink-dev/c/iTNOgLwD2bI); web.dev, [passkey reuse across sites with Related Origin Requests](https://web.dev/articles/webauthn-related-origin-requests). Related articles: [I miss it, so it is working](i-miss-it.md), [No server, by design](no-server-by-design.md), [Where the vault keys live](where-the-vault-keys-live.md), [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) and [How to run synthetic users](how-to-run-synthetic-users.md).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-passkey-opens-the-vault)

### Builds on

- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.

### Continued by

- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.
- [The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it](the-vault-crosses-chrome-profiles.md) The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.
- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 77 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=77)

**Posting this article on LinkedIn?** The cover is [the-passkey-opens-the-vault.jpg](banners/the-passkey-opens-the-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-passkey-opens-the-vault.html)*
