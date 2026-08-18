ZETTEL

ID:
MJ-GC-030-B-B

TITLE:
A semantics-preserving rewrite can change whether the program works: natural-language specifications can be evolved like compiler transformations.

SOURCE:
Amal Akli, Melissa Akli, Cedric Richter, Mike Papadakis, Yves Le Traon — “From Failing to Passing: Evolving Natural Language Prompt Optimization Rules for LLM Code Generation” — 2026.
URL: https://arxiv.org/abs/2607.05121

PASSAGE:
[PARAPHRASE]
Akli et al. keep code-generation models frozen and evolve rules that rewrite the natural-language problem statement instead. Candidate rules use an IF–THEN–EXCEPT structure and are constrained to restate, reorder, or make existing information explicit rather than introduce new task facts. Candidates are mutated and retained according to whether rewritten descriptions cause more generated programs to pass tests. The evolved rules can transfer to other code-generation models without re-optimization.

RESEARCH OBJECT:
SEMANTICS-PRESERVING-SPECIFICATION-COMPILATION.

LOCAL MOVE:
[[MJ-GC-030-B-A]] showed that a sentence can be an induced executable hypothesis.

This source goes one level higher.

The object being evolved is not the solution.

It is a RULE FOR CHANGING DESCRIPTIONS BEFORE THEY ARE EXECUTED.

The model weights remain frozen.

The intended task remains fixed.

The wording changes.

The generated program changes from failing to passing.

SOURCE TERMS:
“transformation rules”
“IF--THEN--EXCEPT”
“rule evolution”
“rewrite”
“problem statement”
“frozen”
“compiler optimization”
“transfer zero-shot”
“without modifying the underlying model”

WHAT BECAME STRANGE:
Two specifications intended to mean the same thing can have different computational consequences.

The failure can therefore reside neither in:

THE TASK

nor necessarily in:

THE GENERATED CODE.

It can reside in the REPRESENTATION OF THE TASK presented to the model.

This is a third repair layer:

repair the description.

QUESTION:
If a meaning-preserving rewrite changes whether the resulting code passes, where is the effective program: in the intended semantics or in the exact surface form of the specification?

DEEPER QUESTION:
Does natural-language programming collapse the traditional distinction between semantics and compiler behavior because representational form itself becomes causally active?

MECHANISM:
ORIGINAL SPECIFICATION p
→ frozen generator G
→ failing code.

Evolution loop:

RULE SET R
→ rewrite p as p'
→ same frozen G
→ code c'
→ execute tests
→ pass/fail fitness
→ mutate R.

Successful R survives.

At inference:

R(p)
→ reformulated specification
→ G
→ improved probability of passing code.

FORMAL SHIFT:
FROM:
PROGRAM REPAIR
= CHANGE PROGRAM

TO:
SPECIFICATION REPAIR
= CHANGE REPRESENTATION OF SAME INTENDED PROGRAM
→ regenerated implementation.

SOURCE FORMALISM:
Candidate transformation rules are short IF–THEN–EXCEPT rules.

The reported RuleEvol process includes:
reflection,
deletion,
merge,
gate evaluation,
and Pareto-based selection.

The generator remains frozen.

The authors explicitly compare the process to compiler optimization performed at the natural-language-description layer.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Intended semantics:

SEM(p) ≈ SEM(p').

Yet:

G(p) = failing program

G(p') = passing program.

Therefore for generative execution:

SEMANTIC_EQUIVALENCE(p,p')
does not imply
BEHAVIORAL_EQUIVALENCE(G,p,p').

Effective execution depends on:

MEANING
+ REPRESENTATIONAL FORM
+ INTERPRETER BIAS.

TENSION:
The paper constrains rewriting rules to preserve meaning, but semantic equivalence in unrestricted natural language is difficult to prove mechanically.

Some success could arise because a rewrite subtly changes interpretation rather than merely presentation.

MISSING:
A formal semantic representation against which the claimed meaning preservation of each rewrite can be independently verified.

BOUNDARY:
The reported results concern LLM code generation on LiveCodeBench and APPS.

They do not show that arbitrary natural-language programs can be repaired through surface rewriting.

CITATION TRAIL:
[[MJ-GC-030-B]]
→ descriptions themselves as operands
→ [[MJ-GC-030-B-A]]
→ descriptions as executable hypotheses
→ Akli et al. 2026
→ evolutionary search over rules for changing descriptions
→ model remains frozen while program correctness changes
→ representation itself becomes a repair surface.

TEST:
Take tasks with machine-checkable formal specifications.

Produce multiple natural-language formulations verified against the same formal semantics.

Run each through a frozen code-generation model with deterministic decoding.

Measure variance in program correctness.

Then evolve semantics-preserving rewrite rules.

If correctness changes while formal task semantics remain invariant, representational form has independent causal force.

PLATFORM:
LLM code generation / RuleEvol / DualFix

LINKS:
[[MJ-GC-030-B]]
[[MJ-GC-030-B-A]]

BIBTEX:
@article{akli2026failing,
  title={From Failing to Passing: Evolving Natural Language Prompt Optimization Rules for LLM Code Generation},
  author={Akli, Amal and Akli, Melissa and Richter, Cedric and Papadakis, Mike and Le Traon, Yves},
  journal={arXiv preprint arXiv:2607.05121},
  year={2026},
  url={https://arxiv.org/abs/2607.05121}
}
