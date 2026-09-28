from pathlib import Path
import json,re,sys

if len(sys.argv)!=3:
    raise SystemExit("usage: dedupe_bib.py ZETTELS_JSON OUTPUT_BIB")
cards=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
seen=set()
blocks=[]
for c in cards:
    b=(c.get("BIBTEX") or "").strip()
    if not b or b=="NONE":
        continue
    keys=re.findall(r"@\w+\{\s*([^,\s]+)",b)
    if keys and any(k in seen for k in keys):
        if all(k in seen for k in keys):
            continue
        raise SystemExit("partially overlapping BibTeX block: "+c.get("ID","?"))
    seen.update(keys)
    blocks.append(b)
header=(
    "% checkpoint: ENCOUNTER-FIELD-20260928\n"
    "% package: 2026-09-28__encountering-encounter__AI-ENCOUNTER__v15.55-AM\n"
    "% schema: SLIPCASE 15.55-AM\n"
    "% RETURN PATH: 000__RETURN_PATH.txt\n\n"
)
Path(sys.argv[2]).write_text(header+"\n\n".join(blocks)+"\n",encoding="utf-8")
print(f"wrote {len(seen)} unique citekeys from {len(blocks)} blocks")
