ZETTEL

ID:
SCGAI-003

TITLE:
Collaborative prompting makes the history of modification part of the creative object.

SOURCE:
Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko — “The Social Construction of Generative AI Prompts” — CHI EA ’24 — 2024 — https://doi.org/10.1145/3613905.3650947

PASSAGE:
[QUOTE] “Set a goal and then try and work through the journey of getting there collectively and letting people see like how prompts modify over time.” — P7

RESEARCH OBJECT:
Collaboration includes exposing the temporal sequence through which a prompt changes. The trajectory of revisions becomes visible and socially useful.

LOCAL MOVE:
Move the unit of analysis from PROMPT to PROMPT-HISTORY.

SOURCE TERMS:
goal; collectively; journey; prompts modify over time; collaborative effort; tips and tricks

WHAT BECAME STRANGE:
The final prompt may be less informative than the sequence of failed and successful transformations that produced it.

QUESTION:
What becomes visible if prompt research records lineage rather than final strings?

DEEPER QUESTION:
Is a mature prompt better represented as a version-controlled process than as a piece of natural-language text?

MECHANISM:
Shared goal → prompt version → execution → output evaluation → collective modification → next version → accumulated visible history.

FORMAL SHIFT:
PROMPT = STRING becomes PROMPT = VERSIONED TRAJECTORY.

SOURCE FORMALISM:
The paper describes collaborative experiments in which groups iteratively build on prompts, share discoveries, and observe how prompts change over time.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
P0 →[Δ1/result1] P1 →[Δ2/result2] P2 → … → Pn; research object H(P)={(Pi,Δi,resulti)}.

TENSION:
Prompt-sharing interfaces privilege the current prompt, while the participant’s account suggests the pedagogically valuable object is the lineage.

MISSING:
Whether participants preserve complete histories or reconstruct them retrospectively from memory and platform traces.

BOUNDARY:
The passage describes collaborative practice but does not claim version history is necessary for all prompting.

CITATION TRAIL:
[[SCGAI-2024]] → P7 on prompts modifying over time → version histories/provenance systems → test whether commits/forks/diffs/merges fit prompt evolution.

TEST:
Record every prompt revision and output in a collaborative session; compare learning from final-only versus full revision history.

PLATFORM:
MidJourney / Discord

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
