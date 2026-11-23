ZETTEL

ID: CALVINO-005.06

TITLE:
The programmer's aesthetic constraints are not the characters' subjective constraints.

SOURCE:
Italo Calvino — Working synopsis for L'ordre dans le crime — reproduced by Paul Braffort in "L'ordre dans le crime: Une expérience cybernétique avec Italo Calvino" — Europe, no. 815 (1997), section 2.

PASSAGE:
[PARAPHRASE]
After distinguishing objective constraints from constraints inferred from character personalities, Calvino introduces a further category: aesthetic constraints, which he also identifies as subjective constraints of the programmer.

He then asks whether character-based and aesthetic constraints can be considered simultaneously.

Braffort reports that the preliminary implementation remained limited to logical constraints and that its compatibility matrices did not sufficiently reduce combinatorial explosion.

RESEARCH OBJECT:
A third constraint regime that belongs neither to the storyworld's physical conditions nor to its characters' dispositions.

LOCAL MOVE:
Calvino recognizes that a sequence can satisfy narrative compatibility requirements while remaining unsatisfactory from the programmer's aesthetic perspective.

The specification therefore contains distinct problems of possibility, characterization, and artistic selection.

SOURCE TERMS:
"contraintes objectives";
"contraintes subjectives";
"contraintes esthétiques";
"subjectives du programmeur";
"acceptable logiquement";
"acceptable psychologiquement."

WHAT BECAME STRANGE:
The unresolved problem is not simply that characters need to change.

Even a system that correctly models every character transformation would still not necessarily produce the narrative an artist wants.

The aesthetic requirements of the programmer occupy a distinct position from those of the fictional agents.

QUESTION:
How can an author-directed generative system evaluate a developing narrative without reducing character autonomy to compliance with a predetermined plot?

DEEPER QUESTION:
What happens when the event that is most plausible for a character is the event that is least desirable for the work's aesthetic development?

MECHANISM:
Physical constraints exclude actions that violate the established world.

Character constraints evaluate actions relative to dispositions and narrative motivations.

Aesthetic constraints evaluate larger configurations according to artistic purposes.

These evaluations can disagree.

FORMAL SHIFT:
Candidate narrative
→ physical consistency assessment
→ character plausibility assessment
→ aesthetic assessment
→ [selection, revision, or rejection]
→ revised narrative possibilities.

SOURCE FORMALISM:
Calvino identifies objective, subjective, and aesthetic constraints.

He explicitly raises the problem of considering subjective and aesthetic constraints together.

Braffort describes compatibility matrices for preliminary logical and semantic filtering.

The consulted account supplies no completed algorithm integrating all three constraint regimes.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

C_world(N) = world consistency
C_character(N) = character plausibility
Q_aesthetic(N) = artistic evaluation

Then:

Generate(N)
subject to C_world(N)

Evaluate:
C_character(N)
Q_aesthetic(N)

These evaluations need not agree.

A character-plausible event may weaken aesthetic structure.

An aesthetically valuable event may challenge the current character model and require its revision.

TENSION:
Michael Brenner's 2010 continual-planning framework addresses evolving beliefs, motivations, and character traits but explicitly leaves plot interestingness outside its formal machinery.

This suggests that increasingly rich world simulation does not automatically resolve Calvino's separate aesthetic problem.

Yet an external aesthetic optimizer may suppress unexpected developments arising from the simulated characters.

MISSING:
A representation of aesthetic criteria that permits them to change during composition.

A method for distinguishing deliberate aesthetic exception from inconsistency or opportunistic constraint relaxation.

An account of which aesthetic decisions should belong to the author, the generator, the reader, or their interaction.

BOUNDARY:
Calvino identifies aesthetic constraints as a problem for the programmer. The surviving specification does not demonstrate that they were implemented.

The evidence does not license reducing aesthetic evaluation to a single numeric reward, nor does it establish that formal criteria can never contribute to aesthetic judgment.

CITATION TRAIL:
[[CALVINO-005]]
→ Calvino's synopsis, aesthetic constraints
→ Braffort (1997), section 2
→ Brenner (2010), Discussion, pp. 1521–1522
→ Dehn (1981), author-directed generation
→ research on experience management and aesthetic evaluation.

TEST:
Construct a small narrative generator with independent physical, character, and aesthetic evaluators.

Define an event that:

A. Satisfies physical constraints.

B. Is plausible for a character.

C. Undermines the desired dramatic trajectory.

Compare three systems:

1. Reject the event through an aesthetic filter.

2. Accept the event and revise subsequent narrative goals.

3. Modify the character model to favor the originally desired trajectory.

Determine which interventions preserve consistency, which impose authorial control, and which permit unanticipated narrative development.

PLATFORM:
[[Aesthetic Governance of Generative Systems]]
[[Character Autonomy Versus Authorial Control]]

LINKS:
[[CALVINO-005]]
[[CALVINO-005.01]]
[[CALVINO-005.04]]
[[CALVINO-002]]
[[CALVINO-007]]
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
  note    = {Section 2 reproduces Calvino's distinction between objective, subjective, and aesthetic constraints}
}
