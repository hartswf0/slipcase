ZETTEL

ID:
MINECRAFT-GAMBLING-021

TITLE:
Minecraft bans “gambling” as an all-ages world-content failure while separately engineering currencies so they cannot escape the server.

SOURCE:
Mojang Studios — Minecraft Usage Guidelines — current version, accessed 2026-08-17.

PASSAGE:
[PARAPHRASE] Minecraft permits server monetization and virtual currencies under constraints, requires those currencies to lack real-world value and cross-server/cash-out capability, and requires servers and monetization to remain suitable for all ages, explicitly listing gambling among unsuitable content.

RESEARCH OBJECT:
Minecraft attacks the gambling boundary from two directions that are usually separated:

CONTENT:
gambling is unsuitable for the all-ages environment.

ECONOMY:
server money must not become external money.

LOCAL MOVE:
Mojang does not need to supply a complete mathematical definition of loot boxes in order to constrain the space in which gambling-like economies can emerge.

It makes the server's economy deliberately provincial and the server's content deliberately all-ages.

SOURCE TERMS:
server
virtual currencies
real-world value
cashed out
transferred
all ages
gambling
trusted environment

WHAT BECAME STRANGE:
Minecraft's safest currency is, by design, a bad currency.

It cannot travel.
It cannot cash out.
It cannot become general money.

Its weakness is protective.

QUESTION:
Can economic incapacity be a platform safety feature?

DEEPER QUESTION:
What if metaverse interoperability is sometimes the dangerous operation rather than the desired one?

MECHANISM:
<REAL MONEY>
→ <SERVER CURRENCY>
→ [SPEND INSIDE SERVER]

blocked:

<SERVER CURRENCY>
-X→ <CASH>

<SERVER CURRENCY>
-X→ <OTHER SERVER>

simultaneously:

<SERVER CONTENT>
→ [ALL-AGES TEST]
→ gambling excluded

FORMAL SHIFT:
<INTEROPERABILITY AS FEATURE>
→ <NON-INTEROPERABILITY AS GOVERNANCE>
→ [BLOCK EXITS]
→ <BOUNDED ECONOMY>

SOURCE FORMALISM:
Minecraft allows in-game virtual currencies only if they:
- have no real-world value;
- cannot be cashed out;
- cannot be transferred across other servers;
- cannot be converted into real-world currency.

It separately requires server monetization/content to remain suitable for all ages and names gambling as an example of unsuitable content.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SAFE_SERVER_CURRENCY(c) requires:

CASHOUT(c) = false
CROSS_SERVER(c) = false
REAL_WORLD_CONVERT(c) = false

A currency can function locally because it fails globally.

TENSION:
Metaverse imaginaries repeatedly celebrate portable identities, assets, and currencies.

Minecraft makes portability of server currency precisely what must NOT happen.

MISSING:
How Mojang distinguishes prohibited gambling from permitted randomized gameplay or rewards that require no payment.

BOUNDARY:
The Usage Guidelines prohibit gambling in monetized/all-ages server contexts and constrain server currencies. They do not provide a comprehensive gambling-law test.

CITATION TRAIL:
[[MINECRAFT-MONEY-007]]
→ current Usage Guidelines
→ all-ages requirement
→ non-interoperability as protection

[[LOOTBOX-BORDER-008]]
→ convertibility
→ world boundary
→ safety by containment

TEST:
Take a compliant Minecraft currency and successively add:

PLAYER TRANSFER
CROSS-SERVER TRANSFER
MARKETPLACE EXCHANGE
CASHOUT
RANDOM PAID REWARDS.

Observe which addition first destroys compliance and which first changes the regulatory interpretation.

PLATFORM:
[[Some world walls are safety mechanisms]]

LINKS:
[[MINECRAFT-MONEY-007]]
[[LOOTBOX-BORDER-008]]
[[SECOND-LIFE-NOVELTY-016]]

BIBTEX:
@misc{minecraft_usage_guidelines_2026,
  author = {{Mojang Studios}},
  title = {Minecraft Usage Guidelines},
  year = {2026},
  url = {https://www.minecraft.net/en-us/usage-guidelines},
  note = {Accessed 2026-08-17}
}