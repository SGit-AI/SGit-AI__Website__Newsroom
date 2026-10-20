/**
 * calls.js: what a call to the vault server is, and what it carries (card 078).
 *
 * The pane lists every call this page makes to dev.send.sgraph.ai. Each is named from its address (a read, a write,
 * a batch, an append-lane operation; an object, a ref, a branch index), and, when the vault it belongs to is open
 * in this page, decrypted on demand with that vault's read key and named again from what is inside: a commit (its
 * message, parents and tree), a tree (its entries, with their names decrypted), a ref (the commit it points at), or
 * a file (its text). Nothing here sends anything; decoding uses keys the page already holds and shows what the
 * server stored, which is ciphertext.
 *
 * The objects, as the vendored library writes them (assets/vendor/sg-vault/v0.2.3):
 *   bare/data/obj-cas-imm-<12 hex>   an immutable object: a commit (commit_v2), a tree (tree_v1) or a file's bytes
 *   bare/refs/ref-pid-muw-<12 hex>   the published ref, {commit_id}; ref-pid-snw-… is a device's working ref
 *   bare/indexes/idx-pid-muw-<…>     the branch index
 *
 * @module vault-calls
 */

export const KINDS = {
    commit: 'a commit', tree: 'a tree (a folder listing)', ref: 'a ref (which commit is current)', 'clone-ref': 'a working ref (this device’s branch)',
    'branch-index': 'the branch index', object: 'an object', file: 'a file’s contents', append: 'an append-lane operation', list: 'a listing', info: 'vault info', other: 'a call',
}

/** A file id, named from its shape alone. */
export function kindOfFileId(id) {
    const s = String(id || '')
    if (/(^|\/)obj-cas-imm-[0-9a-f]+$/.test(s)) return 'object'
    if (/(^|\/)ref-pid-muw-/.test(s)) return 'ref'
    if (/(^|\/)ref-pid-snw-/.test(s)) return 'clone-ref'
    if (/(^|\/)idx-pid-/.test(s)) return 'branch-index'
    return 'file'
}

/** A call, named from its method and address: { op, vaultId, fileId, kind, short }. */
export function describeCall(method, url, endpoint = 'https://dev.send.sgraph.ai') {
    let p = String(url || '')
    if (p.startsWith(endpoint)) p = p.slice(endpoint.length)
    p = p.split('?')[0]
    const seg = p.split('/').filter(Boolean).map(x => { try { return decodeURIComponent(x) } catch (e) { return x } })
    const out = { op: 'other', vaultId: '', fileId: '', kind: 'other', short: p }
    if (seg[0] === 'api' && seg[1] === 'vault') {
        const op = seg[2]
        if (op === 'read' || op === 'write' || op === 'delete') { out.op = op; out.vaultId = seg[3] || ''; out.fileId = seg.slice(4).join('/'); out.kind = kindOfFileId(out.fileId) }
        else if (op === 'batch') { out.op = 'batch'; out.vaultId = seg[3] || ''; out.kind = 'object' }
        else if (op === 'append') { out.op = 'append ' + (seg[3] || ''); out.vaultId = seg[4] || ''; out.kind = 'append' }
        else if (op === 'list') { out.op = 'list'; out.vaultId = seg[3] || ''; out.kind = 'list' }
        else if (op === 'public-info') { out.op = 'info'; out.vaultId = seg[3] || ''; out.kind = 'info' }
        else if (op === 'presigned') { out.op = 'presigned'; out.vaultId = seg[4] || ''; out.fileId = seg.slice(5).join('/'); out.kind = kindOfFileId(out.fileId) }
        out.short = `${out.op} ${out.fileId ? out.fileId.replace(/^bare\//, '').replace(/(obj-cas-imm-|ref-pid-...-|idx-pid-...-)([0-9a-f]{4})[0-9a-f]+/, '$1$2…') : ''}`.trim()
    }
    return out
}

/** The operations of a batch: [{ op, fileId, kind, data (base64)? , status? }] from its request and its response. */
export function batchOps(requestText, responseText) {
    let ops = [], res = []
    try { ops = (JSON.parse(requestText || '{}').operations || []) } catch (e) { ops = [] }
    try { res = (JSON.parse(responseText || '{}').results || []) } catch (e) { res = [] }
    const byId = new Map(res.map(r => [r.file_id, r]))
    return ops.map(o => {
        const r = byId.get(o.file_id) || {}
        return { op: o.op, fileId: o.file_id, kind: kindOfFileId(o.file_id), data: o.data || r.data || null, status: r.status || '' }
    })
}

const B64 = s => { const bin = atob(String(s)); const u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); return u }
export const fromBase64 = B64

/**
 * Decrypted bytes, named from what is inside: { type, summary, value }. `decrypt(bytes)` is the vault's own decrypt
 * (AES-GCM with its read key), used again for a commit's message and a tree's names, which are encrypted inside.
 */
export async function classifyPlain(bytes, decrypt) {
    const text = (() => { try { return new TextDecoder('utf-8', { fatal: true }).decode(bytes) } catch (e) { return null } })()
    if (text == null) return { type: 'file', summary: `${bytes.length} bytes, not text`, value: null }
    let j = null
    try { j = JSON.parse(text) } catch (e) { j = null }
    const dec = async b64 => { try { return new TextDecoder().decode(await decrypt(B64(b64))) } catch (e) { return null } }
    if (j && j.schema && /^commit_/.test(j.schema)) {
        const message = j.message_enc ? await dec(j.message_enc) : (j.message || '')
        return { type: 'commit', summary: `“${message || ''}”, ${(j.parents || []).length} parent(s), at ${j.timestamp_ms ? new Date(j.timestamp_ms).toISOString().slice(0, 19).replace('T', ' ') : '?'}`,
                 value: { message, parents: j.parents || [], tree_id: j.tree_id, timestamp: j.timestamp_ms ? new Date(j.timestamp_ms).toISOString() : null, branch_id: j.branch_id || null } }
    }
    if (j && j.schema && /^tree_/.test(j.schema)) {
        const entries = []
        for (const e of (j.entries || []).slice(0, 200)) {
            const name = e.name_enc ? await dec(e.name_enc) : (e.name || '')
            const size = e.size_enc ? await dec(e.size_enc) : (e.size != null ? String(e.size) : '')
            entries.push({ name, kind: e.tree_id ? 'folder' : 'file', size: size == null ? '' : size, id: e.tree_id || e.blob_id || '' })
        }
        return { type: 'tree', summary: `${entries.length} entr${entries.length === 1 ? 'y' : 'ies'}: ${entries.slice(0, 6).map(e => e.name + (e.kind === 'folder' ? '/' : '')).join(', ')}${entries.length > 6 ? ', …' : ''}`, value: { entries } }
    }
    if (j && typeof j.commit_id === 'string' && Object.keys(j).length <= 3) return { type: 'ref', summary: `points at ${j.commit_id}`, value: j }
    if (j && (j.branches || j.head_ref_id || j.named)) return { type: 'branch-index', summary: 'the branches of this vault', value: j }
    return { type: 'file', summary: j ? `JSON, ${text.length} characters` : `text, ${text.length} characters`, value: text }
}

/** Mask what a call's body says about credentials before it is shown: tokens, keys, payloads. */
export function maskJson(text) {
    let j
    try { j = JSON.parse(text) } catch (e) { return null }
    const walk = x => {
        if (Array.isArray(x)) return x.map(walk)
        if (!x || typeof x !== 'object') return x
        const o = {}
        for (const [k, v] of Object.entries(x)) {
            if (/token|key|secret|anchor|hash/i.test(k)) o[k] = typeof v === 'string' ? `•••• (${v.length} characters)` : '••••'
            else if (k === 'payload' || k === 'data' || k === 'content') o[k] = typeof v === 'string' ? `ciphertext, ${v.length} characters (base64)` : v
            else o[k] = walk(v)
        }
        return o
    }
    return JSON.stringify(walk(j), null, 1)
}
