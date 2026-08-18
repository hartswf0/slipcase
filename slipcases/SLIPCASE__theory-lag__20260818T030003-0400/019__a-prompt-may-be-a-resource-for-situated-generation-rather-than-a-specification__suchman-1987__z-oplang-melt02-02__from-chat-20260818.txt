ZETTEL

ID:
Z-OPLANG-MELT02-02

TITLE:
A prompt may be a resource for situated generation rather than a specification of a future artifact.

SOURCE:
Lucy Suchman — Plans and Situated Actions: The Problem of Human-Machine Communication — 1987 — p. 52.

SOURCE URL:
https://books.google.com/books/about/Plans_and_Situated_Actions.html?id=AJ_eBJtHxmsC

PASSAGE:
[QUOTE]
“plans are resources for situated action but do not in any strong sense determine its course.”

RESEARCH OBJECT:
<PROMPT-AS-RESOURCE>.

The prompt may function less like a compressed future artifact and more like a resource consulted while a trajectory is being locally produced.

LOCAL MOVE:
Suchman attacks a planning model in which an abstract representation determines the detailed course of practical action.

A plan is useful precisely without containing the concrete circumstances through which action will unfold.

SOURCE TERMS:
“plan”
“resource”
“situated action”
“course”
“embodied practices”
“changing circumstances”
“representation”

WHAT BECAME STRANGE:
Our existing field still gives the prompt too much sovereignty.

Even when we say:

<partial specification>
→ <model completion>
→ <realization>,

we imagine that the prompt stands before the action and somehow governs what follows.

Suchman suggests another topology:

<prompt>
does not contain a deficient version of the action.

It may be one resource among others recruited while the next move is locally produced.

QUESTION:
What if a prompt does not partially specify a future artifact at all, but furnishes a resource through which the next situated move becomes possible?

DEEPER QUESTION:
Does “specification completion” mistakenly assume that somewhere there exists a specification waiting to become complete?

MECHANISM:
<representation>
provides orientation.

<local situation>
contains contingencies not represented in advance.

<actor/interpreter>
[uses]
{
  representation,
  current circumstances,
  available resources,
  emerging consequences
}

to produce:

<next action>.

The trajectory is constructed recursively rather than unfolded from the plan.

FORMAL SHIFT:
<PROMPT AS INCOMPLETE SPECIFICATION>
→ [COMPLETE]
→ <EXECUTION>

becomes:

<PROMPT AS RESOURCE>
+
<CURRENT SITUATION>
→ [LOCAL INTERPRETATION]
→ <NEXT MOVE>
→ <NEW SITUATION>

SOURCE FORMALISM:
Suchman’s claim is conceptual rather than computational:

plans can represent action while failing to determine its concrete course.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

At time t:

a_t = f(P, S_t, R_t)

where:

P = relatively persistent prompt/plan,
S_t = presently available situation,
R_t = other usable resources,
a_t = locally produced action.

Then:

S_(t+1) = transition(S_t, a_t).

P need never encode the entire path.

TENSION:
Suchman’s argument concerns human situated action.

An autoregressive model is not situated in the human ethnomethodological sense merely because it possesses a context window.

Treating token context as equivalent to lived situation would erase the very distinction Suchman is trying to preserve.

MISSING:
What counts as <situation> for a generative model?

Possible candidates differ radically:

- token context,
- conversation history,
- tool state,
- selected artifacts,
- environment state,
- user judgment,
- institutional setting,
- the user’s embodied circumstances.

The field currently calls too many of these things “context.”

BOUNDARY:
Suchman does not provide a theory of prompts.

The useful pressure is negative:

we cannot assume that because an expression precedes action, it contains a partial determination of that action.

CITATION TRAIL:
Suchman — Human-Machine Reconfigurations.
Ethnomethodology.
Situated action.
Plans versus scripts in CSCW.
Prompt Event.
Computational Addressability.

TEST:
Keep one prompt fixed across a sequence of changing situations.

Alter:
- available tools,
- prior artifacts,
- selected objects,
- environmental state,
- interaction history.

Observe whether the prompt’s operative meaning remains stable.

If different situated resources systematically produce different local trajectories while the prompt remains unchanged, model the prompt as a resource rather than a partial executable path.

PLATFORM:
[[Interpretive Coupling]]

LINKS:
[[Prompt Event]]
[[Computational Addressability]]
[[Specification Completion]]

BIBTEX:
@book{suchman1987plans,
  author = {Suchman, Lucy A.},
  title = {Plans and Situated Actions: The Problem of Human-Machine Communication},
  publisher = {Cambridge University Press},
  year = {1987}
}
