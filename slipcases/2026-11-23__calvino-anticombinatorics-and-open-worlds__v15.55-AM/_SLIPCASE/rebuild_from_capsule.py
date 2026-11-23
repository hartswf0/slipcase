#!/usr/bin/env python3
"""Rebuild files from SLIPCASE standalone index.html or exported capsule JSON.
Usage: python rebuild_from_capsule.py index.html reconstructed/
No network, external packages, or original chat needed.
"""
import base64,hashlib,html,json,pathlib,re,sys
src=pathlib.Path(sys.argv[1])
source=src.read_text(encoding='utf-8')
if source.lstrip().startswith('{'):
  c=json.loads(source)
else:
  m=re.search(r'<script id="slipcase-capsule" type="application/json">(.*?)</script>',source,re.S)
  if not m:raise SystemExit('No embedded SLIPCASE capsule found')
  c=json.loads(m.group(1))
root=pathlib.Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=True)
written=[]
for rel,obj in c['files'].items():
  if pathlib.PurePosixPath(rel).is_absolute() or '..' in pathlib.PurePosixPath(rel).parts:raise ValueError(rel)
  data=base64.b64decode(obj['base64']) if obj.get('encoding')=='base64' else obj['content'].encode('utf-8')
  found=hashlib.sha256(data).hexdigest()
  if found!=obj['sha256']:raise ValueError('SHA256 mismatch '+rel)
  target=root/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);written.append(rel)
for card in c['cards']:
  path=root/card['filename']; got=hashlib.sha256(path.read_bytes()).hexdigest()
  if got!=card['sha256']:raise ValueError('Zettel checksum mismatch '+card['filename'])
  mirror=root/'_MD'/card['filename'].replace('.txt','.md')
  if mirror.read_bytes()!=path.read_bytes():raise ValueError('Mirror mismatch '+card['filename'])
(root/'index.html').write_bytes(src.read_bytes())
(root/'READER.html').write_bytes(src.read_bytes())
(root/'_SLIPCASE'/'MANIFEST.json').parent.mkdir(parents=True,exist_ok=True)
(root/'_SLIPCASE'/'MANIFEST.json').write_text(json.dumps(c['manifest'],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checkpoint':c['checkpoint'],'files_restored':len(written),'cards_verified':len(c['cards']),'status':'reconstructed'},indent=2))
