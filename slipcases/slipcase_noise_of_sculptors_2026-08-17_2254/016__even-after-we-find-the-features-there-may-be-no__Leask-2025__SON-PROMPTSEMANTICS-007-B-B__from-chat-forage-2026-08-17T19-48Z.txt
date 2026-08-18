ZETTEL

ID:
SON-PROMPTSEMANTICS-007-B-B

TITLE:
EVEN AFTER WE FIND THE “FEATURES,” THERE MAY BE NO ONE TRUE SET OF FEATURES.

SOURCE:
Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey & Neel Nanda — “Sparse Autoencoders Do Not Find Canonical Units of Analysis” — ICLR 2025.
SOURCE URL: https://arxiv.org/abs/2502.04878

PASSAGE:
[PARAPHRASE]
The authors find that sparse autoencoders of different dictionary sizes produce different granularities and compositions rather than converging on one unique, complete, irreducible set of features.

[QUOTE]
They conclude that “no single SAE configuration provides a universal solution.”

RESEARCH OBJECT:
NON-CANONICAL INTERPRETATION.

[[SON-PROMPTSEMANTICS-007-B-A]] destroyed the idea that one neuron must equal one concept.

Sparse autoencoders appeared to promise recovery of the hidden “real” features underneath those mixed neurons.

This paper destabilizes even that rescue.

LOCAL MOVE:
The interpretability pipeline seemed to be:

POLYSEMANTIC NEURONS
→ decompose them
→ discover TRUE FEATURES.

But the decomposition itself depends on scale.

A broad feature in one dictionary can split into several narrower features in another.

More strangely, a feature in a larger dictionary can sometimes compose information associated with several smaller features.

The decomposition does not simply reveal finer and finer atoms.

SOURCE TERMS:
canonical units
sparse autoencoders
dictionary size
feature splitting
meta-SAE
atomic
complete
unique
latent
stitching

WHAT BECAME STRANGE:
“Einstein” can be recovered as one feature.

But the source reports that it can also be decomposed into features corresponding to ideas such as:

scientist
Germany
famous person.

Which one is real?

EINSTEIN?

Or the conjunction:

SCIENTIST
+
GERMANY
+
FAMOUS PERSON?

Or both at different useful scales?

Interpretability begins to resemble choosing a vocabulary rather than uncovering the vocabulary.

QUESTION:
If equally functional decompositions carve model activity at different semantic granularities, what warrants calling any extracted feature a genuine unit of model meaning?

DEEPER QUESTION:
Could model semantics lack a privileged ontology altogether—so that “concepts” emerge partly from the resolution at which an interpreter chooses to describe computation?

MECHANISM:
Sparse autoencoders reconstruct model activations using a larger sparse dictionary.

Changing dictionary size changes the available latent basis.

The authors compare dictionaries using SAE stitching and meta-SAEs.

They find:

NOVEL LATENTS:
larger dictionaries capture information absent from smaller ones.

RECONSTRUCTION LATENTS:
larger latents may refine smaller features.

COMPOSED LATENTS:
larger latents can sometimes combine structure associated with multiple smaller latents.

Thus scaling the dictionary does not reveal a simple fixed inventory.

FORMAL SHIFT:
FROM:

MODEL
→ hidden TRUE FEATURE SET F*
→ interpretability discovers F*

TO:

MODEL ACTIVATION X
→ decomposition D_k(X)
→ feature vocabulary F_k

where changing k can change:

number
granularity
composition
interpretation

of the resulting features.

SOURCE FORMALISM:
[PARAPHRASE]

The source defines a canonical set as one that is:

unique
complete
atomic.

Its experiments using SAE stitching and meta-SAEs provide evidence against SAEs recovering such a set.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

X = same model activation.

Two valid decompositions:

D_1(X)
=
{A, B, C}

D_2(X)
=
{AB, C_1, C_2, D}

may both reconstruct X usefully.

Therefore:

INTERPRETABLE(X)

does not imply:

UNIQUE_ONTOLOGY(X).

A concept inventory can be:

TASK-RELATIVE
SCALE-RELATIVE
DECOMPOSITION-RELATIVE

without being arbitrary.

TENSION:
The paper does not prove that canonical units do not exist.

It shows that current SAE methods do not identify them and casts doubt on simple convergence stories.

There may still be a privileged decomposition inaccessible to these methods.

Alternatively, asking for one privileged decomposition may itself be the category error.

MISSING:
A criterion for deciding when two decompositions are merely alternative descriptions and when one better captures causal computation.

Evidence for or against irreducible features independent of dictionary architecture.

Tests of whether downstream control is more reliable at one semantic granularity than another.

A theory of interpretation that tolerates plural decompositions without collapsing into “anything goes.”

BOUNDARY:
The source studies SAEs applied to GPT-2 Small and Gemma 2 2B among its experiments.

Its conclusion concerns what these interpretability methods recover, not metaphysical proof that neural computation has no canonical structure.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007-B]]
→ concepts without concept neurons
→ [[SON-PROMPTSEMANTICS-007-B-A]]
→ superposed feature directions
→ sparse autoencoders attempt decomposition
→ Leask et al.
→ decomposition changes with dictionary size
→ even FEATURE may be an interpretive scale rather than a discovered atom

TEST:
Train multiple independently initialized sparse dictionaries at:

1×
2×
4×
8×
16×

the model activation dimension.

For a target concept C:

find all associated latents
perform causal steering
perform ablation
compare reconstruction
map splitting and composition across scales

Ask:

Does one feature persist as a stable causal object?

Or does C continually redistribute across valid decompositions?

The decisive evidence for non-canonicity would be multiple incompatible decompositions with comparable:

reconstruction
predictive power
and causal control.

PLATFORM:
arXiv / ICLR 2025

LINKS:
[[SON-PROMPTSEMANTICS-007-B]]
[[SON-PROMPTSEMANTICS-007-B-A]]

BIBTEX:
@misc{leask2025sparse,
  author = {Patrick Leask and Bart Bussmann and Michael Pearce and Joseph Bloom and Curt Tigges and Noura Al Moubayed and Lee Sharkey and Neel Nanda},
  title = {Sparse Autoencoders Do Not Find Canonical Units of Analysis},
  year = {2025},
  eprint = {2502.04878},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2502.04878},
  note = {Accepted to ICLR 2025}
}
