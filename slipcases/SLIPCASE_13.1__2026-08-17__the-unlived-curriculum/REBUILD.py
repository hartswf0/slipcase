#!/usr/bin/env python3
import sys,re,json,base64,hashlib
from pathlib import Path
if len(sys.argv)<3: raise SystemExit("usage: python REBUILD.py index.html OUTPUT_DIR")
s=Path(sys.argv[1]).read_text(encoding="utf-8");o=Path(sys.argv[2]);o.mkdir(parents=True,exist_ok=True)
m=re.search(r'<script id="capsule" type="application/json">(.*?)</script>',s,re.S)
if not m: raise SystemExit("capsule missing")
files=json.loads(m.group(1))
for f in files:
    b=base64.b64decode(f["b64"]);h=hashlib.sha256(b).hexdigest()
    if h!=f["sha256"]: raise SystemExit("hash mismatch: "+f["path"])
    p=o/f["path"];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
print(f"RECONSTRUCTED {len(files)} FILES; ALL SHA-256 HASHES MATCH")
