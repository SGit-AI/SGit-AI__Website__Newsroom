#!/usr/bin/env python3
"""The passkey lab: a page of proofs of concept for "The passkey opens the vault".

    python3 admin/build/passkey_lab.py        # writes passkey/index.html (lab.js, lab.css and vectors.json are served from the API host)

The article (articles/the-passkey-opens-the-vault.html) designs a reader account with no server and no sign-in:
a passkey's PRF bytes derive a door vault, the door holds the master vault's key, the master holds the rest. Before
any of it is built into the reader's account, this page lets a person try each piece in their own browser: make a
passkey for this site, get the PRF bytes and see that they are the same on another device, derive the door and
sgit's keys from them, make a recovery code, check the browser against sgit's own Python, and, with an access key,
create the door on the vault server and open it again. The code is passkey/lab.js; the vectors come from
admin/build/passkey_vectors.py. Nothing on the page touches the reading account.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, HOST  # noqa: E402
from api import api_url  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
# The vault library that runs dev.vault.sgraph.ai, vendored at v0.2.3 and loaded from this origin in VENDOR.md's order,
# then the one local extension. Plain scripts, each declaring a global; lab.js reaches them through assets/newsroom-vault.js.
VENDORED = ["sg-send/sg-send-crypto.js", "sg-send/sg-send.js", "sg-vault/sg-vault-crypto.js", "sg-vault/sg-vault-object-store.js",
            "sg-vault/sg-vault-ref-manager.js", "sg-vault/sg-vault-commit.js", "sg-vault/sg-vault.js", "sg-vault/sg-vault--file-ops.js",
            "sg-vault/sg-vault--folder-ops.js", "sg-vault/sg-vault--sync.js", "sg-vault/sg-vault--history.js", "sg-vault/sg-vault--branches.js"]
HEAD = (f'<link rel="stylesheet" href="{api_url("passkey/lab.css")}">\n'
        + "".join(f'<script src="{api_url("assets/vendor/sg-vault/v0.2.3/" + f)}"></script>\n' for f in VENDORED)
        + f'<script src="{api_url("assets/vendor/sg-vault/local/sg-vault--create-with-id.js")}"></script>\n')


def card(n, title, what, acts, extra=""):
    return f"""<section class="poc" id="poc{n}">
<h2>{n}. {title}</h2>
<p class="what">{what}</p>
<div class="acts">{acts}</div>
{extra}<div class="out" id="poc{n}-out"></div>
</section>
"""


def page():
    body = f"""<div class="note lab"><b>A lab, not a feature.</b> Nothing here changes your reading account, your balance or your personas. The page stores one public thing in this browser, the id of a passkey it made, so it can say so next time. Keys it derives are shown behind a reveal and kept in the page&rsquo;s memory only; an access key you paste is kept the same way and forgotten when the page closes. The page loads no code from anywhere else, and every call it makes to a vault server is listed as it happens.</div>
<p>The design is in <a href="../articles/the-passkey-opens-the-vault.html">The passkey opens the vault</a>: a passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site; from those bytes the browser <em>computes</em> the key and the address of a small door vault, so nothing has to be stored to be found; the door holds the master vault&rsquo;s key. Each card below is one step of that, as a thing you can press.</p>

{card(0, "What this browser can do", "WebAuthn, the platform authenticator, and whether the browser says it supports the PRF extension. Nothing to press: it is read when the page opens.", "")}
{card(1, "Make a passkey for this site", f"<code>navigator.credentials.create()</code> with <code>rp.id</code> set to this host, a resident key, user verification required, and the <code>prf</code> extension. The passkey is stored by your provider (Google Password Manager, iCloud Keychain, Windows Hello, a hardware key, or the browser&rsquo;s own store); the page learns a credential id, a public key and whether PRF is on. It never learns who you are.",
     '<button type="button" class="btn primary" id="poc1-go">Make a passkey</button><span class="dim">You will be asked for a touch, a face or a PIN.</span>',
     '<div class="ladder" id="poc1-ladder" hidden><b>No PRF bytes from this passkey.</b> The article&rsquo;s ladder, in order:<ol><li>Sign in to a passkey provider (Google Password Manager in Chrome, iCloud Keychain in Safari), so the passkey syncs and PRF is available.</li><li>Use your phone by QR: a passkey on the phone, one scan at a time.</li><li>Plug in a hardware key.</li><li>Stay on this device: the browser&rsquo;s own copy of the reading account keeps working, and the recovery code (4) is the way back.</li></ol></div>')}
{card(2, "Touch it: the PRF bytes", "<code>navigator.credentials.get()</code> with the fixed input, the SHA-256 of a public string. The authenticator returns 32 bytes computed from a secret it keeps for this site and this passkey. The same passkey gives the same bytes on every device it syncs to, through the same kind of path; that is the whole trick. Through a different path (a phone over QR, instead of the provider on the device) the same passkey can give different bytes, which a test here found on 12 October 2026; the result shows which path answered, and the design gives each path its own door: <a href='../admin/notes/2026-10-12__one-door-per-passkey-path.md'>one door per passkey path</a>.",
     '<label>Input text <input type="text" id="poc2-input" class="mono"></label><button type="button" class="btn primary" id="poc2-go">Get the PRF bytes</button>',
     '<div class="ladder" id="poc2-compare" hidden>Your fingerprint here: <b class="mono" id="poc2-mine"></b>. From another device: <input type="text" id="poc2-other" class="mono" placeholder="8 hex characters" maxlength="8"> <button type="button" class="btn sm" id="poc2-cmp-go">Compare</button> <span id="poc2-cmp-out" class="dim"></span></div>')}
{card(3, "From the bytes, the door", "The article&rsquo;s derivation, made exact: HKDF to a seed, a passphrase and an 8-character vault id; then sgit&rsquo;s own derivation of the read key and the write key, PBKDF2-HMAC-SHA256 at 600,000 iterations each, timed on this device. The door&rsquo;s key is not stored anywhere: it comes out the same every time.",
     '<button type="button" class="btn" id="poc3-go">Derive again</button><span class="dim">Runs by itself after 2.</span>')}
{card(4, "A recovery code: the second door", "26 characters of base32, 128 bits, made by the page and in the real flow shown once. In place of the PRF bytes it derives a second door to the same master, for the day every passkey is gone.",
     '<button type="button" class="btn primary" id="poc4-go">Make a recovery code</button>',
     '<div class="ladder">Type a code back: <input type="text" id="poc4-code" class="mono" placeholder="XXXX-XXXX-…"> <button type="button" class="btn sm" id="poc4-check">Which door?</button> <label class="dim"><input type="checkbox" id="poc4-use"> use it as the door in 3 and 6 when there is no passkey</label> <span id="poc4-check-out" class="dim"></span></div>')}
{card(5, "Test vectors: the browser and sgit agree", f"The same derivation from a fixed, fake PRF output, compared value by value with what sgit&rsquo;s own Python produced (<a href='{api_url('passkey/vectors.json')}'>vectors.json</a>, from <code>admin/build/passkey_vectors.py</code>). Runs when the page opens. If any line is wrong, the browser and the command line would open different vaults.",
     '<span id="poc5-use" hidden><button type="button" class="btn" id="poc5-use-go">Use the test vector as the door in 3 and 6</button> <span class="dim">for trying the server without a passkey</span></span>')}
<section class="poc" id="poc6" hidden>
<h2>6. Real vaults: the door, the master and the reader vault</h2>
<p class="what">With the door from 3 (or the recovery code from 4, or the test vector), the vault library that runs dev.vault.sgraph.ai, <a href="{api_url('assets/vendor/sg-vault/v0.2.3/VENDOR.md')}">vendored here</a> and loaded from this origin, creates and opens real sgit vaults: the <b>door</b> at its derived address, holding the master&rsquo;s key and a record of where it came from (kind, provider, path, credential id, device, date); the <b>master</b>, made at random, holding the reader vault&rsquo;s key and the list of doors; the <b>reader vault</b>, where a note is written and read back. Every vault made here is one <code>sgit clone</code> opens, with write access, from the key shown behind each reveal. Writing needs an <b>access key</b> for the server, which is the thing a reader will buy; opening and reading need nothing.</p>
<div class="acts">
  <label>Server <select id="poc6-server"><option value="https://dev.send.sgraph.ai">dev.send.sgraph.ai</option><option value="https://send.sgraph.ai">send.sgraph.ai</option></select></label>
  <label>Access key <input type="password" id="poc6-access" autocomplete="off" placeholder="kept in memory only"></label>
  <label>This device <input type="text" id="poc6-device" maxlength="40" placeholder="a label for the door&rsquo;s record"></label>
</div>
<div class="acts">
  <button type="button" class="btn" id="poc6-check">Is there a door at <span class="mono" id="poc6-id"></span>?</button>
  <button type="button" class="btn primary" id="poc6-create" disabled>Create the account: door, master, reader vault</button>
  <button type="button" class="btn" id="poc6-unlock">Unlock through this door</button>
  <button type="button" class="btn" id="poc6-add" disabled>Add the recovery code as a second door</button>
</div>
<div class="acts">
  <label>A note <input type="text" id="poc6-note" maxlength="200" placeholder="goes into the reader vault, notes/"></label>
  <button type="button" class="btn" id="poc6-write" disabled>Write it and read it back</button>
</div>
<p class="dim">An address with no door says so; it is not an error. A vault id is never destroyed, because a destroyed id can never be used again and a door&rsquo;s is derived. The test vector&rsquo;s door has the same address for everyone, so on the real server only the first person can create it. Moving the reading account into the reader vault is the next step and is not built.</p>
<div class="out" id="poc6-out"></div>
<ul class="calls" id="poc6-log" hidden></ul>
</section>

<h2 id="notes">What this lab is, and is not</h2>
<ul>
<li><b>The relying party id is this host.</b> On newsroom.sgit.ai a passkey made here is for newsroom.sgit.ai exactly, as the article&rsquo;s trust boundary asks; it does not work on sgit.ai or on any other site. The derivation&rsquo;s constants name newsroom.sgit.ai whichever host runs the page, so the test vectors are the same everywhere.</li>
<li><b>Where the passkey lives decides what you get.</b> Card 1 shows whether the passkey is backup-eligible, which is the browser&rsquo;s word for synced. A clean browser with no provider may make a passkey that signs and returns no PRF bytes; card 2 says so if it happens, and card 1 shows the ladder.</li>
<li><b>A door per path, not per passkey.</b> On 12 October 2026 one Google Password Manager passkey gave one set of bytes through the provider on a Mac and on an iPhone, and a different set, consistently, when a phone answered a QR code from a Mac or an iPad: same credential id, same user handle, same input. Apple&rsquo;s developer forums carry the same symptom for iCloud Keychain passkeys since late 2024, with a fix announced and a tester reporting it persisting. A second passkey in iCloud Keychain gave the same bytes on a Mac, a current iPad and a current iPhone, in Safari and in Chrome, which is the common case; an older iPad that could not use it locally offered only the QR path. The design therefore treats every distinct set of bytes as its own door to the same master, adds a door while unlocked on a device where both paths run (a Mac with Chrome runs both in one session), and uses the recovery code to bring a new path in where no door opens. The finding, the bug and the revised design are written out in <a href="../admin/notes/2026-10-12__one-door-per-passkey-path.md">one door per passkey path</a>.</li>
<li><b>Not built here:</b> the master vault, the newsroom vault, moving the reading account into it, adding a second path or passkey as a door, retiring a door, and anything that signs the reader in. The brief&rsquo;s phase five is where those land, after the move.</li>
<li><b>The door record this lab writes</b> is one sgit object (<code>obj-cas-imm-&hellip;</code>, content-addressed), encrypted the way sgit encrypts, so sgit&rsquo;s own code can decrypt it; it is not yet a commit in a tree, so <code>sgit clone</code> of the door would show an empty history. The real door will be a vault with one committed file.</li>
<li><b>Tests:</b> <code>admin/build/test_passkey.mjs</code> drives the page in Chromium with a virtual authenticator that has PRF, checks the derivation against the vectors, and runs the server flow against a stand-in server; the real server is tried by a person with an access key.</li>
</ul>
<script type="module">
import {{ lab }} from '{api_url('passkey/lab.js')}';
lab({{ vectors: '{api_url('passkey/vectors.json')}' }});
</script>
"""
    agent = (f"A lab page for the design in https://{HOST}/articles/the-passkey-opens-the-vault.html: in a browser, make a passkey with the PRF extension, "
             "get the PRF bytes, derive a door vault's passphrase and id (HKDF) and sgit's read and write keys (PBKDF2, 600,000 iterations), make a recovery "
             f"code, compare with sgit's Python at https://{HOST}/passkey/vectors.json, and with an access key create the door on a vault server and open it. "
             "It stores nothing but a passkey id; it does not touch the reading account. The derivation is written out at the top of https://" + HOST + "/passkey/lab.js.")
    return newsroom_page("passkey/index.html", "The passkey lab",
                         "Try the pieces of a reader account with no server: make a passkey with PRF, see the same bytes on every device through the same path, derive a door vault and sgit's keys from them, make a recovery code, check against sgit's own code, and create the door on a vault server.",
                         body, eyebrow="A lab: the passkey opens the vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="Each step of the design, as a thing you can press in your own browser: a passkey, its PRF bytes, the door derived from them, a recovery code, and the door created on a vault server.",
                         agent=agent, head=HEAD)


def main():
    changed = write("passkey/index.html", page())
    print(f"passkey_lab: {'written' if changed else 'unchanged'} passkey/index.html")


if __name__ == "__main__":
    main()
