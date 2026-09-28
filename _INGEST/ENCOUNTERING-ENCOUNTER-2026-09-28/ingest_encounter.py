from pathlib import Path
import collections, hashlib, html, json, re, shutil, sys

if len(sys.argv) != 4:
    raise SystemExit('usage: ingest_encounter.py INDEX TARGET INGEST_DIR')
index_path = Path(sys.argv[1])
target = Path(sys.argv[2])
ingest = Path(sys.argv[3])
text = index_path.read_text(encoding='utf-8')
m = re.search(r'<script type="application/json" id="DATA">(.*?)</script>', text, re.S)
if not m:
    raise SystemExit('embedded DATA not found')
d = json.loads(m.group(1).replace('<\\/script>', '</script>'))
if len(d.get('cards', [])) != 37:
    raise SystemExit(f"expected 37 cards, got {len(d.get('cards', []))}")

if target.exists():
    shutil.rmtree(target)
target.mkdir(parents=True)
for sub in ('_MD','_MOCS','_ARRANGEMENTS','_PROMPTS','_RESOURCES','_SLIPCASE'):
    (target/sub).mkdir()
shutil.copy2(index_path, target/'index.html')

for c in d['cards']:
    payload = c['payload']
    got = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    if got != c['_sha256']:
        raise SystemExit(f"card hash mismatch {c['ID']}: {got}")
    fn = c['_filename']
    (target/fn).write_text(payload, encoding='utf-8')
    (target/'_MD'/Path(fn).with_suffix('.md').name).write_text(payload, encoding='utf-8')

(target/'ZETTELS.json').write_text(json.dumps(d['cards'],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(target/'ZETTELS.jsonl').write_text('\n'.join(json.dumps(c,ensure_ascii=False) for c in d['cards'])+'\n',encoding='utf-8')
with (target/'ZETTELS.txt').open('w',encoding='utf-8') as f:
    for i,c in enumerate(d['cards']):
        if i:
            f.write('\n\n'+'='*78+'\n\n')
        f.write(c['payload'])

for src_name in ('zettel_forage_inquiry_opposition_v3.0.txt','zettel_forage_recursive_v3.1.txt'):
    src = ingest/src_name
    if not src.exists():
        raise SystemExit(f'missing staged prompt: {src}')
    shutil.copy2(src,target/'_PROMPTS'/src_name)
(target/'_PROMPTS'/'assembly_prompt.txt').write_text(d['assembly_prompt'],encoding='utf-8')
(target/'000__PROMPTS.txt').write_text(
    'PROMPTS\n\n'
    '- _PROMPTS/zettel_forage_inquiry_opposition_v3.0.txt\n'
    '- _PROMPTS/zettel_forage_recursive_v3.1.txt\n'
    '- _PROMPTS/assembly_prompt.txt\n',encoding='utf-8')

for name,body in d['mocs'].items():
    (target/'_MOCS'/name).write_text(body,encoding='utf-8')
for name,body in d['arrangements'].items():
    (target/'_ARRANGEMENTS'/name).write_text(body,encoding='utf-8')

(target/'encountering-encounter__2026-09-28.tex').write_text(d['paper_tex'],encoding='utf-8')
(target/'encountering-encounter__2026-09-28.html').write_text(d['paper_html'],encoding='utf-8')
(target/'encountering-encounter__2026-09-28__SOURCE_MAP.txt').write_text(d['source_map'],encoding='utf-8')
(target/'encountering-encounter__2026-09-28__MAKING_HISTORY.txt').write_text(d['making_history'],encoding='utf-8')
(target/'encountering-encounter__2026-09-28__ASSEMBLY_APPENDIX.txt').write_text(
    'ASSEMBLY INSTRUMENT\n\nExact publication assembly prompt: _PROMPTS/assembly_prompt.txt\nThe same prompt is embedded in index.html.\n',encoding='utf-8')
(target/'000__MAKING_HISTORY.txt').write_text(d['making_history'],encoding='utf-8')
(target/'000__RETURN_PATH.txt').write_text(d['return_path'],encoding='utf-8')
(target/'000__REBUILD.txt').write_text(d['rebuild'],encoding='utf-8')

bibs=[]; seen=set()
for c in d['cards']:
    b=c.get('BIBTEX','').strip()
    if b and b!='NONE' and b not in seen:
        seen.add(b); bibs.append(b)
bib_header=(
    '% checkpoint: ENCOUNTER-FIELD-20260928\n'
    '% package: 2026-09-28__encountering-encounter__AI-ENCOUNTER__v15.55-AM\n'
    '% schema: v15.55-AM\n'
    '% RETURN PATH: 000__RETURN_PATH.txt\n\n')
(target/'encounter_field_20260928__references.bib').write_text(bib_header+'\n\n'.join(bibs)+'\n',encoding='utf-8')
bib_lines=['BIBLIOGRAPHY','',f'UNIQUE BIBTEX BLOCKS: {len(bibs)}','']
for i,b in enumerate(bibs,1):
    mm=re.search(r'@[^{]+\{\s*([^,\s]+)',b)
    bib_lines += [f"{i:02d}. {mm.group(1) if mm else 'UNRESOLVED'}",b,'']
bib_text='\n'.join(bib_lines)
(target/'000__BIBLIOGRAPHY.txt').write_text(bib_text,encoding='utf-8')
(target/'000__BIBLIOGRAPHY.html').write_text(
    "<!doctype html><meta charset='utf-8'><title>Encounter bibliography</title><style>body{max-width:900px;margin:40px auto;font:15px/1.5 system-ui}pre{white-space:pre-wrap}</style><h1>Bibliography</h1><pre>"+html.escape(bib_text)+"</pre>",encoding='utf-8')

with (target/'000__RESOURCES.txt').open('w',encoding='utf-8') as f:
    f.write('RESOURCES\n\n')
    for r in d['resources']:
        f.write(f"NAME: {r.get('name','')}\nTYPE: {r.get('type','')}\nSTATE: {r.get('state','')}\nURL: {r.get('url') or 'NONE'}\nUSED BY: {', '.join(r.get('used_by',[])) or 'NONE'}\n\n")
with (target/'_RESOURCES'/'originating_zettel_capture_fenced.txt').open('w',encoding='utf-8') as f:
    for c in d['cards']:
        f.write('~~~text\n'+c['payload'].rstrip('\n')+'\n~~~\n\n')

edges=['OPEN EDGES','']
for c in d['cards']:
    edges += [f"## {c['ID']} — {c['TITLE']}",
              f"QUESTION: {c.get('QUESTION','NONE')}",
              f"DEEPER QUESTION: {c.get('DEEPER QUESTION','NONE')}",
              f"MISSING: {c.get('MISSING','NONE')}",
              f"TEST: {c.get('TEST','NONE')}",'']
(target/'000__OPEN_EDGES.txt').write_text('\n'.join(edges),encoding='utf-8')

def jsonl(path,rows):
    path.write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in rows)+'\n',encoding='utf-8')
jsonl(target/'_SLIPCASE'/'NODES.jsonl',d['nodes'])
jsonl(target/'_SLIPCASE'/'RELATIONS.jsonl',d['relations'])
jsonl(target/'_SLIPCASE'/'RESOURCES.jsonl',d['resources'])
jsonl(target/'_SLIPCASE'/'APPEARANCES.jsonl',[
    {'card':c['_filename'],'original_id':c['ID'],'order':c['_order'],'origin':'conversation-visible encounter research'}
    for c in d['cards']])
(target/'_SLIPCASE'/'ALIASES.json').write_text('{}\n',encoding='utf-8')
(target/'_SLIPCASE'/'ORIGINAL_MANIFEST.json').write_text(json.dumps(d['manifest'],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

counts=collections.Counter(r['type'] for r in d['relations'])
map_lines=['ENCOUNTER FIELD MAP','',f"NODES: {len(d['nodes'])}",f"RELATIONS: {len(d['relations'])}",'']
map_lines += [f'{k}: {v}' for k,v in sorted(counts.items())]
map_lines += ['','RELATIONS','']
for r in d['relations']:
    map_lines.append(f"{r.get('source')} --{r.get('type')}--> {r.get('target')} [{r.get('resolution','')}]")
(target/'000__MAP.txt').write_text('\n'.join(map_lines)+'\n',encoding='utf-8')

def esc(s):
    return html.escape(str(s))
cards_html=["<!doctype html><meta charset='utf-8'><title>Encounter cards</title><style>@page{size:6in 4in;margin:.25in}body{margin:0;font:10pt Georgia,serif}article{box-sizing:border-box;width:5.5in;height:3.5in;padding:.15in;page-break-after:always;overflow:hidden;border:1px solid #999;white-space:pre-wrap}h2{font:700 11pt system-ui;margin:0 0 .08in}</style>"]
for c in d['cards']:
    cards_html.append(f"<article><h2>{esc(c['ID'])} · {esc(c['TITLE'])}</h2>{esc(c['payload'])}</article>")
(target/'CARDS.html').write_text(''.join(cards_html),encoding='utf-8')
shutil.copy2(target/'index.html',target/'READER.html')

zs=[n for n in d['nodes'] if n.get('type')=='ZETTEL']
w=1200; row=28; h=max(400,80+row*len(zs))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>text{{font:13px system-ui;fill:#111}} .id{{font-weight:700}}</style><rect width="100%" height="100%" fill="white"/>']
for i,n in enumerate(zs):
    y=35+i*row
    svg.append(f'<circle cx="24" cy="{y}" r="4" fill="#111"/><text class="id" x="38" y="{y+4}">{esc(n["id"])}</text><text x="190" y="{y+4}">{esc(n.get("label",""))}</text>')
svg.append('</svg>')
(target/'NETWORK.svg').write_text(''.join(svg),encoding='utf-8')
(target/'NETWORK.html').write_text("<!doctype html><meta charset='utf-8'><title>Encounter network</title><object data='NETWORK.svg' type='image/svg+xml' style='width:100%;height:100vh'></object>",encoding='utf-8')

mark='''<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 72 72" role="img" aria-label="mediation mark"><g fill="none" stroke="#333" stroke-width="2.2" stroke-linecap="round"><path d="M28 38c4-5 11-6 16-2"/><path d="M21 45c8-12 24-15 35-6"/><path d="M15 51c12-18 36-22 51-9"/></g><circle cx="34" cy="32" r="2.7" fill="#333"/><path d="M31 35c2 2 5 2 7 0" fill="none" stroke="#333" stroke-width="1.25" stroke-linecap="round"/></svg>'''
(target/'MARK.svg').write_text(mark+'\n',encoding='utf-8')

(target/'000__START_HERE.txt').write_text(
'''ENCOUNTER SLIPCASE

START HERE

This is a portable research field on encounter as a historical, philosophical, HCI, and AI concept, with a special focus on making relational human–AI encounter empirically falsifiable.

READ FIRST
1. encountering-encounter__2026-09-28.pdf — current scholarly wager.
2. 000__MAP.txt — topology and active ghosts.
3. _MOCS/Operational_Encounter_Model.md — operational constellation.
4. READER.html — offline card desk.
5. 000__BIBLIOGRAPHY.html — evidence.

Evidence cards are immutable payloads. Derived maps, graphs, MOCs, and the paper are revisable views.
''',encoding='utf-8')

recon='''#!/usr/bin/env python3
from pathlib import Path
import sys,re,json,hashlib
if len(sys.argv)!=3: raise SystemExit("usage: RECONSTRUCT.py INDEX_HTML OUTPUT_DIR")
index=Path(sys.argv[1]).read_text(encoding="utf-8")
m=re.search(r'<script type="application/json" id="DATA">(.*?)</script>',index,re.S)
if not m: raise SystemExit("embedded DATA not found")
data=json.loads(m.group(1).replace("<\\\\/script>","</script>"))
out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True); (out/"_MD").mkdir(exist_ok=True)
for c in data["cards"]:
    fn=c["_filename"]; payload=c["payload"]
    (out/fn).write_text(payload,encoding="utf-8")
    (out/"_MD"/fn.replace(".txt",".md")).write_text(payload,encoding="utf-8")
bad=[c["ID"] for c in data["cards"] if hashlib.sha256(c["payload"].encode()).hexdigest()!=c["_sha256"]]
print(json.dumps({"cards_reconstructed":len(data["cards"]),"hash_failures":bad,"output":str(out)},indent=2))
if bad: raise SystemExit(2)
'''
(target/'RECONSTRUCT.py').write_text(recon,encoding='utf-8')

(target/'_SLIPCASE'/'GITHUB_INGEST.txt').write_text(
    'github_ingest_verified: true\n'
    'checkpoint: ENCOUNTER-FIELD-20260928\n'
    'schema: v15.55-AM\n'
    'source: standalone index.html replication capsule\n'
    'capsule_sha256: 9fe104eab98e66956b3887eeb9b5ccd9661637116cb7441cdc03025875d57113\n'
    'original_local_zip_sha256: 29c318381f496313f6284908a71ede8c193da77249b02cf33490bcc111d1a024\n'
    'immutable_card_payloads_verified: 37/37\n'
    'note: binary PDFs are regenerated on GitHub from preserved sources; original local ZIP hash is retained as a receipt.\n',
    encoding='utf-8')

assert len(list(target.glob('*__from-CONVERSATION.txt'))) == 37
assert len(list((target/'_MD').glob('*.md'))) == 37
for c in d['cards']:
    if hashlib.sha256((target/c['_filename']).read_bytes()).hexdigest()!=c['_sha256']:
        raise SystemExit('payload verification failed: '+c['ID'])

files=sorted(p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file())
(target/'000__INDEX.txt').write_text('INDEX\n\n'+'\n'.join(files)+'\n',encoding='utf-8')
print(json.dumps({'cards':37,'nodes':len(d['nodes']),'relations':len(d['relations']),'resources':len(d['resources']),'files_before_pdf':len(files)},indent=2))
