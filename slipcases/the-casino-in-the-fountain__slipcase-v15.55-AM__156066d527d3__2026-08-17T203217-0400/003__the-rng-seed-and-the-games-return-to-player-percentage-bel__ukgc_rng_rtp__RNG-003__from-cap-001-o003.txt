ZETTEL

ID: RNG-003

TITLE:
The RNG seed and the game’s return-to-player percentage belong to different mechanisms.

SOURCE:
UK Gambling Commission — RTS 7; Live Return to Player Performance Monitoring of Games of Chance — accessed 2026-08-17.

SOURCE URL:
https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes

PASSAGE:
[PARAPHRASE] RTS 7 treats seeds as an unpredictability problem, while theoretical RTP is defined separately as the designed return percentage of the game.

RESEARCH OBJECT:
The supplied article collapses two technical objects when it says PRNG “seed” numbers are the means of ensuring a steady RTP. Regulatory documentation instead treats seeding as part of RNG unpredictability and RTP as a designed statistical property of the game.

LOCAL MOVE:
The regulatory architecture separates initialization/state of the random generator from probabilities, pay tables, and expected financial return.

SOURCE TERMS:
seed value
seeding
re-seeding
predictability
theoretical RTP
actual RTP
expected probabilities
pay tables

WHAT BECAME STRANGE:
A seed selects or initializes a pseudorandom sequence. It is not, in the regulatory model, the object that directly specifies how much money the game is designed to return.

QUESTION:
Why is it so tempting to locate an entire probabilistic system inside its RNG?

DEEPER QUESTION:
What conceptual errors appear when architectures are described through one charismatic component—the model, algorithm, RNG, database—while the transformations around that component disappear?

MECHANISM:
SOURCE ACCOUNT:
<SEED>
→ PRNG
→ [ENSURE STEADY RTP]
→ <GAME RETURN>

REGULATORY ARCHITECTURE:
<SEED + RNG ALGORITHM>
→ [GENERATE UNPREDICTABLE INPUT]
→ <RANDOM INPUT>

<RANDOM INPUT + GAME RULES + PAYTABLE>
→ [MAP]
→ <OUTCOME DISTRIBUTION>
→ <THEORETICAL / ACTUAL RTP>

FORMAL SHIFT:
<ONE PROBABILISTIC MACHINE>
→ <RNG STATE> + <OUTCOME MAPPING> + <PAYTABLE>
→ [SEPARATE OPERATIONS]
→ <DISTINCT TESTABLE PROPERTIES>

SOURCE FORMALISM:
RTS 7A: seeding must not introduce predictability.
RTS 7B: random inputs are mapped according to probabilities and pay tables.
RTP guidance: theoretical RTP is the designed return percentage; actual RTP is calculated from operational wins and turnover.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SEED ≠ RTP

seed → RNG state
RNG state → random stream
random stream + mapping → outcome distribution
outcome distribution + payouts → theoretical RTP

TENSION:
The uploaded source explicitly states that PRNGs use “seed” numbers and claims this is “the only way” to ensure a steady RTP. fileciteturn0file0L74-L82 The regulator assigns these concerns to separate parts of the system.

MISSING:
The supplied article gives no technical derivation showing how a seed value establishes RTP.

BOUNDARY:
This zettel does not establish how every commercial gambling implementation calculates RTP. It establishes that the regulator distinguishes seeding, outcome mapping, and RTP rather than treating them as one mechanism.

CITATION TRAIL:
RTS 7A and 7B.
UKGC Live Return to Player Performance Monitoring.
Technical game-mathematics documentation from approved test houses.

TEST:
Implement the same game/paytable with many different PRNG seeds. Measure whether long-run theoretical RTP changes merely because the seed changes.

PLATFORM:
[[Do not mistake a component for the system]]

LINKS:
[[RNG-001]]
[[RNG-002]]
[[Architecture corrects vocabulary]]

BIBTEX:
@misc{ukgc_rng_rtp,
  author       = {{UK Gambling Commission}},
  title        = {RTS 7 -- Generation of Random Outcomes and Live Return to Player Performance Monitoring},
  url          = {https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes},
  note         = {Accessed 2026-08-17}
}