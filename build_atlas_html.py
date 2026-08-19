import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "slipcases.json"), "r", encoding="utf-8") as f:
    cases_data = json.load(f)

all_notes = []
for c in cases_data:
    all_notes.extend(c.get("cards", []))

atlas_template = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">
<meta name="theme-color" content="#ffffff">
<title>SLIPCASE — Structural Atlas</title>
<style>
/* SLIPCASE Master Brand Command v1.0 Design Tokens */
:root {
  --blue: #0647E5;
  --blue-soft: #E7EEFF;
  --paper: #FFFFFF;
  --field: #F7F8FA;
  --bg: #F7F8FA;
  --ink: #111318;
  --grey: #9CA3AF;
  --muted-dark: #6B7280;
  --pale: #E7EEFF;
  --wash: #EFF4FF;
  --border: #E5E7EB;
  --code-bg: #F3F4F6;
  --grid-step: 40px;
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

/* Header */
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

/* Control Bar */
.control-bar {
  flex: 0 0 auto;
  height: 40px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--paper);
  border-bottom: 1.5px solid var(--pale);
  z-index: 39;
}
.ctrl-group {
  display: flex;
  align-items: center;
  gap: 6px;
}
.ctrl-btn {
  height: 28px;
  padding: 0 10px;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--paper);
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: .06em;
  color: var(--ink);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.ctrl-btn:hover { border-color: var(--blue); color: var(--blue); }
.ctrl-btn.primary { background: var(--blue); color: #fff; border-color: var(--blue); }

/* Atlas Stage */
#atlasStage {
  flex: 1 1 auto;
  position: relative;
  overflow: hidden;
  background: var(--field);
  touch-action: none;
  cursor: grab;
}
#atlasStage.panning { cursor: grabbing; }

#dotGrid {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(circle at 1px 1px, rgba(6,71,229,.22) 1.2px, transparent 0);
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

/* Lego Atomic Slip Block */
.lego-block {
  position: absolute;
  width: 280px;
  background: var(--paper);
  border: 1.5px solid var(--pale);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(17,19,24,.05);
  display: flex;
  flex-direction: column;
  user-select: none;
  touch-action: none;
  transition: box-shadow .15s ease, border-color .15s ease;
}
.lego-block::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3.5px;
  background: var(--pale);
  border-radius: 7px 7px 0 0;
}
.lego-block.selected { border-color: var(--blue); box-shadow: 0 8px 24px rgba(6,71,229,.18); }
.lego-block.dragging { box-shadow: 0 16px 38px rgba(6,71,229,.26); opacity: .94; z-index: 100 !important; }

/* Color Coding Themes for Field Types */
.lego-block[data-theme="question"] { border-left: 3px solid var(--blue); }
.lego-block[data-theme="question"]::before { background: var(--blue); }
.lego-block[data-theme="passage"] { background: var(--wash); }
.lego-block[data-theme="passage"]::before { background: var(--blue-soft); }
.lego-block[data-theme="code"] { background: var(--code-bg); border-color: var(--ink); }
.lego-block[data-theme="code"]::before { background: var(--ink); }
.lego-block[data-theme="object"] { border-left: 3px solid var(--ink); }

.lego-head {
  padding: 10px 12px 6px;
  border-bottom: 1px solid var(--pale);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.lego-tag {
  font-family: var(--mono);
  font-size: 8.5px;
  font-weight: 900;
  letter-spacing: .12em;
  color: var(--blue);
  text-transform: uppercase;
}
.lego-meta {
  font-family: var(--mono);
  font-size: 8px;
  font-weight: 750;
  color: var(--muted-dark);
}
.lego-body {
  padding: 10px 12px 12px;
  font-family: var(--serif);
  font-size: 14.5px;
  line-height: 1.48;
  white-space: pre-wrap;
  overflow-wrap: break-word;
}
.lego-block[data-theme="code"] .lego-body {
  font-family: var(--mono);
  font-size: 11px;
  line-height: 1.55;
}

/* Snap Guide Line */
.snap-guide {
  position: absolute;
  background: var(--blue);
  pointer-events: none;
  z-index: 90;
  display: none;
}
.snap-guide.h { height: 1.5px; left: 0; right: 0; }
.snap-guide.v { width: 1.5px; top: 0; bottom: 0; }

/* Long Press Action Menu */
#popMenu {
  position: fixed;
  z-index: 250;
  display: none;
  background: var(--paper);
  border: 1.5px solid var(--blue);
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(6,71,229,.2);
  padding: 4px;
  gap: 4px;
}
#popMenu.open { display: flex; }
.pop-btn {
  height: 32px;
  padding: 0 12px;
  border-radius: 4px;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 850;
  letter-spacing: .06em;
  color: var(--blue);
}
.pop-btn:hover { background: var(--blue-soft); }
.pop-btn.danger { color: #DC2626; }
.pop-btn.danger:hover { background: #FEE2E2; }

/* Slipcase Drawer */
#atlasDrawer {
  position: fixed;
  z-index: 280;
  left: 0;
  right: 0;
  bottom: 0;
  max-height: 72vh;
  background: var(--paper);
  border-top: 1.5px solid var(--blue);
  transform: translateY(102%);
  transition: transform .24s cubic-bezier(.2,.85,.25,1);
  display: flex;
  flex-direction: column;
  padding-bottom: var(--bottom);
}
#atlasDrawer.open { transform: translateY(0); }
.adHead {
  flex: 0 0 auto;
  padding: 11px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--pale);
}
.adTitle { font-family: var(--mono); font-size: 10px; font-weight: 900; color: var(--blue); letter-spacing: .1em; }
.adBody { flex: 1; overflow-y: auto; padding: 12px; }
.adCaseGrid { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 8px; }
.adCaseBtn {
  border: 1.5px solid var(--pale);
  background: var(--paper);
  border-radius: 6px;
  padding: 10px 8px;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
  cursor: pointer;
}
.adCaseBtn:hover { border-color: var(--blue); }
.adCaseId { font-family: var(--mono); font-size: 9px; font-weight: 850; color: var(--blue); }
.adCaseMeta { font-size: 9.5px; color: var(--muted-dark); }

.scrim { position: fixed; inset: 0; z-index: 200; background: rgba(17,19,24,.15); display: none; }
.scrim.open { display: block; }
.toast {
  position: fixed;
  z-index: 400;
  left: 50%;
  bottom: calc(20px + var(--bottom));
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
</style>
</head>
<body>
<div id="app">

  <!-- HEADER -->
  <header>
    <div class="brand-group" id="brandBtn" onclick="location.href='index.html'">
      <svg class="brand-logo-svg" viewBox="0 0 24 24">
        <rect x="2" y="5" width="20" height="15" rx="2"></rect>
        <path d="M4 5V3a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2"></path>
        <line x1="7" y1="10" x2="17" y2="10"></line>
        <line x1="7" y1="14" x2="13" y2="14"></line>
      </svg>
      <div class="brand-text-col">
        <div class="brand-wordmark">SLIPCASE</div>
        <div class="brand-subtitle">STRUCTURAL ATLAS &middot; LEGO GRID</div>
      </div>
    </div>

    <div class="search-wrap">
      <input id="search" class="search" placeholder="Search 1,418 atomic slips..." autocomplete="off">
    </div>

    <button id="drawerOpenBtn" class="accession-badge-btn">DEAL SLIPCASES (32)</button>
  </header>

  <!-- CONTROL BAR -->
  <div class="control-bar">
    <div class="ctrl-group">
      <button class="ctrl-btn" id="zoomOutBtn">&minus; ZOOM</button>
      <button class="ctrl-btn" id="zoomResetBtn">100%</button>
      <button class="ctrl-btn" id="zoomInBtn">&plus; ZOOM</button>
      <span style="font-family:var(--mono);font-size:8.5px;color:var(--grey);margin-left:6px;" id="zoomLabel">100%</span>
    </div>
    <div class="ctrl-group">
      <button class="ctrl-btn" id="snapToggleBtn">GRID SNAP: ON</button>
      <button class="ctrl-btn primary" id="autoBuildBtn">AUTO-BUILD STRUCTURES</button>
      <button class="ctrl-btn" id="clearGridBtn">CLEAR</button>
    </div>
  </div>

  <!-- ATLAS STAGE -->
  <main id="atlasStage">
    <div id="dotGrid"></div>
    <div id="world"></div>
  </main>

  <!-- DRAWER -->
  <section id="atlasDrawer">
    <div class="adHead">
      <span class="adTitle">DEAL SLIPCASE TO LEGO GRID</span>
      <button class="ctrl-btn" id="drawerCloseBtn">CLOSE</button>
    </div>
    <div class="adBody">
      <div class="adCaseGrid" id="adCaseGrid"></div>
    </div>
  </section>
  <div class="scrim" id="drawerScrim"></div>

  <!-- LONG PRESS MENU -->
  <div id="popMenu">
    <button class="pop-btn" id="popCopyBtn">COPY TEXT</button>
    <button class="pop-btn danger" id="popDeleteBtn">RETURN SLIP</button>
  </div>

  <div class="toast" id="toast"></div>
</div>

<script>
window.ZETTEL_DATA = /* DATA_NOTES */;
</script>
<script>
(()=>{
"use strict";

const NOTES = Array.isArray(window.ZETTEL_DATA) ? window.ZETTEL_DATA : [];

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

/* Audio Synthesizer */
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playClick(freq = 720, duration = 0.016) {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(140, audioCtx.currentTime + duration);
    gain.gain.setValueAtTime(0.16, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {}
  if (navigator.vibrate) navigator.vibrate(10);
}

/* State */
let gridSnap = true;
const GRID_STEP = 40;
const BLOCK_W = 280;
const ZOOM_MIN = 0.2, ZOOM_MAX = 2.5;

let viewTransform = { x: 40, y: 40, z: 1 };
let blocks = []; // [{ id, noteId, f, text, x, y, el, theme }]
let nextBlockId = 1;
let selectedBlockId = null;
let activePopBlockId = null;

let isPanning = false, panStart = { x: 0, y: 0 }, panOrigin = { x: 0, y: 0 };
let isDraggingBlock = false, dragStart = { x: 0, y: 0 }, blockOrigin = { x: 0, y: 0 }, currentDragBlock = null;
let longPressTimer = null;

const stage = $("#atlasStage"), world = $("#world"), dotGrid = $("#dotGrid");

function applyTransform() {
  world.style.transform = `translate(${viewTransform.x}px,${viewTransform.y}px) scale(${viewTransform.z})`;
  const g = Math.max(12, GRID_STEP * viewTransform.z);
  dotGrid.style.backgroundSize = g + "px " + g + "px";
  dotGrid.style.backgroundPosition = (viewTransform.x % g) + "px " + (viewTransform.y % g) + "px";
  $("#zoomLabel").textContent = Math.round(viewTransform.z * 100) + "%";
}

function snap(val) {
  return gridSnap ? Math.round(val / GRID_STEP) * GRID_STEP : Math.round(val);
}

function getTheme(f) {
  if (HEAD_FIELD.test(f)) return "question";
  if (f === "PASSAGE" || f === "SOURCE") return "passage";
  if (CODE_FIELD.test(f)) return "code";
  return "object";
}

function createLegoBlock(noteId, f, x, y) {
  const n = NOTES.find(x => x.id === noteId);
  if (!n) return null;
  const text = valueFor(n, f);
  if (!text) return null;

  const theme = getTheme(f);
  const id = nextBlockId++;
  
  const el = document.createElement("article");
  el.className = "lego-block";
  el.dataset.id = id;
  el.dataset.theme = theme;
  el.style.left = x + "px";
  el.style.top = y + "px";
  el.style.zIndex = id;

  el.innerHTML = `
    <div class="lego-head">
      <span class="lego-tag">${esc(f)}</span>
      <span class="lego-meta">${esc(n.id)} &middot; ${esc(n.type)}</span>
    </div>
    <div class="lego-body">${esc(text)}</div>
  `;

  const blockObj = { id, noteId, f, text, x, y, el, theme };
  blocks.push(blockObj);
  world.appendChild(el);
  playClick(640);
  return blockObj;
}

function placeLegoCase(caseIdx) {
  const caseNotes = NOTES.filter(n => n.case_idx === caseIdx);
  if (!caseNotes.length) return;

  const centerWorldX = (innerWidth / 2 - viewTransform.x) / viewTransform.z;
  const centerWorldY = (innerHeight / 2 - viewTransform.y) / viewTransform.z;

  let col = 0, row = 0;
  caseNotes.forEach((n) => {
    FIELD_ORDER.forEach(f => {
      if (valueFor(n, f)) {
        const posX = snap(centerWorldX - 300 + col * (BLOCK_W + 40));
        const posY = snap(centerWorldY - 200 + row * 180);
        createLegoBlock(n.id, f, posX, posY);
        row++;
        if (row >= 4) { row = 0; col++; }
      }
    });
  });
  closeDrawer();
  toast(`Built Lego structure for Case #${caseIdx + 1}`);
}

/* Auto-Build All 31 Cases into Atomic Lego Matrix */
function autoBuildMatrix() {
  world.innerHTML = "";
  blocks = [];
  nextBlockId = 1;

  let globalCol = 0;
  for (let cIdx = 0; cIdx < 31; cIdx++) {
    const cNotes = NOTES.filter(n => n.case_idx === cIdx);
    let row = 0;
    cNotes.forEach(n => {
      FIELD_ORDER.forEach(f => {
        if (valueFor(n, f)) {
          const posX = globalCol * (BLOCK_W + 40);
          const posY = row * 160;
          createLegoBlock(n.id, f, posX, posY);
          row++;
        }
      });
    });
    globalCol++;
  }
  viewTransform = { x: 60, y: 60, z: 0.45 };
  applyTransform();
  toast("Auto-built Lego Matrix across 31 Slipcases");
}

/* Touch & Mouse Pointer Controls */
stage.addEventListener("pointerdown", e => {
  const blockEl = e.target.closest(".lego-block");
  if (blockEl) {
    const bId = +blockEl.dataset.id;
    currentDragBlock = blocks.find(b => b.id === bId);
    if (currentDragBlock) {
      isDraggingBlock = true;
      dragStart = { x: e.clientX, y: e.clientY };
      blockOrigin = { x: currentDragBlock.x, y: currentDragBlock.y };
      blockEl.classList.add("dragging");
      selectedBlockId = bId;

      longPressTimer = setTimeout(() => {
        if (isDraggingBlock) {
          activePopBlockId = bId;
          openPopMenu(e.clientX, e.clientY);
          playClick(900);
        }
      }, 430);
    }
  } else {
    isPanning = true;
    panStart = { x: e.clientX, y: e.clientY };
    panOrigin = { x: viewTransform.x, y: viewTransform.y };
    stage.classList.add("panning");
    closePopMenu();
  }
  stage.setPointerCapture(e.pointerId);
});

stage.addEventListener("pointermove", e => {
  if (isDraggingBlock && currentDragBlock) {
    const dx = (e.clientX - dragStart.x) / viewTransform.z;
    const dy = (e.clientY - dragStart.y) / viewTransform.z;
    if (Math.hypot(dx, dy) > 8) clearTimeout(longPressTimer);

    const rawX = blockOrigin.x + dx;
    const rawY = blockOrigin.y + dy;
    currentDragBlock.x = snap(rawX);
    currentDragBlock.y = snap(rawY);
    currentDragBlock.el.style.left = currentDragBlock.x + "px";
    currentDragBlock.el.style.top = currentDragBlock.y + "px";
  } else if (isPanning) {
    viewTransform.x = panOrigin.x + (e.clientX - panStart.x);
    viewTransform.y = panOrigin.y + (e.clientY - panStart.y);
    applyTransform();
  }
});

stage.addEventListener("pointerup", e => {
  clearTimeout(longPressTimer);
  if (isDraggingBlock && currentDragBlock) {
    currentDragBlock.el.classList.remove("dragging");
    playClick(520);
  }
  isDraggingBlock = false;
  isPanning = false;
  stage.classList.remove("panning");
});

stage.addEventListener("wheel", e => {
  e.preventDefault();
  const factor = e.deltaY < 0 ? 1.1 : 0.9;
  const newZ = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, viewTransform.z * factor));
  const r = newZ / viewTransform.z;
  viewTransform.x = e.clientX - (e.clientX - viewTransform.x) * r;
  viewTransform.y = e.clientY - (e.clientY - viewTransform.y) * r;
  viewTransform.z = newZ;
  applyTransform();
}, { passive: false });

/* Long Press Menu */
function openPopMenu(x, y) {
  const menu = $("#popMenu");
  menu.style.left = Math.min(x, innerWidth - 160) + "px";
  menu.style.top = Math.min(y, innerHeight - 80) + "px";
  menu.classList.add("open");
}

function closePopMenu() {
  $("#popMenu").classList.remove("open");
  activePopBlockId = null;
}

$("#popCopyBtn").onclick = async () => {
  const b = blocks.find(x => x.id === activePopBlockId);
  if (b) {
    try {
      await navigator.clipboard.writeText(`${b.noteId} — ${b.f}\n${b.text}`);
      toast("Copied Lego slip text");
    } catch(e) {}
  }
  closePopMenu();
};

$("#popDeleteBtn").onclick = () => {
  const idx = blocks.findIndex(x => x.id === activePopBlockId);
  if (idx >= 0) {
    blocks[idx].el.remove();
    blocks.splice(idx, 1);
    toast("Returned Lego slip");
  }
  closePopMenu();
};

/* Drawer */
function openDrawer() {
  let html = "";
  for (let i = 0; i < 31; i++) {
    const cNotes = NOTES.filter(n => n.case_idx === i);
    const acc = `SLP / FIELD ${strPad(i + 1)}`;
    html += `
      <div class="adCaseBtn" onclick="placeLegoCase(${i})">
        <div class="adCaseId">${acc}</div>
        <div class="adCaseMeta">${cNotes.length} ZETTELS</div>
      </div>
    `;
  }
  $("#adCaseGrid").innerHTML = html;
  $("#atlasDrawer").classList.add("open");
  $("#drawerScrim").classList.add("open");
}

function closeDrawer() {
  $("#atlasDrawer").classList.remove("open");
  $("#drawerScrim").classList.remove("open");
}

function strPad(n) { return n < 10 ? "00" + n : n < 100 ? "0" + n : "" + n; }

$("#drawerOpenBtn").onclick = openDrawer;
$("#drawerCloseBtn").onclick = closeDrawer;
$("#drawerScrim").onclick = closeDrawer;

/* Zoom Controls */
$("#zoomInBtn").onclick = () => { viewTransform.z = Math.min(ZOOM_MAX, viewTransform.z * 1.25); applyTransform(); };
$("#zoomOutBtn").onclick = () => { viewTransform.z = Math.max(ZOOM_MIN, viewTransform.z * 0.8); applyTransform(); };
$("#zoomResetBtn").onclick = () => { viewTransform = { x: 40, y: 40, z: 1 }; applyTransform(); };

$("#snapToggleBtn").onclick = () => {
  gridSnap = !gridSnap;
  $("#snapToggleBtn").textContent = `GRID SNAP: ${gridSnap ? 'ON' : 'OFF'}`;
  toast(`Grid Snapping ${gridSnap ? 'Enabled' : 'Disabled'}`);
};

$("#autoBuildBtn").onclick = () => autoBuildMatrix();
$("#clearGridBtn").onclick = () => {
  world.innerHTML = "";
  blocks = [];
  toast("Grid cleared");
};

function toast(msg) {
  const t = $("#toast");
  t.textContent = msg;
  t.classList.add("open");
  setTimeout(() => t.classList.remove("open"), 1500);
}

/* Boot */
autoBuildMatrix();
})();
</script>
</body>
</html>
"""

rendered = atlas_template.replace("/* DATA_NOTES */", json.dumps(all_notes))
with open(os.path.join(BASE_DIR, "atlas.html"), "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Generated standalone atlas.html with {len(all_notes)} cards.")
