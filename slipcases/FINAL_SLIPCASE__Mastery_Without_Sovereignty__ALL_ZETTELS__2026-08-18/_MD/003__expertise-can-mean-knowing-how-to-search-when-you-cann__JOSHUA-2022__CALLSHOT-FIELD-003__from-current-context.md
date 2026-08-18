ZETTEL

ID:
CALLSHOT-FIELD-003

TITLE:
EXPERTISE CAN MEAN KNOWING HOW TO SEARCH WHEN YOU CANNOT DIRECTLY CONTROL THE RESULT.

SOURCE:
Joshua Larson interview with Watson Hartsoe, 2022-10-18, 32:59 and 48:51. Local source: _RESOURCES/BLUE_MJ_Interview 2_Joshua.pages. SOURCE URL: LOCAL_FILE

PASSAGE:
[QUOTE]
“I just have to accept that I don’t have that level of control”

[QUOTE]
“you just kind of have to wander around.”

RESEARCH OBJECT:
PROMPT CRAFT IS PARTLY CALIBRATED NAVIGATION UNDER INCOMPLETE CONTROLLABILITY.

LOCAL MOVE:
Joshua distinguishes techniques that shift outputs from aesthetics he can only encounter among many samples. He later describes prompt search as wandering among local and global maxima.

SOURCE TERMS:
“stumble upon” · “30 or 40 images” · “control” · “local maxima” · “global maxima” · “wander around” · “experimentation”

WHAT BECAME STRANGE:
The expert does not necessarily know the command that produces the target. Expertise may instead be the ability to recognize promising regions, allocate samples, and know when causality is too weak to claim.

QUESTION:
How should prompt expertise be measured when exact reproducibility is impossible?

DEEPER QUESTION:
Is natural-language control better modeled as distribution steering plus search rather than program execution?

MECHANISM:
DESIRED PROPERTY → PROMPT P → STOCHASTIC SAMPLES → HUMAN JUDGMENT → MUTATE P → REPEAT.

FORMAL SHIFT:
EXPERTISE = COMMAND OF OUTPUT → EXPERTISE = SEARCH + CALIBRATION + PARTIAL STEERING.

SOURCE FORMALISM:
[PARAPHRASE]
Joshua reports both practical prompt techniques and aesthetics he cannot reliably lock in, and uses an optimization-landscape metaphor for experimentation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
O ~ G(P, ξ); skill includes choosing P, choosing N samples, judging O, and estimating whether ΔP has repeatable effect.

TENSION:
The optimization metaphor implies a stable objective landscape, but human taste and model behavior can change during the search.

MISSING:
Repeated-measures evidence separating prompt effect size from lucky samples and evaluator drift.

BOUNDARY:
This describes one practitioner and a 2022 Midjourney model state.

CITATION TRAIL:
[[MJ-JOSHUA-009]] → incomplete control → [[MJ-JOSHUA-013]] maxima metaphor → [[CALLSHOT-FIELD-004]] epistemic action and [[CALLSHOT-FIELD-005]] model adaptation.

TEST:
Have experts and novices target the same aesthetic under fixed model/version/seed policy. Measure not only best output but calibration: predicted controllability versus observed repeatability.

PLATFORM:
Midjourney · stochastic control

LINKS:
[[MJ-JOSHUA-009]] [[MJ-JOSHUA-013]] [[CALLSHOT-FIELD-004]] [[CALLSHOT-FIELD-005]]

BIBTEX:
NONE
