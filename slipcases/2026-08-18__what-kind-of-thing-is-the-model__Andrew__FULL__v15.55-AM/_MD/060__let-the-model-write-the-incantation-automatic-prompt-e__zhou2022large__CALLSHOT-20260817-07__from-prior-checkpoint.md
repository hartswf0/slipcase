ZETTEL

ID:
CALLSHOT-20260817-07

TITLE:
LET THE MODEL WRITE THE INCANTATION — automatic prompt engineering treats instructions as programs and searches over them.

SOURCE:
Yongchao Zhou et al. — “Large Language Models Are Human-Level Prompt Engineers” — 2022.
https://arxiv.org/abs/2211.01910

PASSAGE:
[PARAPHRASE]
Automatic Prompt Engineer generates candidate natural-language instructions with an LLM, evaluates those instructions by using another model to execute them, and selects instructions according to a score. The authors explicitly treat the instruction as the “program.”

RESEARCH OBJECT:
PROMPT-AS-SEARCHABLE-PROGRAM.

LOCAL MOVE:
[[MJ-GC-030-B-A]] showed that examples can induce a natural-language description of a task.

APE adds selection pressure.

Do not ask:

WHAT IS THE RIGHT PROMPT?

Generate a population of possible prompts.

Execute them.

Keep the ones whose consequences best satisfy the metric.

SOURCE TERMS:
“instruction”
“program”
“automatic instruction generation”
“selection”
“instruction candidates”
“score function”

WHAT BECAME STRANGE:
Prompt writing becomes empirical search over sentences.

A sentence’s value is not determined by whether it sounds precise to a human.

Its value is determined by what happens when the interpreter runs it.

QUESTION:
How different are prompts selected for behavioral performance from prompts humans judge semantically clearest?

DEEPER QUESTION:
Does executable natural language acquire a distinction analogous to extensional versus intensional equivalence: sentences that mean different things to us but cause the machine to behave similarly, and vice versa?

MECHANISM:
TASK EXAMPLES / OBJECTIVE
→ generate instruction candidates I₁…Iₙ
→ execute each instruction
→ score consequences
→ select I*.

FORMAL SHIFT:
FROM:
WRITE PROMPT.

TO:
SEARCH(PROMPT SPACE)
UNDER
BEHAVIORAL FITNESS.

SOURCE FORMALISM:
APE treats candidate instructions as programs and evaluates them through zero-shot execution by an LLM against a chosen score.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

FITNESS(I)
=
SCORE(
EXECUTE(M, I, TASKS)
).

Prompt engineering becomes:

argmax_I FITNESS(I).

TENSION:
A high-scoring instruction may exploit idiosyncrasies of the particular model or evaluation set rather than express a generally portable task specification.

MISSING:
A measure of PROMPT PORTABILITY across:
models,
versions,
contexts,
languages,
and tool environments.

BOUNDARY:
APE’s evidence concerns its evaluated NLP tasks and models; it does not establish universal parity with skilled human prompt design.

CITATION TRAIL:
[[MJ-GC-030-B-A]]
→ instruction induced from examples
→ APE
→ instructions generated as candidates
→ execution supplies fitness
→ prompting becomes program search.

TEST:
Generate 100 candidate instructions for one task.

Rank independently by:

HUMAN CLARITY
MODEL PERFORMANCE
CROSS-MODEL TRANSFER.

Inspect prompts where these rankings strongly disagree.

PLATFORM:
Large language models / Automatic Prompt Engineer

LINKS:
[[MJ-GC-030-B-A]]
[[MJ-GC-030-B-B]]
[[CALLSHOT-20260817-06]]

BIBTEX:
@article{zhou2022large,
  title={Large Language Models Are Human-Level Prompt Engineers},
  author={Zhou, Yongchao and Muresanu, Andrei Ioan and Han, Ziwen and Paster, Keiran and Pitis, Silviu and Chan, Harris and Ba, Jimmy},
  journal={arXiv preprint arXiv:2211.01910},
  year={2022},
  url={https://arxiv.org/abs/2211.01910}
}
