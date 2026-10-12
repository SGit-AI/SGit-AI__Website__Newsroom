# One door per passkey path

**Date:** 12 October 2026. **Status:** a finding from the passkey lab, and the design change it forces. The lab shows the finding; nothing beyond the lab is built.

**Related:** [The passkey opens the vault](../../articles/the-passkey-opens-the-vault.html) (the design), [the passkey lab](../../passkey/index.html) (where the finding was made), `admin/build/test_passkey.mjs` (what is checked).

## In one paragraph

The design derives a small door vault from a passkey's PRF bytes and keeps the master vault's key inside the door. It rests on one claim: the same passkey gives the same bytes wherever it is used. A test on 12 October with one Google Password Manager passkey found that the claim holds along one path and not across paths. Used by the provider on the device (a Mac, then an iPhone), the passkey gave one set of bytes. Used through the cross-device flow, where a phone answers a QR code from a Mac or an iPad, the same passkey gave a different set, and gave it consistently. Same credential id, same user handle, same input, different bytes. A second test with an iCloud Keychain passkey gave the same bytes on a Mac, a current iPad and a current iPhone, in Safari and in Chrome, which is the main scenario the design is for; an older iPad that could not use the passkey locally offered only the QR path, which is a different path. The unit of the design is therefore not the passkey but the path: a door per set of bytes, every door pointing at the same master and recording where it came from. The article already has most of this (every passkey is a door, so is a recovery code, a door is added while unlocked, the master lists its doors), so what changes is small and sharp: the middle layer stays because it cannot be removed, adding a door becomes a normal first-week step rather than an edge case, and the page must treat an unknown door address as "no door here yet", never as a failure.

## Tested first: a Google Password Manager passkey

One passkey, made on newsroom.sgit.ai by card 1 of the lab with the PRF extension, stored in Google Password Manager and synced. Card 2 asks the authenticator for the PRF bytes with the fixed input, the SHA-256 of `newsroom.sgit.ai/door/v1`, and shows a fingerprint of the result. Four runs:

| Run | Client | How the passkey answered | Fingerprint |
|---|---|---|---|
| 1 | Chrome on a Mac | Google Password Manager on the Mac, Touch ID | bb0f774a |
| 2 | Safari on an iPhone | Google Password Manager on the phone, Face ID | bb0f774a |
| 3 | Safari on an iPad | QR code, scanned by the iPhone; the phone's Google Password Manager answered | a963886e |
| 4 | Chrome on the Mac, "use a different passkey", "use a phone, tablet or security key" | QR code, scanned by the same iPhone; the same provider answered | a963886e |

In all four the page showed the same credential id, the same user handle and the same flags (user present, user verified, backup eligible, backed up). The input hash was the same. Runs 3 and 4 share a client-side path, the hybrid transport, and share a result. Runs 1 and 2 share the other path and share the other result. Nothing else distinguishes them: run 1 and run 4 are the same browser on the same machine, minutes apart, differing only in which way the phone's provider was reached.

The fingerprints quoted are those the lab showed on the day. The lab's fingerprint was then the first four bytes of the PRF output itself, which is a careless thing to put on a screen and in a chat; since v0.9.1 it is the first four bytes of the SHA-256 of the output, so the values above are no longer what the page would show, and they remain valid as evidence that the outputs differed.

## Tested second: an iCloud Keychain passkey

A second passkey, made by card 1 and stored in iCloud Keychain instead, on the same day:

| Run | Client | How the passkey answered | Result |
|---|---|---|---|
| 5 | Safari on the Mac | iCloud Keychain on the Mac | one fingerprint, call it K |
| 6 | Chrome on the Mac | iCloud Keychain, through the system's passkey support | K |
| 7 | Safari on a current iPad | iCloud Keychain on the iPad | K |
| 8 | Safari on a current iPhone | iCloud Keychain on the phone | K |
| 9 | Safari on an older iPad | No passkey offered locally; the browser went straight to the QR path | not completed |

Runs 5 to 8 are the scenario the design is for: one person, their own devices, one provider, and the same bytes everywhere through the platform path, in both browsers. Chrome on the Mac matches Safari because it reaches iCloud Keychain passkeys through the same system provider, so the bytes are computed in the same place. Run 9 is the boundary: a device that cannot use the passkey locally, because its operating system predates the support, offers only the cross-device path, and by the first test's result that path should be expected to give its own bytes and therefore its own door. It was not completed, so whether an iCloud Keychain passkey over QR matches its local bytes on these versions is unknown; the lab's path row would tell, and the design does not depend on the answer.

Two conclusions follow. The claim in the article is right for the common case and needs the qualifier "through the same kind of path", not a retraction. And the product should steer a reader to the provider on the device first, and present the QR route as a path that gets its own door, rather than as the same thing done remotely.

## What the extension is supposed to do

The WebAuthn PRF extension is defined over the CTAP2 `hmac-secret` extension. An authenticator keeps a random value per credential (CTAP calls it CredRandom, and keeps two: one used when the user was verified, one when not) and returns HMAC-SHA-256 of that value over a salt the client supplies. The WebAuthn specification asks the client to hash the site's input first, as SHA-256 of the string `WebAuthn PRF`, a zero byte and the input, so that a site's chosen bytes never reach the authenticator raw, and asks platform authenticators that answer PRF directly to apply the same hashing, so that the result is the same whichever way the credential is reached. The intent is explicit: one credential, one input, one output.

Two layers can break that intent without either being obviously wrong on its own. If one path applies the prefix hash and the other does not, or one applies it twice, the HMAC is over different salts. If one path selects the "with user verification" seed and the other the "without" seed, the HMAC uses different keys even over the same salt. The second is the one Apple's engineers pointed at (below). From outside the authenticator the two cannot be told apart, and neither output can be checked against the specification, because both need the credential's secret. What can be said is that each path is deterministic: the device-local path gave the same bytes on two devices and two operating systems, and the hybrid path gave the same bytes from two clients.

## This is a known class of bug

Apple's developer forums carry the same symptom for iCloud Keychain passkeys, reported from late 2024: one PRF value when the passkey is used on the device, another when an iPhone or iPad scans a QR code shown by a Mac, for the same credential and the same salt. In one thread an Apple engineer called it a bug, said the hybrid value should match the local one provided user verification is handled the same way on both paths, noted that the extension uses different seeds depending on whether user verification was performed, and said a fix was in the iOS 18.4 and macOS 15.4 betas. A later tester in another thread reported the mismatch persisting on a Safari 18.4 beta. A third thread records a Chrome-on-Mac user seeing exactly runs 1 and 4 of the table above.

Our passkey lives in Google Password Manager, not iCloud Keychain, and is served to the QR flow through iOS's cross-device role for third-party providers. So either the bridge that hands a hybrid request to a third-party provider still carries the bug, or the provider itself behaves differently when reached that way. Both are plausible; the lab cannot tell them apart. What the lab can tell, now, is which path a result came from: the browser reports whether the authenticator was platform or cross-platform, and card 2 shows it.

The thing to notice is how long this sat. PRF reached Safari in 2024 and the hybrid path later still; the forum threads are months apart and unresolved on the page. A defect in the one property that makes PRF useful for encryption, visible to anyone who tries two paths, would not survive long under real load. The reasonable inference is that few people are deriving encryption keys from passkeys across the hybrid path in production. That is not a reason to avoid the technique; it is a reason to design as if the bytes are a key a provider lends for one path, on one day, and to keep every door replaceable.

## What changes in the design

### The unit is the path

A door is a function of the bytes. Whatever produced a distinct set of bytes gets a distinct door: a passkey through its provider on the device, the same passkey through a phone over the hybrid link, a hardware key, a second passkey, the recovery code. The article's sentence "the same passkey gives the same bytes on every device it syncs to" becomes "the same passkey gives the same bytes on every device it syncs to, through the same kind of path; a different path can give different bytes, and gets its own door". The lab's card 2 and the hub pages now say the narrower thing.

### The middle layer stays, and this is why

An earlier draft of the design had a stored first vault that pointed at the main vault, and it was simplified to a door computed from the passkey with nothing stored. The door that remained is still a middle layer, one small vault between the passkey and the master, and this finding is the reason it has to remain. If the master's key were derived from the PRF bytes directly, a path that gives other bytes would derive another master, and nothing could join the two. With the door in between, a second path is one more small vault holding the same master key, written once. The layer costs one vault per path and one derivation on unlock, and buys independence from how any provider computes its bytes.

### Every door says where it came from

A door holds the master vault's key and a small record: the kind of door (a passkey, the recovery code), the provider as the browser named it, the path (platform or cross-platform), the credential id (public; it is what any site sees at sign-in), a device label the reader types, and the date. The master vault keeps the list of its doors with each door's own vault key, so that from any open door the page can read, rewrite or delete every other door. That list is what makes retiring a door possible without the passkey that made it.

### Adding a door moves no key through a person

The step the article describes as "while unlocked on one, register the other" is the whole mechanism, and it does not involve typing or pasting a vault key. The page is unlocked, so the master key is in its memory. The reader asks for the PRF bytes again by the other path. The page derives the new door from those bytes, encrypts the master key under the new door's read key, writes the door's one file with the reader's access key, and adds the door to the master's list. The provider that answered sees a PRF evaluation request and returns bytes; it never sees the master key, a vault key or a passphrase. Nothing is copied, nothing is pasted, nothing public carries a key.

A Mac with Chrome is where both paths run in one session, as run 4 showed: the provider on the Mac answers locally, and "use a phone, tablet or security key" reaches the same passkey over the hybrid link. So the one-off setup for the phone-by-QR path is two gestures on the Mac: open the door you have, then add the QR path as a door. Afterwards the iPad, or any browser that reaches the phone by QR, derives that door and finds the master.

### Where no device has both paths, the recovery code is the bootstrap

On a device that cannot reach an existing door (a new tablet whose only route is the QR path, before that path has a door), the reader types the recovery code once. It derives the recovery door, which holds the master key; the page is now unlocked; the new path's door is written as above. The recovery code is the one secret a person ever types, and only on a device where no door opens. It is already in the design as the second door; this makes it also the way a new path joins.

### Providers without PRF hold the recovery code, and are not doors

A provider that returns no PRF bytes (Chrome's own store today, and any password manager whose passkeys do not support the extension) cannot be a door, because there are no bytes to derive one from. It can still hold the recovery code as a secure note. That makes it a holder of a door's passphrase, which is a different and weaker thing: whoever can read the note can open the recovery door. It is a fair place for the code for a reader who trusts that manager with their passwords already, and it should be described as what it is, not as a passkey door.

### What a lost device needs

Deleting a lost device's door file stops that path from finding the master, from the next unlock on. It does not stop a copy of the master key that the lost device may have had in memory. The full answer is to rotate the master vault's key and rewrite the doors that are kept, which is a larger operation on the master vault and is designed, not built. The door list in the master is what makes the smaller step possible from any remaining door.

### What a provider's fix does to a door

If Apple or Google changes one path so its bytes match the other, the door for the path that moved stops opening and the door for the other path takes over, with no loss. If a change moves a path's bytes to something new, that path finds no door, says so, and the reader adds one from an open door or with the recovery code. The design never has to guess which output was correct; it only has to keep every door replaceable and never treat an unknown address as an error.

## The flow, written out

1. **First device.** Make a passkey. Get its bytes. Derive the door. Create the door, the master, the newsroom vault and the recovery door, with the access key. Show the recovery code once. The master records one passkey door and the recovery door.
2. **Second path, same device.** Unlocked. Ask for the bytes by the other path (on a Mac: the phone by QR). Derive. Write a second door with the same master key. The master now records three doors.
3. **A new device that can reach an existing path.** Ask for the bytes, derive, open the door, read the master. Nothing to set up.
4. **A new device that reaches only a path with no door.** The page derives an address, finds nothing, and says "no door here for this path yet". Type the recovery code. The recovery door opens the master. Add this path as a door. From now on this device opens without the code.
5. **A lost device.** From any open door, delete the lost door from the master's list and the server. Rotate the master's key when that is built.

## What the lab shows now, and what it does not

Card 2 shows the path (platform or cross-platform) with each result and says that a different path can give different bytes. Its fingerprint is a hash of the bytes rather than a prefix of them. The comparison box names "another path" among the reasons two fingerprints differ. Card 1 already showed the attachment and the transports at creation.

Not built: adding a path as a door (a card that takes an open door and the other path's bytes and writes the second door), the master vault, its door list, retiring a door, rotating the master. Those are the article's phase five. The lab's card 6 writes one door; the add-a-door card is that same write with the master key taken from memory instead of made at random.

## Field notes from the two days

Smaller things seen while testing, for whoever updates the article or builds the next step:

- **Chrome's first attempt to create a Google Password Manager passkey** showed "Can't reach Google Password Manager. Try again in a few minutes"; the second attempt worked. That is Chrome's side, transient, and the page should say "try again" rather than treat it as a failure of the design.
- **Card 0's PRF capability** reads `null` in some browsers rather than true or false, through `getClientCapabilities()`. The lab now says "the browser does not say" in that case; card 1's `prf.enabled` is the answer that counts.
- **Safari's QR dialog names the registrable domain** ("sign in to sgit.ai") where Chrome's names the host (newsroom.sgit.ai). The relying party id is newsroom.sgit.ai on both create and get; the dialogs word it differently.
- **The flags were the same on every path**: user present, user verified, backup eligible, backed up. The flags do not reveal the path; `authenticatorAttachment` does, and card 2 now shows it.
- **The credential id and the user handle were identical across every path and provider path**, which is how the page can be sure that the differing bytes came from one passkey.
- **The lab's fingerprint was the first four bytes of the PRF output** until v0.9.1, which put 32 bits of the secret on screen and in chat; it is now a hash of the output. The door derivation was never weakened in practice (the seed is a 256-bit HKDF output), and it was still the wrong thing to show.
- **PBKDF2 at 600,000 iterations** for the read and write keys took on the order of a tenth of a second each on a laptop and several times that on a phone, as the article estimated; the lab shows the time with each key.
- **Chrome's own store** (no provider signed in) signs and returns no PRF bytes, as the article says; the lab shows the ladder in that case.

## Reporting it

The symptom is reproducible with the lab in a few minutes: one Google Password Manager passkey, card 2 on the device, then card 2 through "use a phone" from the same browser. It is worth filing with Apple through Feedback Assistant, with logs from both devices as their engineers asked in the forum threads, and with Google against Password Manager's PRF handling on iOS, so that whichever side owns the bridge sees it.

## Sources

- Apple Developer Forums, "Different PRF output when using platform or cross-platform authentication attachment": https://developer.apple.com/forums/thread/764730
- Apple Developer Forums, "Passkey PRF inconsistency between Apple devices": https://developer.apple.com/forums/thread/774111
- Apple Developer Forums, "PRF extension not supported in Safari's cross-device WebAuthn flow": https://developer.apple.com/forums/thread/774112
- W3C Web Authentication Level 3, the PRF extension (`prf`), and the FIDO CTAP2 `hmac-secret` extension it is defined over.
- Yubico, the PRF extension: https://developers.yubico.com/WebAuthn/Concepts/PRF_Extension/
