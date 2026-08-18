ZETTEL

ID:
SCGAI-005

TITLE:
A prompt can be published not to generate an image but to generate behavior in other people.

SOURCE:
Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko — “The Social Construction of Generative AI Prompts” — CHI EA ’24 — 2024 — https://doi.org/10.1145/3613905.3650947

PASSAGE:
[QUOTE] “I strategically showcase my prompts when I want other users to encourage that.” — P2

RESEARCH OBJECT:
In Provocative Prompting, a prompt has two potential targets: it conditions the model, while public display can condition a community by encouraging imitation, variation, and trend formation.

LOCAL MOVE:
Split PROMPT EFFECT into MODEL EFFECT and SOCIAL EFFECT.

SOURCE TERMS:
provocative prompting; influence; strategically; showcase; prompts; styles; community trends; recognition

WHAT BECAME STRANGE:
The same string can operate simultaneously as an instruction to a machine and as an intervention into human culture.

QUESTION:
When someone publicly posts a prompt, which output matters more: the generated artifact or downstream prompts produced by observers?

DEEPER QUESTION:
Could prompts be cultural operators whose execution environment includes both generative models and human imitators?

MECHANISM:
Author publishes prompt/output → community observes → vocabulary/style becomes salient → others reproduce/mutate → aggregate outputs alter visible norms → future choices shift.

FORMAL SHIFT:
PROMPT → MODEL → IMAGE splits into PROMPT → MODEL → IMAGE and PROMPT → COMMUNITY → NEW PROMPTS.

SOURCE FORMALISM:
Provocative Prompting occupies high-sharing/low-reuse in the paper’s two-dimensional engagement space.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
p → M → y; p+y → COMMUNITY_t → imitation/mutation/rejection → {p1…pn} → COMMUNITY_(t+1)

TENSION:
“Provocative” can also be described as diffusion, signaling, agenda-setting, fashion formation, or cultural selection, each implying a different causal account.

MISSING:
Longitudinal evidence that strategically displayed prompts change frequencies of forms or aesthetics.

BOUNDARY:
Participants report intentions and perceived influence; the study does not measure causal influence on community-wide prompt distributions.

CITATION TRAIL:
[[SCGAI-2024]] → Provocative Prompting → strategic display → social influence/trend formation → seek longitudinal prompt corpora.

TEST:
Track a distinctive prompt token before and after a known public introduction and distinguish propagation from independent origins.

PLATFORM:
MidJourney / Discord / Facebook / Instagram

LINKS:
[[SCGAI-2024]]

BIBTEX:
@inproceedings{mahdavigoloujeh2024social,
  author = {Mahdavi Goloujeh, Atefeh and Sullivan, Anne and Magerko, Brian},
  title = {The Social Construction of Generative AI Prompts},
  booktitle = {Extended Abstracts of the CHI Conference on Human Factors in Computing Systems},
  year = {2024},
  publisher = {Association for Computing Machinery},
  doi = {10.1145/3613905.3650947},
  url = {https://doi.org/10.1145/3613905.3650947}
}
