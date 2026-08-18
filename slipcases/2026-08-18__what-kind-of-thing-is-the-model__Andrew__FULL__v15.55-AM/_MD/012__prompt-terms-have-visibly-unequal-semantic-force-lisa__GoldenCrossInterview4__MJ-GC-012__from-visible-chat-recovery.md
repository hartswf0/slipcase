ZETTEL

ID:
MJ-GC-012

TITLE:
Prompt terms have visibly unequal semantic force: “Lisa Frank” strongly reorganizes color.

SOURCE:
GOLD_MJ_Interview_4.wh.GoldenCross_otter_ai 2.pages — Otter.ai transcript — 26:18.

PASSAGE:
[QUOTE]
“if I add the word, Lisa Frank, you know, there's a very clear difference and how that's gonna affect things with the color.”

RESEARCH OBJECT:
UNEQUAL-PROMPT-TERM-FORCE.

LOCAL MOVE:
Against uncertain prompt folklore, the speaker identifies some terms whose intervention produces an apparently obvious output shift.

SOURCE TERMS:
“add the word”
“Lisa Frank”
“very clear difference”
“affect things”
“color”

WHAT BECAME STRANGE:
Words of equal textual size can have radically unequal effects inside the generator.

QUESTION:
What determines the effective force of a prompt token or phrase?

DEEPER QUESTION:
Can a generative model's semantic space be empirically mapped by measuring the magnitude and direction of output changes caused by terms?

MECHANISM:
BASE PROMPT
+ HIGH-FORCE TERM
→ large perceptual displacement in output distribution.

FORMAL SHIFT:
FROM words as descriptive units
TO words as unequal operators over generation.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
FORCE(term)
:= distance(
distribution(output | P),
distribution(output | P + term)
).

TENSION:
The speaker treats the effect as obvious, but obvious perceptual change still does not reveal the model's internal causal machinery.

MISSING:
Repeated comparisons quantifying how consistently “Lisa Frank” changes color and what other features it changes simultaneously.

BOUNDARY:
The passage establishes a perceived output difference, not a measured latent-space force.

CITATION TRAIL:
Transcript 26:18
→ “Lisa Frank”
→ clear color shift
→ later gravitational metaphor for prompt terms.

TEST:
Compare otherwise identical prompt batches with and without “Lisa Frank,” then identify recurrent dimensions of change.

PLATFORM:
Midjourney

LINKS:
[[MJ-GC-011]]
[[MJ-GC-019]]
[[MJ-GC-020]]

BIBTEX:
@misc{GoldenCrossInterview4,
  title = {GOLD MJ Interview 4},
  howpublished = {Otter.ai transcript},
  note = {Uploaded interview transcript; interview date and full speaker metadata not established}
}
