ZETTEL

ID: CALVINO-016

TITLE:
An admissible event sequence still needs an explanation for why its characters act.

SOURCE:
Mark O. Riedl and R. Michael Young — "Narrative Planning: Balancing Plot and Character" — Journal of Artificial Intelligence Research 39 (2010), pp. 217–267.

PASSAGE:
[PARAPHRASE]
The authors develop a narrative planner that searches for causally coherent action sequences while also representing goals that explain characters' participation in those sequences.

RESEARCH OBJECT:
A distinction between causal validity and perceived character intentionality.

LOCAL MOVE:
The paper treats narrative generation as a planning problem in which actions must contribute both to plot progression and to intelligible character behavior.

SOURCE TERMS:
"narrative planning";
"character intentionality";
"causal links";
"Intent-based Partial Order Causal Link."

WHAT BECAME STRANGE:
Calvino's basic anticombinatorial problem asks whether actions can coexist. A stronger narrative problem asks why those actions belong to this story, performed by these characters.

QUESTION:
Can a narrative satisfy every logical compatibility constraint while remaining unintelligible as character-driven fiction?

DEEPER QUESTION:
What is the smallest representation that distinguishes an admissible sequence of events from a motivated narrative?

MECHANISM:
A planning system links actions through preconditions and effects while associating character actions with explanatory goals.

FORMAL SHIFT:
Initial world state
→ candidate actions
→ [causal and intentional planning]
→ coherent action sequence with goal explanations.

SOURCE FORMALISM:
Intent-based Partial Order Causal Link planning, abbreviated IPOCL.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For each narrative action a:

1. Its required preconditions must hold.
2. Its effects must update the world consistently.
3. A relevant character goal should explain its performance.

Logical validity alone checks only part of the problem.

TENSION:
An intentionally motivated character can still participate in an aesthetically unsuccessful story. Conversely, literature can deliberately present unexplained or contradictory motives.

MISSING:
A general account of how genre, unreliable narration, thematic ambiguity, and literary surprise modify the desirability of explicit intention.

BOUNDARY:
IPOCL is one approach to narrative planning. It is not a universal model of literary creativity or a direct continuation of Calvino's experiment.

CITATION TRAIL:
Riedl and Young (2010).
Meehan (1977).
Dehn (1981).
Calvino's subjective narrative constraints, as documented by Braffort.

TEST:
Generate narratives with identical event inventories but different planning conditions: causal-only, causal-plus-intentional, and intentional with permitted ambiguity. Compare consistency and reader interpretations of character motives.

PLATFORM:
[[Causal and Intentional Narrative Generation]]

LINKS:
[[CALVINO-003]]
[[CALVINO-005]]
[[CALVINO-008]]
[[CALVINO-010]]

BIBTEX:
@article{riedl2010narrative,
  author  = {Riedl, Mark O. and Young, R. Michael},
  title   = {Narrative Planning: Balancing Plot and Character},
  journal = {Journal of Artificial Intelligence Research},
  volume  = {39},
  pages   = {217--267},
  year    = {2010},
  doi     = {10.1613/JAIR.2989},
  url     = {https://faculty.cc.gatech.edu/~riedl/pubs/jair.pdf}
}
