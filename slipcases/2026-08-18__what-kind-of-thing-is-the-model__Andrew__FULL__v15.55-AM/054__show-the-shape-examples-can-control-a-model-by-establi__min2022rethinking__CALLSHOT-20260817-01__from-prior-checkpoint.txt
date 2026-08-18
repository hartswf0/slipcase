ZETTEL

ID:
CALLSHOT-20260817-01

TITLE:
SHOW THE SHAPE — examples can control a model by establishing the answer-space and interaction form even when the demonstrated answers are wrong.

SOURCE:
Sewon Min et al. — “Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?” — 2022.
https://arxiv.org/abs/2202.12837

PASSAGE:
[PARAPHRASE]
Across the classification and multiple-choice tasks studied, replacing correct demonstration labels with random labels produced surprisingly small performance losses. The authors instead identify the demonstrated label space, input distribution, and overall input-output format as important contributors to in-context learning.

RESEARCH OBJECT:
EXAMPLE-AS-INTERFACE-SPECIFICATION.

LOCAL MOVE:
[[MJ-GC-007]] treated the visible prompt-output pair as a pedagogical unit.

[[MJ-GC-030-B-A]] treated natural language as a hypothesis that can be executed.

This source splits demonstration prompting into several operations.

An example may tell the model:

WHAT KIND OF THING COMES IN.

WHAT KIND OF THING MAY COME OUT.

WHAT THE TURN SHAPE LOOKS LIKE.

without primarily teaching the correct transformation between them.

The pragmatic operation is therefore:

DO NOT ONLY DESCRIBE THE TASK.

STAGE THE KIND OF EVENT YOU WANT THE MODEL TO CONTINUE.

SOURCE TERMS:
“demonstrations”
“label space”
“distribution of the input text”
“format”
“input-label mapping”
“in-context learning”

WHAT BECAME STRANGE:
An example can be operationally useful even when part of what it explicitly says is false.

That means demonstrations may function partly as theatrical blocking.

They place props onstage.
They assign roles.
They establish the rhythm of the exchange.

The model continues the scene.

QUESTION:
When practitioners say “give it examples,” which component are they actually controlling: semantics, output ontology, distribution, format, or all four?

DEEPER QUESTION:
Could prompt craft become more precise by decomposing examples into separate operations rather than treating “few-shot prompting” as one technique?

MECHANISM:
DEMONSTRATIONS
→ expose INPUT TYPE
→ expose OUTPUT SPACE
→ expose SERIALIZATION / TURN FORMAT
→ condition next generation.

Correct input-output correspondence may supply an additional signal but was not the dominant signal in the studied tasks.

FORMAL SHIFT:
FROM:
EXAMPLE = miniature correct lesson

TO:
EXAMPLE = temporary interface declaration.

SOURCE FORMALISM:
The paper separates four properties of demonstrations:

1. input-label mapping,
2. input-text distribution,
3. label space,
4. input-label pairing format.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXAMPLE
=
{
DOMAIN_HINT,
OUTPUT_VOCABULARY,
TURN_GRAMMAR,
MAPPING_HINT
}.

Practical operation:

SHOW(
  desired_input_shape,
  desired_output_shape,
  desired_interaction_shape
).

TENSION:
The striking random-label result concerns the tasks and models studied in this paper.

For many contemporary instruction-following, generative, reasoning, or exact-transformation tasks, demonstration correctness may matter substantially more.

MISSING:
A contemporary comparison across:
classification,
creative generation,
code transformation,
structured extraction,
agent action,
image prompting.

BOUNDARY:
Do not convert “ground-truth labels mattered little in these experiments” into “example correctness does not matter.”

CITATION TRAIL:
[[MJ-GC-007]]
→ prompt-output pair as learning object
→ Min et al.
→ demonstrations decompose into mapping, domain, label space, and format
→ practical prompt operation becomes SHOW THE SHAPE.

TEST:
Take one task and construct four prompt variants:

FORMAT ONLY
OUTPUT SPACE ONLY
DOMAIN EXAMPLES ONLY
CORRECT INPUT→OUTPUT EXAMPLES.

Measure which component actually changes performance.

PLATFORM:
Large language models / in-context learning

LINKS:
[[MJ-GC-007]]
[[MJ-GC-030-B-A]]

BIBTEX:
@article{min2022rethinking,
  title={Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?},
  author={Min, Sewon and Lyu, Xinxi and Holtzman, Ari and Artetxe, Mikel and Lewis, Mike and Hajishirzi, Hannaneh and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:2202.12837},
  year={2022},
  url={https://arxiv.org/abs/2202.12837}
}
