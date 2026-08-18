ZETTEL

ID:
CALLSHOT-20260817-09

TITLE:
DRAW THE SHOT INSTEAD OF DESCRIBING IT — ControlNet lets pose, edges, depth, or segmentation become a parallel prompt language.

SOURCE:
Lvmin Zhang, Anyi Rao, Maneesh Agrawala — “Adding Conditional Control to Text-to-Image Diffusion Models” — 2023.
https://arxiv.org/abs/2302.05543

PASSAGE:
[PARAPHRASE]
ControlNet adds spatial conditioning controls to pretrained text-to-image diffusion models. The paper demonstrates conditions including edges, depth maps, segmentation maps, and human pose, used singly or together and with or without text prompts.

RESEARCH OBJECT:
NONLINGUISTIC-PROMPT-AS-SPATIAL-CONSTRAINT.

LOCAL MOVE:
[[MJ-GC-026]] defined the transition from game to tool partly through increased control.

This source shows one way the industry/research community solved a fundamental prompt problem:

STOP TRYING TO SAY GEOMETRY.

GIVE THE GEOMETRY.

SOURCE TERMS:
“spatial conditioning controls”
“edges”
“depth”
“segmentation”
“human pose”
“single or multiple conditions”
“with or without prompts”

WHAT BECAME STRANGE:
Natural language may be the wrong control channel for some intentions.

“Put the arm exactly here” is difficult prose.

A pose skeleton can state it immediately.

Prompt practice therefore expands from writing instructions into choosing the representation best matched to the constraint.

QUESTION:
Which intentions are better expressed as words, examples, masks, pose graphs, depth fields, schemas, or coordinates?

DEEPER QUESTION:
Is “prompting” becoming a general practice of assembling heterogeneous constraints rather than writing natural-language descriptions?

MECHANISM:
TEXT CONDITION
+
SPATIAL CONDITION {
EDGE |
DEPTH |
POSE |
SEGMENTATION
}
→ controlled diffusion generation.

FORMAL SHIFT:
FROM:
DESCRIBE EVERYTHING IN WORDS.

TO:
SEMANTICS → WORDS
GEOMETRY → SPATIAL SIGNAL
IDENTITY → REFERENCE
FORMAT → SCHEMA
ACTION → TOOL.

SOURCE FORMALISM:
ControlNet conditions a pretrained diffusion backbone using additional learned control networks, demonstrated with spatial signals such as edge, depth, segmentation, and pose maps.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CALL_SHOT =
bundle {
LANGUAGE,
GEOMETRY,
REFERENCE,
CONSTRAINTS
}.

Choose representation R_i according to the property being controlled.

TENSION:
Adding explicit spatial control can reduce generative freedom and surprise.

Greater toolhood may require deliberately surrendering some of the productive deviation celebrated in [[MJ-GC-029]].

MISSING:
A practical grammar telling creators which modality should encode which class of intention.

BOUNDARY:
ControlNet demonstrates these mechanisms for compatible diffusion architectures; it is not a universal mechanism for all image models.

CITATION TRAIL:
[[MJ-GC-026]]
→ control marks toolhood
→ ControlNet
→ spatial conditions supplement language
→ “prompt” expands into heterogeneous control bundle.

TEST:
Take one target image.

Attempt control using:

TEXT ONLY
TEXT + POSE
TEXT + EDGE
TEXT + DEPTH
TEXT + MULTIPLE CONDITIONS.

For each desired property, record which representation provides the cleanest intervention.

PLATFORM:
Stable Diffusion / ControlNet

LINKS:
[[MJ-GC-026]]
[[MJ-GC-023-A]]
[[CALLSHOT-20260817-08]]

BIBTEX:
@article{zhang2023controlnet,
  title={Adding Conditional Control to Text-to-Image Diffusion Models},
  author={Zhang, Lvmin and Rao, Anyi and Agrawala, Maneesh},
  journal={arXiv preprint arXiv:2302.05543},
  year={2023},
  url={https://arxiv.org/abs/2302.05543}
}
