ZETTEL

ID:
SCGAI-002

TITLE:
Prompt ownership can turn into collaboration after the copied prompt produces a difference.

SOURCE:
Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko — “The Social Construction of Generative AI Prompts” — CHI EA ’24 — 2024 — https://doi.org/10.1145/3613905.3650947

PASSAGE:
[QUOTE] “it almost becomes a collaboration because I’m learning from this person and it’s not adversarial.” — P8

RESEARCH OBJECT:
A participant describes a reversal in the meaning of copying: another person takes their prompt, changes it slightly, and obtains a better result. The act initially interpreted as appropriation becomes evidence that teaches the original author something.

LOCAL MOVE:
Treat reuse not simply as COPY but as an experiment performed on another person’s contribution.

SOURCE TERMS:
copy; add one word; better image; collaboration; learning; adversarial; credit

WHAT BECAME STRANGE:
A copied prompt can return information to its supposed owner. Appropriation becomes an epistemic loop when the derivative version reveals something about the prompt-model relation.

QUESTION:
Under what conditions does prompt copying become reciprocal experimentation rather than extraction?

DEEPER QUESTION:
Can another person experimentally probe your linguistic artifact and return discoveries without ever coordinating with you?

MECHANISM:
PROMPT_A → copied by B → small modification → OUTPUT_B differs → A observes difference → A learns → interpretation shifts from theft toward collaboration.

FORMAL SHIFT:
COPYING AS TRANSFER becomes COPYING AS DISTRIBUTED EXPERIMENTATION.

SOURCE FORMALISM:
The source locates Proprietary/Solitary and Collaborative prompting at different positions within Prompt Sharing × Prompt Reuse and states orientations are temporary/context-dependent rather than permanent types.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
A: p → M → y1
B: mutate(p, Δ) → M → y2
A observes (Δ, y2-y1) → KNOWLEDGE_A increases

TENSION:
The same operation—copying and modifying—can be interpreted as theft, derivation, experimentation, or collaboration; technical transformation alone does not determine social meaning.

MISSING:
Variables causing the interpretive transition: attribution, modification magnitude, reciprocity, public visibility, prior relationship, usefulness of returned result.

BOUNDARY:
One participant’s retrospective reinterpretation demonstrates a possible transition, not a general law.

CITATION TRAIL:
[[SCGAI-2024]] → P8’s change from “copy” to “collaboration” → distributed creativity → ask whether collaboration requires intentional coordination.

TEST:
Vary attribution, permission, modification size, reciprocity, and visibility while holding the copied prompt constant; ask where cases change category.

PLATFORM:
MidJourney

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
