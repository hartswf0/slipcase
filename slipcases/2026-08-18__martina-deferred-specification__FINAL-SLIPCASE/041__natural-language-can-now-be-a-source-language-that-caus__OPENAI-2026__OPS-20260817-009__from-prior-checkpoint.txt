ZETTEL

ID:
OPS-20260817-009

TITLE:
Natural language can now be a source language that causes the model to synthesize a temporary program of actions.

SOURCE:
OpenAI Agents SDK — Programmatic Tool Calling — current documentation accessed August 17, 2026.
https://openai.github.io/openai-agents-python/tools/

PASSAGE:
[QUOTE]
“Programmatic Tool Calling lets a supported OpenAI Responses model generate JavaScript that calls eligible tools”

RESEARCH OBJECT:
WORDS → GENERATED PROGRAM → TOOL CALLS → WORLD OPERATIONS.

LOCAL MOVE:
[[MJ-MARTINA-021-A-A]] asked whether a prompt is a score, script, or something else.

Current programmatic tool calling introduces a startling third layer.

The model can respond to natural language not with prose and not immediately with a tool call, but by generating JavaScript that orchestrates multiple permitted tools.

SOURCE TERMS:
“Programmatic Tool Calling”
“generate JavaScript”
“eligible tools”
“loops”
“branching”
“parallel calls”
“intermediate calculations”
“V8 environment”

WHAT BECAME STRANGE:
The prompt can function as source material for a program that does not exist before the request.

The execution chain becomes:

ENGLISH
→ GENERATED JAVASCRIPT
→ TYPED TOOL CALLS
→ EXTERNAL OPERATIONS.

This is much closer to literal “words becoming operations” than ordinary chatbot prompting.

QUESTION:
Is generated orchestration code the missing intermediate representation between natural-language intention and world-changing action?

DEEPER QUESTION:
When the executable program is synthesized only after the user speaks, where does the program begin: in the user's description, the generated JavaScript, the tool schemas, or the complete runtime assemblage?

MECHANISM:
OpenAI's current Agents SDK documents Programmatic Tool Calling in which supported Responses models generate JavaScript capable of calling explicitly permitted tools, combining outputs, looping, branching, and performing intermediate calculations in a hosted V8 environment.

FORMAL SHIFT:
FROM:
USER_LANGUAGE
→ MODEL
→ TOOL_CALL

TO:
USER_LANGUAGE
→ MODEL
→ PROGRAM_SYNTHESIS
→ PROGRAM_EXECUTION
→ TOOL_CALL_1...n
→ RESULT.

SOURCE FORMALISM:
Programmatic Tool Calling:

model
→ generated JavaScript

JavaScript runs in:
fresh hosted V8 environment

Program may access:
only explicitly allowed tools

Program may:
loop
branch
parallelize calls
combine outputs
perform intermediate calculations.

OUR FORMALIZATION:
[OUR FORMORMALIZATION — NOT SOURCE SYNTAX]

NL_INTENTION
→ SYNTHESIZE(P)

where:

P = {
  CONTROL_FLOW,
  TOOL_INVOCATIONS,
  INTERMEDIATE_STATE
}

then:

EXECUTE(P, ALLOWED_TOOLS)
→ WORLD_EFFECTS / DATA_EFFECTS.

The generated program is ephemeral but operationally decisive.

TENSION:
The natural-language prompt alone still does not determine the synthesized program.

Tool inventory, schemas, allowed callers, runtime restrictions, model behavior, and approvals all participate in the resulting operation.

MISSING:
A provenance format that records the chain:

user words
→ generated program
→ each child tool call
→ each state change
→ final result.

BOUNDARY:
Generated JavaScript operates only inside the permissions and environment supplied by the host. Natural language does not magically acquire unrestricted computational authority.

CITATION TRAIL:
[[MJ-MARTINA-021-A-A]]
→ prompt may be executable without being a score
→ programmatic tool calling inserts synthesized code between language and action
→ description becomes source language for transient programs
→ “the prompt is not the program” becomes literally inspectable
→ forage the generated intermediate representation.

TEST:
For one natural-language task, save:

1. exact user request
2. complete tool surface
3. generated JavaScript
4. actual tool-call trace
5. resulting state
6. final response

Repeat fifty times.

Compare identical user language against divergent generated programs.

Ask which invariants remain stable across executions and whether those invariants can be expressed independently of any one generated program.

PLATFORM:
OpenAI Responses API; OpenAI Agents SDK; Programmatic Tool Calling

LINKS:
[[MJ-MARTINA-021-A-A]]
[[MJ-MARTINA-030-A]]
[[OPS-20260817-003]]
[[OPS-20260817-001]]

BIBTEX:
@misc{openai2026programmatictools,
  author = {{OpenAI}},
  title = {OpenAI Agents SDK: Programmatic Tool Calling},
  year = {2026},
  url = {https://openai.github.io/openai-agents-python/tools/}
}
