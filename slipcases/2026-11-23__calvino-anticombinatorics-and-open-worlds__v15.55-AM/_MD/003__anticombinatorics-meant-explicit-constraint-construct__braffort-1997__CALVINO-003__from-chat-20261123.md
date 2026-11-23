ZETTEL

ID: CALVINO-003

TITLE:
Anticombinatorics meant explicit constraint construction, not simply choosing from many possibilities.

SOURCE:
Paul Braffort — "L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino" — Europe, no. 815, March 1997, sections 2–3.

PASSAGE:
[PARAPHRASE]
Braffort describes writing programs that eliminated incompatible narrative combinations through logical and semantic compatibility matrices. The resulting filters did not adequately control combinatorial explosion.

RESEARCH OBJECT:
The difference between constraints that define admissible narrative states and probabilities that favor particular generated sequences.

LOCAL MOVE:
Braffort identifies anticombinatorial work with the explicit specification of structures, rules, and constraints. His account gives the term a narrower operational meaning than general selection from possibility.

SOURCE TERMS:
"filtres anti-combinatoires";
"matrices de compatibilité";
"contraintes objectives";
"contraintes subjectives."

WHAT BECAME STRANGE:
The apparent equivalence between anticombinatorics and probabilistic generation disappears when the systems' operations are compared.

QUESTION:
What would a modern generative model need to represent before it could perform Calvino's anticombinatorial operations rather than merely resemble their outcomes?

DEEPER QUESTION:
Can narrative admissibility be learned statistically, or does it require explicit representations of causality, action, time, and changing world states?

MECHANISM:
Calvino–Braffort:
Define candidate relations, then test their compatibility.

Autoregressive language modeling:
Estimate a conditional distribution over subsequent tokens.

FORMAL SHIFT:
Narrative actions
→ character/action relations
→ [compatibility tests]
→ admissible sequences.

SOURCE FORMALISM:
Four characters; twelve specified actions; pairwise relations; logical and semantic filters.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Constraint system:
C(sequence, world_state) ∈ {0,1}

Language model:
P(token_t | token_<t, context)

A highly probable token sequence is not necessarily an admissible event sequence.

TENSION:
A learned model can approximate constraints without implementing an explicit logical verifier. A constraint engine can enforce consistency without producing interesting prose.

MISSING:
A shared representation that permits both learned generation and verification of narrative state transitions.

BOUNDARY:
Braffort's surviving account does not supply a complete executable implementation or evidence that the intended novel was successfully generated.

CITATION TRAIL:
Braffort, section 2, objective and subjective constraints.
Calvino, "Prose et anticombinatoire," pp. 319–331.
Meehan, TALE-SPIN (1977).

TEST:
Construct a small four-character narrative corpus. Compare free generation, probabilistic reranking, and explicit state-based constraint checking. Measure violations separately from aesthetic preferences.

PLATFORM:
[[Narrative Constraint Engines]]

LINKS:
[[CALVINO-004]]
[[CALVINO-005]]
[[CALVINO-008]]

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
