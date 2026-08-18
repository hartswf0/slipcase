ZETTEL

ID:
CALLSHOT-FIELD-013

TITLE:
THE SHOT IS NOT FULLY CALLED UNTIL FAILURE CAN BE SCORED.

SOURCE:
OpenAI API Reference — Graders / Evals, current documentation accessed 2026-08-17. SOURCE URL: https://platform.openai.com/docs/api-reference/graders

PASSAGE:
[PARAPHRASE]
OpenAI exposes graders including string checks, text similarity, model-based labels/scores, and multi-grader combinations.

RESEARCH OBJECT:
SPECIFICATION CAN BE EXPRESSED AFTER GENERATION AS AN EXECUTABLE CRITERION OF ACCEPTANCE.

LOCAL MOVE:
Prompt iteration becomes more durable when a failure is not only repaired in prose but converted into a test that can detect future regressions.

SOURCE TERMS:
“grader” · “string check” · “text similarity” · “label model” · “multi” · “passing”

WHAT BECAME STRANGE:
The most consequential prompt instruction may be the one compiled into a judge after the first failure.

QUESTION:
When is improving the test more effective than improving the prompt?

DEEPER QUESTION:
Does reliable natural-language programming require expressing intention twice: prospectively as instruction and retrospectively as executable acceptance?

MECHANISM:
TASK → OUTPUT → GRADER → PASS/FAIL → FAILURE ANALYSIS → PROMPT/TOOL/SCHEMA CHANGE → RERUN.

FORMAL SHIFT:
SPECIFICATION = PROMPT → SPECIFICATION = PROMPT + TEST SUITE.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI’s grader API includes deterministic comparisons, similarity metrics, model-based graders, and composed graders.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ACCEPT iff G_1(O,state) … G_n(O,state) satisfy threshold. FAILURE → NEW TEST → FUTURE INVARIANT.

TENSION:
An executable metric can stabilize the wrong target and create reliable optimization toward an impoverished proxy.

MISSING:
Tests for important qualities that humans can recognize before they can formalize them.

BOUNDARY:
Evals measure represented criteria only; passing does not imply global correctness.

CITATION TRAIL:
[[CALLSHOT-20260817-07]] → failure becomes test → [[CALLSHOT-FIELD-008]] invariants migrate out of prose.

TEST:
Take twenty historical prompt corrections. Compile every mechanically expressible one into graders, then test whether prompt length can shrink without losing reliability.

PLATFORM:
OpenAI Evals · graders · agent engineering

LINKS:
[[CALLSHOT-20260817-07]] [[CALLSHOT-FIELD-008]] [[CALLSHOT-FIELD-014]]

BIBTEX:
@misc{OpenAIGraders2026, author={{OpenAI}}, title={Graders API Reference}, year={2026}, url={https://platform.openai.com/docs/api-reference/graders}}
