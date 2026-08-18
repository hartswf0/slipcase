ZETTEL

ID:
RETENTION-005-E

TITLE:
Prompt-to-Prompt proves that “prompt control” is not a property of the sentence alone but of the interface architecture that interprets it.

SOURCE:
Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or — “Prompt-to-Prompt Image Editing with Cross Attention Control” — 2022. The authors note that ordinary text-to-image systems may radically alter an image after a small textual change, then introduce cross-attention control enabling localized and global edits using textual prompt changes while preserving relevant prior structure.

PASSAGE:
[PARAPHRASE]
The paper makes the same textual operation—change a word—behave differently by preserving and manipulating cross-attention information from the prior generation. Text becomes a more local editing control because the system architecture changes how that text is operationalized.

RESEARCH OBJECT:
PROMPT CONTROL IS INTERFACE-RELATIVE.

LOCAL MOVE:
The Copyright Office's 2025 prompt conclusion is explicitly technology-contingent. Prompt-to-Prompt supplies a concrete technical reason why that qualification matters.

SOURCE TERMS:
prompt-to-prompt
editing
cross-attention
localized editing
preserve
text
control

WHAT BECAME STRANGE:
The same natural-language instruction:

CHANGE DOG TO CAT

can mean:

REGENERATE ALMOST EVERYTHING

under one interface,

or:

REPLACE A LOCAL SEMANTIC ELEMENT WHILE PRESERVING COMPOSITION

under another.

QUESTION:
Should legal authorship attach to what the user types, or to the degree of control the entire human-interface-model assembly gives that utterance?

DEEPER QUESTION:
Can a change in interface engineering convert an identical linguistic act from weak suggestion into expressive execution?

MECHANISM:
ordinary:

p
→ G
→ y

p'
→ G
→ y' radically changed.

Prompt-to-Prompt:

p,y,attention structure
+
localized textual edit p'
→ controlled cross-attention manipulation
→ y' preserving much of y.

FORMAL SHIFT:
<PROMPT AS GLOBAL CONDITION>
→ [RETAIN MODEL-STATE STRUCTURE]
→ <PROMPT AS LOCAL EDIT OPERATOR>

SOURCE FORMALISM:
The paper identifies cross-attention layers as critical to the relation between words and spatial layout and manipulates those layers to support prompt-directed editing.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Do not define:

    Control(p)

Define:

    Control(p | M, interface, retained_state).

Same p may satisfy:

    Control(p | I₁) << Control(p | I₂).

TENSION:
Prompt-to-Prompt is a technical research system, not a copyright holding.

Demonstrating increased controllability does not establish that the legal originality threshold has been met.

MISSING:
Empirical legal analysis of interfaces where natural-language edits have repeatable feature-local effects.

BOUNDARY:
“PROMPTS ALONE” is unstable as a technical category unless the surrounding interaction architecture is held fixed.

CITATION TRAIL:
[[RETENTION-005]]
→ prompt as possible upstream authorship site
→ USCO says current technology lacks sufficient control
→ Prompt-to-Prompt changes prompt-to-output controllability
→ authorship question becomes architecture-relative.

TEST:
Use identical paired textual edits under:

A. vanilla text-to-image regeneration
B. Prompt-to-Prompt-style retained-attention editing.

Measure preservation of non-target properties.

Ask whether the legal analysis should remain identical when the user's words exert measurably different feature-level control.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[prompt-to-prompt]]
[[interface-relative-authorship]]
[[cross-attention]]
[[control-topology]]

BIBTEX:
@article{HertzEtAl2022PromptToPrompt,
  author  = {Hertz, Amir and Mokady, Ron and Tenenbaum, Jay and Aberman, Kfir and Pritch, Yael and Cohen-Or, Daniel},
  title   = {Prompt-to-Prompt Image Editing with Cross Attention Control},
  journal = {arXiv preprint arXiv:2208.01626},
  year    = {2022}
}
