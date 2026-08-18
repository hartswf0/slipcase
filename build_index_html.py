import os, glob, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
slipcases_dir = os.path.join(BASE_DIR, 'slipcases')
folders = sorted([f for f in os.listdir(slipcases_dir) if os.path.isdir(os.path.join(slipcases_dir, f)) and not f.startswith('.')])

# Meta Clusters for Cases of Cases (Brand Command v1.0 Taxonomy)
META_CLUSTERS = {
    '01. Epistemics & Formalization': [
        '2026-08-17__prompt-semantics-hidden-machinery__SES-20260817-234319-a5ef0e2e',
        '2026-08-18__martina-deferred-specification__FINAL-SLIPCASE',
        'FINAL_SLIPCASE__Mastery_Without_Sovereignty__ALL_ZETTELS__2026-08-18',
        'SLIPCASE__theory-lag__20260818T030003-0400',
        'SLIPCASE_AFTER_SURPRISE_FINAL_2026-08-18',
        'SLIPCASE_DEEP_LINEAGE_2026-08-18',
        'SLIPCASE__PROMOTION_FIELD__2026-08-18__74d74484bfdd',
        'slipcase_ontology_build'
    ],
    '02. Cultural Semiotics & Craft': [
        '2026-08-17__the-shop-makes-the-prompt__SLIPCASE-20260817-AIACS-01',
        '2026-08-18__prompt-battles-smackdown__PB-SC-20260818-4D1C1A7BD0__slipcase',
        'slipcase_noise_of_sculptors_2026-08-17_2254',
        'the-casino-in-the-fountain__slipcase-v15.55-AM__156066d527d3__2026-08-17T203217-0400',
        'prompt-practices__FINAL__2026-08-18',
        'slipcase-intro__2026-08-18__082152Z',
        'slipcase_final_20260818'
    ],
    '03. Architecture, Construction & Space': [
        'HOUSE_LANGUAGE_SUBURB_SLIPCASE_2026-08-18',
        'house-language__FULL-FINAL__2026-08-18',
        'house_language_many_mansions_2026-08-18',
        'primitive_construction_slipcase_20260818',
        'THE_HUT__FINAL_FIELD__2026-08-18',
        'black-mountain-structured-openness__SCF-20260818-BMC-004__v15.55-AM__FINAL'
    ],
    '04. Models, Generative Loops & Trajectories': [
        '2026-08-18__what-kind-of-thing-is-the-model__Andrew__FULL__v15.55-AM',
        '2026-08-18__what-can-you-still-reopen__16-zettels__FINAL',
        'prompt-forward-slipcase-2026-08-18',
        'prompt-magic-generative-trajectory__2026-08-18',
        'the-prompt-keeps-disappearing__FINAL-SLIPCASE-15.55-AM__2026-08-18',
        'how_is_this_gonna_be_screwed_up_20260817'
    ],
    '05. Relational Freedom & Governance': [
        'safe-relational-freedom-field__2026-08-18__a5ef0e2e',
        '2026-08-17__slipcase__mycelium-sole-field__v15.55-AM (1)',
        'SLIPCASE_13.1__2026-08-17__the-unlived-curriculum',
        'YELMO_FINAL__all-zettels-and-paper'
    ]
}

cases_data = []
all_notes = []
all_pdfs = []
cards_lookup = {}

def parse_card_file(filepath, case_id, case_name, case_idx, idx):
    with open(filepath, 'r', errors='ignore') as f:
        content = f.read()
        
    lines = content.split('\n')
    sections = {}
    cur_field = None
    cur_lines = []
    
    header_re = re.compile(r'^([A-Z0-9_\-\s]{2,40}):\s*(.*)$')
    
    for line in lines:
        m = header_re.match(line)
        if m and m.group(1).strip() == m.group(1).strip().upper() and not line.startswith('http') and not line.startswith('HTTP'):
            field = m.group(1).strip()
            if cur_field:
                sections[cur_field] = '\n'.join(cur_lines).strip()
            cur_field = field
            val = m.group(2).strip()
            cur_lines = [val] if val else []
        else:
            if cur_field:
                cur_lines.append(line)
                
    if cur_field:
        sections[cur_field] = '\n'.join(cur_lines).strip()
        
    cid = sections.get('ID') or sections.get('ZETTEL ID') or os.path.splitext(os.path.basename(filepath))[0]
    if '\n' in cid: cid = cid.split('\n')[0].strip()
    if not cid: cid = os.path.splitext(os.path.basename(filepath))[0]
        
    title = sections.get('TITLE') or sections.get('HEADLINE') or sections.get('QUESTION') or os.path.splitext(os.path.basename(filepath))[0]
    if '\n' in title: title = title.split('\n')[0].strip()
        
    card_type = sections.get('TYPE') or sections.get('OPERATOR') or 'ZETTEL'
    if '\n' in card_type: card_type = card_type.split('\n')[0].strip()
        
    topic = sections.get('TOPIC') or sections.get('THEME') or sections.get('PLATFORM') or case_name
    if '\n' in topic: topic = topic.split('\n')[0].strip()
        
    symbol = sections.get('SYMBOL') or (card_type[:2].capitalize() if card_type else 'Zt')
    if '\n' in symbol: symbol = symbol.split('\n')[0].strip()
        
    source = sections.get('SOURCE') or sections.get('SOURCES') or ''
    passage = sections.get('PASSAGE') or sections.get('EVIDENCE') or sections.get('EXCERPT') or ''
    
    # Extract wikilinks [[...]]
    raw_links = re.findall(r'\[\[(.*?)\]\]', content)
    clean_links = sorted(list(set([l.strip() for l in raw_links if l.strip()])))
    
    fields = {}
    known_keys = {'ID', 'TITLE', 'TYPE', 'TOPIC', 'SYMBOL', 'SOURCE', 'PASSAGE', 'ZETTEL ID', 'HEADLINE', 'OPERATOR', 'THEME'}
    for k, v in sections.items():
        if k not in known_keys and v:
            fields[k] = v
            
    if 'QUESTION' in sections and 'QUESTION' not in fields:
        fields['QUESTION'] = sections['QUESTION']
        
    card_obj = {
        'id': cid,
        'fn': os.path.splitext(os.path.basename(filepath))[0],
        'num': idx + 1,
        'title': title,
        'type': card_type,
        'topic': topic,
        'symbol': symbol,
        'source': source,
        'passage': passage,
        'case_id': case_id,
        'case_idx': case_idx,
        'case_name': case_name,
        'links': clean_links,
        'fields': fields,
        'raw': content
    }
    return card_obj

card_global_idx = 0
for folder_idx, folder in enumerate(folders):
    w = os.path.join(slipcases_dir, folder)
    clean_name = folder.replace('__', ' — ').replace('_', ' ').replace('-', ' ')
    accession_code = f"SLP / FIELD {str(folder_idx + 1).zfill(3)}"
    
    meta_field = 'General Research'
    for mf, cases_list in META_CLUSTERS.items():
        if folder in cases_list:
            meta_field = mf
            break
    
    # PDFs (exclude MARK.pdf)
    pdfs = glob.glob(f'{w}/**/*.pdf', recursive=True) + glob.glob(f'{w}/*.pdf')
    pdfs = sorted(list(set(pdfs)))
    pdfs = [p for p in pdfs if not os.path.basename(p) == 'MARK.pdf']
    pdf_list = []
    for p in pdfs:
        rel = os.path.relpath(p, BASE_DIR)
        p_obj = {
            'name': os.path.basename(p),
            'rel': rel,
            'case_id': folder,
            'case_idx': folder_idx,
            'case_name': clean_name,
            'accession': accession_code,
            'size': os.path.getsize(p),
            'is_paper': not ('_RESOURCES' in p or 'scan' in p.lower())
        }
        pdf_list.append(p_obj)
        all_pdfs.append(p_obj)
        
    # Text cards
    txt_files = sorted([f for f in glob.glob(f'{w}/*.txt') if not os.path.basename(f).startswith('000__')])
    case_notes = []
    for tf in txt_files:
        card = parse_card_file(tf, folder, clean_name, folder_idx, card_global_idx)
        card_global_idx += 1
        case_notes.append(card)
        all_notes.append(card)
        cards_lookup[card['id'].lower()] = card
        cards_lookup[card['fn'].lower()] = card
        cards_lookup[card['title'].lower()] = card
        
    # Specials (structural docs)
    specials = {}
    for sf in sorted(glob.glob(f'{w}/000__*.txt')):
        sname = os.path.basename(sf)
        try:
            with open(sf, 'r', errors='ignore') as f:
                specials[sname] = f.read()
        except:
            pass
            
    cases_data.append({
        'id': folder,
        'accession': accession_code,
        'meta_field': meta_field,
        'name': clean_name,
        'folder': folder,
        'pdf_count': len(pdf_list),
        'pdfs': pdf_list,
        'card_count': len(case_notes),
        'cards': case_notes,
        'specials': specials
    })

# Build Relational Graph Model (Cases of Cases, Slips of Slips)
graph_nodes = []
graph_links = []
case_relation_matrix = {}

# 1. Add 31 Case Hub Nodes
for c_idx, c in enumerate(cases_data):
    graph_nodes.append({
        'id': f"case_{c['id']}",
        'label': c['name'],
        'type': 'case',
        'meta_field': c['meta_field'],
        'accession': c['accession'],
        'card_count': c['card_count'],
        'pdf_count': c['pdf_count'],
        'case_idx': c_idx,
        'r': 18
    })

# 2. Add 1,244 Slip Nodes & Containment Links
for card in all_notes:
    graph_nodes.append({
        'id': f"slip_{card['id']}",
        'label': card['title'],
        'type': 'slip',
        'card_type': card['type'],
        'topic': card['topic'],
        'case_id': card['case_id'],
        'case_idx': card['case_idx'],
        'card_idx': card['num'] - 1,
        'r': 6
    })
    # Case -> Slip link
    graph_links.append({
        'source': f"case_{card['case_id']}",
        'target': f"slip_{card['id']}",
        'type': 'contains',
        'w': 1
    })

# 3. Add Verified Card-to-Card Links & Cross-Case Bridges
for card in all_notes:
    for link_target in card['links']:
        target_card = cards_lookup.get(link_target.lower())
        if target_card and target_card['id'] != card['id']:
            graph_links.append({
                'source': f"slip_{card['id']}",
                'target': f"slip_{target_card['id']}",
                'type': 'cross_cite',
                'w': 1.5
            })
            if card['case_id'] != target_card['case_id']:
                pair = tuple(sorted([card['case_id'], target_card['case_id']]))
                case_relation_matrix[pair] = case_relation_matrix.get(pair, 0) + 1

# 4. Add Cross-Case Bridges
for (c1, c2), count in case_relation_matrix.items():
    graph_links.append({
        'source': f"case_{c1}",
        'target': f"case_{c2}",
        'type': 'case_bridge',
        'count': count,
        'w': min(6, 2 + count * 0.1)
    })

graph_data = {
    'nodes': graph_nodes,
    'links': graph_links,
    'meta_clusters': META_CLUSTERS
}

# Save standalone JSON datasets
with open(os.path.join(BASE_DIR, 'slipcases.json'), 'w') as f:
    json.dump(cases_data, f, indent=2)

from build_data import prompts_data

html_template = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F7F8FA">
<link rel="icon" type="image/png" href="slipcase.png">
<title>SLIPCASE — Portable Research Field</title>
<style>
/* SLIPCASE Master Brand Command v1.0 Design Tokens */
:root {
  --blue: #0647E5;
  --blue-soft: #E7EEFF;
  --blue-hover: #053bc2;
  --paper: #FFFFFF;
  --bg: #F7F8FA;
  --ink: #111318;
  --muted: #9CA3AF;
  --muted-dark: #6B7280;
  --line: #E5E7EB;
  --line-dark: #D1D5DB;
  --code-bg: #F3F4F6;
  --top: env(safe-area-inset-top);
  --bottom: env(safe-area-inset-bottom);
}
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; margin: 0; padding: 0; }
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
}
button, input, select { font: inherit; color: inherit; }
button { border: 0; background: none; cursor: pointer; }

#app {
  position: fixed;
  inset: 0;
  background: var(--bg);
  display: flex;
  flex-direction: column;
}

/* Master Header */
header {
  position: absolute;
  z-index: 30;
  top: 0;
  left: 0;
  right: 0;
  height: calc(62px + var(--top));
  padding: var(--top) 16px 0;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 12px;
  align-items: center;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}
.brand-group {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}
.brand-logo-svg {
  width: 26px;
  height: 26px;
  stroke: var(--blue);
  stroke-width: 1.6;
  fill: none;
}
.brand-text-col {
  display: flex;
  flex-direction: column;
}
.brand-wordmark {
  font-size: 13.5px;
  font-weight: 900;
  letter-spacing: .14em;
  color: var(--blue);
  line-height: 1.1;
}
.brand-subtitle {
  font-size: 8px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--muted-dark);
  text-transform: uppercase;
  margin-top: 2px;
}

.search-wrap {
  position: relative;
  width: 100%;
  max-width: 520px;
}
.search {
  width: 100%;
  height: 40px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--bg);
  padding: 0 32px 0 12px;
  outline: 0;
  font-size: 13px;
  color: var(--ink);
  transition: all .15s ease;
}
.search:focus {
  border-color: var(--blue);
  background: var(--paper);
  box-shadow: 0 0 0 3px var(--blue-soft);
}
.search-shortcut {
  position: absolute;
  right: 10px;
  top: 11px;
  font-size: 10px;
  font-family: ui-monospace, SFMono-Regular, monospace;
  color: var(--muted);
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 1px 5px;
  pointer-events: none;
}

.accession-badge-btn {
  height: 38px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--bg);
  padding: 0 12px;
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .06em;
  color: var(--blue);
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}
.accession-badge-btn:hover {
  background: var(--blue-soft);
  border-color: var(--blue);
}

/* Master Triad Methodology Navigation (PRESERVE · RELATE · RETURN) */
.methodology-bar {
  position: absolute;
  z-index: 29;
  left: 0;
  right: 0;
  top: calc(62px + var(--top));
  height: 48px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
  overflow-x: auto;
  scrollbar-width: none;
}
.methodology-bar::-webkit-scrollbar { display: none; }

.nav-triad-group {
  display: flex;
  align-items: center;
  gap: 4px;
}
.nav-pillar-label {
  font-size: 8.5px;
  font-weight: 900;
  letter-spacing: .12em;
  color: var(--muted);
  text-transform: uppercase;
  margin-right: 6px;
  padding-left: 4px;
}
.nav-tab-btn {
  border: 1px solid transparent;
  border-radius: 6px;
  padding: 6px 11px;
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted-dark);
  text-transform: uppercase;
  white-space: nowrap;
  transition: all .12s ease;
}
.nav-tab-btn:hover {
  color: var(--ink);
  background: var(--bg);
}
.nav-tab-btn.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.nav-divider {
  width: 1px;
  height: 18px;
  background: var(--line);
  margin: 0 8px;
}

/* Sub-toolbar (Filter Chips for LINES) */
.subtoolbar {
  position: absolute;
  z-index: 28;
  left: 0;
  right: 0;
  top: calc(110px + var(--top));
  height: 38px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 5px;
  overflow-x: auto;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
  scrollbar-width: none;
}
.subtoolbar::-webkit-scrollbar { display: none; }
.subchip {
  flex: 0 0 auto;
  border: 1px solid var(--line);
  border-radius: 4px;
  background: var(--paper);
  padding: 4px 8px;
  font-size: 8.5px;
  font-weight: 850;
  letter-spacing: .05em;
  color: var(--muted-dark);
  text-transform: uppercase;
}
.subchip.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}

/* Main Viewport */
main {
  position: absolute;
  top: calc(148px + var(--top));
  bottom: calc(14px + var(--bottom));
  left: 0;
  right: 0;
  overflow-y: auto;
  background: var(--bg);
  scrollbar-width: none;
}
main.top-short {
  top: calc(110px + var(--top));
}
main::-webkit-scrollbar { display: none; }

/* View Panes */
.pane { display: none; width: 100%; height: 100%; }
.pane.active { display: block; }

/* =========================================================
   1. LINES MODE (ZETTEL LINES INSPECTOR)
   ========================================================= */
.lines-container {
  max-width: 860px;
  margin: 0 auto;
  background: var(--paper);
  border-left: 1px solid var(--line);
  border-right: 1px solid var(--line);
  min-height: 100%;
}
.zgroup {
  border-bottom: 8px solid var(--bg);
}
.zhead {
  position: sticky;
  top: 0;
  z-index: 5;
  background: rgba(255,255,255,.98);
  backdrop-filter: blur(12px);
  padding: 12px 16px 10px;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: start;
  cursor: pointer;
}
.zid {
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 9px;
  font-weight: 850;
  letter-spacing: .08em;
  color: var(--blue);
  margin-bottom: 3px;
  text-transform: uppercase;
}
.ztitle {
  font-size: 15px;
  line-height: 1.25;
  font-weight: 850;
  letter-spacing: -.02em;
}
.ztype {
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 8.5px;
  font-weight: 850;
  color: var(--muted-dark);
  border: 1px solid var(--line);
  padding: 3px 6px;
  border-radius: 4px;
  background: var(--bg);
  white-space: nowrap;
}

.lineRow {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 14px;
  padding: 13px 16px;
  border-bottom: 1px solid var(--line);
  background: var(--paper);
  position: relative;
  user-select: none;
  cursor: pointer;
}
.lineRow:last-child { border-bottom: 0; }
.lineRow.selected { background: var(--blue); color: #fff; }
.lineRow.selected .fieldName { color: var(--blue-soft); }
.fieldName {
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 8.5px;
  line-height: 1.3;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--muted-dark);
  text-transform: uppercase;
  padding-top: 3px;
  word-break: break-word;
}
.lineText {
  font-family: "Source Serif 4", ui-serif, Georgia, serif;
  font-size: 16.5px;
  line-height: 1.5;
  white-space: pre-wrap;
}
.lineRow[data-field="TITLE"] .lineText,
.lineRow[data-field="QUESTION"] .lineText,
.lineRow[data-field="DEEPER QUESTION"] .lineText {
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  font-weight: 760;
  letter-spacing: -.025em;
}
.lineRow[data-field="TITLE"] .lineText { font-size: 18px; line-height: 1.24; }
.lineRow[data-field="QUESTION"] .lineText { font-size: 18.5px; line-height: 1.26; }
.lineRow[data-field="DEEPER QUESTION"] .lineText { font-size: 17px; line-height: 1.28; }
.lineRow.code .lineText {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 12px;
  line-height: 1.55;
  background: var(--code-bg);
  padding: 10px 12px;
  border-radius: 6px;
  overflow-x: auto;
}
.lineRow.selected.code .lineText { background: rgba(0,0,0,.25); color: #fff; }

.empty {
  padding: 60px 20px;
  text-align: center;
  color: var(--muted-dark);
  font-size: 13.5px;
  line-height: 1.6;
}

/* Floating Selection Bar */
.selection {
  position: absolute;
  z-index: 40;
  left: 12px;
  right: 12px;
  bottom: calc(10px + var(--bottom));
  min-height: 52px;
  border-radius: 10px;
  background: var(--ink);
  color: #fff;
  display: none;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 8px;
  padding: 6px 8px 6px 14px;
  box-shadow: 0 12px 36px rgba(0,0,0,.2);
}
.selection.open { display: grid; }
.selCount { font-size: 11.5px; font-weight: 800; letter-spacing: .05em; font-family: ui-monospace, monospace; }
.selection button {
  height: 36px;
  padding: 0 12px;
  border-radius: 6px;
  background: #262930;
  color: #fff;
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.selection .primary { background: var(--blue); color: #fff; }

/* Continuous Reading Stack Sheet */
.stack {
  position: absolute;
  z-index: 70;
  inset: 0;
  background: var(--paper);
  transform: translateY(104%);
  transition: transform .24s cubic-bezier(.2,.8,.2,1);
  display: flex;
  flex-direction: column;
}
.stack.open { transform: translateY(0); }
.stackHead {
  height: calc(58px + var(--top));
  padding: var(--top) 16px 0;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 48px 1fr 48px;
  align-items: center;
  background: var(--paper);
}
.stackHead button { height: 42px; font-size: 18px; font-weight: 900; }
.stackHead div { text-align: center; font-size: 10.5px; font-weight: 850; color: var(--blue); letter-spacing: .08em; font-family: ui-monospace, monospace; }
.stackScroll {
  flex: 1;
  overflow-y: auto;
  padding: 16px 20px calc(24px + var(--bottom));
  max-width: 800px;
  margin: 0 auto;
  width: 100%;
}
.stackItem {
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
}
.stackMeta {
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 9px;
  color: var(--blue);
  font-weight: 800;
  letter-spacing: .08em;
  margin-bottom: 6px;
  text-transform: uppercase;
}
.stackText {
  font-family: "Source Serif 4", ui-serif, Georgia, serif;
  font-size: 18.5px;
  line-height: 1.55;
  white-space: pre-wrap;
}

/* =========================================================
   2. RELATE MODE: 3D SLIPCASE FIELD (THREE.JS ENGINE)
   ========================================================= */
.three-pane-wrap {
  width: 100%;
  height: 100%;
  position: relative;
  background: #FFFFFF;
}
#threeCanvas {
  width: 100%;
  height: 100%;
  display: block;
}
.three-hud {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(255,255,255,.94);
  backdrop-filter: blur(10px);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 4px 16px rgba(0,0,0,.04);
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 10px;
  pointer-events: none;
  z-index: 10;
}
.three-hud-title {
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
  margin-bottom: 3px;
}
.three-hud-meta {
  color: var(--muted-dark);
}
.three-controls {
  position: absolute;
  top: 14px;
  right: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  z-index: 10;
}
.three-btn {
  height: 32px;
  padding: 0 10px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 6px;
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--ink);
  box-shadow: 0 2px 8px rgba(0,0,0,.03);
}
.three-btn.active {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}

.three-inspector-panel {
  position: absolute;
  bottom: 14px;
  left: 14px;
  right: 14px;
  max-width: 480px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 14px 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,.1);
  display: none;
  z-index: 20;
}
.three-inspector-panel.open { display: block; }

/* =========================================================
   3. RELATE MODE: MASSIVE RELATIONAL GRAPH (CANVAS)
   ========================================================= */
.graph-pane-wrap {
  width: 100%;
  height: 100%;
  position: relative;
  background: #FAFAFC;
}
#graphCanvas {
  width: 100%;
  height: 100%;
  display: block;
}
.graph-hud {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(255,255,255,.94);
  backdrop-filter: blur(10px);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 4px 16px rgba(0,0,0,.04);
  font-family: ui-monospace, SFMono-Regular, monospace;
  font-size: 10px;
  pointer-events: none;
  z-index: 10;
}
.graph-hud-title {
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
  margin-bottom: 4px;
}
.graph-hud-meta {
  color: var(--muted-dark);
}
.graph-controls {
  position: absolute;
  top: 12px;
  right: 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  z-index: 10;
}
.graph-btn {
  height: 32px;
  padding: 0 10px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 6px;
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--ink);
  box-shadow: 0 2px 8px rgba(0,0,0,.03);
}
.graph-btn.active {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}

.graph-inspector-panel {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  max-width: 480px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 14px 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,.1);
  display: none;
  z-index: 20;
}
.graph-inspector-panel.open { display: block; }
.graph-insp-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}
.graph-insp-accession {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 850;
  color: var(--blue);
}
.graph-insp-title {
  font-size: 15px;
  font-weight: 850;
  line-height: 1.25;
  margin-bottom: 8px;
}
.graph-insp-desc {
  font-size: 12px;
  color: var(--muted-dark);
  line-height: 1.4;
  margin-bottom: 10px;
}
.graph-insp-actions {
  display: flex;
  gap: 6px;
}

/* =========================================================
   4. RELATE MODE: NESTED MATRIX ("CASES OF CASES")
   ========================================================= */
.matrix-wrap {
  max-width: 860px;
  margin: 0 auto;
  padding: 16px 16px calc(28px + var(--bottom));
}
.matrix-intro {
  background: var(--paper);
  border: 1px solid var(--line);
  border-left: 3px solid var(--blue);
  border-radius: 8px;
  padding: 14px 16px;
  margin-bottom: 16px;
}
.matrix-intro-k {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
  margin-bottom: 4px;
}
.matrix-intro-v {
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--ink);
}

.cluster-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 10px;
  margin-bottom: 12px;
  overflow: hidden;
}
.cluster-head {
  padding: 12px 16px;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
}
.cluster-title {
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--blue);
}
.cluster-meta {
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 800;
  color: var(--muted-dark);
}
.cluster-body {
  display: flex;
  flex-direction: column;
}
.matrix-case-row {
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 140px 1fr auto;
  gap: 12px;
  align-items: center;
  cursor: pointer;
  transition: background .12s ease;
}
.matrix-case-row:last-child { border-bottom: 0; }
.matrix-case-row:hover { background: var(--blue-soft); }
.matrix-case-accession {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 850;
  color: var(--blue);
}
.matrix-case-name {
  font-size: 13.5px;
  font-weight: 800;
}
.matrix-case-counts {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 800;
  color: var(--muted-dark);
  white-space: nowrap;
}

/* =========================================================
   5. FLIPPER MODE (TACTILE CARD DECK)
   ========================================================= */
.flipper-wrap {
  padding: 16px 16px calc(24px + var(--bottom));
  max-width: 760px;
  margin: 0 auto;
}
.deck-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 12px;
}
.deck-btn {
  height: 36px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--paper);
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.deck-btn:hover { background: var(--bg); }
.deck-counter {
  font-family: ui-monospace, monospace;
  font-size: 10.5px;
  font-weight: 850;
  color: var(--blue);
  letter-spacing: .06em;
}
.card-box {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 20px 18px;
  box-shadow: 0 4px 16px rgba(0,0,0,.02);
}
.card-meta-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--line);
}
.card-id-tag {
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--blue);
}
.card-type-tag {
  font-family: ui-monospace, monospace;
  font-size: 8.5px;
  font-weight: 850;
  color: var(--ink);
  background: var(--bg);
  border: 1px solid var(--line);
  padding: 2px 6px;
  border-radius: 4px;
}
.card-title-main {
  font-size: 21px;
  font-weight: 850;
  line-height: 1.25;
  letter-spacing: -.025em;
  margin-bottom: 8px;
}
.card-source-main {
  font-size: 12px;
  color: var(--muted-dark);
  line-height: 1.45;
  margin-bottom: 14px;
}
.card-question-box {
  background: var(--blue-soft);
  border-left: 3px solid var(--blue);
  padding: 12px 14px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 14px;
}
.card-question-label {
  font-family: ui-monospace, monospace;
  font-size: 8.5px;
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
  margin-bottom: 4px;
}
.card-question-text {
  font-size: 16.5px;
  font-weight: 750;
  line-height: 1.35;
  letter-spacing: -.02em;
}
.card-passage-box {
  margin-bottom: 16px;
  font-family: "Source Serif 4", ui-serif, Georgia, serif;
  font-size: 17px;
  line-height: 1.55;
}
.card-fields-accordion {
  border-top: 1px solid var(--line);
  padding-top: 14px;
}
.card-field-row {
  margin-bottom: 12px;
}
.card-field-k {
  font-family: ui-monospace, monospace;
  font-size: 8.5px;
  font-weight: 900;
  color: var(--muted-dark);
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-bottom: 3px;
}
.card-field-v {
  font-size: 14px;
  line-height: 1.48;
}

/* =========================================================
   6. PDF LIBRARY MODE (RETURN)
   ========================================================= */
.pdf-wrap {
  padding: 16px 16px calc(24px + var(--bottom));
  max-width: 860px;
  margin: 0 auto;
}
.pdf-filter-bar {
  display: flex;
  gap: 6px;
  margin-bottom: 14px;
  overflow-x: auto;
  scrollbar-width: none;
}
.pdf-filter-bar::-webkit-scrollbar { display: none; }
.pdf-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}
.pdf-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdf-card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}
.pdf-title {
  font-size: 15px;
  font-weight: 800;
  line-height: 1.28;
  letter-spacing: -.02em;
}
.pdf-case {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 850;
  color: var(--blue);
  margin-top: 4px;
  text-transform: uppercase;
}
.pdf-tag {
  font-family: ui-monospace, monospace;
  font-size: 8.5px;
  font-weight: 900;
  letter-spacing: .06em;
  padding: 3px 6px;
  border-radius: 4px;
  white-space: nowrap;
  text-transform: uppercase;
}
.tag-paper { background: var(--blue-soft); color: var(--blue); }
.tag-scan { background: var(--bg); color: var(--muted-dark); border: 1px solid var(--line); }

.pdf-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 10px;
  border-top: 1px solid var(--line);
}
.pdf-size {
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 800;
  color: var(--muted-dark);
}
.pdf-btn-group {
  display: flex;
  gap: 6px;
}
.pdf-btn {
  height: 32px;
  padding: 0 12px;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: var(--bg);
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  display: inline-flex;
  align-items: center;
  text-decoration: none;
}
.pdf-btn.primary {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}

/* PDF READER MODAL */
.pdf-modal {
  position: absolute;
  z-index: 90;
  inset: 0;
  background: var(--paper);
  transform: translateY(104%);
  transition: transform .24s cubic-bezier(.2,.8,.2,1);
  display: flex;
  flex-direction: column;
}
.pdf-modal.open { transform: translateY(0); }
.pdf-modal-head {
  height: calc(58px + var(--top));
  padding: var(--top) 16px 0;
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  background: var(--paper);
}
.pdf-modal-title {
  font-size: 13px;
  font-weight: 850;
  max-width: 50%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.pdf-frame-wrap {
  flex: 1;
  position: relative;
  background: #525659;
}
.pdf-frame {
  width: 100%;
  height: 100%;
  border: 0;
}
.pdf-fallback-note {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 14px;
  font-size: 11px;
  color: var(--muted-dark);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

/* =========================================================
   7. MAPS & STRUCTURAL DOCS MODE (PRESERVE)
   ========================================================= */
.maps-wrap {
  padding: 16px 16px calc(24px + var(--bottom));
  max-width: 860px;
  margin: 0 auto;
}
.maps-tabs {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  margin-bottom: 12px;
  scrollbar-width: none;
}
.maps-tabs::-webkit-scrollbar { display: none; }
.map-tab-btn {
  flex: 0 0 auto;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--paper);
  padding: 6px 10px;
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted-dark);
  text-transform: uppercase;
}
.map-tab-btn.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.doc-box {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px 16px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 12.5px;
  line-height: 1.6;
  white-space: pre-wrap;
  overflow-x: auto;
}
.doc-action-bar {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  margin-top: 10px;
}

/* =========================================================
   8. PROMPT OPERATOR MODE (RETURN - COOL RADIO)
   ========================================================= */
.prompts-wrap {
  padding: 16px 16px calc(24px + var(--bottom));
  max-width: 780px;
  margin: 0 auto;
}
.poml-stepper {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  margin-bottom: 14px;
  scrollbar-width: none;
}
.poml-stepper::-webkit-scrollbar { display: none; }
.poml-step-btn {
  flex: 0 0 auto;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--paper);
  padding: 6px 10px;
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted-dark);
}
.poml-step-btn.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.poml-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 20px 18px;
  margin-bottom: 14px;
}
.poml-head-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}
.poml-num {
  font-family: ui-monospace, monospace;
  font-size: 10px;
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
}
.poml-ver {
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 850;
  color: var(--muted-dark);
}
.poml-title {
  font-size: 20px;
  font-weight: 850;
  line-height: 1.2;
  margin-bottom: 4px;
}
.poml-sub {
  font-size: 12px;
  color: var(--muted-dark);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: .06em;
  font-weight: 750;
}
.poml-say-box {
  background: var(--blue-soft);
  border-left: 3px solid var(--blue);
  padding: 10px 12px;
  border-radius: 0 6px 6px 0;
  margin-bottom: 12px;
  font-size: 13px;
  font-weight: 750;
  color: var(--blue);
}
.poml-desc {
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--ink);
  margin-bottom: 14px;
}
.poml-contract-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 14px;
}
.poml-contract-col {
  background: var(--bg);
  padding: 8px 10px;
  border-radius: 6px;
}
.poml-contract-k {
  font-family: ui-monospace, monospace;
  font-size: 8px;
  font-weight: 900;
  color: var(--muted-dark);
  letter-spacing: .08em;
  margin-bottom: 2px;
}
.poml-contract-v {
  font-size: 11px;
  line-height: 1.4;
}
.poml-actions-bar {
  display: flex;
  gap: 8px;
}
.poml-btn {
  height: 36px;
  padding: 0 14px;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: var(--paper);
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.poml-btn.primary {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.poml-code-box {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 11.5px;
  line-height: 1.6;
  white-space: pre-wrap;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
  max-height: 480px;
  overflow-y: auto;
}

/* Modals & Scrims */
.scrim {
  position: absolute;
  z-index: 80;
  inset: 0;
  background: rgba(17,19,24,.3);
  display: none;
}
.scrim.open { display: block; }
.sheet {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: calc(12px + var(--bottom));
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 14px;
  box-shadow: 0 18px 60px rgba(0,0,0,.16);
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.sheetTitle {
  padding: 4px 6px 12px;
  font-family: ui-monospace, monospace;
  font-size: 10px;
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
  text-transform: uppercase;
}
.sheetScroll {
  overflow-y: auto;
  flex: 1;
}
.sheetGrid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px;
}
.sheetGrid button {
  min-height: 42px;
  border-radius: 6px;
  background: var(--bg);
  font-family: ui-monospace, monospace;
  font-size: 9.5px;
  font-weight: 800;
  padding: 6px 8px;
  text-align: center;
  border: 1px solid var(--line);
}
.sheetGrid button.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}

.caseList {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.caseRowBtn {
  padding: 10px 12px;
  border-radius: 6px;
  background: var(--bg);
  border: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-align: left;
}
.caseRowBtn.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.caseRowBtn.on .caseRowMeta, .caseRowBtn.on .caseRowAccession {
  color: var(--blue-soft);
}
.caseRowAccession {
  font-family: ui-monospace, monospace;
  font-size: 8.5px;
  font-weight: 850;
  color: var(--blue);
}
.caseRowTitle {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: -.01em;
  margin-top: 1px;
}
.caseRowMeta {
  font-family: ui-monospace, monospace;
  font-size: 9px;
  font-weight: 800;
  color: var(--muted-dark);
  white-space: nowrap;
}

/* Toast */
.toast {
  position: absolute;
  z-index: 100;
  left: 50%;
  bottom: calc(76px + var(--bottom));
  transform: translateX(-50%);
  background: var(--ink);
  color: #fff;
  border-radius: 999px;
  padding: 8px 16px;
  font-size: 11px;
  font-weight: 750;
  display: none;
  white-space: nowrap;
  box-shadow: 0 6px 20px rgba(0,0,0,.2);
}
.toast.open { display: block; }

/* Responsive adjustments */
@media(min-width: 760px) {
  header, .methodology-bar, .subtoolbar, main {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: min(880px, 100%);
  }
  .selection {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: 560px;
  }
  .sheet {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: 620px;
  }
  .lineRow {
    grid-template-columns: 140px 1fr;
    padding-left: 20px;
    padding-right: 20px;
  }
  .zhead {
    padding-left: 20px;
    padding-right: 20px;
  }
  .pdf-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three/examples/jsm/"
  }
}
</script>
</head>
<body>
<div id="app">

  <!-- Master Header -->
  <header>
    <div class="brand-group" id="brandBtn">
      <svg class="brand-logo-svg" viewBox="0 0 24 24">
        <rect x="2" y="5" width="20" height="15" rx="2"></rect>
        <path d="M4 5V3a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"></path>
        <line x1="7" y1="10" x2="17" y2="10"></line>
        <line x1="7" y1="14" x2="13" y2="14"></line>
      </svg>
      <div class="brand-text-col">
        <div class="brand-wordmark">SLIPCASE</div>
        <div class="brand-subtitle">PORTABLE RESEARCH FIELD</div>
      </div>
    </div>

    <div class="search-wrap">
      <input id="search" class="search" placeholder="Search 1,244 zettels, 124 PDFs, 5,083 relations" autocomplete="off">
      <span class="search-shortcut">/</span>
    </div>

    <button id="caseNavBtn" class="accession-badge-btn">ALL CASES (31)</button>
  </header>

  <!-- Master Methodology Navigation (PRESERVE · RELATE · RETURN) -->
  <div class="methodology-bar" id="methodologyBar">
    <div class="nav-triad-group">
      <span class="nav-pillar-label">PRESERVE</span>
      <button class="nav-tab-btn on" data-tab="lines">LINES</button>
      <button class="nav-tab-btn" data-tab="flipper">FLIPPER</button>
      <button class="nav-tab-btn" data-tab="maps">MAPS</button>
    </div>

    <div class="nav-divider"></div>

    <div class="nav-triad-group">
      <span class="nav-pillar-label">RELATE</span>
      <button class="nav-tab-btn" data-tab="three">3D FIELD</button>
      <button class="nav-tab-btn" data-tab="graph">MASSIVE GRAPH</button>
      <button class="nav-tab-btn" data-tab="matrix">NESTED MATRIX</button>
    </div>

    <div class="nav-divider"></div>

    <div class="nav-triad-group">
      <span class="nav-pillar-label">RETURN</span>
      <button class="nav-tab-btn" data-tab="pdfs" id="pdfTabBtn">PDFS (124)</button>
      <button class="nav-tab-btn" data-tab="prompts">PROMPTS</button>
    </div>
  </div>

  <!-- Secondary Field Filters Bar for LINES mode -->
  <div class="subtoolbar" id="linesSubtoolbar">
    <button class="subchip on" data-filter="ALL">ALL</button>
    <button class="subchip" data-filter="QUESTION">QUESTIONS</button>
    <button class="subchip" data-filter="PASSAGE">PASSAGES</button>
    <button class="subchip" data-filter="RESEARCH OBJECT">OBJECTS</button>
    <button class="subchip" data-filter="MECHANISM">MECHANISMS</button>
    <button class="subchip" data-filter="FORMAL SHIFT">FORMALISMS</button>
    <button class="subchip" data-filter="TYPE">TYPES</button>
    <button class="subchip" data-filter="SOURCE">SOURCES</button>
    <button class="subchip" id="moreFiltersBtn">FIELD FILTER...</button>
  </div>

  <!-- Main Viewport -->
  <main id="mainViewport">
    
    <!-- 1. LINES PANE (PRESERVE) -->
    <div class="pane active" id="pane-lines">
      <div class="lines-container">
        <div id="table"></div>
      </div>
    </div>

    <!-- 2. FLIPPER PANE (PRESERVE) -->
    <div class="pane" id="pane-flipper">
      <div class="flipper-wrap">
        <div class="deck-controls">
          <button class="deck-btn" id="prevCardBtn">&larr; PREV</button>
          <div class="deck-counter" id="deckCounter">CARD 1 OF 1244</div>
          <button class="deck-btn" id="nextCardBtn">NEXT &rarr;</button>
        </div>
        <div class="deck-controls" style="margin-top:-4px;">
          <button class="deck-btn" id="toggleRawBtn">RAW TEXT</button>
          <button class="deck-btn" id="copyCardBtn">COPY CARD &orarr;</button>
          <button class="deck-btn" id="downloadCardBtn">DOWNLOAD .TXT &darr;</button>
        </div>
        <div id="cardBoxContainer" style="margin-top:10px;"></div>
      </div>
    </div>

    <!-- 3. MAPS PANE (PRESERVE) -->
    <div class="pane" id="pane-maps">
      <div class="maps-wrap">
        <div class="maps-tabs" id="mapsTabs"></div>
        <div class="doc-box" id="mapDocContent"></div>
        <div class="doc-action-bar">
          <button class="deck-btn" id="copyDocBtn">COPY DOCUMENT &orarr;</button>
          <button class="deck-btn" id="downloadDocBtn">DOWNLOAD .TXT &darr;</button>
        </div>
      </div>
    </div>

    <!-- 4. 3D SLIPCASE FIELD PANE (RELATE - THREE.JS) -->
    <div class="pane" id="pane-three">
      <div class="three-pane-wrap">
        <div class="three-hud">
          <div class="three-hud-title">3D ORTHOGRAPHIC RESEARCH FIELD</div>
          <div class="three-hud-meta" id="threeHudMeta">31 SLIPCASE BOXES &middot; STEPPED SLIPS &middot; CLICK TO INSPECT</div>
        </div>

        <div class="three-controls">
          <button class="three-btn active" id="threeViewAllBtn" onclick="setThreeViewMode('all')">ALL 31 CASES</button>
          <button class="three-btn" id="threeViewFocusBtn" onclick="setThreeViewMode('focus')">ACTIVE CASE</button>
          <button class="three-btn" onclick="resetThreeCamera()">RESET ANGLE</button>
        </div>

        <div id="threeContainer" style="width:100%;height:100%;"></div>

        <div class="three-inspector-panel" id="threeInspectorPanel">
          <div class="graph-insp-head">
            <span class="graph-insp-accession" id="threeInspAccession">SLP / FIELD</span>
            <button onclick="closeThreeInspector()" style="font-size:12px;font-weight:900;">&times;</button>
          </div>
          <div class="graph-insp-title" id="threeInspTitle">Slipcase Title</div>
          <div class="graph-insp-desc" id="threeInspDesc">Contains cards and documents.</div>
          <div class="graph-insp-actions">
            <button class="deck-btn" id="threeInspLinesBtn">OPEN ZETTEL LINES &rarr;</button>
            <button class="deck-btn" id="threeInspFlipperBtn">OPEN CARD DECK &rarr;</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 5. MASSIVE GRAPH PANE (RELATE) -->
    <div class="pane" id="pane-graph">
      <div class="graph-pane-wrap">
        <div class="graph-hud">
          <div class="graph-hud-title">RELATIONAL FIELD GRAPH</div>
          <div class="graph-hud-meta" id="graphHudMeta">31 CASES &middot; 1,244 SLIPS &middot; 5,083 CROSS-LINKS</div>
        </div>

        <div class="graph-controls">
          <button class="graph-btn active" id="graphModeAllBtn" onclick="setGraphMode('all')">ALL SLIPS &amp; CASES</button>
          <button class="graph-btn" id="graphModeCasesBtn" onclick="setGraphMode('cases')">CASES OF CASES</button>
          <button class="graph-btn" id="graphModeBridgesBtn" onclick="setGraphMode('bridges')">CROSS-CASE BRIDGES</button>
          <button class="graph-btn" onclick="resetGraphView()">RESET VIEW</button>
        </div>

        <canvas id="graphCanvas"></canvas>

        <div class="graph-inspector-panel" id="graphInspectorPanel">
          <div class="graph-insp-head">
            <span class="graph-insp-accession" id="graphInspAccession">SLP / FIELD</span>
            <button onclick="closeGraphInspector()" style="font-size:12px;font-weight:900;">&times;</button>
          </div>
          <div class="graph-insp-title" id="graphInspTitle">Title</div>
          <div class="graph-insp-desc" id="graphInspDesc">Details</div>
          <div class="graph-insp-actions">
            <button class="deck-btn" id="graphInspOpenBtn">INSPECT IN LINES &rarr;</button>
            <button class="deck-btn" id="graphInspFlipperBtn">OPEN IN FLIPPER &rarr;</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. NESTED MATRIX PANE (RELATE) -->
    <div class="pane" id="pane-matrix">
      <div class="matrix-wrap">
        <div class="matrix-intro">
          <div class="matrix-intro-k">CASES OF CASES &middot; SLIPS OF SLIPS &middot; RELATIONAL MATRIX</div>
          <div class="matrix-intro-v">Multi-tiered archival taxonomy organizing 31 field slipcases into 5 meta-research clusters, exposing 5,083 cross-citations and 124 primary source documents.</div>
        </div>
        <div id="matrixClusterContainer"></div>
      </div>
    </div>

    <!-- 7. PDF LIBRARY PANE (RETURN) -->
    <div class="pane" id="pane-pdfs">
      <div class="pdf-wrap">
        <div class="pdf-filter-bar">
          <button class="subchip on" data-pdf-cat="ALL" id="pdfCatAll">ALL (124)</button>
          <button class="subchip" data-pdf-cat="PAPERS" id="pdfCatPapers">PAPERS</button>
          <button class="subchip" data-pdf-cat="SCANS" id="pdfCatScans">SCANS &amp; RESOURCES</button>
        </div>
        <div class="pdf-grid" id="pdfGrid"></div>
      </div>
    </div>

    <!-- 8. PROMPT OPERATOR PANE (RETURN - COOL RADIO) -->
    <div class="pane" id="pane-prompts">
      <div class="prompts-wrap">
        <div class="poml-stepper" id="pomlStepper"></div>
        <div id="pomlCardContainer"></div>
        <div class="poml-code-box" id="pomlCodeBox"></div>
      </div>
    </div>

  </main>

  <!-- Floating Selection Bar -->
  <div class="selection" id="selection">
    <div class="selCount" id="selCount">0 selected</div>
    <button id="clearBtn">CLEAR</button>
    <button id="stackBtn" class="primary">READ STACK</button>
  </div>

  <!-- Stack Modal (Continuous Line Reading) -->
  <section class="stack" id="stack">
    <div class="stackHead">
      <button id="stackBack">&larr;</button>
      <div id="stackCount">SELECTED LINES</div>
      <button id="copyBtn">&#x29c9;</button>
    </div>
    <div class="stackScroll" id="stackScroll"></div>
  </section>

  <!-- PDF Reader Modal -->
  <section class="pdf-modal" id="pdfModal">
    <div class="pdf-modal-head">
      <button class="deck-btn" id="closePdfModalBtn">&larr; CLOSE</button>
      <div class="pdf-modal-title" id="pdfModalTitle">DOCUMENT</div>
      <div style="display:flex;gap:6px;">
        <a class="deck-btn" id="pdfModalExtBtn" target="_blank">OPEN TAB &nearr;</a>
        <a class="deck-btn" id="pdfModalDlBtn" download>DOWNLOAD &darr;</a>
      </div>
    </div>
    <div class="pdf-frame-wrap">
      <object id="pdfObject" class="pdf-frame" type="application/pdf" data="">
        <iframe id="pdfIframe" class="pdf-frame" src="about:blank"></iframe>
      </object>
      <div class="pdf-fallback-note">
        <span>If inline PDF viewing is blocked by your browser's local sandbox, open directly in a new tab:</span>
        <a class="deck-btn" id="pdfFallbackBtn" target="_blank" style="flex:0 0 auto;">OPEN DIRECTLY &nearr;</a>
      </div>
    </div>
  </section>

  <!-- Filter Modal Sheet -->
  <div class="scrim" id="filterScrim">
    <div class="sheet">
      <div class="sheetTitle">SELECT FIELD FILTER</div>
      <div class="sheetScroll">
        <div class="sheetGrid" id="sheetGrid"></div>
      </div>
    </div>
  </div>

  <!-- Case Switcher Sheet -->
  <div class="scrim" id="caseScrim">
    <div class="sheet">
      <div class="sheetTitle">SELECT FIELD SLIPCASE</div>
      <div class="sheetScroll">
        <div class="caseList" id="caseList"></div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast" id="toast"></div>

</div>

<!-- Primary Application Logic -->
<script>
/* Embedded Research Data */
const CASES = /* DATA_CASES */;
const ALL_NOTES = /* DATA_NOTES */;
const ALL_PDFS = /* DATA_PDFS */;
const GRAPH = /* DATA_GRAPH */;
const PROMPTS = /* DATA_PROMPTS */;

const MAIN_FIELDS = [
  "TITLE","QUESTION","DEEPER QUESTION","PASSAGE","RESEARCH OBJECT","LOCAL MOVE",
  "SOURCE TERMS","WHAT BECAME STRANGE","MECHANISM","FORMAL SHIFT","SOURCE FORMALISM",
  "OUR FORMALIZATION","TENSION","MISSING","BOUNDARY","CITATION TRAIL","TEST",
  "PLATFORM","LINKS","BIBTEX","SOURCE"
];

/* State Variables */
let currentTab = "lines";
let selectedCaseIdx = -1; // -1 means ALL CASES
let lineFilter = "ALL";
let pdfCategory = "ALL";
let currentCardIdx = 0;
let currentPromptIdx = 0;
let rawCardMode = false;
let currentActiveDocKey = "";
let selectedLines = new Set();
let toastTimer = null;

/* DOM Helpers */
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s ?? "").replace(/[&<>"']/g, m => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));

function getActiveNotes() {
  if (selectedCaseIdx === -1) return ALL_NOTES;
  return CASES[selectedCaseIdx]?.cards || [];
}

function getActivePdfs() {
  if (selectedCaseIdx === -1) return ALL_PDFS;
  return CASES[selectedCaseIdx]?.pdfs || [];
}

/* =========================================================
   1. NAVIGATION & METHODOLOGY TRIAD SWITCHING
   ========================================================= */
function setTab(tab) {
  currentTab = tab;
  $$(".nav-tab-btn").forEach(b => b.classList.toggle("on", b.dataset.tab === tab));
  $$(".pane").forEach(p => p.classList.remove("active"));
  const targetPane = $(`#pane-${tab}`);
  if (targetPane) targetPane.classList.add("active");
  
  const subtoolbar = $("#linesSubtoolbar");
  const mainVp = $("#mainViewport");
  if (tab === "lines") {
    subtoolbar.style.display = "flex";
    mainVp.classList.remove("top-short");
    renderLines();
  } else {
    subtoolbar.style.display = "none";
    mainVp.classList.add("top-short");
  }

  if (tab === "flipper") renderFlipper();
  if (tab === "maps") renderMaps();
  if (tab === "three") window.triggerThreeResize?.();
  if (tab === "graph") initGraphEngine();
  if (tab === "matrix") renderMatrix();
  if (tab === "pdfs") renderPdfs();
  if (tab === "prompts") renderPrompts();
  window.scrollTo(0,0);
}

$$(".nav-tab-btn").forEach(b => {
  b.onclick = () => setTab(b.dataset.tab);
});

$("#brandBtn").onclick = () => {
  selectedCaseIdx = -1;
  updateActiveCaseLabel();
  setTab("lines");
};

/* =========================================================
   2. CASE SWITCHER
   ========================================================= */
function updateActiveCaseLabel() {
  if (selectedCaseIdx === -1) {
    $("#caseNavBtn").textContent = "ALL CASES (31)";
    $("#pdfTabBtn").textContent = `PDFS (${ALL_PDFS.length})`;
  } else {
    const c = CASES[selectedCaseIdx];
    const shortAcc = c.accession || `CASE ${selectedCaseIdx + 1}`;
    $("#caseNavBtn").textContent = shortAcc;
    $("#pdfTabBtn").textContent = `PDFS (${c.pdfs.length})`;
  }
}

function openCaseModal() {
  let html = `
    <div class="caseRowBtn ${selectedCaseIdx === -1 ? 'on' : ''}" onclick="selectCase(-1)">
      <div>
        <div class="caseRowAccession">GLOBAL REPOSITORY</div>
        <div class="caseRowTitle">ALL 31 FIELD SLIPCASES</div>
      </div>
      <div class="caseRowMeta">${ALL_NOTES.length} SLIPS &middot; ${ALL_PDFS.length} PDFS</div>
    </div>
  `;

  CASES.forEach((c, idx) => {
    html += `
      <div class="caseRowBtn ${selectedCaseIdx === idx ? 'on' : ''}" onclick="selectCase(${idx})">
        <div>
          <div class="caseRowAccession">${esc(c.accession)} &middot; ${esc(c.meta_field)}</div>
          <div class="caseRowTitle">${esc(c.name)}</div>
        </div>
        <div class="caseRowMeta">${c.card_count} SLIPS &middot; ${c.pdf_count} PDFS</div>
      </div>
    `;
  });

  $("#caseList").innerHTML = html;
  $("#caseScrim").classList.add("open");
}

window.selectCase = function(idx) {
  selectedCaseIdx = idx;
  currentCardIdx = 0;
  updateActiveCaseLabel();
  $("#caseScrim").classList.remove("open");
  if (currentTab === "lines") renderLines();
  if (currentTab === "flipper") renderFlipper();
  if (currentTab === "maps") renderMaps();
  if (currentTab === "three") window.updateThreeFocus?.(idx);
  if (currentTab === "graph") initGraphEngine();
  if (currentTab === "matrix") renderMatrix();
  if (currentTab === "pdfs") renderPdfs();
  toast(idx === -1 ? "Showing All 31 Slipcases" : `Switched to ${CASES[idx].accession}`);
};

$("#caseNavBtn").onclick = openCaseModal;
$("#caseScrim").addEventListener("pointerdown", e => {
  if (e.target === $("#caseScrim")) $("#caseScrim").classList.remove("open");
});

/* =========================================================
   3. LINES MODULE (ZETTEL LINES INSPECTOR)
   ========================================================= */
function rowKey(id, field) { return id + "|||" + field; }
function unpack(key) { const i = key.indexOf("|||"); return [key.slice(0,i), key.slice(i+3)]; }

function valueFor(n, field) {
  if (field === "TITLE") return n.title;
  if (field === "SOURCE") return n.source;
  if (field === "PASSAGE") return n.passage;
  if (field === "TYPE") return n.type;
  if (field === "QUESTION" && n.fields["QUESTION"]) return n.fields["QUESTION"];
  return n.fields[field] ?? "";
}

function fieldsFor(n) {
  if (lineFilter === "ALL") return MAIN_FIELDS.filter(f => valueFor(n, f));
  if (lineFilter === "TYPE") return ["TYPE"];
  return valueFor(n, lineFilter) ? [lineFilter] : [];
}

function lineMatches(n, field, q) {
  if (!q) return true;
  const hay = [n.id, n.type, n.topic, n.case_name, field, valueFor(n, field)].join(" ").toLowerCase();
  return q.split(/\s+/).every(t => hay.includes(t));
}

function renderLines() {
  const notes = getActiveNotes();
  const q = $("#search").value.trim().toLowerCase();
  let html = "";
  let matchedCount = 0;

  notes.forEach(n => {
    const fields = fieldsFor(n).filter(f => lineMatches(n, f, q));
    if (!fields.length) return;
    matchedCount++;
    html += `
      <section class="zgroup" data-zettel="${esc(n.id)}">
        <div class="zhead" onclick="selectWholeZettel('${esc(n.id)}')">
          <div>
            <div class="zid">${esc(n.id)} &middot; ${esc(n.topic)}</div>
            <div class="ztitle">${esc(n.title)}</div>
          </div>
          <div class="ztype">${esc(n.type)}</div>
        </div>
    `;
    fields.forEach(field => {
      const key = rowKey(n.id, field);
      const v = valueFor(n, field);
      const code = /FORMAL|BIBTEX|MECHANISM/.test(field);
      html += `
        <article class="lineRow ${selectedLines.has(key) ? 'selected' : ''} ${code ? 'code' : ''}" data-key="${esc(key)}" data-field="${esc(field)}">
          <div class="fieldName">${esc(field)}</div>
          <div class="lineText">${esc(v)}</div>
        </article>
      `;
    });
    html += `</section>`;
  });

  $("#table").innerHTML = html || `<div class="empty">No zettels or lines matched your query.</div>`;
  bindLineRows();
  updateSelectionUI();
}

function bindLineRows() {
  $$(".lineRow").forEach(row => {
    let timer = null, start = null, moved = false;
    row.addEventListener("pointerdown", e => {
      start = { x: e.clientX, y: e.clientY };
      moved = false;
      timer = setTimeout(() => {
        if (!moved) {
          const [id] = unpack(row.dataset.key);
          selectWholeZettel(id);
          navigator.vibrate?.(12);
        }
      }, 470);
    });
    row.addEventListener("pointermove", e => {
      if (start && Math.hypot(e.clientX - start.x, e.clientY - start.y) > 8) {
        moved = true;
        clearTimeout(timer);
      }
    });
    row.addEventListener("pointerup", () => {
      clearTimeout(timer);
      if (!moved) toggleLine(row.dataset.key);
    });
    row.addEventListener("contextmenu", e => {
      e.preventDefault();
      const [id] = unpack(row.dataset.key);
      selectWholeZettel(id);
    });
  });
}

function toggleLine(key) {
  if (selectedLines.has(key)) {
    selectedLines.delete(key);
  } else {
    selectedLines.add(key);
  }
  const el = $(`.lineRow[data-key="${CSS.escape(key)}"]`);
  if (el) el.classList.toggle("selected", selectedLines.has(key));
  updateSelectionUI();
}

window.selectWholeZettel = function(id) {
  const notes = getActiveNotes();
  const n = notes.find(x => x.id === id);
  if (!n) return;
  const keys = MAIN_FIELDS.filter(f => valueFor(n, f)).map(f => rowKey(id, f));
  const all = keys.every(k => selectedLines.has(k));
  keys.forEach(k => all ? selectedLines.delete(k) : selectedLines.add(k));
  renderLines();
  toast(all ? "Zettel lines cleared" : "Whole Zettel selected");
};

function updateSelectionUI() {
  $("#selCount").textContent = `${selectedLines.size} selected`;
  $("#selection").classList.toggle("open", selectedLines.size > 0);
}

function clearSelected() {
  selectedLines.clear();
  renderLines();
  toast("Selection cleared");
}

function getSelectedItems() {
  const items = [];
  const notes = ALL_NOTES;
  notes.forEach(n => {
    MAIN_FIELDS.forEach(field => {
      const key = rowKey(n.id, field);
      if (selectedLines.has(key) && valueFor(n, field)) {
        items.push({ n, field, text: valueFor(n, field) });
      }
    });
  });
  return items;
}

function openStack() {
  const items = getSelectedItems();
  $("#stackCount").textContent = `${items.length} LINES`;
  $("#stackScroll").innerHTML = items.map(x => `
    <article class="stackItem" data-field="${esc(x.field)}">
      <div class="stackMeta">${esc(x.n.id)} &middot; ${esc(x.field)} &middot; ${esc(x.n.type)} &middot; ${esc(x.n.case_name)}</div>
      <div class="stackText">${esc(x.text)}</div>
    </article>
  `).join("");
  $("#stack").classList.add("open");
}

function closeStack() {
  $("#stack").classList.remove("open");
}

async function copySelectedLines() {
  const items = getSelectedItems();
  const text = items.map(x => `${x.n.id} [${x.field}]\n${x.text}`).join("\n\n---\n\n");
  try {
    await navigator.clipboard.writeText(text);
    toast("Selected lines copied to clipboard");
  } catch(e) {
    toast("Clipboard copy failed");
  }
}

function setLineFilter(f) {
  lineFilter = f;
  $$("#linesSubtoolbar .subchip").forEach(b => b.classList.toggle("on", b.dataset.filter === f));
  $("#filterScrim").classList.remove("open");
  renderLines();
}

function openFilterSheet() {
  const opts = [
    "ALL", "QUESTION", "DEEPER QUESTION", "PASSAGE", "RESEARCH OBJECT", 
    "LOCAL MOVE", "WHAT BECAME STRANGE", "MECHANISM", "FORMAL SHIFT", 
    "SOURCE FORMALISM", "OUR FORMALIZATION", "TENSION", "MISSING", 
    "BOUNDARY", "TEST", "CITATION TRAIL", "PLATFORM", "LINKS", "BIBTEX", "TYPE", "SOURCE"
  ];
  $("#sheetGrid").innerHTML = opts.map(f => `
    <button class="${lineFilter === f ? 'on' : ''}" onclick="setLineFilter('${esc(f)}')">${esc(f)}</button>
  `).join("");
  $("#filterScrim").classList.add("open");
}

window.setLineFilter = setLineFilter;
$$("#linesSubtoolbar .subchip[data-filter]").forEach(b => {
  b.onclick = () => setLineFilter(b.dataset.filter);
});
$("#moreFiltersBtn").onclick = openFilterSheet;
$("#filterScrim").addEventListener("pointerdown", e => {
  if (e.target === $("#filterScrim")) $("#filterScrim").classList.remove("open");
});

$("#clearBtn").onclick = clearSelected;
$("#stackBtn").onclick = openStack;
$("#stackBack").onclick = closeStack;
$("#copyBtn").onclick = copySelectedLines;

/* =========================================================
   4. RELATE MODULE: MASSIVE GRAPH ENGINE (HTML5 CANVAS)
   ========================================================= */
let graphMode = "all";
let graphAnimId = null;
let graphNodes = [];
let graphLinks = [];
let transform = { x: 0, y: 0, k: 1 };
let isDraggingGraph = false;
let dragStart = { x: 0, y: 0 };
let hoveredNode = null;
let selectedNode = null;

function initGraphEngine() {
  const canvas = $("#graphCanvas");
  const container = $(".graph-pane-wrap");
  if (!canvas || !container) return;

  const dpr = window.devicePixelRatio || 1;
  const w = container.clientWidth || 800;
  const h = container.clientHeight || 600;
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  canvas.style.width = w + "px";
  canvas.style.height = h + "px";

  buildGraphTopology(w, h);
  
  if (graphAnimId) cancelAnimationFrame(graphAnimId);
  runGraphPhysics();
  bindGraphEvents(canvas);
}

function buildGraphTopology(w, h) {
  const cx = w / 2;
  const cy = h / 2;
  
  const caseNodeMap = {};
  graphNodes = [];
  graphLinks = [];

  const rawCaseNodes = GRAPH.nodes.filter(n => n.type === 'case');
  const rawSlipNodes = GRAPH.nodes.filter(n => n.type === 'slip');

  rawCaseNodes.forEach((cn, i) => {
    const angle = (i / rawCaseNodes.length) * 2 * Math.PI;
    const radius = Math.min(w, h) * 0.38;
    const node = {
      ...cn,
      x: cx + Math.cos(angle) * radius + (Math.random() - 0.5) * 40,
      y: cy + Math.sin(angle) * radius + (Math.random() - 0.5) * 40,
      vx: 0,
      vy: 0,
      radius: 16
    };
    graphNodes.push(node);
    caseNodeMap[cn.id] = node;
  });

  if (graphMode === "all" || graphMode === "bridges") {
    const visibleSlips = (selectedCaseIdx === -1) 
      ? rawSlipNodes 
      : rawSlipNodes.filter(s => s.case_idx === selectedCaseIdx);

    const slipNodeMap = {};
    visibleSlips.forEach((sn, i) => {
      const parentCase = caseNodeMap[`case_${sn.case_id}`];
      const pX = parentCase ? parentCase.x : cx;
      const pY = parentCase ? parentCase.y : cy;
      const angle = Math.random() * 2 * Math.PI;
      const dist = 30 + Math.random() * 70;
      const node = {
        ...sn,
        x: pX + Math.cos(angle) * dist,
        y: pY + Math.sin(angle) * dist,
        vx: 0,
        vy: 0,
        radius: 4.5
      };
      graphNodes.push(node);
      slipNodeMap[sn.id] = node;
    });

    GRAPH.links.forEach(l => {
      const sNode = (l.type === 'contains') ? caseNodeMap[l.source] : slipNodeMap[l.source];
      const tNode = (l.type === 'case_bridge') ? caseNodeMap[l.target] : slipNodeMap[l.target];
      if (sNode && tNode) {
        graphLinks.push({ source: sNode, target: tNode, type: l.type, w: l.w || 1 });
      }
    });
  } else if (graphMode === "cases") {
    GRAPH.links.filter(l => l.type === 'case_bridge').forEach(l => {
      const sNode = caseNodeMap[l.source];
      const tNode = caseNodeMap[l.target];
      if (sNode && tNode) {
        graphLinks.push({ source: sNode, target: tNode, type: 'case_bridge', w: l.w || 2, count: l.count || 1 });
      }
    });
  }

  $("#graphHudMeta").textContent = `${rawCaseNodes.length} CASES · ${graphNodes.filter(n=>n.type==='slip').length} SLIPS · ${graphLinks.length} ACTIVE EDGES`;
}

function runGraphPhysics() {
  const canvas = $("#graphCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const dpr = window.devicePixelRatio || 1;

  for (let i = 0; i < graphLinks.length; i++) {
    const l = graphLinks[i];
    const dx = l.target.x - l.source.x;
    const dy = l.target.y - l.source.y;
    const dist = Math.hypot(dx, dy) || 1;
    const targetDist = l.type === 'contains' ? 50 : l.type === 'case_bridge' ? 140 : 80;
    const force = (dist - targetDist) * 0.003;
    const fx = (dx / dist) * force;
    const fy = (dy / dist) * force;
    l.source.vx += fx;
    l.source.vy += fy;
    l.target.vx -= fx;
    l.target.vy -= fy;
  }

  for (let i = 0; i < graphNodes.length; i++) {
    const n1 = graphNodes[i];
    for (let j = i + 1; j < Math.min(graphNodes.length, i + 60); j++) {
      const n2 = graphNodes[j];
      const dx = n2.x - n1.x;
      const dy = n2.y - n1.y;
      const dist = Math.hypot(dx, dy) || 1;
      const minDist = n1.radius + n2.radius + 15;
      if (dist < minDist) {
        const force = (minDist - dist) * 0.04;
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;
        n1.vx -= fx;
        n1.vy -= fy;
        n2.vx += fx;
        n2.vy += fy;
      }
    }
    n1.x += n1.vx;
    n1.y += n1.vy;
    n1.vx *= 0.88;
    n1.vy *= 0.88;
  }

  ctx.save();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.scale(dpr, dpr);
  ctx.translate(transform.x, transform.y);
  ctx.scale(transform.k, transform.k);

  const q = $("#search").value.trim().toLowerCase();

  for (let i = 0; i < graphLinks.length; i++) {
    const l = graphLinks[i];
    ctx.beginPath();
    ctx.moveTo(l.source.x, l.source.y);
    ctx.lineTo(l.target.x, l.target.y);
    if (l.type === 'case_bridge') {
      ctx.strokeStyle = "rgba(6, 71, 229, 0.4)";
      ctx.lineWidth = Math.min(3, l.w);
    } else if (l.type === 'cross_cite') {
      ctx.strokeStyle = "rgba(6, 71, 229, 0.25)";
      ctx.lineWidth = 1;
    } else {
      ctx.strokeStyle = "rgba(229, 231, 235, 0.8)";
      ctx.lineWidth = 0.8;
    }
    ctx.stroke();
  }

  for (let i = 0; i < graphNodes.length; i++) {
    const n = graphNodes[i];
    const isMatched = !q || (n.label && n.label.toLowerCase().includes(q));
    const isSelected = selectedNode && selectedNode.id === n.id;
    const isHovered = hoveredNode && hoveredNode.id === n.id;

    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius * (isSelected ? 1.4 : isHovered ? 1.2 : 1), 0, 2 * Math.PI);
    
    if (n.type === 'case') {
      ctx.fillStyle = isMatched ? "#0647E5" : "rgba(6, 71, 229, 0.2)";
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = "#FFFFFF";
      ctx.stroke();

      ctx.font = "bold 9.5px ui-monospace, monospace";
      ctx.fillStyle = isMatched ? "#111318" : "rgba(17,19,24,0.3)";
      ctx.fillText(n.accession || n.label.slice(0, 18), n.x + n.radius + 4, n.y + 3);
    } else {
      ctx.fillStyle = isSelected ? "#0647E5" : isMatched ? "#111318" : "rgba(17,19,24,0.15)";
      ctx.fill();
      if (transform.k > 1.2 || isHovered || isSelected) {
        ctx.font = "8px Inter, sans-serif";
        ctx.fillStyle = isMatched ? "#6B7280" : "rgba(107,114,128,0.2)";
        ctx.fillText(n.label.slice(0, 22), n.x + n.radius + 3, n.y + 2.5);
      }
    }
  }

  ctx.restore();
  graphAnimId = requestAnimationFrame(runGraphPhysics);
}

function bindGraphEvents(canvas) {
  let isDown = false;
  canvas.onmousedown = e => {
    isDown = true;
    dragStart = { x: e.clientX - transform.x, y: e.clientY - transform.y };
  };
  window.onmousemove = e => {
    if (!isDown) {
      const rect = canvas.getBoundingClientRect();
      const mx = (e.clientX - rect.left - transform.x) / transform.k;
      const my = (e.clientY - rect.top - transform.y) / transform.k;
      hoveredNode = graphNodes.find(n => Math.hypot(n.x - mx, n.y - my) <= n.radius + 4) || null;
      canvas.style.cursor = hoveredNode ? "pointer" : "grab";
      return;
    }
    transform.x = e.clientX - dragStart.x;
    transform.y = e.clientY - dragStart.y;
  };
  window.onmouseup = () => { isDown = false; };

  canvas.onclick = e => {
    const rect = canvas.getBoundingClientRect();
    const mx = (e.clientX - rect.left - transform.x) / transform.k;
    const my = (e.clientY - rect.top - transform.y) / transform.k;
    const clicked = graphNodes.find(n => Math.hypot(n.x - mx, n.y - my) <= n.radius + 4);
    if (clicked) {
      selectedNode = clicked;
      showGraphInspector(clicked);
    } else {
      closeGraphInspector();
    }
  };

  canvas.onwheel = e => {
    e.preventDefault();
    const factor = e.deltaY < 0 ? 1.1 : 0.9;
    transform.k = Math.max(0.3, Math.min(4, transform.k * factor));
  };
}

function showGraphInspector(n) {
  const panel = $("#graphInspectorPanel");
  panel.classList.add("open");
  if (n.type === 'case') {
    $("#graphInspAccession").textContent = `${n.accession} · ${n.meta_field}`;
    $("#graphInspTitle").textContent = n.label;
    $("#graphInspDesc").textContent = `Workspace containing ${n.card_count} atomic zettel slips and ${n.pdf_count} research PDFs.`;
    $("#graphInspOpenBtn").onclick = () => {
      selectCase(n.case_idx);
      setTab("lines");
    };
    $("#graphInspFlipperBtn").onclick = () => {
      selectCase(n.case_idx);
      setTab("flipper");
    };
  } else {
    $("#graphInspAccession").textContent = `SLIP · ${n.card_type} · ${n.topic}`;
    $("#graphInspTitle").textContent = n.label;
    $("#graphInspDesc").textContent = `Contained in slipcase #${n.case_idx + 1}.`;
    $("#graphInspOpenBtn").onclick = () => {
      selectCase(n.case_idx);
      setTab("lines");
    };
    $("#graphInspFlipperBtn").onclick = () => {
      selectCase(n.case_idx);
      currentCardIdx = n.card_idx || 0;
      setTab("flipper");
    };
  }
}

window.closeGraphInspector = function() {
  selectedNode = null;
  $("#graphInspectorPanel").classList.remove("open");
};

window.setGraphMode = function(mode) {
  graphMode = mode;
  $$(".graph-controls .graph-btn").forEach(b => b.classList.remove("active"));
  if (mode === "all") $("#graphModeAllBtn").classList.add("active");
  if (mode === "cases") $("#graphModeCasesBtn").classList.add("active");
  if (mode === "bridges") $("#graphModeBridgesBtn").classList.add("active");
  initGraphEngine();
};

window.resetGraphView = function() {
  transform = { x: 0, y: 0, k: 1 };
  initGraphEngine();
};

/* =========================================================
   5. RELATE MODULE: NESTED MATRIX ("CASES OF CASES")
   ========================================================= */
function renderMatrix() {
  const container = $("#matrixClusterContainer");
  let html = "";

  for (const [clusterName, folderList] of Object.entries(GRAPH.meta_clusters)) {
    const clusterCases = CASES.filter(c => folderList.includes(c.id));
    const totalSlips = clusterCases.reduce((acc, c) => acc + c.card_count, 0);
    const totalPdfs = clusterCases.reduce((acc, c) => acc + c.pdf_count, 0);

    html += `
      <div class="cluster-card">
        <div class="cluster-head">
          <div class="cluster-title">${esc(clusterName)}</div>
          <div class="cluster-meta">${clusterCases.length} CASES &middot; ${totalSlips} SLIPS &middot; ${totalPdfs} PDFS</div>
        </div>
        <div class="cluster-body">
    `;

    clusterCases.forEach(c => {
      const idx = CASES.findIndex(x => x.id === c.id);
      html += `
        <div class="matrix-case-row" onclick="selectCase(${idx}); setTab('lines');">
          <div class="matrix-case-accession">${esc(c.accession)}</div>
          <div class="matrix-case-name">${esc(c.name)}</div>
          <div class="matrix-case-counts">${c.card_count} SLIPS &middot; ${c.pdf_count} PDFS &rarr;</div>
        </div>
      `;
    });

    html += `</div></div>`;
  }

  container.innerHTML = html;
}

/* =========================================================
   6. FLIPPER MODULE (TACTILE CARD DECK)
   ========================================================= */
function renderFlipper() {
  const notes = getActiveNotes();
  if (notes.length === 0) {
    $("#cardBoxContainer").innerHTML = `<div class="empty">No cards available in this view.</div>`;
    $("#deckCounter").textContent = "0 OF 0";
    return;
  }

  if (currentCardIdx >= notes.length) currentCardIdx = 0;
  if (currentCardIdx < 0) currentCardIdx = notes.length - 1;

  const card = notes[currentCardIdx];
  $("#deckCounter").textContent = `CARD ${currentCardIdx + 1} OF ${notes.length}`;

  if (rawCardMode) {
    $("#cardBoxContainer").innerHTML = `
      <div class="card-box">
        <div class="card-meta-bar">
          <div class="card-id-tag">${esc(card.id)} &middot; RAW SOURCE</div>
          <div class="card-type-tag">${esc(card.type)}</div>
        </div>
        <pre class="doc-box">${esc(card.raw)}</pre>
      </div>
    `;
    return;
  }

  let fieldsHtml = "";
  for (const [k, v] of Object.entries(card.fields)) {
    if (k === "QUESTION") continue;
    fieldsHtml += `
      <div class="card-field-row">
        <div class="card-field-k">${esc(k)}</div>
        <div class="card-field-v">${esc(v)}</div>
      </div>
    `;
  }

  const qText = card.fields["QUESTION"] || card.title;

  $("#cardBoxContainer").innerHTML = `
    <div class="card-box">
      <div class="card-meta-bar">
        <div class="card-id-tag">${esc(card.id)} &middot; ${esc(card.case_name)}</div>
        <div class="card-type-tag">${esc(card.type)}</div>
      </div>
      <div class="card-title-main">${esc(card.title)}</div>
      ${card.source ? `<div class="card-source-main">${esc(card.source)}</div>` : ''}
      
      <div class="card-question-box">
        <div class="card-question-label">CORE QUESTION</div>
        <div class="card-question-text">${esc(qText)}</div>
      </div>

      ${card.passage ? `<div class="card-passage-box">${esc(card.passage)}</div>` : ''}

      ${fieldsHtml ? `<div class="card-fields-accordion">${fieldsHtml}</div>` : ''}
    </div>
  `;
}

function nextCard() {
  const notes = getActiveNotes();
  if (notes.length === 0) return;
  currentCardIdx = (currentCardIdx + 1) % notes.length;
  renderFlipper();
}

function prevCard() {
  const notes = getActiveNotes();
  if (notes.length === 0) return;
  currentCardIdx = (currentCardIdx - 1 + notes.length) % notes.length;
  renderFlipper();
}

$("#nextCardBtn").onclick = nextCard;
$("#prevCardBtn").onclick = prevCard;

$("#toggleRawBtn").onclick = () => {
  rawCardMode = !rawCardMode;
  $("#toggleRawBtn").textContent = rawCardMode ? "FORMATTED" : "RAW TEXT";
  renderFlipper();
};

$("#copyCardBtn").onclick = async () => {
  const notes = getActiveNotes();
  if (!notes[currentCardIdx]) return;
  try {
    await navigator.clipboard.writeText(notes[currentCardIdx].raw);
    toast("Card text copied");
  } catch(e) {
    toast("Copy failed");
  }
};

$("#downloadCardBtn").onclick = () => {
  const notes = getActiveNotes();
  if (!notes[currentCardIdx]) return;
  const card = notes[currentCardIdx];
  const blob = new Blob([card.raw], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `${card.id}.txt`;
  a.click();
  toast(`Downloaded ${card.id}.txt`);
};

/* Touch swipe for Flipper */
let touchStartX = 0;
let touchEndX = 0;
$("#pane-flipper").addEventListener("touchstart", e => {
  touchStartX = e.changedTouches[0].screenX;
}, { passive: true });
$("#pane-flipper").addEventListener("touchend", e => {
  touchEndX = e.changedTouches[0].screenX;
  if (touchEndX < touchStartX - 50) nextCard();
  if (touchEndX > touchStartX + 50) prevCard();
}, { passive: true });

/* =========================================================
   7. PDF LIBRARY & DUAL-ENGINE READER (RETURN)
   ========================================================= */
function renderPdfs() {
  const pdfs = getActivePdfs();
  const q = $("#search").value.trim().toLowerCase();
  
  let filtered = pdfs.filter(p => {
    if (pdfCategory === "PAPERS" && !p.is_paper) return false;
    if (pdfCategory === "SCANS" && p.is_paper) return false;
    if (!q) return true;
    return p.name.toLowerCase().includes(q) || p.case_name.toLowerCase().includes(q);
  });

  const papersCount = pdfs.filter(p => p.is_paper).length;
  const scansCount = pdfs.filter(p => !p.is_paper).length;

  $("#pdfCatAll").textContent = `ALL (${pdfs.length})`;
  $("#pdfCatPapers").textContent = `PAPERS (${papersCount})`;
  $("#pdfCatScans").textContent = `SCANS & RESOURCES (${scansCount})`;

  if (filtered.length === 0) {
    $("#pdfGrid").innerHTML = `<div class="empty">No PDFs match your filter.</div>`;
    return;
  }

  $("#pdfGrid").innerHTML = filtered.map(p => {
    const sizeMb = (p.size / (1024 * 1024)).toFixed(2);
    const cleanTitle = p.name.replace(/_/g, ' ').replace('.pdf', '');
    return `
      <div class="pdf-card">
        <div class="pdf-card-top">
          <div>
            <div class="pdf-title">${esc(cleanTitle)}</div>
            <div class="pdf-case">${esc(p.accession || '')} &middot; ${esc(p.case_name)}</div>
          </div>
          <div class="pdf-tag ${p.is_paper ? 'tag-paper' : 'tag-scan'}">${p.is_paper ? 'PAPER' : 'SCAN'}</div>
        </div>
        <div class="pdf-actions">
          <div class="pdf-size">${sizeMb} MB</div>
          <div class="pdf-btn-group">
            <a class="pdf-btn primary" href="${encodeURI(p.rel)}" target="_blank">OPEN PDF &nearr;</a>
            <button class="pdf-btn" onclick="openPdfModal('${encodeURIComponent(p.rel)}', '${esc(cleanTitle)}')">PREVIEW</button>
          </div>
        </div>
      </div>
    `;
  }).join("");
}

window.openPdfModal = function(encodedRel, title) {
  const rel = decodeURIComponent(encodedRel);
  $("#pdfModalTitle").textContent = title;
  $("#pdfModalExtBtn").href = rel;
  $("#pdfModalDlBtn").href = rel;
  $("#pdfFallbackBtn").href = rel;
  
  $("#pdfObject").data = rel;
  $("#pdfIframe").src = rel;
  $("#pdfModal").classList.add("open");
};

function closePdfModal() {
  $("#pdfModal").classList.remove("open");
  $("#pdfObject").data = "";
  $("#pdfIframe").src = "about:blank";
}

$("#closePdfModalBtn").onclick = closePdfModal;

$$(".pdf-filter-bar .subchip").forEach(b => {
  b.onclick = () => {
    pdfCategory = b.dataset.pdfCat;
    $$(".pdf-filter-bar .subchip").forEach(c => c.classList.toggle("on", c.dataset.pdfCat === pdfCategory));
    renderPdfs();
  };
});

/* =========================================================
   8. MAPS & STRUCTURAL DOCS MODULE (PRESERVE)
   ========================================================= */
function renderMaps() {
  const caseData = selectedCaseIdx === -1 ? CASES[0] : CASES[selectedCaseIdx];
  if (!caseData || !caseData.specials || Object.keys(caseData.specials).length === 0) {
    $("#mapsTabs").innerHTML = '';
    $("#mapDocContent").textContent = "No structural 000__* documents found for this slipcase.";
    return;
  }

  const docKeys = Object.keys(caseData.specials);
  if (!currentActiveDocKey || !caseData.specials[currentActiveDocKey]) {
    currentActiveDocKey = docKeys[0];
  }

  $("#mapsTabs").innerHTML = docKeys.map(k => {
    const label = k.replace('000__', '').replace('.txt', '').replace(/_/g, ' ');
    return `
      <button class="map-tab-btn ${currentActiveDocKey === k ? 'on' : ''}" onclick="selectDocKey('${esc(k)}')">${esc(label)}</button>
    `;
  }).join("");

  $("#mapDocContent").textContent = caseData.specials[currentActiveDocKey] || "Empty file.";
}

window.selectDocKey = function(k) {
  currentActiveDocKey = k;
  renderMaps();
};

$("#copyDocBtn").onclick = async () => {
  const caseData = selectedCaseIdx === -1 ? CASES[0] : CASES[selectedCaseIdx];
  const docText = caseData?.specials?.[currentActiveDocKey] || "";
  try {
    await navigator.clipboard.writeText(docText);
    toast("Document copied to clipboard");
  } catch(e) {
    toast("Copy failed");
  }
};

$("#downloadDocBtn").onclick = () => {
  const caseData = selectedCaseIdx === -1 ? CASES[0] : CASES[selectedCaseIdx];
  const docText = caseData?.specials?.[currentActiveDocKey] || "";
  const blob = new Blob([docText], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = currentActiveDocKey || "document.txt";
  a.click();
  toast(`Downloaded ${currentActiveDocKey}`);
};

/* =========================================================
   9. PROMPT OPERATOR MODULE (RETURN - COOL RADIO)
   ========================================================= */
function renderPrompts() {
  $("#pomlStepper").innerHTML = PROMPTS.map((p, idx) => `
    <button class="poml-step-btn ${currentPromptIdx === idx ? 'on' : ''}" onclick="selectPrompt(${idx})">${p.num} ${esc(p.title)} ${esc(p.ver)}</button>
  `).join("");

  const p = PROMPTS[currentPromptIdx];
  $("#pomlCardContainer").innerHTML = `
    <div class="poml-card">
      <div class="poml-head-row">
        <div class="poml-num">INSTRUMENT ${p.num} &middot; POML ${p.ver}</div>
        <div class="poml-ver">${p.lines} LINES &middot; ${p.chars} CHARS</div>
      </div>
      <div class="poml-title">${esc(p.title)} ${esc(p.ver)}</div>
      <div class="poml-sub">${esc(p.sub)}</div>
      
      <div class="poml-say-box">SAY: &ldquo;${esc(p.say)}&rdquo;</div>
      <div class="poml-desc">${esc(p.what)}</div>

      <div class="poml-contract-grid">
        <div class="poml-contract-col">
          <div class="poml-contract-k">INPUT CONTRACT</div>
          <div class="poml-contract-v">${esc(p.inp)}</div>
        </div>
        <div class="poml-contract-col">
          <div class="poml-contract-k">OUTPUT CONTRACT</div>
          <div class="poml-contract-v">${esc(p.out)}</div>
        </div>
      </div>

      <div class="poml-actions-bar">
        <button class="poml-btn primary" onclick="copyAndAdvancePrompt()">COPY &amp; NEXT &rarr;</button>
        <button class="poml-btn" onclick="copyPromptText()">COPY PROMPT</button>
        <button class="poml-btn" onclick="downloadPromptFile()">DOWNLOAD .POML</button>
      </div>
    </div>
  `;

  $("#pomlCodeBox").textContent = p.text;
}

window.selectPrompt = function(idx) {
  currentPromptIdx = idx;
  renderPrompts();
};

window.copyAndAdvancePrompt = async function() {
  const p = PROMPTS[currentPromptIdx];
  try {
    await navigator.clipboard.writeText(p.text);
    toast(`Copied ${p.title} ${p.ver}`);
    currentPromptIdx = (currentPromptIdx + 1) % PROMPTS.length;
    renderPrompts();
  } catch(e) {
    toast("Copy failed");
  }
};

window.copyPromptText = async function() {
  const p = PROMPTS[currentPromptIdx];
  try {
    await navigator.clipboard.writeText(p.text);
    toast(`Copied ${p.title} ${p.ver}`);
  } catch(e) {
    toast("Copy failed");
  }
};

window.downloadPromptFile = function() {
  const p = PROMPTS[currentPromptIdx];
  const blob = new Blob([p.text], { type: "text/xml;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = p.file;
  a.click();
  toast(`Downloaded ${p.file}`);
};

/* =========================================================
   10. GLOBAL SEARCH & KEYBOARD SHORTCUTS
   ========================================================= */
$("#search").addEventListener("input", () => {
  if (currentTab === "lines") renderLines();
  if (currentTab === "pdfs") renderPdfs();
});

document.addEventListener("keydown", e => {
  if (e.key === "/" && document.activeElement !== $("#search")) {
    e.preventDefault();
    $("#search").focus();
  }
  if (e.key === "Escape") {
    closeStack();
    closePdfModal();
    closeGraphInspector();
    window.closeThreeInspector?.();
    $("#filterScrim").classList.remove("open");
    $("#caseScrim").classList.remove("open");
  }
  if (currentTab === "flipper") {
    if (e.key === "ArrowRight") nextCard();
    if (e.key === "ArrowLeft") prevCard();
  }
  if (currentTab === "prompts") {
    if (e.key === "ArrowRight") { currentPromptIdx = (currentPromptIdx + 1) % PROMPTS.length; renderPrompts(); }
    if (e.key === "ArrowLeft") { currentPromptIdx = (currentPromptIdx - 1 + PROMPTS.length) % PROMPTS.length; renderPrompts(); }
  }
});

function toast(msg) {
  clearTimeout(toastTimer);
  $("#toast").textContent = msg;
  $("#toast").classList.add("open");
  toastTimer = setTimeout(() => $("#toast").classList.remove("open"), 1400);
}

/* Initial Mount */
updateActiveCaseLabel();
setTab("lines");
</script>

<!-- Three.js 3D Orthographic Slipcase Field Module -->
<script type="module">
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const BLUE = 0x0647E5;
const WHITE = 0xffffff;

let scene, camera, renderer, controls, collectionGroup;
let threeViewMode = "all";
let raycaster, mouse;
let caseMeshes = [];

function initThree() {
  const container = document.getElementById("threeContainer");
  if (!container) return;

  scene = new THREE.Scene();
  scene.background = new THREE.Color(WHITE);

  camera = new THREE.OrthographicCamera();
  camera.position.set(7, 5, 9);
  camera.lookAt(0, 0, 0);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(container.clientWidth || 800, container.clientHeight || 600);
  container.innerHTML = "";
  container.appendChild(renderer.domElement);

  const fillMaterial = new THREE.MeshBasicMaterial({ color: WHITE });
  const edgeMaterial = new THREE.LineBasicMaterial({ color: BLUE, linewidth: 1.5 });

  function outlinedBox(width, height, depth, position = [0, 0, 0]) {
    const geometry = new THREE.BoxGeometry(width, height, depth);
    const group = new THREE.Group();
    const fill = new THREE.Mesh(geometry, fillMaterial);
    const edges = new THREE.LineSegments(new THREE.EdgesGeometry(geometry), edgeMaterial);
    group.add(fill, edges);
    group.position.set(...position);
    return group;
  }

  function createSlipcase({ width = 2, height = 1.5, depth = 1.5, slips = 5, slipHeight = 1.3, slipInset = 0.18, panel = 0.035, label = true, caseData = null } = {}) {
    const root = new THREE.Group();
    root.userData = { caseData };

    // Box bottom, left, right, back, front
    root.add(outlinedBox(width, panel, depth, [0, panel / 2, 0]));
    root.add(outlinedBox(panel, height, depth, [-width / 2 + panel / 2, height / 2, 0]));
    root.add(outlinedBox(panel, height, depth, [width / 2 - panel / 2, height / 2, 0]));
    root.add(outlinedBox(width, height, panel, [0, height / 2, -depth / 2 + panel / 2]));

    const frontHeight = height * 0.68;
    root.add(outlinedBox(width, frontHeight, panel, [0, frontHeight / 2, depth / 2 - panel / 2]));

    // Stepped slips
    const usableDepth = depth - slipInset * 2;
    const spacing = slips > 1 ? usableDepth / (slips - 1) : 0;

    for (let i = 0; i < slips; i++) {
      const z = -usableDepth / 2 + i * spacing;
      const rise = (slips - i - 1) * 0.055;
      const slip = outlinedBox(width * 0.76, slipHeight, 0.025, [0, height * 0.55 + rise, z]);
      root.add(slip);
    }

    if (label) {
      const labelPlate = outlinedBox(width * 0.30, height * 0.18, 0.02, [0, height * 0.32, depth / 2 + 0.016]);
      root.add(labelPlate);
    }

    return root;
  }

  collectionGroup = new THREE.Group();
  scene.add(collectionGroup);

  function buildCollection() {
    while (collectionGroup.children.length > 0) {
      collectionGroup.remove(collectionGroup.children[0]);
    }
    caseMeshes = [];

    if (threeViewMode === "all") {
      // Arrange 31 slipcases in a structured archival grid
      const cols = 6;
      const spacingX = 3.2;
      const spacingZ = 2.8;

      CASES.forEach((c, idx) => {
        const row = Math.floor(idx / cols);
        const col = idx % cols;
        const slipCount = Math.min(8, Math.max(3, Math.round(c.card_count / 10)));
        const box = createSlipcase({
          width: 2.0,
          height: 1.45,
          depth: 1.45,
          slips: slipCount,
          caseData: c
        });
        box.position.x = (col - (cols - 1) / 2) * spacingX;
        box.position.z = (row - 2) * spacingZ;
        collectionGroup.add(box);
        caseMeshes.push(box);
      });
      controls.target.set(0, 0.8, 0);
    } else {
      // Focus on active case
      const targetCase = selectedCaseIdx === -1 ? CASES[0] : CASES[selectedCaseIdx];
      const slipCount = Math.min(10, Math.max(4, Math.round(targetCase.card_count / 8)));
      const box = createSlipcase({
        width: 2.4,
        height: 1.7,
        depth: 1.7,
        slips: slipCount,
        slipHeight: 1.5,
        caseData: targetCase
      });
      box.position.set(0, 0, 0);
      collectionGroup.add(box);
      caseMeshes.push(box);
      controls.target.set(0, 0.8, 0);
    }
  }

  buildCollection();
  collectionGroup.rotation.y = -0.12;

  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.enablePan = true;
  controls.minPolarAngle = Math.PI * 0.15;
  controls.maxPolarAngle = Math.PI * 0.48;
  controls.target.set(0, 0.8, 0);

  raycaster = new THREE.Raycaster();
  mouse = new THREE.Vector2();

  function resize() {
    const container = document.getElementById("threeContainer");
    if (!container) return;
    const w = container.clientWidth || 800;
    const h = container.clientHeight || 600;
    const aspect = w / h;
    const viewHeight = threeViewMode === "all" ? 14 : 5.6;

    camera.left = -viewHeight * aspect / 2;
    camera.right = viewHeight * aspect / 2;
    camera.top = viewHeight / 2;
    camera.bottom = -viewHeight / 2;
    camera.updateProjectionMatrix();

    renderer.setSize(w, h);
  }

  resize();
  window.addEventListener("resize", resize);
  window.triggerThreeResize = resize;

  window.setThreeViewMode = mode => {
    threeViewMode = mode;
    document.querySelectorAll(".three-controls .three-btn").forEach(b => b.classList.remove("active"));
    if (mode === "all") document.getElementById("threeViewAllBtn").classList.add("active");
    if (mode === "focus") document.getElementById("threeViewFocusBtn").classList.add("active");
    buildCollection();
    resize();
  };

  window.updateThreeFocus = idx => {
    if (threeViewMode === "focus") {
      buildCollection();
      resize();
    }
  };

  window.resetThreeCamera = () => {
    camera.position.set(7, 5, 9);
    controls.target.set(0, 0.8, 0);
    resize();
  };

  // Raycasting on Click
  renderer.domElement.addEventListener("click", e => {
    const rect = renderer.domElement.getBoundingClientRect();
    mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(collectionGroup.children, true);

    if (intersects.length > 0) {
      let topGroup = intersects[0].object;
      while (topGroup.parent && topGroup.parent !== collectionGroup) {
        topGroup = topGroup.parent;
      }
      if (topGroup.userData && topGroup.userData.caseData) {
        const c = topGroup.userData.caseData;
        const cIdx = CASES.findIndex(x => x.id === c.id);
        showThreeInspector(c, cIdx);
      }
    }
  });

  function showThreeInspector(c, cIdx) {
    const panel = document.getElementById("threeInspectorPanel");
    panel.classList.add("open");
    document.getElementById("threeInspAccession").textContent = `${c.accession} · ${c.meta_field}`;
    document.getElementById("threeInspTitle").textContent = c.name;
    document.getElementById("threeInspDesc").textContent = `Physical slipcase workspace holding ${c.card_count} zettels and ${c.pdf_count} research PDFs.`;
    document.getElementById("threeInspLinesBtn").onclick = () => {
      selectCase(cIdx);
      setTab("lines");
    };
    document.getElementById("threeInspFlipperBtn").onclick = () => {
      selectCase(cIdx);
      setTab("flipper");
    };
  }

  window.closeThreeInspector = () => {
    document.getElementById("threeInspectorPanel").classList.remove("open");
  };

  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }

  animate();
}

window.addEventListener("DOMContentLoaded", () => {
  setTimeout(initThree, 100);
});
</script>
</body>
</html>
"""

# Replace placeholders with serialized JSON datasets
html_rendered = html_template.replace('/* DATA_CASES */', json.dumps(cases_data)) \
                             .replace('/* DATA_NOTES */', json.dumps(all_notes)) \
                             .replace('/* DATA_PDFS */', json.dumps(all_pdfs)) \
                             .replace('/* DATA_GRAPH */', json.dumps(graph_data)) \
                             .replace('/* DATA_PROMPTS */', json.dumps(prompts_data))

# Write index.html to workspace
with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_rendered)

print('Successfully re-indexed and wrote index.html and slipcases.json with 3D Field, Massive Graph & Relational Matrix.')
