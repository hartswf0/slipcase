from pathlib import Path, PurePosixPath
import base64, hashlib, json, re, sys, zipfile, io

source, target = Path(sys.argv[1]), Path(sys.argv[2])
raw = re.search(rb'<script id="capsule" type="application/octet-stream">([A-Za-z0-9+/=]+)</script>', source.read_bytes())
if raw is None:
    raise SystemExit("No capsule found")
with zipfile.ZipFile(io.BytesIO(base64.b64decode(raw[1], validate=True))) as archive:
    if archive.testzip():
        raise SystemExit("Corrupt capsule ZIP")
    if target.exists() and any(target.iterdir()):
        raise SystemExit("Use an empty output directory")
    for name in archive.namelist():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name:
            raise SystemExit(f"Unsafe path {name}")
    archive.extractall(target)
manifest = json.loads((target/'_SLIPCASE/MANIFEST.json').read_text())
for path, digest in manifest['files'].items():
    if hashlib.sha256((target/path).read_bytes()).hexdigest() != digest:
        raise SystemExit(f"Hash mismatch {path}")
(target/'index.html').write_bytes(source.read_bytes())
print(f"Verified {len(manifest['files'])} hashed files")
