#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,sys
R=Path(__file__).resolve().parent.parent
M=json.loads((R/'_SLIPCASE'/'MANIFEST.json').read_text(encoding='utf-8'))
FIELDS=['ID','TITLE','SOURCE','SOURCE URL','PASSAGE','RESEARCH OBJECT','LOCAL MOVE','SOURCE TERMS','WHAT BECAME STRANGE','QUESTION','DEEPER QUESTION','MECHANISM','FORMAL SHIFT','SOURCE FORMALISM','OUR FORMALIZATION','TENSION','MISSING','BOUNDARY','CITATION TRAIL','TEST','PLATFORM','LINKS','BIBTEX']
def sha(b):return hashlib.sha256(b).hexdigest()
def parse(t):
 p=[]
 for f in FIELDS:
  m=re.search(r'(?m)^'+re.escape(f)+r':\s*$',t)
  if m:p.append((m.start(),m.end(),f))
 p.sort();o={f:'' for f in FIELDS}
 for i,(s,e,f) in enumerate(p):o[f]=t[e:(p[i+1][0] if i+1<len(p) else len(t))].strip()
 return o
fail=[];recs=[]
for c in M['immutable_cards']:
 p=R/c['filename'];m=R/c['mirror']
 if not p.exists() or sha(p.read_bytes())!=c['sha256']:fail.append('root:'+c['filename'])
 if not m.exists() or sha(m.read_bytes())!=c['mirror_sha256']:fail.append('mirror:'+c['mirror'])
 if p.exists():
  t=p.read_text(encoding='utf-8');F=parse(t);recs.append({**c,'id':F['ID'] or 'NOID','title':F['TITLE'],'source':F['SOURCE'],'source_url':F['SOURCE URL'],'fields':F,'payload':t})
if fail:
 print('HASH/FILE FAIL');print('\n'.join(fail));sys.exit(2)
(R/'ZETTELS.json').write_text(json.dumps(recs,ensure_ascii=False,indent=2),encoding='utf-8')
with open(R/'ZETTELS.jsonl','w',encoding='utf-8') as f:
 for x in recs:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(f'OK: {len(recs)} immutable card roots and mirrors verified; ZETTELS.json/jsonl rebuilt.')
