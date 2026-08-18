ZETTEL

ID:
MJ-GC-022-A

TITLE:
A “semantic black hole” may actually be a binding failure: composition breaks because the system cannot reliably keep entities, attributes, and relations attached to one another.

SOURCE:
Weixi Feng, Xuehai He, Tsu-Jui Fu, Varun Jampani, Arjun Akula, Pradyumna Narayana, Sugato Basu, Xin Eric Wang, William Yang Wang — “Training-Free Structured Diffusion Guidance for Compositional Text-to-Image Synthesis” — arXiv:2212.05032 — 2022/2023.
URL: https://arxiv.org/abs/2212.05032

PASSAGE:
[PARAPHRASE]
Feng et al. identify attribution binding and composition involving multiple objects as persistent problems in text-to-image diffusion models. They improve results by introducing linguistic structure into diffusion guidance and manipulating cross-attention representations associated with object layout and content.

RESEARCH OBJECT:
ATTRACTOR-DOMINANCE-VERSUS-COMPOSITIONAL-BINDING-FAILURE.

LOCAL MOVE:
[[MJ-GC-022]] interpreted “Mona Lisa” swallowing neighboring concepts as unusually deep semantic gravity.

Feng et al. expose a competing explanation.

A model may successfully represent:
A,
B,
red,
blue,
left,
right

while nevertheless failing to preserve:

red(A)
blue(B)
left_of(A,B).

What looks phenomenologically like one concept “pulling” everything toward itself may sometimes be a failure to bind multiple requested components into the correct structure.

SOURCE TERMS:
“attribution-binding”
“compositional”
“multiple objects”
“linguistic structures”
“cross-attention”
“object layouts”
“content”

WHAT BECAME STRANGE:
Knowing every requested concept is not enough.

A generator can possess A and B while failing at A-WITH-B.

The hard problem may therefore sit not in the semantic nodes themselves but in the RELATIONS that must survive generation.

QUESTION:
When “Mona Lisa” overwhelms another concept, has the weaker concept disappeared, or has the model failed to bind it to the right entity, attribute, or region?

DEEPER QUESTION:
Are the strangest prompt failures better understood as failures of semantic representation or failures of compositional grammar?

MECHANISM:
PROMPT:
ENTITY_A + ATTRIBUTE_A
ENTITY_B + ATTRIBUTE_B
RELATION(A,B)

MODEL may represent all individual tokens

BUT

ATTENTION / GENERATION
→ ATTRIBUTE_A attached to B
→ ATTRIBUTE_B omitted
→ relation reversed
→ entity omitted
→ composition collapses.

FORMAL SHIFT:
FROM:
STRONG CONCEPT
→ gravitational domination
→ weak concept erased

TO competing hypotheses:

H1 — ATTRACTOR DOMINANCE
Concept A overwhelms B.

H2 — BINDING FAILURE
A and B survive internally or partially, but their requested relations are not maintained.

H3 — BOTH
Strong priors distort already-fragile compositional binding.

SOURCE FORMALISM:
[PARAPHRASE]
The paper manipulates cross-attention using linguistic structure in order to improve attribute binding and image composition.

Its reported mechanism assigns semantic importance to cross-attention keys and values associated with layout and content, then restructures guidance to better preserve compositional semantics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Representation success:

R = {A, B, x, y}

does not entail compositional success:

C = {
x(A),
y(B),
REL(A,B)
}.

Therefore:

CONCEPT_PRESENT(B) = true

can coexist with:

BINDING_CORRECT(B) = false.

“Black hole” behavior must distinguish:

ERASURE
from
MISBINDING
from
RELATIONAL COLLAPSE.

TENSION:
The interviewee's gravity metaphor elegantly predicts phenomenology:
some concepts feel disproportionately difficult to combine.

The compositionality literature warns that this phenomenology does not uniquely identify a mechanism.

MISSING:
A diagnostic decomposition of the Mona Lisa example showing whether failures consist of:
concept omission,
style leakage,
identity substitution,
attribute leakage,
layout displacement,
or relation failure.

BOUNDARY:
Feng et al. study Stable Diffusion-based machinery, not Midjourney.

Their results cannot establish the cause of Midjourney's Mona Lisa behavior.

CITATION TRAIL:
[[MJ-GC-022]]
→ Mona Lisa “black hole”
→ [[MJ-GC-020]] semantic composition
→ Feng et al.
→ compositional generation fails specifically at attribution and binding
→ “semantic gravity” splits into representation strength versus relational binding.

TEST:
Construct prompts combining one allegedly dominant recognizable concept D with a second concept B.

Score outputs separately for:
D present?
B present?
attributes correct?
spatial relation correct?
style leakage?
identity substitution?

If B remains visible but its properties migrate to D, the failure supports BINDING COLLAPSE more than simple semantic erasure.

PLATFORM:
Stable Diffusion / compositional text-to-image generation

LINKS:
[[MJ-GC-022]]
[[MJ-GC-020]]
[[MJ-GC-019]]
[[MJ-GC-021]]

BIBTEX:
@article{feng2022structured,
  title={Training-Free Structured Diffusion Guidance for Compositional Text-to-Image Synthesis},
  author={Feng, Weixi and He, Xuehai and Fu, Tsu-Jui and Jampani, Varun and Akula, Arjun and Narayana, Pradyumna and Basu, Sugato and Wang, Xin Eric and Wang, William Yang},
  journal={arXiv preprint arXiv:2212.05032},
  year={2022},
  url={https://arxiv.org/abs/2212.05032}
}
