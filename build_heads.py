from pathlib import Path
import collections
import json
import math
import re

ROOT = Path(__file__).resolve().parent
SLIPCASES = ROOT / "slipcases"
MANIFEST = ROOT / "slipcases.json"

STOP = {
    "the","and","for","that","with","from","into","this","these","those","what","when",
    "where","which","who","how","why","are","was","were","been","being","have","has",
    "had","does","did","its","their","our","your","not","but","can","may","might","must",
    "will","would","should","could","about","across","through","between","within","without",
    "field","slipcase","final","paper","source","research","zettel","zettels","all","case",
    "2026","pdf","prompt","prompts"
}

def clean_ws(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

def humanize(folder):
    s = re.sub(r"^\d{4}-\d{2}-\d{2}__", "", folder)
    s = re.sub(r"__(?:FINAL|FULL|v[\w.\-]+|[A-Z0-9\-]+)$", "", s, flags=re.I)
    s = s.replace("__", " — ").replace("_", " ").replace("-", " ")
    return clean_ws(s).title()

def section(text, names):
    if not text:
        return ""
    lines = text.splitlines()
    wanted = {n.upper() for n in names}
    for i, line in enumerate(lines):
        raw = line.strip()
        m = re.match(r"^([A-Z][A-Z0-9 _/\-]{2,50})\s*:\s*(.*)$", raw)
        if m and m.group(1).strip().upper() in wanted:
            if m.group(2).strip():
                return clean_ws(m.group(2))
            out = []
            for nxt in lines[i+1:]:
                t = nxt.strip()
                if not t:
                    if out:
                        break
                    continue
                if re.match(r"^[A-Z][A-Z0-9 _/\-]{2,50}\s*:?\s*$", t):
                    break
                out.append(t)
            if out:
                return clean_ws(" ".join(out))
        if raw.upper() in wanted:
            out = []
            for nxt in lines[i+1:]:
                t = nxt.strip()
                if not t:
                    if out:
                        break
                    continue
                if re.match(r"^[A-Z][A-Z0-9 _/\-]{2,50}\s*:?\s*$", t):
                    break
                out.append(t)
            if out:
                return clean_ws(" ".join(out))
    return ""

def first_question(text):
    if not text:
        return ""
    for para in re.split(r"\n\s*\n", text):
        q = clean_ws(para)
        if "?" in q and 20 <= len(q) <= 420:
            return q[:q.rfind("?")+1]
    return ""

def tokens(text):
    return {
        t for t in re.findall(r"[a-z][a-z0-9]{2,}", (text or "").lower())
        if t not in STOP and not t.isdigit()
    }

if not MANIFEST.exists():
    raise SystemExit("slipcases.json missing; run build_index_html.py first")

cases = json.loads(MANIFEST.read_text(encoding="utf-8"))
if not cases:
    raise SystemExit("empty slipcase manifest")

# Ignore previously generated heads when regenerating.
for case in cases:
    case["cards"] = [
        c for c in case.get("cards", [])
        if not str(c.get("type", "")).upper().startswith("HEAD")
        and not str(c.get("fn", "")).startswith("000A__HEAD__")
    ]
    case["card_count"] = len(case["cards"])

# Build a lookup for existing cards and measure within/cross-case connectivity.
lookup = {}
for case in cases:
    for card in case["cards"]:
        for k in (card.get("id"), card.get("fn"), card.get("title")):
            if k:
                lookup[str(k).lower()] = card

degree = collections.Counter()
bridges = collections.Counter()
for case in cases:
    for card in case["cards"]:
        for target in card.get("links") or []:
            tc = lookup.get(str(target).lower())
            if not tc or tc.get("id") == card.get("id"):
                continue
            degree[(case["id"], card.get("id"))] += 1
            degree[(tc["case_id"], tc.get("id"))] += 1
            if tc["case_id"] != case["id"]:
                pair = tuple(sorted((case["id"], tc["case_id"])))
                bridges[pair] += 1

heads = []
head_by_case = {}

for idx, case in enumerate(cases, 1):
    field_id = f"HEAD-FIELD-{idx:03d}"
    cards = case["cards"]
    specials = case.get("specials") or {}
    start = specials.get("000__START_HERE.txt", "")
    structural = start or "\n\n".join(str(v) for k, v in specials.items() if k.endswith(".txt"))

    anchor = None
    if cards:
        anchor = max(
            cards,
            key=lambda c: (
                degree[(case["id"], c.get("id"))],
                bool((c.get("fields") or {}).get("QUESTION")),
                -int(c.get("num") or 0),
            ),
        )

    title = ""
    for ln in structural.splitlines():
        t = clean_ws(ln)
        if 5 <= len(t) <= 150 and not re.match(r"^(checkpoint|status|read first|field|return)\b", t, re.I):
            title = t
            break
    if not title:
        title = humanize(case["folder"])
    head_title = title if "HEAD" in title.upper() else f"{title} — HEAD"

    fields = (anchor or {}).get("fields") or {}
    question = clean_ws(fields.get("QUESTION") or fields.get("DEEPER QUESTION") or "")
    if not question:
        question = section(structural, ["CORE QUESTION", "RESEARCH QUESTION", "QUESTION"])
    if not question:
        question = first_question(structural)
    if not question:
        question = f"What governing problem organizes the field {humanize(case['folder'])}?"

    thesis = clean_ws(
        fields.get("RESEARCH OBJECT")
        or fields.get("WHAT BECAME STRANGE")
        or fields.get("LOCAL MOVE")
        or ""
    )
    if not thesis:
        thesis = section(structural, ["ARGUMENT", "THESIS", "WAGER", "CLAIM", "OVERVIEW"])
    if not thesis and anchor:
        thesis = clean_ws(anchor.get("title"))
    if not thesis:
        thesis = "This head preserves the case as a single navigable field and binds its zettels, documents, and PDFs to one entry point."

    child_ids = [str(c.get("id") or c.get("fn")) for c in cards]
    pdfs = case.get("pdfs") or []
    bridge_rows = []
    for other in cases:
        if other["id"] == case["id"]:
            continue
        n = bridges.get(tuple(sorted((case["id"], other["id"]))), 0)
        if n:
            bridge_rows.append((n, other["id"]))
    bridge_rows.sort(reverse=True)

    head = {
        "id": field_id,
        "field_no": idx,
        "accession": case.get("accession") or f"SLP / FIELD {idx:03d}",
        "case_id": case["id"],
        "case_title": title,
        "title": head_title,
        "question": question,
        "thesis": thesis,
        "anchor_id": (anchor or {}).get("id"),
        "child_ids": child_ids,
        "child_count": len(child_ids),
        "pdf_count": len(pdfs),
        "pdfs": [{"name": p["name"], "rel": p["rel"]} for p in pdfs],
        "bridges": [{"case_id": cid, "weight": n} for n, cid in bridge_rows],
    }
    heads.append(head)
    head_by_case[case["id"]] = head

# Write one first-class HEAD ZETTEL at the front of every case.
for h in heads:
    cdir = SLIPCASES / h["case_id"]
    cdir.mkdir(parents=True, exist_ok=True)
    for old in cdir.glob("000A__HEAD__*.txt"):
        old.unlink()

    child_links = "\n".join(f"[[{cid}]]" for cid in h["child_ids"]) or "(no indexed child zettels in this preserved projection)"
    pdf_links = "\n".join(f"[[PDF::{p['rel']}]]" for p in h["pdfs"]) or "(no PDFs in this case)"
    bridge_links = "\n".join(
        f"[[{head_by_case[b['case_id']]['id']}]] × {b['weight']} cross-case card links"
        for b in h["bridges"][:12]
    ) or "(no explicit cross-case card links yet)"
    all_links = [f"[[{cid}]]" for cid in h["child_ids"]]
    all_links += [f"[[{head_by_case[b['case_id']]['id']}]]" for b in h["bridges"][:12]]

    body = f"""HEAD ZETTEL

ID:
{h['id']}

TITLE:
{h['title']}

TYPE:
HEAD ZETTEL

TOPIC:
{h['case_title']}

ACCESSION:
{h['accession']}

CASE:
{h['case_id']}

QUESTION:
{h['question']}

THESIS:
{h['thesis']}

ANCHOR:
{f"[[{h['anchor_id']}]]" if h['anchor_id'] else "STRUCTURAL FIELD / NO SINGLE CHILD ANCHOR"}

SCOPE:
{h['child_count']} descendant zettels
{h['pdf_count']} PDFs

HEAD INVARIANT:
This is the single entry zettel for this case. It must remain first in the deck, point downward to the preserved child field, outward to the PDFs, and sideways to explicit cross-case bridges.

CHILDREN:
{child_links}

PDF MAP:
{pdf_links}

BRIDGES:
{bridge_links}

LINKS:
{chr(10).join(all_links) if all_links else "(none yet)"}
"""
    (cdir / f"000A__HEAD__FIELD-{h['field_no']:03d}.txt").write_text(body, encoding="utf-8")

# Build the 38 HEAD <-> 126 PDF mapping.
pdf_rows = []
for h in heads:
    for p in h["pdfs"]:
        pdf_rows.append({
            "id": f"PDF-{len(pdf_rows)+1:03d}",
            "name": p["name"],
            "rel": p["rel"],
            "home_head": h["id"],
            "home_case": h["case_id"],
        })

head_docs = {}
df = collections.Counter()
for h in heads:
    case = next(x for x in cases if x["id"] == h["case_id"])
    child_titles = " ".join(c.get("title", "") for c in case["cards"])
    ts = tokens(" ".join([h["title"], h["question"], h["thesis"], child_titles]))
    head_docs[h["id"]] = ts
    for t in ts:
        df[t] += 1

N = len(heads)
def similarity(pdf_name, head_id):
    pt = tokens(Path(pdf_name).stem.replace("_", " ").replace("-", " "))
    ht = head_docs[head_id]
    overlap = pt & ht
    if not overlap:
        return 0.0, []
    score = sum(math.log((N + 1) / (df[t] + 1)) + 1 for t in overlap)
    denom = sum(math.log((N + 1) / (df[t] + 1)) + 1 for t in pt) or 1
    return score / denom, sorted(overlap)

related_edges = []
for p in pdf_rows:
    ranked = []
    for h in heads:
        if h["id"] == p["home_head"]:
            continue
        score, shared = similarity(p["name"], h["id"])
        if score > 0:
            ranked.append((score, len(shared), h["id"], shared))
    ranked.sort(reverse=True)
    p["related_heads"] = []
    for score, nshared, hid, shared in ranked[:3]:
        if nshared >= 2 and score >= 0.22:
            rel = {"head": hid, "score": round(score, 4), "shared_terms": shared}
            p["related_heads"].append(rel)
            related_edges.append({
                "source": p["id"], "target": hid, "type": "lexical_related",
                "score": round(score, 4), "shared_terms": shared
            })

ownership_edges = [
    {"source": p["home_head"], "target": p["id"], "type": "owns"}
    for p in pdf_rows
]
bridge_edges = [
    {
        "source": head_by_case[a]["id"],
        "target": head_by_case[b]["id"],
        "type": "cross_case_cards",
        "weight": w,
    }
    for (a, b), w in sorted(bridges.items())
]

mapping = {
    "schema": "SLIPCASE_HEAD_PDF_MAP_V1",
    "counts": {
        "heads": len(heads),
        "pdfs": len(pdf_rows),
        "ownership_edges": len(ownership_edges),
        "related_pdf_head_edges": len(related_edges),
        "head_bridge_edges": len(bridge_edges),
    },
    "heads": heads,
    "pdfs": pdf_rows,
    "edges": ownership_edges + related_edges + bridge_edges,
}
(ROOT / "heads-pdf-map.json").write_text(json.dumps(mapping, indent=2), encoding="utf-8")

lines = [
    "SLIPCASE — HEAD ZETTEL / PDF MAP",
    f"{len(heads)} HEADS · {len(pdf_rows)} PDFs",
    "",
    "INVARIANT",
    "Every case has exactly one HEAD ZETTEL. Every PDF has exactly one home HEAD.",
    "Additional PDF→HEAD edges are lexical leads, not source-grounded claims.",
    "",
]
for h in heads:
    lines += [
        f"{h['id']}  {h['title']}",
        f"CASE: {h['case_id']}",
        f"QUESTION: {h['question']}",
        f"CHILDREN: {h['child_count']}",
        f"PDFS: {h['pdf_count']}",
    ]
    for p in h["pdfs"]:
        lines.append(f"  → {p['name']}")
    for b in h["bridges"][:8]:
        lines.append(f"  ↔ {head_by_case[b['case_id']]['id']}  ({b['weight']} explicit card links)")
    lines.append("")
(ROOT / "heads-pdf-map.txt").write_text("\n".join(lines), encoding="utf-8")

data_js = json.dumps(mapping, separators=(",", ":")).replace("</", "<\\/")
page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>SLIPCASE — 38 HEADS / 126 PDFs</title><link rel="icon" type="image/png" href="slipcase.png"><style>
:root{--ink:#111318;--muted:#6b7280;--line:#e5e7eb;--blue:#0647e5;--paper:#fff}*{box-sizing:border-box}html,body{margin:0;background:var(--paper);color:var(--ink);font:14px/1.35 ui-sans-serif,system-ui,-apple-system,sans-serif}header{position:sticky;top:0;z-index:4;background:#fffffff2;border-bottom:1px solid var(--line);padding:14px 16px;backdrop-filter:blur(12px)}h1{font-size:16px;margin:0 0 3px}.sub{font-size:12px;color:var(--muted)}#wrap{display:grid;grid-template-columns:minmax(280px,38%) 1fr;min-height:calc(100vh - 58px)}#heads{border-right:1px solid var(--line);padding:8px}.head{display:block;width:100%;border:0;border-bottom:1px solid var(--line);background:#fff;padding:12px 10px;text-align:left;cursor:pointer}.head b{display:block;font-size:13px}.head span{display:block;color:var(--muted);font-size:11px;margin-top:3px}.head.active{background:#eef3ff;box-shadow:inset 3px 0 var(--blue)}#pdfs{padding:10px 14px}.pdf{padding:10px 4px;border-bottom:1px solid var(--line)}.pdf b{font-size:12px}.pdf small{display:block;color:var(--muted)}.pdf.hit{background:#eef3ff}.pdf.related{box-shadow:inset 3px 0 #9ca3af;padding-left:10px}#empty{padding:30px;color:var(--muted)}@media(max-width:720px){#wrap{grid-template-columns:1fr}#heads{border-right:0}.head:not(.active){display:none}header{position:relative}}
</style></head><body><header><h1>38 HEAD ZETTELS ↔ 126 PDFs</h1><div class="sub">one canonical entry per case · ownership + explicit cross-case bridges + lexical PDF leads</div></header><div id="wrap"><div id="heads"></div><div id="pdfs"><div id="empty">Choose a HEAD.</div></div></div><script>const D=__DATA__;const heads=document.querySelector('#heads'),pdfs=document.querySelector('#pdfs');const byHead=Object.fromEntries(D.heads.map(h=>[h.id,h]));function show(id){document.querySelectorAll('.head').forEach(x=>x.classList.toggle('active',x.dataset.id===id));const h=byHead[id];const owned=D.pdfs.filter(p=>p.home_head===id);const related=D.pdfs.filter(p=>(p.related_heads||[]).some(r=>r.head===id)&&p.home_head!==id);let out=`<div style="padding:8px 4px 14px"><b>${h.id}</b><div style="font-size:18px;margin:4px 0">${h.title}</div><div style="color:#6b7280">${h.question}</div><div style="margin-top:8px">${h.child_count} child zettels · ${h.pdf_count} home PDFs</div></div>`;out+=owned.map(p=>`<div class="pdf hit"><b>${p.name}</b><small>HOME · ${p.rel}</small></div>`).join('');if(related.length)out+=`<div style="padding:18px 4px 4px;font-size:11px;color:#6b7280">RELATED PDF LEADS</div>`+related.map(p=>`<div class="pdf related"><b>${p.name}</b><small>HOME ${p.home_head}</small></div>`).join('');pdfs.innerHTML=out||'<div id="empty">No PDFs.</div>';}D.heads.forEach(h=>{const b=document.createElement('button');b.className='head';b.dataset.id=h.id;b.innerHTML=`<b>${h.id} · ${h.case_title}</b><span>${h.child_count} zettels · ${h.pdf_count} PDFs</span>`;b.onclick=()=>show(h.id);heads.appendChild(b);});show(D.heads[0].id);</script></body></html>""".replace("__DATA__", data_js)
(ROOT / "heads-pdf-map.html").write_text(page, encoding="utf-8")

print(f"HEAD map built: {len(heads)} heads, {len(pdf_rows)} PDFs, {len(ownership_edges)} ownership edges, {len(bridge_edges)} head bridges, {len(related_edges)} lexical PDF leads.")
