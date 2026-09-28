#!/usr/bin/env python3
from pathlib import Path
import sys,re,json,hashlib
if len(sys.argv)!=3: raise SystemExit("usage: RECONSTRUCT.py INDEX_HTML OUTPUT_DIR")
index=Path(sys.argv[1]).read_text(encoding="utf-8")
m=re.search(r'<script type="application/json" id="DATA">(.*?)</script>',index,re.S)
if not m: raise SystemExit("embedded DATA not found")
data=json.loads(m.group(1).replace("<\\/script>","</script>"))
out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True); (out/"_MD").mkdir(exist_ok=True)
for c in data["cards"]:
    fn=c["_filename"]; payload=c["payload"]
    (out/fn).write_text(payload,encoding="utf-8")
    (out/"_MD"/fn.replace(".txt",".md")).write_text(payload,encoding="utf-8")
bad=[c["ID"] for c in data["cards"] if hashlib.sha256(c["payload"].encode()).hexdigest()!=c["_sha256"]]
print(json.dumps({"cards_reconstructed":len(data["cards"]),"hash_failures":bad,"output":str(out)},indent=2))
if bad: raise SystemExit(2)
