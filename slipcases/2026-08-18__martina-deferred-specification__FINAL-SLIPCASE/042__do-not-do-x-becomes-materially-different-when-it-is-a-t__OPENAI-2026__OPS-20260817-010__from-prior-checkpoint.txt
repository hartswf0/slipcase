ZETTEL

ID:
OPS-20260817-010

TITLE:
“Do not do X” becomes materially different when it is a tripwire instead of advice.

SOURCE:
OpenAI Agents SDK — Guardrails — current documentation accessed August 17, 2026.
https://openai.github.io/openai-agents-python/guardrails/

PASSAGE:
[PARAPHRASE]
Tool input guardrails can run before execution and can skip a call, replace its output, or trigger an exception that halts execution.

RESEARCH OBJECT:
NORMATIVE LANGUAGE CAN MIGRATE FROM INSTRUCTION INTO EXECUTABLE VETO.

LOCAL MOVE:
[[OPS-20260817-004]] moved mandatory positive behavior from prose into `tool_choice`.

Guardrails reveal the negative counterpart.

Instead of:

“Never execute this operation under condition C.”

one can install machinery capable of preventing execution when C is detected.

SOURCE TERMS:
“guardrails”
“validation”
“before execution”
“skip”
“tripwire”
“halt”
“tool guardrails”

WHAT BECAME STRANGE:
There is a categorical difference between:

PROHIBITION AS SENTENCE

and:

PROHIBITION AS INTERRUPTION.

The first requests obedience.

The second changes what transitions the system permits.

QUESTION:
Which safety and behavioral rules should be expressed as prompt instructions and which should become executable vetoes?

DEEPER QUESTION:
Does a mature language-to-action system require a distinction analogous to constitutional law versus police power: rules that describe what should happen versus mechanisms that can stop what happens?

MECHANISM:
The Agents SDK supports tool guardrails around function-tool calls. Input guardrails run before tool execution and can prevent or alter execution behavior; tripwires can raise exceptions and halt an agent run.

FORMAL SHIFT:
FROM:
PROMPT:
“Do not perform forbidden action.”

TO:
candidate_action
→ VALIDATE
→ {
    PASS → EXECUTE
    FAIL → BLOCK
  }

SOURCE FORMALISM:
Tool guardrail lifecycle:

MODEL proposes call
→ input tool guardrail
→ execute or block
→ tool output
→ output tool guardrail.

Tripwire:
validation result
→ exception
→ halt.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

NORM
= predicate P(action, context)

ENFORCEMENT:

if P == false:
    transition → DENIED
else:
    transition → EXECUTE

The important shift is:

“SHOULD NOT”
→
“CANNOT PASS THIS GATE.”

TENSION:
Guardrails themselves may use fallible models or imperfect validators. Runtime enforcement is stronger than prompting only to the extent that the predicate is correctly specified and reliably evaluated.

MISSING:
A systematic method for deciding which natural-language invariants are compilable into deterministic or independently evaluated guardrails.

BOUNDARY:
Not every ethical, contextual, or interpretive rule can be reduced to a simple executable predicate.

CITATION TRAIL:
[[OPS-20260817-004]]
→ positive requirement leaves prompt via tool_choice
→ guardrails move negative requirement into runtime
→ imperative and prohibition acquire enforcement machinery
→ prompt practice becomes institutional architecture.

TEST:
Take a production agent prompt and extract every sentence containing:
never,
must not,
only if,
requires approval,
do not.

For each rule construct two versions:

A. instruction-only
B. runtime guardrail

Generate adversarial and ordinary task cases.

Measure:
violation rate,
false blocks,
latency,
recovery behavior.

Retain prose only where executable enforcement proves impossible or undesirable.

PLATFORM:
OpenAI Agents SDK; agent guardrails

LINKS:
[[OPS-20260817-004]]
[[MJ-MARTINA-014-A-A]]
[[MJ-MARTINA-015-A]]

BIBTEX:
@misc{openai2026guardrails,
  author = {{OpenAI}},
  title = {OpenAI Agents SDK: Guardrails},
  year = {2026},
  url = {https://openai.github.io/openai-agents-python/guardrails/}
}
