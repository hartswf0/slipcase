ZETTEL

ID: CALVINO-005.04

TITLE:
Contradictory desires can belong to one coherent character.

SOURCE:
R. Michael Young — "Sketching a Generative Model of Intention Management for Characters In Stories: Adding Intention Management to a Belief-Driven Story Planning Algorithm" — AIIDE Workshop on Intelligent Narrative Technologies (2017), pp. 281–287, especially pp. 282–284.

PASSAGE:
[PARAPHRASE]
Young's HEADSPACEX representation permits a character to possess desires supported by inconsistent motivations and even desires for contradictory conditions.

Desires become intentions when a character adopts specific goals and plans.

In the initial implementation, characters revise intentions in response to new beliefs but do not freely adopt goals inconsistent with those to which they are already committed.

RESEARCH OBJECT:
A distinction between contradictory desires, contradictory intentions, and contradictory descriptions of the physical world.

LOCAL MOVE:
Young represents desires separately from intentions and allows conflicting dispositions to coexist without immediately treating them as planning inconsistencies.

The model imposes stronger restrictions when desires are converted into commitments.

SOURCE TERMS:
"HEADSPACEX";
"belief state";
"desire";
"intention";
"motivations";
"apparent solution";
"single-minded commitment";
"intention revision."

WHAT BECAME STRANGE:
A character who wants incompatible outcomes is not necessarily an incoherent character.

Conflict between desires may be precisely what gives the character narrative interest.

The parent zettel's proposed dynamic compatibility conditions therefore raise a new danger: treating psychological consistency as if it were logical consistency.

QUESTION:
When should contradictory character dispositions be preserved rather than eliminated by an anticombinatorial filter?

DEEPER QUESTION:
Can a computational character change through conflict among existing motivations rather than through a rule that directly rewrites personality attributes?

MECHANISM:
A character possesses multiple desires.

Contextual conditions influence which desires become intentions.

Adopted intentions organize plans.

New information can invalidate those plans and trigger revision or abandonment.

The resulting behavior depends on both the character's dispositions and its commitments.

FORMAL SHIFT:
Potentially conflicting desires
→ contextual motivations
→ [intention adoption]
→ committed plan
→ [new beliefs or failure]
→ revised intention state.

SOURCE FORMALISM:
HEADSPACEX defines:

Belief states containing beliefs held true, held false, or unknown.

Desires as tuples of character, motivation conditions, and a desired epistemic literal.

Intentions as tuples including character, adoption state, motivations, goal condition, and plan.

Plans represented through partial-order causal-link structures.

The paper explicitly allows inconsistent desires while limiting intention adoption through single-minded commitment.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Character c desires:

D1: protect another character
D2: expose that character's secret

Both desires may remain active.

Context K1 may activate D1 as an intention.
Context K2 may activate D2.

The resulting tension is not:

WorldState = logically inconsistent

but:

CharacterDesires = potentially incompatible

An intention-selection mechanism must decide which commitments become actionable.

TENSION:
A strict narrative planner can maintain consistent commitments by excluding contradictory intentions.

A literary representation may instead need ambivalence, indecision, self-deception, and action inconsistent with previously stated commitments.

Young's initial HEADSPACEX model uses single-minded commitment, while acknowledging the need for a wider range of character-specific commitment policies.

MISSING:
A general mechanism for representing ambivalence without forcing an immediate resolution into a single intention.

An account of when contradictory behavior should count as character complexity, deception, transformation, or computational error.

BOUNDARY:
HEADSPACEX does not establish that contradiction automatically produces compelling characters.

Its initial commitment policy should not be mistaken for a comprehensive psychological model.

CITATION TRAIL:
[[CALVINO-005]]
→ Young (2017), Definitions 2–4
→ Bratman, Intention, Plans, and Practical Reason (1987)
→ Cohen and Levesque, "Intention Is Choice with Commitment" (1990)
→ van der Hoek, Jamroga, and Wooldridge, "Towards a Theory of Intention Revision" (2007).

TEST:
Define a character with two conflicting desires.

Compare:

A. A planner that rejects contradictory desires.

B. HEADSPACEX-style desire representation with single-minded commitments.

C. A model permitting explicit conflict and revision among commitments.

Hold narrative events constant.

Measure differences in available character trajectories, failed plans, and explanations of behavior.

Ask readers whether the resulting actions appear contradictory, complex, or unmotivated.

PLATFORM:
[[Computational Character Ambivalence]]
[[Narrative Psychology and Intention Revision]]

LINKS:
[[CALVINO-005]]
[[CALVINO-005.01]]
[[CALVINO-005.03]]
[[CALVINO-016]]

BIBTEX:
@inproceedings{young2017sketching,
  author    = {Young, R. Michael},
  title     = {Sketching a Generative Model of Intention Management for Characters In Stories: Adding Intention Management to a Belief-Driven Story Planning Algorithm},
  booktitle = {Proceedings of the AIIDE-17 Workshop on Intelligent Narrative Technologies},
  pages     = {281--287},
  year      = {2017},
  publisher = {AAAI Press},
  url       = {https://cdn.aaai.org/ojs/12986/12986-52-16503-1-2-20201228.pdf}
}
