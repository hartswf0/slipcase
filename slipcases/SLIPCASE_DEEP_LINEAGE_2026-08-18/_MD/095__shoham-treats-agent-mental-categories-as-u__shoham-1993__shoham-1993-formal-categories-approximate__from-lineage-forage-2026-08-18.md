ZETTEL

ID:
shoham-1993-formal-categories-approximate

TITLE:
Shoham treats agent mental categories as useful approximations, not a uniquely correct ontology.

SOURCE:
Yoav Shoham — “Agent-oriented programming” — 1993 — Artificial Intelligence 60(1):51–92

SOURCE URL:
https://www.sciencedirect.com/science/article/pii/0004370293900349

PASSAGE:
[SOURCE SUMMARY] Shoham cautions that correspondence between formal agent categories and commonsense mental notions is approximate and allows that different applications may require different category sets and interpreters.

RESEARCH OBJECT:
EXPLICIT NON-IDENTITY BETWEEN FORMAL CATEGORY AND SOCIAL CONCEPT

LOCAL MOVE:
Recover the source’s own warning against reifying the formal ontology.

SOURCE TERMS:
formal category; common sense; approximation; interpreter; application

WHAT BECAME STRANGE:
The programming paradigm is more epistemically modest than later summaries that treat belief, intention, or promise as mechanically captured.

QUESTION:
Can a language expose that one of its primitives is an application-specific approximation rather than a universal type?

DEEPER QUESTION:
What happens to interoperability when different systems legitimately formalize the same social concept differently?

MECHANISM:
<commonsense concept> → [APPLICATION-SPECIFIC FORMALIZATION] → <computable category>

FORMAL SHIFT:
natural/social concept → explicitly approximate computational type

SOURCE FORMALISM:
AOP language and interpreter; the qualification concerns interpretation of its formal categories.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
formal_type ≠ social_concept; relation = MODEL_OF(scope,assumptions).

TENSION:
Standardization pressures systems toward shared categories even when the source admits there may be no uniquely right set.

MISSING:
A provenance mechanism recording which interpretation authorized each formal communicative type.

BOUNDARY:
Approximation does not make the categories arbitrary; they remain formally defined within the programming system.

CITATION TRAIL:
Shoham caveat → FIPA standardization → Singh critique of standard semantics

TEST:
Implement two interoperable agents with different internal ontologies but the same public commitment protocol.

PLATFORM:
[[formalization-remainder]]

LINKS:
[[graph-2026-lossy-formalization]]
[[singh-1998-public-perspective-testability]]

BIBTEX:
@article{shoham1993aop, author={Shoham, Yoav}, title={Agent-oriented programming}, journal={Artificial Intelligence}, year={1993}, volume={60}, number={1}, pages={51--92}, doi={10.1016/0004-3702(93)90034-9}}
