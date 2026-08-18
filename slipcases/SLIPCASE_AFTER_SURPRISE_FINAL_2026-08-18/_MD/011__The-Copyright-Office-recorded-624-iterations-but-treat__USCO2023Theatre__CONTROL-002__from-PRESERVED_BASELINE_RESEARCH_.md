ZETTEL

ID:
CONTROL-002

TITLE:
The Copyright Office recorded 624 iterations but treated the number as irrelevant to whether Allen controlled the particular expressive result.

SOURCE:
U.S. Copyright Office Review Board — Decision Affirming Refusal to Register Théâtre D’opéra Spatial — September 5, 2023 — pp. 2, 6.

PASSAGE:
[PARAPHRASE]
The administrative record states that Jason Allen reported at least 624 revisions and text prompts before arriving at the initial Midjourney image. The Board nevertheless focused on whether those prompts determined specific expressive elements of the generated result, concluding that the outcome depended on how Midjourney processed the prompts.

RESEARCH OBJECT:
ITERATION COUNT and EXPRESSIVE CONTROL are different variables.

LOCAL MOVE:
The essay’s “odometer versus steering” distinction is unusually well aligned with the structure of the official record.

SOURCE TERMS:
624
revisions
text prompts
creative input
influence
specific expressive result
human authorship

WHAT BECAME STRANGE:
The Board had exactly the evidence that popular discussions often demand:

A LARGE NUMBER OF PROMPTS.

It did not treat that quantity as dispositive evidence of authorship over the generated image.

QUESTION:
What evidence WOULD distinguish repeated search from repeatable control over expressive elements?

DEEPER QUESTION:
Can a legal inquiry into human authorship be operationalized using counterfactual control tests without collapsing legal authorship into engineering controllability?

MECHANISM:
Allen:
prompt revision
→ output
→ inspect
→ revise
→ output
→ repeat ≥624 times.

Board’s question:
did human input determine traditional expressive elements,
or did system processing supply them?

FORMAL SHIFT:
<WORKFLOW LENGTH>
≠
<CONTROL OVER PARTICULAR EXPRESSIVE FEATURES>

SOURCE FORMALISM:
NONE.

The source applies copyright doctrine case-by-case, not a quantitative control metric.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Iteration length:

    L = number of generation/revision cycles.

Control over feature f:

    C_f =
    ability to intentionally set f
    while holding specified neighboring features invariant.

No implication follows automatically:

    large L
    → large C_f.

TENSION:
Repeated iteration can be the process through which a practitioner discovers and exercises genuine control.

The number is therefore not meaningless; it is simply non-diagnostic by itself.

MISSING:
Allen’s actual sequence of prompts and outputs.

Without it, the 624-step path cannot be reconstructed at feature level.

BOUNDARY:
The Office’s decision is evidence about U.S. copyright authorship doctrine in this specific record.

It is not a general scientific verdict that prompting cannot constitute control.

CITATION TRAIL:
[[CONTROL-001]]
→ prospective control test
→ Théâtre D’opéra Spatial
→ 624 iterations
→ iteration quantity fails to reveal steering.

[[UPTAKE-003]]
→ counterfactual control
→ legal record supplies unusually explicit conflict between effort and expressive control.

TEST:
Obtain or reconstruct a generation history.

For each revision classify:

TARGET DECLARED BEFORE OUTPUT
FEATURE CHANGED AS REQUESTED
FEATURE PRESERVED AS REQUESTED
UNREQUESTED ATTRACTIVE CHANGE
POST-HOC SELECTION.

Compute control evidence independently of total prompt count.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[CONTROL-001]]
[[UPTAKE-003]]
[[prompt-count]]
[[authorship]]
[[steering-vs-search]]

BIBTEX:
@misc{USCO2023Theatre,
  author       = {{U.S. Copyright Office Review Board}},
  title        = {Decision Affirming Refusal to Register Théâtre D'opéra Spatial},
  year         = {2023},
  month        = {September},
  day          = {5}
}
