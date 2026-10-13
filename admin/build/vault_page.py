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
<div class="note"><b>A beta.</b> The pane on the right is the vault, in three tabs: <b>This page</b>, your notes on what you read and the lane that carries the ones you choose to the newsroom; <b>Vault</b>, the reading account this browser keeps, carried between your devices through an encrypted vault that opens with your passkey; <b>Keys</b>, every vault of your account with its key. It is on every page, behind the <b>Vault</b> button beside the balance. Nothing about the meter changes; the vault is a second home for its data that you keep current.</div>
<h2 id="feedback">The feedback loop</h2>
<ol>
<li><b>Read, and tap.</b> On any page, open the pane; it stays open from page to page until you close it. Above the chips it says what this browser knows about the page: read how many times, when, how far, what it cost. Select a phrase if one is the point. One tap keeps a note in this browser: <em>Done</em> (read it, done with it, off your lists), <em>Read later</em>, <em>Not for me</em>, <em>More like this</em>, <em>Liked</em>, <em>Wrong</em>, <em>Fix this</em>, <em>Idea</em>, with the phrase you had selected. Under the chips, <b>Write to the newsroom</b> takes a message for the newsroom&rsquo;s agent, about the page or anything else: <em>Save and send</em> keeps it and sends it in one press. On <a href="../wire/index.html">the wire</a>, the decision is at each story, and a decided story folds to its headline. The <b>Reading</b> tab lists every page read here, newest first, with its decision, and folds the done ones away.</li>
<li><b>Update the vault</b>, in the Vault tab, when you like: your notes travel with your reads to your other devices, in this device&rsquo;s own file.</li>
<li><b>Send to the newsroom</b> the notes you have not sent. The first send makes a <b>lane</b>: a vault of its own, whose write key stays in your master and whose <b>read key</b> the pane shows. Hand that key to the newsroom once, in the open; it reads the lane and cannot write to it, and nothing else of yours is in it. Later sends go to the same lane.</li>
<li><b>The newsroom reads the lane</b> with <code>sgit clone</code> or <code>admin/build/lane.py</code>, and answers in the open: a fix in a release, a version of an article. Nothing comes back through the lane.</li>
</ol>
<p>The design, the record, what is not built and the experiments to run are in <a href="../{NOTE2}">the feedback loop</a>.</p>
<h2 id="loop">The reading account, between devices</h2>
<ol>
<li><b>On this device,</b> press <em>Enable with your passkey</em>. The first time there is no door at the derived address: paste an access key and <em>Create the account</em>. Three vaults are made (a door, a master, a reader vault), the access key goes into the master, and a recovery code is shown once.</li>
<li><b>Read.</b> Open a few articles; the meter charges them into local storage as it always has.</li>
<li><b>Update the vault.</b> This device&rsquo;s records are written as one file, one commit, published.</li>
<li><b>On another device,</b> enable with the same passkey. The door is there, the master brings the access key, the reader vault opens. <em>Across your devices</em> lists the first one. <em>Bring that device&rsquo;s activity here</em> adds its records to this browser and the meter shows the consolidated balance.</li>
<li><b>Read and update there too.</b> Two files, one view, the same figures on both devices.</li>
</ol>
<h2 id="principles">The principles</h2>
<ul>
<li><b>Local storage stays primary</b>, written in real time by the meter; the vault is updated when you ask.</li>
<li><b>Records, never totals.</b> Reads, top-ups and personas go in raw; reads, spend, declined, credit and balance are recomputed from them with one starting credit for the account.</li>
<li><b>One file per device, written only by that device.</b> Two devices never write the same file, so there is nothing to merge and no conflict by construction. The consolidated view is computed from all the files each time.</li>
<li><b>Brought-in records keep their author.</b> What arrives from another device is tagged with it, and the next sync from here writes only this device&rsquo;s own records back.</li>
<li><b>Nothing is typed twice.</b> The access key is pasted once and lives in the master; every other device gets it by opening the master with its passkey, or with the recovery code once.</li>
</ul>
<p>The design, the data layout, what is not synced and why, and the experiments to run next are in <a href="../{NOTE}">the activity vault</a>. The pieces it is made of are in <a href="../passkey/index.html">the passkey lab</a>, and the vault code is the library that runs dev.vault.sgraph.ai, <a href="../assets/vendor/sg-vault/v0.2.3/VENDOR.md">vendored here</a>.</p>
<h2 id="keys">Your keys</h2>
<p>The Keys tab lists every vault of your account with its key, shown only when you press Reveal: the door of this device and the other doors, the master, the reader vault, the lane and its read key. Any of them opens on its own, with <code>sgit clone</code> or in the vault app. A key opens that vault to whoever holds it, and the master&rsquo;s opens everything, so handle them like the recovery code. The lane&rsquo;s read key is the one thing meant to be handed over.</p>
<h2 id="data">What leaves this browser</h2>
<p>Ciphertext, to the vault server (dev.send.sgraph.ai), when you create, update, send or open: every file is encrypted here under keys derived from your passkey, and the server sees requests, sizes and times. The pane lists every call as it happens. The access key travels only as a request header to that server. Your notes leave this browser only when you press Update (to your own reader vault) or Send (to your own lane). Nothing goes anywhere else.</p>
"""
    agent = (f"The vault pane (assets/vault-pane/vault-pane.js) has three tabs. This page: the reader's notes (assets/vault-pane/notes.js; one tap at a piece: read-later, not-for-me, "
             "more-like-this, liked, wrong, fix, idea, done, follow-up, with words and the selected phrase, or a message alone, kind note, written under Write to the newsroom; kept in localStorage sgit.notes.v1) and Send to the newsroom, which writes the notes not yet "
             "sent into a lane, a vault of its own whose key is in the master (lane.json) and whose read key the reader hands over; the newsroom reads it with "
             "`NEWSROOM_LANE_KEY=<read key> python3 admin/build/lane.py`. Vault: the reading account carried between devices through an sgit vault opened with a passkey: "
             "a door derived from the PRF bytes (assets/door.js), the master and the reader vault (assets/newsroom-vault.js); the reader vault holds "
             "activity/account.json (one starting credit) and activity/devices/<device>.json (that device's raw reads, top-ups, personas and notes, rewritten whole on each sync); "
             "totals are recomputed from the records (assets/vault-pane/sync.js). Keys: every vault with its key behind Reveal. Local storage stays primary; the vault is updated when the reader presses Update. "
             f"The designs are https://{HOST}/{NOTE} and https://{HOST}/{NOTE2}; the tests are admin/build/test_sync.mjs (the logic), test_pane.mjs (two devices in Chromium against a mock of the vault API) "
             "and test_notes.mjs (the feedback loop end to end, including the sgit CLI reading the lane with the read key).")
    return newsroom_page("vault/index.html", "Your vault",
                         "Your notes on what you read, kept as you read and sent to the newsroom down a lane of their own; the reading account carried between your devices through an encrypted vault that opens with your passkey; every key of your account.",
                         body, eyebrow="Your vault · beta", crumbs=(("Account", "account/index.html"),),
                         lead="Your notes and your reading account live in this browser. The vault is their second home, one you own and every device of yours reaches with a passkey; the lane is how the notes you choose reach the newsroom without the rest. Enable it on the right, read, tap, update, send.",
                         agent=agent)


def main():
    changed = write("vault/index.html", page())
    print(f"vault_page: {'written' if changed else 'unchanged'} vault/index.html")


if __name__ == "__main__":
    main()
