ZETTEL

ID:
MJ-GC-018

TITLE:
Underspecified prompts fall toward defaults: escaping model priors requires adding difference.

SOURCE:
GOLD_MJ_Interview_4.wh.GoldenCross_otter_ai 2.pages — Otter.ai transcript — 1:04:46.

PASSAGE:
[QUOTE]
“some of those biases you really have to overcome.”

[QUOTE]
“If you don't ask for what you want, it's just going to fall into the same defaults”

[QUOTE]
“if you just ask for, you know, a castle on top of a hill, there's only so much randomness that's built into those words, where unless you add more things to it, it's always going to look kind of the same.”

RESEARCH OBJECT:
SPECIFICATION-AS-ESCAPE-FROM-MODEL-DEFAULT.

LOCAL MOVE:
Prompt detail does more than describe desired content. It functions as force applied against high-probability defaults.

SOURCE TERMS:
“biases”
“overcome”
“fall into”
“same defaults”
“castle on top of a hill”
“add more things”

WHAT BECAME STRANGE:
Silence is not neutral. What the user fails to specify is filled by the model's learned defaults.

QUESTION:
Which omitted dimensions are most strongly filled by Midjourney defaults?

DEEPER QUESTION:
Does effective prompting require not only saying what one wants but actively counter-specifying what the model would otherwise assume?

MECHANISM:
LOW SPECIFICATION
→ model prior dominates
→ recurrent default.

ADDITIONAL CONSTRAINT
→ reduced/default-shifted output space.

FORMAL SHIFT:
FROM specification as description
TO specification as resistance to prior.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
OUTPUT ≈ PRIOR when PROMPT_INFORMATION is low.

As PROMPT_CONSTRAINT increases,
relative influence of some defaults can decrease.

TENSION:
Adding more prompt information may escape one default while introducing other strong semantic attractors.

MISSING:
Which kinds of additions diversify output versus merely replace one default with another.

BOUNDARY:
The source speaks phenomenologically about “defaults”; it does not identify specific training-data or architectural causes.

CITATION TRAIL:
Transcript 1:04:46
→ “fall into the same defaults”
→ castle-on-hill example
→ prompt detail as escape mechanism.

TEST:
Generate repeated batches from progressively specified versions of one simple prompt and measure which visual dimensions diversify.

PLATFORM:
Midjourney

LINKS:
[[MJ-GC-017]]
[[MJ-GC-019]]
[[MJ-GC-021]]

BIBTEX:
@misc{GoldenCrossInterview4,
  title = {GOLD MJ Interview 4},
  howpublished = {Otter.ai transcript},
  note = {Uploaded interview transcript; interview date and full speaker metadata not established}
}
