ZETTEL

ID:
METAVERSE-DIM-004

TITLE:
The metaverse may be representation-independent: 2D and 3D can be clients of the same world.

SOURCE:
Mozilla — Hubs — 2018; Roblox Terms of Use — 2026; Kaneva lineage.

SOURCE URL:
https://blog.mozilla.org/en/mozilla/enabling-social-experiences-using-mixed-reality-and-the-open-web/

PASSAGE:
[PARAPHRASE]
Hubs exposed one room across desktop, mobile, and VR; Roblox defines its Services across websites, applications, consoles, VR, Player, and Studio.

RESEARCH OBJECT:
The Kaneva → Hubs → Roblox line suggests that DIMENSION is the wrong ontology.

A world can have:

2D menus
web profiles
commerce pages
mobile screens
3D scenes
VR embodiment

without becoming six different worlds.

LOCAL MOVE:
The persistent entities—identity, inventory, permissions, relationships, purchases, world state—can survive shifts in representational dimensionality.

SOURCE TERMS:
website
platform
applications
virtual reality
desktop
mobile
room
Services

WHAT BECAME STRANGE:
“2D metaverse” may not be a contradiction.

Neither may “3D metaverse” describe the decisive feature.

QUESTION:
What must remain invariant across representations for two interfaces to count as access to one world?

DEEPER QUESTION:
Is a metaverse better defined by persistent referents than by spatial rendering?

MECHANISM:
<WORLD STATE>
→ [CLIENT A]
→ <2D>

<WORLD STATE>
→ [CLIENT B]
→ <3D>

<WORLD STATE>
→ [CLIENT C]
→ <VR>

FORMAL SHIFT:
<METAVERSE = 3D SPACE>
→ <METAVERSE = PERSISTENT REFERENTIAL SYSTEM>
→ [MULTIPLE RENDERERS]
→ <POLYMORPHIC WORLD>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD :=
{
    identities,
    objects,
    relations,
    permissions,
    histories,
    economies
}

INTERFACE :=
projection(WORLD, device, context)

DIMENSION(INTERFACE) ≠ DIMENSION(WORLD)

TENSION:
Immersive-metaverse rhetoric privileges 3D embodiment.

Actual platforms repeatedly place critical world operations—identity, discovery, purchase, policy, moderation, administration—outside the rendered 3D scene.

MISSING:
A principled threshold for determining when two interfaces are projections of one world rather than merely linked services.

BOUNDARY:
Cross-device branding alone does not prove shared world-state. The invariants must be traced entity by entity.

CITATION TRAIL:
Kaneva
Mozilla Hubs
Roblox
Minecraft
MUD web frontends
MMORPG account portals

TEST:
For each system, trace:

IDENTITY
INVENTORY
FRIENDS
CURRENCY
WORLD OBJECT
PURCHASE
MESSAGE
PERMISSION

across its web, mobile, desktop, and immersive clients.

PLATFORM:
[[The world is invariant; the interface conjugates it]]

LINKS:
[[KANEVA-DIM-001]]
[[HUBS-URL-001]]
[[Representation-independent worlds]]

BIBTEX:
@misc{mozilla_roblox_multiclient,
  title = {Cross-Interface World Access in Mozilla Hubs and Roblox},
  note = {Primary-source comparison},
  year = {2026}
}