ZETTEL

ID:
LAW-SHAM-20260817-03

TITLE:
2026-08-17 — A prompt cannot be rescued after failure by treating it as a nose of wax.

SOURCE:
White v. Dunbar, 119 U.S. 47, 51–52 (1886); Shambibble interview transcript, 2022-10-22, 03:01–04:01.

SOURCE URL:
https://www.govinfo.gov/content/pkg/USREPORTS-119/pdf/USREPORTS-119-47.pdf
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]

PASSAGE:
[QUOTE — WHITE v. DUNBAR]
“like a nose of wax”

[PARAPHRASE]
White rejects construing claim language opportunistically in different directions after the fact.

[QUOTE — SHAMBIBBLE]
“most people they use words, they don't think really hard about double meanings or ways they can be misinterpreted”

RESEARCH OBJECT:
POST HOC INTENTION IS NOT OPERATIVE LANGUAGE.

LOCAL MOVE:
A recurring failure in prompting is to defend an instruction by explaining what the user “obviously meant” after the system did something else. Patent claim doctrine disciplines the opposite instinct: operative text has consequences outside the drafter's private intention.

Shambibble behaves this way with the orange example. He does not tell the model that it should have understood him. He redrafts.

SOURCE TERMS:
“nose of wax”
“double meanings”
“misinterpreted”
“plain import”
“redraft”

WHAT BECAME STRANGE:
The prompt failure is evidentiary. It reveals that the claimed instruction did not exclude a reading the drafter assumed away. The correct response is amendment, not retrospective insistence.

QUESTION:
When an AI follows a plausible but unintended reading, should that event be treated as model error, drafting error, or an unresolved allocation between them?

DEEPER QUESTION:
What would a doctrine against post hoc prompt construction look like—one that forces the designer to preserve the original instruction and show exactly which amendment excludes the failed reading?

MECHANISM:
Preserve original prompt. Preserve failed output/action. State intended reading. State alternate reading demonstrated by failure. Draft smallest amendment that separates them. Retest.

FORMAL SHIFT:
FAILURE
→ “THAT IS NOT WHAT I MEANT”

becomes

FAILURE
→ DOCUMENT ALTERNATE CONSTRUCTION
→ AMEND LANGUAGE
→ RETEST

SOURCE FORMALISM:
White v. Dunbar is a claim-construction case warning against twisting claim meaning after issuance to fit desired outcomes.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT AMENDMENT RECORD = {original text, demonstrated construction, amendment, reason, regression test}.

TENSION:
Models also make unreasonable errors. Not every unexpected result indicts drafting. A mature practice needs a way to separate unsupported execution from textually available interpretation.

MISSING:
A standard for identifying when an output was sufficiently supported by the instruction to count as a drafting ambiguity rather than model noncompliance.

BOUNDARY:
White concerns public patent claims and infringement, not interactive instructions. Its value here is anti-post-hoc discipline, not doctrinal equivalence.

CITATION TRAIL:
[[MJ-2022-001]]
→ double meanings
→ White v. Dunbar
→ private intention loses control
→ failure forces amendment rather than reinterpretation

TEST:
Collect prompt failures and have blinded reviewers judge whether each output is supported by the original text. For supported-but-unwanted readings, require amendments that preserve the original prompt and identify the exact ambiguity repaired.

PLATFORM:
Patent claim construction
Prompt debugging

LINKS:
[[MJ-2022-001]]
[[SHAM-20260817-05]]
[[SHOT-20260817-07]]

BIBTEX:
@misc{white1886,
 author={{Supreme Court of the United States}},
 title={White v. Dunbar, 119 U.S. 47},
 year={1886},
 url={https://www.govinfo.gov/content/pkg/USREPORTS-119/pdf/USREPORTS-119-47.pdf}
}
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03; automated transcript}
}
