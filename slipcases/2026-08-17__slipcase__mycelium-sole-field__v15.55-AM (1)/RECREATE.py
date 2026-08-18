#!/usr/bin/env python3
import sys,re,json,base64,hashlib
from pathlib import Path
if len(sys.argv)<3:
    raise SystemExit("usage: python RECREATE.py index.html OUTPUT_DIR")
html=Path(sys.argv[1]).read_text(encoding='utf-8')
out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
m=re.search(r'<script id="slipcase-embedded" type="application/json">(.*?)</script>',html,re.S)
if not m: raise SystemExit('embedded package not found')
data=json.loads(m.group(1))
fail=[]
for f in data['files']:
    p=out/f['path']; p.parent.mkdir(parents=True,exist_ok=True)
    b=base64.b64decode(f['b64']); p.write_bytes(b)
    h=hashlib.sha256(b).hexdigest()
    if h!=f['sha256']: fail.append(f['path'])
(out/'index.html').write_text(html,encoding='utf-8')
if fail: raise SystemExit('HASH FAIL: '+', '.join(fail))
print(f"reconstructed {len(data['files'])} embedded files + index.html; hashes verified")
