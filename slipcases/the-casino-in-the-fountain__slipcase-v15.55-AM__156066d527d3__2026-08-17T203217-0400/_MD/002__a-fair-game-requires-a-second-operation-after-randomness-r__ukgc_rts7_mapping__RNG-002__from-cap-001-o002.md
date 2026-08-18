ZETTEL

ID: RNG-002

TITLE:
A fair game requires a second operation after randomness: random numbers must be mapped into outcomes.

SOURCE:
UK Gambling Commission — Remote Gambling and Software Technical Standards — RTS 7B: Generation of Random Outcomes — current version, accessed 2026-08-17.

SOURCE URL:
https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes

PASSAGE:
[QUOTE] “The mapping of the random inputs to game outcomes should be in accordance with prevailing probabilities, pay tables, etc.”

RESEARCH OBJECT:
Randomness alone cannot make a game fair. Between RNG output and what the player experiences lies a mapping operation that converts random inputs into game outcomes according to probabilities and pay tables.

LOCAL MOVE:
RTS 7B separates generation of randomness from implementation of game rules.

SOURCE TERMS:
random inputs
game outcomes
prevailing probabilities
pay tables
mapping
scaled
rules

WHAT BECAME STRANGE:
“The RNG decides what happens” is technically too compressed. The RNG produces inputs. Another mechanism decides what those inputs mean inside the game.

QUESTION:
Where exactly does chance become meaning?

DEEPER QUESTION:
When a representation-producing machine feeds another machine that assigns consequences to those representations, which layer should be treated as the locus of fairness?

MECHANISM:
<RANDOM NUMBER>
→ mapping / scaling
→ [APPLY GAME RULES + PAY TABLE]
→ <GAME OUTCOME>

FORMAL SHIFT:
<UNDifferentiated CHANCE>
→ <RANDOM INPUT>
→ [MAP THROUGH GAME MODEL]
→ <PLAYER-VISIBLE EVENT + PAYOUT>

SOURCE FORMALISM:
RTS 7 distinguishes:
1. generation of random outputs,
2. scaling,
3. mapping random inputs to game outcomes,
4. application of probabilities/pay tables,
5. presentation of the resulting game event.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

R := RNG()
I := SCALE(R, required_range)
O := GAME_MAP(I, rules, paytable)
P := SETTLE(O)

Fairness cannot therefore be tested solely as a property of R.

TENSION:
The uploaded source treats the RNG as the mechanism guaranteeing the outcome of each round is random. fileciteturn0file0L68-L82 The regulatory architecture exposes additional transformations between generated number and experienced result.

MISSING:
The regulatory text specifies that mapping must correspond to declared probabilities and pay tables but does not reduce all possible implementations to a single algorithm.

BOUNDARY:
This does not show that the RNG is unimportant. It shows that RNG correctness is necessary but insufficient for game-level fairness.

CITATION TRAIL:
UK Gambling Commission RTS 7A–7D.
UK Gambling Commission Remote Gambling Equipment architecture.
Independent test-house documentation distinguishing RNG testing from game-math testing.

TEST:
Construct a toy game with a perfectly uniform RNG but deliberately biased RNG-to-outcome mapping. Test whether output randomness remains statistically valid while player outcome probabilities become unfair.

PLATFORM:
[[Representation becomes consequence through mapping]]

LINKS:
[[RNG-001]]
[[Fairness is architectural]]
[[The map between number and event]]

BIBTEX:
@misc{ukgc_rts7_mapping,
  author       = {{UK Gambling Commission}},
  title        = {RTS 7 -- Generation of Random Outcomes},
  howpublished = {Remote Gambling and Software Technical Standards},
  url          = {https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes},
  note         = {Accessed 2026-08-17}
}