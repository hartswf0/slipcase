ZETTEL

ID:
DEFAULT-IMAGES-CHI26-A-1

TITLE:
A generator can represent a concept early in denoising and then forget it before the image is finished.

SOURCE:
Aishwarya Agarwal, Srikrishna Karanam, K J Joseph, Apoorv Saxena, Koustava Goswami, and Balaji Vasan Srinivasan — “A-STAR: Test-time Attention Segregation and Retention for Text-to-image Synthesis” — ICCV 2023 — https://arxiv.org/abs/2306.14544

PASSAGE:
[PARAPHRASE] Agarwal et al. inspect cross-attention during Stable Diffusion generation and report two distinct failures. Different concepts can compete for the same spatial regions, causing one concept to disappear from the final image. More strangely, concepts that are visibly represented in cross-attention during early denoising may cease to be represented strongly enough later in denoising. Their intervention therefore includes an “attention retention” loss intended to preserve concept-specific attention across the generation trajectory.

RESEARCH OBJECT:
Prompt neglect is not necessarily an input-stage failure.

A concept may enter the generative process successfully and still fail to survive execution.

The relevant object is therefore not merely:

WAS CONCEPT C UNDERSTOOD?

but:

FOR HOW LONG DID C REMAIN CAUSALLY PRESENT?

This opens a temporal failure class between comprehension and output:

SEMANTIC EXTINCTION DURING GENERATION.

LOCAL MOVE:
Replace the binary model:

UNDERSTOOD / NOT UNDERSTOOD

with a trajectory:

ACQUIRED
→ LOCATED
→ COMPETES
→ RETAINED / LOST
→ VISIBLE / ABSENT.

SOURCE TERMS:
cross-attention
attention segregation
attention retention
concept overlap
denoising
semantic alignment
ignored concepts

WHAT BECAME STRANGE:
An image generator can apparently “know” about something at timestep t and nevertheless produce an image at timestep T in which that thing never existed.

Failure may therefore occur after representation.

The generator does not merely misunderstand.

It can forget.

QUESTION:
Do Midjourney default images arise because unknown concepts never acquire representation, or because weak concept representations briefly arise and are then extinguished by stronger recurrent motifs during generation?

DEEPER QUESTION:
Could a default image be the visual residue left after requested semantics lose a competition they initially entered?

MECHANISM:
A-STAR observes cross-attention overlap between concepts and declining preservation of concept-specific attention across denoising.

A requested concept can therefore fail through at least two mechanisms:

1. SPATIAL COLLISION:
multiple concepts claim overlapping regions.

2. TEMPORAL ATTRITION:
a concept appears in early attention but is not retained through later denoising.

FORMAL SHIFT:
FROM:

PROMPT
→ REPRESENTATION
→ IMAGE

TO:

PROMPT
→ REPRESENTATION₀
→ REPRESENTATION₁
→ ...
→ REPRESENTATIONₜ
→ IMAGE

where semantic state itself can decay.

SOURCE FORMALISM:
A-STAR introduces two test-time losses:

attention segregation loss
→ reduce spatial overlap between attention maps for distinct concepts

attention retention loss
→ preserve attention information for concepts across denoising timesteps.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For requested concept c, define semantic presence over time:

M_c(t) = measurable concept-specific conditioning / attention at denoising step t.

Static failure:

M_c(0) ≈ 0.

Temporal semantic extinction:

M_c(t₁) > 0
but
M_c(t₂) → 0
for t₂ > t₁.

Final omission therefore does not imply initial non-representation.

A default-image hypothesis becomes:

weak requested concept c
+
strong recurrent motif d

M_c(t) ↓
M_d(t) ↑
→ output dominated by d.

TENSION:
Cross-attention is evidence about internal conditioning behavior, not a transparent readout of “understanding.”

A concept appearing in an attention map does not establish human-like semantic comprehension.

But it is sufficient to destroy the simpler claim that every missing object must have been absent from the computation from the beginning.

MISSING:
A timestep-by-timestep analysis of prompts that actually trigger default images.

Specifically missing is whether the requested unknown term:

never gains attention,

briefly gains attention and loses it,

or never gains interpretable attention while an eventual default motif progressively acquires it.

BOUNDARY:
A-STAR studies compositional failures in inspectable diffusion models, not Midjourney default images.

The temporal-loss mechanism is therefore a candidate mechanism for the parent phenomenon, not its demonstrated cause.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-A]]
→ silent partial interpretation
→ A-STAR cross-attention analysis
→ concepts present early but absent later
→ prompt failure becomes a temporal state-transition problem
→ test default motifs for semantic replacement trajectories.

TEST:
Use an inspectable diffusion model and construct three prompt classes:

known concept
rare but recognized concept
default-triggering or nonce concept.

For each generation, record token-specific cross-attention maps at every denoising step.

Measure:

time of first concept localization
peak attention
attention persistence
time of extinction
time of emergence of recurrent fallback motifs.

The discriminating result is whether default-like outputs exhibit:

ABSENCE FROM START

versus

REPRESENTATION THEN EXTINCTION

versus

REPRESENTATION THEN REPLACEMENT.

PLATFORM:
Stable Diffusion / diffusion-model cross-attention analysis; proposed application to default-image experiments.

LINKS:
[[DEFAULT-IMAGES-CHI26-A]]

BIBTEX:
@inproceedings{Agarwal2023ASTAR,
  author = {Agarwal, Aishwarya and Karanam, Srikrishna and Joseph, K J and Saxena, Apoorv and Goswami, Koustava and Srinivasan, Balaji Vasan},
  title = {A-STAR: Test-time Attention Segregation and Retention for Text-to-image Synthesis},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},
  year = {2023},
  pages = {2283--2293},
  url = {https://arxiv.org/abs/2306.14544}
}
