ZETTEL

ID: CALVINO-005.01

TITLE:
Calvino excluded changing personalities, not all changing constraints.

SOURCE:
Italo Calvino — Working synopsis for L'ordre dans le crime — reproduced by Paul Braffort in "L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino" — Europe, no. 815 (1997), section 2.

PASSAGE:
[QUOTE]
"Dans chaque permutation, après qu’une action de meurtre a eu lieu, la victime ne peut plus accomplir ni subir aucune action."

[QUOTE]
"Chaque personnage pourrait changer dans le déroulement de l’histoire [...] : perdre certaines incompatibilités pu en acquérir d’autres!!!!!!!!"

[QUOTE]
"Pour le moment on renonce à explorer ce domaine."

RESEARCH OBJECT:
A previously obscured distinction between event-dependent constraints on physical states and event-dependent transformations of character dispositions.

LOCAL MOVE:
Calvino already requires an action's occurrence to change what subsequent actions are permissible. Murder changes the availability of a character for subsequent events.

What he postpones is a different problem: actions that transform the character's psychological or interpersonal compatibility conditions.

SOURCE TERMS:
"Ordre des séquences";
"contraintes objectives";
"contraintes subjectives";
"incompatibilités";
"déroulement de l’histoire."

WHAT BECAME STRANGE:
The parent zettel describes a transition from fixed constraints to evolving constraints. But Calvino's original procedure already depends on evolving physical conditions.

The actual omission is narrower and more interesting: the system can represent a character becoming dead but not becoming different.

QUESTION:
What distinguishes updating a character's physical availability from updating the dispositions that determine which actions the character might perform?

DEEPER QUESTION:
Why do discrete physical transformations fit the combinatorial specification more readily than transformations of character, motive, or social relationship?

MECHANISM:
An event changes the conditions against which later events are evaluated.

Physical constraint:
A murdered character cannot subsequently act.

Dispositional constraint:
A previously incompatible action could become compatible following an intervening experience.

The first is included in Calvino's specification. The second is explicitly deferred.

FORMAL SHIFT:
Action sequence
→ current physical conditions
→ [event-dependent exclusion]
→ permissible subsequent actions.

Character experience
→ changed dispositions
→ [recompute subjective compatibility]
→ changed narrative possibilities.

SOURCE FORMALISM:
Twelve named actions distributed among four characters.

Sequential compatibility constraints.

After a murder, its victim cannot participate in subsequent actions.

Calvino explicitly identifies, but does not implement, the acquisition and loss of subjective incompatibilities.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Separate:

P(t) = physical state
D(t) = character dispositions

P(t+1) = PhysicalEffects(action(t), P(t))

D(t+1) = DispositionalEffects(action(t), D(t), P(t))

Admissible(action, t)
  = PhysicalCompatibility(action, P(t))
    AND
    CharacterCompatibility(action, D(t))

Calvino specifies operations resembling the first update, but leaves the second unresolved.

TENSION:
A psychological disposition might change because of an event, without that change being reducible to the event's physical effects.

Conversely, some apparently psychological constraints can be represented through ordinary state variables.

MISSING:
Criteria for distinguishing dispositions from temporary intentions, beliefs, relationships, and physical capacities.

A representation of which experiences produce which changes, including changes that cannot be inferred from observable actions alone.

BOUNDARY:
The synopsis demonstrates that Calvino identified dynamic character incompatibilities. It does not establish that every psychological variable was intended to be computationally modeled.

CITATION TRAIL:
[[CALVINO-005]]
→ Calvino's original synopsis, quoted by Braffort
→ distinction between physical and subjective constraints
→ Brenner, "Creating Dynamic Story Plots with Continual Multiagent Planning" (2010)
→ Young, "Sketching a Generative Model of Intention Management" (2017).

TEST:
Implement the original four-character, twelve-action system under three conditions:

A. Static compatibility rules.

B. Physical state changes only.

C. Physical and dispositional state changes.

Use identical starting characters and action inventories.

Identify which sequences become valid or invalid, and which kinds of character development remain impossible to represent.

PLATFORM:
[[Evolving Narrative Possibility Spaces]]

LINKS:
[[CALVINO-005]]
[[CALVINO-003]]
[[CALVINO-013]]
[[CALVINO-016]]

BIBTEX:
@article{braffort1997ordre,
  author  = {Braffort, Paul},
  title   = {L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino},
  journal = {Europe},
  number  = {815},
  year    = {1997},
  month   = mar,
  url     = {https://www.paulbraffort.net/litterature/critique/calvino_crime.html},
  note    = {Section 2 reproduces passages from Calvino's working synopsis}
}
