ZETTEL

ID:
ENCOUNTER-OP-025

TITLE:
Connection events make relational participation computable without claiming access to inner states.

SOURCE:
Charles Rich, Brett Ponsler, Aaron Holroyd, and Candace L. Sidner — “Recognizing Engagement in Human-Robot Interaction” — 2010 — HRI ’10, pp. 375–382. ([doi.org](https://doi.org/10.1145/1734454.1734580))

PASSAGE:
[PARAPHRASE] Their computational model recognizes four kinds of connection events: directed gaze, mutual facial gaze, conversational adjacency pairs, and backchannels. ([doi.org](https://doi.org/10.1145/1734454.1734580))

RESEARCH OBJECT:
Encounter can be operationalized first as an event stream rather than as an inferred emotion, attitude, or metaphysical relation.

LOCAL MOVE:
Rich and colleagues translate engagement theory into independently detectable interaction events and package the recognizers as computational machinery.

SOURCE TERMS:
engagement
connection events
directed gaze
mutual facial gaze
conversational adjacency pairs
backchannels
recognizer

WHAT BECAME STRANGE:
An encounter detector does not initially need to determine whether the human “feels engaged” or whether the machine “understands.” It can detect whether the interaction repeatedly produces recognizable signs of relational connection.

QUESTION:
What are the LLM equivalents of HRI connection events?

DEEPER QUESTION:
Which connection events require actual reciprocal contingency rather than merely an output that resembles reciprocity?

MECHANISM:
raw behavior
→ event recognition
→ temporally distributed connection evidence
→ engagement-state inference.

FORMAL SHIFT:
<MULTIMODAL ACTIVITY STREAM>
→ <CONNECTION EVENTS>
→ [EVENT RECOGNITION]
→ <RELATIONAL STATE ESTIMATE>

SOURCE FORMALISM:
Four implemented recognizers:
DIRECTED GAZE
MUTUAL FACIAL GAZE
CONVERSATIONAL ADJACENCY PAIRS
BACKCHANNELS

The system was implemented as a ROS component and preliminarily evaluated in a human–robot pointing game. ([doi.org](https://doi.org/10.1145/1734454.1734580))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For text-based AI:

CONNECTION_EVENT ∈ {
  SUMMONS_UPTAKE,
  QUESTION_ANSWER_PAIR,
  REFERENCE_UPTAKE,
  ACKNOWLEDGMENT,
  BACKCHANNEL,
  UNDERSTANDING_CHECK,
  REPAIR_INITIATION,
  REPAIR_RESOLUTION,
  CLOSING_UPTAKE
}

Encounter continuity becomes a temporal pattern over events rather than TURN_COUNT alone.

TENSION:
A fluent LLM can generate adjacency pairs and acknowledgments by construction. Their presence may therefore have much lower discriminative value than they do in embodied HRI.

MISSING:
Connection events whose occurrence depends upon previous relational state rather than generic dialogue competence.

BOUNDARY:
Recognizable connection behavior is evidence of interactional organization, not evidence of machine consciousness, intention, or genuine mutual understanding.

CITATION TRAIL:
[[ENCOUNTER-OP-024]]
[[ENCOUNTER-006]]
→ Rich et al. 2010
→ conversation analysis
→ repair
→ textual connection-event grammar.

TEST:
Build a turn-level annotation scheme for the proposed textual connection events. Compare:
single-shot QA,
multi-turn factual assistance,
iterative co-creation,
and sustained open conversation.
Test which event types discriminate these conditions after controlling for raw turn count.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-002]]
[[Connection Events]]
[[Computable Encounter]]

BIBTEX:
@inproceedings{RichEtAl2010Engagement,
  author = {Charles Rich and Brett Ponsler and Aaron Holroyd and Candace L. Sidner},
  title = {Recognizing Engagement in Human-Robot Interaction},
  booktitle = {Proceedings of the 5th ACM/IEEE International Conference on Human-Robot Interaction},
  year = {2010},
  pages = {375--382},
  doi = {10.1145/1734454.1734580}
}