ZETTEL

ID:
Z-RF-20260817-006

TITLE:
The minority prompt corrects downstream while the bias remains upstream.

SOURCE:
Felipe Rivas San Martín — Un Archivo Inexistente — Écfrasis, 2024 — “Un prompt minoritario,” pp. 46–50.

PASSAGE:
[PARAPHRASE]
Rivas says prompts are his only direct point of intervention in the Stable Diffusion workflow he describes, while the model’s algorithmic configuration and training database arrive already given and are not neutral. He proposes the “prompt minoritario” specifically to counter biases manifested in those prior conditions.

RESEARCH OBJECT:
A minority prompt is a downstream compensatory operation against upstream conditions the artist does not control.

LOCAL MOVE:
This qualifies [[Z-AIACS-006]]. The source does not simply relocate governance to the user; it makes visible an asymmetry between the layer where bias originates and the layer where the artist can intervene.

SOURCE TERMS:
“única incidencia”
“configuración algorítmica”
“base de entrenamiento”
“no son neutrales”
“prompt minoritario”
“contrarrestar”

WHAT BECAME STRANGE:
The person asked to repair representation may have access only to the least structural layer of the system.

QUESTION:
When a prompt compensates successfully for biased priors without altering them, has anything in the underlying representational system actually been corrected?

DEEPER QUESTION:
Should prompt-based bias correction be understood as agency, workaround, accessibility technique, invisible labor, or all four?

MECHANISM:
upstream training/configuration bias
→ skewed baseline generation
→ user observes mismatch
→ minority prompt adds counter-conditioning
→ locally altered output
→ upstream distribution remains unchanged

FORMAL SHIFT:
<UPSTREAM BIAS>
→ <DEFAULT GENERATIVE TENDENCY>
→ [DOWNSTREAM COUNTER-PROMPT]
→ <LOCAL REPRESENTATIONAL REPAIR>

SOURCE FORMALISM:
Rivas gives concrete examples in which requests for two men yielded classed or racialized defaults, then describes modifying prompt instructions to counter the training-data tendencies.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

STRUCTURAL_REPAIR changes M

COMPENSATORY_REPAIR changes conditioning c

G(M, c)
→ mismatch

G(M, c + counter_condition)
→ desired local result

while M remains fixed.

TENSION:
[[Z-AIACS-006]] asked whether representational governance had been relocated to users. Rivas’s account suggests something harsher: responsibility for local correction may be displaced to the user while authority over the causal substrate remains elsewhere.

MISSING:
Evidence comparing the amount of corrective prompting required across represented groups and determining whether repeated user corrections ever feed back into model or platform changes.

BOUNDARY:
Rivas documents his own artistic practice and theorizes “prompt minoritario.” The source does not establish that every successful corrective prompt leaves every relevant system layer unchanged.

CITATION TRAIL:
[[Z-AIACS-006]]
→ Rivas San Martín, “Un prompt minoritario”
→ only point of artist intervention versus predetermined model/database
→ distinguish compensatory from structural repair
→ measure corrective labor

TEST:
Create matched requests varying one represented social category at a time. Give users a fixed success criterion and measure iterations, added tokens, negative constraints, and time required to reach it. Repeat after model updates to see whether corrective labor decreases or merely changes vocabulary.

PLATFORM:
[[Minority Prompt]]

LINKS:
[[Z-AIACS-006]]
[[Corrective Description]]
[[Compensatory Labor]]
[[Representational Governance]]

BIBTEX:
@book{RivasSanMartin2024Archivo,
  author = {Felipe Rivas San Martín},
  title = {Un Archivo Inexistente},
  publisher = {Écfrasis, ediciones},
  address = {Santiago},
  year = {2024},
  isbn = {978-956-09200-7-2}
}
