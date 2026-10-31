# Brief for José's agent: from a Lovable MVP to a published app, a domain and a newsroom

Read this brief and the article it comes from (newsroom.sgit.ai/articles/from-lovable-to-your-own-newsroom.html). Work in small steps; after each, show José what changed and a link he can open. Never put secrets, client data or keys in a public repository.

## Step 1: the Lovable app into GitHub
1. In Lovable, connect GitHub (project settings) so the project syncs to a repository under José's account.
2. Check the stack: a Vite project builds to `dist/` and can be served by GitHub Pages as static files. A TanStack Start project (server rendering) needs a static build first, or a host that runs Node; say which it is before going on.
3. Add `.github/workflows/deploy-pages.yml` from this pack. In Settings, Pages, choose GitHub Actions as the source.
4. Push, wait for the workflow, open the Pages address, and send José the link.

## Step 2: a domain with José's name
1. Buy the domain in AWS Route 53 (Registered domains). Route 53 sells .com, .io, .site, .ai and .dev among others; it does not sell .pt, which can be bought from a .pt registrar and still use Route 53 for DNS.
2. In GitHub, verify the domain for José's account (Settings, Pages, Verified domains), so nobody else can use it.
3. One subdomain per app, under a demos subdomain: `<app>.demos.<domain>`. For each: a CNAME record in Route 53 to `<github-user>.github.io`, and the same name in the repository's Pages custom domain setting (it writes a `CNAME` file). Turn on Enforce HTTPS once the certificate is issued.
4. Keep a list of apps in `apps.json` (see `apps.example.json`) in the main site's repository.

## Step 3: newsroom.<domain>
1. Follow "Your own newsroom" (newsroom.sgit.ai/articles/your-own-newsroom.html): one public repository, GitHub Pages published by Actions after a validation step, and a house-rules file.
2. Start from `newsroom-CLAUDE.md` in this pack as the house rules, and change the voice to José's.
3. Point `newsroom.<domain>` at it with a CNAME, as in step 2.
4. First articles: one per app, what it does, who it is for, what it does not do yet, with the link.

## Done means
José sends Dinis two or three links: apps live on `<app>.demos.<domain>`, and the articles about them on `newsroom.<domain>`.

## Later: private versions for clients
The same workflow with a private repository per client: their customisations, their domain or ours, their data never in the public demo. GitHub Pages from a private repository needs a paid GitHub plan; or the client hosts it.
