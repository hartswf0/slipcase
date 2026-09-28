ZETTEL

ID:
ENCOUNTER-OP-029

TITLE:
The encounter may have to be measured as a trajectory of coordination rather than as properties of either participant.

SOURCE:
Nancy J. Cooke, Jamie C. Gorman, Christopher W. Myers, and Jasmine L. Duran — “Interactive Team Cognition” — 2013 — Cognitive Science 37(2), 255–285. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/23167661/))

PASSAGE:
[QUOTE] Interactive Team Cognition treats team cognition as “an activity, not a property or a product.” ([doi.org](https://doi.org/10.1111/cogs.12009))

RESEARCH OBJECT:
The appropriate measurement unit for relational intelligence may be the temporal organization of interaction itself.

LOCAL MOVE:
Cooke and colleagues oppose accounts that infer team cognition primarily from similarity between static individual knowledge structures. They instead place interaction, coordination, context, and adaptation at the team level.

SOURCE TERMS:
interactive team cognition
team interaction
activity
team level
context
coordination
communication flow
adaptation

WHAT BECAME STRANGE:
Human score + AI score cannot necessarily recover a relational phenomenon. Even perfect individual measures can miss whether the coupled process adapts coherently.

QUESTION:
What properties exist in a human–AI trajectory that cannot be assigned to either participant independently?

DEEPER QUESTION:
Could relational intelligence be measured without attributing cognition to the AI at all?

MECHANISM:
heterogeneous perspectives/capabilities
→ interaction
→ temporally coordinated action
→ adaptation to changing conditions
→ team-level performance.

FORMAL SHIFT:
<HUMAN VARIABLES + AI VARIABLES>
→ <TIME-ORDERED JOINT ACTIVITY>
→ [DYNAMIC COORDINATION ANALYSIS]
→ <RELATIONAL PROCESS MEASURE>

SOURCE FORMALISM:
Interactive Team Cognition advances three premises:
team cognition is an activity;
it should be studied at the team level;
it is inseparable from context. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/23167661/))

The authors also describe measures based on communication flow, speaker/listener identities, and timing in team tasks. ([doi.org](https://doi.org/10.1111/cogs.12009))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SESSION =
{e₁, e₂, ... eₙ}

where each event records:
actor,
timestamp,
operation,
referent,
artifact-state,
response-to-prior-event.

Candidate relational variables:
CROSS-ACTOR DEPENDENCY
ADAPTATION AFTER PERTURBATION
COORDINATION LATENCY
TURN-TO-TURN INFORMATION GAIN
STATE-TRANSITION DIVERSITY.

TENSION:
Shared-mental-model approaches can measure convergence between participants. Interactive Team Cognition warns that convergence may be unnecessary or even less informative than adaptive coordination.

MISSING:
A principled translation from human team interaction to human–AI systems whose participants have radically different internal architectures.

BOUNDARY:
Cooke et al. study human teams. Applying team cognition to AI does not imply the machine possesses human cognition.

CITATION TRAIL:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-008]]
→ Interactive Team Cognition
→ dynamical coordination
→ cross-recurrence / temporal coupling
→ human–AI encounter trajectories.

TEST:
For the same corpus, compare prediction of independent expert-rated task development using:
A. individual user/model features,
B. final output features,
C. temporal relational features.
If C adds explanatory power beyond A+B, the interaction contains measurable structure not captured by participant properties alone.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-008]]
[[Interaction-Level Measure]]
[[Relational Intelligence]]

BIBTEX:
@article{CookeEtAl2013Interactive,
  author = {Nancy J. Cooke and Jamie C. Gorman and Christopher W. Myers and Jasmine L. Duran},
  title = {Interactive Team Cognition},
  journal = {Cognitive Science},
  year = {2013},
  volume = {37},
  number = {2},
  pages = {255--285},
  doi = {10.1111/cogs.12009}
}