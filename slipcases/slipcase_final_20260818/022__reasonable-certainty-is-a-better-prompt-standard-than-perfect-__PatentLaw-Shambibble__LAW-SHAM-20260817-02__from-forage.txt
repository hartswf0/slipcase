ZETTEL

ID:
LAW-SHAM-20260817-02

TITLE:
2026-08-17 — Reasonable certainty is a better prompt standard than perfect precision.

SOURCE:
Nautilus, Inc. v. Biosig Instruments, Inc., 572 U.S. 898, 909–11 (2014); 35 U.S.C. § 112(b).

SOURCE URL:
https://www.govinfo.gov/app/details/USREPORTS-572/USREPORTS-572-898
https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title35-section112

PASSAGE:
[QUOTE — NAUTILUS]
“absolute precision is unattainable.”

[PARAPHRASE]
Nautilus requires patent claims, read with the specification and prosecution history, to inform skilled readers of scope with reasonable certainty.

RESEARCH OBJECT:
MANAGED INDETERMINACY.

LOCAL MOVE:
Prompt engineering is often narrated as a march from vague English toward complete specification. Patent law has lived longer with the impossibility of that endpoint. [[MJ-2022-005]] and [[SHAM-20260817-08]] likewise reject total knowledge: Shambibble can test bounded relations while admitting he cannot assign exact causal percentages to every phrase.

The legal lesson is not “be precise.” It is more exacting: draw consequential boundaries with enough certainty for the relevant interpreter while admitting that language cannot eliminate every edge case.

SOURCE TERMS:
“reasonable certainty”
“absolute precision”
“scope”
“studied ignorance”
“there's not a lot we know”

WHAT BECAME STRANGE:
The lawyer may be useful to prompt practice precisely because law does not equate professional drafting with perfect language. It professionalizes the management of residual uncertainty.

QUESTION:
What would “reasonable certainty” mean for a prompt whose output is stochastic rather than legally construed?

DEEPER QUESTION:
Should prompt sufficiency be measured by whether the remaining ambiguity can change a consequential action, rather than by whether more detail could theoretically be added?

MECHANISM:
Identify action-relevant scope. Specify enough constraints that materially distinct interpretations do not cross unacceptable boundaries. Leave harmless or creative variables open.

FORMAL SHIFT:
MAXIMAL SPECIFICATION
→ impossible / brittle

becomes

MATERIAL BOUNDARIES
+ TOLERATED OPENNESS
→ REASONABLE OPERATIONAL CERTAINTY

SOURCE FORMALISM:
35 U.S.C. § 112(b) requires claims particularly pointing out and distinctly claiming the invention; Nautilus interprets definiteness through reasonable certainty while acknowledging limits of language.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A prompt is reasonably certain when surviving ambiguity does not materially alter the authorized action class, protected invariants, or acceptance test.

TENSION:
Too much ambiguity can authorize harmful divergence. Too much precision can eliminate productive underdetermination, overfit one model version, or make adaptation impossible.

MISSING:
A severity-sensitive metric of prompt ambiguity that distinguishes aesthetic variation from action-scope variation.

BOUNDARY:
Nautilus defines a patent-law validity standard. “Reasonable operational certainty” is our proposed transfer, not legal doctrine.

CITATION TRAIL:
[[SHAM-20260817-08]]
→ studied ignorance
→ Nautilus
→ absolute precision rejected
→ certainty becomes consequential rather than total

TEST:
For prompts with known acceptance tests, progressively remove constraints. Find the point at which output variation first changes authorized action or invariant satisfaction. Compare that empirical boundary with human judgments of “clear enough.”

PLATFORM:
Patent law
Prompt evaluation
Natural-language programming

LINKS:
[[SHAM-20260817-08]]
[[MJ-2022-005]]
[[SHOT-20260817-09]]

BIBTEX:
@misc{nautilus2014,
 author={{Supreme Court of the United States}},
 title={Nautilus, Inc. v. Biosig Instruments, Inc., 572 U.S. 898},
 year={2014},
 url={https://www.govinfo.gov/app/details/USREPORTS-572/USREPORTS-572-898}
}
@misc{usc112,
 author={{United States Congress}},
 title={35 U.S.C. § 112},
 url={https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title35-section112}
}
