# A browser for one: the build brief for Dinis's iPhone newsroom app

*18 October 2026, written by newsroom.writer for the agent that builds it. Status: a brief; nothing in it is built. The article is [a browser for one](https://newsroom.sgit.ai/articles/a-browser-for-one.html). Facts below were checked on 18 October 2026; the ones marked "test first" are not confirmed by any source.*

## The ask

An iPhone app, installed on Dinis's own phone, that is a focused browser for newsroom.sgit.ai. Every time it opens, it shows the newsroom where he left it. It knows what he has read and what he has not, opens his vault, keeps his history, lets him build his own reading workflows, keeps tabs, works offline, never reloads a page on its own, uses as little of the screen as it can, and receives what his agents send him. It is a business-logic layer on top of the site; logic that proves itself moves into the site later.

## Decisions already made by the facts

- **Engine: WebKit.** Outside the EU (iOS 17.4+, BrowserEngineKit) and Japan (iOS 26.2), an app that browses the web must use WebKit. The UK's CMA designated Apple with strategic market status on 22 October 2025 with the browser engine in scope, but as of 18 October 2026 it has published no requirement on engines. Gecko and Blink have not shipped on iOS anywhere. So: a native Swift shell around WebKit, using SwiftUI's `WebView` and `WebPage` (iOS 26+) or `WKWebView`.
- **A paid Apple Developer Program membership is required.** Apple's capability table lists *Associated domains* and *Push notifications* as available to the paid programmes and not to a free Apple account. Associated domains are what let passkeys work in the app for `newsroom.sgit.ai`; push is how agents reach the phone. A free account also expires the install every 7 days.
- **Not built by a cloud Linux session.** An iOS app is built and signed with Xcode on macOS. Paths: a Claude Code session on Dinis's Mac (`xcodebuild`, `xcrun devicectl`); GitHub Actions macOS runners (`macos-26`, about $0.062 a minute against $0.006 for Linux); Xcode Cloud (25 compute hours a month included with the membership). Recommended: build in CI and install through TestFlight, so the agent never needs the phone.

## Test first (phase 0, before any other code)

1. **Passkeys with the PRF extension inside the app's WebKit view.** The vault unlocks with `navigator.credentials.get` and the PRF extension, with the relying party `newsroom.sgit.ai` (`assets/door.js`, `assets/vault-pane/vault-pane.js`). Safari supports PRF for iCloud Keychain passkeys from iOS 18; no source confirms PRF results come back inside a third-party app's WebKit view. Build the smallest app with the associated domain and try the site's own unlock. If PRF does not come back, run the ceremony natively with AuthenticationServices and hand the 32 bytes to the page over the script bridge.
2. **The association file.** `https://newsroom.sgit.ai/.well-known/apple-app-site-association` (no extension, `application/json`) with `webcredentials` for the app's ID. The site already serves `/.well-known/` from GitHub Pages; check the content type and that Apple's CDN fetches it.
3. **Storage persistence.** Whether the web view's IndexedDB and localStorage survive a week unused and storage pressure. Design so the reading state is always rebuilt from the vault; mirror it natively over the bridge if needed.

Done when: on Dinis's phone, the app opens the newsroom, unlocks the vault with his passkey, and his reading state matches Safari's.

## The app (phase 1)

- **Opens to the newsroom, where he left it.** The last tab, the scroll position, restored at launch (iOS 26 adds local and session storage restoration for web views).
- **Tabs, minimal chrome.** A native tab strip that hides on scroll; no address bar unless asked; one gesture for back.
- **Never reloads on its own.** Pages kept in memory and on disk; a pull to refresh only when he asks.
- **Offline.** Every article opened is kept, page and figures, through a `WKURLSchemeHandler` cache or web archives; the reading list is pre-fetched on Wi-Fi.
- **App-bound domains.** `newsroom.sgit.ai` and the vault server listed in `WKAppBoundDomains` (at most ten), which service workers and script injection need.
- **Knows the reading.** The site's reading records (`sgit.reading.v1`, the meter, the folds) are the source; the app reads them over the bridge and shows read, part read and unread in its own lists.
- **The bridge.** A `WKScriptMessageHandler` with a small, versioned set of messages: reading state, vault status, open in a new tab, notify. Every message the page can send is listed in one file, with its behaviour policy beside it.

## Workflows (phase 2)

Dinis builds his own: a morning run (the wires, then new articles, then the briefs page), a review run (articles with open findings), a catch-up run (articles changed since he last read them). A workflow is a small JSON file in his vault, so it travels with him and an agent can propose one. The app runs it as a sequence of tabs with a "next" gesture.

## From the agents (phase 3)

- **Without a server:** when the app is open, it polls his vault for what the agents have written (a daily brief, a review, an answer), and shows it in a native inbox.
- **With push:** a small sender, one function holding the push key, that an agent calls with "vault X changed" and no content; the app fetches and decrypts on the phone. Background refresh exists but runs when the system chooses, so it is a bonus, not the channel.

## Constraints

- Nothing of the vault or reading leaves the phone except to the vault server, as today.
- The app is for one person; it is not on the App Store. TestFlight or a development install only.
- Every piece of logic that works in the app is written so it can move into the site; the app should get thinner over time, not thicker.
- Its behaviour policy is written before it ships: what it can reach (the newsroom, the vault, the push sender), what it may do, and what it must never do (send reading data anywhere else).

## Tests

- Phase 0's three checks, recorded with the iOS version and the device.
- A UI test that opens two tabs, goes offline, relaunches, and finds both tabs and their positions.
- A bridge test: every message in the list round-trips; an unknown message is refused.

## Alternative if the test fails or the membership is not wanted

A home-screen web app: from iOS 26 every site added to the Home Screen opens as a web app by default; passkeys and PRF behave as in Safari; web push works from iOS 16.4. It needs no Mac and no membership. It has no native tabs and no background fetch, so the tabs and offline behaviour would be built in the page.

## Questions for Dinis

- Pay for the developer membership (about $99 a year), or start with the home-screen web app?
- Build on your Mac with a local session, or in CI with TestFlight?
- Which three workflows first?
