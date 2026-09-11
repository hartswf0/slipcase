from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
MAP = ROOT / 'heads-pdf-map.json'

OVERRIDES = {
    '2026-08-21__when-meaning-gets-to-work__CULTUREOS-20260821-1443': {
        'case_title': 'WHEN MEANING GETS TO WORK — CULTURAL RUNTIME',
        'title': 'WHEN MEANING GETS TO WORK — CULTURAL RUNTIME — HEAD',
        'question': 'Through what arrangements do symbolic forms acquire practical consequences?',
        'thesis': 'Cultural forms do not carry their practical consequences inside themselves. Their practical careers are assembled through persons, offices, artifacts, classifications, temporal arrangements, infrastructures, trained capacities, interfaces, and repair practices. “Runtime” names the analytic question of how meaning gets to work; it is not a claim that culture is software.'
    },
    '2026-08-22__floor-bee-blank-box__CHAT-PAPER-ZETTEL-FIELD': {
        'case_title': 'THE FLOOR, THE BEE, AND THE BLANK BOX',
        'title': 'THE FLOOR, THE BEE, AND THE BLANK BOX — HEAD',
        'question': 'What does the work think the participant did?',
        'thesis': 'Participation is treated here as an attribution problem rather than a checklist of inputs. The portable practice is to probe the edge, then follow what survives: test what the work recognizes, ignores, permits, refuses, or carries forward as participant action.'
    },
    '2026-09-01__the-model-is-training-you__MODEL-TRAINING-YOU-2026-09-01': {
        'case_title': 'THE MODEL IS TRAINING YOU',
        'title': 'THE MODEL IS TRAINING YOU — HEAD',
        'question': 'What changes in human practice when prompt engineering reformats the environment into machine-legible form?',
        'thesis': 'Prompt engineering also reformats the human environment into machine-legible form. The paper asks how prompt formats classify and silence distinctions, how success can masquerade as causal explanation, and how reversible legibility might preserve routes back to evidence, ambiguity, and alternative interpretation.'
    },
    'slipcase_ontology_build': {
        'case_title': 'THE VANISHING PROMPT — BOUNDEDNESS / CAUSALITY',
        'title': 'THE VANISHING PROMPT — BOUNDEDNESS / CAUSALITY — HEAD',
        'question': 'What kind of thing is a prompt if making it causally adequate makes it cease to be a prompt?',
        'thesis': 'Prompt scholarship faces a boundedness–causality dilemma. A thin prompt is bounded, portable, and experimentally convenient but causally incomplete; a thick prompt absorbs the conditions needed to explain behavior but expands toward situated execution and loses the identity that made it a prompt. This is a testable pressure on prompt ontologies, not a solved ontology.'
    },
}

def replace_section(text, field, value):
    pat = rf'(^' + re.escape(field) + r':\s*\n)(.*?)(?=\n[A-Z][A-Z0-9 _/\-]{2,40}:\s*\n|\Z)'
    return re.sub(pat, lambda m: m.group(1) + value.strip() + '\n', text, count=1, flags=re.M | re.S)

mapping = json.loads(MAP.read_text(encoding='utf-8'))
by_case = {h['case_id']: h for h in mapping['heads']}

for case_id, values in OVERRIDES.items():
    h = by_case.get(case_id)
    if not h:
        raise SystemExit(f'missing head for override: {case_id}')
    h.update(values)
    p = ROOT / 'slipcases' / case_id / f"000A__HEAD__FIELD-{h['field_no']:03d}.txt"
    text = p.read_text(encoding='utf-8')
    text = replace_section(text, 'TITLE', h['title'])
    text = replace_section(text, 'TOPIC', h['case_title'])
    text = replace_section(text, 'QUESTION', h['question'])
    text = replace_section(text, 'THESIS', h['thesis'])
    p.write_text(text, encoding='utf-8')

MAP.write_text(json.dumps(mapping, indent=2), encoding='utf-8')

# Rebuild the plain-text head/PDF map from the refined canonical objects.
head_by_case = {h['case_id']: h for h in mapping['heads']}
lines = [
    'SLIPCASE — HEAD ZETTEL / PDF MAP',
    f"{mapping['counts']['heads']} HEADS · {mapping['counts']['pdfs']} PDFs",
    '',
    'INVARIANT',
    'Every case has exactly one HEAD ZETTEL. Every PDF has exactly one home HEAD.',
    'Additional PDF→HEAD edges are lexical leads, not source-grounded claims.',
    '',
]
for h in mapping['heads']:
    lines += [
        f"{h['id']}  {h['title']}",
        f"CASE: {h['case_id']}",
        f"QUESTION: {h['question']}",
        f"THESIS: {h['thesis']}",
        f"CHILDREN: {h['child_count']}",
        f"PDFS: {h['pdf_count']}",
    ]
    for p in h['pdfs']:
        lines.append(f"  → {p['name']}")
    for b in h.get('bridges', [])[:8]:
        lines.append(f"  ↔ {head_by_case[b['case_id']]['id']}  ({b['weight']} explicit card links)")
    lines.append('')
(ROOT / 'heads-pdf-map.txt').write_text('\n'.join(lines), encoding='utf-8')

# Replace the embedded data object in the interactive HTML without touching its UI.
html_path = ROOT / 'heads-pdf-map.html'
html = html_path.read_text(encoding='utf-8')
data_js = json.dumps(mapping, separators=(',', ':')).replace('</', '<\\/')
html, n = re.subn(r'const D=.*?;const heads=', 'const D=' + data_js + ';const heads=', html, count=1, flags=re.S)
if n != 1:
    raise SystemExit('could not locate embedded HEAD map data in heads-pdf-map.html')
html_path.write_text(html, encoding='utf-8')

print(f"Refined {len(OVERRIDES)} sparse/projection HEADs from preserved field sources.")
