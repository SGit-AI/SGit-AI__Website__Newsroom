#!/usr/bin/env python3
"""The vault page: /vault/index.html, where the vault pane opens on its own and the design is explained.

    python3 admin/build/vault_page.py

The pane itself (assets/vault-pane/) is on every page that carries the meter, through the nav chrome.py writes;
this page is the one that opens it on arrival, says what it does, and links the architecture note.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
NOTE = "admin/notes/2026-10-12__the-activity-vault.md"
NOTE2 = "admin/notes/2026-10-12__the-feedback-loop.md"


def page():
    body = f"""<script>document.documentElement.setAttribute('data-vault-open', '')</script>
<div class="note"><b>A beta.</b> The pane on the right is the vault, in four tabs: <b>This page</b>, your notes on what you read and the lane that carries the ones you choose to the newsroom; <b>Reading</b>, every page read in this browser, with its decision; <b>Vault</b>, the reading account this browser keeps, carried between your devices through an encrypted vault that opens with your passkey, and the link that lets a browser without your passkey send into it; <b>Keys</b>, every vault of your account with its key. It is on every page, behind the <b>Vault</b> button beside the balance; the button counts what is only in this browser, and a strip above the tabs names it, with <em>Update the vault</em> one press away. Nothing about the meter changes; the vault is a second home for its data that you keep current.</div>
<h2 id="feedback">The feedback loop</h2>
<ol>
<li><b>Read, and tap.</b> On any page, open the pane; it stays open from page to page until you close it. Above the chips it says what this browser knows about the page: read how many times, when, how far, what it cost. Select a phrase if one is the point. One tap keeps a note in this browser: <em>Done</em> (read it, done with it, off your lists), <em>Read later</em>, <em>Follow up</em>, <em>Not for me</em>, <em>More like this</em>, <em>Liked</em>, <em>Wrong</em>, <em>Fix this</em>, <em>Idea</em>, with the phrase you had selected. Under the chips, <b>Write to the newsroom</b> takes a message for the newsroom&rsquo;s agent, about the page or anything else: <em>Save and send</em> keeps it and sends it in one press; <em>Save, send later</em> keeps it for the next send. On <a href="../wire/index.html">the wire</a>, six of the decisions are at each story (Done, Read later, Follow up, Not for me, More like this, Wrong), and a decided story folds to its headline. The <b>Reading</b> tab lists every page read here, newest first, with its decision, and folds the done ones away.</li>
<li><b>Update the vault</b> when you like: from the strip above the tabs, from the Vault tab, or from the wire&rsquo;s bar. This device&rsquo;s notes travel with its reads, top-ups, personas and the wire stories it has seen to your other devices, in this device&rsquo;s own file. Until you do, they exist in this browser alone: the Vault button counts them, and the strip says what clearing the browser would lose.</li>
<li><b>Send from a browser without your passkey.</b> One an app opens links in, one signed in to nothing, an old iPad: in the Vault tab, <em>Make a link for another browser</em>, then open it, paste it or scan its QR code there. That browser can add what it holds to your vault&rsquo;s inbox and read nothing; the Vault tab shows what arrived, from which browser, before you bring it in. <a href="send.html">The sending page</a>, <a href="../admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md">the design</a>.</li>
<li><b>Send to the newsroom</b> the notes you have not sent. The first send makes a <b>lane</b>: a vault of its own, whose write key stays in your master and whose <b>read key</b> the pane shows. Hand that key to the newsroom once, in the open; it reads the lane and cannot write to it, and nothing else of yours is in it. Later sends go to the same lane. A send also rewrites this device&rsquo;s file in the reader vault, so your other devices see the notes as sent.</li>
<li><b>The newsroom reads the lane</b> with <code>sgit clone</code> or <code>admin/build/lane.py</code>, and answers in the open: a fix in a release, a version of an article. Nothing comes back through the lane.</li>
</ol>
<p>The design, the record, what is not built and the experiments to run are in <a href="../{NOTE2}">the feedback loop</a>.</p>
<h2 id="loop">Open, or connect</h2>
<p>Two ways in, and nothing to name first. <b>Open your vault</b> with your passkey: this browser reads it and writes to it, the meter shows your whole account, and what you read here reaches your other devices. <b>Connect with a link</b>, in a browser that cannot reach your passkey: it only sends; what it holds goes to your vault&rsquo;s inbox, and where the vault is open you file it under a device you already have, or a new one. The map of the states a browser can be in is <a href="../admin/notes/2026-10-13__open-or-connect-a-vault.md">in the design</a>.</p>
<ol>
<li><b>Open with your passkey.</b> If no passkey answers, the pane offers to make one for this site. The first time there is no door at the derived address: paste an access key and <em>Create the account</em>. Three vaults are made (a door, a master, a reader vault), the access key goes into the master, and a recovery code is shown once. An account made before the pane wrote the access key into the master asks for it once.</li>
<li><b>Which device is this?</b> When the vault already knows devices and this browser is none of them, the pane asks: one of them, with its reads and last update, or a new one with a name. Two browsers can share a device (the iPad&rsquo;s two browsers, two Chrome profiles): one row across your devices, one author on the records, every write combined with what the vault already holds for it. Taking a device as this browser&rsquo;s own brings its records here as this browser&rsquo;s.</li>
<li><b>What the vault holds comes here.</b> After the open, the other devices&rsquo; reads, notes and stories seen are brought into this browser on their own, tagged with their device, and the meter shows the account&rsquo;s balance, recomputed from every record. On a page change nothing is brought in without you: the Vault tab and the strip above the tabs say what is in the vault and not here, with <em>Bring them here</em> one press away.</li>
<li><b>Read, and update.</b> The meter charges into local storage as it always has; <em>Update the vault</em> writes this device&rsquo;s records as one file, one commit, published, combined with what the vault had for it.</li>
<li><b>Connect with a link</b>, in a browser without your passkey: paste the link the Vault tab shows, or open <a href="send.html">the sending page</a> from it. The pane says which vault it sends to, takes a name for the browser, and offers <em>Send to my vault</em> there and above the tabs on every page. It can add and never read, so the meter there shows that browser alone.</li>
<li><b>File what arrived.</b> Where the vault is open, the Vault tab lists what each browser sent, from which browser and what it carries, with a choice of where to file it: as a device of its own, or under one you already have, this one included. The choice is remembered for that browser&rsquo;s next batch; a name that matches a device you have is offered first.</li>
<li><b>Recovery code, check, forget.</b> <em>I have a recovery code</em> opens the account on a device whose passkey cannot be a door, and <em>Add this device with the code</em> gives that path a door of its own. <em>Check the vault</em> re-reads every device&rsquo;s file; <em>Forget on this device</em> clears the keys from this tab and leaves the vault unchanged.</li>
</ol>
<h2 id="opened">Your vaults, opened</h2>
<ul>
<li><b>Browse them.</b> <a href="browse.html">Your vaults, opened</a> shows every vault of your account, here with your keys: the files, any file&rsquo;s contents, the commits and the files as they were at each. The master&rsquo;s and the door&rsquo;s files open only behind Reveal, because they hold keys.</li>
<li><b>Your reader vault has an app.</b> The newsroom&rsquo;s viewer lives in a vault of its own, published with a public read key. Your next Update links it into your reader vault, read-only, and makes it the vault&rsquo;s app, so the vault opened in the SG/Vault app shows your account, devices, reading and notes. The code is shared and never copied; your records never go into it. <a href="browse.html#demo">See it on a demo account</a>.</li>
<li><b>Merge devices.</b> In the Vault tab, tick two or more devices in <em>Across your devices</em> and merge them into one, iPad 1, iPad 2 and iPad 3 into iPad. Every read, note, top-up and story seen is kept; a browser still using a merged device is filed under the one it went into. <em>Change</em> beside <em>Device</em> moves this browser into another device the same way.</li>
<li><b>See the calls.</b> The <em>Calls</em> tab names every call to the vault server, a commit, a tree, a file, a ref, an append-lane operation, and, on a press, decrypts what it carried with the key of its vault, when that vault is open in the page. The server only ever had the ciphertext.</li>
</ul>
<h2 id="principles">The principles</h2>
<ul>
<li><b>Local storage stays primary</b>, written in real time by the meter; the vault is updated when you ask, and what it holds is brought in when you open it.</li>
<li><b>Records, never totals.</b> Reads, top-ups, personas, notes and the wire stories seen go in raw; reads, spend, declined, credit and balance are recomputed from them with one starting credit for the account.</li>
<li><b>One file per device, and a device is a bucket you name.</b> Two browsers may share one; every write is combined with the file as it is, so neither loses the other&rsquo;s records, and the records keep one author. The consolidated view is computed from all the files each time.</li>
<li><b>Brought-in records keep their author.</b> What arrives from another device is tagged with it, and the next sync from here writes only this device&rsquo;s own records back.</li>
<li><b>Nothing is typed twice.</b> The access key is pasted once and lives in the master; every other device gets it by opening the master with its passkey, or with the recovery code once.</li>
</ul>
<p>The design, the data layout, what is not synced and why, and the experiments to run next are in <a href="../{NOTE}">the activity vault</a>. The pieces it is made of are in <a href="../passkey/index.html">the passkey lab</a>, and the vault code is the library that runs dev.vault.sgraph.ai, <a href="../assets/vendor/sg-vault/v0.2.3/VENDOR.md">vendored here</a>.</p>
<h2 id="keys">Your keys</h2>
<p>The Keys tab lists every vault of your account with its key: the door of this device and the other doors, the master, the reader vault, and the lane with its read key. A key is shown only when you press Reveal; the lane&rsquo;s read key is shown with Copy. Any of them opens on its own, with <code>sgit clone</code> or in the vault app. A key opens that vault to whoever holds it, and the master&rsquo;s opens everything, so handle them like the recovery code. The lane&rsquo;s read key is the one thing meant to be handed over.</p>
<h2 id="data">What leaves this browser</h2>
<p>Ciphertext, to the vault server (dev.send.sgraph.ai), when you create, update, send or open: every file is encrypted here under keys derived from your passkey, and the server sees requests, sizes and times. The pane lists every call as it happens. The access key travels only as a request header to that server. Your notes leave this browser only when you press Update (to your own reader vault) or Send, including <em>Save and send</em> (to your own lane, and your device&rsquo;s file in the reader vault). <em>Check the vault</em>, <em>Look in the lane</em> and <em>Bring their activity here</em> only read. A browser holding your inbox link sends ciphertext to the lane and reads nothing back; <em>Bring them in</em> writes what arrived into your reader vault. Nothing goes anywhere else.</p>
<p>The keys of an open account live in memory and, for the life of this tab, in session storage, so moving from page to page does not ask for your passkey again; <em>Forget on this device</em> clears them. Local storage holds this device&rsquo;s id and label, your notes, what this browser has seen on the wire and the time of its last update, and never a key or the access key.</p>
"""
    agent = (f"The vault pane (assets/vault-pane/vault-pane.js) has four tabs. This page: what this browser knows about the page from the meter's records (assets/vault-pane/reading.js), the reader's notes (assets/vault-pane/notes.js; one tap at a piece: done, read-later, follow-up, not-for-me, "
             "more-like-this, liked, wrong, fix, idea, with words and the selected phrase, or a message alone, kind note, written under Write to the newsroom; kept in localStorage sgit.notes.v1) and Send to the newsroom, which writes the notes not yet "
             "sent into a lane, a vault of its own whose key is in the master (lane.json) and whose read key the reader hands over; the newsroom reads it with "
             "`NEWSROOM_LANE_KEY=&lt;read key&gt; python3 admin/build/lane.py`; a send also rewrites the device's file in the reader vault. Reading: every page read in this browser, newest first, with its decision, the done ones folded away. Vault: the reading account carried between devices through an sgit vault opened with a passkey: "
             "a door derived from the PRF bytes (assets/door.js), the master and the reader vault (assets/newsroom-vault.js); the reader vault holds "
             "activity/account.json (one starting credit) and activity/devices/&lt;device&gt;.json (that device's raw reads, top-ups, personas, notes and the wire stories it has seen, rewritten whole on each sync); "
             "totals are recomputed from the records (assets/vault-pane/sync.js). The Vault tab also makes the inbox link (assets/vault-pane/inbox.js: an append lane on the reader vault and an RSA-OAEP key pair, inbox.json in the master) and drains it. Keys: every vault with its key behind Reveal, the lane's read key with Copy, and the inbox's lane and key fingerprint. Above the tabs and as a count on the Vault button: what this browser holds that the vault does not yet (assets/vault-pane/pending.js; the wire's seen stories from assets/vault-pane/wire-state.js), with Update the vault one press away; the keys of an open account live in memory and in sessionStorage for the tab's life. Local storage stays primary; the vault is updated when the reader presses Update. Two ways in (card 059): Open with the passkey, after which, when the vault knows devices and this browser is none of them, the pane asks which device this is (an existing one is adopted: its id, label and records become this browser's own; NV.setDeviceBranch) and then merges what the vault holds on its own (inbound() in sync.js counts it; the strip and the Vault tab show it with Bring them here); or Connect with a link, send only. Every device-file write is combine(prev, extract(local)). At the drain, a File under choice per sending browser, refile() re-tags the batch, and the choice is kept as aliases in the master's inbox.json. Design: /admin/notes/2026-10-13__open-or-connect-a-vault.md. "
             f"The designs are https://{HOST}/{NOTE} and https://{HOST}/{NOTE2}; the tests are admin/build/test_sync.mjs (the logic), test_pane.mjs (two devices in Chromium against a mock of the vault API) "
             "and test_notes.mjs (the feedback loop end to end, including the sgit CLI reading the lane with the read key).")
    return newsroom_page("vault/index.html", "Your vault",
                         "Your notes on what you read, kept as you read and sent to the newsroom down a lane of their own; the reading account carried between your devices through an encrypted vault that opens with your passkey; every key of your account.",
                         body, eyebrow="Your vault · beta", crumbs=(("Account", "account/index.html"),),
                         lead="Your notes and your reading account live in this browser. The vault is their second home, one you own and every device of yours reaches with a passkey; the lane is how the notes you choose reach the newsroom without the rest. Open it on the right, or connect a browser that cannot; read, tap, update, send.",
                         agent=agent)


def send_page():
    """vault/send.html: the sending side of the inbox (card 049), for a browser that holds the link and no passkey."""
    body = """<div id="send-mount" class="send-box"><p class="dim">Loading&hellip;</p></div>
<noscript><p>Sending needs a script: this page encrypts in your browser and writes nothing anywhere without one.</p></noscript>
<script type="module">
import { mountSend } from '../assets/vault-pane/send.js';
mountSend(document.getElementById('send-mount'));
</script>
<h2 id="what">What this page does</h2>
<p>Your vault opens with your passkey, and some browsers cannot reach it: one an app opens a link in, one signed in to nothing, an old iPad. What they hold, your reads, your notes and the stories you saw on the wire, would stay there. This page sends it to your vault without the passkey.</p>
<ul>
<li><b>The link</b> comes from your vault, in the pane&rsquo;s Vault tab, as a URL, as text or as a QR code. It carries two things: where to write, an append lane on your reader vault, and the public key to encrypt to. Nothing else: not your vault&rsquo;s key, not its read key.</li>
<li><b>What is sent</b> is this browser&rsquo;s own records, as one file, encrypted here to that key (RSA-OAEP and AES-256-GCM, sgit&rsquo;s hybrid envelope) and appended to the lane. The vault server sees ciphertext, a size and a time.</li>
<li><b>This browser can add and cannot read.</b> The lane answers a write with <code>{"ok": true}</code> and nothing more; not even what was sent can be read back from here.</li>
<li><b>Your vault takes it in</b> the next time you open it with your passkey: the Vault tab lists what is waiting, from which browser and when, and brings it in on one press, with this browser as its author.</li>
<li><b>Nothing is removed from this browser.</b> The count of what is only here goes to zero once it is sent; the records stay.</li>
</ul>
<p>Anyone holding the link can add to the lane, and nobody holding it can read anything. Your vault shows what arrived before it brings it in, and can make a new link, which stops the old one. The brief is <a href="../articles/sixteen-notes-i-did-not-want-to-lose.html">Sixteen notes I did not want to lose</a>; the design is <a href="../admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md">in the note</a>.</p>
"""
    agent = ("vault/send.html is the sending side of the reader's inbox (assets/vault-pane/send.js, assets/vault-pane/inbox.js). The link, in the fragment, is "
             "sgi1.&lt;reader vault id&gt;.&lt;append token, hex&gt;.&lt;RSA-OAEP 3072 public key, SPKI, base64url&gt;; the page keeps it in localStorage sgit.inbox.link and removes it from the address. "
             "It extracts this browser's own records as a device file (assets/vault-pane/sync.js format, v 1), wraps it as {kind: 'sgit-newsroom-inbox/v1', to: &lt;key fingerprint&gt;, sent_at, file}, "
             "seals it with sgit's hybrid envelope v2 and POSTs {append_token, payload} to https://dev.send.sgraph.ai/api/vault/append/write/&lt;vault id&gt;. The reader's vault pane drains the lane with the enum key "
             "and the private key, both in the master vault.")
    return newsroom_page("vault/send.html", "Send to my vault",
                         "Send what this browser holds, your reads, notes and the stories you saw, to your vault, from a browser that cannot reach your passkey: encrypted here, appended to a lane it can write to and never read.",
                         body, eyebrow="Your vault · send from any browser", crumbs=(("Account", "account/index.html"), ("Your vault", "vault/index.html")),
                         lead="A browser with no passkey can still keep what it holds: it encrypts it to your vault's key and appends it to your vault's inbox, which it can write to and never read.",
                         agent=agent, head='<link rel="stylesheet" href="../assets/vault-pane/send.css">')


def browse_page():
    """vault/browse.html: your vaults, opened, with the session the pane keeps (card 079)."""
    import json
    demo = json.loads((ROOT / "admin/content/vaults/vault-viewer-demo.json").read_text())
    viewer = json.loads((ROOT / "admin/content/vaults/vault-viewer.json").read_text())
    demo_id, demo_hex, viewer_id = demo["vault_id"], demo["read_key"][-64:], viewer["vault_id"]
    body = f"""<div id="browse-mount" class="browse"><p class="dim">Loading&hellip;</p></div>
<noscript><p>This page opens your vaults in your browser and needs a script to do it.</p></noscript>
<script type="module">
import {{ mountBrowse }} from '../assets/vault-pane/browse.js';
mountBrowse(document.getElementById('browse-mount'));
</script>
<h2 id="demo">The viewer, on a demo account</h2>
<p>A reader vault made for showing, with a made-up account, linked to the newsroom&rsquo;s viewer exactly as yours is: press to open it in the SG/Vault app, read-only, with its published read key. What you see is the viewer, loaded from its own vault <code>{viewer_id}</code> through the link, reading the demo vault&rsquo;s records.</p>
<p><button type="button" class="btn" id="browse-demo-open">Open the demo in the SG/Vault app</button></p>
<div class="sgv-host" id="browse-demo"></div>
<script type="module">
import {{ mountEmbed }} from '../assets/vault-pane/sg-embed.js';
document.getElementById('browse-demo-open').addEventListener('click', function () {{ this.remove(); mountEmbed(document.getElementById('browse-demo'), {{ vaultId: '{demo_id}', readKeyHex: '{demo_hex}', mode: 'app', label: 'The demo reader vault, in App Mode' }}) }});
</script>
<p class="small"><img src="../engineering/shots/079-viewer-in-the-sg-app.png" alt="The demo reader vault in the SG/App, read-only: the newsroom's viewer shows a balance of £4.84, 3 pages read, 2 notes, 2 devices, the reading and the notes" style="max-width:100%;border:1px solid var(--line, #e3e5ea);border-radius:8px"></p>
<h2 id="what">What this page shows</h2>
<ul>
<li><b>Every vault of your account</b>, opened here with the keys the pane holds for this tab: the reader vault (your reads, notes and devices, one file per device, and the link to the newsroom&rsquo;s viewer), the lane (the notes you sent to the newsroom), the master (the keys of the others) and this door (the master&rsquo;s key). The master&rsquo;s and the door&rsquo;s files open only behind Reveal.</li>
<li><b>The files and the commits.</b> The tree as published now, any file&rsquo;s contents, and the commits, newest first; pick one to see the tree and the files as they were.</li>
<li><b>The reader vault in the SG/Vault app</b>, on a press: its read key is handed to the app at dev.vault.sgraph.ai over its embed protocol, never in an address, never stored, and it cannot write. App Mode opens the vault with its app: <b>the newsroom&rsquo;s viewer</b>, a vault of its own that every reader vault links read-only and opens with. The vault browser there shows the files, the SGit history and the settings.</li>
<li><b>Nothing is written from this page</b>, and nothing leaves the browser but requests for ciphertext; every one is listed in the pane&rsquo;s Calls tab, named and, on a press, decrypted.</li>
</ul>
<p>The design is <a href="../admin/notes/2026-10-16__the-vault-opened.md">the vault, opened</a>; the viewer&rsquo;s source is <a href="vault-app/README.md">vault/vault-app/</a>.</p>
"""
    agent = ("vault/browse.html opens the reader's vaults in the page with the session the vault pane keeps in sessionStorage (sgit.vault.session: the door): "
             "assets/vault-pane/browse.js unlocks the door, the master, the reader vault and the lane with the vendored library, lists every file (vault.listFolder), "
             "reads any file (master and door behind Reveal), lists the commits (vault.logCommits) and the files at a commit (listTreeAt, readFileAt). It writes nothing. "
             "The reader vault also opens in the SG/Vault app (dev.vault.sgraph.ai) through assets/vault-pane/sg-embed.js (the embed protocol, as sgit.ai's vault-ui-embed.js uses it), with the vault's read key handed over postMessage; "
             "App Mode opens the shared viewer, a vault linked read-only into each reader vault (newsroom-viewer.link.json, .vault/owner/ro-links.json, .vault/app.json, index.html). "
             "The viewer's source is vault/vault-app/ and its public record admin/content/vaults/vault-viewer.json, published by admin/build/viewer_vault.mjs.")
    return newsroom_page("vault/browse.html", "Your vaults, opened",
                         "Every vault of your account, opened in your browser: the files, any file's contents, the commits, and your reader vault in the SG/Vault app with the newsroom's viewer.",
                         body, eyebrow="Your vault · browse", crumbs=(("Account", "account/index.html"), ("Your vault", "vault/index.html")),
                         lead="What your vaults hold, file by file and commit by commit, opened here with your keys. The server only ever had the ciphertext.",
                         agent=agent, head='<link rel="stylesheet" href="../assets/vault-pane/browse.css">')


def main():
    changed = write("vault/browse.html", browse_page())
    print(f"vault_page: {'written' if changed else 'unchanged'} vault/browse.html")
    changed = write("vault/index.html", page())
    print(f"vault_page: {'written' if changed else 'unchanged'} vault/index.html")
    changed = write("vault/send.html", send_page())
    print(f"vault_page: {'written' if changed else 'unchanged'} vault/send.html")


if __name__ == "__main__":
    main()
