ZETTEL

ID:
SON-IEC-005

TITLE:
“Trial and error is the teacher” has a technical ancestor: interactive evolutionary computation makes subjective human judgment the fitness function.

SOURCE:
Hideyuki Takagi — “Interactive Evolutionary Computation: Fusion of the Capabilities of EC Optimization and Human Evaluation” — Proceedings of the IEEE 89(9), 2001, pp. 1275–1296. URL: https://ieeexplore.ieee.org/document/949485/

PASSAGE:
[QUOTE]
Takagi defines IEC as evolutionary computation that “optimizes systems based on subjective human evaluation.”

RESEARCH OBJECT:
PROMPT CRAFT can be modeled as HUMAN-IN-THE-LOOP SEARCH even when the user cannot articulate a formal objective function.

LOCAL MOVE:
The parent describes:

Joseph generating more than 10,000 images around a discovered “magical prompt,”
Ignite maintaining protocols for randomized generation,
Oscar repeatedly testing model biases,
Shambibble performing rigorous empirical prompt experiments.

Later it states:

“If the prompt-craft channel is the school, trial and error is the teacher.”

Takagi supplies an older computational category for precisely the strange case where the machine can generate alternatives but the human supplies a fitness judgment that is difficult to formalize.

SOURCE TERMS:
interactive evolutionary computation
optimization
subjective human evaluation
fitness
search
user preference

WHAT BECAME STRANGE:
The prompt may not be the primary unit of craft.

The ITERATION LOOP may be.

A skilled user might outperform a novice not because they possess a superior sentence but because they have developed a superior method for:

generating variation
noticing differences
selecting promising outputs
constructing the next variation
remembering the search trajectory

QUESTION:
Is prompt craft better understood as linguistic composition or as interactive optimization over an opaque generative system?

DEEPER QUESTION:
What knowledge resides in the prompt itself, and what knowledge exists only in the user's iterative selection procedure?

MECHANISM:
Interactive evolutionary computation addresses problems where a useful objective depends on human subjective evaluation rather than a computable fitness function.

A system generates candidates.

A human evaluates them.

That evaluation changes subsequent search.

FORMAL SHIFT:
FROM:

PROMPT
→ IMAGE

TO:

PROMPT_t
→ GENERATE
→ CANDIDATES_t
→ HUMAN EVALUATION
→ SELECT / MODIFY
→ PROMPT_t+1
→ GENERATE
→ ...

SOURCE FORMALISM:
[PARAPHRASE]

IEC combines evolutionary-computation search with human evaluation where system quality depends on subjective properties difficult to encode as ordinary objective functions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

state_t =
{
prompt_t,
outputs_t,
user_memory_t
}

outputs_t = MODEL(prompt_t, randomness_t)

evaluation_t = HUMAN(outputs_t)

prompt_(t+1) =
VARIATE(prompt_t, evaluation_t, user_memory_t)

CRAFT =
quality of the entire iterative policy,
not merely quality of prompt_t.

TENSION:
Midjourney prompting is not literally an evolutionary algorithm merely because users iterate.

Many users alter prompts without explicit populations, mutation operators, recombination, or algorithmic selection.

The relationship may therefore be FORMAL RESEMBLANCE rather than historical genealogy.

That distinction must remain open.

MISSING:
Detailed prompt histories from expert users.

Evidence of how users decide what to preserve, mutate, discard, or recombine.

Whether expert prompting can be predicted better by final-prompt features or by properties of the preceding search trajectory.

BOUNDARY:
IEC provides a formal ancestor for subjective interactive search.

It does not establish that Midjourney users consciously adopted evolutionary computation or that their practices instantiate every component of an evolutionary algorithm.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ 10,000-image magical-prompt exploration
→ randomized prompt protocols
→ “trial and error is the teacher”
→ Takagi 2001
→ human subjective evaluation as optimization signal
→ prompt craft becomes ITERATIVE SEARCH POLICY

TEST:
Record complete generation histories from expert and novice prompt users.

For each transition classify:

KEEP
DELETE
MUTATE
RECOMBINE
RANDOMIZE
RETURN
BRANCH

Then compare final-output quality under two conditions:

A. give a new user only the expert’s final prompt
B. give the new user the expert’s search procedure but not the final prompt

If B preserves more expertise than A, craft resides substantially in the search policy rather than the prompt artifact.

PLATFORM:
Proceedings of the IEEE

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]
[[SON-CONTROL-003]]

BIBTEX:
@article{takagi2001interactive,
  author = {Hideyuki Takagi},
  title = {Interactive Evolutionary Computation: Fusion of the Capabilities of EC Optimization and Human Evaluation},
  journal = {Proceedings of the IEEE},
  volume = {89},
  number = {9},
  pages = {1275--1296},
  year = {2001},
  doi = {10.1109/5.949485},
  url = {https://ieeexplore.ieee.org/document/949485/}
}
