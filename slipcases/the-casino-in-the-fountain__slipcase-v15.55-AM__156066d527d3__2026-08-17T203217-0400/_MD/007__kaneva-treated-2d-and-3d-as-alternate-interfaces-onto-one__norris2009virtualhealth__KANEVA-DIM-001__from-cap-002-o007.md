ZETTEL

ID: KANEVA-DIM-001

TITLE:
Kaneva treated 2D and 3D as alternate interfaces onto one social world rather than as separate destinations.

SOURCE:
James R. Norris — “The Growth and Direction of Healthcare Support Groups in Virtual Worlds” — Journal of Virtual Worlds Research — 2009.

SOURCE URL:
https://jvwr-ojs-utexas.tdl.org/jvwr/article/view/658/500

PASSAGE:
[QUOTE] Kaneva provided “flexibility to easily move back and forth from the 2D web to the 3D Virtual World of Kaneva.”

RESEARCH OBJECT:
The unusual object is not a 3D world with an accompanying website. It is an identity-and-content system deliberately exposed through representations of different dimensionality.

LOCAL MOVE:
Kaneva refuses to make entry into 3D the prerequisite for participation. The 2D profile/social-network layer and 3D avatar/world layer are presented as traversable faces of the same service.

SOURCE TERMS:
2D web
3D Virtual World
move back and forth
social networking
avatar
profile

WHAT BECAME STRANGE:
A “virtual world” need not coincide with its rendered three-dimensional space. If relationships, profiles, media, groups, and identity persist while the interface changes dimensionality, the world may reside in the persistent state beneath both representations.

QUESTION:
Where is the virtual world if its inhabitants can leave 3D without leaving the world?

DEEPER QUESTION:
Can dimensionality be understood as a view over world-state rather than a defining property of the world itself?

MECHANISM:
[OUR INFERENCE]

<USER + SOCIAL STATE + MEDIA + RELATIONS>
→ [SELECT REPRESENTATION]
→ <2D PROFILE / SOCIAL WEB>

or

<USER + SOCIAL STATE + MEDIA + RELATIONS>
→ [SELECT REPRESENTATION]
→ <3D AVATAR / SPATIAL WORLD>

FORMAL SHIFT:
<WORLD = 3D SCENE>
→ <PERSISTENT SOCIAL STATE>
→ [RENDER THROUGH DIFFERENT INTERFACES]
→ <2D WORLD-VIEW | 3D WORLD-VIEW>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD := persistent_state

VIEW₂D(WORLD) := profiles + groups + messages + media
VIEW₃D(WORLD) := avatars + homes + places + embodied interaction

switch(VIEW₂D, VIEW₃D) ≠ exit(WORLD)

TENSION:
Calling Kaneva a “3D virtual world” makes the 3D client sound ontologically primary. Kaneva's own product language instead emphasized movement between the 2D web and 3D world.

MISSING:
The public descriptions do not establish the precise backend data architecture or exactly which entities were shared between the two clients.

BOUNDARY:
The evidence supports continuity of user experience and service identity across 2D and 3D. It does not by itself prove that every object or action had a single shared underlying representation.

CITATION TRAIL:
Kaneva's archived technical documentation.
Kaneva client/server documentation.
Database schemas or source released through its developer program.
Contemporary comparisons with Second Life, Vivaty, There, and Active Worlds.

TEST:
Recover one Kaneva account through archived documentation and construct an entity matrix:

ENTITY | EXISTS IN 2D | EXISTS IN 3D | SAME ID? | MUTATION PROPAGATES?

Test profile, avatar name, friend, group, media item, home, event, and message.

PLATFORM:
[[A world can exceed its rendering]]

LINKS:
[[Representation is not world-state]]
[[One object multiple interfaces]]
[[Dimensional continuity]]

BIBTEX:
@article{norris2009virtualhealth,
  author  = {Norris, James R.},
  title   = {The Growth and Direction of Healthcare Support Groups in Virtual Worlds},
  journal = {Journal of Virtual Worlds Research},
  year    = {2009},
  url     = {https://jvwr-ojs-utexas.tdl.org/jvwr/article/view/658/500}
}