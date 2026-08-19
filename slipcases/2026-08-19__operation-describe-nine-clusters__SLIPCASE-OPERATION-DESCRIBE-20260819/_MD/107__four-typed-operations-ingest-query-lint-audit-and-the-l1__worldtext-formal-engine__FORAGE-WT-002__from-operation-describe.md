ZETTEL

ID: FORAGE-WT-002

TITLE: Four typed operations (INGEST/QUERY/LINT/AUDIT) and the L1–L9 violation taxonomy with numeric thresholds

SOURCE: worldtext/syntheses/worldtext-formal-engine.md — §III "Core Operations" (3.1–3.4)

PASSAGE: [QUOTE] "INGEST : Source × G → G' × Trace × Set<Violation> where G' = G ∪ ΔG and ΔG.sources ∩ G.sources = ∅ (no source duplication)" ... "QUERY : String × G → Answer × Trail × Set<Source> where ∀ citation ∈ Answer.citations : citation ∈ G.sources" ... "LINT : G → Set<(Violation, Severity, Set<Node>)>" ... "AUDIT : Operator × List<Event> → DriftReport × Trace"

RESEARCH OBJECT: A minimal operational calculus for maintaining a knowledge world: every state change and every read is one of four typed operations, and each operation is obligated to emit provenance (Trace) or diagnostics (Violation).

LOCAL MOVE: The file takes verbs from library science and software engineering (ingest, query, lint, audit) and gives each a type signature, an 8-step procedure, and an output contract — turning curation rituals into an API.

SOURCE TERMS: INGEST, QUERY, LINT, AUDIT; Trail; DriftReport; FRAGILE_EXPERT risk; violation types L1 CONTRADICTION, L2 BROKEN_TRAIL, L3 ORPHAN_ENTITY, L4 THIN_DESCRIPTION, L5 DEAD_OPERATION, L6 SEMANTIC_BLEACHING, L7 STALE_SYNTHESIS, L8 MISSING_FORBIDS, L9 SCALE_VIOLATION; thresholds τ_thick, τ_bleach, τ_specific, τ_stale.

WHAT BECAME STRANGE: "Thick description" — Geertz's interpretive category — is here a lintable numeric property: L4 fires when cross_link_density(entity) < τ_thick where τ_thick = 3. Interpretive depth is operationalized as graph degree.

QUESTION: Is cross-link density a valid proxy for thickness, or does it invite Goodharting (adding decorative links to pass L4)?

DEEPER QUESTION: Can hermeneutic qualities (thickness, bleaching, staleness) ever be given non-gameable numeric thresholds, or is every LINT rule for meaning necessarily a proxy that the operator must periodically re-derive?

MECHANISM: LINT detection rules are predicates over graph structure and corpus statistics: e.g. [QUOTE] "L6 SEMANTIC_BLEACHING: ∃ term : frequency(term, G) > τ_bleach ∧ specificity(term) < τ_specific" with [QUOTE] "τ_thick = 3 (minimum cross-links per entity); τ_bleach = 100 (maximum term frequency before flagging); τ_specific = 0.3 (minimum specificity score); τ_stale = 90 (days since last revision)".

FORMAL SHIFT: From editorial judgment ("this entry feels thin") to decidable predicates with declared severities (CRITICAL/HIGH/MEDIUM/LOW) and an explicit anti-hallucination invariant on QUERY: "Answer must cite only nodes in G. No external hallucination."

SOURCE FORMALISM: The four signatures quoted above, plus AUDIT's output record: [QUOTE] "{ query_drift: Set<(Term, Direction)>, vocabulary_change: { gained: Set<Term>, lost: Set<Term> }, source_bias: { overused: Set<Source>, avoided: Set<Source> }, constraint_range: { used: Set<Rule>, unused: Set<Rule> }, diagnosis: String }" and the trigger "If vocabulary_change.lost > vocabulary_change.gained: flag FRAGILE_EXPERT risk".

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] LINT as a family of monotone predicates P_i : G → 2^Violations; the system is "healthy" iff ⋃P_i(G) ∩ {CRITICAL, HIGH} = ∅. AUDIT is a second-order operation: it lints not G but the operator's interaction log with G — LINT : G, AUDIT : Hom(Operator, G).

TENSION: `specificity(term)` is used as if computable (τ_specific = 0.3) but no definition of the specificity function is given anywhere in the file; the taxonomy is decidable only modulo an undefined oracle. Rival reading: the thresholds are rhetorical placeholders that make the *shape* of the check concrete while deferring the metric.

MISSING: No composition laws (is LINT idempotent? does INGEST followed by INGEST of the same source violate the no-duplication clause or no-op?); no rollback/undo operation despite mutable Entity and Rule nodes; the never-defined CORE_OPS enumeration that L5 quantifies over.

BOUNDARY: AUDIT covers only quantifiable drift (terms, counts, coverage); it cannot detect an operator whose vocabulary is stable but whose understanding has hollowed — the case epistemic-debt.md calls "competent without comprehension."

CITATION TRAIL: worldtext-formal-engine.md → seven-failure-modes.md (L1–L9 operationalize Modes 1–6; AUDIT operationalizes Mode 7) → epistemic-debt.md (FRAGILE_EXPERT flag).

TEST: Seed the repo with known violations and measure the file's own declared targets: "Lint catches ≥80% of manually-seeded contradictions (recall)" and "≤20% false contradictions (precision)" (§VII) — a stated, runnable benchmark.

PLATFORM: Any corpus with a term index and link graph; the file gives per-operation complexity targets (incremental lint O(Δ × k), audit O(W) per window).

LINKS: [[FORAGE-WT-001]], [[FORAGE-WT-003]], [[FORAGE-WT-004]], [[FORAGE-WT-007]]

BIBTEX: @unpublished{worldtext-formal-engine-2026, title={Worldtext Formal Engine — Coherence-Preserving Repository Runtime}, note={worldtext/syntheses/worldtext-formal-engine.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
