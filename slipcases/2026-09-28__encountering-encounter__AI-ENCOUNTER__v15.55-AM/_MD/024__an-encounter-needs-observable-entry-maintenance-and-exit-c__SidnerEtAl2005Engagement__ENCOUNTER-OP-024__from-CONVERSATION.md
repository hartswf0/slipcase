ZETTEL

ID:
ENCOUNTER-OP-024

TITLE:
An encounter needs observable entry, maintenance, and exit conditions before it needs a score.

SOURCE:
Candace L. Sidner, Christopher Lee, Cory D. Kidd, Neal Lesh, and Charles Rich — “Explorations in Engagement for Humans and Robots” — 2005 — Artificial Intelligence 166(1–2), 140–164. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0004370205000512))

PASSAGE:
[QUOTE] Engagement is the process by which participants “start, maintain and end their perceived connection to one another.” ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0004370205000512))

RESEARCH OBJECT:
Before asking whether an encounter is strong, transformative, or meaningful, operationalization needs to determine whether a bounded relational episode has occurred at all.

LOCAL MOVE:
Sidner and colleagues replace engagement-as-feeling with engagement-as-process. The phenomenon has temporal organization: connection is established, maintained, and terminated.

SOURCE TERMS:
engagement
start
maintain
end
perceived connection
conversation
collaboration
engagement gestures

WHAT BECAME STRANGE:
“Multi-turn” is a weak proxy for encounter duration. Twenty turns can occur without any identifiable transition into a jointly maintained relation, while a short sequence can contain explicit entry, maintenance checking, and disengagement.

QUESTION:
What observable events mark the transition from mere availability to an active human–AI encounter?

DEEPER QUESTION:
Can an encounter fail to begin even though prompt-response traffic is occurring?

MECHANISM:
availability
→ initiation/contact
→ uptake
→ maintained connection
→ checking/renewal
→ disengagement
→ termination.

FORMAL SHIFT:
<UNSEGMENTED CHAT LOG>
→ <RELATIONAL PHASES>
→ [BOUNDARY DETECTION]
→ <ENCOUNTER EPISODE>

SOURCE FORMALISM:
The source conceptualizes engagement as a process with a beginning, maintenance, and ending; it does not supply a general-purpose formal state machine for LLM interaction.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

STATE ∈ {
  AVAILABLE,
  INITIATING,
  ESTABLISHED,
  MAINTAINING,
  DISENGAGING,
  ENDED
}

An operational encounter detector first estimates transition times:

t_start
t_established
t_last_renewal
t_end

Only events between t_established and t_end belong to the bounded encounter.

TENSION:
[[ENCOUNTER-AI-016]] defines encounters through sustained multi-turn generative coupling, but “sustained” remains underspecified without observable boundary conditions.

MISSING:
Textual or multimodal equivalents of the engagement signals that allow beginning, maintenance, and ending to be inferred reliably.

BOUNDARY:
Sidner et al. study engagement with an embodied robot. Their findings do not establish that the same cues identify encounter boundaries in text-only LLM interaction.

CITATION TRAIL:
[[ENCOUNTER-AI-016]]
→ Sidner et al. 2005
→ Rich et al. 2010 computational recognition
→ conversation openings/closings
→ LLM encounter segmentation.

TEST:
Create a corpus containing complete human–LLM sessions rather than isolated turns. Have independent annotators mark:
NO ENCOUNTER,
INITIATION,
ESTABLISHED,
MAINTENANCE,
DISENGAGEMENT,
END.
Then test whether turn count, elapsed time, adjacency structure, topic persistence, acknowledgment, and explicit closing predict those boundaries.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-016]]
[[ENCOUNTER-002]]
[[Encounter Boundary]]
[[Temporal Encounter]]

BIBTEX:
@article{SidnerEtAl2005Engagement,
  author = {Candace L. Sidner and Christopher Lee and Cory D. Kidd and Neal Lesh and Charles Rich},
  title = {Explorations in Engagement for Humans and Robots},
  journal = {Artificial Intelligence},
  year = {2005},
  volume = {166},
  number = {1-2},
  pages = {140--164},
  doi = {10.1016/j.artint.2005.03.005}
}