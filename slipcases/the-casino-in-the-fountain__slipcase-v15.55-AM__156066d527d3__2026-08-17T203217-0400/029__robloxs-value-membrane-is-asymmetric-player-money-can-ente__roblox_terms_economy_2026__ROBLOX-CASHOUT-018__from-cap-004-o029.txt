ZETTEL

ID:
ROBLOX-CASHOUT-018

TITLE:
Roblox's value membrane is asymmetric: player money can enter a random-item economy while creator earnings can leave as dollars.

SOURCE:
Roblox Corporation — Roblox Terms of Use — 2026.
Roblox Corporation — Developer Exchange Terms of Use — current 2026 version.

PASSAGE:
[PARAPHRASE] Roblox permits location-dependent Random Virtual Items acquired with Robux or otherwise. Separately, eligible creators may convert qualifying Earned Robux—including Robux earned from in-game virtual-product purchases—into real money through DevEx.

RESEARCH OBJECT:
“Can it cash out?” is not one question.

Cash-out capability depends on ACTOR and PROVENANCE.

A player may spend Robux on an in-experience transaction.

Robux received by the creator through compliant monetization may become Earned Robux and enter DevEx.

The economic membrane therefore has direction.

LOCAL MOVE:
Roblox distinguishes Robux not merely by numerical denomination but by how they were obtained.

SOURCE TERMS:
Random Virtual Item
Robux
Earned Robux
DevEx
Cash Out
in-game purchases
virtual products
creator

WHAT BECAME STRANGE:
Two numerically identical Robux balances can have different relationships to real money because one is classified as Earned Robux and the other is not.

Money itself acquires provenance.

QUESTION:
Can convertibility be actor-relative and history-dependent?

DEEPER QUESTION:
What happens to gambling analysis when money's path OUT of the system exists for the seller but not necessarily for the purchaser holding the randomized prize?

MECHANISM:
<PLAYER REAL MONEY>
→ <ROBUX>
→ [RANDOMIZED PURCHASE]
→ <VIRTUAL ITEM>

simultaneously:

<PLAYER PURCHASE>
→ <CREATOR EARNED ROBUX>
→ [DEVEX IF ELIGIBLE]
→ <REAL MONEY>

FORMAL SHIFT:
<CURRENCY HAS VALUE>
→ <CURRENCY TOKEN HAS PROVENANCE>
→ [CLASSIFY EARNING SOURCE + ACTOR]
→ <CASHABLE | NON-CASHABLE>

SOURCE FORMALISM:
DevEx distinguishes Earned Robux from:
- directly purchased Robux,
- gift-card Robux,
- Premium grants,
- certain trading/resale proceeds,
and permits qualifying Earned Robux to be cashed out subject to eligibility and Roblox discretion.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CASHABLE(amount, actor, provenance)

not:

CASHABLE(currency)

Value is typed:

Robux<Purchased>
Robux<Earned>
Robux<Resale>
Robux<Grant>

TENSION:
Loot-box analysis often asks whether the prize possessed by the PLAYER is cashable.

But platform economies may send real-money value out through a different actor entirely: the CREATOR.

MISSING:
How consumer-protection and gambling frameworks should model asymmetric convertibility where payers and beneficiaries occupy different sides of the exchange graph.

BOUNDARY:
DevEx does not mean every Robux earned through every transaction can be cashed out. Roblox defines eligibility and qualifying Earned Robux narrowly and retains discretion.

CITATION TRAIL:
[[LOOTBOX-BORDER-008]]
→ convertibility
→ Roblox DevEx
→ actor-relative cashout

[[ROBLOX-RANDOM-006]]
→ paid randomized rewards
→ creator monetization

TEST:
Trace one unit of real money through:

PLAYER
→ ROBUX PURCHASE
→ RANDOM ITEM PURCHASE
→ CREATOR REVENUE
→ EARNED ROBUX
→ DEVEX
→ CREATOR BANK ACCOUNT.

Identify which edge regulators conventionally treat as the “cash-out” edge and which edges disappear from the model.

PLATFORM:
[[Money has direction and provenance]]

LINKS:
[[ROBLOX-RANDOM-006]]
[[LOOTBOX-BORDER-008]]
[[XSOLLA-ROBLOX-012]]

BIBTEX:
@misc{roblox_terms_economy_2026,
  author = {{Roblox Corporation}},
  title = {Roblox Terms of Use},
  year = {2026},
  url = {https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use}
}

@misc{roblox_devex_2026,
  author = {{Roblox Corporation}},
  title = {Developer Exchange Terms of Use},
  year = {2026},
  url = {https://en.help.roblox.com/hc/en-us/articles/115005718246-Developer-Exchange-Terms-of-Use}
}