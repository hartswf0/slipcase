REBUILD

Checkpoint: SLIPCASE-CHAT-ZETTELS-2026-08-18

Core evidence regeneration:
1. Keep all root `NNN__...txt` zettel cards unchanged.
2. Run: `python3 _SLIPCASE/rebuild.py` from package root.
3. The script verifies the hashes in `_SLIPCASE/MANIFEST.json`, reparses card fields, and rewrites `ZETTELS.json`, `ZETTELS.jsonl`, and `_SLIPCASE/NODES.rebuilt.jsonl`.
4. Derived graph views can then be reconstructed from PLATFORM and every `[[...]]` address using the resolution order recorded in this package.

Full desk regeneration:
- `READER.html`, `NETWORK.html`, `NETWORK.svg`, `CARDS.html`, MOCs, arrangements, bibliography views, and paper are derived artifacts and may be rebuilt or replaced without changing evidence.
- The exact assembly instrument is `_PROMPTS/001__SLIPCASE_15.55-AM.txt`.
- `index.html` embeds evidence and is intended to remain a useful single-file replication capsule.

Missing earlier families remain missing until an exact original export is supplied. Never fabricate them during rebuild.
