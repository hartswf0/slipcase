ZETTEL

ID:
OPS-20260817-004

TITLE:
The strongest imperative may not be written in the prompt.

SOURCE:
OpenAI Agents SDK — Agents / Forcing Tool Use — current documentation accessed August 17, 2026.
https://openai.github.io/openai-agents-python/agents/

PASSAGE:
[QUOTE]
“Supplying a list of tools doesn't always mean the LLM will use a tool.”

RESEARCH OBJECT:
TOOL_CHOICE AS EXTRALINGUISTIC IMPERATIVE.

LOCAL MOVE:
[[MJ-MARTINA-014-A-A]] treated prompt engineering as a discipline of learning how to word commands more effectively.

The Agents SDK exposes a stronger operation.

Instead of saying:

“you must use the calculator”

the runtime can set:

tool_choice = required

or specify a particular tool.

SOURCE TERMS:
“tool_choice”
“auto”
“required”
“none”
“specific tool”
“force tool use”

WHAT BECAME STRANGE:
The instruction hierarchy has acquired a layer that is not prose.

A developer can stop trying to persuade the model linguistically and constrain the action space directly.

QUESTION:
Which prompt instructions should cease being prompts and become runtime constraints?

DEEPER QUESTION:
Is mature prompt engineering partly the progressive removal of requirements from natural language into stronger control mechanisms?

MECHANISM:
The Agents SDK exposes `tool_choice` settings that permit the model to choose automatically, require some tool call, forbid tool use, or require a named tool.

FORMAL SHIFT:
FROM:
PROMPT:
“You must call TOOL_X.”

TO:
RUNTIME:
tool_choice = TOOL_X

The requirement moves:

FROM semantic request
TO control configuration.

SOURCE FORMALISM:
tool_choice ∈ {
  auto,
  required,
  none,
  specific_tool_name
}

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For requirement R:

if R can be ENFORCED_BY_RUNTIME
then prefer:

R → CONSTRAINT

rather than:

R → NATURAL_LANGUAGE_REQUEST

This creates a hierarchy:

WISH
< INSTRUCTION
< SCHEMA
< RUNTIME_CONSTRAINT
< EXECUTION_GATE.

TENSION:
Not every behavioral requirement can be translated into a runtime option. Many semantic requirements remain irreducibly interpretive.

MISSING:
A taxonomy mapping common prompt requirements to the strongest currently available enforcement layer.

BOUNDARY:
`tool_choice` constrains whether and which tool is selected; it does not guarantee correct arguments or correct downstream behavior.

CITATION TRAIL:
[[MJ-MARTINA-014-A-A]]
→ user learns to write stronger instructions
→ current APIs permit nonlinguistic enforcement
→ the requirement leaves the prompt
→ forage migration from persuasion to constraint.

TEST:
Collect 100 production prompt clauses containing:
must,
never,
always,
only,
exactly,
do not.

For each ask:

Can this requirement instead be represented as:
schema,
tool configuration,
type,
permission,
guardrail,
state-machine transition,
validator?

Measure failures before and after moving enforceable clauses out of prose.

PLATFORM:
OpenAI Agents SDK

LINKS:
[[MJ-MARTINA-014-A-A]]
[[MJ-MARTINA-013]]
[[MJ-MARTINA-015-A]]

BIBTEX:
@misc{openai2026forcingtools,
  author = {{OpenAI}},
  title = {OpenAI Agents SDK: Forcing Tool Use},
  year = {2026},
  url = {https://openai.github.io/openai-agents-python/agents/}
}
