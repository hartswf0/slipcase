ZETTEL

ID:
OPS-20260817-001

TITLE:
A tool description is not documentation; it is part of the machine's action-selection policy.

SOURCE:
Model Context Protocol — Schema Reference / Tool — 2025-06-18.
https://modelcontextprotocol.io/specification/2025-06-18/schema

PASSAGE:
[QUOTE]
“This can be used by clients to improve the LLM’s understanding of available tools.”

RESEARCH OBJECT:
TOOL DESCRIPTION AS OPERATIVE AFFORDANCE DESCRIPTION.

LOCAL MOVE:
[[MJ-MARTINA-016]] treated vocabulary as a control surface for generated images. MCP exposes a sharper contemporary case: natural-language descriptions are attached directly to executable tools so that the model can decide which operation is appropriate.

The words do not describe an output.

They describe what can be done.

SOURCE TERMS:
“Tool”
“name”
“description”
“inputSchema”
“outputSchema”
“hint”
“available tools”

WHAT BECAME STRANGE:
Writing “Search the repository for symbols” or “Create a calendar event” is simultaneously documentation for a human and a cue used by a model to choose an executable capability.

The description begins to resemble an affordance inscription:

THIS IS WHAT THIS VERB DOES.

QUESTION:
How much of agent behavior is determined by the wording of tool descriptions rather than the user's prompt?

DEEPER QUESTION:
When a natural-language description participates in selecting an executable operation, has documentation become part of program control flow?

MECHANISM:
MCP Tool objects associate a programmatic name and input schema with an optional human-readable description. The specification explicitly says this description can improve the LLM's understanding of available tools.

FORMAL SHIFT:
FROM:
PROMPT
→ MODEL
→ TEXT

TO:
USER_LANGUAGE
→ MODEL

MODEL sees:
{
  TOOL_NAME,
  TOOL_DESCRIPTION,
  INPUT_SCHEMA
}

→ SELECT_TOOL
→ construct arguments
→ potential action.

SOURCE FORMALISM:
Tool {
  name: string
  title?: string
  description?: string
  inputSchema: JSON Schema
  outputSchema?: JSON Schema
  annotations?: ToolAnnotations
}

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

TOOL_DESCRIPTION
≈ ACTION_AFFORDANCE_HINT

Tool selection becomes approximately:

SELECT(
  user_intent,
  {name_i, description_i, schema_i}
)

The operational vocabulary of the system therefore includes not only what the user says but what developers have said the system is capable of doing.

TENSION:
The MCP specification explicitly calls the description a “hint.” It is not a formal guarantee that the model will select the right tool.

MISSING:
Controlled evidence showing how changes in tool description wording alter tool-selection behavior while names, schemas, model, and task remain constant.

BOUNDARY:
A description does not itself execute a tool. It participates in the model-facing representation from which tool choice may be inferred.

CITATION TRAIL:
[[MJ-MARTINA-016]]
→ vocabulary controls generated representation
→ MCP Tool.description controls understanding of executable capabilities
→ descriptive vocabulary becomes an action-selection surface
→ forage tool descriptions as operative language.

TEST:
Create five tools with fixed implementations and schemas.

For each tool produce:
A. precise description
B. vague description
C. overlapping description
D. misleading description
E. no description

Run the same task corpus and measure:
tool selection accuracy,
unnecessary calls,
missed calls,
argument correctness.

Determine how much executable behavior changes from changing words alone.

PLATFORM:
Model Context Protocol; contemporary LLM agents

LINKS:
[[MJ-MARTINA-016]]
[[MJ-MARTINA-014-A-A]]

BIBTEX:
@misc{mcp2025schema,
  author = {{Model Context Protocol}},
  title = {Schema Reference},
  year = {2025},
  url = {https://modelcontextprotocol.io/specification/2025-06-18/schema}
}
