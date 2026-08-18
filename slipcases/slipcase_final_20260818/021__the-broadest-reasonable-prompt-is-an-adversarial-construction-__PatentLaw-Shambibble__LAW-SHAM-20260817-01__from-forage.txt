ZETTEL

ID:
LAW-SHAM-20260817-01

TITLE:
2026-08-17 — The broadest reasonable prompt is an adversarial construction test.

SOURCE:
U.S. Patent and Trademark Office, Manual of Patent Examining Procedure § 2111, “Claim Interpretation; Broadest Reasonable Interpretation,” current USPTO edition consulted 2026-08-17; Shambibble interview transcript, 2022-10-22, 03:01–04:29.

SOURCE URL:
https://www.uspto.gov/web/offices/pac/mpep/s2111.html
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]

PASSAGE:
[QUOTE — SHAMBIBBLE]
“Except insofar as you're thinking adversarial, you're thinking, Okay, well, how is this gonna be screwed up?”

[PARAPHRASE — USPTO]
During patent examination, pending claims receive their broadest reasonable interpretation consistent with the specification, from the perspective of a person of ordinary skill in the art.

RESEARCH OBJECT:
BROAD INTERPRETATION AS A PRE-EXECUTION TEST.

LOCAL MOVE:
[[MJ-2022-001]] already framed prompt writing as anticipating misinterpretation. Patent examination supplies a disciplined analogue: do not test language only under the reading the drafter intended. Pressure it under the broadest reasonable construction the authorized interpreter could give it.

Shambibble's “orange” problem is miniature claim construction. The drafter says ORANGE intending a color; the interpreter finds another permissible referent. His solution is not to insist on private intent but to alter the operative language: “no fruit, no sphere, no circle.”

SOURCE TERMS:
“thinking adversarial”
“how is this gonna be screwed up?”
“broadest reasonable interpretation”
“plain meaning”
“specification”
“ordinary skill in the art”

WHAT BECAME STRANGE:
Prompt advice usually asks whether an instruction is clear to the writer. Patent practice asks a harsher question: what is the widest consequential reading the interpreter may reasonably adopt? The lawyer's expertise begins where cooperative interpretation ends.

QUESTION:
Can a prompt be red-teamed by construing each operative phrase under its broadest reasonable model interpretation before execution?

DEEPER QUESTION:
Who or what occupies the role of the patent system's “person of ordinary skill” when the interpreter is a changing model whose learned associations, tokenization, tools, and system instructions are not stable public doctrine?

MECHANISM:
Draft instruction. Identify scope-bearing terms. Generate plausible alternate readings consistent with the surrounding context. Execute or simulate those readings. Amend language where an alternate reading produces a materially different action.

FORMAL SHIFT:
INTENDED READING
→ PROMPT
→ EXECUTION

becomes

PROMPT
→ BROADEST REASONABLE CONSTRUCTIONS
→ ADVERSARIAL TEST
→ AMENDMENT
→ EXECUTION

SOURCE FORMALISM:
USPTO MPEP § 2111: broadest reasonable interpretation consistent with the specification; plain meaning ordinarily reflects the understanding of one of ordinary skill in the art.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

BRP(P, C, M) = set of materially plausible readings of prompt P under context C by model/runtime M.

A prompt is not operationally clear merely because intended_reading ∈ BRP. It is clearer when materially dangerous alternate readings have been excluded or safely bounded.

TENSION:
Patent BRI is an institutional doctrine constrained by specification, precedent, and a skilled-artisan perspective. Model “reasonableness” is empirical and unstable. The analogy becomes false if BRI is treated as a literal model-decoding algorithm.

MISSING:
A practical method for enumerating “reasonable” machine readings without merely inventing every logically possible misreading.

BOUNDARY:
MPEP doctrine governs patent examination, not AI systems. The proposed Broadest Reasonable Prompt test is an analogy and design heuristic.

CITATION TRAIL:
[[MJ-2022-001]]
→ Shambibble asks “how is this gonna be screwed up?”
→ USPTO broadest reasonable interpretation
→ intended meaning loses privilege
→ prompt red-teaming becomes claim construction

TEST:
Take 100 consequential agent prompts. Before execution, have an independent model produce the three broadest materially different readings consistent with context. Compare those predictions with observed failures. Test whether BRP review catches more failures than ordinary “make this clearer” editing.

PLATFORM:
Patent prosecution
Prompt language
Agentic AI

LINKS:
[[MJ-2022-001]]
[[SHOT-20260817-01]]
[[SHAM-20260817-08]]

BIBTEX:
@misc{uspto2111,
 author={{U.S. Patent and Trademark Office}},
 title={MPEP § 2111: Claim Interpretation; Broadest Reasonable Interpretation},
 url={https://www.uspto.gov/web/offices/pac/mpep/s2111.html}
}

@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03; automated transcript}
}
