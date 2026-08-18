ZETTEL

ID:
FORAGE-WINFIELD-BLACKMORE-002

TITLE:
NOVELTY CAN BEGIN AS A BAD COPY THAT LATER BECOMES A GOOD COPY

SOURCE:
Alan F. T. Winfield and Susan Blackmore — Experiments in Artificial Culture: from noisy imitation to storytelling robots — 2022 — §2 Copybots

SOURCE URL:
https://arxiv.org/abs/2106.11754

PASSAGE:
[PARAPHRASE]
Embodied imitation introduced errors. A poor-fidelity copy could generate a substantially changed behavior; subsequent high-fidelity copying could then preserve and spread that mutation.

The authors also observed cases where imitation errors accelerated later learning.

RESEARCH OBJECT:
Variation and preservation need not come from the same operation.

Low fidelity can create the novelty.
High fidelity can make the novelty durable.

LOCAL MOVE:
The Copybot experiments turn copying error from implementation noise into an evolutionary operator.

SOURCE TERMS:
noisy imitation
variation
behavioural heredity
high-fidelity imitation
behavioural species
embodied social learning

WHAT BECAME STRANGE:
Originality may depend less on escaping imitation than on alternating imperfect and accurate imitation.

QUESTION:
What happens if creative systems are designed around controlled transitions between miscopying and faithful copying rather than around explicit novelty objectives?

DEEPER QUESTION:
Does creativity require a two-stage machine:

first, a mechanism allowed to misunderstand;
then, a mechanism capable of remembering the misunderstanding accurately?

MECHANISM:
<BEHAVIOR A>
→ imperfect embodied observation
→ MUTATED BEHAVIOR B
→ high-fidelity copying of B
→ B becomes persistent
→ lineage diverges from A

FORMAL SHIFT:
<SOURCE BEHAVIOR>
→ <IMPERFECT REPRESENTATION>
→ [MISCOPY]
→ <HERITABLE NOVELTY>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

NOVELTY
≠ maximal randomness

Possible generative sequence:

low-fidelity transformation
→ selection
→ high-fidelity propagation.

TENSION:
Many creative systems simultaneously demand:
"be original"
and
"follow the reference accurately."

The experiment suggests separating these demands temporally rather than averaging them into one generation step.

MISSING:
A controllable account of which distortions generate useful novelty and which merely destroy structure.

BOUNDARY:
The experiment establishes behavioral evolution in simple robot movement patterns, not a general theory of artistic creativity.

"Behavioural species" is an experimental description within this artificial-cultural system, not proof of biological speciation or aesthetic originality.

CITATION TRAIL:
Winfield and Erbas — noisy robot imitation.
Research on iterated learning.
Copying error in cultural evolution.
Mutation-selection balance.
Studies of creative constraint and transformation.

TEST:
Give a generative model a reference artifact.

Compare:

A. direct originality instruction;
B. maximum-faithfulness copying;
C. deliberate lossy reconstruction followed by faithful elaboration of the reconstruction.

Blind-rate resulting artifacts for both novelty and coherence.

PLATFORM:
[[winfield_blackmore_2022_artificial_culture.platform6]]

LINKS:
[[forgetting-can-stabilize-culture]]
[[creative-miscopy]]
[[originality-without-originality-objective]]

BIBTEX:
@article{winfield2022artificialculture,
  title={Experiments in Artificial Culture: from noisy imitation to storytelling robots},
  author={Winfield, Alan F. T. and Blackmore, Susan},
  journal={Philosophical Transactions of the Royal Society B: Biological Sciences},
  volume={377},
  number={1843},
  year={2022},
  url={https://arxiv.org/abs/2106.11754}
}
