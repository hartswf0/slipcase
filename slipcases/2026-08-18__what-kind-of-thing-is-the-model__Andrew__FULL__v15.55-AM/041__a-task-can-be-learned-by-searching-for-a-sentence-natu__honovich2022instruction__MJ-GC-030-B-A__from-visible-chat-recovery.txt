ZETTEL

ID:
MJ-GC-030-B-A

TITLE:
A task can be learned by searching for a sentence: natural language itself becomes the hypothesis space.

SOURCE:
Or Honovich, Uri Shaham, Samuel R. Bowman, Omer Levy — “Instruction Induction: From Few Examples to Natural Language Task Descriptions” — 2022.
URL: https://arxiv.org/abs/2205.10782

PASSAGE:
[PARAPHRASE]
Honovich et al. give language models input-output demonstrations and ask them to infer a natural-language instruction describing the underlying task. They evaluate the inferred instruction by executing it on further examples.

[QUOTE]
“one searches for the best description in the natural language hypothesis space.”

RESEARCH OBJECT:
NATURAL-LANGUAGE-AS-HYPOTHESIS-SPACE.

LOCAL MOVE:
[[MJ-GC-030-B]] followed Minsky and Papert from:

DESCRIPTION OF STATE

to:

DESCRIPTION OF TRANSFORMATION.

Instruction induction closes a loop that was only hypothetical there.

The system receives examples of a transformation.

It produces a DESCRIPTION of that transformation.

The description is then fed back to a language model and evaluated by whether it reproduces the transformation on new cases.

DESCRIPTION OF CHANGE
has become
EXECUTABLE HYPOTHESIS.

SOURCE TERMS:
“instruction induction”
“input-output demonstrations”
“underlying task”
“natural language instruction”
“executing”
“natural language hypothesis space”

WHAT BECAME STRANGE:
Learning can produce a sentence instead of a parameter update.

The thing learned is readable.

The learned hypothesis is also executable by another invocation of the model.

Natural language occupies three positions simultaneously:

DATA DESCRIPTION.
THEORY OF THE DATA.
PROGRAM FOR NEW DATA.

QUESTION:
When an induced sentence successfully generalizes a transformation, should it be understood as an explanation, a hypothesis, a program, or all three?

DEEPER QUESTION:
Could natural language become a genuinely recursive computational medium in which systems learn by synthesizing descriptions that are themselves executable by the same class of systems?

MECHANISM:
DEMONSTRATIONS:

(x₁ → y₁)
(x₂ → y₂)
...
(xₙ → yₙ)

→ MODEL INDUCTION

→ NATURAL-LANGUAGE INSTRUCTION I

→ execute I on new x*

→ predicted y*.

Performance of y*
evaluates I.

FORMAL SHIFT:
FROM:
EXAMPLES
→ latent parameter fitting
→ behavior

TO:
EXAMPLES
→ NATURAL-LANGUAGE DESCRIPTION
→ EXECUTION OF DESCRIPTION
→ behavior.

SOURCE FORMALISM:
The paper defines an instruction-induction task over 24 tasks and an evaluation metric based on executing the generated instruction.

The authors report substantially stronger instruction induction from InstructGPT than original GPT-3 and explicitly frame the result as search over a natural-language hypothesis space.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

D = {(x_i,y_i)}.

INDUCE(D)
→ sentence I.

EXECUTE(I,x)
→ y.

Score:

FIT(I,D_test).

Therefore:

I ∈ NATURAL_LANGUAGE

but functionally:

I : X → Y

when interpreted by model M.

The sentence becomes an operator only relative to an interpreter M.

TENSION:
The instruction is not executable by itself.

Its operational meaning depends on a second language-model invocation.

Natural language has therefore not become machine code.

It has become executable relative to a learned interpreter.

MISSING:
Whether two semantically different instructions that perform identically should be treated as the same learned program.

BOUNDARY:
The result concerns the paper's selected tasks and models.

It does not establish that arbitrary computational transformations can be induced as reliable natural-language instructions.

CITATION TRAIL:
[[MJ-GC-030-B]]
→ Minsky & Papert: describe the transformation between descriptions
→ Honovich et al. 2022
→ infer task description from examples
→ execute induced description
→ natural language becomes an explicit hypothesis space.

TEST:
Create an unknown transformation T and provide only demonstrations.

Induce ten different natural-language descriptions I₁…I₁₀.

Then test them on adversarial unseen inputs.

Separate:

TEXTUAL SIMILARITY
SEMANTIC SIMILARITY
EXECUTION EQUIVALENCE.

Ask whether two radically different descriptions can implement the same transformation and whether nearly identical descriptions can implement different ones.

PLATFORM:
Large language models / instruction induction

LINKS:
[[MJ-GC-030-B]]
[[MJ-GC-030-A]]

BIBTEX:
@article{honovich2022instruction,
  title={Instruction Induction: From Few Examples to Natural Language Task Descriptions},
  author={Honovich, Or and Shaham, Uri and Bowman, Samuel R. and Levy, Omer},
  journal={arXiv preprint arXiv:2205.10782},
  year={2022},
  url={https://arxiv.org/abs/2205.10782}
}
