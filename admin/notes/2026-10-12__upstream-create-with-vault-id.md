# Upstream issue for SGraph-AI__App__Send: `SGVault.create(…, { vaultId })`

**For:** https://github.com/the-cyber-boardroom/SGraph-AI__App__Send, the vault UI library at
`sgraph_ai_app_send__ui__vault/v0/v0.2/v0.2.3/_common/js/lib/sg-vault/sg-vault.js`.
**From:** newsroom.sgit.ai, 12 October 2026. **Local patch until it ships:**
`assets/vendor/sg-vault/local/sg-vault--create-with-id.js` in SGit-AI__Website__Newsroom.
**Also listed** as item 4 of "What the library needs" on https://sgit.ai/docs/vault/vault-from-javascript.html.

## The ask

Let `SGVault.create(sgSend, passphrase, options)` take `options.vaultId`. When it is given, use it in
place of the random 8-character id drawn at step 1, validate it as `parseVaultKey` does
(`^[a-z0-9]{4,24}$`), and refuse to create when a vault already exists at that address.

## Why

The passkey design (https://sgit.ai/articles/the-passkey-opens-the-vault.html) computes a small door
vault's **id and passphrase** from a passkey's PRF bytes, so that nothing has to be stored to find it:
the browser derives the address, opens the door, and finds the master vault's key inside. Such a vault
can be opened by the library today (`SGVault.open` takes any `passphrase:vault_id`) and cannot be created
by it, because `create` always draws its own id. newsroom.sgit.ai had to add a static method to make
doors as real vaults instead of raw objects.

## The shape we are running

```js
// identical to create() except for the id, plus the address check; cloneBranch as open() takes it
SGVault.createWithId(sgSend, passphrase, vaultId, { name, description, cloneBranch })
```

Before writing anything it makes the two reads `open` makes before it loads a tree: the branch index,
then the named ref it names (or the derived one). If either exists, or either exists and cannot be
decrypted, it throws with `code: 'EEXISTS'`; "HEAD ref missing" is the one answer that means free. It
then resets the ref manager's raw-ref cache, so that the first `pushIfMatch` after creation arms the
compare-and-swap exactly as it does after `create()`.

Suggested upstream form:

```js
static async create(sgSend, passphrase, options = {}) {
    const vault = new SGVault(sgSend)
    vault._passphrase = passphrase
    if (options.vaultId) {
        if (!/^[a-z0-9]{4,24}$/.test(options.vaultId)) throw new Error('vault_id must be 4-24 lowercase alphanumeric characters')
        vault._vaultId = options.vaultId
    } else {
        // the existing random draw
    }
    // ... derive keys, init managers ...
    if (options.vaultId && await vault._addressTaken()) { const e = new Error(`vault ${vault._vaultId} already exists`); e.code = 'EEXISTS'; throw e }
    // ... the rest unchanged
}
```

## Two things seen while doing this, for the same change

- `create` hard-codes the clone branch `'web-ui'`; `open` takes `options.cloneBranch`. Letting `create`
  take it too keeps one client's clone ref apart from every other browser's from the first commit.
- The random draw in `create` is `alphabet[b % 36]` over 8 random bytes, which favours the first 4
  characters of the alphabet slightly (256 is not a multiple of 36). Rejection sampling (`b < 252`) is
  what sgit's own `generate_vault_key` does and what the newsroom's `randomPassphrase` does.

## Tests that would show it

In the newsroom's `admin/build/test_vault.mjs`, against a mock of the vault API: a door created at a
derived id is a vault with a named ref, a branch index and content-addressed objects; `sgit clone` of it
from the prefixed key reads every file; a second `createWithId` at the same address is refused with
`EEXISTS`; `open` of an address nobody has used fails with "HEAD ref missing" and nothing else.
