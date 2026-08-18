ZETTEL

ID:
MJ-GC-022-A-A

TITLE:
Semantic siblings interfere with one another: composition gets worse when cohyponyms enter the same image.

SOURCE:
Raphael Tang, Linqing Liu, Akshat Pandey, Zhiying Jiang, Gefei Yang, Karun Kumar, Pontus Stenetorp, Jimmy Lin, Ferhan Ture — “What the DAAM: Interpreting Stable Diffusion Using Cross Attention” — ACL 2023 — pp. 5644–5659.
URL: https://aclanthology.org/2023.acl-long.310/

PASSAGE:
[PARAPHRASE]
Tang et al. investigate feature entanglement and report that the presence of cohyponyms reduces generation quality by 9%. They separately find that descriptive adjectives attend too broadly.

RESEARCH OBJECT:
SEMANTIC-SIBLING-INTERFERENCE.

LOCAL MOVE:
[[MJ-GC-022-A]] split “semantic gravity” from compositional binding failure.

This source exposes a sharper variable:

WHAT ELSE IS IN THE SAME SEMANTIC NEIGHBORHOOD?

Failures are not only produced by one overwhelmingly famous attractor.

Related categories can interfere with one another during composition.

SOURCE TERMS:
“cohyponyms”
“feature entanglement”
“generation quality”
“descriptive adjectives”
“attend too broadly”

WHAT BECAME STRANGE:
Adding a second concept does not simply add information.

The identity of the second concept can damage the first.

[OUR INFERENCE]
Semantic proximity may sometimes be an enemy of compositional separability.

The model may know both concepts while failing to keep their features apart.

QUESTION:
Why should two concepts occupying related semantic categories be harder to keep compositionally distinct?

DEEPER QUESTION:
Does generative representation become least reliable precisely where human categorization says two things belong together?

MECHANISM:
PROMPT:
ENTITY_A
+ ENTITY_B
+ ATTRIBUTES.

When A and B are cohyponyms:

representation / attention
→ feature entanglement
→ degraded generation fidelity.

Separately:

ADJECTIVE
→ attribution region spreads too broadly
→ property can fail to remain localized to intended entity.

FORMAL SHIFT:
FROM:
DOMINANT CONCEPT
overwhelms
WEAK CONCEPT

TO:
RELATED CONCEPT_A
↔ INTERFERENCE ↔
RELATED CONCEPT_B.

The failure may be horizontal between siblings rather than vertical domination by one attractor.

SOURCE FORMALISM:
[PARAPHRASE]
DAAM uses aggregated cross-attention to investigate semantic phenomena.

The reported experiments identify:
cohyponym-related degradation,
and overly broad attribution for descriptive adjectives.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

A, B ∈ same semantic category.

Expected composition:

FEATURES(A) remain bound to A
FEATURES(B) remain bound to B.

Observed failure hypothesis:

SIMILARITY(A,B) ↑
→ separability(A,B) ↓
→ ATTRIBUTE_LEAKAGE / ENTANGLEMENT ↑.

This final causal relation is a hypothesis for testing, not a claim made by the source.

TENSION:
The paper reports a cohyponym effect, but “semantic similarity causes interference” is stronger than the evidence directly establishes.

Other properties of the tested prompts or representations may account for the degradation.

MISSING:
A controlled gradient from:
unrelated noun pairs
→ moderately related nouns
→ close cohyponyms
while holding visual complexity constant.

BOUNDARY:
The reported 9% degradation is specific to the paper's experiments and should not be generalized to all text-to-image models.

CITATION TRAIL:
[[MJ-GC-022-A]]
→ binding failure versus semantic gravity
→ Tang et al. 2023
→ cohyponyms measurably worsen generation
→ binding difficulty may depend on relations among concepts, not simply strength of individual concepts.

TEST:
Create matched two-object prompts:

DOG + TEAPOT
DOG + CAR
DOG + CAT
DOG + WOLF.

Attach distinct attributes to each object.

Measure:
object omission,
attribute leakage,
identity blending,
DAAM-map overlap,
and relation fidelity.

Test whether compositional failure increases with semantic relatedness rather than merely prompt length or visual complexity.

PLATFORM:
Stable Diffusion / DAAM

LINKS:
[[MJ-GC-022-A]]
[[MJ-GC-023-A]]
[[MJ-GC-023-A-A]]

BIBTEX:
@inproceedings{tang2023daam,
  title={What the DAAM: Interpreting Stable Diffusion Using Cross Attention},
  author={Tang, Raphael and Liu, Linqing and Pandey, Akshat and Jiang, Zhiying and Yang, Gefei and Kumar, Karun and Stenetorp, Pontus and Lin, Jimmy and Ture, Ferhan},
  booktitle={Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
  pages={5644--5659},
  year={2023},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2023.acl-long.310},
  url={https://aclanthology.org/2023.acl-long.310/}
}
