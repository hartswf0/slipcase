from pathlib import Path
import json,re,hashlib,subprocess,sys,zipfile
R=Path(__file__).resolve().parents[1]
z=sorted([p for p in R.glob('*.txt') if re.match(r'^(HOUSE|INGOLD)-',p.name)])
m=sorted((R/'_MD').glob('*.md'))
j=json.loads((R/'ZETTELS.json').read_text())
rels=json.loads((R/'_SLIPCASE'/'relations.json').read_text())
checks=[]
def ck(name,cond,detail=''):
    checks.append((name,bool(cond),detail));
    if not cond: raise AssertionError(name+': '+detail)
ck('admitted zettels = root TXT = _MD mirrors = JSON records',len(z)==len(m)==len(j),f'{len(z)} / {len(m)} / {len(j)}')
for p in z:
    q=R/'_MD'/(p.stem+'.md'); ck('mirror '+p.name,q.exists() and q.read_bytes()==p.read_bytes())
for r in j:
    p=R/r['_file']; ck('hash '+r['ID'],hashlib.sha256(p.read_bytes()).hexdigest()==r['_sha256'])
ids=[r['ID'] for r in j]; ck('no ID collisions',len(ids)==len(set(ids)),str(len(ids)))
hashes=[r['_sha256'] for r in j]; duphash=len(hashes)-len(set(hashes))
# relations
pt=sum(len(re.findall(r'\[\[[^\]]+\]\]',re.search(r'(?ms)^PLATFORM:\n(.*?)(?=\n\nLINKS:)',p.read_text()).group(1))) for p in z)
lt=sum(len(re.findall(r'\[\[[^\]]+\]\]',re.search(r'(?ms)^LINKS:\n(.*?)(?=\n\nBIBTEX:)',p.read_text()).group(1))) for p in z)
alladdr=sum(len(re.findall(r'\[\[[^\]]+\]\]',p.read_text())) for p in z)
native=[x for x in rels if x['derivation']=='NATIVE']
ck('PLATFORM occurrences = MEMBER_OF records',pt==sum(1 for x in native if x['edge']=='MEMBER_OF'),str(pt))
ck('LINKS occurrences = LINKS_TO records',lt==sum(1 for x in native if x['edge']=='LINKS_TO'),str(lt))
ck('all [[ADDRESS]] occurrences = classified native relation records',alladdr==len(native),f'{alladdr} / {len(native)}')
broken=[x for x in native if re.match(r'^(HOUSE|INGOLD)-',x['target']) and x['resolution_state'].startswith('UNRESOLVED')]
ck('no broken explicit zettel IDs',not broken,str(broken[:5]))
# bibliography/paper
bib=(R/'SLIPCASE-20260817T2053-0400__references.bib').read_text(); bibkeys=set(re.findall(r'@\w+\{([^,]+),',bib))
tex=(R/'programming-before-specification__2026-08-17.tex').read_text(); cites=set()
for mm in re.finditer(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',tex): cites.update(x.strip() for x in mm.group(1).split(','))
ck('paper citekeys subset bibliography citekeys',cites<=bibkeys,', '.join(sorted(cites-bibkeys)))
maptxt=(R/'programming-before-specification__SOURCE_MAP.txt').read_text(); mapkeys=set(k.strip() for x in re.findall(r'^CITEKEY:\s*(.+)$',maptxt,re.M) for k in x.split(';') if k.strip()!='NONE')
ck('source-map citekeys subset bibliography citekeys',mapkeys<=bibkeys,', '.join(sorted(mapkeys-bibkeys)))
# required artifacts
required=['index.html','000__START_HERE.txt','000__RETURN_PATH.txt','000__INDEX.txt','000__MAP.txt','000__BIBLIOGRAPHY.txt','000__BIBLIOGRAPHY.html','000__RESOURCES.txt','000__PROMPTS.txt','000__OPEN_EDGES.txt','000__MAKING_HISTORY.txt','000__REBUILD.txt','NETWORK.html','NETWORK.svg','READER.html','CARDS.html','MARK.svg','SLIPCASE-20260817T2053-0400__references.bib','programming-before-specification__2026-08-17.tex','programming-before-specification__2026-08-17.pdf','programming-before-specification__SOURCE_MAP.txt','programming-before-specification__2026-08-17__ASSEMBLY_APPENDIX.txt','SLIPCASE_FINAL_PROMPT.txt','ZETTELS.txt','ZETTELS.json','ZETTELS.jsonl']
missing=[x for x in required if not (R/x).exists()]; ck('required root artifacts exist',not missing,', '.join(missing))
for d in ['_MD','_MOCS','_ARRANGEMENTS','_PROMPTS','_RESOURCES','_SLIPCASE']: ck('directory '+d,(R/d).is_dir())
# prompt identity
ck('assembly prompt hash',hashlib.sha256((R/'SLIPCASE_FINAL_PROMPT.txt').read_bytes()).hexdigest()=='9ceab9e5344b73e4218462f2ad86fea590c5b8dde2820aa25c16fd5875362b1a')
# pdf basic health and no obvious unresolved citation placeholders in extracted text
pdf=R/'programming-before-specification__2026-08-17.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1)); ck('paper PDF has pages',pages>=5,str(pages))
txt=subprocess.run(['pdftotext',str(pdf),'-'],capture_output=True,text=True,check=True).stdout
ck('paper has no obvious unresolved citation placeholders','??' not in txt and 'undefined citation' not in txt.lower())
# JS syntax check by extracting inline script
idx=(R/'index.html').read_text(); sm=re.search(r'<script>(.*)</script>',idx,re.S); ck('index has embedded script',bool(sm))
js=R/'_SLIPCASE'/'index-inline.js'; js.write_text(sm.group(1))
node=subprocess.run(['node','--check',str(js)],capture_output=True,text=True); ck('index JavaScript parses',node.returncode==0,node.stderr)
# report
counts={
'admitted_zettels':len(z),'payload_duplicate_hashes':duphash,'platform_occurrences':pt,'links_occurrences':lt,'all_address_occurrences':alladdr,'native_relations':len(native),'derived_relations':len(rels)-len(native),'ghosts':len(set(x['target'] for x in native if x.get('target_type')=='GHOST')),'bibliography_citekeys':len(bibkeys),'paper_citekeys':len(cites),'paper_pages':pages}
report=['VERIFICATION','']+[f'{k}: {v}' for k,v in counts.items()]+['','CHECKS:']+[f'- {"PASS" if ok else "FAIL"}: {name}'+(f' — {detail}' if detail else '') for name,ok,detail in checks]
(R/'_SLIPCASE'/'verification.txt').write_text('\n'.join(report)+'\n')
print('\n'.join(report))
