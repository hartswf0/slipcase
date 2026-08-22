#!/usr/bin/env python3
"""Reconstruct the complete text-native research field from GitHub-safe base64 chunks."""
from pathlib import Path
import base64, hashlib, lzma, tarfile, io
ROOT=Path(__file__).resolve().parent
parts=sorted((ROOT/'_PAYLOAD').glob('part-*.b64'))
if not parts: raise SystemExit('no payload chunks found')
b64=b''.join(p.read_bytes() for p in parts)
raw=base64.b64decode(b64)
sha=hashlib.sha256(raw).hexdigest()
expected='45ceb77a9e9220e8ab4e342eed5ee61d3ad506f65914bc43ac93d456d9ea3066'
if sha!=expected: raise SystemExit(f'payload checksum mismatch: {sha}')
tar_bytes=lzma.decompress(raw)
with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode='r:') as tf:
    tf.extractall(ROOT)
print(f'unpacked {len(tf.getmembers())} entries; payload sha256={sha}')
