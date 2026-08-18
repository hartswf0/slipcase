ZETTEL

ID:
SHAM-20260817-06

TITLE:
2026-08-17 — Quotation marks turn words from instructions into things the image must contain.

SOURCE:
Shambibble interview transcript — 2022-10-22 — approximately 1:04:50–1:05:53. Midjourney — “Text Generation” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://docs.midjourney.com/hc/en-us/articles/32502277092109-Text-Generation

PASSAGE:
[QUOTE — SHAMBIBBLE]
“I figured out how to do this. I made Nicolas Cage with a speech bubble saying we’re stealing the sham prompts. And the idea is that okay, well, if people see this, it’d be like, how did you do that?”

[QUOTE — CURRENT MIDJOURNEY DOCUMENTATION]
“you can get words or phrases to show up in your images by putting them inside double quotation marks”

RESEARCH OBJECT:
PROMPT LANGUAGE CAN SWITCH BETWEEN INSTRUCTION AND INSCRIPTION.

LOCAL MOVE:
The 2022 trick is historically revealing because generating legible text was itself a hack worth stealing. Current Midjourney makes the distinction explicit: quoted words are treated as text that should appear in the image. A punctuation mark now marks a change in ontological role for language — from control instruction to depicted object.

SOURCE TERMS:
“speech bubble”
“words”
“double quotation marks”
“written”
“text”

WHAT BECAME STRANGE:
The same token sequence can participate in two different layers of the generative act: words that operate on the image and words that are supposed to exist inside the image.

QUESTION:
What mechanisms let a natural-language interface distinguish language-as-command from language-as-content?

DEEPER QUESTION:
Is quotation the simplest instance of a more general problem for generative systems: representing the same symbol both as executable instruction and as inert world material?

MECHANISM:
Unquoted language supplies generative description. Quoted phrase is marked for literal inscription. The model must render symbolic content while also obeying surrounding descriptive language.

FORMAL SHIFT:
WORDS AS CONTROL
→ QUOTATION BOUNDARY
→ WORDS AS WORLD CONTENT

SOURCE FORMALISM:
Current Midjourney documentation instructs users to put desired image text inside double quotation marks and recommends Raw or lower Stylize when exact text is difficult.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A generative prompt contains multiple semantic strata. Delimiters can cast text from one stratum to another: instruction, literal content, reference, parameter, or metadata.

TENSION:
Quotation does not guarantee perfect typography. Current documentation explicitly offers additional controls and editing when text remains inaccurate.

MISSING:
A cross-system taxonomy of delimiters that recast natural language into content rather than instruction.

BOUNDARY:
The current quoted-text feature is not proven to descend historically from Shambibble’s 2022 workaround.

CITATION TRAIL:
Shambibble text hack
→ text becomes a shareable prompt technique
→ current quotation syntax
→ language receives explicit instruction/content boundary
→ connects to [[SHOT-20260817-03]] typed representation

TEST:
Across image, video, code, and agent systems, enumerate cases where identical natural-language material can be either instruction or payload. Test how delimiters, schemas, quoting, escaping, or role separation perform the cast.

PLATFORM:
Midjourney

LINKS:
[[SHOT-20260817-03]]
[[MJ-2022-003]]
[[MJ-2022-010]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
