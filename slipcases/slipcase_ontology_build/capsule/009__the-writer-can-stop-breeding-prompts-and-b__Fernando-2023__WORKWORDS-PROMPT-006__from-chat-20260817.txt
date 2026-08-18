ZETTEL

ID:
WORKWORDS-PROMPT-006

TITLE:
The writer can stop breeding prompts and begin breeding the prompts that breed prompts.

SOURCE:
Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, and Tim Rocktäschel — “Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution” — 2023 — arXiv:2309.16797

PASSAGE:
[PARAPHRASE] Promptbreeder maintains a population of task prompts, evaluates their fitness, and uses an LLM to mutate them. Crucially, the instructions that govern mutation are themselves prompts, and those “mutation-prompts” are also evolved.

RESEARCH OBJECT:
PROMPT PRACTICE BECOMES SELF-REFERENTIAL.

There are now at least two textual species:

prompts that perform the task

and

prompts that alter the prompts that perform the task.

The second species can itself change.

LOCAL MOVE:
Distant writing becomes evolutionary writing.

The author no longer needs to decide the final wording or even directly decide each revision.

They design:

population,
variation machinery,
selection environment,
fitness.

SOURCE TERMS:
Promptbreeder
task-prompts
mutation-prompts
population
fitness
evolution
self-referential improvement

WHAT BECAME STRANGE:
A prompt can be judged not by what it makes the model do, but by what kinds of other prompts it causes to come into existence.

Its output is a lineage of instructions.

QUESTION:
At what point does authorship migrate from sentence construction to selective environment construction?

DEEPER QUESTION:
If the mutation rule itself evolves, where is the stable program?

MECHANISM:
population of task prompts
→ evaluate fitness
→ mutation prompt instructs LLM to alter them
→ new task-prompt population
→ mutation prompts themselves mutate
→ selection
→ repeat.

FORMAL SHIFT:
FROM:

AUTHOR
→ PROMPT
→ OUTPUT

TO:

AUTHOR
→ EVOLUTIONARY CONDITIONS
→ MUTATION PROMPTS
→ TASK PROMPTS
→ OUTPUTS
→ FITNESS
→ NEW CONDITIONS.

SOURCE FORMALISM:
Promptbreeder evolves a population of task prompts according to task fitness while simultaneously evolving the mutation prompts used to generate variations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Task prompt population:

P_t.

Mutation-prompt population:

M_t.

Generation:

P_(t+1) = mutate(P_t | M_t).

Meta-generation:

M_(t+1) = mutate(M_t | ...).

Selection evaluates descendants under fitness F.

The operational unit is therefore no longer a prompt.

It is a reproducing prompt ecology.

TENSION:
Evolutionary improvement sounds autonomous, but the fitness function remains an enormous site of authorship.

What looks like surrendering textual control may actually relocate control into evaluation.

The author stops choosing sentences and starts choosing survival.

MISSING:
A cultural or literary account of:

prompt ancestry,
mutation,
selection,
extinction,
convergence,
speciation,
and inherited fragments.

BOUNDARY:
Promptbreeder optimizes benchmark performance. Evolution toward metric fitness is not equivalent to artistic, epistemic, or cultural improvement.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B-1]]
→ prompts can be rewritten before execution
→ Promptbreeder
→ rewriting mechanism becomes prompt-governed
→ mutation instruction itself evolves
→ next edge: genetic programming, evolutionary art, cultural evolution, and authorship through selection.

TEST:
Archive every task prompt and mutation prompt from an evolutionary run.

Construct its genealogy.

Track which phrases survive, disappear, recombine, or repeatedly re-emerge.

Then ask whether successful linguistic fragments behave more like:

ideas,
genes,
macros,
incantations,
or local adaptations to one model.

PLATFORM:
LLM-driven evolutionary prompt optimization.

LINKS:
[[DEFAULT-IMAGES-CHI26-B-1]]

BIBTEX:
@article{Fernando2023Promptbreeder,
  author = {Fernando, Chrisantha and Banarse, Dylan and Michalewski, Henryk and Osindero, Simon and Rockt{\"a}schel, Tim},
  title = {Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution},
  year = {2023},
  url = {https://arxiv.org/abs/2309.16797}
}
