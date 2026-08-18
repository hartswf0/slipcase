ZETTEL

ID:
SHOT-20260817-07

TITLE:
2026-08-17 — A failure can become one new sentence in the program that governs the next attempt.

SOURCE:
Zehua Pei, Hui-Ling Zhen, Shixiong Kai, Sinno Jialin Pan, Yunhe Wang, Mingxuan Yuan, Bei Yu — “SCOPE: Prompt Evolution for Enhancing Agent Effectiveness” — arXiv:2512.15374v2 — version dated 2026-05-28 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2512.15374

PASSAGE:
[QUOTE]
“we treat the agent’s prompt as an evolvable parameter”

RESEARCH OBJECT:
FAILURE AS SPECIFICATION DELTA.

LOCAL MOVE:
[[MJ-2022-004]] already contained the seed:

change one thing
rerun
observe.

[[MJ-2022-005]] sharpened that into bounded empirical knowledge.

[[MJ-2022-009]] then warned that prompt knowledge itself can decay as models change.

SCOPE introduces a different relationship between execution and instruction:

the trace produced by execution can become material from which the next prompt is rewritten.

Failure does not merely produce a second attempt.

Failure can author a rule.

SOURCE TERMS:
“execution trace”
“learning signal”
“guideline”
“prompt evolution”
“tactical memory”
“strategic memory”

WHAT BECAME STRANGE:
The program's consequences can write the language that governs the program.

The direction:

PROMPT
→ BEHAVIOR

becomes recursive:

PROMPT
→ BEHAVIOR
→ CORRECTION
→ PROMPT.

QUESTION:
Which observed failures deserve promotion into durable prompt rules?

DEEPER QUESTION:
Could the real specification of an agent be the genealogy of failures from which its present instructions were accumulated?

MECHANISM:
Prompt θₜ governs execution.

Execution emits trace τₜ.

Trace contains error or inefficiency.

System derives guideline gₜ.

Guideline is classified, consolidated, or rejected.

Prompt changes.

Next execution occurs under θₜ₊₁.

FORMAL SHIFT:
PROMPT
→ FAILURE
→ RETRY

becomes

PROMPTₜ
→ TRACEₜ
→ RULEₜ
→ PROMPTₜ₊₁
→ TRACEₜ₊₁

SOURCE FORMALISM:
The paper represents prompt evolution as:

θₜ₊₁ = θₜ ⊕ gₜ

where a newly synthesized guideline modifies the current prompt.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

FAILURE
→ SPECIFICATION DELTA

But every delta needs a scope:

TURN
TASK
PROJECT
TOOL
AGENT
GLOBAL.

This directly reconnects to [[SHOT-20260817-02]].

TENSION:
[[MJ-2022-009]] says prompt rules can expire.

SCOPE-like accumulation risks producing:

prompt fossils
contradictions
overfitting
rule bloat.

A living prompt therefore needs both:

MEMORY
and
FORGETTING.

MISSING:
A provenance-preserving prompt architecture where every instruction can answer:

What failure created me?
When?
On which model?
For which operation?
Am I still reproducible?

BOUNDARY:
SCOPE is a research system evaluated on agent tasks.

The proposed genealogical prompt repository is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[MJ-2022-004]]
→ empirical prompt testing
→ [[MJ-2022-005]]
→ bounded operational knowledge
→ [[MJ-2022-009]]
→ prompt-rule decay
→ SCOPE 2026
→ execution trace creates guideline
→ [[SHOT-20260817-02]]
→ guideline requires scope
→ prompt becomes corrigible program history

TEST:
Beginning 2026-08-17, maintain an agent prompt where no new operational instruction may be added without:

originating trace
date
model/version
failure description
scope
reproduction test.

Periodically rerun the originating test.

If the failure no longer reproduces, mark the rule for deletion.

Compare with an ordinary static prompt accumulated through undocumented edits.

PLATFORM:
LLM agents
Coding agents
Deep-research agents
Prompt evolution

LINKS:
[[MJ-2022-004]]
[[MJ-2022-005]]
[[MJ-2022-009]]
[[SHOT-20260817-02]]
[[SHOT-20260817-06]]
[[SHOT-20260817-09]]

BIBTEX:
@misc{pei2026scope,
  title={SCOPE: Prompt Evolution for Enhancing Agent Effectiveness},
  author={Pei, Zehua and Zhen, Hui-Ling and Kai, Shixiong and Pan, Sinno Jialin and Wang, Yunhe and Yuan, Mingxuan and Yu, Bei},
  year={2026},
  eprint={2512.15374},
  archivePrefix={arXiv}
}
