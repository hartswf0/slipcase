ZETTEL

ID:
SHOT-20260817-08

TITLE:
2026-08-17 — Treat the first prompt as evidence of requirements, not as the finished program.

SOURCE:
Junjie Shi, Weisong Sun, Zhenpeng Chen, Zhujun Wu, Xiaohong Chen, Zhi Jin, Yang Liu — “REprompt: Prompt Generation for Intelligent Software Development Guided by Requirements Engineering” — arXiv:2601.16507 — submitted 2026-01-23 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2601.16507

PASSAGE:
[QUOTE]
“prompts in software development can be viewed as a form of software requirements.”

RESEARCH OBJECT:
PROMPT AS PROVISIONAL REQUIREMENT.

LOCAL MOVE:
[[MJ-2022-002]] began with the patent attorney's unexpected transfer:

“facility with describing a thing”
became useful for generative AI.

[[MJ-2022-010]] later speculated that prompt craft might disappear once models understood ordinary language well enough.

REprompt opens a stranger possibility.

The user's initial natural language does not have to become more like code.

It can remain incomplete because the system treats it as the beginning of requirements work.

The machine does not merely execute the sentence.

It interrogates the sentence until a more executable specification exists.

SOURCE TERMS:
“requirements”
“elicitation”
“analysis”
“specification”
“validation”
“dependency-aware”
“interview”

WHAT BECAME STRANGE:
“Vague prompt” may be the wrong diagnosis.

A vague request can be perfectly adequate as:

INPUT TO SPECIFICATION DISCOVERY.

The failure occurs only when the system treats raw requirements as finished requirements.

QUESTION:
When should an agent execute immediately, and when should it enter requirements-discovery mode?

DEEPER QUESTION:
Is the operative unit of natural-language programming the requirements conversation rather than the prompt?

MECHANISM:
User states desired consequence.

System extracts explicit requirements.

System detects unresolved requirements.

System elicits missing information or resolves discoverable facts.

System analyzes dependencies.

System constructs executable specification.

Specification is validated.

Execution begins.

FORMAL SHIFT:
UTTERANCE₀
→ EXECUTION

becomes

UTTERANCE₀
→ REQUIREMENTS
→ ELICITATION
→ SPECIFICATION
→ VALIDATION
→ EXECUTION

SOURCE FORMALISM:
[PARAPHRASE]

REprompt explicitly maps requirements-engineering stages including elicitation, analysis, specification, and validation into prompt refinement for software-development tasks.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

FIRST PROMPT
=
PROVISIONAL REQUIREMENTS

not

FINAL PROGRAM TEXT.

This pairs directly with [[SHOT-20260817-05]]:

requirements can remain linguistic until a bounded deterministic region becomes ready for compilation.

TENSION:
More elicitation can recover missing intent.

More elicitation can also become obstruction.

[[SHOT-20260817-01]] says to default toward action when action is clearly requested.

Therefore requirements discovery should not become an excuse for refusing to operate when missing facts can instead be observed with tools.

MISSING:
A decision rule distinguishing:

ASK USER
LOOK IT UP
INFER SAFELY
USE DEFAULT
LEAVE UNRESOLVED
BLOCK EXECUTION.

BOUNDARY:
REprompt concerns software development.

The general theory of provisional requirements is broader than the source.

CITATION TRAIL:
[[MJ-2022-002]]
→ specification skill migrates into prompting
→ [[MJ-2022-010]]
→ natural language improves
→ REprompt 2026
→ first utterance becomes requirements evidence
→ [[SHOT-20260817-01]]
→ execute rather than endlessly discuss
→ [[SHOT-20260817-05]]
→ compile only when formalization becomes useful

TEST:
On 2026-08-17, collect terse real-world build requests.

For each request construct:

EXPLICIT
INFERRED
UNKNOWN
DEFAULTED
DISCOVERABLE
BLOCKING.

Generate once directly from the raw request.

Generate again after requirements compilation.

Ask the original requester to identify:

which inferred requirements were correct
which were invented
which questions were unnecessary
which missing constraints caused real failures.

PLATFORM:
Vibe coding
Software agents
Requirements engineering
Natural-language programming

LINKS:
[[MJ-2022-002]]
[[MJ-2022-010]]
[[SHOT-20260817-01]]
[[SHOT-20260817-05]]
[[SHOT-20260817-09]]

BIBTEX:
@misc{shi2026reprompt,
  title={REprompt: Prompt Generation for Intelligent Software Development Guided by Requirements Engineering},
  author={Shi, Junjie and Sun, Weisong and Chen, Zhenpeng and Wu, Zhujun and Chen, Xiaohong and Jin, Zhi and Liu, Yang},
  year={2026},
  eprint={2601.16507},
  archivePrefix={arXiv}
}
