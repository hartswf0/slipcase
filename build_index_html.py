import os, glob, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
slipcases_dir = os.path.join(BASE_DIR, 'slipcases')
folders = sorted([f for f in os.listdir(slipcases_dir) if os.path.isdir(os.path.join(slipcases_dir, f)) and not f.startswith('.')])

cases_data = []
all_notes = []
all_pdfs = []

def parse_card_file(filepath, case_id, case_name, idx):
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
    if '\n' in cid:
        cid = cid.split('\n')[0].strip()
    if not cid:
        cid = os.path.splitext(os.path.basename(filepath))[0]
        
    title = sections.get('TITLE') or sections.get('HEADLINE') or sections.get('QUESTION') or os.path.splitext(os.path.basename(filepath))[0]
    if '\n' in title:
        title = title.split('\n')[0].strip()
        
    card_type = sections.get('TYPE') or sections.get('OPERATOR') or 'ZETTEL'
    if '\n' in card_type:
        card_type = card_type.split('\n')[0].strip()
        
    topic = sections.get('TOPIC') or sections.get('THEME') or sections.get('PLATFORM') or case_name
    if '\n' in topic:
        topic = topic.split('\n')[0].strip()
        
    symbol = sections.get('SYMBOL') or (card_type[:2].capitalize() if card_type else 'Zt')
    if '\n' in symbol:
        symbol = symbol.split('\n')[0].strip()
        
    source = sections.get('SOURCE') or sections.get('SOURCES') or ''
    passage = sections.get('PASSAGE') or sections.get('EVIDENCE') or sections.get('EXCERPT') or ''
    
    fields = {}
    known_keys = {'ID', 'TITLE', 'TYPE', 'TOPIC', 'SYMBOL', 'SOURCE', 'PASSAGE', 'ZETTEL ID', 'HEADLINE', 'OPERATOR', 'THEME'}
    for k, v in sections.items():
        if k not in known_keys and v:
            fields[k] = v
            
    if 'QUESTION' in sections and 'QUESTION' not in fields:
        fields['QUESTION'] = sections['QUESTION']
        
    return {
        'id': cid,
        'num': idx + 1,
        'title': title,
        'type': card_type,
        'topic': topic,
        'symbol': symbol,
        'source': source,
        'passage': passage,
        'case_id': case_id,
        'case_name': case_name,
        'fields': fields,
        'raw': content
    }

card_global_idx = 0
for folder in folders:
    w = os.path.join(slipcases_dir, folder)
    clean_name = folder.replace('__', ' — ').replace('_', ' ').replace('-', ' ')
    
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
            'case_name': clean_name,
            'size': os.path.getsize(p),
            'is_paper': not ('_RESOURCES' in p or 'scan' in p.lower())
        }
        pdf_list.append(p_obj)
        all_pdfs.append(p_obj)
        
    # Text cards
    txt_files = sorted([f for f in glob.glob(f'{w}/*.txt') if not os.path.basename(f).startswith('000__')])
    case_notes = []
    for tf in txt_files:
        card = parse_card_file(tf, folder, clean_name, card_global_idx)
        card_global_idx += 1
        case_notes.append(card)
        all_notes.append(card)
        
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
        'name': clean_name,
        'folder': folder,
        'pdf_count': len(pdf_list),
        'pdfs': pdf_list,
        'card_count': len(case_notes),
        'cards': case_notes,
        'specials': specials
    })

# Save standalone JSON data
with open(os.path.join(BASE_DIR, 'slipcases.json'), 'w') as f:
    json.dump(cases_data, f, indent=2)

from build_data import prompts_data

html_template = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f5f2eb">
<link rel="icon" type="image/png" href="slipcase.png">
<title>SLIPCASE — Portable Research Field &amp; Prompt Operator</title>
<style>
:root {
  --bg: #f5f2eb;
  --paper: #fffefa;
  --ink: #171717;
  --muted: #777168;
  --line: #d9d4ca;
  --line-light: #ece8df;
  --blue: #2455ff;
  --blue-soft: #edf2ff;
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

/* Header */
header {
  position: absolute;
  z-index: 30;
  top: 0;
  left: 0;
  right: 0;
  height: calc(58px + var(--top));
  padding: var(--top) 12px 0;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 8px;
  align-items: center;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
}
.brand {
  height: 42px;
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--ink);
  display: flex;
  align-items: center;
  padding: 0 4px;
}
.search {
  height: 42px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--paper);
  padding: 0 12px;
  outline: 0;
  min-width: 0;
  font-size: 13.5px;
  color: var(--ink);
}
.search:focus {
  border-color: var(--blue);
}
.filterBtn {
  height: 42px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--paper);
  padding: 0 11px;
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--ink);
  white-space: nowrap;
}

/* Mode Navigation Bar */
.toolbar {
  position: absolute;
  z-index: 29;
  left: 0;
  right: 0;
  top: calc(58px + var(--top));
  height: 46px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
  scrollbar-width: none;
}
.toolbar::-webkit-scrollbar { display: none; }

.chip {
  flex: 0 0 auto;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper);
  padding: 7px 11px;
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted);
  text-transform: uppercase;
}
.chip.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}
.chip-case {
  border-color: var(--blue);
  color: var(--blue);
  background: var(--blue-soft);
  max-width: 220px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Secondary Filter Bar for LINES */
.subtoolbar {
  position: absolute;
  z-index: 28;
  left: 0;
  right: 0;
  top: calc(104px + var(--top));
  height: 38px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  gap: 5px;
  overflow-x: auto;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
  scrollbar-width: none;
}
.subtoolbar::-webkit-scrollbar { display: none; }
.subchip {
  flex: 0 0 auto;
  border: 1px solid var(--line-light);
  border-radius: 6px;
  background: var(--bg);
  padding: 4px 8px;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: .05em;
  color: var(--muted);
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
  top: calc(142px + var(--top));
  bottom: calc(14px + var(--bottom));
  left: 0;
  right: 0;
  overflow-y: auto;
  background: var(--paper);
  scrollbar-width: none;
}
main.top-short {
  top: calc(104px + var(--top));
}
main::-webkit-scrollbar { display: none; }

/* View Panes */
.pane { display: none; }
.pane.active { display: block; }

/* LINES MODE */
.zgroup {
  border-bottom: 8px solid var(--bg);
}
.zhead {
  position: sticky;
  top: 0;
  z-index: 5;
  background: rgba(255,254,250,.97);
  backdrop-filter: blur(12px);
  padding: 11px 12px 10px;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  align-items: start;
  cursor: pointer;
}
.zid {
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--muted);
  margin-bottom: 3px;
  text-transform: uppercase;
}
.ztitle {
  font-size: 14.5px;
  line-height: 1.22;
  font-weight: 800;
  letter-spacing: -.02em;
}
.ztype {
  font-size: 9px;
  font-weight: 850;
  color: var(--muted);
  white-space: nowrap;
  border: 1px solid var(--line);
  padding: 2px 6px;
  border-radius: 4px;
  background: var(--bg);
}

.lineRow {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 12px;
  padding: 13px 12px;
  border-bottom: 1px solid #e8e3da;
  background: var(--paper);
  position: relative;
  user-select: none;
  cursor: pointer;
}
.lineRow:last-child { border-bottom: 0; }
.lineRow.selected { background: var(--ink); color: #fff; }
.lineRow.selected .fieldName { color: #bdb8af; }
.fieldName {
  font-size: 8.5px;
  line-height: 1.3;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--muted);
  text-transform: uppercase;
  padding-top: 3px;
  word-break: break-word;
}
.lineText {
  font-family: ui-serif, Georgia, serif;
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
.lineRow[data-field="QUESTION"] .lineText { font-size: 19px; line-height: 1.25; color: var(--ink); }
.lineRow.selected[data-field="QUESTION"] .lineText { color: #fff; }
.lineRow[data-field="DEEPER QUESTION"] .lineText { font-size: 17.5px; line-height: 1.28; }
.lineRow[data-field="PASSAGE"] .lineText { font-size: 17px; }
.lineRow.code .lineText {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 12px;
  line-height: 1.55;
  background: #f2eee6;
  padding: 10px;
  border-radius: 8px;
  overflow-x: auto;
}
.lineRow.selected.code .lineText { background: #272727; color: #f0f0f0; }

.empty {
  padding: 60px 18px;
  text-align: center;
  color: var(--muted);
  font-size: 13.5px;
  line-height: 1.6;
}

/* Floating Selection Bar */
.selection {
  position: absolute;
  z-index: 40;
  left: 10px;
  right: 10px;
  bottom: calc(8px + var(--bottom));
  min-height: 56px;
  border-radius: 16px;
  background: var(--ink);
  color: #fff;
  display: none;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 8px;
  padding: 7px 8px 7px 14px;
  box-shadow: 0 14px 40px rgba(0,0,0,.18);
}
.selection.open { display: grid; }
.selCount { font-size: 11.5px; font-weight: 800; letter-spacing: .05em; }
.selection button {
  height: 40px;
  padding: 0 12px;
  border-radius: 11px;
  background: #2a2a2a;
  color: #fff;
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.selection .primary { background: #fff; color: #111; }

/* Stack Sheet (Continuous Reader) */
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
  padding: var(--top) 10px 0;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 48px 1fr 48px;
  align-items: center;
  background: var(--paper);
}
.stackHead button { height: 42px; font-size: 18px; font-weight: 900; }
.stackHead div { text-align: center; font-size: 10.5px; font-weight: 850; color: var(--muted); letter-spacing: .07em; }
.stackScroll {
  flex: 1;
  overflow-y: auto;
  padding: 14px 16px calc(24px + var(--bottom));
}
.stackItem {
  padding: 16px 0;
  border-bottom: 1px solid var(--line);
}
.stackMeta {
  font-size: 8.5px;
  color: var(--muted);
  font-weight: 850;
  letter-spacing: .08em;
  margin-bottom: 6px;
  text-transform: uppercase;
}
.stackText {
  font-family: ui-serif, Georgia, serif;
  font-size: 18.5px;
  line-height: 1.5;
  white-space: pre-wrap;
}
.stackItem[data-field="QUESTION"] .stackText {
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  font-weight: 760;
  letter-spacing: -.03em;
}

/* FLIPPER MODE */
.flipper-wrap {
  padding: 14px 14px calc(24px + var(--bottom));
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
  height: 38px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--paper);
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.deck-counter {
  font-size: 10.5px;
  font-weight: 850;
  color: var(--muted);
  letter-spacing: .06em;
}
.card-box {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 18px 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,.03);
}
.card-meta-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--line-light);
}
.card-id-tag {
  font-size: 9.5px;
  font-weight: 900;
  letter-spacing: .08em;
  color: var(--muted);
}
.card-type-tag {
  font-size: 9px;
  font-weight: 850;
  color: var(--blue);
  background: var(--blue-soft);
  padding: 3px 8px;
  border-radius: 6px;
}
.card-title-main {
  font-size: 21px;
  font-weight: 800;
  line-height: 1.25;
  letter-spacing: -.025em;
  margin-bottom: 8px;
}
.card-source-main {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.45;
  margin-bottom: 14px;
}
.card-question-box {
  background: var(--bg);
  border-left: 3px solid var(--blue);
  padding: 12px 14px;
  border-radius: 0 10px 10px 0;
  margin-bottom: 14px;
}
.card-question-label {
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
  font-family: ui-serif, Georgia, serif;
  font-size: 17px;
  line-height: 1.5;
}
.card-fields-accordion {
  border-top: 1px solid var(--line-light);
  padding-top: 12px;
}
.card-field-row {
  margin-bottom: 12px;
}
.card-field-k {
  font-size: 8.5px;
  font-weight: 900;
  color: var(--muted);
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-bottom: 3px;
}
.card-field-v {
  font-size: 14.5px;
  line-height: 1.48;
}
.raw-card-view {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 12px;
  line-height: 1.6;
  white-space: pre-wrap;
  background: var(--bg);
  padding: 14px;
  border-radius: 10px;
  max-height: 520px;
  overflow-y: auto;
}

/* PDF LIBRARY MODE */
.pdf-wrap {
  padding: 14px 14px calc(24px + var(--bottom));
  max-width: 820px;
  margin: 0 auto;
}
.pdf-filter-bar {
  display: flex;
  gap: 6px;
  margin-bottom: 12px;
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
  border-radius: 14px;
  padding: 14px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdf-card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}
.pdf-title {
  font-size: 15px;
  font-weight: 800;
  line-height: 1.28;
  letter-spacing: -.02em;
}
.pdf-case {
  font-size: 9.5px;
  font-weight: 850;
  color: var(--muted);
  margin-top: 4px;
  text-transform: uppercase;
}
.pdf-tag {
  font-size: 8.5px;
  font-weight: 900;
  letter-spacing: .06em;
  padding: 3px 6px;
  border-radius: 4px;
  white-space: nowrap;
  text-transform: uppercase;
}
.tag-paper { background: var(--blue-soft); color: var(--blue); }
.tag-scan { background: var(--bg); color: var(--muted); border: 1px solid var(--line); }

.pdf-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 8px;
  border-top: 1px solid var(--line-light);
}
.pdf-size {
  font-size: 9.5px;
  font-weight: 800;
  color: var(--muted);
}
.pdf-btn-group {
  display: flex;
  gap: 6px;
}
.pdf-btn {
  height: 34px;
  padding: 0 12px;
  border-radius: 8px;
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
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
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
  padding: var(--top) 12px 0;
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  background: var(--paper);
}
.pdf-modal-title {
  font-size: 12px;
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
  border-radius: 10px;
  padding: 10px 12px;
  font-size: 11px;
  color: var(--muted);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

/* MAPS & STRUCTURAL DOCS MODE */
.maps-wrap {
  padding: 14px 14px calc(24px + var(--bottom));
  max-width: 820px;
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
  border-radius: 8px;
  background: var(--paper);
  padding: 6px 10px;
  font-size: 9px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted);
  text-transform: uppercase;
}
.map-tab-btn.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}
.doc-box {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 16px 14px;
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

/* PROMPTS MODE (Cool Radio POML Suite) */
.prompts-wrap {
  padding: 14px 14px calc(24px + var(--bottom));
  max-width: 760px;
  margin: 0 auto;
}
.poml-stepper {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  margin-bottom: 12px;
  scrollbar-width: none;
}
.poml-stepper::-webkit-scrollbar { display: none; }
.poml-step-btn {
  flex: 0 0 auto;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 6px 10px;
  font-size: 9.5px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--muted);
}
.poml-step-btn.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}
.poml-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 18px 16px;
  margin-bottom: 14px;
}
.poml-head-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}
.poml-num {
  font-size: 11px;
  font-weight: 900;
  color: var(--blue);
  letter-spacing: .08em;
}
.poml-ver {
  font-size: 9.5px;
  font-weight: 850;
  color: var(--muted);
}
.poml-title {
  font-size: 20px;
  font-weight: 850;
  line-height: 1.2;
  margin-bottom: 4px;
}
.poml-sub {
  font-size: 12.5px;
  color: var(--muted);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: .05em;
  font-weight: 750;
}
.poml-say-box {
  background: var(--bg);
  border-left: 3px solid var(--ink);
  padding: 10px 12px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 12px;
  font-size: 13px;
  font-weight: 750;
}
.poml-desc {
  font-size: 13.5px;
  line-height: 1.5;
  color: #333;
  margin-bottom: 12px;
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
  border-radius: 8px;
}
.poml-contract-k {
  font-size: 8px;
  font-weight: 900;
  color: var(--muted);
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
  height: 38px;
  padding: 0 14px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--paper);
  font-size: 10px;
  font-weight: 850;
  letter-spacing: .06em;
}
.poml-btn.primary {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}
.poml-code-box {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 11.5px;
  line-height: 1.6;
  white-space: pre-wrap;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px;
  max-height: 480px;
  overflow-y: auto;
}

/* Modals & Scrims */
.scrim {
  position: absolute;
  z-index: 80;
  inset: 0;
  background: rgba(20,18,15,.22);
  display: none;
}
.scrim.open { display: block; }
.sheet {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: calc(10px + var(--bottom));
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 12px;
  box-shadow: 0 18px 60px rgba(0,0,0,.16);
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.sheetTitle {
  padding: 4px 6px 10px;
  font-size: 10.5px;
  font-weight: 900;
  color: var(--muted);
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
  min-height: 44px;
  border-radius: 10px;
  background: var(--bg);
  font-size: 10px;
  font-weight: 800;
  padding: 6px 8px;
  text-align: center;
  border: 1px solid var(--line-light);
}
.sheetGrid button.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}

.caseList {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.caseRowBtn {
  padding: 10px 12px;
  border-radius: 10px;
  background: var(--bg);
  border: 1px solid var(--line-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-align: left;
}
.caseRowBtn.on {
  background: var(--ink);
  color: #fff;
  border-color: var(--ink);
}
.caseRowBtn.on .caseRowMeta {
  color: #c5c0b6;
}
.caseRowTitle {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: -.01em;
}
.caseRowMeta {
  font-size: 9.5px;
  font-weight: 800;
  color: var(--muted);
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
  padding: 8px 14px;
  font-size: 11px;
  font-weight: 750;
  display: none;
  white-space: nowrap;
  box-shadow: 0 6px 20px rgba(0,0,0,.2);
}
.toast.open { display: block; }

/* Responsive adjustments */
@media(min-width: 760px) {
  header, .toolbar, .subtoolbar, main {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: min(840px, 100%);
  }
  .selection {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: 540px;
  }
  .sheet {
    left: 50%;
    right: auto;
    transform: translateX(-50%);
    width: 600px;
  }
  .lineRow {
    grid-template-columns: 130px 1fr;
    padding-left: 18px;
    padding-right: 18px;
  }
  .zhead {
    padding-left: 18px;
    padding-right: 18px;
  }
  .pdf-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
</head>
<body>
<div id="app">

  <!-- Header -->
  <header>
    <button class="brand" id="brandBtn">SLIPCASE</button>
    <input id="search" class="search" placeholder="Search 1,244 zettels &amp; lines" autocomplete="off">
    <button id="caseNavBtn" class="filterBtn">ALL CASES</button>
  </header>

  <!-- Navigation Toolbar -->
  <div class="toolbar" id="mainToolbar">
    <button class="chip on" data-tab="lines">LINES</button>
    <button class="chip" data-tab="flipper">FLIPPER</button>
    <button class="chip" data-tab="pdfs" id="pdfTabChip">PDFS (124)</button>
    <button class="chip" data-tab="maps">MAPS</button>
    <button class="chip" data-tab="prompts">PROMPTS</button>
    <button class="chip chip-case" id="activeCaseChip" onclick="openCaseModal()">ALL (31 CASES)</button>
  </div>

  <!-- Sub-toolbar for LINES mode -->
  <div class="subtoolbar" id="linesSubtoolbar">
    <button class="subchip on" data-filter="ALL">ALL</button>
    <button class="subchip" data-filter="QUESTION">QUESTIONS</button>
    <button class="subchip" data-filter="PASSAGE">PASSAGES</button>
    <button class="subchip" data-filter="RESEARCH OBJECT">OBJECTS</button>
    <button class="subchip" data-filter="MECHANISM">MECHANISMS</button>
    <button class="subchip" data-filter="FORMAL SHIFT">FORMALISMS</button>
    <button class="subchip" data-filter="TYPE">TYPES</button>
    <button class="subchip" data-filter="SOURCE">SOURCES</button>
    <button class="subchip" id="moreFiltersBtn">FILTER...</button>
  </div>

  <!-- Main Viewport -->
  <main id="mainViewport">
    
    <!-- 1. LINES PANE -->
    <div class="pane active" id="pane-lines">
      <div id="table"></div>
    </div>

    <!-- 2. FLIPPER PANE -->
    <div class="pane" id="pane-flipper">
      <div class="flipper-wrap">
        <div class="deck-controls">
          <button class="deck-btn" id="prevCardBtn">&larr; PREV</button>
          <div class="deck-counter" id="deckCounter">CARD 1 OF 1244</div>
          <button class="deck-btn" id="nextCardBtn">NEXT &rarr;</button>
        </div>
        <div class="deck-controls" style="margin-top:-4px;">
          <button class="deck-btn" id="toggleRawBtn">RAW TEXT</button>
          <button class="deck-btn" id="copyCardBtn">COPY CARD</button>
          <button class="deck-btn" id="downloadCardBtn">DOWNLOAD</button>
        </div>
        <div id="cardBoxContainer" style="margin-top:10px;"></div>
      </div>
    </div>

    <!-- 3. PDF LIBRARY PANE -->
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

    <!-- 4. MAPS & STRUCTURAL DOCS PANE -->
    <div class="pane" id="pane-maps">
      <div class="maps-wrap">
        <div class="maps-tabs" id="mapsTabs"></div>
        <div class="doc-box" id="mapDocContent"></div>
        <div class="doc-action-bar">
          <button class="deck-btn" id="copyDocBtn">COPY DOCUMENT</button>
          <button class="deck-btn" id="downloadDocBtn">DOWNLOAD .TXT</button>
        </div>
      </div>
    </div>

    <!-- 5. PROMPT OPERATOR PANE (Cool Radio Suite) -->
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
    <button id="stackBtn" class="primary">READ</button>
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
      <div class="sheetTitle">SELECT SLIPCASE WORKSPACE</div>
      <div class="sheetScroll">
        <div class="caseList" id="caseList"></div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast" id="toast"></div>

</div>

<script>
(()=>{
/* Embedded Research Data */
const CASES = /* DATA_CASES */;
const ALL_NOTES = /* DATA_NOTES */;
const ALL_PDFS = /* DATA_PDFS */;
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
   1. NAVIGATION & TAB SWITCHING
   ========================================================= */
function setTab(tab) {
  currentTab = tab;
  $$("#mainToolbar .chip[data-tab]").forEach(b => b.classList.toggle("on", b.dataset.tab === tab));
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
  if (tab === "pdfs") renderPdfs();
  if (tab === "maps") renderMaps();
  if (tab === "prompts") renderPrompts();
  window.scrollTo(0,0);
}

$$("#mainToolbar .chip[data-tab]").forEach(b => {
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
    $("#activeCaseChip").textContent = "ALL (31 CASES)";
    $("#pdfTabChip").textContent = `PDFS (${ALL_PDFS.length})`;
  } else {
    const c = CASES[selectedCaseIdx];
    const shortName = c.name.length > 18 ? c.name.slice(0, 16) + "..." : c.name;
    $("#caseNavBtn").textContent = shortName.toUpperCase();
    $("#activeCaseChip").textContent = shortName.toUpperCase();
    $("#pdfTabChip").textContent = `PDFS (${c.pdfs.length})`;
  }
}

function openCaseModal() {
  let html = `
    <div class="caseRowBtn ${selectedCaseIdx === -1 ? 'on' : ''}" onclick="selectCase(-1)">
      <div>
        <div class="caseRowTitle">ALL 31 FIELD SLIPCASES</div>
        <div class="caseRowMeta">${ALL_NOTES.length} ZETTEL CARDS &middot; ${ALL_PDFS.length} RESEARCH PDFS</div>
      </div>
      <div class="caseRowMeta">GLOBAL</div>
    </div>
  `;

  CASES.forEach((c, idx) => {
    html += `
      <div class="caseRowBtn ${selectedCaseIdx === idx ? 'on' : ''}" onclick="selectCase(${idx})">
        <div>
          <div class="caseRowTitle">${esc(c.name)}</div>
          <div class="caseRowMeta">${c.card_count} CARDS &middot; ${c.pdf_count} PDFS</div>
        </div>
        <div class="caseRowMeta">#${String(idx + 1).padStart(2, '0')}</div>
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
  if (currentTab === "pdfs") renderPdfs();
  if (currentTab === "maps") renderMaps();
  toast(idx === -1 ? "Showing All Slipcases" : `Switched to ${CASES[idx].name}`);
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
   4. FLIPPER MODULE (TACTILE CARD FLIPPER)
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
        <pre class="raw-card-view">${esc(card.raw)}</pre>
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
   5. PDF LIBRARY & DUAL-ENGINE READER
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
            <div class="pdf-case">${esc(p.case_name)}</div>
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
   6. MAPS & STRUCTURAL DOCS MODULE
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
   7. PROMPT OPERATOR MODULE (Cool Radio Suite)
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
   8. GLOBAL SEARCH & KEYBOARD SHORTCUTS
   ========================================================= */
$("#search").addEventListener("input", () => {
  if (currentTab === "lines") renderLines();
  if (currentTab === "pdfs") renderPdfs();
});

document.addEventListener("keydown", e => {
  if (e.key === "Escape") {
    closeStack();
    closePdfModal();
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
})();
</script>
</body>
</html>
"""

# Replace placeholders with serialized JSON datasets
html_rendered = html_template.replace('/* DATA_CASES */', json.dumps(cases_data)) \
                             .replace('/* DATA_NOTES */', json.dumps(all_notes)) \
                             .replace('/* DATA_PDFS */', json.dumps(all_pdfs)) \
                             .replace('/* DATA_PROMPTS */', json.dumps(prompts_data))

# Write index.html to workspace
with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_rendered)

print('Successfully re-indexed and wrote index.html and slipcases.json')
