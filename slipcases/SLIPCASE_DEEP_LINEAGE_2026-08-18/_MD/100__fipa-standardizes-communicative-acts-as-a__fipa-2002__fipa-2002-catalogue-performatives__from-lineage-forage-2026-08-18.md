ZETTEL

ID:
fipa-2002-catalogue-performatives

TITLE:
FIPA standardizes communicative acts as a shared machine-readable catalogue.

SOURCE:
Foundation for Intelligent Physical Agents — FIPA Communicative Act Library Specification — 2002 — SC00037J

SOURCE URL:
https://www.fipa.org/specs/fipa00037/SC00037J.html

PASSAGE:
[SOURCE SUMMARY] The specification enumerates standardized communicative acts including request, refuse, propose, agree, inform, confirm, query, and others for interoperable agent communication.

RESEARCH OBJECT:
STANDARDIZED ILLOCUTIONARY VOCABULARY

LOCAL MOVE:
Follow explicit performative categories from philosophy into an interoperability standard.

SOURCE TERMS:
communicative act; request; refuse; propose; agree; inform; standard; interoperability

WHAT BECAME STRANGE:
A category of speech becomes an infrastructure-level type whose identifier is expected to mean the same thing across independently built programs.

QUESTION:
What has to be standardized beyond the act name for cross-system meaning to survive?

DEEPER QUESTION:
Does a universal act catalogue suppress domain-specific forms of commitment or provide the minimal shared layer beneath them?

MECHANISM:
<FIPA act type + content + participants> → [INTERPRET UNDER STANDARD SEMANTICS] → <expected rational/mental effect>

FORMAL SHIFT:
explicit performative → standardized protocol token

SOURCE FORMALISM:
The specification defines a library of communicative acts with formal semantic descriptions and compositional use in interaction protocols.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ACT_TYPE is a standardized symbol; semantic interoperability requires shared interpretation of its FP/RE clauses.

TENSION:
Standard naming improves interoperability while increasing the stakes of whatever ontology the standard chooses.

MISSING:
Empirical evidence about divergent implementations of the same FIPA act semantics.

BOUNDARY:
The catalogue is not a claim that human conversation consists only of these acts.

CITATION TRAIL:
Austin/Searle explicit acts → AOP/ACL research → FIPA Communicative Act Library

TEST:
Compare three FIPA-compliant implementations of REFUSE and inspect whether identical message types produce the same public consequences.

PLATFORM:
[[speech-act-to-instruction]]

LINKS:
[[austin-1962-explicitness-force]]
[[shoham-1993-speech-act-primitives]]
[[fipa-2002-feasibility-rational-effect]]

BIBTEX:
@techreport{fipa2002cal, author={{Foundation for Intelligent Physical Agents}}, title={FIPA Communicative Act Library Specification}, institution={FIPA}, year={2002}, number={SC00037J}, url={https://www.fipa.org/specs/fipa00037/SC00037J.html}}
