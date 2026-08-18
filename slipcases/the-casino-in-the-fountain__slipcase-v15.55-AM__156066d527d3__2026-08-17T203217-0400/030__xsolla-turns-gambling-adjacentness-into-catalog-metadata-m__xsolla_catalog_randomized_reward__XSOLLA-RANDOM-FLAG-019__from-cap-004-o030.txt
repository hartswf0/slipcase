ZETTEL

ID:
XSOLLA-RANDOM-FLAG-019

TITLE:
Xsolla turns gambling-adjacentness into catalog metadata: “Mark as paid randomized reward.”

SOURCE:
Xsolla — Catalog Management Documentation — current documentation, accessed 2026-08-17.

PASSAGE:
[QUOTE] “Mark as paid randomized reward”

[PARAPHRASE] Xsolla instructs developers to enable this toggle when a paid currency, item, package, or bundle will participate in random-reward mechanics such as loot boxes or gacha, noting that the parameter may be required in countries with legal restrictions.

RESEARCH OBJECT:
A sprawling legal controversy eventually becomes a boolean-looking property in an item-management interface.

The product is classified BEFORE the random event occurs.

The metadata anticipates what the item will later participate in.

LOCAL MOVE:
Xsolla attaches regulatory significance not only to a loot box itself but to currencies, items, packages, and bundles that feed paid randomized-reward mechanics.

SOURCE TERMS:
paid randomized reward
toggle
virtual currency
virtual item
bundle
loot boxes
gacha
countries
legal restrictions

WHAT BECAME STRANGE:
The legal property does not belong solely to the random generator.

A currency becomes legally interesting because of its FUTURE USE.

QUESTION:
Can an object's regulatory type be determined by a mechanic it has not yet entered?

DEEPER QUESTION:
Are modern compliance systems creating a kind of effect system for game economies, where objects carry annotations describing dangerous downstream operations?

MECHANISM:
<VIRTUAL ITEM / CURRENCY / BUNDLE>
→ [ANNOTATE: PAID_RANDOMIZED_REWARD]
→ <CATALOG METADATA>
→ [JURISDICTIONAL COMPLIANCE LOGIC]
→ <AVAILABLE / RESTRICTED / ALTERED>

FORMAL SHIFT:
<LEGAL ANALYSIS IN PROSE>
→ <CATALOG ATTRIBUTE>
→ [MACHINE PROCESS]
→ <COMMERCE BEHAVIOR>

SOURCE FORMALISM:
Xsolla documentation supplies the explicit configuration operation:

Mark as paid randomized reward = enabled

for relevant paid currencies, currency packages, items, and bundles.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

type Item = {
    sku,
    price,
    ...
    paid_randomized_reward: Boolean
}

The remarkable shift is:

LEGAL CATEGORY
→ DATA FIELD.

TENSION:
Roblox exposes policy through player-specific booleans.

Xsolla exposes randomized-reward status through product metadata.

The legal system is appearing at two different locations in the stack:

PLAYER POLICY
and
OBJECT TYPE.

MISSING:
What exact checkout, availability, disclosure, or geo-restriction behaviors Xsolla automatically derives from this flag in each jurisdiction.

BOUNDARY:
Xsolla says the parameter “may be required” in countries with legal restrictions. The documentation does not establish that the toggle alone guarantees legal compliance.

CITATION TRAIL:
[[XSOLLA-EXOSKELETON-010]]
→ Xsolla catalog
→ randomized-reward toggle
→ law as metadata

[[ROBLOX-LAW-005]]
→ policy boolean
→ regulatory typing

TEST:
Trace the flag through Xsolla's APIs and storefront:

CONFIGURATION
→ CATALOG RESPONSE
→ COUNTRY DETECTION
→ CHECKOUT
→ DISPLAY
→ ENTITLEMENT.

Determine every runtime behavior that changes when only this bit changes.

PLATFORM:
[[Law becomes a datatype]]

LINKS:
[[XSOLLA-EXOSKELETON-010]]
[[ROBLOX-LAW-005]]
[[LOOTBOX-BORDER-008]]

BIBTEX:
@misc{xsolla_catalog_randomized_reward,
  author = {{Xsolla}},
  title = {Catalog Management},
  url = {https://developers.xsolla.com/items-catalog/catalog-management/},
  note = {Accessed 2026-08-17}
}