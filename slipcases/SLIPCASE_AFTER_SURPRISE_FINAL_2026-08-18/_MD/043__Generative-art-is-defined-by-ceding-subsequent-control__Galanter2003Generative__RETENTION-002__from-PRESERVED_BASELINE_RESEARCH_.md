ZETTEL

ID:
RETENTION-002

TITLE:
Generative art is defined by ceding subsequent control, so loss of local steering can be a positive feature of the production path.

SOURCE:
Philip Galanter — “What is Generative Art? Complexity Theory as a Context for Art Theory” — Generative Art 2003 Conference — pp. 3, 15–16.

PASSAGE:
[PARAPHRASE]
Galanter defines generative art through the use of a system that operates with some autonomy and says the artist thereby cedes partial or total subsequent control. He later contrasts such practice with making intuitive design judgments throughout construction.

RESEARCH OBJECT:
CONTROL is not one scalar quantity.

Generative practice can deliberately trade:

LOCAL MOMENT-TO-MOMENT CONTROL

for:

UPSTREAM CONTROL OVER A SYSTEM.

LOCAL MOVE:
The parent searches for consequential branches where someone notices a difference and steers the trajectory.

Galanter identifies an art form partly constituted by removing the artist from many such downstream branches.

SOURCE TERMS:
generative art
autonomous system
subsequent control
system
art making
intuitive design judgments

WHAT BECAME STRANGE:
A workflow with fewer downstream interventions may involve MORE deliberate system design rather than less agency.

QUESTION:
Can two production paths have equal total agency but radically different distributions of control over time?

DEEPER QUESTION:
Should authorship/control analysis integrate control across the whole causal graph rather than count interventions near the final artifact?

MECHANISM:
artist
→ designs/selects system G
→ sets G in motion

then:

G
→ autonomous transformations
→ output.

Possible later artist intervention is optional rather than definitional.

FORMAL SHIFT:
<CONTINUOUS DIRECT CONTROL>
→ <SYSTEM DESIGN>
→ [AUTONOMOUS GENERATION]
→ <RESULT>

SOURCE FORMALISM:
Galanter’s definition requires a system sufficiently defined and self-contained to operate with some autonomy.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Represent control as a vector:

    C =
    <C_system,
     C_initialization,
     C_trajectory,
     C_selection,
     C_modification>

rather than:

    C ∈ ℝ.

Two works may satisfy:

    ΣC_A ≈ ΣC_B

while:

    C_A ≠ C_B

component-wise.

TENSION:
There is no obvious commensurable unit allowing different forms of control to be summed.

The vector may be analytically safer than any “total control” score.

MISSING:
A representation-invariant way to compare upstream system design with downstream steering.

BOUNDARY:
Local loss of control cannot by itself diagnose absence of creative agency.

Generative practice may intentionally place agency upstream.

CITATION TRAIL:
[[PATH-001]]
→ consequential branch
→ Galanter on autonomous generative systems
→ artist cedes subsequent control
→ control must be localized rather than merely counted.

TEST:
Take three workflows producing visually comparable artifacts:

A.
direct hand construction

B.
rule-based generator with no curation

C.
stochastic generator with extensive curation.

For each annotate every controllable variable by stage.

Compare control topology rather than number of interventions.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[PATH-001]]
[[generative-art]]
[[control-topology]]
[[autonomy]]
[[system-design]]

BIBTEX:
@inproceedings{Galanter2003Generative,
  author    = {Galanter, Philip},
  title     = {What is Generative Art? Complexity Theory as a Context for Art Theory},
  booktitle = {Proceedings of Generative Art 2003},
  year      = {2003}
}
