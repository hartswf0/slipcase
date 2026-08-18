from pathlib import Path
import json,hashlib,re,zipfile,sys
root=Path(__file__).resolve().parent.parent
R=json.loads((root/'ZETTELS.json').read_text())
M={x['id']:x for x in R}
manifest_lines=list(__import__('csv').DictReader((root/'_SLIPCASE'/'ZETTEL_MANIFEST.csv').open()))
errs=[]
for row in manifest_lines:
    r=M[row['id']]; p=root/row['filename']; md=root/'_MD'/row['filename'].replace('.txt','.md')
    if not p.exists() or not md.exists(): errs.append('missing '+row['id']); continue
    if p.read_text()!=r['payload'] or md.read_text()!=r['payload']: errs.append('payload mismatch '+row['id'])
    h=hashlib.sha256(r['payload'].encode()).hexdigest()
    if h!=r['sha256']: errs.append('hash '+row['id'])
rels=[json.loads(x) for x in (root/'_SLIPCASE'/'RELATIONS.jsonl').read_text().splitlines() if x]
plat_occ=sum(len(re.findall(r'\[\[([^\]]+)\]\]',(r.get('fields') or {}).get('PLATFORM','') or '')) for r in R)
links_occ=sum(len(re.findall(r'\[\[([^\]]+)\]\]',(r.get('fields') or {}).get('LINKS','') or '')) for r in R)
wik_occ=sum(len(re.findall(r'\[\[([^\]]+)\]\]',r['payload'])) for r in R)
checks={
'json_records':len(R),'manifest_zettels':len(manifest_lines),'root_zettels':sum(1 for row in manifest_lines if (root/row['filename']).is_file()),'_MD_mirrors':sum(1 for row in manifest_lines if (root/'_MD'/row['filename'].replace('.txt','.md')).is_file()),
'platform_occurrences':plat_occ,'member_of_records':sum(1 for e in rels if e['type']=='MEMBER_OF'),
'links_occurrences':links_occ,'links_to_records':sum(1 for e in rels if e['type']=='LINKS_TO'),
'wikilik_occurrences':wik_occ,'wikilinks_to_records':sum(1 for e in rels if e['type']=='WIKILINKS_TO')}
if not (checks['json_records']==checks['manifest_zettels']==checks['root_zettels']==checks['_MD_mirrors']): errs.append('zettel count equality')
if checks['platform_occurrences']!=checks['member_of_records']: errs.append('platform equality')
if checks['links_occurrences']!=checks['links_to_records']: errs.append('links equality')
if checks['wikilik_occurrences']!=checks['wikilinks_to_records']: errs.append('wikilink equality')
print(json.dumps(checks,indent=2)); print('ERRORS',len(errs)); [print(' -',e) for e in errs]
sys.exit(1 if errs else 0)
