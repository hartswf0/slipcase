ZETTEL

ID:
Z-EDUPM-015

TITLE:
CRYPTOGRAPHICALLY VERIFIED IS NOT THE SAME AS EDUCATIONALLY VALID: THE VERIFIER REINTRODUCES JUDGMENT AFTER THE MACHINE SAYS THE CREDENTIAL IS AUTHENTIC.

SOURCE:
Manu Sporny, Dave Longley, David Chadwick, and Ivan Herman — Verifiable Credentials Data Model v2.0 — 2025 — W3C Recommendation — Appendix A, Validation.

PASSAGE:
[PARAPHRASE] The W3C specification separates cryptographic verification from later validation questions such as validity period, status, schema, trust in the issuer, and fitness for the verifier's purpose.

RESEARCH OBJECT:
Machine-verifiable credentials do not eliminate judgment.

They relocate judgment from “is this document authentic?” to “what should this authentic claim count for here?”

LOCAL MOVE:
The specification explicitly refuses to collapse technical proof into fitness for purpose.

A credential can be cryptographically intact yet still fail the verifier's application-specific requirements.

SOURCE TERMS:
verification
validation
fitness for purpose
verifier
issuer
claims
cryptographic proof
status
validity period
trust

WHAT BECAME STRANGE:
The dream of an “un-gameable credential” contains a category error.

Cryptography can answer questions like:

Was this claim altered?
Who signed it?
Is the proof valid?

It cannot automatically answer:

Does this qualification make this person good at this job?
Should this badge count as equivalent to that degree?
Does this old achievement still matter?
Do we trust this issuer?
Is this the kind of evidence we care about?

The supposedly objective credential ends by returning authority to interpretation.

QUESTION:
If machine verification cannot establish fitness for purpose, does finer-grained credentialization actually eliminate institutional gatekeepers—or multiply the number of moments at which gatekeepers must interpret claims?

DEEPER QUESTION:
Could the future credential economy automate authenticity while making meaning more contested?

MECHANISM:
credential presented
→ cryptographic verification
→ status / validity checks
→ issuer trust judgment
→ fitness-for-purpose judgment
→ application-specific acceptance

FORMAL SHIFT:
<CLAIM>
→ [CRYPTOGRAPHICALLY VERIFY]
→ <AUTHENTIC CLAIM>
→ [VALIDATE FOR LOCAL PURPOSE]
→ <ACCEPT / REJECT / INTERPRET>

SOURCE FORMALISM:
The W3C model distinguishes verification from validation.

Its validation discussion separately addresses:

validity periods,
credential status,
schema,
fitness for purpose,
and whether the verifier trusts the issuer to make the relevant claim.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

VERIFY(C) = TRUE

does not imply:

FIT(C, purpose) = TRUE

nor:

TRUST(issuer(C), claim(C)) = TRUE

nor:

PREDICTS_SUCCESS(C, context) = TRUE.

Therefore:

AUTHENTICITY
≠
VALIDITY
≠
RELEVANCE
≠
PREDICTIVE FITNESS.

TENSION:
[[Z-EDUPM-008]] asked whether smaller credentials might restore signal resolution.

This source reveals that technical resolution does not remove semantic ambiguity.

The credential can become perfectly machine-readable while the question “what does this mean about this person?” remains institutionally undecided.

MISSING:
Empirical evidence about how employers construct fitness-for-purpose rules when consuming machine-verifiable skill credentials at scale.

BOUNDARY:
The W3C standard specifies credential architecture, not labor-market hiring policy.

It does not conclude that verifiable credentials increase or decrease credentialism.

CITATION TRAIL:
[[Z-EDUPM-008]]
→ W3C validation
→ verification versus fitness for purpose
→ local verifier judgment
→ persistence of interpretation

Follow:
credential trust frameworks
assessment validity
construct validity
employer skill inference
qualification equivalence
automated hiring

TEST:
Create one cryptographically valid skill credential.

Present the identical credential to:

a university,
a regulated profession,
a startup,
a federal employer,
a freelance marketplace.

Record each verifier's acceptance rules and rationale.

If decisions diverge while cryptographic verification remains constant, map precisely where interpretive authority re-enters.

PLATFORM:
[[THE SEMANTIC LAST MILE OF CREDENTIALS]]

LINKS:
[[Z-EDUPM-008]]
[[Verification Is Not Validation]]
[[Fitness for Purpose]]
[[Authenticity Without Meaning]]

BIBTEX:
@techreport{sporny2025vc,
  author      = {Sporny, Manu and Longley, Dave and Chadwick, David and Herman, Ivan},
  title       = {Verifiable Credentials Data Model v2.0},
  institution = {World Wide Web Consortium},
  type        = {W3C Recommendation},
  year        = {2025},
  month       = may
}