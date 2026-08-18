ZETTEL

ID:
shoham-1993-good-faith-obligation

TITLE:
Executable mentalistic communication depends on behavioral assumptions linking internal attitudes to action.

SOURCE:
Yoav Shoham — “Agent-oriented programming” — 1993 — Artificial Intelligence 60(1):51–92

SOURCE URL:
https://www.sciencedirect.com/science/article/pii/0004370293900349

PASSAGE:
[SOURCE SUMMARY] The AOP framework uses consistency/good-faith style constraints connecting commitments, capabilities, and subsequent behavior so that intentional categories have operational consequences.

RESEARCH OBJECT:
GOOD-FAITH ASSUMPTION AS HIDDEN SEMANTIC GLUE

LOCAL MOVE:
Surface the assumptions required to make private mental-state semantics predict public behavior.

SOURCE TERMS:
commitment; capability; consistency; honesty; action; agent

WHAT BECAME STRANGE:
Formal semantics does not remove trust; it can relocate trust into axioms about how agents connect mental state to action.

QUESTION:
Which protocol properties fail when an agent lies about or violates its represented mental state?

DEEPER QUESTION:
Should a communication standard specify internal rationality constraints or only externally observable normative consequences?

MECHANISM:
<private attitude> + <good-faith/rationality constraints> → [ACTION] → <observable trace>

FORMAL SHIFT:
mental-state semantics → behavioral consequence via auxiliary assumptions

SOURCE FORMALISM:
AOP imposes constraints on permitted agent methods/mental-state transitions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PRIVATE_SEMANTICS is operationally useful only under BRIDGE_AXIOMS(private_state, public_behavior).

TENSION:
The stronger the bridge axioms, the less autonomy the supposedly autonomous agent retains.

MISSING:
Exact catalogue of AOP bridge assumptions and how later ACL work relaxes them.

BOUNDARY:
This card does not claim Shoham assumes perfect honesty in every possible AOP system.

CITATION TRAIL:
AOP mental state → Smith/Cohen good-faith assumptions → Singh public-semantics critique

TEST:
Construct a conforming message trace with intentionally false private beliefs and test whether external compliance remains decidable.

PLATFORM:
[[private-to-public-semantics]]

LINKS:
[[smith-cohen-1996-trust-assumption]]
[[singh-1998-private-intention-normative-limit]]

BIBTEX:
@article{shoham1993aop, author={Shoham, Yoav}, title={Agent-oriented programming}, journal={Artificial Intelligence}, year={1993}, volume={60}, number={1}, pages={51--92}, doi={10.1016/0004-3702(93)90034-9}}
