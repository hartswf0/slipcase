ZETTEL

ID: FORAGE-PT-036

TITLE: A learned cross-modal correspondence is a projection rule, so the collapse thesis has been describing a projection and calling it a shared space

SOURCE: PROGRAMS/opek.json <core_thesis> read against PROGRAMS/mmt.json <central command>; contrastive multimodal training as the mechanism [UNVERIFIED for specific architectures and gap measurements]

PASSAGE: [QUOTE] opek.json: "it [routes] both through <shared artificial semantics>, thereby [weakening] the inherited <text/image distinction> at the level of <technical substrate>" [QUOTE] mmt.json: "Do not ask, 'How does a proposition look like the world?' Ask, 'What disciplined arrangement lets one system be laid against another and tested?'"

RESEARCH OBJECT: A vocabulary transplant that changes what the collapse thesis claims. Contrastive training does not merge two spaces; it learns a correspondence that lets one be laid against the other. That is precisely a disciplined arrangement for testing one system against another — a projection rule in the model-measure sense. The two instruments describe the same mechanism, one as fusion and one as measurement.

LOCAL MOVE: This child supplies the positive term the parent lacked. Where the parent could only say the gap might persist, this says what persistence *means*: alignment is projection, and projection presupposes two things to relate.

SOURCE TERMS: shared artificial semantics / routes / technical substrate / disciplined arrangement / laid against / correspondence

WHAT BECAME STRANGE: Under the projection reading, a persistent modality gap stops being counterevidence and becomes the *precondition*. A projection rule between two identical spaces would be the identity map and would do no work. The collapse thesis therefore needs the gap it is embarrassed by — and its strongest formulation is the one it currently denies: text and image remain distinct and are related by a learned, trainable, revisable rule.

QUESTION: Can the learned cross-modal correspondence be characterised as a projection with an inverse — what can be recovered by going back from image space to text space, and what is lost?

DEEPER QUESTION: If the correspondence is a projection rule, then it is exactly the kind of thing that can be *lost* or *drift*. Model updates change the rule. So a prompt written for one model version is a description under a projection no longer in force — which makes prompt brittleness a projection-maintenance problem rather than a robustness bug.

MECHANISM: <TEXT> -> encoder_t -> region A ; <IMAGE> -> encoder_i -> region B ; [CONTRASTIVE TRAINING LEARNS A CORRESPONDENCE BETWEEN A AND B] -> pairs align while regions remain distinguishable -> [CORRESPONDENCE USED AS PROJECTION] -> <ONE MODALITY LAID AGAINST THE OTHER AND TESTED>

FORMAL SHIFT: <TWO MODALITIES> -> <LEARNED CORRESPONDENCE> -> [PROJECTION AND INVERSE] -> <MEASURABLE RELATION, NOT FUSION>

SOURCE FORMALISM: opek asserts routing through shared semantics; mmt supplies projection-and-contact as the schema. Neither supplies geometry.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Treat the alignment as a map P: A -> B. Report three quantities: residual gap (distance between region centroids after alignment), invertibility (what is recoverable applying P inverse), and drift (change in P across model versions). The collapse thesis predicts gap -> 0; the projection reading predicts gap stays positive while invertibility and drift become the interesting variables.

TENSION: READING A: fusion — one space, and the gap is a training artifact that better methods will close. READING B: projection — two spaces with a learned rule, and the gap is structural, so "collapse" is the wrong word for what happened.

The discriminating measurement is the same for both and nobody has reported it in these terms: track the residual gap across generations while tracking retrieval performance. Rising retrieval with a stable gap supports B decisively.

MISSING: Verified gap measurements. Any characterisation of the inverse. Any study of how the correspondence drifts across versions, which is the practically consequential quantity.

BOUNDARY: This is a reinterpretation of a mechanism, not a measurement of one. Whether contrastive alignment behaves like a projection with a usable inverse is exactly what the test would decide.

CITATION TRAIL: [[FORAGE-PT-009]] and [[FORAGE-PT-008]] -> the projection vocabulary -> alignment as projection -> next: modality-gap measurements (retrieve and verify), and cross-version prompt-brittleness studies read as projection drift.

TEST: For three model versions, measure residual centroid gap, retrieval accuracy, and the stability of the same prompt's output region. Stable gap with improving retrieval falsifies fusion; changing output region across versions with identical prompts measures projection drift and reframes prompt brittleness.

PLATFORM: [[alignment-is-projection]]

LINKS: [[FORAGE-PT-008]] [[FORAGE-PT-009]] [[FORAGE-PT-035]]

BIBTEX: @unpublished{opek_program, title={OPERATIVE_EKPHRASIS_AFTER_AI}, note={PROGRAMS/opek.json, read against PROGRAMS/mmt.json}, year={2026}}
