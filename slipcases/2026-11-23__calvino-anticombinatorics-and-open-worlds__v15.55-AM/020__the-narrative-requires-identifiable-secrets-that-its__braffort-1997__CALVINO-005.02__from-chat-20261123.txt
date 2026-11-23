ZETTEL

ID: CALVINO-005.02

TITLE:
The narrative requires identifiable secrets that its original combinatorial vocabulary does not represent.

SOURCE:
Italo Calvino — Working synopsis for L'ordre dans le crime — reproduced in Paul Braffort, "L'ordre dans le crime" (1997), section 2, compatibility rules for the appropriation of secrets and wills.

PASSAGE:
[QUOTE]
"La réversibilité des actes d’appropriation de secret est possible, s’il se trouve des deux côtés des secrets différents."

[PARAPHRASE]
A character who has obtained another's secret need not obtain that same secret again, but may obtain a different secret through another action.

RESEARCH OBJECT:
An implicit narrative entity that must be represented before the stated compatibility rule can be executed correctly.

LOCAL MOVE:
Calvino treats the appropriation of a secret as an action between two characters while simultaneously requiring the computer to distinguish one secret from another.

The basic combinatorial model identifies the action and its participants. The semantic rule requires an additional identity relation.

SOURCE TERMS:
"appropriation d’un secret";
"secrets différents";
"réversibilité";
"relations";
"compatibilité."

WHAT BECAME STRANGE:
The first representation problem is not necessarily how to make characters change.

It is how to represent what their actions are about.

The phrase "a different secret" introduces an entity whose identity is not contained in the action's original binary character relation.

QUESTION:
What additional entities must be introduced before Calvino's supposedly simple compatibility rules can be implemented?

DEEPER QUESTION:
At what point does a finite combinatorial inventory turn into an open-ended ontology of objects, knowledge, obligations, and relationships?

MECHANISM:
The system must determine whether two actions concern the same information.

Without secret identity, it cannot distinguish obtaining the same secret repeatedly from obtaining several different secrets.

The corresponding problem recurs for distinct wills, motivations, and interpersonal commitments.

FORMAL SHIFT:
Binary character relation
→ action with an additional semantic object
→ [compare object identity and possession]
→ determine whether repetition is redundant or consequential.

SOURCE FORMALISM:
Four characters.

Twelve actions.

Each action is assigned an ordered pair of distinct characters.

The synopsis additionally distinguishes the same secret from different secrets, without supplying an explicit datatype for secret identity in the reported initial enumeration.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Initial event:
E = (actor, action, patient)

Required richer event:
E = (actor, action, patient, object)

For secret acquisition:

E1 = (A, discovers, B, secret_1)
E2 = (A, extracts, B, secret_2)

The redundancy judgment depends on:

secret_1 == secret_2

It cannot be determined from actor, action, and patient alone.

TENSION:
The additional object can make semantic compatibility computable, but every introduced entity creates further questions.

Who possesses the secret?
Who knows it?
Can two characters independently discover it?
Does revealing it change its status?
Can the content of a secret itself change?

MISSING:
A specification of secret identity, ownership, knowledge, disclosure, and temporal persistence.

Evidence about whether Braffort's implemented matrices represented these semantic objects or only approximated their effects.

BOUNDARY:
The original enumeration omits explicit secret identifiers. This does not prove that Braffort's programs lacked all auxiliary representations; their complete source code has not been established.

CITATION TRAIL:
[[CALVINO-005]]
→ Calvino's rules for secret appropriation
→ the semantic identity missing from binary action representation
→ research on epistemic planning
→ formal representations of knowledge and belief in multiagent systems.

TEST:
Construct two distinct twelve-action sequences that have identical actor-action-patient assignments but differ in whether a later acquisition concerns the same secret.

Try to classify both using only the original event vocabulary.

Introduce explicit secret identifiers and repeat.

The resulting difference establishes the minimum additional representational requirement.

PLATFORM:
[[Narrative Ontology and Hidden State]]
[[Formal Audits of Computational Literature]]

LINKS:
[[CALVINO-005]]
[[CALVINO-003]]
[[CALVINO-013]]
[[CALVINO-014]]

BIBTEX:
@article{braffort1997ordre,
  author  = {Braffort, Paul},
  title   = {L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino},
  journal = {Europe},
  number  = {815},
  year    = {1997},
  month   = mar,
  url     = {https://www.paulbraffort.net/litterature/critique/calvino_crime.html},
  note    = {Contains excerpts from Calvino's synopsis concerning secrets, wills, and action compatibility}
}
