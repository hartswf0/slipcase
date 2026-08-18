ZETTEL

ID:
RETENTION-005-Q-B

TITLE:
A negative prompt does not simply subtract a forbidden object; its effect depends on when and how guidance enters the diffusion trajectory.

SOURCE:
Yutong Ban et al. — “Understanding the Impact of Negative Prompts” — 2024.

PASSAGE:
[PARAPHRASE]
The study reports time-dependent negative-prompt effects and a reverse-activation phenomenon in which applying negative guidance too early can help induce the object later suppressed.

RESEARCH OBJECT:
NEGATION IN LANGUAGE DOES NOT MAP TO LOGICAL NEGATION IN THE GENERATOR.

LOCAL MOVE:
Replace branch-pruning-as-set-subtraction with dynamic guidance over a trajectory.

SOURCE TERMS:
negative prompt
reverse activation
critical step
diffusion
noise
removal
guidance

WHAT BECAME STRANGE:
“No glasses” may require the forbidden concept to become internally active before it disappears externally.

QUESTION:
What does it mean to call a prompt a refusal when the mechanism can transiently construct what it refuses?

DEEPER QUESTION:
Can absence in a final representation have a positive causal history that provenance ought to preserve?

MECHANISM:
negative concept n → encoded guidance → early dynamics can induce n-related structure → later counteracting guidance → final absence.

FORMAL SHIFT:
<NEGATION = DELETE POSSIBILITY> → <NEGATION = DYNAMIC COUNTER-TRAJECTORY>

SOURCE FORMALISM:
The paper studies positive and negative noise predictions across diffusion timesteps.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
z_{t+1}=F(z_t,g_positive,g_negative,t), with negative effect changing over t.

TENSION:
Mechanism is architecture/setting-specific, not universal to all negative prompting.

MISSING:
Whether ordinary interfaces can expose timing of negative guidance artistically.

BOUNDARY:
Negative prompts are soft architecture-dependent interventions, not declarative logical prohibitions.

CITATION TRAIL:
[[RETENTION-005-Q]] → branch pruning → technical dynamics → reverse activation → absence has hidden trajectory.

TEST:
Apply same negative concept early-only, middle-only, late-only, and throughout; save intermediate states and trace feature emergence/disappearance.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-Q]]
[[reverse-activation]]
[[negative-guidance]]
[[absence-has-history]]

BIBTEX:
NONE
