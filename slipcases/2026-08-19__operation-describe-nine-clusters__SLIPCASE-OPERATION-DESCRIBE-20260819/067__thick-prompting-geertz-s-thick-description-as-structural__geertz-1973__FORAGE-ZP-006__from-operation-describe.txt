ZETTEL

ID: FORAGE-ZP-006

TITLE: Thick prompting: Geertz's thick description as structural (not decorative) theory of prompting a saturated model

SOURCE: Z-Port/final-draft-v2.md §2 (identical core in v3, final-assembled §2); Z-Port/final-draft-v4.md ("Prompting as Performance and Thick Description"); Z-Port/worldtext-after-ekphrasis.md §2; Z-Port/deep-research-report (14).md (Thick prompting bin)

PASSAGE: [QUOTE] "The difference between thin and thick prompting is not length but situated pressure." (final-draft-v2.md §2) [QUOTE] "A thin prompt says: 'Make Achilles' shield.' A thick prompt says: 'Make the shield as a worked bronze world being fabricated scene by scene, not as a fantasy emblem. Let the surface hold sky, city, field, law, dance, harvest, war, and Ocean as an ordered cosmos. Avoid heroic poster composition. Treat the shield as a world-bearing artifact whose scenes imply motion, institutions, labor, ritual, and fate.'" (final-draft-v2.md §2) [QUOTE] "Geertz is useful here because he treats description as an engagement with layered codes rather than as a neutral recording of surface behavior. A wink, a twitch, and a parody of a wink may look similar, but they belong to different symbolic orders." (final-draft-v2.md §2) [QUOTE] "It does not trust the default. It prunes the default." (final-draft-v2.md §2)

RESEARCH OBJECT: The paper's second coined concept, "thick prompting": prompting theorized via Geertz 1973 as negotiation with layered codes. Key structural claim: "Prompting is thick because the system is thick" (watson-sections-final.md) — the model is pre-saturated with "captions, images, styles, genres, metadata, interface defaults, safety constraints, platform habits, and cultural residues," so thin prompts release the default rather than a neutral rendering. Thickness = organized constraint ("what to preserve, what to resist, what to foreground, what to suppress"), explicitly NOT verbosity ("A long prompt can still be thin if it merely piles up adjectives" — worldtext-after-ekphrasis §2).

LOCAL MOVE: Rescue the Geertz analogy from decoration by relocating thickness: it is a property of the model first and of the prompt only in response — turning an anthropological method into an interaction requirement.

SOURCE TERMS: thick prompting; thick description; situated pressure; layered codes; wink/twitch/parody; prune the default; vending machine (thin model of prompting); "the model is already thick"

WHAT BECAME STRANGE: The machine occupies Geertz's position of the culture, not the ethnographer's: the prompter is the fieldworker and the latent space is the field — but a field that answers back with artifacts, so ethnographic description and demiurgic command fuse in one act.

QUESTION: Where exactly does the analogy hold: Geertz's thickness concerns intention and public meaning (the winker means something); model weights carry statistical association without intention — can "symbolic orders" describe distributional structure without category error?

DEEPER QUESTION: If good description of a culture and good instruction to a model turn out to require the same skill (making layered context explicit), is there a general theory of description-as-interface underneath both — and is that the real discovery the paper circles without naming?

MECHANISM: Defaults as learned expectation: "The model fills silence with what it has learned to expect: generic gloss, familiar compositions, inherited clichés, dominant visual styles, and platform-friendly compromises" (v2). A thick prompt adds constraint mass until the output leaves the high-probability basin — cultivation, not command.

FORMAL SHIFT: Prompt quality re-measured: from surface completeness (how much is named) to constraint effectiveness (how far the output moves from the default distribution) — length is decoupled from thickness.

SOURCE FORMALISM: The thin/thick Achilles-shield prompt pair (quoted above) is the operative formalism; v4 adds: thickness "is selected context that changes the act's identity across frames" (watson-sections-final.md).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Thickness(p) ≠ |p|. Thickness(p) ∝ D_KL(P(output|p) ‖ P(output|subject(p))) — the divergence a prompt induces from the model's default distribution for its bare subject. Thin prompt: divergence ≈ 0 (vending machine). Thick prompt: high divergence in targeted dimensions (style, structure, relations) while preserving subject.

TENSION: READING A (v2/v3): Geertz supplies a structural analogy — prompt : model :: thick description : culture; the wink example does real work. READING B (v4/portugal): Geertz supplies mainly a provisionality claim — descriptions are endless, "there is no final perfect prompt"; the symbolic-order machinery is dropped, and Wiener's control signal (cf. Wiener 1948) partially replaces Geertz. The concept's theoretical backbone differs between the Watson and Bolter registers.

MISSING: No engagement with Geertz's critics (thick description as interpretive overreach); no criteria distinguishing a thick prompt from an over-constrained one that merely swaps one cliché set for another; the Orlowski et al. 2025 "thick outputs" citation does the empirical work but is uncited in any bibliography seen.

BOUNDARY: The claim covers prompting of probabilistic generative models; the drafts explicitly contrast this with "the symbolically coded knowledge structures of earlier AI" (v4/portugal), where interrogation would not be endless.

CITATION TRAIL: Geertz 1973 (The Interpretation of Cultures, introductory essay) → Liu & Chilton 2023 (design guidelines from 5,493 generations) → Oppenlaender 2024 (six prompt-modifier types; ethnography) → Lindley & Whitham 2025 ("prompt craft," latent-space navigation) → Zhang, Yuan & Yao 2025 (metaprompting) → Orlowski et al. 2025 ("thick outputs") → Meyer (platform realism) as the reason thickness is necessary.

TEST: Operationalize: hold subject constant, vary prompts along (a) length and (b) constraint structure independently; measure stylistic distance of outputs from the bare-subject default. The thesis predicts (b) not (a) drives the distance.

PLATFORM: Text-to-image platforms generally; Midjourney v6 example (see FORAGE-ZP-007); world-model generators by extension (thick prompting "must begin to specify the conditions under which an environment can persist and change").

LINKS: [[FORAGE-ZP-007]], [[FORAGE-ZP-004]], [[FORAGE-ZP-011]], [[FORAGE-ZP-012]]

BIBTEX: @book{geertz1973interpretation, author = {Geertz, Clifford}, title = {The Interpretation of Cultures}, publisher = {Basic Books}, address = {New York}, year = {1973}}
