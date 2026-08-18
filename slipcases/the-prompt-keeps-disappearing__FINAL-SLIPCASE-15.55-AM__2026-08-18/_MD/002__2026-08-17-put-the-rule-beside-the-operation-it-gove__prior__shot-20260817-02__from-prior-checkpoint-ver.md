ZETTEL

ID:
SHOT-20260817-02

TITLE:
2026-08-17 — Put the rule beside the operation it governs.

SOURCE:
OpenAI — “o3/o4-mini Function Calling Guide” — OpenAI Cookbook — published 2025-05-26 — current guidance consulted 2026-08-17.
SOURCE URL: https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide

PASSAGE:
[QUOTE]
“This serves as a durable interface contract between reasoning models and tool APIs.”

RESEARCH OBJECT:
LOCALIZED PROMPT POLICY.

LOCAL MOVE:
[[MJ-2022-003]] discovered that the visible prompt is not the final machine representation.

[[MJ-2022-008-A]] showed a related spatial movement in interface history:

situated practice
→ systematization
→ interface primitive.

Current function-calling practice introduces another movement.

Instructions themselves migrate toward the operation they constrain.

Instead of one giant prompt saying:

never overwrite files
only refund delivered orders
look up users before modification
never invent identifiers

the relevant rule can live beside:

file_write
refund
user_update
database_lookup.

The specification becomes spatially distributed across the agent's action surface.

SOURCE TERMS:
“function description”
“usage criteria”
“arguments”
“interface contract”
“tool”
“developer instructions”

WHAT BECAME STRANGE:
The prompt no longer has one canonical location.

The behavior of the system can be distributed across:

system instructions
tool descriptions
schemas
runtime context
state
examples
review policies.

Prompt engineering therefore starts to look less like writing one document and more like arranging laws across a computational territory.

QUESTION:
Which instruction belongs at which scope?

DEEPER QUESTION:
Is prompt architecture developing the equivalent of lexical scope, where rules should be bound to the smallest domain in which they are valid?

MECHANISM:
Global policy establishes universal invariants.

Tool-local policy specifies:
when operation O is available
what preconditions O requires
what O must never do
how O's arguments are constructed.

When the agent considers O, the relevant rules are encountered locally.

FORMAL SHIFT:
ONE PROMPT
→ MANY GOVERNING LOCATIONS

SOURCE FORMALISM:
[PARAPHRASE]

OpenAI's function-calling guidance recommends placing detailed invocation criteria and argument requirements in function descriptions so the tool definition itself serves as an interface contract.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT SCOPE:

GLOBAL
PROJECT
ROLE
STATE
TOOL
ARGUMENT
TURN

Rule R should ideally live at:

smallest_scope(R)

that still governs every situation where R must hold.

TENSION:
Centralizing rules makes the total specification easier for humans to inspect.

Localizing rules makes them more salient when the operation is selected.

This creates a new engineering tradeoff:

HUMAN LEGIBILITY
versus
MODEL-LOCAL RELEVANCE.

[[SHOT-20260817-07]] complicates this further because rules can later be synthesized from execution traces and inserted into changing scopes.

MISSING:
A prompt-scope calculus.

We do not yet have robust conventions for deciding whether a correction belongs to:

this turn
this tool
this project
this agent
all future tasks.

BOUNDARY:
The source concerns OpenAI function calling.

The analogy to lexical scope is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[MJ-2022-003]]
→ machine receives representations beneath visible language
→ [[MJ-2022-008-A]]
→ practice becomes formalized interface
→ current function descriptions become behavioral contracts
→ prompt fragments move beside operations
→ [[SHOT-20260817-07]]
→ execution can later rewrite those fragments

TEST:
Take one agent with twelve behavioral constraints.

Implement three versions dated 2026-08-17:

GLOBAL:
all rules in one system prompt.

LOCAL:
each rule attached only to the tool or state it governs.

HYBRID:
critical invariants global, operation-specific constraints local.

Measure:

tool-selection accuracy
argument errors
rule violations
cross-tool interference
prompt-token cost
human auditability.

PLATFORM:
OpenAI function calling
Tool-using agents

LINKS:
[[MJ-2022-003]]
[[MJ-2022-008-A]]
[[SHOT-20260817-03]]
[[SHOT-20260817-04]]
[[SHOT-20260817-07]]

BIBTEX:
NONE
