ZETTEL

ID:
ENCOUNTER-OP-030

TITLE:
Joint attention to a shared object can be more diagnostic than attention to the artificial partner.

SOURCE:
Giulia Perugia, Maike Paetzel-Prüsmann, Madelene Alanenpää, and Ginevra Castellano — “I Can See It in Your Eyes: Gaze as an Implicit Cue of Uncanniness and Task Performance in Repeated Interactions With Robots” — 2021 — Frontiers in Robotics and AI 8:645956. ([frontiersin.org](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.645956/full))

PASSAGE:
[PARAPHRASE] During the joint task, attention to the shared screen predicted involvement and task performance better than gaze toward the robot; more gaze at the robot predicted poorer task performance. ([frontiersin.org](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.645956/full))

RESEARCH OBJECT:
Encounter may be triadic rather than dyadic: HUMAN ↔ SHARED WORLD ↔ AI.

LOCAL MOVE:
The study separates social chat from joint activity and discovers that the meaning of the same cue changes with interactional context.

SOURCE TERMS:
shared attention
mutual gaze
joint task
engagement
task performance
object of shared attention
object of exclusive attention

WHAT BECAME STRANGE:
Looking at the artificial partner can become evidence of worse coordination precisely when both participants should be oriented toward a shared task object.

QUESTION:
What is the textual/generative equivalent of joint attention to a shared object?

DEEPER QUESTION:
Are the strongest AI encounters actually encounters around a third thing rather than encounters with AI itself?

MECHANISM:
human and artificial partner
→ coordinate attention on common object
→ act upon common task state
→ contributions become mutually relevant through that object
→ joint progress becomes observable.

FORMAL SHIFT:
<HUMAN ↔ AI>
→ <HUMAN ↔ SHARED OBJECT ↔ AI>
→ [JOINT MODIFICATION / REFERENCE]
→ <COORDINATED ACTIVITY>

SOURCE FORMALISM:
The study operationalizes attentional focus as percentage of gaze directed toward:
ROBOT,
SHARED SCREEN,
EXCLUSIVE TABLET,
OTHER,
and relates these measures to reported involvement and task performance. ([frontiersin.org](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.645956/full))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For generative AI, replace gaze with referential/action focus:

SHARED_OBJECT ∈ {
  document,
  codebase,
  image,
  design,
  argument map,
  simulation,
  physical task state
}

SHARED_OBJECT_UPTAKE =
fraction of turns that correctly reference or transform the current common object state.

TENSION:
Conversational interfaces encourage attention toward the apparent interlocutor. Productive encounter may instead require the AI itself to recede as both participants orient toward the work.

MISSING:
A reliable way to distinguish shared-object attention from mere lexical repetition of object descriptions.

BOUNDARY:
The HRI result concerns gaze allocation in one embodied collaborative game. It does not establish a universal superiority of object-oriented over partner-oriented attention.

CITATION TRAIL:
[[ENCOUNTER-AI-013]]
[[ENCOUNTER-AI-016]]
→ Perugia et al. 2021
→ joint attention
→ shared artifacts
→ co-creative object trajectories.

TEST:
Create matched AI tasks with:
A. ephemeral chat only,
B. persistent visible shared artifact.
Measure reference accuracy, repair, artifact improvement, turn efficiency, and post-task conceptual change. Test whether encounter signatures concentrate around the shared artifact rather than social-language intensity.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-013]]
[[ENCOUNTER-AI-016]]
[[Shared Object]]
[[Triadic Encounter]]

BIBTEX:
@article{PerugiaEtAl2021Eyes,
  author = {Giulia Perugia and Maike Paetzel-Pr{\"u}smann and Madelene Alanenp{\"a}{\"a} and Ginevra Castellano},
  title = {I Can See It in Your Eyes: Gaze as an Implicit Cue of Uncanniness and Task Performance in Repeated Interactions With Robots},
  journal = {Frontiers in Robotics and AI},
  year = {2021},
  volume = {8},
  pages = {645956},
  doi = {10.3389/frobt.2021.645956}
}