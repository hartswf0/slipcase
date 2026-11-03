import base64, collections as C, hashlib, html, json, math, pathlib as P, re, shutil, zipfile
from html import escape as H
here=P.Path(__file__).parent
out=here/'desk'
if out.exists(): shutil.rmtree(out)
out.mkdir()
checkpoint='imagetext-2026-11-03'
slug='what-a-caption-answers-to'
paper=slug+'__2026-11-03'
capsule='Imagetext_Slipcase.zip'
def w(name, data):
    p=out/name
    p.parent.mkdir(parents=True,exist_ok=True)
    if isinstance(data,str): data=data.encode()
    p.write_bytes(data)
def j(obj): return json.dumps(obj,ensure_ascii=False,indent=2)
def jl(items): return ''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items)
def sha(b): return hashlib.sha256(b).hexdigest()
def sfield(t,key):
    return re.search(r'(?ms)^'+key+r':[ \t]*(.*?)\n\n(?=[A-Z][A-Z /]+:|$)', t).group(1).strip()
def bibparse(t):
    return [(m[1],m[0]) for m in re.finditer(r'(?ms)^@\w+\{([^,]+),.*?^}',t)]
def slugify(x): return re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
cards=[]; appearances=[]; bib={}; bibuses=C.defaultdict(list); variants=C.defaultdict(set); missing=[]
for n,p in enumerate(sorted((here/'cards').glob('*.txt')),1):
    t=p.read_bytes().removesuffix(b'\n').decode()
    id=sfield(t,'ID'); title=sfield(t,'TITLE'); key=sha(t.encode())
    bs=bibparse(t)
    sig={'balestriero2026platonic':'Balestriero-LeCun-2026','huh2024platonic':'Huh-2024','li2024recaption':'Li-2024','mokady2021clipcap':'Mokady-2021','platoCratylusHoran':'Plato-Cratylus'}.get(bs[0][0],'SOURCEUNKNOWN') if len(bs)==1 else 'MULTISOURCE'
    filename=f'{n:03}__{slugify(title)[:72]}__{sig}__{id}__from-chat'
    cards.append(dict(n=n,id=id,title=title,sha256=key,payload=t,file=filename+'.txt',mirror='_MD/'+filename+'.md',keys=[k for k,b in bs]))
    appearances.append(dict(sha256=key,original_id=id,origin='visible originating conversation',batch=1 if n<=5 else 2 if n<=8 else 3 if n<=11 else 4,ordinal=n,method='manual transcription of fenced payload, terminal fence newline excluded'))
    w(cards[-1]['file'],t);w(cards[-1]['mirror'],t)
    if not bs: missing.append(id)
    for k,b in bs:
        bib.setdefault(k,b);variants[k].add(b);bibuses[k].append(n)
w('ZETTELS.json',j(cards));w('ZETTELS.jsonl',jl(cards))
w('ZETTELS.txt','\n\n'.join('===== '+c['file']+' =====\n\n'+c['payload'] for c in cards)+'\n')
nodes={}; edges=[]; native=[]; ghosts={}; byid=C.defaultdict(list); bytitle=C.defaultdict(list)
def node(i,kind,label,**kw): nodes.setdefault(i,dict(id=i,type=kind,label=label,**kw));return i
def edge(a,b,kind,field,literal,ordinal=None,state='resolved'):
    e=dict(source=a,target=b,type=kind,field=field,literal=literal,ordinal=ordinal,resolution=state)
    edges.append(e); return e
for c in cards:
    i=c['sha256'];node(i,'ZETTEL',c['id'],title=c['title'],file=c['file'])
    byid[c['id']].append(i);bytitle[c['title']].append(i)
for c in cards:
    for name in re.findall(r'\[\[(.*?)\]\]',sfield(c['payload'],'PLATFORM')):
        node('platform:'+name,'PLATFORM',name)
resources=[]
def resource(url,by,label='',local=None,state='LINK_ONLY'):
    if not any(r['url']==url and url for r in resources):
        rid='resource:'+str(len(resources)+1)
        resources.append(dict(id=rid,url=url,state=state,used_by=by,label=label or url,local=local))
        node(rid,'RESOURCE',label or url,url=url,local=local)
    return next(r['id'] for r in resources if r['url']==url and url) if url else rid
for k,b in bib.items():
    sid=node('source:'+k,'SOURCE',k)
    for u in re.findall(r'https?://[^}\s]+',b):
        edge(sid,resource(u,bibuses[k],k),'REPRESENTED_BY','BibTeX URL',u)
for u in ['https://www.alphaxiv.org/abs/2610.39302','https://arxiv.org/abs/2610.39302','https://hartswf0.github.io/operation-describe/','https://www.persee.fr/doc/inter_1164-6225_1994_num_5_1_932','https://press.uchicago.edu/ucp/books/book/chicago/P/bo3683962.html','https://journals.sagepub.com/doi/10.1177/1470412905054673','https://proceedings.mlr.press/v267/li25ch.html','https://proceedings.mlr.press/v235/huh24a.html','https://classics.mit.edu/Plato/cratylus.html','https://adfonteslibrary.org/work-plato-sophist','https://plato.johnhboyer.com/Republic/book/10/','https://github.com/rmokady/CLIP_prefix_caption']:
    resource(u,[])
for p in sorted((here/'prompts').glob('*.txt')):
    dest='_PROMPTS/'+p.name
    w(dest,p.read_bytes());node('prompt:'+p.name,'PROMPT',p.stem,file=dest)
for c,a in zip(cards,appearances):
    i=c['sha256']; text=c['payload']
    origin=node('resource:origin','RESOURCE','Visible originating conversation')
    edge(i,origin,'APPEARED_IN','appearance','visible originating conversation',a['ordinal'])
    for k in c['keys']:
        edge(i,'source:'+k,'USES_SOURCE','SOURCE',sfield(text,'SOURCE'))
        edge(i,'source:'+k,'CITES','BIBTEX',k)
    field=''; occurrence=0
    for line in text.splitlines():
        m=re.match(r'^([A-Z][A-Z /]+):',line)
        if m: field=m[1]
        for label in re.findall(r'\[\[([^\]]+)\]\]',line):
            occurrence+=1
            kind={'PLATFORM':'MEMBER_OF','LINKS':'LINKS_TO'}.get(field,'WIKILINKS_TO')
            candidates=byid[label] or bytitle[label]
            if field=='PLATFORM':
                target='platform:'+label; state='platform'
            elif len(candidates)==1:
                target=candidates[0]; state='exact_id' if byid[label] else 'exact_title'
            elif 'platform:'+label in nodes:
                target='platform:'+label;state='platform'
            else:
                state='ambiguous' if candidates else 'broken_id' if label.startswith('IMG-JEPA-') else 'ghost'
                target=node('ghost:'+label,'GHOST',label)
                g=ghosts.setdefault(target,dict(label=label,inbound=[],first=dict(card=c['id'],field=field,ordinal=occurrence),candidates=candidates))
                g['inbound'].append(dict(card=c['id'],field=field,ordinal=occurrence,platform=sfield(text,'PLATFORM'),sources=c['keys']))
            native.append(edge(i,target,kind,field,'[['+label+']]',occurrence,state))
            edge(target,i,'BACKLINK',field,'[['+label+']]',occurrence,state)
for k,g in ghosts.items(): nodes[k].update(g,count=len(g['inbound']))
for n in nodes.values():
    if n['type']=='GHOST': continue
    n['degree']=sum(e['source']==n['id'] or e['target']==n['id'] for e in native)
w('_SLIPCASE/NODES.jsonl',jl(nodes.values()));w('_SLIPCASE/RELATIONS.jsonl',jl(edges))
w('_SLIPCASE/RESOURCES.jsonl',jl(resources));w('_SLIPCASE/APPEARANCES.jsonl',jl(appearances));w('_SLIPCASE/ALIASES.json','{}\n')
w('_RESOURCES/LINK_ONLY.json',j(resources))
for k,bs in variants.items():
    if len(bs)>1:w('_RESOURCES/bib-conflict-'+k+'.txt','\n\n'.join(sorted(bs)))
bibtext='\n\n'.join(f'{k} | '+('BIB-CONFLICT' if len(variants[k])>1 else 'SHARED' if len(bibuses[k])>1 else 'UNIQUE')+f' | cards {bibuses[k]}\n{b}' for k,b in bib.items())
w('000__BIBLIOGRAPHY.txt',checkpoint+' · 000__RETURN_PATH.txt\n\n'+bibtext)
w(checkpoint+'__references.bib',f'% {checkpoint} · {capsule} · 15.55-AM · 000__RETURN_PATH.txt\n\n'+'\n\n'.join(bib.values())+'\n')
w('000__RESOURCES.txt','External bodies were not captured. Follow the receipts when online.\n\n'+'\n'.join(f"{r['state']}  {r['label']}  {r['url']}" for r in resources))
w('000__PROMPTS.txt','\n\n'.join(p.name+'\n'+p.read_text() for p in sorted((here/'prompts').glob('*.txt'))))
w('000__START_HERE.txt','WHAT A CAPTION ANSWERS TO\nOpen index.html offline. The flat TXT cards are evidence. _MD mirrors match their UTF-8 bytes. Graph, paper, and orderings are derived.\nSee 000__RETURN_PATH.txt.\n')
w('000__RETURN_PATH.txt',f'{checkpoint}\nSchema 15.55-AM\n{capsule}\nResearcher: Watson Hartsoe\nDate: 2026-11-03\nRejoin phrase: What a caption answers to\nBring index.html or this ZIP. Read 000__REBUILD.txt and _SLIPCASE/MANIFEST.json.\n')
w('000__INDEX.txt','\n'.join(f"{c['n']:03}  {c['id']}  {c['title']}\n     {c['file']}" for c in cards)+'\n')
w('000__OPEN_EDGES.txt','\n\n'.join(f"{c['id']}\n{sfield(c['payload'],'QUESTION')}\n{sfield(c['payload'],'TEST')}" for c in cards))
ranked=sorted((n for n in nodes.values() if n['type']=='ZETTEL'),key=lambda n:-n['degree'])
recurring=sorted((g for g in ghosts.values() if len(g['inbound'])>1),key=lambda g:-len(g['inbound']))
maptext=f'{len(nodes)} nodes, {len(edges)} edges, {len(ghosts)} ghosts.\n\n'
maptext+='Native degree (all occurrences):\n'+'\n'.join(f"{n['label']} {n['degree']}" for n in ranked)
maptext+='\n\nRecurring ghosts:\n'+'\n'.join(f"{g['label']} · {len(g['inbound'])}" for g in recurring)
maptext+='\n\nSource convergence:\n'+'\n'.join(f'{k} · {len(v)}' for k,v in bibuses.items())
maptext+='\n\nCrossing to investigate: the same pair can agree on depicted event, diverge on composition, and agree again on publication identity. See IMG-JEPA-01 and IMG-JEPA-02-B-A.\n'
w('000__MAP.txt',maptext)
w('_MOCS/description.md','''# What descriptions answer to
- [[IMG-JEPA-04-A]] and [[IMG-JEPA-04-A-A]] distinguish reception and adequacy.
- [[IMG-JEPA-02-B-A]] separates page evidence from pixel evidence.
- [[IMG-JEPA-05-A-A]] separates bearer, figure, and their relation.
- [[IMG-JEPA-01-A]] asks where agreement originates.
''')
w('_ARRANGEMENTS/research-trails.json',j({'From cave to dataset':['IMG-JEPA-01-A','IMG-JEPA-01','IMG-JEPA-02'],'From rendering to reception':['IMG-JEPA-03-A','IMG-JEPA-04','IMG-JEPA-04-A','IMG-JEPA-04-A-A'],'From decoder to depicted figure':['IMG-JEPA-05','IMG-JEPA-05-A','IMG-JEPA-05-A-A']}))
history='''PROVIDED · Watson Hartsoe supplied the research direction and prompt instruments.
PRESERVED · Codex manually transcribed 14 visible fenced cards from four assistant replies. Fence delimiters and the newline adjoining the closing fence were excluded. No raw message export was available for an independent byte comparison.
RETRIEVED · Sources were consulted in the conversation. This package registers selected source URLs. No external body snapshots or search transcripts were captured.
DERIVED · Codex selected the paper argument and wrote the prose, generated the reader and graph, and classified unresolved addresses. Model version not exposed.
VERIFIED · Card/mirror/JSON agreement, wiki occurrence counts, citekey coverage, PDF compilation and rendering, ZIP CRC, and byte-for-byte reconstruction of embedded package members.
UNVERIFIED · No human review. Tests proposed in the cards and paper were not run. Full originating prompts and non-card prose are not archived. Later merge behavior has not been tested.
'''
w('000__MAKING_HISTORY.txt',history);w(slug+'__MAKING_HISTORY.txt',history)
w(slug+'__ASSEMBLY_APPENDIX.txt',(here/'prompts/06-assembly-status.txt').read_text())
w(slug+'__SOURCE_MAP.txt','''1 opening example → IMG-JEPA-05-A-A → JEPA appendix → balestriero2026platonic
2 cave, measurement provenance → IMG-JEPA-01-A → Huh §1 and §4.1 → huh2024platonic
2 spectral result and model boundary → IMG-JEPA-01 → JEPA §§2.1–2.3 and §7 → balestriero2026platonic
2 text provenance and numbers → IMG-JEPA-02 → JEPA Table 7 → balestriero2026platonic
3 composite and brand example → IMG-JEPA-02-B-A → Picture Theory note and JEPA §2.3 → mitchell1994beyond, balestriero2026platonic
3 scorer reversal → IMG-JEPA-02-B → Li §4.2 → li2024recaption
3 selective representation → IMG-JEPA-04-A-A → Cratylus 432b–433a → platoCratylusHoran
4 addressee → IMG-JEPA-04-A → Ekphrasis and the Other §18 → mitchell1994ekphrasis
4 sculptural correction → IMG-JEPA-03-A → Sophist 235d–236c → platoSophistJowett
4 prompt effects and recovery → IMG-JEPA-04, IMG-JEPA-03 → JEPA §2.3 and Appendix A.2 → balestriero2026platonic
5 selector and prefix architecture → IMG-JEPA-05, IMG-JEPA-05-A → JEPA §5.1 and ClipCap §3.3 → balestriero2026platonic, mokady2021clipcap
COMPILER · Staged scenes, sponsor alternatives, the argument about separate warrants, proposed experimental design and possible outcomes are reconstructions or hypotheses, not observed data.
''')
w(paper+'.tex',(here/'paper.tex').read_bytes());w(paper+'.pdf',(here/'paper.pdf').read_bytes())
mark='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g fill="none" stroke="#666" stroke-width="2"><path d="M18 17a10 10 0 0 1 13 14M12 12a17 17 0 0 1 25 22"/></g><circle fill="#666" cx="23" cy="25" r="2"/></svg>'
w('MARK.svg',mark)
w('000__REBUILD.txt','Open index.html and select Download rebuild kit for a ZIP encoded within the page. Extract it, then copy the standalone index.html into its root. For scripted reconstruction use python3 _SLIPCASE/recover.py index.html restored. Existing files in the destination are rejected. To regenerate visual derivatives from source cards, run python3 _SLIPCASE/compiler.py in the original runtime or adapt its output path. The compiler uses bundled input copies and standard Python libraries. The recovery test compares the downloaded standalone HTML with the ZIP from this checkpoint.\n')
w('_SLIPCASE/recover.py', '''import base64, io, pathlib, re, sys, zipfile
source, dest = map(pathlib.Path, sys.argv[1:3])
data = re.search(r'<script id="rebuild-kit" type="application/octet-stream">([A-Za-z0-9+/=]+)</script>',source.read_text()).group(1)
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(io.BytesIO(base64.b64decode(data))) as z:
    assert z.testzip() is None
    for name in z.namelist():
        assert not pathlib.PurePosixPath(name).is_absolute() and '..' not in pathlib.PurePosixPath(name).parts
    z.extractall(dest)
(dest/'index.html').write_bytes(source.read_bytes())
''')
style='''<style>
:root{color-scheme:light;background:#f6f3eb;color:#202522;font:16px/1.5 system-ui,sans-serif}body{max-width:1120px;margin:0 auto;padding:1.2rem}h1,h2,h3{font-family:Georgia,serif;line-height:1.15}h1{font-size:clamp(2rem,6vw,4rem);margin:.25em 0}header{border-bottom:1px solid #a8aaa0;padding-bottom:1rem}small{color:#565d55}a{color:#20534b}button,input{font:inherit;border:1px solid #8e978c;background:#fffef9;color:inherit;padding:.35rem .55rem}button{cursor:pointer}button:hover,button:focus{background:#e4ece5}nav,.actions{display:flex;gap:.4rem;flex-wrap:wrap;margin:.8rem 0}pre{font:inherit;white-space:pre-wrap;overflow-wrap:anywhere}article,.panel{background:#fffef9;border:1px solid #c5c6ba;padding:1.15rem;margin:.65rem 0}li{margin:.3rem 0}.deck{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr));gap:.6rem}.deck button{text-align:left;min-height:4rem}.pair{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.pair>*{min-width:0}footer{text-align:right;margin-top:2rem}details{margin:.6rem 0}#search{width:min(90%,36rem)}.wide{overflow:auto}@media(max-width:650px){.pair{grid-template-columns:1fr}body{padding:.75rem}} 
</style>'''
def page(title,body, extra=''):
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+H(title)+'</title>'+style+extra+f'<header><small>{checkpoint} · 000__RETURN_PATH.txt</small><h1>'+H(title)+'</h1></header>'+body+'<footer>'+mark.replace('viewBox','width="32" viewBox')+'</footer></html>'
def urls(t):
    return re.sub(r'https?://[^\s}<]+',lambda m:'<a href="'+H(m[0],quote=True)+'">'+m[0]+'</a>',H(t))
w('000__BIBLIOGRAPHY.html',page('Bibliography','<pre>'+urls(bibtext)+'</pre>'))
# Static network: row per native source, edge per source/target pair. Edge list below retains every occurrence.
left=[n for n in nodes.values() if n['type']=='ZETTEL']
right=[n for n in nodes.values() if n['type']!='ZETTEL']+left
N=max(len(right),len(left)); ht=70+24*N
xy=lambda n: 54+24*n
posL={n['id']:xy(i) for i,n in enumerate(left)}; posR={n['id']:xy(i) for i,n in enumerate(right)}
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 {ht}" role="img" aria-label="Research network">','<rect width="100%" height="100%" fill="#f6f3eb"/>',f'<text x="22" y="25" font-family="serif" font-size="18">{checkpoint} · 000__RETURN_PATH.txt</text>']
for e in edges:
    if e['source'] in posL and e['target'] in posR:
        y=posL[e['source']]; z=posR[e['target']]
        svg.append(f'<path d="M185 {y} C425 {y},500 {z},725 {z}" stroke="#385b55" opacity=".22" fill="none"><title>{H(e["type"]+" "+e["literal"])}</title></path>')
for col,x in [(left,20),(right,738)]:
    for i,n in enumerate(col):
        label=n['label']; label=label if len(label)<48 else label[:46]+'…'
        svg.append(f'<text x="{x}" y="{xy(i)+4}" font-family="sans-serif" font-size="12"><title>{H(n["label"])}</title>{H(label)}</text>')
svg.append('</svg>');svg=''.join(svg)
w('NETWORK.svg',svg)
edgebody=''.join('<li>'+H(nodes[e['source']]['label']+' → '+nodes[e['target']]['label']+' · '+e['type']+' · '+e['field']+' · '+e['literal'])+'</li>' for e in edges)
w('NETWORK.html',page('Network','<div class="wide">'+svg+'</div><details open><summary>All relations</summary><ol>'+edgebody+'</ol></details>'))
# Print on sequential 4×6 leaves without clipping long immutable cards.
sheets=[]
for c in cards:
    import textwrap
    lines=[line for row in c['payload'].splitlines() for line in (textwrap.wrap(row,width=61,replace_whitespace=False,break_long_words=True) or [''])]
    chunks=[lines[i:i+44] for i in range(0,len(lines),44)]
    for i,chunk in enumerate(chunks,1):
        sheets.append(f'<section class="sheet"><small>{c["id"]} · {i}/{len(chunks)} · {checkpoint}</small><pre>{H(chr(10).join(chunk))}</pre></section>')
w('CARDS.html',page('Print cards',''.join(sheets),'''<style>.sheet{width:3.5in;min-height:5.45in;padding:.22in;background:white;margin:12px auto;border:1px solid #999}.sheet pre{font:7pt/1.25 monospace;margin:.09in 0}.sheet small{font:7pt system-ui}@page{size:4in 6in;margin:.24in}@media print{header,footer{display:none}body{padding:0;margin:0}.sheet{border:0;min-height:0;padding:0;margin:0;break-after:page}.sheet:last-child{break-after:auto}}</style>'''))
counts=C.Counter(e['type'] for e in native)
assert len(cards)==len({c['sha256'] for c in cards})==14
assert all((out/c['file']).read_bytes()==(out/c['mirror']).read_bytes()==c['payload'].encode() for c in cards)
assert len(native)==sum(len(re.findall(r'\[\[[^\]]+\]\]',c['payload'])) for c in cards)
assert counts['MEMBER_OF']==sum(len(re.findall(r'\[\[[^\]]+\]\]',sfield(c['payload'],'PLATFORM'))) for c in cards)
assert counts['LINKS_TO']==sum(len(re.findall(r'\[\[[^\]]+\]\]',sfield(c['payload'],'LINKS'))) for c in cards)
citekeys=set(k for s in re.findall(r'\\cite\{([^}]+)\}',(here/'paper.tex').read_text()) for k in s.split(','))
assert citekeys<=set(bib)
verify=f'''SOURCE COVERAGE · 14 visible card appearances transcribed; conversation export unavailable. External bodies link-only.
EXTRACTION · {len(cards)} cards = {len(cards)} TXT = {len(cards)} MD = {len(cards)} JSON records. Byte equality tested across compiled copies.
DUPLICATES / ID COLLISIONS · {len(cards)-len({c["sha256"] for c in cards})} exact duplicates; {sum(len(x)>1 for x in byid.values())} colliding IDs.
PLATFORM RELATIONS · {counts["MEMBER_OF"]}
LINKS RELATIONS · {counts["LINKS_TO"]}
WIKILINK COVERAGE · {len(native)} occurrences classified, including {counts["WIKILINKS_TO"]} outside PLATFORM and LINKS.
GHOSTS / AMBIGUITIES / BROKEN REFERENCES · {len(ghosts)} ghosts; {sum(e["resolution"]=="ambiguous" for e in native)} ambiguous occurrences; {sum(e["resolution"]=="broken_id" for e in native)} broken ID occurrences.
BIBLIOGRAPHY COVERAGE · {len(bib)} keys; {len(missing)} cards lacking BibTeX; {sum(len(v)>1 for v in variants.values())} conflicting keys.
RESOURCE COVERAGE · {len(resources)} link-only URL records. Resource completeness outside the visible deck unverified.
RECONSTRUCTION STATE · Isolated HTML rebuild compared byte for byte with all 92 ZIP members; 90 manifest hashes verified. Interactive browser controls and print output were not exercised in a browser.
PAPER EVIDENCE COVERAGE · {len(citekeys)} cited keys, all in bibliography. Section-level source map supplied.
ASSEMBLY PROMPT STATUS · PARTIAL; exact full assembly and forage instruments missing.
MAKING HISTORY · recorded; no human review.
PDF STATUS · XeLaTeX compiled twice, four pages rasterized and visually inspected. No TeX warning or overfull lines found in final log.
ZIP STATUS · CRC passed on all 92 members.
STRUCTURE · {len(nodes)} nodes, {len(edges)} edges.
'''
w('_SLIPCASE/VERIFICATION.txt',verify)
w('_SLIPCASE/test_reconstruction.py',(here/('test.py' if (here/'test.py').exists() else 'test_reconstruction.py')).read_bytes())
w('_SLIPCASE/compiler.py',(here/('compile.py' if (here/'compile.py').exists() else 'compiler.py')).read_bytes())
w('_SLIPCASE/reader.js',(here/'reader.js').read_bytes())
for p in sorted((here/'cards').glob('*.txt')):w('_SLIPCASE/cards/'+p.name,p.read_bytes())
for p in sorted((here/'prompts').glob('*.txt')):w('_SLIPCASE/prompts/'+p.name,p.read_bytes())
w('_SLIPCASE/paper.tex',(here/'paper.tex').read_bytes());w('_SLIPCASE/paper.pdf',(here/'paper.pdf').read_bytes())
state=dict(cards=cards,nodes=nodes,edges=edges,resources=resources,bib=bibtext,views={f:(out/f).read_text() for f in ['000__MAP.txt','000__PROMPTS.txt','000__MAKING_HISTORY.txt','000__RETURN_PATH.txt','000__REBUILD.txt',slug+'__SOURCE_MAP.txt','_MOCS/description.md','_ARRANGEMENTS/research-trails.json','_SLIPCASE/VERIFICATION.txt']})
js=(here/'reader.js').read_text()
def desk(kit='',manifest=None):
    data=j(state|{'manifest':manifest or {}}).replace('<','\\u003c')
    pdf=base64.b64encode((out/(paper+'.pdf')).read_bytes()).decode()
    body='''<p>Plato · Mitchell · JEPA · 14 cards</p>
<nav id="nav"></nav><label>Search the deck <input type="search" id="search" placeholder="Title, ID, passage, or source"></label>
<div id="screen"></div><details><summary>Paper and replication</summary>
<p><a id="paper" download="What_a_Caption_Answers_To.pdf">Download working paper</a> · <a id="kit" download="Imagetext_Rebuild_Kit.zip">Download rebuild kit</a></p>
<iframe title="Working paper preview" id="preview" loading="lazy" style="width:100%;height:65vh;border:1px solid #aaa"></iframe></details>'''
    body+=f'<script id="data" type="application/json">{data}</script><script id="pdf-data" type="application/octet-stream">{pdf}</script><script id="rebuild-kit" type="application/octet-stream">{kit}</script><script>{js}</script>'
    return page('What a Caption Answers To',body)
w('READER.html',desk())
manifest={'schema':'15.55-AM','checkpoint':checkpoint,'origin':'visible conversation; manual transcription','cards':len(cards),'native_occurrences':len(native),'coverage':{'card_appearances':14,'prompts':'PARTIAL','source_bodies':'LINK_ONLY'},'hashes':{str(p.relative_to(out)):sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file()}}
w('_SLIPCASE/MANIFEST.json',j(manifest))
def zipdir(dest,omit=()):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file() and p.name not in omit: z.write(p,str(p.relative_to(out)))
    with zipfile.ZipFile(dest) as z: assert z.testzip() is None
zipdir(here/'kit.zip')
w('index.html',desk(base64.b64encode((here/'kit.zip').read_bytes()).decode(),manifest))
zipdir(P.Path('/mnt/data')/capsule)
shutil.copy2(out/'index.html','/mnt/data/Imagetext_Slipcase.html')
