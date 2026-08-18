ZETTEL

ID:
MINECRAFT-MONEY-007

TITLE:
Minecraft protects the boundary of a server by forbidding its virtual currency from crossing it.

SOURCE:
Mojang Studios — Minecraft Usage Guidelines — current version.

SOURCE URL:
https://www.minecraft.net/en-us/usage-guidelines

PASSAGE:
[PARAPHRASE]
Server currencies may be sold but cannot be cashed out, transferred between servers, or converted to real-world currency.

RESEARCH OBJECT:
Minecraft permits a virtual economy partly by requiring that its money remain provincial.

The server economy is protected from interoperability.

LOCAL MOVE:
Mojang defines acceptable server currency through negative convertibility conditions.

SOURCE TERMS:
virtual currencies
real-world value
cashed out
transferred across other servers
converted
server

WHAT BECAME STRANGE:
Metaverse discourse often treats interoperability as an unquestioned good.

Minecraft's commercial rules make ECONOMIC NON-INTEROPERABILITY a safety boundary.

QUESTION:
Why must money stop at the edge of the world?

DEEPER QUESTION:
Does a virtual world become safer precisely when some representations cannot escape it?

MECHANISM:
<REAL MONEY>
→ [PURCHASE]
→ <SERVER CURRENCY>
→ [SPEND LOCALLY]

FORBIDDEN:

<SERVER CURRENCY>
-X→ <OTHER SERVER>

<SERVER CURRENCY>
-X→ <REAL MONEY>

FORMAL SHIFT:
<CURRENCY>
→ <WORLD-BOUNDED TOKEN>
→ [REMOVE CONVERTIBILITY]
→ <LOCAL ECONOMY>

SOURCE FORMALISM:
Minecraft requires server virtual currencies to:
- lack real-world value,
- be non-cashable,
- be non-transferable across servers,
- be non-convertible to real-world currency.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

currency c belongs_to world W

valid(c) only if:

cashout(c) = false
transfer(c, W₂) = false
real_value(c) = null

TENSION:
Interoperable asset proposals seek:

OBJECT_W1 → OBJECT_W2.

Minecraft's rules intentionally block an analogous transformation for server currencies.

MISSING:
How these restrictions are enforced technically across independent Java servers.

BOUNDARY:
Minecraft does permit monetization and some gameplay-affecting entitlements; the rules do not prohibit all server economies.

CITATION TRAIL:
Minecraft Usage Guidelines
Minecoins
Minecraft Marketplace
server monetization history
Tebex
Xsolla server commerce

TEST:
Compare twenty large Minecraft servers.

For each currency ask:

PURCHASEABLE?
TRADEABLE?
TRANSFERABLE?
CASHABLE?
REFUNDABLE?
SERVER-BOUND?

Determine whether world boundaries are more strongly enforced economically than spatially.

PLATFORM:
[[A world is partly defined by what cannot cross its border]]

LINKS:
[[Economic membrane]]
[[Lootbox convertibility]]
[[Metaverse interoperability opposition]]

BIBTEX:
@misc{mojang_usage_guidelines,
  author = {{Mojang Studios}},
  title = {Minecraft Usage Guidelines},
  url = {https://www.minecraft.net/en-us/usage-guidelines},
  note = {Accessed 2026-08-17}
}