import os, json

with open('/tmp/slipcase_data.json', 'r') as f:
    cases_data = json.load(f)

# Import prompts from build_data
from build_data import prompts_data

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="slipcase.png">
<title>SLIPCASE — Mobile Field Reader & Prompt Operator</title>
<style>
:root {
  --fg: #0d0d0d;
  --bg: #ffffff;
  --dim: #767676;
  --hair: #e2e2e2;
  --hi: #f6f6f6;
  --card-bg: #fafafa;
  --go: #19e6c8;
  --accent: #0055ff;
  --badge-bg: #eeeeee;
  --badge-fg: #333333;
  --code-bg: #1e1e1e;
  --code-fg: #e6e6e6;
  --radius: 6px;
  --shadow: 0 4px 16px rgba(0,0,0,0.06);
}

[data-theme="dark"] {
  --fg: #f2f2f2;
  --bg: #0f1115;
  --dim: #9aa0a6;
  --hair: #262a33;
  --hi: #161a22;
  --card-bg: #181d26;
  --go: #00e5a3;
  --accent: #4d8dff;
  --badge-bg: #262c38;
  --badge-fg: #c5cdd8;
  --shadow: 0 4px 16px rgba(0,0,0,0.3);
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body {
  font: 14.5px/1.6 ui-monospace, "SF Mono", "Menlo", "Consolas", monospace;
  color: var(--fg);
  background: var(--bg);
  padding-bottom: calc(24px + env(safe-area-inset-bottom));
  min-height: 100vh;
}

.wrap { max-width: 900px; margin: 0 auto; padding: 0 16px; }

/* Header & Station ID */
header {
  padding: 16px 0 12px;
  border-bottom: 1px solid var(--hair);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}
.brand { display: flex; align-items: center; gap: 10px; }
.brand-icon { width: 28px; height: 28px; flex: 0 0 28px; }
h1 { font-size: 17px; font-weight: 700; letter-spacing: 0.02em; }
.subhead { font-size: 11.5px; color: var(--dim); margin-top: 2px; }

.hdr-controls { display: flex; gap: 8px; align-items: center; }
.theme-btn {
  border: 1px solid var(--hair);
  background: var(--hi);
  color: var(--fg);
  padding: 6px 10px;
  font: inherit;
  font-size: 12px;
  border-radius: var(--radius);
  cursor: pointer;
}

/* Master Mode Switcher */
.mode-bar {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 12px 0 8px;
  scrollbar-width: none;
}
.mode-bar::-webkit-scrollbar { display: none; }
.mode-tab {
  flex: 0 0 auto;
  border: 1.5px solid var(--hair);
  background: var(--bg);
  color: var(--fg);
  padding: 8px 14px;
  font: 600 12px/1 inherit;
  border-radius: 20px;
  cursor: pointer;
  letter-spacing: 0.03em;
  transition: all 0.15s ease;
}
.mode-tab.on {
  background: var(--fg);
  color: var(--bg);
  border-color: var(--fg);
}

/* Section Containers */
.tab-pane { display: none; margin-top: 14px; }
.tab-pane.active { display: block; }

/* PROMPT OPERATOR STYLING (Inspired by Cool Radio) */
.prompt-nav {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 8px 0 12px;
  scrollbar-width: none;
}
.prompt-nav::-webkit-scrollbar { display: none; }
.chip {
  flex: 0 0 auto;
  border: 1px solid var(--fg);
  padding: 8px 12px;
  font: 12px/1 inherit;
  background: var(--bg);
  color: var(--fg);
  cursor: pointer;
  letter-spacing: 0.03em;
  border-radius: 4px;
}
.chip.on { background: var(--fg); color: var(--bg); }
.chip.off { border-color: var(--hair); color: var(--dim); }

.pos-indicator {
  font-size: 11.5px;
  color: var(--dim);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-top: 1px solid var(--hair);
  padding-top: 10px;
  margin-bottom: 4px;
}

.step-card {
  background: var(--card-bg);
  border: 1px solid var(--hair);
  border-radius: var(--radius);
  padding: 16px;
  margin-bottom: 14px;
}
.step-ver { font-size: 11.5px; color: var(--dim); letter-spacing: 0.06em; font-weight: 600; }
.step-title { font-size: 24px; line-height: 1.2; margin: 4px 0 2px; font-weight: 700; }
.step-sub { font-size: 13.5px; color: var(--accent); margin-bottom: 12px; font-weight: 600; }
.step-what { font-size: 14px; margin-bottom: 14px; line-height: 1.5; }

dl.prompt-dl { border-top: 1px solid var(--hair); margin-bottom: 12px; }
dt.prompt-dt { font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--dim); padding-top: 8px; }
dd.prompt-dd { font-size: 13.5px; padding-bottom: 8px; border-bottom: 1px solid var(--hair); }
dd.say { font-weight: 700; color: var(--fg); }

.bigbtn {
  display: block;
  width: 100%;
  border: 2px solid var(--fg);
  background: var(--fg);
  color: var(--bg);
  font: 700 15px/1.2 inherit;
  padding: 16px 14px;
  cursor: pointer;
  letter-spacing: 0.03em;
  margin-bottom: 8px;
  border-radius: var(--radius);
  transition: transform 0.1s;
}
.bigbtn:active { transform: translateY(1px); }
.bigbtn.done { background: var(--go); color: #000; border-color: var(--fg); }
.hint { font-size: 11.5px; color: var(--dim); text-align: center; margin-bottom: 14px; }

.minor-btns { display: flex; gap: 8px; margin-bottom: 16px; }
.minor-btns button {
  flex: 1;
  border: 1px solid var(--hair);
  background: var(--hi);
  color: var(--fg);
  font: 12.5px/1 inherit;
  padding: 12px 6px;
  cursor: pointer;
  border-radius: var(--radius);
}
.minor-btns button:active { background: var(--hair); }

pre.prompt-pre {
  display: none;
  border: 1px solid var(--hair);
  background: var(--hi);
  padding: 14px;
  white-space: pre-wrap;
  word-wrap: break-word;
  font: 11.5px/1.6 inherit;
  max-height: 60vh;
  overflow: auto;
  margin-bottom: 16px;
  border-radius: var(--radius);
  -webkit-overflow-scrolling: touch;
}
pre.prompt-pre.on { display: block; }
.prompt-meta { font-size: 11px; color: var(--dim); border-top: 1px solid var(--hair); padding-top: 10px; }

/* SLIPCASE FLIPPER & CARDS */
.case-select-box {
  margin-bottom: 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.case-select-label { font-size: 11px; text-transform: uppercase; color: var(--dim); letter-spacing: 0.08em; }
.case-dropdown {
  width: 100%;
  padding: 10px 12px;
  font: inherit;
  font-size: 13px;
  border: 1.5px solid var(--fg);
  border-radius: var(--radius);
  background: var(--bg);
  color: var(--fg);
}

.case-summary-bar {
  display: flex;
  gap: 8px;
  font-size: 11px;
  color: var(--dim);
  margin-bottom: 14px;
  flex-wrap: wrap;
}
.case-badge {
  background: var(--badge-bg);
  color: var(--badge-fg);
  padding: 3px 8px;
  border-radius: 12px;
  font-weight: 600;
}

.card-deck-wrapper {
  position: relative;
  touch-action: pan-y;
}

.flipper-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}
.flip-btn {
  border: 1.5px solid var(--fg);
  background: var(--bg);
  color: var(--fg);
  padding: 10px 16px;
  font: 700 13px/1 inherit;
  cursor: pointer;
  border-radius: var(--radius);
}
.flip-btn:disabled { opacity: 0.3; border-color: var(--hair); }
.flip-pos { font-size: 12px; font-weight: 700; color: var(--dim); text-align: center; }

.slip-card {
  background: var(--card-bg);
  border: 1.5px solid var(--hair);
  border-radius: var(--radius);
  padding: 18px 16px;
  box-shadow: var(--shadow);
  margin-bottom: 14px;
  position: relative;
}
.slip-header {
  border-bottom: 1px solid var(--hair);
  padding-bottom: 10px;
  margin-bottom: 12px;
}
.slip-num { font-size: 11px; color: var(--accent); font-weight: 700; letter-spacing: 0.05em; }
.slip-title { font-size: 17px; font-weight: 700; line-height: 1.3; margin: 4px 0 2px; }
.slip-source { font-size: 12px; color: var(--dim); margin-top: 4px; }
.slip-question {
  background: var(--hi);
  border-left: 3px solid var(--accent);
  padding: 8px 12px;
  font-size: 12.5px;
  margin: 10px 0;
  border-radius: 0 var(--radius) var(--radius) 0;
}

.slip-body {
  font-size: 12.5px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 55vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 10px;
  background: var(--bg);
  border: 1px solid var(--hair);
  border-radius: var(--radius);
}

.card-actions {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}
.card-act-btn {
  flex: 1;
  border: 1px solid var(--fg);
  background: var(--bg);
  color: var(--fg);
  padding: 10px 8px;
  font: 600 12px/1 inherit;
  cursor: pointer;
  border-radius: var(--radius);
  text-align: center;
}
.card-act-btn:active { background: var(--hi); }

/* PDF READER & LIBRARY */
.pdf-filter-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
.pdf-search-input {
  flex: 1;
  min-width: 200px;
  padding: 10px 12px;
  border: 1px solid var(--hair);
  background: var(--hi);
  color: var(--fg);
  font: inherit;
  font-size: 13px;
  border-radius: var(--radius);
}
.pdf-list-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 70vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.pdf-item-card {
  border: 1px solid var(--hair);
  background: var(--card-bg);
  padding: 12px 14px;
  border-radius: var(--radius);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: border-color 0.15s;
}
.pdf-item-card:hover { border-color: var(--fg); }
.pdf-info-col { flex: 1; min-width: 0; }
.pdf-item-name { font-size: 13px; font-weight: 700; word-break: break-word; }
.pdf-item-meta { font-size: 11px; color: var(--dim); margin-top: 3px; }
.pdf-open-btn {
  border: 1px solid var(--fg);
  background: var(--fg);
  color: var(--bg);
  padding: 8px 12px;
  font: 600 11.5px/1 inherit;
  border-radius: var(--radius);
  cursor: pointer;
  white-space: nowrap;
}

/* PDF Modal / Full View */
.pdf-viewer-modal {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.85);
  z-index: 1000;
  flex-direction: column;
  padding: env(safe-area-inset-top) 0 env(safe-area-inset-bottom);
}
.pdf-viewer-modal.active { display: flex; }
.pdf-viewer-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  background: #111;
  color: #fff;
  border-bottom: 1px solid #333;
}
.pdf-viewer-title { font-size: 13px; font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 65%; }
.pdf-close-btn {
  background: #333;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: var(--radius);
  cursor: pointer;
  font: inherit;
  font-size: 12px;
}
.pdf-frame-wrap { flex: 1; width: 100%; height: 100%; background: #222; }
.pdf-frame { width: 100%; height: 100%; border: none; }

/* SPECIAL DOCS & MAPS */
.spec-list { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px; }
.spec-btn {
  border: 1px solid var(--hair);
  background: var(--hi);
  color: var(--fg);
  padding: 6px 10px;
  font: 12px inherit;
  border-radius: var(--radius);
  cursor: pointer;
}
.spec-btn.active { background: var(--fg); color: var(--bg); border-color: var(--fg); }
.spec-content-view {
  background: var(--card-bg);
  border: 1px solid var(--hair);
  border-radius: var(--radius);
  padding: 14px;
  font-size: 12px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 60vh;
  overflow-y: auto;
}

/* OMNI-SEARCH */
.search-box-wrap { margin-bottom: 14px; }
.omni-input {
  width: 100%;
  padding: 12px 14px;
  font: inherit;
  font-size: 14px;
  border: 1.5px solid var(--fg);
  background: var(--bg);
  color: var(--fg);
  border-radius: var(--radius);
}
.search-results-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 65vh;
  overflow-y: auto;
}
.search-res-item {
  border: 1px solid var(--hair);
  background: var(--card-bg);
  padding: 12px;
  border-radius: var(--radius);
  cursor: pointer;
}
.search-res-item:hover { border-color: var(--accent); }
.search-res-title { font-size: 13.5px; font-weight: 700; color: var(--accent); }
.search-res-case { font-size: 11px; color: var(--dim); margin-bottom: 4px; }
.search-res-snippet { font-size: 12px; color: var(--fg); line-height: 1.4; }

/* Footer */
footer {
  border-top: 1px solid var(--hair);
  margin-top: 24px;
  padding: 16px 0 28px;
  font-size: 11px;
  color: var(--dim);
  text-align: center;
}

@media (max-width: 600px) {
  .step-title { font-size: 20px; }
  .slip-title { font-size: 15px; }
  .mode-tab { padding: 7px 11px; font-size: 11px; }
}
</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="brand">
    <div class="brand-icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round">
        <circle cx="50" cy="50" r="38"/>
        <circle cx="50" cy="36.0" r="4.6" fill="currentColor" stroke="none"/>
        <path d="M37.2 38.3 A 13 13 0 0 0 62.8 38.3"/>
        <path d="M27.8 39.9 A 22.5 22.5 0 0 0 72.2 39.9"/>
        <path d="M18.5 41.6 A 32 32 0 0 0 81.5 41.6"/>
      </svg>
    </div>
    <div>
      <h1>SLIPCASE & PROMPT OPERATOR</h1>
      <div class="subhead">Mobile Field Reader · 31 Slipcases · 1,244 Slips · 140 PDFs</div>
    </div>
  </div>
  <div class="hdr-controls">
    <button class="theme-btn" id="themeToggle" title="Toggle Dark/Light Mode">🌓</button>
  </div>
</header>

<!-- Navigation Mode Tabs -->
<div class="mode-bar">
  <button class="mode-tab on" data-tab="prompts">⚡ Prompt Operator</button>
  <button class="mode-tab" data-tab="flipper">🗂 Card Deck Flipper</button>
  <button class="mode-tab" data-tab="pdfs">📄 Mobile PDF Reader</button>
  <button class="mode-tab" data-tab="cases">🗺 Cases & Field Maps</button>
  <button class="mode-tab" data-tab="search">🔍 Omni-Search</button>
</div>

<!-- TAB 1: PROMPT OPERATOR -->
<section id="tab-prompts" class="tab-pane active">
  <div class="prompt-nav" id="promptNav"></div>
  <div class="pos-indicator" id="promptPos"></div>
  <div id="promptStepContent"></div>
</section>

<!-- TAB 2: SLIPCASE CARD FLIPPER -->
<section id="tab-flipper" class="tab-pane">
  <div class="case-select-box">
    <label class="case-select-label" for="caseSelect">Active Case / Workspace</label>
    <select id="caseSelect" class="case-dropdown"></select>
  </div>
  
  <div class="case-summary-bar" id="caseSummaryBar"></div>

  <div class="card-deck-wrapper" id="cardDeckWrapper">
    <div class="flipper-controls">
      <button class="flip-btn" id="prevCardBtn">← Prev Slip</button>
      <div class="flip-pos" id="cardPosIndicator">Slip 1 of 1</div>
      <button class="flip-btn" id="nextCardBtn">Next Slip →</button>
    </div>

    <div class="slip-card" id="slipCardRender"></div>

    <div class="card-actions">
      <button class="card-act-btn" id="copyCardBtn">📋 Copy Payload</button>
      <button class="card-act-btn" id="toggleRawBtn">👁 Toggle Raw / Parsed</button>
      <button class="card-act-btn" id="dlCardBtn">💾 Download .txt</button>
      <button class="card-act-btn" id="randomCardBtn">🎲 Random</button>
    </div>
  </div>
</section>

<!-- TAB 3: MOBILE PDF READER & LIBRARY -->
<section id="tab-pdfs" class="tab-pane">
  <div class="pdf-filter-bar">
    <input type="text" id="pdfSearchInput" class="pdf-search-input" placeholder="Search 140 PDFs by name or case...">
    <select id="pdfCategorySelect" class="case-dropdown" style="width:auto;">
      <option value="all">All PDFs (140)</option>
      <option value="papers">Compiled Papers</option>
      <option value="resources">Research Scans & Resources</option>
    </select>
  </div>

  <div class="pdf-list-grid" id="pdfListGrid"></div>
</section>

<!-- TAB 4: CASES & FIELD MAPS -->
<section id="tab-cases" class="tab-pane">
  <div class="case-select-box">
    <label class="case-select-label" for="caseMetaSelect">Select Slipcase to Inspect</label>
    <select id="caseMetaSelect" class="case-dropdown"></select>
  </div>
  <div class="spec-list" id="specListBar"></div>
  <div class="spec-content-view" id="specContentView">Select a document above to view its contents.</div>
</section>

<!-- TAB 5: OMNI SEARCH -->
<section id="tab-search" class="tab-pane">
  <div class="search-box-wrap">
    <input type="text" id="omniSearchInput" class="omni-input" placeholder="Search across all 1,244 cards & 140 PDFs...">
  </div>
  <div class="pos-indicator" id="searchCountIndicator">Enter search keywords above.</div>
  <div class="search-results-list" id="searchResultsList"></div>
</section>

<!-- PDF MODAL VIEWER -->
<div class="pdf-viewer-modal" id="pdfViewerModal">
  <div class="pdf-viewer-bar">
    <div class="pdf-viewer-title" id="pdfModalTitle">PDF Reader</div>
    <div style="display:flex;gap:6px;">
      <button class="pdf-close-btn" id="pdfModalExternalBtn">↗ New Tab</button>
      <button class="pdf-close-btn" id="pdfModalCloseBtn">✕ Close</button>
    </div>
  </div>
  <div class="pdf-frame-wrap">
    <iframe class="pdf-frame" id="pdfIframe" src="about:blank"></iframe>
  </div>
</div>

<footer>
  SLIPCASE PORTABLE RESEARCH FIELD & PROMPT OPERATOR<br>
  Watson Hartsoe · Atlanta · 2026-08-18 · 100% Offline & Mobile-Ready
</footer>

</div>

<script>
/* Embedded Dataset */
const PROMPTS = """ + json.dumps(prompts_data) + """;
const CASES = """ + json.dumps(cases_data) + """;

/* Application State */
let currentTab = 'prompts';
let currentPromptIdx = 0;
let promptShown = false;

let currentCaseIdx = 0;
let currentCardIdx = 0;
let showRawCard = false;

let activePdfUrl = '';

/* Utility functions */
const esc = s => (s||'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

/* Theme Toggle */
const themeBtn = document.getElementById('themeToggle');
let isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
if (localStorage.getItem('slipcase_theme')) {
  isDark = localStorage.getItem('slipcase_theme') === 'dark';
}
document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
themeBtn.onclick = () => {
  isDark = !isDark;
  document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
  localStorage.setItem('slipcase_theme', isDark ? 'dark' : 'light');
};

/* Mode Tab Switching */
document.querySelectorAll('.mode-tab').forEach(tab => {
  tab.onclick = () => {
    document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('on'));
    tab.classList.add('on');
    currentTab = tab.dataset.tab;
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    document.getElementById('tab-' + currentTab).classList.add('active');
    window.scrollTo(0,0);
  };
});

/* =========================================================
   1. PROMPT OPERATOR MODULE
   ========================================================= */
function renderPromptNav() {
  const nav = document.getElementById('promptNav');
  nav.innerHTML = PROMPTS.map((p, n) =>
    `<button class="chip ${n === currentPromptIdx ? 'on' : (p.say === '—' ? 'off' : '')}" data-n="${n}">${p.num} ${esc(p.title)}</button>`
  ).join('');
  nav.querySelectorAll('.chip').forEach(b => {
    b.onclick = () => {
      currentPromptIdx = +b.dataset.n;
      promptShown = false;
      drawPrompt();
    };
  });
}

function drawPrompt() {
  const p = PROMPTS[currentPromptIdx];
  document.getElementById('promptPos').textContent = `Prompt ${currentPromptIdx + 1} of ${PROMPTS.length} · Instrument ${p.num}`;
  
  document.getElementById('promptStepContent').innerHTML = `
    <div class="step-card">
      <div class="step-ver">${p.num}${p.ver ? ' · v' + esc(p.ver) : ''}</div>
      <h2 class="step-title">${esc(p.title)}</h2>
      <div class="step-sub">${esc(p.sub)}</div>
      <div class="step-what">${esc(p.what)}</div>
      <dl class="prompt-dl">
        <dt class="prompt-dt">Paste into</dt><dd class="prompt-dd">${esc(p.inp)}</dd>
        <dt class="prompt-dt">You get back</dt><dd class="prompt-dd">${esc(p.out)}</dd>
        <dt class="prompt-dt">Then say</dt><dd class="prompt-dd say">${esc(p.say)}</dd>
      </dl>
    </div>
    <button class="bigbtn" id="promptGoBtn">Copy ${p.num} ${esc(p.title)}${currentPromptIdx < PROMPTS.length - 1 ? ' + Next' : ''}</button>
    <div class="hint">Tap to copy to clipboard${currentPromptIdx < PROMPTS.length - 1 ? ', advances automatically' : ''}.</div>
    <div class="minor-btns">
      <button id="promptShowBtn">${promptShown ? 'Hide prompt' : 'Read prompt'}</button>
      <button id="promptDlBtn">Download .txt</button>
      <button id="promptPrevBtn">Back</button>
    </div>
    <pre class="prompt-pre ${promptShown ? 'on' : ''}">${esc(p.text)}</pre>
    <div class="prompt-meta">${p.lines} lines · ${(p.chars / 1024).toFixed(1)} KB · sha ${p.sha}<br>${esc(p.file)}</div>
  `;

  renderPromptNav();

  document.getElementById('promptGoBtn').onclick = async e => {
    const b = e.currentTarget;
    try { await navigator.clipboard.writeText(p.text); }
    catch(_) {
      const a = document.createElement('textarea'); a.value = p.text; a.style.position = 'fixed';
      document.body.appendChild(a); a.select(); document.execCommand('copy'); a.remove();
    }
    b.textContent = 'Copied!'; b.classList.add('done');
    setTimeout(() => {
      if (currentPromptIdx < PROMPTS.length - 1) {
        currentPromptIdx++;
        promptShown = false;
        drawPrompt();
        window.scrollTo(0,0);
      } else {
        drawPrompt();
      }
    }, 650);
  };

  document.getElementById('promptShowBtn').onclick = () => {
    promptShown = !promptShown;
    drawPrompt();
  };

  document.getElementById('promptDlBtn').onclick = () => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([p.text], { type: 'text/plain' }));
    a.download = p.file;
    a.click();
    URL.revokeObjectURL(a.href);
  };

  document.getElementById('promptPrevBtn').onclick = () => {
    currentPromptIdx = (currentPromptIdx - 1 + PROMPTS.length) % PROMPTS.length;
    promptShown = false;
    drawPrompt();
    window.scrollTo(0,0);
  };
}

/* =========================================================
   2. SLIPCASE FLIPPER MODULE
   ========================================================= */
function initCaseSelector() {
  const sel = document.getElementById('caseSelect');
  const metaSel = document.getElementById('caseMetaSelect');
  
  const optionsHtml = CASES.map((c, idx) => 
    `<option value="${idx}">${idx + 1}. ${c.name} (${c.card_count} slips, ${c.pdf_count} PDFs)</option>`
  ).join('');

  sel.innerHTML = optionsHtml;
  metaSel.innerHTML = optionsHtml;

  sel.onchange = () => {
    currentCaseIdx = +sel.value;
    currentCardIdx = 0;
    renderCardFlipper();
  };

  metaSel.onchange = () => {
    renderCaseSpecials(+metaSel.value);
  };
}

function renderCardFlipper() {
  const activeCase = CASES[currentCaseIdx];
  if (!activeCase || !activeCase.cards || activeCase.cards.length === 0) {
    document.getElementById('cardPosIndicator').textContent = '0 slips in case';
    document.getElementById('slipCardRender').innerHTML = '<div style="padding:20px;text-align:center;color:var(--dim)">This slipcase does not contain standalone text slips. Check the PDF tab or Case Documents!</div>';
    document.getElementById('prevCardBtn').disabled = true;
    document.getElementById('nextCardBtn').disabled = true;
    return;
  }

  const cards = activeCase.cards;
  if (currentCardIdx >= cards.length) currentCardIdx = 0;
  if (currentCardIdx < 0) currentCardIdx = cards.length - 1;

  const card = cards[currentCardIdx];

  // Update Case Summary Bar
  document.getElementById('caseSummaryBar').innerHTML = `
    <span class="case-badge">${cards.length} Slips</span>
    <span class="case-badge">${activeCase.pdf_count} PDFs</span>
    <span class="case-badge">${Object.keys(activeCase.specials || {}).length} Field Docs</span>
  `;

  // Update Pos Indicator
  document.getElementById('cardPosIndicator').textContent = `Slip ${currentCardIdx + 1} of ${cards.length}`;
  document.getElementById('prevCardBtn').disabled = cards.length <= 1;
  document.getElementById('nextCardBtn').disabled = cards.length <= 1;

  // Render Card Content
  if (showRawCard) {
    document.getElementById('slipCardRender').innerHTML = `
      <div class="slip-header">
        <div class="slip-num">SLIP #${currentCardIdx + 1} · ${esc(card.id)}</div>
        <div class="slip-title">${esc(card.t)}</div>
        ${card.s ? `<div class="slip-source">SOURCE: ${esc(card.s)}</div>` : ''}
      </div>
      <pre class="slip-body">${esc(card.c)}</pre>
    `;
  } else {
    document.getElementById('slipCardRender').innerHTML = `
      <div class="slip-header">
        <div class="slip-num">SLIP #${currentCardIdx + 1} · ${esc(card.id)}</div>
        <div class="slip-title">${esc(card.t)}</div>
        ${card.s ? `<div class="slip-source"><strong>Source:</strong> ${esc(card.s)}</div>` : ''}
      </div>
      ${card.q ? `<div class="slip-question"><strong>Question:</strong> ${esc(card.q)}</div>` : ''}
      <pre class="slip-body">${esc(card.c)}</pre>
    `;
  }
}

// Touch swipe gesture support for mobile card flipping
let touchStartX = 0;
let touchEndX = 0;
const cardDeckWrap = document.getElementById('cardDeckWrapper');

cardDeckWrap.addEventListener('touchstart', e => {
  touchStartX = e.changedTouches[0].screenX;
}, { passive: true });

cardDeckWrap.addEventListener('touchend', e => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
}, { passive: true });

function handleSwipe() {
  const swipeThreshold = 50;
  if (touchEndX < touchStartX - swipeThreshold) {
    // Swipe left -> Next
    flipNext();
  }
  if (touchEndX > touchStartX + swipeThreshold) {
    // Swipe right -> Prev
    flipPrev();
  }
}

function flipNext() {
  const cards = CASES[currentCaseIdx].cards;
  if (cards && cards.length > 0) {
    currentCardIdx = (currentCardIdx + 1) % cards.length;
    renderCardFlipper();
  }
}

function flipPrev() {
  const cards = CASES[currentCaseIdx].cards;
  if (cards && cards.length > 0) {
    currentCardIdx = (currentCardIdx - 1 + cards.length) % cards.length;
    renderCardFlipper();
  }
}

document.getElementById('nextCardBtn').onclick = flipNext;
document.getElementById('prevCardBtn').onclick = flipPrev;

document.getElementById('copyCardBtn').onclick = async e => {
  const card = CASES[currentCaseIdx].cards[currentCardIdx];
  if (!card) return;
  const btn = e.currentTarget;
  try { await navigator.clipboard.writeText(card.c); }
  catch(_) {
    const a = document.createElement('textarea'); a.value = card.c; a.style.position = 'fixed';
    document.body.appendChild(a); a.select(); document.execCommand('copy'); a.remove();
  }
  btn.textContent = '✓ Copied!';
  setTimeout(() => btn.textContent = '📋 Copy Payload', 1000);
};

document.getElementById('toggleRawBtn').onclick = () => {
  showRawCard = !showRawCard;
  renderCardFlipper();
};

document.getElementById('dlCardBtn').onclick = () => {
  const card = CASES[currentCaseIdx].cards[currentCardIdx];
  if (!card) return;
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([card.c], { type: 'text/plain' }));
  a.download = card.id;
  a.click();
  URL.revokeObjectURL(a.href);
};

document.getElementById('randomCardBtn').onclick = () => {
  const cards = CASES[currentCaseIdx].cards;
  if (cards && cards.length > 0) {
    currentCardIdx = Math.floor(Math.random() * cards.length);
    renderCardFlipper();
  }
};

/* =========================================================
   3. MOBILE PDF READER & LIBRARY MODULE
   ========================================================= */
function getAllPdfs() {
  let list = [];
  CASES.forEach(c => {
    if (c.pdfs) {
      c.pdfs.forEach(p => {
        list.push({ ...p, caseName: c.name, caseFolder: c.folder });
      });
    }
  });
  return list;
}

function renderPdfLibrary() {
  const query = document.getElementById('pdfSearchInput').value.toLowerCase();
  const category = document.getElementById('pdfCategorySelect').value;
  const allPdfs = getAllPdfs();

  const filtered = allPdfs.filter(p => {
    const matchesQuery = p.name.toLowerCase().includes(query) || p.caseName.toLowerCase().includes(query);
    if (!matchesQuery) return false;
    if (category === 'papers') return p.is_paper;
    if (category === 'resources') return !p.is_paper;
    return true;
  });

  const grid = document.getElementById('pdfListGrid');
  if (filtered.length === 0) {
    grid.innerHTML = '<div style="padding:20px;text-align:center;color:var(--dim)">No matching PDFs found.</div>';
    return;
  }

  grid.innerHTML = filtered.map(p => {
    const sizeMb = (p.size / (1024 * 1024)).toFixed(2);
    // Relative path constructed to work from Downloads root or local subfolder
    const relUrl = p.rel;
    return `
      <div class="pdf-item-card">
        <div class="pdf-info-col" onclick="openPdfViewer('${encodeURIComponent(relUrl)}', '${esc(p.name)}')">
          <div class="pdf-item-name">${p.is_paper ? '📘 ' : '📑 '} ${esc(p.name)}</div>
          <div class="pdf-item-meta">${esc(p.caseName)} · ${sizeMb} MB ${p.is_paper ? '· [Compiled Paper]' : '· [Source / Scan]'}</div>
        </div>
        <button class="pdf-open-btn" onclick="openPdfViewer('${encodeURIComponent(relUrl)}', '${esc(p.name)}')">Read PDF</button>
      </div>
    `;
  }).join('');
}

document.getElementById('pdfSearchInput').oninput = renderPdfLibrary;
document.getElementById('pdfCategorySelect').onchange = renderPdfLibrary;

function openPdfViewer(url, title) {
  const decodedUrl = decodeURIComponent(url);
  activePdfUrl = decodedUrl;
  document.getElementById('pdfModalTitle').textContent = title;
  document.getElementById('pdfIframe').src = decodedUrl;
  document.getElementById('pdfViewerModal').classList.add('active');
}

document.getElementById('pdfModalCloseBtn').onclick = () => {
  document.getElementById('pdfViewerModal').classList.remove('active');
  document.getElementById('pdfIframe').src = 'about:blank';
};

document.getElementById('pdfModalExternalBtn').onclick = () => {
  if (activePdfUrl) {
    window.open(activePdfUrl, '_blank');
  }
};

/* =========================================================
   4. CASES & FIELD MAPS MODULE
   ========================================================= */
function renderCaseSpecials(caseIdx) {
  const activeCase = CASES[caseIdx];
  const listBar = document.getElementById('specListBar');
  const view = document.getElementById('specContentView');

  if (!activeCase || !activeCase.specials || Object.keys(activeCase.specials).length === 0) {
    listBar.innerHTML = '';
    view.textContent = 'No special 000__* files found for this case.';
    return;
  }

  const keys = Object.keys(activeCase.specials);
  listBar.innerHTML = keys.map((k, idx) => 
    `<button class="spec-btn ${idx === 0 ? 'active' : ''}" data-key="${k}">${k.replace('000__','').replace('.txt','')}</button>`
  ).join('');

  view.textContent = activeCase.specials[keys[0]] || '';

  listBar.querySelectorAll('.spec-btn').forEach(btn => {
    btn.onclick = () => {
      listBar.querySelectorAll('.spec-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      view.textContent = activeCase.specials[btn.dataset.key] || '';
    };
  });
}

/* =========================================================
   5. OMNI-SEARCH MODULE
   ========================================================= */
const omniInput = document.getElementById('omniSearchInput');
const omniResults = document.getElementById('searchResultsList');
const searchCount = document.getElementById('searchCountIndicator');

omniInput.oninput = () => {
  const q = omniInput.value.trim().toLowerCase();
  if (!q) {
    searchCount.textContent = 'Enter search keywords above.';
    omniResults.innerHTML = '';
    return;
  }

  let matches = [];
  CASES.forEach((c, cIdx) => {
    // Search cards
    if (c.cards) {
      c.cards.forEach((card, cardIdx) => {
        if (card.t.toLowerCase().includes(q) || card.c.toLowerCase().includes(q) || (card.s && card.s.toLowerCase().includes(q))) {
          // generate snippet
          const lowerC = card.c.toLowerCase();
          const pos = lowerC.indexOf(q);
          let snippet = '';
          if (pos !== -1) {
            const start = Math.max(0, pos - 40);
            const end = Math.min(card.c.length, pos + 100);
            snippet = (start > 0 ? '...' : '') + card.c.substring(start, end).replace(/\\n/g, ' ') + (end < card.c.length ? '...' : '');
          } else {
            snippet = card.t;
          }
          matches.push({
            type: 'card',
            caseIdx: cIdx,
            cardIdx: cardIdx,
            title: card.t,
            caseName: c.name,
            snippet: snippet
          });
        }
      });
    }

    // Search PDFs
    if (c.pdfs) {
      c.pdfs.forEach(p => {
        if (p.name.toLowerCase().includes(q)) {
          matches.push({
            type: 'pdf',
            caseName: c.name,
            title: p.name,
            rel: p.rel,
            snippet: 'PDF document in ' + c.name
          });
        }
      });
    }
  });

  searchCount.textContent = `Found ${matches.length} matching result(s)`;

  if (matches.length === 0) {
    omniResults.innerHTML = '<div style="padding:20px;text-align:center;color:var(--dim)">No cards or PDFs matched your query.</div>';
    return;
  }

  omniResults.innerHTML = matches.slice(0, 100).map(m => {
    if (m.type === 'card') {
      return `
        <div class="search-res-item" onclick="jumpToCard(${m.caseIdx}, ${m.cardIdx})">
          <div class="search-res-case">🗂 ${esc(m.caseName)}</div>
          <div class="search-res-title">Slip: ${esc(m.title)}</div>
          <div class="search-res-snippet">${esc(m.snippet)}</div>
        </div>
      `;
    } else {
      return `
        <div class="search-res-item" onclick="openPdfViewer('${encodeURIComponent(m.rel)}', '${esc(m.title)}')">
          <div class="search-res-case">📄 ${esc(m.caseName)}</div>
          <div class="search-res-title">PDF: ${esc(m.title)}</div>
          <div class="search-res-snippet">${esc(m.snippet)}</div>
        </div>
      `;
    }
  }).join('');
};

function jumpToCard(caseIdx, cardIdx) {
  currentCaseIdx = caseIdx;
  currentCardIdx = cardIdx;
  document.getElementById('caseSelect').value = caseIdx;
  renderCardFlipper();
  
  // Switch tab to flipper
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.remove('on'));
  document.querySelector('.mode-tab[data-tab="flipper"]').classList.add('on');
  currentTab = 'flipper';
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.getElementById('tab-flipper').classList.add('active');
  window.scrollTo(0,0);
}

/* Keyboard Shortcuts */
window.addEventListener('keydown', e => {
  if (currentTab === 'prompts') {
    if (e.key === 'ArrowRight') { currentPromptIdx = (currentPromptIdx + 1) % PROMPTS.length; promptShown = false; drawPrompt(); }
    if (e.key === 'ArrowLeft') { currentPromptIdx = (currentPromptIdx - 1 + PROMPTS.length) % PROMPTS.length; promptShown = false; drawPrompt(); }
  } else if (currentTab === 'flipper') {
    if (e.key === 'ArrowRight') { flipNext(); }
    if (e.key === 'ArrowLeft') { flipPrev(); }
  }
});

/* Initialize Everything on Load */
drawPrompt();
initCaseSelector();
renderCardFlipper();
renderPdfLibrary();
renderCaseSpecials(0);
</script>
</body>
</html>
"""

# Write index.html to SLIPCASE workspace
with open('/Users/gaia/SLIPCASE/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

# Also write to Downloads workspace
with open('/Users/gaia/Downloads/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Successfully generated index.html in /Users/gaia/SLIPCASE/index.html and /Users/gaia/Downloads/index.html')
