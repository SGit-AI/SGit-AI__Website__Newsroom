import json,os
d=lambda x:json.dumps(x,ensure_ascii=False)
def write(g):
    assert set(g['topics'])<={'agents-and-policy','vaults-and-method','news-and-evidence','startups-and-strategy','graphs-and-knowledge','site-and-engineering'}, 'topic'
    assert all(e[2] in {'extends','depends-on','compared-with','contrasts','produces','example-of','answers','leads-to'} for e in g['edges']), 'edge relation'
    assert all(n[2] in {'concept','claim','method','artefact','example','question'} for n in g['nodes']), 'node kind'
    out='{\n'+',\n'.join([f' "slug": {d(g["slug"])}',f' "teaser": {d(g["teaser"])}',f' "topics": {d(g["topics"])}',f' "core_idea": {d(g["core_idea"])}',
     ' "nodes": [\n'+',\n'.join('  '+d({"id":n[0],"label":n[1],"kind":n[2],"summary":n[3]}) for n in g['nodes'])+'\n ]',
     ' "edges": [\n'+',\n'.join('  '+d({"from":e[0],"to":e[1],"rel":e[2]}) for e in g['edges'])+'\n ]',
     ' "links": {\n'+',\n'.join(f'  {d(k)}: {d(v)}' for k,v in g['links'].items())+'\n }',
     ' "quotes": [\n'+',\n'.join('  '+d({"text":q[0],"why":q[1]}) for q in g['quotes'])+'\n ]'])+'\n}\n'
    body=open(f'articles/{g["slug"]}.md').read()
    for q in g['quotes']: assert q[0] in body,(g['slug'],q[0])
    assert len(g['teaser'])<=160,(g['slug'],len(g['teaser']))
    for a in g['links']['articles']: assert os.path.exists(f'articles/{a}.md'),a
    open(f'articles/graphs/{g["slug"]}.json','w').write(out); print('wrote',g['slug'])
