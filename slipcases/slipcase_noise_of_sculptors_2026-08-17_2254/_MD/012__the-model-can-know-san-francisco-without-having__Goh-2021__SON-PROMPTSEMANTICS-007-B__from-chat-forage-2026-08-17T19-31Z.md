ZETTEL

ID:
SON-PROMPTSEMANTICS-007-B

TITLE:
THE MODEL CAN KNOW SAN FRANCISCO WITHOUT HAVING A SAN FRANCISCO NEURON.

SOURCE:
Gabriel Goh, Chelsea Voss, Daniela Amodei, Shan Carter, Michael Petrov, Justin Jay Wang, Nick Cammarata & Chris Olah — “Multimodal Neurons in Artificial Neural Networks” — OpenAI — March 4, 2021.
SOURCE URL: https://openai.com/index/multimodal-neurons/

PASSAGE:
[PARAPHRASE]
The researchers report that CLIP can perform surprisingly precise geolocation while they could not identify a single “San Francisco” neuron.

[QUOTE]
They suggest the information may instead exist “as a direction or as some other more complex manifold.”

RESEARCH OBJECT:
A REPRESENTABLE CONCEPT NEED NOT HAVE A LOCAL ADDRESS.

LOCAL MOVE:
[[SON-PROMPTSEMANTICS-007]] proposed that prompts act as addresses into learned visual regularities.

But an address metaphor normally assumes something like a destination.

The OpenAI interpretability result makes that assumption unstable.

A model may behave as though it possesses a concept without that concept being isolatable in one neuron or decomposable into obvious constituent concept-neurons.

The “address” may point into a distributed relation.

SOURCE TERMS:
geolocation
neuron
activation
direction
manifold
concept
representation
abstraction

WHAT BECAME STRANGE:
The model can apparently possess actionable knowledge that nobody can point to.

There may be no:

SAN FRANCISCO UNIT
SAN FRANCISCO BOX
SAN FRANCISCO FILE
SAN FRANCISCO SYMBOL

yet the system can still behave as if SAN FRANCISCO exists.

A concept can therefore be operationally real without being locally stored.

QUESTION:
What exactly does a prompt word address if its corresponding model concept has no identifiable location?

DEEPER QUESTION:
Can an executable language have meaningful terms whose denotations exist only as distributed transformations across a high-dimensional system?

MECHANISM:
A neural representation can distribute information across patterns of activity rather than isolate one concept in one component.

A downstream operation can exploit this distributed structure even when interpretability methods fail to identify a single corresponding neuron.

FORMAL SHIFT:
FROM:

WORD
→ ADDRESS
→ CONCEPT LOCATION
→ OPERATION

TO:

WORD
→ PERTURBATION OF DISTRIBUTED REPRESENTATION
→ RELATIONAL PATTERN / DIRECTION / MANIFOLD
→ OPERATION

The address may be a transformation rather than a destination.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Naive localist model:

CONCEPT(C)
=
unit_i

Distributed model:

CONCEPT(C)
=
pattern over {u_1 ... u_n}

or potentially:

CONCEPT(C)
=
direction d_C

or:

CONCEPT(C)
=
region / manifold M_C

Then prompting with token C need not:

LOOK UP(C)

It may instead:

TRANSFORM(state, representation(C)).

TENSION:
Failure to discover a “San Francisco” neuron does not prove that no more localized representation exists.

Interpretability methods are incomplete.

The source itself frames direction/manifold encoding as a hypothesis.

Therefore the strange result is epistemic as much as architectural:

MODEL CAPABILITY
>
OUR ABILITY TO LOCATE ITS REPRESENTATION.

MISSING:
Causal interventions identifying where geolocation information is represented.

Comparison across model layers and architectures.

Whether concepts used effectively in text-to-image prompting exhibit localized, directional, manifold-like, or highly distributed representations.

A theory of MODEL REFERENCE that does not require symbolic storage.

BOUNDARY:
The source concerns CLIP interpretability.

“Direction” and “manifold” are proposed possibilities in this passage, not demonstrated representations of San Francisco.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007]]
→ prompt as address
→ interpretability search for concept units
→ model demonstrates concept-level capability without discoverable concept neuron
→ address metaphor breaks
→ prompt may operate as transformation over distributed state rather than pointer to stored meaning

TEST:
Choose concepts for which a model demonstrates strong behavioral competence.

For each concept attempt:

single-unit ablation
sparse-unit probing
linear-direction probing
distributed-subspace probing
activation patching

Measure which intervention most strongly changes concept-specific behavior.

Then ask whether prompt sensitivity predicts the localization structure.

If powerful prompt terms correspond to distributed rather than localized representations, “magic words” may be handles on transformations that have no single internal referent.

PLATFORM:
OpenAI

LINKS:
[[SON-PROMPTSEMANTICS-007]]
[[SON-PROMPTSEMANTICS-007-A]]

BIBTEX:
@misc{goh2021multimodalneurons,
  author = {Gabriel Goh and Chelsea Voss and Daniela Amodei and Shan Carter and Michael Petrov and Justin Jay Wang and Nick Cammarata and Chris Olah},
  title = {Multimodal Neurons in Artificial Neural Networks},
  year = {2021},
  month = {March},
  howpublished = {OpenAI},
  url = {https://openai.com/index/multimodal-neurons/}
}
