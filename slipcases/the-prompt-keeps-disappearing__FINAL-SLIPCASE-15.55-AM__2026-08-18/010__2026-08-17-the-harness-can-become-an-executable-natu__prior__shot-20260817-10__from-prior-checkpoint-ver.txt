ZETTEL

ID:
SHOT-20260817-10

TITLE:
2026-08-17 — The harness can become an executable natural-language object.

SOURCE:
Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng — “Natural-Language Agent Harnesses” — arXiv:2603.25723v2 — version dated 2026-05-18 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2603.25723

PASSAGE:
[QUOTE]
“express harness behavior in editable natural language”

RESEARCH OBJECT:
NATURAL LANGUAGE AS PORTABLE CONTROL LOGIC.

LOCAL MOVE:
[[SHOT-20260817-02]] distributed prompt policy across tools and scopes.

[[SHOT-20260817-05]] showed natural language compiling deterministic subregions into temporary programs.

Natural-Language Agent Harnesses pushes in the opposite direction as well: high-level controller behavior usually buried in runtime code can be externalized into editable natural language and executed by a shared runtime.

The language/code traffic is therefore bidirectional.

SOURCE TERMS:
“agent harness”
“editable natural language”
“portable executable artifact”
“explicit contracts”
“durable artifacts”
“runtime”

WHAT BECAME STRANGE:
The same system can move procedure from language into code when determinism is useful and move control logic from code back into language when inspectability and portability are useful.

QUESTION:
What makes natural-language control logic executable rather than merely advisory?

DEEPER QUESTION:
If a harness can be represented as editable language, is the program now the prompt, the runtime, the contract between them, or the entire coupled object?

MECHANISM:
Control logic is written in natural language.

A runtime interprets that control logic under explicit contracts.

The runtime exposes tools, state, and durable artifacts.

The same language-level harness can be transferred across tasks or runtime adapters.

FORMAL SHIFT:
CONTROLLER CODE
→ EXECUTION

becomes

NATURAL-LANGUAGE HARNESS
+
RUNTIME CONTRACT
→ EXECUTION

SOURCE FORMALISM:
[PARAPHRASE]

Pan et al. introduce Natural-Language Agent Harnesses and an Intelligent Harness Runtime that executes them through explicit contracts, durable artifacts, and lightweight adapters.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXECUTABLE LANGUAGE
=
NATURAL-LANGUAGE CONTROL LOGIC
+
DEFINED RUNTIME
+
TOOL CONTRACTS
+
STATE SEMANTICS.

The words alone are not executable.

Execution belongs to the relation between words and runtime.

TENSION:
[[SHOT-20260817-05]] formalizes language into code for predictable control flow.

This source textualizes controller code into natural language for portability and inspection.

Neither direction wins.

The boundary itself becomes movable.

MISSING:
A criterion for deciding which control decisions should remain textual and which should be compiled into conventional code.

BOUNDARY:
The source studies a specific harness representation and runtime. It does not establish that arbitrary natural-language instructions constitute executable harnesses.

CITATION TRAIL:
[[SHOT-20260817-02]]
→ distributed control policy
→ [[SHOT-20260817-05]]
→ language compiles temporary code
→ Pan et al. 2026
→ controller code can migrate back into editable natural language
→ executable meaning depends on a runtime contract

TEST:
Take the same agent workflow and implement its high-level controller twice:

CODE HARNESS
and
NATURAL-LANGUAGE HARNESS.

Hold model, tools, tasks, and evaluation constant.

Measure:
behavioral equivalence
portability
human inspectability
edit cost
runtime failures
ability to localize a behavioral change.

PLATFORM:
LLM agents
Agent harnesses
Coding agents
Computer-use agents

LINKS:
[[SHOT-20260817-02]]
[[SHOT-20260817-05]]
[[SHOT-20260817-07]]

BIBTEX:
@misc{pan2026nlah,
  title={Natural-Language Agent Harnesses},
  author={Pan, Linyue and Zou, Lexiao and Guo, Shuo and Ni, Jingchen and Zheng, Hai-Tao},
  year={2026},
  eprint={2603.25723},
  archivePrefix={arXiv}
}
