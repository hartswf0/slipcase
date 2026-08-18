ZETTEL

ID:
HL-20260817-01

TITLE:
THE PLAN IS NOT THE SHOT: ONE WORLD REQUIRES REPRESENTATIONS WITH DIFFERENT JURISDICTIONS

SOURCE:
Tim Ingold, “On Building a House,” Chapter 4 of Making: Anthropology, Archaeology, Art and Architecture (Routledge, 2013), especially pp. 53–56. SOURCE URL: https://doi.org/10.4324/9780203559055

ABIDING ACRES, SCENE-BRIEF.md, hartswf0/abiding-halfworld. SOURCE URL: https://github.com/hartswf0/abiding-halfworld/blob/main/SCENE-BRIEF.md

PASSAGE:
[QUOTE — INGOLD] “Their straight lines were not the notional point-to-point connectors of Euclid, but actual lengths of cord pegged out on site and at full scale.”

[QUOTE — INGOLD] “Their points were nails or stakes, hammered into wood or ground.”

[QUOTE — ABIDING] “A plan is a map, not a shot list.”

[PARAPHRASE — ABIDING] The scene convention distinguishes stable plan-space from frame-space. Named stations hold world position and continuity; shot construction separately requires one subject, a committed distance, deliberate omission, a lens, and a two-second readability test.

RESEARCH OBJECT:
The House of Language cannot be one universal representational system.

ABIDING ACRES demonstrates a concrete failure of representational monism. A top-down plan can be metrically correct and still produce an unreadable image when projected into a cinematic frame. The plan answers where bodies may be. The shot answers what matters now. These are not different resolutions of the same representation. They have different obligations.

Ingold’s constructive geometry clarifies why this matters. For medieval masons, a line could be a full-scale cord on the site and a point could be a nail or stake. Representation was embedded in the work rather than standing above it as a complete abstract description. ABIDING similarly gains reliability when plan-space is treated as one working instrument among others rather than as the universal description from which every subsequent decision should be deduced.

The operative hypothesis is therefore JURISDICTIONAL SEMANTICS: a world-building system becomes more reliable when each representation has a declared domain of authority and is prevented from answering questions for which it was not designed.

LOCAL MOVE:
SHOTCALL RULE:

Before every render, name five things:

SUBJECT
DISTANCE
OMIT
CONCEPT
GROUND TRUTH PRESERVED

Permit PLAN to decide named world positions and continuity.
Permit SHOT to decide selection, emphasis, framing, and legibility.
Do not infer visual importance from the number of true objects in plan-space.

SOURCE TERMS:
constructive geometry
plan
station
subject
distance
lens
frame
omission
contact pair
map
shot list

WHAT BECAME STRANGE:
Correctness is representation-relative.

A plan can be true while its projection is false as a picture. This is not necessarily a contradiction. It reveals that “correct” means correct with respect to a task and a representational jurisdiction.

The strange consequence is that a world may require several mutually irreducible truths at once: metric truth, continuity truth, identity truth, conceptual truth, and perceptual truth.

QUESTION:
What is the minimum set of representational jurisdictions required for a computational world to remain spatially consistent, narratively continuous, semantically directed, and perceptually legible?

DEEPER QUESTION:
Can a programming language for worlds be designed as a federation of partial languages in which no representation is allowed to claim the whole world?

MECHANISM:
PLAN establishes persistent spatial possibility.

SCENE establishes current event.

LOCK establishes identity invariants.

CONCEPT establishes interpretive pressure.

SHOTCALL establishes subject and projection.

LOOK determines whether the projection actually reads.

FORMAL SHIFT:
FROM:

ONE DESCRIPTION
→ EXECUTION
→ WORLD

TO:

PLAN ─────────────┐
LOCK ─────────────┤
SCENE ────────────┤
CONCEPT ──────────┼→ SHOTCALL → RENDER → LOOK
CONTINUITY ───────┤
CURRENT STATE ────┘

SOURCE FORMALISM:
ABIDING explicitly implements named plan stations, contact pairs, character locks, concept weights, scene occupancy, CLOSE/MEDIUM/WIDE framing, lens(), and a render-look-revise loop.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

J = {PLAN, LOCK, CONCEPT, CONTINUITY, SHOT, LOOK}

Each language L in J has a jurisdiction Jur(L).

Reliability requires:

for decision d,
use L only if d ∈ Jur(L).

A category error occurs when one language is asked to determine a property outside its jurisdiction.

Example:

PLAN may determine position.
PLAN may not determine visual salience.

TENSION:
READING A:
These are merely implementation modules inside one larger program.

READING B:
The modules instantiate genuinely different semantics. Metric placement cannot itself encode salience; a concept weight cannot itself encode coordinates; a visual inspection cannot itself establish historical source fidelity.

If B holds, House Language is not a higher-level universal syntax. It is a protocol for negotiating among partial languages.

MISSING:
A rigorous inventory of the decisions each existing ABIDING representation is allowed to make.

Cases where jurisdictional conflict cannot be resolved without revising the underlying world model.

Evidence from another world-building system showing the same division independently.

BOUNDARY:
This zettel does not claim that representational jurisdictions are ontologically natural or immutable. They are designed partitions whose usefulness must be tested against failures.

CITATION TRAIL:
[[HOUSE-LANGUAGE-001-E]]
→ Ingold constructive geometry
→ ABIDING plan-space
→ “A plan is a map, not a shot list”
→ metrically true / pictorially false
→ representation-relative correctness
→ jurisdictional semantics
→ federated House Language

TEST:
Choose ten ABIDING scenes with the same plan.

For each record every consequential decision and classify its source:

PLAN
LOCK
SCENE TEXT
CONCEPT
CONTINUITY
SHOTCALL
LOOK/LEDGER

Then deliberately remove one jurisdiction at a time.

Measure which failures appear.

The zettel gains support if distinct failure classes reliably appear when distinct representational jurisdictions are removed, and if no single remaining representation can recover all of them without importing information from the missing layer.

PLATFORM:
HOUSE LANGUAGE / ABIDING HALFWORLD / JURISDICTIONAL SEMANTICS / SHOTCALLING

LINKS:
[[HOUSE-LANGUAGE-001-E]]
[[HOUSE-LANGUAGE-001-F]]
[[HOUSE-SHOT-001]]
[[ABIDING-HALFWORLD]]
[[PLAN-IS-NOT-SHOT]]
[[JURISDICTIONAL-SEMANTICS]]

BIBTEX:
@book{Ingold2013Making,
  author    = {Ingold, Tim},
  title     = {Making: Anthropology, Archaeology, Art and Architecture},
  year      = {2013},
  publisher = {Routledge},
  doi       = {10.4324/9780203559055},
  url       = {https://doi.org/10.4324/9780203559055}
}

@misc{Hartsoe2026SceneBrief,
  author = {Hartsoe, Watson},
  title  = {ABIDING ACRES — Scene Convention},
  year   = {2026},
  url    = {https://github.com/hartswf0/abiding-halfworld/blob/main/SCENE-BRIEF.md}
}
