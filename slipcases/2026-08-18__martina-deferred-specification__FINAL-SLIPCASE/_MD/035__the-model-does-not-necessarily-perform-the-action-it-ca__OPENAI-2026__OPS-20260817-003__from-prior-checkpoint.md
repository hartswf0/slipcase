ZETTEL

ID:
OPS-20260817-003

TITLE:
The model does not necessarily perform the action it calls for.

SOURCE:
OpenAI Agents SDK — Tools — current documentation accessed August 17, 2026.
https://openai.github.io/openai-agents-python/tools/

PASSAGE:
[QUOTE]
“The model still decides when to call them, but your application or configured execution environment performs the actual work.”

RESEARCH OBJECT:
ACTION IS SPLIT BETWEEN SEMANTIC SELECTION AND EXECUTIVE AUTHORITY.

LOCAL MOVE:
[[MJ-MARTINA-015-A]] broke the analogy between human briefing and machine prompting. Current tool-calling architecture gives a more precise distinction.

The model can choose an operation.

Another system executes it.

SOURCE TERMS:
“local runtime tools”
“model”
“decides”
“call”
“application”
“execution environment”
“actual work”

WHAT BECAME STRANGE:
The apparently agentic sentence:

“Delete the file.”

can traverse several distinct authorities:

USER requests
MODEL proposes operation
RUNTIME authorizes
TOOL executes
WORLD changes.

No single utterance contains the whole action.

QUESTION:
Where exactly does agency reside in a tool-using language model system?

DEEPER QUESTION:
If the model selects an action but cannot itself authorize or execute it, is “the AI did X” an analytically misleading description of the event?

MECHANISM:
OpenAI distinguishes local/runtime tools from the model response itself. The model decides when to call a tool, while the application or configured environment performs the work.

FORMAL SHIFT:
FROM:
WORDS
→ AI ACTION

TO:
USER_UTTERANCE
→ MODEL_INFERENCE
→ TOOL_CALL_PROPOSAL
→ RUNTIME
→ TOOL_IMPLEMENTATION
→ WORLD_CHANGE.

SOURCE FORMALISM:
[PARAPHRASE]
The Agents SDK distinguishes hosted tools, local/runtime execution tools, function tools, and other callable capabilities. Local runtime tools execute outside the model response.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SELECT ≠ EXECUTE

MODEL_AUTHORITY:
choose / propose arguments

HOST_AUTHORITY:
expose / validate / approve / execute

TOOL_AUTHORITY:
perform implementation

ENVIRONMENT:
accept resulting state transition

TENSION:
Hosted tool configurations can collapse some of these boundaries because execution may occur in provider-managed environments.

MISSING:
A general vocabulary for attributing causal responsibility across request, selection, authorization, execution, and consequence.

BOUNDARY:
Tool calling does not mean the model independently possesses arbitrary operating-system or external-world authority.

CITATION TRAIL:
[[MJ-MARTINA-015-A]]
→ prompt/brief analogy breaks
→ current tool architecture separates decision from execution
→ “making AI do something” decomposes into multiple authorities
→ pursue the runtime as the hidden sovereign of prompting.

TEST:
Instrument a tool-using agent and record five timestamps for every consequential action:

REQUESTED
SELECTED
VALIDATED
EXECUTED
CONFIRMED

Then deliberately interrupt one stage at a time.

Determine which statements remain true:
“the user commanded it”
“the model chose it”
“the application allowed it”
“the tool did it.”

PLATFORM:
OpenAI Agents SDK; function calling; runtime tools

LINKS:
[[MJ-MARTINA-015-A]]
[[MJ-MARTINA-021-A-A]]

BIBTEX:
@misc{openai2026agentstools,
  author = {{OpenAI}},
  title = {OpenAI Agents SDK: Tools},
  year = {2026},
  url = {https://openai.github.io/openai-agents-python/tools/}
}
