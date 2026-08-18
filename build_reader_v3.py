import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "slipcases.json"), "r", encoding="utf-8") as f:
    cases = json.load(f)

all_notes = []
for c in cases:
    all_notes.extend(c.get("cards", []))

reader_template = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<title>SLIPCASE — Field Reader v3</title>
<style>
/* SLIPCASE v3.
   Reading is scrolling. Holding is touching. Nothing pages.
   Controls exist only while valid, and live on the thing they change. */
:root{
  --blue:#0647E5;--paper:#fff;--field:#F7F8FA;--ink:#111318;--grey:#9CA3AF;--pale:#E7EEFF;
  --wash:#EFF4FF;--line:1.5px;--top:env(safe-area-inset-top);--bot:env(safe-area-inset-bottom);
  --sans:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif:"Source Serif 4",ui-serif,Georgia,serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--sans)}
button,input{font:inherit;color:inherit}button{border:0;background:none;cursor:pointer;padding:0;text-align:inherit}
button:focus-visible,input:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
#app{position:fixed;inset:0;display:flex;flex-direction:column}

header{flex:0 0 auto;padding:calc(10px + var(--top)) 16px 10px;display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:center;border-bottom:var(--line) solid var(--pale);background:var(--paper);z-index:10}
.wordmark{font-size:12px;font-weight:700;letter-spacing:.42em;color:var(--blue);white-space:nowrap;text-transform:uppercase}
.search{height:38px;border:var(--line) solid var(--pale);border-radius:6px;background:var(--paper);padding:0 12px;outline:0;min-width:0;font-size:13px;font-family:var(--mono)}
.search::placeholder{color:var(--grey)}
.search:focus{border-color:var(--blue)}

#stage{flex:1 1 auto;position:relative;overflow:hidden;background:var(--field);touch-action:pan-y}
.pane{position:absolute;inset:0}
@media(prefers-reduced-motion:no-preference){
  .pane{animation:in .18s ease}
  .pane.fromRight{animation:inR .2s ease}
  .pane.fromLeft{animation:inL .2s ease}
}
@keyframes in{from{opacity:0}to{opacity:1}}
@keyframes inR{from{opacity:0;transform:translateX(18px)}to{opacity:1;transform:none}}
@keyframes inL{from{opacity:0;transform:translateX(-18px)}to{opacity:1;transform:none}}

.fieldGrid{position:absolute;inset:0 0 26px 0;padding:18px 16px 6px;display:grid;grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(3,1fr);gap:12px}
@media(min-width:680px){.fieldGrid{grid-template-columns:repeat(3,1fr);padding:22px;gap:14px}}
@media(min-width:1020px){.fieldGrid{grid-template-columns:repeat(4,1fr);max-width:1180px;left:50%;transform:translateX(-50%);width:100%}}
.caseCard{position:relative;background:var(--paper);border:var(--line) solid var(--pale);border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:10px;min-height:0;text-align:center}
.caseCard:hover,.caseCard:active{border-color:var(--blue)}
.caseCard svg{width:min(56%,106px);height:auto}
.caseId{font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--blue);font-weight:700}
.caseTopic{font-size:11px;line-height:1.25;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;max-width:100%}
.caseCount{font-family:var(--mono);font-size:9px;color:var(--grey);letter-spacing:.06em}
.held{position:absolute;top:8px;right:8px;min-width:18px;height:18px;padding:0 4px;background:var(--blue);color:#fff;font-family:var(--mono);font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;border-radius:3px}
.dotRail{position:absolute;left:0;right:0;bottom:8px;display:flex;justify-content:center;gap:5px}
.dot{width:5px;height:5px;border:1px solid var(--blue);background:var(--paper)}
.dot.on{background:var(--blue)}
.emptyField{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:var(--grey);font-family:var(--mono);font-size:12px;letter-spacing:.06em}

.read{position:absolute;inset:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin}
.doc{max-width:680px;margin:0 auto;padding:0 18px 90px}
.docHead{position:sticky;top:0;background:var(--field);padding:14px 0 10px;border-bottom:var(--line) solid var(--pale);z-index:3;display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.docId{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--blue);white-space:nowrap;font-weight:800}
.docWhere{font-family:var(--mono);font-size:10px;color:var(--grey);letter-spacing:.08em;white-space:nowrap}
.docTags{font-family:var(--mono);font-size:10px;color:var(--grey);letter-spacing:.06em;padding:10px 0 2px}
.slip{position:relative;margin:14px 0;padding:12px 14px 13px 16px;background:var(--paper);border:var(--line) solid var(--pale);border-radius:6px;user-select:none;-webkit-user-select:none}
.slip::before{content:"";position:absolute;left:-1.5px;top:-1.5px;bottom:-1.5px;width:3px;background:transparent;border-radius:4px 0 0 4px}
.slip.on{background:var(--wash);border-color:var(--blue)}
.slip.on::before{background:var(--blue)}
.slip.hit{border-color:var(--blue)}
.fLabel{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;color:var(--blue);margin-bottom:7px;display:flex;justify-content:space-between;gap:8px;font-weight:700}
.fLabel .heldMark{color:var(--blue);opacity:0;font-size:9.5px;letter-spacing:.1em;font-weight:800}
.slip.on .fLabel .heldMark{opacity:1}
.fBody{font-family:var(--serif);font-size:17px;line-height:1.55;white-space:pre-wrap;overflow-wrap:break-word}
.slip[data-kind="head"] .fBody{font-family:var(--sans);font-weight:650;letter-spacing:-.015em;font-size:20px;line-height:1.32}
.slip[data-kind="code"] .fBody{font-family:var(--mono);font-size:12px;line-height:1.6;background:var(--field);padding:10px 12px;margin:-2px -4px 0;border-radius:4px}
.caseBar{position:absolute;top:0;left:0;height:2px;background:var(--blue);z-index:4;transition:width .2s ease}

#chip{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(14px + var(--bot));z-index:20;height:42px;padding:0 18px;background:var(--blue);color:#fff;font-family:var(--mono);font-size:11px;letter-spacing:.12em;display:none;align-items:center;gap:10px;box-shadow:0 4px 18px rgba(6,71,229,.32);border-radius:999px}
#chip.show{display:flex}
#chip .n{background:#fff;color:var(--blue);min-width:20px;height:20px;padding:0 5px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;border-radius:999px}
@media(prefers-reduced-motion:no-preference){#chip.pulse{animation:pulse .28s ease}}
@keyframes pulse{40%{transform:translateX(-50%) scale(1.07)}}

#shade{position:fixed;inset:0;background:rgba(17,19,24,.28);z-index:30;opacity:0;pointer-events:none;transition:opacity .2s}
#shade.show{opacity:1;pointer-events:auto}
#tray{position:fixed;left:0;right:0;bottom:0;z-index:31;background:var(--paper);border-top:var(--line) solid var(--blue);max-height:76vh;display:flex;flex-direction:column;transform:translateY(102%);transition:transform .24s cubic-bezier(.3,.9,.3,1);padding-bottom:var(--bot)}
#tray.show{transform:none}
.trayHead{flex:0 0 auto;display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:var(--line) solid var(--pale)}
.trayTitle{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--blue);font-weight:800}
.trayClear{font-family:var(--mono);font-size:10px;letter-spacing:.1em;color:var(--grey)}
.trayClear:hover{color:var(--blue)}
.trayList{flex:1 1 auto;overflow-y:auto;overscroll-behavior:contain;padding:6px 0 4px}
.tItem{display:grid;grid-template-columns:26px 1fr 34px;align-items:start;gap:6px;padding:9px 12px 9px 8px;border-bottom:1px solid var(--pale);background:var(--paper)}
.tItem.drag{opacity:.35}
.tHandle{width:26px;padding-top:3px;display:flex;flex-direction:column;gap:3px;align-items:center;cursor:grab;touch-action:none}
.tHandle i{display:block;width:14px;height:0;border-top:1.5px solid var(--grey)}
.tBody{min-width:0;text-align:left}
.tMeta{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;color:var(--blue);margin-bottom:3px;font-weight:700}
.tText{font-family:var(--serif);font-size:13px;line-height:1.4;color:var(--ink);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.tItem.open .tText{display:block;-webkit-line-clamp:unset;white-space:pre-wrap}
.tDrop{width:34px;height:26px;display:flex;align-items:center;justify-content:center;color:var(--grey);font-size:16px;line-height:1}
.tDrop:hover{color:var(--blue)}
.trayActs{flex:0 0 auto;display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px 16px calc(12px + var(--bot));border-top:var(--line) solid var(--pale)}
.trayBtn{height:42px;border:var(--line) solid var(--blue);border-radius:6px;color:var(--blue);font-family:var(--mono);font-size:10.5px;font-weight:800;letter-spacing:.12em;display:flex;align-items:center;justify-content:center}
.trayBtn.filled{background:var(--blue);color:#fff}

#toast{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(70px + var(--bot));z-index:40;background:var(--ink);color:#fff;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;padding:9px 14px;opacity:0;pointer-events:none;transition:opacity .18s;border-radius:999px}
#toast.show{opacity:1}
mark{background:var(--pale);color:inherit}
</style>
</head>
<body>
<div id="app">
<header>
  <button class="wordmark" id="homeBtn">Slipcase</button>
  <input id="search" class="search" placeholder="search 1,244 zettels across 31 slipcases" autocomplete="off" aria-label="Search">
</header>
<div id="stage"></div>
</div>

<button id="chip" aria-label="Open tray"><span>TRAY</span><span class="n" id="chipN">0</span></button>
<div id="shade"></div>
<section id="tray" role="dialog" aria-label="Tray">
  <div class="trayHead">
    <span class="trayTitle" id="trayTitle">TRAY</span>
    <button class="trayClear" id="trayClear">CLEAR</button>
  </div>
  <div class="trayList" id="trayList"></div>
  <div class="trayActs">
    <button class="trayBtn" id="copyBtn">COPY ALL</button>
    <button class="trayBtn filled" id="exportBtn">EXPORT .MD</button>
  </div>
</section>
<div id="toast"></div>

<script>
window.ZETTEL_DATA = /* DATA_NOTES */;
</script>
<script>
(()=>{
"use strict";

const LONG_PRESS_MS=430;
const MOVE_CANCEL_PX=10;
const SWIPE_PX=56;
const SWIPE_SLOP=42;
const SEARCH_DEBOUNCE_MS=110;
const MAX_QUERY_TOKENS=8;
const ICON_SLIPS_MAX=5;
const MAX_DOTS=14;
const TOAST_MS=1400;

const FIELD_ORDER=["TITLE","QUESTION","DEEPER QUESTION","PASSAGE","RESEARCH OBJECT","LOCAL MOVE","SOURCE TERMS","WHAT BECAME STRANGE","MECHANISM","FORMAL SHIFT","SOURCE FORMALISM","OUR FORMALIZATION","TENSION","MISSING","BOUNDARY","CITATION TRAIL","TEST","PLATFORM","LINKS","BIBTEX","SOURCE"];
const CODE_FIELD=/FORMAL|BIBTEX|MECHANISM/;
const HEAD_FIELD=/^(TITLE|QUESTION|DEEPER QUESTION)$/;

const notes=Array.isArray(window.ZETTEL_DATA)&&window.ZETTEL_DATA.length?window.ZETTEL_DATA:[];

const ESC={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"};
const esc=s=>String(s??"").replace(/[&<>"']/g,m=>ESC[m]);
const valueFor=(n,f)=>f==="TITLE"?n.title:f==="SOURCE"?n.source:f==="PASSAGE"?n.passage:(n.fields&&n.fields[f])||"";

const CASES=[];
for(let i=0;i<notes.length;i++){
  const n=notes[i],slips=[];let low=(n.id+" "+n.type+" "+n.topic+" "+(n.symbol||"")+" "+n.case_name).toLowerCase();
  for(const f of FIELD_ORDER){
    const v=valueFor(n,f);if(!v)continue;
    const l=(f+" "+v).toLowerCase();low+=" "+l;
    slips.push({f,text:v,low});
  }
  CASES.push({i,slips,low});
}

let view="FIELD";
let qTokens=[];
let filtered=CASES.map((_,k)=>k);
let fieldPage=0,caseK=0,slideDir=0;
let tray=[];
let trayOpen=false;
let searchTimer=0,toastTimer=0;

const $=id=>document.getElementById(id);
const stage=$("stage");
const pageSize=()=>innerWidth>=1020?12:innerWidth>=680?9:6;
const match=low=>{for(const t of qTokens)if(!low.includes(t))return false;return true};
const inTray=(i,f)=>tray.findIndex(t=>t.i===i&&t.f===f);
const heldInCase=i=>tray.reduce((a,t)=>a+(t.i===i?1:0),0);

function toast(msg){
  const t=$("toast");t.textContent=msg;t.classList.add("show");
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>t.classList.remove("show"),TOAST_MS);
}
function haptic(){if(navigator.vibrate)navigator.vibrate(12)}

function hl(text){
  let out=esc(text);
  if(!qTokens.length)return out;
  for(const t of qTokens){
    if(!t)continue;
    const re=new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),"gi");
    out=out.replace(re,m=>"\u0001"+m+"\u0002");
  }
  return out.replace(/\u0001/g,"<mark>").replace(/\u0002/g,"</mark>");
}

function caseIcon(count){
  const n=Math.min(count,ICON_SLIPS_MAX);let s="";
  for(let k=0;k<n;k++){const x=20+k*7,y=16-k*3.5;
    s+=`<rect x="${x}" y="${y}" width="34" height="40" rx="5" fill="#fff" stroke="#0647E5" stroke-width="2.5"/>`}
  return `<svg viewBox="0 0 96 78" aria-hidden="true">${s}
  <path d="M14 34 h68 v38 h-68 z" fill="#fff" stroke="#0647E5" stroke-width="2.5"/>
  <rect x="38" y="48" width="20" height="11" fill="#fff" stroke="#0647E5" stroke-width="2.5"/></svg>`;
}

function renderField(){
  const ps=pageSize(),pages=Math.max(1,Math.ceil(filtered.length/ps));
  fieldPage=Math.min(Math.max(fieldPage,0),pages-1);
  let html="";
  if(!filtered.length)html=`<div class="emptyField">NOTHING IN THE FIELD MATCHES</div>`;
  else{
    const s=fieldPage*ps,e=Math.min(s+ps,filtered.length);let cards="";
    for(let k=s;k<e;k++){
      const c=CASES[filtered[k]],n=notes[c.i],h=heldInCase(c.i);
      cards+=`<button class="caseCard" data-k="${k}">${h?`<span class="held">${h}</span>`:""}${caseIcon(c.slips.length)}<span class="caseId">${esc(n.id)}</span><span class="caseTopic">${esc(n.topic)} · ${esc(n.type)}</span><span class="caseCount">${c.slips.length} SLIPS</span></button>`;
    }
    let dots="";
    if(pages>1&&pages<=MAX_DOTS)for(let p=0;p<pages;p++)dots+=`<span class="dot${p===fieldPage?" on":""}"></span>`;
    html=`<div class="fieldGrid">${cards}</div><div class="dotRail">${dots}</div>`;
  }
  const cls=slideDir>0?"fromRight":slideDir<0?"fromLeft":"";
  stage.innerHTML=`<div class="pane ${cls}">${html}</div>`;slideDir=0;
}

function renderRead(keepScroll){
  const c=CASES[filtered[caseK]],n=notes[c.i];
  let body="";
  for(let s=0;s<c.slips.length;s++){
    const slip=c.slips[s];
    const kind=CODE_FIELD.test(slip.f)?"code":HEAD_FIELD.test(slip.f)?"head":"text";
    const on=inTray(c.i,slip.f)>=0;
    const hit=qTokens.length&&match(slip.low);
    body+=`<div class="slip${on?" on":""}${hit?" hit":""}" data-s="${s}" data-kind="${kind}">
      <div class="fLabel"><span>${esc(slip.f)}</span><span class="heldMark">HELD</span></div>
      <div class="fBody">${hl(slip.text)}</div></div>`;
  }
  const pct=filtered.length>1?((caseK+1)/filtered.length*100):100;
  const cls=slideDir>0?"fromRight":slideDir<0?"fromLeft":"";
  stage.innerHTML=`<div class="pane ${cls}"><div class="caseBar" style="width:${pct}%"></div>
    <div class="read" id="readScroll"><div class="doc">
      <div class="docHead"><span class="docId">${esc(n.id)}</span><span class="docWhere">${caseK+1} / ${filtered.length}</span></div>
      <div class="docTags">${esc(n.type)} · ${esc(n.topic)}${n.symbol?" · "+esc(n.symbol):""}</div>
      ${body}
    </div></div></div>`;
  slideDir=0;
  if(keepScroll!=null)$("readScroll").scrollTop=keepScroll;
}

function render(keepScroll){view==="FIELD"?renderField():renderRead(keepScroll)}

function syncChip(pulse){
  const chip=$("chip");
  chip.classList.toggle("show",tray.length>0);
  $("chipN").textContent=tray.length;
  if(pulse){chip.classList.remove("pulse");void chip.offsetWidth;chip.classList.add("pulse")}
  if(!tray.length&&trayOpen)closeTray();
}

function toggleHold(s){
  const c=CASES[filtered[caseK]],slip=c.slips[s],at=inTray(c.i,slip.f);
  const el=stage.querySelector(`.slip[data-s="${s}"]`);
  if(at>=0){tray.splice(at,1);el&&el.classList.remove("on")}
  else{tray.push({i:c.i,f:slip.f});el&&el.classList.add("on");haptic()}
  syncChip(at<0);
  if(trayOpen)renderTray();
}
async function copySlip(s){
  const c=CASES[filtered[caseK]],slip=c.slips[s],n=notes[c.i];
  try{await navigator.clipboard.writeText(n.id+" — "+slip.f+"\n"+slip.text);haptic();toast("COPIED "+slip.f)}
  catch(e){toast("COPY UNAVAILABLE")}
}

function openTray(){trayOpen=true;renderTray();$("shade").classList.add("show");$("tray").classList.add("show")}
function closeTray(){trayOpen=false;$("shade").classList.remove("show");$("tray").classList.remove("show")}
function renderTray(){
  $("trayTitle").textContent="TRAY · "+tray.length+" SLIP"+(tray.length===1?"":"S");
  let html="";
  for(let t=0;t<tray.length;t++){
    const e=tray[t],n=notes[e.i];
    html+=`<div class="tItem" data-t="${t}">
      <div class="tHandle" data-h="${t}" aria-label="Reorder"><i></i><i></i><i></i></div>
      <button class="tBody" data-b="${t}"><div class="tMeta">${esc(n.id)} — ${esc(e.f)}</div><div class="tText">${esc(valueFor(n,e.f))}</div></button>
      <button class="tDrop" data-x="${t}" aria-label="Remove">×</button></div>`;
  }
  $("trayList").innerHTML=html;
}
function trayText(){
  return tray.map(e=>notes[e.i].id+" — "+e.f+"\n"+valueFor(notes[e.i],e.f)).join("\n\n");
}
function trayMarkdown(){
  let out="# SLIPCASE TRAY\n\n";
  for(const e of tray){const n=notes[e.i];
    out+="## "+n.id+" · "+e.f+"\n\n"+valueFor(n,e.f)+"\n\n---\n\n"}
  return out;
}

let press=null;
stage.addEventListener("pointerdown",e=>{
  const slipEl=e.target.closest(".slip");
  press={x:e.clientX,y:e.clientY,slipEl,long:false,moved:false,timer:0};
  if(slipEl&&view==="READ"){
    press.timer=setTimeout(()=>{if(press&&!press.moved){press.long=true;copySlip(+slipEl.dataset.s)}},LONG_PRESS_MS);
  }
});
stage.addEventListener("pointermove",e=>{
  if(!press)return;
  if(Math.hypot(e.clientX-press.x,e.clientY-press.y)>MOVE_CANCEL_PX){press.moved=true;clearTimeout(press.timer)}
});
stage.addEventListener("pointerup",e=>{
  if(!press)return;clearTimeout(press.timer);
  const dx=e.clientX-press.x,dy=e.clientY-press.y,p=press;press=null;
  if(Math.abs(dx)>=SWIPE_PX&&Math.abs(dy)<SWIPE_SLOP){
    const dir=dx<0?1:-1;
    if(view==="FIELD"){const pages=Math.max(1,Math.ceil(filtered.length/pageSize()));
      if(fieldPage+dir>=0&&fieldPage+dir<pages){fieldPage+=dir;slideDir=dir;renderField()}return}
    if(caseK+dir>=0&&caseK+dir<filtered.length){caseK+=dir;slideDir=dir;renderRead()}return;
  }
  if(p.moved||p.long)return;
  const card=e.target.closest(".caseCard");
  if(card){caseK=+card.dataset.k;slideDir=1;view="READ";renderRead();return}
  const slipEl=e.target.closest(".slip");
  if(slipEl&&view==="READ")toggleHold(+slipEl.dataset.s);
});
stage.addEventListener("pointercancel",()=>{if(press){clearTimeout(press.timer);press=null}});
stage.addEventListener("contextmenu",e=>{if(e.target.closest(".slip"))e.preventDefault()});

$("homeBtn").addEventListener("click",()=>{view="FIELD";render()});
$("chip").addEventListener("click",openTray);
$("shade").addEventListener("click",closeTray);
$("trayClear").addEventListener("click",()=>{tray=[];syncChip(false);renderTray();render()});
$("copyBtn").addEventListener("click",async()=>{
  try{await navigator.clipboard.writeText(trayText());toast("COPIED "+tray.length+" SLIPS")}
  catch(e){toast("COPY UNAVAILABLE")}
});
$("exportBtn").addEventListener("click",()=>{
  const blob=new Blob([trayMarkdown()],{type:"text/markdown"});
  const a=document.createElement("a");a.href=URL.createObjectURL(blob);
  a.download="slipcase-tray.md";a.click();URL.revokeObjectURL(a.href);
  toast("EXPORTED "+tray.length+" SLIPS");
});

$("trayList").addEventListener("click",e=>{
  const x=e.target.closest("[data-x]");
  if(x){tray.splice(+x.dataset.x,1);syncChip(false);renderTray();render();return}
  const b=e.target.closest("[data-b]");
  if(b)b.closest(".tItem").classList.toggle("open");
});
let drag=null;
$("trayList").addEventListener("pointerdown",e=>{
  const h=e.target.closest("[data-h]");if(!h)return;
  e.preventDefault();
  const item=h.closest(".tItem");
  drag={from:+h.dataset.h,y:e.clientY,hRow:item.offsetHeight,el:item};
  item.classList.add("drag");
  h.setPointerCapture(e.pointerId);
});
$("trayList").addEventListener("pointermove",e=>{
  if(!drag)return;
  const shift=Math.round((e.clientY-drag.y)/drag.hRow);
  const to=Math.min(Math.max(drag.from+shift,0),tray.length-1);
  if(to!==drag.from){
    const[m]=tray.splice(drag.from,1);tray.splice(to,0,m);
    drag.from=to;drag.y=e.clientY;
    renderTray();
    const el=$("trayList").querySelector(`.tItem[data-t="${to}"]`);
    if(el){el.classList.add("drag");drag.el=el}
  }
});
const endDrag=()=>{if(drag){drag.el&&drag.el.classList.remove("drag");drag=null}};
$("trayList").addEventListener("pointerup",endDrag);
$("trayList").addEventListener("pointercancel",endDrag);

document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT")return;
  if(e.key==="Escape"){trayOpen?closeTray():(view="FIELD",render());return}
  if(e.key==="t"&&tray.length){trayOpen?closeTray():openTray();return}
  const dir=e.key==="ArrowRight"||e.key==="j"?1:e.key==="ArrowLeft"||e.key==="k"?-1:0;
  if(!dir)return;
  if(view==="FIELD"){const pages=Math.max(1,Math.ceil(filtered.length/pageSize()));
    if(fieldPage+dir>=0&&fieldPage+dir<pages){fieldPage+=dir;slideDir=dir;renderField()}}
  else if(caseK+dir>=0&&caseK+dir<filtered.length){caseK+=dir;slideDir=dir;renderRead()}
});

$("search").addEventListener("input",e=>{
  clearTimeout(searchTimer);
  searchTimer=setTimeout(()=>{
    qTokens=e.target.value.trim().toLowerCase().split(/\s+/).filter(Boolean).slice(0,MAX_QUERY_TOKENS);
    filtered=[];
    for(let k=0;k<CASES.length;k++)if(!qTokens.length||match(CASES[k].low))filtered.push(k);
    fieldPage=0;caseK=0;view="FIELD";render();
  },SEARCH_DEBOUNCE_MS);
});
addEventListener("resize",()=>{if(view==="FIELD")renderField()});

syncChip(false);
render();
})();
</script>
</body>
</html>
"""

rendered = reader_template.replace("/* DATA_NOTES */", json.dumps(all_notes))
with open(os.path.join(BASE_DIR, "slipcase-reader-v3.html"), "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Generated standalone slipcase-reader-v3.html with {len(all_notes)} cards.")
