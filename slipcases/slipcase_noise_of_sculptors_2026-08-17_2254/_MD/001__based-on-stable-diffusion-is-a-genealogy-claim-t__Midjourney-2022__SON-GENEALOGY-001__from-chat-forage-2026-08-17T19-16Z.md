ZETTEL

ID:
SON-GENEALOGY-001

TITLE:
“BASED ON STABLE DIFFUSION” is a genealogy claim the paper has not yet earned.

SOURCE:
Midjourney — “Legacy Features” — official documentation. URL: https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features
Stability AI — “Stable Diffusion Launch Announcement” — August 10, 2022. URL: https://stability.ai/news-updates/stable-diffusion-announcement
Stability AI — “Stable Diffusion Public Release” — August 22, 2022. URL: https://stability.ai/news-updates/stable-diffusion-public-release

PASSAGE:
[QUOTE]
Midjourney’s official retrospective says: “Version 1 was the default model from February 2022 to April 2022.”

[PARAPHRASE]
It dates Version 3 to July–November 2022.

[QUOTE]
Stability AI announced the first researcher release of Stable Diffusion on August 10, 2022.

RESEARCH OBJECT:
GENEALOGICAL DEPENDENCE must be distinguished from participation in the same technical lineage.

LOCAL MOVE:
The parent states that “Versions 1-3 of Midjourney were based on the Stable Diffusion text-to-image model.”

Official timelines make that formulation newly problematic. Midjourney V1 was already operating months before Stable Diffusion’s August 2022 release, and V3 was already the default before the Stable Diffusion researcher release.

This does not prove that Midjourney could not have shared earlier unpublished research, code, personnel, methods, or checkpoints. It means “based on Stable Diffusion” cannot be inherited without evidence.

SOURCE TERMS:
Version 1
Version 3
default model
Stable Diffusion
release
Latent Diffusion Models

WHAT BECAME STRANGE:
The chronology reverses the apparent genealogy.

If Midjourney V1 was already running in February 2022, what exactly could “based on Stable Diffusion” mean?

Possibilities split:

1. direct dependence on Stable Diffusion code or weights
2. dependence on the earlier Latent Diffusion Models research
3. shared dependence on diffusion + CLIP research
4. private pre-release technical exchange
5. merely retrospective similarity

Those are radically different historical claims.

QUESTION:
What primary evidence establishes a direct technical dependency between Midjourney V1–V3 and Stable Diffusion?

DEEPER QUESTION:
If that dependency cannot be established, what is the actual technical genealogy connecting Midjourney, CLIP-guided generation, diffusion models, Latent Diffusion Models, and Stable Diffusion?

MECHANISM:
Chronological falsification pressure.

A claimed derivation must survive:

PRECURSOR EXISTENCE
→ ACCESS
→ TECHNICAL TRANSMISSION
→ IMPLEMENTATION EVIDENCE
→ DESCENDANT SYSTEM

Chronological overlap or architectural resemblance alone supplies none of the middle three steps.

FORMAL SHIFT:
FROM:

Midjourney
→ “based on”
→ Stable Diffusion

TO:

Midjourney
← UNKNOWN TECHNICAL LINEAGE →
{diffusion research, CLIP, LDM, proprietary development, possible collaborators}

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DERIVES_FROM(A, B)

requires at least one evidenced transmission relation:

CODE_FROM(A,B)
OR
WEIGHTS_FROM(A,B)
OR
ARCHITECTURE_FROM(A,B)
OR
DECLARED_DEPENDENCE(A,B)

SIMILAR(A,B) ≠ DERIVES_FROM(A,B)

PRECEDES(A,B) places additional pressure on DERIVES_FROM(A,B).

TENSION:
The parent may be directionally right that Midjourney belongs to the same diffusion-model revolution while being historically wrong about the specific ancestor.

A weaker genealogy may survive even if the stronger one dies.

MISSING:
Primary-source architecture descriptions for Midjourney V1–V3.

Contemporaneous statements by David Holz or Midjourney developers naming CompVis, Rombach et al., Stable Diffusion, Latent Diffusion Models, or specific borrowed implementations.

Code, model-card, checkpoint, collaboration, or acknowledgment evidence.

BOUNDARY:
Release chronology does not prove absence of private access before public release.

This ZETTEL therefore does not conclude that Midjourney was independent of Stable Diffusion. It concludes that the parent’s specific dependency claim remains unverified.

CITATION TRAIL:
[[SCULPTORS-NOISE-CONTROL-2022]]
→ claim that Midjourney V1–V3 were based on Stable Diffusion
→ official Midjourney version chronology
→ official Stable Diffusion release chronology
→ unresolved technical genealogy

TEST:
Search only contemporaneous 2021–2022 primary evidence from Midjourney, David Holz, CompVis, Stability AI, Runway, and named developers.

Search specifically for:

“Midjourney” + “Stable Diffusion”
“Midjourney” + “latent diffusion”
“Midjourney” + “CompVis”
“David Holz” + “Rombach”
“Midjourney architecture”
“Midjourney model” + “CLIP”

Classify every result as:

DIRECT DEPENDENCE
SHARED ANCESTOR
COLLABORATION
RESEMBLANCE
NO EVIDENCE

Do not infer influence from similarity.

PLATFORM:
Midjourney documentation / Stability AI

LINKS:
[[SCULPTORS-NOISE-CONTROL-2022]]

BIBTEX:
@misc{midjourney_legacy_features,
  author = {{Midjourney}},
  title = {Legacy Features},
  howpublished = {Midjourney Documentation},
  url = {https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features},
  note = {Accessed 2026-08-17}
}

@misc{stabilityai_stable_diffusion_launch_2022,
  author = {{Stability AI}},
  title = {Stable Diffusion Launch Announcement},
  year = {2022},
  month = {August},
  url = {https://stability.ai/news-updates/stable-diffusion-announcement}
}

@misc{stabilityai_stable_diffusion_public_2022,
  author = {{Stability AI}},
  title = {Stable Diffusion Public Release},
  year = {2022},
  month = {August},
  url = {https://stability.ai/news-updates/stable-diffusion-public-release}
}
