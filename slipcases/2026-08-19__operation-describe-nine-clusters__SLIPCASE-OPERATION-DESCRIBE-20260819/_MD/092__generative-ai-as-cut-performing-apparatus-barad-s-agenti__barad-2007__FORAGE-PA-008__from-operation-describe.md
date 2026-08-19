ZETTEL

ID: FORAGE-PA-008

TITLE: Generative AI as cut-performing apparatus: Barad's agential cut, itemized, plus Scott's metis test

SOURCE: PAPERS/cyber-00.md section 2 ("Agential Realism: The Cut That Makes the World Appear") and PAPERS/cyber-02.md sections 2, 6 ("Agential Cuts"; "Legibility and Metis")

PASSAGE: [QUOTE, cyber-00] "Generative AI systems perform cuts constantly. A training dataset cuts culture into collectable examples. A tokenizer cuts language into processable fragments. An embedding system cuts meaning into vector relations. A diffusion model cuts noise into image. A content policy cuts permissible from forbidden generation. A prompt cuts possibility into a request. A ranking system cuts better from worse. A user interface cuts visible controls from hidden operations. A benchmark cuts intelligence into measurable performance. A safety layer cuts acceptable creativity from unacceptable risk." [QUOTE, cyber-02] "Generative AI is not dangerous merely because it can be wrong. It is dangerous because it can make its cuts feel natural." [QUOTE, cyber-02] "AI ethics needs a metis test: what situated knowledge is being simplified, and who bears the cost of that simplification?"

RESEARCH OBJECT: The ten-item cut inventory — the most operational artifact in either paper — which translates Barad's intra-action/agential-cut vocabulary into a checklist over the generative pipeline; joined to Scott's legibility critique: "Training data is not the world; it is a legibility regime. Labels are not neutral; they are cuts. Benchmarks are not merely evaluations; they define what counts as performance."

LOCAL MOVE: Pushes ethics upstream of outputs: [QUOTE, cyber-00] "The ethical demand is not simply to judge outputs. It is to become responsible for the apparatuses through which outputs become possible." Accuracy questions "come too late if they only inspect the product after the apparatus has already organized the field of possibility."

SOURCE TERMS: intra-action; agential cut; phenomenon; material-discursive apparatus; ethics of mattering; legibility; metis; cut visibility; "cuts accumulate... defaults become habits, habits become infrastructures of expectation"

WHAT BECAME STRANGE: Neutral-seeming engineering artifacts — tokenizers, benchmarks, ranking functions — reappear as boundary-drawing acts with world-making consequences; "bias" is demoted ("many AI harms arise from the baseline itself," not deviation from it).

QUESTION: Which cuts in the inventory are contestable in practice (policy, prompt) and which are frozen at training time (tokenizer, dataset) — and does responsibility scale with contestability?

DEEPER QUESTION: If every observation is itself a cut (second-order point), what distinguishes a RESPONSIBLE cut from any other — is "cut visibility" a coherent norm, or does exposing cuts just perform another cut?

MECHANISM: Entities don't precede relations; apparatuses enact local separability (subject/object, signal/noise, relevant/irrelevant). Each pipeline stage enacts one such separation; composed, they organize the field of the possible before any output exists. Scott supplies the failure mode: simplification below requisite variety destroys the local knowledge (metis) that actual life depends on; generative AI worsens this because "it does not merely classify; it re-expresses" — producing "the appearance of local knowledge without belonging to the practices that sustain it."

FORMAL SHIFT: From representational evaluation (does output correspond to world?) to constitutive evaluation (what distinctions made this output possible, and who answers for them?).

SOURCE FORMALISM: Barad's agential realism (phenomenon, intra-action, cut) as inherited formalism; the cut inventory as an enumerated list.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Pipeline P = c1 ∘ c2 ∘ ... ∘ cn where each ci: possibility-space → possibility-space is a cut with metadata ⟨what-excluded, who-set-it, mutable?, visible?⟩. Metis test = audit function m(ci) returning (simplified knowledge, cost-bearer). Responsibility ledger = the set of ci with visible=false and cost-bearer ≠ setter.

TENSION: cyber-00 and cyber-02 restate each other almost section-for-section; where they differ: cyber-00 aims at a named synthesis ("agential cybernetic media") with seven commitments and a wider cast (Beer, von Foerster, Deleuze, Ubuntu/Indigenous ontologies, Papert, Nelson), while cyber-02 is leaner, sharpens the interface program ("expose the cut... label epistemic status... make refusal educational"), and coins the stronger aphorisms ("better cuts," "accountable world-centered AI" vs cyber-00's "responsible participation in world-making systems"). cyber-00 keeps a "human-centered is not enough" line; cyber-02 escalates it to "Against Human-Centered Evasion."

MISSING: Any worked example of the metis test applied to one real system; also no engagement with whether cut-exposure is cognitively usable (interface overload).

BOUNDARY: Framework explicitly covers apparatuses in general ("Cameras, simulations, social platforms, maps, robots... state databases all belong to the broader family"); what distinguishes AI is only convergence "in a single apparatus."

CITATION TRAIL: Barad, *Meeting the Universe Halfway* (agential realism, ethics of mattering); Scott, *Seeing Like a State* (legibility, metis); Flusser; Bateson; Beer (requisite variety); von Foerster (increase the number of choices); Deleuze ("Postscript on the Societies of Control"); Ha & Schmidhuber (world models).

TEST: Apply the ten-cut inventory plus metis test to one deployed text-to-image system and one benchmark; check whether harms surfaced by the audit are invisible to output-level bias metrics — the papers' central claim made falsifiable.

PLATFORM: Full generative stack: dataset curation, tokenizer, embeddings, diffusion/LLM, policy layer, ranking, UI, benchmark.

LINKS: [[FORAGE-PA-009]], [[FORAGE-PA-003]], [[FORAGE-PA-006]], [[FORAGE-PA-011]]

BIBTEX: @book{barad2007meeting, author={Barad, Karen}, title={Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning}, publisher={Duke University Press}, year={2007}} @book{scott1998seeing, author={Scott, James C.}, title={Seeing Like a State}, publisher={Yale University Press}, year={1998}} % cyber-00.md and cyber-02.md are unattributed essays; cyber-02 self-describes as generated from a "Lineage Jukebox instruction" and "morphism map".
