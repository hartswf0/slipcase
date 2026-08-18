from pathlib import Path
import hashlib,re,json
ROOT=Path(__file__).resolve().parents[1]
fields=['ID','TITLE','SOURCE','PASSAGE','RESEARCH OBJECT','LOCAL MOVE','SOURCE TERMS','WHAT BECAME STRANGE','QUESTION','DEEPER QUESTION','MECHANISM','FORMAL SHIFT','SOURCE FORMALISM','OUR FORMALIZATION','TENSION','MISSING','BOUNDARY','CITATION TRAIL','TEST','PLATFORM','LINKS','BIBTEX']
pat=re.compile(r'(?m)^('+'|'.join(re.escape(x) for x in fields)+r'):\\s*$')
def parse(t):
 m=list(pat.finditer(t)); d={}
 for i,x in enumerate(m): d[x.group(1)]=t[x.end():(m[i+1].start() if i+1<len(m) else len(t))].strip('\\n')
 return d
cards=[]
for p in sorted(ROOT.glob('[0-9][0-9][0-9]__*.txt')):
 t=p.read_text(encoding='utf-8'); d=parse(t)
 if d.get('ID'): cards.append({'id':d['ID'],'title':d.get('TITLE',''),'root_file':p.name,'payload_hash':hashlib.sha256(t.encode()).hexdigest(),'payload':t})
(ROOT/'ZETTELS.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'ZETTELS.jsonl').write_text('\\n'.join(json.dumps(x,ensure_ascii=False) for x in cards)+'\\n',encoding='utf-8')
print('Reindexed',len(cards),'cards. This lightweight script does not rewrite canonical root cards.')
