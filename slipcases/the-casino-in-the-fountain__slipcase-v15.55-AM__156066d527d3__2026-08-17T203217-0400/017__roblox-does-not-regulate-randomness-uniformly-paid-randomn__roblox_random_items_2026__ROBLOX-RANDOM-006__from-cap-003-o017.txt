ZETTEL

ID:
ROBLOX-RANDOM-006

TITLE:
Roblox does not regulate “randomness” uniformly: paid randomness can be conditional while advertising rewards must be predetermined.

SOURCE:
Roblox — Terms of Use; Advertising Standards — 2026.

SOURCE URL:
https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use

PASSAGE:
[PARAPHRASE]
Creators offering Random Virtual Items must disclose acquisition odds; Roblox separately requires rewarded-video rewards to be predetermined rather than random.

RESEARCH OBJECT:
The governed object is not RANDOMNESS alone.

The platform distinguishes the pathway by which chance is attached to value.

LOCAL MOVE:
Roblox permits some random-item mechanisms under disclosure and user/jurisdiction constraints while categorically removing random rewards from rewarded-video advertising.

SOURCE TERMS:
Random Virtual Item
odds
transaction
Rewarded Video
pre-determined
chance-based mechanics

WHAT BECAME STRANGE:
The same algorithmic primitive:

RANDOM_SELECT(items)

changes governance category depending on what operation precedes it.

PAY → RANDOM
and
WATCH AD → RANDOM

are not treated identically.

QUESTION:
Where exactly does randomness become problematic?

DEEPER QUESTION:
Should platform regulation be modeled over isolated mechanics or over complete transaction chains?

MECHANISM:
PAID PATH:
<USER VALUE>
→ [TRANSACTION]
→ <RANDOM ITEM>
→ disclosure/policy constraints

AD PATH:
<USER ATTENTION>
→ [WATCH AD]
→ <REWARD>
→ RANDOMNESS FORBIDDEN

FORMAL SHIFT:
<RANDOMNESS>
→ <RANDOMNESS-IN-A-TRANSACTION-TOPOLOGY>
→ [CLASSIFY]
→ <DIFFERENT POLICY>

SOURCE FORMALISM:
Roblox Terms require disclosure of odds for Random Virtual Items.

Roblox Advertising Standards require rewarded-video rewards to be predetermined.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

POLICY(randomness, exchange_type)

not:

POLICY(randomness)

TENSION:
If chance itself were the prohibited property, both systems would receive the same treatment.

They do not.

MISSING:
The normative rationale for why these transaction paths receive different restrictions is not fully stated in the cited rules.

BOUNDARY:
This does not show paid loot boxes are unrestricted. They remain subject to disclosure and player-specific policy restrictions.

CITATION TRAIL:
Roblox random items
Roblox advertising rules
FTC dark-pattern work
rewarded advertising research
gacha regulation

TEST:
Build a matrix:

REAL MONEY
ROBUX
EARNED CURRENCY
AD VIEW
GAMEPLAY
FREE CLAIM

×

DETERMINISTIC REWARD
RANDOM REWARD

Then map Roblox's policy for every cell.

PLATFORM:
[[Mechanics acquire meaning from transaction topology]]

LINKS:
[[ROBLOX-LAW-005]]
[[Lootbox topology]]
[[Randomness is not one operation]]

BIBTEX:
@misc{roblox_random_items_2026,
  author = {{Roblox Corporation}},
  title = {Roblox Terms of Use and Advertising Standards},
  year = {2026},
  url = {https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use}
}