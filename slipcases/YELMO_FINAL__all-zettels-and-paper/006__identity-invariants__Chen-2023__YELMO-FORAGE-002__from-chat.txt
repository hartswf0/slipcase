ZETTEL

ID: YELMO-FORAGE-002

TITLE: IDENTITY IS THE PART OF THE CHARACTER THAT SURVIVES CHANGING EVERYTHING ELSE

SOURCE: Hong Chen, Yipeng Zhang, Simin Wu, Xin Wang, Xuguang Duan, Yuwei Zhou, and Wenwu Zhu — “DisenBooth: Identity-Preserving Disentangled Tuning for Subject-Driven Text-to-Image Generation” — arXiv:2305.03374 — https://arxiv.org/abs/2305.03374

PASSAGE: [PARAPHRASE] DisenBooth separates information shared across a subject’s images from image-specific information such as pose and background. The shared representation is trained to preserve identity; the image-specific representation carries identity-irrelevant variation.

RESEARCH OBJECT: Yelmo’s mutation problem contains a more fundamental problem than character consistency: what counts as the character at all? DisenBooth operationalizes an answer by decomposing training images into information shared across images and information specific to individual images. Subject identity is assigned to the shared representation; pose, background, and related contingencies are pushed into a separate identity-irrelevant representation. The technical solution therefore makes an implicit ontological claim: the character is what remains invariant when scenes change.

LOCAL MOVE: [[YELMO-FORAGE-001]] asked what must remain invariant for several generated images to count as the same individual. DisenBooth does not merely preserve more details. It creates machinery for deciding which details belong to identity and which may change.

SOURCE TERMS: subject identity; identity-relevant information; identity-irrelevant information; disentangled embedding; textual identity-preserved embedding; visual identity-irrelevant embedding; weak denoising; contrastive embedding

WHAT BECAME STRANGE: [OUR INFERENCE] Character identity becomes an intersection operation. The model is encouraged to call the information common across several images “the subject” and to treat the rest as removable circumstance. But a scarf, scar, crooked tooth, lighting condition, wheelchair, costume, or habitual pose can be either identity or circumstance depending on the reference set. Identity is therefore not simply discovered in the images; the training variation helps manufacture the distinction between essence and accident.

QUESTION: When a generative system separates identity-relevant from identity-irrelevant information, what determines which visual properties become part of the person and which become merely context?

DEEPER QUESTION: Is computational identity an intrinsic representation of a subject, or the residue produced by deliberately varying everything we permit the system to forget?

MECHANISM: Several images of one subject → shared textual representation across all images + image-specific visual representations → objectives discourage the shared representation from encoding every image-specific detail → shared representation captures common information → shared representation alone is used to regenerate the subject under new conditions.

FORMAL SHIFT: FROM: IDENTITY = A COMPLETE DESCRIPTION OF YELMO. TO: IDENTITY = INFORMATION PRESERVED ACROSS A CONTROLLED SET OF TRANSFORMATIONS.

SOURCE FORMALISM: The source defines an identity-preserved embedding f_s = E_T(P_s), shared across the subject images, and separate image-specific identity-irrelevant embeddings f_i. During training they jointly condition denoising; during ordinary subject-driven generation the identity-preserved representation can be used without the image-specific representations.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] IMAGES {YELMO_A, YELMO_B, YELMO_C} → COMMON(YELMO_A,YELMO_B,YELMO_C) = IDENTITY → DIFFERENCE_EACH_IMAGE = CONTEXT → IDENTITY + NEW_CONTEXT → “SAME” YELMO

TENSION: Disentanglement increases editability precisely by deciding that some observed attributes do not define the subject. Yet there is no universal visual boundary between identity and circumstance. If every reference image shows Yelmo wearing the same hat, the shared-information heuristic may promote the hat toward identity; if the hat varies, it may become disposable.

MISSING: A principled account of how identity-relevant ground truth is established; tests involving ambiguous attributes that can legitimately function either as identity markers or changeable context; evidence about how reference-set composition changes the learned identity.

BOUNDARY: DisenBooth operationalizes visual subject identity for image generation. Its identity/irrelevance distinction is an engineering decomposition and should not be mistaken for a general philosophical or psychological theory of personal identity.

CITATION TRAIL: [[YELMO-FORAGE-001]] → character must persist across scenes → DisenBooth separates shared identity from image-specific variation → next edge: deliberately manipulate which properties remain constant in the reference set and observe whether the model comes to treat those properties as constitutive of the subject

TEST: Create an artificial character with six attributes. Across multiple training conditions, hold a different subset invariant while varying the others: hat, eye color, facial mark, body shape, clothing, pose. Train otherwise identical subject representations. Generate the same test scenes and measure which attributes persist. If the system’s notion of identity changes systematically with the invariants of the reference set, identity has been experimentally shown to be partly constructed by the training examples rather than merely recovered from them.

PLATFORM: SUBJECT-DRIVEN TEXT-TO-IMAGE GENERATION / STABLE DIFFUSION / DISENTANGLED PERSONALIZATION

LINKS: [[YELMO-FORAGE-001]]

BIBTEX: @misc{chen2023disenbooth, author={Chen, Hong and Zhang, Yipeng and Wu, Simin and Wang, Xin and Duan, Xuguang and Zhou, Yuwei and Zhu, Wenwu}, title={DisenBooth: Identity-Preserving Disentangled Tuning for Subject-Driven Text-to-Image Generation}, year={2023}, eprint={2305.03374}, archivePrefix={arXiv}, primaryClass={cs.CV}, doi={10.48550/arXiv.2305.03374}, url={https://arxiv.org/abs/2305.03374}}
