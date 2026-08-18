ZETTEL

ID:
LAW-SHAM-20260817-12

TITLE:
2026-08-17 — Copyright’s “prompt” is smaller than the practice it is trying to evaluate.

SOURCE:
U.S. Copyright Office, Copyright and Artificial Intelligence, Part 2: Copyrightability, January 2025, pp. 21–28; Shambibble, “Image Prompting and--,” 2022.

SOURCE URL:
https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
[LOCAL UPLOAD — Midjourney Image Prompting.pdf]

PASSAGE:
[QUOTE — U.S. COPYRIGHT OFFICE]
“prompts alone do not provide sufficient human control”

[PARAPHRASE — SHAMBIBBLE GUIDE]
The guide’s recurring-character and scene-construction workflows combine text, selected prior outputs, multiple image references, image weights, stylization settings, rerolls, multiprompt decomposition, and sometimes externally composited mockups.

RESEARCH OBJECT:
THE UNIT-OF-AUTHORSHIP PROBLEM.

LOCAL MOVE:
[[LAW-SHAM-20260817-09]] showed that the operative prompt can be distributed across representational channels. Copyright doctrine now makes that distribution consequential. The Copyright Office’s prompt analysis asks whether prompts sufficiently determine expressive elements and concludes that current generally available prompts alone usually do not. But Shambibble’s 2022 practice is already not “prompts alone.” It is a sequence of selections and interventions spread across text, images, parameters, and revisions.

The legal question therefore cannot be exhausted by asking how detailed the final text prompt was. It must identify which expressive elements, if any, were human-authored, selected, arranged, modified, or otherwise controlled across the whole workflow.

SOURCE TERMS:
“prompts alone”
“human control”
“expressive elements”
“selection”
“coordination”
“arrangement”
“expressive inputs”

WHAT BECAME STRANGE:
The practice that early users called prompting may be legally significant precisely where it ceases to look like one prompt.

QUESTION:
What is the legally relevant unit of human contribution in an iterative multimodal generative workflow?

DEEPER QUESTION:
Could copyright analysis become more accurate by reconstructing the provenance of expressive control element-by-element rather than classifying an entire workflow as “prompting”?

MECHANISM:
Human contribution can occur at multiple stages: create or select an input image; choose which output becomes a reference; set parameters; compose a mockup; revise text; arrange outputs; modify generated material. Copyrightability then depends on whether protected human expression or sufficiently original human selection, arrangement, or modification is perceptible in the resulting work.

FORMAL SHIFT:
PROMPT
→ OUTPUT
→ AUTHORSHIP QUESTION

becomes

CONTROL RECORD = {
  human expressive inputs,
  selections,
  arrangements,
  modifications,
  parameterized constraints,
  model-determined expression
}
→ element-specific authorship analysis

SOURCE FORMALISM:
The Copyright Office distinguishes prompts from expressive inputs and from later modification or arrangement. It states that prompts alone generally do not provide sufficient control with current technology, while human-authored expressive material perceptible in an output and original selection, coordination, arrangement, or modification can be protected case by case.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

AUTHORED(output_element e) cannot be inferred from prompt_detail alone.

It requires tracing e to the human/model control record.

TENSION:
The Copyright Office directly considers iterative prompt revision and says repeated rerolling does not by itself increase control over expression. Shambibble’s labor and ingenuity therefore cannot simply be relabeled authorship. The unresolved issue concerns contributions outside repeated textual prompting and the specific expressive elements they determine.

MISSING:
Case-level evidence applying Part 2’s framework to workflows that use reference-image banks, masks, external compositing, direct manipulation, or multimodal controls rather than text prompting alone.

BOUNDARY:
This zettel does not conclude that Shambibble’s images or any particular AI-assisted work are copyrightable. Copyrightability remains fact-specific.

CITATION TRAIL:
[[LAW-SHAM-20260817-09]]
→ multimodal operative brief
→ U.S. Copyright Office Part 2
→ “prompts alone” insufficient control
→ expressive inputs and arrangements treated separately
→ legal unit shifts from prompt to provenance of expressive elements

TEST:
Take a documented generative workflow and label every final expressive element by its causal/provenance path: human-authored input, model-generated variation, human selection, human arrangement, human modification, or unresolved. Compare this element-level record with a prompt-only authorship analysis.

PLATFORM:
U.S. copyright law
Midjourney
Generative art
Authorship

LINKS:
[[LAW-SHAM-20260817-09]]
[[LAW-SHAM-20260817-10]]
[[SHAM-20260817-04]]
[[LAW-SHAM-20260817-08]]

BIBTEX:
@report{usco2025part2,
  author={{U.S. Copyright Office}},
  title={Copyright and Artificial Intelligence, Part 2: Copyrightability},
  year={2025},
  month={1},
  url={https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf}
}
@misc{shambibble2022imageprompting,
  author={{Shambibble}},
  title={Image Prompting and--},
  year={2022},
  note={Midjourney community guide; researcher-provided PDF and text copy}
}
