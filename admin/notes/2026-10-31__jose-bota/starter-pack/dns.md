# DNS records in Route 53 (example: domain josebota.io, GitHub user josebota)

| Name | Type | Value | For |
|---|---|---|---|
| josebota.io | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 | the main site on GitHub Pages |
| www.josebota.io | CNAME | josebota.github.io | the main site |
| newsroom.josebota.io | CNAME | josebota.github.io | the newsroom repository |
| agent-reach.demos.josebota.io | CNAME | josebota.github.io | one app, one repository |

Each repository sets its own custom domain in Settings, Pages. Verify the domain for the account first. The four A addresses are GitHub Pages' published apex addresses; check GitHub's documentation before using them.
