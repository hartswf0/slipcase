ZETTEL

ID:
XSOLLA-EXOSKELETON-010

TITLE:
Xsolla's Web Shop lets the purchase leave the game while the purchased object stays inside it.

SOURCE:
Xsolla — “Xsolla launches Buy Button for mobile games” — 2025.

SOURCE URL:
https://xsolla.com/newsroom/xsolla-launches-buy-button-for-mobile-games-to-help-developers-take-back-control-of-their-revenue

PASSAGE:
[PARAPHRASE]
An in-game link can open browser checkout for virtual items, currency, or bundles and synchronize those offers with the game.

RESEARCH OBJECT:
Commerce and world-state can be spatially separated.

The user exits the game's rendering environment to transact, yet the consequence returns to the game as an inventory or currency mutation.

LOCAL MOVE:
Xsolla externalizes the payment interface while retaining continuity with in-game identity, catalog, LiveOps, rewards, and purchases.

SOURCE TERMS:
external link
browser-based checkout
virtual items
currencies
bundles
catalog synchronization
LiveOps
Merchant of Record

WHAT BECAME STRANGE:
The shop does not have to be inside the world for the transaction to alter the world.

QUESTION:
Where does an in-game purchase occur?

DEEPER QUESTION:
If payment moves to another interface, company, browser context, and legal stack while its effects return to the game, is commerce part of the world or infrastructure around it?

MECHANISM:
<IN-GAME OFFER>
→ [LINK]
→ <WEB CHECKOUT>
→ [PAYMENT]
→ <ENTITLEMENT>
→ [SYNC]
→ <IN-GAME STATE CHANGE>

FORMAL SHIFT:
<3D / GAME COMMERCE UI>
→ <2D WEB COMMERCE>
→ [TRANSACT]
→ <GAME OBJECT>

SOURCE FORMALISM:
Xsolla describes:
browser checkout
catalog synchronization
Merchant-of-Record handling
LiveOps synchronization
parental controls
multi-channel commerce.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD_ACTION:
buy(sword)

may compile to:

leave_rendering()
→ authenticate_web()
→ transact()
→ issue_entitlement()
→ return()
→ inventory += sword

TENSION:
“Leaving the game” visually does not mean leaving the game's economy.

The economic world can extend farther than the rendered world.

MISSING:
Exactly which player identifiers and entitlement messages establish continuity between the game client and web checkout for each implementation.

BOUNDARY:
Xsolla's claims describe its commerce architecture and product capabilities; they do not imply every game implements identical flows.

CITATION TRAIL:
Xsolla Web Shop
Apple anti-steering litigation
Epic v. Apple
Merchant of Record
cross-platform entitlements

TEST:
Trace one item purchase byte-by-byte:

GAME OFFER
→ URL
→ AUTH TOKEN
→ CART
→ PAYMENT
→ WEBHOOK
→ INVENTORY DATABASE
→ GAME CLIENT

Mark every change of interface, operator, jurisdiction, and datatype.

PLATFORM:
[[The world has a commercial exoskeleton]]

LINKS:
[[2D commerce / 3D consequence]]
[[KANEVA-DIM-001]]
[[Transaction topology]]

BIBTEX:
@misc{xsolla2025buybutton,
  author = {{Xsolla}},
  title = {Xsolla launches Buy Button for mobile games to help developers take back control of their revenue},
  year = {2025},
  url = {https://xsolla.com/newsroom/xsolla-launches-buy-button-for-mobile-games-to-help-developers-take-back-control-of-their-revenue}
}