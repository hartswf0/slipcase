ZETTEL

ID:
FORAGE-WALTER-001

TITLE:
THE COMMAND CAN HELP CONSTRUCT THE WORLD REQUIRED TO OBEY IT

SOURCE:
Matthew R. Walter, Siddharth Patki, Andrea F. Daniele, Ethan Fahnestock, Felix Duvallet, Sachithra Hemachandra, Jean Oh, Anthony Stentz, Nicholas Roy, and Thomas M. Howard — Language Understanding for Field and Service Robots in a Priori Unknown Environments — 2021 — Abstract / framework description

PASSAGE:
[PARAPHRASE]
Earlier grounding approaches often assume a detailed spatial-semantic map containing possible referents before a natural-language command can be grounded.

Walter and colleagues instead treat language as another sensor.

Information implicit in an utterance contributes evidence about an unknown environment, allowing the robot to maintain a probability distribution over a latent world model while executing the task.

RESEARCH OBJECT:
Execution need not wait for the world model required to interpret the command.

Interpretation of the command can participate in constructing that world model.

LOCAL MOVE:
The source reverses the usual dependency between world representation and language grounding.

Instead of:

known world → ground language,

it permits:

language + perception + action history → infer world → ground and act.

SOURCE TERMS:
language as a sensor
a priori unknown environment
latent environment model
belief-space policy
probabilistic language grounding
symbolic action space
mental models

WHAT BECAME STRANGE:
The words do not merely specify an action inside a known world.

They can provide evidence that certain parts of the world must exist.

QUESTION:
If a command can supply evidence for the environment in which it becomes executable, where is the boundary between describing a world and constructing the model of that world?

DEEPER QUESTION:
How little shared world structure is actually required before language can bootstrap the missing rest?

MECHANISM:
<UTTERANCE>
+
<ROBOT OBSERVATIONS>
+
<ACTION HISTORY>
→ infer distribution over latent environment model
→ ground language against uncertain model
→ infer symbolic actions
→ act
→ receive new observations
→ update environment belief
→ continue

FORMAL SHIFT:
<COMMAND + UNKNOWN WORLD>
→ <PROBABILITY DISTRIBUTION OVER POSSIBLE WORLDS>
→ [ACT / OBSERVE / UPDATE]
→ <PROGRESSIVELY GROUNDED EXECUTION>

SOURCE FORMALISM:
The framework treats spatial, topological, and semantic information implicit in an utterance as evidence for a latent environment model.

That distribution is incorporated into a probabilistic language-grounding model.

An imitation-learned belief-space policy reasons over environment and behavior distributions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

The parent suggested:

SHARED WORLD MODEL
+
DESCRIPTION
→ EXECUTION

This source supports a weaker requirement:

SHARED GENERATIVE / GROUNDING MACHINERY
+
DESCRIPTION
+
PERCEPTION
→ INFER WORLD MODEL
→ EXECUTION

Compatibility may therefore be required at the level of ontology and inference machinery rather than at the level of a pre-agreed world instance.

TENSION:
[[FORAGE-WINFIELD-BLACKMORE-003]] proposed that a story becomes executable because speaker and listener possess sufficiently compatible machinery for rerunning the transmitted counterfactual.

Walter et al. pressure the strongest version of that claim.

The listener need not already possess the relevant environment model.

Language can help infer it.

But the apparent liberation from a shared world merely pushes the question downward:
the robot must still know what kinds of entities, relations, actions, and evidence the utterance can refer to.

MISSING:
The minimum substrate that must be shared before language can function as a sensor.

Candidates include:

object ontology,
action ontology,
spatial relations,
causal expectations,
parser structure,
embodiment,
or a learned correspondence between language and perception.

BOUNDARY:
The framework does not show that arbitrary descriptions can create arbitrary executable ontologies from nothing.

The robot has substantial prior architecture, learned grounding machinery, sensors, action representations, and task structure.

CITATION TRAIL:
[[FORAGE-WINFIELD-BLACKMORE-003]]
→ natural-language grounding in unknown environments
→ Walter et al.'s language-as-sensor framework
→ symbol emergence / open-world grounding
→ systems that must acquire new concepts, not merely discover new instances
→ the minimum prior structure required for words to build a runnable world

TEST:
Construct a series of increasingly severe mismatches between speaker and robot:

1. unknown locations, shared ontology
2. unknown objects, shared object classes
3. novel object classes
4. novel spatial relations
5. novel action primitives
6. novel causal rules

Give commands that require each missing element.

Measure the first level at which language can no longer bootstrap the world required for execution without external ontology modification.

PLATFORM:
[[description-requires-a-machine-that-can-obey]]

LINKS:
[[FORAGE-WINFIELD-BLACKMORE-003]]
[[language-as-sensor]]
[[the-command-builds-its-own-stage]]
[[minimum-shared-world]]

BIBTEX:
@article{walter2021language,
  title={Language Understanding for Field and Service Robots in a Priori Unknown Environments},
  author={Walter, Matthew R. and Patki, Siddharth and Daniele, Andrea F. and Fahnestock, Ethan and Duvallet, Felix and Hemachandra, Sachithra and Oh, Jean and Stentz, Anthony and Roy, Nicholas and Howard, Thomas M.},
  journal={arXiv preprint arXiv:2105.10396},
  year={2021},
  url={https://arxiv.org/abs/2105.10396}
}
