ZETTEL

ID: FORAGE-DD-004

TITLE: Homeric oral-formulaic composition as a probabilistic generative system (analogy, not equivalence)

SOURCE: Dry-Dock/BULKHEAD-04_shield-performance.md; 00_PLIMSOLL-LINE/portugal-draft.md (§ The shield of Achilles as performance and process); developed in KEEL BLOCKS/SYNTH-01_prompters-archive.md (Parry/Lord paragraph)

PASSAGE: [QUOTE] "we propose this analogy (not equivalence): that Homeric oral poetry can itself be thought of as a generative system. The system was evolved over generations by poets who fashioned formulaic epithets that suited the metrical constraints ... The process was not deterministic, but it was probabilistic. No two tellings of Achilles' wrath would be line for line the same, but all of them would evoke that same Homeric world of gods and heroes ... Homer's ekphrasis of the shield was already in this sense produced operatively." [QUOTE from SYNTH-01, citing Parry] the formula is "an expression regularly used under the same metrical conditions to express a given essential idea." [PARAPHRASE] The guard-rails: Homeric composition "could not be fashioned by a deterministic (procedural) algorithm"; the oral theory has been "(mis)interpreted and critiqued as a deterministic explanation."

RESEARCH OBJECT: A genealogical claim that the first ekphrasis was ALREADY operatively produced: the oral tradition functions as a trained generative model (formulae = weighted tokens shaped by metrical constraint; performance = sampling; tellings = non-identical world-consistent outputs). SYNTH-01 pins the analogy's exact scope: "The analogy holds at exactly one level: in both Homeric song and generative AI, output emerges through constrained recombination inside a patterned system of inheritance."

LOCAL MOVE: Convert Parry/Lord's oral-formulaic theory from a philological account of transmission into a systems claim: dactylic hexameter is the constraint set, generations of poets are the training process, and the singer is an inference engine over cultural memory — while explicitly refusing the deterministic reading.

SOURCE TERMS: oral-formulaic theory (Parry, Lord 2018 [1960]); formula; dactylic hexameter; epithet (swift-footed Achilles, wine-dark sea, rosy-fingered dawn, bright-eyed Athena); analogy not equivalence; constrained recombination; composition in performance.

WHAT BECAME STRANGE: "Generative AI" loses its novelty: a probabilistic generative system for world-consistent output is at least as old as archaic Greece — the training corpus was the tradition and the platform was the singer's body.

QUESTION: If Homeric song is a generative system, who or what is the prompter — the audience, the occasion, or the opening invocation of the Muse?

DEEPER QUESTION: What does the disanalogy do for the theory: the drafts insist "only the poet can suffer" the constraints (BULKHEAD-03) — is embodied suffering the single feature that keeps the analogy from collapsing into equivalence, and can that feature carry the whole normative weight placed on it?

MECHANISM: Constraint-shaped vocabulary evolution over generations (epithets fitted to metrical slots) → internalized grammar of habit (Lord's singer "does not move mechanically") → real-time performance generating novel-but-recognizable instantiations of one world.

FORMAL SHIFT: From text-transmission philology (how did the Iliad reach writing?) to generative-systems description (what class of machine is a tradition?).

SOURCE FORMALISM: Parry's formula definition; Lord's composition-in-performance; the drafts' explicit deterministic/probabilistic contrast.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Tradition T = (V, C, W): V formulaic units, C metrical/narrative constraints, W usage weights evolved by selection across performances. A telling is a sample from P(sequence | C, W, occasion). Model claim: distinct tellings s1 ≠ s2 with world(s1) = world(s2) = Homeric world; determinism excluded because P is non-degenerate.

TENSION: READING A (BULKHEAD-04): the analogy dignifies AI generation by giving it a classical pedigree — Homer as proto-operative. READING B (implicit in SYNTH-01's warning): the analogy "should not erase the difference between an embodied singer embedded in a living tradition and a stochastic model trained on scraped corpora" — used carelessly it flattens a living tradition into a dataset. The drafts hold A while footnoting B; the tension is managed, not resolved.

MISSING: Parry is never independently cited (STATUS note: "Parry not separately cited (only via Lord)"); the [citation?] for oral transmission debate is never filled; no engagement with computational Homerists or with statistical analyses of formula distribution that could make the "probabilistic" claim empirical.

BOUNDARY: The analogy is declared to hold "at exactly one level" (constrained recombination); extensions to meaning, intention, or audience relation are explicitly out of bounds.

CITATION TRAIL: Lord 2018 [1960], The Singer of Tales → Parry (formula definition, via SYNTH-01) → Lessing 2022 [1766] (temporal medium) → Taplin 1980.

TEST: Corpus test: measure conditional entropy of formula choice given metrical position in the Iliad; a genuinely probabilistic-but-constrained system predicts mid-range entropy (neither free choice nor slot-filling determinism).

PLATFORM: Oral epic performance as the "platform"; explicit comparanda are diffusion/LLM generators.

LINKS: [[FORAGE-DD-005]] [[FORAGE-DD-003]] [[FORAGE-DD-008]] [[FORAGE-DD-001]]

BIBTEX: @book{lord2018singer, author={Lord, Albert B.}, title={The Singer of Tales}, edition={3}, editor={Elmer, David F.}, publisher={Center for Hellenic Studies}, year={2018}, note={First published 1960}}
