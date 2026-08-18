ZETTEL

ID:
SON-IEC-005-C

TITLE:
OPEN-ENDEDNESS MAY REQUIRE FORGETTING: one remembered step helped VLM explorers; more memory sometimes made them collapse into themselves.

SOURCE:
Sam Earle, Kai Arulkumaran, Andrew Dai, Akarsh Kumar, Julian Togelius & Sebastian Risi — “In Search of the Ingredients of Open-Endedness: Replicating Picbreeder with Large Vision-Language Models” — GECCO 2026.
SOURCE URL: https://arxiv.org/abs/2605.23908
DOI: https://doi.org/10.1145/3795095.3805186

PASSAGE:
[QUOTE]
The authors conclude that “a little context goes a long way.”

[PARAPHRASE]
With no history, agents repeatedly published duplicates. A one-step context performed strongly on semantic recall. Increasing context did not monotonically improve performance and sometimes reduced recall and diversity; the authors hypothesize information overload and self-reinforcing loops.

RESEARCH OBJECT:
CREATIVE MEMORY has a dosage.

More remembered history is not automatically more exploratory intelligence.

LOCAL MOVE:
[[SON-IEC-005]] asked where expertise lives in an iterative search procedure.

[[SON-IEC-005-A]] showed that objectives can trap search.

Earle et al. perform an unusually direct experiment: replace Picbreeder’s human selectors with vision-language models and manipulate how much recent history they can see.

The resulting failure is not simply amnesia.

Too little memory produces repetition.

Too much memory can produce another kind of repetition: the system begins recursively reinforcing its own previous preferences.

SOURCE TERMS:
open-endedness
context length
history
exploration
semantic recall
visual coverage
semantic coverage
phylogenetic tree
mode collapse
agents

WHAT BECAME STRANGE:
Remembering can prevent repetition.

Remembering more can create repetition.

The second repetition is stranger because it may look like refinement.

The paper reports longer-context agents repeatedly producing highly refined motifs, including recurring top-down soda-can forms in one condition.

The system can therefore mistake increasingly coherent self-consistency for continued exploration.

QUESTION:
Is forgetting an active ingredient of generative creativity rather than merely a limitation of memory?

DEEPER QUESTION:
How much history should an artificial creative agent retain before memory changes from a map of explored territory into an attractor that keeps returning the agent to its own prior tastes?

MECHANISM:
The experiment varies Context Length CL.

CL = 0:
current population only
→ poor protection against repeating prior choices
→ duplicate publication

CL = 1:
current + immediately previous interaction
→ enough history to notice immediate repetition
→ strong Semantic Recall in the reported sweep

larger CL:
more previous interaction exposed simultaneously
→ no monotonic improvement
→ some conditions show lower recall/diversity and messier or repetitive motifs

The authors suggest information overload and, for some longer contexts, possible self-reinforcing “auto-sycophantic” dynamics.

FORMAL SHIFT:
FROM:

MORE MEMORY
→ BETTER SEARCH

TO:

TOO LITTLE MEMORY
→ FORGET WHERE YOU HAVE BEEN
→ repetition

ENOUGH MEMORY
→ recognize recent repetition
→ divergence

TOO MUCH MEMORY
→ repeatedly condition on your own prior choices
→ preference reinforcement
→ attractor

SOURCE FORMALISM:
[PARAPHRASE]

The study defines Context Length CL as the number of previous interaction steps supplied to each VLM agent.

Experiments compare CL values including:

0
1
2
10
20/full

and evaluate generated archives using Semantic Recall, Visual Coverage, Semantic Coverage, and phylogenetic Tree Balance.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

M_t = retained creative history
π = selection policy
A_t = candidate archive

π(candidate | A_t, M_t)

When |M_t| ≈ 0:

LOCAL_REPEAT ↑

When |M_t| is sufficient:

RECENT_REPEAT_DETECTION ↑

But beyond some system-dependent threshold:

SELF_CONDITIONING ↑
ATTRACTOR_STRENGTH ↑
OPEN_ENDEDNESS may ↓

Creative memory therefore may require:

REMEMBER ENOUGH TO KNOW WHERE YOU WERE
+
FORGET ENOUGH TO STOP BEING WHO YOU WERE.

TENSION:
The experiment does not establish a universal optimum at CL=1.

Different metrics respond differently, full-history runs also gained diversity under an additional novelty-oriented instruction, and context length is only a crude proxy for human memory.

Human remembering is selective, reconstructive, lossy, embodied, and distributed across time.

A token window is not human memory.

MISSING:
Experiments with selective rather than contiguous memory.

Memory of:

only failures
only distant ancestors
only surprising transitions
only semantic summaries
random prior states
contradictory preferences

Comparison with human participants under controlled memory aids.

Whether the harmful variable is amount of history, repetitive wording, self-generated justification, attention dilution, or reinforcement of explicit identity/preferences.

BOUNDARY:
The result concerns specific VLM-driven Picbreeder experiments in a constrained evolutionary image system.

It does not establish that longer context generally reduces creativity in language models.

The important finding is non-monotonicity, not “short context is always better.”

CITATION TRAIL:
[[SON-IEC-005]]
→ search policy rather than final prompt
→ [[SON-IEC-005-A]]
→ exploration requires resisting deceptive attraction
→ VLM Picbreeder replication
→ memory prevents one attractor while creating another
→ creative intelligence may require engineered forgetting

TEST:
Run identical generative-search agents under six memory policies:

A. NONE
B. LAST TURN
C. FULL HISTORY
D. RANDOM SAMPLE OF HISTORY
E. NOVELTY-ONLY MEMORY
F. COMPRESSED CONTRADICTION MEMORY

Hold model, generation budget, candidate space, and selection instructions constant.

Measure:

duplicate rate
semantic coverage
visual coverage
branch depth
branch balance
return-to-prior-motif frequency
human interestingness

Then inspect whether selective forgetting outperforms both amnesia and total recall.

PLATFORM:
arXiv / GECCO 2026

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-A]]
[[SON-IEC-005-B]]

BIBTEX:
@misc{earle2026picbreeder,
  author = {Sam Earle and Kai Arulkumaran and Andrew Dai and Akarsh Kumar and Julian Togelius and Sebastian Risi},
  title = {In Search of the Ingredients of Open-Endedness: Replicating Picbreeder with Large Vision-Language Models},
  year = {2026},
  eprint = {2605.23908},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi = {10.1145/3795095.3805186},
  url = {https://arxiv.org/abs/2605.23908}
}
