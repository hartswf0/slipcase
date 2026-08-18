ZETTEL

ID:
LAW-SHAM-20260817-06

TITLE:
2026-08-17 — Antecedent basis is a theory of state reference for prompt language.

SOURCE:
U.S. Patent and Trademark Office, MPEP § 2175, form paragraph 7.34.05, “Lack of Antecedent Basis in the Claims,” current edition consulted 2026-08-17.

SOURCE URL:
https://www.uspto.gov/web/offices/pac/mpep/s2175.html

PASSAGE:
[PARAPHRASE — USPTO]
A lack of antecedent basis can make claim scope indeterminate; USPTO examples include later references such as “said lever” or “the lever” without sufficient earlier introduction.

RESEARCH OBJECT:
REFERENCE BINDING AS A LANGUAGE OPERATION.

LOCAL MOVE:
Prompt failures frequently involve expressions such as “it,” “the file,” “the same character,” “that version,” or “use the earlier one.” These appear natural to humans because conversational context supplies antecedents. In tool-using systems the referent may be ambiguous across files, turns, objects, or generated candidates.

Patent claim drafting has a specialized discipline for this problem: introduce an element, then bind later references to it.

SOURCE TERMS:
“antecedent basis”
“said lever”
“the lever”
“indeterminate”
“same character”
“the file”

WHAT BECAME STRANGE:
An apparently fussy feature of legal drafting becomes highly computational: nouns need identities that persist across operations.

QUESTION:
When does ordinary conversational reference become too weak for an agent that mutates state?

DEEPER QUESTION:
Could prompt language acquire explicit antecedent binding—names, handles, IDs, scoped aliases—without forcing users into conventional programming syntax?

MECHANISM:
Introduce entity E with stable identifier. Subsequent instruction references E by bound name. Runtime checks that every definite reference resolves uniquely before consequential execution.

FORMAL SHIFT:
NATURAL REFERENCE
“change the file and send it”

becomes

BIND file := artifact_42
MODIFY file
SEND file

SOURCE FORMALISM:
USPTO examination practice treats aggravated lack of antecedent basis as an indefiniteness problem when it makes claim scope indeterminate.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT ANTECEDENT CHECK: every definite noun phrase that controls a state mutation must resolve to one live entity or trigger clarification.

TENSION:
Human dialogue succeeds with loose reference constantly. Requiring explicit binding everywhere would make prompt language cumbersome. The useful threshold is consequential ambiguity, not grammatical purity.

MISSING:
A classifier for references that are harmlessly inferable versus references that can target materially different objects or states.

BOUNDARY:
Patent antecedent basis is a claim-drafting doctrine, not an AI binding system. The state-reference analogy is ours.

CITATION TRAIL:
[[SHAM-20260817-04]]
→ recurring character requires identity persistence
→ patent antecedent basis
→ referent becomes bound state
→ identity control moves from description to explicit reference

TEST:
Build an agent benchmark where prompts use pronouns and definite descriptions across multiple similar files/characters/objects. Compare ordinary context, explicit IDs, and automatic antecedent checking on wrong-target actions.

PLATFORM:
Patent examination
Agent state
Prompt language

LINKS:
[[SHAM-20260817-04]]
[[SHOT-20260817-02]]
[[SHOT-20260817-03]]

BIBTEX:
@misc{uspto2175,
 author={{U.S. Patent and Trademark Office}},
 title={MPEP § 2175: Rejections under 35 U.S.C. 112(b)},
 url={https://www.uspto.gov/web/offices/pac/mpep/s2175.html}
}
