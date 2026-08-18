ZETTEL

ID: YELMO-FORAGE-003

TITLE: THE SAME CHARACTER DOES NOT HAVE TO BE STORED ANYWHERE; THE IMAGES CAN MAKE EACH OTHER CONSISTENT

SOURCE: Yoad Tewel, Omri Kaduri, Rinon Gal, Yoni Kasten, Lior Wolf, Gal Chechik, and Yuval Atzmon — “Training-Free Consistent Text-to-Image Generation” — arXiv:2402.03286 — https://arxiv.org/abs/2402.03286

PASSAGE: [PARAPHRASE] ConsiStory generates several images together and makes each generated subject attend to subject regions in the other simultaneously generated images, sharing internal activations during denoising rather than first learning a permanent personalized subject representation.

RESEARCH OBJECT: [[YELMO-FORAGE-001]] treated persistent character identity as something that might have to be stored: a learned embedding, identifier, model adaptation, or other durable representation of Yelmo. ConsiStory reveals a stranger possibility. The system can create apparent persistence without storing a persistent character beforehand. Separate images become consistent because they exchange subject information while they are coming into existence. Identity can therefore be produced as a relation among outputs rather than retrieved from a representation possessed prior to generation.

LOCAL MOVE: Pressure the assumption in [[YELMO-FORAGE-001]] that narrative continuity requires REPRESENTATION(YELMO) to exist before SCENE_1, SCENE_2, and SCENE_3. ConsiStory instead lets the scenes constrain one another during generation.

SOURCE TERMS: training-free consistent generation; cross-frame consistency; subject-driven self-attention; shared attention; internal activations; feature injection; dense correspondence; layout diversity; subject masks

WHAT BECAME STRANGE: [OUR INFERENCE] “The same character” can be an emergent agreement among images. There may be no canonical Yelmo from which every frame descends. Frame A helps determine Yelmo in frame B while frame B simultaneously helps determine Yelmo in frame A. Continuity becomes reciprocal constraint.

QUESTION: If several images become mutually consistent without reference to an independently fixed original, where is the identity they share?

DEEPER QUESTION: Can fictional identity be relational rather than representational: not a stored object copied into scenes, but an invariant negotiated among scenes as they are generated?

MECHANISM: Multiple prompts enter one generation batch → subject regions are localized during denoising → a subject patch in one image can attend to subject information in other images → features propagate across images → correspondence-based feature injection further aligns matching details → images converge toward a shared subject appearance.

FORMAL SHIFT: FROM: IDENTITY → IMAGE_1; IDENTITY → IMAGE_2; IDENTITY → IMAGE_3. TO: IMAGE_1 ↔ IMAGE_2 ↔ IMAGE_3 → MUTUALLY STABILIZED IDENTITY.

SOURCE FORMALISM: ConsiStory extends self-attention so the Query from one generated image can access Keys from subject regions in other generated images. It additionally injects features between corresponding subject patches. The authors counter the resulting loss of layout diversity with dropout and blending from an ordinary non-consistent sampling path.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] {PROMPT_1, PROMPT_2, PROMPT_3} → {NOISY_SCENE_1, NOISY_SCENE_2, NOISY_SCENE_3} → CROSS-SCENE SUBJECT CONSTRAINTS → CO-EMERGENT YELMO → {SCENE_1(Y), SCENE_2(Y), SCENE_3(Y)}

TENSION: Mutual constraint solves persistence but threatens difference. The same information-sharing operation that makes the subject coherent can reduce variation in layout. Narrative continuity and narrative transformation therefore pull against one another inside the mechanism itself.

MISSING: Whether one frame becomes an implicit dominant anchor even when no external canonical image is supplied; when during denoising a stable subject identity first becomes recoverable; whether different generation orders, batch membership, or neighboring prompts change the identity that emerges.

BOUNDARY: ConsiStory establishes visual consistency, not metaphysical numerical identity. Similar-looking subjects across outputs count as consistent under the task even though there is no persistent physical individual passing through time.

CITATION TRAIL: [[YELMO-FORAGE-001]] → persistent representation proposed as condition of storytelling → ConsiStory achieves consistency through shared internal activations without per-subject optimization → next edge: determine whether identity resides in an object, an anchor, or the topology of relations among generated frames

TEST: Generate the same five-scene Yelmo story under four conditions: independent generation; all five frames generated jointly; one designated anchor frame shared with each other frame; and a chain where frame 1 communicates only with 2, 2 with 3, and so on. Compare subject similarity matrices. Then repeat after replacing one scene with a radically different depiction. If identity changes depending on the graph connecting the scenes, persistence is partly a property of the relation structure rather than a fixed character representation.

PLATFORM: CONSISTORY / DIFFUSION SELF-ATTENTION / TRAINING-FREE CONSISTENT IMAGE GENERATION

LINKS: [[YELMO-FORAGE-001]]

BIBTEX: @misc{tewel2024trainingfree, author={Tewel, Yoad and Kaduri, Omri and Gal, Rinon and Kasten, Yoni and Wolf, Lior and Chechik, Gal and Atzmon, Yuval}, title={Training-Free Consistent Text-to-Image Generation}, year={2024}, eprint={2402.03286}, archivePrefix={arXiv}, primaryClass={cs.CV}, doi={10.48550/arXiv.2402.03286}, url={https://arxiv.org/abs/2402.03286}}
