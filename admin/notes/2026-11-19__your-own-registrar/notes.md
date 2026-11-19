# Notes: your-own-registrar (19 November 2026)

Dinis, in writer-10's session: research registrars (pricing, gaps, UI, API, agent-friendly) to recommend one to AgentiCCells customers moving to their own registrar; AWS felt heavy, and he thought it does not do .ai; maybe a European registrar.

Research done on 19 November 2026 from each registrar's own pages, read-only (no accounts, no forms). Pages that refused or did not load: Namecheap (403), GoDaddy (403), Hover (unreadable), Cloudflare's price page (403), Infomaniak's price page (loading). Their figures in the article are marked unconfirmed or left out.

| Registrar | Seat | .com | .eu | .pt | .co.uk | .ai a year | Free privacy | API / agent tooling | Catch |
|---|---|---|---|---|---|---|---|---|---|
| Gandi | FR | €11.65→31.98 | €3.99→30 | €17.38→30-40 | €5.99→23.98 | €97.44→160 | Yes | scoped expiring PATs | renewals |
| OVHcloud | FR | €8.49→14.29 | €7.49→8.59 | €16.99→13.39 | €7.49→7.98 | €70.99→119.99 | unconfirmed | official MCP, OAuth2, cannot pay | .com/.ai renewal |
| INWX | DE | €15.50 | €5 promo (€10) | €35 | €10 | €100 per 2 yrs | No (paid) | RPC API, OT&E, Terraform | paid privacy; renewals not shown |
| Hostinger | LT | $0.01 (3 yrs)→19.99 | $4.99→7.99 | $18.99→18.99 | $3.99→11.99 | $50→109.99 | Yes | API and official MCP (OAuth) | promos |
| IONOS | DE | £1-9→15 | £6→12 | not on UK list | £1-4→10 | £80→120 | unconfirmed | DNS API | £90 restore |
| Hetzner | DE | €14.50 | €12 | no | no | no (Robot) | unconfirmed | unconfirmed | narrow TLDs |
| Infomaniak | CH | unconfirmed | unconfirmed | unconfirmed | unconfirmed | unconfirmed | No (CHF 2.40-3) | unconfirmed | prices did not load |
| Porkbun | US | $11.81 flat | $5.88 flat | no | $5.66 flat | $82.70 flat | Yes | keys by domain/IP/permission, spend cap, MCP incl. no-purchases | no .pt |
| Namecheap | US | unconfirmed | | | | unconfirmed | | API needs 20+ domains or $50 balance/spend; Terraform; MCP | API gate |
| Cloudflare | US | at cost | no | no | yes | at cost | Yes | Registrar API beta since 15 Apr 2026; scoped tokens; MCP | no .eu/.pt; its nameservers |
| Route 53 | US | $16 | $8 | no | $9 | $137 | no on .ai and .eu | IAM, CLI | price; DNS $0.50/zone/month |
| Squarespace | US | $10 headline | | | | | Yes | reseller API only | no customer API |
| Dynadot | US | $11.62 | €3.94→5.66 | $11.28 | $6.15 | $85.60 | unconfirmed | API (prepaid balance), MCP | restore $460 on .ai |
| Hover | CA | unconfirmed | | | | | Yes | none found | price |
| name.com | US | $13.99/$21.99 | | | | $99.99 | unconfirmed | CORE API | renewal |
| GoDaddy | US | unconfirmed | | | | | | scoped PATs | renewals |

Primary sources (read 19 Nov 2026): gandi.net/en/domain/tld/{com,eu,pt,co.uk,ai}; docs.gandi.net whois_privacy; api.gandi.net/docs/authentication; ovhcloud.com/en-ie/domains/tld/{com,eu,pt,co.uk,ai}; docs.ovhcloud.com mcp-domain-getting-started (updated 18 Nov 2026); inwx.de/en/{tld}-domain; inwx.com/en/offer/api; kb.inwx.com whois privacy; hostinger.com/tld and /support/11079316; ionos.co.uk/domains/domain-name-prices; hetzner.com/registrationrobot; infomaniak.com/en/domains/domain-privacy; porkbun.com/products/domains, /tld/ai, /api/json/v3/documentation; cloudflare.com/tld-policies, /products/registrar; developers.cloudflare.com/registrar/faq, /api/resources/registrar; docs.aws.amazon.com Route53 DeveloperGuide ai.html, eu.html, co.uk.html, registrar-tld-list.html; AWS Route 53 domain pricing PDF; aws.amazon.com/route53/pricing; dynadot.com/domain/prices and /domain/api-commands; name.com/domains/ai; domains.squarespace.com; developer.godaddy.com/en/docs/api-users. Locations are general knowledge.
