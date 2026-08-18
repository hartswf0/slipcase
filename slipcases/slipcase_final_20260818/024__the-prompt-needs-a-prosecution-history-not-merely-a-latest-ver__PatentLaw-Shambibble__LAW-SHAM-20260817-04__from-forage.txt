ZETTEL

ID:
LAW-SHAM-20260817-04

TITLE:
2026-08-17 — The prompt needs a prosecution history, not merely a latest version.

SOURCE:
Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722, 733–41 (2002); Shambibble interview transcript, 2022-10-22, 46:25–48:36.

SOURCE URL:
https://supreme.justia.com/cases/federal/us/535/722/
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]

PASSAGE:
[PARAPHRASE — FESTO]
Patent prosecution history can limit later attempts to recapture subject matter surrendered by narrowing amendment.

[QUOTE — SHAMBIBBLE]
“you could like run that same prop with the same seed and take them out one by one.”

RESEARCH OBJECT:
AMENDMENT HISTORY AS OPERATIVE MEMORY.

LOCAL MOVE:
[[SHOT-20260817-07]] argues that execution failure can become a specification delta. Festo makes the history problem deeper: an amendment has meaning partly because of what it abandoned.

Prompt iteration usually destroys this negative history. Users delete the phrase that caused trouble, add a new clause, and keep only the latest prompt. The resulting text says what currently governs but not which interpretations were deliberately surrendered—or why.

SOURCE TERMS:
“prosecution history”
“amendment”
“surrender”
“take them out one by one”
“specification delta”

WHAT BECAME STRANGE:
A correction is not only new language. It is a boundary event with a before, an after, and a reason. Losing the before-state makes old failures easy to reintroduce.

QUESTION:
What should a prompt system remember about deleted constraints?

DEEPER QUESTION:
Can an agent distinguish an instruction that is absent because it was never relevant from one that is absent because it was deliberately revoked after causing a known failure?

MECHANISM:
Prompt P0 produces failure F. Amendment A narrows or changes P0 to P1. Record A's reason and the behavioral territory intentionally excluded. Future edits are checked against that record before re-expanding scope.

FORMAL SHIFT:
LATEST PROMPT ONLY

becomes

P0
→ FAILURE / ADVERSE CONSTRUCTION
→ AMENDMENT A
→ P1
→ REGRESSION TEST
→ PRESERVED HISTORY

SOURCE FORMALISM:
Festo limits recapture under the doctrine of equivalents after certain narrowing amendments made during patent prosecution.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT PROSECUTION HISTORY = versioned instructions + observed adverse constructions + amendment reasons + revoked/superseded states + regression tests.

TENSION:
Legal estoppel should not be imported literally. Prompt systems often should be allowed to reconsider old constraints when the model, task, or evidence changes. The transferable principle is provenance of narrowing, not permanent prohibition.

MISSING:
How to represent the “territory” surrendered by a natural-language amendment in a machine-testable way.

BOUNDARY:
The analogy is methodological. A prompt amendment does not create legal estoppel.

CITATION TRAIL:
[[SHOT-20260817-07]]
→ failure as specification delta
→ Festo
→ amendment carries negative history
→ deleted prompt text may remain epistemically operative

TEST:
For a longitudinal agent, preserve every constraint amendment with a reason and one regression example. Later propose automatic simplifications. Measure whether provenance-aware simplification reintroduces fewer historical failures than latest-prompt-only maintenance.

PLATFORM:
Patent prosecution
Prompt evolution
Agent memory

LINKS:
[[SHOT-20260817-07]]
[[SHAM-20260817-05]]
[[SHAM-20260817-08]]

BIBTEX:
@misc{festo2002,
 author={{Supreme Court of the United States}},
 title={Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722},
 year={2002},
 url={https://supreme.justia.com/cases/federal/us/535/722/}
}
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03; automated transcript}
}
