from pathlib import Path
import hashlib, json, sys

if len(sys.argv) != 3:
    raise SystemExit("usage: restore_capture.py ZETTELS_JSON OUTPUT")
cards=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
ids=[
"4y2eel","bsuq0v","k4pw76","5vyoar","gbdhgr","7tsvhj","00hq9f","2q5xma",
"7tnw3a","f45xni","jpn0ax","0rvzf3","okaf4i","dz4498","fc0ju5","pl6k2u",
"94m7fl","0gdcd0","34u3t7","gzm8pa","1367o3","cw5umh","njn257","dycrsj",
"2intrx","elkebq","cj6cjj","fo2km4","r1mkmi","ypitvg","ugks76","u7f56a",
"yjsbou","252sao","kfip1j","evx74q","pkqb2t"
]
if len(cards)!=len(ids):
    raise SystemExit(f"expected {len(ids)} cards, got {len(cards)}")
fence=chr(96)*3
blocks=[]
for c,ident in zip(cards,ids):
    blocks.append(fence+'text id="'+ident+'"\n'+c["payload"]+'\n'+fence)
body="\n\n".join(blocks)+"\n"
expected="5e7e7c7f6418169ef38e8b019c23eb9a72623af1de938114c8485ede59bc816f"
got=hashlib.sha256(body.encode("utf-8")).hexdigest()
if got!=expected:
    raise SystemExit(f"capture hash mismatch: {got}")
Path(sys.argv[2]).write_text(body,encoding="utf-8")
print("originating capture restored:",got)
