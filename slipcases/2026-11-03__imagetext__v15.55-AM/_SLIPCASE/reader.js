const D=JSON.parse(document.querySelector('#data').textContent);
const screen=document.querySelector('#screen'), search=document.querySelector('#search');
const cardBy=Object.fromEntries(D.cards.map(c=>[c.sha256,c]));
let mode=matchMedia('(max-width:650px)').matches?'READ':'DECK', selected=D.cards[0], pin=null, trail=[];
const h=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const button=(label,key,value='')=>`<button data-action="${key}" data-value="${h(value)}">${h(label)}</button>`;
const modes=['DECK','READ','GRAPH','SOURCES','BIBLIOGRAPHY','GHOSTS','MOCs','TRAIL'];
document.querySelector('#nav').innerHTML=modes.map(m=>button(m,'mode',m)).join('')+button('Surprise','surprise')+button('Provenance','mode','PROVENANCE');
function select(c){selected=c;mode='READ';if(trail.at(-1)!==c)trail.push(c);render();}
function address(id){const n=D.nodes[id];return button(n.label,'node',id);}
function relations(id){return D.edges.filter(e=>e.source===id);}
function article(c){
 const native=relations(c.sha256).filter(e=>['MEMBER_OF','LINKS_TO','WIKILINKS_TO'].includes(e.type));let k=0;
 const payload=c.payload.split(/(\[\[[^\]]+\]\])/g).map((s,i)=>i%2?button(s,'node',native[k++].target):h(s)).join('');
 const neighborhood=relations(c.sha256).filter(e=>['BACKLINK','MEMBER_OF','LINKS_TO','WIKILINKS_TO','USES_SOURCE'].includes(e.type));
 return `<article><small>${h(c.id)} · ${h(c.sha256)}</small><h2>${h(c.title)}</h2><div class="actions">${button(pin===c?'Unpin':'Pin for comparison','pin',c.sha256)}${button('Copy BibTeX','bib',c.sha256)}</div><details open><summary>Neighborhood and backlinks</summary><ul>${neighborhood.map(e=>`<li>${h(e.type)} · ${address(e.target)}</li>`).join('')}</ul></details><details open><summary>Card payload</summary><pre>${payload}</pre></details></article>`;
}
function showNode(id){
 if(cardBy[id]){select(cardBy[id]);return;}
 const n=D.nodes[id];if(!n)return;
 const links=relations(id);
 screen.innerHTML=`<article><small>${h(n.type)}</small><h2>${h(n.label)}</h2>${n.url?`<a href="${h(n.url)}">Open source</a>`:''}<ul>${links.map(e=>`<li>${h(e.type)} · ${address(e.target)} · ${h(e.field)}</li>`).join('')}</ul><pre>${h(JSON.stringify(n,null,2))}</pre></article>`;
}
function render(){
 const q=search.value.trim().toLowerCase();
 if(q||mode==='DECK'){
   const rows=D.cards.filter(c=>!q||(c.payload+' '+c.file).toLowerCase().includes(q));
   screen.innerHTML='<h2>Deck</h2><div class="deck">'+rows.map(c=>button(c.id+' · '+c.title,'node',c.sha256)).join('')+'</div>'+(rows.length?'':'<p>No cards found.</p>');return;
 }
 if(mode==='READ'){screen.innerHTML=pin&&pin!==selected?'<div class="pair">'+article(pin)+article(selected)+'</div>':article(selected);return;}
 if(mode==='GRAPH'){screen.innerHTML='<h2>Graph</h2><ul>'+D.edges.map(e=>`<li>${address(e.source)} → ${address(e.target)} · ${h(e.type)} · ${h(e.field)}</li>`).join('')+'</ul>';return;}
 if(mode==='SOURCES'){screen.innerHTML='<h2>Source receipts</h2><ul>'+D.resources.map(r=>`<li><a href="${h(r.url)}">${h(r.label)}</a> · ${h(r.state)} · ${h(r.used_by.join(', '))}</li>`).join('')+'</ul>';return;}
 if(mode==='GHOSTS'){screen.innerHTML='<h2>Open addresses</h2><ul>'+Object.values(D.nodes).filter(n=>n.type==='GHOST').map(n=>`<li>${address(n.id)} · ${n.count}</li>`).join('')+'</ul>';return;}
 if(mode==='TRAIL'){screen.innerHTML='<h2>Session trail</h2><ol>'+trail.map(c=>`<li>${address(c.sha256)}</li>`).join('')+'</ol><pre>'+h(D.views['_ARRANGEMENTS/research-trails.json'])+'</pre>';return;}
 if(mode==='MOCs'){screen.innerHTML='<h2>Maps of content</h2><pre>'+h(D.views['_MOCS/description.md'])+'</pre>';return;}
 if(mode==='BIBLIOGRAPHY'){screen.innerHTML='<h2>Bibliography</h2>'+button('Copy bibliography','copyall')+'<pre>'+h(D.bib)+'</pre>';return;}
 screen.innerHTML=Object.entries(D.views).map(([k,v])=>`<details><summary>${h(k)}</summary><pre>${h(v)}</pre></details>`).join('')+'<details><summary>Manifest and hashes</summary><pre>'+h(JSON.stringify(D.manifest,null,2))+'</pre></details>';
}
function copy(text){
 const area=document.createElement('textarea');area.value=text;screen.prepend(area);area.select();
 try{if(document.execCommand('copy'))area.remove();}catch(e){}
}
document.addEventListener('click',ev=>{
 const b=ev.target.closest('[data-action]');if(!b)return;const a=b.dataset.action,v=b.dataset.value;
 if(a==='mode'){search.value='';mode=v;render();}
 if(a==='node'){search.value='';showNode(v);}
 if(a==='surprise'){search.value='';select(D.cards[Math.floor(Math.random()*D.cards.length)]);}
 if(a==='pin'){pin=pin===cardBy[v]?null:cardBy[v];render();}
 if(a==='bib')copy(cardBy[v].payload.split('\nBIBTEX:\n').at(-1));
 if(a==='copyall')copy(D.bib);
});
search.addEventListener('input',render);
function file(id,type){
 const data=document.querySelector('#'+id).textContent;
 if(!data)return '';
 return URL.createObjectURL(new Blob([Uint8Array.from(atob(data),c=>c.charCodeAt(0))],{type}));
}
const p=file('pdf-data','application/pdf');document.querySelector('#paper').href=p;
document.querySelector('#preview').src=p;
const kit=file('rebuild-kit','application/zip');const ka=document.querySelector('#kit');if(kit)ka.href=kit;else ka.hidden=true;
trail.push(selected);render();
