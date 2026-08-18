ZETTEL

ID:
LIT-BROOKS-010

TITLE:
“The prompt leans on a world” splits into two architectures: representing the world and remaining coupled to it.

SOURCE:
Rodney A. Brooks — “Intelligence without representation” — 1991 — Artificial Intelligence 47, pp. 139–159, especially pp. 139, 146ff.

PASSAGE:
[PARAPHRASE]
Brooks argues for systems whose activity-producing layers connect perception directly to action rather than depending on a central world representation. His robots continuously match behavior to the actual environment; coherent behavior can emerge from interacting layers without a central representation of either world or intention.

RESEARCH OBJECT:
Ongoing world coupling as an alternative to representing context.

LOCAL MOVE:
Brooks changes the role of the environment from something primarily modeled inside the system to something repeatedly consulted through perception and action.

SOURCE TERMS:
real world
perception
action
activity producers
layers
world as its own model
central representation

WHAT BECAME STRANGE:
“Give the model more context” may be the wrong remedy when the missing resource is continued access to the world rather than a richer textual representation of it.

QUESTION:
When prompting succeeds because a system can inspect files, images, interfaces, sensors, tools, or live state, should that still be called “context”?

DEEPER QUESTION:
Does tool-using multimodal AI mark a shift from ever-larger representations toward partial environmental coupling?

MECHANISM:
Perception of present environment
→ locally active behavior
→ action
→ environment changes
→ renewed perception.

FORMAL SHIFT:
<WORLD REPRESENTATION AS CENTRAL MODEL>
→ <ONGOING PERCEPTION–ACTION COUPLING>
→ [ACT / RESENSE]
→ <ADAPTIVE BEHAVIOR>

SOURCE FORMALISM:
A layered behavior architecture in which independent activity-producing layers connect perception to action and can suppress or interact with other layers.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
STATIC PROMPTING:
WORLD → REPRESENTATION → MODEL → OUTPUT

COUPLED AGENT:
WORLD ↔ PERCEIVE → ACT ↔ WORLD

TENSION:
Contemporary LLM agents still rely heavily on representations: tokens, embeddings, images, tool outputs, summaries. Brooks’s stronger anti-representational claim therefore cannot simply be transferred.

MISSING:
A vocabulary for degrees and kinds of coupling rather than a binary representation/no-representation distinction.

BOUNDARY:
Brooks’s robots are not language models, and his architecture does not establish that linguistic prompting is embodied or situated merely because tools are available.

CITATION TRAIL:
Situated robotics.
Agre & Chapman.
Suchman.
Gibson.
Embodied interaction.

TEST:
Give two systems the same initial textual description of a changing environment. Allow only one to re-perceive the environment between actions. Identify which apparent “understanding” depends on representation and which on continued coupling.

PLATFORM:
[[PROMPT LEANS ON A WORLD]]

LINKS:
[[WORLD AS ITS OWN MODEL]]
[[CONTEXT / COUPLING]]
[[REPRESENTATION IS NOT SITUATION]]

BIBTEX:
@article{brooks1991intelligence,
  author = {Rodney A. Brooks},
  title = {Intelligence without Representation},
  journal = {Artificial Intelligence},
  volume = {47},
  number = {1--3},
  pages = {139--159},
  year = {1991}
}