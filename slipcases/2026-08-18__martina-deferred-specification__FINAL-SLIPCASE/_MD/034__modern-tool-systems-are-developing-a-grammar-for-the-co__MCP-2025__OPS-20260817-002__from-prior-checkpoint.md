ZETTEL

ID:
OPS-20260817-002

TITLE:
Modern tool systems are developing a grammar for the consequences of verbs.

SOURCE:
Model Context Protocol — ToolAnnotations — 2025-06-18.
https://modelcontextprotocol.io/specification/2025-06-18/schema

PASSAGE:
[QUOTE]
“If true, the tool may perform destructive updates to its environment.”

RESEARCH OBJECT:
EFFECT ANNOTATIONS AS A PRAGMATICS OF MACHINE VERBS.

LOCAL MOVE:
[[MJ-MARTINA-012-A-A]] asked what actually chooses when the user delegates an unspecified decision. MCP adds another layer: operations can carry explicit metadata about the kind of consequences they may produce.

SOURCE TERMS:
“readOnlyHint”
“destructiveHint”
“idempotentHint”
“openWorldHint”
“ToolAnnotations”
“environment”

WHAT BECAME STRANGE:
The tool is no longer characterized only by WHAT it means.

It can also be marked by WHAT HAPPENS IF IT IS SAID AGAIN.

READ_ONLY
DESTRUCTIVE
IDEMPOTENT
OPEN_WORLD

These resemble grammatical properties of executable verbs.

QUESTION:
Are tool-effect annotations becoming an operational equivalent of grammatical aspect and modality for machine action?

DEEPER QUESTION:
What would a complete effect system for natural-language-controlled computation need to express beyond read-only, destructive, idempotent, and open-world?

MECHANISM:
MCP defines optional ToolAnnotations that provide hints about whether a tool modifies its environment, may be destructive, is idempotent, or interacts with an open world.

FORMAL SHIFT:
FROM:
VERB:
DELETE_FILE(path)

TO:
VERB:
DELETE_FILE(path)

EFFECTS:
{
  readOnly = false
  destructive = true
  idempotent = ?
  openWorld = false
}

SOURCE FORMALISM:
ToolAnnotations {
  title?: string
  readOnlyHint?: boolean
  destructiveHint?: boolean
  idempotentHint?: boolean
  openWorldHint?: boolean
}

The MCP specification also warns that these properties are hints and should not be trusted when supplied by untrusted servers.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ACTION =
NAME
+ ARGUMENT_TYPE
+ EFFECT_TYPE

Possible future effect vocabulary:

READ
WRITE
DELETE
SEND
PUBLISH
SPEND
COMMIT
IRREVERSIBLE
REPEAT_SAFE
EXTERNAL_WORLD
REQUIRES_CONSENT

TENSION:
The specification explicitly says annotations are only hints and may not faithfully describe actual behavior.

The grammar of consequence therefore exists without guaranteeing the truth of its own verbs.

MISSING:
A trustworthy mechanism binding declared effect annotations to the implementation that actually runs.

BOUNDARY:
ToolAnnotations describe expected effects; they do not enforce those effects.

CITATION TRAIL:
[[MJ-MARTINA-012-A-A]]
→ omitted decisions redistribute action
→ MCP marks action consequences explicitly
→ executable verbs acquire effect metadata
→ description of action separates from description of consequence
→ pursue machine pragmatics as effect typing.

TEST:
Take fifty agent tools from real MCP servers.

For each:
record declared annotations,
inspect implementation,
execute in a controlled sandbox,
record actual environmental effects.

Construct a confusion matrix between declared and observed:
READ_ONLY,
DESTRUCTIVE,
IDEMPOTENT,
OPEN_WORLD.

Then ask what additional effect categories are required to explain mismatches.

PLATFORM:
Model Context Protocol

LINKS:
[[MJ-MARTINA-012-A-A]]
[[MJ-MARTINA-015-A]]

BIBTEX:
@misc{mcp2025toolannotations,
  author = {{Model Context Protocol}},
  title = {Schema Reference: ToolAnnotations},
  year = {2025},
  url = {https://modelcontextprotocol.io/specification/2025-06-18/schema}
}
