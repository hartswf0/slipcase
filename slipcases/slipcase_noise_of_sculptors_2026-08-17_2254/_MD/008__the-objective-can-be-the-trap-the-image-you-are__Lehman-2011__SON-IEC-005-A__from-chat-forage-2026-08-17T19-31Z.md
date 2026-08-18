ZETTEL

ID:
SON-IEC-005-A

TITLE:
THE OBJECTIVE CAN BE THE TRAP: the image you are trying to reach can make its own stepping stones invisible.

SOURCE:
Joel Lehman & Kenneth O. Stanley — “Abandoning Objectives: Evolution Through the Search for Novelty Alone” — Evolutionary Computation 19(2), 2011, pp. 189–223.
SOURCE URL: https://doi.org/10.1162/EVCO_a_00025
FULL TEXT: https://gwern.net/doc/reinforcement-learning/exploration/2011-lehman.pdf

PASSAGE:
[QUOTE]
“Paradoxically, in these cases, pursuing the objective may prevent the objective from being reached.”

RESEARCH OBJECT:
DECEPTIVE OBJECTIVES.

The target itself can create a misleading gradient.

An intermediate state that is essential for reaching a desirable outcome may look worse according to every measure of resemblance to that outcome.

LOCAL MOVE:
[[SON-IEC-005]] reframed prompt craft from composition of a single prompt into iterative human-guided search.

Lehman and Stanley force the next move.

Iteration is not enough.

The criterion used to choose the next iteration determines which regions of possibility can ever be reached.

If every prompt revision is selected because its output looks MORE LIKE the image already imagined, then prompt craft may systematically destroy precisely the strange intermediate outputs from which genuinely novel solutions could emerge.

SOURCE TERMS:
objective
fitness
deception
local optimum
novelty
behavior space
stepping stone
archive

WHAT BECAME STRANGE:
The obviously rational prompting strategy—

KEEP WHATEVER LOOKS CLOSER TO THE IMAGE I WANT

—can be exactly the wrong algorithm.

A useful intermediate image may have to become:

less recognizable
less beautiful
less accurate
less semantically similar
less obviously relevant

before its descendants become dramatically better.

The shortest path through generative possibility need not monotonically resemble the destination.

QUESTION:
How often does goal-directed prompt iteration eliminate outputs that would have become productive stepping stones under further mutation?

DEEPER QUESTION:
What if expert prompt craft is not primarily the ability to describe a destination, but the ability to recognize valuable departures whose destination cannot yet be named?

MECHANISM:
Objective search assigns value according to proximity to a predefined goal.

In deceptive spaces:

candidate
→ appears closer to goal
→ receives higher fitness
→ reproduces
→ enters local optimum

while:

candidate
→ appears farther from goal
→ receives lower fitness
→ discarded

even when the discarded candidate lies on the only path to the superior solution.

Novelty search replaces goal proximity with behavioral difference from previously encountered solutions.

FORMAL SHIFT:
FROM:

prompt_t
→ candidates
→ choose candidate MOST LIKE TARGET
→ prompt_t+1

TO:

prompt_t
→ candidates
→ characterize DIFFERENCE
→ preserve unexplored behavior
→ branch
→ discover future target retroactively

The destination can become recognizable only after the path has produced it.

SOURCE FORMALISM:
[PARAPHRASE]

Novelty search replaces objective fitness with a novelty metric that rewards behaviors occupying sparsely visited regions of behavior space.

The source defines sparseness relative to nearest neighbors:

ρ(x) =
(1/k) Σ dist(x, μ_i)

where μ_i are nearest neighbors of x in the current population and archive.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

T = currently imagined target
I_t = generated image
D(I_t,T) = distance from target
N(I_t,A) = novelty relative to archive A

OBJECTIVE PROMPTING:

SELECT(I_t)
=
min D(I_t,T)

NOVELTY PROMPTING:

SELECT(I_t)
=
max N(I_t,A)

DECEPTIVE PROMPT SPACE exists when:

D(I_a,T) < D(I_b,T)

but descendants(I_b)

contain solutions superior to every reachable descendant of I_a.

TENSION:
Generative-image prompting is not an evolutionary optimization algorithm merely because users iterate.

The analogy becomes mechanically stronger only when candidate generation, selection, retention, and branching can be identified.

Furthermore, abandoning an objective does not mean behaving randomly.

Lehman and Stanley explicitly distinguish novelty search from random search.

MISSING:
Complete prompt genealogies rather than final prompts.

Cases where an apparently failed image later became an indispensable ancestor.

A behavioral characterization suitable for measuring novelty among generated images without simply substituting another hidden aesthetic objective.

Evidence comparing expert users who optimize resemblance with users who deliberately preserve strange deviations.

BOUNDARY:
Lehman and Stanley demonstrate deceptive objectives in evolutionary search domains including maze navigation and biped locomotion.

The existence and prevalence of equivalent deceptive landscapes in text-to-image prompting remain empirical questions.

FORMAL RESEMBLANCE is not genealogy.

CITATION TRAIL:
[[SON-IEC-005]]
→ prompt craft as iterative human evaluation
→ Lehman & Stanley
→ objective functions can suppress necessary stepping stones
→ target resemblance becomes a possible source of search failure
→ prompt expertise shifts from DESTINATION DESCRIPTION toward STEPPING-STONE RECOGNITION

TEST:
Construct a controlled image-generation study.

Give participants the same difficult target image and equal generation budgets.

CONDITION A — TARGET:
At every round, preserve candidates judged most similar to the target.

CONDITION B — NOVELTY:
At every round, preserve candidates judged most different from previously explored outputs while remaining minimally interesting.

CONDITION C — HYBRID:
Maintain separate branches for target similarity and novelty.

Record full ancestry.

At the end compare:

best target match
human preference
semantic diversity
number of distinct branches
distance trajectories
whether successful outputs descend through temporary decreases in target similarity

The decisive evidence is not whether novelty produces stranger pictures.

It is whether superior target-reaching lineages contain ancestors that objective selection would have killed.

PLATFORM:
Evolutionary Computation / MIT Press

LINKS:
[[SON-IEC-005]]

BIBTEX:
@article{lehman2011abandoning,
  author = {Joel Lehman and Kenneth O. Stanley},
  title = {Abandoning Objectives: Evolution Through the Search for Novelty Alone},
  journal = {Evolutionary Computation},
  volume = {19},
  number = {2},
  pages = {189--223},
  year = {2011},
  doi = {10.1162/EVCO_a_00025},
  url = {https://doi.org/10.1162/EVCO_a_00025}
}
