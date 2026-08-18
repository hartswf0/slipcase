ZETTEL

ID:
LIT-AGRE-008

TITLE:
Deictic computation predates LLM prompting; the new question is where indexical binding is performed.

SOURCE:
Philip E. Agre and David Chapman — “Pengi: An Implementation of a Theory of Activity” — 1987 — Proceedings of AAAI-87, pp. 268–272.

PASSAGE:
[PARAPHRASE]
Agre and Chapman present Pengi as an implementation of a dynamic theory of everyday activity intended to produce complex, apparently planful behavior without explaining that organization through ordinary plan-following.

RESEARCH OBJECT:
Computational organization around ongoing situated activity rather than execution of a complete prior plan.

LOCAL MOVE:
Pengi turns philosophical dissatisfaction with plan-based action into an implemented AI architecture.

SOURCE TERMS:
activity
plan-following
dynamic
implementation
Pengi
apparently planful

WHAT BECAME STRANGE:
“Deixis may be closer to prompting than command” has a computational prehistory. Situated and indexical alternatives to plan execution were already being built inside AI in the 1980s.

QUESTION:
What changes when indexicality migrates from an internal representational strategy in a hand-built agent to ordinary user-facing language such as “this,” “there,” and “again”?

DEEPER QUESTION:
Does contemporary prompting externalize to the user a mode of situated control that earlier reactive systems implemented internally?

MECHANISM:
Ongoing environmental situation
→ locally relevant activity distinctions
→ action selected relative to current situation
→ environment changes
→ new situation.

FORMAL SHIFT:
<PRECOMPUTED PLAN>
→ <ONGOING SITUATION>
→ [LOCALLY COORDINATE ACTION]
→ <APPARENTLY PLANFUL ACTIVITY>

SOURCE FORMALISM:
Pengi is an implemented computational system; the paper’s contribution is architectural rather than a natural-language prompt syntax.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
“that one”
has operative value only if
INDEXICAL_BINDING(current_state, history)
can return an actionable referent.

TENSION:
Pengi does not show that natural-language prompts themselves are deictic programs. Its representational machinery and domain differ sharply from contemporary language models.

MISSING:
A direct technical genealogy linking Pengi-style indexical-functional representation to later multimodal conversational systems.

BOUNDARY:
Similarity of mechanism is not evidence of historical influence on modern prompting.

CITATION TRAIL:
Agre — Computation and Human Experience.
Agre & Chapman — “What Are Plans For?”
Suchman.
Brooks.
Ballard et al. — deictic codes.

TEST:
Compare a Pengi-style internal deictic variable with “that one” in a multimodal model. Locate exactly where referent binding occurs in each architecture and what state must persist.

PLATFORM:
[[DEICTIC PROMPTING]]

LINKS:
[[INDEXICAL COMPUTATION]]
[[SITUATED ACTION]]
[[COMMAND / DEIXIS]]

BIBTEX:
@inproceedings{agrechapman1987pengi,
  author = {Philip E. Agre and David Chapman},
  title = {Pengi: An Implementation of a Theory of Activity},
  booktitle = {Proceedings of the Sixth National Conference on Artificial Intelligence},
  pages = {268--272},
  year = {1987}
}