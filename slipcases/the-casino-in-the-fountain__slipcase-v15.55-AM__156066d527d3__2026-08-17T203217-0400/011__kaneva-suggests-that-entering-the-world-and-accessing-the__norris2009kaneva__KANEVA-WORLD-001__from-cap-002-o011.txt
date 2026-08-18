ZETTEL

ID: KANEVA-WORLD-001

TITLE:
Kaneva suggests that “entering the world” and “accessing the world” are different operations.

SOURCE:
Kaneva product language preserved by Norris — 2009; contemporary Kaneva descriptions — 2007–2009.

SOURCE URL:
https://jvwr-ojs-utexas.tdl.org/jvwr/article/view/658/500

PASSAGE:
[PARAPHRASE] Kaneva advertised movement back and forth between its 2D web presence and its 3D virtual world.

RESEARCH OBJECT:
The distinction between WORLD and WORLD CLIENT becomes visible.

A user can remain connected to the social system without invoking the representational machinery that makes the system appear as navigable 3D space.

LOCAL MOVE:
Kaneva distributes participation across a lightweight 2D representation and a heavier 3D client.

SOURCE TERMS:
2D web
3D Virtual World
move back and forth
social networking
virtual world

WHAT BECAME STRANGE:
Downloading or launching the 3D client may not be “entering Kaneva.” It may instead be requesting a particular rendering and interaction regime for something the user was already inside.

QUESTION:
What operation does a 3D client actually perform on a world that already exists as network state?

DEEPER QUESTION:
Should rendering be understood as world creation, world access, or one temporary interpretation of an already-operating world?

MECHANISM:
<WORLD STATE>
→ [2D CLIENT]
→ <DOCUMENTARY / PROFILE INTERFACE>

<WORLD STATE>
→ [3D CLIENT]
→ <SPATIAL / AVATAR INTERFACE>

FORMAL SHIFT:
[ENTER WORLD]
→ [INVOKE REPRESENTATION]

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ACCESS(W) ≠ RENDER_3D(W)

RENDER_3D(W) :=
project(
    W,
    dimensions = 3,
    interaction = embodied_navigation,
    representation = avatar + object + place
)

RENDER_2D(W) :=
project(
    W,
    dimensions = 2,
    interaction = document_navigation,
    representation = profile + list + page
)

TENSION:
Virtual-world discourse commonly identifies the rendered environment with the world. Kaneva's explicit 2D/3D traversal makes that identification harder to sustain.

MISSING:
We need Kaneva's actual architecture to determine which state lived server-side independently of either rendering and which state was client-specific.

BOUNDARY:
This is an architectural hypothesis generated from the documented cross-interface design, not a recovered description of Kaneva's source code.

CITATION TRAIL:
Kaneva source/code releases associated with its developer program.
Client protocol documentation.
Persistence research in virtual-world literature.
Database-versus-rendering architectures in MUDs, Active Worlds, and Second Life.

TEST:
Turn the 3D Kaneva client off.

Enumerate everything that still exists.

Whatever survives is a candidate for WORLD STATE rather than WORLD RENDERING.

Then turn the 2D site off and repeat.

The intersection is the strongest candidate for Kaneva's representation-independent world.

PLATFORM:
[[The world is not the picture of the world]]

LINKS:
[[KANEVA-DIM-001]]
[[Persistent state precedes rendering]]
[[Entering is an interface effect]]

BIBTEX:
@article{norris2009kaneva,
  author  = {Norris, James R.},
  title   = {The Growth and Direction of Healthcare Support Groups in Virtual Worlds},
  journal = {Journal of Virtual Worlds Research},
  year    = {2009},
  url     = {https://jvwr-ojs-utexas.tdl.org/jvwr/article/view/658/500}
}