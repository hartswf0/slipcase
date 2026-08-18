ZETTEL

ID:
SHOT-20260817-04

TITLE:
2026-08-17 — Call the route, not only the destination.

SOURCE:
OpenAI — “o3/o4-mini Function Calling Guide” — OpenAI Cookbook — published 2025-05-26 — current guidance consulted 2026-08-17.
SOURCE URL: https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide

PASSAGE:
[PARAPHRASE]
OpenAI illustrates multi-tool workflows in which the model first checks necessary state, then checks eligibility or policy, then performs the mutating operation, then communicates the result.

RESEARCH OBJECT:
PROCEDURAL SHOT CALLING.

LOCAL MOVE:
[[MJ-2022-001]] framed prompt craft as protecting intention against unwanted interpretation.

[[SHOT-20260817-01]] adds ACTION MODE:

do not merely talk about the requested change.

This child asks a further question:

Even after execution is authorized, should the user specify only the destination?

Or should the user also specify the legal path?

“Refund this order”

is an end state.

“Check delivery, verify eligibility, issue refund, then notify”

is a state-transition program written in ordinary language.

SOURCE TERMS:
“sequence”
“tools”
“functions”
“boundaries”
“completed”
“constraints”

WHAT BECAME STRANGE:
Natural language becomes dramatically more program-like when it names the transitions that must occur rather than only the final state.

QUESTION:
Which parts of an agentic workflow should the human call explicitly, and which should remain open for model planning?

DEEPER QUESTION:
Is the stable division of labor:

HUMAN:
critical dependencies and invariants

MODEL:
route through everything else?

MECHANISM:
Goal enters.

Precondition A must be observed.

A determines whether B is legal.

B determines whether state mutation C is authorized.

Successful C produces postcondition D.

FORMAL SHIFT:
END STATE:

“Make X true.”

becomes

STATE₀
→ OBSERVE
→ STATE₁
→ CHECK
→ STATE₂
→ MUTATE
→ STATE₃
→ VERIFY
→ REPORT

SOURCE FORMALISM:
[PARAPHRASE]

OpenAI's guide demonstrates ordered sequences of function use for tasks whose valid execution depends on earlier observations and policy checks.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SHOT =
GOAL
+
DEPENDENCIES
+
PRECONDITIONS
+
CRITICAL ORDER
+
STOP CONDITIONS
+
POSTCONDITIONS

TENSION:
[[SHOT-20260817-02]] says rules should be placed close to operations.

This zettel says some relationships between operations must remain visible across the entire workflow.

Local scope alone cannot represent dependency.

Too little procedure creates unsafe improvisation.

Too much procedure turns the model into a brittle script executor.

MISSING:
A practical vocabulary separating:

MUST HAPPEN BEFORE
MAY HAPPEN BEFORE
REQUIRES
PREFER
NEVER
UNTIL
RETRY
ROLL BACK
ASK BEFORE
VERIFY AFTER.

BOUNDARY:
The source provides engineering patterns, not a universal claim that ordered prompting is always superior.

CITATION TRAIL:
[[MJ-2022-001]]
→ ambiguity
→ [[SHOT-20260817-01]]
→ action mode
→ current multi-tool workflows
→ route becomes explicit
→ [[SHOT-20260817-05]]
→ predictable routes can be compiled into temporary code

TEST:
Choose ten multi-tool tasks on 2026-08-17.

Prompt each as:

GOAL ONLY

ORDERED STEPS

DEPENDENCIES ONLY

INVARIANTS + AUTONOMOUS PLANNING.

Inject an unexpected intermediate failure.

Measure:

completion
unsafe action
unnecessary steps
ability to recover
ability to exploit an alternate route.

PLATFORM:
Tool-calling agents
Workflow automation
Coding agents

LINKS:
[[MJ-2022-001]]
[[SHOT-20260817-01]]
[[SHOT-20260817-02]]
[[SHOT-20260817-05]]
[[SHOT-20260817-06]]

BIBTEX:
NONE
