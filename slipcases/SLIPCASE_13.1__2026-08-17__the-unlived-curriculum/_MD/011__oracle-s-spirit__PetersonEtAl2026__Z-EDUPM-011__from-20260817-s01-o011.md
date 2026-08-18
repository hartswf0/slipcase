ZETTEL

ID:
Z-EDUPM-011

TITLE:
A PREDICTION MARKET CAN CORRECTLY PREDICT REALITY AND STILL LOSE BECAUSE SETTLEMENT FOLLOWS THE ORACLE SPECIFICATION RATHER THAN THE EVENT'S “SPIRIT.”

SOURCE:
Jack Peterson, Joseph Krug, Micah Zoltu, Austin K. Williams, and Stephanie Alexander — Augur: a Decentralized Oracle and Prediction Market Platform (v2.0) — 2026 — Sections I.1 and III.7.

PASSAGE:
[PARAPHRASE] Augur requires market creators to specify a resolution source. Its discussion of ambiguous markets recounts a TradeSports contract concerning a North Korean missile: the launch occurred, but the contract required U.S. Department of Defense confirmation, so the market's contractual condition was not satisfied.

RESEARCH OBJECT:
Outcome settlement is not direct contact with reality.

A prediction market needs a second representational machine that decides what event counts as having happened.

LOCAL MOVE:
Augur separates:

EVENT
from
RESOLUTION SOURCE
from
REPORTED OUTCOME
from
SETTLEMENT.

The market cannot simply ask reality.

It must specify who or what is authorized to answer for reality.

SOURCE TERMS:
resolution source
designated reporter
objective reality
invalid market
ambiguous
subjective
oracle
reporting
settlement
market outcome

WHAT BECAME STRANGE:
The alleged epistemic purity of the prediction market bottoms out in a bureaucratic sentence.

The bettor does not ultimately bet:

DID X HAPPEN?

The bettor bets:

WILL X COUNT AS HAVING HAPPENED UNDER THIS RESOLUTION PROCEDURE?

That opens a much stranger educational analogy.

A university does not merely predict:

IS THIS PERSON CAPABLE?

It repeatedly constructs oracles that settle narrower propositions:

Did the rubric count this response?
Did the registrar award the credit?
Did the committee count this publication?
Did the credential satisfy this employer?
Did the accreditor recognize this program?

QUESTION:
If educational institutions are predictive infrastructures, where are their resolution sources—the procedures authorized to convert messy human capability into settleable institutional facts?

DEEPER QUESTION:
How often does the “spirit” of educational success diverge from the literal event that the institutional oracle is authorized to recognize?

MECHANISM:
real-world event
→ resolution specification
→ authorized evidence source
→ reporting
→ dispute
→ finalized outcome
→ payout

FORMAL SHIFT:
<WORLD>
→ <RESOLUTION RULE>
→ [OBSERVE THROUGH AUTHORIZED SOURCE]
→ <SETTLED EVENT>

SOURCE FORMALISM:
Augur specifies four market stages:

creation
→ trading
→ reporting
→ settlement.

At market creation, a resolution source is selected.

Ambiguous or subjective markets may resolve as Invalid.

SOURCE REALITY and CONTRACT RESOLUTION are therefore explicitly distinct parts of the architecture.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Reality:
R

Resolution function:
O(R, rule, source) → settled outcome S

Possible condition:

R = TRUE
but
S = FALSE

when the contract settles:

“authorized source confirms R”

rather than merely:

“R occurred.”

TENSION:
[[Z-EDUPM-004]] treated replication markets as a process of converting open scientific claims into settleable events.

Augur makes the hidden consequence visible:

settleability introduces an oracle, and the oracle can become the thing actually being predicted.

MISSING:
A systematic inventory of educational resolution sources and disputes where institutional settlement diverges from later assessments of capability.

BOUNDARY:
Augur is a prediction-market protocol.

Calling grading committees, registrars, accreditors, or employers “oracles” is our formal analogy, not terminology used by the source.

CITATION TRAIL:
[[Z-EDUPM-001]]
[[Z-EDUPM-004]]
→ Augur resolution source
→ ambiguous markets
→ letter / spirit divergence
→ institutional settlement

Follow:
decentralized common-knowledge oracles
contract specification
measurement theory
assessment validity
boundary objects
classification infrastructures

TEST:
Choose one educational proposition:

“Student X is competent at Y.”

Construct four possible resolution sources:

exam score,
professor judgment,
portfolio review,
employer task performance.

Ask independent evaluators to settle the identical proposition under each rule.

Measure disagreement.

The disagreement is the oracle-dependence hidden by the apparently singular credential.

PLATFORM:
[[EDUCATIONAL ORACLES]]

LINKS:
[[Z-EDUPM-001]]
[[Z-EDUPM-004]]
[[Settlement Is Not Reality]]
[[Educational Oracles]]

BIBTEX:
@misc{peterson2026augur,
  author = {Peterson, Jack and Krug, Joseph and Zoltu, Micah and Williams, Austin K. and Alexander, Stephanie},
  title  = {Augur: a Decentralized Oracle and Prediction Market Platform (v2.0)},
  year   = {2026},
  note   = {arXiv:1501.01042}
}