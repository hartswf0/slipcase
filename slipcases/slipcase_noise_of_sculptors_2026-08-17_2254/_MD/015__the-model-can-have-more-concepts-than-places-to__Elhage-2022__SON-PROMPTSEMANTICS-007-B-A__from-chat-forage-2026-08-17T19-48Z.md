ZETTEL

ID:
SON-PROMPTSEMANTICS-007-B-A

TITLE:
THE MODEL CAN HAVE MORE CONCEPTS THAN PLACES TO PUT THEM.

SOURCE:
Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg & Christopher Olah — “Toy Models of Superposition” — 2022.
SOURCE URL: https://arxiv.org/abs/2209.10652

PASSAGE:
[PARAPHRASE]
The authors construct toy networks in which polysemanticity arises because sparse features are represented in superposition: multiple features share representational dimensions.

RESEARCH OBJECT:
SUPERPOSITION.

[[SON-PROMPTSEMANTICS-007-B]] asked how a model can possess an operational concept without possessing a corresponding concept neuron.

Superposition supplies a much stranger possibility:

THERE MAY BE MORE FEATURES THAN DIMENSIONS AVAILABLE TO REPRESENT THEM.

LOCAL MOVE:
The earlier zettel weakened:

CONCEPT
=
NEURON.

Superposition weakens the replacement:

CONCEPT
=
SOME OTHER UNIQUE LOCATION.

When features are sufficiently sparse, a model can represent many feature directions in fewer dimensions by allowing them to interfere.

The storage space itself becomes shared.

SOURCE TERMS:
superposition
features
dimensions
sparsity
polysemanticity
interference
geometry
uniform polytopes

WHAT BECAME STRANGE:
A neuron responding to:

legal language
DNA
Hebrew
and another unrelated pattern

need not mean the neuron itself possesses one bizarre composite concept.

The neuron may be a projection surface through which several independently useful features pass.

The model therefore need not contain one box per concept.

It can overlap concepts geometrically.

Meaning can be multiplexed.

QUESTION:
If multiple concepts occupy overlapping representational dimensions, what exactly is a prompt activating when it appears to invoke one concept?

DEEPER QUESTION:
Can model semantics be understood as interference patterns in which concepts exist not as stored objects but as recoverable directions through shared representational matter?

MECHANISM:
A network has a hidden representation with fewer dimensions than the number of useful sparse features.

Rather than discard features, it can encode feature directions non-orthogonally.

When few features are active simultaneously, interference remains tolerable.

Individual neurons then participate in several features.

Polysemanticity emerges from representational compression.

FORMAL SHIFT:
FROM:

FEATURE_i
→ NEURON_i

TO:

FEATURE_1 ↘
FEATURE_2 → SHARED DIMENSIONS
FEATURE_3 ↗

Each feature is represented as a direction through a common space rather than monopolizing one coordinate.

SOURCE FORMALISM:
[PARAPHRASE]

The toy models study sparse input features using small ReLU networks and show regimes where additional features are stored in superposition, producing polysemantic neurons and structured geometric arrangements.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Suppose:

m = representational dimensions
n = useful features

with:

n > m

Localist representation would require:

FEATURE_i ↔ coordinate_i

and therefore fail for n > m.

Superposition instead permits:

FEATURE_i ↔ direction v_i ∈ R^m

where many v_i share the same coordinates.

Activation state:

h = Σ a_i v_i

Meaning must then be inferred from a combination of directions rather than read directly from individual coordinate values.

TENSION:
Superposition provides a mechanism for more features than dimensions in toy models.

It does not establish that every polysemantic neuron in a production model is explained by this mechanism.

Nor does “feature direction” automatically equal a human semantic concept.

The source makes the concept-location problem harder, not solved.

MISSING:
Causal evidence connecting specific prompt-sensitive concepts to superposed features in multimodal generative systems.

Measures of interference between prompt concepts.

Whether apparently strange prompt interactions occur because two desired concepts share representational dimensions.

Whether prompt specificity works partly by disambiguating overlapping feature directions.

BOUNDARY:
The paper deliberately studies toy models.

Its value here is mechanistic possibility, not proof that Midjourney or CLIP implements identical geometry.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007-B]]
→ no identifiable San Francisco neuron
→ Toy Models of Superposition
→ features need not map one-to-one onto neurons
→ several features can share dimensions
→ concept location becomes geometric multiplexing rather than storage

TEST:
Identify pairs of concepts whose prompt effects interfere unexpectedly.

For each pair:

measure internal representation directions
estimate cosine similarity
activate separately
activate jointly
intervene on suspected shared dimensions

Compare:

independent-feature prediction
versus
superposition/interference prediction.

The strongest evidence would be:

A and B individually controllable
+
A+B produces systematic interference
+
the interference is causally altered by manipulating their shared representational subspace.

PLATFORM:
arXiv / Transformer Circuits

LINKS:
[[SON-PROMPTSEMANTICS-007-B]]

BIBTEX:
@misc{elhage2022toy,
  author = {Nelson Elhage and Tristan Hume and Catherine Olsson and Nicholas Schiefer and Tom Henighan and Shauna Kravec and Zac Hatfield-Dodds and Robert Lasenby and Dawn Drain and Carol Chen and Roger Grosse and Sam McCandlish and Jared Kaplan and Dario Amodei and Martin Wattenberg and Christopher Olah},
  title = {Toy Models of Superposition},
  year = {2022},
  eprint = {2209.10652},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2209.10652}
}
