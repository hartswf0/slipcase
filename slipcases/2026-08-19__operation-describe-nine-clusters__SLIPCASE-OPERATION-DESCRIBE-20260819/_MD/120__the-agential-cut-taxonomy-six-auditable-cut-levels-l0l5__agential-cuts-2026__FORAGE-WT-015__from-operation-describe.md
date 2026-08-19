ZETTEL

ID: FORAGE-WT-015

TITLE: The agential cut taxonomy: six auditable cut levels (L0–L5), seven commitments, and the Metis Test

SOURCE: worldtext/syntheses/agential-cuts.md — "The Core Principle", "The Cut Taxonomy", "The Seven Commitments", "The Metis Test", "The Apparatus Audit"

PASSAGE: [QUOTE] "Before any AI system can be evaluated for accuracy, coherence, or beauty, it has already **enacted a world** through these cuts. The agential cut is prior to quality; it is the *condition* of quality." [QUOTE] "**The Apparatus Principle**: A generative system is not a tool that the operator uses. It is an apparatus that operates *on* the operator. The operator's only defense is to make the cuts visible, contestable, and revisable."

RESEARCH OBJECT: A layered audit schema for the exclusions a generative system performs before producing anything: L0 Training Cut (OEM), L1 Architecture Cut (OEM), L2 Policy Cut (OEM/Service Provider), L3 Prompt Cut (Operator), L4 Interface Cut (Service Provider), L5 Interpretation Cut (Operator) — each with a controlling party and an audit question, plus a five-question executable ritual (the Metis Test) and a seven-dimension periodic Apparatus Audit with three-state health indicators.

LOCAL MOVE: The file converts a metaphysical thesis (Barad's agential realism: the cut produces both subject and object) into a compliance instrument — a table you can run down, a ritual with declared inputs and an output block (`metis-assessment` appended to the artifact). Ontology becomes checklist.

SOURCE TERMS: Agential cut; intra-action; apparatus (Flusser); functionary vs. player; legibility and metis (Scott); requisite variety (Beer); modulation/dividual (Deleuze); objects-to-think-with (Papert); Cut Visibility; Choice Amplification; Relational Adequacy; Metis Preservation; Apparatus Literacy; World-Making Accountability; apparatus-manifest.md; "Cuts Made" section.

WHAT BECAME STRANGE: Liability for world-making is distributed along the cut stack: the operator controls only L3 and L5, while L0–L2 and L4 belong to OEM and platform — so most of what a "creative" output excludes was decided by parties absent from the session. The prompt is revealed as the *fourth* cut, not the first.

QUESTION: Commitment 1 demands every cut be "inspectable by the operator... what alternatives were suppressed" — is suppressed-alternative logging even coherent for a stochastic sampler (the unchosen tokens are astronomically many), or must "cuts made" always be a curated fiction of the true exclusion set?

DEEPER QUESTION: Question 4 of the Metis Test splits every simplification into augmentation ("making the world more legible *to the operator*") vs. substitution ("legible *to the system* at the cost of the operator's understanding"). Is this augmentation/substitution polarity decidable at ingest time, or only retrospectively — once epistemic debt has or hasn't materialized — making the test a prophecy rather than a measurement?

MECHANISM: The Metis Test fires "on every major ingest" with five questions: what local knowledge is simplified; who bears the cost; is it reversible; does it serve operator or apparatus; what counter-narrative is suppressed — output scored into a metis-assessment block. The Apparatus Audit scores seven dimensions (training transparency, policy transparency, interface openness, override capacity, metis preservation, provenance depth, ecological awareness) as ✓/⚠/✗.

FORMAL SHIFT: From bias critique (post-hoc, content-level) to cut accounting (structural, level-indexed, party-attributed): the unit of analysis is not the biased output but the located decision that excluded its alternatives.

SOURCE FORMALISM: The six-row L0–L5 table (Cut Type / What It Does / Who Controls It / Audit Question); the Seven Commitments each with named implementation hooks (ritual-cut-visibility, ritual-trail-building, ritual-metis-test, ritual-explanation-gate, apparatus-manifest.md); the refined distinction [QUOTE] "RAG makes invisible cuts; Worldtext makes visible cuts. This is the structural difference."

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] A generation is a composition y = ι ∘ φ₄ ∘ π ∘ φ₂ ∘ φ₁ ∘ φ₀ (x) of level-indexed restriction maps φᵢ, each with an owner ω(φᵢ) ∈ {OEM, Provider, Operator}; auditability(system) = |{i : φᵢ has a recoverable exclusion log}| / 6; the Apparatus Principle asserts a feedback term — the operator at time t+1 is partially a function of φ₄, φ₂ at time t.

TENSION: Commitment 3 requires the operator be able to "override lint, contest policy, inject contradiction," while the Explanation Gate regime (Commitment 7, epistemic-debt.md) monitors operator override rate with "Warning at >30%" — the corpus simultaneously valorizes overriding the apparatus (Flusserian play) and pathologizes it (debt signal). Which overrides are play and which are debt is undecided.

MISSING: Weighting across the seven audit dimensions; what any operator can actually do about L0/L1 findings beyond documentation (the audit can reveal but not repair OEM cuts); an actual apparatus-manifest.md instance in the repo; Scott's question "who bears the cost" has no cost unit.

BOUNDARY: L0–L2 auditing presumes disclosure the OEM does not give; for frontier models the top three rows of the taxonomy are structurally ✗/Unknown, so the instrument's coverage is honest about a territory it cannot enter.

CITATION TRAIL: agential-cuts.md → PAPERS/cyber-00.md, cyber-02.md, cyber-03.md → Barad (agential realism), Flusser (apparatus), Scott (Seeing Like a State's legibility/metis), Beer (requisite variety), Deleuze (societies of control), Papert (constructionism), Bateson (ecology of mind) → worldtext-definitive-theory.md §8 (the Metis Principle) → causal-worldtext-runtime.md (RAG distinction refined).

TEST: Rule-compliance is checkable in-repo: do recent lint reports contain the mandated "Cuts Made" section? Does any ingest log a metis-assessment block? (The synthesis mandates both; their absence is a measurable theory-execution gap on its own terms.)

PLATFORM: Ritual/checklist layer over any worldtext directory; audit table implementable as a scored markdown template.

LINKS: [[FORAGE-WT-014]], [[FORAGE-WT-007]], [[FORAGE-WT-012]], [[FORAGE-WT-016]]

BIBTEX: @unpublished{agential-cuts-2026, title={The Agential Cut Diagnostic}, note={worldtext/syntheses/agential-cuts.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
