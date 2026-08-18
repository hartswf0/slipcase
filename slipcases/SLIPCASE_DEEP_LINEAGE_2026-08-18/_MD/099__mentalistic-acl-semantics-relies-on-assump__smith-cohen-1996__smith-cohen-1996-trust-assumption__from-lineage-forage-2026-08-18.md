ZETTEL

ID:
smith-cohen-1996-trust-assumption

TITLE:
Mentalistic ACL semantics relies on assumptions about agents communicating in good faith.

SOURCE:
Ira A. Smith and Philip R. Cohen — “Toward a Semantics for an Agent Communications Language Based on Speech-Acts” — 1996 — AAAI-96

SOURCE URL:
https://cdn.aaai.org/AAAI/1996/AAAI96-004.pdf

PASSAGE:
[SOURCE SUMMARY] The paper assumes cooperative/good-faith message use so that communicative acts and their intended mental effects can support coordination.

RESEARCH OBJECT:
TRUST AS A PRECONDITION OF PRIVATE-STATE SEMANTICS

LOCAL MOVE:
Treat honesty/cooperation assumptions as part of semantic architecture rather than a background convenience.

SOURCE TERMS:
good faith; belief; intention; communication; coordination

WHAT BECAME STRANGE:
A formally defined communication language can still require a social assumption that cannot be inferred from message syntax.

QUESTION:
Can a standard distinguish semantic compliance from sincerity?

DEEPER QUESTION:
What should happen when autonomous agents strategically exploit the gap between public messages and private attitudes?

MECHANISM:
<message> + <good-faith assumption> → [INFER ATTITUDE/EFFECT] → <coordination>

FORMAL SHIFT:
formal message semantics → formal semantics plus trust assumption

SOURCE FORMALISM:
Mentalistic logical semantics; trust assumption is an interpretive condition on use.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Public trace does not entail private attitude unless TRUST_BRIDGE is assumed.

TENSION:
Autonomy makes strategic divergence plausible; interoperability requires a basis that remains usable under divergence.

MISSING:
Failure semantics for deceptive or merely non-cooperative agents.

BOUNDARY:
The paper’s formal contribution remains real even if the trust assumption limits deployment scope.

CITATION TRAIL:
Shoham good-faith constraints → Smith/Cohen → Singh critique → public commitments

TEST:
Create identical public traces from sincere and insincere agents and ask what the standard can actually verify.

PLATFORM:
[[private-to-public-semantics]]

LINKS:
[[shoham-1993-good-faith-obligation]]
[[singh-1998-public-perspective-testability]]

BIBTEX:
@inproceedings{smithcohen1996semantics, author={Smith, Ira A. and Cohen, Philip R.}, title={Toward a Semantics for an Agent Communications Language Based on Speech-Acts}, booktitle={Proceedings of AAAI-96}, year={1996}, pages={24--31}, publisher={AAAI Press}}
