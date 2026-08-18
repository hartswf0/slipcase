ZETTEL

ID:
SON-PROMPTSEMANTICS-007-B-C

TITLE:
CUT OFF ONE HEAD AND ANOTHER HEAD ANSWERS: causal intervention can cause the model to change the computation you were trying to measure.

SOURCE:
Thomas McGrath, Matthew Rahtz, Janos Kramar, Vladimir Mikulik & Shane Legg — “The Hydra Effect: Emergent Self-repair in Language Model Computations” — 2023.
SOURCE URL: https://arxiv.org/abs/2307.15771

PASSAGE:
[PARAPHRASE]
The authors report that ablating one attention layer can cause another layer to compensate, which they call the Hydra effect.

RESEARCH OBJECT:
INTERVENTION-INDUCED RECOMPUTATION.

[[SON-PROMPTSEMANTICS-007-B]] asked where a concept resides.

[[SON-PROMPTSEMANTICS-007-B-A]] made location distributed.

[[SON-PROMPTSEMANTICS-007-B-B]] made the decomposition non-canonical.

The Hydra effect introduces a still stranger obstacle:

THE ANSWER TO “WHAT DOES THIS COMPONENT DO?” MAY CHANGE WHEN YOU REMOVE THE COMPONENT.

LOCAL MOVE:
Causal analysis often assumes:

REMOVE COMPONENT X
→ observe lost behavior
→ infer contribution of X.

But if downstream components respond to the intervention:

REMOVE X
→ Y changes behavior
→ behavior partially recovers.

The intervention reveals not just the original computation but the system’s response to damage.

SOURCE TERMS:
Hydra effect
self-repair
ablation
attention layer
compensation
adaptive computation
factual recall
causal analysis

WHAT BECAME STRANGE:
A component can be important while its removal has a small behavioral effect.

Not because it did nothing.

Because the rest of the network did something different after it disappeared.

Causal redundancy is therefore not necessarily static redundancy.

It can be adaptive.

The model you measure after ablation is computationally different from the model that existed before ablation.

QUESTION:
How can we infer the normal causal role of a component when intervening on that component changes the behavior of other components?

DEEPER QUESTION:
Is the fundamental computational object a fixed circuit, or a field of conditional pathways whose causal organization depends on which pathways remain available?

MECHANISM:
The authors ablate model components and inspect downstream effects.

They identify cases where removing one attention layer produces compensatory changes elsewhere.

The downstream computation partially restores effects lost through ablation.

The source reports these behaviors even in models trained without dropout.

FORMAL SHIFT:
FROM:

NORMAL:

A
→ B
→ OUTPUT

ABLATE A:

0
→ B
→ ΔOUTPUT

infer ROLE(A) from ΔOUTPUT

TO:

NORMAL:

A
→ B
→ OUTPUT

ABLATE A:

0
→ B'
→ OUTPUT'

where:

B' ≠ B

because the remaining network responds to A’s absence.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let normal computation be:

Y = F(A, B)

After intervention do(A=0):

B may become:

B' = G(B | A=0)

Therefore observed effect:

Y - F(0, B')

does not directly equal:

the original contribution of A.

INTERVENTION EFFECT
=
LOSS OF A
+
COMPENSATION RESPONSE.

TENSION:
“Self-repair” can sound stronger than the evidence.

The cited study reports compensatory computation, not conscious detection of injury or general fault tolerance.

Later work also finds self-repair can be incomplete, noisy, and prompt-dependent.

The strange point survives without anthropomorphism:

causal organization can be intervention-sensitive.

MISSING:
Whether similar compensation appears in multimodal and diffusion models.

Whether steering one semantic direction causes competing features to strengthen.

Whether prompt manipulations can trigger analogous compensatory pathways.

Methods for estimating counterfactual:

WHAT WOULD THIS COMPONENT HAVE CONTRIBUTED

without allowing downstream computation to reorganize around its absence.

BOUNDARY:
The paper studies language-model computations and specific ablation procedures.

The Hydra metaphor is the authors’ name for the observed compensation phenomenon, not a claim of biological regeneration.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007-B]]
→ concept location
→ [[SON-PROMPTSEMANTICS-007-B-A]]
→ distributed superposition
→ [[SON-PROMPTSEMANTICS-007-B-B]]
→ non-canonical decomposition
→ Hydra effect
→ removing a component changes downstream computation
→ causal explanation itself becomes intervention-dependent

TEST:
For a candidate circuit component A:

1. record normal downstream activations B
2. ablate A
3. record changed downstream activations B'
4. separately patch B back toward its normal state while A remains ablated

Compare:

NORMAL
ABLATE-A
ABLATE-A + FREEZE-DOWNSTREAM
ABLATE-A + PATCH-NORMAL-DOWNSTREAM

If behavioral loss becomes substantially larger when compensation is prevented, naive ablation underestimates A’s original contribution.

Repeat across prompts to test whether the compensating pathway itself is context-dependent.

PLATFORM:
arXiv

LINKS:
[[SON-PROMPTSEMANTICS-007-B]]
[[SON-PROMPTSEMANTICS-007-B-A]]
[[SON-PROMPTSEMANTICS-007-B-B]]

BIBTEX:
@misc{mcgrath2023hydra,
  author = {Thomas McGrath and Matthew Rahtz and Janos Kramar and Vladimir Mikulik and Shane Legg},
  title = {The Hydra Effect: Emergent Self-repair in Language Model Computations},
  year = {2023},
  eprint = {2307.15771},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2307.15771}
}
