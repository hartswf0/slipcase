ZETTEL

ID: PROMPT-FORAGE-001

TITLE: PROMPT EXPERTISE MAY BE APPRENTICESHIP IN A COMMUNITY, NOT KNOWLEDGE OF THE MODEL

SOURCE: Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-to-Image Generation” — Behaviour & Information Technology 43(15), 2024 — https://doi.org/10.1080/0144929X.2023.2286532

PASSAGE: [QUOTE] “Prompt engineering, thus, is iterative and practitioners formulate prompts as probes into the generative models’ latent space.”

RESEARCH OBJECT: The parent treats sophisticated prompting partly as acquiring knowledge of “what the AI knows,” while simultaneously describing expertise as something learned by watching other people’s prompts, comparing results, experimenting, and sharing tricks. Oppenlaender makes that second process analytically central: prompt engineering is an acquired, iterative practice whose working knowledge is accumulated through trial and error, online resources, and community exchange. The important object may therefore not be private knowledge of a model but a socially maintained repertoire for probing an opaque system.

LOCAL MOVE: Pressure the parent’s claim that “knowledge of AI is essential for prompt craft” by distinguishing knowledge of model internals from practical knowledge circulated among practitioners. The parent itself reports both the desire to understand what the AI “knows” and the belief that the best learning occurs by inspecting other people’s prompts.

SOURCE TERMS: prompt engineering; prompt modifiers; subject terms; image prompts; style modifiers; quality boosters; repeating terms; magic terms; iterative experimentation; online community

WHAT BECAME STRANGE: [OUR INFERENCE] A practitioner can become demonstrably better at operating a model while possessing an inaccurate theory of why the successful operations work. Prompt expertise and model understanding can therefore diverge.

QUESTION: What exactly is learned when a prompting community becomes more skilled: properties of the underlying model, stable empirical regularities of an interface, or socially transmitted conventions that happen to work under a particular model version?

DEEPER QUESTION: When an opaque machine is learned collectively through repeated probing, at what point does community practice become an informal experimental science, and at what point does it become folklore?

MECHANISM: Practitioner runs prompt → observes generated image → compares outcome with intention and other practitioners’ outputs → adopts, rejects, or modifies prompt terms → circulates successful modifiers through prompts, guides, databases, and community discussion → other practitioners repeat the cycle.

FORMAL SHIFT: FROM: PROMPT EXPERTISE = KNOWING WHAT THE AI KNOWS. TO: PROMPT EXPERTISE = SOCIALLY ACCUMULATED SKILL IN PROBING AN OPAQUE GENERATIVE SYSTEM.

SOURCE FORMALISM: Oppenlaender identifies six practitioner categories of prompt modifier: subject terms, image prompts, style modifiers, quality boosters, repeating terms, and magic terms. The taxonomy describes practitioner practice rather than an internal grammar of the model.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] COMMUNITY OBSERVATION → HYPOTHESIS ABOUT MODIFIER → PROMPT → OUTPUT → COMPARISON → RETAIN / REVISE / DISCARD → CIRCULATED PRACTICE

TENSION: The parent’s practitioners often speak as though successful prompting reveals the model’s hidden database or weighting logic. Oppenlaender instead documents a practice built from experimentation and communal learning. A rule can therefore be operationally useful without being an accurate causal explanation.

MISSING: Controlled evidence separating robust modifier effects from model-version artifacts, confirmation bias, selective sharing, and post-hoc explanations of successful generations.

BOUNDARY: Oppenlaender’s intensive autoethnographic experimentation used VQGAN–CLIP in 2021, although the paper discusses the broader emerging text-to-image ecosystem. Its findings do not establish the internal mechanism of the Midjourney version represented in the parent material.

CITATION TRAIL: [[PARENT-ZETTEL-ID]] → parent claims about learning from others, prompt ownership, “magic words,” and knowing what the AI knows → Oppenlaender’s ethnography of prompt modifiers → next edge: experimentally distinguish community knowledge that predicts outputs from community explanation that merely rationalizes them

TEST: Extract three concrete rules from the parent—such as moving strongly weighted terms to the end, avoiding “photorealistic,” and substituting corpus-associated phrases. Hold model, seed, parameters, and base prompt constant. Systematically permute only the claimed operation across repeated generations. Measure whether the predicted effect survives replication, semantic paraphrase, and model-version changes. Then compare observed effects with practitioners’ stated explanations.

PLATFORM: VQGAN–CLIP / EARLY TEXT-TO-IMAGE PROMPT COMMUNITIES

LINKS: [[PARENT-ZETTEL-ID]]

BIBTEX: @article{oppenlaender2024taxonomy, author={Oppenlaender, Jonas}, title={A Taxonomy of Prompt Modifiers for Text-to-Image Generation}, journal={Behaviour \& Information Technology}, volume={43}, number={15}, pages={3763--3776}, year={2024}, doi={10.1080/0144929X.2023.2286532}, url={https://doi.org/10.1080/0144929X.2023.2286532}}
