ZETTEL

ID:
CALLSHOT-20260817-03

TITLE:
GIVE IT VERBS — tool schemas turn a language model from a speaker into a selector over typed external actions.

SOURCE:
OpenAI — “Function calling and other API updates” — June 13, 2023; current OpenAI API documentation on function tools.
https://openai.com/index/function-calling-and-other-api-updates/
https://platform.openai.com/docs/api-reference/responses

PASSAGE:
[PARAPHRASE]
Function calling lets developers describe functions and their argument schemas to a model. The model can select a function and generate structured arguments; tool controls can also require tool use or constrain the model to an allowed subset of tools. Execution of the external function remains an application-side operation.

RESEARCH OBJECT:
VERB-VOCABULARY-AS-ACTION-SPACE.

LOCAL MOVE:
[[MJ-GC-030-A]] followed SHRDLU into the hidden machinery between sentence and action.

Function calling gives that machinery a contemporary practical form.

To make an AI do something, developers frequently do not teach it arbitrary action.

They hand it a finite verb vocabulary:

SEARCH(...)
SEND_EMAIL(...)
CREATE_EVENT(...)
MOVE_OBJECT(...)
RUN_QUERY(...).

Natural language is interpreted relative to those available verbs.

SOURCE TERMS:
“functions”
“tools”
“arguments”
“JSON Schema”
“tool_choice”
“required”
“allowed tools”

WHAT BECAME STRANGE:
Agency can be added without changing the model’s vocabulary of ordinary language.

You change the verbs the environment exposes.

The effective ontology of action lives partly outside the model.

QUESTION:
Is the most important design decision in an agent the prompt, or the set of verbs it is permitted to invoke?

DEEPER QUESTION:
Does an AI’s practical world consist less of everything it can describe than of the operations its tool layer makes executable?

MECHANISM:
USER UTTERANCE
+
TOOL SET {
V₁(schema₁),
V₂(schema₂),
...
}
→ model chooses action
→ produces typed arguments
→ host executes external operation
→ result returns to model/environment.

FORMAL SHIFT:
FROM:
LANGUAGE MODEL
→ TEXT.

TO:
LANGUAGE MODEL
→ TYPED ACTION REQUEST
→ EXTERNAL STATE CHANGE.

SOURCE FORMALISM:
OpenAI function tools include a function name, description, and parameter schema. Tool-choice controls can permit automatic selection, require tool use, or constrain selection to allowed tools.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD OF POSSIBLE ACTIONS:

A = {verb₁, verb₂, ... verbₙ}.

Prompt interpretation becomes:

UTTERANCE
→ SELECT verb_i
→ BIND arguments
→ EXECUTE.

Changing A changes what “make AI do things” can mean.

TENSION:
The model proposes the call.

The host application performs the action.

Calling this “the model acted” hides an important delegation boundary.

MISSING:
A vocabulary for distinguishing:
MODEL DECISION,
TOOL REQUEST,
AUTHORIZATION,
EXECUTION,
OBSERVED CONSEQUENCE.

BOUNDARY:
Function calling does not itself execute arbitrary functions unless the surrounding application provides and runs them.

CITATION TRAIL:
[[MJ-GC-030-A]]
→ language interpreted against domain operations
→ function calling
→ action space represented as typed verbs
→ pragmatic prompt craft becomes VERB DESIGN.

TEST:
Build the same agent with:

A. one generic execute(command) tool;
B. five precise typed tools;
C. twenty narrow tools.

Hold model and user tasks constant.

Measure:
wrong-action rate,
argument errors,
ambiguity,
recoverability,
and unauthorized affordances.

PLATFORM:
Tool-calling language models / APIs

LINKS:
[[MJ-GC-030-A]]
[[MJ-GC-030-B-C]]
[[CALLSHOT-20260817-02]]

BIBTEX:
@misc{openai2023functioncalling,
  author={{OpenAI}},
  title={Function Calling and Other API Updates},
  year={2023},
  url={https://openai.com/index/function-calling-and-other-api-updates/}
}
