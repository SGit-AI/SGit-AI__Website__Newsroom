import subprocess,collections,sys,re
def g(*a): return subprocess.run(["git",*a],capture_output=True,text=True).stdout
for d in ["2026-10-23T12:00:00Z","2026-10-30T23:59:00Z","2026-11-06T23:59:00Z","2026-11-13T23:59:00Z","2026-11-20T23:59:00Z"]:
    sha=g("rev-list","-1","--first-parent",f"--before={d}","HEAD").strip()
    files=[f for f in g("ls-tree","--name-only",sha,"software/").split() if re.search(r"software_list(_[^/]*)?\.md$",f)]
    split=[f for f in files if "_" in f.split("software_list")[1]]
    use=split or files
    c=collections.Counter(); n=0
    for f in use:
        for line in g("show",f"{sha}:{f}").splitlines():
            if not line.startswith("|") or line.startswith("|:") or line.startswith("| ---") : continue
            cols=[x.strip() for x in line.strip().strip("|").split("|")]
            if cols[0] in ("Supplier","---") or len(cols)<6: continue
            # find first status-like column
            st=next((x for x in cols[2:6] if x in ("Fix","Vulnerable","Investigation","Not vuln","Runtime-dependent","Workaround","Not affected","Unknown")),"?")
            c[st]+=1; n+=1
    print(d[:10],sha[:10],len(use),"files rows",n,dict(c))
