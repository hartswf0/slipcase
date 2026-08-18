ZETTEL

ID:
CALLSHOT-FIELD-014

TITLE:
NATURAL LANGUAGE CAN SPECIFY THE CONTROL POLICY FOR A TEMPORARY PROGRAM THE MODEL WRITES TO OPERATE TOOLS.

SOURCE:
OpenAI API, “Model guidance” for GPT-5.6 — Programmatic Tool Calling, current documentation accessed 2026-08-17. SOURCE URL: https://developers.openai.com/api/docs/guides/latest-model

PASSAGE:
[PARAPHRASE]
GPT-5.6 Programmatic Tool Calling can write JavaScript to call eligible tools, pass results between calls, and process intermediate outputs in a hosted runtime.

RESEARCH OBJECT:
PROMPTING CAN MOVE ONE LEVEL UP: FROM ASKING FOR AN ACTION TO DESCRIBING AN ORCHESTRATION POLICY THAT SYNTHESIZES A TEMPORARY PROGRAM.

LOCAL MOVE:
Current guidance frames Programmatic Tool Calling as suitable for bounded, tool-heavy stages that do not require fresh model judgment between every step.

SOURCE TERMS:
“Programmatic Tool Calling” · “JavaScript” · “eligible tools” · “bounded” · “intermediate outputs” · “hosted runtime”

WHAT BECAME STRANGE:
The prompt can describe a small operating policy—allowed tools, retries, stopping, output contract—while the actual control flow is synthesized after the request.

QUESTION:
Which programming control structures can be safely deferred into operational prose?

DEEPER QUESTION:
Where is the boundary between useful deferred formalization and accidentally reinventing an inferior programming language in natural language?

MECHANISM:
OPERATIONAL POLICY → MODEL SYNTHESIZES PROGRAM π → π CALLS TOOLS / REDUCES RESULTS → MODEL RESUMES JUDGMENT.

FORMAL SHIFT:
PROMPT → TOOL CALL becomes PROMPT → TEMPORARY PROGRAM → TOOL GRAPH → STATE → MODEL.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI describes Programmatic Tool Calling as model-written JavaScript for bounded, tool-heavy workflows, with explicit guidance to retain fresh semantic judgment where needed.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ORCHESTRATION_SPEC={stage, tools, parallelism, retries, stop, schema, handoff}; MODEL(spec)→π; π executes under capabilities.

TENSION:
The farther execution moves into synthesized orchestration, the less the literal user utterance resembles the actual program that ran.

MISSING:
Comparative evidence showing when prose-defined orchestration is clearer and safer than handwritten deterministic code.

BOUNDARY:
The pattern is intentionally bounded; it is not recommended for every multi-tool workflow.

CITATION TRAIL:
[[CALLSHOT-20260817-08]] → programmatic tool calling → joins tool descriptions, authorization, schemas, and evals into one operational stack.

TEST:
Implement the same workflow as ordinary tool calls, programmatic tool calling, handwritten orchestration code, and a reusable skill. Compare correctness, traceability, modification cost, and failure modes.

PLATFORM:
OpenAI GPT-5.6 · Programmatic Tool Calling · orchestration

LINKS:
[[CALLSHOT-20260817-08]] [[CALLSHOT-FIELD-007]] [[CALLSHOT-FIELD-008]] [[CALLSHOT-FIELD-011]] [[CALLSHOT-FIELD-013]]

BIBTEX:
@misc{OpenAIModelGuidancePTC2026, author={{OpenAI}}, title={Model guidance: Programmatic Tool Calling}, year={2026}, url={https://developers.openai.com/api/docs/guides/latest-model}}
