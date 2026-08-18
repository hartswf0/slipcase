ZETTEL

ID: RNG-001

TITLE:
“True randomness” becomes a regulatory threshold called “acceptable randomness.”

SOURCE:
UK Gambling Commission — Remote Gambling and Software Technical Standards — RTS 7: Generation of Random Outcomes — current version, accessed 2026-08-17.

SOURCE URL:
https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes

PASSAGE:
[QUOTE] “Random number generation and game results must be ‘acceptably random’.”

RESEARCH OBJECT:
The regulatory object is not metaphysical or mathematical proof of “true randomness.” It is an operational standard assembled from statistical distribution, unpredictability, non-repetition, safe seeding, and scaling.

LOCAL MOVE:
The Commission replaces an absolute property—randomness—with a demonstrable compliance condition: “acceptably random.”

SOURCE TERMS:
acceptably random
high degree of confidence
statistical analysis
unpredictable
seed value
seeding and re-seeding
scaling

WHAT BECAME STRANGE:
A certification does not need to establish that an RNG is “truly random” in an unrestricted sense. It needs to establish particular observable and computational properties strongly enough for the regulatory purpose.

QUESTION:
What happens when an ontological property such as RANDOM becomes a regulatory predicate defined by a finite battery of tests?

DEEPER QUESTION:
How many supposedly intrinsic properties of technical systems—fair, secure, private, explainable, random—exist operationally only through institutions specifying what counts as sufficient evidence?

MECHANISM:
<RNG>
→ statistical + computational tests
→ [COMPARE AGAINST REGULATORY CRITERIA]
→ <ACCEPTABLY RANDOM>

FORMAL SHIFT:
<RANDOMNESS AS PROPERTY>
→ <TESTABLE OUTPUT + IMPLEMENTATION CHARACTERISTICS>
→ [CERTIFY]
→ <REGULATORY ACCEPTABILITY>

SOURCE FORMALISM:
RTS 7A requires:
- distribution according to expected/theoretical probabilities
- computational unpredictability
- avoidance of repeated or synchronized streams
- seeding/re-seeding that does not introduce predictability
- scaling that preserves required qualities

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ACCEPTABLE_RANDOMNESS(R) :=
DISTRIBUTION_OK(R)
∧ UNPREDICTABLE(R)
∧ NONCYCLING(R)
∧ SEEDING_SAFE(R)
∧ SCALING_PRESERVES(R)

TENSION:
The supplied mycelium.is text describes testing as searching for statistical “patterns” and says successful testing certifies an RNG as “safe and truly random.” The regulator uses the more qualified “acceptably random” and specifies several requirements beyond absence of detectable statistical patterns. fileciteturn0file0L84-L94

MISSING:
The standard does not answer the philosophical question of whether a software RNG is “really” random. That question is unnecessary for the regulatory operation being performed.

BOUNDARY:
The evidence licenses the claim that UK gambling regulation operationalizes randomness through explicit requirements. It does not establish that all jurisdictions or testing laboratories define randomness identically.

CITATION TRAIL:
UK Gambling Commission — Testing Strategy for Compliance with Remote Gambling and Software Technical Standards.
Gaming Laboratories International — GLI-11.
Technical literature distinguishing statistical randomness, pseudorandomness, and entropy sources.

TEST:
Collect the exact randomness predicates used by five gambling regulators or test laboratories and compare whether certification converges on one formal object or produces jurisdiction-specific versions of “random.”

PLATFORM:
[[Properties become operational through tests]]

LINKS:
[[Certification constructs technical properties]]
[[Randomness as institutional object]]
[[Tests as definitions]]

BIBTEX:
@misc{ukgc_rts7_random_outcomes,
  author       = {{UK Gambling Commission}},
  title        = {RTS 7 -- Generation of Random Outcomes},
  howpublished = {Remote Gambling and Software Technical Standards},
  url          = {https://www.gamblingcommission.gov.uk/standards/remote-gambling-and-software-technical-standards/rts-7-generation-of-random-outcomes},
  note         = {Accessed 2026-08-17}
}