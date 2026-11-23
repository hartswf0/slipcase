ZETTEL

ID: CALVINO-005

TITLE:
Calvino identified character transformation and then excluded it from the computation.

SOURCE:
Paul Braffort — "L'ordre dans le crime" — 1997, section 2, discussion of subjective constraints.

PASSAGE:
[QUOTE]
"Pour le moment on renonce à explorer ce domaine."

[PARAPHRASE]
Calvino allows that characters could acquire or lose incompatibilities through actions they perform or undergo, but sets that possibility aside.

RESEARCH OBJECT:
Dynamic narrative constraints that change as a consequence of the narrative itself.

LOCAL MOVE:
The project confronts the possibility that characters cannot be modeled adequately through fixed attributes and compatibility relations.

SOURCE TERMS:
"contraintes subjectives";
"changer dans le déroulement de l'histoire";
"incompatibilités."

WHAT BECAME STRANGE:
The most promising computational problem may be the one Calvino explicitly declined to explore.

QUESTION:
What if narrative possibility is not a fixed search space, but a space whose constraints are continually rewritten by the story's events?

DEEPER QUESTION:
Can the possibility space change during narrative generation without making the model's consistency criteria arbitrary?

MECHANISM:
An event changes character attributes, relationships, obligations, or capabilities. Those changes alter which subsequent events are possible or plausible.

FORMAL SHIFT:
Character state at t
→ event
→ [update attributes and relations]
→ revised possibilities at t+1.

SOURCE FORMALISM:
Braffort reports the possibility of changing incompatibilities, but supplies no completed procedure for implementing this domain.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

S(t+1) = T(S(t), action(t))

C(t+1) = Constraints(S(t+1))

AvailableActions(t+1) =
  {a : C(t+1, a) = true}

An action changes not only the story but also its future possibility space.

TENSION:
Strict filtering presupposes stable constraints. Character development can invalidate assumptions that were previously useful for excluding combinations.

MISSING:
A representation for belief revision, learning, changing motives, transformations of relationships, and conflicting character perspectives.

BOUNDARY:
Calvino anticipated the problem. The source does not demonstrate that he solved it.

CITATION TRAIL:
Braffort's unpublished synopsis, quoted in the 1997 essay.
Narrative planning and character-state modeling.
Meehan, TALE-SPIN (1977).
Riedl and Young (2010).

TEST:
Run the same twelve-action narrative under two conditions: fixed character compatibility and compatibility updated after every event. Compare which plots become newly possible and which contradictions disappear.

PLATFORM:
[[Evolving Narrative Possibility Spaces]]

LINKS:
[[CALVINO-003]]
[[CALVINO-008]]
[[CALVINO-016]]

BIBTEX:
@article{braffort1997ordre,
  author  = {Braffort, Paul},
  title   = {L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino},
  journal = {Europe},
  number  = {815},
  month   = mar,
  year    = {1997},
  url     = {https://www.paulbraffort.net/litterature/critique/calvino_crime.html}
}
