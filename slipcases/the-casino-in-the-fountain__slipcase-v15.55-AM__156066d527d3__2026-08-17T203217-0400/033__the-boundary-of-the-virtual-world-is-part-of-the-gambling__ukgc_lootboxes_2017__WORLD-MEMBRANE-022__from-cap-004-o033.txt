ZETTEL

ID:
WORLD-MEMBRANE-022

TITLE:
The boundary of the virtual world is part of the gambling machine.

SOURCE:
UK Gambling Commission — “Loot boxes within video games” — 2017, updated 2021.
Linden Lab — Policy Regarding Wagering in Second Life.
Mojang Studios — Minecraft Usage Guidelines.

PASSAGE:
[PARAPHRASE] The UK Gambling Commission identifies cash-out capability as a key factor in determining whether chance-acquired in-game items become money or money's worth. Linden Lab similarly distinguishes non-convertible novelty objects. Minecraft explicitly requires server currencies not to cross into other servers or real-world currency.

RESEARCH OBJECT:
The decisive mechanism may sit nowhere near the RNG.

It can sit at the BORDER.

The same chance mechanism acquires a different economic or regulatory character depending upon whether its output can leave the world.

LOCAL MOVE:
Three different governance systems make permeability load-bearing.

The question shifts from:

HOW RANDOM IS THE BOX?

to:

WHERE CAN THE RESULT GO?

SOURCE TERMS:
money or money's worth
cashed out
confined
converted
novelty objects
real-world value
transferred across servers

WHAT BECAME STRANGE:
The world boundary is not passive scenery around the economic system.

It participates causally in the economic system.

QUESTION:
Should convertibility be modeled as part of the gambling mechanism itself?

DEEPER QUESTION:
Could the same randomizer become a fundamentally different social machine merely by adding one outbound edge from virtual object to external value?

MECHANISM:
SYSTEM A:

PAY
→ CHANCE
→ OBJECT
→ [WORLD MEMBRANE: CLOSED]

SYSTEM B:

PAY
→ CHANCE
→ OBJECT
→ [WORLD MEMBRANE: PERMEABLE]
→ MONEY / MONEY'S WORTH

FORMAL SHIFT:
<GAMBLING MECHANIC LOCATED IN RNG>
→ <GAMBLING MECHANIC DISTRIBUTED ACROSS RNG + ECONOMY + WORLD BOUNDARY>
→ [ADD EXIT]
→ <NEW REGULATORY OBJECT>

SOURCE FORMALISM:
UK Gambling Commission:
chance-acquired items confined to the game and unable to cash out are unlikely to constitute licensable gambling on that basis.

Linden Lab:
non-convertible novelty-object payouts are treated differently from convertible value.

Minecraft:
server currency must not be cashable, cross-server transferable, or real-world convertible.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

MECHANIC :=
{
    consideration,
    randomizer,
    reward,
    transfer_graph
}

not:

MECHANIC := randomizer

Classification may therefore change when:

randomizer₁ = randomizer₂
reward₁ = reward₂
consideration₁ = consideration₂

but:

transfer_graph₁ ≠ transfer_graph₂.

TENSION:
A player may experience both systems identically at the moment of opening.

Their downstream economic topology may nevertheless make them different regulatory objects.

MISSING:
How to incorporate unofficial markets, account sales, gifting, creator cash-out, and grey-market exchange without collapsing every desirable virtual object into “money's worth.”

BOUNDARY:
These sources come from different institutional regimes and cannot simply be treated as one common legal rule.

Their convergence is conceptual: each makes boundaries and convertibility consequential.

CITATION TRAIL:
[[LOOTBOX-BORDER-008]]
→ UK Gambling Commission
→ [[SECOND-LIFE-NOVELTY-016]]
→ [[MINECRAFT-GAMBLING-021]]
→ transfer topology as mechanism

TEST:
Build a minimal simulation where every parameter is fixed except transferability.

Add exchange edges one at a time:

NONE
GIFT
PLAYER TRADE
PLATFORM RESALE
CROSS-WORLD TRANSFER
FIAT CASHOUT
UNOFFICIAL CASH MARKET
CREATOR-ONLY CASHOUT.

For each graph, rerun legal, economic, and behavioral classification.

PLATFORM:
[[The membrane is machinery]]

LINKS:
[[LOOTBOX-BORDER-008]]
[[SECOND-LIFE-NOVELTY-016]]
[[MINECRAFT-MONEY-007]]
[[ROBLOX-CASHOUT-018]]

BIBTEX:
@misc{ukgc_lootboxes_2017,
  author = {{UK Gambling Commission}},
  title = {Loot Boxes within Video Games},
  year = {2017},
  url = {https://www.gamblingcommission.gov.uk/news/article/loot-boxes-within-video-games},
  note = {Updated 2021}
}

@misc{linden_wagering_policy,
  author = {{Linden Lab}},
  title = {Policy Regarding Wagering in Second Life},
  url = {https://wiki.secondlife.com/wiki/Linden_Lab_Official:Policy_Regarding_Wagering_in_Second_Life}
}

@misc{minecraft_usage_guidelines_2026,
  author = {{Mojang Studios}},
  title = {Minecraft Usage Guidelines},
  year = {2026},
  url = {https://www.minecraft.net/en-us/usage-guidelines}
}