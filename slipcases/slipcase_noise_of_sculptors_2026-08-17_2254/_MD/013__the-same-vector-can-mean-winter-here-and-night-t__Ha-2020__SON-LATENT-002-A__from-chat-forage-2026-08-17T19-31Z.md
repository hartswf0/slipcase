ZETTEL

ID:
SON-LATENT-002-A

TITLE:
THE SAME VECTOR CAN MEAN WINTER HERE AND NIGHT THERE.

SOURCE:
Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen & Sylvain Paris — “GANSpace: Discovering Interpretable GAN Controls” — NeurIPS 2020.
SOURCE URL: https://arxiv.org/abs/2004.02546
FULL TEXT: https://arxiv.org/html/2004.02546

PASSAGE:
[QUOTE]
“A direction that makes the image more blue might mean winter for some classes, but just nighttime for others.”

RESEARCH OBJECT:
LATENT DIRECTIONS HAVE CONTEXTUAL SEMANTICS.

A numerical transformation can remain stable while its apparent meaning changes.

LOCAL MOVE:
[[SON-LATENT-002]] separated the Midjourney community’s folk “latent-space landscape” from the narrower technical latent representation in Latent Diffusion Models.

GANSpace now complicates that correction.

In some generative architectures, latent directions really can correspond to interpretable transformations.

Yet even there the direction does not possess a context-free semantic label.

The same transformation can become WINTER in one image domain and NIGHT in another.

SOURCE TERMS:
latent directions
principal components
PCA
latent space
feature space
interpretable controls
class-independent
entanglement
StyleGAN
BigGAN

WHAT BECAME STRANGE:
There can be a real vector.

There can be a repeatable operation.

There can be a visible semantic effect.

And still there may be no single correct word for what the vector MEANS.

Meaning appears only when the transformation encounters a particular generated world.

“More blue” is not yet:

WINTER
NIGHT
COLD
SHADE

until the rest of the representation constrains its interpretation.

QUESTION:
Does a latent direction contain a semantic meaning, or does meaning emerge only from the interaction between direction and current generative state?

DEEPER QUESTION:
Could operational semantics in generative systems be fundamentally contextual in the strong sense that the same executable transformation means different things in different worlds?

MECHANISM:
GANSpace samples latent or feature representations and applies PCA to identify major directions of variation.

For StyleGAN, the paper defines edits by adding combinations of principal directions to the intermediate latent representation.

These directions can produce recognizable transformations.

However, interpretation depends on the model, layer, class, and surrounding representation.

FORMAL SHIFT:
FROM:

VECTOR d
=
SEMANTIC ATTRIBUTE “BLUE” / “WINTER” / “NIGHT”

TO:

MEANING
=
INTERPRET(
  transformation d,
  base state z,
  class c,
  model M,
  layer range L
)

The operation can remain constant while its semantic description changes.

SOURCE FORMALISM:
[QUOTE — SOURCE SYNTAX]

For StyleGAN, GANSpace gives the edit:

w′ = w + Vx

where V contains principal directions and x specifies user-controlled offsets.

The paper also gives the analogous BigGAN latent edit:

z′ = z + Ux

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let d_blue be a repeatable latent transformation.

Then:

APPLY(d_blue, snowy-landscape)
→ “more winter”

APPLY(d_blue, urban-night-scene)
→ “more nighttime”

Therefore:

SEMANTICS(d)

is incomplete.

A stronger object is:

SEMANTICS(d | WORLD_STATE)

Operational meaning is relational.

TENSION:
Calling these directions “semantic” can conceal two different claims:

1. the transformation produces a human-interpretable regularity
2. the transformation internally represents a stable semantic concept

GANSpace directly supports the first.

It does not automatically prove the second.

A direction may encode correlated visual variation rather than a concept in any stronger symbolic sense.

MISSING:
Whether equivalent contextual directions exist in diffusion-model latent or activation spaces.

Whether prompt embeddings interact with those directions compositionally.

Whether the same prompt phrase generates systematically different operational transformations depending on image state in ways analogous to GANSpace’s class-dependent direction meanings.

A distinction between:

INTERPRETABLE DIRECTION
SEMANTIC DIRECTION
CAUSAL FEATURE
CORRELATED DATASET AXIS

BOUNDARY:
GANSpace analyzes pretrained GANs including StyleGAN and BigGAN.

Its latent machinery must not be imported directly into Midjourney or Latent Diffusion Models.

The source shows that the folk metaphor of “moving through latent space” can be technically literal in some architectures while remaining architecture-specific.

CITATION TRAIL:
[[SON-LATENT-002]]
→ technical latent representation versus user landscape metaphor
→ GANSpace
→ PCA discovers controllable latent directions
→ identical direction can receive different semantic interpretations by class
→ latent “meaning” becomes relation between OPERATION and WORLD

TEST:
Take one discovered latent direction d across multiple classes or base states.

For every application collect:

numerical transformation
generated before/after pair
human semantic labels
model-generated labels
feature changes

Then test:

INVARIANT OPERATION?
INVARIANT VISUAL PROPERTY?
INVARIANT HUMAN MEANING?

If operation remains stable while human meaning changes, semantic labels belong to the transformation-in-context rather than the vector alone.

Repeat the experiment with text-conditioning directions in a diffusion model.

PLATFORM:
arXiv / NeurIPS

LINKS:
[[SON-LATENT-002]]
[[SON-PROMPTSEMANTICS-007]]

BIBTEX:
@inproceedings{harkonen2020ganspace,
  author = {Erik H{\"a}rk{\"o}nen and Aaron Hertzmann and Jaakko Lehtinen and Sylvain Paris},
  title = {GANSpace: Discovering Interpretable GAN Controls},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {33},
  pages = {9841--9850},
  year = {2020},
  url = {https://arxiv.org/abs/2004.02546}
}
