from pathlib import Path
from collections import Counter, defaultdict
import base64, hashlib, html, io, json, re, shutil, subprocess, sys, tempfile, zipfile


src = Path(__file__).resolve().parent / 'input'
root = Path(sys.argv[1]).resolve()
dest = Path(sys.argv[2]).resolve()
root.mkdir(parents=True, exist_ok=True)
dest.mkdir(parents=True, exist_ok=True)
CP = 'DENNING-2026-11-03'
ZIP = 'Denning_Slipcase.zip'
paper = 'Who_Can_Reopen_the_Decision__2026-11-03'
ret = CP + ' · 000__RETURN_PATH.txt'
def put(name, value):
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(value if isinstance(value, bytes) else value.encode())
def read(name):
    return (src / name).read_text()
def dump(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)
def jsonl(name, records):
    put(name, ''.join(dump(r)+'\n' for r in records))
def sha(data):
    return hashlib.sha256(data).hexdigest()
def slug(s):
    return re.sub('[^A-Za-z0-9]+','-',s).strip('-')
def field(b, k):
    m = re.search(r'^\s*'+k+r'\s*=\s*\{(.*)\},?$', b, re.M)
    return m[1].strip('{}').replace('\\&','&') if m else ''
def safejson(o):
    return dump(o).replace('<', '\\u003c')
esc = html.escape
cards, nodes, rel, appearances, bib = [], {}, [], [], {}
def node(key, kind, title, **kw):
    nodes.setdefault(key, dict(key=key,type=kind,title=title,**kw))
    return key
def edge(kind, source, target, literal, field, ordinal, state='EXACT', card=None):
    rel.append(dict(type=kind, **{'from':source,'to':target}, card=card or source, literal=literal, field=field, ordinal=ordinal, state=state))
names = ['Positive-Sum-Rivalry','The-Next-Windfall','The-Investment-Hurdle','Signature-on-the-Deck','Enablement-and-Exit','The-Paid-Alibi','Who-Can-Reverse-It','The-Flak-Catcher','The-Absent-Sequel','Dissent-in-the-Denominator','The-Change-Order','Patient-Shareholder-Value','Pricing-the-Gain','The-Limited-Assortment','Who-Enters-the-Loop','The-Advisor-Crossing']
sigs = 'Porter-2008 Acemoglu-et-al-2022 Koller-et-al-2026 Denning-2026 Denning-2026 Graeber-2018 Davies Graeber Denning-2026 Graeber Davies Amazon-1997 McKinsey-2000 Costco-2025 Denning-2010 Denning'.split()
fields_rx = re.compile(r'^([A-Z][A-Z /-]+):\n', re.M)
platforms, ids, titles = {}, defaultdict(list), defaultdict(list)
for i,payload in enumerate(read('cards').rstrip('\n').split('\n<<<CARD>>>\n'),1):
    fields = {}
    marks = list(fields_rx.finditer(payload))
    for j,m in enumerate(marks):
        fields[m[1]] = payload[m.end():marks[j+1].start() if j+1<len(marks) else len(payload)].rstrip('\n')
    ident, title, digest = fields['ID'],fields['TITLE'],sha(payload.encode())
    key = 'z-'+digest
    origin = 'forage' if i<=5 else 'opposition' if i<=11 else 'recursion'
    filename = f'{i:03}__{names[i-1]}__{sigs[i-1]}__{ident}__from-{origin}.txt'
    appearances.append(dict(key=f'appearance-{i:02}',card=key,position=i,origin=origin,provenance='Visible conversation; manual transcription',classification='ADMITTED' if key not in nodes else 'EXACT_DUPLICATE'))
    if key in nodes:
        continue
    node(key,'ZETTEL',title,original_id=ident,filename=filename)
    cards.append(dict(key=key,id=ident,title=title,name=names[i-1],order=i,filename=filename,sha=digest,payload=payload,object=fields['RESEARCH OBJECT'],fields=fields))
    ids[ident].append(key)
    titles[title].append(key)
    put(filename,payload)
    put('_MD/'+filename[:-4]+'.md',payload)
    for name in re.findall(r'\[\[(.+?)\]\]',fields.get('PLATFORM','')):
        platforms[name] = node('p-'+sha(name.encode())[:16],'PLATFORM',name)
    raw=fields['BIBTEX']
    cite=re.match(r'@\w+\{([^,]+)',raw)[1]
    bkey=cite if cite not in bib or bib[cite]['raw']==raw else cite+'#'+sha(raw.encode())[:12]
    author=field(raw,'author')
    date=field(raw,'year')
    work=field(raw,'title')
    doi=field(raw,'doi')
    b=bib.setdefault(bkey,dict(key=cite,raw=raw,title=work,citation=f'{author} · {work}'+(f' · {date}' if date else ''),author=author,year=date,doi=doi,url=field(raw,'url') or ('https://doi.org/'+doi if doi else ''),cards=[],explicit=[]))
    b['cards'].append(key)
    b['explicit'].append(key)
    edge('CITES',key,'s-'+bkey,cite,'BIBTEX',1)
aliases={}
ghosts=defaultdict(list)
def resolve(name):
    for candidates in (ids.get(name), [aliases[name]] if name in aliases else None,titles.get(name),[c['key'] for c in cards if c['name']==name]):
        if candidates:
            if len(candidates)==1:return candidates[0],'EXACT'
            return node('g-'+sha(name.encode())[:16],'GHOST',name,candidates=candidates),'AMBIGUOUS'
    if name in platforms:return platforms[name],'EXACT'
    if re.match(r'https?://',name):
        return node('external-'+sha(name.encode())[:16],'RESOURCE',name,url=name),'EXTERNAL'
    return node('g-'+sha(name.encode())[:16],'GHOST',name),'BROKEN_ID' if re.fullmatch(r'ZF-MGMT-\d+',name) else 'UNRESOLVED'
for c in cards:
    for f,s in c['fields'].items():
        for ordinal,m in enumerate(re.finditer(r'\[\[(.+?)\]\]',s),1):
            target,state=resolve(m[1])
            edge({'PLATFORM':'MEMBER_OF','LINKS':'LINKS_TO'}.get(f,'WIKILINKS_TO'),c['key'],target,m[0],f,ordinal,state)
            if nodes[target]['type']=='GHOST':ghosts[target].append(rel[-1])
native=[r for r in rel if r['type'] in ('MEMBER_OF','LINKS_TO','WIKILINKS_TO')]
for r in native:
    edge('BACKLINK',r['to'],r['from'],r['literal'],r['field'],r['ordinal'],r['state'],r['card'])
for key, edges in ghosts.items():
    nodes[key].update(inbound=edges,count=len(edges),first=edges[0],source_cards=list(dict.fromkeys(e['card'] for e in edges)),
                      platforms=list(dict.fromkeys(next(c for c in cards if c['key']==e['card'])['fields']['PLATFORM'] for e in edges)),
                      surrounding_sources=list(dict.fromkeys(next(c for c in cards if c['key']==e['card'])['fields']['SOURCE'] for e in edges)))
for i,title in enumerate(['PRIME ZETTEL FORAGE — INQUIRY + OPPOSITION','PRIME ZETTEL FORAGE — RECURSIVE INQUIRY','SLIPCASE — PORTABLE RESEARCH FIELD'],1):
    local={1:'_PROMPTS/forage-3.0.poml',2:'_PROMPTS/recursive-3.1.poml',3:'_PROMPTS/assembly.poml'}[i]
    node(f'prompt-{i}','PROMPT',title,local=local if (src/Path(local).name).exists() else None)
for a in appearances:
    ak=node(a['key'],'RESOURCE','Conversation card appearance '+str(a['position']),state='PASTED')
    edge('APPEARED_IN',a['card'],ak,a['origin'],'conversation',a['position'])
    edge('GENERATED_BY',a['card'],'prompt-1' if a['position']<12 else 'prompt-2',a['origin'],'conversation',a['position'], 'CONTEXTUAL')
resources=[]
source_map={
1:['porter2008five','denning2026businessschools'],2:['acemoglu2022eclipse'],3:['koller2026strategyauthortalks','denning2026businessschools'],
4:['denning2026businessschools'],5:['denning2026businessschools'],6:['graeber2018bullshit','denning2026businessschools'],7:['daviesTaming'],
8:['graeberRiseBullshitJobs'],9:['denning2026businessschools','daviesTaming'],10:['graeberPointlessJob','daviesTaming','denning2026businessschools'],
11:['daviesTaming'],12:['amazon1997shareholderletter','denning2026businessschools'],13:['mckinsey2000delivering','denning2026businessschools'],
14:['costco2025form10k','denning2026businessschools'],15:['denning2010radical','daviesTaming'],16:['denningAbout','denning2026businessschools']}
for c in cards:
    for j,k in enumerate(source_map[c['order']],1):
        b=bib[k]
        if c['key'] not in b['cards']:b['cards'].append(c['key'])
        edge('USES_SOURCE',c['key'],'s-'+k,c['fields']['SOURCE'].splitlines()[j-1],'SOURCE',j,'CURATED')
for k,b in bib.items():
    b['status']='BIB-CONFLICT' if '#' in k else 'SHARED' if len(b['cards'])>1 else 'UNIQUE'
    b['cards'].sort(key=lambda x:nodes[x]['original_id'])
    sk=node('s-'+k,'SOURCE',b['title'],citekey=b['key'])
    rk=node('r-'+k,'RESOURCE',b['title'],url=b['url'],state='LINK_ONLY')
    edge('REPRESENTED_BY',sk,rk,b['url'],'URL / DOI',1,card=None)
    resources.append(dict(key=rk,title=b['title'],state='LINK_ONLY',url=b['url'],doi=b['doi'],author=b['author'],year=b['year'],cards=b['cards'],local=None,provided_by='Visible card bibliography'))
for line in read('receipts.tsv').splitlines():
    key,title,url,orders=line.split('\t')
    rk=node('receipt-'+key,'RESOURCE',title,url=url,state='LINK_ONLY')
    used=[c['key'] for c in cards if f"{c['order']:03}" in orders.split()]
    resources.append(dict(key=rk,title=title,state='LINK_ONLY',url=url,cards=used,local=None,provided_by='Conversation source or retrieval receipt'))
    for j,k in enumerate(used,1):edge('USES_SOURCE',k,rk,url,'supplemental receipt',j,'CURATED')
for path in sorted(src.glob('resource-*')):
    local='_RESOURCES/'+path.name.removeprefix('resource-')
    put(local,path.read_bytes())
    rk=node('local-'+slug(path.name),'RESOURCE',path.name.removeprefix('resource-'),state='PASTED',local=local)
    b=bib['denning2026businessschools']
    edge('REPRESENTED_BY','s-denning2026businessschools',rk,local,'local body',2,'PARTIAL_PASTE')
    resources.append(dict(key=rk,title=nodes[rk]['title'],state='PASTED',url=b['url'],cards=b['cards'],local=local,provided_by='User paste; manually transcribed article body'))
for path in src.glob('*.poml'):put('_PROMPTS/'+path.name,path.read_bytes())
put('000__PROMPTS.txt',read('prompts.txt'))
put('000__MAKING_HISTORY.txt',read('history'))
put(paper.split('__')[0]+'__MAKING_HISTORY.txt',read('history'))
put(paper.split('__')[0]+'__SOURCE_MAP.txt',read('source-map.txt'))
put(paper.split('__')[0]+'__ASSEMBLY_APPENDIX.txt',ret+'\n\nAssembly instrument: _PROMPTS/assembly.poml\nStandalone index → Files → _PROMPTS/assembly.poml.\n')
put('000__RETURN_PATH.txt',f'{ret}\nSchema 15.55-AM · {ZIP}\nResearcher: Watson Hartsoe · 2026-11-03\nRejoin phrase: Who can reopen the decision?\nResume via 000__OPEN_EDGES.txt and _SLIPCASE/MANIFEST.json.\nRestore or recompile via 000__REBUILD.txt.\n')
put('000__START_HERE.txt',f'{ret}\n\nOpen index.html directly. Start with Deck or a MOC.\nRead the working paper from the desk or the root PDF.\nCARDS.html prints an evidence-and-question face for each exact root card.\nThe evidence boundary and omissions are in 000__MAKING_HISTORY.txt.\n')
put('000__REBUILD.txt',f'''{ret}
Restore the full published tree from index.html via Recover ZIP. Add the original index.html to the extracted folder.
For verified extraction use: python _SLIPCASE/rebuild.py /path/to/index.html /path/to/empty-directory
For independent recompilation from inputs: python _SLIPCASE/build.py /path/to/new-empty-directory /path/to/output
Recompilation requires Python 3.9+, XeLaTeX, Poppler (pdfinfo), BibTeX, and the fonts/packages declared by the manuscript.
Inputs accompany build.py. Do not edit existing card payloads in place. Add an appearance and a new payload for amendments.
For merge, deduplicate exact payload hashes only. Retain appearances, original IDs, variant citekeys, and unresolved addresses. Recompute edges.
''')
put('ZETTELS.txt','\n\n'+'\n\n'.join('=== '+c['filename']+' ===\n\n'+c['payload'] for c in cards)+'\n')
put('ZETTELS.json',dump(cards))
jsonl('ZETTELS.jsonl',cards)
put('000__INDEX.txt',ret+'\n\n'+'\n'.join(c['filename']+'\n  '+c['title'] for c in cards)+'\n')
put('000__OPEN_EDGES.txt',ret+'\n\n'+'\n\n'.join(c['id']+' · '+c['title']+'\n'+ '\n'.join(k+'\n'+c['fields'][k] for k in ['TENSION','MISSING','BOUNDARY','CITATION TRAIL','TEST']) for c in cards)+'\n')
put('000__RESOURCES.txt',ret+'\n\n'+'\n\n'.join(r['state']+' · '+r['title']+'\n'+' · '.join(x for x in (r['url'],r['local']) if x)+'\nCards: '+', '.join(nodes[k]['original_id'] for k in r['cards']) for r in resources)+'\n')
put('000__BIBLIOGRAPHY.txt',ret+'\n\n'+'\n\n'.join(b['status']+' · '+b['citation']+'\n'+b['url']+'\nCards: '+', '.join(nodes[k]['original_id'] for k in b['cards'])+'\n'+b['raw'] for b in bib.values())+'\n\nNEEDS-CITATION: Original McKinsey staff papers, Bain and BCG primary articles, and original Marquis interview receipts remain follow-up work.\n')
bibname=CP+'__references.bib'
put(bibname,f'% {CP} | {ZIP} | schema 15.55-AM | 000__RETURN_PATH.txt\n\n'+'\n\n'.join(b['raw'] for b in bib.values())+'\n')
mocs=[]
for title,key in platforms.items():
    group=[r['from'] for r in native if r['to']==key and r['type']=='MEMBER_OF']
    mocs.append(dict(title=title,note='Declared membership. Outgoing links and backlinks extend this view.',cards=group))
mocs.extend(dict(title=t,note=n,cards=[cards[i-1]['key'] for i in indices]) for t,n,indices in [
 ('From customer benefit to decision authority','Read across financial ends, operational learning, and standing.',[1,3,12,13,14,15,7]),
 ('After the recommendation','Follow the same decision through authorization, complaint, and revision.',[4,6,7,8,9,10,11,16])])
for i,m in enumerate(mocs,1):
    folder='_MOCS' if i<=len(platforms) else '_ARRANGEMENTS'
    put(f"{folder}/{i:02}__{slug(m['title'])}.md",ret+'\n\n# '+m['title']+'\n\n'+m['note']+'\n\n'+'\n'.join('- [['+nodes[k]['original_id']+']] '+nodes[k]['title'] for k in m['cards'])+'\n')
g={n['key']:set() for n in nodes.values() if n['type'] in ('ZETTEL','PLATFORM','GHOST','CONCEPT')}
pairs=list(dict.fromkeys(tuple(sorted((r['from'],r['to']))) for r in native))
for a,b in pairs:
    g.setdefault(a,set()).add(b)
    g.setdefault(b,set()).add(a)
def reachable(start, skip=None):
    seen, stack={start},[start]
    while stack:
        a=stack.pop()
        for b in g[a]-seen:
            if skip and (a,b) in (skip,skip[::-1]):continue
            seen.add(b)
            stack.append(b)
    return seen
unseen=set(g)
components=[]
while unseen:
    group=reachable(min(unseen))
    components.append(len(group))
    unseen-=group
bridges=[(a,b) for a,b in pairs if b not in reachable(a,(a,b))]
degrees=sorted(cards,key=lambda c:(-len(g[c['key']]),c['order']))
describe=lambda k:nodes[k]['title']
maptext=ret+'\n\n'+f'Native field: {len(g)} nodes, {len(native)} edge occurrences, {len(pairs)} unique undirected pairs.\n'
maptext+=f'Connected components: {sorted(components,reverse=True)}\n'
maptext+=f'Leaves: {sum(len(v)==1 for v in g.values())}. Orphans: {sum(not v for v in g.values())}. Bridges: {len(bridges)}.\n'
maptext+='\nRoot platforms\n'+'\n'.join(platforms)+'\n\nMost connected cards\n'+'\n'.join(f"{c['id']} · {len(g[c['key']])} · {c['title']}" for c in degrees[:6])
maptext+='\n\nRecurring open addresses\n'+'\n'.join(f"{len(v)} · {describe(k)}" for k,v in sorted(ghosts.items(),key=lambda kv:-len(kv[1])) if len(v)>1)
maptext+='\n\nSource convergence\n'+'\n'.join(f"{len(b['cards'])} · {b['title']}" for b in sorted(bib.values(),key=lambda b:-len(b['cards'])) if len(b['cards'])>1)
maptext+='\n\nCrossing to pursue\nDoes a right to contradict the metric survive the move from an agile client demonstration to an executive budget review? Follow 010 → 015 → 007.\n\nBridges\n'+'\n'.join(describe(a)+' ↔ '+describe(b) for a,b in bridges)+'\n'
put('000__MAP.txt',maptext)
cols=[
 [n for n in nodes.values() if n['type'] in ('SOURCE','RESOURCE','PROMPT')],
 [nodes[c['key']] for c in cards],
 [n for n in nodes.values() if n['type'] in ('PLATFORM','GHOST','CONCEPT')]]
height=max(len(col) for col in cols)*30+100
positions={}
for j,col in enumerate(cols):
    for i,n in enumerate(col):
        positions[n['key']]=(28+j*400,66+i*30 if j!=1 else 66+round(i*(height-105)/(len(col)-1)))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1230 {height}" role="img" aria-label="Complete field"><title>{ret}</title><rect width="100%" height="100%" fill="#fffdf6"/>']
for j,t in enumerate(['Sources, resources &amp; prompts','Zettels','Platforms &amp; open addresses']):
    svg.append(f'<text x="{28+j*400}" y="31" font-family="serif" font-size="19" fill="#243d35">{t}</text>')
for r in rel:
    if r['type']=='BACKLINK':continue
    x,y=positions[r['from']]; a,b=positions[r['to']]
    opacity='.25' if r in native else '.13'
    svg.append(f'<path d="M{x},{y} C{(x+a)/2},{y} {(x+a)/2},{b} {a},{b}" fill="none" stroke="#376858" opacity="{opacity}"><title>{esc(r["type"]+" · "+r["literal"])}</title></path>')
for n in nodes.values():
    x,y=positions[n['key']]
    label=(n.get('original_id','')+' '+n['title']).strip()
    short=label if len(label)<51 else label[:49]+'…'
    svg.append(f'<g data-jump="{n["key"]}"><title>{esc(label)}</title><circle cx="{x}" cy="{y}" r="3" fill="#456658"/><text x="{x+7}" y="{y+4}" style="paint-order:stroke;stroke:#fffdf6;stroke-width:3px" fill="#27342d" font-family="sans-serif" font-size="11">{esc(short)}</text></g>')
svg.append(f'<text x="28" y="{height-12}" font-size="11">{ret}</text></svg>')
svg=''.join(svg)
put('NETWORK.svg',svg)
mark='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 28"><g fill="none" stroke="#799087" stroke-width="1.4" stroke-linecap="round"><path d="M12 19a10 10 0 0 1 13-13m-9 15a8 8 0 0 0 13-7m-23 6A16 16 0 0 1 26 2m-8 24a14 14 0 0 0 17-15"/><circle cx="21" cy="14" r="1" fill="#799087"/></g></svg>'
put('MARK.svg',mark)
put(paper+'.tex',read('paper.tex'))
citekeys={k for group in re.findall(r'\\cite\w*\{([^}]+)',read('paper.tex')) for k in group.split(',')}
assert citekeys <= {b['key'] for b in bib.values()}
for cmd in [['xelatex','-interaction=nonstopmode','-halt-on-error',paper+'.tex'],['bibtex',paper],['xelatex','-interaction=nonstopmode','-halt-on-error',paper+'.tex'],['xelatex','-interaction=nonstopmode','-halt-on-error',paper+'.tex']]:
    r=subprocess.run(cmd,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if r.returncode:raise RuntimeError(r.stdout.decode(errors='replace')[-6000:])
log=(root/(paper+'.log')).read_text(errors='replace')
warnings=[l for l in log.splitlines() if re.search('Warning|Overfull',l)]
pages=int(re.search(r'Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',root/(paper+'.pdf')],text=True))[1])
for ext in ('aux','out','log','bbl','blg'): (root/(paper+'.'+ext)).unlink(missing_ok=True)
def page(title,body,style=''):
    return f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>body{{background:#f6f4ed;color:#25382e;max-width:78rem;margin:auto;padding:1rem;font:16px/1.45 Georgia,serif}}pre{{white-space:pre-wrap;overflow-wrap:anywhere}}a{{color:#24594c}}{style}</style><h1>{title}</h1><p>{ret}</p>{body}</html>'
put('000__BIBLIOGRAPHY.html',page('Bibliography',''.join('<article><h2>'+esc(b['title'])+'</h2><p>'+esc(b['status']+' · '+b['citation'])+'</p><a href="'+esc(b['url'],quote=True)+'">'+esc(b['url'])+'</a><p>'+esc(', '.join(nodes[k]['original_id'] for k in b['cards']))+'</p><pre>'+esc(b['raw'])+'</pre></article>' for b in bib.values())))
put('NETWORK.html',page('Complete field',svg+'<pre>'+esc(maptext)+'</pre>','svg{display:block;min-width:860px;width:100%;height:auto}'))
put('CARDS.html',page('Print cards',''.join('<article><small>'+c['id']+' · '+CP+'</small><h2>'+esc(c['title'])+'</h2><blockquote>'+esc(c['fields']['PASSAGE'])+'</blockquote><p><b>Question</b> '+esc(c['fields']['QUESTION'])+'</p><p><b>Test</b> '+esc(c['fields']['TEST'])+'</p><footer>'+esc(c['sha'][:16])+' · 000__RETURN_PATH.txt</footer></article>' for c in cards),
    'article{box-sizing:border-box;width:4in;min-height:6in;padding:.27in;margin:1em 0;border:1px solid #88998b;background:white;position:relative;font:12px/1.32 Georgia}article h2{font-size:20px}article blockquote{margin:0;padding-left:.14in;border-left:2px solid #b6c4b5}footer{margin-top:1em;color:#536d60}@page{size:4in 6in;margin:0}@media print{body{margin:0;padding:0;background:white}body>h1,body>p{display:none}article{height:6in;margin:0;border:0;break-after:page;break-inside:avoid}article:last-of-type{break-after:auto}}'))
for p in sorted(src.iterdir()):
    put('_SLIPCASE/input/'+p.name,p.read_bytes())
put('_SLIPCASE/build.py',Path(__file__).read_bytes())
put('_SLIPCASE/rebuild.py',(src/'rebuild.py').read_bytes())
jsonl('_SLIPCASE/NODES.jsonl',nodes.values())
jsonl('_SLIPCASE/RELATIONS.jsonl',rel)
jsonl('_SLIPCASE/RESOURCES.jsonl',resources)
jsonl('_SLIPCASE/APPEARANCES.jsonl',appearances)
put('_SLIPCASE/ALIASES.json',dump(aliases))
assert len(cards)==len(list(root.glob('*__from-*.txt')))==len(list((root/'_MD').glob('*.md')))
assert all((root/c['filename']).read_bytes()==(root/'_MD'/(c['filename'][:-4]+'.md')).read_bytes()==c['payload'].encode() for c in cards)
assert len(native)==sum(len(re.findall(r'\[\[(.+?)\]\]',c['payload'])) for c in cards)
counts=Counter(r['type'] for r in native)
assert counts['MEMBER_OF']==sum(len(re.findall(r'\[\[(.+?)\]\]',c['fields']['PLATFORM'])) for c in cards)
assert counts['LINKS_TO']==sum(len(re.findall(r'\[\[(.+?)\]\]',c['fields']['LINKS'])) for c in cards)
verification=f'''{ret}
SOURCE COVERAGE: Visible three zettel outputs. Earlier conversation or external originals are outside the byte-comparison scope.
EXTRACTION: {len(appearances)} appearances; {len(cards)} TXT cards = Markdown mirrors = JSON records. TXT and Markdown bytes verified.
DUPLICATES / ID COLLISIONS: {len(appearances)-len(cards)} exact duplicates; {sum(len(v)>1 for v in ids.values())} ID collisions.
PLATFORM RELATIONS: {counts['MEMBER_OF']} MEMBER_OF.
LINKS RELATIONS: {counts['LINKS_TO']} LINKS_TO.
WIKILINK COVERAGE: {len(native)} addresses classified; {counts['WIKILINKS_TO']} outside PLATFORM and LINKS.
GHOSTS / AMBIGUITIES / BROKEN REFERENCES: {len(ghosts)} ghosts; {sum(r['state']=='AMBIGUOUS' for r in native)} ambiguous occurrences; {sum(r['state']=='BROKEN_ID' for r in native)} broken ID occurrences.
BIBLIOGRAPHY COVERAGE: {len(bib)} unique raw entries from {len(cards)} card blocks. Supplemental receipts are separately registered.
RESOURCE COVERAGE: {sum(r['state']=='LINK_ONLY' for r in resources)} LINK_ONLY; {sum(r['local'] is not None for r in resources)} local bodies. Full original Forbes paste and external full texts are outside the verified archive.
RECONSTRUCTION STATE: Capsule extraction and byte comparison required by build. Hash scope excludes index.html, READER.html, and MANIFEST.json to avoid circular hashes.
PAPER EVIDENCE COVERAGE: {len(citekeys)} used citekeys, all present. Interpretive mapping in SOURCE_MAP; human review unverified.
ASSEMBLY PROMPT STATUS: All three full prompt transcriptions; transport-byte fidelity unverified. See 000__PROMPTS.txt.
MAKING HISTORY: 000__MAKING_HISTORY.txt identifies agency, selection, and gaps.
PDF STATUS: XeLaTeX/BibTeX compiled; {pages} pages; final log warnings: {warnings or 'none matched'}.
ZIP STATUS: Build requires ZIP CRC checks and capsule extraction test.
STRUCTURE: Root cards, mirrors, indices, paper, offline reader, graph, print views, and reconstruction inputs generated.
'''
put('_SLIPCASE/VERIFICATION.txt',verification)
def files():
    return sorted(p for p in root.rglob('*') if p.is_file() and p.relative_to(root).as_posix()!='index.html')
manifest=dict(checkpoint=CP,schema='15.55-AM',package=ZIP,files={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files() if p.name not in ('MANIFEST.json','READER.html')},cards=[dict(id=c['id'],sha=c['sha'],filename=c['filename']) for c in cards],hash_exclusions=['index.html','READER.html','_SLIPCASE/MANIFEST.json'])
put('_SLIPCASE/MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
payload_files={p.relative_to(root).as_posix():p.read_text() for p in files() if p.suffix in ('.txt','.poml','.bib','.tex','.json','.md') and '/input/' not in p.as_posix() and p.name!='ZETTELS.json' and not p.relative_to(root).as_posix().startswith('_MD/') and p.name not in [c['filename'] for c in cards]}
data=dict(cards=[{k:v for k,v in c.items() if k!='fields'} for c in cards],nodes=list(nodes.values()),native=native,relations=rel,bib=list(bib.values()),resources=resources,mocs=mocs,map=maptext,svg=svg,files=payload_files,pdf=base64.b64encode((root/(paper+'.pdf')).read_bytes()).decode(),paperName=paper+'.pdf',zipName=ZIP)
desk=read('desk.html').replace('__DATA__',safejson(data)).replace('<!--MARK-->',mark)
put('READER.html',desk.replace('__CAPSULE__',''))
def zip_to(target,include_index):
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files()+([root/'index.html'] if include_index else []):
            z.write(p,p.relative_to(root).as_posix())
    if hasattr(target,'seek'):target.seek(0)
    with zipfile.ZipFile(target) as z:assert z.testzip() is None
capsule=io.BytesIO()
zip_to(capsule,False)
put('index.html',desk.replace('__CAPSULE__','<script id="capsule" type="application/octet-stream">'+base64.b64encode(capsule.getvalue()).decode()+'</script>'))
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([sys.executable,root/'_SLIPCASE/rebuild.py',root/'index.html',tmp],check=True)
    for p in files()+[root/'index.html']:
        assert p.read_bytes()==(Path(tmp)/p.relative_to(root)).read_bytes()
zip_to(dest/ZIP,True)
shutil.copy2(root/'index.html',dest/'Denning_Research_Desk.html')
shutil.copy2(root/(paper+'.pdf'),dest/(paper+'.pdf'))
print(verification)
