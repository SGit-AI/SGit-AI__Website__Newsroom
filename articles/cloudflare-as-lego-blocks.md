# Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines, sgit.ai

> I keep my domains at Cloudflare, and Cloudflare keeps shipping good things, but I do not want to learn Cloudflare. I would like to use it, the way a non-specialist would, with an agent doing the one-time setup. So this maps its developer platform, as of 18 October 2026, as the smallest blocks a person could put together, each with what it is for and what is free: static hosting with unlimited free requests, Workers at 100,000 requests a day, R2 storage with no egress fees, D1, KV and Durable Objects, 71 models running on Cloudflare's own GPUs with 10,000 free neurons a day and a promise not to train on what you send, inbound email, Zero Trust access for up to 50 users, and domains at cost. Then it tests the question I most wanted answered: can an sgit vault live on Cloudflare? A read-only vault needs no code at all. `sgit publish` writes a folder any static host can serve, and the real sgit client cloned it back identically. A read-write vault needs one Worker of 83 lines, one R2 bucket and one Durable Object per vault, all on the free plan. We wrote it and ran it in Cloudflare's own local runtime with the real client: create, push, clone, a stale push that merged, two pushes at once where one was told "nothing was overwritten", a read-only clone that could not write, and no plaintext anywhere on the server. The catch for non-specialists is setup: Cloudflare's API cannot be called from a web page, so the one-time setup is a Deploy to Cloudflare button, a temporary account, or an agent with the command line. That is fine, because it happens once.

*Source: <https://newsroom.sgit.ai/articles/cloudflare-as-lego-blocks.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines

# Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.2.0, 3 versions](versions/cloudflare-as-lego-blocks.md) · [newsroom v0.12.106](https://newsroom.sgit.ai/admin/versions.html) · cloudflareworkersr2durable-objectsworkers-aisgitvaultsminimal-codeself-hostingarticle

***Abstract:** I keep my domains at Cloudflare, and Cloudflare keeps shipping good things, but I do not want to learn Cloudflare. I would like to use it, the way a non-specialist would, with an agent doing the one-time setup. So this maps its developer platform, as of 18 October 2026, as the smallest blocks a person could put together, each with what it is for and what is free: static hosting with unlimited free requests, Workers at 100,000 requests a day, R2 storage with no egress fees, D1, KV and Durable Objects, 71 models running on Cloudflare's own GPUs with 10,000 free neurons a day and a promise not to train on what you send, inbound email, Zero Trust access for up to 50 users, and domains at cost. Then it tests the question I most wanted answered: can an sgit vault live on Cloudflare? A read-only vault needs no code at all. `sgit publish` writes a folder any static host can serve, and the real sgit client cloned it back identically. A read-write vault needs one Worker of 83 lines, one R2 bucket and one Durable Object per vault, all on the free plan. We wrote it and ran it in Cloudflare's own local runtime with the real client: create, push, clone, a stale push that merged, two pushes at once where one was told "nothing was overwritten", a read-only clone that could not write, and no plaintext anywhere on the server. The catch for non-specialists is setup: Cloudflare's API cannot be called from a web page, so the one-time setup is a Deploy to Cloudflare button, a temporary account, or an agent with the command line. That is fine, because it happens once.*

Cloudflare's developer platform as blocks, grouped by job. Put something on the web: static assets, free and unlimited; Workers, 100,000 requests a day; DNS and domains at cost. Keep data: R2 with 10 GB and zero egress, D1, KV, Durable Objects. Think with models it hosts: Workers AI with 10,000 neurons a day on Cloudflare's own GPUs, AI Gateway, Vectorize and AI Search. Run jobs: cron, queues and workflows, Browser Run, and Containers on the paid plan. Talk and guard: inbound email routing, email sending on the paid plan, Access free to 50 users, Turnstile and Tunnel.

Less code: a series in four parts

Code is a liability: remove what each use case does not call, apply it to the browser, and build on small blocks you did not have to write.

[1 · MeasuredThe minimum code belowOne real use case of sgit, under coverage: 428 of 1,500 files ran, and a tree of only those passed.](the-minimum-code-below.md)[2 · Less codeThe code you do not shipThe worst bugs sit in features nobody needed; models make removing them safe, and someone can be paid to keep it small.](the-code-you-do-not-ship.md)[3 · The browserA minimal viable browserA small kernel and components loaded when needed: a browser for one app, one agent, or a reader, sold as speed.](a-minimal-viable-browser.md)[you are here4 · Small blocksCloudflare as Lego blocksStorage, compute, models, email and identity as blocks, and an sgit vault server in 83 lines.](cloudflare-as-lego-blocks.md)

## In short

- **Use it without learning it.** The aim is a non-specialist, or an agent on their behalf, putting blocks together once.
- **Most blocks are free.** Hosting, Workers, R2, D1, KV, Durable Objects, Workers AI, inbound email, Access to 50 users.
- **Some models stay inside.** Workers AI runs its 71 models on Cloudflare's GPUs, and does not train on what you send.
- **A read-only vault needs no code.** `sgit publish` plus any static host; we cloned it back identically.
- **A read-write vault needs 83 lines.** One Worker, one R2 bucket, one Durable Object per vault, tested with the real client.
- **Setup is the hard part.** The API cannot be called from a web page, so it is a button, a temporary account, or an agent, once.

## What I would like

I am technical, and I could learn Cloudflare. I do not want to. I would like to use it the way I use a good tool: put a site on a domain I already own there, keep a vault, run a small API, call a model, receive mail, and not think about any of it again. And I would like the smallest pieces that do each job, the same argument as [the minimum code below](the-minimum-code-below.md): the least code and the least configuration that does exactly the thing.

The way to get there is not a course. It is a set of skills and prompts an agent can follow, and a few short code examples, so that setup happens once, correctly, and the result is something I own.

## The blocks

All limits are from Cloudflare's own pages, read on 18 October 2026; most were updated in the last two months, and they change.

**Put something on the web.**

- **Static assets.** Requests to static files are free and unlimited, on every plan. This is where a site, or a read-only vault, lives.
- **Workers.** Code at the edge: 100,000 requests a day free, 10 ms of CPU per request; $5 a month for 10 million requests and up to five minutes of CPU each.
- **DNS and Registrar.** DNS on every plan; domains sold "without markup fees", at the registry's price.

**Keep data.**

- **R2.** Object storage: 10 GB, a million writes and ten million reads a month free, and no egress fees. Buckets can be pinned to the EU or the US when created.
- **D1.** SQL: 5 GB, 5 million rows read and 100,000 written a day.
- **KV.** Key-value: 100,000 reads and 1,000 writes a day.
- **Durable Objects.** One small server per thing, that handles one request at a time, with its own SQLite storage. Free on the SQLite backend: 100,000 requests a day and 5 GB.

**Think, with models it hosts.**

- **Workers AI.** 10,000 neurons a day free, then $0.011 per 1,000. Its catalogue lists 71 models, all marked Cloudflare-hosted, running, as the [Workers AI overview](https://developers.cloudflare.com/workers-ai/) puts it, on "GPUs on Cloudflare's network": Llama 4 Scout, gpt-oss-120b, Qwen 3, Kimi K2.6, Gemma 4, Mistral Small, DeepSeek, GLM, Whisper and image models among them.
- **AI Gateway.** Caching, rate limits and logs in front of any model, free.
- **Vectorize and AI Search.** Embeddings and search over your own documents; AI Search starts billing on 1 November 2026, after a free allowance.

**Run jobs.**

- **Cron Triggers.** Five per account on the free plan.
- **Queues and Workflows.** 10,000 queue operations and 3,000 workflow steps a day.
- **Browser Run.** A headless browser on Cloudflare, renamed from Browser Rendering in April: ten minutes a day free.
- **Containers.** Full containers, on the paid plan only.

**Talk and guard.**

- **Email Routing.** Inbound mail to your domains, free and unlimited; Email Workers process it in code.
- **Email Sending.** In beta, on the paid plan: 3,000 emails a month, then $0.35 per 1,000.
- **Access.** Zero Trust login in front of anything, free for up to 50 users.
- **Turnstile and Tunnel.** Bot checks without puzzles, and a way to put a laptop's service on the web.

## Which models stay inside Cloudflare

This matters for anyone who wants an assistant over private material. Workers AI's privacy page says "Cloudflare does not use Customer Content processed by Workers AI to train AI models", and the models it lists run on Cloudflare's own GPUs. So a Worker that calls a `@cf/` model, on data in your own R2 bucket, keeps the whole loop inside your Cloudflare account.

One caution. Since 2026 the same call can also reach other providers' models, OpenAI's or Anthropic's, through AI Gateway. Those do not run on Cloudflare's GPUs. If staying inside is the point, the model name is the control: `@cf/` stays, anything else leaves.

It also answers a gap from [free models, your own key](free-models-your-own-key.md): Cloudflare had the most generous free allowance there, but a web page cannot call its API directly. A Worker in the reader's own account can, which is exactly the small server that article said would be needed.

## An sgit vault on Cloudflare

medium

The question I most wanted answered was whether a vault could live on Cloudflare, and how much code that takes. The answer comes from how sgit is built. The server never sees a key or a plaintext byte: it stores encrypted objects under ids, and checks one thing on writes, the vault's write key. That is [the value of constraints](the-value-of-constraints.md) in practice: because the server can read nothing, it has almost nothing to do.

**Read-only: no code.** sgit already knows how to read a vault from any static file host. `sgit publish` writes a folder: a plaintext cover and a manifest, with the encrypted objects beside them at the paths the client asks for. We published a test vault, 39 files and 220 KB, served the folder from a plain file server, and cloned it with the read key and `--transport static`. The clone was identical. On Cloudflare that folder goes into Workers static assets or a public R2 bucket, and costs nothing at this size. There is nothing to write to, so nothing can be written.

**Read-write: 83 lines.** The vault API sgit talks to has seven endpoints: info, read, list, batch, write, delete and destroy, plus an auth check this Worker always answers. We wrote them as one Worker. Reads go straight to R2. Every write for a vault goes through that vault's Durable Object, which Cloudflare runs one request at a time, so the compare-and-swap that stops two pushes overwriting each other is atomic. The first write to a vault binds its write key, by keeping a SHA-256 of it; later writes must match.

We ran it in Cloudflare's own runtime, workerd, locally through Miniflare 4, and pointed the real sgit client at it:

1. **Create, commit, push, clone.** The clone was identical to the original.
2. **A push over a stale copy.** sgit merged it; both edits were kept.
3. **Two pushes at the same moment.** One won. The other was told "the branch moved on the server while this push was in flight (a teammate pushed first); nothing was overwritten and nothing of yours is lost", pulled, and pushed. Both files landed.
4. **A read-only clone.** It refused to write: "This vault was cloned read-only."
5. **A wrong write key.** The Worker answered 403.
6. **The server's storage.** We searched every file the server stored for the plaintext; none of it was there.

This is the whole Worker:

```

// A read-write sgit vault server on Cloudflare: one Worker, one R2 bucket, one Durable Object class.
// The server only ever holds ciphertext. Reads go straight to R2; every write for a vault goes through
// that vault's Durable Object, which runs one request at a time, so compare-and-swap is atomic.
// The write key is bound to the vault on its first write (a SHA-256 of it is kept); later writes must match.

const J = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { 'content-type': 'application/json', ...CORS } });
const CORS = { 'access-control-allow-origin': '*', 'access-control-allow-headers': 'content-type,x-sgraph-access-token,x-api-key,x-sgraph-vault-write-key', 'access-control-allow-methods': 'GET,PUT,POST,DELETE,OPTIONS' };
const b64 = (u8) => { let s = ''; for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode(...u8.subarray(i, i + 0x8000)); return btoa(s); };
const unb64 = (s) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
const sha256 = async (s) => b64(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))));
const same = (a, b) => a.length === b.length && a.every((x, i) => x === b[i]);
const VID = /^[a-z0-9]{4,24}$/;

export default {
  async fetch(req, env) {
    if (req.method === 'OPTIONS') return new Response(null, { headers: CORS });
    if (env.ACCESS_TOKEN && req.headers.get('x-sgraph-access-token') !== env.ACCESS_TOKEN) return J({ error: 'access token required' }, 401);
    const p = new URL(req.url).pathname.split('/').map(decodeURIComponent);       // ['', 'api', 'vault', op, vid, fid?]
    if (p[2] === 'info') return J({ name: 'sgit-vault-on-cloudflare', version: '0.1.0' });
    if (p[2] === 'auth') return J({ ok: true });
    const [op, vid, fid] = [p[3], p[4], p.slice(5).join('/')];
    if (p[2] !== 'vault' || !VID.test(vid || '')) return J({ error: 'not found' }, 404);
    if (await env.VAULTS.head(`${vid}/.tombstone`)) return J({ error: `vault ${vid} has been permanently deleted` }, 403);
    if (op === 'read' && req.method === 'GET') {                                  // ciphertext, straight from R2
      const o = await env.VAULTS.get(`${vid}/${fid}`);
      return o ? new Response(o.body, { headers: CORS }) : J({ error: 'not found' }, 404);
    }
    if (op === 'list') {
      const prefix = new URL(req.url).searchParams.get('prefix') || '', files = [];
      let cursor;
      do { const r = await env.VAULTS.list({ prefix: `${vid}/${prefix}`, cursor });
           r.objects.forEach((o) => { if (!o.key.endsWith('/.writekey')) files.push(o.key.slice(vid.length + 1)); });
           cursor = r.truncated ? r.cursor : null; } while (cursor);
      return J({ files });
    }
    if (op === 'batch') {
      const body = await req.json();
      if (body.operations.every((o) => o.op === 'read')) return J(await readMany(env, vid, body.operations));
      return env.WRITER.get(env.WRITER.idFromName(vid)).fetch(new Request(req.url, { method: 'POST', headers: req.headers, body: JSON.stringify(body) }));
    }
    if (['write', 'delete', 'destroy'].includes(op)) return env.WRITER.get(env.WRITER.idFromName(vid)).fetch(req);
    return J({ error: 'not found' }, 404);
  },
};

async function readMany(env, vid, ops) {
  const results = await Promise.all(ops.map(async ({ file_id }) => {
    const o = await env.VAULTS.get(`${vid}/${file_id}`);
    return o ? { status: 'ok', file_id, data: b64(new Uint8Array(await o.arrayBuffer())) } : { status: 'not_found', file_id };
  }));
  return { status: 'ok', results };
}

export class VaultWriter {                     // one per vault; Cloudflare runs its requests one at a time
  constructor(state, env) { this.env = env; }
  async authorised(vid, key) {
    if (!key) return false;
    const h = await sha256(key), k = `${vid}/.writekey`, held = await this.env.VAULTS.get(k);
    if (!held) { await this.env.VAULTS.put(k, h); return true; }               // first write binds the key
    return (await held.text()) === h;
  }
  async fetch(req) {
    const p = new URL(req.url).pathname.split('/').map(decodeURIComponent), [op, vid, fid] = [p[3], p[4], p.slice(5).join('/')];
    if (!(await this.authorised(vid, req.headers.get('x-sgraph-vault-write-key')))) return J({ error: 'write key does not match this vault' }, 403);
    const B = this.env.VAULTS;
    if (op === 'write') { await B.put(`${vid}/${fid}`, await req.arrayBuffer()); return J({ status: 'ok' }); }
    if (op === 'delete') { await B.delete(`${vid}/${fid}`); return J({ status: 'ok' }); }
    if (op === 'destroy') { await B.put(`${vid}/.tombstone`, new Date().toISOString()); return J({ status: 'ok' }); }
    const { operations } = await req.json();
    for (const o of operations) if (o.op === 'write-if-match' && o.match) {      // compare everything first: a lost race writes nothing
      const cur = await B.get(`${vid}/${o.file_id}`);
      if (!cur || !same(new Uint8Array(await cur.arrayBuffer()), unb64(o.match))) return J({ status: 'conflict', message: `CAS mismatch on ${o.file_id}` });              // inside an HTTP 200, as sgit expects
    }
    const results = [];
    for (const o of operations) {
      if (o.op === 'read') { results.push(...(await readMany(this.env, vid, [o])).results); continue; }
      if (o.op === 'delete') await B.delete(`${vid}/${o.file_id}`);
      else await B.put(`${vid}/${o.file_id}`, unb64(o.data));
      results.push({ status: 'ok', file_id: o.file_id });
    }
    return J({ status: 'ok', results });
  }
}

```

And its configuration, for `wrangler deploy`:

```

# An sgit vault server on Cloudflare: deploy with `npx wrangler deploy` after `npx wrangler r2 bucket create sgit-vaults`.
name = "sgit-vault"
main = "worker.js"
compatibility_date = "2026-08-01"

[[r2_buckets]]
binding = "VAULTS"
bucket_name = "sgit-vaults"

[[durable_objects.bindings]]
name = "WRITER"
class_name = "VaultWriter"

[[migrations]]
tag = "v1"
new_sqlite_classes = ["VaultWriter"]

# Optional: require an access token on every request, as the hosted server does.
# npx wrangler secret put ACCESS_TOKEN

```

What it does not do yet, said plainly. Files over 4 MB use presigned uploads in sgit, which this Worker does not implement. There is one optional access token, not one per user. The free plan's 10 ms of CPU per request will be tight for very large batch reads. And it has not yet run on a real Cloudflare account: everything above was in the same runtime Cloudflare uses, on this machine. Python Workers became generally available on 21 September, so a Python version is possible too; for seven endpoints, JavaScript is the smaller code.

## How a non-specialist sets it up

Here is the catch. We tested Cloudflare's API from a browser's point of view: it does not answer the preflight a web page needs, so a page cannot call it directly, even with the user's own token. Setup cannot happen purely in a browser tab. That leaves four ways, and three of them suit someone who does not want to learn Cloudflare.

1. **A Deploy to Cloudflare button.** A link that clones a public repository into the user's own account, creates the R2 bucket, Durable Objects and other resources it declares, builds and deploys. For a vault host, that is one click and a sign-in. It works for Workers, not Pages.
2. **A temporary account.** Since June, `wrangler deploy --temporary` deploys with no sign-up; it stays live for an hour, with a link to claim it as a real account. Good for trying something before committing to it.
3. **An agent, once.** Claude Code, or any agent with a terminal, signs in with `wrangler login` and its OAuth flow, runs the commands, and hands back the URL. Cloudflare also runs an MCP server for its whole API, so an agent can do it without the command line. A new command-line tool, `cf`, entered open beta on 28 September and will replace Wrangler, which Cloudflare will keep maintaining for 18 months after the beta ends; a skill written today should say which it uses.
4. **The dashboard's own assistant.** Agent Lee, in beta, can change settings such as DNS records with your approval, but cannot deploy applications.

The pattern I would like is the first and third together: a published repository per package, with a button for people and a skill for agents, so that "host my vault on my Cloudflare account" is one sentence to an agent, done once, with a scoped token that can be revoked.

## Five packages

The blocks are more useful as packages, each the smallest set for one job.

| Package | Blocks | On the free plan? |
|---|---|---|
| A site on my domain | Static assets, DNS | Yes |
| My vault, hosted | Static assets, or a Worker with R2 and a Durable Object | Yes |
| An assistant over my documents | Workers AI, R2, AI Gateway, Access | Yes, within the allowances |
| An inbox that does things | Email Routing, an Email Worker | Yes |
| A form or a small API | A Worker, D1, Turnstile | Yes |

Each one is a repository with a button, a skill and a page saying exactly what it can reach, which is its behaviour policy.

## What I would watch

- **The command line is changing.** `cf` replaces Wrangler; Wrangler is maintained for 18 months after cf's beta ends.
- **AI Search starts billing on 1 November 2026.** After 5 million ingestion tokens and 1,000 queries of each kind a month.
- **Data residency is partial on the free plan.** R2 buckets can be pinned to the EU; the full Data Localization Suite is for Enterprise.
- **"Free" moves.** The limits above are October's.

## What this does not claim

- **The Worker has not run on a real account.** It ran in Cloudflare's runtime, locally, with the real sgit client.
- **It is a prototype.** No large files, one shared access token, no rate limits.
- **The hosted sgit server may check write keys differently.** Ours binds the key on first write; that is our choice.
- **Limits change.** Every number is as Cloudflare's pages gave it on 18 October 2026.

Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai) if you deploy it on a real account and something breaks.

## Where this comes from

A voice memo from me on 18 October 2026. Cloudflare's developer documentation, read on 18 October 2026 by a research agent: [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) and [pricing](https://developers.cloudflare.com/workers/platform/pricing/), [R2 pricing](https://developers.cloudflare.com/r2/pricing/), [Durable Objects pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/), [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [models](https://developers.cloudflare.com/workers-ai/models/) and [privacy](https://developers.cloudflare.com/workers-ai/platform/privacy/), [Email Service pricing](https://developers.cloudflare.com/email-service/platform/pricing/), [Browser Run limits](https://developers.cloudflare.com/browser-rendering/platform/limits/), [Deploy to Cloudflare buttons](https://developers.cloudflare.com/workers/platform/deploy-buttons/), [temporary accounts](https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/), [Cloudflare's MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/), [R2 data location](https://developers.cloudflare.com/r2/reference/data-location/), and the blog posts on [Python Workers](https://blog.cloudflare.com/python-workers-ga/) and [the cf command line](https://blog.cloudflare.com/cloudflare-cf-cli-launch/). The API's lack of CORS was tested from this machine. The vault tests: sgit 0.21.0 against the Worker above in workerd through Miniflare 4, and against a plain static file server, on 18 October 2026. Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Vaults & method[This article as a graph →](graphs.md#cloudflare-as-lego-blocks)

### Builds on

- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [Free models, your own key: what a reader can use from the browser in October 2026, and what they cannot](free-models-your-own-key.md) Which free model APIs a reader can call from a web page with their own key, October 2026: four pass both tests, NVIDIA fails both, and 2026 took a lot away.
- [The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think](the-value-of-constraints.md) sgit's encryption and open source matter less as features than as constraints: they remove the temptations that lead to server code, lock-in and bad decisions.

### Continued by

- [Ephemeral town planner services: a better name than serverless, now that serverless includes things that bill you by the hour](ephemeral-town-planner-services.md) Serverless meant scale to zero and pay per use; now it covers hourly bills. A better name: ephemeral town planner services, and a test for it.
- [Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open](three-linkedin-pages.md) Three companies, no LinkedIn pages: the decisions, every drafted field with its count, thirty first posts already written, and a new profile, in the open.
- [A minimal viable browser: why Firefox is the one that can build it, and what it would take](a-minimal-viable-browser.md) A small kernel and components loaded when needed: a browser for one app, one agent or a reader. Mozilla can build it, and should sell it as speed.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 180 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=180)

**Posting this article on LinkedIn?** The cover is [cloudflare-as-lego-blocks.jpg](banners/cloudflare-as-lego-blocks.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/cloudflare-as-lego-blocks.html)*
