ZETTEL

ID:
Z-EDUPM-014

TITLE:
A DIGITAL CREDENTIAL CAN CEASE TO BE TRUE FOR OPERATIONAL PURPOSES WITHOUT ERASING THE HISTORICAL EVENT THAT PRODUCED IT.

SOURCE:
Manu Sporny, Dave Longley, David Chadwick, and Ivan Herman — Verifiable Credentials Data Model v2.0 — 2025 — W3C Recommendation — Sections 4.9–4.10.

PASSAGE:
[PARAPHRASE] The W3C model allows credentials to specify `validFrom`, `validUntil`, and `credentialStatus`; status can communicate conditions such as suspension or revocation.

RESEARCH OBJECT:
Credentialing can move from an immutable historical certificate toward a stateful claim whose present operational validity is machine-checkable.

LOCAL MOVE:
The specification separates several things ordinarily compressed into “the credential”:

the claim,
its issuer,
its cryptographic proof,
its validity interval,
and its current status.

SOURCE TERMS:
verifiable credential
issuer
holder
verifier
validFrom
validUntil
credentialStatus
revoked
suspended
claims

WHAT BECAME STRANGE:
“I graduated in 2020” appears grammatically permanent.

But a digital credential architecture can represent:

CLAIM EXISTS
+
CLAIM WAS VALID
+
CLAIM IS CURRENTLY VALID / EXPIRED / SUSPENDED / REVOKED.

That creates the technical possibility of credentials that behave less like archival diplomas and more like state variables.

Human qualification can become queryable in the present tense.

QUESTION:
What happens to education when credentials cease to be durable records of completed events and become continuously inspectable states with validity windows and status transitions?

DEEPER QUESTION:
Could hyper-credentialism mutate into a system in which competence must not merely be earned repeatedly but remain technically “alive”?

MECHANISM:
issuer makes claim
→ cryptographically secures credential
→ validity interval attached
→ status endpoint / status structure attached
→ verifier checks current condition
→ credential accepted or rejected for present use

FORMAL SHIFT:
<PAST ACHIEVEMENT>
→ <SIGNED CLAIM>
→ [ATTACH TIME + STATUS]
→ <PRESENT-TENSE CREDENTIAL STATE>

SOURCE FORMALISM:
The W3C data model explicitly provides:

`issuer`
`credentialSubject`
`validFrom`
`validUntil`
`credentialStatus`

and models an issuer-holder-verifier ecosystem.

`validUntil` can identify when credential information ceases to be valid.

`credentialStatus` can expose status such as revocation or suspension.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Traditional diploma:

ACHIEVEMENT(t₀)
→ CREDENTIAL
→ persists as historical record

Stateful credential:

C(t) =
{
 issuer,
 subject,
 claim,
 validFrom,
 validUntil,
 status
}

Possible transitions:

VALID
→ EXPIRED

VALID
→ SUSPENDED
→ VALID

VALID
→ REVOKED

TENSION:
[[Z-EDUPM-008]] proposed that micro-credentials decompose one large signal into smaller settlement events.

The W3C architecture introduces another axis:

those smaller claims can also acquire TIME and STATE.

Granularity need not merely multiply credentials.

It can make credentials dynamically revisable.

MISSING:
Evidence about which educational and workforce credentials actually use expiration, suspension, or revocation rather than merely supporting those fields technically.

BOUNDARY:
The W3C standard permits validity periods and credential status.

It does not require educational credentials to expire or claim that degrees should become revocable competence subscriptions.

CITATION TRAIL:
[[Z-EDUPM-008]]
→ W3C Verifiable Credentials Data Model 2.0
→ validity period
→ credential status
→ qualification as temporal state

Follow:
Open Badges 3.0
professional license renewal
expiring technical certifications
continuing education requirements
credential-status privacy architectures

TEST:
Collect 1,000 machine-verifiable educational and workforce credentials.

Record whether each implements:

validUntil,
credentialStatus,
revocation,
suspension,
refresh,
recertification.

Then classify what kinds of knowledge institutions choose to make permanent versus perishable.

PLATFORM:
[[CREDENTIALS AS STATE MACHINES]]

LINKS:
[[Z-EDUPM-008]]
[[Credential Expiration]]
[[Qualification as State]]
[[Human Capital Marked to Time]]

BIBTEX:
@techreport{sporny2025vc,
  author      = {Sporny, Manu and Longley, Dave and Chadwick, David and Herman, Ivan},
  title       = {Verifiable Credentials Data Model v2.0},
  institution = {World Wide Web Consortium},
  type        = {W3C Recommendation},
  year        = {2025},
  month       = may
}