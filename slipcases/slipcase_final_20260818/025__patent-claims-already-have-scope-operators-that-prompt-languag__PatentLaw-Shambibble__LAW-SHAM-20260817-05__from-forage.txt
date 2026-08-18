ZETTEL

ID:
LAW-SHAM-20260817-05

TITLE:
2026-08-17 — Patent claims already have scope operators that prompt language lacks.

SOURCE:
U.S. Patent and Trademark Office, MPEP § 2111.03, “Transitional Phrases,” current edition consulted 2026-08-17.

SOURCE URL:
https://www.uspto.gov/web/offices/pac/mpep/s2111.html#d0e2048

PASSAGE:
[PARAPHRASE — USPTO]
“Comprising” is presumptively open-ended: recited elements are required but additional unrecited elements may remain within scope. “Consisting of” is used as a closed transition.

RESEARCH OBJECT:
OPEN-WORLD VERSUS CLOSED-WORLD INSTRUCTION SCOPE.

LOCAL MOVE:
Shambibble's negative prompting—“no fruit, no sphere, no circle”—shows the cost of not having stable scope semantics. Ordinary prompt verbs such as include, use, make, and contain do not reliably say whether unmentioned additions are allowed.

Patent drafting has lexicalized this distinction. A single transitional phrase can change whether the claim admits unrecited elements.

SOURCE TERMS:
“comprising”
“consisting of”
“open-ended”
“closed”
“negative prompting”

WHAT BECAME STRANGE:
Prompt language may not chiefly need more descriptive adjectives. It may need standardized operators for closure.

QUESTION:
What is the prompt equivalent of “comprising” versus “consisting of”?

DEEPER QUESTION:
Should agent instructions expose explicit open/closed-world semantics so that “include A, B, C” can be distinguished from “use only A, B, C” without relying on conversational implication?

MECHANISM:
Instruction defines required set R. Scope operator determines whether output/action may include X ∉ R. OPEN permits additional compatible elements; CLOSED prohibits them unless separately authorized.

FORMAL SHIFT:
LIST OF REQUIREMENTS
+ PRAGMATIC GUESS ABOUT EXCLUSIVITY

becomes

SCOPE_OPERATOR(OPEN|CLOSED|ESSENTIALLY_CLOSED)
+ REQUIREMENTS

SOURCE FORMALISM:
Patent claim drafting uses transitional phrases with settled scope consequences, including the open-ended “comprising” and closed “consisting of.”

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

REQUIRE {A,B,C} COMPRISING → must include A,B,C; may add compatible items.
REQUIRE {A,B,C} CONSISTING → must include A,B,C; may not add peer items.

TENSION:
Legal transitional terms work because an interpretive institution gives them stable meaning. Simply borrowing the words for prompts would not create stable semantics unless the runtime adopts them formally.

MISSING:
Whether current models already respond reliably to ordinary-language open/closed formulations, and whether formal scope operators improve performance.

BOUNDARY:
This zettel proposes design vocabulary inspired by patent drafting; it does not claim patent terms already possess computational semantics in AI systems.

CITATION TRAIL:
[[MJ-2022-001]]
→ negative exclusions
→ patent transitional phrases
→ scope becomes explicit operator
→ prompt language needs closure semantics

TEST:
Construct matched instructions differing only in “include,” “include at least,” “use only,” “comprising,” and “consisting of.” Test across models and tool agents for unauthorized additions. Then implement explicit OPEN/CLOSED schema flags and compare reliability.

PLATFORM:
Patent drafting
Prompt language design

LINKS:
[[MJ-2022-001]]
[[SHOT-20260817-03]]
[[LAW-SHAM-20260817-01]]

BIBTEX:
@misc{uspto211103,
 author={{U.S. Patent and Trademark Office}},
 title={MPEP § 2111.03: Transitional Phrases},
 url={https://www.uspto.gov/web/offices/pac/mpep/s2111.html}
}
