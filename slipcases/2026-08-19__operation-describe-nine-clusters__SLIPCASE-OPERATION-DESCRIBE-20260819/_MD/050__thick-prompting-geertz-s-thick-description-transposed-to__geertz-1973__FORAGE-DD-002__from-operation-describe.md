ZETTEL

ID: FORAGE-DD-002

TITLE: Thick prompting: Geertz's thick description transposed to probing model weights

SOURCE: Dry-Dock/BULKHEAD-03_thick-description.md (Part A, Jay); Dry-Dock/PORTUGAL-PAPER-SOURCE.md and 00_PLIMSOLL-LINE/portugal-draft.md (§ Prompting as performance and thick description)

PASSAGE: [QUOTE] "We suggest the term 'thick prompting' to characterize all of these practices, appealing to the anthropologist Clifford Geertz's concept of 'thick description'..." [QUOTE] "Both thick description and thick prompting are seeking to engage with layers of coding. In the case of thick description, it is the layers of cultural coding that overdetermine any practice. In the case of thick prompting, the coding consists of all the semantic layers that have been absorbed into the weights of the model. To prompt is to probe those layers in order to tease out the artifact. Because the models are probabilistic ... the process of interrogating them is always approximate, incomplete, and potentially endless. There is no final perfect prompt." [PARAPHRASE] The move is set against the twentieth-century product-orientation of ekphrasis theory: [QUOTE] "The theory of ekphrasis in the twentieth century emphasized the finished product, the poem, not the process of its making, a well-wrought urn, as critic Cleanth Brooks put it, in a reference to perhaps the most famous English language ekphrasis, Keats' 'Ode on a Grecian Urn.'"

RESEARCH OBJECT: A coined concept — "thick prompting" — that imports an anthropological method (interpretation of layered cultural coding) into HCI-adjacent prompt practice, with a structural mapping: cultural coding : practice :: semantic layers in weights : generated artifact. Its corollary is an anti-teleology of prompting: no terminal prompt exists.

LOCAL MOVE: Reframe iterative prompting (refinement, metaprompting, JSON/scripts/code as prompts) not as engineering optimization but as interpretive description that can never be completed — aligning prompting with the progymnasmata's performance culture against Brooks's finished urn.

SOURCE TERMS: thick description (Geertz 1973); thick prompting; promptcraft; metaprompting (Zhang, Yuan, Yao 2025); progymnasmata; well-wrought urn (Brooks); community of practice.

WHAT BECAME STRANGE: The prompt, normally treated as a command with a right answer, becomes an ethnographic instrument aimed at a culture — except the "culture" is a frozen statistical archive, which raises the question of whether interpretation of a non-agent is interpretation at all.

QUESTION: What exactly is "thick" about a thick prompt — length, structure, layers of constraint, or the interpretive stance of the prompter?

DEEPER QUESTION: Geertz's thickness lives in the interpreter's reconstruction of meaning others already share; a model's weights encode statistics, not meanings — does thick prompting therefore commit a category error, or does it reveal that cultural coding and statistical coding were always closer than the humanities admitted?

MECHANISM: Iterative loop: prompt → artifact → inspection → re-prompt; multimodal escalation (images prompting images, data files, scripts, code as prompts); metaprompting as prompts that generate prompts; all interrogating probabilistic layers that cannot be exhausted.

FORMAL SHIFT: From prompt-as-specification (one-shot, satisfiable) to prompt-as-provisional-description (endless, asymptotic).

SOURCE FORMALISM: Geertz's thin/thick distinction; the twitch/wink example (developed in KEEL BLOCKS/SYNTH-01: "A thick description reconstructs the layered codes ... that make the contraction legible as a wink rather than a twitch. The thickness is not more words. It is more frames.").

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Prompting as a non-converging sequence p_1, p_2, ... with artifacts a_i = G(p_i); thickness(p) = number of independent constraint frames (relation, medium, exclusion, social frame, correction), not |p|; the claim "no final perfect prompt" = for all p there exists a frame f not captured by G(p).

TENSION: READING A (Jay, BULKHEAD-03 Part A): thick means "there is always more to say" — thickness is endless interpretive surplus. READING B (Watson, Part B and SEED-01): "Thick prompting is not about length. It is about pressure" — thickness is organized constraint that defeats defaults. The BULKHEAD-03 STATUS note flags this seam explicitly: Watson's opening "must not feel like a contradiction of Jay's Geertz." The two definitions never get reconciled in any draft.

MISSING: Any actual thick prompt reproduced and analyzed as an object (the paper gestures at JSON/scripts/code prompts but never exhibits one); a criterion distinguishing a thick prompt from a merely long one.

BOUNDARY: The Geertz transfer is licensed only where the model's training data carries cultural coding; for models trained on synthetic or narrow data the analogy loses its object.

CITATION TRAIL: Geertz 1993 [1973] → Brooks (well-wrought urn, uncited in References per STATUS note) → Brosch 2018a/b (digital ekphrasis as performance) → Zhang/Yuan/Yao 2025; Zhao et al. 2024; Ceurstemont 2025 (metaprompting).

TEST: Take one subject, generate with (a) a long unstructured prompt and (b) a short multi-frame constrained prompt; if (b) moves the output further from the platform default, Watson's pressure definition beats Jay's surplus definition.

PLATFORM: Text-to-image and multimodal generators; LLM metaprompting pipelines.

LINKS: [[FORAGE-DD-003]] [[FORAGE-DD-001]] [[FORAGE-DD-005]] [[FORAGE-DD-013]]

BIBTEX: @book{geertz1973interpretation, author={Geertz, Clifford}, title={The Interpretation of Cultures}, publisher={Basic Books}, year={1973}}
