ZETTEL

ID:
WWP-20260817-05

TITLE:
Prompting can occur without words: preference itself is becoming executable.

SOURCE:
Midjourney — “Style Creator” — Official Documentation — https://docs.midjourney.com/hc/en-us/articles/41308374558221-Style-Creator — accessed 2026-08-17

PASSAGE:
[QUOTE] The text prompt used for previews “doesn’t guide the Style Creator itself.”

RESEARCH OBJECT:
Style Creator separates language from control: users repeatedly select preferred images, and selected/unselected examples refine a reusable style code. The text prompt can function as a probe for seeing the emerging style rather than the specification of that style.

LOCAL MOVE:
Replace PROMPTING = SAYING WHAT YOU WANT with PROMPTING = DIFFERENTIAL SELECTION AMONG POSSIBILITIES.

SOURCE TERMS:
Style Creator; Style Reference Code; sample styles; selection; refinement rounds; preview; prompt; style

WHAT BECAME STRANGE:
Words can become diagnostic rather than directive. The operative specification emerges from repeated acts of recognition that may never be linguistically articulated.

QUESTION:
What kinds of knowledge are easier to specify through repeated selection than through language?

DEEPER QUESTION:
Does natural-language programming represent only one species of a broader exemplar-programming phenomenon?

MECHANISM:
latent desired quality → candidates → human recognizes preferred instances → select/reject → system updates style representation → new candidates → repeated discrimination → reusable style code.

FORMAL SHIFT:
DESCRIPTION: WORDS → REPRESENTATION becomes OSTENSION: EXAMPLES → HUMAN DISCRIMINATION → LATENT REPRESENTATION.

SOURCE FORMALISM:
Midjourney presents sample images over refinement rounds and constructs a reusable --sref code; documentation distinguishes the preview prompt from the mechanism shaping the style.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
C_t → {LIKE_t, NOT_LIKE_t}; STYLE_t → UPDATE(LIKE_t,NOT_LIKE_t) → STYLE_(t+1).

TENSION:
Social-construction accounts foreground circulating prompt words; preference-trained style codes can make the socially legible linguistic artifact disappear.

MISSING:
Whether users can converge on similar executable styles while using radically different—or no stable—descriptive vocabulary.

BOUNDARY:
The source describes Midjourney Style Creator. “Exemplar programming” is [OUR FORMALIZATION — NOT SOURCE TERMINOLOGY].

CITATION TRAIL:
[[SCGAI-005]] → prompt as cultural operator → [[SCGAI-007]] → socio-technical practice → Style Creator → preference becomes executable → programming-by-example/tacit knowledge.

TEST:
Compare word-only, selection-only, and combined specification of an aesthetic target, then test transfer to unfamiliar subjects and verbalizability of the learned rule.

PLATFORM:
Midjourney Style Creator / generative image systems

LINKS:
[[SCGAI-005]]
[[SCGAI-007]]

BIBTEX:
@misc{midjourney_style_creator, author={{Midjourney}}, title={Style Creator}, howpublished={Midjourney Documentation}, url={https://docs.midjourney.com/hc/en-us/articles/41308374558221-Style-Creator}, note={Accessed 2026-08-17}}
