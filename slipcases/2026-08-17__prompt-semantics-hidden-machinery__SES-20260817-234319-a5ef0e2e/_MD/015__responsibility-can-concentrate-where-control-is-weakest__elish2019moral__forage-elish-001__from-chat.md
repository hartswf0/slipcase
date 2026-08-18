ZETTEL

ID:
FORAGE-ELISH-001

TITLE:
RESPONSIBILITY CAN CONCENTRATE WHERE CONTROL IS WEAKEST

SOURCE:
Madeleine Clare Elish — Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction — 2019 — Abstract / analysis of distributed control and responsibility

PASSAGE:
[PARAPHRASE]
Elish argues that in complex automated systems agency and control can be distributed across actors, components, institutions, and time while responsibility after failure becomes concentrated on a nearby human operator who exercised comparatively little control.

She calls this configuration a moral crumple zone.

RESEARCH OBJECT:
The architecture that distributes causal agency need not be the architecture that distributes blame.

LOCAL MOVE:
The source separates two questions commonly collapsed in discussions of autonomous systems:

Who participated in producing the action?

Who becomes responsible after the action fails?

SOURCE TERMS:
moral crumple zone
distributed agency
control
responsibility
human-in-the-loop
automated system
misattribution

WHAT BECAME STRANGE:
Making agency harder to locate can make blame easier to locate.

The nearest visible human can become the endpoint into which an otherwise distributed system discharges responsibility.

QUESTION:
If effective agency belongs to an assemblage, why should responsibility follow the most human-looking node rather than the distribution of actual control?

DEEPER QUESTION:
Could "human oversight" itself become a mechanism for protecting automated systems by manufacturing a person onto whom failure can be attributed?

MECHANISM:
<DISTRIBUTED SOCIOTECHNICAL CONTROL>
→ automated action
→ failure
→ demand for accountable actor
→ attribution compresses distributed causation
→ nearest / legible human absorbs responsibility
→ technological and institutional architecture recedes

FORMAL SHIFT:
<DISTRIBUTED CONTROL>
→ <SYSTEM FAILURE>
→ [RESPONSIBILITY ATTRIBUTION]
→ <CONCENTRATED HUMAN LIABILITY>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

C_i = actual control exercised by actor i
R_i = responsibility assigned after failure

A naive accountability model expects:

R_i ∝ C_i

The moral-crumple-zone hypothesis identifies cases where:

low C_human
coexists with
high R_human.

The mapping from causation to responsibility is therefore itself an institutional mechanism requiring analysis.

TENSION:
[[FORAGE-SHANAHAN-002]] proposed that effective agency can be located across a pipeline even without a persistent inner agent.

Elish makes the governance consequence more difficult.

If agency is distributed, merely declaring the "system" agentic does not distribute responsibility.

Nor does retaining a human-in-the-loop guarantee meaningful human control.

The human may instead become the system's liability surface.

MISSING:
A method for mapping:

authority,
information,
intervention capacity,
temporal opportunity,
causal contribution,
and assigned responsibility

across an AI-agent pipeline.

"Human approval" alone does not reveal any of these.

BOUNDARY:
Elish analyzes accidents and responsibility in complex automated and autonomous sociotechnical systems.

The concept does not by itself determine legal liability for contemporary LLM agents, nor prove that every human oversight role functions as a moral crumple zone.

CITATION TRAIL:
[[FORAGE-SHANAHAN-002]]
→ Elish's moral crumple zone
→ Bainbridge's ironies of automation
→ authority-responsibility mismatch
→ contemporary tool-using AI agents
→ whether human confirmation interfaces transfer responsibility without transferring meaningful control

TEST:
For a real or simulated tool-using AI failure, reconstruct every consequential decision as a timeline.

For each actor or component record:

information available,
actions available,
time available to intervene,
authority to override,
causal contribution,
and responsibility assigned afterward.

Then test whether attributed responsibility correlates with actual intervention capacity or merely with human proximity to the final action.

PLATFORM:
[[agency-as-pipeline]]

LINKS:
[[FORAGE-SHANAHAN-002]]
[[responsibility-is-not-distributed-like-agency]]
[[human-in-the-loop-as-liability-surface]]
[[moral-crumple-zone]]

BIBTEX:
@article{elish2019moral,
  title={Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction},
  author={Elish, Madeleine Clare},
  journal={Engaging Science, Technology, and Society},
  volume={5},
  pages={40--60},
  year={2019},
  doi={10.17351/ests2019.260}
}
