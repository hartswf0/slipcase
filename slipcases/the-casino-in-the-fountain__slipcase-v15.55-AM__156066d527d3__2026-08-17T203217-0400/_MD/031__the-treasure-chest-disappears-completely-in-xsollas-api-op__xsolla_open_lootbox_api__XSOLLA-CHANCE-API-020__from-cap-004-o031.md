ZETTEL

ID:
XSOLLA-CHANCE-API-020

TITLE:
The treasure chest disappears completely in Xsolla's API: “open loot box” is a remote state mutation with three identifiers.

SOURCE:
Xsolla — Store API v1 — Open Loot Box — current deprecated API documentation.

PASSAGE:
[PARAPHRASE] Xsolla documents a POST endpoint that “opens a loot box in a game inventory,” taking a project identifier plus item, SKU/class, and user identifiers. The endpoint is now deprecated.

RESEARCH OBJECT:
Strip away the animation.

Strip away the chest.

Strip away the avatar.

Strip away the room.

The supposedly spatial event:

OPEN LOOT BOX

reduces to an authenticated network request over inventory state.

LOCAL MOVE:
The API reveals the non-diegetic machinery beneath a familiar world metaphor.

SOURCE TERMS:
POST
open loot box
game inventory
asset_id
class_id
user_id
deprecated

WHAT BECAME STRANGE:
The chest is optional.

The world is optional.

Even the visible act of opening is optional.

The operative object is an inventory transition associated with a user.

QUESTION:
What is a loot box after every representational layer has been removed?

DEEPER QUESTION:
Could gambling-adjacent game mechanics be audited more accurately at the API/state-transition layer than at the interface layer?

MECHANISM:
POST
/projects/{project_id}/store/lootbox/open

INPUT:
asset_id
class_id
user_id

→ [OPEN]
→ <CHANGED GAME INVENTORY>

FORMAL SHIFT:
<TREASURE CHEST>
→ <API ENDPOINT>
→ [STATE TRANSITION]
→ <INVENTORY MUTATION>

SOURCE FORMALISM:
POST /projects/{project_id}/store/lootbox/open

The endpoint is documented as deprecated and scheduled for future removal.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OPEN_BOX(user, box)
→ RNG?
→ resolve_reward()
→ mutate(inventory[user])

The API documentation exposes the outer operation but not the internal random-selection mechanism.

TENSION:
Xsolla's marketing language in 2022 called “the gamble” part of loot-box excitement.

Its API presents none of that phenomenology.

The same object appears as:

MARKETING:
EXCITEMENT

INTERFACE:
CHEST

API:
POST

DATABASE:
STATE CHANGE.

MISSING:
Where probability resolution occurred in this API generation: Xsolla-side, partner-side, or elsewhere.

The endpoint does not expose the random algorithm in the retrieved documentation.

BOUNDARY:
The API proves that Xsolla exposed a programmatic loot-box-opening operation. It does not establish the randomness implementation or why the operation was deprecated.

CITATION TRAIL:
[[XSOLLA-EXOSKELETON-010]]
→ commerce infrastructure
→ deprecated loot-box API
→ representational stripping

[[RNG-002]]
→ RNG-to-outcome mapping
→ inventory state transition

TEST:
Recover the earlier Xsolla Store API loot-box specification and trace:

PURCHASE
→ INVENTORY BOX
→ OPEN REQUEST
→ RANDOM SELECTION
→ REWARD
→ INVENTORY UPDATE.

Locate exactly where randomness occurred and which system possessed the probability table.

PLATFORM:
[[The box is an interface fiction over a state transition]]

LINKS:
[[XSOLLA-EXOSKELETON-010]]
[[RNG-002]]
[[GAMBLING-TOPOLOGY-014]]

BIBTEX:
@misc{xsolla_open_lootbox_api,
  author = {{Xsolla}},
  title = {Store API v1: Open Loot Box},
  url = {https://developers.xsolla.com/store-api/v1/loot-boxes/loot-boxes/open-loot-box/},
  note = {Deprecated API; accessed 2026-08-17}
}