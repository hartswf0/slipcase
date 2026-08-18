from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'_SLIPCASE'/'MANIFEST.json').read_text(encoding='utf-8'))
errors=[]
for c in manifest['zettels']:
    p=root/c['filename']; m=root/'_MD'/Path(c['filename']).with_suffix('.md').name
    if not p.exists(): errors.append('missing '+str(p.relative_to(root))); continue
    data=p.read_bytes(); h=hashlib.sha256(data).hexdigest()
    if h!=c['sha256']: errors.append('hash mismatch '+c['filename'])
    if not m.exists() or m.read_bytes()!=data: errors.append('mirror mismatch '+c['filename'])
print('zettels checked:',len(manifest['zettels']))
print('errors:',len(errors))
for e in errors: print('ERROR',e)
sys.exit(1 if errors else 0)
