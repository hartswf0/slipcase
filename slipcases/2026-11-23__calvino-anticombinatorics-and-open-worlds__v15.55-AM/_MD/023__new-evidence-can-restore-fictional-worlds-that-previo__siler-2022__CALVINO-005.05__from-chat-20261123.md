ZETTEL

ID: CALVINO-005.05

TITLE:
New evidence can restore fictional worlds that previous constraints excluded.

SOURCE:
Cory Siler — "Open-World Narrative Generation to Answer Players' Questions" — Proceedings of AIIDE 2022, pp. 307–310, especially pp. 307–308.

PASSAGE:
[PARAPHRASE]
Siler distinguishes logically possible worlds from worlds an audience considers plausible.

In classical possible-worlds reasoning, new observations eliminate worlds inconsistent with the evidence.

In the proposed alternative, plausibility judgments are nonmonotonic. An audience can encounter evidence that forces it to reconsider worlds previously excluded by default assumptions or genre conventions.

Siler illustrates the difference through an example in which evidence about dragons changes which fictional worlds readers find plausible.

RESEARCH OBJECT:
A revision process in which new information can expand rather than merely reduce the set of considered narrative worlds.

LOCAL MOVE:
Siler questions the need for a narrative generator to settle every fact of the fictional world before the player encounters it.

The paper proposes maintaining both immutable commitments established by observations and revisable hypotheses about unseen parts of the world.

SOURCE TERMS:
"open-world narrative generation";
"immutable commitments";
"plausible worlds";
"nonmonotonic reasoning";
"player beliefs";
"implicit questions";
"contrivance."

WHAT BECAME STRANGE:
Calvino's anticombinatorics progressively removes incompatible configurations.

Siler identifies an important alternative.

A fictional world initially ruled out as implausible can become plausible when the reader discovers new evidence.

Narrative development may require restoring possibilities rather than only eliminating them.

QUESTION:
Can an anticombinatorial system remain useful if its candidate worlds are permitted to re-enter consideration after previously being excluded?

DEEPER QUESTION:
Should fictional-world generation seek convergence on one world, or maintain a changing family of plausible worlds whose distinctions matter to the audience?

MECHANISM:
The audience observes a narrative event.

The observation changes its beliefs about the story.

Previously plausible explanations may lose credibility.

Previously rejected explanations may become plausible.

Further events can be generated to answer questions raised by the revised beliefs.

FORMAL SHIFT:
Observed narrative evidence
→ plausible-world hypotheses
→ [new observation]
→ nonmonotonic revision
→ enlarged or altered hypothesis space.

SOURCE FORMALISM:
Siler proposes two representational layers:

1. Immutable commitments that future narrative extensions must respect.

2. Plausible worlds inferred beyond the player's direct observations.

The proposed process models the world and player beliefs, infers implicit questions, and adds narrative material in response.

The paper presents a research proposal rather than a demonstrated complete implementation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

H(t) = plausible narrative hypotheses
E(t) = observed evidence
D(t) = revisable defaults

Classical elimination:
H(t+1) is a subset of H(t)

Nonmonotonic revision:
H(t+1) need not be a subset of H(t)

A hypothesis excluded under an earlier default can return when new evidence defeats that default.

The distinction is between logical contradiction and defeasible plausibility.

TENSION:
Allowing worlds to re-enter consideration supports revelation, ambiguity, and shifts in genre.

But unrestricted revision can undermine continuity and permit arbitrary explanations.

The generator must distinguish facts already shown to the audience from assumptions that the audience merely supplied.

MISSING:
A formal procedure for updating plausible-world rankings from audience behavior.

A reliable distinction between revising an assumption and contradicting an established observation.

A test for whether an unexpected addition enriches the fictional world or merely repairs a poorly constructed plot.

BOUNDARY:
Siler's proposal does not prove that open-world generation improves narrative quality.

Nonmonotonic revision does not license changing facts already established as immutable commitments.

CITATION TRAIL:
[[CALVINO-005]]
→ Siler (2022), Modeling section
→ Klassen, Levesque, and McIlraith, "Towards Representing What Readers of Fiction Believe" (2017)
→ Riedl and Young, "Open-World Planning for Story Generation" (2005)
→ Robertson and Young, "Finding Schrödinger's Gun" (2014).

TEST:
Provide three descriptions of a fictional location.

Initially, all three suggest an ordinary terrestrial city.

Introduce a fourth description establishing an impossible or supernatural spatial condition.

Compare:

A. A system that eliminates inconsistent candidate worlds.

B. A system that revises genre and plausibility assumptions.

C. A system that preserves multiple competing interpretations.

Record which earlier observations each system must contradict, reinterpret, or preserve.

PLATFORM:
[[Nonmonotonic Narrative Worlds]]
[[The Foundry — Fictional Image to World]]

LINKS:
[[CALVINO-005]]
[[CALVINO-005.03]]
[[CALVINO-009]]
[[CALVINO-017]]
[[CALVINO-018]]

BIBTEX:
@inproceedings{siler2022openworld,
  author    = {Siler, Cory},
  title     = {Open-World Narrative Generation to Answer Players' Questions},
  booktitle = {Proceedings of the Eighteenth AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment},
  pages     = {307--310},
  year      = {2022},
  publisher = {AAAI Press},
  url       = {https://ojs.aaai.org/index.php/AIIDE/article/download/21981/21750/26033}
}
