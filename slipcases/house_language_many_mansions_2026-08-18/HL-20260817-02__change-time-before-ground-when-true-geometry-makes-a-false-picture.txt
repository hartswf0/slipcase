ZETTEL

ID:
HL-20260817-02

TITLE:
CHANGE TIME BEFORE GROUND WHEN TRUE GEOMETRY MAKES A FALSE PICTURE

SOURCE:
Tim Ingold, “On Building a House,” Chapter 4 of Making: Anthropology, Archaeology, Art and Architecture (Routledge, 2013), p. 48. SOURCE URL: https://doi.org/10.4324/9780203559055

ABIDING ACRES, SCENE-BRIEF.md, hartswf0/abiding-halfworld. SOURCE URL: https://github.com/hartswf0/abiding-halfworld/blob/main/SCENE-BRIEF.md

PASSAGE:
[QUOTE — INGOLD, quoting Stewart Brand] “the idea is crystalline, the fact fluid.”

[PARAPHRASE — INGOLD] Builders inhabit the kink between intended form and an unfolding world; operations seldom go according to plan and require continual improvisation.

[PARAPHRASE — ABIDING] Contact pairs in plan-space are intentionally about a hand’s width apart. At useful camera scales two correctly placed bodies may fuse into one silhouette. The preferred correction is to select a different moment in the action when they are genuinely separated; only later should frame-space be cheated, and any cheat must be recorded.

RESEARCH OBJECT:
ABIDING provides a small but exact instance of a general House Language principle: when one truthful representation yields a misleading representation downstream, the first correction should preserve as much upstream truth as possible.

A contact pair can be geometrically correct. A lens can project it correctly. The frame can still communicate an impossible two-headed body. The failure belongs neither simply to the plan nor simply to the renderer. It occurs in translation between representational jurisdictions.

The crucial discovery is that time is a correction variable. Instead of altering ground truth, the system can choose another true state along the action trajectory.

LOCAL MOVE:
SHOTCALL INVARIANT:

WHEN TWO TRUE BODIES FUSE:

1. KEEP NAMED GROUND STATIONS.
2. SEARCH THE ACTION TRAJECTORY FOR A LEGIBLE t.
3. SEARCH FOR AN EXISTING BEAT THAT SEPARATES THEM.
4. ADJUST LENS WHILE PRESERVING RELATIVE GEOMETRY.
5. ONLY THEN CHEAT FRAME-SPACE.
6. IF CHEATING, RECORD THE LIE IN THE LEDGER.

NAME THIS:
CHANGE TIME BEFORE GROUND.

SOURCE TERMS:
crystalline
fluid
contact pair
metric honesty
lens
moment
frame-space
geometry
ledger
cheat

WHAT BECAME STRANGE:
Time is not only narrative sequence. It is a representational degree of freedom for preserving spatial truth.

A frame may become more truthful by showing a different true instant rather than by making the world less true.

QUESTION:
When a truthful world-state produces a misleading projection, which dimensions may a shot alter without falsifying the world?

DEEPER QUESTION:
Can House Language encode a hierarchy of representational interventions ordered by how much underlying world truth they disturb?

MECHANISM:
WORLD TRAJECTORY:

S(t0), S(t1), S(t2), ... S(tn)

At some t:

PROJECT(S(t)) = perceptually misleading.

Instead of mutating S, search for t* such that:

WORLD_CONSTRAINTS(S(t*)) remain true
and
LEGIBILITY(PROJECT(S(t*))) improves.

FORMAL SHIFT:
FROM:

BAD FRAME
→ MOVE ACTOR

TO:

BAD FRAME
→ SEARCH TRUE TIME
→ SEARCH TRUE BEAT
→ SEARCH PROJECTION
→ DECLARE FRAME CHEAT
→ ONLY THEN ALTER WORLD.

SOURCE FORMALISM:
ABIDING uses per-scene progress/moment parameters, a lens operation, named stations, and a ledger that must record deliberate divergence from plan geometry.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CORRECTION PRIORITY:

TIME
> BEAT
> LENS
> DECLARED FRAME CHEAT
> WORLD MUTATION

where A > B means attempt A before B.

TENSION:
READING A:
This is a narrow cinematographic trick for avoiding silhouette overlap.

READING B:
It reveals a broader method for translating among representations: prefer corrections that preserve upstream invariants and shift only the downstream projection.

MISSING:
Other failure classes where temporal selection repairs a representation without altering world-state.

A criterion for when selecting a different instant preserves geometry but destroys dramatic truth.

BOUNDARY:
A different true instant is not automatically a faithful shot. If the selected time erases the event the scene is about, geometric fidelity has been purchased with dramatic falsification.

CITATION TRAIL:
[[HOUSE-LANGUAGE-001-C]]
→ crystalline idea / fluid fact
→ contact pair
→ true ground / false picture
→ choose another moment
→ minimal intervention hierarchy
→ change time before ground

TEST:
Collect every ABIDING scene where two actors visually fuse.

For each try corrections in this order:

TIME
BEAT
LENS
FRAME CHEAT
WORLD MOVE

Record after each intervention:

GEOMETRIC FIDELITY
DRAMATIC FIDELITY
TWO-SECOND LEGIBILITY
NEW DISTORTION INTRODUCED

The principle survives if earlier interventions repeatedly restore legibility while preserving more upstream invariants than later ones.

PLATFORM:
HOUSE LANGUAGE / ABIDING HALFWORLD / REPRESENTATIONAL REPAIR

LINKS:
[[HOUSE-LANGUAGE-001-C]]
[[HOUSE-SHOT-004]]
[[ABIDING-HALFWORLD]]
[[CHANGE-TIME-BEFORE-GROUND]]
[[FRAME-TRUTH]]
[[METRIC-HONESTY]]

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
