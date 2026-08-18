ZETTEL

ID:
FORAGE-WINFIELD-BLACKMORE-001

TITLE:
FORGETTING CAN STABILIZE CULTURE

SOURCE:
Alan F. T. Winfield and Susan Blackmore — Experiments in Artificial Culture: from noisy imitation to storytelling robots — 2022 — §2 Copybots

SOURCE URL:
https://arxiv.org/abs/2106.11754

PASSAGE:
[PARAPHRASE]
The researchers compared robot collectives with no memory, limited memory, and unlimited memory.

The limited-memory condition produced the most stable population of behavioral types.

RESEARCH OBJECT:
Memory capacity is not monotonically related to cultural persistence.

Under at least one embodied evolutionary mechanism, selective loss can produce greater stability than unlimited retention.

LOCAL MOVE:
The experiment varies memory size rather than treating storage capacity as an unquestioned benefit.

SOURCE TERMS:
limited memory
collective memory
behavioural evolution
memes
stability
forgetting

WHAT BECAME STRANGE:
The archive may preserve a tradition by losing things.

QUESTION:
When does increasing memory make a generative system less stable rather than more capable?

DEEPER QUESTION:
Could forgetting be an active design parameter for artificial cultures, agents, and prompt-driven worlds rather than merely a technical limitation?

MECHANISM:
<BEHAVIORAL VARIANTS>
→ copied into finite memory
→ older variants displaced
→ surviving variants circulate more repeatedly
→ fewer larger behavioral clusters persist

FORMAL SHIFT:
<BEHAVIORAL HISTORY>
→ <BOUNDED MEMORY>
→ [SELECTIVE RETENTION / DISPLACEMENT]
→ <STABLE CULTURAL CLUSTERS>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let M be memory capacity.

The experiment warns against assuming:

cultural stability ∝ M.

A candidate relation may instead be non-monotonic:

stability = f(M)

with an intermediate M producing greater persistence than either M = 0 or effectively unlimited M.

TENSION:
Contemporary agent architectures often frame longer context, larger memory stores, and more complete retrieval as straightforward capability improvements.

The Copybot result suggests that persistence may depend on exclusion.

MISSING:
The mechanism responsible for the limited-memory advantage is not yet general enough to tell us when forgetting stabilizes versus impoverishes a culture.

BOUNDARY:
These are small embodied robot collectives with simple learned movement behaviors.

The experiment does not establish that limited context improves LLM agents, human institutions, or complex cultures.

CITATION TRAIL:
Erbas and Winfield — experiments underlying the limited-memory result.
Cultural-evolution literature on transmission bottlenecks.
Iterated learning.
Agent-memory architectures.
Context-window pruning.

TEST:
Run otherwise identical populations of language-model agents with:

A. complete transcript retention,
B. sliding-window memory,
C. salience-based forgetting,
D. no episodic memory.

Seed several competing conventions and measure lineage diversity, convention persistence, drift, and recovery after perturbation.

PLATFORM:
[[winfield_blackmore_2022_artificial_culture.platform7]]

LINKS:
[[bounded-memory-as-cultural-selection]]
[[context-is-not-memory]]
[[forgetting-as-an-operation]]

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
