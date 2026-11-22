import json,hashlib,urllib.request,sys
from concurrent.futures import ThreadPoolExecutor
def get(u): return urllib.request.urlopen(u,timeout=30).read()
res={}
for base in sys.argv[1:]:
    m=json.loads(get(base+"manifest.json"))
    files=m.get("entries") or m.get("files")
    items=list(files.items()) if isinstance(files,dict) else [(f["path"],f) for f in files]
    def chk(it):
        p,i=it
        try: h=hashlib.sha256(get(base+p)).hexdigest()
        except Exception as e: return p,"FETCH "+str(e)[:40],None
        return p,("ok" if h==i["sha256"] else "MISMATCH"),h
    out=list(ThreadPoolExecutor(8).map(chk,items))
    bad=[o for o in out if o[1]!="ok"]
    tot=sum(i.get("bytes",0) for _,i in items)
    print(base,"files",len(items),"bytes",tot,"ok",len(out)-len(bad),"bad",bad[:5])
    res[base]={p:h for p,_,h in out}
json.dump(res,open("hashes_all.json","w"),indent=1)
