import json,shutil,os,sys,glob
ROOT="/home/user/SGit-AI__Website__Newsroom"  # adjust
shutil.copy(f'{D}/{slug}.md',f'{A}/{slug}.md')
for f in glob.glob(f'{D}/pad-*.webp'): shutil.copy(f,f'{A}/images/')
json.dump({"slug":slug,"by":"newsroom.writer","sections":{
 "top":{"line":"What our agents cost at Web Summit: a swarm for pennies, newsroom days in API-equivalent hundreds.","para":"Part ten of the series."},
 "in-short":{"line":"216 open-weight calls for 6.8 cents; about $2 on a frontier model; 98% of newsroom tokens were memory.","para":"Context is the cost."},
 "ends":{"line":"Long frontier sessions and small signed swarm tasks, measured side by side.","para":"Pennies against dollars."},
 "swarm":{"line":"Signed packets with a mandate, grant and budget, run by a push; 216 calls for $0.068.","para":"Frontier prices are list prices."},
 "newsroom":{"line":"Accountant days of $375 to $924 API-equivalent; 98% cache reads.","para":"Not money spent."},
 "storm":{"line":"3.84 billion tokens, 98.7% cache reads, against $2.50 of model calls.","para":"Fresh sessions 46% cheaper."},
 "good":{"line":"Cheap models as second readers, checked by agreement, never the labeller.","para":"Room to answer matters."},
 "lessons":{"line":"Context is the cost; start again from notes; code first; a budget per task.","para":"Four lessons."},
 "limits":{"line":"API-equivalent is not spent; frontier figures are list prices; session tokens unmeasured.","para":"Three limits."},
 "sources":{"line":"The swarm repositories, the accountant's reports and the storm site's accounts.","para":"Re-read 18 November 2026."}}},open(f'{A}/summaries/{slug}.json','w'),indent=1,ensure_ascii=False)
os.chdir(f'{ROOT}/admin/content'); sys.path.insert(0,f'{ROOT}/admin/writer/tools')
from graph import write
write({"slug":slug,"teaser":"What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.",
 "topics":["agents-and-policy"],
 "core_idea":"Agent cost is dominated by sessions re-reading their history, while small signed tasks on open-weight models cost pennies, so put repeating work in code and cheap checked models and restart sessions from notes.",
 "nodes":[("swarm","The swarm","example","Signed packets, 6.8 cents."),("news","The newsroom","example","API-equivalent hundreds."),("cache","Cache reads","concept","98% of tokens."),("fresh","Starting fresh","method","Cheaper than remembering."),("second","Second readers","method","Cheap models checked."),("budget","Budgets per task","method","Packets carry limits.")],
 "edges":[("swarm","news","contrasts"),("cache","news","extends"),("fresh","cache","answers"),("second","swarm","extends"),("budget","swarm","extends")],
 "links":{"articles":["ten-days-at-web-summit","after-the-storm","spend-fewer-tokens"],"pages":[],"sites":["https://swarm.promptugal.news/","https://storm-charles.promptugal.news/accounts/"]},
 "quotes":[("Context is the cost.","The accountant."),("One run is one commit, one workflow run and one result.","The swarm.")]})
p=f'{ROOT}/admin/content/front/sections.json'; s=json.load(open(p))
for k,v in s.items():
  if isinstance(v,dict) and 'a-guide-born-in-a-storm' in v: v[slug]=v['a-guide-born-in-a-storm']
open(p,'w').write(json.dumps(s,indent=1,ensure_ascii=False)+'\n')
h=f'{A}/ten-days-at-web-summit.md'; t=open(h).read()
old='10. **Pennies against dollars:**'; new='10. [Pennies against dollars](/articles/pennies-against-dollars.html):'
assert old in t,'hub'; open(h,'w').write(t.replace(old,new))
sm=f'{A}/summaries/ten-days-at-web-summit.json'; d=json.load(open(sm)); d['sections']['series'].pop('hash',None); json.dump(d,open(sm,'w'),indent=1,ensure_ascii=False)
sc=f'{ROOT}/admin/notes/2026-11-14__ten-days-series/schedule.md'; t=open(sc).read()
t=t.replace('| 10 | next |','| 10 | live (18 Nov) |').replace('| 11 | queued |','| 11 | next |'); open(sc,'w').write(t)
print('installed')
