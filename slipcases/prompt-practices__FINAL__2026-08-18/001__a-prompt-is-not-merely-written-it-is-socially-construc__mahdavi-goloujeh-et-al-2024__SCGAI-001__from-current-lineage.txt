ZETTEL

ID:
SCGAI-001

TITLE:
A prompt is not merely written; it is socially constructed.

SOURCE:
Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko — “The Social Construction of Generative AI Prompts” — CHI EA ’24 — 2024 — https://doi.org/10.1145/3613905.3650947

PASSAGE:
[QUOTE] “prompts are socially constructed and shaped by the interests and values of diverse groups [13], rather than happening in a social vacuum.”

RESEARCH OBJECT:
The paper relocates the prompt from the individual-model interface into a social field. Prompt wording is partly produced by communities that circulate examples, establish norms, attach values to reuse, and teach what counts as effective or legitimate prompting.

LOCAL MOVE:
Replace PROMPT-AS-INSTRUCTION with PROMPT-AS-SOCIOTECHNICAL-OBJECT.

SOURCE TERMS:
socially constructed; interests; values; social vacuum; prompt adaptation; sharing; peer learning; collective knowledge building

WHAT BECAME STRANGE:
The apparently private act of typing a sentence may contain an invisible population of prior prompt writers, tutorials, platform conventions, copied modifiers, aesthetic trends, and prohibitions.

QUESTION:
Where does the boundary of a prompt end: at the typed string, the user’s accumulated repertoire, or the community that made that repertoire available?

DEEPER QUESTION:
Could prompt execution be modeled as an act performed by a distributed social system rather than an isolated human user?

MECHANISM:
Community examples circulate → users observe reusable forms → forms enter individual repertoires → prompts generate outputs → outputs/prompts recirculate → subsequent prompting changes.

FORMAL SHIFT:
INDIVIDUAL USER → PROMPT → MODEL becomes COMMUNITY → USER REPERTOIRE → PROMPT → MODEL → SHARED OUTPUT → COMMUNITY.

SOURCE FORMALISM:
The paper organizes prompting through Prompt Sharing and Prompt Reuse, producing four orientations: Proprietary/Solitary, Derivative, Collaborative, and Provocative.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
COMMUNITY(t) → available_prompt_forms(t) → USER_REPERTOIRE(t) → PROMPT(t) → OUTPUT(t) → COMMUNITY(t+1)

TENSION:
“Social construction” can mean that people learn prompting socially, or the stronger claim that the prompt itself is constituted by collective practices. The paper directly establishes the former more strongly than the latter.

MISSING:
A traceable genealogy showing how a specific prompt fragment moves through multiple users and changes along the way.

BOUNDARY:
The study concerns 19 US-based MidJourney users and English-language prompting; it does not establish identical mechanisms across models, languages, or communities.

CITATION TRAIL:
[[SCGAI-2024]] → social-construction claim → Social Construction of Technology [13] → ask how relevant social groups constitute the artifact.

TEST:
Take one widely circulated prompt formula and reconstruct earliest observable appearances, modifications, communities of circulation, and ownership claims.

PLATFORM:
MidJourney / Discord / Facebook prompt communities

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
