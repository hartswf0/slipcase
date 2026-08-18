ZETTEL

ID:
LAW-SHAM-20260817-10

TITLE:
2026-08-17 — A reference bank preserves identity by making its representations disagree.

SOURCE:
Shambibble, “Image Prompting and--,” Midjourney community guide, 2022, especially the revised recurring-character procedure.

SOURCE URL:
[LOCAL UPLOAD — Midjourney Image Prompting.pdf]

PASSAGE:
[QUOTE]
“The important thing is a couple of recognizably similar faces in different formats so no one medium dominates.”

[PARAPHRASE]
Shambibble says his earlier practice of reusing pencil headshots could contaminate later outputs because “pencil sketch” information traveled with the facial features. His revised practice stored the same character across pencil, digital matte painting, ink outline, and photographic representations.

RESEARCH OBJECT:
CONTROL THROUGH REPRESENTATIONAL DISAGREEMENT.

LOCAL MOVE:
[[SHAM-20260817-04]] treated the recurring-character hack as a missing control surface. The guide reveals the more surprising mechanism. Consistency is not achieved by making every reference identical. It is achieved by preserving what should remain constant across deliberately different representations so that medium-specific features are less able to masquerade as identity.

SOURCE TERMS:
“bank of images”
“same character”
“different formats”
“no one medium dominates”
“smudge your character downstream”

WHAT BECAME STRANGE:
To make one thing persist, Shambibble introduces controlled disagreement around it.

QUESTION:
Can invariance be specified more reliably by showing a model the same entity under deliberately varied irrelevant conditions than by supplying one supposedly perfect reference?

DEEPER QUESTION:
Is the operative analogue of a legal definition sometimes a set of contrasting examples whose intersection, rather than any single example, identifies the intended scope?

MECHANISM:
Generate multiple representations of entity E. Vary medium while preserving identity. Feed several representations together. Features common across references reinforce E. Medium-specific features conflict and may cancel or lose relative influence.

FORMAL SHIFT:
ONE REFERENCE
→ identity + medium contamination

becomes

{E in medium A,
 E in medium B,
 E in medium C,
 E in medium D}
→ intersecting identity signal
+ competing incidental style signals

SOURCE FORMALISM:
The guide describes a practical bank of multiple headshots of one character in different media and explicitly states the purpose: preventing one medium from dominating downstream generations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

identity(E) ≈ features stable across deliberately varied representations of E

TENSION:
This cancellation account is a practitioner explanation, not a verified description of Midjourney’s internal mechanism. Multiple references can also introduce additional noise or shared biases.

MISSING:
Controlled evidence that representational variation isolates identity better than repeated near-duplicate references under otherwise matched conditions.

BOUNDARY:
The source describes a 2022 Midjourney technique. Do not infer that current systems combine references by literal feature intersection.

CITATION TRAIL:
[[SHAM-20260817-04]]
→ recurring character hack
→ revised guide procedure
→ medium contaminates identity
→ deliberate cross-medium disagreement
→ invariance emerges from what survives variation

TEST:
Create matched reference sets for the same synthetic character: one near-duplicate set and one cross-medium set. Hold reference count and prompt constant. Compare identity retention and medium leakage across new scenes.

PLATFORM:
Midjourney
Reference-image prompting
Character consistency

LINKS:
[[SHAM-20260817-04]]
[[LAW-SHAM-20260817-09]]
[[MJ-2022-017]]

BIBTEX:
@misc{shambibble2022imageprompting,
  author={{Shambibble}},
  title={Image Prompting and--},
  year={2022},
  note={Midjourney community guide; researcher-provided PDF and text copy}
}
