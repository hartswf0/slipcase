ZETTEL

ID: FORAGE-WT-012

TITLE: The Causal Worldtext runtime: tripartite raw/schema/wiki architecture, three verbs, and the RAG critique

SOURCE: worldtext/syntheses/causal-worldtext-runtime.md — "Core Thesis", "The Tripartite Directory Architecture", "The Three Verbs", "The Explanation Gate", "RAG vs. Worldtext", "Minimum Viable Executing Ecology"

PASSAGE: [QUOTE] "The worldtext is the **compiled theory** — the theory that the programmer holds, externalized into markdown." [QUOTE] "RAG answers the question: *given a query, what chunks are relevant?* Worldtext answers the question: *given a world, what is true?*"

RESEARCH OBJECT: An engineering specification for a stateful knowledge runtime built from plain markdown: Layer 1 raw/ (immutable evidence — "No AI writes to raw/. No human edits raw/."), Layer 2 CLAUDE.md (slow-mutating schema/governor, "the physical embodiment of the operator's theory"), Layer 3 wiki/ (high-mutability executing ecology with index.md and append-only log.md), operated by exactly three verbs — INGEST, QUERY, LINT — in a closed feedback loop.

LOCAL MOVE: The file defines the *lower bound* of the category: a "Minimum Viable Executing Ecology" — ≥1 raw source, a schema file, index.md, append-only log.md, ≥3 wikilinked pages, and three defined rituals. [QUOTE] "Below this threshold, the system is a note-taking app. Above it, it is an executing ecology." Category membership gets an explicit constructive criterion.

SOURCE TERMS: Causal Worldtext; compiled theory; executing ecology; tripartite architecture; epistemic anchor; schema/governor; Explanation Gate; confidence tags; wikilink traversal; "REQUIRES OPERATOR RULING"; lint-report.md; Minimum Viable Executing Ecology; language as infrastructure.

WHAT BECAME STRANGE: Mutability becomes the organizing dimension of the whole architecture — the three layers are distinguished not by content type but by rate of permissible change (never / slow / continuous), making a knowledge system a stratified geology of write-permissions rather than a database of topics.

QUESTION: The QUERY protocol commands "LLM reads index.md first. Always." and forbids external citations — is index-first traversal actually enforceable on an LLM, and what measures compliance (nothing in the spec observes whether the model really traversed the declared trail)?

DEEPER QUESTION: The RAG table scopes worldtext to "Personal/team scale — <200 documents, 1-10 operators" with theory "Essential — the operator's theory IS the system." Is there a scaling wall at which inhabitation necessarily degrades into retrieval — i.e., is theory-possession bounded by human working memory, making worldtext constitutively small?

MECHANISM: The Explanation Gate: when LINT finds "Page A claims X. Page B claims ¬X. Source in raw/ supports both," the LLM halts automated integration, files the contradiction in wiki/contradictions/, and the operator MUST read both claims, consult raw/, rule definitively, record reasoning, update the wiki — [QUOTE] "This cannot be skipped. This cannot be delegated to AI. This is the anti-epistemic-debt instrument."

FORMAL SHIFT: From knowledge management as storage/search to knowledge management as a runtime with typed layers, a scheduler (lint every N sessions), an interrupt mechanism (the Gate), and a flight recorder (log.md) — note-taking rebuilt as systems engineering.

SOURCE FORMALISM: The three-verb loop diagram (INGEST → QUERY → LINT → "triggers new INGEST if contradictions found"); the eight-step INGEST protocol; the six-step QUERY protocol with the hallucination prohibition ("If the wiki doesn't have the answer, the LLM says so"); the nine-row RAG-vs-Worldtext comparison table (state, infrastructure, cross-reference, contradiction, citations, memory, sweet spot, theory, failure mode); the Minimum Viable Executing Ecology component table.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Runtime = ⟨L₁, L₂, L₃, V⟩ with write-permission lattice w(L₁)=∅, w(L₂)={operator}, w(L₃)={operator, LLM|gated}; V = {ingest, query, lint} where lint ∘ ingest is mandatory-eventually (liveness) and the Gate is a blocking exception: contradiction ⇒ suspend(LLM-writes) until operator-ruling ∈ log. Soundness claim: every L₃ assertion is a theorem of L₁ evidence under L₂ axioms — checkable per claim via its citation.

TENSION: This file's Explanation Gate requires contradictions to be *resolved* by definitive operator ruling; control-surface.md Rule 4 orders the opposite: "Contradictions are not resolved. They are marked as cosmological fault lines. The lint protocol preserves them." The corpus contains both a resolution regime and a preservation regime for the same event class, unreconciled. (A third regime, lore absorption, appears in continuity-debt.md.)

MISSING: Confidence-tag algebra (how tags combine across wikilinks); concurrency (two operators, one wiki); any completion criterion for the closed verb loop (crn.json's "exit conditions" complaint applies to this very diagram); empirical comparison against an actual RAG baseline.

BOUNDARY: The architecture presumes a single honest LLM session that obeys the schema; adversarial or forgetful models break Layer discipline silently, and the spec has no detection for schema non-compliance itself.

CITATION TRAIL: causal-worldtext-runtime.md → Doc 2 "The Machine World: Causal Worldtext, Thick Prompts, and the Epistemology of Continuous AI" → Naur (1985), Bateson (1972) → continuity-debt.md, epistemic-debt.md (the two debts this runtime is designed to prevent) → clean-stack-and-artifact-lifecycle.md.

TEST: Checkable claim: the QUERY discipline ("forbidden from hallucinating external citations") is measurable — sample answers, verify every citation resolves to a wiki page and thence to raw/; the spec predicts 100% resolution, giving a hard compliance metric for any implementation.

PLATFORM: Plain markdown + wikilinks + any schema-reading LLM (CLAUDE.md convention); explicitly no vector database.

LINKS: [[FORAGE-WT-001]], [[FORAGE-WT-007]], [[FORAGE-WT-013]], [[FORAGE-WT-002]]

BIBTEX: @unpublished{causal-worldtext-runtime-2026, title={Causal Worldtext Runtime}, note={worldtext/syntheses/causal-worldtext-runtime.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
