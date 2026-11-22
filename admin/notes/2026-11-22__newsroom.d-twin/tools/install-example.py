import json,shutil,os,sys
ROOT="/home/user/SGit-AI__Website__Newsroom"; A=f"{ROOT}/admin/content/articles"; D=os.path.dirname(os.path.abspath(__file__)); slug="the-primitives-of-trust"
shutil.copy(f'{D}/{slug}.md',f'{A}/{slug}.md'); shutil.copy(f'{D}/prim-map.webp',f'{A}/images/')
L=lambda l,p:{"line":l,"para":p}
json.dump({"slug":slug,"by":"newsroom.writer","sections":{
 "top":L("Why a web of trust works now: commodity primitives, an engine the user never sees, links that count both ways.","The primitives."),
 "in-short":L("Earlier failures, commodity primitives, a transparent engine, two-way links, provenance, hard to game.","Six points."),
 "why-now":L("Earlier key stores failed for want of workflows; the February briefs had the ideas; the pieces are now commodity.","Why now."),
 "primitives":L("A site per person, mature PKI, keys anywhere, git, QR codes, and an agent engine, even a small model.","The pieces."),
 "direction":L("Anyone can link to anyone; only returned links count; a page holds only its owner's links.","Direction."),
 "provenance":L("Kinds plus date, place and event make links confirmable; agents nudge; checks mostly in code.","Provenance."),
 "fractal":L("Each owner defines their schema; only nodes, edges and signatures stay constant.","Fractal schemas."),
 "security":L("Easy to game one node, hard to game them all at once.","Security."),
 "identity":L("Open identity at scale, author-signed content, and every identity provider as evidence.","Identity."),
 "standard":L("Next: a small standard for keys, links, claims, confirmation and walking the graph.","A standard."),
 "limits":L("Kinds and provenance proposed; small models a bet; DNS later.","Three limits."),
 "sources":L("My thinking, my February and March briefs, and pki.sgit.ai, on 21 November 2026.","21 November 2026.")}},open(f'{A}/summaries/{slug}.json','w'),indent=1,ensure_ascii=False)
os.chdir(f'{ROOT}/admin/content'); sys.path.insert(0,f'{ROOT}/admin/writer/tools')
from graph import write
write({"slug":slug,"teaser":"Why a web of trust between people works now: commodity primitives, an agent engine users never see, and links that count only both ways.",
 "topics":["agents-and-policy"],
 "core_idea":"A web of trust became practical once its primitives became commodity, a site per person, mature PKI, keys in browsers and agents, git and an agent engine that signs and follows keys transparently; links count only when returned, carry confirmable provenance, and owner-defined schemas make the whole hard to game.",
 "nodes":[("primitives","Commodity primitives","concept","Sites, PKI, keys, git."),("engine","The agent engine","method","Signs, verifies, follows."),("direction","Two-way links","claim","Only returned links count."),("provenance","Kinds and provenance","method","Confirmable."),("fractal","Owner-defined schemas","concept","Nodes, edges, signatures constant."),("identity","Open identity","claim","With every provider.")],
 "edges":[("primitives","engine","produces"),("engine","direction","depends-on"),("provenance","direction","extends"),("fractal","provenance","extends"),("direction","identity","produces")],
 "links":{"articles":["the-site-factory-works","agents-have-an-identity-now","a-secret-is-a-qr-code","a-web-of-trust-for-careers","an-anonymous-profile-vouched-for","person-graph","a-directory-of-people-and-keys"],"pages":[],"sites":[]},
 "quotes":[("we cannot push this overhead onto users","Dinis."),("It is easy to game one node, or one component.","Dinis.")]})
p=f'{ROOT}/admin/content/front/sections.json'; s=json.load(open(p)); s['articles'][slug]=s['articles']['the-sovereign-website']
open(p,'w').write(json.dumps(s,indent=1,ensure_ascii=False)+'\n')
n=f'{ROOT}/admin/notes/2026-11-21__{slug}'; os.makedirs(n,exist_ok=True)
open(f'{n}/notes.md','w').write("# Notes: the-primitives-of-trust (21 November 2026)\n\nDinis's spoken brief: an article in its own right on linking trust between individuals with public keys; the primitives coming together, a Wardley map; earlier failed attempts at a PKI store for want of workflows; website-based (later DNS) two-way trust; trust through connectivity; GitHub Pages; an engine that signs, verifies and follows keys transparently; keys in browsers and agents, ephemeral or long-lived; an agent is a model with a loop and tools, likely works with Haiku and open-weight models; anyone can link to anyone, only returned links count; a person's page holds only outgoing links, so bad actors cannot corrupt it; connection requests; kinds plus provenance (date, event) and confirmation nudges; deterministic checks and injection guards; owner-defined (fractal) schemas with only nodes, edges and signatures constant; easy to game one node, hard across the board; author-signed content and identity that works with every provider. Earlier writing found in SGraph-AI__App__Send (dev): briefs v0.4.27 (21 Feb 2026, natural revocation through graph maintenance), v0.6.14 trust web and content trust (23 Feb), v0.12.2 identity infrastructure (7 Mar), trust spectrum article (9 Mar). docs.diniscruz.ai was checked; the gamification-for-news piece he recalled was not located there, so the February content-trust brief is cited instead.\n")
print('installed')
