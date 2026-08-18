ZETTEL

ID:
HL-20260817-04

TITLE:
A CONCEPT WEIGHT CAN CALL A SHOT WITHOUT DETERMINING IT

SOURCE:
Tim Ingold, “On Building a House,” Chapter 4 of Making: Anthropology, Archaeology, Art and Architecture (Routledge, 2013), pp. 54–55, discussing rules and maxims. SOURCE URL: https://doi.org/10.4324/9780203559055

ABIDING ACRES, BUILD-BRIEF.md, SCENE-BRIEF.md and atlas/world.json, hartswf0/abiding-halfworld. SOURCE URL: https://github.com/hartswf0/abiding-halfworld

PASSAGE:
[QUOTE — INGOLD] The masons’ rules “comprised resources for action, but did not determine it.”

[PARAPHRASE — ABIDING] The concept graph is explicitly treated as a director. A scene at watched(8) must be framed through a relation of surveillance; a scene at standing(7) must visually organize whether a person is recognized by an apparatus. The concept does not dictate coordinates or a unique camera.

RESEARCH OBJECT:
House Language needs an executable category between metadata and deterministic instruction.

ABIDING’s concept weights occupy this category. watched(8) is not simply a theme label because downstream agents are instructed to change the frame because of it. But it is not a macro such as CAMERA = SURVEILLANCE_POV. Multiple different images can correctly instantiate the same pressure.

This resembles Ingold’s account of craft maxims as resources for action rather than complete determinants of practice.

The important computational category is therefore ORIENTING OPERATOR: an instruction that constrains what must become perceptible while deliberately leaving the concrete realization open to situated judgment.

LOCAL MOVE:
PROVISIONAL SHOTCALL GRAMMAR:

WATCHED h>=7
→ an observing relation must become structurally legible.

STANDING h>=7
→ recognition/nonrecognition by an apparatus must dominate composition.

DEAD h>=7
→ absence must carry more visual force than explanatory information.

MEADOW h>=7
→ nonhuman route or ground may displace the human figure as subject.

Do not bind any operator to one stock camera pattern.

SOURCE TERMS:
rules
maxims
resources for action
concept graph
director
watched
standing
dead
meadow
weight
framing

WHAT BECAME STRANGE:
A semantically compressed token can exert more directorial force than a much longer scene description.

“Two children stand at the bulb” establishes bodies and action.

watched(8) establishes what the picture must make perceptible.

QUESTION:
Can concept weights become a small operational language whose commands create recognizable visual invariants without collapsing into fixed templates?

DEEPER QUESTION:
What kind of computational semantics is needed for commands whose function is to reorganize attention rather than specify a state transition?

MECHANISM:
SCENE FACTS
→ what occurs.

PLAN
→ where.

LOCKS
→ who/what remains invariant.

CONCEPT(h)
→ what relation must become salient.

SHOTCALLER
→ chooses one situated realization.

LOOK
→ tests whether salience became perceptible.

FORMAL SHIFT:
FROM:

CONCEPT = ANNOTATION

TO:

CONCEPT = UNDERDETERMINED DIRECTORIAL OPERATOR.

SOURCE FORMALISM:
ABIDING stores weighted concept references h and instructs scene agents to use those weights as framing guidance.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DIRECT(scene, c, h)

if h < 4:
c may remain contextual.

if 4 <= h < 7:
c must influence composition.

if h >= 7:
c must alter the dominant visual relation.

TENSION:
READING A:
Concept weights are merely creative notes interpreted by a human or model.

READING B:
Once they impose repeatable constraints on downstream transformations, they possess operational semantics even though their outputs remain underdetermined.

MISSING:
A multi-agent experiment establishing whether the same concept operator yields both recognizable invariants and non-identical solutions.

A vocabulary of allowed visual relations for each concept that does not become a style cookbook.

BOUNDARY:
WATCHED must not become synonymous with surveillance-camera POV. A deterministic cliché would destroy the situated judgment that makes it an orienting operator.

CITATION TRAIL:
[[HOUSE-LANGUAGE-001-F]]
→ Ingold / Polanyi maxims
→ resources for action
→ ABIDING concept graph
→ concept as director
→ underdetermined operator
→ shotcalling language

TEST:
Give five independent staging agents the same source scene, plan, locks, and WATCHED 8 instruction.

Do not show them an existing render.

PASS if:
all five make an observing relation perceptible;
none is forced into an identical camera solution.

FAIL if:
the instruction produces no common invariant;
or all five converge on one stock visual trope.

PLATFORM:
HOUSE LANGUAGE / ABIDING HALFWORLD / CONCEPT OPERATORS / SHOTCALLING

LINKS:
[[HOUSE-LANGUAGE-001-F]]
[[HOUSE-SHOT-003]]
[[ABIDING-HALFWORLD]]
[[CONCEPT-AS-DIRECTOR]]
[[ORIENTING-OPERATOR]]
[[WATCHED]]
[[STANDING]]

BIBTEX:
@book{Ingold2013Making,
  author    = {Ingold, Tim},
  title     = {Making: Anthropology, Archaeology, Art and Architecture},
  year      = {2013},
  publisher = {Routledge},
  doi       = {10.4324/9780203559055},
  url       = {https://doi.org/10.4324/9780203559055}
}

@misc{Hartsoe2026Abiding,
  author = {Hartsoe, Watson},
  title  = {ABIDING ACRES / abiding-halfworld},
  year   = {2026},
  url    = {https://github.com/hartswf0/abiding-halfworld}
}
