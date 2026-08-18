ZETTEL

ID:
MJ-GC-023-A-A

TITLE:
Grammar has a pixel geometry: syntactic relations leave asymmetric spatial traces inside generated images.

SOURCE:
Raphael Tang, Linqing Liu, Akshat Pandey, Zhiying Jiang, Gefei Yang, Karun Kumar, Pontus Stenetorp, Jimmy Lin, Ferhan Ture — “What the DAAM: Interpreting Stable Diffusion Using Cross Attention” — ACL 2023 — pp. 5644–5659.
URL: https://aclanthology.org/2023.acl-long.310/

PASSAGE:
[PARAPHRASE]
DAAM aggregates cross-attention throughout Stable Diffusion's denoising process into spatial attribution maps for individual words. The authors then compare these maps using ten syntactic dependency relations. For some relations, the attribution region of the syntactic head consistently contains the dependent's region; for other relations, the containment runs in the opposite direction.

RESEARCH OBJECT:
SYNTAX-AS-PIXEL-GEOMETRY.

LOCAL MOVE:
[[MJ-GC-023-A]] replaced the interviewee's gravitational folk theory with token-pixel attention evolving through diffusion time.

DAAM makes the next move stranger.

The relevant object is not merely:

WORD
→ REGION.

Relations between words also correspond to relations between their spatial attribution maps.

Grammar acquires a measurable geometry inside image generation.

SOURCE TERMS:
“syntax in the pixel space”
“head”
“dependent”
“heat map”
“cross-attention”
“attribution maps”
“dependency relations”

WHAT BECAME STRANGE:
A grammatical dependency is normally invisible.

Here it can be investigated as an overlap or containment relation between regions of an image.

Syntax does not merely precede the picture.

Some syntax appears to leave a spatial footprint in the machinery producing the picture.

QUESTION:
Which syntactic relations reliably induce which geometric relations between token attribution maps?

DEEPER QUESTION:
Does text-to-image generation partially compile grammatical relations into spatial organization, or are these geometric correspondences only side effects of learned correlations?

MECHANISM:
PROMPT TOKENS
→ cross-attention during denoising
→ token-level spatial attribution maps.

External syntactic analysis gives:

HEAD h
→ DEPENDENT d.

Observed map relation can then be tested:

MAP(h) contains MAP(d)

or

MAP(d) contains MAP(h)

or

neither.

FORMAL SHIFT:
FROM:
TOKEN
→ PIXEL REGION

TO:
SYNTACTIC RELATION(token₁, token₂)
→ RELATION(
    ATTRIBUTION_REGION(token₁),
    ATTRIBUTION_REGION(token₂)
  ).

SOURCE FORMALISM:
[PARAPHRASE]
DAAM upsamples and aggregates cross-attention maps from the denoising module.

The authors evaluate noun segmentation and generalized word attribution, then compare head-dependent attribution-map interactions for ten dependency relations.

They report systematic directionality in map subsumption for some dependency types.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

M(w) = spatial attribution map for word w.

For syntactic dependency:

DEP(h,d).

Define:

CONTAINS(h,d)
when support(M(d)) is substantially nested within support(M(h)).

Then investigate:

DEP_TYPE
→ distribution over
{
CONTAINS(h,d),
CONTAINS(d,h),
OVERLAP,
DISJOINT
}.

Grammar becomes experimentally comparable to geometry.

TENSION:
The analysis finds correlations between linguistic dependency relations and attribution-map structure.

It does not show that Stable Diffusion explicitly constructs a syntactic parse and then converts that parse into geometry.

MISSING:
Minimal-pair experiments where vocabulary is held nearly constant while dependency structure alone changes.

BOUNDARY:
DAAM studies Stable Diffusion.

This cannot establish that Midjourney uses the same internal machinery.

CITATION TRAIL:
[[MJ-GC-023-A]]
→ prompt influence becomes token-pixel attention
→ Tang et al. 2023
→ syntax studied directly “in the pixel space”
→ grammatical dependency acquires spatial signature.

TEST:
Construct minimal prompt pairs using nearly identical words but different grammatical binding.

Example structure:

“a red bird beside a blue dog”

versus a rearrangement designed to alter which adjective modifies which noun.

For each pair:

1. fix seed;
2. generate images;
3. compute DAAM maps;
4. measure containment and overlap among adjective/noun maps;
5. test whether changing grammatical relation predictably changes map geometry.

PLATFORM:
Stable Diffusion / DAAM

LINKS:
[[MJ-GC-023-A]]
[[MJ-GC-022-A]]

BIBTEX:
@inproceedings{tang2023daam,
  title={What the DAAM: Interpreting Stable Diffusion Using Cross Attention},
  author={Tang, Raphael and Liu, Linqing and Pandey, Akshat and Jiang, Zhiying and Yang, Gefei and Kumar, Karun and Stenetorp, Pontus and Lin, Jimmy and Ture, Ferhan},
  booktitle={Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
  pages={5644--5659},
  year={2023},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2023.acl-long.310},
  url={https://aclanthology.org/2023.acl-long.310/}
}
