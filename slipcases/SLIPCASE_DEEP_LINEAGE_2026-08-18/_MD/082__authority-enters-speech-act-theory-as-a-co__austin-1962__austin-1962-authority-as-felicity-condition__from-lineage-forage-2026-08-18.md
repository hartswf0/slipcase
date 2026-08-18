ZETTEL

ID:
austin-1962-authority-as-felicity-condition

TITLE:
Authority enters speech-act theory as a condition on who may make an utterance count.

SOURCE:
J. L. Austin — How to Do Things with Words — 1962 — Lectures I–II and VIII

SOURCE URL:
https://web.english.upenn.edu/~cavitch/pdf-library/Austin_How_To_Do_Things_with_Words.pdf

PASSAGE:
[SOURCE SUMMARY] Austin’s examples repeatedly require the right person in the right institutional position: the appointed ship-namer, an eligible participant in marriage, or a judge whose pronouncement operates because of office and context.

RESEARCH OBJECT:
AUTHORITY AS A SEMANTIC PRECONDITION

LOCAL MOVE:
Treat office and authorization as part of the semantics of institutional action rather than external sociology.

SOURCE TERMS:
appointed; appropriate person; judge; verdict; conventional procedure; context

WHAT BECAME STRANGE:
The same words can have different institutional effects depending on who says them, so actor identity and office are not merely metadata.

QUESTION:
Where should authority live in an executable institutional language: actor type, capability, role, credential, or contextual relation?

DEEPER QUESTION:
Can authority itself be derived recursively from prior status assignments without an infinite regress?

MECHANISM:
<actor + office + procedure + circumstance> → [AUTHORIZED PERFORMANCE] → <institutional consequence>

FORMAL SHIFT:
utterance-centered semantics → authority-sensitive transition semantics

SOURCE FORMALISM:
No formal authorization calculus is supplied by Austin.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
DECLARE(a,x,K) succeeds only if AUTHORIZED(a,x,K); otherwise it produces ATTEMPTED_ACT without the institutional effect.

TENSION:
Treating authority as a boolean predicate makes implementation possible while hiding how authority is historically produced, contested, or revoked.

MISSING:
A primary-source bridge from Austin’s appropriateness conditions to authorization in computational protocol languages.

BOUNDARY:
Austin’s examples establish dependence on office and circumstance; they do not specify a general political theory of authority.

CITATION TRAIL:
Austin 1962 → Searle declarations/status functions → workflow roles → institutional protocol guards

TEST:
Hold words constant and vary speaker office. The runtime should produce different deontic consequences without changing the utterance string.

PLATFORM:
[[authority-as-runtime]]

LINKS:
[[searle-2018-counts-as-schema]]
[[coordinator-1993-menu-semantics-a]]
[[singh-1998-social-context]]

BIBTEX:
@book{austin1962things, author={Austin, J. L.}, title={How to Do Things with Words}, year={1962}, publisher={Clarendon Press}, address={Oxford}}
