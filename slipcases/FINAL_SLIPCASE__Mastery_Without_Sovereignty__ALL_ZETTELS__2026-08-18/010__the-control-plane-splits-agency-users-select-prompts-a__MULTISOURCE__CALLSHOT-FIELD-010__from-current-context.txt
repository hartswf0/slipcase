ZETTEL

ID:
CALLSHOT-FIELD-010

TITLE:
THE CONTROL PLANE SPLITS AGENCY: USERS SELECT PROMPTS, APPLICATIONS SUPPLY RESOURCES, MODELS SELECT TOOLS.

SOURCE:
Model Context Protocol Specification, server overview / prompts / resources / tools, revisions 2025-06-18 and 2025-11-25. SOURCE URL: https://modelcontextprotocol.io/specification/2025-06-18/server/index

PASSAGE:
[QUOTE]
“Prompts” — “User-controlled”
“Resources” — “Application-controlled”
“Tools” — “Model-controlled”

RESEARCH OBJECT:
THE PRACTICAL PROGRAM OF AN AGENTIC INTERACTION IS DISTRIBUTED ACROSS MULTIPLE CONTROL REGIMES.

LOCAL MOVE:
MCP explicitly distinguishes who controls three primitives. A user can provide the same words and inhabit a different practical world because the application attaches different resources or exposes different tools.

SOURCE TERMS:
“Prompts” · “Resources” · “Tools” · “User-controlled” · “Application-controlled” · “Model-controlled”

WHAT BECAME STRANGE:
The user’s utterance no longer owns the whole causal chain. Intention, context, capability, model selection, and permissions can have different authors.

QUESTION:
Where is intention located when multiple actors control different parts of the action topology?

DEEPER QUESTION:
Should agent prompting be modeled as temporary allocation of powers rather than a command from one speaker to one machine?

MECHANISM:
USER PROMPT + APP CONTEXT + SERVER CAPABILITIES + MODEL TOOL SELECTION + PERMISSIONS → ACTION.

FORMAL SHIFT:
USER PROMPT → MODEL ACTION becomes CONTROL TOPOLOGY → ACTION.

SOURCE FORMALISM:
[PARAPHRASE]
MCP distinguishes prompts as user-controlled templates, resources as application-controlled context, and tools as model-controlled executable functions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ACTION=F(USER_INTENT, PROMPT, APP_CONTEXT, EXPOSED_TOOLS, MODEL_SELECTION, PERMISSIONS, TOOL_RESULT).

TENSION:
Distributed control improves modularity but multiplies plausible failure origins and complicates responsibility.

MISSING:
A standard action-provenance record spanning all contributing control layers.

BOUNDARY:
MCP standardizes interfaces but host applications can implement control and confirmation differently.

CITATION TRAIL:
[[CALLSHOT-20260817-05]] → MCP control hierarchy → prompt is only one node in the operative system.

TEST:
Perturb one layer at a time while holding the user request fixed: prompt template, resource set, tool description, available tool set, permission rule. Measure action changes.

PLATFORM:
Model Context Protocol · agent infrastructure

LINKS:
[[CALLSHOT-20260817-05]] [[CALLSHOT-FIELD-007]] [[CALLSHOT-FIELD-009]] [[CALLSHOT-FIELD-011]]

BIBTEX:
@misc{MCP2025, author={{Model Context Protocol}}, title={Server Features Overview}, year={2025}, url={https://modelcontextprotocol.io/specification/2025-06-18/server/index}}
