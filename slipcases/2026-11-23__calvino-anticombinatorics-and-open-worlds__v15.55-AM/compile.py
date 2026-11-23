#!/usr/bin/env python3
"""SLIPCASE reproducible compiler, source archives -> all derived field records.
Uses standard Python libraries plus networkx when present. No network dependencies.
Run: python compile.py .
"""
from __future__ import annotations
import collections, datetime, hashlib, html, json, math, os, pathlib, random, re, shutil, sys, textwrap, unicodedata, zipfile
from urllib.parse import urlparse
ROOT = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).parent).resolve()
RAW = ROOT/'raw'; OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
CHECKPOINT='Calvino-Open-Worlds-2026-11-23'
SCHEMA='SLIPCASE/15.55-AM'; PACKAGENAME='calvino_open_worlds_slipcase_2026-11-23.zip'
DATE='2026-11-23'; ORIGIN='chat-20261123'
PAPER_SLUG='what_constraints_cannot_decide'; PAPER_PREFIX=f'{PAPER_SLUG}__{DATE}'
FIELDS=['ID','TITLE','SOURCE','PASSAGE','RESEARCH OBJECT','LOCAL MOVE','SOURCE TERMS','WHAT BECAME STRANGE','QUESTION','DEEPER QUESTION','MECHANISM','FORMAL SHIFT','SOURCE FORMALISM','OUR FORMALIZATION','TENSION','MISSING','BOUNDARY','CITATION TRAIL','TEST','PLATFORM','LINKS','BIBTEX']
SHA=lambda x:hashlib.sha256(x).hexdigest()
write=lambda p,s: pathlib.Path(p).write_text(s,encoding='utf-8')
jdump=lambda o:json.dumps(o,ensure_ascii=False,indent=2)
mdas = {'research_note__2026-11-23.md':'research_note__2026-11-23.md'}
raw_blocks=[]
for p in [RAW/'001-006.txt',RAW/'007-012.txt',RAW/'013-018.txt',RAW/'005-children.txt']:
  t=p.read_text(encoding='utf-8')
  for m in re.finditer(r'(?ms)^```text\n(.*?)\n```[ \t]*(?:\n|\Z)',t):
    body=m.group(1)+'\n'
    raw_blocks.append((p.name,body))
assert len(raw_blocks)==24,len(raw_blocks)

def slug(s,maxlen=62):
  s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
  s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
  return s[:maxlen].rstrip('-') or 'unnamed'

def parse_fields(payload):
  idmatch=re.search(r'(?m)^ID:[ \t]*([^\n]+)\n',payload)
  out={'ID':idmatch.group(1).strip() if idmatch else ''}
  ms=list(re.finditer(r'(?m)^([A-Z][A-Z ]+|ID):\n',payload))
  for i,m in enumerate(ms):
    key=m.group(1); end=ms[i+1].start() if i+1<len(ms) else len(payload)
    out[key]=payload[m.end():end].strip('\n')
  return out

def parse_bib(bib):
  if not bib or bib=='NONE':return None
  m=re.search(r'@([a-zA-Z]+)\s*\{\s*([^,\s]+)\s*,',bib)
  if not m:return None
  fields={}
  for match in re.finditer(r'(?m)^\s*([a-zA-Z][a-zA-Z_]*)\s*=\s*(\{.*\}|\".*\"|[A-Za-z0-9_-]+)\s*,?\s*$',bib):
    v=match.group(2).strip()
    if v.startswith('{') and v.endswith('}'):v=v[1:-1]
    if v.startswith('"') and v.endswith('"'):v=v[1:-1]
    fields[match.group(1).lower()]=v
  return {'type':m.group(1).lower(),'citekey':m.group(2),'fields':fields,'raw':bib}

records=[]
for idx,(origin,body) in enumerate(raw_blocks,1):
  f=parse_fields(body)
  assert list(f)==FIELDS,(idx,list(f))
  original_id=f['ID'].strip(); bib=parse_bib(f['BIBTEX'])
  sig='SOURCEUNKNOWN'
  if bib:
    key=bib['citekey']; author=bib['fields'].get('author','').split(',')[0].split(' and ')[0].strip()
    sig=(slug(author,24)+'-'+bib['fields'].get('year','nd'))
  filename=f'{idx:03}__{slug(f["TITLE"],53)}__{sig}__{original_id}__from-{ORIGIN}.txt'
  name=filename
  write(OUT/name,body); (OUT/'_MD').mkdir(exist_ok=True); write(OUT/'_MD'/name.replace('.txt','.md'),body)
  records.append({'seq':idx,'original_id':original_id,'id':SHA(body.encode()),'sha256':SHA(body.encode()),'filename':filename,'title':f['TITLE'].strip(),'source':f['SOURCE'].strip(),'source_url':(bib or {}).get('fields',{}).get('url'),'fields':f,'bib':bib,'payload':body,'origin':origin,'status':'ADMITTED','retranscription':'re-entered from visible chat context; no direct transcript export available'})

# Preserve research note and all instructions supplied during active visible scope.
(OUT/'_RESOURCES').mkdir(exist_ok=True)
(OUT/'_PROMPTS').mkdir(exist_ok=True)
resourcepath=OUT/'_RESOURCES'/'research_note__2026-11-23.md'
write(resourcepath,(RAW/'research_note__2026-11-23.md').read_text())
promptfiles=[('forage_initial_v3.0','poml_3_0.xml'),('forage_recursive_v3.1','poml_3_1.xml'),('assembly_slipcase_v15.55-AM','poml_15_55_AM.xml')]
prompts=[]
for name,fn in promptfiles:
  body=(RAW/fn).read_text()
  target='_PROMPTS/'+name+'.xml'
  write(OUT/target,body)
  prompts.append({'id':'PROMPT:'+name,'name':name,'file':target,'sha256':SHA(body.encode()),'body':body,'type':'PROMPT','source':'visible conversation retranscription'})

# BibTeX: preserve every variant in cards, compile normalized citation-level identities.
variants=collections.defaultdict(list)
for r in records:
 if r['bib']: variants[r['bib']['citekey']].append((r['seq'],r['bib']))
refs=[]; refs_by_key={}
for key,items in sorted(variants.items()):
  raws=list(dict.fromkeys(x['raw'] for _,x in items)); canon=items[0][1]
  structural=[{k:v for k,v in x['fields'].items() if k not in ('note','month')} for _,x in items]
  diffmaterial=len(set(json.dumps(x,sort_keys=True) for x in structural))>1
  status='BIB-CONFLICT' if diffmaterial else ('BIB-ALIAS' if len(raws)>1 else ('SHARED' if len(items)>1 else 'UNIQUE'))
  ref={'citekey':key,'type':canon['type'],'fields':canon['fields'],'raw':canon['raw'],'raw_variants':raws,'used_by':[r['original_id'] for r in records if r['bib'] and r['bib']['citekey']==key],'status':status}
  refs.append(ref);refs_by_key[key]=ref
bibhead=f'% SLIPCASE checkpoint: {CHECKPOINT}\n% package: {PACKAGENAME}\n% schema: {SCHEMA}\n% RETURN PATH: 000__RETURN_PATH.txt\n% All raw variants remain in immutable source cards and BIBLIOGRAPHY.html.\n\n'
bibtext=bibhead+'\n\n'.join(x['raw'] for x in refs)+'\n'
write(OUT/(CHECKPOINT+'__references.bib'),bibtext)

# Graph: preserve every wikilink, including ones in CITATION TRAIL and repeated occurrences.
all_by_id=collections.defaultdict(list); all_by_title=collections.defaultdict(list)
for r in records:all_by_id[r['original_id']].append(r);all_by_title[r['title']].append(r)
platform_names=set()
for r in records:
  platform_names.update(re.findall(r'\[\[([^\]\n]+)\]\]',r['fields']['PLATFORM']))
all_addresses=[];relations=[];nodes=[];ghost_data={}
for r in records:
  nodes.append({'id':'Z:'+r['sha256'],'type':'ZETTEL','label':r['title'],'original_id':r['original_id'],'filename':r['filename'],'sha256':r['sha256']})
source_nodes={};
for ref in refs:
  sid='SOURCE:'+ref['citekey'];source_nodes[ref['citekey']]=sid
  nodes.append({'id':sid,'type':'SOURCE','label':ref['fields'].get('title',ref['citekey']),'citekey':ref['citekey'],'url':ref['fields'].get('url'),'bib_status':ref['status']})
for pn in sorted(platform_names):nodes.append({'id':'PLATFORM:'+pn,'type':'PLATFORM','label':pn})

wpat=re.compile(r'\[\[([^\]\n]+)\]\]')
for r in records:
  src='Z:'+r['sha256'];fld=r['fields']
  if r['bib']:
    relations.append({'from':src,'to':source_nodes[r['bib']['citekey']],'type':'USES_SOURCE','literal':r['bib']['citekey'],'source_card':r['original_id'],'source_field':'BIBTEX','ordinal':1,'resolution':'EXACT_CITEKEY','derived':True})
  for field_name,block in fld.items():
    for ordinal,m in enumerate(wpat.finditer(block),1):
      addr=m.group(1)
      rule=None;trg=None
      if addr in all_by_id:
        if len(all_by_id[addr])==1:trg='Z:'+all_by_id[addr][0]['sha256'];rule='EXACT_ID'
        else:rule='AMBIGUOUS_ID'
      elif len(all_by_title.get(addr,[]))==1:
        trg='Z:'+all_by_title[addr][0]['sha256'];rule='EXACT_TITLE'
      elif addr in platform_names:
        trg='PLATFORM:'+addr;rule='EXACT_PLATFORM'
      else:rule='GHOST'
      if not trg:
        trg='GHOST:'+addr
        g=ghost_data.setdefault(addr,{'name':addr,'inbound':[],'first_occurrence':r['seq'],'count':0,'source_cards':[]})
        g['count']+=1;g['source_cards'].append(r['original_id']);g['inbound'].append({'card':r['original_id'],'field':field_name,'ordinal':ordinal})
      edge_type={'PLATFORM':'MEMBER_OF','LINKS':'LINKS_TO'}.get(field_name,'WIKILINKS_TO')
      e={'from':src,'to':trg,'type':edge_type,'literal':addr,'source_card':r['original_id'],'source_field':field_name,'ordinal':ordinal,'resolution':rule,'derived':False}
      relations.append(e);all_addresses.append(e)

# Derived ghost nodes are explicitly different from unresolved wiki-address ghosts.
for r in records:
 text=r['fields']['MISSING'].strip()
 if text and text!='NONE':
  # Each MISSING field is an open research object, not a user-declared link.
  gid='GHOST:OPEN:'+r['original_id']
  ghost_data['OPEN:'+r['original_id']]={'name':f'Open mechanism — {r["original_id"]}','inbound':[{'card':r['original_id'],'field':'MISSING','ordinal':1}], 'first_occurrence':r['seq'],'count':1,'source_cards':[r['original_id']], 'text':text, 'derived':True}
  relations.append({'from':'Z:'+r['sha256'],'to':gid,'type':'REPRESENTED_BY','literal':text,'source_card':r['original_id'],'source_field':'MISSING','ordinal':1,'resolution':'DERIVED_OPEN_QUESTION','derived':True})
for name,g in ghost_data.items():
  nodes.append({'id':'GHOST:'+name,'type':'GHOST','label':g['name'],'derived':g.get('derived',False)})

# A resource entry for each unique BibTeX URL + local pasted note; preserve original sources and linking.
resources=[]
for ref in refs:
 f=ref['fields']
 rid='RESOURCE:'+ref['citekey']
 resources.append({'id':rid,'name':f.get('title',ref['citekey']),'type':'WEB_PDF' if f.get('url','').lower().endswith('.pdf') else 'WEB','author':f.get('author'),'year':f.get('year'),'title':f.get('title'),'url':f.get('url'),'doi':f.get('doi'),'original_file':None,'local_copy':None,'provided_by':'Cited in generated zettel','used_by':ref['used_by'],'state':'LINK_ONLY','note':'Bibliographic metadata supplied in zettels; remote body not republished.'})
 nodes.append({'id':rid,'type':'RESOURCE','label':f.get('title',ref['citekey']),'url':f.get('url')})
 relations.append({'from':source_nodes[ref['citekey']],'to':rid,'type':'REPRESENTED_BY','literal':ref['citekey'],'source_card':None,'source_field':'RESOURCES','ordinal':1,'resolution':'CITEKEY','derived':True})
resources.append({'id':'RESOURCE:research_note','name':'Calvino\'s Anticombinatorics and Contemporary Generative AI','type':'PASTED_RESEARCH_NOTE','author':'Researcher-provided','year':'2026','title':'Calvino\'s Anticombinatorics and Contemporary Generative AI','url':None,'doi':None,'original_file':'visible chat message, 2026-11-23','local_copy':'_RESOURCES/research_note__2026-11-23.md','provided_by':'user in conversation','used_by':[],'state':'PASTED','note':'Text transcribed from visible request; integrity within ZIP hashed, external comparison not conducted.'})
nodes.append({'id':'RESOURCE:research_note','type':'RESOURCE','label':'Original research note'})
for p in prompts:
 nodes.append({'id':p['id'],'type':'PROMPT','label':p['name']})

# Source evidence verification strictly bounded to current web checks.
source_checks={
  'braffort1997ordre':{'status':'OPENED_PRIMARY','details':'Primary author testimony HTML opened 2026-11-23; relevant constraint passages inspected, incl. sections 2–3.'},
  'duncan2012calvino':{'status':'OPENED_PDF_SCREENSHOT','details':'PDF opened and page 103 visually inspected; clinamen discussion and note in text inspected.'},
  'brenner2010creating':{'status':'OPENED_PDF_SCREENSHOT','details':'PDF opened; page 1518 visually inspected, interestingness limitation in extracted page 1522.'},
  'meehan1977talespin':{'status':'OPENED_PRIMARY_SITE','details':'IJCAI proceedings landing page and full-text extraction opened.'},
  'siler2022openworld':{'status':'ACCESS_DENIED','details':'Publisher URL returned an access-block page; claim not independently reverified.'},
}
for res in resources:
 key=res['id'].replace('RESOURCE:','')
 res['verification']=source_checks.get(key,{'status':'NOT_OPENED','details':'Link retained from available BibTeX; content not independently inspected.'})

# Preserve source citations mentioned without compiled BibTeX as raw citation-trail leads.
trail_lines=[]
for r in records:
 for line in r['fields']['CITATION TRAIL'].splitlines():
  if line.strip():trail_lines.append({'card':r['original_id'],'literal':line.strip(),'status':'TRAIL_LEAD_UNVERIFIED_AS_SEPARATE_WORK'})

# Backlinks for every address; class-name relations remain serializable.
backlinks=collections.defaultdict(list)
for e in relations:
 if e['type'] in ('MEMBER_OF','LINKS_TO','WIKILINKS_TO'):
  backlinks[e['to']].append({'from':e['source_card'],'field':e['source_field'],'literal':e['literal']})

# Handful of derived interpretations, explicitly not part of source payloads.
mocs=[
 {'name':'The missing ontology','addresses':['CALVINO-003','CALVINO-005','CALVINO-005.01','CALVINO-005.02','CALVINO-005.03','CALVINO-005.04','CALVINO-005.06'],'thesis':'Begin with what action schemas fail to represent: secrets, states, knowledge, desires, aesthetic criteria.'},
 {'name':'Worlds that refuse closure','addresses':['CALVINO-012','CALVINO-009','CALVINO-017','CALVINO-005.05','CALVINO-018'],'thesis':'Do not precommit to one literal geography when the source permits several world hypotheses.'},
 {'name':'Who carries the exception?','addresses':['CALVINO-001','CALVINO-002','CALVINO-007','CALVINO-011','CALVINO-015','CALVINO-005.06'],'thesis':'Trace the locus of aesthetic choice across author, reader, generator, and training.'},
 {'name':'A second 1977','addresses':['CALVINO-003','CALVINO-008','CALVINO-009','CALVINO-016','CALVINO-005.03'],'thesis':'Parallel, not genealogically proven, architectures of world modeling.'},
]
arrangements=[
 {'name':'Start from a secret','cards':['CALVINO-005.02','CALVINO-005.03','CALVINO-005.04','CALVINO-005.06','CALVINO-003'],'question':'What representation must exist before filtering can begin?'},
 {'name':'The city that may not be one','cards':['CALVINO-017','CALVINO-009','CALVINO-005.05','CALVINO-012','CALVINO-018'],'question':'When should incompatible fictional evidence be unified, branched, or left suspended?'},
 {'name':'The elusive clinamen','cards':['CALVINO-001','CALVINO-007','CALVINO-011','CALVINO-002','CALVINO-015'],'question':'What counts as a deliberate, evidenced exception rather than improbable sampling?'},
]
(OUT/'_MOCS').mkdir(exist_ok=True)
for n,moc in enumerate(mocs,1):
  write(OUT/'_MOCS'/f'{n:02}__{slug(moc["name"])}.md', '# '+moc['name']+'\n\n'+moc['thesis']+'\n\n'+'\n'.join(f'- [[{x}]]' for x in moc['addresses'])+'\n')
(OUT/'_ARRANGEMENTS').mkdir(exist_ok=True)
for n,a in enumerate(arrangements,1):write(OUT/'_ARRANGEMENTS'/f'{n:02}__{slug(a["name"])}.md','# '+a['name']+'\n\n'+a['question']+'\n\n'+' → '.join(f'[[{x}]]' for x in a['cards'])+'\n')

# Persist structured data.
(OUT/'_SLIPCASE').mkdir(exist_ok=True)
write(OUT/'ZETTELS.json',jdump(records)+'\n')
write(OUT/'ZETTELS.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
write(OUT/'ZETTELS.txt',('\n'+'═'*68+'\n').join(f'CARD {r["seq"]:03d} — {r["filename"]}\n\n'+r['payload'] for r in records))
write(OUT/'_SLIPCASE'/'NODES.jsonl',''.join(json.dumps(n,ensure_ascii=False)+'\n' for n in nodes))
write(OUT/'_SLIPCASE'/'RELATIONS.jsonl',''.join(json.dumps(n,ensure_ascii=False)+'\n' for n in relations))
write(OUT/'_SLIPCASE'/'RESOURCES.jsonl',''.join(json.dumps(n,ensure_ascii=False)+'\n' for n in resources))
write(OUT/'_SLIPCASE'/'APPEARANCES.jsonl',''.join(json.dumps({'seq':r['seq'],'sha256':r['sha256'],'original_id':r['original_id'],'origin':r['origin'],'raw_file':r['origin'],'status':'ADMITTED'})+'\n' for r in records))
write(OUT/'_SLIPCASE'/'ALIASES.json',jdump({'exact_aliases':{},'original_ids_colliding':{k:len(v) for k,v in all_by_id.items() if len(v)>1}}))
write(OUT/'_SLIPCASE'/'TRAIL_REFERENCES.jsonl',''.join(json.dumps(n,ensure_ascii=False)+'\n' for n in trail_lines))
write(OUT/'_SLIPCASE'/'BIBLIOGRAPHY_VARIANTS.json',jdump(refs))

stats={
 'cards':len(records),'md':len(list((OUT/'_MD').glob('*.md'))),'unique_original_ids':len(all_by_id),'id_collisions':{k:len(v) for k,v in all_by_id.items() if len(v)>1},
 'duplicate_payloads':len(records)-len(set(r['sha256'] for r in records)),
 'platform_occurrences':sum(e['type']=='MEMBER_OF' for e in relations),
 'links_occurrences':sum(e['type']=='LINKS_TO' for e in relations),
 'all_wikilinks':len(all_addresses),
 'other_field_wikilinks':sum(e['type']=='WIKILINKS_TO' for e in relations),
 'ghosts_unresolved_addresses':len([k for k,v in ghost_data.items() if not v.get('derived')]),
 'ghosts_derived_open_questions':len([k for k,v in ghost_data.items() if v.get('derived')]),
 'nodes':len(nodes),'edges':len(relations),'sources':len(refs),'resources':len(resources),
 'bibliography_status':dict(collections.Counter(r['status'] for r in refs)),
 'source_checks':dict(collections.Counter(x['verification']['status'] for x in resources)),
}
assert stats['cards']==stats['md']==len(records)
assert stats['platform_occurrences']==sum(len(wpat.findall(r['fields']['PLATFORM'])) for r in records)
assert stats['links_occurrences']==sum(len(wpat.findall(r['fields']['LINKS'])) for r in records)
assert stats['all_wikilinks']==sum(len(wpat.findall(v)) for r in records for v in r['fields'].values())

# Ordered paper bibliography in proper readable citekey format.
def bib_citation(ref):
 f=ref['fields']; return f.get('author','Author not recorded')+'. '+f.get('year','n.d.')+'. '+f.get('title','Title not recorded')+'. '+f.get('journal',f.get('booktitle',''))+f.get('volume','')+('. '+f.get('pages') if f.get('pages') else '')
biblines=[f'BIBLIOGRAPHY / {CHECKPOINT}','Exact BibTeX variants remain in root cards and BIBLIOGRAPHY_VARIANTS.json.','']
for ref in refs:
 biblines += [f'[{ref["citekey"]}] {ref["status"]}',bib_citation(ref),f'URL: {ref["fields"].get("url", "not supplied")}',f'DOI: {ref["fields"].get("doi", "not supplied")}',f'Cards: {", ".join(ref["used_by"])}', 'RAW BIBTEX:',ref['raw'],'']
write(OUT/'000__BIBLIOGRAPHY.txt','\n'.join(biblines))
write(OUT/'000__BIBLIOGRAPHY.html','<!doctype html><html lang="en"><meta charset="utf-8"><title>Bibliography — '+CHECKPOINT+'</title><style>body{max-width:920px;margin:3em auto;padding:1em;font:16px Georgia;line-height:1.5;color:#222}section{border-top:1px solid #ccc;padding:1em 0}pre{white-space:pre-wrap;font:12px ui-monospace,monospace;background:#f7f7f7;padding:1em}a{color:#333}small{color:#666}</style><h1>Bibliography</h1><p>'+CHECKPOINT+' · RETURN PATH: 000__RETURN_PATH.txt</p>'+''.join('<section><h3>'+html.escape(x['fields'].get('title',x['citekey']))+'</h3><p>'+html.escape(bib_citation(x))+'</p><small>'+x['status']+' · '+html.escape(', '.join(x['used_by']))+'</small><p><a href="'+html.escape(x['fields'].get('url',''))+'">Source URL</a></p><pre>'+html.escape(x['raw'])+'</pre></section>' for x in refs)+'</html>')

write(OUT/'000__START_HERE.txt',f'''{CHECKPOINT}\n\nBegin with index.html (self-contained), or READER.html (self-contained), or read any root TXT card.\nWorking Paper · AI-augmented research process\nEvidence, prompts, and making history preserved.\n\nScope: 24 visible zettels in the active context, one pasted research note, three pasted POML prompts. No complete account archive or original project repository was available. Captured content was re-entered from visible messages; comparison against a machine-exported transcript was not available.\n\nRead: 000__INDEX.txt / 000__MAP.txt / 000__OPEN_EDGES.txt\nCite: 000__BIBLIOGRAPHY.html / {CHECKPOINT}__references.bib\nResume: 000__RETURN_PATH.txt / 000__REBUILD.txt\nPaper: {PAPER_PREFIX}.pdf\n''')
write(OUT/'000__RETURN_PATH.txt',f'''CHECKPOINT: {CHECKPOINT}\nCHECKPOINT ID: {SHA((CHECKPOINT+DATE).encode())}\nSCHEMA: {SCHEMA}\nPACKAGE: {PACKAGENAME}\nRESEARCHER: user-supplied research context; author identity not explicitly assigned to this paper\nASSEMBLY MODEL: OpenAI GPT-6\nDATE: {DATE}\nREJOIN PHRASE: "Resume {CHECKPOINT} from SLIPCASE index.html; preserve payload SHA-256, rebuild graph, continue the unresolved secret-identity and nonmonotonic world problems."\n\nKEY FILES\nindex.html; ZETTELS.jsonl; _SLIPCASE/MANIFEST.json; _SLIPCASE/RELATIONS.jsonl; {CHECKPOINT}__references.bib; _PROMPTS/assembly_slipcase_v15.55-AM.xml; {PAPER_PREFIX}.tex; {PAPER_PREFIX}.pdf; 000__REBUILD.txt.\n\nRebuild derived files with included compile.py from raw/ input when available. From index.html alone, use Download capsule data / Reconstruction JSON to recover exact root card payloads.\n''')
write(OUT/'000__INDEX.txt',f'{CHECKPOINT} — FLAT CARD INDEX\n\n'+'\n'.join(f'{r["seq"]:03d}  {r["original_id"]}  {r["title"]}\n     {r["filename"]}  SHA256 {r["sha256"]}' for r in records)+'\n')
counts=collections.Counter([e['source_card'] for e in relations if e['type'] in ('LINKS_TO','WIKILINKS_TO')])
maptxt=[f'{CHECKPOINT} — FIELD MAP',f'Cards {stats["cards"]}; linked addresses {stats["all_wikilinks"]}; platforms {len(platform_names)}; ghosts (derived MISSING) {stats["ghosts_derived_open_questions"]}; unresolved [[address]] ghosts {stats["ghosts_unresolved_addresses"]}.','', 'PLATFORMS']
for pn in sorted(platform_names):
 users=[r['original_id'] for r in records if pn in wpat.findall(r['fields']['PLATFORM'])]
 maptxt.append(f'[[{pn}]] <- {", ".join(users)}')
maptxt+=['','MOST LINKING CARDS'] + [f'{rid}: {n}' for rid,n in counts.most_common(12)]
maptxt+=['','GHOSTS']+[f'{g["name"]}: {g.get("text", "Unresolved address")}' for g in ghost_data.values()]
write(OUT/'000__MAP.txt','\n'.join(maptxt)+'\n')
write(OUT/'000__OPEN_EDGES.txt',f'{CHECKPOINT} — OPEN EDGES\n\n'+'\n\n'.join(f'[{r["original_id"]}] {r["fields"]["TITLE"]}\nQUESTION: {r["fields"]["QUESTION"]}\nMISSING: {r["fields"]["MISSING"]}\nTEST: {r["fields"]["TEST"]}' for r in records)+'\n')
write(OUT/'000__RESOURCES.txt',f'{CHECKPOINT} — RESOURCES\nSource contents are link-only unless supplied in the visible conversation.\n\n'+'\n\n'.join(f'[{x["id"]}] {x["name"]}\nTYPE: {x["type"]}\nSTATE: {x["state"]}\nURL: {x["url"] or "none"}\nLOCAL: {x["local_copy"] or "none"}\nCHECK: {x.get("verification",{}).get("status","not applicable")} — {x.get("verification",{}).get("details","")}' for x in resources)+'\n')
write(OUT/'000__PROMPTS.txt',f'{CHECKPOINT} — CONSEQUENTIAL PROMPTS\n\n'+'\n\n'.join(f'{p["name"]} — {p["file"]}\nSHA-256 {p["sha256"]}\n{p["body"]}' for p in prompts))
write(OUT/'000__MAKING_HISTORY.txt',f'''{CHECKPOINT}\nWHO: Researcher supplied the research note, all 24 zettels via prior messages, and three instructions. GPT-6 compiled, structured, drafted and designed the deliverables on {DATE}. No human review of this resulting package is asserted.\n\nORIGIN: Active conversation visible in this turn only, not complete historical archive. Zettels transcribed into raw/*.txt from visible context. Research note and POMLs manually re-entered from same visible context. No direct machine transcript export or byte comparison to original chat was available; source-text exactness against the interface remains UNVERIFIED.\n\nCONTROL: Researcher supplied scope, questions, values, and format. GPT-6 selected paper argument, generated bibliographic normalization and graph resolution, created interface and text. No outside connected accounts were queried.\n\nUNTOUCHED: Once archived into root cards, the cards are not rewritten by the compiler. SHA256 is computed for bytes in this package, not evidence of source transcript identity. Raw BibTeX variants remain in root cards.\n\nVERIFIED: Automated identity counts, mirror byte equality, relation cardinalities. Web pages/PDFs for Braffort, Duncan, Brenner, Meehan were opened; PDF screenshots for Duncan and Brenner inspected. Arithmetic 12**12 computed locally: 8,916,100,448,256.\n\nUNVERIFIED: Full original Calvino archive, Braffort program code, original 1977 demonstration outputs, numerous supplied bibliographic links, source quote wording beyond checked material, user authorship attribution, complete chat history. Siler publisher resource was blocked.\n\nRETURN PATH: 000__RETURN_PATH.txt. REBUILD: 000__REBUILD.txt.\n''')
write(OUT/'000__REBUILD.txt',f'''{CHECKPOINT} — REBUILD PROCEDURE\n\nA. For a local ZIP extract, run python compile.py . from the package root when raw/ inputs are retained. The compiler regenerates root cards and the core graph.\nB. Verify exact payloads with sha256sum against ZETTELS.json sha256; _MD mirrors must be byte-equal to each root card.\nC. Check _SLIPCASE/RELATIONS.jsonl for all PLATFORM, LINKS and other [[address]] occurrences. Do not reinterpret ambiguous IDs as exact links.\nD. In an isolated recipient context, open index.html. The embedded capsule JSON contains zettel payloads, bibliography, graph, prompts, selected resources, paper HTML, and reconstruction metadata. Press "Download reconstruction JSON" and use _SLIPCASE/rebuild_from_capsule.py to restore cards.\nE. Regenerate TeX/PDF from {PAPER_PREFIX}.tex with xelatex twice. References are rendered into the TeX; named references.bib remains as source bibliography.\nF. Merge by SHA256 of payload, never ID/title. Record appearances, ambiguous IDs and citation variants independently. Re-resolve graph.\n\nLIMIT: Manual retranscription is not a verified byte-level chat export. The package supplies internal integrity and transparent provenance only.\n''')
write(ROOT/'stage1.json',jdump({'stats':stats,'refs':[x['citekey'] for x in refs],'cards':[x['original_id'] for x in records]}))
print(jdump(stats))
