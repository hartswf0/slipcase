ZETTEL

ID: FORAGE-DD-009

TITLE: The V-M-C mapping: Homer's shield as Ha & Schmidhuber's world-model architecture — with a Controller problem

SOURCE: Dry-Dock/BULKHEAD-06_shield-as-worldtext.md (Part B); Dry-Dock/ARCHIVE/BULKHEAD-02_shield-as-worldtext.md; KEEL BLOCKS/SYNTH-02_shield-as-world-model.md (mapping table); KEEL BLOCKS/SEED-02_shield-as-worldtext-evolved.md

PASSAGE: [QUOTE, BULKHEAD-06 Part B] "Ha and Schmidhuber's architecture comprises three core components: a Vision model that compresses observations into compact latent vectors, a Memory model that predicts future states as probability distributions, and a Controller that maps current vision and memory states to action. Homer's shield anticipates this tripartite structure. The visual descriptions of the metalwork parallel the Vision model, providing the sensory surface. The procedural algorithms of the harvest, the battle, and the trial function as the Memory model, predicting how the environment changes over time. The warrior who carries the shield, or the audience who visualizes it, functions as the Controller." [QUOTE, SYNTH-02 table] Controller = "Hephaestus at the forge: the maker who works inside the system's own representations to construct the world scene by scene," with the Controller "entirely divorced from the 'real' external environment" (Ha & Schmidhuber 2018). [PARAPHRASE] SEED-02 gives a five-row mapping: cosmos→rim boundary = V's compressed latent space; two cities = M's social state transitions (adjudication→feast, ambush→counterattack); agricultural cycle = M's temporal consistency; surface textures = V's probabilistic rendering; the prompt/Hephaestus's hammer = C.

RESEARCH OBJECT: The paper's most original structural contribution (SEED-02's own assessment): a component-by-component isomorphism between the shield's composition and the canonical world-model architecture, making an archaic artifact readable as an engineering diagram — and, crucially, an unresolved disagreement inside the corpus about what the Controller is.

LOCAL MOVE: Refuse the loose "Homer anticipates AI" gesture and instead force a typed mapping: each shield subsystem must land on exactly one architectural component with its function preserved (compression, prediction, policy).

SOURCE TERMS: world model; V-M-C (Vision/Memory/Controller); VAE; MDN-RNN; hallucinated dream (Ha & Schmidhuber 2018); latent vector; boundary initialization; social state transition; temporal consistency.

WHAT BECAME STRANGE: A decorative surface reveals itself as layered infrastructure: the golden vines and silver fish are not the content of the shield but its render pass — "The surfaces ... are generated from the underlying rule system, not the reverse" (SYNTH-02).

QUESTION: Does the mapping survive its own precision — e.g., is the agricultural cycle really prediction (M) rather than mere depiction of cyclical time?

DEEPER QUESTION: Who is the Controller of a worldtext? The corpus gives three incompatible answers — Hephaestus/the maker (SYNTH-02), the warrior/audience who navigates the world (BULKHEAD-06), the prompt itself as Hephaestus's hammer (SEED-02) — and each answer allocates agency, and therefore responsibility, to a different party in generative media.

MECHANISM: V compresses the cosmos into a bounded representation (Ocean at rim as the latent space's edge); M encodes lawful transitions (trial procedure, ambush sequence, plough→harvest→vintage→dance); C acts inside the representation only — which is exactly Ha & Schmidhuber's point about training an agent inside its own dream, and exactly the shield's condition: everything happens on the shield, nothing in the world.

FORMAL SHIFT: From analogy between products (shield ≈ generated world) to isomorphism between architectures (shield's composition ≈ the generator's component graph).

SOURCE FORMALISM: Ha & Schmidhuber 2018 V/M/C decomposition; SYNTH-02's three-column mapping table; SEED-02's five-row mapping table.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Mapping phi: {shield subsystems} → {V, M, C} required to be functional and function-preserving: phi(cosmos+rim)=V, phi(cities+cycle)=M, phi(x)=C where x ∈ {Hephaestus, warrior/audience, prompt} is UNDERDETERMINED — the corpus's three candidate assignments of C are mutually exclusive under a functional mapping, which is the zettel's finding.

TENSION: READING A (BULKHEAD-06): Controller = the warrior/audience — the world model is a pedagogy, "learning to navigate the complexities of mortal life by exploring the world the artifact generates." READING B (SYNTH-02/SEED-02): Controller = Hephaestus/the prompt — the world model is a poietics, the maker acting inside representations. A makes worldtext about reception and inhabitation; B makes it about authorship and control. The drafts never notice they disagree.

MISSING: The entire V-M-C mapping was cut from 00_PLIMSOLL-LINE/portugal-draft.md (only the bare Ha & Schmidhuber definition survives); LeCun 2022 is listed in ARCHIVE citations but never used; no engagement with critiques of the world-model paradigm.

BOUNDARY: The isomorphism is heuristic — Homer's "predictions" are narrated typical sequences, not probability distributions; SEED-02's own audit calls it the paper's "most original structural contribution," not a proof.

CITATION TRAIL: Ha & Schmidhuber 2018 (NeurIPS 31) → Bruce et al. 2024 (Genie 2, DeepMind) → Garcez & Lamb 2023 → Taplin 1980 → Moretti 1996.

TEST: Adversarial mapping: attempt the same V-M-C assignment on a non-world ekphrasis (Keats's urn); if it succeeds equally well, the mapping is unfalsifiable decoration — if it fails (no transition rules, no boundary operator), the shield's specialness is corroborated.

PLATFORM: Genie 2/3 (DeepMind), Marble (World Labs) as the contemporary instances.

LINKS: [[FORAGE-DD-008]] [[FORAGE-DD-010]] [[FORAGE-DD-011]] [[FORAGE-DD-012]]

BIBTEX: @inproceedings{ha2018worldmodels, author={Ha, David and Schmidhuber, J{\"u}rgen}, title={Recurrent World Models Facilitate Policy Evolution}, booktitle={Advances in Neural Information Processing Systems 31}, year={2018}, doi={10.48550/arXiv.1809.01999}}
