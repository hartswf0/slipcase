ZETTEL

ID:
austin-1962-promise-orders-future-conduct

TITLE:
A promise is consequential because it reorganizes what later conduct counts as in order.

SOURCE:
J. L. Austin — How to Do Things with Words — 1962 — Lectures II–IV

SOURCE URL:
https://web.english.upenn.edu/~cavitch/pdf-library/Austin_How_To_Do_Things_with_Words.pdf

PASSAGE:
[SOURCE SUMMARY] Austin distinguishes sincerity from the conventional effect of promising and analyzes the promise as committing the speaker, making some later conduct obligatory or out of order even when intention is defective.

RESEARCH OBJECT:
NORMATIVE STATE CREATED BY A SPEECH ACT

LOCAL MOVE:
Shift from the message as information to the durable normative relation created by its successful performance.

SOURCE TERMS:
promise; obligation; commitment; subsequent conduct; insincerity; infelicity

WHAT BECAME STRANGE:
The speech act can have a normative afterlife that persists after the utterance event has vanished.

QUESTION:
What is the smallest public state required to represent the continuing effect of a promise?

DEEPER QUESTION:
Does an executable promise need access to private sincerity, or can its public normative consequences be tracked independently?

MECHANISM:
<felicitous promise event> → [CREATE OBLIGATION] → <future conduct evaluated under new normative state>

FORMAL SHIFT:
event semantics → persistent normative state

SOURCE FORMALISM:
Austin analyzes entailment-like relations among performances and obligations but provides no formal commitment calculus.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROMISE(debtor,creditor,p) ⇒ create Commitment(debtor,creditor,p,status=OPEN)

TENSION:
The public persistence of obligation creates a path toward commitment semantics, while Austin’s sincerity conditions resist reducing all meaning to the public ledger.

MISSING:
A direct conceptual history from promise-as-obligation to computational social commitments.

BOUNDARY:
Austin does not equate promises with database records or define discharge/cancel/release operations.

CITATION TRAIL:
Austin promise → speech-act theory → social commitments in agent communication → Yolum/Singh protocol state

TEST:
Separate a promise’s public commitment state from its private intention and ask which protocol properties remain testable.

PLATFORM:
[[felicity-to-protocol]]

LINKS:
[[yolum-singh-2002-commitment-as-action-meaning]]
[[singh-1998-private-intention-normative-limit]]
[[coordinator-1993-incompletion-token-a]]

BIBTEX:
@book{austin1962things, author={Austin, J. L.}, title={How to Do Things with Words}, year={1962}, publisher={Clarendon Press}, address={Oxford}}
