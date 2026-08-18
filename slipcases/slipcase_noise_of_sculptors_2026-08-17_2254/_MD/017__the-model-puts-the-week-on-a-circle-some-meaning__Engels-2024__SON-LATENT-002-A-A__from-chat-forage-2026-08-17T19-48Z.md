ZETTEL

ID:
SON-LATENT-002-A-A

TITLE:
THE MODEL PUTS THE WEEK ON A CIRCLE: some meanings are not directions but shapes that computation moves around.

SOURCE:
Joshua Engels, Eric J. Michaud, Isaac Liao, Wes Gurnee & Max Tegmark — “Not All Language Model Features Are One-Dimensionally Linear” — ICLR 2025.
SOURCE URL: https://arxiv.org/abs/2405.14860

PASSAGE:
[PARAPHRASE]
The authors discover circular representations of weekdays and months in language models and provide intervention evidence that these circles participate in modular-arithmetic computations involving those concepts.

RESEARCH OBJECT:
SEMANTIC MANIFOLDS.

[[SON-LATENT-002-A]] showed that a latent direction can have context-dependent meaning.

This source creates a deeper rupture:

SOME CONCEPTS MAY NOT BE DIRECTIONS AT ALL.

They may require multidimensional geometry.

LOCAL MOVE:
A large amount of interpretability language assumes:

CONCEPT
=
LINEAR DIRECTION.

Increase the coordinate and you get “more” of the feature.

That works naturally for concepts admitting an axis:

more formal
more positive
more toxic.

But weekdays do not have endpoints.

Sunday wraps into Monday.

A line is topologically wrong.

A circle fits the operation.

SOURCE TERMS:
multi-dimensional features
circular features
days of the week
months
modular arithmetic
intervention
irreducible
activation space

WHAT BECAME STRANGE:
The geometry is not decorative.

According to the source, models use these circular representations in computations involving weekdays and months.

Thus:

REPRESENTATION SHAPE

can match:

CONCEPTUAL OPERATION.

The model does not merely know that Wednesday and Thursday are related.

It can place the week in a geometry where moving forward eventually returns to the beginning.

QUESTION:
Which concepts require shapes rather than directions for their computational representation?

DEEPER QUESTION:
Could part of what we call “meaning” inside a model be the topology of the transformations a concept permits?

MECHANISM:
A one-dimensional linear feature can be represented by a scalar coordinate along a direction.

A cyclic variable cannot preserve its adjacency structure on an ordinary line without a discontinuity.

A two-dimensional circular representation can encode:

Monday
Tuesday
...
Sunday

as angular positions.

An operation such as adding days can then correspond to movement around the circle.

FORMAL SHIFT:
FROM:

CONCEPT C
→ scalar activation a_C

TO:

CONCEPT C
→ position on manifold M_C

and:

OPERATION
→ transformation on M_C.

For cyclic concepts:

M_C ≈ S¹

rather than R.

SOURCE FORMALISM:
[PARAPHRASE]

The paper defines irreducible multidimensional features and uses sparse-autoencoder-based methods to identify circular representations.

It reports intervention evidence that the weekday/month circles function in modular-arithmetic tasks.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Represent weekday d as:

θ_d = 2πd / 7

state:

v_d = (cos θ_d, sin θ_d)

“three days later” becomes:

ROTATE(v_d, 6π/7)

rather than:

LOOKUP(d + 3).

Meaning therefore may reside partly in:

GEOMETRY
+
LEGAL TRANSFORMATIONS.

TENSION:
A discovered circle need not be the only representation involved in weekday reasoning.

Models may contain redundant or parallel mechanisms.

The evidence is strongest for the studied tasks and architectures.

Nor should every cyclical human concept be assumed to receive circular neural geometry.

MISSING:
Comparable geometries for:

color hue
musical pitch classes
seasons
narrative cycles
social hierarchies
spatial orientation
grammatical tense
kinship
political spectra

Evidence that prompt effects can be predicted from manifold topology.

Whether generative image models encode stylistic or visual variables as circles, tori, trees, or other nonlinear manifolds.

BOUNDARY:
This source studies language-model representations, not image-generator latent spaces.

The child changes the conceptual possibilities for “latent geometry” without claiming identical implementation in Midjourney.

CITATION TRAIL:
[[SON-LATENT-002-A]]
→ latent directions have contextual semantics
→ assumption that concepts are vectors
→ Engels et al.
→ weekdays and months form circular multidimensional features
→ model computation operates over conceptual geometry
→ meaning may be TOPOLOGY + TRANSFORMATION

TEST:
Choose concept families with known relational structure:

LINE:
small → large

CIRCLE:
January → ... → December → January

TREE:
animal → mammal → dog

GRID:
north/south × east/west

For each, probe model activations and compare candidate geometries.

Then intervene in the recovered geometry.

Ask whether operations appropriate to the human concept correspond to transformations preserving that geometry.

The strongest result would be:

different conceptual structures
→ different internal topologies
→ topology-specific causal computation.

PLATFORM:
arXiv / ICLR 2025

LINKS:
[[SON-LATENT-002-A]]
[[SON-PROMPTSEMANTICS-007-B]]

BIBTEX:
@misc{engels2024notall,
  author = {Joshua Engels and Eric J. Michaud and Isaac Liao and Wes Gurnee and Max Tegmark},
  title = {Not All Language Model Features Are One-Dimensionally Linear},
  year = {2024},
  eprint = {2405.14860},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2405.14860},
  note = {Accepted to ICLR 2025}
}
