ZETTEL

ID:
MJ-GC-011-A-A

TITLE:
Prompt folklore can be turned into one-word counterfactual surgery: hold the seed fixed, remove one word, and locate the disturbance inside individual attention heads.

SOURCE:
Maisha Maliha and Dean F. Hougen — “Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions” — Findings of ACL 2026 — pp. 25287–25299.
URL: https://aclanthology.org/2026.findings-acl.1265/

PASSAGE:
[PARAPHRASE]
Maliha and Hougen hold the sampling seed fixed while removing individual prompt words to create counterfactual generations. They compare cross-attention before and after the intervention and introduce a head-resolved score that reveals differences among attention heads. Their experiments report token grounding, semantic drift, and head specialization across denoising timesteps.

RESEARCH OBJECT:
ONE-WORD-CAUSAL-SURGERY.

LOCAL MOVE:
[[MJ-GC-011-A]] found that Midjourney itself eventually supplies a seed as a partial experimental control.

The interviewee wanted an experiment capable of distinguishing:

THIS WORD CAUSED THE EFFECT

from

I SAW THE EFFECT AFTER USING THIS WORD.

Maliha and Hougen provide a much stronger version of that experiment in an inspectable diffusion model:

KEEP RANDOM START FIXED.
DELETE ONE WORD.
GENERATE THE COUNTERFACTUAL.
WATCH WHAT CHANGES INSIDE THE MODEL.

SOURCE TERMS:
“controlled prompt interventions”
“removing a single word”
“sampling seed fixed”
“counterfactual generations”
“head-resolved”
“semantic drift”
“head specialization”
“denoising timesteps”

WHAT BECAME STRANGE:
A supposedly vague linguistic ingredient can be surgically ablated like a component in a circuit.

Even stranger:

its causal effect need not be distributed evenly through the model.

Different attention heads and different moments of denoising can respond differently to the missing word.

QUESTION:
Do notorious “magic words” act through a small number of specialized mechanisms, or do they perturb the entire generation process diffusely?

DEEPER QUESTION:
Can prompt craft eventually be decomposed into a causal anatomy in which individual linguistic elements have identifiable WHERE and WHEN signatures inside generation?

MECHANISM:
PROMPT P
+ fixed seed S
→ internal activations A
→ image I.

COUNTERFACTUAL:

P \ {word_i}
+ same seed S
→ activations A'
→ image I'.

Compare:

ΔOUTPUT = I - I'

and

ΔHEAD(h,t)
= change in token contribution
for attention head h
at timestep t.

FORMAL SHIFT:
FROM:
“this phrase seems to work”

TO:
WORD ABLATION
+ RANDOMNESS CONTROL
+ INTERNAL MEASUREMENT
→ CAUSAL LOCALIZATION.

SOURCE FORMALISM:
[PARAPHRASE]
The framework records cross-attention activations throughout UNet denoising and forms token-level spatial grounding maps.

Causal interventions remove one word at a time while retaining the sampling seed.

The authors define a head-resolved spike score from divergence between token-contribution distributions before and after intervention.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For token w:

CAUSAL_SIGNATURE(w)
=
{
OUTPUT_DELTA(w),
SPACE_DELTA(w,x,y),
HEAD_DELTA(w,h),
TIME_DELTA(w,t)
}.

A “magic word” can therefore be tested for:

GLOBAL influence,
LOCAL influence,
EARLY influence,
LATE influence,
or negligible influence.

TENSION:
Cross-attention activation is not automatically equivalent to causal importance.

The paper attempts to strengthen causal faithfulness through controlled deletion, but interpretation of internal components remains model-specific.

MISSING:
Application of the method to prompt folklore terms that users independently believe to possess unusually strong effects.

BOUNDARY:
The source investigates Stable Diffusion.

It cannot tell us what “octane render” does internally inside proprietary Midjourney models.

CITATION TRAIL:
[[MJ-GC-011-A]]
→ seed as imperfect experimental control
→ Maliha & Hougen 2026
→ fixed-seed one-word ablation
→ counterfactual output
→ head- and timestep-resolved disturbance
→ prompt superstition becomes experimentally dissectible.

TEST:
Choose ten historically “magic” visual prompt terms such as rendering/style modifiers.

For each term:

1. insert it into multiple neutral base prompts;
2. lock sampling seed;
3. remove only that term;
4. measure perceptual output difference;
5. compute per-head and per-timestep intervention scores;
6. repeat across seeds.

Classify each term:

NO EFFECT
OUTPUT EFFECT WITHOUT LOCALIZED SIGNATURE
LOCALIZED MECHANISTIC EFFECT
BROAD MECHANISTIC EFFECT.

PLATFORM:
Stable Diffusion / mechanistic interpretability

LINKS:
[[MJ-GC-011-A]]
[[MJ-GC-023-A]]
[[MJ-GC-010]]
[[MJ-GC-011]]

BIBTEX:
@inproceedings{maliha2026mechanistic,
  title={Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions},
  author={Maliha, Maisha and Hougen, Dean F.},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  pages={25287--25299},
  year={2026},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2026.findings-acl.1265},
  url={https://aclanthology.org/2026.findings-acl.1265/}
}
