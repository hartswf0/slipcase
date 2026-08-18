ZETTEL

ID: YELMO-FORAGE-004

TITLE: CHARACTERS KEEP THEIR IDENTITIES BY NOT LOOKING AT EACH OTHER

SOURCE: Huiguo He, Qiuyue Wang, Yuan Zhou, Yuxuan Cai, Hongyang Chao, Jian Yin, and Huan Yang — “Improving Multi-Subject Consistency in Open-Domain Image Generation with Isolation and Reposition Attention” — arXiv:2411.19261 — https://arxiv.org/abs/2411.19261

PASSAGE: [PARAPHRASE] The authors identify “internal attraction” among subjects in diffusion self-attention: information from distinct subjects can interact strongly enough that they converge into a hybrid entity. Their Isolation Attention prevents each subject from referencing the other subjects’ Key and Value features.

RESEARCH OBJECT: An obscure line in the Yelmo notes becomes technically prophetic: when the group tried adding other characters, Yelmo began altering them. A later diffusion paper identifies a mechanism with exactly this morphology. Multiple subjects can exert “internal attraction” through self-attention and fuse into composite characters. The proposed repair is not better description but enforced computational noninteraction between subject regions.

LOCAL MOVE: [[YELMO-FORAGE-001]] asked how multiple persistent identities compose without interference. This source turns interference from a vague failure into a measurable attention phenomenon and supplies an intervention that can selectively remove it.

SOURCE TERMS: multi-subject consistency; internal attraction; subject convergence; subject fusion; Isolation Attention; Reposition Attention; Query; Key; Value; masking; positional influence

WHAT BECAME STRANGE: [OUR INFERENCE] In ordinary language, two characters must interact for a scene to contain a relationship. Inside this generative mechanism, too much representational interaction can literally erase their difference. To produce two characters who visibly interact, the system may need to prevent their internal representations from interacting in precisely the layer responsible for visual coherence.

QUESTION: How can a generative system represent interaction between characters while preventing the machinery representing those characters from collapsing them into one another?

DEEPER QUESTION: Does compositional representation require a protected boundary around each entity before relations among entities can safely be represented?

MECHANISM: Several subjects occupy one target image → self-attention computes responses across image tokens → subject regions respond disproportionately to other subject regions → features bleed across identities → subjects converge toward a composite → Isolation Attention masks cross-subject responses → each subject instead references itself, background, and its own external reference → identities remain more independent.

FORMAL SHIFT: FROM: MORE CONNECTION BETWEEN SUBJECT FEATURES = BETTER COMPOSITION. TO: COMPOSITION REQUIRES SELECTIVE DISCONNECTION SO THAT RELATIONS DO NOT DESTROY RELATA.

SOURCE FORMALISM: In Isolation Attention, the Query for subject i is prevented from referencing the Key and Value features belonging to other subjects in the target image. The undesired cross-subject attention-map responses are masked, while reference information for the corresponding subject remains available.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] YELMO ↔ PIRATE ATTENTION → FEATURE CONTAMINATION → YELMO-PIRATE HYBRID; MASK(YELMO↔PIRATE INTERNAL ATTENTION) + PRESERVE EXTERNAL REFERENCES → YELMO + PIRATE

TENSION: Complete representational isolation would seem hostile to depicting contact, occlusion, shared lighting, exchanged objects, gaze, collision, or touch. The system must therefore maintain entity boundaries while still constructing scene-level relations among those entities.

MISSING: Which attention interactions are necessary for genuine physical and narrative relations between characters; whether isolation causes failures when two subjects touch or overlap; whether identity leakage increases predictably with semantic similarity, spatial proximity, or number of subjects.

BOUNDARY: IR-Diffusion studies particular diffusion architectures and reference-conditioned multi-subject generation. “Internal attraction” is the authors’ name for an attention phenomenon, not evidence of a universal property of generative models.

CITATION TRAIL: [[YELMO-FORAGE-001]] → “we couldn’t add other characters / he would start altering the other characters” → later multi-subject diffusion research identifies subject fusion caused by cross-subject self-attention → Isolation Attention preserves individuality by blocking those responses → next edge: construct an entity-relation architecture in which interaction is represented without representational fusion

TEST: Create two deliberately maximally distinguishable characters and generate them at increasing spatial proximity: separate sides of frame, standing adjacent, holding hands, embracing, wrestling, and partially occluding. Record cross-subject attention and identity fidelity with normal attention and Isolation Attention. Then repeat with visually similar characters. Determine whether the threshold at which interaction becomes identity fusion can be predicted from proximity, similarity, and attention flow.

PLATFORM: IR-DIFFUSION / MULTI-SUBJECT IMAGE GENERATION / SELF-ATTENTION

LINKS: [[YELMO-FORAGE-001]]

BIBTEX: @misc{he2024multisubject, author={He, Huiguo and Wang, Qiuyue and Zhou, Yuan and Cai, Yuxuan and Chao, Hongyang and Yin, Jian and Yang, Huan}, title={Improving Multi-Subject Consistency in Open-Domain Image Generation with Isolation and Reposition Attention}, year={2024}, eprint={2411.19261}, archivePrefix={arXiv}, primaryClass={cs.CV}, doi={10.48550/arXiv.2411.19261}, url={https://arxiv.org/abs/2411.19261}}
