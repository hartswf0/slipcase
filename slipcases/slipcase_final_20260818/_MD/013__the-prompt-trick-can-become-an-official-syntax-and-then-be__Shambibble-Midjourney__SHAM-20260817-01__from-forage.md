ZETTEL

ID:
SHAM-20260817-01

TITLE:
2026-08-17 — The prompt trick can become an official syntax and then become legacy.

SOURCE:
Shambibble interview transcript — 2022-10-22 — approximately 1:03:53–1:05:29. Midjourney — “Multi-Prompts & Weights” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights

PASSAGE:
[QUOTE — SHAMBIBBLE]
“A lot of people only use it for waiting. Because that’s, that’s like some feature of multi prompting is you can take one part and wait it up a little bit. But it’s not all it’s not like that’s not emphasis that will actually break up your prop.”

[QUOTE — CURRENT MIDJOURNEY DOCUMENTATION]
“You add a double colon `::` between the different ideas in your prompt. This acts like a divider.”

RESEARCH OBJECT:
PROMPT DECOMPOSITION HAS A LIFECYCLE.

LOCAL MOVE:
[[MJ-2022-009]] says prompt knowledge may become meaningless in six months. Shambibble’s multi-prompt example supplies a concrete mechanism: punctuation did not merely strengthen a phrase; it changed how the prompt was partitioned. Current Midjourney documentation still explains that decomposition, but lists multi-prompts as compatible only through model 6.1. A once-central control can survive as documented legacy syntax while newer model generations move elsewhere.

SOURCE TERMS:
“multi prompting”
“break up your prop”
“double colon”
“separate instructions”
“weights”

WHAT BECAME STRANGE:
A prompt technique can pass through three states: discovery, officialization, and obsolescence. The durable knowledge may be the distinction the trick exposed — decomposition versus emphasis — rather than the exact token sequence `::`.

QUESTION:
When a prompt technique disappears from current models, what exactly has vanished: the user need, the implementation, or only the old syntax?

DEEPER QUESTION:
Can the history of prompt craft be written as a sequence of user-discovered distinctions that migrate into model architecture or interface controls and thereby erase the lexical tricks that first exposed them?

MECHANISM:
Phrase is treated as one semantic bundle. User inserts separator. Separate prompt parts receive independent treatment and optional weights. Later system versions may remove or redesign the explicit operator.

FORMAL SHIFT:
PHRASE
→ USER DISCOVERS DECOMPOSITION OPERATOR
→ OPERATOR BECOMES DOCUMENTED FEATURE
→ FEATURE BECOMES VERSION-BOUND LEGACY

SOURCE FORMALISM:
Midjourney documentation states that `::` separates ideas before they are combined and documents numeric weights. It lists compatibility through V6.1.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

TRICK(t, version) may be transient while DISTINCTION(t) remains durable.

syntax lifetime < conceptual lifetime

TENSION:
The later disappearance of a syntax does not prove that a model “learned” the underlying distinction internally. It may instead indicate interface redesign or an incompatible architecture.

MISSING:
A version-by-version implementation history explaining why multi-prompts are absent from later versions.

BOUNDARY:
Similarity between the 2022 practitioner technique and later documentation establishes continuity of functionality, not that Shambibble caused the feature or that later removal resulted from better language understanding.

CITATION TRAIL:
[[MJ-2022-009]]
→ Shambibble on multi-prompt decomposition
→ official Midjourney multi-prompt syntax
→ current compatibility stops at 6.1
→ prompt trick acquires an afterlife

TEST:
Collect prominent Midjourney prompt techniques from 2022–2024. For each, record first community appearance, documentation date, supported model versions, replacement feature if any, and whether the underlying user problem remains. Distinguish SYNTAX DEATH from PROBLEM DEATH.

PLATFORM:
Midjourney
Discord

LINKS:
[[MJ-2022-009]]
[[MJ-2022-004]]
[[SHOT-20260817-03]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
