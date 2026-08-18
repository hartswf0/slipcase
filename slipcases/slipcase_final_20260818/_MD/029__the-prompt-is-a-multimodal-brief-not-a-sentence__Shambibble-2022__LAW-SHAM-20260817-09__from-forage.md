ZETTEL

ID:
LAW-SHAM-20260817-09

TITLE:
2026-08-17 — The prompt is a multimodal brief, not a sentence.

SOURCE:
Shambibble, “Image Prompting and--,” Midjourney community guide, 2022, provided PDF and text copy; Shambibble interview transcript, 2022-10-22.

SOURCE URL:
[LOCAL UPLOAD — Midjourney Image Prompting.pdf]
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]

PASSAGE:
[QUOTE — SHAMBIBBLE GUIDE]
“Image prompting is basically MJ letting one side draw what the other side describes to it over the phone.”

[QUOTE — SHAMBIBBLE GUIDE]
“We’re just trying to visually get across subjects/composition.”

RESEARCH OBJECT:
REPRESENTATIONAL ADVOCACY.

LOCAL MOVE:
[[LAW-SHAM-20260817-01]] treated prompting as adversarial construction of operative language. The guide forces a correction: the operative object need not be language alone. When text cannot reliably carry a spatial relation, identity, or style, Shambibble changes the medium of the instruction. A crude composite, a bank of reference faces, an image weight, a multiprompt boundary, and ordinary prose can all participate in one act of specification.

This makes the legal analogy stronger but narrower. A lawyer does not advocate only through sentences. A brief can incorporate exhibits, defined terms, diagrams, stipulations, and separately weighted authorities. Shambibble’s practice similarly treats representation choice itself as part of the argument to the interpreter.

SOURCE TERMS:
“inspiration”
“internal language”
“image prompt”
“subjects/composition”
“image weight”
“multiprompt”

WHAT BECAME STRANGE:
The central skill may not be writing a better prompt. It may be choosing which proposition belongs in which representational channel.

QUESTION:
When a generative system accepts text, images, references, parameters, masks, and structured controls, what is the correct unit to call “the prompt”?

DEEPER QUESTION:
Does prompt law need a doctrine of multimodal construction in which meaning is attributed to the whole operative record rather than to the final string of text?

MECHANISM:
Identify the intended relation. Observe where verbal specification fails. Move the disputed information into a representation the model handles more reliably. Combine channels while monitoring interference between them. Execute and revise.

FORMAL SHIFT:
TEXT PROMPT
→ MODEL

becomes

OPERATIVE BRIEF = {
  text,
  image evidence,
  weights,
  exclusions,
  decomposition,
  layout cue,
  prior output
}
→ MODEL

SOURCE FORMALISM:
The guide explicitly distinguishes text prompting from image prompting, describes image weight, uses multiple image prompts, and recommends crude visual mockups for complex scenes whose spatial relations Midjourney handles poorly in text.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For proposition p, choose channel c that maximizes reliable transmission while minimizing unwanted collateral associations:

c*(p) = argmax_c reliability(p,c) - interference(p,c)

TENSION:
A legal brief is interpreted under public institutional rules. A generative model is not a tribunal and does not owe reasons. Calling these inputs “arguments” is useful only if it keeps attention on interpretation under constrained evidence rather than anthropomorphizing the model.

MISSING:
A comparative map of which semantic relations are best carried by text, image, schema, direct manipulation, or example across current generative systems.

BOUNDARY:
The guide concerns Midjourney in 2022. Its exact controls are obsolete or version-bound. The durable object is the representational move, not the syntax.

CITATION TRAIL:
[[LAW-SHAM-20260817-01]]
→ adversarial construction
→ Shambibble image-prompting guide
→ language fails to carry some relations
→ representation changes
→ prompt becomes multimodal operative brief

TEST:
Choose fifty tasks containing identity, spatial relation, style, and composition constraints. Express each constraint separately through text, reference image, schema, and crude visual mockup where available. Measure instruction fidelity and cross-constraint interference. Determine whether representation choice predicts success better than prompt length.

PLATFORM:
Midjourney
Multimodal prompting
Patent practice
Natural-language programming

LINKS:
[[LAW-SHAM-20260817-01]]
[[SHAM-20260817-04]]
[[SHAM-20260817-06]]
[[SHOT-20260817-03]]

BIBTEX:
@misc{shambibble2022imageprompting,
  author={{Shambibble}},
  title={Image Prompting and--},
  year={2022},
  note={Midjourney community guide; researcher-provided PDF and text copy}
}
