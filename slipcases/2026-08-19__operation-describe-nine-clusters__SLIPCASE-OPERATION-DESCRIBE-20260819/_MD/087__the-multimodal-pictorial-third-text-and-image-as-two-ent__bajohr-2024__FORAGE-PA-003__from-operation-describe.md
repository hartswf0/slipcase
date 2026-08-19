ZETTEL

ID: FORAGE-PA-003

TITLE: The multimodal pictorial third: text and image as two entrances into one substrate

SOURCE: PAPERS/bajohr.md (= tenne.md), section 5 "The Multimodal Pictorial Third"

PASSAGE: [QUOTE] "Multimodal AI changes the topology. In models trained across text and image, the relation is not simply one medium representing another. Instead, both are mapped into a shared computational space. Text and image become different entrances into a third field. ... it behaves like a **multimodal pictorial third**: a substrate in which text and image are no longer primary opposites but different surface expressions of an underlying model. ... The border is no longer between poem and painting. The border is between human interpretation and model representation."

RESEARCH OBJECT: The topological claim that ekphrasis's two-term drama (word reaching toward image) is replaced by a three-term structure whose third term is a learned statistical space — "not a human imagination, not a Platonic realm of forms, not a museum of representations."

LOCAL MOVE: Outbids remediation theory: [QUOTE] "Remediation still assumes identifiable media being refashioned through other media. But shared embedding space suggests something more unsettling: not the translation of one medium into another, but the partial suspension of medial difference inside computation."

SOURCE TERMS: multimodal pictorial third; shared embedding space; remediation; ekphrastic hope and fear (Heffernan/Mitchell); suspension of medial difference

WHAT BECAME STRANGE: Lessing's canonical division (temporal language vs spatial image) becomes an interface convention rather than an ontology: "Interfaces still separate input boxes from generated pictures... But at the level of model operation, the distinction has been technically weakened."

QUESTION: In what sense is the third field "pictorial" rather than neutral — does the embedding space privilege image-like structure, or is that an artifact of the generation direction studied?

DEEPER QUESTION: If the operative border is now "between human interpretation and model representation," does every classical inter-media problem (translation, adaptation, ekphrasis, illustration) reduce to one problem — alignment between cultural categories and latent geometry?

MECHANISM: Contrastive training on image-caption pairs places both modalities in one vector space; cross-modal proximity replaces cross-modal representation; text and image become "surface expressions" (decodings) of shared latent points. Media difference persists culturally and legally at the surface while being weakened at the substrate.

FORMAL SHIFT: From a dyadic relation R(word, image) to a mediated triple: word → E ← image, where both project into embedding space E and all crossings are routed through E rather than performed directly.

SOURCE FORMALISM: NONE (the "third" is named and characterized in prose; no diagram or notation).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Media m1, m2 with encoders f1: m1→E, f2: m2→E. Classical ekphrasis ≈ partial map g: m1→m2 with no shared codomain; multimodal condition: g = decode2 ∘ f1. Medial difference "suspends" iff distance in E, not modality tag, predicts generation behavior.

TENSION: cyber-00.md/cyber-02.md would insist the third field is an APPARATUS that performs cuts and carries politics ("What histories does it compress into style?"), whereas bajohr.md treats it primarily as a topological/semiotic fact and defers politics to a paragraph ("Artificial semantics is not innocent"). Same object, different first question: geometry vs responsibility.

MISSING: Empirical grounding — no probing of an actual embedding space; no account of modality gap findings (text and image embeddings occupying separate cones in CLIP space), which would complicate "shared" substrate.

BOUNDARY: The claim is explicitly scoped: text and image "do not disappear culturally"; suspension happens only "at the level of model operation."

CITATION TRAIL: Lessing, *Laocoön*; Heffernan; W.J.T. Mitchell (ekphrastic hope/fear; imagetext); Bolter & Grusin (remediation, argued against); Farocki (operational images, distinguished from); CLIP.

TEST: Measure whether cross-modal nearest neighbors in a real embedding space predict prompt→image behavior better than any modality-internal feature; if yes, the "third field" is doing the causal work the paper assigns it.

PLATFORM: CLIP-family multimodal encoders; DALL-E/Stable Diffusion decoders.

LINKS: [[FORAGE-PA-002]], [[FORAGE-PA-016]], [[FORAGE-PA-008]]

BIBTEX: @article{bajohr2024operative, author={Bajohr, Hannes}, title={Operative ekphrasis: The collapse of the text/image distinction in multimodal {AI}}, journal={Word \& Image}, volume={40}, number={2}, pages={77--90}, year={2024}} % essay in repo is about Bajohr's concept; file authorship unverified.
