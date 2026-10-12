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


def page():
    body = f"""<script>document.documentElement.setAttribute('data-vault-open', '')</script>
<div class="note"><b>A beta.</b> The pane on the right is the vault: the reading account this browser keeps, carried between your devices through an encrypted vault that opens with your passkey. It is on every page, behind the <b>Vault</b> button beside the balance. Nothing about the meter changes; the vault is a second home for its data that you keep current.</div>
<h2 id="loop">The loop</h2>
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
<h2 id="data">What leaves this browser</h2>
<p>Ciphertext, to the vault server (dev.send.sgraph.ai), when you create, update or open: every file is encrypted here under keys derived from your passkey, and the server sees requests, sizes and times. The pane lists every call as it happens. The access key travels only as a request header to that server. Nothing goes anywhere else.</p>
"""
    agent = (f"The vault pane (assets/vault-pane/vault-pane.js) carries the reading account between a reader's devices through an sgit vault opened with a passkey: "
             "a door derived from the PRF bytes (assets/door.js), the master and the reader vault (assets/newsroom-vault.js). The reader vault holds "
             "activity/account.json (one starting credit) and activity/devices/<device>.json (that device's raw reads, top-ups and personas, rewritten whole on each sync); "
             "totals are recomputed from the records (assets/vault-pane/sync.js). Local storage stays primary; the vault is updated when the reader presses Update. "
             f"The design is https://{HOST}/{NOTE}; the tests are admin/build/test_sync.mjs (the logic) and test_pane.mjs (two devices in Chromium against a mock of the vault API).")
    return newsroom_page("vault/index.html", "Your vault",
                         "The reading account this browser keeps, carried between your devices through an encrypted vault that opens with your passkey: records, never totals; one file per device; the vault updated when you ask.",
                         body, eyebrow="Your vault · beta", crumbs=(("Account", "account/index.html"),),
                         lead="The reading account lives in this browser. The vault is its second home, one you own and every device of yours reaches with a passkey. Enable it on the right, read, update; then do the same on another device.",
                         agent=agent)


def main():
    changed = write("vault/index.html", page())
    print(f"vault_page: {'written' if changed else 'unchanged'} vault/index.html")


if __name__ == "__main__":
    main()
