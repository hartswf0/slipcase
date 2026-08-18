ZETTEL

ID:
XSOLLA-ROBLOX-012

TITLE:
The hidden boundary of Roblox becomes visible on the credit-card statement: “Xsolla*Roblox.”

SOURCE:
Roblox Support — “Unauthorized Charges & Refund Requests” — current; Xsolla corporate timeline.

SOURCE URL:
https://en.help.roblox.com/hc/en-us/articles/203312650-Unauthorized-Charges-Refund-Requests

PASSAGE:
[QUOTE] “If the charge on your statement says ‘Xsolla*Roblox’, please contact Xsolla’s Customer Support team.”

RESEARCH OBJECT:
The player experiences ROBLOX.

The payment system may experience a multi-actor transaction involving Roblox, Xsolla, banks, card networks, and customer-support jurisdictions.

The architectural seam becomes legible when the transaction fails.

LOCAL MOVE:
Roblox routes support responsibility according to the payment processor encoded in the statement descriptor.

SOURCE TERMS:
Xsolla*Roblox
third-party payment processors
refund
charge
Customer Support
payment provider

WHAT BECAME STRANGE:
Infrastructure that is deliberately invisible during successful play becomes visible during failure.

QUESTION:
Can failure messages reveal the actual architecture of a supposedly seamless world?

DEEPER QUESTION:
Are chargebacks, error messages, receipts, privacy notices, and refund routes better maps of a platform than its visual interface?

MECHANISM:
<PLAYER>
→ ROBLOX
→ <PAYMENT REQUEST>
→ XSOLLA
→ <PAYMENT NETWORK>

failure:

<CHARGE>
→ [READ DESCRIPTOR]
→ <DETERMINE RESPONSIBLE ACTOR>
→ [ROUTE DISPUTE]

FORMAL SHIFT:
<ONE PLATFORM>
→ <MULTI-INSTITUTIONAL STACK>
→ [FAILURE]
→ <ARCHITECTURE BECOMES VISIBLE>

SOURCE FORMALISM:
Roblox distinguishes charges labeled:

Xsolla*Roblox

from charges labeled:

Roblox

and assigns different support paths.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SUCCESS hides topology.

FAILURE exposes topology.

if descriptor == "Xsolla*Roblox":
    authority = XSOLLA_SUPPORT
else if descriptor == "Roblox":
    authority = ROBLOX_SUPPORT

TENSION:
The user-facing world promises continuity.

The transactional backend partitions responsibility.

MISSING:
Which Roblox purchasing channels currently route through Xsolla, in which jurisdictions, and under what transaction types.

BOUNDARY:
The documentation proves that some Roblox charges are processed or supported through Xsolla. It does not establish that Xsolla processes every Roblox transaction.

CITATION TRAIL:
Roblox billing architecture
Xsolla/Roblox 2018 agreement
Merchant of Record
payment descriptors
chargebacks
consumer recourse

TEST:
Purchase identical Robux packages through:

WEB
IOS
ANDROID
XBOX
PLAYSTATION
QUEST

Record:

STATEMENT DESCRIPTOR
MERCHANT
PROCESSOR
REFUND AUTHORITY
TAX ACTOR
PLATFORM FEE
ENTITLEMENT PATH.

The result is the institutional anatomy of one virtual currency.

PLATFORM:
[[Failures reveal the machine]]

LINKS:
[[XSOLLA-EXOSKELETON-010]]
[[Invisible infrastructure]]
[[Roblox economy]]

BIBTEX:
@misc{roblox_xsolla_billing,
  author = {{Roblox Corporation}},
  title = {Unauthorized Charges \& Refund Requests},
  url = {https://en.help.roblox.com/hc/en-us/articles/203312650-Unauthorized-Charges-Refund-Requests},
  note = {Accessed 2026-08-17}
}