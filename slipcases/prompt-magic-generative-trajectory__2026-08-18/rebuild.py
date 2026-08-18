from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parent
cards=[]
for p in sorted(p for p in root.glob('[0-9][0-9][0-9]__*.txt') if re.match(r'^(?!000)\d{3}__',p.name)):
    body=p.read_text(encoding='utf-8')
    def F(n):
        m=re.search(r'\n'+re.escape(n)+r':\n(.*?)(?=\n\n[A-Z][A-Z ]+:\n|\Z)',body,re.S);return m.group(1).strip() if m else ''
    cards.append({'filename':p.name,'payload':body,'sha256':hashlib.sha256(body.encode()).hexdigest(),'ID':F('ID'),'TITLE':F('TITLE'),'LINKS':F('LINKS'),'PLATFORM':F('PLATFORM')})
(root/'ZETTELS.rebuilt.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')
print('rebuilt',len(cards),'cards')
