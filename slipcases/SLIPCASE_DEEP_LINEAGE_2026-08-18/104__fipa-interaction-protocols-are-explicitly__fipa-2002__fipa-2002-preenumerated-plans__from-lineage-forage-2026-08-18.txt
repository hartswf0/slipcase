ZETTEL

ID:
fipa-2002-preenumerated-plans

TITLE:
FIPA interaction protocols are explicitly pre-enumerated inter-agent plans.

SOURCE:
Foundation for Intelligent Physical Agents — FIPA Communicative Act Library Specification — 2002 — interaction-protocol discussion

SOURCE URL:
https://www.fipa.org/specs/fipa00037/SC00037J.html

PASSAGE:
[SOURCE SUMMARY] The specification describes interaction protocols as pre-enumerated inter-agent plans composed from communicative acts using sequencing, alternatives, and other protocol structure.

RESEARCH OBJECT:
PROTOCOL AS PRE-ENUMERATED PLAN

LOCAL MOVE:
Expose the sequence-first architecture later commitment protocols criticize.

SOURCE TERMS:
interaction protocol; pre-enumerated; plan; sequence; choice; communicative act

WHAT BECAME STRANGE:
The standard formalizes not only act meanings but also expected patterns of interaction, creating a second layer of constraint.

QUESTION:
When does a protocol plan become overconstraint rather than interoperability support?

DEEPER QUESTION:
Can semantics define obligations strongly enough that legal sequences can be generated at runtime instead of pre-enumerated?

MECHANISM:
<protocol plan> + <current point> → [SELECT ALLOWED BRANCH] → <next communicative act>

FORMAL SHIFT:
act semantics → predesigned multi-act trajectory

SOURCE FORMALISM:
Protocol compositions specify sequences/alternatives over standardized communicative acts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SEQUENCE_FIRST: traces are enumerated then executed. COMMITMENT_FIRST: traces are generated under normative constraints.

TENSION:
Pre-enumeration offers predictability and analyzability but can constrain autonomous agents under unanticipated opportunities or failures.

MISSING:
Empirical comparison of trace flexibility and verification costs between FIPA plans and commitment protocols.

BOUNDARY:
Pre-enumerated does not mean strictly linear; protocols may contain alternatives and branches.

CITATION TRAIL:
FIPA interaction protocols → Yolum/Singh critique of sequence-oriented protocols

TEST:
Add an unforeseen but commitment-preserving detour to a FIPA-style protocol and test whether it is formally legal.

PLATFORM:
[[sequence-vs-semantics]]

LINKS:
[[yolum-singh-2002-sequence-overconstraint]]
[[smith-cohen-1996-cfa-derived-not-primitive]]

BIBTEX:
@techreport{fipa2002cal, author={{Foundation for Intelligent Physical Agents}}, title={FIPA Communicative Act Library Specification}, institution={FIPA}, year={2002}, number={SC00037J}, url={https://www.fipa.org/specs/fipa00037/SC00037J.html}}
