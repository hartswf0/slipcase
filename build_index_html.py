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

# Build Relational Graph Model
graph_nodes = []
graph_links = []
case_relation_matrix = {}

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
    graph_links.append({
        'source': f"case_{card['case_id']}",
        'target': f"slip_{card['id']}",
        'type': 'contains',
        'w': 1
    })

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

# Save standalone JSON dataset
with open(os.path.join(BASE_DIR, 'slipcases.json'), 'w') as f:
    json.dump(cases_data, f, indent=2)

from build_data import prompts_data

html_template = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="slipcase.png">
<title>SLIPCASE — Portable Research Field</title>
<style>
/* SLIPCASE Master Brand Command v1.0 Design Tokens */
:root {
  --blue: #0647E5;
  --blue-soft: #E7EEFF;
  --blue-hover: #053bc2;
  --paper: #FFFFFF;
  --field: #F7F8FA;
  --bg: #F7F8FA;
  --ink: #111318;
  --grey: #9CA3AF;
  --muted: #9CA3AF;
  --muted-dark: #6B7280;
  --pale: #E7EEFF;
  --wash: #EFF4FF;
  --line: 1.5px;
  --border: #E5E7EB;
  --code-bg: #F3F4F6;
  --top: env(safe-area-inset-top);
  --bottom: env(safe-area-inset-bottom);
  --sans: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --serif: "Source Serif 4", ui-serif, Georgia, serif;
  --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; margin: 0; padding: 0; }
html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  overscroll-behavior: none;
}
button, input, select { font: inherit; color: inherit; }
button { border: 0; background: none; cursor: pointer; padding: 0; text-align: inherit; }
button:focus-visible, input:focus-visible { outline: 2px solid var(--blue); outline-offset: 2px; }

#app {
  position: fixed;
  inset: 0;
  background: var(--paper);
  display: flex;
  flex-direction: column;
}

/* -- LOADER: The mark draws itself -- */
#loader {
  position: fixed;
  inset: 0;
  z-index: 300;
  background: var(--paper);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  transition: opacity .38s ease;
}
#loader.done { opacity: 0; pointer-events: none; }
#loader svg { width: 132px; height: auto; }
#loader .ln { fill: none; stroke: var(--blue); stroke-width: 2.4; stroke-linejoin: round; stroke-dasharray: 240; stroke-dashoffset: 240; animation: draw .62s ease forwards; }
#loader .sl { fill: #fff; opacity: 0; animation: rise .5s ease forwards; }
#loader .word { font-size: 11px; letter-spacing: .42em; color: var(--blue); text-transform: uppercase; opacity: 0; animation: fade .5s ease .5s forwards; font-weight: 600; }
#loader .sub { font-family: var(--mono); font-size: 9px; letter-spacing: .14em; color: var(--grey); opacity: 0; animation: fade .5s ease .72s forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@keyframes rise { from { opacity: 0; transform: translateY(9px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fade { to { opacity: 1; } }

/* -- HEADER -- */
header {
  flex: 0 0 auto;
  padding: calc(8px + var(--top)) 16px 8px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 12px;
  align-items: center;
  background: var(--paper);
  border-bottom: 1.5px solid var(--pale);
  z-index: 40;
}
.brand-group {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}
.brand-logo-svg {
  width: 24px;
  height: 24px;
  stroke: var(--blue);
  stroke-width: 1.6;
  fill: none;
}
.brand-text-col {
  display: flex;
  flex-direction: column;
}
.brand-wordmark {
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .16em;
  color: var(--blue);
  line-height: 1.1;
  text-transform: uppercase;
}
.brand-subtitle {
  font-size: 7.5px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--grey);
  text-transform: uppercase;
  margin-top: 2px;
}

.search-wrap {
  position: relative;
  width: 100%;
  max-width: 480px;
}
.search {
  width: 100%;
  height: 38px;
  border: 1.5px solid var(--pale);
  border-radius: 6px;
  background: var(--paper);
  padding: 0 32px 0 11px;
  outline: 0;
  font-size: 12.5px;
  font-family: var(--mono);
  color: var(--ink);
  transition: all .15s ease;
}
.search:focus {
  border-color: var(--blue);
  box-shadow: 0 0 0 2px var(--pale);
}
.search::placeholder { color: var(--grey); }
.search-shortcut {
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 10px;
  font-family: var(--mono);
  color: var(--grey);
  background: var(--paper);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
  pointer-events: none;
}

.accession-badge-btn {
  height: 36px;
  border: 1.5px solid var(--pale);
  border-radius: 6px;
  background: var(--paper);
  padding: 0 10px;
  font-family: var(--mono);
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: .06em;
  color: var(--blue);
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}
.accession-badge-btn:hover {
  background: var(--pale);
  border-color: var(--blue);
}

/* -- METHODOLOGY TRIAD NAVIGATION (PRESERVE · RELATE · RETURN) -- */
.methodology-bar {
  flex: 0 0 auto;
  height: 44px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--paper);
  border-bottom: 1.5px solid var(--pale);
  overflow-x: auto;
  scrollbar-width: none;
  z-index: 39;
}
.methodology-bar::-webkit-scrollbar { display: none; }

.nav-triad-group {
  display: flex;
  align-items: center;
  gap: 4px;
}
.nav-pillar-label {
  font-size: 8px;
  font-weight: 900;
  letter-spacing: .14em;
  color: var(--grey);
  text-transform: uppercase;
  margin-right: 4px;
  padding-left: 2px;
}
.nav-tab-btn {
  border: 1.5px solid transparent;
  border-radius: 5px;
  padding: 5px 9px;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: .06em;
  color: var(--muted-dark);
  text-transform: uppercase;
  white-space: nowrap;
  transition: all .12s ease;
}
.nav-tab-btn:hover {
  color: var(--ink);
  background: var(--field);
}
.nav-tab-btn.on {
  background: var(--blue);
  color: #fff;
  border-color: var(--blue);
}
.nav-divider {
  width: 1px;
  height: 16px;
  background: var(--pale);
  margin: 0 6px;
}

/* -- SUB-TOOLBAR (Filter Chips for LINES) -- */
.subtoolbar {
  flex: 0 0 auto;
  height: 36px;
  padding: 0 16px;
  display: none;
  align-items: center;
  gap: 5px;
  overflow-x: auto;
  background: var(--field);
  border-bottom: 1px solid var(--border);
  scrollbar-width: none;
  z-index: 38;
}
.subtoolbar::-webkit-scrollbar { display: none; }
.subchip {
  flex: 0 0 auto;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--paper);
  padding: 3px 7px;
  font-family: var(--mono);
  font-size: 8px;
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

/* -- MAIN STAGE -- */
main {
  flex: 1 1 auto;
  position: relative;
  overflow: hidden;
  background: var(--field);
}
.pane {
  display: none;
  width: 100%;
  height: 100%;
  position: absolute;
  inset: 0;
  overflow-y: auto;
  scrollbar-width: thin;
}
.pane.active { display: block; }
.pane.no-scroll { overflow: hidden; }

/* =========================================================
   1. READER VIEW (SLIPCASE V3 GESTURE-DRIVEN SCROLLING ENGINE)
   ========================================================= */
#readerStage {
  position: absolute;
  inset: 0;
  overflow: hidden;
  background: var(--field);
  touch-action: pan-y;
}
.rPane {
  position: absolute;
  inset: 0;
}
@media(prefers-reduced-motion:no-preference){
  .rPane { animation: in .18s ease; }
  .rPane.fromRight { animation: inR .2s ease; }
  .rPane.fromLeft { animation: inL .2s ease; }
}
@keyframes in { from { opacity: 0; } to { opacity: 1; } }
@keyframes inR { from { opacity: 0; transform: translateX(18px); } to { opacity: 1; transform: none; } }
@keyframes inL { from { opacity: 0; transform: translateX(-18px); } to { opacity: 1; transform: none; } }

/* Grid of cases */
.rFieldGrid {
  position: absolute;
  inset: 0 0 26px 0;
  padding: 18px 16px 6px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 12px;
}
@media(min-width:680px) { .rFieldGrid { grid-template-columns: repeat(3, 1fr); padding: 22px; gap: 14px; } }
@media(min-width:1020px) { .rFieldGrid { grid-template-columns: repeat(4, 1fr); max-width: 1180px; left: 50%; transform: translateX(-50%); width: 100%; } }
.rCaseCard {
  position: relative;
  background: var(--paper);
  border: var(--line) solid var(--pale);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px;
  min-height: 0;
  text-align: center;
  transition: border-color .12s ease;
}
.rCaseCard:hover, .rCaseCard:active { border-color: var(--blue); }
.rCaseCard svg { width: min(56%, 106px); height: auto; }
.rCaseId { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; color: var(--blue); }
.rCaseTopic { font-size: 11px; line-height: 1.25; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; max-width: 100%; }
.rCaseCount { font-family: var(--mono); font-size: 9px; color: var(--grey); letter-spacing: .06em; }
.rHeldBadge {
  position: absolute;
  top: 8px;
  right: 8px;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  background: var(--blue);
  color: #fff;
  font-family: var(--mono);
  font-size: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
}
.rDotRail {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 8px;
  display: flex;
  justify-content: center;
  gap: 5px;
}
.rDot { width: 5px; height: 5px; border: 1px solid var(--blue); background: var(--paper); }
.rDot.on { background: var(--blue); }
.rEmptyField { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: var(--grey); font-family: var(--mono); font-size: 12px; letter-spacing: .06em; }

/* READ: single scrolling zettel */
.rReadScroll {
  position: absolute;
  inset: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
}
.rDoc { max-width: 680px; margin: 0 auto; padding: 0 18px 90px; }
.rDocHead {
  position: sticky;
  top: 0;
  background: var(--field);
  padding: 14px 0 10px;
  border-bottom: var(--line) solid var(--pale);
  z-index: 3;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 10px;
}
.rDocId { font-family: var(--mono); font-size: 11px; letter-spacing: .1em; color: var(--blue); white-space: nowrap; }
.rDocWhere { font-family: var(--mono); font-size: 10px; color: var(--grey); letter-spacing: .08em; white-space: nowrap; }
.rDocTags { font-family: var(--mono); font-size: 10px; color: var(--grey); letter-spacing: .06em; padding: 10px 0 2px; }

/* Individual Slip in Reader */
.rSlip {
  position: relative;
  margin: 14px 0;
  padding: 12px 14px 13px 16px;
  background: var(--paper);
  border: var(--line) solid var(--pale);
  border-radius: 6px;
  user-select: none;
  -webkit-user-select: none;
  cursor: pointer;
}
.rSlip::before {
  content: "";
  position: absolute;
  left: -1.5px;
  top: -1.5px;
  bottom: -1.5px;
  width: 3px;
  background: transparent;
  border-radius: 4px 0 0 4px;
}
.rSlip.on { background: var(--wash); border-color: var(--blue); }
.rSlip.on::before { background: var(--blue); }
.rSlip.hit { border-color: var(--blue); }
.rfLabel {
  font-family: var(--mono);
  font-size: 9.5px;
  letter-spacing: .14em;
  color: var(--blue);
  margin-bottom: 7px;
  display: flex;
  justify-content: space-between;
  gap: 8px;
}
.rfLabel .rHeldMark { color: var(--blue); opacity: 0; font-size: 9.5px; letter-spacing: .1em; font-weight: 800; }
.rSlip.on .rfLabel .rHeldMark { opacity: 1; }
.rfBody { font-family: var(--serif); font-size: 17px; line-height: 1.55; white-space: pre-wrap; overflow-wrap: break-word; }
.rSlip[data-kind="head"] .rfBody { font-family: var(--sans); font-weight: 650; letter-spacing: -.015em; font-size: 20px; line-height: 1.32; }
.rSlip[data-kind="code"] .rfBody { font-family: var(--mono); font-size: 12px; line-height: 1.6; background: var(--field); padding: 10px 12px; margin: -2px -4px 0; border-radius: 4px; }
.rCaseBar { position: absolute; top: 0; left: 0; height: 2px; background: var(--blue); z-index: 4; transition: width .2s ease; }

/* Floating Tray Chip */
#rChip {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(14px + var(--bottom));
  z-index: 50;
  height: 42px;
  padding: 0 18px;
  background: var(--blue);
  color: #fff;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: .12em;
  display: none;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 18px rgba(6,71,229,.32);
  border-radius: 999px;
}
#rChip.show { display: flex; }
#rChip .n {
  background: #fff;
  color: var(--blue);
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 800;
  border-radius: 999px;
}
@media(prefers-reduced-motion:no-preference){ #rChip.pulse { animation: pulse .28s ease; } }
@keyframes pulse { 40% { transform: translateX(-50%) scale(1.07); } }

/* Tray Drawer */
#rShade {
  position: fixed;
  inset: 0;
  background: rgba(17,19,24,.28);
  z-index: 210;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s;
}
#rShade.show { opacity: 1; pointer-events: auto; }
#rTray {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 220;
  background: var(--paper);
  border-top: var(--line) solid var(--blue);
  max-height: 76vh;
  display: flex;
  flex-direction: column;
  transform: translateY(102%);
  transition: transform .24s cubic-bezier(.3,.9,.3,1);
  padding-bottom: var(--bottom);
}
#rTray.show { transform: none; }
.rTrayHead {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: var(--line) solid var(--pale);
}
.rTrayTitle { font-family: var(--mono); font-size: 11px; font-weight: 850; letter-spacing: .14em; color: var(--blue); }
.rTrayClear { font-family: var(--mono); font-size: 10px; letter-spacing: .1em; color: var(--grey); }
.rTrayClear:hover { color: var(--blue); }
.rTrayList { flex: 1 1 auto; overflow-y: auto; overscroll-behavior: contain; padding: 6px 0 4px; }
.rtItem {
  display: grid;
  grid-template-columns: 26px 1fr 34px;
  align-items: start;
  gap: 6px;
  padding: 9px 12px 9px 8px;
  border-bottom: 1px solid var(--pale);
  background: var(--paper);
}
.rtItem.drag { opacity: .35; }
.rtHandle { width: 26px; padding-top: 3px; display: flex; flex-direction: column; gap: 3px; align-items: center; cursor: grab; touch-action: none; }
.rtHandle i { display: block; width: 14px; height: 0; border-top: 1.5px solid var(--grey); }
.rtBody { min-width: 0; text-align: left; }
.rtMeta { font-family: var(--mono); font-size: 9.5px; letter-spacing: .1em; color: var(--blue); margin-bottom: 3px; font-weight: 700; }
.rtText { font-family: var(--serif); font-size: 13px; line-height: 1.4; color: var(--ink); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.rtItem.open .rtText { display: block; -webkit-line-clamp: unset; white-space: pre-wrap; }
.rtDrop { width: 34px; height: 26px; display: flex; align-items: center; justify-content: center; color: var(--grey); font-size: 16px; line-height: 1; }
.rtDrop:hover { color: var(--blue); }
.rTrayActs {
  flex: 0 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  padding: 12px 16px calc(12px + var(--bottom));
  border-top: var(--line) solid var(--pale);
}
.rTrayBtn {
  height: 42px;
  border: var(--line) solid var(--blue);
  border-radius: 6px;
  color: var(--blue);
  font-family: var(--mono);
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .12em;
  display: flex;
  align-items: center;
  justify-content: center;
}
.rTrayBtn.filled { background: var(--blue); color: #fff; }
mark { background: var(--pale); color: inherit; }

/* =========================================================
   2. TABLE VIEW (INFINITE 2D VOID SPATIAL WORKBENCH)
   ========================================================= */
#tableStage {
  position: absolute;
  inset: 0;
  background: var(--paper);
  touch-action: none;
  overflow: hidden;
  cursor: grab;
}
#tableStage.panning { cursor: grabbing; }
#grain {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(circle at 1px 1px, rgba(6,71,229,.16) 1px, transparent 0);
  background-repeat: repeat;
}
#world {
  position: absolute;
  top: 0;
  left: 0;
  width: 0;
  height: 0;
  transform-origin: 0 0;
  will-change: transform;
}
.reg { position: absolute; pointer-events: none; }
.reg i { position: absolute; background: var(--pale); }
.reg .h { width: 34px; height: 1px; }
.reg .v { width: 1px; height: 34px; }

.card {
  position: absolute;
  width: 280px;
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-radius: 9px 9px 0 0;
  box-shadow: 0 1px 0 rgba(17,19,24,.04);
  display: flex;
  flex-direction: column;
  touch-action: none;
  user-select: none;
}
.card.on { border-color: var(--blue); box-shadow: 0 6px 22px rgba(6,71,229,.14); }
.card.drag { box-shadow: 0 14px 34px rgba(6,71,229,.20); }
.card.landing { animation: land .34s cubic-bezier(.2,.9,.25,1); }
@keyframes land { from { opacity: 0; transform: translateY(-16px) scale(.94); } to { opacity: 1; transform: none; } }
.cTab {
  position: absolute;
  top: -14px;
  left: 14px;
  max-width: 74%;
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-bottom: 0;
  border-radius: 6px 6px 0 0;
  padding: 4px 10px 7px;
  font-family: var(--mono);
  font-size: 8.5px;
  letter-spacing: .1em;
  color: var(--blue);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card.on .cTab { border-color: var(--blue); }
.cMeta {
  padding: 11px 13px 7px;
  border-bottom: 1px solid var(--pale);
  font-family: var(--mono);
  font-size: 8.5px;
  letter-spacing: .06em;
  color: var(--grey);
}
.cMeta b { color: var(--blue); font-weight: 500; }
.cBody {
  padding: 11px 13px 13px;
  font-family: var(--serif);
  font-size: 13.5px;
  line-height: 1.46;
  white-space: pre-wrap;
  overflow-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 9;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card.open .cBody { -webkit-line-clamp: unset; display: block; }
.card[data-k="head"] .cBody { font-family: var(--sans); font-weight: 640; letter-spacing: -.015em; font-size: 14.5px; line-height: 1.34; }
.card[data-k="code"] .cBody { font-family: var(--mono); font-size: 10.5px; line-height: 1.55; background: var(--field); }

.table-bar {
  position: absolute;
  z-index: 60;
  display: flex;
  gap: 6px;
  align-items: center;
}
#tableTopbar { top: 10px; left: 10px; right: 10px; justify-content: space-between; }
#tableBotbar { bottom: calc(10px + var(--bottom)); left: 10px; right: 10px; justify-content: space-between; }
.tgrp {
  display: flex;
  gap: 6px;
  align-items: center;
  background: rgba(255,255,255,.94);
  backdrop-filter: blur(6px);
  padding: 4px;
  border: 1.5px solid var(--pale);
  border-radius: 6px;
}
.tbtn {
  height: 34px;
  padding: 0 10px;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--ink);
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
  border-radius: 4px;
}
.tbtn:hover, .tbtn:active { color: var(--blue); }
.tbtn.key { background: var(--blue); color: var(--paper); }
.tbtn.key:hover { color: var(--paper); }
.tbtn:disabled { opacity: .32; }
#tableStatus {
  font-family: var(--mono);
  font-size: 8.5px;
  letter-spacing: .08em;
  color: var(--grey);
  padding: 0 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 44vw;
}

/* =========================================================
   3. LINES VIEW (ROW-BY-ROW INSPECTOR)
   ========================================================= */
.lines-container {
  max-width: 860px;
  margin: 0 auto;
  background: var(--paper);
  border-left: 1px solid var(--border);
  border-right: 1px solid var(--border);
  min-height: 100%;
}
.zgroup { border-bottom: 8px solid var(--bg); }
.zhead {
  position: sticky;
  top: 0;
  z-index: 5;
  background: rgba(255,255,255,.98);
  backdrop-filter: blur(12px);
  padding: 12px 16px 10px;
  border-bottom: 1px solid var(--border);
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: start;
  cursor: pointer;
}
.zid { font-family: var(--mono); font-size: 9px; font-weight: 850; letter-spacing: .08em; color: var(--blue); margin-bottom: 3px; text-transform: uppercase; }
.ztitle { font-size: 15px; line-height: 1.25; font-weight: 850; letter-spacing: -.02em; }
.ztype { font-family: var(--mono); font-size: 8.5px; font-weight: 850; color: var(--muted-dark); border: 1px solid var(--border); padding: 3px 6px; border-radius: 4px; background: var(--bg); white-space: nowrap; }

.lineRow {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 14px;
  padding: 13px 16px;
  border-bottom: 1px solid var(--border);
  background: var(--paper);
  position: relative;
  user-select: none;
  cursor: pointer;
}
.lineRow:last-child { border-bottom: 0; }
.lineRow.selected { background: var(--blue); color: #fff; }
.lineRow.selected .fieldName { color: var(--blue-soft); }
.fieldName { font-family: var(--mono); font-size: 8.5px; line-height: 1.3; font-weight: 900; letter-spacing: .08em; color: var(--muted-dark); text-transform: uppercase; padding-top: 3px; word-break: break-word; }
.lineText { font-family: var(--serif); font-size: 16.5px; line-height: 1.5; white-space: pre-wrap; }
.lineRow[data-field="TITLE"] .lineText,
.lineRow[data-field="QUESTION"] .lineText,
.lineRow[data-field="DEEPER QUESTION"] .lineText { font-family: var(--sans); font-weight: 760; letter-spacing: -.025em; }
.lineRow.code .lineText { font-family: var(--mono); font-size: 12px; line-height: 1.55; background: var(--code-bg); padding: 10px 12px; border-radius: 6px; overflow-x: auto; }
.lineRow.selected.code .lineText { background: rgba(0,0,0,.25); color: #fff; }

.empty { padding: 60px 20px; text-align: center; color: var(--muted-dark); font-size: 13.5px; line-height: 1.6; }

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
.selCount { font-size: 11.5px; font-weight: 800; letter-spacing: .05em; font-family: var(--mono); }
.selection button { height: 36px; padding: 0 12px; border-radius: 6px; background: #262930; color: #fff; font-size: 10px; font-weight: 850; letter-spacing: .06em; }
.selection .primary { background: var(--blue); color: #fff; }

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
.stackHead { height: calc(58px + var(--top)); padding: var(--top) 16px 0; border-bottom: 1px solid var(--border); display: grid; grid-template-columns: 48px 1fr 48px; align-items: center; background: var(--paper); }
.stackHead button { height: 42px; font-size: 18px; font-weight: 900; }
.stackHead div { text-align: center; font-size: 10.5px; font-weight: 850; color: var(--blue); letter-spacing: .08em; font-family: var(--mono); }
.stackScroll { flex: 1; overflow-y: auto; padding: 16px 20px calc(24px + var(--bottom)); max-width: 800px; margin: 0 auto; width: 100%; }
.stackItem { padding: 18px 0; border-bottom: 1px solid var(--border); }
.stackMeta { font-family: var(--mono); font-size: 9px; color: var(--blue); font-weight: 800; letter-spacing: .08em; margin-bottom: 6px; text-transform: uppercase; }
.stackText { font-family: var(--serif); font-size: 18.5px; line-height: 1.55; white-space: pre-wrap; }

/* 4. RELATE: 3D FIELD, GRAPH, MATRIX */
.three-pane-wrap, .graph-pane-wrap { width: 100%; height: 100%; position: relative; background: #FFFFFF; }
#graphCanvas { width: 100%; height: 100%; display: block; }
.three-hud, .graph-hud {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(255,255,255,.94);
  backdrop-filter: blur(10px);
  border: 1.5px solid var(--pale);
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 4px 16px rgba(0,0,0,.04);
  font-family: var(--mono);
  font-size: 9.5px;
  pointer-events: none;
  z-index: 10;
}
.three-hud-title, .graph-hud-title { font-weight: 900; color: var(--blue); letter-spacing: .08em; margin-bottom: 3px; }
.three-hud-meta, .graph-hud-meta { color: var(--muted-dark); }
.three-controls, .graph-controls { position: absolute; top: 12px; right: 12px; display: flex; flex-direction: column; gap: 6px; z-index: 10; }
.three-btn, .graph-btn {
  height: 32px;
  padding: 0 10px;
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-radius: 6px;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--ink);
}
.three-btn.active, .graph-btn.active { background: var(--blue); color: #fff; border-color: var(--blue); }

.three-inspector-panel, .graph-inspector-panel {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  max-width: 480px;
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-radius: 10px;
  padding: 14px 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,.1);
  display: none;
  z-index: 20;
}
.three-inspector-panel.open, .graph-inspector-panel.open { display: block; }
.graph-insp-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; }
.graph-insp-accession { font-family: var(--mono); font-size: 9px; font-weight: 850; color: var(--blue); }
.graph-insp-title { font-size: 15px; font-weight: 850; line-height: 1.25; margin-bottom: 8px; }
.graph-insp-desc { font-size: 12px; color: var(--muted-dark); line-height: 1.4; margin-bottom: 10px; }
.graph-insp-actions { display: flex; gap: 6px; }

/* Matrix */
.matrix-wrap { max-width: 860px; margin: 0 auto; padding: 16px 16px calc(28px + var(--bottom)); }
.matrix-intro { background: var(--paper); border: 1.5px solid var(--pale); border-left: 3px solid var(--blue); border-radius: 8px; padding: 14px 16px; margin-bottom: 16px; }
.matrix-intro-k { font-family: var(--mono); font-size: 9px; font-weight: 900; color: var(--blue); letter-spacing: .08em; margin-bottom: 4px; }
.matrix-intro-v { font-size: 13px; line-height: 1.5; color: var(--ink); }
.cluster-card { background: var(--paper); border: 1.5px solid var(--pale); border-radius: 10px; margin-bottom: 12px; overflow: hidden; }
.cluster-head { padding: 12px 16px; background: var(--field); border-bottom: 1.5px solid var(--pale); display: flex; align-items: center; justify-content: space-between; cursor: pointer; }
.cluster-title { font-size: 12px; font-weight: 900; letter-spacing: .06em; text-transform: uppercase; color: var(--blue); }
.cluster-meta { font-family: var(--mono); font-size: 9px; font-weight: 800; color: var(--muted-dark); }
.cluster-body { display: flex; flex-direction: column; }
.matrix-case-row { padding: 12px 16px; border-bottom: 1px solid var(--pale); display: grid; grid-template-columns: 140px 1fr auto; gap: 12px; align-items: center; cursor: pointer; transition: background .12s ease; }
.matrix-case-row:last-child { border-bottom: 0; }
.matrix-case-row:hover { background: var(--blue-soft); }
.matrix-case-accession { font-family: var(--mono); font-size: 9px; font-weight: 850; color: var(--blue); }
.matrix-case-name { font-size: 13px; font-weight: 800; }
.matrix-case-counts { font-family: var(--mono); font-size: 9px; font-weight: 800; color: var(--muted-dark); white-space: nowrap; }

/* 5. RETURN: PDFS, MAPS, PROMPTS */
.pdf-wrap, .maps-wrap, .prompts-wrap { padding: 16px 16px calc(24px + var(--bottom)); max-width: 860px; margin: 0 auto; }
.pdf-filter-bar, .maps-tabs, .poml-stepper { display: flex; gap: 6px; margin-bottom: 14px; overflow-x: auto; scrollbar-width: none; }
.pdf-filter-bar::-webkit-scrollbar, .maps-tabs::-webkit-scrollbar, .poml-stepper::-webkit-scrollbar { display: none; }
.pdf-grid { display: grid; grid-template-columns: 1fr; gap: 10px; }
.pdf-card { background: var(--paper); border: 1.5px solid var(--pale); border-radius: 8px; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; }
.pdf-card-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.pdf-title { font-size: 14.5px; font-weight: 800; line-height: 1.28; letter-spacing: -.02em; }
.pdf-case { font-family: var(--mono); font-size: 9px; font-weight: 850; color: var(--blue); margin-top: 4px; text-transform: uppercase; }
.pdf-tag { font-family: var(--mono); font-size: 8.5px; font-weight: 900; letter-spacing: .06em; padding: 3px 6px; border-radius: 4px; white-space: nowrap; text-transform: uppercase; }
.tag-paper { background: var(--blue-soft); color: var(--blue); }
.tag-scan { background: var(--bg); color: var(--muted-dark); border: 1px solid var(--border); }
.pdf-actions { display: flex; align-items: center; justify-content: space-between; padding-top: 10px; border-top: 1px solid var(--border); }
.pdf-size { font-family: var(--mono); font-size: 9.5px; font-weight: 800; color: var(--muted-dark); }
.pdf-btn-group { display: flex; gap: 6px; }
.pdf-btn, .deck-btn { height: 32px; padding: 0 12px; border-radius: 6px; border: 1.5px solid var(--pale); background: var(--paper); font-family: var(--mono); font-size: 9px; font-weight: 850; letter-spacing: .06em; display: inline-flex; align-items: center; text-decoration: none; }
.pdf-btn.primary, .deck-btn.primary { background: var(--blue); color: #fff; border-color: var(--blue); }

.doc-box { background: var(--paper); border: 1.5px solid var(--pale); border-radius: 8px; padding: 18px 16px; font-family: var(--mono); font-size: 12px; line-height: 1.6; white-space: pre-wrap; overflow-x: auto; }
.doc-action-bar { display: flex; justify-content: flex-end; gap: 8px; margin-top: 10px; }

/* PROMPTS */
.poml-card { background: var(--paper); border: 1.5px solid var(--pale); border-radius: 12px; padding: 20px 18px; margin-bottom: 14px; }
.poml-head-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; }
.poml-num { font-family: var(--mono); font-size: 10px; font-weight: 900; color: var(--blue); letter-spacing: .08em; }
.poml-ver { font-family: var(--mono); font-size: 9px; font-weight: 850; color: var(--muted-dark); }
.poml-title { font-size: 19px; font-weight: 850; line-height: 1.2; margin-bottom: 4px; }
.poml-sub { font-size: 11px; color: var(--muted-dark); margin-bottom: 12px; text-transform: uppercase; letter-spacing: .06em; font-weight: 750; }
.poml-say-box { background: var(--blue-soft); border-left: 3px solid var(--blue); padding: 10px 12px; border-radius: 0 6px 6px 0; margin-bottom: 12px; font-size: 13px; font-weight: 750; color: var(--blue); }
.poml-desc { font-size: 13px; line-height: 1.5; color: var(--ink); margin-bottom: 14px; }
.poml-contract-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 14px; }
.poml-contract-col { background: var(--bg); padding: 8px 10px; border-radius: 6px; }
.poml-contract-k { font-family: var(--mono); font-size: 8px; font-weight: 900; color: var(--muted-dark); letter-spacing: .08em; margin-bottom: 2px; }
.poml-contract-v { font-size: 11px; line-height: 1.4; }
.poml-actions-bar { display: flex; gap: 8px; }
.poml-btn { height: 36px; padding: 0 14px; border-radius: 6px; border: 1.5px solid var(--pale); background: var(--paper); font-family: var(--mono); font-size: 9.5px; font-weight: 850; letter-spacing: .06em; }
.poml-btn.primary { background: var(--blue); color: #fff; border-color: var(--blue); }
.poml-code-box { font-family: var(--mono); font-size: 11px; line-height: 1.6; white-space: pre-wrap; background: var(--paper); border: 1.5px solid var(--pale); border-radius: 8px; padding: 16px; max-height: 480px; overflow-y: auto; }

/* Table Drawer */
#drawer {
  position: fixed;
  z-index: 280;
  left: 0;
  right: 0;
  bottom: 0;
  max-height: 76vh;
  background: var(--paper);
  border-top: 1.5px solid var(--blue);
  transform: translateY(102%);
  transition: transform .26s cubic-bezier(.2,.85,.25,1);
  display: flex;
  flex-direction: column;
  padding-bottom: var(--bottom);
}
#drawer.open { transform: translateY(0); }
.dHead {
  flex: 0 0 auto;
  padding: 11px 12px;
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 8px;
  align-items: center;
  border-bottom: 1px solid var(--pale);
}
.dSearch {
  height: 36px;
  border: 1.5px solid var(--pale);
  background: var(--paper);
  padding: 0 11px;
  outline: 0;
  min-width: 0;
  font-family: var(--mono);
  font-size: 12px;
}
.dSearch:focus { border-color: var(--blue); }
.dSearch::placeholder { color: var(--grey); }
.dBody { flex: 1 1 auto; overflow: auto; padding: 12px; scrollbar-width: thin; }
.caseRow { display: grid; grid-template-columns: repeat(auto-fill, minmax(96px, 1fr)); gap: 10px; }
.caseBtn {
  border: 1.5px solid var(--pale);
  background: var(--paper);
  border-radius: 6px;
  padding: 9px 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  text-align: center;
}
.caseBtn:hover, .caseBtn.on { border-color: var(--blue); }
.caseBtn svg { width: 56px; height: auto; }
.caseBtn .cid { font-family: var(--mono); font-size: 8.5px; letter-spacing: .06em; color: var(--blue); }
.caseBtn .ctp { font-size: 9px; color: var(--grey); line-height: 1.2; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.fan { margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--pale); }
.fanHead { font-family: var(--mono); font-size: 9px; letter-spacing: .1em; color: var(--grey); margin-bottom: 9px; display: flex; justify-content: space-between; gap: 8px; align-items: center; }
.fanHead b { color: var(--blue); font-weight: 500; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { border: 1.5px solid var(--pale); background: var(--paper); padding: 8px 10px; font-family: var(--mono); font-size: 9px; letter-spacing: .07em; color: var(--ink); border-radius: 5px 5px 0 0; }
.chip:hover { border-color: var(--blue); color: var(--blue); }
.chip.placed { background: var(--pale); color: var(--blue); border-color: var(--pale); }
.dEmpty { padding: 34px 10px; text-align: center; font-family: var(--mono); font-size: 11px; letter-spacing: .06em; color: var(--grey); }

.scrim { position: fixed; inset: 0; z-index: 200; background: rgba(17,19,24,.12); display: none; }
.scrim.open { display: block; }
.sheet {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: calc(12px + var(--bottom));
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-radius: 12px;
  padding: 14px;
  box-shadow: 0 18px 60px rgba(0,0,0,.16);
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.sheetTitle { padding: 4px 6px 12px; font-family: var(--mono); font-size: 10px; font-weight: 900; color: var(--blue); letter-spacing: .08em; text-transform: uppercase; }
.sheetScroll { overflow-y: auto; flex: 1; }
.sheetGrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; }
.sheetGrid button { min-height: 42px; border-radius: 6px; background: var(--bg); font-family: var(--mono); font-size: 9.5px; font-weight: 800; padding: 6px 8px; text-align: center; border: 1px solid var(--border); }
.sheetGrid button.on { background: var(--blue); color: #fff; border-color: var(--blue); }

.caseList { display: flex; flex-direction: column; gap: 4px; }
.caseRowBtn { padding: 10px 12px; border-radius: 6px; background: var(--bg); border: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; text-align: left; }
.caseRowBtn.on { background: var(--blue); color: #fff; border-color: var(--blue); }
.caseRowBtn.on .caseRowMeta, .caseRowBtn.on .caseRowAccession { color: var(--blue-soft); }
.caseRowAccession { font-family: var(--mono); font-size: 8.5px; font-weight: 850; color: var(--blue); }
.caseRowTitle { font-size: 12.5px; font-weight: 800; letter-spacing: -.01em; margin-top: 1px; }
.caseRowMeta { font-family: var(--mono); font-size: 9px; font-weight: 800; color: var(--muted-dark); white-space: nowrap; }

.toast {
  position: fixed;
  z-index: 400;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(76px + var(--bottom));
  transform: translateX(-50%);
  background: var(--ink);
  color: #fff;
  border-radius: 999px;
  padding: 8px 16px;
  font-family: var(--mono);
  font-size: 10.5px;
  font-weight: 750;
  display: none;
  white-space: nowrap;
  box-shadow: 0 6px 20px rgba(0,0,0,.2);
}
.toast.open { display: block; }

.pdf-modal {
  position: fixed;
  z-index: 250;
  inset: 0;
  background: var(--paper);
  transform: translateY(104%);
  transition: transform .24s cubic-bezier(.2,.8,.2,1);
  display: flex;
  flex-direction: column;
}
.pdf-modal.open { transform: translateY(0); }
.pdf-modal-head { height: calc(54px + var(--top)); padding: var(--top) 16px 0; border-bottom: 1.5px solid var(--pale); display: flex; align-items: center; justify-content: space-between; gap: 12px; background: var(--paper); }
.pdf-modal-title { font-size: 13px; font-weight: 850; max-width: 50%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.pdf-frame-wrap { flex: 1; position: relative; background: #525659; }
.pdf-frame { width: 100%; height: 100%; border: 0; }
.pdf-fallback-note { position: absolute; bottom: 12px; left: 12px; right: 12px; background: var(--paper); border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px; font-size: 11px; color: var(--muted-dark); display: flex; align-items: center; justify-content: space-between; gap: 8px; }

@media(min-width: 760px) {
  .pdf-grid { grid-template-columns: 1fr 1fr; }
  .lineRow { grid-template-columns: 140px 1fr; padding-left: 20px; padding-right: 20px; }
  .zhead { padding-left: 20px; padding-right: 20px; }
  .selection { left: 50%; right: auto; transform: translateX(-50%); width: 560px; }
  .sheet { left: 50%; right: auto; transform: translateX(-50%); width: 620px; }
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

  <!-- LOADER -->
  <div id="loader">
    <svg viewBox="0 0 96 78" aria-hidden="true">
      <g>
        <rect class="sl" x="20" y="16" width="34" height="40" rx="5" style="animation-delay:.18s"/>
        <rect class="ln sl" x="20" y="16" width="34" height="40" rx="5" style="animation-delay:.18s;fill:none"/>
        <rect class="sl" x="27" y="12.5" width="34" height="40" rx="5" style="animation-delay:.26s"/>
        <rect class="ln sl" x="27" y="12.5" width="34" height="40" rx="5" style="animation-delay:.26s;fill:none"/>
        <rect class="sl" x="34" y="9" width="34" height="40" rx="5" style="animation-delay:.34s"/>
        <rect class="ln sl" x="34" y="9" width="34" height="40" rx="5" style="animation-delay:.34s;fill:none"/>
      </g>
      <path class="ln" d="M14 34 h68 v38 h-68 z" style="fill:#fff"/>
      <rect class="ln" x="38" y="48" width="20" height="11" style="animation-delay:.3s"/>
    </svg>
    <div class="word">Slipcase</div>
    <div class="sub" id="loadNote">PREPARING THE RESEARCH FIELD</div>
  </div>

  <!-- MASTER HEADER -->
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

  <!-- METHODOLOGY BAR (PRESERVE · RELATE · RETURN) -->
  <div class="methodology-bar" id="methodologyBar">
    <div class="nav-triad-group">
      <span class="nav-pillar-label">PRESERVE</span>
      <button class="nav-tab-btn on" data-tab="reader">READER</button>
      <button class="nav-tab-btn" data-tab="table">TABLE</button>
      <button class="nav-tab-btn" data-tab="lines">LINES</button>
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

  <!-- Sub-toolbar -->
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

  <!-- VIEWPORT -->
  <main id="mainViewport">
    
    <!-- 1. READER PANE (SLIPCASE V3 GESTURE-DRIVEN SCROLLING ENGINE) -->
    <div class="pane active no-scroll" id="pane-reader">
      <div id="readerStage"></div>
    </div>

    <!-- 2. TABLE PANE (INFINITE 2D SPATIAL WORKBENCH) -->
    <div class="pane no-scroll" id="pane-table">
      <div id="tableStage">
        <div id="grain"></div>
        <div id="world"></div>
      </div>

      <div class="table-bar" id="tableTopbar">
        <div class="tgrp">
          <span class="brand-wordmark" style="font-size:10px;padding:0 6px;">TABLE</span>
          <span id="tableStatus">—</span>
        </div>
        <div class="tgrp">
          <button class="tbtn" id="fitBtn">FIT</button>
          <button class="tbtn" id="saveBtn">SAVE</button>
          <button class="tbtn" id="openBtn">OPEN</button>
          <button class="tbtn" id="shareBtn">SHARE</button>
        </div>
      </div>

      <div class="table-bar" id="tableBotbar">
        <div class="tgrp">
          <button class="tbtn key" id="drawerBtn">SLIPCASES</button>
          <button class="tbtn" id="readBtn">READ ORDER</button>
        </div>
        <div class="tgrp" id="selGrp" style="display:none">
          <button class="tbtn" id="expandBtn">EXPAND</button>
          <button class="tbtn" id="removeBtn">RETURN</button>
        </div>
      </div>
    </div>

    <!-- 3. LINES PANE -->
    <div class="pane" id="pane-lines">
      <div class="lines-container">
        <div id="table"></div>
      </div>
    </div>

    <!-- 4. MAPS PANE -->
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

    <!-- 5. 3D FIELD PANE -->
    <div class="pane no-scroll" id="pane-three">
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
            <button class="deck-btn" id="threeInspReaderBtn">OPEN IN READER &rarr;</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. GRAPH PANE -->
    <div class="pane no-scroll" id="pane-graph">
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
            <button class="deck-btn" id="graphInspReaderBtn">OPEN IN READER &rarr;</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 7. NESTED MATRIX PANE -->
    <div class="pane" id="pane-matrix">
      <div class="matrix-wrap">
        <div class="matrix-intro">
          <div class="matrix-intro-k">CASES OF CASES &middot; SLIPS OF SLIPS &middot; RELATIONAL MATRIX</div>
          <div class="matrix-intro-v">Multi-tiered archival taxonomy organizing 31 field slipcases into 5 meta-research clusters, exposing 5,083 cross-citations and 124 primary source documents.</div>
        </div>
        <div id="matrixClusterContainer"></div>
      </div>
    </div>

    <!-- 8. PDFS PANE -->
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

    <!-- 9. PROMPTS PANE -->
    <div class="pane" id="pane-prompts">
      <div class="prompts-wrap">
        <div class="poml-stepper" id="pomlStepper"></div>
        <div id="pomlCardContainer"></div>
        <div class="poml-code-box" id="pomlCodeBox"></div>
      </div>
    </div>

  </main>

  <!-- FLOATING TRAY CHIP & DRAWER FOR READER -->
  <button id="rChip" aria-label="Open tray"><span>TRAY</span><span class="n" id="rChipN">0</span></button>
  <div id="rShade"></div>
  <section id="rTray" role="dialog" aria-label="Tray">
    <div class="rTrayHead">
      <span class="rTrayTitle" id="rTrayTitle">TRAY</span>
      <button class="rTrayClear" id="rTrayClear">CLEAR</button>
    </div>
    <div class="rTrayList" id="rTrayList"></div>
    <div class="rTrayActs">
      <button class="rTrayBtn" id="rCopyBtn">COPY ALL</button>
      <button class="rTrayBtn filled" id="rExportBtn">EXPORT .MD</button>
    </div>
  </section>

  <!-- TABLE DRAWER -->
  <section id="drawer">
    <div class="dHead">
      <input id="dSearch" class="dSearch" placeholder="Search 31 slipcases and 1,244 cards..." autocomplete="off">
      <button class="tbtn" id="drawerClose">CLOSE</button>
    </div>
    <div class="dBody" id="dBody"></div>
  </section>

  <!-- Selection Bar for LINES -->
  <div class="selection" id="selection">
    <div class="selCount" id="selCount">0 selected</div>
    <button id="clearBtn">CLEAR</button>
    <button id="stackBtn" class="primary">READ STACK</button>
  </div>

  <!-- Stack Modal -->
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

  <!-- Case Switcher Sheet -->
  <div class="scrim" id="caseScrim">
    <div class="sheet">
      <div class="sheetTitle">SELECT FIELD SLIPCASE</div>
      <div class="sheetScroll">
        <div class="caseList" id="caseList"></div>
      </div>
    </div>
  </div>

  <!-- Filter Modal Sheet -->
  <div class="scrim" id="filterScrim">
    <div class="sheet">
      <div class="sheetTitle">SELECT FIELD FILTER</div>
      <div class="sheetScroll">
        <div class="sheetGrid" id="sheetGrid"></div>
      </div>
    </div>
  </div>

  <div class="scrim" id="drawerScrim"></div>
  <input type="file" id="filePick" accept=".json,application/json" style="display:none">

  <!-- Toast Notification -->
  <div class="toast" id="toast"></div>

</div>

<!-- Primary Application Engine -->
<script>
(()=>{
"use strict";

const CASES_DATA = /* DATA_CASES */;
const ALL_NOTES = /* DATA_NOTES */;
const ALL_PDFS = /* DATA_PDFS */;
const GRAPH = /* DATA_GRAPH */;
const PROMPTS = /* DATA_PROMPTS */;

window.CASES_DATA = CASES_DATA;
window.ZETTEL_DATA = ALL_NOTES;

const FIELD_ORDER = [
  "TITLE","QUESTION","DEEPER QUESTION","PASSAGE","RESEARCH OBJECT","LOCAL MOVE",
  "SOURCE TERMS","WHAT BECAME STRANGE","MECHANISM","FORMAL SHIFT","SOURCE FORMALISM",
  "OUR FORMALIZATION","TENSION","MISSING","BOUNDARY","CITATION TRAIL","TEST",
  "PLATFORM","LINKS","BIBTEX","SOURCE"
];

const CODE_FIELD = /FORMAL|BIBTEX|MECHANISM/;
const HEAD_FIELD = /^(TITLE|QUESTION|DEEPER QUESTION)$/;

const ESC = { "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;" };
const esc = s => String(s ?? "").replace(/[&<>"']/g, m => ESC[m]);
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];

function valueFor(n, f) {
  if (f === "TITLE") return n.title;
  if (f === "SOURCE") return n.source;
  if (f === "PASSAGE") return n.passage;
  if (f === "TYPE") return n.type;
  if (f === "QUESTION" && n.fields && n.fields["QUESTION"]) return n.fields["QUESTION"];
  return (n.fields && n.fields[f]) || "";
}

let currentTab = "reader";
let selectedCaseIdx = -1;
let lineFilter = "ALL";
let pdfCategory = "ALL";
let currentPromptIdx = 0;
let currentActiveDocKey = "";
let selectedLines = new Set();
let toastTimer = null;

function getActiveNotes() {
  if (selectedCaseIdx === -1) return ALL_NOTES;
  return CASES_DATA[selectedCaseIdx]?.cards || [];
}

function getActivePdfs() {
  if (selectedCaseIdx === -1) return ALL_PDFS;
  return CASES_DATA[selectedCaseIdx]?.pdfs || [];
}

function setTab(tab) {
  currentTab = tab;
  $$(".nav-tab-btn").forEach(b => b.classList.toggle("on", b.dataset.tab === tab));
  $$(".pane").forEach(p => p.classList.remove("active"));
  const targetPane = $(`#pane-${tab}`);
  if (targetPane) targetPane.classList.add("active");

  const subtoolbar = $("#linesSubtoolbar");
  if (tab === "lines") {
    subtoolbar.style.display = "flex";
    renderLines();
  } else {
    subtoolbar.style.display = "none";
  }

  if (tab === "reader") renderReader();
  if (tab === "table") applyTableView();
  if (tab === "maps") renderMaps();
  if (tab === "three") window.triggerThreeResize?.();
  if (tab === "graph") initGraphEngine();
  if (tab === "matrix") renderMatrix();
  if (tab === "pdfs") renderPdfs();
  if (tab === "prompts") renderPrompts();
}

$$(".nav-tab-btn").forEach(b => {
  b.onclick = () => setTab(b.dataset.tab);
});

$("#brandBtn").onclick = () => {
  selectedCaseIdx = -1;
  updateActiveCaseLabel();
  setTab("reader");
};

function updateActiveCaseLabel() {
  if (selectedCaseIdx === -1) {
    $("#caseNavBtn").textContent = "ALL CASES (31)";
    $("#pdfTabBtn").textContent = `PDFS (${ALL_PDFS.length})`;
  } else {
    const c = CASES_DATA[selectedCaseIdx];
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

  CASES_DATA.forEach((c, idx) => {
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
  updateActiveCaseLabel();
  $("#caseScrim").classList.remove("open");
  if (currentTab === "reader") { readerView = "FIELD"; readerFieldPage = 0; renderReader(); }
  if (currentTab === "table") applyTableView();
  if (currentTab === "lines") renderLines();
  if (currentTab === "maps") renderMaps();
  if (currentTab === "three") window.updateThreeFocus?.(idx);
  if (currentTab === "graph") initGraphEngine();
  if (currentTab === "matrix") renderMatrix();
  if (currentTab === "pdfs") renderPdfs();
  toast(idx === -1 ? "Showing All 31 Slipcases" : `Switched to ${CASES_DATA[idx].accession}`);
};

$("#caseNavBtn").onclick = openCaseModal;
$("#caseScrim").addEventListener("pointerdown", e => {
  if (e.target === $("#caseScrim")) $("#caseScrim").classList.remove("open");
});

/* =========================================================
   1. READER ENGINE (SLIPCASE V3 GESTURES & SCROLLING)
   ========================================================= */
const LONG_PRESS_MS = 430;
const MOVE_CANCEL_PX = 10;
const SWIPE_PX = 56;
const SWIPE_SLOP = 42;
const MAX_DOTS = 14;

// Index notes for Reader & Table
const KASTEN_CASES = [];
const kastenById = new Map();

for (let i = 0; i < ALL_NOTES.length; i++) {
  const n = ALL_NOTES[i], slips = [];
  let low = (n.id + " " + n.type + " " + n.topic + " " + (n.symbol || "") + " " + n.case_name).toLowerCase();
  for (const f of FIELD_ORDER) {
    const v = valueFor(n, f);
    if (!v) continue;
    slips.push({ f, text: v });
    low += " " + (f + " " + v).toLowerCase();
  }
  KASTEN_CASES.push({ i, id: n.id, slips, low, case_idx: n.case_idx });
  kastenById.set(n.id, i);
}

let readerView = "FIELD"; // "FIELD" | "READ"
let readerFiltered = KASTEN_CASES.map((_, k) => k);
let readerFieldPage = 0, readerCaseK = 0, readerSlideDir = 0;
let readerTray = []; // [{i, f}]
let readerTrayOpen = false;

const readerPageSize = () => innerWidth >= 1020 ? 12 : innerWidth >= 680 ? 9 : 6;
const inReaderTray = (i, f) => readerTray.findIndex(t => t.i === i && t.f === f);
const heldInReaderCase = i => readerTray.reduce((a, t) => a + (t.i === i ? 1 : 0), 0);

function monolineCaseIcon(count) {
  const n = Math.min(count, 5);
  let s = "";
  for (let k = 0; k < n; k++) {
    const x = 20 + k * 7, y = 16 - k * 3.5;
    s += `<rect x="${x}" y="${y}" width="34" height="40" rx="5" fill="#fff" stroke="#0647E5" stroke-width="2.5"/>`;
  }
  return `<svg viewBox="0 0 96 78" aria-hidden="true">${s}
  <path d="M14 34 h68 v38 h-68 z" fill="#fff" stroke="#0647E5" stroke-width="2.5"/>
  <rect x="38" y="48" width="20" height="11" fill="#fff" stroke="#0647E5" stroke-width="2.5"/></svg>`;
}

function hl(text, qTokens) {
  let out = esc(text);
  if (!qTokens || !qTokens.length) return out;
  for (const t of qTokens) {
    if (!t) continue;
    const re = new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi");
    out = out.replace(re, m => "\u0001" + m + "\u0002");
  }
  return out.replace(/\u0001/g, "<mark>").replace(/\u0002/g, "</mark>");
}

function renderReader(keepScroll) {
  const activeKasten = (selectedCaseIdx === -1) 
    ? KASTEN_CASES.map((_, k) => k) 
    : KASTEN_CASES.map((c, k) => ({ c, k })).filter(x => x.c.case_idx === selectedCaseIdx).map(x => x.k);

  const q = $("#search").value.trim().toLowerCase();
  const qTokens = q ? q.split(/\s+/).filter(Boolean) : [];

  readerFiltered = activeKasten.filter(k => {
    if (!qTokens.length) return true;
    return qTokens.every(t => KASTEN_CASES[k].low.includes(t));
  });

  const stage = $("#readerStage");

  if (readerView === "FIELD") {
    const ps = readerPageSize(), pages = Math.max(1, Math.ceil(readerFiltered.length / ps));
    readerFieldPage = Math.min(Math.max(readerFieldPage, 0), pages - 1);
    let html = "";
    if (!readerFiltered.length) {
      html = `<div class="rEmptyField">NOTHING IN THE FIELD MATCHES</div>`;
    } else {
      const s = readerFieldPage * ps, e = Math.min(s + ps, readerFiltered.length);
      let cards = "";
      for (let k = s; k < e; k++) {
        const c = KASTEN_CASES[readerFiltered[k]], n = ALL_NOTES[c.i], h = heldInReaderCase(c.i);
        cards += `
          <button class="rCaseCard" data-k="${k}">
            ${h ? `<span class="rHeldBadge">${h}</span>` : ""}
            ${monolineCaseIcon(c.slips.length)}
            <span class="rCaseId">${esc(n.id)}</span>
            <span class="rCaseTopic">${esc(n.topic)} &middot; ${esc(n.type)}</span>
            <span class="rCaseCount">${c.slips.length} SLIPS</span>
          </button>
        `;
      }
      let dots = "";
      if (pages > 1 && pages <= MAX_DOTS) {
        for (let p = 0; p < pages; p++) dots += `<span class="rDot${p === readerFieldPage ? " on" : ""}"></span>`;
      }
      html = `<div class="rFieldGrid">${cards}</div><div class="rDotRail">${dots}</div>`;
    }
    const cls = readerSlideDir > 0 ? "fromRight" : readerSlideDir < 0 ? "fromLeft" : "";
    stage.innerHTML = `<div class="rPane ${cls}">${html}</div>`;
    readerSlideDir = 0;
  } 
  else {
    if (!readerFiltered.length) { readerView = "FIELD"; renderReader(); return; }
    readerCaseK = Math.min(Math.max(readerCaseK, 0), readerFiltered.length - 1);
    const c = KASTEN_CASES[readerFiltered[readerCaseK]], n = ALL_NOTES[c.i];
    let body = "";
    for (let s = 0; s < c.slips.length; s++) {
      const slip = c.slips[s];
      const kind = CODE_FIELD.test(slip.f) ? "code" : HEAD_FIELD.test(slip.f) ? "head" : "text";
      const on = inReaderTray(c.i, slip.f) >= 0;
      const hit = qTokens.length && qTokens.every(t => slip.text.toLowerCase().includes(t));
      body += `
        <div class="rSlip${on ? " on" : ""}${hit ? " hit" : ""}" data-s="${s}" data-kind="${kind}">
          <div class="rfLabel"><span>${esc(slip.f)}</span><span class="rHeldMark">HELD</span></div>
          <div class="rfBody">${hl(slip.text, qTokens)}</div>
        </div>
      `;
    }
    const pct = readerFiltered.length > 1 ? ((readerCaseK + 1) / readerFiltered.length * 100) : 100;
    const cls = readerSlideDir > 0 ? "fromRight" : readerSlideDir < 0 ? "fromLeft" : "";
    stage.innerHTML = `
      <div class="rPane ${cls}">
        <div class="rCaseBar" style="width:${pct}%"></div>
        <div class="rReadScroll" id="rReadScroll">
          <div class="rDoc">
            <div class="rDocHead">
              <span class="rDocId">${esc(n.id)}</span>
              <span class="rDocWhere">${readerCaseK + 1} / ${readerFiltered.length}</span>
            </div>
            <div class="rDocTags">${esc(n.type)} &middot; ${esc(n.topic)} &middot; ${esc(n.case_name)}</div>
            ${body}
          </div>
        </div>
      </div>
    `;
    readerSlideDir = 0;
    if (keepScroll != null) $("#rReadScroll").scrollTop = keepScroll;
  }
}

function syncReaderChip(pulse) {
  const chip = $("#rChip");
  chip.classList.toggle("show", readerTray.length > 0);
  $("#rChipN").textContent = readerTray.length;
  if (pulse) {
    chip.classList.remove("pulse");
    void chip.offsetWidth;
    chip.classList.add("pulse");
  }
  if (!readerTray.length && readerTrayOpen) closeReaderTray();
}

function toggleReaderHold(s) {
  const c = KASTEN_CASES[readerFiltered[readerCaseK]], slip = c.slips[s], at = inReaderTray(c.i, slip.f);
  const el = $("#readerStage").querySelector(`.rSlip[data-s="${s}"]`);
  if (at >= 0) {
    readerTray.splice(at, 1);
    if (el) el.classList.remove("on");
  } else {
    readerTray.push({ i: c.i, f: slip.f });
    if (el) el.classList.add("on");
    if (navigator.vibrate) navigator.vibrate(12);
  }
  syncReaderChip(at < 0);
  if (readerTrayOpen) renderReaderTray();
}

async function copyReaderSlip(s) {
  const c = KASTEN_CASES[readerFiltered[readerCaseK]], slip = c.slips[s], n = ALL_NOTES[c.i];
  try {
    await navigator.clipboard.writeText(n.id + " — " + slip.f + "\n" + slip.text);
    if (navigator.vibrate) navigator.vibrate(12);
    toast("Copied " + slip.f);
  } catch (e) {
    toast("Copy unavailable");
  }
}

function openReaderTray() {
  readerTrayOpen = true;
  renderReaderTray();
  $("#rShade").classList.add("show");
  $("#rTray").classList.add("show");
}

function closeReaderTray() {
  readerTrayOpen = false;
  $("#rShade").classList.remove("show");
  $("#rTray").classList.remove("show");
}

function renderReaderTray() {
  $("#rTrayTitle").textContent = "TRAY · " + readerTray.length + " SLIP" + (readerTray.length === 1 ? "" : "S");
  let html = "";
  for (let t = 0; t < readerTray.length; t++) {
    const e = readerTray[t], n = ALL_NOTES[e.i];
    html += `
      <div class="rtItem" data-t="${t}">
        <div class="rtHandle" data-h="${t}" aria-label="Reorder"><i></i><i></i><i></i></div>
        <button class="rtBody" data-b="${t}"><div class="rtMeta">${esc(n.id)} — ${esc(e.f)}</div><div class="rtText">${esc(valueFor(n, e.f))}</div></button>
        <button class="rtDrop" data-x="${t}" aria-label="Remove">&times;</button>
      </div>
    `;
  }
  $("#rTrayList").innerHTML = html;
}

function readerTrayText() {
  return readerTray.map(e => ALL_NOTES[e.i].id + " — " + e.f + "\n" + valueFor(ALL_NOTES[e.i], e.f)).join("\n\n");
}

function readerTrayMarkdown() {
  let out = "# SLIPCASE TRAY\n\n";
  for (const e of readerTray) {
    const n = ALL_NOTES[e.i];
    out += "## " + n.id + " · " + e.f + "\n\n" + valueFor(n, e.f) + "\n\n---\n\n";
  }
  return out;
}

/* Reader Pointer Handlers */
let readerPress = null;
$("#readerStage").addEventListener("pointerdown", e => {
  const slipEl = e.target.closest(".rSlip");
  readerPress = { x: e.clientX, y: e.clientY, slipEl, long: false, moved: false, timer: 0 };
  if (slipEl && readerView === "READ") {
    readerPress.timer = setTimeout(() => {
      if (readerPress && !readerPress.moved) {
        readerPress.long = true;
        copyReaderSlip(+slipEl.dataset.s);
      }
    }, LONG_PRESS_MS);
  }
});

$("#readerStage").addEventListener("pointermove", e => {
  if (!readerPress) return;
  if (Math.hypot(e.clientX - readerPress.x, e.clientY - readerPress.y) > MOVE_CANCEL_PX) {
    readerPress.moved = true;
    clearTimeout(readerPress.timer);
  }
});

$("#readerStage").addEventListener("pointerup", e => {
  if (!readerPress) return;
  clearTimeout(readerPress.timer);
  const dx = e.clientX - readerPress.x, dy = e.clientY - readerPress.y, p = readerPress;
  readerPress = null;

  if (Math.abs(dx) >= SWIPE_PX && Math.abs(dy) < SWIPE_SLOP) {
    const dir = dx < 0 ? 1 : -1;
    if (readerView === "FIELD") {
      const pages = Math.max(1, Math.ceil(readerFiltered.length / readerPageSize()));
      if (readerFieldPage + dir >= 0 && readerFieldPage + dir < pages) {
        readerFieldPage += dir;
        readerSlideDir = dir;
        renderReader();
      }
      return;
    }
    if (readerCaseK + dir >= 0 && readerCaseK + dir < readerFiltered.length) {
      readerCaseK += dir;
      readerSlideDir = dir;
      renderReader();
    }
    return;
  }
  if (p.moved || p.long) return;

  const card = e.target.closest(".rCaseCard");
  if (card) {
    readerCaseK = +card.dataset.k;
    readerSlideDir = 1;
    readerView = "READ";
    renderReader();
    return;
  }
  const slipEl = e.target.closest(".rSlip");
  if (slipEl && readerView === "READ") toggleReaderHold(+slipEl.dataset.s);
});

$("#readerStage").addEventListener("pointercancel", () => {
  if (readerPress) { clearTimeout(readerPress.timer); readerPress = null; }
});
$("#readerStage").addEventListener("contextmenu", e => {
  if (e.target.closest(".rSlip")) e.preventDefault();
});

$("#rChip").onclick = openReaderTray;
$("#rShade").onclick = closeReaderTray;
$("#rTrayClear").onclick = () => { readerTray = []; syncReaderChip(false); renderReaderTray(); renderReader(); };
$("#rCopyBtn").onclick = async () => {
  try {
    await navigator.clipboard.writeText(readerTrayText());
    toast(`Copied ${readerTray.length} slips`);
  } catch (e) { toast("Copy unavailable"); }
};
$("#rExportBtn").onclick = () => {
  const blob = new Blob([readerTrayMarkdown()], { type: "text/markdown" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "slipcase-tray.md";
  a.click();
  URL.revokeObjectURL(a.href);
  toast(`Exported ${readerTray.length} slips`);
};

$("#rTrayList").addEventListener("click", e => {
  const x = e.target.closest("[data-x]");
  if (x) { readerTray.splice(+x.dataset.x, 1); syncReaderChip(false); renderReaderTray(); renderReader(); return; }
  const b = e.target.closest("[data-b]");
  if (b) b.closest(".rtItem").classList.toggle("open");
});

/* =========================================================
   2. TABLE ENGINE (INFINITE 2D VOID SPATIAL WORKBENCH)
   ========================================================= */
const MAX_CARDS = 400;
const MAX_VISIBLE = 180;
const CARD_W = 280, CARD_H_EST = 230, CULL_PAD = 420;
const ZOOM_MIN = 0.22, ZOOM_MAX = 2.4;
const DRAG_SLOP = 5;
const ROW_BAND = 140;
const SCHEMA = "slipcase.table/1";

let tableCards = [];
let tableView = { x: 0, y: 0, z: 1 };
let tableSelId = null, nextCardId = 1;
const mountedTableCards = new Map();
let tableGest = null;
const tablePts = new Map();

const world = $("#world"), tableStage = $("#tableStage"), grain = $("#grain");

function applyTableView() {
  world.style.transform = `translate(${tableView.x}px,${tableView.y}px) scale(${tableView.z})`;
  const g = Math.max(14, 26 * tableView.z);
  grain.style.backgroundSize = g + "px " + g + "px";
  grain.style.backgroundPosition = (tableView.x % g) + "px " + (tableView.y % g) + "px";
  grain.style.opacity = tableView.z < 0.5 ? 0.35 : 0.75;
  cullTable();
}

function screenToWorld(sx, sy) { return { x: (sx - tableView.x) / tableView.z, y: (sy - tableView.y) / tableView.z }; }
function centerWorld() { return screenToWorld(innerWidth / 2, innerHeight / 2); }

function createCardEl(c, n, slip) {
  const kind = CODE_FIELD.test(c.f) ? "code" : HEAD_FIELD.test(c.f) ? "head" : "text";
  const el = document.createElement("article");
  el.className = "card landing" + (tableSelId === c.id ? " on" : "") + (c.open ? " open" : "");
  el.dataset.id = c.id;
  el.dataset.k = kind;
  el.style.left = c.x + "px";
  el.style.top = c.y + "px";
  el.innerHTML = `<div class="cTab">${esc(c.f)}</div><div class="cMeta"><b>${esc(n.id)}</b> · ${esc(n.type)} · ${esc(n.topic)}</div><div class="cBody">${esc(slip ? slip.text : "—")}</div>`;
  return el;
}

function slipOf(c) {
  const ci = kastenById.get(c.noteId);
  if (ci === undefined) return null;
  const slips = KASTEN_CASES[ci].slips;
  for (let s = 0; s < slips.length; s++) if (slips[s].f === c.f) return slips[s];
  return null;
}

function cullTable() {
  const x0 = -tableView.x / tableView.z - CULL_PAD, y0 = -tableView.y / tableView.z - CULL_PAD;
  const x1 = (innerWidth - tableView.x) / tableView.z + CULL_PAD, y1 = (innerHeight - tableView.y) / tableView.z + CULL_PAD;
  let shown = 0;
  const keep = new Set();

  for (let i = 0; i < tableCards.length; i++) {
    const c = tableCards[i];
    const vis = c.x + CARD_W > x0 && c.x < x1 && c.y + CARD_H_EST > y0 && c.y < y1;
    if (!vis || shown >= MAX_VISIBLE) continue;
    shown++;
    keep.add(c.id);
    if (mountedTableCards.has(c.id)) continue;
    const ci = kastenById.get(c.noteId);
    if (ci === undefined) continue;
    const el = createCardEl(c, ALL_NOTES[ci], slipOf(c));
    world.appendChild(el);
    mountedTableCards.set(c.id, el);
  }

  for (const [id, el] of mountedTableCards) {
    if (!keep.has(id)) {
      el.remove();
      mountedTableCards.delete(id);
    }
  }
}

function refreshTableCard(id) {
  const el = mountedTableCards.get(id);
  if (!el) return;
  const c = tableCards.find(k => k.id === id);
  if (!c) return;
  el.classList.toggle("on", tableSelId === id);
  el.classList.toggle("open", !!c.open);
  el.style.left = c.x + "px";
  el.style.top = c.y + "px";
}

function placeSlipOnTable(noteId, f, at) {
  if (tableCards.length >= MAX_CARDS) { tableStatus("TABLE FULL — " + MAX_CARDS + " SLIPS"); return null; }
  const c = { id: nextCardId++, noteId, f, x: Math.round(at.x), y: Math.round(at.y), open: false };
  tableCards.push(c);
  selectTableCard(c.id);
  cullTable();
  autosaveTable();
  return c;
}

function dealCaseOnTable(ci) {
  const c = KASTEN_CASES[ci];
  if (!c) return;
  const base = centerWorld();
  let placed = 0;
  const cap = Math.min(c.slips.length, MAX_CARDS - tableCards.length);
  for (let s = 0; s < cap; s++) {
    const col = Math.floor(s / 4), row = s % 4;
    placeSlipOnTable(c.id, c.slips[s].f, { x: base.x - CARD_W / 2 + col * (CARD_W + 26), y: base.y - 200 + row * (CARD_H_EST + 22) });
    placed++;
  }
  tableStatus("DEALT " + placed + " SLIPS · " + c.id);
  closeTableDrawer();
}

function removeSelectedTableCard() {
  if (tableSelId === null) return;
  const i = tableCards.findIndex(c => c.id === tableSelId);
  if (i < 0) return;
  tableCards.splice(i, 1);
  const el = mountedTableCards.get(tableSelId);
  if (el) { el.remove(); mountedTableCards.delete(tableSelId); }
  selectTableCard(null);
  autosaveTable();
  tableStatus("RETURNED TO THE CASE");
}

function selectTableCard(id) {
  const prev = tableSelId;
  tableSelId = id;
  if (prev !== null) refreshTableCard(prev);
  if (id !== null) refreshTableCard(id);
  $("#selGrp").style.display = id === null ? "none" : "flex";
  if (id !== null) {
    const c = tableCards.find(k => k.id === id);
    $("#expandBtn").textContent = c && c.open ? "COLLAPSE" : "EXPAND";
  }
}

function toggleOpenTableCard() {
  if (tableSelId === null) return;
  const c = tableCards.find(k => k.id === tableSelId);
  if (!c) return;
  c.open = !c.open;
  refreshTableCard(c.id);
  $("#expandBtn").textContent = c.open ? "COLLAPSE" : "EXPAND";
  autosaveTable();
}

tableStage.addEventListener("pointerdown", e => {
  tablePts.set(e.pointerId, { x: e.clientX, y: e.clientY });
  if (tablePts.size === 2) {
    const it = [...tablePts.values()];
    tableGest = { mode: "pinch", d0: Math.hypot(it[0].x - it[1].x, it[0].y - it[1].y), z0: tableView.z, cx: (it[0].x + it[1].x) / 2, cy: (it[0].y + it[1].y) / 2, vx: tableView.x, vy: tableView.y };
    tableStage.classList.remove("panning");
    return;
  }
  if (tablePts.size > 2) return;
  const el = e.target.closest(".card");
  if (el) {
    const c = tableCards.find(k => k.id === +el.dataset.id);
    if (!c) return;
    tableGest = { mode: "card", id: c.id, el, sx: e.clientX, sy: e.clientY, ox: c.x, oy: c.y, moved: false };
  } else {
    tableGest = { mode: "pan", sx: e.clientX, sy: e.clientY, ox: tableView.x, oy: tableView.y, moved: false };
    tableStage.classList.add("panning");
  }
  tableStage.setPointerCapture(e.pointerId);
});

tableStage.addEventListener("pointermove", e => {
  if (!tablePts.has(e.pointerId)) return;
  tablePts.set(e.pointerId, { x: e.clientX, y: e.clientY });
  if (!tableGest) return;
  if (tableGest.mode === "pinch") {
    const it = [...tablePts.values()];
    if (it.length < 2) return;
    const d = Math.hypot(it[0].x - it[1].x, it[0].y - it[1].y);
    if (tableGest.d0 <= 0) return;
    const z = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, tableGest.z0 * (d / tableGest.d0))), r = z / tableGest.z0;
    tableView.z = z;
    tableView.x = tableGest.cx - (tableGest.cx - tableGest.vx) * r;
    tableView.y = tableGest.cy - (tableGest.cy - tableGest.vy) * r;
    applyTableView();
    return;
  }
  const dx = e.clientX - tableGest.sx, dy = e.clientY - tableGest.sy;
  if (!tableGest.moved && Math.hypot(dx, dy) < DRAG_SLOP) return;
  if (!tableGest.moved) {
    tableGest.moved = true;
    if (tableGest.mode === "card") tableGest.el.classList.add("drag");
  }
  if (tableGest.mode === "pan") {
    tableView.x = tableGest.ox + dx;
    tableView.y = tableGest.oy + dy;
    applyTableView();
  } else {
    const c = tableCards.find(k => k.id === tableGest.id);
    if (!c) return;
    c.x = Math.round(tableGest.ox + dx / tableView.z);
    c.y = Math.round(tableGest.oy + dy / tableView.z);
    tableGest.el.style.left = c.x + "px";
    tableGest.el.style.top = c.y + "px";
  }
});

tableStage.addEventListener("pointerup", e => {
  tablePts.delete(e.pointerId);
  tableStage.classList.remove("panning");
  if (!tableGest) return;
  if (tableGest.mode === "card") {
    tableGest.el.classList.remove("drag");
    if (!tableGest.moved) selectTableCard(tableGest.id === tableSelId ? null : tableGest.id);
    else autosaveTable();
  } else if (tableGest.mode === "pan" && !tableGest.moved) {
    selectTableCard(null);
  }
  tableGest = null;
});

tableStage.addEventListener("pointercancel", e => {
  tablePts.delete(e.pointerId);
  tableStage.classList.remove("panning");
  tableGest = null;
});

tableStage.addEventListener("wheel", e => {
  e.preventDefault();
  if (e.ctrlKey || e.metaKey) {
    const z = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, tableView.z * Math.exp(-e.deltaY * 0.0016))), r = z / tableView.z;
    tableView.x = e.clientX - (e.clientX - tableView.x) * r;
    tableView.y = e.clientY - (e.clientY - tableView.y) * r;
    tableView.z = z;
  } else {
    tableView.x -= e.deltaX;
    tableView.y -= e.deltaY;
  }
  applyTableView();
}, { passive: false });

function fitTable() {
  if (!tableCards.length) {
    tableView = { x: innerWidth / 2 - 140, y: innerHeight / 2 - 120, z: 1 };
    applyTableView();
    tableStatus("EMPTY TABLE");
    return;
  }
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for (let i = 0; i < tableCards.length; i++) {
    const c = tableCards[i];
    if (c.x < x0) x0 = c.x;
    if (c.y < y0) y0 = c.y;
    if (c.x + CARD_W > x1) x1 = c.x + CARD_W;
    if (c.y + CARD_H_EST > y1) y1 = c.y + CARD_H_EST;
  }
  const pad = 70, w = x1 - x0 + pad * 2, h = y1 - y0 + pad * 2;
  tableView.z = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, Math.min(innerWidth / w, innerHeight / h)));
  tableView.x = innerWidth / 2 - ((x0 + x1) / 2) * tableView.z;
  tableView.y = innerHeight / 2 - ((y0 + y1) / 2) * tableView.z;
  applyTableView();
}

function readingOrder() {
  const out = tableCards.slice();
  out.sort((a, b) => {
    const ra = Math.floor(a.y / ROW_BAND), rb = Math.floor(b.y / ROW_BAND);
    return ra !== rb ? ra - rb : a.x - b.x;
  });
  return out;
}

async function copyReadingOrder() {
  if (!tableCards.length) { tableStatus("NOTHING ON THE TABLE"); return; }
  const ord = readingOrder();
  let out = "";
  for (let i = 0; i < ord.length; i++) {
    const c = ord[i], slip = slipOf(c);
    out += c.noteId + " — " + c.f + "\n" + (slip ? slip.text : "") + "\n\n";
  }
  try {
    await navigator.clipboard.writeText(out.trimEnd());
    tableStatus("COPIED " + ord.length + " SLIPS IN ARRANGEMENT ORDER");
  } catch (err) {
    tableStatus("COPY UNAVAILABLE");
  }
}

function boardData() { return { schema: SCHEMA, saved: new Date().toISOString(), view: tableView, cards: tableCards }; }
function downloadFile(name, text, mime) {
  const blob = new Blob([text], { type: mime || "application/json" });
  const url = URL.createObjectURL(blob), a = document.createElement("a");
  a.href = url; a.download = name; document.body.appendChild(a); a.click();
  a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function saveTableFile() {
  const stamp = new Date().toISOString().slice(0, 10).replace(/-/g, "");
  downloadFile("slipcase-table-" + stamp + ".json", JSON.stringify(boardData(), null, 1));
  tableStatus("SAVED · " + tableCards.length + " SLIPS");
}

function loadTableBoard(obj) {
  if (!obj || obj.schema !== SCHEMA || !Array.isArray(obj.cards)) return false;
  const cap = Math.min(obj.cards.length, MAX_CARDS);
  tableCards = []; nextCardId = 1;
  for (let i = 0; i < cap; i++) {
    const c = obj.cards[i];
    if (!c || typeof c.noteId !== "string" || typeof c.f !== "string") continue;
    tableCards.push({ id: nextCardId++, noteId: c.noteId, f: c.f, x: +c.x || 0, y: +c.y || 0, open: !!c.open });
  }
  if (obj.view && isFinite(obj.view.z)) tableView = { x: +obj.view.x || 0, y: +obj.view.y || 0, z: Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, +obj.view.z || 1)) };
  for (const [, el] of mountedTableCards) el.remove();
  mountedTableCards.clear(); selectTableCard(null); applyTableView();
  return true;
}

function autosaveTable() {
  try { localStorage.setItem("slipcase.table", JSON.stringify(boardData())); }
  catch (err) {}
}

function restoreTable() {
  try {
    const raw = localStorage.getItem("slipcase.table");
    return raw ? loadTableBoard(JSON.parse(raw)) : false;
  } catch (err) { return false; }
}

function shareTableLink() {
  if (!tableCards.length) { tableStatus("NOTHING TO SHARE"); return; }
  try {
    const packed = btoa(unescape(encodeURIComponent(JSON.stringify({ schema: SCHEMA, view: tableView, cards: tableCards.map(c => ({ noteId: c.noteId, f: c.f, x: c.x, y: c.y, open: c.open })) }))));
    const url = location.origin + location.pathname + "#t=" + packed;
    navigator.clipboard.writeText(url).then(
      () => tableStatus("LINK COPIED · " + tableCards.length + " SLIPS"),
      () => { location.hash = "t=" + url.split("#t=")[1]; tableStatus("LINK IN ADDRESS BAR"); }
    );
  } catch (err) { tableStatus("SHARE FAILED — USE SAVE"); }
}

let tableStatusTimer = 0;
function tableStatus(msg) {
  clearTimeout(tableStatusTimer);
  $("#tableStatus").textContent = msg;
  tableStatusTimer = setTimeout(() => { $("#tableStatus").textContent = tableCards.length ? tableCards.length + " SLIPS ON THE TABLE" : "EMPTY TABLE"; }, 2600);
}

let drawerCaseIdx = -1, drawerQueryTokens = [], drawerTimer = 0;

function placedSet() {
  const s = new Set();
  for (let i = 0; i < tableCards.length; i++) s.add(tableCards[i].noteId + "|" + tableCards[i].f);
  return s;
}

function renderTableDrawer() {
  const visibleCases = (selectedCaseIdx === -1) ? KASTEN_CASES : KASTEN_CASES.filter(c => c.case_idx === selectedCaseIdx);
  const shown = [];
  for (let k = 0; k < visibleCases.length && shown.length < 80; k++) {
    const c = visibleCases[k];
    if (!drawerQueryTokens.length || drawerQueryTokens.every(t => c.low.includes(t))) shown.push(c);
  }
  let html = `<div class="caseRow">`;
  for (let s = 0; s < shown.length; s++) {
    const c = shown[s], n = ALL_NOTES[c.i];
    const isCur = drawerCaseIdx === c.i;
    html += `<button class="caseBtn${isCur ? " on" : ""}" data-c="${c.i}">${monolineCaseIcon(c.slips.length)}<span class="cid">${esc(n.id)}</span><span class="ctp">${esc(n.topic)}</span></button>`;
  }
  html += `</div>`;

  if (drawerCaseIdx >= 0 && KASTEN_CASES[drawerCaseIdx]) {
    const c = KASTEN_CASES[drawerCaseIdx], n = ALL_NOTES[c.i], held = placedSet();
    html += `<div class="fan"><div class="fanHead"><span><b>${esc(n.id)}</b> · ${esc(n.type)} · ${c.slips.length} SLIPS</span><button class="tbtn" data-deal="1">DEAL ALL</button></div><div class="chips">`;
    for (let s = 0; s < c.slips.length; s++) {
      const on = held.has(c.id + "|" + c.slips[s].f);
      html += `<button class="chip${on ? " placed" : ""}" data-f="${esc(c.slips[s].f)}">${esc(c.slips[s].f)}</button>`;
    }
    html += `</div></div>`;
  }
  $("#dBody").innerHTML = html || `<div class="dEmpty">NOTHING MATCHES</div>`;
}

$("#dBody").addEventListener("click", e => {
  const cb = e.target.closest(".caseBtn");
  if (cb) { drawerCaseIdx = +cb.dataset.c; renderTableDrawer(); return; }
  if (e.target.closest("[data-deal]")) { dealCaseOnTable(drawerCaseIdx); return; }
  const chip = e.target.closest(".chip");
  if (chip && drawerCaseIdx >= 0) {
    const c = KASTEN_CASES[drawerCaseIdx], base = centerWorld();
    const jx = (Math.random() - 0.5) * 90, jy = (Math.random() - 0.5) * 70;
    placeSlipOnTable(c.id, chip.dataset.f, { x: base.x - CARD_W / 2 + jx, y: base.y - CARD_H_EST / 2 + jy });
    renderTableDrawer();
    tableStatus("PLACED · " + chip.dataset.f);
  }
});

function openTableDrawer() {
  $("#drawer").classList.add("open");
  $("#drawerScrim").classList.add("open");
  renderTableDrawer();
}

function closeTableDrawer() {
  $("#drawer").classList.remove("open");
  $("#drawerScrim").classList.remove("open");
}

$("#drawerBtn").onclick = openTableDrawer;
$("#drawerClose").onclick = closeTableDrawer;
$("#drawerScrim").onclick = closeTableDrawer;
$("#fitBtn").onclick = fitTable;
$("#readBtn").onclick = copyReadingOrder;
$("#saveBtn").onclick = saveTableFile;
$("#shareBtn").onclick = shareTableLink;
$("#expandBtn").onclick = toggleOpenTableCard;
$("#removeBtn").onclick = removeSelectedTableCard;

$("#openBtn").onclick = () => { $("#filePick").click(); };
$("#filePick").addEventListener("change", e => {
  const f = e.target.files && e.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try {
      const obj = JSON.parse(String(r.result));
      if (loadTableBoard(obj)) { tableStatus("TABLE OPENED · " + tableCards.length + " SLIPS"); fitTable(); autosaveTable(); }
      else tableStatus("NOT A VALID SLIPCASE TABLE FILE");
    } catch (err) { tableStatus("NOT VALID JSON"); }
  };
  r.readAsText(f);
});

$("#dSearch").addEventListener("input", e => {
  clearTimeout(drawerTimer);
  drawerTimer = setTimeout(() => {
    drawerQueryTokens = e.target.value.trim().toLowerCase().split(/\s+/).filter(Boolean).slice(0, 8);
    drawerCaseIdx = -1;
    renderTableDrawer();
  }, 110);
});

/* =========================================================
   3. LINES MODULE (ROW-BY-ROW INSPECTOR)
   ========================================================= */
function rowKey(id, field) { return id + "|||" + field; }
function unpack(key) { const i = key.indexOf("|||"); return [key.slice(0,i), key.slice(i+3)]; }

function fieldsFor(n) {
  if (lineFilter === "ALL") return FIELD_ORDER.filter(f => valueFor(n, f));
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

  notes.forEach(n => {
    const fields = fieldsFor(n).filter(f => lineMatches(n, f, q));
    if (!fields.length) return;
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
      const code = CODE_FIELD.test(field);
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
  });
}

function toggleLine(key) {
  if (selectedLines.has(key)) selectedLines.delete(key);
  else selectedLines.add(key);
  const el = $(`.lineRow[data-key="${CSS.escape(key)}"]`);
  if (el) el.classList.toggle("selected", selectedLines.has(key));
  updateSelectionUI();
}

window.selectWholeZettel = function(id) {
  const notes = getActiveNotes();
  const n = notes.find(x => x.id === id);
  if (!n) return;
  const keys = FIELD_ORDER.filter(f => valueFor(n, f)).map(f => rowKey(id, f));
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
  ALL_NOTES.forEach(n => {
    FIELD_ORDER.forEach(field => {
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
      <div class="stackMeta">${esc(x.n.id)} &middot; ${esc(x.field)} &middot; ${esc(x.n.type)}</div>
      <div class="stackText">${esc(x.text)}</div>
    </article>
  `).join("");
  $("#stack").classList.add("open");
}

function closeStack() { $("#stack").classList.remove("open"); }

async function copySelectedLines() {
  const items = getSelectedItems();
  const text = items.map(x => `${x.n.id} [${x.field}]\n${x.text}`).join("\n\n---\n\n");
  try {
    await navigator.clipboard.writeText(text);
    toast("Selected lines copied");
  } catch(e) { toast("Clipboard copy failed"); }
}

function setLineFilter(f) {
  lineFilter = f;
  $$("#linesSubtoolbar .subchip").forEach(b => b.classList.toggle("on", b.dataset.filter === f));
  $("#filterScrim").classList.remove("open");
  renderLines();
}

function openFilterSheet() {
  $("#sheetGrid").innerHTML = FIELD_ORDER.map(f => `
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
   4. GRAPH ENGINE
   ========================================================= */
let graphMode = "all";
let graphAnimId = null, graphNodes = [], graphLinks = [];
let graphTransform = { x: 0, y: 0, k: 1 };
let isDraggingGraph = false, graphDragStart = { x: 0, y: 0 };
let hoveredNode = null, selectedNode = null;

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
  const cx = w / 2, cy = h / 2;
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
      vx: 0, vy: 0, radius: 16
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
        vx: 0, vy: 0, radius: 4.5
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
    const dx = l.target.x - l.source.x, dy = l.target.y - l.source.y;
    const dist = Math.hypot(dx, dy) || 1;
    const targetDist = l.type === 'contains' ? 50 : l.type === 'case_bridge' ? 140 : 80;
    const force = (dist - targetDist) * 0.003;
    const fx = (dx / dist) * force, fy = (dy / dist) * force;
    l.source.vx += fx; l.source.vy += fy;
    l.target.vx -= fx; l.target.vy -= fy;
  }

  for (let i = 0; i < graphNodes.length; i++) {
    const n1 = graphNodes[i];
    for (let j = i + 1; j < Math.min(graphNodes.length, i + 60); j++) {
      const n2 = graphNodes[j];
      const dx = n2.x - n1.x, dy = n2.y - n1.y;
      const dist = Math.hypot(dx, dy) || 1;
      const minDist = n1.radius + n2.radius + 15;
      if (dist < minDist) {
        const force = (minDist - dist) * 0.04;
        const fx = (dx / dist) * force, fy = (dy / dist) * force;
        n1.vx -= fx; n1.vy -= fy;
        n2.vx += fx; n2.vy += fy;
      }
    }
    n1.x += n1.vx; n1.y += n1.vy;
    n1.vx *= 0.88; n1.vy *= 0.88;
  }

  ctx.save();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.scale(dpr, dpr);
  ctx.translate(graphTransform.x, graphTransform.y);
  ctx.scale(graphTransform.k, graphTransform.k);

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
      if (graphTransform.k > 1.2 || isHovered || isSelected) {
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
    graphDragStart = { x: e.clientX - graphTransform.x, y: e.clientY - graphTransform.y };
  };
  window.onmousemove = e => {
    if (!isDown) {
      const rect = canvas.getBoundingClientRect();
      const mx = (e.clientX - rect.left - graphTransform.x) / graphTransform.k;
      const my = (e.clientY - rect.top - graphTransform.y) / graphTransform.k;
      hoveredNode = graphNodes.find(n => Math.hypot(n.x - mx, n.y - my) <= n.radius + 4) || null;
      canvas.style.cursor = hoveredNode ? "pointer" : "grab";
      return;
    }
    graphTransform.x = e.clientX - graphDragStart.x;
    graphTransform.y = e.clientY - graphDragStart.y;
  };
  window.onmouseup = () => { isDown = false; };

  canvas.onclick = e => {
    const rect = canvas.getBoundingClientRect();
    const mx = (e.clientX - rect.left - graphTransform.x) / graphTransform.k;
    const my = (e.clientY - rect.top - graphTransform.y) / graphTransform.k;
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
    graphTransform.k = Math.max(0.3, Math.min(4, graphTransform.k * factor));
  };
}

function showGraphInspector(n) {
  const panel = $("#graphInspectorPanel");
  panel.classList.add("open");
  if (n.type === 'case') {
    $("#graphInspAccession").textContent = `${n.accession} · ${n.meta_field}`;
    $("#graphInspTitle").textContent = n.label;
    $("#graphInspDesc").textContent = `Workspace containing ${n.card_count} atomic zettel slips and ${n.pdf_count} research PDFs.`;
    $("#graphInspOpenBtn").onclick = () => { selectCase(n.case_idx); setTab("lines"); };
    $("#graphInspReaderBtn").onclick = () => { selectCase(n.case_idx); setTab("reader"); };
  } else {
    $("#graphInspAccession").textContent = `SLIP · ${n.card_type} · ${n.topic}`;
    $("#graphInspTitle").textContent = n.label;
    $("#graphInspDesc").textContent = `Contained in slipcase #${n.case_idx + 1}.`;
    $("#graphInspOpenBtn").onclick = () => { selectCase(n.case_idx); setTab("lines"); };
    $("#graphInspReaderBtn").onclick = () => { selectCase(n.case_idx); setTab("reader"); };
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
  graphTransform = { x: 0, y: 0, k: 1 };
  initGraphEngine();
};

/* NESTED MATRIX */
function renderMatrix() {
  const container = $("#matrixClusterContainer");
  let html = "";

  for (const [clusterName, folderList] of Object.entries(GRAPH.meta_clusters)) {
    const clusterCases = CASES_DATA.filter(c => folderList.includes(c.id));
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
      const idx = CASES_DATA.findIndex(x => x.id === c.id);
      html += `
        <div class="matrix-case-row" onclick="selectCase(${idx}); setTab('reader');">
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

/* PDFS */
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

/* MAPS */
function renderMaps() {
  const caseData = selectedCaseIdx === -1 ? CASES_DATA[0] : CASES_DATA[selectedCaseIdx];
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
  const caseData = selectedCaseIdx === -1 ? CASES_DATA[0] : CASES_DATA[selectedCaseIdx];
  const docText = caseData?.specials?.[currentActiveDocKey] || "";
  try {
    await navigator.clipboard.writeText(docText);
    toast("Document copied");
  } catch(e) { toast("Copy failed"); }
};

$("#downloadDocBtn").onclick = () => {
  const caseData = selectedCaseIdx === -1 ? CASES_DATA[0] : CASES_DATA[selectedCaseIdx];
  const docText = caseData?.specials?.[currentActiveDocKey] || "";
  const blob = new Blob([docText], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = currentActiveDocKey || "document.txt";
  a.click();
  toast(`Downloaded ${currentActiveDocKey}`);
};

/* PROMPTS */
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
  } catch(e) { toast("Copy failed"); }
};

window.copyPromptText = async function() {
  const p = PROMPTS[currentPromptIdx];
  try {
    await navigator.clipboard.writeText(p.text);
    toast(`Copied ${p.title} ${p.ver}`);
  } catch(e) { toast("Copy failed"); }
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

/* SEARCH & SHORTCUTS */
$("#search").addEventListener("input", () => {
  if (currentTab === "reader") { readerFieldPage = 0; renderReader(); }
  if (currentTab === "lines") renderLines();
  if (currentTab === "pdfs") renderPdfs();
});

document.addEventListener("keydown", e => {
  if (e.key === "/" && document.activeElement !== $("#search") && document.activeElement !== $("#dSearch")) {
    e.preventDefault();
    $("#search").focus();
  }
  if (e.key === "Escape") {
    closeStack();
    closePdfModal();
    closeGraphInspector();
    closeTableDrawer();
    closeReaderTray();
    window.closeThreeInspector?.();
    $("#filterScrim").classList.remove("open");
    $("#caseScrim").classList.remove("open");
  }
  if (currentTab === "reader") {
    if (e.key === "t" && readerTray.length) { readerTrayOpen ? closeReaderTray() : openReaderTray(); }
    const dir = e.key === "ArrowRight" || e.key === "j" ? 1 : e.key === "ArrowLeft" || e.key === "k" ? -1 : 0;
    if (dir) {
      if (readerView === "FIELD") {
        const pages = Math.max(1, Math.ceil(readerFiltered.length / readerPageSize()));
        if (readerFieldPage + dir >= 0 && readerFieldPage + dir < pages) {
          readerFieldPage += dir;
          readerSlideDir = dir;
          renderReader();
        }
      } else if (readerCaseK + dir >= 0 && readerCaseK + dir < readerFiltered.length) {
        readerCaseK += dir;
        readerSlideDir = dir;
        renderReader();
      }
    }
  }
  if (currentTab === "table") {
    if (e.key === "f") fitTable();
    if (e.key === "s" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); saveTableFile(); }
    if ((e.key === "Backspace" || e.key === "Delete") && tableSelId !== null) { e.preventDefault(); removeSelectedTableCard(); }
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

(function bootTable() {
  const reg = document.createElement("div");
  reg.className = "reg";
  reg.style.left = "-40px";
  reg.style.top = "-40px";
  reg.innerHTML = `<i class="h"></i><i class="v"></i>`;
  world.appendChild(reg);

  let restored = false;
  if (location.hash.startsWith("#t=")) {
    try {
      restored = loadTableBoard(JSON.parse(decodeURIComponent(escape(atob(location.hash.slice(3))))));
    } catch (err) {}
  }
  if (!restored && !restoreTable()) {
    tableView = { x: innerWidth / 2 - 140, y: innerHeight / 2 - 120, z: 1 };
  }
  applyTableView();
  $("#tableStatus").textContent = tableCards.length ? tableCards.length + " SLIPS ON THE TABLE" : "EMPTY TABLE";

  setTimeout(() => {
    $("#loader").classList.add("done");
    setTimeout(() => { const l = $("#loader"); if (l) l.remove(); }, 420);
    if (!tableCards.length) tableStatus("PRESS SLIPCASES TO LAY OUT SLIPS");
  }, 950);
})();

syncReaderChip(false);
updateActiveCaseLabel();
setTab("reader");
})();
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

    root.add(outlinedBox(width, panel, depth, [0, panel / 2, 0]));
    root.add(outlinedBox(panel, height, depth, [-width / 2 + panel / 2, height / 2, 0]));
    root.add(outlinedBox(panel, height, depth, [width / 2 - panel / 2, height / 2, 0]));
    root.add(outlinedBox(width, height, panel, [0, height / 2, -depth / 2 + panel / 2]));

    const frontHeight = height * 0.68;
    root.add(outlinedBox(width, frontHeight, panel, [0, frontHeight / 2, depth / 2 - panel / 2]));

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

    const CASES_DATA = window.CASES_DATA || [];

    if (threeViewMode === "all") {
      const cols = 6;
      const spacingX = 3.2;
      const spacingZ = 2.8;

      CASES_DATA.forEach((c, idx) => {
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
      controls?.target.set(0, 0.8, 0);
    } else {
      const targetCase = selectedCaseIdx === -1 ? CASES_DATA[0] : CASES_DATA[selectedCaseIdx];
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
      controls?.target.set(0, 0.8, 0);
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
        const CASES_DATA = window.CASES_DATA || [];
        const cIdx = CASES_DATA.findIndex(x => x.id === c.id);
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
    document.getElementById("threeInspLinesBtn").onclick = () => { selectCase(cIdx); setTab("lines"); };
    document.getElementById("threeInspReaderBtn").onclick = () => { selectCase(cIdx); setTab("reader"); };
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

print('Successfully re-indexed and wrote index.html with Reader v3, Table, Lines, 3D, Graph, Matrix, PDFs, Maps, and Prompts.')
