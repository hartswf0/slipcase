ZETTEL

ID:
CALLSHOT-FIELD-007

TITLE:
TOOL DESCRIPTIONS ARE LANGUAGE INSIDE THE ACTION-SELECTOR.

SOURCE:
OpenAI API Reference — Responses custom function tools — current documentation accessed 2026-08-17. SOURCE URL: https://platform.openai.com/docs/api-reference/responses

PASSAGE:
[QUOTE]
“A description of the function. Used by the model to determine whether or not to call the function.”

RESEARCH OBJECT:
NATURAL-LANGUAGE DESCRIPTIONS OF TOOLS PARTICIPATE DIRECTLY IN WHICH EXTERNAL ACTION THE MODEL CHOOSES.

LOCAL MOVE:
In tool-using agents, an executable function is paired with a name, description, and JSON-schema parameter contract. The description is not only human-facing documentation; it is model-facing action-selection context.

SOURCE TERMS:
“function” · “description” · “determine whether or not to call” · “parameters” · “strict”

WHAT BECAME STRANGE:
Two identical executables can become different practical affordances if their linguistic descriptions differ.

QUESTION:
How much of an agent’s action repertoire is determined by executable code versus the words that make capabilities legible?

DEEPER QUESTION:
Are tool descriptions a form of operational semantics written in ordinary language?

MECHANISM:
CAPABILITY + NAME + DESCRIPTION + SCHEMA → MODEL TOOL SELECTION → ARGUMENTS → EXTERNAL EXECUTION.

FORMAL SHIFT:
WORDS DOCUMENT FUNCTIONS → WORDS PARTICIPATE IN FUNCTION DISPATCH.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI custom function tools include a model-facing natural-language description and a JSON-schema parameter definition.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
TOOL={name, description, input_contract, executable}; Δdescription can produce Δaction while executable is unchanged.

TENSION:
The executable constrains what can happen, but the description influences whether the model considers the action appropriate.

MISSING:
Controlled ablation evidence isolating tool description wording from tool names, schemas, and system instructions.

BOUNDARY:
The API documentation establishes intended use of descriptions, not a complete causal model of tool selection.

CITATION TRAIL:
[[CALLSHOT-20260817-01]] → tool description as dispatch language → links prompt craft to explicit action vocabulary.

TEST:
Expose functionally identical tools under systematically varied descriptions. Measure selection rate, wrong-tool rate, argument correctness, and unnecessary invocation.

PLATFORM:
OpenAI Responses API · function calling · agents

LINKS:
[[CALLSHOT-20260817-01]] [[CALLSHOT-FIELD-001]] [[CALLSHOT-FIELD-008]]

BIBTEX:
@misc{OpenAIFunctionTools2026, author={{OpenAI}}, title={Responses API Reference: Function tools}, year={2026}, url={https://platform.openai.com/docs/api-reference/responses}}
