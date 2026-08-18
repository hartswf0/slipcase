ZETTEL

ID:
SHOT-20260817-05

TITLE:
2026-08-17 — The prompt can call a temporary program into existence and let it disappear after the shot.

SOURCE:
OpenAI — “Programmatic Tool Calling” — OpenAI API documentation — accessed 2026-08-17.
SOURCE URL: https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling

PASSAGE:
[QUOTE]
“Let models compose and run JavaScript that orchestrates tool calls.”

RESEARCH OBJECT:
EPHEMERAL PROGRAMMING.

LOCAL MOVE:
[[MJ-2022-010]] speculated that prompt craft might disappear as models became better at ordinary language.

[[MJ-2022-011]] then anticipated movement beyond the text command line.

[[SHOT-20260817-04]] shows that contemporary users can still call procedural routes in language.

Programmatic Tool Calling reveals a stranger outcome:

natural language does not need to disappear in favor of code.

Language can summon the code it needs.

The prompt describes or constrains the operation.

The model writes an ephemeral program.

The program performs the deterministic portion.

Then control returns to language.

SOURCE TERMS:
“JavaScript”
“orchestrates”
“tool calls”
“loops”
“conditions”
“parallel”
“intermediate results”
“predictable control flow”

WHAT BECAME STRANGE:
The natural-language prompt and program text need not compete for the same role.

The prompt can be upstream of code.

The code can exist only for the duration of one operational necessity.

QUESTION:
Is ephemeral generated control flow becoming a new programming unit between prompt and persistent software?

DEEPER QUESTION:
What should remain unresolved in language, and what should be temporarily formalized into deterministic procedure?

MECHANISM:
User supplies goal.

Model reasons semantically.

Model detects a predictable subproblem.

Model generates code.

Code:
loops
branches
calls tools
filters intermediate data.

Code returns result.

Model resumes semantic interpretation.

FORMAL SHIFT:
PROMPT
→ TOOL
→ PROMPT
→ TOOL
→ PROMPT

becomes

PROMPT
→ MODEL
→ TEMPORARY PROGRAM {
    TOOL
    LOOP
    CONDITION
    PARALLEL CALL
}
→ RESULT
→ MODEL

SOURCE FORMALISM:
[PARAPHRASE]

OpenAI documents programmatic tool calling as a mechanism where generated JavaScript can coordinate allowed tool calls and intermediate control flow.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

LANGUAGE
→ DEFER FORMALIZATION
→ IDENTIFY DETERMINISTIC SUBSPACE
→ COMPILE SUBSPACE
→ EXECUTE
→ DISSOLVE PROGRAM
→ RETURN TO LANGUAGE

TENSION:
[[MJ-2022-010]] imagined better natural-language understanding eliminating prompt craft.

The current-day trajectory suggests almost the opposite:

natural language can survive precisely because it delegates exact procedure to generated code only when exact procedure becomes useful.

The boundary is therefore not:

LANGUAGE versus CODE.

It is:

JUDGMENT versus PROCEDURE.

MISSING:
A reliable operation for detecting when a task region has become sufficiently specified to compile.

Possible conditions:

stable inputs
known tool set
deterministic branching
no unresolved semantic judgment
bounded side effects
known recovery path.

BOUNDARY:
Programmatic Tool Calling is an OpenAI API capability.

The concept EPHEMERAL PROGRAMMING is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[MJ-2022-010]]
→ prompt craft may disappear
→ [[MJ-2022-011]]
→ text interface may branch into other control surfaces
→ [[SHOT-20260817-04]]
→ language specifies route
→ programmatic tool calling
→ route becomes generated code
→ language and code alternate during one operation

TEST:
On current 2026-08-17 agent workflows, annotate every step:

J = requires semantic judgment
D = sufficiently deterministic.

Compile maximal contiguous D regions into temporary code while leaving J regions model-mediated.

Compare against an all-model tool loop.

Measure:

tokens
latency
execution errors
semantic errors
recovery
auditability.

PLATFORM:
OpenAI Responses API
Programmatic Tool Calling
Agentic workflows

LINKS:
[[MJ-2022-010]]
[[MJ-2022-011]]
[[SHOT-20260817-04]]
[[SHOT-20260817-06]]
[[SHOT-20260817-08]]

BIBTEX:
NONE
