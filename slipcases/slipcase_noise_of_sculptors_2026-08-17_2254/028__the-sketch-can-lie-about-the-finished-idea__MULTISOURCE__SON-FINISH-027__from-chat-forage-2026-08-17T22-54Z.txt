ZETTEL

ID:
SON-FINISH-027

TITLE:
THE SKETCH CAN LIE ABOUT THE FINISHED IDEA.

SOURCE:
Joshua [ARVR] / Numinous, Discord exchange with cool radio, 12 October 2022; user-provided field transcript and screenshots preserved in this checkpoint. SOURCE URL: NONE — private field archive. Corroborating summary in Sun, Hartsoe & Ottolin, “Sculptors of Noise: Control in Midjourney AI Art Community,” 2022; local PDF preserved in _RESOURCES/.

PASSAGE:
[QUOTE — USER-PROVIDED TRANSCRIPT]
“the only way it sold me is because it was finished.”

[PARAPHRASE]
Joshua says an architectural direction had previously looked too weak in earlier art, but a more finished Midjourney rendering made the direction persuasive. He argues that many designs may fail at the “thumbnail sketch” stage and become discoverable only through more finished exploration.

RESEARCH OBJECT:
EVALUATION ORDER.

LOCAL MOVE:
Generative AI is usually described as making ideation faster or expanding possibility space.

Joshua identifies a different mechanism.

Traditional creative pipelines use cheap, low-resolution representations to decide which possibilities deserve expensive refinement.

If some ideas reveal their value only at higher resolution, the pipeline kills them before they become legible.

Generative AI lowers the cost of appealing that early judgment.

SOURCE TERMS:
finished
thumbnail sketches
more finished exploration
deadends
iterate
hone in

WHAT BECAME STRANGE:
The bottleneck is not only generating an idea.

It is deciding WHEN the idea must stand trial.

A thumbnail is not merely a smaller version of a finished design.

It is an evaluator with its own bias.

QUESTION:
Which valuable ideas are systematically rejected because their virtues do not survive low-resolution representation?

DEEPER QUESTION:
Does generative AI change creativity primarily by expanding what can be imagined, or by changing the stage at which judgment becomes economically possible?

MECHANISM:
Conventional pipeline:

idea
→ cheap representation
→ judgment
→ selective investment
→ finish.

Joshua’s observed pipeline:

idea
→ cheap near-finish
→ judgment
→ revised belief about the idea
→ sustained exploration.

The cost of apparent finish falls before the cost of attention falls.

FORMAL SHIFT:
FROM:

IDEA QUALITY
→ JUDGMENT

TO:

REPRESENTATION RESOLUTION
× IDEA
→ JUDGMENT.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let I be an idea and R_k a representation at resolution k.

J(I,R_k) = creator judgment of I when encountered through R_k.

The pipeline assumes:

J(I,R_low) ≈ J(I,R_high).

Joshua supplies a counterexample where:

J(I,R_low) = REJECT
J(I,R_high) = ADOPT.

TENSION:
Cheap finish can rescue late-legible ideas.

Cheap finish can also make weak ideas look persuasive before they earn attention.

The same mechanism that broadens exploration creates a new selection crisis.

MISSING:
A controlled comparison of judgments made from thumbnails, medium-fidelity prototypes, and generatively finished representations of the same underlying concepts.

Evidence across domains beyond visual concept design.

A measure of false negatives versus false positives introduced by each representation level.

BOUNDARY:
This zettel generalizes from one professional creative director’s reported experience. It does not establish how common the mechanism is across users or domains.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ office-hours question about ceding control
→ Joshua’s magical prompt
→ rejected earlier direction
→ “the only way it sold me is because it was finished”
→ representation resolution becomes part of creative judgment

TEST:
Give expert designers the same candidate concepts in three conditions:

THUMBNAIL
MID-FIDELITY
GENERATIVE NEAR-FINISH.

Require KEEP/KILL judgments at each stage.

Then fully realize every concept regardless of early judgment.

Measure which condition best predicts final expert preference and which valuable concepts each stage falsely kills.

PLATFORM:
Midjourney / professional concept design / creative judgment

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]
[[SON-CURIOSITY-020]]
[[SON-FOLKTHEORY-021]]

BIBTEX:
@unpublished{sun_hartsoe_ottolin_sculptors,
  author = {Zhoujun Sun and Watson Hartsoe and Tommy Ottolin},
  title = {Sculptors of Noise: Control in Midjourney AI Art Community},
  year = {2022},
  note = {CS 6470: Design of Online Communities, Georgia Institute of Technology. User-supplied research paper}
}
