from pathlib import Path
import json,hashlib,sys
src=Path(sys.argv[1]); dest=Path(sys.argv[2]); dest.mkdir(parents=True,exist_ok=True); (dest/'_MD').mkdir(exist_ok=True)
records=json.loads(src.read_text(encoding='utf-8'))
for z in records:
    payload=z['payload']; fn=z['filename']; sha=hashlib.sha256(payload.encode()).hexdigest()
    assert sha==z['sha256'], (fn,sha,z['sha256'])
    (dest/fn).write_text(payload,encoding='utf-8'); (dest/'_MD'/fn.replace('.txt','.md')).write_text(payload,encoding='utf-8')
print(f'reconstructed {len(records)} cards; hashes verified')
